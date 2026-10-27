"""SNVs on GRCh38: parsing, normalisation, the cache key and the strand pre-check (spec 1, section 5.1)."""

import re
from dataclasses import dataclass

import requests

BASES = set("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


class VariantError(ValueError):
    """Raised for anything that is not a plus-strand GRCh38 SNV."""


@dataclass(frozen=True, order=True)
class Variant:
    chrom: str
    pos: int
    ref: str
    alt: str

    @classmethod
    def make(cls, chrom, pos, ref, alt) -> "Variant":
        chrom = str(chrom).strip()
        chrom = chrom if chrom.lower().startswith("chr") else f"chr{chrom}"
        chrom = "chr" + chrom[3:]
        ref, alt = str(ref).strip().upper(), str(alt).strip().upper()
        if len(ref) != 1 or len(alt) != 1:
            raise VariantError(f"Only SNVs are supported (single-base ref and alt); got {ref}>{alt}. "
                               "Indels and multi-base changes are not scored by QBiC-SELEX here.")
        if ref not in BASES or alt not in BASES:
            raise VariantError(f"Alleles must be A, C, G or T; got {ref}>{alt}.")
        if ref == alt:
            raise VariantError(f"ref and alt are the same base ({ref}).")
        try:
            pos = int(pos)
        except (TypeError, ValueError):
            raise VariantError(f"Position must be an integer; got {pos!r}.") from None
        if pos < 1:
            raise VariantError(f"Position must be 1-based (>= 1); got {pos}.")
        return cls(chrom, pos, ref, alt)

    def key(self) -> str:
        return f"{self.chrom}:{self.pos}:{self.ref}>{self.alt}"

    @property
    def chrom_bare(self) -> str:
        return self.chrom[3:]

    def __str__(self) -> str:
        return self.key()


_FORMS = [
    re.compile(r"^(?:chr)?(\w+):(\d+):([A-Za-z]+)>([A-Za-z]+)$"),        # chr5:1295113:G>A
    re.compile(r"^(?:chr)?(\w+)-(\d+)-([A-Za-z]+)-([A-Za-z]+)$"),        # chr5-1295113-G-A
    re.compile(r"^(?:chr)?(\w+):(\d+)\s+([A-Za-z]+)>([A-Za-z]+)$"),      # 5:1295113 G>A
]


def parse(text: str) -> Variant:
    text = text.strip()
    for form in _FORMS:
        m = form.match(text)
        if m:
            return Variant.make(*m.groups())
    raise VariantError(f"Could not parse '{text}'. Use chr5:1295113:G>A, chr5-1295113-G-A or 5:1295113 G>A "
                       "(GRCh38, 1-based, plus strand).")


def ensembl_base(v: Variant, timeout: float = 20.0) -> str:
    url = (f"https://rest.ensembl.org/sequence/region/human/{v.chrom_bare}:{v.pos}..{v.pos}:1"
           "?content-type=text/plain")
    r = requests.get(url, timeout=timeout, headers={"User-Agent": "variant2mechanism/0.1"})
    r.raise_for_status()
    return r.text.strip().upper()


def strand_precheck(v: Variant, fetch=ensembl_base) -> str | None:
    """A message if the alleles look like minus-strand notation; None otherwise or if Ensembl is unreachable."""
    try:
        base = fetch(v)
    except Exception:
        return None          # submit anyway; qbic_status catches mismatches
    if base == v.ref:
        return None
    if base == v.ref.translate(COMPLEMENT):
        fixed = f"{v.chrom}:{v.pos} {v.ref.translate(COMPLEMENT)}>{v.alt.translate(COMPLEMENT)}"
        return f"Alleles look like minus-strand notation. QBiC-SELEX needs plus-strand alleles: use {fixed}."
    return None
