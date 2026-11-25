"""ClaimGraph: the one shared scientific record of a run, changed only through validated mutations (SPEC 3, 13.6-13.8).

Agents never edit state. Each change goes through a method here that checks it and either applies it, appending a
DecisionEvent, or raises GraphRefusal with a reason an agent can act on. A refused mutation leaves the graph exactly
as it was (every public mutation is atomic, whatever exception stops it). apply_updates() runs a batch of proposed
changes one by one, records a refuse_update event for each refusal, then propagates dependencies once.

What the checks protect:
- identity: evidence can only support or contradict a claim about the TFs, genes, elements and traits it names
  (Evidence.about_*), whatever kind the proposer gave an entity; a claim about what an element does (an element as
  its subject) needs evidence that names that element, so a TF knockdown that changed a gene never tests an enhancer;
  a binding claim must name the bound factor as a TF, TF group or complex; a group's members are fixed when it is
  created (from the QBiC-SELEX group registry when one is given); a link to a group's claim names the member its
  evidence is about, except the group's own QBiC-SELEX inventory item when its gate-passing models agree, which is
  about the group as a whole; supersession never copies links, so TF-A evidence never moves to TF-B silently;
- the case variant: one rule (variant_mention) reads every text that may name a variant (labels, canonical ids,
  about_variants and about_elements entries): the case variant is named by its rsIDs, its chrom:pos and any allele
  pair written there; a variant reference is the case variant unless its label names another variant, and its
  canonical id, when it names a variant, must name the case; an rsID that a code tool reports at the case's exact
  coordinates and alleles is recorded as the case variant's own (add_variant_alias), and an element that a code tool
  places over the variant is recorded as containing it (add_variant_element), so evidence naming "the enhancer
  containing <rsID>" is about that element. The request itself is never changed: inferred diseases and contexts are
  stored as inferred candidates, never as input;
- which variant: evidence naming only other variants (about_variants) never supports or contradicts a claim about the
  case variant, nor evidence naming none of a claim's other variants a claim about them; evidence that compares
  alleles must name the variant whose alleles it compared before it bears on an allelic claim; a TF or gene
  perturbation never tests what the variant's alleles do, and an experiment that does not compare them (a region
  deletion, a single-allele assay) is at most indirect for a claim that they differ;
- allele frame and direction: a claim about the case variant names its effect allele (alt unless stated) and an
  observation's direction is read for the allele it names, so "ref binds more" cannot support "alt binds more"; an
  observed effect contradicts only by a different direction (an absence of effect is a measured null), so agreement
  can never be used as a contradiction;
- context: applicability is computed by code (context_match) and a proposer may only weaken it, by naming a weaker
  match (proxy or different); a proposed "unknown" states no judgement and leaves code's value, except on a
  contradicts link, where it withholds the contradiction until a link confirms the scope; a different context,
  or an allele-resolved readout from a context homozygous at the variant, is stored as context only; a lost context is
  unknown, never exact, for cell-based evidence and for nulls;
- evidence class: only a DIRECT class (schemas.DIRECT) makes a claim supported or contradicted in scope; an INDIRECT
  class (QBiC-SELEX prediction, association, L2G) leaves it unresolved and shows as its "predicted"/"associated" basis;
  direct evidence on both sides makes a claim contested, never supported or contradicted;
- concurrency: every link and every assessment bumps the claim's version, so an assessment based on an older reading
  is stale; a held assessment that its current links no longer meet is reset to unresolved by code;
- missingness: empty retrievals create no Evidence, and a measured null contradicts only in an exact, matched scope;
- vetoes: expressed_in and occupies claims can never be required, so expression and ChIP can defer a TF hypothesis
  but never reject it; rejection needs a contradicted required claim, and it happens when the contradiction is
  assessed, so no later change in the same batch can repair it away; a replacement hypothesis must keep every
  required claim of the hypothesis it retires; a rejection is final, except that code reinstates (as deferred, once)
  a hypothesis whose rejecting contradiction was later withdrawn, so a misread contradiction cannot eliminate a
  story and a story cannot oscillate;
- dependencies flag downstream claims and hypothesis paths but never change an assessment;
- anti-repeat: a hypothesis whose structural signature (built from normalised symbols, so a canonical id added later
  cannot change it) matches a rejected one is refused.

IDs come from counters (entities N, claims C, evidence E, tool calls T, hypotheses H, questions Q, events D,
comparisons P), so the same sequence of calls always yields the same graph. graph.version counts committed mutations;
events that only record (refusals, stops) leave it unchanged.
"""

import copy
import csv
import json
import math
import re
from collections.abc import Iterable, Iterator, Mapping, Sequence
from contextlib import contextmanager
from functools import lru_cache, wraps
from pathlib import Path
from typing import Any, Literal, get_args

from pydantic import Field

from . import ENGINE_VERSION
from .context_match import link_applicability, normalise_scope, scope_key
from .schemas import (
    ALLELIC_RELATIONS,
    ASSESSORS,
    ASSOCIATED_BASIS,
    CLASS_ORDER,
    CONTEXT_FREE_CLASSES,
    DIRECT,
    INVESTIGATORS,
    PREDICTED_BASIS,
    REQUIRABLE,
    SPECIFIC_DIRECTIONS,
    Applicability,
    Assessment,
    BudgetSnapshot,
    Case,
    Claim,
    ClaimDisplay,
    ClaimHistoryEntry,
    ContextScope,
    DecisionEvent,
    Direction,
    Disposition,
    Entity,
    EntityKind,
    EventAction,
    Evidence,
    EvidenceLink,
    Hypothesis,
    InferredCandidate,
    LinkStrength,
    MechanismClass,
    PairComparison,
    PathStatus,
    Question,
    QuestionStatus,
    Relation,
    Role,
    RunResult,
    Stance,
    ToolCall,
    V9Model,
    evidence_strength,
)
from .traits import ontology_id, trait_identity, trait_key

PREFIXES = ("N", "C", "E", "T", "H", "Q", "D", "P")
SYMBOL_KINDS = frozenset({"gene", "tf", "tf_group", "transcript"})     # labels kept in upper case
LABEL_KEYED = frozenset({"gene", "tf", "transcript"})                  # one entity per normalised symbol
HGNC_KINDS = frozenset({"gene", "tf"})
MEMBER_KINDS = frozenset({"tf_group", "complex", "binding_event"})     # entities whose members are TFs
BINDER_KINDS = frozenset({"tf", "tf_group", "complex"})                # what a binding claim can name as the factor
BINDING_RELATIONS = frozenset({"occupies", "alters_binding"})
TF_IDENTITY_RELATIONS = frozenset({"occupies", "alters_binding", "expressed_in"})   # TFs matched in about_tfs only
FLIP: dict[str, Direction] = {"increases": "decreases", "decreases": "increases", "creates": "abolishes",
                              "abolishes": "creates"}
APPLICABILITY_RANK = {"exact": 3, "proxy": 2, "unknown": 1, "different": 0}
EVIDENCE_FROM = ("records_found", "incomplete")          # retrieval statuses that may carry Evidence
# Dispositions a hypothesis never leaves, with one exception: reinstate() returns a hypothesis that code rejected for a
# contradicted required claim to "deferred" once that contradiction is withdrawn (reassessed, or its link replaced),
# and only once. Every other path (set_disposition, revisions, apply_updates) treats both as final.
FINAL = ("rejected", "superseded")
REJECTION_RULE = "contradicted_required_claim"           # details["rule"] of the rejections reinstate() can undo
RULE_REASON = re.compile(r"required claim (C\d+(?:, C\d+)*) contradicted in scope")   # the same, in older graphs
DISPOSITION_ACTION: dict[str, EventAction] = {"active": "activate", "deferred": "defer", "rejected": "reject",
                                              "leading": "decide", "tied": "decide",
                                              "superseded": "revise_hypothesis"}
INVESTIGATOR_KINDS = frozenset({"attach_evidence", "assess", "new_claim", "supersede_claim"})
KEY_PREFIX = "key:"
MAX_REASON = 600
DOI_URLS = ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "http://dx.doi.org/")
ARTICLE_PREFIX = re.compile(r"(pmcid|pmid|doi)\s*[:\s]\s*")             # "PMID:1", "pmcid: PMC2", "DOI 10.1/x"
RSID = re.compile(r"rs\d+", re.I)
STANDARD_CHROM = r"[0-9]{1,2}|X|Y|MT?"
POSITION = re.compile(rf"(?<![0-9A-Za-z])(?:chr)?({STANDARD_CHROM}):(\d+)", re.I)   # "chr2:60490908", "2:60490908"
# An allele pair written right after a position: "chr2:60490908:T:G", "2:60490908 T>G", "chr2:60490908_T/G". A third
# allele ("T/C/G", a multiallelic listing) or anything else after the pair leaves the position without alleles, so a
# listing never reads as another variant.
ALLELE_PAIR = re.compile(r"[:_\s]*([ACGT]+|-)\s*[>/:]\s*([ACGT]+|-)(?![0-9A-Za-z])(?!\s*[>/:])", re.I)
CANDIDATE_ROLES = frozenset({"code", "coordinator"})                    # who may record an inferred candidate
# Relations whose claims say that the variant's alleles differ in what they do at the site (C3-2): only an
# experiment that compares (or edits) the alleles tests them directly. causal_at_locus has its allele_targeted
# qualifier, and associated_with_expression is established by association statistics, not experiments.
ALLELE_COMPARED_RELATIONS = frozenset({"alters_binding", "alters_regulatory_activity", "alters_rna"})
FACTOR_PERTURBATIONS = frozenset({"tf", "gene"})          # ExperimentRecord.manipulated values that change a factor


class GraphRefusal(Exception):
    """A mutation the graph will not apply. `reason` is written for the agent that proposed it."""

    def __init__(self, reason: str):
        super().__init__(reason)
        self.reason = reason


# --- inputs to the graph (internal; roles.py converts the strict LLM models into these) ------------------------------

class EntityRef(V9Model):
    """An entity named in a claim: an existing entity_id, or a kind and label (deduplicated by the graph)."""
    kind: EntityKind
    label: str = ""
    canonical_id: str | None = None
    entity_id: str | None = None
    members: list[str] = Field(default_factory=list)       # tf_group, complex, binding_event: member TF symbols
    qualifiers: dict[str, str] = Field(default_factory=dict)


class ClaimDraft(V9Model):
    subjects: list[EntityRef]
    relation: Relation
    objects: list[EntityRef]
    direction: Direction = "unspecified"
    effect_allele: str | None = None      # claims naming a variant: the allele the direction is for (default alt)
    allele_scope: str | None = None
    context: ContextScope | None = None
    mechanism_class: MechanismClass = "other"
    assertion_text: str = ""
    dependencies: list[str] = Field(default_factory=list)  # claim ids (or key: references inside apply_updates)
    limitations: list[str] = Field(default_factory=list)


class HypothesisDraft(V9Model):
    title: str
    summary: str = ""
    claim_ids: list[str] = Field(default_factory=list)
    required_claim_ids: list[str] = Field(default_factory=list)   # added to claim_ids when missing there
    assumptions: list[str] = Field(default_factory=list)
    context: ContextScope | None = None
    endpoint: str = "molecular"
    mechanism_class: MechanismClass = "other"
    disposition: Literal["active", "deferred"] = "active"
    disposition_reason: str = ""
    revisit_trigger: str | None = None
    origin: Literal["initial", "regenerated", "evidence_led"] = "initial"
    replaces: str | None = None
    member_alternatives: list[str] = Field(default_factory=list)
    missing_links: list[str] = Field(default_factory=list)
    reason_for_inclusion: str = ""


class HypothesisChanges(V9Model):
    """A revision: None leaves a field as it is. replace_claims swaps a claim in place (required stays required)."""
    title: str | None = None
    summary: str | None = None
    assumptions: list[str] | None = None
    context: ContextScope | None = None
    endpoint: str | None = None
    mechanism_class: MechanismClass | None = None
    member_alternatives: list[str] | None = None
    missing_links: list[str] | None = None
    reason_for_inclusion: str | None = None
    add_claim_ids: list[str] = Field(default_factory=list)
    add_required_claim_ids: list[str] = Field(default_factory=list)
    remove_claim_ids: list[str] = Field(default_factory=list)
    replace_claims: dict[str, str] = Field(default_factory=dict)


UpdateKind = Literal["attach_evidence", "assess", "new_claim", "supersede_claim", "add_claim_to_hypothesis",
                     "replace_required_claim", "revise_hypothesis", "set_disposition", "add_hypothesis"]


class GraphUpdate(V9Model):
    """One proposed change, as apply_updates() takes it. Which fields a kind needs:

    attach_evidence          claim_id, evidence_id, stance [, applicability, rationale, limitations,
                             suggested_assessment + base_version (the claim version the proposer read)]
    assess                   claim_id, assessment, base_version, rationale
    new_claim                claim [, hypothesis_id, required, reason]   (hypothesis fields: coordinator only)
    supersede_claim          claim_id (old), claim (the replacement), reason [, hypothesis_ids (coordinator only)]
    add_claim_to_hypothesis  hypothesis_id, claim_id [, required, reason]
    replace_required_claim   hypothesis_id, claim_id (old), new_claim_id, reason
    revise_hypothesis        hypothesis_id, changes, reason
    set_disposition          hypothesis_id, disposition, reason [, revisit_trigger]
    add_hypothesis           hypothesis

    `key` names what a new_claim, supersede_claim or add_hypothesis creates; a later update in the same batch can
    refer to it as "key:<name>" in any id field (and in draft dependencies and claim lists)."""
    kind: UpdateKind
    key: str | None = None
    claim_id: str | None = None
    evidence_id: str | None = None
    hypothesis_id: str | None = None
    new_claim_id: str | None = None
    hypothesis_ids: list[str] = Field(default_factory=list)
    stance: Stance | None = None
    applicability: Applicability | None = None
    rationale: str = ""
    limitations: list[str] = Field(default_factory=list)
    assessment: Assessment | None = None
    suggested_assessment: Assessment | None = None
    base_version: int | None = None
    claim: ClaimDraft | None = None
    required: bool = False
    hypothesis: HypothesisDraft | None = None
    changes: HypothesisChanges | None = None
    disposition: Disposition | None = None
    reason: str = ""
    revisit_trigger: str | None = None


class UpdateOutcome(V9Model):
    index: int                                   # position in the batch
    kind: str
    accepted: bool
    ids: list[str] = Field(default_factory=list)          # what the update created or acted on (first: the main one)
    event_ids: list[str] = Field(default_factory=list)
    reason: str = ""                                      # why it was refused
    note: str = ""                                        # e.g. "duplicate of C3", "applicability corrected"


class ModelUsage(V9Model):
    calls: int = 0
    cost_usd: float = 0.0


class GraphState(V9Model):
    """Everything graph.json holds; ClaimGraph.to_json/from_json round-trip it losslessly. Fields added later have
    defaults, so an older graph.json still loads (with nothing recorded for them)."""
    engine_version: str = ENGINE_VERSION
    case: Case
    version: int = 0
    counters: dict[str, int]
    model_usage: ModelUsage = Field(default_factory=ModelUsage)
    variant_aliases: dict[str, str] = Field(default_factory=dict)    # lower-case rsID -> the code tool call reporting it
    variant_elements: dict[str, str] = Field(default_factory=dict)   # element id -> the code tool call placing it
    entities: dict[str, Entity] = Field(default_factory=dict)
    claims: dict[str, Claim] = Field(default_factory=dict)
    evidence: dict[str, Evidence] = Field(default_factory=dict)
    hypotheses: dict[str, Hypothesis] = Field(default_factory=dict)
    questions: dict[str, Question] = Field(default_factory=dict)
    tool_calls: dict[str, ToolCall] = Field(default_factory=dict)
    comparisons: dict[str, PairComparison] = Field(default_factory=dict)
    events: list[DecisionEvent] = Field(default_factory=list)
    result: RunResult | None = None

    # Derived views: recomputed from claims on export, never trusted as evidence when loading.
    claim_refinements: list[dict[str, Any]] = Field(default_factory=list)
    hypothesis_families: list[dict[str, Any]] = Field(default_factory=list)


GREEK_LETTERS: dict[str, str] = {
    "α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon", "ζ": "zeta", "η": "eta", "θ": "theta",
    "ι": "iota", "κ": "kappa", "λ": "lambda", "μ": "mu", "µ": "mu", "σ": "sigma", "τ": "tau", "ω": "omega"}
# Spelt-out letters long enough not to be part of another word ("eta" is inside "beta", "mu" inside "immune").
_GREEK_WORD = re.compile("alpha|beta|gamma|delta|epsilon|kappa|lambda|sigma|omega")


def greek_key(name: str) -> str | None:
    """A protein name that carries a Greek letter, in one spelling: lower case, the letter spelt out, and nothing but
    letters and digits ("AP-2α", "AP-2alpha" and "AP2-alpha" are all "ap2alpha"). None for a name with no Greek
    letter, written or spelt out: such a name is not looked up among aliases at all."""
    text = "".join(GREEK_LETTERS.get(ch, ch) for ch in " ".join(name.split()).casefold())
    key = re.sub(r"[^a-z0-9]", "", text)
    return key if key and _GREEK_WORD.search(key) else None


class SymbolResolver:
    """HGNC symbol normalisation: approved symbols, plus previous symbols that point to one approved gene. Alias
    symbols are left out on purpose: many are shared between genes, and a wrong merge would move evidence.

    One kind of alias is read, since the second version of the fill: a protein name with a Greek letter (AP-2α,
    C/EBPβ, PPARγ). Articles name a protein that way and never a gene, so such a name was no approved symbol, the
    record stayed under a TF nobody else names, and it never met the candidate it was about. The letter says which
    paralogue is meant, which is what makes the name safe to resolve where a bare family name (AP-2) is not. It
    resolves only when exactly one approved gene lists it among its aliases (greek_key: hyphens, slashes and spaces
    aside) and no other gene's symbol reads the same."""

    def __init__(self, symbols: dict[str, tuple[str, str]], formerly: Mapping[str, Sequence[str]] | None = None,
                 greek: Mapping[str, tuple[str, str]] | None = None):
        self._symbols = symbols                  # upper-case symbol -> (approved symbol, HGNC id)
        self._formerly = {k.upper(): tuple(v) for k, v in (formerly or {}).items()}
        self._greek = dict(greek or {})          # greek_key of an alias -> (approved symbol, HGNC id)

    @classmethod
    def from_hgnc(cls, path: str | Path) -> "SymbolResolver":
        """Read hgnc_complete_set.txt (tab-separated, read only)."""
        approved: dict[str, tuple[str, str]] = {}
        previous: dict[str, set[tuple[str, str]]] = {}
        genes: dict[str, set[str]] = {}          # a previous symbol -> the genes (not pseudogenes) that had it
        aliases: dict[str, set[tuple[str, str]]] = {}     # greek_key of an alias -> the genes that list it
        with open(path, newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                if row.get("status") != "Approved":
                    continue
                hit = (row["symbol"].strip(), row["hgnc_id"].strip())
                approved[hit[0].upper()] = hit
                for prev in (row.get("prev_symbol") or "").split("|"):
                    if prev.strip():
                        previous.setdefault(prev.strip().upper(), set()).add(hit)
                        if (row.get("locus_group") or "").strip() != "pseudogene":
                            genes.setdefault(prev.strip().upper(), set()).add(hit[0])
                for alias in (row.get("alias_symbol") or "").split("|"):
                    if key := greek_key(alias):
                        aliases.setdefault(key, set()).add(hit)
        table = {k: next(iter(v)) for k, v in previous.items() if len(v) == 1 and k not in approved}
        table.update(approved)
        formerly = {k: sorted(v - {approved[k][0]}) for k, v in genes.items() if k in approved}
        # a Greek-letter alias of exactly one gene, unless another gene's own symbol reads the same
        spelt = {re.sub(r"[^a-z0-9]", "", k.casefold()): v[0] for k, v in table.items()}
        greek = {k: next(iter(v)) for k, v in aliases.items()
                 if len(v) == 1 and spelt.get(k, next(iter(v))[0]) == next(iter(v))[0]}
        return cls(table, {k: v for k, v in formerly.items() if v}, greek)

    def __call__(self, symbol: str) -> tuple[str, str] | None:
        found = self._symbols.get(" ".join(symbol.split()).upper())
        if found is None and self._greek and (key := greek_key(symbol)):
            found = self._greek.get(key)
        return found

    def formerly(self, symbol: str) -> tuple[str, ...]:
        """The other genes (pseudogenes aside) that once had this approved symbol: TCF4 was the symbol of TCF7L2 and
        TCF3 that of TCF7L1. The graph reads such a name as today's gene; in an article it can mean either, so a
        caller that files what an article says must not take it for one of them."""
        return self._formerly.get(" ".join(symbol.split()).upper(), ())


class GroupRegistry:
    """QBiC-SELEX model-sharing groups: group id -> member TF symbols. A tf_group entity whose canonical id is a
    registry group takes its members from here when it is created, so no claim draft can add or drop a member."""

    def __init__(self, groups: Mapping[str, Sequence[str]]):
        self._groups = {_text(gid).upper(): tuple(dict.fromkeys(_text(m).upper() for m in members if _text(m)))
                        for gid, members in groups.items()}

    @classmethod
    def from_groups_json(cls, path: str | Path) -> "GroupRegistry":
        """Read cache/groups.json directly (read only; never through qbic Registry.groups(), which can rewrite it)."""
        data = json.loads(Path(path).read_text())
        return cls({g["id"]: g.get("tfs") or [] for g in data.get("groups") or []})

    def members(self, group_id: str | None) -> tuple[str, ...] | None:
        """The member symbols of a registry group, or None when the id is not a registry group."""
        return self._groups.get(_text(group_id).upper()) if group_id else None


def _text(value: str | None) -> str:
    return " ".join(str(value or "").split())


def _same(a: str, b: str) -> bool:
    return _text(a).casefold() == _text(b).casefold()


def _num(entity_id: str) -> int:
    return int(entity_id[1:])


def _chrom(value: str) -> str:
    """A chromosome name for comparison: "chr2" and "2" are 2; "chrM", "M" and "MT" are MT."""
    name = _text(value).upper()
    name = name[3:] if name.startswith("CHR") else name
    return "MT" if name == "M" else name


@lru_cache(maxsize=32)
def _position_pattern(chrom: str) -> re.Pattern[str]:
    """POSITION, plus the case's own chromosome name when it is not a standard one (a synthetic case's "SYN"), so a
    case on any chromosome can be named by its chrom:pos."""
    own = _chrom(chrom)
    if not own or re.fullmatch(STANDARD_CHROM, own, re.I):
        return POSITION
    return re.compile(rf"(?<![0-9A-Za-z])(?:chr)?({re.escape(own)}|{STANDARD_CHROM}):(\d+)", re.I)


def _positions(text: str, chrom: str) -> list[tuple[str, int, frozenset[str] | None]]:
    """Every chrom:pos a text names (positions read on the case's chromosome naming as well), each with the allele
    pair written right after it as a set, or None when no pair is written."""
    out = []
    for m in _position_pattern(chrom).finditer(text):
        pair = ALLELE_PAIR.match(text, m.end())
        alleles = frozenset((pair.group(1).upper(), pair.group(2).upper())) if pair else None
        out.append((_chrom(m.group(1)), int(m.group(2)), alleles))
    return out


def _ident(value: str | None) -> str:
    """An element or trait name for identity matching: case, spacing and punctuation ignored."""
    return re.sub(r"[^0-9a-z]+", " ", _text(value).casefold()).strip()


def article_key(value: str | None, *, pmcid: bool = False) -> str | None:
    """One article identifier in one form, so an article compares equal however a source or an agent wrote its id:
    a leading "PMID:", "PMCID:" or "DOI:" (any case) or a doi.org URL is dropped; a PMCID becomes PMC<digits>, a DOI
    lower case, a PMID its digits. Bare digits are a PMID, except where the value is known to be a PMCID (`pmcid`: a
    pmcid parameter, or a "PMCID:" prefix). Any other text is kept case-folded, so it still matches itself. None for an
    empty value. The tool runner (full-text budget) and the graph (article dedup, extraction checks) both use this."""
    low = _text(value).casefold()
    for url in DOI_URLS:
        if low.startswith(url):
            return low[len(url):].strip() or None
    if m := ARTICLE_PREFIX.match(low):
        low, pmcid = low[m.end():].strip(), pmcid or m.group(1) == "pmcid"
    if re.fullmatch(r"pmc\d+", low):
        return "PMC" + low[3:]
    if low.isdigit():
        return f"PMC{low}" if pmcid else low
    return low or None


def _read_ids(call: ToolCall) -> set[str]:
    """Every identifier of the article a successful read returned (what it was read as, and what the adapter said)."""
    keys = (article_key(call.fulltext_article), article_key(call.read_article), *map(article_key, call.article_ids))
    return {k for k in keys if k}


def _allele_token(value: str | None) -> str:
    """The allele an observation names, from texts like "G", "g allele", "T (minor)", "ref" or "alt"."""
    return re.split(r"[\s(),;:]+", _text(value).upper())[0] if _text(value) else ""


def _homozygous(genotype: str | None) -> bool:
    """A genotype such as GG, G/G, T|T or "homozygous reference"."""
    if not genotype:
        return False
    if re.search(r"homozyg", genotype, re.I):
        return True
    bases = re.sub(r"[\s/|]", "", genotype).upper()
    return len(bases) >= 2 and bases.isalpha() and len(set(bases)) == 1


def _sign(direction: str) -> int | None:
    """+1 / -1 for a specific direction, 0 for no_change, None for unspecified."""
    return SPECIFIC_DIRECTIONS.get(direction, 0 if direction == "no_change" else None)


def _json_problem(value: Any, path: str) -> str | None:
    """Why a value is not JSON-native (dict with str keys, list, str, int, finite float, bool, None), or None. The
    graph must serialise losslessly: a numpy number or a NaN would break graph.json or change on the round trip."""
    kind = type(value)
    if value is None or kind in (str, int, bool):
        return None
    if kind is float:
        return None if math.isfinite(value) else f"{path} is {value!r} (omit a missing value instead)"
    if kind is list:
        return next((p for i, x in enumerate(value) if (p := _json_problem(x, f"{path}[{i}]"))), None)
    if kind is dict:
        for k, x in value.items():
            if type(k) is not str:
                return f"{path} has a non-string key {k!r}"
            if p := _json_problem(x, f"{path}.{k}"):
                return p
        return None
    return f"{path} holds a value of type {kind.__name__} (JSON-native values only)"


def display_of(claim: Claim, evidence: Mapping[str, Evidence]) -> ClaimDisplay:
    """The report's status for a claim: its assessment paired with its basis (SPEC 2, 13.6), derived from the claim
    and the evidence its links name, never stored. A pure function, so a report can show a claim as it stood at an
    earlier version (an older assessment and set of links) by the same rule the graph uses:

        contradicted_in_scope  contradicted, basis the strongest class among its direct contradicting links
        contested              contested
        supported_in_scope     supported, basis the strongest class among its direct exact/proxy supporting links
        otherwise              associated / predicted when indirect association-type / prediction support is linked
                               (the basis names it), else unresolved

    `basis_classes` lists every class among its supports links; the dependency flag is carried as a separate badge."""

    def classes(stance: str, strength: str | None = None, apps: tuple[str, ...] = ()) -> list[str]:
        found = {evidence[x.evidence_id].evidence_class for x in claim.evidence_links
                 if x.stance == stance and (strength is None or x.strength == strength)
                 and (not apps or x.applicability in apps)}
        return sorted(found, key=CLASS_ORDER.index)

    supports = classes("supports")
    basis = None
    if claim.assessment == "contradicted_in_scope":
        status = "contradicted"
        basis = next(iter(classes("contradicts", "direct")), None)
    elif claim.assessment == "contested":
        status = "contested"
    elif claim.assessment == "supported_in_scope":
        status = "supported"
        basis = next(iter(classes("supports", "direct", ("exact", "proxy"))), None)
    else:
        indirect = classes("supports", "indirect")
        if associated := [c for c in indirect if c in ASSOCIATED_BASIS]:
            status, basis = "associated", associated[0]
        elif predicted := [c for c in indirect if c in PREDICTED_BASIS]:
            status, basis = "predicted", predicted[0]
        else:
            status = "unresolved"
    return ClaimDisplay(status=status, basis=basis, basis_classes=supports, dependency_flag=claim.dependency_flag)


def _atomic(method):
    """Run a mutation so that any exception inside it (a GraphRefusal or anything else) restores the graph to its
    state before the call. Nested atomic calls share the outermost snapshot."""

    @wraps(method)
    def wrapper(self: "ClaimGraph", *args, **kwargs):
        if self._depth:
            return method(self, *args, **kwargs)
        snapshot = self._snapshot()
        self._depth += 1
        try:
            return method(self, *args, **kwargs)
        except BaseException:
            self._restore(snapshot)
            raise
        finally:
            self._depth -= 1

    return wrapper


class ClaimGraph:
    """See the module docstring. Read the public attributes freely; change state only through the methods.
    `resolver` HGNC-normalises gene and TF symbols; `groups` (the QBiC-SELEX group registry) fixes the members of
    registry tf_groups. The engine passes both; tests may omit them."""

    def __init__(self, case: Case, resolver: SymbolResolver | None = None, groups: GroupRegistry | None = None):
        self.engine_version = ENGINE_VERSION
        self.case = case
        self.resolver = resolver
        self.groups = groups
        self.version = 0
        self.counters: dict[str, int] = {p: 0 for p in PREFIXES}
        self.model_usage = ModelUsage()
        self.variant_aliases: dict[str, str] = {}      # rsIDs of the case variant found by code (add_variant_alias)
        self.variant_elements: dict[str, str] = {}     # elements containing the case variant (add_variant_element)
        self.entities: dict[str, Entity] = {}
        self.claims: dict[str, Claim] = {}
        self.evidence: dict[str, Evidence] = {}
        self.hypotheses: dict[str, Hypothesis] = {}
        self.questions: dict[str, Question] = {}
        self.tool_calls: dict[str, ToolCall] = {}
        self.comparisons: dict[str, PairComparison] = {}
        self.events: list[DecisionEvent] = []
        self.result: RunResult | None = None
        self._depth = 0
        self._entity_by_canonical: dict[tuple[str, str], str] = {}
        self._entity_by_label: dict[tuple[str, str], str] = {}
        self._claim_by_key: dict[tuple, str] = {}

    # --- bookkeeping -------------------------------------------------------------------------------------------------

    def _next(self, prefix: str) -> str:
        self.counters[prefix] += 1
        return f"{prefix}{self.counters[prefix]}"

    def _snapshot(self) -> tuple:
        # Tool calls and events are append-only, so their containers are copied shallowly; the case is replaced,
        # never changed in place (add_inferred_candidate), so keeping the reference is enough.
        deep = copy.deepcopy((self.entities, self.claims, self.evidence, self.hypotheses, self.questions,
                              self.comparisons, self.result, self.counters, self.model_usage))
        return (deep, dict(self.tool_calls), len(self.events), self.version, dict(self._entity_by_canonical),
                dict(self._entity_by_label), dict(self._claim_by_key), self.case, dict(self.variant_aliases),
                dict(self.variant_elements))

    def _restore(self, snapshot: tuple) -> None:
        (deep, tool_calls, n_events, version, by_canonical, by_label, by_key, case, aliases,
         elements) = snapshot
        (self.entities, self.claims, self.evidence, self.hypotheses, self.questions, self.comparisons, self.result,
         self.counters, self.model_usage) = deep
        self.tool_calls, self.version = tool_calls, version
        del self.events[n_events:]
        self._entity_by_canonical, self._entity_by_label, self._claim_by_key = by_canonical, by_label, by_key
        self.case, self.variant_aliases, self.variant_elements = case, aliases, elements

    @contextmanager
    def batch(self) -> Iterator[None]:
        """Many mutations under one snapshot, for code that makes thousands of them (the code-only fill links every
        record on file): each mutation alone copies the graph first, which is what makes it atomic and what makes a
        thousand of them slow. Inside a batch the mutations share the snapshot taken here, as nested atomic calls
        do. An exception that leaves the block restores the graph to its state before the batch. A refusal caught
        inside the block undoes nothing, so only catch one from a method that checks before it changes anything:
        link and assess do; add_claim does once its entities resolve."""
        if self._depth:
            yield
            return
        snapshot = self._snapshot()
        self._depth += 1
        try:
            yield
        except BaseException:
            self._restore(snapshot)
            raise
        finally:
            self._depth -= 1

    @contextmanager
    def scratch(self) -> Iterator[None]:
        """Mutations that are never kept: the graph is put back as it was when the block ends, however it ends.
        Unlike batch, each mutation inside is as atomic as outside one, so code that states a claim and links a
        record in one step behaves exactly as it will when it runs for good. For code that needs to see what a step
        would give before deciding what to do next (the fill's loop looks at the table between its rounds)."""
        if self._depth:
            raise RuntimeError("scratch() cannot run inside a batch: its mutations would not be atomic")
        snapshot = self._snapshot()
        try:
            yield
        finally:
            self._restore(snapshot)

    def fulltext_articles(self) -> list[frozenset[str]]:
        """The unique articles read in full, each as the set of its identifiers (article_key form). Two counted reads
        that share any identifier (what each was read as, or any id its adapter reported) are one article, so an
        article read by PMCID and later by PMID or DOI is counted once. Deterministic: reads are taken in call order
        and the result is sorted."""
        groups: list[set[str]] = []
        for t in self.tool_calls.values():
            if not (t.fulltext_article and t.charged_to != "none" and t.execution_status == "success"):
                continue
            ids = _read_ids(t)
            for g in [g for g in groups if g & ids]:
                ids |= g
                groups.remove(g)
            groups.append(ids)
        return sorted((frozenset(g) for g in groups), key=sorted)

    def budget_snapshot(self) -> BudgetSnapshot:
        """Tool counts come from the recorded calls; model calls and cost from set_model_usage()."""
        calls = self.tool_calls.values()
        return BudgetSnapshot(model_calls=self.model_usage.calls, cost_usd=round(self.model_usage.cost_usd, 6),
                              tool_calls=sum(t.charged_to == "agent" for t in calls),
                              code_tool_calls=sum(t.charged_to == "code" for t in calls),
                              fulltext_reads=len(self.fulltext_articles()))

    def set_model_usage(self, calls: int, cost_usd: float) -> None:
        """The engine reports model calls and spend so every later event's budget snapshot carries them."""
        self.model_usage = ModelUsage(calls=calls, cost_usd=cost_usd)

    def _event(self, action: EventAction, role: Role, reason: str, *, targets: Iterable[str] = (),
               evidence: Iterable[str] = (), supersedes: Iterable[str] = (), details: dict[str, Any] | None = None,
               mutate: bool = True) -> DecisionEvent:
        before = self.version
        if mutate:
            self.version += 1
        event = DecisionEvent(event_id=self._next("D"), graph_version_before=before, graph_version_after=self.version,
                              role=role, action=action, target_ids=list(dict.fromkeys(targets)),
                              evidence_ids=list(dict.fromkeys(evidence)), concise_reason=_text(reason)[:MAX_REASON],
                              supersedes=list(supersedes), budget_snapshot=self.budget_snapshot(),
                              details=details or {})
        self.events.append(event)
        return event

    def log(self, action: EventAction, role: Role, reason: str, target_ids: Iterable[str] = (),
            evidence_ids: Iterable[str] = (), details: dict[str, Any] | None = None) -> str:
        """Record a decision that changes no graph object (normalize, collect_facts, audit, stop, ...)."""
        return self._event(action, role, reason, targets=target_ids, evidence=evidence_ids, details=details,
                           mutate=False).event_id

    # --- entities ----------------------------------------------------------------------------------------------------

    def _symbol(self, symbol: str) -> str:
        label = _text(symbol).upper()
        hit = self.resolver(label) if self.resolver and label else None
        return hit[0].upper() if hit else label

    def _canonical(self, kind: str, label: str, canonical_id: str | None) -> tuple[str, str | None]:
        """Normalised label and canonical id. For genes and TFs an HGNC hit wins over any id a proposer gave."""
        label = _text(label)
        if kind in SYMBOL_KINDS:
            label = label.upper()
        if kind in HGNC_KINDS and self.resolver and label and (hit := self.resolver(label)):
            label, canonical_id = hit[0].upper(), hit[1]
        if kind == "phenotype":
            canonical_id = ontology_id(canonical_id) or canonical_id
        return label, (_text(canonical_id) or None)

    @staticmethod
    def _label_key(kind: str, label: str) -> tuple[str, str]:
        if kind == "phenotype":
            return kind, trait_key(label)
        return kind, (label.upper() if kind in SYMBOL_KINDS else label.casefold())

    def _find_entity(self, kind: str, label: str, canonical_id: str | None) -> str | None:
        """Genes, TFs and transcripts are one entity per normalised symbol (a second id for the same symbol is never
        a second entity); phenotypes retain full source-label scopes even with a shared ontology id; other kinds
        are keyed on the canonical id first (two elements may share a label)."""
        if kind == "phenotype":
            # A broad ontology id may describe distinct measurements/populations. Keep their full labels.
            return next((e.entity_id for e in self.entities.values() if e.kind == kind
                         and trait_key(e.label) == trait_key(label)
                         and (not canonical_id or not e.canonical_id or canonical_id == e.canonical_id)), None)
        if kind in LABEL_KEYED and label and (hit := self._entity_by_label.get(self._label_key(kind, label))):
            return hit
        if canonical_id and (kind, canonical_id) in self._entity_by_canonical:
            return self._entity_by_canonical[(kind, canonical_id)]
        if kind in LABEL_KEYED:
            return None
        hit = self._entity_by_label.get(self._label_key(kind, label)) if label else None
        if hit and not (canonical_id and self.entities[hit].canonical_id):
            return hit
        return None

    def _index_entity(self, ent: Entity) -> None:
        if ent.canonical_id:
            self._entity_by_canonical.setdefault((ent.kind, ent.canonical_id), ent.entity_id)
        self._entity_by_label.setdefault(self._label_key(ent.kind, ent.label), ent.entity_id)

    def _refuse_new_members(self, ent: Entity, labels: Iterable[str]) -> None:
        have = [self.entities[p].label for p in ent.participants]
        extra = sorted(set(labels) - set(have))
        if extra:
            registry = ent.kind == "tf_group" and self.groups and self.groups.members(ent.canonical_id) is not None
            source = "from the QBiC-SELEX group registry" if registry else "fixed when it was created"
            raise GraphRefusal(f"{ent.label} ({ent.entity_id}) has the members {', '.join(have) or 'none'}, {source}; "
                               f"{', '.join(extra)} cannot be added: name another group, or the TF itself")

    @_atomic
    def entity(self, kind: EntityKind, label: str, canonical_id: str | None = None,
               qualifiers: dict[str, str] | None = None, participants: Sequence[str] = ()) -> str:
        """The id of the entity, created when new (no event). Genes, TFs and transcripts are deduplicated on their
        normalised symbol (HGNC-normalised when a resolver is set), other kinds on (kind, canonical_id) when given,
        else (kind, normalised label). Phenotypes also require the same normalised full label. An existing entity
        gains a missing canonical id and new qualifiers, never new
        participants: a group's members are fixed at creation (a registry group's come from the registry)."""
        label, canonical_id = self._canonical(kind, label, canonical_id)
        if not label and not canonical_id:
            raise GraphRefusal(f"a {kind} entity needs a label or a canonical id")
        for pid in participants:
            if pid not in self.entities:
                raise GraphRefusal(f"participant {pid} is not an entity")
        registry = self.groups.members(canonical_id) if kind == "tf_group" and self.groups else None
        if registry is not None:
            listed = [self.entity("tf", m) for m in registry]
            extra = sorted({self.entities[p].label for p in participants if p not in listed})
            if extra:
                raise GraphRefusal(f"{canonical_id}'s members are {', '.join(registry)}, from the QBiC-SELEX group "
                                   f"registry; {', '.join(extra)} cannot be added")
            participants = listed
        found = self._find_entity(kind, label, canonical_id)
        if found:
            ent = self.entities[found]
            self._refuse_new_members(ent, (self.entities[p].label for p in participants))
            if canonical_id and not ent.canonical_id:
                ent.canonical_id = canonical_id
                self._index_entity(ent)
            for k, v in (qualifiers or {}).items():
                ent.qualifiers.setdefault(k, v)
            return found
        if kind == "tf_group" and not participants:
            raise GraphRefusal(f"tf_group {label or canonical_id} needs its member TFs (from the group registry, or "
                               "listed with the group)")
        eid = self._next("N")
        ent = Entity(entity_id=eid, kind=kind, canonical_id=canonical_id, label=label or str(canonical_id),
                     participants=list(dict.fromkeys(participants)), qualifiers=dict(qualifiers or {}))
        self.entities[eid] = ent
        self._index_entity(ent)
        return eid

    def variant_entity(self) -> str:
        """The case variant's entity (canonical id GRCh38:chrom:pos:ref:alt)."""
        v = self.case.variant
        return self.entity("variant", v.rsid or f"{v.chrom}:{v.pos} {v.ref}>{v.alt}", canonical_id=v.key)

    def _case_rsids(self) -> set[str]:
        """The case variant's own rsIDs (lower case): the supplied one and those code recorded as aliases."""
        supplied = self.case.variant.rsid
        return ({supplied.lower()} if supplied else set()) | set(self.variant_aliases)

    def variant_mention(self, text: str | None) -> Literal["case", "other"] | None:
        """What a text names as a variant, by the one rule the graph applies to variant labels, canonical ids and
        the about_variants and about_elements entries of evidence (the engine and the evaluator should call it rather
        than copy it):

            None     no rsID and no chromosome position ("the G allele", "V", ""): it names no variant explicitly;
            "case"   only the case variant: its key (GRCh38:chrom:pos:ref:alt, any case), one of its rsIDs (the
                     supplied one or an alias code recorded, any case), or its chrom:pos ("chr" optional; positions
                     are GRCh38, as the case is), with any allele pair written after the position being the case's
                     ref and alt in either order ("chr2:60490908:T>G", "2:60490908 G/T");
            "other"  anything else that names a variant: an rsID that is not the case's own (with no rsID supplied or
                     recorded, every rsID), another chromosome or position, or another allele pair at the case's
                     position ("chr2:60490908:T>C"). A text naming the case variant and another one names another.

        Alleles after an rsID are not read: papers write them on either strand."""
        t = _text(text)
        v = self.case.variant
        if not t:
            return None
        if t.casefold() == v.key.casefold():
            return "case"
        rsids = {r.lower() for r in RSID.findall(t)}
        positions = _positions(t, v.chrom)
        if not rsids and not positions:
            return None
        if rsids - self._case_rsids():
            return "other"
        site, alleles = (_chrom(v.chrom), v.pos), {v.ref, v.alt}
        if any((chrom, pos) != site or (pair is not None and pair != alleles) for chrom, pos, pair in positions):
            return "other"
        return "case"

    def _is_case_variant(self, label: str) -> bool:
        """A variant label means the case variant unless it names another variant (variant_mention): an rsID that is
        not one of the case's own (the supplied rsID and recorded aliases; with none, any rsID names another variant),
        another chromosome position, or another allele pair at the case's position."""
        return self.variant_mention(label) != "other"

    def _names_case_variant(self, text: str) -> bool:
        """Whether a text names the case variant explicitly: by one of its rsIDs, its key or its chrom:pos."""
        return self.variant_mention(text) == "case"

    def ref_is_case_variant(self, ref: EntityRef) -> bool:
        """Whether a variant reference resolves to the case variant (the rule _ref_entity applies): an existing
        entity id is the case variant's entity; otherwise the label must not name another variant, and a canonical
        id, when given, must name the case variant (its key, one of its rsIDs, or its chrom:pos with the case's alleles
        when alleles are written). The engine checks effect alleles by it before the graph files a claim."""
        if ref.kind != "variant":
            return False
        if ref.entity_id:
            e = self.entities.get(ref.entity_id)
            return e is not None and e.kind == "variant" and e.canonical_id == self.case.variant.key
        return self._is_case_variant(ref.label) and (not _text(ref.canonical_id)
                                                     or self.variant_mention(ref.canonical_id) == "case")

    def _ref_entity(self, ref: EntityRef, create: bool) -> str | None:
        """Resolve an EntityRef to an id; with create=False only look it up (None: it would be new). A variant
        reference is the case variant's entity when ref_is_case_variant holds: a canonical id that names the case
        variant by an alias rsID or by its chrom:pos (as a model may write it) resolves to the case, never to a second
        variant entity. Any other canonical id is kept as given."""
        if ref.entity_id:
            if ref.entity_id not in self.entities:
                raise GraphRefusal(f"unknown entity {ref.entity_id}")
            return ref.entity_id
        label, canonical = ref.label, ref.canonical_id
        if ref.kind == "variant" and self.ref_is_case_variant(ref):
            return self.variant_entity() if create else self._find_entity("variant", "", self.case.variant.key)
        if ref.members and ref.kind not in MEMBER_KINDS:
            raise GraphRefusal(f"only a tf_group, complex or binding_event lists members ({ref.kind} {label})")
        if not create:
            found = self._find_entity(ref.kind, *self._canonical(ref.kind, label, canonical))
            if found and ref.members:
                self._refuse_new_members(self.entities[found], (self._symbol(m) for m in ref.members if _text(m)))
            return found
        members = [self.entity("tf", m) for m in ref.members if _text(m)]
        return self.entity(ref.kind, label, canonical, ref.qualifiers, members)

    # --- the case: inferred candidates, the variant's rsIDs and the elements containing it --------------------------

    @staticmethod
    def _candidate_key(kind: str, label: str) -> str | None:
        """What makes two labels one candidate: a disease ignoring case, spacing and punctuation; a context by its
        normalised scope (HepG2, "Hep G2 cells" and "hepg2" are one context). None when the label names nothing."""
        if kind == "disease":
            return _ident(label) or None
        return scope_key(ContextScope(label=label))

    @_atomic
    def add_inferred_candidate(self, candidate: InferredCandidate, role: Role) -> bool:
        """Record a disease or context the run inferred in case.inferred_candidates (serialised with the case, shown
        labelled as inferred). The request is never changed: an inference never becomes supplied disease or context,
        and a candidate the request already supplies, or one already inferred (same kind and normalised label), is
        ignored (returns False). Only code and the coordinator infer candidates, and every basis_evidence_ids entry
        must be evidence in this graph, so an inference names what it rests on. graph.case is replaced, never changed
        in place: read graph.case afterwards. Logs an add_inferred_candidate event and returns True when added."""
        if role not in CANDIDATE_ROLES:
            raise GraphRefusal(f"inferred candidates are recorded by the coordinator or code, not the "
                               f"{role.replace('_', ' ')}")
        candidate = InferredCandidate.model_validate(candidate.model_dump())
        label = _text(candidate.label)
        key = self._candidate_key(candidate.kind, label)
        if key is None:
            raise GraphRefusal(f"an inferred {candidate.kind} needs a label that names one (got {candidate.label!r})")
        basis = list(dict.fromkeys(_text(e) for e in candidate.basis_evidence_ids if _text(e)))
        if unknown := [e for e in basis if e not in self.evidence]:
            raise GraphRefusal(f"unknown evidence {', '.join(unknown)}: an inferred candidate's basis must be "
                               "evidence in this graph")
        known = ({("disease", self._candidate_key("disease", d)) for d in self.case.supplied_disease}
                 | {("context", scope_key(s)) for s in self.case.supplied_context}
                 | {(c.kind, self._candidate_key(c.kind, c.label)) for c in self.case.inferred_candidates})
        if (candidate.kind, key) in known:
            return False
        stored = candidate.model_copy(update={"label": label, "basis_evidence_ids": basis,
                                              "note": _text(candidate.note)})
        self.case = self.case.model_copy(update={"inferred_candidates": [*self.case.inferred_candidates, stored]})
        self._event("add_inferred_candidate", role, f"inferred {candidate.kind} (not supplied): {label}",
                    evidence=basis, details={"kind": candidate.kind, "label": label, "note": stored.note})
        return True

    def _code_call(self, tool_call_id: str, what: str) -> ToolCall:
        """The successful, code-requested tool call with records that a fact about the case variant must come from:
        an agent's request, an empty search or a failure never changes what the case variant is."""
        call = self.tool_calls.get(tool_call_id)
        if call is None:
            raise GraphRefusal(f"unknown tool call {tool_call_id}")
        if call.execution_status != "success" or call.retrieval_status not in EVIDENCE_FROM:
            raise GraphRefusal(f"{tool_call_id} returned {call.execution_status}/{call.retrieval_status}: {what} is "
                               "recorded only from a successful call that found records")
        if call.requested_by != "code":
            raise GraphRefusal(f"{tool_call_id} was requested by the {call.requested_by.replace('_', ' ')}: {what} is "
                               "recorded only from code's own fact collection")
        return call

    @_atomic
    def add_variant_alias(self, rsid: str, tool_call_id: str) -> bool:
        """Record an rsID as the case variant's own: the rsID dbSNP gives the case's exact coordinates and alleles, as a
        code tool call (variant_annotation) reported it. A request may give coordinates only; without the alias,
        claims and papers naming that rsID would be filed under another variant. Claims naming it are then about the
        case variant (frame "case", effect allele rules apply); claims made before keep the entity they were given.
        case.variant.rsid is never changed: the request stays as supplied. Refused unless the call exists, succeeded
        with records, was requested by code and its observations name the rsID, and refused for an rsID other than a
        supplied one. Idempotent: False when the rsID is already the case's own. Logs an add_variant_alias event."""
        name = _text(rsid).lower()
        if not re.fullmatch(r"rs\d+", name):
            raise GraphRefusal(f"{rsid!r} is not an rsID (rs followed by digits)")
        supplied = (self.case.variant.rsid or "").lower()
        if supplied and name != supplied:
            raise GraphRefusal(f"{name} conflicts with the case's supplied rsID {supplied}: an alias never replaces "
                               "the request's own identifier")
        call = self._code_call(tool_call_id, "an rsID alias")
        if not re.search(rf"(?<![0-9A-Za-z]){name}(?![0-9])", json.dumps(call.observations), re.I):
            raise GraphRefusal(f"{tool_call_id}'s observations do not name {name}")
        if name in self._case_rsids():
            return False
        self.variant_aliases[name] = tool_call_id
        self._event("add_variant_alias", "code", f"{tool_call_id} reports {name} at the case variant's coordinates "
                    f"and alleles: claims naming {name} are about the case variant", targets=[tool_call_id],
                    details={"rsid": name, "tool_call_id": tool_call_id})
        return True

    @_atomic
    def add_variant_element(self, element: str, tool_call_id: str) -> bool:
        """Record that an element (its canonical id, e.g. a cCRE accession) contains the case variant, as a code tool
        call (ccre_overlap) reported it. Evidence naming a region by the variant, as papers do ("the enhancer
        containing rs1427407"), is then about this element. Refused unless the call exists, succeeded with records,
        was requested by code and one of its evidence items names the element in about_elements. Idempotent: False
        when the element is already recorded. Logs an add_variant_element event."""
        name = _text(element)
        key = _ident(name)
        if not key:
            raise GraphRefusal("an element containing the case variant needs its id")
        call = self._code_call(tool_call_id, "an element containing the case variant")
        naming = [e for e in call.evidence_ids if key in {_ident(x) for x in self.evidence[e].about_elements}]
        if not naming:
            raise GraphRefusal(f"no evidence of {tool_call_id} names element {name} (about_elements)")
        if any(_ident(x) == key for x in self.variant_elements):
            return False
        self.variant_elements[name] = tool_call_id
        self._event("add_variant_element", "code", f"{tool_call_id} places the case variant in element {name}",
                    targets=[tool_call_id], evidence=naming, details={"element": name, "tool_call_id": tool_call_id})
        return True

    # --- claims ------------------------------------------------------------------------------------------------------

    def _frame(self, entity_ids: Iterable[str]) -> Literal["case", "other"] | None:
        """Whether a claim names the case variant ("case"), only another variant ("other"), or no variant."""
        kinds = [(self.entities[e].kind, self.entities[e].canonical_id) for e in entity_ids]
        if any(k == "variant" and c == self.case.variant.key for k, c in kinds):
            return "case"
        return "other" if any(k == "variant" for k, _ in kinds) else None

    def _claim_frame(self, claim: Claim) -> Literal["case", "other"] | None:
        return self._frame(claim.subject_ids + claim.object_ids)

    def claim_frame(self, claim_id: str) -> Literal["case", "other"] | None:
        """Which variant a claim is about: "case" when it names the case variant's entity (a reference naming the case
        by an rsID code recorded as its alias, or by its chrom:pos, resolves to that entity), "other" when it names
        only other variants (an LD partner, or an rsID named before code recorded it as an alias), None when it names
        no variant (an element-gene or gene-trait link). The rule the graph's allele frame and variant checks use; a
        KeyError for an unknown claim id."""
        return self._claim_frame(self.claims[claim_id])

    def _case_variant_names(self) -> str:
        """How messages name the case variant: its rsIDs (supplied, then recorded aliases) and its position."""
        v = self.case.variant
        rsids = ([v.rsid.lower()] if v.rsid else []) + sorted(set(self.variant_aliases) - {(v.rsid or "").lower()})
        return ", ".join([*rsids, f"chr{v.chrom}:{v.pos} {v.ref}>{v.alt}"])

    def _allele_side(self, allele: str | None) -> Literal["ref", "alt"] | None:
        """Which allele of the case variant a text names (a base, "ref" or "alt"), or None."""
        token, v = _allele_token(allele), self.case.variant
        if token in ("REF", "REFERENCE") or (token and token == v.ref):
            return "ref"
        if token in ("ALT", "ALTERNATE", "ALTERNATIVE") or (token and token == v.alt):
            return "alt"
        return None

    def _effect_allele(self, draft: ClaimDraft, entity_ids: Sequence[str]) -> str | None:
        """The claim's effect allele: for the case variant its ref or alt base (alt when the draft names none); for
        another variant as given; none for a claim that names no variant."""
        given = _text(draft.effect_allele).upper() or None
        frame = self._frame(entity_ids)
        if frame == "case":
            if given is None:
                return self.case.variant.alt
            side = self._allele_side(given)
            if side is None:
                v = self.case.variant
                raise GraphRefusal(f"effect allele {given} is neither ref {v.ref} nor alt {v.alt} of the case variant")
            return self.case.variant.ref if side == "ref" else self.case.variant.alt
        if frame == "other":
            return given and _allele_token(given)
        if given:
            raise GraphRefusal("an effect allele belongs to a claim that names a variant")
        return None

    def _key_direction(self, direction: str, effect_allele: str | None,
                       frame: Literal["case", "other"] | None) -> str:
        """The direction in a common frame: for the case variant, what the alt allele does ("ref decreases" is "alt
        increases"); for another variant, tagged with its effect allele."""
        if frame == "case" and effect_allele == self.case.variant.ref != self.case.variant.alt:
            return FLIP.get(direction, direction)
        if frame == "other" and effect_allele:
            return f"{effect_allele}:{direction}"
        return direction

    def _claim_key(self, subjects: Sequence[str], relation: str, objects: Sequence[str], direction: str,
                   effect_allele: str | None, allele_scope: str | None, context: ContextScope | None) -> tuple:
        frame = self._frame([*subjects, *objects])
        return (tuple(sorted(subjects)), relation, tuple(sorted(objects)),
                self._key_direction(direction, effect_allele, frame), _text(allele_scope).casefold() or None,
                scope_key(context))

    def _live_claim(self, claim_id: str) -> Claim:
        claim = self.claims.get(claim_id)
        if claim is None:
            raise GraphRefusal(f"unknown claim {claim_id}")
        if claim.superseded_by:
            raise GraphRefusal(f"{claim_id} is superseded by {claim.superseded_by}; act on the replacement")
        return claim

    def _describe(self, subjects: Sequence[str], relation: str, objects: Sequence[str], direction: str,
                  effect_allele: str | None) -> str:
        """A plain default assertion text when the proposer gave none."""
        notes = [direction] if direction != "unspecified" else []
        if effect_allele and notes:
            notes.append(f"effect allele {effect_allele}")
        subject_names = ", ".join(self.entities[i].label for i in subjects)
        object_names = ", ".join(self.entities[i].label for i in objects)
        tail = f" ({'; '.join(notes)})" if notes else ""
        return f"{subject_names} {relation.replace('_', ' ')} {object_names}{tail}"

    def _check_shape(self, relation: str, entity_ids: Sequence[str]) -> None:
        """A binding claim names the bound factor as a TF, TF group or complex, so its identity can be checked."""
        if relation in BINDING_RELATIONS and not any(self.entities[e].kind in BINDER_KINDS for e in entity_ids):
            named = ", ".join(f"{self.entities[e].label} ({self.entities[e].kind})" for e in entity_ids)
            raise GraphRefusal(f"a {relation} claim names the bound factor as a tf, tf_group or complex entity (this "
                               f"one names {named})")

    def _depends_on(self, claim_id: str, target: str) -> bool:
        """Whether claim_id rests (directly or through its premises) on target."""
        seen: set[str] = set()
        stack = [claim_id]
        while stack:
            current = stack.pop()
            if current == target:
                return True
            if current not in seen:
                seen.add(current)
                stack.extend(self.claims[current].dependencies)
        return False

    def _merge_dependencies(self, claim: Claim, dependencies: Sequence[str], role: Role, reason: str) -> list[str]:
        """A duplicate draft's premises become premises of the shared claim (one event), so a failed premise is
        propagated to it whichever hypothesis proposed it."""
        added = [d for d in dict.fromkeys(dependencies) if d not in claim.dependencies]
        for dep in added:
            if self._depends_on(dep, claim.claim_id):
                raise GraphRefusal(f"{claim.claim_id} cannot depend on {dep}: {dep} already rests on "
                                   f"{claim.claim_id}")
        if added:
            claim.dependencies.extend(added)
            self._event("add_dependency", role, reason or f"{claim.claim_id} also rests on {', '.join(added)}",
                        targets=[claim.claim_id, *added],
                        details={"added": added, "dependencies": list(claim.dependencies)})
        return added

    @_atomic
    def add_claim(self, draft: ClaimDraft, role: Role, reason: str = "") -> str:
        """The id of the claim, created when new. A draft with the same key (entities, relation, direction in the
        common allele frame, allele scope, normalised context) returns the existing claim: similar wording is never a
        new claim; the draft's new premises are added to it."""
        return self._add_claim(draft, role, reason)[0]

    def _add_claim(self, draft: ClaimDraft, role: Role, reason: str) -> tuple[str, bool, list[str]]:
        """(claim id, created, premises added to an existing claim)."""
        if not draft.subjects or not draft.objects:
            raise GraphRefusal("a claim needs at least one subject and one object")
        for dep in draft.dependencies:
            self._live_claim(dep)
        context = normalise_scope(draft.context, variant=self.case.variant)
        found = [self._ref_entity(r, create=False) for r in draft.subjects + draft.objects]
        if all(found):
            n = len(draft.subjects)
            ids = [str(f) for f in found]
            key = self._claim_key(ids[:n], draft.relation, ids[n:], draft.direction,
                                  self._effect_allele(draft, ids), draft.allele_scope, context)
            if existing := self._claim_by_key.get(key):
                old = self.claims[existing]
                if old.superseded_by:
                    raise GraphRefusal(f"this proposition is {existing}, superseded by {old.superseded_by}; use the "
                                       "replacement or propose a materially different claim")
                return existing, False, self._merge_dependencies(old, draft.dependencies, role, reason)
        subjects = [str(self._ref_entity(r, create=True)) for r in draft.subjects]
        objects = [str(self._ref_entity(r, create=True)) for r in draft.objects]
        self._check_shape(draft.relation, subjects + objects)
        effect = self._effect_allele(draft, subjects + objects)
        key = self._claim_key(subjects, draft.relation, objects, draft.direction, effect, draft.allele_scope, context)
        cid = self._next("C")
        claim = Claim(claim_id=cid, subject_ids=subjects, relation=draft.relation, object_ids=objects,
                      direction=draft.direction, effect_allele=effect, allele_scope=_text(draft.allele_scope) or None,
                      context_scope=context, mechanism_class=draft.mechanism_class,
                      assertion_text=_text(draft.assertion_text) or self._describe(subjects, draft.relation, objects,
                                                                                   draft.direction, effect),
                      dependencies=list(dict.fromkeys(draft.dependencies)), limitations=list(draft.limitations),
                      proposed_by=role)
        self.claims[cid] = claim
        self._claim_by_key[key] = cid
        event = self._event("new_claim", role, reason or claim.assertion_text, targets=[cid],
                            details={"relation": claim.relation, "direction": claim.direction,
                                     "effect_allele": claim.effect_allele, "dependencies": claim.dependencies})
        claim.history.append(ClaimHistoryEntry(version=1, assessment="unassessed", event_id=event.event_id,
                                               action="new_claim"))
        return cid, True, []

    # --- evidence ----------------------------------------------------------------------------------------------------

    @staticmethod
    def _source_ids(ev: Evidence) -> set[str]:
        """Every article id the evidence cites, in article_key form (a PMID, PMCID or DOI of one paper is one
        source)."""
        keys = [article_key(i) for i in ev.source_ids]
        if ev.experiment:
            x = ev.experiment
            keys += [article_key(x.source_id), article_key(x.pmcid, pmcid=True), article_key(x.doi)]
        return {k for k in keys if k}

    @staticmethod
    def _observed_key(ev: Evidence) -> str:
        return json.dumps([ev.evidence_class, ev.result_kind, ev.allele, ev.direction, sorted(ev.about_tfs),
                           sorted(ev.about_genes), sorted(ev.about_elements), sorted(ev.about_traits),
                           sorted(x.casefold() for x in ev.about_variants), scope_key(ev.context),
                           _text(ev.observed_result).casefold()])

    @staticmethod
    def _literature_key(ev: Evidence) -> str:
        """What makes two extractions from one article the same experiment: the location, intervention and endpoint,
        and what was observed about what (class, result kind, allele, direction, TFs, genes, elements, traits,
        variants, context and system). Wording is not part of it: one figure testing two variants is two items."""
        x = ev.experiment
        system = [_text(getattr(x.system, f)).casefold() for f in ("organism", "tissue_or_cell", "treatment",
                                                                    "genotype_or_allele")]
        return json.dumps([_text(x.location).casefold(), _text(x.intervention).casefold(),
                           _text(x.endpoint).casefold(), ev.evidence_class, ev.result_kind,
                           _allele_token(ev.allele) or None, ev.direction, sorted(ev.about_tfs),
                           sorted(ev.about_genes), sorted(ev.about_elements), sorted(ev.about_traits),
                           sorted(v.casefold() for v in ev.about_variants), scope_key(ev.context), system])

    def _find_evidence(self, ev: Evidence) -> str | None:
        """Literature: one article (any shared PMID/PMCID/DOI) and the same literature key. Otherwise: the same
        independence group and observed key."""
        if ev.experiment is not None:
            ids, key = self._source_ids(ev), self._literature_key(ev)
            return next((e.evidence_id for e in self.evidence.values()
                         if e.experiment is not None and ids & self._source_ids(e) and self._literature_key(e) == key),
                        None)
        key = self._observed_key(ev)
        return next((e.evidence_id for e in self.evidence.values()
                     if e.independence_group == ev.independence_group and self._observed_key(e) == key), None)

    def _add_evidence(self, ev: Evidence, call: ToolCall | None = None) -> str:
        if ev.evidence_id:
            raise GraphRefusal("evidence ids are issued by the graph; pass evidence_id=''")
        if not _text(ev.observed_result) or not _text(ev.independence_group):
            raise GraphRefusal("evidence needs an observed_result and an independence_group")
        if ev.evidence_class == "synthetic" and not (self.case.synthetic and ev.origin == "fixture"):
            raise GraphRefusal("synthetic evidence exists only as fixture evidence in a synthetic case (SYN-)")
        if ev.origin == "fixture" and not self.case.synthetic:
            raise GraphRefusal("fixture evidence never enters a biological case")
        if ev.result_kind == "null_in_assessed_scope":
            if ev.assessed_relation is None:
                raise GraphRefusal("a measured null must state the relation its assay's scope tests "
                                   "(assessed_relation)")
            if ev.direction not in ("no_change", "unspecified"):
                raise GraphRefusal(f"a measured null cannot carry the direction {ev.direction}")
        elif ev.direction == "no_change":
            raise GraphRefusal("an observation of no change is a measured null: give it result_kind "
                               "null_in_assessed_scope and the assessed_relation its assay's scope tests")
        if problem := _json_problem(ev.data, "data"):
            raise GraphRefusal(f"evidence {problem}")
        ref = ev.retrieval_ref
        if ref is None and ev.evidence_class != "metadata_audit":
            raise GraphRefusal("evidence must name the tool call that retrieved it (retrieval_ref)")
        if ref is not None:
            tc = call if call is not None and call.tool_call_id == ref else self.tool_calls.get(ref)
            if tc is None:
                raise GraphRefusal(f"evidence names an unknown tool call {ref}")
            if tc.execution_status != "success" or tc.retrieval_status not in EVIDENCE_FROM:
                raise GraphRefusal(f"{ref} returned {tc.execution_status}/{tc.retrieval_status}: an empty or failed "
                                   "retrieval creates no Evidence")
        ev = ev.model_copy(update={
            "about_tfs": list(dict.fromkeys(self._symbol(s) for s in ev.about_tfs if _text(s))),
            "about_genes": list(dict.fromkeys(self._symbol(s) for s in ev.about_genes if _text(s))),
            "about_elements": list(dict.fromkeys(_text(s) for s in ev.about_elements if _text(s))),
            "about_traits": list(dict.fromkeys(_text(s) for s in ev.about_traits if _text(s))),
            "about_variants": list(dict.fromkeys(_text(s) for s in ev.about_variants if _text(s))),
            "source_ids": list(dict.fromkeys(_text(s) for s in ev.source_ids if _text(s))),
            "context": normalise_scope(ev.context, variant=self.case.variant)})
        if existing := self._find_evidence(ev):
            known = self.evidence[existing]
            known.source_ids.extend(s for s in ev.source_ids if s not in known.source_ids)   # keep every id
            return existing
        eid = self._next("E")
        self.evidence[eid] = ev.model_copy(update={"evidence_id": eid})
        return eid

    def _check_read(self, ev: Evidence) -> None:
        """An extracted experiment must come from a literature read of its own article (cited by any of the ids the
        read reports for it)."""
        tc = self.tool_calls.get(ev.retrieval_ref) if ev.retrieval_ref else None
        if tc is None or not tc.read_article:
            what = "names no tool call" if ev.retrieval_ref is None else (
                f"names {ev.retrieval_ref}, which is not a literature read" if tc else
                f"names an unknown tool call {ev.retrieval_ref}")
            raise GraphRefusal(f"an extracted experiment must name the literature read that returned its article "
                               f"(retrieval_ref); this one {what}")
        sources = self._source_ids(ev)
        if not _read_ids(tc) & sources:
            raise GraphRefusal(f"{tc.tool_call_id} read {tc.read_article}, but the experiment cites "
                               f"{', '.join(sorted(sources)) or 'no article'}")

    @_atomic
    def add_evidence(self, evidence: Evidence, role: Role, reason: str = "") -> str:
        """Evidence not created by a tool call: an experiment extracted from a paper the run read (origin
        "literature", an ExperimentRecord, retrieval_ref = the read of that article), or a metadata audit (no
        retrieval_ref needed). Tool and fixture evidence enter with their call (record_tool_call). Returns the
        existing id for a duplicate."""
        if evidence.evidence_class != "metadata_audit":
            if evidence.origin != "literature":
                raise GraphRefusal("tool and fixture evidence enters with its tool call (record_tool_call); "
                                   "add_evidence takes experiments extracted from a paper the run read, and "
                                   "metadata audits")
            if evidence.experiment is None:
                raise GraphRefusal("an extracted experiment needs its ExperimentRecord (source, location and the "
                                   "verified passage)")
            self._check_read(evidence)
        n = len(self.evidence)
        eid = self._add_evidence(evidence)
        created = len(self.evidence) > n
        self._event("add_evidence", role, reason or evidence.observed_result, targets=[eid], evidence=[eid],
                    details={"created": created, "evidence_class": evidence.evidence_class}, mutate=created)
        return eid

    def reserve_tool_call_id(self) -> str:
        """The next T# (the runner needs it before the call to name raw/T#.json)."""
        return self._next("T")

    @_atomic
    def record_tool_call(self, call: ToolCall, evidence: Sequence[Evidence] = ()) -> ToolCall:
        """Store a ToolCall whose id came from reserve_tool_call_id(), adding its Evidence (deduplicated; each item's
        retrieval_ref becomes the call). Evidence from a call that found no records is refused, and so are
        observations that are not JSON-native."""
        tid = call.tool_call_id
        if tid in self.tool_calls or not re.fullmatch(r"T\d+", tid) or _num(tid) > self.counters["T"]:
            raise GraphRefusal(f"{tid} is not a reserved, unused tool call id")
        if evidence and (call.execution_status != "success" or call.retrieval_status not in EVIDENCE_FROM):
            raise GraphRefusal(f"{call.tool_name} returned {call.execution_status}/{call.retrieval_status}: an empty "
                               "or failed retrieval creates no Evidence")
        if problem := _json_problem(call.observations, "observations"):
            raise GraphRefusal(f"{call.tool_name}: {problem}")
        ids: list[str] = []
        for ev in evidence:
            eid = self._add_evidence(ev.model_copy(update={"retrieval_ref": tid}), call)
            if eid not in ids:
                ids.append(eid)
        stored = call.model_copy(update={"evidence_ids": ids})
        self.tool_calls[tid] = stored
        self._event("tool_call", call.requested_by, call.message or f"{call.tool_name}: {call.execution_status}",
                    targets=[tid] + ([call.question_id] if call.question_id else []), evidence=ids,
                    details={"tool": call.tool_name, "execution_status": call.execution_status,
                             "retrieval_status": call.retrieval_status, "charged_to": call.charged_to,
                             "cached": call.cached})
        return stored

    # --- evidence links ----------------------------------------------------------------------------------------------

    def _element_refusal(self, ev: Evidence, e: Entity, subject: bool, via_variant: Sequence[str]) -> str:
        """Why evidence is not about a claim's element, worded so the proposer can act on it (name the element, or
        see which elements code recorded over the variant)."""
        reason = (f"{ev.evidence_id} is about element(s) {', '.join(ev.about_elements) or 'none named'}, not "
                  f"{e.canonical_id or e.label}")
        if subject:
            reason += (": a claim about what an element does needs evidence that names that element (a TF or gene "
                       "perturbation that changed a gene is not a test of the element)")
        if via_variant:
            recorded = ", ".join(self.variant_elements) or "none"
            reason += (f"; '{via_variant[0]}' names the case variant, and the elements recorded as containing it are "
                       f"{recorded}")
        return reason

    @staticmethod
    def _group_prediction(ev: Evidence, group: Entity) -> bool:
        """Whether a prediction is about a model-sharing group as a whole: the QBiC-SELEX inventory's item for that
        group (data.group_id) when its gate-passing models agree about the allele (data.discordant is False, which
        only the inventory writes). Such an item speaks for no single member, so a link to the group's own claim needs
        none named. A discordant group's items (each about the members whose models favour one allele), a single
        model's prediction (qbic_tf_detail) and every experiment are about members, and a link must say which."""
        return (ev.evidence_class == "prediction" and ev.origin == "tool" and ev.data.get("discordant") is False
                and group.canonical_id is not None and str(ev.data.get("group_id")) == group.canonical_id)

    def _check_identity(self, claim: Claim, ev: Evidence, rationale: str) -> list[str]:
        """Every TF, group, complex, gene, element and trait the claim names must be what the evidence is about.
        Returns notes for the link's event (what was accepted on a rule that needs saying).

        Groups: the evidence must be about a member, and the rationale must name the member it is about, so that
        member-level evidence (a ChIP-seq peak of one paralog, an EMSA, one model's prediction) is never read as the
        group's. The one exception is the group's own QBiC-SELEX inventory item when its gate-passing models agree
        (_group_prediction): it is about the group as a whole, and requiring a member's name only refused the link a
        predicted group claim rests on.

        Elements: an element that is a subject of the claim (what the element does) must be named by the evidence,
        whatever the relation, so a TF knockdown that changed a gene cannot test "element E regulates gene G". An
        element in the object position must be named when the evidence names elements at all, and always for
        `overlaps` (a reporter construct naming no accession is not about another element). An about_elements entry
        naming the case variant by rsID or chrom:pos ("the enhancer containing rs1427407") names every element code
        recorded as containing the variant (add_variant_element); every entry also matches by label or canonical id."""
        notes: list[str] = []
        binding = claim.relation in TF_IDENTITY_RELATIONS
        tfs = set(ev.about_tfs) if binding else set(ev.about_tfs) | set(ev.about_genes)
        tf_names = ", ".join(sorted(tfs)) or "no TF"
        genes = set(ev.about_genes)
        elements = {_ident(x) for x in ev.about_elements}
        via_variant = [x for x in ev.about_elements if self._names_case_variant(x)]
        if via_variant:
            elements |= {_ident(x) for x in self.variant_elements}
        for eid in claim.subject_ids + claim.object_ids:
            e = self.entities[eid]
            names = {_ident(e.label), _ident(e.canonical_id)} - {""}
            if e.kind == "tf" and e.label not in tfs:
                raise GraphRefusal(f"{ev.evidence_id} is about {tf_names}, not {e.label}: evidence about one TF cannot "
                                   "support or contradict a claim about another")
            if e.kind == "tf_group":
                members = [self.entities[p].label for p in e.participants]
                hits = [m for m in members if m in tfs]
                if not hits:
                    raise GraphRefusal(f"{ev.evidence_id} is about {tf_names}, none of the members of {e.label} "
                                       f"({', '.join(members)})")
                if not any(re.search(rf"(?<![A-Za-z0-9]){re.escape(m)}(?![A-Za-z0-9])", rationale, re.I)
                           for m in hits):
                    if not self._group_prediction(ev, e):
                        raise GraphRefusal(f"a link to group claim {claim.claim_id} must name the member the "
                                           f"evidence is about ({', '.join(hits)}) in its rationale")
                    notes.append(f"{ev.evidence_id} is the QBiC-SELEX inventory item of group {e.canonical_id} "
                                 "itself (its gate-passing models agree about the allele), so no member is named")
            if e.kind in ("complex", "binding_event"):
                members = [self.entities[p].label for p in e.participants]
                if not members:
                    raise GraphRefusal(f"{e.label} ({e.kind}) lists no member TFs, so no evidence can be matched to "
                                       "it: name its members")
                if missing := [m for m in members if m not in tfs]:
                    raise GraphRefusal(f"{ev.evidence_id} is about {tf_names}; {e.label} needs every member "
                                       f"({', '.join(missing)} missing)")
            if e.kind in ("gene", "transcript") and not {e.label, _text(e.canonical_id).upper()} & genes:
                raise GraphRefusal(f"{ev.evidence_id} is about {', '.join(sorted(genes)) or 'no gene'}, not "
                                   f"{e.kind} {e.label}")
            if e.kind == "element":
                subject = eid in claim.subject_ids
                if (subject or ev.about_elements or claim.relation == "overlaps") and not names & elements:
                    raise GraphRefusal(self._element_refusal(ev, e, subject, via_variant))
            if e.kind == "phenotype" and not trait_identity(e.label, e.canonical_id, ev.about_traits):
                raise GraphRefusal(f"{ev.evidence_id} is about trait(s) {', '.join(ev.about_traits) or 'none named'}, "
                                   f"not {e.label}: evidence about one trait cannot support or contradict a claim "
                                   "about another")
        return notes

    def _same_variant(self, text: str, entity: Entity) -> bool:
        """Whether a text names the variant of an entity filed as another variant: a shared rsID, or the same
        chrom:pos with no conflicting allele pair."""
        names = f"{entity.label} {entity.canonical_id or ''}"
        if {r.lower() for r in RSID.findall(text)} & {r.lower() for r in RSID.findall(names)}:
            return True
        chrom = self.case.variant.chrom
        theirs = _positions(names, chrom)
        return any((c, p) == (c2, p2) and (a is None or a2 is None or a == a2)
                   for c, p, a in _positions(text, chrom) for c2, p2, a2 in theirs)

    def _check_variants(self, claim: Claim, ev: Evidence) -> None:
        """Evidence about one variant never supports or contradicts a claim about another (supports/contradicts only).

        - A claim about the case variant: evidence whose about_variants name variants, none of them the case variant
          (variant_mention), is refused: an EMSA of an LD partner tested in the same paper is not about the case.
        - A claim about other variants only: evidence that names variants must name one of the claim's (by rsID or
          position); an entry naming the case variant never counts.
        - Either, for a relation in ALLELIC_RELATIONS: evidence that compares alleles (an allele, or an experiment
          that manipulated the allele) must name the claim's variant, or which variant's alleles it compared is
          unknown. Evidence that compares no alleles and names no variant is about an element, gene or cell line and
          passes; entries that name no variant (no rsID or position) are ignored. A claim naming no variant (an
          element-gene link) is not checked here."""
        frame = self._claim_frame(claim)
        if frame is None:
            return
        if frame == "case" and ev.data.get("variant_identity_status") == "unresolved":
            raise GraphRefusal("Paper variant identity is unresolved, not verified different: retain the "
                               "experiment in paper scope until a source-backed case mapping is available")
        if (frame == "case" and ev.data.get("paper_assembly") not in (None, self.case.variant.assembly) and
                not ev.data.get("variant_identity") and any(_positions(x, self.case.variant.chrom)
                                                           for x in ev.about_variants)):
            raise GraphRefusal("Paper coordinates need a verified assembly/strand mapping to the case before "
                               "support or contradiction; retain the experiment in its original scope meanwhile")
        named = [(x, m) for x in ev.about_variants if (m := self.variant_mention(x)) is not None]
        if frame == "case":
            about_claim = any(m == "case" for _, m in named)
            wanted = f"the case variant ({self._case_variant_names()})"
        else:
            others = [self.entities[e] for e in claim.subject_ids + claim.object_ids
                      if self.entities[e].kind == "variant" and self.entities[e].canonical_id != self.case.variant.key]
            about_claim = any(m == "other" and any(self._same_variant(x, e) for e in others) for x, m in named)
            wanted = ", ".join(e.label for e in others)
        if named and not about_claim:
            raise GraphRefusal(f"{ev.evidence_id} is about {', '.join(x for x, _ in named)}, not {wanted}: evidence "
                               "about one variant cannot support or contradict a claim about another")
        compares = bool(_text(ev.allele)) or (ev.experiment is not None and ev.experiment.manipulated == "allele")
        if claim.relation in ALLELIC_RELATIONS and compares and not about_claim:
            raise GraphRefusal(f"{ev.evidence_id} compares alleles but names no variant (about_variants): state which "
                               f"variant's alleles were compared; {claim.claim_id} is about {wanted}")

    def _variant_subject(self, claim: Claim) -> bool:
        """Whether the claim's subject is its variant: the case variant (frame "case"), or another variant (frame
        "other")."""
        frame = self._claim_frame(claim)
        kinds = [(self.entities[e].kind, self.entities[e].canonical_id) for e in claim.subject_ids]
        if frame == "case":
            return ("variant", self.case.variant.key) in kinds
        return frame == "other" and any(k == "variant" for k, _ in kinds)

    def _strength(self, claim: Claim, ev: Evidence) -> tuple[LinkStrength, str]:
        """What this evidence can do for this claim: the class matrix (schemas.evidence_strength), narrowed for an
        experiment bearing on what a variant's alleles do (a claim whose subject is the variant, with a relation in
        ALLELIC_RELATIONS), with the reason when narrowed:
        - a TF or gene perturbation (ExperimentRecord.manipulated "tf" or "gene") is context: knocking down a factor
          shows the factor matters, not that the alleles differ;
        - for alters_binding, alters_regulatory_activity and alters_rna, an experiment that compares no alleles
          (manipulated is not "allele" and the evidence names no allele: a region deletion, a CRISPRi of the element, a
          single-allele reporter or EMSA) is at most indirect: it shows the element or the binding matters, not that
          the alleles differ.
        Tool evidence (no experiment record) and claims whose subject is an element, TF or gene keep the class matrix.
        The one place a link's strength is computed."""
        strength = evidence_strength(claim.relation, ev)
        x = ev.experiment
        if (x is None or strength == "context" or claim.relation not in ALLELIC_RELATIONS
                or not self._variant_subject(claim)):
            return strength, ""
        if x.manipulated in FACTOR_PERTURBATIONS:
            factor = "TF" if x.manipulated == "tf" else "gene"
            return "context", (f"a {factor} perturbation does not test what the variant's alleles do (it shows the "
                               f"{factor} matters, not that the alleles differ)")
        if ev.evidence_class == "reporter_assay" and claim.relation == "alters_regulatory_activity":
            scope = " ".join([claim.assertion_text,
                              (claim.context_scope.condition or "") if claim.context_scope else "",
                              *(self.entities[e].label for e in claim.object_ids)]).casefold()
            if "endogenous" in scope and not any(w in scope for w in ("reporter", "construct", "episomal")):
                return "indirect", ("a reporter assay does not establish endogenous regulatory activity; "
                                     "add a reporter-scoped claim and keep this broader claim unresolved")
        if (claim.relation in ALLELE_COMPARED_RELATIONS and strength == "direct" and x.manipulated != "allele"
                and not _text(ev.allele)):
            return "indirect", ("an experiment that does not compare the variant's alleles (a region deletion, a "
                                "CRISPRi of the element, a single-allele assay) shows that the element or the binding "
                                "matters, not that the alleles differ")
        return strength, ""

    def link_strength(self, claim_id: str, evidence_id: str) -> LinkStrength:
        """What a supports or contradicts link of this evidence would do for this claim: "direct" (can settle it),
        "indirect" (at most unresolved, shown as its basis) or "context" (context_only links only). The graph's own
        rule (_strength), for packets that show what a link can do before it is proposed; a KeyError for an unknown
        id."""
        return self._strength(self.claims[claim_id], self.evidence[evidence_id])[0]

    def _placed_direction(self, claim: Claim, ev: Evidence) -> str:
        """The evidence's direction read in the claim's allele frame: flipped when the evidence names the claim's
        other allele. Refused when the evidence names an allele the case variant does not have, or reports a
        direction without naming the allele it refers to while the claim states a direction (a claim of no change
        is met by any direction, so it needs no allele)."""
        frame = self._claim_frame(claim)
        if frame == "case" and ev.allele:
            side = self._allele_side(ev.allele)
            if side is None:
                v = self.case.variant
                raise GraphRefusal(f"{ev.evidence_id} is about allele {ev.allele}, which is neither ref {v.ref} nor "
                                   f"alt {v.alt} of the case variant")
            return ev.direction if side == self._allele_side(claim.effect_allele) else FLIP.get(ev.direction,
                                                                                                ev.direction)
        if frame is None or ev.direction not in SPECIFIC_DIRECTIONS or claim.direction not in SPECIFIC_DIRECTIONS:
            return ev.direction
        if frame == "other" and claim.effect_allele and _allele_token(ev.allele) == claim.effect_allele:
            return ev.direction
        raise GraphRefusal(f"{ev.evidence_id} reports '{ev.direction}' but its allele "
                           f"({ev.allele or 'not stated'}) cannot be placed in {claim.claim_id}'s allele frame "
                           f"(effect allele {claim.effect_allele or 'not stated'}): state which allele the direction "
                           "refers to, or link it as context_only")

    @staticmethod
    def _check_direction(claim: Claim, ev: Evidence, stance: Stance, placed: str) -> None:
        """An observed effect supports only a matching (or unstated) direction and contradicts only a different one:
        the opposite sign, or a claim of no change. Agreement can never be linked as a contradiction."""
        if ev.result_kind != "effect":
            return
        c, e = _sign(claim.direction), _sign(placed)
        where = "" if placed == ev.direction else " (read for the claim's effect allele)"
        if stance == "supports":
            if c == 0:
                raise GraphRefusal(f"{claim.claim_id} claims no change; an observed effect ({ev.evidence_id}) can "
                                   "contradict it, never support it")
            if c and e and c != e:
                raise GraphRefusal(f"{ev.evidence_id} observed '{placed}'{where}, opposite to the claim's "
                                   f"'{claim.direction}': it can contradict this claim, never support it")
        elif stance == "contradicts" and c != 0:
            if c is None:
                raise GraphRefusal(f"{claim.claim_id} states no direction: an observed effect contradicts only a claim "
                                   "of the opposite direction or of no change (an observed absence of effect is a "
                                   "measured null)")
            if e is None:
                raise GraphRefusal(f"{ev.evidence_id} states no direction, so it cannot contradict "
                                   f"{claim.claim_id}'s '{claim.direction}'")
            if c == e:
                raise GraphRefusal(f"{ev.evidence_id} observed '{placed}'{where}, as {claim.claim_id} claims: it "
                                   "agrees with the claim and cannot contradict it")

    @staticmethod
    def _check_null(claim: Claim, ev: Evidence, stance: Stance, applicability: str, rationale: str) -> None:
        if ev.result_kind != "null_in_assessed_scope":
            return
        if stance == "supports":
            if claim.direction != "no_change":
                raise GraphRefusal(f"{ev.evidence_id} is a measured null: it cannot support a claim of an effect")
            return
        if claim.direction == "no_change":
            raise GraphRefusal(f"{ev.evidence_id} is a measured null, which agrees with {claim.claim_id}'s claim of no "
                               "change")
        if applicability != "exact":
            raise GraphRefusal(f"{ev.evidence_id} is a measured null: it contradicts only in an exact scope (this "
                               f"link is {applicability})")
        if ev.assessed_relation != claim.relation:
            raise GraphRefusal(f"{ev.evidence_id} is a null for {ev.assessed_relation}, not {claim.relation}")
        if not _text(rationale):
            raise GraphRefusal("a measured null used as a contradiction needs an explicit rationale")

    def _homozygous_readout(self, claim: Claim, ev: Evidence) -> str | None:
        """The genotype, when an allele-resolved readout of the endogenous alleles comes from a context homozygous at
        the case variant and the claim compares that variant's alleles (it cannot show a difference there)."""
        if ev.data.get("allele_specific") is not True or ev.context is None or not _homozygous(ev.context.genotype):
            return None
        if claim.relation not in ALLELIC_RELATIONS or self._claim_frame(claim) != "case":
            return None
        return ev.context.genotype

    @_atomic
    def link(self, claim_id: str, evidence_id: str, stance: Stance, role: Role, rationale: str = "",
             applicability: Applicability | None = None, limitations: Sequence[str] = ()) -> EvidenceLink:
        """Attach evidence to a claim after the class-matrix, identity, variant, allele-frame, direction, null and
        context checks. Code computes applicability; a stronger proposed value is corrected (corrected=True), a weaker
        match the proposer names (proxy, different) is kept, and a proposed "unknown" states no judgement, so code's
        exact or proxy is stored (the link's event says so), except on a contradicts link, where it is kept and
        withholds the contradiction until a link confirms the scope. A supports/contradicts link in a different
        context, or from an allele-resolved readout in a homozygous context, is stored as context_only. Linking
        evidence that is already linked replaces the earlier link (the event names it) when the stance or
        applicability changes. Every link bumps the claim's version; a held assessment the new links no longer meet is
        reset to unresolved by code. context_only links pass every identity and variant check: they record what was
        read, never what it shows."""
        claim = self._live_claim(claim_id)
        ev = self.evidence.get(evidence_id)
        if ev is None:
            raise GraphRefusal(f"unknown evidence {evidence_id}")
        if ev.evidence_class == "synthetic" and not self.case.synthetic:
            raise GraphRefusal("synthetic evidence may link only in a synthetic case (SYN-)")
        strength, narrowed = self._strength(claim, ev)
        context_free = ev.evidence_class in CONTEXT_FREE_CLASSES and ev.result_kind == "effect"
        code = link_applicability(claim.context_scope, ev.context, context_free=context_free)
        # A proposed "unknown" states no judgement about the two contexts, so it cannot weaken a match code computed;
        # a proposer weakens a match by naming the weaker one (proxy or different). The exception is a contradiction:
        # there "unknown" withholds it (a contradiction can reject a hypothesis) until a link confirms the scope.
        no_judgement = applicability == "unknown" and code in ("exact", "proxy") and stance != "contradicts"
        proposed = None if no_judgement else applicability
        corrected = proposed is not None and APPLICABILITY_RANK[proposed] > APPLICABILITY_RANK[code]
        stored = code if proposed is None or corrected else proposed
        final, downgraded = stance, None
        notes = [f"applicability corrected from {applicability} to {code}"] if corrected else []
        if no_judgement:
            notes.append(f"the proposed applicability 'unknown' states no judgement: code's '{code}' is stored")
        if stance in ("supports", "contradicts"):
            if strength == "context":
                if ev.experiment is not None and ev.experiment.authors_hypothesis_vs_result == "hypothesis":
                    raise GraphRefusal(f"{evidence_id} states the authors' hypothesis, not a result; link it as "
                                       "context_only")
                if narrowed:
                    raise GraphRefusal(f"{evidence_id} cannot {stance[:-1]} {claim_id}: {narrowed}; link it as "
                                       "context_only")
                allowed = sorted(DIRECT.get(claim.relation, set()))
                raise GraphRefusal(f"{ev.evidence_class} evidence cannot {stance[:-1]} a {claim.relation} claim "
                                   f"(classes that can: {', '.join(allowed) or 'see the class matrix'}); link it as "
                                   "context_only")
            notes += self._check_identity(claim, ev, rationale)
            self._check_variants(claim, ev)
            if narrowed:
                notes.append(f"indirect: {narrowed}")
            self._check_direction(claim, ev, stance, self._placed_direction(claim, ev))
            self._check_null(claim, ev, stance, stored, rationale)
            if stored == "different":
                final, downgraded = "context_only", stance
                notes.append(f"stored as context_only: the evidence context is different ({stance} proposed)")
            elif genotype := self._homozygous_readout(claim, ev):
                final, downgraded = "context_only", stance
                notes.append(f"stored as context_only: an allele-resolved readout from a context homozygous "
                             f"({genotype}) at the variant cannot compare its alleles ({stance} proposed)")
        prior = next((x for x in claim.evidence_links if x.evidence_id == evidence_id), None)
        if prior is not None and (prior.stance, prior.applicability) == (final, stored):
            self.log("decide", role, f"{evidence_id} is already linked to {claim_id}; retained unchanged",
                        target_ids=[claim_id], evidence_ids=[evidence_id], details={"idempotent_link": True})
            return prior
        if prior is not None:
            notes.append(f"replaces the {prior.stance} ({prior.applicability}) link of {prior.event_id}")
        link = EvidenceLink(claim_id=claim_id, evidence_id=evidence_id, stance=final, applicability=stored,
                            rationale=_text(rationale), limitations=list(limitations), proposed_by=role,
                            code_applicability=code, corrected=corrected,
                            strength=strength if final in ("supports", "contradicts") else "context",
                            downgraded_from=downgraded, revises=prior.event_id if prior else None)
        if prior is None:
            claim.evidence_links.append(link)
        else:
            claim.evidence_links[claim.evidence_links.index(prior)] = link
        event = self._event("attach_evidence", role, rationale or "; ".join(notes) or f"{final} link",
                            targets=[claim_id], evidence=[evidence_id], supersedes=[prior.event_id] if prior else [],
                            details={"stance": final, "applicability": stored, "code_applicability": code,
                                     "corrected": corrected, "strength": link.strength, "downgraded_from": downgraded,
                                     "revises": link.revises, "claim_version": claim.version + 1, "notes": notes})
        link.event_id = event.event_id
        claim.version += 1
        claim.history.append(ClaimHistoryEntry(version=claim.version, assessment=claim.assessment,
                                               event_id=event.event_id, action="attach_evidence",
                                               rationale=f"{evidence_id} linked as {final} ({stored})"))
        self._recheck(claim, f"after {evidence_id} was linked as {final}")
        return link

    # --- assessment --------------------------------------------------------------------------------------------------

    def _gate_problem(self, claim: Claim, assessment: Assessment) -> str | None:
        """Why the claim's current links do not allow this assessment, or None when they do."""
        links = claim.evidence_links

        def direct(stance: str) -> list[str]:
            return [x.evidence_id for x in links
                    if x.stance == stance and x.strength == "direct" and x.applicability in ("exact", "proxy")]

        allowed = ", ".join(sorted(DIRECT.get(claim.relation, set()))) or "none without a qualifier"
        pro, con = direct("supports"), direct("contradicts")
        if assessment == "supported_in_scope":
            if not pro:
                indirect = sorted({self.evidence[x.evidence_id].evidence_class for x in links
                                   if x.stance == "supports" and x.strength == "indirect"})
                hint = f"; its support is indirect ({', '.join(indirect)}), so it stays unresolved" if indirect else ""
                if set(indirect) & DIRECT.get(claim.relation, set()):
                    hint += (" (an experiment that does not compare the variant's alleles counts as indirect for a "
                             "claim that they differ)")
                return (f"supported_in_scope needs a supports link with exact or proxy applicability from a class that "
                        f"can establish {claim.relation} ({allowed}){hint}")
            if con:
                return (f"{', '.join(con)} contradict {claim.claim_id} directly while {', '.join(pro)} support it: the "
                        "claim is contested, not supported")
        if assessment == "contradicted_in_scope":
            if not con:
                return (f"contradicted_in_scope needs a contradicts link with exact or proxy applicability from a "
                        f"class that can establish {claim.relation} ({allowed}); missing or indirect evidence never "
                        "contradicts")
            if pro:
                return (f"{', '.join(pro)} support {claim.claim_id} directly while {', '.join(con)} contradict it: the "
                        "claim is contested, not contradicted")
        if assessment == "contested":
            usable = [x for x in links if x.applicability != "different" and x.strength in ("direct", "indirect")]
            sides = {x.stance for x in usable}
            if not {"supports", "contradicts"} <= sides or not any(x.strength == "direct" for x in usable):
                return ("contested needs a supports and a contradicts link (not in a different context), at least one "
                        "of them from a direct class")
        return None

    def _set_assessment(self, claim: Claim, assessment: Assessment, rationale: str, role: Role,
                        details: dict[str, Any]) -> None:
        """Apply an assessment that passed its gate; a contradiction rejects every open hypothesis requiring the
        claim at once (role code), so nothing later in a batch can repair the contradiction away."""
        before = claim.assessment
        claim.assessment, claim.assessment_rationale = assessment, _text(rationale)
        claim.version += 1
        decisive = [x.evidence_id for x in claim.evidence_links if x.stance in ("supports", "contradicts")]
        event = self._event("assess", role, rationale, targets=[claim.claim_id], evidence=decisive,
                            details={"from": before, "to": assessment, "claim_version": claim.version, **details})
        claim.history.append(ClaimHistoryEntry(version=claim.version, assessment=assessment, event_id=event.event_id,
                                               action="assess", rationale=claim.assessment_rationale))
        if assessment == "contradicted_in_scope":
            self._reject_contradicted(h for h in self.hypotheses.values() if claim.claim_id in h.required_claim_ids)

    def _recheck(self, claim: Claim, cause: str) -> None:
        """A held assessment must always meet its gate on the claim's current links; when a link breaks that (direct
        evidence on the other side, or a revised link), code resets the claim to unresolved for reassessment."""
        if claim.assessment in ("unassessed", "unresolved"):
            return
        if problem := self._gate_problem(claim, claim.assessment):
            self._set_assessment(claim, "unresolved", f"{claim.assessment} no longer holds {cause}: {problem}", "code",
                                 {"automatic": True})

    @_atomic
    def assess(self, claim_id: str, assessment: Assessment, rationale: str, role: Role, base_version: int,
               suggested_by: Role | None = None) -> int:
        """Set a claim's assessment through the evidence gates; returns the claim's new version. base_version must be
        the claim's current version (optimistic concurrency: every link and assessment bumps it). Only the
        coordinator, the critic or code assess; an investigator's suggestion is applied by code through the same gate
        (suggested_by records whose it was). contradicted_in_scope rejects the hypotheses that require the claim."""
        claim = self._live_claim(claim_id)
        if role not in ASSESSORS:
            raise GraphRefusal("investigators suggest assessments; the engine applies them through the same gate")
        if base_version != claim.version:
            raise GraphRefusal(f"stale update: {claim_id} is at version {claim.version}, the proposal was based on "
                               f"version {base_version}; re-read the claim")
        if assessment == "unassessed":
            raise GraphRefusal("unassessed is only a claim's initial value")
        if not _text(rationale):
            raise GraphRefusal("an assessment needs a rationale")
        if problem := self._gate_problem(claim, assessment):
            raise GraphRefusal(problem)
        self._set_assessment(claim, assessment, rationale, role,
                             {"base_version": base_version, "suggested_by": suggested_by})
        return claim.version

    def display(self, claim_id: str) -> ClaimDisplay:
        """The report's status for a claim: assessment paired with its basis (SPEC 2, 13.6). Derived, never stored."""
        return display_of(self.claims[claim_id], self.evidence)

    def display_status(self, claim_id: str) -> str:
        return self.display(claim_id).status

    # --- hypotheses --------------------------------------------------------------------------------------------------

    def _open_hypothesis(self, hid: str) -> Hypothesis:
        h = self.hypotheses.get(hid)
        if h is None:
            raise GraphRefusal(f"unknown hypothesis {hid}")
        if h.disposition in FINAL:
            raise GraphRefusal(f"{hid} is {h.disposition}, which is final; propose a regenerated hypothesis instead")
        return h

    def _check_required(self, required: Sequence[str]) -> None:
        if not required:
            raise GraphRefusal("a hypothesis needs at least one required claim")
        for cid in required:
            relation = self.claims[cid].relation
            if relation not in REQUIRABLE:
                raise GraphRefusal(f"{cid} ({relation}) cannot be a required claim: expression and occupancy can "
                                   "defer a hypothesis but never reject it; keep it as an optional claim")

    def _check_newly_required(self, added: Iterable[str]) -> None:
        """A claim already contradicted in scope cannot become required: the hypothesis would exist only to be
        rejected, and a contradiction must never be moved between hypotheses to make one fall."""
        for cid in added:
            if self.claims[cid].assessment == "contradicted_in_scope":
                raise GraphRefusal(f"{cid} is contradicted_in_scope, so it cannot become a required claim; propose a "
                                   "materially different claim")

    def signature(self, mechanism_class: str, required_claim_ids: Sequence[str]) -> str:
        """Exact scoped identity, separate from related families. Claims are already deduplicated by participants,
        relation, allele frame and context. Their stable ids preserve phenotype/element identities and all required
        links, without letting wording or a subsequently added canonical id disguise an identical rejected claim."""
        return f"scoped:{mechanism_class}|required={','.join(sorted(set(required_claim_ids)))}"

    def hypothesis_signature(self, h: Hypothesis) -> str:
        # Older snapshots carry the former coarse signature. Read them without rewriting their history.
        return self.signature(h.mechanism_class, h.required_claim_ids)

    def scope_views(self) -> dict[str, list[dict[str, Any]]]:
        from .scope_graph import claim_refinements, hypothesis_families

        refinements = claim_refinements(self)
        return {"claim_refinements": refinements, "hypothesis_families": hypothesis_families(self, refinements)}

    def _check_not_rejected(self, signature: str, exclude: str | None = None) -> None:
        for h in self.hypotheses.values():
            if h.disposition == "rejected" and self.hypothesis_signature(h) == signature and h.hypothesis_id != exclude:
                raise GraphRefusal(f"this repeats rejected hypothesis {h.hypothesis_id} (same structure: {signature}); "
                                   "propose a structurally different alternative")

    def _current(self, claim_id: str) -> str:
        """The claim a supersession chain leads to (the claim itself when it was never superseded)."""
        while (nxt := self.claims[claim_id].superseded_by) is not None:
            claim_id = nxt
        return claim_id

    def _path_status(self, h: Hypothesis) -> dict[str, PathStatus]:
        out: dict[str, PathStatus] = {}
        for cid in h.claim_ids:
            claim = self.claims[cid]
            out[cid] = ("superseded" if claim.superseded_by
                        else "premise_failed" if claim.dependency_flag != "none" else "intact")
        return out

    def _shared(self, claim_ids: Iterable[str], hid: str) -> dict[str, list[str]]:
        out = {cid: [o.hypothesis_id for o in self.hypotheses.values()
                     if o.hypothesis_id != hid and cid in o.claim_ids] for cid in claim_ids}
        return {k: v for k, v in out.items() if v}

    @_atomic
    def add_hypothesis(self, draft: HypothesisDraft, role: Role) -> str:
        """Add a hypothesis. Refused when a required claim cannot be required, when deferral lacks a reason and
        trigger, or when its signature repeats a rejected hypothesis. A draft whose signature equals an open
        hypothesis is merged: the existing id is returned. With `replaces`, an open replaced hypothesis becomes
        superseded, which is final, so the replacement must keep each of its required claims (or the claim that
        superseded it) as required: only a contradiction (rejection) eliminates a viable story."""
        claim_ids = list(dict.fromkeys(draft.claim_ids + draft.required_claim_ids))
        required = list(dict.fromkeys(draft.required_claim_ids))
        for cid in claim_ids:
            self._live_claim(cid)
        self._check_required(required)
        if draft.disposition == "deferred" and not (_text(draft.disposition_reason) and _text(draft.revisit_trigger)):
            raise GraphRefusal("a deferred hypothesis needs a reason and a revisit trigger")
        if draft.replaces and draft.replaces not in self.hypotheses:
            raise GraphRefusal(f"unknown hypothesis {draft.replaces}")
        sig = self.signature(draft.mechanism_class, required)
        self._check_not_rejected(sig)
        self._check_newly_required(required)
        if same := next((h.hypothesis_id for h in self.hypotheses.values()
                         if self.hypothesis_signature(h) == sig and h.disposition not in FINAL), None):
            existing = self.hypotheses[same]
            added = [c for c in claim_ids if c not in existing.claim_ids]
            if added:
                self.revise_hypothesis(same, HypothesisChanges(add_claim_ids=added),
                                       "same scoped required claims; retained additional optional claims", role)
            self.log("decide", role, f"reused {same}: identical scoped required claims; retained all proposed claims",
                        target_ids=[same, *claim_ids], details={"merge": True, "added_claim_ids": added})
            return same
        replaced = self.hypotheses[draft.replaces] if draft.replaces else None
        if replaced is not None and replaced.disposition not in FINAL:
            dropped = [c for c in replaced.required_claim_ids if self._current(c) not in required]
            if dropped:
                raise GraphRefusal(f"this would retire {replaced.hypothesis_id} without a contradicted required claim: "
                                   f"it drops {', '.join(dropped)}. Keep them required, revise "
                                   f"{replaced.hypothesis_id} instead, or defer it")
        hid = self._next("H")
        h = Hypothesis(hypothesis_id=hid, title=_text(draft.title), summary=draft.summary, claim_ids=claim_ids,
                       required_claim_ids=required, assumptions=list(draft.assumptions),
                       context=normalise_scope(draft.context, variant=self.case.variant),
                       endpoint=draft.endpoint, mechanism_class=draft.mechanism_class, disposition=draft.disposition,
                       disposition_reason=_text(draft.disposition_reason),
                       revisit_trigger=_text(draft.revisit_trigger) or None, origin=draft.origin,
                       replaces=draft.replaces, member_alternatives=list(draft.member_alternatives),
                       missing_links=list(draft.missing_links), reason_for_inclusion=draft.reason_for_inclusion,
                       signature=sig)
        h.path_status = self._path_status(h)
        self.hypotheses[hid] = h
        action: EventAction = "regenerate" if draft.origin == "regenerated" else "propose"
        event = self._event(action, role, draft.reason_for_inclusion or h.title, targets=[hid, *claim_ids],
                            details={"signature": sig, "disposition": h.disposition, "required": required,
                                     "shared_claims": self._shared(claim_ids, hid), "replaces": draft.replaces})
        h.history.append({"kind": "created", "version": 1, "event_id": event.event_id, "disposition": h.disposition})
        if replaced is not None and replaced.disposition not in FINAL:
            self._set_disposition(replaced, "superseded", f"replaced by {hid}", role)
        return hid

    def _revised(self, h: Hypothesis, changes: HypothesisChanges) -> dict[str, Any]:
        claim_ids, required = list(h.claim_ids), list(h.required_claim_ids)
        for old, new in changes.replace_claims.items():
            if old not in claim_ids:
                raise GraphRefusal(f"{old} is not a claim of {h.hypothesis_id}")
            self._live_claim(new)
            claim_ids = list(dict.fromkeys(new if c == old else c for c in claim_ids))
            required = list(dict.fromkeys(new if c == old else c for c in required))
        for cid in changes.remove_claim_ids:
            if cid not in claim_ids:
                raise GraphRefusal(f"{cid} is not a claim of {h.hypothesis_id}")
            claim_ids = [c for c in claim_ids if c != cid]
            required = [c for c in required if c != cid]
        for cid in changes.add_claim_ids + changes.add_required_claim_ids:
            self._live_claim(cid)
            if cid not in claim_ids:
                claim_ids.append(cid)
        required += [c for c in changes.add_required_claim_ids if c not in required]
        self._check_required(required)
        fields = {k: v for k, v in changes.model_dump(exclude_none=True).items()
                  if k not in ("add_claim_ids", "add_required_claim_ids", "remove_claim_ids", "replace_claims")}
        if changes.context is not None:
            fields["context"] = normalise_scope(changes.context, variant=self.case.variant)
        fields.update(claim_ids=claim_ids, required_claim_ids=required)
        fields["signature"] = self.signature(fields.get("mechanism_class", h.mechanism_class), required)
        self._check_not_rejected(fields["signature"], exclude=h.hypothesis_id)
        self._check_newly_required(c for c in required if c not in h.required_claim_ids)
        return fields

    @_atomic
    def revise_hypothesis(self, hid: str, changes: HypothesisChanges, reason: str, role: Role) -> int:
        """A new version of an open hypothesis (the previous one is kept in history); returns the new version.
        Replacing a required claim keeps every other claim (local repair)."""
        h = self._open_hypothesis(hid)
        if not _text(reason):
            raise GraphRefusal("a revision needs a reason")
        fields = self._revised(h, changes)
        current = {k: getattr(h, k) for k in fields}
        if fields == current:
            raise GraphRefusal(f"the revision changes nothing in {hid}")
        previous = h.model_dump(mode="json", exclude={"history", "path_status"})
        for k, v in fields.items():
            setattr(h, k, v)
        h.version += 1
        h.path_status = self._path_status(h)
        added = [c for c in h.claim_ids if c not in previous["claim_ids"]]
        event = self._event("revise_hypothesis", role, reason, targets=[hid, *added, *changes.replace_claims],
                            supersedes=list(changes.replace_claims),
                            details={"version": h.version, "replaced": changes.replace_claims,
                                     "added": added, "removed": [c for c in previous["claim_ids"]
                                                                 if c not in h.claim_ids],
                                     "shared_claims": self._shared(added, hid)})
        h.history.append({"kind": "revision", "version": h.version, "event_id": event.event_id,
                          "reason": _text(reason), "previous": previous})
        return h.version

    def add_claim_to_hypothesis(self, hid: str, claim_id: str, required: bool, reason: str, role: Role) -> int:
        """Add a (possibly shared) claim to a hypothesis, optionally as required; returns the new version."""
        h = self._open_hypothesis(hid)
        if claim_id in h.claim_ids and (not required or claim_id in h.required_claim_ids):
            raise GraphRefusal(f"{claim_id} is already a{' required' if required else ''} claim of {hid}")
        changes = (HypothesisChanges(add_required_claim_ids=[claim_id]) if required
                   else HypothesisChanges(add_claim_ids=[claim_id]))
        return self.revise_hypothesis(hid, changes, reason or f"add {claim_id}", role)

    def replace_required_claim(self, hid: str, old_claim_id: str, new_claim_id: str, reason: str, role: Role) -> int:
        """Local repair: swap one required claim, keeping every other claim and its evidence."""
        h = self._open_hypothesis(hid)
        if old_claim_id not in h.required_claim_ids:
            raise GraphRefusal(f"{old_claim_id} is not a required claim of {hid}")
        return self.revise_hypothesis(hid, HypothesisChanges(replace_claims={old_claim_id: new_claim_id}), reason,
                                      role)

    @_atomic
    def supersede_claim(self, old_id: str, draft: ClaimDraft, reason: str, role: Role,
                        hypothesis_ids: Sequence[str] = ()) -> str:
        """Replace a claim by a materially different one (another TF, direction, target or context). Links are not
        copied: each must be re-linked and re-checked, so TF-A evidence never moves to TF-B silently. The old claim and
        its links stay. Hypotheses named here swap the old claim for the new one (each a new version)."""
        old = self._live_claim(old_id)
        if not _text(reason):
            raise GraphRefusal("a supersession needs a reason")
        if old_id in draft.dependencies:
            raise GraphRefusal(f"the replacement cannot depend on the claim it supersedes ({old_id})")
        for hid in hypothesis_ids:
            if old_id not in self._open_hypothesis(hid).claim_ids:
                raise GraphRefusal(f"{old_id} is not a claim of {hid}")
        new_id, created, _ = self._add_claim(draft, role, reason)
        if new_id == old_id:
            raise GraphRefusal(f"the replacement is the same proposition as {old_id}; a supersession needs a material "
                               "change (TF, direction, target or context)")
        new = self.claims[new_id]
        if new.supersedes is None:
            new.supersedes = old_id
        old.superseded_by = new_id
        self._event("supersede_claim", role, reason, targets=[old_id, new_id], supersedes=[old_id],
                    details={"reused_existing_claim": not created, "links_copied": 0})
        for hid in hypothesis_ids:
            self.revise_hypothesis(hid, HypothesisChanges(replace_claims={old_id: new_id}), reason, role)
        return new_id

    def _contradicted_required(self, h: Hypothesis) -> list[str]:
        return [c for c in h.required_claim_ids if self.claims[c].assessment == "contradicted_in_scope"]

    def _reject_contradicted(self, hypotheses: Iterable[Hypothesis]) -> None:
        """Reject (role code) each open hypothesis with a contradicted_in_scope required claim, naming the claim and
        the direct contradicting evidence. The event's details record the rule and the claims (REJECTION_RULE), which
        is what reinstate() reads when such a contradiction is later withdrawn."""
        for h in list(hypotheses):
            bad = self._contradicted_required(h) if h.disposition not in FINAL else []
            if bad:
                ev_ids = list(dict.fromkeys(x.evidence_id for c in bad for x in self.claims[c].evidence_links
                                            if x.stance == "contradicts" and x.strength == "direct"
                                            and x.applicability in ("exact", "proxy")))
                self._set_disposition(h, "rejected", f"required claim {', '.join(bad)} contradicted in scope "
                                                     f"(evidence {', '.join(ev_ids)})", "code", evidence_ids=ev_ids,
                                      details={"rule": REJECTION_RULE, "claims": bad})

    def _set_disposition(self, h: Hypothesis, disposition: Disposition, reason: str, role: Role,
                         revisit_trigger: str | None = None, evidence_ids: Sequence[str] = (),
                         details: Mapping[str, Any] | None = None) -> None:
        before = h.disposition
        h.disposition, h.disposition_reason = disposition, _text(reason)
        h.revisit_trigger = (_text(revisit_trigger) or None) if disposition == "deferred" else None
        event = self._event(DISPOSITION_ACTION[disposition], role, reason, targets=[h.hypothesis_id],
                            evidence=evidence_ids, details={"from": before, "to": disposition,
                                                            "revisit_trigger": h.revisit_trigger, **(details or {})})
        h.history.append({"kind": "disposition", "version": h.version, "event_id": event.event_id, "from": before,
                          "to": disposition, "reason": h.disposition_reason})

    def _rule_rejection(self, h: Hypothesis) -> tuple[DecisionEvent | None, list[str]]:
        """The event of a rejected hypothesis's rejection and the claims it rested on, when code made it through the
        contradicted-required-claim rule (its details name the rule; a graph written before they did is read by its
        reason); (None, []) for a rejection made any other way (a coordinator's, a critic's, a code
        set_disposition)."""
        entry = next((x for x in reversed(h.history) if x.get("kind") == "disposition" and x.get("to") == "rejected"),
                     None)
        event = next((e for e in reversed(self.events) if entry and e.event_id == entry.get("event_id")), None)
        if event is None or event.role != "code" or event.action != "reject":
            return None, []
        if "rule" in event.details:
            claims = event.details.get("claims") if event.details["rule"] == REJECTION_RULE else None
            return (event, [str(c) for c in claims]) if isinstance(claims, list) and claims else (None, [])
        if m := RULE_REASON.match(event.concise_reason):
            return event, m.group(1).split(", ")
        return None, []

    @_atomic
    def reinstate(self, hid: str, reason: str, role: Role = "code") -> bool:
        """Undo a code rejection whose contradiction no longer stands: the one way out of a final disposition (FINAL).

        Code rejects a hypothesis when a required claim is assessed contradicted_in_scope. A later reassessment, or a
        replaced link that reset the claim to unresolved, can withdraw that contradiction, and a rejection with no
        basis must not stand; nor may a story oscillate, so a hypothesis is reinstated at most once and a second
        rejection is final.

        Refused (GraphRefusal): a role other than code; an unknown hypothesis; one that is not rejected; a rejection
        code did not make through the contradicted-required-claim rule (a coordinator's or critic's rejection, or a
        code set_disposition, stays final). Returns False and changes nothing when a required claim is still
        contradicted_in_scope, when the hypothesis was already reinstated once, or when an open hypothesis has the
        same signature (the story is already open). Otherwise the hypothesis becomes deferred, with the reason and a
        revisit trigger naming the claims whose contradiction was withdrawn; its history gains {"kind":
        "reinstatement", "from": "rejected", "to": "deferred", "rejected_by": <the rejecting event>, "claims": [...],
        ...}, and a "reinstate" event (role code) records it. The anti-repeat block lifts by itself (the hypothesis is
        no longer rejected). Returns True."""
        if role != "code":
            raise GraphRefusal(f"only code reinstates a rejected hypothesis (when the contradiction it rested on was "
                               f"withdrawn), not the {role.replace('_', ' ')}")
        h = self.hypotheses.get(hid)
        if h is None:
            raise GraphRefusal(f"unknown hypothesis {hid}")
        if h.disposition != "rejected":
            raise GraphRefusal(f"{hid} is {h.disposition}, not rejected: only a rejected hypothesis is reinstated")
        rejection, claims = self._rule_rejection(h)
        if rejection is None:
            raise GraphRefusal(f"{hid} was not rejected by code for a contradicted required claim: that rejection is "
                               "final")
        if (self._contradicted_required(h) or any(x.get("kind") == "reinstatement" for x in h.history)
                or any(self.hypothesis_signature(o) == self.hypothesis_signature(h) and o.disposition not in FINAL
                       for o in self.hypotheses.values())):
            return False
        named = ", ".join(claims)
        why = _text(reason) or f"the contradiction of {named} that rejected {hid} was withdrawn"
        trigger = (f"new direct evidence on {named}, or its reassessment: the contradiction that rejected {hid} "
                   f"({rejection.event_id}) was withdrawn")
        h.disposition, h.disposition_reason, h.revisit_trigger = "deferred", why, trigger
        event = self._event("reinstate", "code", why, targets=[hid, *claims],
                            details={"from": "rejected", "to": "deferred", "rejected_by": rejection.event_id,
                                     "claims": claims, "revisit_trigger": trigger})
        h.history.append({"kind": "reinstatement", "version": h.version, "event_id": event.event_id,
                          "from": "rejected", "to": "deferred", "reason": why, "rejected_by": rejection.event_id,
                          "claims": claims})
        return True

    @_atomic
    def set_disposition(self, hid: str, disposition: Disposition, reason: str, role: Role,
                        revisit_trigger: str | None = None) -> None:
        """rejected needs a contradicted_in_scope required claim (else: defer instead); deferred needs a reason and a
        revisit trigger; leading and tied come only from the comparison step (role code); superseded needs a
        hypothesis that replaces this one. Rejected and superseded are final."""
        h = self.hypotheses.get(hid)
        if h is None:
            raise GraphRefusal(f"unknown hypothesis {hid}")
        if h.disposition in FINAL:
            raise GraphRefusal(f"{hid} is {h.disposition}, which is final; propose a regenerated hypothesis instead")
        if not _text(reason):
            raise GraphRefusal("a disposition change needs a reason")
        if disposition == h.disposition:
            raise GraphRefusal(f"{hid} is already {disposition}")
        if disposition == "rejected" and not self._contradicted_required(h):
            raise GraphRefusal(f"{hid} has no contradicted_in_scope required claim, so it cannot be rejected; defer it "
                               "instead, with a reason and a revisit trigger")
        if disposition == "deferred" and not _text(revisit_trigger):
            raise GraphRefusal("deferring needs a reason and a revisit trigger")
        if disposition in ("leading", "tied") and role != "code":
            raise GraphRefusal("leading and tied are set only by the comparison step (compare.py)")
        if disposition == "superseded" and not any(o.replaces == hid for o in self.hypotheses.values()):
            raise GraphRefusal(f"{hid} can be superseded only by a hypothesis that replaces it")
        self._set_disposition(h, disposition, reason, role, revisit_trigger)

    # --- dependencies ------------------------------------------------------------------------------------------------

    def _premise_failed(self, claim_id: str, flags: dict[str, str]) -> bool:
        """A premise fails when it (or the replacement it was superseded by) is contradicted in scope or is itself
        flagged; a supersession without a named replacement also fails it."""
        seen: set[str] = set()
        current: str | None = claim_id
        while current is not None and current not in seen:
            seen.add(current)
            claim = self.claims[current]
            if claim.assessment == "contradicted_in_scope" or flags.get(current, "none") != "none":
                return True
            current = claim.superseded_by
        return current is not None          # a cycle of supersessions names no usable replacement

    def propagate(self) -> list[str]:
        """Recompute dependency flags and hypothesis paths; one propagate event (role code) when anything changed.
        Assessments never change here, and rejection is not done here: a hypothesis is rejected when its required
        claim is assessed contradicted_in_scope. Idempotent. Returns the new event ids."""
        start = len(self.events)
        flags = {cid: "none" for cid in self.claims}
        broken: dict[str, list[str]] = {}
        changed = True
        while changed:                       # dependencies point to earlier claims; a few passes settle it
            changed = False
            for cid, claim in self.claims.items():
                if flags[cid] == "none":
                    failed = [d for d in claim.dependencies if self._premise_failed(d, flags)]
                    if failed:
                        flags[cid], broken[cid], changed = "unsupported_due_to_dependency", failed, True
        flagged = {cid: broken[cid] for cid in self.claims
                   if flags[cid] != "none" and self.claims[cid].dependency_flag == "none"}
        cleared = [cid for cid in self.claims if flags[cid] == "none" and self.claims[cid].dependency_flag != "none"]
        for cid, claim in self.claims.items():
            claim.dependency_flag = flags[cid]
        paths: dict[str, dict[str, str]] = {}
        for h in self.hypotheses.values():
            new = self._path_status(h)
            if new != h.path_status:
                paths[h.hypothesis_id] = {k: v for k, v in new.items() if v != "intact"}
                h.path_status = new
        if flagged or cleared or paths:
            reason = "; ".join(f"{cid}: premise {', '.join(deps)} failed" for cid, deps in flagged.items())
            self._event("propagate", "code", reason or "dependency flags updated",
                        targets=[*flagged, *cleared, *paths],
                        details={"flagged": flagged, "cleared": cleared, "path_status": paths})
        return [e.event_id for e in self.events[start:]]

    # --- questions, comparisons, result ------------------------------------------------------------------------------

    @_atomic
    def add_question(self, question: Question, role: Role) -> str:
        """Store an open question (question_id ''), returning its Q#."""
        if question.question_id:
            raise GraphRefusal("question ids are issued by the graph; pass question_id=''")
        for cid in question.target_claim_ids:
            if cid not in self.claims:
                raise GraphRefusal(f"unknown claim {cid}")
        for hid in question.hypothesis_ids:
            if hid not in self.hypotheses:
                raise GraphRefusal(f"unknown hypothesis {hid}")
        qid = self._next("Q")
        self.questions[qid] = question.model_copy(update={"question_id": qid})
        self._event("ask", role, question.text, targets=[qid, *question.target_claim_ids, *question.hypothesis_ids],
                    details={"route": question.route, "actions": [a.model_dump(mode="json") for a in question.actions]})
        return qid

    @_atomic
    def update_question(self, question_id: str, status: QuestionStatus, role: Role, answer_summary: str = "",
                        remaining_gap: str = "") -> None:
        """Record a question's status (answered, unanswerable, deferred, refused) and what remains open."""
        q = self.questions.get(question_id)
        if q is None:
            raise GraphRefusal(f"unknown question {question_id}")
        if status not in get_args(QuestionStatus):
            raise GraphRefusal(f"unknown question status {status!r}")
        self.questions[question_id] = q.model_copy(update={"status": status, "answer_summary": _text(answer_summary),
                                                           "remaining_gap": _text(remaining_gap)})
        self._event("ask", role, answer_summary or f"{question_id} {status}", targets=[question_id],
                    details={"status": status, "remaining_gap": remaining_gap})

    @_atomic
    def add_comparison(self, comparison: PairComparison, role: Role) -> str:
        """Store a pairwise comparison (compare.py validates it first and sets accepted/refusal_reason)."""
        if comparison.comparison_id:
            raise GraphRefusal("comparison ids are issued by the graph; pass comparison_id=''")
        for hid in (comparison.a, comparison.b):
            if hid not in self.hypotheses:
                raise GraphRefusal(f"unknown hypothesis {hid}")
        if comparison.a == comparison.b:
            raise GraphRefusal("a comparison needs two different hypotheses")
        pid = self._next("P")
        self.comparisons[pid] = comparison.model_copy(update={"comparison_id": pid})
        self._event("compare", role, comparison.reason or comparison.outcome,
                    targets=[pid, comparison.a, comparison.b, *comparison.decisive_claim_ids],
                    details={"outcome": comparison.outcome, "accepted": comparison.accepted,
                             "refusal_reason": comparison.refusal_reason})
        return pid

    @_atomic
    def set_result(self, result: RunResult, role: Role = "code") -> None:
        for hid in result.leading_ids + [w.hypothesis_id for w in result.weakest_links]:
            if hid not in self.hypotheses:
                raise GraphRefusal(f"unknown hypothesis {hid}")
        self.result = result
        self._event("decide", role, result.summary or result.outcome, targets=result.leading_ids,
                    details={"outcome": result.outcome, "stop_reason": result.stop_reason,
                             "budget_stop": result.budget_stop})

    # --- reading helpers ---------------------------------------------------------------------------------------------

    def hypotheses_with_claim(self, claim_id: str) -> list[str]:
        return [h.hypothesis_id for h in self.hypotheses.values() if claim_id in h.claim_ids]

    def links(self, claim_id: str, stance: Stance | None = None) -> list[EvidenceLink]:
        return [x for x in self.claims[claim_id].evidence_links if stance is None or x.stance == stance]

    # --- batches -----------------------------------------------------------------------------------------------------

    @staticmethod
    def _ref(value: str | None, keys: dict[str, str]) -> str | None:
        if value is None or not value.startswith(KEY_PREFIX):
            return value
        name = value[len(KEY_PREFIX):]
        if name not in keys:
            raise GraphRefusal(f"{value} names nothing created earlier in this batch")
        return keys[name]

    def _refs(self, values: Iterable[str], keys: dict[str, str]) -> list[str]:
        return [str(self._ref(v, keys)) for v in values]

    @staticmethod
    def _need(u: GraphUpdate, *names: str) -> None:
        missing = [n for n in names if getattr(u, n) in (None, "")]
        if missing:
            raise GraphRefusal(f"{u.kind} needs {', '.join(missing)}")

    def _named_claim(self, u: GraphUpdate, keys: dict[str, str]) -> str | None:
        """The existing claim an update names in claim_id, if any."""
        try:
            claim_id = self._ref(u.claim_id, keys)
        except GraphRefusal:
            return None
        return claim_id if claim_id in self.claims else None

    @_atomic
    def _apply_one(self, u: GraphUpdate, role: Role, keys: dict[str, str]) -> tuple[list[str], str]:
        if role in INVESTIGATORS:
            if u.kind not in INVESTIGATOR_KINDS:
                raise GraphRefusal(f"the {role.replace('_', ' ')} proposes evidence links, assessments and claims; "
                                   "hypothesis changes are the coordinator's")
            if (u.kind == "new_claim" and (u.hypothesis_id or u.required)) or (
                    u.kind == "supersede_claim" and u.hypothesis_ids):
                raise GraphRefusal(f"the {role.replace('_', ' ')} proposes claims; adding a claim to a hypothesis, "
                                   "making it required or swapping it into a hypothesis is the coordinator's")
        claim_id, hid = self._ref(u.claim_id, keys), self._ref(u.hypothesis_id, keys)
        if u.kind == "attach_evidence":
            self._need(u, "claim_id", "evidence_id", "stance")
            link = self.link(str(claim_id), str(u.evidence_id), u.stance, role, u.rationale,
                             u.applicability, u.limitations)
            unjudged = u.applicability == "unknown" and link.applicability in ("exact", "proxy")
            note = "; ".join(([f"applicability corrected to {link.code_applicability}"] if link.corrected else [])
                             + ([f"applicability unknown is no judgement: code's {link.applicability} is stored"]
                                if unjudged else [])
                             + (["stored as context_only"] if link.downgraded_from else [])
                             + ([f"replaces the link of {link.revises}"] if link.revises else []))
            return [link.claim_id, link.evidence_id], note
        if u.kind == "assess":
            self._need(u, "claim_id", "assessment", "base_version")
            if role in INVESTIGATORS:
                self.assess(str(claim_id), u.assessment, u.rationale, "code", u.base_version,
                            suggested_by=role)
            else:
                self.assess(str(claim_id), u.assessment, u.rationale, role, u.base_version)
            return [str(claim_id)], ""
        if u.kind == "new_claim":
            self._need(u, "claim")
            draft = u.claim.model_copy(update={"dependencies": self._refs(u.claim.dependencies, keys)})
            cid, created, added = self._add_claim(draft, role, u.reason or u.rationale)
            if hid:
                h = self._open_hypothesis(hid)
                if cid not in h.claim_ids or (u.required and cid not in h.required_claim_ids):
                    self.add_claim_to_hypothesis(hid, cid, u.required, u.reason or f"add {cid}", role)
            notes = ([] if created else [f"duplicate of existing claim {cid}"]) + (
                [f"premises {', '.join(added)} added"] if added else [])
            return [cid], "; ".join(notes)
        if u.kind == "supersede_claim":
            self._need(u, "claim_id", "claim", "reason")
            draft = u.claim.model_copy(update={"dependencies": self._refs(u.claim.dependencies, keys)})
            new = self.supersede_claim(str(claim_id), draft, u.reason, role, self._refs(u.hypothesis_ids, keys))
            return [new, str(claim_id)], ""
        if u.kind == "add_claim_to_hypothesis":
            self._need(u, "hypothesis_id", "claim_id")
            self.add_claim_to_hypothesis(str(hid), str(claim_id), u.required, u.reason, role)
            return [str(hid), str(claim_id)], ""
        if u.kind == "replace_required_claim":
            self._need(u, "hypothesis_id", "claim_id", "new_claim_id", "reason")
            new = str(self._ref(u.new_claim_id, keys))
            self.replace_required_claim(str(hid), str(claim_id), new, u.reason, role)
            return [str(hid), new, str(claim_id)], ""
        if u.kind == "revise_hypothesis":
            self._need(u, "hypothesis_id", "changes", "reason")
            c = u.changes
            changes = c.model_copy(update={
                "add_claim_ids": self._refs(c.add_claim_ids, keys),
                "add_required_claim_ids": self._refs(c.add_required_claim_ids, keys),
                "remove_claim_ids": self._refs(c.remove_claim_ids, keys),
                "replace_claims": {str(self._ref(k, keys)): str(self._ref(v, keys))
                                   for k, v in c.replace_claims.items()}})
            self.revise_hypothesis(str(hid), changes, u.reason, role)
            return [str(hid)], ""
        if u.kind == "set_disposition":
            self._need(u, "hypothesis_id", "disposition", "reason")
            self.set_disposition(str(hid), u.disposition, u.reason, role, u.revisit_trigger)
            return [str(hid)], ""
        self._need(u, "hypothesis")
        d = u.hypothesis
        draft = d.model_copy(update={"claim_ids": self._refs(d.claim_ids, keys),
                                     "required_claim_ids": self._refs(d.required_claim_ids, keys),
                                     "replaces": self._ref(d.replaces, keys)})
        known = set(self.hypotheses)
        new_hid = self.add_hypothesis(draft, role)
        return [new_hid], f"merged into {new_hid} (same signature)" if new_hid in known else ""

    def apply_updates(self, updates: Iterable[GraphUpdate],
                      role: Role) -> tuple[list[UpdateOutcome], list[UpdateOutcome]]:
        """Apply a batch in order. Each update is atomic; a refusal records a refuse_update event (with the reason)
        and the batch goes on. A base_version is the claim version the proposer read, before this batch: the batch's
        own earlier links and assessments do not make it stale, any other change does. A suggested assessment on
        attach_evidence is applied after its link, through the same gate, as code. Dependencies are propagated once
        at the end. Returns (accepted, refused)."""
        accepted: list[UpdateOutcome] = []
        refused: list[UpdateOutcome] = []
        keys: dict[str, str] = {}
        read: dict[str, int] = {}            # claim id -> its version when this batch first named it
        created_here: set[str] = set()      # local keys resolving to older duplicates must still supply versions

        def refuse(i: int, kind: str, reason: str, u: GraphUpdate) -> None:
            targets = [v for v in (u.claim_id, u.evidence_id, u.hypothesis_id, u.new_claim_id) if v]
            eid = self._event("refuse_update", role, reason, targets=targets, mutate=False,
                              details={"kind": kind, "index": i,
                                       "update": u.model_dump(mode="json", exclude_defaults=True)}).event_id
            refused.append(UpdateOutcome(index=i, kind=kind, accepted=False, reason=reason, event_ids=[eid]))

        for i, u in enumerate(updates):
            start = len(self.events)
            known_before = set(self.claims)
            named = self._named_claim(u, keys)
            if named is not None:
                read.setdefault(named, self.claims[named].version)
            if named in created_here and (u.claim_id or "").startswith(KEY_PREFIX) and \
                    u.kind in ("attach_evidence", "assess") and u.base_version is None:
                # The model could not read a version for a claim that this batch has just created.
                # Existing claims (including duplicates resolved through local keys) keep the stale-read guard.
                u = u.model_copy(update={"base_version": read[named]})
            batch_u = u
            if u.kind == "assess" and named is not None and u.base_version == read[named]:
                batch_u = u.model_copy(update={"base_version": self.claims[named].version})
            try:
                ids, note = self._apply_one(batch_u, role, keys)
            except GraphRefusal as r:
                refuse(i, u.kind, r.reason, u)
                continue
            if u.key and ids:
                keys[u.key] = ids[0]
                if u.kind in ("new_claim", "supersede_claim") and ids[0] not in known_before:
                    created_here.add(ids[0])
            accepted.append(UpdateOutcome(index=i, kind=u.kind, accepted=True, ids=ids, note=note,
                                          event_ids=[e.event_id for e in self.events[start:]]))
            if u.kind == "attach_evidence" and u.suggested_assessment is not None:
                start = len(self.events)
                claim_id = ids[0]
                try:
                    if u.base_version is None:
                        raise GraphRefusal("a suggested assessment needs the base_version it was made against")
                    if u.base_version != read[claim_id]:
                        raise GraphRefusal(f"stale update: {claim_id} was at version {read[claim_id]} when this batch "
                                           f"began, the suggestion was based on version {u.base_version}; re-read "
                                           "the claim")
                    assessor: Role = "code" if role in INVESTIGATORS else role
                    self.assess(claim_id, u.suggested_assessment, u.rationale, assessor,
                                self.claims[claim_id].version, suggested_by=role)
                except GraphRefusal as r:
                    refuse(i, "assess", r.reason, u)
                    continue
                accepted.append(UpdateOutcome(index=i, kind="assess", accepted=True, ids=[claim_id],
                                              event_ids=[e.event_id for e in self.events[start:]]))
        self.propagate()
        return accepted, refused

    # --- serialisation -----------------------------------------------------------------------------------------------

    def to_state(self) -> GraphState:
        return GraphState(engine_version=self.engine_version, case=self.case, version=self.version,
                          counters=self.counters, model_usage=self.model_usage, variant_aliases=self.variant_aliases,
                          variant_elements=self.variant_elements, entities=self.entities, claims=self.claims,
                          evidence=self.evidence, hypotheses=self.hypotheses, questions=self.questions,
                          tool_calls=self.tool_calls, comparisons=self.comparisons, events=self.events,
                          result=self.result, **self.scope_views())

    def to_json(self, indent: int | None = 2) -> str:
        """graph.json: everything, in id order, losslessly (from_json(to_json()) gives an equal graph)."""
        return self.to_state().model_dump_json(indent=indent)

    @classmethod
    def from_state(cls, state: GraphState, resolver: SymbolResolver | None = None,
                   groups: GroupRegistry | None = None) -> "ClaimGraph":
        g = cls(state.case, resolver, groups)
        g.engine_version, g.version, g.counters = state.engine_version, state.version, dict(state.counters)
        g.model_usage = state.model_usage
        g.variant_aliases, g.variant_elements = dict(state.variant_aliases), dict(state.variant_elements)
        g.entities, g.claims, g.evidence = dict(state.entities), dict(state.claims), dict(state.evidence)
        g.hypotheses, g.questions = dict(state.hypotheses), dict(state.questions)
        g.tool_calls, g.comparisons = dict(state.tool_calls), dict(state.comparisons)
        g.events, g.result = list(state.events), state.result
        for ent in g.entities.values():
            g._index_entity(ent)
        for claim in g.claims.values():
            key = g._claim_key(claim.subject_ids, claim.relation, claim.object_ids, claim.direction,
                               claim.effect_allele, claim.allele_scope, claim.context_scope)
            g._claim_by_key.setdefault(key, claim.claim_id)
        return g

    @classmethod
    def from_json(cls, text: str, resolver: SymbolResolver | None = None,
                  groups: GroupRegistry | None = None) -> "ClaimGraph":
        return cls.from_state(GraphState.model_validate_json(text), resolver, groups)


# --- candidate retention: which inventory groups the hypotheses sketched (SPEC 13.5) ---------------------------------
# One rule for the engine's metrics, the bundle's metrics.json and the evaluator (bundle re-exports both names).

def hypothesis_versions(h: Hypothesis) -> list[tuple[list[str], list[str]]]:
    """Every version of a hypothesis as (claim ids, member alternatives), oldest first: each revision keeps the version
    it replaced in history ("previous"), and the last entry is the hypothesis as it stands."""
    earlier = [(list(prev.get("claim_ids") or []), list(prev.get("member_alternatives") or []))
               for entry in h.history if entry.get("kind") == "revision"
               and isinstance(prev := entry.get("previous"), Mapping)]
    return [*earlier, (list(h.claim_ids), list(h.member_alternatives))]


def sketched_groups(graph: ClaimGraph, rows: Iterable[Mapping[str, Any]]) -> set[str]:
    """The inventory groups (group ids from `rows`, the qbic_inventory observation rows) that some version of some
    hypothesis named, whatever its disposition: as a tf_group, or through a member TF (a TF entity, a member of a
    named group, complex or binding event, or a member alternative). Claims count from every version of every
    hypothesis, and so does every claim they superseded, however long the chain. So a group a local repair or a
    supersession replaced was considered, never "inventory_only" (SPEC 13.5): candidate retention measures what was
    never sketched, not what a repair dropped. Symbols compare whitespace-collapsed and upper case."""
    claims: set[str] = set()
    tfs: set[str] = set()
    for h in graph.hypotheses.values():
        for claim_ids, alternatives in hypothesis_versions(h):
            claims |= {c for c in claim_ids if c in graph.claims}
            tfs |= {_text(a).upper() for a in alternatives if _text(a)}
    frontier = sorted(claims)
    while frontier:                     # the claims each named claim superseded, back to the first proposition
        prior = graph.claims[frontier.pop()].supersedes
        if prior and prior in graph.claims and prior not in claims:
            claims.add(prior)
            frontier.append(prior)
    groups: set[str] = set()
    for cid in claims:
        for eid in graph.claims[cid].subject_ids + graph.claims[cid].object_ids:
            entity = graph.entities[eid]
            if entity.kind == "tf_group" and entity.canonical_id:
                groups.add(_text(entity.canonical_id).upper())
            if entity.kind == "tf":
                tfs.add(_text(entity.label).upper())
            if entity.kind in MEMBER_KINDS:
                tfs |= {_text(graph.entities[p].label).upper() for p in entity.participants}
    return {str(r.get("group_id")) for r in rows
            if _text(r.get("group_id")).upper() in groups
            or {_text(m.get("tf")).upper() for m in r.get("members") or [] if isinstance(m, Mapping)} & tfs}
