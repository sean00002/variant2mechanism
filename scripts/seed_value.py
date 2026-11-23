"""Three seeds (v7): how much of an answer is noise, and the model's ranking against the pairwise one.

    uv run python scripts/seed_value.py [runs/eval_v7_deepseek runs/eval_v7_luna ...]

Per folder, configuration and mode: how often a case's top answer (the top chain's TF, or the null) and its verdict
change across seeds; seed-averaged scores; and top-1 under the model's probabilities against top-1 under the
tournament's Bradley-Terry ranking on the same runs, with an exact sign-flip test over cases. The verdict is also
recomputed on the pairwise ranking, from the facts and games each report stores. Then one line per case.
"""

import json
import sys
from itertools import product

import pandas as pd

from variant2mechanism.agent.stages.tournament import beats_null
from variant2mechanism.agent.stages.verdict import decide
from variant2mechanism.config import REPO, load_config
from variant2mechanism.evaluation import metrics
from variant2mechanism.evaluation.gold import is_control, load_gold, scored_cases, scoring_tf
from variant2mechanism.qbic.registry import get_registry

FOLDERS = ["runs/eval_v7_deepseek", "runs/eval_v7_luna"]


def answer(chain: dict, reg) -> str:
    return "null" if chain["is_null"] else (metrics.resolves_to(reg, chain["tf"]) or f"?{chain['tf']}")


def right(ans: str | None, row: dict, reg) -> bool | None:
    if ans is None:
        return None
    if is_control(row):
        return ans == "null"
    return ans == (metrics.resolves_to(reg, scoring_tf(row)) or scoring_tf(row))


def sign_flip_p(diffs: list[float]) -> float:
    """Exact two-sided p for the mean of paired differences, flipping the sign of each case's difference."""
    d = [x for x in diffs if x == x and x != 0]
    if not d:
        return 1.0
    obs = abs(sum(d))
    hits = sum(abs(sum(s * x for s, x in zip(signs, d, strict=True))) >= obs - 1e-12
               for signs in product((1, -1), repeat=len(d)))
    return round(hits / 2 ** len(d), 4)


def pairwise_verdict(report: dict, binding: str) -> str | None:
    """The verdict with the chains in the tournament's order instead of the model's."""
    t, v = report.get("tournament"), report.get("verdict")
    if not t or not v:
        return None
    by_id = {c["id"]: c for c in report["chains"]}
    chains = [{"id": i, "is_null": by_id[i]["is_null"], "tf": by_id[i]["tf"],
               "allele": by_id[i].get("allele_binding_more"),
               "links": [{"step": lk["step"], "status": lk.get("status", "missing")} for lk in by_id[i]["links"]]}
              for i in t["ranking"]]
    null = next(c["id"] for c in chains if c["is_null"])
    ok = None if chains[0]["is_null"] else beats_null(t, chains[0]["id"], null)
    return decide(chains, v["facts"], ok, binding)[0]


def verdict_right(v: str | None, top: str | None, row: dict, reg) -> bool | None:
    if v is None:
        return None
    if is_control(row):
        return v == "no mechanism"
    return v == "mechanism" and right(top, row, reg)


def load(folders: list[str], gold: dict, reg, binding: str = "either") -> pd.DataFrame:
    rows = []
    for folder in folders:
        for path in sorted((REPO / folder).glob("*/*/*/*/report.json")):
            if ".prev-" in path.parent.name:
                continue
            r = json.loads(path.read_text())
            g = gold.get(r["case_id"])
            if g is None:
                continue
            chains = sorted(r["chains"], key=lambda c: c["rank"])
            by_id = {c["id"]: c for c in chains}
            t = r.get("tournament")
            llm_top = answer(chains[0], reg)
            pair_top = answer(by_id[t["ranking"][0]], reg) if t else None
            pv = pairwise_verdict(r, binding)
            rows.append({**metrics.score_run(r, g, None, reg), "folder": folder.removeprefix("runs/"),
                         "llm_top": llm_top, "pairwise_top": pair_top, "llm_right": right(llm_top, g, reg),
                         "pairwise_right": right(pair_top, g, reg), "pairwise_verdict": pv,
                         "pairwise_verdict_right": verdict_right(pv, pair_top, g, reg)})
    return pd.DataFrame(rows)


def share(s: pd.Series) -> float | None:
    s = s.dropna()
    return round(float(s.astype(float).mean()), 3) if len(s) else None


def summary(df: pd.DataFrame) -> pd.DataFrame:
    out = []
    for (folder, config, mode), g in df.groupby(["folder", "config", "mode"]):
        per_case = g.groupby("case_id")
        seeds = per_case.size()
        multi = g[g.case_id.isin(seeds[seeds > 1].index)].groupby("case_id")
        llm, pw = per_case["llm_right"].mean(), per_case["pairwise_right"].apply(share)
        v = metrics.verdict_summary(g)
        out.append({"runs": folder, "config": config, "mode": mode, "cases": len(seeds),
                    "seeds per case": f"{seeds.min()}" if seeds.min() == seeds.max() else f"{seeds.min()}-{seeds.max()}",
                    "top answer changes": share(multi["llm_top"].nunique().gt(1)) if len(multi) else None,
                    "verdict changes": share(multi["verdict"].nunique().gt(1)) if len(multi) else None,
                    "right, model ranking": share(llm), "right, pairwise": share(pw),
                    "pairwise vs model p": sign_flip_p((pw - llm).tolist()),
                    "verdict right": v.get("verdict_accuracy"), "answered": v.get("answered"),
                    "right when answered": v.get("accuracy_answered"),
                    "mechanism at controls": v.get("verdict_overclaim_controls"),
                    "verdict right, pairwise order": share(g.pairwise_verdict_right),
                    "answered, pairwise order": share(g.pairwise_verdict.dropna() != "undetermined"),
                    "cost per run": round(float(g.cost_usd.mean()), 4)})
    return pd.DataFrame(out)


def per_case(df: pd.DataFrame) -> pd.DataFrame:
    out = []
    for (folder, config, mode, case), g in df.sort_values("seed").groupby(["folder", "config", "mode", "case_id"]):
        out.append({"runs": folder, "config": config, "mode": mode, "case": case,
                    "control": "yes" if g.control.iloc[0] else "",
                    "model top, by seed": ", ".join(g.llm_top), "pairwise top": ", ".join(map(str, g.pairwise_top)),
                    "verdicts": ", ".join(map(str, g.verdict)),
                    "verdicts, pairwise order": ", ".join(map(str, g.pairwise_verdict))})
    return pd.DataFrame(out)


def main(folders: list[str]) -> None:
    cfg = load_config()
    reg = get_registry()
    gold = {r["case_id"]: r for r in scored_cases(load_gold(cfg)).to_dict("records")}
    df = load(folders, gold, reg, (cfg.get("verdict") or {}).get("binding", "either"))
    if df.empty:
        print("no saved runs in", ", ".join(folders))
        return
    print(metrics.markdown(summary(df)))
    print()
    print(metrics.markdown(per_case(df)))


if __name__ == "__main__":
    main(sys.argv[1:] or FOLDERS)
