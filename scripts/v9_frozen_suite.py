"""Run the v9 engine once on every case of the gold specification, at one commit, under one currency cap.

    python scripts/v9_frozen_suite.py run --out runs/eval_v9_frozen_<date> --budget-usd 2.00
    python scripts/v9_frozen_suite.py audit --out runs/eval_v9_frozen_<date>

`run` reads only each case's clean request (variant, origin, and for the supplied_disease form the disease) from
eval/v9_gold_spec.json: no label, component or note reaches the engine, which is started as a separate process
(`v2m v9 run`) per case. It refuses a working tree with uncommitted changes, because the suite is one test of one
frozen engine, and it stops before a case once the suite has spent its cap. A case that already has a folder is
skipped, so an interrupted suite resumes; nothing is ever re-run or overwritten. `audit` then scores each finished
run with `v2m v9 audit` and writes one table. With --dry-run, `run` prints what it would do and starts nothing.
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "eval" / "v9_gold_spec.json"
LEDGER = ROOT / "state" / "budget_release.json"        # the release profile's ledger; `v2m v9 run` charges "dev"


def requests(form: str) -> list[dict]:
    """The clean requests, in the specification's order: nothing but what a user would type."""
    spec = json.loads(SPEC.read_text())
    return [{"case_id": c["case_id"], **{k: c["requests"][form][k] for k in ("variant", "origin", "disease", "context")}}
            for c in spec["cases"]]


def spent() -> float:
    return float(json.loads(LEDGER.read_text())["dev"]["spent"]) if LEDGER.exists() else 0.0


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()


def command(request: dict, folder: Path) -> list[str]:
    cmd = ["v2m", "v9", "run", "--variant", request["variant"], "--origin", request["origin"], "--out", str(folder)]
    for flag in ("disease", "context"):
        for value in request[flag]:
            cmd += [f"--{flag}", value]
    return cmd


def run(args) -> int:
    out = (ROOT / args.out).resolve()
    todo = requests(args.form)
    if args.dry_run:
        for r in todo:
            print(" ".join(command(r, out / r["case_id"])))
        print(f"{len(todo)} cases, form {args.form}, cap ${args.budget_usd:.2f}; ledger at ${spent():.4f}")
        return 0
    if git("status", "--porcelain", "--untracked-files=no"):
        print("refused: the working tree has uncommitted changes; a frozen suite runs one commit", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    record_path = out / "suite.json"
    record = json.loads(record_path.read_text()) if record_path.exists() else {
        "commit": git("rev-parse", "HEAD"), "form": args.form, "budget_usd": args.budget_usd,
        "started": datetime.now().isoformat(timespec="seconds"), "ledger_before": spent(), "cases": {}}
    if record["commit"] != git("rev-parse", "HEAD") or record["form"] != args.form:
        print(f"refused: {record_path} was started at commit {record['commit'][:7]} with form {record['form']}",
              file=sys.stderr)
        return 2
    for r in todo:
        folder = out / r["case_id"]
        if folder.exists():
            continue
        used = spent() - record["ledger_before"]
        if used >= args.budget_usd:
            print(f"stopped before {r['case_id']}: ${used:.4f} of the ${args.budget_usd:.2f} cap is spent")
            break
        before = spent()
        done = subprocess.run(command(r, folder), cwd=ROOT, capture_output=True, text=True)
        (out / f"{r['case_id']}.log").write_text(done.stdout + done.stderr)
        record["cases"][r["case_id"]] = {"exit": done.returncode, "cost_usd": round(spent() - before, 6),
                                        "finished": (folder / "graph.json").exists()}
        record_path.write_text(json.dumps(record, indent=1))
        print(f"{r['case_id']}: exit {done.returncode}, ${record['cases'][r['case_id']]['cost_usd']:.4f}", flush=True)
    record["spent_usd"] = round(spent() - record["ledger_before"], 6)
    record_path.write_text(json.dumps(record, indent=1))
    print(f"suite: {len(record['cases'])} of {len(todo)} cases run, ${record['spent_usd']:.4f}")
    return 0


def audit(args) -> int:
    out = (ROOT / args.out).resolve()
    for r in requests("main"):
        folder = out / r["case_id"]
        if not (folder / "graph.json").exists():
            print(f"{r['case_id']}: no finished run")
            continue
        done = subprocess.run(["v2m", "v9", "audit", "--run", str(folder), "--case", r["case_id"]], cwd=ROOT,
                              capture_output=True, text=True)
        print(f"{r['case_id']}: {(done.stdout or done.stderr).strip().splitlines()[-1] if done.stdout or done.stderr else done.returncode}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="action", required=True)
    r = sub.add_parser("run")
    r.add_argument("--out", required=True, help="the suite's folder, under the repository")
    r.add_argument("--budget-usd", type=float, required=True, help="the cap for the whole suite")
    r.add_argument("--form", choices=["main", "supplied_disease"], default="main",
                   help="main gives the engine the variant alone; supplied_disease adds the disease")
    r.add_argument("--dry-run", action="store_true")
    a = sub.add_parser("audit")
    a.add_argument("--out", required=True)
    args = parser.parse_args()
    return run(args) if args.action == "run" else audit(args)


if __name__ == "__main__":
    sys.exit(main())
