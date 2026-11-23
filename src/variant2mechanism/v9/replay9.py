"""Replay of a saved v9 run (SPEC 8, 13.4): re-run it offline from its own bundle into a new folder and compare
graph.json.

Why it is built this way:
- Tool answers come from the saved bundle (RecordedToolRunner: tool_calls.jsonl, evidence.jsonl and raw/), never from
  an adapter or the HTTP cache, which keeps only HTTP 200 responses; model replies come from the response cache behind
  a transport that refuses to send, so a replay needs no key, no network and no money. A tool request the saved run
  never made, or a reply the cache does not hold, is a miss: the engine stops at once with cache_miss (exit 2) rather
  than deciding from a different graph.
- The case is the saved run's own: the manifest's case, which is the case as the run started (graph.json's case also
  holds the candidates the run inferred), checked against graph.json's variant and supplied context. A replay never
  resolves the request again, so an rsID lookup or a reference source that appeared since cannot change it.
- The saved run is checked before anything runs: a bundle file that changed after the run wrote it is refused
  (exit 1), and a run whose engine recorded that it cannot be replayed (a max_tokens retry, a refusal, a provider
  error, a currency or wall-time stop: replies the response cache never holds) is not re-executed (exit 2, with the
  engine's reasons).
- A folder that lacks something the run used is not re-executed either (exit 2, each missing item named, nothing
  written): a raw result a tool call names that is not there, one a public export reduced on purpose (its manifest
  lists it under public_export.raw_files_rewritten: a literature read kept to its verified passages, a search without
  its abstracts), or the fixture file a fixture run was made from (a public copy names it by file name only). A
  replay copies the recorded raw bytes into its own calls, so without them it could only report differences that
  say nothing about the run. A raw file that is a link, lies outside the folder, or changed with no export saying so
  is refused (exit 1).
- The replay runs with the saved run's models (cache keys hold the model, effort and max_tokens), roles, limits and
  tool allowlist from its manifest, whatever config.yaml says now.
- Fixture runs replay with their fixture's scripted roles (a reply the script lacks is a miss) and its tools as the
  saved bundle recorded them; evidence bundles replay their tool calls only (no engine and no model); a code-only
  fill replays its tool calls and then fills the table again (commands.fill_graph), with no model; a fill with the
  reader also takes each article's reading from the response cache, like an engine run's replies.
- The replay is a new run folder outside the saved run, with its own bundle, reports, budget state and trace: the
  saved run and the shared caches are only read.

Exit codes: 0 identical (apart from times, seconds, costs and cached flags); 1 different, failed, or the saved run
changed after it was written; 2 a cache miss, a run that stopped with cache_miss, a saved run that says it cannot
be replayed, or a folder that lacks what the run used (incomplete).
"""

import hashlib
import json
import time
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ..config import Config, load_config
from . import fill
from .bundle import Bundle, build_manifest, compare_graph_json, load_bundle, new_run_dir, safe_raw_path, write_bundle
from .commands import collect_evidence, fill_graph, fill_manifest, recorded_fixture, wire, write_table
from .investigate import EngineLimits
from .report import write_reports
from .schemas import Case
from .tools import ToolLimits

EXIT = {"identical": 0, "different": 1, "failed": 1, "miss": 2, "not_replayable": 2, "incomplete": 2}
REPLAY_BUDGET_USD = 1e9      # nothing is spent (the transport refuses); the reservation before a send must not refuse
FREE = {"input": 0.0, "output": 0.0}
LLM_KEYS = ("generator", "critic", "summariser")


@dataclass
class Replay9:
    saved: Path
    out: Path
    kind: str = ""                     # engine, fixture, evidence or fill
    status: str = ""                   # identical, different, failed, miss, not_replayable or incomplete
    message: str = ""
    differences: list[str] = field(default_factory=list)
    reasons: list[str] = field(default_factory=list)          # why the saved run cannot be replayed
    tool_misses: list[str] = field(default_factory=list)      # tool requests the saved bundle does not answer
    missing: list[str] = field(default_factory=list)          # what the run used that the saved folder lacks
    notes: list[str] = field(default_factory=list)
    model_calls: int = 0
    tool_calls: int = 0
    seconds: float = 0.0
    written: bool = False              # the replay's bundle is in `out`

    @property
    def code(self) -> int:
        return EXIT[self.status]

    def line(self) -> str:
        what = {"identical": "identical apart from times, costs and cached flags",
                "different": f"{len(self.differences)} difference(s)", "failed": "failed", "miss": "cache miss",
                "not_replayable": "not replayable",
                "incomplete": f"not re-executed: the folder lacks {len(self.missing)} item(s) the run used"}[self.status]
        out = f"{self.saved}{f' ({self.kind} run)' if self.kind else ''}: {what}"
        if self.status in ("identical", "different", "miss"):
            source = "the fixture's script" if self.kind == "fixture" else "the response cache"
            out += (f"; {self.model_calls} model call(s) answered by {source}, {self.tool_calls} tool call(s) by the "
                    "saved bundle")
        if self.message:
            out += f" ({self.message})"
        return out + f"; {self.seconds:.1f} s"


def replay_config(manifest: Mapping[str, Any], out: Path, base: Config | None = None) -> Config:
    """config.yaml as the saved run saw it: its models (the response cache's keys hold model, effort and max_tokens)
    and its v9 block (roles, limits, tool allowlist) from the manifest, over the current settings; the budget state in
    `out`, with a limit no reservation reaches (nothing is spent), and a zero price for any model the price list lacks
    (a replay never pays, but LLMClient prices its reservation)."""
    cfg = base or load_config()
    saved = manifest.get("config") or {}
    llm = {**cfg["llm"], **(saved.get("models") or {})}
    prices = dict(llm.get("prices_per_mtok") or {})
    for key in LLM_KEYS:
        if llm.get(key) and llm[key] not in prices:
            prices[llm[key]] = dict(FREE)
    v9 = {**(cfg.get("v9") or {}), **(saved.get("v9") or {})}
    budget = {"dev": REPLAY_BUDGET_USD, "eval": REPLAY_BUDGET_USD, "spare": 0.0, "state_file": str(out / "budget.json")}
    return Config({**cfg, "llm": {**llm, "prices_per_mtok": prices}, "v9": v9, "budget_usd": budget})


def _model(cls: Any, values: Any) -> Any:
    """A limits model from a saved manifest's dict (fields the current model lacks are left out), or None."""
    if not isinstance(values, Mapping):
        return None
    return cls(**{k: v for k, v in values.items() if k in cls.model_fields})


def saved_limits(manifest: Mapping[str, Any], cfg: Config) -> tuple[EngineLimits, ToolLimits]:
    """The engine and tool limits the saved run ran with (its manifest), else the config's."""
    parts = manifest.get("engine") or {}
    limits = _model(EngineLimits, parts.get("limits")) or EngineLimits.from_config(cfg)
    return limits, _model(ToolLimits, parts.get("tool_limits")) or limits.tool_limits()


def _identity(case: Case) -> tuple[str, str]:
    """What the saved tool answers depend on: the variant and the supplied context."""
    return case.variant.key, json.dumps([s.model_dump(mode="json") for s in case.supplied_context], sort_keys=True)


def raw_inputs(saved: Path, bundle: Bundle) -> tuple[list[str], list[str]]:
    """The saved tool calls' raw results as the folder holds them: (missing, problems). `missing`: a raw result an
    executed call names that the folder lacks, or one a public export rewrote on purpose (its manifest lists it under
    public_export.raw_files_rewritten); a replay copies these bytes into its own calls, so without them it cannot
    reproduce the run. `problems`: a path that is not raw/<name>, a link or anything but a regular file inside the
    folder, or bytes that changed after the run with no export saying so. Only raw/<name> paths inside the folder are
    read: the bundle is data."""
    export = bundle.manifest.get("public_export")
    rewritten = set(export.get("raw_files_rewritten") or []) if isinstance(export, Mapping) else set()
    folder = saved.resolve()
    missing: list[str] = []
    problems: list[str] = []
    for tid, call in bundle.graph.tool_calls.items():
        if call.charged_to == "none" or not call.raw_result_path:
            continue
        rel = safe_raw_path(call.raw_result_path)
        path = saved / rel if rel is not None else None
        if path is None:
            problems.append(f"{tid} names the raw result {call.raw_result_path!r}, which is not raw/<name> in the run "
                            "folder")
        elif path.is_symlink() or not path.resolve().is_relative_to(folder) or (path.exists() and not path.is_file()):
            problems.append(f"{rel} is not a regular file inside the saved run (a replay never follows a link)")
        elif not path.exists():
            missing.append(f"{rel}: the raw result of {tid} ({call.tool_name}), which this folder does not hold")
        elif call.raw_result_hash and hashlib.sha256(path.read_bytes()).hexdigest() != call.raw_result_hash:
            if rel in rewritten:
                missing.append(f"{rel}: the raw result of {tid} ({call.tool_name}) as the run wrote it; this public "
                               "copy holds it without its article text")
            else:
                problems.append(f"{rel} changed after the run wrote it (it no longer matches {tid}'s raw_result_hash)")
    return missing, problems


def _check_apart(saved: Path, out: Path) -> None:
    s, o = saved.resolve(), out.resolve()
    if o == s or s in o.parents or o in s.parents:
        raise ValueError(f"the replay folder {out} must lie outside the saved run {saved}")


def replay(saved: str | Path, out: str | Path, base: Config | None = None) -> Replay9:
    """Re-execute one saved v9 run offline into the new folder `out` and compare graph.json (see the module
    docstring). Never raises: a failure is a "failed" result with its message."""
    res = Replay9(Path(saved), Path(out))
    started = time.monotonic()
    try:
        _replay(res, base)
    except Exception as e:  # a re-execution needs its caches and data/; say what broke
        res.status, res.message = "failed", f"{type(e).__name__}: {str(e)[:300]}"
    res.seconds = round(time.monotonic() - started, 1)
    return res


def _replay(res: Replay9, base: Config | None) -> None:
    saved, out = res.saved, res.out
    _check_apart(saved, out)
    bundle = load_bundle(saved)
    manifest = bundle.manifest
    if bundle.integrity:
        res.status = "failed"
        res.message = "the saved run changed after it was written: " + "; ".join(bundle.integrity)
        return
    if not manifest or "case" not in manifest:
        res.status, res.message = "failed", "no manifest.json with the run's case: not a complete v9 bundle"
        return
    parts = manifest.get("engine") or {}
    res.kind = ("fixture" if manifest.get("mode") == "fixture" else
                "fill" if parts.get("driver") in fill.DRIVERS else "engine" if parts else "evidence")
    # a fill with the reader made model calls: its replay takes them from the response cache
    articles = (parts.get("reader") or {}).get("max_articles") if res.kind == "fill" else None
    if parts and parts.get("replayable") is False:
        res.status, res.message = "not_replayable", "the saved run's engine recorded that it cannot be replayed"
        res.reasons = [str(why) for why in parts.get("not_replayable") or []] or ["no reason was recorded"]
        return
    if res.kind == "fill" and parts.get("fill_format") not in (None, fill.FILL_FORMAT):
        # A fill asks a fixed list of sources. A run made before a source was added holds no answer for it, so this
        # code cannot repeat that run, and saying so beats reporting a missing response.
        res.status = "not_replayable"
        res.message = "the saved run was filled by an earlier version of the fill than this code has"
        res.reasons = [f"fill_format: the run has {parts.get('fill_format')}, this code {fill.FILL_FORMAT}"]
        return
    if articles:
        # The reader's instructions and output form are part of every request it makes. A run read under earlier
        # ones cannot be answered from the cache by this code, and saying so beats reporting a missing reply.
        from . import reader
        saved_reader = parts.get("reader") or {}
        now = reader.manifest_parts(None, articles)
        changed = [key for key in ("reader_format", "prompt_sha256", "schema_sha256")
                   if saved_reader.get(key) != now[key]]
        if changed:
            res.status = "not_replayable"
            res.message = "the saved run was read under earlier reader instructions than this code has"
            res.reasons = [f"{key}: the run has {saved_reader.get(key)}, this code {now[key]}" for key in changed]
            return
    second = parts.get("critic") if res.kind == "fill" else None
    if second:
        # The critic's instructions and output form are part of every request it makes, as the reader's are.
        from . import critic
        now = critic.manifest_parts(None, second.get("settings") or {})
        changed = [key for key in ("critic_format", "prompt_sha256", "schema_sha256") if second.get(key) != now[key]]
        if changed:
            res.status = "not_replayable"
            res.message = "the saved run's critic read under earlier instructions than this code has"
            res.reasons = [f"{key}: the run has {second.get(key)}, this code {now[key]}" for key in changed]
            return
    third = parts.get("judge") if res.kind == "fill" else None
    if third:
        # ... and so are the judge's
        from . import judge
        now = judge.manifest_parts(None, third.get("settings") or {})
        changed = [key for key in ("judge_format", "prompt_sha256", "schema_sha256") if third.get(key) != now[key]]
        if changed:
            res.status = "not_replayable"
            res.message = "the saved run's judge read under earlier instructions than this code has"
            res.reasons = [f"{key}: the run has {third.get(key)}, this code {now[key]}" for key in changed]
            return
    case = Case.model_validate(manifest["case"])
    if _identity(case) != _identity(bundle.graph.case):
        res.status, res.message = "failed", "the manifest's case is not the one graph.json records"
        return
    missing, problems = raw_inputs(saved, bundle)
    if problems:
        res.status, res.message = "failed", "; ".join(problems[:3]) + (f" (and {len(problems) - 3} more)"
                                                                        if len(problems) > 3 else "")
        return
    fixture = None
    if res.kind == "fixture":
        request = manifest.get("request") or {}
        try:
            fixture, unchanged = recorded_fixture(request)
        except FileNotFoundError:
            missing.append(f"the fixture {request.get('fixture')} the run was made from: it is neither in v9/fixtures "
                           "nor a file here")
        else:
            if fixture.case.model_dump(mode="json") != case.model_dump(mode="json"):
                res.status, res.message = "failed", "the fixture's case is no longer the saved run's"
                return
            if not unchanged:
                res.notes.append("the fixture file changed after the run")
    if missing:
        res.status, res.missing = "incomplete", missing
        res.message = "nothing was run or written"
        return
    cfg = replay_config(manifest, out, base)
    limits, tool_limits = saved_limits(manifest, cfg)
    new_run_dir(out)
    w = wire(cfg, "fixture" if fixture is not None else "cache_only", out, fixture=fixture, recorded=saved,
             limits=limits, tool_limits=tool_limits, models=res.kind not in ("evidence", "fill") or bool(articles),
             code_tools=res.kind == "fill", critic=dict(second.get("settings") or {}) or True if second else False,
             judge=dict(third.get("settings") or {}) or True if third else False)
    if res.kind == "evidence":
        graph = w.graph(case)
        collect_evidence(graph, w.runner)
        manifest_parts: Mapping[str, Any] = {}
        metrics: Mapping[str, Any] = {}
    elif res.kind == "fill":
        graph, counts = fill_graph(w, case, articles=articles)
        manifest_parts = fill_manifest(w, counts, articles)
        metrics = {"fill": counts}
    else:
        result = w.engine().run(case)
        graph, manifest_parts, metrics = result.graph, result.manifest_parts, result.metrics
    stop = graph.result.stop_reason if graph.result is not None else None
    callers = [c for c in (w.roles, w.critic, w.judge) if c is not None]
    res.model_calls = sum(c.calls_used for c in callers)
    res.tool_calls = sum(t.charged_to != "none" for t in graph.tool_calls.values())
    res.tool_misses = list(getattr(w.runner, "misses", None) or [])
    res.differences = compare_graph_json(json.loads((saved / "graph.json").read_text(encoding="utf-8")),
                                         json.loads(graph.to_json()))
    missed = next((c for c in callers if c.replay_miss), None)
    model_miss = missed is not None
    if res.tool_misses or model_miss or stop == "cache_miss":
        res.status = "miss"
        res.message = (f"{len(res.tool_misses)} tool request(s) the saved run never made" if res.tool_misses
                       else missed.failures[-1]["message"][:200] if missed is not None and missed.failures
                       else "the run stopped with cache_miss")
    else:
        res.status = "different" if res.differences else "identical"
    replayed = build_manifest(request=manifest.get("request") or {}, case=case, mode=w.mode, config=cfg,
                              manifest_parts=manifest_parts, graph=graph, profile=manifest.get("profile"))
    write_bundle(graph, metrics, {**replayed, "replay_of": {"run_folder": str(saved), "status": res.status,
                                                            "differences": len(res.differences)}}, out)
    res.written = True
    try:
        write_reports(out)
        if res.kind == "fill":
            write_table(out, graph)
    except Exception as e:  # the comparison stands without a report
        res.notes.append(f"report not written ({type(e).__name__}: {e})")
