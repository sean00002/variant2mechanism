"""Compare run sets (spec 3, section 6.2): screen versions and models, named mode, seed 0; counts, not percentages.

    uv run python scripts/compare_screens.py --runs "v1=runs/eval_deepseek" "v2=runs/eval_v2_deepseek" \
        [--configs single no_qbic full] [--per-case full]

A set may list several folders, "name=dir1,dir2": each configuration comes from the first folder that ran it. Screen
v3 reran only `full`, so "v3=runs/eval_v3_deepseek,runs/eval_v2_deepseek" takes its single and no_qbic runs from v2,
which the unchanged prompts would replay from the cache; a v3 full run that failed is not filled in from v2.
"""

import argparse
import json
import re
from collections import Counter

import pandas as pd

from variant2mechanism.config import REPO, load_config
from variant2mechanism.evaluation import metrics
from variant2mechanism.evaluation.gold import load_gold, scoring_tf
from variant2mechanism.qbic.registry import get_registry

CONFIGS = ["single", "no_qbic", "full"]
SITE = re.compile(r"site strength: ref ([\d.]+)th, alt ([\d.]+)th")


def count(s, value=True) -> str:
    s = [x for x in s if x is not None and x == x]
    return f"{sum(1 for x in s if x == value)} of {len(s)}" if s else "none"


def mean(s) -> str:
    s = [float(x) for x in s if x is not None and x == x]
    return f"{sum(s) / len(s):.2f}" if s else "none"


def first_in_screen(d: pd.DataFrame) -> str:
    s = [x for x in d[~d.control].screen_rank if x == x and x is not None]
    return f"{sum(1 for x in s if x == 1)} of {len(s)}" if s else "n/a"


def reports(folder: str):
    for p in sorted((REPO / folder).glob("*/named/0/*/report.json")):
        yield json.loads(p.read_text())


def report_facts(folder: str, gold: dict) -> dict:
    """Per (config, TF case): whether the null chain was ranked first, and in a full run the gold TF's place in the
    occupied list (0: not listed; v1 reports have no such list)."""
    out = {}
    for rep in reports(folder):
        r = gold.get(rep["case_id"])
        if r is None or r["label_class"].startswith("control"):
            continue
        top = min(rep["chains"], key=lambda c: c["rank"]) if rep["chains"] else {}
        f = {"null_first": bool(top.get("is_null"))}
        occ = (rep.get("screen") or {}).get("occupied")
        if rep["config"] == "full" and occ is not None:
            tfs = [x["tf"] for x in occ]
            f["screen_rank"] = tfs.index(scoring_tf(r)) + 1 if scoring_tf(r) in tfs else 0
        out[rep["config"], rep["case_id"]] = f
    return out


def load_set(spec: str, reg, gold: pd.DataFrame, labels) -> pd.DataFrame:
    """A configuration comes from the first folder that ran it at all, so a run that failed there stays missing."""
    by_case = {r["case_id"]: r for r in gold.to_dict("records")}
    frames, seen = [], set()
    for folder in spec.split(","):
        df = metrics.collect(REPO / folder, reg, gold, labels)
        if df.empty:
            continue
        df = df[(df["mode"] == "named") & ~df.config.isin(seen)].copy()
        seen |= set(df.config)
        facts = report_facts(folder, by_case)
        keys = list(zip(df.config, df.case_id, strict=True))
        df["screen_rank"] = [facts.get(k, {}).get("screen_rank") for k in keys]
        df["null_first_tf"] = [facts.get(k, {}).get("null_first") for k in keys]
        df["folder"] = folder
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def table(dfs: dict[str, pd.DataFrame], configs: list[str]) -> list[str]:
    cols = [(c, v) for c in configs for v in dfs]
    rows = {
        "Gold TF ranked first": lambda d: count(d[~d.control].top1),
        "Gold TF in top 3": lambda d: count(d[~d.control].top3),
        "Direction right (when the gold TF is ranked)": lambda d: count(d[~d.control].direction_correct),
        "TF cases: null ranked first (under-claiming)": lambda d: count(d[~d.control].null_first_tf),
        "Gold TF first in the screen's occupied list": first_in_screen,
        "Random controls: null ranked first": lambda d: count(d[d.control_type == "control_random"].null_top1),
        "Random controls: over-claiming (mean)": lambda d: mean(d[d.control_type == "control_random"].overclaim),
        "Near-miss controls: null ranked first": lambda d: count(d[d.control_type == "control_near_miss"].null_top1),
        "Near-miss controls: over-claiming (mean)": lambda d: mean(d[d.control_type == "control_near_miss"].overclaim),
        "Answer in the evidence (retrieval audit)": lambda d: count(d[~d.control].get("answer_in_evidence", [])),
        "Agent asked a tool about the gold TF": lambda d: count(d[~d.control].get("agent_asked_for_tf", [])),
        "Investigate calls per run (mean)": lambda d: mean(d.investigate_calls),
        "Runs scored": lambda d: str(len(d)),
        "Cost, total": lambda d: f"${d.cost_usd.sum():.2f}",
    }
    head = [f"{v} {c}" if len(configs) > 1 else v for c, v in cols]
    out = ["| | " + " | ".join(head) + " |", "|---|" + "---|" * len(cols)]
    for name, fn in rows.items():
        cells = []
        for c, v in cols:
            sub = dfs[v][dfs[v].config == c]
            cells.append(fn(sub) if len(sub) else "not run")
        out.append(f"| {name} | " + " | ".join(cells) + " |")
    return out


def per_case(dfs: dict[str, pd.DataFrame], gold: pd.DataFrame, configs: list[str]) -> list[str]:
    cols = [(c, v) for c in configs for v in dfs]
    head = [f"{v} {c}" if len(configs) > 1 else v for c, v in cols]
    out = ["| Case | " + " | ".join(head) + " |", "|---|" + "---|" * len(cols)]
    for cid in gold.case_id:
        cells = []
        for c, v in cols:
            r = dfs[v][(dfs[v].case_id == cid) & (dfs[v].config == c)]
            if r.empty:
                cells.append("not run")
                continue
            r = r.iloc[0]
            if r.control:
                cells.append(f"null {'first' if r.null_top1 else 'not first'}, over-claim {r.overclaim:.2f}")
                continue
            rank = "absent" if r.correct_rank != r.correct_rank or r.correct_rank is None else f"rank {int(r.correct_rank)}"
            sr = r.screen_rank
            cells.append(rank + ("" if sr != sr or sr is None else f" (screen {int(sr) or 'none'})"))
        out.append(f"| {cid} | " + " | ".join(cells) + " |")
    return out


def proposed_at_controls(folder: str, gold: dict, pct: float) -> list[str]:
    """TFs the agent proposed at each control in `full`, with the screen's word for each: an occupied TF's site class
    (v2 reports have none, so it is read from the screen line's percentiles with the same cut-off), occupancy unknown,
    or not in the screen."""
    out = []
    for rep in reports(folder):
        r = gold.get(rep["case_id"])
        if rep["config"] != "full" or r is None or not r["label_class"].startswith("control"):
            continue
        screen = rep.get("screen") or {}
        occ, unk = {x["tf"]: x for x in screen.get("occupied", [])}, {x["tf"] for x in screen.get("unknown", [])}
        lines = {e["summary"].split(" (")[0]: e["summary"] for e in rep["evidence"] if e.get("tool") == "qbic_screen"}
        names = []
        for tf in (h.get("tf") for h in rep["chains"]):
            if not tf:
                continue
            if tf in occ:
                strong = occ[tf].get("strong_site")
                if strong is None and (m := SITE.search(lines.get(tf, ""))):
                    strong = max(float(m[1]), float(m[2])) >= pct
                word = "occupied" if strong is None else "occupied, strong site" if strong else "occupied, weak site"
            else:
                word = "occupancy unknown" if tf in unk else "not in the screen"
            names.append(f"{tf} ({word})")
        out.append(f"- {rep['case_id']} ({r['label_class']}): {', '.join(names) or 'none'}")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--runs", nargs="+", default=["v1=runs/eval_deepseek", "v2=runs/eval_v2_deepseek"],
                    help='"name=folder[,folder...]"')
    ap.add_argument("--configs", nargs="+", default=CONFIGS, choices=CONFIGS)
    ap.add_argument("--per-case", nargs="+", default=["no_qbic", "full"], choices=CONFIGS)
    args = ap.parse_args()
    reg, gold, labels = get_registry(), load_gold(), metrics.load_direction_labels()
    sets = dict(s.split("=", 1) for s in args.runs)
    dfs = {name: load_set(spec, reg, gold, labels) for name, spec in sets.items()}
    print("\n".join(table(dfs, args.configs)))
    print()
    print("\n".join(per_case(dfs, gold, args.per_case)))
    print()
    for name, d in dfs.items():
        d = d[d.config.isin(args.configs)]
        print(f"{name} flags ({', '.join(args.configs)}):", dict(Counter(f for fs in d["flags"] for f in fs)))
    pct = float(load_config()["screen"]["strong_site_pct"])
    by_case = {r["case_id"]: r for r in gold.to_dict("records")}
    for name, spec in sets.items():
        print(f"\n{name}: TFs proposed at the controls in full (site class at the {pct:g}th percentile)")
        print("\n".join(proposed_at_controls(spec.split(",")[0], by_case, pct)))


if __name__ == "__main__":
    main()
