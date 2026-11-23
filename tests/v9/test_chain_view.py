"""chain.py: claims read link by link, the strongest kind of evidence on each, and an order that allows ties.

Graphs are built through the graph API on the development variant rs1427407 (chr2:60490908 T>G); TF, gene and trait
names and every observation are stipulated for the tests, not claims about that variant.
"""

import json

import pytest

from variant2mechanism.v9 import bundle, chain, report
from variant2mechanism.v9.graph import ClaimGraph, EntityRef, GraphRefusal, HypothesisDraft
from variant2mechanism.v9.schemas import Evidence, RunResult, ToolCall

from .test_report_support import (
    ELEMENT,
    HEPG2,
    VARIANT,
    claim,
    dev_case,
    gene,
    inventory_call,
    inventory_row,
    rich_graph,
    tf,
    tool_evidence,
    write_run,
)

TRAIT = EntityRef(kind="phenotype", label="LDL cholesterol")
INVESTIGATOR = "computational_investigator"


def group(i: int, members: list[str]) -> EntityRef:
    return EntityRef(kind="tf_group", label=f"G{i:03d}", canonical_id=f"G{i:03d}", members=members)


def hypothesis(g: ClaimGraph, title: str, required=(), optional=(), **kw) -> str:
    return g.add_hypothesis(HypothesisDraft(title=title, claim_ids=list(optional), required_claim_ids=list(required),
                                            **kw), "coordinator")


def link_of(view: dict, key: str) -> dict:
    return next(x for x in view["links"] if x["key"] == key)


def candidate(view: dict, key: str, label: str) -> dict:
    return next(c for c in link_of(view, key)["candidates"] if c["label"].startswith(label))


def binding_assay(g: ClaimGraph, symbol: str, assess: bool = True) -> str:
    """A binding claim for one TF with an allele-comparing assay linked in the claim's own context."""
    cid = claim(g, [VARIANT], "alters_binding", [tf(symbol)], "increases", HEPG2)
    eid = tool_evidence(g, "binding_assay", f"EMSA: {symbol} binds the G probe more.", about_tfs=[symbol], allele="G",
                        direction="increases", about_variants=["rs1427407"], context=HEPG2)
    g.link(cid, eid, "supports", INVESTIGATOR, "the G probe binds more")
    if assess:
        g.assess(cid, "supported_in_scope", "allelic EMSA", "critic", g.claims[cid].version)
    return cid


def eqtl(g: ClaimGraph, symbol: str) -> str:
    cid = claim(g, [VARIANT], "associated_with_expression", [gene(symbol)], "increases")
    eid = tool_evidence(g, "association", f"eQTL: G is associated with higher {symbol}.", about_genes=[symbol],
                        allele="G", direction="increases", about_variants=["rs1427407"])
    g.link(cid, eid, "supports", INVESTIGATOR, "same allele and direction")
    g.assess(cid, "supported_in_scope", "eQTL", "critic", g.claims[cid].version)
    return cid


def gwas(g: ClaimGraph) -> str:
    cid = claim(g, [VARIANT], "associated_with_trait", [TRAIT], "decreases")
    eid = tool_evidence(g, "association", "GWAS: G is associated with lower LDL cholesterol.",
                        about_traits=["LDL cholesterol"], allele="G", direction="decreases",
                        about_variants=["rs1427407"])
    g.link(cid, eid, "supports", INVESTIGATOR, "same allele and direction")
    return cid


def fragments() -> ClaimGraph:
    """Three hypotheses that each hold one part of a route: binding, a target gene and the trait association."""
    g = ClaimGraph(dev_case())
    hypothesis(g, "TFX binding differs", [binding_assay(g, "TFX")], mechanism_class="tf_binding")
    hypothesis(g, "GENE1 expression association", [eqtl(g, "GENE1")], mechanism_class="association_only")
    hypothesis(g, "LDL association", [gwas(g)], mechanism_class="association_only", endpoint="LDL cholesterol")
    return g


@pytest.mark.parametrize("strength, cls, rung", [
    ("direct", "perturbation", "edit"), ("direct", "dependency_screen", "edit"),
    ("direct", "reporter_assay", "assay"), ("direct", "binding_assay", "assay"), ("direct", "occupancy", "assay"),
    ("direct", "association", "association"), ("indirect", "statistical_inference", "association"),
    ("indirect", "prediction", "prediction"), ("indirect", "precomputed_prediction", "prediction"),
    ("indirect", "perturbation", None), ("indirect", "binding_assay", None), ("indirect", "occupancy", None),
    ("direct", "annotation", None), ("direct", "expression", None), ("context", "reporter_assay", None),
])
def test_a_rung_is_read_from_the_links_strength_and_class(strength, cls, rung):
    assert chain.link_rung(strength, cls) == rung


def test_the_ladder_is_ordered_by_kind_of_evidence_only():
    assert [r["key"] for r in chain.chain_view(ClaimGraph(dev_case()))["rungs"]] == [
        "edit", "assay", "association", "prediction", "none"]
    assert chain.LEVEL == {"edit": 4, "assay": 3, "association": 2, "prediction": 1, "none": 0}


def test_three_fragment_hypotheses_read_as_one_chain():
    g = fragments()
    view = chain.chain_view(g)
    assert [(x["key"], x["rung"]) for x in view["links"]] == [
        ("binding", "assay"), ("activity", None), ("gene", "association"), ("mediation", None),
        ("trait", "association")]
    assert view["links_measured"] == ["binding"] and view["links_with_evidence"] == ["binding", "gene", "trait"]
    assert view["summary"] == ("TF binding: allele-resolved assay (TFX) · Regulatory activity: no claim · "
                               "Target gene: association (GENE1) · Gene to trait: no claim · "
                               "Variant to trait: association (LDL cholesterol)")
    # an association is what a variant-to-trait link can have, so it is not reported as a gap
    assert [m["link"] for m in view["missing"]] == ["activity", "gene", "mediation"]
    order = view["order"]
    assert order["tiers"] == [["H1", "H2", "H3"]] and order["above"] == [] and order["ties"] == []
    assert order["parts_of_one_route"] is True
    assert any("parts of one route, not as rivals" in t for t in order["text"])


def test_the_view_changes_nothing_and_is_deterministic_json():
    g = rich_graph()
    before = g.to_json()
    first = chain.chain_view(g)
    assert g.to_json() == before
    assert json.loads(json.dumps(first)) == first == chain.chain_view(g)
    assert not any(k in first for k in ("score", "probability", "confidence"))


def test_an_assessment_is_shown_beside_the_rung_never_changed_by_it():
    g = fragments()
    view = chain.chain_view(g)
    trait = candidate(view, "trait", "LDL cholesterol")
    assert (trait["rung"], trait["assessment"], trait["settled"]) == ("association", "unassessed", False)
    assert "not assessed" in chain.candidate_text(trait, "G")
    assert g.claims[trait["claims"][0]["id"]].assessment == "unassessed"
    binding = candidate(view, "binding", "TFX")
    assert (binding["rung"], binding["settled"], binding["status"]) == ("assay", True, "supported")


def test_a_context_match_its_proposer_weakened_is_said_so():
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "associated_with_trait", [TRAIT], "decreases")
    eid = tool_evidence(g, "association", "GWAS: G is associated with lower LDL cholesterol.",
                        about_traits=["LDL cholesterol"], allele="G", direction="decreases",
                        about_variants=["rs1427407"])
    link = g.link(cid, eid, "supports", "coordinator", "same allele and direction", applicability="unknown")
    assert (link.applicability, link.code_applicability) == ("exact", "exact")         # no judgement: code's stands
    assert candidate(chain.chain_view(g), "trait", "LDL cholesterol")["claims"][0]["weakened"] == []
    link.applicability = "unknown"                 # as a run saved before that rule holds it: the weaker value kept
    with pytest.raises(GraphRefusal, match="supported_in_scope needs"):
        g.assess(cid, "supported_in_scope", "GWAS", "critic", g.claims[cid].version)
    cand = candidate(chain.chain_view(g), "trait", "LDL cholesterol")
    assert cand["rung"] == "association" and cand["claims"][0]["weakened"] == [eid]
    assert "its proposer declared the context match unknown, though code computed a match" in chain.candidate_text(
        cand, "G")
    exact = candidate(chain.chain_view(fragments()), "trait", "LDL cholesterol")        # code's own value, unweakened
    assert exact["claims"][0]["weakened"] == [] and "context match" not in chain.candidate_text(exact, "G")


def test_the_alt_allele_frame_is_used_for_every_direction():
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "decreases", HEPG2, effect_allele="T")   # T is the ref
    read = candidate(chain.chain_view(g), "binding", "TFX")["claims"][0]
    assert read["id"] == cid and read["effect_allele"] == "T" and read["alt_direction"] == "increases"
    assert "G ↑" in chain.claim_text(read, "G")


def test_an_unlinked_inventory_prediction_gives_the_prediction_rung():
    g = ClaimGraph(dev_case())
    inventory = inventory_call(g, [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"},
                                                           {"tf": "TFZ", "mapping": "cisbp"}])])
    cid = claim(g, [VARIANT], "alters_binding", [group(1, ["TFX", "TFZ"])], "increases")
    view = chain.chain_view(g)
    cand = candidate(view, "binding", "G001")
    assert (cand["rung"], cand["source"], cand["settled"]) == ("prediction", "inventory", False)
    prediction = cand["claims"][0]["prediction"]
    assert prediction["state"] == "agrees" and prediction["linked"] is False
    assert [i["evidence"] for i in prediction["items"]] == inventory.evidence_ids
    assert "read from the inventory, not linked by a role" in chain.candidate_text(cand, "G")
    assert g.claims[cid].evidence_links == [] and g.display(cid).status == "unresolved"     # nothing was linked
    assert link_of(view, "binding")["rung"] == "prediction"
    assert [m["text"] for m in view["missing"] if m["link"] == "binding"] == [
        "TF binding: predicted only: no measurement is linked."]


def test_a_linked_prediction_is_read_from_its_link():
    g = ClaimGraph(dev_case())
    inventory = inventory_call(g, [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"}])])
    cid = claim(g, [VARIANT], "alters_binding", [group(1, ["TFX"])], "increases")
    g.link(cid, inventory.evidence_ids[0], "supports", INVESTIGATOR, "the TFX model favours G")
    cand = candidate(chain.chain_view(g), "binding", "G001")
    assert (cand["rung"], cand["source"]) == ("prediction", "links")
    assert cand["claims"][0]["prediction"]["linked"] is True
    assert "not linked by a role" not in chain.candidate_text(cand, "G")


def test_a_prediction_for_the_other_allele_gives_no_rung():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"}])])       # the model favours G (alt)
    claim(g, [VARIANT], "alters_binding", [group(1, ["TFX"])], "decreases")              # the claim says G binds less
    cand = candidate(chain.chain_view(g), "binding", "G001")
    assert (cand["rung"], cand["level"]) == ("none", 0)
    assert cand["claims"][0]["prediction"]["state"] == "disagrees"
    assert "this opposes the claim's direction" in chain.candidate_text(cand, "G")


def test_a_claim_without_a_direction_still_reads_the_prediction():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"}])])
    claim(g, [VARIANT], "alters_binding", [tf("TFX")])                                    # direction unspecified
    cand = candidate(chain.chain_view(g), "binding", "TFX")
    assert cand["rung"] == "prediction" and cand["claims"][0]["prediction"]["state"] == "direction_unstated"


def test_models_scored_below_the_gate_and_factors_without_a_model_are_told_apart():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, False, [{"tf": "TFX", "mapping": "own"}]), inventory_row(2, True)])
    claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")
    claim(g, [VARIANT], "alters_binding", [tf("TFQ")], "increases")
    view = chain.chain_view(g)
    below, absent = candidate(view, "binding", "TFX"), candidate(view, "binding", "TFQ")
    assert below["claims"][0]["prediction"] == {"state": "below_gate", "items": [], "linked": False,
                                                "groups": ["G001"], "large": []}
    assert absent["claims"][0]["prediction"]["state"] == "not_covered"
    assert below["rung"] == absent["rung"] == "none"
    assert "none passes the gate" in chain.candidate_text(below, "G")
    assert "holds no model covering it" in chain.candidate_text(absent, "G")


def test_no_inventory_means_no_prediction_entry():
    g = ClaimGraph(dev_case())
    claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")
    assert candidate(chain.chain_view(g), "binding", "TFX")["claims"][0]["prediction"] is None


def test_a_member_assay_joins_its_groups_candidate():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"}, {"tf": "TFZ", "mapping": "cisbp"}])])
    group_claim = claim(g, [VARIANT], "alters_binding", [group(1, ["TFX", "TFZ"])], "increases")
    member_claim = binding_assay(g, "TFX")
    view = chain.chain_view(g)
    assert len(link_of(view, "binding")["candidates"]) == 1
    cand = link_of(view, "binding")["candidates"][0]
    assert cand["label"] == "G001 (TFX, TFZ)" and cand["rung"] == "assay" and cand["settled"] is True
    assert [r["id"] for r in cand["claims"]] == [member_claim, group_claim]              # strongest first
    assert cand["claims"][0]["names"] == ["TFX"]
    assert f"{member_claim} (TFX) supported in scope" in chain.candidate_text(cand, "G")
    assert g.claims[group_claim].evidence_links == []                                     # nothing was transferred


def test_a_member_of_two_groups_with_claims_stays_its_own_candidate():
    g = ClaimGraph(dev_case())
    claim(g, [VARIANT], "alters_binding", [group(1, ["TFX", "TFA"])], "increases")
    claim(g, [VARIANT], "alters_binding", [group(2, ["TFX", "TFB"])], "increases")
    claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")
    assert len(link_of(chain.chain_view(g), "binding")["candidates"]) == 3


def test_expression_chip_and_the_size_of_z_never_rank_a_candidate():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}], z=4.2),
                       inventory_row(2, True, [{"tf": "TFB", "mapping": "own"}], z=160.0)])
    claim(g, [VARIANT], "alters_binding", [tf("TFA")], "increases")
    claim(g, [VARIANT], "alters_binding", [tf("TFB")], "increases")
    occupies = claim(g, [tf("TFB")], "occupies", [ELEMENT], context=HEPG2)
    chip = tool_evidence(g, "occupancy", "ChIP-seq: a TFB peak covers the variant in HepG2.", about_tfs=["TFB"],
                         about_elements=["EH38E0000001"], context=HEPG2)
    g.link(occupies, chip, "supports", INVESTIGATOR, "peak at the variant")
    g.assess(occupies, "supported_in_scope", "ChIP-seq peak", "critic", g.claims[occupies].version)
    expressed = claim(g, [tf("TFB")], "expressed_in", [EntityRef(kind="context", label="HepG2")])
    view = chain.chain_view(g)
    binding = link_of(view, "binding")
    assert [c["label"] for c in binding["candidates"]] == ["TFA", "TFB"]                  # id order, not z or ChIP
    assert binding["tied"] is True and {c["level"] for c in binding["candidates"]} == {1}
    assert [c["id"] for c in candidate(view, "binding", "TFB")["context"]] == [occupies, expressed]
    assert candidate(view, "binding", "TFA")["context"] == []
    assert "context, never ranked" in chain.candidate_text(candidate(view, "binding", "TFB"), "G")
    assert view["unplaced"] == []                                                         # context is not "unplaced"
    assert "z" not in json.dumps(view["links"])


def test_an_experiment_that_compares_no_alleles_gives_no_rung():
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", HEPG2)
    chip = tool_evidence(g, "occupancy", "ChIP-seq: a TFX peak covers the variant in HepG2.", about_tfs=["TFX"],
                         context=HEPG2)
    g.link(cid, chip, "supports", INVESTIGATOR, "a peak, not an allelic difference")
    assert g.claims[cid].evidence_links[0].strength == "indirect"
    cand = candidate(chain.chain_view(g), "binding", "TFX")
    assert cand["rung"] == "none" and [e["id"] for e in cand["claims"][0]["indirect"]] == [chip]
    assert "indirect, no rung" in chain.candidate_text(cand, "G")


def test_contested_counts_as_none_and_contradicted_ranks_below_it():
    view = chain.chain_view(rich_graph())
    activity = link_of(view, "activity")["candidates"][0]
    assert (activity["state"], activity["level"], activity["assessment"]) == ("contested", 0, "contested")
    assert link_of(view, "activity")["rung"] == "none" and link_of(view, "activity")["top"] == []
    genes = {c["label"]: c for c in link_of(view, "gene")["candidates"]}
    assert (genes["GENE1"]["rung"], genes["GENE1"]["level"]) == ("association", 2)
    assert (genes["GENE2"]["state"], genes["GENE2"]["level"]) == ("contradicted", chain.CONTRADICTED_LEVEL)
    assert [c["label"] for c in link_of(view, "gene")["candidates"]] == ["GENE1", "GENE2"]
    rows = {r["key"]: r for r in chain.chain_rows(view, "G")}
    assert rows["gene"]["others"] == "GENE2 (contradicted in scope)"
    assert rows["activity"]["others"].endswith("(contested)")


def test_a_superseded_claim_is_left_out_and_its_replacement_is_read():
    view = chain.chain_view(rich_graph())                 # TFX's binding claim was superseded by TFZ's
    labels = [c["label"] for c in link_of(view, "binding")["candidates"]]
    assert labels == ["TFZ"]


def test_claims_that_are_not_links_of_the_chain_are_listed_never_dropped():
    g = ClaimGraph(dev_case())
    other = claim(g, [EntityRef(kind="variant", label="rs7606173")], "alters_binding", [tf("TFX")], "increases")
    trans = claim(g, [tf("TFX")], "regulates", [gene("GENE1")], "increases")
    loose = claim(g, [VARIANT], "other", [gene("GENE1")])
    location = claim(g, [VARIANT], "overlaps", [ELEMENT])
    view = chain.chain_view(g)
    assert {u["id"]: u["why"] for u in view["unplaced"]} == {
        other: "about another variant",
        trans: "a factor-to-gene link, not a link from the variant or its element",
        loose: "relation other is not a link of the chain"}
    assert view["placed"] == 0 and [c["id"] for c in view["location"]["claims"]] == [location]


def test_an_element_to_gene_claim_is_flagged_when_its_element_is_not_the_variants():
    g = rich_graph()
    view = chain.chain_view(g)
    read = next(r for r in candidate(view, "gene", "GENE1")["claims"] if r["relation"] == "regulates")
    assert "names no variant, and its element is not recorded as containing the variant" in read["flags"]
    call = g.reserve_tool_call_id()
    overlap = Evidence(evidence_class="annotation", observed_result="The variant lies in cCRE EH38E0000001.",
                       independence_group="ccre", origin="tool", about_elements=["EH38E0000001"])
    g.record_tool_call(ToolCall(tool_call_id=call, tool_name="ccre_overlap", execution_status="success",
                                retrieval_status="records_found", requested_by="code", charged_to="code"), [overlap])
    g.add_variant_element("EH38E0000001", call)
    read = next(r for r in candidate(chain.chain_view(g), "gene", "GENE1")["claims"] if r["relation"] == "regulates")
    assert read["flags"] == []


def test_hypotheses_are_ordered_link_by_link_with_ties_and_unordered_pairs():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFP", "mapping": "own"}]),
                       inventory_row(2, True, [{"tf": "TFQ", "mapping": "own"}])])
    measured = binding_assay(g, "TFX")
    predicted_p = claim(g, [VARIANT], "alters_binding", [tf("TFP")], "increases")
    predicted_q = claim(g, [VARIANT], "alters_binding", [tf("TFQ")], "increases")
    expression = eqtl(g, "GENE1")
    hypothesis(g, "TFX with GENE1", [measured, expression], mechanism_class="tf_binding")      # H1: assay + eQTL
    hypothesis(g, "TFX alone", [measured], mechanism_class="tf_binding")                       # H2: assay
    hypothesis(g, "TFP predicted", [predicted_p], mechanism_class="tf_binding")                # H3: prediction
    hypothesis(g, "TFQ predicted", [predicted_q], mechanism_class="tf_binding")                # H4: prediction
    hypothesis(g, "GENE1 alone", [expression], mechanism_class="association_only")             # H5: eQTL
    order = chain.chain_view(g)["order"]
    assert order["tiers"] == [["H1"], ["H2", "H5"], ["H3", "H4"]]
    assert order["ties"] == [["H3", "H4"]]
    above = {(p["upper"], p["lower"]): p["stronger_at"] for p in order["above"]}
    assert above[("H1", "H2")] == ["gene"] and above[("H1", "H5")] == ["binding"]
    assert above[("H2", "H3")] == ["binding"] and ("H2", "H5") not in above and ("H5", "H2") not in above
    assert ("H5", "H3") not in above and ("H3", "H5") not in above                   # each is stronger somewhere
    assert order["parts_of_one_route"] is False
    assert order["text"][0].startswith("Nothing ranks above H1. Ranked below at least one of them: H2, H5.")
    assert order["text"][-1] == "Tied (the same kind of evidence on every link): H3 = H4."


def test_rejected_hypotheses_are_not_compared_and_deferred_ones_are():
    view = chain.chain_view(rich_graph())
    assert [(h["id"], h["disposition"]) for h in view["hypotheses"]] == [
        ("H2", "leading"), ("H3", "deferred"), ("H4", "active")]


def test_hypotheses_with_no_evidence_are_not_called_a_tie():
    g = ClaimGraph(dev_case())
    hypothesis(g, "TFX", [claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")])
    hypothesis(g, "TFY", [claim(g, [VARIANT], "alters_binding", [tf("TFY")], "increases")])
    assert chain.chain_view(g)["order"]["text"] == [
        "No open hypothesis has supporting evidence on any link, so there is nothing to order."]


def test_both_reports_show_the_chain_and_an_evidence_bundle_shows_none(tmp_path):
    g = fragments()
    g.set_result(RunResult(outcome="multiple_explanations", stop_reason="converged"), "code")
    run = write_run(g, tmp_path / "run")
    loaded = bundle.load_bundle(run)
    data = report.report_data(loaded)
    assert data["chain"] == chain.for_report(chain.chain_view(g))        # the ranked rows a report lists
    for rendered in (report.render_html(loaded), report.render_markdown(loaded)):
        assert "Mechanism chain" in rendered
        assert "TF binding: allele-resolved assay (TFX)" in rendered
        assert "Gene to trait: no claim proposes this link." in rendered
        assert "parts of one route, not as rivals" in rendered
        assert "Multiple explanations" in rendered                    # the comparison's own outcome is still shown
    assert g.result.outcome == "multiple_explanations"
    empty = ClaimGraph(dev_case())
    inventory_call(empty, [inventory_row(1, True)])
    bare = bundle.load_bundle(write_run(empty, tmp_path / "evidence"))
    assert "Mechanism chain" not in report.render_html(bare) + report.render_markdown(bare)


def test_report_text_from_the_graph_cannot_become_markup(tmp_path):
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "alters_regulatory_activity", [EntityRef(kind="element", label="<img src=x>|construct")],
                "increases", HEPG2)
    eid = tool_evidence(g, "reporter_assay", "Luciferase: the G construct is more active.", allele="G",
                        direction="increases", about_variants=["rs1427407"], context=HEPG2,
                        about_elements=["<img src=x>|construct"])
    g.link(cid, eid, "supports", INVESTIGATOR, "more active")
    loaded = bundle.load_bundle(write_run(g, tmp_path / "run"))
    html, md = report.render_html(loaded), report.render_markdown(loaded)
    assert "<img src=x>" not in html and "&lt;img src=x&gt;" in html
    assert "<img src=x>" not in md and "\\|construct" in md
