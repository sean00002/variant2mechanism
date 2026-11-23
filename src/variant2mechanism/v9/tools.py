"""The tool contract (SPEC 4.1, 4.2, 13.4): ToolSpec, the adapter registry, ToolRunner and RecordedToolRunner.

Agents ask for tools as data (ToolRequest); code runs them here and the result becomes a ToolCall in the graph. The
runner keeps the scientific and resource rules out of every adapter:

- requests are validated against the tool's ToolSpec; an unknown tool, a bad parameter (or not exactly one of a
  one_of group), a variant the tool does not cover or a tool outside the allowlist is refused with a clear message
  (execution_status "not_applicable", charged to no budget);
- an identical request (same tool, same canonical parameters) returns the earlier ToolCall and is not counted again;
- agent-initiated calls count against max_tool_calls and unique full-text articles against fulltext_hard; code's
  fact collection (role "code") is counted separately; over budget, the request is refused and the engine is told.
  A read counts only when it returned the article, and one article is one read whichever identifier (PMID, PMCID,
  DOI) it was requested by, so a re-read is free and never refused at the cap;
- every raw result is written once to run_dir/raw/T#.json (never overwritten) and its sha256 kept;
- run() never raises: an adapter exception becomes execution_status "error" with a short message, and an adapter
  that breaks the evidence contract (Evidence from an empty retrieval, a malformed Evidence item, values that are not
  JSON-native) is recorded as an error without Evidence. A failed call is still charged and recorded under its
  canonical parameters, so a repeat is deduplicated (never re-executed for free) and replay can answer it;
- cache_only mode refuses an HTTP client that is not offline, so it can never reach the network.

Retrieval is not biology: an adapter reports what the source returned (records_found, no_records_found, ...) and
creates Evidence only for records; support and contradiction exist only as evidence links on claims (graph.py).

Adapters register into REGISTRY (adapters.py, literature.py) with `@register_tool(ToolSpec(...))`. Subclasses
answer from somewhere other than an adapter by overriding `_execute`: RecordedToolRunner replays a saved bundle, and
fixtures.FixtureToolRunner answers synthetic fixtures.
"""

import copy
import hashlib
import json
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal, get_args

from pydantic import ConfigDict, Field, model_validator

from ..config import Config
from .graph import EVIDENCE_FROM, ClaimGraph, GraphRefusal, article_key
from .schemas import (
    Case,
    ChargedTo,
    Coverage,
    Evidence,
    EvidenceClass,
    ExecutionStatus,
    ParamValue,
    RetrievalStatus,
    Role,
    RunMode,
    ToolCall,
    ToolRequest,
    V9Model,
)

ParamType = Literal["str", "int", "float", "bool", "list[str]"]
CONTEXT_PARAMS = ("context", "biosample", "tissue")
ROUTE_OF = {"computational_investigator": "computational", "literature_investigator": "literature"}
ROLES = frozenset(get_args(Role))
MAX_MESSAGE = 300


class ToolRefusal(Exception):
    """A request the runner will not execute; `message` is what the agent is told."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class ParamSpec(V9Model):
    type: ParamType = "str"
    required: bool = False
    description: str = ""
    normalise: Literal["strip", "upper", "lower"] = "strip"   # strings and list items; upper for gene/TF symbols
    choices: list[str] = Field(default_factory=list)          # allowed values (after normalisation), when fixed


class ToolSpec(V9Model):
    """What a tool is, for code (validation, applicability, provenance) and for prompts (describe())."""
    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)
    name: str
    route: Literal["computational", "literature"]
    description: str = ""
    params: dict[str, ParamSpec] = Field(default_factory=dict)
    assemblies: list[str] = Field(default_factory=lambda: ["GRCh38"])        # empty: any (literature)
    variant_types: list[str] = Field(default_factory=lambda: ["SNV", "indel", "other"])
    requires_context: bool = False         # needs a supplied context or a context/biosample/tissue parameter
    coverage_notes: str = ""
    result_semantics: str = ""             # what records_found / no_records_found mean for this tool
    provider: str = ""
    dataset_release: str = ""
    release_fn: Callable[[Config | None], str] | None = Field(default=None, exclude=True)
    rate_policy: Literal["serial", "parallel"] = "serial"
    evidence_classes: list[EvidenceClass] = Field(default_factory=list)
    network: bool = False
    fulltext_params: list[str] = Field(default_factory=list)  # non-empty: a full-text read, keyed by these params
    # Groups of alternative parameters: a request must set exactly one of each group (qbic_tf_detail takes a TF or a
    # group, never both or neither), checked before anything runs, so a malformed request costs no budget.
    one_of: list[list[str]] = Field(default_factory=list)
    tool_version: str = "1"

    @model_validator(mode="after")
    def _groups_name_params(self) -> "ToolSpec":
        for group in self.one_of:
            if not group:
                raise ValueError(f"tool {self.name}: a one_of group names no parameter")
            if unknown := sorted(set(group) - set(self.params)):
                raise ValueError(f"tool {self.name}: one_of group {group} names unknown parameter(s) "
                                 f"{', '.join(unknown)}")
        return self

    def release(self, config: Config | None = None) -> str:
        """The dataset release, from release_fn when the adapter reports it at run time."""
        return self.release_fn(config) if self.release_fn else self.dataset_release

    def describe(self) -> dict[str, Any]:
        """The compact form role packets show: name, route, what it does, its parameters (and which of them are
        alternatives: exactly one of each one_of group) and result semantics."""
        params = {name: {"type": p.type, "required": p.required, "description": p.description,
                         **({"choices": p.choices} if p.choices else {})} for name, p in sorted(self.params.items())}
        return {"name": self.name, "route": self.route, "description": self.description, "params": params,
                **({"one_of": [list(g) for g in self.one_of]} if self.one_of else {}),
                "result_semantics": self.result_semantics, "coverage_notes": self.coverage_notes,
                "evidence_classes": list(self.evidence_classes)}


@dataclass(frozen=True)
class ToolContext:
    """What an adapter may use. `graph` is for reading earlier results only; adapters never mutate it."""
    spec: ToolSpec
    case: Case
    graph: ClaimGraph
    config: Config | None
    mode: RunMode
    http: Any                                  # an Http-like client (offline in cache_only mode), or None
    run_dir: Path | None
    tool_call_id: str
    role: Role
    question_id: str | None


@dataclass
class AdapterResult:
    """An adapter's answer. Evidence only for records found (never for an empty search, an error or a miss)."""
    execution_status: ExecutionStatus = "success"
    retrieval_status: RetrievalStatus = "unknown"
    observations: list[dict[str, Any]] = field(default_factory=list)
    coverage: Coverage = field(default_factory=Coverage)
    evidence: list[Evidence] = field(default_factory=list)
    raw: Any = None                            # JSON-native; written to raw/T#.json
    raw_bytes: bytes | None = None             # or the exact bytes (replay keeps the original hash)
    message: str = ""
    provider: str | None = None                # defaults: the spec's
    dataset_release: str | None = None
    tool_version: str | None = None
    assembly: str | None = None
    cached: bool = False
    fulltext_article: str | None = None        # the article read, when it differs from the parameters' key
    fulltext_read: bool = True                 # False: a full-text tool that could only return the abstract
    article_ids: list[str] = field(default_factory=list)   # every id of the article read (PMID, PMCID, DOI)
    retrieval_time: str | None = None


Adapter = Callable[[dict[str, ParamValue], ToolContext], AdapterResult]


class ToolRegistry:
    """Tool name -> (ToolSpec, adapter). Names are unique; specs are listed in name order (deterministic prompts)."""

    def __init__(self):
        self._specs: dict[str, ToolSpec] = {}
        self._adapters: dict[str, Adapter | None] = {}

    def register(self, spec: ToolSpec, adapter: Adapter | None) -> None:
        if spec.name in self._specs:
            raise ValueError(f"tool {spec.name!r} is already registered")
        self._specs[spec.name] = spec
        self._adapters[spec.name] = adapter

    def tool(self, spec: ToolSpec) -> Callable[[Adapter], Adapter]:
        """Decorator: register the function as the adapter for `spec`."""
        def wrap(fn: Adapter) -> Adapter:
            self.register(spec, fn)
            return fn
        return wrap

    def spec(self, name: str) -> ToolSpec | None:
        return self._specs.get(name)

    def adapter(self, name: str) -> Adapter | None:
        return self._adapters.get(name)

    def names(self, route: str | None = None) -> list[str]:
        return sorted(n for n, s in self._specs.items() if route is None or s.route == route)

    def specs(self, route: str | None = None) -> list[ToolSpec]:
        return [self._specs[n] for n in self.names(route)]


REGISTRY = ToolRegistry()


def register_tool(spec: ToolSpec) -> Callable[[Adapter], Adapter]:
    """Register an adapter in the default registry (adapters.py and literature.py use this)."""
    return REGISTRY.tool(spec)


def _normalise(value: str, how: str) -> str:
    value = " ".join(value.split())
    return value.upper() if how == "upper" else value.lower() if how == "lower" else value


def canonical_params(spec: ToolSpec, params: dict[str, Any]) -> dict[str, ParamValue]:
    """Validate request parameters against the spec and return them canonical (sorted keys, normalised strings,
    sorted de-duplicated lists, empty values dropped), or raise ToolRefusal saying what is wrong. Each one_of group
    must have exactly one parameter set once empty values are dropped."""
    unknown = sorted(set(params) - set(spec.params))
    if unknown:
        allowed = ", ".join(sorted(spec.params)) or "none"
        raise ToolRefusal(f"{spec.name}: unknown parameter(s) {', '.join(unknown)} (allowed: {allowed})")
    out: dict[str, ParamValue] = {}
    for name, p in sorted(spec.params.items()):
        value = params.get(name)
        if p.type == "str":
            if value is not None and not isinstance(value, str):
                raise ToolRefusal(f"{spec.name}: {name} must be a string")
            value = _normalise(value, p.normalise) if value is not None else None
            value = value or None
        elif p.type == "list[str]":
            if value is not None and not (isinstance(value, list) and all(isinstance(v, str) for v in value)):
                raise ToolRefusal(f"{spec.name}: {name} must be a list of strings")
            items = sorted({_normalise(v, p.normalise) for v in value or []} - {""})
            value = items or None
        elif p.type == "bool":
            if value is not None and not isinstance(value, bool):
                raise ToolRefusal(f"{spec.name}: {name} must be true or false")
        elif p.type == "int":
            if isinstance(value, float) and value.is_integer():
                value = int(value)
            if value is not None and (isinstance(value, bool) or not isinstance(value, int)):
                raise ToolRefusal(f"{spec.name}: {name} must be an integer")
        elif p.type == "float":
            if value is not None and (isinstance(value, bool) or not isinstance(value, int | float)):
                raise ToolRefusal(f"{spec.name}: {name} must be a number")
            value = float(value) if value is not None else None
        if value is None:
            if p.required:
                raise ToolRefusal(f"{spec.name}: missing required parameter {name}")
            continue
        if p.choices:
            values = value if isinstance(value, list) else [value]
            bad = [v for v in values if str(v) not in p.choices]
            if bad:
                raise ToolRefusal(f"{spec.name}: {name} must be one of {', '.join(p.choices)} "
                                  f"(got {', '.join(map(str, bad))})")
        out[name] = value
    for group in spec.one_of:
        given = [name for name in group if name in out]
        if len(given) != 1:
            raise ToolRefusal(f"{spec.name}: give exactly one of {', '.join(group)} "
                              f"(got {', '.join(given) or 'none'})")
    return out


def canonical_key(tool: str, params: dict[str, Any]) -> str:
    """The dedupe and replay key of a request: tool name plus canonical parameters."""
    return json.dumps([tool, params], sort_keys=True, separators=(",", ":"))


class ToolLimits(V9Model):
    max_tool_calls: int = 24          # agent-initiated calls
    fulltext_soft: int = 5            # unique full-text articles: the soft target the engine reports
    fulltext_hard: int = 8            # and the hard cap
    max_code_calls: int | None = None  # code's fact collection (None: no cap)


class ToolBudget(V9Model):
    tool_calls_used: int
    tool_calls_left: int
    code_tool_calls: int
    fulltext_used: int
    fulltext_left: int
    fulltext_soft_reached: bool


def _now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def _short(text: str) -> str:
    return " ".join(str(text).split())[:MAX_MESSAGE]


def _checked_evidence(item: Any) -> Evidence:
    """An adapter's Evidence item, re-validated: model_copy(update=...) skips validation, so a malformed field (a
    string where a ContextScope belongs) would otherwise reach the graph."""
    if not isinstance(item, Evidence):
        raise TypeError(f"adapter returned a {type(item).__name__} where Evidence belongs")
    return Evidence.model_validate(item.model_dump(warnings=False))


def _raw_bytes(result: AdapterResult) -> bytes | None:
    """The bytes of raw/T#.json: the adapter's exact bytes, or its JSON-native raw value (NaN refused)."""
    if result.raw_bytes is not None or result.raw is None:
        return result.raw_bytes
    return json.dumps(result.raw, sort_keys=True, ensure_ascii=False, indent=1, allow_nan=False).encode()


class ToolRunner:
    """Runs ToolRequests through registered adapters (live or cache_only) under the contract in the module docstring.
    `http` is the client adapters use (it must be offline in cache_only mode; the runner never builds one). `clock`
    returns the ISO retrieval time (inject a fixed one for deterministic tests)."""

    def __init__(self, config: Config | None = None, mode: RunMode = "cache_only", http: Any = None,
                 run_dir: str | Path | None = None, limits: ToolLimits | None = None,
                 registry: ToolRegistry | None = None, allowed_tools: list[str] | None = None,
                 clock: Callable[[], str] | None = None):
        if mode == "cache_only" and http is not None and getattr(http, "offline", False) is not True:
            raise ValueError("cache_only mode needs an offline HTTP client (Http(..., offline=True)): it must never "
                             "reach the network")
        self.config, self.mode, self.http = config, mode, http
        self.run_dir = Path(run_dir) if run_dir is not None else None
        self.limits = limits or ToolLimits()
        self.registry = registry if registry is not None else REGISTRY
        self.allowed_tools = sorted(allowed_tools) if allowed_tools is not None else None
        self.clock = clock or _now

    # --- what the engine reads ---------------------------------------------------------------------------------------

    def specs(self, route: str | None = None) -> list[ToolSpec]:
        """The specs an agent on this route may request (allowlist applied), in name order."""
        return [s for s in self.registry.specs(route) if self.allowed_tools is None or s.name in self.allowed_tools]

    def budget(self, graph: ClaimGraph) -> ToolBudget:
        snap = graph.budget_snapshot()
        return ToolBudget(tool_calls_used=snap.tool_calls,
                          tool_calls_left=max(0, self.limits.max_tool_calls - snap.tool_calls),
                          code_tool_calls=snap.code_tool_calls, fulltext_used=snap.fulltext_reads,
                          fulltext_left=max(0, self.limits.fulltext_hard - snap.fulltext_reads),
                          fulltext_soft_reached=snap.fulltext_reads >= self.limits.fulltext_soft)

    # --- running -----------------------------------------------------------------------------------------------------

    def run(self, request: ToolRequest, case: Case, graph: ClaimGraph, role: Role,
            question_id: str | None = None) -> ToolCall:
        """Execute (or refuse, or deduplicate) one request; the ToolCall is recorded in the graph. Never raises."""
        try:
            if role not in ROLES:
                return self._refuse(graph, request, "code", question_id, f"unknown role {role!r}: the request is "
                                                                         "not run")
            return self._run(request, case, graph, role, question_id)
        except Exception as e:  # the contract: a tool request never raises into the engine
            requested_by: Role = role if role in ROLES else "code"
            call = ToolCall(tool_call_id="", tool_name=request.tool, query_parameters=request.params,
                            purpose=request.purpose, execution_status="error", requested_by=requested_by,
                            question_id=question_id, message=_short(f"tool runner error: {type(e).__name__}: {e}"),
                            retrieval_time=self.clock(), charged_to="code" if requested_by == "code" else "agent")
            try:
                return graph.record_tool_call(call.model_copy(update={"tool_call_id": graph.reserve_tool_call_id()}))
            except Exception:
                return call

    def _spec(self, name: str) -> ToolSpec | None:
        return self.registry.spec(name)

    def _refuse(self, graph: ClaimGraph, request: ToolRequest, role: Role, question_id: str | None, message: str,
                params: dict[str, ParamValue] | None = None) -> ToolCall:
        call = ToolCall(tool_call_id=graph.reserve_tool_call_id(), tool_name=request.tool,
                        query_parameters=params if params is not None else request.params, purpose=request.purpose,
                        execution_status="not_applicable", requested_by=role, question_id=question_id,
                        message=_short(message), retrieval_time=self.clock(), charged_to="none")
        return graph.record_tool_call(call)

    @staticmethod
    def _not_applicable(spec: ToolSpec, params: dict[str, ParamValue], case: Case) -> str | None:
        v = case.variant
        if spec.assemblies and v.assembly not in spec.assemblies:
            return f"{spec.name} supports {', '.join(spec.assemblies)} only (this variant is {v.assembly})"
        if spec.variant_types and v.variant_type not in spec.variant_types:
            return f"{spec.name} covers {', '.join(spec.variant_types)} only (this variant is {v.variant_type})"
        if spec.requires_context and not case.supplied_context and not any(params.get(p) for p in CONTEXT_PARAMS):
            return f"{spec.name} needs a context: none was supplied and the request names none"
        return None

    @staticmethod
    def _article(spec: ToolSpec, params: dict[str, ParamValue]) -> str | None:
        """The article a full-text tool would read, from the first of its fulltext_params that is set."""
        return next((str(params[p]) for p in spec.fulltext_params if params.get(p)), None)

    @staticmethod
    def _requested_ids(spec: ToolSpec, params: dict[str, ParamValue]) -> set[str]:
        """That article's identifier in graph.article_key form; bare digits in a pmcid parameter are a PMCID."""
        name = next((p for p in spec.fulltext_params if params.get(p)), None)
        key = article_key(str(params[name]), pmcid="pmcid" in name.lower()) if name else None
        return {key} if key else set()

    @staticmethod
    def _earlier(graph: ClaimGraph, tool: str, params: dict[str, ParamValue]) -> ToolCall | None:
        """An executed call with the same tool and canonical parameters (refusals are never reused)."""
        return next((t for t in graph.tool_calls.values()
                     if t.tool_name == tool and t.charged_to != "none" and t.query_parameters == params), None)

    def _run(self, request: ToolRequest, case: Case, graph: ClaimGraph, role: Role,
             question_id: str | None) -> ToolCall:
        spec = self._spec(request.tool)
        if spec is None:
            names = ", ".join(s.name for s in self.specs()) or "none"
            return self._refuse(graph, request, role, question_id,
                                f"unknown tool '{request.tool}' (available: {names})")
        if self.allowed_tools is not None and spec.name not in self.allowed_tools:
            return self._refuse(graph, request, role, question_id, f"{spec.name} is not in this run's tool allowlist")
        if role in ROUTE_OF and ROUTE_OF[role] != spec.route:
            return self._refuse(graph, request, role, question_id,
                                f"{spec.name} is a {spec.route} tool; the {role.replace('_', ' ')} cannot request it")
        try:
            params = canonical_params(spec, request.params)
        except ToolRefusal as r:
            return self._refuse(graph, request, role, question_id, r.message)
        if reason := self._not_applicable(spec, params, case):
            return self._refuse(graph, request, role, question_id, reason, params)
        if earlier := self._earlier(graph, spec.name, params):
            return earlier
        charged: ChargedTo = "code" if role == "code" else "agent"
        snap = graph.budget_snapshot()
        if charged == "agent" and snap.tool_calls >= self.limits.max_tool_calls:
            return self._refuse(graph, request, role, question_id, f"tool budget exhausted ({snap.tool_calls} of "
                                f"{self.limits.max_tool_calls} agent tool calls used)", params)
        if charged == "code" and self.limits.max_code_calls is not None and snap.code_tool_calls >= \
                self.limits.max_code_calls:
            return self._refuse(graph, request, role, question_id, "code fact-collection budget exhausted", params)
        article = self._article(spec, params)
        if article and snap.fulltext_reads >= self.limits.fulltext_hard and \
                not self._requested_ids(spec, params) & set().union(*graph.fulltext_articles()):
            return self._refuse(graph, request, role, question_id, f"full-text budget exhausted ({snap.fulltext_reads} "
                                f"of {self.limits.fulltext_hard} articles read); re-reading one of those is free",
                                params)
        tid = graph.reserve_tool_call_id()
        ctx = ToolContext(spec=spec, case=case, graph=graph, config=self.config, mode=self.mode, http=self.http,
                          run_dir=self.run_dir, tool_call_id=tid, role=role, question_id=question_id)
        call, evidence = self._execute_call(tid, spec, request, params, ctx, charged, article)
        try:
            return graph.record_tool_call(call, evidence)
        except Exception as e:  # a GraphRefusal, or an item the graph could not take: the call is recorded anyway
            reason = e.reason if isinstance(e, GraphRefusal) else f"{type(e).__name__}: {e}"
            broken = call.model_copy(update={"execution_status": "error", "retrieval_status": "unknown",
                                             "observations": [], "fulltext_article": None, "read_article": None,
                                             "article_ids": [], "message": _short(f"adapter contract: {reason}")})
            return graph.record_tool_call(broken)

    def _execute_call(self, tid: str, spec: ToolSpec, request: ToolRequest, params: dict[str, ParamValue],
                      ctx: ToolContext, charged: ChargedTo, article: str | None) -> tuple[ToolCall, list[Evidence]]:
        """Run the adapter and build its ToolCall. Any failure on the way (the adapter, a malformed result, the raw
        file) becomes an error call under the same id, charged like a success, so it is never re-run for free."""
        try:
            result = self._execute(spec, params, ctx)
            if not isinstance(result, AdapterResult):
                raise TypeError(f"adapter returned {type(result).__name__}, not AdapterResult")
            evidence = [_checked_evidence(e) for e in result.evidence]
            data = _raw_bytes(result)
            path = f"raw/{tid}.json" if data is not None and self.run_dir is not None else None
            call = self._call(tid, spec, request, params, result, ctx.role, ctx.question_id, charged, article, path,
                              hashlib.sha256(data).hexdigest() if data is not None else None)
            if path is not None:
                self._write_raw(path, data)
            return call, evidence
        except Exception as e:  # an adapter failure is a recorded error, never an exception
            failed = AdapterResult(execution_status="error", message=f"{type(e).__name__}: {e}")
            return self._call(tid, spec, request, params, failed, ctx.role, ctx.question_id, charged, article, None,
                              None), []

    def _execute(self, spec: ToolSpec, params: dict[str, ParamValue], ctx: ToolContext) -> AdapterResult:
        adapter = self.registry.adapter(spec.name)
        if adapter is None:
            return AdapterResult(execution_status="unavailable", message=f"no adapter is registered for {spec.name}")
        return adapter(params, ctx)

    def _write_raw(self, path: str, data: bytes) -> None:
        """Write the raw result once (mode "xb": an existing file is an error, never overwritten)."""
        target = self.run_dir / path
        target.parent.mkdir(parents=True, exist_ok=True)
        with open(target, "xb") as f:
            f.write(data)

    def _call(self, tid: str, spec: ToolSpec, request: ToolRequest, params: dict[str, ParamValue],
              result: AdapterResult, role: Role, question_id: str | None, charged: ChargedTo, article: str | None,
              path: str | None, digest: str | None) -> ToolCall:
        """The ToolCall for an executed request. A full-text tool's call is a read only when it returned the article
        (success with records_found or incomplete): only then does it name the article (read_article, every id of it
        in article_ids) and, for full text, consume the full-text budget (fulltext_article). An empty or failed read
        costs no full-text budget and nothing can be extracted from it."""
        reader = (bool(spec.fulltext_params) and result.execution_status == "success"
                  and result.retrieval_status in EVIDENCE_FROM)
        read_article = (result.fulltext_article or article) if reader else None
        fulltext = read_article if reader and result.fulltext_read else None
        article_ids: list[str] = []
        if reader:
            ids = {article_key(read_article), *map(article_key, result.article_ids), *self._requested_ids(spec, params)}
            article_ids = sorted(k for k in ids if k)
        return ToolCall(tool_call_id=tid, tool_name=spec.name, tool_version=result.tool_version or spec.tool_version,
                        query_parameters=params, purpose=request.purpose, provider=result.provider or spec.provider,
                        dataset_release=result.dataset_release or spec.release(self.config),
                        assembly=result.assembly or (spec.assemblies[0] if spec.assemblies else None),
                        retrieval_time=result.retrieval_time or self.clock(), raw_result_hash=digest,
                        execution_status=result.execution_status, retrieval_status=result.retrieval_status,
                        observations=copy.deepcopy(result.observations), coverage=result.coverage,
                        raw_result_path=path, requested_by=role, question_id=question_id, cached=result.cached,
                        message=_short(result.message), charged_to=charged, fulltext_article=fulltext,
                        read_article=read_article, article_ids=article_ids)


def _case_identity(case: Case) -> str:
    """What tool answers depend on: the variant and any supplied context."""
    return json.dumps([case.variant.key, [s.model_dump(mode="json") for s in case.supplied_context]], sort_keys=True)


class RecordedToolRunner(ToolRunner):
    """Replay at the adapter level (SPEC 13.4): each (tool, canonical params) is answered from a saved bundle's
    tool_calls.jsonl, evidence.jsonl and raw/ (the raw bytes are copied, so hashes match), for the case the bundle's
    graph.json names. A request the bundle never executed, or a request for another variant or supplied context, gives
    execution_status "cache_miss" and is listed in `misses`. No adapter, HTTP or network is used; the specs still come
    from the registry, so import the adapter modules (or pass a registry) first."""

    def __init__(self, bundle_dir: str | Path, *, config: Config | None = None, run_dir: str | Path | None = None,
                 limits: ToolLimits | None = None, registry: ToolRegistry | None = None,
                 allowed_tools: list[str] | None = None, clock: Callable[[], str] | None = None):
        super().__init__(config=config, mode="cache_only", http=None, run_dir=run_dir, limits=limits,
                         registry=registry, allowed_tools=allowed_tools, clock=clock)
        self.bundle_dir = Path(bundle_dir)
        self.misses: list[str] = []
        self.recorded_case = Case.model_validate(json.loads((self.bundle_dir / "graph.json").read_text())["case"])
        self._recorded = self._load()

    def _load(self) -> dict[str, tuple[ToolCall, list[Evidence]]]:
        def lines(name: str) -> list[str]:
            path = self.bundle_dir / name
            return [x for x in path.read_text().splitlines() if x.strip()] if path.exists() else []

        evidence = {e.evidence_id: e for e in (Evidence.model_validate_json(x) for x in lines("evidence.jsonl"))}
        index: dict[str, tuple[ToolCall, list[Evidence]]] = {}
        for call in (ToolCall.model_validate_json(x) for x in lines("tool_calls.jsonl")):
            if call.charged_to != "none":
                index.setdefault(canonical_key(call.tool_name, call.query_parameters),
                                 (call, [evidence[i] for i in call.evidence_ids]))
        return index

    def _execute(self, spec: ToolSpec, params: dict[str, ParamValue], ctx: ToolContext) -> AdapterResult:
        key = canonical_key(spec.name, params)
        if _case_identity(ctx.case) != _case_identity(self.recorded_case):
            self.misses.append(key)
            return AdapterResult(execution_status="cache_miss",
                                 message=f"the saved bundle answers {self.recorded_case.variant.key} with its own "
                                         f"supplied context, not this case ({ctx.case.variant.key})")
        hit = self._recorded.get(key)
        if hit is None:
            self.misses.append(key)
            return AdapterResult(execution_status="cache_miss",
                                 message="not in the saved bundle: replaying this request would need a new tool call")
        call, evidence = hit
        raw = self.bundle_dir / call.raw_result_path if call.raw_result_path else None
        return AdapterResult(
            execution_status=call.execution_status, retrieval_status=call.retrieval_status,
            observations=copy.deepcopy(call.observations), coverage=call.coverage,
            evidence=[e.model_copy(update={"evidence_id": "", "retrieval_ref": None}) for e in evidence],
            raw_bytes=raw.read_bytes() if raw is not None and raw.exists() else None, message=call.message,
            provider=call.provider, dataset_release=call.dataset_release, tool_version=call.tool_version,
            assembly=call.assembly, cached=True, fulltext_article=call.read_article,
            fulltext_read=call.fulltext_article is not None, article_ids=list(call.article_ids),
            retrieval_time=call.retrieval_time)
