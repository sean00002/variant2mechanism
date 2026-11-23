"""abf.py and coloc.py: Bayes factors per variant, fine-mapping under one causal variant, and colocalisation.

The formulas are checked against their closed forms on a few variants (where every case can be written out), and
the behaviour against simulated loci whose causal variants are known (simulate.py).
"""

import itertools

import numpy as np
import pytest

from variant2mechanism.statgen import abf, coloc
from variant2mechanism.statgen import simulate as S


def cohort(seed: int, n: int, p: int = 200, rho: float = 0.97):
    """Frequencies and genotypes of one cohort; two cohorts with one `freq` share their LD pattern."""
    rng = np.random.default_rng(seed)
    freq = S.frequencies(p, np.random.default_rng(1))
    return freq, S.genotypes(n, freq, rho, rng), rng


def labf(g: np.ndarray, freq: np.ndarray, effects: dict[int, float], rng) -> np.ndarray:
    beta, se = S.association(g, S.trait(g, effects, rng))
    return abf.log_abf(beta, se, abf.prior_sd("quant", abf.estimate_sdy(se ** 2, freq, g.shape[0])))


# --- Bayes factors -------------------------------------------------------------------------------------------------------

def test_the_log_bayes_factor_is_wakefields():
    beta, se, w = np.array([0.2, -0.1, 0.0]), np.array([0.05, 0.05, 0.02]), 0.15
    v, z = se ** 2, beta / se
    direct = np.log(np.sqrt(v / (v + w ** 2)) * np.exp(z ** 2 / 2 * w ** 2 / (v + w ** 2)))
    assert np.allclose(abf.log_abf(beta, se, w), direct, rtol=0, atol=1e-12)
    assert abf.log_abf(beta, se, w)[0] == pytest.approx(0.5 * (np.log(0.1) + 0.9 * 16))     # r = 0.9, z = 4
    assert abf.log_abf(np.array([0.0]), np.array([0.02]), w)[0] < 0                          # no effect: against


def test_a_z_score_of_ninety_does_not_overflow():
    out = abf.log_abf(np.array([-0.148228, 0.001]), np.array([0.00166391, 0.002]), 0.15)
    assert np.all(np.isfinite(out)) and out[0] > 3000
    assert abf.posterior(out) == pytest.approx([1.0, 0.0])


def test_the_prior_follows_the_kind_of_trait():
    assert abf.prior_sd("quant") == 0.15 and abf.prior_sd("quant", 2.0) == 0.3 and abf.prior_sd("cc") == 0.2
    with pytest.raises(ValueError, match="quant or cc"):
        abf.prior_sd("binary")


def test_the_traits_standard_deviation_is_recovered_from_the_standard_errors():
    freq, g, rng = cohort(3, 4000)
    for sd in (1.0, 2.5):
        _, se = S.association(g, S.trait(g, {}, rng, noise_sd=sd))
        assert abf.estimate_sdy(se ** 2, freq, 4000) == pytest.approx(sd, rel=0.05)
    with pytest.raises(ValueError, match="to estimate sdY from"):
        abf.estimate_sdy(np.array([0.01]), np.array([np.nan]), 100)


def test_bad_input_is_refused():
    with pytest.raises(ValueError, match="positive standard error"):
        abf.log_abf(np.array([0.1]), np.array([0.0]), 0.15)
    with pytest.raises(ValueError, match="differ in length"):
        abf.log_abf(np.array([0.1, 0.2]), np.array([0.1]), 0.15)
    with pytest.raises(ValueError, match="coverage"):
        abf.credible_set(np.array([1.0]), 0.0)


# --- one causal variant --------------------------------------------------------------------------------------------------

def test_the_credible_set_is_the_smallest_that_reaches_the_coverage():
    pp = np.array([0.05, 0.5, 0.15, 0.3])
    assert abf.credible_set(pp, 0.95).tolist() == [1, 3, 2]
    assert abf.credible_set(pp, 0.5).tolist() == [1] and abf.credible_set(pp, 0.51).tolist() == [1, 3]
    assert abf.credible_set(pp, 1.0).tolist() == [1, 3, 2, 0]


def test_the_credible_set_holds_the_causal_variant_and_its_neighbours_in_ld():
    freq, g, rng = cohort(5, 5000)
    pp = abf.posterior(labf(g, freq, {80: S.effect_for_z(9, 5000, freq[80])}, rng))
    members = abf.credible_set(pp)
    assert pp.sum() == pytest.approx(1.0) and 80 in members
    assert max(abs(int(i) - 80) for i in members) <= 10        # the set stays near the causal variant


def test_with_two_signals_the_set_follows_the_stronger_one_only():
    freq, g, rng = cohort(6, 5000)
    effects = {50: S.effect_for_z(10, 5000, freq[50]), 150: S.effect_for_z(6, 5000, freq[150])}
    members = abf.credible_set(abf.posterior(labf(g, freq, effects, rng)))
    assert any(abs(int(i) - 50) <= 5 for i in members) and not any(abs(int(i) - 150) <= 20 for i in members)


# --- colocalisation ------------------------------------------------------------------------------------------------------

def test_the_five_posteriors_equal_the_sum_over_every_configuration():
    rng = np.random.default_rng(11)
    l1, l2 = rng.normal(0, 3, 6), rng.normal(0, 3, 6)
    p1, p2, p12 = 1e-3, 2e-3, 5e-4
    b1, b2 = np.exp(l1), np.exp(l2)
    h3 = sum(p1 * p2 * b1[i] * b2[j] for i, j in itertools.permutations(range(6), 2))
    cases = np.array([1.0, p1 * b1.sum(), p2 * b2.sum(), h3, p12 * (b1 * b2).sum()])
    found = coloc.coloc_abf(l1, l2, p1, p2, p12)
    assert np.allclose(found.pp, cases / cases.sum(), rtol=1e-10)
    assert found.pp.sum() == pytest.approx(1.0) and found.snp_h4.sum() == pytest.approx(1.0)
    assert found.n_variants == 6 and found.priors == (p1, p2, p12)
    assert found.as_dict()["PP.H4"] == found.h4 and set(found.as_dict()) == {f"PP.H{i}" for i in range(5)}


def test_one_variant_cannot_be_two_different_causal_variants():
    found = coloc.coloc_abf(np.array([8.0]), np.array([9.0]))
    assert found.h3 == 0.0 and found.pp.sum() == pytest.approx(1.0)


@pytest.mark.parametrize("gwas, eqtl, expected", [
    ({80: 8}, {80: 8}, "PP.H4"),             # the same causal variant
    ({40: 8}, {160: 8}, "PP.H3"),            # two causal variants, far apart
    ({80: 8}, {}, "PP.H1"),                  # only the first trait has one
    ({}, {80: 8}, "PP.H2"),
    ({}, {}, "PP.H0"),
])
def test_colocalisation_names_the_case_the_data_were_simulated_under(gwas, eqtl, expected):
    freq, g1, rng1 = cohort(21, 5000)
    _, g2, rng2 = cohort(22, 500)
    l1 = labf(g1, freq, {j: S.effect_for_z(z, 5000, freq[j]) for j, z in gwas.items()}, rng1)
    l2 = labf(g2, freq, {j: S.effect_for_z(z, 500, freq[j]) for j, z in eqtl.items()}, rng2)
    found = coloc.coloc_abf(l1, l2).as_dict()
    assert max(found, key=found.get) == expected and found[expected] > 0.8


def test_the_shared_variant_carries_the_share_of_h4():
    freq, g1, rng1 = cohort(31, 5000)
    _, g2, rng2 = cohort(32, 500)
    found = coloc.coloc_abf(labf(g1, freq, {80: S.effect_for_z(9, 5000, freq[80])}, rng1),
                            labf(g2, freq, {80: S.effect_for_z(9, 500, freq[80])}, rng2))
    assert found.h4 > 0.9 and abs(int(np.argmax(found.snp_h4)) - 80) <= 5


def test_the_prior_of_a_shared_variant_moves_the_answer_one_way():
    freq, g1, rng1 = cohort(41, 3000)
    _, g2, rng2 = cohort(42, 300)
    l1 = labf(g1, freq, {80: S.effect_for_z(5, 3000, freq[80])}, rng1)
    l2 = labf(g2, freq, {84: S.effect_for_z(5, 300, freq[84])}, rng2)
    rows = coloc.sensitivity(l1, l2)
    assert [p for p, _, _ in rows] == [1e-8, 1e-7, 1e-6, 1e-5, 1e-4]
    assert all(a[2] <= b[2] for a, b in itertools.pairwise(rows))      # more prior for sharing, more H4
    assert rows[3][1:] == (coloc.coloc_abf(l1, l2).h3, coloc.coloc_abf(l1, l2).h4)


def test_colocalisation_refuses_lists_that_do_not_match():
    with pytest.raises(ValueError, match="same, non-empty list"):
        coloc.coloc_abf(np.array([1.0, 2.0]), np.array([1.0]))
    with pytest.raises(ValueError, match="priors"):
        coloc.coloc_abf(np.array([1.0]), np.array([1.0]), p12=0.0)
