"""The Anthropic API transport and the opus5_v8 profile, with a fake SDK client: a chat-completions body in, the same
form out, so the client's cache, budget and trace are unchanged."""

import json
from types import SimpleNamespace as NS

import anthropic
import httpx2
import pytest
from pydantic import BaseModel

from variant2mechanism.agent.anthropic_api import anthropic_transport
from variant2mechanism.agent.llm import Budget, LLMClient, LLMError, MissingKey, Refused
from variant2mechanism.config import load_config, with_profile

MODEL = "claude-opus-5"


class FakeClient:
    """`client.messages.stream(**params)` as the SDK has it: a context manager whose final message is the reply."""

    def __init__(self, *replies):
        self.replies, self.params = list(replies), []
        self.messages = self

    def stream(self, **params):
        self.params.append(params)
        reply = self.replies.pop(0)

        class Stream:
            def __enter__(self):
                if isinstance(reply, Exception):
                    raise reply
                return self

            def __exit__(self, *exc):
                return False

            def get_final_message(self):
                return reply
        return Stream()


def reply(text, stop="end_turn", details=None):
    usage = NS(input_tokens=1000, output_tokens=400, cache_read_input_tokens=0, cache_creation_input_tokens=0,
               output_tokens_details=NS(thinking_tokens=120))
    return NS(id="msg_1", model=MODEL, content=[NS(type="thinking", thinking=""), NS(type="text", text=text)],
              stop_reason=stop, stop_details=details, usage=usage)


class Answer(BaseModel):
    tf: str


def client(monkeypatch, tmp_path, fake):
    from variant2mechanism.agent import anthropic_api
    real = anthropic_api.anthropic_transport
    monkeypatch.setattr(anthropic_api, "anthropic_transport", lambda: real(client=fake))
    return LLMClient(with_profile(load_config(), "opus5_v8"), cache_dir=tmp_path / "llm",
                     budget=Budget(tmp_path / "budget.json", {"dev": 1.0}), trace_path=tmp_path / "trace.jsonl")


def test_missing_key_is_named_not_printed(monkeypatch):
    monkeypatch.delenv("V2M_ANTHROPIC_API_KEY", raising=False)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "another-tools-key")       # the shared name is never read
    with pytest.raises(MissingKey, match="V2M_ANTHROPIC_API_KEY is not set"):
        anthropic_transport()


def test_a_chat_body_becomes_a_messages_request_and_comes_back(monkeypatch, tmp_path):
    fake = FakeClient(reply('{"tf": "GATA1"}'))
    res = client(monkeypatch, tmp_path, fake).call("generator", "generate", "sys", [{"role": "user", "content": "q"}],
                                                   output_model=Answer)
    p = fake.params[0]
    assert p["model"] == MODEL and p["system"] == "sys" and p["messages"] == [{"role": "user", "content": "q"}]
    assert p["max_tokens"] == 32000 and p["output_config"]["effort"] == "medium"
    assert p["output_config"]["format"]["type"] == "json_schema" and not p["output_config"]["format"]["schema"][
        "additionalProperties"]
    assert not {"thinking", "temperature", "reasoning", "response_format"} & set(p)
    assert res.parsed.tf == "GATA1" and res.provider == "Anthropic API" and res.model == MODEL
    assert res.cost == pytest.approx((1000 * 5.0 + 400 * 25.0) / 1e6)              # list prices: no cost is reported
    trace = json.loads((tmp_path / "trace.jsonl").read_text())
    assert (trace["input_tokens"], trace["output_tokens"], trace["thinking_tokens"]) == (1000, 400, 120)
    assert trace["finish_reason"] == "stop" and trace["provider"] == "Anthropic API"


def test_max_tokens_doubles_and_a_refusal_names_its_category(monkeypatch, tmp_path):
    refusal = reply("", "refusal", NS(category="bio", explanation="declined by the classifier"))
    fake = FakeClient(reply('{"tf": "SP', "max_tokens"), reply('{"tf": "SPI1"}'), refusal)
    llm = client(monkeypatch, tmp_path, fake)
    res = llm.call("critic", "critique", "s", [{"role": "user", "content": "x"}], output_model=Answer)
    assert res.parsed.tf == "SPI1" and [p["max_tokens"] for p in fake.params] == [16000, 32000]
    with pytest.raises(Refused, match=r"content filter stopped the reply \(bio: declined by the classifier\)"):
        llm.call("critic", "critique", "s", [{"role": "user", "content": "y"}])
    assert len(list((tmp_path / "llm").glob("*.json"))) == 1          # neither the cut-off reply nor the refusal


def test_tools_and_api_errors_fail_loudly():
    with pytest.raises(LLMError, match="text stages only"):
        anthropic_transport(client=FakeClient())({"model": MODEL, "max_tokens": 10, "messages": [],
                                                  "tools": [{"type": "function"}]})
    req = httpx2.Request("POST", "https://api.anthropic.com/v1/messages")
    down = anthropic.InternalServerError("overloaded", response=httpx2.Response(529, request=req), body=None)
    body = {"model": MODEL, "max_tokens": 10, "messages": [{"role": "user", "content": "x"}]}
    with pytest.raises(LLMError, match="Anthropic API error 529: overloaded"):
        anthropic_transport(client=FakeClient(down))(body)
    with pytest.raises(LLMError, match=r"call failed \(APIConnectionError\)"):
        anthropic_transport(client=FakeClient(anthropic.APIConnectionError(request=req)))(body)


def test_the_opus5_profile_calls_the_anthropic_api_with_its_own_folders_and_cap():
    base = load_config()
    op = with_profile(base, "opus5_v8")
    assert op["llm"]["api"] == "anthropic" and base["llm"]["api"] == "openrouter"
    assert {op["llm"][r] for r in ("generator", "critic", "summariser")} == {MODEL}
    assert op["llm"]["prices_per_mtok"][MODEL] == {"input": 5.0, "output": 25.0}
    assert op["v8"]["runs_dir"] == "runs/eval_v8_opus5" and op["budget_usd"]["state_file"] == "state/budget_v8_opus5.json"
    assert op["budget_usd"]["eval"] == 14.0 and op["budget_usd"]["dev"] == 0.0


def cached_reply(text, fresh, read=0, written=0, model="claude-sonnet-5-5"):
    usage = NS(input_tokens=fresh, output_tokens=100, cache_read_input_tokens=read,
               cache_creation_input_tokens=written, output_tokens_details=None)
    return NS(id="msg_2", model=model, content=[NS(type="text", text=text)], stop_reason="end_turn",
              stop_details=None, usage=usage)


def test_the_fills_critic_caches_its_instructions_and_pays_the_cache_prices(monkeypatch, tmp_path):
    """The critic's client sends the same instructions with every record. They are marked for the API's prompt
    cache; the tokens written to it and read from it are charged at the model's own prices for them."""
    from variant2mechanism.agent import anthropic_api
    from variant2mechanism.v9 import critic as K
    real = anthropic_api.anthropic_transport
    fake = FakeClient(cached_reply("a", 1500, written=3000), cached_reply("b", 1400, read=3000))
    monkeypatch.setattr(anthropic_api, "anthropic_transport", lambda **kw: real(client=fake, **kw))
    cfg = K.critic_config(load_config())
    assert cfg["llm"]["cache_system"] is True and "cache_system" not in load_config()["llm"]
    llm = LLMClient(cfg, cache_dir=tmp_path / "llm", budget=Budget(tmp_path / "budget.json", {"dev": 1.0}),
                    trace_path=tmp_path / "trace.jsonl")
    first = llm.call(K.LLM_KEY, "check", "the instructions", [{"role": "user", "content": "record 1"}])
    second = llm.call(K.LLM_KEY, "check", "the instructions", [{"role": "user", "content": "record 2"}])
    marked = [{"type": "text", "text": "the instructions", "cache_control": {"type": "ephemeral"}}]
    assert [p["system"] for p in fake.params] == [marked, marked]
    assert first.usage["prompt_tokens"] == 4500 and second.usage["prompt_tokens"] == 4400
    assert first.usage["prompt_tokens_details"] == {"cached_tokens": 0, "cache_write_tokens": 3000}
    assert second.usage["prompt_tokens_details"] == {"cached_tokens": 3000}
    assert first.cost == pytest.approx((1500 * 2.0 + 3000 * 2.5 + 100 * 10.0) / 1e6)
    assert second.cost == pytest.approx((1400 * 2.0 + 3000 * 0.10 + 100 * 10.0) / 1e6)
    one, two = (json.loads(line) for line in (tmp_path / "trace.jsonl").read_text().splitlines())
    assert (one["input_tokens"], one["cache_read_tokens"], one["cache_write_tokens"]) == (4500, 0, 3000)
    assert (two["input_tokens"], two["cache_read_tokens"]) == (4400, 3000) and "cache_write_tokens" not in two


def test_without_the_setting_nothing_is_marked_and_cached_tokens_cost_the_input_price(monkeypatch, tmp_path):
    fake = FakeClient(cached_reply("x", 1000, read=2000, written=500, model=MODEL))
    res = client(monkeypatch, tmp_path, fake).call("generator", "generate", "sys", [{"role": "user", "content": "q"}])
    assert fake.params[0]["system"] == "sys"
    assert res.cost == pytest.approx((3500 * 5.0 + 100 * 25.0) / 1e6)      # the model's entry has no cache prices


def test_the_response_cache_key_is_the_same_with_and_without_the_prompt_cache(monkeypatch, tmp_path):
    """Marking the instructions changes what a call costs, not what is asked: a reply saved without the mark
    answers the same call with it."""
    from variant2mechanism.agent import anthropic_api
    from variant2mechanism.v9 import critic as K
    real = anthropic_api.anthropic_transport
    fake = FakeClient(cached_reply("a", 1500))
    monkeypatch.setattr(anthropic_api, "anthropic_transport", lambda **kw: real(client=fake, **kw))
    cfg = K.critic_config(load_config())
    plain = type(cfg)({**cfg, "llm": {**cfg["llm"], "cache_system": False}})
    keys = []
    for config in (plain, cfg):
        llm = LLMClient(config, cache_dir=tmp_path / "llm", budget=Budget(tmp_path / "budget.json", {"dev": 1.0}),
                        trace_path=tmp_path / "trace.jsonl")
        keys.append(llm.call(K.LLM_KEY, "check", "the instructions", [{"role": "user", "content": "record"}]).cached)
    assert keys == [False, True] and len(fake.params) == 1 and fake.params[0]["system"] == "the instructions"
