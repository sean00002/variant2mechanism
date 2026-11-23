"""Context matching: biosample identities stay distinct, proxies are labelled, missing context is unknown."""

import json

import pytest
import yaml

from variant2mechanism.config import REPO
from variant2mechanism.context.occupancy import MATCH_FILE
from variant2mechanism.v9 import context_match as cm
from variant2mechanism.v9.schemas import ContextScope, Variant


def scope(label: str, **kw) -> ContextScope:
    return cm.scope_from_label(label, **kw)


def compare(a: str, b: str) -> str:
    return cm.compare_context(scope(a), scope(b))


def test_hep3b_and_hepg2_are_distinct_and_proxy_at_best():
    hep3b, hepg2 = scope("Hep3B"), scope("HepG2")
    assert hep3b.biosample == "Hep 3B2.1-7" and hepg2.biosample == "HepG2"
    assert compare("Hep3B", "HepG2") == "proxy"
    assert compare("DepMap:ACH-000625 (Hep 3B2.1-7)", "HepG2") == "proxy"
    assert compare("DepMap:ACH-000625 (Hep 3B2.1-7)", "Hep 3B") == "exact"
    assert cm.load_table().declared_proxy("Hep 3B2.1-7", "HepG2")     # v8's declaration is read, not lost


def test_primary_hepatocytes_and_liver_tissue_are_proxies():
    assert compare("primary human hepatocytes", "liver") == "proxy"
    assert compare("primary hepatocytes", "hepatocyte") == "proxy"     # the ENCODE term may be differentiated cells
    assert compare("GTEx:Liver", "liver tissue") == "exact"
    assert compare("GTEx:Liver", "right lobe of liver") == "proxy"


def test_unrelated_known_contexts_are_different_and_unknown_names_unknown():
    assert compare("HepG2", "K562") == "different"
    assert compare("liver", "Whole Blood") == "different"
    assert compare("context X", "HepG2") == "unknown"         # an unrecognised name could be anything
    assert compare("context X", "context X") == "exact"


def test_missing_context_is_unknown_but_two_unscoped_sides_agree():
    assert cm.compare_context(None, scope("HepG2")) == "unknown"
    assert cm.compare_context(scope("none supplied"), scope("HepG2")) == "unknown"
    assert cm.compare_context(None, None) == "unknown"
    assert cm.link_applicability(None, None, context_free=True) == "exact"     # a coordinate fact against another
    assert cm.link_applicability(None, None, context_free=False) == "unknown"  # a cell assay that lost its context
    assert cm.link_applicability(None, scope("HepG2"), context_free=True) == "unknown"


def test_two_distinct_cell_lines_are_proxies_only_when_declared():
    assert compare("K562", "GM12878") == "different"            # both "blood", unrelated lines
    assert compare("HeLa-S3", "HeLa") == "proxy"                # a declared subline
    assert compare("Hep3B", "HepG2") == "proxy"                 # declared in both tables
    assert compare("primary hepatocytes", "HepG2") == "proxy"   # a primary cell shares its tissue with the line
    assert compare("liver", "HepG2") == "proxy"


def test_a_species_or_a_condition_alone_is_a_scope_and_the_record_kind_wins():
    mouse, stressed = ContextScope(species="mouse"), ContextScope(condition="ER stress")
    assert not cm.is_unscoped(mouse) and cm.scope_key(mouse) == "mouse:any"
    assert not cm.is_unscoped(stressed) and cm.scope_key(stressed) == "any|er stress"
    assert cm.link_applicability(None, mouse, context_free=True) == "unknown"
    assert cm.normalise_scope(ContextScope(label="HepG2", biosample_kind="organism")).biosample_kind == "cell_line"
    unknown = cm.normalise_scope(ContextScope(label="context X", biosample_kind="organism"))
    assert unknown.biosample_kind == "organism"                 # no record: the stated kind is all there is


def test_species_and_condition_never_give_exact():
    assert compare("mouse liver", "liver") == "proxy"
    assert scope("mouse liver").species == "mouse"
    stressed = scope("primary hepatocytes", condition="lipid-loaded")
    plain = scope("primary hepatocytes")
    assert cm.compare_context(stressed, plain) == "proxy"        # the claim's condition is not shown to be met
    assert cm.compare_context(plain, stressed) == "exact"        # a general claim, instantiated under a condition
    basal = scope("primary hepatocytes", condition="basal")
    assert cm.compare_context(stressed, basal) == "proxy"
    assert cm.scope_key(stressed) != cm.scope_key(basal)


def test_names_normalise_like_v8():
    assert scope("Hep G2 cells").biosample == "HepG2"
    assert scope("HCT 116").biosample == "HCT116"
    assert scope("MCF7").biosample == "MCF-7"
    assert scope("Muscle - Skeletal").tissue == "muscle"
    organ = scope("Thyroid")
    assert organ.biosample is None and organ.tissue == "thyroid"
    assert cm.compare_context(organ, scope("thyroid gland")) == "exact"


def test_genotype_at_the_variant_is_carried_when_a_source_states_it():
    rs12740374 = Variant(chrom="1", pos=109274968, ref="G", alt="T", rsid="rs12740374")
    assert scope("Hep3B", variant=rs12740374).genotype == "GG"
    assert scope("SK-HEP-1", variant=rs12740374).genotype == "GT"
    assert scope("HepG2", variant=rs12740374).genotype is None       # not stated, so not invented
    assert scope("Hep3B").genotype is None


def test_table_rejects_unknown_tissues_and_proxies(tmp_path):
    bad = {"tissues": {"liver": ["liver"]},
           "biosamples": [{"name": "A", "kind": "cell_line", "tissue": "lung"}]}
    (tmp_path / "bad.yaml").write_text(yaml.safe_dump(bad))
    with pytest.raises(ValueError, match="no keywords"):
        cm.load_table(tmp_path / "bad.yaml", tmp_path / "missing.yaml")
    bad["biosamples"] = [{"name": "A", "kind": "cell_line", "tissue": "liver", "proxies": ["B"]}]
    (tmp_path / "bad2.yaml").write_text(yaml.safe_dump(bad))
    with pytest.raises(ValueError, match="unknown proxy"):
        cm.load_table(tmp_path / "bad2.yaml", tmp_path / "missing.yaml")


def test_v8_match_file_lines_resolve_to_their_records():
    """Every DepMap line in v8's yaml is a v9 record with the same DepMap id (identities are reused, not edited)."""
    table = cm.load_table()
    for key, entry in yaml.safe_load(MATCH_FILE.read_text()).items():
        if key.startswith("DepMap:ACH-"):
            rec = table.record(key)
            assert rec is not None and rec.depmap == key.split(":", 1)[1]
            assert table.record(entry["line"]).name == rec.name


@pytest.mark.data
def test_every_screen_core_biosample_has_a_record():
    names = json.loads((REPO / "data" / "screen" / "core_biosamples.json").read_text())
    table = cm.load_table()
    assert {n: table.record(n) is not None for n in set(names)} == {n: True for n in set(names)}
    flagged = {r.name for r in table.records.values() if r.in_screen_core}
    assert flagged == set(names)
