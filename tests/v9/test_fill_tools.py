"""fill_tools.py: the lookups only code makes, in a registry of their own.

A fake provider answers Open Targets; the bulk tools run the adapters' own code on the saved responses of the
development variant rs1427407. Nothing here reaches the network.
"""

import json

import pytest

from variant2mechanism.v9 import adapters, commands, fill_tools, proteins
from variant2mechanism.v9.graph import ClaimGraph
from variant2mechanism.v9.http9 import Http9
from variant2mechanism.v9.schemas import ToolRequest, Variant
from variant2mechanism.v9.tools import REGISTRY, AdapterResult, ToolRunner

from .test_adapters_tools import DEV, FIXTURES, SORT1, Session, case, evidence
from .test_l2g_pagination import page

pytestmark = pytest.mark.data
RELEASE = {"dataVersion": {"year": "26", "month": "09"}, "apiVersion": {"x": "26", "y": "9", "z": "0"}}


def runner(v9_cfg, folder, session=None) -> ToolRunner:
    """A runner on the fill's registry: live on a fake provider, or cache-only."""
    http = (Http9(folder / "http", offline=False, session=session, sleep=lambda s: None) if session is not None
            else Http9.from_config(v9_cfg, offline=True))
    return ToolRunner(config=v9_cfg, mode="live" if session is not None else "cache_only", http=http,
                      run_dir=folder / "run", registry=fill_tools.registry(), clock=lambda: "T0")


def ask(r: ToolRunner, graph: ClaimGraph, tool: str, **params):
    return r.run(ToolRequest(tool=tool, params=params), graph.case, graph, "code")


def associations(rows, count=None):
    return {"data": {"meta": RELEASE, "target": {"id": "ENSG00000134243", "approvedSymbol": "SORT1",
                                                 "associatedDiseases": {"count": len(rows) if count is None else count,
                                                                        "rows": rows}}}}


def row(disease_id: str, name: str, **scores: float) -> dict:
    return {"disease": {"id": disease_id, "name": name}, "score": 0.5,
            "datasourceScores": [{"id": k, "score": v} for k, v in scores.items()]}


# --- the registry --------------------------------------------------------------------------------------------------------

def test_the_code_only_tools_sit_in_a_registry_of_their_own():
    commands.register_tools()
    reg = fill_tools.registry()
    assert set(fill_tools.CODE_TOOL_NAMES) == {"tf_occupancy_set", "tf_expression_set", "credible_sets_all",
                                               "gene_disease", "adastra_asb"}
    assert set(reg.names()) == set(REGISTRY.names()) | set(fill_tools.CODE_TOOL_NAMES)
    assert not set(fill_tools.CODE_TOOL_NAMES) & set(REGISTRY.names())      # what a role is shown does not change
    assert all(reg.spec(n) is REGISTRY.spec(n) and reg.adapter(n) is REGISTRY.adapter(n) for n in REGISTRY.names())
    assert fill_tools.allowed(None) is None
    assert fill_tools.allowed(["gtex_eqtl"]) == ["gtex_eqtl", *fill_tools.CODE_TOOL_NAMES]


def test_the_fills_wiring_knows_the_code_only_tools_and_the_others_do_not(v9_cfg, tmp_path):
    plain = commands.wire(v9_cfg, "cache_only", tmp_path / "a", models=False)
    filling = commands.wire(v9_cfg, "cache_only", tmp_path / "b", models=False, code_tools=True)
    names = {s.name for s in filling.runner.specs("computational")}
    assert set(fill_tools.CODE_TOOL_NAMES) <= names and filling.client is None
    assert not set(fill_tools.CODE_TOOL_NAMES) & {s.name for s in plain.runner.specs()}
    refused = plain.runner.run(ToolRequest(tool="gene_disease", params={"gene": "SORT1"}), case(DEV),
                               ClaimGraph(case(DEV)), "code")
    assert refused.execution_status == "not_applicable" and refused.charged_to == "none"


# --- gene_disease --------------------------------------------------------------------------------------------------------

def test_gene_disease_keeps_the_sources_that_are_a_record_about_the_gene(v9_cfg, tmp_path):
    rows = [row("EFO_0004611", "low density lipoprotein cholesterol measurement", gene_burden=0.9,
                gwas_credible_sets=0.99, europepmc=0.4),
            row("MONDO_0005010", "coronary artery disorder", gwas_credible_sets=0.97, clinical_precedence=0.7),
            row("Orphanet_79211", "Combined hyperlipidemia", impc=0.3, a_new_source=0.2)]
    session = Session(lambda method, url, body: (200, associations(rows)))
    graph = ClaimGraph(case(SORT1))
    call = ask(runner(v9_cfg, tmp_path, session), graph, "gene_disease", gene="sort1",
               traits=["MONDO_0005010", "EFO_0004611", "Orphanet_79211"])
    sent = session.calls[0]["json"]
    assert sent["variables"] == {"id": "ENSG00000134243", "index": 0,
                                 "ids": ["EFO_0004611", "MONDO_0005010", "Orphanet_79211"]}
    assert "enableIndirect: false" in sent["query"] and "includeMeasurements: true" in sent["query"]
    assert call.retrieval_status == "records_found" and call.dataset_release.startswith("Open Targets Platform 26.09")
    found = {(e.data["datasource"], e.evidence_class, e.data["disease_id"]) for e in evidence(graph, call)}
    assert found == {("gene_burden", "association", "EFO_0004611"),
                     ("impc", "statistical_inference", "Orphanet_79211")}
    burden = next(e for e in evidence(graph, call) if e.data["datasource"] == "gene_burden")
    assert burden.about_genes == ["SORT1"] and burden.about_variants == [] and burden.context is None
    assert burden.about_traits == ["low density lipoprotein cholesterol measurement", "EFO_0004611"]
    assert "rare-variant burden tests of the gene link SORT1" in burden.observed_result
    mouse = next(e for e in evidence(graph, call) if e.data["datasource"] == "impc")
    assert mouse.context.species == "mouse" and "in_vivo" not in mouse.data      # a match, not a measurement
    assert any("does not say that this trait was measured" in note for note in mouse.limitations)
    listed = {o["disease_id"]: o for o in call.observations if o["record"] == "association"}
    assert listed["MONDO_0005010"]["used"] == {} and set(listed["MONDO_0005010"]["not_used"]) == {
        "gwas_credible_sets", "clinical_precedence"}
    assert listed["Orphanet_79211"]["not_used"] == {"a_new_source": 0.2}
    assert sum("is listed, never Evidence" in note for note in call.coverage.limitations) == 3


def test_gene_disease_with_only_the_locus_own_signal_finds_nothing_which_is_not_evidence_against(v9_cfg, tmp_path):
    rows = [row("EFO_0004611", "low density lipoprotein cholesterol measurement", gwas_credible_sets=0.99)]
    session = Session(lambda method, url, body: (200, associations(rows)))
    graph = ClaimGraph(case(SORT1))
    call = ask(runner(v9_cfg, tmp_path, session), graph, "gene_disease", gene="SORT1", traits=["EFO_0004611"])
    assert (call.execution_status, call.retrieval_status, call.evidence_ids) == ("success", "no_records_found", [])
    assert "0 records" in call.message and "1 of them have an association of any kind" in call.message


def test_gene_disease_without_traits_lists_and_returns_no_evidence(v9_cfg, tmp_path):
    rows = [row("EFO_0004611", "low density lipoprotein cholesterol measurement", gene_burden=0.9)]
    session = Session(lambda method, url, body: (200, associations(rows, count=422)))
    graph = ClaimGraph(case(SORT1))
    call = ask(runner(v9_cfg, tmp_path, session), graph, "gene_disease", gene="SORT1")
    assert call.retrieval_status == "no_records_found" and not call.evidence_ids and len(session.calls) == 1
    assert session.calls[0]["json"]["variables"]["ids"] is None and "name the traits" in call.message


def test_gene_disease_reads_every_page_and_says_when_it_could_not(v9_cfg, tmp_path):
    def answer(method, url, body):
        index = body["variables"]["index"]
        rows = [row(f"EFO_{index:03d}{i:04d}", f"trait {index}-{i}", gene_burden=0.5)
                for i in range(fill_tools.GENE_PAGE)]
        return 200, associations(rows, count=fill_tools.GENE_PAGE * (fill_tools.GENE_MAX_PAGES + 1))
    session = Session(answer)
    graph = ClaimGraph(case(SORT1))
    call = ask(runner(v9_cfg, tmp_path, session), graph, "gene_disease", gene="SORT1", traits=["EFO_0000001"])
    assert len(session.calls) == fill_tools.GENE_MAX_PAGES and call.retrieval_status == "incomplete"
    assert len(call.evidence_ids) == fill_tools.GENE_PAGE * fill_tools.GENE_MAX_PAGES
    assert any(note.startswith("read ") for note in call.coverage.limitations)


def test_gene_disease_failures_are_statuses_never_no_records(v9_cfg, tmp_path):
    graph = ClaimGraph(case(SORT1))
    unknown = ask(runner(v9_cfg, tmp_path / "a", Session(lambda *a: (200, associations([])))), graph,
                  "gene_disease", gene="NOTAGENE1", traits=["EFO_0004611"])
    assert unknown.execution_status == "not_applicable" and "no Ensembl gene id" in unknown.message
    failed = ask(runner(v9_cfg, tmp_path / "b", Session(lambda *a: (400, {"errors": [{"message": "bad"}]}))),
                 graph, "gene_disease", gene="SORT1", traits=["EFO_0004611"])
    assert failed.execution_status != "success" and failed.retrieval_status != "no_records_found"
    offline = ask(runner(v9_cfg, tmp_path / "c"), ClaimGraph(case(SORT1)), "gene_disease", gene="SORT1",
                  traits=["EFO_0000000"])
    assert offline.execution_status == "cache_miss" and not offline.evidence_ids


# --- credible_sets_all ---------------------------------------------------------------------------------------------------

def test_credible_sets_all_returns_every_sets_records_with_its_mapped_terms(v9_cfg, tmp_path):
    fixture = json.loads((FIXTURES / "ot_credible_sets.json").read_text())["response"]
    session = Session(lambda method, url, body: (200, fixture))
    graph = ClaimGraph(case(SORT1))
    r = runner(v9_cfg, tmp_path, session)
    call = ask(r, graph, "credible_sets_all")
    sets = [o for o in call.observations if o["record"] == "set"]
    assert sets and all(set(o) >= {"study_locus_id", "study_id", "trait", "diseases", "pip"} for o in sets)
    assert call.observations[0]["read"] == len(sets) and call.dataset_release.startswith("Open Targets Platform")
    found = evidence(graph, call)
    assert {e.evidence_class for e in found} == {"statistical_inference", "precomputed_prediction"}
    # the same records the single-trait tool returns for one of those sets: one item in the graph, not two
    one = r.run(ToolRequest(tool="credible_sets_l2g", params={"trait": sets[0]["trait"]}), graph.case, graph, "code")
    assert one.evidence_ids and set(one.evidence_ids) <= set(call.evidence_ids)


def test_credible_sets_all_marks_unread_sets_as_incomplete(v9_cfg, tmp_path):
    session = Session(lambda m, u, b: (200, page(b["variables"]["index"], 100)))
    graph = ClaimGraph(case(DEV))
    call = ask(runner(v9_cfg, tmp_path, session), graph, "credible_sets_all")
    assert call.retrieval_status == "incomplete" and len(session.calls) == adapters.OT_MAX_PAGES
    assert len([o for o in call.observations if o["record"] == "set"]) == call.observations[0]["read"]
    empty = ask(runner(v9_cfg, tmp_path / "b", Session(lambda m, u, b: (200, page(0, 0)))), ClaimGraph(case(DEV)),
                "credible_sets_all")
    assert empty.retrieval_status == "no_records_found" and not empty.evidence_ids


# --- the bulk forms ------------------------------------------------------------------------------------------------------

def test_tf_occupancy_set_is_chip_occupancy_once_per_tf_with_one_raw_result(v9_cfg, tmp_path, monkeypatch):
    seen = []

    def one(params, ctx):
        seen.append((params, ctx.spec.name))
        tf = params["tf"]
        records = [adapters._evidence(evidence_class="occupancy", observed_result=f"a peak of {tf}",
                                      about_tfs=[tf], about_variants=["rs1427407"],
                                      independence_group=f"CHIP:{tf}")] if tf != "TFNONE" else []
        return AdapterResult(retrieval_status="records_found" if records else "no_records_found", evidence=records,
                             raw={"peaks": ["the same for every TF"], "query": {"tf": tf}}, cached=True,
                             retrieval_time="2026-01-01T00:00:00+00:00")
    monkeypatch.setattr(adapters, "chip_occupancy", one)
    graph = ClaimGraph(case(DEV))
    call = ask(runner(v9_cfg, tmp_path), graph, "tf_occupancy_set", tfs=["tfb", "TFA", "TFNONE"])
    assert seen == [({"tf": "TFA"}, "chip_occupancy"), ({"tf": "TFB"}, "chip_occupancy"),
                    ({"tf": "TFNONE"}, "chip_occupancy")]
    assert call.retrieval_status == "records_found" and len(call.evidence_ids) == 2 and call.cached
    assert [(o["tf"], o["experiments"]) for o in call.observations] == [("TFA", 1), ("TFB", 1), ("TFNONE", 0)]
    raw = json.loads((tmp_path / "run" / call.raw_result_path).read_text())
    assert raw == {"peaks": ["the same for every TF"], "query": {"tfs": ["TFA", "TFB", "TFNONE"]}}
    missing = ask(runner(v9_cfg, tmp_path / "x"), ClaimGraph(case(DEV)), "tf_occupancy_set")
    assert missing.execution_status == "not_applicable"            # a list of TFs is required


def test_a_failed_source_fails_the_whole_bulk_call(v9_cfg, tmp_path, monkeypatch):
    monkeypatch.setattr(adapters, "chip_occupancy", lambda params, ctx: AdapterResult(
        execution_status="cache_miss", message="ENCODE/Factorbook: not in the HTTP cache"))
    call = ask(runner(v9_cfg, tmp_path), ClaimGraph(case(DEV)), "tf_occupancy_set", tfs=["TFA"])
    assert call.execution_status == "cache_miss" and not call.evidence_ids


def test_tf_expression_set_returns_the_levels_tf_expression_returns(v9_cfg, tmp_path):
    graph = ClaimGraph(case(DEV))
    r = runner(v9_cfg, tmp_path)
    call = ask(r, graph, "tf_expression_set", tfs=["GATA1", "TAL1"], context="K562")
    levels = {e.about_tfs[0]: e for e in evidence(graph, call)}
    assert set(levels) == {"GATA1", "TAL1"} and all(e.evidence_class == "expression" for e in levels.values())
    assert all(isinstance(e.data["tpm"], float) for e in levels.values())           # a level, no threshold call
    single = r.run(ToolRequest(tool="tf_expression", params={"tf": "GATA1", "context": "K562"}), graph.case, graph,
                   "code")
    assert single.evidence_ids == [levels["GATA1"].evidence_id]                     # one record, whichever tool
    none = ask(r, graph, "tf_expression_set", tfs=["GATA1"])
    assert none.retrieval_status == "no_records_found"                              # no context: nothing to say


# --- adastra_asb ---------------------------------------------------------------------------------------------------------

def asb(name: str, accession: str, ref: float, alt: float, motif: str | None = "Concordant", **more) -> dict:
    """One TF's pooled call as ADASTRA returns it: -log10 FDR for each allele."""
    return {"transcription_factor": {"name": name, "uniprot_ac": accession, "experiments_count": 12},
            "log_p_value_ref": ref, "log_p_value_alt": alt, "es_ref": 1.5, "es_alt": -0.4,
            "is_asb": max(ref, alt) >= 1.30103, "motif_concordance": motif, **more}


def entry(variant=DEV, alt=None, tfs=(), cells=()) -> dict:
    return {"chromosome": f"chr{variant.chrom}", "position": variant.pos, "ref": variant.ref,
            "alt": alt or variant.alt, "rs_id": 1427407, "tf_aggregated_snps": list(tfs),
            "cl_aggregated_snps": [{"cell_line": {"name": c}, "is_asb": True, "log_p_value_ref": 2.0,
                                    "log_p_value_alt": 0.0} for c in cells]}


def adastra(results, status=200) -> Session:
    def answer(method, url, body):
        assert url == (f"{fill_tools.ADASTRA_API}/search/snps/advanced?chromosome=chr{DEV.chrom}"
                       f"&start={DEV.pos}&end={DEV.pos}")
        return status, {"total": len(results), "results": results}
    return Session(answer)


def test_adastra_gives_one_record_per_tf_that_favours_an_allele_and_lists_the_rest(v9_cfg, tmp_path):
    found = entry(tfs=[asb("ANDR_HUMAN", "P10275", 3.4, 0.0),                  # AR prefers the reference allele
                       asb("FOXA1_HUMAN", "P55317", 0.0, 1.6, motif="No Hit"),  # FOXA1 the other, with no motif
                       asb("TLE3_HUMAN", "Q04726", 0.6, 0.0, motif=None),       # tested, not significant
                       asb("BRD4_HUMAN", "O60885", 0.0, 2.1, motif=None),       # passes, and is not a TF
                       asb("NOSUCH_HUMAN", "X00000", 2.0, 0.0)],                # passes, and HGNC does not know it
                  cells=["22RV1 (prostate carcinoma)"])
    graph = ClaimGraph(case(DEV))
    call = ask(runner(v9_cfg, tmp_path, adastra([found, entry(alt="C", tfs=[asb("ANDR_HUMAN", "P10275", 5.0, 0.0)])])),
               graph, "adastra_asb")
    assert (call.execution_status, call.retrieval_status) == ("success", "records_found")
    assert call.dataset_release == fill_tools.ADASTRA_RELEASE and call.message == "3 of 5 proteins tested favour one allele"
    ar, foxa1, brd4 = evidence(graph, call)
    assert (ar.evidence_class, ar.origin, ar.about_tfs, ar.allele, ar.direction) == (
        "occupancy", "tool", ["AR"], "T", "increases")
    assert ar.data["allele_specific"] is True and ar.data["fdr_ref"] == pytest.approx(10 ** -3.4)
    assert "favour the T allele over G" in ar.observed_result and len(ar.limitations) == 2
    assert any("another variant on the same haplotype" in x for x in ar.limitations)
    assert (foxa1.about_tfs, foxa1.allele) == (["FOXA1"], "G")
    assert any("no motif of this TF over the variant" in x for x in foxa1.limitations)
    # a TF stays a record about its binding whatever the motif column says; a protein that does not bind DNA itself
    # is flagged, and says what its reads can and cannot show
    assert [(e.data["protein"], e.data[proteins.COFACTOR_FLAG]) for e in (ar, foxa1, brd4)] == [
        ("tf", False), ("tf", False), ("not_tf", True)]
    assert "BRD4, which does not bind DNA itself," in brd4.observed_result and "motif" not in brd4.observed_result
    assert any("names no TF that reads the variant" in x for x in brd4.limitations)
    assert not any("no motif of this TF" in x for x in brd4.limitations)
    rows = {o["adastra_tf"]: o for o in call.observations if o["record"] == "tf"}
    assert [rows[k]["evidence"] for k in ("ANDR_HUMAN", "FOXA1_HUMAN", "TLE3_HUMAN", "NOSUCH_HUMAN")] == [
        True, True, False, False]
    assert (rows["BRD4_HUMAN"]["protein"], rows["NOSUCH_HUMAN"]["protein"]) == ("not_tf", "unknown")
    assert rows["TLE3_HUMAN"]["passes_fdr"] is False and rows["NOSUCH_HUMAN"]["tf"] is None
    assert [o["alt"] for o in call.observations if o["record"] == "other_allele"] == ["C"]     # never this variant's
    assert any("no single HGNC symbol" in x for x in call.coverage.limitations)
    assert any("not evidence that the alleles bind alike" in x for x in call.coverage.limitations)


def test_adastra_with_no_entry_or_no_tf_past_the_threshold_finds_nothing_and_a_failure_is_a_failure(v9_cfg, tmp_path):
    for label, results in (("a", []), ("b", [entry(tfs=[asb("ANDR_HUMAN", "P10275", 0.8, 0.0)])]),
                           ("c", [entry(alt="C", tfs=[asb("ANDR_HUMAN", "P10275", 5.0, 0.0)])])):
        graph = ClaimGraph(case(DEV))
        call = ask(runner(v9_cfg, tmp_path / label, adastra(results)), graph, "adastra_asb")
        assert (call.execution_status, call.retrieval_status, call.evidence_ids) == ("success", "no_records_found", [])
    graph = ClaimGraph(case(DEV))
    call = ask(runner(v9_cfg, tmp_path / "d", adastra([], status=503)), graph, "adastra_asb")
    assert call.execution_status != "success" and call.evidence_ids == []
    # cache-only with nothing saved is a miss. One base from the development variant, which no run asks about: a
    # live run on rs1427407 saves ADASTRA's answer for its position in the cache the tests can read.
    graph = ClaimGraph(case(Variant(chrom="2", pos=60490909, ref="T", alt="G")))
    call = ask(runner(v9_cfg, tmp_path / "e"), graph, "adastra_asb")
    assert call.execution_status == "cache_miss" and call.evidence_ids == []


def test_an_adastra_record_counts_as_a_measurement_for_the_tfs_own_claim(v9_cfg, tmp_path):
    from variant2mechanism.v9 import fill
    from variant2mechanism.v9 import table as T
    graph = ClaimGraph(case(DEV))
    call = ask(runner(v9_cfg, tmp_path, adastra([entry(tfs=[asb("ANDR_HUMAN", "P10275", 3.4, 0.0)])])), graph,
               "adastra_asb")
    (record,) = evidence(graph, call)
    assert T.can_count(T.SLOTS["binding.allele"], record) and T.lane_of(record) == "database"
    fill.run(graph)
    claim = next(c for c in graph.claims.values() if c.relation == "alters_binding")
    assert claim.assertion_text == "The two alleles of rs1427407 differ in binding AR."
    (link,) = claim.evidence_links
    assert (link.evidence_id, link.stance, link.strength) == (record.evidence_id, "supports", "direct")
    assert link.rationale == "ADASTRA: ChIP-seq reads of AR over the variant favour the T allele"
    table = T.from_graph(graph)
    from .test_fill import first
    assert table.chains[0].title.startswith("AR")
    cell = first(table, "binding.allele").cells["database"]
    assert cell.state == "supports" and [(r.kind, r.tool) for r in cell.records] == [("assay", "adastra_asb")]
    assert cell.lookups == [call.tool_call_id] and T.check(table, graph) == []


def test_reads_of_a_protein_that_does_not_bind_dna_count_for_the_sites_activity_and_name_no_tf(v9_cfg, tmp_path):
    """BRD4 reads acetylated histones. Reads of it that favour one allele show that the site's state differs between
    the alleles: the record fills the database cell of that claim, and BRD4 enters no chain as a TF."""
    from variant2mechanism.v9 import fill
    from variant2mechanism.v9 import table as T

    from .test_fill import first
    graph = ClaimGraph(case(DEV))
    call = ask(runner(v9_cfg, tmp_path, adastra([entry(tfs=[asb("BRD4_HUMAN", "O60885", 0.0, 2.1, motif=None),
                                                            asb("ANDR_HUMAN", "P10275", 3.4, 0.0)])])),
               graph, "adastra_asb")
    brd4, ar = evidence(graph, call)
    assert T.listed("activity.allele", "database", "adastra_asb", brd4)
    assert not T.listed("binding.allele", "database", "adastra_asb", brd4)
    assert T.listed("binding.allele", "database", "adastra_asb", ar)
    assert not T.listed("activity.allele", "database", "adastra_asb", ar)
    assert T.can_count(T.SLOTS["activity.allele"], brd4) and not T.can_count(T.SLOTS["activity.allele"], ar)
    fill.run(graph)
    binding = [c for c in graph.claims.values() if c.relation == "alters_binding"]
    assert [c.assertion_text for c in binding] == ["The two alleles of rs1427407 differ in binding AR."]
    (activity,) = [c for c in graph.claims.values() if c.relation == "alters_regulatory_activity"]
    assert activity.assertion_text.startswith("The two alleles of rs1427407 differ in the regulatory activity of ")
    (link,) = activity.evidence_links
    assert (link.evidence_id, link.stance, link.strength) == (brd4.evidence_id, "supports", "direct")
    assert link.rationale == ("ADASTRA: ChIP-seq reads of BRD4, which does not bind DNA itself, favour the G allele "
                              "over the variant: the site's state differs between the alleles")
    table = T.from_graph(graph)
    assert [chain.title.split(" → ")[0] for chain in table.chains] == ["AR"]
    cell = first(table, "activity.allele").cells["database"]
    assert cell.state == "supports" and [(r.kind, r.tool) for r in cell.records] == [("assay", "adastra_asb")]
    assert first(table, "binding.allele").cells["database"].state == "supports" and T.check(table, graph) == []


def test_a_record_made_before_proteins_were_sorted_stays_a_record_about_binding():
    from types import SimpleNamespace as Filed

    from variant2mechanism.v9 import table as T
    old = Filed(evidence_class="occupancy", about_tfs=["BRD4"], about_genes=[], about_elements=[], about_traits=[],
                data={"allele_specific": True})
    assert T.listed("binding.allele", "database", "adastra_asb", old)
    assert not T.listed("activity.allele", "database", "adastra_asb", old)
