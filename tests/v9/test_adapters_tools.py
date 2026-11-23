"""The context and association adapters against the saved HTTP responses (offline, through the isolated cache copy)
and local data, plus fake sessions for the live-only paths (the v9 Open Targets query, CIViC, SCREEN online).

rs12740374 appears only to test plumbing on its saved responses (it is the variant with the fullest cache); the
development case rs1427407 is used where its responses exist. Assertions are about statuses, provenance and the
evidence contract, never about which mechanism is right.
"""

import json
import re
from pathlib import Path

import pytest

from variant2mechanism.v9.adapters import CIVIC, SCREEN_API
from variant2mechanism.v9.context_match import scope_from_label
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef
from variant2mechanism.v9.http9 import Http9
from variant2mechanism.v9.schemas import Case, ToolCall, ToolRequest, Variant
from variant2mechanism.v9.tools import ToolRunner

pytestmark = pytest.mark.data

FIXTURES = Path(__file__).parent / "fixtures" / "adapters"
SORT1 = Variant(chrom="1", pos=109274968, ref="G", alt="T", rsid="rs12740374")
DEV = Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407")
HEP3B = scope_from_label("Hep3B")


def case(variant: Variant, context=(), origin="germline", disease=()) -> Case:
    return Case(case_id="DEV-PLUMBING", variant=variant, origin=origin, supplied_context=list(context),
                supplied_disease=list(disease))


def cache_only(v9_cfg, folder: Path) -> ToolRunner:
    """A cache-only runner whose run folder belongs to one graph (raw/T#.json is never overwritten)."""
    return ToolRunner(config=v9_cfg, mode="cache_only", http=Http9.from_config(v9_cfg, offline=True),
                      run_dir=folder, clock=lambda: "T0")


@pytest.fixture
def offline(v9_cfg, tmp_path) -> ToolRunner:
    return cache_only(v9_cfg, tmp_path / "run")


def live(v9_cfg, folder: Path, session) -> ToolRunner:
    """A live runner on a fake provider, with its own HTTP cache and run folder under `folder`."""
    http = Http9(folder / "http", offline=False, session=session, sleep=lambda s: None)
    return ToolRunner(config=v9_cfg, mode="live", http=http, run_dir=folder / "run", clock=lambda: "T0")


def run(runner: ToolRunner, graph: ClaimGraph, tool: str, **params) -> ToolCall:
    return runner.run(ToolRequest(tool=tool, params=params), graph.case, graph, "computational_investigator")


def evidence(graph: ClaimGraph, call: ToolCall):
    return [graph.evidence[e] for e in call.evidence_ids]


class Response:
    def __init__(self, status: int, body):
        self.status_code, self._body, self.text, self.headers = status, body, json.dumps(body), {}

    def json(self):
        return self._body


class Session:
    """A fake provider: `answer(method, url, body)` returns (status, body); every request is recorded."""

    def __init__(self, answer):
        self.answer, self.calls = answer, []

    def request(self, method, url, json=None, timeout=None, headers=None):
        self.calls.append({"method": method, "url": url, "json": json, "headers": dict(headers or {})})
        return Response(*self.answer(method, url, json))


def test_variant_annotation_reports_consequences_and_the_reference_check_without_clinical_fields(offline, tmp_path):
    graph = ClaimGraph(case(SORT1))
    call = run(offline, graph, "variant_annotation")
    assert (call.execution_status, call.retrieval_status) == ("success", "records_found")
    check = next(o for o in call.observations if o["record"] == "reference_check")
    assert check["status"] == "verified" and {c["source"] for c in check["checks"]} == {
        "qbic_21mer", "hg38_fasta", "ensembl_vep"}
    ev = evidence(graph, call)
    assert ev and all(e.evidence_class == "annotation" and e.origin == "tool" for e in ev)
    assert "CELSR2" in {g for e in ev for g in e.about_genes}
    assert any(o["record"] == "nearby_gene" for o in call.observations)
    text = json.dumps(call.observations) + (tmp_path / "run" / call.raw_result_path).read_text()
    for leak in ("pubmed", "clin_sig", "COSV", "CR105220", "conservation", "phenotype_or_disease"):
        assert leak not in text


def test_an_uncached_variant_is_a_cache_miss_with_no_evidence_and_nothing_sent(offline):
    # One base from rs1427407, which no run asks about: ChIP-seq lookups are saved by position, and a live run on
    # rs1427407 (a development variant of the reader) saves the position this test used to take for unsaved.
    graph = ClaimGraph(case(Variant(chrom="2", pos=60490909, ref="T", alt="C")))
    for tool in ("variant_annotation", "gtex_eqtl", "chip_occupancy", "credible_sets_l2g"):
        call = run(offline, graph, tool)
        assert call.execution_status == "cache_miss" and call.evidence_ids == [], tool
        assert "nothing was sent" in call.message
    assert graph.evidence == {} and offline.http.requests_made == 0


def test_hep3b_context_keeps_hepg2_evidence_as_a_proxy(offline):
    graph = ClaimGraph(case(SORT1, context=[HEP3B]))
    ccre = run(offline, graph, "ccre_overlap")
    classes = [o for o in ccre.observations if o["record"] == "biosample_class" and o["match"]]
    assert {o["biosample"]: o["match"] for o in classes} == {"HepG2": "proxy", "hepatocyte": "proxy",
                                                             "right lobe of liver": "proxy"}
    hepg2_class = next(e for e in evidence(graph, ccre) if e.context and e.context.biosample == "HepG2")
    chip = run(offline, graph, "chip_occupancy", tf="CEBPB", biosample="Hep3B")
    hepg2_peak = [e for e in evidence(graph, chip) if e.context.biosample == "HepG2"]
    assert len(hepg2_peak) == 1 and hepg2_peak[0].result_kind == "effect"
    assert {o["match"] for o in chip.observations if o["record"] == "experiment" and o["biosample"] == "MCF-7"} \
        == {None}                                   # outside the requested scope: listed, not evidence
    element = EntityRef(kind="element", label="EH38E1374646", canonical_id="EH38E1374646")
    occupies = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="tf", label="CEBPB")], relation="occupies",
                                          objects=[element], context=HEP3B), "coordinator")
    link = graph.link(occupies, hepg2_peak[0].evidence_id, "supports", "computational_investigator",
                      "a CEBPB peak in HepG2, a proxy for Hep3B", applicability="exact")
    assert (link.code_applicability, link.applicability, link.corrected) == ("proxy", "proxy", True)
    overlaps = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label="chr1:109274968")],
                                          relation="overlaps", objects=[element], context=HEP3B), "coordinator")
    assert graph.link(overlaps, hepg2_class.evidence_id, "supports", "computational_investigator",
                      "dELS in HepG2").code_applicability == "proxy"


def test_an_encode_assay_without_an_aggregator_peak_is_listed_never_a_measured_null(offline, v9_cfg, tmp_path):
    """Review finding 11: a locus query cannot show that Factorbook or ReMap processed an experiment with no peak
    there (and they disagree for experiments both process), so no ChIP null is Evidence; the assays are listed in the
    requested or supplied scope and only counted elsewhere (CTCF has about 166 such biosamples here)."""
    graph = ClaimGraph(case(SORT1))
    k562 = run(offline, graph, "chip_occupancy", tf="CEBPB", biosample="K562")
    assert (k562.retrieval_status, k562.evidence_ids) == ("no_records_found", [])
    listed = [o for o in k562.observations if o["record"] == "assayed_no_peak"]
    assert [(o["biosample"], len(o["experiments"]), o["match"]) for o in listed] == [("K562", 3, "exact")]
    assert any("not Evidence" in x for x in k562.coverage.limitations)
    ctcf = run(offline, graph, "chip_occupancy", tf="CTCF")                      # no biosample, none supplied
    assert not [o for o in ctcf.observations if o["record"] == "assayed_no_peak"]
    [elsewhere] = [o for o in ctcf.observations if o["record"] == "assayed_no_peak_elsewhere"]
    assert elsewhere["biosamples"] > 100 and len(elsewhere["examples"]) <= 8
    assert all(e.result_kind == "effect" and e.about_tfs == ["CTCF"] for e in evidence(graph, ctcf))
    supplied = ClaimGraph(case(SORT1, context=[scope_from_label("K562")]))
    in_context = run(cache_only(v9_cfg, tmp_path / "supplied"), supplied, "chip_occupancy", tf="CEBPB")
    assert [o["biosample"] for o in in_context.observations if o["record"] == "assayed_no_peak"] == ["K562"]
    assert not any(e.result_kind != "effect" for g in (graph, supplied) for e in g.evidence.values())


def test_chip_survey_lists_factors_in_symbol_order_without_evidence(offline):
    graph = ClaimGraph(case(SORT1))
    call = run(offline, graph, "chip_occupancy")
    factors = [o["tf"] for o in call.observations]
    assert call.retrieval_status == "records_found" and call.evidence_ids == [] and factors == sorted(factors)
    assert {"CEBPA", "CEBPB", "HNF4A"} <= set(factors)


def test_gtex_eqtls_name_the_alt_allele_and_share_groups_with_screen_links(offline, v9_cfg, tmp_path, force_cache_miss):
    graph = ClaimGraph(case(SORT1))
    gtex = run(offline, graph, "gtex_eqtl")
    ev = evidence(graph, gtex)
    assert len(ev) == 39 and all(e.allele == "T" and e.evidence_class == "association" for e in ev)
    sort1 = next(e for e in ev if e.about_genes == ["SORT1"] and e.data["tissue"] == "Liver")
    assert sort1.direction == "increases" and round(sort1.data["nes"], 2) == 1.27 and sort1.context.tissue == "liver"
    assert all(("increases" if e.data["nes"] > 0 else "decreases") == e.direction for e in ev)
    ccre = run(offline, graph, "ccre_overlap")
    screen_groups = {e.independence_group for e in evidence(graph, ccre) if e.evidence_class == "association"}
    assert {e.independence_group for e in ev} & screen_groups      # one GTEx v8 result, not two sources
    liver_only = run(offline, graph, "gtex_eqtl", gene="SORT1", tissue="Liver")
    assert liver_only.evidence_ids == [sort1.evidence_id]
    absent = cache_only(v9_cfg, tmp_path / "dev")
    force_cache_miss(absent.http, "gtexportal.org/")
    missing = run(absent, ClaimGraph(case(DEV)), "gtex_eqtl")
    assert missing.execution_status == "cache_miss" and missing.evidence_ids == []


def test_gwas_rows_carry_the_catalog_effect_allele_and_pages_are_read_up_to_the_cache(offline, v9_cfg, tmp_path, force_cache_miss):
    force_cache_miss(offline.http, "page=1")
    graph = ClaimGraph(case(SORT1))
    call = run(offline, graph, "gwas_associations")
    assert call.retrieval_status == "incomplete" and "100 of 698" in call.coverage.assessed_scope
    ev = evidence(graph, call)
    assert len(ev) == 100 and {e.allele for e in ev} == {"G", "T", None}
    assert all(e.direction == "unspecified" for e in ev if e.allele is None)
    ldl = run(offline, graph, "gwas_associations", trait="LDL cholesterol")
    whole = re.compile(r"(?<![a-z0-9])ldl cholesterol(?![a-z0-9])")
    assert ldl.evidence_ids
    assert all(any(whole.search(t.casefold()) for t in e.about_traits) for e in evidence(graph, ldl))
    vldl_only = {e.evidence_id for e in ev if not any(whole.search(t.casefold()) for t in e.about_traits)
                 and any("vldl cholesterol" in t.casefold() for t in e.about_traits)}
    assert not vldl_only & set(ldl.evidence_ids)          # "LDL cholesterol" never matches "VLDL cholesterol"
    dev = run(cache_only(v9_cfg, tmp_path / "dev"), ClaimGraph(case(DEV)), "gwas_associations")
    assert dev.retrieval_status == "records_found" and len(dev.evidence_ids) == 25


def test_no_records_found_creates_no_evidence(offline, v9_cfg, tmp_path):
    near_miss = case(Variant(chrom="8", pos=127401265, ref="T", alt="C", rsid="rs73706717"))
    graph = ClaimGraph(near_miss)
    gwas = run(offline, graph, "gwas_associations")
    assert (gwas.execution_status, gwas.retrieval_status, gwas.evidence_ids) == ("success", "no_records_found", [])
    assert "not a negative" in gwas.message
    no_rsid = run(cache_only(v9_cfg, tmp_path / "no_rsid"),
                  ClaimGraph(case(Variant(chrom="1", pos=109274968, ref="G", alt="T"))), "gwas_associations")
    assert no_rsid.execution_status == "not_applicable"
    outside = run(offline, graph, "qbic_tf_detail", tf="EP300")
    assert outside.retrieval_status == "no_records_found" and outside.evidence_ids == []
    assert graph.evidence == {}


def test_credible_sets_offline_use_the_cached_query_and_never_take_a_maximum(offline, force_cache_miss):
    force_cache_miss(offline.http, "graphql", body_fragment="V2MCredibleSets")
    graph = ClaimGraph(case(SORT1))
    survey = run(offline, graph, "credible_sets_l2g")
    assert survey.retrieval_status == "incomplete" and survey.evidence_ids == []
    summary = survey.observations[0]
    assert (summary["credible_sets"], summary["release"]) == (2316, "release not recorded")
    scoped = run(offline, graph, "credible_sets_l2g", trait="LDL cholesterol")
    ev = evidence(graph, scoped)
    assert ev and {e.evidence_class for e in ev} == {"statistical_inference", "precomputed_prediction"}
    whole = re.compile(r"(?<![a-z0-9])ldl cholesterol(?![a-z0-9])")
    assert all(any(whole.search(t.casefold()) for t in e.about_traits) for e in ev)
    assert "best_l2g" not in json.dumps(scoped.observations)
    for e in ev:
        if e.evidence_class == "precomputed_prediction":     # each score stays with its own credible set
            assert e.independence_group == next(x.independence_group for x in ev if x.evidence_class ==
                                                "statistical_inference" and x.data["study_id"] == e.data["study_id"])


def test_credible_sets_live_query_reads_release_pip_l2g_and_colocalisation(v9_cfg, tmp_path):
    fixture = json.loads((FIXTURES / "ot_credible_sets.json").read_text())["response"]
    session = Session(lambda method, url, body: (200, fixture))
    runner = live(v9_cfg, tmp_path / "live", session)
    graph = ClaimGraph(case(SORT1))
    call = run(runner, graph, "credible_sets_l2g", trait="Monounsaturated fatty acid levels")
    assert call.dataset_release == "Open Targets Platform 26.09 (API 26.9.0)"
    # The fixture has 148 colocalisations but returns only 3: these are useful, incomplete results.
    assert call.retrieval_status == "incomplete" and len(session.calls) == 1
    assert session.calls[0]["json"]["variables"] == {"v": "1_109274968_G_T", "ids": ["1_109274968_G_T"], "index": 0}
    ev = evidence(graph, call)
    sets = [e for e in ev if e.evidence_class == "statistical_inference" and "colocalises" not in e.observed_result]
    coloc = [e for e in ev if "colocalises" in e.observed_result]
    assert len(sets) == 1 and round(sets[0].data["pip"], 3) == 0.349
    assert {e.about_genes[0] for e in coloc} == {"PSRC1", "SORT1"} and all(e.context for e in coloc)
    assert len({e.independence_group for e in ev}) == 1
    only = run(runner, graph, "credible_sets_l2g", trait="Monounsaturated fatty acid levels", gene="SORT1")
    assert {g for e in evidence(graph, only) for g in e.about_genes} == {"SORT1"}


def test_expression_is_a_level_in_the_matching_context_never_a_threshold_call(offline, v9_cfg, tmp_path):
    graph = ClaimGraph(case(SORT1, context=[HEP3B]))
    call = run(offline, graph, "tf_expression", tf="CEBPA")
    [ev] = evidence(graph, call)
    assert (ev.evidence_class, ev.direction, ev.context.biosample) == ("expression", "unspecified", "Hep 3B2.1-7")
    assert call.observations[0]["source_context"] == "DepMap:ACH-000625"
    low = run(offline, graph, "tf_expression", tf="CEBPE")
    assert low.evidence_ids and all(e.result_kind == "effect" for e in evidence(graph, low))
    tissue = run(offline, graph, "tf_expression", tf="CEBPA", context="liver")
    assert evidence(graph, tissue)[0].context.tissue == "liver"
    unknown = run(cache_only(v9_cfg, tmp_path / "none"), ClaimGraph(case(SORT1)), "tf_expression", tf="CEBPA")
    assert unknown.retrieval_status == "no_records_found" and unknown.observations[0]["status"] == "unknown"


def test_depmap_context_reports_values_for_the_line_and_lineage(offline, v9_cfg, tmp_path):
    graph = ClaimGraph(case(SORT1, context=[HEP3B]))
    call = run(offline, graph, "depmap_context", gene="SORT1")
    values = call.observations[0]
    assert (values["line"], values["lineage"]) == ("ACH-000625", "Liver") and "line_effect" not in values
    classes = sorted(e.evidence_class for e in evidence(graph, call))
    assert classes == ["dependency_screen", "expression", "expression"]
    none = run(cache_only(v9_cfg, tmp_path / "none"), ClaimGraph(case(SORT1)), "depmap_context", gene="SORT1")
    assert none.retrieval_status == "no_records_found" and "no cell line or lineage" in none.message


def test_civic_matches_by_gene_and_variant_name(v9_cfg, tmp_path, offline, force_cache_miss):
    tert = case(Variant(chrom="5", pos=1295113, ref="G", alt="A"), origin="somatic")
    force_cache_miss(offline.http, "civicdb.org/api/graphql")
    assert run(offline, ClaimGraph(tert), "civic_lookup", genes=["TERT"]).execution_status == "cache_miss"
    canned = json.loads((FIXTURES / "civic_tert.json").read_text())
    session = Session(lambda m, url, body: (200, canned["browse"] if "Browse" in body["query"] else canned["variant"]))
    runner = live(v9_cfg, tmp_path / "live", session)
    graph = ClaimGraph(tert)
    listing = run(runner, graph, "civic_lookup", genes=["TERT"])
    assert listing.evidence_ids == [] and {o["name"] for o in listing.observations} == {"C228T", "C250T"}
    named = run(runner, graph, "civic_lookup", genes=["TERT"], variant="C228T")
    ev = evidence(graph, named)
    assert len(ev) == 3 and all(e.evidence_class == "clinical_assertion" and e.about_genes == ["TERT"] for e in ev)
    submitted = [e for e in ev if e.data["status"] == "SUBMITTED"]
    assert submitted and all("not yet accepted" in " ".join(e.limitations) for e in submitted)
    assert all(c["url"] == CIVIC for c in session.calls)


def test_screen_online_needs_a_key_and_never_records_it(v9_cfg, tmp_path, offline, monkeypatch):
    graph = ClaimGraph(case(SORT1))
    absent = run(offline, graph, "screen_online")
    assert absent.execution_status == "unavailable" and "V2M_SCREEN_API_KEY" in absent.message
    assert offline.http.requests_made == 0
    secret = "screen-key-not-real-0042"
    monkeypatch.setenv("V2M_SCREEN_API_KEY", secret)
    element = {"accession": "EH38E1374646", "chromosome": "chr1", "start": 109274793, "stop": 109275142,
               "ccre_group": "dELS", "dnase_max_zscore": 3.1, "h3k27ac_max_zscore": 2.2}
    session = Session(lambda m, url, body: (200, {"data": {"getmaxZScoresQuery": [element]}}))
    runner = live(v9_cfg, tmp_path / "live", session)
    graph = ClaimGraph(case(SORT1))              # a new run: the keyless call above would be deduplicated
    call = run(runner, graph, "screen_online")
    assert call.execution_status == "success" and len(call.evidence_ids) == 1
    assert graph.evidence[call.evidence_ids[0]].independence_group == "ENCODE-cCRE:EH38E1374646"
    assert session.calls[0]["url"] == SCREEN_API and session.calls[0]["headers"]["Authorization"] == f"Bearer {secret}"
    recorded = json.dumps([c.model_dump() for c in graph.tool_calls.values()]) + json.dumps(
        [e.model_dump() for e in graph.evidence.values()]) + json.dumps([e.model_dump() for e in graph.events])
    stored = "".join(p.read_text() for p in (tmp_path / "live" / "run" / "raw").iterdir())
    cached = "".join(p.read_text() for p in (tmp_path / "live" / "http").iterdir())
    assert secret not in recorded + stored + cached
    refused = live(v9_cfg, tmp_path / "again", Session(lambda m, url, body: (403, {"error": "request not allowed"})))
    denied = run(refused, ClaimGraph(case(SORT1)), "screen_online")
    assert denied.execution_status == "unavailable" and denied.evidence_ids == []
