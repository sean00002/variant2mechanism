"""Model output schemas (spec 2, section 4) and the code checks the schemas cannot express.

No dict fields and no numeric bounds: structured outputs need closed objects and do not enforce ranges, so ranges
and counts are checked in code (`check_chains`, `check_revised`, `check_regrade`).
"""

from typing import Literal

from pydantic import BaseModel

Step = Literal["binding", "element", "gene", "cell_type", "phenotype"]
Status = Literal["supported", "weak", "missing"]
STEPS: list[str] = ["binding", "element", "gene", "cell_type", "phenotype"]


class Link(BaseModel):
    step: Step
    claim: str
    evidence_ids: list[str]


class Hypothesis(BaseModel):
    id: str
    title: str
    is_null: bool
    tf: str | None                      # coverage_status is filled in by code from the registry (spec 3, 3.1)
    allele_binding_more: Literal["ref", "alt"] | None
    element: str | None
    target_gene: str | None
    cell_type: str | None
    links: list[Link]
    predictions: list[str]
    falsified_if: list[str]
    probability: float


class Chains(BaseModel):
    hypotheses: list[Hypothesis]


class LinkGrade(BaseModel):
    hypothesis_id: str
    step: Step
    status: Status
    reason: str


class Check(BaseModel):
    tool: str
    args_json: str
    resolves: str
    why: str


class CritiqueOut(BaseModel):                # the critique, and each round's regrade
    grades: list[LinkGrade]
    problems: list[str]
    checks: list[Check]


class PlannedCall(BaseModel):
    tool: str
    args_json: str
    resolves: str
    expected: str                           # the result expected, and what it would change


class Plan(BaseModel):
    calls: list[PlannedCall]
    stop_reason: str                        # empty unless `calls` is empty


class CheckResult(BaseModel):
    call: str
    observed: str
    as_expected: Literal["yes", "no", "unclear"]


class Outcome(BaseModel):
    hypothesis_id: str
    outcome: str


class PredictionRow(BaseModel):
    test: str
    cost: Literal["existing data", "low", "medium", "high"]
    outcomes: list[Outcome]
    separates_top_two: bool


class Revised(BaseModel):
    hypotheses: list[Hypothesis]
    matrix: list[PredictionRow]
    next_experiment: str


class RevisedRound(Revised):                # a refinement round's revision: also each call's result against its plan
    check_results: list[CheckResult]


class Quote(BaseModel):
    pmid: str
    sentence: str


class Quotes(BaseModel):
    quotes: list[Quote]


# -- code checks ----------------------------------------------------------------------------------------------


class SchemaCheckError(ValueError):
    """A model output that parses but breaks a rule; the message is sent back to the model on the retry."""


def check_chains(hyps: list[Hypothesis]) -> list[Hypothesis]:
    """Exactly one null, 3 to 5 chains, unique ids, the five steps once each in order; probabilities normalised."""
    problems = []
    if not 3 <= len(hyps) <= 5:
        problems.append(f"give 3 to 5 chains, not {len(hyps)}")
    nulls = [h for h in hyps if h.is_null]
    if len(nulls) != 1:
        problems.append(f"exactly one chain must have is_null true; found {len(nulls)}")
    ids = [h.id for h in hyps]
    if len(set(ids)) != len(ids):
        problems.append(f"chain ids must be unique; got {ids}")
    for h in hyps:
        if h.is_null:
            if h.links:
                problems.append(f"{h.id} is the null: its links must be empty")
            continue
        steps = [link.step for link in h.links]
        if steps != STEPS:
            problems.append(f"{h.id}: links must be the five steps once each in order {STEPS}; got {steps}")
        if not h.tf or "," in h.tf or " " in h.tf.strip():
            problems.append(f"{h.id}: tf must be one HGNC symbol; got {h.tf!r}")
        if h.allele_binding_more is None:
            problems.append(f"{h.id}: allele_binding_more must be 'ref' or 'alt' for a non-null chain")
    if any(h.probability < 0 for h in hyps):
        problems.append("probabilities must not be negative")
    if problems:
        raise SchemaCheckError("; ".join(problems))
    total = sum(h.probability for h in hyps)
    for h in hyps:
        h.probability = (h.probability / total) if total > 0 else 1 / len(hyps)
    return hyps


def check_revised(out: Revised) -> Revised:
    check_chains(out.hypotheses)
    ids = {h.id for h in out.hypotheses}
    for row in out.matrix:
        bad = {o.hypothesis_id for o in row.outcomes} - ids
        if bad:
            raise SchemaCheckError(f"matrix row '{row.test[:40]}' names unknown hypotheses {sorted(bad)}")
    if not out.matrix:
        raise SchemaCheckError("give at least one prediction-matrix row")
    return out


def required_grades(hyps: list[Hypothesis]) -> set[tuple[str, str]]:
    return {(h.id, link.step) for h in hyps if not h.is_null for link in h.links}


def check_grades(grades: list[LinkGrade], hyps: list[Hypothesis]) -> list[LinkGrade]:
    """Every link graded exactly once; grades for unknown links are dropped."""
    need = required_grades(hyps)
    got = [(g.hypothesis_id, g.step) for g in grades]
    missing = need - set(got)
    if missing:
        raise SchemaCheckError(f"grade every link; missing {sorted(missing)[:8]}")
    seen, out = set(), []
    for g in grades:
        k = (g.hypothesis_id, g.step)
        if k in need and k not in seen:
            seen.add(k)
            out.append(g)
    return out
