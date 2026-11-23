"""sumstats.py, locus.py and plot.py: windows of the two published formats, matched alleles, one window analysed.

No test reaches a server. The tables are written here in the two sources' own column layouts, from a simulated
locus whose causal variants are known, and the reader is used offline against a cache folder the test fills.
"""

import gzip
import json

import numpy as np
import pandas as pd
import pytest

from variant2mechanism.statgen import locus, plot, sumstats
from variant2mechanism.statgen import simulate as S

P, START = 200, 109_200_000
BASES = np.array(list("ACGT"))


def tables(seed: int = 7, swap_every: int = 3):
    """A GWAS table and an eQTL table of one simulated window, as the two sources write them: the GWAS shares its
    causal variant (80) with gene ENSG_SHARED and has another than ENSG_OTHER (160); ENSG_QUIET has no signal and
    ENSG_FEW is listed at ten variants only. Every `swap_every`-th GWAS row names the other allele as the effect
    allele, with the effect's sign changed to match."""
    rng = np.random.default_rng(seed)
    freq = S.frequencies(P, rng)
    pos = START + 500 * np.arange(P)
    ref = BASES[rng.integers(0, 4, P)]
    alt = BASES[(np.searchsorted(BASES, ref) + rng.integers(1, 4, P)) % 4]
    g1, g2 = S.genotypes(6000, freq, 0.97, rng), S.genotypes(500, freq, 0.97, rng)
    beta, se = S.association(g1, S.trait(g1, {80: S.effect_for_z(9, 6000, freq[80])}, rng))
    swap = np.arange(P) % swap_every == 0
    gwas = pd.DataFrame({
        "chromosome": "1", "base_pair_location": pos, "effect_allele": np.where(swap, ref, alt),
        "other_allele": np.where(swap, alt, ref), "beta": np.where(swap, -beta, beta), "standard_error": se,
        "effect_allele_frequency": np.where(swap, 1 - freq, freq), "p_value": 0.5,
        "variant_id": [f"1_{x}" for x in pos], "n": 6000, "rsid": [f"rs{9000 + i}" for i in range(P)]})
    rows = []
    for gene, causal in (("ENSG_SHARED", {80: 9}), ("ENSG_OTHER", {160: 9}), ("ENSG_QUIET", {})):
        b, s = S.association(g2, S.trait(g2, {j: S.effect_for_z(z, 500, freq[j]) for j, z in causal.items()}, rng))
        rows.append(pd.DataFrame({
            "molecular_trait_id": gene, "chromosome": "1", "position": pos, "ref": ref, "alt": alt,
            "variant": [f"chr1_{x}" for x in pos], "ma_samples": 100, "maf": freq, "pvalue": 0.5, "beta": b,
            "se": s, "type": "SNP", "ac": 200, "an": 1000, "r2": "NA", "molecular_trait_object_id": gene,
            "gene_id": gene, "median_tpm": 5.0, "rsid": [f"rs{9000 + i}" for i in range(P)]}))
    rows.append(rows[0].iloc[:10].assign(gene_id="ENSG_FEW", molecular_trait_id="ENSG_FEW"))
    return gwas.astype(str), pd.concat(rows, ignore_index=True).astype(str), pos, freq


# --- where the files are -------------------------------------------------------------------------------------------------

def test_the_addresses_follow_the_two_sources_layouts():
    assert sumstats.gwas_catalog_url("GCST90239658") == (
        "https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90239001-GCST90240000/GCST90239658/"
        "harmonised/GCST90239658.h.tsv.gz")
    assert "/GCST004001-GCST005000/GCST004131/" in sumstats.gwas_catalog_url("GCST004131")
    assert "/GCST90239001-GCST90240000/GCST90240000/" in sumstats.gwas_catalog_url("GCST90240000")
    assert sumstats.eqtl_catalogue_url("QTS000015", "QTD000266").endswith(
        "/eQTL/sumstats/QTS000015/QTD000266/QTD000266.all.tsv.gz")
    with pytest.raises(ValueError, match="not a GWAS Catalog study accession"):
        sumstats.gwas_catalog_url("rs12740374")


# --- the reader, offline -------------------------------------------------------------------------------------------------

def test_a_cached_window_is_read_without_asking_the_server(tmp_path):
    gwas, _, pos, _ = tables()
    url = sumstats.gwas_catalog_url("GCST90239658")
    path = tmp_path / "windows" / f"GCST90239658.h__1_{pos[0]}_{pos[-1]}.tsv.gz"
    path.parent.mkdir(parents=True)
    with gzip.open(path, "wt") as out:
        gwas.to_csv(out, sep="\t", index=False)
    reader = sumstats.WindowReader(tmp_path, offline=True)
    table = reader.window(url, "chr1", int(pos[0]), int(pos[-1]))
    assert list(table.columns) == list(gwas.columns) and len(table) == P and reader.requests == []
    assert table["base_pair_location"].iloc[0] == str(pos[0])           # text, as the source wrote it


def test_an_offline_reader_says_what_the_cache_lacks(tmp_path):
    reader = sumstats.WindowReader(tmp_path, offline=True)
    url = sumstats.eqtl_catalogue_url("QTS000015", "QTD000266")
    with pytest.raises(sumstats.CacheMiss, match="the first block of"):
        reader.window(url, "1", 100, 200)
    (tmp_path / "header").mkdir()
    (tmp_path / "header" / "QTD000266.all.tsv.gz.header.tsv").write_text("gene_id\tposition\n")
    assert reader.header(url) == ["gene_id", "position"]
    with pytest.raises(sumstats.CacheMiss, match="the index of"):
        reader.window(url, "1", 100, 200)
    with pytest.raises(ValueError, match="a start of at least 1"):
        reader.window(url, "1", 200, 100)


# --- the tables as numbers, and matched alleles --------------------------------------------------------------------------

def test_rows_without_an_effect_are_left_out_and_the_sample_size_is_half_the_allele_number():
    gwas, eqtl, _, _ = tables()
    gwas.loc[0, "beta"], gwas.loc[1, "standard_error"], eqtl.loc[0, "se"] = "NA", "0", ""
    g, e = sumstats.gwas_frame(gwas), sumstats.eqtl_frame(eqtl)
    assert len(g) == P - 2 and len(e) == len(eqtl) - 1
    assert e["n"].iloc[0] == 500 and g["pos"].dtype.kind == "i" and "an" not in e.columns
    with pytest.raises(ValueError, match="lacks the column"):
        sumstats.gwas_frame(gwas.drop(columns=["standard_error"]))


def test_effects_are_written_for_one_allele_and_mismatched_alleles_are_left_out():
    gwas, eqtl, pos, freq = tables()
    g = sumstats.gwas_frame(gwas)
    e = sumstats.eqtl_frame(eqtl)
    one = e[e["gene"] == "ENSG_SHARED"]
    shared = sumstats.align(g, one)
    assert len(shared) == P and shared["pos"].is_monotonic_increasing
    # row 0 was written for the other allele: after matching, its effect is for the eQTL table's alt allele again
    plain = sumstats.align(sumstats.gwas_frame(tables(swap_every=10 ** 6)[0]), one)
    assert np.allclose(shared["beta_gwas"], plain["beta_gwas"]) and np.allclose(shared["maf_gwas"], freq)
    assert g["beta"].iloc[0] == pytest.approx(-shared["beta_gwas"].iloc[0])
    assert shared["n_eqtl"].iloc[0] == 500 and shared["rsid"].iloc[3] == "rs9003"
    other = g.copy()
    other.loc[5, "effect_allele"] = "N"                                 # another variant at that position
    doubled = pd.concat([other, other.iloc[[9]]], ignore_index=True)    # one variant listed twice
    left = sumstats.align(doubled, one)
    assert len(left) == P - 2 and not {int(pos[5]), int(pos[9])} & set(left["pos"])
    bare = sumstats.align(g.drop(columns=["eaf", "n", "rsid"]), one.drop(columns=["maf", "n"]))
    assert bare["maf_gwas"].isna().all() and bare["n_eqtl"].isna().all() and len(bare) == P


# --- one window ----------------------------------------------------------------------------------------------------------

def analysed():
    gwas, eqtl, pos, _ = tables()
    return locus.analyse(sumstats.gwas_frame(gwas), sumstats.eqtl_frame(eqtl), focus=int(pos[80]),
                         symbols={"ENSG_SHARED": "SHARED1"}), pos


def test_the_window_is_fine_mapped_and_each_gene_compared():
    result, pos = analysed()
    by = {g["gene"]: g for g in result["genes"]}
    assert set(by) == {"ENSG_SHARED", "ENSG_OTHER", "ENSG_QUIET"}
    assert by["ENSG_SHARED"]["PP.H4"] > 0.9 and by["ENSG_OTHER"]["PP.H3"] > 0.9 and by["ENSG_QUIET"]["PP.H1"] > 0.8
    assert result["genes"][0]["gene"] == "ENSG_SHARED" and by["ENSG_SHARED"]["symbol"] == "SHARED1"
    assert abs(by["ENSG_SHARED"]["shared_variant"]["pos"] - pos[80]) <= 5 * 500
    assert result["skipped"] == [{"gene": "ENSG_FEW", "symbol": "ENSG_FEW", "shared_variants": 10,
                                  "why": "fewer than 50 variants are in both tables"}]
    near = [abs(v["pos"] - pos[80]) for v in result["gwas"]["credible_set"]]
    assert result["gwas"]["variants"] == P and max(near) <= 10 * 500
    assert sum(v["pp"] for v in result["gwas"]["credible_set"]) >= 0.95
    assert result["gwas"]["sdy"] == pytest.approx(1.0, rel=0.05)
    assert [row["p12"] for row in by["ENSG_SHARED"]["sensitivity"]] == [1e-8, 1e-7, 1e-6, 1e-5, 1e-4]


def test_the_variant_of_interest_is_reported_with_both_effects_for_one_allele():
    result, pos = analysed()
    focus = result["gwas"]["focus"]
    gene = next(g for g in result["genes"] if g["gene"] == "ENSG_SHARED")["focus"]
    assert focus["pos"] == pos[80] and focus["rsid"] == "rs9080" and focus["in_credible_set"] in (True, False)
    assert gene["rsid"] == "rs9080" and gene["z_gwas"] > 4 and gene["z_eqtl"] > 4     # both raise, for alt
    assert locus.analyse(*[f(t) for f, t in zip((sumstats.gwas_frame, sumstats.eqtl_frame), tables()[:2],
                                                strict=True)])["gwas"]["focus"] is None


def test_the_result_is_plain_data_and_records_its_settings():
    result, _ = analysed()
    saved = json.loads(json.dumps(locus.summary(result)))
    assert "tables" not in saved and saved["settings"] == {
        "p1": 1e-4, "p2": 1e-4, "p12": 1e-5, "gwas_kind": "quant", "eqtl_kind": "quant", "coverage": 0.95,
        "min_variants": 50}
    assert set(result["tables"]) == {"gwas", "ENSG_SHARED", "ENSG_OTHER", "ENSG_QUIET"}
    strict = locus.analyse(*[f(t) for f, t in zip((sumstats.gwas_frame, sumstats.eqtl_frame), tables()[:2],
                                                  strict=True)], settings=locus.Settings(p12=1e-8))
    assert strict["genes"][0]["PP.H4"] < result["genes"][0]["PP.H4"]


def test_p_values_are_computed_on_the_log_scale():
    assert locus.minus_log10_p(np.array([1.959964]))[0] == pytest.approx(-np.log10(0.05), abs=1e-5)
    assert locus.minus_log10_p(np.array([-89.08]))[0] == pytest.approx(1725.3, abs=1.0)   # p = 4.7e-1726
    assert locus.minus_log10_p(np.array([0.0]))[0] == 0.0


def test_the_figure_is_drawn(tmp_path):
    result, _ = analysed()
    out = plot.regional(result, ["ENSG_SHARED", "ENSG_OTHER", "ENSG_MISSING"], tmp_path / "fig" / "window.png",
                        chrom="1", gwas_label="A simulated GWAS", eqtl_label="simulated tissue", focus_label="rs9080")
    assert out.exists() and out.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n" and out.stat().st_size > 20_000
