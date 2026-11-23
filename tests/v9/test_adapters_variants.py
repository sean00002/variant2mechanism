"""Which variant each adapter observation is about (core C3-1, Evidence.about_variants), on the saved responses.

The graph never lets evidence about one variant support or contradict a claim about another, and refuses allele-bearing
evidence that names no variant for an allelic claim; it reads the variant from about_variants. So every observation
made at the case variant names it (its rsID, supplied or recorded by fact collection, and "chrN:pos ref>alt"), another
variant's observation names that variant only, a GWAS Catalog row its own SNPs, a CIViC assertion its CIViC variant,
and observations about an element, a gene or a cell line only name none. Assertions are about identity, never about
which mechanism is right; rs12740374 appears only for plumbing on its saved responses.
"""

import copy
import json

import pytest

from variant2mechanism.v9.adapters import collect_facts
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, GraphRefusal
from variant2mechanism.v9.schemas import Case, ToolRequest, Variant

from .test_adapters_tools import DEV, FIXTURES, HEP3B, SORT1, Session, cache_only, case, evidence, live, run

pytestmark = pytest.mark.data

SORT1_NAMES = ["rs12740374", "chr1:109274968 G>T"]
OTHER_EQTL = "chr1:109274857 G>C"                 # GTEx's chr1_109274857_G_C_b38, in the same cCRE
ELEMENT = EntityRef(kind="element", label="EH38E1374646", canonical_id="EH38E1374646")
CLEAN = Case(case_id="REQ-CLEAN-DEV", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G"), origin="germline")
ELEMENT_ONLY = ("SCREEN-class:", "SCREEN-CRISPR:", "SCREEN-3D:")        # a cCRE's classes and gene links


@pytest.fixture
def offline(v9_cfg, tmp_path):
    return cache_only(v9_cfg, tmp_path / "run")


def claim(graph: ClaimGraph, subject: EntityRef, relation: str, obj: EntityRef, **fields) -> str:
    return graph.add_claim(ClaimDraft(subjects=[subject], relation=relation, objects=[obj], **fields), "coordinator")


def variant(label: str) -> EntityRef:
    return EntityRef(kind="variant", label=label)


def test_every_observation_at_the_case_variant_names_it_and_element_gene_and_line_items_name_none(offline):
    graph = ClaimGraph(case(SORT1, context=[HEP3B]))
    requests = (("variant_annotation", {}), ("ccre_overlap", {}), ("qbic_inventory", {}),
                ("qbic_tf_detail", {"tf": "CEBPA"}), ("chip_occupancy", {"tf": "CEBPB"}), ("gtex_eqtl", {}),
                ("gwas_associations", {}), ("credible_sets_l2g", {"trait": "LDL cholesterol"}),
                ("tf_expression", {"tf": "CEBPA"}), ("depmap_context", {"gene": "CEBPA"}))
    calls = {tool: run(offline, graph, tool, **params) for tool, params in requests}
    assert all(c.evidence_ids for c in calls.values()), {t: c.message for t, c in calls.items() if not c.evidence_ids}
    kinds, alleles = set(), 0
    for tool, call in calls.items():
        for ev in evidence(graph, call):
            mentions = {graph.variant_mention(x) for x in ev.about_variants}
            if ev.evidence_class in ("expression", "dependency_screen") or ev.independence_group.startswith(
                    ELEMENT_ONLY):
                assert ev.about_variants == [], (tool, ev.observed_result)
                kinds.add("element, gene or line")
            elif ev.data.get("case_variant") is False:       # another variant's eQTL in the element
                assert ev.about_variants == [OTHER_EQTL] and mentions == {"other"}, ev.observed_result
                kinds.add("another variant")
            elif tool == "gwas_associations":                # each Catalog row names its own SNP(s)
                assert ev.about_variants == ["rs12740374"], ev.observed_result
                kinds.add(tool)
            else:
                assert ev.about_variants == SORT1_NAMES and mentions == {"case"}, (tool, ev.observed_result)
                kinds.add(tool)
            if ev.allele is not None:                        # every allele-bearing item names its variant
                assert "case" in mentions, (tool, ev.observed_result)
                alleles += 1
    assert kinds == {"element, gene or line", "another variant", *(t for t, _ in requests
                                                                    if t not in ("tf_expression", "depmap_context"))}
    assert alleles > 100


def test_a_coordinates_only_case_is_named_by_the_rsid_fact_collection_recorded(v9_cfg, tmp_path):
    """Without a supplied rsID the case variant is named by the rsID dbSNP gives its exact alleles (recorded as its
    own by collect_facts) and its position; VEP names the rsID it found in the same call, before it is recorded."""
    runner = cache_only(v9_cfg, tmp_path / "run")
    graph = ClaimGraph(CLEAN)
    annotation, overlap, inventory, _ = collect_facts(CLEAN, graph, runner)
    assert graph.variant_aliases == {"rs1427407": annotation.tool_call_id}
    named = ["rs1427407", "chr2:60490908 T>G"]
    at_variant = [*evidence(graph, annotation), *evidence(graph, inventory),
                  *(e for e in evidence(graph, overlap) if e.independence_group.startswith("ENCODE-cCRE:"))]
    detail = runner.run(ToolRequest(tool="qbic_tf_detail", params={"tf": "SPI1"}), graph.case, graph,
                        "computational_investigator")
    at_variant += evidence(graph, detail)
    assert len(at_variant) > 300 and all(e.about_variants == named for e in at_variant)
    assert {graph.variant_mention(x) for e in at_variant for x in e.about_variants} == {"case"}


def test_an_observation_at_the_case_variant_never_bears_on_a_claim_about_another_variant(offline):
    """An overlap or a ChIP peak at rs12740374 placed nothing about rs629301 (another variant, possibly in the same
    enhancer), and another variant's eQTL in the element says nothing about rs12740374; each used to link."""
    graph = ClaimGraph(case(SORT1))
    overlap = run(offline, graph, "ccre_overlap")
    chip = run(offline, graph, "chip_occupancy", tf="CEBPB")
    [registry] = [e for e in evidence(graph, overlap) if e.independence_group.startswith("ENCODE-cCRE:")]
    other_eqtl = next(e for e in evidence(graph, overlap) if e.data.get("case_variant") is False)
    peak = evidence(graph, chip)[0]
    partner = variant("rs629301")
    with pytest.raises(GraphRefusal, match="evidence about one variant"):
        graph.link(claim(graph, partner, "overlaps", ELEMENT), registry.evidence_id, "supports",
                   "computational_investigator", "the same enhancer")
    with pytest.raises(GraphRefusal, match="evidence about one variant"):
        graph.link(claim(graph, partner, "alters_binding", EntityRef(kind="tf", label="CEBPB")), peak.evidence_id,
                   "supports", "computational_investigator", "a CEBPB peak at the locus")
    assert graph.link(claim(graph, variant("rs12740374"), "overlaps", ELEMENT), registry.evidence_id, "supports",
                      "computational_investigator", "the registry overlap").strength == "direct"
    gene = EntityRef(kind="gene", label=other_eqtl.about_genes[0])
    with pytest.raises(GraphRefusal, match="evidence about one variant"):
        graph.link(claim(graph, variant("rs12740374"), "regulates", gene), other_eqtl.evidence_id, "supports",
                   "computational_investigator", "an eQTL in the element")
    theirs = claim(graph, variant(OTHER_EQTL), "regulates", gene)
    assert graph.claim_frame(theirs) == "other"
    assert graph.link(theirs, other_eqtl.evidence_id, "supports", "computational_investigator",
                      "that variant's own eQTL").strength == "indirect"


def test_a_gwas_row_names_its_own_snps_and_a_haplotype_says_so(v9_cfg, tmp_path):
    """Two Catalog rows for rs1427407 are associations of a 20-SNP haplotype: they were written as associations of
    rs1427407 alone and named only it."""
    graph = ClaimGraph(case(DEV))
    rows = evidence(graph, run(cache_only(v9_cfg, tmp_path / "run"), graph, "gwas_associations"))
    haplotypes = [e for e in rows if len(e.about_variants) > 1]
    assert len(rows) == 25 and len(haplotypes) == 2
    assert all(e.about_variants == ["rs1427407"] for e in rows if e not in haplotypes)
    for e in haplotypes:
        assert e.about_variants[0] == "rs1427407" and len(set(e.about_variants)) == 20
        assert "a haplotype of 20 variants including rs1427407 is associated" in e.observed_result
        assert any("not of rs1427407 alone" in x for x in e.limitations) and e.allele is None
    hap = haplotypes[0]
    partner = variant(next(x for x in hap.about_variants if x != "rs1427407"))
    trait = EntityRef(kind="phenotype", label=hap.about_traits[0])
    assert graph.link(claim(graph, partner, "associated_with_trait", trait), hap.evidence_id, "supports",
                      "computational_investigator", "the haplotype holds it").stance == "supports"
    single = next(e for e in rows if e not in haplotypes)
    with pytest.raises(GraphRefusal, match="evidence about one variant"):
        graph.link(claim(graph, partner, "associated_with_trait", EntityRef(kind="phenotype",
                                                                            label=single.about_traits[0])),
                   single.evidence_id, "supports", "computational_investigator", "rs1427407's row")


def test_a_credible_set_names_the_case_variant_never_its_lead(v9_cfg, tmp_path):
    """The Catalase set holds rs12740374 with lead chr1:109275908 C>T: its PIP is the case variant's, and nothing
    found through the case variant stands for the lead."""
    fixture = json.loads((FIXTURES / "ot_credible_sets.json").read_text())["response"]
    graph = ClaimGraph(case(SORT1))
    call = run(live(v9_cfg, tmp_path / "live", Session(lambda m, u, b: (200, fixture))), graph, "credible_sets_l2g",
               trait="Catalase levels")
    items = evidence(graph, call)
    [pip] = [e for e in items if "lead_variant" in e.data]
    assert pip.data["lead_variant"] == "1_109275908_C_T" and len(items) > 1
    assert all(e.about_variants == SORT1_NAMES for e in items)
    trait = EntityRef(kind="phenotype", label="Catalase levels")
    with pytest.raises(GraphRefusal, match="evidence about one variant"):
        graph.link(claim(graph, variant("chr1:109275908 C>T"), "associated_with_trait", trait), pip.evidence_id,
                   "supports", "computational_investigator", "the set's lead")
    assert graph.link(claim(graph, variant("rs12740374"), "associated_with_trait", trait), pip.evidence_id,
                      "supports", "computational_investigator", "in the set").strength == "direct"


def test_a_civic_assertion_names_its_civic_variant_never_a_grch37_position(v9_cfg, tmp_path):
    canned = json.loads((FIXTURES / "civic_tert.json").read_text())
    browse = copy.deepcopy(canned["browse"])
    for node in browse["data"]["browseVariants"]["nodes"]:          # a test alias: CIViC lists rsIDs as RS<digits>
        node["aliases"] = ["RS100000001", "-124C>T"] if node["name"] == "C228T" else node["aliases"]
    session = Session(lambda m, url, body: (200, browse if "Browse" in body["query"] else canned["variant"]))
    tert = case(Variant(chrom="5", pos=1295113, ref="G", alt="A"), origin="somatic")
    graph = ClaimGraph(tert)
    items = evidence(graph, run(live(v9_cfg, tmp_path / "live", session), graph, "civic_lookup", genes=["TERT"],
                                variant="C228T"))
    assert len(items) == 3 and all(e.about_variants == ["TERT C228T", "rs100000001"] for e in items)
    assert not any("1295228" in x for e in items for x in e.about_variants)        # CIViC's GRCh37 coordinates
    assert {graph.variant_mention(x) for x in items[0].about_variants} == {None, "other"}
