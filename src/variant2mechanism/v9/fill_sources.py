"""Sources added in the second version of the fill (24 Nov 2026): each is asked by code, and no model role sees one.

    udacha_asa          UDACHA: allele-specific chromatin accessibility called at the variant, per cell type
    mavedb_reporter     MaveDB: saturation-mutagenesis reporter assays that measured this exact substitution
    protein_qtl_sets    Open Targets: credible sets of protein QTLs holding the variant
    tumour_recurrence   cBioPortal: tumours of one sequenced cohort that carry this exact mutation, by cancer type
    litvar_search       LitVar and PubTator (NCBI): articles that name the variant under any spelling
    litvar_mentions     the spellings one article uses for the variant, as NCBI's text mining marks them

Why these and no more: one or two sources per kind of record, each from a public institute, a consortium or the
field's own repository, and each filling a cell that had none or a step the chain did not have. They are registered
with the other code-only tools (fill_tools.CODE_TOOLS), so the tools a role is shown, and every saved prompt, stay
as they are.

udacha_asa reads UDACHA, the chromatin-accessibility counterpart of ADASTRA (the same group and the same statistics):
DNase-seq, ATAC-seq and FAIRE-seq reads over a variant in cells heterozygous for it, pooled per cell type.
- A record says that the state of the site differs between the alleles in that cell type. It names no protein, so it
  bears on "the two alleles differ in the regulatory activity of the site" and on no TF's binding. The class matrix
  has no class of its own for accessibility; the record is filed as reads over a site in cells (occupancy) with its
  own flag, which the matrix lets count for that one claim (schemas.QUALIFIED_DIRECT_FILL).
- One record per cell type and assay whose call passes 5% FDR on one allele: the level the ADASTRA source uses.
  UDACHA's own flag is set at 10%; a call between the two is listed and is never a record.
- A variant with no entry is "nothing found", never evidence that the alleles are alike: only a variant that some
  assayed cell is heterozygous for can be called.
- The call compares two haplotypes, so another variant inside the accessible region could cause it; every record
  says so. Effect sizes and FDR values are kept in `data` and never read by anything that orders a chain.

mavedb_reporter reads MaveDB, where multiplexed assays of variant effect are deposited. A saturation-mutagenesis
reporter assay of a regulatory element measured every single-base change in it, so when the variant lies in such an
element the exact substitution has a measurement.
- The variant is looked up by its ClinGen allele identifier (the ClinGen Allele Registry gives it for the
  substitution written in HGVS); MaveDB lists the measurements of that allele.
- Only score sets of a regulatory element are read (a protein's deep mutational scan measures something else).
- A record needs the set's own p-value below 1e-5 and at least ten barcodes: the significance level and the
  inclusion rule of the study that deposited these sets (PubMed 31395865). A measurement that does not pass is
  listed and is no record: at that level, "not significant" is not a measured absence.
- A record states no direction. The set gives a log2 effect for the substitution against its own target sequence,
  which need not carry the reference allele; the number is kept as the set records it.
- Replicates of one experiment share an independence group, so two libraries of one study are one observation.

protein_qtl_sets asks Open Targets, with the client the fill already uses, for the credible sets of protein QTLs
that hold the variant. Open Targets says of each whether the protein is encoded near the signal (cis) or elsewhere.
- A cis set is a record that the alleles differ in the level of that gene's protein: the same kind of record as an
  eQTL credible set, one step later. It bears on the target-gene step.
- A trans set is listed and is never a record: it says the locus matters to a protein encoded elsewhere, not that
  the gene is this variant's target (the reason table.py gives for leaving protein QTLs out of colocalisations).
- Plasma is where the protein was measured, not where the variant acts; and an antibody- or aptamer-based assay can
  read a changed protein as a changed level. Every record says both.

tumour_recurrence asks cBioPortal for the tumours of one cohort (MSK-IMPACT 2017, 10,945 tumours sequenced with a
gene panel) that carry this exact substitution, in the genes the variant's annotation names.
- The cohort is on GRCh37, so the tool needs the variant's GRCh37 placement, which the annotation records for a
  variant with an rsID; without one it does not apply.
- One record per cancer type in which the mutation was called in the tumours of at least two patients. A count is
  not a test: no background mutation rate is modelled, and the record says so. The counts are kept in `data` and
  never read by anything that orders a chain.
- An inherited variant is filtered out of somatic calls, so for one this returns nothing, which says nothing.

litvar_search and litvar_mentions serve the reader (reader.py). LitVar normalises the ways articles write a variant
(an rsID, an HGVS name, a shorthand) to one entry; PubTator, the text-mining service LitVar is built on, serves the
search over those entries and the marked-up text of each article. A list of papers and a list of spellings are
pointers: neither is Evidence, and neither says that an article's name is this variant. What an article's name means
is still decided by the literature route's own checks.
"""

import csv
import re
from collections import Counter
from functools import lru_cache
from typing import Any
from urllib.parse import quote

from ..context import genetics
from . import adapters, variant_identity
from .proteins import ACCESSIBILITY_FLAG
from .qbic_reader import reader_for
from .schemas import Coverage, Evidence
from .tools import AdapterResult, ParamSpec, ToolContext, ToolSpec

FDR_5 = 0.05
SAME_HAPLOTYPE = ("called in cells heterozygous for the variant: another variant on the same haplotype, inside the "
                  "region, could cause the imbalance")


def _unique(values: Any) -> list[Any]:
    return list(dict.fromkeys(v for v in values if v))


def _fdr(log_p: Any) -> float | None:
    """The FDR-corrected p-value from its -log10, as ADASTRA and UDACHA store it."""
    return None if log_p is None else float(10 ** -float(log_p))


def _release(meta: dict[str, Any] | None) -> str | None:
    dv, api = (meta or {}).get("dataVersion") or {}, (meta or {}).get("apiVersion") or {}
    return (f"Open Targets Platform {dv.get('year')}.{dv.get('month')} (API {api.get('x')}.{api.get('y')}."
            f"{api.get('z')})") if dv else None


# --- udacha_asa -----------------------------------------------------------------------------------------------------

UDACHA_API = "https://udacha.autosome.org/api/v5"
UDACHA_RELEASE = "UDACHA (API v5)"
UDACHA_ASSAYS: tuple[tuple[str, str], ...] = (
    ("dnase_aggregated_snps", "DNase-seq"), ("atac_aggregated_snps", "ATAC-seq"),
    ("faire_aggregated_snps", "FAIRE-seq"))
UDACHA_ASA = ToolSpec(
    name="udacha_asa", route="computational",
    description=("UDACHA's allele-specific chromatin accessibility calls at the variant: for each cell type with "
                 "DNase-seq, ATAC-seq or FAIRE-seq reads over it in a heterozygous cell, whether the reads favour one "
                 "allele."),
    variant_types=["SNV"], provider="UDACHA (udacha.autosome.org)", dataset_release=UDACHA_RELEASE,
    coverage_notes=("Only variants that some assayed cell is heterozygous for can be called. No entry is not evidence "
                    "that the alleles are alike."),
    result_semantics=("records_found: one record per cell type and assay whose pooled reads favour one allele at 5% "
                      "FDR, with the allele. no_records_found: the variant has no entry, or no cell type passed. A "
                      "cell type tested and not past 5% is an observation, never a record."),
    rate_policy="serial", evidence_classes=["occupancy"], network=True)


def udacha_evidence(v: Any, row: dict[str, Any], assay: str, about: list[str]) -> Evidence | None:
    """One cell type's pooled call for one assay as a record, or None when it does not pass 5% FDR on either allele."""
    fdr = {"ref": _fdr(row.get("log_p_value_ref")), "alt": _fdr(row.get("log_p_value_alt"))}
    sides = [side for side in ("ref", "alt") if fdr[side] is not None and fdr[side] <= FDR_5]
    if not sides:
        return None
    cell = row.get("cell_line") or {}
    name = " ".join(str(cell.get("name") or "").split()) or "an unnamed cell type"
    base = {"ref": v.ref, "alt": v.alt}
    limitations = [SAME_HAPLOTYPE,
                   "reads of open chromatin name no protein: the record shows that the state of the site differs "
                   "between the alleles, not which TF reads the variant"]
    if len(sides) == 2:
        limitations.append("called for both alleles, in different experiments: no single direction")
        allele, said = None, "favour each allele in some experiments"
    else:
        allele = base[sides[0]]
        other = base["alt" if sides[0] == "ref" else "ref"]
        said = f"favour the {allele} allele over {other} (FDR {fdr[sides[0]]:.2g})"
    return Evidence(
        origin="tool", access="dataset", evidence_class="occupancy",
        source_ids=[f"UDACHA:{assay}:{cell.get('cl_id')}:chr{v.chrom}:{v.pos}:{v.ref}>{v.alt}"],
        observed_result=f"{UDACHA_RELEASE}: {assay} reads over {adapters._where(v)} in {name} {said}.",
        data={"allele_specific": True, ACCESSIBILITY_FLAG: True, "source": "UDACHA", "release": UDACHA_RELEASE,
              "assay": assay, "cell_type": name, "fdr_ref": fdr["ref"], "fdr_alt": fdr["alt"],
              "effect_size_ref": row.get("es_ref"), "effect_size_alt": row.get("es_alt"),
              "experiments": cell.get("experiments_count"), "assembly": "GRCh38"},
        allele=allele, direction="increases" if allele else "unspecified", context=adapters._context(name, v),
        about_variants=about, independence_group=f"UDACHA:{assay}:{name}", limitations=limitations)


def udacha_asa(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return adapters._no_http(ctx.spec.name)
    v = ctx.case.variant
    rec = adapters._Recorder(ctx.http)
    answer = rec.get(f"{UDACHA_API}/search/snps/advanced?chromosome=chr{v.chrom}&start={v.pos}&end={v.pos}")
    if not answer.ok or not isinstance(answer.data, dict):
        return adapters._failed(rec, "UDACHA", answer)
    entries = [x for x in answer.data.get("results") or [] if isinstance(x, dict)]
    mine = [x for x in entries if x.get("position") == v.pos and str(x.get("ref")).upper() == v.ref
            and str(x.get("alt")).upper() == v.alt]
    about = adapters._case_names(ctx)
    evidence: list[Evidence] = []
    observations: list[dict[str, Any]] = [{"record": "summary", "entries_at_position": len(entries),
                                           "entries_for_this_variant": len(mine), "release": UDACHA_RELEASE}]
    observations += [{"record": "other_allele", "ref": x.get("ref"), "alt": x.get("alt"), "rs_id": x.get("rs_id")}
                     for x in entries if x not in mine]
    for entry in mine:
        for field, assay in UDACHA_ASSAYS:
            for row in entry.get(field) or []:
                item = udacha_evidence(v, row, assay, about)
                observations.append({
                    "record": "cell_type", "assay": assay, "cell_type": (row.get("cell_line") or {}).get("name"),
                    "passes_fdr_5": item is not None, "passes_fdr_10": bool(row.get("is_asb")),
                    "fdr_ref": _fdr(row.get("log_p_value_ref")), "fdr_alt": _fdr(row.get("log_p_value_alt")),
                    "effect_size_ref": row.get("es_ref"), "effect_size_alt": row.get("es_alt"),
                    "evidence": item is not None})
                if item is not None:
                    evidence.append(item)
    tested = sum(o["record"] == "cell_type" for o in observations)
    return AdapterResult(
        retrieval_status="records_found" if evidence else "no_records_found", observations=observations,
        coverage=Coverage(
            requested_scope=f"UDACHA allele-specific chromatin accessibility at {adapters._where(v)}",
            assessed_scope=f"{tested} cell type and assay pair(s) tested there, {len(evidence)} favouring one allele "
                           f"at {FDR_5:g} FDR",
            limitations=["UDACHA can only call a variant in cells that are heterozygous for it: no entry, or a cell "
                         "type that did not pass, is not evidence that the alleles are alike"]),
        evidence=evidence, raw={"requests": rec.records(), "results": entries, "release": UDACHA_RELEASE},
        dataset_release=UDACHA_RELEASE, assembly="GRCh38",
        message=(f"{len(evidence)} of {tested} cell type and assay pairs favour one allele" if mine else
                 "the variant has no UDACHA entry"),
        cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- mavedb_reporter ------------------------------------------------------------------------------------------------

CLINGEN_API = "https://reg.clinicalgenome.org/allele"
MAVEDB_API = "https://api.mavedb.org/api/v1"
MAVE_P = 1e-5                      # the significance level of the study behind the regulatory sets (PubMed 31395865)
MAVE_MIN_TAGS = 10                 # its inclusion rule: at least ten barcodes for a variant
MAVE_READ = 12                     # measurements read for one allele
REFSEQ_GRCH38: dict[str, str] = {
    "1": "NC_000001.11", "2": "NC_000002.12", "3": "NC_000003.12", "4": "NC_000004.12", "5": "NC_000005.10",
    "6": "NC_000006.12", "7": "NC_000007.14", "8": "NC_000008.11", "9": "NC_000009.12", "10": "NC_000010.11",
    "11": "NC_000011.10", "12": "NC_000012.12", "13": "NC_000013.11", "14": "NC_000014.9", "15": "NC_000015.10",
    "16": "NC_000016.10", "17": "NC_000017.11", "18": "NC_000018.10", "19": "NC_000019.10", "20": "NC_000020.11",
    "21": "NC_000021.9", "22": "NC_000022.11", "X": "NC_000023.11", "Y": "NC_000024.10"}
_CELLS = re.compile(r"\bin ([A-Za-z0-9][A-Za-z0-9./-]{1,24}) cells\b")
MAVEDB_REPORTER = ToolSpec(
    name="mavedb_reporter", route="computational",
    description=("MaveDB's saturation-mutagenesis reporter assays of regulatory elements that measured this exact "
                 "substitution: the effect on reporter activity, with the set's own p-value."),
    variant_types=["SNV"], provider="MaveDB (mavedb.org), through the ClinGen Allele Registry",
    dataset_release="MaveDB (version read at retrieval is not recorded by its API)",
    coverage_notes=("Only variants inside an element that someone mutagenised and deposited: about twenty well-known "
                    "elements. No measurement is not evidence that the alleles are alike."),
    result_semantics=("records_found: one reporter_assay record per score set of a regulatory element that measured "
                      "the substitution with p below 1e-5 and at least ten barcodes. no_records_found: no allele id, "
                      "no measurement, or none past that level. A measurement that does not pass is an observation, "
                      "never a record."),
    rate_policy="serial", evidence_classes=["reporter_assay"], network=True)


def hgvs_g(v: Any) -> str | None:
    """The substitution in HGVS on the GRCh38 chromosome's RefSeq sequence, or None for a chromosome without one."""
    accession = REFSEQ_GRCH38.get(str(v.chrom).upper())
    return f"{accession}:g.{v.pos}{v.ref}>{v.alt}" if accession else None


def _p_words(p: float) -> str:
    return "below the smallest number the set stores" if p <= 0 else f"{p:.1e}"


def mavedb_evidence(v: Any, measurement: dict[str, Any], detail: dict[str, Any], score_set: dict[str, Any],
                    caid: str, about: list[str]) -> tuple[Evidence | None, str]:
    """One measurement as a record, or None with the reason it is none: the set is not of a regulatory element, it
    stores no p-value, or the measurement does not pass the study's own level and inclusion rule."""
    targets = [t for t in score_set.get("targetGenes") or [] if isinstance(t, dict)]
    if not any(str(t.get("category") or "").casefold() == "regulatory" for t in targets):
        return None, "the score set is not of a regulatory element"
    scores = detail.get("scores") or {}
    score, p, tags = (adapters._number(scores.get(k)) for k in ("score", "p-value", "unique_tags"))
    if score is None or p is None:
        return None, "the set stores no score or no p-value for it"
    if tags is not None and tags < MAVE_MIN_TAGS:
        return None, f"{tags:g} barcodes, fewer than the {MAVE_MIN_TAGS} the study needs to include a variant"
    if p >= MAVE_P:
        return None, f"p {p:.2g}, not below the study's significance level of {MAVE_P:g}"
    urn, set_urn = str(measurement.get("variantUrn") or ""), str(measurement.get("scoreSetUrn") or "")
    title = " ".join(str(score_set.get("title") or measurement.get("scoreSetTitle") or "").split())
    target = ", ".join(_unique(str(t.get("name") or "") for t in targets)) or "a regulatory element"
    pmids = [f"PMID:{x['identifier']}" for x in score_set.get("primaryPublicationIdentifiers") or []
             if isinstance(x, dict) and str(x.get("dbName")) == "PubMed" and x.get("identifier")]
    cells = _CELLS.search(str(score_set.get("shortDescription") or ""))
    where = cells.group(1) if cells else ""
    experiment = set_urn.rsplit("-", 2)[0] if set_urn.count("-") >= 2 else set_urn
    return Evidence(
        origin="tool", access="dataset", evidence_class="reporter_assay",
        source_ids=[f"MaveDB:{urn}", *pmids],
        observed_result=(f"MaveDB {set_urn} ({title}): a saturation-mutagenesis reporter assay of {target}"
                         + (f" in {where} cells" if where else "")
                         + f" measured {adapters._where(v)} with a log2 effect of {score:+.2f} on reporter activity "
                         f"(p {_p_words(p)}" + (f"; {tags:g} barcodes" if tags is not None else "") + ")."),
        data={"source": "MaveDB", "score_set": set_urn, "variant_urn": urn, "title": title, "target": target,
              "score": score, "p_value": p, "unique_tags": tags, "clingen_allele_id": caid, "cells": where or None,
              "licence": ((score_set.get("license") or {}).get("shortName")), "assembly": "GRCh38"},
        context=adapters._context(where, v) if where else None, about_variants=about,
        independence_group=f"MaveDB:{experiment}",
        limitations=["an episomal reporter" + (f" in {where} cells" if where else "") + ": not the endogenous locus",
                     "the log2 effect is the set's own, for the substitution against the sequence the study "
                     "mutagenised, which need not carry the reference allele: no direction is read from it"]), ""


def mavedb_reporter(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return adapters._no_http(ctx.spec.name)
    v = ctx.case.variant
    name = hgvs_g(v)
    if name is None:
        return AdapterResult(execution_status="not_applicable",
                             message=f"chromosome {v.chrom} has no RefSeq accession on file, so no allele id was asked")
    rec = adapters._Recorder(ctx.http)
    coverage = Coverage(requested_scope=f"MaveDB reporter assays that measured {adapters._where(v)}",
                        limitations=["MaveDB holds only elements someone mutagenised and deposited: no measurement "
                                     "is not evidence that the alleles are alike"])
    registry = rec.get(f"{CLINGEN_API}?hgvs={quote(name, safe='')}")
    found = registry.data if registry.ok and isinstance(registry.data, dict) else None
    caid = str((found or {}).get("@id") or "").rsplit("/", 1)[-1]
    observations: list[dict[str, Any]] = [{"record": "allele", "hgvs": name, "clingen_allele_id": caid or None}]
    if found is None and registry.status not in (400, 404):
        return adapters._failed(rec, "the ClinGen Allele Registry", registry, observations)
    if not re.fullmatch(r"CA\d+", caid):
        coverage.assessed_scope = "the ClinGen Allele Registry has no identifier for this substitution"
        return AdapterResult(retrieval_status="no_records_found", observations=observations, coverage=coverage,
                             raw={"requests": rec.records()}, cached=rec.cached, retrieval_time=rec.retrieval_time(),
                             message="no ClinGen allele identifier, so MaveDB holds no measurement under one")
    listed = rec.get(f"{MAVEDB_API}/clingen-alleles/{caid}/measurements")
    if not listed.ok or not isinstance(listed.data, list):
        if listed.status == 404:
            coverage.assessed_scope = f"MaveDB lists no measurement of {caid}"
            return AdapterResult(retrieval_status="no_records_found", observations=observations, coverage=coverage,
                                 raw={"requests": rec.records()}, cached=rec.cached,
                                 retrieval_time=rec.retrieval_time(), message=f"MaveDB lists no measurement of {caid}")
        return adapters._failed(rec, "MaveDB", listed, observations)
    direct = [m for m in listed.data if isinstance(m, dict) and m.get("isCurrent") is not False
              and m.get("relationship") == "direct" and m.get("assayLevel") == "genomic"
              and m.get("assayLevelHgvs") == name]
    about = adapters._case_names(ctx)
    evidence: list[Evidence] = []
    sets: dict[str, dict[str, Any]] = {}
    details: list[dict[str, Any]] = []
    for m in direct[:MAVE_READ]:
        urn, set_urn = str(m.get("variantUrn") or ""), str(m.get("scoreSetUrn") or "")
        detail = rec.get(f"{MAVEDB_API}/variants/{quote(urn, safe=':')}")
        if set_urn not in sets:
            answer = rec.get(f"{MAVEDB_API}/score-sets/{quote(set_urn, safe=':')}")
            sets[set_urn] = answer.data if answer.ok and isinstance(answer.data, dict) else {}
        if not detail.ok or not isinstance(detail.data, dict) or not sets[set_urn]:
            observations.append({"record": "measurement", "variant_urn": urn, "score_set": set_urn, "evidence": False,
                                 "why": "its detail or its score set could not be read"})
            continue
        details.append(detail.data)
        item, why = mavedb_evidence(v, m, detail.data, sets[set_urn], caid, about)
        scores = detail.data.get("scores") or {}
        observations.append({"record": "measurement", "variant_urn": urn, "score_set": set_urn,
                             "title": m.get("scoreSetTitle"), "score": scores.get("score"),
                             "p_value": scores.get("p-value"), "unique_tags": scores.get("unique_tags"),
                             "evidence": item is not None, "why": why})
        if item is not None:
            evidence.append(item)
    read = sum(o["record"] == "measurement" for o in observations)
    unread = [o for o in observations if o["record"] == "measurement" and "could not be read" in str(o.get("why"))]
    coverage.assessed_scope = (f"{len(listed.data)} measurement(s) of {caid} listed, {len(direct)} of this exact "
                               f"substitution on the genome, {read} read, {len(evidence)} past the study's level")
    if len(direct) > MAVE_READ:
        coverage.limitations.append(f"read the first {MAVE_READ} of {len(direct)} measurements")
    incomplete = bool(unread) or len(direct) > MAVE_READ
    return AdapterResult(
        retrieval_status="incomplete" if incomplete else "records_found" if evidence else "no_records_found",
        observations=observations, coverage=coverage, evidence=evidence,
        raw={"requests": rec.records(), "allele": caid, "measurements": listed.data, "details": details,
             "score_sets": {k: {f: s.get(f) for f in ("urn", "title", "shortDescription", "targetGenes",
                                                       "primaryPublicationIdentifiers", "license", "publishedDate")}
                            for k, s in sets.items()}},
        assembly="GRCh38", message=f"{len(evidence)} of {read} measurement(s) read pass the study's level",
        cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- protein_qtl_sets -----------------------------------------------------------------------------------------------

PQTL_PAGE, PQTL_MAX_PAGES = 50, 5
PQTL_QUERY = """query V2MProteinQtl($v: String!, $ids: [String!]!, $index: Int!) {
  meta { apiVersion { x y z } dataVersion { year month } }
  variant(variantId: $v) {
    id
    credibleSets(page: {index: $index, size: %d}, studyTypes: [pqtl]) {
      count
      rows {
        studyLocusId studyId isTransQtl finemappingMethod confidence variant { id }
        study { id projectId traitFromSource nSamples pubmedId target { id approvedSymbol }
                biosample { biosampleName } }
        locus(variantIds: $ids, page: {index: 0, size: 1}) {
          rows { variant { id } posteriorProbability is95CredibleSet is99CredibleSet beta } }
      }
    }
  }
}""" % PQTL_PAGE
PROTEIN_QTL_SETS = ToolSpec(
    name="protein_qtl_sets", route="computational",
    description=("Open Targets credible sets of protein QTLs holding the variant: for a protein encoded near the "
                 "signal (cis), the variant's PIP; proteins encoded elsewhere (trans) are listed."),
    variant_types=["SNV"], provider="Open Targets Platform GraphQL",
    dataset_release="Open Targets Platform (release read from meta at retrieval)",
    coverage_notes=("Protein levels measured in blood plasma for the most part: where the protein was measured, not "
                    "where the variant acts. Open Targets' own call says whether a set is cis or trans."),
    result_semantics=("records_found: one statistical_inference record per cis credible set, about the gene whose "
                      "protein was measured. no_records_found: no credible set of a protein QTL holds the variant, or "
                      "only trans sets do. A trans set is an observation, never a record."),
    rate_policy="serial", evidence_classes=["statistical_inference"], network=True)


def pqtl_evidence(row: dict[str, Any], vid: str, release: str, symbol: str, v: Any, about: list[str]) -> Evidence:
    """One cis credible set as a record about the gene whose protein was measured."""
    study = row.get("study") or {}
    sid, lead = row.get("studyLocusId"), (row.get("variant") or {}).get("id")
    locus = adapters._pip(row, vid)
    pip = locus.get("posteriorProbability")
    biosample = ((study.get("biosample") or {}).get("biosampleName")) or ""
    method = (f"{row.get('finemappingMethod')}: {row.get('confidence')}" if row.get("finemappingMethod") else
              "method not recorded")
    sources = [f"OT:{sid}"] + ([f"PMID:{study['pubmedId']}"] if study.get("pubmedId") else [])
    return Evidence(
        origin="tool", access="dataset", evidence_class="statistical_inference", source_ids=sources,
        observed_result=(f"Open Targets ({release}): {vid} is in a credible set of a protein QTL for the {symbol} "
                         f"protein, encoded near the signal, in {biosample or 'an unstated biosample'} "
                         f"({study.get('projectId')}; {method}" + (f"; lead variant {lead}" if lead else "") + ")"
                         + (f" with posterior inclusion probability {pip:.3g}." if pip is not None else ".")),
        data={"study_locus_id": sid, "study_id": study.get("id"), "qtl_type": "pqtl", "cis": True, "pip": pip,
              "in_95_set": locus.get("is95CredibleSet"), "in_99_set": locus.get("is99CredibleSet"),
              "variant_beta": locus.get("beta"), "lead_variant": lead, "project": study.get("projectId"),
              "n_samples": study.get("nSamples"), "gene": symbol, "gene_id": (study.get("target") or {}).get("id"),
              "biosample": biosample or None, "release": release},
        context=adapters._context(biosample, v) if biosample else None, about_genes=[symbol], about_variants=about,
        independence_group=f"PQTL-STUDY:{study.get('id') or sid}",
        limitations=[f"the protein's level in {biosample or 'the biosample'}: not the gene's RNA, and not the tissue "
                     "where the variant acts",
                     "an antibody- or aptamer-based assay can read a changed protein as a changed level",
                     "a credible set holds every variant the signal could be: the PIP is this variant's share"])


def protein_qtl_sets(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return adapters._no_http(ctx.spec.name)
    v = ctx.case.variant
    vid = f"{v.chrom}_{v.pos}_{v.ref}_{v.alt}"
    rec = adapters._Recorder(ctx.http)
    rows: list[dict[str, Any]] = []
    count, release = 0, None
    for index in range(PQTL_MAX_PAGES):
        r = rec.query(genetics.OT, {"query": PQTL_QUERY, "variables": {"v": vid, "ids": [vid], "index": index}})
        data = (r.data or {}).get("data") if r.ok and isinstance(r.data, dict) else None
        if data is None:
            if index == 0:
                return adapters._failed(rec, "Open Targets", r)
            rec.partial.append(f"protein-QTL page {index} failed: {r.error or 'no data'}")
            break
        release = _release(data.get("meta")) or release
        sets = ((data.get("variant") or {}).get("credibleSets") or {})
        count = int(sets.get("count") or 0)
        rows += sets.get("rows") or []
        if len(rows) >= count or not sets.get("rows"):
            break
    release = release or "release not recorded"
    reg = reader_for(adapters._config(ctx)).registry
    about = adapters._case_names(ctx)
    evidence: list[Evidence] = []
    observations: list[dict[str, Any]] = [{"record": "summary", "credible_sets": count, "read": len(rows),
                                           "release": release}]
    for row in rows:
        study = row.get("study") or {}
        target = study.get("target") or {}
        symbol = adapters._gene_symbol(reg, str(target.get("approvedSymbol") or ""), target.get("id")) \
            if target.get("approvedSymbol") else ""
        cis = row.get("isTransQtl") is False
        measured_in = (study.get("biosample") or {}).get("biosampleName")
        # a claim about a protein's level is scoped to where it was measured, so a set that names no biosample is
        # listed and states nothing
        item = pqtl_evidence(row, vid, release, symbol, v, about) if cis and symbol and measured_in else None
        observations.append({
            "record": "set", "study_locus_id": row.get("studyLocusId"), "study_id": study.get("id"),
            "protein_of": symbol or None, "trans": row.get("isTransQtl"), "project": study.get("projectId"),
            "biosample": (study.get("biosample") or {}).get("biosampleName"),
            "pip": adapters._pip(row, vid).get("posteriorProbability"), "evidence": item is not None})
        if item is not None:
            evidence.append(item)
    trans = sum(o["record"] == "set" and o["trans"] is True for o in observations)
    limitations = ["a trans set (the protein is encoded elsewhere) is listed and is never a record: it does not say "
                   "that the gene is this variant's target"]
    if len(rows) < count:
        limitations.append(f"read {len(rows)} of {count} credible sets")
    limitations += adapters._partial_notes(rec, "Open Targets")
    incomplete = len(rows) < count or bool(rec.partial)
    return AdapterResult(
        retrieval_status="incomplete" if incomplete and (rows or count) else
        "records_found" if evidence else "no_records_found",
        observations=observations,
        coverage=Coverage(requested_scope=f"every Open Targets credible set of a protein QTL containing {vid}",
                          assessed_scope=f"{len(rows)} of {count} read: {len(evidence)} cis, {trans} trans",
                          limitations=limitations),
        evidence=evidence, raw={"requests": rec.records(), "credible_sets": rows, "release": release},
        dataset_release=release,
        message=f"{len(evidence)} cis and {trans} trans protein-QTL credible set(s) hold the variant",
        cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- tumour_recurrence ----------------------------------------------------------------------------------------------

CBIO_API = "https://www.cbioportal.org/api"
CBIO_STUDY = "msk_impact_2017"
CBIO_COHORT = "the MSK-IMPACT 2017 cohort"
CBIO_PMID = "PMID:28481359"
CBIO_GENES = 5                     # genes of the variant's annotation asked about
CBIO_MIN_PATIENTS = 2              # recurrent: called in the tumours of more than one patient
TUMOUR_RECURRENCE = ToolSpec(
    name="tumour_recurrence", route="computational",
    description=("cBioPortal: the tumours of one sequenced cohort (MSK-IMPACT 2017) that carry this exact "
                 "substitution, counted by cancer type."),
    variant_types=["SNV"], provider="cBioPortal (cbioportal.org)", dataset_release="cBioPortal, study msk_impact_2017",
    coverage_notes=("A gene panel reads only the regions it targets, and inherited variants are filtered out of "
                    "somatic calls: nothing found says nothing. The cohort is on GRCh37."),
    result_semantics=("records_found: one association record per cancer type in which the mutation was called in the "
                      "tumours of at least two patients, with the counts. no_records_found: the mutation was not "
                      "called, or in one patient per cancer type at most. A count is not a test."),
    rate_policy="serial", evidence_classes=["association"], network=True)


@lru_cache(maxsize=4)
def _entrez_ids(path: str) -> dict[str, int]:
    """Approved HGNC symbol (upper case) -> Entrez gene id."""
    found: dict[str, int] = {}
    with open(path, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row.get("status") == "Approved" and (row.get("entrez_id") or "").strip().isdigit():
                found[row["symbol"].strip().upper()] = int(row["entrez_id"])
    return found


def grch37_placement(graph: Any) -> dict[str, Any] | None:
    """The case variant's one GRCh37 placement, as the annotation recorded it (variant_identity.mappings)."""
    rows = [row for _, row in variant_identity.mappings(graph) if row.get("assembly") == "GRCh37"]
    return rows[0] if len(rows) == 1 else None


def recurrence_evidence(v: Any, place: dict[str, Any], gene: str, cancer_type: str, patients: int, sequenced: int,
                        kind: str, about: list[str]) -> Evidence:
    where37 = f"chr{place['chrom']}:{place['pos']} {place['ref']}>{place['alt']}"
    return Evidence(
        origin="tool", access="dataset", evidence_class="association",
        source_ids=[f"cBioPortal:{CBIO_STUDY}:{gene}:{place['chrom']}:{place['pos']}:{place['ref']}>{place['alt']}:"
                    f"{cancer_type}", CBIO_PMID],
        observed_result=(f"cBioPortal, {CBIO_COHORT}: the somatic mutation {adapters._where(v)} (GRCh37 {where37}; "
                         f"{gene}" + (f", {kind}" if kind else "") + f") was called in the tumours of {patients} of "
                         f"{sequenced} patients with {cancer_type}."),
        data={"source": "cBioPortal", "study": CBIO_STUDY, "gene": gene, "cancer_type": cancer_type,
              "patients_with_mutation": patients, "patients_sequenced": sequenced,
              "share": patients / sequenced if sequenced else None, "grch37": where37, "mutation_type": kind or None},
        about_traits=[cancer_type], about_variants=about,
        independence_group=f"cBioPortal:{CBIO_STUDY}:{cancer_type}",
        limitations=["a count among the sequenced tumours of that type: no background mutation rate is modelled, and "
                     "nothing is compared with normal tissue",
                     "a gene panel at one cancer centre: the regions it targets, in the patients it saw",
                     "somatic: the mutation recurs in tumours; it does not say that an inherited allele raises risk"])


def tumour_recurrence(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return adapters._no_http(ctx.spec.name)
    v = ctx.case.variant
    if ctx.case.origin == "germline":
        return AdapterResult(execution_status="not_applicable",
                             message="the request gives the variant as inherited: a somatic cohort does not call it")
    place = grch37_placement(ctx.graph) if ctx.graph is not None else None
    if place is None:
        return AdapterResult(execution_status="not_applicable",
                             message="no single GRCh37 placement of the variant is on file (the annotation records "
                                     "one for a variant with an rsID), and the cohort is on GRCh37")
    calls = [t for t in ctx.graph.tool_calls.values() if t.tool_name == "variant_annotation"]
    genes = _unique(g for t in calls for g in adapters._consequence_genes(t))
    path = ctx.config.path("data", "hgnc") if ctx.config is not None else None
    entrez = _entrez_ids(str(path)) if path is not None and path.exists() else {}
    asked = [(g, entrez[g.upper()]) for g in genes if g.upper() in entrez][:CBIO_GENES]
    if not asked:
        return AdapterResult(execution_status="not_applicable",
                             message="the variant's annotation names no gene with an Entrez id to ask the cohort by")
    rec = adapters._Recorder(ctx.http)
    profile, samples = f"{CBIO_STUDY}_mutations", f"{CBIO_STUDY}_all"
    hits: list[tuple[str, dict[str, Any]]] = []
    observations: list[dict[str, Any]] = []
    for gene, gene_id in asked:
        r = rec.get(f"{CBIO_API}/molecular-profiles/{profile}/mutations?sampleListId={samples}"
                    f"&entrezGeneId={gene_id}&projection=SUMMARY")
        if not r.ok or not isinstance(r.data, list):
            return adapters._failed(rec, "cBioPortal", r, observations)
        exact = [m for m in r.data if isinstance(m, dict) and str(m.get("chr")) == str(place["chrom"])
                 and m.get("startPosition") == place["pos"] == m.get("endPosition")
                 and str(m.get("referenceAllele")).upper() == place["ref"]
                 and str(m.get("variantAllele")).upper() == place["alt"]]
        observations.append({"record": "gene", "gene": gene, "entrez_id": gene_id, "mutations_in_cohort": len(r.data),
                             "this_substitution": len(exact)})
        hits += [(gene, m) for m in exact]
    coverage = Coverage(
        requested_scope=f"tumours of {CBIO_COHORT} carrying {adapters._where(v)} (GRCh37 chr{place['chrom']}:"
                        f"{place['pos']} {place['ref']}>{place['alt']}), in {', '.join(g for g, _ in asked)}",
        limitations=["a gene panel reads only the regions it targets, and inherited variants are filtered out of "
                     "somatic calls: nothing found says nothing about the variant",
                     "a count is not a test: no background mutation rate is modelled"])
    if len(genes) > len(asked):
        coverage.limitations.append(f"asked about {len(asked)} of the {len(genes)} genes the annotation names")
    evidence: list[Evidence] = []
    if hits:
        r = rec.get(f"{CBIO_API}/studies/{CBIO_STUDY}/clinical-data?clinicalDataType=SAMPLE"
                    "&attributeId=CANCER_TYPE&projection=SUMMARY")
        if not r.ok or not isinstance(r.data, list):
            return adapters._failed(rec, "cBioPortal", r, observations)
        type_of = {str(x.get("sampleId")): str(x.get("value") or "") for x in r.data if isinstance(x, dict)}
        patients: dict[str, set[str]] = {}
        for x in r.data:
            if isinstance(x, dict) and x.get("value"):
                patients.setdefault(str(x["value"]), set()).add(str(x.get("patientId")))
        gene = hits[0][0]
        kinds = Counter(str(m.get("mutationType") or "") for _, m in hits)
        kind = kinds.most_common(1)[0][0] if kinds else ""
        carriers: dict[str, set[str]] = {}
        for _, m in hits:
            cancer_type = type_of.get(str(m.get("sampleId")), "")
            if cancer_type:
                carriers.setdefault(cancer_type, set()).add(str(m.get("patientId")))
        about = adapters._case_names(ctx)
        for cancer_type in sorted(carriers, key=lambda t: (-len(carriers[t]), t)):
            n, of = len(carriers[cancer_type]), len(patients.get(cancer_type, ()))
            counted = n >= CBIO_MIN_PATIENTS
            observations.append({"record": "cancer_type", "cancer_type": cancer_type, "patients_with_mutation": n,
                                 "patients_sequenced": of, "evidence": counted})
            if counted:
                evidence.append(recurrence_evidence(v, place, gene, cancer_type, n, of, kind, about))
    carriers_total = len({str(m.get("patientId")) for _, m in hits})
    coverage.assessed_scope = (f"{len(hits)} call(s) of this substitution in {carriers_total} patient(s); "
                               f"{len(evidence)} cancer type(s) with at least {CBIO_MIN_PATIENTS} patients")
    return AdapterResult(
        retrieval_status="records_found" if evidence else "no_records_found", observations=observations,
        coverage=coverage, evidence=evidence,
        raw={"requests": rec.records(), "study": CBIO_STUDY, "placement": place,
             "calls": [{k: m.get(k) for k in ("sampleId", "patientId", "chr", "startPosition", "referenceAllele",
                                              "variantAllele", "mutationType", "proteinChange")} for _, m in hits]},
        assembly="GRCh37",
        message=(f"called in {carriers_total} patient(s); {len(evidence)} cancer type(s) with at least "
                 f"{CBIO_MIN_PATIENTS}" if hits else "the cohort does not call this substitution"),
        cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- litvar_search, litvar_mentions ---------------------------------------------------------------------------------

LITVAR_API = "https://www.ncbi.nlm.nih.gov/research/litvar2-api"
PUBTATOR_API = "https://www.ncbi.nlm.nih.gov/research/pubtator3-api"
LITVAR_RESULTS = 10                # PubTator lists ten papers a page; one page is read
SPELLING_MIN, SPELLING_MAX = 4, 40
SPELLINGS_KEPT = 8
_RSID = re.compile(r"rs\d+", re.I)
LITVAR_SEARCH = ToolSpec(
    name="litvar_search", route="literature",
    description=("Articles that name the variant under any spelling LitVar normalises to its rsID, in PubTator's "
                 "relevance order, optionally with words that must also occur. Lists papers; creates no evidence."),
    params={"words": ParamSpec(type="list[str]", description="words or quoted phrases, any one of which must occur")},
    assemblies=[], provider="LitVar and PubTator (NCBI)", dataset_release="LitVar 2 and PubTator 3 (NCBI)",
    coverage_notes=("Text mining: a listed article may name another variant, and an article that names this one may "
                    "be missed. Only a variant with an rsID can be asked about."),
    result_semantics=("records_found: papers listed (read one to extract its experiments). no_records_found: LitVar "
                      "has no entry for the variant's rsID at its position, or no paper matched; neither says "
                      "anything about the biology."),
    rate_policy="serial", evidence_classes=[], network=True)
LITVAR_MENTIONS = ToolSpec(
    name="litvar_mentions", route="literature",
    description=("The spellings one article uses for the variant, as PubTator marks them in its text (an HGVS name, a "
                 "shorthand). Pointers to where the article speaks of it; never evidence, and never proof of "
                 "identity."),
    params={"pmid": ParamSpec(type="str", required=True, description="the article's PubMed id")},
    assemblies=[], provider="PubTator (NCBI)", dataset_release="PubTator 3 (NCBI)",
    coverage_notes="Text mining of the title, the abstract and, for open-access articles, the full text.",
    result_semantics=("records_found: at least one spelling other than an rsID. no_records_found: the article is "
                      "not annotated, or names the variant by its rsID only."),
    rate_policy="serial", evidence_classes=[], network=True)


def litvar_entry_url(rsid: str) -> str:
    return f"{LITVAR_API}/variant/get/{quote(f'litvar@{rsid}##', safe='')}"


def pubtator_name_url(rsid: str) -> str:
    return f"{PUBTATOR_API}/entity/autocomplete/?query={quote(rsid, safe='')}"


def pubtator_search_url(accession: str, words: list[str]) -> str:
    """PubTator's search for one entity, with any one of `words` as well; its first page, in relevance order."""
    text = accession + (f" AND ({' OR '.join(words)})" if words else "")
    return f"{PUBTATOR_API}/search/?text={quote(text, safe='')}&page=1"


def pubtator_text_url(pmid: str) -> str:
    return f"{PUBTATOR_API}/publications/export/biocjson?pmids={pmid}&full=true"


def case_rsids(ctx: ToolContext) -> list[str]:
    """The variant's rsIDs as the reader searches by them: the request's, then those recorded as its own."""
    aliases = sorted(getattr(ctx.graph, "variant_aliases", None) or [])
    return _unique(x.lower() for x in [ctx.case.variant.rsid, *aliases] if x and _RSID.fullmatch(x))


def _same_place(detail: dict[str, Any], v: Any) -> bool:
    """Whether LitVar's entry sits at the case variant's GRCh38 position."""
    return f"{v.chrom}:{v.pos}" in [str(x) for x in detail.get("data_chromosome_base_position") or []]


def litvar_search(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return AdapterResult(execution_status="unavailable", message="litvar_search has no HTTP client")
    v = ctx.case.variant
    rsids = case_rsids(ctx)
    if not rsids:
        return AdapterResult(execution_status="not_applicable",
                             message="no rsID is recorded for the variant, and LitVar is asked by rsID")
    words = sorted({str(w).strip() for w in (params.get("words") or []) if str(w).strip()})   # one request, any order
    rec = adapters._Recorder(ctx.http)
    observations: list[dict[str, Any]] = []
    papers: list[dict[str, Any]] = []
    coverage = Coverage(requested_scope=f"articles LitVar lists for {', '.join(rsids)}"
                        + (f" that also hold one of: {', '.join(words)}" if words else ""),
                        limitations=["text mining lists papers: it is not evidence, a listed paper may name another "
                                     "variant, and an empty list is not evidence of absence"])
    for rsid in rsids:
        detail = rec.get(litvar_entry_url(rsid))
        if not detail.ok or not isinstance(detail.data, dict):
            if detail.status in (400, 404):
                observations.append({"record": "variant", "rsid": rsid, "known": False})
                continue
            return adapters._failed(rec, "LitVar", detail, observations)
        entry = {"record": "variant", "rsid": rsid, "known": True, "name": detail.data.get("name"),
                 "genes": detail.data.get("gene"), "same_position": _same_place(detail.data, v)}
        observations.append(entry)
        if not entry["same_position"]:
            continue                               # LitVar's entry for this rsID is somewhere else: not this variant
        named = rec.get(pubtator_name_url(rsid))
        if not named.ok or not isinstance(named.data, list):
            return adapters._failed(rec, "PubTator", named, observations)
        accession = next((str(x.get("_id")) for x in named.data if isinstance(x, dict)
                          and str(x.get("db_id") or "").lower() == f"{rsid}##" and x.get("biotype") == "variant"), "")
        entry["accession"] = accession or None
        if not accession:
            continue
        found = rec.get(pubtator_search_url(accession, words))
        if not found.ok or not isinstance(found.data, dict):
            return adapters._failed(rec, "PubTator", found, observations)
        entry["papers_matching"] = found.data.get("count")
        for x in (found.data.get("results") or [])[:LITVAR_RESULTS]:
            if not isinstance(x, dict) or not (x.get("pmid") or x.get("pmcid")):
                continue
            paper = {"record": "paper", "pmid": str(x["pmid"]) if x.get("pmid") else None,
                     "pmcid": x.get("pmcid") or None, "doi": x.get("doi") or None,
                     "title": " ".join(str(x.get("title") or "").split()), "publication_type": "",
                     "journal": x.get("journal"), "year": str(x.get("date") or "")[:4] or None, "found_for": rsid}
            if not any(p["pmid"] == paper["pmid"] and p["pmcid"] == paper["pmcid"] for p in papers):
                papers.append(paper)
    known = [o for o in observations if o.get("known") and o.get("same_position")]
    coverage.assessed_scope = (f"{len(known)} of {len(rsids)} rsID(s) have a LitVar entry at the variant's position; "
                               f"{len(papers)} paper(s) listed")
    return AdapterResult(
        retrieval_status="records_found" if papers else "no_records_found", observations=[*papers, *observations],
        coverage=coverage, raw={"requests": rec.records(), "papers": papers, "variants": observations},
        message=f"{len(papers)} paper(s) listed for {', '.join(rsids)}", cached=rec.cached,
        retrieval_time=rec.retrieval_time())


def spellings(document: dict[str, Any], rsids: list[str]) -> list[dict[str, Any]]:
    """The strings one annotated article uses for a variant with one of these rsIDs, most frequent first: the text
    of each variant annotation PubTator normalised to it. An rsID itself is left out (the reader searches by it
    already), and so is a string too short or too long to be a name, or with no digit in it ("G > A")."""
    wanted = {r.lower() for r in rsids}
    counts: Counter[str] = Counter()
    for passage in document.get("passages") or []:
        for a in passage.get("annotations") or [] if isinstance(passage, dict) else []:
            infons = a.get("infons") or {}
            if infons.get("type") != "Variant":
                continue
            theirs = {str(x).lower() for x in [infons.get("rsid"), *(infons.get("rsids") or [])] if x}
            text = " ".join(str(a.get("text") or "").split())
            if (theirs & wanted and SPELLING_MIN <= len(text) <= SPELLING_MAX and any(c.isdigit() for c in text)
                    and not _RSID.fullmatch(text)):
                counts[text] += 1
    ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [{"record": "spelling", "text": text, "count": n} for text, n in ordered[:SPELLINGS_KEPT]]


def litvar_mentions(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return AdapterResult(execution_status="unavailable", message="litvar_mentions has no HTTP client")
    pmid = str(params.get("pmid") or "").strip()
    rsids = case_rsids(ctx)
    if not pmid.isdigit() or not rsids:
        return AdapterResult(execution_status="not_applicable",
                             message="litvar_mentions needs a PubMed id and a variant with an rsID")
    rec = adapters._Recorder(ctx.http)
    answer = rec.get(pubtator_text_url(pmid))
    if not answer.ok or not isinstance(answer.data, dict | list):
        return adapters._failed(rec, "PubTator", answer)
    documents = answer.data.get("PubTator3") if isinstance(answer.data, dict) else answer.data
    document = next((d for d in documents or [] if isinstance(d, dict) and str(d.get("pmid")) == pmid), None)
    found = spellings(document, rsids) if document is not None else []
    return AdapterResult(
        retrieval_status="records_found" if found else "no_records_found", observations=found,
        coverage=Coverage(requested_scope=f"how PMID:{pmid} writes {', '.join(rsids)}",
                          assessed_scope=(f"{len((document or {}).get('passages') or [])} annotated passage(s)"
                                          if document is not None else "the article is not annotated"),
                          limitations=["text mining: a spelling is a pointer to where the article speaks of the "
                                       "variant, never proof that the name means this variant"]),
        raw={"requests": rec.records(), "pmid": pmid, "rsids": rsids, "spellings": found},
        message=f"{len(found)} spelling(s) other than an rsID", cached=rec.cached,
        retrieval_time=rec.retrieval_time())


SOURCE_TOOLS: tuple[tuple[ToolSpec, Any], ...] = (
    (UDACHA_ASA, udacha_asa), (MAVEDB_REPORTER, mavedb_reporter), (PROTEIN_QTL_SETS, protein_qtl_sets),
    (TUMOUR_RECURRENCE, tumour_recurrence), (LITVAR_SEARCH, litvar_search), (LITVAR_MENTIONS, litvar_mentions))
