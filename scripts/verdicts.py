"""The verdict (agent/stages/verdict.py) for saved runs: a baseline at no model cost.

    uv run python scripts/verdicts.py [runs/eval_v3_deepseek runs/eval_v6_luna ...]

Each saved report's ranked chains and final link statuses go through the same rule as a live run, with facts from
code: QBiC-SELEX from the cache (full runs only), ENCODE occupancy and ReMap through the HTTP cache, expression
from local files; `single` runs get no facts. Prints, for each binding rule (critic, code, either) and per folder,
configuration and mode, the verdict metrics next to top-1 and null-top-1.
"""

import json
import sys

import pandas as pd

from variant2mechanism.agent.stages.verdict import BINDING_RULES, chain_facts, decide
from variant2mechanism.config import REPO, load_config
from variant2mechanism.context.base import Case
from variant2mechanism.context.chip import remap_peaks
from variant2mechanism.context.http import Http
from variant2mechanism.context.occupancy import fetch
from variant2mechanism.evaluation import metrics
from variant2mechanism.evaluation.gold import load_gold, scored_cases
from variant2mechanism.qbic.expression import get_expression
from variant2mechanism.qbic.registry import get_registry
from variant2mechanism.qbic.tools import QbicTools
from variant2mechanism.qbic.variants import Variant

FOLDERS = ["runs/eval_v3_deepseek", "runs/eval_v3_luna", "runs/eval_v4_luna", "runs/eval_v5_luna", "runs/eval_v6_luna"]


def md(df: pd.DataFrame) -> str:
    """A markdown table, without the optional tabulate dependency."""
    lines = ["| " + " | ".join(map(str, df.columns)) + " |", "|" + "---|" * len(df.columns)]
    lines += ["| " + " | ".join("" if pd.isna(v) else str(v) for v in row) + " |" for row in df.itertuples(index=False)]
    return "\n".join(lines)


def report_chains(report: dict) -> list[dict]:
    return [{"id": c["id"], "is_null": c["is_null"], "tf": c["tf"], "allele": c.get("allele_binding_more"),
             "links": [{"step": lk["step"], "status": lk.get("status", "missing")} for lk in c["links"]]}
            for c in sorted(report["chains"], key=lambda c: c["rank"])]


def main(folders: list[str]) -> None:
    cfg = load_config()
    reg, expression, qbic = get_registry(), get_expression(), QbicTools(cfg)
    http = Http(cfg.path("tools", "http_cache"))
    min_tpm = float(cfg["screen"]["min_tpm"])
    gold = {r["case_id"]: r for r in scored_cases(load_gold(cfg)).to_dict("records")}
    occupancy, cases = {}, {}
    rows = []
    for folder in folders:
        for path in sorted((REPO / folder).glob("*/*/*/*/report.json")):
            if ".prev-" in path.parent.name:
                continue
            report = json.loads(path.read_text())
            g = gold.get(report["case_id"])
            if g is None:
                continue
            variant = Variant.make(g["chrom"], int(g["pos_grch38"]), g["ref"], g["alt"])
            if report["case_id"] not in occupancy:
                case = Case(variant, g["disease_or_trait"], expression_context=g["expression_context"], http=http)
                cases[report["case_id"]], occupancy[report["case_id"]] = case, fetch(case, reg)[0]
            chains = report_chains(report)
            gathered = report["config"] != "single"
            facts = chain_facts(chains, variant, g["expression_context"], reg,
                                qbic if report["config"] == "full" else None,
                                occupancy[report["case_id"]] if gathered else None,
                                expression if gathered else None, min_tpm,
                                lambda s, c=cases[report["case_id"]]: remap_peaks(c, s))
            for rule in BINDING_RULES:
                v, why = decide(chains, facts, binding=rule)
                row = metrics.score_run({**report, "verdict": {"verdict": v, "reason": why}}, g, None, reg)
                rows.append({"rule": rule, "folder": folder.removeprefix("runs/"), **row})
    df = pd.DataFrame(rows)
    table = []
    for (rule, folder, config, mode), g in df.groupby(["rule", "folder", "config", "mode"]):
        s = metrics.verdict_summary(g)
        tf, ctl = g[~g.control], g[g.control]
        table.append({"rule": rule, "runs": folder, "config": config, "mode": mode, "n": len(g),
                      "top1 (TF cases)": round(float(tf.top1.astype(bool).mean()), 2),
                      "null top1 (controls)": round(float(ctl.null_top1.astype(bool).mean()), 2),
                      "verdict right": s["verdict_accuracy"], "answered": s["answered"],
                      "right when answered": s["accuracy_answered"],
                      "mechanism at controls": s["verdict_overclaim_controls"]})
    print(md(pd.DataFrame(table)))
    counts = df.assign(case=df.control.map({True: "control", False: "TF case"})).groupby(
        ["rule", "case", "verdict"]).size()
    print("\nVerdicts by case type:\n" + md(counts.unstack(fill_value=0).reset_index()))


if __name__ == "__main__":
    main(sys.argv[1:] or FOLDERS)
