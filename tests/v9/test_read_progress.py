"""Changed focus wording is not progress; a genuinely new passage or claim scope is."""

from types import SimpleNamespace

from variant2mechanism.v9 import progress
from variant2mechanism.v9.investigate import Engine, EngineLimits, _Run
from variant2mechanism.v9.schemas import Question, ToolCall, ToolRequest

from .test_evidence_adoption import observation_graph


def reading(g, focus, text="The measured result in context Z.", *, target="C1", location="body/p1"):
    qid = g.add_question(Question(text=f"Read {focus}", route="literature", target_claim_ids=[target],
                                 hypothesis_ids=["H1"], actions=[ToolRequest(tool="literature_read",
                                 params={"pmcid": "PMC123", "focus": [focus]})]), "coordinator")
    tid = g.reserve_tool_call_id()
    g.record_tool_call(ToolCall(tool_call_id=tid, tool_name="literature_read", execution_status="success",
        retrieval_status="records_found", requested_by="literature_investigator",
        query_parameters={"pmcid": "PMC123", "focus": [focus]}, observations=[
            {"kind": "article", "pmcid": "PMC123", "access": "full_text", "focus": [focus]},
            {"kind": "passage", "location": location, "text": text, "matched": [focus]}]), [])
    return qid, tid


def test_rephrased_focus_and_metadata_do_not_make_old_passages_new():
    g = observation_graph()
    q1, t1 = reading(g, "activity")
    q2, t2 = reading(g, "regulation")
    assert progress.read_state(g, q1, [t1]) == progress.read_state(g, q2, [t2])
    state = _Run(g, 0, question_calls={q2: [t2]})
    key, passages = progress.read_state(g, q1, [t1])
    state.read_history[key] = [(q1, passages)]
    assert Engine.__new__(Engine)._repeated_read(state, q2)
    assert g.questions[q2].status == "deferred"
    assert "No new source passages" in g.questions[q2].answer_summary


def test_new_passage_and_new_claim_scope_are_not_blocked():
    g = observation_graph()
    q1, t1 = reading(g, "activity")
    q2, t2 = reading(g, "new endpoint", text="A different result is reported.", location="body/p2")
    state = _Run(g, 0, question_calls={q2: [t2]})
    key, passages = progress.read_state(g, q1, [t1])
    state.read_history[key] = [(q1, passages)]
    assert not Engine.__new__(Engine)._repeated_read(state, q2)
    q3, t3 = reading(g, "direction")
    state.question_calls[q3] = [t3]
    g.claims["C1"].direction = "decreases"
    assert not Engine.__new__(Engine)._repeated_read(state, q3)


def test_one_refused_extraction_can_be_repaired_but_not_retried_forever():
    g = observation_graph()
    q1, t1 = reading(g, "activity")
    q2, t2 = reading(g, "exact result")
    q3, t3 = reading(g, "exact result again")
    key, passages = progress.read_state(g, q1, [t1])
    state = _Run(g, 0, question_calls={q2: [t2], q3: [t3]}, read_history={key: [(q1, passages)]})
    g.log("refuse_update", "literature_investigator", "passage not contiguous",
          details={"kind": "add_evidence", "question_id": q1})
    engine = Engine.__new__(Engine)
    assert not engine._repeated_read(state, q2)
    state.read_history[key].append((q2, passages))
    assert engine._repeated_read(state, q3)


def test_failed_reads_have_no_text_but_repeated_abstract_text_is_recognised():
    g = observation_graph()
    q, t = reading(g, "assay")
    g.tool_calls[t].execution_status = "error"
    assert progress.read_state(g, q, [t]) is None
    g.tool_calls[t].execution_status = "success"
    g.tool_calls[t].observations[0]["access"] = "abstract_only"
    assert progress.read_state(g, q, [t]) is not None  # recognises the text, not proof of full-body access


def test_invalid_answer_gets_one_retry_and_remains_a_processing_gap_after_a_second_failure():
    g = observation_graph()
    q1, t1 = reading(g, "activity")
    q2, t2 = reading(g, "repair the answer")
    q3, t3 = reading(g, "retry again")
    key, passages = progress.read_state(g, q1, [t1])
    state = _Run(g, 0, question_calls={q2: [t2], q3: [t3]}, read_history={key: [(q1, passages)]})
    engine = Engine.__new__(Engine)
    for q in [q1, q2]:
        g.log("refuse_update", "literature_investigator", "invalid answer", target_ids=[q],
              details={"failed": True, "kind": "invalid_output", "stage": "investigate (answer)"})
        if q == q1:
            assert not engine._repeated_read(state, q2)
            state.read_history[key].append((q2, passages))
    assert engine._repeated_read(state, q3)
    assert "processing gap" in g.questions[q3].answer_summary
    assert g.claims["C1"].assessment == "unassessed"


def test_budget_stop_preserves_an_audit_and_final_comparison():
    engine = Engine.__new__(Engine)
    engine.limits = EngineLimits(max_model_calls=24, reserve_audit_calls=4)
    engine.clock = lambda: 0
    engine.roles = SimpleNamespace(calls_used=17, max_calls=24, reserve=2, currency_exhausted=False,
                                   replay_miss=False, affordable=lambda final: True)
    engine.runner = SimpleNamespace(replay_miss=False)
    state = _Run(observation_graph(), 0)
    assert engine._blocker(state, final=False) == "budget_model_calls"
    assert engine._blocker(state, final=False, audit=True) is None
    assert engine._blocker(state, final=True) is None
