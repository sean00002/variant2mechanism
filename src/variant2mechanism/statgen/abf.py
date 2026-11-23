"""Approximate Bayes factors per variant, and fine-mapping under the assumption of one causal variant.

Wakefield (2009): for a variant with effect estimate b and standard error s, and a prior N(0, W) on the true
effect, the Bayes factor for association against no association is

    ABF = sqrt(V / (V + W)) * exp(z^2 / 2 * W / (V + W)),    V = s^2,  z = b / s,

so with r = W / (V + W) its logarithm is (log(1 - r) + r * z^2) / 2. Everything here works with logarithms: at a
GWAS of a million people z^2 is in the thousands and the factor itself overflows.

The prior standard deviation follows the coloc R package, so that results can be compared with it: 0.15 standard
deviations of the trait for a quantitative trait, 0.2 on the log-odds scale for a case-control trait.

If a window holds exactly one causal variant and each variant is as likely as another before the data, the
posterior probability that variant i is the causal one is ABF_i / sum(ABF). The credible set is the smallest set of
variants whose probabilities add up to the coverage asked for. Nothing here uses LD: the assumption of one causal
variant stands in for it, and where it fails the set follows the strongest signal only.
"""

from typing import Literal

import numpy as np
from scipy.special import logsumexp

QUANT_PRIOR_SD = 0.15              # of the trait's standard deviation (coloc's default for a quantitative trait)
CC_PRIOR_SD = 0.2                  # on the log-odds scale (coloc's default for a case-control trait)
Kind = Literal["quant", "cc"]


def estimate_sdy(varbeta: np.ndarray, maf: np.ndarray, n: np.ndarray | float) -> float:
    """The trait's standard deviation, from the variance of the effect estimates: for a variant with allele
    frequency f in n people, var(b) is about sdY^2 / (2 n f (1 - f)). The estimate is the slope of 2 n f (1 - f)
    on 1 / var(b) through the origin, as coloc's sdY.est fits it."""
    varbeta, maf = np.asarray(varbeta, float), np.asarray(maf, float)
    n = np.broadcast_to(np.asarray(n, float), varbeta.shape)
    keep = np.isfinite(varbeta) & (varbeta > 0) & np.isfinite(maf) & (maf > 0) & (maf < 1) & np.isfinite(n)
    if not keep.any():
        raise ValueError("no variant has a variance, an allele frequency and a sample size to estimate sdY from")
    over = 1.0 / varbeta[keep]
    nvx = 2.0 * n[keep] * maf[keep] * (1.0 - maf[keep])
    slope = float(np.sum(nvx * over) / np.sum(over * over))
    return float(np.sqrt(slope))


def prior_sd(kind: Kind, sdy: float | None = None) -> float:
    """The standard deviation of the prior on a variant's true effect, on the scale the effects are given in."""
    if kind == "cc":
        return CC_PRIOR_SD
    if kind != "quant":
        raise ValueError(f"a trait is quant or cc, not {kind!r}")
    return QUANT_PRIOR_SD * (1.0 if sdy is None else float(sdy))


def log_abf(beta: np.ndarray, se: np.ndarray, sd_prior: float) -> np.ndarray:
    """The logarithm of Wakefield's approximate Bayes factor for each variant."""
    beta, se = np.asarray(beta, float), np.asarray(se, float)
    if beta.shape != se.shape:
        raise ValueError("beta and se differ in length")
    if not np.all(np.isfinite(beta)) or not np.all(np.isfinite(se)) or np.any(se <= 0):
        raise ValueError("every variant needs a finite effect and a positive standard error")
    v, w = se * se, float(sd_prior) ** 2
    r = w / (v + w)
    z = beta / se
    return 0.5 * (np.log1p(-r) + r * z * z)


def posterior(labf: np.ndarray) -> np.ndarray:
    """The probability that each variant is the causal one, given that exactly one variant of the window is."""
    labf = np.asarray(labf, float)
    return np.exp(labf - logsumexp(labf))


def credible_set(pp: np.ndarray, coverage: float = 0.95) -> np.ndarray:
    """The indices of the smallest set of variants whose probabilities reach `coverage`, most probable first."""
    pp = np.asarray(pp, float)
    if not 0 < coverage <= 1:
        raise ValueError("coverage lies in (0, 1]")
    order = np.argsort(-pp, kind="stable")
    reached = np.cumsum(pp[order])
    # the first position at which the running total reaches the coverage (the tolerance absorbs rounding at 1.0)
    size = int(np.searchsorted(reached, coverage - 1e-12, side="left")) + 1
    return order[:min(size, len(order))]
