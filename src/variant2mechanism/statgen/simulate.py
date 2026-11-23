"""A simulated locus with known causal variants, for the tests and to show what each method assumes.

Real summary statistics never come with the answer. Here the causal variants are chosen, so a method can be checked
against the truth: does the credible set hold the causal variant, does colocalisation say "shared" when the two
traits share it and "distinct" when they do not, does one signal hide another.

- Genotypes. Each person has two haplotypes. A haplotype is a chain along the variants: a standard normal value
  per variant, correlated `rho` with the value at the variant before it, and the minor allele is carried where the
  value falls below the variant's frequency quantile. Neighbouring variants are therefore in LD that decays with
  distance, as on a chromosome, and every variant has its own allele frequency.
- A trait is the sum of the chosen variants' effects (per copy of the minor allele) plus normal noise.
- Summary statistics are what a GWAS reports: for each variant alone, the slope of the trait on the genotype and
  its standard error.
- Two cohorts drawn with the same frequencies and the same `rho` (a GWAS and an eQTL study) share their LD
  pattern without sharing people, which is what colocalisation of two published studies assumes.
"""

import numpy as np
from scipy.stats import norm


def frequencies(p: int, rng: np.random.Generator, low: float = 0.05, high: float = 0.5) -> np.ndarray:
    """A minor allele frequency for each of `p` variants."""
    return rng.uniform(low, high, p)


def genotypes(n: int, freq: np.ndarray, rho: float, rng: np.random.Generator) -> np.ndarray:
    """Minor allele counts (0, 1 or 2) of `n` people at the variants with frequencies `freq`, in LD `rho` between
    neighbours on the latent scale."""
    if not 0 <= rho < 1:
        raise ValueError("rho lies in [0, 1)")
    p = len(freq)
    latent = np.empty((2 * n, p))
    latent[:, 0] = rng.standard_normal(2 * n)
    step = np.sqrt(1.0 - rho * rho)
    for j in range(1, p):
        latent[:, j] = rho * latent[:, j - 1] + step * rng.standard_normal(2 * n)
    carried = latent < norm.ppf(freq)
    return (carried[:n].astype(np.int8) + carried[n:].astype(np.int8))


def trait(g: np.ndarray, effects: dict[int, float], rng: np.random.Generator, noise_sd: float = 1.0) -> np.ndarray:
    """A trait for the people of `g`: `effects` maps a variant's index to its effect per copy of the minor allele."""
    y = rng.normal(0.0, noise_sd, g.shape[0])
    for j, b in effects.items():
        y = y + b * g[:, j]
    return y


def association(g: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """The effect estimate and its standard error for each variant, each tested alone (simple regression)."""
    n = g.shape[0]
    x = g - g.mean(axis=0)
    yc = y - y.mean()
    sxx = np.einsum("ij,ij->j", x, x)
    if np.any(sxx == 0):
        raise ValueError("a variant does not vary in this sample")
    beta = (x.T @ yc) / sxx
    residual = (float(yc @ yc) - beta * beta * sxx) / (n - 2)
    return beta, np.sqrt(residual / sxx)


def ld(g: np.ndarray) -> np.ndarray:
    """The correlation matrix of the variants in this sample: the in-sample LD that susie.susie_rss needs."""
    return np.corrcoef(g, rowvar=False)


def effect_for_z(z: float, n: int, freq: float, noise_sd: float = 1.0) -> float:
    """The effect per allele that gives an expected z-score of about `z` in `n` people at a variant with minor
    allele frequency `freq`."""
    return float(z * noise_sd / np.sqrt(n * 2.0 * freq * (1.0 - freq)))
