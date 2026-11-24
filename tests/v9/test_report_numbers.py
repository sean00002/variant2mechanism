"""Under the chain table: the numbers each source returned, and what would fill the gaps (v9/report.py)."""

import gzip
import sys
from pathlib import Path

import pytest

from variant2mechanism.v9 import report as R
from variant2mechanism.v9 import table as T
from variant2mechanism.v9.graph import ClaimGraph

ROOT = Path(__file__).resolve().parents[2]
COPIES = ROOT / "demo" / "tables"                         # public copies of saved runs: real records, no network


def graph(case: str) -> ClaimGraph:
    packed = COPIES / case / "graph.json.gz"
    if not packed.is_file():
        pytest.skip("demo/tables is not in this checkout")
    with gzip.open(packed, "rt", encoding="utf-8") as handle:
        return ClaimGraph.from_json(handle.read())


@pytest.fixture(scope="module")
def hox() -> tuple[ClaimGraph, dict]:
    g = graph("rs339331")
    return g, R.table_extras(g)


def rows_of(extras: dict, claim: str, source: str) -> list[list[str]]:
    return [row for row in extras["numbers"] if row[0] == claim and row[2].startswith(source)]


def test_a_span_is_one_value_or_the_lowest_and_the_highest():
    assert R._span([], str) == ""
    assert R._span([0.5], lambda x: f"{x:.1f}") == "0.5"
    assert R._span([0.2, 0.9, 0.5], lambda x: f"{x:.1f}") == "0.2 to 0.9"
    assert R._span([0.51, 0.52], lambda x: f"{x:.1f}") == "0.5"          # the same in words is said once
    assert R._p_text(0.0) == "below 1e-300" and R._p_text(4.1e-5) == "4.1e-05"
    assert R._some(["a", "b", "a", "", None, "c", "d", "e", "f"]) == "a, b, c, d and 2 more"


def test_every_number_is_the_records_own(hox):
    """The allele-specific binding row says what the saved record holds, to the digit it is shown with."""
    g, extras = hox
    (row,) = rows_of(extras, "TF binding: the alleles differ", "ADASTRA")
    ev = next(e for e in g.evidence.values() if (e.data or {}).get("source") == "ADASTRA" and "HOXB13" in e.about_tfs)
    fdr = min(ev.data["fdr_ref"], ev.data["fdr_alt"])
    assert row[1] == "Database" and row[3] == "1"
    assert f"FDR {fdr:.2g}" in row[4] and f"reads favour {ev.allele}" in row[4]
    assert f"{ev.data['tf_experiments']} experiments" in row[4]


def test_a_prediction_row_gives_the_models_numbers_and_where_they_stand_in_the_background(hox):
    _, extras = hox
    (row,) = rows_of(extras, "TF binding: the alleles differ", "QBiC-SELEX")
    assert row[1] == "Model prediction"
    for part in ("group G024", "more binding to T", "|z| 103.5", "p below 1e-300", "4 of 4 models past the gate",
                 "in the top 10% for this group"):
        assert part in row[4]


def test_a_literature_row_counts_experiments_and_articles_and_quotes_nothing(hox):
    _, extras = hox
    for row in extras["numbers"]:
        if row[1] == "Literature":
            assert "experiment" in row[4] and "article" in row[4] and "PMID:" in row[4]
            assert '"' not in row[4]                                      # the sentences stay in the quotations


def test_the_rows_of_a_cell_hold_every_record_the_cell_counts(hox):
    g, extras = hox
    table = T.from_graph(g)
    first = table.chains[0]
    steps, parts, lanes = dict(T.STEPS), dict(T.PARTS), dict(T.LANES)
    for key in T.SLOT_KEYS:
        claim = table.claims[str(first.claims[key])]
        title = f"{steps[claim.step]}: {parts[claim.part].lower()}"
        for lane in T.LANE_KEYS:
            counted = sum(r.stance != "beside" for r in claim.cells[lane].records)
            shown = sum(int(row[3]) for row in extras["numbers"] if row[0] == title and row[1] == lanes[lane])
            assert shown == counted, (key, lane)


def test_a_range_never_picks_a_best_record(hox):
    """Several records of one source give the lowest and the highest value, not the best one."""
    _, extras = hox
    (row,) = rows_of(extras, "Trait: the alleles differ", "Open Targets credible sets")
    assert int(row[3]) > 1 and " to " in row[4] and "fine-mapping probability" in row[4]


def test_the_gaps_of_a_chain_with_measured_binding_and_gene_are_its_regulatory_activity(hox):
    _, extras = hox
    assert [(f["claim"], f["kind"]) for f in extras["fills"]] == [
        ("Regulatory activity: the alleles differ", "Experiment"),
        ("Regulatory activity: the alleles differ", "Model run")]
    assert all(f["state"] == "nothing supports it" for f in extras["fills"])
    assert "reporter assay" in extras["fills"][0]["text"] and "LNCaP" in extras["fills"][0]["text"]


def test_a_somatic_mutation_is_told_which_source_is_missing():
    fills = R.table_extras(graph("tert_c228t"))["fills"]
    assert fills[0]["claim"] == "The tie for first" and "transcription factor" in fills[0]["text"]
    by_kind = {(f["claim"], f["kind"]): f["text"] for f in fills}
    assert "somatic" in by_kind[("Trait: the alleles differ", "Source")]
    assert "eQTL cannot exist for a somatic mutation" in by_kind[("Target gene: the alleles differ", "Experiment")]
    order = [f["state"] for f in fills[1:]]
    assert order == sorted(order, key=list(R.NEEDS.values()).index)      # the weakest claims first


def test_a_tie_names_every_tied_gene_and_no_single_factor():
    fills = R.table_extras(graph("rs642961"))["fills"]
    assert "target gene" in fills[0]["text"] and "IRF6" in fills[0]["text"]
    gene = next(f for f in fills if f["claim"] == "Target gene: the alleles differ")
    assert "IRF6" in gene["text"] and "UTP25" in gene["text"]             # each tied gene, not the first chain's
    tied = R.table_extras(graph("rs12740374"))["fills"]
    binding = next(f for f in tied if f["claim"] == "TF binding: the alleles differ")
    assert "each of the tied transcription factors" in binding["text"] and "predicts more binding" not in binding["text"]


def test_both_formats_show_the_two_blocks_and_point_to_them():
    from variant2mechanism.v9.bundle import Bundle

    g = graph("rs13078086")                                               # the smallest saved copy
    bundle = Bundle(path=COPIES / "rs13078086", manifest={}, graph=g, metrics={}, evaluation=None, integrity=())
    md, page = R.render_markdown(bundle, render_only=True), R.render_html(bundle, render_only=True)
    for text in (md, page):
        assert R.NUMBERS_TITLE in text and R.FILLS_TITLE in text and "under the chain table" in text
    assert "None suggested." not in md
    assert "<li>None suggested.</li>" not in page         # the page's script holds the words for a run with no gaps
    assert md.index(R.NUMBERS_TITLE) < md.index(R.FILLS_TITLE) < md.index("## Outcome")
    assert "\\|z\\|" in md                                                # a bar inside a table cell is escaped


def test_a_chain_with_nothing_to_fill_says_so_and_a_run_with_no_chain_shows_neither_block():
    full = {"rows": [["TF binding"]], "numbers": [], "fills": []}
    assert R.FILLS_NONE in "\n".join(R._fills_markdown(full)) and R.FILLS_NONE in R._fills_html(full)
    assert R._numbers_markdown(full) == [] and R._numbers_html(full) == ""
    empty = {"rows": [], "numbers": [], "fills": []}
    assert R._fills_markdown(empty) == [] and R._fills_html(empty) == ""
    assert sys.modules[R.__name__].table_extras(ClaimGraph.from_json(graph("rs13078086").to_json()))["numbers"]
