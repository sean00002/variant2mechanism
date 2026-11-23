"""susie.py and simulate.py: several causal variants in one window, on data whose causal variants are known."""

import numpy as np
import pytest

from variant2mechanism.statgen import abf, susie
from variant2mechanism.statgen import simulate as S

N, P = 4000, 150


def locus(seed: int, rho: float = 0.97):
    rng = np.random.default_rng(seed)
    freq = S.frequencies(P, rng)
    g = S.genotypes(N, freq, rho, rng)
    return freq, g, S.ld(g), rng


def zscores(g: np.ndarray, freq: np.ndarray, causal: dict[int, float], rng) -> np.ndarray:
    beta, se = S.association(g, S.trait(g, {j: S.effect_for_z(z, N, freq[j]) for j, z in causal.items()}, rng))
    return beta / se


# --- the simulated locus -------------------------------------------------------------------------------------------------

def test_neighbouring_variants_are_in_ld_and_distant_ones_are_not():
    freq, g, r, _ = locus(1)
    assert g.shape == (N, P) and set(np.unique(g)) <= {0, 1, 2}
    assert np.allclose(g.mean(axis=0) / 2, freq, atol=0.03)               # each variant has its own frequency
    assert np.median(np.abs(np.diag(r, 1))) > 0.5 and np.median(np.abs(np.diag(r, 100))) < 0.1
    with pytest.raises(ValueError, match="rho"):
        S.genotypes(10, freq, 1.0, np.random.default_rng(0))


def test_the_summary_statistics_are_those_of_a_regression_of_the_trait_on_each_variant():
    freq, g, _, rng = locus(2)
    y = S.trait(g, {40: 0.3}, rng)
    beta, se = S.association(g, y)
    slope, intercept = np.polyfit(g[:, 40].astype(float), y, 1)
    residual = y - (slope * g[:, 40] + intercept)
    by_hand = np.sqrt(residual @ residual / (N - 2) / np.sum((g[:, 40] - g[:, 40].mean()) ** 2))
    assert beta[40] == pytest.approx(slope) and se[40] == pytest.approx(by_hand)
    assert beta[40] == pytest.approx(0.3, abs=0.06)
    assert zscores(g, freq, {40: 8.0}, rng)[40] == pytest.approx(8.0, abs=2.5)   # effect_for_z aims at this z


# --- SuSiE ---------------------------------------------------------------------------------------------------------------

def test_one_signal_gives_one_credible_set_that_holds_the_causal_variant():
    freq, g, r, rng = locus(3)
    fit = susie.susie_rss(zscores(g, freq, {70: 9.0}, rng), r, N)
    assert fit.converged and len(fit.sets) == 1 and 70 in fit.sets[0].variants
    assert fit.sets[0].coverage >= 0.95 and fit.sets[0].purity >= 0.5
    assert np.all((fit.pip >= 0) & (fit.pip <= 1)) and fit.pip[fit.sets[0].variants].sum() > 0.95
    assert np.all(np.diff(fit.elbo) > -1e-6)                              # the objective never falls


def test_two_signals_give_two_sets_where_one_causal_variant_would_find_one():
    freq, g, r, rng = locus(4)
    z = zscores(g, freq, {40: 10.0, 110: 7.0}, rng)
    fit = susie.susie_rss(z, r, N)
    held = sorted(next((c for c in (40, 110) if c in s.variants), None) for s in fit.sets)
    assert held == [40, 110] and fit.converged
    assert fit.pip[40] > 0.5 or fit.pip[fit.sets[0].variants].sum() > 0.9
    one = abf.credible_set(abf.posterior(abf.log_abf(z, np.ones(P), 0.15 * np.sqrt(N))))
    assert not any(abs(int(i) - 110) <= 15 for i in one)                  # the second signal is not in that set


def test_no_signal_gives_no_credible_set():
    freq, g, r, rng = locus(5)
    fit = susie.susie_rss(zscores(g, freq, {}, rng), r, N)
    assert fit.sets == [] and fit.pip.max() < 0.5 and fit.converged


def test_two_variants_in_perfect_ld_share_the_set():
    freq, g, _, rng = locus(6)
    g = np.column_stack([g, g[:, 70]])                                    # a copy of variant 70 as variant P
    z = zscores(g, np.append(freq, freq[70]), {70: 9.0}, rng)
    fit = susie.susie_rss(z, S.ld(g), N)
    members = set(fit.sets[0].variants.tolist())
    assert {70, P} <= members and fit.pip[70] == pytest.approx(fit.pip[P], abs=1e-6) and fit.pip[70] < 0.6


def test_the_credible_sets_follow_susies_rules():
    alpha = np.array([[0.6, 0.3, 0.06, 0.04], [0.25, 0.25, 0.25, 0.25], [0.6, 0.3, 0.06, 0.04]])
    r = np.array([[1.0, 0.9, 0.8, 0.1], [0.9, 1.0, 0.8, 0.1], [0.8, 0.8, 1.0, 0.1], [0.1, 0.1, 0.1, 1.0]])
    sets = susie.credible_sets(alpha, np.array([1.0, 1.0, 1.0]), r)
    assert len(sets) == 1                                                 # the copy is dropped, the impure one too
    assert sets[0].variants.tolist() == [0, 1, 2] and sets[0].coverage == pytest.approx(0.96)
    assert sets[0].purity == pytest.approx(0.8) and sets[0].effect == 0
    assert susie.credible_sets(alpha, np.array([0.0, 0.0, 0.0]), r) == []  # no effect kept, no set


def test_susie_refuses_input_that_does_not_fit():
    with pytest.raises(ValueError, match="for 3 variants"):
        susie.susie_rss(np.zeros(3), np.eye(2), 100)
    with pytest.raises(ValueError, match="greater than 1"):
        susie.susie_rss(np.zeros(2), np.eye(2), 1)
    with pytest.raises(ValueError, match="finite"):
        susie.susie_rss(np.array([np.nan, 0.0]), np.eye(2), 100)
