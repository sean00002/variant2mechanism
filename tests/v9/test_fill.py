"""fill.py: the chain table filled by code alone, from the records an evidence bundle and its lookups hold.

Graphs hold records shaped as the adapters write them, on the development variant rs1427407 (chr2:60490908 T>G); TF,
gene and trait names and every observation are stipulated for the tests, not claims about that variant. No test here
calls a model, a provider or the network.
"""

import pytest

from variant2mechanism.v9 import chain, fill
from variant2mechanism.v9 import table as T
from variant2mechanism.v9.graph import ClaimGraph, GraphRefusal
from variant2mechanism.v9.schemas import Case, ContextScope, Evidence, ToolCall, Variant

from .test_report_support import HEPG2, dev_case, discordant_inventory, inventory_call, inventory_row

CASE = ["rs1427407"]
ELEMENT = "EH38E0000001"
LIVER = ContextScope(label="Liver", source="evidence")
K562 = ContextScope(label="K562", source="evidence")
LDL = {"id": "EFO_0004611", "name": "low density lipoprotein cholesterol measurement"}
TFX = [{"tf": "TFX", "mapping": "own"}]


def record(cls: str, text: str, **fields) -> Evidence:
    return Evidence(evidence_class=cls, observed_result=text, independence_group=fields.pop("group", text),
                    origin="tool", **fields)


def code_call(g: ClaimGraph, tool: str, evidence=(), observations=(), status: str | None = None, **params) -> ToolCall:
    """One of code's own tool calls with its records, as the runner records it."""
    evidence = list(evidence)
    return g.record_tool_call(ToolCall(
        tool_call_id=g.reserve_tool_call_id(), tool_name=tool, execution_status="success",
        retrieval_status=status or ("records_found" if evidence else "no_records_found"),
        observations=list(observations), query_parameters=params, requested_by="code", charged_to="code"), evidence)


def bundle_graph(case: Case | None = None, rows=None) -> ClaimGraph:
    """What an evidence bundle and the fill's lookups hold for one variant: a gate-passing QBiC-SELEX group (TFX), the
    variant's cCRE with a CRISPR link to GENE1 and the variant's eQTL for GENE1, a GWAS association, the ChIP-seq
    survey and a peak of TFX, a credible set with its locus-to-gene score and two colocalisations, and Open Targets'
    burden test linking GENE1 to the trait."""
    g = ClaimGraph(case or dev_case())
    inventory_call(g, rows or [inventory_row(1, True, TFX), inventory_row(2, False)])
    ccre = code_call(g, "ccre_overlap", [
        record("annotation", "chr2:60490908 lies in cCRE EH38E0000001.", about_elements=[ELEMENT],
               about_variants=CASE),
        record("perturbation", "CRISPRi of cCRE EH38E0000001 in HepG2 changed GENE1.", about_elements=[ELEMENT],
               about_genes=["GENE1"], context=HEPG2, direction="increases"),
        record("association", "SCREEN eQTL link: the variant is an eQTL for GENE1 in Liver.",
               about_elements=[ELEMENT], about_genes=["GENE1"], about_variants=CASE, allele="G",
               direction="increases", context=LIVER, group="GTEX:GENE1:Liver"),
        record("annotation", "cCRE EH38E0000001 contacts GENE2 (Hi-C).", about_elements=[ELEMENT],
               about_genes=["GENE2"]),
    ])
    g.add_variant_element(ELEMENT, ccre.tool_call_id)
    code_call(g, "gwas_associations", [
        record("association", "GWAS Catalog GCST1: rs1427407 is associated with LDL cholesterol levels.",
               about_traits=sorted({LDL["id"], LDL["name"], "LDL cholesterol levels"}), about_variants=CASE,
               allele="G", direction="decreases", data={"accession": "GCST1"}, group="GWAS-STUDY:GCST1")],
        observations=[{"record": "association", "accession": "GCST1", "trait": "LDL cholesterol levels",
                       "reported_traits": ["LDL cholesterol levels"],
                       "efo": [{"id": LDL["id"], "label": LDL["name"]}]}])
    code_call(g, "chip_occupancy", observations=[{"record": "factor", "tf": "TFX", "experiments": 1},
                                                  {"record": "factor", "tf": "TFQ", "experiments": 2}],
              status="records_found")
    code_call(g, "tf_occupancy_set", [
        record("occupancy", "ChIP-seq for TFX in HepG2 (ENCSR1) has a peak containing chr2:60490908.",
               about_tfs=["TFX"], about_elements=[ELEMENT], about_variants=CASE, context=HEPG2,
               group="CHIP:ENCSR1")], tfs=["TFX"])
    sets = {"study_locus_id": "SL1", "study_id": "GCST1"}
    code_call(g, "credible_sets_all", [
        record("statistical_inference", "Open Targets: the variant is in credible set SL1 (LDL-C).",
               about_traits=["LDL-C", LDL["name"], LDL["id"]], about_variants=CASE, data=sets,
               group="GWAS-STUDY:GCST1"),
        record("precomputed_prediction", "Open Targets L2G scores GENE1 0.810 for credible set SL1 (LDL-C).",
               about_genes=["GENE1"], about_traits=["LDL-C", LDL["name"], LDL["id"]], about_variants=CASE,
               data={**sets, "gene": "GENE1"}, group="GWAS-STUDY:GCST1"),
        record("statistical_inference", "Credible set SL1 colocalises with the eqtl credible set of GENE1 in Liver.",
               about_genes=["GENE1"], about_traits=["LDL-C", LDL["name"], LDL["id"]], about_variants=CASE,
               data={**sets, "qtl_type": "eqtl"}, context=LIVER, group="GWAS-STUDY:GCST1"),
        record("statistical_inference", "Credible set SL1 colocalises with the pqtl credible set of GENE9 in plasma.",
               about_genes=["GENE9"], about_traits=["LDL-C", LDL["name"], LDL["id"]], about_variants=CASE,
               data={**sets, "qtl_type": "pqtl"}, group="GWAS-STUDY:GCST1"),
    ], observations=[{"record": "summary", "credible_sets": 1, "read": 1},
                     {"record": "set", **sets, "trait": "LDL-C", "diseases": [LDL]}])
    code_call(g, "gene_disease", [
        record("association", "Open Targets: rare-variant burden tests of the gene link GENE1 to LDL-C.",
               about_genes=["GENE1"], about_traits=[LDL["name"], LDL["id"]],
               data={"gene": "GENE1", "disease": LDL["name"], "disease_id": LDL["id"], "datasource": "gene_burden"},
               group="OT-ASSOC:gene_burden:GENE1")], gene="GENE1", traits=[LDL["id"]])
    return g


def filled(case: Case | None = None, rows=None) -> tuple[ClaimGraph, dict, T.Table]:
    g = bundle_graph(case, rows)
    counts = fill.run(g)
    return g, counts, T.from_graph(g)


def first(table: T.Table, slot: str) -> T.TableClaim:
    return table.claims[table.chains[0].claims[slot]]


def states(claim: T.TableClaim) -> dict[str, str]:
    return {lane: cell.state for lane, cell in claim.cells.items()}


# --- what code states and links ------------------------------------------------------------------------------------------

def test_code_states_a_claim_for_everything_a_record_can_count_for_and_the_table_passes_every_rule():
    g, counts, table = filled()
    assert counts["claims"] == {"binding.allele": 1, "binding.premise": 1, "activity.allele": 0,
                                "activity.premise": 1, "gene.allele": 1, "gene.premise": 1, "trait.allele": 1,
                                "trait.premise": 2}                  # GENE1 and the protein-QTL gene GENE9
    assert T.check(table, g) == []
    assert table.chains[0].title == "G001 (TFX) → GENE1" and (table.chains[0].rank, table.chains[0].ties) == (1, 1)
    assert states(first(table, "binding.allele")) == {"database": "not_checked", "model": "supports",
                                                      "literature": "not_checked"}       # no runner: ADASTRA unasked
    assert states(first(table, "binding.premise")) == {"database": "supports", "model": "no_source",
                                                       "literature": "not_checked"}
    assert states(first(table, "activity.premise"))["database"] == "supports"
    assert states(first(table, "gene.allele"))["database"] == "supports"
    assert states(first(table, "gene.premise"))["database"] == "supports"
    assert states(first(table, "trait.allele"))["database"] == "supports"
    assert states(first(table, "trait.premise")) == {"database": "supports", "model": "supports",
                                                     "literature": "not_checked"}
    assert first(table, "gene.premise").strongest == "edit" and first(table, "binding.premise").strongest == "recorded"
    assert all(c.proposed_by == "code" and c.direction == "unspecified" for c in g.claims.values())
    assert not g.hypotheses and g.model_usage.calls == 0


def test_without_co_factor_reads_code_states_no_claim_that_the_alleles_differ_in_regulatory_activity():
    """The one database source for it is ADASTRA's reads of a protein that does not bind DNA itself. This run never
    asked ADASTRA, so the cell is not checked; no model predicts it."""
    g, counts, table = filled()
    activity = first(table, "activity.allele")
    assert not activity.stated and counts["claims"]["activity.allele"] == 0
    assert states(activity) == {"database": "not_checked", "model": "no_source", "literature": "not_checked"}
    assert not [c for c in g.claims.values() if c.relation == "alters_regulatory_activity"]


def test_every_record_that_names_a_claims_subject_is_counted_listed_beside_or_set_aside():
    g, counts, table = filled()
    assert all(not cell.unjudged for c in table.claims.values() for cell in c.cells.values())
    numbers = T.counts(table, T.check(table, g))
    assert numbers["unjudged"] == 0 and numbers["claims_stated"] == 7 and numbers["claims_supported"] == 7
    assert counts["records_set_aside"] == 0 and counts["records_counted"] >= 9


def test_a_contact_or_a_protein_qtl_is_no_record_about_the_genes_rna():
    g, _, table = filled()
    genes = {g.entities[c.object_ids[0]].label for c in g.claims.values() if c.relation == "associated_with_expression"}
    assert genes == {"GENE1"}                                    # not GENE2 (a contact), not GENE9 (a protein QTL)
    onward = {g.entities[c.subject_ids[0]].label for c in g.claims.values() if c.relation == "contributes_to_trait"}
    assert onward == {"GENE1", "GENE9"}                          # the protein QTL bears on the trait claim only
    titles = [c.title for c in table.chains]
    assert titles == ["G001 (TFX) → GENE1", "G001 (TFX) → GENE9"]
    assert table.chains[1].rank == 2                             # no target gene claim: its weakest link is empty


def test_a_trait_claim_names_the_term_its_source_mapped_the_trait_to():
    g, _, _ = filled()
    traits = {(g.entities[c.object_ids[0]].label, g.entities[c.object_ids[0]].canonical_id)
              for c in g.claims.values() if c.relation == "associated_with_trait"}
    assert traits == {(LDL["name"], LDL["id"])}                  # one term for the Catalog row and the credible set
    trait = next(c for c in g.claims.values() if c.relation == "associated_with_trait")
    assert len(trait.evidence_links) == 2 and trait.assessment == "supported_in_scope"


def test_a_claim_is_assessed_only_where_the_graphs_gate_allows_it():
    g, _, _ = filled()
    by_relation = {c.relation: c.assessment for c in g.claims.values()}
    assert by_relation["overlaps"] == "supported_in_scope"       # a direct record, no context needed
    assert by_relation["alters_binding"] == "unassessed"         # a prediction never settles a claim
    assert by_relation["associated_with_expression"] == "unassessed"   # an eQTL in Liver, a claim with no context


def test_the_result_is_an_answer_although_binding_is_only_predicted():
    g, counts, _ = filled()
    # an answer, and a partial one: no source of code's own compares the alleles' regulatory activity
    assert g.result.outcome == "partial_mechanism" and g.result.stop_reason == "converged"
    assert "No claim: regulatory activity." in g.result.summary
    assert "Leading chain: G001 (TFX) → GENE1." in g.result.summary
    assert "Predicted only: TF binding." in g.result.summary and "no article was read" in g.result.summary
    assert counts["driver"] == fill.DRIVER and (counts["chains"], counts["leaders"]) == (2, 1)
    assert fill.manifest_parts(counts)["driver"] == fill.DRIVER and "driver" not in fill.manifest_parts(counts)["counts"]


def test_a_variant_with_no_record_gets_no_chain_and_says_so():
    g = ClaimGraph(dev_case())
    counts = fill.run(g)
    assert g.result.outcome == "no_supported_explanation" and counts["chains"] == 0 and not g.claims
    table = T.from_graph(g)
    assert len(table.chains) == 1 and not any(c.stated for c in table.claims.values()) and T.check(table, g) == []


def test_a_fill_is_deterministic():
    one, two = bundle_graph(), bundle_graph()
    assert fill.run(one) == fill.run(two) and one.to_json() == two.to_json()


# --- which record goes where ---------------------------------------------------------------------------------------------

def test_a_record_about_another_variant_never_fills_a_claim_that_the_alleles_differ():
    g = bundle_graph()
    code_call(g, "gtex_eqtl", [record("association", "rs999 is an eQTL for GENE5 in Liver.", about_genes=["GENE5"],
                                      about_variants=["rs999"], allele="A", direction="increases", context=LIVER)])
    fill.run(g)
    assert "GENE5" not in {e.label for e in g.entities.values()}


def test_a_record_the_graph_refuses_is_set_aside_with_the_graphs_reason():
    g = bundle_graph()
    bad = code_call(g, "gtex_eqtl", [record("association", "The C allele raises GENE1 in Liver.",
                                            about_genes=["GENE1"], about_variants=CASE, allele="C",
                                            direction="increases", context=LIVER)]).evidence_ids[0]
    counts = fill.run(g)
    table = T.from_graph(g)
    cell = first(table, "gene.allele").cells["database"]
    assert counts["records_set_aside"] == 1 and [s.record for s in cell.set_aside] == [bad]
    assert "neither ref T nor alt G" in cell.set_aside[0].why and T.check(table, g) == []


def test_a_group_whose_models_disagree_gets_both_predictions_each_naming_its_members():
    g = ClaimGraph(dev_case())
    discordant_inventory(g)
    fill.run(g)
    split = next(c for c in g.claims.values() if g.entities[c.object_ids[0]].canonical_id == "G049")
    assert [x.stance for x in split.evidence_links] == ["supports", "supports"]
    assert all("SPI1" in x.rationale for x in split.evidence_links)
    cell = first(T.from_graph(g), "binding.allele").cells["model"]
    assert cell.state == "supports" and len(cell.records) == 2


def test_a_prediction_also_bears_on_another_group_that_shares_one_of_its_tfs():
    rows = [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"}, {"tf": "TFY", "mapping": "cisbp"}]),
            inventory_row(2, True, [{"tf": "TFY", "mapping": "own"}, {"tf": "TFZ", "mapping": "own"}])]
    g = ClaimGraph(dev_case())
    inventory_call(g, rows)
    fill.run(g)
    links = {g.entities[c.object_ids[0]].canonical_id: [x.rationale for x in c.evidence_links]
             for c in g.claims.values()}
    assert len(links["G001"]) == 2 and len(links["G002"]) == 2
    assert any("gate-passing models of group G002, which also cover TFY" in r for r in links["G001"])
    table = T.from_graph(g)
    assert T.check(table, g) == []


def test_a_disease_in_the_request_limits_the_trait_claims_to_the_terms_that_name_it():
    wanted = Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"),
                  supplied_disease=["coronary artery disease"])
    g, counts, table = filled(wanted)
    assert counts["claims"]["trait.allele"] == 0 and counts["claims"]["trait.premise"] == 0
    assert not first(table, "trait.allele").stated
    named = Case(case_id="DEV-1", variant=wanted.variant, supplied_disease=["low density lipoprotein cholesterol"])
    assert filled(named)[1]["claims"]["trait.allele"] == 1


# --- presence, never size -------------------------------------------------------------------------------------------------

def expression(g: ClaimGraph, tf: str, tpm: float, context: ContextScope = HEPG2) -> str:
    return code_call(g, "tf_expression_set", [
        record("expression", f"{tf} is expressed at {tpm:g} TPM in {context.label}.", about_tfs=[tf],
               about_genes=[tf], context=context, data={"tpm": tpm}, group=f"EXPRESSION:{context.label}:{tf}")],
        tfs=[tf]).evidence_ids[0]


def in_hepg2() -> Case:
    return Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"),
                supplied_context=[HEPG2])


def test_expression_counts_at_the_detection_convention_and_a_lower_level_is_evidence_of_nothing():
    g = bundle_graph(in_hepg2())
    level = expression(g, "TFX", 12.5)
    fill.run(g)
    stated = next(c for c in g.claims.values() if c.relation == "expressed_in")
    assert [(x.evidence_id, x.stance) for x in stated.evidence_links] == [(level, "supports")]
    assert stated.assessment == "supported_in_scope" and "12.5 TPM" in stated.evidence_links[0].rationale
    low = bundle_graph(in_hepg2())
    weak = expression(low, "TFX", 0.2)
    fill.run(low)
    claim = next(c for c in low.claims.values() if c.relation == "expressed_in")
    assert [(x.evidence_id, x.stance) for x in claim.evidence_links] == [(weak, "context_only")]
    table = T.from_graph(low)
    beside = [r for r in first(table, "binding.premise").cells["database"].records if r.id == weak]
    assert beside[0].stance == "beside" and "below the 1 TPM convention" in beside[0].note
    assert "no evidence against it" in beside[0].note and T.check(table, low) == []
    assert fill.EXPRESSED_TPM == 1.0


def test_a_peak_in_another_context_than_the_requests_stands_beside_the_claim():
    g = bundle_graph(in_hepg2())
    code_call(g, "tf_occupancy_set", [
        record("occupancy", "ChIP-seq for TFX in K562 (ENCSR2) has a peak containing chr2:60490908.",
               about_tfs=["TFX"], about_elements=[ELEMENT], about_variants=CASE, context=K562, group="CHIP:ENCSR2")],
        tfs=["TFX", "TFW"])
    fill.run(g)
    table = T.from_graph(g)
    records = {r.text.split(" in ")[1].split(" ")[0]: (r.stance, r.note)
               for r in first(table, "binding.premise").cells["database"].records}
    assert records == {"HepG2": ("supports", ""), "K562": ("beside", "from another context")}
    assert T.check(table, g) == []


def test_a_tf_on_record_as_in_place_stands_above_an_equal_one_and_nothing_is_removed():
    """Two groups, both predicted only. One has a ChIP-seq peak: it leads, and the other stays, one rank down, with
    the same kinds of evidence on every link."""
    rows = [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}]), inventory_row(2, True, TFX)]
    g = bundle_graph(rows=rows)
    fill.run(g)
    ranked = chain.chain_view(g)["ranked"]
    first_two = [(r["title"], r["rank"], r["ties"], r["in_place"]) for r in ranked["chains"][:2]]
    assert first_two == [("G002 (TFX) → GENE1", 1, 1, ["occupies"]), ("G001 (TFA) → GENE1", 2, 1, [])]
    assert ranked["chains"][0]["strength"] == ranked["chains"][1]["strength"]
    assert chain.versus_text(ranked["chains"][1], ranked["chains"][0]) == (
        "the same kinds of evidence on every link; no record of a ChIP-seq peak over the variant")
    assert ranked["total"] == 4 and "record shows the factor in place" in ranked["rule"]


def test_presence_breaks_ties_and_never_lifts_a_chain_over_a_stronger_link():
    """A measured binding claim with no peak stays above a predicted one with a peak."""
    rows = [inventory_row(1, True, [{"tf": "TFA", "mapping": "own"}]), inventory_row(2, True, TFX)]
    g = bundle_graph(rows=rows)
    fill.run(g)
    measured = next(c for c in g.claims.values() if g.entities[c.object_ids[0]].canonical_id == "G001")
    read = code_call(g, "literature_read", status="records_found")
    g.tool_calls[read.tool_call_id].read_article = "PMID:1"
    g.tool_calls[read.tool_call_id].article_ids.append("1")
    from .test_chain_table import paper
    emsa = paper(g, "binding_assay", "TFA bound the G probe more strongly than the T probe.", read.tool_call_id,
                 about_tfs=["TFA"], allele="G", direction="increases")
    g.link(measured.claim_id, emsa, "supports", "literature_investigator", "TFA binds the G probe more")
    ranked = chain.chain_view(g)["ranked"]["chains"]
    assert [(r["title"], r["rank"]) for r in ranked[:2]] == [("G001 (TFA) → GENE1", 1), ("G002 (TFX) → GENE1", 2)]
    assert ranked[0]["in_place"] == [] and ranked[1]["in_place"] == ["occupies"]


# --- the lookups ---------------------------------------------------------------------------------------------------------

class Runner:
    """Stands in for the tool runner: records what code asks and returns a call with no records."""

    def __init__(self, names):
        self.names, self.asked = names, []

    def specs(self, route=None):
        return [type("Spec", (), {"name": n})() for n in self.names]

    def run(self, request, case, graph, role, question_id=None):
        self.asked.append((request.tool, dict(request.params), role))
        return code_call(graph, request.tool, **request.params)


def test_code_asks_for_what_its_candidates_need_and_nothing_else():
    g = bundle_graph()
    runner = Runner(["credible_sets_all", "tf_occupancy_set", "tf_expression_set", "gene_disease"])
    fill.Fill(g, runner).lookups()
    asked = {tool: params for tool, params, _ in runner.asked}
    assert [tool for tool, _, _ in runner.asked] == ["credible_sets_all", "tf_occupancy_set", "gene_disease",
                                                     "gene_disease"]
    assert asked["tf_occupancy_set"] == {"tfs": ["TFX"]}             # TFQ has a peak and no gate-passing group
    assert {p["gene"] for t, p, _ in runner.asked if t == "gene_disease"} == {"GENE1", "GENE9"}
    assert asked["gene_disease"]["traits"] == [LDL["id"]]
    assert all(role == "code" for _, _, role in runner.asked)
    assert "tf_expression_set" not in asked                          # no context in the request: nothing to look up


def test_expression_is_looked_up_only_when_the_request_names_a_context():
    g = bundle_graph(in_hepg2())
    runner = Runner(["credible_sets_all", "tf_occupancy_set", "tf_expression_set", "gene_disease"])
    fill.Fill(g, runner).lookups()
    assert ("tf_expression_set", {"tfs": ["TFX"]}, "code") in runner.asked


def test_a_runner_without_the_code_only_tools_is_asked_for_nothing():
    g = bundle_graph()
    runner = Runner(["chip_occupancy", "gtex_eqtl"])
    assert fill.Fill(g, runner).lookups() == [] and runner.asked == []


# --- the graph's batch ---------------------------------------------------------------------------------------------------

def test_a_batch_shares_one_snapshot_and_an_exception_undoes_all_of_it():
    g = bundle_graph()
    before = g.to_json()
    with pytest.raises(RuntimeError), g.batch():
        fill.Fill(g).attach()
        assert g.claims
        raise RuntimeError("stop")
    assert g.to_json() == before and g._depth == 0
    with g.batch():                                  # a refusal caught inside a batch leaves the batch in place
        with pytest.raises(GraphRefusal):
            g.link("C999", "E1", "supports", "code", "no such claim")
        fill.Fill(g).attach()
    assert g.claims and g._depth == 0


# --- the report ----------------------------------------------------------------------------------------------------------

def test_both_reports_show_the_table_and_say_the_run_was_filled_by_code_alone(tmp_path):
    from variant2mechanism.v9 import bundle, report

    from .test_report_support import write_run
    g = bundle_graph()
    counts = fill.run(g)
    run = write_run(g, tmp_path / "run", parts=fill.manifest_parts(counts))
    loaded = bundle.load_bundle(run)
    data = report.report_data(loaded)
    assert data["meta"]["code_only"] is True and data["meta"]["evidence_only"] is False
    assert data["table"]["rows"] == T.first_rows(T.from_graph(g)) and len(data["table"]["rows"]) == 8
    assert data["table"]["rules"] == T.PASSES and data["table"]["stated"] == 7
    markdown = report.render_markdown(loaded)
    assert "## Chain table" in markdown and "The run stated 7 of its 8 claims." in markdown
    assert "| TF binding | The parts are in place | G001 (TFX) | supports: 1 (occupancy) | no source |" in markdown
    assert "(not stated by the run) | not checked | no source | not checked |" in markdown    # regulatory activity
    assert "no model was called, so no hypothesis was proposed" in markdown
    assert "**Partial mechanism**; stopped because converged." in markdown
    assert "Molecular evidence" not in markdown and "Chain completeness" not in markdown     # nothing was compared
    html = report.render_html(loaded)
    assert 'id="table"' in html and "Filled by code alone" in html and '<a href="#table">Chain table</a>' in html
    assert "Whole-hypothesis comparison" not in html.split('id="summary"')[1].split("</section>")[0]


def test_a_run_with_hypotheses_keeps_its_comparison_lines_and_gains_the_table(tmp_path):
    from variant2mechanism.v9 import bundle, report

    from .test_report_support import rich_graph, write_run
    g = rich_graph()
    loaded = bundle.load_bundle(write_run(g, tmp_path / "run"))
    markdown = report.render_markdown(loaded)
    assert "## Chain table" in markdown and report.report_data(loaded)["meta"]["code_only"] is False
    if g.result is not None and g.hypotheses:
        assert "**Molecular evidence:**" in markdown and "Filled by code alone" not in report.render_html(loaded)
