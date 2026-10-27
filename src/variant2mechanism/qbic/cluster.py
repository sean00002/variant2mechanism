"""Run QBiC-SELEX on the cluster: SSH, upload, sbatch array, poll, fetch, validate, import (spec 1, 5.3).

Every ssh call uses BatchMode=yes. Uploads and downloads go through `ssh host 'cat ...'`, which works
through the proxy and a master connection. Job files are written only under cluster.jobs_dir.
"""

import gzip
import io
import logging
import re
import subprocess
import time
from datetime import UTC, datetime

import pandas as pd

from ..config import Config
from .backend import Backend, BackendError, Busy, JobFailed, chunk_models, make_run_id, variants_tsv
from .variants import Variant

log = logging.getLogger(__name__)

FIX = "Open the SSH connection first: run ssh -fN {host} in a terminal and complete the login."

# names kept from before the backend split
ClusterError = BackendError
ClusterJobFailed = JobFailed
ClusterBusy = Busy
__all__ = ["Cluster", "ClusterError", "ClusterJobFailed", "ClusterBusy", "ClusterUnavailable", "ClusterTimeout",
           "chunk_models", "make_run_id", "FIX"]


class ClusterUnavailable(BackendError):
    pass


class ClusterTimeout(BackendError):
    def __init__(self, run_id: str, message: str):
        super().__init__(message)
        self.run_id = run_id


SBATCH = """#!/bin/bash
#SBATCH -J qbic-{run_id}
#SBATCH -p {partition}
{gres_line}#SBATCH -c {cpus_per_task}
#SBATCH --mem={mem}
#SBATCH -t {time}
#SBATCH --array=0-{last_chunk}
#SBATCH -o {dir}/slurm-%A_%2a.out
set -euo pipefail
cd {dir}
i=$(printf '%02d' "$SLURM_ARRAY_TASK_ID")
start=$(date +%s)
{qbic_selex} predict -v variants.tsv -m models_$i.txt --model-dir {model_dir} \\
  {stats_args} -g {genome} -o results_$i.csv
gzip -f results_$i.csv
echo $(( $(date +%s) - start )) > done_$i
"""


class Cluster(Backend):
    """The slurm backend: upload over SSH, sbatch an array, poll, fetch."""
    name = "slurm"

    def __init__(self, cfg: Config | None = None, ssh: str = "ssh", sleep=time.sleep, clock=time.time):
        super().__init__(cfg, sleep, clock)
        self.c, self.s = self.cfg["cluster"], self.cfg["slurm"]
        self.host = self.c["host"]
        self.ssh_bin = ssh

    # -- ssh -----------------------------------------------------------------------------------------------

    def _ssh(self, command: str, stdin: bytes | None = None, check: bool = True,
             timeout: float = 600) -> subprocess.CompletedProcess:
        argv = [self.ssh_bin, "-o", "BatchMode=yes", "-o", "ConnectTimeout=300", self.host, command]
        r = subprocess.run(argv, input=stdin, capture_output=True, timeout=timeout)
        if check and r.returncode != 0:
            raise ClusterError(f"ssh command failed ({r.returncode}): {command[:120]}\n"
                               f"{r.stderr.decode(errors='replace')[-800:]}")
        return r

    def check_connection(self) -> None:
        master = subprocess.run([self.ssh_bin, "-O", "check", self.host], capture_output=True, timeout=30)
        if master.returncode == 0:
            return
        r = subprocess.run([self.ssh_bin, "-o", "BatchMode=yes", "-o", "ConnectTimeout=20", self.host, "true"],
                           capture_output=True, timeout=400)
        if r.returncode != 0:
            raise ClusterUnavailable(FIX.format(host=self.host))

    def upload(self, remote_dir: str, name: str, data: bytes) -> None:
        self._ssh(f"mkdir -p {remote_dir} && cat > {remote_dir}/{name}", stdin=data)

    def fetch(self, remote_path: str) -> bytes:
        return self._ssh(f"cat {remote_path}").stdout

    # -- run -----------------------------------------------------------------------------------------------

    def job_script(self, run_id: str, remote_dir: str, n_chunks: int, stats: bool, overrides: dict) -> str:
        s = {**self.s, **overrides}
        gres = s.get("gres") or ""
        stats_args = f"-c {self.c['cov_dir']} --compute-stats --device {s['device']}" if stats else ""
        return SBATCH.format(run_id=run_id, partition=s["partition"],
                             gres_line=f"#SBATCH --gres={gres}\n" if gres else "",
                             cpus_per_task=s["cpus_per_task"], mem=s["mem"], time=s["time"],
                             last_chunk=n_chunks - 1, dir=remote_dir, qbic_selex=self.c["qbic_selex"],
                             model_dir=self.c["model_dir"], stats_args=stats_args, genome=self.c["genome"])

    def submit(self, variants: list[Variant], stats: bool = True, **overrides) -> dict:
        """Upload inputs and submit the array. Returns the run record (also saved locally)."""
        self.check_connection()
        keys = [v.key() for v in variants]
        run_id = make_run_id(keys)
        remote = f"{self.c['jobs_dir']}/{run_id}"
        n_chunks = int(overrides.get("model_chunks", self.s["model_chunks"]))
        chunks = chunk_models(self.cache.models, n_chunks)
        self.upload(remote, "variants.tsv", variants_tsv(variants).encode())
        for i, ms in enumerate(chunks):
            self.upload(remote, f"models_{i:02d}.txt", ("\n".join(ms) + "\n").encode())
        self.upload(remote, "job.sbatch", self.job_script(run_id, remote, len(chunks), stats, overrides).encode())
        out = self._ssh(f"cd {remote} && env -u SLURM_JOB_ID sbatch --parsable job.sbatch").stdout.decode().strip()
        job = out.splitlines()[-1].split(";")[0].strip()
        if not job.isdigit():
            raise ClusterError(f"sbatch did not return a job id: {out!r}")
        s = {**self.s, **overrides}
        run = {"run_id": run_id, "remote_dir": remote, "slurm_job": job, "keys": keys, "stats": stats,
               "n_chunks": len(chunks), "partition": s["partition"], "gres": s.get("gres") or None,
               "device": s["device"] if stats else None, "submitted": self.clock(),
               "created_utc": datetime.now(UTC).isoformat(timespec="seconds")}
        self._save(run)
        log.info("submitted %s as Slurm job %s (%d tasks)", run_id, job, len(chunks))
        return run

    def wait(self, run: dict, timeout_hours: float | None = None) -> str:
        """Poll until the job leaves the queue. Returns the final sacct state (or 'UNKNOWN')."""
        timeout = float(timeout_hours if timeout_hours is not None else self.s["timeout_hours"]) * 3600
        start, last, job = self.clock(), None, run["slurm_job"]
        while True:
            r = self._ssh(f"squeue -h -j {job} -o '%i %T %R'", check=False)
            # stderr carries the proxy's "[compsci-session] using compute node" line; only stdout lists jobs
            lines = [ln.split() for ln in r.stdout.decode(errors="replace").splitlines()
                     if ln.startswith(job) and len(ln.split()) > 1]
            if not lines or "Invalid job id" in r.stderr.decode(errors="replace"):
                break
            states = sorted({ln[1] for ln in lines})
            if states != last:
                log.info("job %s: %s", job, ", ".join(states))
                last = states
            if self.clock() - start > timeout:
                raise ClusterTimeout(run["run_id"], f"Run {run['run_id']} (job {job}) still {'/'.join(states)} after "
                                     f"{timeout / 3600:g} h; it was left running. Import it later with "
                                     f"`v2m qbic import {run['run_id']}`.")
            self.sleep(float(self.s["poll_seconds"]))
        acct = self._ssh(f"sacct -n -P -j {job} -o JobID,State,ExitCode,Elapsed,NodeList", check=False)
        rows = [ln.split("|") for ln in acct.stdout.decode().splitlines() if ln.strip()]
        run["sacct"] = rows
        return rows[0][1] if rows else "UNKNOWN"

    def collect(self, run: dict) -> pd.DataFrame:
        """Check every task finished, fetch and concatenate results; raise ClusterJobFailed with log tails."""
        remote, job = run["remote_dir"], run["slurm_job"]
        listing = self._ssh(f"cd {remote} && ls -1", check=False).stdout.decode().split()
        task_seconds, failed = {}, []
        for i in range(run["n_chunks"]):
            nn = f"{i:02d}"
            if f"done_{nn}" in listing and f"results_{nn}.csv.gz" in listing:
                task_seconds[nn] = int(self.fetch(f"{remote}/done_{nn}").decode().strip() or 0)
            else:
                failed.append(nn)
        if failed:
            tails = []
            for nn in failed[:4]:
                t = self._ssh(f"tail -n 50 {remote}/slurm-{job}_{nn}.out", check=False).stdout.decode(errors="replace")
                tails.append(f"--- task {nn} ---\n{t}")
            rep = self._ssh(f"cat {remote}/qbic_error_report_*.log", check=False).stdout.decode(errors="replace")
            raise JobFailed(f"Run {run['run_id']}: tasks {', '.join(failed)} did not finish.\n"
                                   + "\n".join(tails) + (f"\n--- error report ---\n{rep[-3000:]}" if rep else ""))
        frames = []
        for i in range(run["n_chunks"]):
            raw = gzip.decompress(self.fetch(f"{remote}/results_{i:02d}.csv.gz"))
            frames.append(pd.read_csv(io.BytesIO(raw), dtype={"variant_key": str, "model": str}))
        out = self._ssh(f"cat {remote}/slurm-{job}_00.out", check=False).stdout.decode(errors="replace")
        m = re.search(r"Statistics on GPU: (.+)", out)
        run["gpu_name"] = m.group(1).strip() if m else None
        run["task_seconds"] = task_seconds
        return pd.concat(frames, ignore_index=True)
