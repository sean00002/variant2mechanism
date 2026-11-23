"""Budgets and stopping (SPEC 6, 13.9): every cap is a ceiling, a budget stop is disclosed, and without a final
comparison the outcome comes from the graph alone (compare.py's code fallback).

The fixtures are the controlled and synthetic ones; scripts are cut or altered here to reach each limit.
"""

import json

from variant2mechanism.v9.fixtures import load_fixture
from variant2mechanism.v9.investigate import EngineLimits
from variant2mechanism.v9.tools import ToolLimits

from .test_engine_support import decided_alone, events, run_fixture

WRONG_TF = load_fixture("controlled_wrong_tf").roles
SYNTHETIC = load_fixture("synthetic_repair").roles


def finish_length(reply: dict) -> dict:
    reply["choices"][0]["finish_reason"] = "length"
    return reply


def test_wall_time_stop_decides_from_the_graph_alone(v9_cfg, tmp_path):
    now = [0.0]

    def tick(_body):                                 # each model call takes 1000 s; the cap is 1200 s
        now[0] += 1000.0

    result, scripted, _ = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, clock=lambda: now[0], on_send=tick)
    r = result.graph.result
    assert r.stop_reason == "wall_time" and r.budget_stop is True
    assert scripted.titles() == ["V9Propose", "V9Investigate"]          # no critic call after the wall time
    # the graph alone names no hypothesis, and H1's binding claim (C1, a ChIP peak only) is unsettled, so the
    # supported element-to-gene bridge (C2) alone is not a mechanism
    assert r.outcome == "no_supported_explanation" and r.leading_ids == []
    assert result.graph.hypotheses["H1"].disposition == "active"
    assert r.downgraded_from is None and "graph alone" in r.summary
    assert "C1" in [w.claim_id for w in r.weakest_links]                    # the unresolved binding claim
    assert events(result, "decide")[-1].role == "code"
    assert result.metrics["wall_seconds"] == 2000.0
    decided_alone(result, "no_supported_explanation")                       # result, metrics and manifest agree


def test_the_reserve_keeps_the_final_comparison_after_a_model_call_stop(v9_cfg, tmp_path):
    scripts = {**WRONG_TF, "critic": [{
        "comparisons": [], "outcome": {"category": "partial_mechanism", "leading_ids": ["H1"],
                                       "summary": "binding by TFA is unresolved; the element-to-gene link holds",
                                       "weakest_links": [], "next_experiments": []}}]}
    result, scripted, caller = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, scripts=scripts,
                                           limits=EngineLimits(max_model_calls=8))
    r = result.graph.result
    assert r.stop_reason == "budget_model_calls" and r.budget_stop is True
    assert scripted.titles() == ["V9Propose", "V9Investigate", "V9Plan", "V9Final"]   # no audit, but a final
    assert any(e.details.get("skipped") == "budget_model_calls" for e in events(result, "audit"))
    assert caller.calls_used <= 8
    # the critic's partial_mechanism needs H1's molecular claims settled; its binding claim C1 is not
    assert r.outcome == "no_supported_explanation" and r.downgraded_from == "partial_mechanism"
    assert "C1" in r.downgrade_reason and r.leading_ids == []
    assert result.graph.questions["Q3"].status == "open" and any("Q3" in q for q in r.uninvestigated_questions)


def test_repairs_that_eat_the_reserve_leave_the_code_fallback(v9_cfg, tmp_path):
    good = WRONG_TF["computational_investigator"][0]
    scripts = {**WRONG_TF, "computational_investigator": ["{}", '{"answers": "not a list"}', "{}",
                                                          json.dumps(good)]}

    def alter(role, index, reply):                   # max_tokens twice: four sends for one call
        return finish_length(reply) if role == "computational_investigator" and index in (0, 2) else reply

    result, scripted, caller = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, scripts=scripts, alter=alter,
                                           limits=EngineLimits(max_model_calls=8))
    r = result.graph.result
    assert caller.calls_used == 5 <= 8                                        # the cap is never exceeded
    assert scripted.titles() == ["V9Propose"] + ["V9Investigate"] * 4
    assert r.stop_reason == "budget_model_calls" and r.budget_stop is True
    assert "V9Final" not in scripted.titles() and "V9Critique" not in scripted.titles()
    assert any(e.details.get("skipped") == "budget_model_calls" for e in events(result, "compare"))
    assert r.outcome == "no_supported_explanation" and r.downgraded_from is None    # from the graph alone
    assert result.graph.claims["C2"].assessment == "supported_in_scope"     # the repaired answer was applied


def test_currency_budget_stops_without_further_calls(v9_cfg, tmp_path):
    def priced(role, index, reply):
        reply["usage"]["cost"] = 0.05
        return reply

    result, scripted, caller = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, alter=priced, budget_usd=0.12)
    r = result.graph.result
    assert r.stop_reason == "budget_currency" and r.budget_stop is True
    assert len(scripted.sent) == 2 and caller.currency_exhausted               # the third call never left
    assert caller.failures[-1]["kind"] == "budget_currency"
    assert abs(caller.cost_usd - 0.10) < 1e-9 and result.metrics["cost_usd"] == caller.cost_usd
    assert r.outcome == "no_supported_explanation" and r.leading_ids == []
    assert result.manifest_parts["replayable"] is False                      # a replay would not stop there


def test_a_final_comparison_refused_by_the_currency_budget_is_a_budget_stop(v9_cfg, tmp_path):
    def priced(role, index, reply):                  # the audit spends almost the whole currency budget
        reply["usage"]["cost"] = 0.999 if (role, index) == ("critic", 0) else 0.0
        return reply

    result, scripted, caller = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, alter=priced, budget_usd=1.0)
    r = result.graph.result
    assert scripted.titles()[-1] == "V9Critique" and caller.failures[-1]["kind"] == "budget_currency"
    assert caller.failures[-1]["stage"] == "final"
    assert r.budget_stop is True and r.stop_reason == "coordinator_stop"    # the investigation itself was not cut
    assert "graph alone" in r.summary and r.leading_ids == []


def test_agent_tool_budget_stops_the_rounds(v9_cfg, tmp_path):
    result, scripted, _ = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, tool_limits=ToolLimits(max_tool_calls=2))
    g = result.graph
    assert g.result.stop_reason == "budget_tool_calls" and g.result.budget_stop is True
    assert g.questions["Q3"].status == "open" and not any(t.tool_name == "syn_binding_assay"
                                                           for t in g.tool_calls.values())
    assert result.metrics["tool_calls"]["agent"] == 2 and "V9Final" in scripted.titles()


def copy_only_regeneration() -> dict:
    regeneration = dict(SYNTHETIC["coordinator"][1])
    return {**regeneration, "hypotheses": regeneration["hypotheses"][:1], "questions": []}


def test_regeneration_is_capped(v9_cfg, tmp_path):
    scripts = {"coordinator": [SYNTHETIC["coordinator"][0], copy_only_regeneration()],
               "computational_investigator": SYNTHETIC["computational_investigator"][:1]}
    result, scripted, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path, scripts=scripts)
    r = result.graph.result
    assert scripted.titles() == ["V9Propose", "V9Investigate", "V9Propose"]
    assert r.stop_reason == "regeneration_limit" and r.budget_stop is False
    assert r.outcome == "no_supported_explanation" and result.metrics["regenerations"] == 1
    assert sum("repeats rejected hypothesis H1" in e.concise_reason for e in events(result, "refuse_update")) == 1


def test_a_raised_regeneration_limit_allows_one_more(v9_cfg, tmp_path):
    scripts = {"coordinator": [SYNTHETIC["coordinator"][0], copy_only_regeneration(), copy_only_regeneration()],
               "computational_investigator": SYNTHETIC["computational_investigator"][:1]}
    result, scripted, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path, scripts=scripts,
                                      limits=EngineLimits(max_regenerations=2))
    assert scripted.titles().count("V9Propose") == 3 and result.metrics["regenerations"] == 2
    assert result.graph.result.stop_reason == "regeneration_limit"
    assert sum("repeats rejected hypothesis H1" in e.concise_reason for e in events(result, "refuse_update")) == 2
