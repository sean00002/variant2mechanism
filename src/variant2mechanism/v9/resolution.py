"""Report molecular findings separately from completion/ranking of a declared hypothesis.

This derived view never promotes a hypothesis, changes an assessment or transfers evidence between claims.
"""

from .graph import ClaimGraph

MOLECULAR = frozenset({"alters_binding", "alters_regulatory_activity", "alters_rna"})


def support_summary(graph: ClaimGraph) -> dict:
    def settled(cid, hid=None):
        c = graph.claims[cid]
        return (c.assessment == "supported_in_scope" and not c.superseded_by and c.dependency_flag == "none"
                and (hid is None or graph.hypotheses[hid].path_status.get(cid, "intact") == "intact"))

    molecular = [cid for cid, c in graph.claims.items() if c.relation in MOLECULAR and
                 graph.claim_frame(cid) == "case" and settled(cid) and any(
                     link.stance == "supports" and link.applicability in ("exact", "proxy") and
                     link.strength == "direct" and
                     graph.evidence[link.evidence_id].evidence_class not in ("prediction", "annotation")
                     for link in c.evidence_links)]
    hypotheses = {hid: h for hid, h in graph.hypotheses.items()
                  if h.disposition not in ("rejected", "superseded")}
    membership = {cid: [hid for hid, h in hypotheses.items() if cid in h.claim_ids and settled(cid, hid)]
                  for cid in molecular}
    complete = [hid for hid, h in hypotheses.items() if h.required_claim_ids and
                any(hid in membership[cid] for cid in molecular) and
                all(settled(cid, hid) for cid in h.required_claim_ids)]
    gaps = {hid: [cid for cid in h.required_claim_ids if not settled(cid, hid)] for hid, h in hypotheses.items()}
    return {
        "molecular_status": "supported" if molecular else "not_established",
        "molecular_label": ("Supported molecular claims" if complete else "Supported partial mechanism")
                           if molecular else "No supported variant-level molecular claim yet",
        "supported_molecular_claim_ids": molecular,
        "claim_hypotheses": membership,
        "required_link_status": "supported_for_declared_endpoint" if complete else "unresolved",
        "required_link_label": "Required links supported for a declared endpoint" if complete else
                               "Complete mechanism chain unresolved",
        "supported_required_path_ids": complete,
        "required_gaps": gaps,
        "note": "Molecular support includes optional claims and is scoped to their linked evidence. Required-link "
                "completion is relative to each stated endpoint; a molecular-only endpoint is not disease mediation. "
                "Neither field chooses a winning hypothesis or changes the whole-hypothesis comparison.",
    }
