"""Run the judge over the ties of saved fills, and report what it says of each tied candidate.

    python scripts/v9_judge_check.py --runs runs/reader_dev_<date> --out runs/judge_check_<name> --dry-run
    python scripts/v9_judge_check.py --runs runs/reader_dev_<date> --out runs/judge_dev_<date> --decoys \\
        --budget-usd 0.30

The judge (src/variant2mechanism/v9/judge.py) reads a finished run and changes no cell of it, so what it would say
inside a fill can be had from the saved run, which is read and never changed. For every case whose first rank is
shared, code lists the TFs and genes the tied chains differ in and, for each, the experiments read from articles
that name it and that no cell counts for it; the judge answers for each candidate whether an experiment ties it to
the variant's site. A case with one leading chain, or with no such experiment, is listed and makes no call. This
is how the judge is developed (on variants outside the evaluated cases) and then run once on the evaluated ones.

Every packet already lists one made-up candidate, which a reading has to turn down (judge.py). --decoys adds a
harder control that needs no label either: each tie that is read is read once more with every real candidate's
name replaced by a name no paragraph of the packet holds; the records are the same. A judge that reads the text
answers not_shown or cannot_tell for every such candidate; one that agrees with whatever it is shown does not.

A live run spends money, so --budget-usd is required: no case is started once the calls so far have cost that
much, and the profile's own budget still applies. --mode cache-only takes every reply from the response cache and
spends nothing. --dry-run builds the packets, prints their size and a cost estimate from the list price, and calls
nothing. Nothing is written into an existing --out folder.
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from variant2mechanism.agent.llm import Budget, LLMClient  # noqa: E402
from variant2mechanism.config import profile_config  # noqa: E402
from variant2mechanism.v9 import critic as K  # noqa: E402
from variant2mechanism.v9 import judge as J  # noqa: E402
from variant2mechanism.v9 import roles as R  # noqa: E402
from variant2mechanism.v9.bundle import load_bundle  # noqa: E402
from variant2mechanism.v9.commands import OFFLINE_BUDGET_USD, refusing  # noqa: E402

OUTPUT_TOKENS = (150, 700)         # a reply's tokens per call, thinking included: the range the estimate assumes
CHARS_PER_TOKEN = 2.5              # measured on the critic's packets, which are the same kind of text
SHOWN = 300                        # characters of a quotation in summary.md


class _NoCalls:
    """Stands where a role caller would, for --dry-run: packets are built and nothing is sent."""
    calls_used = 0

    def set_limits(self, *_: int) -> None:
        pass


def cases(runs: Path, only: set[str]) -> list[Path]:
    return sorted(p for p in runs.iterdir() if (p / "graph.json").exists() and (not only or p.name in only))


def decoy(graph, tie: J.Tie, judge: J.Judge) -> J.Tie:
    """The tie with each candidate that has experiments renamed to a name its packet never holds."""
    asked = [c for c in tie.candidates if c.records]
    passages = judge.passages(graph, asked)
    held = " ".join([p.text for p in passages.values()]
                    + [graph.evidence[eid].experiment.passage for c in asked for eid in c.records]).casefold()
    used: set[str] = set()
    out = []
    for c in tie.candidates:
        if not c.records:
            out.append(c)
            continue
        name = next(d for d in J.PLACEBOS[c.kind] if d.casefold() not in held and d not in used)
        used.add(name)
        out.append(J.Candidate(c.kind, name, (name,), c.records, c.on_file))
    return J.Tie(tie.chains, tie.differ, tuple(out))


def estimate(found: list[dict], cfg) -> str:
    """The packets' size and what they would cost at the list price, for --dry-run."""
    chosen = K.settings(cfg)
    price = (cfg["llm"].get("prices_per_mtok") or {}).get(chosen["model"])
    system = len(J.system_prompt())
    sizes = [len(text) for item in found for text in item["packets"]]
    chars = len(sizes) * system + sum(sizes)
    lines = [f"{len(found)} case(s) with a tie for first; {sum(bool(i['packets']) for i in found)} have experiments "
             f"for a tied candidate; {len(sizes)} packet(s), {chars:,} characters with the instructions, about "
             f"{chars / CHARS_PER_TOKEN:,.0f} input tokens",
             f"judge: {chosen['model']} through {chosen['api']}, effort {chosen['effort']}"]
    for item in found:
        tie = item["tie"]
        named = ", ".join(f"{J.KIND_SHORT[c.kind]} {c.label} ({len(c.records)} of {c.on_file})"
                          for c in tie.candidates if c.records) or "no candidate has an experiment on file"
        lines.append(f"  {item['case']}: {tie.chains} chains tied, differing in the {J.differ_words(tie.differ)}; "
                     f"{len(tie.candidates)} candidate(s); {named}; {len(item['packets'])} packet(s)")
    if price and sizes:
        cached = K.critic_config(cfg)["llm"].get("cache_system") and "cache_read" in price
        repeats = (price.get("cache_write", price["input"]) + (len(sizes) - 1) * price["cache_read"] if cached
                   else len(sizes) * price["input"])
        paid = system / CHARS_PER_TOKEN * repeats + sum(sizes) / CHARS_PER_TOKEN * price["input"]
        low, high = ((paid + len(sizes) * n * price["output"]) / 1e6 for n in OUTPUT_TOKENS)
        lines.append(f"at ${price['input']:g} in and ${price['output']:g} out per million tokens"
                     + (f", the instructions read from the prompt cache at ${price['cache_read']:g}" if cached else "")
                     + f": about ${low:.2f} to ${high:.2f} (assuming {OUTPUT_TOKENS[0]} to {OUTPUT_TOKENS[1]} "
                     "output tokens a call, thinking included)")
    elif sizes:
        lines.append(f"no list price for {chosen['model']} in config.yaml: no estimate")
    return "\n".join(lines)


def short(text: str, limit: int = SHOWN) -> str:
    text = " ".join(str(text or "").split())
    return text if len(text) <= limit else text[:limit - 1] + "…"


def _answer(row: dict) -> str:
    basis = f", {row['basis']}" if row["basis"] != "none" else ""
    both = " (both readings)" if row.get("agreed") else ""
    return f"{row['answer'].replace('_', ' ')}{basis}{both}"


def summary(results: list[dict], runs: Path, spent: float, calls: int, stopped: str | None) -> str:
    read = [r for r in results if r["found"]["asked"]]
    lines = [f"# The judge over {runs.name}", "",
             f"{len(results)} case(s) with a tie for first; {len(read)} have experiments on file for a tied "
             f"candidate and were read. {calls} model call(s), ${spent:.4f}."
             + (f" Stopped early: {stopped}." if stopped else ""), "",
             "| Case | Chains tied | They differ in | Candidates | With experiments | Points to | Points away from | "
             "Not shown | Undecided |", "|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        f = r["found"]
        rows = f["rows"]

        def names(*answers: str, rows=rows) -> str:
            return ", ".join(f"{J.KIND_SHORT[x['kind']]} {x['label']}" for x in rows if x["answer"] in answers) or "-"
        lines.append(f"| {r['case']} | {f['chains']} | {J.differ_words(f['differ'])} | {f['candidates']} | "
                     f"{f['with_experiments']} | {names('shown')} | {names('against')} | {names('not_shown')} | "
                     f"{names('cannot_tell', 'disagreed', 'check_failed', 'no_answer')} |")
    asked_twice = [x for r in read for x in r["found"]["rows"] if r["found"]["orders"] == 2]
    if asked_twice:
        same = sum(x["agreed"] is True for x in asked_twice)
        lines += ["", f"Asked twice, with the candidates in opposite orders: {same} of {len(asked_twice)} "
                      "candidate(s) got the same answer both times."]
    made_up = [a for r in results for f in (r["found"], r.get("decoy") or {}) for a in (f.get("check") or {}).get("answers", [])]
    if made_up:
        down = sum(a in ("not_shown", "cannot_tell") for a in made_up)
        lines += ["", f"Every reading also listed a made-up candidate: it was turned down in {down} of "
                      f"{len(made_up)} reading(s)."]
    decoys = [x for r in results for x in (r.get("decoy") or {}).get("rows", [])]
    if decoys:
        caught = [x for x in decoys if x["answer"] in ("not_shown", "cannot_tell")]
        lines += ["", "## Decoys", "",
                  f"{len(decoys)} candidate(s) read again under a name no paragraph holds: the judge tied none of "
                  f"them to the site for {len(caught)} of {len(decoys)}.", ""]
        lines += [f"- {r['case']}: the decoy {x['label']} was answered {_answer(x)} ({short(x['reason'], 200)})"
                  for r in results for x in (r.get("decoy") or {}).get("rows", [])
                  if x["answer"] not in ("not_shown", "cannot_tell")]
    lines += ["", "## Every candidate read", ""]
    for r in read:
        for x in r["found"]["rows"]:
            more = x["on_file"] - x["sent"]
            lines += [f"- **{r['case']}, {J.KIND_SHORT[x['kind']]} {x['label']}**: {_answer(x)}; "
                      f"{x['sent']} experiment(s) read" + (f", {more} more on file" if more > 0 else ""),
                      f"  - the judge: {short(x['reason'], 400)}"]
            if x["agreed"] is False:
                lines += [f"  - reading {i}: {g['answer'].replace('_', ' ')}"
                          + (f", {g['basis']}" if g["basis"] != "none" else "") + f" ({short(g['reason'], 300)})"
                          for i, g in enumerate(x["readings"], 1)]
            lines += [f"  - {q['id']} ({q['source']} {q['location']}): \"{short(q['passage'])}\""
                      + (" (sentences the judge named; code copied them)" if q["pointed"] else "")
                      for q in x["records"]]
    if not read:
        lines.append("None.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--runs", required=True, help="a folder of saved fills, one folder per case")
    parser.add_argument("--out", required=True, help="a new folder for verdicts.json and summary.md")
    parser.add_argument("--mode", choices=["live", "cache-only"], default="live")
    parser.add_argument("--budget-usd", type=float, default=None, help="live mode (required): stop at this spend")
    parser.add_argument("--decoys", action="store_true", help="add the decoy control")
    parser.add_argument("--only", nargs="*", default=[], help="case folders to run (default: all)")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    runs, out = (ROOT / args.runs).resolve(), (ROOT / args.out).resolve()
    cfg = profile_config(args.profile)
    tied = []
    for folder in cases(runs, set(args.only)):
        graph = load_bundle(folder).graph
        tie = J.find_tie(graph)
        if tie is not None:
            tied.append({"case": folder.name, "folder": folder, "graph": graph, "tie": tie})
    if args.dry_run:
        for item in tied:
            item["packets"] = [text for _, text in J.Judge(_NoCalls(), item["folder"]).packets(item["graph"],
                                                                                              item["tie"])]
        print(estimate(tied, cfg))
        return 0
    live = args.mode == "live"
    if live and args.budget_usd is None:
        print("refused: a live run spends money; give --budget-usd", file=sys.stderr)
        return 2
    if out.exists():
        print(f"refused: {out} already exists; choose a new folder", file=sys.stderr)
        return 2
    out.mkdir(parents=True)
    second = K.critic_config(cfg, offline=not live)
    trace = out / "trace.jsonl"
    client = (LLMClient(second, phase="dev", trace_path=trace) if live else
              LLMClient(second, transport=refusing("a cache-only run"), phase="dev", trace_path=trace,
                        budget=Budget(out / "budget.json", {"dev": OFFLINE_BUDGET_USD})))
    roles = R.RoleCaller(client, second)
    results, stopped = [], None
    for n, item in enumerate(tied, 1):
        if live and roles.cost_usd >= args.budget_usd:
            stopped = f"${roles.cost_usd:.4f} spent of the ${args.budget_usd:.2f} given"
            break
        judge = J.Judge(roles, item["folder"])
        found = judge.ask(item["graph"], item["tie"])
        result = {"case": item["case"], "found": {k: v for k, v in found.items() if k != "failures"}}
        if args.decoys and found["asked"] and judge.stopped is None:
            again = J.Judge(roles, item["folder"])
            result["decoy"] = {k: v for k, v in again.ask(item["graph"], decoy(item["graph"], item["tie"], again)).items()
                               if k != "failures"}
            judge.stopped = again.stopped
        results.append(result)
        said = ", ".join(f"{J.KIND_SHORT[x['kind']]} {x['label']}: {_answer(x)}" for x in found["rows"])
        print(f"{n}/{len(tied)} {item['case']}: {found['chains']} tied; {said or 'nothing to read'}"
              + (f"; decoys: {', '.join(_answer(x) for x in result['decoy']['rows'])}" if "decoy" in result else "")
              + f" (${roles.cost_usd:.4f})", flush=True)
        if judge.stopped:
            stopped = judge.stopped
            break
    record = {"runs": str(runs.relative_to(ROOT)), "mode": args.mode, "decoys": args.decoys,
              "judge": J.manifest_parts(roles, K.settings(cfg)), "model_calls": roles.calls_used,
              "cost_usd": roles.cost_usd, "stopped": stopped, "failures": roles.failures, "results": results}
    (out / "verdicts.json").write_text(json.dumps(record, indent=1))
    (out / "summary.md").write_text(summary(results, runs, roles.cost_usd, roles.calls_used, stopped))
    print(f"judge check: {len(results)} tie(s), {roles.calls_used} model call(s), ${roles.cost_usd:.4f}; "
          f"see {out / 'summary.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
