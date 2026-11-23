"""ClaimGraph: the scientific invariants its mutations enforce (SPEC 3, 13.6-13.8).

Biological cases here use the development variant rs1427407 (chr2:60490908 T>G), never a gold case; TF symbols and
observations are stipulated for the test and are not claims about that variant.
"""

import json

import pytest

from variant2mechanism.v9.fixtures import FixtureToolRunner, load_fixture
from variant2mechanism.v9.graph import (
    ClaimDraft,
    ClaimGraph,
    EntityRef,
    GraphRefusal,
    GraphUpdate,
    HypothesisChanges,
    HypothesisDraft,
    SymbolResolver,
)
from variant2mechanism.v9.schemas import (
    REQUIRABLE,
    Case,
    ContextScope,
    Evidence,
    ExperimentRecord,
    PairComparison,
    Question,
    RunResult,
    ToolCall,
    ToolRequest,
    Variant,
    evidence_strength,
)

VARIANT = EntityRef(kind="variant", label="rs1427407")
ELEMENT = EntityRef(kind="element", label="enhancer", canonical_id="EH38E0000001")
ABOUT_ELEMENT = ["EH38E0000001"]          # evidence about what the element does names it (about_elements)
ABOUT_VARIANT = ["rs1427407"]             # evidence comparing the case variant's alleles names it (about_variants)


def dev_case() -> Case:
    return Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"))


def ctx(label: str) -> ContextScope:
    return ContextScope(label=label, source="supplied")


def tf(symbol: str) -> EntityRef:
    return EntityRef(kind="tf", label=symbol)


def gene(symbol: str) -> EntityRef:
    return EntityRef(kind="gene", label=symbol)


def group(*members: str, gid: str = "G035") -> EntityRef:
    return EntityRef(kind="tf_group", label=f"group {gid}", canonical_id=gid, members=list(members))


def claim(g: ClaimGraph, subjects, relation, objects, direction="unspecified", context=None, deps=(), **kw) -> str:
    draft = ClaimDraft(subjects=subjects, relation=relation, objects=objects, direction=direction, context=context,
                       dependencies=list(deps), **kw)
    return g.add_claim(draft, "coordinator")


def tool_call(g: ClaimGraph, retrieval_status="records_found", tool="test_tool", evidence=(), **kw) -> ToolCall:
    tid = g.reserve_tool_call_id()
    return g.record_tool_call(ToolCall(tool_call_id=tid, tool_name=tool, execution_status="success",
                                       retrieval_status=retrieval_status, requested_by="computational_investigator",
                                       charged_to="agent", **kw), list(evidence))


def evidence(g: ClaimGraph, cls: str, text: str, group_id: str | None = None, **kw) -> str:
    """Tool evidence, recorded with its own call (the way an adapter's evidence enters the graph)."""
    ev = Evidence(evidence_class=cls, observed_result=text, independence_group=group_id or text, origin="tool", **kw)
    return tool_call(g, evidence=[ev]).evidence_ids[0]


def read_call(g: ClaimGraph, article: str = "PMC100", retrieval_status: str = "records_found") -> str:
    """A literature read that returned an article (what an extracted experiment must cite)."""
    return tool_call(g, retrieval_status, tool="literature_read", read_article=article).tool_call_id


def hypothesis(g: ClaimGraph, required, optional=(), title="H", mechanism="regulatory", **kw) -> str:
    return g.add_hypothesis(HypothesisDraft(title=title, claim_ids=list(optional), required_claim_ids=list(required),
                                            mechanism_class=mechanism, **kw), "coordinator")


@pytest.fixture
def g() -> ClaimGraph:
    return ClaimGraph(dev_case())


# --- canonicalisation and dedup ------------------------------------------------------------------------------------

def test_entities_deduplicate_on_canonical_id_and_normalised_label(g):
    a = g.entity("gene", " sort1 ")
    assert g.entity("gene", "SORT1") == a and g.entities[a].label == "SORT1"
    assert g.entity("gene", "SORT1", canonical_id="HGNC:11186") == a        # the existing entity gains the id
    assert g.entities[a].canonical_id == "HGNC:11186"
    assert g.entity("gene", "SORT1", canonical_id="ENSG00000134243") == a   # one entity per symbol, first id kept
    assert g.entities[a].canonical_id == "HGNC:11186"
    assert g.entity("element", "x", canonical_id="EH38E0000001") == g.entity("element", "y", "EH38E0000001")
    assert g.entity("tf", "CEBPA") != g.entity("gene", "CEBPA")              # kind is part of identity
    grp = g.entity("tf_group", "G035", "G035", participants=[g.entity("tf", "CEBPA"), g.entity("tf", "CEBPB")])
    assert g.entity("tf_group", "other label", "G035", participants=[g.entity("tf", "CEBPB")]) == grp
    hnf4a = g.entity("tf", "HNF4A")
    with pytest.raises(GraphRefusal, match="fixed when it was created"):
        g.entity("tf_group", "G035", "G035", participants=[hnf4a])
    assert [g.entities[p].label for p in g.entities[grp].participants] == ["CEBPA", "CEBPB"]
    with pytest.raises(GraphRefusal, match="needs its member TFs"):
        g.entity("tf_group", "a group with no members", "G999")


def test_variant_references_map_to_the_case_variant_unless_they_name_another(g):
    v = g.variant_entity()
    assert g.entities[v].canonical_id == "GRCh38:2:60490908:T:G"
    c1 = claim(g, [EntityRef(kind="variant", label="the G allele")], "overlaps", [ELEMENT])
    c2 = claim(g, [EntityRef(kind="variant", label="rs1427407 (chr2:60490908)")], "overlaps", [ELEMENT])
    assert c1 == c2 and g.claims[c1].subject_ids == [v]
    other = claim(g, [EntityRef(kind="variant", label="rs999 (an LD partner)")], "overlaps", [ELEMENT])
    assert g.claims[other].subject_ids != [v]


def test_hgnc_resolver_normalises_previous_symbols(tmp_path):
    hgnc = tmp_path / "hgnc.txt"
    hgnc.write_text("hgnc_id\tsymbol\tstatus\tprev_symbol\n"
                    "HGNC:1\tNEWA\tApproved\t\"OLDA|SHARED\"\n"
                    "HGNC:2\tNEWB\tApproved\tSHARED\n")
    g = ClaimGraph(dev_case(), resolver=SymbolResolver.from_hgnc(hgnc))
    a = g.entity("gene", "olda")
    assert g.entities[a].label == "NEWA" and g.entities[a].canonical_id == "HGNC:1"
    assert g.entity("gene", "NEWA") == a
    assert g.entities[g.entity("gene", "SHARED")].canonical_id is None       # ambiguous previous symbol: untouched
    eid = evidence(g, "association", "obs", about_genes=["OldA"])
    assert g.evidence[eid].about_genes == ["NEWA"]


def test_claims_deduplicate_on_structure_not_wording(g):
    c1 = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2 cells"),
               assertion_text="The enhancer drives GENE1")
    n_events = len(g.events)
    c2 = claim(g, [ELEMENT], "regulates", [gene("gene1")], "increases", ctx("Hep G2"),
               assertion_text="Completely different wording")
    assert c1 == c2 and len(g.events) == n_events                          # no new claim, no event
    assert g.claims[c1].assertion_text == "The enhancer drives GENE1"
    assert claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2")) != c1
    assert claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("Hep3B")) != c1
    assert claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases",
                 ContextScope(label="HepG2", condition="lipid-loaded")) != c1


def test_evidence_deduplicates_and_keeps_every_source_id(g):
    e1 = evidence(g, "occupancy", "CEBPA ChIP-seq peak over the variant in HepG2", "ENCSR000AAA",
                  about_tfs=["CEBPA"], source_ids=["ENCODE:ENCSR000AAA"])
    again = evidence(g, "occupancy", "CEBPA ChIP-seq peak over the variant in  HepG2", "ENCSR000AAA",
                     about_tfs=["cebpa"], source_ids=["ReMap:ENCSR000AAA"])
    assert again == e1 and g.evidence[e1].source_ids == ["ENCODE:ENCSR000AAA", "ReMap:ENCSR000AAA"]
    other = evidence(g, "occupancy", "CEBPA peak 300 bp away (nearby, not overlapping)", "ENCSR000AAA",
                     about_tfs=["CEBPA"])
    assert other != e1 and g.evidence[other].independence_group == g.evidence[e1].independence_group
    tid = read_call(g, "PMC100")

    def paper(source_ids, location):
        exp = ExperimentRecord(source_id="PMID:1", pmcid="PMC100", access="full_text", location=location,
                               passage="p", intervention="EMSA", endpoint="binding")
        ev = Evidence(evidence_class="binding_assay", observed_result="Binding was stronger to G.",
                      independence_group="PMID:1#EMSA/binding/nuclear extract", origin="literature",
                      source_ids=source_ids, experiment=exp, retrieval_ref=tid, access="full_text")
        return g.add_evidence(ev, "literature_investigator")

    p1 = paper(["PMID:1"], "results/p3")
    assert paper(["PMC100"], "results/p3") == p1                           # one article, one location
    assert set(g.evidence[p1].source_ids) == {"PMID:1", "PMC100"}
    assert paper(["PMID:1"], "fig2") != p1


# --- link validation -----------------------------------------------------------------------------------------------

def test_identity_a_cebpa_assay_cannot_support_a_cebpb_claim(g):
    chip = evidence(g, "occupancy", "CEBPA ChIP-seq peak over the variant in HepG2", about_tfs=["CEBPA"],
                    context=ctx("HepG2"))
    cebpb = claim(g, [tf("CEBPB")], "occupies", [ELEMENT], context=ctx("HepG2"))
    cebpa = claim(g, [tf("CEBPA")], "occupies", [ELEMENT], context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="not CEBPB"):
        g.link(cebpb, chip, "supports", "computational_investigator", "a C/EBP peak")
    with pytest.raises(GraphRefusal, match="not CEBPB"):
        g.link(cebpb, chip, "contradicts", "computational_investigator", "no CEBPB peak")
    g.link(cebpb, chip, "context_only", "computational_investigator", "a paralog's peak, context only")
    assert g.link(cebpa, chip, "supports", "computational_investigator", "CEBPA peak").strength == "direct"


def test_identity_a_group_claim_needs_a_member_and_names_it(g):
    binding = claim(g, [VARIANT], "alters_binding", [group("CEBPA", "CEBPB", "CEBPE")], "increases")
    pred = evidence(g, "prediction", "best G035 model predicts more binding to G", about_tfs=["CEBPB", "CEBPE"],
                    allele="G", direction="increases", about_variants=ABOUT_VARIANT)
    with pytest.raises(GraphRefusal, match="must name the member"):
        g.link(binding, pred, "supports", "computational_investigator", "the group model predicts more binding")
    g.link(binding, pred, "supports", "computational_investigator", "the CEBPB model predicts more binding")
    outsider = evidence(g, "prediction", "CEBPG model predicts more binding", about_tfs=["CEBPG"], allele="G",
                        direction="increases", about_variants=ABOUT_VARIANT)
    with pytest.raises(GraphRefusal, match="none of the members"):
        g.link(binding, outsider, "supports", "computational_investigator", "CEBPG")


def inventory_item(g: ClaimGraph, gid: str = "G035", tfs=("CEBPA", "CEBPB", "CEBPE"), discordant: bool = False) -> str:
    """One QBiC-SELEX inventory item as the adapter writes it: about the TFs its gate-passing models map to, with
    data.group_id and data.discordant (False when those models agree about the allele)."""
    return evidence(g, "prediction", f"QBiC-SELEX predicts more binding to G for model-sharing group {gid}",
                    about_tfs=list(tfs), allele="G", direction="increases", about_variants=ABOUT_VARIANT,
                    data={"group_id": gid, "discordant": discordant, "models": ["MODEL_1", "MODEL_2"]})


GROUP_RATIONALE = ("The QBiC-SELEX prediction for G035 favours G over T. This is indirect predicted evidence, not an "
                   "observed binding difference.")           # what a coordinator wrote in a saved run: no member named


def test_identity_a_groups_own_inventory_prediction_needs_no_member_named(g):
    binding = claim(g, [VARIANT], "alters_binding", [group("CEBPA", "CEBPB", "CEBPE")], "increases")
    link = g.link(binding, inventory_item(g), "supports", "coordinator", GROUP_RATIONALE)
    assert (link.stance, link.strength) == ("supports", "indirect")
    assert g.display(binding).status == "predicted" and g.display(binding).basis == "prediction"
    notes = next(e for e in g.events if e.event_id == link.event_id).details["notes"]
    assert any("inventory item of group G035 itself" in n and "no member is named" in n for n in notes)
    with pytest.raises(GraphRefusal, match="its support is indirect"):          # a prediction never settles a claim
        g.assess(binding, "supported_in_scope", "predicted", "critic", g.claims[binding].version)


def test_identity_naming_a_member_for_the_groups_own_prediction_adds_no_note(g):
    binding = claim(g, [VARIANT], "alters_binding", [group("CEBPA", "CEBPB", "CEBPE")], "increases")
    link = g.link(binding, inventory_item(g), "supports", "coordinator", "the CEBPB models favour G")
    assert next(e for e in g.events if e.event_id == link.event_id).details["notes"] == []


@pytest.mark.parametrize("what", ["discordant_group", "single_model", "another_group", "experiment"])
def test_identity_member_level_evidence_still_names_its_member(g, what):
    binding = claim(g, [VARIANT], "alters_binding", [group("CEBPA", "CEBPB", "CEBPE")], "increases")
    if what == "discordant_group":                     # the group's models disagree: each item is about some members
        eid = inventory_item(g, tfs=("CEBPB",), discordant=True)
    elif what == "single_model":                       # qbic_tf_detail: one model's prediction, no data.discordant
        eid = evidence(g, "prediction", "QBiC-SELEX model CEBPB_MODEL predicts more binding to G",
                       about_tfs=["CEBPB"], allele="G", direction="increases", about_variants=ABOUT_VARIANT,
                       data={"model": "CEBPB_MODEL", "group_id": "G035"})
    elif what == "another_group":                      # an inventory item of a different group that shares a member
        eid = inventory_item(g, gid="G036", tfs=("CEBPB", "CEBPD"))
    else:                                              # an experiment about one member
        eid = evidence(g, "binding_assay", "EMSA: CEBPB binds the G probe more", about_tfs=["CEBPB"], allele="G",
                       direction="increases", about_variants=ABOUT_VARIANT)
    with pytest.raises(GraphRefusal, match=r"must name the member the evidence is about \(CEBPB\)"):
        g.link(binding, eid, "supports", "coordinator", GROUP_RATIONALE)
    g.link(binding, eid, "supports", "coordinator", "this is about CEBPB")


def test_identity_the_groups_own_prediction_still_passes_every_other_gate(g):
    weaker = claim(g, [VARIANT], "alters_binding", [group("CEBPA", "CEBPB", "CEBPE")], "decreases")
    item = inventory_item(g)                                               # predicts more binding to G, the alt
    with pytest.raises(GraphRefusal, match="opposite to the claim's 'decreases'"):
        g.link(weaker, item, "supports", "coordinator", GROUP_RATIONALE)
    other = claim(g, [VARIANT], "alters_binding", [group("SP1", "SP3", gid="G015")], "increases")
    with pytest.raises(GraphRefusal, match="none of the members"):
        g.link(other, item, "supports", "coordinator", GROUP_RATIONALE)
    occupies = claim(g, [group("CEBPA", "CEBPB", "CEBPE")], "occupies", [ELEMENT])
    with pytest.raises(GraphRefusal, match="prediction evidence cannot support a occupies claim"):
        g.link(occupies, item, "supports", "coordinator", GROUP_RATIONALE)


def test_a_coordinators_group_prediction_update_is_applied_with_its_suggested_assessment(g):
    """The update a coordinator sent in a saved run, which the member rule used to refuse."""
    binding = claim(g, [VARIANT], "alters_binding", [group("CEBPA", "CEBPB", "CEBPE")], "increases")
    accepted, refused = g.apply_updates([GraphUpdate(
        kind="attach_evidence", claim_id=binding, evidence_id=inventory_item(g), stance="supports",
        applicability="unknown", rationale=GROUP_RATIONALE, suggested_assessment="unresolved", base_version=1)],
        "coordinator")
    assert refused == [] and [o.kind for o in accepted] == ["attach_evidence", "assess"]
    assert not any(e.action == "refuse_update" for e in g.events)
    c = g.claims[binding]
    assert c.assessment == "unresolved" and [x.stance for x in c.evidence_links] == ["supports"]
    assert c.evidence_links[0].applicability == "exact"                    # its "unknown" was no judgement
    assert accepted[0].note == "applicability unknown is no judgement: code's exact is stored"
    assert g.display(binding).status == "predicted"


def test_identity_gene_evidence_stays_with_its_gene(g):
    eqtl = evidence(g, "association", "G allele: higher GENE2 expression in liver (NES 0.4)", about_genes=["GENE2"],
                    about_elements=ABOUT_ELEMENT, allele="G", direction="increases", context=ctx("GTEx:Liver"))
    reg = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("liver"))
    with pytest.raises(GraphRefusal, match="not gene GENE1"):
        g.link(reg, eqtl, "supports", "computational_investigator", "eQTL")


def test_direction_opposite_evidence_contradicts_but_never_supports(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    up = evidence(g, "perturbation", "CRISPRi of the element lowers GENE1", about_genes=["GENE1"],
                  about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="opposite"):
        g.link(c, up, "supports", "computational_investigator", "")
    assert g.link(c, up, "contradicts", "computational_investigator", "matched direction test").stance == "contradicts"
    created = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "creates")
    pred = evidence(g, "prediction", "more predicted binding to G", about_tfs=["TFX"], allele="G",
                    direction="increases", about_variants=ABOUT_VARIANT)
    g.link(created, pred, "supports", "computational_investigator", "creates ~ increases")


def test_a_proposer_weakens_a_match_by_naming_the_weaker_one(g):
    c = claim(g, [tf("CEBPA")], "occupies", [ELEMENT], context=ctx("HepG2"))
    peak = evidence(g, "occupancy", "CEBPA peak in HepG2", about_tfs=["CEBPA"], context=ctx("HepG2"))
    link = g.link(c, peak, "supports", "computational_investigator", "a drug-treated subline", applicability="proxy")
    assert (link.code_applicability, link.applicability, link.corrected) == ("exact", "proxy", False)
    assert g.events[-1].details["notes"] == []
    other = evidence(g, "occupancy", "another CEBPA peak in HepG2", about_tfs=["CEBPA"], context=ctx("HepG2"))
    link = g.link(c, other, "supports", "computational_investigator", "not the same cells", applicability="different")
    assert (link.stance, link.downgraded_from, link.applicability) == ("context_only", "supports", "different")


def test_an_unknown_applicability_is_no_judgement_on_a_supporting_link(g):
    """An agent that writes "unknown" by habit must not leave a claim that can never be assessed as supported."""
    c = claim(g, [VARIANT], "associated_with_trait", [EntityRef(kind="phenotype", label="LDL cholesterol")],
              "decreases")
    gwas = evidence(g, "association", "GWAS: G is associated with lower LDL cholesterol",
                    about_traits=["LDL cholesterol"], allele="G", direction="decreases", about_variants=ABOUT_VARIANT)
    accepted, refused = g.apply_updates([GraphUpdate(kind="attach_evidence", claim_id=c, evidence_id=gwas,
                                                     stance="supports", applicability="unknown",
                                                     rationale="the association names this trait")], "coordinator")
    assert refused == [] and accepted[0].note == "applicability unknown is no judgement: code's exact is stored"
    link = g.claims[c].evidence_links[0]
    assert (link.code_applicability, link.applicability, link.corrected) == ("exact", "exact", False)
    g.assess(c, "supported_in_scope", "GWAS association", "critic", g.claims[c].version)
    held = g.claims[c].version
    again = g.link(c, gwas, "supports", "critic", "the same again", applicability="unknown")
    assert again == link and g.claims[c].version == held                    # nor does it weaken a link already held
    assert g.claims[c].assessment == "supported_in_scope"


def test_an_unknown_applicability_changes_nothing_code_did_not_compute(g):
    scoped = claim(g, [tf("CEBPA")], "occupies", [ELEMENT], context=ctx("HepG2"))
    lost = evidence(g, "occupancy", "CEBPA peak, biosample not recorded", about_tfs=["CEBPA"])
    link = g.link(scoped, lost, "supports", "computational_investigator", "no context", applicability="unknown")
    assert (link.code_applicability, link.applicability, link.corrected) == ("unknown", "unknown", False)
    assert g.events[-1].details["notes"] == []
    k562 = evidence(g, "occupancy", "CEBPA peak in K562", about_tfs=["CEBPA"], context=ctx("K562"))
    link = g.link(scoped, k562, "supports", "computational_investigator", "another tissue", applicability="unknown")
    assert (link.stance, link.applicability, link.corrected) == ("context_only", "different", True)


def test_an_unknown_applicability_still_withholds_a_contradiction(g):
    """A contradiction can reject a hypothesis, so a proposer unsure of the scope holds it back with "unknown"."""
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    up = evidence(g, "perturbation", "activating the element raises GENE1 in HepG2", about_genes=["GENE1"],
                  about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    link = g.link(c, up, "contradicts", "computational_investigator", "maybe not the same scope",
                  applicability="unknown")
    assert (link.code_applicability, link.applicability) == ("exact", "unknown")
    assert g.events[-1].details["notes"] == []
    with pytest.raises(GraphRefusal, match="contradicted_in_scope needs"):
        g.assess(c, "contradicted_in_scope", "matched", "critic", g.claims[c].version)


def test_applicability_is_computed_by_code_and_only_weakened_by_the_proposer(g):
    c = claim(g, [tf("CEBPA")], "occupies", [ELEMENT], context=ctx("Hep3B"))
    hepg2 = evidence(g, "occupancy", "CEBPA peak in HepG2", about_tfs=["CEBPA"], context=ctx("HepG2"))
    link = g.link(c, hepg2, "supports", "computational_investigator", "liver line", applicability="exact")
    assert (link.code_applicability, link.applicability, link.corrected) == ("proxy", "proxy", True)
    assert g.events[-1].details["corrected"] is True
    assert g.events[-1].details["notes"] == ["applicability corrected from exact to proxy"]
    unjudged = evidence(g, "occupancy", "second CEBPA peak in HepG2", about_tfs=["CEBPA"], context=ctx("HepG2"))
    link = g.link(c, unjudged, "supports", "computational_investigator", "no view on the scope",
                  applicability="unknown")
    assert (link.applicability, link.corrected) == ("proxy", False)      # "unknown" is no judgement: code's stands
    assert g.events[-1].details["notes"] == [
        "the proposed applicability 'unknown' states no judgement: code's 'proxy' is stored"]
    k562 = evidence(g, "occupancy", "CEBPA peak in K562", about_tfs=["CEBPA"], context=ctx("K562"))
    link = g.link(c, k562, "supports", "computational_investigator", "another tissue")
    assert (link.stance, link.downgraded_from, link.applicability) == ("context_only", "supports", "different")
    # Three links made versions 2, 3 and 4. A proxy link can support in scope; the K562 peak never counts.
    assert g.assess(c, "supported_in_scope", "HepG2 proxy peak", "critic", 4) == 5


def test_class_matrix_prediction_alone_leaves_binding_unresolved_and_shows_predicted(g):
    c = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", ctx("HepG2"))
    pred = evidence(g, "prediction", "QBiC-SELEX z = 9.1, more binding to G", about_tfs=["TFX"], allele="G",
                    direction="increases", data={"z": 9.1, "mapping": "own"}, about_variants=ABOUT_VARIANT)
    assert g.link(c, pred, "supports", "computational_investigator", "QBiC").strength == "indirect"
    with pytest.raises(GraphRefusal, match="indirect \\(prediction\\)"):
        g.assess(c, "supported_in_scope", "big z", "critic", 2)
    assert g.display(c).model_dump() == {"status": "predicted", "basis": "prediction", "basis_classes": ["prediction"],
                                         "dependency_flag": "none"}
    expression = evidence(g, "expression", "TFX TPM 40 in HepG2", about_tfs=["TFX"])
    with pytest.raises(GraphRefusal, match="link it as context_only"):
        g.link(c, expression, "supports", "computational_investigator", "expressed")
    review = evidence(g, "review", "A review says TFX binds here", about_tfs=["TFX"])
    with pytest.raises(GraphRefusal, match="cannot contradict"):
        g.link(c, review, "contradicts", "critic", "review")
    allelic = evidence(g, "occupancy", "allele-specific TFX ChIP reads favour G in HepG2", about_tfs=["TFX"],
                       allele="G", direction="increases", context=ctx("HepG2"), data={"allele_specific": True},
                       about_variants=ABOUT_VARIANT)
    assert g.link(c, allelic, "supports", "computational_investigator", "allelic").strength == "direct"
    g.assess(c, "supported_in_scope", "allele-resolved occupancy", "critic", 3)
    assert g.display(c).status == "supported" and g.display(c).basis == "occupancy"


def test_class_matrix_association_is_direct_only_for_association_claims(g):
    eqtl = evidence(g, "association", "G allele: higher GENE1 in liver", about_genes=["GENE1"], allele="G",
                    about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("GTEx:Liver"),
                    about_variants=ABOUT_VARIANT)
    assoc = claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases", ctx("liver"))
    reg = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("liver"))
    g.link(assoc, eqtl, "supports", "computational_investigator", "eQTL")
    g.link(reg, eqtl, "supports", "computational_investigator", "eQTL suggests the element drives GENE1")
    g.assess(assoc, "supported_in_scope", "liver eQTL", "critic", 2)
    with pytest.raises(GraphRefusal):
        g.assess(reg, "supported_in_scope", "eQTL only", "critic", 2)
    assert g.display_status(reg) == "associated" and g.display_status(assoc) == "supported"


def test_mapping_type_never_changes_what_a_prediction_can_do():
    own = Evidence(evidence_class="prediction", observed_result="x", independence_group="m", origin="tool",
                   data={"mapping_type": "own"})
    mapped = own.model_copy(update={"data": {"mapping_type": "CIS-BP-mapped"}})
    for relation in REQUIRABLE | {"expressed_in", "occupies"}:
        assert evidence_strength(relation, own) == evidence_strength(relation, mapped)


# --- missingness and measured nulls ---------------------------------------------------------------------------------

def test_empty_retrievals_create_no_evidence(g):
    ev = Evidence(evidence_class="occupancy", observed_result="no peak", independence_group="x", origin="tool",
                  about_tfs=["TFX"])
    for status, retrieval in (("success", "no_records_found"), ("cache_miss", "unknown"), ("error", "unknown")):
        tid = g.reserve_tool_call_id()
        call = ToolCall(tool_call_id=tid, tool_name="t", execution_status=status, retrieval_status=retrieval,
                        requested_by="code")
        with pytest.raises(GraphRefusal, match="creates no Evidence"):
            g.record_tool_call(call, [ev])
        assert tid not in g.tool_calls                                      # refused atomically
    empty_read = read_call(g, "PMC9", retrieval_status="no_records_found")
    extracted = Evidence(evidence_class="binding_assay", observed_result="EMSA: no binding", origin="literature",
                         independence_group="PMID:9#EMSA", source_ids=["PMC9"], retrieval_ref=empty_read,
                         experiment=ExperimentRecord(source_id="PMID:9", pmcid="PMC9", access="abstract_only",
                                                     location="abstract", passage="p"))
    with pytest.raises(GraphRefusal, match="creates no Evidence"):
        g.add_evidence(extracted, "literature_investigator")
    assert g.evidence == {}


def test_a_measured_null_contradicts_only_in_an_exact_matched_scope(g):
    occ = claim(g, [tf("TFX")], "occupies", [ELEMENT], context=ctx("HepG2"))
    null = evidence(g, "occupancy", "TFX ChIP-seq in HepG2: no peak within 1 kb", about_tfs=["TFX"],
                    context=ctx("HepG2"), result_kind="null_in_assessed_scope", assessed_relation="occupies",
                    direction="no_change")
    with pytest.raises(GraphRefusal, match="cannot support"):
        g.link(occ, null, "supports", "computational_investigator", "assayed")
    with pytest.raises(GraphRefusal, match="explicit rationale"):
        g.link(occ, null, "contradicts", "computational_investigator", "")
    proxy = claim(g, [tf("TFX")], "occupies", [ELEMENT], context=ctx("Hep3B"))
    with pytest.raises(GraphRefusal, match="exact scope"):
        g.link(proxy, null, "contradicts", "computational_investigator", "HepG2 null")
    binding = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="null for occupies"):
        g.link(binding, null, "contradicts", "computational_investigator", "no peak")
    g.link(occ, null, "contradicts", "computational_investigator", "assayed in the same line, no peak")
    with pytest.raises(GraphRefusal, match="assessed_relation"):
        evidence(g, "occupancy", "an unscoped null", about_tfs=["TFX"], result_kind="null_in_assessed_scope")


# --- assessments ---------------------------------------------------------------------------------------------------

def test_assessment_gates_and_optimistic_concurrency(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="supported_in_scope needs"):
        g.assess(c, "supported_in_scope", "no evidence yet", "critic", 1)
    with pytest.raises(GraphRefusal, match="missing or indirect evidence never contradicts"):
        g.assess(c, "contradicted_in_scope", "nothing found", "critic", 1)
    with pytest.raises(GraphRefusal, match="initial value"):
        g.assess(c, "unassessed", "reset", "critic", 1)
    with pytest.raises(GraphRefusal, match="investigators suggest"):
        g.assess(c, "unresolved", "x", "computational_investigator", 1)
    assert g.assess(c, "unresolved", "not yet investigated", "coordinator", 1) == 2
    with pytest.raises(GraphRefusal, match="stale update"):
        g.assess(c, "unresolved", "based on an old read", "critic", 1)
    crispr = evidence(g, "perturbation", "CRISPRi of the element lowers GENE1 2-fold", about_genes=["GENE1"],
                      about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    g.link(c, crispr, "supports", "computational_investigator", "CRISPRi")
    with pytest.raises(GraphRefusal, match="stale update"):                # the link made version 3
        g.assess(c, "supported_in_scope", "read before the CRISPRi link", "critic", 2)
    g.assess(c, "supported_in_scope", "CRISPRi in the same line", "critic", 3)
    assert [(h.version, h.assessment, h.action) for h in g.claims[c].history] == [
        (1, "unassessed", "new_claim"), (2, "unresolved", "assess"), (3, "unresolved", "attach_evidence"),
        (4, "supported_in_scope", "assess")]
    eqtl = evidence(g, "association", "eQTL: lower GENE1 with the element's G allele", about_genes=["GENE1"],
                    about_elements=ABOUT_ELEMENT, direction="decreases", context=ctx("HepG2"))
    g.link(c, eqtl, "contradicts", "computational_investigator", "opposite-sign eQTL")
    assert g.claims[c].assessment == "supported_in_scope"                 # an indirect contradiction keeps it
    g.assess(c, "contested", "CRISPRi and an opposite eQTL disagree", "critic", 5)


def test_investigator_assessments_go_through_the_same_gate_as_code(g):
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    eqtl = evidence(g, "association", "eQTL: higher GENE1 with the element's G allele", about_genes=["GENE1"],
                    about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    accepted, refused = g.apply_updates([
        GraphUpdate(kind="attach_evidence", claim_id=c, evidence_id=eqtl, stance="supports",
                    rationale="eQTL supports", suggested_assessment="supported_in_scope", base_version=1),
        GraphUpdate(kind="assess", claim_id=c, assessment="unresolved", base_version=1,
                    rationale="association only"),
    ], "computational_investigator")
    assert [o.kind for o in accepted] == ["attach_evidence", "assess"]
    assert [o.kind for o in refused] == ["assess"] and "supported_in_scope needs" in refused[0].reason
    applied = next(e for e in g.events if e.action == "assess")
    assert applied.role == "code" and applied.details["suggested_by"] == "computational_investigator"
    assert [e.action for e in g.events if e.role == "computational_investigator"][-1] == "refuse_update"


# --- hypotheses, required claims and dispositions -------------------------------------------------------------------

def test_expression_and_occupancy_claims_can_never_be_required(g):
    expr = claim(g, [tf("TFX")], "expressed_in", [EntityRef(kind="context", label="HepG2")], context=ctx("HepG2"))
    occ = claim(g, [tf("TFX")], "occupies", [ELEMENT], context=ctx("HepG2"))
    binding = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")
    for bad in (expr, occ):
        with pytest.raises(GraphRefusal, match="cannot be a required claim"):
            hypothesis(g, [binding, bad])
    h = hypothesis(g, [binding], [expr, occ])
    with pytest.raises(GraphRefusal, match="cannot be a required claim"):
        g.add_claim_to_hypothesis(h, occ, True, "make it required", "coordinator")
    low = evidence(g, "expression", "TFX TPM 0.3 in HepG2 (below detection)", about_tfs=["TFX"],
                   context=ctx("HepG2"), result_kind="null_in_assessed_scope", assessed_relation="expressed_in")
    g.link(expr, low, "contradicts", "computational_investigator", "measured, not detected")
    g.assess(expr, "contradicted_in_scope", "TPM 0.3", "critic", 2)
    g.propagate()
    assert g.hypotheses[h].disposition == "active"                       # expression never vetoes a TF
    with pytest.raises(GraphRefusal, match="defer it instead"):
        g.set_disposition(h, "rejected", "not expressed", "critic")


def test_dispositions_rejected_deferred_leading(g):
    binding = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")
    h = hypothesis(g, [binding])
    with pytest.raises(GraphRefusal, match="defer it instead"):
        g.set_disposition(h, "rejected", "weak prediction", "coordinator")
    with pytest.raises(GraphRefusal, match="revisit trigger"):
        g.set_disposition(h, "deferred", "budget", "coordinator")
    with pytest.raises(GraphRefusal, match="comparison step"):
        g.set_disposition(h, "leading", "looks best", "critic")
    g.set_disposition(h, "deferred", "another question is more informative", "coordinator",
                      revisit_trigger="an allele-specific binding assay appears")
    assert g.hypotheses[h].revisit_trigger == "an allele-specific binding assay appears"
    g.set_disposition(h, "active", "budget allows", "coordinator")
    g.set_disposition(h, "leading", "preferred on every divergent claim", "code")
    assert [x["to"] for x in g.hypotheses[h].history if x["kind"] == "disposition"] == ["deferred", "active",
                                                                                         "leading"]
    with pytest.raises(GraphRefusal, match="deferred hypothesis needs"):
        hypothesis(g, [claim(g, [VARIANT], "alters_binding", [tf("TFY")], "increases")], disposition="deferred",
                   disposition_reason="later")


def test_supersession_keeps_independent_support_and_never_moves_tf_evidence(g):
    """Controlled fixture (b): wrong TF, supported element->gene link."""
    a_bind = claim(g, [VARIANT], "alters_binding", [tf("TFA")], "increases", ctx("HepG2"))
    reg = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    h = hypothesis(g, [a_bind, reg], title="TFA drives GENE1")
    a_chip = evidence(g, "occupancy", "allele-specific TFA ChIP favours G in HepG2", about_tfs=["TFA"], allele="G",
                      direction="increases", context=ctx("HepG2"), data={"allele_specific": True},
                      about_variants=ABOUT_VARIANT)
    crispr = evidence(g, "perturbation", "CRISPRi of the element lowers GENE1", about_genes=["GENE1"],
                      about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    g.link(a_bind, a_chip, "supports", "computational_investigator", "allelic ChIP")
    g.link(reg, crispr, "supports", "computational_investigator", "CRISPRi")
    g.assess(reg, "supported_in_scope", "CRISPRi in HepG2", "critic", 2)
    b_draft = ClaimDraft(subjects=[VARIANT], relation="alters_binding", objects=[tf("TFB")], direction="increases",
                         context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="same proposition"):
        g.supersede_claim(a_bind, ClaimDraft(subjects=[VARIANT], relation="alters_binding", objects=[tf("TFA")],
                                             direction="increases", context=ctx("HepG2")), "no change", "coordinator")
    b_bind = g.supersede_claim(a_bind, b_draft, "the literature names TFB, not TFA", "coordinator", [h])
    old, new = g.claims[a_bind], g.claims[b_bind]
    assert (old.superseded_by, new.supersedes) == (b_bind, a_bind)
    assert new.evidence_links == [] and [x.evidence_id for x in old.evidence_links] == [a_chip]  # nothing copied
    hyp = g.hypotheses[h]
    assert hyp.version == 2 and hyp.required_claim_ids == [b_bind, reg]
    assert hyp.history[-1]["previous"]["required_claim_ids"] == [a_bind, reg]
    assert g.claims[reg].assessment == "supported_in_scope" and len(g.claims[reg].evidence_links) == 1
    with pytest.raises(GraphRefusal, match="not TFB"):
        g.link(b_bind, a_chip, "supports", "computational_investigator", "reuse the TFA ChIP")
    with pytest.raises(GraphRefusal, match="superseded by"):
        g.link(a_bind, crispr, "context_only", "computational_investigator", "x")
    assert hyp.path_status == {b_bind: "intact", reg: "intact"}


def test_local_repair_replaces_one_required_claim_and_keeps_the_rest(g):
    a = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    keep = claim(g, [VARIANT], "overlaps", [ELEMENT])
    h = hypothesis(g, [a, keep])
    b = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    g.replace_required_claim(h, a, b, "sign corrected after a matched test", "coordinator")
    assert g.hypotheses[h].required_claim_ids == [b, keep] and g.claims[a].superseded_by is None
    with pytest.raises(GraphRefusal, match="not a required claim"):
        g.replace_required_claim(h, a, b, "again", "coordinator")
    with pytest.raises(GraphRefusal, match="changes nothing"):
        g.revise_hypothesis(h, HypothesisChanges(title="H"), "no-op", "coordinator")


def test_dependency_flags_never_change_an_assessment(g):
    premise = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    down = claim(g, [gene("GENE1")], "affects_process", [EntityRef(kind="process", label="cell growth")],
                 "decreases", ctx("HepG2"), deps=[premise])
    further = claim(g, [EntityRef(kind="process", label="cell growth")], "contributes_to_trait",
                    [EntityRef(kind="phenotype", label="trait T")], deps=[down])
    h = hypothesis(g, [premise], [down, further])
    own = evidence(g, "perturbation", "GENE1 knockdown slows growth in HepG2", about_genes=["GENE1"],
                   direction="decreases", context=ctx("HepG2"))
    g.link(down, own, "supports", "computational_investigator", "its own experiment")
    g.assess(down, "supported_in_scope", "knockdown", "critic", 2)
    up = evidence(g, "perturbation", "activating the element raises GENE1", about_genes=["GENE1"],
                  about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    g.link(premise, up, "contradicts", "computational_investigator", "matched test")
    g.assess(premise, "contradicted_in_scope", "opposite sign", "critic", 2)
    assert g.hypotheses[h].disposition == "rejected" and g.events[-1].action == "reject"   # at the assessment
    events = g.propagate()
    assert g.claims[down].assessment == "supported_in_scope"              # its own evidence still stands
    assert g.claims[down].dependency_flag == g.claims[further].dependency_flag == "unsupported_due_to_dependency"
    assert g.claims[further].assessment == "unassessed"                   # never "contradicted" by propagation
    assert g.display(down).status == "supported" and g.display(down).dependency_flag != "none"
    assert g.hypotheses[h].path_status == {premise: "intact", down: "premise_failed", further: "premise_failed"}
    assert [g.events[int(e[1:]) - 1].action for e in events] == ["propagate"]
    assert g.propagate() == []                                            # idempotent


def test_regenerating_a_rejected_structure_is_refused_and_revisions_cannot_reach_it(g):
    a = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    h1 = hypothesis(g, [a])
    up = evidence(g, "perturbation", "activating the element raises GENE1", about_genes=["GENE1"],
                  about_elements=ABOUT_ELEMENT, direction="increases", context=ctx("HepG2"))
    g.link(a, up, "contradicts", "computational_investigator", "matched")
    g.assess(a, "contradicted_in_scope", "opposite sign", "critic", 2)
    assert g.hypotheses[h1].disposition == "rejected"
    reworded = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"),
                     assertion_text="The element represses GENE1 in liver lines")
    with pytest.raises(GraphRefusal, match=f"repeats rejected hypothesis {h1}"):
        hypothesis(g, [reworded], title="same story, new words", origin="regenerated", replaces=h1)
    other = claim(g, [ELEMENT], "regulates", [gene("GENE2")], "increases", ctx("HepG2"))
    h2 = hypothesis(g, [other], origin="regenerated")
    with pytest.raises(GraphRefusal, match="repeats rejected"):
        g.revise_hypothesis(h2, HypothesisChanges(replace_claims={other: reworded}), "drift back", "coordinator")
    with pytest.raises(GraphRefusal, match="final"):
        g.revise_hypothesis(h1, HypothesisChanges(title="revived"), "revive", "coordinator")
    assert hypothesis(g, [other], title="same structure again") == h2      # merged by signature, not duplicated


def test_refused_compound_mutations_leave_the_graph_unchanged(g):
    a = claim(g, [VARIANT], "alters_binding", [tf("TFA")], "increases")
    occ = claim(g, [tf("TFA")], "occupies", [ELEMENT])
    h = hypothesis(g, [a], [occ])
    before = g.to_json()
    draft = ClaimDraft(subjects=[tf("TFB")], relation="occupies", objects=[ELEMENT])
    with pytest.raises(GraphRefusal, match="cannot be a required claim"):
        g.supersede_claim(a, draft, "swap a required binding claim for an occupancy claim", "coordinator", [h])
    assert g.to_json() == before


# --- batches ---------------------------------------------------------------------------------------------------------

def test_apply_updates_with_batch_keys_and_recorded_refusals(g):
    binding = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")
    accepted, refused = g.apply_updates([
        GraphUpdate(kind="new_claim", key="reg", reason="element to gene",
                    claim=ClaimDraft(subjects=[ELEMENT], relation="regulates", objects=[gene("GENE1")],
                                     direction="increases", context=ctx("HepG2"))),
        GraphUpdate(kind="add_hypothesis", key="h",
                    hypothesis=HypothesisDraft(title="TFX drives GENE1", required_claim_ids=[binding, "key:reg"],
                                               mechanism_class="tf_binding")),
        GraphUpdate(kind="new_claim", key="dup", claim=ClaimDraft(subjects=[ELEMENT], relation="regulates",
                                                                  objects=[gene("gene1")], direction="increases",
                                                                  context=ctx("Hep G2"))),
        GraphUpdate(kind="set_disposition", hypothesis_id="key:h", disposition="rejected", reason="dislike"),
        GraphUpdate(kind="add_claim_to_hypothesis", hypothesis_id="key:missing", claim_id=binding),
        GraphUpdate(kind="assess", claim_id=binding, assessment="unresolved", rationale="x"),
    ], "coordinator")
    reg, hid = accepted[0].ids[0], accepted[1].ids[0]
    assert g.hypotheses[hid].required_claim_ids == [binding, reg]
    assert accepted[2].note == f"duplicate of existing claim {reg}"
    assert [(o.index, o.kind) for o in refused] == [(3, "set_disposition"), (4, "add_claim_to_hypothesis"),
                                                     (5, "assess")]
    assert "names nothing created earlier" in refused[1].reason and "needs base_version" in refused[2].reason
    refusals = [e for e in g.events if e.action == "refuse_update"]
    assert len(refusals) == 3 and all(e.graph_version_before == e.graph_version_after for e in refusals)
    assert refusals[0].details["update"]["kind"] == "set_disposition"
    _, refused = g.apply_updates([GraphUpdate(kind="set_disposition", hypothesis_id=hid, disposition="deferred",
                                              reason="x", revisit_trigger="y")], "literature_investigator")
    assert "hypothesis changes are the coordinator's" in refused[0].reason


# --- the synthetic scenario (SPEC 11), driven through the graph API --------------------------------------------------

def test_synthetic_scenario_end_to_end(tmp_path):
    fixture = load_fixture("synthetic_repair")
    g = ClaimGraph(fixture.case)
    runner = FixtureToolRunner(fixture, run_dir=tmp_path / "run")
    V, E = EntityRef(kind="variant", label="V"), EntityRef(kind="element", label="E", canonical_id="SYN:E")
    X, Y, P = gene("X"), gene("Y"), EntityRef(kind="phenotype", label="phenotype P")
    context_x = ContextScope(label="context X", biosample="context X", source="supplied")
    f0 = claim(g, [V], "overlaps", [E], mechanism_class="regulatory", assertion_text="V overlaps element E")
    f1 = claim(g, [E], "regulates", [X], "decreases", context_x, mechanism_class="regulatory",
               assertion_text="Activating element E decreases gene X expression in context X")
    f2 = claim(g, [X], "contributes_to_trait", [P], "decreases", deps=[f1], mechanism_class="regulatory",
               assertion_text="The decrease in gene X explains phenotype P")
    h1 = hypothesis(g, [f1, f2], [f0], title="E represses X, which explains P", endpoint="phenotype P")

    s0 = runner.run(ToolRequest(tool="syn_element_overlap"), g.case, g, "computational_investigator")
    s1 = runner.run(ToolRequest(tool="syn_element_perturbation", params={"gene": "x"}), g.case, g,
                    "computational_investigator")
    gene_y = runner.run(ToolRequest(tool="syn_element_perturbation", params={"gene": "Y"}), g.case, g,
                        "computational_investigator")
    assert (gene_y.retrieval_status, gene_y.evidence_ids) == ("no_records_found", [])   # missing, not negative
    assert {g.evidence[e].evidence_class for e in s0.evidence_ids + s1.evidence_ids} == {"synthetic"}

    accepted, refused = g.apply_updates([
        GraphUpdate(kind="attach_evidence", claim_id=f0, evidence_id=s0.evidence_ids[0], stance="supports",
                    rationale="S0 places V inside E", suggested_assessment="supported_in_scope", base_version=1),
        GraphUpdate(kind="attach_evidence", claim_id=f1, evidence_id=s1.evidence_ids[0], stance="supports",
                    rationale="misread"),
        GraphUpdate(kind="attach_evidence", claim_id=f1, evidence_id=s1.evidence_ids[0], stance="contradicts",
                    rationale="the matched intervention increases X", suggested_assessment="contradicted_in_scope",
                    base_version=1),
    ], "computational_investigator")
    assert len(refused) == 1 and "opposite" in refused[0].reason
    assert [(c, g.claims[c].assessment) for c in (f0, f1, f2)] == [
        (f0, "supported_in_scope"), (f1, "contradicted_in_scope"), (f2, "unassessed")]
    assert g.claims[f2].dependency_flag == "unsupported_due_to_dependency"
    assert [g.display_status(c) for c in (f0, f1, f2)] == ["supported", "contradicted", "unresolved"]
    h = g.hypotheses[h1]
    assert h.disposition == "rejected" and f1 in h.disposition_reason and s1.evidence_ids[0] in h.disposition_reason
    assert h.path_status[f2] == "premise_failed"
    reject = next(e for e in g.events if e.action == "reject")
    assert reject.role == "code" and reject.evidence_ids == s1.evidence_ids

    _, refused = g.apply_updates([GraphUpdate(kind="add_hypothesis", hypothesis=HypothesisDraft(
        title="E represses X (regenerated)", claim_ids=[f0], required_claim_ids=[f1, f2],
        mechanism_class="regulatory", origin="regenerated", replaces=h1))], "coordinator")
    assert "repeats rejected hypothesis" in refused[0].reason
    f3 = claim(g, [E], "regulates", [Y], context=context_x, mechanism_class="regulatory",
               assertion_text="Element E regulates gene Y")
    h2 = hypothesis(g, [f3], [f0], title="E regulates Y", origin="regenerated", endpoint="phenotype P")
    g.assess(f3, "unresolved", "the fixture has no perturbation record for gene Y", "critic", 1)
    g.propagate()
    assert g.hypotheses[h2].disposition == "active" and g.claims[f3].assessment == "unresolved"
    assert g.claims[f0].assessment == "supported_in_scope"               # F0 retained

    text = g.to_json()
    again = ClaimGraph.from_json(text)
    assert again.to_json() == text and again.to_state() == g.to_state()
    assert json.loads(text)["engine_version"] == "v9.0"
    assert (tmp_path / "run" / "raw" / f"{s1.tool_call_id}.json").exists()


def test_round_trip_keeps_indexes_working():
    g = ClaimGraph(dev_case())
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    loaded = ClaimGraph.from_json(g.to_json())
    assert claim(loaded, [ELEMENT], "regulates", [gene("gene1")], "increases", ctx("Hep G2")) == c
    assert loaded.entity("gene", "GENE1") == g.entity("gene", "GENE1")
    assert claim(loaded, [ELEMENT], "regulates", [gene("GENE2")]) == "C2"        # counters continue


def test_questions_comparisons_result_and_version_semantics(g):
    binding = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")
    other = claim(g, [VARIANT], "alters_binding", [tf("TFY")], "increases")
    h1, h2 = hypothesis(g, [binding], title="TFX"), hypothesis(g, [other], title="TFY")
    q = g.add_question(Question(text="Is binding allele-specific?", target_claim_ids=[binding], hypothesis_ids=[h1],
                                route="computational", actions=[ToolRequest(tool="chip_occupancy",
                                                                            params={"tf": "TFX"})]), "coordinator")
    g.update_question(q, "unanswerable", "computational_investigator", remaining_gap="no allelic ChIP exists")
    assert g.questions[q].status == "unanswerable" and g.questions[q].remaining_gap == "no allelic ChIP exists"
    with pytest.raises(GraphRefusal, match="unknown question status"):
        g.update_question(q, "solved", "critic")
    p = g.add_comparison(PairComparison(a=h1, b=h2, outcome="insufficient_evidence", reason="both predicted only"),
                         "critic")
    with pytest.raises(GraphRefusal, match="two different hypotheses"):
        g.add_comparison(PairComparison(a=h1, b=h1, outcome="tied"), "critic")
    version = g.version
    g.log("stop", "code", "no affordable discriminating action")
    assert g.version == version and g.events[-1].graph_version_before == g.events[-1].graph_version_after
    g.set_result(RunResult(outcome="no_supported_explanation", stop_reason="no_affordable_discriminating_action",
                           summary="neither binding claim is supported"))
    assert g.version == version + 1 and g.result.outcome == "no_supported_explanation"
    assert (q, p) == ("Q1", "P1") and [e.event_id for e in g.events] == [f"D{i}" for i in range(1, len(g.events) + 1)]
