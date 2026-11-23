"""What each adapter observation is about, how independent it is, and what its status claims (review round 2).

Every finding here was reproduced on the saved responses before the fix: another variant's eQTL supporting the case
variant (2), odds ratios read as text and lost (3), one measurement in two independence groups (4), a lineage median
filed as an organ (5), a palindromic effect allele taken at face value (6), raw results that changed with the clock
(7), a GraphQL error read as "no records" (8) and a scoped search with unread pages reported as "no records" (9).
Assertions are about identity, independence, allele frames and statuses, never about which mechanism is right.
"""

import json

import pytest

from variant2mechanism.v9 import http9
from variant2mechanism.v9.context_match import scope_from_label
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, GraphRefusal
from variant2mechanism.v9.schemas import Variant
from variant2mechanism.v9.tools import ToolRunner

from .test_adapters_tools import DEV, FIXTURES, HEP3B, SORT1, Session, cache_only, case, evidence, live, run

pytestmark = pytest.mark.data

ELEMENT = EntityRef(kind="element", label="EH38E1374646", canonical_id="EH38E1374646")
TERT = case(Variant(chrom="5", pos=1295113, ref="G", alt="A"), origin="somatic")
RS4784227 = Variant(chrom="16", pos=52565276, ref="C", alt="T", rsid="rs4784227")
GRAPHQL_ERROR = {"errors": [{"message": "Cannot query field 'browseVariants'"}], "data": None}


@pytest.fixture
def offline(v9_cfg, tmp_path) -> ToolRunner:
    return cache_only(v9_cfg, tmp_path / "run")


def claim(graph: ClaimGraph, subject: EntityRef, relation: str, obj: EntityRef, **fields) -> str:
    return graph.add_claim(ClaimDraft(subjects=[subject], relation=relation, objects=[obj], **fields), "coordinator")


def test_another_variants_eqtl_in_the_element_is_about_the_element_never_this_variant(offline):
    """Finding 2: cCRE EH38E1374646 carries GTEx eQTLs of chr1_109274857_G_C for PSRC1; they were association
    Evidence that a critic could take as exact, direct support for "rs12740374 is associated with PSRC1 expression"."""
    graph = ClaimGraph(case(SORT1))
    ccre = run(offline, graph, "ccre_overlap")
    eqtls = [e for e in evidence(graph, ccre) if "eQTL link" in e.observed_result]
    other = [e for e in eqtls if not e.data["case_variant"]]
    own = [e for e in eqtls if e.data["case_variant"]]
    assert len(other) == 4 and {e.data["variant"] for e in other} == {"chr1_109274857_G_C_b38"}
    assert all(e.evidence_class == "annotation" and (e.allele, e.direction) == (None, "unspecified") for e in other)
    assert all("chr1_109274857_G_C_b38" in e.observed_result and any("not of chr1:109274968" in x for x in
                                                                      e.limitations) for e in other)
    assert own and all(e.evidence_class == "association" and e.allele == "T" for e in own)
    target = other[0]
    psrc1 = EntityRef(kind="gene", label="PSRC1")
    about_variant = claim(graph, EntityRef(kind="variant", label="rs12740374"), "associated_with_expression", psrc1,
                          context=target.context)
    with pytest.raises(GraphRefusal, match="cannot support"):
        graph.link(about_variant, target.evidence_id, "supports", "computational_investigator", "an eQTL here")
    assert graph.link(about_variant, target.evidence_id, "context_only", "critic", "another variant").stance == \
        "context_only"
    about_element = claim(graph, ELEMENT, "regulates", psrc1)
    assert graph.link(about_element, target.evidence_id, "supports", "computational_investigator",
                      "an eQTL of a variant in this element").strength == "indirect"


def test_gtex_v8_names_are_current_symbols_and_share_a_group_with_screen_by_ensembl_id(offline):
    """Finding 4: GTEx v8 still calls SARS1 "SARS", so gene=SARS1 found nothing and GTEx's and SCREEN's report of the
    same result fell into two independence groups."""
    graph = ClaimGraph(case(SORT1))
    found = []
    for name in ("SARS1", "SARS"):
        call = run(offline, graph, "gtex_eqtl", gene=name)
        [ev] = evidence(graph, call)
        found.append(ev.evidence_id)
        assert call.retrieval_status == "records_found" and ev.about_genes == ["SARS1"]
        assert "GTEx v8 name SARS" in ev.observed_result and "ENSG00000031698" in ev.independence_group
    assert found[0] == found[1]
    ccre = run(offline, graph, "ccre_overlap")
    screen = {e.independence_group for e in evidence(graph, ccre)
              if e.evidence_class == "association" and e.about_genes == ["SARS1"]}
    assert graph.evidence[found[0]].independence_group in screen


def test_gwas_odds_ratios_given_as_text_keep_their_effect_and_direction(v9_cfg, tmp_path):
    """Finding 3: the Catalog's v2 API gives or_value as text ("0.7883", "1.23 (Oncoarray)"); those rows lost effect
    and direction, so "C increases breast cancer risk" took support from an OR of 0.79 for C."""
    graph = ClaimGraph(case(RS4784227))
    call = run(cache_only(v9_cfg, tmp_path / "run"), graph, "gwas_associations")
    raw = json.loads((tmp_path / "run" / call.raw_result_path).read_text())
    with_or = {a["accession_id"] for a in raw["associations"] if a.get("or_value") is not None}
    by_study = {e.data["accession"]: e for e in evidence(graph, call)}
    assert with_or and all(by_study[s].data["effect"] is not None for s in with_or)
    rashkin, oncoarray = by_study["GCST90011804"], by_study["GCST004988"]
    assert (rashkin.allele, rashkin.direction, rashkin.data["effect"]) == ("C", "decreases", 0.7883)
    assert (oncoarray.allele, oncoarray.direction, oncoarray.data["effect"]) == ("T", "increases", 1.23)
    risk_of_c = claim(graph, EntityRef(kind="variant", label="rs4784227"), "associated_with_trait",
                      EntityRef(kind="phenotype", label="breast cancer"), direction="increases", effect_allele="C")
    with pytest.raises(GraphRefusal, match="opposite"):
        graph.link(risk_of_c, rashkin.evidence_id, "supports", "computational_investigator", "C is the effect allele")


def test_one_gwas_study_is_one_independence_group_in_the_catalog_and_open_targets(offline, force_cache_miss):
    """Finding 4: GCST90476419 was GWAS:GCST90476419 in the Catalog and OT:GCST90476419 in Open Targets, two
    independent supports for one measurement."""
    graph = ClaimGraph(case(SORT1))
    force_cache_miss(offline.http, "graphql", body_fragment="V2MCredibleSets")
    catalog = run(offline, graph, "gwas_associations", trait="total cholesterol")
    sets = run(offline, graph, "credible_sets_l2g", trait="total cholesterol")
    by_study = {e.data["accession"]: e.independence_group for e in evidence(graph, catalog)}
    shared = [e for e in evidence(graph, sets) if e.data.get("study_id") in by_study]
    assert shared and all(e.independence_group == by_study[e.data["study_id"]] == f"GWAS-STUDY:{e.data['study_id']}"
                          for e in shared)


def test_one_depmap_value_is_one_item_and_a_lineage_median_is_never_an_organ_or_a_line(offline):
    """Findings 4 and 5: CEBPA's TPM in Hep3B was two independent items (tf_expression and depmap_context), and the
    median over 27 liver-lineage cancer lines was filed as liver tissue, exact support for "expressed in liver"."""
    graph = ClaimGraph(case(SORT1, context=[HEP3B]))
    expression = run(offline, graph, "tf_expression", tf="CEBPA")
    depmap = run(offline, graph, "depmap_context", gene="CEBPA")
    [line] = expression.evidence_ids
    assert line in depmap.evidence_ids and len(graph.evidence) == len(depmap.evidence_ids)   # one value, one item
    medians = [e for e in evidence(graph, depmap) if e.context.biosample != "Hep 3B2.1-7"]
    assert len(medians) == 2 and {e.context.biosample_kind for e in medians} == {"cell_line"}
    assert all("lineage" in e.context.biosample and e.context.tissue == "liver" for e in medians)
    median_tpm = next(e for e in medians if e.evidence_class == "expression")
    cebpa = EntityRef(kind="tf", label="CEBPA")
    in_liver = claim(graph, cebpa, "expressed_in", EntityRef(kind="context", label="liver"),
                     context=scope_from_label("liver"))
    assert graph.link(in_liver, median_tpm.evidence_id, "supports", "computational_investigator",
                      "liver-lineage lines").code_applicability == "proxy"
    in_hep3b = claim(graph, cebpa, "expressed_in", EntityRef(kind="context", label="Hep3B"), context=HEP3B)
    assert graph.link(in_hep3b, median_tpm.evidence_id, "supports", "computational_investigator",
                      "liver-lineage lines").stance == "context_only"


def test_a_palindromic_effect_allele_is_never_placed_and_another_base_is_never_flipped(v9_cfg, tmp_path):
    """Finding 6: for a G>C variant the Catalog's effect allele C may be on either strand, so its direction is not
    placed; a base that is neither allele stays unplaced (many rsIDs are multiallelic)."""
    def row(rsid: str, allele: str) -> dict:
        return {"accession_id": "GCST1", "reported_trait": ["LDL cholesterol"], "efo_traits": [],
                "snp_allele": [{"rs_id": rsid, "effect_allele": allele}], "beta": "0.2 unit increase",
                "pvalue_mantissa": 1, "pvalue_exponent": -20, "pubmed_id": "1"}

    def page(method, url, body):
        rsid = url.split("rs_id=")[1].split("&")[0]
        allele = "C" if rsid == "rs900" else "G"
        return 200, {"_embedded": {"associations": [row(rsid, allele)]}, "page": {"totalElements": 1}, "_links": {}}

    for name, variant, why in (("palindromic", Variant(chrom="1", pos=1000, ref="G", alt="C", rsid="rs900"),
                                "reads the same on both strands"),
                               ("other base", Variant(chrom="1", pos=1000, ref="C", alt="T", rsid="rs901"),
                                "neither ref C nor alt T")):
        graph = ClaimGraph(case(variant))
        call = run(live(v9_cfg, tmp_path / name, Session(page)), graph, "gwas_associations")
        [ev] = evidence(graph, call)
        assert (ev.allele, ev.direction) == (None, "unspecified") and any(why in x for x in ev.limitations)
        assert ev.data["effect_allele"] in ("C", "G") and ev.data["effect"] == 0.2      # kept as stated, as data


def test_the_same_cache_only_call_writes_the_same_raw_bytes_whatever_the_clock(v9_cfg, tmp_path, monkeypatch):
    """Finding 7: a failed request's retrieval time was the clock's, so the same cache-only call wrote different raw
    bytes (and raw_result_hash) a second later."""
    requests = [("gtex_eqtl", {}), ("civic_lookup", {"genes": ["BCL11A"]}),
                ("credible_sets_l2g", {"trait": "fetal hemoglobin"}), ("chip_occupancy", {"tf": "GATA1"})]
    written = []
    for when in ("2026-01-01T00:00:00+00:00", "2027-06-30T12:00:00+00:00"):
        monkeypatch.setattr(http9, "_now", lambda when=when: when)
        folder = tmp_path / when[:4]
        runner, graph = cache_only(v9_cfg, folder), ClaimGraph(case(DEV))
        calls = [run(runner, graph, tool, **params) for tool, params in requests]
        assert any(c.execution_status == "cache_miss" for c in calls)
        written.append([(c.raw_result_hash, (folder / c.raw_result_path).read_bytes()) for c in calls])
    assert written[0] == written[1]


def test_a_graphql_error_inside_an_http_200_is_a_failure_never_no_records(v9_cfg, tmp_path):
    """Finding 8: {"errors": [...], "data": null} with HTTP 200 became "no CIViC variant named C228T (no record)"
    and "Open Targets: no record"; errors that come with data leave the records incomplete."""
    civic = run(live(v9_cfg, tmp_path / "civic", Session(lambda m, u, b: (200, GRAPHQL_ERROR))), ClaimGraph(TERT),
                "civic_lookup", genes=["TERT"], variant="C228T")
    assert (civic.execution_status, civic.evidence_ids) == ("error", []) and "GraphQL error" in civic.message
    sets = run(live(v9_cfg, tmp_path / "ot", Session(lambda m, u, b: (200, GRAPHQL_ERROR))), ClaimGraph(case(SORT1)),
               "credible_sets_l2g", trait="LDL cholesterol")
    assert (sets.execution_status, sets.evidence_ids) == ("error", []) and "GraphQL error" in sets.message
    fixture = json.loads((FIXTURES / "ot_credible_sets.json").read_text())["response"]
    partial = {**fixture, "errors": [{"message": "colocalisation timed out"}]}
    graph = ClaimGraph(case(SORT1))
    some = run(live(v9_cfg, tmp_path / "partial", Session(lambda m, u, b: (200, partial))), graph,
               "credible_sets_l2g", trait="Monounsaturated fatty acid levels")
    assert (some.execution_status, some.retrieval_status) == ("success", "incomplete") and some.evidence_ids
    assert any("colocalisation timed out" in x for x in some.coverage.limitations)


def test_a_scoped_search_with_unread_pages_is_incomplete_never_no_records(offline, v9_cfg, tmp_path, force_cache_miss):
    """Finding 9: rs12740374 with trait "coronary artery disease" read 100 of 698 GWAS rows, found none in scope and
    said "no record"; the same holds for credible sets and GTEx pages."""
    graph = ClaimGraph(case(SORT1))
    force_cache_miss(offline.http, "page=1")
    force_cache_miss(offline.http, "graphql", body_fragment="V2MCredibleSets")
    cad = run(offline, graph, "gwas_associations", trait="coronary artery disease")
    assert (cad.retrieval_status, cad.evidence_ids) == ("incomplete", []) and "not read" in cad.message
    sets = run(offline, graph, "credible_sets_l2g", trait="a trait no study has measured")
    assert (sets.retrieval_status, sets.evidence_ids) == ("incomplete", []) and "not read" in sets.message
    psrc1 = {"geneSymbol": "PSRC1", "gencodeId": "ENSG00000134222.16", "tissueSiteDetailId": "Liver", "nes": 0.3,
             "pValue": 1e-6}
    first_page = {"data": [psrc1], "paging_info": {"numberOfPages": 2, "page": 0}}
    gtex = run(live(v9_cfg, tmp_path / "gtex", Session(lambda m, u, b: (200, first_page))), ClaimGraph(case(SORT1)),
               "gtex_eqtl", gene="SORT1")
    assert (gtex.retrieval_status, gtex.evidence_ids) == ("incomplete", [])

    def remap_down(method, url, body):          # Factorbook and ENCODE answer with nothing; ReMap cannot be read
        if "factorbook" in url:
            return 200, {"data": {"peaksrange": {"data": []}}}
        return (200, {"@graph": []}) if "encodeproject" in url else (404, {"error": "not found"})

    chip = run(live(v9_cfg, tmp_path / "chip", Session(remap_down)), ClaimGraph(case(SORT1)), "chip_occupancy",
               tf="CEBPB")
    assert (chip.retrieval_status, chip.evidence_ids) == ("incomplete", [])
    assert any("ReMap could not be read" in x for x in chip.coverage.limitations)
