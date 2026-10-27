"""TF expression in a context, from local DepMap and GTEx files (spec 1, section 7.1).

Contexts: `DepMap:ACH-000971 (HCT 116)`, `DepMap:subtype=Glioblastoma (...)`, `GTEx:<tissue> (...)`, or
`none (...)`/empty. The bracketed note is for people and is ignored. DepMap values are log2(TPM + 1).
"""

import gzip
import json
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

from ..config import load_config
from .registry import Registry, get_registry


class ContextError(ValueError):
    """Raised for an expression context that names no known line, subtype or tissue."""


@dataclass(frozen=True)
class Context:
    kind: str            # depmap_line, depmap_subtype, gtex, none
    value: str | None    # ModelID, subtype or tissue
    text: str            # as given

    def describe(self) -> str:
        if self.kind == "none":
            return "none: expression filter skipped"
        return {"depmap_line": "DepMap line", "depmap_subtype": "DepMap subtype median",
                "gtex": "GTEx tissue median"}[self.kind] + f" {self.value}"


_NOTE = re.compile(r"\s*\([^()]*\)\s*$")


def _candidates(text: str) -> list[str]:
    """The text, then the text with a trailing bracketed note removed (tissue names can hold brackets)."""
    text = text.strip()
    stripped = _NOTE.sub("", text).strip()
    return [text] if stripped == text else [text, stripped]


def tpm_from_log(x):
    """DepMap stores log2(TPM + 1)."""
    return np.power(2.0, x) - 1.0


class Expression:
    """DepMap matrix (lines x genes, TPM) and GTEx medians (genes x tissues, TPM), keyed by HGNC symbol."""

    def __init__(self, depmap_tpm: pd.DataFrame, depmap_subtype: pd.Series, gtex_tpm: pd.DataFrame, tfs: set[str]):
        self.depmap = depmap_tpm
        self.subtype = depmap_subtype.reindex(depmap_tpm.index)
        self.gtex = gtex_tpm
        self.tfs = tfs

    def parse(self, text: str | None) -> Context:
        if text is None or not str(text).strip() or str(text).strip().lower().startswith("none"):
            return Context("none", None, str(text or ""))
        text = str(text).strip()
        if text.startswith("DepMap:subtype="):
            body = text[len("DepMap:subtype="):]
            for c in _candidates(body):
                if (self.subtype == c).any():
                    return Context("depmap_subtype", c, text)
            raise ContextError(f"No DepMap expression lines have OncotreeSubtype '{_candidates(body)[-1]}'.")
        if text.startswith("DepMap:"):
            body = text[len("DepMap:"):]
            m = re.match(r"(ACH-\d+)", body.strip())
            if m and m.group(1) in self.depmap.index:
                return Context("depmap_line", m.group(1), text)
            raise ContextError(f"DepMap line '{body.strip()}' is not in the expression matrix.")
        if text.startswith("GTEx:"):
            body = text[len("GTEx:"):]
            for c in _candidates(body):
                if c in self.gtex.columns:
                    return Context("gtex", c, text)
            raise ContextError(f"GTEx has no tissue '{_candidates(body)[-1]}'.")
        raise ContextError(f"Unknown expression context '{text}'. Use DepMap:<ModelID>, "
                           "DepMap:subtype=<Oncotree subtype>, GTEx:<tissue> or none.")

    def vector(self, ctx: Context) -> tuple[pd.Series, pd.DataFrame, int | None]:
        """TPM by gene for the context, the matrix of all contexts (columns = contexts), and n_lines."""
        if ctx.kind == "depmap_line":
            return self.depmap.loc[ctx.value], self.depmap.T, None
        if ctx.kind == "depmap_subtype":
            lines = self.subtype.index[self.subtype == ctx.value]
            return self.depmap.loc[lines].median(axis=0), self.depmap.T, len(lines)
        if ctx.kind == "gtex":
            return self.gtex[ctx.value], self.gtex, None
        raise ContextError("No expression data for context 'none'.")

    def tf_expression(self, symbols: list[str], context: str | Context | None) -> dict:
        ctx = context if isinstance(context, Context) else self.parse(context)
        if ctx.kind == "none":
            return {s: {"tpm": None, "source": ctx.describe()} for s in symbols}
        vec, everything, n_lines = self.vector(ctx)
        tf_vals = vec[vec.index.isin(self.tfs)].dropna()
        ranks = tf_vals.rank(ascending=False, method="min")
        out = {}
        for s in symbols:
            if s not in vec.index or pd.isna(vec.get(s)):
                out[s] = {"tpm": None, "source": ctx.describe(), "note": "gene not in this dataset"}
                continue
            tpm = float(vec[s])
            row = everything.loc[s].dropna().to_numpy()
            rec = {"tpm": round(tpm, 2),
                   "rank_among_tfs": int(ranks[s]) if s in ranks.index else None,
                   "n_tfs": int(len(tf_vals)),
                   "percentile_across_contexts": round(float((row <= tpm).mean() * 100), 1),
                   "source": ctx.describe()}
            if n_lines is not None:
                rec["n_lines"] = n_lines
            out[s] = rec
        return out


# -- loading the real files ------------------------------------------------------------------------------------


def _depmap_binary(csv_path: Path, cache_dir: Path) -> tuple[np.ndarray, list[str], list[str]]:
    """Parse the DepMap CSV once; keep a float32 copy and its labels outside Dropbox."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    stem = csv_path.stem
    npy, meta = cache_dir / f"{stem}.npy", cache_dir / f"{stem}.json"
    if npy.exists() and meta.exists():
        m = json.loads(meta.read_text())
        if m["source_size"] == csv_path.stat().st_size:
            return np.load(npy), m["rows"], m["columns"]
    df = pd.read_csv(csv_path, index_col=0)
    np.save(npy, df.to_numpy(dtype=np.float32))
    meta.write_text(json.dumps({"source": str(csv_path), "source_size": csv_path.stat().st_size,
                                "rows": df.index.tolist(), "columns": df.columns.tolist()}))
    return df.to_numpy(dtype=np.float32), df.index.tolist(), df.columns.tolist()


_HEADER = re.compile(r"^(.*) \((\d+)\)$")


def depmap_symbols(columns: list[str], reg: Registry) -> list[str]:
    """`SYMBOL (EntrezID)` to HGNC symbol: by Entrez ID, then by symbol."""
    out = []
    for c in columns:
        m = _HEADER.match(c)
        sym, entrez = (m.group(1), m.group(2)) if m else (c, None)
        out.append(reg.entrez_to_symbol.get(entrez) or reg.canonical(sym))
    return out


def load_gtex(path: Path, reg: Registry) -> pd.DataFrame:
    with gzip.open(path, "rt") as f:
        df = pd.read_csv(f, sep="\t", skiprows=2)
    ens = df.pop("Name").str.split(".").str[0]
    desc = df.pop("Description")
    df.index = [reg.hgnc_by_ensembl.get(e) or reg.canonical(d) for e, d in zip(ens, desc, strict=True)]
    return df[~df.index.duplicated()]


@lru_cache(maxsize=1)
def get_expression() -> Expression:
    cfg = load_config()
    reg = get_registry()
    values, rows, cols = _depmap_binary(cfg.path("data", "depmap_expression"), cfg.path("data", "depmap_cache"))
    depmap = pd.DataFrame(tpm_from_log(values), index=rows, columns=depmap_symbols(cols, reg))
    depmap = depmap.loc[:, ~depmap.columns.duplicated()]
    models = pd.read_csv(cfg.path("data", "depmap_models"), usecols=["ModelID", "OncotreeSubtype"], low_memory=False)
    subtype = models.drop_duplicates("ModelID").set_index("ModelID")["OncotreeSubtype"]
    return Expression(depmap, subtype, load_gtex(cfg.path("data", "gtex"), reg), reg.lambert_tfs)


def tf_expression(symbols: list[str], context: str | None) -> dict:
    return get_expression().tf_expression(symbols, context)
