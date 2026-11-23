"""The engine on the synthetic repair fixture (SPEC 11): scripted roles, fixture tools, the whole loop.

Every observation is stipulated by the fixture; the expected behaviour follows the plan's matched-direction
contradiction: the contradicted required claim rejects H1 at its assessment (by code), the dependent phenotype claim
is flagged but never contradicted, the regenerated copy of H1 is refused, H2 stays unresolved, and the run ends with
no supported explanation and a recorded stop reason.
"""

import json

from variant2mechanism.v9.fixtures import load_fixture
from variant2mechanism.v9.graph import ClaimGraph

from .test_engine_support import events, run_fixture


def test_synthetic_run_rejects_flags_regenerates_and_abstains(v9_cfg, tmp_path):
    result, scripted, caller = run_fixture(v9_cfg, "synthetic_repair", tmp_path)
    g = result.graph
    assert result.metrics["engine_error"] is None
    f0, f1, f2, f3 = "C1", "C2", "C3", "C4"
    assert [(c, g.claims[c].assessment) for c in (f0, f1, f2, f3)] == [
        (f0, "supported_in_scope"), (f1, "contradicted_in_scope"), (f2, "unassessed"), (f3, "unresolved")]
    assert g.claims[f2].dependency_flag == "unsupported_due_to_dependency"            # flagged, not contradicted
    assert g.hypotheses["H1"].disposition == "rejected" and g.hypotheses["H1"].path_status[f2] == "premise_failed"

    # H1 is rejected by code at the contradicted_in_scope assessment, naming the claim and the evidence
    assess = next(e for e in g.events if e.action == "assess" and e.details.get("to") == "contradicted_in_scope")
    reject = next(e for e in g.events if e.action == "reject")
    assert g.events.index(reject) == g.events.index(assess) + 1
    assert reject.role == "code" and reject.target_ids == ["H1"] and f1 in reject.concise_reason
    assert reject.evidence_ids == g.tool_calls["T2"].evidence_ids
    assert assess.details["suggested_by"] == "computational_investigator" and assess.role == "code"

    # the misread supports link and the regenerated copy of H1 were refused, with reasons
    refusals = [e.concise_reason for e in events(result, "refuse_update")]
    assert any("opposite" in r for r in refusals)
    assert any("repeats rejected hypothesis H1" in r for r in refusals)
    regenerated = [h for h in g.hypotheses.values() if h.origin == "regenerated"]
    assert [h.hypothesis_id for h in regenerated] == ["H2"] and regenerated[0].replaces == "H1"
    assert g.hypotheses["H2"].disposition == "active" and g.hypotheses["H2"].required_claim_ids == [f3]
    assert f0 in g.hypotheses["H2"].claim_ids                                  # the supported overlap is kept

    # the empty retrieval for gene Y created no evidence and no contradiction
    call_y = next(t for t in g.tool_calls.values() if t.query_parameters == {"gene": "Y"})
    assert call_y.retrieval_status == "no_records_found" and call_y.evidence_ids == []
    assert not [x for x in g.claims[f3].evidence_links]
    assert g.questions["Q2"].status == "unanswerable"

    r = g.result
    assert r.outcome == "no_supported_explanation" and r.stop_reason == "coordinator_stop"
    assert r.budget_stop is False and r.downgraded_from is None
    stop = events(result, "stop")
    assert stop and stop[-1].details["stop_reason"] == "coordinator_stop" and stop[-1].role == "coordinator"
    assert events(result, "decide")[-1].role == "code"
    assert result.metrics["regenerations"] == 1 and result.metrics["outcome"] == "no_supported_explanation"
    assert result.manifest_parts["stop_reason"] == "coordinator_stop"
    assert set(result.manifest_parts["prompts"]) >= {"rules", "coordinator_system", "critic_final"}

    # every scripted reply was used exactly once, in call order, and each counted as a model call
    fixture = load_fixture("synthetic_repair")
    assert len(scripted.responses.served) == sum(len(v) for v in fixture.roles.values())
    assert caller.calls_used == len(scripted.sent) == result.metrics["model_calls"]
    assert scripted.titles() == ["V9Propose", "V9Investigate", "V9Propose", "V9Investigate", "V9Plan",
                                 "V9Critique", "V9Final"]


def test_synthetic_run_is_deterministic_and_round_trips(v9_cfg, tmp_path):
    first, _, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path / "a")
    second, _, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path / "b")
    a, b = json.loads(first.graph.to_json()), json.loads(second.graph.to_json())
    assert a == b                                               # cost 0 and a fixed clock: nothing volatile here
    assert ClaimGraph.from_json(first.graph.to_json()).to_json() == first.graph.to_json()


def test_packets_fence_data_and_carry_versions_and_effect_alleles(v9_cfg, tmp_path):
    result, scripted, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path)
    packets = scripted.packets()
    propose, investigate = packets[0], packets[1]
    assert propose.startswith("Role: coordinator; stage: propose; round 0")
    fenced = "".join(part.split("</data>")[0] for part in propose.split("<data>")[1:])
    outside = "".join(part.split("</data>")[-1] for part in propose.split("<data>"))
    for text in ("Synthetic variant V lies inside synthetic element E.", "E1 [synthetic", '"overlaps":true'):
        assert text in fenced and text not in outside                     # tool text sits inside the fences
    assert "C2 v1 [unassessed" in investigate                             # the version an update must carry
    assert "Ref allele A, alt allele G".lower() in propose.lower()
    plan = next(p for p in packets if p.startswith("Role: coordinator; stage: plan"))
    assert "C4 v2 [unresolved" in plan and "repeats rejected hypothesis H1" in plan   # refusals reach the plan
    # no volatile values (times, costs, cache flags) in any packet, so a replay sends the same requests
    for p in packets:
        assert "2026-11-08T" not in p and "$" not in p and "cost_usd" not in p and "cached" not in p.lower()
