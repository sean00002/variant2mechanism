"""The local backend: the same `qbic-selex predict` chunks as the cluster job, run as parallel processes here.

Each process needs about 1.2 GB with statistics (one 8,192 x 8,192 covariance at a time); unpacking a covariance
takes about 0.6 s on an M1 Max, so 997 models take about 11 minutes in one process. The genome index must be the
cluster's (same .fai md5), so local rows share the cluster's settings hash and the two backends share one cache.
"""

import hashlib
import logging
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from ..config import REPO, Config
from .backend import Backend, BackendError, JobFailed, chunk_models, make_run_id, variants_tsv
from .variants import Variant

log = logging.getLogger(__name__)


def _expand(p: str) -> Path:
    path = Path(os.path.expanduser(str(p)))
    return path if path.is_absolute() else REPO / path


def qbic_selex_executable(setting: str | None) -> str:
    """The configured path, or the qbic-selex installed next to this Python."""
    if setting and setting != "qbic-selex":
        return str(_expand(setting))
    here = Path(sys.executable).parent / "qbic-selex"
    return str(here) if here.exists() else (shutil.which("qbic-selex") or "qbic-selex")


def md5_file(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


class LocalBackend(Backend):
    name = "local"

    def __init__(self, cfg: Config | None = None, sleep=time.sleep, clock=time.time, runner=subprocess.run):
        super().__init__(cfg, sleep, clock)
        self.l = self.cfg["local"]
        self.runner = runner
        self.exe = qbic_selex_executable(self.l.get("qbic_selex"))
        self.model_dir = _expand(self.l["model_dir"])
        self.cov_dir = _expand(self.l["cov_dir"])
        self.genome = _expand(self.l["genome"])
        self.jobs_dir = _expand(self.l.get("jobs_dir", "state/qbic_jobs"))

    def check_ready(self, stats: bool) -> None:
        problems = []
        if not self.model_dir.is_dir():
            problems.append(f"model weights not found at {self.model_dir}")
        if stats and not self.cov_dir.is_dir():
            problems.append(f"covariances not found at {self.cov_dir} (qbic-selex download primary-covs)")
        fai = Path(str(self.genome) + ".fai")
        if not self.genome.exists() or not fai.exists():
            problems.append(f"genome and its .fai not found at {self.genome}")
        else:
            want = self.cfg["cluster"]["genome_fai_md5"]
            got = md5_file(fai)
            if got != want:
                problems.append(f"local genome index md5 {got} differs from the cluster's {want}; results would not "
                                "share the cache. Use the same hg38.fa as the cluster.")
        if problems:
            raise BackendError("Local QBiC-SELEX is not ready: " + "; ".join(problems))

    def _task(self, job_dir: Path, i: int, stats: bool, device: str) -> tuple[int, int, str]:
        nn = f"{i:02d}"
        argv = [self.exe, "predict", "-v", "variants.tsv", "-m", f"models_{nn}.txt", "--model-dir",
                str(self.model_dir), "-g", str(self.genome), "-o", f"results_{nn}.csv"]
        if stats:
            argv[6:6] = ["-c", str(self.cov_dir), "--compute-stats", "--device", device]
        start = time.time()
        with open(job_dir / f"task_{nn}.log", "w") as logf:
            r = self.runner(argv, cwd=job_dir, stdout=logf, stderr=subprocess.STDOUT)
        secs = round(time.time() - start)
        if r.returncode == 0 and (job_dir / f"results_{nn}.csv").exists():
            (job_dir / f"done_{nn}").write_text(f"{secs}\n")
        return i, r.returncode, nn

    def submit(self, variants: list[Variant], stats: bool = True, **overrides) -> dict:
        """Write the inputs and run every chunk now, `local.workers` at a time."""
        self.check_ready(stats)
        keys = [v.key() for v in variants]
        run_id = make_run_id(keys)
        job_dir = self.jobs_dir / run_id
        job_dir.mkdir(parents=True, exist_ok=True)
        workers = int(overrides.get("workers", self.l.get("workers", 6)))
        chunks = chunk_models(self.cache.models, int(overrides.get("model_chunks", workers)))
        (job_dir / "variants.tsv").write_text(variants_tsv(variants))
        for i, ms in enumerate(chunks):
            (job_dir / f"models_{i:02d}.txt").write_text("\n".join(ms) + "\n")
        device = overrides.get("device", self.l.get("device", "cpu"))
        run = {"run_id": run_id, "backend": "local", "job_dir": str(job_dir), "slurm_job": None, "keys": keys,
               "stats": stats, "n_chunks": len(chunks), "partition": "local", "gres": None,
               "device": device if stats else None, "submitted": self.clock(),
               "created_utc": datetime.now(UTC).isoformat(timespec="seconds"), "workers": workers}
        self._save(run)
        log.info("local run %s: %d chunks, %d at a time, statistics %s", run_id, len(chunks), workers, stats)
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for _i, code, nn in pool.map(lambda i: self._task(job_dir, i, stats, device), range(len(chunks))):
                log.info("chunk %s finished (exit %d)", nn, code)
        return run

    def wait(self, run: dict, timeout_hours: float | None = None) -> str:
        return "COMPLETED"          # submit runs to completion

    def collect(self, run: dict) -> pd.DataFrame:
        job_dir = Path(run["job_dir"])
        task_seconds, failed = {}, []
        for i in range(run["n_chunks"]):
            nn = f"{i:02d}"
            done = job_dir / f"done_{nn}"
            if done.exists():
                task_seconds[nn] = int(done.read_text().strip() or 0)
            else:
                failed.append(nn)
        if failed:
            tails = []
            for nn in failed[:4]:
                logf = job_dir / f"task_{nn}.log"
                tail = "\n".join(logf.read_text(errors="replace").splitlines()[-50:]) if logf.exists() else ""
                tails.append(f"--- task {nn} ---\n{tail}")
            raise JobFailed(f"Run {run['run_id']}: chunks {', '.join(failed)} failed.\n" + "\n".join(tails))
        run["task_seconds"] = task_seconds
        run["gpu_name"] = None
        return pd.concat([pd.read_csv(job_dir / f"results_{i:02d}.csv", dtype={"variant_key": str, "model": str})
                          for i in range(run["n_chunks"])], ignore_index=True)
