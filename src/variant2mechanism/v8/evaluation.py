"""The v8 evaluation (the testing plan in agent-lab/v8-plan-draft.md): arms, scoring and the planned comparisons.

Arms (all masked except named_given):
  full_given     the full workflow with the gold set's expression context
  full_inferred  the full workflow with the context inferred by code
  noqbic_given   no QBiC-SELEX: candidates from ChIP-seq and expression only
  single         the memory test: the generator alone, with no tools and no evidence
  ablation       full_given without the gold TF's own rows and the papers naming it (uses the label: evaluation only)
  named_given    full_given with the rsID shown and no literature cut-off: the real-use reference
Masked arms cut the literature at the start of the year the case's source paper came out; the workflow only receives
the date. Each arm except single also has a code-only baseline (`code_only`), which makes no model call.
Runs go to <runs_dir>/<arm>/<repeat>/<case_id> (code-only runs to <runs_dir>/code/<arm>/0/<case_id>); a run whose
report.json exists is skipped. A repeat is not a sampling seed: it only changes the model's cache key (reports keep
the old field name `seed` beside `repeat`).
"""

import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from math import comb
from pathlib import Path

import pandas as pd

from ..agent.case import load_gold_case
from ..agent.llm import BudgetExceeded, LLMError
from ..agent.stages.screen import RunStopped
from ..config import REPO, Config, load_config
from ..context.http import Http
from ..evaluation.gold import is_control, load_gold, scoring_tf
from ..evaluation.metrics import resolves_to
from .run import run_case8

log = logging.getLogger(__name__)
ARMS = {"full_given": {"arm": "full", "masked": True, "infer": False},
        "full_inferred": {"arm": "full", "masked": True, "infer": True},
        "noqbic_given": {"arm": "no_qbic", "masked": True, "infer": False},
        "single": {"arm": "single", "masked": True, "infer": False},
        "single_rules": {"arm": "single", "masked": True, "infer": False, "prompts": "rules"},  # the first memory
        #   test, under the v8 generator's rules ("only the evidence you are given"): willingness to answer, not memory
        "ablation": {"arm": "full", "masked": True, "infer": False, "ablation": True},
        "named_given": {"arm": "full", "masked": False, "infer": False, "no_cutoff": True}}
EXPORT = "https://www.ncbi.nlm.nih.gov/research/pubtator3-api/publications/export/biocjson?pmids={pmid}"


def cutoff_date(row: dict, http: Http) -> str | None:
    """1 January of the year the case's source paper came out (TF cases with a PMID only)."""
    if is_control(row):
        return None
    pmid = str(row.get("source_pmid_or_ref", "")).split(";")[0].strip()
    if not pmid.isdigit():
        return None
    r = http.get(EXPORT.format(pmid=pmid), timeout=60)
    docs = r.data.get("PubTator3", []) if r.ok and isinstance(r.data, dict) else []
    year = str(docs[0].get("date", ""))[:4] if docs else ""
    return f"{year}-01-01" if year.isdigit() else None


def run_dir(cfg: Config, arm: str, seed: int, case_id: str, code_only: bool = False) -> Path:
    root = REPO / cfg["v8"]["runs_dir"]
    return (root / "code" / arm / "0" / case_id) if code_only else (root / arm / str(seed) / case_id)


def run_arm(arm: str, cases: list[str] | None = None, repeats: list[int] = (0,), cfg: Config | None = None,
            transport=None, code_only: bool = False, concurrency: int = 4, phase: str = "eval") -> list[dict]:
    cfg = cfg or load_config()
    spec_arm = ARMS[arm]
    if code_only and spec_arm["arm"] == "single":
        raise ValueError("the memory test has no code-only baseline")
    gold = {r["case_id"]: r for r in load_gold(cfg).to_dict("records")}
    cases = cases or list(gold)
    http = Http(cfg.path("tools", "http_cache"))
    jobs, status = [], []
    for seed in ([0] if code_only else repeats):
        for case_id in cases:
            d = run_dir(cfg, arm, seed, case_id, code_only)
            if (d / "report.json").exists():
                status.append({"arm": arm, "case_id": case_id, "repeat": seed, "status": "skipped (done)"})
            else:
                jobs.append((case_id, seed, d))
    stop = False

    def one(case_id, seed, d):
        if stop:
            return {"arm": arm, "case_id": case_id, "repeat": seed, "status": "not run (budget)"}
        row = gold[case_id]
        drop = set()
        if spec_arm.get("ablation") and not is_control(row):
            drop = {scoring_tf(row)}
        before = None if spec_arm.get("no_cutoff") else cutoff_date(row, http)
        try:
            r = run_case8(load_gold_case(case_id, cfg), arm=spec_arm["arm"], masked=spec_arm["masked"], seed=seed,
                          cfg=cfg, transport=transport, run_dir=d, phase=phase, infer=spec_arm["infer"],
                          code_only=code_only, drop=drop, before=before,
                          single_prompts=spec_arm.get("prompts", "memory"))
            return {"arm": arm, "case_id": case_id, "repeat": seed, "status": "ok", "cost_usd": r["cost_usd"],
                    "seconds": r["seconds"]}
        except BudgetExceeded as e:
            return {"arm": arm, "case_id": case_id, "repeat": seed, "status": "budget", "error": str(e)}
        except (RunStopped, LLMError) as e:
            d.mkdir(parents=True, exist_ok=True)
            (d / "error.json").write_text(json.dumps({"error": str(e)}))
            return {"arm": arm, "case_id": case_id, "repeat": seed, "status": "failed", "error": str(e)[:300]}

    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futs = [pool.submit(one, *j) for j in jobs]
        for f in as_completed(futs):
            row = f.result()
            status.append(row)
            log.info("%s", row)
            if row["status"] == "budget":
                stop = True
    return status


# -- scoring ---------------------------------------------------------------------------------------------------------


def targets(row: dict) -> set[str]:
    return {g.strip().upper() for g in str(row.get("target_gene", "")).split(",") if g.strip()} - {"NONE"}


def same_family(reg, a: str | None, b: str | None) -> bool:
    if not a or not b:
        return False
    ga = {g["id"] for g in reg.groups_of_tf(a)}
    return bool(ga & {g["id"] for g in reg.groups_of_tf(b)})


def leaked(report: dict, gold_tf: str | None) -> bool:
    """A paper the run retrieved names the variant and the gold TF together."""
    if not gold_tf:
        return False
    rsid = None
    for e in report.get("evidence", []):
        if e["tool"] == "variant_annotation":
            import re
            m = re.search(r"Known IDs: (rs\d+)", e["summary"])
            rsid = m.group(1) if m else None
    for p in report.get("papers", []):
        if rsid and rsid.lower() in {v.lower() for v in p.get("variants") or []} and gold_tf.upper() in set(
                p.get("genes") or []):
            return True
    return False


def score_run8(report: dict, row: dict, reg, arm: str, code_only: bool) -> dict:
    control = is_control(row)
    gold_tf = None if control else (resolves_to(reg, scoring_tf(row)) or scoring_tf(row))
    out = {"arm": arm, "code_only": code_only, "case_id": report["case_id"], "seed": report["seed"] or 0,
           "control": control, "control_type": row.get("label_class") if control else None,
           "covered": None if control else reg.coverage(gold_tf)["status"] != "not_in_coverage",
           "cost_usd": report["cost_usd"], "seconds": report["seconds"], "model_calls": report["model_calls"],
           "tool_failures": sum(1 for f in report.get("flags", []) if f["flag"] == "tool_failed")}
    if report["arm"] == "single":
        tops = [c["tf"] for c in report.get("single", [])]
        top = resolves_to(reg, tops[0]) if tops else None
        # naming the gold TF itself is a family hit too, also when QBiC-SELEX has no family for it
        out |= {"strict_top1": (top == gold_tf) if gold_tf else None,
                "family_top1": (top == gold_tf or same_family(reg, top, gold_tf)) if gold_tf else None,
                "gold_anywhere": (gold_tf in {resolves_to(reg, t) for t in tops}) if gold_tf else None,
                "top_tf": tops[0] if tops else None}
        return out
    v = report["verdict"]
    ranked = [c for c in report["chains"] if c["rank"] is not None]
    ranked.sort(key=lambda c: c["rank"])
    top = ranked[0] if ranked else None
    top_tf = resolves_to(reg, top["tf"]) if top else None
    fams = report["screen"]["families"]
    overall = v["overall"]["verdict"]
    out |= {"verdict": overall, "tf_line": v["tf"]["verdict"], "disease_line": v["disease"]["state"],
            "top_tf": top["tf"] if top else None, "top_gene": top["target_gene"] if top else None,
            "n_chains": len(report["chains"]), "n_eliminated": len(report["eliminated"]),
            "context": report["context"].get("context"), "context_route": report["context"].get("route"),
            "element": report["element"]["status"], "leak": leaked(report, gold_tf),
            "lookups_run": sum(1 for x in report.get("lookups", []) if x.get("run"))}
    if control:
        out |= {"verdict_correct": overall == "no mechanism", "abstained": overall == "undetermined",
                "overclaim": overall == "mechanism", "tf_line_overclaim": v["tf"]["verdict"] == "mechanism",
                "disease_ok": v["disease"]["state"] in ("no_association", "not_testable")}
        return out
    gid_of = {f["fid"]: f.get("gid") for f in fams}
    groups = {g["id"]: g for g in reg.groups()["groups"]}
    gold_fams = {g["id"] for g in reg.groups_of_tf(gold_tf)} if gold_tf else set()
    fam_rank = next((i for i, f in enumerate(fams, 1) if f.get("gid") in gold_fams), None)
    fam_row = fams[fam_rank - 1] if fam_rank else None
    strict = top_tf == gold_tf
    family = strict or (bool(top) and gid_of.get(top["family_id"]) in gold_fams)
    naming = [c for c in ranked if resolves_to(reg, c["tf"]) == gold_tf]
    elim = [c for c in report["chains"] if c["eliminated"] and resolves_to(reg, c["tf"]) == gold_tf]
    if strict and overall == "mechanism":
        stage = None
    elif strict:
        stage = "verdict"
    elif reg.coverage(gold_tf)["status"] == "not_in_coverage" and report["arm"] == "full":
        stage = "no model"
    elif elim:
        stage = "eliminated"
    elif naming:
        stage = "ranking"
    elif fam_row is None or fam_rank > int(load_config()["v8"]["family"]["top_n"]):
        stage = "screen"
    else:
        stage = "member"
    out |= {"strict_top1": strict, "family_top1": family, "gene_top1": bool(top) and (top["target_gene"] or "").upper()
            in targets(row), "verdict_correct": strict and overall == "mechanism",
            "lenient_correct": family and overall == "mechanism", "abstained": overall == "undetermined",
            "overclaim": None, "gold_family_rank": fam_rank,
            "gold_named_by_code": bool(fam_row) and fam_row["named"] == gold_tf,
            "gold_rank": naming[0]["rank"] if naming else None,
            "disease_ok": v["disease"]["state"] in ("supported", "not_testable"), "failure_stage": stage,
            "group_members": len(groups.get(gid_of.get(top["family_id"]), {}).get("tfs", [])) if top else None}
    return out


def collect(cfg: Config | None = None) -> pd.DataFrame:
    from ..qbic.registry import get_registry
    cfg = cfg or load_config()
    reg = get_registry()
    gold = {r["case_id"]: r for r in load_gold(cfg).to_dict("records")}
    root = REPO / cfg["v8"]["runs_dir"]
    rows = []
    for path in sorted(root.glob("**/report.json")):
        if ".prev-" in str(path):
            continue
        rel = path.relative_to(root).parts
        code_only = rel[0] == "code"
        arm = rel[1] if code_only else rel[0]
        if arm not in ARMS:
            continue
        rep = json.loads(path.read_text())
        if rep["case_id"] in gold:
            rows.append(score_run8(rep, gold[rep["case_id"]], reg, arm, code_only))
    return pd.DataFrame(rows)


def attempts(cfg: Config | None = None) -> pd.DataFrame:
    """Every attempt kept under the runs folder: completed (report.json), failed (error.json and no report), and
    earlier attempts that were run again (their folders renamed <case>.prev-<time>), by arm and runner."""
    cfg = cfg or load_config()
    root = REPO / cfg["v8"]["runs_dir"]
    rows = []
    for path in sorted([*root.glob("**/report.json"), *root.glob("**/error.json")]):
        rel = path.relative_to(root).parts
        code_only = rel[0] == "code"
        if len(rel) != 4 + code_only or rel[code_only] not in ARMS:
            continue
        if path.name == "error.json" and (path.parent / "report.json").exists():
            continue
        rows.append({"arm": rel[code_only], "code_only": code_only, "earlier": ".prev-" in rel[-2],
                     "failed": path.name == "error.json"})
    return pd.DataFrame(rows, columns=["arm", "code_only", "earlier", "failed"])


def share(s) -> float | None:
    s = [x for x in s if x is not None and x == x]
    return round(sum(bool(x) for x in s) / len(s), 3) if s else None


def frac(s) -> str | None:
    """'k/n': how many of the values that are not missing are true."""
    s = [x for x in s if x is not None and x == x]
    return f"{sum(bool(x) for x in s)}/{len(s)}" if s else None


def summary(df: pd.DataFrame, att: pd.DataFrame | None = None) -> pd.DataFrame:
    """One row per arm and runner, as k/n over runs (each repeat counts). TF cases and controls are kept apart;
    family accuracy is over the TF cases whose gold TF QBiC-SELEX covers. With `att` (attempts()), also the attempts:
    completed runs, failures still standing, and failed attempts that were run again."""
    out = []
    for (arm, code), g in df.groupby(["arm", "code_only"]):
        tf, ctl = g[~g.control], g[g.control]
        answered = tf[~tf["abstained"].fillna(False).astype(bool)] if "abstained" in tf else tf
        covered = tf[tf["covered"].fillna(False).astype(bool)] if "covered" in tf else tf
        row = {"arm": arm, "who": "code only" if code else "agent"}
        if att is not None:
            a = att[(att.arm == arm) & (att.code_only == code)]
            row |= {"attempted": len(a), "failed": int((a.failed & ~a.earlier).sum()), "rerun": int(a.earlier.sum())}
        row |= {"runs": len(g), "repeats": g.seed.nunique(), "strict_top1": frac(tf.get("strict_top1", [])),
                "family_top1": frac(covered.get("family_top1", [])), "gene_top1": frac(tf.get("gene_top1", [])),
                "verdict_correct_tf": frac(tf.get("verdict_correct", [])),
                "lenient_correct_tf": frac(tf.get("lenient_correct", [])), "abstain_tf": frac(tf.get("abstained", [])),
                "precision_tf": frac(answered.get("verdict_correct", [])),
                "verdict_correct_controls": frac(ctl.get("verdict_correct", [])),
                "overclaim_controls": frac(ctl.get("overclaim", [])),
                "tf_line_overclaim_controls": frac(ctl.get("tf_line_overclaim", [])),
                "disease_line_ok": frac(g.get("disease_ok", [])), "leaks": int(g.get("leak", pd.Series(
                    dtype=bool)).fillna(False).astype(bool).sum()) if "leak" in g else 0,
                "cost_per_run": round(float(g.cost_usd.mean()), 4),
                "minutes_per_run": round(float(g.seconds.mean() / 60), 2)}
        out.append(row)
    done = {(r["arm"], r["who"]) for r in out}
    for (arm, code), a in (att.groupby(["arm", "code_only"]) if att is not None and len(att) else []):
        if (arm, "code only" if code else "agent") not in done:      # every attempt failed: keep the arm in view
            out.append({"arm": arm, "who": "code only" if code else "agent", "attempted": len(a),
                        "failed": int((a.failed & ~a.earlier).sum()), "rerun": int(a.earlier.sum()), "runs": 0})
    table = pd.DataFrame(out)
    if not len(table):
        return table
    for col in ("attempted", "failed", "rerun", "runs", "repeats", "leaks"):
        if col in table:
            table[col] = table[col].astype("Int64")             # counts stay whole numbers beside an empty row
    return table.sort_values(["arm", "who"], kind="stable").reset_index(drop=True)


def exact_sign_test(wins: int, losses: int) -> float:
    """Two-sided exact sign test on discordant pairs (McNemar exact)."""
    n = wins + losses
    if n == 0:
        return 1.0
    k = min(wins, losses)
    p = sum(comb(n, i) for i in range(0, k + 1)) / 2 ** n
    return round(min(1.0, 2 * p), 4)


def paired(df_a: pd.DataFrame, df_b: pd.DataFrame, metric: str) -> dict:
    """Per case: the mean of `metric` over repeats in each arm; wins, losses and ties of A over B; exact sign test.
    Cases where either arm has no value (a control has no strict_top1) are left out, and `cases` says how many
    remain."""
    a = df_a.groupby("case_id")[metric].apply(lambda s: share(s))
    b = df_b.groupby("case_id")[metric].apply(lambda s: share(s))
    both = [c for c in a.index if c in b.index and pd.notna(a[c]) and pd.notna(b[c])]
    wins = sum(1 for c in both if a[c] > b[c])
    losses = sum(1 for c in both if a[c] < b[c])
    return {"metric": metric, "cases": len(both),
            "a_mean": round(sum(a[c] for c in both) / len(both), 3) if both else None,
            "b_mean": round(sum(b[c] for c in both) / len(both), 3) if both else None,
            "a_better": wins, "b_better": losses, "ties": len(both) - wins - losses,
            "p_sign_test": exact_sign_test(wins, losses),
            "per_case": {c: [a[c], b[c]] for c in both}}
