"""Realistic investigator output shapes: local references and nested links must reach the graph safely."""

import copy

import pytest

from variant2mechanism.agent.schemas import SchemaCheckError
from variant2mechanism.v9 import roles
from variant2mechanism.v9.investigate import Engine, _Run
from variant2mechanism.v9.schemas import Question

from .test_evidence_adoption import discovery_fixture, observation_graph


def answer_case(*, nested=True):
    graph = observation_graph()
    qid = graph.add_question(Question(text="Test the newly observed factor", route="computational",
                                     target_claim_ids=["C1"], hypothesis_ids=["H1"]), "coordinator")
    claim = copy.deepcopy(discovery_fixture().roles["coordinator"][2]["new_hypotheses"][0]["sketch"]["claims"][0])
    claim["context"] = {"label": "context Z", "species": "human", "condition": None}
    claim["initial_links"][0]["evidence_id"] = "E1"
    proposal = {"kind": "new_claim", "claim_id": None, "base_version": None, "evidence_id": None,
                "experiment_index": None, "stance": None, "applicability": None, "rationale": "A different factor",
                "limitations": [], "suggested_assessment": None, "new_claim": claim}
    updates = [proposal]
    if not nested:
        link = claim["initial_links"].pop()
        updates.append({**proposal, "kind": "attach_evidence", "claim_id": "key:new_binding", "new_claim": None,
                        **link})
    answer = {"question_id": qid, "status": "answered", "answer_summary": "The assay measures the new factor.",
              "claim_ids": ["C1", "key:new_binding"], "tool_call_ids": ["T1"], "experiments": [],
              "proposed_updates": updates, "remaining_gap": "Downstream mediation is untested.",
              "next_question": "", "follow_up_actions": []}
    return graph, {"answers": [answer]}


def apply(graph, raw):
    parsed = roles.V9Investigate.model_validate(raw)
    roles.investigate_check(graph, "computational", [raw["answers"][0]["question_id"]], {})(parsed)
    engine = Engine.__new__(Engine)
    engine._apply_answers(_Run(graph, 0), "computational", parsed, "answer")


@pytest.mark.parametrize("nested", [False, True])
def test_new_claim_local_references_and_assessments_work_without_guessed_versions(nested):
    graph, raw = answer_case(nested=nested)
    apply(graph, raw)
    claim = graph.claims["C2"]
    assert claim.assessment == "supported_in_scope"
    assert [(x.evidence_id, x.strength, x.applicability) for x in claim.evidence_links] == [("E1", "direct", "exact")]
    assert graph.claims["C1"].assessment == "unassessed"
    assert not graph.claims["C1"].evidence_links
    assert "C2" not in graph.hypotheses["H1"].claim_ids  # only the coordinator adopts a claim into a hypothesis


def test_undeclared_local_metadata_reference_is_still_refused():
    graph, raw = answer_case()
    raw["answers"][0]["claim_ids"].append("key:undeclared")
    with pytest.raises(SchemaCheckError, match="unknown claim key:undeclared"):
        apply(graph, raw)
    assert len(graph.claims) == 1


def test_initial_links_cannot_bypass_factor_identity():
    graph, raw = answer_case()
    raw["answers"][0]["proposed_updates"][0]["new_claim"]["objects"][0]["label"] = "DIFFERENT_FACTOR"
    apply(graph, raw)
    assert not graph.claims["C2"].evidence_links
    assert graph.claims["C2"].assessment == "unassessed"
    assert any(e.action == "refuse_update" and e.details.get("kind") == "attach_evidence" for e in graph.events)


def test_local_alias_of_an_existing_duplicate_does_not_get_a_free_assessment_version():
    graph, raw = answer_case()
    claim = roles.V9Claim.model_validate(raw["answers"][0]["proposed_updates"][0]["new_claim"])
    graph.add_claim(roles.claim_draft(claim, graph.case, "other", []), "coordinator")
    apply(graph, raw)
    assert len(graph.claims) == 2
    assert graph.claims["C2"].evidence_links  # linking evidence is safe; grading still needs a read version
    assert graph.claims["C2"].assessment == "unassessed"
    assert any(e.action == "refuse_update" and e.details.get("kind") == "assess" and
               "base_version" in e.concise_reason for e in graph.events)


def test_existing_claim_assessment_still_requires_its_read_version():
    graph, raw = answer_case(nested=False)
    raw["answers"][0]["proposed_updates"][1]["claim_id"] = "C1"
    with pytest.raises(SchemaCheckError, match="needs the base_version shown"):
        apply(graph, raw)


def test_a_new_claim_that_cites_an_experiment_that_was_not_accepted_is_refused_not_raised():
    """Any update kind can cite an experiment of its answer by index. When that experiment was refused, the update
    has no evidence to stand on: it is logged as refused and the rest of the answer is applied."""
    from .test_engine_literature import PASSAGE, experiment

    graph, raw = answer_case(nested=False)
    raw["answers"][0]["experiments"] = [experiment(PASSAGE, "sec1/p1")]
    new_claim, link = raw["answers"][0]["proposed_updates"]
    new_claim["experiment_index"] = 0
    qid = raw["answers"][0]["question_id"]
    graph.questions[qid].route = "literature"               # only the literature route extracts experiments
    parsed = roles.V9Investigate.model_validate(raw)
    roles.investigate_check(graph, "literature", [qid], {})(parsed)
    assert not parsed._proposal_errors                      # the reply itself is well formed
    engine = Engine.__new__(Engine)
    engine._extract = lambda *args: None                    # the experiment is not accepted as evidence
    engine._apply_answers(_Run(graph, 0), "literature", parsed, "answer")
    refused = [e for e in graph.events if e.action == "refuse_update"]
    assert any("experiment 0" in e.concise_reason and "the new_claim update that cites it is not applied"
               in e.concise_reason for e in refused)
    assert "C2" not in graph.claims
