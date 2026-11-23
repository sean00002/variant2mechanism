"""Run the critic over the article records a saved fill counts, and report what it says of each.

    python scripts/v9_critic_check.py --runs runs/reader_dev_<date> --out runs/critic_check_<name> --dry-run
    python scripts/v9_critic_check.py --runs runs/reader_dev_<date> --out runs/critic_check_<name> \\
        --decoys --budget-usd 0.50
    python scripts/v9_critic_check.py --runs runs/fill_reader_v2_20261117 --out runs/critic_test_<date> \\
        --relations audited --audit eval/critic_audit_20261117.json --budget-usd 1.00

This is how the critic (src/variant2mechanism/v9/critic.py) is developed and tested without re-running a fill: the
saved runs are read and never changed. For every experiment read from an article that counts for or against a claim
in a saved run, the critic gets the packet it would get inside a fill (the variant, the quotation in its paragraph,
the claims) and answers shown, not_shown or cannot_tell for each claim. Where it names further sentences of the
paragraph as the ones that state the result, the summary shows the quotation code copied.

--alone keeps only the records a fill would send: those that are the only record counted for, or against, some
claim of their run. Without it every counted record is read, which gives more answers to judge the critic by.

--decoys adds a control that needs no label. For each record, one more packet asks about the same text with the
TF or gene of each claim replaced by one the paragraph never names. A critic that reads the text answers
not_shown for every such claim; one that agrees with whatever it is shown does not.

--audit FILE scores the answers against an audit of one run's records (eval/critic_audit_20261117.json): how many
of the records the audit found wrong the critic takes out, and which of the others it takes out too.

A live run spends money, so --budget-usd is required: no call is started once the calls so far have cost that
much, and the profile's own budget still applies. --mode cache-only takes every reply from the response cache and
spends nothing. --dry-run builds the packets, prints their size and a cost estimate from the list price, and calls
nothing. Nothing is written into an existing --out folder.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from variant2mechanism.agent.llm import Budget, LLMClient  # noqa: E402
from variant2mechanism.config import profile_config  # noqa: E402
from variant2mechanism.v9 import critic as K  # noqa: E402
from variant2mechanism.v9 import roles as R  # noqa: E402
from variant2mechanism.v9.bundle import load_bundle  # noqa: E402
from variant2mechanism.v9.commands import OFFLINE_BUDGET_USD, refusing  # noqa: E402

# Where a claim's sentence names its TF or gene (the sentences fill.py writes), for the decoy control.
NAMED = (
    ("tf", re.compile(r"differ in binding (?P<name>.+?)\.$")),
    ("tf", re.compile(r"^(?P<name>.+?) occupies the site of ")),
    ("gene", re.compile(r"the RNA of (?P<name>\S+?)(?: in .+)?\.$")),
    ("gene", re.compile(r"regulates (?P<name>\S+?)(?: in .+)?\.$")),
    ("gene", re.compile(r"^(?P<name>\S+) bears on ")),
)
# Names to put in a decoy claim: the first one the paragraph, the quotation and the claim do not hold.
DECOYS = {"tf": ("ZNF143", "NRF1", "YY1", "REST", "MAX"), "gene": ("ALB", "MYOD1", "INS", "HBB", "TTN")}
OUTPUT_TOKENS = (150, 700)         # a reply's tokens per call, thinking included: the range the estimate assumes
CHARS_PER_TOKEN = 2.5              # measured on this critic's packets (22 Nov 2026: 11,800 characters, 4,750 tokens)
SHOWN = 240                        # characters of a quotation in summary.md


def cases(runs: Path, only: set[str]) -> list[Path]:
    return sorted(p for p in runs.iterdir() if (p / "graph.json").exists() and (not only or p.name in only))


def decoy(claims: list[tuple[str, K.Asked]], text: str) -> list[tuple[str, K.Asked]]:
    """The claims with their TF or gene replaced by a name the text does not hold; claims that name neither are
    left out."""
    held = text.casefold()
    out = []
    for cid, asked in claims:
        for kind, pattern in NAMED:
            found = pattern.search(asked.text)
            if not found:
                continue
            name = found.group("name")
            other = next((d for d in DECOYS[kind] if d.casefold() not in held
                          and d.casefold() not in asked.text.casefold()), None)
            if other is not None:
                out.append((cid, K.Asked(asked.text.replace(name, other), asked.stance,
                                         asked.label.replace(name, other))))
            break
    return out


def collect(folders: list[Path], relations: list[str] | None, decoys: bool, alone: bool = False) -> list[dict]:
    """One item per packet: a counted record of a saved run with its claims, then (with decoys) its decoy. With
    `alone`, only the records that are the only one counted under some claim and stance of their run."""
    items = []
    for folder in folders:
        graph = load_bundle(folder).graph
        articles: dict = {}
        lone = set(K.alone(K.counted_by_side(K.linked_items(graph)))) if alone else None
        for evidence, claims in K.linked_items(graph, relations):
            if lone is not None and evidence.evidence_id not in lone:
                continue
            passage = K.load_passage(graph, evidence, folder, articles)
            base = {"case": folder.name, "folder": folder, "graph": graph, "evidence": evidence,
                    "paragraph": passage}
            items.append({**base, "claims": claims, "decoy": False})
            shown = " ".join((passage.text, passage.before, passage.after, evidence.experiment.passage))
            swapped = decoy(claims, shown) if decoys else []
            if swapped:
                items.append({**base, "claims": swapped, "decoy": True})
    return items


def estimate(items: list[dict], cfg) -> str:
    """The packets' size and what they would cost at the list price, for --dry-run. The instructions are the same
    in every call: where the critic's client sends them to the provider's prompt cache (critic.critic_config) and
    the model has cache prices, they are counted as one write and then reads."""
    chosen = K.settings(cfg)
    price = (cfg["llm"].get("prices_per_mtok") or {}).get(chosen["model"])
    system = len(K.system_prompt())
    packets = [len(K.packet(i["graph"], i["evidence"], i["paragraph"], [a for _, a in i["claims"]])) for i in items]
    chars = len(items) * system + sum(packets)
    tokens = chars / CHARS_PER_TOKEN
    lines = [f"{len(items)} packet(s) ({sum(i['decoy'] for i in items)} of them decoys), "
             f"{sum(len(i['claims']) for i in items)} claim check(s); {chars:,} characters with the "
             f"instructions, about {tokens:,.0f} input tokens",
             f"{sum(not i['paragraph'].text for i in items)} packet(s) have no paragraph (the article could not be "
             "loaded from the saved run)",
             f"critic: {chosen['model']} through {chosen['api']}, effort {chosen['effort']}"]
    if price:
        cached = bool(items) and K.critic_config(cfg)["llm"].get("cache_system") and "cache_read" in price
        repeats = (price.get("cache_write", price["input"]) + (len(items) - 1) * price["cache_read"] if cached
                   else len(items) * price["input"])
        paid = system / CHARS_PER_TOKEN * repeats + sum(packets) / CHARS_PER_TOKEN * price["input"]
        low, high = ((paid + len(items) * n * price["output"]) / 1e6 for n in OUTPUT_TOKENS)
        lines.append(f"at ${price['input']:g} in and ${price['output']:g} out per million tokens"
                     + (f", the instructions read from the prompt cache at ${price['cache_read']:g}" if cached else "")
                     + f": about ${low:.2f} to ${high:.2f} (assuming {OUTPUT_TOKENS[0]} to {OUTPUT_TOKENS[1]} "
                     "output tokens a call, thinking included)")
    else:
        lines.append(f"no list price for {chosen['model']} in config.yaml: no estimate")
    return "\n".join(lines)


def short(text: str, limit: int = SHOWN) -> str:
    text = " ".join(str(text or "").split())
    return text if len(text) <= limit else text[:limit - 1] + "…"


def summary(rows: list[dict], audit: dict | None, runs: Path, spent: float, calls: int, stopped: str | None) -> str:
    real = [r for r in rows if not r["decoy"]]
    fake = [r for r in rows if r["decoy"]]
    answered = [r for r in real if r["verdict"] is not None]
    lines = [f"# The critic over {runs.name}", "",
             f"{len({(r['case'], r['evidence']) for r in real})} counted record(s), {len(real)} claim check(s); "
             f"{calls} model call(s), ${spent:.4f}." + (f" Stopped early: {stopped}." if stopped else ""), "",
             "| Answer | Claim checks |", "|---|---|"]
    lines += [f"| {v.replace('_', ' ')} | {sum(r['verdict'] == v for r in real)} |"
              for v in ("shown", "not_shown", "cannot_tell")]
    lines += [f"| no answer | {len(real) - len(answered)} |", ""]
    if fake:
        said = [r for r in fake if r["verdict"] is not None]
        caught = [r for r in said if r["verdict"] == "not_shown"]
        lines += ["## Decoys", "",
                  f"{len(fake)} claim(s) with the TF or gene replaced by one the paragraph never names: the critic "
                  f"answered not shown for {len(caught)} of the {len(said)} it answered.", ""]
        lines += [f"- {r['case']} {r['evidence']}: answered {r['verdict']} for \"{short(r['claim'], 120)}\" "
                  f"({short(r['reason'], 160)})" for r in said if r["verdict"] != "not_shown"]
        lines.append("")
    if audit is not None:
        wrong = audit["wrong"]
        by_record: dict[str, list[dict]] = {}
        for r in real:
            by_record.setdefault(f"{r['case']}/{r['evidence']}", []).append(r)
        out = {key for key, found in by_record.items() if any(r["verdict"] == "not_shown" for r in found)}
        lines += ["## Against the audit", "",
                  f"The audit ({audit['audited']}) found {len(wrong)} of {audit['records']} counted records wrong. "
                  f"The critic took out {len(out & set(wrong))} of those {len(wrong)}, and "
                  f"{len(out - set(wrong))} of the other {len(by_record) - len(set(wrong) & set(by_record))}.", "",
                  "| Record the audit found wrong | The critic | Fault | Its reason |", "|---|---|---|---|"]
        for key in wrong:
            for r in by_record.get(key, [{"verdict": "not in this run", "fault": "", "reason": ""}]):
                lines.append(f"| {key} | {str(r['verdict']).replace('_', ' ')} | {r['fault'] or ''} | "
                             f"{short(r['reason'], 200)} |")
        lines.append("")
    pointed = [r for r in real if r.get("pointed")]
    if pointed:
        lines += ["## Quotations the critic extended", "",
                  f"For {len(pointed)} claim(s) the critic named further sentences of the paragraph as the ones "
                  "that state the result, and code copied them.", ""]
        for r in pointed:
            lines += [f"- **{r['case']} {r['evidence']}** ({r['source']} {r['location']}), sentences "
                      f"{r['sentences'][0]} to {r['sentences'][1]}",
                      f"  - claim: {r['claim']}",
                      f"  - the reader's quotation: \"{short(r['passage'])}\"",
                      f"  - now quoted: \"{short(r['pointed'], 2 * SHOWN)}\"",
                      f"  - the critic: {short(r['reason'], 400)}"]
        lines.append("")
    lines += ["## Every claim the critic did not find shown", ""]
    for r in real:
        if r["verdict"] in ("not_shown", "cannot_tell"):
            lines += [f"- **{r['case']} {r['evidence']}** ({r['source']} {r['location']}): "
                      f"{r['verdict'].replace('_', ' ')}" + (f", {r['fault']}" if r["fault"] != "none" else ""),
                      f"  - claim: {r['claim']}",
                      f"  - quotation: \"{short(r['passage'])}\"",
                      f"  - the critic: {short(r['reason'], 400)}"]
    if not any(r["verdict"] in ("not_shown", "cannot_tell") for r in real):
        lines.append("None.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--runs", required=True, help="a folder of saved fills, one folder per case")
    parser.add_argument("--out", required=True, help="a new folder for verdicts.json and summary.md")
    parser.add_argument("--mode", choices=["live", "cache-only"], default="live")
    parser.add_argument("--budget-usd", type=float, default=None, help="live mode (required): stop at this spend")
    parser.add_argument("--relations", choices=["all", "audited"], default="all",
                        help="audited: only claims of the relations the audit file covers (needs --audit)")
    parser.add_argument("--decoys", action="store_true", help="add the decoy control")
    parser.add_argument("--alone", action="store_true",
                        help="only the records that are alone behind a cell: what a fill sends")
    parser.add_argument("--audit", default=None, help="an audit file to score against")
    parser.add_argument("--only", nargs="*", default=[], help="case folders to run (default: all)")
    parser.add_argument("--profile", default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    runs, out = (ROOT / args.runs).resolve(), (ROOT / args.out).resolve()
    audit = json.loads((ROOT / args.audit).read_text()) if args.audit else None
    if args.relations == "audited" and audit is None:
        print("refused: --relations audited needs --audit", file=sys.stderr)
        return 2
    relations = list(audit["relations"]) if args.relations == "audited" else None
    cfg = profile_config(args.profile)
    items = collect(cases(runs, set(args.only)), relations, args.decoys, args.alone)
    if args.dry_run:
        print(estimate(items, cfg))
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
    critics: dict[str, K.Critic] = {}
    rows, stopped = [], None
    for n, item in enumerate(items, 1):
        if live and roles.cost_usd >= args.budget_usd:
            stopped = f"${roles.cost_usd:.4f} spent of the ${args.budget_usd:.2f} given"
            break
        checker = critics.setdefault(item["case"], K.Critic(roles, item["folder"], max_records=len(items) + 1))
        roles.set_limits(R.GUARD * (len(items) + 1), 0)
        evidence = item["evidence"]
        checks = checker.review(item["graph"], evidence, [a for _, a in item["claims"]])
        for (cid, asked), check in zip(item["claims"], checks, strict=True):
            rows.append({"case": item["case"], "evidence": evidence.evidence_id, "decoy": item["decoy"],
                         "source": evidence.source_ids[0] if evidence.source_ids else "",
                         "location": evidence.experiment.location, "passage": evidence.experiment.passage,
                         "claim_id": cid, "claim": asked.text, "stance": asked.stance, "label": asked.label,
                         "verdict": check.verdict if check else None, "fault": check.fault if check else None,
                         "reason": " ".join(check.reason.split()) if check else "",
                         "pointed": check.passage if check else "",
                         "sentences": list(check.sentences) if check and check.sentences else None})
        print(f"{n}/{len(items)} {item['case']} {evidence.evidence_id}{' decoy' if item['decoy'] else ''}: "
              + ", ".join(c.verdict if c else "no answer" for c in checks) + f" (${roles.cost_usd:.4f})", flush=True)
        if checker.stopped:
            stopped = checker.stopped
            break
    record = {"runs": str(runs.relative_to(ROOT)), "mode": args.mode, "relations": args.relations,
              "decoys": args.decoys, "alone": args.alone, "audit": args.audit, "critic": K.manifest_parts(roles, K.settings(cfg)),
              "model_calls": roles.calls_used, "cost_usd": roles.cost_usd, "stopped": stopped,
              "failures": roles.failures, "rows": rows}
    (out / "verdicts.json").write_text(json.dumps(record, indent=1))
    (out / "summary.md").write_text(summary(rows, audit, runs, roles.cost_usd, roles.calls_used, stopped))
    print(f"critic check: {len(rows)} claim check(s), {roles.calls_used} model call(s), ${roles.cost_usd:.4f}; "
          f"see {out / 'summary.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
