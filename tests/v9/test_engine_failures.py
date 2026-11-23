"""Failures, replay and determinism (SPEC 6, 13.4, 13.9): a run that could not investigate never reports a scientific
outcome, provider text never reaches a packet, a replay either reproduces the run or stops with cache_miss, repeated
questions cost no model call, a missing inventory is shown as missing, and nothing depends on the hash seed.

Fixtures and scripts are the synthetic and controlled ones (stipulated, not biological data); failures are injected
through the scripted transport.
"""

import copy
import hashlib
import json
import os
import subprocess
import sys

import pytest

from variant2mechanism.agent.llm import Budget, LLMClient
from variant2mechanism.config import REPO
from variant2mechanism.v9 import roles as R
from variant2mechanism.v9.fixtures import Fixture, FixtureToolRunner, load_fixture
from variant2mechanism.v9.graph import GroupRegistry, SymbolResolver
from variant2mechanism.v9.investigate import Engine, EngineLimits, fixture_facts
from variant2mechanism.v9.replay import ReplayMiss, refuse
from variant2mechanism.v9.tools import RecordedToolRunner

from .test_engine_support import decided_alone, events, run_fixture

WRONG_TF = load_fixture("controlled_wrong_tf")
OCCUPANCY = load_fixture("controlled_remove_occupancy").roles


def without_cost(value):
    """A graph's JSON without cost fields: cached replies cost nothing on replay."""
    if isinstance(value, dict):
        return {k: without_cost(v) for k, v in value.items() if k != "cost_usd"}
    if isinstance(value, list):
        return [without_cost(v) for v in value]
    return value


# --- a run that could not investigate --------------------------------------------------------------------------------

def test_a_refused_proposal_is_retried_as_a_proposal_then_ends_as_an_engine_error(v9_cfg, tmp_path):
    def refuse_coordinator(role, index, reply):
        if role == "coordinator":
            reply["choices"][0]["finish_reason"] = "content_filter"
        return reply

    result, scripted, caller = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, alter=refuse_coordinator)
    r = result.graph.result
    assert scripted.titles() == ["V9Propose", "V9Propose"]
    assert all(p.startswith("Role: coordinator; stage: propose") and "REGENERATION: no reportable" not in p
               for p in scripted.packets())                       # the retry is a proposal, not a regeneration
    assert result.metrics["regenerations"] == 0 and [f["kind"] for f in caller.failures] == ["content_filter"] * 2
    assert r.outcome == "input_or_capability_limitation" and r.stop_reason == "engine_error"
    assert r.budget_stop is False and "no usable proposal" in r.summary and not result.graph.hypotheses
    assert result.manifest_parts["replayable"] is False
    decided_alone(result, "input_or_capability_limitation")


def test_a_provider_that_never_answers_is_a_capability_limitation(v9_cfg, tmp_path):
    def down(_body):
        raise ConnectionError("upstream unavailable")

    result, _, caller = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path, on_send=down)
    r = result.graph.result
    assert [f["kind"] for f in caller.failures] == ["ConnectionError"] * 2 and caller.calls_used == 0
    assert (r.outcome, r.stop_reason) == ("input_or_capability_limitation", "engine_error")
    decided_alone(result, "input_or_capability_limitation")


def test_an_internal_error_is_never_reported_as_a_scientific_result(v9_cfg, tmp_path, monkeypatch):
    def broken(*_args, **_kwargs):
        raise KeyError("E999")

    monkeypatch.setattr(R, "propose_packet", broken)
    result, scripted, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path)
    r = result.graph.result
    assert scripted.sent == [] and result.metrics["engine_error"].startswith("KeyError")
    assert (r.outcome, r.stop_reason) == ("input_or_capability_limitation", "engine_error")
    assert events(result, "stop")[-1].details["stop_reason"] == "engine_error"
    decided_alone(result, "input_or_capability_limitation")


def test_an_internal_error_after_hypotheses_exist_still_names_none(v9_cfg, tmp_path, monkeypatch):
    """An error in the middle of the investigation, once hypotheses are active: the result is a limitation in both the
    result and the metrics, and the active hypotheses are neither leading nor tied."""
    def broken(*_args, **_kwargs):
        raise RuntimeError("the plan packet could not be built")

    monkeypatch.setattr(R, "plan_packet", broken)
    result, _, _ = run_fixture(v9_cfg, "controlled_wrong_tf", tmp_path)
    assert result.graph.hypotheses and result.metrics["engine_error"].startswith("RuntimeError")
    assert {h.disposition for h in result.graph.hypotheses.values()} == {"active"}
    decided_alone(result, "input_or_capability_limitation")
    assert result.graph.result.stop_reason == "engine_error"


def test_a_failed_plan_with_nothing_left_to_run_stops_without_a_critic_call(v9_cfg, tmp_path):
    scripts = {**WRONG_TF.roles, "coordinator": [WRONG_TF.roles["coordinator"][0], "{}", "{}"]}
    result, scripted, caller = run_fixture(v9_cfg, WRONG_TF, tmp_path, scripts=scripts)
    r = result.graph.result
    assert scripted.titles() == ["V9Propose", "V9Investigate", "V9Plan", "V9Plan"]      # the plan and its repair
    assert (r.outcome, r.stop_reason) == ("input_or_capability_limitation", "engine_error")
    assert caller.failures[-1]["kind"] == "invalid_output" and "plan failed" in r.summary
    assert result.graph.claims["C2"].assessment == "supported_in_scope"      # what was investigated is kept
    decided_alone(result, "input_or_capability_limitation")


def test_a_cache_only_run_that_misses_a_reply_is_not_called_a_replay(v9_cfg, tmp_path):
    """A cache-only run answers model calls from the response cache as a replay does: a miss stops it with cache_miss,
    worded for any run (the wiring found "the replay cannot go on" on runs that were not replays)."""
    def not_cached(_body):
        raise ReplayMiss("no cached reply for this request")

    result, _, caller = run_fixture(v9_cfg, "synthetic_repair", tmp_path, on_send=not_cached)
    stop = events(result, "stop")[-1]
    assert stop.details["stop_reason"] == "cache_miss" and [f["kind"] for f in caller.failures] == ["replay_miss"]
    assert "the run cannot go on" in stop.concise_reason and "replay" not in stop.concise_reason
    decided_alone(result, "input_or_capability_limitation")
    assert result.metrics["cache_miss"] is True


def test_provider_text_stays_out_of_packets(v9_cfg, tmp_path):
    def flaky(role, index, reply):
        if (role, index) == ("computational_investigator", 0):
            raise ConnectionError("502 Bad Gateway from upstream provider (request id abc123)")
        return reply

    result, scripted, _ = run_fixture(v9_cfg, "controlled_remove_occupancy", tmp_path, alter=flaky)
    plan = next(p for p in scripted.packets() if p.startswith("Role: coordinator; stage: plan"))
    assert "(ConnectionError)" in plan and "abc123" not in plan
    failed = next(e for e in events(result, "refuse_update") if e.details.get("failed"))
    assert failed.details["kind"] == "ConnectionError" and "abc123" in failed.details["error"]
    assert "abc123" not in failed.concise_reason


# --- replay ----------------------------------------------------------------------------------------------------------------

def save_bundle(result, run_dir) -> None:
    """The three files RecordedToolRunner reads (raw/ is already in the run folder)."""
    (run_dir / "graph.json").write_text(result.graph.to_json())
    (run_dir / "tool_calls.jsonl").write_text("".join(t.model_dump_json() + "\n"
                                                      for t in result.graph.tool_calls.values()))
    (run_dir / "evidence.jsonl").write_text("".join(e.model_dump_json() + "\n" for e in result.graph.evidence.values()))


def replay(cfg, saved, out, cache_dir):
    caller = R.RoleCaller(LLMClient(cfg, transport=refuse, budget=Budget(out / "budget.json", {"dev": 1e9}),
                                    cache_dir=cache_dir), cfg)
    runner = RecordedToolRunner(saved, config=cfg, run_dir=out / "run", registry=FixtureToolRunner(WRONG_TF).registry)
    engine = Engine(cfg, "cache_only", caller, runner, out / "run", limits=EngineLimits(), facts=fixture_facts,
                    resolver=SymbolResolver({}), groups=GroupRegistry({}), clock=lambda: 0.0)
    return engine.run(WRONG_TF.case), caller, runner


def test_a_clean_run_replays_identically_from_its_bundle_and_the_response_cache(v9_cfg, tmp_path):
    cache = tmp_path / "llm"
    original, _, _ = run_fixture(v9_cfg, WRONG_TF, tmp_path / "a", cache_dir=cache)
    assert original.manifest_parts["replayable"] is True and original.manifest_parts["not_replayable"] == []
    save_bundle(original, tmp_path / "a" / "run")
    again, caller, runner = replay(v9_cfg, tmp_path / "a" / "run", tmp_path / "b", cache)
    assert runner.misses == [] and caller.failures == [] and not again.metrics["cache_miss"]
    assert without_cost(json.loads(again.graph.to_json())) == without_cost(json.loads(original.graph.to_json()))


@pytest.mark.parametrize("title", ["V9Plan", "V9Critique", "V9Final"])
def test_a_replay_that_misses_a_model_reply_stops_with_cache_miss(v9_cfg, tmp_path, title):
    """The miss stops the replay at once: no later call, no decision from a different graph, and never a budget
    stop (review finding: the miss was swallowed as an ordinary failure and the replay decided anyway)."""
    cache = tmp_path / "llm"
    original, scripted, _ = run_fixture(v9_cfg, WRONG_TF, tmp_path / "a", cache_dir=cache)
    save_bundle(original, tmp_path / "a" / "run")
    lost = next(b for b in scripted.sent if b["response_format"]["json_schema"]["schema"]["title"] == title)
    key = hashlib.sha256(json.dumps({**lost, "seed": 0}, sort_keys=True, default=str).encode()).hexdigest()
    (cache / f"{key}.json").unlink()                                   # that reply is no longer cached
    again, caller, _ = replay(v9_cfg, tmp_path / "a" / "run", tmp_path / "b", cache)
    r = again.graph.result
    assert (r.outcome, r.stop_reason, r.budget_stop) == ("input_or_capability_limitation", "cache_miss", False)
    assert [f["kind"] for f in caller.failures] == ["replay_miss"]
    assert again.metrics["cache_miss"] is True and not again.graph.comparisons and r.leading_ids == []
    decided_alone(again, "input_or_capability_limitation")


def test_a_replay_that_misses_a_tool_result_stops_before_the_investigator_reads_it(v9_cfg, tmp_path):
    cache = tmp_path / "llm"
    original, _, _ = run_fixture(v9_cfg, WRONG_TF, tmp_path / "a", cache_dir=cache)
    saved = tmp_path / "a" / "run"
    save_bundle(original, saved)
    kept = [line for line in (saved / "tool_calls.jsonl").read_text().splitlines()
            if json.loads(line)["tool_name"] != "syn_binding_assay"]
    (saved / "tool_calls.jsonl").write_text("\n".join(kept) + "\n")
    again, caller, runner = replay(v9_cfg, saved, tmp_path / "b", cache)
    assert runner.misses and again.graph.result.stop_reason == "cache_miss"
    assert caller.usage["computational_investigator"]["calls"] == 1 and caller.failures == []
    decided_alone(again, "input_or_capability_limitation")


def test_a_max_tokens_retry_makes_the_run_unreplayable(v9_cfg, tmp_path):
    critic = WRONG_TF.roles["critic"]
    scripts = {**WRONG_TF.roles, "critic": [critic[0], critic[1], critic[1]]}

    def cut(role, index, reply):
        if (role, index) == ("critic", 1):
            reply["choices"][0]["finish_reason"] = "length"
        return reply

    result, _, caller = run_fixture(v9_cfg, WRONG_TF, tmp_path, scripts=scripts, alter=cut)
    assert result.graph.result.outcome == "leading_explanation"            # the run itself is unaffected
    assert result.manifest_parts["replayable"] is False
    assert any("max_tokens" in why for why in result.manifest_parts["not_replayable"])
    assert caller.unreplayable == [{"role": "critic", "stage": "final", "why": caller.unreplayable[0]["why"]}]


# --- progress, inventory and determinism -----------------------------------------------------------------------------

def test_a_repeated_question_is_closed_without_a_model_call(v9_cfg, tmp_path):
    repeat = copy.deepcopy(OCCUPANCY["coordinator"][0]["questions"][0])
    repeat.update(target_claims=["C2"], hypotheses=["H1"])             # Q1 exactly: same action and target
    plan = {"hypothesis_updates": [], "assessments": [], "questions": [repeat], "stop": {"stop": False, "reason": ""}}
    scripts = {**OCCUPANCY, "coordinator": [OCCUPANCY["coordinator"][0], plan, plan, plan]}
    result, scripted, _ = run_fixture(v9_cfg, "controlled_remove_occupancy", tmp_path, scripts=scripts)
    g, r = result.graph, result.graph.result
    assert scripted.titles() == ["V9Propose", "V9Investigate", "V9Plan", "V9Critique", "V9Final"]
    assert g.questions["Q3"].status == "refused" and "repeats Q1" in g.questions["Q3"].answer_summary
    assert r.stop_reason == "converged" and r.budget_stop is False
    assert result.metrics["tool_calls"]["agent"] == 2


def test_a_question_whose_target_changed_is_investigated_again(v9_cfg, tmp_path):
    repeat = copy.deepcopy(OCCUPANCY["coordinator"][0]["questions"][0])
    repeat.update(target_claims=["C1"], hypotheses=["H1"])             # the same action, another target claim
    plan = {"hypothesis_updates": [], "assessments": [], "questions": [repeat], "stop": {"stop": False, "reason": ""}}
    stop = {"hypothesis_updates": [], "assessments": [], "questions": [], "stop": {"stop": True, "reason": "done"}}
    again = {"answers": [{**OCCUPANCY["computational_investigator"][0]["answers"][0], "question_id": "Q3",
                          "claim_ids": ["C1"], "proposed_updates": []}]}
    scripts = {**OCCUPANCY, "coordinator": [OCCUPANCY["coordinator"][0], plan, stop],
               "computational_investigator": [*OCCUPANCY["computational_investigator"], again]}
    result, scripted, _ = run_fixture(v9_cfg, "controlled_remove_occupancy", tmp_path, scripts=scripts)
    assert scripted.titles().count("V9Investigate") == 2 and result.graph.questions["Q3"].status == "unanswerable"
    assert result.metrics["tool_calls"]["agent"] == 2                 # the repeated request ran free


def unavailable_inventory() -> Fixture:
    fixture = load_fixture("synthetic_repair").model_dump(mode="json")
    fixture["tools"]["qbic_inventory"] = {
        "spec": {"route": "computational", "description": "Synthetic fixture inventory of model-sharing groups.",
                 "params": {}, "assemblies": [], "evidence_classes": ["synthetic"]},
        "responses": [{"params": {}, "execution_status": "cache_miss", "retrieval_status": "unknown",
                       "message": "precompute required: QBiC-SELEX statistics not cached for this variant"}]}
    return Fixture.model_validate(fixture)


def test_a_missing_inventory_is_shown_as_missing_data_in_every_packet(v9_cfg, tmp_path):
    _, scripted, _ = run_fixture(v9_cfg, unavailable_inventory(), tmp_path)
    for packet in scripted.packets():
        assert "QBiC-SELEX inventory unavailable" in packet and "precompute required" in packet
        assert "missing data, not evidence" in packet


def test_requests_and_graph_do_not_depend_on_the_hash_seed(v9_cfg, tmp_path):
    script = tmp_path / "seeded_run.py"
    script.write_text(
        "import hashlib, json, sys\n"
        "from pathlib import Path\n"
        "from variant2mechanism.config import load_config\n"
        "from tests.v9.test_engine_support import run_fixture\n"
        "out = Path(sys.argv[1])\n"
        "result, scripted, _ = run_fixture(load_config(), 'synthetic_repair', out, cache_dir=out / 'llm')\n"
        "usage = {k: {n: v for n, v in u.items() if n != 'latency_s'}\n"
        "         for k, u in result.metrics.pop('model_usage_by_role').items()}\n"
        "parts = [scripted.sent, json.loads(result.graph.to_json()), result.metrics, usage]\n"
        "print(json.dumps([hashlib.sha256(json.dumps(x, sort_keys=True).encode()).hexdigest() for x in parts]))\n")
    digests = set()
    for seed in ("0", "4242"):
        env = {**os.environ, "PYTHONHASHSEED": seed, "PYTHONDONTWRITEBYTECODE": "1",
               "PYTHONPATH": os.pathsep.join([str(REPO), os.environ.get("PYTHONPATH", "")])}
        done = subprocess.run([sys.executable, str(script), str(tmp_path / f"seed{seed}")], env=env, cwd=tmp_path,
                              capture_output=True, text=True, timeout=300)
        assert done.returncode == 0, done.stderr[-2000:]
        digests.add(done.stdout.strip().splitlines()[-1])
    assert len(digests) == 1, digests                                 # requests, graph, metrics (latency aside)
