"""Evidence can change the candidate mechanisms without refuting the old ones.

All invented factors/observations below are fixtures. The end-to-end tests exercise the real engine and graph with
scripted role outputs; they prove the contract, not that a language model will choose these actions reliably.
"""

import copy
import json

import pytest

from variant2mechanism.agent.schemas import SchemaCheckError
from variant2mechanism.v9 import adoption, report, roles
from variant2mechanism.v9.fixtures import Fixture, load_fixture
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, HypothesisDraft
from variant2mechanism.v9.investigate import Engine, EngineLimits, _Run
from variant2mechanism.v9.schemas import ContextScope, Evidence, ToolCall
from variant2mechanism.v9.tools import ToolBudget

from .test_engine_support import run_fixture


def empty_plan(**changes):
    return {"hypothesis_updates": [], "new_hypotheses": [], "inferred_candidates": [], "evidence_decisions": [],
            "assessments": [], "questions": [], "stop": {"stop": True, "reason": "no useful lookup remains"},
            **changes}


def observation_graph():
    fixture = load_fixture("controlled_wrong_tf")
    g = ClaimGraph(fixture.case)
    old = g.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label="V3")], relation="alters_binding",
                                objects=[EntityRef(kind="tf", label="TFA")], direction="increases"), "coordinator")
    g.add_hypothesis(HypothesisDraft(title="Old candidate", required_claim_ids=[old]), "coordinator")
    g.log("propose", "coordinator", "initial candidate")
    tid = g.reserve_tool_call_id()
    ev = Evidence(evidence_class="occupancy", source_ids=["SYN-NEW"], observed_result="TFB allele-specific occupancy",
                  about_tfs=["TFB"], about_variants=["SYN:3"], allele="A", direction="increases",
                  independence_group="SYN-NEW", origin="fixture", data={"allele_specific": True},
                  context=ContextScope(label="context Z", biosample="context Z", species="human", source="evidence"))
    g.record_tool_call(ToolCall(tool_call_id=tid, tool_name="fixture", execution_status="success",
                               retrieval_status="records_found", requested_by="computational_investigator"), [ev])
    return g


def decision(disposition="defer", **changes):
    return {"evidence_ids": ["E1"], "disposition": disposition, "claim_refs": [], "reason": "lower priority",
            "revisit_trigger": "an active investigation finishes", **changes}


def test_new_observation_cannot_disappear_without_a_decision():
    g = observation_graph()
    assert adoption.pending(g) == [["E1"]]
    with pytest.raises(SchemaCheckError, match="needs an evidence decision"):
        roles.plan_check(g, {})(roles.V9Plan.model_validate(empty_plan()))
    plan = roles.V9Plan.model_validate(empty_plan(evidence_decisions=[decision()]))
    roles.plan_check(g, {})(plan)
    Engine.__new__(Engine)._review_evidence(_Run(g, 0), plan.evidence_decisions, {})
    assert adoption.pending(g) == []
    assert "lower priority" in " ".join(adoption.context_lines(g))
    assert g.claims["C1"].assessment == "unassessed"   # deferral is not biological rejection


def test_prose_revision_cannot_claim_to_represent_an_observation():
    g = observation_graph()
    d = roles.V9EvidenceDecision.model_validate(decision("represented", claim_refs=["C1"]))
    Engine.__new__(Engine)._review_evidence(_Run(g, 0), [d], {})
    assert adoption.pending(g) == [["E1"]]
    assert g.events[-1].action == "refuse_update"
    assert "summary edit" in g.events[-1].concise_reason


def test_old_unlinked_observation_survives_in_plan_audit_and_report():
    g = observation_graph()
    budget = roles.PacketBudget(model_used=4, model_cap=24, model_reserve=2,
        tools=ToolBudget(tool_calls_used=1, tool_calls_left=23, code_tool_calls=0,
                         fulltext_used=0, fulltext_left=8, fulltext_soft_reached=False),
        fulltext_soft=5, fulltext_hard=8, regenerations_used=0, max_regenerations=1)
    ctx = roles.PacketContext(specs={}, budget=budget)
    # No recent event includes this evidence, and no hypothesis links to it.
    for packet in (roles.plan_packet(g, ctx, round_no=3, since_event=len(g.events)),
                   roles.audit_packet(g, ctx, round_no=3, audited=["H1"]),
                   roles.final_packet(g, ctx, profiles={}, critique=None, stale=[], round_no=3)):
        assert "E1: observation awaiting adoption" in packet
        assert g.evidence["E1"].observed_result in packet
    gaps = report._gaps(g, {"C1": {"status": "unresolved", "status_label": "Unresolved"}})
    assert any(gap["kind"] == "unadopted_observation" and gap["ids"] == ["E1"] for gap in gaps)


@pytest.mark.parametrize("change", [
    {"disposition": "defer", "revisit_trigger": None},
    {"disposition": "represented", "claim_refs": []},
    {"evidence_ids": ["E999"]},
    {"reason": ""},
])
def test_evidence_decisions_are_auditable(change):
    g = observation_graph()
    with pytest.raises(SchemaCheckError):
        roles.plan_check(g, {})(roles.V9Plan.model_validate(empty_plan(evidence_decisions=[decision(**change)])))


def test_unrelated_observation_can_be_set_aside_without_creating_a_claim():
    g = observation_graph()
    g.evidence["E1"].about_variants = ["SYN:999"]
    d = roles.V9EvidenceDecision.model_validate(decision("set_aside", reason="The assay tests another variant.",
                                                       revisit_trigger=None))
    Engine.__new__(Engine)._review_evidence(_Run(g, 0), [d], {})
    assert not adoption.pending(g)
    assert len(g.claims) == 1 and len(g.hypotheses) == 1


def test_old_plan_scripts_still_load_but_live_schema_requires_adoption_fields():
    old = {k: v for k, v in empty_plan().items()
           if k not in {"new_hypotheses", "inferred_candidates", "evidence_decisions"}}
    assert roles.V9Plan.model_validate(old)._legacy_adoption
    with pytest.raises(SchemaCheckError, match="pre-adoption scripts"):
        roles.plan_check(observation_graph(), {})(roles.V9Plan.model_validate(old))
    roles.plan_check(observation_graph(), {}, allow_legacy=True)(roles.V9Plan.model_validate(old))
    assert {"new_hypotheses", "inferred_candidates", "evidence_decisions"} <= set(
        roles.V9Plan.model_json_schema()["required"])


def discovery_fixture(old_tf="TFA", new_tf="TFB", direction="increases", *, defer_old=False):
    raw = load_fixture("controlled_wrong_tf").model_dump(mode="json")
    # Names are varied deliberately: this must be a general revision operation, not a recognised biology example.
    raw = json.loads(json.dumps(raw).replace("TFA", old_tf).replace("TFB", new_tf))
    scripts = raw["roles"]
    evidence = raw["tools"]["syn_binding_assay"]["responses"][0]["evidence"][0]
    evidence["direction"] = direction
    evidence["observed_result"] = f"Stipulated assay: {new_tf} binding {direction} for allele A."
    original = scripts["coordinator"][0]["hypotheses"][0]
    sketch = copy.deepcopy(original)
    sketch.update(key="new_factor", title=f"Observed {new_tf} binding", summary="A partial molecular explanation.",
                  reason_kind="literature_report", reason_detail="A newly returned allele-comparative observation.",
                  member_alternatives=[], missing_links=["TF binding mediation of element activity remains untested."])
    binding = copy.deepcopy(sketch["claims"][0])
    binding.update(key="new_binding", direction=direction, assertion_text=f"Allele A {direction} {new_tf} binding.")
    binding["objects"][0]["label"] = new_tf
    binding["initial_links"] = [{"evidence_id": "E4", "stance": "supports", "applicability": None,
                                  "rationale": "The assay directly measures this factor and allele.",
                                  "suggested_assessment": "supported_in_scope"}]
    sketch["claims"] = [binding]
    sketch["reuse_claims"] = [{"ref": "C2", "required": False}, {"ref": "C3", "required": False}]
    # The investigator reports the observation, without withdrawing the old candidate or moving its evidence.
    answer = scripts["computational_investigator"][1]["answers"][0]
    answer["proposed_updates"] = []
    answer["answer_summary"] = "The experiment concerns a different factor; consider a separate claim."
    plan = empty_plan(new_hypotheses=[{"sketch": sketch, "basis_evidence_ids": ["E4"]}],
                      evidence_decisions=[{"evidence_ids": ["E4"], "disposition": "represented",
                                           "claim_refs": ["new_binding"], "reason": "New factor represented explicitly.",
                                           "revisit_trigger": None}])
    if defer_old:
        plan["hypothesis_updates"] = [{"hypothesis_id": "H1", "action": "defer", "reason": "Prioritise new assay.",
                                       "claim_id": None, "new_claim": None, "new_claim_id": None, "required": False,
                                       "revisit_trigger": "new branch stalls or evidence addresses the old factor",
                                       "revision": None}]
    scripts["coordinator"][2] = plan
    scripts["critic"][0].update(reportable_ids=["H1", "H2"] if not defer_old else ["H2"], consequential=False)
    scripts["critic"][1] = {"comparisons": [], "outcome": {"category": "no_supported_explanation",
        "leading_ids": [], "summary": "Molecular observations do not establish downstream mediation.",
        "weakest_links": [], "next_experiments": []}}
    return Fixture.model_validate(raw)


@pytest.mark.parametrize("old,new,direction", [("TFA", "TFB", "increases"), ("FACTORX", "FACTORY", "decreases")])
def test_new_branch_while_old_hypothesis_remains_viable(v9_cfg, tmp_path, old, new, direction):
    result, scripted, _ = run_fixture(v9_cfg, discovery_fixture(old, new, direction), tmp_path)
    g = result.graph
    assert result.metrics["engine_error"] is None
    assert result.metrics["regenerations"] == 0
    assert len(g.hypotheses) == 2 and g.hypotheses["H2"].origin == "evidence_led"
    assert g.hypotheses["H1"].disposition not in ("rejected", "superseded")
    assert not g.claims["C1"].superseded_by and g.claims["C1"].assessment != "contradicted_in_scope"
    assert g.claims["C2"].assessment == "supported_in_scope" and g.claims["C2"].evidence_links[0].evidence_id == "E3"
    c = g.claims[g.hypotheses["H2"].required_claim_ids[0]]
    assert g.entities[c.object_ids[0]].label == new and c.direction == direction
    assert c.assessment == "supported_in_scope" and [link.evidence_id for link in c.evidence_links] == ["E4"]
    assert "C2" in g.hypotheses["H2"].claim_ids  # reuse valid independent observation
    assert "C2" not in g.hypotheses["H2"].required_claim_ids
    assert any(e.action == "review_evidence" for e in g.events)
    assert any(e.details.get("basis_evidence_ids") == {"new_factor": ["E4"]} for e in g.events)
    assert scripted.titles().count("V9Propose") == 1
    engine = Engine.__new__(Engine)
    engine.limits = EngineLimits(max_additional_hypotheses=1)
    assert engine._discovery_capacity(_Run(g, 0)) == 0  # rejected/deferred branches still consume the run cap


@pytest.mark.parametrize("defer_old", [False, True])
def test_active_slots_are_bounded_and_deferral_is_not_rejection(v9_cfg, tmp_path, defer_old):
    result, _, _ = run_fixture(v9_cfg, discovery_fixture(defer_old=defer_old), tmp_path,
                              limits=EngineLimits(max_active=1))
    g = result.graph
    assert result.metrics["engine_error"] is None
    assert sum(h.disposition == "active" for h in g.hypotheses.values()) <= 1
    assert g.hypotheses["H1" if defer_old else "H2"].disposition == "deferred"
    assert all(h.disposition != "rejected" for h in g.hypotheses.values())


def test_discovery_limits_and_unknown_basis_are_checked(v9_cfg, tmp_path):
    fixture = discovery_fixture()
    g = observation_graph()
    plan = roles.V9Plan.model_validate(fixture.roles["coordinator"][2])
    with pytest.raises(SchemaCheckError, match="at most 0"):
        roles.plan_check(g, {}, max_new=0)(plan)
    with pytest.raises(SchemaCheckError, match="unknown evidence E4"):
        roles.plan_check(g, {})(plan)


def test_discovery_cannot_just_name_evidence_without_using_it():
    g = observation_graph()
    raw = discovery_fixture().roles["coordinator"][2]
    raw["new_hypotheses"][0]["basis_evidence_ids"] = ["E1"]
    raw["new_hypotheses"][0]["sketch"]["claims"][0]["initial_links"] = []
    with pytest.raises(SchemaCheckError, match="at least one basis evidence must be linked"):
        roles.plan_check(g, {})(roles.V9Plan.model_validate(raw))


def test_questions_can_target_the_branch_created_in_the_same_plan(v9_cfg, tmp_path):
    fixture = discovery_fixture()
    question = copy.deepcopy(fixture.roles["coordinator"][0]["questions"][0])
    question.update(text="Investigate the new branch", target_claims=["new_binding"], hypotheses=["new_factor"])
    fixture.roles["coordinator"][2]["questions"] = [question]
    result, _, _ = run_fixture(v9_cfg, fixture, tmp_path)
    assert result.metrics["engine_error"] is None
    question = next(q for q in result.graph.questions.values() if q.text == "Investigate the new branch")
    assert question.hypothesis_ids == ["H2"]
    assert question.target_claim_ids == result.graph.hypotheses["H2"].required_claim_ids


@pytest.mark.data
def test_saved_observations_are_still_visible_after_their_first_round():
    from variant2mechanism.config import REPO

    p = REPO / "runs/dev_v9_release/dev1_rs1427407/graph.json"
    if not p.exists():
        pytest.skip("saved diagnostic run is not distributed")
    g = ClaimGraph.from_json(p.read_text())
    grouped = [ids for ids in adoption.pending(g) if "E338" in ids]
    assert grouped == [["E338", "E339", "E344"]]  # same source passage, not three discoveries
    assert g.evidence["E338"].about_tfs == ["GATA1", "TAL1"]
    assert not adoption.represented_by(g, "E344")  # a context-only link is not an adopted binding claim
