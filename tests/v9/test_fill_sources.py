"""fill_sources.py: the sources added in the second version of the fill, and what the fill and the reader do with them.

Fake providers answer every request; names, numbers and observations are stipulated for the tests on the development
variant rs1427407 (chr2:60490908 T>G), not claims about it. Nothing here reaches the network or a model.
"""

from pathlib import Path

import pytest

from variant2mechanism.v9 import fill, fill_tools, proteins, reader
from variant2mechanism.v9 import fill_sources as S
from variant2mechanism.v9 import literature as lit
from variant2mechanism.v9 import roles as R
from variant2mechanism.v9 import table as T
from variant2mechanism.v9.context_match import scope_from_label
from variant2mechanism.v9.graph import ClaimGraph, SymbolResolver, greek_key
from variant2mechanism.v9.http9 import Http9
from variant2mechanism.v9.schemas import QUALIFIED_DIRECT_FILL, ToolRequest, evidence_strength
from variant2mechanism.v9.tools import ToolLimits, ToolRunner

from . import test_literature_fakes as fakes
from .test_adapters_tools import DEV, Session, case, evidence
from .test_fill import CASE, ELEMENT, bundle_graph, code_call, first
from .test_reader import RSID, VARIANTS, Model, experiment, read_records, reading

SHORT, SHORT_PMID = "PMC9000009", "90000009"              # the synthetic article that never writes the rsID
NAMED, NAMED_PMID = "PMC9000010", "90000010"              # one that writes two mutations by their own names only
HGVS = "NC_000002.12:g.60490908T>G"
RELEASE = {"dataVersion": {"year": "26", "month": "09"}, "apiVersion": {"x": "26", "y": "9", "z": "0"}}


def live(folder: Path, session: Session, cfg=None) -> ToolRunner:
    """A runner on the fill's registry, live on a fake provider."""
    http = Http9(folder / "http", offline=False, session=session, sleep=lambda s: None)
    return ToolRunner(config=cfg, mode="live", http=http, run_dir=folder / "run", registry=fill_tools.registry(),
                      clock=lambda: "T0")


def ask(r: ToolRunner, graph: ClaimGraph, tool: str, **params):
    return r.run(ToolRequest(tool=tool, params=params), graph.case, graph, "code")


def by_url(routes: dict) -> Session:
    """A fake provider that answers each URL from a table and anything else with 404."""
    def answer(method, url, body):
        return routes.get(url, (404, {"detail": "not found"}))
    return Session(answer)


# --- udacha_asa -----------------------------------------------------------------------------------------------------

def cell(name: str, ref: float, alt: float) -> dict:
    """One cell type's pooled call as UDACHA returns it: -log10 FDR for each allele; its own flag is set at 10%."""
    return {"cell_line": {"cl_id": len(name), "name": name, "experiments_count": 3}, "log_p_value_ref": ref,
            "log_p_value_alt": alt, "es_ref": -1.0, "es_alt": 1.5, "is_asb": max(ref, alt) >= 1.0}


def udacha_entry(alt: str | None = None, dnase=(), atac=()) -> dict:
    return {"chromosome": f"chr{DEV.chrom}", "position": DEV.pos, "ref": DEV.ref, "alt": alt or DEV.alt,
            "rs_id": 1427407, "dnase_aggregated_snps": list(dnase), "atac_aggregated_snps": list(atac),
            "faire_aggregated_snps": []}


def udacha(results, status: int = 200) -> Session:
    url = f"{S.UDACHA_API}/search/snps/advanced?chromosome=chr{DEV.chrom}&start={DEV.pos}&end={DEV.pos}"
    return by_url({url: (status, {"total": len(results), "results": results})})


def test_udacha_gives_one_record_per_cell_type_past_five_percent_and_lists_the_rest(tmp_path):
    found = udacha_entry(dnase=[cell("liver", 0.0, 7.1),          # the alternate allele is the open one
                                cell("K562", 2.0, 0.0),           # the reference allele, in another cell type
                                cell("stomach", 0.0, 1.2)],       # past UDACHA's own 10%, not past 5%
                         atac=[cell("pancreatic islets", 0.0, 3.4)])
    graph = ClaimGraph(case(DEV))
    call = ask(live(tmp_path, udacha([found, udacha_entry(alt="C", dnase=[cell("liver", 9.0, 0.0)])])), graph,
               "udacha_asa")
    assert (call.execution_status, call.retrieval_status) == ("success", "records_found")
    assert call.message == "3 of 4 cell type and assay pairs favour one allele"
    liver, k562, islets = evidence(graph, call)
    assert (liver.evidence_class, liver.origin, liver.allele, liver.direction, liver.about_tfs) == (
        "occupancy", "tool", "G", "increases", [])
    assert liver.data[proteins.ACCESSIBILITY_FLAG] is True and liver.data["assay"] == "DNase-seq"
    assert liver.data["fdr_alt"] == pytest.approx(10 ** -7.1) and liver.context.label == "liver"
    assert "DNase-seq reads over chr2:60490908 T>G in liver favour the G allele over T" in liver.observed_result
    assert (k562.allele, islets.data["assay"]) == ("T", "ATAC-seq")
    assert any("another variant on the same haplotype" in x for x in liver.limitations)
    assert any("name no protein" in x for x in liver.limitations)
    rows = {o["cell_type"]: o for o in call.observations if o["record"] == "cell_type"}
    assert (rows["stomach"]["passes_fdr_5"], rows["stomach"]["passes_fdr_10"], rows["stomach"]["evidence"]) == (
        False, True, False)
    assert [o["alt"] for o in call.observations if o["record"] == "other_allele"] == ["C"]     # never this variant's
    assert any("not evidence that the alleles are alike" in x for x in call.coverage.limitations)


def test_udacha_with_no_entry_finds_nothing_and_a_failure_is_a_failure(tmp_path):
    for label, results in (("a", []), ("b", [udacha_entry(dnase=[cell("stomach", 0.0, 1.2)])]),
                           ("c", [udacha_entry(alt="C", dnase=[cell("liver", 9.0, 0.0)])])):
        graph = ClaimGraph(case(DEV))
        call = ask(live(tmp_path / label, udacha(results)), graph, "udacha_asa")
        assert (call.execution_status, call.retrieval_status, call.evidence_ids) == ("success", "no_records_found", [])
    graph = ClaimGraph(case(DEV))
    call = ask(live(tmp_path / "d", udacha([], status=503)), graph, "udacha_asa")
    assert call.execution_status != "success" and call.evidence_ids == []


def test_reads_of_open_chromatin_count_for_the_sites_activity_and_for_no_tf():
    record = S.udacha_evidence(DEV, cell("liver", 0.0, 7.1), "DNase-seq", CASE)
    assert proteins.ACCESSIBILITY_FLAG in QUALIFIED_DIRECT_FILL[("alters_regulatory_activity", "occupancy")]
    assert evidence_strength("alters_regulatory_activity", record) == "direct"
    assert T.listed("activity.allele", "database", "udacha_asa", record)
    assert not T.listed("binding.allele", "database", "udacha_asa", record)     # the map offers it to no TF's claim
    assert S.udacha_evidence(DEV, cell("stomach", 0.0, 1.2), "DNase-seq", CASE) is None
    both = S.udacha_evidence(DEV, cell("mixed", 2.0, 2.0), "ATAC-seq", CASE)
    assert (both.allele, both.direction) == (None, "unspecified")
    g = bundle_graph()
    call = code_call(g, "udacha_asa", [record, S.udacha_evidence(DEV, cell("K562", 2.0, 0.0), "ATAC-seq", CASE)])
    counts = fill.run(g)
    assert counts["claims"]["activity.allele"] == 1
    claim = next(c for c in g.claims.values() if c.relation == "alters_regulatory_activity")
    assert claim.assertion_text == f"The two alleles of rs1427407 differ in the regulatory activity of {ELEMENT}."
    assert [(x.stance, x.strength) for x in claim.evidence_links] == [("supports", "direct")] * 2
    assert claim.evidence_links[0].rationale == ("UDACHA: DNase-seq reads over the variant in liver favour the G "
                                                 "allele: the site's state differs between the alleles")
    table = T.from_graph(g)
    cell_ = first(table, "activity.allele").cells["database"]
    assert cell_.state == "supports" and {(r.kind, r.tool) for r in cell_.records} == {("assay", "udacha_asa")}
    assert cell_.lookups == [call.tool_call_id] and first(table, "activity.allele").strongest == "assay"
    assert not any(c.relation == "alters_binding" and "liver" in str(c.assertion_text) for c in g.claims.values())
    assert T.check(table, g) == []


# --- mavedb_reporter ------------------------------------------------------------------------------------------------

def measurement(n: int, set_urn: str, **more) -> dict:
    return {"variantUrn": f"{set_urn}#{n}", "score": -2.0, "assayLevel": "genomic", "relationship": "direct",
            "assayLevelHgvs": HGVS, "scoreSetUrn": set_urn, "scoreSetTitle": f"MPRA {set_urn}", "isCurrent": True,
            **more}


def score_set(urn: str, category: str = "regulatory", cells: str = "HepG2") -> dict:
    return {"urn": urn, "title": f"Saturation mutagenesis MPRA of an invented enhancer, {urn[-3:]}",
            "shortDescription": f"Saturation mutagenesis MPRA of an invented enhancer in {cells} cells.",
            "targetGenes": [{"name": "invented enhancer", "category": category}],
            "primaryPublicationIdentifiers": [{"identifier": "90000031", "dbName": "PubMed"}],
            "license": {"shortName": "CC0"}}


def detail(score: float, p: float, tags: float | None = 40.0) -> dict:
    scores = {"score": score, "p-value": p, **({} if tags is None else {"unique_tags": tags})}
    return {"scores": scores, "mapped": {"genomic": {"hgvs": HGVS}}}


def mavedb(measurements: list[dict], details: dict[str, dict], sets: dict[str, dict], caid: str = "CA1") -> Session:
    routes = {f"{S.CLINGEN_API}?hgvs={S.quote(HGVS, safe='')}": (200, {"@id": f"http://reg.genome.network/allele/{caid}"}),
              f"{S.MAVEDB_API}/clingen-alleles/{caid}/measurements": (200, measurements)}
    routes.update({f"{S.MAVEDB_API}/variants/{S.quote(urn, safe=':')}": (200, d) for urn, d in details.items()})
    routes.update({f"{S.MAVEDB_API}/score-sets/{urn}": (200, s) for urn, s in sets.items()})
    return by_url(routes)


def test_mavedb_counts_a_measurement_past_the_studys_level_and_lists_the_others(tmp_path):
    a, b, c, d = (f"urn:mavedb:00000099-a-{i}" for i in (1, 2, 3, 4))
    protein = "urn:mavedb:00000098-a-1"
    listed = [measurement(1, a), measurement(2, b), measurement(3, c), measurement(4, d), measurement(5, protein),
              measurement(6, a, relationship="equivalent"), measurement(7, a, assayLevelHgvs="NC_000002.12:g.5A>C")]
    details = {f"{a}#1": detail(-2.9, 0.0), f"{b}#2": detail(-0.4, 3e-3), f"{c}#3": detail(-2.7, 0.0, tags=9.0),
               f"{d}#4": detail(1.8, 2e-9, tags=None), f"{protein}#5": detail(-1.0, 0.0)}
    sets = {a: score_set(a), b: score_set(b), c: score_set(c), d: score_set(d, cells="GBM"),
            protein: score_set(protein, category="protein_coding")}
    graph = ClaimGraph(case(DEV))
    call = ask(live(tmp_path, mavedb(listed, details, sets)), graph, "mavedb_reporter")
    assert (call.execution_status, call.retrieval_status) == ("success", "records_found")
    assert call.message == "2 of 5 measurement(s) read pass the study's level"
    one, four = evidence(graph, call)
    assert (one.evidence_class, one.origin, one.allele, one.direction) == ("reporter_assay", "tool", None, "unspecified")
    assert one.source_ids == [f"MaveDB:{a}#1", "PMID:90000031"] and one.context.label == "HepG2"
    assert (one.data["score"], one.data["p_value"], one.data["unique_tags"]) == (-2.9, 0.0, 40.0)
    assert "log2 effect of -2.90 on reporter activity (p below the smallest number the set stores; 40 barcodes)" \
        in one.observed_result
    assert one.independence_group == four.independence_group == "MaveDB:urn:mavedb:00000099"   # one experiment
    assert any("no direction is read from it" in x for x in one.limitations)
    assert four.context is not None and "p 2.0e-09)" in four.observed_result and four.data["unique_tags"] is None
    why = {o["variant_urn"]: o["why"] for o in call.observations if o["record"] == "measurement"}
    assert "not below the study's significance level" in why[f"{b}#2"]
    assert "fewer than the 10 the study needs" in why[f"{c}#3"]
    assert why[f"{protein}#5"] == "the score set is not of a regulatory element"
    assert evidence_strength("alters_regulatory_activity", one) == "direct"
    assert T.listed("activity.allele", "database", "mavedb_reporter", one)


def test_mavedb_without_an_allele_id_or_a_measurement_finds_nothing(tmp_path):
    graph = ClaimGraph(case(DEV))
    none = by_url({f"{S.CLINGEN_API}?hgvs={S.quote(HGVS, safe='')}": (200, {"@id": "_:CA"})})
    call = ask(live(tmp_path / "a", none), graph, "mavedb_reporter")
    assert (call.execution_status, call.retrieval_status, call.evidence_ids) == ("success", "no_records_found", [])
    assert "no ClinGen allele identifier" in call.message
    graph = ClaimGraph(case(DEV))
    call = ask(live(tmp_path / "b", mavedb([], {}, {})), graph, "mavedb_reporter")
    assert (call.execution_status, call.retrieval_status, call.evidence_ids) == ("success", "no_records_found", [])
    assert S.hgvs_g(DEV) == HGVS and S.hgvs_g(DEV.model_copy(update={"chrom": "MT"})) is None


def test_a_reporter_measurement_fills_the_database_cell_of_regulatory_activity():
    a = "urn:mavedb:00000099-a-1"
    record, why = S.mavedb_evidence(DEV, measurement(1, a), detail(-2.9, 0.0), score_set(a), "CA1", CASE)
    assert why == ""
    g = bundle_graph()
    code_call(g, "mavedb_reporter", [record])
    fill.run(g)
    claim = next(c for c in g.claims.values() if c.relation == "alters_regulatory_activity")
    (link,) = claim.evidence_links
    assert (link.stance, link.strength) == ("supports", "direct") and "MaveDB" in link.rationale
    table = T.from_graph(g)
    cell_ = first(table, "activity.allele").cells["database"]
    assert cell_.state == "supports" and [(r.kind, r.tool) for r in cell_.records] == [("assay", "mavedb_reporter")]
    assert T.check(table, g) == []


# --- protein_qtl_sets -----------------------------------------------------------------------------------------------

def pqtl_row(n: int, symbol: str, trans: bool | None, biosample: str | None = "blood plasma", pip: float = 0.9) -> dict:
    return {"studyLocusId": f"SL{n}", "studyId": f"STUDY_{symbol}", "isTransQtl": trans, "finemappingMethod": "SuSiE-inf",
            "confidence": "fine-mapped", "variant": {"id": "2_60490000_A_G"},
            "study": {"id": f"STUDY_{symbol}", "projectId": "UKB_PPP_EUR", "traitFromSource": symbol, "nSamples": 30000,
                      "pubmedId": None, "target": {"id": None, "approvedSymbol": symbol},
                      "biosample": {"biosampleName": biosample} if biosample else None},
            "locus": {"rows": [{"variant": {"id": "2_60490908_T_G"}, "posteriorProbability": pip,
                                "is95CredibleSet": True, "is99CredibleSet": True, "beta": 0.2}]}}


@pytest.mark.data
def test_a_cis_protein_qtl_is_a_record_about_the_gene_and_a_trans_one_is_listed(v9_cfg, tmp_path):
    rows = [pqtl_row(1, "BCL11A", False), pqtl_row(2, "APOB", True), pqtl_row(3, "PAPOLG", False, biosample=None),
            pqtl_row(4, "REL", None)]

    def answer(method, url, body):
        assert "studyTypes: [pqtl]" in body["query"] and body["variables"]["v"] == "2_60490908_T_G"
        return 200, {"data": {"meta": RELEASE, "variant": {"id": "2_60490908_T_G",
                                                            "credibleSets": {"count": len(rows), "rows": rows}}}}
    graph = ClaimGraph(case(DEV))
    call = ask(live(tmp_path, Session(answer), v9_cfg), graph, "protein_qtl_sets")
    assert (call.execution_status, call.retrieval_status) == ("success", "records_found")
    assert call.message == "1 cis and 1 trans protein-QTL credible set(s) hold the variant"
    (record,) = evidence(graph, call)
    assert (record.evidence_class, record.about_genes, record.about_traits) == ("statistical_inference", ["BCL11A"], [])
    assert (record.data["qtl_type"], record.data["cis"], record.data["pip"]) == ("pqtl", True, 0.9)
    assert record.context.label == "blood plasma" and "posterior inclusion probability 0.9" in record.observed_result
    assert any("not the tissue where the variant acts" in x for x in record.limitations)
    kept = {o["protein_of"]: o["evidence"] for o in call.observations if o["record"] == "set"}
    assert kept == {"BCL11A": True, "APOB": False, "PAPOLG": False, "REL": False}   # trans, no biosample, no call
    assert T.listed("gene.allele", "database", "protein_qtl_sets", record)
    assert not T.listed("trait.allele", "database", "protein_qtl_sets", record)


def test_a_cis_protein_qtl_states_a_claim_about_the_protein_where_it_was_measured():
    record = S.pqtl_evidence(pqtl_row(1, "GENE7", False), "2_60490908_T_G", "the release", "GENE7", DEV, CASE)
    g = bundle_graph()
    code_call(g, "protein_qtl_sets", [record])
    counts = fill.run(g)
    assert counts["claims"]["gene.allele"] == 2                       # GENE1's RNA, and GENE7's protein
    claim = next(c for c in g.claims.values() if "level of the" in c.assertion_text)
    assert claim.assertion_text == ("The two alleles of rs1427407 differ in the level of the GENE7 protein in blood "
                                    "plasma.")
    # counted as an association and left unassessed: plasma is not where the variant acts, and a settled claim would
    # decide which chain of a tie is listed first
    assert (claim.relation, claim.context_scope.label, claim.assessment) == (
        "associated_with_expression", "blood plasma", "unassessed")
    (link,) = claim.evidence_links
    assert (link.stance, link.strength, link.applicability) == ("supports", "direct", "exact")
    table = T.from_graph(g)
    gene7 = next(c for c in table.claims.values() if c.step == "gene" and c.part == "allele" and c.names["genes"] == ["GENE7"])
    assert gene7.text == "The two alleles differ in the gene's RNA or protein." and gene7.strongest == "association"
    assert [r.tool for r in gene7.cells["database"].records] == ["protein_qtl_sets"]
    assert any(ch.title.endswith("GENE7") for ch in table.chains)     # the gene is a candidate of a chain
    assert T.check(table, g) == []


# --- tumour_recurrence ----------------------------------------------------------------------------------------------

def annotated(graph: ClaimGraph, gene: str = "TERT") -> None:
    """The annotation's GRCh37 placement of the case variant and the gene it names."""
    v = graph.case.variant
    code_call(graph, "variant_annotation", observations=[
        {"record": "variant_mapping", "assembly": "GRCh37", "chrom": v.chrom, "pos": v.pos + 77, "ref": v.ref,
         "alt": v.alt, "case_key": v.key, "case_strand_flip": False, "rsid": v.rsid, "source": "test"},
        {"record": "consequence", "gene": gene, "consequences": ["upstream_gene_variant"]}], status="records_found")


def mutation(patient: str, pos: int, alt: str = DEV.alt, sample: int = 1) -> dict:
    return {"sampleId": f"{patient}-T0{sample}", "patientId": patient, "chr": DEV.chrom, "startPosition": pos,
            "endPosition": pos, "referenceAllele": DEV.ref, "variantAllele": alt, "mutationType": "5'Flank",
            "proteinChange": "Promoter"}


def cohort(mutations: list[dict], types: dict[str, str], gene_id: int = 7015) -> Session:
    study = S.CBIO_STUDY
    clinical = [{"sampleId": f"{p}-T0{n}", "patientId": p, "value": t} for p, t in types.items() for n in (1, 2)]
    return by_url({
        f"{S.CBIO_API}/molecular-profiles/{study}_mutations/mutations?sampleListId={study}_all"
        f"&entrezGeneId={gene_id}&projection=SUMMARY": (200, mutations),
        f"{S.CBIO_API}/studies/{study}/clinical-data?clinicalDataType=SAMPLE&attributeId=CANCER_TYPE"
        "&projection=SUMMARY": (200, clinical)})


@pytest.mark.data
def test_tumours_are_counted_by_patient_and_cancer_type_and_one_patient_is_not_recurrence(v9_cfg, tmp_path):
    pos = DEV.pos + 77
    types = {"P1": "Glioma", "P2": "Glioma", "P3": "Glioma", "P4": "Melanoma", "P5": "Melanoma", "P6": "Bladder Cancer"}
    calls = [mutation("P1", pos), mutation("P1", pos, sample=2),      # two samples of one patient: one patient
             mutation("P2", pos), mutation("P4", pos),                # Melanoma: one patient only
             mutation("P3", pos, alt="A"), mutation("P5", pos + 3)]   # another allele, another position
    graph = ClaimGraph(case(DEV, origin="somatic"))
    annotated(graph)
    call = ask(live(tmp_path, cohort(calls, types), v9_cfg), graph, "tumour_recurrence")
    assert (call.execution_status, call.retrieval_status) == ("success", "records_found")
    assert call.message == "called in 3 patient(s); 1 cancer type(s) with at least 2"
    (record,) = evidence(graph, call)
    assert (record.evidence_class, record.about_traits, record.about_genes) == ("association", ["Glioma"], [])
    assert (record.data["patients_with_mutation"], record.data["patients_sequenced"]) == (2, 3)
    assert "was called in the tumours of 2 of 3 patients with Glioma" in record.observed_result
    assert any("no background mutation rate is modelled" in x for x in record.limitations)
    rows = {o["cancer_type"]: o for o in call.observations if o["record"] == "cancer_type"}
    assert (rows["Melanoma"]["patients_with_mutation"], rows["Melanoma"]["evidence"]) == (1, False)
    assert T.listed("trait.allele", "database", "tumour_recurrence", record)
    fill.run(graph)
    claim = next(c for c in graph.claims.values() if c.relation == "associated_with_trait")
    assert claim.assertion_text.endswith("differ in Glioma.")
    assert claim.evidence_links[0].rationale == ("cBioPortal: this mutation was called in the tumours of 2 of 3 "
                                                 "patients with Glioma")


@pytest.mark.data
def test_the_cohort_is_not_asked_without_a_grch37_placement_or_about_an_inherited_variant(v9_cfg, tmp_path):
    graph = ClaimGraph(case(DEV, origin="somatic"))
    call = ask(live(tmp_path / "a", cohort([], {}), v9_cfg), graph, "tumour_recurrence")
    assert call.execution_status == "not_applicable" and "GRCh37 placement" in call.message
    graph = ClaimGraph(case(DEV, origin="germline"))
    annotated(graph)
    call = ask(live(tmp_path / "b", cohort([], {}), v9_cfg), graph, "tumour_recurrence")
    assert call.execution_status == "not_applicable" and "inherited" in call.message
    graph = ClaimGraph(case(DEV, origin="unknown"))
    annotated(graph)
    call = ask(live(tmp_path / "c", cohort([mutation("P1", 5)], {"P1": "Glioma"}), v9_cfg), graph, "tumour_recurrence")
    assert (call.execution_status, call.retrieval_status, call.evidence_ids) == ("success", "no_records_found", [])
    assert call.message == "the cohort does not call this substitution"


# --- litvar_search, litvar_mentions ---------------------------------------------------------------------------------

ACCESSION = "@VARIANT_rs1427407"
WORDS = sorted(reader.ASSAY_WORDS)                         # the tool sends them in one order, whoever asks


def paper(pmid: str, pmcid: str | None, title: str) -> dict:
    return {"_id": pmid, "pmid": int(pmid), "pmcid": pmcid, "title": title, "journal": "J Synth Genomics",
            "date": "2024-01-01T00:00:00Z", "doi": f"10.5555/v2m.test.{pmid[-1]}", "score": 1.0}


def litvar_routes(papers: list[dict], position: str = "2:60490908", accession: str = ACCESSION) -> dict:
    return {S.litvar_entry_url(RSID): {"_id": f"litvar@{RSID}##", "rsid": RSID, "gene": ["BCL11A"], "name": RSID,
                                       "data_chromosome_base_position": [position]},
            S.pubtator_name_url(RSID): [{"_id": "@VARIANT_rs14274070", "biotype": "variant", "db_id": "rs14274070##"},
                                        {"_id": accession, "biotype": "variant", "db_id": f"{RSID}##"}],
            S.pubtator_search_url(accession, WORDS): {"results": papers, "count": len(papers) + 90, "page_size": 10}}


def marked(pmid: str, *texts: tuple[str, str | None]) -> dict:
    """An article as PubTator marks it: variant annotations, each with its text and the rsID it was normalised to."""
    notes = [{"text": t, "infons": {"type": "Variant", "rsid": r, "rsids": [r] if r else []}} for t, r in texts]
    notes.append({"text": "GATA1", "infons": {"type": "Gene", "identifier": "2623"}})
    return {"PubTator3": [{"pmid": int(pmid), "passages": [{"annotations": notes}]}]}


def source_runner(routes: dict, folder: Path) -> ToolRunner:
    return ToolRunner(mode="cache_only", http=fakes.FakeHttp(routes), run_dir=folder, registry=fill_tools.registry(),
                      limits=ToolLimits(fulltext_soft=30, fulltext_hard=30), clock=lambda: fakes.NOW)


def test_litvar_lists_the_papers_of_its_entry_at_the_variants_position(tmp_path):
    listed = [paper("90000008", VARIANTS, "Probe comparisons."), paper(SHORT_PMID, SHORT, "A shorthand.")]
    graph = ClaimGraph(case(DEV))
    call = ask(source_runner(litvar_routes(listed), tmp_path / "a"), graph, "litvar_search", words=WORDS)
    assert (call.execution_status, call.retrieval_status, call.evidence_ids) == ("success", "records_found", [])
    found = [o for o in call.observations if o["record"] == "paper"]
    assert [(o["pmid"], o["pmcid"]) for o in found] == [("90000008", VARIANTS), (SHORT_PMID, SHORT)]
    (entry,) = [o for o in call.observations if o["record"] == "variant"]
    assert (entry["same_position"], entry["accession"], entry["papers_matching"]) == (True, ACCESSION, 92)
    # an entry somewhere else is not this variant: nothing is listed, and PubTator is not asked
    graph = ClaimGraph(case(DEV))
    runner = source_runner(litvar_routes(listed, position="2:1"), tmp_path / "b")
    call = ask(runner, graph, "litvar_search", words=WORDS)
    assert (call.execution_status, call.retrieval_status) == ("success", "no_records_found")
    assert runner.http.calls == [S.litvar_entry_url(RSID)]
    # no rsID to ask by
    graph = ClaimGraph(case(DEV.model_copy(update={"rsid": None})))
    call = ask(source_runner(litvar_routes(listed), tmp_path / "c"), graph, "litvar_search", words=WORDS)
    assert call.execution_status == "not_applicable"


def test_the_spellings_of_an_article_are_the_marks_normalised_to_this_variant():
    document = marked(SHORT_PMID, ("T908G", RSID), ("T908G", RSID), ("c.-124C>T", RSID), (RSID, RSID),
                      ("G > T", RSID), ("V600E", "rs113488022"), ("C250T", None))["PubTator3"][0]
    assert S.spellings(document, [RSID]) == [{"record": "spelling", "text": "T908G", "count": 2},
                                             {"record": "spelling", "text": "c.-124C>T", "count": 1}]
    assert S.spellings(document, ["rs1"]) == []


def reading_setup(cfg, tmp: Path, epmc: dict[int, list[str]], listed: list[dict], replies: dict[str, dict]):
    """The reader on the fill's registry: Europe PMC as in test_reader, LitVar and PubTator beside it, and the
    synthetic article that writes the variant by a shorthand only."""
    routes, rec = fakes.routes(), fakes.records()
    for i, query in enumerate(reader.queries(RSID)):
        routes[lit.search_url(query, reader.SEARCH_RESULTS)] = fakes.search_response([rec[p] for p in epmc.get(i, [])])
    short = {**rec["PMC9000007"], "id": SHORT_PMID, "pmid": SHORT_PMID, "pmcid": SHORT, "doi": "10.5555/v2m.test.9",
             "title": "An invented enhancer mutation changes reporter activity.",
             "abstractText": "We describe invented reporter experiments on the enhancer mutation T908G."}
    routes[lit.metadata_url(SHORT, None)] = fakes.search_response([short])
    routes[lit.fulltext_url(SHORT)] = fakes.text("oa_shorthand.xml")
    routes.update(litvar_routes(listed))
    routes[S.pubtator_text_url(SHORT_PMID)] = marked(SHORT_PMID, ("T908G", RSID), ("T908G", RSID))
    model = Model(cfg, tmp, replies)
    runner = source_runner(routes, tmp / "run")
    return bundle_graph(), reader.Reader(R.RoleCaller(model.client, cfg), runner), model, runner


SHORT_REPORTER = experiment(
    "sec1.1/p1", assay="reporter_assay", intervention="luciferase reporter with T and G allele constructs",
    endpoint="luciferase activity", comparator="the T allele construct",
    result="the G allele construct gave twofold lower activity", direction="decreases", about_variants=["T908G"],
    manipulated="allele", compared_allele="G", tissue_or_cell="K562 cells")


def test_an_article_only_litvar_lists_is_read_with_the_spellings_it_uses(v9_cfg, tmp_path):
    listed = [paper("90000008", VARIANTS, "Probe comparisons."), paper(SHORT_PMID, SHORT, "A shorthand.")]
    graph, read, model, runner = reading_setup(v9_cfg, tmp_path, {0: [VARIANTS]}, listed,
                                               {SHORT: reading(SHORT_REPORTER)})
    counts = fill.run(graph, None, read)
    summary = counts["reading"]
    assert [s["listed"] for s in summary["searches"]] == [1, 0, 2]            # two Europe PMC queries, then LitVar
    assert summary["searches"][2]["query"].startswith("litvar_search")
    rows = {r["label"]: r for r in summary["articles"]}
    assert (rows[SHORT]["status"], rows[SHORT]["spellings"], rows[SHORT].get("litvar_only")) == ("read", ["T908G"], True)
    assert rows[VARIANTS]["status"] == "read" and "spellings" not in rows[VARIANTS]
    # the spellings are asked for the article only LitVar listed, and only its packet names them
    assert [u for u in runner.http.calls if "biocjson" in u] == [S.pubtator_text_url(SHORT_PMID)]
    short, other = (next(p for p in model.packets if key in p) for key in (SHORT, VARIANTS))
    assert "- this article writes it as: " in short and "T908G" in short.split("<data>")[0]
    assert "this article writes it as" not in other
    assert "[sec1.1/p1]" in short and "[sec2/p1]" not in short                # the result, not the retelling
    # the article defines its shorthand by position and alleles, so the literature route's own rule places it
    (record,) = [e for e in read_records(graph) if e.source_ids[0].endswith(SHORT_PMID)]
    assert record.evidence_class == "reporter_assay" and graph.variant_mention(record.about_variants[0]) == "case"
    claim = next(c for c in graph.claims.values() if c.relation == "alters_regulatory_activity")
    assert record.evidence_id in [x.evidence_id for x in claim.evidence_links if x.stance == "supports"]
    assert reader.MAX_ARTICLES == 3 * reader.SEARCH_RESULTS and summary["format"] == 6
    # a shorthand the article defines by a position is placed by that position, never by the text-mining rule
    assert "text_mined_names" not in record.data and summary["by_name"] == 0


# --- an article's own name for a mutation ---------------------------------------------------------------------------

MINUS = "\u2212"                                         # the article writes a true minus sign; PubTator a hyphen
OURS, THEIRS = f"{MINUS}58A>C", f"{MINUS}70C>T"            # T>G on the other strand; another mutation


def named_reporter(location: str, name: str = OURS, allele: str | None = "C", direction: str = "decreases") -> dict:
    return experiment(location, assay="reporter_assay", endpoint="luciferase activity",
                      intervention="luciferase reporter with mutant and wild-type constructs",
                      comparator="the wild-type construct", result="the mutant construct changed activity",
                      direction=direction, about_variants=[name], manipulated="allele", compared_allele=allele,
                      tissue_or_cell="K562 cells")


def named_setup(cfg, tmp: Path, marks: list[tuple[str, str | None]], *experiments: dict):
    """The reader on the article that names its mutations by their own names: only LitVar lists it, and PubTator
    marks its variant names as `marks` says (a text and the rsID it is normalised to)."""
    routes, rec = fakes.routes(), fakes.records()
    for query in reader.queries(RSID):
        routes[lit.search_url(query, reader.SEARCH_RESULTS)] = fakes.search_response([])
    named = {**rec["PMC9000007"], "id": NAMED_PMID, "pmid": NAMED_PMID, "pmcid": NAMED, "doi": "10.5555/v2m.test.10",
             "title": "Two invented promoter mutations change reporter activity.",
             "abstractText": f"We describe invented reporter experiments on the promoter mutations {OURS} and {THEIRS}."}
    routes[lit.metadata_url(NAMED, None)] = fakes.search_response([named])
    routes[lit.fulltext_url(NAMED)] = fakes.text("oa_named.xml")
    routes.update(litvar_routes([paper(NAMED_PMID, NAMED, "Two mutations.")]))
    routes[S.pubtator_text_url(NAMED_PMID)] = marked(NAMED_PMID, *marks)
    model = Model(cfg, tmp, {NAMED: reading(*experiments)})
    graph, read = bundle_graph(), reader.Reader(R.RoleCaller(model.client, cfg), source_runner(routes, tmp / "run"))
    counts = fill.run(graph, None, read)
    refusals = [e.concise_reason for e in graph.events
                if e.action == "refuse_update" and (e.details or {}).get("reader") is True]
    return graph, counts["reading"], refusals


def test_a_name_writes_one_base_change_or_none():
    from variant2mechanism.v9.variant_identity import name_change
    for name in ("-124C>T", "c.-124C > T", "c.-124c > T", f"{MINUS}124 C >T", "C228T", "C>T to -124", "+ -124C>T"):
        assert name_change(name) == ("C", "T"), name
    assert name_change("G228A") == ("G", "A") and name_change("T908G") == ("T", "G")
    for name in ("-124 C", "cytosine located -124", "p.C228T", "C250T/C228T", "CC>TT 124", "A>A 5", "rs1427407", ""):
        assert name_change(name) is None, name


def test_a_name_is_found_however_it_is_spaced_and_never_inside_another():
    assert {lit.name_key(n) for n in ("-124C>T", "-124 C >T", "+ -124C>T", f"{MINUS}124C > T")} == {"-124C>T"}
    assert lit.name_key("c.-124c > T") == lit.name_key("c.-124C>T") == "C.-124C>T"
    found = lit.name_pattern("-124C>T")
    for text in (f"the {MINUS}124C>T mutation", f"c.{MINUS}124C > T", "(-124 C>T)", f"{MINUS}124C>T/{MINUS}146C>T"):
        assert found.search(lit.normalise_for_match(text)), text
    for text in (f"{MINUS}1124C>T", f"{MINUS}124C>TT", "+124C>T", "124C>T", f"{MINUS}146C>T"):
        assert not found.search(lit.normalise_for_match(text)), text
    unsigned = lit.name_pattern("124C>T")                 # a number is not read out of a signed or longer one
    assert unsigned.search("at 124C>T") and not any(unsigned.search(t) for t in ("-124C>T", "1,124C>T", "+124C>T"))
    assert lit.name_pattern("G > A") is None              # a name needs a number


def test_an_articles_own_name_counts_as_the_variant_under_two_checks(v9_cfg, tmp_path):
    marks = [("-58A>C", RSID), ("-58A>C", RSID), ("-70C>T", "rs90000017")]
    graph, summary, refusals = named_setup(
        v9_cfg, tmp_path, marks,
        named_reporter("sec1.1/p1"),                      # the quotation writes the name: counted
        named_reporter("sec1.1/p2"),                      # the quotation is about the other mutation
        named_reporter("sec1.2/p1"),                      # no name where the result is
        named_reporter("sec1.1/p2", THEIRS, "T", "increases"))   # a name no text mining ties to this variant
    (row,) = summary["articles"]
    assert (row["status"], row["spellings"], row["experiments"]) == ("read", ["-58A>C"], 4)
    (record,) = read_records(graph)
    assert row["accepted"] == row["by_name"] == [record.evidence_id] and summary["by_name"] == 1
    # the record is about the case variant, with the allele placed on the forward strand (C is G there)
    assert record.about_variants == [graph.case.variant.key] and record.allele == "G"
    assert record.experiment.about_variants == [f"paper:{NAMED}:-58A>C"]          # the article's notation is kept
    proof = record.data["variant_identity"]
    assert (proof["basis"], proof["paper_change"], proof["case_alleles"], proof["paper_to_case_strand_flip"],
            proof["paper_allele"], proof["case_allele"], proof["written_in"], proof["rsids"]) == (
        "text_mined_name", ["A", "C"], ["T", "G"], True, "C", "G", ["passage"], [RSID])
    assert graph.tool_calls[proof["tool_call"]].tool_name == "litvar_mentions"
    assert record.data["variant_identity_status"] == "text_mined"                # never "verified_same"
    assert any("text mining" in x and "Text mining can be wrong" in x for x in record.limitations)
    claim = next(c for c in graph.claims.values() if c.relation == "alters_regulatory_activity")
    assert record.evidence_id in [x.evidence_id for x in claim.evidence_links if x.stance == "supports"]
    # the other three are refused, each for what it lacks
    assert len(refusals) == 3 and all("names no variant the paper names" in r for r in refusals)
    assert sum("counts only where it is written" in r for r in refusals) == 2
    assert sum("they name no rsID or chromosome position" in r for r in refusals) == 1
    # the table prints how the record was identified, beside its quotation
    (shown,) = [r for c in T.from_graph(graph).claims.values() for r in c.cells["literature"].records
                if r.id == record.evidence_id and r.stance == "supports"]
    assert "named \"-58A>C\" in the quotation:" in shown.note and "text mining" in shown.note


def test_a_name_whose_base_change_is_not_the_variants_stays_unresolved(v9_cfg, tmp_path):
    # text mining ties the other mutation's name to this variant too: the base change (C>T) is not T>G on either strand
    marks = [("-58A>C", RSID), ("-70C>T", RSID)]
    graph, summary, refusals = named_setup(v9_cfg, tmp_path, marks,
                                           named_reporter("sec1.1/p2", THEIRS, "T", "increases"))
    (record,) = read_records(graph)
    assert record.data["variant_identity_status"] == "unresolved" and "variant_identity" not in record.data
    assert record.about_variants == [f"paper:{NAMED}:-70C>T"] and summary["by_name"] == 0
    assert any("the base change it writes (C>T) is not T>G on either strand" in x for x in record.limitations)
    assert not [x for c in graph.claims.values() for x in c.evidence_links
                if x.evidence_id == record.evidence_id and x.stance in ("supports", "contradicts")]


def mined_record(graph: ClaimGraph, allele: str | None, spelling: str = "-58A>C", pmid: str = NAMED_PMID):
    """A record as the literature route files it under an article's own name, and the lookup that ties the name."""
    from variant2mechanism.v9.schemas import Evidence
    code_call(graph, "litvar_mentions", observations=[{"record": "spelling", "text": "-58A>C", "count": 2}],
              pmid=NAMED_PMID)
    article = lit.Article(pmid=pmid, pmcid=NAMED, title="Two mutations.", route="europepmc_fulltext",
                          access="full_text", sections=[])
    key = lit.name_key(spelling)
    return Evidence(evidence_class="reporter_assay", source_ids=[f"PMID:{pmid}"], observed_result="lower activity",
                    allele=allele, direction="decreases", about_variants=[f"paper:{NAMED}:{key}"], origin="literature",
                    independence_group=f"PMID:{pmid}#reporter_assay",
                    data={"variant_identity_status": "unresolved", "text_mined_names": [
                        {"name": key, "spelling": spelling, "change": ["A", "C"], "written_in": "passage"}]}), article


def test_what_the_name_rule_does_not_take():
    from variant2mechanism.v9.variant_identity import normalise_evidence

    def after(variant=DEV, allele: str | None = "C", **kw):
        graph = ClaimGraph(case(variant))
        record, article = mined_record(graph, allele, **kw)
        return normalise_evidence(record, graph, article=article), graph

    done, graph = after()
    assert (done.allele, done.about_variants, done.data["variant_identity_status"]) == ("G", [graph.case.variant.key],
                                                                                      "text_mined")
    assert after(allele="A")[0].allele == "T" and after(allele=None)[0].allele is None
    # a name on the forward strand needs no complement
    same, _ = after(DEV.model_copy(update={"ref": "A", "alt": "C"}))
    assert (same.allele, same.data["variant_identity"]["paper_to_case_strand_flip"]) == ("C", False)
    refused = {
        "reads the same on both strands": after(DEV.model_copy(update={"ref": "A", "alt": "T"})),
        "is not C>A on either strand": after(DEV.model_copy(update={"ref": "C", "alt": "A"})),   # the reverse order
        "no text-mining lookup of this article": after(pmid="90000011"),
        "no text-mining lookup of this article ": after(spelling="-58 A>C"),     # not the spelling the lookup lists
        "is not a base of that name (A>C)": after(allele="G"),                   # it could be a third allele
    }
    for why, (record, _) in refused.items():
        assert record.data["variant_identity_status"] == "unresolved" and "variant_identity" not in record.data, why
        assert record.about_variants[0].startswith("paper:") and any(why.strip() in x for x in record.limitations), why
    # nothing else files such a record, and a record without the flag is left as it is
    graph = ClaimGraph(case(DEV))
    record, article = mined_record(graph, "C")
    plain = record.model_copy(update={"data": {}})
    assert normalise_evidence(plain, graph, article=article) == plain


def test_without_the_litvar_tools_the_reader_reads_as_before(v9_cfg, tmp_path):
    from .test_reader import FOUND, REPLIES, setup
    graph, read, model = setup(v9_cfg, tmp_path, FOUND, REPLIES)             # the default registry: no LitVar
    read.run(graph)
    assert len(read.searches) == 2 and not any("writes it as" in p for p in model.packets)


# --- names with a Greek letter --------------------------------------------------------------------------------------

def hgnc(tmp: Path, rows: list[tuple[str, str, str]]) -> Path:
    path = tmp / "hgnc.txt"
    lines = ["hgnc_id\tsymbol\tstatus\tprev_symbol\talias_symbol\tlocus_group"]
    lines += [f"HGNC:{i}\t{symbol}\tApproved\t{prev}\t{alias}\tprotein-coding gene"
              for i, (symbol, prev, alias) in enumerate(rows, 1)]
    path.write_text("\n".join(lines) + "\n")
    return path


def test_a_name_with_a_greek_letter_resolves_to_the_one_gene_that_lists_it(tmp_path):
    resolver = SymbolResolver.from_hgnc(hgnc(tmp_path, [
        ("TFAP2A", "TFAP2", "AP-2|AP-2alpha"), ("TFAP2B", "", "AP-2beta|AP2-B"), ("CEBPA", "CEBP", "C/EBP-alpha"),
        ("GSTM1", "", "MU|GST-mu1"), ("PSMA2", "", "MU"), ("IFNA17", "", "IFN-alphaI"), ("IFNA21", "", "IFN-alphaI"),
        ("ALPHA1", "", ""), ("GENEX", "", "alpha-1")]))
    assert greek_key("AP-2α") == greek_key("AP-2alpha") == greek_key("AP2 alpha") == "ap2alpha"
    assert greek_key("AP-2") is None and greek_key("GATA3") is None and greek_key("immune") is None
    assert resolver("AP-2α")[0] == resolver("AP-2alpha")[0] == resolver("ap2-ALPHA")[0] == "TFAP2A"
    assert resolver("AP-2β")[0] == "TFAP2B" and resolver("C/EBPα")[0] == "CEBPA"
    assert resolver("AP-2") is None                        # a family name says no paralogue: aliases are not read
    assert resolver("IFN-αI") is None                      # two genes list it
    assert resolver("α-1") is None and resolver("ALPHA1")[0] == "ALPHA1"   # another gene's own symbol reads the same
    assert resolver("TFAP2")[0] == "TFAP2A" and resolver("TFAP2A")[0] == "TFAP2A"   # symbols are read as before
    assert SymbolResolver({"TFAP2A": ("TFAP2A", "HGNC:1")})("AP-2α") is None       # no alias table, no lookup


def test_a_tf_named_with_a_greek_letter_meets_the_claim_about_its_gene():
    resolver = SymbolResolver({"TFX": ("TFX", "HGNC:1")}, greek={"tfxalpha": ("TFX", "HGNC:1")})
    g = ClaimGraph(bundle_graph().case, resolver=resolver)
    assert g.entity("tf", "TFX-α") == g.entity("tf", "TFX")
    assert scope_from_label("K562").label == "K562"        # (the context table is untouched by any of this)
