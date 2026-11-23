"""collect_facts (SPEC 6 step 2) and inventory_rows (contract C2), offline on the saved caches.

The development case rs1427407 runs end to end; TERT C228T (a gold case) appears only to check the somatic route's
plumbing, and an uncached position checks that every step is recorded when nothing is available.
"""

import json
from pathlib import Path

import pytest

from variant2mechanism.v9.adapters import collect_facts, inventory_rows
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef
from variant2mechanism.v9.http9 import Http9
from variant2mechanism.v9.schemas import Case, ToolRequest, Variant
from variant2mechanism.v9.tools import ToolLimits, ToolRunner

pytestmark = pytest.mark.data

STEPS = ["variant_annotation", "ccre_overlap", "qbic_inventory"]
DEV = Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"),
           origin="germline")
CLEAN = Case(case_id="REQ-CLEAN-DEV", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G"), origin="germline")
TERT = Case(case_id="DEV-PLUMBING-2", variant=Variant(chrom="5", pos=1295113, ref="G", alt="A"), origin="somatic")
NOWHERE = Case(case_id="DEV-3", variant=Variant(chrom="2", pos=1000000, ref="A", alt="C"))


def cache_only(v9_cfg, folder: Path, limits: ToolLimits | None = None) -> ToolRunner:
    return ToolRunner(config=v9_cfg, mode="cache_only", http=Http9.from_config(v9_cfg, offline=True),
                      run_dir=folder, limits=limits, clock=lambda: "T0")


def test_the_development_case_collects_every_fact_as_code(v9_cfg, tmp_path, force_cache_miss):
    runner = cache_only(v9_cfg, tmp_path / "run")
    force_cache_miss(runner.http, "gtexportal.org/")
    graph = ClaimGraph(DEV)
    calls = collect_facts(DEV, graph, runner)
    assert [c.tool_name for c in calls] == [*STEPS, "gtex_eqtl"]
    assert all(c.requested_by == "code" and c.charged_to == "code" for c in calls)
    assert [c.execution_status for c in calls] == ["success", "success", "success", "cache_miss"]
    assert calls[-1].evidence_ids == []                # this fixture explicitly has no GTEx response
    budget = runner.budget(graph)
    assert (budget.tool_calls_used, budget.code_tool_calls) == (0, 4)
    event = graph.events[-1]
    assert (event.action, event.role, event.target_ids) == ("collect_facts", "code", [c.tool_call_id for c in calls])
    rows = inventory_rows(graph)
    assert len(rows) == 631 and sum(r["evidence_id"] is not None for r in rows) == 322
    assert graph.variant_aliases == {}                 # the supplied rsID is already the case's own
    [element] = [o["accession"] for o in calls[1].observations if o["record"] == "element"]
    assert graph.variant_elements == {element: calls[1].tool_call_id} and event.details["elements"] == [element]
    assert runner.http.requests_made == 0


def test_a_coordinates_only_case_gets_dbsnps_exact_rsid_and_its_element(v9_cfg, tmp_path):
    """Cross-notes C2-9 and C2-10, and review finding 10: the rsID dbSNP gives these exact coordinates and alleles is
    recorded as the case variant's own (the request is never changed), so GWAS is searched by it and a paper's "the
    enhancer containing rs1427407" names the cCRE that fact collection found."""
    runner = cache_only(v9_cfg, tmp_path / "run")
    graph = ClaimGraph(CLEAN)
    annotation, overlap, *_ = collect_facts(CLEAN, graph, runner)
    assert graph.variant_aliases == {"rs1427407": annotation.tool_call_id}
    assert graph.case.variant.rsid is None and CLEAN.variant.rsid is None
    [element] = graph.variant_elements
    assert graph.variant_elements[element] == overlap.tool_call_id
    gwas = runner.run(ToolRequest(tool="gwas_associations"), graph.case, graph, "computational_investigator")
    assert gwas.retrieval_status == "records_found" and len(gwas.evidence_ids) == 25 and "rs1427407" in gwas.message
    claim = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="element", label=element, canonical_id=element)],
                                       relation="overlaps", objects=[EntityRef(kind="variant", label="rs1427407")]),
                            "coordinator")
    assert graph.claims[claim].object_ids == [graph.variant_entity()]     # the alias names the case variant
    overlap_item = next(e for e in overlap.evidence_ids if graph.evidence[e].about_elements == [element])
    assert graph.link(claim, overlap_item, "supports", "computational_investigator", "the registry overlap").stance \
        == "supports"


class _VepSession:
    """A fake Ensembl and GWAS Catalog: VEP answers with one record whose co-located rsIDs are given, the overlap
    endpoint with no genes, the Catalog with an empty page; every URL asked is kept."""

    def __init__(self, colocated: list[dict]):
        self.colocated, self.urls = colocated, []

    def request(self, method, url, json=None, timeout=None, headers=None):
        self.urls.append(url)
        if "/vep/" in url:
            body = [{"allele_string": "T/A", "start": 60490908, "end": 60490908, "strand": 1,
                     "most_severe_consequence": "intron_variant", "colocated_variants": self.colocated}]
        elif "/overlap/" in url:
            body = []
        elif "/gwas/" in url:
            body = {"_embedded": {"associations": []}, "page": {"totalElements": 0}, "_links": {}}
        else:
            return _Response(404, {"error": "not found"})
        return _Response(200, body)


class _Response:
    def __init__(self, status: int, body):
        self.status_code, self._body, self.text, self.headers = status, body, json.dumps(body), {}

    def json(self):
        return self._body


def test_a_co_located_rsid_of_another_allele_never_names_the_case_variant(v9_cfg, tmp_path):
    """Review finding 10: gwas_associations took the first rsID VEP co-locates with the position, with no allele
    check, so a T>A case at rs1427407's position (T/C/G) would have received rs1427407's associations."""
    t_to_a = Case(case_id="REQ-OTHER-ALLELE", variant=Variant(chrom="2", pos=60490908, ref="T", alt="A"))
    site = {"start": 60490908, "end": 60490908, "strand": 1, "seq_region_name": "2"}
    for name, colocated, alias in (("another allele", [{"id": "rs1427407", "allele_string": "T/C/G", **site}], None),
                                   ("this allele", [{"id": "rs1427407", "allele_string": "T/C/G", **site},
                                                    {"id": "rs999", "allele_string": "T/A/C", **site}], "rs999")):
        session = _VepSession(colocated)
        runner = ToolRunner(config=v9_cfg, mode="live", run_dir=tmp_path / name / "run", clock=lambda: "T0",
                            http=Http9(tmp_path / name / "http", offline=False, session=session, sleep=lambda s: None))
        graph = ClaimGraph(t_to_a)
        annotation = collect_facts(t_to_a, graph, runner)[0]
        variant = next(o for o in annotation.observations if o["record"] == "variant")
        assert "rs1427407" in variant["rsids"] and "rs1427407" not in variant["exact_rsids"]
        assert graph.variant_aliases == ({alias: annotation.tool_call_id} if alias else {})
        gwas = runner.run(ToolRequest(tool="gwas_associations"), graph.case, graph, "computational_investigator")
        if alias is None:
            assert gwas.execution_status == "not_applicable"
        assert not any("rs_id=rs1427407" in url for url in session.urls)
        assert any(f"rs_id={alias}" in url for url in session.urls) == bool(alias)


def test_an_rsid_that_conflicts_with_the_supplied_one_is_noted_never_recorded(v9_cfg, tmp_path):
    misnamed = Case(case_id="REQ-MISNAMED", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs7"))
    graph = ClaimGraph(misnamed)
    collect_facts(misnamed, graph, cache_only(v9_cfg, tmp_path / "run"))
    event = graph.events[-1]
    assert graph.variant_aliases == {} and graph.case.variant.rsid == "rs7"
    assert event.action == "collect_facts" and any(x.startswith("rs1427407:") and "rs7" in x
                                                   for x in event.details["refused"])


def test_a_somatic_case_asks_civic_by_the_genes_vep_names(v9_cfg, tmp_path, force_cache_miss):
    graph = ClaimGraph(TERT)
    offline = cache_only(v9_cfg, tmp_path / "run")
    force_cache_miss(offline.http, "civicdb.org/api/graphql")
    calls = collect_facts(TERT, graph, offline)
    assert [c.tool_name for c in calls] == [*STEPS, "civic_lookup"]
    assert "TERT" in calls[-1].query_parameters["genes"]
    assert calls[-1].execution_status == "cache_miss" and calls[-1].evidence_ids == []
    assert calls[0].execution_status == "success" and calls[2].execution_status == "success"


def test_an_unknown_origin_takes_the_germline_route(v9_cfg, tmp_path):
    case = DEV.model_copy(update={"origin": "unknown", "case_id": "DEV-4"})
    calls = collect_facts(case, ClaimGraph(case), cache_only(v9_cfg, tmp_path / "run"))
    assert calls[-1].tool_name == "gtex_eqtl"


def test_nothing_available_is_recorded_step_by_step_and_never_raises(v9_cfg, tmp_path):
    runner = cache_only(v9_cfg, tmp_path / "run")
    graph = ClaimGraph(NOWHERE)
    calls = collect_facts(NOWHERE, graph, runner)
    assert [c.tool_name for c in calls] == [*STEPS, "gtex_eqtl"]
    assert [(c.execution_status, c.retrieval_status) for c in calls] == [
        ("cache_miss", "unknown"), ("success", "no_records_found"), ("cache_miss", "unknown"),
        ("cache_miss", "unknown")]
    assert graph.evidence == {} and runner.http.requests_made == 0
    assert inventory_rows(graph) == []


def test_a_refused_step_is_still_a_recorded_call(v9_cfg, tmp_path):
    runner = cache_only(v9_cfg, tmp_path / "run", ToolLimits(max_code_calls=2))
    graph = ClaimGraph(NOWHERE)
    calls = collect_facts(NOWHERE, graph, runner)
    assert len(calls) == 4 and all(c.tool_call_id in graph.tool_calls for c in calls)
    assert [c.charged_to for c in calls] == ["code", "code", "none", "none"]
    assert "budget exhausted" in calls[2].message
