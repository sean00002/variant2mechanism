"""The reader: the literature column of the chain table, filled one article at a time.

Why: in the claim-graph engine a model searched, chose what to read, re-read, extracted and proposed links in one
loop. Over 15 runs that loop made 79 reads of 40 articles and ended with 16 linked experiments, and it could not be
measured stage by stage. Here every stage but one is code, so each can be counted and replayed:

    find      code searches Europe PMC for the variant's own names (its rsIDs), once per query, and asks
              LitVar for the articles that name it under any spelling
    choose    code keeps the articles whose retrievable text names the variant, and the passages to show
    read      the model reads one article in one call and returns the experiments it reports
    file      code copies the sentences the model pointed to, checks every field against the text
              (literature.evidence_from_experiment) and files what passes as a record
    link      code decides which claims a record bears on (fill.py), through the graph's gates

- One call per article, and an article is read once. The packet is a function of the article and the variant only:
  it holds no hypothesis, no candidate and no claim, so a reply cannot be shaped by what the run hopes to find, the
  same article gives the same request in every run and arm, and a replay is answered from the response cache.
- The model points, code quotes. Each passage is shown with its location id and numbered sentences; an experiment
  names a location and a run of sentences, and code copies that stretch as the passage. A quotation is therefore
  the article's own text by construction, and what remains to check is what the experiment is about.
- One correction, for pointers only. In the first paid run a fifth of the returned experiments pointed to a stretch
  longer than a quotation may be (600 characters, four sentences), and each was lost. A reply with such a pointer,
  or one that points outside what was shown, is now sent back once with the numbers, through the model client's
  own validation retry, and the corrected reply is taken as it comes: what still breaks a limit is refused, one
  experiment at a time. Nothing else is sent back: a field code's checks refuse stays refused, so a model cannot
  bend a record until it passes.
- Two things only the reader can see are asked of it as yes or no, and code acts on them. In the first run of
  the reworked reader, 5 of 44 counted records were wrong: a reporter that compared whole haplotypes counted for
  the one variant, "inconsistent" and "not significant" differences counted as effects, and a later article's
  summary with no assay named counted as a binding assay. So an experiment now says whether what it compared
  differs at more variants than this one (only allele-specific expression, an association, may then count for a
  claim about the alleles) and whether the article itself calls the result unclear (it then counts for nothing);
  and a record whose description says the article names no assay is refused. Each of the two answers can only
  take a record out of the count.
- The model names the assay family from a fixed list, and code's own reading of the description decides wherever
  it recognises one (literature.labelled_class). In the first paid run code recognised no assay in 48 of 258
  descriptions ("allele editing", "immunoprecipitation followed by allele quantification", "dominant negative"),
  among them the experiments that mattered most. The transcripts of the two alleles compared inside heterozygous
  cells (allele-specific expression) are filed as an association: they compare the two haplotypes, not this variant
  alone, so they count as an eQTL does and never as an edit or an assay of the variant.
- The model does not search, plan, link or assess. What it remembers is not in the packet and cannot become a
  record: every record carries the passage it was read from.
- Which articles: those a search for the variant's name lists, in the search's own order (its title-or-abstract
  query first, then a query that also asks for an assay word), reviews left out, up to `max_articles` articles.
  An article whose retrieved text does not name the variant is not sent to the model. The default cap is every
  article the searches can list (3 x 10): a reading costs about a sixth of a cent, so cost is no reason to
  read fewer. The order and the cap were fixed from cost and from what a claim about a variant's alleles needs,
  never from how they score a labelled case.
- A third search, since format 4: LitVar (fill_sources.litvar_search). Articles write one variant many ways (an
  rsID, an HGVS name such as c.-124C>T, a shorthand such as C228T), and a search for the rsID lists only those
  that write the rsID. LitVar normalises the spellings to one entry, and PubTator's search over it is asked the
  second query again: the articles that name the variant, under any spelling, together with an assay word, in its
  relevance order, the first ten. They come after the Europe PMC articles, so those keep their place.
- An article only LitVar listed is read with the spellings it uses. Its text need not hold the rsID at all, so
  code asks PubTator how that article writes the variant (fill_sources.litvar_mentions), chooses the passages by
  those spellings too, and tells the model what they are. An article Europe PMC listed is read exactly as before,
  so its request is unchanged.
- Since format 5 such a spelling can also identify the variant when a record is filed. In the first run on a
  somatic mutation (TERT C228T) the search found the reporter, pull-down and base-editing articles, and 16 of
  their experiments were refused because the article writes "-124C>T" and never an rsID or a position. A record
  may now name the variant as the article does, where the quotation or its paragraph, heading or caption writes
  that name, and it counts as this variant under two checks, both code: text mining ties the name to the
  variant's rsID in that same article, and the base change the name writes is the variant's on one strand or the
  other (variant_identity._text_mined_map, which also says what is not taken). Text mining can be wrong, so each
  such record says how it was identified, and the table prints that with it. The request to the model is the
  same as in format 4, so a saved reading is filed again at no cost.
- Which passages: the abstract, every passage that names the variant, and, when the title or abstract names it (the
  article is about it), the article's other passages in document order, up to READ_CHARS characters. Introduction,
  Background and Discussion sections are left out: the literature route files a result quoted from them as a
  retelling, which counts for nothing.
- Nothing here is evidence of absence. An article that could not be retrieved, a reply that failed and a search cut
  by the cap are recorded as such; the table calls a literature cell "nothing found" only on the strength of the
  articles that were read, and its note says how many of those found that was.
- What code cannot find it does not read: LitVar knows a variant by its rsID, so a variant with none, and a
  spelling LitVar files under another entry, are still missed. That is measured, not hidden: the funnel reports
  how many articles each search listed.
"""

import re
from collections.abc import Sequence
from pathlib import Path
from typing import Any, Literal

from ..agent.schemas import SchemaCheckError
from . import literature as L
from . import proteins
from .chain import JOIN_FLAG
from .graph import ClaimGraph, GraphRefusal, article_key
from .roles import GUARD, RoleCaller, Strict, fence, prompt
from .schemas import (
    Direction,
    EvidenceClass,
    ExperimentRecord,
    ExperimentSystem,
    Manipulated,
    Role,
    ToolCall,
    ToolRequest,
)
from .tools import ToolRunner
from .variant_identity import normalise_evidence, verified_aliases

READER_FORMAT = 6                  # 2: the model names the assay family; one correction of pointers.
                                   # 3: it also says when a comparison is of haplotypes and when a result is unclear
                                   # 4: a third search (LitVar), and its articles are read with their own spellings
                                   # 5: a record may name the variant as such an article does (two checks, code)
                                   # 6: an experiment that changed a TF and read out a gene is flagged as a join
EXTRACTOR: Role = "literature_investigator"   # the graph's role for an experiment a model extracted from an article
SEARCH_RESULTS = 10                # records one search lists (the literature route's cap)
MAX_ARTICLES = 3 * SEARCH_RESULTS  # articles one run sends to the model: every article its searches can list
LITVAR_TOOL, MENTIONS_TOOL = "litvar_search", "litvar_mentions"
FETCH_FACTOR = 3                   # articles fetched per article sent: one that does not name the variant costs no call
READ_CHARS = 30_000                # characters of one article's passages in one packet
MAX_SENTENCES = 4                  # consecutive sentences one quotation may span
NOTE_LIMIT = 300
PROBLEMS_SHOWN = 12                # pointer problems one correction request lists
# The assay family the model names, and the evidence class it stands for. "other" is no class: the record is filed
# only if code itself recognises an assay in its description.
Assay = Literal["binding_assay", "reporter_assay", "chip", "perturbation", "allelic_expression", "other"]
ASSAY_CLASS: dict[str, EvidenceClass | None] = {
    "binding_assay": "binding_assay", "reporter_assay": "reporter_assay", "chip": "occupancy",
    "perturbation": "perturbation", "allelic_expression": "association", "other": None}
# A description that says the article names no assay: such a record is a statement, not an experiment.
_UNNAMED = re.compile(r"\b(?:not|un)[ -]?(?:specified|stated|described|named|given|reported)\b", re.I)
# Assay words for the second query: a claim that the alleles differ needs an experiment that compared them.
ASSAY_WORDS = ("EMSA", '"mobility shift"', "luciferase", "reporter", "MPRA", "ChIP", "CRISPR",
               '"allele-specific"', '"base editing"')
SEARCH_PURPOSE = "the reader: articles that name the variant"
LITVAR_PURPOSE = "the reader: articles that name the variant under any spelling, with an assay word"
MENTIONS_PURPOSE = "the reader: how this article writes the variant"
READ_PURPOSE = "the reader: the article's text, for one reading"
# What became of an article a search listed. Only the first two looked into its text.
STATUSES: tuple[tuple[str, str], ...] = (
    ("read", "read by the model"),
    ("no_mention", "its retrieved text does not name the variant where it reports results"),
    ("review", "a review: it retells, and a retelling is not a record"),
    ("unreadable", "its text could not be retrieved"),
    ("failed", "the model call failed"),
    ("over_cap", "not reached: the cap on articles per run"),
)
LOOKED = ("read", "no_mention")
# A full stop after one of these does not end a sentence.
ABBREVIATIONS = frozenset({"fig", "figs", "al", "vs", "ref", "refs", "no", "e.g", "i.e", "etc", "approx", "ca", "cf",
                           "dr", "eq", "supp", "suppl", "tab", "resp", "nos"})
_BOUNDARY = re.compile(r"[.!?][\"')\]]?\s+(?=[A-Z0-9(\[\"'])")


# --- what the model returns --------------------------------------------------------------------------------------------

class ReadExperiment(Strict):
    location: str
    first_sentence: int
    last_sentence: int
    organism: str
    tissue_or_cell: str
    treatment: str
    genotype_or_allele: str
    assay: Assay
    intervention: str
    endpoint: str
    comparator: str
    result: str
    direction: Direction
    about_tfs: list[str]
    about_genes: list[str]
    about_elements: list[str]
    about_traits: list[str]
    about_variants: list[str]
    manipulated: Manipulated
    compared_allele: str | None
    authors_hypothesis_vs_result: Literal["result", "hypothesis", "mixed"]
    scope_does_not_test: str
    haplotype: bool                    # what was compared differs at more variants than the one asked about
    unclear: bool                      # the article calls the difference not significant, a trend or inconsistent


def reader_flags(x: ReadExperiment, evidence: Any, resolver: Any = None,
                 tfs: frozenset[str] | None = None) -> dict[str, Any]:
    """Data flags a reading adds to a filed record, for code's linking (fill.read_targets). Two come from the model
    alone, and each can only take a record out of the count, never put one in: `haplotype_comparison` (the
    comparison is between haplotypes of several variants) and `unclear_result` (the article itself calls the
    difference not significant, a trend or inconsistent). `allele_specific` needs both keys: the reader says the
    ChIP compared the alleles, and code found the allele named as an allele in the quotation. The engine sets that
    flag only when the paragraph says "allele-specific" or the quotation names both alleles, which misses "reads
    showed strong preferential binding to the G-allele in the heterozygous lines".

    For ChIP, code also says which of the proteins named do not bind DNA by sequence (proteins.py: an approved gene
    symbol that is not on the TF list; a name that is no approved symbol stays unknown and is treated as a TF).
    `not_tf` lists them, and `allele_specific_cofactor` is set when the reads are allele-specific and every protein
    named is one: such a record bears on the site's regulatory activity, not on a TF's binding. Without the TF list
    (`tfs` None) neither is set and the record is linked as before."""
    flags: dict[str, Any] = {}
    if x.haplotype:
        flags["haplotype_comparison"] = True
    if x.unclear:
        flags["unclear_result"] = True
    if evidence.evidence_class == "occupancy" and x.manipulated == "allele" and evidence.allele:
        flags["allele_specific"] = True
    # An experiment that changed a TF and read out another gene's RNA or protein shows the TF acting on that gene.
    # No cell counts it (it compares no alleles and tests no element); chain.py uses it to tell which TF and gene
    # of a tie belong together. Not flagged: a measured null, a result the article calls unclear, a readout that
    # is not a gene product, and a "gene" that is the TF itself.
    if (x.manipulated == "tf" and evidence.evidence_class == "perturbation" and not x.unclear
            and evidence.about_tfs and evidence.result_kind != "null_in_assessed_scope"
            and L._endpoint_category(x.endpoint) == "expression"):
        def symbol(name: str) -> str:
            """The approved symbol of a name the article uses, where it has one (C/EBP-alpha is CEBPA). The flag
            holds symbols, so that the order of chains can be read from the saved graph alone."""
            found = resolver(str(name)) if resolver is not None else None
            return found[0] if found else str(name)

        changed = [symbol(t) for t in evidence.about_tfs]
        genes = [g for g in dict.fromkeys(symbol(g) for g in evidence.about_genes)
                 if g.upper() not in {t.upper() for t in changed}]
        if genes:
            flags[JOIN_FLAG] = {"tfs": list(dict.fromkeys(changed)), "genes": genes}
    if evidence.evidence_class == "occupancy" and tfs is not None and resolver is not None:
        other = [name for name in evidence.about_tfs
                 if (found := resolver(name)) is not None and proteins.kind(found[0], tfs) == proteins.NOT_TF]
        if other:
            flags[proteins.NOT_TF_NAMES] = other
            allelic = flags.get("allele_specific") or evidence.data.get("allele_specific") is True
            if allelic and len(other) == len(evidence.about_tfs):
                flags[proteins.COFACTOR_FLAG] = True
    return flags


class ArticleReading(Strict):
    experiments: list[ReadExperiment]
    note: str


def system_prompt() -> str:
    return prompt("reader_system")


# --- sentences ---------------------------------------------------------------------------------------------------------

def sentences(text: str) -> list[tuple[int, int]]:
    """(start, end) of each sentence of a passage, in order and without surrounding space. A sentence ends at a full
    stop, question or exclamation mark followed by space and a capital, a digit or an opening bracket or quote,
    unless the stop follows an abbreviation (Fig., et al., vs.) or a single letter (E. coli, an initial). Splitting
    too often costs nothing, since a quotation may span several sentences; the split only has to be the same every
    time, which it is: it reads nothing but the text."""
    bounds = [0]
    for m in _BOUNDARY.finditer(text):
        if text[m.start()] == ".":
            words = text[max(0, m.start() - 12):m.start()].split()
            word = words[-1].lstrip("([\"'").casefold() if words else ""
            if word in ABBREVIATIONS or (len(word) == 1 and word.isalpha()):
                continue
        bounds.append(m.end())
    bounds.append(len(text))
    found = []
    for start, end in zip(bounds, bounds[1:], strict=False):
        while start < end and text[start].isspace():
            start += 1
        while end > start and text[end - 1].isspace():
            end -= 1
        if end > start:
            found.append((start, end))
    return found


# --- which articles, which passages --------------------------------------------------------------------------------------

def names(graph: ClaimGraph) -> list[str]:
    """The names code can search by: the variant's rsIDs (the request's, then those a tool reports at its exact
    coordinates and alleles)."""
    return list(dict.fromkeys(x for x in [graph.case.variant.rsid, *sorted(graph.variant_aliases)] if x))


def queries(name: str) -> list[str]:
    """The two searches for one name: articles that name it in their title or abstract, then articles that name it
    anywhere together with an assay word."""
    return [f'TITLE_ABS:"{name}"', f'"{name}" AND ({" OR ".join(ASSAY_WORDS)})']


def _ids(record: dict[str, Any]) -> set[str]:
    keys = {article_key(record.get("pmid")), article_key(record.get("pmcid"), pmcid=True),
            article_key(record.get("doi"))}
    return {k for k in keys if k}


def choose(article: L.Article, ids: Sequence[str]) -> tuple[list[L.ArticleSection], int]:
    """The passages one call shows, in document order, and how many passages name the variant at all (module
    docstring: the abstract, the passages that name the variant, then the rest of an article that is about it; never
    a section that retells; READ_CHARS characters in all). Empty when no passage outside a retelling section names
    the variant: there is then nothing a record could be read from."""
    patterns = [L._term_pattern(n) for n in ids]

    def named(text: str) -> bool:
        folded = L.normalise_for_match(text).casefold()
        return any(p.search(folded) for p in patterns)

    sections = article.sections
    told = {i for i, s in enumerate(sections) if L._retold(s, "") is not None}
    hits = [i for i, s in enumerate(sections) if named(f"{s.heading} {s.text}")]
    reported = [i for i in hits if i not in told]
    if not reported:
        return [], len(hits)
    abstract = [i for i, s in enumerate(sections) if s.location.startswith("abstract/")]
    about = named(article.title) or any(i in abstract for i in hits)
    rest = [i for i in range(len(sections)) if i not in told] if about else []
    chosen: list[int] = []
    used = 0
    for i in dict.fromkeys([*abstract, *reported, *rest]):
        size = len(sections[i].text)
        if used + size <= READ_CHARS:
            chosen.append(i)
            used += size
    return [sections[i] for i in sorted(chosen)], len(hits)


def render(chosen: Sequence[L.ArticleSection]) -> str:
    """The passages as the model sees them: each under its location id and heading, one numbered sentence a line."""
    lines: list[str] = []
    for s in chosen:
        lines.append(f"[{s.location}]" + (f" {s.heading}" if s.heading else ""))
        lines += [f"({n}) {s.text[a:b]}" for n, (a, b) in enumerate(sentences(s.text), 1)]
        lines.append("")
    return fence("\n".join(lines).rstrip())


def packet(graph: ClaimGraph, article: L.Article, chosen: Sequence[L.ArticleSection],
           spellings: Sequence[str] = (), aliases: Sequence[str] = ()) -> str:
    """What one call reads: the variant as code knows it, the article's identifiers and the chosen passages. It
    holds nothing of the run (no claim, candidate, hypothesis or budget) and nothing volatile, so one article and
    one variant always give one request. `spellings`: how this article writes the variant, for an article only
    LitVar listed; without any the packet is what it was before LitVar was asked. `aliases`: the names a catalogue
    lists for the variant, for an article the loop found; the same for every such article of one variant."""
    v = graph.case.variant
    known = names(graph)
    where = f"{article.journal} {article.year or ''}".strip()
    spelt = ([f"- this article writes it as: {fence('; '.join(spellings))} (marked by text mining, which can be "
              "wrong: an experiment is about this variant only if its passage, heading or legend says so; name it "
              "as the passage does)"] if spellings else [])
    listed = ([f"- a catalogue lists it under these names: {fence('; '.join(aliases))} (an article may use one: an "
               "experiment is about this variant only if its passage, heading or legend says so; name it as the "
               "passage does)"] if aliases else [])
    lines = [
        "Role: reader; stage: read one article",
        "",
        "Variant",
        "- names: " + (", ".join(known) if known else "no rsID is recorded for it"),
        *spelt,
        *listed,
        f"- {v.assembly} chr{v.chrom}:{v.pos}; reference allele {v.ref}, alternate allele {v.alt}, both written on "
        "the forward strand (an article may write them on the other strand)",
        "",
        f"Article: {fence(article.title)}",
        f"- {', '.join(article.source_ids())}" + (f"; {fence(where)}" if where else "")
        + (f"; publication type: {fence(article.publication_type)}" if article.publication_type else ""),
        "- access: " + ("full text" if article.access == "full_text" else
                        "abstract only (methods, controls and full results were not retrieved)"),
        f"- passages shown: {len(chosen)} of {len(article.sections)}",
        "",
        "<data>",
        render(chosen),
        "</data>",
        "",
        "Return the experiments this article reports, as your instructions say. Point to each result by the "
        "location id in square brackets and the numbers of its first and last sentence.",
    ]
    return "\n".join(lines)


def locate(x: ReadExperiment, shown: Sequence[L.ArticleSection]) -> tuple[L.ArticleSection, str]:
    """The passage shown that an experiment points to and the stretch of it that its sentence numbers name. Refused
    when it points outside what was shown or spans more sentences than a quotation may."""
    location = x.location.strip().strip("[]").strip()
    section = next((s for s in shown if s.location == location), None)
    if section is None:
        raise L.ExtractionRefused(f"{x.location!r} is not the location id of a passage shown")
    spans = sentences(section.text)
    first, last = x.first_sentence, x.last_sentence
    if not 1 <= first <= last <= len(spans):
        raise L.ExtractionRefused(f"sentences {first} to {last} are not sentences of {location}, which has "
                                  f"{len(spans)}")
    if last - first >= MAX_SENTENCES:
        raise L.ExtractionRefused(f"a quotation spans at most {MAX_SENTENCES} consecutive sentences (this one, "
                                  f"{last - first + 1})")
    return section, section.text[spans[first - 1][0]:spans[last - 1][1]]


def pointer_problems(reading: "ArticleReading", shown: Sequence[L.ArticleSection]) -> list[str]:
    """What is wrong with where a reading's experiments point, one line per experiment, in words the model can act
    on: a location that was not shown, sentence numbers the passage does not have, more sentences than a quotation
    may span, or a stretch longer or shorter than the literature route verifies. Empty when every pointer is good.
    Only pointers are looked at: what an experiment says is checked when it is filed."""
    problems = []
    for i, x in enumerate(reading.experiments):
        try:
            _, passage = locate(x, shown)
        except L.ExtractionRefused as r:
            problems.append(f"experiment {i}: {r.reason}")
            continue
        size = len(L._quoted(passage))
        if size > L.PASSAGE_MAX:
            problems.append(f"experiment {i}: sentences {x.first_sentence} to {x.last_sentence} of [{x.location}] "
                            f"are {size} characters, and a quotation holds at most {L.PASSAGE_MAX}: point to the "
                            "one or two sentences that state the result")
        elif size < L.PASSAGE_MIN:
            problems.append(f"experiment {i}: sentence {x.first_sentence} of [{x.location}] is {size} characters, "
                            f"too short to verify: point to the sentence that states the result")
    return problems


def correction(problems: Sequence[str]) -> str:
    """The text sent back with a reply whose pointers break a limit (at most PROBLEMS_SHOWN of them)."""
    more = len(problems) - PROBLEMS_SHOWN
    return ("some experiments do not point to a quotation code can copy. Change only where they point (location, "
            "first_sentence, last_sentence), keep every other experiment and field as it is, and drop an experiment "
            "only if no sentence shown states its result. " + "; ".join(problems[:PROBLEMS_SHOWN])
            + (f"; and {more} more with the same fault" if more > 0 else ""))


def record(x: ReadExperiment, article: L.Article, shown: Sequence[L.ArticleSection]) -> ExperimentRecord:
    """A returned experiment as the literature route's record, with the passage copied from the sentences it points
    to and the article's identifiers filled in by code (the model never writes either). Refused when it points
    outside what was shown."""
    section, passage = locate(x, shown)
    return ExperimentRecord(
        source_id=article.source_ids()[0], pmcid=article.pmcid, doi=article.doi,
        publication_type=article.publication_type, access=article.access, location=section.location,
        passage=passage,
        system=ExperimentSystem(organism=x.organism, tissue_or_cell=x.tissue_or_cell, treatment=x.treatment,
                                genotype_or_allele=x.genotype_or_allele),
        intervention=x.intervention, endpoint=x.endpoint, comparator=x.comparator, result=x.result,
        direction=x.direction, scope_does_not_test=x.scope_does_not_test, about_tfs=list(x.about_tfs),
        about_genes=list(x.about_genes), about_elements=list(x.about_elements), about_traits=list(x.about_traits),
        about_variants=[" ".join(v.split()) for v in x.about_variants if v.strip()], manipulated=x.manipulated,
        compared_allele=(x.compared_allele or "").strip() or None,
        authors_hypothesis_vs_result=x.authors_hypothesis_vs_result)


# --- the reader --------------------------------------------------------------------------------------------------------

class Reader:
    """One run's reading (see the module docstring). `roles` makes the model calls and counts them; `runner` runs the
    searches and fetches the articles, as role code, into the run folder. `max_articles` caps the model calls."""

    def __init__(self, roles: RoleCaller, runner: ToolRunner, *, max_articles: int = MAX_ARTICLES):
        if max_articles < 1:
            raise ValueError("the reader needs room for at least one article")
        self.roles, self.runner, self.max_articles = roles, runner, max_articles
        roles.set_limits(GUARD * max_articles, 0)          # every article may take a repair and its retries
        self.articles: list[dict[str, Any]] = []
        self.searches: list[ToolCall] = []
        self.stopped: str | None = None                    # cache_miss or budget_currency: reading could not go on
        # A dry run of the loop sends no model anything: it reads what the response cache holds and lists what
        # it does not, instead of stopping at the first article whose reading is not saved.
        self.keep_going = False

    # --- find ----------------------------------------------------------------------------------------------------------

    def find(self, graph: ClaimGraph) -> list[dict[str, Any]]:
        """The articles the searches list, each once, in the order found: one row per article with its ids, title,
        publication type and the searches that listed it."""
        rows: list[dict[str, Any]] = []
        for name in names(graph):
            for query in queries(name):
                call = self.runner.run(ToolRequest(tool=L.SEARCH_TOOL, purpose=SEARCH_PURPOSE,
                                                   params={"query": query, "max_results": SEARCH_RESULTS}),
                                       graph.case, graph, "code")
                self.searches.append(call)
                for found in call.observations if call.execution_status == "success" else []:
                    ids = _ids(found)
                    if not ids:
                        continue
                    row = next((r for r in rows if r["ids"] & ids), None)
                    if row is None:
                        row = {"ids": set(), "pmid": None, "pmcid": None, "doi": None, "title": "",
                               "publication_type": "", "found_by": [], "status": "over_cap", "why": ""}
                        rows.append(row)
                    row["ids"] |= ids
                    for key in ("pmid", "pmcid", "doi", "title", "publication_type"):
                        row[key] = row[key] or found.get(key) or row[key]
                    if call.tool_call_id not in row["found_by"]:
                        row["found_by"].append(call.tool_call_id)
        self._litvar(graph, rows)
        return rows

    def _has(self, tool: str) -> bool:
        return any(spec.name == tool for spec in self.runner.specs("literature"))

    def _litvar(self, graph: ClaimGraph, rows: list[dict[str, Any]]) -> None:
        """The third search (module docstring): the articles LitVar lists for the variant with an assay word, added
        after those Europe PMC listed. A row only LitVar listed is marked, so it is read with the spellings the
        article uses; one Europe PMC listed as well keeps the request it always had."""
        if not names(graph) or not self._has(LITVAR_TOOL):
            return
        call = self.runner.run(ToolRequest(tool=LITVAR_TOOL, purpose=LITVAR_PURPOSE,
                                           params={"words": list(ASSAY_WORDS)}), graph.case, graph, "code")
        self.searches.append(call)
        for found in call.observations if call.execution_status == "success" else []:
            ids = _ids(found) if found.get("record") == "paper" else set()
            if not ids:
                continue
            row = next((r for r in rows if r["ids"] & ids), None)
            if row is None:
                row = {"ids": set(), "pmid": None, "pmcid": None, "doi": None, "title": "", "publication_type": "",
                       "found_by": [], "status": "over_cap", "why": "", "litvar_only": True}
                rows.append(row)
            row["ids"] |= ids
            for key in ("pmid", "pmcid", "doi", "title"):
                row[key] = row[key] or found.get(key) or row[key]
            if call.tool_call_id not in row["found_by"]:
                row["found_by"].append(call.tool_call_id)

    def _spellings(self, graph: ClaimGraph, row: dict[str, Any]) -> list[str]:
        """How an article only LitVar listed writes the variant (PubTator's marks in its text); nothing for any
        other article, for one with no PubMed id, or when the lookup fails. An article a later round of the loop
        found (loop.py) is asked about too: it was found by something other than the rsID."""
        if (not (row.get("litvar_only") or row.get("loop")) or not row.get("pmid")
                or not self._has(MENTIONS_TOOL)):
            return []
        call = self.runner.run(ToolRequest(tool=MENTIONS_TOOL, params={"pmid": str(row["pmid"])},
                                           purpose=MENTIONS_PURPOSE), graph.case, graph, "code")
        row["spellings_call"] = call.tool_call_id or None
        if call.execution_status != "success":
            return []
        return [str(o["text"]) for o in call.observations if o.get("record") == "spelling" and o.get("text")]

    # --- read ----------------------------------------------------------------------------------------------------------

    def _fetch(self, graph: ClaimGraph, row: dict[str, Any]) -> tuple[ToolCall, L.Article] | None:
        """The article's text, saved in the run folder by the read tool; None (and the row says why) when it cannot
        be retrieved."""
        params: dict[str, Any] = {"focus": names(graph)}
        if row["pmcid"]:
            params["pmcid"] = row["pmcid"]
        elif row["pmid"]:
            params["pmid"] = row["pmid"]
        else:
            row.update(status="unreadable", why="the search gave no PMID or PMCID to read it by")
            return None
        call = self.runner.run(ToolRequest(tool=L.READ_TOOL, params=params, purpose=READ_PURPOSE), graph.case, graph,
                               "code")
        row["read"] = call.tool_call_id or None
        if (call.execution_status != "success" or call.retrieval_status not in L.EVIDENCE_FROM
                or not call.read_article or self.runner.run_dir is None):
            row.update(status="unreadable", why=call.message or f"{call.execution_status}/{call.retrieval_status}")
            return None
        try:
            return call, L.load_article(Path(self.runner.run_dir), call)
        except L.ExtractionRefused as r:
            row.update(status="unreadable", why=r.reason)
            return None

    def _file(self, graph: ClaimGraph, x: ReadExperiment, index: int, article: L.Article, call: ToolCall,
              shown: Sequence[L.ArticleSection], spelt: Sequence[str] = ()) -> str | None:
        """One returned experiment as a record, or None after its refusal is logged with the reason. `spelt`: how
        text mining says this article writes the variant, by which a record may name it (module docstring)."""
        try:
            rec = record(x, article, shown)
            if _UNNAMED.search(x.intervention):
                raise L.ExtractionRefused("the record says the article does not name the assay or the method: a "
                                          "finding with none named is a statement, not an experiment")
            evidence = L.evidence_from_experiment(rec, call, article, resolver=graph.resolver,
                                                  label=ASSAY_CLASS[x.assay], own_figures=True, mined=spelt)
            evidence = normalise_evidence(evidence, graph, article=article)
            flags = reader_flags(x, evidence, graph.resolver, proteins.tf_symbols(self.runner.config))
            evidence = evidence.model_copy(update={"data": {**evidence.data, **flags}})
            return graph.add_evidence(evidence, EXTRACTOR, f"experiment read from {article.key} {rec.location}")
        except L.ExtractionRefused as r:
            reason = r.reason
        except GraphRefusal as r:
            reason = r.reason
        except Exception as e:  # a failed extraction is a refusal, never a crash
            reason = f"{type(e).__name__}: {e}"
        graph.log("refuse_update", EXTRACTOR, f"experiment {index} of {article.key} refused: {reason}",
                  target_ids=[call.tool_call_id],
                  details={"kind": "add_evidence", "reader": True, "article": article.key,
                           "experiment_index": index, "experiment": x.model_dump(mode="json")})
        return None

    def read(self, graph: ClaimGraph, row: dict[str, Any]) -> None:
        """One article: fetch, choose, one model call, file. The row records what happened."""
        if L._REVIEW.search(row["publication_type"] or ""):
            row.update(status="review", why="indexed as a review")
            return
        fetched = self._fetch(graph, row)
        if fetched is None:
            return
        call, article = fetched
        row.update(article=article.key, access=article.access, title=row["title"] or article.title)
        if any(a.get("article") == article.key and a is not row for a in self.articles):
            row.update(status="read", why="the same article as an earlier row", duplicate=True)
            return
        if article.is_review:
            row.update(status="review", why="a review article")
            return
        spelt = self._spellings(graph, row)
        # An article the loop found may write the variant by a name a catalogue lists for it and verified by
        # position (a somatic mutation's shorthand). Its passages are chosen by those names too, and the model is
        # told them. Every article of the first reading is read exactly as before.
        listed = verified_aliases(graph) if row.get("loop") else []
        shown, named = choose(article, [*names(graph), *spelt, *listed])
        row.update(passages=len(article.sections), passages_naming=named, passages_shown=len(shown),
                   characters=sum(len(s.text) for s in shown), **({"spellings": spelt} if spelt else {}),
                   **({"aliases": listed} if listed else {}))
        if not shown:
            row.update(status="no_mention", why="the variant is named only where the article retells earlier work"
                       if named else "no passage of the retrieved text names the variant")
            return
        sent = self.roles.client.calls

        def pointers(reading: ArticleReading) -> ArticleReading:
            """Send a first reply back once when it points where code cannot copy from; take a later one as it
            comes (module docstring)."""
            problems = pointer_problems(reading, shown) if self.roles.client.calls - sent == 1 else []
            if problems:
                raise SchemaCheckError(correction(problems))
            return reading

        out = self.roles.read(system_prompt(), packet(graph, article, shown, spelt, listed), ArticleReading,
                              pointers)
        row["sends"] = self.roles.client.calls - sent
        graph.set_model_usage(self.roles.calls_used, self.roles.cost_usd)
        if out is None:
            kind = self.roles.failures[-1]["kind"] if self.roles.failures else "failed"
            row.update(status="failed", why=kind)
            if self.roles.replay_miss and self.keep_going:
                self.roles.replay_miss = False
            elif self.roles.replay_miss:
                self.stopped = "cache_miss"
            elif self.roles.currency_exhausted:
                self.stopped = "budget_currency"
            graph.log("refuse_update", EXTRACTOR, f"the reading of {article.key} failed: {kind}",
                      target_ids=[call.tool_call_id], details={"kind": "reading", "reader": True, "failed": True,
                                                               "article": article.key, "failure": kind})
            return
        accepted = [eid for i, x in enumerate(out.experiments)
                    if (eid := self._file(graph, x, i, article, call, shown, spelt))]
        by_name = [eid for eid in dict.fromkeys(accepted)
                   if (graph.evidence[eid].data.get("variant_identity") or {}).get("basis") == "text_mined_name"]
        row.update(status="read", why="", experiments=len(out.experiments),
                   accepted=list(dict.fromkeys(accepted)), refused=len(out.experiments) - len(accepted),
                   note=" ".join(out.note.split())[:NOTE_LIMIT], **({"by_name": by_name} if by_name else {}))

    # --- the run ---------------------------------------------------------------------------------------------------------

    def run(self, graph: ClaimGraph) -> dict[str, Any]:
        """Find, then read in the order found until `max_articles` model calls are made, FETCH_FACTOR times as many
        articles have been fetched, or reading has to stop (a reply missing from the cache, the currency budget).
        Every article gets one event with what became of it, and the run one summary event; returns the summary
        (also the manifest's and the metrics')."""
        self.articles = self.find(graph)
        sent = fetched = 0
        for row in self.articles:
            if self.stopped or sent >= self.max_articles or fetched >= FETCH_FACTOR * self.max_articles:
                break                                      # the rest keep the status over_cap
            before = self.roles.calls_used
            self.read(graph, row)
            sent += self.roles.calls_used > before or row["status"] == "failed"
            fetched += bool(row.get("read"))
        if self.stopped:
            for row in self.articles:
                if row["status"] == "over_cap":
                    row["why"] = f"reading stopped: {self.stopped}"
        for row in self.articles:
            self._close(graph, row)
        return self.log_summary(graph)

    def log_summary(self, graph: ClaimGraph) -> dict[str, Any]:
        """The reading's summary, logged as the run's count of what was found, read and filed. The last one logged
        is the one a table and a report quote, so the loop logs it again after its rounds (loop.py)."""
        summary = self.summary()
        graph.log("collect_facts", "code",
                  f"the reader: {summary['found']} article(s) found by {len(self.searches)} search(es), "
                  f"{summary['read']} read, {summary['experiments']} experiment(s) returned, "
                  f"{summary['accepted']} filed as records",
                  target_ids=[c.tool_call_id for c in self.searches if c.tool_call_id],
                  details={"reader_summary": {k: v for k, v in summary.items()
                                              if k not in ("articles", "model_calls", "cost_usd")}})
        return summary

    def _close(self, graph: ClaimGraph, row: dict[str, Any]) -> None:
        """One article's row as it is kept, and its event: what became of the article."""
        row["ids"] = sorted(row["ids"])
        label = row.get("article") or row["pmcid"] or (f"PMID:{row['pmid']}" if row["pmid"] else row["doi"])
        row["label"] = label
        graph.log("collect_facts", "code",
                  f"the reader: {label}: {row['status']}" + (f" ({row['why']})" if row["why"] else "")
                  + (f"; {row.get('experiments', 0)} experiment(s) returned, {len(row.get('accepted', []))} filed"
                     if row["status"] == "read" and not row.get("duplicate") else ""),
                  target_ids=[t for t in [row.get("read")] if t], evidence_ids=row.get("accepted", []),
                  details={"reader": {k: v for k, v in row.items() if k != "note"}})

    def known(self, found: dict[str, Any]) -> dict[str, Any] | None:
        """The row of an article already listed, by any identifier it shares with a search record."""
        ids = _ids(found)
        return next((r for r in self.articles if ids & set(r["ids"])), None) if ids else None

    def read_more(self, graph: ClaimGraph, rows: Sequence[dict[str, Any]], cap: int, *,
                  reading: bool = True) -> list[dict[str, Any]]:
        """Articles a later search listed (the loop, loop.py), read exactly as the first ones were: fetched, the
        passages that name the variant chosen, one model call each, every experiment filed by the same checks. The
        packet holds nothing of why the article was looked for. `rows` are new rows in the order to read them;
        at most `cap` are sent to the model, and the rest keep the status over_cap. With `reading` False nothing
        is fetched or sent (a dry run): the rows are listed and say so. Returns the rows, closed."""
        self.roles.set_limits(self.roles.max_calls + GUARD * max(cap, 0), 0)
        sent = 0
        for row in rows:
            self.articles.append(row)
            if not reading:
                row.update(status="over_cap", why="a dry run: listed, not read")
            elif self.stopped or sent >= cap:
                row["why"] = f"reading stopped: {self.stopped}" if self.stopped else "the round's cap on articles"
            else:
                before = self.roles.calls_used
                self.read(graph, row)
                sent += self.roles.calls_used > before or row["status"] == "failed"
            self._close(graph, row)
        return list(rows)

    def summary(self) -> dict[str, Any]:
        rows = [r for r in self.articles if not r.get("duplicate")]
        counts = {key: sum(r["status"] == key for r in rows) for key, _ in STATUSES}
        return {
            "format": READER_FORMAT, "max_articles": self.max_articles, "read_chars": READ_CHARS,
            "searches": [{"call": c.tool_call_id,
                          "query": c.query_parameters.get("query") or f"{c.tool_name} (LitVar, with an assay word)",
                          "status": f"{c.execution_status}/{c.retrieval_status}",
                          "listed": sum(bool(_ids(o)) for o in c.observations)}
                         for c in self.searches],
            "found": len(rows), **counts,
            "experiments": sum(r.get("experiments", 0) for r in rows),
            "accepted": len({e for r in rows for e in r.get("accepted", [])}),
            "by_name": len({e for r in rows for e in r.get("by_name", [])}),
            "refused": sum(r.get("refused", 0) for r in rows),
            "corrected": sum(r.get("sends", 0) > 1 for r in rows),
            "model_calls": self.roles.calls_used, "cost_usd": self.roles.cost_usd,
            "failures": [{"stage": f["stage"], "kind": f["kind"]} for f in self.roles.failures],
            "stopped": self.stopped, "articles": self.articles}


def manifest_parts(roles: RoleCaller | None, max_articles: int) -> dict[str, Any]:
    """What a run with the reader records as its settings: the prompt and output schema by hash, the model the
    reader's role runs with, and the caps. Without `roles`, the settings that do not depend on a run (a replay
    compares them with a saved run's)."""
    import hashlib
    import json

    from ..agent.llm import strict_schema
    schema = json.dumps(strict_schema(ArticleReading), sort_keys=True).encode()
    return {"reader_format": READER_FORMAT, "max_articles": max_articles, "read_chars": READ_CHARS,
            "max_sentences": MAX_SENTENCES, "passage_max": L.PASSAGE_MAX,
            "queries": [*queries("<name>"), f"{LITVAR_TOOL}: <name> under any spelling AND "
                                            f"({' OR '.join(ASSAY_WORDS)})"],
            "prompt_sha256": hashlib.sha256(system_prompt().encode()).hexdigest(),
            "schema_sha256": hashlib.sha256(schema).hexdigest(),
            "model": roles.role_models().get("literature_investigator") if roles else None,
            "not_replayable": list(roles.unreplayable) if roles else []}
