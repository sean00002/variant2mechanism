"""Non-destructive scope relationships and hypothesis families.

These are derived views, never evidence or entailment edges. Unknown scope is not universal scope.
Shared ontology annotations justify only related_scope, never a population subset or evidence transfer.
"""

from itertools import combinations

from .context_match import is_unscoped, load_table, scope_key
from .traits import ontology_id, trait_key


def _phenotype_ids(graph, entity, claim):
    ids = {ontology_id(entity.canonical_id)} - {None}
    for link in claim.evidence_links:
        ev = graph.evidence[link.evidence_id]
        if trait_key(entity.label) in {trait_key(x) for x in ev.about_traits}:
            ids |= {ontology_id(x) for x in ev.about_traits} - {None}
    return ids


def _entities_match(graph, left, right, a, b):
    """Equal participants, or a shared phenotype annotation. The latter is only a possible relationship."""
    if set(left) == set(right):
        return True, True, []
    fixed_a = {x for x in left if graph.entities[x].kind != "phenotype"}
    fixed_b = {x for x in right if graph.entities[x].kind != "phenotype"}
    pa = [graph.entities[x] for x in left if graph.entities[x].kind == "phenotype"]
    pb = [graph.entities[x] for x in right if graph.entities[x].kind == "phenotype"]
    if fixed_a != fixed_b or len(pa) != 1 or len(pb) != 1:
        return False, False, []
    if trait_key(pa[0].label) == trait_key(pb[0].label):
        return True, True, []
    shared = sorted(_phenotype_ids(graph, pa[0], a) & _phenotype_ids(graph, pb[0], b))
    return bool(shared), False, shared


def _narrower(parent, child):
    """Only an explicitly recorded organ scope and a registry-known biosample from that organ.

    The relationship describes the scope hierarchy, not that an organ-level biological effect holds in every cell.
    Conditions/genotypes must agree; no free-text population hierarchy or tissue keyword is taken as proof.
    """
    if not parent or not child or not parent.tissue or parent.biosample or not child.biosample:
        return False
    rec = load_table().record(child.biosample)
    return bool(rec and rec.tissue == parent.tissue == child.tissue
                and parent.biosample_kind == "tissue" and parent.species == child.species
                and parent.condition == child.condition and parent.genotype == child.genotype)


def claim_refinements(graph):
    result = []
    claims = [c for c in graph.claims.values() if not c.superseded_by]
    for a, b in combinations(claims, 2):
        if (a.relation, a.mechanism_class) != (b.relation, b.mechanism_class):
            continue
        da = graph._key_direction(a.direction, a.effect_allele, graph._claim_frame(a))
        db = graph._key_direction(b.direction, b.effect_allele, graph._claim_frame(b))
        if da != db or a.allele_scope != b.allele_scope:
            continue
        sm, se, si = _entities_match(graph, a.subject_ids, b.subject_ids, a, b)
        om, oe, oi = _entities_match(graph, a.object_ids, b.object_ids, a, b)
        if not sm or not om:
            continue
        parent, child, kind = a, b, "related_scope"
        basis = "shared phenotype annotation; measurement/population nesting is not established"
        if se and oe:
            if scope_key(a.context_scope) == scope_key(b.context_scope):
                kind, basis = "equivalent_scope", "same participants, relation, allele frame and normalised scope"
            elif is_unscoped(a.context_scope) != is_unscoped(b.context_scope):
                parent, child = (a, b) if is_unscoped(a.context_scope) else (b, a)
                kind, basis = "specifies_scope", "adds missing context; unspecified does not mean universal"
            elif _narrower(a.context_scope, b.context_scope) or _narrower(b.context_scope, a.context_scope):
                parent, child = (a, b) if _narrower(a.context_scope, b.context_scope) else (b, a)
                kind, basis = "narrower_scope_than", "biosample-to-organ relation in the local context registry"
            else:
                basis = "same biological assertion in different contexts; no verified subset relationship"
        result.append({"parent_claim_id": parent.claim_id, "child_claim_id": child.claim_id,
                       "relation": kind, "basis": basis, "shared_annotations": sorted(set(si + oi)),
                       "transfers_evidence": False})
    return result


def hypothesis_families(graph, refinements=None):
    """Connected families for browsing; membership never merges, ranks, activates or rejects a hypothesis."""
    edges = claim_refinements(graph) if refinements is None else refinements
    groups = [{hid} for hid in graph.hypotheses]
    for a, b in combinations(graph.hypotheses.values(), 2):
        if a.mechanism_class != b.mechanism_class:
            continue
        ca, cb = set(a.required_claim_ids), set(b.required_claim_ids)
        related = bool(ca & cb) or any(
            (e["parent_claim_id"] in ca and e["child_claim_id"] in cb)
            or (e["child_claim_id"] in ca and e["parent_claim_id"] in cb) for e in edges)
        if related:
            ga = next(g for g in groups if a.hypothesis_id in g)
            gb = next(g for g in groups if b.hypothesis_id in g)
            if ga is not gb:
                ga.update(gb)
                groups.remove(gb)
    order = {h: i for i, h in enumerate(graph.hypotheses)}
    result = []
    for group in groups:
        members = sorted(group, key=order.__getitem__)
        claims = {c for h in members for c in graph.hypotheses[h].claim_ids}
        result.append({"family_id": f"family:{members[0]}", "hypothesis_ids": members,
                       "claim_ids": sorted(claims, key=lambda x: int(x[1:])),
                       "refinements": [e for e in edges if e["parent_claim_id"] in claims
                                       and e["child_claim_id"] in claims], "assessment": "not_assessed"})
    return result
