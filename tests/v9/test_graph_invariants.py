"""Regression tests for the v9 core review: each test replays a scenario that once broke a scientific invariant of the
claim graph (identity, allele frame, gates, concurrency, anti-repeat, elimination, context, evidence entry).

Biological cases use the development variant rs1427407 (chr2:60490908 T>G, so ref T, alt G); TF and gene symbols,
genotypes and observations are stipulated for the tests and are not claims about that variant.
"""

import json
import math

import numpy as np
import pytest

from variant2mechanism.v9.graph import (
    ClaimDraft,
    ClaimGraph,
    EntityRef,
    GraphRefusal,
    GraphUpdate,
    GroupRegistry,
    HypothesisChanges,
    HypothesisDraft,
    SymbolResolver,
)
from variant2mechanism.v9.schemas import (
    Case,
    ContextScope,
    Evidence,
    ExperimentRecord,
    ExperimentSystem,
    ToolCall,
    Variant,
    evidence_strength,
)

VARIANT = EntityRef(kind="variant", label="rs1427407")
ELEMENT = EntityRef(kind="element", label="enhancer", canonical_id="EH38E0000001")
ABOUT_ELEMENT = ["EH38E0000001"]          # evidence about what the element does names it (about_elements)
ABOUT_VARIANT = ["rs1427407"]             # evidence comparing the case variant's alleles names it (about_variants)
LDL = EntityRef(kind="phenotype", label="LDL cholesterol")


def dev_case() -> Case:
    return Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"))


@pytest.fixture
def g() -> ClaimGraph:
    return ClaimGraph(dev_case())


def ctx(label: str, **kw) -> ContextScope:
    return ContextScope(label=label, source="supplied", **kw)


def tf(symbol: str) -> EntityRef:
    return EntityRef(kind="tf", label=symbol)


def gene(symbol: str) -> EntityRef:
    return EntityRef(kind="gene", label=symbol)


def claim(g: ClaimGraph, subjects, relation, objects, direction="unspecified", context=None, deps=(), **kw) -> str:
    return g.add_claim(ClaimDraft(subjects=subjects, relation=relation, objects=objects, direction=direction,
                                  context=context, dependencies=list(deps), **kw), "coordinator")


def record(g: ClaimGraph, evidence=(), tool="test_tool", retrieval_status="records_found", **kw) -> ToolCall:
    tid = g.reserve_tool_call_id()
    return g.record_tool_call(ToolCall(tool_call_id=tid, tool_name=tool, execution_status="success",
                                       retrieval_status=retrieval_status, requested_by="computational_investigator",
                                       charged_to="agent", **kw), list(evidence))


def evidence(g: ClaimGraph, cls: str, text: str, **kw) -> str:
    ev = Evidence(evidence_class=cls, observed_result=text, independence_group=kw.pop("group", text), origin="tool",
                  **kw)
    return record(g, [ev]).evidence_ids[0]


def hypothesis(g: ClaimGraph, required, optional=(), title="H", mechanism="regulatory", **kw) -> str:
    return g.add_hypothesis(HypothesisDraft(title=title, claim_ids=list(optional), required_claim_ids=list(required),
                                            mechanism_class=mechanism, **kw), "coordinator")


def version(g: ClaimGraph, claim_id: str) -> int:
    return g.claims[claim_id].version


def contradict(g: ClaimGraph, claim_id: str, evidence_id: str) -> None:
    """Link a matched contradiction and assess it (as the critic)."""
    g.link(claim_id, evidence_id, "contradicts", "computational_investigator", "matched test")
    g.assess(claim_id, "contradicted_in_scope", "matched contradiction", "critic", version(g, claim_id))


# --- identity: every kind, element and trait (H1) -------------------------------------------------------------------

def test_a_binding_claim_must_name_the_factor_as_a_tf_group_or_complex(g):
    for kind in ("gene", "binding_event"):
        with pytest.raises(GraphRefusal, match="names the bound factor as a tf, tf_group or complex"):
            claim(g, [EntityRef(kind=kind, label="CEBPB")], "occupies", [ELEMENT], context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="bound factor"):
        claim(g, [VARIANT], "alters_binding", [gene("CEBPB")], "increases", ctx("HepG2"))
    chip = evidence(g, "occupancy", "CEBPA ChIP-seq peak over the variant in HepG2", about_tfs=["CEBPA"],
                    context=ctx("HepG2"))
    bare = claim(g, [EntityRef(kind="complex", label="CEBPB complex")], "occupies", [ELEMENT], context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="lists no member TFs"):
        g.link(bare, chip, "supports", "computational_investigator", "peak")
    dimer = claim(g, [EntityRef(kind="complex", label="CEBPA:CEBPB", members=["CEBPA", "CEBPB"])], "occupies",
                  [ELEMENT], context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="needs every member"):
        g.link(dimer, chip, "supports", "computational_investigator", "a CEBPA peak is not the heterodimer")
    assert g.claims[bare].evidence_links == g.claims[dimer].evidence_links == []


def test_genes_transcripts_elements_and_traits_are_matched_to_what_the_evidence_is_about(g):
    psrc1 = evidence(g, "perturbation", "CRISPRi of the element lowers PSRC1 in HepG2", about_genes=["PSRC1"],
                     about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    sort1 = claim(g, [ELEMENT], "regulates", [EntityRef(kind="transcript", label="SORT1")], "increases", ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="not transcript SORT1"):
        g.link(sort1, psrc1, "supports", "computational_investigator", "CRISPRi")
    other_element = evidence(g, "reporter_assay", "Luciferase: EH38E0000002 G allele 3x higher in HepG2", allele="G",
                             about_elements=["EH38E0000002"], direction="increases", context=ctx("HepG2"))
    activity = claim(g, [VARIANT], "alters_regulatory_activity", [ELEMENT], "increases", ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="not EH38E0000001"):
        g.link(activity, other_element, "supports", "computational_investigator", "reporter")
    construct = evidence(g, "reporter_assay", "Luciferase: the variant's G allele construct 3x higher in HepG2",
                         allele="G", direction="increases", context=ctx("HepG2"), about_variants=ABOUT_VARIANT)
    assert g.link(activity, construct, "supports", "computational_investigator", "allelic constructs").strength == \
        "direct"                                    # a construct naming no accession is not about another element
    overlap = claim(g, [VARIANT], "overlaps", [ELEMENT])
    for about in (["EH38E0000002"], []):           # an overlap must name the element it overlaps
        ann = evidence(g, "annotation", f"variant overlap ({about})", about_elements=about)
        with pytest.raises(GraphRefusal, match="not EH38E0000001"):
            g.link(overlap, ann, "supports", "computational_investigator", "overlap")
    height = evidence(g, "association", "GWAS: G allele associated with taller height", allele="G",
                      direction="increases", about_traits=["body height"])
    ldl = claim(g, [VARIANT], "associated_with_trait", [LDL], "increases")
    with pytest.raises(GraphRefusal, match="not LDL cholesterol"):
        g.link(ldl, height, "supports", "computational_investigator", "GWAS")
    gwas = evidence(g, "association", "GWAS: G allele associated with higher LDL-cholesterol", allele="G",
                    direction="increases", about_traits=["LDL-Cholesterol", "EFO_0004611"])
    assert g.link(ldl, gwas, "supports", "computational_investigator", "GWAS").strength == "direct"
    minigene = evidence(g, "reporter_assay", "GENE2 minigene: G allele skips exon 3", allele="G",
                        about_genes=["GENE2"], direction="increases", context=ctx("HepG2"))
    rna = claim(g, [VARIANT], "alters_rna", [gene("GENE1")], "increases", ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="not gene GENE1"):
        g.link(rna, minigene, "supports", "computational_investigator", "minigene")


def test_group_members_are_fixed_at_creation(g):
    grp = EntityRef(kind="tf_group", label="group G035", canonical_id="G035", members=["CEBPA", "CEBPB"])
    b = claim(g, [VARIANT], "alters_binding", [grp], "increases", ctx("HepG2"))
    hnf = evidence(g, "binding_assay", "EMSA: HNF4A binds the G allele more strongly (HepG2 extract)",
                   about_tfs=["HNF4A"], allele="G", direction="increases", context=ctx("HepG2"))
    widened = grp.model_copy(update={"members": ["HNF4A"]})
    n_events = len(g.events)
    with pytest.raises(GraphRefusal, match="fixed when it was created"):
        claim(g, [widened], "expressed_in", [EntityRef(kind="context", label="HepG2")], context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="fixed when it was created"):   # a duplicate draft cannot widen it either
        claim(g, [VARIANT], "alters_binding", [widened], "increases", ctx("HepG2"))
    gid = g.claims[b].object_ids[0]
    assert [g.entities[p].label for p in g.entities[gid].participants] == ["CEBPA", "CEBPB"]
    assert len(g.events) == n_events and not any(e.label == "HNF4A" for e in g.entities.values())
    with pytest.raises(GraphRefusal, match="none of the members"):
        g.link(b, hnf, "supports", "computational_investigator", "HNF4A EMSA")


def test_registry_groups_take_their_members_from_the_registry(tmp_path):
    groups = tmp_path / "groups.json"
    groups.write_text(json.dumps({"settings": {}, "groups": [
        {"id": "G035", "label": "bZIP, 3 models", "tfs": ["CEBPA", "CEBPB", "CEBPE"], "models": []}]}))
    g = ClaimGraph(dev_case(), groups=GroupRegistry.from_groups_json(groups))
    c = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf_group", label="G035", canonical_id="G035")],
              "increases")
    gid = g.claims[c].object_ids[0]
    assert [g.entities[p].label for p in g.entities[gid].participants] == ["CEBPA", "CEBPB", "CEBPE"]
    with pytest.raises(GraphRefusal, match="QBiC-SELEX group registry"):
        claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf_group", label="G035", canonical_id="G035",
                                                         members=["HNF4A"])], "decreases")
    adhoc = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf_group", label="CEBP paralogs",
                                                             members=["CEBPA", "CEBPD", "CEBPG"])], "increases")
    assert len(g.entities[g.claims[adhoc].object_ids[0]].participants) == 3   # an ad hoc group keeps its own list
    again = ClaimGraph.from_json(g.to_json(), groups=g.groups)
    assert again.to_state() == g.to_state()


# --- allele frame and direction (H2) --------------------------------------------------------------------------------

def test_directions_are_read_in_the_claims_allele_frame(g):
    c = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", ctx("HepG2"))
    assert g.claims[c].effect_allele == "G"                               # the alt allele unless stated
    ref_more = evidence(g, "binding_assay", "EMSA in HepG2 extract: TFX binds the T allele more strongly",
                        about_tfs=["TFX"], allele="T", direction="increases", context=ctx("HepG2"),
                        about_variants=ABOUT_VARIANT)
    with pytest.raises(GraphRefusal, match="opposite"):
        g.link(c, ref_more, "supports", "computational_investigator", "EMSA")
    alt_more = evidence(g, "binding_assay", "EMSA (second gel): TFX binds the G allele more strongly",
                        about_tfs=["TFX"], allele="g allele", direction="increases", context=ctx("HepG2"),
                        about_variants=ABOUT_VARIANT)
    with pytest.raises(GraphRefusal, match="agrees with the claim"):
        g.link(c, alt_more, "contradicts", "computational_investigator", "x")
    other = evidence(g, "binding_assay", "EMSA: binding differs for allele C", about_tfs=["TFX"], allele="C",
                     direction="increases", context=ctx("HepG2"), about_variants=ABOUT_VARIANT)
    with pytest.raises(GraphRefusal, match="neither ref T nor alt G"):
        g.link(c, other, "supports", "computational_investigator", "x")
    no_allele = evidence(g, "binding_assay", "EMSA: TFX binding increases", about_tfs=["TFX"],
                         direction="increases", context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="cannot be placed"):
        g.link(c, no_allele, "supports", "computational_investigator", "x")
    assert g.link(c, ref_more, "contradicts", "computational_investigator", "T binds more").stance == "contradicts"
    assert g.link(c, alt_more, "supports", "computational_investigator", "G binds more").stance == "supports"
    g.assess(c, "contested", "the two gels disagree", "critic", version(g, c))


def test_one_proposition_in_either_allele_frame_is_one_claim(g):
    alt = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", ctx("HepG2"))
    ref = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "decreases", ctx("HepG2"), effect_allele="T")
    assert ref == alt
    flipped = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", ctx("HepG2"), effect_allele="ref")
    assert flipped != alt and g.claims[flipped].effect_allele == "T"
    assert g.signature("tf_binding", [alt]) != g.signature("tf_binding", [flipped])
    with pytest.raises(GraphRefusal, match="neither ref T nor alt G"):
        claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", effect_allele="C")
    with pytest.raises(GraphRefusal, match="names a variant"):
        claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", effect_allele="G")


def test_agreement_never_contradicts_and_no_change_is_opposite_to_any_effect(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    h = hypothesis(g, [c])
    same = evidence(g, "perturbation", "CRISPRi of the element lowers GENE1 (the element increases GENE1)",
                    about_genes=["GENE1"], about_elements=ABOUT_ELEMENT, direction="increases",
                    context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="agrees with the claim"):
        g.link(c, same, "contradicts", "computational_investigator", "contradicts")
    with pytest.raises(GraphRefusal):
        g.assess(c, "contradicted_in_scope", "x", "critic", version(g, c))
    assert g.hypotheses[h].disposition == "active"
    with pytest.raises(GraphRefusal, match="measured null"):
        evidence(g, "reporter_assay", "Luciferase in HepG2: no difference between G and T constructs",
                 direction="no_change", context=ctx("HepG2"))
    none = claim(g, [VARIANT], "alters_regulatory_activity", [ELEMENT], "no_change", ctx("HepG2"))
    up = evidence(g, "reporter_assay", "Luciferase in HepG2: G construct 3x higher", allele="G",
                  direction="increases", context=ctx("HepG2"), about_variants=ABOUT_VARIANT)
    with pytest.raises(GraphRefusal, match="claims no change"):
        g.link(none, up, "supports", "computational_investigator", "reporter")
    assert g.link(none, up, "contradicts", "computational_investigator", "an effect").stance == "contradicts"
    null = evidence(g, "reporter_assay", "Luciferase in HepG2: no difference between G and T constructs",
                    context=ctx("HepG2"), result_kind="null_in_assessed_scope",
                    assessed_relation="alters_regulatory_activity")
    with pytest.raises(GraphRefusal, match="agrees with"):
        g.link(none, null, "contradicts", "computational_investigator", "a null")
    assert g.link(none, null, "supports", "computational_investigator", "a null").stance == "supports"
    undirected = claim(g, [ELEMENT], "regulates", [gene("GENE2")], context=ctx("HepG2"))
    up2 = evidence(g, "perturbation", "activating the element raises GENE2", about_genes=["GENE2"],
                   about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="states no direction"):
        g.link(undirected, up2, "contradicts", "computational_investigator", "x")


# --- elimination needs a contradicted required claim (H3, M2) -------------------------------------------------------

def test_replaces_must_keep_the_required_claims_of_the_hypothesis_it_retires(g):
    cebpa = claim(g, [VARIANT], "alters_binding", [tf("CEBPA")], "increases", ctx("HepG2"))
    hnf4a = claim(g, [VARIANT], "alters_binding", [tf("HNF4A")], "increases", ctx("HepG2"))
    h1 = hypothesis(g, [cebpa], mechanism="tf_binding", title="CEBPA")
    with pytest.raises(GraphRefusal, match=f"retire {h1} without a contradicted required claim"):
        hypothesis(g, [hnf4a], mechanism="tf_binding", title="HNF4A instead", replaces=h1)
    assert g.hypotheses[h1].disposition == "active"
    reg = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    newer = claim(g, [VARIANT], "alters_binding", [tf("CEBPB")], "increases", ctx("HepG2"))
    h0 = hypothesis(g, [newer, reg], mechanism="tf_binding", title="to be revised")
    swapped = g.supersede_claim(newer, ClaimDraft(subjects=[VARIANT], relation="alters_binding", objects=[tf("CEBPE")],
                                                  direction="increases", context=ctx("HepG2")),
                                "the member is CEBPE", "coordinator")
    h2 = hypothesis(g, [cebpa, reg], mechanism="tf_binding", title="CEBPA and its target", replaces=h1)
    assert g.hypotheses[h1].disposition == "superseded" and g.hypotheses[h1].disposition_reason == f"replaced by {h2}"
    h3 = hypothesis(g, [swapped, reg], mechanism="tf_binding", title="CEBPE", replaces=h0)   # a superseded claim's
    assert g.hypotheses[h0].disposition == "superseded" and h3 in g.hypotheses              # replacement counts


def test_investigators_cannot_edit_hypotheses(g):
    good = claim(g, [VARIANT], "alters_binding", [tf("CEBPA")], "increases", ctx("HepG2"))
    h = hypothesis(g, [good], mechanism="tf_binding")
    other = claim(g, [ELEMENT], "regulates", [gene("GENE9")], "decreases", ctx("HepG2"))
    contradict(g, other, evidence(g, "perturbation", "activating the element raises GENE9", about_genes=["GENE9"],
                                  about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2")))
    draft = ClaimDraft(subjects=[ELEMENT], relation="regulates", objects=[gene("GENE9")], direction="decreases",
                       context=ctx("HepG2"))
    replacement = ClaimDraft(subjects=[VARIANT], relation="alters_binding", objects=[tf("CEBPB")],
                             direction="increases", context=ctx("HepG2"))
    _, refused = g.apply_updates([
        GraphUpdate(kind="new_claim", hypothesis_id=h, required=True, reason="needed", claim=draft),
        GraphUpdate(kind="new_claim", required=True, reason="needed", claim=draft),
        GraphUpdate(kind="supersede_claim", claim_id=good, claim=replacement, reason="other member",
                    hypothesis_ids=[h]),
    ], "literature_investigator")
    assert len(refused) == 3 and all("coordinator's" in o.reason for o in refused)
    assert g.hypotheses[h].required_claim_ids == [good] and g.hypotheses[h].disposition == "active"
    with pytest.raises(GraphRefusal, match="cannot become a required claim"):   # nor can the coordinator
        g.add_claim_to_hypothesis(h, other, True, "make it required", "coordinator")
    with pytest.raises(GraphRefusal, match="cannot become a required claim"):
        hypothesis(g, [other], title="built on a contradicted claim")


def test_a_contradiction_rejects_at_once_and_cannot_be_repaired_away(g):
    f1 = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    keep = claim(g, [VARIANT], "overlaps", [ELEMENT])
    h1 = hypothesis(g, [f1, keep], title="E represses GENE1")
    s1 = evidence(g, "perturbation", "activating E raises GENE1", about_genes=["GENE1"], direction="increases",
                  about_elements=ABOUT_ELEMENT, context=ctx("HepG2"))
    accepted, refused = g.apply_updates([
        GraphUpdate(kind="attach_evidence", claim_id=f1, evidence_id=s1, stance="contradicts", rationale="matched",
                    suggested_assessment="contradicted_in_scope", base_version=1),
        GraphUpdate(kind="supersede_claim", claim_id=f1, reason="sign corrected to fit S1", hypothesis_ids=[h1],
                    claim=ClaimDraft(subjects=[ELEMENT], relation="regulates", objects=[gene("GENE1")],
                                     direction="increases", context=ctx("HepG2"))),
        GraphUpdate(kind="revise_hypothesis", hypothesis_id=h1, reason="drop it",
                    changes=HypothesisChanges(remove_claim_ids=[f1])),
        GraphUpdate(kind="assess", claim_id=f1, assessment="unresolved", base_version=1, rationale="not convinced"),
    ], "coordinator")
    assert [o.kind for o in accepted] == ["attach_evidence", "assess", "assess"]
    assert [o.kind for o in refused] == ["supersede_claim", "revise_hypothesis"]
    assert all("final" in o.reason for o in refused)
    hyp = g.hypotheses[h1]
    assert (hyp.disposition, hyp.version, hyp.required_claim_ids) == ("rejected", 1, [f1, keep])
    assert g.claims[f1].assessment == "unresolved"            # the claim can be reassessed; the rejection stands


# --- anti-repeat through canonical ids (H4) -------------------------------------------------------------------------

def reject_cebpa(g: ClaimGraph) -> tuple[str, str]:
    c = claim(g, [VARIANT], "alters_binding", [tf("CEBPA")], "increases", ctx("HepG2"))
    h = hypothesis(g, [c], mechanism="tf_binding", title="CEBPA")
    contradict(g, c, evidence(g, "binding_assay", "EMSA in HepG2 extract: CEBPA binds the G allele less",
                              about_tfs=["CEBPA"], allele="G", direction="decreases", context=ctx("HepG2"),
                              about_variants=ABOUT_VARIANT))
    assert g.hypotheses[h].disposition == "rejected"
    return c, h


def test_a_canonical_id_added_later_cannot_reopen_a_rejected_story(g):
    c, h1 = reject_cebpa(g)
    signature = g.hypotheses[h1].signature
    claim(g, [EntityRef(kind="tf", label="CEBPA", canonical_id="HGNC:1833")], "expressed_in",
          [EntityRef(kind="context", label="HepG2")], context=ctx("HepG2"))
    assert g.signature("tf_binding", [c]) == signature
    liver = claim(g, [VARIANT], "alters_binding", [tf("CEBPA")], "increases", ctx("liver"))
    # A matched HepG2 contradiction does not reject a distinct liver-scope claim.
    assert hypothesis(g, [liver], mechanism="tf_binding", origin="regenerated") != h1
    with pytest.raises(GraphRefusal, match=f"repeats rejected hypothesis {h1}"):
        hypothesis(g, [c], mechanism="tf_binding", origin="regenerated")


def test_the_hgnc_id_wins_over_a_proposers_id(tmp_path):
    hgnc = tmp_path / "hgnc.txt"
    hgnc.write_text("hgnc_id\tsymbol\tstatus\tprev_symbol\nHGNC:1833\tCEBPA\tApproved\t\n")
    g = ClaimGraph(dev_case(), resolver=SymbolResolver.from_hgnc(hgnc))
    c, h1 = reject_cebpa(g)
    bogus = EntityRef(kind="tf", label="CEBPA", canonical_id="CEBPA-model-1")
    dup = claim(g, [VARIANT], "alters_binding", [bogus], "increases", ctx("HepG2"))
    assert dup == c and [e.canonical_id for e in g.entities.values() if e.label == "CEBPA"] == ["HGNC:1833"]
    with pytest.raises(GraphRefusal, match="repeats rejected"):
        hypothesis(g, [dup], mechanism="tf_binding", origin="regenerated")


# --- gates and concurrency (H5, M1) ---------------------------------------------------------------------------------

def test_direct_evidence_on_both_sides_makes_a_claim_contested(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    h = hypothesis(g, [c])
    up = evidence(g, "perturbation", "CRISPRi lowers GENE1 (the element increases GENE1)", about_genes=["GENE1"],
                  about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    down = evidence(g, "perturbation", "CRISPRa of the element lowers GENE1", about_genes=["GENE1"],
                    about_elements=ABOUT_ELEMENT, direction="decreases", context=ctx("HepG2"))
    g.link(c, up, "supports", "computational_investigator", "CRISPRi")
    g.link(c, down, "contradicts", "computational_investigator", "CRISPRa opposite")
    for assessment in ("supported_in_scope", "contradicted_in_scope"):
        with pytest.raises(GraphRefusal, match="contested"):
            g.assess(c, assessment, "pick one", "critic", version(g, c))
    g.assess(c, "contested", "CRISPRi and CRISPRa disagree", "critic", version(g, c))
    assert g.hypotheses[h].disposition == "active"


def test_every_link_bumps_the_version_so_an_older_reading_is_stale(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    g.link(c, evidence(g, "perturbation", "CRISPRi lowers GENE1", about_genes=["GENE1"], direction="increases",
                       about_elements=ABOUT_ELEMENT, context=ctx("HepG2")),
           "supports", "computational_investigator", "CRISPRi")
    seen = version(g, c)
    late = evidence(g, "perturbation", "deletion of the element raises GENE1", about_genes=["GENE1"],
                    about_elements=ABOUT_ELEMENT, direction="decreases", context=ctx("HepG2"))
    g.apply_updates([GraphUpdate(kind="attach_evidence", claim_id=c, evidence_id=late, stance="contradicts",
                                 rationale="deletion raises GENE1")], "literature_investigator")
    assert version(g, c) == seen + 1 and g.claims[c].history[-1].action == "attach_evidence"
    _, refused = g.apply_updates([GraphUpdate(kind="assess", claim_id=c, assessment="supported_in_scope",
                                              base_version=seen, rationale="CRISPRi supports")], "critic")
    assert "stale update" in refused[0].reason and g.claims[c].assessment == "unassessed"


def test_a_batch_never_goes_stale_on_its_own_changes(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    first = evidence(g, "perturbation", "CRISPRi lowers GENE1", about_genes=["GENE1"], direction="increases",
                     about_elements=ABOUT_ELEMENT, context=ctx("HepG2"))
    second = evidence(g, "perturbation", "a second guide lowers GENE1", about_genes=["GENE1"],
                      about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    accepted, refused = g.apply_updates([
        GraphUpdate(kind="attach_evidence", claim_id=c, evidence_id=first, stance="supports", rationale="guide 1"),
        GraphUpdate(kind="attach_evidence", claim_id=c, evidence_id=second, stance="supports", rationale="guide 2",
                    suggested_assessment="supported_in_scope", base_version=1),
    ], "computational_investigator")
    assert refused == [] and g.claims[c].assessment == "supported_in_scope" and version(g, c) == 4


def test_a_held_assessment_is_reset_when_its_links_no_longer_meet_its_gate(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    crispr = evidence(g, "perturbation", "CRISPRi lowers GENE1", about_genes=["GENE1"], direction="increases",
                      about_elements=ABOUT_ELEMENT, context=ctx("HepG2"))
    g.link(c, crispr, "supports", "computational_investigator", "CRISPRi")
    g.assess(c, "supported_in_scope", "CRISPRi", "critic", version(g, c))
    down = evidence(g, "perturbation", "CRISPRa of the element lowers GENE1", about_genes=["GENE1"],
                    about_elements=ABOUT_ELEMENT, direction="decreases", context=ctx("HepG2"))
    g.link(c, down, "contradicts", "literature_investigator", "an opposite activation result")
    reset = g.events[-1]
    assert g.claims[c].assessment == "unresolved"
    assert (reset.action, reset.role, reset.details["automatic"]) == ("assess", "code", True)
    g.assess(c, "contested", "activation and interference disagree", "critic", version(g, c))


def test_a_first_link_can_be_revised_and_the_revision_is_recorded(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    h = hypothesis(g, [c])
    s1 = evidence(g, "perturbation", "activating E raises GENE1 in HepG2", about_genes=["GENE1"],
                  about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    weak = g.link(c, s1, "contradicts", "computational_investigator", "maybe not the same scope",
                  applicability="unknown")
    assert (weak.applicability, weak.code_applicability) == ("unknown", "exact")
    with pytest.raises(GraphRefusal, match="contradicted_in_scope needs"):
        g.assess(c, "contradicted_in_scope", "matched", "critic", version(g, c))
    before = version(g, c)
    assert g.link(c, s1, "contradicts", "critic", "the same again", applicability="unknown") == weak
    assert version(g, c) == before
    fixed = g.link(c, s1, "contradicts", "critic", "same line, same intervention")
    assert fixed.applicability == "exact" and fixed.revises == weak.event_id
    assert g.claims[c].evidence_links == [fixed] and g.events[-1].supersedes == [weak.event_id]
    g.assess(c, "contradicted_in_scope", "matched", "critic", version(g, c))
    assert g.hypotheses[h].disposition == "rejected"
    other = claim(g, [ELEMENT], "regulates", [gene("GENE2")], "increases", ctx("HepG2"))
    crispr = evidence(g, "perturbation", "CRISPRi lowers GENE2 in HepG2", about_genes=["GENE2"],
                      about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    g.link(other, crispr, "context_only", "literature_investigator", "background")
    g.link(other, crispr, "supports", "computational_investigator", "CRISPRi")
    g.assess(other, "supported_in_scope", "CRISPRi", "critic", version(g, other))
    g.link(other, crispr, "context_only", "critic", "the passage was misread")
    assert g.claims[other].assessment == "unresolved"                    # its basis was withdrawn


# --- context (H6) ---------------------------------------------------------------------------------------------------

def test_a_lost_context_is_never_exact_for_cell_assays_or_nulls(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases")
    crispr = evidence(g, "perturbation", "CRISPRi of the element lowers GENE1", about_genes=["GENE1"],
                      about_elements=ABOUT_ELEMENT, direction="increases")
    assert g.link(c, crispr, "supports", "literature_investigator", "CRISPRi").applicability == "unknown"
    with pytest.raises(GraphRefusal, match="supported_in_scope needs"):
        g.assess(c, "supported_in_scope", "CRISPRi", "critic", version(g, c))
    overlap = claim(g, [VARIANT], "overlaps", [ELEMENT])
    ann = evidence(g, "annotation", "the variant lies in EH38E0000001", about_elements=["EH38E0000001"])
    assert g.link(overlap, ann, "supports", "computational_investigator", "overlap").applicability == "exact"
    assoc = claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    h = hypothesis(g, [assoc])
    null = evidence(g, "association", "eQTL test for GENE1: not significant", about_genes=["GENE1"],
                    result_kind="null_in_assessed_scope", assessed_relation="associated_with_expression")
    with pytest.raises(GraphRefusal, match="exact scope"):
        g.link(assoc, null, "contradicts", "computational_investigator", "tested, nothing")
    assert g.hypotheses[h].disposition == "active"
    basal = claim(g, [ELEMENT], "regulates", [gene("GENE3")], "increases")
    stressed = claim(g, [ELEMENT], "regulates", [gene("GENE3")], "increases", ContextScope(condition="ER stress"))
    mouse = claim(g, [ELEMENT], "regulates", [gene("GENE3")], "increases", ContextScope(species="mouse"))
    assert len({basal, stressed, mouse}) == 3


def test_in_vivo_comes_only_from_the_adapter_flag(g):
    kd = evidence(g, "perturbation", "GENE1 knockdown in HepG2 lowers secreted apoB", about_genes=["GENE1"],
                  direction="increases", context=ContextScope(label="HepG2", biosample_kind="organism"))
    stored = g.evidence[kd]
    assert stored.context.biosample_kind == "cell_line"                  # the record's kind wins
    assert evidence_strength("contributes_to_trait", stored) == "indirect"
    mouse = stored.model_copy(update={"data": {"in_vivo": True}})
    assert evidence_strength("contributes_to_trait", mouse) == "direct"


def test_an_allele_resolved_readout_from_a_homozygous_context_is_context_only(g):
    c = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", ctx("HepG2"))
    h = hypothesis(g, [c], mechanism="tf_binding")
    imbalance = dict(about_tfs=["TFX"], result_kind="null_in_assessed_scope", assessed_relation="alters_binding",
                     data={"allele_specific": True})
    hom = evidence(g, "binding_assay", "Allelic imbalance in HepG2 (TT here): none for TFX",
                   context=ctx("HepG2", genotype="TT"), **imbalance)
    link = g.link(c, hom, "contradicts", "computational_investigator", "no imbalance")
    assert (link.stance, link.downgraded_from) == ("context_only", "contradicts")
    with pytest.raises(GraphRefusal, match="contradicted_in_scope needs"):
        g.assess(c, "contradicted_in_scope", "no imbalance", "critic", version(g, c))
    het = evidence(g, "binding_assay", "Allelic imbalance in HepG2 (GT here): none for TFX",
                   context=ctx("HepG2", genotype="G/T"), **imbalance)
    assert g.link(c, het, "contradicts", "computational_investigator", "no imbalance").stance == "contradicts"
    g.assess(c, "contradicted_in_scope", "no imbalance in a heterozygous line", "critic", version(g, c))
    assert g.hypotheses[h].disposition == "rejected"
    activity = claim(g, [VARIANT], "alters_regulatory_activity", [ELEMENT], "increases", ctx("HepG2"))
    constructs = evidence(g, "reporter_assay", "Luciferase in HepG2 (TT): the G construct is 3x higher", allele="G",
                          direction="increases", context=ctx("HepG2", genotype="TT"), about_variants=ABOUT_VARIANT)
    assert g.link(activity, constructs, "supports", "computational_investigator", "constructs").stance == "supports"


# --- duplicates, evidence entry and variants (M3, M4, M6, M7) -------------------------------------------------------

def test_a_duplicate_draft_adds_its_premises_to_the_shared_claim(g):
    f2 = claim(g, [gene("GENE1")], "contributes_to_trait", [LDL], "decreases")
    f1 = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    accepted, _ = g.apply_updates([GraphUpdate(kind="new_claim", reason="the trait link rests on the element", claim=(
        ClaimDraft(subjects=[gene("GENE1")], relation="contributes_to_trait", objects=[LDL], direction="decreases",
                   dependencies=[f1])))], "coordinator")
    assert accepted[0].ids == [f2] and f1 in accepted[0].note and g.claims[f2].dependencies == [f1]
    assert any(e.action == "add_dependency" for e in g.events)
    with pytest.raises(GraphRefusal, match="already rests on"):
        claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"), deps=[f2])
    h = hypothesis(g, [f1, f2])
    contradict(g, f1, evidence(g, "perturbation", "activating E raises GENE1", about_genes=["GENE1"],
                               about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2")))
    g.propagate()
    assert g.claims[f2].dependency_flag == "unsupported_due_to_dependency"
    assert g.hypotheses[h].path_status[f2] == "premise_failed"


def test_literature_dedup_keeps_distinct_experiments_apart(g):
    read = record(g, tool="literature_read", read_article="PMID:1").tool_call_id

    def emsa(symbol, cell, direction, allele):
        exp = ExperimentRecord(source_id="PMID:1", access="full_text", location="fig3", passage="p",
                               intervention="EMSA", endpoint="binding", direction=direction,
                               system=ExperimentSystem(tissue_or_cell=cell), about_tfs=[symbol])
        ev = Evidence(evidence_class="binding_assay", observed_result=f"EMSA: {symbol} binding in {cell}",
                      independence_group=f"PMID:1#EMSA/binding/{cell}", origin="literature", source_ids=["PMID:1"],
                      experiment=exp, retrieval_ref=read, access="full_text", about_tfs=[symbol], allele=allele,
                      direction=direction, context=ctx(cell))
        return g.add_evidence(ev, "literature_investigator")

    a = emsa("CEBPA", "HepG2", "increases", "G")
    assert len({a, emsa("CEBPB", "HeLa", "decreases", "G"), emsa("CEBPA", "HepG2", "increases", "T")}) == 3
    assert emsa("CEBPA", "HepG2", "increases", "G") == a


def test_add_evidence_takes_extractions_from_a_read_of_that_article_and_audits(g):
    annotation_call = record(g).tool_call_id
    fake = Evidence(evidence_class="perturbation", observed_result="CRISPRi of the element lowers GENE1 in HepG2",
                    independence_group="made-up", origin="tool", retrieval_ref=annotation_call, about_genes=["GENE1"],
                    about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="enters with its tool call"):
        g.add_evidence(fake, "coordinator")
    exp = ExperimentRecord(source_id="PMID:7", pmcid="PMC7", access="full_text", location="results/p2",
                           passage="CRISPRi lowered GENE1", intervention="CRISPRi", endpoint="GENE1 mRNA")
    extracted = fake.model_copy(update={"origin": "literature", "experiment": exp, "source_ids": ["PMID:7"]})
    with pytest.raises(GraphRefusal, match="not a literature read"):
        g.add_evidence(extracted, "literature_investigator")
    other_read = record(g, tool="literature_read", read_article="PMC8").tool_call_id
    with pytest.raises(GraphRefusal, match="read PMC8"):
        g.add_evidence(extracted.model_copy(update={"retrieval_ref": other_read}), "literature_investigator")
    read = record(g, tool="literature_read", read_article="PMC7").tool_call_id
    eid = g.add_evidence(extracted.model_copy(update={"retrieval_ref": read}), "literature_investigator")
    audit = Evidence(evidence_class="metadata_audit", observed_result="The cited cell line is Hep3B, not HepG2.",
                     independence_group="audit-1", origin="tool")
    assert g.add_evidence(audit, "critic").startswith("E")
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    assert g.link(c, eid, "supports", "literature_investigator", "CRISPRi").strength == "direct"
    guess = exp.model_copy(update={"location": "discussion/p1", "authors_hypothesis_vs_result": "hypothesis"})
    speculation = g.add_evidence(extracted.model_copy(update={"retrieval_ref": read, "experiment": guess,
                                                              "independence_group": "PMID:7#guess"}),
                                 "literature_investigator")
    with pytest.raises(GraphRefusal, match="authors' hypothesis"):
        g.link(c, speculation, "supports", "literature_investigator", "the authors propose it")
    assert g.link(c, speculation, "context_only", "literature_investigator", "a hypothesis").stance == "context_only"


def test_without_a_case_rsid_an_rsid_label_names_another_variant():
    g = ClaimGraph(Case(case_id="REQ-abc", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G")))
    case_variant = g.variant_entity()
    ld = claim(g, [EntityRef(kind="variant", label="rs999 (LD partner, r2 0.9)")], "associated_with_trait", [LDL],
               "decreases")
    assert g.claims[ld].subject_ids != [case_variant]
    same = claim(g, [EntityRef(kind="variant", label="the G allele at 2:60490908")], "overlaps", [ELEMENT])
    assert g.claims[same].subject_ids == [case_variant]
    assert g.claims[ld].effect_allele is None                            # no frame can be checked for another variant


# --- atomicity and JSON-native values (M5, low) ---------------------------------------------------------------------

def test_any_exception_inside_a_mutation_rolls_it_back(g):
    good = Evidence(evidence_class="annotation", observed_result="variant lies in element E", independence_group="a",
                    origin="tool")
    malformed = good.model_copy(update={"context": "HepG2", "independence_group": "b"})   # skips validation
    before = g.to_json()
    tid = g.reserve_tool_call_id()
    with pytest.raises(AttributeError):
        g.record_tool_call(ToolCall(tool_call_id=tid, tool_name="t", execution_status="success",
                                    retrieval_status="records_found", requested_by="code", charged_to="code"),
                           [good, malformed])
    assert g.evidence == {} and g.tool_calls == {} and json.loads(g.to_json()) == {**json.loads(before),
                                                                                   "counters": g.counters}


def test_evidence_data_and_observations_must_be_json_native(g):
    for value, problem in ((np.int64(3), "int64"), (math.nan, "nan"), ({"z": (1, 2)}, "tuple")):
        with pytest.raises(GraphRefusal, match=problem):
            evidence(g, "prediction", f"QBiC-SELEX: {problem}", about_tfs=["TFX"], data={"z": value})
    tid = g.reserve_tool_call_id()
    with pytest.raises(GraphRefusal, match="observations"):
        g.record_tool_call(ToolCall(tool_call_id=tid, tool_name="t", execution_status="success",
                                    retrieval_status="records_found", requested_by="code",
                                    observations=[{"z": np.float64(1.5)}]))
    kept = evidence(g, "prediction", "QBiC-SELEX: z 2.5", about_tfs=["TFX"], data={"z": 2.5, "models": [1, 2]})
    again = ClaimGraph.from_json(g.to_json())
    assert again.evidence[kept] == g.evidence[kept] and again.to_state() == g.to_state()
