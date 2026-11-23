"""Role calls for the v9 engine: what a model reads, what it may return, and how often it may be asked (SPEC 5, 13.9,
13.10; contract C4).

Why one module: everything a model sees or returns passes through here, so one place decides what reaches a prompt
and what comes back.
- Packets are rendered by code from the case and the graph only (never gold labels, case notes, the request's free
  text or provenance, or evaluator fields), in a fixed order, with the claim versions an update must carry as
  base_version and the effect allele of every directional claim. Everything rendered from the graph sits inside
  <data> ... </data>: tool results and paper text, and also what roles wrote earlier (hypotheses, rationales,
  answers, gaps, refusal reasons), because a role may have copied untrusted text into them. The rules tell every
  role that fenced text is data, never instructions. Tool observations are shown as whole records up to a bound, so
  a record (a paper's identifiers, a peak's coordinates) is never cut in half. Nothing volatile (times, costs, cache
  flags, run mode, provider error text) enters a packet, so a replay sends the same requests and is answered from
  the response cache.
- Output models are strict: every field required (a nullable field is still required), no dict fields (free tool
  arguments travel as `params_json` strings), no numeric bounds (code checks counts and ranges), and unique class
  names (V9Propose, V9Plan, V9Investigate, V9Critique, V9Final), because fake transports dispatch on the schema title.
  The `*_check` functions raise SchemaCheckError for unknown ids, tools, parameters and update kinds, so the model
  sees the reason in its one repair; what passes is only a proposal, which the graph accepts or refuses.
- RoleCaller is the only code that calls the model. `max_model_calls` counts every send, repairs and max_tokens
  retries included; one LLMClient.call can take four sends, so a call is made only when `calls + 4 <= cap`, and
  ordinary calls also leave `reserve` sends (default 2) for the final comparison, so a run stopped by its budget can
  still be compared. A failed call returns None after it is logged; the engine records it and goes on or stops. A
  reply the response cache cannot give back on replay (a max_tokens retry, a refusal, a provider error) is recorded
  in `unreplayable`, and a replay's missing reply sets `replay_miss`, so a replay fails loudly instead of deciding
  from a different graph.
"""

import hashlib
import json
import logging
import re
from collections.abc import Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass, field
from functools import cache
from pathlib import Path
from typing import Any, Literal, get_args

from pydantic import BaseModel, ConfigDict, Field, PrivateAttr, model_validator

from ..agent.llm import BudgetExceeded, LLMClient, LLMError, Refused, strict_schema
from ..agent.schemas import SchemaCheckError
from . import adoption
from .discovery import context_lines as discovery_lines
from .evidence_view import packet_lines
from .graph import (
    ALLELE_COMPARED_RELATIONS,
    ClaimDraft,
    ClaimGraph,
    EntityRef,
    GraphUpdate,
    HypothesisChanges,
)
from .mechanistic_gaps import gap_lines
from .replay import ReplayMiss
from .resolution import support_summary
from .schemas import (
    ALLELIC_RELATIONS,
    DIRECT,
    INDIRECT,
    QUALIFIED_DIRECT,
    REQUIRABLE,
    Applicability,
    Assessment,
    Case,
    ComparisonOutcome,
    ContextScope,
    Direction,
    EntityKind,
    ExperimentRecord,
    ExperimentSystem,
    Manipulated,
    MechanismClass,
    Outcome,
    Question,
    Relation,
    Rubric,
    Stance,
    ToolRequest,
)
from .tools import ToolBudget, ToolRefusal, ToolSpec, canonical_params

log = logging.getLogger(__name__)

GUARD = 4                   # sends one LLMClient.call can take: reply, max_tokens retry, repair, its retry
DEFAULT_MAX_CALLS = 24
DEFAULT_RESERVE = 2         # sends kept back for the final comparison
DEFAULT_ROLE_KEYS = {"coordinator": "generator", "computational_investigator": "generator",
                     "literature_investigator": "generator", "critic": "critic", "extraction": "summariser"}
ROUTE_ROLE = {"computational": "computational_investigator", "literature": "literature_investigator"}
TITLE_ROLE = {"V9Propose": "coordinator", "V9Plan": "coordinator", "V9Critique": "critic", "V9Final": "critic"}
PROMPT_DIR = Path(__file__).with_name("prompts")
PROMPT_NAMES = ("rules", "coordinator_system", "coordinator_propose", "coordinator_plan", "investigator_system",
                "investigator_computational", "investigator_literature", "critic_system", "critic_audit",
                "critic_final")
MAX_OBSERVATIONS = 4000     # characters of one tool call's observations in a packet (whole records only; a
                            # literature search is bounded to about 3 800 by the literature module, so it fits whole)
MAX_READ = 16000            # ... of a literature read (the adapter already bounds an article to about 14 000)
MAX_DATA = 600              # ... of one evidence item's data
# A reason for inclusion that is only a rank: a rank phrase ("largest |z|", "highest TPM", "strongest predicted
# binding change") or a peak phrase ("a ChIP-seq peak"), and nothing else once numbers, group ids, filler words and
# short "in/at/among ..." qualifiers are set aside (SPEC 13.5: the critic flags such activations; code asks for a
# reason before it accepts the sketch).
RANK_PHRASE = re.compile(
    r"\b(?:largest|highest|strongest|biggest|greatest|best|top|maximum|max|most\s+significant|lowest)"
    r"(?:\s+(?:absolute|predicted|binding|allelic|qbic(?:-selex)?|median|mean|chip(?:-?seq)?))*"
    r"\s+(?:z(?:[- ]?scores?)?|tpm|expression(?:\s+levels?)?|scores?|signal|ranks?|effects?(?:\s+sizes?)?|"
    r"changes?|differences?|p(?:[- ]?values?)?)\b|\b(?:ranked|ranks)\s+(?:first|top|highest)\b|\btop[- ]ranked\b")
PEAK_PHRASE = re.compile(r"\b(?:an?\s+|the\s+)?(?:chip(?:-?seq)?|encode|remap)\s+peaks?\b")
QUALIFIER = re.compile(r"\b(?:in|at|among|across|of|for|on|over|within|from|by)\b(?:\s+[\w./+-]+){1,4}")
FILLER = frozenset({"it", "this", "that", "these", "its", "their", "the", "a", "an", "has", "have", "had", "shows",
                    "show", "showing", "with", "is", "are", "was", "were", "group", "groups", "tf", "tfs", "factor",
                    "factors", "model", "models", "value", "values", "variant", "site", "inventory", "all", "any",
                    "other", "others", "overall", "and", "or", "than", "z", "only", "here", "one"})


# --- strict output models ---------------------------------------------------------------------------------------------

class Strict(BaseModel):
    """Base of every model a language model fills: closed objects and no defaults, so every field is required."""
    model_config = ConfigDict(extra="forbid")


Level = Literal["high", "medium", "low"]
ReasonKind = Literal["predicted_allelic_binding", "regulatory_annotation", "genetic_association",
                     "literature_report", "prior_knowledge", "member_or_paralog_alternative", "distinct_mechanism",
                     "supplied_input"]
ChallengeKind = Literal["overclaim", "wrong_applicability", "evidence_dependence", "unsupported_causal_language",
                        "missing_alternative", "direction_mismatch", "source_mismatch", "context_mismatch"]


class V9Entity(Strict):
    kind: EntityKind
    label: str = Field(description="a symbol, element id, trait or the case variant's rsID or chrom:pos")
    canonical_id: str | None = Field(description="for a tf_group, its QBiC-SELEX group id as the inventory lists "
                                                 "it (G followed by digits); an element's id when known; a "
                                                 "phenotype ontology id supplied by the source, else null. Keep "
                                                 "the full source trait label including measurement/population "
                                                 "qualifiers; a shared broad id does not merge these scopes")
    members: list[str] = Field(description="member TF symbols of a complex or binding_event; empty otherwise "
                                           "(a QBiC-SELEX group's members come from the registry)")


class V9Context(Strict):
    label: str = Field(description="a biosample, cell type or tissue name as given or observed")
    species: str
    condition: str | None


APPLICABILITY_FIELD = ("null leaves the context match code computes; proxy or different states a weaker match (give the "
                       "reason in the rationale); unknown is read as null on a supports link and withholds the "
                       "contradiction on a contradicts link")


class V9Link(Strict):
    evidence_id: str
    stance: Stance
    applicability: Applicability | None = Field(description=APPLICABILITY_FIELD)
    rationale: str
    suggested_assessment: Assessment | None


class V9Claim(Strict):
    key: str = Field(description="a short name, unique in this answer")
    subjects: list[V9Entity]
    relation: Relation
    objects: list[V9Entity]
    direction: Direction
    effect_allele: str | None = Field(description="for a claim about the case variant: the allele whose effect the "
                                                  "direction states (ref or alt; null means alt)")
    context: V9Context | None
    assertion_text: str
    required: bool
    depends_on: list[str] = Field(description="claim keys of this answer, or existing claim ids")
    initial_links: list[V9Link]


class V9ClaimUse(Strict):
    ref: str = Field(description="an existing claim id, or the key of a claim defined in another sketch")
    required: bool


class V9Action(Strict):
    tool: str
    params_json: str = Field(description="the parameters as a JSON object")
    purpose: str


class V9Rubric(Strict):
    consequence: Level
    discrimination: Level
    applicability: Level
    cost: Level


class V9Question(Strict):
    text: str
    route: Literal["computational", "literature"]
    target_claims: list[str] = Field(description="claim ids, or claim keys of this answer")
    hypotheses: list[str] = Field(description="hypothesis ids, or sketch keys of this answer")
    rubric: V9Rubric
    possible_outcomes: list[str]
    actions: list[V9Action]


class V9Sketch(Strict):
    key: str
    title: str
    summary: str
    mechanism_class: MechanismClass
    endpoint: str = Field(description='"molecular", or the trait or phenotype the mechanism reaches')
    context: V9Context | None
    activate: bool
    deferral_reason: str | None
    revisit_trigger: str | None
    reason_kind: ReasonKind
    reason_detail: str = Field(description="the specific reason; a rank (largest z, highest TPM, a ChIP peak) is not "
                                           "a reason")
    member_alternatives: list[str]
    missing_links: list[str]
    assumptions: list[str]
    replaces: str | None = Field(description="on regeneration: the rejected hypothesis this one answers, or null")
    claims: list[V9Claim]
    reuse_claims: list[V9ClaimUse]


class V9Inferred(Strict):
    kind: Literal["disease", "context"]
    label: str
    basis_evidence_ids: list[str]
    note: str


class V9Reactivate(Strict):
    hypothesis_id: str
    reason: str


class V9Propose(Strict):
    directions: list[str]
    inferred_candidates: list[V9Inferred]
    hypotheses: list[V9Sketch]
    fourth_active_reason: str | None
    reactivate: list[V9Reactivate]
    questions: list[V9Question]


class V9Revision(Strict):
    title: str | None
    summary: str | None
    endpoint: str | None
    assumptions: list[str] | None
    member_alternatives: list[str] | None
    missing_links: list[str] | None
    remove_claim_ids: list[str]


class V9HypothesisUpdate(Strict):
    hypothesis_id: str
    action: Literal["revise", "defer", "activate", "reject", "supersede_claim", "add_claim",
                    "replace_required_claim"]
    reason: str
    claim_id: str | None = Field(description="supersede_claim and replace_required_claim: the claim replaced; "
                                             "add_claim: an existing claim to add (or null with new_claim)")
    new_claim: V9Claim | None
    new_claim_id: str | None = Field(description="replace_required_claim: an existing replacement claim id")
    required: bool
    revisit_trigger: str | None
    revision: V9Revision | None


class V9Assess(Strict):
    claim_id: str
    base_version: int = Field(description="the claim version shown in the packet")
    assessment: Assessment
    rationale: str


class V9Stop(Strict):
    stop: bool
    reason: str


class V9Discovery(Strict):
    sketch: V9Sketch
    basis_evidence_ids: list[str]


class V9EvidenceDecision(Strict):
    evidence_ids: list[str]
    disposition: Literal["represented", "defer", "set_aside"]
    claim_refs: list[str] = Field(description="existing claim ids or keys of claims added in this plan; "
                                            "represented requires a non-context evidence link in a hypothesis")
    reason: str
    revisit_trigger: str | None


class V9Plan(Strict):
    hypothesis_updates: list[V9HypothesisUpdate]
    new_hypotheses: list[V9Discovery]
    inferred_candidates: list[V9Inferred]
    evidence_decisions: list[V9EvidenceDecision]
    assessments: list[V9Assess]
    questions: list[V9Question]
    stop: V9Stop
    _legacy_adoption: bool = PrivateAttr(default=False)

    @model_validator(mode="wrap")
    @classmethod
    def old_script(cls, value, handler):
        """Read saved pre-adoption scripts; new model requests still require all fields in their strict schema."""
        names = ("new_hypotheses", "inferred_candidates", "evidence_decisions")
        legacy = isinstance(value, dict) and not any(n in value for n in names)
        if legacy:
            value = {**value, **{n: [] for n in names}}
        out = handler(value)
        out._legacy_adoption = legacy
        return out


class V9Experiment(Strict):
    source_id: str = Field(description="PMID:<number>")
    pmcid: str | None
    doi: str | None
    publication_type: str
    access: Literal["full_text", "abstract_only"]
    location: str = Field(description="the location id shown with the passage, e.g. sec2/p3 or fig1")
    passage: str = Field(description="one exact, contiguous passage of 20 to 600 characters, or an @span:start:end "
                                     "selector supplied in a source-local repair packet (code copies the sentence)")
    organism: str
    tissue_or_cell: str
    treatment: str
    genotype_or_allele: str = Field(description="the genotype of the system at the variant as the paper states it "
                                                "(e.g. a homozygous cell line); never the allele compared")
    intervention: str = Field(description="what the experiment manipulated or applied (the assay)")
    endpoint: str = Field(description="what it measured (the readout)")
    comparator: str
    result: str
    direction: Direction
    scope_supports: str
    scope_does_not_test: str
    about_tfs: list[str]
    about_genes: list[str]
    about_elements: list[str] = Field(description="the regions the experiment manipulated or measured, as the paper "
                                                  "names them, or by the case variant (the enhancer containing "
                                                  "<rsID>)")
    about_traits: list[str]
    about_variants: list[str] = Field(description="the variant(s) the experiment tested, as the passage, its heading "
                                                  "or caption names them (an rsID, or chromosome:position with its "
                                                  "alleles); empty when it names none. An allele comparison must "
                                                  "name the variant whose alleles it compared")
    manipulated: Manipulated = Field(description="allele (the variant's alleles compared or edited), element, tf, "
                                                 "gene, or none (observational)")
    compared_allele: str | None = Field(description="only for designs that compare alleles: the allele whose effect "
                                                    "direction describes, as written in the passage; null otherwise, "
                                                    "never a genotype")
    authors_hypothesis_vs_result: Literal["result", "hypothesis", "mixed"]


class V9Proposal(Strict):
    kind: Literal["attach_evidence", "assess", "new_claim", "supersede_claim"]
    claim_id: str | None = Field(description='a claim id, or "key:<key>" of a claim proposed earlier in this answer')
    base_version: int | None = Field(description="the claim version shown in the packet")
    evidence_id: str | None
    experiment_index: int | None = Field(description="0-based index into this answer's experiments")
    stance: Stance | None
    applicability: Applicability | None = Field(description=APPLICABILITY_FIELD)
    rationale: str
    limitations: list[str]
    suggested_assessment: Assessment | None
    new_claim: V9Claim | None


class V9Answer(Strict):
    question_id: str
    status: Literal["answered", "unanswerable", "needs_follow_up"]
    answer_summary: str
    claim_ids: list[str] = Field(description='existing claim ids, or "key:<key>" for new claims declared in '
                                            'this answer; this list is metadata, not an evidence link')
    tool_call_ids: list[str]
    experiments: list[V9Experiment]
    proposed_updates: list[V9Proposal]
    remaining_gap: str
    next_question: str
    follow_up_actions: list[V9Action]


class V9Investigate(Strict):
    answers: list[V9Answer]
    # Semantic errors in individual updates must not discard independently verifiable experiments.
    _proposal_errors: dict[tuple[int, int], list[str]] = PrivateAttr(default_factory=dict)


class V9Challenge(Strict):
    claim_id: str
    base_version: int
    kind: ChallengeKind
    evidence_ids: list[str]
    gap: str
    requested_action: V9Action | None
    suggested_assessment: Assessment | None


class V9PassageCheck(Strict):
    evidence_id: str
    verdict: Literal["faithful", "misread", "not_in_source", "scope_exceeded"]
    note: str


class V9ActivationFlag(Strict):
    hypothesis_id: str
    reason: str


class V9Critique(Strict):
    challenges: list[V9Challenge]
    passage_checks: list[V9PassageCheck]
    activation_flags: list[V9ActivationFlag]
    reportable_ids: list[str]
    consequential: bool


class V9Comparison(Strict):
    a: str
    b: str
    outcome: ComparisonOutcome
    decisive_claim_ids: list[str]
    decisive_gaps: list[str]
    reason: str


class V9WeakLink(Strict):
    hypothesis_id: str
    claim_id: str
    why: str


class V9NextExperiment(Strict):
    text: str
    distinguishes: list[str]
    claim_ids: list[str]


class V9Outcome(Strict):
    category: Outcome
    leading_ids: list[str]
    summary: str
    weakest_links: list[V9WeakLink]
    next_experiments: list[V9NextExperiment]


class V9Final(Strict):
    comparisons: list[V9Comparison]
    outcome: V9Outcome


OUTPUT_MODELS: tuple[type[Strict], ...] = (V9Propose, V9Plan, V9Investigate, V9Critique, V9Final)


# --- prompts, role keys and limits -------------------------------------------------------------------------------------

@cache
def prompt(name: str) -> str:
    """One prompt file's text (prompts/<name>.txt)."""
    return (PROMPT_DIR / f"{name}.txt").read_text().strip()


def prompt_hashes() -> dict[str, str]:
    """sha256 of each prompt file, for the manifest."""
    return {n: hashlib.sha256((PROMPT_DIR / f"{n}.txt").read_bytes()).hexdigest() for n in PROMPT_NAMES}


def schema_hashes() -> dict[str, str]:
    """sha256 of each output model's strict schema (what the model is asked to fill), for the manifest."""
    return {m.__name__: hashlib.sha256(json.dumps(strict_schema(m), sort_keys=True).encode()).hexdigest()
            for m in OUTPUT_MODELS}


def _listed(names: Iterable[str], conjunction: str) -> str:
    items = sorted(names)
    return items[0] if len(items) == 1 else f"{', '.join(items[:-1])} {conjunction} {items[-1]}"


def class_matrix_text() -> str:
    """The evidence class x relation matrix as the prompts state it, generated from schemas so it cannot drift from
    what graph.py enforces."""
    lines = ["Evidence classes per claim relation (code enforces this matrix):"]
    for rel in get_args(Relation):
        if rel == "other":
            lines.append("- other: indirect for any class except review and metadata_audit")
            continue
        qualified = [f"{cls} only when data.{flag} is true" for (r, cls), flag in sorted(QUALIFIED_DIRECT.items())
                     if r == rel]
        direct = ", ".join(sorted(DIRECT[rel]) + qualified) or "none"
        indirect = ", ".join(sorted(INDIRECT[rel])) or "none"
        lines.append(f"- {rel}: direct {direct}; indirect {indirect}")
    lines += ["- review and metadata_audit are context only for every relation; so is a passage that states the "
              "authors' hypothesis rather than a result. synthetic fixture evidence is direct, in synthetic cases "
              "only.",
              "Experiments on what the variant's alleles do (a claim with the variant as its subject and one of the "
              f"relations {_listed(ALLELIC_RELATIONS, 'or')}): a TF or gene perturbation (knockdown, knockout, "
              "overexpression) is context only, because it shows that the factor matters, not that the alleles "
              f"differ; for {_listed(ALLELE_COMPARED_RELATIONS, 'and')} claims, an experiment that does not compare "
              "the two alleles (a region deletion, CRISPRi of the element, a single-allele assay) is at most "
              "indirect.",
              "Direct evidence with exact or proxy applicability can make a claim supported_in_scope or "
              "contradicted_in_scope; direct evidence on both sides makes it contested. Indirect evidence can be "
              "linked as supports or contradicts but leaves the claim unresolved (shown as predicted or "
              "associated). Any other class may only be linked as context_only."]
    return "\n".join(lines)


def system_prompt(role: str, route: str | None = None) -> str:
    """rules + class matrix + the role's own instructions (and the route's, for an investigator)."""
    parts = [prompt("rules"), class_matrix_text()]
    if role == "coordinator":
        parts.append(prompt("coordinator_system"))
    elif role == "critic":
        parts.append(prompt("critic_system"))
    else:
        parts += [prompt("investigator_system"), prompt(f"investigator_{route}")]
    return "\n\n".join(parts)


def role_keys(config: Mapping[str, Any]) -> dict[str, str]:
    """v9 role -> LLMClient key (generator, critic or summariser): `v9.roles` over the SPEC 13.10 defaults
    (coordinator and both investigators -> generator, critic -> critic, passage extraction -> summariser)."""
    given = ((config.get("v9") or {}).get("roles")) or {}
    return {**DEFAULT_ROLE_KEYS, **{k: str(v) for k, v in given.items() if k in DEFAULT_ROLE_KEYS}}


def model_call_limits(config: Mapping[str, Any]) -> tuple[int, int]:
    """(max_model_calls, reserve_model_calls) from `v9.limits`, with the SPEC 13.9 defaults."""
    limits = ((config.get("v9") or {}).get("limits")) or {}
    return (int(limits.get("max_model_calls", DEFAULT_MAX_CALLS)),
            int(limits.get("reserve_model_calls", DEFAULT_RESERVE)))


def script_role(body: dict) -> str:
    """The v9 role a request body belongs to (for ScriptedResponses.transport): the schema title, and for an
    investigator call the role named on the packet's first line."""
    title = (((body.get("response_format") or {}).get("json_schema") or {}).get("schema") or {}).get("title")
    if title in TITLE_ROLE:
        return TITLE_ROLE[title]
    first = next((m.get("content") or "" for m in body.get("messages", []) if m.get("role") == "user"), "")
    found = re.match(r"Role: (\w+)", first)
    if title == "V9Investigate" and found:
        return found.group(1)
    raise ValueError(f"no v9 role for a request with schema title {title!r}")


# --- ids and text helpers ----------------------------------------------------------------------------------------------

def id_order(item_id: str) -> tuple[str, int]:
    """Sort key for graph ids (C2 before C10)."""
    found = re.fullmatch(r"([A-Z]+)(\d+)", item_id)
    return (found.group(1), int(found.group(2))) if found else (item_id, 0)


def sort_ids(ids: Iterable[str]) -> list[str]:
    return sorted(set(ids), key=id_order)


def fence(text: Any) -> str:
    """Untrusted text cannot open or close a data fence."""
    return re.sub(r"<(/?)(data)", r"&lt;\1\2", str(text), flags=re.I)


def compact(value: Any, limit: int) -> str:
    """Compact, key-sorted JSON, cut at `limit` characters with a note (deterministic)."""
    text = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), default=str)
    return text if len(text) <= limit else f"{text[:limit]} ... [cut: {len(text)} characters in all]"


def rank_only(detail: str) -> bool:
    """Whether a reason for inclusion is nothing but a rank (largest z, highest TPM, a ChIP peak), however it is
    phrased: once rank and peak phrases, numbers and bracketed values, group ids, filler words and short qualifiers
    ("in the inventory", "among C2H2 groups", "at the variant in HepG2") are set aside, nothing is left. A reason
    that also states something else (an allele, a motif, an assay, an element) is not rank-only."""
    text = re.sub(r"\([^)]*\)|\[[^\]]*\]", " ", detail.lower().replace("|", " "))
    stripped, found = RANK_PHRASE.subn(" ", text)
    stripped, peaks = PEAK_PHRASE.subn(" ", stripped)
    if not found + peaks:
        return False
    stripped = QUALIFIER.sub(" ", stripped)
    words = [w for w in re.findall(r"[a-z][a-z0-9-]*", stripped) if w not in FILLER and not re.fullmatch(r"g\d+", w)]
    return not words


def scope_text(scope: ContextScope | None) -> str:
    if scope is None or not (scope.biosample or scope.tissue or scope.condition or scope.species != "human"):
        return "none"
    parts = [scope.biosample or (f"{scope.tissue} tissue" if scope.tissue else scope.label)]
    if scope.biosample and scope.tissue:
        parts.append(f"tissue {scope.tissue}")
    if scope.species != "human":
        parts.append(scope.species)
    if scope.condition:
        parts.append(f"condition {scope.condition}")
    if scope.genotype:
        parts.append(f"genotype at the variant {scope.genotype}")
    return ", ".join(parts) + f" [{scope.source}]"


def allele_side(case: Case, allele: str | None) -> str:
    v = case.variant
    if not allele:
        return ""
    if allele.upper() == v.alt:
        return f"{allele} (alt)"
    if allele.upper() == v.ref:
        return f"{allele} (ref)"
    return allele


# --- packet rendering --------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class PacketBudget:
    """What a packet says about resources: deterministic counts only (no time, no cost)."""
    model_used: int
    model_cap: int
    model_reserve: int
    tools: ToolBudget
    fulltext_soft: int
    fulltext_hard: int
    regenerations_used: int
    max_regenerations: int

    def text(self) -> str:
        t = self.tools
        return (f"Budget: model calls {self.model_used} of {self.model_cap} used ({self.model_reserve} kept for the "
                f"final comparison); agent tool calls {t.tool_calls_used} of {t.tool_calls_used + t.tool_calls_left} "
                f"used; full-text reads {t.fulltext_used} of {self.fulltext_hard} (soft target {self.fulltext_soft}); "
                f"regenerations {self.regenerations_used} of {self.max_regenerations}.")


@dataclass(frozen=True)
class PacketContext:
    """Everything a packet needs besides the graph."""
    specs: Mapping[str, Sequence[ToolSpec]]          # route -> tool specs (allowlist applied)
    budget: PacketBudget
    inventory: Sequence[Mapping[str, Any]] = ()      # adapters.inventory_rows(graph), when QBiC-SELEX ran
    flags: Mapping[str, str] = field(default_factory=dict)   # hypothesis -> the critic's activation flag
    max_sketches: int = 8
    max_active: int = 3


def header(role: str, stage: str, round_no: int) -> str:
    """The packet's first line (scripted transports read the role from it)."""
    return f"Role: {role}; stage: {stage}; round {round_no}"


def render_case(graph: ClaimGraph) -> str:
    """The case as the request gave it (the variant with its rsID when the request supplied one, origin, supplied
    disease and context), the candidates the run inferred (labelled inferred), and what code's own tools found about
    the variant: the rsID at its exact coordinates and alleles, and the elements containing it. Never input_text or
    input_provenance: free text sent with a request is report metadata, not evidence, and a provenance note that
    depends on the cache would make a replay send different requests."""
    case, v = graph.case, graph.case.variant
    lines = ["<case>",
             f"Variant: {v.assembly} {v.chrom}:{v.pos} {v.ref}>{v.alt}; ref allele {v.ref}, alt allele {v.alt}; "
             f"{v.variant_type}; reference check {v.reference_check}"]
    if v.rsid:
        lines.append(f"rsID (supplied): {v.rsid}")
    lines += [f"Origin: {case.origin}" + (" (keep it unknown)" if case.origin == "unknown" else ""),
              "Supplied disease: " + ("; ".join(case.supplied_disease) or "none supplied"),
              "Supplied context: " + ("; ".join(scope_text(s) for s in case.supplied_context) or "none supplied")]
    rendered = [f"{c.kind} {c.label}" + (f" (basis {', '.join(c.basis_evidence_ids)})" if c.basis_evidence_ids else "")
                for c in case.inferred_candidates]
    lines.append("Inferred candidates (inferred, not supplied): " + ("; ".join(rendered) or "none"))
    found = [f"rsID {r} at these coordinates and alleles ({t})" for r, t in sorted(graph.variant_aliases.items())]
    found += [f"element {e} contains the variant ({t})" for e, t in sorted(graph.variant_elements.items())]
    lines.append("Found by code's own tools (facts, not supplied): " + ("; ".join(found) or "none"))
    from .variant_identity import identity_lines
    lines += identity_lines(graph)
    lines.append("</case>")
    return "\n".join(fence(x) for x in lines)


def entity_text(graph: ClaimGraph, entity_id: str) -> str:
    e = graph.entities[entity_id]
    if e.kind == "variant":
        own = e.canonical_id == graph.case.variant.key
        return f"variant {e.label}" + (" (the case variant)" if own else "")
    text = f"{e.kind} {e.label}"
    if e.canonical_id and e.canonical_id != e.label:
        text += f" [{e.canonical_id}]"
    if e.participants:
        text += " (members " + ", ".join(graph.entities[p].label for p in e.participants) + ")"
    return text


def claim_lines(graph: ClaimGraph, claim_id: str, links: bool = True) -> list[str]:
    """A claim with its version (an update's base_version), assessment, display status and effect allele."""
    c = graph.claims[claim_id]
    d = graph.display(claim_id)
    shown = d.status + (f", basis {d.basis}" if d.basis else "")
    subjects = "; ".join(entity_text(graph, e) for e in c.subject_ids)
    objects = "; ".join(entity_text(graph, e) for e in c.object_ids)
    text = f"{claim_id} v{c.version} [{c.assessment}; shown {shown}] {subjects} --{c.relation}--> {objects}"
    if c.direction != "unspecified":
        text += f"; direction {c.direction}"
        if c.effect_allele:
            text += f" for effect allele {allele_side(graph.case, c.effect_allele)}"
    text += f"; context {scope_text(c.context_scope)}"
    if c.dependencies:
        text += f"; depends on {', '.join(c.dependencies)}"
    if c.dependency_flag != "none":
        text += f"; {c.dependency_flag}"
    if c.superseded_by:
        text += f"; SUPERSEDED by {c.superseded_by}"
    if c.supersedes:
        text += f"; supersedes {c.supersedes}"
    lines = [fence(text), fence(f"  assertion: {c.assertion_text}")]
    if c.assessment_rationale:
        lines.append(fence(f"  assessment rationale: {c.assessment_rationale}"))
    if links:
        for x in c.evidence_links:
            note = ", applicability corrected by code" if x.corrected else ""
            note += f", stored as context_only (proposed {x.downgraded_from})" if x.downgraded_from else ""
            lines.append(fence(f"  link {x.evidence_id} {x.stance} ({x.strength}, {x.applicability}{note}) by "
                               f"{x.proposed_by}: {x.rationale}"))
    return lines


def hypothesis_lines(graph: ClaimGraph, hid: str, full: bool = True,
                     flags: Mapping[str, str] | None = None) -> list[str]:
    h = graph.hypotheses[hid]
    head = f"{hid} v{h.version} [{h.disposition}] {h.title} (mechanism {h.mechanism_class}; endpoint {h.endpoint})"
    if not full:
        return [fence(f"{head}; {h.disposition_reason or 'no reason recorded'}; signature {h.signature}")]
    optional = [c for c in h.claim_ids if c not in h.required_claim_ids]
    lines = [head, f"  required claims: {', '.join(h.required_claim_ids)}; optional: {', '.join(optional) or 'none'}",
             f"  reason for inclusion: {h.reason_for_inclusion or 'none given'}"]
    if flags and hid in flags:
        lines.append(f"  critic's activation flag: the reason for activating it is only a rank ({flags[hid]})")
    if h.summary:
        lines.append(f"  summary: {h.summary}")
    if h.context is not None:
        lines.append(f"  context: {scope_text(h.context)}")
    if h.member_alternatives:
        lines.append(f"  member alternatives: {', '.join(h.member_alternatives)}")
    if h.missing_links:
        lines.append(f"  missing links: {'; '.join(h.missing_links)}")
    if h.assumptions:
        lines.append(f"  assumptions: {'; '.join(h.assumptions)}")
    broken = {k: v for k, v in h.path_status.items() if v != "intact"}
    if broken:
        lines.append("  path: " + ", ".join(f"{k} {v}" for k, v in sorted(broken.items(), key=lambda kv: id_order(kv[0]))))
    if h.disposition == "deferred":
        lines.append(f"  deferred: {h.disposition_reason}; revisit when: {h.revisit_trigger}")
    if h.replaces:
        lines.append(f"  replaces {h.replaces}")
    return [fence(x) for x in lines]


STRENGTH_TEXT = {"direct": "direct", "indirect": "indirect (at most unresolved)",
                 "context": "context only (supports and contradicts are refused)"}


def strength_line(graph: ClaimGraph, evidence_id: str, claim_ids: Iterable[str]) -> str | None:
    """What a supports or contradicts link of this evidence could do for each live claim it is not yet linked to
    (graph.link_strength: the class matrix, narrowed for experiments on the variant's alleles). Identity (TF, gene,
    element, trait, variant) is checked only when a link is proposed, so this says what the class and the design allow,
    not that a link will be accepted."""
    parts = []
    for cid in sort_ids(claim_ids):
        c = graph.claims.get(cid)
        if c is None or c.superseded_by or any(x.evidence_id == evidence_id for x in c.evidence_links):
            continue
        parts.append(f"{cid} {STRENGTH_TEXT[graph.link_strength(cid, evidence_id)]}")
    if not parts:
        return None
    return ("  if linked as supports or contradicts (class and design only; identity is checked when linked): "
            + "; ".join(parts))


def evidence_lines(graph: ClaimGraph, evidence_id: str, claim_ids: Iterable[str] = ()) -> list[str]:
    """One evidence item, for inside a <data> fence; with `claim_ids`, also what a link to each of those claims could
    do (strength_line)."""
    e = graph.evidence[evidence_id]
    kind = ", measured null for " + str(e.assessed_relation) if e.result_kind == "null_in_assessed_scope" else ""
    lines = [f"{evidence_id} [{e.evidence_class}{kind}; origin {e.origin}; from {e.retrieval_ref or 'no tool call'}; "
             f"independence group {e.independence_group}; access {e.access}]",
             f"  observed: {e.observed_result}"]
    if e.allele or e.direction != "unspecified":
        lines.append(f"  allele {allele_side(graph.case, e.allele) or 'not stated'}: {e.direction}")
    about = [f"{name} {', '.join(values)}" for name, values in (("TFs", e.about_tfs), ("genes", e.about_genes),
                                                                  ("elements", e.about_elements),
                                                                  ("traits", e.about_traits),
                                                                  ("variants", e.about_variants)) if values]
    if about:
        lines.append("  about: " + "; ".join(about))
    lines.append(f"  context: {scope_text(e.context)}")
    if e.data:
        lines.append(f"  data: {compact(e.data, MAX_DATA)}")
    if e.source_ids:
        lines.append(f"  sources: {', '.join(e.source_ids)}")
    x = e.experiment
    if x is not None:
        s = x.system
        compared = f"; allele compared {x.compared_allele}" if x.compared_allele else ""
        lines += [f"  experiment: {x.source_id} {x.location} ({x.access}; {x.authors_hypothesis_vs_result})",
                  f"  passage: \"{x.passage}\"",
                  f"  system: {s.organism}; {s.tissue_or_cell}; treatment {s.treatment or 'none'}; genotype "
                  f"{s.genotype_or_allele or 'not stated'}",
                  f"  intervention {x.intervention}; manipulated {x.manipulated}{compared}; endpoint {x.endpoint}; "
                  f"comparator {x.comparator}; result {x.result}",
                  f"  scope supports: {x.scope_supports}; does not test: {x.scope_does_not_test}"]
    if e.limitations:
        lines.append(f"  limitations: {'; '.join(e.limitations)}")
    if claim_ids and (strength := strength_line(graph, evidence_id, claim_ids)):
        lines.append(strength)
    return [fence(x) for x in lines]


def records_text(records: Sequence[Any], limit: int) -> str:
    """Tool observations as compact, key-sorted JSON, whole records only: records are taken in their order while
    they fit within `limit` characters, and a note counts the rest. A record cut in half could lose exactly what
    identifies it (a paper's PMID, a peak's coordinates), so none is ever cut."""
    shown: list[str] = []
    size = 2                                   # the brackets
    for record in records:
        text = json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"), default=str)
        if size + len(text) + (1 if shown else 0) > limit:
            break
        size += len(text) + (1 if shown else 0)
        shown.append(text)
    out = "[" + ",".join(shown) + "]"
    if len(shown) < len(records):
        out += (f" [{len(shown)} of {len(records)} records shown: the rest would pass the {limit}-character bound "
                "for one call]")
    return out


def tool_call_lines(graph: ClaimGraph, call_id: str) -> list[str]:
    """One tool call and what it returned (retrieval only), for inside a <data> fence."""
    t = graph.tool_calls[call_id]
    params = compact(t.query_parameters, 400)
    evidence = f"evidence {', '.join(t.evidence_ids)}" if t.evidence_ids else "no evidence"
    lines = [f"{call_id} {t.tool_name} {params}: {t.execution_status} / {t.retrieval_status}; {evidence}"]
    if t.message:
        lines.append(f"  message: {t.message}")
    c = t.coverage
    if c.requested_scope or c.assessed_scope or c.limitations:
        lines.append(f"  coverage: requested {c.requested_scope or 'not stated'}; assessed "
                     f"{c.assessed_scope or 'not stated'}" + (f"; limits: {'; '.join(c.limitations)}"
                                                               if c.limitations else ""))
    if t.observations:
        limit = MAX_READ if t.read_article or t.tool_name == "evidence_inspect" else MAX_OBSERVATIONS
        lines.append(f"  observations: {records_text(t.observations, limit)}")
    return [fence(x) for x in lines]


def question_lines(graph: ClaimGraph, qid: str) -> list[str]:
    q = graph.questions[qid]
    r = q.rubric
    lines = [f"{qid} [{q.status}; {q.route}; round {q.round}] {q.text}",
             f"  targets: {', '.join(q.target_claim_ids) or 'none'}; hypotheses: {', '.join(q.hypothesis_ids) or 'none'}",
             f"  rubric: consequence {r.consequence}, discrimination {r.discrimination}, applicability "
             f"{r.applicability}, cost {r.cost}"]
    if q.possible_outcomes:
        lines.append(f"  possible outcomes: {'; '.join(q.possible_outcomes)}")
    for a in q.actions:
        lines.append(f"  action: {a.tool} {compact(a.params, 400)}" + (f" ({a.purpose})" if a.purpose else ""))
    if q.answer_summary:
        lines.append(f"  answer: {q.answer_summary}")
    if q.remaining_gap:
        lines.append(f"  remaining gap: {q.remaining_gap}")
    return [fence(x) for x in lines]


def tools_text(specs: Mapping[str, Sequence[ToolSpec]], routes: Sequence[str]) -> str:
    lines = []
    for route in routes:
        lines.append(f"Tools, {route} route (params_json is a JSON object of these parameters):")
        for s in specs.get(route, ()):
            params = ", ".join(f"{n} ({p.type}{', required' if p.required else ''}"
                               + (f", one of {'/'.join(p.choices)}" if p.choices else "")
                               + (f": {p.description}" if p.description else "") + ")"
                               for n, p in sorted(s.params.items())) or "none"
            exactly = "".join(f" Give exactly one of: {', '.join(group)}." for group in s.one_of)
            lines.append(f"- {s.name}: {s.description} Parameters: {params}.{exactly} Results: "
                         f"{s.result_semantics or '-'}"
                         + (f" Coverage: {s.coverage_notes}" if s.coverage_notes else "")
                         + (f" Evidence classes: {', '.join(s.evidence_classes)}." if s.evidence_classes else ""))
        if not specs.get(route):
            lines.append("- none available")
    return "\n".join(lines)


def group_items(graph: ClaimGraph, rows: Sequence[Mapping[str, Any]]) -> dict[str, list[tuple[str, str | None]]]:
    """Group id -> the Evidence items of that inventory group, each with the allele it favours (E id order): one item,
    or one per allele when the group's gate-passing models disagree about the allele (data.discordant; adapters joins
    a row to the item for its binds_more allele). Read from the calls that produced the rows' items, in one pass; a
    group below the gate has none."""
    calls = sort_ids({ev.retrieval_ref for r in rows if (ev := graph.evidence.get(str(r.get("evidence_id") or "")))
                      is not None and ev.retrieval_ref in graph.tool_calls})
    found: dict[str, dict[str, str | None]] = {}
    for tid in calls:
        for e in graph.tool_calls[tid].evidence_ids:
            if e in graph.evidence:
                found.setdefault(str(graph.evidence[e].data.get("group_id")), {})[e] = graph.evidence[e].allele
    return {g: [(e, items[e]) for e in sort_ids(items)] for g, items in found.items()}


def inventory_items(graph: ClaimGraph, row: Mapping[str, Any]) -> list[tuple[str, str | None]]:
    """The Evidence items of one inventory row's group (group_items); [] for a group below the gate."""
    return group_items(graph, [row]).get(str(row.get("group_id")), [])


def inventory_named(graph: ClaimGraph, rows: Sequence[Mapping[str, Any]]) -> set[str]:
    """Inventory groups that live claims name: as a tf_group, through a member TF, or by linking any of the group's
    evidence items (a discordant group has one per allele)."""
    groups, tfs, linked = set(), set(), set()
    for c in graph.claims.values():
        if c.superseded_by:
            continue
        linked |= {x.evidence_id for x in c.evidence_links}
        for eid in c.subject_ids + c.object_ids:
            e = graph.entities[eid]
            if e.kind == "tf_group" and e.canonical_id:
                groups.add(e.canonical_id.upper())
            tfs |= {graph.entities[p].label for p in e.participants} if e.kind in ("tf_group", "complex") else set()
            if e.kind == "tf":
                tfs.add(e.label)
    named = set()
    by_group = group_items(graph, rows)
    for r in rows:
        members = {str(m.get("tf", "")).upper() for m in r.get("members") or []}
        items = {e for e, _ in by_group.get(str(r["group_id"]), [])} | {r.get("evidence_id")} - {None}
        if str(r["group_id"]).upper() in groups or members & tfs or items & linked:
            named.add(str(r["group_id"]))
    return named


def inventory_line(case: Case, r: Mapping[str, Any], items: Sequence[tuple[str, str | None]] = ()) -> str:
    """One inventory row. `items` (inventory_items) adds, for a group whose gate-passing models disagree about the
    allele, each of its Evidence items with the allele it favours, so either can be linked to the claim about the
    members whose models it reports."""
    members = ", ".join(f"{m['tf']} ({'own' if m.get('mapping') == 'own' else 'CIS-BP-mapped'})"
                        for m in r.get("members") or [])
    side = r.get("binds_more")
    allele = {"ref": f"ref ({case.variant.ref})", "alt": f"alt ({case.variant.alt})"}.get(side, str(side))
    z = r.get("z")
    z_text = f"{z:.2f}" if isinstance(z, int | float) else "not available"
    stem = r.get("paralog_stem") or "none"
    line = (f"{r.get('evidence_id') or '-'} {r['group_id']} {r.get('dbd') or 'DBD not stated'} | members {members} | "
            f"paralog stem {stem} | more predicted binding: {allele} | z {z_text} | "
            f"{r.get('n_pass')}/{r.get('n_models')} models pass")
    if len(items) > 1:
        favours = ", ".join(f"{e} favours {allele_side(case, a) or 'no stated allele'}" for e, a in items)
        line += f" | the gate-passing models disagree about the allele: {favours}"
    return line


def inventory_text(graph: ClaimGraph, rows: Sequence[Mapping[str, Any]], full: bool) -> str:
    """The QBiC-SELEX inventory (C4): every gate-passing group in a neutral order (DNA-binding domain, then group id;
    never by z, TPM or ChIP) on the propose and regenerate packets; later packets only the groups live claims name.
    When the run asked for the inventory but has no rows (a cache miss, an error, nothing cached), every packet says
    so, with the call's status: an inventory that is missing must never read as one in which nothing was predicted."""
    if not rows:
        calls = sort_ids(t for t, x in graph.tool_calls.items() if x.tool_name == "qbic_inventory")
        if not calls:
            return ""
        t = graph.tool_calls[calls[-1]]
        note = (f"QBiC-SELEX inventory unavailable for this variant ({t.tool_call_id} {t.execution_status}/"
                f"{t.retrieval_status}" + (f": {t.message}" if t.message else "") + "). This is missing data, not "
                "evidence: it rules no TF or group in or out.")
        return "<data>\n" + fence(note) + "\n</data>"
    passing = sorted((r for r in rows if r.get("passes_gate")), key=lambda r: (str(r.get("dbd") or ""),
                                                                                 str(r["group_id"])))
    below = sum(1 for r in rows if not r.get("passes_gate"))
    named = set() if full else inventory_named(graph, rows)
    shown = passing if full else [r for r in passing if str(r["group_id"]) in named]
    lines = [f"QBiC-SELEX inventory: model-sharing groups with a model past the Bonferroni gate: {len(passing)}, listed "
             f"by DNA-binding domain then group id (not by z); groups with no model past the gate: {below}. The gate "
             "limits what is listed, not what is eligible: any TF stays queryable with qbic_tf_detail. A CIS-BP-mapped "
             "model counts as the TF's own."]
    if not full:
        lines.append(f"Shown: the {len(shown)} of {len(passing)} gate-passing groups that live claims name.")
    by_group = group_items(graph, shown)
    lines += [fence(inventory_line(graph.case, r, by_group.get(str(r["group_id"]), []))) for r in shown]
    return "<data>\n" + "\n".join(lines) + "\n</data>"


def _section(title: str, lines: Sequence[str]) -> str:
    """A section rendered from the graph. Its text came from tools, papers or earlier roles (which may quote either),
    so it sits inside a data fence: material to evaluate, never an instruction."""
    if not lines:
        return f"{title}: none"
    return f"{title}:\n<data>\n" + "\n".join(lines) + "\n</data>"


def _claims(graph: ClaimGraph, claim_ids: Iterable[str]) -> list[str]:
    return [line for cid in sort_ids(claim_ids) for line in claim_lines(graph, cid)]


def _evidence(graph: ClaimGraph, evidence_ids: Iterable[str]) -> list[str]:
    return packet_lines(graph, evidence_ids, evidence_lines)


def _linked(graph: ClaimGraph, claim_ids: Iterable[str]) -> set[str]:
    return {x.evidence_id for cid in claim_ids for x in graph.claims[cid].evidence_links}


def _inventory_evidence(graph: ClaimGraph) -> set[str]:
    return {e for t in graph.tool_calls.values() if t.tool_name == "qbic_inventory" for e in t.evidence_ids}


def _open(graph: ClaimGraph) -> list[str]:
    return [h for h, x in graph.hypotheses.items() if x.disposition not in ("rejected", "superseded")]


def _hypotheses(graph: ClaimGraph, ctx: PacketContext) -> list[str]:
    lines = []
    for hid in sort_ids(graph.hypotheses):
        full = graph.hypotheses[hid].disposition not in ("rejected", "superseded")
        lines += hypothesis_lines(graph, hid, full=full, flags=ctx.flags)
    if graph.hypotheses:
        lines.append(fence("Scope relationships and families (organisational only; no inherited support): "
                           + json.dumps(graph.scope_views(), ensure_ascii=False)))
    return lines


def _questions(graph: ClaimGraph) -> list[str]:
    return [x for q in sort_ids(graph.questions) for x in question_lines(graph, q)]


def _with_inventory(parts: list[str], graph: ClaimGraph, ctx: PacketContext, full: bool) -> None:
    if text := inventory_text(graph, ctx.inventory, full=full):
        parts.append(text)


def propose_packet(graph: ClaimGraph, ctx: PacketContext, *, regenerate: bool, round_no: int) -> str:
    """Initial proposal or regeneration: the case, every fact collected, the full inventory, and on regeneration the
    hypotheses so far with the signatures that cannot be proposed again."""
    stage = "regenerate" if regenerate else "propose"
    inventory = _inventory_evidence(graph)
    facts = [x for t in sort_ids(graph.tool_calls) if graph.tool_calls[t].tool_name != "qbic_inventory"
             for x in tool_call_lines(graph, t)]
    parts = [header("coordinator", stage, round_no), render_case(graph), _section("Tool calls so far", facts),
             _section("Evidence (other than the inventory rows)", _evidence(graph, set(graph.evidence) - inventory))]
    _with_inventory(parts, graph, ctx, full=True)
    if regenerate:
        live = [c for c, x in graph.claims.items() if not x.superseded_by]
        rejected = [fence(f"{h.hypothesis_id}: {h.signature} ({h.disposition_reason})")
                    for h in graph.hypotheses.values() if h.disposition == "rejected"]
        parts += ["REGENERATION: no reportable active hypothesis remains. Propose structurally different hypotheses; "
                  "the rejected structures listed below are refused whatever the wording.",
                  _section("Rejected structures", rejected), _section("Hypotheses so far", _hypotheses(graph, ctx)),
                  _section("Live claims (reuse those that still hold)", _claims(graph, live))]
    parts += [_section("Questions so far", _questions(graph)), tools_text(ctx.specs, ("computational", "literature")),
              f"Limits: at most {ctx.max_sketches} sketches are kept; at most {ctx.max_active} active (one more only "
              "with fourth_active_reason); the rest are deferred.",
              ctx.budget.text(), prompt("coordinator_propose")]
    return "\n\n".join(parts)


def plan_packet(graph: ClaimGraph, ctx: PacketContext, *, round_no: int, since_event: int) -> str:
    """After a round: the hypotheses, the claims of open hypotheses and of open questions, their evidence, the new
    evidence and refusals since the last plan, the questions and the inventory rows live claims name."""
    open_h = _open(graph)
    claims = {c for h in open_h for c in graph.hypotheses[h].claim_ids}
    claims |= {c for q in graph.questions.values() if q.status == "open" for c in q.target_claim_ids}
    claims |= {graph.claims[c].superseded_by for c in list(claims) if graph.claims[c].superseded_by}
    recent = graph.events[since_event:]
    awaiting = {eid for ids in adoption.pending(graph) for eid in ids}
    # Investigator-created claims need not belong to a hypothesis yet. Show them so the coordinator can adopt them.
    claims |= {cid for cid, c in graph.claims.items() if not c.superseded_by and
               any(link.evidence_id in awaiting for link in c.evidence_links)}
    new_evidence = {e for ev in recent if ev.action == "tool_call" for e in ev.evidence_ids}
    new_evidence |= {e for ev in recent if ev.action == "add_evidence" for e in ev.evidence_ids}
    refusals = [fence(f"{ev.event_id} by {ev.role}: {ev.concise_reason}") for ev in recent
                if ev.action == "refuse_update"]
    shown = _linked(graph, claims) | awaiting | (new_evidence - _inventory_evidence(graph))
    parts = [header("coordinator", "plan", round_no), render_case(graph),
             _section("Hypotheses", _hypotheses(graph, ctx)), _section("Claims", _claims(graph, claims)),
             _section("Mechanistic resolution gaps (questions, not new evidence)", gap_lines(graph, claims)),
             _section("Persistent literature discovery leads", discovery_lines(graph)),
             _section("Evidence linked to these claims, and new evidence since the last plan",
                      _evidence(graph, shown)),
             _section("Observation adoption (persists across rounds)", adoption.context_lines(graph)),
             _section("Refused updates since the last plan", refusals), _section("Questions", _questions(graph))]
    _with_inventory(parts, graph, ctx, full=False)
    parts += [tools_text(ctx.specs, ("computational", "literature")),
              f"Limits: at most {ctx.max_active} active hypotheses.", ctx.budget.text(), prompt("coordinator_plan")]
    return "\n\n".join(parts)


def investigate_packet(graph: ClaimGraph, ctx: PacketContext, *, route: str, step: str, questions: Sequence[str],
                       question_calls: Mapping[str, Sequence[str]], round_no: int) -> str:
    """One route's questions with the results of their actions, the claims they target and the claims of the
    hypotheses they concern (with versions), and the evidence already linked to those claims."""
    role = ROUTE_ROLE[route]
    open_h = set(_open(graph))
    hyps = {h for q in questions for h in graph.questions[q].hypothesis_ids if h in open_h}
    targets = {c for q in questions for c in graph.questions[q].target_claim_ids}
    claims = set(targets) | {c for h in hyps for c in graph.hypotheses[h].claim_ids}
    claims |= {graph.claims[c].superseded_by for c in list(claims) if graph.claims[c].superseded_by}
    calls = [t for q in questions for t in question_calls.get(q, ())]
    from_calls = {e for t in calls for e in graph.tool_calls[t].evidence_ids}
    def render_result(g, eid, _):
        return evidence_lines(g, eid, targets if eid in from_calls else ())
    evidence = packet_lines(graph, from_calls | _linked(graph, claims), render_result)
    blocks: list[str] = []
    for q in questions:
        results = [x for t in question_calls.get(q, ()) for x in tool_call_lines(graph, t)]
        blocks += [*([""] if blocks else []), *question_lines(graph, q), "  results:",
                   *(results or ["  no tool call ran"])]
    parts = [header(role, step, round_no), render_case(graph),
             _section("Questions for this step (answer each by its id)", blocks),
             _section("Hypotheses these questions concern", [x for h in sort_ids(hyps)
                                                              for x in hypothesis_lines(graph, h, flags=ctx.flags)]),
             _section("Claims (use the version shown as base_version)", _claims(graph, claims)),
             _section("Mechanistic resolution gaps (questions, not new evidence)", gap_lines(graph, claims)),
             _section("Evidence from these results and evidence already linked to these claims", evidence)]
    _with_inventory(parts, graph, ctx, full=False)
    if route == "literature":
        parts.append(_section("Persistent literature discovery leads", discovery_lines(graph)))
    parts += [tools_text(ctx.specs, (route,)), ctx.budget.text(),
              f"Task: step {step}. Answer each question above by its id, following your route's instructions for "
              "this step. Return JSON matching the schema."]
    return "\n\n".join(parts)


def audit_packet(graph: ClaimGraph, ctx: PacketContext, *, round_no: int, audited: Sequence[str]) -> str:
    """The hypotheses under audit (the active ones; when none is active, the deferred ones) with every claim, link and
    linked evidence (literature passages included)."""
    claims = {c for h in audited for c in graph.hypotheses[h].claim_ids}
    deferred = [h for h in audited if graph.hypotheses[h].disposition == "deferred"]
    parts = [header("critic", "audit", round_no), render_case(graph)]
    if deferred:
        parts.append(f"No hypothesis is active. Audit the deferred hypotheses {', '.join(sort_ids(deferred))}: a "
                     "deferral is a priority decision, never a refutation, and one made for missing data is improper. "
                     "List in reportable_ids each deferred hypothesis that could still be reported; code reactivates "
                     "those for the final comparison.")
    parts += [_section("Hypotheses", _hypotheses(graph, ctx)),
              _section("Claims of the hypotheses under audit", _claims(graph, claims)),
              _section("Mechanistic resolution gaps (questions, not new evidence)", gap_lines(graph, claims)),
              _section("Linked evidence", _evidence(graph, _linked(graph, claims))),
              _section("Observations not represented in the hypotheses", adoption.context_lines(graph)),
              _section("Evidence awaiting adoption",
                       _evidence(graph, {e for ids in adoption.pending(graph) for e in ids})),
              _section("Questions", _questions(graph))]
    _with_inventory(parts, graph, ctx, full=False)
    parts += [tools_text(ctx.specs, ("computational", "literature")), ctx.budget.text(), prompt("critic_audit")]
    return "\n\n".join(parts)


def final_packet(graph: ClaimGraph, ctx: PacketContext, *, profiles: Mapping[str, Any],
                 critique: V9Critique | None, stale: Sequence[str], round_no: int,
                 reinstated: Sequence[str] = ()) -> str:
    """The comparison profiles of the active hypotheses (code-computed), their claims and evidence, the audit, the
    rejections code reinstated because their contradiction was withdrawn, and any rejection whose contradiction no
    longer stands that stays rejected."""
    active = [h for h, x in graph.hypotheses.items() if x.disposition == "active"]
    claims = {c for h in active for c in graph.hypotheses[h].claim_ids}
    audit: list[str] = []
    if critique is not None:
        audit = ([fence(f"challenge {c.claim_id} ({c.kind}): {c.gap}") for c in critique.challenges]
                 + [fence(f"passage {p.evidence_id}: {p.verdict} {p.note}") for p in critique.passage_checks]
                 + [fence(f"activation flag {f.hypothesis_id}: {f.reason}") for f in critique.activation_flags]
                 + [f"reportable: {', '.join(critique.reportable_ids) or 'none'}"])
    back = [f"{h}: code rejected it for a contradicted required claim; that contradiction was withdrawn, so code "
            f"reinstated it once (now {graph.hypotheses[h].disposition}). A reinstatement is not support: its claims "
            "stand as assessed, and it is compared only while active" for h in reinstated if h in graph.hypotheses]
    standing = [f"{h}: rejected, but none of its required claims ({', '.join(graph.hypotheses[h].required_claim_ids)}) "
                "is contradicted in scope now; code could not reinstate it (a second rejection is final, and code "
                "reinstates only its own rejections), so it stays rejected and is not compared"
                for h in stale if graph.hypotheses.get(h) is not None and graph.hypotheses[h].disposition == "rejected"]
    parts = [header("critic", "final", round_no), render_case(graph),
             _section("Molecular support and chain completeness (independent of ranking)",
                      [fence(compact(support_summary(graph), 12000))]),
             _section("Hypotheses", _hypotheses(graph, ctx)),
             _section("Comparison profiles (code-computed)", [fence(compact(dict(sorted(profiles.items())), 60000))]),
             _section("Claims of the active hypotheses", _claims(graph, claims)),
             _section("Linked evidence", _evidence(graph, _linked(graph, claims))), _section("Audit", audit),
             _section("Observation adoption and deferrals", adoption.context_lines(graph)),
             _section("Evidence awaiting adoption",
                      _evidence(graph, {e for ids in adoption.pending(graph) for e in ids})),
             _section("Rejections reinstated by code", back),
             _section("Rejections that no longer stand", standing), _section("Questions", _questions(graph))]
    _with_inventory(parts, graph, ctx, full=False)
    parts += [ctx.budget.text(), prompt("critic_final")]
    return "\n\n".join(parts)


# --- checks (SchemaCheckError -> the model's one repair) ---------------------------------------------------------------

Specs = Mapping[str, Sequence[ToolSpec]]


def _raise(problems: list[str]) -> None:
    if problems:
        raise SchemaCheckError("; ".join(dict.fromkeys(problems)))


def parse_params(params_json: str) -> dict[str, Any]:
    """params_json as a dict, or ValueError saying why it is not a usable parameter object."""
    value = json.loads(params_json or "{}")
    if not isinstance(value, dict):
        raise ValueError("params_json must be a JSON object")
    for k, v in value.items():
        ok = isinstance(v, str | int | float | bool) or (isinstance(v, list) and all(isinstance(x, str) for x in v))
        if not ok:
            raise ValueError(f"parameter {k} must be a string, number, true/false or a list of strings")
    return value


def action_problems(action: V9Action, specs: Specs, route: str | None, where: str) -> list[str]:
    """Unknown tool, a tool of the other route, or parameters the tool's spec refuses."""
    allowed = {s.name: s for r, items in specs.items() if route is None or r == route for s in items}
    spec = allowed.get(action.tool)
    if spec is None:
        other = next((r for r, items in specs.items() for s in items if s.name == action.tool), None)
        if other:
            return [f"{where}: {action.tool} is a {other} tool; a {route} question cannot use it"]
        return [f"{where}: unknown tool {action.tool!r} (available: {', '.join(sorted(allowed)) or 'none'})"]
    try:
        canonical_params(spec, parse_params(action.params_json))
    except (ValueError, ToolRefusal) as e:
        return [f"{where}: {getattr(e, 'message', None) or e}"]
    return []


def _live(graph: ClaimGraph, claim_id: str) -> str | None:
    """Why an id is not a live claim, or None."""
    c = graph.claims.get(claim_id)
    if c is None:
        return f"unknown claim {claim_id}"
    if c.superseded_by:
        return f"{claim_id} is superseded by {c.superseded_by}"
    return None


def _version(graph: ClaimGraph, claim_id: str, base: int | None, where: str) -> list[str]:
    c = graph.claims.get(claim_id)
    if c is None or base is None or base == c.version:
        return []
    return [f"{where}: base_version {base} is not {claim_id}'s version shown in the packet (v{c.version})"]


REF_WORDS = frozenset({"REF", "REFERENCE"})
ALT_WORDS = frozenset({"ALT", "ALTERNATE", "ALTERNATIVE"})


def is_case_allele(case: Case, allele: str) -> bool:
    """Whether an effect allele names the case variant's ref or alt, read as the graph reads it: its first word ("T",
    "ref", "G (alt)")."""
    token = re.split(r"[\s(),;:]+", allele.strip().upper())[0]
    return token in REF_WORDS | ALT_WORDS | {case.variant.ref, case.variant.alt}


def claim_problems(graph: ClaimGraph, claim: V9Claim, keys: set[str], where: str) -> list[str]:
    """A claim spec's entities, effect allele, premises and initial links: mistakes the graph would refuse, caught
    here so the model can repair them instead of losing the hypothesis that needs the claim."""
    problems = []
    entities = claim.subjects + claim.objects
    if not claim.subjects or not claim.objects:
        problems.append(f"{where}: a claim needs at least one subject and one object")
    for e in entities:
        if e.members and e.kind not in ("complex", "binding_event", "tf_group"):
            problems.append(f"{where}: only a tf_group, complex or binding_event lists members ({e.kind} {e.label})")
        if e.kind == "tf_group" and not (e.canonical_id or e.members):
            problems.append(f"{where}: tf_group {e.label} needs its QBiC-SELEX group id as canonical_id")
    if claim.relation in ("occupies", "alters_binding") and not any(e.kind in ("tf", "tf_group", "complex")
                                                                     for e in entities):
        problems.append(f"{where}: a {claim.relation} claim names the bound factor as a tf, tf_group or complex; "
                        "for variant-to-factor binding use a variant subject and a tf object, not a gene or "
                        "binding_event object. Separate factor-specific measurements into separate claims; "
                        "do not infer a tested complex from co-occurrence.")
    allele = (claim.effect_allele or "").strip()
    variants = [e for e in entities if e.kind == "variant"]
    v = graph.case.variant
    if allele and not variants:
        problems.append(f"{where}: effect_allele belongs to a claim that names a variant; use null")
    elif allele and any(graph.ref_is_case_variant(entity_ref(e)) for e in variants) and \
            not is_case_allele(graph.case, allele):
        # the graph's own rule: a label naming no other variant, or a canonical id naming the case (an alias rsID,
        # its chrom:pos), is the case variant, whose effect allele must be its ref or alt
        problems.append(f"{where}: effect_allele must be ref ({v.ref}) or alt ({v.alt}) of the case variant")
    for dep in claim.depends_on:
        if dep not in keys and (problem := _live(graph, dep)):
            problems.append(f"{where}: depends_on {dep}: {problem}")
    for link in claim.initial_links:
        if link.evidence_id not in graph.evidence:
            problems.append(f"{where}: unknown evidence {link.evidence_id}")
    return problems


def question_problems(graph: ClaimGraph, q: V9Question, specs: Specs, claim_keys: set[str], hyp_keys: set[str],
                      where: str) -> list[str]:
    problems = [f"{where}: unknown claim {c}" for c in q.target_claims if c not in claim_keys and c not in graph.claims]
    problems += [f"{where}: unknown hypothesis {h}" for h in q.hypotheses
                 if h not in hyp_keys and h not in graph.hypotheses]
    if not q.actions:
        problems.append(f"{where}: a question needs at least one tool action")
    for i, a in enumerate(q.actions):
        problems += action_problems(a, specs, q.route, f"{where} action {i}")
    return problems


def _cycles(claims: Sequence[V9Claim]) -> list[str]:
    deps = {c.key: [d for d in c.depends_on if d in {x.key for x in claims}] for c in claims}
    state: dict[str, int] = {}

    def visit(k: str) -> bool:
        if state.get(k) == 1:
            return True
        if state.get(k) == 2:
            return False
        state[k] = 1
        found = any(visit(d) for d in deps[k])
        state[k] = 2
        return found

    return [f"claim keys depend on each other in a cycle through {k}" for k in deps if k not in state and visit(k)]


def propose_check(graph: ClaimGraph, specs: Specs, *, regenerate: bool) -> Callable[[V9Propose], V9Propose]:
    def check(out: V9Propose) -> V9Propose:
        problems: list[str] = []
        sketch_keys = [h.key for h in out.hypotheses]
        claims = [c for h in out.hypotheses for c in h.claims]
        claim_keys = [c.key for c in claims]
        for name, keys in (("sketch", sketch_keys), ("claim", claim_keys)):
            problems += [f"{name} key {k!r} is used twice" for k in sorted({k for k in keys if keys.count(k) > 1})]
            problems += [f"every {name} needs a non-empty key" for k in keys if not k.strip()][:1]
        known = set(claim_keys)
        for h in out.hypotheses:
            where = f"sketch {h.key}"
            for c in h.claims:
                problems += claim_problems(graph, c, known, f"{where} claim {c.key}")
                if c.required and c.relation not in REQUIRABLE:
                    problems.append(f"{where} claim {c.key}: {c.relation} claims can only be optional (expression "
                                    "and occupancy never decide a hypothesis)")
            for use in h.reuse_claims:
                if use.ref not in known and (problem := _live(graph, use.ref)):
                    problems.append(f"{where}: reuse_claims {use.ref}: {problem}")
            if not any(c.required for c in h.claims) and not any(u.required for u in h.reuse_claims):
                problems.append(f"{where}: a hypothesis needs at least one required claim")
            if not h.activate and not ((h.deferral_reason or "").strip() and (h.revisit_trigger or "").strip()):
                problems.append(f"{where}: a sketch that is not activated needs a deferral_reason and a "
                                "revisit_trigger")
            if not h.reason_detail.strip() or rank_only(h.reason_detail):
                problems.append(f"{where}: reason_detail must give a specific reason for inclusion; a rank (largest "
                                "z, highest TPM, a ChIP peak) is not one")
            if h.replaces is not None and (not regenerate or h.replaces not in graph.hypotheses):
                problems.append(f"{where}: replaces names {h.replaces}, " + (
                    "but only a regenerated sketch replaces a hypothesis" if not regenerate else "an unknown hypothesis"))
        problems += _cycles(claims)
        for i, q in enumerate(out.questions):
            problems += question_problems(graph, q, specs, known, set(sketch_keys), f"question {i}")
        for c in out.inferred_candidates:
            problems += [f"inferred candidate {c.label}: unknown evidence {e}" for e in c.basis_evidence_ids
                         if e not in graph.evidence]
        for r in out.reactivate:
            h = graph.hypotheses.get(r.hypothesis_id)
            if not regenerate or h is None or h.disposition != "deferred":
                problems.append(f"reactivate {r.hypothesis_id}: only a deferred hypothesis can be reactivated, on "
                                "regeneration")
        _raise(problems)
        return out
    return check


def plan_check(graph: ClaimGraph, specs: Specs, *, max_new: int = 2,
               allow_legacy: bool = False) -> Callable[[V9Plan], V9Plan]:
    def check(out: V9Plan) -> V9Plan:
        problems: list[str] = []
        if out._legacy_adoption and not allow_legacy:
            problems.append("plan must include new_hypotheses, inferred_candidates and evidence_decisions; "
                            "pre-adoption scripts are accepted only in fixture or cache-only mode")
        sketches = [x.sketch for x in out.new_hypotheses]
        new_claims = [c for h in sketches for c in h.claims]
        new_claims += [u.new_claim for u in out.hypothesis_updates if u.new_claim is not None]
        claim_keys = {c.key for c in new_claims}
        if len(claim_keys) != len(new_claims):
            problems.append("new claim keys must be unique across discoveries and hypothesis updates")
        if claim_keys & set(graph.claims) or {h.key for h in sketches} & set(graph.hypotheses):
            problems.append("new claim/sketch keys must not shadow existing graph ids")
        if len(sketches) > max_new:
            problems.append(f"at most {max_new} new hypotheses may be proposed in this plan")
        proposal = V9Propose(directions=[], inferred_candidates=out.inferred_candidates, hypotheses=sketches,
                             fourth_active_reason=None, reactivate=[], questions=[])
        try:
            propose_check(graph, specs, regenerate=False)(proposal)
        except SchemaCheckError as error:
            problems.append(str(error))
        for discovery in out.new_hypotheses:
            if not discovery.basis_evidence_ids:
                problems.append(f"discovery {discovery.sketch.key} needs basis_evidence_ids")
            problems += [f"discovery {discovery.sketch.key}: unknown evidence {eid}"
                         for eid in discovery.basis_evidence_ids if eid not in graph.evidence]
            # Naming a real evidence id is not enough: the branch must use some of its basis in a scoped claim.
            # The graph still gates those links on application; this check grants no support to a hypothesis.
            new_by_key = {c.key: c for c in new_claims}
            members = list(discovery.sketch.claims)
            members += [new_by_key[r.ref] for r in discovery.sketch.reuse_claims if r.ref in new_by_key]
            linked = {link.evidence_id for c in members for link in c.initial_links
                      if link.stance != "context_only"}
            linked |= {link.evidence_id for r in discovery.sketch.reuse_claims if r.ref in graph.claims
                       for link in graph.claims[r.ref].evidence_links
                       if link.stance != "context_only" and link.strength != "context"}
            if not linked.intersection(discovery.basis_evidence_ids):
                problems.append(f"discovery {discovery.sketch.key}: at least one basis evidence must be linked "
                                "to a new or reused claim with a non-context stance")
        for i, u in enumerate(out.hypothesis_updates):
            where = f"hypothesis update {i} ({u.action} {u.hypothesis_id})"
            h = graph.hypotheses.get(u.hypothesis_id)
            if h is None:
                problems.append(f"{where}: unknown hypothesis")
                continue
            if u.new_claim is not None:
                problems += claim_problems(graph, u.new_claim, set(), f"{where} new_claim")
            requiring = u.action == "replace_required_claim" or (u.action == "add_claim" and u.required)
            if requiring and u.new_claim is not None and u.new_claim.relation not in REQUIRABLE:
                problems.append(f"{where}: {u.new_claim.relation} claims can only be optional")
            if u.action == "revise" and u.revision is None:
                problems.append(f"{where}: revise needs revision")
            if u.action == "defer" and not (u.revisit_trigger or "").strip():
                problems.append(f"{where}: defer needs a revisit_trigger")
            if u.action in ("supersede_claim", "replace_required_claim"):
                pool = h.claim_ids if u.action == "supersede_claim" else h.required_claim_ids
                if u.claim_id not in pool:
                    problems.append(f"{where}: claim_id must be a{' required' if u.action != 'supersede_claim' else ''}"
                                    f" claim of {u.hypothesis_id}")
            if u.action == "supersede_claim" and u.new_claim is None:
                problems.append(f"{where}: supersede_claim needs new_claim")
            if u.action == "add_claim" and (u.claim_id is None) == (u.new_claim is None):
                problems.append(f"{where}: add_claim needs either claim_id or new_claim")
            if u.action == "add_claim" and u.claim_id is not None and (problem := _live(graph, u.claim_id)):
                problems.append(f"{where}: {problem}")
            if u.action == "replace_required_claim":
                if (u.new_claim_id is None) == (u.new_claim is None):
                    problems.append(f"{where}: replace_required_claim needs either new_claim_id or new_claim")
                elif u.new_claim_id is not None and (problem := _live(graph, u.new_claim_id)):
                    problems.append(f"{where}: {problem}")
            if u.revision is not None:
                problems += [f"{where}: {c} is not a claim of {u.hypothesis_id}" for c in u.revision.remove_claim_ids
                             if c not in h.claim_ids]
        for i, a in enumerate(out.assessments):
            where = f"assessment {i}"
            if (problem := _live(graph, a.claim_id)) is not None:
                problems.append(f"{where}: {problem}")
            else:
                problems += _version(graph, a.claim_id, a.base_version, where)
        reviewed = set()
        for decision in out.evidence_decisions:
            if not decision.evidence_ids or not decision.reason.strip():
                problems.append("an evidence decision needs evidence ids and a reason")
            for eid in decision.evidence_ids:
                if eid not in graph.evidence:
                    problems.append(f"evidence decision: unknown evidence {eid}")
                if eid in reviewed:
                    problems.append(f"evidence {eid} has more than one decision in this plan")
                reviewed.add(eid)
            if decision.disposition == "defer" and not (decision.revisit_trigger or "").strip():
                problems.append("deferring evidence needs a revisit_trigger")
            if decision.disposition == "represented" and not decision.claim_refs:
                problems.append("represented evidence needs claim_refs; changing a summary is not adoption")
            for ref in decision.claim_refs:
                if ref not in claim_keys and (problem := _live(graph, ref)):
                    problems.append(f"evidence decision claim {ref}: {problem}")
        # A new plan must account for observations left outside the current mechanisms, including explicit deferral.
        # Pre-adoption fixture scripts remain readable; live strict output always contains these new fields.
        if not out._legacy_adoption:
            linked = {link.evidence_id for c in new_claims for link in c.initial_links
                      if link.stance != "context_only"}
            for ids in adoption.required_reviews(graph):
                if not set(ids) & (reviewed | linked):
                    problems.append(f"observation {', '.join(ids)} needs an evidence decision or a new claim link")
        for i, q in enumerate(out.questions):
            problems += question_problems(graph, q, specs, claim_keys, {h.key for h in sketches}, f"question {i}")
        _raise(problems)
        return out
    return check


def investigate_check(graph: ClaimGraph, route: str, questions: Sequence[str],
                      specs: Specs) -> Callable[[V9Investigate], V9Investigate]:
    def check(out: V9Investigate) -> V9Investigate:
        problems: list[str] = []
        out._proposal_errors = {}
        seen: set[str] = set()
        keys: set[str] = set()
        for i, a in enumerate(out.answers):
            where = f"answer {i} ({a.question_id})"
            if a.question_id not in questions:
                problems.append(f"{where}: answer only the questions given ({', '.join(questions)})")
            if a.question_id in seen:
                problems.append(f"{where}: one answer per question")
            seen.add(a.question_id)
            declared = {"key:" + u.new_claim.key for u in a.proposed_updates
                        if u.kind in ("new_claim", "supersede_claim") and u.new_claim is not None}
            problems += [f"{where}: unknown claim {c}" for c in a.claim_ids
                         if c not in graph.claims and c not in declared]
            problems += [f"{where}: unknown tool call {t}" for t in a.tool_call_ids if t not in graph.tool_calls]
            if a.experiments and route != "literature":
                problems.append(f"{where}: only the literature investigator extracts experiments")
            for j, u in enumerate(a.proposed_updates):
                accepted_keys = set(keys)
                errors = _proposal_problems(graph, u, a, accepted_keys, f"{where} update {j}")
                if errors:
                    if route == "literature":
                        out._proposal_errors[i, j] = errors
                    else:
                        problems += errors
                else:
                    keys = accepted_keys
            for j, act in enumerate(a.follow_up_actions):
                problems += action_problems(act, specs, route, f"{where} follow-up {j}")
        _raise(problems)
        return out
    return check


def _proposal_problems(graph: ClaimGraph, u: V9Proposal, answer: V9Answer, keys: set[str], where: str) -> list[str]:
    problems = []
    if u.kind in ("attach_evidence", "assess", "supersede_claim"):
        if u.claim_id is None:
            return [f"{where}: {u.kind} needs claim_id"]
        if u.claim_id.startswith("key:"):
            if u.kind == "supersede_claim" or u.claim_id[4:] not in keys:
                problems.append(f"{where}: {u.claim_id} names no claim proposed earlier in this answer")
        elif (problem := _live(graph, u.claim_id)) is not None:
            problems.append(f"{where}: {problem}")
        elif u.base_version is not None:
            problems += _version(graph, u.claim_id, u.base_version, where)
    if u.kind == "attach_evidence":
        if u.stance is None:
            problems.append(f"{where}: attach_evidence needs a stance")
        if (u.evidence_id is None) == (u.experiment_index is None):
            problems.append(f"{where}: attach_evidence needs either evidence_id or experiment_index")
        elif u.evidence_id is not None and u.evidence_id not in graph.evidence:
            problems.append(f"{where}: unknown evidence {u.evidence_id}")
        elif u.experiment_index is not None and not 0 <= u.experiment_index < len(answer.experiments):
            problems.append(f"{where}: experiment_index {u.experiment_index} is not one of this answer's "
                            f"{len(answer.experiments)} experiments")
    local = bool(u.claim_id and u.claim_id.startswith("key:") and u.claim_id[4:] in keys)
    if u.kind in ("assess", "attach_evidence") and u.suggested_assessment is not None and \
            u.base_version is None and not local:
        problems.append(f"{where}: a suggested assessment needs the base_version shown")
    if u.kind == "assess" and u.suggested_assessment is None:
        problems.append(f"{where}: assess needs suggested_assessment")
    if u.kind in ("new_claim", "supersede_claim"):
        if u.new_claim is None:
            problems.append(f"{where}: {u.kind} needs new_claim")
        else:
            problems += claim_problems(graph, u.new_claim, set(), f"{where} new_claim")
            keys.add(u.new_claim.key)
    return problems


def critique_check(graph: ClaimGraph, specs: Specs) -> Callable[[V9Critique], V9Critique]:
    def check(out: V9Critique) -> V9Critique:
        problems: list[str] = []
        for i, c in enumerate(out.challenges):
            where = f"challenge {i}"
            if c.claim_id not in graph.claims:
                problems.append(f"{where}: unknown claim {c.claim_id}")
            else:
                problems += _version(graph, c.claim_id, c.base_version, where)
            problems += [f"{where}: unknown evidence {e}" for e in c.evidence_ids if e not in graph.evidence]
            if c.requested_action is not None:
                problems += action_problems(c.requested_action, specs, None, f"{where} requested_action")
        problems += [f"passage check: unknown evidence {p.evidence_id}" for p in out.passage_checks
                     if p.evidence_id not in graph.evidence]
        problems += [f"unknown hypothesis {h}" for h in [f.hypothesis_id for f in out.activation_flags]
                     + out.reportable_ids if h not in graph.hypotheses]
        _raise(problems)
        return out
    return check


def final_check(graph: ClaimGraph) -> Callable[[V9Final], V9Final]:
    def check(out: V9Final) -> V9Final:
        problems: list[str] = []
        hyps = [h for c in out.comparisons for h in (c.a, c.b)] + out.outcome.leading_ids
        hyps += [w.hypothesis_id for w in out.outcome.weakest_links]
        hyps += [h for x in out.outcome.next_experiments for h in x.distinguishes]
        claims = [c for x in out.comparisons for c in x.decisive_claim_ids]
        claims += [w.claim_id for w in out.outcome.weakest_links]
        claims += [c for x in out.outcome.next_experiments for c in x.claim_ids]
        problems += [f"unknown hypothesis {h}" for h in hyps if h not in graph.hypotheses]
        problems += [f"unknown claim {c}" for c in claims if c not in graph.claims]
        problems += [f"comparison {i} compares {c.a} with itself" for i, c in enumerate(out.comparisons) if c.a == c.b]
        _raise(problems)
        return out
    return check


# --- conversions into graph inputs -------------------------------------------------------------------------------------

def entity_ref(e: V9Entity) -> EntityRef:
    return EntityRef(kind=e.kind, label=e.label, canonical_id=e.canonical_id or None, members=list(e.members))


def context_scope(c: V9Context | None, case: Case) -> ContextScope | None:
    """A model's context as a ContextScope (the graph normalises it): "supplied" when it names a supplied context."""
    if c is None or not c.label.strip():
        return None
    supplied = {s.label.casefold() for s in case.supplied_context} | {
        (s.biosample or "").casefold() for s in case.supplied_context}
    source = "supplied" if c.label.strip().casefold() in supplied else "inferred"
    return ContextScope(label=c.label.strip(), species=c.species.strip() or "human",
                        condition=(c.condition or "").strip() or None, source=source)


def claim_draft(c: V9Claim, case: Case, mechanism_class: MechanismClass, dependencies: Sequence[str]) -> ClaimDraft:
    return ClaimDraft(subjects=[entity_ref(e) for e in c.subjects], relation=c.relation,
                      objects=[entity_ref(e) for e in c.objects], direction=c.direction,
                      effect_allele=(c.effect_allele or "").strip() or None, context=context_scope(c.context, case),
                      mechanism_class=mechanism_class, assertion_text=c.assertion_text,
                      dependencies=list(dependencies))


def tool_request(a: V9Action) -> ToolRequest:
    return ToolRequest(tool=a.tool, params=parse_params(a.params_json), purpose=a.purpose)


def question_input(q: V9Question, targets: Sequence[str], hypotheses: Sequence[str], round_no: int) -> Question:
    r = q.rubric
    return Question(text=q.text, target_claim_ids=list(dict.fromkeys(targets)),
                    hypothesis_ids=list(dict.fromkeys(hypotheses)), route=q.route,
                    rubric=Rubric(consequence=r.consequence, discrimination=r.discrimination,
                                  applicability=r.applicability, cost=r.cost),
                    possible_outcomes=list(q.possible_outcomes), actions=[tool_request(a) for a in q.actions],
                    round=round_no)


def experiment_record(x: V9Experiment) -> ExperimentRecord:
    """An extracted experiment as the literature module's record (contract C3 with CORE-CHANGES-2 C2-8 and
    CORE-CHANGES-3 C3-1): what was manipulated, the elements and variants it concerns (the literature module keeps
    only the variant names the paper supports), and, for an allele comparison only, the allele its direction
    describes."""
    return ExperimentRecord(source_id=x.source_id, pmcid=x.pmcid, doi=x.doi, publication_type=x.publication_type,
                            access=x.access, location=x.location, passage=x.passage,
                            system=ExperimentSystem(organism=x.organism, tissue_or_cell=x.tissue_or_cell,
                                                    treatment=x.treatment, genotype_or_allele=x.genotype_or_allele),
                            intervention=x.intervention, endpoint=x.endpoint, comparator=x.comparator,
                            result=x.result, direction=x.direction, scope_supports=x.scope_supports,
                            scope_does_not_test=x.scope_does_not_test, about_tfs=list(x.about_tfs),
                            about_genes=list(x.about_genes), about_elements=list(x.about_elements),
                            about_traits=list(x.about_traits),
                            about_variants=[" ".join(v.split()) for v in x.about_variants if v.strip()],
                            manipulated=x.manipulated, compared_allele=(x.compared_allele or "").strip() or None,
                            authors_hypothesis_vs_result=x.authors_hypothesis_vs_result)


def reason_text(kind: str, detail: str) -> str:
    return f"{kind}: {' '.join(detail.split())}"


def revision_changes(r: V9Revision) -> HypothesisChanges:
    return HypothesisChanges(title=r.title, summary=r.summary, endpoint=r.endpoint, assumptions=r.assumptions,
                             member_alternatives=r.member_alternatives, missing_links=r.missing_links,
                             remove_claim_ids=list(r.remove_claim_ids))


def proposal_update(u: V9Proposal, case: Case, evidence_id: str | None, mechanism_class: MechanismClass) -> GraphUpdate:
    """An investigator's proposal as a GraphUpdate (experiment_index already resolved to evidence_id). Investigators
    never set hypothesis fields; the graph refuses them anyway."""
    if u.kind == "attach_evidence":
        return GraphUpdate(kind="attach_evidence", claim_id=u.claim_id, evidence_id=evidence_id, stance=u.stance,
                           applicability=u.applicability, rationale=u.rationale, limitations=list(u.limitations),
                           suggested_assessment=u.suggested_assessment, base_version=u.base_version)
    if u.kind == "assess":
        return GraphUpdate(kind="assess", claim_id=u.claim_id, assessment=u.suggested_assessment,
                           base_version=u.base_version, rationale=u.rationale)
    claim = u.new_claim
    draft = claim_draft(claim, case, mechanism_class, claim.depends_on)
    if u.kind == "new_claim":
        return GraphUpdate(kind="new_claim", key=claim.key, claim=draft, reason=u.rationale)
    return GraphUpdate(kind="supersede_claim", key=claim.key, claim_id=u.claim_id, claim=draft, reason=u.rationale)


# --- the caller --------------------------------------------------------------------------------------------------------

class RoleCaller:
    """The only code that calls the model. Each method sends one structured call (LLMClient.call with the output
    model and a check, which allows exactly one repair) and returns the parsed output, or None after logging the
    failure in `failures` (and `last_error`). `calls_used` counts every send (repairs and max_tokens retries
    included), `cost_usd` the spend, `usage` both per v9 role. A call is refused before sending unless `calls_used +
    4 <= max_calls`; ordinary calls also leave `reserve` sends for the final comparison. `currency_exhausted` is set
    when the profile's currency budget refuses a call.

    Replay (SPEC 13.4) answers every call from the response cache, which never holds a reply cut by max_tokens, a
    content-filter refusal or a reply that never came: `unreplayable` lists each call that met one of these (so the
    manifest can say the run will not replay), and `replay_miss` is set when the refusing replay transport found no
    cached reply, so the engine stops instead of deciding from a different graph. Failure kinds are short fixed words
    (invalid_output, max_tokens, content_filter, replay_miss, budget_currency, budget_model_calls, or the exception
    type); provider text stays in the failure's message, never in a packet."""

    def __init__(self, client: LLMClient, config: Mapping[str, Any], *, max_calls: int | None = None,
                 reserve: int | None = None):
        self.client = client
        self.config = config
        self.keys = role_keys(config)
        llm = config.get("llm") or {}
        unknown = sorted({k for k in self.keys.values() if k not in llm})
        if unknown:
            raise ValueError(f"v9.roles maps onto unknown llm keys: {', '.join(unknown)}")
        cap, keep = model_call_limits(config)
        self.max_calls = cap if max_calls is None else max_calls
        self.reserve = keep if reserve is None else reserve
        self.calls_used = 0
        self.cost_usd = 0.0
        self.usage: dict[str, dict[str, Any]] = {}
        self.failures: list[dict[str, Any]] = []
        self.last_error = ""
        self.currency_exhausted = False
        self.replay_miss = False
        self.unreplayable: list[dict[str, str]] = []

    def set_limits(self, max_calls: int, reserve: int) -> None:
        """The engine's limits win over the config's when it is given explicit ones."""
        self.max_calls, self.reserve = max_calls, reserve

    def affordable(self, final: bool = False) -> bool:
        """Whether one more call fits: `calls + 4 <= cap`, and for an ordinary call also the reserve."""
        return self.calls_used + GUARD + (0 if final else self.reserve) <= self.max_calls

    def role_models(self) -> dict[str, dict[str, Any]]:
        """v9 role -> the LLMClient key, model, effort and max_tokens it runs with (for the manifest)."""
        llm = self.config.get("llm") or {}
        return {role: {"key": key, "model": llm.get(key), "effort": (llm.get("effort") or {}).get(key),
                       "max_tokens": (llm.get("max_tokens") or {}).get(key)} for role, key in self.keys.items()}

    def propose(self, packet: str, check: Callable, *, regenerate: bool) -> V9Propose | None:
        return self._call("coordinator", "regenerate" if regenerate else "propose", system_prompt("coordinator"),
                          packet, V9Propose, check)

    def plan(self, packet: str, check: Callable) -> V9Plan | None:
        return self._call("coordinator", "plan", system_prompt("coordinator"), packet, V9Plan, check)

    def investigate(self, route: str, packet: str, check: Callable, *, step: str) -> V9Investigate | None:
        role = ROUTE_ROLE[route]
        return self._call(role, f"investigate_{step}", system_prompt(role, route), packet, V9Investigate, check,
                          key_role="extraction" if step == "extract" else role)

    def audit(self, packet: str, check: Callable) -> V9Critique | None:
        return self._call("critic", "audit", system_prompt("critic"), packet, V9Critique, check)

    def final(self, packet: str, check: Callable) -> V9Final | None:
        return self._call("critic", "final", system_prompt("critic"), packet, V9Final, check, final=True)

    def read(self, system: str, packet: str, model: type[Strict], check: Callable) -> Any:
        """One article read by the reader (reader.py, which owns the prompt and the output model): counted under the
        role "reader", with the model settings of the literature investigator."""
        return self._call("reader", "read", system, packet, model, check, key_role="literature_investigator")

    def critique(self, system: str, packet: str, model: type[Strict], check: Callable) -> Any:
        """One article record checked by the fill's critic (critic.py, which owns the prompt and the output model),
        on the critic's own model client: counted under the role "critic", with that client's critic settings."""
        return self._call("critic", "check", system, packet, model, check, key_role="critic")

    def judge(self, system: str, packet: str, model: type[Strict], check: Callable) -> Any:
        """One tie read by the fill's judge (judge.py, which owns the prompt and the output model), on the second
        model's client: counted under the role "judge", with that client's critic settings."""
        return self._call("judge", "tie", system, packet, model, check, key_role="critic")

    def _fail(self, role: str, stage: str, kind: str, message: str) -> None:
        self.last_error = f"{kind}: {message}"[:600]
        self.failures.append({"role": role, "stage": stage, "kind": kind, "message": message[:600]})
        self.usage.setdefault(role, self._blank())["failures"] += 1
        log.warning("v9 %s %s failed: %s", role, stage, self.last_error)

    @staticmethod
    def _not_cached(kind: str, sends: int) -> str | None:
        """Why a failed call cannot be answered from the response cache on replay, or None when it can. A reply that
        failed validation twice is cached and fails the same way again, unless a max_tokens retry made more than two
        sends; a guard refusal sends nothing in either run; a replay's own miss is not a property of the run."""
        if kind in ("budget_model_calls", "replay_miss") or (kind == "invalid_output" and sends <= 2):
            return None
        return {"invalid_output": "a reply cut by max_tokens was retried; the cut reply is not cached",
                "max_tokens": "replies cut by max_tokens are not cached",
                "content_filter": "a content-filter refusal is not cached",
                "budget_currency": "the currency budget refused a send; a replay, whose cached replies cost nothing, "
                                   "would go on"}.get(kind, f"the provider call failed ({kind}); no reply was cached")

    @staticmethod
    def _blank() -> dict[str, Any]:
        return {"calls": 0, "cost_usd": 0.0, "failures": 0, "prompt_tokens": 0, "completion_tokens": 0,
                "latency_s": 0.0}

    def _call(self, role: str, stage: str, system: str, packet: str, model: type[Strict], check: Callable,
              *, final: bool = False, key_role: str | None = None) -> Any:
        if self.currency_exhausted:
            self._fail(role, stage, "budget_currency", "the currency budget is exhausted")
            return None
        if not self.affordable(final):
            self._fail(role, stage, "budget_model_calls", f"{self.calls_used} of {self.max_calls} model calls used")
            return None
        calls, cost = self.client.calls, self.client.total_cost
        trace = {"v9_role": role, "v9_stage": stage, "packet_sha256": hashlib.sha256(packet.encode()).hexdigest()}
        result, failure = None, None
        try:
            result = self.client.call(self.keys[key_role or role], f"v9_{stage}", system,
                                      [{"role": "user", "content": packet}], output_model=model, check=check,
                                      trace=trace)
        except BudgetExceeded as e:
            self.currency_exhausted = True
            failure = ("budget_currency", str(e))
        except ReplayMiss as e:
            self.replay_miss = True
            failure = ("replay_miss", str(e))
        except Refused as e:
            failure = ("content_filter", str(e))
        except LLMError as e:
            text = str(e)
            failure = ("invalid_output" if "failed validation" in text else
                       "max_tokens" if "max_tokens" in text else type(e).__name__, text)
        except Exception as e:  # a transport or provider failure is recorded, never raised into the engine
            failure = (type(e).__name__, str(e))
        used = self.client.calls - calls
        spent = self.client.total_cost - cost
        self.calls_used += used
        self.cost_usd = round(self.cost_usd + spent, 6)
        usage = self.usage.setdefault(role, self._blank())
        usage["calls"] += used
        usage["cost_usd"] = round(usage["cost_usd"] + spent, 6)
        if failure is not None:
            if why := self._not_cached(failure[0], used):
                self.unreplayable.append({"role": role, "stage": stage, "why": why})
            self._fail(role, stage, *failure)
            return None
        if "max_tokens" in result.retries:
            self.unreplayable.append({"role": role, "stage": stage,
                                      "why": "a reply cut by max_tokens was retried; the cut reply is not cached"})
        usage["prompt_tokens"] += int((result.usage or {}).get("prompt_tokens") or 0)
        usage["completion_tokens"] += int((result.usage or {}).get("completion_tokens") or 0)
        usage["latency_s"] = round(usage["latency_s"] + result.latency, 2)
        return result.parsed
