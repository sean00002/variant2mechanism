"""The gold claim specification (SPEC 10, 13.12): built mechanically, reproducible, hashed with the CSV's sha256 and
its reference files' (and refused once any of them changes), flagged for review where reading the CSV needs a
judgement, and never editing the CSV.

The component checks use tests/v9/fixtures/evaluation/dev_gold.csv: stipulated gold-format rows for the development
variant rs1427407, not claims about it. The committed eval/v9_gold_spec.json is only checked against its own CSV.
"""

import copy
import csv
import hashlib
import json
import shutil

import pytest

from variant2mechanism.config import REPO, Config
from variant2mechanism.v9.evaluation import (
    COMPONENTS,
    GOLD_SPEC_FILE,
    build_gold_spec,
    load_gold_spec,
    render_gold_spec,
    spec_entry,
    write_gold_spec,
)

pytestmark = pytest.mark.data       # HGNC and the Lambert table live in data/reference

DEV_CSV = REPO / "tests" / "v9" / "fixtures" / "evaluation" / "dev_gold.csv"
GOLD = REPO / "data" / "gold_set.csv"


def sha256(path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture
def dev_spec(v9_cfg) -> dict:
    return build_gold_spec(DEV_CSV, config=v9_cfg)


def test_the_spec_is_reproducible_and_hashed_with_its_csv(v9_cfg, tmp_path):
    before = sha256(DEV_CSV)
    first, second = build_gold_spec(DEV_CSV, config=v9_cfg), build_gold_spec(DEV_CSV, config=v9_cfg)
    assert first == second and render_gold_spec(first) == render_gold_spec(second)
    assert first["source"]["csv_sha256"] == before
    assert set(first["source"]) >= {"csv", "csv_sha256", "groups_sha256", "hgnc_sha256", "lambert_sha256",
                                    "biosamples_sha256"}
    assert first["status"] == "unreviewed" and first["rules"]
    out = write_gold_spec(tmp_path / "spec.json", csv_path=DEV_CSV, config=v9_cfg)
    assert out.read_text() == render_gold_spec(first)
    with pytest.raises(FileExistsError, match="review"):
        write_gold_spec(out, csv_path=DEV_CSV, config=v9_cfg)
    assert write_gold_spec(out, csv_path=DEV_CSV, config=v9_cfg, overwrite=True).read_text() == out.read_text()
    assert sha256(DEV_CSV) == before                       # the CSV is read, never edited


def test_a_spec_is_refused_once_its_csv_changes(v9_cfg, tmp_path):
    csv_copy = tmp_path / "gold.csv"
    shutil.copy(DEV_CSV, csv_copy)
    path = write_gold_spec(tmp_path / "spec.json", csv_path=csv_copy, config=v9_cfg)
    assert [c["case_id"] for c in load_gold_spec(path)["cases"]] == ["dev_member", "dev_ambiguous", "dev_uncovered",
                                                                      "dev_control"]
    csv_copy.write_text(csv_copy.read_text().replace("SORT1", "PSRC1", 1))
    with pytest.raises(ValueError, match="csv changed after the gold spec was built"):
        load_gold_spec(path)


def test_a_spec_is_refused_once_a_reference_file_changes(v9_cfg, tmp_path):
    """The components read the model-sharing groups (and HGNC, Lambert, the biosample table): a spec built from other
    groups than the current ones is stale, whatever the user's review settled."""
    groups = tmp_path / "groups.json"
    shutil.copy(v9_cfg.path("cache", "groups"), groups)
    cfg = Config({**copy.deepcopy(dict(v9_cfg)), "cache": {**v9_cfg["cache"], "groups": str(groups)}})
    path = write_gold_spec(tmp_path / "spec.json", csv_path=DEV_CSV, config=cfg)
    assert load_gold_spec(path, config=cfg)["status"] == "unreviewed"
    groups.write_text(groups.read_text() + "\n")
    with pytest.raises(ValueError, match="groups changed after the gold spec was built"):
        load_gold_spec(path, config=cfg)


def test_components_are_read_mechanically(dev_spec):
    entry = spec_entry(dev_spec, "dev_member")
    c = entry["components"]
    assert c["tf_member"]["tfs"] == ["CEBPA"]
    assert [g["id"] for g in c["tf_group"]["groups"]] == ["G035"]
    assert c["tf_group"]["groups"][0]["tfs"] == ["CEBPA", "CEBPB", "CEBPE"]
    assert c["tf_family"]["dbd"] == ["bZIP"] and c["tf_family"]["needs_review"]   # the CSV says C/EBP
    assert (c["direction"]["alt_direction"], c["direction"]["binds_more"]) == ("increases", "alt")
    assert c["target_gene"]["genes"] == ["SORT1"]
    assert [(s["label"], s["recognised"]) for s in c["context"]["scopes"]] == [("Liver", True), ("HepG2", True)]
    assert c["context"]["scopes"][1]["scope"]["biosample"] == "HepG2"
    assert (c["phenotype"]["labels"], c["phenotype"]["bracketed"]) == (["LDL cholesterol"], ["1p13"])
    assert entry["alternatives"] == []
    # The notes name POU5F1B, a TF in the Lambert list: a possible alternative TF and target gene, never accepted,
    # so both components wait for review (not just the entry).
    for name in ("tf_member", "target_gene"):
        assert c[name]["needs_review"] and any("POU5F1B" in r for r in c[name]["review_reasons"]), name
    assert not c["tf_group"]["needs_review"]
    assert entry["row"]["causal_tf"] == "CEBPA" and entry["row"]["source_pmid_or_ref"] == "12345678"
    assert entry["requests"]["main"]["disease"] == []
    assert entry["requests"]["supplied_disease"]["disease"] == ["LDL cholesterol"]
    assert entry["variant"]["key"] == "GRCh38:2:60490908:T:G" and entry["origin"] == "germline"


def test_judgement_calls_are_flagged_for_review_not_decided(dev_spec):
    c = spec_entry(dev_spec, "dev_ambiguous")["components"]
    assert len(c["tf_group"]["groups"]) > 1 and c["tf_group"]["needs_review"]   # HNF4A sits in several groups
    assert c["direction"]["alt_direction"] is None and c["direction"]["needs_review"]   # "gain" names no allele
    assert c["target_gene"]["genes"] == ["SORT1", "PSRC1"] and c["target_gene"]["needs_review"]
    assert c["context"]["needs_review"] and not c["context"]["scopes"][1]["recognised"]
    assert c["phenotype"]["labels"] == ["Coronary artery disease", "LDL cholesterol"]
    uncovered = spec_entry(dev_spec, "dev_uncovered")["components"]
    assert uncovered["tf_member"]["applicable"]
    assert not uncovered["tf_group"]["applicable"] and "capability" in uncovered["tf_group"]["reason"]
    # Not in coverage: naming a modelled relative is the failure the case tests, so family credit does not apply.
    assert not uncovered["tf_family"]["applicable"] and "not in QBiC-SELEX coverage" in uncovered["tf_family"]["reason"]
    assert uncovered["direction"]["alt_direction"] == "decreases"       # risk G (alt) disrupts the motif


def test_a_control_has_no_component_and_expects_the_null(dev_spec):
    entry = spec_entry(dev_spec, "dev_control")
    assert entry["control"] and not entry["needs_review"]
    assert all(not entry["components"][name]["applicable"] for name in COMPONENTS)
    assert entry["expected"].startswith("null") and "not an established biological null" in entry["expected"]
    with pytest.raises(KeyError, match="dev_member"):
        spec_entry(dev_spec, "rs0")


def test_the_committed_spec_matches_the_gold_csv(v9_cfg):
    spec = load_gold_spec()                                # refused if data/gold_set.csv changed since
    with open(GOLD, newline="") as f:
        assert [c["case_id"] for c in spec["cases"]] == [r["case_id"] for r in csv.DictReader(f)]
    if spec["status"] == "unreviewed":                     # until the user's review edits it, it is the mechanical build
        assert json.loads(GOLD_SPEC_FILE.read_text()) == build_gold_spec(GOLD, config=v9_cfg)
