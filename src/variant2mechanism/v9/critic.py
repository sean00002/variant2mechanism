"""The critic: a second model, from another provider, reads an article record against the claims it counts for.

Why: the reader (reader.py) is one model reading one article once. Code's checks on what it returns are checks of
form: the quotation is the article's own text, the TF is named in the paragraph, the assay is of a known family.
Whether the quoted sentences show what a claim states is a judgement code cannot make, and in the first run of the
reworked reader 5 of 44 counted records did not show it. A second reading by a different model is an independent
check of exactly that judgement, and the first place in this workflow where two models meet.

- Only where its answer can change a cell. A record is read when it is the only one of its stance behind a claim's
  literature cell: taking it out changes the cell, while taking out one of several leaves the cell as it was. Code
  decides this (fill.py), and reads again when an answer leaves another record alone. In the first run that read
  every record, 15 of the 58 counted stood alone, and the one cell that changed was one of those.
- One call per record, before the record is linked. The packet holds the variant, the paragraph the quotation was
  copied from as numbered sentences, which of them are the quotation, the paragraphs on either side as context, and
  the claims code counts the record for or against, each as one sentence with code's one-line label of the record.
  It holds nothing of the reader's reading (no field of the experiment, no direction, no note), no other record
  and nothing of the run. So the critic judges the article's text and not the first model's account of it, and one
  record with its claims always gives one request, which a replay takes from the response cache.
- Three answers per claim: shown, not_shown (with a fault from a fixed list and one sentence of reason) or
  cannot_tell.
- It can take a record out of the count, or point to where the result stands, and code acts, not the model. A
  claim's "not_shown" keeps the record from being linked to that claim: the table lists it as set aside, with the
  critic's reason. When the quotation stops short of a result that other sentences of the same paragraph state,
  the critic answers "shown" and names those sentences by number; code copies them, as it copies the reader's
  (the model points, code quotes), and the record keeps its place with the longer quotation. "shown" and
  "cannot_tell" otherwise leave the record where the reader and code put it, and the table says which of the two
  it was. No answer adds a record, a claim or a link, so a critic that errs on the lenient side leaves the table
  as it was.
- No reply, no change. A failed call, a provider refusal or a record beyond the cap leaves the record counted and
  listed as not reviewed; the run says how many. Nothing is retried beyond the model client's one validation retry.
- Another provider. Two readings by one model share its blind spots, so the critic's model is set apart from the
  reader's (`v9.critic` in config.yaml, else DEFAULTS): its own client, the same budget and trace.
- The instructions (prompts/critic_record_system.txt) follow from what each kind of claim needs to be shown, and
  were developed on variants outside the evaluated cases. Their author knew the five errors named above, so a test
  on those 44 records says whether the critic applies the rule, not whether it would find a new kind of error.
"""

import hashlib
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any, Literal, NamedTuple

from ..agent.schemas import SchemaCheckError
from ..config import Config, ConfigError
from . import literature as L
from .graph import ClaimGraph
from .roles import GUARD, RoleCaller, Strict, fence, prompt
from .schemas import Evidence, Role

# 2: only a record that stands alone behind a cell is read; the paragraph is shown as numbered sentences with the
# paragraphs on either side; a result the quotation leaves out can be pointed to, and code copies the sentences
CRITIC_FORMAT = 2
CRITIC: Role = "critic"            # the graph's role for the critic's verdicts
# The critic's model: Claude Sonnet 5.5 through the Anthropic API (key V2M_ANTHROPIC_API_KEY), where the reader's
# default is GPT-6 Luna through OpenRouter. `v9.critic` in config.yaml overrides any of the four. A reply the
# provider's safety filter stops is not sent again, to this model or another: the record stays counted, not reviewed.
DEFAULTS: dict[str, Any] = {"api": "anthropic", "model": "claude-sonnet-5-5", "effort": "low", "max_tokens": 4000}
LLM_KEY = "critic"                 # the model client's key the critic's settings are stored under
MAX_RECORDS = 200                  # records one run sends to the critic; the rest stay counted, listed as not reviewed
PARAGRAPH_CHARS = 3000             # characters of the quotation's paragraph in one packet
NEIGHBOUR_CHARS = 1200             # characters of the paragraph before it, and of the one after
REASON_LIMIT = 300
Verdict = Literal["shown", "not_shown", "cannot_tell"]
Fault = Literal["none", "other_entity", "not_this_variant", "no_clear_result", "no_experiment", "not_own_result",
                "other"]
FAULT_WORDS: dict[str, str] = {
    "other_entity": "the result is about another factor, gene, region or trait",
    "not_this_variant": "what was compared is not the two alleles of this variant alone",
    "no_clear_result": "the article does not report the result the record was counted as",
    "no_experiment": "the sentence states a finding with no experiment of the article behind it",
    "not_own_result": "the result is retold from earlier work, or is a hypothesis",
    "other": "the text does not show the claim",
}
STANCE_WORDS = {"supports": "FOR", "contradicts": "AGAINST"}
# What became of a record code counts. Only the first had a reply.
STATUSES: tuple[tuple[str, str], ...] = (
    ("reviewed", "read by the critic"),
    ("failed", "the critic's call failed"),
    ("not_reached", "not sent: the cap on records, or the critic had stopped"),
    ("not_alone", "not sent: another record stands with it behind every cell it counts in"),
)
Run = tuple[int, int]              # the numbers (from 1) of the first and last sentence of a stretch of a paragraph


class Asked(NamedTuple):
    """One claim a record would be counted for: the claim as a sentence, the stance code would link the record with
    (supports or contradicts) and code's one-line label of the record for that claim."""
    text: str
    stance: str
    label: str


class Passage(NamedTuple):
    """The paragraph a record's quotation was copied from ("" when its article cannot be loaded), and the paragraphs
    before and after it in the same section, which a packet shows as context only."""
    text: str
    before: str = ""
    after: str = ""


class ClaimCheck(Strict):
    claim: int                         # the claim's number in the packet
    verdict: Verdict
    fault: Fault
    reason: str
    first_sentence: int                # with shown: the sentences that state a result the quotation leaves out,
    last_sentence: int                 # by their numbers in the paragraph; 0 and 0 otherwise


class RecordCheck(Strict):
    checks: list[ClaimCheck]


class Answer(NamedTuple):
    """The critic's answer for one claim, as code acts on it. `passage` is the quotation code copied when the critic
    pointed to sentences outside the record's own quotation (`sentences`: the stretch copied); "" when it did not."""
    verdict: str
    fault: str
    reason: str
    passage: str = ""
    sentences: Run | None = None


def system_prompt() -> str:
    return prompt("critic_record_system")


# --- settings ----------------------------------------------------------------------------------------------------------

def settings(cfg: Mapping[str, Any]) -> dict[str, Any]:
    """The critic's model settings: `v9.critic` over DEFAULTS. ConfigError for a key that is not one of the four."""
    given = dict((cfg.get("v9") or {}).get("critic") or {})
    unknown = sorted(set(given) - set(DEFAULTS))
    if unknown:
        raise ConfigError(f"config.yaml: v9.critic has no setting {', '.join(unknown)} (it has "
                          f"{', '.join(DEFAULTS)})")
    return {**DEFAULTS, **given}


def critic_config(cfg: Config, chosen: Mapping[str, Any] | None = None, *, offline: bool = False) -> Config:
    """The config the critic's own model client runs with: `cfg` with the provider and, under the client's `critic`
    key, the model, effort and max_tokens of the critic's settings (`chosen`: a saved run's, for its replay).
    Everything else is the run's own, so the critic spends from the same budget. A live run needs a list price for
    the model (the client reserves a worst case before each call); offline nothing is paid, so a model the price
    list lacks gets a zero price. Through the Anthropic API the instructions, the same text in every call and most
    of what a call sends, go to the prompt cache: they are paid in full once and at the cached price afterwards."""
    s = {**settings(cfg), **(chosen or {})}
    llm = dict(cfg["llm"])
    prices = dict(llm.get("prices_per_mtok") or {})
    if s["model"] not in prices:
        if not offline:
            raise ConfigError(f"config.yaml: llm.prices_per_mtok has no price for the critic's model {s['model']}")
        prices[s["model"]] = {"input": 0.0, "output": 0.0}
    llm.update({"api": s["api"], LLM_KEY: s["model"], "prices_per_mtok": prices,
                "cache_system": s["api"] == "anthropic",
                "effort": {**(llm.get("effort") or {}), LLM_KEY: s["effort"]},
                "max_tokens": {**(llm.get("max_tokens") or {}), LLM_KEY: int(s["max_tokens"])}})
    return Config({**cfg, "llm": llm})


# --- sentences ---------------------------------------------------------------------------------------------------------

def _sentences(text: str) -> list[tuple[int, int]]:
    from .reader import sentences
    return sentences(text)


def quoted_run(text: str, passage: str) -> Run | None:
    """Where a quotation sits among its paragraph's sentences: the numbers of the first and last sentence it
    touches, or None when it cannot be placed. The reader's quotations are copied sentence by sentence, so they are
    found as they stand; a quotation an earlier route matched with its typography folded is found the same way."""
    if not text or not passage:
        return None
    at, size = text.find(passage), len(passage)
    if at < 0:
        span = L._span(text, L._quoted(passage))
        at, size = (text.find(span), len(span)) if span else (-1, 0)
    if at < 0:
        return None
    inside = [n for n, (a, b) in enumerate(_sentences(text), 1) if a < at + size and b > at]
    return (inside[0], inside[-1]) if inside else None


def numbered(text: str, run: Run | None, limit: int = PARAGRAPH_CHARS) -> tuple[list[str], list[int]]:
    """A paragraph as a packet shows it, one numbered sentence a line, and the numbers shown: every sentence when
    the paragraph fits `limit` characters, else the sentences nearest the quotation (the first ones when it could
    not be placed), with a mark where sentences were left out. A sentence keeps its number either way."""
    spans = _sentences(text)
    numbers = list(range(1, len(spans) + 1))
    if sum(b - a for a, b in spans) > limit:
        near = run or (1, 1)
        kept, used = [], 0
        for n in sorted(numbers, key=lambda n: (max(near[0] - n, n - near[1], 0), n)):
            size = spans[n - 1][1] - spans[n - 1][0]
            if kept and used + size > limit:
                break
            kept.append(n)
            used += size
        numbers = sorted(kept)
    lines, last = [], 0
    for n in numbers:
        if n != last + 1:
            lines.append("[...]")
        lines.append(f"({n}) {text[spans[n - 1][0]:spans[n - 1][1]]}")
        last = n
    if numbers and numbers[-1] != len(spans):
        lines.append("[...]")
    return lines, numbers


def pointed(text: str, run: Run | None, first: int, last: int) -> tuple[str, Run] | None:
    """The quotation code copies when the critic names sentences `first` to `last` of the paragraph as the ones
    that state a result, and the stretch it is: from the record's own quotation through the named sentences when
    that is a quotation the reader's limits allow (reader.MAX_SENTENCES consecutive sentences, and the literature
    route's length), else the named sentences alone. None when those break a limit themselves."""
    from .reader import MAX_SENTENCES
    spans = _sentences(text)

    def cut(a: int, b: int) -> tuple[str, Run] | None:
        if not 1 <= a <= b <= len(spans) or b - a >= MAX_SENTENCES:
            return None
        out = text[spans[a - 1][0]:spans[b - 1][1]]
        return (out, (a, b)) if L.PASSAGE_MIN <= len(L._quoted(out)) <= L.PASSAGE_MAX else None

    joined = cut(min(run[0], first), max(run[1], last)) if run is not None else None
    return joined or cut(first, last)


def _within(run: Run | None, first: int, last: int) -> bool:
    return run is not None and run[0] <= first <= last <= run[1]


# --- the packet --------------------------------------------------------------------------------------------------------

def variant_lines(graph: ClaimGraph) -> list[str]:
    """The variant as code knows it, in the reader's words (reader.packet)."""
    from .reader import names
    v = graph.case.variant
    known = names(graph)
    return ["Variant",
            "- names: " + (", ".join(known) if known else "no rsID is recorded for it"),
            f"- {v.assembly} chr{v.chrom}:{v.pos}; reference allele {v.ref}, alternate allele {v.alt}, both written "
            "on the forward strand (an article may write them on the other strand)"]


def _neighbour(text: str, *, end: bool) -> str:
    """A neighbouring paragraph as a packet shows it: its last NEIGHBOUR_CHARS characters when it comes before the
    quotation's paragraph, its first when it comes after."""
    if len(text) <= NEIGHBOUR_CHARS:
        return text
    return "[...] " + text[-NEIGHBOUR_CHARS:] if end else text[:NEIGHBOUR_CHARS] + " [...]"


def packet(graph: ClaimGraph, evidence: Evidence, paragraph: str | Passage, claims: Sequence[Asked]) -> str:
    """What one call reads: the variant, where the record is from, the paragraph as numbered sentences with the
    quotation marked, the paragraphs on either side, and the claims. It holds nothing of the reader's reading and
    nothing of the run, and no id a later run could number otherwise."""
    x = evidence.experiment
    shown = paragraph if isinstance(paragraph, Passage) else Passage(paragraph)
    source = evidence.source_ids[0] if evidence.source_ids else "an article"
    run = quoted_run(shown.text, x.passage)
    lines = ["Role: critic; stage: check one record", "", *variant_lines(graph), "",
             f"Record: from {fence(source)}, passage [{fence(x.location)}]", ""]
    if shown.before:
        lines += ["The paragraph before it (context only: a result stated only here does not count):",
                  "<data>", fence(_neighbour(shown.before, end=True)), "</data>", ""]
    if shown.text:
        lines += ["The paragraph the quotation was copied from, one numbered sentence a line:",
                  "<data>", fence("\n".join(numbered(shown.text, run)[0])), "</data>", ""]
    else:
        lines += ["The paragraph the quotation was copied from: not available, so judge the quotation alone.", ""]
    if shown.after:
        lines += ["The paragraph after it (context only: a result stated only here does not count):",
                  "<data>", fence(_neighbour(shown.after, end=False)), "</data>", ""]
    where = ("" if not shown.text else
             f", sentence {run[0]} of the paragraph" if run is not None and run[0] == run[1] else
             f", sentences {run[0]} to {run[1]} of the paragraph" if run is not None else
             ", which code could not place among the numbered sentences")
    lines += [f"The quotation (the sentences the record rests on{where}):",
              "<data>", fence(x.passage), "</data>", "",
              "Claims code counts this record for or against:",
              *(f"{i}. {STANCE_WORDS[c.stance]}: {fence(c.text)} Counted as: {fence(c.label)}."
                for i, c in enumerate(claims, 1)),
              "",
              "Return one check for each numbered claim, as your instructions say."]
    return "\n".join(lines)


def checked(n: int, text: str = "", run: Run | None = None):
    """The reply check for a packet of `n` claims about a quotation that is sentences `run` of the paragraph `text`:
    one check per claim, numbered as the packet numbers them; a fault exactly when the verdict is not_shown; and
    sentence numbers only with shown, naming sentences the packet shows that code can copy as a quotation. A reply
    that breaks this is sent back once by the model client."""
    from .reader import MAX_SENTENCES
    shown = set(numbered(text, run)[1]) if text else set()

    def check(out: RecordCheck) -> RecordCheck:
        numbers = sorted(c.claim for c in out.checks)
        if numbers != list(range(1, n + 1)):
            raise SchemaCheckError(f"return exactly one check for each of the {n} claim(s), numbered 1 to {n}; "
                                   f"this reply numbers them {numbers}")
        for c in out.checks:
            if (c.verdict == "not_shown") != (c.fault != "none"):
                raise SchemaCheckError(f"claim {c.claim}: give a fault with not_shown, and the fault \"none\" with "
                                       "shown or cannot_tell")
            first, last = c.first_sentence, c.last_sentence
            if (first, last) == (0, 0):
                continue
            if c.verdict != "shown":
                raise SchemaCheckError(f"claim {c.claim}: give sentence numbers only with shown, when sentences "
                                       "outside the quotation state the result; otherwise give 0 and 0")
            if not (first <= last and first in shown and last in shown):
                raise SchemaCheckError(f"claim {c.claim}: sentences {first} to {last} are not sentences of the "
                                       "paragraph shown; give the numbers printed before the sentences, or 0 and 0")
            if not _within(run, first, last) and pointed(text, run, first, last) is None:
                raise SchemaCheckError(f"claim {c.claim}: sentences {first} to {last} cannot be copied as a "
                                       f"quotation: name at most {MAX_SENTENCES} consecutive sentences, at most "
                                       f"{L.PASSAGE_MAX} characters in all, that state the result")
        return out
    return check


def refusal(check: Any) -> str:
    """Why a record is not counted for a claim the critic answered not_shown for, as the table words it."""
    reason = " ".join(check.reason.split())[:REASON_LIMIT]
    return (f"the critic, a second model, read the quotation in its paragraph: {FAULT_WORDS[check.fault]}"
            + (f" ({reason})" if reason else ""))


def load_passage(graph: ClaimGraph, evidence: Evidence, run_dir: Path | None,
                 articles: dict[str, L.Article | None] | None = None) -> Passage:
    """The passage a record's quotation was copied from, with the passages before and after it in the same section,
    read from the article its read saved in `run_dir` (raw/T#.json); empty when the article cannot be loaded (the
    packet then says so). `articles` keeps the articles already loaded, by the read's tool call."""
    articles = articles if articles is not None else {}
    ref = evidence.retrieval_ref or ""
    if ref not in articles:
        call = graph.tool_calls.get(ref)
        try:
            articles[ref] = L.load_article(run_dir, call) if call is not None and run_dir is not None else None
        except L.ExtractionRefused:
            articles[ref] = None
    article = articles[ref]
    location = evidence.experiment.location
    sections = article.sections if article is not None else []
    at = next((i for i, s in enumerate(sections) if s.location == location), None)
    if at is None:
        return Passage("")
    part = location.rpartition("/")[0]

    def beside(i: int) -> str:
        """The neighbouring passage, when it is a passage of the same section (never a legend or another section)."""
        ok = 0 <= i < len(sections) and part and sections[i].location.rpartition("/")[0] == part
        return sections[i].text if ok else ""

    return Passage(sections[at].text, beside(at - 1), beside(at + 1))


def load_paragraph(graph: ClaimGraph, evidence: Evidence, run_dir: Path | None,
                   articles: dict[str, L.Article | None] | None = None) -> str:
    """The text of the passage a record's quotation was copied from, or "" (load_passage)."""
    return load_passage(graph, evidence, run_dir, articles).text


# --- which records -----------------------------------------------------------------------------------------------------

def alone(counted: Mapping[Any, Sequence[str]], asked: Sequence[str] = ()) -> list[str]:
    """The records that stand alone: each is the only one counted under some key of `counted` (a claim and a stance:
    one side of one cell). `asked` are records already read, which are not named again. In the order first seen."""
    done = set(asked)
    return list(dict.fromkeys(ids[0] for ids in counted.values() if len(ids) == 1 and ids[0] not in done))


# --- the critic --------------------------------------------------------------------------------------------------------

class Critic:
    """One run's critic (see the module docstring). `roles` makes its model calls, on the critic's own client;
    `run_dir` is the folder the articles were saved in (raw/T#.json), from which a record's paragraph is loaded."""

    def __init__(self, roles: RoleCaller, run_dir: Path | str | None, *, max_records: int = MAX_RECORDS):
        self.roles, self.run_dir, self.max_records = roles, Path(run_dir) if run_dir is not None else None, max_records
        roles.set_limits(GUARD * max_records, 0)           # every record may take a repair and its retries
        self.rows: list[dict[str, Any]] = []
        self.stopped: str | None = None                    # cache_miss or budget_currency: no further call is made
        self.alone_not_sent = 0                            # set by the fill: records left alone that it did not send
        self._articles: dict[str, L.Article | None] = {}
        self._base: tuple[int, float] | None = None

    def passage(self, graph: ClaimGraph, evidence: Evidence) -> Passage:
        """The passage the record's quotation was copied from, with its neighbours (load_passage)."""
        return load_passage(graph, evidence, self.run_dir, self._articles)

    def paragraph(self, graph: ClaimGraph, evidence: Evidence) -> str:
        return self.passage(graph, evidence).text

    def _row(self, evidence: Evidence, claims: int) -> dict[str, Any]:
        row: dict[str, Any] = {"evidence": evidence.evidence_id,
                               "source": evidence.source_ids[0] if evidence.source_ids else "",
                               "location": evidence.experiment.location, "claims": claims}
        self.rows.append(row)
        return row

    def skip(self, evidence: Evidence, claims: int) -> None:
        """Note a record code counts that was not sent, because another record stands with it behind every cell it
        counts in: no answer about it could change a cell."""
        self._row(evidence, claims).update(status="not_alone", why="another record stands with it in every cell")

    def review(self, graph: ClaimGraph, evidence: Evidence, claims: Sequence[Asked]) -> list[Answer | None]:
        """One record against the claims it is counted for: the critic's answer for each, in the order given, or
        None for each when there was no reply (the record then stays as it is). Makes one model call, and none
        when `claims` is empty, the cap is reached or an earlier call showed that no further one can be answered."""
        if not claims:
            return []
        if self._base is None:
            self._base = (graph.model_usage.calls, graph.model_usage.cost_usd)
        row = self._row(evidence, len(claims))
        sent = sum(r["status"] in ("reviewed", "failed") for r in self.rows[:-1])
        if self.stopped or sent >= self.max_records:
            row.update(status="not_reached", why=f"the critic had stopped: {self.stopped}" if self.stopped else
                       f"the cap of {self.max_records} records")
            return [None] * len(claims)
        shown = self.passage(graph, evidence)
        run = quoted_run(shown.text, evidence.experiment.passage)
        before = self.roles.client.calls
        out = self.roles.critique(system_prompt(), packet(graph, evidence, shown, claims), RecordCheck,
                                  checked(len(claims), shown.text, run))
        row["sends"] = self.roles.client.calls - before
        graph.set_model_usage(self._base[0] + self.roles.calls_used,
                              round(self._base[1] + self.roles.cost_usd, 6))
        if out is None:
            kind = self.roles.failures[-1]["kind"] if self.roles.failures else "failed"
            row.update(status="failed", why=kind)
            if self.roles.replay_miss:
                self.stopped = "cache_miss"
            elif self.roles.currency_exhausted:
                self.stopped = "budget_currency"
            return [None] * len(claims)
        by_number = {c.claim: c for c in out.checks}
        answers = [self._answer(by_number[i], shown.text, run) for i in range(1, len(claims) + 1)]
        row.update(status="reviewed", verdicts=[a.verdict for a in answers], faults=[a.fault for a in answers],
                   extended=sum(bool(a.passage) for a in answers))
        return list(answers)

    @staticmethod
    def _answer(check: ClaimCheck, text: str, run: Run | None) -> Answer:
        """A check as code acts on it. Sentences named inside the record's own quotation add nothing; sentences
        outside it become the quotation code copies (pointed)."""
        first, last = check.first_sentence, check.last_sentence
        if check.verdict == "shown" and (first, last) != (0, 0) and not _within(run, first, last):
            found = pointed(text, run, first, last)
            if found is not None:
                return Answer(check.verdict, check.fault, check.reason, *found)
        return Answer(check.verdict, check.fault, check.reason)

    def summary(self) -> dict[str, Any]:
        """The critic's counts for one run (also the manifest's and the metrics'): the records code counts, those it
        was asked about and their claims, its verdicts, and what it could not review."""
        verdicts = [v for r in self.rows for v in r.get("verdicts", [])]
        faults = [f for r in self.rows for f in r.get("faults", []) if f != "none"]
        counts = {key: sum(r["status"] == key for r in self.rows) for key, _ in STATUSES}
        sent = [r for r in self.rows if r["status"] != "not_alone"]
        return {"format": CRITIC_FORMAT, "records": len(self.rows), "asked": len(sent), **counts,
                "claims": sum(r["claims"] for r in sent),
                **{v: verdicts.count(v) for v in ("shown", "not_shown", "cannot_tell")},
                "faults": {f: faults.count(f) for f in sorted(set(faults))},
                "records_taken_out": sum(bool(r.get("verdicts")) and all(v == "not_shown" for v in r["verdicts"])
                                         for r in self.rows),
                "extended": sum(r.get("extended", 0) for r in self.rows),
                "alone_not_sent": self.alone_not_sent,
                "corrected": sum(r.get("sends", 0) > 1 for r in self.rows),
                "model_calls": self.roles.calls_used, "cost_usd": self.roles.cost_usd,
                "failures": [{"stage": f["stage"], "kind": f["kind"]} for f in self.roles.failures],
                "stopped": self.stopped, "rows": self.rows}


def linked_items(graph: ClaimGraph, relations: Sequence[str] | None = None,
                 ) -> list[tuple[Evidence, list[tuple[str, Asked]]]]:
    """For a saved run: every experiment read from an article that counts for or against a claim, in evidence
    order, with those claims (the claim's id, and the claim as the critic is asked about it: its sentence, the
    link's stance and the rationale code linked it with). "Counts" is the table's reading (table._linked): a
    supporting or contradicting link, not from a different context, that gives a rung or tests the claim directly.
    `relations` keeps only claims of those relations. This is how the critic is run over a run made without one
    (scripts/v9_critic_check.py)."""
    from .chain import link_rung
    found: dict[str, list[tuple[str, Asked]]] = {}
    for claim in graph.claims.values():
        if relations is not None and claim.relation not in relations:
            continue
        for x in claim.evidence_links:
            ev = graph.evidence[x.evidence_id]
            if (ev.origin == "literature" and ev.experiment is not None and x.stance in STANCE_WORDS
                    and x.applicability != "different"
                    and (link_rung(x.strength, ev.evidence_class) is not None or x.strength == "direct")):
                found.setdefault(x.evidence_id, []).append(
                    (claim.claim_id, Asked(claim.assertion_text, x.stance, x.rationale or "a record of the article")))
    return [(graph.evidence[eid], claims) for eid in graph.evidence if (claims := found.get(eid))]


def counted_by_side(items: Sequence[tuple[Evidence, Sequence[tuple[str, Asked]]]]) -> dict[tuple[str, str], list[str]]:
    """The records of `items` (linked_items) under each claim and stance they count with: one side of one cell."""
    sides: dict[tuple[str, str], list[str]] = {}
    for evidence, claims in items:
        for cid, asked in claims:
            sides.setdefault((cid, asked.stance), []).append(evidence.evidence_id)
    return sides


def manifest_parts(roles: RoleCaller | None, chosen: Mapping[str, Any]) -> dict[str, Any]:
    """What a run with the critic records as its settings: the prompt and output schema by hash, the provider and
    model, and the caps. Without `roles`, the settings that do not depend on a run (a replay compares them with a
    saved run's)."""
    from ..agent.llm import strict_schema
    schema = json.dumps(strict_schema(RecordCheck), sort_keys=True).encode()
    return {"critic_format": CRITIC_FORMAT, "max_records": MAX_RECORDS, "paragraph_chars": PARAGRAPH_CHARS,
            "neighbour_chars": NEIGHBOUR_CHARS,
            "prompt_sha256": hashlib.sha256(system_prompt().encode()).hexdigest(),
            "schema_sha256": hashlib.sha256(schema).hexdigest(),
            "settings": {k: chosen[k] for k in DEFAULTS if k in chosen},
            "not_replayable": list(roles.unreplayable) if roles else []}
