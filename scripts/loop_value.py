"""Does the critique loop help? Draft against final answer in every run with a critique (seed 0), and, for the
multi-round runs (v4), round by round. Counts, not percentages.

    uv run python scripts/loop_value.py

A top answer is right when the top chain names the gold TF (TF cases) or is the null (controls). "Fixed" means wrong
before and right after; "broken" the reverse. Also: how often each planned call's result matched the expectation the
planner wrote down, and why the loop stopped.
"""

import json
from collections import Counter, defaultdict

from variant2mechanism.config import REPO
from variant2mechanism.evaluation import metrics
from variant2mechanism.evaluation.gold import load_gold, scoring_tf
from variant2mechanism.qbic.registry import get_registry

ONE_ROUND = {"runs/eval": "Claude v1", "runs/eval_deepseek": "DeepSeek v1", "runs/eval_v2_deepseek": "DeepSeek v2",
             "runs/eval_v3_deepseek": "DeepSeek v3", "runs/eval_v3_luna": "Luna v3"}
MULTI_ROUND = {"runs/eval_v4_luna": "Luna v4", "runs/eval_v4_deepseek": "DeepSeek v4",
               "runs/eval_v5_luna": "Luna v5", "runs/eval_v5_deepseek": "DeepSeek v5", "runs/eval_v6_luna": "Luna v6"}
LOOPS = [("one round (v3)", "runs/eval_v3_luna"), ("up to three (v4)", "runs/eval_v4_luna"),
         ("up to three, not-assayed fix (v5)", "runs/eval_v5_luna"), ("v5 plus ReMap (v6)", "runs/eval_v6_luna")]
reg = get_registry()
rows = {r["case_id"]: r for r in load_gold().to_dict("records")}


def reports(folders):
    for folder, name in folders.items():
        for p in sorted((REPO / folder).glob("*/*/0/*/report.json")):
            r = json.loads(p.read_text())
            if r["config"] != "single" and r.get("chains_v0") and r["case_id"] in rows:
                yield name, r


def want(cid: str) -> str:
    g = rows[cid]
    return "null" if g["label_class"].startswith("control") else (metrics.resolves_to(reg, scoring_tf(g)) or
                                                                  scoring_tf(g))


def top(chains: list[dict]) -> str:
    c = max(chains, key=lambda c: c["probability"]) if chains else None
    return "null" if c is None or c["is_null"] else (metrics.resolves_to(reg, c["tf"]) or c["tf"])


def move(before: bool, after: bool) -> str:
    return "right both" if before and after else "fixed" if after else "broken" if before else "wrong both"


def kind(cid: str) -> str:
    return "control" if rows[cid]["label_class"].startswith("control") else "TF case"


def stop_kind(reason: str) -> str:
    return ("round limit" if "limit" in reason else "a round changed nothing" if "moved no" in reason
            else "the answer held" if "left the top chain" in reason else "no new information"
            if "no new information" in reason else "nothing new to run" if "call to run" in reason else reason)


def table(tally: dict, title: str) -> list[str]:
    out = [f"| {title} | right both | fixed | broken | wrong both |", "|---|---|---|---|---|"]
    for key in sorted(tally):
        t = tally[key]
        out.append(f"| {' · '.join(key)} | {t['right both']} | {t['fixed']} | {t['broken']} | {t['wrong both']} |")
    return out + [""]


def compare(loops: list[tuple[str, str]], mode: str = "masked", config: str = "full") -> list[str]:
    """One model, mode and configuration under different loops, over the cases every loop ran."""
    def load(folder):
        out = {}
        for p in (REPO / folder / config / mode / "0").glob("*/report.json"):
            r = json.loads(p.read_text())
            out[r["case_id"]] = r
        return out

    sets = [load(folder) for _, folder in loops if (REPO / folder).exists()]
    labels = [label for label, folder in loops if (REPO / folder).exists()]
    cases = sorted(set.intersection(*(set(x) for x in sets)))
    tf = [c for c in cases if kind(c) == "TF case"]

    def col(rs):
        def p_null(r):
            return sum(c["probability"] for c in r["chains"] if c["is_null"])

        def p_gold(r):
            return metrics.tf_marginals(r["chains"], reg).get(want(r["case_id"]), 0.0)

        def mean(xs):
            return f"{sum(xs) / len(xs):.2f}" if xs else "none"
        return [str(sum(top(rs[c]["chains"]) == want(c) for c in tf)),
                str(sum(want(c) in [top([x]) for x in rs[c]["chains"][:3]] for c in tf)),
                str(sum(top(rs[c]["chains"]) == "null" for c in tf)), mean([p_gold(rs[c]) for c in tf]),
                mean([p_null(rs[c]) for c in cases if rows[c]["label_class"] == "control_random"]),
                mean([p_null(rs[c]) for c in cases if rows[c]["label_class"] == "control_near_miss"]),
                f"${sum(rs[c]['cost_usd'] for c in cases):.2f}", mean([rs[c]["model_calls"] for c in cases]),
                mean([rs[c]["seconds"] for c in cases])]

    names = ["TF cases: gold TF ranked first", "TF cases: gold TF in the top three", "TF cases: null ranked first",
             "TF cases: mean p(gold TF)", "Random controls: mean p(null)", "Near-miss controls: mean p(null)",
             "Cost, total", "Model calls per run (mean)", "Seconds per run (mean)"]
    cols = [col(x) for x in sets]
    out = [f"| {mode} `{config}`, {len(cases)} cases ({len(tf)} TF cases) | " + " | ".join(labels) + " |",
           "|---|" + "---|" * len(labels)]
    out += [f"| {n} | " + " | ".join(c[i] for c in cols) + " |" for i, n in enumerate(names)]
    return out + [""]


def main():
    one = defaultdict(Counter)
    for _name, r in reports(ONE_ROUND):
        w = want(r["case_id"])
        one[(kind(r["case_id"]),)][move(top(r["chains_v0"]) == w, top(r["chains"]) == w)] += 1
    lines = ["### One-round runs (v1 to v3): draft against final top answer", ""] + table(one, "Kind")

    steps, final, stops, verdicts, statuses, n_rounds = (defaultdict(Counter), defaultdict(Counter), defaultdict(Counter),
                                                         defaultdict(Counter), defaultdict(Counter),
                                                         defaultdict(Counter))
    for name, r in reports(MULTI_ROUND):
        w, k = want(r["case_id"]), kind(r["case_id"])
        versions = [r["chains_v0"]] + [rd["chains"] for rd in r["rounds"]]
        for i in range(1, len(versions)):
            steps[(name, k, f"round {i}")][move(top(versions[i - 1]) == w, top(versions[i]) == w)] += 1
        final[(name, k)][move(top(r["chains_v0"]) == w, top(r["chains"]) == w)] += 1
        stops[name][stop_kind(r["stop_reason"])] += 1
        n_rounds[name][len(r["rounds"])] += 1
        verdicts[name].update(x["as_expected"] for rd in r["rounds"] for x in rd["check_results"])
        statuses[name].update(c["status"].split(":")[0] for c in r["investigate_calls"])
    if final:
        lines += ["### Multi-round runs (v4): draft against final top answer", ""] + table(final, "Run set · kind")
        lines += ["### Multi-round runs (v4): each round against the one before", ""] + table(steps,
                                                                                             "Run set · kind · round")
        for name in n_rounds:
            lines += [f"{name}: rounds run {dict(sorted(n_rounds[name].items()))}; why the loop stopped "
                      f"{dict(stops[name])}; planned calls {dict(statuses[name])}; results against the planner's "
                      f"expectation {dict(verdicts[name])}.", ""]
        lines += ["### GPT-6 Luna: the three loops", ""] + compare(LOOPS)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
