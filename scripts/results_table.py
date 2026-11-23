"""One row per gold-set case for the v8 grid: what the agent named in each repeat of the main arm, what the code-only
baseline and the memory test (no tools, no evidence) named, and the verdict lines, with every total given as k/n.
Writes eval/v8_cases.md (luna_v8) or eval/v8_cases_<name>.md for another profile.

    uv run python scripts/results_table.py [--profile luna_v8]
"""

import argparse

import pandas as pd
from v8_results import TITLES

from variant2mechanism.config import REPO, load_config, with_profile
from variant2mechanism.evaluation.gold import is_control, load_gold, scoring_tf
from variant2mechanism.v8 import evaluation as ev

KIND = {"tf_mechanism_cancer": "TF, cancer", "tf_mechanism_other": "TF, other", "control_near_miss": "near-miss control",
        "control_random": "random control"}


def mark(right) -> str:
    return "" if right is None else (" ✓" if right else " ✗")


def named(tf, none: str = "no chain") -> str:
    return str(tf) if pd.notna(tf) and tf else none


def cell(runs: pd.DataFrame, ctl: bool, none: str = "no chain") -> str:
    """The first run's top TF, marked against the gold TF at a TF case."""
    if not len(runs):
        return "not run"
    x = runs.iloc[0]
    return named(x.top_tf, none) + ("" if ctl else mark(bool(x.strict_top1)))


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--profile", default="luna_v8")
    args = p.parse_args(argv)
    cfg = with_profile(load_config(), args.profile)
    df = ev.collect(cfg)
    gold = load_gold(cfg).to_dict("records")
    agent = df[(df.arm == "full_given") & ~df.code_only]
    code = df[(df.arm == "full_given") & df.code_only]
    saved = None if args.profile == "luna_v8" else ev.collect(load_config())    # the saved GPT-6 Luna grid
    borrowed = not len(code) and saved is not None
    if borrowed:                       # code only makes no model call: the saved grid's runs hold for every model
        code = saved[(saved.arm == "full_given") & saved.code_only]
    luna = None if saved is None else saved[(saved.arm == "full_given") & ~saved.code_only & (saved.seed == 0)]
    memory = df[df.arm == "single"]
    repeats = sorted(agent.seed.unique())
    heads = ([f"Agent, repeat {r}" for r in repeats] + ([] if luna is None else ["GPT-6 Luna, repeat 0"])
             + ["Code only"] + (["Memory test"] if len(memory) else []) + ["TF line, overall verdict (agent, repeat 0)"])
    rows = ["| Case | Kind | Gold TF | " + " | ".join(heads) + " |", "|---|---|---|" + "---|" * len(heads)]
    for g in gold:
        cid, ctl = g["case_id"], is_control(g)
        a = agent[agent.case_id == cid].set_index("seed")
        c = code[code.case_id == cid]
        m = memory[memory.case_id == cid]
        cells = [cid, KIND.get(g["label_class"], g["label_class"]), "none (control)" if ctl else scoring_tf(g)]
        for r in repeats:
            x = a.loc[r] if r in a.index else None
            cells.append("not run" if x is None else named(x.top_tf) + ("" if ctl else mark(bool(x.strict_top1))))
        if luna is not None:
            cells.append(cell(luna[luna.case_id == cid], ctl))
        cells.append(cell(c, ctl))
        if len(memory):
            cells.append(cell(m, ctl, "none"))
        x0 = a.loc[0] if 0 in a.index else None
        cells.append("not run" if x0 is None else f"{x0.tf_line}, {x0.verdict}")
        rows.append("| " + " | ".join(str(v) for v in cells) + " |")
    tf_agent, tf_code = agent[~agent.control], code[~code.control]
    all_three = sum(1 for _, x in tf_agent.groupby("case_id") if len(x) == len(repeats) and x.strict_top1.all())
    n_tf = tf_agent.case_id.nunique()
    ctl0 = agent[agent.control & (agent.seed == 0)]
    over = ctl0[ctl0.tf_line_overclaim.astype(bool)]
    rescued = int(over.verdict_correct.astype(bool).sum())
    title = TITLES.get(args.profile, cfg["llm"]["generator"])
    lines = [f"# v8 per case ({title})", "",
             "Main arm (`full_given`: the given context, rsID masked, literature cut at the source paper's year). "
             "✓ the gold TF named first, ✗ another TF. A control is right when the overall verdict is \"no "
             "mechanism\".", "", *rows, "",
             f"- Agent: the gold TF first in {ev.frac(tf_agent.strict_top1)} TF-case runs"
             + (f"; right in all {len(repeats)} repeats at {all_three}/{n_tf} TF cases." if len(repeats) > 1 else "."),
             *([] if luna is None else [f"- GPT-6 Luna, repeat 0 (the saved grid): the gold TF first in "
                                        f"{ev.frac(luna[~luna.control].strict_top1)} TF cases."]),
             f"- Code-only baseline: {ev.frac(tf_code.strict_top1)} TF cases"
             + (" (the saved grid's runs: code only makes no model call)." if borrowed else "."),
             *([f"- Memory test, no tools and no evidence: {ev.frac(memory[~memory.control].strict_top1)} TF cases."]
               if len(memory) else []),
             f"- Controls, agent, repeat 0: overall \"no mechanism\" {ev.frac(ctl0.verdict_correct)}; the TF line "
             f"says \"mechanism\" at {ev.frac(ctl0.tf_line_overclaim)}"
             + (", and only the disease line turns those into \"no mechanism\"." if len(over) and rescued == len(over)
                else f", and the disease line turns {rescued}/{len(over)} of those into \"no mechanism\"." if len(over)
                else ".")]
    stem = "v8_cases" if args.profile == "luna_v8" else f"v8_cases_{args.profile.removesuffix('_v8')}"
    (REPO / "eval" / f"{stem}.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
