"""One window of published summary statistics: a harmonised GWAS file or an eQTL dataset, read by region and cached.

Two public sources publish what colocalisation needs, an effect and its standard error for every variant, as
bgzip-compressed tables with a tabix index, so that one window can be read without downloading the file:

- the GWAS Catalog's harmonised summary statistics (GRCh38, forward strand): one row per variant, with the effect
  allele, the other allele, beta and its standard error;
- the eQTL Catalogue's "all" tables: one row per variant and gene, with ref, alt, beta and its standard error for
  the alt allele.

How a window is read: the index is fetched once (about 2 MB a file) and kept; the file's first line gives the
column names; pysam then asks the server for only the compressed blocks that hold the window (HTTP range requests).
Every window read is saved under the cache folder with a small record of where it came from, so the same window is
never requested twice and an analysis can be repeated with no network (`offline=True` reads the cache only).
EBI asks for no more than one such request every couple of seconds; the reader waits between requests.

Alleles: a GWAS row is matched to an eQTL row when they sit at the same position and name the same two alleles.
Effects are then written for the eQTL table's alt allele, so a GWAS effect given for the other allele changes
sign. Both sources are on the forward strand of GRCh38, so no strand is flipped; a pair of alleles that does not
match (a different variant at the same position) is left out, as is a variant listed twice.
"""

import gzip
import hashlib
import io
import json
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

import numpy as np
import pandas as pd

GWAS_ROOT = "https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics"
EQTL_ROOT = "https://ftp.ebi.ac.uk/pub/databases/spot/eQTL/sumstats"
MIN_INTERVAL = 2.5                 # seconds between requests: EBI asks for one tabix request every couple of seconds
HEADER_BYTES = 65536               # one bgzip block is at most 64 KB, and the first holds the column names
USER_AGENT = "statgen-window-reader"
GWAS_COLUMNS = {"pos": "base_pair_location", "effect_allele": "effect_allele", "other_allele": "other_allele",
                "beta": "beta", "se": "standard_error"}
GWAS_OPTIONAL = {"eaf": "effect_allele_frequency", "n": "n", "rsid": "rsid"}
EQTL_COLUMNS = {"gene": "gene_id", "pos": "position", "ref": "ref", "alt": "alt", "beta": "beta", "se": "se"}
EQTL_OPTIONAL = {"maf": "maf", "an": "an", "rsid": "rsid", "trait": "molecular_trait_id"}


class CacheMiss(Exception):
    """An offline reader was asked for something the cache does not hold."""


def gwas_catalog_url(accession: str) -> str:
    """The harmonised summary statistics of a GWAS Catalog study (GCST...), in the Catalog's folders of a thousand."""
    digits = accession.removeprefix("GCST")
    if not accession.startswith("GCST") or not digits.isdigit():
        raise ValueError(f"{accession!r} is not a GWAS Catalog study accession")
    low = (int(digits) - 1) // 1000 * 1000 + 1
    width = len(digits)
    return (f"{GWAS_ROOT}/GCST{low:0{width}d}-GCST{low + 999:0{width}d}/{accession}/harmonised/"
            f"{accession}.h.tsv.gz")


def eqtl_catalogue_url(study: str, dataset: str) -> str:
    """The table of every association of one eQTL Catalogue dataset (study QTS..., dataset QTD...)."""
    return f"{EQTL_ROOT}/{study}/{dataset}/{dataset}.all.tsv.gz"


def _chrom(value: str) -> str:
    return str(value).removeprefix("chr")


@dataclass
class WindowReader:
    """Reads windows of remote tabix-indexed tables, through a cache folder (see the module docstring)."""
    cache_dir: Path
    offline: bool = False
    min_interval: float = MIN_INTERVAL
    requests: list[str] = field(default_factory=list)      # what was asked of the server, for a run's record
    _last: float = 0.0

    def __post_init__(self) -> None:
        self.cache_dir = Path(self.cache_dir)

    # --- the server ----------------------------------------------------------------------------------------------------

    def _wait(self, what: str) -> None:
        if self.offline:
            raise CacheMiss(f"offline, and the cache does not hold {what}")
        pause = self._last + self.min_interval - time.monotonic()
        if pause > 0:
            time.sleep(pause)
        self._last = time.monotonic()
        self.requests.append(what)

    def _get(self, url: str, what: str, headers: dict[str, str] | None = None) -> bytes:
        self._wait(what)
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, **(headers or {})})
        with urllib.request.urlopen(request, timeout=180) as reply:
            return reply.read()

    # --- the three things a window needs -------------------------------------------------------------------------------

    def index(self, url: str) -> Path:
        """The table's tabix index, as a local file."""
        path = self.cache_dir / "index" / (url.rsplit("/", 1)[1] + ".tbi")
        if not path.exists():
            data = self._get(url + ".tbi", f"the index of {url}")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        return path

    def header(self, url: str) -> list[str]:
        """The table's column names: its first line, from its first compressed block."""
        path = self.cache_dir / "header" / (url.rsplit("/", 1)[1] + ".header.tsv")
        if not path.exists():
            raw = self._get(url, f"the first block of {url}", {"Range": f"bytes=0-{HEADER_BYTES - 1}"})
            try:
                text = gzip.GzipFile(fileobj=io.BytesIO(raw)).read(HEADER_BYTES)
            except (EOFError, OSError):
                text = b""                                 # the range ended inside a block: the first one is enough
            line = text.split(b"\n", 1)[0].decode().lstrip("#")
            if "\t" not in line:
                raise ValueError(f"the first line of {url} is not a row of column names")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(line + "\n")
        return path.read_text().rstrip("\n").split("\t")

    def window(self, url: str, chrom: str, start: int, end: int) -> pd.DataFrame:
        """The rows of the table between `start` and `end` (1-based, both included) on `chrom`, as text columns
        under the table's own names."""
        chrom = _chrom(chrom)
        if not 1 <= start <= end:
            raise ValueError("a window runs from a start of at least 1 to an end at or after it")
        name = url.rsplit("/", 1)[1]
        path = self.cache_dir / "windows" / f"{name.removesuffix('.tsv.gz')}__{chrom}_{start}_{end}.tsv.gz"
        if not path.exists():
            columns = self.header(url)
            index = self.index(url)
            self._wait(f"{url} {chrom}:{start}-{end}")
            import pysam  # installed with the project (qbic-selex needs it); used only when a window is fetched
            table = pysam.TabixFile(url, index=str(index))
            try:
                rows = list(table.fetch(chrom, start - 1, end)) if chrom in table.contigs else []
            finally:
                table.close()
            text = "\n".join(["\t".join(columns), *rows]) + "\n"
            path.parent.mkdir(parents=True, exist_ok=True)
            with gzip.open(path, "wt") as out:
                out.write(text)
            path.with_suffix(".json").write_text(json.dumps({
                "url": url, "chrom": chrom, "start": start, "end": end, "rows": len(rows),
                "fetched": datetime.now(UTC).isoformat(timespec="seconds"),
                "sha256": hashlib.sha256(text.encode()).hexdigest()}, indent=1))
        return pd.read_csv(path, sep="\t", dtype=str, keep_default_na=False)


# --- the two tables as numbers -------------------------------------------------------------------------------------------

def _numbers(frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    for c in columns:
        frame[c] = pd.to_numeric(frame[c], errors="coerce")
    return frame


def _named(table: pd.DataFrame, required: dict[str, str], optional: dict[str, str], what: str) -> pd.DataFrame:
    missing = [c for c in required.values() if c not in table.columns]
    if missing:
        raise ValueError(f"{what} lacks the column(s) {', '.join(missing)}")
    names = {**required, **{k: c for k, c in optional.items() if c in table.columns}}
    return table[list(names.values())].rename(columns={c: k for k, c in names.items()}).copy()


def gwas_frame(table: pd.DataFrame) -> pd.DataFrame:
    """A window of a harmonised GWAS table as numbers: pos, effect_allele, other_allele, beta, se, and where the
    table has them eaf (of the effect allele), n and rsid. Rows without an effect or a standard error are left out."""
    out = _named(table, GWAS_COLUMNS, GWAS_OPTIONAL, "the GWAS table")
    out = _numbers(out, [c for c in ("pos", "beta", "se", "eaf", "n") if c in out.columns])
    out = out[np.isfinite(out["beta"]) & np.isfinite(out["se"]) & (out["se"] > 0) & out["pos"].notna()]
    out["pos"] = out["pos"].astype(int)
    for c in ("effect_allele", "other_allele"):
        out[c] = out[c].str.upper()
    return out.reset_index(drop=True)


def eqtl_frame(table: pd.DataFrame) -> pd.DataFrame:
    """A window of an eQTL Catalogue table as numbers: gene, pos, ref, alt, beta and se (for the alt allele), and
    where the table has them maf, n (half the allele number) and rsid."""
    out = _named(table, EQTL_COLUMNS, EQTL_OPTIONAL, "the eQTL table")
    out = _numbers(out, [c for c in ("pos", "beta", "se", "maf", "an") if c in out.columns])
    out = out[np.isfinite(out["beta"]) & np.isfinite(out["se"]) & (out["se"] > 0) & out["pos"].notna()]
    out["pos"] = out["pos"].astype(int)
    if "an" in out.columns:
        out["n"] = out.pop("an") / 2.0
    for c in ("ref", "alt"):
        out[c] = out[c].str.upper()
    return out.reset_index(drop=True)


def align(gwas: pd.DataFrame, eqtl: pd.DataFrame) -> pd.DataFrame:
    """The variants both tables hold, one row each, with both effects written for the eQTL table's alt allele:
    pos, ref, alt, rsid, and beta, se, maf and n of each (suffix _gwas, _eqtl; a column a table lacks is NaN).
    `eqtl` holds one gene. A variant either table lists twice, or whose alleles differ between them, is left out."""
    def side(frame: pd.DataFrame, keys: list[str], suffix: str, optional: tuple[str, ...]) -> pd.DataFrame:
        out = frame.drop_duplicates(keys, keep=False).copy()
        for column in optional:
            if column not in out.columns:
                out[column] = "" if column == "rsid" else np.nan
        named = ("beta", "se", *optional)
        return out[[*keys, *named]].rename(columns={c: f"{c}{suffix}" for c in named})

    g = side(gwas, ["pos", "effect_allele", "other_allele"], "_gwas", ("eaf", "n", "rsid"))
    e = side(eqtl, ["pos", "ref", "alt"], "_eqtl", ("maf", "n", "rsid"))
    both = g.merge(e, on="pos")
    same = (both["effect_allele"] == both["alt"]) & (both["other_allele"] == both["ref"])
    swapped = (both["effect_allele"] == both["ref"]) & (both["other_allele"] == both["alt"])
    both = both[same | swapped].copy()
    sign = np.where(both["effect_allele"] == both["alt"], 1.0, -1.0)
    both["beta_gwas"] = both["beta_gwas"] * sign
    alt_frequency = np.where(sign > 0, both["eaf_gwas"], 1.0 - both["eaf_gwas"])
    both["maf_gwas"] = np.minimum(alt_frequency, 1.0 - alt_frequency)
    both["rsid"] = np.where(both["rsid_eqtl"].astype(str) != "", both["rsid_eqtl"], both["rsid_gwas"])
    # the same position and alleles twice after the merge: one table lists the variant under two alleles' orders
    both = both.drop_duplicates(["pos", "ref", "alt"], keep=False).sort_values("pos")
    return both[["pos", "ref", "alt", "rsid", "beta_gwas", "se_gwas", "maf_gwas", "n_gwas",
                 "beta_eqtl", "se_eqtl", "maf_eqtl", "n_eqtl"]].reset_index(drop=True)
