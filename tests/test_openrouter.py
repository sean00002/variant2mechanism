"""The OpenRouter transport and the model client's request format, with a fake HTTP session."""

import json

import pytest
from fake_llm import message
from pydantic import BaseModel

from variant2mechanism.agent.llm import Budget, LLMClient, LLMError, LLMResult, MissingKey
from variant2mechanism.agent.openrouter import openrouter_transport
from variant2mechanism.config import ConfigError, load_config, with_profile

MODEL = "deepseek/deepseek-v4.1-flash-1017"


class FakeSession:
    def __init__(self, replies):
        self.replies, self.bodies = list(replies), []

    def post(self, url, headers, data, timeout):
        self.bodies.append(json.loads(data))
        status, body = self.replies.pop(0)

        class R:
            status_code = status
            text = json.dumps(body)

            def json(self):
                return body
        return R()


def test_missing_key_is_named_not_printed(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    with pytest.raises(MissingKey, match="OPENROUTER_API_KEY is not set"):
        openrouter_transport()


def test_transport_adds_routing_and_retries(monkeypatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    waits = []
    s = FakeSession([(429, {"error": {"code": 429, "message": "slow down"}}),
                     (200, {"error": {"code": 502, "message": "provider down"}}), (200, message("ok"))])
    out = openrouter_transport({"sort": "price"}, session=s, sleep=waits.append)({"model": MODEL, "messages": []})
    assert out["choices"][0]["message"]["content"] == "ok" and len(waits) == 2
    assert s.bodies[0]["usage"] == {"include": True}
    assert s.bodies[0]["provider"] == {"require_parameters": True, "sort": "price"}
    bad = FakeSession([(400, {"error": {"code": 400, "message": "invalid schema"}})])
    with pytest.raises(LLMError, match="OpenRouter error 400: invalid schema"):
        openrouter_transport(session=bad, sleep=lambda s: None)({"model": MODEL, "messages": []})


def test_tool_calls_and_echo():
    calls = [{"id": "c1", "type": "function", "function": {"name": "eqtl_lookup", "arguments": '{"tissue": null}'}},
             {"id": "c2", "type": "function", "function": {"name": "chip_peaks", "arguments": "{bad"}}]
    msg = message(None, "tool_calls", tool_calls=calls)["choices"][0]["message"]
    res = LLMResult(msg, "tool_calls", {}, 0.0, False)
    assert res.tool_calls[0] == {"id": "c1", "name": "eqtl_lookup", "input": {"tissue": None}}
    assert "_invalid_json" in res.tool_calls[1]["input"]
    echo = res.echo()
    assert echo["role"] == "assistant" and echo["tool_calls"] == calls and echo["reasoning_details"]


class Answer(BaseModel):
    tf: str


def test_client_request_cost_and_trace(monkeypatch, tmp_path):
    monkeypatch.setenv("OPENROUTER_API_KEY", "test-key")
    reply = message('{"tf": "GATA1"}', usage={"prompt_tokens": 1200, "completion_tokens": 300, "cost": 0.0031})
    session = FakeSession([(200, reply)])
    from variant2mechanism.agent import openrouter
    real = openrouter.openrouter_transport
    monkeypatch.setattr(openrouter, "openrouter_transport", lambda provider=None: real(provider, session=session))
    budget = Budget(tmp_path / "budget.json", {"dev": 0.5})
    llm = LLMClient(load_config(), cache_dir=tmp_path / "llm", budget=budget, trace_path=tmp_path / "trace.jsonl")
    res = llm.call("generator", "generate", "sys", [{"role": "user", "content": "q"}], output_model=Answer)
    assert res.parsed.tf == "GATA1" and res.cost == pytest.approx(0.0031) and res.provider == "Fake"
    assert budget.spent("dev") == pytest.approx(0.0031)
    body = session.bodies[0]
    assert body["model"] == MODEL and body["messages"][0] == {"role": "system", "content": "sys"}
    assert body["response_format"]["json_schema"]["strict"] and body["reasoning"] == {"effort": "medium"}
    trace = json.loads((tmp_path / "trace.jsonl").read_text())
    assert trace["provider"] == "Fake" and trace["finish_reason"] == "stop" and trace["input_tokens"] == 1200


def test_profile_merges_and_unknown_profile_fails():
    base = load_config()
    assert base["llm"]["generator"] == base["llm"]["critic"] == base["llm"]["summariser"] == MODEL
    cl = with_profile(base, "claude")
    assert cl["llm"]["generator"] == "anthropic/claude-opus-5" and cl["eval"]["runs_dir"] == "runs/eval_v2_claude"
    assert all(cl["llm"][r] in cl["llm"]["prices_per_mtok"] for r in ("generator", "critic", "summariser"))
    assert cl["eval"]["gold_set"] == base["eval"]["gold_set"]
    assert cl["budget_usd"]["state_file"] != base["budget_usd"]["state_file"]
    assert base["llm"]["generator"] == MODEL                           # the loaded config is not changed
    with pytest.raises(ConfigError, match="no profile"):
        with_profile(base, "nope")


def test_luna_profile_has_its_own_two_dollar_cap():
    lu = with_profile(load_config(), "luna")
    assert {lu["llm"][r] for r in ("generator", "critic", "summariser")} == {"openai/gpt-6-luna"}
    assert "openai/gpt-6-luna" in lu["llm"]["prices_per_mtok"] and lu["eval"]["runs_dir"] == "runs/eval_v6_luna"
    b = lu["budget_usd"]
    assert b["state_file"] == "state/budget_luna.json" and b["dev"] + b["eval"] + b["spare"] == pytest.approx(2.0)
