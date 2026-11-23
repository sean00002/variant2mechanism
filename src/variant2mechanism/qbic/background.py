"""How large a QBiC-SELEX prediction is for a TF group, across unlabelled variants.

The Bonferroni gate says a prediction differs from zero. It does not say the change is large for that TF: across
21.8 million background variants the median model passes the gate at 36% of them, and a group of many models at
nearly all of them (the 81 homeodomain models: 99.8%). So "large" is read against the group's own distribution.

The table (resources/background_group_quantiles.tsv) holds, for each of the 631 model-sharing groups, quantiles of
|z| of the group's model with the largest |z| at each background variant. That is how a group's value is taken at a
query variant, so the two are compared like with like, whatever the group's size. The background is the IGVF
TLand Y2AVE variant list with the variants this project evaluates or develops on left out
(resources/background_summary.json), so no cut-off was chosen by how it does on a labelled case.

A prediction is "in the group's top 10%" when its |z| is at or above the group's 90th percentile. The fraction was
fixed before the background was run. It is a yes or a no and is only ever used to order chains that are otherwise
equal (v9/chain.py): it removes no TF, and a TF with no model loses nothing by it.
"""

import csv
import json
from functools import lru_cache
from pathlib import Path
from typing import Any

RESOURCES = Path(__file__).parent / "resources"
TABLE = RESOURCES / "background_group_quantiles.tsv"
SUMMARY = RESOURCES / "background_summary.json"
TOP_SHARE = 0.10                                 # the share of background variants a "large" prediction is among
TOP_COLUMN = "abs_z_p90"                         # the table's column for 1 - TOP_SHARE


@lru_cache(maxsize=1)
def group_cutoffs() -> dict[str, float]:
    """|z| at the 90th percentile of each group's background, by group id."""
    with TABLE.open(newline="") as handle:
        return {row["group_id"]: float(row[TOP_COLUMN]) for row in csv.DictReader(handle, delimiter="\t")}


@lru_cache(maxsize=1)
def summary() -> dict[str, Any]:
    """Where the background came from and how many variants it holds."""
    return json.loads(SUMMARY.read_text())


def in_top_share(group_id: str | None, z: float | None) -> bool | None:
    """Whether |z| is in the top 10% of what this group predicts across the background. None when the group is not
    in the table or z is missing: unknown, never a no."""
    cutoff = group_cutoffs().get(str(group_id))
    if cutoff is None or z is None:
        return None
    return abs(float(z)) >= cutoff
