"""Lookups that only code makes: three tools asked for many things at once, the gene-to-trait source, and
allele-specific binding from ADASTRA.

Why they are not in adapters.py: a model role asks one question at a time (one TF, one trait), so the tools it is
shown answer one. Code filling a chain table asks the same question of every candidate, and one call per TF would
write the same ChIP-seq response into the run folder a hundred times. These tools sit in their own registry
(registry(): every default tool plus these), which only the fill's runner uses, so the tools a role is shown, and
with them every saved prompt, stay as they are.

    tf_occupancy_set    chip_occupancy for a list of TFs: the same Evidence, one raw result
    tf_expression_set   tf_expression for a list of TFs in the request's context: the same Evidence
    credible_sets_all   credible_sets_l2g for every credible set holding the variant, with no trait named
    gene_disease        Open Targets' direct evidence that a gene bears on a disease or trait
    adastra_asb         ADASTRA's allele-specific ChIP-seq binding calls at the variant, one record per TF

The three bulk tools add no rule of their own: they run the adapter's own code and return its Evidence unchanged, so
an item one of them returns and the item its single-question tool returns are one record in the graph.

gene_disease reads Open Targets' association of one gene with the traits it is asked about, source by source, and
keeps the sources that are a record about the gene: rare-variant burden tests, curated gene-disease pairs (ClinVar,
PanelApp, Gene2Phenotype, Orphanet, ClinGen, UniProt, the Cancer Gene Census, cancer biomarkers), driver inference
from tumour cohorts, and mouse knockouts whose phenotypes were matched to the disease. Three sources are listed and
never Evidence:
- GWAS credible sets assigned to the gene by the locus-to-gene model. They can be the very signal the variant under
  study belongs to, which the variant-to-trait claim and the locus-to-gene score already count: a chain must not be
  supported twice by one association.
- Text-mined co-occurrence in articles, which is no record of an experiment.
- Drugs in clinical development. A trial is a bet that the target matters, and the association row does not say
  whether a drug was approved or failed; only its score does, and no score is read as a call here.
A mouse knockout is filed as an inference, not as a perturbation that measured the trait: Open Targets matches the
knockout's whole phenotype profile to the disease by a similarity score, so the record does not say that the trait
of the claim was measured. An article that reports such a measurement is a perturbation, and a reader can file it.
Only evidence annotated to the trait itself is read (enableIndirect false): a parent term does not stand for its
children. The scores are kept in `data` and never read by anything that orders a chain.

adastra_asb reads ADASTRA (release 6.1, "Mabel"), which pools the ChIP-seq experiments of each protein and calls,
at each variant that some cell is heterozygous for, whether the reads over it favour one allele. What it returns is
a measurement in cells: allele-resolved ChIP-seq, the same kind of record as allele-specific ChIP read from an
article. Which claim a record bears on depends on what the protein is (proteins.py):
- A transcription factor: "the two alleles differ in binding the TF". ADASTRA is the one database source for it.
- A protein that does not bind DNA itself (BRD4, β-catenin): "the two alleles differ in the regulatory activity of
  the site". Its reads show the state of the site and name no TF that reads the variant, so it enters no chain as a
  TF. ADASTRA's motif column cannot make this call: it is empty for such a protein, and "no hit" for a TF only says
  that one motif scan found nothing, which a QBiC-SELEX prediction for the same allele can contradict.
The rest holds for both kinds:
- One record per TF whose call passes ADASTRA's own 5% FDR on one allele. A TF that was tested and did not pass is
  listed, never a record: too few reads over the variant is the usual reason, and that is not a measured absence.
- A variant with no entry is "nothing found", not evidence that the alleles bind alike: ADASTRA can only call a
  variant in cells that are heterozygous for it and were assayed for that TF.
- An imbalance in a TF's reads does not say that TF reads the variant: a factor bound next to the one whose site
  the variant changes shows the same imbalance. ADASTRA says whether the TF's own motif agrees (motif concordance),
  and every record carries that as a limitation when it does not. The record still counts: it is the measurement.
- The call is made in cells heterozygous for the variant, so it compares two haplotypes. Another variant on the same
  haplotype, inside the bound region, could cause the imbalance; every record says so.
- ADASTRA names TFs by UniProt entry (ANDR_HUMAN). A record is made only for a TF whose UniProt accession the HGNC
  table maps to one approved symbol; the others are listed with what was missing.
- Effect sizes and FDR values are kept in `data` and never read by anything that orders a chain.
"""

import csv
from dataclasses import replace
from functools import lru_cache
from typing import Any

from ..context import genetics
from . import adapters, http9, literature, proteins  # noqa: F401  (literature registers its tools in the registry)
from .qbic_reader import reader_for
from .schemas import ContextScope, Coverage, Evidence
from .tools import REGISTRY, AdapterResult, ParamSpec, ToolContext, ToolRegistry, ToolSpec

GENE_PAGE, GENE_MAX_PAGES = 100, 5
# Open Targets data sources that are a record about the gene and the trait: (evidence class, what it is).
OT_SOURCES: dict[str, tuple[str, str]] = {
    "gene_burden": ("association", "rare-variant burden tests of the gene"),
    "eva": ("clinical_assertion", "ClinVar classifications of germline variants in the gene"),
    "eva_somatic": ("clinical_assertion", "ClinVar classifications of somatic variants in the gene"),
    "genomics_england": ("clinical_assertion", "Genomics England PanelApp gene panels"),
    "gene2phenotype": ("clinical_assertion", "Gene2Phenotype curated gene-disease pairs"),
    "orphanet": ("clinical_assertion", "Orphanet curated gene-disease pairs"),
    "clingen": ("clinical_assertion", "ClinGen gene-disease validity curation"),
    "uniprot_literature": ("clinical_assertion", "UniProt curated disease annotation"),
    "uniprot_variants": ("clinical_assertion", "UniProt curated disease variants"),
    "cancer_gene_census": ("clinical_assertion", "the COSMIC Cancer Gene Census"),
    "cancer_biomarkers": ("clinical_assertion", "Cancer Genome Interpreter biomarkers"),
    "intogen": ("statistical_inference", "IntOGen driver-gene inference from tumour cohorts"),
    "impc": ("statistical_inference", "IMPC mouse knockouts, their phenotypes matched to the disease by similarity,"),
}
OT_NOT_USED: dict[str, str] = {
    "gwas_credible_sets": ("GWAS credible sets assigned to the gene by the locus-to-gene model: they can be this "
                           "variant's own signal, which the variant-to-trait claim and the locus-to-gene score "
                           "already count"),
    "europepmc": "text-mined co-occurrence in articles: no record of an experiment",
    "clinical_precedence": ("drugs with this target in clinical development for the disease: a trial is a bet on the "
                            "target, and this row does not say whether a drug was approved or failed"),
}
OT_OTHER = "a source this tool does not map to a kind of evidence"
IMPC_LIMITS = ["mouse, not human", "the knockout's phenotype profile was matched to the human disease by a similarity "
               "score: the record does not say that this trait was measured"]
OT_GENE_QUERY = """query V2MGeneDisease($id: String!, $ids: [String!], $index: Int!) {
  meta { apiVersion { x y z } dataVersion { year month } }
  target(ensemblId: $id) {
    id approvedSymbol
    associatedDiseases(Bs: $ids, enableIndirect: false, includeMeasurements: true,
                       page: {index: $index, size: %d}) {
      count
      rows { disease { id name } score datasourceScores { id score } }
    }
  }
}""" % GENE_PAGE


def _inner(ctx: ToolContext, spec: ToolSpec) -> ToolContext:
    """The context an adapter sees when a bulk tool runs it: its own spec, everything else the bulk call's."""
    return replace(ctx, spec=spec)


def _unique(values: list[str]) -> list[str]:
    return list(dict.fromkeys(v for v in values if v))


def _oldest(results: list[AdapterResult]) -> str | None:
    times = sorted(r.retrieval_time for r in results if r.retrieval_time)
    return times[0] if times else None


# --- tf_occupancy_set -----------------------------------------------------------------------------------------------

TF_OCCUPANCY_SET = ToolSpec(
    name="tf_occupancy_set", route="computational",
    description=("chip_occupancy for a list of TFs in one call: per-experiment Evidence for every listed TF with a "
                 "ChIP-seq peak containing the variant (ENCODE Factorbook peaks and ReMap 2022)."),
    params={"tfs": ParamSpec(type="list[str]", required=True, normalise="upper", description="HGNC TF symbols")},
    variant_types=["SNV"], provider=adapters.CHIP_OCCUPANCY.provider,
    dataset_release=adapters.CHIP_OCCUPANCY.dataset_release, coverage_notes=adapters.CHIP_OCCUPANCY.coverage_notes,
    result_semantics=("records_found: the Evidence chip_occupancy returns for each listed TF (occupancy, one item per "
                      "experiment with a peak containing the variant), and one observation per TF. "
                      "no_records_found: no listed TF has such a peak, which is no evidence either way."),
    rate_policy="parallel", evidence_classes=["occupancy"], network=True)


def tf_occupancy_set(params: dict, ctx: ToolContext) -> AdapterResult:
    tfs = list(params["tfs"])
    inner = _inner(ctx, adapters.CHIP_OCCUPANCY)
    results = [(tf, adapters.chip_occupancy({"tf": tf}, inner)) for tf in tfs]
    failed = next((r for _, r in results if r.execution_status != "success"), None)
    if failed is not None:                       # the sources are the same for every TF: one failure is all of them
        return AdapterResult(execution_status=failed.execution_status, message=failed.message, raw=failed.raw)
    evidence = [e for _, r in results for e in r.evidence]
    incomplete = any(r.retrieval_status == "incomplete" for _, r in results)
    bound = [tf for tf, r in results if r.evidence]
    first = results[0][1]
    limitations = _unique([note for _, r in results for note in r.coverage.limitations
                           if not note.startswith("ENCODE assayed")])
    return AdapterResult(
        retrieval_status="incomplete" if incomplete else "records_found" if evidence else "no_records_found",
        observations=[{"record": "factor", "tf": tf, "experiments": len(r.evidence),
                       "retrieval_status": r.retrieval_status} for tf, r in results],
        coverage=Coverage(requested_scope=f"ChIP-seq for {len(tfs)} TFs at {adapters._where(ctx.case.variant)}",
                          assessed_scope=f"{len(bound)} of them with a peak containing the variant, "
                                         f"{len(evidence)} experiments",
                          limitations=limitations),
        evidence=evidence, raw={**(first.raw or {}), "query": {"tfs": tfs}},
        message=f"{len(bound)} of {len(tfs)} TFs have a peak containing the variant ({len(evidence)} experiments)",
        cached=all(r.cached for _, r in results), retrieval_time=_oldest([r for _, r in results]))


# --- tf_expression_set ----------------------------------------------------------------------------------------------

TF_EXPRESSION_SET = ToolSpec(
    name="tf_expression_set", route="computational",
    description=("tf_expression for a list of TFs in one call: each TF's expression level in a context, from local "
                 "DepMap and GTEx v8 data. Reported as levels, never as a threshold call."),
    params={"tfs": ParamSpec(type="list[str]", required=True, normalise="upper", description="HGNC symbols"),
            "context": ParamSpec(description="a cell line, tissue, GTEx:<tissue> or DepMap:<ACH id>; default: the "
                                             "supplied context")},
    assemblies=[], provider=adapters.TF_EXPRESSION.provider, dataset_release=adapters.TF_EXPRESSION.dataset_release,
    coverage_notes=adapters.TF_EXPRESSION.coverage_notes,
    result_semantics=("records_found: the Evidence tf_expression returns for each listed TF (expression, a TPM level "
                      "per resolved context). no_records_found: no context, an unknown context or no listed gene in "
                      "the data."),
    rate_policy="parallel", evidence_classes=["expression"])


def tf_expression_set(params: dict, ctx: ToolContext) -> AdapterResult:
    tfs = list(params["tfs"])
    inner = _inner(ctx, adapters.TF_EXPRESSION)
    extra = {"context": params["context"]} if params.get("context") else {}
    results = [adapters.tf_expression({"tf": tf, **extra}, inner) for tf in tfs]
    evidence = [e for r in results for e in r.evidence]
    observations = [o for r in results for o in r.observations]
    return AdapterResult(
        retrieval_status="records_found" if evidence else "no_records_found", observations=observations,
        coverage=Coverage(requested_scope=f"expression of {len(tfs)} genes in "
                                          f"{params.get('context') or 'the supplied context'}",
                          assessed_scope=f"{len(evidence)} level(s)",
                          limitations=_unique([note for r in results for note in r.coverage.limitations])),
        evidence=evidence, raw={"tfs": tfs, "context": params.get("context"), "observations": observations},
        message=f"{len(evidence)} expression level(s) for {len(tfs)} genes")


# --- credible_sets_all ----------------------------------------------------------------------------------------------

CREDIBLE_SETS_ALL = ToolSpec(
    name="credible_sets_all", route="computational",
    description=("Every Open Targets GWAS credible set containing the variant, with no trait named: per set, the "
                 "variant's PIP, its locus-to-gene scores and its molecular-QTL colocalisations."),
    variant_types=["SNV"], provider=adapters.CREDIBLE_SETS_L2G.provider,
    dataset_release=adapters.CREDIBLE_SETS_L2G.dataset_release,
    coverage_notes=adapters.CREDIBLE_SETS_L2G.coverage_notes,
    result_semantics=("records_found: the Evidence credible_sets_l2g returns for a set, for every set read "
                      "(statistical_inference for the set and each colocalisation, precomputed_prediction for each "
                      "L2G row), and one observation per set with its trait and mapped disease terms. "
                      "no_records_found: every set was read and none holds the variant. incomplete: some sets were "
                      "not read."),
    rate_policy="serial", evidence_classes=["statistical_inference", "precomputed_prediction"], network=True)


def credible_sets_all(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return adapters._no_http(ctx.spec.name)
    v = ctx.case.variant
    vid = f"{v.chrom}_{v.pos}_{v.ref}_{v.alt}"
    rec = adapters._Recorder(ctx.http)
    rows, count, release, failure = adapters._ot_sets_v9(rec, vid)
    legacy = failure is not None and http9.is_cache_miss(failure)
    if legacy:
        rows, count = adapters._ot_sets_legacy(rec, ctx)
        release = "release not recorded"
        if not rows and rec.failure() is not None and all(not r.ok for _, _, r in rec.results):
            return adapters._failed(rec, "Open Targets", failure)
    elif failure is not None:
        return adapters._failed(rec, "Open Targets", failure)
    release = release or "release not recorded"
    about = adapters._case_names(ctx)
    evidence: list[Evidence] = []
    observations: list[dict[str, Any]] = [{
        "record": "summary", "credible_sets": count, "read": len(rows), "release": release,
        "query": "earlier cached query (first 200 sets of every type)" if legacy else "v9 query"}]
    truncated = []
    for row in rows:
        items = adapters._ot_evidence(row, vid, release, None, v, about)
        evidence += items
        study = row.get("study") or {}
        observations.append({
            "record": "set", "study_locus_id": row.get("studyLocusId"), "study_id": study.get("id"),
            "trait": study.get("traitFromSource"),
            "diseases": [{"id": d.get("id"), "name": d.get("name")} for d in study.get("diseases") or []],
            "pip": adapters._pip(row, vid).get("posteriorProbability"), "evidence": len(items)})
        for field in ("l2GPredictions", "colocalisation"):
            result = row.get(field) or {}
            read = len(result.get("rows") or [])
            if read < (result.get("count") or 0):
                truncated.append({"study_locus_id": row.get("studyLocusId"), "field": field, "read": read,
                                  "count": result["count"]})
    incomplete = legacy or len(rows) < count or bool(rec.partial) or bool(truncated)
    limitations = ["per credible set: never a maximum across unrelated studies"]
    if legacy:
        limitations.append("offline: an earlier cached query (first 200 credible sets of every type, no release, no "
                           "study-locus ids, no colocalisation)")
    elif len(rows) < count:
        limitations.append(f"read {len(rows)} of {count} credible sets (page cap {adapters.OT_MAX_PAGES})")
    if truncated:
        limitations.append(f"{len(truncated)} nested result lists truncated: first {adapters.OT_L2G_ROWS} L2G and "
                           f"{adapters.OT_COLOC_ROWS} colocalisation rows per set; a missing gene is not evidence of "
                           "absence")
        observations.append({"record": "nested_coverage", "truncated": truncated})
    limitations += adapters._partial_notes(rec, "Open Targets")
    status = ("incomplete" if incomplete and (rows or count or rec.partial) else
              "records_found" if rows else "no_records_found")
    return AdapterResult(
        retrieval_status=status, observations=observations,
        coverage=Coverage(requested_scope=f"every Open Targets GWAS credible set containing {vid}",
                          assessed_scope=f"{len(rows)} of {count} credible sets read", limitations=limitations),
        evidence=evidence, raw={"requests": rec.records(), "credible_sets": rows, "release": release},
        dataset_release=release, message=f"{len(rows)} of {count} credible sets read, {len(evidence)} records",
        cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- gene_disease ---------------------------------------------------------------------------------------------------

GENE_DISEASE = ToolSpec(
    name="gene_disease", route="computational",
    description=("Open Targets' direct evidence that a gene bears on the traits named, source by source: rare-variant "
                 "burden tests, curated gene-disease pairs, driver inference and mouse knockouts matched to the "
                 "disease. Without traits it lists the gene's highest-scoring associations and returns no Evidence."),
    params={"gene": ParamSpec(required=True, normalise="upper", description="an HGNC symbol"),
            "traits": ParamSpec(type="list[str]", description="ontology ids of the traits to ask about (EFO_..., "
                                                              "MONDO_..., HP_...), as Open Targets writes them")},
    assemblies=[], provider="Open Targets Platform GraphQL (target.associatedDiseases)",
    dataset_release="Open Targets Platform (release read from meta at retrieval)",
    coverage_notes=("Only evidence annotated to the trait itself (no ontology propagation), measurements included. "
                    "GWAS credible sets assigned to the gene, text-mined co-occurrence and drugs in development are "
                    "listed, never Evidence: the first can be the association under study, the second is no "
                    "experiment, the third is a bet on the target. Scores are Open Targets' own and are not comparable "
                    "across sources."),
    result_semantics=("records_found: Evidence per gene, trait and source, of the class that source is (association, "
                      "clinical_assertion, statistical_inference). no_records_found: Open Targets holds no evidence "
                      "from a source this tool uses for these traits, which is no evidence against the gene. "
                      "incomplete: some rows were not read."),
    rate_policy="serial", evidence_classes=["association", "clinical_assertion", "statistical_inference"],
    network=True)


def gene_disease_evidence(gene: str, ensembl: str, row: dict[str, Any], release: str) -> list[Evidence]:
    """The Evidence of one gene-trait association row: one item per source this tool uses, about the gene and the
    trait as Open Targets names it (name and ontology id). No item names a variant. A mouse knockout's item has a
    mouse context and does not carry the in_vivo flag: the source asserts a phenotype match, not that the trait was
    measured. Every other source is free of a cell or tissue context."""
    disease = row.get("disease") or {}
    did, name = str(disease.get("id") or ""), str(disease.get("name") or "")
    out = []
    for item in sorted(row.get("datasourceScores") or [], key=lambda x: str(x.get("id"))):
        source = str(item.get("id"))
        if source not in OT_SOURCES or not item.get("score"):
            continue
        cls, what = OT_SOURCES[source]
        mouse = source == "impc"
        out.append(Evidence(
            origin="tool", access="dataset", evidence_class=cls,
            source_ids=[f"OT:{ensembl}-{did}:{source}"],
            observed_result=(f"Open Targets ({release}): {what} link {gene} to {name} ({did}); source score "
                             f"{float(item['score']):.2f}."),
            data={"gene": gene, "gene_id": ensembl, "disease_id": did, "disease": name, "datasource": source,
                  "score": float(item["score"]), "release": release},
            context=ContextScope(label="mouse", species="mouse", biosample_kind="organism",
                                 source="evidence") if mouse else None,
            about_genes=[gene], about_traits=_unique([name, did]),
            independence_group=f"OT-ASSOC:{source}:{ensembl}:{did}",
            limitations=["an association record of the gene: it says nothing about this variant",
                         *(IMPC_LIMITS if mouse else [])]))
    return out


def gene_disease(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return adapters._no_http(ctx.spec.name)
    gene = str(params["gene"])
    ensembl = reader_for(adapters._config(ctx)).registry.ensembl_by_symbol.get(gene)
    if not ensembl:
        return AdapterResult(execution_status="not_applicable",
                             message=f"{gene}: no Ensembl gene id in the HGNC table, so Open Targets was not asked")
    ids = list(params.get("traits") or [])
    rec = adapters._Recorder(ctx.http)
    rows, count, release = [], 0, None
    for index in range(GENE_MAX_PAGES if ids else 1):
        r = rec.query(genetics.OT, {"query": OT_GENE_QUERY,
                                    "variables": {"id": ensembl, "ids": ids or None, "index": index}})
        data = (r.data or {}).get("data") if r.ok and isinstance(r.data, dict) else None
        if data is None:
            if index == 0:
                return adapters._failed(rec, "Open Targets", r)
            rec.partial.append(f"association page {index} failed: {r.error or 'no data'}")
            break
        meta = data.get("meta") or {}
        dv, api = meta.get("dataVersion") or {}, meta.get("apiVersion") or {}
        release = (f"Open Targets Platform {dv.get('year')}.{dv.get('month')} (API {api.get('x')}.{api.get('y')}."
                   f"{api.get('z')})") if dv else release
        found = ((data.get("target") or {}).get("associatedDiseases") or {})
        count = int(found.get("count") or 0)
        rows += found.get("rows") or []
        if len(rows) >= count or not found.get("rows"):
            break
    release = release or "release not recorded"
    evidence = [e for row in rows for e in gene_disease_evidence(gene, ensembl, row, release)] if ids else []
    observations: list[dict[str, Any]] = [{"record": "summary", "gene": gene, "gene_id": ensembl,
                                           "traits_asked": len(ids), "associations": count, "read": len(rows),
                                           "release": release}]
    for row in rows:
        scores = {str(x.get("id")): x.get("score") for x in row.get("datasourceScores") or []}
        disease = row.get("disease") or {}
        observations.append({
            "record": "association", "disease_id": disease.get("id"), "disease": disease.get("name"),
            "used": {k: v for k, v in sorted(scores.items()) if k in OT_SOURCES},
            "not_used": {k: v for k, v in sorted(scores.items()) if k not in OT_SOURCES}})
    limitations = [f"{source} is listed, never Evidence: {why}" for source, why in OT_NOT_USED.items()]
    limitations.append("only evidence annotated to the trait itself is read: a parent term does not stand for its "
                       "children")
    if not ids:
        limitations.append("no trait named: the gene's highest-scoring associations are listed, no Evidence")
    if len(rows) < count:
        limitations.append(f"read {len(rows)} of {count} associations")
    limitations += adapters._partial_notes(rec, "Open Targets")
    incomplete = bool(ids) and (len(rows) < count or bool(rec.partial))
    status = "incomplete" if incomplete else "records_found" if evidence else "no_records_found"
    if not ids:
        message = f"{gene}: {count} associations, the first {len(rows)} listed (no Evidence): name the traits"
    else:
        message = (f"{gene}: {len(evidence)} records for {len({e.data['disease_id'] for e in evidence})} of the "
                   f"{len(ids)} traits asked about; {count} of them have an association of any kind")
    return AdapterResult(
        retrieval_status=status, observations=observations,
        coverage=Coverage(requested_scope=f"Open Targets evidence linking {gene} to {len(ids)} trait(s)" if ids else
                          f"Open Targets associations of {gene}",
                          assessed_scope=f"{len(rows)} of {count} associations read", limitations=limitations),
        evidence=evidence, raw={"requests": rec.records(), "gene": gene, "gene_id": ensembl, "traits": ids,
                                "associations": rows, "release": release},
        dataset_release=release, message=message, cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- the registry the fill's runner uses ----------------------------------------------------------------------------

# --- adastra_asb ----------------------------------------------------------------------------------------------------

ADASTRA_API = "https://adastra.autosome.org/api/v6"
ADASTRA_RELEASE = "ADASTRA 6.1 (Mabel)"
ADASTRA_FDR = 0.05                 # ADASTRA's own threshold for calling allele-specific binding (its is_asb)
ADASTRA_NO_MOTIF = ("No Hit", None, "")
ADASTRA_ASB = ToolSpec(
    name="adastra_asb", route="computational",
    description=("ADASTRA's allele-specific binding calls at the variant: for each TF with ChIP-seq reads over it in "
                 "a heterozygous cell, whether the reads favour one allele."),
    variant_types=["SNV"], provider="ADASTRA (adastra.autosome.org)", dataset_release=ADASTRA_RELEASE,
    coverage_notes=("Only variants that some assayed cell is heterozygous for can be called, and only for the TFs "
                    "assayed in such a cell. No entry is not evidence that the alleles bind alike."),
    result_semantics=("records_found: one occupancy record per protein whose pooled ChIP-seq reads favour one allele "
                      "at 5% FDR, with the allele, whether the protein is a TF, and whether a TF's own motif agrees "
                      "as a limitation when it does not. no_records_found: the variant has no entry, or no protein "
                      "passed. A protein tested and not significant is an observation, never a record."),
    rate_policy="serial", evidence_classes=["occupancy"], network=True)


@lru_cache(maxsize=4)
def _uniprot_symbols(path: str) -> dict[str, str]:
    """UniProt accession -> approved HGNC symbol, for accessions the table gives to exactly one approved gene."""
    found: dict[str, set[str]] = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row.get("status") != "Approved":
                continue
            for accession in (row.get("uniprot_ids") or "").split("|"):
                if accession.strip():
                    found.setdefault(accession.strip().upper(), set()).add(row["symbol"].strip())
    return {accession: next(iter(symbols)) for accession, symbols in found.items() if len(symbols) == 1}


def _fdr(log_p: Any) -> float | None:
    """ADASTRA stores -log10 of the FDR-corrected p-value."""
    return None if log_p is None else float(10 ** -float(log_p))


def adastra_evidence(v: Any, row: dict[str, Any], symbol: str, about: list[str],
                     kind: str = proteins.UNKNOWN) -> Evidence | None:
    """One protein's pooled call as a record, or None when it does not pass on either allele. `kind` says whether
    the protein binds DNA by sequence (proteins.kind): a record of one that does not is flagged, and bears on the
    site's regulatory activity, not on a TF's binding."""
    fdr = {"ref": _fdr(row.get("log_p_value_ref")), "alt": _fdr(row.get("log_p_value_alt"))}
    sides = [side for side in ("ref", "alt") if fdr[side] is not None and fdr[side] <= ADASTRA_FDR]
    if not sides:
        return None
    base = {"ref": v.ref, "alt": v.alt}
    tf = row.get("transcription_factor") or {}
    motif = row.get("motif_concordance")
    cofactor = kind == proteins.NOT_TF
    limitations = ["pooled over the ChIP-seq experiments of this protein in every cell type ADASTRA holds, so it "
                   "names no cell type",
                   "called in cells heterozygous for the variant: another variant on the same haplotype, inside the "
                   "bound region, could cause the imbalance"]
    if cofactor:
        limitations.append(f"{symbol} does not bind DNA by sequence ({proteins.SOURCE}): the imbalance shows that "
                           "the state of the site differs between the alleles, and names no TF that reads the "
                           "variant")
    elif motif in ADASTRA_NO_MOTIF:
        limitations.append("ADASTRA finds no motif of this TF over the variant: the imbalance may follow another "
                           "factor bound at the site, so it does not show that this TF reads the variant")
    elif "discordant" in str(motif).casefold():
        limitations.append(f"the TF's own motif predicts the other allele (ADASTRA motif concordance: {motif}): the "
                           "imbalance may follow another factor bound at the site")
    if len(sides) == 2:
        limitations.append("called for both alleles, in different experiments: no single direction")
        allele, said = None, "favour each allele in some experiments"
    else:
        allele = base[sides[0]]
        other = base["alt" if sides[0] == "ref" else "ref"]
        said = f"favour the {allele} allele over {other} (FDR {fdr[sides[0]]:.2g})"
    return Evidence(
        origin="tool", access="dataset", evidence_class="occupancy",
        source_ids=[f"ADASTRA:{tf.get('uniprot_ac')}:chr{v.chrom}:{v.pos}:{v.ref}>{v.alt}"],
        observed_result=(f"{ADASTRA_RELEASE}: ChIP-seq reads of {symbol}"
                         f"{', which does not bind DNA itself,' if cofactor else ''} over {adapters._where(v)} "
                         f"{said}" + ("." if cofactor else f"; motif concordance: {motif or 'not given'}.")),
        data={"allele_specific": True, proteins.COFACTOR_FLAG: cofactor, "protein": kind, "source": "ADASTRA", "release": ADASTRA_RELEASE, "adastra_tf": tf.get("name"),
              "uniprot": tf.get("uniprot_ac"), "fdr_ref": fdr["ref"], "fdr_alt": fdr["alt"],
              "effect_size_ref": row.get("es_ref"), "effect_size_alt": row.get("es_alt"),
              "motif_concordance": motif, "tf_experiments": tf.get("experiments_count"), "assembly": "GRCh38"},
        allele=allele, direction="increases" if allele else "unspecified", about_tfs=[symbol], about_variants=about,
        independence_group=f"ADASTRA:{symbol}", limitations=limitations)


def adastra_asb(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return adapters._no_http(ctx.spec.name)
    v = ctx.case.variant
    rec = adapters._Recorder(ctx.http)
    url = f"{ADASTRA_API}/search/snps/advanced?chromosome=chr{v.chrom}&start={v.pos}&end={v.pos}"
    answer = rec.get(url)
    if not answer.ok or not isinstance(answer.data, dict):
        return adapters._failed(rec, "ADASTRA", answer)
    entries = [x for x in answer.data.get("results") or [] if isinstance(x, dict)]
    mine = [x for x in entries if x.get("position") == v.pos and str(x.get("ref")).upper() == v.ref
            and str(x.get("alt")).upper() == v.alt]
    path = ctx.config.path("data", "hgnc") if ctx.config is not None else None
    symbols = _uniprot_symbols(str(path)) if path is not None and path.exists() else {}
    about = adapters._case_names(ctx)
    tfs = proteins.tf_symbols(ctx.config)
    evidence: list[Evidence] = []
    observations: list[dict[str, Any]] = [{"record": "summary", "entries_at_position": len(entries),
                                           "entries_for_this_variant": len(mine), "release": ADASTRA_RELEASE}]
    observations += [{"record": "other_allele", "ref": x.get("ref"), "alt": x.get("alt"), "rs_id": x.get("rs_id")}
                     for x in entries if x not in mine]
    unnamed = 0
    for entry in mine:
        for row in entry.get("tf_aggregated_snps") or []:
            tf = row.get("transcription_factor") or {}
            symbol = symbols.get(str(tf.get("uniprot_ac") or "").upper())
            kind = proteins.kind(symbol, tfs)
            item = adastra_evidence(v, row, symbol, about, kind) if symbol else None
            passed = bool(row.get("is_asb"))
            unnamed += passed and not symbol
            observations.append({
                "record": "tf", "adastra_tf": tf.get("name"), "uniprot": tf.get("uniprot_ac"), "tf": symbol,
                "protein": kind, "passes_fdr": passed, "fdr_ref": _fdr(row.get("log_p_value_ref")),
                "fdr_alt": _fdr(row.get("log_p_value_alt")), "effect_size_ref": row.get("es_ref"),
                "effect_size_alt": row.get("es_alt"), "motif_concordance": row.get("motif_concordance"),
                "evidence": item is not None})
            if item is not None:
                evidence.append(item)
        observations += [{"record": "cell_type", "cell_type": (c.get("cell_line") or {}).get("name"),
                          "passes_fdr": bool(c.get("is_asb")), "fdr_ref": _fdr(c.get("log_p_value_ref")),
                          "fdr_alt": _fdr(c.get("log_p_value_alt"))} for c in entry.get("cl_aggregated_snps") or []]
    tested = sum(o["record"] == "tf" for o in observations)
    limitations = ["ADASTRA can only call a variant in cells that are heterozygous for it and were assayed for the "
                   "protein: no entry, or a protein that did not pass, is not evidence that the alleles bind alike"]
    if unnamed:
        limitations.append(f"{unnamed} protein(s) passed and have no single HGNC symbol for their UniProt "
                           "accession, so they are listed and not counted")
    return AdapterResult(
        retrieval_status="records_found" if evidence else "no_records_found", observations=observations,
        coverage=Coverage(requested_scope=f"ADASTRA allele-specific binding at {adapters._where(v)}",
                          assessed_scope=f"{tested} protein(s) tested there, {len(evidence)} favouring one allele at "
                                         f"{ADASTRA_FDR:g} FDR", limitations=limitations),
        evidence=evidence, raw={"requests": rec.records(), "results": entries, "release": ADASTRA_RELEASE},
        dataset_release=ADASTRA_RELEASE, assembly="GRCh38",
        message=(f"{len(evidence)} of {tested} proteins tested favour one allele" if mine else
                 "the variant has no ADASTRA entry"),
        cached=rec.cached, retrieval_time=rec.retrieval_time())


CODE_TOOLS: tuple[tuple[ToolSpec, Any], ...] = (
    (TF_OCCUPANCY_SET, tf_occupancy_set), (TF_EXPRESSION_SET, tf_expression_set),
    (CREDIBLE_SETS_ALL, credible_sets_all), (GENE_DISEASE, gene_disease), (ADASTRA_ASB, adastra_asb))
CODE_TOOL_NAMES: tuple[str, ...] = tuple(spec.name for spec, _ in CODE_TOOLS)


def registry() -> ToolRegistry:
    """Every default tool (adapters and literature, registered on import) plus the code-only tools, in a registry of
    its own: the default one, and so what a role is shown, is not changed."""
    out = ToolRegistry()
    for name in REGISTRY.names():
        out.register(REGISTRY.spec(name), REGISTRY.adapter(name))
    for spec, adapter in CODE_TOOLS:
        out.register(spec, adapter)
    return out


def allowed(config_allowlist: list[str] | None) -> list[str] | None:
    """The config's tool allowlist with the code-only tools added (None: every tool)."""
    return None if config_allowlist is None else [*config_allowlist, *CODE_TOOL_NAMES]
