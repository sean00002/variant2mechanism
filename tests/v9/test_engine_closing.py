"""The closing steps (SPEC 6 step 8): the audit may reopen the investigation once (a regeneration when no active
hypothesis is reportable, or one more round for consequential challenges that request actions); before a
regeneration the non-reportable hypotheses give up their active slots, and they come back when the regeneration adds
nothing; a misread passage can no longer support a claim, and a rejection that rested on it is reinstated as deferred
by code, once (CORE-CHANGES-3 C3-5), or disclosed when the graph keeps it; the critic's activation flags reach later
packets; the engine's default symbol resolver and group registry come from the config.
"""

import copy

import pytest

from variant2mechanism.v9.fixtures import FixtureToolRunner, load_fixture
from variant2mechanism.v9.graph import ClaimGraph, GraphRefusal
from variant2mechanism.v9.investigate import Engine, EngineLimits, fixture_facts
from variant2mechanism.v9.roles import RoleCaller

from .test_engine_support import Scripted, events, run_fixture

OCCUPANCY = load_fixture("controlled_remove_occupancy").roles
WRONG_TF = load_fixture("controlled_wrong_tf").roles
SYNTHETIC = load_fixture("synthetic_repair").roles


def audit(reportable, challenges=(), passage_checks=(), consequential=False) -> dict:
    return {"challenges": list(challenges), "passage_checks": list(passage_checks), "activation_flags": [],
            "reportable_ids": list(reportable), "consequential": consequential}


def stop_plan(reason: str) -> dict:
    return {"hypothesis_updates": [], "assessments": [], "questions": [], "stop": {"stop": True, "reason": reason}}


def test_no_reportable_hypothesis_triggers_one_regeneration_then_a_second_audit(v9_cfg, tmp_path):
    regeneration = {**OCCUPANCY["coordinator"][0], "questions": [], "hypotheses": [{
        **OCCUPANCY["coordinator"][0]["hypotheses"][0], "key": "h_regulatory", "mechanism_class": "regulatory",
        "title": "TFA binding changes the activity of element E2", "reason_kind": "distinct_mechanism",
        "reason_detail": "a regulatory reading of the same binding change, not yet investigated",
        "claims": [], "reuse_claims": [{"ref": "C1", "required": True}]}]}
    scripts = {"coordinator": [*OCCUPANCY["coordinator"], regeneration, stop_plan("nothing left to test")],
               "computational_investigator": OCCUPANCY["computational_investigator"],
               "critic": [audit([]), audit(["H1", "H2", "H3"]), OCCUPANCY["critic"][1]]}
    result, scripted, _ = run_fixture(v9_cfg, "controlled_remove_occupancy", tmp_path, scripts=scripts)
    assert scripted.titles() == ["V9Propose", "V9Investigate", "V9Plan", "V9Critique", "V9Propose", "V9Plan",
                                 "V9Critique", "V9Final"]
    reopen = [e for e in events(result, "audit") if e.role == "code"]
    assert [e.details["continue"] for e in reopen] == ["regenerate"]          # once: the second audit cannot
    g = result.graph
    assert g.hypotheses["H3"].origin == "regenerated" and g.hypotheses["H3"].disposition == "active"
    assert result.metrics["regenerations"] == 1 and g.result.stop_reason == "coordinator_stop"


def three_active_without_questions() -> dict:
    """The occupancy proposal with a third active sketch (the active limit) and no questions."""
    first = copy.deepcopy(OCCUPANCY["coordinator"][0])
    third = copy.deepcopy(first["hypotheses"][0])
    third.update(key="h_tfa_reg", title="TFA binding changes element E2 activity", mechanism_class="regulatory",
                 reason_kind="distinct_mechanism", reason_detail="a regulatory reading of the TFA binding change",
                 claims=[], reuse_claims=[{"ref": "bind_a", "required": True}])
    first["hypotheses"].append(third)
    first["questions"] = []
    return first


def regeneration(hypotheses: list) -> dict:
    return {**three_active_without_questions(), "hypotheses": hypotheses, "questions": []}


NEW_STORY = {**OCCUPANCY["coordinator"][0]["hypotheses"][0], "key": "h_new", "title": "A new story on element E2",
             "mechanism_class": "other", "reason_kind": "distinct_mechanism",
             "reason_detail": "an alternative not yet examined", "claims": [],
             "reuse_claims": [{"ref": "C1", "required": True}]}
NONE_REPORTABLE_FINAL = {"comparisons": [], "outcome": {
    "category": "no_supported_explanation", "leading_ids": [], "summary": "binding is predicted only",
    "weakest_links": [], "next_experiments": []}}


def test_a_regeneration_after_the_audit_gets_the_active_slots(v9_cfg, tmp_path):
    """Three non-reportable hypotheses hold every active slot: code defers them first, so the regenerated sketch is
    active and reaches the second audit and the final comparison (it is not deferred for the active limit)."""
    scripts = {"coordinator": [three_active_without_questions(), stop_plan("nothing to test"),
                               regeneration([NEW_STORY]), stop_plan("done")],
               "critic": [audit([]), audit(["H4"]), NONE_REPORTABLE_FINAL]}
    result, scripted, _ = run_fixture(v9_cfg, "controlled_remove_occupancy", tmp_path, scripts=scripts)
    g = result.graph
    assert scripted.titles() == ["V9Propose", "V9Plan", "V9Critique", "V9Propose", "V9Plan", "V9Critique",
                                 "V9Final"]
    assert g.hypotheses["H4"].origin == "regenerated" and g.hypotheses["H4"].disposition == "active"
    for hid in ("H1", "H2", "H3"):
        h = g.hypotheses[hid]
        assert h.disposition == "deferred" and "not a refutation" in h.disposition_reason and h.revisit_trigger
    final = scripted.packets()[-1]
    assert "Claims of the active hypotheses" in final and "H4 v" in final


def test_parked_hypotheses_return_when_the_regeneration_adds_nothing(v9_cfg, tmp_path):
    scripts = {"coordinator": [three_active_without_questions(), stop_plan("nothing to test"), regeneration([])],
               "critic": [audit([]), audit(["H1", "H2", "H3"]), NONE_REPORTABLE_FINAL]}
    result, scripted, _ = run_fixture(v9_cfg, "controlled_remove_occupancy", tmp_path, scripts=scripts)
    g = result.graph
    assert {h: x.disposition for h, x in g.hypotheses.items()} == {"H1": "active", "H2": "active", "H3": "active"}
    restored = [e for e in events(result, "activate") if e.role == "code"
                and "left no active hypothesis" in e.concise_reason]
    assert len(restored) == 3 and scripted.titles()[-1] == "V9Final"
    assert g.result.stop_reason == "regeneration_limit" and g.result.outcome == "no_supported_explanation"


def misread_e2() -> list:
    """The synthetic critic, finding the passage behind H1's only contradiction (E2 on C2) misread."""
    critic = copy.deepcopy(SYNTHETIC["critic"])
    critic[0]["passage_checks"] = [{"evidence_id": "E2", "verdict": "misread",
                                    "note": "the record describes another intervention"}]
    return critic


def test_a_rejection_whose_contradiction_the_critic_withdraws_is_reinstated_as_deferred(v9_cfg, tmp_path):
    """The critic finds the passage behind the only contradiction misread: the claim falls back to unresolved, and
    code reinstates H1 as deferred (graph.reinstate), once; the final packet, the summary and the metrics say so. A
    reinstatement is not support: the outcome is unchanged."""
    result, scripted, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path, scripts={**SYNTHETIC, "critic": misread_e2()})
    g = result.graph
    h1 = g.hypotheses["H1"]
    assert g.claims["C2"].assessment == "unresolved" and h1.disposition == "deferred" and h1.revisit_trigger
    back = events(result, "reinstate")
    assert len(back) == 1 and back[0].role == "code" and back[0].details["claims"] == ["C2"]
    assert [x["kind"] for x in h1.history].count("reinstatement") == 1
    assert not [e for e in events(result, "audit") if e.details.get("stale_rejection")]      # reversed, not noted
    final = next(p for p in scripted.packets() if p.startswith("Role: critic; stage: final"))
    assert "Rejections reinstated by code:" in final and "code reinstated it once (now deferred)" in final
    assert "Rejections that no longer stand: none" in final
    assert "Reinstated by code as deferred" in g.result.summary and "H1 (C2 no longer contradicted" in g.result.summary
    assert result.metrics["reinstated"] == ["H1"] and result.metrics["stale_rejections"] == []
    assert g.result.outcome == "no_supported_explanation"


@pytest.mark.parametrize("kept", ["false", "refused"])
def test_a_stale_rejection_the_graph_keeps_is_disclosed_once(v9_cfg, tmp_path, monkeypatch, kept):
    """When graph.reinstate leaves the rejection in place (it returns False: a second rejection, or a structure an
    open hypothesis holds; or it refuses: a rejection code did not make), the run says plainly that it no longer
    stands, once."""
    def reinstate(self, hid, reason, role="code"):
        if kept == "refused":
            raise GraphRefusal(f"{hid} was not rejected by code for a contradicted required claim")
        return False

    monkeypatch.setattr(ClaimGraph, "reinstate", reinstate)
    result, scripted, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path, scripts={**SYNTHETIC, "critic": misread_e2()})
    g = result.graph
    assert g.claims["C2"].assessment == "unresolved" and g.hypotheses["H1"].disposition == "rejected"
    noted = [e for e in events(result, "audit") if e.details.get("stale_rejection") == "H1"]
    assert len(noted) == 1 and noted[0].role == "code" and noted[0].details["reinstated"] is False
    assert ("not rejected by code" if kept == "refused" else "the graph keeps it rejected") in noted[0].details["why"]
    final = next(p for p in scripted.packets() if p.startswith("Role: critic; stage: final"))
    assert "Rejections that no longer stand:" in final and "H1: rejected, but none" in final
    assert "no longer stand: H1" in g.result.summary and result.metrics["stale_rejections"] == ["H1"]
    assert result.metrics["reinstated"] == [] and not events(result, "reinstate")


def test_a_rejection_withdrawn_during_a_round_is_reinstated_and_audited_like_any_deferred_one(v9_cfg, tmp_path):
    """An investigator relinks E2 (the only contradiction of C2) as context only in round 2: code reinstates H1 as
    deferred right after that round, so the coordinator's plan sees it deferred. The plan defers H2 too; nothing is
    active and no regeneration is left, so the audit covers the deferred hypotheses, H1 among them, and the critic's
    reportable H1 is brought back for the final comparison."""
    investigator = copy.deepcopy(SYNTHETIC["computational_investigator"])
    investigator[1]["answers"][0]["proposed_updates"].append({
        "kind": "attach_evidence", "claim_id": "C2", "base_version": None, "evidence_id": "E2",
        "experiment_index": None, "stance": "context_only", "applicability": None,
        "rationale": "on rereading, the intervention is not the one C2 describes", "limitations": [],
        "suggested_assessment": None, "new_claim": None})
    defer_h2 = {"hypothesis_updates": [{
        "hypothesis_id": "H2", "action": "defer", "reason": "no tool in this fixture tests gene Y", "claim_id": None,
        "new_claim": None, "new_claim_id": None, "required": False, "revisit_trigger": "a gene Y record appears",
        "revision": None}], "assessments": [], "questions": [],
        "stop": {"stop": True, "reason": "nothing affordable is left to test"}}
    critic = [audit(["H1"]), {"comparisons": [], "outcome": {
        "category": "no_supported_explanation", "leading_ids": [], "summary": "C2 is unresolved again",
        "weakest_links": [], "next_experiments": []}}]
    scripts = {**SYNTHETIC, "coordinator": [*SYNTHETIC["coordinator"][:2], defer_h2],
               "computational_investigator": investigator, "critic": critic}
    result, scripted, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path, scripts=scripts)
    g = result.graph
    back = events(result, "reinstate")
    plan = next(e for e in g.events if e.action == "defer" and e.target_ids == ["H2"])
    assert len(back) == 1 and g.events.index(back[0]) < g.events.index(plan)      # before the coordinator's plan
    plan_packet = next(p for p in scripted.packets() if p.startswith("Role: coordinator; stage: plan"))
    assert "H1 v1 [deferred]" in plan_packet and "reinstated by code" in plan_packet
    audit_packet = next(p for p in scripted.packets() if p.startswith("Role: critic; stage: audit"))
    assert "Audit the deferred hypotheses H1, H2" in audit_packet
    assert g.hypotheses["H1"].disposition == "active" and g.hypotheses["H2"].disposition == "deferred"
    final = scripted.packets()[-1]
    assert final.startswith("Role: critic; stage: final") and "Claims of the active hypotheses" in final
    assert g.result.stop_reason == "regeneration_limit" and g.result.outcome == "no_supported_explanation"
    assert result.metrics["reinstated"] == ["H1"]


def test_activation_flags_reach_the_final_packet_and_the_metrics(v9_cfg, tmp_path):
    flagged = {**audit(["H1"]), "activation_flags": [{"hypothesis_id": "H1", "reason": "activated for the largest z"}]}
    scripts = {**WRONG_TF, "critic": [flagged, WRONG_TF["critic"][1]]}
    result, scripted, _ = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, scripts=scripts)
    final = scripted.packets()[-1]
    assert "critic's activation flag: the reason for activating it is only a rank (activated for the largest z)" \
        in final
    assert result.metrics["activation_flags"] == [{"hypothesis_id": "H1", "reason": "activated for the largest z"}]


def test_consequential_challenges_get_one_more_round_and_no_second_audit(v9_cfg, tmp_path):
    challenge = {"claim_id": "C4", "base_version": 3, "kind": "missing_alternative", "evidence_ids": ["E4"],
                 "gap": "no occupancy evidence for TFB in context Z",
                 "requested_action": {"tool": "syn_chip", "params_json": '{"tf": "TFB"}', "purpose": "TFB occupancy"},
                 "suggested_assessment": None}
    extra = {"answers": [{"question_id": "Q4", "status": "unanswerable",
                          "answer_summary": "no ChIP-seq records for TFB: missing data", "claim_ids": ["C4"],
                          "tool_call_ids": ["T5"], "experiments": [], "proposed_updates": [],
                          "remaining_gap": "TFB occupancy is untested", "next_question": "",
                          "follow_up_actions": []}]}
    scripts = {**WRONG_TF, "computational_investigator": [*WRONG_TF["computational_investigator"], extra],
               "critic": [audit(["H1"], [challenge], consequential=True), WRONG_TF["critic"][1]]}
    result, scripted, _ = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, scripts=scripts)
    g = result.graph
    assert scripted.titles()[-3:] == ["V9Critique", "V9Investigate", "V9Final"]
    assert [e.details["continue"] for e in events(result, "audit") if e.role == "code"] == ["extra_round"]
    ask = next(e for e in events(result, "ask") if e.target_ids[0] == "Q4")
    assert ask.role == "critic" and g.questions["Q4"].target_claim_ids == ["C4"]
    assert g.questions["Q4"].status == "unanswerable" and g.tool_calls["T5"].evidence_ids == []
    assert g.claims["C4"].assessment == "supported_in_scope"                 # missing data changed nothing
    assert g.result.stop_reason == "coordinator_stop" and g.result.outcome == "leading_explanation"


def test_a_misread_passage_can_no_longer_support_a_claim(v9_cfg, tmp_path):
    check = {"evidence_id": "E4", "verdict": "misread", "note": "the assay does not compare the two alleles"}
    scripts = {**WRONG_TF, "critic": [audit(["H1"], passage_checks=[check]), WRONG_TF["critic"][1]]}
    result, _, _ = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, scripts=scripts)
    g = result.graph
    link = next(x for x in g.claims["C4"].evidence_links if x.evidence_id == "E4")
    assert link.stance == "context_only" and link.proposed_by == "critic" and link.revises is not None
    assert g.claims["C4"].assessment == "unresolved"
    reset = [e for e in events(result, "assess") if e.target_ids == ["C4"] and e.details.get("automatic")]
    assert reset and reset[0].role == "code"


def test_the_engine_builds_the_resolver_and_group_registry_from_the_config(v9_cfg, tmp_path):
    fixture = load_fixture("synthetic_repair")
    caller = RoleCaller(Scripted(v9_cfg, {}).client, v9_cfg)
    engine = Engine(v9_cfg, "fixture", caller, FixtureToolRunner(fixture), tmp_path, facts=fixture_facts)
    assert engine.groups is not None and engine.groups.members("G001")
    if v9_cfg.path("data", "hgnc").exists():
        assert engine.resolver is not None and engine.resolver("tp53")[0] == "TP53"
    assert engine.limits == EngineLimits.from_config(v9_cfg) and caller.max_calls == engine.limits.max_model_calls
    assert EngineLimits().max_model_calls == 24 and EngineLimits().max_regenerations == 1     # SPEC 13.9


def test_limits_come_from_the_v9_block_and_explicit_limits_win(v9_cfg):
    cfg = {**v9_cfg, "v9": {"limits": {"max_model_calls": 30, "wall_seconds": 900, "http_request_cap": 150}}}
    limits = EngineLimits.from_config(cfg)
    assert (limits.max_model_calls, limits.wall_seconds, limits.max_active) == (30, 900, 3)
    caller = RoleCaller(Scripted(v9_cfg, {}).client, cfg)
    assert caller.max_calls == 30
    Engine(cfg, "fixture", caller, FixtureToolRunner(load_fixture("synthetic_repair")), None,
           limits=EngineLimits(max_model_calls=10, reserve_model_calls=1))
    assert (caller.max_calls, caller.reserve) == (10, 1)
