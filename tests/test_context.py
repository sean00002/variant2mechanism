"""Context tools against recorded responses in tests/fixtures/http (record with scripts/record_fixtures.py)."""

from pathlib import Path

import pandas as pd
import pytest

from variant2mechanism.context.base import SUMMARY_LIMIT, Case
from variant2mechanism.context.catalog import tool_definitions
from variant2mechanism.context.ccre import ccre_lookup
from variant2mechanism.context.chip import chip_peaks
from variant2mechanism.context.depmap import COMMON_ESSENTIAL_LINE, gene_dependency, is_common_essential
from variant2mechanism.context.ensembl import nearest_genes, variant_annotation
from variant2mechanism.context.genetics import eqtl_lookup, finemap_lookup, gene_disease, gwas_lookup
from variant2mechanism.context.http import Http
from variant2mechanism.context.literature import literature_search
from variant2mechanism.qbic.variants import Variant

FIXTURES = Path(__file__).parent / "fixtures" / "http"


@pytest.fixture
def http():
    return Http(FIXTURES, offline=True)


@pytest.fixture
def rs6983267(http):
    return Case(Variant.make("chr8", 127401060, "G", "T"), "Colorectal cancer", rsid="rs6983267", http=http)


@pytest.fixture
def tert(http):
    return Case(Variant.make("chr5", 1295113, "G", "A"), "Glioblastoma", origin="somatic", http=http)


def test_variant_formats(rs6983267):
    assert rs6983267.ensembl == "8:127401060" and rs6983267.opentargets == "8_127401060_G_T"
    assert rs6983267.gtex == "chr8_127401060_G_T_b38" and rs6983267.gnomad == "8-127401060-G-T"


def test_variant_annotation(rs6983267):
    r = variant_annotation(rs6983267)
    assert r.ok and r.kind == "computational" and "rs6983267" in r.summary and "GERP" in r.summary
    assert "enhancer" in r.summary and "WARNING" not in r.summary


def test_nearest_genes_strand_aware(rs6983267, tert):
    r = nearest_genes(rs6983267)
    first = r.full[0]
    assert first["gene"] == "POU5F1B" and r.summary.splitlines()[1].startswith("POU5F1B")
    t = nearest_genes(tert)
    assert t.full[0]["gene"] == "TERT" and t.full[0]["strand"] == -1 and t.full[0]["position"] == "upstream"


@pytest.mark.data           # the ENCODE cCRE file in data/reference/
def test_ccre_local_and_screen(rs6983267, tert):
    r = ccre_lookup(rs6983267)
    assert r.ok and "pELS" in r.summary and "DNase z" in r.summary
    assert ccre_lookup(tert).full["local"]["class"] == "PLS"


def test_gwas(rs6983267):
    r = gwas_lookup(rs6983267)
    assert r.ok and r.summary.startswith("69 GWAS Catalog associations") and "effect allele" in r.summary


def test_gwas_needs_rsid(tert):
    r = gwas_lookup(tert)
    assert not r.ok and "no rsID" in r.summary


def test_finemap(rs6983267):
    r = finemap_lookup(rs6983267)
    assert r.ok and "PIP" in r.summary and "POU5F1B" in r.summary


def test_literature_and_masking(rs6983267):
    q = 'rs6983267 AND POU5F1B AND "colorectal cancer"'
    r = literature_search(rs6983267, q)
    assert r.ok and r.full and all(p["pmid"] for p in r.full)
    m = literature_search(rs6983267, q, masked=True)
    assert "rs6983267" not in m.summary and all("rs6983267" not in p["abstract"] for p in m.full)


def test_chip_peaks_tells_no_experiment_from_no_peak(rs6983267):
    """ENCODE assayed TCF7L2 in K562 (no peak here), HOXB13 only in A549, and never TFAP2A."""
    absent = chip_peaks(rs6983267, "TCF7L2", biosample="K562")
    assert absent.full["status"] == "assayed_no_peak" and "evidence against TCF7L2 occupancy" in absent.summary
    none_here = chip_peaks(rs6983267, "HOXB13", biosample="LNCaP clone FGC")
    assert none_here.ok and none_here.full["status"] == "not_assayed"
    assert "ENCODE says nothing about it there, for or against" in none_here.summary and "A549" in none_here.summary
    assert "ENCODE never assayed TFAP2A" in chip_peaks(rs6983267, "TFAP2A").summary
    assert "ReMap 2022 has no TFAP2A peak" in chip_peaks(rs6983267, "TFAP2A").summary


def test_remap_supplies_occupancy_encode_lacks():
    """rs339331: ENCODE assayed HOXB13 only in A549; ReMap has HOXB13 peaks over it in LNCaP (published ChIP-seq)."""
    case = Case(Variant.make("chr6", 116888889, "T", "C"), "Prostate cancer", http=Http(FIXTURES, offline=True))
    r = chip_peaks(case, "HOXB13", biosample="LNCaP clone FGC")
    assert r.full["status"] == "peak" and "ENCODE has no HOXB13 ChIP-seq experiment" in r.summary
    assert "LNCaP (GSE" in r.summary and "nearest summit 11 bp" in r.summary
    assert chip_peaks(case, "HOXB13", biosample="K562").full["status"] == "not_assayed"   # ReMap: no K562 peak


def test_investigate_tools(rs6983267, tert):
    c = chip_peaks(rs6983267, "TCF7L2", biosample="HCT116")
    assert c.ok and "HCT116" in c.summary and c.full["status"] == "peak"
    assert "SK-N-SH" in chip_peaks(tert, "GABPA").summary
    e = eqtl_lookup(rs6983267, tissue="Colon")
    assert e.ok and "NES is the effect of the alt allele" in e.summary
    g = gene_disease(rs6983267, "MYC", ensembl_id="ENSG00000136997")
    assert g.ok and "MONDO_0005575" in g.summary


@pytest.mark.data           # the ENCODE cCRE file in data/reference/
def test_summaries_are_short(rs6983267):
    for fn in (variant_annotation, nearest_genes, ccre_lookup, gwas_lookup, finemap_lookup):
        assert len(fn(rs6983267).summary) <= SUMMARY_LIMIT


def test_offline_miss_is_an_error_not_an_exception(http):
    case = Case(Variant.make("chr1", 12345, "A", "C"), "x", http=http)
    r = variant_annotation(case)
    assert not r.ok and "offline and not cached" in r.summary


class FlakySession:
    def __init__(self, statuses, retry_after=None):
        self.statuses, self.calls, self.retry_after = list(statuses), 0, retry_after

    def request(self, *a, **k):
        self.calls += 1
        status = self.statuses.pop(0) if self.statuses else 200
        hdrs = {"Retry-After": str(self.retry_after)} if (self.retry_after and status != 200) else {}

        class R:
            status_code = status
            headers = hdrs
            text = '{"seq": "G"}' if status == 200 else "busy"

            def json(self):
                return [{"allele_string": "A/C", "most_severe_consequence": "intergenic_variant"}]
        return R()


def test_retries_with_backoff_then_error_summary(tmp_path):
    waits = []
    s = FlakySession([503] * 6)
    http = Http(tmp_path, session=s, sleep=waits.append)
    r = variant_annotation(Case(Variant.make("chr1", 5, "A", "C"), "x", http=http))
    assert s.calls == 6 and not r.ok and r.retryable and "failed after 6 tries" in r.summary
    assert waits == [2, 4, 8, 16, 32]


def test_retry_after_is_honoured(tmp_path):
    waits = []
    http = Http(tmp_path, session=FlakySession([429, 200], retry_after=7), sleep=waits.append)
    assert http.get("https://example.org/z").ok and waits == [7]


def test_whole_tool_is_rerun_after_a_transient_failure(tmp_path):
    from variant2mechanism.context.base import call_tool
    waits = []
    s = FlakySession([503] * 6)                      # the first run's 6 tries all fail; the re-run succeeds
    case = Case(Variant.make("chr1", 5, "A", "C"), "x", http=Http(tmp_path, session=s, sleep=waits.append),
                retry_wait=60)
    r = call_tool(variant_annotation, case)
    assert r.ok and r.attempts == 2 and 60 in waits and s.calls == 7


def test_lasting_errors_are_not_rerun(tmp_path):
    from variant2mechanism.context.base import call_tool
    s = FlakySession([404] * 10)
    case = Case(Variant.make("chr1", 5, "A", "C"), "x", http=Http(tmp_path, session=s, sleep=lambda x: None))
    r = call_tool(variant_annotation, case)
    assert not r.ok and not r.retryable and r.attempts == 1 and s.calls == 1
    offline = Case(Variant.make("chr1", 6, "A", "C"), "x", http=Http(tmp_path / "o", offline=True))
    assert call_tool(variant_annotation, offline).attempts == 1


def test_retry_recovers_and_caches(tmp_path):
    s = FlakySession([429, 200])
    http = Http(tmp_path, session=s, sleep=lambda x: None)
    assert http.get("https://example.org/x").ok and s.calls == 2
    assert http.get("https://example.org/x").cached and s.calls == 2      # second call free


def test_client_error_not_retried(tmp_path):
    s = FlakySession([404])
    r = Http(tmp_path, session=s, sleep=lambda x: None).get("https://example.org/y")
    assert not r.ok and s.calls == 1 and "HTTP 404" in r.error


def test_tool_definitions_are_strict():
    full = {t["function"]["name"] for t in tool_definitions("full", cancer=True)}
    no_qbic = {t["function"]["name"] for t in tool_definitions("no_qbic", cancer=False)}
    assert "qbic_tf_detail" in full and "qbic_tf_detail" not in no_qbic and "gene_dependency" not in no_qbic
    for t in tool_definitions("full", cancer=True):
        f, s = t["function"], t["function"]["parameters"]
        assert t["type"] == "function" and f["strict"] and s["additionalProperties"] is False
        assert set(s["required"]) == set(s["properties"])


# -- gene_dependency and common essentials ------------------------------------------------------------------


@pytest.fixture
def essentials(tmp_path):
    p = tmp_path / "CRISPRInferredCommonEssentials.csv"
    p.write_text("Essentials\nESS1 (111)\nOLDNAME (222)\n")
    return p


def small_depmap():
    effects = pd.DataFrame({"ESS1": [-1.2, -1.0, -0.9], "OTHER": [-0.1, -0.7, 0.0]}, index=["ACH-1", "ACH-2", "ACH-3"])
    models = pd.DataFrame({"CellLineName": ["L1", "L2", "L3"], "OncotreeLineage": ["Bowel", "Bowel", "Lung"],
                           "OncotreeSubtype": ["Colon Adenocarcinoma"] * 2 + ["NSCLC"]}, index=effects.index)
    return effects, models


def test_common_essential_match_by_entrez_then_symbol(essentials):
    assert is_common_essential("RENAMED", "222", essentials)       # Entrez ID matches despite a new symbol
    assert is_common_essential("ESS1", None, essentials)           # no Entrez ID: symbol
    assert not is_common_essential("OTHER", "333", essentials)


def test_gene_dependency_flags_common_essential(essentials):
    effects, models = small_depmap()
    case = Case(Variant.make("chr8", 1, "G", "T"), "Colorectal cancer", expression_context="DepMap:ACH-1 (L1)")
    ess = gene_dependency(case, "ESS1", effects, models, essentials, entrez="111")
    assert ess.full["common_essential"] and COMMON_ESSENTIAL_LINE in ess.summary
    assert "Bowel lineage, 2 lines" in ess.summary and "L1 (ACH-1): -1.20" in ess.summary
    other = gene_dependency(case, "OTHER", effects, models, essentials, entrez="333")
    assert not other.full["common_essential"] and COMMON_ESSENTIAL_LINE not in other.summary
    assert other.full["lineage_median"] == pytest.approx(-0.4)


@pytest.mark.data
def test_real_common_essentials_myc_vs_tcf7l2():
    from variant2mechanism.config import load_config
    path = load_config().path("data", "depmap_common_essentials")
    assert is_common_essential("MYC", "4609", path)
    assert not is_common_essential("TCF7L2", "6934", path)



def test_chip_filter_never_hides_a_peak_over_the_variant(tmp_path):
    """Regression (rs1427407): filtering to K562 hid a GATA1 erythroblast peak that contains the SNP."""
    pos = 60490908
    peaks = [{"experiment_accession": "ENCSR1", "chrom": "chr2", "chrom_start": pos - 67, "chrom_end": pos + 244,
              "target": "GATA1", "biosample": "erythroblast"},
             {"experiment_accession": "ENCSR2", "chrom": "chr2", "chrom_start": pos + 16, "chrom_end": pos + 620,
              "target": "GATA1", "biosample": "erythroblast"}]

    class S:
        def request(self, *a, **k):
            class R:
                status_code, headers, text = 200, {}, ""

                def json(self):
                    return {"data": {"peaksrange": {"data": peaks}}}
            return R()
    case = Case(Variant.make("chr2", pos, "T", "G"), "x", http=Http(tmp_path, session=S(), sleep=lambda x: None))
    r = chip_peaks(case, "GATA1", biosample="K562")
    assert "No ENCODE GATA1 ChIP-seq peak contains" in r.summary
    assert "In other biosamples, 1 GATA1 peaks do contain the variant: erythroblast" in r.summary
    assert len(r.full["other_biosamples"]) == 1
