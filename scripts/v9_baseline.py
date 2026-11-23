"""M0 of the v9 plan: freeze the current baseline without committing anything.

Writes runs/v9_baseline/<label>/ (gitignored) with:
  manifest.json      HEAD, branch, the changed and untracked files with their SHA-256, and fingerprints of the
                     configuration, prompts, gold set, QBiC cache, SCREEN downloads and the HTTP/LLM caches
  tracked.patch      `git diff --binary HEAD`: every uncommitted change to tracked files
  untracked.tar.gz   the untracked, non-ignored files (the M1 work), exactly as they are on disk

Nothing in the repository is changed, staged or committed. Re-running with the same label refuses to overwrite.

    UV_PROJECT_ENVIRONMENT=$HOME/.venvs/v2m-v2 uv run --frozen python scripts/v9_baseline.py --label 2026-11-08
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tarfile
from datetime import UTC, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def tree_fingerprint(folder: Path, pattern: str = "*") -> dict:
    """Count and hash the names and sizes of a folder's files (cheap; contents of large caches are not read)."""
    if not folder.exists():
        return {"exists": False}
    h = hashlib.sha256()
    n = 0
    size = 0
    for p in sorted(folder.rglob(pattern)):
        if p.is_file():
            st = p.stat()
            h.update(f"{p.relative_to(folder)}\t{st.st_size}\n".encode())
            n += 1
            size += st.st_size
    return {"exists": True, "files": n, "bytes": size, "names_sizes_sha256": h.hexdigest()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--label", default=datetime.now(UTC).strftime("%Y-%m-%d"))
    args = ap.parse_args()
    out = ROOT / "runs" / "v9_baseline" / args.label
    if out.exists():
        print(f"{out} exists; a baseline is immutable, choose another --label", file=sys.stderr)
        return 1
    out.mkdir(parents=True)

    changed = [line[3:] for line in git("status", "--porcelain").splitlines() if not line.startswith("??")]
    untracked = git("ls-files", "--others", "--exclude-standard").splitlines()
    (out / "tracked.patch").write_text(git("diff", "--binary", "HEAD"))
    with tarfile.open(out / "untracked.tar.gz", "w:gz") as tar:
        for rel in untracked:
            tar.add(ROOT / rel, arcname=rel)

    files = {}
    for rel in sorted(set(changed) | set(untracked)):
        p = ROOT / rel
        files[rel] = sha256(p) if p.is_file() else "missing"
    fingerprints = {}
    for rel in ["config.yaml", "pyproject.toml", "uv.lock", "data/gold_set.csv", "cache/qbic.sqlite", "cache/groups.json",
                "data/screen/MANIFEST.md5"]:
        p = ROOT / rel
        fingerprints[rel] = sha256(p) if p.is_file() else "missing"
    for rel in ["src/variant2mechanism/v8/prompts", "src/variant2mechanism/agent/prompts"]:
        fingerprints[rel] = {str(p.relative_to(ROOT)): sha256(p) for p in sorted((ROOT / rel).glob("*.txt"))}
    caches = {name: tree_fingerprint(ROOT / name) for name in ["cache/http", "cache/llm", "cache/screen", "data/screen"]}

    manifest = {
        "kind": "v9_baseline",
        "created_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "head": git("rev-parse", "HEAD").strip(),
        "branch": git("branch", "--show-current").strip(),
        "changed_tracked": sorted(changed),
        "untracked": sorted(untracked),
        "file_sha256": files,
        "fingerprints": fingerprints,
        "caches": caches,
        "tracked_patch_sha256": sha256(out / "tracked.patch"),
        "untracked_tar_sha256": sha256(out / "untracked.tar.gz"),
        "note": "Snapshot of the working tree before v9 work. Nothing was staged or committed. Restore with "
                "`git apply tracked.patch` on HEAD and `tar xzf untracked.tar.gz`.",
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"baseline written to {out.relative_to(ROOT)}: {len(changed)} changed, {len(untracked)} untracked files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
