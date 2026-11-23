"""The sum of single effects model (SuSiE) fitted to z-scores and an LD matrix, for a window with several signals.

Wang et al. (2020) write the effects of the p variants of a window as a sum of L "single effects", each a vector
with exactly one non-zero entry. Each single effect l has a posterior over which variant it is (alpha[l]) and how
large it is there (mu[l]); they are fitted one at a time, each to what the others leave unexplained, until the fit
stops improving. Zou et al. (2022) fit the same model from summary statistics: with z-scores z from n people and
the correlation matrix R of the variants in those people, the sufficient statistics are

    X'X = (n - 1) R,    X'y = sqrt(n - 1) z~,    y'y = n - 1,    z~ = z * sqrt((n - 1) / (z^2 + n - 2)),

for genotypes and a trait scaled to variance one. This file follows susieR's susie_rss with a sample size given
and its defaults: L = 10, residual variance fixed at one, each effect's prior variance estimated by maximum
likelihood and set to zero when that does not beat no effect, convergence when the objective gains less than 1e-3.

What comes out:

    pip      per variant, the probability that it is causal: 1 - prod over the effects kept of (1 - alpha[l, j])
    sets     per effect kept, the smallest set of variants whose alpha adds up to the coverage (95%), dropped when
             two of its variants correlate below 0.5 (the set then does not point at one signal)

R must be the correlation in the sample the z-scores come from. With a reference panel instead, and a GWAS large
enough to make the z-scores precise, the mismatch shows up as signals that are not there. This package therefore
calls susie_rss only on simulated data, where R is computed from the same genotypes (simulate.py).
"""

from typing import NamedTuple

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.special import logsumexp

L_DEFAULT = 10
SCALED_PRIOR_VARIANCE = 0.2        # the starting prior variance of an effect, as a share of the trait's variance
COVERAGE, MIN_ABS_CORR = 0.95, 0.5
MAX_ITER, TOL, PRIOR_TOL = 100, 1e-3, 1e-9
_EPS = float(np.sqrt(np.finfo(float).eps))


class CredibleSet(NamedTuple):
    """One effect's credible set: the variants (indices, most probable first), what their alpha adds up to, and
    the smallest absolute correlation between two of them."""
    effect: int
    variants: np.ndarray
    coverage: float
    purity: float


class Susie(NamedTuple):
    alpha: np.ndarray                  # (L, p): which variant each effect is
    mu: np.ndarray                     # (L, p): the effect's posterior mean, were it that variant
    prior_variance: np.ndarray         # (L,): 0 for an effect the data did not ask for
    pip: np.ndarray                    # (p,)
    sets: list[CredibleSet]
    elbo: list[float]
    converged: bool


def _lbf(v: float, shat2: np.ndarray, t2: np.ndarray) -> np.ndarray:
    """The log Bayes factor of each variant for one effect with prior variance v (t2: the squared z of the fit)."""
    if v <= 0:
        return np.zeros_like(shat2)
    return 0.5 * np.log(shat2 / (v + shat2)) + 0.5 * t2 * (v / (v + shat2))


def _loglik(v: float, shat2: np.ndarray, t2: np.ndarray, log_prior: np.ndarray) -> float:
    return float(logsumexp(_lbf(v, shat2, t2) + log_prior))


def _prior_variance(v_init: float, shat2: np.ndarray, t2: np.ndarray, log_prior: np.ndarray) -> float:
    """The prior variance that maximises the single-effect likelihood (susieR's "optim" on the log scale), kept at
    its previous value when the search does worse, and set to zero when it does not beat no effect at all."""
    found = minimize_scalar(lambda lv: -_loglik(float(np.exp(lv)), shat2, t2, log_prior), bounds=(-30.0, 15.0),
                            method="bounded")
    v = float(np.exp(found.x))
    if _loglik(v, shat2, t2, log_prior) < _loglik(v_init, shat2, t2, log_prior):
        v = v_init
    return 0.0 if _loglik(0.0, shat2, t2, log_prior) >= _loglik(v, shat2, t2, log_prior) else v


def _single_effect(xtr: np.ndarray, d: np.ndarray, v: float, sigma2: float, log_prior: np.ndarray):
    """One single-effect regression on what the other effects leave: (alpha, mu, mu2, v, the model's log Bayes
    factor)."""
    betahat, shat2 = xtr / d, sigma2 / d
    t2 = betahat * betahat / shat2
    v = _prior_variance(v, shat2, t2, log_prior)
    lpo = _lbf(v, shat2, t2) + log_prior
    lbf_model = float(logsumexp(lpo))
    alpha = np.exp(lpo - lbf_model)
    post_var = 1.0 / (1.0 / v + d / sigma2) if v > 0 else np.zeros_like(d)
    mu = post_var * xtr / sigma2
    return alpha, mu, post_var + mu * mu, v, lbf_model


def credible_sets(alpha: np.ndarray, prior_variance: np.ndarray, r: np.ndarray, coverage: float = COVERAGE,
                  min_abs_corr: float = MIN_ABS_CORR) -> list[CredibleSet]:
    """The credible set of each effect whose prior variance is not zero, without repeats, purest first."""
    found: dict[frozenset[int], CredibleSet] = {}
    for effect in np.flatnonzero(prior_variance > PRIOR_TOL):
        order = np.argsort(-alpha[effect], kind="stable")
        size = int(np.sum(np.cumsum(alpha[effect][order]) < coverage)) + 1
        members = order[:size]
        key = frozenset(int(i) for i in members)
        if key in found:
            continue
        sub = np.abs(r[np.ix_(members, members)])
        purity = 1.0 if size == 1 else float(sub[np.triu_indices(size, 1)].min())
        if purity >= min_abs_corr:
            found[key] = CredibleSet(int(effect), members, float(alpha[effect][members].sum()), purity)
    return sorted(found.values(), key=lambda s: -s.purity)


def susie_rss(z: np.ndarray, r: np.ndarray, n: float, n_effects: int = L_DEFAULT, coverage: float = COVERAGE,
              min_abs_corr: float = MIN_ABS_CORR, max_iter: int = MAX_ITER, tol: float = TOL) -> Susie:
    """Fit the model to z-scores `z` of p variants and their correlation matrix `r` in the same `n` people."""
    z, r = np.asarray(z, float), np.asarray(r, float)
    p = len(z)
    if r.shape != (p, p):
        raise ValueError(f"R is {r.shape[0]} x {r.shape[1]} for {p} variants")
    if not n > 1:
        raise ValueError("n must be greater than 1")
    if not np.all(np.isfinite(z)) or not np.all(np.isfinite(r)):
        raise ValueError("z and R must be finite")
    r = (r + r.T) / 2.0
    z = z * np.sqrt((n - 1.0) / (z * z + n - 2.0))
    xtx, xty, yty = (n - 1.0) * r, np.sqrt(n - 1.0) * z, n - 1.0
    d = np.diag(xtx).copy()
    sigma2 = 1.0
    log_prior = np.log(np.full(p, 1.0 / p) + _EPS)
    alpha = np.full((n_effects, p), 1.0 / p)
    mu, mu2 = np.zeros((n_effects, p)), np.zeros((n_effects, p))
    v = np.full(n_effects, SCALED_PRIOR_VARIANCE)
    kl = np.zeros(n_effects)
    xtxr = np.zeros(p)
    elbo, converged = [-np.inf], False
    for _ in range(max_iter):
        for effect in range(n_effects):
            xtxr -= xtx @ (alpha[effect] * mu[effect])
            xtr = xty - xtxr
            alpha[effect], mu[effect], mu2[effect], v[effect], lbf_model = _single_effect(
                xtr, d, float(v[effect]), sigma2, log_prior)
            b, b2 = alpha[effect] * mu[effect], alpha[effect] * mu2[effect]
            kl[effect] = -lbf_model - 0.5 / sigma2 * (-2.0 * float(b @ xtr) + float(d @ b2))
            xtxr += xtx @ b
        b = alpha * mu
        betabar = b.sum(axis=0)
        er2 = (yty - 2.0 * float(betabar @ xty) + float(betabar @ xtx @ betabar) - float(np.sum((b @ xtx) * b))
               + float(np.sum(d * (alpha * mu2))))
        elbo.append(-n / 2.0 * np.log(2.0 * np.pi * sigma2) - er2 / (2.0 * sigma2) - float(kl.sum()))
        if elbo[-1] - elbo[-2] < tol:
            converged = True
            break
    kept = v > PRIOR_TOL
    pip = 1.0 - np.prod(1.0 - alpha[kept], axis=0) if kept.any() else np.zeros(p)
    return Susie(alpha, mu, v, pip, credible_sets(alpha, v, r, coverage, min_abs_corr), elbo[1:], converged)
