"""Operational gap reminders; no new claims, causal edges, scores or evidence are inferred."""

from collections.abc import Iterable

from .graph import ClaimGraph


def gap_lines(graph: ClaimGraph, claim_ids: Iterable[str]) -> list[str]:
    claims = [graph.claims[c] for c in sorted(set(claim_ids)) if c in graph.claims and
              not graph.claims[c].superseded_by]
    lines = []
    for c in claims:
        kinds = {graph.entities[e].kind for e in c.subject_ids + c.object_ids}
        if c.relation == "overlaps" and {"variant", "element"} <= kinds:
            activity = [x.claim_id for x in claims if x.relation == "alters_regulatory_activity" and
                        set(x.subject_ids) == set(c.subject_ids) and set(x.object_ids) == set(c.object_ids)]
            detail = ", ".join(f"{cid} ({graph.display(cid).status})" for cid in activity) or "not proposed"
            lines.append(f"{c.claim_id}: localisation is not an allelic effect. Variant-to-element activity: "
                         f"{detail}. Seek allele-resolved results; region deletion only tests the region. "
                         "Do not reject for missing results or require a modern database accession in an old paper.")
        if c.relation == "alters_regulatory_activity" and "variant" in kinds:
            molecular = [x.claim_id for x in claims if set(x.subject_ids) == set(c.subject_ids) and
                         x.relation in ("alters_binding", "alters_rna")]
            detail = ", ".join(f"{cid} ({graph.display(cid).status})" for cid in molecular) or "not proposed"
            lines.append(f"{c.claim_id}: activity status {graph.display(c.claim_id).status}; candidate molecular "
                         f"changes: {detail}. Even a supported activity effect can leave HOW unresolved. "
                         "Inspect primary results for binding, chromatin, RNA or another measured process. "
                         "TF binding is optional; a candidate binding/RNA effect alone does not establish "
                         "mediation of this activity effect. Preserve a coarse supported effect while refining it.")
        if c.relation == "occupies":
            lines.append(f"{c.claim_id}: occupancy localises a factor; ordinary ChIP does not establish an "
                         "allele-dependent binding change or its mediation of enhancer activity.")
    return lines
