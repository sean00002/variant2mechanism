"""Check the cluster connection, paths and scheduler (spec 1, A0 step 3). Read-only; submits nothing."""

import subprocess
import sys

from variant2mechanism.config import load_config


def ssh(host: str, command: str, timeout: int = 400) -> subprocess.CompletedProcess:
    return subprocess.run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=300", host, command],
                          capture_output=True, text=True, timeout=timeout)


def main() -> int:
    cfg = load_config()
    c = cfg["cluster"]
    master = subprocess.run(["ssh", "-O", "check", c["host"]], capture_output=True, text=True)
    print("master connection:", (master.stderr or master.stdout).strip() or "ok")
    checks = " ; ".join([
        'hostname', 'echo "job=$SLURM_JOB_ID"', 'command -v sbatch squeue sacct', 'sinfo -s',
        f'{c["qbic_selex"]} --version',
        *[f'test -e {p} && echo "ok {p}" || echo "MISSING {p}"'
          for p in (c["data_dir"], c["model_dir"], c["cov_dir"], c["genome"], c["genome"] + ".fai")],
        f'test -d {c["jobs_dir"]} && echo "ok {c["jobs_dir"]}" || echo "not yet created: {c["jobs_dir"]}"',
    ])
    r = ssh(c["host"], checks)
    print(r.stdout.strip())
    if r.returncode != 0:
        print(r.stderr.strip(), file=sys.stderr)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
