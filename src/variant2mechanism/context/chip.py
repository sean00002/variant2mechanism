"""ENCODE TF ChIP-seq peaks over the variant, from Factorbook (`chip_peaks`).

The answer is one of three, so that an empty search is not read as evidence against binding: a peak contains the
variant; ENCODE assayed the TF in the requested biosample and no peak contains it (evidence against occupancy there);
or ENCODE has no such experiment (no information). Which experiments exist comes from the same released-experiment
search the occupancy step uses, through the HTTP cache.

Then ReMap 2022 (published ChIP-seq from GEO and ENCODE, reprocessed), through the UCSC Genome Browser API (hg38 track
`ReMapTFs`): one request per variant, filtered here by TF and biosample. A ReMap peak in a matching biosample counts as
occupancy; no ReMap peak is no information, since ReMap lists peaks, not the experiments behind them.
"""

from .base import Case, ToolResult, failed

FACTORBOOK = "https://factorbook.api.wenglab.org/graphql"
ENCODE_SEARCH = ("https://www.encodeproject.org/search/?type=Experiment&assay_title=TF+ChIP-seq&status=released"
                 "&assembly=GRCh38&format=json&limit=all&field=target.label&field=biosample_ontology.term_name"
                 "&field=accession")
UCSC_API = "https://api.genome.ucsc.edu/getData/track"
REMAP = "ReMap 2022 (UCSC track ReMapTFs)"


def _norm(name: str) -> str:
    return str(name).lower().replace("-", "").replace(" ", "")


def same_biosample(asked: str, name: str) -> bool:
    a, b = _norm(asked), _norm(name)
    return bool(a and b) and (a in b or b in a)


def remap_peaks(case: Case, tf: str) -> list[dict] | None:
    """ReMap peaks of `tf` that contain the variant, each with its dataset, biosample and summit; None on failure."""
    v = case.variant
    r = case.http.get(f"{UCSC_API}?genome=hg38;track=ReMapTFs;chrom={v.chrom};start={v.pos - 1};end={v.pos}",
                      timeout=60)
    items = r.data.get("ReMapTFs") if r.ok and isinstance(r.data, dict) else None
    if items is None:
        return None
    return [{"dataset": x["name"].split(".")[0], "biosample": x.get("Biotypes", ""), "summit_distance":
             abs(int(x["thickStart"]) + 1 - v.pos)} for x in items
            if (x.get("TF") or "").upper() == tf.upper() and int(x["chromStart"]) < v.pos <= int(x["chromEnd"])]


def remap_text(tf: str, peaks: list[dict] | None, biosample: str | None) -> tuple[str, bool]:
    """The ReMap sentence, and whether ReMap has a peak in a matching biosample (any biosample if none was asked)."""
    if peaks is None:
        return " ReMap could not be reached.", False
    if not peaks:
        return (f" ReMap 2022 has no {tf} peak over the variant (ReMap lists peaks only, so this is no evidence "
                f"against binding)."), False
    match = [p for p in peaks if not biosample or same_biosample(biosample, p["biosample"])]
    by_bio: dict[str, set] = {}
    for p in peaks:
        by_bio.setdefault(p["biosample"], set()).add(p["dataset"])
    listed = "; ".join(f"{b} ({', '.join(sorted(d)[:3])})" for b, d in sorted(by_bio.items(), key=lambda x: -len(x[1]))[:8])
    head = (f" ReMap 2022 (published ChIP-seq, reprocessed): {len(peaks)} {tf} peaks contain the variant, in "
            f"{len(by_bio)} biosamples: {listed}.")
    if biosample:
        head += (f" {len(match)} of them in biosamples matching '{biosample}'" + (
            f", nearest summit {min(p['summit_distance'] for p in match)} bp from the variant." if match else "."))
    else:
        head += f" Nearest summit {min(p['summit_distance'] for p in peaks)} bp from the variant."
    return head, bool(match)


def assayed_biosamples(case: Case, tf: str) -> set[str] | None:
    """Biosamples with released ENCODE TF ChIP-seq for `tf` (GRCh38); None if the search failed or has no list."""
    e = case.http.get(ENCODE_SEARCH, timeout=180)
    graph = e.data.get("@graph") if e.ok and isinstance(e.data, dict) else None
    if graph is None:
        return None
    return {(x.get("biosample_ontology") or {}).get("term_name", "") for x in graph
            if ((x.get("target") or {}).get("label") or "").upper() == tf.upper()}


def chip_peaks(case: Case, tf: str, biosample: str | None = None, flank: int = 100) -> ToolResult:
    v = case.variant
    args = {"tf": tf, "biosample": biosample}
    where = f" in biosamples matching '{biosample}'" if biosample else ""
    assays = assayed_biosamples(case, tf)
    here = sorted(b for b in assays if not biosample or _norm(biosample) in _norm(b)) if assays is not None else None
    remap = remap_peaks(case, tf)
    rtext, remap_here = remap_text(tf, remap, biosample)
    if here == []:
        known = f" ENCODE assayed {tf} in: {', '.join(sorted(assays)[:12])}." if assays else f" ENCODE never assayed {tf}."
        status = "peak" if remap_here else "not_assayed"
        lead = ("" if remap_here else ", so ENCODE says nothing about it there, for or against")
        return ToolResult("chip_peaks", args, f"ENCODE has no {tf} ChIP-seq experiment{where}{lead}.{known}{rtext}",
                          {"status": status, "assayed_in": sorted(assays), "remap": remap},
                          f"ENCODE experiment search; {REMAP}", ENCODE_SEARCH, "epigenomic")
    q = ('{ peaksrange(assembly: "GRCh38", target: "%s", range: [{chrom: "%s", chrom_start: %d, chrom_end: %d}], '
         'limit: 500) { data } }' % (tf.replace('"', ""), v.chrom, v.pos - flank, v.pos + flank))
    r = case.http.graphql(FACTORBOOK, q)
    if not r.ok:
        return failed("chip_peaks", args, "Factorbook", "epigenomic", r)
    rows = ((r.data.get("data") or {}).get("peaksrange") or {}).get("data") or []
    containing = [x for x in rows if x["chrom_start"] < v.pos <= x["chrom_end"]]
    over, elsewhere = containing, []
    if biosample:
        b = _norm(biosample)
        over = [x for x in containing if b in _norm(x["biosample"])]
        elsewhere = [x for x in containing if x not in over]
    bios = sorted({x["biosample"] for x in over})
    exps = sorted({x["experiment_accession"] for x in over})
    if over:
        status = "peak"
        summary = (f"{len(over)} ENCODE {tf} ChIP-seq peaks contain {v.key()}{where}: biosamples {', '.join(bios)}; "
                   f"experiments {', '.join(exps[:8])}.")
    else:
        near = len(rows) - len(containing)
        if remap_here:
            status = "peak"
            summary = f"No ENCODE {tf} ChIP-seq peak contains {v.key()}{where}, but ReMap has one (below)."
        elif here is None:              # the experiment list could not be read: say so, as before
            status = "unknown"
            summary = (f"No ENCODE {tf} ChIP-seq peak contains {v.key()}{where}. Absence can also mean no {tf} "
                       f"experiment in that biosample.")
        else:
            status = "assayed_no_peak"
            summary = (f"No ENCODE {tf} ChIP-seq peak contains {v.key()}{where}, although ENCODE assayed {tf} there "
                       f"({', '.join(here[:8])}): evidence against {tf} occupancy at the variant in that biosample.")
        if not elsewhere:
            summary += f" {near} peaks lie within {flank} bp without containing it."
    if elsewhere:      # never hide that the variant is inside a peak in another biosample
        other = sorted({x["biosample"] for x in elsewhere})
        summary += (f" In other biosamples, {len(elsewhere)} {tf} peaks do contain the variant: {', '.join(other)} "
                    f"(experiments {', '.join(sorted({x['experiment_accession'] for x in elsewhere})[:6])}).")
    return ToolResult("chip_peaks", args, summary + rtext,
                      {"status": status, "matching": over, "other_biosamples": elsewhere, "remap": remap},
                      f"Factorbook (ENCODE TF ChIP-seq peaks); {REMAP}", FACTORBOOK, "epigenomic",
                      retrieved_utc=r.retrieved_utc)
