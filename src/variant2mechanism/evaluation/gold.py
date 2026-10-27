"""The gold set: which columns a run may see, which are labels, and how controls are recognised.

Only PROMPT_COLUMNS ever reach a case header. The label columns, the source and the notes are for scoring and
for people; they never go into a prompt.
"""

import pandas as pd

from ..config import Config, load_config

PROMPT_COLUMNS = ("case_id", "variant", "chrom", "pos_grch38", "ref", "alt", "origin", "disease_or_trait",
                  "expression_context")
LABEL_COLUMNS = ("causal_tf", "tf_family", "direction", "target_gene", "tissue_or_cell_type", "qbic_model",
                 "score_level", "label_class")
NEVER_IN_PROMPT = LABEL_COLUMNS + ("source_pmid_or_ref", "notes")
NONE_VALUES = {"", "none", "nan", "not applicable", "n/a"}


def load_gold(cfg: Config | None = None) -> pd.DataFrame:
    cfg = cfg or load_config()
    return pd.read_csv(cfg.path("eval", "gold_set"), dtype=str, keep_default_na=False)


def excluded(cfg: Config | None = None) -> dict[str, str]:
    """Cases taken out of the evaluation (eval.exclude), with the reason. Their rows stay in the gold set."""
    cfg = cfg or load_config()
    return dict(cfg["eval"].get("exclude") or {})


def scored_cases(gold: pd.DataFrame, cfg: Config | None = None) -> pd.DataFrame:
    """The gold set without the excluded cases: what the grid runs and the metrics score."""
    return gold[~gold.case_id.isin(excluded(cfg))]


def is_control(row) -> bool:
    """Controls: label_class control_* or score_level control or causal_tf none. The correct answer is the null."""
    get = row.get if hasattr(row, "get") else lambda k, d="": getattr(row, k, d)
    label = str(get("label_class", "")).strip().lower()
    level = str(get("score_level", "")).strip().lower()
    tf = str(get("causal_tf", "")).strip().lower()
    return label.startswith("control") or label == "mutational_process" or level == "control" or tf in NONE_VALUES


def scoring_tf(row) -> str | None:
    """The TF a case is scored on: the first one listed; None for controls."""
    if is_control(row):
        return None
    get = row.get if hasattr(row, "get") else lambda k, d="": getattr(row, k, d)
    return str(get("causal_tf", "")).split(",")[0].strip() or None
