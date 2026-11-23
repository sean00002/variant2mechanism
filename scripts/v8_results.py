"""The v8 test results (agent-lab/v8-plan-draft.md, testing section): summaries per arm, the planned comparisons,
the controls' over-claims, the memory test, and v8 against the earlier GPT-6 Luna versions. Every proportion carries
its denominator; TF cases and controls are scored apart; the JSON is strict (no NaN). Writes eval/v8_results.json
and eval/v8_results.md for the luna_v8 profile, eval/v8_results_<name>.* for another (deepseek_v8 -> _deepseek).

    uv run python scripts/v8_results.py [--profile luna_v8]
"""

import argparse
import json
from statistics import mean

import pandas as pd

from variant2mechanism.config import REPO, load_config, with_profile
from variant2mechanism.evaluation import metrics as m7
from variant2mechanism.evaluation.gold import is_control, load_gold, scoring_tf
from variant2mechanism.qbic.registry import get_registry
from variant2mechanism.v8 import evaluation as ev

EARLIER = ["eval_v3_luna", "eval_v4_luna", "eval_v5_luna", "eval_v6_luna", "eval_v7_luna"]
TITLES = {"luna_v8": "GPT-6 Luna", "deepseek_v8": "DeepSeek V4.1 Flash", "opus55_v8": "Claude Opus 5.5",
          "opus5_v8": "Claude Opus 5"}


def earlier_versions(reg) -> pd.DataFrame:
    rows = []
    for v in EARLIER:
        df = m7.collect(REPO / "runs" / v, reg)
        if not len(df):
            continue
        df = df[(df.config == "full") & (df["mode"] == "masked") & (df.seed == 0)].copy()
        df["version"] = v.removeprefix("eval_").removesuffix("_luna")
        df["right"] = df.apply(lambda r: bool(r["null_top1"]) if r["control"] else bool(r["top1"]), axis=1)
        rows.append(df)
    return pd.concat(rows, ignore_index=True)


def per_case(df: pd.DataFrame, arm: str, code_only: bool = False, repeat: int | None = 0) -> pd.DataFrame:
    if not len(df):
        return df
    g = df[(df.arm == arm) & (df.code_only == code_only)]
    return g if repeat is None else g[g.seed == repeat]


def repeat_agreement(df: pd.DataFrame) -> dict:
    g = per_case(df, "full_given", repeat=None)
    out = {}
    for case, x in g.groupby("case_id"):
        if x.seed.nunique() < 2:
            continue
        tops = {str(t) if pd.notna(t) else "no chain" for t in x.top_tf}      # a run with no chain differs too
        out[case] = {"repeats": int(x.seed.nunique()), "top_tf_same": len(tops) == 1,
                     "verdict_same": x.verdict.nunique(dropna=False) == 1, "top_tfs": sorted(tops),
                     "verdicts": sorted(set(map(str, x.verdict)))}
    return out


def answered(df: pd.DataFrame) -> str | None:
    """Memory-test runs that named any TF, as k/n."""
    return ev.frac(df.top_tf.notna()) if len(df) else None


def overclaims(g: pd.DataFrame) -> dict:
    """Controls by type: the TF line's "mechanism" and the overall verdict's, as k/n over runs."""
    ctl = g[g.control] if len(g) else g
    return {t: {"tf_line_mechanism": ev.frac(x.tf_line_overclaim), "overall_mechanism": ev.frac(x.overclaim)}
            for t, x in ctl.groupby("control_type")} if len(ctl) else {}


def comparisons(df: pd.DataFrame, code: pd.DataFrame, luna: pd.DataFrame | None = None, title: str = "") -> dict:
    """The planned comparisons, A against B per case: TF cases and controls apart, so neither hides the other. For
    another model, `luna` is the saved grid's main arm, compared first."""
    fg = per_case(df, "full_given")
    pairs = {f"{title} vs GPT-6 Luna (full, given)": (fg, luna)} if luna is not None else {}
    pairs |= {"agent vs code-only (full, given)": (fg, code),
              "full vs no QBiC-SELEX (given)": (fg, per_case(df, "noqbic_given")),
              "given vs inferred context": (fg, per_case(df, "full_inferred")),
              "masked vs named (real-use reference)": (fg, per_case(df, "named_given")),
              "full vs ablation (gold TF's rows removed)": (fg, per_case(df, "ablation"))}
    out = {}
    for name, (a, b) in pairs.items():
        if not (len(a) and len(b)):
            continue
        tf_a, tf_b, ctl_a, ctl_b = a[~a.control], b[~b.control], a[a.control], b[b.control]
        rows = {f"{k} (TF cases)": ev.paired(tf_a, tf_b, k) for k in ("verdict_correct", "strict_top1")}
        rows["family_top1 (covered TF cases)"] = ev.paired(tf_a[tf_a.covered.astype(bool)],
                                                           tf_b[tf_b.covered.astype(bool)], "family_top1")
        if len(ctl_a) and len(ctl_b):
            rows["verdict_correct (controls)"] = ev.paired(ctl_a, ctl_b, "verdict_correct")
            rows["tf_line_overclaim (controls)"] = ev.paired(ctl_a, ctl_b, "tf_line_overclaim")
        out[name] = rows
    return out


def versus_earlier(fg: pd.DataFrame, old: pd.DataFrame) -> tuple[str | None, dict]:
    versions = {}
    for v, g in old.groupby("version"):
        tf, ctl = g[~g.control], g[g.control]
        versions[v] = {"cases": len(g), "tf_top1": ev.frac(tf.top1), "controls_null_top1": ev.frac(ctl.null_top1),
                       "cost_per_run": round(float(g.cost_usd.mean()), 4)}
    complete = [v for v in versions if versions[v]["cases"] == 15]
    best = max(complete, key=lambda v: (ev.share(old[(old.version == v) & ~old.control].top1) or 0,
                                        ev.share(old[(old.version == v) & old.control].null_top1) or 0), default=None)
    if not best or not len(fg):
        return best, {"versions": versions}
    b = old[old.version == best].set_index("case_id")
    cases = []
    for r in fg.to_dict("records"):
        if r["case_id"] not in b.index:
            continue
        o = b.loc[r["case_id"]]
        old_right = bool(o["null_top1"]) if r["control"] else bool(o["top1"])
        new_right = bool(r["verdict_correct"]) if r["control"] else bool(r["strict_top1"])
        cases.append({"case_id": r["case_id"], "control": r["control"], "old": old_right, "new": new_right,
                      "new_top": r["top_tf"], "new_verdict": r["verdict"]})
    wins = sum(1 for c in cases if c["new"] and not c["old"])
    losses = sum(1 for c in cases if c["old"] and not c["new"])
    return best, {"versions": versions, "best_earlier": best, "cases": cases, "v8_better": wins,
                  "earlier_better": losses, "p_sign_test": ev.exact_sign_test(wins, losses)}


def clean(x):
    """Strict JSON: NaN becomes null and numpy scalars plain numbers."""
    if hasattr(x, "item") and not isinstance(x, (list, dict, str)):
        x = x.item()
    if isinstance(x, float) and x != x:
        return None
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [clean(v) for v in x]
    return x


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--profile", default="luna_v8")
    args = p.parse_args(argv)
    cfg = with_profile(load_config(), args.profile)
    title = TITLES.get(args.profile, cfg["llm"]["generator"])
    stem = "v8_results" if args.profile == "luna_v8" else f"v8_results_{args.profile.removesuffix('_v8')}"
    reg = get_registry()
    gold = {r["case_id"]: r for r in load_gold(cfg).to_dict("records")}
    df = ev.collect(cfg)
    att = ev.attempts(cfg)
    summ = ev.summary(df, att)
    fg = per_case(df, "full_given")
    saved = None if args.profile == "luna_v8" else ev.collect(load_config())    # the saved GPT-6 Luna grid
    code = per_case(df, "full_given", True)
    if not len(code) and saved is not None:      # code only makes no model call: the saved grid's runs hold
        code = per_case(saved, "full_given", True)
    comp = comparisons(df, code, None if saved is None else per_case(saved, "full_given"), title)
    # the earlier versions are Luna grids: only Luna's v8 is compared with them
    best, earlier = versus_earlier(fg, earlier_versions(reg)) if saved is None else (None, {"versions": {}})
    memory, rules, ablation = per_case(df, "single"), per_case(df, "single_rules"), per_case(df, "ablation")
    tf_mem = memory[~memory.control] if len(memory) else memory
    out = {"profile": args.profile, "models": title, "summary": summ.to_dict("records"), "comparisons": comp,
           "control_overclaims": {"agent": overclaims(fg), "code only": overclaims(code)},
           "earlier_versions": earlier.pop("versions"), "v8_vs_best_earlier": earlier,
           "repeat_agreement": repeat_agreement(df),
           "memory_floor": {"strict_top1": ev.frac(tf_mem.get("strict_top1", [])),
                            "family_top1": ev.frac(tf_mem.get("family_top1", [])),
                            "gold_anywhere": ev.frac(tf_mem.get("gold_anywhere", []))} if len(memory) else None,
           "memory_under_rules": {"answered": answered(rules), "strict_top1": ev.frac(
               rules[~rules.control].get("strict_top1", []))} if len(rules) else None,
           "ablation": {"still_named_top": ev.frac(ablation[~ablation.control].get("strict_top1", []))}
           if len(ablation) else None,
           "attempts": {"attempted": len(att), "completed": len(df), "failed": int((att.failed & ~att.earlier).sum()),
                        "rerun": int(att.earlier.sum())},
           "runs": df.to_dict("records"), "spend_usd": round(float(df.cost_usd.sum()), 4) if len(df) else 0.0,
           "gold": {k: {"tf": scoring_tf(v), "control": is_control(v), "targets": sorted(ev.targets(v)),
                        "label_class": v["label_class"]} for k, v in gold.items()}}
    (REPO / "eval" / f"{stem}.json").write_text(json.dumps(clean(out), indent=1, allow_nan=False))
    a = out["attempts"]
    lines = [f"# v8 results ({title})", "",
             "Each cell is k/n over runs: every repeat of a case counts once. TF-case columns cover the 9 TF cases "
             "and control columns the 6 controls; family_top1 is over the 8 TF cases whose gold TF QBiC-SELEX covers "
             "(ARID5B, at rs1421085, has no model). `attempted` counts failed attempts that were run again (`rerun`).",
             "", m7.markdown(summ), "",
             "## Controls: how often each line says \"mechanism\" (main arm, repeat 0)", ""]
    for who, by_type in out["control_overclaims"].items():
        for t, x in by_type.items():
            lines.append(f"- {who}, {t.replace('_', ' ')}: TF line {x['tf_line_mechanism']}, overall verdict "
                         f"{x['overall_mechanism']}")
    lines += ["", "## Planned comparisons (repeat 0, per case)", ""]
    for name, rows in comp.items():
        for k, x in rows.items():
            lines.append(f"- {name}, {k}: A {x['a_mean']} vs B {x['b_mean']} over {x['cases']} cases; A better in "
                         f"{x['a_better']}, B in {x['b_better']}, tied in {x['ties']}; sign test p {x['p_sign_test']}")
    if out["memory_floor"]:
        mf = out["memory_floor"]
        lines += ["", f"Memory test (no tools, no evidence): gold TF named first in {mf['strict_top1']} TF cases, its "
                      f"family in {mf['family_top1']}, anywhere in the list in {mf['gold_anywhere']}."]
    if saved is None:
        lines += ["", f"Best earlier version: {best}; v8 better on {earlier.get('v8_better')} cases, earlier better "
                      f"on {earlier.get('earlier_better')} (p {earlier.get('p_sign_test')})."]
    else:
        lines += ["", "Code only comes from the saved GPT-6 Luna grid: it makes no model call, so it is the same for "
                      "every model. The earlier versions were Luna grids and are not compared here.", ""]
    lines += [f"Attempts: {a['attempted']}, completed {a['completed']}, failed {a['failed']}; {a['rerun']} failed "
              "attempts were run again.",
              f"Total spend: ${out['spend_usd']:.3f} over {len(df)} completed runs (mean "
              f"${mean(df.cost_usd) if len(df) else 0:.4f}), as each report records it."]
    (REPO / "eval" / f"{stem}.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
