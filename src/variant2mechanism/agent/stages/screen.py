"""Screen (code, `full` only): screen v2 from spec 3, as one evidence row for the summary and one per listed TF.

Occupancy first: the candidates are TFs that ENCODE ChIP-seq places on the variant, then expressed TFs ENCODE never
assayed. Within each occupancy class, occupied TFs with a strong site come first (screen v3, the site-strength
rule). The count of models passing Bonferroni is never shown to the model; it stays in report.json as a diagnostic.
"""

from ...context.base import ToolResult
from ...qbic.screen import NO_PEAK
from ..case import RunState

SOURCE = "QBiC-SELEX 1.0.0 primary collection (997 models)"
OCCUPANCY_TEXT = {"bound_here": "bound here", "bound_elsewhere": "bound elsewhere",
                  "not_assayed": "unknown (ENCODE never assayed this TF)", "unknown": "unknown (occupancy lookup failed)"}


class RunStopped(RuntimeError):
    """The run cannot continue honestly (for example, QBiC-SELEX results are unavailable in `full`)."""


def tf_line(r: dict, context: str, strong_pct: float | None = None) -> str:
    model = "its own model" if r["best_model_kind"] == "own" else f"a CIS-BP-mapped model of {r['best_model_tf']}"
    strong = r.get("strong_site")         # None: no site rule for this row (occupancy unknown, or no weights)
    if r["passes_gate"] and strong is not False:
        change = f"{r['allele_binding_more']} allele binds more; QBiC-SELEX detects a change (|z| above the gate)"
    elif r["passes_gate"]:
        change = f"{r['allele_binding_more']} allele binds more (|z| above the gate), but between weak k-mers"
    else:
        change = (f"{r['allele_binding_more']} allele binds slightly more; occupied, no clear allelic change "
                  f"(|z| below the gate)")
    expr = (f"{r['tpm']} TPM, rank {r['rank']} of {r['n_tfs']} TFs in {context}" if r.get("tpm") is not None
            else "expression not filtered")
    occ = OCCUPANCY_TEXT.get(r["occupancy"], r["occupancy"])
    if r["occupancy"] in ("bound_here", "bound_elsewhere"):
        where = r["biosamples_here"] or r["biosamples_elsewhere"]
        occ += f": ENCODE ChIP-seq peak over the variant in {', '.join(where[:5])}" + \
            (f" (+{len(where) - 5} more)" if len(where) > 5 else "") + f", e.g. {r['experiment']}"
    site = r.get("site_strength") or {}
    site_txt = (f" Best model's site strength: ref {site['ref_percentile']}th, alt {site['alt_percentile']}th "
                "percentile of its k-mer coefficients") if "ref_percentile" in site else ""
    if site_txt and strong is True:
        site_txt += f": a strong site (the better allele reaches the {strong_pct:g}th)."
    elif site_txt and strong is False:
        site_txt += (f": a weak site (neither allele reaches the {strong_pct:g}th), so the ChIP peak more likely "
                     "reflects another site in the element.")
    elif site_txt:
        site_txt += "."
    coverage = "own model" if r["coverage"] == "own_model" else "mapped models only"
    return (f"{r['tf']} ({r['group']}; QBiC-SELEX coverage: {coverage}): best model {r['best_model']} ({model}), "
            f"z {r['z']}, effect {r['effect']}: {change}. {expr}. Occupancy: {occ}.{site_txt}")


def summary_line(v: str, out: dict) -> str:
    c, g, pct = out["counts"], out["gate"], out.get("strong_site_pct")
    text = (f"QBiC-SELEX screen of {v}, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. "
            f"Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed ({out['context']}),"
            f" bound here before bound elsewhere, then " + ("a strong site before a weak one, then " if pct else "") +
            f"by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). "
            f"Shown: {len(out['occupied'])} of {c['occupied']} occupied"
            + (f" ({c['occupied_strong_site']} with a strong site)" if pct else "") + ", "
            f"{len(out['unknown'])} of {c['unknown']} with unknown occupancy. Left out: {c['unbound_assayed_here']} TFs "
            f"assayed in the matching biosample and {c['unbound_assayed_elsewhere']} assayed only elsewhere, none with a "
            f"peak here" + (f"; {c['occupied_not_expressed']} bound but below 1 TPM" if c["occupied_not_expressed"]
                            else "") + ". "
            f"The gate (|z| > {g['abs_z']}, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says "
            f"nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.")
    if pct:
        text += (f" Site strength is the better allele's best k-mer over the variant, as a percentile of the best "
                 f"model's k-mers; a strong site reaches the {pct:g}th. At a weak site the ChIP peak more likely "
                 f"reflects another site in the element.")
    if not out["occupancy_available"]:
        text += " The occupancy lookup failed, so occupancy is unknown for every TF."
    elif out["nothing_occupied"]:
        text += " " + NO_PEAK
    elif out.get("no_strong_site"):
        text += " No occupied TF has a strong site at the variant."
    return text


def screen(state: RunState) -> None:
    v = state.spec.variant
    out = state.qbic.qbic_screen_v2(v.chrom, v.pos, v.ref, v.alt, state.spec.expression_context, state.occupancy)
    if "error" in out:
        raise RunStopped(f"qbic_screen failed: {out['error']} Fix: {out['fix']}")
    state.screen = out
    args = {"variant": v.key(), "expression_context": state.spec.expression_context}
    state.ledger.add_evidence("screen", ToolResult("qbic_screen", args, summary_line(v.key(), out),
                                                   {k: val for k, val in out.items() if k not in ("occupied", "unknown")},
                                                   SOURCE, "cache/qbic.sqlite", "computational", limit=3000,
                                                   status="found" if out["occupied"] or out["unknown"]
                                                   else "tested_negative"))
    for r in out["occupied"] + out["unknown"]:
        state.ledger.add_evidence("screen", ToolResult("qbic_screen", {**args, "tf": r["tf"]},
                                                       tf_line(r, state.spec.expression_context or "this context",
                                                               out.get("strong_site_pct")), r,
                                                       SOURCE, "cache/qbic.sqlite", "computational", limit=3000,
                                                       status="found" if r["passes_gate"] else "tested_negative"))
