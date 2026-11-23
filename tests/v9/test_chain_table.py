"""table.py: a run's answer as eight claims per chain with three cells each, the reader for saved runs and the checker.

Graphs are built through the graph API on the development variant rs1427407 (chr2:60490908 T>G); TF, gene and trait
names and every observation are stipulated for the tests, not claims about that variant.
"""

import importlib.util
import json
import sys
from typing import get_args

import pytest

from variant2mechanism.config import REPO
from variant2mechanism.v9 import chain
from variant2mechanism.v9 import table as T
from variant2mechanism.v9.graph import ClaimGraph, EntityRef
from variant2mechanism.v9.schemas import (
    ContextScope,
    Evidence,
    ExperimentRecord,
    Question,
    Relation,
    RunResult,
    ToolCall,
)

from .test_chain_view import INVESTIGATOR, TRAIT
from .test_report_support import (
    ELEMENT,
    HEPG2,
    VARIANT,
    claim,
    dev_case,
    gene,
    inventory_call,
    inventory_row,
    tf,
    tool_evidence,
    write_run,
)

CASE_NAMES = ["rs1427407"]
LIVER = ContextScope(label="Liver", source="evidence")


def call(g: ClaimGraph, tool: str, status: str = "records_found", evidence=(), **kw) -> ToolCall:
    return g.record_tool_call(ToolCall(tool_call_id=g.reserve_tool_call_id(), tool_name=tool,
                                       execution_status="success", retrieval_status=status,
                                       requested_by="code", charged_to="code", **kw), list(evidence))


def paper(g: ClaimGraph, cls: str, text: str, read: str, *, pmid: str = "PMID:1", **fields) -> str:
    """One experiment read from an article the run read: a literature record with its quoted passage."""
    record = ExperimentRecord(source_id=pmid, access="full_text", location="results/p2", passage=text,
                              manipulated="allele")
    ev = Evidence(evidence_class=cls, observed_result=text, independence_group=f"{pmid}#{cls}", origin="literature",
                  source_ids=[pmid], experiment=record, retrieval_ref=read, access="full_text",
                  about_variants=CASE_NAMES, **fields)
    return g.add_evidence(ev, "literature_investigator")


def eqtl_record(g: ClaimGraph, symbol: str, context: ContextScope | None = None, variants=CASE_NAMES) -> str:
    where = f" in {context.label}" if context else ""
    return tool_evidence(g, "association", f"eQTL: G is associated with higher {symbol}{where}.", tool="gtex_eqtl",
                         about_genes=[symbol], allele="G", direction="increases", about_variants=list(variants),
                         context=context)


def route() -> tuple[ClaimGraph, dict[str, str]]:
    """One chain, TFX -> GENE1 -> LDL cholesterol, with a record of each kind: a QBiC-SELEX inventory item and an
    EMSA from an article for binding, the element's cCRE record, a GTEx eQTL, and a GWAS Catalog association."""
    g = ClaimGraph(dev_case())
    ids: dict[str, str] = {}
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"}]), inventory_row(2, False)])
    ids["binding"] = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", HEPG2)
    ids["read"] = call(g, "literature_read", read_article="PMID:1", article_ids=["1"]).tool_call_id
    ids["emsa"] = paper(g, "binding_assay", "TFX bound the G probe more strongly than the T probe.", ids["read"],
                        about_tfs=["TFX"], allele="G", direction="increases", context=HEPG2)
    g.link(ids["binding"], ids["emsa"], "supports", "literature_investigator", "the G probe binds TFX more")
    ids["place"] = claim(g, [VARIANT], "overlaps", [ELEMENT])
    ids["ccre"] = tool_evidence(g, "annotation", "chr2:60490908 lies in cCRE EH38E0000001.", tool="ccre_overlap",
                                about_elements=["EH38E0000001"], about_variants=CASE_NAMES)
    g.link(ids["place"], ids["ccre"], "supports", "code", "the registry places the variant in it")
    ids["gene"] = claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    ids["eqtl"] = eqtl_record(g, "GENE1")
    g.link(ids["gene"], ids["eqtl"], "supports", INVESTIGATOR, "same allele and direction")
    ids["trait"] = claim(g, [VARIANT], "associated_with_trait", [TRAIT], "decreases")
    ids["gwas"] = tool_evidence(g, "association", "GWAS: G is associated with lower LDL cholesterol.",
                                tool="gwas_associations", about_traits=["LDL cholesterol"], allele="G",
                                direction="decreases", about_variants=CASE_NAMES)
    g.link(ids["trait"], ids["gwas"], "supports", INVESTIGATOR, "same allele and direction")
    return g, ids


def first(table: T.Table, slot: str) -> T.TableClaim:
    return table.claims[table.chains[0].claims[slot]]


def rules(problems) -> list[str]:
    return sorted({p.rule for p in problems})


# --- the definition ------------------------------------------------------------------------------------------------------

def test_the_eight_slots_cover_every_relation_and_only_the_trait_step_shares_two():
    placed = [r for slot in T.SLOTS.values() for r in slot.relations]
    assert set(placed) == set(get_args(Relation)) - {"other"}
    twice = {r for r in placed if placed.count(r) > 1}
    assert twice == {"contributes_to_trait", "affects_process"}                # said of the variant, or of a gene
    assert T.SLOTS["trait.allele"].relations >= twice and T.SLOTS["trait.premise"].relations == twice
    assert list(T.SLOTS) == [f"{step}.{part}" for step, _ in T.STEPS for part, _ in T.PARTS]


def test_every_source_row_gives_records_that_can_count_in_its_cell():
    for s in T.SOURCES:
        assert s.classes and s.classes <= T.slot_classes(s.slot), (s.tool, s.slot)
        model = s.classes <= chain.PREDICTION_CLASSES
        assert s.lane == "literature" or (s.lane == "model") == model, (s.tool, s.slot)
        if s.lane != "literature":
            assert not s.classes & chain.PREDICTION_CLASSES or model, (s.tool, s.slot)


def test_eighteen_cells_have_a_source_and_six_have_none():
    without = sorted(f"{slot}/{lane}" for slot in T.SLOTS for lane in T.LANE_KEYS if not T.sources_for(slot, lane))
    assert without == ["activity.allele/model", "activity.premise/model", "binding.premise/model",
                       "gene.allele/model", "gene.premise/model", "trait.allele/model"]
    # one tool, two cells: its records are told apart by whether the protein binds DNA itself
    assert [s.tool for s in T.sources_for("binding.allele", "database")] == ["adastra_asb"]
    assert [s.tool for s in T.sources_for("activity.allele", "database")] == ["adastra_asb"]


def test_a_record_counts_once_per_fact_it_states():
    """The variant's own eQTL is the allele claim's record; it is not also a source for the premise it implies."""
    assert [s.tool for s in T.sources_for("gene.premise", "database")] == ["ccre_overlap"]
    assert T.sources_for("gene.premise", "database")[0].classes == {"perturbation"}
    homes = sorted(s.slot for s in T.SOURCES if s.tool == "credible_sets_l2g" and s.lane == "model")
    assert homes == ["trait.premise"]


def test_a_row_says_which_of_a_tools_records_it_means():
    """One tool, one evidence class, three facts: a credible set, its colocalisation with an RNA QTL of a gene, and
    its colocalisation with a protein QTL, which is no record about the gene's RNA."""
    g = ClaimGraph(dev_case())
    kinds = {
        "set": dict(about_traits=["LDL cholesterol"]),
        "eqtl": dict(about_traits=["LDL cholesterol"], about_genes=["GENE1"], data={"qtl_type": "eqtl"}),
        "pqtl": dict(about_traits=["LDL cholesterol"], about_genes=["GENE9"], data={"qtl_type": "pqtl"}),
    }
    ids = {name: tool_evidence(g, "statistical_inference", f"a {name} record", tool="credible_sets_all",
                               about_variants=CASE_NAMES, **fields) for name, fields in kinds.items()}
    homes = {name: sorted(key for key in T.SLOT_KEYS
                          if T.listed(key, "database", "credible_sets_all", g.evidence[eid]))
             for name, eid in ids.items()}
    assert homes == {"set": ["trait.allele"], "eqtl": ["gene.allele", "trait.premise"], "pqtl": ["trait.premise"]}
    assert not T.listed("trait.allele", "database", "gwas_associations", g.evidence[ids["set"]])      # another tool


def test_an_experiment_the_class_matrix_holds_indirect_cannot_count():
    assert "binding_assay" not in T.slot_classes("activity.allele")             # an EMSA is not a test of activity
    assert "annotation" not in T.slot_classes("gene.premise")                   # a 3D contact is not regulation
    assert "occupancy" in T.slot_classes("binding.allele")                      # allele-specific ChIP reads can


def test_the_definition_page_carries_the_same_map_states_and_rules_as_the_code():
    page = (REPO / "docs" / "chain-table.md").read_text(encoding="utf-8")
    flat = " ".join(page.split())
    assert T.source_table() in page
    for _, words, meaning in T.STATES:
        assert f"| {words} | {meaning} |" in page
    for _, text in T.RULES:
        assert " ".join(text.split()) in flat
    for slot in T.SLOTS.values():
        assert slot.text in flat


# --- reading a run -------------------------------------------------------------------------------------------------------

def test_a_route_reads_as_one_chain_with_a_record_of_each_kind():
    g, ids = route()
    table = T.from_graph(g)
    assert len(table.chains) == 1 and list(table.chains[0].claims) == list(T.SLOT_KEYS)
    stated = {slot: table.claims[ident].stated for slot, ident in table.chains[0].claims.items()}
    assert stated == {"binding.allele": True, "binding.premise": False, "activity.allele": False,
                      "activity.premise": True, "gene.allele": True, "gene.premise": False, "trait.allele": True,
                      "trait.premise": False}
    binding = first(table, "binding.allele")
    assert {lane: cell.state for lane, cell in binding.cells.items()} == {
        "database": "not_checked", "model": "supports", "literature": "supports"}     # this run never asked ADASTRA
    assert [r.id for r in binding.cells["literature"].records] == [ids["emsa"]]
    assert binding.cells["literature"].records[0].passage == "TFX bound the G probe more strongly than the T probe."
    assert binding.cells["model"].records[0].note.startswith("read from the QBiC-SELEX inventory")
    assert binding.strongest == "assay" and binding.names["tfs"] == ["TFX"]
    place = first(table, "activity.premise")
    assert place.cells["database"].state == "supports" and place.strongest == "recorded"
    assert first(table, "gene.allele").cells["database"].state == "supports"
    assert first(table, "trait.allele").cells["database"].records[0].kind == "association"
    assert T.check(table, g) == []


def test_reading_changes_nothing_and_is_deterministic_json():
    g, _ = route()
    before = g.to_json()
    one, two = T.from_graph(g).model_dump_json(), T.from_graph(g).model_dump_json()
    assert one == two and g.to_json() == before
    assert json.loads(one)["format"] == T.FORMAT


def test_the_strongest_record_of_an_allele_claim_is_the_chain_views_rung():
    g, _ = route()
    row = chain.chain_view(g)["ranked"]["chains"][0]
    table = T.from_graph(g)
    for link, slot in (("binding", "binding.allele"), ("gene", "gene.allele"), ("trait", "trait.allele")):
        assert first(table, slot).strongest == row["cells"][link]["kind"]


def test_a_gene_to_trait_claim_is_the_trait_steps_premise_and_an_element_to_gene_claim_the_gene_steps():
    g, _ = route()
    onward = claim(g, [gene("GENE1")], "contributes_to_trait", [TRAIT], "decreases")
    l2g = tool_evidence(g, "precomputed_prediction", "L2G scores GENE1 0.81 for LDL cholesterol.",
                        tool="credible_sets_l2g", about_genes=["GENE1"], about_traits=["LDL cholesterol"],
                        about_variants=CASE_NAMES)
    g.link(onward, l2g, "supports", INVESTIGATOR, "the same gene and trait")
    wired = claim(g, [ELEMENT], "regulates", [gene("GENE1")])
    table = T.from_graph(g)
    premise = first(table, "trait.premise")
    assert premise.graph_claims == [onward] and premise.cells["model"].state == "supports"
    assert premise.cells["model"].records[0].kind == "prediction" and premise.strongest == "prediction"
    assert first(table, "gene.premise").graph_claims == [wired]
    assert first(table, "gene.allele").graph_claims != first(table, "gene.premise").graph_claims
    assert T.check(table, g) == []


def test_a_record_from_another_context_stands_beside_and_the_cell_says_nothing_found():
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases", HEPG2)
    eid = eqtl_record(g, "GENE1", LIVER)
    g.link(cid, eid, "supports", INVESTIGATOR, "the same gene", applicability="different")
    cell = first(T.from_graph(g), "gene.allele").cells["database"]
    assert cell.state == "nothing_found" and cell.lookups and cell.unjudged == []
    assert [(r.stance, r.note) for r in cell.records] == [("beside", "from another context")]
    assert T.check(T.from_graph(g), g) == []


def test_a_record_on_file_that_nobody_judged_is_listed_and_breaks_the_rule():
    g, ids = route()
    left = eqtl_record(g, "GENE1", LIVER)                                        # same gene, this variant: unjudged
    eqtl_record(g, "GENE2")                                                      # another gene: not this claim's
    eqtl_record(g, "GENE1", HEPG2, variants=["rs999"])                           # a neighbour's eQTL: not its alleles
    table = T.from_graph(g)
    cell = first(table, "gene.allele").cells["database"]
    assert cell.state == "supports" and cell.unjudged == [left] and cell.unjudged_total == 1
    problems = T.check(table, g)
    assert rules(problems) == ["unjudged"] and left in problems[0].text


def test_a_claim_with_records_on_file_and_none_linked_is_not_checked_not_nothing_found():
    g = ClaimGraph(dev_case())
    claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    eqtl_record(g, "GENE1")
    cell = first(T.from_graph(g), "gene.allele").cells["database"]
    assert cell.state == "not_checked" and cell.unjudged_total == 1


def test_a_lookup_that_returned_nothing_for_the_gene_is_nothing_found_and_no_lookup_is_not_checked():
    g = ClaimGraph(dev_case())
    claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    assert first(T.from_graph(g), "gene.allele").cells["database"].state == "not_checked"
    eqtl_record(g, "GENE2")                                                      # GTEx was asked; nothing for GENE1
    cell = first(T.from_graph(g), "gene.allele").cells["database"]
    assert cell.state == "nothing_found" and len(cell.lookups) == 1
    assert first(T.from_graph(g), "gene.allele").cells["model"].state == "no_source"


def test_a_lookup_filtered_to_another_gene_did_not_look_for_this_one():
    g = ClaimGraph(dev_case())
    claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    call(g, "gtex_eqtl", "no_records_found", query_parameters={"gene": "GENE2"})
    assert first(T.from_graph(g), "gene.allele").cells["database"].state == "not_checked"
    call(g, "gtex_eqtl", "no_records_found", query_parameters={"gene": "GENE1"})
    assert first(T.from_graph(g), "gene.allele").cells["database"].state == "nothing_found"


def test_a_literature_cell_is_looked_into_only_by_reads_for_a_question_about_its_claim():
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")
    call(g, "literature_read", read_article="PMID:9", article_ids=["9"])         # a read for no question
    assert first(T.from_graph(g), "binding.allele").cells["literature"].state == "not_checked"
    qid = g.add_question(Question(text="Is there an allelic binding assay?", target_claim_ids=[cid],
                                  route="literature"), "coordinator")
    call(g, "literature_read", read_article="PMID:10", article_ids=["10"], question_id=qid)
    assert first(T.from_graph(g), "binding.allele").cells["literature"].state == "nothing_found"


@pytest.mark.parametrize("rows, state, note", [
    ([inventory_row(1, False, [{"tf": "TFX", "mapping": "own"}])], "nothing_found",
     "its QBiC-SELEX models do not pass the gate"),
    ([inventory_row(1, True, [{"tf": "TFY", "mapping": "own"}])], "no_source", "no QBiC-SELEX model covers it"),
])
def test_models_below_the_gate_found_nothing_and_a_factor_without_a_model_has_no_source(rows, state, note):
    g = ClaimGraph(dev_case())
    inventory_call(g, rows)
    claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases")
    table = T.from_graph(g)
    cell = first(table, "binding.allele").cells["model"]
    assert (cell.state, cell.note) == (state, note) and bool(cell.lookups) == (state == "nothing_found")
    assert T.check(table, g) == []


def test_a_prediction_for_the_other_allele_disagrees_and_gives_the_claim_no_support():
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"}])])          # favours G, the alt
    claim(g, [VARIANT], "alters_binding", [tf("TFX")], "decreases")                         # G binds less
    table = T.from_graph(g)
    binding = first(table, "binding.allele")
    assert binding.cells["model"].state == "disagrees" and binding.strongest == "none"
    assert chain.chain_view(g)["ranked"]["chains"][0]["cells"]["binding"]["kind"] == "none"
    assert T.check(table, g) == []


def test_a_record_the_graph_refused_for_the_claim_is_set_aside_with_the_graphs_reason():
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    eid = eqtl_record(g, "GENE1")
    g.log("refuse_update", "coordinator", f"{eid} was proposed with the wrong allele", target_ids=[cid, eid])
    cell = first(T.from_graph(g), "gene.allele").cells["database"]
    assert [(s.record, s.why) for s in cell.set_aside] == [(eid, f"{eid} was proposed with the wrong allele")]
    assert cell.state == "nothing_found" and cell.unjudged == []
    assert "1 set aside" in T.to_markdown(T.from_graph(g))


def test_a_claim_that_is_no_step_is_listed_beside_the_table():
    g, _ = route()
    loose = claim(g, [tf("TFX")], "regulates", [gene("GENE1")])
    table = T.from_graph(g)
    assert [b["claim"] for b in table.beside] == [loose]
    assert all(loose not in c.graph_claims for c in table.claims.values())


def test_a_run_with_no_claims_gives_one_chain_of_eight_claims_nobody_stated():
    g = ClaimGraph(dev_case())
    table = T.from_graph(g)
    assert len(table.chains) == 1 and table.chains[0].title == "no chain stated"
    assert all(not c.stated and not c.graph_claims for c in table.claims.values()) and len(table.claims) == 8
    assert T.check(table, g) == []
    numbers = T.counts(table)
    assert numbers["claims_stated"] == 0 and numbers["cells"]["no_source"] == 6
    assert numbers["cells"]["not_checked"] == 18 and sum(numbers["cells"].values()) == 24
    assert "no TF named (not stated by the run)" in T.to_markdown(table)


def test_a_claim_nobody_stated_still_names_what_the_chain_names_and_reports_what_is_on_file():
    """The run asked nothing about the TF being in place, and holds an expression level and a ChIP-seq survey for
    it: the cell says "not checked" and counts the record, where the old reading said "no claim"."""
    g, _ = route()
    level = tool_evidence(g, "expression", "TFX is expressed at 12 TPM in HepG2.", tool="tf_expression",
                          about_tfs=["TFX"], about_genes=["TFX"], context=HEPG2)
    tool_evidence(g, "expression", "TFY is expressed at 3 TPM in HepG2.", tool="tf_expression",
                  about_tfs=["TFY"], about_genes=["TFY"], context=HEPG2)          # another TF: not this claim's
    table = T.from_graph(g)
    premise = first(table, "binding.premise")
    assert not premise.stated and premise.names["tfs"] == ["TFX"] and premise.label == "TFX"
    cell = premise.cells["database"]
    assert (cell.state, cell.unjudged) == ("not_checked", [level])
    assert premise.cells["model"].state == "no_source" and premise.cells["literature"].state == "not_checked"
    onward = first(table, "trait.premise")
    assert onward.names["genes"] == ["GENE1"] and onward.names["traits"] == ["LDL cholesterol"]
    assert rules(T.check(table, g)) == ["unjudged"]


def test_a_claim_that_names_nothing_is_about_anything_of_that_kind_at_the_variant():
    """No binding claim was made, and the inventory holds a gate-passing prediction: it is on file and not judged."""
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"}])])
    claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    binding = first(T.from_graph(g), "binding.allele")
    assert not binding.stated and binding.label == "no TF named" and binding.names["tfs"] == []
    assert (binding.cells["model"].state, binding.cells["model"].unjudged_total) == ("not_checked", 1)


def test_a_shared_ontology_term_is_enough_to_need_a_judgement():
    """A locus-to-gene score filed under another label of the trait's term is a record somebody has to judge."""
    g = ClaimGraph(dev_case())
    term = EntityRef(kind="phenotype", label="LDL cholesterol", canonical_id="EFO_0004611")
    claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    claim(g, [VARIANT], "associated_with_trait", [term], "decreases")
    left = tool_evidence(g, "precomputed_prediction", "L2G scores GENE1 0.8 for LDL-C levels.",
                         tool="credible_sets_l2g", about_genes=["GENE1"],
                         about_traits=["LDL-C levels", "EFO_0004611"], about_variants=CASE_NAMES)
    tool_evidence(g, "precomputed_prediction", "L2G scores GENE1 0.4 for height.", tool="credible_sets_l2g",
                  about_genes=["GENE1"], about_traits=["body height", "EFO_0004339"], about_variants=CASE_NAMES)
    premise = first(T.from_graph(g), "trait.premise")
    assert "EFO_0004611" in premise.names["trait_ids"]
    assert premise.cells["model"].unjudged == [left] and premise.cells["model"].state == "not_checked"


def test_a_record_that_shows_a_tf_in_place_is_named_by_its_class_not_as_an_allele_assay():
    g, _ = route()
    bound = claim(g, [tf("TFX")], "occupies", [VARIANT])
    peak = tool_evidence(g, "occupancy", "ChIP-seq for TFX in HepG2 has a peak containing chr2:60490908.",
                         tool="chip_occupancy", about_tfs=["TFX"], about_variants=CASE_NAMES, context=HEPG2)
    g.link(bound, peak, "supports", "code", "a ChIP-seq peak of TFX contains the variant")
    table = T.from_graph(g)
    premise = first(table, "binding.premise")
    assert premise.stated and premise.graph_claims == [bound]
    assert [(r.stance, r.kind) for r in premise.cells["database"].records] == [("supports", None)]
    assert premise.strongest == "recorded" and "supports: 1 (occupancy)" in T.to_markdown(table)
    assert T.check(table, g) == []


def test_the_gene_to_trait_claim_holds_every_standing_claim_that_names_the_gene():
    """A colocalisation and a locus-to-gene score for the same gene and two traits are one table claim: the score
    is not left unjudged because the view shows only the strongest of them in the chain's cell."""
    g, _ = route()
    other = EntityRef(kind="phenotype", label="apolipoprotein B")
    strong = claim(g, [gene("GENE1")], "contributes_to_trait", [TRAIT])
    weak = claim(g, [gene("GENE1")], "contributes_to_trait", [other])
    coloc = tool_evidence(g, "statistical_inference", "The LDL signal colocalises with an eQTL of GENE1.",
                          tool="credible_sets_all", about_genes=["GENE1"], about_traits=["LDL cholesterol"],
                          about_variants=CASE_NAMES, data={"qtl_type": "eqtl"})
    score = tool_evidence(g, "precomputed_prediction", "L2G scores GENE1 0.7 for apolipoprotein B.",
                          tool="credible_sets_all", about_genes=["GENE1"], about_traits=["apolipoprotein B"],
                          about_variants=CASE_NAMES)
    g.link(strong, coloc, "supports", "code", "the signal colocalises with a QTL of GENE1")
    g.link(weak, score, "supports", "code", "the locus-to-gene model scores GENE1")
    table = T.from_graph(g)
    premise = first(table, "trait.premise")
    assert premise.graph_claims == [strong, weak] and premise.strongest == "association"
    assert premise.cells["model"].state == "supports" and premise.cells["database"].state == "supports"
    assert not [p for p in T.check(table, g) if "trait.premise" in p.where]


# --- the checker ---------------------------------------------------------------------------------------------------------

def test_a_record_from_a_source_the_map_does_not_list_breaks_the_record_rule():
    g = ClaimGraph(dev_case())
    cid = claim(g, [VARIANT], "associated_with_expression", [gene("GENE1")], "increases")
    eid = tool_evidence(g, "association", "eQTL: G is associated with higher GENE1.", about_genes=["GENE1"],
                        allele="G", direction="increases", about_variants=CASE_NAMES)        # tool "test_tool"
    g.link(cid, eid, "supports", INVESTIGATOR, "same allele and direction")
    problems = T.check(T.from_graph(g), g)
    assert rules(problems) == ["record"] and "test_tool" in problems[0].text


def test_the_checker_reads_the_runs_files_not_the_tables_copy():
    g, ids = route()
    table = T.from_graph(g)
    cell = first(table, "gene.allele").cells["database"]
    cell.records[0].id = "E999"
    assert "E999 is not in the run's files" in [p.text for p in T.check(table, g)]
    table = T.from_graph(g)
    first(table, "gene.allele").cells["database"].records[0].id = ids["emsa"]    # a literature record, an EMSA
    texts = [p.text for p in T.check(table, g)]
    assert f"{ids['emsa']} is a literature record" in texts
    assert any("cannot count for this claim" in t for t in texts)


def test_a_counted_record_for_an_allele_claim_must_name_this_variant():
    g, _ = route()
    stray = tool_evidence(g, "association", "eQTL of the element's other variant for GENE1.", tool="gtex_eqtl",
                          about_genes=["GENE1"], about_variants=["rs999"])
    table = T.from_graph(g)
    cell = first(table, "gene.allele").cells["database"]
    cell.records.append(T.Record(id=stray, stance="supports", evidence_class="association", kind="association"))
    assert [p.rule for p in T.check(table, g)] == ["variant"]


def test_states_must_match_what_the_cell_counts_and_cites():
    g, _ = route()
    table = T.from_graph(g)
    cell = first(table, "trait.allele").cells["database"]
    cell.state = "nothing_found"                                 # it counts a record, and cites no lookup that failed
    cell.lookups = []
    assert [p.rule for p in T.check(table, g)] == ["record", "looked"]
    table = T.from_graph(g)
    first(table, "activity.allele").cells["model"].state = "not_checked"         # the map lists no source there
    first(table, "trait.allele").cells["literature"].state = "no_source"         # the map lists one, no reason given
    assert [p.rule for p in T.check(table, g)] == ["looked", "looked"]


def test_a_chain_missing_a_slot_or_naming_an_unknown_claim_breaks_the_shape():
    g, _ = route()
    table = T.from_graph(g)
    del table.chains[0].claims["trait.premise"]
    table.chains[0].claims["gene.allele"] = "gene.allele:C99"
    table.chains[0].claims["binding.allele"] = table.chains[0].claims["trait.allele"]
    table.chains[0].claims["gene.premise"] = None
    found = [p.text for p in T.check(table, g) if p.rule == "shape"]
    assert len(found) == 4 and any("C99" in t for t in found) and any("another slot" in t for t in found)
    assert any("every chain has all eight" in t for t in found)
    table = T.from_graph(g)
    first(table, "binding.premise").stated = True                  # the table says a claim states it; none does
    assert [p.rule for p in T.check(table, g)] == ["shape"]


def test_a_literature_record_without_its_passage_breaks_the_quoted_rule():
    g, ids = route()
    g.evidence[ids["emsa"]].experiment.passage = "  "
    assert rules(T.check(T.from_graph(g), g)) == ["quoted"]


# --- the numbers and the text --------------------------------------------------------------------------------------------

def test_counts_describe_the_first_chain():
    g, _ = route()
    eqtl_record(g, "GENE1", LIVER)
    table = T.from_graph(g)
    numbers = T.counts(table, T.check(table, g))
    assert (numbers["chains"], numbers["tied"], numbers["claims_stated"], numbers["claims_supported"]) == (1, 1, 4, 4)
    assert numbers["parts"] == {"allele": {"stated": 3, "supported": 3}, "premise": {"stated": 1, "supported": 1}}
    assert numbers["cells"] == {"supports": 5, "disagrees": 0, "both": 0, "nothing_found": 1, "not_checked": 12,
                                "no_source": 6}
    assert sum(numbers["cells"].values()) == 24
    assert numbers["lanes"] == {"database": {"with_source": 8, "supported": 3},
                                "model": {"with_source": 2, "supported": 1},
                                "literature": {"with_source": 8, "supported": 1}}
    assert numbers["unjudged"] == 1 and numbers["problems"]["unjudged"] == 1
    assert numbers["strongest"]["binding.allele"] == "assay" and numbers["strongest"]["trait.premise"] == "none"


def test_the_markdown_shows_the_first_chain_and_escapes_graph_text():
    g, _ = route()
    claim(g, [VARIANT], "alters_regulatory_activity", [EntityRef(kind="element", label="a | b construct")])
    text = T.to_markdown(T.from_graph(g), [])
    assert "Chain 1 of 1: TFX → GENE1" in text and "a \\| b construct" in text
    assert "| TF binding | The parts are in place | TFX (not stated by the run) | not checked |" in text
    assert text.rstrip().endswith("The table passes every rule.")
    row = next(line for line in text.splitlines() if line.startswith("| TF binding | The alleles differ"))
    assert row.count("|") == 7 and "not checked" in row and "supports: 1 (assay)" in row


# --- the script ----------------------------------------------------------------------------------------------------------

def load_script():
    spec = importlib.util.spec_from_file_location("v9_chain_table", REPO / "scripts" / "v9_chain_table.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_the_script_writes_tables_and_a_summary_and_never_into_the_runs(tmp_path, monkeypatch, capsys):
    g, _ = route()
    eqtl_record(g, "GENE1", LIVER)
    g.set_result(RunResult(outcome="no_supported_explanation", stop_reason="coordinator_stop", summary="none"))
    runs = tmp_path / "runs"
    write_run(g, runs / "case_a")
    write_run(ClaimGraph(dev_case()), runs / "case_b")
    before = sorted(p.name for p in (runs / "case_a").iterdir())
    script = load_script()
    out = tmp_path / "tables"
    monkeypatch.setattr(sys, "argv", ["v9_chain_table.py", "--runs", str(runs), "--out", str(out)])
    assert script.main() == 0
    assert sorted(p.name for p in (runs / "case_a").iterdir()) == before
    saved = T.Table.model_validate_json((out / "case_a" / "table.json").read_text(encoding="utf-8"))
    assert saved == T.from_graph(g)
    summary = (out / "summary.md").read_text(encoding="utf-8")
    assert "| case_a | 1 (1) | 4 of 8 | 4 |" in summary and "| case_b | 1 (1) | 0 of 8 | 0 |" in summary
    assert "| `gtex_eqtl` | 2 | 1 | 0 |" in summary and "| unjudged | 1 |" in summary
    assert "| case_a | 0 | 1 | 1 | 0 | 1 | 1 | 1 |" in summary          # one read of one article, one record, linked
    rows = json.loads((out / "summary.json").read_text(encoding="utf-8"))
    assert [r["run"] for r in rows] == ["case_a", "case_b"] and rows[0]["outcome"] == "no_supported_explanation"
    assert rows[1]["funnel"] == dict.fromkeys(rows[1]["funnel"], 0)
    assert rows[0]["problems"][0]["rule"] == "unjudged"
    capsys.readouterr()
    assert script.main() == 2 and "already exists" in capsys.readouterr().err   # a second run needs a new folder
