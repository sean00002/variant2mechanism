"""Read saved v9 runs as chain tables, check them and write the counts.

    python scripts/v9_chain_table.py --runs runs/eval_v9_frozen_<date> --out runs/chain_table_<date>

For every run folder under --runs (a folder with a graph.json, or a public copy with a graph.json.gz) this builds the run's chain table (v9/table.py), checks
it against the table's rules and writes <out>/<run>/table.json and table.md, then <out>/summary.json and summary.md
for the whole set. It reads the saved graphs and nothing else: no model call, no network, no gold label, and nothing
is written into the run folders. --out must be a new folder.
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from v9_demo_export import has_graph, saved_graph  # noqa: E402

from variant2mechanism.v9 import table as T  # noqa: E402


def sources_used(graph, table: T.Table) -> dict[str, dict[str, int]]:
    """Per tool: the records the run holds, how many of them the table counts for a claim of any chain, and how many
    more it lists beside one."""
    counted = {r.id for c in table.claims.values() for cell in c.cells.values() for r in cell.records
               if r.stance != "beside"}
    beside = {r.id for c in table.claims.values() for cell in c.cells.values() for r in cell.records} - counted
    out: dict[str, dict[str, int]] = {}
    for ev in graph.evidence.values():
        call = graph.tool_calls.get(ev.retrieval_ref or "")
        row = out.setdefault(call.tool_name if call else ev.origin, {"on_file": 0, "counted": 0, "beside": 0})
        row["on_file"] += 1
        row["counted"] += ev.evidence_id in counted
        row["beside"] += ev.evidence_id in beside
    return out


def funnel(graph) -> dict[str, int]:
    """Literature, from searches to records: the searches and reads the run made, the articles those reads returned
    (a read by PMCID and one by PMID of one article are one article), the reads beyond the first of an article, the
    experiments the run tried to file from them (accepted, or refused by the quote and identity checks), and the
    accepted ones linked to a claim as support or contradiction."""
    calls = [t for t in graph.tool_calls.values() if t.charged_to != "none"]
    reads = [t for t in calls if t.tool_name == "literature_read" and t.read_article]
    articles: list[set[str]] = []
    for t in reads:
        ids = set(t.article_ids) or {t.read_article}
        for known in [a for a in articles if a & ids]:
            ids |= known
            articles.remove(known)
        articles.append(ids)
    accepted = {e.evidence_id for e in graph.evidence.values() if e.origin == "literature"}
    linked = {x.evidence_id for c in graph.claims.values() for x in c.evidence_links
              if x.stance in ("supports", "contradicts")}
    refused = sum(1 for e in graph.events if e.action == "refuse_update" and e.details.get("kind") == "add_evidence")
    out = {"searches": sum(t.tool_name == "literature_search" for t in calls), "reads": len(reads),
           "articles": len(articles), "repeated_reads": len(reads) - len(articles),
           "experiments_tried": len(accepted) + refused, "experiments_accepted": len(accepted),
           "experiments_linked": len(accepted & linked)}
    # a run with the reader (reader.py) also says what became of every article its searches listed
    reading = next((e.details["reader_summary"] for e in reversed(graph.events)
                    if isinstance(e.details.get("reader_summary"), dict)), None)
    if reading is not None:
        out.update({f"reader_{key}": int(reading.get(key) or 0) for key, _ in READER})
    # ... and a run with the critic (critic.py) what its second reading found
    second = next((e.details["critic_summary"] for e in reversed(graph.events)
                   if isinstance(e.details.get("critic_summary"), dict)), None)
    if second is not None:
        out.update({f"critic_{key}": int(second.get(key) or 0) for key, _ in CRITIC})
    # ... and a run with the judge (judge.py) what it read of a tie for first
    third = next((e.details["judge_summary"] for e in reversed(graph.events)
                  if isinstance(e.details.get("judge_summary"), dict)), None)
    if third is not None:
        out.update({f"judge_{key}": int(third.get(key) or 0) for key, _ in JUDGE})
    return out


def judge_names(graph) -> dict[str, str]:
    """The candidates the judge's answers name, by what the answer says of them."""
    said = [e.details["judge"] for e in graph.events if isinstance(e.details.get("judge"), dict)]
    return {key: ", ".join(f"{x['kind'].replace('tf', 'TF')} {x['label']}" for x in said
                           if x["answer"] in answers) or "-"
            for key, answers in (("to", ("shown",)), ("away", ("against",)),
                                 ("undecided", ("cannot_tell", "disagreed", "check_failed", "no_answer")))}


FUNNEL = (("searches", "Searches"), ("reads", "Reads"), ("articles", "Articles read"),
          ("repeated_reads", "Reads of an article already read"), ("experiments_tried", "Experiments filed or refused"),
          ("experiments_accepted", "Accepted"), ("experiments_linked", "Linked to a claim"))
# What became of the articles a reader's searches listed (reader.STATUSES), then what the model returned.
READER = (("found", "Articles found"), ("read", "Read by the model"), ("corrected", "Sent back once for its pointers"), ("no_mention", "Variant not named in the text"),
          ("review", "Reviews"), ("unreadable", "Text not retrieved"), ("failed", "Model call failed"),
          ("over_cap", "Beyond the cap"), ("experiments", "Experiments returned"), ("accepted", "Filed as records"))


# What the critic's second reading did with the experiments code would have counted, then with their claims.
CRITIC = (("records", "Experiments up for counting"), ("not_alone", "Not alone behind a claim: not sent"),
          ("reviewed", "Read by the critic"), ("failed", "Call failed"), ("not_reached", "Beyond the cap"),
          ("alone_not_sent", "Alone and not read"), ("claims", "Claims checked"), ("shown", "Shown"),
          ("extended", "Shown, quotation extended"), ("not_shown", "Not shown"), ("cannot_tell", "Cannot tell"),
          ("records_taken_out", "Experiments counted for nothing after it"))


# What the judge read of a tie for first: the tie, the candidates, the calls, then its answers by candidate.
JUDGE = (("chains", "Chains tied for first"), ("candidates", "Tied TFs and genes"),
         ("with_experiments", "With experiments no cell counts"), ("asked", "Read by the judge"),
         ("experiments", "Experiments read"), ("orders", "Readings (orders)"), ("shown", "Tied to the site"),
         ("against", "An experiment changed nothing"), ("not_shown", "Not tied"), ("cannot_tell", "Cannot tell"),
         ("disagreed", "Readings disagreed"), ("check_failed", "Made-up candidate accepted"),
         ("no_answer", "No answer"))
JUDGE_NAMES = (("to", "Points to"), ("away", "Points away from"), ("undecided", "Undecided"))


def read_run(folder: Path) -> dict:
    graph = saved_graph(folder)                          # a run folder, or its public copy (demo/tables)
    table = T.from_graph(graph)
    problems = T.check(table, graph)
    result = graph.result
    return {"run": folder.name, "variant": table.variant, "outcome": result.outcome if result else None,
            "stop_reason": result.stop_reason if result else None, "table": table, "problems": problems,
            "counts": T.counts(table, problems), "sources": sources_used(graph, table), "funnel": funnel(graph),
            "judge": judge_names(graph)}


def summary_markdown(rows: list[dict], runs: Path) -> str:
    lines = [f"# Chain tables of {len(rows)} saved runs", "",
             f"Runs read from `{runs}`. Each row is the run's first chain; a chain has 8 claims and 24 cells. "
             "\"Claims stated\" counts the claims a claim of the run states; the others are asked by the table and "
             "answered from the run's lookups and the records on file. \"Records not judged\" counts, over that "
             "chain's cells, the records the run holds that name what a claim names and were neither counted, listed "
             "beside it nor set aside. \"Other rules broken\" and the Rules table at the end count every chain of "
             "the run.", "",
             "| Run | Chains (tied first) | Claims stated | With support | Supports | Disagrees or both | Nothing found "
             "| Not checked | No source | Records not judged | Other rules broken |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    total: Counter = Counter()
    for r in rows:
        c = r["counts"]
        cells = c["cells"]
        other = sum(n for rule, n in c["problems"].items() if rule != "unjudged")
        values = {"stated": c["claims_stated"], "supported": c["claims_supported"], "supports": cells["supports"],
                  "against": cells["disagrees"] + cells["both"], "nothing_found": cells["nothing_found"],
                  "not_checked": cells["not_checked"], "no_source": cells["no_source"],
                  "unjudged": c["unjudged"], "other": other}
        total.update(values)
        lines.append(f"| {r['run']} | {c['chains']} ({c['tied']}) | {values['stated']} of 8 | {values['supported']} "
                     f"| {values['supports']} | {values['against']} | {values['nothing_found']} "
                     f"| {values['not_checked']} | {values['no_source']} | {values['unjudged']} | {other} |")
    n = len(rows)
    lines.append(f"| **All {n}** | | {total['stated']} of {8 * n} | {total['supported']} | {total['supports']} "
                 f"| {total['against']} | {total['nothing_found']} | {total['not_checked']} | {total['no_source']} "
                 f"| {total['unjudged']} | {total['other']} |")
    lines += ["", "## By kind of claim", "", "| Claims | Stated by the run | With support |", "|---|---|---|"]
    for part, label in T.PARTS:
        stated = sum(r["counts"]["parts"][part]["stated"] for r in rows)
        held = sum(r["counts"]["parts"][part]["supported"] for r in rows)
        lines.append(f"| {label} | {stated} of {4 * n} | {held} of {4 * n} |")
    lines += ["", "## By claim", "",
              "| Claim | Stated by the run | With support | Strongest kind of record, by run count |",
              "|---|---|---|---|"]
    steps = dict(T.STEPS)
    for key, slot in T.SLOTS.items():
        claims = [r["table"].claims[r["table"].chains[0].claims[key]] for r in rows if r["table"].chains]
        kinds = Counter(c.strongest for c in claims)
        part = "alleles differ" if slot.part == "allele" else "in place"
        shown = ", ".join(f"{k} {v}" for k, v in kinds.most_common()) or "-"
        lines.append(f"| {steps[slot.step]}: {part} | {sum(c.stated for c in claims)} of {n} "
                     f"| {len(claims) - kinds.get('none', 0)} | {shown} |")
    lines += ["", "## By cell", "", "The first chain's cells over the runs.", "",
              "| Claim | Database | Model prediction | Literature |", "|---|---|---|---|"]
    for key, slot in T.SLOTS.items():
        cells = []
        for lane in T.LANE_KEYS:
            states = Counter(r["table"].claims[r["table"].chains[0].claims[key]].cells[lane].state for r in rows
                             if r["table"].chains)
            cells.append(", ".join(f"{T.STATE_WORDS[k]} {states[k]}" for k in T.STATE_KEYS if states[k]) or "-")
        part = "alleles differ" if slot.part == "allele" else "in place"
        lines.append(f"| {steps[slot.step]}: {part} | {' | '.join(cells)} |")
    lines += ["", "## By kind of record", "", "| Kind | Cells with a source | Cells with support |", "|---|---|---|"]
    for lane, label in T.LANES:
        with_source = sum(r["counts"]["lanes"][lane]["with_source"] for r in rows)
        supported = sum(r["counts"]["lanes"][lane]["supported"] for r in rows)
        lines.append(f"| {label} | {with_source} | {supported} |")
    lines += ["", "## Records on file and records used", "",
              "| Source | Records on file | Counted for a claim | Listed beside a claim |", "|---|---|---|---|"]
    tools: dict[str, Counter] = {}
    for r in rows:
        for tool, row in r["sources"].items():
            tools.setdefault(tool, Counter()).update(row)
    for tool, row in sorted(tools.items(), key=lambda kv: -kv[1]["on_file"]):
        lines.append(f"| `{tool}` | {row['on_file']} | {row['counted']} | {row['beside']} |")
    all_rows = Counter()
    for row in tools.values():
        all_rows.update(row)
    lines.append(f"| **All** | {all_rows['on_file']} | {all_rows['counted']} | {all_rows['beside']} |")
    lines += ["", "## Literature: from searches to records", "",
              "| Run | " + " | ".join(label for _, label in FUNNEL) + " |", "|---|" + "---|" * len(FUNNEL)]
    reading: Counter = Counter()
    for r in rows:
        reading.update(r["funnel"])
        lines.append(f"| {r['run']} | " + " | ".join(str(r["funnel"][key]) for key, _ in FUNNEL) + " |")
    lines.append(f"| **All {n}** | " + " | ".join(str(reading[key]) for key, _ in FUNNEL) + " |")
    read = [r for r in rows if "reader_found" in r["funnel"]]
    if read:
        lines += ["", "## The reader: what became of the articles found", "",
                  "Code searched for the variant's names and a model read each article once. \"Read by the model\" "
                  "is also the number of model calls. An experiment the model returned is filed as a record only "
                  "when code finds its sentences in the article and its fields agree with the text.", "",
                  "| Run | " + " | ".join(label for _, label in READER) + " |", "|---|" + "---|" * len(READER)]
        lines += [f"| {r['run']} | " + " | ".join(str(r["funnel"][f"reader_{key}"]) for key, _ in READER) + " |"
                  for r in read]
        lines.append(f"| **All {len(read)}** | " + " | ".join(str(reading[f"reader_{key}"]) for key, _ in READER)
                     + " |")
    checked = [r for r in rows if "critic_records" in r["funnel"]]
    if checked:
        lines += ["", "## The critic: a second reading of what would be counted", "",
                  "Before the experiments from articles are linked, a second model from another provider reads "
                  "each one that would be the only record counted for, or against, some claim: its quotation in "
                  "its paragraph, against each claim code would count it for. An experiment with another record "
                  "beside it under every such claim is not sent, because no answer on it could change a cell (a "
                  "run made before 22 November 2026 sent every experiment, and shows none in that column). "
                  "\"Read by the critic\" is also the number of its model calls. A claim it answers \"not "
                  "shown\" does not get the record. With \"shown\" it may name further sentences of the "
                  "paragraph as the ones that state the result, and code copies them into the quotation. It can "
                  "add no record.", "",
                  "| Run | " + " | ".join(label for _, label in CRITIC) + " |", "|---|" + "---|" * len(CRITIC)]
        lines += [f"| {r['run']} | " + " | ".join(str(r["funnel"][f"critic_{key}"]) for key, _ in CRITIC) + " |"
                  for r in checked]
        lines.append(f"| **All {len(checked)}** | " + " | ".join(str(reading[f"critic_{key}"]) for key, _ in CRITIC)
                     + " |")
    judged = [r for r in rows if "judge_chains" in r["funnel"]]
    if judged:
        lines += ["", "## The judge: reading a tie for first", "",
                  "Where chains tie for first, code lists the TFs and genes they differ in and, for each, the "
                  "experiments read from articles that name it and that no cell counts for it. A second model reads "
                  "them and says for each candidate whether an experiment ties it to the variant's site. It is "
                  "asked twice, with the candidates in opposite orders and one made-up candidate among them; only an "
                  "answer both readings give is kept, and nothing is kept from a tie where a reading accepts the "
                  "made-up candidate. No cell, rank or count of tied chains changes. A run with one leading chain "
                  "is not listed.", "",
                  "| Run | " + " | ".join(label for _, label in JUDGE + JUDGE_NAMES) + " |",
                  "|---|" + "---|" * len(JUDGE + JUDGE_NAMES)]
        lines += [f"| {r['run']} | " + " | ".join([*(str(r["funnel"][f"judge_{key}"]) for key, _ in JUDGE),
                                                  *(r["judge"][key] for key, _ in JUDGE_NAMES)]) + " |"
                  for r in judged]
    broken = Counter()
    for r in rows:
        broken.update(r["counts"]["problems"])
    lines += ["", "## Rules", "", "| Rule | Times broken | What it says |", "|---|---|---|"]
    lines += [f"| {key} | {broken[key]} | {text} |" for key, text in T.RULES]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--runs", required=True, help="a folder of saved v9 run folders, or one run folder")
    parser.add_argument("--out", required=True, help="a new folder for the tables and the summary")
    args = parser.parse_args()
    runs = (ROOT / args.runs).resolve()
    out = (ROOT / args.out).resolve()
    if out.exists():
        print(f"refused: {out} already exists; choose a new folder", file=sys.stderr)
        return 2
    folders = [runs] if has_graph(runs) else sorted(p for p in runs.iterdir() if p.is_dir() and has_graph(p))
    if not folders:
        print(f"refused: no run folder with a graph.json under {runs}", file=sys.stderr)
        return 2
    out.mkdir(parents=True)
    rows = []
    for folder in folders:
        row = read_run(folder)
        rows.append(row)
        target = out / folder.name
        target.mkdir()
        (target / "table.json").write_text(row["table"].model_dump_json(indent=1), encoding="utf-8")
        (target / "table.md").write_text(T.to_markdown(row["table"], row["problems"]), encoding="utf-8")
        c = row["counts"]
        print(f"{folder.name}: {c['chains']} chain(s), {c['claims_stated']} of 8 claims stated, "
              f"{c['claims_supported']} with support, {c['unjudged']} record(s) not judged", flush=True)
    shown = runs.relative_to(ROOT) if runs.is_relative_to(ROOT) else runs
    (out / "summary.md").write_text(summary_markdown(rows, shown), encoding="utf-8")
    (out / "summary.json").write_text(json.dumps(
        [{k: v for k, v in r.items() if k not in ("table", "problems")}
         | {"problems": [p.model_dump() for p in r["problems"]]} for r in rows], indent=1), encoding="utf-8")
    print(f"summary: {out / 'summary.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
