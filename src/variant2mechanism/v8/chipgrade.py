"""ChIP grades (v8): how close each TF's ChIP-seq binding comes to the variant.

Grade 1: a ReMap 2022 summit within 50 bp of the variant. Grade 2: the variant inside a ReMap peak extended by 50 bp
on each side, or inside an ENCODE peak (Factorbook peaks carry no summit). Grade 3: no peak. Each grade is kept for
the biosamples matching the context and for any biosample. Grade 2 never counts against a TF: an off-centre summit
can mean a weaker second site at the variant, or a cell line without the allele that binds more.
"""

import re
from dataclasses import dataclass, field

REMAP_URL = ("https://api.genome.ucsc.edu/getData/track?genome=hg38;track=ReMapTFs;chrom={chrom};start={start};"
             "end={end}")
REMAP = "ReMap 2022 (UCSC track ReMapTFs)"


def name_match(a: str, b: str) -> bool:
    """Biosample names match when equal after dropping case, spaces and hyphens (HCT116, HCT-116), or when the shorter
    has at least 5 characters and is contained in the other (LNCaP, LNCaP clone FGC); short names must be equal, so
    that a line called HEL never matches HeLa."""
    x, y = re.sub(r"[^a-z0-9]", "", str(a).lower()), re.sub(r"[^a-z0-9]", "", str(b).lower())
    if not x or not y:
        return False
    if x == y:
        return True
    short, long_ = sorted((x, y), key=len)
    return len(short) >= 5 and short in long_


@dataclass
class Chip:
    pos: int                                   # the variant, 1-based
    remap: list[dict]                          # ReMap peaks over the variant +/- window, with their summit distance
    occupancy: object | None                   # context/occupancy.Occupancy: ENCODE peaks and what ENCODE assayed
    here_names: list[str] = field(default_factory=list)   # biosample names matching the context
    remap_ok: bool = True
    url: str = ""

    def here(self, biosample: str) -> bool:
        return any(name_match(n, biosample) for n in self.here_names) if biosample else False

    def member(self, tf: str) -> dict:
        """The grades of one TF, here and anywhere, with the nearest summit and where it was seen."""
        peaks = [p for p in self.remap if p["tf"] == tf.upper()]
        here = [p for p in peaks if self.here(p["biosample"])]
        enc = self.occupancy.peaks_of(tf) if self.occupancy is not None else []
        enc_here = [p for p in enc if self.here(p["biosample"])]
        assayed = (self.occupancy.assayed.get(tf, set()) if self.occupancy is not None else set())

        def grade(ps, encode):
            if any(p["summit_distance"] <= p["window"] for p in ps):
                return 1
            return 2 if ps or encode else 3

        return {"grade_here": grade(here, enc_here), "grade_any": grade(peaks, enc),
                "summit_here": min((p["summit_distance"] for p in here), default=None),
                "summit_any": min((p["summit_distance"] for p in peaks), default=None),
                "cells_here": sorted({p["biosample"] for p in here} | {p["biosample"] for p in enc_here}),
                "cells_any": sorted({p["biosample"] for p in peaks} | {p["biosample"] for p in enc})[:12],
                "encode_here": bool(enc_here), "assayed_here": any(self.here(b) for b in assayed),
                "assayed_any": bool(assayed) or bool(peaks)}

    def summary(self) -> dict:
        tfs = sorted({p["tf"] for p in self.remap})
        g1 = [t for t in tfs if any(p["summit_distance"] <= p["window"] for p in self.remap if p["tf"] == t)]
        return {"tfs_with_peaks": len(tfs), "tfs_with_summit": len(g1), "remap_ok": self.remap_ok}


def fetch_chip(case, occupancy, here_names: list[str], window: int = 50) -> Chip:
    """ReMap peaks overlapping the variant +/- `window` bp, through the case's HTTP cache."""
    v = case.variant
    url = REMAP_URL.format(chrom=v.chrom, start=max(0, v.pos - 1 - window), end=v.pos + window)
    r = case.http.get(url, timeout=120)
    items = r.data.get("ReMapTFs") if r.ok and isinstance(r.data, dict) else None
    peaks = []
    for x in items or []:
        start, end, summit = int(x["chromStart"]), int(x["chromEnd"]), int(x["thickStart"])
        peaks.append({"tf": str(x.get("TF") or "").upper(), "biosample": x.get("Biotypes", ""),
                      "dataset": str(x.get("name", "")).split(".")[0], "summit_distance": abs(summit + 1 - v.pos),
                      "inside": start < v.pos <= end, "window": window})
    return Chip(v.pos, peaks, occupancy, here_names, remap_ok=items is not None, url=url)
