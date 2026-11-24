"""Public copies of saved fill runs, small enough to keep in the repository.

    python scripts/v9_demo_export.py --runs runs/<suite> --out demo/<a new folder>

For every run folder under --runs this makes the run's public copy in a temporary folder (`v2m v9 export`: quoted
passages bounded, article text removed, local paths cut) and keeps four files of it:

    graph.json.gz   the claim graph of the public copy: what the table, the report and the score are built from
    table.md        the first chain's eight claims and their cells (v9/table.py)
    answer.md       the top of the run's report: the ranked chains, the first chain's table and the outcome
    manifest.json   what ran (models, formats, sources) and what the export cut

answer.md leaves out the report's two subsections that quote the articles (the reading of a tie and the
quotations). The quotations are in the graph and the rendered report shows them: unpack graph.json.gz into an empty
folder as graph.json and run `v2m v9 report --run <that folder>`.

scripts/v9_chain_table.py and scripts/v9_table_score.py read a folder made here as they read a folder of runs
(`saved_graph`). Nothing is written into an existing --out folder, and the runs are not changed.
"""

import argparse
import gzip
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from variant2mechanism.v9 import table as T  # noqa: E402
from variant2mechanism.v9.bundle import export_public, load_bundle  # noqa: E402
from variant2mechanism.v9.graph import ClaimGraph  # noqa: E402

GRAPH, PACKED = "graph.json", "graph.json.gz"
KEPT_SECTIONS = ("Answer", "Chain table", "Outcome")      # second-level sections of a report that answer.md keeps
QUOTING = ("Reading the tie", "What the articles say")    # their subsections that quote articles: left out
FOOTER = ("\n---\n\nThis page is the top of the run's report. The whole report, with the sentences quoted from the "
          "articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).\n")


def has_graph(folder: Path) -> bool:
    return (folder / GRAPH).is_file() or (folder / PACKED).is_file()


def saved_graph(folder: Path) -> ClaimGraph | None:
    """The claim graph of a run folder (graph.json) or of a public copy made here (graph.json.gz); None when the
    folder holds neither."""
    if (folder / GRAPH).is_file():
        return load_bundle(folder).graph
    if (folder / PACKED).is_file():
        with gzip.open(folder / PACKED, "rt", encoding="utf-8") as handle:
            return ClaimGraph.from_json(handle.read())
    return None


def answer_part(report: str) -> str:
    """A report down to its outcome, without the subsections that quote articles: the title and the request, the
    answer, the first chain's table with its numbers and what would fill its gaps, and the outcome."""
    kept, keep, quoting = [], True, False
    for line in report.splitlines():
        if line.startswith("## "):
            keep, quoting = line[3:].startswith(KEPT_SECTIONS), False
        elif line.startswith("### "):
            quoting = line[4:].startswith(QUOTING)
        if keep and not quoting:
            kept.append(line)
    return "\n".join(kept).rstrip() + "\n"


def export_case(run: Path, out: Path) -> dict:
    """One run's public copy, reduced to the four files. Returns what was written, for the log."""
    with tempfile.TemporaryDirectory() as tmp:
        public = export_public(run, Path(tmp) / run.name)
        text = (public / GRAPH).read_text(encoding="utf-8")
        graph = ClaimGraph.from_json(text)
        table = T.from_graph(graph)
        problems = T.check(table, graph)
        out.mkdir(parents=True)
        with open(out / PACKED, "wb") as raw, gzip.GzipFile(GRAPH, "wb", 9, raw, mtime=0) as handle:
            handle.write(text.encode("utf-8"))                 # mtime 0: the same graph gives the same bytes
        (out / "table.md").write_text(T.to_markdown(table, problems), encoding="utf-8")
        (out / "answer.md").write_text(answer_part((public / "report.md").read_text(encoding="utf-8")) + FOOTER,
                                       encoding="utf-8")
        shutil.copyfile(public / "manifest.json", out / "manifest.json")
    return {"run": run.name, "chains": len(table.chains), "problems": len(problems),
            "packed_bytes": (out / PACKED).stat().st_size}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--runs", required=True, help="a folder of saved fill runs, one folder per case")
    parser.add_argument("--out", required=True, help="a new folder for the public copies")
    args = parser.parse_args()
    runs, out = (ROOT / args.runs).resolve(), (ROOT / args.out).resolve()
    if out.exists():
        print(f"refused: {out} already exists; choose a new folder", file=sys.stderr)
        return 2
    folders = sorted(p for p in runs.iterdir() if (p / GRAPH).is_file())
    if not folders:
        print(f"refused: no run folder with a {GRAPH} under {runs}", file=sys.stderr)
        return 2
    total = 0
    for folder in folders:
        row = export_case(folder, out / folder.name)
        total += row["packed_bytes"]
        print(f"{row['run']}: {row['chains']} chain(s), {row['problems']} rule(s) broken, "
              f"{row['packed_bytes'] / 1e6:.2f} MB", flush=True)
    print(f"{len(folders)} public copies in {out} ({total / 1e6:.1f} MB of graphs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
