"""The literature route (SPEC 4.4 as amended by 13.11; contract C3): search Europe PMC, read one paper with stable
locations, verify quoted passages, and turn an extracted experiment into Evidence.

Why it is built this way:
- A search is triage, never evidence. It lists papers (PMID, PMCID, DOI, open-access flags, a short abstract), merges
  records that share an identifier, and creates no Evidence; an empty search says nothing about the biology. Its
  observations stay within SEARCH_LIMIT characters, so the whole list reaches the investigator's packet.
- Full text comes from the route that serves it. Europe PMC's fullTextXML serves only its open-access subset and
  reports every other paper as HTTP 500 with a JSON body (Http9 classifies that "unavailable" and never retries it), so
  it is asked only when the record says isOpenAccess "Y". Otherwise NCBI efetch db=pmc returns the JATS, author
  manuscripts included, sent with tool=variant2mechanism and no key or email. A JATS document without a body is a
  publisher-restricted record: the read is abstract only, says so, and does not use the full-text budget. When a JATS
  route fails (a cache miss, the request cap, an outage), the read reports that failure instead of quietly reading the
  abstract: a run with a complete cache would have read the full text, so the evidence would differ unseen.
- Locations come from the document's structure alone (abstract/p1, body/p2, sec2.1/p3, fig1, table2, table2/cells,
  supp1), never from the focus terms, so a passage has the same location in every read of the same text.
- The raw result of a read is the parsed Article (raw/T#.json). An extracted experiment becomes Evidence only when its
  passage is found in that saved text as whole words, not governed by a negation just before it, after folding only
  typography (whitespace, quotes, dashes, ligatures, soft hyphens); superscripts, subscripts and fractions are kept, so
  a changed number never verifies. The stored passage is the exact source span.
- What an experiment is about is checked against the paper: a TF, gene, element or trait the extractor names is kept
  only when the section the passage comes from (with its heading) names it, so a GATA1 assay can never be filed as a
  TAL1 one. A binding or occupancy assay, and a TF or gene manipulation, need the factor or gene they are about. A TF
  or gene perturbation shows that the factor matters, never what an element or the variant's alleles do, so it
  carries neither; an element perturbation (a region deletion) compares no alleles, so for a claim about what the
  alleles do it is indirect at most (the graph applies both, core C3-2; the evidence says so in its limitations).
- So is the variant: papers test an LD partner next to the variant of interest, often in the same figure, and an
  assay of one variant says nothing about another's alleles. An rsID or chromosome position the extractor names is
  kept only when the paper names it for this experiment: in the quoted passage when the passage names any variant,
  else in its section, heading or caption, else anywhere in the article when the article names no other variant (an
  rsID and the position the paper writes beside it are one variant). Kept entries are stored as the graph reads them
  (rs<digits>, chr<chrom>:<pos> ref>alt). A record that compares alleles must name the one variant whose alleles it
  compared; without one it is refused, since the graph could not tell whose alleles differ.
- The allele a direction refers to comes only from the record's compared_allele, for a design that compares alleles,
  when the passage names it as an allele; a genotype ("TT") is the context's and never an allele.
- The direction must be the one the passage states for what the record is about (signed cues, negation respected, the
  reference side of a comparison read as such); a contradicting direction is refused, and a no-change record is
  refused when its clause states an effect. Evidence directions are in the frame claims use: the effect of what the
  experiment changed, so a deletion that lowered a gene is evidence that the element raises it.
- One paper can hold several experiments. The evidence class comes from the intervention; a passage in an
  Introduction, Background or Discussion section, or one that retells earlier work, is class review (context only),
  never a second observation. The independence group is the article plus the class, the endpoint category and the
  normalised system, so two wordings of one experiment share a group.
- Data flags that let a class count as direct evidence (allele_specific, allele_targeted, in_vivo) are set only when
  the paper states them: an allele conversion (never a cut, indel or deletion), an allele-resolved readout, an
  organism-level experiment (never a cell line).
- Article text is untrusted data. Markup is stripped at parse time (a "<script>" or "</data>" in a paper reaches no
  packet or report as markup), nothing in the text is ever interpreted, and the text shown to an agent is bounded.
- A public export keeps verified passages (each at most 600 characters), drops article text and bounds every other
  free-text field: author manuscripts carry no licence.
"""

import copy
import hashlib
import html
import json
import re
import unicodedata
import xml.etree.ElementTree as ET
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field, replace
from html.entities import name2codepoint
from pathlib import Path
from typing import Any, Literal
from urllib.parse import quote

from pydantic import Field, ValidationError

from ..context.http import HttpResult
from .context_match import scope_from_label, scope_key, species_of
from .graph import ClaimGraph, SymbolResolver, article_key
from .http9 import classify, is_cache_miss
from .schemas import (
    ContextScope,
    Coverage,
    Direction,
    Evidence,
    EvidenceClass,
    ExecutionStatus,
    ExperimentRecord,
    ExperimentSystem,
    Relation,
    RetrievalStatus,
    ToolCall,
    V9Model,
)
from .tools import AdapterResult, ParamSpec, ToolContext, ToolSpec, register_tool

EPMC_REST = "https://www.ebi.ac.uk/europepmc/webservices/rest"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
NCBI_TOOL = "variant2mechanism"        # NCBI asks callers to name their tool; no key and no email are ever sent
SEARCH_TOOL, READ_TOOL = "literature_search", "literature_read"

DEFAULT_RESULTS, MAX_RESULTS = 10, 10
QUERY_LIMIT = 500
RETURN_LIMIT = 14_000        # characters of observation JSON one read returns to the agent
SEARCH_LIMIT = 3_800         # ... one search returns: the engine shows a search's observations whole up to this
EXCERPT_LIMIT = 3_000        # the longest stretch of one section shown: a window around its first match
MIN_WINDOW = 400             # a remaining budget shorter than this is not worth a window
OUTLINE_LIMIT = 2_500        # characters of the section outline in a read's header
ABSTRACT_LIMIT = 1_200       # per search record (lowered alike until the records fit SEARCH_LIMIT)
TITLE_LIMIT, TITLE_FLOOR = 300, 60   # a search shortens titles to TITLE_FLOOR before it drops a record
JOURNAL_LIMIT, TYPE_LIMIT = 120, 120
HEADING_LIMIT = 200
RESULT_LIMIT = 500           # an extracted experiment's observed_result
FIELD_LIMIT = 300            # every other free-text field of an extracted experiment
NAME_LIMIT, MAX_NAMES = 200, 20      # one TF, gene, element, trait or variant name, and names per list
TOGETHER_CLEAR = 40          # an rsID and a position written side by side are one variant when no other is this near
PASSAGE_MIN, PASSAGE_MAX = 20, 600   # a verified passage: long enough to mean something, short enough to export
PUBLIC_PASSAGE_LIMIT = PASSAGE_MAX
MAX_DOCUMENT_CHARS = 20_000_000
MAX_FOCUS_TERMS, FOCUS_TERM_LIMIT = 20, 80   # keeps a read's header small whatever focus an agent sends
EVIDENCE_FROM = ("records_found", "incomplete")
# When no route returned text, the read's status is its most consequential failure: a cache miss first (replaying
# the run would need the network), then an error, then a stated unavailability.
FAILURE_RANK = {"cache_miss": 3, "error": 2, "unavailable": 1}
_EMAIL = re.compile(r"[^\s@]+@[^\s@]+\.[^\s@]+")

Route = Literal["europepmc_fulltext", "ncbi_efetch", "abstract"]
Access = Literal["full_text", "abstract_only"]


class ExtractionRefused(Exception):
    """An extracted experiment that cannot become Evidence. `reason` is written for the extractor; the engine logs
    it as a refuse_update event."""

    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


class ArticleSection(V9Model):
    location: str                # stable id: abstract/p1, body/p2, sec2.1/p3, fig1, table2, table2/cells, supp1
    heading: str = ""
    text: str
    reference_ids: list[str] = Field(default_factory=list)


class ArticleReference(V9Model):
    """Discovery metadata, never an extractable experiment from the citing article."""
    reference_id: str
    label: str = ""
    title: str = ""
    citation: str = ""
    pmid: str | None = None
    pmcid: str | None = None
    doi: str | None = None


class Article(V9Model):
    """A parsed paper: the raw result of literature_read (raw/T#.json) and what passages are verified against."""
    pmid: str | None = None
    pmcid: str | None = None
    doi: str | None = None
    title: str = ""
    journal: str = ""
    year: int | None = None
    publication_type: str = ""
    route: Route
    access: Access
    sections: list[ArticleSection] = Field(default_factory=list)
    references: list[ArticleReference] = Field(default_factory=list)
    source_sha256: str | None = None     # sha256 of the document the text was parsed from (provenance)

    @property
    def key(self) -> str:
        """One id for the article: its PMCID, else PMID:<n>, else DOI:<doi> (the full-text budget counts these)."""
        return self.pmcid or (f"PMID:{self.pmid}" if self.pmid else f"DOI:{self.doi}")

    @property
    def is_review(self) -> bool:
        return bool(_REVIEW.search(self.publication_type))

    def source_ids(self) -> list[str]:
        """Every id of the article, prefixed: one paper is one source whichever id a record cites."""
        return [x for x in (f"PMID:{self.pmid}" if self.pmid else "", f"PMCID:{self.pmcid}" if self.pmcid else "",
                            f"DOI:{self.doi}" if self.doi else "") if x]

    def section(self, location: str) -> ArticleSection | None:
        return next((s for s in self.sections if s.location == location), None)


# --- text: untrusted, plain, comparable ---------------------------------------------------------------------------

_SCRIPT = re.compile(r"<(script|style)\b[^>]*>.*?</\1\s*>", re.I | re.S)
_COMMENT = re.compile(r"<!--.*?-->|<!\[CDATA\[|\]\]>|<![A-Za-z][^<>]*>", re.S)
_TAG = re.compile(r"</?([A-Za-z][A-Za-z0-9:._-]*)(?:\s[^<>]*)?/?>")
_ANY_TAG = re.compile(r"<[^<>]*>")
_INLINE_TAGS = frozenset({"a", "b", "big", "bold", "code", "em", "i", "italic", "inline-formula", "named-content",
                          "sc", "small", "span", "strong", "styled-content", "sub", "sup", "tt", "u", "underline"})
# Soft hyphens, zero-width and bidirectional controls, and the Unicode tag characters and variation selectors that
# can carry text a reader never sees.
_INVISIBLE = re.compile("[\u00ad\u034f\u061c\u115f\u1160\u17b4\u17b5\u180e\u200b-\u200f\u202a-\u202e"
                        "\u2060-\u2064\u2066-\u206f\ufe00-\ufe0f\ufeff\U000e0000-\U000e007f\U000e0100-\U000e01ef]")
_CONTROL = re.compile(r"[\x00-\x1f\x7f-\x9f]")
# Typography a quotation may change without changing what it says. Only these are folded: superscripts, subscripts,
# fractions and other compatibility characters stay as they are, so "10" with a superscript 3 never matches "103".
_FOLD: dict[int, str] = (
    {ord(c): "'" for c in "\u2018\u2019\u201a\u201b\u2032\u2035`\u00b4"}
    | {ord(c): '"' for c in "\u201c\u201d\u201e\u201f\u2033\u2036\u00ab\u00bb"}
    | {ord(c): "-" for c in "\u2010\u2011\u2012\u2013\u2014\u2015\u2043\u2212\ufe58\ufe63\uff0d"}
    | {ord(c): " " for c in "\u00a0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u202f"
                              "\u205f\u3000"}
    | {0xFB00: "ff", 0xFB01: "fi", 0xFB02: "fl", 0xFB03: "ffi", 0xFB04: "ffl", 0xFB05: "st", 0xFB06: "st",
       0x00B5: "\u03bc"})
_QUOTE_CHARS = "\"'"


def _ends_word(text: str) -> bool:
    """Whether text ends with a character an exponent or a citation number can follow (10^3, GATA1^12, (2019)^5)."""
    return bool(text) and (text[-1].isalnum() or text[-1] in ")]")


def _tag(m: re.Match[str]) -> str:
    """A tag in untrusted HTML: inline tags vanish, block tags become a space, and a superscript after a word or
    number is marked with ^ so that 10<sup>3</sup> reads 10^3 (not 103) and GATA1<sup>12</sup> reads GATA1^12."""
    name = m.group(1).lower()
    if name == "sup" and not m.group(0).startswith("</"):
        before = _ANY_TAG.sub("", m.string[max(0, m.start() - 80):m.start()])
        return "^" if _ends_word(before) else ""
    return "" if name in _INLINE_TAGS else " "


def clean_text(value: Any) -> str:
    """Untrusted text as plain text: entities decoded; scripts, comments and tags removed (inline tags without a
    space, block tags as one, a superscript after a word or number as ^); invisible, bidirectional and control
    characters dropped; canonical composition (NFC); whitespace collapsed."""
    text = unicodedata.normalize("NFC", html.unescape(str(value or "")))
    text = _COMMENT.sub(" ", _SCRIPT.sub(" ", text))
    text = _TAG.sub(_tag, text)
    text = _CONTROL.sub(" ", _INVISIBLE.sub("", text))
    return " ".join(text.split())


def _norm_map(text: str) -> tuple[str, list[int], list[int]]:
    """Text in matching form, with where each of its characters came from: starts[i]:ends[i] is the source stretch
    behind character i, so a match in matching form maps back to the exact source text."""
    chars: list[str] = []
    starts: list[int] = []
    ends: list[int] = []
    space = True                                  # collapses leading and repeated whitespace
    for i, ch in enumerate(text):
        if _INVISIBLE.match(ch):
            continue
        folded = _FOLD.get(ord(ch), ch)
        if folded == " " or ch.isspace():
            if not space:
                chars.append(" ")
                starts.append(i)
                ends.append(i + 1)
                space = True
            continue
        for c in folded:
            chars.append(c)
            starts.append(i)
            ends.append(i + 1)
        space = False
    if chars and chars[-1] == " ":
        chars.pop()
        starts.pop()
        ends.pop()
    return "".join(chars), starts, ends


def normalise_for_match(text: str) -> str:
    """The form passages are compared in: canonical composition (NFC); curly quotes, primes and dashes made plain;
    typographic spaces made plain; ligatures spelled out and the micro sign read as mu; soft hyphens and zero-width
    characters removed; whitespace collapsed. Case, wording, superscripts, subscripts and fractions are kept: a
    passage that changes a word or a number is not the source's."""
    return _norm_map(unicodedata.normalize("NFC", str(text or "")))[0]


def _bounded(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "\u2026" if limit > 1 else ""


def _field(value: Any, limit: int = FIELD_LIMIT) -> str:
    """An extractor's free-text field as stored: plain text, bounded (it is the extractor's summary, never the
    paper's text, so it never needs to be long)."""
    return _bounded(clean_text(value), limit)


# --- identifiers ----------------------------------------------------------------------------------------------------

_DOI_PREFIXES = ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/", "doi:")


def _parse_id(value: Any) -> tuple[str, str] | None:
    """('pmid', '123'), ('pmcid', 'PMC123') or ('doi', '10.x/y' in lower case) from any common spelling ("PMID:123",
    "123", "PMCID:PMC123", "pmc123", "doi:10.x/y", a doi.org URL); None for anything else."""
    text = " ".join(str(value or "").split())
    low = text.casefold()
    for prefix in _DOI_PREFIXES:
        if low.startswith(prefix):
            low = low[len(prefix):].strip()
            return ("doi", low) if low.startswith("10.") and "/" in low else None
    if low.startswith("pmid:"):
        low = low[5:].strip()
        return ("pmid", low) if low.isdigit() else None
    if low.startswith("pmcid:"):
        low = low[6:].strip()
    if re.fullmatch(r"pmc\d+", low):
        return ("pmcid", "PMC" + low[3:])
    if low.isdigit():
        return ("pmid", low)
    if low.startswith("10.") and "/" in low:
        return ("doi", low)
    return None


def _id_of(kind: str, value: Any) -> str | None:
    parsed = _parse_id(value)
    return parsed[1] if parsed and parsed[0] == kind else None


def _keys(pmid: str | None, pmcid: str | None, doi: str | None) -> set[tuple[str, str]]:
    return {k for k in (("pmid", pmid), ("pmcid", pmcid), ("doi", doi)) if k[1]}


def _article_keys(article: Article) -> set[tuple[str, str]]:
    return _keys(article.pmid, article.pmcid, article.doi)


def _label(pmid: str | None, pmcid: str | None) -> str:
    return " / ".join(x for x in (pmcid, f"PMID {pmid}" if pmid else "") if x) or "the article"


# --- HTTP -------------------------------------------------------------------------------------------------------------

def search_url(query: str, page_size: int) -> str:
    """Europe PMC REST search, resultType=core (abstracts and open-access flags), relevance order."""
    return f"{EPMC_REST}/search?query={quote(query)}&format=json&pageSize={page_size}&resultType=core"


def metadata_url(pmcid: str | None, pmid: str | None) -> str:
    """The Europe PMC record of one article, by PMCID when known (else by PMID)."""
    return search_url(f"PMCID:{pmcid}" if pmcid else f"EXT_ID:{pmid} AND SRC:MED", 5)


def fulltext_url(pmcid: str) -> str:
    return f"{EPMC_REST}/{pmcid}/fullTextXML"


def efetch_url(pmcid: str) -> str:
    return f"{EFETCH}?db=pmc&id={pmcid[3:]}&retmode=xml&tool={NCBI_TOOL}"


def _outcome(result: HttpResult) -> tuple[str, str]:
    """A failed response as Http9 classifies it (contract C1), with a cache miss kept apart: "no_records" (HTTP 404),
    "cache_miss" (offline and not saved: replaying it would need the network), "unavailable" (a stated refusal such as
    Europe PMC's 500 with a JSON body, the request cap, or an outage that outlasted the retries) or "error"."""
    if is_cache_miss(result):
        return "cache_miss", f"not in the HTTP cache: {result.url} (cache-only mode never reaches the network)"
    return classify(result), " ".join(str(result.error or f"HTTP {result.status}").split())


@dataclass
class _Fetch:
    """One request of a read and how it ended: ok, no_records, or a failure status."""
    route: str
    url: str
    outcome: str
    note: str = ""
    cached: bool = False
    retrieved: str = ""

    def describe(self) -> str:
        detail = f": {self.note}" if self.note else ""
        return _bounded(f"{self.route} {self.outcome}{' (cached)' if self.cached else ''}{detail}", 160)

    @property
    def status(self) -> ExecutionStatus:
        """The execution status a failed request gives the whole read."""
        return self.failure(self.outcome)

    @staticmethod
    def failure(outcome: str) -> ExecutionStatus:
        return "cache_miss" if outcome == "cache_miss" else "unavailable" if outcome == "unavailable" else "error"


@dataclass
class _Paper:
    """One Europe PMC record, as kept: identifiers, bibliographic fields, access flags and the abstract."""
    pmid: str | None
    pmcid: str | None
    doi: str | None
    title: str
    journal: str
    year: int | None
    publication_type: str
    is_open_access: bool
    in_pmc: bool
    nih_author_manuscript: bool
    abstract_html: str
    digest: str
    source: str = ""

    @property
    def keys(self) -> set[tuple[str, str]]:
        return _keys(self.pmid, self.pmcid, self.doi)

    @property
    def read_route(self) -> str:
        """What a literature_read of this paper would try first."""
        if self.pmcid:
            return "europepmc_fulltext" if self.is_open_access else "ncbi_efetch"
        return "abstract" if self.pmid else "none"

    def merge(self, other: "_Paper") -> None:
        """Fill identifiers and fields this record lacks from another record of the same article."""
        for name in ("pmid", "pmcid", "doi", "title", "journal", "year", "publication_type", "abstract_html"):
            if not getattr(self, name) and getattr(other, name):
                setattr(self, name, getattr(other, name))
        self.is_open_access |= other.is_open_access
        self.in_pmc |= other.in_pmc
        self.nih_author_manuscript |= other.nih_author_manuscript


def _publication_types(types: list[str]) -> str:
    """The publication types worth showing, each once: funding notes ("Research Support, ...") say nothing about
    whether a paper is primary research or a review."""
    kept = [t for t in (clean_text(x) for x in types) if t and not t.casefold().startswith("research support")]
    return _bounded("; ".join(dict.fromkeys(kept)), TYPE_LIMIT)


def _paper(row: Any) -> _Paper | None:
    """A Europe PMC result row as a _Paper; None when it has no PMID, PMCID or DOI (nothing could read it)."""
    if not isinstance(row, dict):
        return None
    pmid, pmcid, doi = _id_of("pmid", row.get("pmid")), _id_of("pmcid", row.get("pmcid")), _id_of("doi", row.get("doi"))
    if not (pmid or pmcid or doi):
        return None
    journal = ((row.get("journalInfo") or {}).get("journal") or {}).get("title") or row.get("journalTitle") or ""
    types = (row.get("pubTypeList") or {}).get("pubType") or []
    types = [types] if isinstance(types, str) else [t for t in types if isinstance(t, str)]
    year = str(row.get("pubYear") or "")
    return _Paper(pmid=pmid, pmcid=pmcid, doi=doi, title=_bounded(clean_text(row.get("title")), TITLE_LIMIT),
                  journal=_bounded(clean_text(journal), JOURNAL_LIMIT), year=int(year) if year.isdigit() else None,
                  publication_type=_publication_types(types),
                  is_open_access=row.get("isOpenAccess") == "Y", in_pmc=row.get("inPMC") == "Y",
                  nih_author_manuscript=row.get("nihAuthMan") == "Y", abstract_html=str(row.get("abstractText") or ""),
                  digest=hashlib.sha256(json.dumps(row, sort_keys=True).encode()).hexdigest(),
                  source=str(row.get("source") or ""))


def _papers(rows: list[Any]) -> tuple[list[_Paper], int]:
    """Usable records in relevance order, one per article (records sharing a PMID, PMCID or DOI merged), and the
    number of rows dropped for having no identifier."""
    papers: list[_Paper] = []
    index: dict[tuple[str, str], int] = {}
    dropped = 0
    for row in rows:
        paper = _paper(row)
        if paper is None:
            dropped += 1
            continue
        hit = next((index[k] for k in sorted(paper.keys) if k in index), None)
        if hit is None:
            hit = len(papers)
            papers.append(paper)
        else:
            papers[hit].merge(paper)
        for k in papers[hit].keys:
            index[k] = hit
    return papers, dropped


def _abstract_parts(abstract_html: str) -> list[tuple[str, str]]:
    """(heading, text) paragraphs of a Europe PMC abstract, split at its <h4> subheadings."""
    pieces = re.split(r"<h4[^>]*>(.*?)</h4>", abstract_html or "", flags=re.I | re.S)
    parts = [("Abstract", clean_text(pieces[0]))]
    parts += [(f"Abstract \u203a {clean_text(h)}" if clean_text(h) else "Abstract", clean_text(t))
              for h, t in zip(pieces[1::2], pieces[2::2], strict=True)]
    return [(h, t) for h, t in parts if t]


# --- JATS -----------------------------------------------------------------------------------------------------------

BLOCKS = frozenset({"p", "list", "disp-quote", "boxed-text", "statement", "def-list", "preformat", "verse-group",
                    "speech"})                         # paragraph-like children of a section
FLOATS = frozenset({"fig", "table-wrap", "supplementary-material"})
SKIP_TEXT = frozenset({"fig", "fig-group", "table-wrap", "table-wrap-group", "supplementary-material", "tex-math",
                       "annotation", "annotation-xml", "graphic", "inline-graphic", "media", "object-id", "script",
                       "style"})                      # floats are read separately; code and graphics are not text
SPACED = frozenset({"p", "title", "label", "caption", "list-item", "td", "th", "tr", "break", "disp-formula",
                    "disp-quote", "def", "term", "list", "sec", "table-wrap-foot", "fn"})
NOT_FLOATS = frozenset({"ref-list", "sub-article", "response", "fn-group", "ack", "front", "front-stub"})
BACK_SKIP_TYPES = frozenset({"supplementary-material", "display-objects", "data-availability", "coi-statement",
                             "funding-information", "author-contributions", "ethics-statement", "acknowledgments",
                             "acknowledgements", "abbreviations", "author-notes", "conflict"})
_BACK_SKIP_TITLE = re.compile(r"acknowledg|funding|conflict|competing interest|author contribution|data availability|"
                              r"abbreviation|disclosure|financial support|supplementary|online content", re.I)


def _local(tag: Any) -> str:
    return tag.rsplit("}", 1)[-1] if isinstance(tag, str) else ""


def _children(el: ET.Element | None, *names: str) -> list[ET.Element]:
    return [] if el is None else [c for c in el if _local(c.tag) in names]


def _child(el: ET.Element | None, *names: str) -> ET.Element | None:
    found = _children(el, *names)
    return found[0] if found else None


def _gathered_end(parts: list[str]) -> str:
    return next((p for p in reversed(parts) if p), "")


def _gather(el: ET.Element, parts: list[str]) -> None:
    tag = _local(el.tag)
    spaced = tag in SPACED
    if spaced:
        parts.append(" ")
    elif tag == "sup" and _ends_word(_gathered_end(parts)):
        parts.append("^")                      # an exponent or citation number: 10^3, not 103; GATA1^12, not GATA112
    if el.text:
        parts.append(el.text)
    for child in el:
        if _local(child.tag) not in SKIP_TEXT:
            _gather(child, parts)
        if child.tail:
            parts.append(child.tail)
    if spaced:
        parts.append(" ")


def _text(el: ET.Element | None) -> str:
    """The plain text of an element, without nested figures, tables, supplements, TeX or graphics."""
    if el is None:
        return ""
    parts: list[str] = []
    _gather(el, parts)
    return clean_text("".join(parts))


def _heading_of(sec: ET.Element) -> str:
    return " ".join(x for x in (_text(_child(sec, "label")), _text(_child(sec, "title"))) if x)


def _reference_ids(el: ET.Element) -> list[str]:
    return list(dict.fromkeys(rid for x in el.iter() if _local(x.tag) == "xref" and
                             x.get("ref-type") == "bibr" for rid in x.get("rid", "").split()))


def _references(article: ET.Element) -> list[ArticleReference]:
    def entries(el: ET.Element):
        for child in el:
            tag = _local(child.tag)
            if tag in ("sub-article", "response"):
                continue
            if tag == "ref":
                yield child
            else:
                yield from entries(child)

    refs = []
    # PMC also supplies ref-lists inside body sections, not only in back matter.
    for el in entries(article):
        if not el.get("id"):
            continue
        ids = {}
        title = ""
        for node in el.iter():
            if _local(node.tag) == "article-title":
                title = _text(node)
            if _local(node.tag) == "pub-id":
                kind = {"pmc": "pmcid", "pubmed": "pmid"}.get(node.get("pub-id-type"),
                                                              node.get("pub-id-type"))
                if kind in ("pmid", "pmcid", "doi") and (value := _id_of(kind, _text(node))):
                    ids[kind] = value
            if _local(node.tag) == "ext-link":
                kind = node.get("ext-link-type")
                value = node.get("{http://www.w3.org/1999/xlink}href", "")
                if kind in ("pmid", "pmcid", "doi") and (value := _id_of(kind, value)):
                    ids[kind] = value
        refs.append(ArticleReference(reference_id=el.get("id"), label=_text(_child(el, "label")).rstrip("."),
                                     title=_bounded(title, TITLE_LIMIT), citation=_bounded(_text(el), 600), **ids))
    return refs


def _walk_section(sec: ET.Element, location: str, parent: str, out: list[ArticleSection]) -> None:
    """Paragraph-like children as <location>/p<n> (numbered within the section), subsections as <location>.<m>."""
    title = _heading_of(sec) or f"untitled section {location}"
    heading = _bounded(f"{parent} \u203a {title}" if parent else title, HEADING_LIMIT)
    paragraphs = subsections = 0
    for child in sec:
        tag = _local(child.tag)
        if tag in BLOCKS and (text := _text(child)):
            paragraphs += 1
            out.append(ArticleSection(location=f"{location}/p{paragraphs}", heading=heading, text=text,
                                      reference_ids=_reference_ids(child)))
        elif tag == "sec":
            subsections += 1
            _walk_section(child, f"{location}.{subsections}", heading, out)


def _abstract_sections(meta: ET.Element | None) -> list[ArticleSection]:
    """Every abstract of the article (not translations or graphical abstracts), paragraphs numbered across them."""
    out: list[ArticleSection] = []

    def walk(el: ET.Element, heading: str) -> None:
        for child in el:
            tag = _local(child.tag)
            if tag in BLOCKS and (text := _text(child)):
                out.append(ArticleSection(location=f"abstract/p{len(out) + 1}", heading=heading, text=text,
                                          reference_ids=_reference_ids(child)))
            elif tag == "sec":
                sub = _heading_of(child)
                walk(child, _bounded(f"{heading} \u203a {sub}" if sub else heading, HEADING_LIMIT))

    for abstract in _children(meta, "abstract"):
        if abstract.get("abstract-type") in ("graphical", "toc"):
            continue
        walk(abstract, _bounded(_text(_child(abstract, "title")) or "Abstract", HEADING_LIMIT))
    return out


def _wanted_back(sec: ET.Element) -> bool:
    kind = (sec.get("sec-type") or "").casefold()
    return kind not in BACK_SKIP_TYPES and not _BACK_SKIP_TITLE.search(_text(_child(sec, "title")))


def _main_sections(article: ET.Element) -> tuple[list[ArticleSection], list[ArticleSection]]:
    """The body: paragraphs before any section (body/p<n>), then its sections; and the back matter's content
    sections (online methods), numbered on from the body's (sec1, sec2, ... in document order)."""
    body: list[ArticleSection] = []
    back: list[ArticleSection] = []
    top_paragraphs = sections = 0
    body_el = _child(article, "body")
    for child in list(body_el) if body_el is not None else []:
        tag = _local(child.tag)
        if tag in BLOCKS and (text := _text(child)):
            top_paragraphs += 1
            body.append(ArticleSection(location=f"body/p{top_paragraphs}", heading="Main text", text=text,
                                       reference_ids=_reference_ids(child)))
        elif tag == "sec":
            sections += 1
            _walk_section(child, f"sec{sections}", "", body)
    for sec in _children(_child(article, "back"), "sec"):
        if _wanted_back(sec):
            sections += 1
            _walk_section(sec, f"sec{sections}", "", back)
    return body, back


def _iter_floats(el: ET.Element) -> Iterator[ET.Element]:
    for child in el:
        tag = _local(child.tag)
        if tag in NOT_FLOATS:
            continue
        if tag in FLOATS:
            yield child
        else:
            yield from _iter_floats(child)


def _float_sections(article: ET.Element) -> list[ArticleSection]:
    """Figure, table and supplement captions in document order (fig<n>, table<n>, supp<n>), wherever the JATS puts
    them (inside sections, in back matter or in a floats group); a table's cells as table<n>/cells."""
    out: list[ArticleSection] = []
    counts = {"fig": 0, "table-wrap": 0, "supplementary-material": 0}
    names = {"fig": ("fig", "Figure"), "table-wrap": ("table", "Table"), "supplementary-material": ("supp", "Supplement")}
    for part in _children(article, "body", "back", "floats-group"):
        for el in _iter_floats(part):
            kind = _local(el.tag)
            prefix, default = names[kind]
            counts[kind] += 1
            location = f"{prefix}{counts[kind]}"
            heading = _bounded(_text(_child(el, "label")) or f"{default} {counts[kind]}", HEADING_LIMIT)
            caption = " ".join(x for x in (_text(_child(el, "caption")),
                                           *(_text(f) for f in _children(el, "table-wrap-foot"))) if x)
            if caption:
                out.append(ArticleSection(location=location, heading=heading, text=caption,
                                          reference_ids=_reference_ids(el)))
            if kind != "table-wrap":
                continue
            rows = [" | ".join(_text(c) for c in tr if _local(c.tag) in ("td", "th"))
                    for tr in el.iter() if _local(tr.tag) == "tr"]
            if rows := [r for r in rows if r.strip(" |")]:
                out.append(ArticleSection(location=f"{location}/cells", heading=f"{heading} (cells)",
                                          text="\n".join(rows)))
    return out


def _jats_ids(meta: ET.Element | None) -> dict[str, str | None]:
    ids: dict[str, str | None] = {"pmid": None, "pmcid": None, "doi": None}
    for el in _children(meta, "article-id"):
        kind, value = (el.get("pub-id-type") or "").casefold(), _text(el)
        if kind == "pmid":
            ids["pmid"] = ids["pmid"] or _id_of("pmid", value)
        elif kind in ("pmcid", "pmc"):
            ids["pmcid"] = ids["pmcid"] or _id_of("pmcid", value if value.upper().startswith("PMC") else f"PMC{value}")
        elif kind == "doi":
            ids["doi"] = ids["doi"] or _id_of("doi", value)
    return ids


def _jats_year(meta: ET.Element | None) -> int | None:
    years = [_text(_child(d, "year")) for d in _children(meta, "pub-date")]
    return next((int(y) for y in years if y.isdigit()), None)


def _parser() -> ET.XMLParser:
    """An expat parser that knows the HTML named entities (JATS may use them without a readable DTD). Expat never
    fetches external entities and bounds entity expansion."""
    parser = ET.XMLParser()
    parser.entity.update({name: chr(code) for name, code in name2codepoint.items()})
    return parser


def parse_jats(text: str, route: Route) -> Article | None:
    """Parse a JATS document (an <article>, or a <pmc-articleset> holding one) from `route`. A document with a body
    is full text; one without (a publisher-restricted PMC record) is the abstract only, route "abstract". None when
    the document holds no article. Raises ValueError for text that is not readable XML."""
    if len(text) > MAX_DOCUMENT_CHARS:
        raise ValueError(f"the document is larger than {MAX_DOCUMENT_CHARS} characters")
    try:
        root = ET.fromstring(text.lstrip("\ufeff"), parser=_parser())
        article = root if _local(root.tag) == "article" else next(
            (el for el in root.iter() if _local(el.tag) == "article"), None)
        if article is None:
            return None
        front = _child(article, "front")
        meta = _child(front, "article-meta")
        journal_meta = _child(front, "journal-meta")
        body, back = _main_sections(article)
        full = bool(body)                       # back matter alone (notes, methods stubs) is not a full text
        sections = _abstract_sections(meta) + (body + back + _float_sections(article) if full else [])
        title = _text(_child(_child(meta, "title-group"), "article-title"))
        journal = _text(_child(_child(journal_meta, "journal-title-group"), "journal-title")) or _text(
            _child(journal_meta, "journal-title"))
    except ET.ParseError as e:
        raise ValueError(f"the response is not readable XML ({e})") from e
    except RecursionError as e:
        raise ValueError("the document is nested too deeply to read") from e
    return Article(**_jats_ids(meta), title=_bounded(title, TITLE_LIMIT), journal=journal, year=_jats_year(meta),
                   publication_type=clean_text(article.get("article-type") or ""),
                   route=route if full else "abstract", access="full_text" if full else "abstract_only",
                   sections=sections, references=_references(article) if full else [],
                   source_sha256=hashlib.sha256(text.encode()).hexdigest())


# --- reading one article ----------------------------------------------------------------------------------------------

@dataclass
class _Read:
    """The outcome of a read: the article (or None), the Europe PMC record, every request made on the way, and why
    only the abstract was read when that is all there is."""
    article: Article | None = None
    fetches: list[_Fetch] = field(default_factory=list)
    paper: _Paper | None = None
    version: str = ""                    # the Europe PMC service version that answered the metadata request
    conflict: str = ""
    why_abstract: str = ""


def _metadata(http: Any, pmcid: str | None, pmid: str | None, read: _Read) -> None:
    url = metadata_url(pmcid, pmid)
    r = http.get(url)
    if not r.ok:
        read.fetches.append(_Fetch("metadata", url, *_outcome(r)))
        return
    result_list = r.data.get("resultList") if isinstance(r.data, dict) else None
    rows = result_list.get("result") if isinstance(result_list, dict) else None
    if not isinstance(rows, list):
        read.fetches.append(_Fetch("metadata", url, "error", "Europe PMC returned an unexpected payload"))
        return
    papers, _ = _papers(rows)
    want = ("pmcid", pmcid) if pmcid else ("pmid", pmid)
    read.paper = next((p for p in papers if want in p.keys), None)
    read.version = str(r.data.get("version") or "")
    read.fetches.append(_Fetch("metadata", url, "ok" if read.paper else "no_records", cached=r.cached,
                               retrieved=r.retrieved_utc))


def _fetch_jats(http: Any, route: Route, pmcid: str, read: _Read) -> Article | None:
    url = fulltext_url(pmcid) if route == "europepmc_fulltext" else efetch_url(pmcid)
    r = http.get(url)
    if not r.ok:
        read.fetches.append(_Fetch(route, url, *_outcome(r)))
        return None
    if not isinstance(r.data, str):
        read.fetches.append(_Fetch(route, url, "no_records", "the response is not JATS XML", r.cached, r.retrieved_utc))
        return None
    try:
        article = parse_jats(r.data, route)
    except ValueError as e:
        read.fetches.append(_Fetch(route, url, "error", str(e), r.cached, r.retrieved_utc))
        return None
    if article is None:
        read.fetches.append(_Fetch(route, url, "no_records", "no article in the response", r.cached, r.retrieved_utc))
        return None
    if article.pmcid and article.pmcid != pmcid:
        read.fetches.append(_Fetch(route, url, "error", f"the response is {article.pmcid}, not {pmcid}", r.cached,
                                   r.retrieved_utc))
        return None
    read.fetches.append(_Fetch(route, url, "ok", "full text" if article.access == "full_text" else "no body",
                               r.cached, r.retrieved_utc))
    return article


def _with_paper(article: Article, paper: _Paper | None) -> Article:
    """Fill what the JATS lacks from the Europe PMC record; the record's bibliographic fields win."""
    if paper is None:
        return article
    sections = article.sections
    if not any(s.location.startswith("abstract/") for s in sections):
        abstract = [ArticleSection(location=f"abstract/p{i}", heading=h, text=t)
                    for i, (h, t) in enumerate(_abstract_parts(paper.abstract_html), 1)]
        sections = abstract + sections
    types: dict[str, str] = {}
    for listed in (paper.publication_type, article.publication_type):
        for t in filter(None, (x.strip() for x in listed.split(";"))):
            types.setdefault(t.casefold(), t)            # each type once, first spelling kept
    return article.model_copy(update={
        "pmid": article.pmid or paper.pmid, "pmcid": article.pmcid or paper.pmcid, "doi": article.doi or paper.doi,
        "title": paper.title or article.title, "journal": paper.journal or article.journal,
        "year": paper.year or article.year, "publication_type": "; ".join(types.values()), "sections": sections})


def _from_paper(paper: _Paper) -> Article:
    """The abstract-only article a Europe PMC record gives when PMC has no JATS for the paper."""
    sections = [ArticleSection(location=f"abstract/p{i}", heading=h, text=t)
                for i, (h, t) in enumerate(_abstract_parts(paper.abstract_html), 1)]
    return Article(pmid=paper.pmid, pmcid=paper.pmcid, doi=paper.doi, title=paper.title, journal=paper.journal,
                   year=paper.year, publication_type=paper.publication_type, route="abstract",
                   access="abstract_only", sections=sections, source_sha256=paper.digest)


def _read_article(http: Any, pmcid: str | None, pmid: str | None) -> _Read:
    """Metadata from Europe PMC, then full text from the route that serves it: fullTextXML for open-access papers,
    else (or when that fails) NCBI efetch. Only the abstract is read when PMC holds the paper without a body
    (publisher-restricted), when PMC has no record of it, or when it has no PMCID. A JATS route that failed (a cache
    miss, an outage, the request cap) leaves no article: the read reports the failure, because the abstract would
    silently stand in for a full text that a complete cache or a working network returns."""
    read = _Read()
    _metadata(http, pmcid, pmid, read)
    paper = read.paper
    if paper is not None and pmid and paper.pmid and paper.pmid != pmid:
        read.conflict = f"{pmcid} is PMID {paper.pmid}, not PMID {pmid}"
        return read
    pmcid = pmcid or (paper.pmcid if paper else None)
    if pmcid:
        front: Article | None = None
        routes: list[Route] = (["europepmc_fulltext"] if paper is not None and paper.is_open_access else [])
        for route in [*routes, "ncbi_efetch"]:
            article = _fetch_jats(http, route, pmcid, read)
            if article is not None and article.access == "full_text":
                read.article = _with_paper(article, paper)
                return _checked(read, pmcid, pmid)
            front = front or article
        if front is not None:
            read.article, read.why_abstract = (_with_paper(front, paper),
                                               "PMC holds no body for it (publisher-restricted)")
        elif any(f.route != "metadata" and f.outcome in FAILURE_RANK for f in read.fetches):
            return read
        elif paper is not None:
            read.article, read.why_abstract = _from_paper(paper), f"PMC returned no article for {pmcid}"
    elif paper is not None:
        read.article, read.why_abstract = _from_paper(paper), "no PMCID"
    return _checked(read, pmcid, pmid)


def _checked(read: _Read, pmcid: str | None, pmid: str | None) -> _Read:
    """Refuse an article whose PMID is not the one asked for (the two ids named two articles)."""
    if read.article is not None and pmid and read.article.pmid and read.article.pmid != pmid:
        read.conflict = f"{pmcid or read.article.key} is PMID {read.article.pmid}, not PMID {pmid}"
        read.article = None
    return read


# --- what a read shows the agent ----------------------------------------------------------------------------------

LOCATION_TERM = re.compile(r"(abstract|body|sec\d+(?:\.\d+)*|fig\d+|table\d+|supp\d+)(?:/p\d+|/cells)?")


def _size(obj: Any) -> int:
    return len(json.dumps(obj, ensure_ascii=False, separators=(",", ":")))


def _term_pattern(term: str) -> re.Pattern[str]:
    """A focus term matched case-insensitively as whole words (a plural s/es allowed): "SORT1" never matches
    "SORT10"."""
    t = normalise_for_match(term).casefold()
    left = r"(?<![0-9a-z])" if t[:1].isalnum() else ""
    right = r"(?:e?s)?(?![0-9a-z])" if t[-1:].isalnum() else ""
    return re.compile(left + re.escape(t) + right)


def _window(text: str, patterns: list[re.Pattern[str]], size: int) -> tuple[str, bool]:
    """The section's text, or a window of `size` characters around its first focus match when it is longer."""
    if len(text) <= size:
        return text, False
    low = text.lower()
    hits = [m.start() for p in patterns if (m := p.search(low))]
    start = max(0, min(hits, default=0) - size // 4)
    if start:
        start = text.rfind(" ", 0, start) + 1
    end = start + size
    if end < len(text):
        end = max(text.rfind(" ", start, end), start + size // 2)
    return ("\u2026 " if start else "") + text[start:end].strip() + (" \u2026" if end < len(text) else ""), True


def _outline(sections: list[ArticleSection]) -> tuple[list[dict[str, Any]], bool]:
    """One entry per section, figure or table (location, heading, passage count), bounded."""
    entries: dict[str, dict[str, Any]] = {}
    for s in sections:
        container = s.location.split("/")[0]
        if container in entries:
            entries[container]["passages"] += 1
        else:
            entries[container] = {"location": container, "heading": _bounded(s.heading, 120), "passages": 1}
    shown, used = [], 0
    for entry in entries.values():
        used += _size(entry) + 1
        if used > OUTLINE_LIMIT:
            return shown, True
        shown.append(entry)
    return shown, False


def _candidates(article: Article, focus: list[str]) -> tuple[list[tuple[int, list[str]]], list[str]]:
    """Sections to show, best first, with the focus terms each matched; and the terms that matched nothing.
    Location terms (sec3, fig2, sec2.1/p4) come first, then sections by the number of distinct terms they match
    (document order breaks ties). With no focus, or none matching, the abstract and the captions lead."""
    sections = article.sections
    locations = [t for t in focus if LOCATION_TERM.fullmatch(t)]
    words = [t for t in focus if t not in locations]
    picked: list[tuple[int, list[str]]] = []
    seen: set[int] = set()
    hit_terms: set[str] = set()
    for term in locations:
        for i, s in enumerate(sections):
            if i not in seen and (s.location == term or s.location.startswith((term + "/", term + "."))):
                picked.append((i, [term]))
                seen.add(i)
                hit_terms.add(term)
    patterns = [(t, _term_pattern(t)) for t in words]
    scored = []
    for i, s in enumerate(sections):
        folded = normalise_for_match(s.text + " " + s.heading).casefold()
        matched = [t for t, p in patterns if p.search(folded)]
        hit_terms.update(matched)
        if matched and i not in seen:
            scored.append((-len(matched), i, matched))
    picked += [(i, matched) for _, i, matched in sorted(scored)]
    if not picked:
        leads = [i for i, s in enumerate(sections) if s.location.startswith("abstract/")]
        leads += [i for i, s in enumerate(sections) if re.fullmatch(r"(fig|table|supp)\d+", s.location)]
        leads += [i for i, s in enumerate(sections) if s.location.startswith(("body/", "sec"))]
        picked = [(i, []) for i in leads]
    return picked, [t for t in focus if t not in hit_terms]


def _read_observations(article: Article, focus: list[str], fetches: list[_Fetch]) -> list[dict[str, Any]]:
    """The header (identifiers, route, access, outline, routes tried) and the passages chosen for the focus, in
    document order, all within RETURN_LIMIT characters of JSON."""
    outline, truncated = _outline(article.sections)
    picked, unmatched = _candidates(article, focus)
    # Follow the bibliography's actual xref ids, never guess that display number 8 means ref id B8.
    refs = {r.reference_id: r for r in article.references}
    explicit = [r.reference_id for r in article.references if any(
        t.casefold() in (r.reference_id.casefold(), f"reference {r.label}".casefold(),
                        f"ref {r.label}".casefold()) or (len(t) >= 4 and t.casefold() in r.title.casefold())
        for t in focus)]
    ordered = list(dict.fromkeys(explicit + [rid for i, _ in picked
                                             for rid in article.sections[i].reference_ids if rid in refs]))
    references = []
    for rid in ordered[:8]:
        r = refs[rid]
        obs = {"kind": "reference", "reference_id": rid, "label": r.label, "title": r.title,
               "pmid": r.pmid, "pmcid": r.pmcid, "doi": r.doi,
               "citation": r.citation if not r.title else "",
               "cited_by_locations": [s.location for s in article.sections if rid in s.reference_ids][:12]}
        if _size(references + [obs]) > 3000:
            break
        references.append(obs)
    header: dict[str, Any] = {
        "kind": "article", "pmid": article.pmid, "pmcid": article.pmcid, "doi": article.doi, "title": article.title,
        "journal": article.journal, "year": article.year, "publication_type": article.publication_type,
        "route": article.route, "access": article.access, "focus": focus, "unmatched_focus": unmatched,
        "sections_total": len(article.sections), "passages_shown": 0, "characters_shown": 0,
        "references_total": len(refs), "references_shown": len(references),
        "reference_note": "Discovery pointers only, not experimental evidence. Read the cited source itself; "
                          "xref links are paragraph-level, not proof that each cited paper supports every sentence.",
        "outline": outline, "outline_truncated": truncated, "routes_tried": [f.describe() for f in fetches]}
    budget = RETURN_LIMIT - _size([header, *references]) - 64        # room for the final counts
    patterns = [_term_pattern(t) for t in focus if not LOCATION_TERM.fullmatch(t)]
    chosen: list[tuple[int, dict[str, Any]]] = []
    for index, matched in picked:
        s = article.sections[index]
        obs = {"kind": "passage", "location": s.location, "heading": s.heading, "text": "", "matched": matched,
               "excerpt": False, "reference_ids": s.reference_ids}
        room = min(EXCERPT_LIMIT, budget - _size(obs) - 1)
        for _ in range(3):                              # JSON escaping can make the text cost more than its length
            if room < min(MIN_WINDOW, len(s.text)):
                break
            obs["text"], obs["excerpt"] = _window(s.text, patterns, room)
            over = _size(obs) + 1 - budget
            if over <= 0:
                budget -= _size(obs) + 1
                chosen.append((index, obs))
                break
            room -= over
    passages = [obs for _, obs in sorted(chosen, key=lambda x: x[0])]
    header["passages_shown"] = len(passages)
    header["characters_shown"] = sum(len(p["text"]) for p in passages)
    return [header, *references, *passages]


def _record(p: _Paper) -> dict[str, Any]:
    """A search record as listed: identifiers, bibliographic fields, access flags, the route a read would take and
    the whole abstract (plain text)."""
    return {"pmid": p.pmid, "pmcid": p.pmcid, "doi": p.doi, "title": p.title, "journal": p.journal, "year": p.year,
            "publication_type": p.publication_type, "is_open_access": p.is_open_access, "in_pmc": p.in_pmc,
            "nih_author_manuscript": p.nih_author_manuscript, "read_route": p.read_route,
            "abstract": " ".join(t for _, t in _abstract_parts(p.abstract_html))}


def _search_observations(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Preserve every returned paper's usable identifier. Shorten abstracts and display metadata, never silently
    remove the last discovery pointer to meet the packet bound. Full metadata remains in the raw result."""
    cap, title_cap, shown = ABSTRACT_LIMIT, TITLE_LIMIT, len(records)
    while shown:
        observations = [{**r, "title": _bounded(r["title"], title_cap), "abstract": _bounded(r["abstract"], cap),
                         "abstract_truncated": len(r["abstract"]) > cap} for r in records[:shown]]
        over = _size(observations) - SEARCH_LIMIT
        if over <= 0:
            return observations
        step = over // shown + 1
        if cap:
            cap = max(0, cap - max(step, 20))
        elif title_cap > TITLE_FLOOR:
            title_cap = max(TITLE_FLOOR, title_cap - max(step, 10))
        else:
            minimal = []
            for r in records:
                item = {k: r.get(k) for k in ("pmid", "pmcid", "title", "publication_type", "read_route")}
                if not item["pmid"] and not item["pmcid"]:
                    item["doi"] = r.get("doi")
                item.update(title=_bounded(r["title"], TITLE_FLOOR), abstract="", abstract_truncated=bool(r["abstract"]),
                            metadata_compacted=True)
                minimal.append(item)
            if _size(minimal) > SEARCH_LIMIT:
                minimal = [{k: v for k, v in item.items() if k in ("pmid", "pmcid", "doi", "title")}
                           for item in minimal]
            return minimal
    return []


# --- the tools --------------------------------------------------------------------------------------------------------

SEARCH_SPEC = ToolSpec(
    name=SEARCH_TOOL, route="literature",
    description="Search Europe PMC for papers (titles, short abstracts, identifiers and open-access flags). "
                "If all returned papers are reviews, make one additional search excluding indexed reviews and "
                "retain one review as a citation pointer. Unlabelled articles still need inspection. "
                "Lists papers to read; a search creates no evidence.",
    params={"query": ParamSpec(type="str", required=True,
                               description="Europe PMC query: gene, TF or variant names, assay and context words; "
                                           "fielded search allowed (TITLE_ABS:, PMCID:, AUTH:)"),
            "max_results": ParamSpec(type="int", description=f"records to list, 1 to {MAX_RESULTS} "
                                                             f"(default {DEFAULT_RESULTS}; more records means "
                                                             "shorter abstracts)")},
    assemblies=[],
    coverage_notes=f"Europe PMC metadata and abstracts in relevance order; the list is bounded to {SEARCH_LIMIT} "
                   "characters, so abstracts are shortened; searches miss papers.",
    result_semantics="records_found: papers listed (read one to extract its experiments); no_records_found: the "
                     "query matched nothing, which says nothing about the biology; incomplete: some returned records "
                     "had no PMID, PMCID or DOI and are not listed.",
    provider="Europe PMC", dataset_release="Europe PMC REST", rate_policy="serial", evidence_classes=[], network=True)

READ_SPEC = ToolSpec(
    name=READ_TOOL, route="literature",
    description="Read one paper: full text (Europe PMC open access, else NCBI PMC) or the abstract when no full text "
                "is available. Returns the section outline and the passages matching the focus terms, each with a "
                "stable location id to cite in extracted experiments. Also returns bibliography identifiers linked "
                "to the selected paragraphs, for discovering cited primary studies (not evidence).",
    params={"pmcid": ParamSpec(type="str", normalise="upper",
                               description="PMC id from literature_search (preferred)"),
            "pmid": ParamSpec(type="str", description="PubMed id, for a paper without a PMCID"),
            "focus": ParamSpec(type="list[str]", normalise="lower",
                               description="terms selecting the passages shown (TF, gene, allele, assay, context), "
                                           "or location ids from the outline (sec3, fig2, sec2.1/p4), or a reference "
                                           "id/label shown in the text (e.g. reference 8)")},
    assemblies=[],
    coverage_notes=f"Full text only from PMC; at most {RETURN_LIMIT} characters are shown per read (ask again with "
                   "other focus terms or locations: re-reading an article already read, by any of its ids, is free); "
                   "abstract-only reads do not use the full-text budget.",
    result_semantics="records_found: the paper's text was read (see access: full_text or abstract_only); "
                     "no_records_found: no article with this id; unavailable/error/cache_miss: the text could not be "
                     "retrieved, which says nothing about the biology.",
    provider="Europe PMC / NCBI PMC", dataset_release="Europe PMC REST", rate_policy="serial",
    evidence_classes=["binding_assay", "reporter_assay", "perturbation", "occupancy", "review"], network=True,
    fulltext_params=["pmcid", "pmid"])


@register_tool(SEARCH_SPEC)
def literature_search(params: dict[str, Any], ctx: ToolContext) -> AdapterResult:
    """Europe PMC search: one observation per article (records sharing an id merged), within SEARCH_LIMIT
    characters. No Evidence: a search is triage."""
    http = ctx.http
    if http is None:
        return AdapterResult(execution_status="unavailable", message="the literature route has no HTTP client")
    query = clean_text(params["query"])
    if not query or len(query) > QUERY_LIMIT:
        return AdapterResult(execution_status="not_applicable",
                             message=f"literature_search needs a query of 1 to {QUERY_LIMIT} characters")
    if _EMAIL.search(query):
        return AdapterResult(execution_status="not_applicable",
                             message="literature_search never sends an e-mail address: remove it from the query")
    wanted = int(params.get("max_results") or DEFAULT_RESULTS)
    n = min(max(wanted, 1), MAX_RESULTS)
    url = search_url(query, n)
    coverage = Coverage(requested_scope=f"Europe PMC search: {query} (up to {n} records)",
                        limitations=["a search lists papers: it is not evidence, and an empty search is not evidence "
                                     "of absence"])
    r = http.get(url)
    if not r.ok:
        outcome, note = _outcome(r)
        if outcome == "no_records":
            return AdapterResult(retrieval_status="no_records_found", coverage=coverage,
                                 message=f"Europe PMC search: {note} (no records)")
        return AdapterResult(execution_status=_Fetch.failure(outcome), coverage=coverage,
                             message=f"Europe PMC search: {note}")
    if not isinstance(r.data, dict) or not isinstance(r.data.get("resultList"), dict):
        return AdapterResult(execution_status="error", coverage=coverage, cached=r.cached,
                             message="Europe PMC search returned an unexpected payload")
    rows = r.data["resultList"].get("result")
    rows = rows if isinstance(rows, list) else []
    hits = r.data.get("hitCount")
    hits = hits if isinstance(hits, int) else len(rows)
    papers, dropped = _papers(rows)
    papers = papers[:n]
    discovery = None
    citation_lane = None
    fallback_incomplete = False
    cached = r.cached
    if n >= 2 and papers and all(_REVIEW.search(p.publication_type) for p in papers):
        # One bounded, auditable extra request. Do not broaden the scientific scope silently, and do not
        # interpret absence of a Review tag as proof of a primary experiment.
        query2 = f"({query}) NOT PUB_TYPE:review"
        url2 = search_url(query2, MAX_RESULTS)
        r2 = http.get(url2)
        cached = cached and r2.cached
        discovery = {"query": query2, "url": url2, "reason": "all returned papers indexed as reviews",
                     "status": "unavailable", "records": []}
        if r2.ok and isinstance(r2.data, dict) and isinstance(r2.data.get("resultList"), dict):
            rows2 = r2.data["resultList"].get("result") or []
            candidates, dropped2 = _papers(rows2 if isinstance(rows2, list) else [])
            candidates = [p for p in candidates if not _REVIEW.search(p.publication_type)]
            discovery.update(status="records_found" if candidates else "no_records_found",
                             hit_count=r2.data.get("hitCount"),
                             records=[{**_record(p), "source": p.source} for p in candidates])
            fallback_incomplete = bool(dropped2)
            if candidates:
                papers = candidates[:n - 1] + papers[:1]
        else:
            fallback_incomplete = True
        coverage.limitations.append("Review-only result list triggered one non-review search; its status is "
                                    f"{discovery['status']}. Non-review indexing does not certify primary evidence.")
    elif hits > n and n >= 6 and not re.search(r"sort_\w+:|\b(?:PMCID|EXT_ID|DOI):", query, re.I):
        # Retrieval diversity, not an evidence score. Keep relevance results and sample established cited work
        # under exactly the same query; never insert a known paper or gene from an evaluation label.
        query2 = f"({query}) sort_cited:y"
        r2 = http.get(search_url(query2, n))
        citation_lane = {"query": query2, "status": "unavailable", "records": []}
        cached = cached and r2.cached
        if r2.ok and isinstance(r2.data, dict) and isinstance(r2.data.get("resultList"), dict):
            other, _ = _papers(r2.data["resultList"].get("result") or [])
            citation_lane.update(status="records_found" if other else "no_records_found",
                                 records=[_record(p) for p in other])
            mixed, seen = [], set()
            for a, b in zip(papers + [None] * len(other), other + [None] * len(papers), strict=True):
                for p in (a, b):
                    if p is not None and not p.keys & seen:
                        mixed.append(p)
                        seen |= p.keys
            papers = mixed[:n]
        coverage.limitations.append("Bounded relevance/citation-order discovery mix. Citation count is not "
                                    "evidence quality; inspect primary experiments. Secondary lane: " +
                                    citation_lane["status"])
    status: RetrievalStatus = ("incomplete" if dropped or (hits and not papers)
                               or fallback_incomplete
                               else "records_found" if papers else "no_records_found")
    records = [_record(p) for p in papers]
    observations = _search_observations(records)
    version = str(r.data.get("version") or "")
    coverage.assessed_scope = f"{len(observations)} of {hits} hits listed, in Europe PMC relevance order"
    if discovery:
        coverage.assessed_scope = (f"{len(observations)} papers listed after review-only fallback; original query "
                                   f"had {hits} hits; each query uses relevance order, candidates shown first")
    elif citation_lane:
        coverage.assessed_scope = f"{len(observations)} papers from relevance and citation-order discovery lanes"
    if dropped:
        coverage.limitations.append(f"{dropped} returned record(s) had no PMID, PMCID or DOI and are not listed")
    left_out = len(papers) - len(observations)
    if left_out:
        coverage.limitations.append(f"{left_out} further record(s) found but not listed: the list is bounded to "
                                    f"{SEARCH_LIMIT} characters (ask for fewer records or a narrower query)")
    raw = {"query": query, "url": url, "hit_count": hits, "version": version, "dropped": dropped,
           "original_records": rows, "discovery": discovery, "citation_lane": citation_lane,
           "records": [{**rec, "source": p.source} for rec, p in zip(records, papers, strict=True)]}
    message = (f"Europe PMC: {len(observations)} of {hits} hits listed for '{query}'" if papers else
               f"Europe PMC: no usable records for '{query}' (an empty search is not evidence of absence)")
    if left_out:
        message += f"; {left_out} more found but not listed (size bound)"
    if wanted > MAX_RESULTS:
        message += f"; max_results is capped at {MAX_RESULTS}"
    if discovery:
        message = f"Europe PMC: {len(observations)} papers listed after review-only fallback ({discovery['status']})"
    return AdapterResult(retrieval_status=status, observations=observations, coverage=coverage, raw=raw,
                         message=message, cached=cached, retrieval_time=r.retrieved_utc or None,
                         dataset_release=f"Europe PMC REST {version}" if version else None)


@register_tool(READ_SPEC)
def literature_read(params: dict[str, Any], ctx: ToolContext) -> AdapterResult:
    """Read one article (see the module docstring for the routes). The raw result is the parsed Article; the agent
    sees the outline and the focus passages. Every id of the article goes to the runner (article_ids), so a re-read by
    another id is free; only full text counts against the full-text budget."""
    http = ctx.http
    if http is None:
        return AdapterResult(execution_status="unavailable", message="the literature route has no HTTP client")
    given_pmcid, given_pmid = params.get("pmcid"), params.get("pmid")
    pmcid = _id_of("pmcid", given_pmcid if not str(given_pmcid or "").isdigit() else f"PMC{given_pmcid}")
    pmid = _id_of("pmid", given_pmid)
    if (given_pmcid and not pmcid) or (given_pmid and not pmid) or not (pmcid or pmid):
        return AdapterResult(execution_status="not_applicable",
                             message="literature_read needs a pmcid (PMC followed by digits) or a pmid (digits)")
    focus = [str(t)[:FOCUS_TERM_LIMIT] for t in params.get("focus") or []][:MAX_FOCUS_TERMS]
    read = _read_article(http, pmcid, pmid)
    label = _label(pmid, pmcid)
    requested = f"{label}" + (f", focus: {', '.join(focus)}" if focus else "")
    tried = [f.describe() for f in read.fetches]
    if read.conflict:
        return AdapterResult(execution_status="not_applicable", message=f"the ids name two articles: {read.conflict}",
                             coverage=Coverage(requested_scope=requested, limitations=tried))
    article = read.article
    if article is None:
        failures = [f for f in read.fetches if f.outcome in FAILURE_RANK]
        coverage = Coverage(requested_scope=requested, limitations=tried)
        if failures:
            worst = max(failures, key=lambda f: FAILURE_RANK[f.outcome])
            return AdapterResult(execution_status=worst.status, coverage=coverage,
                                 message=f"{label} could not be read ({worst.route} {worst.outcome}): {worst.note}")
        return AdapterResult(retrieval_status="no_records_found", coverage=coverage,
                             message=f"no article {label} in Europe PMC or PMC")
    used = [f for f in read.fetches if f.outcome == "ok"]
    observations = _read_observations(article, focus, read.fetches)
    full = article.access == "full_text"
    source = {"europepmc_fulltext": "Europe PMC (open access)", "ncbi_efetch": "NCBI PMC (efetch)"}
    limitations = [f"route: {d}" for d in tried if not d.startswith(("metadata ok", "europepmc_fulltext ok",
                                                                     "ncbi_efetch ok"))]
    if not full:
        limitations.append("abstract only: methods, controls and full results were not read")
    header = observations[0]
    if header["passages_shown"] < len(article.sections):
        limitations.append(f"{header['passages_shown']} of {len(article.sections)} passages shown; ask again with "
                           "other focus terms or location ids (re-reading the same article is free)")
    message = (f"full text of {article.key} from {source[article.route]}" if full else
               f"abstract only for {article.key}: {read.why_abstract}")
    message += f"; {header['passages_shown']} of {len(article.sections)} passages shown"
    return AdapterResult(
        retrieval_status="records_found" if article.sections else "incomplete", observations=observations,
        coverage=Coverage(requested_scope=requested,
                          assessed_scope="full text: abstract, sections, figure and table captions" if full else
                          "abstract only", limitations=limitations),
        raw=article.model_dump(mode="json"), message=message,
        provider="NCBI PMC (E-utilities)" if article.route == "ncbi_efetch" else "Europe PMC",
        cached=bool(used) and all(f.cached for f in used),
        retrieval_time=next((f.retrieved for f in reversed(used) if f.retrieved), None),
        fulltext_article=article.key, fulltext_read=full, article_ids=article.source_ids(),
        dataset_release=f"Europe PMC REST {read.version}" if read.version else "NCBI PMC")


# --- verification -----------------------------------------------------------------------------------------------------

# A negation just before a quoted stretch ("did not | increase BCL11A"; "no detectable | binding"): the stretch alone
# would say the opposite of the sentence.
_NEGATOR = re.compile(r"(?:\b(?:not|no|never|without|nor|neither|cannot|unable to|fail(?:s|ed)? to)|n't)"
                      r"(?:\s+[\w-]+){0,2}\s*$", re.I)


def _quoted(passage: str) -> str:
    """A quoted passage in matching form, without wrapping quotation marks."""
    text = normalise_for_match(passage)
    while len(text) >= 2 and text[0] in _QUOTE_CHARS and text[-1] in _QUOTE_CHARS:
        text = text[1:-1].strip()
    return text


def _span(text: str, target: str) -> str | None:
    """The exact source stretch of `text` that `target` (in matching form) matches as whole words, with no negation
    governing it; None when there is none."""
    source = unicodedata.normalize("NFC", text)
    norm, starts, ends = _norm_map(source)
    at = norm.find(target)
    while at >= 0:
        end = at + len(target)
        cut_before = target[0].isalnum() and at > 0 and norm[at - 1].isalnum()
        cut_after = target[-1].isalnum() and end < len(norm) and norm[end].isalnum()
        if not (cut_before or cut_after or _NEGATOR.search(norm[max(0, at - 60):at])):
            return source[starts[at]:ends[end - 1]]
        at = norm.find(target, at + 1)
    return None


def _locate(article: Article, passage: str, prefer: str | None = None) -> tuple[ArticleSection, str] | None:
    """The section holding the passage (`prefer` first, then document order) and the exact source span it matched;
    None when no single section holds it, or when it is shorter than PASSAGE_MIN or longer than PASSAGE_MAX."""
    target = _quoted(passage)
    if not PASSAGE_MIN <= len(target) <= PASSAGE_MAX:
        return None
    for s in sorted(article.sections, key=lambda s: s.location != prefer):
        if (span := _span(s.text, target)) is not None:
            return s, span
    return None


def verify_passage(article: Article, passage: str, *, prefer: str | None = None) -> str | None:
    """The location of the section holding the passage verbatim (typography folded as in normalise_for_match), as
    whole words and not governed by a negation just before it, trying `prefer` (the location the extractor named)
    first; None when no single section holds it, or when the passage is shorter than PASSAGE_MIN or longer than
    PASSAGE_MAX characters."""
    found = _locate(article, passage, prefer)
    return found[0].location if found else None


def _require_read(call: ToolCall) -> None:
    if (call.tool_name != READ_TOOL or call.execution_status != "success"
            or call.retrieval_status not in EVIDENCE_FROM or not call.read_article):
        raise ExtractionRefused(f"{call.tool_call_id} is not a successful literature read ({call.tool_name}: "
                                f"{call.execution_status}/{call.retrieval_status})")


def _same_article(article: Article, read_article: str | None) -> bool:
    parsed = _parse_id(read_article)
    return parsed is not None and parsed in _article_keys(article)


def load_article(run_dir: str | Path, call: ToolCall) -> Article:
    """The article a successful literature read saved (run_dir/raw/T#.json). Refused when the call is not a
    successful read, the file is missing or not an article, its bytes no longer match the hash recorded at the read,
    or it is another article than the one the read reports."""
    _require_read(call)
    if not re.fullmatch(r"T\d+", call.tool_call_id):
        raise ExtractionRefused(f"{call.tool_call_id!r} is not a tool call id")
    rel = f"raw/{call.tool_call_id}.json"
    try:
        data = (Path(run_dir) / rel).read_bytes()
    except OSError as e:
        raise ExtractionRefused(f"{rel} is missing: the text {call.tool_call_id} read was not saved") from e
    if call.raw_result_hash and hashlib.sha256(data).hexdigest() != call.raw_result_hash:
        raise ExtractionRefused(f"{rel} has changed since {call.tool_call_id} read it")
    try:
        article = Article.model_validate_json(data)
    except ValidationError as e:
        raise ExtractionRefused(f"{rel} is not a parsed article") from e
    if not _same_article(article, call.read_article):
        raise ExtractionRefused(f"{rel} holds {article.key}, not {call.read_article}")
    return article


def _read_ids(call: ToolCall) -> set[str]:
    """Every id of the article a read returned, in graph.article_key form: what the runner recorded (read_article,
    fulltext_article, article_ids) and the ids the read's header reports."""
    first = call.observations[0] if call.observations else {}
    header = first if isinstance(first, dict) and first.get("kind") == "article" else {}
    keys = {article_key(v) for v in (call.read_article, call.fulltext_article, *call.article_ids,
                                     header.get("pmid"), header.get("doi"))}
    keys.add(article_key(header.get("pmcid"), pmcid=True))
    return {k for k in keys if k}


def find_read(graph: ClaimGraph, record: ExperimentRecord) -> ToolCall:
    """The successful literature read of the article a record cites (by any of its PMID, PMCID or DOI), preferring a
    read that returned full text, then the earliest. Refused when the run read no such article."""
    cited = {k for k in (article_key(record.source_id), article_key(record.pmcid, pmcid=True),
                         article_key(record.doi)) if k}
    reads = [t for t in graph.tool_calls.values()
             if t.tool_name == READ_TOOL and t.execution_status == "success" and t.read_article
             and t.retrieval_status in EVIDENCE_FROM and cited & _read_ids(t)]
    if not reads:
        raise ExtractionRefused(f"no literature read in this run returned {record.source_id}; read it before "
                                "extracting its experiments")
    return min(reads, key=lambda t: (t.fulltext_article is None, int(t.tool_call_id[1:])))


def _check_citation(record: ExperimentRecord, article: Article, call: ToolCall) -> None:
    """Every id the record states must be this article's; at least one must be checkable against it."""
    have = dict(_article_keys(article))
    checked = False
    for name, value in (("source_id", record.source_id), ("pmcid", record.pmcid), ("doi", record.doi)):
        if not value:
            continue
        parsed = _parse_id(value)
        if parsed is None:
            raise ExtractionRefused(f"the record's {name} {value!r} is not a PMID, PMCID or DOI")
        kind, ident = parsed
        if kind not in have:
            continue
        if have[kind] != ident:
            raise ExtractionRefused(f"the record cites {value}, but {call.tool_call_id} read "
                                    f"{', '.join(article.source_ids())}: extract only from the article that was read")
        checked = True
    if not checked:
        raise ExtractionRefused(f"the record cites no id of the article {call.tool_call_id} read "
                                f"({', '.join(article.source_ids())})")


# --- what an experiment is: class, independence and retelling ----------------------------------------------------------

_REVIEW = re.compile(r"\breview", re.I)
_CELLULAR = re.compile(r"crispr|\bcas9|\bcas12|\bdcas9|knock-?down|knock-?out|knock-?in|\bsirna|\bshrna|\brnai\b|"
                       r"morpholino|over-?express|ectopic(?:ally)? express|genome edit|base edit|prime edit|\btalen|"
                       r"zinc-finger nuclease|transgenic|degron|\bdtag\b|\binhibitor|\binhibition\b|antisense oligo|"
                       r"\bsgrna|guide rna")
_ASSAYS: tuple[tuple[EvidenceClass, re.Pattern[str]], ...] = (
    ("binding_assay", re.compile(r"\bemsa|electrophoretic mobility|gel-? ?shift|supershift|band-? ?shift|"
                                 r"pull-? ?down|\bdnap\b|\bdapa\b|surface plasmon|\bspr\b|footprint|"
                                 r"fluorescence (?:polari[sz]ation|anisotropy)|binding assay|\bselex\b")),
    ("reporter_assay", re.compile(r"luciferase|reporter|\bmpra\b|massively parallel|starr-?seq|\bcat assay|"
                                  r"galactosidase")),
    ("occupancy", re.compile(r"\bchip\b|chromatin immunoprecipitation|cut ?& ?run|cut ?& ?tag|cut and (?:run|tag)|"
                             r"\bdamid\b")),
)
_CONSTRUCT = re.compile(r"delet|disrupt|excis|mutagenesis|mutat|ablat")
_ENDPOINTS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("reporter", re.compile(r"luciferase|reporter|enhancer activity|promoter activity|transcriptional activity|"
                            r"transactivation|mpra|starr")),
    ("binding", re.compile(r"bind|occupan|\bchip\b|emsa|shift|pull-? ?down|recruit")),
    ("chromatin", re.compile(r"accessib|atac|dnase|h3k\d|histone|methylat|chromatin")),
    ("phenotype", re.compile(r"phenotyp|trait|disease|cholesterol|\bldl\b|\bhdl\b|lipid|plasma|serum|tumou?r|growth|"
                             r"survival|prolifer|weight|glucose|insulin|haemoglobin|hemoglobin")),
    ("expression", re.compile(r"express|mrna|transcript|protein|abundance|qpcr|rt-pcr|western|rna-seq|level")),
)
# Sections and wording that retell work rather than report it: their passages are context, never a new observation.
_RETOLD_HEADINGS = frozenset({"introduction", "background", "discussion", "conclusion", "conclusions",
                              "concluding remarks", "perspective", "perspectives", "outlook"})
_RETELLING = re.compile(
    r"\bpreviously\b|\bprevious (?:[\w-]+ ){0,3}?(?:stud|work|report|finding|experiment|assay|analys|data|paper|"
    r"observation)|\bearlier (?:[\w-]+ ){0,2}?(?:stud|work|report|finding|experiment|paper)|"
    r"\b(?:has|have|had) (?:also )?been (?:previously )?(?:shown|reported|demonstrated|described|proposed|suggested|"
    r"identified|found)\b|\bet al\b|\breported (?:by|in|previously|earlier|before)\b|"
    r"\bas (?:previously |earlier )?(?:reported|described|shown)\b|\bothers have\b|\bprior (?:stud|work|report)", re.I)


def _fold(*texts: str) -> str:
    return normalise_for_match(" ".join(t for t in texts if t)).casefold()


def assay_class(intervention: str) -> tuple[EvidenceClass | None, str]:
    """The evidence class an intervention names, or (None, why). A cellular manipulation (CRISPR, knockdown,
    overexpression, an inhibitor) is a perturbation whatever it is read out with; otherwise exactly one assay family
    (binding assay, reporter assay, ChIP-type occupancy) decides; a deletion or mutation with no assay named is a
    perturbation. Two assay families in one intervention are two experiments."""
    text = _fold(intervention)
    if _CELLULAR.search(text):
        return "perturbation", ""
    named = [cls for cls, pattern in _ASSAYS if pattern.search(text)]
    if len(named) > 1:
        return None, f"the intervention names several assays ({', '.join(named)}): give one experiment per assay"
    if named:
        return named[0], ""
    if _CONSTRUCT.search(text):
        return "perturbation", ""
    return None, ("the intervention names no assay this route maps (EMSA or another binding assay; luciferase, MPRA "
                  "or another reporter; CRISPR, knockdown, overexpression, an inhibitor or a deletion; ChIP or "
                  "CUT&RUN)")


def _endpoint_category(endpoint: str) -> str:
    text = _fold(endpoint)
    return next((name for name, pattern in _ENDPOINTS if pattern.search(text)), "other")


# Where an article points to its own data: "(Fig. 3B)", "Figure S4E", "Table 1", "Extended Data Fig. 2".
_CALLOUT = re.compile(r"\b(?:fig(?:ure)?s?|tables?)\b\.?\s*S?\d", re.I)


def _retold(section: ArticleSection, passage: str, own_figures: bool = False) -> str | None:
    """Why a passage retells rather than reports (it sits in an Introduction, Background or Discussion section, or
    uses retelling wording such as "previously" or "et al."), or None. With `own_figures`, wording alone does not
    make a retelling of a passage that points to one of the article's own figures or tables: "differentiated as
    previously described (Patsch et al., 2015) ... higher expression of EDN1 (Figure 3B)" cites a method and reports
    the article's result. The reader's quotations run to several sentences, and this is how its records of an
    article's own experiments stopped being filed as retellings."""
    for part in section.heading.split("\u203a"):
        name = re.sub(r"^[\dIVXivx]+[.)]?\s+", "", part.strip()).casefold()
        if name in _RETOLD_HEADINGS:
            return f"the passage is in the {part.strip()} section"
    if (m := _RETELLING.search(passage)) and not (own_figures and _CALLOUT.search(passage)):
        return f"the passage retells earlier work ('{m.group(0)}')"
    return None


# --- what an experiment is about: names checked against the paper -----------------------------------------------------

# HGNC writes Greek letters as Latin capitals (C/EBP-alpha is CEBPA, HNF-4-alpha HNF4A).
_GREEK = str.maketrans({**{0x03B1 + i: c for i, c in enumerate("ABGDEZHQIKLMNXOPRSSTUFCYW")},
                        **{0x0391 + i: c for i, c in enumerate("ABGDEZHQIKLMNXOPR")},
                        **{0x03A3 + i: c for i, c in enumerate("STUFCYW")}})
_CHAIN = re.compile(r"[0-9A-Za-z\u0391-\u03a9\u03b1-\u03c9]+(?:[-/.][0-9A-Za-z\u0391-\u03a9\u03b1-\u03c9]+)*")
_SEPARATORS = re.compile(r"[-/.]")
_STOP_WORDS = frozenset("a an and as at by for from in into its near of on or that the this to with within around "
                        "about across along containing contains harbouring harboring carrying bearing including "
                        "spanning overlapping encompassing surrounding".split())
_VARIANT_TOKEN = re.compile(r"rs\d+|chr[0-9xym]{1,2}|\d{5,}")      # an rsID, a chromosome or a position


def _compact(symbol: str) -> str:
    """A gene symbol in one spelling: GATA-1 and Gata1 are GATA1, C/EBP-alpha is CEBPA, Nkx2.5 is NKX25."""
    return _SEPARATORS.sub("", symbol.translate(_GREEK)).upper()


def _symbol_forms(text: str) -> set[str]:
    """Every gene-symbol spelling a text contains: each word chain (GATA-1, C/EBP-alpha, GATA1/TAL1) whole and each
    of its pieces, in compact form."""
    forms: set[str] = set()
    for m in _CHAIN.finditer(normalise_for_match(text)):
        chain = m.group()
        forms.add(_compact(chain))
        forms.update(_compact(p) for p in _SEPARATORS.split(chain) if p)
    return forms


def _symbol_in(forms: Iterable[str], name: str, resolver: SymbolResolver | None) -> str | None:
    """The name to keep when `forms` (a text's _symbol_forms) name this TF or gene (as written, in another spelling,
    or by an HGNC previous symbol when a resolver is given), else None. A paper's spelling of an approved symbol
    (GATA-1, C/EBP-alpha) is kept as the approved symbol when the resolver knows it, so the graph can match it."""
    key = _compact(normalise_for_match(name))
    if not key or " " in key:
        return None
    direct = resolver(name) if resolver else None
    approved = direct or (resolver(key) if resolver else None)
    if key in forms:
        return approved[0] if approved and not direct else name
    if resolver and approved and any(resolver(f) == approved for f in forms):
        return name
    return None


def _singular(token: str) -> str:
    return token[:-1] if len(token) > 3 and token.endswith("s") and not token.endswith("ss") else token


def _tokens(text: str) -> list[str]:
    """Words for name matching: case, punctuation, digit grouping (60,490,908) and a plural s ignored."""
    folded = re.sub(r"(?<=\d),(?=\d{3}(?!\d))", "", _fold(text))
    return [_singular(t) for t in re.findall(r"[0-9a-z\u03b1-\u03c9]+", folded)]


@dataclass(frozen=True)
class _Scope:
    """Where an extraction's names must come from: the verified section (a paragraph, a caption or a table's cells
    with the table's caption) and its heading; the whole article only for the variant an element is named by."""
    location: str
    text: str
    symbols: frozenset[str]
    words: frozenset[str]
    article_words: frozenset[str]
    resolver: SymbolResolver | None

    @classmethod
    def of(cls, article: Article, section: ArticleSection, resolver: SymbolResolver | None) -> "_Scope":
        parts = [section.heading, section.text]
        if section.location.endswith("/cells") and (table := article.section(section.location.rsplit("/", 1)[0])):
            parts.append(table.text)
        text = " ".join(parts)
        everything = " ".join([article.title, *(s.text for s in article.sections)])
        return cls(section.location, text, frozenset(_symbol_forms(text)), frozenset(_tokens(text)),
                   frozenset(_tokens(everything)), resolver)

    def symbol(self, name: str) -> str | None:
        """The TF or gene name to keep when the scope names it (_symbol_in), else None."""
        return _symbol_in(self.symbols, name, self.resolver)

    def region(self, name: str) -> bool:
        """Whether the scope names an element or trait: every word of the name (articles and linking words aside)
        occurs there; an rsID, chromosome or position in an element's name may occur anywhere in the article."""
        words = [w for w in _tokens(name) if w not in _STOP_WORDS]
        return bool(words) and all(w in (self.article_words if _VARIANT_TOKEN.fullmatch(w) else self.words)
                                   for w in words)


def _names(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(x for x in (clean_text(v) for v in values) if x))[:MAX_NAMES]


def _grounded(values: Iterable[str], check: Any, what: str, scope: _Scope, notes: list[str]) -> list[str]:
    """The names the scope names (as `check` returns them); the others are dropped with a limitation."""
    kept: list[str] = []
    dropped: list[str] = []
    for name in _names(values):
        hit = check(name) if len(name) <= NAME_LIMIT else None
        if hit:
            kept.append(name if hit is True else hit)
        else:
            dropped.append(_bounded(name, 60))
    if dropped:
        notes.append(f"{what} not named where the passage is ({scope.location}), so not kept: {', '.join(dropped)}")
    return list(dict.fromkeys(kept))


@dataclass(frozen=True)
class _About:
    tfs: list[str]
    genes: list[str]
    elements: list[str]
    traits: list[str]


_TF_GENE_ACTION = re.compile(r"\bsirna|\bshrna|\brnai\b|knock-?down|over-?express|ectopic(?:ally)? express|morpholino|"
                             r"degron|\bdtag\b|antisense|\binhibitor|forced expression")
_REGION_ACTION = re.compile(r"crispr|cas9|cas12|\bkrab\b|\bvp64\b|\bvpr\b|talen|zinc-finger|delet|excis|disrupt|ablat|"
                            r"remov|mutat|mutagen|\bedit|knock-?in|\binsert|silenc|tiling|reporter|luciferase|\bmpra\b|"
                            r"starr|construct|transgen")


def _about(record: ExperimentRecord, cls: EvidenceClass, passage: str, scope: _Scope, notes: list[str]) -> _About:
    """What the experiment is about, as the paper names it. Refused: a binding or occupancy assay without the factor
    it measured, a TF or gene manipulation without that TF or gene, and a record that says it changed an element or
    allele where the paper describes only a knockdown, overexpression or inhibitor (a TF or gene perturbation tests
    neither an element nor the variant's alleles, core C3-2). Elements are dropped for a TF or gene manipulation, and
    for a perturbation whose record does not say what it changed."""
    tfs = _grounded(record.about_tfs, scope.symbol, "TF(s)", scope, notes)
    genes = _grounded(record.about_genes, scope.symbol, "gene(s)", scope, notes)
    traits = _grounded(record.about_traits, scope.region, "trait(s)", scope, notes)
    elements = _grounded(record.about_elements, scope.region, "element(s)", scope, notes)
    if cls == "review":
        return _About(tfs, genes, elements, traits)
    manipulated = record.manipulated
    said = _fold(passage)
    if manipulated in ("element", "allele") and _TF_GENE_ACTION.search(said) and not _REGION_ACTION.search(said):
        raise ExtractionRefused(f"the record says the experiment changed an {manipulated}, but the passage describes a "
                                "knockdown, overexpression or inhibitor: that is a TF or gene perturbation, which does "
                                "not test what the variant's alleles or an element do (it shows the factor matters); "
                                "set manipulated to tf or gene")
    if cls == "perturbation" and manipulated == "element" and not _REGION_ACTION.search(_fold(scope.text)):
        raise ExtractionRefused("the record says the experiment changed an element, but the passage's section "
                                "describes no change to a region (a deletion, CRISPR interference or activation, a "
                                "mutation or a reporter construct)")
    if elements and (manipulated in ("tf", "gene") or (cls == "perturbation" and manipulated == "none")):
        target = {"tf": "TF", "gene": "gene"}.get(manipulated)
        why = (f"a {target} perturbation does not test what an element does (it shows the {target} matters)" if target
               else "the record does not say what the perturbation changed")
        notes.append(f"{why}: element(s) not kept ({', '.join(elements)})")
        elements = []
    if cls in ("binding_assay", "occupancy") and not tfs:
        raise ExtractionRefused(f"a {cls.replace('_', ' ')} is about the factor it measured: name it in about_tfs as "
                                f"the passage's section ({scope.location}) names it")
    if cls == "perturbation" and manipulated == "tf" and not tfs:
        raise ExtractionRefused(f"a TF manipulation is about that TF: name it in about_tfs as the passage's section "
                                f"({scope.location}) names it")
    if cls == "perturbation" and manipulated == "gene" and not genes:
        raise ExtractionRefused(f"a gene manipulation is about that gene: name it in about_genes as the passage's "
                                f"section ({scope.location}) names it")
    return _About(tfs, genes, elements, traits)


# --- alleles ----------------------------------------------------------------------------------------------------------

_ALLELE_NOUN = r"(?:allele|probe|construct|haplotype|oligo\w*|variant|version|sequence|form)s?\b"


def _allele_pattern(allele: str) -> re.Pattern[str]:
    """Where a text names a base as an allele: next to allele wording ("the T allele", "allele T", "T and G probes"),
    or in a conversion ("T to G", "T>G", "the T allele to G"); never a bare letter ("A 300-bp deletion", "T cells")."""
    b, other = re.escape(allele), "[ACGT]"
    pair = r"(?: and | or |/| versus | vs\.? )"
    conversion = r"(?:\s?(?:>|\u2192|->)\s?|-to-| to | into )"
    return re.compile(
        rf"(?<![A-Za-z0-9]){b}[- ]{_ALLELE_NOUN}|\balleles? {b}(?![A-Za-z0-9])|"
        rf"(?<![A-Za-z0-9]){b}{pair}{other}[- ]{_ALLELE_NOUN}|(?<![A-Za-z0-9]){other}{pair}{b}[- ]{_ALLELE_NOUN}|"
        rf"(?<![A-Za-z0-9]){other}(?:[- ]allele)?{conversion}(?:an? |the )?{b}(?![A-Za-z0-9])|"
        rf"(?<![A-Za-z0-9]){b}(?:[- ]allele)?{conversion}(?:an? |the )?{other}(?![A-Za-z0-9])")


_REF_ALT = {"ref": re.compile(r"\bref(?:erence)?[- ]allele|\ballele[s]? \(?ref(?:erence)?\b", re.I),
            "alt": re.compile(r"\balt(?:ernat(?:iv)?e)?[- ]allele|\ballele[s]? \(?alt(?:ernat(?:iv)?e)?\b", re.I)}


def _names_allele(text: str, allele: str) -> bool:
    if allele in _REF_ALT:
        return bool(_REF_ALT[allele].search(text))
    return bool(_allele_pattern(allele).search(text))


def _alleles_named(text: str) -> set[str]:
    return {a for a in ("A", "C", "G", "T", "ref", "alt") if _names_allele(text, a)}


def _one_allele(value: str) -> str | None:
    """The single allele a compared_allele names ("T", "the T allele", "ref", "alternative allele"), or None for a
    genotype (TT, T/G, homozygous) or anything else."""
    text = " ".join(re.sub(r"\([^)]*\)", " ", value).split())
    words = {w.casefold() for w in re.findall(r"[A-Za-z]+", text)}
    ref, alt = words & {"ref", "reference"}, words & {"alt", "alternative", "alternate"}
    if ref or alt:
        return None if (ref and alt) or len(words - {"ref", "reference", "alt", "alternative", "alternate", "the",
                                                     "allele"}) else ("ref" if ref else "alt")
    m = re.fullmatch(r"(?:the\s+)?([ACGTacgt])(?:[\s-]+allele)?", text)
    return m.group(1).upper() if m else None


def _allele_scope(record: ExperimentRecord) -> str | None:
    """What an experiment that changed a factor or a region cannot show about the variant's alleles, in the terms of
    the graph's rule (core C3-2), or None for a design that compares alleles or only observes."""
    if record.manipulated in ("tf", "gene"):
        factor = "TF" if record.manipulated == "tf" else "gene"
        return (f"a {factor} perturbation does not test what the variant's alleles do (it shows the {factor} matters, "
                "not that the alleles differ): context only for claims about them")
    if record.manipulated == "element":
        return ("an element perturbation (a region deletion, CRISPR interference or activation, a construct without an "
                "allele comparison) shows that the element matters, not that the variant's alleles differ: indirect at "
                "most for claims about what the alleles do")
    return None


def _compared(record: ExperimentRecord, cls: EvidenceClass, passage: str, scope: _Scope,
              notes: list[str], alias_alts: set[str] | None = None) -> tuple[str | None, bool]:
    """(the allele the direction refers to, whether the design compares alleles). The allele comes only from
    compared_allele, for a design that compares the variant's alleles (manipulated "allele", or an assay of
    constructs or occupancy whose section names two alleles), when the passage names it as an allele. A genotype is
    the context's, never an allele: a region deleted in TT cells says nothing about the T allele. A TF or gene
    perturbation and an element perturbation compare no alleles (core C3-2), so they never keep one."""
    design = record.manipulated == "allele" or (
        record.manipulated == "none" and cls in ("binding_assay", "reporter_assay", "occupancy")
        and len(_alleles_named(scope.text)) >= 2)
    value = clean_text(record.compared_allele)
    if not value:
        return None, design
    allele = _one_allele(value)
    reason = ("is not one allele (a genotype describes the context, not the allele a direction refers to)"
              if allele is None else
              "is not kept: " + {"tf": "a TF perturbation does not test the variant's alleles",
                                 "gene": "a gene perturbation does not test the variant's alleles",
                                 "element": "an element perturbation does not compare the variant's alleles"}.get(
                  record.manipulated, "the experiment does not compare the variant's alleles (its section names "
                                      "fewer than two)")
              if not design else
              "is not named as an allele in the passage" if not _names_allele(passage, allele) and
              allele not in (alias_alts or set()) else "")
    if reason:
        notes.append(f"compared_allele '{_bounded(value, 40)}' {reason}")
        return None, design
    return allele, design


# --- which variant: entries checked against the paper ---------------------------------------------------------------

# An rsID as a whole word: rs1427407 never matches inside rs14274070.
_RSID_MENTION = re.compile(r"(?<![0-9A-Za-z])rs(\d{1,12})(?![0-9])", re.I)
# A chromosome position ("chr2:60490908", "chr2:60,490,908", "2:60490908"). In a paper an unprefixed one needs seven
# digits or an allele pair after it, so ratios, times and dilutions (3:1, 1:1000, 1:200,000) never read as positions;
# a range ("chr2:60490700-60491200") is a region, not a variant.
_SITE_MENTION = re.compile(r"(?<![0-9A-Za-z])(chr\s?)?([0-9]{1,2}|X|Y|MT?)\s?[:,]\s?(\d{1,3}(?:,\d{3})+|\d+)"
                           r"(?![0-9]|,\d|\s?-\s?\d)", re.I)
# The allele pair written right after a position ("chr2:60490908 T>G", "2:60490908:T:G", "chr2:60,490,908 (T/G)"); a
# third allele (a multiallelic listing) leaves the position without a pair, as in the graph's own rule.
_SITE_PAIR = re.compile(r"\s?[(\[]?\s?(?:[:_]\s?)?([ACGT]+|-)\s?(?:->|>|/|:|\u2192)\s?([ACGT]+|-)"
                        r"(?![0-9A-Za-z])(?!\s?[>/:])", re.I)
# What may stand between an rsID and the position a paper writes with it ("rs1427407 (chr2:60,490,908 T>G)",
# "chr2:60490908, rs1427407", "rs1427407 [hg38: chr2:...]"): punctuation and an assembly name, nothing else.
_TOGETHER = re.compile(r"[^0-9A-Za-z]{0,4}(?:(?:hg|grch)\s?\d{2}[^0-9A-Za-z]{0,4})?", re.I)


@dataclass(frozen=True)
class _Mention:
    """A variant a text names: an rsID (node ("rs", "rs1427407")) or a chromosome position (node ("site", "2",
    "60490908")) with the allele pair written right after it, at start:end of the text's matching form."""
    node: tuple[str, ...]
    pair: tuple[str, str] | None
    start: int
    end: int

    def written(self) -> str:
        """The form about_variants keeps, the one the graph reads: rs<digits>, or chr<chrom>:<pos> and its ref>alt
        when an allele pair is known (alleles after an rsID are never read: papers write them on either strand)."""
        if self.node[0] == "rs":
            return self.node[1]
        if self.node[0] == "paper":
            return f"paper:{self.node[1]}:{self.node[2]}"
        return f"chr{self.node[1]}:{self.node[2]}" + (f" {self.pair[0]}>{self.pair[1]}" if self.pair else "")


def _mentions(text: str, *, entry: bool = False) -> tuple[str, list[_Mention]]:
    """The text in matching form and the variants it names, in order. `entry`: the text is an about_variants entry,
    where a position needs no "chr", seven digits or alleles to be read as one."""
    folded = normalise_for_match(text)
    found = [_Mention(("rs", f"rs{m.group(1)}"), None, m.start(), m.end()) for m in _RSID_MENTION.finditer(folded)]
    for m in _SITE_MENTION.finditer(folded):
        if not m.group(1) and "," in folded[m.end(2):m.start(3)]:
            continue  # a comma-separated count is not a chromosome position without an explicit chr prefix
        chrom, digits = m.group(2).upper(), m.group(3).replace(",", "")
        if chrom.isdigit():
            if not 1 <= int(chrom) <= 22:
                continue
            chrom = str(int(chrom))
        pair = _SITE_PAIR.match(folded, m.end())
        if not (entry or m.group(1) or len(digits) >= 7 or pair):
            continue
        found.append(_Mention(("site", "MT" if chrom == "M" else chrom, str(int(digits))),
                              (pair.group(1).upper(), pair.group(2).upper()) if pair else None,
                              m.start(), pair.end() if pair else m.end()))
    return folded, sorted(found, key=lambda x: x.start)


def _together(folded: str, found: list[_Mention], i: int) -> bool:
    """Whether a text writes mentions i and i + 1 (in text order) as one variant: an rsID and a position side by side,
    with only punctuation or an assembly name between them and no other variant within TOGETHER_CLEAR characters (a
    listing of several variants and their positions pairs nothing)."""
    first, second = found[i], found[i + 1]
    if ({first.node[0], second.node[0]} != {"rs", "site"} or first.end > second.start
            or not _TOGETHER.fullmatch(folded[first.end:second.start])):
        return False
    low, high, pair = first.start - TOGETHER_CLEAR, second.end + TOGETHER_CLEAR, (first.node, second.node)
    before = i - 1
    while before >= 0 and found[before].start > low - 2 * TOGETHER_CLEAR:    # no mention is that long
        if found[before].end > low and found[before].node not in pair:
            return False
        before -= 1
    after = i + 2
    while after < len(found) and found[after].start < high:
        if found[after].node not in pair:
            return False
        after += 1
    return True


class _VariantIndex:
    """The variants an article names (title, headings and text): which rsID and position the paper writes as one
    variant, and the allele pairs it writes at each position."""

    def __init__(self, article: Article):
        self._parent: dict[tuple[str, ...], tuple[str, ...]] = {}
        self.pairs: dict[tuple[str, ...], dict[frozenset[str], tuple[str, str]]] = {}
        self.mentions: list[_Mention] = []
        self.aliases: dict[str, dict[str, tuple[_Mention, str]]] = {}
        self.paper_names: dict[str, _Mention] = {}
        for text in [article.title, *dict.fromkeys(s.heading for s in article.sections),
                     *(s.text for s in article.sections)]:
            folded, found = _mentions(text)
            self.mentions += found
            for m in found:
                self._parent.setdefault(m.node, m.node)
                if m.pair:
                    self.pairs.setdefault(m.node, {}).setdefault(frozenset(m.pair), m.pair)
            for i in range(len(found) - 1):          # only neighbours can stand side by side: linear in the mentions
                if _together(folded, found, i):
                    self._join(found[i].node, found[i + 1].node)
            for m in found:
                # Require an explicit adjacent definition: chrN:pos C>T (C123T), or C123T (chrN:pos C>T).
                right = re.match(r"\s?\(([ACGT]\d+[ACGT])\)", folded[m.end:], re.I)
                left = re.search(r"\b([ACGT]\d+[ACGT])\s?\($", folded[:m.start], re.I)
                alias = (right or left)
                if alias and m.pair and (alias[1][0].upper(), alias[1][-1].upper()) == m.pair:
                    self.aliases.setdefault(alias[1].upper(), {})[m.written()] = (m, text)
        # A shorthand can identify a paper's experimental object without identifying a genomic case. It is
        # namespaced to this paper, never guessed from a numeric suffix or silently read as a chromosome position.
        for section in article.sections:
            if not re.search(r"promoter|non[- ]?coding|nucleotide|oligonucleotide|base.pair", section.text, re.I):
                continue
            for match in re.finditer(r"(?<![A-Za-z0-9])([ACGT]\d+[ACGT])(?![A-Za-z0-9])", section.text, re.I):
                alias = match[1].upper()
                if len(self.aliases.get(alias, {})) == 1:
                    continue
                m = _Mention(("paper", article.key, alias), (alias[0], alias[-1]), match.start(), match.end())
                self.paper_names[alias] = m
                self._parent.setdefault(m.node, m.node)
                self.mentions.append(m)

    def local_mentions(self, text: str) -> list[_Mention]:
        """Expand only unique, explicitly defined article-local names; never infer an alias from prior knowledge."""
        found = _mentions(text)[1]
        for alias, definitions in self.aliases.items():
            if len(definitions) == 1 and re.search(r"(?<![A-Za-z0-9])" + re.escape(alias) +
                                                  r"(?![A-Za-z0-9])", text, re.I):
                found.append(next(iter(definitions.values()))[0])
        for alias, mention in self.paper_names.items():
            if re.search(r"(?<![A-Za-z0-9])" + re.escape(alias) + r"(?![A-Za-z0-9])", text, re.I):
                found.append(mention)
        return found

    def group(self, node: tuple[str, ...]) -> tuple[str, ...]:
        """The one variant a node belongs to (itself when the paper writes it with no other form)."""
        parent = self._parent
        while parent.get(node, node) != node:
            parent[node] = parent[parent[node]]                 # path halving keeps the chains short
            node = parent[node]
        return node

    def _join(self, a: tuple[str, ...], b: tuple[str, ...]) -> None:
        ra, rb = self.group(a), self.group(b)
        if ra != rb:
            self._parent[max(ra, rb)] = min(ra, rb)

    def names(self, e: _Mention, found: Iterable[_Mention]) -> bool:
        """Whether mentions name the variant an entry names: the same rsID, the same position with no conflicting
        allele pair, or the other form the paper writes that variant in."""
        root = self.group(e.node)
        for m in found:
            if m.node == e.node:
                if e.pair is None or m.pair is None or frozenset(e.pair) == frozenset(m.pair):
                    return True
            elif self.group(m.node) == root:
                return True
        return False

    def only(self, node: tuple[str, ...]) -> bool:
        """Whether this is the only variant the article names (however written), with one allele pair at most at any
        position: then a passage that names no variant is about it."""
        root = self.group(node)
        return (node in self._parent and all(self.group(n) == root for n in self._parent)
                and all(len(p) <= 1 for p in self.pairs.values()))


def _variants(record: ExperimentRecord, passage: str, scope: _Scope, index: _VariantIndex,
              notes: list[str]) -> tuple[list[str], list[_Mention], list[str]]:
    """The variants the record names (about_variants) that the paper names for this experiment, as the graph reads
    them; the others are dropped with a limitation. An entry's rsID or position is kept when the quoted passage names
    it (when the passage names any variant, it must be one of them), else when the passage's section, heading or
    caption names it, else when it is the only variant the article names. A position takes the allele pair the paper
    writes there; one written with other alleles, or a bare one where the paper writes several pairs, is dropped.
    Returns the kept entries, their mentions and the reasons for each drop (for a refusal)."""
    in_passage = index.local_mentions(passage)
    in_scope = index.local_mentions(scope.text)
    kept: dict[str, _Mention] = {}
    dropped: dict[str, list[str]] = {}
    for entry in _names(record.about_variants):
        found = _mentions(entry, entry=True)[1] if len(entry) <= NAME_LIMIT else []
        if not found and len(entry) <= NAME_LIMIT:
            found = index.local_mentions(entry)
        if not found:
            dropped.setdefault("they name no rsID or chromosome position (write rs<digits>, or chr<n>:<position> "
                               "ref>alt)", []).append(_bounded(entry, 60))
        for e in found:
            label, why = e.written(), ""
            written = index.pairs.get(e.node, {}) if e.node[0] == "site" else {}
            if e.pair and written and frozenset(e.pair) not in written:
                why = (f"the article writes that position with other alleles "
                       f"({', '.join(f'{a}>{b}' for a, b in written.values())})")
            elif in_passage and not index.names(e, in_passage):
                why = (f"the passage names {', '.join(dict.fromkeys(m.written() for m in in_passage))}, and an "
                       "experiment is about the variant its passage names")
            elif not in_passage and not index.names(e, in_scope):
                if not index.names(e, index.mentions):
                    why = "the article does not name them"
                elif not index.only(e.node):
                    why = (f"they are not named where the passage is ({scope.location}, its heading or caption), and "
                           "the article names other variants")
            if not why and not e.pair and written:
                if len(written) > 1:
                    why = "the article writes several allele pairs at that position: give the pair compared"
                else:
                    e = replace(e, pair=next(iter(written.values())))
            if why:
                dropped.setdefault(why, []).append(label)
            else:
                kept.setdefault(e.written(), e)
    reasons = [f"variant(s) {', '.join(dict.fromkeys(labels))} not kept: {why}" for why, labels in dropped.items()]
    notes.extend(reasons)
    return list(kept), list(kept.values()), reasons


# --- direction ------------------------------------------------------------------------------------------------------

_UP = re.compile(r"\b(?:increas\w*|higher|elevat\w*|enhanc(?:ed|es|ing|ement)|augment\w*|up-?regulat\w*|greater|"
                 r"stronger|more|gain(?:ed|s)?|rais(?:ed|es|ing)|rose|boost\w*|creat(?:ed|es|ing)|promot(?:ed|es|ing)|"
                 r"strengthen\w*|potentiat\w*)\b", re.I)
_DOWN = re.compile(r"\b(?:decreas\w*|lower(?:ed|ing|s)?|reduc\w*|diminish\w*|attenuat\w*|abolish\w*|abrogat\w*|loss|"
                   r"lost|weaker|weaken\w*|less|fewer|down-?regulat\w*|repress(?:ed|es|ing)|suppress(?:ed|es|ing)|"
                   r"impair\w*|declin\w*|dropp?(?:ed|s)?|fell|fall(?:s|ing)?|lessen\w*|eliminat\w*)\b", re.I)
_NULL_PHRASE = re.compile(
    r"\bno (?:(?:statistically )?significant |detectable |measurable |apparent |obvious |further |appreciable )?"
    r"(?:difference|effect|change|alteration|increase|decrease|reduction|binding|activity|association|impact)|"
    r"\b(?:did|does|do|was|were|is|are|could|had|has|have) not (?:significantly |detectably |measurably )?"
    r"(?:alter|change|affect|differ|influence|increase|decrease|reduce|bind|modify|impair|enhance|show)|"
    r"\bnot (?:statistically )?significant(?:ly)?\b|\bfailed to (?:alter|change|affect|increase|decrease|reduce|bind)|"
    r"\bn\.s\.", re.I)
_NULL_WORD = re.compile(r"\b(?:unchanged|unaffected|unaltered|comparable|similar|indistinguishable|equivalent)\b", re.I)
_CLAUSE = re.compile(r";|:\s|\.\s|\b(?:whereas|while|but|although|however|unlike)\b|\b(?:in|by) contrast\b", re.I)
# The reference side of a comparison: the allele right after "than", "compared with", "relative to" or "versus" (a
# few linking words allowed), or a few words later when allele wording names it ("than constructs carrying the G
# allele"); "more than 2-fold higher for the T allele" names no reference.
_REF_WORD = r"(?:[ACGT]|(?i:ref(?:erence)?|alt(?:ernat(?:iv)?e)?))"
_REFERENCE = re.compile(rf"\b(?i:than|compared\s+(?:with|to)|relative\s+to|versus|vs\.?)\s+(?:"
                        rf"(?:(?i:that|those|from|with|in|for|at|of|on|to|the|a|an)\s+){{0,3}}({_REF_WORD})"
                        rf"(?![A-Za-z0-9])|(?:[\w-]+\s+){{0,3}}?({_REF_WORD})[- ](?i:allele|probe|construct|"
                        rf"haplotype|variant)s?\b)")
_CONVERTED_FROM = re.compile(r"(?<![A-Za-z0-9])([ACGT])(?:[- ]allele)?(?:\s?(?:>|\u2192|->)\s?|-to-| to | into )"
                             r"(?:an? |the )?[ACGT](?![A-Za-z0-9])")
_SIGN = {"increases": 1, "creates": 1, "decreases": -1, "abolishes": -1}
_FLIP: dict[str, Direction] = {"increases": "decreases", "decreases": "increases", "creates": "abolishes",
                               "abolishes": "creates"}
# What a perturbation did to what it changed: removed or blocked it (its effect is the opposite of the change seen),
# or added or raised it (its effect is the change seen).
_LOSS = re.compile(r"delet|knock-?out|knock-?down|\bsirna|\bshrna|\brnai\b|crispri|\bkrab\b|inhibit|disrupt|excis|"
                   r"ablat|silenc|repress|degron|\bdtag\b|morpholino|antisense|loss-of-function|deplet|mutat|remov|"
                   r"\bnull\b|deficien|indel|frameshift")
_GAIN = re.compile(r"over-?express|ectopic|crispra|\bvp64\b|\bvpr\b|\bp300\b|activat|gain-of-function|"
                   r"forced expression|transgen|tether")


def _clauses(passage: str, about: _About, scope: _Scope) -> list[str]:
    """The clauses of the passage that name what the record is about (its TFs or genes); all of it when none does.
    "TAL1 binding was similar, whereas GATA1 binding was threefold higher" says different things about each."""
    clauses = [c for c in _CLAUSE.split(passage) if c and c.strip()]
    names = about.tfs + about.genes
    if not names:
        return clauses
    hits = [c for c in clauses if any(_symbol_in(_symbol_forms(c), n, scope.resolver) for n in names)]
    return hits or clauses


def _signs(clauses: list[str]) -> set[int]:
    """The signs of the directional words the clauses state, a negated one ("did not increase") left out."""
    out: set[int] = set()
    for clause in clauses:
        for pattern, sign in ((_UP, 1), (_DOWN, -1)):
            if any(not _NEGATOR.search(clause[max(0, m.start() - 60):m.start()]) for m in pattern.finditer(clause)):
                out.add(sign)
    return out


def _states_null(clause: str) -> bool:
    return bool(_NULL_PHRASE.search(clause)) or any(
        not _NEGATOR.search(clause[max(0, m.start() - 60):m.start()]) for m in _NULL_WORD.finditer(clause))


def _is_reference(passage: str, allele: str) -> bool:
    """Whether the allele is the reference side of the passage's comparison ("... than the G allele", "relative to
    G", "converted T to G" for T), so the passage's direction words describe the other allele."""
    refs = {m.group(1) for m in _CONVERTED_FROM.finditer(passage)}
    for m in _REFERENCE.finditer(passage):
        word = m.group(1) or m.group(2)
        refs.add(word if len(word) == 1 else "ref" if word.casefold().startswith("ref") else "alt")
    return allele in refs


def _stated_direction(record: ExperimentRecord, passage: str, about: _About, allele: str | None, scope: _Scope,
                      notes: list[str]) -> tuple[Direction, Literal["effect", "null_in_assessed_scope"]]:
    """The record's direction checked against the passage: kept when the clauses about the record's TFs or genes
    state it (for the compared allele, read from the right side of a comparison), refused when they state the
    opposite or no change, dropped to unspecified with a limitation when they state no direction. A no-change record
    is refused unless they state an absence of effect and none of them states an effect."""
    clauses = _clauses(passage, about, scope)
    if record.direction == "no_change":
        if stated := [c for c in clauses if _signs([c]) and not _states_null(c)]:
            raise ExtractionRefused(f"the record reports no change, but the passage states an effect, not an absence "
                                    f"of effect, for what the record is about ('{_bounded(stated[0].strip(), 120)}')")
        if not any(_states_null(c) for c in clauses):
            raise ExtractionRefused("the record reports no change, but the passage does not state an absence of "
                                    "effect")
        return "no_change", "null_in_assessed_scope"
    sign = _SIGN.get(record.direction)
    if sign is None:
        return record.direction, "effect"
    signs = _signs(clauses)
    if allele and _is_reference(passage, allele):
        signs = {-s for s in signs}
    if not signs:
        if any(_states_null(c) for c in clauses):
            raise ExtractionRefused(f"the record reports '{record.direction}', but the passage states no change for "
                                    "what the record is about: record it as no_change")
        notes.append(f"the passage does not state the direction the record gives ({record.direction})")
        return "unspecified", "effect"
    if sign not in signs:
        side = f" for the {allele} allele" if allele else ""
        raise ExtractionRefused(f"the record reports '{record.direction}'{side}, but the passage states the opposite "
                                "direction: give the change the passage reports, for the compared allele")
    return record.direction, "effect"


def _effect_frame(cls: EvidenceClass, record: ExperimentRecord, passage: str, direction: Direction,
                  allele: str | None, notes: list[str]) -> Direction:
    """The direction in the frame claims use: the effect of what the experiment changed. A record states the change
    the passage reports; for a perturbation that removed or blocked an element, TF or gene (a deletion, knockdown,
    CRISPR interference, an inhibitor), the effect of that element, TF or gene is the opposite (a deletion that
    lowered BCL11A is evidence that the element raises it). Allele comparisons and binding readouts keep the stated
    direction. A perturbation that does not say whether it removed or added activity cannot be placed."""
    if direction not in _FLIP or allele is not None or record.manipulated == "allele" or \
            cls not in ("perturbation", "reporter_assay"):
        return direction
    text = _fold(record.intervention)
    loss, gain = bool(_LOSS.search(text)), bool(_GAIN.search(text))
    if not (loss or gain):
        said = _fold(passage)
        loss, gain = bool(_LOSS.search(said)), bool(_GAIN.search(said))
    if loss and not gain:
        notes.append(f"direction is the effect of what the experiment removed or blocked: its loss {direction[:-1]}d "
                     "the endpoint")
        return _FLIP[direction]
    if (gain and not loss) or cls == "reporter_assay":     # a construct reports the activity of what it carries
        return direction
    notes.append("the intervention does not say whether it removed or added activity, so the direction cannot be "
                 "placed")
    return "unspecified"


# --- data flags and context -----------------------------------------------------------------------------------------

_ALLELE_SPECIFIC = re.compile(r"allele-? ?specific|allelic (?:imbalance|ratio|bias|skew)|allele-? ?resolved")
_CONVERSION = re.compile(r"base edit|prime edit|convert|knock-?in|substitut|swap|allele replacement|"
                         r"(?<![a-z0-9])[acgt] ?(?:>|\u2192|-to-| to ) ?[acgt](?![a-z0-9])")
_DISRUPTION = re.compile(r"indel|frameshift|\bcut\b|cleav|knock-?out|delet|disrupt|excis|\bnhej\b|non-?homologous")
_IN_VIVO = re.compile(r"\bin[ -]vivo\b|\bmice\b|\brats\b|zebrafish|transgenic|\banimals\b|"
                      r"\bknock-?(?:out|in) (?:mice|mouse|rats?|animals)\b")
_GENOTYPE = re.compile(r"^[ACGT]{2}$|^[ACGT] ?[/|] ?[ACGT]$|homozyg|heterozyg", re.I)
_NULL_RELATION: dict[str, Relation] = {"binding_assay": "alters_binding", "occupancy": "occupies",
                                       "reporter_assay": "alters_regulatory_activity",
                                       "association": "associated_with_expression"}   # allele-specific expression
_PERTURBATION_NULL: dict[str, Relation] = {"reporter": "alters_regulatory_activity", "binding": "occupies",
                                           "chromatin": "alters_regulatory_activity", "expression": "regulates",
                                           "phenotype": "contributes_to_trait", "other": "affects_process"}


def _organismal(context: ContextScope | None) -> bool:
    """An organism-level context: not a cell line, primary cell or anything called cells, and either another
    species than human or a whole organism."""
    if context is None or context.biosample_kind in ("cell_line", "primary_cell"):
        return False
    if re.search(r"\bcell|\bline\b", f"{context.label} {context.biosample or ''}", re.I):
        return False
    return context.species != "human" or context.biosample_kind == "organism"


def _flags(cls: EvidenceClass, record: ExperimentRecord, passage: str, scope: _Scope, context: ContextScope | None,
           allele: str | None) -> dict[str, bool]:
    """Data flags the matrix reads, set only when the paper states them (never inferred from a context name):
    allele_specific for an allele-resolved occupancy readout (stated as allele-specific, or comparing two alleles in
    the passage); allele_targeted for a perturbation that converts the variant's allele (base or prime editing, a
    knock-in or substitution, never a cut, indel or deletion) or a reporter whose constructs differ at the compared
    allele (the section names two alleles); in_vivo for a perturbation in an organism (never a cell line)."""
    flags: dict[str, bool] = {}
    where = _fold(scope.text)
    compares = allele is not None and len(_alleles_named(scope.text)) >= 2
    if cls == "occupancy" and (_ALLELE_SPECIFIC.search(where) or (compares and len(_alleles_named(passage)) >= 2)):
        flags["allele_specific"] = True
    if cls == "perturbation":
        design = _fold(record.intervention, passage)
        if record.manipulated == "allele" and allele and _CONVERSION.search(design) and not _DISRUPTION.search(design):
            flags["allele_targeted"] = True
        if _organismal(context) and _IN_VIVO.search(f"{where} {_fold(record.intervention)}"):
            flags["in_vivo"] = True
    if cls == "reporter_assay" and record.manipulated == "allele" and compares:
        flags["allele_targeted"] = True       # constructs that differ at the alleles the section names
    return flags


def _context(record: ExperimentRecord) -> ContextScope | None:
    """The system as a context scope: the cell or tissue (normalised), the organism as species, the treatment as
    condition, and the genotype when the record states one (an allele named for a construct is not a genotype)."""
    s = record.system
    label, organism, treatment = _field(s.tissue_or_cell), _field(s.organism), _field(s.treatment)
    if not label and not organism:
        return None
    species = species_of(organism) if organism else "human"
    scope = (scope_from_label(label, source="evidence", species=species, condition=treatment or None) if label
             else ContextScope(species=species, condition=treatment or None, source="evidence"))
    genotype = _field(s.genotype_or_allele)
    return scope.model_copy(update={"genotype": genotype}) if _GENOTYPE.search(genotype) else scope


def _slug(text: str, limit: int = 60) -> str:
    return re.sub(r"[^0-9a-z]+", " ", text.casefold()).strip()[:limit].strip() or "unspecified"


# --- an extracted experiment as Evidence ------------------------------------------------------------------------------

def labelled_class(intervention: str, label: EvidenceClass | None) -> tuple[EvidenceClass | None, str, str]:
    """(the evidence class, why there is none, a note) for an experiment whose reader also named its assay family.
    Code's own reading of the intervention (assay_class) decides wherever it recognises exactly one family, so
    nothing it files without a label changes class with one. The label only fills what code cannot read: where
    the wording names no family code knows ("allele editing", "immunoprecipitation followed by genotyping"), or
    names several and the label is one of them. The note says which of the two happened."""
    named, why = assay_class(intervention)
    if label is None:
        return named, why, ""
    if named is not None:
        return named, "", ("" if named == label else
                           f"the reader labelled this {label.replace('_', ' ')}; code reads its description as "
                           f"{named.replace('_', ' ')}, which is the class kept")
    text = _fold(intervention)
    several = [cls for cls, pattern in _ASSAYS if pattern.search(text)]
    if several and label not in several:
        return None, why, ""
    return label, "", (f"the assay family ({label.replace('_', ' ')}) is the reader's label: the description of "
                       "the intervention names " + ("several" if several else "none code recognises"))


def evidence_from_experiment(record: ExperimentRecord, call: ToolCall, article: Article, *,
                             resolver: SymbolResolver | None = None,
                             label: EvidenceClass | None = None, own_figures: bool = False) -> Evidence:
    """An extracted experiment as Evidence ready for graph.add_evidence (evidence_id "", origin literature,
    retrieval_ref = the read). Refused (ExtractionRefused) when the call is not a successful read of this article,
    the record cites another article, the passage is not found verbatim, the record gives no result, the
    intervention names no single assay, what the experiment is about is missing from the paper, a record that
    compares alleles (manipulated "allele", or a compared_allele for a design that compares them) names no variant the
    paper names for it or names more than one, or the direction contradicts the passage (module docstring).
    `resolver` (the graph's HGNC SymbolResolver; the engine passes graph.resolver) lets a paper name a TF or gene by a
    previous symbol. `label` is the assay family the reader named for the experiment (reader.py); it is used only
    where code's reading of the intervention names none (labelled_class), and a record made without one is unchanged.
    `own_figures` (the reader sets it) keeps a passage that points to the article's own figure or table from being
    filed as a retelling for its wording alone (_retold).

    The record's direction is the change the passage reports, for its compared allele when it compares alleles; the
    Evidence direction is the effect of what the experiment changed (_effect_frame). Names, variants, the allele and
    the data flags are kept only as the paper states them; every drop is a limitation. The kept variants
    (about_variants) go to both the experiment record and the Evidence, which the graph checks."""
    _require_read(call)
    if not _same_article(article, call.read_article):
        raise ExtractionRefused(f"the article given ({article.key}) is not the one {call.tool_call_id} read "
                                f"({call.read_article})")
    _check_citation(record, article, call)
    quoted = _quoted(record.passage)
    if len(quoted) < PASSAGE_MIN:
        raise ExtractionRefused(f"the passage is too short to verify (under {PASSAGE_MIN} characters): quote the "
                                "sentence that states the result")
    if len(quoted) > PASSAGE_MAX:
        raise ExtractionRefused(f"the passage is longer than {PASSAGE_MAX} characters: quote only the sentence(s) "
                                "that state the result")
    found = _locate(article, quoted, record.location)
    if found is None:
        raise ExtractionRefused(f"the passage is not in {article.key} as {call.tool_call_id} read it (compared as "
                                "whole words after folding whitespace, quotes, dashes and ligatures): quote one "
                                "contiguous passage exactly, without ellipses, and keep a negation that governs it")
    section, passage = found
    result = _field(record.result, RESULT_LIMIT)
    if not result:
        raise ExtractionRefused("the record states no result")
    assay, why, label_note = labelled_class(record.intervention, label)
    retold = _retold(section, passage, own_figures)
    review = article.is_review or bool(_REVIEW.search(record.publication_type)) or retold is not None
    if assay is None and not review:
        raise ExtractionRefused(why)
    cls: EvidenceClass = "review" if review or assay is None else assay
    endpoint = _endpoint_category(record.endpoint)
    notes: list[str] = [x for x in [_field(record.scope_does_not_test), label_note] if x]
    if own_figures and retold is None and _RETELLING.search(passage):
        notes.append("the passage cites earlier work and points to this article's own figure or table: read as the "
                     "article's result")
    if review:
        notes.append("a retelling (" + (retold or "a review article") + "): context only, never a second "
                     "experimental observation")
    if article.access == "abstract_only":
        notes.append("abstract only: methods, controls and full results were not read")
    if record.authors_hypothesis_vs_result != "result":
        notes.append("the passage states the authors' hypothesis, not a result" if
                     record.authors_hypothesis_vs_result == "hypothesis" else
                     "the passage mixes a result with the authors' interpretation")
    scope = _Scope.of(article, section, resolver)
    about = _about(record, cls, passage, scope, notes)
    index = _VariantIndex(article)
    variants, named, unnamed = _variants(record, passage, scope, index, notes)
    aliases = {alias: next(iter(defs.values())) for alias, defs in index.aliases.items() if len(defs) == 1 and
               re.search(r"(?<![A-Za-z0-9])" + re.escape(alias) + r"(?![A-Za-z0-9])", scope.text, re.I) and
               any(index.names(m, named) for m, _ in defs.values())}
    # A mutant-versus-wild-type result may use a defined mutation name rather than repeat its base letters.
    alias_alts = {m.pair[1] for m, _ in aliases.values() if m.pair} if (
        re.search(r"wild[- ]?type|reference", scope.text, re.I) and
        re.search(r"mutant|mutation", scope.text, re.I)) else set()
    if re.search(r"wild[- ]?type|reference", scope.text, re.I) and re.search(r"mutant|mutation", scope.text, re.I):
        alias_alts |= {m.pair[1] for m in named if m.node[0] == "paper" and m.pair}
    allele, design = _compared(record, cls, passage, scope, notes, alias_alts)
    if cls != "review" and design and (record.manipulated == "allele" or clean_text(record.compared_allele)):
        if not variants:
            raise ExtractionRefused(
                "the record compares alleles but names no variant the paper names for this experiment "
                "(about_variants): name the variant whose alleles were compared, by its rsID or chromosome position "
                "as the passage writes it (or, when the passage names none, as its section, heading or caption does)"
                + "".join(f"; {x}" for x in unnamed))
        if len({index.group(m.node) for m in named}) > 1:
            raise ExtractionRefused(f"an allele comparison is about one variant's alleles, but the record names "
                                    f"{', '.join(variants)}: give one experiment per variant, naming the one whose "
                                    "alleles the passage compares")
    if cls != "review" and (limit := _allele_scope(record)):
        notes.append(limit)
    stated, kind = _stated_direction(record, passage, about, allele, scope, notes)
    direction = stated
    assessed: Relation | None = None
    if kind == "null_in_assessed_scope":
        allele = None
        assessed = (_PERTURBATION_NULL[endpoint] if assay == "perturbation" else
                    "alters_binding" if assay == "occupancy" and _ALLELE_SPECIFIC.search(_fold(scope.text))
                    else _NULL_RELATION.get(assay or "", "other"))
    elif design and allele is None and direction in _SIGN:
        notes.append("an allele comparison's direction needs the allele it refers to (compared_allele, named in the "
                     "passage), so it is not kept")
        direction = "unspecified"
    else:
        direction = _effect_frame(cls, record, passage, direction, allele, notes)
    context = _context(record)
    flags = {} if review else _flags(cls, record, passage, scope, context, allele)
    paper_names = [m.node[2] for m in named if m.node[0] == "paper"]
    if paper_names:
        flags.update(paper_variant_names=paper_names, variant_identity_status="unresolved")
        notes.append("Mutation shorthand retained in this paper's scope; case identity is unresolved, not different.")
    if cls == "reporter_assay" and record.manipulated == "allele" and allele in alias_alts:
        flags["allele_targeted"] = True
    if aliases:
        flags["paper_variant_aliases"] = {alias: {"variant": m.written(),
            "definition_locations": [s.location for s in article.sections if s.text == definition]}
            for alias, (m, definition) in aliases.items()}
    builds = { {"hg18": "GRCh36", "hg19": "GRCh37", "hg38": "GRCh38"}.get(b.casefold(), b.upper().replace("GRCH", "GRCh"))
              for b in re.findall(r"\b(?:GRCh3[678]|hg(?:18|19|38))\b",
                                  " ".join(s.text for s in article.sections), re.I)}
    if builds:
        flags["paper_assembly"] = next(iter(builds)) if len(builds) == 1 else "ambiguous"
    article_id = article.source_ids()[0]
    system = _slug(scope_key(context) or record.system.organism)
    s = record.system
    experiment = record.model_copy(update={
        "source_id": article_id, "pmcid": article.pmcid, "doi": article.doi,
        "publication_type": _field(article.publication_type or record.publication_type),
        "access": article.access, "location": section.location, "passage": passage, "direction": stated,
        "result": result, "intervention": _field(record.intervention), "endpoint": _field(record.endpoint),
        "comparator": _field(record.comparator), "scope_supports": _field(record.scope_supports),
        "scope_does_not_test": _field(record.scope_does_not_test),
        "system": ExperimentSystem(organism=_field(s.organism), tissue_or_cell=_field(s.tissue_or_cell),
                                   treatment=_field(s.treatment), genotype_or_allele=_field(s.genotype_or_allele)),
        "about_tfs": about.tfs, "about_genes": about.genes, "about_elements": about.elements,
        "about_traits": about.traits, "about_variants": variants, "compared_allele": allele})
    return Evidence(
        evidence_class=cls, source_ids=article.source_ids(),
        raw_artifact_ref=f"{call.raw_result_path}#{section.location}" if call.raw_result_path else None,
        retrieval_ref=call.tool_call_id, observed_result=result,
        data=flags,
        allele=allele, direction=direction, context=context, about_tfs=about.tfs, about_genes=about.genes,
        about_elements=about.elements, about_traits=about.traits, about_variants=variants,
        independence_group=f"{article_id}#{cls}/{endpoint}/{system}", origin="literature",
        access=article.access, experiment=experiment,
        limitations=list(dict.fromkeys(_bounded(x, FIELD_LIMIT) for x in notes)), result_kind=kind,
        assessed_relation=assessed)


# --- the public export (SPEC 13.11) ---------------------------------------------------------------------------------

REMOVED = "[removed in the public export]"


def _cut(text: str, limit: int = PUBLIC_PASSAGE_LIMIT) -> str:
    """A verbatim prefix of at most `limit` characters, ending at a word boundary when one is near: nothing is
    added, so a cut passage is still source text."""
    if len(text) <= limit:
        return text
    head = text[:limit]
    space = head.rfind(" ")
    return (head[:space] if space >= limit // 2 else head).rstrip()


def _cut_strings(value: Any) -> Any:
    """Every string in a JSON value cut to PUBLIC_PASSAGE_LIMIT characters (keys and shorter strings unchanged), so
    no free-text field can carry article text into a public export."""
    if isinstance(value, dict):
        return {k: _cut_strings(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_cut_strings(v) for v in value]
    return _cut(value) if isinstance(value, str) else value


def public_evidence(evidence: dict[str, Any]) -> dict[str, Any]:
    """An Evidence (as JSON) for a public export: a literature item keeps its verified passage, cut verbatim to
    PUBLIC_PASSAGE_LIMIT characters (verified passages never exceed it), and every other string is cut to the same
    bound (extraction already bounds the extractor's fields; this also covers older runs)."""
    out = copy.deepcopy(evidence)
    experiment = out.get("experiment")
    if out.get("origin") == "literature" and isinstance(experiment, dict):
        experiment["passage"] = _cut(str(experiment.get("passage") or ""))
    return _cut_strings(out)


def public_tool_call(call: dict[str, Any]) -> dict[str, Any]:
    """A ToolCall (as JSON) for a public export: a read's passages and a search's abstracts are dropped (marked
    text_dropped / abstract_dropped); identifiers, titles, routes and the outline stay."""
    out = copy.deepcopy(call)
    for obs in out.get("observations") or []:
        if out.get("tool_name") == READ_TOOL and obs.get("kind") == "passage":
            obs["text"], obs["text_dropped"] = "", True
        elif out.get("tool_name") == SEARCH_TOOL and "abstract" in obs:
            obs["abstract"], obs["abstract_dropped"] = "", True
    return out


def public_raw(call: dict[str, Any], raw: bytes, evidence: Iterable[dict[str, Any]]) -> bytes:
    """The raw file of a call for a public export. A literature read's article keeps its metadata and only the
    verified passages that evidence from this call quotes (each at its location, bounded); a search keeps its
    records without abstracts; any other tool's raw file is returned unchanged."""
    name, tid = call.get("tool_name"), call.get("tool_call_id")
    if name == READ_TOOL:
        try:
            article = Article.model_validate_json(raw)
        except ValidationError:                  # not a parsed article: keep nothing of it
            return json.dumps({"text_dropped": True, "tool_call_id": tid}, sort_keys=True).encode()
        kept: dict[tuple[str, str], ArticleSection] = {}
        for ev in evidence:
            experiment = ev.get("experiment") or {}
            if ev.get("origin") != "literature" or ev.get("retrieval_ref") != tid or not experiment.get("passage"):
                continue
            location = str(experiment.get("location") or "")
            section = article.section(location)
            text = _cut(str(experiment["passage"]))
            kept.setdefault((location, text), ArticleSection(location=location, text=text,
                                                             heading=section.heading if section else ""))
        stub = article.model_copy(update={"sections": list(kept.values())})
        return json.dumps(stub.model_dump(mode="json"), sort_keys=True, ensure_ascii=False, indent=1).encode()
    if name == SEARCH_TOOL:
        try:
            data = json.loads(raw)
            records = list(data.get("records") or [])
        except (ValueError, AttributeError):     # not a search result: keep nothing of it
            return json.dumps({"text_dropped": True, "tool_call_id": tid}, sort_keys=True).encode()
        records += data.get("original_records") or []
        records += (data.get("discovery") or {}).get("records") or []
        for record in records:
            record["abstract"], record["abstract_dropped"] = "", True
            if "abstractText" in record:
                record["abstractText"] = ""
        return json.dumps(data, sort_keys=True, ensure_ascii=False, indent=1).encode()
    return raw


def public_details(value: Any) -> Any:
    """Event details for a public export: every quoted passage removed (an accepted one lives on in its Evidence; a
    refused extraction's passage was never verified) and any other long string cut to PUBLIC_PASSAGE_LIMIT."""
    if isinstance(value, dict):
        return {k: REMOVED if k == "passage" and v else public_details(v) for k, v in value.items()}
    if isinstance(value, list):
        return [public_details(v) for v in value]
    return _cut(value) if isinstance(value, str) else value


def public_graph_state(state: dict[str, Any]) -> dict[str, Any]:
    """graph.json content (ClaimGraph.to_state() as JSON) under the excerpt policy: tool calls and evidence as
    public_tool_call / public_evidence give them, event details as public_details gives them, and every string of
    the claims, hypotheses, questions, comparisons and result (rationales, answers, summaries: agent text that could
    quote a paper) cut to PUBLIC_PASSAGE_LIMIT."""
    out = copy.deepcopy(state)
    out["evidence"] = {k: public_evidence(v) for k, v in (out.get("evidence") or {}).items()}
    out["tool_calls"] = {k: public_tool_call(v) for k, v in (out.get("tool_calls") or {}).items()}
    out["events"] = [{**e, "details": public_details(e.get("details") or {})} for e in out.get("events") or []]
    for part in ("claims", "hypotheses", "questions", "comparisons", "result"):
        if out.get(part) is not None:
            out[part] = _cut_strings(out[part])
    return out
