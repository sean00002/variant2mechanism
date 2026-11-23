"""The v9 run folder: create it, write and load the bundle, fingerprint the run, compare replays and make a public
export (SPEC 8, 13.4, 13.11, 13.16).

Everything a run leaves behind goes through this module, so the rules that make a run reviewable hold in one place:

    run-folder/
      manifest.json     the clean request, case, mode, engine version, code fingerprint (git HEAD, dirty flag, a hash
                        of `git diff HEAD`, sha256 of every v9 source and prompt), a scrubbed config subset, the
                        engine's parts (prompt hashes, role models, limits, stop reason), dataset releases, cache
                        policy, created time and the sha256 of every bundle file
      graph.json        the full ClaimGraph (lossless)
      evidence.jsonl    one Evidence.model_dump_json() per line   } exactly what RecordedToolRunner reads, so a run
      tool_calls.jsonl  one ToolCall.model_dump_json() per line   } replays at the adapter level (SPEC 13.4)
      events.jsonl      one DecisionEvent per line
      metrics.json      normalised: counts derived from the graph, plus the engine's model usage
      raw/              T#.json results, written once by the ToolRunner during the run
      report.html, report.md        written by report.py
      evaluation.json   evaluator-only (evaluation.py); never read by the engine

Why each rule:
- A run folder is new or refused, and every file is created exclusively: a run never mixes its files with another's
  and nothing a reviewer has seen is silently replaced (SPEC 13.16).
- The manifest holds no secrets and no environment variables: request, config and engine entries whose names mention
  API or access keys, tokens, secrets, passwords, credentials, auth headers, cookies or environment variables are
  dropped (a bare "key", an LLM client key name such as "generator", is kept), and nothing is read from the
  environment.
- The code fingerprint covers what `git diff HEAD` cannot see: every v9 source by hash, and every untracked file under
  src/ (a module that was never committed changes behaviour as much as an edited one).
- The manifest records the sha256 of every bundle file; load_bundle checks them (Bundle.integrity), a report says when
  a file changed after the run, and a public export refuses such a folder, so what is published is what the run wrote.
- Replay compares graph.json while ignoring what differs by design between two executions of the same run (times,
  seconds, latency, costs and cached flags); a changed assessment, link or disposition is a difference.
- A public export applies the literature route's excerpt policy (literature.public_graph_state, public_raw) to the
  whole folder: verified passages only, each bounded, every other free-text field bounded too, and no article text,
  because author manuscripts carry no licence (SPEC 13.11). It copies only regular raw files inside the run folder
  whose bytes match their call's raw_result_hash: a link, or a file replaced after the run, could put anything into
  a public folder. Its manifest names every item whose text the policy cut, whichever field it was, and names a
  replayed run or a fixture file by its last path part, never by a local path.
- Candidate retention (SPEC 13.5) is measured with one rule, sketched_groups (it lives in graph.py, so the engine's
  metrics use it without importing this module; it is re-exported here with hypothesis_versions, never redefined):
  an inventory group counts as sketched when any version of any hypothesis named it, through a claim, a claim that
  claim superseded, or a member alternative. A group dropped by a local repair was considered; only a group no
  hypothesis ever named is inventory_only.
- The inventory is read as the adapters wrote it: a group whose gate-passing models disagree about the allele has one
  Evidence item per allele (data.discordant), and its row joins the item for the allele the row names (binds_more),
  the adapters' own rule (inventory_rows); both items belong to the inventory.
- Counts that the graph already defines are taken from the graph: full-text reads and articles read are grouped by
  ClaimGraph.fulltext_articles, the rule the full-text budget uses, never by a second copy of it.
"""

import hashlib
import json
import math
import os
import re
import subprocess
from collections import Counter
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from ..config import REPO
from . import ENGINE_VERSION
from .graph import ClaimGraph, GraphState, sketched_groups
from .graph import hypothesis_versions as hypothesis_versions  # re-exported with sketched_groups (graph's objects)
from .schemas import Case, RunMode, ToolCall

BUNDLE_FORMAT = 1
METRICS_FORMAT = 1
# Written in this order; the manifest last, so a folder with a manifest holds a complete bundle.
BUNDLE_FILES = ("graph.json", "evidence.jsonl", "events.jsonl", "tool_calls.jsonl", "metrics.json", "manifest.json")
V9_DIR = Path(__file__).resolve().parent
SOURCE_SUFFIXES = frozenset({".py", ".txt", ".yaml", ".yml", ".json", ".html"})
# A config, request or engine key is dropped from the manifest when any of its words is one of these, or when it is a
# compound naming a key ("api_key", "access_key"); a bare "key" (an LLM client key such as "generator") is kept.
SECRET_WORDS = frozenset({"apikey", "token", "secret", "password", "passwd", "credential", "credentials", "auth",
                          "authorization", "bearer", "cookie", "env", "environ"})
# Fields that differ by design between a run and its replay. Any key ending in _time, _seconds or _usd, or starting
# with latency, is volatile too.
VOLATILE_KEYS = frozenset({"retrieval_time", "cached", "cost_usd", "seconds", "wall_seconds", "latency", "latency_s",
                           "created", "timestamp"})
CACHE_POLICY: dict[str, dict[str, str]] = {
    "live": {"http": "read-through cache; the network is used on a miss",
             "model_calls": "response cache, then the provider, within the profile's budget"},
    "cache_only": {"http": "offline: saved responses only; a miss is recorded as cache_miss",
                   "model_calls": "saved responses only; a miss is refused, never paid"},
    "fixture": {"http": "not used: synthetic fixture tools answer every request",
                "model_calls": "scripted role outputs; no provider is called"},
}
QBIC_POLICY = "cache/qbic.sqlite, read only; a variant that is not cached needs a separate precompute (no job is run)"
REPLAY_POLICY = "adapter level: tool_calls.jsonl, evidence.jsonl and raw/ answer the same requests (SPEC 13.4)"
RAW_PATH = re.compile(r"raw/[A-Za-z0-9][A-Za-z0-9_.-]*")
# Model usage fields as metrics.json names them, with the other names an engine may report them under.
USAGE_FIELDS = {"calls": ("calls",), "cost_usd": ("cost_usd",), "input_tokens": ("input_tokens", "prompt_tokens"),
                "output_tokens": ("output_tokens", "completion_tokens"), "thinking_tokens": ("thinking_tokens",),
                "latency_s": ("latency_s",), "cache_hits": ("cache_hits",), "failures": ("failures",)}
ROLE_USAGE_KEYS = ("model_usage_by_role", "by_role", "per_role")


@dataclass(frozen=True)
class Bundle:
    """A loaded run folder. The graph is rebuilt from graph.json, which is lossless; rendering needs nothing else.
    `integrity` lists the bundle files that no longer match the sha256 the manifest recorded (verify_files); empty
    when every file is as the run wrote it, or when the manifest records none."""
    path: Path
    manifest: dict[str, Any]
    graph: ClaimGraph
    metrics: dict[str, Any]
    evaluation: dict[str, Any] | None
    integrity: tuple[str, ...] = ()


# --- small helpers ---------------------------------------------------------------------------------------------------

def _now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_text(text: str) -> str:
    return _sha256_bytes(text.encode("utf-8"))


def _plain(value: Any) -> Any:
    """A JSON-native copy: models dumped, tuples and sets as lists, non-finite floats as None (json.dumps would write
    NaN, which is not JSON), numpy values as Python ones, anything else as its text. Bundle files must load back."""
    if isinstance(value, BaseModel):
        return _plain(value.model_dump(mode="json"))
    if isinstance(value, Mapping):
        return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, list | tuple):
        return [_plain(v) for v in value]
    if isinstance(value, set | frozenset):
        return sorted((_plain(v) for v in value), key=lambda v: json.dumps(v, sort_keys=True))
    if value is None or isinstance(value, bool | int | str):
        return value
    if isinstance(value, float):
        return value if math.isfinite(value) else None
    if callable(getattr(value, "tolist", None)):
        return _plain(value.tolist())
    return str(value)


def _secret_key(key: str) -> bool:
    """Whether a key names a credential or an environment variable ("api_key_env", "apiKey", "token", ...)."""
    words = [w for w in re.split(r"[^a-z0-9]+", re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", key).lower()) if w]
    return any(w in SECRET_WORDS for w in words) or ("key" in words and len(words) > 1)


def _scrub(value: Any) -> Any:
    """Drop every mapping entry whose key names a credential or an environment variable, at any depth."""
    if isinstance(value, dict):
        return {k: _scrub(v) for k, v in value.items() if not _secret_key(k)}
    if isinstance(value, list):
        return [_scrub(v) for v in value]
    return value


def _number(value: Any) -> int | float | None:
    if isinstance(value, bool) or not isinstance(value, int | float):
        return None
    return value if math.isfinite(value) else None


def _counts(values: Iterable[str]) -> dict[str, int]:
    return dict(sorted(Counter(values).items()))


def _source_key(source_id: str) -> str:
    """One source for counting: "PMID:1" and "pmid:1" are the same, and so are "doi:x" and "https://doi.org/x"."""
    text = " ".join(source_id.split()).casefold()
    for prefix in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "doi:", "pmid:", "pmcid:"):
        if text.startswith(prefix):
            return text[len(prefix):]
    return text


def _jsonl(items: Iterable[BaseModel]) -> str:
    return "".join(item.model_dump_json() + "\n" for item in items)


def write_new(path: Path, text: str) -> None:
    """Create a file that must not exist (mode "x"): a bundle file is never overwritten."""
    with open(path, "x", encoding="utf-8") as f:
        f.write(text)


def safe_raw_path(path: str | None) -> str | None:
    """A raw result path as the runner writes it (raw/<name>), or None: a path from a saved bundle is data, and one
    that left the run folder ("../x", "/etc/x") must never be read, copied or linked."""
    return path if path and RAW_PATH.fullmatch(path) and ".." not in path else None


# --- run folders -----------------------------------------------------------------------------------------------------

def new_run_dir(path: str | Path) -> Path:
    """Create a new run folder. An existing path is refused, never reused, renamed or overwritten (SPEC 13.16); the
    ToolRunner writes raw/ into the folder during the run."""
    folder = Path(path)
    try:
        folder.mkdir(parents=True, exist_ok=False)
    except FileExistsError:
        raise FileExistsError(f"{folder} already exists: a run folder is never reused or overwritten; choose a new "
                              "path") from None
    return folder


# --- the manifest ----------------------------------------------------------------------------------------------------

def _git(repo: Path, *args: str) -> bytes | None:
    """Output of a read-only git command, or None when git or the repository is unavailable. --no-optional-locks
    keeps `git status` from rewriting the index, so fingerprinting never writes inside the repository."""
    try:
        done = subprocess.run(["git", "--no-optional-locks", *args], cwd=repo, capture_output=True, timeout=60,
                              check=True)
    except (OSError, subprocess.SubprocessError):
        return None
    return done.stdout


def _untracked_sources(repo: Path) -> dict[str, str] | None:
    """sha256 of every untracked, non-ignored file under src/ (repo-relative path -> digest), or None when git is
    unavailable. `git diff HEAD` leaves untracked files out, so without this a module that was never committed (a
    model transport, the v9 package itself) could change behaviour while the fingerprint stayed the same."""
    listing = _git(repo, "ls-files", "--others", "--exclude-standard", "-z", "--", "src")
    if listing is None:
        return None
    out: dict[str, str] = {}
    for name in sorted(os.fsdecode(n) for n in listing.split(b"\0") if n):
        path = repo / name
        if path.is_file():
            out[name] = _sha256_bytes(path.read_bytes())
    return out


def code_fingerprint(repo: Path = REPO) -> dict[str, Any]:
    """What code made the run: git HEAD, whether the tree differs from it, a hash of `git diff HEAD`, the sha256 of
    every untracked file under src/ (which the diff does not cover), and the sha256 of every v9 source, fixture,
    template and prompt (kept by name even once the package is committed)."""
    files = sorted(p for p in V9_DIR.rglob("*")
                   if p.is_file() and p.suffix in SOURCE_SUFFIXES and "__pycache__" not in p.parts)
    sources = {p.relative_to(V9_DIR).as_posix(): _sha256_bytes(p.read_bytes()) for p in files}
    head = _git(repo, "rev-parse", "HEAD")
    status = _git(repo, "status", "--porcelain")
    diff = _git(repo, "diff", "HEAD", "--no-color", "--no-ext-diff", "--binary")
    untracked = _untracked_sources(repo)
    return {"git": {"head": head.decode().strip() if head is not None else None,
                    "dirty": bool(status.strip()) if status is not None else None,
                    "diff_sha256": _sha256_bytes(diff) if diff is not None else None,
                    "untracked_sha256": (_sha256_text(json.dumps(untracked, sort_keys=True))
                                         if untracked is not None else None),
                    "untracked": untracked},
            "v9_sources_sha256": _sha256_text(json.dumps(sources, sort_keys=True)),
            "v9_sources": sources,
            "prompts": {name: digest for name, digest in sources.items() if name.startswith("prompts/")}}


def config_subset(config: Mapping[str, Any]) -> dict[str, Any]:
    """The settings that shape a run (models, the v9 block with its limits, tool allowlist and policies, the budget
    caps) plus a hash of the whole merged config. Credential and environment-variable entries are dropped."""
    llm = config.get("llm") or {}
    budget = config.get("budget_usd") or {}
    return {"models": _scrub(_plain({k: llm[k] for k in ("api", "generator", "critic", "summariser", "effort",
                                                             "max_tokens") if k in llm})),
            "v9": _scrub(_plain(config.get("v9") or {})),
            "budget_usd": {k: _number(budget[k]) for k in ("dev", "eval", "spare") if k in budget},
            "config_sha256": _sha256_text(json.dumps(_plain(config), sort_keys=True))}


def dataset_releases(graph: ClaimGraph) -> list[dict[str, str | None]]:
    """The tool, provider, release and adapter version of every executed call, once each, in name order."""
    seen = sorted({(t.tool_name, t.provider, t.dataset_release, t.tool_version)
                   for t in graph.tool_calls.values() if t.charged_to != "none"})
    return [{"tool": tool, "provider": provider, "dataset_release": release, "tool_version": version}
            for tool, provider, release, version in seen]


def graph_summary(graph: ClaimGraph) -> dict[str, Any]:
    result = graph.result
    return {"version": graph.version, "entities": len(graph.entities), "claims": len(graph.claims),
            "evidence": len(graph.evidence), "hypotheses": len(graph.hypotheses), "tool_calls": len(graph.tool_calls),
            "events": len(graph.events), "outcome": result.outcome if result else None,
            "stop_reason": result.stop_reason if result else None}


def build_manifest(*, request: Mapping[str, Any], case: Case, mode: RunMode, config: Mapping[str, Any],
                   manifest_parts: Mapping[str, Any], graph: ClaimGraph, profile: str | None,
                   created: str | None = None) -> dict[str, Any]:
    """manifest.json for a run (write_bundle adds the sha256 of each bundle file). `manifest_parts` are the engine's
    (prompt sha256s, role-to-model map, limits, stop reason); `created` defaults to now (UTC)."""
    return {"format": BUNDLE_FORMAT,
            "engine_version": ENGINE_VERSION,
            "created": created or _now(),
            "mode": mode,
            "profile": profile,
            "request": _scrub(_plain(request)),
            "case": case.model_dump(mode="json"),
            "code": code_fingerprint(),
            "config": config_subset(config),
            "engine": _scrub(_plain(manifest_parts)),
            "dataset_releases": dataset_releases(graph),
            "cache_policy": {"mode": mode, **CACHE_POLICY[mode], "qbic": QBIC_POLICY, "replay": REPLAY_POLICY},
            "graph": graph_summary(graph)}


# --- metrics ---------------------------------------------------------------------------------------------------------

def inventory_call(graph: ClaimGraph) -> ToolCall | None:
    """The latest successful qbic_inventory call (contract C2), or None."""
    calls = [t for t in graph.tool_calls.values()
             if t.tool_name == "qbic_inventory" and t.execution_status == "success"]
    return max(calls, key=lambda t: int(t.tool_call_id[1:])) if calls else None


def inventory_items(graph: ClaimGraph) -> dict[str, list[str]]:
    """The Evidence items of the latest successful qbic_inventory call by group id (data.group_id, as text), in the
    call's order: one item per gate-passing group, or one per allele for a group whose gate-passing models disagree
    about which allele binds more (data.discordant). Empty without an inventory."""
    call = inventory_call(graph)
    items: dict[str, list[str]] = {}
    for e in call.evidence_ids if call else []:
        if e in graph.evidence:
            items.setdefault(str(graph.evidence[e].data.get("group_id")), []).append(e)
    return items


def inventory_table(graph: ClaimGraph) -> list[dict[str, Any]]:
    """The QBiC-SELEX inventory as recorded (contract C2): the latest successful qbic_inventory call's observation
    rows, each with the E id of its group's Evidence (None for groups that do not pass the gate), in the adapter's
    neutral order (DBD label, then group id); nothing re-orders them. A row describes its group's best model, so a
    discordant group's row joins the item for the allele the row names (binds_more), else its first item. The same
    rows as adapters.inventory_rows (tests pin it, on real adapter output too), read here from the graph alone:
    importing the adapters loads pysam, pandas and every provider, which rendering a saved run must not need."""
    call = inventory_call(graph)
    if call is None:
        return []
    items = inventory_items(graph)
    v = graph.case.variant

    def joined(row: Mapping[str, Any]) -> str | None:
        group = items.get(str(row.get("group_id"))) or []
        more = row.get("binds_more")
        allele = v.alt if more == "alt" else v.ref if more == "ref" else None
        return next((e for e in group if graph.evidence[e].allele == allele), group[0] if group else None)

    return [{**row, "evidence_id": joined(row)} for row in call.observations]


def inventory_summary(graph: ClaimGraph) -> dict[str, Any]:
    """Candidate retention is measured here (SPEC 13.5): `inventory_only` lists the gate-passing groups that no
    version of any hypothesis sketched (sketched_groups), `sketched` the others, both in the inventory's neutral order
    (DBD label, then group id). They are not hypotheses and have no disposition. metrics.json holds this dict as
    "inventory"; the evaluator reads it there."""
    rows = inventory_table(graph)
    passing = [str(r.get("group_id")) for r in rows if r.get("passes_gate") is True]
    sketched = sketched_groups(graph, rows)
    return {"groups": len(rows), "gate_passing": len(passing), "below_gate": len(rows) - len(passing),
            "sketched": [g for g in passing if g in sketched],
            "inventory_only": [g for g in passing if g not in sketched]}


def _usage(record: Mapping[str, Any]) -> dict[str, int | float]:
    """Model usage fields under their metrics.json names (prompt_tokens is read as input_tokens, and so on)."""
    out: dict[str, int | float] = {}
    for name, aliases in USAGE_FIELDS.items():
        value = next((v for a in aliases if (v := _number(record.get(a))) is not None), None)
        if value is not None:
            out[name] = value
    return out


def _model_metrics(engine: Mapping[str, Any], graph: ClaimGraph) -> dict[str, Any]:
    """Model usage from the engine's metrics: totals (`model_calls`, `cost_usd`, tokens, latency) and per-role usage
    (`model_usage_by_role`, or `by_role` / `per_role`). A missing total is the sum over roles; calls and cost fall
    back to the graph's model_usage, which the engine keeps current."""
    by_role = next((engine[k] for k in ROLE_USAGE_KEYS if isinstance(engine.get(k), Mapping)), {})
    roles = {str(role): _usage(usage) for role, usage in sorted(by_role.items()) if isinstance(usage, Mapping)}
    totals = _usage({**engine, "calls": engine.get("model_calls")})

    def total(field: str) -> int | float | None:
        if field in totals:
            return totals[field]
        values = [r[field] for r in roles.values() if field in r]
        return sum(values) if values else None

    calls, cost = total("calls"), total("cost_usd")
    return {"calls": calls if calls is not None else graph.model_usage.calls,
            "cost_usd": round(cost if cost is not None else graph.model_usage.cost_usd, 6),
            **{field: total(field) for field in USAGE_FIELDS if field not in ("calls", "cost_usd")},
            "by_role": roles}


def _articles_read(graph: ClaimGraph) -> int:
    """The articles any successful read returned, abstracts included, grouped by the graph's own rule
    (ClaimGraph.fulltext_articles, which the full-text budget counts with) applied to a view of the graph's reads in
    which each one counts as read: an abstract read by PMID and a full text read by PMCID of the same article are one
    article. The view is built from the graph's state and the graph itself is never changed."""
    reads = {tid: t.model_copy(update={"fulltext_article": t.fulltext_article or t.read_article})
             for tid, t in graph.tool_calls.items() if t.read_article}
    view = ClaimGraph.from_state(GraphState(case=graph.case, counters=dict(graph.counters), tool_calls=reads))
    return len(view.fulltext_articles())


def _tool_metrics(graph: ClaimGraph) -> dict[str, Any]:
    """Tool counts from the recorded calls. Full-text reads are the graph's own budget count (one article read by
    PMCID and later by PMID is one read); articles_read counts every article a read returned, abstracts included,
    by the same rule (_articles_read)."""
    calls = list(graph.tool_calls.values())
    executed = [t for t in calls if t.charged_to != "none"]
    by_tool: dict[str, Counter] = {}
    for t in calls:
        by_tool.setdefault(t.tool_name, Counter())["executed" if t.charged_to != "none" else "refused"] += 1
    return {"requests": len(calls), "executed": len(executed), "refused": len(calls) - len(executed),
            "charged_to_agent": sum(t.charged_to == "agent" for t in calls),
            "charged_to_code": sum(t.charged_to == "code" for t in calls),
            "by_execution_status": _counts(t.execution_status for t in executed),
            "by_retrieval_status": _counts(t.retrieval_status for t in executed),
            "by_tool": {name: dict(sorted(c.items())) for name, c in sorted(by_tool.items())},
            "cached": sum(t.cached for t in executed),
            "fulltext_reads": len(graph.fulltext_articles()),
            "articles_read": _articles_read(graph)}


def _evidence_metrics(graph: ClaimGraph) -> dict[str, Any]:
    items = list(graph.evidence.values())
    linked = {x.evidence_id for c in graph.claims.values() for x in c.evidence_links}
    return {"items": len(items), "linked_to_claims": len(linked),
            "by_class": _counts(e.evidence_class for e in items),
            "by_origin": _counts(e.origin for e in items),
            "unique_sources": len({_source_key(s) for e in items for s in e.source_ids if s.strip()}),
            "independence_groups": len({e.independence_group for e in items})}


def _graph_metrics(graph: ClaimGraph) -> dict[str, Any]:
    return {"version": graph.version, "entities": len(graph.entities), "claims": len(graph.claims),
            "superseded_claims": sum(c.superseded_by is not None for c in graph.claims.values()),
            "claims_by_assessment": _counts(c.assessment for c in graph.claims.values()),
            "hypotheses_by_disposition": _counts(h.disposition for h in graph.hypotheses.values()),
            "questions_by_status": _counts(q.status for q in graph.questions.values()),
            "comparisons": len(graph.comparisons), "events": len(graph.events),
            "refused_updates": sum(e.action == "refuse_update" for e in graph.events)}


def normalise_metrics(metrics: Mapping[str, Any] | None, graph: ClaimGraph) -> dict[str, Any]:
    """metrics.json: one schema whatever the engine reports. Tool, evidence, graph and inventory counts are computed
    from the graph (the record of what happened); model usage and wall time come from the engine's metrics, which are
    also kept whole under "engine". Normalising normalised metrics gives the same result."""
    raw = _plain(dict(metrics or {}))
    engine = (raw.get("engine") or {}) if raw.get("metrics_format") == METRICS_FORMAT else raw
    return {"metrics_format": METRICS_FORMAT,
            "model": _model_metrics(engine, graph),
            "tools": _tool_metrics(graph),
            "evidence": _evidence_metrics(graph),
            "graph": _graph_metrics(graph),
            "inventory": inventory_summary(graph),
            "wall_seconds": _number(engine.get("wall_seconds", engine.get("seconds"))),
            "engine": engine}


# --- writing and loading ---------------------------------------------------------------------------------------------

def write_bundle(graph: ClaimGraph, metrics: Mapping[str, Any] | None, manifest: Mapping[str, Any],
                 run_dir: str | Path) -> Path:
    """Write the bundle files into run_dir (created when missing; raw/ is left as the runner wrote it). Refused, with
    nothing written, when any bundle file already exists; each file is created exclusively, so none is ever
    overwritten. The manifest is written last and lists the sha256 of the other files."""
    folder = Path(run_dir)
    folder.mkdir(parents=True, exist_ok=True)
    existing = [name for name in BUNDLE_FILES if (folder / name).exists()]
    if existing:
        raise FileExistsError(f"{folder} already holds {', '.join(existing)}: bundle files are never overwritten")
    contents = {"graph.json": graph.to_json(),
                "evidence.jsonl": _jsonl(graph.evidence.values()),
                "events.jsonl": _jsonl(graph.events),
                "tool_calls.jsonl": _jsonl(graph.tool_calls.values()),
                "metrics.json": json.dumps(normalise_metrics(metrics, graph), indent=1) + "\n"}
    files = {name: _sha256_text(text) for name, text in contents.items()}
    contents["manifest.json"] = json.dumps({**_plain(manifest), "files": files}, indent=1) + "\n"
    for name in BUNDLE_FILES:
        write_new(folder / name, contents[name])
    return folder


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def verify_files(run_dir: str | Path, manifest: Mapping[str, Any]) -> list[str]:
    """The bundle files that are missing or whose bytes no longer match the sha256 the manifest recorded when the
    bundle was written, one line each; empty when every recorded file matches (or the manifest records none). Only the
    bundle's own file names are read: the manifest is data, and a name it lists is never followed elsewhere."""
    folder = Path(run_dir)
    recorded = manifest.get("files")
    problems = []
    for name, digest in sorted(recorded.items() if isinstance(recorded, Mapping) else []):
        if name not in BUNDLE_FILES:
            continue
        path = folder / name
        if not path.is_file():
            problems.append(f"{name} is missing")
        elif _sha256_bytes(path.read_bytes()) != digest:
            problems.append(f"{name} has changed since the run was written")
    return problems


def load_bundle(run_dir: str | Path) -> Bundle:
    """Load a run folder. graph.json is required; a missing manifest or metrics file loads as {} (a report can still be
    rendered and says so) and evaluation.json as None. `integrity` lists the bundle files that changed after the run
    wrote them (verify_files)."""
    folder = Path(run_dir)
    graph_file = folder / "graph.json"
    if not graph_file.is_file():
        raise FileNotFoundError(f"{folder} has no graph.json: it is not a v9 run folder")
    optional = {name: _read_json(folder / name) if (folder / name).is_file() else None
                for name in ("manifest.json", "metrics.json", "evaluation.json")}
    manifest = optional["manifest.json"] or {}
    return Bundle(path=folder, manifest=manifest,
                  graph=ClaimGraph.from_json(graph_file.read_text(encoding="utf-8")),
                  metrics=optional["metrics.json"] or {}, evaluation=optional["evaluation.json"],
                  integrity=tuple(verify_files(folder, manifest)))


# --- replay comparison -----------------------------------------------------------------------------------------------

def _volatile(key: str) -> bool:
    return key in VOLATILE_KEYS or key.endswith(("_time", "_seconds", "_usd")) or key.startswith("latency")


def _show(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, default=str)
    return text if len(text) <= 80 else text[:77] + "..."


def _same_scalar(a: Any, b: Any) -> bool:
    """Equality that keeps true apart from 1 (Python's True == 1 would hide a changed flag)."""
    if isinstance(a, bool) or isinstance(b, bool):
        return type(a) is type(b) and a == b
    return a == b


def _differences(a: Any, b: Any, path: str, out: list[str]) -> None:
    if isinstance(a, dict) and isinstance(b, dict):
        for key in [*a, *(k for k in b if k not in a)]:
            if _volatile(key):
                continue
            where = f"{path}/{key}"
            if key not in b:
                out.append(f"{where}: only in the first")
            elif key not in a:
                out.append(f"{where}: only in the second")
            else:
                _differences(a[key], b[key], where, out)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            out.append(f"{path or '/'}: {len(a)} items, then {len(b)}")
        for i, (x, y) in enumerate(zip(a, b, strict=False)):
            _differences(x, y, f"{path}[{i}]", out)
    elif type(a) is not type(b) and not (_number(a) is not None and _number(b) is not None):
        out.append(f"{path or '/'}: {_show(a)} -> {_show(b)}")
    elif not _same_scalar(a, b):
        out.append(f"{path or '/'}: {_show(a)} -> {_show(b)}")


def compare_graph_json(a: dict[str, Any], b: dict[str, Any]) -> list[str]:
    """Where two parsed graph.json documents differ, as "/path: first -> second" lines; empty means the same run.
    Volatile fields (retrieval times, seconds, latency, costs, cached flags, created times) are ignored wherever they
    appear; every scientific field (claims, links, assessments, dispositions, events, evidence) is compared."""
    out: list[str] = []
    _differences(a, b, "", out)
    return out


# --- public export (SPEC 13.11) --------------------------------------------------------------------------------------

def _check_apart(source: Path, out: Path) -> None:
    s, o = source.resolve(), out.resolve()
    if o == s or s in o.parents or o in s.parents:
        raise ValueError(f"the export folder {out} must lie outside the run folder {source}")


def _changed(before: Mapping[str, Any], after: Mapping[str, Any]) -> list[str]:
    return [key for key, value in before.items() if after.get(key) != value]


def _file_name(value: str) -> str:
    """The last part of a recorded local path ("/Users/me/x/fixture.json" -> "fixture.json"); a plain name as it is."""
    return re.split(r"[\\/]", value.rstrip("\\/"))[-1] or value


def _agent_text_cut(before: Mapping[str, Any], after: Mapping[str, Any]) -> list[str]:
    """The claims, hypotheses, questions and comparisons (by id), and "result", whose text the excerpt policy cut
    (assertions, rationales, answers and summaries an agent wrote can quote a paper at length)."""
    cut = [key for part in ("claims", "hypotheses", "questions", "comparisons")
           for key in _changed(before.get(part) or {}, after.get(part) or {})]
    return cut + (["result"] if before.get("result") != after.get("result") else [])


def _recorded_raw(run: Path, call: Mapping[str, Any]) -> bytes | None:
    """A call's raw result as the run wrote it, or None when the call names none or the file is missing. Refused
    (ValueError) when the path is a link, resolves outside the run folder or is not a regular file, or when its bytes no
    longer match the call's raw_result_hash: a public export copies what the run recorded, never what a link points to
    or what was put in the folder later."""
    rel = safe_raw_path(call.get("raw_result_path"))
    if rel is None:
        return None
    path = run / rel
    if not path.exists() and not path.is_symlink():
        return None
    resolved = path.resolve()
    if path.is_symlink() or not resolved.is_relative_to(run.resolve()) or not resolved.is_file():
        raise ValueError(f"{rel} is not a regular file inside the run folder: a public export never follows a link")
    data = resolved.read_bytes()
    expected = call.get("raw_result_hash")
    if expected and _sha256_bytes(data) != expected:
        raise ValueError(f"{rel} no longer matches the raw_result_hash {call.get('tool_call_id')} recorded: the file "
                         "changed after the run, so it is not exported")
    return data


def export_public(run_dir: str | Path, out_dir: str | Path) -> Path:
    """A public demo copy of a run in a new folder (SPEC 13.11). The excerpt policy is the literature route's
    (literature.public_graph_state and public_raw): verified passages kept, each bounded; every other free-text field
    of evidence, claims, hypotheses, questions, comparisons and the result cut to the same bound; a read's passages
    and a search's abstracts dropped from tool calls; a read's raw article reduced to its verified passages;
    unverified passages emptied from event details. Every other raw result referenced by a tool call is copied byte
    for byte; evaluation.json (evaluator-only) and unreferenced files are left out; report.html and report.md are
    rendered from the exported data. The manifest's public_export records what the policy changed: evidence_text_cut
    (evidence whose verified passage or any other text field was cut), agent_text_cut (claims, hypotheses, questions,
    comparisons and "result" whose text was cut), tool_calls_text_removed, events_scrubbed, raw_files_rewritten (raw
    files whose bytes no longer match their call's raw_result_hash, by design) and raw_files_missing (raw files the
    run folder lacks). Local paths the manifest records are reduced to their last part: a replay's replay_of.run_folder
    and the file of a fixture run started from a file (request.fixture). Refused (ValueError, nothing written) when a
    bundle file changed after the run wrote it, or when a raw file is a link, leaves the run folder or no longer
    matches its hash. The reports are rendered once in memory before anything is written, so an export never stops
    half-written. out_dir must not exist and must lie outside the run folder."""
    from . import literature  # the excerpt policy belongs to the literature route
    from .report import render_html, render_markdown, write_reports  # report.py imports this module

    source = load_bundle(run_dir)
    out = Path(out_dir)
    _check_apart(source.path, out)
    if source.integrity:
        raise ValueError(f"{source.path} changed after its bundle was written ({'; '.join(source.integrity)}): a "
                         "public export publishes only what the run recorded")
    state = json.loads(source.graph.to_json())
    public = literature.public_graph_state(state)
    graph = ClaimGraph.from_state(GraphState.model_validate(public))
    raws: dict[str, bytes] = {}
    rewritten: list[str] = []
    missing: list[str] = []
    for tid, call in public["tool_calls"].items():
        original = _recorded_raw(source.path, state["tool_calls"][tid])
        path = safe_raw_path(call.get("raw_result_path"))
        if path is None:
            continue
        if original is None:
            missing.append(path)
            continue
        raws[path] = literature.public_raw(call, original, state["evidence"].values())
        if raws[path] != original:
            rewritten.append(path)
    events = {e["event_id"]: e for e in state["events"]}
    shown = dict(source.manifest)
    if isinstance(replay_of := shown.get("replay_of"), Mapping) and replay_of.get("run_folder"):
        # a replay names the run it re-executed by its local path; a public copy names it by folder, as source_run
        shown["replay_of"] = {**replay_of, "run_folder": Path(str(replay_of["run_folder"])).name}
    if isinstance(request := shown.get("request"), Mapping) and isinstance(request.get("fixture"), str):
        # a fixture run started from a file names it by its local path; a public copy names the file only (a fixture
        # named from v9/fixtures is a plain name already); its sha256 still identifies it
        shown["request"] = {**request, "fixture": _file_name(request["fixture"])}
    manifest = {**shown, "public_export": {
        "source_run": source.path.name, "created": _now(), "passage_limit": literature.PUBLIC_PASSAGE_LIMIT,
        "evaluation_left_out": source.evaluation is not None, "files_verified": bool(source.manifest.get("files")),
        "evidence_text_cut": _changed(state["evidence"], public["evidence"]),
        "agent_text_cut": _agent_text_cut(state, public),
        "tool_calls_text_removed": _changed(state["tool_calls"], public["tool_calls"]),
        "events_scrubbed": _changed(events, {e["event_id"]: e for e in public["events"]}),
        "raw_files_rewritten": rewritten, "raw_files_missing": missing}}
    metrics = normalise_metrics(source.metrics, graph)
    preview = Bundle(path=out, manifest=manifest, graph=graph, metrics=metrics, evaluation=None)
    render_html(preview)                # a report that cannot be rendered stops the export before anything is written
    render_markdown(preview)
    new_run_dir(out)
    write_bundle(graph, metrics, manifest, out)
    for path, data in raws.items():
        (out / path).parent.mkdir(parents=True, exist_ok=True)
        with open(out / path, "xb") as f:
            f.write(data)
    write_reports(out)
    return out
