"""No gold label reaches an agent through a tool spec (SPEC 13.12): every registered spec is shown to every role packet
of every case, so its descriptions, parameter docs and examples must name no gold TF, gene, group, context, disease,
variant or source. The examples once named a gold context (in two spellings), a gold TF's QBiC-SELEX group, and a gold
gene and variant.

These tests read data/gold_set.csv (never edited) and cache/groups.json only to prove that; nothing here chooses
anything by a gold row.
"""

import csv
import json
import re

import pytest

import variant2mechanism.v9.adapters  # noqa: F401  (registers the twelve computational tools)
import variant2mechanism.v9.literature  # noqa: F401  (registers the two literature tools)
from variant2mechanism.config import REPO
from variant2mechanism.v9.evaluation import find_label_strings, label_strings, label_strings_by_kind
from variant2mechanism.v9.tools import REGISTRY

pytestmark = pytest.mark.data

GOLD = REPO / "data" / "gold_set.csv"
GROUPS = REPO / "cache" / "groups.json"
TOOLS = {"variant_annotation", "ccre_overlap", "qbic_inventory", "qbic_tf_detail", "chip_occupancy", "gtex_eqtl",
         "tf_expression", "gwas_associations", "credible_sets_l2g", "depmap_context", "civic_lookup", "screen_online",
         "literature_search", "literature_read", "evidence_inspect"}
# Method and resource names the specs cannot do without. They reach the label strings only as identifier-like tokens
# of a row's free-text notes, or as the CIS-BP mapping vocabulary of its model and score columns (which SPEC 13.5 puts
# in every prompt), never as a case's TF, gene, group, context, disease, variant or source: allowed by kind only.
METHOD_TERMS = {"notes_tokens": {"chip", "dbsnp", "encode", "eqtl", "eqtls", "gtex", "hgnc", "l2g", "pip", "snp"},
                "tf": {"cis-bp", "cis-bp-mapped"}, "other": {"mapped"}}


def gold_rows() -> list[dict]:
    if not GOLD.exists() or not GROUPS.exists():
        pytest.skip("data/gold_set.csv or cache/groups.json is not present")
    with open(GOLD, newline="") as f:
        return list(csv.DictReader(f))


def spec_texts() -> dict[str, str]:
    """All a registered spec says (every field it serialises, and the form role packets show), per tool."""
    return {name: json.dumps(REGISTRY.spec(name).model_dump()) + json.dumps(REGISTRY.spec(name).describe())
            for name in REGISTRY.names()}


def gold_group_ids(rows: list[dict]) -> set[str]:
    """The QBiC-SELEX model-sharing groups holding a gold TF (each cell split on , ; / and brackets)."""
    tfs = {x.strip().upper() for row in rows for x in re.split(r"[,;/()]", row["causal_tf"]) if x.strip()}
    return {g["id"] for g in json.loads(GROUPS.read_text())["groups"]
            if tfs & {str(t).upper() for t in g.get("tfs") or ()}}


def test_no_tool_spec_names_a_gold_label(v9_cfg):
    rows, texts = gold_rows(), spec_texts()
    assert len(rows) == 15 and set(texts) == TOOLS
    leaks = []
    for row in rows:
        kinds = label_strings_by_kind(row, config=v9_cfg)
        assert set().union(*kinds.values()) == label_strings(row, config=v9_cfg)
        for kind, strings in kinds.items():
            for tool, text in texts.items():
                leaks += [(row["case_id"], kind, tool, s) for s in find_label_strings(text, strings)
                          if s.casefold() not in METHOD_TERMS.get(kind, set())]
    assert leaks == []
    groups = gold_group_ids(rows)
    assert groups and [(tool, g) for tool, text in texts.items() for g in find_label_strings(text, groups)] == []


def test_the_method_terms_allowed_are_never_a_case_label(v9_cfg):
    """The allowance above holds only for method vocabulary: none of its terms is any row's TF, gene, group, context,
    disease, variant, bracketed text or source."""
    allowed = set().union(*METHOD_TERMS.values())
    for row in gold_rows():
        kinds = label_strings_by_kind(row, config=v9_cfg)
        for kind in ("identity", "gene", "group", "context", "disease", "bracketed", "source"):
            assert not {s.casefold() for s in kinds[kind]} & allowed, (row["case_id"], kind)
        assert not find_label_strings(f"{row['causal_tf']} | {row['tf_family']}", allowed), row["case_id"]
