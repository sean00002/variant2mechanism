"""The regional figure of one window's analysis: the GWAS on top, then one panel per gene, on one shared position axis.

Each panel shows every variant's -log10 p against its position. Panels are stacked rather than overlaid, because a
GWAS of a million people and an eQTL study of two hundred differ in scale by orders of magnitude, and two scales on
one plot mislead. Colour does one job only: the variant of interest is drawn in blue and named, and the variant
that carries most of the shared signal is drawn in orange when it is a different one. Everything else is grey.
The panel titles carry the numbers (the posterior probability of a shared variant), so the figure can be read
without the table.
"""

from pathlib import Path
from typing import Any

import numpy as np

from .locus import minus_log10_p

SURFACE, TEXT, SECOND, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
FOCUS, SHARED = "#2a78d6", "#eb6834"   # checked together for colour-blind separation and contrast on the surface


def regional(result: dict[str, Any], genes: list[str], path: Path | str, *, chrom: str, gwas_label: str,
             eqtl_label: str, focus_label: str | None = None) -> Path:
    """Draw the GWAS and the named genes (ids of result["tables"]) of one analysis (locus.analyse) to a PNG."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    tables = result["tables"]
    by_gene = {g["gene"]: g for g in result["genes"]}
    focus = result.get("focus")
    panels = [("gwas", None), *[(g, by_gene[g]) for g in genes if g in tables and g in by_gene]]
    fig, axes = plt.subplots(len(panels), 1, figsize=(8.0, 2.1 * len(panels) + 0.9), sharex=True,
                             facecolor=SURFACE, squeeze=False)
    axes = axes[:, 0]
    for ax, (key, gene) in zip(axes, panels, strict=True):
        table = tables[key]
        x = table["pos"].to_numpy(float) / 1e6
        z = table["z" if key == "gwas" else "z_eqtl"].to_numpy(float)
        y = minus_log10_p(z)
        ax.set_facecolor(SURFACE)
        ax.scatter(x, y, s=7, color=MUTED, alpha=0.55, linewidths=0, zorder=2, rasterized=True)
        marks = []
        if gene is not None and gene["shared_variant"]["pos"] != focus:
            marks.append((gene["shared_variant"]["pos"], SHARED, gene["shared_variant"]["rsid"] or "largest share"))
        if focus is not None:
            marks.append((focus, FOCUS, focus_label or f"{chrom}:{focus}"))
        for pos, colour, label in marks:
            at = np.flatnonzero(table["pos"].to_numpy() == pos)
            if not len(at):
                continue
            px, py = x[at[0]], y[at[0]]
            ax.scatter([px], [py], s=70, color=colour, edgecolors=SURFACE, linewidths=2, zorder=4)
            ax.annotate(label, (px, py), xytext=(8, 2), textcoords="offset points", color=TEXT, fontsize=9,
                        va="center", zorder=5)
        if gene is None:
            title = gwas_label
        else:
            title = (f"{gene['symbol']} expression, {eqtl_label}: probability of a shared causal variant "
                     f"{gene['PP.H4']:.2f}")
        ax.set_title(title, loc="left", fontsize=10, color=TEXT, pad=6)
        ax.set_ylabel("-log10 p", fontsize=9, color=SECOND)
        ax.set_ylim(0, max(float(np.nanmax(y)) * 1.15, 1.0))
        ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=1)
        ax.tick_params(colors=MUTED, labelsize=8, length=0)
        for side in ("top", "right", "left"):
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color(AXIS)
    axes[-1].set_xlabel(f"Position on chromosome {chrom} (Mb, GRCh38)", fontsize=9, color=SECOND)
    fig.tight_layout()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=160, facecolor=SURFACE)
    plt.close(fig)
    return path
