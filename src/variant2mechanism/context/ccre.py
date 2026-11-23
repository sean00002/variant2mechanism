"""ENCODE cCRE at the variant (local registry) and its signal z-scores (SCREEN `cre_table`)."""

import gzip
from functools import lru_cache
from pathlib import Path

import pandas as pd

from ..config import load_config
from .base import Case, ToolResult, failed

SCREEN = "https://screen-beta-api.wenglab.org/dataws/cre_table"
CLASSES = {"PLS": "promoter-like", "pELS": "proximal enhancer-like", "dELS": "distal enhancer-like",
           "CA-CTCF": "chromatin accessible with CTCF", "CA-H3K4me3": "chromatin accessible with H3K4me3",
           "CA-TF": "chromatin accessible with TF binding", "CA": "chromatin accessible only", "TF": "TF binding only"}


@lru_cache(maxsize=1)
def _registry(path: str) -> dict[str, pd.DataFrame]:
    with gzip.open(path, "rt") as f:
        df = pd.read_csv(f, sep="\t", header=None, usecols=[0, 1, 2, 3, 9],
                         names=["chrom", "start", "end", "accession", "cls"])
    return {c: g.sort_values("start").reset_index(drop=True) for c, g in df.groupby("chrom")}


def local_ccre(chrom: str, pos: int, path: str | Path | None = None) -> dict | None:
    """Overlapping cCRE (BED is 0-based half-open) or else the nearest one, with its distance."""
    path = str(path or load_config().path("data", "ccres"))
    df = _registry(path).get(chrom)
    if df is None or df.empty:
        return None
    hit = df[(df.start < pos) & (df.end >= pos)]
    if not hit.empty:
        r = hit.iloc[0]
        return {"accession": r.accession, "class": r.cls, "start": int(r.start) + 1, "end": int(r.end), "distance": 0}
    dist = pd.concat([(df.start + 1 - pos).abs(), (df.end - pos).abs()], axis=1).min(axis=1)
    r = df.loc[dist.idxmin()]
    return {"accession": r.accession, "class": r.cls, "start": int(r.start) + 1, "end": int(r.end),
            "distance": int(dist.min())}


def ccre_lookup(case: Case, flank: int = 500, bed_path: str | Path | None = None) -> ToolResult:
    v = case.variant
    args = {"variant": v.key(), "flank_bp": flank}
    local = local_ccre(v.chrom, v.pos, bed_path)
    body = {"assembly": "GRCh38", "coord_chrom": v.chrom, "coord_start": v.pos - flank, "coord_end": v.pos + flank}
    r = case.http.post(SCREEN, body)
    lines = []
    if local is None:
        lines.append(f"No cCRE on {v.chrom} in the ENCODE v4 registry.")
    elif local["distance"] == 0:
        lines.append(f"The variant lies in cCRE {local['accession']} ({local['class']}: "
                     f"{CLASSES.get(local['class'], local['class'])}), {v.chrom}:{local['start']}-{local['end']}.")
    else:
        lines.append(f"No cCRE overlaps the variant; nearest is {local['accession']} ({local['class']}) "
                     f"{local['distance']} bp away.")
    if not r.ok:
        res = failed("ccre_lookup", args, "SCREEN cre_table", "epigenomic", r)
        res.summary = "\n".join(lines + [res.summary])
        res.full = {"local": local, "screen_error": r.error}
        return res
    cres = r.data.get("cres", [])
    lines.append(f"SCREEN: {len(cres)} cCREs within {flank} bp (max z-score across ENCODE biosamples):")
    for c in sorted(cres, key=lambda x: abs((x["start"] + x["len"] / 2) - v.pos))[:5]:
        here = c["start"] < v.pos <= c["start"] + c["len"]
        genes = ", ".join((c.get("genesallpc") or {}).get("pc", [])[:3])
        lines.append(f"{c['info']['accession']} {c['pct']}{' (contains the variant)' if here else ''}: "
                     f"DNase z {c['dnase_zscore']:.1f}, H3K27ac z {c['enhancer_zscore']:.1f}, "
                     f"H3K4me3 z {c['promoter_zscore']:.1f}, CTCF z {c['ctcf_zscore']:.1f}; nearby genes {genes}")
    lines.append("Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.")
    inside = local is not None and local["distance"] == 0
    return ToolResult("ccre_lookup", args, "\n".join(lines), {"local": local, "screen": cres},
                      "ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN", SCREEN, "epigenomic",
                      retrieved_utc=r.retrieved_utc, status="found" if inside else "tested_negative")
