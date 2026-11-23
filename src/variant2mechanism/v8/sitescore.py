"""Site strength in overlapping k-mer fashion (v8).

A QBiC-SELEX model scores a sequence as the sum of its k-mer coefficients, and the coefficients of overlapping k-mers
are collinear (in the ETV5 model CCGGAA is -3.28 and its neighbour CCCGGA +3.56), so a single coefficient is not an
affinity. For each allele the score is the sum over every overlapping k-mer in the 21-bp context QBiC-SELEX extracts
(10 bp each side of the variant), as a percentile of the same sum over uniform random 21-mers: the background an
HT-SELEX library starts from. The score is shown in the screen; it never filters or orders candidates.
"""

from functools import lru_cache

import numpy as np

from ..qbic.refsite import _model, model_path

BASES = "ACGT"
N_BACKGROUND = 200_000


def _coefficients(model) -> np.ndarray:
    a = np.empty(4 ** model.kmer_size)
    for kmer, value in model.complete.items():
        i = 0
        for c in kmer:
            i = i * 4 + BASES.index(c)
        a[i] = value
    return a


def _sums(coef: np.ndarray, x: np.ndarray, k: int) -> np.ndarray:
    """Sum of coefficients over every overlapping k-mer of each row of `x` (bases as 0-3)."""
    n = x.shape[1] - k + 1
    idx = np.zeros((x.shape[0], n), dtype=np.int64)
    for j in range(k):
        idx = idx * 4 + x[:, j:j + n]
    return coef[idx].sum(axis=1)


@lru_cache(maxsize=1024)
def _background(model_id: str, length: int, n: int = N_BACKGROUND) -> tuple[np.ndarray, np.ndarray, int]:
    model, _ = _model(str(model_path(model_id)))
    coef = _coefficients(model)
    rng = np.random.default_rng(0)              # fixed: the same percentile for the same site, run after run
    return coef, np.sort(_sums(coef, rng.integers(0, 4, size=(n, length)), model.kmer_size)), model.kmer_size


def site_score(model_id: str, ref_seq: str, alt_seq: str) -> dict:
    """Percentiles of the ref and alt context sums against random sequences of the same length."""
    ref_seq, alt_seq = ref_seq.upper(), alt_seq.upper()
    if len(ref_seq) != len(alt_seq) or set(ref_seq + alt_seq) - set(BASES):
        return {"error": "the context holds bases other than A, C, G and T"}
    coef, bg, k = _background(model_id, len(ref_seq))
    x = np.array([[BASES.index(c) for c in s] for s in (ref_seq, alt_seq)])
    ref, alt = (float(np.searchsorted(bg, v, side="right") / len(bg) * 100) for v in _sums(coef, x, k))
    return {"ref": round(ref, 1), "alt": round(alt, 1), "k": k, "window_bp": len(ref_seq)}


def creates_site(score: dict | None, binds_more: str | None, strong: float = 95.0, weak: float = 90.0) -> bool:
    """The allele that binds more reaches `strong` and the other stays below `weak`: the variant creates the site."""
    if not score or "ref" not in score or binds_more not in ("ref", "alt"):
        return False
    other = "alt" if binds_more == "ref" else "ref"
    return score[binds_more] >= strong and score[other] < weak
