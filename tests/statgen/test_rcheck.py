"""rcheck.py: the same numbers through the R packages, where R has them; skipped where it does not."""

import numpy as np
import pytest

from variant2mechanism.statgen import abf, coloc, rcheck, susie
from variant2mechanism.statgen import simulate as S

HAS_COLOC, HAS_SUSIE = rcheck.available(("coloc",)), rcheck.available(("susieR",))


def simulated():
    rng = np.random.default_rng(17)
    freq = S.frequencies(120, rng)
    g1, g2 = S.genotypes(3000, freq, 0.97, rng), S.genotypes(400, freq, 0.97, rng)
    b1, s1 = S.association(g1, S.trait(g1, {50: S.effect_for_z(8, 3000, freq[50])}, rng))
    b2, s2 = S.association(g2, S.trait(g2, {50: S.effect_for_z(7, 400, freq[50])}, rng))
    return g1, b1, s1, b2, s2


def test_availability_is_a_plain_answer():
    assert rcheck.available(("a-package-that-does-not-exist",)) is False
    assert isinstance(HAS_COLOC, bool) and isinstance(HAS_SUSIE, bool)


@pytest.mark.skipif(not HAS_COLOC, reason="R with the coloc package is not installed")
def test_colocalisation_agrees_with_the_r_package():
    _, b1, s1, b2, s2 = simulated()
    ours = coloc.coloc_abf(abf.log_abf(b1, s1, abf.prior_sd("quant", 1.0)), abf.log_abf(b2, s2, abf.prior_sd("quant", 1.0)))
    assert np.allclose(ours.pp, rcheck.coloc_abf_r(b1, s1, b2, s2), atol=1e-8)


@pytest.mark.skipif(not HAS_SUSIE, reason="R with the susieR package is not installed")
def test_susie_agrees_with_the_r_package():
    g1, b1, s1, _, _ = simulated()
    ours = susie.susie_rss(b1 / s1, S.ld(g1), g1.shape[0])
    assert np.allclose(ours.pip, rcheck.susie_pip_r(b1 / s1, S.ld(g1), g1.shape[0]), atol=1e-3)
