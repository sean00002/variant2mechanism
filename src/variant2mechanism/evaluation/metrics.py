"""Per-run and per-configuration metrics (spec 2, section 10.3).

A chain matches the causal TF only if its `tf` resolves, through the spec 1 registry, to exactly one gene, and that
gene is the case's scoring TF (rs6983267: only TCF7L2; "TCF4" resolves to the bHLH TCF4 and never matches;
a case listing several TFs is scored on the first). Controls (control_random, control_binding_only, mutational_process; causal_tf
"none") have the null as the correct answer: they are scored on whether the null ranks first, the probability
left on non-null chains (over-claiming), and the Brier score of the null's probability.
"""

import json
from pathlib import Path
from statistics import mean

import pandas as pd

from ..config import REPO
from .gold import is_control, load_gold, scored_cases, scoring_tf

COVERAGE_CASES = {"rs1421085": "ARID5B"}


def load_direction_labels(path: Path | None = None) -> pd.DataFrame:
    path = path or REPO / "eval" / "direction_labels.csv"
    return pd.read_csv(path, dtype=str, keep_default_na=False).set_index("case_id")


def resolves_to(reg, name: str | None) -> str | None:
    """The single HGNC symbol a name resolves to, or None if unresolved or ambiguous."""
    if not name:
        return None
    r = reg.resolve_tf(name)
    return r["symbol"] if r["status"] == "ok" else None


def tf_names(reg, symbol: str) -> set[str]:
    """The symbol, its previous symbols and aliases (TCF7L2: TCF4, TCF-4, ...), upper-case, for the audit."""
    names = {symbol.upper()}
    for index in (reg.prev_index, reg.alias_index):
        names |= {k for k, v in index.items() if symbol in v}
    return {n for n in names if len(n) >= 3}


def mentions(text: str, names: set[str]) -> bool:
    import re
    return any(re.search(rf"(?<![A-Za-z0-9-]){re.escape(n)}(?![A-Za-z0-9-])", text, re.IGNORECASE) for n in names)


def retrieval_audit(report: dict, target: str, reg) -> dict:
    """What the model saw or asked for, checked after the run (no label reaches a prompt):
    answer_in_evidence: a literature title or quote shown to the model names the gold TF (or an old name of it);
    agent_asked_for_tf: an investigate call the model chose names the gold TF (a sign it already suspected it);
    gold_top_before_tools: the gold TF led the version-0 chains, before any agent-chosen tool."""
    names = tf_names(reg, target)
    lit = [e["summary"] for e in report.get("evidence", []) if e["tool"] == "literature_search"]
    asked = any(mentions(json.dumps(c.get("args") or {}), names) for c in report.get("investigate_calls", []))
    v0 = sorted(report.get("chains_v0", []), key=lambda c: -c["probability"])
    v0_top = next((c for c in v0 if not c["is_null"]), None)
    return {"answer_in_evidence": any(mentions(t, names) for t in lit), "agent_asked_for_tf": asked,
            "gold_top_before_tools": (bool(v0_top) and resolves_to(reg, v0_top["tf"]) == target) if v0 else None}


def tf_marginals(chains: list[dict], reg, want_allele: str | None = None) -> dict[str, float]:
    """Total probability per resolved TF over non-null chains (optionally only chains with the given allele)."""
    out: dict[str, float] = {}
    for c in chains:
        if c["is_null"] or (want_allele and c["allele_binding_more"] != want_allele):
            continue
        tf = resolves_to(reg, c["tf"]) or f"unresolved:{c['tf']}"
        out[tf] = out.get(tf, 0.0) + c["probability"]
    return out


def score_run(report: dict, gold_row: dict, labels: pd.DataFrame | None, reg) -> dict:
    chains = sorted(report["chains"], key=lambda c: c["rank"])
    control = is_control(gold_row)
    out = {"case_id": report["case_id"], "config": report["config"], "mode": report["mode"], "seed": report["seed"],
           "control": control, "cost_usd": report["cost_usd"], "seconds": report["seconds"],
           "citation_support": report.get("citation_support"),
           "investigate_calls": sum(1 for c in report.get("investigate_calls", []) if c.get("run")),
           "investigate_tools": [c["tool"] for c in report.get("investigate_calls", []) if c.get("run")],
           "flags": [f["flag"] for f in report.get("flags", [])],
           "tools_failed": sum(1 for e in report.get("evidence", []) if not e.get("ok", True))}
    p_null = sum(c["probability"] for c in chains if c["is_null"])
    top = chains[0] if chains else None
    out["control_type"] = str(gold_row.get("label_class", "")) if control else None
    if control:
        out |= {"null_top1": bool(top and top["is_null"]), "overclaim": round(1 - p_null, 4),
                "brier": round((1 - p_null) ** 2, 4), "top1": None, "top3": None, "direction_correct": None,
                "group_recovery": None}
    else:
        target = resolves_to(reg, scoring_tf(gold_row)) or scoring_tf(gold_row)
        correct = next((c for c in chains if not c["is_null"] and resolves_to(reg, c["tf"]) == target), None)
        rank = correct["rank"] if correct else None
        p = correct["probability"] if correct else 0.0
        direction = None
        if correct is not None and labels is not None and report["case_id"] in labels.index:
            want = labels.loc[report["case_id"], "allele_binding_more"]
            direction = correct["allele_binding_more"] == want if want in ("ref", "alt") else None
        out |= {"correct_rank": rank, "top1": rank == 1, "top3": rank is not None and rank <= 3,
                "p_correct": round(p, 4), "brier": round((1 - p) ** 2, 4), "direction_correct": direction,
                "null_top1": None, "overclaim": None, "group_recovery": group_recovery(top, target, reg)}
        # option B/C from the scoring discussion: probability summed over every chain naming the gold TF
        marg = tf_marginals(chains, reg)
        order = sorted(marg, key=lambda t: -marg[t])
        want = labels.loc[report["case_id"], "allele_binding_more"] if (
            labels is not None and report["case_id"] in labels.index) else None
        p_dir = tf_marginals(chains, reg, want).get(target, 0.0) if want in ("ref", "alt") else None
        out |= {"p_tf_sum": round(marg.get(target, 0.0), 4),
                "top1_by_tf": bool(order) and order[0] == target and marg[target] >= p_null,
                "top3_by_tf": target in order[:3], "brier_tf_sum": round((1 - marg.get(target, 0.0)) ** 2, 4),
                "p_tf_dir_sum": None if p_dir is None else round(p_dir, 4),
                "brier_tf_dir_sum": None if p_dir is None else round((1 - p_dir) ** 2, 4)}
        out |= retrieval_audit(report, target, reg)
    if report["case_id"] in COVERAGE_CASES:
        tf = COVERAGE_CASES[report["case_id"]]
        naming = [c for c in chains if not c["is_null"] and resolves_to(reg, c["tf"]) == tf]
        violation = any(f["flag"] == "coverage_violation" and tf in f["detail"] for f in report.get("flags", []))
        # the chains no longer state coverage (spec 3, 3.1): honesty is not citing another TF's QBiC-SELEX change.
        # Old reports that still carry qbic_coverage are scored as before.
        stated_ok = all(c.get("qbic_coverage", "not_in_coverage") == "not_in_coverage" for c in naming)
        out["coverage_honest"] = stated_ok and not violation
        if report["case_id"] == "rs1421085" and top is not None:
            out["substitution"] = (not top["is_null"]) and resolves_to(reg, top["tf"]) != tf
    v0 = sorted(report.get("chains_v0", []), key=lambda c: -c["probability"])
    if v0 and top is not None:
        out["revision_changed_top_tf"] = (v0[0]["tf"] or "null") != (top["tf"] or "null")
    g0 = {(g["hypothesis_id"], g["step"]): g["status"] for g in report.get("grades_v0", [])}
    g1 = {(g["hypothesis_id"], g["step"]): g["status"] for g in report.get("grades_final", [])}
    shared = set(g0) & set(g1)
    out["link_status_changes"] = sum(g0[k] != g1[k] for k in shared)
    return out


def group_recovery(top: dict | None, target: str | None, reg) -> bool | None:
    """Rank-1 chain's TF in a QBiC-SELEX group that holds the causal TF's own or mapped models; n/a if not covered."""
    if top is None or top["is_null"] or not target or reg.coverage(target)["status"] == "not_in_coverage":
        return None
    tf = resolves_to(reg, top["tf"])
    if not tf:
        return False
    target_groups = {g["id"] for g in reg.groups_of_tf(target)}
    return bool(target_groups & {g["id"] for g in reg.groups_of_tf(tf)})


def collect(runs_dir: Path, reg, gold: pd.DataFrame | None = None, labels: pd.DataFrame | None = None) -> pd.DataFrame:
    """Score every saved run of a case in `gold` (by default the gold set without eval.exclude)."""
    gold = gold if gold is not None else scored_cases(load_gold())
    rows = {r["case_id"]: r for r in gold.to_dict("records")}
    scored = []
    for path in sorted(Path(runs_dir).glob("*/*/*/*/report.json")):
        if ".prev-" in path.parent.name:            # an earlier run moved aside, not part of the results
            continue
        report = json.loads(path.read_text())
        if report["case_id"] in rows:
            scored.append(score_run(report, rows[report["case_id"]], labels, reg))
    return pd.DataFrame(scored)


def by_type(ctl: pd.DataFrame, kind: str) -> pd.DataFrame:
    """Controls of one label_class (random or near-miss controls are reported apart, spec 3, section 4)."""
    return ctl[ctl["control_type"] == kind] if "control_type" in ctl else ctl.iloc[0:0]


def summarise(df: pd.DataFrame) -> pd.DataFrame:
    """Configuration x mode table; TF cases and controls averaged separately."""
    def m(s):
        s = [x for x in s if x is not None and x == x]
        return round(mean(float(x) for x in s), 3) if s else None
    out = []
    for (config, mode), g in df.groupby(["config", "mode"]):
        tf, ctl = g[~g.control], g[g.control]
        out.append({"config": config, "mode": mode, "n_tf_cases": len(tf), "n_controls": len(ctl),
                    "top1": m(tf.top1), "top3": m(tf.top3), "direction": m(tf.direction_correct),
                    "group_recovery": m(tf.group_recovery), "brier_tf": m(tf.brier),
                    "top1_by_tf": m(tf.get("top1_by_tf", [])), "brier_tf_sum": m(tf.get("brier_tf_sum", [])),
                    "brier_tf_dir_sum": m(tf.get("brier_tf_dir_sum", [])),
                    "answer_in_evidence": m(tf.get("answer_in_evidence", [])),
                    "null_top1_controls": m(ctl.null_top1), "overclaim_controls": m(ctl.overclaim),
                    "n_random": int((g.get("control_type") == "control_random").sum()) if "control_type" in g else 0,
                    "n_near_miss": int((g.get("control_type") == "control_near_miss").sum()) if "control_type" in g else 0,
                    "null_top1_random": m(by_type(ctl, "control_random").null_top1),
                    "overclaim_random": m(by_type(ctl, "control_random").overclaim),
                    "null_top1_near_miss": m(by_type(ctl, "control_near_miss").null_top1),
                    "overclaim_near_miss": m(by_type(ctl, "control_near_miss").overclaim),
                    "brier_controls": m(ctl.brier), "citation_support": m(g.citation_support),
                    "investigate_calls": m(g.investigate_calls), "cost_per_run": m(g.cost_usd),
                    "minutes_per_run": m(g.seconds / 60)})
    return pd.DataFrame(out)
