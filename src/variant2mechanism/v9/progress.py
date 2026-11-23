"""Content-based checks for repeated reading. New focus words alone are not new observations."""

import hashlib
import json
import re

from .graph import ClaimGraph


def read_state(graph: ClaimGraph, question_id: str, call_ids: list[str]) -> tuple[tuple, frozenset[str]] | None:
    """The biological question scope and the passages actually returned, independent of focus words/call ids.

    Do not coalesce different claim entities, directions or contexts. Actual abstract text can be recognised as
    already read; missing/error responses cannot. A later full-text passage remains new information.
    """
    passages: set[str] = set()
    articles: set[str] = set()
    for tid in call_ids:
        call = graph.tool_calls[tid]
        if call.tool_name != "literature_read":
            continue
        if call.execution_status != "success":
            return None
        article = next((o for o in call.observations if o.get("kind") == "article"), {})
        source = article.get("pmcid") or article.get("pmid") or article.get("doi")
        if not source or article.get("access") not in ("full_text", "abstract_only"):
            return None
        articles.add(source)
        for observation in call.observations:
            if observation.get("kind") == "reference":
                key = [source, "reference", {k: observation.get(k) for k in
                       ("reference_id", "pmid", "pmcid", "doi", "title", "citation")}]
                passages.add(hashlib.sha256(json.dumps(key, sort_keys=True).encode()).hexdigest())
            if observation.get("location") and observation.get("text"):
                text = re.sub(r"\s+", " ", observation["text"]).strip()
                key = [source, observation["location"], text]
                passages.add(hashlib.sha256(json.dumps(key).encode()).hexdigest())
    if not passages:
        return None
    scope = []
    for cid in graph.questions[question_id].target_claim_ids:
        c = graph.claims[cid]
        scope.append(json.dumps([c.subject_ids, c.relation, c.object_ids, c.direction, c.effect_allele,
                                 c.context_scope.model_dump(mode="json") if c.context_scope else None,
                                 c.dependencies], sort_keys=True))
    return (tuple(sorted(scope)), tuple(sorted(articles))), frozenset(passages)
