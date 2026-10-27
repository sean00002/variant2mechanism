"""Local expression and CRISPR dependency: `tf_expression` and `gene_dependency` (spec 2, section 6)."""

import re
from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

from ..config import load_config
from ..qbic.expression import ContextError, _depmap_binary, depmap_symbols
from .base import Case, ToolResult, failed

DEPENDENT = -0.5          # gene effect below which a line is called dependent (DepMap convention)
COMMON_ESSENTIAL_LINE = ("common-essential in DepMap: a strong knockout effect here is not evidence for a "
                         "lineage-specific role")
_HEADER = re.compile(r"^(.*) \((\d+)\)$")


def tf_expression(case: Case, tf: str, context: str | None = None) -> ToolResult:
    from ..qbic.expression import get_expression
    from ..qbic.registry import get_registry
    ctx_text = context or case.expression_context
    args = {"tf": tf, "context": ctx_text}
    name = get_registry().resolve_tf(tf)
    if name["status"] != "ok":
        cands = ", ".join(c["symbol"] for c in name["candidates"]) or "none"
        return failed("tf_expression", args, "local DepMap/GTEx", "expression",
                      message=f"{tf}: {name['status']} (candidates: {cands})")
    sym = name["symbol"]
    try:
        e = get_expression().tf_expression([sym], ctx_text)[sym]
    except ContextError as err:
        return failed("tf_expression", args, "local DepMap/GTEx", "expression", message=str(err))
    if e.get("tpm") is None:
        summary = f"{sym}: no expression value ({e.get('note') or e['source']})."
    else:
        summary = (f"{sym} in {e['source']}: {e['tpm']} TPM, rank {e['rank_among_tfs']} of {e['n_tfs']} TFs "
                   f"(1 = highest); this context is at the {e['percentile_across_contexts']}th percentile of "
                   f"{sym} across all {'DepMap lines' if 'DepMap' in e['source'] else 'GTEx tissues'}"
                   + (f"; median of {e['n_lines']} lines" if "n_lines" in e else "") + ".")
    if name["notes"]:
        summary += " Note: " + " ".join(name["notes"])
    return ToolResult("tf_expression", args, summary, {"symbol": sym, **e}, "DepMap expression / GTEx v8 medians",
                      "local files", "expression")


# -- gene dependency ---------------------------------------------------------------------------------------


def _key(header: str) -> tuple[str, str | None]:
    m = _HEADER.match(header.strip())
    return (m.group(1), m.group(2)) if m else (header.strip(), None)


@lru_cache(maxsize=2)
def common_essentials(path: str) -> tuple[set[str], set[str]]:
    """Entrez IDs and symbols of DepMap's inferred common-essential genes."""
    col = pd.read_csv(path).iloc[:, 0].dropna().astype(str)
    entrez, symbols = set(), set()
    for h in col:
        sym, eid = _key(h)
        symbols.add(sym.upper())
        if eid:
            entrez.add(eid)
    return entrez, symbols


def is_common_essential(gene: str, entrez: str | None, path: str | Path) -> bool:
    """Match by Entrez ID first, then by symbol."""
    ids, symbols = common_essentials(str(path))
    return bool(entrez and str(entrez) in ids) or gene.upper() in symbols


@lru_cache(maxsize=1)
def _effects() -> pd.DataFrame:
    cfg = load_config()
    from ..qbic.registry import get_registry
    values, rows, cols = _depmap_binary(cfg.path("data", "depmap_crispr"), cfg.path("data", "depmap_cache"))
    df = pd.DataFrame(values, index=rows, columns=depmap_symbols(cols, get_registry()))
    return df.loc[:, ~df.columns.duplicated()]


@lru_cache(maxsize=1)
def _models() -> pd.DataFrame:
    cfg = load_config()
    return pd.read_csv(cfg.path("data", "depmap_models"), low_memory=False,
                       usecols=["ModelID", "CellLineName", "OncotreeLineage", "OncotreeSubtype"]
                       ).drop_duplicates("ModelID").set_index("ModelID")


def lineage_lines(context: str | None, models: pd.DataFrame) -> tuple[str | None, list[str], str | None]:
    """(lineage, lines of that lineage, the context's own line) from a DepMap expression context."""
    if not context or not context.startswith("DepMap:"):
        return None, [], None
    body = context[len("DepMap:"):].strip()
    if body.startswith("subtype="):
        sub = re.sub(r"\s*\([^()]*\)\s*$", "", body[len("subtype="):]).strip()
        lin = models.loc[models.OncotreeSubtype == sub, "OncotreeLineage"].mode()
        lineage = lin.iloc[0] if len(lin) else None
        return lineage, models.index[models.OncotreeSubtype == sub].tolist(), None
    m = re.match(r"(ACH-\d+)", body)
    if not m or m.group(1) not in models.index:
        return None, [], None
    line = m.group(1)
    lineage = models.at[line, "OncotreeLineage"]
    return lineage, models.index[models.OncotreeLineage == lineage].tolist(), line


def gene_dependency(case: Case, gene: str, effects: pd.DataFrame | None = None, models: pd.DataFrame | None = None,
                    essentials_path: str | Path | None = None, entrez: str | None = None) -> ToolResult:
    """CRISPR gene effect for the case's lineage, and whether the gene is common-essential."""
    args = {"gene": gene, "context": case.expression_context}
    cfg = load_config()
    effects = _effects() if effects is None else effects
    models = _models() if models is None else models
    essentials_path = essentials_path or cfg.path("data", "depmap_common_essentials")
    if entrez is None:
        from ..qbic.registry import get_registry
        reg = get_registry()
        entrez = next((e for e, s in reg.entrez_to_symbol.items() if s == gene), None)
    if gene not in effects.columns:
        return failed("gene_dependency", args, "DepMap CRISPR", "expression", message=f"{gene} not in the matrix")
    col = effects[gene].dropna()
    lineage, lines, own = lineage_lines(case.expression_context, models)
    in_lin = col[col.index.isin(lines)]
    parts = [f"DepMap CRISPR gene effect for {gene} (0 = no effect, -1 = median common-essential; "
             f"< {DEPENDENT} called dependent)."]
    if own and own in col.index:
        parts.append(f"{models.at[own, 'CellLineName']} ({own}): {col[own]:.2f}.")
    if len(in_lin):
        parts.append(f"{lineage} lineage, {len(in_lin)} lines: median {np.median(in_lin):.2f}, "
                     f"{(in_lin < DEPENDENT).mean() * 100:.0f}% dependent.")
    elif lineage is None:
        parts.append("No DepMap lineage for this case's context; all lines only.")
    parts.append(f"All {len(col)} lines: median {np.median(col):.2f}, {(col < DEPENDENT).mean() * 100:.0f}% dependent.")
    essential = is_common_essential(gene, entrez, essentials_path)
    if essential:
        parts.append(COMMON_ESSENTIAL_LINE + ".")
    full = {"gene": gene, "entrez": entrez, "lineage": lineage, "line": own,
            "line_effect": float(col[own]) if own and own in col.index else None,
            "lineage_median": float(np.median(in_lin)) if len(in_lin) else None, "lineage_n": int(len(in_lin)),
            "all_median": float(np.median(col)), "common_essential": essential}
    return ToolResult("gene_dependency", args, " ".join(parts), full,
                      "DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3)",
                      "local files", "expression")
