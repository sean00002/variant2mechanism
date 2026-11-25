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


def test_the_current_copies_rebuild_and_a_join_reads_from_the_packed_graph_alone(export):
    from variant2mechanism.v9 import table as T

    folder = ROOT / "demo" / "current"
    if not export.has_graph(folder / "rs12740374"):
        pytest.skip("demo/current is not in this checkout")
    for case in ("rs12740374", "tert_c228t", "rs7001688"):
        graph = export.saved_graph(folder / case)
        table = T.from_graph(graph)
        assert not T.check(table, graph)
        assert T.to_markdown(table, []) == (folder / case / "table.md").read_text(encoding="utf-8")
    # the record that joins the C/EBP group to SORT1 puts their chain first, and no symbol table is needed to see it
    first = T.from_graph(export.saved_graph(folder / "rs12740374")).chains[0]
    assert (first.rank, first.ties, first.title) == (1, 1, "G035 (CEBPA, CEBPB, CEBPE) → SORT1")
    assert len(first.joined) == 2
    # a random control is what it was: every chain ties and nothing joins
    control = T.from_graph(export.saved_graph(folder / "rs7001688"))
    assert control.chains[0].ties == 316 and not any(c.joined for c in control.chains)


def test_the_loop_copies_rebuild_and_show_their_round_from_the_packed_graph_alone(export):
    from variant2mechanism.v9 import loop
    from variant2mechanism.v9 import table as T

    folder = ROOT / "demo" / "loop"
    if not export.has_graph(folder / "tert_c250t"):
        pytest.skip("demo/loop is not in this checkout")
    views = {}
    for case in ("tert_c250t", "rs4684847", "rs4784227", "rs9349379"):
        graph = export.saved_graph(folder / case)
        table = T.from_graph(graph)
        assert not T.check(table, graph)
        assert T.to_markdown(table, []) == (folder / case / "table.md").read_text(encoding="utf-8")
        views[case] = view = loop.report_view(graph)
        assert "It was a dry run" in view["lead"] and "did not change" in view["moved"]
        # a dry run reads nothing and files nothing, whatever its searches listed
        assert all((row[5], row[6]) == ("0", "0") for row in view["effort"])
    column = {name: i for i, name in enumerate(loop.EFFORT_HEADERS)}
    # a tie with no article on file: one search for each tied TF group, then the names a catalogue gives the mutation
    tied = views["tert_c250t"]["effort"]
    assert [row[column["Why"]] for row in tied] == (["the variant with a tied candidate"] * 11
                                                    + ["another name of the variant"] * 2)
    assert [row[column["Searched for"]] for row in tied[-2:]] == ["C250T", "-146C>T"]
    assert sum(int(row[column["New"]]) for row in tied) == 41
    # every pair of TF and gene in the first chains is searched alike, and a pair with no article stays unjoined
    pairs = [row for row in views["rs4684847"]["effort"] if row[column["Why"]] == "the TF changed and the gene read out"]
    assert [row[column["Searched for"]] for row in pairs] == ["PRRX1 → PPARG", "PRRX1 → TIMP4", "ILF3 → PPARG",
                                                              "ILF3 → TIMP4"]
    assert all(row[column["Join the pair"]] == "0" for row in pairs)
    # where pairs do list articles, they wait for the joiner: seven readings at rs4784227, none made in a dry run
    queued = [row for row in views["rs4784227"]["effort"] if row[column["Why"]] == "the TF changed and the gene read out"]
    assert len(queued) == 4 and sum(int(row[column["New"]]) for row in queued) == 7
    # a random control: 316 chains tie, too many to search alike, so nothing is searched and the report says so
    control = loop.report_view(export.saved_graph(folder / "rs7001688"))
    assert control["effort"] == [] and "there was nothing to search for" in control["lead"]
    assert control["rounds"] == ["Round 1, planned by code: nothing on the menu; 316 tied candidates are too many to "
                                 "search for one by one."]
