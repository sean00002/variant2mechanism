"""The evaluation runner (spec 2, section 10.2): resumable, concurrent in one process, stops at the eval budget.

Runs go to runs/eval/<config>/<named|masked>/<seed>/<case_id>/. A run whose report.json exists is skipped. Cases
come from the gold set, controls included; only PROMPT_COLUMNS reach the run (agent.case.load_gold_case).
"""

import json
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from ..agent.case import load_gold_case
from ..agent.llm import BudgetExceeded, LLMError
from ..agent.run import run_case
from ..agent.stages.screen import RunStopped
from ..config import REPO, Config, load_config
from .gold import is_control, load_gold

log = logging.getLogger(__name__)
PILOT_CASES = ["tert_c228t", "rs6983267", "rs4784227", "rs1421085"]


def pilot_cases(gold) -> list[str]:
    """The four named pilot cases plus the first control (rs642961 if there is none yet)."""
    controls = [r["case_id"] for r in gold.to_dict("records") if is_control(r)]
    return PILOT_CASES + [controls[0] if controls else "rs642961"]


def run_dir(cfg: Config, config: str, mode: str, seed: int, case_id: str) -> Path:
    return REPO / cfg["eval"]["runs_dir"] / config / mode / str(seed) / case_id


def run_grid(cases: list[str], configs: list[str], masked: bool = False, seed: int = 0, cfg: Config | None = None,
             transport=None, concurrency: int | None = None, phase: str = "eval") -> list[dict]:
    """Run every (case, config) not yet done. Returns one status row per job."""
    cfg = cfg or load_config()
    mode = "masked" if masked else "named"
    jobs, status = [], []
    for config in configs:
        for case_id in cases:
            d = run_dir(cfg, config, mode, seed, case_id)
            if (d / "report.json").exists():
                status.append({"case_id": case_id, "config": config, "status": "skipped (done)"})
            else:
                jobs.append((case_id, config, d))
    stop = False

    def one(case_id, config, d):
        if stop:
            return {"case_id": case_id, "config": config, "status": "not run (budget)"}
        try:
            r = run_case(load_gold_case(case_id, cfg), config, masked=masked, seed=seed, cfg=cfg, transport=transport,
                         run_dir=d, phase=phase)
            return {"case_id": case_id, "config": config, "status": "ok", "cost_usd": r["cost_usd"],
                    "seconds": r["seconds"]}
        except BudgetExceeded as e:
            return {"case_id": case_id, "config": config, "status": "budget", "error": str(e)}
        except (RunStopped, LLMError) as e:
            d.mkdir(parents=True, exist_ok=True)
            (d / "error.json").write_text(json.dumps({"error": str(e)}))
            return {"case_id": case_id, "config": config, "status": "failed", "error": str(e)[:300]}

    with ThreadPoolExecutor(max_workers=concurrency or int(cfg["eval"]["concurrency"])) as pool:
        futs = [pool.submit(one, *j) for j in jobs]
        for f in as_completed(futs):
            row = f.result()
            status.append(row)
            if row["status"] == "budget":
                stop = True
                log.warning("eval budget reached; remaining runs are not started")
    return status


def pilot(cfg: Config | None = None, transport=None) -> list[dict]:
    cfg = cfg or load_config()
    return run_grid(pilot_cases(load_gold(cfg)), ["full"], cfg=cfg, transport=transport)
