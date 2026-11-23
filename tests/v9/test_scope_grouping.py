"""Scope relationships organise claims; they never make evidence transferable."""

import json

from variant2mechanism.v9.graph import ClaimGraph, EntityRef
from variant2mechanism.v9.report import scope_html
from variant2mechanism.v9.schemas import ContextScope

from .test_graph import VARIANT, claim, ctx, dev_case, evidence, gene, hypothesis


def trait(g, label, canonical_id="EFO_1234567"):
    return claim(g, [VARIANT], "associated_with_trait",
                 [EntityRef(kind="phenotype", label=label, canonical_id=canonical_id)],
                 mechanism_class="association_only")


def test_different_measured_traits_are_retained_under_a_related_family():
    g = ClaimGraph(dev_case())
    a, b = trait(g, "Trait Q"), trait(g, "Trait Q in population R")
    ha, hb = hypothesis(g, [a], mechanism="association_only"), hypothesis(g, [b], mechanism="association_only")
    assert ha != hb and g.hypotheses[hb].claim_ids == [b]
    v = g.scope_views()
    assert v["hypothesis_families"][0]["hypothesis_ids"] == [ha, hb]
    assert v["claim_refinements"][0]["relation"] == "related_scope"
    assert not v["claim_refinements"][0]["transfers_evidence"]
    assert "subset" in scope_html(g)


def test_mean_and_maximum_are_related_not_subsets_and_unrelated_traits_stay_apart():
    g = ClaimGraph(dev_case())
    ids = [trait(g, "Trait Q (mean)"), trait(g, "Trait Q (maximum)"), trait(g, "Trait Z", "EFO_7654321")]
    hs = [hypothesis(g, [c], mechanism="association_only") for c in ids]
    v = g.scope_views()
    assert len(v["hypothesis_families"]) == 2
    assert v["hypothesis_families"][0]["hypothesis_ids"] == hs[:2]
    assert [e["relation"] for e in v["claim_refinements"]] == ["related_scope"]


def test_unknown_context_is_specified_not_universal_and_no_support_is_inherited():
    g = ClaimGraph(dev_case())
    a = claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")])
    b = claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], context=ctx("liver"))
    ha, hb = hypothesis(g, [a]), hypothesis(g, [b])
    e = evidence(g, "statistical_inference", "GENE1 association in liver", about_genes=["GENE1"],
                 about_variants=["rs1427407"], context=ctx("liver"))
    g.link(b, e, "supports", "computational_investigator")
    v = g.scope_views()
    assert ha != hb
    assert v["claim_refinements"][0]["relation"] == "specifies_scope"
    assert not g.claims[a].evidence_links and g.claims[a].assessment == "unassessed"
    assert len(g.claims[b].evidence_links) == 1 and len(g.evidence) == 1


def test_known_organ_to_biosample_scope_is_narrower_but_cells_are_not_nested():
    g = ClaimGraph(dev_case())
    ids = [claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], context=ctx(x))
           for x in ("liver", "HepG2", "Hep3B")]
    v = g.scope_views()["claim_refinements"]
    assert {(e["parent_claim_id"], e["child_claim_id"]) for e in v if e["relation"] == "narrower_scope_than"} == {
        (ids[0], ids[1]), (ids[0], ids[2])}
    assert next(e for e in v if e["parent_claim_id"] == ids[1])["relation"] == "related_scope"


def test_context_labels_alone_cannot_certify_a_tissue_subset():
    g = ClaimGraph(dev_case())
    for x in ("liver", "unregistered liver biosample"):
        claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], context=ctx(x))
    assert g.scope_views()["claim_refinements"][0]["relation"] == "related_scope"


def test_genotype_and_treatment_scopes_remain_distinct():
    g = ClaimGraph(dev_case())
    scopes = [ContextScope(genotype="G/G"), ContextScope(genotype="T/T"),
              ContextScope(condition="treated"), ContextScope(condition="untreated")]
    ids = [claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], context=s) for s in scopes]
    assert len(set(ids)) == 4
    assert all(e["relation"] == "related_scope" for e in g.scope_views()["claim_refinements"])


def test_different_directions_or_variants_do_not_refine_one_another():
    g = ClaimGraph(dev_case())
    for direction in ("increases", "decreases"):
        claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], direction)
    claim(g, [EntityRef(kind="variant", label="rs999")], "associated_with_expression", [gene("GENE1")])
    assert not g.scope_views()["claim_refinements"]


def test_duplicate_hypothesis_retains_new_optional_claim_and_is_auditable():
    g = ClaimGraph(dev_case())
    a, b = trait(g, "Trait Q"), trait(g, "Trait Z", "EFO_7654321")
    h = hypothesis(g, [a])
    assert hypothesis(g, [a], optional=[b]) == h
    assert g.hypotheses[h].claim_ids == [a, b]
    assert g.hypotheses[h].required_claim_ids == [a]
    assert g.events[-1].details == {"merge": True, "added_claim_ids": [b]}


def test_same_participants_in_different_edges_are_not_a_duplicate_mechanism():
    g = ClaimGraph(dev_case())
    a = claim(g, [gene("GENE1")], "regulates", [gene("GENE2")])
    b = claim(g, [gene("GENE2")], "regulates", [gene("GENE1")])
    assert hypothesis(g, [a]) != hypothesis(g, [b])


def test_scope_views_round_trip_and_loaded_views_cannot_inject_evidence():
    g = ClaimGraph(dev_case())
    a, b = trait(g, "Trait Q"), trait(g, "Trait Q in population R")
    hypothesis(g, [a])
    hypothesis(g, [b])
    original = g.to_json()
    assert ClaimGraph.from_json(original).to_json() == original
    body = json.loads(original)
    body["claim_refinements"][0]["transfers_evidence"] = True
    assert ClaimGraph.from_json(json.dumps(body)).to_json() == original


def test_legacy_coarse_signatures_do_not_collapse_distinct_scopes_on_resume():
    g = ClaimGraph(dev_case())
    a, b = trait(g, "Trait Q"), trait(g, "Trait Q in population R")
    ha, hb = hypothesis(g, [a]), hypothesis(g, [b])
    state = json.loads(g.to_json())
    for h in state["hypotheses"].values():
        h["signature"] = "legacy:association-with-no-phenotype"
    restored = ClaimGraph.from_json(json.dumps(state))
    assert hypothesis(restored, [b]) == hb and ha != hb
    assert len(restored.hypotheses) == 2
