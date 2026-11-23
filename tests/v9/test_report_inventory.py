"""The report's QBiC-SELEX inventory on real adapter output: qbic_inventory run offline on the development case
rs1427407 (chr2:60490908 T>G), reading cache/qbic.sqlite read only. Several groups there have gate-passing models that
disagree about the allele; group G049 is one (SPIB's model favours G, SPI1's own model favours T), so it carries one
Evidence item per allele. Each row must join the item for the allele its best model names (the adapters' own rule),
and the report must show both items and count the row as linked through either. Skipped when the data folder or the
QBiC-SELEX caches are absent. The groups and alleles asserted are facts of the cached scores, not tuned outcomes."""

import pytest

from variant2mechanism.v9 import adapters, bundle, report
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef
from variant2mechanism.v9.http9 import Http9
from variant2mechanism.v9.schemas import Case, ToolRequest, Variant
from variant2mechanism.v9.tools import ToolRunner

from .test_report_support import write_run

pytestmark = pytest.mark.data

DEV = Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"))


@pytest.fixture
def inventory_graph(v9_cfg, tmp_path) -> ClaimGraph:
    """The development case's graph after code's qbic_inventory call, offline (skipped without the caches)."""
    for section, key in (("cache", "db"), ("cache", "groups")):
        if not v9_cfg.path(section, key).is_file():
            pytest.skip(f"the QBiC-SELEX cache {v9_cfg[section][key]} is not present")
    runner = ToolRunner(config=v9_cfg, mode="cache_only", http=Http9.from_config(v9_cfg, offline=True),
                        run_dir=tmp_path / "run", clock=lambda: "2026-11-08T12:00:00+00:00")
    graph = ClaimGraph(DEV)
    call = runner.run(ToolRequest(tool="qbic_inventory"), graph.case, graph, "code")
    if call.execution_status != "success":
        pytest.skip(f"qbic_inventory did not run offline here: {call.execution_status} ({call.message})")
    return graph


def test_real_inventory_rows_join_the_item_for_the_rows_allele(inventory_graph):
    g = inventory_graph
    rows = bundle.inventory_table(g)
    assert rows == adapters.inventory_rows(g)                 # the adapters' rule, read from the graph alone
    items = bundle.inventory_items(g)
    split = {group for group, ids in items.items() if len(ids) > 1}
    assert "G049" in split and all(len(ids) <= 2 for ids in items.values())
    v = g.case.variant
    for row in rows:
        if row["passes_gate"]:
            joined = g.evidence[row["evidence_id"]]
            assert joined.data["group_id"] == row["group_id"]
            assert joined.allele == (v.alt if row["binds_more"] == "alt" else v.ref)
        else:
            assert row["evidence_id"] is None and str(row["group_id"]) not in items
    g049 = next(r for r in rows if r["group_id"] == "G049")
    assert g049["binds_more"] == "alt" and g.evidence[g049["evidence_id"]].allele == "G"
    assert bundle.inventory_summary(g)["gate_passing"] == len(items) == sum(r["passes_gate"] for r in rows)


def test_the_report_shows_both_items_of_a_discordant_real_group(inventory_graph, tmp_path):
    g = inventory_graph
    g049 = bundle.inventory_items(g)["G049"]
    own_t = next(e for e in g049 if g.evidence[e].allele == "T")          # SPI1's own model favours T
    assert "SPI1" in g.evidence[own_t].about_tfs and g.evidence[own_t].data["mapping"]["SPI1"] == "own"
    binds_t = g.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label="rs1427407")],
                                     relation="alters_binding", objects=[EntityRef(kind="tf", label="SPI1")],
                                     direction="increases", effect_allele="T"), "coordinator")
    g.link(binds_t, own_t, "supports", "computational_investigator", "SPI1's own model favours T")
    data = report.report_data(bundle.load_bundle(write_run(g, tmp_path / "bundle")))
    row = next(r for r in data["inventory"]["rows"] if r["group"] == "G049")
    assert row["discordant"] is True and row["evidence"] != own_t                  # the row is SPIB's model's (G)
    assert sorted((x["id"], x["allele"]) for x in row["items"]) == sorted((e, g.evidence[e].allele) for e in g049)
    assert row["claims"] == [binds_t] and data["inventory"]["linked"] == 1        # linked through the T item
    assert all(data["evidence"][e]["inventory"] for e in g049)                   # neither is "other evidence"
    html = report.render_html(bundle.load_bundle(tmp_path / "bundle"))
    assert "the group&#x27;s gate-passing models disagree" in html and f"{own_t}: T binds more" in html
