"""`v2m v9 ...`: the wiring of a v9 run, built in one factory (SPEC 12, 13.3, 13.4, 13.9, 13.16).

Why it is built this way:
- One factory, `wire`, builds every part a run needs, so a live run, a cache-only run, a synthetic fixture and a
  replay differ only where they must: where tool answers come from (the registered adapters over Http9, a fixture's
  stipulated responses, or a saved bundle) and where model replies come from (the provider, through agent/'s own
  transport, which alone reads the key from the environment; a fixture's scripts; or the response cache behind a
  transport that refuses to send).
- cache_only never reaches the network and never pays: Http9 is offline (a response that was never saved is recorded
  as cache_miss, which is missing data, not evidence) and the model transport refuses, so a reply the response cache
  does not hold stops the run with cache_miss (exit 2) instead of calling a provider. Its budget state lives in the
  run folder: nothing is spent and the profile's budget file is not touched.
- Every run gets a new folder (bundle.new_run_dir refuses an existing one; the default is <v9.runs_dir>/<request id>);
  the tool runner writes raw/ there during the run, then bundle.py writes the bundle and report.py the reports.
- A fixture run keeps its scripted replies, budget state and trace inside its own folder, never in cache/llm or the
  profile's budget: scripted replies are not model output. Its symbol table and group registry are empty, so the
  synthetic world never depends on data/.
- `evidence` is code's fact collection alone: no model call and no engine parts in the manifest, so the report calls
  the folder an evidence bundle. Like the engine, it ends as an input limitation (stop reason input_invalid) when the
  stated reference allele does not match GRCh38.
- `fill` is the evidence bundle taken to an answer by code alone (fill.py): the same collection, then the lookups the
  candidates need, a claim for everything a record can count for, every record linked through the graph's gates,
  and the chain table (table.json, table.md) beside the reports. No model client is built, so it cannot spend. Its
  runner also knows the code-only tools (fill_tools.py), which sit in a registry of their own, so the tools a role
  is shown, and with them the prompts of every saved run, do not change.
- `fill --read` adds the reader (reader.py): a model client is built, as for `run`, and used for one thing only, one
  call per article. Its calls are capped by the number of articles, its spend by the profile's budget, and in
  cache-only mode a reply that is not cached stops the reading (cache_miss, exit 2) instead of calling a provider.
- config.yaml's v9 block is checked before a new run: the call guard and the literature policy it states are fixed in
  code, and every allowlisted tool must exist, so the config never claims what the code does not do.
- The evaluator's commands (audit, eval) are wired in cli.py: no v9 module but the evaluator itself may import it,
  which keeps gold material out of every engine path.
- Nothing here reads, prints or stores an environment variable or a key.
"""

import hashlib
import json
import re
import sys
import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from ..agent.llm import Budget, LLMClient
from ..config import Config, ConfigError, load_config, profile_config
from . import roles as R
from .bundle import build_manifest, export_public, new_run_dir, write_bundle, write_new
from .chain import chain_view
from .fixtures import FIXTURE_DIR, Fixture, FixtureToolRunner, ScriptedResponses, ScriptExhausted, load_fixture
from .graph import ClaimGraph, GroupRegistry, SymbolResolver
from .http9 import Http9
from .intake import IntakeError, Request, build_case
from .investigate import Engine, EngineLimits, Facts, default_groups, default_resolver, fixture_facts
from .replay import ReplayMiss
from .report import write_reports
from .schemas import Case, RunMode, RunResult, ToolCall, ToolRequest
from .tools import REGISTRY, RecordedToolRunner, ToolLimits, ToolRunner, ToolSpec

Transport = Callable[[dict], dict]

MODES: dict[str, RunMode] = {"live": "live", "cache-only": "cache_only"}
FIXTURE_ALIASES = {"synthetic": "synthetic_repair"}
FIXTURE_NAME = re.compile(r"[A-Za-z0-9_]+")
# A refusing or scripted transport never spends, but LLMClient reserves a worst case before each send: the limit only
# has to be large enough that the reservation never refuses first (a miss would then look like a budget stop).
OFFLINE_BUDGET_USD = 1e9
FIXTURE_BUDGET_USD = 1.0
# Stop reasons that end a command with a non-zero exit: 2 when the input or the caches cannot give a result (the
# report still says why), 1 when the engine could not investigate.
STOP_EXIT = {"cache_miss": 2, "input_invalid": 2, "unsupported_variant": 2, "engine_error": 1}
EVIDENCE_PURPOSE = "evidence bundle: what the source reports at the variant, with no TF, gene or trait named"
# CIViC is searched by gene and variant name, so it applies to nothing without them; collect_facts runs it for a
# somatic variant with the genes VEP names (SPEC 6 step 2).
LEFT_TO_FACTS = frozenset({"civic_lookup"})


# --- config ----------------------------------------------------------------------------------------------------------

def register_tools() -> Any:
    """Import the tool modules, which register their tools in tools.REGISTRY on import: a runner (or a recorded runner)
    built before this would know no tool. Returns the adapters module (collect_facts lives there)."""
    from . import adapters, literature  # noqa: F401  (imported for their registrations)
    return adapters


def literature_policy() -> dict[str, int]:
    """What the literature route does, as config.yaml's v9.literature states it (fixed in literature.py)."""
    from . import literature
    return {"max_results": literature.MAX_RESULTS, "read_chars": literature.RETURN_LIMIT,
            "passage_chars": literature.PASSAGE_MAX}


def allowlist(cfg: Mapping[str, Any]) -> list[str] | None:
    """config.yaml's v9.tool_allowlist (None: every registered tool)."""
    allowed = (cfg.get("v9") or {}).get("tool_allowlist")
    return [str(t) for t in allowed] if allowed is not None else None


def check_config(cfg: Mapping[str, Any]) -> None:
    """Refuse a v9 block that states what the code does not do: the call guard (roles.GUARD) and the literature policy
    (literature.py) are fixed in code, and every allowlisted tool must be registered. ConfigError says what differs."""
    v9 = cfg.get("v9") or {}
    problems = []
    guard = (v9.get("limits") or {}).get("call_guard")
    if guard is not None and guard != R.GUARD:
        problems.append(f"v9.limits.call_guard is {guard}, but one structured call can take {R.GUARD} sends "
                        "(roles.GUARD)")
    fixed = literature_policy()
    for key, value in (v9.get("literature") or {}).items():
        if key not in fixed:
            problems.append(f"v9.literature.{key} is not a setting of the literature route (it has "
                            f"{', '.join(fixed)})")
        elif value != fixed[key]:
            problems.append(f"v9.literature.{key} is {value}, but the literature route uses {fixed[key]}")
    allowed = allowlist(cfg)
    if allowed is not None:
        register_tools()
        unknown = sorted(set(allowed) - set(REGISTRY.names()))
        if unknown:
            problems.append(f"v9.tool_allowlist names tools that do not exist: {', '.join(unknown)}")
    if problems:
        raise ConfigError("config.yaml: " + "; ".join(problems))


# --- model transports --------------------------------------------------------------------------------------------------

def refusing(what: str) -> Transport:
    """A model transport that never sends: every reply must come from the response cache. It raises ReplayMiss, which
    RoleCaller reads as a replay miss, so the engine stops with cache_miss at once instead of deciding without it."""
    def send(body: dict) -> dict:
        raise ReplayMiss(f"{body.get('model')}: {what} takes model replies from the response cache only, and this one "
                         "is not there (it would need a paid call)")
    return send


def scripted(fixture: Fixture) -> Transport:
    """A fixture's role scripts as a model transport (roles.script_role tells which role a request is for). A call the
    script does not cover is a miss (ReplayMiss), never a provider call."""
    send = ScriptedResponses.from_fixture(fixture).transport(R.script_role)

    def transport(body: dict) -> dict:
        try:
            return send(body)
        except ScriptExhausted as e:
            raise ReplayMiss(f"{e}: the fixture scripts no reply for this call") from None
    return transport


# --- the factory -------------------------------------------------------------------------------------------------------

@dataclass
class Wiring:
    """The parts of one run, built by wire(): one tool runner, one model client and role caller (none for an evidence
    bundle), the engine's limits, fact collection, symbol table and group registry, all on one run folder."""
    cfg: Config
    mode: RunMode
    run_dir: Path
    limits: EngineLimits
    runner: ToolRunner
    facts: Facts
    resolver: SymbolResolver | None
    groups: GroupRegistry | None
    http: Http9 | None = None
    client: LLMClient | None = None
    roles: R.RoleCaller | None = None
    critic: R.RoleCaller | None = None           # the fill's critic, on a model client of its own (critic.py)
    critic_settings: dict[str, Any] | None = None
    judge: R.RoleCaller | None = None            # the fill's judge, on another client of the same model (judge.py)
    judge_settings: dict[str, Any] | None = None
    loop: Any = None                             # the fill's loop, once a run has built it (loop.Loop)

    def engine(self) -> Engine:
        """A new Engine for one run (one RoleCaller and one Engine per run)."""
        if self.roles is None:
            raise ValueError("this wiring has no model client: an evidence bundle runs no engine")
        return Engine(self.cfg, self.mode, self.roles, self.runner, self.run_dir, limits=self.limits,
                      facts=self.facts, resolver=self.resolver, groups=self.groups)

    def graph(self, case: Case) -> ClaimGraph:
        """An empty claim graph for a run without the engine (an evidence bundle)."""
        return ClaimGraph(case, self.resolver, self.groups)

    def http_counts(self) -> dict[str, int] | None:
        if self.http is None:
            return None
        return {"requests_made": self.http.requests_made, "cache_hits": self.http.cache_hits}


def wire(cfg: Config, mode: RunMode, run_dir: Path, *, http: Http9 | None = None, models: bool = True,
         fixture: Fixture | None = None, recorded: Path | None = None, limits: EngineLimits | None = None,
         tool_limits: ToolLimits | None = None, code_tools: bool = False,
         critic: Mapping[str, Any] | bool = False, judge: Mapping[str, Any] | bool = False,
         models_offline: bool = False) -> Wiring:
    """Build one run's parts on `run_dir` (an existing, new folder: the runner writes raw/ there).

    - With `fixture`: the fixture's tools (or, with `recorded`, a saved fixture bundle's answers) and its scripted
      replies, with the budget state, trace and model cache inside run_dir; empty symbol table and group registry.
    - Otherwise the registered tools (adapters and literature are imported first) over `http` (Http9.from_config,
      offline unless `mode` is live) or, with `recorded`, the saved bundle's answers (RecordedToolRunner); the config's
      tool allowlist; adapters.collect_facts; the HGNC symbol table (SymbolResolver.from_hgnc on data.hgnc) and the
      QBiC-SELEX group registry (GroupRegistry.from_groups_json on cache.groups). Model replies come from the provider
      in live mode (LLMClient's own transport and the profile's dev budget), and otherwise from the response cache
      behind a refusing transport, with the budget state in run_dir. `models=False` builds no model client.
    `limits` default to config.yaml's v9.limits; `tool_limits` to the engine's (a replay passes the saved run's).
    `code_tools` adds the code-only tools (fill_tools.py) to the runner, from a registry of their own.
    `critic` adds the fill's critic (critic.py): a second model client with the critic's provider and model (the
    config's, or the settings given: a saved run's, for its replay), live or cache-only as the first one is, on the
    same trace and budget. `judge` adds the fill's judge (judge.py) the same way: the second model's settings on a
    client of its own. `models_offline`: in live mode, the tools use the network and no model is ever sent a
    request (replies come from the response cache or the call fails): what a dry run of the loop needs, so that
    looking at what it would read costs nothing."""
    limits = limits or EngineLimits.from_config(cfg)
    tool_limits = tool_limits or limits.tool_limits()
    trace = run_dir / "trace.jsonl"
    if fixture is not None:
        runner: ToolRunner = (
            RecordedToolRunner(recorded, config=cfg, run_dir=run_dir, limits=tool_limits,
                               registry=FixtureToolRunner(fixture).registry) if recorded is not None
            else FixtureToolRunner(fixture, run_dir=run_dir, limits=tool_limits))
        client = LLMClient(cfg, transport=scripted(fixture), phase="dev", trace_path=trace, cache_dir=run_dir / "llm",
                           budget=Budget(run_dir / "budget.json", {"dev": FIXTURE_BUDGET_USD}))
        wiring = Wiring(cfg, "fixture", run_dir, limits, runner, fixture_facts, SymbolResolver({}),
                        GroupRegistry({}), client=client)
    else:
        adapters = register_tools()
        registry, allowed = None, allowlist(cfg)
        if code_tools:
            from . import fill_tools
            registry, allowed = fill_tools.registry(), fill_tools.allowed(allowed)
        if recorded is not None:
            http = None
            runner = RecordedToolRunner(recorded, config=cfg, run_dir=run_dir, limits=tool_limits,
                                        registry=registry, allowed_tools=allowed)
        else:
            http = http or Http9.from_config(cfg, offline=(mode != "live"))
            runner = ToolRunner(cfg, mode, http, run_dir, limits=tool_limits, registry=registry,
                                allowed_tools=allowed)
        client = None
        if models and mode == "live" and recorded is None and not models_offline:
            client = LLMClient(cfg, phase="dev", trace_path=trace)
        elif models:
            what = ("this replay" if recorded is not None else
                    "a dry run" if models_offline and mode == "live" else "a cache-only run")
            client = LLMClient(cfg, transport=refusing(what), phase="dev", trace_path=trace,
                               budget=Budget(run_dir / "budget.json", {"dev": OFFLINE_BUDGET_USD}))
        wiring = Wiring(cfg, mode, run_dir, limits, runner, adapters.collect_facts, default_resolver(cfg),
                        default_groups(cfg), http=http, client=client)
    if wiring.client is not None:
        wiring.roles = R.RoleCaller(wiring.client, cfg)
    def second_model(given: Mapping[str, Any] | bool) -> tuple[R.RoleCaller, dict[str, Any]]:
        """A role caller on a client of the second model (critic.critic_config), with the settings it runs with."""
        from . import critic as K
        live = mode == "live" and recorded is None and not models_offline
        chosen = {**K.settings(cfg), **(given if isinstance(given, Mapping) else {})}
        second = K.critic_config(cfg, chosen, offline=not live)
        client = (LLMClient(second, phase="dev", trace_path=trace) if live else
                  LLMClient(second, transport=refusing("this replay" if recorded is not None else "a cache-only run"),
                            phase="dev", trace_path=trace,
                            budget=Budget(run_dir / "budget.json", {"dev": OFFLINE_BUDGET_USD})))
        return R.RoleCaller(client, second), chosen

    if critic and wiring.client is not None and fixture is None:
        wiring.critic, wiring.critic_settings = second_model(critic)
    if judge and wiring.client is not None and fixture is None:
        wiring.judge, wiring.judge_settings = second_model(judge)
    return wiring


# --- the evidence bundle -----------------------------------------------------------------------------------------------

def normalise(graph: ClaimGraph) -> bool:
    """The engine's normalise step for a run without the engine: record the variant's identity, and end as an input
    limitation when the stated reference allele does not match the reference genome (input_invalid) or the assembly is
    not GRCh38 (unsupported_variant). Returns whether collection may go on."""
    v = graph.case.variant
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
        reason, detail = problem
        graph.log("stop", "code", f"{reason}: {detail}", details={"stop_reason": reason, "round": 0, "detail": detail})
        graph.set_result(RunResult(outcome="input_or_capability_limitation", stop_reason=reason,
                                   summary=f"No evidence collected: {detail}."), "code")
        return False
    if v.variant_type != "SNV":
        graph.log("normalize", "code", f"a {v.variant_type}: QBiC-SELEX predictions do not apply; the other tools "
                                       "run", details={"qbic": "not_applicable"})
    return True


def _applies(spec: ToolSpec, case: Case) -> bool:
    """The ToolSpec's own scope: the runner would refuse anything outside it (uncharged)."""
    v = case.variant
    return ((not spec.assemblies or v.assembly in spec.assemblies)
            and (not spec.variant_types or v.variant_type in spec.variant_types)
            and (not spec.requires_context or bool(case.supplied_context)))


def evidence_requests(graph: ClaimGraph, runner: ToolRunner) -> list[ToolRequest]:
    """The computational tools collect_facts did not run that apply to the variant with no argument, in name order:
    no required parameter and no one-of choice (a TF, gene or group to name), and the tool's assembly, variant types
    and context needs met. chip_occupancy then surveys every factor, gtex_eqtl every gene and tissue, and
    credible_sets_l2g every trait; civic_lookup is left to collect_facts."""
    case, done = graph.case, {t.tool_name for t in graph.tool_calls.values()}
    return [ToolRequest(tool=spec.name, purpose=EVIDENCE_PURPOSE) for spec in runner.specs("computational")
            if spec.name not in done and spec.name not in LEFT_TO_FACTS and not spec.one_of
            and not any(p.required for p in spec.params.values()) and _applies(spec, case)]


def collect_evidence(graph: ClaimGraph, runner: ToolRunner) -> list[ToolCall]:
    """What `v2m v9 evidence` collects, as role code and with no model call: the normalise step, adapters.collect_facts,
    then evidence_requests. A replay of an evidence bundle runs exactly this again. Never raises for a tool failure:
    every call is recorded with its status."""
    if not normalise(graph):
        return []
    calls = register_tools().collect_facts(graph.case, graph, runner)
    extra = [runner.run(request, graph.case, graph, "code") for request in evidence_requests(graph, runner)]
    if extra:
        graph.log("collect_facts", "code", "evidence bundle: " + "; ".join(
            f"{c.tool_call_id} {c.tool_name}: {c.execution_status}/{c.retrieval_status}" for c in extra),
            target_ids=[c.tool_call_id for c in extra], evidence_ids=[e for c in extra for e in c.evidence_ids])
    return calls + extra


# --- fixtures ----------------------------------------------------------------------------------------------------------

def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve_fixture(name: str) -> tuple[str, Path]:
    """A fixture by its name in v9/fixtures ("synthetic" is synthetic_repair) or by path: (how the manifest records
    it, the file)."""
    stem = FIXTURE_ALIASES.get(name, name)
    if FIXTURE_NAME.fullmatch(stem) and (FIXTURE_DIR / f"{stem}.json").is_file():
        return stem, FIXTURE_DIR / f"{stem}.json"
    path = Path(name).expanduser()
    if path.is_file():
        return str(path.resolve()), path.resolve()
    names = ", ".join(sorted(p.stem for p in FIXTURE_DIR.glob("*.json")))
    raise FileNotFoundError(f"no fixture {name!r}: give synthetic, a fixture name ({names}) or a fixture file")


def recorded_fixture(request: Mapping[str, Any]) -> tuple[Fixture, bool]:
    """The fixture a saved fixture run names in its manifest request, and whether its file is unchanged since the run.
    The manifest is data: only a plain name in v9/fixtures or an existing file is read, and only as a Fixture."""
    source = request.get("fixture")
    if not isinstance(source, str) or not source:
        raise ValueError("the saved fixture run does not name its fixture")
    path = FIXTURE_DIR / f"{source}.json" if FIXTURE_NAME.fullmatch(source) else Path(source)
    if not path.is_file():
        raise FileNotFoundError(f"the saved run's fixture {source} is no longer there")
    return load_fixture(path), _sha256(path) == request.get("fixture_sha256")


# --- writing a run -----------------------------------------------------------------------------------------------------

def save(w: Wiring, graph: ClaimGraph, metrics: Mapping[str, Any], manifest_parts: Mapping[str, Any], *,
         request: Mapping[str, Any], case: Case, profile: str | None, extra: Mapping[str, Any] | None = None) -> bool:
    """Write the run's bundle (bundle.build_manifest, write_bundle) and then its reports (report.write_reports) into
    the run folder. `case` is the case as the run started (the graph's own may have gained inferred candidates).
    Returns whether the reports were written: a report that cannot be rendered leaves a complete bundle, which
    `v2m v9 report` can render later."""
    manifest = build_manifest(request=request, case=case, mode=w.mode, config=w.cfg, manifest_parts=manifest_parts,
                              graph=graph, profile=profile)
    write_bundle(graph, metrics, {**manifest, **(extra or {})}, w.run_dir)
    try:
        write_reports(w.run_dir)
    except Exception as e:  # the bundle stands; say what broke and how to render it later
        print(f"report not written ({type(e).__name__}: {e}); the bundle is complete: render it with "
              f"`v2m v9 report --run {w.run_dir}`", file=sys.stderr)
        return False
    return True


def summary(graph: ClaimGraph, run_dir: Path, metrics: Mapping[str, Any]) -> str:
    """A few lines on what a run did, for the terminal (the report has everything)."""
    r = graph.result
    executed = [t for t in graph.tool_calls.values() if t.charged_to != "none"]
    missing = sorted({t.tool_name for t in executed if t.execution_status == "cache_miss"})
    head = (f"{r.outcome}, stop reason {r.stop_reason}" if r is not None
            else "evidence bundle (code's fact collection, no model call)")
    lines = [f"{graph.case.case_id} ({graph.case.variant.key}): {head}",
             f"  {metrics.get('model_calls', 0)} model call(s), ${float(metrics.get('cost_usd') or 0.0):.4f}; "
             f"{len(executed)} tool call(s); {len(graph.evidence)} evidence item(s); {len(graph.hypotheses)} "
             "hypothesis(es)"]
    if headline := chain_view(graph)["ranked"]["headline"]:
        lines.append(f"  answer: {headline}")
    if r is not None and r.summary:
        lines.append(f"  {r.summary}")
    if missing:
        lines.append(f"  no saved response for {', '.join(missing)} (cache_miss: missing data, never evidence)")
    lines.append(f"run folder: {run_dir}")
    return "\n".join(lines)


def exit_code(graph: ClaimGraph, reported: bool) -> int:
    code = STOP_EXIT.get(graph.result.stop_reason if graph.result is not None else "", 0)
    return code if code or reported else 1


def _refused(command: str, error: Exception) -> int:
    text = getattr(error, "message", None) or (error.args[0] if isinstance(error, KeyError) and error.args
                                               else str(error))
    print(f"v9 {command}: {text}", file=sys.stderr)
    return 2


def _profile_name(name: str | None) -> str | None:
    """The profile a command runs with, as the manifest records it (None for the bare settings)."""
    name = name or load_config().get("default_profile")
    return None if name in (None, "", "none") else str(name)


def reader_limits(cfg: Mapping[str, Any], articles: int) -> ToolLimits:
    """The tool limits of a fill with the reader: the config's, with room in the full-text budget for every article
    the reader may fetch (it fetches more than it sends to the model: an article that does not name the variant in
    its text costs a fetch and no call)."""
    from .reader import FETCH_FACTOR
    limits = EngineLimits.from_config(cfg).tool_limits()
    room = max(limits.fulltext_hard, FETCH_FACTOR * articles)
    return limits.model_copy(update={"fulltext_soft": room, "fulltext_hard": room})


def _start(args: Any, *, models: bool, code_tools: bool = False, articles: int | None = None,
           critic: bool = False, judge: bool = False, models_offline: bool = False
           ) -> tuple[Wiring, Request, Case, str | None]:
    """Config, intake and a new run folder for `run`, `evidence` and `fill`. Raises IntakeError, ConfigError,
    FileExistsError or ValueError (a refused request or setting). `articles`: the reader's cap, for `fill --read`;
    `critic`: whether the fill has its second reading (`fill --read --critic`); `judge`: whether it has a tie read
    (`fill --read --judge`)."""
    cfg = profile_config(args.profile)
    check_config(cfg)
    mode = MODES[args.mode]
    out = Path(args.out) if args.out else None
    if out is not None and out.exists():         # before intake, which may use the network in live mode
        raise FileExistsError(f"{out} already exists: a run folder is never reused or overwritten; choose a new path")
    http = Http9.from_config(cfg, offline=(mode != "live"))
    request = Request(variant=args.variant, origin=args.origin, disease=list(args.disease or []),
                      context=list(args.context or []), request_id=args.request_id)
    case = build_case(request, config=cfg, http=http, mode=mode)
    run_dir = new_run_dir(out or cfg.path("v9", "runs_dir") / case.case_id)
    tool_limits = reader_limits(cfg, articles) if articles else None
    return (wire(cfg, mode, run_dir, http=http, models=models, code_tools=code_tools, tool_limits=tool_limits,
                 critic=critic, judge=judge, models_offline=models_offline), request, case,
            _profile_name(args.profile))


# --- the commands ------------------------------------------------------------------------------------------------------

def run_command(args: Any) -> int:
    """`v2m v9 run`: one investigation, written as a bundle with its reports. Exit 0 with a result; 2 for a refused
    request, an input the engine cannot assess, or a cache-only run whose model reply is not cached; 1 when the engine
    could not investigate (the bundle and report say why)."""
    try:
        w, request, case, profile = _start(args, models=True)
    except (IntakeError, ConfigError, FileExistsError, ValueError) as e:
        return _refused("run", e)
    result = w.engine().run(case)
    metrics = {**result.metrics, **({"http": w.http_counts()} if w.http is not None else {})}
    reported = save(w, result.graph, metrics, result.manifest_parts, request=request.model_dump(mode="json"),
                    case=case, profile=profile)
    print(summary(result.graph, w.run_dir, metrics))
    return exit_code(result.graph, reported)


def evidence_command(args: Any) -> int:
    """`v2m v9 evidence`: code's fact collection for one variant (collect_evidence), written as an evidence bundle
    (no engine parts in the manifest) with its reports."""
    started = time.monotonic()
    try:
        w, request, case, profile = _start(args, models=False)
    except (IntakeError, ConfigError, FileExistsError, ValueError) as e:
        return _refused("evidence", e)
    graph = w.graph(case)
    collect_evidence(graph, w.runner)
    metrics = {"wall_seconds": round(time.monotonic() - started, 3),
               **({"http": w.http_counts()} if w.http is not None else {})}
    reported = save(w, graph, metrics, {}, request=request.model_dump(mode="json"), case=case, profile=profile)
    print(summary(graph, w.run_dir, metrics))
    return exit_code(graph, reported)


def fill_graph(w: Wiring, case: Case, *, articles: int | None = None,
               loop: Mapping[str, Any] | None = None, skip_unread: bool = False
               ) -> tuple[ClaimGraph, dict[str, Any]]:
    """The fill of one case on a wiring built with code_tools: the evidence bundle, then fill.run, with the reader
    when `articles` (its cap) is given and the wiring has a model client, and with the critic and the judge when the
    wiring has them. `loop` (its settings: planner, rounds, articles, dry) adds the loop that goes back for articles
    after the first reading (loop.py); it needs the reader. `skip_unread`: an article whose reading the response
    cache does not hold is listed as not read and the run goes on, where a cache-only run otherwise stops at it.
    Returns the graph and the fill's counts (empty when the input could not be assessed). A replay runs exactly
    this again."""
    from . import fill
    graph = w.graph(case)
    collect_evidence(graph, w.runner)
    reader = critic = judge = again = None
    if articles and w.roles is not None:
        from .reader import Reader
        reader = Reader(w.roles, w.runner, max_articles=articles)
        reader.keep_going = skip_unread or bool(loop and loop.get("dry"))
        if w.critic is not None:
            from .critic import Critic
            critic = Critic(w.critic, w.runner.run_dir)
        if w.judge is not None:
            from .judge import Judge
            judge = Judge(w.judge, w.runner.run_dir)
        if loop is not None:
            from .loop import Loop
            again = Loop(w.roles if loop.get("planner") == "model" else None, max_rounds=int(loop["rounds"]),
                         round_articles=int(loop["articles"]), dry=bool(loop.get("dry")))
            w.loop = again
    return graph, (fill.run(graph, w.runner, reader, critic, judge, again) if graph.result is None else {})


def loop_settings(args: Any, read: bool) -> dict[str, Any] | None:
    """The loop's settings from the command line (`fill --read --loop ...`), or None without --loop. A dry run
    plans by code: no model is sent anything in one."""
    from . import loop as LP
    who = getattr(args, "loop", None)
    dry = bool(getattr(args, "loop_dry", False))
    rounds, per_round = getattr(args, "loop_rounds", None), getattr(args, "loop_articles", None)
    if who is None:
        if dry or rounds is not None or per_round is not None:
            raise ValueError("--loop-rounds, --loop-articles and --loop-dry need --loop")
        return None
    if not read:
        raise ValueError("--loop goes back for articles after the first reading, so it needs --read")
    rounds = LP.MAX_ROUNDS if rounds is None else rounds
    per_round = LP.ROUND_ARTICLES if per_round is None else per_round
    if rounds < 1 or per_round < 1:
        raise ValueError("--loop-rounds and --loop-articles must be at least 1")
    return {"planner": "code" if dry else who, "rounds": rounds, "articles": per_round, "dry": dry}


def loop_room(settings: Mapping[str, Any]) -> int:
    """The articles a loop may fetch beyond the first reading's: what its rounds read, and the reviews they open."""
    from . import loop as LP
    return int(settings["rounds"]) * (int(settings["articles"]) + LP.FOLLOW_REVIEWS)


def fill_manifest(w: Wiring, counts: Mapping[str, Any], articles: int | None) -> dict[str, Any]:
    """The engine part of a fill's manifest (fill.manifest_parts), with the reader's settings and the tool limits it
    ran with when it had a reader, so a replay reads the same articles."""
    from . import fill
    if not counts:
        return {}
    if not articles or w.roles is None:
        return fill.manifest_parts(counts)
    from . import reader
    second = third = None
    if w.critic is not None:
        from . import critic
        second = critic.manifest_parts(w.critic, w.critic_settings or {})
    if w.judge is not None:
        from . import judge
        third = judge.manifest_parts(w.judge, w.judge_settings or {})
    again = None
    if w.loop is not None:
        from . import loop
        again = loop.manifest_parts(w.loop.planner, w.loop)
    return fill.manifest_parts(counts, reader.manifest_parts(w.roles, articles),
                               w.runner.limits.model_dump(mode="json"), second, third, again)


def model_metrics(w: Wiring) -> dict[str, Any]:
    """What the model calls of a run cost, for metrics.json (nothing when the wiring has no model client)."""
    if w.roles is None:
        return {}
    callers = [c for c in (w.roles, w.critic, w.judge) if c is not None]
    usage = {k: dict(v) for caller in callers for k, v in caller.usage.items()}
    return {"model_calls": sum(c.calls_used for c in callers),
            "cost_usd": round(sum(c.cost_usd for c in callers), 6),
            "model_usage_by_role": dict(sorted(usage.items())),
            "failures": [f for c in callers for f in c.failures]}


def write_table(run_dir: Path, graph: ClaimGraph) -> list[str]:
    """table.json and table.md beside a run's reports: the chain table of its graph and the rules it breaks (none,
    for a fill). Returns one line per broken rule."""
    from . import table as T
    table = T.from_graph(graph)
    problems = T.check(table, graph)
    write_new(run_dir / "table.json", table.model_dump_json(indent=1))
    write_new(run_dir / "table.md", T.to_markdown(table, problems))
    return [f"{p.rule}: {p.where}: {p.text}" for p in problems]


def fill_command(args: Any) -> int:
    """`v2m v9 fill`: the chain table of one variant filled by code (fill.py), written as a bundle with its reports
    and the table. No model is called unless --read is given, which adds the reader (reader.py): one model call per
    article, at most --max-articles of them. With --critic as well, a second model from another provider reads the
    experiments that are the only record behind a cell against the claims they count for (critic.py): one call
    per such experiment. With --judge, when chains tie for first, that second model also reads the experiments no
    cell counts for the tied TFs and genes (judge.py): at most two calls.
    Exit 0 with a table; 2 for a refused request, an input that cannot be assessed, or a cache-only reading whose
    reply is not cached; 1 when the table breaks one of its own rules (the folder is complete and says which)."""
    from .reader import MAX_ARTICLES
    started = time.monotonic()
    read = bool(getattr(args, "read", False))
    second = bool(getattr(args, "critic", False))
    third = bool(getattr(args, "judge", False))
    asked = getattr(args, "max_articles", None)
    articles = (MAX_ARTICLES if asked is None else asked) if read else None
    try:
        if articles is not None and articles < 1:
            raise ValueError("--max-articles must be at least 1")
        if second and not read:
            raise ValueError("--critic checks what the reader files, so it needs --read")
        if third and not read:
            raise ValueError("--judge reads the experiments the reader files, so it needs --read")
        again = loop_settings(args, read)
        room = articles + loop_room(again) if articles and again else articles
        w, request, case, profile = _start(args, models=read, code_tools=True, articles=room, critic=second,
                                           judge=third, models_offline=bool(again and again["dry"]))
    except (IntakeError, ConfigError, FileExistsError, ValueError) as e:
        return _refused("fill", e)
    graph, counts = fill_graph(w, case, articles=articles, loop=again,
                               skip_unread=bool(getattr(args, "skip_unread", False)))
    metrics = {"wall_seconds": round(time.monotonic() - started, 3), "fill": counts, **model_metrics(w),
               **({"http": w.http_counts()} if w.http is not None else {})}
    reported = save(w, graph, metrics, fill_manifest(w, counts, articles),
                    request=request.model_dump(mode="json"), case=case, profile=profile)
    broken = write_table(w.run_dir, graph)
    print(summary(graph, w.run_dir, metrics))
    if broken:
        print(f"  the table breaks {len(broken)} rule(s); see table.md", file=sys.stderr)
    return exit_code(graph, reported) or (1 if broken else 0)


def fixture_command(args: Any) -> int:
    """`v2m v9 fixture NAME --out DIR`: the engine on a synthetic fixture with its scripted roles (no network, no
    provider, no data/), written as a bundle with its reports."""
    try:
        source, path = resolve_fixture(args.fixture)
        fixture = load_fixture(path)
        cfg = profile_config(args.profile)
        run_dir = new_run_dir(args.out)
    except (FileNotFoundError, FileExistsError, ValueError, ConfigError) as e:
        return _refused("fixture", e)
    w = wire(cfg, "fixture", run_dir, fixture=fixture)
    result = w.engine().run(fixture.case)
    request = {"fixture": source, "fixture_sha256": _sha256(path)}
    reported = save(w, result.graph, result.metrics, result.manifest_parts, request=request, case=fixture.case,
                    profile=_profile_name(args.profile))
    print(summary(result.graph, w.run_dir, result.metrics))
    return exit_code(result.graph, reported)


def report_command(args: Any) -> int:
    """`v2m v9 report --run DIR [--out NEW]`: report.html and report.md from a saved run (into a new folder with
    --out, as a render-only report)."""
    try:
        paths = write_reports(args.run, args.out)
    except (FileNotFoundError, FileExistsError, ValueError) as e:
        return _refused("report", e)
    for p in paths:
        print(p)
    return 0


def export_command(args: Any) -> int:
    """`v2m v9 export --run DIR --out NEW`: a public copy of a run (bundle.export_public, SPEC 13.11)."""
    try:
        out = export_public(args.run, args.out)
    except (FileNotFoundError, FileExistsError, ValueError) as e:
        return _refused("export", e)
    print(out)
    return 0


def is_v9_run(path: Path) -> bool:
    """A v9 run folder: graph.json and a manifest the v9 engine wrote."""
    try:
        manifest = json.loads((Path(path) / "manifest.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return (isinstance(manifest, dict) and str(manifest.get("engine_version", "")).startswith("v9")
            and (Path(path) / "graph.json").is_file())


def default_replay_out(saved: Path) -> Path:
    """<runs>/replay/v9/<run folder name>-<UTC time>, beside config.yaml's own v9.runs_dir (a replay folder is new)."""
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    return load_config().path("v9", "runs_dir").parent / "replay" / "v9" / f"{Path(saved).name}-{stamp}"


def replay_folder(saved: Path, out: Path | None = None, *, render_only: bool = False) -> int:
    """`v2m v9 replay DIR` (and `v2m replay DIR` on a v9 run folder): replay9.replay into a new folder, printing the
    outcome; with render_only, the saved run's reports rendered into a new folder instead, re-running nothing."""
    from . import replay9
    saved = Path(saved)
    try:
        out = Path(out) if out is not None else default_replay_out(saved)
    except ConfigError as e:
        print(f"replay: {e}", file=sys.stderr)
        return 1
    if render_only:
        try:
            paths = write_reports(saved, out)
        except (FileNotFoundError, FileExistsError, ValueError) as e:
            print(f"replay: {e}", file=sys.stderr)
            return 1
        for p in paths:
            print(p)
        return 0
    r = replay9.replay(saved, out)
    print(r.line())
    for d in r.differences[:20]:
        print(f"  {d}")
    if len(r.differences) > 20:
        print(f"  ... and {len(r.differences) - 20} more")
    for why in r.reasons:
        print(f"  not replayable: {why}")
    for item in r.missing:
        print(f"  missing: {item}")
    for miss in r.tool_misses[:10]:
        print(f"  a tool request the saved run never made: {miss}")
    for note in r.notes:
        print(f"  note: {note}")
    if r.written:
        print(f"output: {out}")
    return r.code


def replay_command(args: Any) -> int:
    return replay_folder(Path(args.run_dir), Path(args.out) if args.out else None)


COMMANDS: dict[str, Callable[[Any], int]] = {
    "evidence": evidence_command, "fill": fill_command, "run": run_command, "report": report_command,
    "replay": replay_command, "fixture": fixture_command, "export": export_command,
}


def main(args: Any) -> int:
    """Dispatch one `v2m v9` subcommand (cli.py parses; audit and eval are the evaluator's, wired in cli.py)."""
    return COMMANDS[args.v9_command](args)
