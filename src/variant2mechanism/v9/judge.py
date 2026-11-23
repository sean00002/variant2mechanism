"""The judge: when chains tie for first, a second model reads the experiments no cell counts, candidate by candidate.

Why: chains are ordered by the kinds of evidence behind their claims (chain.py), and a cell of the table counts an
experiment only for the claim it tests. Some experiments test no single claim: a TF is removed and the difference
between the alleles disappears; the element is deleted and a gene's protein changes; the element is deleted and a
gene does not move. Such a record names a tied chain's TF or gene and is on file with its quotation, yet no cell
may count it (an experiment that changes a TF does not compare the alleles' binding), so it cannot separate that
chain from the ones it ties with. Most cases of the first runs ended in a tie for first, and in several the
articles on file held exactly such experiments for one of the tied chains. Whether an experiment ties a TF or a
gene to this variant's site is a reading of its text, which code cannot do. What to do with the reading is code's.

- Only a tie for first, and only what the tied chains differ in. A candidate is one TF (or one group of TFs that
  share a binding model) or one target gene that some of the tied chains name and others do not.
- Only experiments no cell counts for the candidate: every experiment read from an article that names it, less
  those counted for or against one of its own claims (its binding claims; a gene's expression, regulation and
  trait claims). Those already entered the order of chains. A candidate with none is not asked about, and a tie
  with none at all makes no call.
- One packet for the tie: the variant, the candidates, and each paragraph an experiment was read from, once, as
  numbered sentences with the records that rest on it. Records and candidates are numbered in the packet, so the
  request does not depend on how a run numbered its evidence. Nothing of the first model's reading is in it.
- Four answers per candidate: shown (an experiment ties it to the site, with the basis: the alleles were compared,
  or the site was tested without comparing them), against (such an experiment changed nothing), not_shown,
  cannot_tell. With shown or against the judge names the records the answer rests on and, as the critic does, the
  sentences that state the result when a quotation stops short; code copies them (the model points, code quotes).
- Asked twice, beside a made-up candidate. A model that is shown a list tends to favour what comes first: in the
  first development run the candidate listed first was twice given a "shown" its records did not bear out. So
  every packet also lists one made-up candidate, a TF or gene that no paragraph names, under the first
  candidate's records, and the packet is sent twice: the real candidates first and the made-up one last, then the
  made-up one first and the real ones in the opposite order. An answer is kept only when both readings give it;
  otherwise the candidate is reported as one the readings disagreed on. A reading that ties the made-up candidate
  to the site has shown that it does not read the names, and nothing from that tie is kept.
- It orders nothing by itself and changes no cell. The answers are written under the tie: which candidates the
  uncounted experiments point to, which they point away from, and for which they settle nothing. The table's
  cells, its ranks and the number of tied chains stay as code made them, so a judge that errs changes one
  sentence and its quotations, never what counts.
- No comparison of strengths. The judge is told to answer for each candidate from its own records and never to
  weigh effect sizes, p-values or the number of records; code reads its answers as yes or no. A candidate nobody
  studied has no records and loses nothing: it stays tied.
- Another model than the reader's, on its own client: the second model's settings (`v9.critic` in config.yaml),
  the same budget and trace. A failed call, a refusal or a reply the cache cannot give back leaves the tie as it
  was, and the run says so.
- The instructions (prompts/judge_system.txt) were developed on variants outside the evaluated cases.
"""

import hashlib
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any, Literal, NamedTuple

from ..agent.schemas import SchemaCheckError
from . import critic as K
from . import literature as L
from . import table as T
from .graph import ClaimGraph
from .roles import GUARD, RoleCaller, Strict, fence, prompt
from .schemas import Role

JUDGE_FORMAT = 1
JUDGE: Role = "judge"              # the graph's role for the judge's readings
MAX_CANDIDATES = 6                 # candidates with experiments that one tie's packet holds
MAX_RECORDS = 8                    # experiments of one candidate in the packet, in the order they were filed
PARAGRAPH_CHARS = 2400             # characters of one paragraph in the packet
NAMES_SHOWN = 40                   # members of a TF group the packet spells out
REASON_LIMIT = 400
# Made-up candidates, by kind: the first whose name no paragraph of the packet holds and no tied chain names
PLACEBOS: dict[str, tuple[str, ...]] = {"tf": ("ZNF143", "NRF1", "YY1", "REST", "MAX", "USF1"),
                                        "gene": ("ALB", "MYOD1", "INS", "HBB", "TTN", "CFTR")}
Reading = Literal["shown", "against", "not_shown", "cannot_tell"]
Basis = Literal["alleles", "site", "none"]
# What tied chains can differ in: the kind, the names a candidate's claim holds, the candidate's own claims (a
# record counted in one of them is not read again), and the words for it.
KINDS: tuple[tuple[str, str, tuple[str, ...], str, str], ...] = (
    ("tf", "tfs", ("binding.allele", "binding.premise"), "transcription factor", "TF"),
    ("gene", "genes", ("gene.allele", "gene.premise", "trait.premise"), "target gene", "gene"),
)
KIND_WORDS = {kind: words for kind, _, _, words, _ in KINDS}
KIND_SHORT = {kind: short for kind, _, _, _, short in KINDS}
BASIS_WORDS = {
    ("tf", "alleles"): "the difference between the alleles, or the haplotypes that carry them, depends on it",
    ("tf", "site"): "the site's activity depends on it; the alleles were not compared",
    ("gene", "alleles"): "a product of the gene differs between the alleles, or the haplotypes that carry them",
    ("gene", "site"): "changing the site changes the gene; the alleles were not compared",
}
ANSWER_WORDS = {
    "shown": "an experiment ties it to the variant's site",
    "against": "an experiment of that kind changed nothing",
    "not_shown": "its experiments do not tie it to the variant's site",
    "cannot_tell": "the text does not say enough to decide",
    "disagreed": "the two readings disagreed",
    "check_failed": "a reading accepted the made-up candidate, so nothing is kept",
    "no_answer": "no answer came back",
}
FINAL = tuple(ANSWER_WORDS)


class Candidate(NamedTuple):
    """One TF (or TF group) or gene that some of the tied chains name: its kind, the table's label for it, the
    symbols it stands for, the experiments on file that name it and that no cell counts for it (at most the cap,
    in the order they were filed), and how many of those are on file in all."""
    kind: str
    label: str
    names: tuple[str, ...]
    records: tuple[str, ...]
    on_file: int


class Tie(NamedTuple):
    """A tie for first: how many chains share the first rank, the kinds they differ in, and the candidates."""
    chains: int
    differ: tuple[str, ...]
    candidates: tuple[Candidate, ...]


class Cited(Strict):
    record: int                        # the record's number in the packet
    first_sentence: int                # the sentences that state a result its quotation leaves out, by their
    last_sentence: int                 # numbers in the paragraph; 0 and 0 otherwise


# The reason comes before the answer on purpose: a reply is written in this order, and a model that commits to an
# answer first can go on to write a reason that contradicts it (it did, in development).
class CandidateCheck(Strict):
    candidate: int                     # the candidate's number in the packet
    reason: str
    answer: Reading
    basis: Basis
    records: list[Cited]


class TieCheck(Strict):
    checks: list[CandidateCheck]


class Shown(NamedTuple):
    """One block of a packet: a paragraph (its text is "" when the article cannot be loaded) with the records that
    rest on it, each as its evidence id and where its quotation sits among the paragraph's sentences."""
    source: str
    location: str
    text: str
    records: tuple[tuple[str, K.Run | None], ...]


def system_prompt() -> str:
    return prompt("judge_system")


def _num(ident: str) -> int:
    digits = "".join(ch for ch in ident if ch.isdigit())
    return int(digits) if digits else 0


# --- what is tied, and what is on file for it --------------------------------------------------------------------------

def find_tie(graph: ClaimGraph, table: T.Table | None = None, *, max_records: int = MAX_RECORDS) -> Tie | None:
    """The tie for first in a graph's chain table, or None when one chain leads or there is none. A candidate is
    listed for every TF and gene the tied chains differ in, with the experiments read from articles that name it
    and are counted in none of its own claims; a link the tied chains all fill alike gives no candidate."""
    table = table if table is not None else T.from_graph(graph)
    leaders = [c for c in table.chains if c.rank == 1]
    if len(leaders) < 2:
        return None
    read = sorted((e for e in graph.evidence.values()
                   if e.origin == "literature" and e.experiment is not None and e.experiment.passage),
                  key=lambda e: _num(e.evidence_id))
    differ, candidates = [], []
    for kind, held, slots, _, _ in KINDS:
        # by what the claim names, not by its id: chains that all name no TF hold one claim each and do not differ
        chains_of: dict[tuple[str, tuple[str, ...]], list[T.TableChain]] = {}
        for chain in leaders:
            if chain.claims.get(slots[0]):
                claim = table.claims[str(chain.claims[slots[0]])]
                chains_of.setdefault((claim.label, tuple(claim.names.get(held) or ())), []).append(chain)
        if len(chains_of) < 2:
            continue
        differ.append(kind)
        for (label, names), chains in chains_of.items():
            if not names:
                continue                                   # a chain that names no TF, or no gene: nothing to look for
            own = {str(chain.claims[slot]) for chain in chains for slot in slots if chain.claims.get(slot)}
            counted = {r.id for cid in own for cell in table.claims[cid].cells.values() for r in cell.records
                       if r.stance != "beside"}
            wanted = {n.upper() for n in names}
            found = [e.evidence_id for e in read if e.evidence_id not in counted
                     and wanted & {a.upper() for a in (e.about_tfs if kind == "tf" else e.about_genes)}]
            candidates.append(Candidate(kind, label, names, tuple(found[:max_records]), len(found)))
    return Tie(len(leaders), tuple(differ), tuple(candidates))


def placebo(graph: ClaimGraph, tie: Tie, asked: Sequence[Candidate], passages: Mapping[str, K.Passage],
            ) -> Candidate | None:
    """The made-up candidate of a packet: of the first candidate's kind and listed under its records, with a name
    that no paragraph or quotation of the packet holds and no tied chain names. None when every name is taken."""
    first = asked[0]
    held = " ".join([p.text for p in passages.values()]
                    + [graph.evidence[eid].experiment.passage for c in asked for eid in c.records]).casefold()
    taken = {n.casefold() for c in tie.candidates for n in (*c.names, c.label)}
    name = next((n for n in PLACEBOS[first.kind] if n.casefold() not in held and n.casefold() not in taken), None)
    return Candidate(first.kind, name, (name,), first.records, first.on_file) if name is not None else None


def differ_words(kinds: Sequence[str]) -> str:
    return " and the ".join(KIND_WORDS[k] for k in kinds) or "nothing code names"


# --- the packet --------------------------------------------------------------------------------------------------------

def layout(graph: ClaimGraph, candidates: Sequence[Candidate], passages: Mapping[str, K.Passage],
           ) -> tuple[list[Shown], dict[str, int]]:
    """The blocks a packet prints for these candidates, in the order the candidates first use them, and the number
    each record has in it (from 1, in the order printed). Records read from one paragraph share its block."""
    blocks: dict[tuple[str, str, str], tuple[str, dict[str, K.Run | None]]] = {}
    for candidate in candidates:
        for eid in candidate.records:
            e = graph.evidence[eid]
            text = passages[eid].text
            source = e.source_ids[0] if e.source_ids else "an article"
            key = (source, e.experiment.location, text or eid)      # without its paragraph a record stands alone
            blocks.setdefault(key, (text, {}))[1].setdefault(eid, K.quoted_run(text, e.experiment.passage))
    shown = [Shown(source, location, text, tuple(records.items()))
             for (source, location, _), (text, records) in blocks.items()]
    numbers = {eid: n for n, eid in enumerate((eid for block in shown for eid, _ in block.records), 1)}
    return shown, numbers


def _near(block: Shown) -> K.Run | None:
    """The stretch of a paragraph its records' quotations span: what a long paragraph is cut around."""
    runs = [run for _, run in block.records if run is not None]
    return (min(a for a, _ in runs), max(b for _, b in runs)) if runs else None


def _named(names: Sequence[str]) -> str:
    more = len(names) - NAMES_SHOWN
    return ", ".join(names[:NAMES_SHOWN]) + (f" and {more} more of the same group" if more > 0 else "")


def packet(graph: ClaimGraph, tie: Tie, candidates: Sequence[Candidate], passages: Mapping[str, K.Passage]) -> str:
    """What one call reads: the variant, what is tied, the candidates in the order given, and each paragraph once
    with the records that rest on it. It holds nothing of the reader's reading and no id of the run."""
    shown, numbers = layout(graph, candidates, passages)
    of: dict[str, list[int]] = {}
    for i, candidate in enumerate(candidates, 1):
        for eid in candidate.records:
            of.setdefault(eid, []).append(i)
    lines = ["Role: judge; stage: read a tie", "", *K.variant_lines(graph), "",
             f"The tie: {tie.chains} chains hold the same kinds of evidence behind every claim. They differ in the "
             f"{differ_words(tie.differ)}.", "", "Candidates"]
    for i, c in enumerate(candidates, 1):
        group = c.kind == "tf" and len(c.names) > 1
        lines.append(f"{i}. {KIND_WORDS[c.kind]}{' group (any member counts)' if group else ''}: "
                     f"{fence(_named(c.names))}")
    lines += ["", "Experiments from articles that name a candidate and that no cell of the table counts for it:"]
    for block in shown:
        lines.append("")
        if block.text:
            lines += [f"Paragraph from {fence(block.source)}, passage [{fence(block.location)}], one numbered "
                      "sentence a line:",
                      "<data>", fence("\n".join(K.numbered(block.text, _near(block), PARAGRAPH_CHARS)[0])), "</data>",
                      "Records resting on this paragraph:"]
        for eid, run in block.records:
            who = of[eid]
            names = f"candidate{'s' if len(who) > 1 else ''} {_listed([str(n) for n in who])}"
            if not block.text:
                lines += [f"Record {numbers[eid]} (names {names}), from {fence(block.source)}, passage "
                          f"[{fence(block.location)}]. Its paragraph is not available; its quotation:",
                          "<data>", fence(graph.evidence[eid].experiment.passage), "</data>"]
            elif run is None:
                lines += [f"- record {numbers[eid]}: names {names}; its quotation, which code could not place among "
                          "the numbered sentences:",
                          "<data>", fence(graph.evidence[eid].experiment.passage), "</data>"]
            else:
                where = f"sentence {run[0]}" if run[0] == run[1] else f"sentences {run[0]} to {run[1]}"
                lines.append(f"- record {numbers[eid]}: names {names}; its quotation is {where}")
    lines += ["", "Return one check for each numbered candidate, as your instructions say."]
    return "\n".join(lines)


def checked(candidates: Sequence[Candidate], shown: Sequence[Shown], numbers: Mapping[str, int]):
    """The reply check for a packet: one check per candidate, numbered as the packet numbers them; a basis exactly
    with shown or against; and records only then, at least one, each a record of that candidate, named once. A
    reply that breaks this is sent back once by the model client. Sentence numbers are not checked here: sentences
    code cannot copy (more than the reader's limits allow, or numbers the paragraph does not have) are left out
    when the answer is read, and the record keeps its own quotation, so a good answer is not lost to a bad pointer
    (in development one was)."""
    n = len(candidates)
    own = {i: {numbers[eid] for eid in c.records} for i, c in enumerate(candidates, 1)}

    def check(out: TieCheck) -> TieCheck:
        given = sorted(c.candidate for c in out.checks)
        if given != list(range(1, n + 1)):
            raise SchemaCheckError(f"return exactly one check for each of the {n} candidate(s), numbered 1 to {n}; "
                                   f"this reply numbers them {given}")
        for c in out.checks:
            tied = c.answer in ("shown", "against")
            if tied != (c.basis != "none"):
                raise SchemaCheckError(f"candidate {c.candidate}: give the basis \"alleles\" or \"site\" with shown "
                                       "or against, and \"none\" with not_shown or cannot_tell")
            cited = [r.record for r in c.records]
            if tied != bool(cited):
                raise SchemaCheckError(f"candidate {c.candidate}: list the records the answer rests on with shown "
                                       "or against (at least one), and none with not_shown or cannot_tell")
            if len(set(cited)) != len(cited):
                raise SchemaCheckError(f"candidate {c.candidate}: name each record once")
            wrong = sorted(set(cited) - own[c.candidate])
            if wrong:
                raise SchemaCheckError(f"candidate {c.candidate}: record(s) {wrong} are not listed as naming it; its "
                                       f"records are {sorted(own[c.candidate])}")
        return out
    return check


# --- the judge ---------------------------------------------------------------------------------------------------------

def _basis(kind: str, basis: str) -> str:
    return BASIS_WORDS.get((kind, basis), "")


def _reason(text: str) -> str:
    """A reason as one line, cut at a word when it is longer than the limit."""
    text = " ".join(text.split())
    return text if len(text) <= REASON_LIMIT else text[:REASON_LIMIT].rsplit(" ", 1)[0] + " …"


class Judge:
    """One run's judge (see the module docstring). `roles` makes its model calls, on the second model's client;
    `run_dir` is the folder the articles were saved in (raw/T#.json), from which a record's paragraph is loaded."""

    def __init__(self, roles: RoleCaller, run_dir: Path | str | None, *, max_candidates: int = MAX_CANDIDATES,
                 max_records: int = MAX_RECORDS):
        self.roles, self.run_dir = roles, Path(run_dir) if run_dir is not None else None
        self.max_candidates, self.max_records = max_candidates, max_records
        # a tie is read at most twice, each reading with its repair; a caller that has made calls keeps them
        roles.set_limits(getattr(roles, "calls_used", 0) + GUARD * 2, 0)
        self.stopped: str | None = None                    # cache_miss or budget_currency
        self._articles: dict[str, L.Article | None] = {}
        self._base: tuple[int, float] | None = None

    def passages(self, graph: ClaimGraph, candidates: Sequence[Candidate]) -> dict[str, K.Passage]:
        """The paragraph each record of these candidates was read from (critic.load_passage)."""
        return {eid: K.load_passage(graph, graph.evidence[eid], self.run_dir, self._articles)
                for c in candidates for eid in c.records}

    def plan(self, graph: ClaimGraph, tie: Tie) -> tuple[list[Candidate], Candidate | None, list[list[Candidate]],
                                                          dict[str, K.Passage]]:
        """How a tie is read: the candidates asked about (those with experiments, up to the cap), the made-up
        candidate, the order of candidates in each packet, and the paragraphs. Two packets: the real candidates
        then the made-up one, and the made-up one then the real ones in the opposite order. Without a made-up
        candidate (every name is taken), two orders for two or more candidates and one packet for one."""
        asked = [c for c in tie.candidates if c.records][:self.max_candidates]
        if not asked:
            return [], None, [], {}
        passages = self.passages(graph, asked)
        check = placebo(graph, tie, asked, passages)
        if check is not None:
            return asked, check, [[*asked, check], [check, *asked[::-1]]], passages
        return asked, None, [asked, asked[::-1]] if len(asked) > 1 else [asked], passages

    def packets(self, graph: ClaimGraph, tie: Tie) -> list[tuple[list[Candidate], str]]:
        """The packets a tie is read with (plan), each with its candidates in the order it lists them; none when
        no candidate has an experiment."""
        _, _, orders, passages = self.plan(graph, tie)
        return [(order, packet(graph, tie, order, passages)) for order in orders]

    def _read(self, graph: ClaimGraph, tie: Tie, order: Sequence[Candidate], passages: Mapping[str, K.Passage],
              ) -> dict[str, dict[str, Any]] | None:
        """One reading of the tie with the candidates in `order`: per candidate (by its label and kind) the
        answer, the basis, the reason and the records it rests on, each as the evidence id with the quotation code
        copied when the judge pointed outside the record's own; None when no reply came."""
        shown, numbers = layout(graph, order, passages)
        if self._base is None:
            self._base = (graph.model_usage.calls, graph.model_usage.cost_usd)
        out = self.roles.judge(system_prompt(), packet(graph, tie, order, passages), TieCheck,
                               checked(order, shown, numbers))
        graph.set_model_usage(self._base[0] + self.roles.calls_used, round(self._base[1] + self.roles.cost_usd, 6))
        if out is None:
            if self.roles.replay_miss:
                self.stopped = "cache_miss"
            elif self.roles.currency_exhausted:
                self.stopped = "budget_currency"
            return None
        by_number = {n: eid for eid, n in numbers.items()}
        where = {eid: (block.text, run) for block in shown for eid, run in block.records}
        found: dict[str, dict[str, Any]] = {}
        for check in out.checks:
            candidate = order[check.candidate - 1]
            records = []
            for cited in check.records:
                eid = by_number[cited.record]
                text, run = where[eid]
                first, last = cited.first_sentence, cited.last_sentence
                copied = (K.pointed(text, run, first, last)
                          if (first, last) != (0, 0) and not K._within(run, first, last) else None)
                records.append({"id": eid, **({"passage": copied[0], "sentences": list(copied[1])} if copied else {})})
            found[f"{candidate.kind}:{candidate.label}"] = {
                "answer": check.answer, "basis": check.basis, "records": records,
                "reason": _reason(check.reason)}
        return found

    def ask(self, graph: ClaimGraph, tie: Tie) -> dict[str, Any]:
        """Read a tie and return the judge's summary; nothing is written to the graph (see run)."""
        with_records = [c for c in tie.candidates if c.records]
        asked, check, orders, passages = self.plan(graph, tie)
        readings: list[dict[str, dict[str, Any]] | None] = []
        for order in orders:
            readings.append(self._read(graph, tie, order, passages))
            if readings[-1] is None:
                break
        # a reading that ties the made-up candidate to the site did not read the names: nothing of the tie is kept
        made_up = ([r[f"{check.kind}:{check.label}"]["answer"] for r in readings if r is not None]
                   if check is not None else [])
        fooled = any(a in ("shown", "against") for a in made_up)
        rows = []
        for c in asked:
            got = [r[f"{c.kind}:{c.label}"] if r is not None else None for r in readings]
            got += [None] * (len(orders) - len(got))
            first = got[0]
            if any(g is None for g in got):
                answer, basis, agreed = "no_answer", "none", None
            elif fooled:
                answer, basis, agreed = "check_failed", "none", False
            elif len({g["answer"] for g in got}) > 1:
                answer, basis, agreed = "disagreed", "none", False
            else:
                bases = {g["basis"] for g in got}
                answer = first["answer"]
                basis = first["basis"] if len(bases) == 1 else "site"       # the weaker reading of the two
                agreed = True if len(got) > 1 else None
            kept = first["records"] if first is not None and answer in ("shown", "against") else []
            records = []
            for r in kept:
                e = graph.evidence[r["id"]]
                records.append({"id": r["id"], "source": e.source_ids[0] if e.source_ids else "",
                                "location": e.experiment.location,
                                "passage": r.get("passage") or e.experiment.passage,
                                "pointed": bool(r.get("passage")), "sentences": r.get("sentences")})
            rows.append({"kind": c.kind, "label": c.label, "names": list(c.names), "on_file": c.on_file,
                         "sent": len(c.records), "answer": answer, "basis": basis, "agreed": agreed,
                         "reason": first["reason"] if first is not None else "",
                         "readings": [{"answer": g["answer"], "basis": g["basis"], "reason": g["reason"]}
                                      for g in got if g is not None],
                         "records": records})
        counts = {key: sum(r["answer"] == key for r in rows) for key in FINAL}
        return {"format": JUDGE_FORMAT, "chains": tie.chains, "differ": list(tie.differ),
                "candidates": len(tie.candidates), "with_experiments": len(with_records), "asked": len(asked),
                "not_sent": len(with_records) - len(asked), "orders": len(orders),
                "experiments": len({eid for c in asked for eid in c.records}), **counts,
                "check": ({"name": check.label, "kind": check.kind, "answers": made_up, "passed": not fooled}
                          if check is not None else None),
                "stopped": self.stopped, "rows": rows,
                "model_calls": self.roles.calls_used, "cost_usd": self.roles.cost_usd,
                "failures": [{"stage": f["stage"], "kind": f["kind"]} for f in self.roles.failures]}

    def run(self, graph: ClaimGraph, table: T.Table | None = None) -> dict[str, Any] | None:
        """Read the graph's tie for first, when it has one, and log what was read: one audit event per candidate
        asked about, and one with the counts, from which a table and a report show it (table.judgement). Returns
        the summary, or None when one chain leads or there is none."""
        tie = find_tie(graph, table, max_records=self.max_records)
        if tie is None:
            return None
        found = self.ask(graph, tie)
        for row in found["rows"]:
            ids = [r["id"] for r in row["records"]]
            basis = f", {row['basis']}" if row["basis"] != "none" else ""
            graph.log("audit", JUDGE,
                      f"the judge on the {KIND_SHORT[row['kind']]} {row['label']}: {row['answer']}{basis}"
                      + (f" ({row['reason']})" if row["reason"] else ""),
                      target_ids=ids, evidence_ids=ids, details={"judge": row})
        graph.log("audit", JUDGE, sentence(found),
                  details={"judge_summary": {k: v for k, v in found.items()
                                             if k not in ("rows", "model_calls", "cost_usd")}})
        return found


# --- words -------------------------------------------------------------------------------------------------------------

def _listed(items: Sequence[str]) -> str:
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def named(row: Mapping[str, Any]) -> str:
    group = row["kind"] == "tf" and len(row.get("names") or []) > 1
    return f"the {'TF group' if group else KIND_SHORT[row['kind']]} {row['label']}"


def _count(n: int, word: str) -> str:
    return f"{n} {word}{'' if n == 1 else 's'}"


def sentence(found: Mapping[str, Any] | None, rows: Sequence[Mapping[str, Any]] | None = None) -> str:
    """The judge's reading in one or two sentences, for the run's answer and a report; empty without a tie. `rows`
    are the per-candidate rows when `found` holds the counts only (as a saved graph does)."""
    if not found:
        return ""
    rows = list(found.get("rows") or rows or [])
    if not found.get("asked"):
        return ("No experiment on file names one of the tied candidates beyond the records the table counts, so "
                "nothing read from the articles separates the tied chains.")
    if all(r["answer"] == "no_answer" for r in rows):
        why = f" ({found['stopped']})" if found.get("stopped") else ""
        return (f"What is on file that no cell of the table counts ({_count(found.get('experiments', 0), 'experiment')} "
                f"on {_count(found['asked'], 'tied candidate')}) was sent to a second model, and no answer came "
                f"back{why}: the tie stands as it is.")
    to = [f"{named(r)} ({_basis(r['kind'], r['basis'])})" for r in rows if r["answer"] == "shown"]
    away = [named(r) for r in rows if r["answer"] == "against"]
    said = ([f"point to {_listed(to)}"] if to else []) + ([f"point away from {_listed(away)}"] if away else [])
    twice = (", asked twice with the candidates in opposite orders and kept only where both readings agree"
             if found.get("orders") == 2 else "")
    if twice and found.get("check"):
        twice += "; each time it also had to turn down a made-up candidate"
    read = f"{_count(found.get('experiments', 0), 'experiment')} on {_count(found['asked'], 'tied candidate')}{twice}"
    if said:
        text = (f"Among the tied chains, experiments that no cell of the table counts {' and '.join(said)}. This is "
                f"a second model's reading of {read}; it changes no cell and no rank.")
    else:
        text = (f"A second model read the experiments that no cell of the table counts ({read}): no answer that "
                "is kept ties a tied candidate to this variant's site, so the tie stands as it is.")
    for key, words in (("cannot_tell", "It could not tell for"), ("disagreed", "Its two readings disagreed on"),
                       ("check_failed", "A reading accepted the made-up candidate, so nothing is kept for"),
                       ("no_answer", "No answer came back for")):
        some = [named(r) for r in rows if r["answer"] == key]
        if some:
            text += f" {words} {_listed(some)}."
    if found.get("not_sent"):
        text += f" Beyond the cap, and not read: {_count(found['not_sent'], 'further candidate')} with experiments."
    if found.get("stopped"):
        text += f" The reading stopped early ({found['stopped']})."
    return text


def manifest_parts(roles: RoleCaller | None, chosen: Mapping[str, Any]) -> dict[str, Any]:
    """What a run with the judge records as its settings: the prompt and output schema by hash, the provider and
    model, and the caps. Without `roles`, the settings that do not depend on a run (a replay compares them with a
    saved run's)."""
    from ..agent.llm import strict_schema
    schema = json.dumps(strict_schema(TieCheck), sort_keys=True).encode()
    return {"judge_format": JUDGE_FORMAT, "max_candidates": MAX_CANDIDATES, "max_records": MAX_RECORDS,
            "paragraph_chars": PARAGRAPH_CHARS,
            "prompt_sha256": hashlib.sha256(system_prompt().encode()).hexdigest(),
            "schema_sha256": hashlib.sha256(schema).hexdigest(),
            "settings": {k: chosen[k] for k in K.DEFAULTS if k in chosen},
            "not_replayable": list(roles.unreplayable) if roles else []}
