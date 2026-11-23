"""The v9 engine: one bounded investigation over one claim graph (SPEC 6 with 13.5, 13.8, 13.9; contract C4).

Why it is built this way:
- Code does everything that is not a scientific judgement: normalising the input, collecting facts, running tools,
  applying proposals through the graph's gates, propagating dependencies, keeping budgets and deciding when to stop.
  The four model roles only propose, through roles.RoleCaller, and every decision is recorded as a graph event.
- Steps: normalise -> collect facts (code) -> propose (coordinator) -> rounds of [run the open questions' actions ->
  computational investigator -> literature investigator -> coordinator plan] -> audit (critic) -> final comparison
  (critic) -> compare.decide. A failed initial proposal is retried once as a proposal (it is not a regeneration).
  With no active hypothesis left, the coordinator regenerates (at most `max_regenerations` times, default 1); the
  graph refuses any story whose structure was rejected. A coordinator's stop is honoured only while a hypothesis is
  active: deferring the last active hypotheses leads to a regeneration, and the audit then sees the deferred ones
  (deferral is a priority decision, never a refutation; the critic can bring back those still reportable).
- The audit may reopen the investigation once: a regeneration when no active hypothesis is reportable (the
  non-reportable ones are deferred by code first, so the new sketches get the active slots, and come back if the
  regeneration leaves nothing active), or one more round for consequential challenges that request actions.
- A question that repeats one already answered (same route, tool requests and target claims, none of which changed
  since) is closed without a model call, so rounds that cannot make progress end the run instead of spending its
  budget.
- Every resource is a cap, never a target: model sends (4-send guard; a reserve kept for the final comparison), agent
  tool calls, full-text reads, the currency budget and wall time on an injected clock. A budget stop keeps the
  scientific state and is disclosed as budget_stop; without a final comparison, compare.py decides from the graph.
- A replay must reproduce the run or fail loudly: when a model reply or a tool result is not in the saved run, the run
  stops with cache_miss before anything else is decided. manifest_parts says whether the run can be replayed at all
  (a max_tokens retry, a refusal, a provider error, a wall-time or currency stop cannot be).
- A run that could not investigate never reports a scientific outcome: an internal error, no usable proposal, or a
  failed plan with nothing left to run ends it with engine_error, and compare.py reports
  input_or_capability_limitation.
- Investigators run one after another (computational, then literature): LLMClient's counters and the HTTP session
  are not thread-safe, and a fixed order keeps a replay identical.
- Missing data never stops, rejects or defers anything here: an empty retrieval leaves a question unanswerable.
- A rejection must keep its basis: when the contradiction that made code reject a hypothesis is withdrawn (a misread
  passage relinked as context only, a reassessment), code reinstates it as deferred, once (graph.reinstate), after the
  round, plan or audit that withdrew it; a stale rejection the graph keeps is disclosed instead.
- `run` never raises: a failed model call is logged (its kind in the event text, the provider's message only in the
  event details) and the run goes on or stops cleanly; a result is always set. The engine writes no bundle.
"""

import importlib
import logging
import time
from collections import Counter
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from functools import cache
from pathlib import Path
from typing import Any

from .. import config as config_module
from . import ENGINE_VERSION, adoption, chain, compare, progress
from . import roles as R
from .graph import (
    ClaimGraph,
    GraphRefusal,
    GraphUpdate,
    GroupRegistry,
    HypothesisDraft,
    SymbolResolver,
    sketched_groups,
)
from .resolution import support_summary
from .roles import RoleCaller, V9Critique, V9Final, V9HypothesisUpdate, V9Investigate, V9Plan, V9Propose
from .schemas import (
    Case,
    EventAction,
    ExperimentRecord,
    InferredCandidate,
    Question,
    Role,
    RunMode,
    RunResult,
    StopReason,
    ToolCall,
    ToolRequest,
    V9Model,
)
from .tools import ToolLimits, ToolRefusal, ToolRunner, canonical_key, canonical_params

log = logging.getLogger(__name__)

ROUTES = ("computational", "literature")
FACTOR_PURPOSE = "context for a transcription factor a binding claim names (shown, never ranked)"
BUDGET_STOPS = frozenset({"budget_model_calls", "budget_tool_calls", "budget_currency", "wall_time"})
NO_MORE_CALLS = frozenset({"budget_currency", "wall_time", "cache_miss", "engine_error"})   # no model call after these
PROPOSAL_ATTEMPTS = 2           # the initial proposal and one retry; neither is a regeneration
LEVEL = {"high": 0, "medium": 1, "low": 2}
COST = {"low": 0, "medium": 1, "high": 2}
LIMIT_TRIGGER = "an active hypothesis is rejected, deferred or resolved"
PARK_REASON = ("deferred by code before a regeneration: the critic found no active hypothesis reportable (a priority "
               "decision, not a refutation)")
PARK_TRIGGER = "the regeneration leaves no active hypothesis, or its hypotheses are rejected"
Facts = Callable[[Case, ClaimGraph, ToolRunner], list[ToolCall]]


class EngineLimits(V9Model):
    """Resource caps (SPEC 13.9 defaults), set from cost and latency, never from gold outcomes; ceilings, not targets.
    `max_tool_calls` and the full-text caps are for building the ToolRunner (`tool_limits()`); the runner enforces
    them."""
    max_sketches: int = 8
    max_active: int = 3
    max_new_hypotheses_per_plan: int = 2
    max_additional_hypotheses: int = 4
    max_regenerations: int = 1
    max_model_calls: int = R.DEFAULT_MAX_CALLS
    reserve_model_calls: int = R.DEFAULT_RESERVE
    reserve_audit_calls: int = 0  # config enables a separate audit reserve; old scripted limits remain readable
    max_tool_calls: int = 24
    fulltext_soft: int = 5
    fulltext_hard: int = 8
    wall_seconds: float = 1200.0

    @classmethod
    def from_config(cls, cfg: Mapping[str, Any]) -> "EngineLimits":
        """`cfg.v9.limits`, ignoring keys that belong to other modules (such as the HTTP request cap)."""
        raw = ((cfg.get("v9") or {}).get("limits")) or {}
        return cls(**{k: v for k, v in raw.items() if k in cls.model_fields})

    def tool_limits(self) -> ToolLimits:
        return ToolLimits(max_tool_calls=self.max_tool_calls, fulltext_soft=self.fulltext_soft,
                          fulltext_hard=self.fulltext_hard)


@dataclass
class EngineResult:
    graph: ClaimGraph
    metrics: dict[str, Any]
    manifest_parts: dict[str, Any]


@dataclass
class _Run:
    """The state of one run (the graph holds the science; this holds the bookkeeping)."""
    graph: ClaimGraph
    started: float
    round: int = 0
    regenerations: int = 0
    proposals: int = 0                      # proposal calls that returned a usable output
    proposal_failures: int = 0
    stop_reason: StopReason | None = None
    stop_detail: str = ""
    question_calls: dict[str, list[str]] = field(default_factory=dict)   # question -> the calls that answer it
    presented: set[str] = field(default_factory=set)                    # questions an investigator has seen
    answered: dict[str, tuple[tuple, dict[str, int]]] = field(default_factory=dict)  # question -> (request, versions)
    plan_mark: int = 0                      # events before this index were shown to an earlier plan
    reopened: bool = False                  # the audit may reopen the investigation once
    final_note: str = ""
    final_blocked: StopReason | None = None
    flags: dict[str, str] = field(default_factory=dict)                 # hypothesis -> critic's activation flag
    stale: list[str] = field(default_factory=list)                      # rejections no longer standing (noted)
    error: str | None = None
    read_history: dict[tuple, list[tuple[str, frozenset[str]]]] = field(default_factory=dict)
    extraction_repairs: set[tuple[str, str]] = field(default_factory=set)


@cache
def _hgnc(path: str) -> SymbolResolver:
    return SymbolResolver.from_hgnc(path)


@cache
def _registry(path: str) -> GroupRegistry:
    return GroupRegistry.from_groups_json(path)


def _config_file(cfg: Mapping[str, Any], section: str, key: str) -> Path | None:
    try:
        path = config_module.Config(cfg).path(section, key)
    except (KeyError, TypeError, config_module.ConfigError):
        return None
    return path if path.exists() else None


def default_resolver(cfg: Mapping[str, Any]) -> SymbolResolver | None:
    """The HGNC resolver from `data.hgnc` (None when the file is absent, as in CI)."""
    path = _config_file(cfg, "data", "hgnc")
    return _hgnc(str(path)) if path else None


def default_groups(cfg: Mapping[str, Any]) -> GroupRegistry | None:
    """The QBiC-SELEX group registry from `cache.groups`, read with json only."""
    path = _config_file(cfg, "cache", "groups")
    return _registry(str(path)) if path else None


def fixture_facts(case: Case, graph: ClaimGraph, runner: ToolRunner) -> list[ToolCall]:
    """Fact collection for synthetic fixture runs (role code), standing in for adapters.collect_facts: every
    computational fixture tool that needs no parameter, in name order."""
    return [runner.run(ToolRequest(tool=s.name, purpose="fact collection"), case, graph, "code")
            for s in runner.specs("computational") if not any(p.required for p in s.params.values())]


class Engine:
    """See the module docstring. `facts(case, graph, runner)` collects the facts (adapters.collect_facts in real
    runs); `resolver` and `groups` default to the HGNC table and cache/groups.json named in the config; `clock`
    measures wall time (inject one for tests)."""

    def __init__(self, config: Mapping[str, Any], mode: RunMode, roles: RoleCaller, runner: ToolRunner,
                 run_dir: Path | None, *, limits: EngineLimits | None = None, facts: Facts | None = None,
                 resolver: SymbolResolver | None = None, groups: GroupRegistry | None = None,
                 clock: Callable[[], float] = time.monotonic):
        self.config, self.mode, self.roles, self.runner = config, mode, roles, runner
        self.run_dir = Path(run_dir) if run_dir is not None else None
        self.limits = limits or EngineLimits.from_config(config)
        if limits is not None:
            roles.set_limits(limits.max_model_calls, limits.reserve_model_calls)
        self.facts = facts
        self.resolver = resolver if resolver is not None else default_resolver(config)
        self.groups = groups if groups is not None else default_groups(config)
        self.clock = clock

    # --- the run -----------------------------------------------------------------------------------------------------

    def run(self, case: Case) -> EngineResult:
        st = _Run(graph=ClaimGraph(case, self.resolver, self.groups), started=self.clock())
        try:
            if self._normalise(st):
                self._collect(st)
                self._loop(st)
                self._close(st)
                self._factor_lookups(st)
        except Exception as e:  # the contract: run never raises; the failure is recorded and the run ends
            log.exception("v9 engine stopped on an internal error")
            st.error = f"{type(e).__name__}: {e}"[:600]
            st.stop_reason, st.stop_detail = "engine_error", f"internal error ({type(e).__name__})"
            try:
                st.graph.log("stop", "code", f"engine_error: {st.stop_detail}; the run cannot assess the case",
                             details={"stop_reason": "engine_error", "round": st.round, "detail": st.error})
            except Exception:
                log.exception("v9 engine could not record its internal error")
        if st.graph.result is None:
            self._settle(st)
        return EngineResult(graph=st.graph, metrics=self._metrics(st), manifest_parts=self._manifest(st))

    def _factor_lookups(self, st: _Run) -> None:
        """After the decision, as role code: for every TF a live binding claim about the case variant names, the
        QBiC-SELEX models of the TF (or of the group named), the ChIP-seq survey at the variant, and the TF's
        expression in the contexts the case and its claims name (chain.named_factors, chain.lookup_contexts). The
        report shows what they return beside the answer. They come after compare.decide and no role sees them, so
        they cannot change an assessment, a comparison or the outcome: a missing peak or a low level is never a
        reason to drop a TF. Tools the runner does not have are skipped; a failed call is a recorded call. Never
        raises."""
        graph = st.graph
        try:
            if graph.result is None or st.stop_reason in ("cache_miss", "engine_error"):
                return
            named = chain.named_factors(graph)
            have = {spec.name for spec in self.runner.specs("computational")}
            requests: list[ToolRequest] = []
            if (named["tfs"] or named["groups"]) and "chip_occupancy" in have:
                requests.append(ToolRequest(tool="chip_occupancy", purpose=FACTOR_PURPOSE))
            if "qbic_tf_detail" in have:
                requests += [ToolRequest(tool="qbic_tf_detail", params={"tf": tf}, purpose=FACTOR_PURPOSE)
                             for tf in named["tfs"][:chain.FACTOR_CAP]]
                requests += [ToolRequest(tool="qbic_tf_detail", params={"group": g["id"]}, purpose=FACTOR_PURPOSE)
                             for g in named["groups"][:chain.FACTOR_CAP]]
            if "tf_expression" in have:
                requests += [ToolRequest(tool="tf_expression", params={"tf": tf, "context": context},
                                         purpose=FACTOR_PURPOSE)
                             for tf in named["listed"] for context in chain.lookup_contexts(graph)]
            if not requests:
                return
            calls = [self.runner.run(request, graph.case, graph, "code") for request in requests]
            graph.log("collect_facts", "code",
                      f"factor lookups after the decision, shown only: {len(calls)} call(s) for "
                      f"{', '.join(named['listed']) or 'the groups named'}",
                      target_ids=[c.tool_call_id for c in calls if c.tool_call_id],
                      evidence_ids=[e for c in calls for e in c.evidence_ids],
                      details={"factors": named["listed"], "not_listed": named["not_listed"],
                               "calls": [{"tool_call_id": c.tool_call_id, "tool": c.tool_name,
                                          "execution_status": c.execution_status,
                                          "retrieval_status": c.retrieval_status} for c in calls]})
        except Exception:
            log.exception("v9 engine could not look up the named factors")

    def _settle(self, st: _Run) -> None:
        """A result for a run that ended without one (an internal error before or during the decision)."""
        reason = st.stop_reason or "engine_error"
        try:
            compare.decide(st.graph, None, stop_reason=reason, budget_stop=reason in BUDGET_STOPS,
                           note=f"{reason}: {st.stop_detail}" if st.stop_detail else reason)
        except Exception as e:
            log.exception("v9 engine could not decide")
            st.error = st.error or f"{type(e).__name__}: {e}"[:600]
            st.graph.set_result(RunResult(outcome="input_or_capability_limitation", stop_reason=reason,
                                          budget_stop=reason in BUDGET_STOPS,
                                          summary=f"The run could not be decided ({type(e).__name__})."), "code")

    def _normalise(self, st: _Run) -> bool:
        """Record the variant's identity; an invalid identity ends the run as an input limitation."""
        graph, v = st.graph, st.graph.case.variant
        graph.log("normalize", "code", f"{v.key} ({v.variant_type}); reference check {v.reference_check}",
                  details={"variant": v.key, "variant_type": v.variant_type, "reference_check": v.reference_check,
                           "origin": graph.case.origin})
        problem = None
        if v.reference_check == "mismatch":
            problem = ("input_invalid", f"the stated reference allele {v.ref} does not match the reference genome at "
                                        f"{v.chrom}:{v.pos}")
        elif v.assembly != "GRCh38":
            problem = ("unsupported_variant", f"assembly {v.assembly} is not supported (GRCh38 only)")
        if problem:
            self._stop(st, *problem)
            graph.set_result(RunResult(outcome="input_or_capability_limitation", stop_reason=problem[0],
                                       summary=f"No investigation: {problem[1]}."), "code")
            return False
        if v.variant_type != "SNV":
            graph.log("normalize", "code", f"a {v.variant_type}: QBiC-SELEX predictions do not apply; annotation and "
                                           "literature routes remain", details={"qbic": "not_applicable"})
        return True

    def _collect(self, st: _Run) -> None:
        graph = st.graph
        if self.facts is None:
            graph.log("collect_facts", "code", "no fact collection is configured for this run")
            return
        start = len(graph.events)
        try:
            calls = list(self.facts(graph.case, graph, self.runner))
        except Exception as e:  # missing facts are recorded and never a prerequisite
            graph.log("collect_facts", "code", f"fact collection failed: {type(e).__name__}: {e}",
                      details={"error": f"{type(e).__name__}: {e}"[:600]})
            return
        if any(e.action == "collect_facts" for e in graph.events[start:]):     # the collector logged its own
            return
        summary = "; ".join(f"{c.tool_name} {c.execution_status}/{c.retrieval_status}" for c in calls)
        graph.log("collect_facts", "code", f"{len(calls)} fact call(s): {summary or 'none'}",
                  target_ids=[c.tool_call_id for c in calls if c.tool_call_id],
                  evidence_ids=[e for c in calls for e in c.evidence_ids],
                  details={"calls": [{"tool_call_id": c.tool_call_id, "tool": c.tool_name,
                                      "execution_status": c.execution_status,
                                      "retrieval_status": c.retrieval_status, "message": c.message} for c in calls]})

    def _loop(self, st: _Run) -> None:
        """Rounds until a stop reason: propose (or regenerate) when nothing is active, run the pending questions, let
        the coordinator plan, stop when nothing affordable could change a required claim."""
        while st.stop_reason is None:
            if blocker := self._blocker(st, final=False):
                self._stop(st, blocker)
                break
            if not self._active(st):
                if st.proposals == 0:
                    if st.proposal_failures >= PROPOSAL_ATTEMPTS:
                        self._stop(st, "engine_error", f"no usable proposal from the coordinator in "
                                                       f"{st.proposal_failures} attempts")
                        break
                    self._propose(st, regenerate=False)
                    continue
                if st.regenerations >= self.limits.max_regenerations:
                    self._stop(st, "regeneration_limit", f"no active hypothesis after {st.regenerations} "
                                                         "regeneration(s)")
                    break
                self._propose(st, regenerate=True)
                continue
            changed = False
            pending = self._pending(st)
            if pending:
                if self.runner.budget(st.graph).tool_calls_left == 0 and self._needs_new_calls(st, pending):
                    self._stop(st, "budget_tool_calls", "the agent tool budget is used up")
                    break
                st.round += 1
                changed = self._round(st, pending)
                if st.stop_reason is not None or not self._active(st):
                    continue
                if blocker := self._blocker(st, final=False):
                    self._stop(st, blocker)
                    break
            plan = self._plan(st)
            if st.stop_reason is not None:            # the plan call hit the currency budget or a replay miss
                break
            if plan is None:
                if self._active(st) and not self._pending(st):
                    self._stop(st, "engine_error", "the coordinator's plan failed and no open question is left")
            elif plan.stop.stop and not self._active(st):
                st.graph.log("refuse_update", "code", "the coordinator's stop is not applied: no hypothesis is active, "
                                                      "so a regeneration comes first (a deferral is not a refutation)",
                             details={"kind": "stop", "reason": plan.stop.reason})
            elif plan.stop.stop:
                self._stop(st, "coordinator_stop", plan.stop.reason, role="coordinator")
            elif self._active(st) and not self._pending(st):
                self._stop(st, "no_affordable_discriminating_action" if changed else "converged",
                           "no open question is left to investigate")

    # --- proposals -------------------------------------------------------------------------------------------------

    def _propose(self, st: _Run, regenerate: bool) -> None:
        graph, ctx = st.graph, self._ctx(st)
        stage: EventAction = "regenerate" if regenerate else "propose"
        if regenerate:
            st.regenerations += 1
        packet = R.propose_packet(graph, ctx, regenerate=regenerate, round_no=st.round)
        out = self.roles.propose(packet, R.propose_check(graph, ctx.specs, regenerate=regenerate),
                                 regenerate=regenerate)
        self._usage(st)
        if out is None:
            st.proposal_failures += 1
            self._failed(st, "coordinator", stage, stage)
            return
        st.proposals += 1
        self._apply_proposal(st, out, regenerate)

    def _apply_proposal(self, st: _Run, out: V9Propose, regenerate: bool, *,
                        evidence_led: bool = False,
                        basis_evidence: Mapping[str, Sequence[str]] | None = None) -> tuple[dict[str, str], dict[str, str]]:
        graph = st.graph
        stage: EventAction = "regenerate" if regenerate else "propose"
        cap = self._discovery_capacity(st) if evidence_led else self.limits.max_sketches
        kept = out.hypotheses[:cap]
        graph.log(stage, "coordinator", f"{len(out.hypotheses)} sketch(es), {len(out.questions)} question(s)",
                  details={"directions": list(out.directions), "sketches": [h.key for h in out.hypotheses],
                           "inferred_candidates": [c.model_dump(mode="json") for c in out.inferred_candidates],
                           "fourth_active_reason": out.fourth_active_reason,
                           **({"origin": "evidence_led", "basis_evidence_ids": dict(basis_evidence or {})}
                              if evidence_led else {})})
        for c in out.inferred_candidates:         # recorded on the case, labelled inferred (never supplied)
            candidate = InferredCandidate(kind=c.kind, label=c.label, basis_evidence_ids=list(c.basis_evidence_ids),
                                          note=c.note)
            try:
                graph.add_inferred_candidate(candidate, "coordinator")
            except GraphRefusal as r:
                graph.log("refuse_update", "coordinator", f"inferred {c.kind} {c.label!r} not recorded: {r.reason}",
                          details={"kind": "add_inferred_candidate", "candidate": candidate.model_dump(mode="json")})
        for h in out.hypotheses[cap:]:
            graph.log("refuse_update", "code", f"sketch {h.key} ({h.title}) not kept: at most "
                                               f"{cap} sketches are kept",
                      details={"kind": "add_hypothesis", "sketch": h.key})
        owner = {c.key: h for h in kept for c in h.claims}
        ids = self._add_claims(st, [c for h in kept for c in h.claims], {k: h.mechanism_class for k, h in owner.items()})
        limit = self.limits.max_active + (1 if not evidence_led and (out.fourth_active_reason or "").strip() else 0)
        for r in out.reactivate:
            if self._active_count(graph) >= limit:
                graph.log("refuse_update", "code", f"{r.hypothesis_id} not reactivated: {limit} hypotheses are active "
                                                   "(the limit)", target_ids=[r.hypothesis_id],
                          details={"kind": "set_disposition"})
                continue
            graph.apply_updates([GraphUpdate(kind="set_disposition", hypothesis_id=r.hypothesis_id,
                                             disposition="active", reason=r.reason)], "coordinator")
        hypotheses: dict[str, str] = {}
        for h in kept:
            refs = [(ids.get(c.key), c.required, c.key) for c in h.claims]
            refs += [(ids.get(u.ref, u.ref if u.ref in graph.claims else None), u.required, u.ref)
                     for u in h.reuse_claims]
            missing = [name for cid, required, name in refs if required and cid is None]
            if missing:
                graph.log("refuse_update", "code", f"sketch {h.key} ({h.title}) not added: its required claim(s) "
                                                   f"{', '.join(missing)} were refused",
                          details={"kind": "add_hypothesis", "sketch": h.key})
                continue
            active = h.activate and self._active_count(graph) < limit
            reason, trigger = h.deferral_reason or "", h.revisit_trigger
            if h.activate and not active:
                reason = f"deferred by code: {limit} hypotheses are active (the limit), not for lack of evidence"
                trigger = LIMIT_TRIGGER
            draft = HypothesisDraft(
                title=h.title, summary=h.summary,
                claim_ids=[cid for cid, required, _ in refs if cid and not required],
                required_claim_ids=[cid for cid, required, _ in refs if cid and required],
                assumptions=list(h.assumptions), context=R.context_scope(h.context, graph.case), endpoint=h.endpoint,
                mechanism_class=h.mechanism_class, disposition="active" if active else "deferred",
                disposition_reason=reason, revisit_trigger=trigger,
                origin="evidence_led" if evidence_led else "regenerated" if regenerate else "initial",
                replaces=h.replaces,
                member_alternatives=list(h.member_alternatives), missing_links=list(h.missing_links),
                reason_for_inclusion=R.reason_text(h.reason_kind, h.reason_detail))
            accepted, _ = graph.apply_updates([GraphUpdate(kind="add_hypothesis", hypothesis=draft)], "coordinator")
            if accepted:
                hypotheses[h.key] = accepted[0].ids[0]
        for q in out.questions:
            targets = [ids.get(t, t) for t in q.target_claims]
            self._ask(st, R.question_input(q, [t for t in targets if t in graph.claims],
                                           [x for x in (hypotheses.get(k, k) for k in q.hypotheses)
                                            if x in graph.hypotheses], st.round + 1), "coordinator")
        self._retire_repeats(st)
        return ids, hypotheses

    def _discovery_capacity(self, st: _Run) -> int:
        used = sum(h.origin == "evidence_led" for h in st.graph.hypotheses.values())
        return max(0, min(self.limits.max_new_hypotheses_per_plan, self.limits.max_additional_hypotheses - used))

    def _add_claims(self, st: _Run, claims: Sequence[R.V9Claim], mechanism: Mapping[str, str]) -> dict[str, str]:
        """New claims in dependency order (one batch, keyed), then their initial links with the version each claim
        has now as base_version (the proposer read nothing newer). Returns claim key -> claim id."""
        graph = st.graph
        keys = {c.key for c in claims}
        ordered, done = [], set()
        while len(ordered) < len(claims):
            ready = [c for c in claims if c.key not in done and all(d in done or d not in keys for d in c.depends_on)]
            if not ready:          # a cycle (the check refuses one); the rest are refused by the graph
                ready = [c for c in claims if c.key not in done]
            for c in ready[:1]:
                ordered.append(c)
                done.add(c.key)
        updates = [GraphUpdate(kind="new_claim", key=c.key, reason=c.assertion_text or f"claim {c.key}",
                               claim=R.claim_draft(c, graph.case, mechanism[c.key],
                                                   [f"key:{d}" if d in keys else d for d in c.depends_on]))
                   for c in ordered]
        accepted, _ = graph.apply_updates(updates, "coordinator") if updates else ([], [])
        ids = {updates[o.index].key: o.ids[0] for o in accepted}
        links = [GraphUpdate(kind="attach_evidence", claim_id=ids[c.key], evidence_id=x.evidence_id, stance=x.stance,
                             applicability=x.applicability, rationale=x.rationale,
                             suggested_assessment=x.suggested_assessment,
                             base_version=graph.claims[ids[c.key]].version if x.suggested_assessment else None)
                 for c in ordered if c.key in ids for x in c.initial_links]
        if links:
            graph.apply_updates(links, "coordinator")
        return ids

    def _ask(self, st: _Run, question: Question, role: Role) -> str | None:
        try:
            return st.graph.add_question(question, role)
        except GraphRefusal as r:
            st.graph.log("refuse_update", role, f"question refused: {r.reason}",
                         details={"kind": "add_question", "question": question.model_dump(mode="json")})
            return None

    # --- rounds ----------------------------------------------------------------------------------------------------

    def _pending(self, st: _Run) -> list[str]:
        """Open questions no investigator has seen, by rubric (consequence, discrimination, applicability, then the
        cheaper first) and id."""
        graph = st.graph
        qids = [q for q, x in graph.questions.items() if x.status == "open" and q not in st.presented]
        return sorted(qids, key=lambda q: (LEVEL[graph.questions[q].rubric.consequence],
                                           LEVEL[graph.questions[q].rubric.discrimination],
                                           LEVEL[graph.questions[q].rubric.applicability],
                                           COST[graph.questions[q].rubric.cost], R.id_order(q)))

    def _request_key(self, request: ToolRequest) -> str:
        """A request's dedupe key: tool and canonical parameters (the parameters as given when the spec refuses
        them)."""
        spec = self.runner.registry.spec(request.tool)
        try:
            params = canonical_params(spec, request.params) if spec else dict(request.params)
        except ToolRefusal:
            params = dict(request.params)
        return canonical_key(request.tool, params)

    def _needs_new_calls(self, st: _Run, qids: Sequence[str]) -> bool:
        """Whether a question's actions include one that has not run yet (a repeat is answered free)."""
        graph = st.graph
        executed = {canonical_key(t.tool_name, t.query_parameters) for t in graph.tool_calls.values()
                    if t.charged_to != "none"}
        for qid in qids:
            for action in graph.questions[qid].actions:
                spec = self.runner.registry.spec(action.tool)
                try:
                    params = canonical_params(spec, action.params) if spec else None
                except ToolRefusal:
                    continue
                if params is not None and canonical_key(action.tool, params) not in executed:
                    return True
        return False

    def _question_state(self, st: _Run, qid: str) -> tuple[tuple, dict[str, int]]:
        """What a question asks (route, target claims, tool requests) and the versions of its target claims now."""
        q = st.graph.questions[qid]
        asked = (q.route, tuple(sorted(q.target_claim_ids)), tuple(sorted(self._request_key(a) for a in q.actions)))
        return asked, {c: st.graph.claims[c].version for c in q.target_claim_ids}

    def _retire_repeats(self, st: _Run) -> None:
        """Close, without a model call, each new question that repeats one an investigator already answered: the
        same route, tool requests and target claims, every action already run, and no target claim changed since.
        Re-asking cannot change anything, so it must not cost a round (or stop the run as a budget stop)."""
        graph = st.graph
        for qid in self._pending(st):
            if self._needs_new_calls(st, [qid]):
                continue
            state = self._question_state(st, qid)
            earlier = next((q for q in sorted(st.answered, key=R.id_order, reverse=True) if st.answered[q] == state),
                           None)
            if earlier is not None:
                graph.update_question(qid, "refused", "code",
                                      f"not asked again: it repeats {earlier} (same route, tool requests and target "
                                      f"claims, none changed since); see {earlier}'s answer")

    def _snapshot(self, st: _Run, hids: Sequence[str]) -> list[tuple]:
        graph = st.graph
        return [(h, graph.hypotheses[h].disposition, tuple(graph.hypotheses[h].required_claim_ids),
                 tuple(graph.claims[c].assessment for c in graph.hypotheses[h].required_claim_ids)) for h in hids]

    def _round(self, st: _Run, qids: Sequence[str]) -> bool:
        """Run the questions' actions, then each route's investigator; True when a required-claim assessment (or
        the disposition) of a hypothesis active at the start changed."""
        graph = st.graph
        active = self._active(st)
        before = self._snapshot(st, active)
        self._execute(st, qids)
        for route in ROUTES:
            mine = [q for q in qids if graph.questions[q].route == route and not self._repeated_read(st, q)]
            if not mine or st.stop_reason is not None:
                continue
            if blocker := self._blocker(st, final=False):
                self._stop(st, blocker)
                break
            self._investigate(st, route, mine)
        self._note_stale(st)                  # a replaced link may have withdrawn a contradiction
        return self._snapshot(st, active) != before

    def _execute(self, st: _Run, qids: Sequence[str]) -> None:
        graph = st.graph
        for qid in qids:
            q = graph.questions[qid]
            for action in q.actions:
                if self._out_of_time(st):
                    self._stop(st, "wall_time")
                    return
                self._run_tool(st, action, R.ROUTE_ROLE[q.route], qid)

    def _run_tool(self, st: _Run, request: ToolRequest, role: Role, qid: str) -> tuple[ToolCall, bool]:
        """Run one request for a question; (the call, whether it executed something new)."""
        known = set(st.graph.tool_calls)
        call = self.runner.run(request, st.graph.case, st.graph, role, qid)
        if call.tool_call_id:
            calls = st.question_calls.setdefault(qid, [])
            if call.tool_call_id not in calls:
                calls.append(call.tool_call_id)
        return call, call.tool_call_id not in known and call.charged_to != "none"

    def _investigate(self, st: _Run, route: str, qids: Sequence[str]) -> None:
        """One route: the investigator answers; follow-up actions it asks for run at once, and it reads their results
        in one more call (for literature, the extraction of experiments from the articles read). Each question an
        answer closed is remembered with its target versions, so a repeat of it can be retired."""
        st.presented |= set(qids)
        self._answer(st, route, qids)
        for qid in qids:
            if state := progress.read_state(st.graph, qid, st.question_calls.get(qid, [])):
                key, passages = state
                st.read_history.setdefault(key, []).append((qid, passages))
            if st.graph.questions[qid].status != "open":
                st.answered[qid] = self._question_state(st, qid)

    def _repeated_read(self, st: _Run, qid: str) -> bool:
        """Skip another interpretation of unchanged passages for unchanged claims. Permit one extraction repair.

        Search or computational actions may bring new observations and are never suppressed by this read-only
        check. A different focus returning a genuinely new passage, or a newly scoped claim, is also allowed.
        """
        graph = st.graph
        q = graph.questions[qid]
        if not q.actions or any(a.tool != "literature_read" for a in q.actions):
            return False
        state = progress.read_state(graph, qid, st.question_calls.get(qid, []))
        if state is None:
            return False
        key, passages = state
        repeats = [(old, seen) for old, seen in st.read_history.get(key, []) if passages <= seen]
        if not repeats:
            return False
        old_ids = {old for old, _ in repeats}
        extraction_failed = any(e.action == "refuse_update" and e.details.get("kind") == "add_evidence" and
                                e.details.get("question_id") in old_ids for e in graph.events)
        processing_failed = {qid for e in graph.events if e.action == "refuse_update" and
                             e.details.get("failed") and e.details.get("kind") in ("invalid_output", "invalid_proposal")
                             for qid in e.target_ids if qid in old_ids}
        repairable = extraction_failed or bool(processing_failed)
        if repairable and len(repeats) == 1:
            return False
        summary = ("Passage processing failed; the bounded retry is exhausted. This is an unresolved processing gap."
                   if repeats[-1][0] in processing_failed else "No new source passages for the same scoped claims.")
        graph.update_question(qid, "deferred", "code", summary,
                              f"Reuse {', '.join(sorted(old_ids))}; change the evidence source, obtain a new passage "
                              "or revise the mechanism. One retry for a refused extraction or invalid answer is "
                              "allowed; failure is not biological evidence.")
        st.presented.add(qid)
        return True

    def _answer(self, st: _Run, route: str, qids: Sequence[str]) -> None:
        graph, role = st.graph, R.ROUTE_ROLE[route]
        out = self._ask_investigator(st, route, qids, "answer")
        if out is None:
            return
        mark = len(graph.events)
        follow = self._apply_answers(st, route, out, "answer")
        if route == "literature":
            self._repair_extractions(st, mark)
            follow = {qid: requests for qid, requests in follow.items()
                      if graph.questions[qid].status == "open"}
        ran: list[str] = []
        for qid, requests in follow.items():
            new = False
            for request in requests:
                if self._out_of_time(st):
                    self._stop(st, "wall_time")
                    return
                new = self._run_tool(st, request, role, qid)[1] or new
            if new:
                ran.append(qid)
            else:
                graph.update_question(qid, "deferred", role, "",
                                      "the follow-up actions asked for did not run (refused, or already run)")
        if not ran:
            return
        if blocker := self._blocker(st, final=False):
            self._stop(st, blocker)
            return
        step = "extract" if route == "literature" else "follow_up"
        second = self._ask_investigator(st, route, ran, step)
        if second is not None:
            mark = len(graph.events)
            self._apply_answers(st, route, second, step)
            if route == "literature":
                self._repair_extractions(st, mark)

    def _repair_extractions(self, st: _Run, since: int) -> None:
        """Repair newly refused extractions once per source/location before another discovery round."""
        from . import extraction_repair
        failed = []
        keys = set()
        for event in st.graph.events[since:]:
            if event.action != "refuse_update" or event.details.get("kind") != "add_evidence":
                continue
            ex = event.details.get("experiment", {})
            key = (ex.get("source_id", ""), ex.get("location", ""))
            if key not in st.extraction_repairs and len(failed) < 6:
                keys.add(key)
                failed.append(event)
        if not failed:
            return
        st.extraction_repairs.update(keys)
        qids = list(dict.fromkeys(e.details["question_id"] for e in failed))
        for qid in qids:
            st.graph.update_question(qid, "deferred", "code", "Extraction requires source-local repair.",
                                     "A refused experiment is a processing gap, not biological absence.")
        if self._blocker(st, final=False):
            return  # leave a visible unresolved processing gap; preserve audit/final reserves
        extra = extraction_repair.packet(st.graph, self.run_dir, failed)
        if not extra:
            return  # no accessible original source: leave the processing gap explicit, never invent text
        for qid in qids:
            st.graph.update_question(qid, "open", "code", "One source-local extraction repair attempt.")
        out = self._ask_investigator(st, "literature", qids, "repair", extra=extra)
        if out is not None:
            self._apply_answers(st, "literature", out, "repair")
        for qid in qids:
            if st.graph.questions[qid].status == "open":
                st.graph.update_question(qid, "deferred", "code", "Source-local repair did not complete.")

    def _ask_investigator(self, st: _Run, route: str, qids: Sequence[str], step: str,
                          extra: str = "") -> V9Investigate | None:
        graph, ctx = st.graph, self._ctx(st)
        packet = R.investigate_packet(graph, ctx, route=route, step=step, questions=list(qids),
                                      question_calls=st.question_calls, round_no=st.round)
        packet += extra
        out = self.roles.investigate(route, packet, R.investigate_check(graph, route, list(qids), ctx.specs),
                                     step=step)
        self._usage(st)
        if out is None:
            self._failed(st, R.ROUTE_ROLE[route], f"investigate ({step})", "refuse_update", qids)
        return out

    def _apply_answers(self, st: _Run, route: str, out: V9Investigate, step: str) -> dict[str, list[ToolRequest]]:
        """Extracted experiments become evidence (literature), proposals one batch through the graph's gates (the
        versions shown in the packet are base versions for the whole batch), then each question's status. Returns
        the follow-up requests to run now."""
        graph, role = st.graph, R.ROUTE_ROLE[route]
        updates: list[GraphUpdate] = []
        for answer_index, answer in enumerate(out.answers):
            q = graph.questions[answer.question_id]
            found = {i: eid for i, x in enumerate(answer.experiments)
                     if (eid := self._extract(st, R.experiment_record(x), answer.question_id, i))}
            for proposal_index, u in enumerate(answer.proposed_updates):
                if errors := out._proposal_errors.get((answer_index, proposal_index)):
                    graph.log("refuse_update", role, "; ".join(errors), target_ids=[answer.question_id],
                              details={"kind": "invalid_proposal", "failed": True,
                                       "question_id": answer.question_id, "proposal_index": proposal_index,
                                       "update": u.model_dump(mode="json")})
                    continue
                # Any kind of update can cite an experiment of this answer (a new claim does, as much as a link). One
                # that was not accepted, or an index the answer does not have, has no evidence to stand on.
                if u.experiment_index is not None and u.experiment_index not in found:
                    graph.log("refuse_update", role, f"experiment {u.experiment_index} of the answer to "
                                                     f"{answer.question_id} was not accepted, so "
                                                     + (f"it cannot be linked to {u.claim_id}"
                                                        if u.kind == "attach_evidence" else
                                                        f"the {u.kind} update that cites it is not applied"),
                              target_ids=[x for x in (u.claim_id,) if x],
                              details={"kind": u.kind, "question_id": answer.question_id,
                                       "update": u.model_dump(mode="json")})
                    continue
                evidence = u.evidence_id if u.experiment_index is None else found[u.experiment_index]
                updates.append(R.proposal_update(u, graph.case, evidence, self._mechanism(st, q, u.claim_id)))
                if u.kind in ("new_claim", "supersede_claim") and u.new_claim is not None:
                    # The shared claim schema exposes initial_links to investigators too. Apply them through the
                    # same batch gates as explicit attach_evidence proposals; never silently discard them.
                    updates.extend(GraphUpdate(kind="attach_evidence", claim_id=f"key:{u.new_claim.key}",
                        evidence_id=link.evidence_id, stance=link.stance, applicability=link.applicability,
                        rationale=link.rationale, suggested_assessment=link.suggested_assessment)
                        for link in u.new_claim.initial_links)
        if updates:
            graph.apply_updates(updates, role)
        follow: dict[str, list[ToolRequest]] = {}
        for answer_index, answer in enumerate(out.answers):
            qid = answer.question_id
            if graph.questions[qid].status != "open":
                continue
            gap = answer.remaining_gap.strip()
            errors = [error for (i, _), values in out._proposal_errors.items() if i == answer_index
                      for error in values]
            if errors:
                graph.update_question(qid, "deferred", role, answer.answer_summary,
                                      f"{gap} Repair refused claim updates: {'; '.join(errors)}. "
                                      "Independently verified experiments were retained; reuse their evidence IDs.")
                continue
            if answer.next_question.strip():
                gap = f"{gap} Suggested next question: {answer.next_question.strip()}".strip()
            if step == "answer" and answer.status == "needs_follow_up" and answer.follow_up_actions:
                follow[qid] = [R.tool_request(a) for a in answer.follow_up_actions]
                continue
            if answer.follow_up_actions:
                asked = "; ".join(f"{a.tool} {a.params_json}" for a in answer.follow_up_actions)
                gap = f"{gap} Follow-up actions not run in this round: {asked}".strip()
            status = {"answered": "answered", "unanswerable": "unanswerable", "needs_follow_up": "deferred"}
            graph.update_question(qid, status[answer.status], role, answer.answer_summary, gap)
        return follow

    def _mechanism(self, st: _Run, q: Question, claim_id: str | None) -> str:
        """The mechanism class a new claim inherits: the claim it supersedes, else the question's first hypothesis."""
        graph = st.graph
        if claim_id in graph.claims:
            return graph.claims[claim_id].mechanism_class
        return next((graph.hypotheses[h].mechanism_class for h in q.hypothesis_ids if h in graph.hypotheses), "other")

    def _extract(self, st: _Run, record: ExperimentRecord, qid: str, index: int) -> str | None:
        """An extracted experiment as evidence, through the literature module (contract C3): the read of the article
        it cites (literature.find_read: by any of its PMID, PMCID or DOI, full text preferred), the passage verified
        against the text that read saved, then graph.add_evidence. A refusal is logged with its reason."""
        graph = st.graph
        try:
            literature = importlib.import_module(f"{__package__}.literature")
        except ImportError as e:
            reason = f"the literature module is unavailable ({e})"
        else:
            try:
                read = literature.find_read(graph, record)
                article = literature.load_article(self.run_dir, read)
                from .extraction_repair import materialise
                selector = record.passage if record.passage.startswith("@span:") else None
                record = materialise(record, article)
                # the graph's HGNC resolver lets a paper name a TF or gene by a previous symbol
                evidence = literature.evidence_from_experiment(record, read, article, resolver=graph.resolver)
                from .variant_identity import normalise_evidence
                evidence = normalise_evidence(evidence, graph, article=article)
                if selector:
                    evidence.data["source_span"] = {"selector": selector, "location": record.location,
                                                     "read_id": read.tool_call_id}
                return graph.add_evidence(evidence, "literature_investigator",
                                          f"experiment from {record.source_id} {record.location}")
            except literature.ExtractionRefused as r:
                reason = r.reason
            except GraphRefusal as r:
                reason = r.reason
            except Exception as e:  # a failed extraction is a refusal, never a crash
                reason = f"{type(e).__name__}: {e}"
        graph.log("refuse_update", "literature_investigator",
                  f"experiment {index} for {qid} ({record.source_id} {record.location}) refused: {reason}",
                  target_ids=[qid], details={"kind": "add_evidence", "question_id": qid, "experiment_index": index,
                                             "experiment": record.model_dump(mode="json")})
        return None

    # --- the coordinator's plan ------------------------------------------------------------------------------------

    def _plan(self, st: _Run) -> V9Plan | None:
        graph, ctx = st.graph, self._ctx(st)
        packet = R.plan_packet(graph, ctx, round_no=st.round, since_event=st.plan_mark)
        packet += f"\nNew sketches allowed in this plan: {self._discovery_capacity(st)} (run-wide cap applies)."
        out = self.roles.plan(packet, R.plan_check(graph, ctx.specs, max_new=self._discovery_capacity(st),
                                                  allow_legacy=self.mode != "live"))
        self._usage(st)
        st.plan_mark = len(graph.events)
        if out is None:
            self._failed(st, "coordinator", "plan", "refuse_update")
            return None
        claim_refs: dict[str, str] = {}
        for i, u in enumerate(out.hypothesis_updates):
            h = graph.hypotheses[u.hypothesis_id]
            if u.action == "activate" and h.disposition != "active" and \
                    self._active_count(graph) >= self.limits.max_active:
                graph.log("refuse_update", "code", f"{u.hypothesis_id} not activated: {self.limits.max_active} "
                                                   "hypotheses are active (the limit); defer one first",
                          target_ids=[u.hypothesis_id], details={"kind": "set_disposition", "index": i})
                continue
            cid = self._apply_hypothesis_update(st, u)
            if cid and u.new_claim is not None:
                claim_refs[u.new_claim.key] = cid
        if out.assessments:
            graph.apply_updates([GraphUpdate(kind="assess", claim_id=a.claim_id, assessment=a.assessment,
                                             base_version=a.base_version, rationale=a.rationale)
                                 for a in out.assessments], "coordinator")
        self._note_stale(st)                  # a reassessment may have withdrawn a contradiction
        hypothesis_refs: dict[str, str] = {}
        if out.new_hypotheses or out.inferred_candidates:
            proposal = R.V9Propose(directions=["evidence-led revision"], hypotheses=[d.sketch for d in out.new_hypotheses],
                                   inferred_candidates=out.inferred_candidates, fourth_active_reason=None,
                                   reactivate=[], questions=[])
            ids, hypothesis_refs = self._apply_proposal(st, proposal, False, evidence_led=True,
                basis_evidence={d.sketch.key: d.basis_evidence_ids for d in out.new_hypotheses})
            claim_refs.update(ids)
        self._review_evidence(st, out.evidence_decisions, claim_refs)
        for q in out.questions:
            targets = [claim_refs.get(c, c) for c in q.target_claims]
            hypotheses = [hypothesis_refs.get(h, h) for h in q.hypotheses]
            self._ask(st, R.question_input(q, targets, hypotheses, st.round + 1), "coordinator")
        self._retire_repeats(st)
        return out

    def _review_evidence(self, st: _Run, decisions: Sequence[R.V9EvidenceDecision], refs: Mapping[str, str]) -> None:
        graph = st.graph
        for decision in decisions:
            claims = [refs.get(c, c) for c in decision.claim_refs]
            if decision.disposition == "represented":
                missing = [eid for eid in decision.evidence_ids
                           if not set(claims) & set(adoption.represented_by(graph, eid))]
                if missing:
                    graph.log("refuse_update", "code", f"evidence adoption refused for {', '.join(missing)}: "
                              "no accepted non-context link to the named claims in a live hypothesis; "
                              "a summary edit does not represent an observation",
                              evidence_ids=missing, details={"kind": "review_evidence"})
                    continue
            graph.log("review_evidence", "coordinator", decision.reason, target_ids=claims,
                      evidence_ids=decision.evidence_ids,
                      details={"disposition": decision.disposition, "evidence_ids": decision.evidence_ids,
                               "claim_ids": claims, "reason": decision.reason,
                               "revisit_trigger": decision.revisit_trigger})

    def _apply_hypothesis_update(self, st: _Run, u: V9HypothesisUpdate) -> str | None:
        """One plan item as graph updates: claim changes first, then any initial links of a new claim with the
        version it has once created."""
        graph = st.graph
        hid, h = u.hypothesis_id, graph.hypotheses[u.hypothesis_id]
        if u.action in ("defer", "activate", "reject"):
            disposition = {"defer": "deferred", "activate": "active", "reject": "rejected"}[u.action]
            graph.apply_updates([GraphUpdate(kind="set_disposition", hypothesis_id=hid, disposition=disposition,
                                             reason=u.reason, revisit_trigger=u.revisit_trigger)], "coordinator")
            return
        if u.action == "revise":
            graph.apply_updates([GraphUpdate(kind="revise_hypothesis", hypothesis_id=hid,
                                             changes=R.revision_changes(u.revision), reason=u.reason)], "coordinator")
            return
        if u.action == "add_claim" and u.claim_id is not None:
            graph.apply_updates([GraphUpdate(kind="add_claim_to_hypothesis", hypothesis_id=hid, claim_id=u.claim_id,
                                             required=u.required, reason=u.reason)], "coordinator")
            return
        if u.action == "replace_required_claim" and u.new_claim_id is not None:
            graph.apply_updates([GraphUpdate(kind="replace_required_claim", hypothesis_id=hid, claim_id=u.claim_id,
                                             new_claim_id=u.new_claim_id, reason=u.reason)], "coordinator")
            return
        claim = u.new_claim
        draft = R.claim_draft(claim, graph.case, h.mechanism_class, claim.depends_on)
        if u.action == "supersede_claim":
            updates = [GraphUpdate(kind="supersede_claim", key="new", claim_id=u.claim_id, claim=draft,
                                   reason=u.reason, hypothesis_ids=[hid])]
        elif u.action == "add_claim":
            updates = [GraphUpdate(kind="new_claim", key="new", claim=draft, hypothesis_id=hid, required=u.required,
                                   reason=u.reason)]
        else:
            updates = [GraphUpdate(kind="new_claim", key="new", claim=draft, reason=u.reason),
                       GraphUpdate(kind="replace_required_claim", hypothesis_id=hid, claim_id=u.claim_id,
                                   new_claim_id="key:new", reason=u.reason)]
        accepted, _ = graph.apply_updates(updates, "coordinator")
        new_id = accepted[0].ids[0] if accepted and accepted[0].index == 0 else None
        if new_id and claim.initial_links:
            graph.apply_updates([GraphUpdate(kind="attach_evidence", claim_id=new_id, evidence_id=x.evidence_id,
                                             stance=x.stance, applicability=x.applicability, rationale=x.rationale,
                                             suggested_assessment=x.suggested_assessment,
                                             base_version=graph.claims[new_id].version if x.suggested_assessment
                                             else None) for x in claim.initial_links], "coordinator")
        return new_id

    # --- closing: audit, final comparison, decision ---------------------------------------------------------------

    def _close(self, st: _Run) -> None:
        """Audit (the active hypotheses, or the deferred ones when none is active), at most one reopening, then the
        final comparison (or the graph alone) and the decision. After a regeneration the new hypotheses are audited
        too; after the extra round the audit stands."""
        critique = None
        if st.stop_reason not in NO_MORE_CALLS and (self._active(st) or self._deferred(st)):
            critique = self._audit(st)
            if critique is not None:
                if not self._active(st):
                    self._revive(st, critique)
                if not st.reopened and self._reopen(st, critique) == "regenerate":
                    self._close(st)
                    return
        self._note_stale(st)
        if self._replay_missed() and st.stop_reason != "cache_miss":   # the audit's reply was not in the cache
            self._stop(st, "cache_miss", "a model reply is not in the response cache, or a tool request is not in "
                                         "the saved run: the run cannot go on")
        final = None
        if st.stop_reason in NO_MORE_CALLS:
            st.final_note = f"{st.stop_reason}: {st.stop_detail}" if st.stop_detail else st.stop_reason
        elif not self._active(st):
            st.final_note = "no active hypothesis to compare"
        elif blocker := self._blocker(st, final=True):
            st.final_blocked = blocker
            st.final_note = f"no final comparison: {blocker}"
            st.graph.log("compare", "code", st.final_note, details={"skipped": blocker})
        else:
            final = self._final(st, critique)
            if final is None and self.roles.replay_miss:
                self._stop(st, "cache_miss", "the final comparison's reply is not in the response cache")
                st.final_note = f"cache_miss: {st.stop_detail}"
            elif final is None and self.roles.currency_exhausted:
                st.final_blocked = "budget_currency"
        compare.decide(st.graph, final, stop_reason=st.stop_reason or "converged",
                       budget_stop=st.stop_reason in BUDGET_STOPS or st.final_blocked is not None,
                       note=st.final_note)

    def _audit(self, st: _Run) -> V9Critique | None:
        graph, ctx = st.graph, self._ctx(st)
        if blocker := self._blocker(st, final=False, audit=True):
            graph.log("audit", "code", f"no audit: {blocker}", details={"skipped": blocker})
            return None
        audited = self._active(st) or self._deferred(st)
        out = self.roles.audit(R.audit_packet(graph, ctx, round_no=st.round, audited=audited),
                               R.critique_check(graph, ctx.specs))
        self._usage(st)
        if out is None:
            self._failed(st, "critic", "audit", "audit")
            return None
        graph.log("audit", "critic", f"{len(out.challenges)} challenge(s), {len(out.passage_checks)} passage "
                                     f"check(s), {len(out.activation_flags)} activation flag(s); reportable: "
                                     f"{', '.join(out.reportable_ids) or 'none'}",
                  target_ids=[c.claim_id for c in out.challenges] + [f.hypothesis_id for f in out.activation_flags],
                  evidence_ids=[e for c in out.challenges for e in c.evidence_ids],
                  details={"audited": list(audited),
                           "challenges": [c.model_dump(mode="json") for c in out.challenges],
                           "passage_checks": [p.model_dump(mode="json") for p in out.passage_checks],
                           "activation_flags": [f.model_dump(mode="json") for f in out.activation_flags],
                           "reportable_ids": list(out.reportable_ids), "consequential": out.consequential})
        st.flags.update({f.hypothesis_id: f.reason for f in out.activation_flags})
        updates = [GraphUpdate(kind="assess", claim_id=c.claim_id, assessment=c.suggested_assessment,
                               base_version=c.base_version, rationale=f"critic ({c.kind}): {c.gap}")
                   for c in out.challenges if c.suggested_assessment is not None]
        for p in out.passage_checks:          # a misread passage can no longer support or contradict anything
            if p.verdict in ("misread", "not_in_source"):
                updates += [GraphUpdate(kind="attach_evidence", claim_id=cid, evidence_id=p.evidence_id,
                                        stance="context_only", rationale=f"critic passage check: {p.verdict}: "
                                                                         f"{p.note}")
                            for cid, c in graph.claims.items() if not c.superseded_by
                            for x in c.evidence_links
                            if x.evidence_id == p.evidence_id and x.stance in ("supports", "contradicts")]
        if updates:
            graph.apply_updates(updates, "critic")
        self._note_stale(st)
        return out

    def _revive(self, st: _Run, critique: V9Critique) -> None:
        """No hypothesis is active: reactivate, as code, the deferred hypotheses the critic finds reportable (up to the
        active limit), so the final comparison weighs them. A deferral is a priority decision, never a refutation,
        and one made for missing data must not settle the outcome by itself."""
        graph = st.graph
        for hid in dict.fromkeys(critique.reportable_ids):
            if self._active_count(graph) >= self.limits.max_active:
                break
            if graph.hypotheses[hid].disposition == "deferred":
                graph.apply_updates([GraphUpdate(kind="set_disposition", hypothesis_id=hid, disposition="active",
                                                 reason="reactivated by code: no hypothesis was active, and the "
                                                        "critic's audit finds this deferred hypothesis reportable")],
                                    "code")

    def _reopen(self, st: _Run, critique: V9Critique) -> str | None:
        """Once per run: regenerate when the critic finds no active hypothesis reportable, or run one more round
        for consequential challenges that request actions. Returns "regenerate", "extra_round" or None."""
        graph = st.graph
        active = self._active(st)
        if not [h for h in critique.reportable_ids if h in active]:
            if st.regenerations >= self.limits.max_regenerations or self._blocker(st, final=False):
                graph.log("audit", "code", "the critic finds no active hypothesis reportable; no regeneration is left "
                                           f"({st.regenerations} of {self.limits.max_regenerations} used, or no "
                                           "budget)", details={"continue": None})
                return None
            st.reopened = True
            graph.log("audit", "code", "the critic finds no active hypothesis reportable: deferring "
                                       f"{', '.join(active) or 'none'} and regenerating",
                      target_ids=active, details={"continue": "regenerate"})
            parked = [hid for hid in active if self._defer(st, hid, PARK_REASON, PARK_TRIGGER)]
            st.stop_reason, st.stop_detail = None, ""
            self._propose(st, regenerate=True)
            self._loop(st)
            if not self._active(st):          # the regeneration left nothing active: the parked hypotheses return
                for hid in parked:
                    if graph.hypotheses[hid].disposition == "deferred" and \
                            self._active_count(graph) < self.limits.max_active:
                        graph.apply_updates([GraphUpdate(kind="set_disposition", hypothesis_id=hid,
                                                         disposition="active",
                                                         reason="reactivated by code: the regeneration left no "
                                                                "active hypothesis")], "code")
            return "regenerate"
        requests = [c for c in critique.challenges if c.requested_action is not None]
        if not (critique.consequential and requests) or self._blocker(st, final=False) or \
                self.runner.budget(graph).tool_calls_left == 0:
            return None
        st.reopened = True
        graph.log("audit", "code", f"{len(requests)} consequential challenge(s) request actions: one more round",
                  details={"continue": "extra_round"})
        qids = []
        for c in requests:
            spec = self.runner.registry.spec(c.requested_action.tool)
            route = spec.route if spec is not None else "computational"
            hyps = [h for h in graph.hypotheses_with_claim(c.claim_id) if h in self._active(st)]
            question = R.question_input(R.V9Question(text=f"Critic challenge on {c.claim_id} ({c.kind}): {c.gap}",
                                                     route=route, target_claims=[c.claim_id], hypotheses=hyps,
                                                     rubric=R.V9Rubric(consequence="high", discrimination="high",
                                                                       applicability="high", cost="medium"),
                                                     possible_outcomes=[], actions=[c.requested_action]),
                                        [c.claim_id], hyps, st.round + 1)
            if qid := self._ask(st, question, "critic"):
                qids.append(qid)
        earlier, st.stop_reason = st.stop_reason, None
        st.round += 1
        self._round(st, qids)
        st.stop_reason = st.stop_reason or earlier
        return "extra_round"

    def _defer(self, st: _Run, hid: str, reason: str, trigger: str) -> bool:
        """Defer a hypothesis as code; a refusal is logged and returns False."""
        accepted, _ = st.graph.apply_updates([GraphUpdate(kind="set_disposition", hypothesis_id=hid,
                                                          disposition="deferred", reason=reason,
                                                          revisit_trigger=trigger)], "code")
        return bool(accepted)

    def _note_stale(self, st: _Run) -> None:
        """A rejection whose contradiction no longer stands (compare.stale_rejections: the passage behind it was found
        misread and relinked as context only, or the claim was reassessed) must not pass as a refutation. Code
        reinstates it as deferred (graph.reinstate: only a rejection code made for a contradicted required claim, and
        only once, so a story cannot oscillate); from then on it is a deferred hypothesis like any other (the
        coordinator may reactivate it, and the audit covers it when nothing is active). One the graph keeps rejected
        (a second rejection, a rejection code did not make, an open hypothesis with its structure) is disclosed once
        instead: an audit event, the final packet, the summary and metrics. Called after every step that can withdraw
        a contradiction (a round, a plan, the audit) and before the decision."""
        graph = st.graph
        for hid in compare.stale_rejections(graph):
            if hid in st.stale:
                continue
            h = graph.hypotheses[hid]
            required = ", ".join(h.required_claim_ids)
            try:
                if graph.reinstate(hid, f"reinstated by code: none of {hid}'s required claims ({required}) is "
                                        "contradicted in scope any more, so its rejection has no basis; deferred, "
                                        "which is not support"):
                    continue
                why = self._kept_rejected(graph, hid)
            except GraphRefusal as r:
                why = r.reason
            st.stale.append(hid)
            graph.log("audit", "code", f"the rejection of {hid} no longer stands: none of its required claims "
                                       f"({required}) is contradicted in scope now; code did not reinstate it "
                                       f"({why}), so it is disclosed, not reversed", target_ids=[hid],
                      details={"stale_rejection": hid, "reinstated": False, "why": why})

    @staticmethod
    def _kept_rejected(graph: ClaimGraph, hid: str) -> str:
        """Why graph.reinstate left a stale rejection in place (it returned False)."""
        h = graph.hypotheses[hid]
        if any(x.get("kind") == "reinstatement" for x in h.history):
            return "it was reinstated once already, and a second rejection is final"
        same = R.sort_ids(o.hypothesis_id for o in graph.hypotheses.values() if o.hypothesis_id != hid
                          and o.signature == h.signature and o.disposition not in ("rejected", "superseded"))
        if same:
            return f"{', '.join(same)} already holds its structure"
        return "the graph keeps it rejected"

    def _final(self, st: _Run, critique: V9Critique | None) -> V9Final | None:
        graph, ctx = st.graph, self._ctx(st)
        profiles = {h: compare.profile(graph, h) for h in self._active(st)}
        packet = R.final_packet(graph, ctx, profiles=profiles, critique=critique, stale=st.stale, round_no=st.round,
                                reinstated=compare.reinstated(graph))
        out = self.roles.final(packet, R.final_check(graph))
        self._usage(st)
        if out is None:
            st.final_note = f"the final comparison failed ({self.roles.failures[-1]['kind']})"
            self._failed(st, "critic", "final comparison", "compare")
        return out

    # --- helpers ---------------------------------------------------------------------------------------------------

    def _active(self, st: _Run) -> list[str]:
        return R.sort_ids(h for h, x in st.graph.hypotheses.items() if x.disposition == "active")

    def _deferred(self, st: _Run) -> list[str]:
        return R.sort_ids(h for h, x in st.graph.hypotheses.items() if x.disposition == "deferred")

    @staticmethod
    def _active_count(graph: ClaimGraph) -> int:
        return sum(h.disposition == "active" for h in graph.hypotheses.values())

    def _out_of_time(self, st: _Run) -> bool:
        return self.clock() - st.started >= self.limits.wall_seconds

    def _replay_missed(self) -> bool:
        """A replay found a model reply (RoleCaller) or a tool request (RecordedToolRunner.misses) that the saved
        run does not hold: nothing decided after that would be the saved run's decision."""
        return self.roles.replay_miss or bool(getattr(self.runner, "misses", None))

    def _blocker(self, st: _Run, final: bool, *, audit: bool = False) -> StopReason | None:
        """Why no model call can be made now, or None."""
        if self._replay_missed():
            return "cache_miss"
        if self._out_of_time(st):
            return "wall_time"
        if self.roles.currency_exhausted:
            return "budget_currency"
        if not self.roles.affordable(final):
            return "budget_model_calls"
        if not final and not audit and (self.roles.calls_used + R.GUARD + self.roles.reserve +
                                        self.limits.reserve_audit_calls > self.roles.max_calls):
            return "budget_model_calls"
        return None

    def _stop(self, st: _Run, reason: StopReason, detail: str = "", role: Role = "code") -> None:
        st.stop_reason, st.stop_detail = reason, detail
        st.graph.log("stop", role, f"{reason}: {detail}" if detail else reason,
                     details={"stop_reason": reason, "round": st.round, "detail": detail})

    def _usage(self, st: _Run) -> None:
        st.graph.set_model_usage(self.roles.calls_used, self.roles.cost_usd)

    def _failed(self, st: _Run, role: Role, stage: str, action: EventAction, targets: Sequence[str] = ()) -> None:
        """Log a role call that returned nothing usable. The event text names the failure kind only (a fixed word):
        provider text varies between a run and its replay and would change every later packet, so the message is
        kept in the details. A replay miss or an exhausted currency budget stops the run here."""
        failure = self.roles.failures[-1]
        st.graph.log(action, role, f"the {role.replace('_', ' ')}'s {stage} output was not usable "
                                   f"({failure['kind']}); nothing from it was applied", target_ids=targets,
                     details={"stage": stage, "failed": True, "kind": failure["kind"], "error": failure["message"]})
        if st.stop_reason is None and self.roles.replay_miss:
            # a replay and a cache-only run both answer every model call from the response cache
            self._stop(st, "cache_miss", "a model reply is not in the response cache: the run cannot go on")
        elif st.stop_reason is None and self.roles.currency_exhausted:
            self._stop(st, "budget_currency", "the profile's currency budget refused a call")

    def _inventory(self, graph: ClaimGraph) -> list[dict[str, Any]]:
        """adapters.inventory_rows (contract C2) once QBiC-SELEX's inventory call succeeded; [] otherwise (the
        packets then say the inventory is unavailable)."""
        if not any(t.tool_name == "qbic_inventory" and t.execution_status == "success"
                   for t in graph.tool_calls.values()):
            return []
        return list(importlib.import_module(f"{__package__}.adapters").inventory_rows(graph))

    def _ctx(self, st: _Run) -> R.PacketContext:
        limits = self.runner.limits
        budget = R.PacketBudget(model_used=self.roles.calls_used, model_cap=self.roles.max_calls,
                                model_reserve=self.roles.reserve, tools=self.runner.budget(st.graph),
                                fulltext_soft=limits.fulltext_soft, fulltext_hard=limits.fulltext_hard,
                                regenerations_used=st.regenerations, max_regenerations=self.limits.max_regenerations)
        return R.PacketContext(specs={route: self.runner.specs(route) for route in ROUTES}, budget=budget,
                               inventory=self._inventory(st.graph), flags=dict(st.flags),
                               max_sketches=self.limits.max_sketches, max_active=self.limits.max_active)

    @staticmethod
    def _inventory_summary(graph: ClaimGraph, rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
        """Candidate retention (SPEC 13.5), by the one rule the bundle and the evaluator use (graph.sketched_groups:
        every version of every hypothesis, member alternatives and supersession chains): the gate-passing groups some
        hypothesis sketched, and those it never did (inventory_only), in the inventory's neutral order. The same dict
        as bundle.inventory_summary (a test pins it); the engine does not import the report module."""
        passing = [str(r.get("group_id")) for r in rows if r.get("passes_gate") is True]
        sketched = sketched_groups(graph, rows)
        return {"groups": len(rows), "gate_passing": len(passing), "below_gate": len(rows) - len(passing),
                "sketched": [g for g in passing if g in sketched],
                "inventory_only": [g for g in passing if g not in sketched]}

    def _replay(self, st: _Run) -> tuple[bool, list[str]]:
        """Whether a replay can answer every model call of this run from the response cache, and why not."""
        reasons = [f"{u['role']} {u['stage']}: {u['why']}" for u in self.roles.unreplayable]
        stop = st.graph.result.stop_reason if st.graph.result else st.stop_reason
        if stop == "wall_time":
            reasons.append("the run stopped on its wall-time limit, which a replay would not reach at the same point")
        if stop == "budget_currency" and not any("currency" in r for r in reasons):
            reasons.append("the run stopped on its currency budget; a replay, whose cached replies cost nothing, "
                           "would go on")
        return not reasons, reasons

    def _metrics(self, st: _Run) -> dict[str, Any]:
        graph = st.graph
        snap = graph.budget_snapshot()
        calls = list(graph.tool_calls.values())
        try:
            inventory = self._inventory_summary(graph, self._inventory(graph))
        except Exception as e:  # metrics never fail a run
            log.warning("inventory rows unavailable for metrics: %s", e)
            inventory = self._inventory_summary(graph, [])
        result = graph.result
        return {
            "engine_version": ENGINE_VERSION, "mode": self.mode,
            "model_calls": self.roles.calls_used, "model_call_cap": self.roles.max_calls,
            "model_call_reserve": self.roles.reserve, "cost_usd": self.roles.cost_usd,
            "model_usage_by_role": {k: dict(v) for k, v in sorted(self.roles.usage.items())},
            "role_failures": list(self.roles.failures),
            "resolution": support_summary(graph),
            "tool_calls": {"agent": snap.tool_calls, "code": snap.code_tool_calls,
                           "refused": sum(t.charged_to == "none" for t in calls),
                           "cached": sum(t.cached for t in calls),
                           "by_status": dict(sorted(Counter(f"{t.execution_status}/{t.retrieval_status}"
                                                            for t in calls).items()))},
            "fulltext_reads": snap.fulltext_reads,
            "unique_sources": len({s for e in graph.evidence.values() for s in e.source_ids}),
            "rounds": st.round, "regenerations": st.regenerations,
            "evidence_led_hypotheses": sum(h.origin == "evidence_led" for h in graph.hypotheses.values()),
            "observations_awaiting_adoption": adoption.pending(graph),
            "evidence_decisions": sum(e.action == "review_evidence" for e in graph.events),
            "refused_updates": sum(e.action == "refuse_update" for e in graph.events),
            "hypotheses": dict(sorted(Counter(h.disposition for h in graph.hypotheses.values()).items())),
            "inventory": inventory,
            "activation_flags": [{"hypothesis_id": h, "reason": r} for h, r in sorted(st.flags.items(),
                                                                                       key=lambda x: R.id_order(x[0]))],
            "inferred_candidates": [c.model_dump(mode="json") for c in graph.case.inferred_candidates],
            "reinstated": compare.reinstated(graph),
            "stale_rejections": list(st.stale),
            "cache_miss": self._replay_missed(),
            "tool_misses": list(getattr(self.runner, "misses", None) or []),
            "stop_reason": result.stop_reason if result else st.stop_reason,
            "budget_stop": result.budget_stop if result else None,
            "outcome": result.outcome if result else None,
            "wall_seconds": round(self.clock() - st.started, 3),
            "engine_error": st.error,
        }

    def _manifest(self, st: _Run) -> dict[str, Any]:
        result = st.graph.result
        replayable, reasons = self._replay(st)
        return {"engine_version": ENGINE_VERSION, "mode": self.mode, "prompts": R.prompt_hashes(),
                "schemas": R.schema_hashes(), "roles": self.roles.role_models(), "limits": self.limits.model_dump(),
                "tool_limits": self.runner.limits.model_dump(),
                "stop_reason": result.stop_reason if result else st.stop_reason,
                "budget_stop": result.budget_stop if result else None,
                "replayable": replayable, "not_replayable": reasons}
