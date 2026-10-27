import json

import pandas as pd
import pytest
from qbic_fixtures import MODELS

from variant2mechanism.qbic.cache import QbicCache
from variant2mechanism.qbic.tools import QbicTools

TERT = ("chr5", 1295113, "G", "A")
KEY = "chr5:1295113:G>A"


@pytest.fixture
def no_ensembl(monkeypatch):
    monkeypatch.setattr("variant2mechanism.qbic.tools.strand_precheck", lambda v: None)


def test_bad_variant_is_an_error_not_an_exception(small_cfg):
    out = QbicTools(small_cfg).qbic_screen("chr5", 1295113, "GA", "A")
    assert "error" in out and "fix" in out


def test_cache_miss_without_permission_makes_no_job(small_cfg, no_ensembl):
    class Boom:
        def run(self, *a, **k):
            raise AssertionError("must not submit")
    out = QbicTools(small_cfg, cluster=Boom()).qbic_screen(*TERT)
    assert out["error"].startswith(KEY) and "allow_miss_jobs" in out["fix"]


def test_minus_strand_hint_returned(small_cfg, monkeypatch):
    monkeypatch.setattr("variant2mechanism.qbic.tools.strand_precheck", lambda v: "Alleles look like minus-strand")
    assert "minus-strand" in QbicTools(small_cfg).qbic_screen("chr5", 1295113, "C", "T")["error"]


@pytest.mark.data
def test_tf_detail_names_and_coverage(small_cfg):
    t = QbicTools(small_cfg)
    assert t.qbic_tf_detail(*TERT, "ARID5B") == {"tf": "ARID5B", "symbol": "ARID5B", "via": "hgnc_symbol",
                                                 "notes": [], "coverage": "not_in_coverage"}
    amb = t.qbic_tf_detail(*TERT, "NRF2")
    assert amb["status"] == "ambiguous" and [c["symbol"] for c in amb["candidates"]] == ["GABPA", "NFE2L2"]


@pytest.mark.data
def test_screen_and_detail_on_synthetic_cached_rows(small_cfg, no_ensembl):
    df = pd.DataFrame({"variant_key": KEY, "ref_sequence": "AGGGCCCGGAGGGGGCTGGGC",
                       "alt_sequence": "AGGGCCCGGAAGGGGCTGGGC", "model": MODELS, "predicted_effect": [3.0, 4.0],
                       "z_score": [9.0, 12.0], "p_value": [1e-19, 1e-33], "qbic_status": "ok"})
    QbicCache(small_cfg).import_results({"run_id": "r1"}, df, {KEY}, stats=True)
    t = QbicTools(small_cfg)
    out = t.qbic_screen(*TERT, expression_context="DepMap:subtype=Glioblastoma (median of 54 lines)")
    assert out["n_pass"] == 2 and out["groups"][0]["best_tf"] == "GABPA"
    assert out["groups"][0]["label"].startswith("Ets") and "site_strength" in out["groups"][0]
    assert len(json.dumps(out)) < 3500
    d = t.qbic_tf_detail(*TERT, "GABPA")
    assert d["coverage"] == "tf" and d["models"][0]["mapping"] == "own" and d["models"][0]["passed_gate"]


@pytest.mark.data
def test_untrimmed_screen_keeps_all_top_groups(no_ensembl):
    """Regression: the 3,000-character trim cut the screen to 4 groups; the screen stage must see all 10."""
    from variant2mechanism.qbic.cache import QbicCache
    t = QbicTools()
    key = "chr1:209815925:A>G"
    if key not in QbicCache(t.cfg).cached([key]):
        pytest.skip("rs642961 is not in the committed cache")
    full = t.qbic_screen("chr1", 209815925, "A", "G", None, compact=False)
    assert len(full["groups"]) == 10 and "n_groups_trimmed" not in full
    assert any(g["label"].startswith("AP-2") for g in full["groups"])     # TFAP2A's group, rank 6
    short = t.qbic_screen("chr1", 209815925, "A", "G", None)
    assert len(json.dumps(short, separators=(",", ":"))) <= 3000
