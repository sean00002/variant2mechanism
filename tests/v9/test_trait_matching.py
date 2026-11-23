"""Orthographic repair must not collapse traits or measurement scopes."""

import pytest

from variant2mechanism.v9.graph import ClaimGraph, GraphRefusal
from variant2mechanism.v9.traits import trait_identity, trait_query_match

from .test_graph import VARIANT, EntityRef, claim, dev_case, evidence


@pytest.mark.parametrize(("label", "source"), [
    ("Fetal haemoglobin levels", "Fetal hemoglobin levels"),
    ("mean corpuscular haemoglobin concentration (MCHC, mean, inv-norm transformed)",
     "mean corpuscular hemoglobin concentration (MCHC, mean, inv-norm transformed)"),
    ("Fetal haemoglobin in sickle cell disease (HbSS or HbSB0), transfusion-adjusted",
     "Fetal hemoglobin in Sickle cell disease (HbSS or HbSB0) (transfusion-adjusted)"),
])
def test_spelling_equivalents_attach_without_rewriting_observations(label, source):
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "associated_with_trait", [EntityRef(kind="phenotype", label=label)])
    eid = evidence(g, "association", source, about_traits=[source], about_variants=["rs1427407"])
    g.link(cid, eid, "supports", "computational_investigator", "Same source trait with UK spelling")
    assert g.links(cid)[0].evidence_id == eid
    assert g.evidence[eid].observed_result == source


def test_shared_ontology_id_preserves_scopes_and_survives_serialisation():
    g = ClaimGraph(dev_case())
    a = g.entity("phenotype", "haematocrit (mean)", "EFO:0004501")
    assert g.entity("phenotype", "hematocrit (mean)", "http://www.ebi.ac.uk/efo/EFO_0004501") == a
    b = g.entity("phenotype", "hematocrit (maximum)", "EFO_0004501")
    assert a != b
    restored = ClaimGraph.from_json(g.to_json())
    assert restored.entity("phenotype", "haematocrit (mean)", "EFO_0004501") == a
    assert restored.entity("phenotype", "haematocrit (maximum)", "EFO:0004501") == b


@pytest.mark.parametrize(("label", "source"), [
    ("hematocrit (mean)", "hematocrit (maximum)"),
    ("fetal hemoglobin in sickle cell disease", "fetal hemoglobin in healthy adults"),
    ("fetal hemoglobin", "adult hemoglobin"),
    ("LDL cholesterol", "VLDL cholesterol"),
])
def test_id_or_substring_cannot_override_different_labels(label, source):
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "associated_with_trait",
                [EntityRef(kind="phenotype", label=label, canonical_id="EFO_0004501")])
    eid = evidence(g, "association", source, about_traits=[source, "EFO_0004501"],
                   about_variants=["rs1427407"])
    with pytest.raises(GraphRefusal, match="about trait"):
        g.link(cid, eid, "supports", "computational_investigator")


def test_id_format_and_query_matching_are_conservative():
    assert trait_identity("EFO:0004576", None, ["http://www.ebi.ac.uk/efo/EFO_0004576"])
    # Different/incomplete mappings do not refute an identical full measured-trait label.
    assert trait_identity("fetal hemoglobin in sickle cell anemia", "MONDO_0011382",
                          ["fetal hemoglobin in sickle cell anemia", "EFO_0004576"])
    assert not trait_identity("fetal hemoglobin in sickle cell anemia", "EFO_0004576",
                              ["fetal hemoglobin in healthy adults", "EFO_0004576"])
    assert trait_query_match("fetal haemoglobin", ["Fetal hemoglobin in sickle cell disease"])
    assert trait_query_match("EFO:0004576", ["EFO_0004576"])
    assert not trait_query_match("LDL cholesterol", ["VLDL cholesterol"])
    assert not trait_query_match("", ["anything"])
