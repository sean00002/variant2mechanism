"""Colocalisation of two traits in one window, from each trait's approximate Bayes factors (coloc.abf).

Giambartolomei et al. (2014). With at most one causal variant per trait in the window, there are five cases:

    H0   neither trait has a causal variant here
    H1   only the first has one
    H2   only the second has one
    H3   both have one, and they are different variants
    H4   both have one, and it is the same variant

Each variant has prior probability p1 of being causal for the first trait only, p2 for the second only and p12 for
both. With l1 and l2 the two traits' log Bayes factors per variant, the evidence for each case is

    H1: p1 * sum(exp(l1))                H2: p2 * sum(exp(l2))
    H3: p1 * p2 * (sum(exp(l1)) * sum(exp(l2)) - sum(exp(l1 + l2)))
    H4: p12 * sum(exp(l1 + l2))

relative to 1 for H0, and the posterior probabilities are these divided by their total. The defaults are those of
the coloc R package (1e-4, 1e-4, 1e-5). Given H4, variant i is the shared one with probability
exp(l1_i + l2_i) / sum(exp(l1 + l2)).

What the result means: a high PP.H4 says the two association signals are explained by one variant. It does not say
the first trait acts through the second, and with several signals per trait in the window the assumption fails
(susie.py handles that, given LD from the GWAS sample).
"""

from typing import NamedTuple

import numpy as np
from scipy.special import logsumexp

P1, P2, P12 = 1e-4, 1e-4, 1e-5
HYPOTHESES = ("H0", "H1", "H2", "H3", "H4")


class Coloc(NamedTuple):
    """The posterior probabilities of H0 to H4, each variant's probability of being the shared variant given H4,
    the priors used and the number of variants."""
    pp: np.ndarray
    snp_h4: np.ndarray
    priors: tuple[float, float, float]
    n_variants: int

    @property
    def h3(self) -> float:
        return float(self.pp[3])

    @property
    def h4(self) -> float:
        return float(self.pp[4])

    def as_dict(self) -> dict[str, float]:
        return {f"PP.{name}": float(p) for name, p in zip(HYPOTHESES, self.pp, strict=True)}


def _logdiff(a: float, b: float) -> float:
    """log(exp(a) - exp(b)); minus infinity when the difference is not positive (one variant: H3 is impossible)."""
    if not a > b:
        return -np.inf
    return float(a + np.log1p(-np.exp(b - a)))


def coloc_abf(labf1: np.ndarray, labf2: np.ndarray, p1: float = P1, p2: float = P2, p12: float = P12) -> Coloc:
    """Colocalisation of two traits from their log approximate Bayes factors over the same variants, in the same
    order (abf.log_abf for each)."""
    l1, l2 = np.asarray(labf1, float), np.asarray(labf2, float)
    if l1.shape != l2.shape or l1.ndim != 1 or not len(l1):
        raise ValueError("the two traits need Bayes factors for the same, non-empty list of variants")
    if not (0 < p1 < 1 and 0 < p2 < 1 and 0 < p12 < 1):
        raise ValueError("the priors lie in (0, 1)")
    both = l1 + l2
    s1, s2, s12 = float(logsumexp(l1)), float(logsumexp(l2)), float(logsumexp(both))
    cases = np.array([0.0,
                      np.log(p1) + s1,
                      np.log(p2) + s2,
                      np.log(p1) + np.log(p2) + _logdiff(s1 + s2, s12),
                      np.log(p12) + s12])
    return Coloc(np.exp(cases - logsumexp(cases)), np.exp(both - s12), (p1, p2, p12), len(l1))


def sensitivity(labf1: np.ndarray, labf2: np.ndarray, p12s: tuple[float, ...] = (1e-8, 1e-7, 1e-6, 1e-5, 1e-4),
                p1: float = P1, p2: float = P2) -> list[tuple[float, float, float]]:
    """(p12, PP.H3, PP.H4) over a range of the prior that the two traits share a causal variant: how much the
    conclusion rests on that prior, which the data cannot inform."""
    out = []
    for p12 in p12s:
        found = coloc_abf(labf1, labf2, p1, p2, p12)
        out.append((p12, found.h3, found.h4))
    return out
