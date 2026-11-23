"""Freeze the fill pipeline: write, or check, the hashes of everything a fill run executes.

    python scripts/v9_freeze.py write --out eval/fill_freeze_<date>.json --runs runs/<the suite to be scored>
    python scripts/v9_freeze.py check eval/fill_freeze_<date>.json

A freeze says that from here nothing changes in how the pipeline fills a table, reads an article, checks a record
or reads a tie, so that one scoring against the gold cases is a test and not a step of development. The work tree
need not be committed for that: the freeze is the sha256 of every file a fill run executes (the package's code,
its prompts and resources, config.yaml, the lock file, the TF group registry), the formats the code declares, the
gold specification it will be scored against, and each table of the suite that will be scored. `check` computes
them again and lists every file that differs; it exits 1 when one does.

Left out on purpose: the report's rendering and the evaluator (v9/report.py, v9/report_template.html,
v9/evaluation.py) and everything under scripts/, docs/ and tests/. How a result is shown, scored or described may
still change after a freeze; what the result is may not.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

PACKAGE = ROOT / "src" / "variant2mechanism"
NOT_FROZEN = {"v9/report.py", "v9/report_template.html", "v9/evaluation.py"}     # display and scoring, not the result
OTHER_FILES = ("config.yaml", "uv.lock", "cache/groups.json", "eval/v9_gold_spec.json")
RUN_FILES = ("table.json", "graph.json")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pipeline_files() -> dict[str, str]:
    """Every file of the package a run can execute or read (code, prompts, resources), less what only shows or
    scores a result, then the files beside the package that a run reads; by path from the repository's root."""
    found = {}
    for path in sorted(PACKAGE.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        if path.relative_to(PACKAGE).as_posix() in NOT_FROZEN:
            continue
        found[path.relative_to(ROOT).as_posix()] = sha256(path)
    for name in OTHER_FILES:
        if (ROOT / name).exists():
            found[name] = sha256(ROOT / name)
    return found


def formats() -> dict[str, int]:
    from variant2mechanism.v9 import critic, fill, judge, reader, table
    return {"fill_format": fill.FILL_FORMAT, "reader_format": reader.READER_FORMAT,
            "critic_format": critic.CRITIC_FORMAT, "judge_format": judge.JUDGE_FORMAT, "table_format": table.FORMAT}


def run_files(runs: Path) -> dict[str, dict[str, str]]:
    return {folder.name: {name: sha256(folder / name) for name in RUN_FILES if (folder / name).exists()}
            for folder in sorted(p for p in runs.iterdir() if (p / "table.json").exists())}


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=False).stdout.strip()


def write(out: Path, runs: Path | None) -> int:
    if out.exists():
        print(f"refused: {out} already exists; a freeze is written once", file=sys.stderr)
        return 2
    record = {
        "what": "The fill pipeline as frozen for one scoring of the evaluated cases: the hashes of everything a "
                "fill run executes. scripts/v9_freeze.py check <this file> lists what has changed since.",
        "frozen": date.today().isoformat(),
        "git": {"head": git("rev-parse", "HEAD"), "branch": git("rev-parse", "--abbrev-ref", "HEAD"),
                "uncommitted_files": len([x for x in git("status", "--porcelain").splitlines() if x.strip()])},
        "formats": formats(),
        "not_frozen": sorted(NOT_FROZEN) + ["scripts/", "docs/", "tests/"],
        "files": pipeline_files(),
        **({"runs": str(runs.relative_to(ROOT)), "run_files": run_files(runs)} if runs is not None else {}),
    }
    out.write_text(json.dumps(record, indent=1) + "\n")
    print(f"freeze written: {len(record['files'])} files"
          + (f", {len(record['run_files'])} runs of {record['runs']}" if runs is not None else "") + f"; {out}")
    return 0


def differences(record: dict) -> list[str]:
    """What differs from a freeze: a file changed, gone or new; a format; a table or graph of the frozen suite."""
    now, then = pipeline_files(), record["files"]
    found = [f"changed: {name}" for name in sorted(set(now) & set(then)) if now[name] != then[name]]
    found += [f"gone: {name}" for name in sorted(set(then) - set(now))]
    found += [f"new: {name}" for name in sorted(set(now) - set(then))]
    found += [f"format {key}: was {value}, is {formats().get(key)}" for key, value in record["formats"].items()
              if formats().get(key) != value]
    if record.get("runs"):
        current = run_files(ROOT / record["runs"]) if (ROOT / record["runs"]).exists() else {}
        for case, files in record["run_files"].items():
            found += [f"run {case}: {name} differs or is gone" for name, digest in files.items()
                      if current.get(case, {}).get(name) != digest]
    return found


def check(path: Path) -> int:
    record = json.loads(path.read_text())
    found = differences(record)
    for line in found:
        print(line)
    print(f"{path.name} ({record['frozen']}): " + (f"{len(found)} difference(s)" if found else
                                                    f"nothing has changed in {len(record['files'])} files"
                                                    + (f" and {len(record.get('run_files', {}))} runs"
                                                       if record.get("runs") else "")))
    return 1 if found else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    w = sub.add_parser("write", help="write a freeze")
    w.add_argument("--out", required=True, help="a new JSON file, under the repository")
    w.add_argument("--runs", default=None, help="the suite that will be scored: its tables are pinned too")
    c = sub.add_parser("check", help="list what differs from a freeze")
    c.add_argument("freeze")
    args = parser.parse_args()
    if args.command == "write":
        return write((ROOT / args.out).resolve(), (ROOT / args.runs).resolve() if args.runs else None)
    return check((ROOT / args.freeze).resolve())


if __name__ == "__main__":
    sys.exit(main())
