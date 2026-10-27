"""What every QBiC-SELEX backend shares: the cache check, one run at a time, the weight check and the import.

A backend fills the cache for the variants it is given. `slurm` runs an array job on the cluster over SSH
(cluster.py); `local` runs the same `qbic-selex predict` chunks as parallel processes on this machine (local.py).
Both write the same rows under the same settings hash, so either one's results satisfy the other.
"""

import fcntl
import hashlib
import json
import logging
import random
import time
from contextlib import contextmanager

import numpy as np
import pandas as pd
from qbic_selex.kmers import sliding_window

from ..config import Config, load_config
from .cache import QbicCache, utc_stamp
from .refsite import _model, model_path
from .variants import Variant

log = logging.getLogger(__name__)


class BackendError(RuntimeError):
    pass


class JobFailed(BackendError):
    pass


class Busy(BackendError):
    pass


def make_run_id(keys: list[str], now: str | None = None) -> str:
    digest = hashlib.sha256("\n".join(sorted(keys)).encode()).hexdigest()[:6]
    return f"{now or utc_stamp()}-{digest}"


def chunk_models(models: list[str], n: int) -> list[list[str]]:
    n = max(1, min(n, len(models)))
    return [models[i::n] for i in range(n)]


def variants_tsv(variants: list[Variant]) -> str:
    return "variant_key\tchrom\tpos\tref\talt\n" + "".join(
        f"{v.key()}\t{v.chrom}\t{v.pos}\t{v.ref}\t{v.alt}\n" for v in variants)


class Backend:
    name = "base"

    def __init__(self, cfg: Config | None = None, sleep=time.sleep, clock=time.time):
        self.cfg = cfg or load_config()
        self.sleep, self.clock = sleep, clock
        self.cache = QbicCache(self.cfg)
        self.state_dir = self.cfg.path("cache", "db").parent / "qbic_runs"

    # each backend provides these
    def submit(self, variants: list[Variant], stats: bool = True, **overrides) -> dict:
        raise NotImplementedError

    def wait(self, run: dict, timeout_hours: float | None = None) -> str:
        raise NotImplementedError

    def collect(self, run: dict) -> pd.DataFrame:
        raise NotImplementedError

    # shared ----------------------------------------------------------------------------------------------

    @contextmanager
    def _lock(self):
        path = self.cfg.path("cache", "db").parent / ".lock"
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise Busy(f"another QBiC-SELEX run holds {path}; wait for it to finish") from None
            try:
                yield
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)

    def _save(self, run: dict) -> None:
        self.state_dir.mkdir(parents=True, exist_ok=True)
        (self.state_dir / f"{run['run_id']}.json").write_text(json.dumps(run, indent=1))

    def load_run(self, run_id: str) -> dict:
        path = self.state_dir / f"{run_id}.json"
        if not path.exists():
            raise BackendError(f"no local record of run {run_id} in {self.state_dir}")
        return json.loads(path.read_text())

    def verify_effects(self, results: pd.DataFrame, n: int = 3, seed: int | None = None) -> list[dict]:
        """Recompute predicted_effect for n random ok pairs from the local weights; require agreement to 1e-4."""
        ok = results[results.qbic_status == "ok"]
        rng = random.Random(seed)
        checked = []
        for i in rng.sample(range(len(ok)), min(n, len(ok))):
            row = ok.iloc[i]
            model, _ = _model(str(model_path(row.model, self.cfg.path("data", "weights_dir"))))
            vals, k = model.complete, model.kmer_size
            local = (sum(np.float32(vals[x]) for x in sliding_window(row.alt_sequence.upper(), k))
                     - sum(np.float32(vals[x]) for x in sliding_window(row.ref_sequence.upper(), k)))
            diff = abs(float(local) - float(row.predicted_effect))
            checked.append({"variant_key": row.variant_key, "model": row.model, "cluster": float(row.predicted_effect),
                            "local": float(local), "diff": diff})
            if diff > 1e-4:
                raise JobFailed(f"local recompute of {row.model} at {row.variant_key} differs by {diff:.2e}; "
                                "the backend may not have run the intended models")
        return checked

    def finish(self, run: dict) -> dict:
        results = self.collect(run)
        run["effect_checks"] = self.verify_effects(results)
        run["rows_imported"] = self.cache.import_results(run, results, set(run["keys"]), run["stats"])
        run["wall_seconds"] = round(self.clock() - run["submitted"], 1)
        self._save(run)
        self.cache.log_call(run["keys"], hit=False, run_id=run["run_id"], slurm_job=run.get("slurm_job"),
                            wall_seconds=run["wall_seconds"])
        return run

    def run(self, variants: list[Variant], stats: bool = True, **overrides) -> str | None:
        """Compute and import the variants not yet cached. Returns the run id (None if all were cached)."""
        keys = [v.key() for v in variants]
        cached = self.cache.cached(keys, stats)
        todo = [v for v in variants if v.key() not in cached]
        if not todo:
            self.cache.log_call(keys, hit=True)
            return None
        with self._lock():
            run = self.submit(todo, stats, **overrides)
            self.wait(run)
            self.finish(run)
        return run["run_id"]

    def import_run(self, run_id: str) -> dict:
        """Wait for and import a run that timed out earlier (`v2m qbic import <run_id>`)."""
        run = self.load_run(run_id)
        with self._lock():
            self.wait(run)
            return self.finish(run)


def get_backend(cfg: Config | None = None, name: str | None = None) -> Backend:
    cfg = cfg or load_config()
    name = name or (cfg.get("qbic") or {}).get("backend", "slurm")
    if name == "slurm":
        from .cluster import Cluster
        return Cluster(cfg)
    if name == "local":
        from .local import LocalBackend
        return LocalBackend(cfg)
    raise BackendError(f"unknown QBiC-SELEX backend '{name}' (use slurm or local)")
