"""Occupancy, in code (spec 3, section 1): which TFs ENCODE ChIP-seq places on the variant, and in which biosamples.

QBiC-SELEX gives the direction and size of an allele's effect on a TF's binding, on the premise that the TF occupies
the site; whether it does comes from here. Two cached queries: every ENCODE TF ChIP-seq peak containing the variant
base (Factorbook, no target), and the released ENCODE TF ChIP-seq experiments (what was assayed, and where). Each TF
then gets one class, strongest first:

    bound_here                 a peak contains the variant in a biosample matching the expression context
    bound_elsewhere            a peak contains the variant, only in other biosamples
    not_assayed                ENCODE has no TF ChIP-seq for this TF
    unbound_assayed_elsewhere  assayed only in other biosamples, and no peak contains the variant
    unbound_assayed_here       assayed in a matching biosample, and no peak contains the variant

Only TFs with a sequence-specific QBiC-SELEX model (own or CIS-BP-mapped) become candidates. Other ChIP targets
(EP300, POLR2A, SIN3A, HDACs and the like) count only as signs that the element is active. ChIP peaks are 300 to
600 bp wide, so occupancy is a property of the element, not of the base.
"""

import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import yaml

from .base import Case, ToolResult, failed
from .chip import ENCODE_SEARCH, FACTORBOOK

MATCH_FILE = Path(__file__).with_name("biosample_match.yaml")
SOURCE = "ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search)"
CLASSES = ("bound_here", "bound_elsewhere", "not_assayed", "unbound_assayed_elsewhere", "unbound_assayed_here")
OCCUPIED = ("bound_here", "bound_elsewhere")
DESCRIBE = {"bound_here": "bound here", "bound_elsewhere": "bound elsewhere", "not_assayed": "never assayed by ENCODE",
            "unbound_assayed_elsewhere": "assayed elsewhere, no peak here",
            "unbound_assayed_here": "assayed in the matching biosample, no peak here"}
# A guard on top of the coverage rule: co-factors, chromatin regulators and the Pol II machinery never become TF
# candidates, even if a mapped model ever named one of them.
NOT_SEQUENCE_SPECIFIC = {"EP300", "CREBBP", "POLR2A", "POLR2B", "POLR2G", "POLR2H", "SIN3A", "SIN3B", "HDAC1",
                         "HDAC2", "HDAC3", "HDAC6", "HDAC8", "KDM1A", "KDM5A", "KDM5B", "BRD4", "RAD21", "SMC3",
                         "EZH2", "SUZ12", "NCOR1", "NCOA3", "MED1", "SMARCA4", "SMARCC2", "TAF1", "CHD1", "CHD2",
                         "CHD4", "CHD7", "RBBP5"}
MAX_ROWS = 10


def norm(name: str) -> str:
    return re.sub(r"[\s\-_]", "", str(name)).lower()


@dataclass
class Match:
    key: str | None                     # the context's entry in biosample_match.yaml; None if it is not listed
    biosamples: list[str]
    proxy: str | None = None

    def matches(self, biosample: str) -> bool:
        return norm(biosample) in {norm(b) for b in self.biosamples}


def context_key(context: str | None) -> str:
    text = (context or "").strip()
    if not text or text.lower().startswith("none"):
        return "none"
    m = re.match(r"(DepMap:ACH-\d+)", text)
    return m.group(1) if m else re.sub(r"\s*\([^()]*\)\s*$", "", text).strip()


def biosample_match(context: str | None, path: Path = MATCH_FILE) -> Match:
    table = yaml.safe_load(Path(path).read_text()) or {}
    key = context_key(context)
    if key not in table:
        return Match(None, [])
    entry = table[key] or {}
    return Match(key, list(entry.get("biosamples") or []), entry.get("proxy"))


@dataclass
class Occupancy:
    variant: str
    match: Match
    peaks: list[dict]                               # every ENCODE TF ChIP-seq peak containing the variant
    assayed: dict[str, set[str]]                    # HGNC symbol -> biosamples ENCODE assayed it in
    symbol_of: dict[str, str | None] = field(default_factory=dict)   # ChIP target label -> HGNC symbol

    def __post_init__(self):
        self._by_symbol: dict[str, list[dict]] = {}
        for p in self.peaks:
            sym = self.symbol_of.get(p["target"])
            if sym:
                self._by_symbol.setdefault(sym, []).append(p)

    def peaks_of(self, symbol: str) -> list[dict]:
        return self._by_symbol.get(symbol, [])

    def tf_class(self, symbol: str) -> str:
        peaks = self.peaks_of(symbol)
        if any(self.match.matches(p["biosample"]) for p in peaks):
            return "bound_here"
        if peaks:
            return "bound_elsewhere"
        where = self.assayed.get(symbol)
        if not where:
            return "not_assayed"
        return "unbound_assayed_here" if any(self.match.matches(b) for b in where) else "unbound_assayed_elsewhere"

    def detail(self, symbol: str) -> dict:
        """The class, the biosamples with a peak (matching first) and one experiment accession, from a matching
        biosample when there is one."""
        peaks = self.peaks_of(symbol)
        here = [p for p in peaks if self.match.matches(p["biosample"])]
        others = [p for p in peaks if p not in here]
        first = (here or others or [None])[0]
        return {"occupancy": self.tf_class(symbol), "n_peaks": len(peaks),
                "biosamples_here": sorted({p["biosample"] for p in here}),
                "biosamples_elsewhere": sorted({p["biosample"] for p in others}),
                "experiment": first["experiment_accession"] if first else None}


def fetch(case: Case, reg) -> tuple[Occupancy | None, ToolResult | None]:
    """Both queries through the case's HTTP cache; on a failure, a failed ToolResult instead of an Occupancy."""
    v = case.variant
    args = {"variant": v.key(), "expression_context": case.expression_context}
    q = ('{ peaksrange(assembly: "GRCh38", range: [{chrom: "%s", chrom_start: %d, chrom_end: %d}], limit: 5000) '
         '{ data } }' % (v.chrom, v.pos - 1, v.pos))
    r = case.http.graphql(FACTORBOOK, q)
    if not r.ok:
        return None, failed("occupancy", args, "Factorbook", "epigenomic", r)
    rows = ((r.data.get("data") or {}).get("peaksrange") or {}).get("data") or []
    peaks = [p for p in rows if p["chrom_start"] < v.pos <= p["chrom_end"]]
    e = case.http.get(ENCODE_SEARCH, timeout=180)
    if not e.ok:
        return None, failed("occupancy", args, "ENCODE experiment search", "epigenomic", e)
    labels = {(x.get("target") or {}).get("label") for x in e.data.get("@graph", [])} | {p["target"] for p in peaks}
    symbol_of = {}
    for label in labels - {None}:
        res = reg.resolve_tf(label)
        symbol_of[label] = res["symbol"] if res["status"] == "ok" else None
    assayed: dict[str, set[str]] = {}
    for x in e.data.get("@graph", []):
        sym = symbol_of.get((x.get("target") or {}).get("label"))
        if sym:
            assayed.setdefault(sym, set()).add((x.get("biosample_ontology") or {}).get("term_name", ""))
    return Occupancy(v.key(), biosample_match(case.expression_context), peaks, assayed, symbol_of), None


def sequence_specific(reg) -> set[str]:
    """TFs with a QBiC-SELEX model of their own or a CIS-BP-mapped one."""
    return (set(reg.own_model) | set(reg.mapped_models)) - NOT_SEQUENCE_SPECIFIC


def candidates(occ: Occupancy, reg, expression=None, context=None, min_tpm: float = 1.0) -> dict:
    """Bound, sequence-specific, expressed TFs: bound_here first, then bound_elsewhere; within a class by the number
    of peaks over the variant, then expression. Also the counts of TFs left out."""
    tfs = sequence_specific(reg)
    bound = sorted(s for s in tfs if occ.peaks_of(s))
    ctx = expression.parse(context) if expression is not None else None
    expr = expression.tf_expression(bound, ctx) if (ctx is not None and ctx.kind != "none") else {}
    rows, not_expressed = [], []
    for s in bound:
        tpm = expr.get(s, {}).get("tpm")
        rec = {"tf": s, **occ.detail(s), "tpm": tpm, "rank": expr.get(s, {}).get("rank_among_tfs"),
               "n_tfs": expr.get(s, {}).get("n_tfs")}
        (not_expressed if (tpm is not None and tpm < min_tpm) else rows).append(rec)
    rows.sort(key=lambda r: (OCCUPIED.index(r["occupancy"]), -r["n_peaks"], -(r["tpm"] or 0)))
    classes = Counter(occ.tf_class(s) for s in tfs if not occ.peaks_of(s))
    return {"rows": rows, "not_expressed": [r["tf"] for r in not_expressed],
            "unbound_here": classes["unbound_assayed_here"], "unbound_elsewhere": classes["unbound_assayed_elsewhere"],
            "not_assayed": classes["not_assayed"]}


def tpm_text(r: dict, context_label: str) -> str:
    if r.get("tpm") is None:
        return "expression not filtered (no expression data for this context)"
    rank = f", rank {r['rank']} of {r['n_tfs']} TFs" if r.get("rank") else ""
    return f"{r['tpm']} TPM in {context_label}{rank}"


def candidate_line(r: dict, context_label: str) -> str:
    where = (f"in the matching biosample {', '.join(r['biosamples_here'])}" if r["biosamples_here"]
             else f"only in other biosamples: {', '.join(r['biosamples_elsewhere'][:6])}"
             + (f" (+{len(r['biosamples_elsewhere']) - 6} more)" if len(r["biosamples_elsewhere"]) > 6 else ""))
    also = (f"; also in {', '.join(r['biosamples_elsewhere'][:4])}"
            + (f" (+{len(r['biosamples_elsewhere']) - 4} more)" if len(r["biosamples_elsewhere"]) > 4 else "")
            if r["biosamples_here"] and r["biosamples_elsewhere"] else "")
    return (f"{r['tf']}: {DESCRIBE[r['occupancy']]}. {r['n_peaks']} ENCODE ChIP-seq peak(s) contain the variant, "
            f"{where}{also} (e.g. {r['experiment']}). {tpm_text(r, context_label)}.")


def element_line(occ: Occupancy, cands: dict, ccre_class: str | None, reg) -> str:
    v = occ.variant
    m = occ.match
    if occ.match.key is None:
        match_txt = ("The expression context has no entry in the biosample map, so no biosample counts as matching "
                     "(add one to biosample_match.yaml).")
    elif not m.biosamples:
        match_txt = "No ENCODE biosample matches the expression context, so no peak counts as bound here."
    else:
        here = [p for p in occ.peaks if m.matches(p["biosample"])]
        match_txt = (f"In the matching biosample {', '.join(m.biosamples)}"
                     + (f" ({m.proxy})" if m.proxy else "")
                     + f": {len(here)} peaks from {len({p['target'] for p in here})} factors.")
    ccre = f" cCRE class at the variant: {ccre_class}." if ccre_class else " No cCRE contains the variant."
    if not occ.peaks:
        return (f"No ENCODE TF ChIP-seq peak contains {v} in any biosample. {match_txt}{ccre} Of the TFs with a "
                f"binding model, {cands['unbound_here']} were assayed in the matching biosample and "
                f"{cands['unbound_elsewhere']} only elsewhere, all without a peak here; {cands['not_assayed']} were "
                f"never assayed.")
    seq = sequence_specific(reg)
    factors = sorted({p["target"] for p in occ.peaks})
    other = [f for f in factors if occ.symbol_of.get(f) not in seq]
    shown = [r["tf"] for r in cands["rows"][:MAX_ROWS]]
    rest = [r["tf"] for r in cands["rows"][MAX_ROWS:]]
    text = (f"ENCODE TF ChIP-seq at {v}: {len(occ.peaks)} peaks contain the variant, from {len(factors)} factors in "
            f"{len({p['biosample'] for p in occ.peaks})} biosamples. {match_txt}{ccre} "
            f"Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; "
            f"signs of an active element, not TF candidates): "
            f"{', '.join(other[:12]) or 'none'}" + (f" (+{len(other) - 12} more)" if len(other) > 12 else "") + ". "
            f"Bound, expressed TFs with a binding model: {len(cands['rows'])}"
            + (f"; listed one per row: {', '.join(shown)}" if shown else "")
            + (f"; also bound: {', '.join(rest[:30])}" + (f" (+{len(rest) - 30} more)" if len(rest) > 30 else "")
               if rest else "") + ". "
            + (f"Bound but below 1 TPM: {', '.join(cands['not_expressed'][:10])}. " if cands["not_expressed"] else "")
            + f"Assayed with no peak here: {cands['unbound_here']} TFs in the matching biosample, "
              f"{cands['unbound_elsewhere']} only elsewhere; never assayed: {cands['not_assayed']}.")
    return text


def occupancy_results(case: Case, reg, expression=None, ccre_class: str | None = None,
                      min_tpm: float = 1.0) -> tuple[Occupancy | None, list[ToolResult]]:
    """The gather step's occupancy evidence: one row for the element, one per listed candidate (at most 10)."""
    occ, err = fetch(case, reg)
    if err is not None:
        return None, [err]
    cands = candidates(occ, reg, expression, case.expression_context, min_tpm)
    ctx_label = case.expression_context or "this context"
    args = {"variant": occ.variant, "expression_context": case.expression_context}
    out = [ToolResult("occupancy", {**args, "part": "element"}, element_line(occ, cands, ccre_class, reg),
                      {"n_peaks": len(occ.peaks), "match": occ.match.biosamples, "counts": {k: v for k, v in
                       cands.items() if k != "rows"}}, SOURCE, FACTORBOOK, "epigenomic")]
    for r in cands["rows"][:MAX_ROWS]:
        out.append(ToolResult("occupancy", {**args, "tf": r["tf"]}, candidate_line(r, ctx_label), r, SOURCE,
                              FACTORBOOK, "epigenomic"))
    return occ, out
