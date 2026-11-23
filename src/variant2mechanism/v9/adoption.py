"""Evidence awaiting a scientific decision, derived from the graph rather than a second mutable store.

An observation that is context-only for the current claims may support a different claim. Keep it in planning
and audit packets until it has a non-context link in a live hypothesis, or an explicit deferral/set-aside decision.
Grouping here is for review only: it never merges evidence records or changes their scientific independence.
"""

import hashlib
import json
import re

from .evidence_view import index_lines
from .graph import ClaimGraph
from .schemas import Evidence

OBSERVATIONS = frozenset({"binding_assay", "occupancy", "reporter_assay", "perturbation", "expression",
                          "association", "statistical_inference", "clinical_assertion", "dependency_screen"})


def eligible(e: Evidence) -> bool:
    """Observed results, not mentions, predictions or interpretations. Scope is still judged by the coordinator."""
    return e.evidence_class in OBSERVATIONS and (
        e.origin != "literature" or (e.experiment is not None and
                                    e.experiment.authors_hypothesis_vs_result != "hypothesis"))


def review_key(e: Evidence) -> str:
    """Recognise re-extractions of a passage despite changes to its prose summary or biosample label.

    Distinct measured factors, alleles, directions and declared experimental conditions stay separate. Every
    grouped record is still displayed, including its scope; this key is not an evidence-independence identifier.
    """
    if e.experiment is None:
        return e.evidence_id
    x = e.experiment
    passage = re.sub(r"\s+", " ", x.passage).strip()
    body = [sorted(e.source_ids), x.location, passage, e.evidence_class, e.allele, e.direction,
            sorted(e.about_tfs), sorted(e.about_genes), sorted(e.about_elements), sorted(e.about_variants),
            sorted(e.about_traits), e.context.species if e.context else None,
            e.context.condition if e.context else None, x.manipulated]
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


def represented_by(graph: ClaimGraph, evidence_id: str) -> list[str]:
    live = {c for h in graph.hypotheses.values() if h.disposition not in ("rejected", "superseded")
            for c in h.claim_ids}
    return sorted(c for c in live if not graph.claims[c].superseded_by and
                  any(link.evidence_id == evidence_id and link.stance != "context_only" and
                      link.strength != "context" for link in graph.claims[c].evidence_links))


def decisions(graph: ClaimGraph) -> dict[str, dict]:
    latest = {}
    for event in graph.events:
        if event.action == "review_evidence":
            for eid in event.evidence_ids:
                if eid in graph.evidence:
                    latest[review_key(graph.evidence[eid])] = event.details
    return latest


def pending(graph: ClaimGraph) -> list[list[str]]:
    """All unresolved review groups, in evidence insertion order; never prioritised by a QBiC gate."""
    initial: set[str] = set()
    for event in graph.events:
        if event.action == "propose":
            break
        initial.update(event.evidence_ids)
    else:
        initial.clear()  # standalone graphs have no proposal boundary
    groups: dict[str, list[str]] = {}
    for eid, evidence in graph.evidence.items():
        if eligible(evidence) and (eid not in initial or evidence.origin == "literature"):
            groups.setdefault(review_key(evidence), []).append(eid)
    reviewed = decisions(graph)
    return [ids for key, ids in groups.items()
            if not any(represented_by(graph, eid) for eid in ids)
            and reviewed.get(key, {}).get("disposition") not in ("defer", "set_aside")]


def context_lines(graph: ClaimGraph) -> list[str]:
    lines = []
    groups = pending(graph)
    required = required_reviews(graph)
    if len(groups) > len(required):
        remaining = [eid for ids in groups if ids not in required for eid in ids]
        lines += [f"This plan must address the {len(required)} review groups listed below. "
                  f"{len(groups) - len(required)} other groups remain pending; no bulk judgement is required. "
                  "Unreviewed means unresolved, never irrelevant or refuted."]
    else:
        remaining = []
    for ids in required:
        e = graph.evidence[ids[0]]
        lines.append(f"{', '.join(ids)}: observation awaiting adoption; class {e.evidence_class}; "
                     f"TFs {', '.join(e.about_tfs) or 'none'}; genes {', '.join(e.about_genes) or 'none'}; "
                     f"variants {', '.join(e.about_variants) or 'not named'}. Context-only for an old claim "
                     "does not mean irrelevant to a new one.")
    if remaining:
        lines += index_lines(graph, remaining, max_chars=4000)
    for decision in decisions(graph).values():
        if decision.get("disposition") in ("defer", "set_aside"):
            lines.append(f"Earlier {decision['disposition']}: {', '.join(decision['evidence_ids'])}; "
                         f"{decision['reason']}; revisit: {decision.get('revisit_trigger') or 'not specified'}")
    return lines


def required_reviews(graph: ClaimGraph, limit: int = 6) -> list[list[str]]:
    """Bound the work of one plan, not the evidence store. Experimental observations precede bulk associations."""
    experimental = {"binding_assay", "occupancy", "reporter_assay", "perturbation"}
    return sorted(pending(graph), key=lambda ids: (graph.evidence[ids[0]].origin != "literature",
        graph.evidence[ids[0]].evidence_class not in experimental, int(ids[0][1:])))[:limit]
