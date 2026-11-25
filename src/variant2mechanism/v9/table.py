"""The chain table: a run's answer as eight small claims per chain, each with the records that bear on it.

Why: the claim graph holds whatever claims the roles made, so a run can end with an eQTL in one hypothesis, an EMSA
in another and nothing said about whether the TF is even expressed, and no reader can tell a gap nobody looked into
from one that was looked into and found empty. The table fixes what an answer is before any model is asked:

    a chain is four steps      TF binding -> regulatory activity -> target gene -> trait
    a step is two claims       the alleles differ; the parts are in place
    a claim has three cells    database, model prediction, literature: one per kind of record
    a cell is in one state     supports, disagrees, both, nothing found, not checked, no source

docs/chain-table.md is the definition for readers. This module is its data (SLOTS, SOURCES, STATES, RULES), a reader
that turns a saved claim-graph run into a table (from_graph) and the checker (check, counts).

- The eight slots cover the graph's relations (every schemas.Relation but "other"), each in one slot, except that
  a claim that something bears on a trait or a process belongs to the trait step's allele slot when it is said of
  the variant and to its premise when it is said of a gene. The allele slots compare this variant's two alleles, so
  only a record naming this variant can fill them; the premise slots are true or false whatever the allele.
- SOURCES says which tool fills which cell. A cell with no row is "no source"; a new source is an adapter and one
  row here. A test holds every row inside the class matrix (schemas.DIRECT, INDIRECT), so the map cannot promise a
  record the graph's gates would refuse. The map is narrower than the matrix where the matrix would count one fact
  twice: the variant's own eQTL fills "the alleles differ in the gene's RNA or protein" and not also "the element
  regulates the gene", which that claim already implies; a locus-to-gene score fills "the gene bears on the trait"
  only. A record that states two facts (a colocalisation: the gene has a QTL here, and it is the trait's signal) has
  two rows.
- A record's kind is how the workflow got it, which is how it can be checked: a database row (the saved response),
  a model's output (the saved output) or an experiment read from an article (the quoted passage). What a language
  model remembers is never a record.
- The reader changes nothing in the graph, transfers no evidence and gives no score. It reads a run as it was saved:
  a cell holds the records the graph's gates accepted as links, and for the binding claim the QBiC-SELEX
  inventory's items for the factor, read as chain.py reads them. A record the run retrieved and never judged for a
  claim is listed as unjudged, never attached.
- Every chain has all eight claims, whether or not the run stated them. A claim the graph does not hold (`stated`
  False) still names what the chain names (its TF, its gene, the variant's element, its traits), so its cells say
  what the run's lookups and records give for it: "nothing found" when a source was asked, "not checked" when
  records on file were never judged or no source was asked. A claim that names nothing of a kind (a chain with no
  gene) is about anything of that kind at the variant.
- The order of chains is chain.py's (weakest link, kind of evidence only) and is not changed here.
- No rule of the checker needs a known answer, so a table for a variant nobody has studied can be checked.
"""

import zlib
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Any, Literal

from pydantic import Field

from .bundle import inventory_call
from .chain import (
    ASSOCIATION_CLASSES,
    LEVEL,
    LINK_KEYS,
    PREDICTION_CLASSES,
    QBIC_STATES,
    chain_view,
    link_rung,
)
from .graph import ClaimGraph
from .proteins import ACCESSIBILITY_FLAG, COFACTOR_FLAG
from .schemas import (
    DIRECT,
    INDIRECT,
    QUALIFIED_DIRECT,
    QUALIFIED_DIRECT_FILL,
    Evidence,
    EvidenceLink,
    V9Model,
    evidence_strength,
)
from .traits import trait_key

# 2: the gene step's first claim is about the gene's RNA or protein (a cis protein QTL fills it), and four sources
# were added to the map (UDACHA, MaveDB, protein QTLs, cBioPortal)
FORMAT = 2
STEPS: tuple[tuple[str, str], ...] = (
    ("binding", "TF binding"), ("activity", "Regulatory activity"), ("gene", "Target gene"), ("trait", "Trait"))
PARTS: tuple[tuple[str, str], ...] = (("allele", "The alleles differ"), ("premise", "The parts are in place"))
LANES: tuple[tuple[str, str], ...] = (
    ("database", "Database"), ("model", "Model prediction"), ("literature", "Literature"))
STATES: tuple[tuple[str, str, str], ...] = (
    ("supports", "supports", "at least one record of this kind supports the claim"),
    ("disagrees", "disagrees", "at least one record of this kind goes against the claim, and none supports it"),
    ("both", "both", "records of this kind on both sides"),
    ("nothing_found", "nothing found", "a source of this kind was asked and returned nothing that bears on the claim"),
    ("not_checked", "not checked", "a source of this kind exists and no answer for this claim is recorded"),
    ("no_source", "no source", "the workflow has no source of this kind for this claim"),
)
STATE_KEYS: tuple[str, ...] = tuple(key for key, _, _ in STATES)
STATE_WORDS: dict[str, str] = {key: words for key, words, _ in STATES}
LANE_KEYS: tuple[str, ...] = tuple(key for key, _ in LANES)
FILLED = frozenset({"supports", "disagrees", "both"})
State = Literal["supports", "disagrees", "both", "nothing_found", "not_checked", "no_source"]
Stance = Literal["supports", "disagrees", "beside"]


@dataclass(frozen=True)
class Slot:
    """One of the eight claims of a chain. `shares` names what a record must have in common with the claim before
    it can bear on it: the TF, the element, the gene, the trait. `site_only`: the claim is about the variant's site
    and nothing else, so a record that also names a TF, a gene or a trait (a 3D contact between the element and a
    gene, say) is about another claim."""
    step: str
    part: str
    text: str
    relations: frozenset[str]
    shares: tuple[str, ...]
    site_only: bool = False

    @property
    def key(self) -> str:
        return f"{self.step}.{self.part}"


SLOTS: dict[str, Slot] = {s.key: s for s in (
    Slot("binding", "allele", "The two alleles differ in binding the TF.",
         frozenset({"alters_binding"}), ("tfs",)),
    Slot("binding", "premise", "The TF is present where it would act: expressed in the context, or bound at the site.",
         frozenset({"occupies", "expressed_in"}), ("tfs",)),
    Slot("activity", "allele", "The two alleles differ in the regulatory activity of the site.",
         frozenset({"alters_regulatory_activity"}), ("elements",)),
    Slot("activity", "premise", "The variant lies in a regulatory element.",
         frozenset({"overlaps"}), ("elements",), site_only=True),
    Slot("gene", "allele", "The two alleles differ in the gene's RNA or protein.",
         frozenset({"associated_with_expression", "alters_rna"}), ("genes",)),
    Slot("gene", "premise", "The element regulates the gene.",
         frozenset({"regulates"}), ("genes",)),
    # contributes_to_trait and affects_process sit in both trait slots: said of the variant they are a claim that the
    # alleles differ in the trait (an allele edited in an animal model), said of a gene they are the premise
    Slot("trait", "allele", "The two alleles differ in the trait.",
         frozenset({"associated_with_trait", "causal_at_locus", "contributes_to_trait", "affects_process"}),
         ("traits",)),
    Slot("trait", "premise", "The gene bears on the trait.",
         frozenset({"contributes_to_trait", "affects_process"}), ("genes", "traits")),
)}
SLOT_KEYS: tuple[str, ...] = tuple(SLOTS)


def slot_classes(slot: str) -> frozenset[str]:
    """The evidence classes that can count for a slot: those the class matrix holds direct for one of its relations
    (or direct once a qualifier is stated, such as allele-specific ChIP reads), and the associations and predictions
    it holds indirect, which give a rung. An experiment the matrix holds indirect (a binding assay for a claim about
    regulatory activity, a region deletion for a claim that the alleles differ) can only stand beside the claim."""
    found: set[str] = set()
    for relation in SLOTS[slot].relations:
        found |= DIRECT[relation] | (INDIRECT[relation] & (ASSOCIATION_CLASSES | PREDICTION_CLASSES))
        found |= {cls for (rel, cls) in (*QUALIFIED_DIRECT, *QUALIFIED_DIRECT_FILL) if rel == relation}
    return frozenset(found)


def can_count(slot: Slot, evidence: Evidence) -> bool:
    """Whether the class matrix lets this record count for or against one of the slot's relations: it tests the
    relation directly, or it is an association or a prediction, which give a rung (chain.link_rung)."""
    for relation in slot.relations:
        strength = evidence_strength(relation, evidence)
        if strength == "direct" or link_rung(strength, evidence.evidence_class) is not None:
            return True
    return False


ABOUT: dict[str, str] = {"tfs": "about_tfs", "genes": "about_genes", "elements": "about_elements",
                         "traits": "about_traits"}
RNA_QTLS: tuple[str, ...] = ("eqtl", "sqtl")
SITE_ONLY: tuple[str, ...] = ("tfs", "genes", "traits")


@dataclass(frozen=True)
class Source:
    """One row of the source map: a tool, the kind of record it returns, the claim those records can bear on, their
    evidence classes and what they are. `needs` and `lacks` say which of a tool's records the row means, by what a
    record names besides the variant (tfs, genes, elements, traits): a credible set names a trait and no gene, and
    its colocalisation with a gene's QTL names both, so the two are different rows although one tool returns both
    with one evidence class. `where` narrows a row by a value in the record's data (the kind of QTL)."""
    tool: str
    lane: str
    slot: str
    classes: frozenset[str]
    gives: str
    needs: tuple[str, ...] = ()
    lacks: tuple[str, ...] = ()
    where: tuple[tuple[str, tuple[str, ...]], ...] = ()   # a field of the record's data and the values the row means


def _row(tool: str, lane: str, slot: str, classes: set[str], gives: str, needs: tuple[str, ...] = (),
         lacks: tuple[str, ...] = (), where: tuple[tuple[str, tuple[str, ...]], ...] = ()) -> Source:
    return Source(tool, lane, slot, frozenset(classes), gives, needs, lacks, where)


def _credible_sets(tool: str) -> tuple[Source, ...]:
    """The four facts an Open Targets credible set states, whichever tool returned it. A claim about a gene's RNA
    takes a colocalising expression or splicing QTL only: a protein QTL is often a trans effect on a protein encoded
    elsewhere, which says the locus matters to that protein and not that the gene is this variant's target."""
    return (
        _row(tool, "database", "trait.allele", {"statistical_inference"},
             "Open Targets credible sets holding the variant, with its PIP", ("traits",), ("genes",)),
        _row(tool, "database", "gene.allele", {"statistical_inference"},
             "colocalisation of a trait signal with the gene's expression or splicing QTL", ("genes",),
             where=(("qtl_type", RNA_QTLS),)),
        _row(tool, "database", "trait.premise", {"statistical_inference"},
             "colocalisation of the trait's signal with the gene's QTL", ("genes", "traits")),
        _row(tool, "model", "trait.premise", {"precomputed_prediction"},
             "Open Targets locus-to-gene score for the trait's signal", ("genes", "traits")))


SOURCES: tuple[Source, ...] = (
    _row("qbic_inventory", "model", "binding.allele", {"prediction"},
         "QBiC-SELEX: the allele each gate-passing group of models favours", ("tfs",)),
    _row("qbic_tf_detail", "model", "binding.allele", {"prediction"},
         "QBiC-SELEX: every gate-passing model of one TF or group", ("tfs",)),
    # one tool, two cells, by what the protein is (v9/proteins.py): a record made before that was recorded has no
    # flag ("None") and stays where it was
    _row("adastra_asb", "database", "binding.allele", {"occupancy"},
         "ADASTRA: allele-specific ChIP-seq binding of a TF called at the variant", ("tfs",),
         where=((COFACTOR_FLAG, ("False", "None")),)),
    _row("adastra_asb", "database", "activity.allele", {"occupancy"},
         "ADASTRA: allele-specific ChIP-seq reads, called at the variant, of a protein that does not bind DNA itself",
         ("tfs",), where=((COFACTOR_FLAG, ("True",)),)),
    # reads of open chromatin name no protein: the record carries its own flag and names no TF
    _row("udacha_asa", "database", "activity.allele", {"occupancy"},
         "UDACHA: allele-specific chromatin accessibility called at the variant, per cell type",
         lacks=("tfs",), where=((ACCESSIBILITY_FLAG, ("True",)),)),
    _row("mavedb_reporter", "database", "activity.allele", {"reporter_assay"},
         "MaveDB: a saturation-mutagenesis reporter assay that measured this exact substitution"),
    _row("chip_occupancy", "database", "binding.premise", {"occupancy"},
         "ENCODE and ReMap ChIP-seq peaks over the variant", ("tfs",)),
    _row("tf_occupancy_set", "database", "binding.premise", {"occupancy"},
         "the same peaks, asked for every candidate TF at once", ("tfs",)),
    _row("tf_expression", "database", "binding.premise", {"expression"},
         "the TF's RNA level in the context (GTEx tissue, DepMap line)", ("tfs",)),
    _row("tf_expression_set", "database", "binding.premise", {"expression"},
         "the same levels, asked for every candidate TF at once", ("tfs",)),
    _row("depmap_context", "database", "binding.premise", {"expression"},
         "DepMap expression of the TF in a cell line and its lineage", ("tfs",)),
    _row("depmap_context", "database", "trait.premise", {"dependency_screen"},
         "DepMap CRISPR gene effect in a cell line and its lineage", ("genes",)),
    _row("ccre_overlap", "database", "activity.premise", {"annotation"},
         "the ENCODE cCRE holding the variant and its class per biosample", ("elements",), SITE_ONLY),
    _row("ccre_overlap", "database", "gene.allele", {"association"}, "SCREEN's eQTL links of this variant",
         ("genes",)),
    _row("ccre_overlap", "database", "gene.premise", {"perturbation"},
         "SCREEN's CRISPR links: the element perturbed, the gene measured", ("genes", "elements")),
    _row("screen_online", "database", "activity.premise", {"annotation"},
         "the SCREEN cCRE holding the variant and its signals", ("elements",), SITE_ONLY),
    _row("variant_annotation", "database", "activity.premise", {"annotation"},
         "Ensembl regulatory features at the variant", ("elements",), SITE_ONLY),
    _row("gtex_eqtl", "database", "gene.allele", {"association"}, "GTEx single-tissue eQTLs of the variant",
         ("genes",)),
    # a protein QTL counts for the gene whose own protein was measured (cis, by Open Targets' own call) and for no
    # other: a trans set says the locus matters to a protein encoded elsewhere
    _row("protein_qtl_sets", "database", "gene.allele", {"statistical_inference"},
         "Open Targets: a credible set of a protein QTL for the gene's own protein, holding the variant", ("genes",),
         ("traits",), (("qtl_type", ("pqtl",)), ("cis", ("True",)))),
    _row("gwas_associations", "database", "trait.allele", {"association"},
         "GWAS Catalog associations of the variant", ("traits",)),
    _row("tumour_recurrence", "database", "trait.allele", {"association"},
         "cBioPortal: the tumours of a sequenced cohort that carry this exact mutation, by cancer type", ("traits",),
         ("genes",)),
    _row("civic_lookup", "database", "trait.allele", {"clinical_assertion"},
         "CIViC clinical evidence for a somatic variant", ("traits",)),
    *_credible_sets("credible_sets_l2g"),
    *_credible_sets("credible_sets_all"),
    _row("gene_disease", "database", "trait.premise", {"association", "clinical_assertion", "statistical_inference"},
         "Open Targets' records linking the gene to the trait: burden tests, curated pairs, matched mouse knockouts",
         ("genes", "traits")),
    *(Source("literature_read", "literature", slot, slot_classes(slot), "an experiment read from an article, quoted")
      for slot in SLOTS),
)
RULES: tuple[tuple[str, str], ...] = (
    ("shape", "Every chain has its four steps, each with both claims; every claim has three cells; every cell is in "
              "one of the six states."),
    ("record", "A cell that reports support or disagreement cites its records, and no other cell counts any. Each "
               "record is in the run's files, of the cell's kind, and from a source the map lists for that cell."),
    ("variant", "A record counted for a claim that the alleles differ names this variant."),
    ("looked", "\"Nothing found\" cites a lookup that completed. \"No source\" appears only where the map has no "
               "source, or says why this claim has none."),
    ("unjudged", "No record on file that names the claim's TF, element, gene or trait is left without a judgement: "
                 "it is counted in the cell, listed beside it, or set aside with a reason."),
    ("quoted", "A literature record carries the passage it was read from and the article it came from."),
)
RULE_KEYS: tuple[str, ...] = tuple(key for key, _ in RULES)
FILTERS: dict[str, str] = {"tf": "tfs", "tfs": "tfs", "group": "groups", "gene": "genes", "genes": "genes",
                           "trait": "traits", "traits": "traits"}
UNJUDGED_SHOWN = 12                                       # unjudged record ids a cell lists before it only counts
READER_LOOKED = ("read", "no_mention")                    # reader statuses that looked into an article's text
NO_ARTICLE = "a search for the variant's names listed no article"
NO_SEARCH = "the search for articles naming the variant did not complete, so none was looked for"
STRONGEST_WORDS: dict[str, str] = {"edit": "edit or perturbation", "assay": "allele-resolved assay",
                                   "association": "association", "prediction": "prediction",
                                   "recorded": "a record that compares nothing", "none": "nothing"}


def sources_for(slot: str, lane: str) -> list[Source]:
    return [s for s in SOURCES if s.slot == slot and s.lane == lane]


def fits(source: Source, evidence: Evidence) -> bool:
    """Whether a record is one the row means: of one of its classes, naming what the row needs and nothing it lacks,
    with the data values the row asks for."""
    return (evidence.evidence_class in source.classes
            and all(getattr(evidence, ABOUT[kind]) for kind in source.needs)
            and not any(getattr(evidence, ABOUT[kind]) for kind in source.lacks)
            and all(str(evidence.data.get(name)) in values for name, values in source.where))


def listed(slot: str, lane: str, tool: str | None, evidence: Evidence) -> bool:
    """Whether the map lists this record, retrieved by this tool, for the cell."""
    return any(s.tool == tool and fits(s, evidence) for s in sources_for(slot, lane))


def lane_of(evidence: Evidence) -> str:
    """The kind of record: an experiment read from an article, a model's output, or else a database row."""
    if evidence.origin == "literature":
        return "literature"
    return "model" if evidence.evidence_class in PREDICTION_CLASSES else "database"


# --- the table ---------------------------------------------------------------------------------------------------------

class Record(V9Model):
    """One record in a cell. `kind` is the rung it gives the claim (edit, assay, association, prediction) or None
    when it gives none; `stance` is how it counts: for the claim, against it, or beside it without counting."""
    id: str
    stance: Stance
    evidence_class: str
    kind: str | None = None
    tool: str | None = None
    sources: list[str] = Field(default_factory=list)
    text: str = ""
    passage: str | None = None
    claim: str | None = None                     # the graph claim it is linked to; None when code read it
    note: str = ""


class SetAside(V9Model):
    record: str
    why: str


class Cell(V9Model):
    state: State
    records: list[Record] = Field(default_factory=list)
    lookups: list[str] = Field(default_factory=list)      # completed tool calls that asked a source for this cell
    unjudged: list[str] = Field(default_factory=list)     # records on file with no judgement for this claim
    unjudged_total: int = 0
    set_aside: list[SetAside] = Field(default_factory=list)
    note: str = ""


class TableClaim(V9Model):
    id: str
    step: str
    part: str
    text: str
    label: str                                   # what it names, as the chain view names it
    names: dict[str, list[str]]                  # tfs, groups, elements, genes, traits (labels), trait_ids
    graph_claims: list[str]
    stated: bool = True                          # False: no claim of the run states it; the table asks it anyway
    cells: dict[str, Cell]
    strongest: str                               # edit, assay, association, prediction, recorded or none


class TableChain(V9Model):
    rank: int
    ties: int
    title: str
    claims: dict[str, str | None]                # slot key -> claim id (every chain has all eight)
    joined: list[str] = Field(default_factory=list)   # experiments that show this chain's TF acting on its gene


class Table(V9Model):
    format: int = FORMAT
    case_id: str
    variant: str
    chains: list[TableChain] = Field(default_factory=list)
    claims: dict[str, TableClaim] = Field(default_factory=dict)
    beside: list[dict[str, str]] = Field(default_factory=list)   # claims that are not a step of any chain


class Problem(V9Model):
    rule: str
    where: str
    text: str


# --- reading a saved run -----------------------------------------------------------------------------------------------

_trait_key = lru_cache(maxsize=None)(trait_key)
NAME_KINDS: tuple[str, ...] = ("tfs", "groups", "elements", "genes", "traits", "trait_ids")
NO_NAME: dict[str, str] = {"binding": "no TF named", "activity": "the variant's site", "gene": "no gene named",
                           "trait": "no trait named"}
LABEL_SHOWN = 3                                           # names a claim's label spells out before it counts the rest


def _unique(values: Iterable[str]) -> list[str]:
    return list(dict.fromkeys(v for v in values if v))


def _entity_names(graph: ClaimGraph, entity_ids: Iterable[str], slot: Slot) -> dict[str, list[str]]:
    """What these entities name, by kind. A trait is named by its label; its ontology id is kept apart (`trait_ids`),
    because an id says which lookups asked about it and never that two labels are one trait. An activity claim
    also names the elements code recorded as holding the variant, since a record about that element is about the
    variant's site."""
    out: dict[str, list[str]] = {kind: [] for kind in NAME_KINDS}
    for eid in entity_ids:
        e = graph.entities[eid]
        if e.kind == "tf":
            out["tfs"].append(e.label)
        elif e.kind in ("tf_group", "complex", "binding_event"):
            out["tfs"] += [graph.entities[p].label for p in e.participants if graph.entities[p].kind == "tf"]
            out["groups"] += [str(e.canonical_id or ""), e.label]
        elif e.kind in ("gene", "transcript"):
            out["genes"].append(e.label)
        elif e.kind in ("phenotype", "process"):
            out["traits"].append(e.label)
            out["trait_ids"].append(str(e.canonical_id or ""))
        elif e.kind == "element":
            out["elements"] += [e.label, str(e.canonical_id or "")]
    if slot.step == "activity":
        out["elements"] += list(graph.variant_elements)
    return {kind: _unique(values) for kind, values in out.items()}


def _names(graph: ClaimGraph, claim_ids: Iterable[str], slot: Slot) -> dict[str, list[str]]:
    """What the claims name, by kind."""
    return _entity_names(graph, [eid for cid in claim_ids
                                 for eid in graph.claims[cid].subject_ids + graph.claims[cid].object_ids], slot)


def names_case(graph: ClaimGraph, evidence: Evidence) -> bool:
    """Whether a record names the case variant (graph.variant_mention, the graph's one rule for it)."""
    return any(graph.variant_mention(x) == "case" for x in evidence.about_variants)


def _shares(graph: ClaimGraph, slot: Slot, names: Mapping[str, list[str]], evidence: Evidence) -> bool:
    """Whether a record names what the claim names: the TF or gene by symbol, the element by label or accession, the
    trait by its label (traits.trait_key: spelling only, never a synonym) or by an ontology term its source mapped
    it to. A shared term is enough here and not in the graph, on purpose: the graph decides what may be linked and
    refuses a term that stands for another label, while this decides what must be judged, and a locus-to-gene score
    for "Cholesterol, total" filed under the term of the chain's "total cholesterol" is a record somebody has to
    judge. A claim that names nothing of a kind (a chain with no gene, a run with no trait claim) is about anything
    of that kind at the variant, so every record shares it. A record that names no element is about the claim's site
    when it names the variant; one that names no trait can still be about the claim's gene."""
    def hit(kind: str, about: Iterable[str], key=str.casefold) -> bool:
        named = [*names[kind], *names.get("trait_ids", [])] if kind == "traits" else names[kind]
        return bool({key(n) for n in named} - {""} & {key(a) for a in about if a})

    if slot.site_only and (evidence.about_tfs or evidence.about_genes or evidence.about_traits):
        return False
    for kind in slot.shares:
        if not names[kind]:
            continue
        if kind == "tfs" and not hit("tfs", evidence.about_tfs, str.upper):
            return False
        if kind == "genes" and not hit("genes", evidence.about_genes, str.upper):
            return False
        if kind == "traits" and not hit("traits", evidence.about_traits, _trait_key):
            if slot.part == "allele" or evidence.about_traits:
                return False
        if kind == "elements" and not hit("elements", evidence.about_elements):
            if evidence.about_elements or not names_case(graph, evidence):
                return False
    return True


def _tool(graph: ClaimGraph, evidence: Evidence) -> str | None:
    call = graph.tool_calls.get(evidence.retrieval_ref or "")
    return call.tool_name if call is not None else None


class _Index:
    """What a table reads from a graph more than once, built on first use: per cell, the records on file that could
    count for it (from a source the map lists for the cell, of a class the class matrix lets count, and naming this
    variant for a claim that the alleles differ); per claim, the records the graph refused for it; per slot, the
    records code judged for a claim nobody stated and did not count (an experiment read from an article that the
    graph would refuse for the claim it would need); what the reader did (reader.py): the article reads that
    looked into a text, its searches that listed nothing, and how many of the articles found were read; what
    the critic said (critic.py) of each record counted for a claim, with its counts for the run; and what the judge
    said (judge.py) of each candidate of a tie, with its counts."""

    def __init__(self, graph: ClaimGraph):
        self.graph = graph
        self._pools: dict[tuple[str, str], list[Evidence]] = {}
        self._aside: dict[str, dict[str, str]] = {}
        self._slot_aside: dict[str, dict[str, str]] = {}
        self._linked: dict[tuple[str, ...], set[str]] = {}
        self.reads: list[str] = []
        self.reading: Mapping[str, Any] | None = None
        self.second: dict[tuple[str, str], Mapping[str, Any]] = {}   # (claim, record) -> the critic's answer
        self.critique: Mapping[str, Any] | None = None
        self.judged: list[Mapping[str, Any]] = []                    # the judge's answer for each candidate asked
        self.judgement: Mapping[str, Any] | None = None
        for event in graph.events:
            if event.action == "audit" and isinstance(event.details.get("judge"), Mapping):
                self.judged.append(event.details["judge"])
            if event.action == "audit" and isinstance(event.details.get("judge_summary"), Mapping):
                self.judgement = event.details["judge_summary"]
            if event.action == "audit" and isinstance(event.details.get("critic"), Mapping):
                for cid in (t for t in event.target_ids if t in graph.claims):
                    for eid in (t for t in event.target_ids if t in graph.evidence):
                        self.second[(cid, eid)] = event.details["critic"]
            if event.action == "audit" and isinstance(event.details.get("critic_summary"), Mapping):
                self.critique = event.details["critic_summary"]
            reader = event.details.get("reader")
            if event.action == "collect_facts" and isinstance(reader, Mapping):
                if reader.get("status") in READER_LOOKED and reader.get("read"):
                    self.reads.append(str(reader["read"]))
            if event.action == "collect_facts" and isinstance(event.details.get("reader_summary"), Mapping):
                self.reading = event.details["reader_summary"]
            if event.action != "refuse_update":
                continue
            records = [t for t in event.target_ids if t in graph.evidence]
            claims = [t for t in event.target_ids if t in graph.claims]
            for cid in claims:
                for eid in records:
                    self._aside.setdefault(cid, {}).setdefault(eid, event.concise_reason)
            slot = event.details.get("slot")
            if not claims and slot in SLOTS:
                for eid in records:
                    self._slot_aside.setdefault(slot, {}).setdefault(eid, event.concise_reason)

    def linked(self, relations: Iterable[str]) -> set[str]:
        """The records linked, with whatever stance, to a claim with one of these relations."""
        key = tuple(sorted(relations))
        if key not in self._linked:
            self._linked[key] = {link.evidence_id for claim in self.graph.claims.values()
                                 if claim.relation in key for link in claim.evidence_links}
        return self._linked[key]

    def reader_lookups(self) -> list[str]:
        """The reader's completed lookups, which every literature cell cites: each article whose text it looked
        into, or, when its searches listed no article at all, those searches."""
        if self.reading is None:
            return []
        if self.reads or self.reading.get("found") or not _searched(self.reading):
            return list(dict.fromkeys(self.reads))
        return [str(x["call"]) for x in self.reading.get("searches") or []]

    def reader_note(self) -> str:
        """How much of what was found the reader read: a literature cell's "nothing found" rests on that much."""
        r = self.reading
        if r is None:
            return ""
        if not r.get("found"):
            return NO_ARTICLE if _searched(r) else NO_SEARCH
        looked = int(r.get("read") or 0) + int(r.get("no_mention") or 0)
        refused = int(r.get("refused") or 0)
        return (f"{r.get('read', 0)} of {r['found']} articles found were read by the model"
                + (f"; {r['found'] - looked} not looked into (a review, no text, a failed call or the cap)"
                   if r["found"] > looked else "")
                + (f"; {refused} of the {r.get('experiments', 0)} experiments it returned did not pass code's checks"
                   if refused else ""))

    def slot_aside(self, slot: Slot, names: Mapping[str, list[str]]) -> dict[str, str]:
        """Records code judged for this slot without a stated claim and did not count, where they name what this
        claim names."""
        return {eid: why for eid, why in self._slot_aside.get(slot.key, {}).items()
                if _shares(self.graph, slot, names, self.graph.evidence[eid])}

    def pool(self, slot: Slot, lane: str) -> list[Evidence]:
        key = (slot.key, lane)
        if key not in self._pools:
            graph = self.graph
            self._pools[key] = [
                ev for ev in graph.evidence.values()
                if lane_of(ev) == lane and listed(slot.key, lane, _tool(graph, ev), ev) and can_count(slot, ev)
                and (slot.part != "allele" or names_case(graph, ev))]
        return self._pools[key]

    def set_aside(self, claim_ids: Iterable[str]) -> dict[str, str]:
        """Records a role proposed for one of these claims and the graph refused, with the graph's reason."""
        out: dict[str, str] = {}
        for cid in claim_ids:
            for eid, why in self._aside.get(cid, {}).items():
                out.setdefault(eid, why)
        return out


def _beside_note(link: EvidenceLink) -> str:
    if link.applicability == "different":
        return "from another context"
    if link.strength == "context" and link.stance == "context_only" and link.downgraded_from is None \
            and link.proposed_by == "code" and link.rationale:
        return link.rationale                             # code says why it counted the record as context only
    if link.strength == "context":
        return "a kind of record that cannot test this claim"
    if link.stance in ("supports", "contradicts"):
        return "an experiment that does not test this claim directly"
    return "linked as context only"


def identity_note(evidence: Evidence) -> str:
    """How a record was taken as about the variant when its article writes neither an rsID nor a position: by the
    article's own name for the mutation, under the two checks of variant_identity._text_mined_map. "" for every
    other record. Printed with the record, because text mining can tie a name to the wrong variant."""
    proof = evidence.data.get("variant_identity") or {}
    if not isinstance(proof, dict) or proof.get("basis") != "text_mined_name":
        return ""
    names = " and ".join(f'"{n}"' for n in proof.get("paper_variants") or [])
    where = ("in the quotation" if proof.get("written_in") == ["passage"] else
             "in the quotation's paragraph, heading or caption, not in the quotation itself")
    return (f"named {names} {where}: NCBI's text mining ties that name to this variant, and its base change "
            "agrees")


def _record(graph: ClaimGraph, evidence: Evidence, stance: Stance, kind: str | None, claim: str | None,
            note: str = "", passage: str | None = None) -> Record:
    """A record as a cell lists it. `passage` replaces the record's own quotation for this claim: the sentences code
    copied where the critic pointed (critic.pointed), which hold the record's quotation or the result it left out.
    A record identified by its article's own name for the mutation says so in its note (identity_note)."""
    passage = passage or (evidence.experiment.passage if evidence.experiment is not None else None)
    note = "; ".join(x for x in (note, identity_note(evidence)) if x)
    return Record(id=evidence.evidence_id, stance=stance, evidence_class=evidence.evidence_class, kind=kind,
                  tool=_tool(graph, evidence), sources=list(evidence.source_ids), text=evidence.observed_result,
                  passage=passage, claim=claim, note=note)


SECOND_READING = {"shown": "a second model read the quotation in its paragraph and agrees",
                  "cannot_tell": "a second model could not tell from the paragraph whether the quotation shows this",
                  "not_reviewed": "not read by the second model"}
SECOND_POINTED = ("a second model found the result in further sentences of the same paragraph; code copied them, "
                  "and they are quoted here")


def _second_note(found: Mapping[str, Any] | None) -> str:
    """What the critic said of a counted record, as a record's note: "" for a run without the critic, and for a
    record it was not asked about because another record stands with it in the cell."""
    if found is None:
        return ""
    if found.get("passage"):
        return SECOND_POINTED
    words = SECOND_READING.get(str(found.get("verdict")), "")
    reason = str(found.get("reason") or "")
    return words + (f" ({reason})" if words and reason and found.get("verdict") == "cannot_tell" else "")


def _linked(graph: ClaimGraph, slot: Slot, claim_ids: Iterable[str], lane: str,
            index: "_Index | None" = None) -> list[Record]:
    """The records of one kind linked to these claims, as the graph's gates stored the links. A supporting or a
    contradicting link counts when its context is not a different one and it gives a rung or tests the claim
    directly (the links chain.py reads a rung from, and the direct annotation or expression record of a premise);
    everything else stands beside the claim. A record linked to two of the claims is listed once, by the link that
    counts. The "assay" rung means an assay that compares the alleles, so a record of a premise never carries it: a
    ChIP-seq peak that shows a TF in place is named by its class. With `index`, a counted record's note says what
    the critic made of it, in a run that had one, and its quotation is the one code copied where the critic
    pointed to further sentences."""
    second = index.second if index is not None else {}
    found: dict[str, Record] = {}
    for cid in claim_ids:
        for x in graph.claims[cid].evidence_links:
            ev = graph.evidence[x.evidence_id]
            if lane_of(ev) != lane:
                continue
            rung = link_rung(x.strength, ev.evidence_class)
            if slot.part == "premise" and rung == "assay":
                rung = None
            if (x.stance in ("supports", "contradicts") and x.applicability != "different"
                    and (rung is not None or x.strength == "direct")):
                said = second.get((cid, x.evidence_id))
                record = _record(graph, ev, "supports" if x.stance == "supports" else "disagrees", rung, cid,
                                 _second_note(said), str(said.get("passage") or "") if said else None)
            else:
                record = _record(graph, ev, "beside", None, cid, _beside_note(x))
            if x.evidence_id not in found or found[x.evidence_id].stance == "beside":
                found[x.evidence_id] = record
    return list(found.values())


def _inventory(graph: ClaimGraph, predictions: list[Mapping[str, Any]], have: set[str]) -> tuple[
        list[Record], str | None, str]:
    """What the QBiC-SELEX inventory holds for a binding claim's factor, read as chain.py reads it: (the items no
    role linked, as records; the cell's state when the inventory has no gate-passing item; a note). An item that
    favours the claim's allele, or a claim that states no allele, supports that the alleles differ; an item for the
    other allele disagrees. Models below the gate are a lookup that found nothing; a factor no model covers has no
    source."""
    if not predictions:
        return [], None, ""
    ordered = sorted(predictions, key=lambda p: QBIC_STATES.index(p["state"]))
    if ordered[0]["state"] == "not_covered":
        return [], "no_source", "no QBiC-SELEX model covers it"
    if ordered[0]["state"] == "below_gate":
        return [], "nothing_found", "its QBiC-SELEX models do not pass the gate"
    records: dict[str, Record] = {}
    for p in ordered:
        for item in p["items"]:
            eid = item["evidence"]
            if eid in have or eid in records:
                continue
            against = item["verdict"] == "disagrees"
            note = "read from the QBiC-SELEX inventory by code" + (
                "; the claim states no allele to compare" if item["verdict"] == "unstated" else "")
            records[eid] = _record(graph, graph.evidence[eid], "disagrees" if against else "supports",
                                   "prediction", None, note)
    return list(records.values()), None, ""


def _covers(params: Mapping[str, Any], names: Mapping[str, list[str]]) -> bool:
    """Whether a tool call's own filters (TFs, a group, genes, traits) leave room for what the claim names. A call
    with no filter asked about everything at the variant. A trait filter is met by a label or by an ontology id."""
    for key, kind in FILTERS.items():
        if key not in params:
            continue
        asked = params[key] if isinstance(params[key], list) else [params[key]]
        if kind == "traits":
            wanted = {_trait_key(str(a)) for a in asked}
            have = {_trait_key(n) for n in [*names["traits"], *names.get("trait_ids", [])]} - {""}
            if have and not any(w in h or h in w for w in wanted for h in have):
                return False
        else:
            wanted = {str(a).upper() for a in asked}
            have = {n.upper() for n in names[kind]} | ({n.upper() for n in names["groups"]} if kind == "tfs" else set())
            if have and not wanted & have:
                return False
    return True


def _lookups(graph: ClaimGraph, slot: Slot, lane: str, claim_ids: Iterable[str],
             names: Mapping[str, list[str]], index: "_Index | None" = None) -> list[str]:
    """The completed tool calls that asked a source of this kind about this claim. A literature call counts when
    the question it served targets one of the claims and it either read an article or searched and found none (a
    search that listed articles nobody read looked into nothing). The reader's reads count for every claim: it is
    asked for every experiment an article reports about the variant and the parts of its mechanism, whatever the
    claim. A database or model call counts when its filters cover what the claim names."""
    claim_ids = set(claim_ids)
    calls = [t for t in graph.tool_calls.values() if t.execution_status == "success"]
    if lane == "literature":
        asked = {q.question_id for q in graph.questions.values() if claim_ids & set(q.target_claim_ids)}
        found = [t.tool_call_id for t in calls if t.question_id in asked and (
            (t.tool_name == "literature_read" and t.read_article)
            or (t.tool_name == "literature_search" and t.retrieval_status == "no_records_found"))]
        return _unique([*found, *(index.reader_lookups() if index is not None else [])])
    tools = {s.tool for s in sources_for(slot.key, lane)}
    return [t.tool_call_id for t in calls if t.tool_name in tools and _covers(t.query_parameters, names)]


def unjudged_records(graph: ClaimGraph, slot: Slot, lane: str, names: Mapping[str, list[str]],
                     judged: set[str], index: _Index | None = None) -> list[str]:
    """Records of this kind on file that could count for the claim and have no judgement for it: from a source the
    map lists for the cell (a row whose `needs` and `lacks` the record meets), of a class the class matrix lets count
    (can_count), naming what the claim names (and, for a claim that the alleles differ, naming this variant), and
    neither counted, listed beside the claim nor set aside."""
    index = index or _Index(graph)
    # A record linked to a claim of this kind has its judgement there, on the claim that names exactly what it
    # measured. Two cases need this: a chain that names no TF (its claim is about any TF at the variant, and an
    # article's ChIP for some TF is linked to that TF's own claim), and a TF that belongs to two model-sharing
    # groups (its measured record is linked to the TF's own claim, and each group's claim names the TF too).
    elsewhere = index.linked(slot.relations)
    return [ev.evidence_id for ev in index.pool(slot, lane)
            if ev.evidence_id not in judged and ev.evidence_id not in elsewhere
            and _shares(graph, slot, names, ev)]


def _strongest(cells: Mapping[str, Cell]) -> str:
    supports = [r for cell in cells.values() for r in cell.records if r.stance == "supports"]
    kinds = [r.kind for r in supports if r.kind]
    if kinds:
        return max(kinds, key=LEVEL.__getitem__)
    return "recorded" if supports else "none"


def _cell(graph: ClaimGraph, index: _Index, slot: Slot, lane: str, claim_ids: list[str],
          names: Mapping[str, list[str]], predictions: list[Mapping[str, Any]]) -> Cell:
    records = _linked(graph, slot, claim_ids, lane, index)
    forced, note = None, ""
    if slot.key == "binding.allele" and lane == "model":
        extra, forced, note = _inventory(graph, predictions, {r.id for r in records})
        records += extra
    have = {r.id for r in records}
    aside = {eid: why for eid, why in {**index.slot_aside(slot, names), **index.set_aside(claim_ids)}.items()
             if lane_of(graph.evidence[eid]) == lane and eid not in have}
    has_source = bool(sources_for(slot.key, lane))
    lookups = _lookups(graph, slot, lane, claim_ids, names, index) if has_source else []
    unjudged = unjudged_records(graph, slot, lane, names, have | set(aside), index) if has_source else []
    counted = {r.stance for r in records} - {"beside"}
    if counted == {"supports", "disagrees"}:
        state = "both"
    elif counted:
        state = counted.pop()
    elif not has_source:
        state = "no_source"
    elif forced == "no_source":
        state, lookups = forced, []
    elif forced is not None:
        state = forced
        if (call := inventory_call(graph)) is not None:
            lookups = _unique([call.tool_call_id, *lookups])
    else:
        state = "nothing_found" if lookups and not unjudged else "not_checked"
    if lane == "literature" and state in ("nothing_found", "not_checked"):
        note = index.reader_note()                        # how much of what was found the reader read
    elif forced is None or state != forced:
        note = ""
    return Cell(state=state, records=records, lookups=lookups, unjudged=unjudged[:UNJUDGED_SHOWN],
                unjudged_total=len(unjudged), set_aside=[SetAside(record=e, why=w) for e, w in aside.items()],
                note=note)


@dataclass
class _Asked:
    """One of a chain's eight claims as the chain view gives it: the graph claims that state it (none: the run did
    not state it), the view's reads of them, and what the chain names for it (entity ids, and symbols with no claim
    of their own)."""
    claim_ids: list[str]
    label: str
    reads: list[Mapping[str, Any]] = field(default_factory=list)
    entities: list[str] = field(default_factory=list)
    genes: list[str] = field(default_factory=list)


def _short(values: list[str], empty: str) -> str:
    values = _unique(values)
    if len(values) > LABEL_SHOWN:
        return "; ".join(values[:LABEL_SHOWN]) + f" and {len(values) - LABEL_SHOWN} more"
    return "; ".join(values) or empty


def _chain_slots(graph: ClaimGraph, row: Mapping[str, Any],
                 candidates: Mapping[str, Mapping[str, Mapping[str, Any]]],
                 location: Mapping[str, Any]) -> dict[str, _Asked]:
    """One ranked chain of the chain view as the eight claims. The view's five links are the four allele claims and
    the gene-to-trait premise; its target gene link also holds the element-to-gene claims (relation regulates), which
    are the gene step's premise; the claims it lists as a factor's context (occupies, expressed_in) are the binding
    step's premise, and its location claims (overlaps) the activity step's. A claim the run did not state still
    names what the chain names: its TF, the variant's element, its gene, its traits."""
    filled = {link: [candidates[link][k] for k in row["cells"][link]["candidates"]] for link in LINK_KEYS}

    def reads(link: str, keep=lambda relation: True) -> list[Mapping[str, Any]]:
        return [r for c in filled[link] for r in c["claims"] if keep(r["relation"])]

    def ids(link: str) -> list[str]:
        return _unique(e for c in filled[link] for e in c["key"].split("+") if e in graph.entities)

    def label(link: str, empty: str) -> str:
        return _short([c["short"] for c in filled[link]] or list(row["cells"][link]["names"]), empty)

    def asked(link: str, text: str, entities: list[str], keep=lambda relation: True) -> _Asked:
        found = reads(link, keep)
        return _Asked([r["id"] for r in found], text, found, entities, loose)

    factor, gene, trait = ids("binding"), ids("gene"), ids("trait")
    loose = [] if filled["gene"] else list(row["cells"]["gene"]["names"])      # a gene with no target gene claim
    # "the gene bears on the trait" is every standing gene-to-trait claim that names the chain's gene, not only the
    # strongest ones the view shows in the chain's cell: a locus-to-gene score beside a colocalisation is part of it
    named = set(gene) or {e for e in ids("mediation") if graph.entities[e].kind in ("gene", "transcript")}
    filled["mediation"] = [c for c in candidates["mediation"].values()
                           if c["level"] >= 0 and named & set(c["key"].split("+"))] if named else []
    elements = _unique(e for c in location["claims"] for e in c["elements"]) or list(location["found_by_code"])
    tf_label, gene_label = label("binding", NO_NAME["binding"]), label("gene", NO_NAME["gene"])
    trait_label = label("trait", NO_NAME["trait"])
    return {
        "binding.allele": asked("binding", tf_label, factor),
        "binding.premise": _Asked(_unique(x["id"] for c in filled["binding"] for x in c["context"]), tf_label,
                                  entities=factor),
        "activity.allele": asked("activity", label("activity", _short(elements, NO_NAME["activity"])),
                                 ids("activity")),
        "activity.premise": _Asked([c["id"] for c in location["claims"]], _short(elements, NO_NAME["activity"])),
        "gene.allele": asked("gene", gene_label, gene, lambda relation: relation != "regulates"),
        "gene.premise": asked("gene", gene_label, gene, lambda relation: relation == "regulates"),
        "trait.allele": asked("trait", trait_label, trait),
        "trait.premise": asked("mediation", label("mediation", f"{gene_label} → {trait_label}"),
                               _unique([*ids("mediation"), *gene, *trait])),
    }


def _merge(a: Mapping[str, list[str]], b: Mapping[str, list[str]]) -> dict[str, list[str]]:
    return {kind: _unique([*a.get(kind, []), *b.get(kind, [])]) for kind in NAME_KINDS}


def _ident(key: str, asked: _Asked) -> str:
    """A claim's id in the table: its slot and the graph claims that state it, or, for one the run did not state,
    what the chain names for it. Long lists are cut to their first id, their length and a checksum."""
    parts = asked.claim_ids or [*asked.entities, *asked.genes]
    body = "+".join(parts)
    if len(parts) > 6:
        body = f"{parts[0]}+{len(parts) - 1}more.{zlib.crc32(body.encode()):08x}"
    return f"{key}:{body}" if asked.claim_ids else f"{key}:({body})"


EMPTY_ROW: dict[str, Any] = {"rank": 1, "ties": 1, "title": "no chain stated",
                             "cells": {link: {"candidates": [], "names": []} for link in LINK_KEYS}}


def from_graph(graph: ClaimGraph) -> Table:
    """A saved claim-graph run as a chain table: one row per chain of chain.chain_view's ranking, in its order, each
    with all eight claims. A claim no claim of the graph states has `stated` False and still names what the chain
    names, so its cells report the run's lookups and the records on file. A run with no chain at all gets one row of
    eight unstated claims: the table then says what was on file and never judged. Deterministic for a graph."""
    view = chain_view(graph)
    index = _Index(graph)
    candidates = {item["key"]: {c["key"]: c for c in item["candidates"]} for item in view["links"]}
    table = Table(case_id=graph.case.case_id, variant=graph.case.variant.key,
                  beside=[{"claim": u["id"], "relation": u["relation"], "why": u["why"]} for u in view["unplaced"]])
    for row in view["ranked"]["chains"] or [EMPTY_ROW]:
        claims: dict[str, str | None] = {}
        for key, asked in _chain_slots(graph, row, candidates, view["location"]).items():
            asked.claim_ids = _unique(asked.claim_ids)
            ident = _ident(key, asked)
            if ident not in table.claims:
                slot = SLOTS[key]
                names = _merge(_names(graph, asked.claim_ids, slot), _entity_names(graph, asked.entities, slot))
                names["genes"] = _unique([*names["genes"], *asked.genes])
                predictions = [r["prediction"] for r in asked.reads if r.get("prediction")]
                cells = {lane: _cell(graph, index, slot, lane, asked.claim_ids, names, predictions)
                         for lane in LANE_KEYS}
                table.claims[ident] = TableClaim(id=ident, step=slot.step, part=slot.part, text=slot.text,
                                                 label=asked.label, names=names, graph_claims=asked.claim_ids,
                                                 stated=bool(asked.claim_ids), cells=cells,
                                                 strongest=_strongest(cells))
            claims[key] = ident
        table.chains.append(TableChain(rank=row["rank"], ties=row["ties"], title=row["title"], claims=claims,
                                       joined=list(row.get("joined") or [])))
    return table


# --- the checker -------------------------------------------------------------------------------------------------------

def check(table: Table, graph: ClaimGraph) -> list[Problem]:
    """Every way the table breaks RULES, read against the run's own files (the graph's evidence and tool calls), not
    against the table's copy of them. Empty: the table passes. Needs no known answer."""
    problems: list[Problem] = []
    index = _Index(graph)

    def add(rule: str, where: str, text: str) -> None:
        problems.append(Problem(rule=rule, where=where, text=text))

    for i, chain in enumerate(table.chains, 1):
        where = f"chain {i}"
        if list(chain.claims) != list(SLOT_KEYS):
            add("shape", where, f"its claims are {', '.join(chain.claims) or 'none'}, not the eight slots in order")
        for key, ident in chain.claims.items():
            if ident is None:
                add("shape", f"{where}, {key}", "the chain has no claim here: every chain has all eight")
            elif ident not in table.claims:
                add("shape", f"{where}, {key}", f"names claim {ident}, which the table does not hold")
            elif (table.claims[ident].step, table.claims[ident].part) != tuple(key.split(".")):
                add("shape", f"{where}, {key}", f"claim {ident} belongs to another slot")
    for ident, claim in table.claims.items():
        key = f"{claim.step}.{claim.part}"
        slot = SLOTS.get(key)
        if slot is None:
            add("shape", ident, f"{key} is not one of the eight slots")
            continue
        if list(claim.cells) != list(LANE_KEYS):
            add("shape", ident, f"its cells are {', '.join(claim.cells) or 'none'}, not the three kinds in order")
        if claim.stated != bool(claim.graph_claims) or any(c not in graph.claims for c in claim.graph_claims):
            add("shape", ident, "says a claim of the run states it, and the run's files hold no such claim"
                if claim.stated else "names claims of the run and says the run did not state it")
        for lane, cell in claim.cells.items():
            where = f"{ident}, {lane}"
            if cell.state not in STATE_KEYS:
                add("shape", where, f"{cell.state} is not a state")
                continue
            rows = sources_for(key, lane)
            counted = {r.stance for r in cell.records} - {"beside"}
            expected = ({"supports", "disagrees"} if cell.state == "both" else {cell.state}
                        if cell.state in FILLED else set())
            if counted != expected:
                add("record", where, f"says {STATE_WORDS[cell.state]} but counts "
                                     f"{' and '.join(sorted(counted)) or 'no'} records")
            for r in cell.records:
                ev = graph.evidence.get(r.id)
                if ev is None:
                    add("record", where, f"{r.id} is not in the run's files")
                    continue
                if lane_of(ev) != lane:
                    add("record", where, f"{r.id} is a {lane_of(ev)} record")
                if r.stance == "beside":
                    continue
                tool = _tool(graph, ev)
                if ev.origin == "tool" and not listed(key, lane, tool, ev):
                    add("record", where, f"{r.id} ({ev.evidence_class} from {tool}) is not a source the map lists "
                                         "for this cell")
                if not can_count(slot, ev):
                    add("record", where, f"{r.id} ({ev.evidence_class}) is a kind of record that cannot count for "
                                         "this claim")
                if slot.part == "allele" and not names_case(graph, ev):
                    add("variant", where, f"{r.id} does not name this variant")
                if lane == "literature" and (ev.experiment is None or not ev.experiment.passage.strip()
                                             or not ev.source_ids):
                    add("quoted", where, f"{r.id} has no quoted passage or names no article")
            if cell.state == "nothing_found":
                done = [t for t in cell.lookups if t in graph.tool_calls
                        and graph.tool_calls[t].execution_status == "success"]
                if not done or len(done) != len(cell.lookups):
                    add("looked", where, "says nothing found but cites no completed lookup" if not done else
                        "cites a lookup that did not complete")
            if cell.state == "no_source" and rows and not cell.note:
                add("looked", where, "says no source although the map lists one, and gives no reason")
            if cell.state != "no_source" and not rows:
                add("looked", where, f"says {STATE_WORDS[cell.state]} although the map lists no source for this cell")
            if rows:
                judged = {r.id for r in cell.records} | {s.record for s in cell.set_aside}
                left = unjudged_records(graph, slot, lane, claim.names, judged, index)
                if left:
                    shown = ", ".join(left[:6]) + (f" and {len(left) - 6} more" if len(left) > 6 else "")
                    add("unjudged", where, f"{len(left)} record(s) on file name what it names and have no "
                                           f"judgement: {shown}")
    return problems


def counts(table: Table, problems: Iterable[Problem] = ()) -> dict[str, Any]:
    """The numbers a table is read by, for its first chain (the leading one; `tied` says how many share its rank):
    how many of its eight claims the run stated, how many have a supporting record of any kind, its 24 cells by
    state, and per kind of record how many of the cells that have a source hold support. `unjudged` counts the
    records on file with no judgement, over those cells."""
    states = {key: 0 for key in STATE_KEYS}
    lanes = {lane: {"with_source": 0, "supported": 0} for lane in LANE_KEYS}
    stated = supported = unjudged = 0
    parts = {part: {"stated": 0, "supported": 0} for part, _ in PARTS}
    strongest: dict[str, str] = {}
    first = table.chains[0] if table.chains else None
    for key in SLOT_KEYS:
        part = key.split(".")[1]
        for lane in LANE_KEYS:
            lanes[lane]["with_source"] += bool(sources_for(key, lane))
        ident = first.claims.get(key) if first else None
        if ident is None:
            continue
        claim = table.claims[ident]
        stated += claim.stated
        parts[part]["stated"] += claim.stated
        held = any(cell.state in ("supports", "both") for cell in claim.cells.values())
        supported += held
        parts[part]["supported"] += held
        strongest[key] = claim.strongest
        for lane, cell in claim.cells.items():
            states[cell.state] += 1
            lanes[lane]["supported"] += cell.state in ("supports", "both")
            unjudged += cell.unjudged_total
    by_rule = {key: 0 for key in RULE_KEYS}
    for p in problems:
        by_rule[p.rule] = by_rule.get(p.rule, 0) + 1
    return {"chains": len(table.chains), "tied": first.ties if first else 0, "title": first.title if first else None,
            "claims_stated": stated, "claims_supported": supported, "parts": parts, "strongest": strongest,
            "cells": states, "lanes": lanes, "unjudged": unjudged, "problems": by_rule}


# --- plain text ----------------------------------------------------------------------------------------------------------

def _cell_words(cell: Cell) -> str:
    counted = [r for r in cell.records if r.stance != "beside"]
    if cell.state in FILLED:
        kinds = _unique(r.kind or r.evidence_class.replace("_", " ") for r in counted)
        text = f"{STATE_WORDS[cell.state]}: {len(counted)} ({', '.join(kinds)})"
    else:
        text = STATE_WORDS[cell.state] + (f" ({cell.note})" if cell.note else "")
    for n, what in ((len(cell.records) - len(counted), "beside"), (len(cell.set_aside), "set aside"),
                    (cell.unjudged_total, "on file, not judged")):
        if n:
            text += f"; {n} {what}"
    return text


def source_table() -> str:
    """The source map as a Markdown table, one row per claim: what can fill each cell today (docs/chain-table.md
    carries it, and a test keeps the two the same)."""
    step_names = dict(STEPS)
    lines = ["| Claim | Database | Model prediction | Literature |", "|---|---|---|---|"]
    for key, slot in SLOTS.items():
        cells = []
        for lane in LANE_KEYS:
            tools = _unique(s.tool for s in sources_for(key, lane))
            cells.append("articles" if lane == "literature" and tools else ", ".join(f"`{t}`" for t in tools)
                         or "no source")
        part = "alleles differ" if slot.part == "allele" else "in place"
        lines.append(f"| {step_names[slot.step]}: {part} | {' | '.join(cells)} |")
    return "\n".join(lines)


TABLE_HEADERS = ["Step", "Claim", "Names", "Database", "Model prediction", "Literature"]
PASSES = "The table passes every rule of docs/chain-table.md."


def first_rows(table: Table) -> list[list[str]]:
    """The first chain's eight claims as plain text cells (TABLE_HEADERS): what each names, marked when the run did
    not state it, and its three cells in words."""
    if not table.chains:
        return []
    step_names, part_names = dict(STEPS), dict(PARTS)
    rows = []
    for key in SLOT_KEYS:
        ident = table.chains[0].claims.get(key)
        if ident is None:
            continue
        claim = table.claims[ident]
        named = claim.label + ("" if claim.stated else " (not stated by the run)")
        rows.append([step_names[claim.step], part_names[claim.part], named,
                     *(_cell_words(claim.cells[lane]) for lane in LANE_KEYS)])
    return rows


QUOTES_PER_CLAIM = 4            # quotations a report shows under one claim; the table file holds every record
STANCE_WORDS = {"supports": "for the claim", "contradicts": "against the claim", "beside": "beside the claim"}


def first_quotes(table: Table) -> list[dict[str, Any]]:
    """The sentences the first chain's literature records were read from, claim by claim: each passage once, with
    the article it is from, how its records count and how many records quote it. Counted records come first, and at
    most QUOTES_PER_CLAIM passages are given per claim (`more` says how many were left out)."""
    if not table.chains:
        return []
    step_names, part_names = dict(STEPS), dict(PARTS)
    out = []
    for key in SLOT_KEYS:
        ident = table.chains[0].claims.get(key)
        if ident is None:
            continue
        claim = table.claims[ident]
        quoted: dict[tuple[str, str], dict[str, Any]] = {}
        records = [r for r in claim.cells["literature"].records if r.passage]
        for r in sorted(records, key=lambda r: r.stance == "beside"):
            entry = quoted.setdefault((r.sources[0] if r.sources else "", r.passage), {
                "source": r.sources[0] if r.sources else "", "passage": r.passage,
                "counts": STANCE_WORDS.get(r.stance, r.stance), "kind": r.kind or r.evidence_class.replace("_", " "),
                "records": 0, **({"second": r.note} if r.stance != "beside" and r.note else {})})
            entry["records"] += 1
        if quoted:
            shown = list(quoted.values())
            out.append({"step": step_names[claim.step], "claim": part_names[claim.part], "names": claim.label,
                        "quotes": shown[:QUOTES_PER_CLAIM], "more": max(0, len(shown) - QUOTES_PER_CLAIM)})
    return out


def report_view(graph: ClaimGraph) -> dict[str, Any]:
    """What a run report shows of the table: the first chain's rows, the sentences its literature records quote,
    how many chains tie with it, and the rules the whole table breaks, by rule. JSON-native and deterministic for a
    graph."""
    table = from_graph(graph)
    problems = check(table, graph)
    numbers = counts(table, problems)
    broken = {rule: n for rule, n in numbers["problems"].items() if n}
    return {"headers": list(TABLE_HEADERS), "rows": first_rows(table), "chains": numbers["chains"],
            "tied": numbers["tied"], "title": numbers["title"], "stated": numbers["claims_stated"],
            "supported": numbers["claims_supported"], "cells": numbers["cells"], "broken": broken,
            "reading": reading_text(graph), "critique": critique_text(graph), "quotes": first_quotes(table),
            "judgement": judgement(graph),
            "rules": (PASSES if not broken else "The table breaks its rules: " + "; ".join(
                f"{rule} {n} time{'s' if n != 1 else ''}" for rule, n in broken.items()) + ".")}


def _searched(reading: Mapping[str, Any]) -> bool:
    """Whether the reader's searches all completed: only then does an empty list mean no article was found."""
    searches = reading.get("searches") or []
    return bool(searches) and all(str(x.get("status", "")).startswith("success/") for x in searches)


def reading_text(graph: ClaimGraph) -> str:
    """One sentence on where the literature column comes from, for a report: what the reader found, read and
    filed; empty for a run without the reader."""
    r = _Index(graph).reading
    if r is None:
        return ""
    if not r.get("found"):
        return f"Literature: {NO_ARTICLE if _searched(r) else NO_SEARCH}."
    left = [f"{r[key]} {words}" for key, words in (("no_mention", "did not name the variant in the text retrieved"),
                                                    ("review", "were reviews"), ("unreadable", "could not be retrieved"),
                                                    ("failed", "failed in the model call"),
                                                    ("over_cap", "were beyond the cap")) if r.get(key)]
    return (f"Literature: {r['found']} articles naming the variant were found and {r.get('read', 0)} read, each once, "
            f"by a model that returned {r.get('experiments', 0)} experiments; {r.get('accepted', 0)} passed code's "
            "checks against the text and were filed as records"
            + (f". Of the rest, {', '.join(left)}." if left else "."))


def critique_text(graph: ClaimGraph) -> str:
    """One sentence on the second reading, for a report: how many of the experiments code would have counted the
    critic read, and what it found; empty for a run without the critic."""
    c = _Index(graph).critique
    if c is None:
        return ""
    if not c.get("records"):
        return "Second reading: no experiment from an article was up for counting, so the critic read none."
    faults = ", ".join(f"{n} {name.replace('_', ' ')}" for name, n in sorted((c.get("faults") or {}).items()))
    if int(c.get("format") or 1) < 2:                      # a run whose critic read every record code counted
        asked = int(c.get("records") or 0)
        which = (f"{asked} experiments code would have counted, each with its paragraph and the claims it would "
                 "count for")
    else:
        asked = int(c.get("asked") or 0)
        if not asked:
            return (f"Second reading: none of the {c['records']} experiments code counts is the only record behind "
                    "a cell, so an answer on any of them could not change a cell, and the second model read none.")
        which = (f"{asked} experiments that are the only record behind a cell, each with its paragraph and the "
                 f"claims it counts for (code counts {c['records']} in all, and an answer on any other could not "
                 "change a cell)")
    left = asked - int(c.get("reviewed") or 0)
    pointed, unsent = int(c.get("extended") or 0), int(c.get("alone_not_sent") or 0)
    return (f"Second reading: a second model, from another provider, read {c.get('reviewed', 0)} of the {which}. "
            f"Of {c.get('claims', 0)} claims checked it found {c.get('shown', 0)} shown, "
            f"{c.get('not_shown', 0)} not shown" + (f" ({faults})" if faults else "")
            + f" and could not tell for {c.get('cannot_tell', 0)}. A record is not counted for a claim it found "
            "not shown; it can add nothing"
            + (f". For {pointed} claim(s) it found the result in further sentences of the paragraph, which code "
               "copied into the quotation" if pointed else "")
            + (f". {left} were not read (a failed call, the cap, or the critic stopped: "
               f"{c.get('stopped') or 'no stop'}) and stay counted" if left else "")
            + (f". {unsent} record(s) ended up alone behind a cell without being read" if unsent else "") + ".")


def judgement(graph: ClaimGraph) -> dict[str, Any] | None:
    """What the judge read of a tie for first (judge.py), for a report: one sentence, and for each candidate it
    was asked about its answer, its reason and the quotations the answer rests on. None for a run without a judge
    or without a tie."""
    from . import judge as J
    index = _Index(graph)
    if index.judgement is None:
        return None
    rows = []
    for r in index.judged:
        basis = J.BASIS_WORDS.get((r["kind"], r["basis"]), "")
        rows.append({"candidate": f"{J.KIND_SHORT[r['kind']]} {r['label']}", "answer": r["answer"],
                     "words": J.ANSWER_WORDS[r["answer"]] + (f": {basis}" if basis else ""),
                     "agreed": r.get("agreed"), "reason": r.get("reason", ""),
                     "on_file": r.get("on_file", 0), "sent": r.get("sent", 0),
                     "quotes": [{"id": q["id"], "source": q.get("source", ""), "passage": q.get("passage", ""),
                                 "pointed": bool(q.get("pointed"))} for q in r.get("records") or []]})
    return {"text": J.sentence(index.judgement, index.judged), "rows": rows,
            "chains": index.judgement.get("chains"), "orders": index.judgement.get("orders")}


def to_markdown(table: Table, problems: Iterable[Problem] = ()) -> str:
    """The first chain's table and the rules it breaks, as Markdown (graph text is escaped for a table cell)."""
    def esc(text: str) -> str:
        return text.replace("|", "\\|").replace("\n", " ")

    problems = list(problems)
    lines = [f"# Chain table: {esc(table.case_id)} ({esc(table.variant)})", ""]
    if not table.chains:
        lines += ["The table holds no chain.", ""]
    else:
        first = table.chains[0]
        tied = f", tied with {first.ties - 1} other(s)" if first.ties > 1 else ""
        lines += [f"Chain 1 of {len(table.chains)}{tied}: {esc(first.title)}", ""]
        if first.joined:
            lines += [f"The TF and the gene belong together: {len(first.joined)} experiment(s) on file changed the "
                      f"TF and saw the gene change ({', '.join(first.joined)}). This breaks ties only.", ""]
        lines += ["| Step | Claim | Names | Database | Model prediction | Literature |", "|---|---|---|---|---|---|"]
        step_names, part_names = dict(STEPS), dict(PARTS)
        for key in SLOT_KEYS:
            step, part = key.split(".")
            ident = first.claims.get(key)
            if ident is None:
                lines.append(f"| {step_names[step]} | {part_names[part]} | no claim | | | |")
                continue
            claim = table.claims[ident]
            cells = " | ".join(esc(_cell_words(claim.cells[lane])) for lane in LANE_KEYS)
            named = esc(claim.label) + ("" if claim.stated else " (not stated by the run)")
            lines.append(f"| {step_names[step]} | {part_names[part]} | {named} | {cells} |")
        lines.append("")
    if problems:
        lines += [f"## Rules broken ({len(problems)})", ""]
        lines += [f"- {p.rule}: {esc(p.where)}: {esc(p.text)}" for p in problems]
    else:
        lines.append("The table passes every rule.")
    return "\n".join(lines) + "\n"
