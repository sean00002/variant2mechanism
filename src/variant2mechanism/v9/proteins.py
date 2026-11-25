"""Which proteins bind DNA by sequence.

ChIP-seq pulls down a protein with the DNA it is cross-linked to, directly or through other proteins. For a
transcription factor, reads that favour one allele of a variant are a measurement of the claim "the two alleles differ
in binding this TF". For a protein with no DNA-binding domain of its own (BRD4 reads acetylated histones, β-catenin
is brought by TCF/LEF factors, cohesin and the Mediator are loaded by others) the same imbalance cannot mean that the
protein reads the variant: it shows that the state of the site differs between the alleles. Such a record therefore
bears on "the two alleles differ in the regulatory activity of the site" and names no TF of a chain.

The list is the census of human transcription factors (Lambert et al. 2018, 1,639 genes marked "Is TF? Yes"), named
by today's HGNC symbol through each row's Ensembl gene id (a few genes have been renamed since: T is now TBXT), and
every TF that has a QBiC-SELEX model. It was fixed from what the proteins are, not from how any labelled case
comes out.

Three kinds, and only one moves a record: "tf" (on the list), "not_tf" (an approved gene symbol that is not on it)
and "unknown" (the list is not available, or the name resolves to no approved symbol, as an article's "AP-2" does
not: a name with a Greek letter, "AP-2α", now resolves through the HGNC table's aliases; graph.SymbolResolver).
An unknown protein is treated as a TF, which is what was done for every protein before this rule.
"""

import csv
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

TF, NOT_TF, UNKNOWN = "tf", "not_tf", "unknown"
SOURCE = "Lambert et al. 2018 census of human TFs, and the TFs with a QBiC-SELEX model"
COFACTOR_FLAG = "allele_specific_cofactor"       # Evidence.data: allele-specific reads of a protein that is not a TF
NOT_TF_NAMES = "not_tf"                          # Evidence.data: the proteins a ChIP record names that are not TFs
ACCESSIBILITY_FLAG = "allele_specific_accessibility"   # Evidence.data: allele-specific reads of open chromatin, which
                                                        # name no protein at all (fill_sources.py)


@lru_cache(maxsize=4)
def _symbols(census: str, hgnc: str | None, groups: str | None) -> frozenset[str]:
    current: dict[str, str] = {}
    if hgnc:
        with open(hgnc, newline="") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                if row.get("status") == "Approved" and row.get("ensembl_gene_id"):
                    current[row["ensembl_gene_id"].strip()] = row["symbol"].strip()
    found: set[str] = set()
    with open(census, newline="") as f:
        for row in csv.DictReader(f):
            if row.get("Is TF?") != "Yes":
                continue
            names = (row.get("HGNC symbol") or "").strip(), current.get((row.get("Ensembl ID") or "").strip(), "")
            found.update(name.upper() for name in names if name)
    if groups:
        data = json.loads(Path(groups).read_text())
        found.update(str(tf).upper() for g in data.get("groups") or [] for tf in g.get("tfs") or [])
    return frozenset(found)


def _file(config: Any, section: str, key: str) -> str | None:
    try:
        path = config.path(section, key)
    except Exception:                             # not set in this configuration
        return None
    return str(path) if path.exists() else None


def tf_symbols(config: Any) -> frozenset[str] | None:
    """The symbols (upper case) of the proteins that bind DNA by sequence, or None when the census file is not at
    the configured path (as in a checkout without the reference data): every protein's kind is then unknown."""
    census = _file(config, "data", "lambert") if config is not None else None
    if census is None:
        return None
    return _symbols(census, _file(config, "data", "hgnc"), _file(config, "cache", "groups"))


def kind(symbol: str | None, tfs: frozenset[str] | None) -> str:
    """The kind of a protein named by an approved HGNC symbol. Give None for a name that is not one."""
    if tfs is None or not symbol:
        return UNKNOWN
    return TF if symbol.upper() in tfs else NOT_TF
