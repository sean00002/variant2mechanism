"""The engine on the two controlled fixtures (SPEC 11 (a) and (b); plan section 14).

(a) Occupancy coverage removed: "no ChIP record" must never become "the TF cannot bind": the occupancy claims stay
unresolved, nothing is contradicted, a request to reject a TF hypothesis for lack of a peak is refused, and both TF
candidates stay active. Deferring both for the missing peak cannot end the run either: the coordinator's stop is not
applied while nothing is active, a regeneration comes first, and the critic audits the deferred hypotheses and brings
back those still reportable for the final comparison.
(b) Wrong TF with a supported element-to-gene link: the member claim is superseded and swapped into the hypothesis,
the element-to-gene claim keeps its evidence, and neither TF's evidence can be moved to the other's claim.
"""

from variant2mechanism.v9.fixtures import load_fixture

from .test_engine_support import events, run_fixture

OCCUPANCY = load_fixture("controlled_remove_occupancy").roles


def test_removed_occupancy_leaves_claims_unresolved_and_keeps_both_candidates(v9_cfg, tmp_path):
    result, _, _ = run_fixture(v9_cfg, "controlled_remove_occupancy", tmp_path)
    g = result.graph
    assert result.metrics["engine_error"] is None
    occupancy = [c for c in g.claims.values() if c.relation == "occupies"]
    assert len(occupancy) == 2 and {c.assessment for c in occupancy} == {"unresolved"}
    for call in g.tool_calls.values():
        if call.tool_name == "syn_occupancy":                              # empty retrievals: no evidence at all
            assert call.retrieval_status == "no_records_found" and call.evidence_ids == []
    assert not [x for c in g.claims.values() for x in c.evidence_links if x.stance == "contradicts"]
    assert all(c.assessment != "contradicted_in_scope" for c in g.claims.values())

    # both TF candidates retained: active, never rejected or deferred for the missing peak
    assert {h: x.disposition for h, x in g.hypotheses.items()} == {"H1": "active", "H2": "active"}
    named = {g.entities[e].label for h in g.hypotheses.values() for c in h.claim_ids
             for e in g.claims[c].subject_ids + g.claims[c].object_ids if g.entities[e].kind == "tf"}
    assert named == {"TFA", "TFB"}
    refused = [e for e in events(result, "refuse_update") if e.role == "coordinator"]
    assert len(refused) == 1 and "cannot be rejected" in refused[0].concise_reason
    assert refused[0].details["update"]["disposition"] == "rejected"
    assert {q.status for q in g.questions.values()} == {"unanswerable"}

    # the shared group prediction stays indirect: binding claims are shown as predicted, never supported
    binding = [c for c in g.claims.values() if c.relation == "alters_binding"]
    assert {g.display_status(c.claim_id) for c in binding} == {"predicted"}
    assert g.result.outcome == "no_supported_explanation" and g.result.stop_reason == "coordinator_stop"
    assert [p.outcome for p in g.comparisons.values()] == ["insufficient_evidence"]


def defer_for_missing_peak(hid: str) -> dict:
    return {"hypothesis_id": hid, "action": "defer", "reason": f"no ChIP-seq record for {hid}'s TF at element E2",
            "claim_id": None, "new_claim": None, "new_claim_id": None, "required": False,
            "revisit_trigger": "occupancy data for context Z becomes available", "revision": None}


def test_deferring_every_candidate_for_missing_occupancy_cannot_end_the_run(v9_cfg, tmp_path):
    plan = {"hypothesis_updates": [defer_for_missing_peak("H1"), defer_for_missing_peak("H2")], "assessments": [],
            "questions": [], "stop": {"stop": True, "reason": "no occupancy data: nothing more to test"}}
    empty_regeneration = {**OCCUPANCY["coordinator"][0], "hypotheses": [], "questions": []}
    audit = {"challenges": [], "passage_checks": [], "activation_flags": [], "reportable_ids": ["H1", "H2"],
             "consequential": False}
    scripts = {**OCCUPANCY, "coordinator": [OCCUPANCY["coordinator"][0], plan, empty_regeneration],
               "critic": [audit, OCCUPANCY["critic"][1]]}
    result, scripted, _ = run_fixture(v9_cfg, "controlled_remove_occupancy", tmp_path, scripts=scripts)
    g = result.graph
    assert scripted.titles() == ["V9Propose", "V9Investigate", "V9Plan", "V9Propose", "V9Critique", "V9Final"]
    not_applied = [e for e in events(result, "refuse_update") if e.details.get("kind") == "stop"]
    assert len(not_applied) == 1 and g.result.stop_reason == "regeneration_limit"
    audit_packet = next(p for p in scripted.packets() if p.startswith("Role: critic; stage: audit"))
    assert "No hypothesis is active" in audit_packet and "H1, H2" in audit_packet
    # deferred for missing data, never rejected; the critic's audit brings both back for the final comparison
    assert {h: x.disposition for h, x in g.hypotheses.items()} == {"H1": "active", "H2": "active"}
    assert not [e for e in g.events if e.action == "reject"]
    assert [p.outcome for p in g.comparisons.values()] == ["insufficient_evidence"]
    assert g.result.outcome == "no_supported_explanation" and g.result.downgraded_from is None


def test_wrong_tf_is_superseded_without_moving_evidence_between_tfs(v9_cfg, tmp_path):
    result, _, _ = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path)
    g = result.graph
    assert result.metrics["engine_error"] is None
    old, new, reg = g.claims["C1"], g.claims["C4"], g.claims["C2"]
    assert [g.entities[c.object_ids[0]].label for c in (old, new)] == ["TFA", "TFB"]
    assert (old.superseded_by, new.supersedes) == ("C4", "C1")

    # the hypothesis keeps its element-to-gene claim and swaps the member claim in place
    h = g.hypotheses["H1"]
    assert h.required_claim_ids == ["C4", "C2"] and h.disposition == "leading"
    assert reg.assessment == "supported_in_scope" and [x.evidence_id for x in reg.evidence_links] == ["E3"]
    assert any(e.details.get("replaced") == {"C1": "C4"} for e in events(result, "revise_hypothesis"))

    # TF-specific evidence stays with its TF: the TFA ChIP never reaches the TFB claim, nor the TFB assay the TFA one
    assert [x.evidence_id for x in new.evidence_links] == ["E4"] and new.assessment == "supported_in_scope"
    assert [x.evidence_id for x in old.evidence_links] == ["E2"]                 # the old claim keeps its own link
    refusals = [e.concise_reason for e in events(result, "refuse_update")]
    assert any("E4 is about TFB, not TFA" in r for r in refusals)
    assert any("E2 is about TFA, not TFB" in r for r in refusals)
    supersede = events(result, "supersede_claim")[0]
    assert supersede.details["links_copied"] == 0 and supersede.role == "computational_investigator"

    assert g.result.outcome == "leading_explanation" and g.result.leading_ids == ["H1"]
    assert g.result.downgraded_from is None and not g.result.weakest_links
