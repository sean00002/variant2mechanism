"""Synthetic fixtures: a tool backend and scripted role outputs for tests and the synthetic demo (SPEC 11).

Why: the graph's repair, rejection and dependency rules must be shown on data whose truth is stipulated, so a test
can say exactly what should happen. A fixture file is one JSON document:

    {"description": "...",
     "case": {Case: case_id starting "SYN-"},
     "retrieval_time": "<ISO time stamped on every fixture call>",
     "tools": {"<tool name>": {"spec": {ToolSpec fields except name},
                               "responses": [{"params": {...}, "execution_status": ..., "retrieval_status": ...,
                                              "observations": [...], "coverage": {...}, "message": "...",
                                              "evidence": [Evidence with evidence_id ""], "raw": ...}]}},
     "roles": {"<role>": [<role output as JSON text or object>, ...]}}

FixtureToolRunner answers each request from "tools" by (tool, canonical params), through the same ToolRunner
contract as live adapters (validation, dedupe, budgets, raw files, evidence rules). ScriptedResponses answers model
calls from "roles" in call order per role. Fixture evidence has origin "fixture"; the graph admits it, and the
"synthetic" evidence class, only in SYN- cases, so fixture data can never reach a biological result.
"""

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from pydantic import Field, model_validator

from .schemas import Case, Coverage, Evidence, ExecutionStatus, ParamValue, RetrievalStatus, V9Model
from .tools import (
    AdapterResult,
    ToolContext,
    ToolLimits,
    ToolRegistry,
    ToolRunner,
    ToolSpec,
    canonical_key,
    canonical_params,
)

FIXTURE_DIR = Path(__file__).with_name("fixtures")


class FixtureResponse(V9Model):
    params: dict[str, ParamValue] = Field(default_factory=dict)
    execution_status: ExecutionStatus = "success"
    retrieval_status: RetrievalStatus = "records_found"
    observations: list[dict[str, Any]] = Field(default_factory=list)
    coverage: Coverage = Field(default_factory=Coverage)
    message: str = ""
    evidence: list[Evidence] = Field(default_factory=list)
    raw: Any = None


class FixtureTool(V9Model):
    spec: dict[str, Any]                         # ToolSpec fields except name (the key in "tools")
    responses: list[FixtureResponse] = Field(default_factory=list)


class Fixture(V9Model):
    description: str
    case: Case
    retrieval_time: str = "2026-11-08T00:00:00+00:00"
    tools: dict[str, FixtureTool] = Field(default_factory=dict)
    roles: dict[str, list[Any]] = Field(default_factory=dict)

    @model_validator(mode="after")
    def _synthetic_only(self) -> "Fixture":
        if not self.case.synthetic:
            raise ValueError(f"fixture case ids start with SYN- (got {self.case.case_id})")
        for name, tool in self.tools.items():
            for r in tool.responses:
                if any(e.origin != "fixture" for e in r.evidence):
                    raise ValueError(f"fixture tool {name}: every evidence item has origin 'fixture'")
        return self

    def tool_specs(self) -> list[ToolSpec]:
        return [ToolSpec.model_validate({**tool.spec, "name": name}) for name, tool in sorted(self.tools.items())]


def load_fixture(name_or_path: str | Path) -> Fixture:
    """A fixture by path, or by name from v9/fixtures/ (e.g. "synthetic_repair")."""
    path = Path(name_or_path)
    if not path.exists():
        path = FIXTURE_DIR / f"{name_or_path}.json"
    return Fixture.model_validate_json(path.read_text())


class FixtureToolRunner(ToolRunner):
    """Answers tool requests from a fixture's stipulated responses. A request the fixture does not script gives
    execution_status "cache_miss"; a non-synthetic case is refused, so fixtures never answer biological runs."""

    def __init__(self, fixture: Fixture | str | Path, *, run_dir: str | Path | None = None,
                 limits: ToolLimits | None = None, allowed_tools: list[str] | None = None,
                 clock: Callable[[], str] | None = None):
        self.fixture = fixture if isinstance(fixture, Fixture) else load_fixture(fixture)
        registry = ToolRegistry()
        for spec in self.fixture.tool_specs():
            registry.register(spec, None)
        super().__init__(mode="fixture", run_dir=run_dir, limits=limits, registry=registry,
                         allowed_tools=allowed_tools, clock=clock or (lambda: self.fixture.retrieval_time))
        self._responses: dict[str, FixtureResponse] = {}
        for spec in self.fixture.tool_specs():
            for r in self.fixture.tools[spec.name].responses:
                key = canonical_key(spec.name, canonical_params(spec, r.params))
                if key in self._responses:
                    raise ValueError(f"fixture tool {spec.name}: two responses for the same parameters")
                self._responses[key] = r

    def _execute(self, spec: ToolSpec, params: dict[str, ParamValue], ctx: ToolContext) -> AdapterResult:
        if not ctx.case.synthetic:
            return AdapterResult(execution_status="not_applicable",
                                 message="fixture tools answer synthetic cases (SYN-) only")
        r = self._responses.get(canonical_key(spec.name, params))
        if r is None:
            return AdapterResult(execution_status="cache_miss", message="the fixture has no response for these "
                                                                        "parameters")
        raw = r.raw if r.raw is not None else {"fixture": ctx.case.case_id, "tool": spec.name, "params": params,
                                               "observations": r.observations}
        return AdapterResult(execution_status=r.execution_status, retrieval_status=r.retrieval_status,
                             observations=[dict(o) for o in r.observations], coverage=r.coverage,
                             evidence=[e.model_copy(deep=True) for e in r.evidence], raw=raw, message=r.message,
                             cached=True)


class ScriptExhausted(LookupError):
    """A role was called more often than its script has outputs."""


class ScriptedResponses:
    """Pre-written role outputs, answered per (role, call index). Objects are stored as canonical JSON text, so the
    same script always yields the same strings. The engine validates them with the role's output schema and counts
    each as a model call costing nothing."""

    def __init__(self, scripts: dict[str, list[Any]]):
        self._scripts = {role: [s if isinstance(s, str) else json.dumps(s, sort_keys=True) for s in items]
                         for role, items in sorted(scripts.items())}
        self._next: dict[str, int] = {role: 0 for role in self._scripts}
        self.served: list[tuple[str, int]] = []

    @classmethod
    def from_fixture(cls, fixture: Fixture | str | Path) -> "ScriptedResponses":
        fixture = fixture if isinstance(fixture, Fixture) else load_fixture(fixture)
        return cls(fixture.roles)

    def get(self, role: str, index: int) -> str:
        """The output scripted for the index-th call (0-based) of a role."""
        items = self._scripts.get(role, [])
        if not 0 <= index < len(items):
            raise ScriptExhausted(f"no scripted output for {role} call {index + 1} (the script has {len(items)})")
        return items[index]

    def next(self, role: str) -> str:
        """The next output for a role, in call order."""
        index = self._next.get(role, 0)
        text = self.get(role, index)
        self._next[role] = index + 1
        self.served.append((role, index))
        return text

    def remaining(self, role: str) -> int:
        return len(self._scripts.get(role, [])) - self._next.get(role, 0)

    def transport(self, role_of: Callable[[dict], str]) -> Callable[[dict], dict]:
        """An LLMClient transport (request body -> chat-completions reply) answering from the script; `role_of`
        maps a request body to its role (roles.py knows which output schema belongs to which role)."""
        def send(body: dict) -> dict:
            role = role_of(body)
            index = self._next.get(role, 0)
            text = self.next(role)
            return {"id": f"scripted-{role}-{index}", "model": body.get("model", "scripted"), "provider": "Scripted",
                    "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": text}}],
                    "usage": {"prompt_tokens": 0, "completion_tokens": 0, "cost": 0.0}}
        return send
