"""The loop: after the first reading, look at where the leading chains are weakest and go back for articles.

Why: the fill looks everything up once. Its report already lists each gap of the leading chain and what would fill
it, and nothing acted on that list. An agent that goes back for evidence is the obvious next part, and the first
engine of this project showed what a free one does: of 194 requests it spent 160 on reading, and 79 readings of 40
articles ended in 16 linked experiments. So the loop here is narrow, and every part of it but one is code:

    gaps      code reads them from the table: a tie for first, then the weakest claims of the leading chain
    menu      code lists what could be done about them this round, each entry with the searches it would run
    plan      a planner model picks from the menu (or, in the baseline arm, code takes the menu in its order)
    act       code runs the searches, and the reader reads the new articles exactly as it read the first ones
    look      code builds the table again, without keeping it, and sees what changed
    stop      after MAX_ROUNDS, when a round changes no cell, when the menu is empty, or when reading has to stop

- Where it sits. Between the first reading and the linking of what was read (fill.Fill.run). A round only adds
  articles and the records filed from them. The table that is kept is built once, afterwards, by the same code
  that builds it without a loop, so it is exactly the table one pass would give over the same articles: the order
  of the rounds cannot change it. Between rounds the table is built in a scratch copy of the graph (preview).
- What a gap is. Only what can change the answer: chains that tie for first and differ in a TF or a gene, and the
  claims of the leading chain that nothing supports, that are predicted only, or that are associated only.
- What is on the menu (this first version; the actions are a registry, and each is a search and a reading):
      candidates   for a tie: the variant's names with each tied TF or gene, one search each
      join         for the pairs of TF and gene in the first chains: articles in which the TF was changed and
                   the gene read out, which the joiner reads (joiner.py); they need not name the variant
      named        for a weak claim that names a TF or a gene: the variant's names with that name
      other_names  the variant under names that are not rsIDs and whose base change is its own: spellings text
                   mining found in the articles read, a catalogue's aliases, and names the planner proposed
      follow       reviews and retellings are not read as experiments; the articles they cite where they speak of
                   the variant are
      proposed     a TF or a gene the planner remembers and the table does not hold, with the variant's names
  Not built yet, and said so in the report: reading on in a paragraph when a record was cut short, widening a
  lookup to more tissues, and anything that costs more than a reading (a model run, a cluster job).
- What a model may do. The planner sees the table, the gaps and the menu, and returns menu numbers with a reason
  each. It may also name up to MAX_PROPOSALS things from memory: a TF, a gene, another name of the variant. A
  proposal is a search term and nothing else. It is marked "from memory" wherever it is shown, a TF or gene must
  be an approved symbol, and another name of the variant must write the variant's own base change. What it
  finds is filed by the same checks as everything else, so a remembered answer with no article behind it leaves
  no trace in the table.
- What keeps it honest.
      the reader stays blind   its request holds the article and the variant, never the gap, the candidate or the
                               search that found the article (reader.read_more)
      equal effort             a tie is one action over every tied candidate: the same search for each, and the
                               new articles are read in turn, one candidate after another. A tie of more than
                               TIE_SEARCHES candidates (a random variant ties hundreds on a prediction alone) is
                               searched for none of them, and so are more than JOIN_PAIRS pairs
      effort is reported       for every search: how many articles it listed, how many were new, how many were
                               read and what came of them, by candidate
      nothing is removed       a record against a claim is filed and shown as before
  On a well-known variant the planner will remember the answer and then find its papers. Such a variant can show
  that evidence is found and filed correctly; it cannot show discovery.
- The baseline. With planner "code" no model plans: the menu is taken in its own order. With no loop at all the
  fill is what it was. The three arms differ in nothing else.
"""

import re
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any, Literal

from ..agent.schemas import SchemaCheckError
from . import joiner as J
from . import literature as L
from . import reader as RD
from . import table as T
from .graph import ClaimGraph
from .roles import GUARD, RoleCaller, Strict, fence, prompt
from .schemas import Role, ToolCall, ToolRequest
from .variant_identity import MINED_TOOL, complement, name_change, verified_aliases

LOOP_FORMAT = 1
MAX_ROUNDS = 3                     # rounds after the first reading
ROUND_ARTICLES = 10                # new articles one round sends to the reader
ACTION_RESULTS = 5                 # articles one search lists
MAX_ACTIONS = 4                    # menu entries one round runs
MAX_PROPOSALS = 3                  # names from the planner's memory in one round
JOIN_ARTICLES = 6                  # articles one round sends to the joiner
TIE_SEARCHES = 24                  # tied candidates one round searches for; a wider tie is not searched one by one
JOIN_PAIRS = 24                    # pairs of TF and gene one round searches; with more pairs none is searched
FOLLOW_REVIEWS = 4                 # reviews one round follows
FOLLOW_PER_REVIEW = 5              # articles taken from one review's citations
NAME_LIMIT = 40
MENU_SHOWN = 12                    # menu entries shown to the planner
PLANNERS = ("model", "code")
PLANNER: Role = "coordinator"      # the graph's role for the planner's choices
LOOP_PURPOSE = "the loop: articles that name the variant with what a weak or tied claim names"
FOLLOW_PURPOSE = "the loop: a review's text, for the articles it cites where it speaks of the variant"
WEAK = ("none", "prediction", "association")              # weakest first
WEAK_WORDS = {"none": "nothing supports it", "prediction": "predicted only", "association": "associated only"}
# The slots whose claims name a TF or a gene, and which list of names holds it.
CHOICES = (("binding.allele", "tfs", "transcription factor"), ("gene.allele", "genes", "target gene"))
NAMED_BY = {"binding.allele": "tfs", "binding.premise": "tfs", "gene.allele": "genes", "gene.premise": "genes",
            "trait.premise": "genes"}
TRAIT_SIDE = ("trait.premise", "trait.allele")             # put first among weak claims when a trait is given
KINDS = ("candidates", "join", "named", "other_names", "follow", "proposed")
# Equal effort means every candidate or none: a search owed to hundreds of tied candidates would be the whole round.
TOO_MANY = ". More than {n} are tied, so they are not searched for one by one"
TOO_MANY_PAIRS = ". More than {n} pairs, so they are not searched for one by one"
STOPS = {"rounds": "the last round allowed was run", "no_change": "a round changed no cell and no rank",
         "empty_menu": "nothing is left on the menu", "no_gap": "the table has no gap the loop works on",
         "reading": "reading had to stop", "dry_run": "a dry run: the first round was planned and nothing was read"}


# --- gaps --------------------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class Gap:
    """One thing the loop may work on. A tie holds the tied candidates; a weak claim holds what it names."""
    id: str
    kind: Literal["tie", "join", "weak"]
    slot: str
    state: str                                   # "<n> chains tie", "<n> pairs" or a WEAK word
    text: str
    names: tuple[tuple[str, tuple[str, ...]], ...] = ()   # (label, the names to search by), one per candidate


def _claim_words(claim: T.TableClaim) -> str:
    return f"{dict(T.STEPS)[claim.step]}: {dict(T.PARTS)[claim.part].lower()}"


def find_gaps(table: T.Table, trait_given: bool = False) -> list[Gap]:
    """The gaps of a table, in the order the loop works on them: the ties for first, then the first chain's claims
    that nothing supports, that are predicted only, and that are associated only (in the table's own order within
    each). When the request names a trait (`trait_given`), the weak claims on the way from the gene to the trait
    come before the other weak claims: the trait is where the chain has to arrive. A table with no chain has
    none."""
    leaders = [c for c in table.chains if c.rank == 1]
    if not leaders or not any(table.claims[str(i)].stated for i in leaders[0].claims.values() if i):
        return []
    gaps: list[Gap] = []
    tied: set[str] = set()
    wide: set[str] = set()                       # what a tie too wide to search names: "tfs", "genes"
    for slot, key, word in CHOICES:
        held = list({c.label: c for c in (table.claims[str(x.claims[slot])] for x in leaders)}.values())
        if len(held) < 2:
            continue
        tied.add(slot)
        names = tuple((c.label, tuple(c.names.get(key) or ())) for c in held)
        if len(names) > TIE_SEARCHES:
            wide.add(key)
        gaps.append(Gap(f"G{len(gaps) + 1}", "tie", slot, f"{len(leaders)} chains tie",
                        f"{len(leaders)} chains tie for first and differ in the {word}: "
                        + "; ".join(label for label, _ in names[:6])
                        + (f" and {len(names) - 6} more" if len(names) > 6 else "")
                        + (TOO_MANY.format(n=TIE_SEARCHES) if key in wide else ""), names))
    # which TF goes with which gene: every pair of the first chains that names both and that no record joins
    pairs: dict[str, tuple[str, tuple[str, ...]]] = {}
    for chain in leaders:
        if chain.joined:
            continue
        tf, gene = (table.claims[str(chain.claims[slot])] for slot in ("binding.allele", "gene.allele"))
        tfs, genes = _searchable(tf.names.get("tfs") or ()), _searchable(gene.names.get("genes") or ())
        if tfs and genes:
            pairs.setdefault(f"{tf.label} → {genes[0]}", (f"{tf.label} → {genes[0]}", (genes[0], *tfs)))
    if pairs:
        shown = list(pairs)[:4]
        gaps.append(Gap(f"G{len(gaps) + 1}", "join", "join", f"{len(pairs)} pair(s)",
                        ("Nothing on file shows that the transcription factor of a first chain acts on its gene: "
                         + "; ".join(shown) + (f" and {len(pairs) - 4} more" if len(pairs) > 4 else "")
                         + (TOO_MANY_PAIRS.format(n=JOIN_PAIRS) if len(pairs) > JOIN_PAIRS else "")),
                        tuple(pairs.values())))
    first = leaders[0]
    weak = []
    for slot in T.SLOT_KEYS:
        claim = table.claims[str(first.claims[slot])]
        if claim.strongest in WEAK and slot not in tied:
            weak.append((not (trait_given and slot in TRAIT_SIDE), WEAK.index(claim.strongest),
                         T.SLOT_KEYS.index(slot), slot, claim))
    for *_, slot, claim in sorted(weak, key=lambda x: x[:3]):
        # the first chain's TF (or gene) is one of the tied candidates: where they are too many to search, searching
        # for it alone would favour it, so the claim carries no name to search by
        key = NAMED_BY.get(slot, "")
        found = () if key in wide else tuple(claim.names.get(key) or ())
        gaps.append(Gap(f"G{len(gaps) + 1}", "weak", slot, claim.strongest,
                        f"{_claim_words(claim)} ({claim.label}): {WEAK_WORDS[claim.strongest]}",
                        ((claim.label, found),) if found else ()))
    return gaps


# --- the variant's names ---------------------------------------------------------------------------------------------

def _own_change(graph: ClaimGraph, name: str) -> bool:
    """Whether a name writes the case variant's own base change, on one strand or the other."""
    v = graph.case.variant
    return name_change(name) in ((v.ref, v.alt), (complement(v.ref), complement(v.alt)))


def other_names(graph: ClaimGraph, proposed: Sequence[str] = ()) -> list[str]:
    """Names of the variant that are not rsIDs and that write its own base change, each spelling once: what text
    mining marked in the articles read, the aliases a catalogue verified by position, then names the planner
    proposed. They are search terms. Whether an article's name is the variant is decided when a record is filed."""
    found = [str(o.get("text") or "") for t in graph.tool_calls.values()
             if t.execution_status == "success" and t.tool_name == MINED_TOOL
             for o in t.observations if o.get("record") == "spelling"]
    found += verified_aliases(graph)
    kept: dict[str, str] = {}
    for name in [*found, *proposed]:
        name = " ".join(name.split())
        if name and len(name) <= NAME_LIMIT and _own_change(graph, name):
            kept.setdefault(L.name_key(name), name)
    return list(kept.values())


def _quoted(name: str) -> str:
    return '"' + " ".join(str(name).replace('"', " ").split()) + '"'


def _any(names: Sequence[str]) -> str:
    """One search term for any of several names."""
    terms = [_quoted(n) for n in dict.fromkeys(names) if str(n).strip()]
    return terms[0] if len(terms) == 1 else "(" + " OR ".join(terms) + ")"


def variant_term(graph: ClaimGraph, others: Sequence[str]) -> str | None:
    """The variant in a search: any of its rsIDs or other names; None when it has neither."""
    names = [*RD.names(graph), *others]
    return _any(names) if names else None


# --- the menu ----------------------------------------------------------------------------------------------------------

@dataclass
class Search:
    """One search of an entry: who or what it is for, and the query."""
    label: str
    query: str
    from_memory: bool = False
    join: tuple[str, tuple[str, ...]] | None = None       # for the joiner: the gene, and the TF's names


@dataclass
class Entry:
    """One thing the loop could do this round."""
    number: int
    kind: str
    gaps: list[str]
    text: str
    searches: list[Search] = field(default_factory=list)
    sources: list[dict[str, Any]] = field(default_factory=list)   # follow: the reviews' rows

    def shown(self) -> dict[str, Any]:
        return {"number": self.number, "kind": self.kind, "gaps": self.gaps, "text": self.text,
                "searches": [{"for": s.label, "query": s.query, **({"from_memory": True} if s.from_memory else {})}
                             for s in self.searches],
                **({"reviews": [str(r.get("label") or r.get("pmcid") or r.get("pmid")) for r in self.sources]}
                   if self.sources else {})}


_DATABASE_ID = re.compile(r"ENS[A-Z]*[GTPR]\d{6,}(?:\.\d+)?|LOC\d+|HGNC:\d+", re.I)


def _searchable(names: Sequence[str]) -> list[str]:
    """Names as search terms, each once. A database identifier (a gene with no symbol is named by its Ensembl id)
    is left out: no article writes one."""
    return list(dict.fromkeys(str(n) for n in names if str(n).strip()
                              and not _DATABASE_ID.fullmatch(str(n).strip())))


def _assay_words() -> str:
    return "(" + " OR ".join(RD.ASSAY_WORDS) + ")"


def _with_names(label: str, variant: str, names: Sequence[str]) -> Search:
    """The search for the variant with any of a candidate's names and an assay word. A large TF group has more
    members than one query holds: names are taken in their order while the query fits, and the label then says
    how many of them were searched."""
    used: list[str] = []
    for name in names:
        if len(f"{variant} AND {_any([*used, name])} AND {_assay_words()}") > L.QUERY_LIMIT:
            break
        used.append(name)
    used = used or list(names[:1])
    cut = f" (first {len(used)} of its {len(names)} names)" if len(used) < len(names) else ""
    return Search(label + cut, f"{variant} AND {_any(used)} AND {_assay_words()}")


def followable(rows: Sequence[Mapping[str, Any]], followed: set[str]) -> list[dict[str, Any]]:
    """The articles on file that retell and were therefore not read as experiments, and that no round followed
    yet: reviews, and articles that name the variant only where they retell earlier work."""
    out: list[dict[str, Any]] = []
    for r in rows:
        retells = r.get("status") == "review" or (r.get("status") == "no_mention" and "retells" in str(r.get("why")))
        ident = str(r.get("pmcid") or r.get("pmid") or "")
        if retells and ident and ident not in followed:
            out.append(dict(r))
    return out[:FOLLOW_REVIEWS]


def build_menu(graph: ClaimGraph, gaps: Sequence[Gap], rows: Sequence[Mapping[str, Any]], *, done: set[str],
               followed: set[str], proposed_names: Sequence[str] = ()) -> list[Entry]:
    """What could be done about the gaps this round, in the order code itself would do it: the ties first, then the
    weak claims, then the two actions that serve every gap (reviews to follow, other names of the variant). A
    search that an earlier round ran is left out, and an entry with nothing left to do is not listed."""
    # A name from the planner's memory is searched under its own entry only. The variant's term in every other
    # search holds what sources gave: its rsIDs and the names on file.
    others = other_names(graph, proposed_names)
    variant = variant_term(graph, other_names(graph))
    menu: list[Entry] = []
    placed: dict[str, Entry] = {}                # a search is on the menu once, under the first entry that asks it

    def add(kind: str, served: list[str], text: str, searches: Sequence[Search] = (),
            sources: Sequence[Mapping[str, Any]] = ()) -> None:
        fresh: list[Search] = []
        for s in searches:
            if s.query in done or len(s.query) > L.QUERY_LIMIT or any(s.query == f.query for f in fresh):
                continue
            if s.query in placed:
                placed[s.query].gaps += [g for g in served if g not in placed[s.query].gaps]
                continue
            fresh.append(s)
        if fresh or sources:
            entry = Entry(len(menu) + 1, kind, list(served), text, fresh, [dict(r) for r in sources])
            menu.append(entry)
            placed.update({s.query: entry for s in fresh})

    literature = [g.id for g in gaps if g.kind != "join"]
    for gap in gaps:
        if gap.kind == "join" and len(gap.names) <= JOIN_PAIRS:
            pairs = [Search(label, J.join_query(names[1:], names[0])[0], join=(names[0], tuple(names[1:])))
                     for label, names in gap.names]
            add("join", [gap.id],
                f"For each of the {len(pairs)} pair(s) of TF and gene in the first chains, search for articles in "
                "which the TF was changed and the gene read out, the same search for each, and have the joiner "
                "read them in turn.", pairs)
    if variant is not None:
        for gap in gaps:
            named = [(label, found) for label, names in gap.names if (found := _searchable(names))]
            if not named or gap.kind == "join" or (gap.kind == "tie" and len(gap.names) > TIE_SEARCHES):
                continue
            # with an assay word, as the first reading's second search has: a claim that is tied or weak needs an
            # experiment, and a bare co-mention lists the papers that only sequence or associate
            searches = [_with_names(label, variant, names) for label, names in named]
            if gap.kind == "tie":
                add("candidates", [gap.id],
                    f"Search for articles that name the variant together with each of the {len(named)} tied "
                    f"candidates, the same search for each, and read the new ones in turn.", searches)
            else:
                add("named", [gap.id], f"Search for articles that name the variant together with "
                                       f"{named[0][0]}, and read the new ones.", searches)
    reviews = followable(rows, followed)
    if reviews and literature:
        add("follow", literature, f"Open {len(reviews)} review(s) or retelling(s) on file and read the articles "
                                  "they cite where they speak of the variant.", sources=reviews)
    if others and literature:
        genes = _searchable(sorted({g for t in graph.tool_calls.values() if t.tool_name == "variant_annotation"
                                    for g in _consequence_genes(t)}))[:3]
        near = f" AND {_any(genes)}" if genes else ""
        add("other_names", literature,
            "Search under the variant's other names (" + ", ".join(others[:4])
            + (f" and {len(others) - 4} more" if len(others) > 4 else "") + ") with an assay word, and read the "
            "new articles.",
            [Search(name, f"{_quoted(name)}{near} AND {_assay_words()}",
                    from_memory=name in proposed_names) for name in others])
    return menu


def _consequence_genes(call: ToolCall) -> list[str]:
    """Genes with a consequence in a successful annotation of the variant."""
    if call.execution_status != "success":
        return []
    return sorted({str(o["gene"]) for o in call.observations if o.get("record") == "consequence" and o.get("gene")})


# --- the planner -------------------------------------------------------------------------------------------------------

class Pick(Strict):
    action: int                                  # a menu number
    why: str


class Proposal(Strict):
    kind: Literal["tf", "gene", "variant_name"]
    name: str
    why: str


class RoundPlan(Strict):
    picks: list[Pick]
    proposals: list[Proposal]
    note: str


def system_prompt() -> str:
    return prompt("planner_system")


def checked(menu: Sequence[Entry]) -> Callable[[RoundPlan], RoundPlan]:
    """The check on a plan's form: menu numbers that exist, each once, no more than a round runs; no more proposals
    than allowed, each a short name. One correction is sent back (the model client's own retry)."""
    numbers = {e.number for e in menu}

    def check(plan: RoundPlan) -> RoundPlan:
        problems = []
        picked = [p.action for p in plan.picks]
        if any(n not in numbers for n in picked):
            problems.append(f"picks must be menu numbers ({', '.join(map(str, sorted(numbers))) or 'none'})")
        if len(set(picked)) != len(picked):
            problems.append("a menu number may be picked once")
        if len(picked) > MAX_ACTIONS:
            problems.append(f"at most {MAX_ACTIONS} picks")
        if len(plan.proposals) > MAX_PROPOSALS:
            problems.append(f"at most {MAX_PROPOSALS} proposals")
        if any(not p.name.strip() or len(p.name) > NAME_LIMIT for p in plan.proposals):
            problems.append(f"a proposed name is 1 to {NAME_LIMIT} characters")
        if problems:
            raise SchemaCheckError("; ".join(problems))
        return plan
    return check


def packet(graph: ClaimGraph, table: T.Table, gaps: Sequence[Gap], menu: Sequence[Entry], *, round_no: int,
           rounds: int, room: int, history: Sequence[Mapping[str, Any]]) -> str:
    """What the planner reads: the variant, the leading chain's eight claims in words, the gaps, the menu and what
    earlier rounds did. No article text is in it."""
    v = graph.case.variant
    case = graph.case
    known = RD.names(graph)
    lines = [
        f"Role: planner; stage: plan round {round_no} of {rounds}",
        "",
        "Variant",
        "- names: " + (", ".join(known) if known else "no rsID is recorded for it"),
        f"- {v.assembly} chr{v.chrom}:{v.pos}; reference allele {v.ref}, alternate allele {v.alt} (forward strand); "
        f"origin: {case.origin}",
    ]
    if case.supplied_disease:
        lines.append("- trait given with the request: " + fence("; ".join(case.supplied_disease)))
    leaders = [c for c in table.chains if c.rank == 1]
    lines += ["", f"The table now: {len(table.chains)} chain(s), {len(leaders)} first. The first chain's claims "
                  "(step | claim | what it names | database | model prediction | literature):"]
    for row in T.first_rows(table):
        cells = [str(x) for x in row]
        if "articles found were read" in cells[-1]:      # how many articles were read is said once, below
            cells[-1] = cells[-1].split(" (", 1)[0]
        lines.append("- " + fence(" | ".join(cells)))
    if said := T.reading_text(graph):
        lines.append("- " + fence(said))
    lines += ["", "Gaps (code lists them; you add none)"]
    lines += [f"{g.id}. {fence(g.text)}" for g in gaps]
    lines += ["", "The menu for this round"]
    for e in menu[:MENU_SHOWN]:
        lines.append(f"{e.number}. [{', '.join(e.gaps)}] {fence(e.text)}")
        lines += [f"     search for {fence(s.label)}: {fence(s.query)}" for s in e.searches[:6]]
        if len(e.searches) > 6:
            lines.append(f"     and {len(e.searches) - 6} more searches of the same form")
    lines += ["", "Earlier rounds"]
    lines += [f"- round {h['round']}: " + fence(h["text"]) for h in history] or ["- none: this is the first"]
    lines += ["", f"Room: up to {room} new article(s) are read this round; {rounds - round_no} round(s) follow.",
              "",
              f"Return the menu numbers to run (at most {MAX_ACTIONS}), most useful first, each with one sentence "
              f"on why; and, only if you remember them, up to {MAX_PROPOSALS} names to search for that the table "
              "does not hold, as your instructions say."]
    return "\n".join(lines)


def screen(graph: ClaimGraph, proposals: Sequence[Proposal]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """A plan's proposals as code takes them (kept, dropped with the reason). A TF or gene must be an approved
    symbol, and is kept under that symbol; another name of the variant must write the variant's own base change."""
    kept, dropped = [], []
    for p in proposals:
        name = " ".join(p.name.split())
        row = {"kind": p.kind, "name": name, "why": " ".join(p.why.split())[:200], "from_memory": True}
        if p.kind == "variant_name":
            if _own_change(graph, name):
                kept.append(row)
            else:
                dropped.append({**row, "dropped": "the base change it writes is not this variant's on either strand"})
            continue
        found = graph.resolver(name) if graph.resolver is not None else None
        if found is None:
            dropped.append({**row, "dropped": "not an approved gene symbol"})
        else:
            kept.append({**row, "name": found[0]})
    return kept, dropped


# --- one run -----------------------------------------------------------------------------------------------------------

COUNTED_STATES = ("supports", "disagrees", "both")         # a cell in one of these holds a record that counts


def _signature(table: T.Table) -> tuple[dict[tuple[str, str, str], dict[str, tuple[str, int]]], list[tuple[int, str]]]:
    """What a round can change: each claim's three cells (state and counted records), by what the claim says and
    names, and the order of chains. A claim's id is not used: stating a claim gives it a new one."""
    cells = {(c.step, c.part, c.label): {lane: (c.cells[lane].state,
                                                sum(r.stance != "beside" for r in c.cells[lane].records))
                                         for lane in T.LANE_KEYS} for c in table.claims.values()}
    return cells, [(c.rank, c.title) for c in table.chains]


def changes(before: T.Table, after: T.Table) -> dict[str, Any]:
    """What differs between two tables of one run: the cells that gained or lost a record that counts, in words,
    and the first chains. A cell that only went from one empty state to another is not listed."""
    old, ranks_old = _signature(before)
    new, ranks_new = _signature(after)
    words = dict(T.STEPS), dict(T.PARTS)
    changed = []
    for key in list(new) + [k for k in old if k not in new]:
        for lane in T.LANE_KEYS:
            was, now = old.get(key, {}).get(lane), new.get(key, {}).get(lane)
            if was == now or not ((was or ("",))[0] in COUNTED_STATES or (now or ("",))[0] in COUNTED_STATES):
                continue
            said = [T.STATE_WORDS.get(x[0], x[0]) + (f" ({x[1]})" if x[1] else "") if x else "no such claim"
                    for x in (was, now)]
            changed.append(f"{words[0][key[0]]}: {words[1][key[1]].lower()} ({key[2]}), {lane}: "
                           f"{said[0]} to {said[1]}")
    first = [[c.title for c in t.chains if c.rank == 1] for t in (before, after)]
    return {"cells": changed, "leaders_before": first[0][:6], "leaders_after": first[1][:6],
            "leaders_changed": first[0] != first[1], "order_changed": ranks_old != ranks_new,
            "any": bool(changed) or ranks_old != ranks_new}


class Loop:
    """One run's loop (see the module docstring). `fill` is the fill it works for, after its first reading and
    before it links what was read. `planner` makes the planner's calls; None is the baseline arm, in which code
    takes the menu in its order. `dry`: the first round is planned and its searches run, and nothing is read."""

    def __init__(self, planner: RoleCaller | None = None, *, max_rounds: int = MAX_ROUNDS,
                 round_articles: int = ROUND_ARTICLES, dry: bool = False):
        if max_rounds < 1 or round_articles < 1:
            raise ValueError("the loop needs room for at least one round and one article")
        self.planner, self.max_rounds, self.round_articles, self.dry = planner, max_rounds, round_articles, dry
        self.rounds: list[dict[str, Any]] = []
        self.stop: str | None = None
        self.done: set[str] = set()              # queries run
        self.followed: set[str] = set()          # reviews opened
        self.proposed: list[dict[str, Any]] = [] # what the planner proposed from memory and code kept
        self.failures = 0                        # rounds in which the planner gave no usable plan
        self.joiner: J.Joiner | None = None      # reads for pairs of TF and gene; made when the run starts

    # --- looking at the table --------------------------------------------------------------------------------------

    @staticmethod
    def preview(fill: Any) -> T.Table:
        """The table as it would be if the run ended now, with nothing kept: what was read is linked and assessed
        by the fill's own code in a scratch copy of the graph, the table is built, and the graph is put back. No
        second model reads anything here."""
        graph = fill.graph
        kept = (dict(fill.claims), {k: list(v) for k, v in fill.by_slot.items()}, set(fill.left_open),
                fill.links, fill.beside, fill.refused, fill.critic)
        fill.critic = None
        try:
            with graph.scratch():
                fill.attach_read()
                with graph.batch():
                    fill.assess()
                return T.from_graph(graph)
        finally:
            (fill.claims, fill.by_slot, fill.left_open, fill.links, fill.beside, fill.refused, fill.critic) = kept

    # --- planning ----------------------------------------------------------------------------------------------------

    def _plan(self, graph: ClaimGraph, table: T.Table, gaps: Sequence[Gap], menu: list[Entry],
              round_no: int) -> dict[str, Any]:
        """The round's plan: which menu entries to run and what was proposed from memory. Code's own order when
        there is no planner or it gives no usable plan."""
        fallback = {"by": "code", "picks": [{"action": e.number, "why": "the menu's own order"}
                                           for e in menu[:MAX_ACTIONS]], "proposals": [], "dropped": [], "note": ""}
        if self.planner is None:
            return fallback
        history = [{"round": r["round"], "text": r["text"]} for r in self.rounds]
        out = self.planner.plan_round(system_prompt(),
                                      packet(graph, table, gaps, menu, round_no=round_no, rounds=self.max_rounds,
                                             room=self.round_articles, history=history),
                                      RoundPlan, checked(menu))
        graph.set_model_usage(self.planner.calls_used, self.planner.cost_usd)
        if out is None:
            self.failures += 1
            kind = self.planner.failures[-1]["kind"] if self.planner.failures else "failed"
            return {**fallback, "by": "code", "note": f"the planner gave no usable plan ({kind}): code's order"}
        kept, dropped = screen(graph, out.proposals)
        return {"by": "planner", "picks": [{"action": p.action, "why": " ".join(p.why.split())[:240]}
                                           for p in out.picks],
                "proposals": kept, "dropped": dropped, "note": " ".join(out.note.split())[:300]}

    # --- acting ------------------------------------------------------------------------------------------------------

    def _search(self, fill: Any, search: Search, round_no: int, kind: str) -> tuple[ToolCall, list[dict[str, Any]],
                                                                                       int]:
        """One search: the call, the rows of the articles no earlier search listed, and how many it listed."""
        graph, reader = fill.graph, fill.reader
        call = reader.runner.run(ToolRequest(tool=L.SEARCH_TOOL, purpose=LOOP_PURPOSE,
                                             params={"query": search.query, "max_results": ACTION_RESULTS}),
                                 graph.case, graph, "code")
        reader.searches.append(call)
        self.done.add(search.query)
        rows, listed = [], 0
        for found in call.observations if call.execution_status == "success" else []:
            ids = RD._ids(found)
            if not ids:
                continue
            listed += 1
            known = reader.known(found) or next((r for r in rows if r["ids"] & ids), None)
            if known is not None:
                if call.tool_call_id not in known["found_by"]:
                    known["found_by"].append(call.tool_call_id)
                continue
            rows.append({"ids": ids, "pmid": found.get("pmid"), "pmcid": found.get("pmcid"), "doi": found.get("doi"),
                         "title": found.get("title") or "", "publication_type": found.get("publication_type") or "",
                         "found_by": [call.tool_call_id], "status": "over_cap", "why": "",
                         "loop": {"round": round_no, "action": kind, "for": search.label,
                                  **({"from_memory": True} if search.from_memory else {})}})
        return call, rows, listed

    def _cited(self, fill: Any, review: dict[str, Any], round_no: int) -> tuple[list[dict[str, Any]], int, str]:
        """The articles one review cites where it speaks of the variant, as new rows: (rows, how many it cites
        there, why none). The review's text is fetched as any article's is; it is never sent to the model."""
        graph, reader = fill.graph, fill.reader
        ident = str(review.get("pmcid") or review.get("pmid") or "")
        self.followed.add(ident)
        if (kept := reader.known(review)) is not None:
            kept["followed"] = round_no
        probe = {**review, "ids": set(review["ids"])}
        fetched = reader._fetch(graph, probe)
        if fetched is None:
            return [], 0, str(probe.get("why") or "its text could not be retrieved")
        _, article = fetched
        spelt = reader._spellings(graph, {**probe, "loop": True})
        patterns = [L._term_pattern(n) for n in [*RD.names(graph), *spelt]]
        wanted: list[str] = []
        for s in article.sections:
            folded = L.normalise_for_match(f"{s.heading} {s.text}").casefold()
            if any(p.search(folded) for p in patterns):
                wanted += [r for r in s.reference_ids if r not in wanted]
        by_id = {r.reference_id: r for r in article.references}
        label = str(review.get("label") or ident)
        rows: list[dict[str, Any]] = []
        for rid in wanted:
            ref = by_id.get(rid)
            if ref is None or not (ref.pmid or ref.pmcid):
                continue
            found = {"pmid": ref.pmid, "pmcid": ref.pmcid, "doi": ref.doi}
            ids = RD._ids(found)
            if not ids or reader.known(found) is not None or any(r["ids"] & ids for r in rows):
                continue
            rows.append({"ids": ids, "pmid": ref.pmid, "pmcid": ref.pmcid, "doi": ref.doi, "title": ref.title or "",
                         "publication_type": "", "found_by": [probe.get("read")] if probe.get("read") else [],
                         "status": "over_cap", "why": "",
                         "loop": {"round": round_no, "action": "follow", "for": label}})
            if len(rows) >= FOLLOW_PER_REVIEW:
                break
        why = "" if rows else ("it cites nothing where it speaks of the variant" if not wanted else
                                "what it cites there is already on file or has no PubMed id")
        return rows, len(wanted), why

    def _act(self, fill: Any, entries: Sequence[Entry], round_no: int) -> tuple[list[dict[str, Any]],
                                                                                 list[dict[str, Any]]]:
        """Run the entries' searches, then read the new articles in turn: one from each search, then the second of
        each, so that the cap on a round cuts every candidate alike. Returns one effort row per search and the
        rows read."""
        effort: list[dict[str, Any]] = []
        queues: list[tuple[dict[str, Any], list[dict[str, Any]]]] = []
        pairs: list[tuple[dict[str, Any], list[dict[str, Any]]]] = []      # the joiner's: one queue a pair
        for entry in entries:
            for search in entry.searches:
                if search.join is not None:
                    gene, tfs = search.join
                    call, rows, listed, held = self.joiner.search(fill.graph, search.label, tfs, gene, round_no)
                    self.done.add(search.query)
                    row = {"action": "join", "number": entry.number, "for": search.label, "query": search.query,
                           "call": call.tool_call_id, "status": f"{call.execution_status}/{call.retrieval_status}",
                           "listed": listed, "new": len(rows),
                           **({"names_searched": f"{held} of {len(tfs)}"} if held < len(tfs) else {})}
                    effort.append(row)
                    pairs.append((row, rows))
                    continue
                call, rows, listed = self._search(fill, search, round_no, entry.kind)
                row = {"action": entry.kind, "number": entry.number, "for": search.label, "query": search.query,
                       "call": call.tool_call_id, "status": f"{call.execution_status}/{call.retrieval_status}",
                       "listed": listed, "new": len(rows),
                       **({"from_memory": True} if search.from_memory else {})}
                effort.append(row)
                queues.append((row, rows))
            for review in entry.sources:
                rows, cited, why = self._cited(fill, review, round_no)
                row = {"action": "follow", "number": entry.number,
                       "for": str(review.get("label") or review.get("pmcid") or review.get("pmid")),
                       "listed": cited, "new": len(rows), **({"why": why} if why else {})}
                effort.append(row)
                queues.append((row, rows))
        ordered: list[dict[str, Any]] = []
        owner: dict[int, dict[str, Any]] = {}
        depth = max((len(rows) for _, rows in queues), default=0)
        for i in range(depth):
            for row, rows in queues:
                if i >= len(rows):
                    continue
                same = next((o for o in ordered if rows[i]["ids"] & o["ids"]), None)
                if same is not None:             # two searches of one round listed it: it is read once
                    same["found_by"] += [c for c in rows[i]["found_by"] if c not in same["found_by"]]
                    row["new"] -= 1
                    row["shared"] = row.get("shared", 0) + 1
                    continue
                ordered.append(rows[i])
                owner[id(rows[i])] = row
        read = fill.reader.read_more(fill.graph, ordered, self.round_articles, reading=not self.dry)
        # the pairs' articles, in turn as well: the first of each pair before the second of any. An article listed
        # for two pairs is read for each of them, with the passages that name that pair.
        turn: list[dict[str, Any]] = []
        for i in range(max((len(rows) for _, rows in pairs), default=0)):
            for row, rows in pairs:
                if i < len(rows):
                    turn.append(rows[i])
                    owner[id(rows[i])] = row
        joined = self.joiner.read_more(fill.graph, turn, JOIN_ARTICLES, reading=not self.dry) if turn else []
        for r in [*read, *joined]:
            row = owner[id(r)]
            row["read"] = row.get("read", 0) + (r["status"] == "read" and not r.get("duplicate"))
            row["experiments"] = row.get("experiments", 0) + int(r.get("experiments") or 0)
            row["filed"] = row.get("filed", 0) + len(r.get("accepted") or [])
            if "join" in r:
                row["joins"] = row.get("joins", 0) + len(r.get("joins") or [])
        for row in effort:
            for key in ("read", "experiments", "filed"):
                row.setdefault(key, 0)
            if row["action"] == "join":
                row.setdefault("joins", 0)
        return effort, [*read, *joined]

    # --- the run -----------------------------------------------------------------------------------------------------

    def run(self, fill: Any) -> dict[str, Any]:
        """The rounds (module docstring). Returns the loop's summary, which the fill keeps with its counts."""
        graph, reader = fill.graph, fill.reader
        self.joiner = J.Joiner(reader)
        if self.planner is not None:             # room for one plan a round, with its repair and retries
            self.planner.set_limits(self.planner.max_calls + GUARD * self.max_rounds, 0)
        table = self.preview(fill)
        first = [c.title for c in table.chains if c.rank == 1][:6]
        proposed_names: list[str] = []
        for round_no in range(1, self.max_rounds + 1):
            gaps = find_gaps(table, bool(graph.case.supplied_disease))
            if not gaps:
                self.stop = "no_gap"
                break
            menu = build_menu(graph, gaps, reader.articles, done=self.done, followed=self.followed,
                              proposed_names=proposed_names)
            plan = self._plan(graph, table, gaps, menu, round_no) if menu or self.planner is not None else None
            entries = [e for p in (plan or {}).get("picks", []) for e in menu if e.number == p["action"]]
            for p in (plan or {}).get("proposals", []):
                self.proposed.append({**p, "round": round_no})
                if p["kind"] == "variant_name":
                    proposed_names.append(p["name"])
            extra = self._proposed(graph, plan, len(menu), proposed_names) if plan else []
            entries = (entries + extra)[:MAX_ACTIONS + len(extra)]
            if not entries:
                self.stop = "empty_menu"
                # say why when a gap is there and no search for it is: a tie or a set of pairs too wide to search
                wide = [f"{len(g.names)} " + ("tied candidates" if g.kind == "tie" else "pairs of TF and gene")
                        + " are too many to search for one by one" for g in gaps
                        if (g.kind == "tie" and len(g.names) > TIE_SEARCHES)
                        or (g.kind == "join" and len(g.names) > JOIN_PAIRS)]
                self._log(graph, round_no, gaps, menu, plan, [], None, "; ".join(["nothing on the menu", *wide]))
                break
            effort, read = self._act(fill, entries, round_no)
            after = table if self.dry else self.preview(fill)
            diff = changes(table, after)
            self._log(graph, round_no, gaps, menu + extra, plan, effort, diff,
                      self._words(entries, effort, read, diff))
            table = after
            if self.dry:
                self.stop = "dry_run"
                break
            if reader.stopped:
                self.stop = "reading"
                break
            if not diff["any"]:
                self.stop = "no_change"
                break
        else:
            self.stop = "rounds"
        summary = self.summary(first, [c.title for c in table.chains if c.rank == 1][:6])
        graph.log("collect_facts", "code",
                  f"the loop: {len(self.rounds)} round(s), {summary['articles_read']} new article(s) read, "
                  f"{summary['filed']} experiment(s) filed; it stopped because {STOPS[self.stop]}",
                  details={"loop_summary": {k: v for k, v in summary.items() if k != "rounds"}})
        return summary

    def _proposed(self, graph: ClaimGraph, plan: Mapping[str, Any], offset: int,
                  proposed_names: Sequence[str]) -> list[Entry]:
        """The searches for what the planner proposed from memory this round: a TF or a gene with the variant's
        names. (Another name of the variant joins the variant's other names, and is searched under that entry in
        the next round's menu.)"""
        variant = variant_term(graph, other_names(graph))
        named = [p for p in plan.get("proposals", []) if p["kind"] in ("tf", "gene")]
        if variant is None or not named:
            return []
        searches = [Search(f"{p['name']} (from memory)", f"{variant} AND {_quoted(p['name'])} AND {_assay_words()}",
                           from_memory=True) for p in named]
        searches = [s for s in searches if s.query not in self.done]
        if not searches:
            return []
        return [Entry(offset + 1, "proposed", [],
                      "Search for articles that name the variant together with what the planner proposed from "
                      "memory: " + ", ".join(p["name"] for p in named) + ".", searches)]

    @staticmethod
    def _words(entries: Sequence[Entry], effort: Sequence[Mapping[str, Any]], read: Sequence[Mapping[str, Any]],
               diff: Mapping[str, Any]) -> str:
        kinds = list(dict.fromkeys(e.kind for e in entries))
        done = ", ".join(DID[k].format(n=sum(e["action"] == k for e in effort)) for k in kinds)
        new = sum(int(r["new"]) for r in effort)
        got = sum(r["status"] == "read" and not r.get("duplicate") for r in read)
        filed = sum(len(r.get("accepted") or []) for r in read)
        joins = sum(int(r.get("joins", 0)) for r in effort)
        what = ((f"{len(diff['cells'])} cell(s) changed" if diff["cells"] else "the order of chains changed")
                + ("; the first chains changed" if diff["leaders_changed"] else "")
                ) if diff["any"] else "no cell and no rank changed"
        return (f"{done}: {new} new article(s) listed, {got} read, {filed} experiment(s) filed"
                + (f", {joins} of them join a TF and a gene" if joins else "") + f"; {what}")

    def _log(self, graph: ClaimGraph, round_no: int, gaps: Sequence[Gap], menu: Sequence[Entry],
             plan: Mapping[str, Any] | None, effort: Sequence[Mapping[str, Any]], diff: Mapping[str, Any] | None,
             text: str) -> None:
        row = {"round": round_no, "text": text,
               "gaps": [{"id": g.id, "kind": g.kind, "slot": g.slot, "state": g.state, "text": g.text} for g in gaps],
               "menu": [e.shown() for e in menu], "plan": dict(plan) if plan else None, "effort": list(effort),
               "changed": dict(diff) if diff else None}
        self.rounds.append(row)
        graph.log("collect_facts", PLANNER if plan and plan.get("by") == "planner" else "code",
                  f"the loop, round {round_no}: {text}",
                  target_ids=[str(e["call"]) for e in effort if e.get("call")],
                  details={"loop_round": row})

    def summary(self, first: Sequence[str] = (), last: Sequence[str] = ()) -> dict[str, Any]:
        effort = [e for r in self.rounds for e in r["effort"]]
        used = (self.planner.usage.get("planner") or {}) if self.planner is not None else {}
        return {
            "format": LOOP_FORMAT, "planner": "model" if self.planner is not None else "code", "dry": self.dry,
            "max_rounds": self.max_rounds, "round_articles": self.round_articles, "rounds_run": len(self.rounds),
            "stop": self.stop, "stop_text": STOPS.get(self.stop or "", ""),
            "searches": sum(1 for e in effort if e.get("call")), "listed": sum(int(e["listed"]) for e in effort),
            "new_articles": sum(int(e["new"]) for e in effort),
            "articles_read": sum(int(e.get("read", 0)) for e in effort),
            "experiments": sum(int(e.get("experiments", 0)) for e in effort),
            "filed": sum(int(e.get("filed", 0)) for e in effort),
            "joins": sum(int(e.get("joins", 0)) for e in effort),
            "pairs_searched": sum(1 for e in effort if e["action"] == "join"),
            "pairs_joined": sorted({str(e["for"]) for e in effort if e.get("joins")}),
            "from_memory": [{k: p[k] for k in ("round", "kind", "name")} for p in self.proposed],
            "planner_failures": self.failures,
            "leaders_before": list(first), "leaders_after": list(last),
            "leaders_changed": list(first) != list(last),
            "cells_changed": sum(len((r.get("changed") or {}).get("cells", [])) for r in self.rounds),
            "model_calls": int(used.get("calls", 0)), "cost_usd": float(used.get("cost_usd", 0.0)),
            "rounds": self.rounds}


def counted_records(graph: ClaimGraph, rounds: Sequence[Mapping[str, Any]], rows: Sequence[Mapping[str, Any]]
                    ) -> dict[str, int]:
    """After the fill has linked everything: for each thing a search was for, how many of the experiments filed
    from the articles it found count for or against a claim. Keyed by "<action>: <for>"."""
    counted = {x.evidence_id for c in graph.claims.values() if not c.superseded_by for x in c.evidence_links
               if x.stance in ("supports", "contradicts")}
    out: dict[str, int] = {}
    for r in rows:
        loop = r.get("loop")
        if isinstance(loop, Mapping) and r.get("accepted"):
            key = f"{loop.get('action')}: {loop.get('for')}"
            out[key] = out.get(key, 0) + sum(e in counted for e in r["accepted"])
    return out


DID = {"candidates": "{n} search(es) for the tied candidates", "named": "{n} search(es) for what a weak claim names",
       "join": "{n} pair(s) of TF and gene searched",
       "other_names": "{n} search(es) under other names of the variant", "follow": "{n} review(s) opened",
       "proposed": "{n} search(es) for names from the planner's memory"}
ACTION_WORDS = {"candidates": "the variant with a tied candidate", "named": "the variant with what a weak claim names",
                "join": "the TF changed and the gene read out",
                "other_names": "another name of the variant", "follow": "what a review cites",
                "proposed": "the variant with a name from the planner's memory"}
EFFORT_HEADERS = ["Round", "Searched for", "Why", "Listed", "New", "Read", "Filed", "Count for a claim",
                  "Join the pair"]
NOT_BUILT = ("Not in this version of the loop: reading on in a paragraph when a record was cut short, widening a "
             "lookup to more tissues, and anything that costs more than a reading (a model run, a cluster job).")


def rounds_ran(rounds: Sequence[Mapping[str, Any]]) -> bool:
    """Whether any round did something: ran a search or opened a review."""
    return any(r.get("effort") for r in rounds)


def report_view(graph: ClaimGraph) -> dict[str, Any] | None:
    """What a report shows of the loop, from the run's own events: one line per round, and for every search what it
    was for, how many articles it listed, how many were new, how many were read, how many experiments were filed and
    how many of those count for a claim. None for a run without the loop."""
    rounds = [e.details["loop_round"] for e in graph.events if isinstance(e.details.get("loop_round"), Mapping)]
    done = next((e.details["loop_summary"] for e in reversed(graph.events)
                 if isinstance(e.details.get("loop_summary"), Mapping)), None)
    if done is None:
        return None
    articles = [e.details["reader"] for e in graph.events
                if isinstance(e.details.get("reader"), Mapping) and e.details["reader"].get("loop")]
    counted = counted_records(graph, rounds, articles)
    who = ("a planner model picked from the menu code listed" if done.get("planner") == "model" else
           "code took its own menu in order")
    lead = (f"After the first reading the loop ran {done['rounds_run']} round(s): {who}. "
            + (("It was a dry run: the searches ran and nothing was read." if done.get("searches") or rounds_ran(rounds)
                else "It was a dry run, and there was nothing to search for.") if done.get("dry") else
               f"It read {done['articles_read']} more article(s), from which {done['filed']} experiment(s) were "
               f"filed: {sum(counted.values())} count for a claim"
               + (f" and {done['joins']} show a first chain's TF acting on its gene" if done.get("joins") else "")
               + f". It stopped because {done.get('stop_text') or done.get('stop')}."))
    before, after = done.get("leaders_before") or [], done.get("leaders_after") or []
    moved = (f"First before: {'; '.join(before) or 'no chain'}. First after: {'; '.join(after) or 'no chain'}."
             if done.get("leaders_changed") else "The chains that are first did not change.")
    lines, effort = [], []
    for r in rounds:
        plan = r.get("plan") or {}
        by = "the planner" if plan.get("by") == "planner" else "code"
        lines.append(f"Round {r['round']}, planned by {by}: {r['text']}."
                     + (f" {plan['note']}" if plan.get("by") == "code" and plan.get("note") else ""))
        why = {p["action"]: p["why"] for p in plan.get("picks", [])}
        for e in r.get("effort") or []:
            what = str(e["for"]) + (" (a review)" if e["action"] == "follow" else "")
            effort.append([str(r["round"]), what, ACTION_WORDS.get(e["action"], e["action"])
                           + (f": {why[e['number']]}" if by == "the planner" and why.get(e.get("number")) else ""),
                           str(e["listed"]), str(e["new"]), str(e.get("read", 0)), str(e.get("filed", 0)),
                           "" if e["action"] == "join" else str(counted.get(f"{e['action']}: {e['for']}", 0)),
                           str(e.get("joins", 0)) if e["action"] == "join" else ""])
    memory = [f"{p['name']} ({p['kind'].replace('_', ' ')}, round {p['round']})" for p in done.get("from_memory") or []]
    return {"lead": lead, "moved": moved, "rounds": lines, "headers": EFFORT_HEADERS, "effort": effort,
            "memory": ("Proposed by the planner from memory, and used as search terms only: " + "; ".join(memory)
                       + ".") if memory else "", "not_built": NOT_BUILT}


def manifest_parts(planner: RoleCaller | None, loop: "Loop") -> dict[str, Any]:
    """What a run with the loop records as its settings: the caps, who planned, and for a planner model its prompt
    and output schema by hash and the model it ran with."""
    import hashlib
    import json

    from ..agent.llm import strict_schema
    parts: dict[str, Any] = {"loop_format": LOOP_FORMAT, "joiner": J.manifest_parts(),
                             "planner": "model" if planner is not None else "code",
                             "max_rounds": loop.max_rounds, "round_articles": loop.round_articles,
                             "action_results": ACTION_RESULTS, "max_actions": MAX_ACTIONS,
                             "max_proposals": MAX_PROPOSALS, "tie_searches": TIE_SEARCHES, "join_pairs": JOIN_PAIRS,
                             "actions": list(KINDS), "dry": loop.dry}
    if planner is not None:
        schema = json.dumps(strict_schema(RoundPlan), sort_keys=True).encode()
        parts.update(prompt_sha256=hashlib.sha256(system_prompt().encode()).hexdigest(),
                     schema_sha256=hashlib.sha256(schema).hexdigest(),
                     model=planner.role_models().get(PLANNER), not_replayable=list(planner.unreplayable))
    return parts

