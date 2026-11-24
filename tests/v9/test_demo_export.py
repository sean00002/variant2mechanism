"""The public copies kept in the repository (scripts/v9_demo_export.py): the cut of a report and the packed graph."""

import gzip
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def export():
    spec = importlib.util.spec_from_file_location("v9_demo_export", ROOT / "scripts" / "v9_demo_export.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


REPORT = """# v2m run report: a variant

Case and request.

## Answer: ranked mechanism chains

**Leading chain: a TF → a gene.**

## Chain table

| Step | Claim |
|---|---|
| TF binding | The alleles differ |

The table passes every rule.

### The numbers behind the cells

| Claim | What it returned |
|---|---|
| TF binding: the alleles differ | FDR 0.00037 |

### What would fill the gaps

- **Regulatory activity: the alleles differ** (nothing supports it). Experiment: a reporter assay.

### Reading the tie

- PMID:1: "a sentence copied from an article"

### What the articles say

- PMID:2: "another sentence copied from an article"

## Outcome

**Partial mechanism**; stopped because converged.

## Mechanism chain

Everything from here on is the full report.

## Evidence

- E1: "a third sentence"
"""


def test_the_answer_keeps_the_request_the_answer_the_table_and_the_outcome(export):
    answer = export.answer_part(REPORT)
    for kept in ("# v2m run report", "Case and request.", "**Leading chain", "| TF binding | The alleles differ |",
                 "The table passes every rule.", "### The numbers behind the cells", "FDR 0.00037",
                 "### What would fill the gaps", "a reporter assay", "## Outcome", "**Partial mechanism**"):
        assert kept in answer
    assert answer.endswith("stopped because converged.\n")


def test_the_answer_leaves_out_every_subsection_that_quotes_an_article_and_the_rest_of_the_report(export):
    answer = export.answer_part(REPORT)
    for cut in ("Reading the tie", "What the articles say", "copied from an article", "Mechanism chain",
                "## Evidence", "a third sentence"):
        assert cut not in answer


def test_a_folder_without_a_graph_has_none(export, tmp_path):
    assert not export.has_graph(tmp_path)
    assert export.saved_graph(tmp_path) is None


def test_a_packed_public_copy_gives_the_table_saved_beside_it(export, tmp_path):
    from variant2mechanism.v9 import table as T

    folder = ROOT / "demo" / "tables" / "rs13078086"           # the smallest of the saved copies
    if not export.has_graph(folder):
        pytest.skip("demo/tables is not in this checkout")
    graph = export.saved_graph(folder)
    table = T.from_graph(graph)
    assert not T.check(table, graph)
    assert T.to_markdown(table, []) == (folder / "table.md").read_text(encoding="utf-8")
    # the same graph unpacked reads the same: a run folder and its public copy are one thing to the scripts
    with gzip.open(folder / "graph.json.gz", "rb") as packed:
        (tmp_path / "graph.json").write_bytes(packed.read())
    assert export.saved_graph(tmp_path).to_json() == graph.to_json()
