"""Offline replay of saved v8 runs (`v2m replay`).

A replay re-executes a saved run from the caches: HTTP offline, every model call answered from cache/llm or refused,
QBiC-SELEX statistics from cache/qbic.sqlite with no job allowed. The new report.json is then compared with the saved
one, apart from `seconds` and `cost_usd`, which differ by design. Nothing is written outside the output folder: the
budget state and the QBiC-SELEX call log go there too, and the saved folder is never touched.

`--render-only` re-renders a saved report.json as report.md and report.html without re-running anything; it needs
only the repository, so it works from a fresh checkout. A re-execution also needs data/ and the caches.

Exit codes: 0 identical, 1 different (or the replay failed), 2 a cache miss: the replay would need a paid model call
or a QBiC-SELEX run.
"""

import json
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

from ..agent.llm import LLMError
from ..config import REPO, Config, load_config
from ..context.http import Http

IGNORED = ("seconds", "cost_usd")
# The guard (tests/test_replay.py, `v2m replay --guard`): every code-only baseline of the main arm, plus three agent
# runs that were checked by hand to replay exactly: a supported lead, a member ambiguity and a near-miss control.
GUARD_AGENT = (("full_given", 0, "rs339331"), ("full_given", 0, "tert_c228t"), ("full_given", 0, "rs73706717"))
EXIT = {"identical": 0, "different": 1, "failed": 1, "miss": 2}


class ReplayMiss(LLMError):
    """A model call that is not in the cache: replaying past it would cost money."""


def refuse(body: dict) -> dict:
    raise ReplayMiss(f"{body.get('model')}: this replay would need a paid model call")


class ReplayHttp(Http):
    """The HTTP cache with the network off; records each request the cache could not answer."""

    def __init__(self, cache_dir: str | Path):
        super().__init__(cache_dir, offline=True)
        self.misses: list[str] = []

    def request(self, method, url, json_body=None, timeout=60, headers=None):
        r = super().request(method, url, json_body=json_body, timeout=timeout, headers=headers)
        if not r.ok and not r.cached:
            self.misses.append(f"{method} {url}")
        return r


@dataclass
class Replay:
    saved: Path
    out: Path
    status: str = ""                         # identical, different, failed or miss
    message: str = ""
    differences: list[str] = field(default_factory=list)
    added: list[str] = field(default_factory=list)      # fields the saved report does not have (newer code)
    http_misses: list[str] = field(default_factory=list)
    model_calls: int = 0
    seconds: float = 0.0

    @property
    def code(self) -> int:
        return EXIT[self.status]

    def line(self) -> str:
        what = {"identical": "identical apart from seconds and cost",
                "different": f"{len(self.differences)} difference(s)", "failed": "failed", "miss": "cache miss"}
        out = f"{label(self.saved)}: {what[self.status]}"
        if self.status in ("identical", "different"):
            out += f"; {self.model_calls} model calls from the cache, {len(self.http_misses)} uncached requests"
        if self.message:
            out += f" ({self.message})"
        return out + f"; {self.seconds:.1f} s"


def label(saved: Path) -> str:
    """case, arm and repeat of a saved run folder: <runs>/<arm>/<repeat>/<case> or <runs>/code/<arm>/0/<case>;
    the folder itself when it is laid out otherwise (demo/v8/<case>)."""
    from ..v8.evaluation import ARMS
    p = Path(saved)
    if p.parent.parent.name not in ARMS or not p.parent.name.isdigit():
        return str(p)
    who = " code only" if p.parent.parent.parent.name == "code" else ""
    return f"{p.name} ({p.parent.parent.name}{who}, repeat {p.parent.name})"


def saved_runs_dir() -> Path:
    """The saved v8 grid; config.yaml's own v8.runs_dir, never a profile's, so replays keep their paths."""
    return REPO / load_config()["v8"]["runs_dir"]


def find_run(case_id: str, arm: str = "full_given", repeat: int = 0, code_only: bool = False,
             runs_dir: Path | None = None) -> Path:
    root = Path(runs_dir or saved_runs_dir())
    d = (root / "code" / arm / "0" / case_id) if code_only else (root / arm / str(repeat) / case_id)
    if not (d / "report.json").exists():
        raise FileNotFoundError(f"no saved run at {d}")
    return d


def guard_runs(runs_dir: Path | None = None) -> list[Path]:
    root = Path(runs_dir or saved_runs_dir())
    code = sorted(p.parent for p in (root / "code" / "full_given" / "0").glob("*/report.json"))
    return code + [find_run(c, a, r, runs_dir=root) for a, r, c in GUARD_AGENT]


def replay_cfg(report: dict, out: Path, base: Config | None = None) -> Config:
    """config.yaml as the run saw it: the saved models in the three roles (the cache key holds the model, effort and
    max_tokens), the budget state and QBiC-SELEX call log inside `out`, and no QBiC-SELEX job on a miss."""
    cfg = base or load_config()
    budget = {"dev": 1e9, "eval": 1e9, "spare": 0.0, "state_file": str(out / "budget.json")}
    cache = {**cfg["cache"], "log": str(out / "qbic_calls.jsonl"), "allow_miss_jobs": False}
    return Config({**cfg, "llm": {**cfg["llm"], **(report.get("models") or {})}, "budget_usd": budget,
                   "cache": cache})


def differences(saved, new, path: str = "", out: list | None = None, added: list | None = None) -> list[str]:
    """Paths where `new` differs from `saved`; fields only `new` has go to `added`."""
    out = [] if out is None else out
    added = [] if added is None else added
    if isinstance(saved, dict) and isinstance(new, dict):
        for k, v in saved.items():
            if not path and k in IGNORED:
                continue
            if k not in new:
                out.append(f"{path}/{k}: missing now")
            else:
                differences(v, new[k], f"{path}/{k}", out, added)
        added += [f"{path}/{k}" for k in new if k not in saved and not (not path and k in IGNORED)]
    elif isinstance(saved, list) and isinstance(new, list):
        if len(saved) != len(new):
            out.append(f"{path}: {len(saved)} items saved, {len(new)} now")
        for i, (a, b) in enumerate(zip(saved, new, strict=False)):
            differences(a, b, f"{path}[{i}]", out, added)
    elif saved != new:
        out.append(f"{path}: {json.dumps(saved, default=str)[:80]} -> {json.dumps(new, default=str)[:80]}")
    return out


def _check_out(saved: Path, out: Path) -> None:
    s, o = saved.resolve(), out.resolve()
    if o == s or s in o.parents or o in s.parents:
        raise ValueError(f"the output folder {out} must lie outside the saved run {saved}")


def replay(saved: Path, out: Path, base: Config | None = None) -> Replay:
    """Re-execute one saved v8 run offline into `out` and compare the reports."""
    from ..agent.case import load_gold_case
    from ..agent.stages.screen import RunStopped
    from ..v8.evaluation import ARMS
    from ..v8.run import run_case8
    saved, out = Path(saved), Path(out)
    _check_out(saved, out)
    old = json.loads((saved / "report.json").read_text())
    if old.get("version") != "v8":
        raise ValueError(f"{saved}: only v8 runs can be replayed so far, not {old.get('version')}")
    arm_key = saved.parent.parent.name
    cfg = replay_cfg(old, out, base)
    http = ReplayHttp(cfg.path("tools", "http_cache"))
    res = Replay(saved, out)
    t0 = time.time()
    try:
        run_case8(load_gold_case(old["case_id"], cfg), arm=old["arm"], masked=old["mode"] == "masked",
                  seed=old["seed"] or 0, cfg=cfg, transport=refuse, http=http, run_dir=out, phase="eval",
                  infer=old["infer_context"], code_only=old["code_only"], drop=set(old["dropped_tfs"]),
                  before=old["literature_before"], single_prompts=ARMS.get(arm_key, {}).get("prompts", "memory"))
    except ReplayMiss as e:
        res.status, res.message = "miss", str(e)
    except RunStopped as e:
        res.status, res.message = ("miss" if "QBiC-SELEX scores unavailable" in str(e) else "failed"), str(e)[:200]
    except Exception as e:             # a re-execution needs data/ and the caches; say what broke, keep going
        res.status, res.message = "failed", f"{type(e).__name__}: {str(e)[:200]}"
    res.seconds, res.http_misses = round(time.time() - t0, 1), http.misses
    if res.status:
        return res
    new = json.loads((out / "report.json").read_text())
    res.model_calls = new.get("model_calls", 0)
    res.differences = differences(old, new, added=res.added)
    res.status = "different" if res.differences else "identical"
    return res


def render(saved: Path, out: Path) -> list[Path]:
    """report.md and report.html from a saved report.json, with nothing re-run (`--render-only`)."""
    from ..v8.report import render_html, render_markdown
    saved, out = Path(saved), Path(out)
    _check_out(saved, out)
    rep = json.loads((saved / "report.json").read_text())
    out.mkdir(parents=True, exist_ok=True)
    paths = [out / "report.md"]
    paths[0].write_text(render_markdown(rep))
    if rep["arm"] != "single":
        paths.append(out / "report.html")
        paths[1].write_text(render_html(rep))
    return paths


def default_out(saved: Path) -> Path:
    """runs/replay/<the saved run's path below runs/>, or below runs/replay/other/ when it is elsewhere."""
    saved = Path(saved).resolve()
    runs = (REPO / "runs").resolve()
    rel = saved.relative_to(runs) if runs in saved.parents else Path("other") / saved.name
    return REPO / "runs" / "replay" / rel


def guard(runs_dir: Path | None = None, out: Path | None = None) -> list[Replay]:
    """Replay the guard set, each run into its own folder under `out` (a temporary folder by default)."""
    runs = guard_runs(runs_dir)
    if out is not None:
        return [replay(s, Path(out) / f"{i:02d}_{s.name}") for i, s in enumerate(runs)]
    with tempfile.TemporaryDirectory(prefix="v2m-replay-") as tmp:
        return [replay(s, Path(tmp) / f"{i:02d}_{s.name}") for i, s in enumerate(runs)]
