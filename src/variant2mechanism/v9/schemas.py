"""The v9 data contract: every object the claim graph holds, and the rules that tie evidence classes to claims.

One module, because the graph, the tool runner, the role packets, the report and the evaluation all read the same
objects. These are internal models (defaults allowed). The strict, default-free models a language model fills live in
roles.py and are converted into these.

Three status layers never mix:
- retrieval: what a tool returned (ToolCall.execution_status and retrieval_status);
- assessment: what the linked evidence lets us say about one scoped claim (Claim.assessment);
- disposition: how a hypothesis is currently handled (Hypothesis.disposition).
An empty retrieval creates no Evidence, so missing data can never become a contradiction. A measured null (an assay
whose scope is known and which saw nothing) is Evidence with result_kind "null_in_assessed_scope".

The evidence-class x relation matrix (DIRECT, INDIRECT, QUALIFIED_DIRECT) is data here and enforced in graph.py:
only a DIRECT class can make a claim supported or contradicted in scope; an INDIRECT class (a QBiC-SELEX prediction,
an association, an L2G score) can be linked but leaves the claim unresolved, and is shown as its basis.

Directions about the case variant are read in an allele frame: a claim names its effect allele (the alt allele unless
it says otherwise) and an observation names the allele its direction refers to, so "T binds more" and "G binds less"
are the same observation and can never support "G binds more".
"""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

Origin = Literal["somatic", "germline", "unknown"]
ExecutionStatus = Literal["success", "error", "unavailable", "cache_miss", "not_applicable"]
RetrievalStatus = Literal["records_found", "no_records_found", "incomplete", "unknown"]
Assessment = Literal["unassessed", "unresolved", "supported_in_scope", "contested", "contradicted_in_scope"]
Disposition = Literal["active", "deferred", "leading", "tied", "rejected", "superseded"]
Stance = Literal["supports", "contradicts", "context_only", "unresolved"]
Applicability = Literal["exact", "proxy", "different", "unknown"]
EvidenceClass = Literal[
    "annotation",              # coordinate/consequence overlap, element registry, nearby genes
    "prediction",              # QBiC-SELEX, executed or cached by us
    "precomputed_prediction",  # retrieved model output, e.g. Open Targets L2G
    "statistical_inference",   # credible sets, PIP, colocalisation
    "association",             # GWAS, eQTL
    "expression",              # RNA/protein levels: permissive, not occupancy
    "occupancy",               # ChIP-seq and comparable
    "binding_assay",           # EMSA, allele-specific binding experiments
    "reporter_assay",          # luciferase, MPRA
    "perturbation",            # CRISPR, knockdown, overexpression, region disruption
    "dependency_screen",       # DepMap gene effect
    "clinical_assertion",      # CIViC, ClinVar
    "review",                  # a review's retelling: never a second experimental observation
    "metadata_audit",          # e.g. a context mismatch found by code or critic
    "synthetic",               # fixture-only; never in biological results
]
Relation = Literal[
    "overlaps", "expressed_in", "occupies", "alters_binding", "alters_regulatory_activity", "regulates",
    "associated_with_expression", "affects_process", "associated_with_trait", "causal_at_locus",
    "contributes_to_trait", "alters_rna", "other",
]
Direction = Literal["increases", "decreases", "creates", "abolishes", "no_change", "unspecified"]
MechanismClass = Literal["tf_binding", "regulatory", "rna_processing", "coding", "association_only", "other"]
EntityKind = Literal["variant", "tf", "tf_group", "binding_event", "element", "gene", "transcript", "process",
                     "phenotype", "context", "complex"]
Role = Literal["code", "coordinator", "computational_investigator", "literature_investigator", "critic",
               "judge"]             # judge: the fill's reading of a tie (judge.py); the engine has none
Outcome = Literal["leading_explanation", "partial_mechanism", "multiple_explanations", "no_supported_explanation",
                  "input_or_capability_limitation"]
ComparisonOutcome = Literal["A_preferred", "B_preferred", "tied", "complementary", "insufficient_evidence"]
StopReason = Literal["converged", "no_affordable_discriminating_action", "coordinator_stop", "budget_model_calls",
                     "budget_tool_calls", "budget_currency", "wall_time", "regeneration_limit", "input_invalid",
                     "cache_miss", "unsupported_variant",
                     "engine_error"]       # an internal failure stopped the run (recorded, never raised out of it)
RunMode = Literal["live", "cache_only", "fixture"]
ResultKind = Literal["effect", "null_in_assessed_scope"]
BiosampleKind = Literal["cell_line", "primary_cell", "tissue", "organism", "unknown"]
ContextSource = Literal["supplied", "inferred", "evidence", "unspecified"]
DependencyFlag = Literal["none", "unsupported_due_to_dependency"]
PathStatus = Literal["intact", "premise_failed", "superseded"]   # one entry per claim of a hypothesis
LinkStrength = Literal["direct", "indirect", "context"]          # what the class matrix allows this link to do
DisplayStatus = Literal["supported", "predicted", "associated", "contested", "contradicted", "unresolved"]
ChargedTo = Literal["agent", "code", "none"]                     # which tool budget a call used ("none": not run)
QuestionStatus = Literal["open", "answered", "unanswerable", "deferred", "refused"]
EventAction = Literal[
    "normalize", "collect_facts", "propose", "activate", "defer", "ask", "tool_call", "attach_evidence", "assess",
    "refuse_update", "new_claim", "supersede_claim", "revise_hypothesis", "reject", "regenerate", "compare", "audit",
    "decide", "stop", "review_evidence",
    "add_evidence",            # evidence not created by a tool call (an extracted experiment, a metadata audit)
    "propagate",               # code: dependency flags and hypothesis paths changed (assessments never do)
    "add_dependency",          # a duplicate claim draft brought premises the existing claim did not have
    "add_inferred_candidate",  # a disease or context the run inferred (stored on the case, never as supplied)
    "add_variant_alias",       # code: an rsID a tool reports at the case variant's exact coordinates and alleles
    "add_variant_element",     # code: an element a tool reports as containing the case variant
    "reinstate",               # code: a rejection whose contradiction was withdrawn is undone, once (graph.reinstate)
]
ParamValue = str | int | float | bool | list[str]

SPECIFIC_DIRECTIONS = {"increases": 1, "creates": 1, "decreases": -1, "abolishes": -1}  # creates~increases etc.
ASSESSORS: frozenset[str] = frozenset({"coordinator", "critic", "code"})
INVESTIGATORS: frozenset[str] = frozenset({"computational_investigator", "literature_investigator"})

# --- the evidence class x relation matrix (SPEC 13.6) -------------------------------------------------------------
# DIRECT: can make a claim supported_in_scope / contradicted_in_scope. INDIRECT: can be linked as supports or
# contradicts but leaves the claim at most unresolved. Anything else may only be linked as context_only.
DIRECT: dict[str, frozenset[str]] = {
    "overlaps": frozenset({"annotation"}),
    "expressed_in": frozenset({"expression"}),
    "occupies": frozenset({"occupancy"}),
    "alters_binding": frozenset({"binding_assay"}),
    "alters_regulatory_activity": frozenset({"reporter_assay", "perturbation"}),
    "regulates": frozenset({"perturbation"}),
    "associated_with_expression": frozenset({"association", "statistical_inference"}),
    "affects_process": frozenset({"perturbation", "dependency_screen"}),
    "associated_with_trait": frozenset({"association", "statistical_inference", "clinical_assertion"}),
    "causal_at_locus": frozenset(),
    "contributes_to_trait": frozenset(),
    "alters_rna": frozenset({"perturbation", "reporter_assay"}),
    "other": frozenset(),
}
INDIRECT: dict[str, frozenset[str]] = {
    "overlaps": frozenset(),
    "expressed_in": frozenset(),
    "occupies": frozenset({"binding_assay"}),
    "alters_binding": frozenset({"prediction", "occupancy"}),
    "alters_regulatory_activity": frozenset({"binding_assay"}),
    "regulates": frozenset({"association", "statistical_inference", "precomputed_prediction", "annotation",
                            "reporter_assay"}),
    "associated_with_expression": frozenset(),
    "affects_process": frozenset({"association"}),
    "associated_with_trait": frozenset(),
    "causal_at_locus": frozenset({"statistical_inference", "association", "perturbation", "reporter_assay"}),
    "contributes_to_trait": frozenset({"association", "statistical_inference", "clinical_assertion",
                                       "precomputed_prediction", "perturbation"}),
    "alters_rna": frozenset({"annotation", "prediction"}),
    "other": frozenset(),
}
# INDIRECT entries that become DIRECT only when the evidence states the qualifier as True in Evidence.data: an
# ordinary ChIP peak does not test allele dependence; a region-disrupting CRISPR or an unedited reporter does not
# show that this allele (not an LD partner) is causal; a cell-culture perturbation is not an organismal trait test.
QUALIFIED_DIRECT: dict[tuple[str, str], str] = {
    ("alters_binding", "occupancy"): "allele_specific",
    ("causal_at_locus", "perturbation"): "allele_targeted",
    ("causal_at_locus", "reporter_assay"): "allele_targeted",
    ("contributes_to_trait", "perturbation"): "in_vivo",
}
# A qualified entry added after the engine's prompts were fixed (14 Nov 2026). The graph enforces it like the ones
# above. It is kept apart because roles.class_matrix_text() prints QUALIFIED_DIRECT into the engine's prompts, and a
# changed prompt would stop the saved engine runs from replaying; only the fill sets this flag (v9/proteins.py).
# Allele-specific ChIP-seq reads of a protein that does not bind DNA itself (a co-factor, a chromatin reader) show
# that the state of the site differs between the alleles. They do not show that a TF reads the variant, so the flag
# is a different one from allele_specific and no such record counts for alters_binding through it. Allele-specific
# reads of open chromatin (DNase-seq, ATAC-seq: fill_sources.py) show the same thing and name no protein at all; they
# carry a flag of their own. Any one of an entry's flags is enough.
QUALIFIED_DIRECT_FILL: dict[tuple[str, str], tuple[str, ...]] = {
    ("alters_regulatory_activity", "occupancy"): ("allele_specific_cofactor", "allele_specific_accessibility"),
}
CONTEXT_ONLY_CLASSES: frozenset[str] = frozenset({"review", "metadata_audit"})
# Classes whose result does not depend on a cell or tissue context: coordinates, sequence-level predictions, population
# statistics, clinical assertions and stipulated fixtures. Only these agree exactly with an unscoped claim when they
# are unscoped themselves; any other class with no recorded context transfers as "unknown" (a lost context is not a
# match), and a measured null never does (its assessed scope must be stated).
CONTEXT_FREE_CLASSES: frozenset[str] = frozenset({
    "annotation", "prediction", "precomputed_prediction", "statistical_inference", "association",
    "clinical_assertion", "synthetic"})
# Relations whose claims about the case variant compare its two alleles inside cells. An allele-resolved readout of
# the endogenous alleles (Evidence.data["allele_specific"] True: allelic imbalance, allele-specific ChIP reads) needs
# both alleles present, so from a context homozygous at the variant it is context only for these claims.
ALLELIC_RELATIONS: frozenset[str] = frozenset({
    "alters_binding", "alters_regulatory_activity", "alters_rna", "causal_at_locus", "associated_with_expression"})
# Relations a hypothesis may require. expressed_in and occupies never: expression and ChIP coverage can at most defer
# a TF hypothesis, never reject it (SPEC 13.8).
REQUIRABLE: frozenset[str] = frozenset({
    "overlaps", "alters_binding", "alters_regulatory_activity", "regulates", "associated_with_expression",
    "affects_process", "associated_with_trait", "causal_at_locus", "contributes_to_trait", "alters_rna", "other"})
# Display basis order, most experimental first (used only to pick the class a badge names).
CLASS_ORDER: tuple[str, ...] = (
    "perturbation", "reporter_assay", "binding_assay", "occupancy", "dependency_screen", "clinical_assertion",
    "statistical_inference", "association", "precomputed_prediction", "prediction", "expression", "annotation",
    "synthetic", "review", "metadata_audit")
ASSOCIATED_BASIS: frozenset[str] = frozenset({"association", "statistical_inference", "precomputed_prediction"})
PREDICTED_BASIS: frozenset[str] = frozenset({"prediction"})


class V9Model(BaseModel):
    """Every v9 model forbids unknown fields, so a typo in a fixture or a saved graph fails loudly."""
    model_config = ConfigDict(extra="forbid")


# --- the case --------------------------------------------------------------------------------------------------------

def variant_type_of(ref: str, alt: str) -> Literal["SNV", "indel", "other"]:
    """SNV: one A, C, G or T on each side. indel: plain bases whose lengths differ (VCF style, with the anchor base).
    other: a same-length multi-base change (an MNV is not an insertion or deletion), or an allele that is not plain
    bases (empty, "-", N, a symbolic allele such as <DEL>), whose length says nothing about what changed."""
    ref, alt = ref.strip().upper(), alt.strip().upper()
    if not ref or not alt or set(ref + alt) - set("ACGT"):
        return "other"
    if len(ref) == len(alt) == 1:
        return "SNV"
    return "indel" if len(ref) != len(alt) else "other"


class Variant(V9Model):
    assembly: str = "GRCh38"
    chrom: str                                   # no "chr" prefix
    pos: int                                     # 1-based
    ref: str
    alt: str
    rsid: str | None = None
    input_text: str = ""
    reference_check: Literal["verified", "mismatch", "unavailable"] = "unavailable"
    variant_type: Literal["SNV", "indel", "other"]

    @model_validator(mode="before")
    @classmethod
    def _type(cls, data: Any) -> Any:
        """Fill variant_type from the alleles when it is omitted (an explicit type is kept). Tools refuse the types
        they do not cover (QBiC-SELEX scores SNVs only), so a wrong guess would run a tool where it does not apply."""
        if isinstance(data, dict) and not data.get("variant_type"):
            data = {**data, "variant_type": variant_type_of(str(data.get("ref") or ""), str(data.get("alt") or ""))}
        return data

    @field_validator("chrom")
    @classmethod
    def _chrom(cls, v: str) -> str:
        v = v.strip()
        return v[3:] if v.lower().startswith("chr") else v

    @field_validator("ref", "alt")
    @classmethod
    def _allele(cls, v: str) -> str:
        return v.strip().upper()

    @property
    def key(self) -> str:
        """The canonical identity used for the variant entity: GRCh38:chrom:pos:ref:alt."""
        return f"{self.assembly}:{self.chrom}:{self.pos}:{self.ref}:{self.alt}"


class ContextScope(V9Model):
    label: str = ""                              # as given or observed
    biosample: str | None = None                 # normalised name (context_match), or None
    biosample_kind: BiosampleKind = "unknown"
    tissue: str | None = None                    # organ-level tissue, lower case
    species: str = "human"
    condition: str | None = None                 # treatment or state (e.g. lipid-loaded)
    genotype: str | None = None                  # genotype at the case variant, when a source states it
    source: ContextSource = "unspecified"


class InferredCandidate(V9Model):
    kind: Literal["disease", "context"]
    label: str
    basis_evidence_ids: list[str] = Field(default_factory=list)
    note: str = ""


class Case(V9Model):
    case_id: str
    variant: Variant
    origin: Origin = "unknown"
    supplied_disease: list[str] = Field(default_factory=list)
    supplied_context: list[ContextScope] = Field(default_factory=list)
    inferred_candidates: list[InferredCandidate] = Field(default_factory=list)
    input_provenance: dict[str, str] = Field(default_factory=dict)

    @property
    def synthetic(self) -> bool:
        """Synthetic fixture cases (ids starting SYN-) are the only ones that may hold synthetic evidence."""
        return self.case_id.startswith("SYN-")


# --- tools and evidence ----------------------------------------------------------------------------------------------

class ToolRequest(V9Model):
    tool: str
    params: dict[str, ParamValue] = Field(default_factory=dict)
    purpose: str = ""


class Coverage(V9Model):
    requested_scope: str = ""
    assessed_scope: str = ""
    limitations: list[str] = Field(default_factory=list)


class ToolCall(V9Model):
    """One tool request and what it returned. Retrieval only: biology lives in evidence links on claims."""
    tool_call_id: str
    tool_name: str
    tool_version: str = ""
    query_parameters: dict[str, ParamValue] = Field(default_factory=dict)   # canonical once validated
    purpose: str = ""
    provider: str = ""
    dataset_release: str = ""
    assembly: str | None = None
    retrieval_time: str = ""                     # ISO 8601; excluded from replay comparison
    raw_result_hash: str | None = None           # sha256 hex of raw/T#.json as written
    execution_status: ExecutionStatus
    retrieval_status: RetrievalStatus = "unknown"
    observations: list[dict[str, Any]] = Field(default_factory=list)
    coverage: Coverage = Field(default_factory=Coverage)
    raw_result_path: str | None = None           # relative to the run folder
    evidence_ids: list[str] = Field(default_factory=list)
    requested_by: Role
    question_id: str | None = None
    cached: bool = False
    message: str = ""
    charged_to: ChargedTo = "none"
    # Set only for a read that returned the article (success, records_found or incomplete): an empty or failed read
    # consumes no full-text budget and nothing can be extracted from it.
    fulltext_article: str | None = None          # the article a full-text read consumed from the budget
    read_article: str | None = None              # the article a literature read returned (full text or abstract)
    # Every identifier of that article (PMID digits, PMC<digits>, lower-case DOI; graph.article_key), including the
    # one it was requested by: one article requested by PMCID and later by PMID is one read, never two.
    article_ids: list[str] = Field(default_factory=list)


class ExperimentSystem(V9Model):
    organism: str = ""
    tissue_or_cell: str = ""
    treatment: str = ""
    # The context's genotype at the variant as the paper states it ("TT", "heterozygous"): it decides whether an
    # allele-resolved readout can compare the alleles there. It is never the allele a direction refers to (a region
    # deleted in TT cells says nothing about T); that is ExperimentRecord.compared_allele.
    genotype_or_allele: str = ""


Manipulated = Literal["allele", "element", "tf", "gene", "none"]


class ExperimentRecord(V9Model):
    source_id: str                               # "PMID:..."
    pmcid: str | None = None
    doi: str | None = None
    publication_type: str = ""
    access: Literal["full_text", "abstract_only"]
    location: str                                # section + paragraph/figure/table id
    passage: str                                 # exact bounded text, verified against the source
    system: ExperimentSystem = Field(default_factory=ExperimentSystem)
    intervention: str = ""
    endpoint: str = ""
    comparator: str = ""
    result: str = ""
    direction: Direction = "unspecified"
    scope_supports: str = ""
    scope_does_not_test: str = ""
    about_tfs: list[str] = Field(default_factory=list)
    about_genes: list[str] = Field(default_factory=list)
    about_traits: list[str] = Field(default_factory=list)
    # The regions the experiment manipulated or measured, as the paper names them. Without them a TF knockdown that
    # changed a gene would pass as a test of what an element does; the graph lets evidence support or contradict a
    # claim about an element only when it names that element. A region named by the case variant ("the enhancer
    # containing rs1427407") names the elements code recorded as containing the variant.
    about_elements: list[str] = Field(default_factory=list)
    # The variants the experiment is about, as the paper names them (an rsID, or chrom:pos with optional alleles);
    # empty when it names none (an element-, gene- or cell-line-level experiment). Papers test an LD partner next to
    # the variant of interest, often in the same figure, and an assay of one variant says nothing about another's
    # alleles. The literature route keeps the entries the verified passage supports and copies them into
    # Evidence.about_variants, the list the graph checks.
    about_variants: list[str] = Field(default_factory=list)
    # What the experiment changed, which decides what it can test. "allele": the variant's alleles compared or edited
    # (EMSA or reporter with both alleles, base or prime editing, allele-specific expression); "element": a region
    # deleted, repressed, activated or tested in a reporter without an allele comparison; "tf": a TF knocked down,
    # knocked out or overexpressed; "gene": the target gene manipulated; "none": observational (ChIP, eQTL,
    # association, imaging).
    manipulated: Manipulated = "none"
    # Only for designs that compare alleles: the allele whose effect `direction` describes, as written in the passage
    # (e.g. "T"). Never a genotype: system.genotype_or_allele is the context's genotype, and reading it as the
    # compared allele would turn a region deletion in TT cells into a statement about the T allele.
    compared_allele: str | None = Field(default=None, description="Single effect allele, e.g. T, never a mutation "
                                      "pair such as C>T. Use the paper strand; code separately verifies case mapping.")
    authors_hypothesis_vs_result: Literal["result", "hypothesis", "mixed"] = "result"


class Evidence(V9Model):
    """One observation or retrieved result. evidence_id is issued by the graph: pass "" when adding.

    The about_* lists say what the observation is about; the graph's identity checks read them, so an item may only
    support or contradict claims about the TFs, genes, elements, traits and variants it names. `allele` is the allele
    its direction refers to (an allele of the case variant, as a base or "ref"/"alt"); `data` holds JSON-native
    values."""
    evidence_id: str = ""
    evidence_class: EvidenceClass
    source_ids: list[str] = Field(default_factory=list)
    raw_artifact_ref: str | None = None
    retrieval_ref: str | None = None             # the tool call that produced it
    observed_result: str                         # one factual sentence (code for adapters, extractor for papers)
    data: dict[str, Any] = Field(default_factory=dict)
    allele: str | None = None
    direction: Direction = "unspecified"
    context: ContextScope | None = None
    about_tfs: list[str] = Field(default_factory=list)
    about_genes: list[str] = Field(default_factory=list)
    about_elements: list[str] = Field(default_factory=list)
    about_traits: list[str] = Field(default_factory=list)       # trait labels or ontology ids (EFO_...)
    # The variants the observation is about, as the source names them: an rsID, or a GRCh38 chrom:pos with optional
    # alleles ("chr2:60490908 T>G"). Empty: it names no variant (an element-, gene- or cell-line-level observation).
    # Evidence naming only other variants never supports or contradicts a claim about the case variant (an LD
    # partner tested in the same paper is not the case variant), and evidence that compares alleles must say whose
    # alleles it compared before it can bear on an allelic claim (graph.link).
    about_variants: list[str] = Field(default_factory=list)
    independence_group: str
    origin: Literal["tool", "literature", "fixture"]
    access: Literal["dataset", "full_text", "abstract_only", "metadata_only", "not_applicable"] = "dataset"
    experiment: ExperimentRecord | None = None
    limitations: list[str] = Field(default_factory=list)
    result_kind: ResultKind = "effect"
    assessed_relation: Relation | None = None    # for a measured null: the relation its assay's scope tests


def evidence_strength(relation: str, evidence: Evidence) -> LinkStrength:
    """What the class matrix lets this evidence do for a claim with this relation (synthetic is DIRECT everywhere;
    whether it may be used at all depends on the case and is checked by the graph). A qualifier (allele_specific,
    allele_targeted, in_vivo) counts only as the flag the adapter or extractor set in `data`, never as a context
    label a proposer wrote; a passage that states the authors' hypothesis rather than a result is context only."""
    cls = evidence.evidence_class
    if cls == "synthetic":
        return "direct"
    if cls in CONTEXT_ONLY_CLASSES:
        return "context"
    if evidence.experiment is not None and evidence.experiment.authors_hypothesis_vs_result == "hypothesis":
        return "context"
    if relation == "other":
        return "indirect"
    qualifier = QUALIFIED_DIRECT.get((relation, cls))
    if qualifier is not None and evidence.data.get(qualifier) is True:
        return "direct"
    if any(evidence.data.get(flag) is True for flag in QUALIFIED_DIRECT_FILL.get((relation, cls), ())):
        return "direct"
    if cls in DIRECT.get(relation, ()):
        return "direct"
    if cls in INDIRECT.get(relation, ()):
        return "indirect"
    return "context"


# --- the claim graph -------------------------------------------------------------------------------------------------

class EvidenceLink(V9Model):
    claim_id: str
    evidence_id: str
    stance: Stance
    applicability: Applicability                 # stored value: code's, or a weaker match the proposer named (proxy,
                                                 # different); a proposed "unknown" is no judgement and leaves code's,
                                                 # except on a contradicts link, where it is kept
    rationale: str = ""
    limitations: list[str] = Field(default_factory=list)
    proposed_by: Role
    event_id: str = ""                           # the event that accepted it
    code_applicability: Applicability            # what code computed with context_match
    corrected: bool = False                      # the proposer claimed a stronger applicability than code allows
    strength: LinkStrength                       # direct / indirect / context, from the class matrix
    downgraded_from: Stance | None = None        # a supports/contradicts link stored as context_only (different
                                                 # context, or an allele-resolved readout from a homozygous context)
    revises: str | None = None                   # the event id of the earlier link to this evidence it replaced


class Entity(V9Model):
    entity_id: str
    kind: EntityKind
    canonical_id: str | None = None
    label: str
    participants: list[str] = Field(default_factory=list)    # entity ids (tf_group members, complex parts)
    qualifiers: dict[str, str] = Field(default_factory=dict)


class ClaimHistoryEntry(V9Model):
    version: int
    assessment: Assessment
    event_id: str
    action: Literal["new_claim", "attach_evidence", "assess"]    # what made this version
    rationale: str = ""


class Claim(V9Model):
    claim_id: str
    version: int = 1                             # +1 per evidence link and per assessment (optimistic concurrency)
    subject_ids: list[str]
    relation: Relation
    object_ids: list[str]
    direction: Direction = "unspecified"         # for a claim about the case variant: what effect_allele does
    effect_allele: str | None = None             # the case variant's ref or alt (default alt); None without a variant
    allele_scope: str | None = None              # e.g. "T vs G (alt vs ref)"
    context_scope: ContextScope | None = None
    mechanism_class: MechanismClass = "other"
    assertion_text: str = ""
    assessment: Assessment = "unassessed"
    assessment_rationale: str = ""
    dependency_flag: DependencyFlag = "none"
    dependencies: list[str] = Field(default_factory=list)
    evidence_links: list[EvidenceLink] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    supersedes: str | None = None
    superseded_by: str | None = None
    proposed_by: Role
    history: list[ClaimHistoryEntry] = Field(default_factory=list)


class Hypothesis(V9Model):
    hypothesis_id: str
    version: int = 1
    title: str
    summary: str = ""
    claim_ids: list[str] = Field(default_factory=list)
    required_claim_ids: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    context: ContextScope | None = None
    endpoint: str = "molecular"                  # trait/phenotype label, or "molecular"
    mechanism_class: MechanismClass = "other"
    disposition: Disposition = "active"
    disposition_reason: str = ""
    revisit_trigger: str | None = None
    origin: Literal["initial", "regenerated", "evidence_led"] = "initial"
    replaces: str | None = None
    member_alternatives: list[str] = Field(default_factory=list)
    missing_links: list[str] = Field(default_factory=list)
    reason_for_inclusion: str = ""
    signature: str = ""                          # code-computed structural key (anti-repeat)
    path_status: dict[str, PathStatus] = Field(default_factory=dict)
    history: list[dict[str, Any]] = Field(default_factory=list)


class Rubric(V9Model):
    consequence: Literal["high", "medium", "low"] = "medium"
    discrimination: Literal["high", "medium", "low"] = "medium"
    applicability: Literal["high", "medium", "low"] = "medium"
    cost: Literal["high", "medium", "low"] = "medium"


class Question(V9Model):
    question_id: str = ""                        # issued by the graph
    text: str
    target_claim_ids: list[str] = Field(default_factory=list)
    hypothesis_ids: list[str] = Field(default_factory=list)
    route: Literal["computational", "literature"]
    rubric: Rubric = Field(default_factory=Rubric)
    possible_outcomes: list[str] = Field(default_factory=list)
    actions: list[ToolRequest] = Field(default_factory=list)
    status: QuestionStatus = "open"
    answer_summary: str = ""
    remaining_gap: str = ""
    round: int = 0


class BudgetSnapshot(V9Model):
    model_calls: int = 0
    tool_calls: int = 0                          # agent-initiated, charged against the tool budget
    code_tool_calls: int = 0                     # code's fact collection, counted separately
    fulltext_reads: int = 0                      # unique articles read in full
    cost_usd: float = 0.0


class DecisionEvent(V9Model):
    """An append-only record of one reviewable decision; never hidden chain-of-thought."""
    event_id: str
    graph_version_before: int
    graph_version_after: int
    role: Role
    action: EventAction
    target_ids: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
    concise_reason: str = ""
    supersedes: list[str] = Field(default_factory=list)
    budget_snapshot: BudgetSnapshot = Field(default_factory=BudgetSnapshot)
    details: dict[str, Any] = Field(default_factory=dict)


class PairComparison(V9Model):
    comparison_id: str = ""                      # issued by the graph
    a: str
    b: str
    outcome: ComparisonOutcome
    decisive_claim_ids: list[str] = Field(default_factory=list)
    decisive_gaps: list[str] = Field(default_factory=list)
    reason: str = ""
    accepted: bool = True
    refusal_reason: str = ""


class NextExperiment(V9Model):
    text: str
    distinguishes: list[str] = Field(default_factory=list)
    claim_ids: list[str] = Field(default_factory=list)
    performed: Literal[False] = False            # suggested, never performed


class WeakLink(V9Model):
    hypothesis_id: str
    claim_id: str
    why: str


class RunResult(V9Model):
    outcome: Outcome
    budget_stop: bool = False
    stop_reason: StopReason
    leading_ids: list[str] = Field(default_factory=list)
    summary: str = ""
    weakest_links: list[WeakLink] = Field(default_factory=list)
    next_experiments: list[NextExperiment] = Field(default_factory=list)
    uninvestigated_questions: list[str] = Field(default_factory=list)
    downgraded_from: Outcome | None = None
    downgrade_reason: str = ""


class ClaimDisplay(V9Model):
    """Derived for the report, never stored as truth: the status badge, its basis class and the dependency badge."""
    status: DisplayStatus
    basis: EvidenceClass | None = None           # the class the badge names
    basis_classes: list[EvidenceClass] = Field(default_factory=list)   # every class among accepted supports
    dependency_flag: DependencyFlag = "none"
