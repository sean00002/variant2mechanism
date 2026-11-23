"""Shared helpers for the engine tests (no tests here): a scripted model client and a fixture engine run.

The model is never called: LLMClient gets a transport built from a fixture's "roles" scripts
(ScriptedResponses.transport, dispatched by roles.script_role on the response schema title and the packet's role line),
a currency budget of its own in the test's temporary folder, and the isolated config, so replies are cached in temp.
"""

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from variant2mechanism.agent.llm import Budget, LLMClient
from variant2mechanism.v9 import roles
from variant2mechanism.v9.fixtures import Fixture, FixtureToolRunner, ScriptedResponses, load_fixture
from variant2mechanism.v9.graph import GroupRegistry, SymbolResolver
from variant2mechanism.v9.investigate import Engine, EngineLimits, EngineResult, fixture_facts
from variant2mechanism.v9.tools import ToolLimits


class Scripted:
    """A scripted LLMClient: `sent` holds every request body, `responses.served` the scripted replies used.
    `alter(role, index, reply)` may change a reply before it is returned (e.g. a max_tokens finish)."""

    def __init__(self, cfg, scripts: dict[str, list[Any]], *, alter: Callable[[str, int, dict], dict] | None = None,
                 on_send: Callable[[dict], None] | None = None, budget_usd: float = 100.0,
                 cache_dir: Path | None = None):
        self.responses = ScriptedResponses(scripts)
        self.sent: list[dict] = []
        send = self.responses.transport(roles.script_role)

        def transport(body: dict) -> dict:
            self.sent.append(json.loads(json.dumps(body)))
            if on_send is not None:
                on_send(body)
            reply = send(body)
            role, index = self.responses.served[-1]
            return alter(role, index, reply) if alter else reply

        budget = Budget(cfg.path("budget_usd", "state_file"), {"dev": budget_usd})
        self.client = LLMClient(cfg, transport=transport, phase="dev", budget=budget, cache_dir=cache_dir)

    def titles(self) -> list[str]:
        return [b["response_format"]["json_schema"]["schema"]["title"] for b in self.sent]

    def packets(self) -> list[str]:
        """The first user message of every request (the packet)."""
        return [next(m["content"] for m in b["messages"] if m["role"] == "user") for b in self.sent]


def run_fixture(cfg, fixture: str | Fixture, tmp_path: Path, *, scripts: dict | None = None,
                limits: EngineLimits | None = None, clock: Callable[[], float] | None = None,
                groups: GroupRegistry | None = None, alter=None, on_send=None, budget_usd: float = 100.0,
                tool_limits: ToolLimits | None = None, facts=fixture_facts,
                cache_dir: Path | None = None) -> tuple[EngineResult, Scripted, roles.RoleCaller]:
    """Run the engine on a fixture with scripted roles; returns (result, the scripted client, the role caller).
    Limits default to the SPEC 13.9 defaults (EngineLimits()), whatever config.yaml's v9 block says. Replies are
    cached in the isolated config's model cache unless `cache_dir` names another folder."""
    fixture = fixture if isinstance(fixture, Fixture) else load_fixture(fixture)
    scripted = Scripted(cfg, scripts if scripts is not None else fixture.roles, alter=alter, on_send=on_send,
                        budget_usd=budget_usd, cache_dir=cache_dir)
    caller = roles.RoleCaller(scripted.client, cfg)
    run_dir = tmp_path / "run"
    runner = FixtureToolRunner(fixture, run_dir=run_dir, limits=tool_limits)
    engine = Engine(cfg, "fixture", caller, runner, run_dir, limits=limits or EngineLimits(), facts=facts,
                    resolver=SymbolResolver({}), groups=groups or GroupRegistry({}), clock=clock or (lambda: 0.0))
    return engine.run(fixture.case), scripted, caller


def events(result: EngineResult, action: str) -> list:
    return [e for e in result.graph.events if e.action == action]


def decided_alone(result: EngineResult, outcome: str | None = None) -> None:
    """A run decided without a final comparison names no hypothesis (leading_ids empty, nothing leading or tied, no
    comparison stored), and its result, metrics and manifest agree on the outcome and the stop."""
    g, r, m = result.graph, result.graph.result, result.metrics
    assert r.leading_ids == [] and not g.comparisons
    assert not [h for h in g.hypotheses.values() if h.disposition in ("leading", "tied")]
    assert (m["outcome"], m["stop_reason"], m["budget_stop"]) == (r.outcome, r.stop_reason, r.budget_stop)
    assert result.manifest_parts["stop_reason"] == r.stop_reason
    if outcome is not None:
        assert r.outcome == m["outcome"] == outcome
