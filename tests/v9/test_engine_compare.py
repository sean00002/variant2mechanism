"""compare.py: profiles, validation of the critic's comparisons, and decide() checks that only ever weaken and never
name a hypothesis the critic did not name.

Graphs are built through the graph API on the development variant rs1427407 (chr2:60490908 T>G); TF and gene
symbols and the observations are stipulated for the test, not claims about that variant.
"""

from typing import get_args

import pytest

from variant2mechanism.v9 import compare
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, HypothesisDraft
from variant2mechanism.v9.roles import V9Comparison, V9Final, V9NextExperiment, V9Outcome, V9WeakLink
from variant2mechanism.v9.schemas import Case, ContextScope, Evidence, Outcome, ToolCall, Variant

VARIANT = EntityRef(kind="variant", label="rs1427407")
ELEMENT = EntityRef(kind="element", label="enhancer", canonical_id="EH38E0000001")
HEPG2 = ContextScope(label="HepG2", source="supplied")


def evidence(g: ClaimGraph, cls: str, text: str, **kw) -> str:
    tid = g.reserve_tool_call_id()
    call = ToolCall(tool_call_id=tid, tool_name="test_tool", execution_status="success",
                    retrieval_status="records_found", requested_by="computational_investigator", charged_to="agent")
    ev = Evidence(evidence_class=cls, observed_result=text, independence_group=text, origin="tool", **kw)
    return g.record_tool_call(call, [ev]).evidence_ids[0]


def claim(g: ClaimGraph, subjects, relation, objects, direction="increases", context=HEPG2) -> str:
    return g.add_claim(ClaimDraft(subjects=subjects, relation=relation, objects=objects, direction=direction,
                                  context=context), "coordinator")


def supported(g: ClaimGraph, cid: str, cls: str, text: str, **kw) -> str:
    eid = evidence(g, cls, text, context=HEPG2, **kw)
    g.link(cid, eid, "supports", "computational_investigator", text)
    g.assess(cid, "supported_in_scope", text, "critic", g.claims[cid].version)
    return eid


def binding(g: ClaimGraph, tf: str) -> str:
    cid = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label=tf)])
    supported(g, cid, "binding_assay", f"{tf} binds G more in an allelic assay", about_tfs=[tf], allele="G",
              direction="increases", about_variants=["rs1427407"])
    return cid


def regulates(g: ClaimGraph, gene: str, direction="increases") -> str:
    return claim(g, [ELEMENT], "regulates", [EntityRef(kind="gene", label=gene)], direction)


def hypothesis(g: ClaimGraph, required, title: str) -> str:
    return g.add_hypothesis(HypothesisDraft(title=title, required_claim_ids=list(required),
                                            mechanism_class="tf_binding"), "coordinator")


def final(category: str, leading: list[str], comparisons=()) -> V9Final:
    return V9Final(comparisons=[V9Comparison(**c) for c in comparisons],
                   outcome=V9Outcome(category=category, leading_ids=leading, summary="critic summary",
                                     weakest_links=[], next_experiments=[]))


@pytest.fixture
def g() -> ClaimGraph:
    """H1: TFX binding (supported) + element regulates GENE1 (unresolved); H2: TFY binding (supported)."""
    graph = ClaimGraph(Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G",
                                                             rsid="rs1427407")))
    hypothesis(graph, [binding(graph, "TFX"), regulates(graph, "GENE1")], "TFX raises GENE1")
    hypothesis(graph, [binding(graph, "TFY")], "TFY binds")
    return graph


def test_profile_lays_out_evidence_without_a_score(g):
    p = compare.profile(g, "H1")
    by_id = {c["claim_id"]: c for c in p["claims"]}
    assert by_id["C1"]["display"] == "supported" and by_id["C1"]["basis"] == "binding_assay"
    assert by_id["C1"]["independent_support"] == 1 and by_id["C1"]["applicability"] == ["exact"]
    assert p["critical_gaps"] == ["C2"] and p["supported_beyond_annotation"] is True
    assert p["shared"] == {"H2": []} and p["divergent"] == {"H2": ["C1", "C2"]}
    assert not any(k in p for k in ("score", "probability", "rank"))


def test_leading_becomes_partial_while_a_bridge_is_unresolved(g):
    comparisons = [{"a": "H1", "b": "H2", "outcome": "A_preferred", "decisive_claim_ids": ["C2"],
                    "decisive_gaps": [], "reason": "H1 links binding to a gene"}]
    r = compare.decide(g, final("leading_explanation", ["H1"], comparisons), stop_reason="converged",
                       budget_stop=False)
    assert r.outcome == "partial_mechanism" and r.downgraded_from == "leading_explanation"
    assert "C2" in r.downgrade_reason and r.leading_ids == ["H1"]
    assert [w.claim_id for w in r.weakest_links] == ["C2"]                  # every unresolved required claim
    assert g.hypotheses["H1"].disposition == "leading"
    assert next(e for e in g.events if e.details.get("to") == "leading").role == "code"
    assert g.comparisons["P1"].accepted


def test_a_leader_must_be_preferred_over_every_supported_rival(g):
    r = compare.decide(g, final("partial_mechanism", ["H1"]), stop_reason="converged", budget_stop=False)
    assert r.outcome == "multiple_explanations" and r.leading_ids == ["H1", "H2"]
    assert {g.hypotheses[h].disposition for h in ("H1", "H2")} == {"tied"}
    assert "not preferred over H2" in r.downgrade_reason


def test_leading_is_never_a_hypothesis_with_a_contradicted_required_claim(g):
    bad = regulates(g, "GENE2", "decreases")
    h3 = hypothesis(g, [bad], "TFZ represses GENE2")
    up = evidence(g, "perturbation", "activating the element raises GENE2", about_genes=["GENE2"],
                  about_elements=["EH38E0000001"], direction="increases", context=HEPG2)
    g.link(bad, up, "contradicts", "computational_investigator", "matched test")
    g.assess(bad, "contradicted_in_scope", "opposite sign", "critic", g.claims[bad].version)
    assert g.hypotheses[h3].disposition == "rejected"
    comparisons = [{"a": h3, "b": "H1", "outcome": "A_preferred", "decisive_claim_ids": [bad], "decisive_gaps": [],
                    "reason": "preferred anyway"}]
    refused = compare.validate(g, final("leading_explanation", [h3], comparisons))[0]
    assert not refused.accepted and "cannot be preferred" in refused.refusal_reason
    r = compare.decide(g, final("leading_explanation", [h3], comparisons), stop_reason="converged",
                       budget_stop=False)
    assert h3 not in r.leading_ids and r.outcome != "leading_explanation"
    assert r.downgraded_from == "leading_explanation" and g.hypotheses[h3].disposition == "rejected"
    stored = next(p for p in g.comparisons.values() if p.a == h3)
    assert not stored.accepted


def test_decisive_claims_must_belong_to_the_pair(g):
    stray = regulates(g, "GENE3")
    comparisons = [{"a": "H1", "b": "H2", "outcome": "tied", "decisive_claim_ids": [stray], "decisive_gaps": [],
                    "reason": "x"}]
    out = compare.validate(g, final("multiple_explanations", ["H1", "H2"], comparisons))
    assert not out[0].accepted and "belong to neither" in out[0].refusal_reason


def test_fallback_without_a_final_comparison_names_no_hypothesis(g):
    """Leading and tied come only from a comparison: the graph alone sets a category and lists the candidates."""
    two_graph = ClaimGraph.from_json(g.to_json())
    two = compare.decide(two_graph, None, stop_reason="wall_time", budget_stop=True,
                         note="no final comparison: wall_time")
    assert two.outcome == "multiple_explanations" and two.budget_stop and two.leading_ids == []
    assert {h.disposition for h in two_graph.hypotheses.values()} == {"active"}
    assert "graph alone" in two.summary and "H1" in two.summary and "H2" in two.summary
    assert two.downgraded_from is None and [w.claim_id for w in two.weakest_links] == ["C2"]
    one = ClaimGraph.from_json(g.to_json())
    one.set_disposition("H2", "deferred", "budget", "coordinator", revisit_trigger="more budget")
    r = compare.decide(one, None, stop_reason="budget_model_calls", budget_stop=True)
    assert r.outcome == "partial_mechanism" and r.leading_ids == [] and r.next_experiments == []
    assert one.hypotheses["H1"].disposition == "active"


def test_a_graph_with_no_hypothesis_or_an_engine_error_reports_no_scientific_outcome(g):
    empty = ClaimGraph(g.case)
    r = compare.decide(empty, None, stop_reason="regeneration_limit", budget_stop=False)
    assert r.outcome == "input_or_capability_limitation" and r.leading_ids == []
    for stop in ("engine_error", "cache_miss"):
        graph = ClaimGraph.from_json(g.to_json())
        r = compare.decide(graph, None, stop_reason=stop, budget_stop=False, note=f"{stop}: test")
        assert r.outcome == "input_or_capability_limitation" and r.leading_ids == [] and stop in r.summary
        assert {h.disposition for h in graph.hypotheses.values()} == {"active"}


def test_leading_needs_every_molecular_claim_settled():
    """A predicted-only binding claim plus a supported GWAS association is not an explanation, whatever the critic
    prefers (review finding: the critic's leader kept leading_explanation)."""
    g = ClaimGraph(Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G",
                                                         rsid="rs1427407")))
    bind = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label="TFX")], context=None)
    pred = evidence(g, "prediction", "group model: G binds more", about_tfs=["TFX"], allele="G", direction="increases",
                    about_variants=["rs1427407"])
    g.link(bind, pred, "supports", "computational_investigator", "group prediction")
    trait = claim(g, [VARIANT], "associated_with_trait", [EntityRef(kind="phenotype", label="trait T")],
                  context=None)
    gwas = evidence(g, "association", "GWAS: G associated with higher trait T", about_traits=["trait T"], allele="G",
                    direction="increases")
    g.link(trait, gwas, "supports", "computational_investigator", "GWAS row")
    g.assess(trait, "supported_in_scope", "GWAS", "critic", g.claims[trait].version)
    h1 = hypothesis(g, [bind, trait], "TFX binding explains trait T")
    hypothesis(g, [binding(g, "TFY")], "TFY binds")
    comparisons = [{"a": h1, "b": "H2", "outcome": "A_preferred", "decisive_claim_ids": [trait], "decisive_gaps": [],
                    "reason": "H1 reaches the trait"}]
    r = compare.decide(g, final("leading_explanation", [h1], comparisons), stop_reason="converged",
                       budget_stop=False)
    assert r.outcome != "leading_explanation" and h1 not in r.leading_ids and r.leading_ids == []
    assert r.downgraded_from == "leading_explanation" and bind in r.downgrade_reason
    assert g.hypotheses[h1].disposition == "active"


def test_a_withdrawn_required_claim_cannot_lead(g):
    """An investigator superseded H1's TF claim and the coordinator never swapped the replacement in: H1's path is
    broken, so H1 cannot lead."""
    new = g.supersede_claim("C1", ClaimDraft(subjects=[VARIANT], relation="alters_binding",
                                             objects=[EntityRef(kind="tf", label="TFB")], direction="increases",
                                             context=HEPG2), "the assay was for TFB", "computational_investigator")
    g.propagate()
    assert g.hypotheses["H1"].path_status["C1"] == "superseded" and g.claims[new].superseded_by is None
    comparisons = [{"a": "H1", "b": "H2", "outcome": "A_preferred", "decisive_claim_ids": ["C2"],
                    "decisive_gaps": [], "reason": "H1 links binding to a gene"}]
    r = compare.decide(g, final("leading_explanation", ["H1"], comparisons), stop_reason="converged",
                       budget_stop=False)
    assert "H1" not in r.leading_ids and r.outcome != "leading_explanation"
    assert g.hypotheses["H1"].disposition == "active" and "C1" in r.downgrade_reason


def test_partial_needs_the_molecular_claims_settled():
    """A supported element-to-gene bridge with an unresolved binding claim is not a partial mechanism."""
    g = ClaimGraph(Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G",
                                                         rsid="rs1427407")))
    bind = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label="TFX")])
    reg = regulates(g, "GENE1")
    supported(g, reg, "perturbation", "activating the enhancer raises GENE1", about_genes=["GENE1"],
              about_elements=["EH38E0000001"], direction="increases")
    h1 = hypothesis(g, [bind, reg], "TFX raises GENE1")
    r = compare.decide(g, final("partial_mechanism", [h1]), stop_reason="converged", budget_stop=False)
    assert r.outcome == "no_supported_explanation" and r.leading_ids == []
    assert r.downgraded_from == "partial_mechanism" and bind in r.downgrade_reason
    assert g.hypotheses[h1].disposition == "active"


def test_a_tie_keeps_an_untested_member_and_never_becomes_a_lead():
    """Missing data never separates hypotheses: an unresolved member of the critic's tie stays in it."""
    g = ClaimGraph(Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G",
                                                         rsid="rs1427407")))
    hypothesis(g, [binding(g, "TFX")], "TFX binds")
    hypothesis(g, [regulates(g, "GENE9")], "the element raises GENE9 (never investigated)")
    r = compare.decide(g, final("multiple_explanations", ["H1", "H2"]), stop_reason="converged", budget_stop=False)
    assert r.outcome == "multiple_explanations" and r.leading_ids == ["H1", "H2"]
    assert {h: x.disposition for h, x in g.hypotheses.items()} == {"H1": "tied", "H2": "tied"}
    assert r.downgraded_from is None


def test_code_never_puts_another_leader_in_place_of_the_critics():
    """The critic names an unsupported H2 as leading: code drops the lead and names nobody, never H1."""
    g = ClaimGraph(Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G",
                                                         rsid="rs1427407")))
    hypothesis(g, [binding(g, "TFX")], "TFX binds")
    hypothesis(g, [regulates(g, "GENE9")], "the element raises GENE9 (never investigated)")
    r = compare.decide(g, final("leading_explanation", ["H2"]), stop_reason="converged", budget_stop=False)
    assert r.leading_ids == [] and r.outcome == "multiple_explanations"
    assert {h.disposition for h in g.hypotheses.values()} == {"active"}
    assert r.downgraded_from == "leading_explanation" and "H2 has no required claim supported" in r.downgrade_reason


def test_an_uncompared_untested_rival_turns_a_lead_into_a_tie():
    g = ClaimGraph(Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G",
                                                         rsid="rs1427407")))
    hypothesis(g, [binding(g, "TFX")], "TFX binds")
    hypothesis(g, [regulates(g, "GENE9")], "the element raises GENE9 (never investigated)")
    r = compare.decide(g, final("leading_explanation", ["H1"]), stop_reason="converged", budget_stop=False)
    assert r.outcome == "multiple_explanations" and r.leading_ids == ["H1", "H2"]
    preferred = ClaimGraph.from_json(g.to_json())
    for h in preferred.hypotheses.values():
        assert h.disposition == "tied"
    fresh = ClaimGraph(g.case)
    hypothesis(fresh, [binding(fresh, "TFX")], "TFX binds")
    hypothesis(fresh, [regulates(fresh, "GENE9")], "the element raises GENE9 (never investigated)")
    comparisons = [{"a": "H1", "b": "H2", "outcome": "A_preferred", "decisive_claim_ids": ["C1"],
                    "decisive_gaps": ["C2 untested"], "reason": "only H1's divergent claim is supported"}]
    led = compare.decide(fresh, final("leading_explanation", ["H1"], comparisons), stop_reason="converged",
                         budget_stop=False)
    assert led.outcome == "leading_explanation" and led.leading_ids == ["H1"]
    assert fresh.hypotheses["H1"].disposition == "leading" and fresh.hypotheses["H2"].disposition == "active"


def test_a_preference_needs_a_divergent_decisive_claim(g):
    shared = hypothesis(g, ["C1", "C3"], "TFX and TFY both bind")
    for decisive in ([], ["C1"]):
        comparison = {"a": "H1", "b": shared, "outcome": "A_preferred", "decisive_claim_ids": decisive,
                      "decisive_gaps": [], "reason": "preferred"}
        out = compare.validate(g, final("leading_explanation", ["H1"], [comparison]))[0]
        assert not out.accepted and "only one of" in out.refusal_reason
    divergent = {"a": "H1", "b": shared, "outcome": "A_preferred", "decisive_claim_ids": ["C2"],
                 "decisive_gaps": [], "reason": "H1 links binding to a gene"}
    assert compare.validate(g, final("leading_explanation", ["H1"], [divergent]))[0].accepted


def test_a_rejection_whose_contradiction_no_longer_stands_is_disclosed(g):
    bad = regulates(g, "GENE2", "decreases")
    h3 = hypothesis(g, [bad], "the element represses GENE2")
    up = evidence(g, "perturbation", "activating the element raises GENE2", about_genes=["GENE2"],
                  about_elements=["EH38E0000001"], direction="increases", context=HEPG2)
    g.link(bad, up, "contradicts", "computational_investigator", "matched test")
    g.assess(bad, "contradicted_in_scope", "opposite sign", "critic", g.claims[bad].version)
    assert g.hypotheses[h3].disposition == "rejected" and compare.stale_rejections(g) == []
    g.link(bad, up, "context_only", "critic", "critic passage check: misread")         # the contradiction is withdrawn
    assert g.claims[bad].assessment == "unresolved" and compare.stale_rejections(g) == [h3]
    r = compare.decide(g, None, stop_reason="converged", budget_stop=False)
    assert f"no longer stand: {h3}" in r.summary


def test_decide_never_upgrades_the_critics_outcome(g):
    for category in get_args(Outcome):
        graph = ClaimGraph.from_json(g.to_json())
        r = compare.decide(graph, final(category, ["H1"]), stop_reason="converged", budget_stop=False)
        assert compare.STRENGTH[r.outcome] <= compare.STRENGTH[category], (category, r.outcome)


def test_weakest_links_and_next_experiments_keep_only_known_ids(g):
    out = V9Final(comparisons=[], outcome=V9Outcome(
        category="no_supported_explanation", leading_ids=[], summary="s",
        weakest_links=[V9WeakLink(hypothesis_id="H1", claim_id="C2", why="untested")],
        next_experiments=[V9NextExperiment(text="perturb the element", distinguishes=["H1", "H2"],
                                           claim_ids=["C2"])]))
    r = compare.decide(g, out, stop_reason="converged", budget_stop=False)
    assert [(w.hypothesis_id, w.claim_id) for w in r.weakest_links] == [("H1", "C2")]
    assert r.next_experiments[0].performed is False and r.next_experiments[0].distinguishes == ["H1", "H2"]
