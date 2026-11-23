"""The analysis of one window: a GWAS signal against the expression of every gene an eQTL dataset tests there.

Input is two tables of the same window (sumstats.gwas_frame and sumstats.eqtl_frame). Output is plain data that
can be saved as JSON and read by a person or by code:

- for the GWAS alone, the variants that could be the causal one if the window holds exactly one (abf.py): each
  variant's posterior probability and the 95% credible set;
- for each gene, the colocalisation of the GWAS signal with the gene's expression signal (coloc.py): PP.H0 to
  PP.H4, the variant that carries most of H4, the strongest variant of each trait, and how PP.H4 moves with the
  prior p12;
- for a variant of interest (`focus`), its own numbers in each of these, with the direction of both effects for
  the same allele.

Every setting that changes a number is in `Settings` and is written into the result. A gene is skipped, with the
reason, when too few variants are shared between the two tables for the comparison to mean anything.
"""

import csv
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy.stats import norm

from . import abf, coloc
from .sumstats import align

LN10 = float(np.log(10.0))


@dataclass(frozen=True)
class Settings:
    """What an analysis is run with. The priors and the coverage are coloc's defaults; a trait's kind is quant
    (effects in units of the trait) or cc (log odds ratios)."""
    p1: float = coloc.P1
    p2: float = coloc.P2
    p12: float = coloc.P12
    gwas_kind: abf.Kind = "quant"
    eqtl_kind: abf.Kind = "quant"
    coverage: float = 0.95
    min_variants: int = 50             # shared variants a gene needs to be compared


DEFAULTS = Settings()


def minus_log10_p(z: np.ndarray) -> np.ndarray:
    """-log10 of the two-sided p-value of each z-score, without underflow (a z of 90 has p near 1e-1700)."""
    return -(norm.logsf(np.abs(np.asarray(z, float))) + np.log(2.0)) / LN10


def _sd_prior(kind: abf.Kind, se: np.ndarray, maf: np.ndarray, n: np.ndarray) -> tuple[float, float | None]:
    """The prior standard deviation for a trait's effects, and the trait's estimated standard deviation when one
    was needed: a quantitative trait's is estimated from the variants that have a frequency and a sample size, and
    taken as one when none has."""
    if kind == "cc":
        return abf.prior_sd("cc"), None
    usable = np.isfinite(maf) & (maf > 0) & np.isfinite(n) & (n > 0)
    sdy = abf.estimate_sdy(se[usable] ** 2, maf[usable], n[usable]) if usable.any() else 1.0
    return abf.prior_sd("quant", sdy), sdy


def _variant(row: pd.Series, **more: Any) -> dict[str, Any]:
    return {"pos": int(row["pos"]), "rsid": str(row.get("rsid") or ""), **more}


def fine_map(gwas: pd.DataFrame, settings: Settings = DEFAULTS) -> dict[str, Any]:
    """The GWAS alone, under one causal variant in the window: each variant's posterior probability (added to the
    table as `pp`), and the credible set."""
    maf = (np.minimum(gwas["eaf"], 1.0 - gwas["eaf"]).to_numpy(float) if "eaf" in gwas.columns
           else np.full(len(gwas), np.nan))
    n = gwas["n"].to_numpy(float) if "n" in gwas.columns else np.full(len(gwas), np.nan)
    beta, se = gwas["beta"].to_numpy(float), gwas["se"].to_numpy(float)
    sd_prior, sdy = _sd_prior(settings.gwas_kind, se, maf, n)
    pp = abf.posterior(abf.log_abf(beta, se, sd_prior))
    members = abf.credible_set(pp, settings.coverage)
    table = gwas.assign(z=beta / se, pp=pp)
    return {"variants": int(len(gwas)), "sd_prior": sd_prior, "sdy": sdy, "coverage": settings.coverage,
            "credible_set": [_variant(table.iloc[i], pp=float(pp[i]), z=float(table["z"].iloc[i])) for i in members],
            "table": table}


def coloc_gene(shared: pd.DataFrame, settings: Settings = DEFAULTS) -> dict[str, Any]:
    """Colocalisation of the GWAS signal with one gene's expression signal, over the variants both tables hold
    (sumstats.align). `shared` gains the columns z_gwas, z_eqtl and snp_h4."""
    sd1, sdy1 = _sd_prior(settings.gwas_kind, shared["se_gwas"].to_numpy(float), shared["maf_gwas"].to_numpy(float),
                          shared["n_gwas"].to_numpy(float))
    sd2, sdy2 = _sd_prior(settings.eqtl_kind, shared["se_eqtl"].to_numpy(float), shared["maf_eqtl"].to_numpy(float),
                          shared["n_eqtl"].to_numpy(float))
    l1 = abf.log_abf(shared["beta_gwas"].to_numpy(float), shared["se_gwas"].to_numpy(float), sd1)
    l2 = abf.log_abf(shared["beta_eqtl"].to_numpy(float), shared["se_eqtl"].to_numpy(float), sd2)
    found = coloc.coloc_abf(l1, l2, settings.p1, settings.p2, settings.p12)
    table = shared.assign(z_gwas=shared["beta_gwas"] / shared["se_gwas"],
                          z_eqtl=shared["beta_eqtl"] / shared["se_eqtl"], snp_h4=found.snp_h4)
    top = table.iloc[int(np.argmax(found.snp_h4))]
    lead_gwas = table.iloc[int(np.argmax(np.abs(table["z_gwas"].to_numpy())))]
    lead_eqtl = table.iloc[int(np.argmax(np.abs(table["z_eqtl"].to_numpy())))]
    return {"variants": int(len(shared)), **found.as_dict(),
            "sd_prior": {"gwas": sd1, "eqtl": sd2}, "sdy": {"gwas": sdy1, "eqtl": sdy2},
            "shared_variant": _variant(top, share_of_h4=float(top["snp_h4"])),
            "lead_gwas": _variant(lead_gwas, z=float(lead_gwas["z_gwas"])),
            "lead_eqtl": _variant(lead_eqtl, z=float(lead_eqtl["z_eqtl"])),
            "sensitivity": [{"p12": p12, "PP.H3": h3, "PP.H4": h4}
                            for p12, h3, h4 in coloc.sensitivity(l1, l2, p1=settings.p1, p2=settings.p2)],
            "table": table}


def _focus(row: pd.Series | None, fields: tuple[str, ...]) -> dict[str, Any] | None:
    if row is None:
        return None
    return {"pos": int(row["pos"]), **{f: (str(row[f]) if f in ("ref", "alt", "rsid", "effect_allele", "other_allele")
                                           else float(row[f])) for f in fields if f in row.index}}


def analyse(gwas: pd.DataFrame, eqtl: pd.DataFrame, settings: Settings = DEFAULTS, focus: int | None = None,
            symbols: dict[str, str] | None = None) -> dict[str, Any]:
    """The whole window: the GWAS fine-mapped alone, then compared with each gene of `eqtl`. `focus` is the
    position of a variant of interest; `symbols` maps the eQTL table's gene ids to names for the result. Tables are
    returned under "tables" (the GWAS under "gwas", each compared gene under its id) for plotting, apart from the
    numbers, which `summary` turns into JSON."""
    symbols = symbols or {}
    mapped = fine_map(gwas, settings)
    gwas_table = mapped.pop("table")
    at = gwas_table[gwas_table["pos"] == focus] if focus is not None else gwas_table.iloc[0:0]
    in_set = {v["pos"] for v in mapped["credible_set"]}
    result: dict[str, Any] = {
        "settings": asdict(settings), "focus": focus,
        "gwas": {**mapped, "focus": ({**_focus(at.iloc[0], ("rsid", "effect_allele", "other_allele", "beta", "se",
                                                           "z", "pp")), "in_credible_set": focus in in_set}
                                     if len(at) == 1 else None)},
        "genes": [], "skipped": []}
    tables: dict[str, pd.DataFrame] = {"gwas": gwas_table}
    for gene, rows in eqtl.groupby("gene", sort=True):
        shared = align(gwas, rows)
        name = symbols.get(str(gene), str(gene))
        if len(shared) < settings.min_variants:
            result["skipped"].append({"gene": str(gene), "symbol": name, "shared_variants": int(len(shared)),
                                      "why": f"fewer than {settings.min_variants} variants are in both tables"})
            continue
        found = coloc_gene(shared, settings)
        table = found.pop("table")
        tables[str(gene)] = table
        here = table[table["pos"] == focus] if focus is not None else table.iloc[0:0]
        result["genes"].append({"gene": str(gene), "symbol": name, **found,
                                "focus": _focus(here.iloc[0], ("ref", "alt", "rsid", "beta_gwas", "z_gwas",
                                                               "beta_eqtl", "z_eqtl", "snp_h4"))
                                if len(here) == 1 else None})
    result["genes"].sort(key=lambda g: -g["PP.H4"])
    result["tables"] = tables
    return result


def summary(result: dict[str, Any]) -> dict[str, Any]:
    """The result without its tables: what is saved as JSON."""
    return {k: v for k, v in result.items() if k != "tables"}


def symbols_from_hgnc(path: str) -> dict[str, str]:
    """Ensembl gene id to approved symbol, from HGNC's complete set (tab-separated); empty when the file is absent."""
    if not Path(path).exists():
        return {}
    with open(path, newline="") as f:
        return {row["ensembl_gene_id"]: row["symbol"] for row in csv.DictReader(f, delimiter="\t")
                if row.get("status") == "Approved" and row.get("ensembl_gene_id")}
