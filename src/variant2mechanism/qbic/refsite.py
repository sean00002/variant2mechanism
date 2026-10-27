"""Reference and alternate site strength from the local model weights (spec 1, section 7.2).

For each allele, the best coefficient among the k k-mers that contain the variant base, as a percentile of the
model's 4^k coefficients. High ref with low alt means the variant breaks a strong site.
"""

from functools import lru_cache
from pathlib import Path

import numpy as np
from qbic_selex.models import MODEL_SUFFIX, load_model

from ..config import load_config

VARIANT_INDEX = 10   # qbic-selex default context: 10 bp each side, variant at index 10


@lru_cache(maxsize=4)
def _index(weights_dir: str) -> dict[str, Path]:
    return {p.name[: -len(MODEL_SUFFIX)]: p for p in Path(weights_dir).rglob(f"*{MODEL_SUFFIX}")}


def model_path(model_id: str, weights_dir: str | Path | None = None) -> Path:
    weights_dir = str(weights_dir or load_config().path("data", "weights_dir"))
    try:
        return _index(weights_dir)[model_id]
    except KeyError:
        raise KeyError(f"no weights for {model_id} under {weights_dir}") from None


@lru_cache(maxsize=1024)
def _model(path: str):
    m = load_model(path)
    return m, np.sort(np.fromiter(m.complete.values(), dtype=np.float64, count=len(m.complete)))


def best_overlapping(complete: dict[str, float], seq: str, k: int, index: int = VARIANT_INDEX) -> float:
    seq = seq.upper()
    starts = range(max(0, index - k + 1), min(index, len(seq) - k) + 1)
    return max(float(complete[seq[i:i + k]]) for i in starts)


def site_strength(model_id: str, ref_sequence: str, alt_sequence: str, weights_dir: str | Path | None = None,
                  index: int = VARIANT_INDEX) -> dict:
    model, coefs = _model(str(model_path(model_id, weights_dir)))
    k = model.kmer_size

    def pct(v: float) -> float:
        return round(float(np.searchsorted(coefs, v, side="right") / len(coefs) * 100), 1)

    ref_best = best_overlapping(model.complete, ref_sequence, k, index)
    alt_best = best_overlapping(model.complete, alt_sequence, k, index)
    return {"ref_percentile": pct(ref_best), "alt_percentile": pct(alt_best), "k": k}
