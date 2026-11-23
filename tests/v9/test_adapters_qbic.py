"""qbic_inventory and qbic_tf_detail against the real cache/qbic.sqlite, read only (SPEC 13.2, 13.5; contract C2).

rs1427407 (chr2:60490908 T>G) is the development case. rs12740374 is a gold case and appears here only to test
plumbing: the counts and groups asserted are facts of the cached scores, not tuned outcomes.
"""

import dataclasses
import json
import sqlite3

import pytest

from variant2mechanism.config import REPO
from variant2mechanism.v9.adapters import inventory_evidence, inventory_rows
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, GraphRefusal
from variant2mechanism.v9.http9 import Http9
from variant2mechanism.v9.qbic_reader import QbicReader, paralog_stems, symbol_stems
from variant2mechanism.v9.schemas import Case, ToolCall, ToolRequest, Variant
from variant2mechanism.v9.tools import ToolRunner

pytestmark = pytest.mark.data

ROW_KEYS = {"group_id", "group_label", "dbd", "members", "paralog_stem", "best_model", "binds_more", "z", "effect",
            "p", "n_pass", "n_models", "passes_gate"}
SORT1 = Case(case_id="DEV-PLUMBING-1", variant=Variant(chrom="1", pos=109274968, ref="G", alt="T"))
DEV = Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"))
UNCACHED = Case(case_id="DEV-2", variant=Variant(chrom="2", pos=60490908, ref="T", alt="C"))


@pytest.fixture
def runner(v9_cfg, tmp_path) -> ToolRunner:
    return ToolRunner(config=v9_cfg, mode="cache_only", http=Http9.from_config(v9_cfg, offline=True),
                      run_dir=tmp_path / "run", clock=lambda: "T0")


def run(runner: ToolRunner, graph: ClaimGraph, tool: str, **params) -> ToolCall:
    return runner.run(ToolRequest(tool=tool, params=params), graph.case, graph, "computational_investigator")


def test_inventory_lists_every_group_in_neutral_order_with_evidence_for_each_gate_passer(runner, tmp_path):
    graph = ClaimGraph(SORT1)
    call = run(runner, graph, "qbic_inventory")
    rows = call.observations
    assert (call.execution_status, call.retrieval_status, call.cached) == ("success", "records_found", True)
    assert len(rows) == 631 and all(set(r) == ROW_KEYS for r in rows)
    assert [(r["dbd"].casefold(), r["group_id"]) for r in rows] == sorted((r["dbd"].casefold(), r["group_id"])
                                                                          for r in rows)
    by_z = sorted(rows, key=lambda r: -abs(r["z"] or 0))
    assert [r["group_id"] for r in rows] != [r["group_id"] for r in by_z]           # never ordered by z
    by_id = {r["group_id"]: r for r in rows}
    assert by_id["G035"]["members"] == [{"tf": t, "mapping": "own"} for t in ("CEBPA", "CEBPB", "CEBPE")]
    assert [m["tf"] for m in by_id["G142"]["members"]] == ["CEBPD"]
    assert [m["tf"] for m in by_id["G143"]["members"]] == ["CEBPG"]
    assert {by_id[g]["paralog_stem"] for g in ("G035", "G142", "G143")} == {"CEBP"}
    assert by_id["G035"]["binds_more"] == "alt" and round(by_id["G035"]["z"], 2) == 22.81
    passing = [r for r in rows if r["passes_gate"]]
    items = [graph.evidence[e] for e in call.evidence_ids]
    assert len(passing) == 182 and {e.data["group_id"] for e in items} == {r["group_id"] for r in passing}
    raw = json.loads((tmp_path / "run" / call.raw_result_path).read_text())
    models = {m["model"]: m for m in raw["models"]}
    for ev in items:
        row = by_id[ev.data["group_id"]]
        assert ev.evidence_class == "prediction" and ev.origin == "tool" and ev.context is None
        assert ev.direction == "increases" and ev.allele in (SORT1.variant.ref, SORT1.variant.alt)
        assert ev.independence_group == f"QBIC:{raw['provenance']['settings_hash']}:{row['group_id']}"
        side = [models[m] for m in ev.data["models"]]          # the gate-passing models this item reports
        assert all(m["passes_gate"] and m["group_id"] == row["group_id"] and allele(SORT1, m) == ev.allele
                   for m in side)
        assert ev.about_tfs == sorted({tf for m in side for tf in m["maps_to"]}) and set(ev.data["mapping"]) == \
            set(ev.about_tfs)
        if not ev.data["discordant"]:                          # one item per group: the row's best model
            assert (ev.data["best_model"], ev.data["z"], ev.allele) == (row["best_model"], row["z"],
                                                                        allele(SORT1, row))
    g035 = next(e for e in items if e.data["group_id"] == "G035")
    assert g035.about_tfs == ["CEBPA", "CEBPB", "CEBPE"] and g035.allele == "T"
    assert len(raw["models"]) == 997 and raw["sequences"]["ref"][10] == "G"


def allele(case: Case, row: dict) -> str:
    """The base a row's (or a model's) binds_more names."""
    return case.variant.alt if row["binds_more"] == "alt" else case.variant.ref


@pytest.mark.parametrize("case, group, tf, own_allele", [(DEV, "G049", "SPI1", "T"), (SORT1, "G038", "HNF1A", "T")])
def test_a_group_whose_gate_passing_models_disagree_reports_each_allele(runner, case, group, tf, own_allele):
    """Review finding 1: at rs1427407 SPIB's model (z +21) predicts more binding to G while SPI1's own model (z -14.1)
    predicts T; at rs12740374 HMBOX1's model predicts G and HNF1A's own model T. The group's Evidence used to give
    every member the best model's allele, hiding the TF's own prediction."""
    graph = ClaimGraph(case)
    call = run(runner, graph, "qbic_inventory")
    items = [graph.evidence[e] for e in call.evidence_ids if graph.evidence[e].data["group_id"] == group]
    assert sorted(e.allele for e in items) == sorted([case.variant.ref, case.variant.alt])
    assert all(e.data["discordant"] for e in items) and len({e.independence_group for e in items}) == 1
    own = next(e for e in items if e.allele == own_allele)
    assert tf in own.about_tfs and own.data["mapping"][tf] == "own"           # the TF's own model, its own allele
    row = next(r for r in inventory_rows(graph) if r["group_id"] == group)
    assert graph.evidence[row["evidence_id"]].allele == allele(case, row)       # the row joins its best model's item
    other = case.variant.ref if own_allele == case.variant.alt else case.variant.alt
    binds_other = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label=f"chr{case.variant.chrom}:"
                                                                 f"{case.variant.pos}")], relation="alters_binding",
                                             objects=[EntityRef(kind="tf", label=tf)], direction="increases",
                                             effect_allele=other), "coordinator")
    with pytest.raises(GraphRefusal, match="opposite"):                         # its own prediction never supports it
        graph.link(binds_other, own.evidence_id, "supports", "computational_investigator", f"{tf} prediction")
    assert graph.link(binds_other, own.evidence_id, "contradicts", "critic",
                      f"{tf}'s own model predicts more binding to {own_allele}").strength == "indirect"


def test_every_gate_passing_model_is_reported_with_its_allele_for_exactly_the_tfs_it_maps_to(v9_cfg):
    """The invariant behind finding 1, over the gold plumbing case and the development case: no gate-passing model's
    prediction is hidden, and no item names a TF that none of its models (own or CIS-BP-mapped) is mapped to."""
    reader = QbicReader(v9_cfg)
    for case in (SORT1, DEV):
        scores = reader.scores(case.variant)
        table = {m["model"]: m for m in reader.model_table(scores)}
        sides = reader.gate_sides(scores)
        items = [e for r in reader.inventory(scores) if r["passes_gate"]
                 for e in inventory_evidence(r, sides[r["group_id"]], case.variant, reader.settings_hash,
                                             reader.gate(scores).p_threshold)]
        for m in (m for m in table.values() if m["passes_gate"]):
            assert any(e.data["group_id"] == m["group_id"] and e.allele == allele(case, m)
                       and set(m["maps_to"]) <= set(e.about_tfs) for e in items), m["model"]
        for e in items:
            assert all(any(tf in table[m]["maps_to"] and allele(case, table[m]) == e.allele for m in e.data["models"])
                       for tf in e.about_tfs)
        assert any(len(s) > 1 for s in sides.values())


def test_development_case_has_322_gate_passing_groups(runner):
    graph = ClaimGraph(DEV)
    call = run(runner, graph, "qbic_inventory")
    groups = [graph.evidence[e].data["group_id"] for e in call.evidence_ids]
    assert len(call.observations) == 631 and len(set(groups)) == 322
    assert sum(r["passes_gate"] for r in call.observations) == 322
    split = {g for g in groups if groups.count(g) == 2}             # discordant groups: one item per allele
    assert len(groups) == 322 + len(split) and "G049" in split and max(groups.count(g) for g in groups) == 2


def test_inventory_rows_join_evidence_ids_on_the_group(runner):
    graph = ClaimGraph(DEV)
    assert inventory_rows(graph) == []
    call = run(runner, graph, "qbic_inventory")
    rows = inventory_rows(graph)
    assert [r["group_id"] for r in rows] == [r["group_id"] for r in call.observations]
    for row in rows:
        if row["passes_gate"]:
            joined = graph.evidence[row["evidence_id"]]
            assert joined.data["group_id"] == row["group_id"] and joined.allele == allele(DEV, row)
        else:
            assert row["evidence_id"] is None
    unjoined = set(call.evidence_ids) - {r["evidence_id"] for r in rows}
    assert unjoined and all(graph.evidence[e].data["discordant"] for e in unjoined)   # the other allele's items


def test_an_uncached_variant_is_a_cache_miss_with_no_evidence_and_no_network(runner):
    graph = ClaimGraph(UNCACHED)
    for tool, params in (("qbic_inventory", {}), ("qbic_tf_detail", {"tf": "CEBPA"})):
        call = run(runner, graph, tool, **params)
        assert call.execution_status == "cache_miss" and "precompute required" in call.message
        assert call.evidence_ids == []
    assert graph.evidence == {} and runner.http.requests_made == 0


def test_tf_detail_treats_own_and_mapped_models_alike_and_shows_site_strength(runner, tmp_path):
    graph = ClaimGraph(SORT1)
    cebpa = run(runner, graph, "qbic_tf_detail", tf="cebpa")
    models = [o for o in cebpa.observations if o["record"] == "model"]
    assert [m["model"] for m in models] == sorted(m["model"] for m in models)          # model id, never z
    assert {m["mapping"]["CEBPA"] for m in models} == {"own", "cisbp"}
    assert all({"ref", "alt", "k"} <= set(m["site_strength"]) for m in models)
    assert (tmp_path / "run" / "cache" / "qbic_site_strength.json").exists()
    for eid in cebpa.evidence_ids:
        ev = graph.evidence[eid]
        model = next(m for m in models if m["model"] == ev.data["model"])
        assert ev.about_tfs == model["maps_to"] and "CEBPA" in ev.about_tfs and model["passes_gate"]
    cebpb = run(runner, graph, "qbic_tf_detail", tf="CEBPB")
    shared = set(cebpa.evidence_ids) & set(cebpb.evidence_ids)
    assert shared                                   # the same model's prediction is one Evidence item
    group = run(runner, graph, "qbic_tf_detail", group="g035")
    assert {o["model"] for o in group.observations if o["record"] == "model"} == {m["model"] for m in models}


def test_tf_detail_without_a_model_or_a_name_creates_no_evidence(runner):
    graph = ClaimGraph(SORT1)
    outside = run(runner, graph, "qbic_tf_detail", tf="EP300")
    assert (outside.execution_status, outside.retrieval_status) == ("success", "no_records_found")
    unknown = run(runner, graph, "qbic_tf_detail", tf="NOT-A-GENE-9")
    both = run(runner, graph, "qbic_tf_detail", tf="CEBPA", group="G035")
    neither = run(runner, graph, "qbic_tf_detail")
    assert [c.execution_status for c in (unknown, both, neither)] == ["not_applicable"] * 3
    assert (both.charged_to, neither.charged_to) == ("none", "none")      # one_of: refused before it runs, free
    assert "exactly one of tf, group" in both.message
    assert runner.budget(graph).tool_calls_used == 2 and graph.evidence == {}


def _gate_decisions(case: Case, evidence) -> tuple:
    """What the graph decides for a CEBPA binding claim linked to this evidence: the link and the assessments."""
    graph = ClaimGraph(case)
    call = graph.record_tool_call(ToolCall(tool_call_id=graph.reserve_tool_call_id(), tool_name="qbic_inventory",
                                           execution_status="success", retrieval_status="records_found",
                                           requested_by="code", charged_to="code"), [evidence])
    claim = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label="chr1:109274968")],
                                       relation="alters_binding", objects=[EntityRef(kind="tf", label="CEBPA")],
                                       direction="increases", effect_allele="T"), "coordinator")
    link = graph.link(claim, call.evidence_ids[0], "supports", "computational_investigator",
                      "QBiC-SELEX predicts more CEBPA binding to T")
    try:
        graph.assess(claim, "supported_in_scope", "a prediction", "critic", graph.claims[claim].version)
        refused = None
    except GraphRefusal as e:
        refused = e.reason
    graph.assess(claim, "unresolved", "prediction only", "critic", graph.claims[claim].version)
    return (link.stance, link.applicability, link.code_applicability, link.strength, refused,
            graph.display_status(claim))


def test_flipping_a_model_from_own_to_mapped_changes_no_field_the_graph_reads(v9_cfg):
    reader = QbicReader(v9_cfg)
    reg = reader.registry
    model = reg.own_model["CEBPA"]
    flipped = QbicReader(v9_cfg, registry=dataclasses.replace(
        reg, own_model={tf: m for tf, m in reg.own_model.items() if tf != "CEBPA"},
        mapped_models={**reg.mapped_models, "CEBPA": [*reg.mapped_models.get("CEBPA", []), model]}))
    scores = reader.scores(SORT1.variant)
    p = reader.gate(scores).p_threshold
    rows = {r["group_id"]: r for r in reader.inventory(scores)}
    other = {r["group_id"]: r for r in flipped.inventory(scores)}
    sides, other_sides = reader.gate_sides(scores), flipped.gate_sides(scores)
    assert {m["tf"]: m["mapping"] for m in other["G035"]["members"]}["CEBPA"] == "cisbp"
    for gid, row in rows.items():
        if not row["passes_gate"]:
            continue
        own_items = inventory_evidence(row, sides[gid], SORT1.variant, reader.settings_hash, p)
        mapped_items = inventory_evidence(other[gid], other_sides[gid], SORT1.variant, reader.settings_hash, p)
        assert len(own_items) == len(mapped_items)
        for own, mapped in zip(own_items, mapped_items, strict=True):
            assert own.model_dump(exclude={"data"}) == mapped.model_dump(exclude={"data"})
            assert {k: x for k, x in own.data.items() if k != "mapping"} == \
                {k: x for k, x in mapped.data.items() if k != "mapping"}
    [own] = inventory_evidence(rows["G035"], sides["G035"], SORT1.variant, reader.settings_hash, p)
    [mapped] = inventory_evidence(other["G035"], other_sides["G035"], SORT1.variant, reader.settings_hash, p)
    assert (own.data["mapping"]["CEBPA"], mapped.data["mapping"]["CEBPA"]) == ("own", "cisbp")
    decisions = _gate_decisions(SORT1, own)
    assert decisions == _gate_decisions(SORT1, mapped)
    stance, _, code_applicability, strength, refused, display = decisions
    assert (stance, code_applicability, strength, display) == ("supports", "exact", "indirect", "predicted")
    assert refused is not None                     # a prediction alone never makes a binding claim supported


def test_reference_check_reads_the_cached_21mer(v9_cfg):
    reader = QbicReader(v9_cfg)
    assert reader.reference_check(SORT1.variant)["status"] == "verified"
    wrong = reader.reference_check(Variant(chrom="1", pos=109274968, ref="T", alt="G"))
    assert (wrong["status"], wrong["genome_base"]) == ("mismatch", "G")
    assert reader.reference_check(Variant(chrom="1", pos=1000, ref="A", alt="C"))["status"] == "unavailable"


def test_paralog_stems_join_paralog_groups_and_ignore_serial_roots(v9_cfg):
    stems = paralog_stems(v9_cfg)
    assert stems["G035"] == stems["G142"] == stems["G143"] == "CEBP"
    assert "ZNF" not in set(stems.values()) and "ZBTB" not in set(stems.values())
    assert symbol_stems(["SHOX", "SHOX2", "EOMES", "MYC", "MYCN"]) == {
        "SHOX": "SHOX", "SHOX2": "SHOX", "EOMES": "EOMES", "MYC": "MYC", "MYCN": "MYC"}


def test_the_database_is_opened_read_only(v9_cfg, monkeypatch):
    opened: list[str] = []
    real = sqlite3.connect

    def spy(target, *args, **kwargs):
        opened.append(str(target))
        return real(target, *args, **kwargs)

    monkeypatch.setattr(sqlite3, "connect", spy)
    QbicReader(v9_cfg).scores(DEV.variant)
    assert opened and all(t.endswith("?mode=ro") and t.startswith("file:") for t in opened)
    assert v9_cfg.path("cache", "db") == REPO / "cache" / "qbic.sqlite"
