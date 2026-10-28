"""One run of the workflow: fixed stages in code, models only inside stages (spec 2, section 1)."""

import logging
import time
from pathlib import Path

from ..config import REPO, Config, load_config
from ..context.base import Case
from ..context.http import Http
from .case import CaseSpec, RunState
from .ledger import Ledger
from .llm import LLMClient
from .report import build_report, write_report
from .stages.citations import citation_check, rank
from .stages.critique import critique
from .stages.gather import gather
from .stages.generate import generate, single
from .stages.investigate import refine
from .stages.screen import screen
from .stages.tournament import tournament
from .stages.verdict import verdict

log = logging.getLogger(__name__)
CONFIGS = ("single", "no_qbic", "full")


def run_dir_for(cfg: Config, spec: CaseSpec, config: str, masked: bool, seed: int, root: str | None = None) -> Path:
    root = root or (cfg.get("runs") or {}).get("dev_dir", "runs/dev")
    return REPO / root / config / ("masked" if masked else "named") / str(seed) / spec.case_id


def run_case(spec: CaseSpec, config: str = "full", masked: bool = False, seed: int = 0, cfg: Config | None = None,
             transport=None, http: Http | None = None, qbic=None, run_dir: Path | None = None, refresh: bool = False,
             phase: str = "dev", fresh: bool = True) -> dict:
    if config not in CONFIGS:
        raise ValueError(f"config must be one of {CONFIGS}")
    cfg = cfg or load_config()
    run_dir = Path(run_dir or run_dir_for(cfg, spec, config, masked, seed))
    if fresh and run_dir.exists():     # keep an earlier run: move it aside rather than delete it
        run_dir.rename(run_dir.with_name(f"{run_dir.name}.prev-{time.strftime('%Y%m%dT%H%M%S')}"))
    run_dir.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    t = cfg["tools"]
    http = http or Http(cfg.path("tools", "http_cache"), refresh=refresh, tries=int(t.get("http_tries", 6)))
    llm = LLMClient(cfg, transport=transport, phase=phase, trace_path=run_dir / "trace.jsonl", seed=seed)
    tool_case = Case(spec.variant, spec.disease, spec.origin, spec.rsid, spec.expression_context, http,
                     retry_rounds=int(t.get("tool_retry_rounds", 2)), retry_wait=float(t.get("tool_retry_wait", 60)))
    if config == "full" and qbic is None:
        from ..qbic.tools import QbicTools
        qbic = QbicTools(cfg)
    state = RunState(spec, config, masked, run_dir, Ledger(run_dir), llm, tool_case, qbic if config == "full" else None)
    try:
        if config == "single":
            single(state)
            state.grades1 = []          # no evidence: every link is missing
        else:
            gather(state)
            if config == "full":
                screen(state)
            generate(state)
            critique(state)
            inv = cfg["investigate"]
            refine(state, int(inv["max_rounds"]), int(inv["max_tool_calls"]))
            if (cfg.get("tournament") or {}).get("enabled"):
                tournament(state)
        for e in state.ledger.evidence():       # a degraded run must be visible: one flag per failed tool call
            if not e.ok:
                state.flag("tool_failed", f"{e.id} {e.tool}: {e.summary.splitlines()[0][:160]}")
        cit = citation_check(state)
        ranked = rank(state, cit["statuses"])
        state.verdict = verdict(state, ranked, cit["statuses"])
        state.ledger.add_chains("rank", 2, ranked, {h.id: i for i, h in enumerate(ranked, 1)})
        report = build_report(state, ranked, cit, time.time() - t0)
        write_report(state, report)
        return report
    finally:
        state.ledger.close()
