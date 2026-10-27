"""One model client (spec 2, section 7): role -> model, effort and max_tokens; response cache; trace; budget guard.

Every call is an OpenAI-style chat completion sent through OpenRouter (agent/openrouter.py), whatever the model.
Since 26 October 2026 the default is DeepSeek V4.1 Flash for every role and the Anthropic API is no longer called
directly. Structured output goes in `response_format` as a strict JSON schema and is validated here with Pydantic, so
a validation error can be sent back once.
"""

import fcntl
import hashlib
import json
import random
import threading
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ValidationError

from ..config import Config, load_config
from .schemas import SchemaCheckError

RETRY_STATUS = {429, 500, 502, 503, 504, 529}
TOOL_CALLS = "tool_calls"


class LLMError(RuntimeError):
    pass


class BudgetExceeded(LLMError):
    pass


class Refused(LLMError):
    pass


class MissingKey(LLMError):
    pass


@dataclass
class LLMResult:
    message: dict                       # the assistant message as returned (content, tool_calls, reasoning_details)
    finish_reason: str                  # stop, tool_calls, length or content_filter
    usage: dict
    cost: float
    cached: bool
    parsed: BaseModel | None = None
    model: str = ""
    provider: str | None = None         # the OpenRouter provider that served the call
    latency: float = 0.0
    retries: list[str] = field(default_factory=list)

    @property
    def text(self) -> str:
        return self.message.get("content") or ""

    @property
    def tool_calls(self) -> list[dict]:
        """[{id, name, input}]. Arguments that are not a JSON object become {"_invalid_json": ...}, which the
        investigate step answers with an error the model can correct."""
        out = []
        for tc in self.message.get("tool_calls") or []:
            raw = tc["function"].get("arguments") or "{}"
            try:
                args = json.loads(raw)
            except json.JSONDecodeError:
                args = None
            out.append({"id": tc["id"], "name": tc["function"]["name"],
                        "input": args if isinstance(args, dict) else {"_invalid_json": raw[:500]}})
        return out

    def echo(self) -> dict:
        """The assistant turn to send back: content and tool calls, with reasoning_details passed back unchanged."""
        turn = {"role": "assistant", "content": self.message.get("content")}
        for key in ("tool_calls", "reasoning_details"):
            if self.message.get(key):
                turn[key] = self.message[key]
        return turn


# -- strict JSON schemas --------------------------------------------------------------------------------------

STRING_FORMATS = {"date-time", "time", "date", "duration", "email", "hostname", "uri", "ipv4", "ipv6", "uuid"}


def strict_schema(model: type[BaseModel] | dict) -> dict:
    """A Pydantic model's JSON schema in strict form: every object closed (additionalProperties false), only the
    keywords strict structured output accepts, and anything else moved into the description as a hint. It follows
    the rules of the Anthropic SDK's transform_schema, so the schemas are the ones the earlier runs sent."""
    schema = dict(model.model_json_schema() if isinstance(model, type) else model)
    out: dict[str, Any] = {}
    defs = schema.pop("$defs", None)
    if defs is not None:
        out["$defs"] = {name: strict_schema(d) for name, d in defs.items()}
    ref = schema.pop("$ref", None)
    if ref is not None:
        out["$ref"] = ref
        return out
    kind = schema.pop("type", None)
    any_of, one_of, all_of = schema.pop("anyOf", None), schema.pop("oneOf", None), schema.pop("allOf", None)
    if any_of or one_of:
        out["anyOf"] = [strict_schema(v) for v in (any_of or one_of)]
    elif all_of:
        out["allOf"] = [strict_schema(v) for v in all_of]
    elif kind is None:
        raise ValueError("a schema needs 'type', 'anyOf', 'oneOf' or 'allOf'")
    else:
        out["type"] = kind
    for key in ("enum", "description", "title"):
        if schema.get(key) is not None:
            out[key] = schema.pop(key)
    if kind == "object":
        out["properties"] = {k: strict_schema(v) for k, v in schema.pop("properties", {}).items()}
        schema.pop("additionalProperties", None)
        out["additionalProperties"] = False
        if schema.get("required") is not None:
            out["required"] = schema.pop("required")
    elif kind == "string" and schema.get("format") in STRING_FORMATS:
        out["format"] = schema.pop("format")
    elif kind == "array":
        if schema.get("items") is not None:
            out["items"] = strict_schema(schema.pop("items"))
        if schema.get("minItems") in (0, 1):
            out["minItems"] = schema.pop("minItems")
    if schema:                          # unsupported keywords: a hint in the description the model may follow
        hint = "{" + ", ".join(f"{k}: {v}" for k, v in schema.items()) + "}"
        out["description"] = (out["description"] + "\n\n" if out.get("description") else "") + hint
    return out


# -- budget ---------------------------------------------------------------------------------------------------


class Budget:
    """Spend per phase in a state file. Reserve the worst case before a call; settle with the real cost after.

    One lock per process (threads) plus a file lock (processes).
    """
    _lock = threading.Lock()

    def __init__(self, path: Path, limits: dict[str, float]):
        self.path, self.limits = Path(path), limits

    @contextmanager
    def _locked(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._lock, open(str(self.path) + ".lock", "w") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            try:
                state = json.loads(self.path.read_text()) if self.path.exists() else {}
                yield state
                self.path.write_text(json.dumps(state, indent=1))
            finally:
                fcntl.flock(lk, fcntl.LOCK_UN)

    def reserve(self, phase: str, amount: float) -> str:
        with self._locked() as st:
            p = st.setdefault(phase, {"spent": 0.0, "reserved": {}})
            held = sum(p["reserved"].values())
            limit = float(self.limits[phase])
            if p["spent"] + held + amount > limit + 1e-9:
                raise BudgetExceeded(f"{phase} budget ${limit:.2f}: spent ${p['spent']:.4f}, held ${held:.4f}; "
                                     f"this call could cost up to ${amount:.4f}. Raise budget_usd.{phase} in config.yaml to continue.")
            rid = f"{time.time_ns()}-{random.randrange(1 << 30)}"
            p["reserved"][rid] = amount
            return rid

    def settle(self, phase: str, rid: str, actual: float) -> None:
        with self._locked() as st:
            p = st.setdefault(phase, {"spent": 0.0, "reserved": {}})
            p["reserved"].pop(rid, None)
            p["spent"] = round(p["spent"] + actual, 6)

    def spent(self, phase: str) -> float:
        with self._locked() as st:
            return st.get(phase, {}).get("spent", 0.0)


# -- client ---------------------------------------------------------------------------------------------------


class LLMClient:
    def __init__(self, cfg: Config | None = None, transport=None, phase: str = "dev", trace_path: Path | None = None,
                 seed: int = 0, cache_dir: Path | None = None, budget: Budget | None = None):
        self.cfg = cfg or load_config()
        self._transport = transport
        self.phase, self.seed = phase, seed
        self.trace_path = trace_path
        self.cache_dir = cache_dir or self.cfg.path("tools", "http_cache").parent / "llm"
        b = self.cfg["budget_usd"]
        self.budget = budget or Budget(self.cfg.path("budget_usd", "state_file"),
                                       {k: v for k, v in b.items() if isinstance(v, int | float)})
        self.total_cost = 0.0
        self.calls = 0

    @property
    def transport(self):
        if self._transport is None:
            from .openrouter import openrouter_transport
            self._transport = openrouter_transport((self.cfg["llm"].get("openrouter") or {}).get("provider"))
        return self._transport

    def role(self, role: str) -> tuple[str, str, int]:
        llm = self.cfg["llm"]
        return llm[role], llm["effort"][role], int(llm["max_tokens"][role])

    def price(self, model: str, usage: dict) -> float:
        """What OpenRouter reports it charged; list prices only when a reply carries no cost (as in tests)."""
        if usage.get("cost") is not None:
            return float(usage["cost"])
        p = self.cfg["llm"]["prices_per_mtok"][model]
        return (usage.get("prompt_tokens", 0) * p["input"] + usage.get("completion_tokens", 0) * p["output"]) / 1e6

    def worst_case(self, model: str, body: dict) -> float:
        p = self.cfg["llm"]["prices_per_mtok"][model]
        chars = len(json.dumps(body["messages"])) + len(json.dumps(body.get("tools", [])))
        return chars / 3.5 * p["input"] / 1e6 + body["max_tokens"] * p["output"] / 1e6

    def call(self, role: str, stage: str, system: str, messages: list[dict], tools: list[dict] | None = None,
             output_model: type[BaseModel] | None = None, check=None) -> LLMResult:
        """One model call. With `output_model`, the JSON is validated (and `check(parsed)` run); one retry with the
        error message, then the stage fails loudly."""
        res = self._call(role, stage, system, messages, tools, output_model)
        if output_model is None:
            return res
        try:
            res.parsed = self._parse(res, output_model, check)
            return res
        except (ValidationError, SchemaCheckError, json.JSONDecodeError) as e:
            err = str(e)[:1500]
        retry_msgs = messages + [res.echo(), {"role": "user", "content": f"That output failed validation: {err}\n"
                                                                         "Return the corrected JSON in full."}]
        res2 = self._call(role, stage, system, retry_msgs, tools, output_model)
        try:
            res2.parsed = self._parse(res2, output_model, check)
        except (ValidationError, SchemaCheckError, json.JSONDecodeError) as e:
            raise LLMError(f"{stage}: output failed validation twice: {str(e)[:600]}") from None
        res2.cost += res.cost
        res2.retries = res.retries + ["validation"] + res2.retries
        return res2

    @staticmethod
    def _parse(res: LLMResult, output_model, check):
        parsed = output_model.model_validate_json(res.text)
        return check(parsed) if check else parsed

    def _call(self, role, stage, system, messages, tools, output_model, max_tokens=None, _retried=False) -> LLMResult:
        model, effort, mt = self.role(role)
        body: dict[str, Any] = {"model": model, "messages": ([{"role": "system", "content": system}] if system else [])
                                + messages, "max_tokens": max_tokens or mt, "reasoning": {"effort": effort}}
        if tools:
            body["tools"] = tools
        if output_model is not None:
            body["response_format"] = {"type": "json_schema", "json_schema": {"name": "output", "strict": True,
                                                                              "schema": strict_schema(output_model)}}
        key = hashlib.sha256(json.dumps({**body, "seed": self.seed}, sort_keys=True, default=str).encode()).hexdigest()
        path = self.cache_dir / f"{key}.json"
        t0 = time.time()
        if path.exists():
            resp, cached, cost = json.loads(path.read_text()), True, 0.0
        else:
            rid = self.budget.reserve(self.phase, self.worst_case(model, body))
            try:
                resp = self.transport(body)
            except Exception:
                self.budget.settle(self.phase, rid, 0.0)
                raise
            cost = self.price(model, resp.get("usage") or {})
            self.budget.settle(self.phase, rid, cost)
            cached = False
        choice = resp["choices"][0]
        message = choice.get("message") or {}
        finish = choice.get("finish_reason") or "stop"
        if message.get("tool_calls") and finish == "stop":          # some providers report "stop" with tool calls
            finish = TOOL_CALLS
        if not cached and finish not in ("length", "content_filter"):
            self.cache_dir.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(resp))
        res = LLMResult(message, finish, resp.get("usage") or {}, cost, cached, model=resp.get("model") or model,
                        provider=resp.get("provider"), latency=round(time.time() - t0, 2))
        self._trace(stage, role, res, body["max_tokens"])
        self.total_cost += cost
        self.calls += 1
        if finish == "content_filter":
            raise Refused(f"{stage}: the provider's content filter stopped the reply; the stage stops here.")
        if finish == "length":
            if _retried:
                raise LLMError(f"{stage}: hit max_tokens twice ({body['max_tokens']})")
            again = self._call(role, stage, system, messages, tools, output_model, body["max_tokens"] * 2, True)
            again.cost += res.cost
            again.retries = ["max_tokens"] + again.retries
            return again
        return res

    def _trace(self, stage: str, role: str, res: LLMResult, max_tokens: int) -> None:
        if not self.trace_path:
            return
        u = res.usage
        line = {"stage": stage, "role": role, "model": res.model, "provider": res.provider,
                "input_tokens": u.get("prompt_tokens"), "output_tokens": u.get("completion_tokens"),
                "thinking_tokens": (u.get("completion_tokens_details") or {}).get("reasoning_tokens"),
                "cache_read_tokens": (u.get("prompt_tokens_details") or {}).get("cached_tokens"),
                "cost_usd": round(res.cost, 6), "latency_s": res.latency, "finish_reason": res.finish_reason,
                "cache_hit": res.cached, "max_tokens": max_tokens}
        with open(self.trace_path, "a") as f:
            f.write(json.dumps(line) + "\n")
