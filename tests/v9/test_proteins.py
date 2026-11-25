"""Which proteins bind DNA by sequence (v9/proteins.py)."""

import json

from variant2mechanism.v9 import proteins, roles
from variant2mechanism.v9.schemas import QUALIFIED_DIRECT, QUALIFIED_DIRECT_FILL, Evidence, evidence_strength


class Paths:
    def __init__(self, files: dict):
        self.files = files

    def path(self, section: str, key: str):
        return self.files[(section, key)]


def census(tmp_path, with_hgnc: bool = True, with_groups: bool = True) -> Paths:
    lambert = tmp_path / "census.csv"
    lambert.write_text("Ensembl ID,HGNC symbol,DBD,Is TF?\n"
                       "ENSG01,GATA1,GATA,Yes\n"
                       "ENSG02,T,T-box,Yes\n"                  # renamed TBXT since the census
                       "ENSG03,BRD4,Unknown,No\n")
    hgnc = tmp_path / "hgnc.txt"
    hgnc.write_text("symbol\tstatus\tensembl_gene_id\n"
                    "GATA1\tApproved\tENSG01\nTBXT\tApproved\tENSG02\nBRD4\tApproved\tENSG03\n")
    groups = tmp_path / "groups.json"
    groups.write_text(json.dumps({"groups": [{"id": "G001", "tfs": ["ZFTA"]}]}))     # a model, and not in the census
    files = {("data", "lambert"): lambert}
    if with_hgnc:
        files[("data", "hgnc")] = hgnc
    if with_groups:
        files[("cache", "groups")] = groups
    return Paths(files)


def test_a_tf_is_on_the_census_under_todays_symbol_or_has_a_model(tmp_path):
    tfs = proteins.tf_symbols(census(tmp_path))
    assert tfs == {"GATA1", "T", "TBXT", "ZFTA"}
    assert [proteins.kind(s, tfs) for s in ("GATA1", "TBXT", "ZFTA", "BRD4")] == ["tf", "tf", "tf", "not_tf"]
    assert proteins.kind("gata1", tfs) == "tf" and proteins.kind(None, tfs) == "unknown"


def test_without_the_census_every_protein_is_unknown_and_the_other_files_are_optional(tmp_path):
    assert proteins.tf_symbols(None) is None and proteins.tf_symbols(Paths({})) is None
    assert proteins.kind("BRD4", None) == "unknown"
    bare = proteins.tf_symbols(census(tmp_path, with_hgnc=False, with_groups=False))
    assert bare == {"GATA1", "T"}                              # the census's own spelling only


def test_the_matrix_counts_co_factor_reads_for_activity_only_and_the_engines_prompt_does_not_change():
    def chip(**data) -> Evidence:
        return Evidence(evidence_class="occupancy", origin="tool", observed_result="reads", data=data,
                        independence_group="test")

    cofactor = chip(allele_specific=True, allele_specific_cofactor=True)
    tf = chip(allele_specific=True)
    assert evidence_strength("alters_regulatory_activity", cofactor) == "direct"
    assert evidence_strength("alters_regulatory_activity", tf) == "context"
    assert evidence_strength("alters_regulatory_activity", chip()) == "context"
    assert evidence_strength("alters_binding", tf) == "direct"
    # the fill's own entry: co-factor reads, and reads of open chromatin, which name no protein at all
    assert set(QUALIFIED_DIRECT_FILL.values()) == {(proteins.COFACTOR_FLAG, proteins.ACCESSIBILITY_FLAG)}
    open_chromatin = chip(allele_specific=True, allele_specific_accessibility=True)
    assert evidence_strength("alters_regulatory_activity", open_chromatin) == "direct"
    assert evidence_strength("alters_binding", chip(allele_specific_accessibility=True)) == "indirect"
    # the engine's prompts print QUALIFIED_DIRECT; the entry added for the fill must not reach them, or the saved
    # engine runs stop replaying
    assert not set(QUALIFIED_DIRECT_FILL) & set(QUALIFIED_DIRECT)
    assert "cofactor" not in roles.class_matrix_text()
