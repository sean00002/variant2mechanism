"""The computational tools of v9 (SPEC 4.3 as amended by section 13; contract C2).

Importing this module registers twelve adapters in tools.REGISTRY: variant_annotation, ccre_overlap, qbic_inventory,
qbic_tf_detail, chip_occupancy, gtex_eqtl, tf_expression, gwas_associations, credible_sets_l2g, depmap_context,
civic_lookup and screen_online. They call the existing providers (context/, qbic/, the read-only v8 readers) through
the run's HTTP client (ctx.http, an Http9: offline in cache-only mode) and read local files from load_config() paths.
Where a provider would write into the repository or reach the network outside that client (QbicCache, QbicTools,
screendb.lookup, strand_precheck), the files are read directly instead (SPEC 13.2).

The adapter contract every tool here keeps (API-core.md section 4):
- retrieval is not biology: an empty search, a missing model, an absent biosample, an error and a cache miss are
  statuses and create no Evidence, so missing data can never become a contradiction. No tool here creates a measured
  null (SPEC 13.7 allows one only where the assay's scope is known): GTEx lists significant eQTLs only, and a locus
  query cannot show that a ChIP aggregator processed an experiment that has no peak there, so an ENCODE assay without
  an aggregator peak is listed, never Evidence. A query that failed (a GraphQL error inside an HTTP 200 included) is a
  failure, and a scoped search that left pages unread is incomplete, never "no records";
- observed_result is one factual sentence written by code from the data, never an interpretation;
- about_tfs / about_genes / about_elements / about_traits name what an observation is about, because the graph's
  identity checks read them: a QBiC-SELEX prediction is about the TFs its models map to (when a group's models
  disagree, each allele gets its own item), another variant's eQTL is about its element and gene, never this
  variant, and genes are current HGNC symbols (GTEx v8 still uses 2017 names);
- about_variants names the variant an observation was made at, because the graph never lets evidence about one
  variant support or contradict a claim about another: an observation at the case variant (VEP, the cCRE and the
  ChIP peaks containing it, QBiC-SELEX, GTEx, Open Targets' sets holding it, the SCREEN eQTL of this variant) names
  its rsID (supplied, else recorded as its own by fact collection) and "chrN:pos ref>alt"; another variant's
  observation names that variant only (a SCREEN eQTL by its GTEx id, as "chr1:109274857 G>C"); a GWAS Catalog row
  names its own SNPs and a CIViC assertion its CIViC variant. Observations about an element, a gene or a cell line
  only (cCRE classes, CRISPR and 3D links, expression, DepMap) name none;
- every directional observation about the variant names the allele its direction refers to: QBiC-SELEX the allele
  predicted to bind more, GTEx the alt allele with the sign of NES, the GWAS Catalog its reported effect allele
  (not placed for an A/T or C/G variant, whose strand the Catalog does not fix);
- one measurement is one independence group whichever tool reports it: a GWAS study in the Catalog and in Open
  Targets, a GTEx v8 eQTL from GTEx and from SCREEN (keyed by Ensembl gene id), a DepMap value from tf_expression and
  depmap_context;
- the data flags allele_specific, allele_targeted and in_vivo are set only when a source states them, and none of
  these sources does;
- expression is a level (class expression) and ChIP is occupancy: neither is turned into a threshold call, and nothing
  is ordered by z, TPM or ChIP; a CIS-BP-mapped QBiC-SELEX model counts as the TF's own (the mapping is provenance in
  data and observations, never in a field the graph reads);
- VEP's clinical, literature and conservation fields reach neither observations nor raw results.

collect_facts() is SPEC 6 step 2 (code's fact collection; it also records the case variant's exact-allele rsIDs and
the element containing it in the graph) and inventory_rows() is the inventory view the engine's packets and the
report read (contract C2). Raw results are deterministic: a response's retrieval time is recorded only when it was
retrieved, so the same cache-only call writes the same bytes.
"""

import gzip
import json
import math
import os
import re
from collections import Counter, defaultdict
from collections.abc import Iterable
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
from typing import Any

import pysam

from ..config import Config, ConfigError, load_config
from ..context import depmap, ensembl, genetics, occupancy
from ..context.base import Case as ProviderCase
from ..context.ccre import CLASSES as CCRE_CLASSES
from ..context.ccre import local_ccre
from ..context.chip import ENCODE_SEARCH
from ..context.http import HttpResult
from ..qbic.expression import ContextError, get_expression
from ..qbic.variants import Variant as ProviderVariant
from ..v8 import chipgrade, screendb
from . import http9
from .context_match import compare_context, is_unscoped, load_table, normalise_scope, scope_from_label
from .graph import ClaimGraph, GraphRefusal
from .qbic_reader import QbicReader, VariantScores, reader_for
from .schemas import Case, ContextScope, Coverage, Evidence, ToolCall, ToolRequest, Variant
from .tools import AdapterResult, ParamSpec, ToolContext, ToolRunner, ToolSpec, register_tool
from .traits import trait_query_match

CIVIC = "https://civicdb.org/api/graphql"
SCREEN_API = "https://screen.api.wenglab.org/graphql"
REMAP_WINDOW = 50                  # ReMap peaks this close to the variant, not containing it, are listed as nearby
GWAS_PAGE_SIZE, GWAS_MAX_PAGES = 100, 7
OT_PAGE_SIZE, OT_MAX_PAGES = 25, 3  # bound nested GraphQL complexity and HTTP use; unread sets stay incomplete
OT_L2G_ROWS, OT_COLOC_ROWS = 5, 3
CIVIC_EVIDENCE_ROWS = 100
NAMED = 8                          # names spelt out in one sentence; the about_* lists carry every one
MATRIX_CLASSES = {"CA-only": "CA", "TF-only": "TF"}     # SCREEN class-matrix labels -> registry (BED) labels
SCREEN_KEY_ENV = "V2M_SCREEN_API_KEY"
NUMBER = re.compile(r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")
COMPLEMENT = str.maketrans("ACGT", "TGCA")
STRAND_AMBIGUOUS = ({"A", "T"}, {"C", "G"})   # an allele pair whose other-strand spelling is the same pair
RSID = re.compile(r"rs\d+", re.I)
GTEX_VARIANT = re.compile(r"(?:chr)?([0-9]{1,2}|X|Y|MT?)_(\d+)_([ACGT]+)_([ACGT]+)(?:_b38)?", re.I)


# --- shared helpers -------------------------------------------------------------------------------------------------

def _config(ctx: ToolContext) -> Config:
    return ctx.config if ctx.config is not None else load_config()


def _where(v: Variant) -> str:
    return f"chr{v.chrom}:{v.pos} {v.ref}>{v.alt}"


def _about_case(v: Variant, rsids: Iterable[str] = ()) -> list[str]:
    """Evidence.about_variants of an observation made at the case variant (core C3-1), named as the graph knows it:
    its rsID (the supplied one; without one, each rsID recorded as the variant's own, `rsids`, lowest first) and its
    GRCh38 position with alleles ("chr2:60490908 T>G"). The graph lets evidence naming only other variants neither
    support nor contradict a claim about the case variant (nor the reverse), and refuses allele-bearing evidence that
    names no variant for an allelic claim, so every observation made at this variant names it."""
    if v.rsid:
        names = [v.rsid]
    else:
        names = sorted({r.lower() for r in rsids if RSID.fullmatch(r)}, key=lambda r: int(r[2:]))
    return [*names, _where(v)]


def _case_names(ctx: ToolContext, found: Iterable[str] = ()) -> list[str]:
    """_about_case for this call's case: with no rsID supplied, the rsIDs fact collection recorded as the case
    variant's own (graph.variant_aliases), and those this very call found for the exact variant (`found`: VEP runs
    before the aliases are recorded)."""
    aliases = getattr(ctx.graph, "variant_aliases", None) or {}
    return _about_case(ctx.case.variant, [*aliases, *found])


def _gtex_variant(variant_id: str) -> str:
    """A GTEx v8 variant id (GRCh38, "chr1_109274857_G_C_b38") written as about_variants names a variant,
    "chr1:109274857 G>C": the graph reads a chrom:pos with alleles, and a GTEx id names nothing to it. Any other form
    is kept as given."""
    m = GTEX_VARIANT.fullmatch(variant_id.strip())
    return f"chr{m.group(1).upper()}:{m.group(2)} {m.group(3).upper()}>{m.group(4).upper()}" if m else variant_id


def _named(items: list[str], limit: int = NAMED) -> str:
    return ", ".join(items[:limit]) + (f" and {len(items) - limit} more" if len(items) > limit else "")


def _evidence(**fields: Any) -> Evidence:
    """Tool evidence: origin tool, access dataset, evidence_id issued later by the graph."""
    return Evidence(origin="tool", access="dataset", **fields)


def _allele_base(v: Variant, side: str | None) -> str | None:
    return v.alt if side == "alt" else v.ref if side == "ref" else None


def _tissue_id(name: str) -> str:
    """A tissue name in one spelling: GTEx's Adipose_Subcutaneous and SCREEN's Adipose Subcutaneous agree."""
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def _gtex_group(variant_id: str, gene: str, tissue: str) -> str:
    """The independence group of one GTEx v8 gene-tissue association, shared by gtex_eqtl and SCREEN's eQTL links
    (both report the same GTEx v8 result), so the two never count as independent observations. `gene` is the Ensembl
    gene id where the source gives one: GTEx v8 names genes as of 2017 (SARS) and SCREEN as of today (SARS1)."""
    return f"GTEx:v8:{variant_id}:{gene.split('.')[0].upper()}:{_tissue_id(tissue)}"


def _gene_symbol(reg: Any, symbol: str, ensembl: str | None = None) -> str:
    """A gene's current HGNC symbol: by Ensembl gene id first, then as a current symbol, then as the previous symbol
    of exactly one gene (GTEx v8's SARS is SARS1), else the name as given, upper-cased. The graph matches genes by
    symbol, so an old name would hide a result from a claim naming the gene."""
    if ensembl and (found := reg.hgnc_by_ensembl.get(ensembl.split(".")[0])):
        return str(found).upper()
    key = symbol.strip().upper()
    if key in reg.hgnc_symbols:
        return str(reg.hgnc_symbols[key]).upper()
    previous = reg.prev_index.get(key) or set()
    return str(next(iter(previous))).upper() if len(previous) == 1 else key


def _number(value: Any) -> float | None:
    """A number a source gives as a number or as text with a note ("1.23 (Oncoarray)", "0.7883"); None for "NR",
    "-", empty or not finite. The GWAS Catalog v2 returns odds ratios as strings."""
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value) if math.isfinite(value) else None
    m = NUMBER.match(str(value or "").strip())
    return float(m.group()) if m and math.isfinite(float(m.group())) else None


def _context(label: str, variant: Variant, condition: str | None = None) -> ContextScope:
    """The scope an observation was made in (a biosample, cell line or tissue as the source names it)."""
    return scope_from_label(label, source="evidence", condition=condition, variant=variant)


def _requested_scopes(ctx: ToolContext, label: str | None) -> list[ContextScope]:
    """What a call is scoped to: the request's biosample or context, else every supplied context (else nothing)."""
    if label:
        return [scope_from_label(label, source="supplied", variant=ctx.case.variant)]
    scopes = (normalise_scope(s, variant=ctx.case.variant) for s in ctx.case.supplied_context)
    return [s for s in scopes if s is not None and not is_unscoped(s)]


def _match(scopes: list[ContextScope], scope: ContextScope) -> str | None:
    """How an observation's context stands to the requested scopes: exact, proxy, or None (outside them)."""
    found = {compare_context(s, scope) for s in scopes}
    return "exact" if "exact" in found else "proxy" if "proxy" in found else None


def _no_http(name: str) -> AdapterResult:
    return AdapterResult(execution_status="unavailable", message=f"{name}: no HTTP client is configured for this run")


class _Recorder:
    """The run's HTTP client, handed to a provider, keeping what each request returned: the raw result's provenance
    and the call's status come from here. Headers are never recorded, so no key can be."""

    def __init__(self, http: Any):
        self.http = http
        self.results: list[tuple[str, Any, HttpResult]] = []
        self.partial: list[str] = []           # GraphQL errors that came with data: the records may be incomplete

    @property
    def offline(self) -> bool:
        return bool(getattr(self.http, "offline", False))

    def request(self, method: str, url: str, json_body: Any = None, **kw: Any) -> HttpResult:
        return self._keep(method, json_body, self.http.request(method, url, json_body=json_body, **kw))

    def get(self, url: str, **kw: Any) -> HttpResult:
        return self._keep("GET", None, self.http.get(url, **kw))

    def post(self, url: str, body: Any, **kw: Any) -> HttpResult:
        return self._keep("POST", body, self.http.post(url, body, **kw))

    def graphql(self, url: str, query: str, **kw: Any) -> HttpResult:
        return self._keep("POST", {"query": query}, self.http.graphql(url, query, **kw))

    def query(self, url: str, body: dict[str, Any], **kw: Any) -> HttpResult:
        """A GraphQL POST (query and variables). An HTTP 200 whose query failed (errors and no data) is a failed
        retrieval, as Http.graphql treats it, so it can never read as "no records"; errors that come with data are
        kept in `partial`, and the adapter reports its records as incomplete."""
        r = self.http.post(url, body, **kw)
        if r.ok and isinstance(r.data, dict) and r.data.get("errors"):
            problem = f"GraphQL error: {' '.join(str(r.data['errors']).split())[:200]}"
            if not r.data.get("data"):
                r = HttpResult(False, r.status, None, r.url, r.retrieved_utc, r.cached, error=problem)
            else:
                self.partial.append(problem)
        return self._keep("POST", body, r)

    def _keep(self, method: str, body: Any, result: HttpResult) -> HttpResult:
        self.results.append((method, body, result))
        return result

    def failure(self) -> HttpResult | None:
        return next((r for _, _, r in self.results if not r.ok), None)

    def records(self) -> list[dict[str, Any]]:
        """Each request's provenance for the raw result. A failed request has no retrieval time (the clock time of a
        miss would make the same cache-only call write different bytes); a response keeps the time it was fetched."""
        return [{"method": m, "url": r.url, "body": b, "status": r.status, "ok": r.ok, "cached": r.cached,
                 "retrieved_utc": r.retrieved_utc if r.ok else None, "error": r.error} for m, b, r in self.results]

    @property
    def cached(self) -> bool:
        """Every response came from the HTTP cache (nothing was sent)."""
        return bool(self.results) and all(r.cached for _, _, r in self.results if r.ok)

    def retrieval_time(self) -> str | None:
        """When the oldest response used was retrieved (a cached response keeps its original time)."""
        times = sorted(r.retrieved_utc for _, _, r in self.results if r.ok and r.retrieved_utc)
        return times[0] if times else None


def _failed(rec: _Recorder, source: str, result: HttpResult | None = None,
            observations: list[dict] | None = None) -> AdapterResult:
    """A retrieval that did not return the records: a cache miss (cache-only run, nothing sent), unavailable, an error,
    or HTTP 404 (no record). Never Evidence."""
    result = result or rec.failure()
    raw = {"requests": rec.records()}
    if result is None:
        return AdapterResult(execution_status="error", message=f"{source}: no response was recorded", raw=raw,
                             observations=observations or [])
    status = http9.execution_status(result)
    if status == "success":
        return AdapterResult(retrieval_status="no_records_found", message=f"{source}: no record ({result.url})",
                             raw=raw, observations=observations or [], cached=rec.cached,
                             retrieval_time=rec.retrieval_time())
    message = (f"{source}: not in the HTTP cache, and this run is cache-only, so nothing was sent ({result.url})"
               if status == "cache_miss" else f"{source}: {result.error}")
    return AdapterResult(execution_status=status, message=message, raw=raw, observations=observations or [])


def _partial_notes(rec: _Recorder, source: str) -> list[str]:
    """Coverage limitations for GraphQL answers that came with errors (their records may be missing)."""
    return [f"{source} answered with errors, so records may be missing: {p}" for p in rec.partial]


def _graphql_status(rec: _Recorder, found: bool) -> str:
    """incomplete when an answer carried GraphQL errors (records may be missing, so even none found is not "no
    record"), else records_found or no_records_found."""
    return "incomplete" if rec.partial else "records_found" if found else "no_records_found"


def _provider_case(ctx: ToolContext, http: Any) -> ProviderCase:
    """The v8 providers' Case for this SNV, with no whole-tool re-runs (Http9 owns retries)."""
    v = ctx.case.variant
    return ProviderCase(variant=ProviderVariant.make(v.chrom, v.pos, v.ref, v.alt), disease="",
                        origin=ctx.case.origin, rsid=v.rsid, http=http, retry_rounds=0)


# --- reference check (SPEC 13.2) -----------------------------------------------------------------------------------

def _fasta_check(variant: Variant, cfg: Config) -> dict[str, Any]:
    try:
        path = cfg.path("local", "genome")
    except (KeyError, ConfigError):
        path = None
    if path is None or not path.exists() or not Path(f"{path}.fai").exists():
        return {"source": "hg38_fasta", "status": "unavailable", "note": "no indexed local hg38 FASTA"}
    fasta = pysam.FastaFile(str(path))
    try:
        base = fasta.fetch(f"chr{variant.chrom}", variant.pos - 1, variant.pos - 1 + len(variant.ref)).upper()
    except (KeyError, ValueError, IndexError) as e:
        return {"source": "hg38_fasta", "status": "unavailable", "note": f"{type(e).__name__}: {e}"[:160]}
    finally:
        fasta.close()
    return {"source": "hg38_fasta", "status": "verified" if base == variant.ref else "mismatch",
            "genome_base": base, "given_ref": variant.ref}


def reference_check(variant: Variant, cfg: Config, vep_record: dict | None = None) -> dict[str, Any]:
    """Does the given ref match the GRCh38 reference? Sources, all offline except a VEP record already fetched: the
    base at index 10 of a cached QBiC-SELEX 21-mer (SNVs), the local indexed hg38 FASTA when present, and VEP's
    reference allele. "mismatch" if any source disagrees, "verified" if one agrees, else "unavailable"."""
    checks = [reader_for(cfg).reference_check(variant) if variant.variant_type == "SNV" else
              {"source": "qbic_21mer", "status": "unavailable", "note": "the cached 21-mers cover SNVs only"},
              _fasta_check(variant, cfg)]
    if vep_record is not None:
        vep_ref = str(vep_record.get("allele_string") or "").split("/")[0].upper()
        status = "unavailable" if not vep_ref else "verified" if vep_ref == variant.ref else "mismatch"
        checks.append({"source": "ensembl_vep", "genome_base": vep_ref or None, "given_ref": variant.ref,
                       "status": status})
    statuses = {c["status"] for c in checks}
    status = "mismatch" if "mismatch" in statuses else "verified" if "verified" in statuses else "unavailable"
    return {"status": status, "checks": checks}


EVIDENCE_INSPECT = ToolSpec(
    name="evidence_inspect", route="computational", assemblies=[],
    description="Inspect existing evidence without network or new evidence. Retrieve full records by IDs, or "
                "search their text and page by offset. Summarised records have not been filtered out.",
    params={"evidence_ids": ParamSpec(type="list[str]", description="up to 12 saved evidence IDs"),
            "query": ParamSpec(description="case-insensitive text filter; * means all records"),
            "offset": ParamSpec(type="int", description="zero-based page offset, default 0"),
            "limit": ParamSpec(type="int", description="records per page, 1 to 12, default 6")},
    result_semantics="Records are existing observations, not independent new evidence; use their original IDs.",
    provider="local claim graph", dataset_release="current run", one_of=[["evidence_ids", "query"]])


@register_tool(EVIDENCE_INSPECT)
def evidence_inspect(params: dict, ctx: ToolContext) -> AdapterResult:
    wanted = params.get("evidence_ids") or []
    if len(wanted) > 12 or any(eid not in ctx.graph.evidence for eid in wanted):
        return AdapterResult(execution_status="not_applicable", message="Specify at most 12 existing evidence IDs")
    query = str(params.get("query") or "").casefold()
    if query == "*":
        query = ""
    rows = [e.model_dump(mode="json") for eid, e in ctx.graph.evidence.items()
            if (not wanted or eid in wanted)]
    rows = [r for r in rows if not query or query in json.dumps(r, ensure_ascii=False).casefold()]
    offset = max(0, int(params.get("offset") or 0))
    limit = min(12, max(1, int(params.get("limit") or (12 if wanted else 6))))
    page = rows[offset:offset + limit]
    return AdapterResult(retrieval_status="records_found" if page else "no_records_found",
                         observations=page, raw={"total": len(rows), "offset": offset, "records": page},
                         message=f"{len(page)} of {len(rows)} existing records; next offset {offset + len(page)}. "
                                 "No new independent evidence.")


# --- variant_annotation ---------------------------------------------------------------------------------------------

VARIANT_ANNOTATION = ToolSpec(
    name="variant_annotation", route="computational",
    description=("Ensembl VEP consequences of the alt allele (genes and regulatory features), a reference-allele "
                 "check (cached QBiC-SELEX context, local hg38, VEP) and the protein-coding genes within 1 Mb as "
                 "candidates."),
    variant_types=["SNV"], provider="Ensembl REST (VEP and overlap endpoints)",
    dataset_release="Ensembl REST, the release current at retrieval (the endpoint pins none)",
    coverage_notes=("GRCh38 SNVs. Consequences only: VEP's clinical, literature and conservation fields are dropped. "
                    "Nearby genes are candidates by distance, never assignments."),
    result_semantics=("records_found: VEP annotated the variant; one Evidence item (annotation) per gene with a "
                      "consequence and per regulatory feature. incomplete: the nearby-gene list could not be read. "
                      "A reference mismatch is reported in the observations. The variant record lists every "
                      "co-located rsID (rsids) and, apart, those with this exact position and alleles (exact_rsids): "
                      "only those name this variant."),
    rate_policy="parallel", evidence_classes=["annotation"], network=True)


def _vep_genes(record: dict) -> list[dict[str, Any]]:
    """VEP's transcript consequences folded per gene, in symbol order."""
    genes: dict[str, dict[str, Any]] = {}
    for t in record.get("transcript_consequences") or []:
        name = t.get("gene_symbol") or t.get("gene_id")
        if not name:
            continue
        g = genes.setdefault(name, {"gene": name, "gene_id": t.get("gene_id"), "consequences": set(),
                                    "biotypes": set(), "distance": None, "transcripts": 0})
        g["consequences"].update(t.get("consequence_terms") or [])
        if t.get("biotype"):
            g["biotypes"].add(t["biotype"])
        g["transcripts"] += 1
        if t.get("distance") is not None:
            g["distance"] = t["distance"] if g["distance"] is None else min(g["distance"], t["distance"])
    return [{**g, "consequences": sorted(g["consequences"]), "biotypes": sorted(g["biotypes"])}
            for _, g in sorted(genes.items())]


def _exact_rsids(record: dict, v: Variant) -> list[str]:
    """The dbSNP rsIDs VEP co-locates with this exact variant: the same chromosome, start and end, the same reference
    allele, and this alt among the rsID's alternative alleles (a multiallelic rsID counts when it includes this alt).
    Another allele at the same position is another variant, whose rsID must never stand for this one. Numeric order
    (the lowest, usually the merge target, first)."""
    found = set()
    for c in record.get("colocated_variants") or []:
        rsid = str(c.get("id") or "")
        alleles = str(c.get("allele_string") or "").upper().split("/")
        if not re.fullmatch(r"rs\d+", rsid) or len(alleles) < 2:
            continue
        if c.get("strand") == -1:
            alleles = [a[::-1].translate(COMPLEMENT) for a in alleles]
        same_place = (str(c.get("seq_region_name") or v.chrom) == v.chrom and c.get("start") == v.pos
                      and c.get("end") == v.pos + len(v.ref) - 1)
        if same_place and alleles[0] == v.ref and v.alt in alleles[1:]:
            found.add(rsid)
    return sorted(found, key=lambda r: int(r[2:]))


def _vep_raw(record: dict) -> dict[str, Any]:
    """The VEP record without its leak-prone fields: colocated variants reduced to rsIDs (no ClinVar, COSMIC, HGMD,
    PubMed or phenotype flags) and no conservation scores."""
    keep_t = ("gene_symbol", "gene_id", "transcript_id", "biotype", "consequence_terms", "distance", "impact", "strand")
    keep_r = ("regulatory_feature_id", "biotype", "consequence_terms", "impact")
    return {"allele_string": record.get("allele_string"),
            "most_severe_consequence": record.get("most_severe_consequence"),
            "rsids": sorted({str(c.get("id")) for c in record.get("colocated_variants") or []
                             if str(c.get("id", "")).startswith("rs")}),
            "transcript_consequences": [{k: t.get(k) for k in keep_t}
                                        for t in record.get("transcript_consequences") or []],
            "regulatory_feature_consequences": [{k: r.get(k) for k in keep_r}
                                                for r in record.get("regulatory_feature_consequences") or []]}


@register_tool(VARIANT_ANNOTATION)
def variant_annotation(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return _no_http(ctx.spec.name)
    cfg, v = _config(ctx), ctx.case.variant
    rec = _Recorder(ctx.http)
    case = _provider_case(ctx, rec)
    vep = ensembl.variant_annotation(case)
    near = ensembl.nearest_genes(case)
    record = vep.full[0] if vep.ok and isinstance(vep.full, list) and vep.full else None
    check = {"record": "reference_check", **reference_check(v, cfg, record)}
    nearby = [{"record": "nearby_gene", **{k: g[k] for k in ("gene", "ensembl", "strand", "tss", "distance_to_tss",
                                                             "position")}} for g in near.full] if near.ok else []
    if record is None:
        return _failed(rec, "Ensembl VEP", observations=[check, *nearby])
    raw_vep = {**_vep_raw(record), "exact_rsids": _exact_rsids(record, v)}
    from .variant_identity import NCBI, placement_rows
    mappings, mapping_note = [], "no exact rsID available for assembly mapping"
    if raw_vep["exact_rsids"]:
        rsid = raw_vep["exact_rsids"][0]
        mapped = rec.get(NCBI + rsid[2:])
        if mapped.ok and isinstance(mapped.data, dict):
            mappings = placement_rows(mapped.data, v, rsid)
        mapping_note = (f"{len(mappings)} primary-assembly allele placements verified" if mappings else
                        "assembly mapping unavailable or ambiguous; never infer a cross-build identity")
    genes = _vep_genes(record)
    regs = [{"id": r.get("regulatory_feature_id"), "biotype": r.get("biotype"),
             "consequences": sorted(r.get("consequence_terms") or [])}
            for r in record.get("regulatory_feature_consequences") or [] if r.get("regulatory_feature_id")]
    where, group = _where(v), f"VEP:{v.key}"
    about = _case_names(ctx, raw_vep["exact_rsids"])        # VEP annotated this exact variant: name it
    evidence = []
    for g in genes:
        distance = f", {g['distance']:,} bp from its nearest transcript" if g["distance"] is not None else ""
        evidence.append(_evidence(
            evidence_class="annotation", source_ids=[f"ENSEMBL:{g['gene_id']}"] if g["gene_id"] else [],
            observed_result=(f"Ensembl VEP: {where} is a {', '.join(g['consequences'])} for {g['gene']} "
                             f"({g['transcripts']} transcript(s){distance})."),
            data={k: g[k] for k in ("gene_id", "consequences", "biotypes", "distance", "transcripts")},
            about_genes=[g["gene"]], about_variants=about, independence_group=group))
    for r in regs:
        evidence.append(_evidence(
            evidence_class="annotation", source_ids=[f"ENSEMBL:{r['id']}"],
            observed_result=f"Ensembl VEP: {where} lies in Ensembl regulatory feature {r['id']} ({r['biotype']}).",
            data={"biotype": r["biotype"], "consequences": r["consequences"]}, about_elements=[r["id"]],
            about_variants=about, independence_group=group))
    observations = [{"record": "variant", "variant": where, "allele_string": raw_vep["allele_string"],
                     "most_severe_consequence": raw_vep["most_severe_consequence"], "rsids": raw_vep["rsids"],
                     "exact_rsids": raw_vep["exact_rsids"]},
                    check, *mappings, {"record": "variant_mapping_status", "message": mapping_note},
                    *({"record": "consequence", **g} for g in genes),
                    *({"record": "regulatory_feature", **r} for r in regs), *nearby]
    limitations = ["consequences are annotations of position, not evidence of an effect"]
    if not near.ok:
        limitations.append("the protein-coding genes within 1 Mb could not be read: " + str(near.full.get("error")))
    if check["status"] == "mismatch":
        limitations.append("the given reference allele disagrees with the genome: see the reference check")
    return AdapterResult(
        retrieval_status="records_found" if near.ok else "incomplete", observations=observations,
        coverage=Coverage(requested_scope=f"VEP consequences, reference check and genes within 1 Mb of {where}",
                          assessed_scope=(f"VEP: {len(genes)} gene(s), {len(regs)} regulatory feature(s); "
                                          f"{len(nearby)} protein-coding gene(s) within 1 Mb"),
                          limitations=limitations),
        evidence=evidence, raw={"requests": rec.records(), "vep": raw_vep, "nearby_genes": near.full if near.ok
                                else None, "reference_check": check, "variant_mappings": mappings},
        message=f"VEP: {raw_vep['most_severe_consequence']}; reference check {check['status']}",
        cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- ccre_overlap ---------------------------------------------------------------------------------------------------

def _manifest_md5(path: Path) -> dict[str, str]:
    """file name -> md5 from an md5sum-style manifest (data/screen/MANIFEST.md5)."""
    if not path.exists():
        return {}
    pairs = (line.split(maxsplit=1) for line in path.read_text().splitlines() if line.strip())
    return {name.strip(): md5 for md5, name in pairs}


def _reference_md5(file: Path) -> str | None:
    """The md5 data/reference/MANIFEST.md records for a reference file (its table lists paths below that folder)."""
    for folder in list(file.parents)[:3]:
        manifest = folder / "MANIFEST.md"
        if manifest.exists():
            for line in manifest.read_text().splitlines():
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 3 and cells[0] and str(file).endswith(cells[0]):
                    return cells[2]
    return None


def ccre_release(cfg: Config | None = None) -> str:
    """The local registry and SCREEN files a ccre_overlap answer came from, by md5 (SPEC 4.3)."""
    cfg = cfg or load_config()
    bed = cfg.path("data", "ccres")
    md5 = _reference_md5(bed)
    screen_md5 = _manifest_md5(cfg.path("data", "screen_dir") / "MANIFEST.md5")
    parts = [f"ENCODE V4 cCRE registry {bed.name.split('.')[0]}" + (f" (md5 {md5})" if md5 else "")]
    if screen_md5:
        parts.append("SCREEN V4 downloads (" + "; ".join(f"{n} md5 {m}" for n, m in sorted(screen_md5.items())) + ")")
    return "; ".join(parts)


@lru_cache(maxsize=64)
def _screen_lines(path: str, size: int, mtime_ns: int, accession: str) -> tuple[str, ...]:
    """Lines of a gzipped SCREEN file whose first field is the accession. The files hold 0.07 to 6 GB of text, so they
    are streamed once and searched for "\\n<accession>\\t" (seconds, where zgrep takes minutes); cached per file
    version (size, mtime) and accession, read only."""
    key = f"\n{accession}\t".encode()
    found: list[str] = []
    buf = b"\n"
    with gzip.open(path, "rb") as f:
        while True:
            block = f.read(1 << 22)
            buf += block if block else b"\n"
            cut = buf.rfind(b"\n")
            complete = buf[: cut + 1]
            start = complete.find(key)
            while start != -1:
                end = complete.find(b"\n", start + 1)
                found.append(complete[start + 1:end].decode())
                start = complete.find(key, end)
            buf = buf[cut:]
            if not block:
                return tuple(found)


@lru_cache(maxsize=4)
def _class_columns(matrix: str, mtime_ns: int, names_file: str) -> tuple[tuple[str, str], ...]:
    """(ENCODE experiment accession, biosample name) for each class-matrix column: accessions from the matrix header,
    names from core_biosamples.json in the same order (the accession stands in when that file is missing)."""
    with gzip.open(matrix, "rt") as f:
        accessions = f.readline().rstrip("\n").split("\t")[1:]
    names_path = Path(names_file)
    names = json.loads(names_path.read_text()) if names_path.exists() else accessions
    if len(names) != len(accessions):
        raise ValueError(f"{names_file} lists {len(names)} biosamples for {len(accessions)} matrix columns")
    return tuple(zip(accessions, names, strict=True))


def screen_extract(cfg: Config, accession: str) -> dict[str, Any]:
    """A cCRE's class in each SCREEN V4 core-collection biosample and its gene links (CRISPR, eQTL, 3D chromatin),
    from the local downloads in data/screen. Read only: never cache/screen, which v8's lookup writes."""
    folder = cfg.path("data", "screen_dir")
    paths = {kind: folder / name for kind, name in screendb.FILES.items()}
    missing = [p.name for p in paths.values() if not p.exists()]
    if missing:
        raise FileNotFoundError(f"SCREEN downloads missing from {folder}: {', '.join(missing)}")
    with ThreadPoolExecutor(max_workers=len(paths)) as pool:   # gzip releases the GIL: the four scans overlap
        lines = dict(zip(paths, pool.map(
            lambda p: _screen_lines(str(p), p.stat().st_size, p.stat().st_mtime_ns, accession), paths.values()),
            strict=True))
    matrix = paths["classes"]
    columns = _class_columns(str(matrix), matrix.stat().st_mtime_ns, str(folder / "core_biosamples.json"))
    labels = lines["classes"][0].split("\t")[1:] if lines["classes"] else []
    classes = [{"experiment": acc, "biosample": name, "class": MATRIX_CLASSES.get(label, label), "source_label": label}
               for (acc, name), label in zip(columns, labels, strict=False)]
    kinds = ("3d", "eqtl", "crispr")
    links = screendb._links({k: list(lines[k]) for k in kinds})
    for kind in kinds:            # v8's parser drops the Ensembl gene id (column 2), which outlives symbol changes
        for link, line in zip(links[kind], lines[kind], strict=True):
            gene_id = line.split("\t")[1].strip()
            link["gene_id"] = gene_id if gene_id.startswith("ENSG") else None
    return {"classes": classes, "links": links}


CCRE_OVERLAP = ToolSpec(
    name="ccre_overlap", route="computational",
    description=("The ENCODE V4 cCRE containing the variant (local registry), its SCREEN V4 class in the "
                 "core-collection biosamples, and its SCREEN gene links: CRISPR perturbations, GTEx v8 eQTLs and 3D "
                 "contacts."),
    params={"biosample": ParamSpec(description=("a biosample or tissue to scope the class Evidence to (exact or "
                                                "proxy matches, e.g. HeLa-S3 for HeLa); default: the supplied "
                                                "context"))},
    provider="ENCODE cCRE registry V4 (local ENCFF420VPZ) and SCREEN V4 downloads (local)", release_fn=ccre_release,
    coverage_notes=("Local files only. SCREEN classes come from 170 core-collection experiments (72 biosample names); "
                    "a biosample outside the collection (HeLa, for one) has no class of its own, only a proxy's "
                    "(HeLa-S3). Gene links belong to the element, not necessarily to this variant."),
    result_semantics=("records_found: the variant lies in a cCRE (Evidence: the overlap; the class in each scoped "
                      "biosample; each gene link: an eQTL of this variant is an association, an eQTL of another "
                      "variant in the element only an annotation of the element). no_records_found: no cCRE contains "
                      "the variant (the nearest is in the observations)."),
    rate_policy="parallel", evidence_classes=["annotation", "perturbation", "association"])


def _ccre_link_evidence(acc: str, links: dict, v: Variant, reg: Any, about: list[str]) -> list[Evidence]:
    """Evidence for a cCRE's SCREEN gene links: CRISPR perturbations, GTEx v8 eQTLs and 3D contacts (annotation;
    contact is not causation). An eQTL of this variant is association evidence about it (allele alt, the sign of the
    slope; about_variants `about`, the case variant's names), in the same independence group as gtex_eqtl's report of
    that result. An eQTL of another variant in the element says something about the element and the gene, nothing
    about this variant: it is an annotation of the element (so it can only hint at an element-gene link), and its
    about_variants name that variant ("chr1:109274857 G>C", from GTEx's id), never this one, so the graph refuses it
    as support or contradiction for any claim about this variant. CRISPR and 3D links are about the element and the
    gene only: they name no variant."""
    out = []
    gtex_id = f"chr{v.chrom}_{v.pos}_{v.ref}_{v.alt}_b38"
    for x in links.get("crispr") or []:
        inhibition = "crispri" in x["method"].lower()
        direction = ("increases" if x["effect"] < 0 else "decreases" if x["effect"] > 0 else "unspecified") \
            if inhibition else "unspecified"
        gene = _gene_symbol(reg, x["gene"], x.get("gene_id"))
        out.append(_evidence(
            evidence_class="perturbation", source_ids=[x["experiment"], acc],
            observed_result=(f"SCREEN V4 CRISPR link: {x['method']} of {x['region']} (cCRE {acc}) in {x['biosample']} "
                             f"changed {gene} expression by {x['effect']:+.3g} (p {x['p']:.2g}; "
                             f"{x['experiment']})."),
            data={"effect": x["effect"], "p": x["p"], "method": x["method"], "region": x["region"],
                  "experiment": x["experiment"], "gene_id": x.get("gene_id"),
                  "direction_basis": ("inhibiting the element changed the gene's expression with the opposite sign"
                                      if inhibition else "not stated for this method")},
            direction=direction, context=_context(x["biosample"], v), about_genes=[gene], about_elements=[acc],
            independence_group=f"SCREEN-CRISPR:{x['experiment']}"))
    for x in links.get("eqtl") or []:
        own = x["variant"] == gtex_id
        gene = _gene_symbol(reg, x["gene"], x.get("gene_id"))
        data = {"variant": x["variant"], "case_variant": own, "slope": x["slope"], "p": x["p"],
                "tissue": x["tissue"], "source": x["source"], "gene_id": x.get("gene_id")}
        group = _gtex_group(x["variant"], x.get("gene_id") or gene, x["tissue"])
        if own:
            sign = "increases" if x["slope"] > 0 else "decreases" if x["slope"] < 0 else "unspecified"
            out.append(_evidence(
                evidence_class="association", source_ids=[x["source"], acc],
                observed_result=(f"SCREEN V4 eQTL link ({x['source']}): {x['variant']} in cCRE {acc} is an eQTL for "
                                 f"{gene} in {x['tissue']} (slope {x['slope']:+.3g} for the {v.alt} allele relative "
                                 f"to {v.ref}, p {x['p']:.2g})."),
                data=data, allele=v.alt, direction=sign, context=_context(x["tissue"], v), about_genes=[gene],
                about_elements=[acc], about_variants=list(about), independence_group=group))
            continue
        out.append(_evidence(
            evidence_class="annotation", source_ids=[x["source"], acc],
            observed_result=(f"SCREEN V4 eQTL link ({x['source']}): another variant in cCRE {acc}, {x['variant']}, is "
                             f"an eQTL for {gene} in {x['tissue']} (slope {x['slope']:+.3g} for its own alt allele, "
                             f"p {x['p']:.2g})."),
            data=data, context=_context(x["tissue"], v), about_genes=[gene], about_elements=[acc],
            about_variants=[_gtex_variant(x["variant"])], independence_group=group,
            limitations=[f"an eQTL of {x['variant']}, not of {_where(v)}: about the element and the gene, never "
                         "evidence about this variant's alleles"]))
    for x in links.get("3d") or []:
        gene = _gene_symbol(reg, x["gene"], x.get("gene_id"))
        out.append(_evidence(
            evidence_class="annotation", source_ids=[x["experiment"], acc],
            observed_result=(f"SCREEN V4 3D-chromatin link: cCRE {acc} contacts {gene} ({x['method']}, "
                             f"{x['experiment']}, {x['biosample']}, score {x['score']})."),
            data={"method": x["method"], "experiment": x["experiment"], "score": x["score"],
                  "genetically_modified": x["modified"], "gene_id": x.get("gene_id")},
            context=_context(x["biosample"], v), about_genes=[gene], about_elements=[acc],
            independence_group=f"SCREEN-3D:{x['experiment']}", limitations=["contact is not causal"]))
    return out


@register_tool(CCRE_OVERLAP)
def ccre_overlap(params: dict, ctx: ToolContext) -> AdapterResult:
    cfg, v = _config(ctx), ctx.case.variant
    bed = cfg.path("data", "ccres")
    local = local_ccre(f"chr{v.chrom}", v.pos, bed)
    where = _where(v)
    requested = f"the ENCODE V4 cCRE registry at {where}"
    if local is None or local["distance"] != 0:
        nearest = [] if local is None else [{"record": "nearest_element", **local}]
        return AdapterResult(retrieval_status="no_records_found", observations=nearest,
                             coverage=Coverage(requested_scope=requested, assessed_scope=f"{bed.name}, every cCRE"),
                             raw={"registry": bed.name, "nearest": local},
                             message=(f"no cCRE contains {where}" + (f"; nearest {local['accession']} "
                                                                     f"({local['class']}) {local['distance']} bp away"
                                                                     if local else "")))
    acc = local["accession"]
    screen = screen_extract(cfg, acc)
    scopes = _requested_scopes(ctx, params.get("biosample"))
    columns = [{**c, "match": _match(scopes, _context(c["biosample"], v)) if scopes else None}
               for c in screen["classes"]]
    about = _case_names(ctx)
    # The overlap says where this variant lies, so it names the variant (another variant in the same element is not
    # placed by it); the element's classes, CRISPR and 3D links are about the element alone and name none.
    evidence = [_evidence(
        evidence_class="annotation", source_ids=[acc, f"ENCODE:{bed.name.split('.')[0]}"],
        observed_result=(f"{where} lies in ENCODE cCRE {acc} ({local['class']}: "
                         f"{CCRE_CLASSES.get(local['class'], local['class'])}), chr{v.chrom}:{local['start']}-"
                         f"{local['end']} (ENCODE V4 registry)."),
        data={"class": local["class"], "start": local["start"], "end": local["end"],
              "registry": bed.name.split(".")[0]},
        about_elements=[acc], about_variants=about, independence_group=f"ENCODE-cCRE:{acc}")]
    for c in columns:
        if c["match"] is None:
            continue
        evidence.append(_evidence(
            evidence_class="annotation", source_ids=[c["experiment"], acc],
            observed_result=(f"SCREEN V4 core collection: cCRE {acc} is classified {c['source_label']} in "
                             f"{c['biosample']} ({c['experiment']})."),
            data={"class": c["class"], "source_label": c["source_label"], "experiment": c["experiment"]},
            context=_context(c["biosample"], v), about_elements=[acc],
            independence_group=f"SCREEN-class:{c['experiment']}:{acc}"))
    evidence += _ccre_link_evidence(acc, screen["links"], v, reader_for(cfg).registry, about)
    links = screen["links"]
    counts = Counter(c["source_label"] for c in columns)
    observations = [{"record": "element", **local, "class_label": CCRE_CLASSES.get(local["class"], local["class"]),
                     "registry": bed.name.split(".")[0]},
                    {"record": "class_summary", "biosamples": len(columns), "classes": dict(sorted(counts.items())),
                     "scoped_to": [s.label or s.biosample or s.tissue for s in scopes]},
                    *({"record": "biosample_class", **c} for c in columns),
                    *({"record": "gene_link", "kind": kind, **x} for kind in ("crispr", "eqtl", "3d")
                      for x in links.get(kind) or [])]
    in_scope = sum(c["match"] is not None for c in columns)
    limitations = ["a cCRE class is an annotation of chromatin state, not an allele-specific experiment"]
    if scopes and not in_scope:
        limitations.append("no SCREEN core-collection biosample matches the requested context, even as a proxy")
    if not scopes:
        limitations.append("no context requested or supplied: per-biosample classes are listed, not made Evidence")
    scoped = ", ".join(s.label or str(s.biosample or s.tissue) for s in scopes)
    return AdapterResult(
        retrieval_status="records_found", observations=observations,
        coverage=Coverage(requested_scope=requested + (f", classes in {scoped}" if scopes else ""),
                          assessed_scope=(f"cCRE {acc}; {len(columns)} SCREEN core biosamples ({in_scope} in scope); "
                                          f"{sum(len(links.get(k) or []) for k in links)} gene links"),
                          limitations=limitations),
        evidence=evidence, raw={"element": local, "screen": screen, "scopes": [s.model_dump() for s in scopes]},
        message=f"{where} lies in {acc} ({local['class']})")


# --- QBiC-SELEX: qbic_inventory and qbic_tf_detail --------------------------------------------------------------------

def qbic_release(cfg: Config | None = None) -> str:
    reader = reader_for(cfg or load_config())
    s = reader.settings
    return (f"QBiC-SELEX {s['qbic_selex']}, {s['collection']} collection (Zenodo {s['zenodo_record']}), settings hash "
            f"{reader.settings_hash}")


QBIC_LIMITATIONS = ["in vitro binding predicted by HT-SELEX k-mer models: not occupancy, TF identity or causality",
                    "z is a test statistic, not a probability; p underflows to 0 above |z| of about 37.8"]


def _qbic_unready(scores: VariantScores, reader: QbicReader) -> AdapterResult:
    """A variant not cached (precompute required) or not scorable (the QBiC-SELEX status, e.g. ref_mismatch)."""
    status = "cache_miss" if scores.status == "cache_miss" else "not_applicable"
    return AdapterResult(execution_status=status, message=scores.message, cached=True,
                         raw={"variant_key": scores.key, "settings_hash": reader.settings_hash,
                              "qbic_statuses": dict(Counter(r["status"] for r in scores.rows))})


def inventory_evidence(row: dict[str, Any], sides: list[dict[str, Any]], variant: Variant, settings_hash: str,
                       p_threshold: float, *, rsids: Iterable[str] = ()) -> list[Evidence]:
    """The prediction Evidence of one gate-passing group (contract C2): one item per allele its gate-passing models
    predict to bind more (`sides`, from QbicReader.gate_sides), with direction increases for that allele and no
    context, about the TFs those models map to (own and CIS-BP-mapped alike). When the models agree, the group has
    one item; when they disagree (SPIB's model against SPI1's own at rs1427407) each allele has its own item, both
    flagged data.discordant and in the group's one independence group (one prediction source), so a claim about a TF
    is only ever linked to what that TF's own models predict. The mapping type sits only in data: it is provenance.
    about_variants names the variant scored: its supplied rsID, else `rsids` (those recorded as its own), and its
    position with alleles."""
    n_pass = sum(len(s["models"]) for s in sides)
    discordant = len(sides) > 1
    about = _about_case(variant, rsids)
    out = []
    for side in sides:
        more = _allele_base(variant, side["binds_more"])
        less = variant.ref if more == variant.alt else variant.alt
        k = len(side["models"])
        if discordant:
            which = (f"{k} of the {n_pass} models of model-sharing group {row['group_id']} ({row['dbd']}) that pass the "
                     f"Bonferroni gate (p < {p_threshold:.2g}); the group's other {n_pass - k} gate-passing model(s) "
                     f"predict more binding to the {less} allele")
        else:
            which = (f"model-sharing group {row['group_id']} ({row['dbd']}): all {k} of its gate-passing models "
                     f"(Bonferroni p < {p_threshold:.2g}; {row['n_models']} models in the group)")
        out.append(_evidence(
            evidence_class="prediction", source_ids=[side["best_model"]],
            observed_result=(f"QBiC-SELEX predicts more binding to the {more} allele than the {less} allele at "
                             f"{_where(variant)} for {which}. These models map to {_named(side['tfs'])}; best model "
                             f"{side['best_model']}, z {side['z']:+.2f}, effect {side['effect']:+.3f}."),
            data={"group_id": row["group_id"], "best_model": side["best_model"], "z": side["z"],
                  "effect": side["effect"], "p": side["p"], "models": side["models"], "discordant": discordant,
                  "n_pass": n_pass, "n_models": row["n_models"], "dbd": row["dbd"],
                  "paralog_stem": row["paralog_stem"], "mapping": side["mapping"], "settings_hash": settings_hash},
            allele=more, direction="increases", about_tfs=list(side["tfs"]), about_variants=list(about),
            independence_group=f"QBIC:{settings_hash}:{row['group_id']}", limitations=list(QBIC_LIMITATIONS)))
    return out


QBIC_INVENTORY = ToolSpec(
    name="qbic_inventory", route="computational",
    description=("Every QBiC-SELEX model-sharing group at the variant (all 997 primary models), in a neutral order "
                 "(DBD label, then group id): members tagged own or CIS-BP-mapped, paralog stem, best model, the "
                 "allele predicted to bind more, z, effect, and how many models pass the Bonferroni gate."),
    variant_types=["SNV"], provider="QBiC-SELEX precomputed scores (cache/qbic.sqlite, read only)",
    release_fn=qbic_release,
    coverage_notes=("Cached variants only: a variant without cached statistics is a cache miss (precompute "
                    "required); v9 never launches a QBiC-SELEX job. A CIS-BP-mapped model counts as the TF's own."),
    result_semantics=("records_found: one observation per group; Evidence (prediction) for every group with a model "
                      "past the gate, none chosen by z, about the TFs its gate-passing models map to. A group whose "
                      "gate-passing models disagree about the allele gets one item per allele (data.discordant). The "
                      "gate sets which groups get Evidence, never which TFs stay eligible: any TF stays queryable with "
                      "qbic_tf_detail."),
    rate_policy="parallel", evidence_classes=["prediction"])


@register_tool(QBIC_INVENTORY)
def qbic_inventory(params: dict, ctx: ToolContext) -> AdapterResult:
    reader = reader_for(_config(ctx))
    v = ctx.case.variant
    scores = reader.scores(v)
    if scores.status != "ok":
        return _qbic_unready(scores, reader)
    rows = reader.inventory(scores)
    gate = reader.gate(scores)
    sides = reader.gate_sides(scores)
    aliases = list(getattr(ctx.graph, "variant_aliases", None) or {})
    evidence = [e for r in rows if r["passes_gate"]
                for e in inventory_evidence(r, sides[r["group_id"]], v, reader.settings_hash, gate.p_threshold,
                                            rsids=aliases)]
    groups = sum(r["passes_gate"] for r in rows)
    discordant = sum(len(s) > 1 for s in sides.values())
    n_ok = sum(r["status"] == "ok" for r in scores.rows)
    return AdapterResult(
        retrieval_status="records_found", observations=rows,
        coverage=Coverage(requested_scope=f"all {len(reader.models)} primary QBiC-SELEX models at {_where(v)}",
                          assessed_scope=(f"{n_ok} of {len(reader.models)} models scored, in {len(rows)} "
                                          f"model-sharing groups"),
                          limitations=[*QBIC_LIMITATIONS, f"the Bonferroni gate (p < {gate.p_threshold:.2g}) only "
                                       "decides which groups carry Evidence; every group is listed"]),
        evidence=evidence,
        raw={"variant_key": scores.key, "provenance": reader.provenance(scores),
             "gate": {"p_threshold": gate.p_threshold, "abs_z_threshold": gate.z_threshold},
             "sequences": {"ref": scores.ref_sequence, "alt": scores.alt_sequence},
             "models": reader.model_table(scores)},
        message=(f"{len(rows)} model-sharing groups listed in neutral order (DBD label, then group id); {groups} have "
                 f"a model past the Bonferroni gate and carry Evidence ({discordant} of them with gate-passing models "
                 f"that disagree about the allele: one item per allele), {len(rows) - groups} do not; any TF stays "
                 "queryable with qbic_tf_detail"),
        cached=True)


QBIC_TF_DETAIL = ToolSpec(
    name="qbic_tf_detail", route="computational",
    description=("Every QBiC-SELEX model of one TF (its own and CIS-BP-mapped models alike) or of one model-sharing "
                 "group: z, effect, the allele predicted to bind more, the gate, and the summed site strength of both "
                 "alleles (shown only)."),
    params={"tf": ParamSpec(normalise="upper", description="an HGNC TF symbol (old names and aliases are resolved)"),
            "group": ParamSpec(normalise="upper", description=("a model-sharing group id as qbic_inventory lists it "
                                                               "(G and three digits)"))},
    variant_types=["SNV"], provider="QBiC-SELEX precomputed scores (cache/qbic.sqlite, read only)",
    release_fn=qbic_release,
    coverage_notes=("Name exactly one of tf or group. A TF with no model of its own or mapped is outside QBiC-SELEX "
                    "coverage: no record, which is no evidence about binding."),
    result_semantics=("records_found: one observation per model, Evidence (prediction) for each model past the "
                      "Bonferroni gate, about the TFs the model maps to. Site strength (summed overlapping k-mers) is "
                      "displayed, never used to order or filter."),
    rate_policy="parallel", evidence_classes=["prediction"], one_of=[["tf", "group"]])


def model_evidence(m: dict[str, Any], variant: Variant, settings_hash: str, p_threshold: float, *,
                   rsids: Iterable[str] = ()) -> Evidence:
    """The prediction Evidence of one gate-passing model, about every TF it maps to (own and mapped alike), naming
    the variant scored as inventory_evidence does."""
    more = _allele_base(variant, m["binds_more"])
    less = variant.ref if more == variant.alt else variant.alt
    return _evidence(
        evidence_class="prediction", source_ids=[m["model"]],
        observed_result=(f"QBiC-SELEX model {m['model']} (group {m['group_id']}) predicts more binding to the {more} "
                         f"allele than the {less} allele at {_where(variant)}: z {m['z']:+.2f}, effect "
                         f"{m['effect']:+.3f}; it passes the Bonferroni gate (p < {p_threshold:.2g})."),
        data={"model": m["model"], "group_id": m["group_id"], "z": m["z"], "effect": m["effect"], "p": m["p"],
              "mapping": m["mapping"], "settings_hash": settings_hash, "site_strength": m.get("site_strength")},
        allele=more, direction="increases", about_tfs=list(m["maps_to"]), about_variants=_about_case(variant, rsids),
        independence_group=f"QBIC:{settings_hash}:{m['group_id']}", limitations=list(QBIC_LIMITATIONS))


@register_tool(QBIC_TF_DETAIL)
def qbic_tf_detail(params: dict, ctx: ToolContext) -> AdapterResult:
    tf, group = params.get("tf"), params.get("group")      # exactly one: the runner enforces the spec's one_of
    reader = reader_for(_config(ctx))
    v = ctx.case.variant
    scores = reader.scores(v)
    if scores.status != "ok":
        return _qbic_unready(scores, reader)
    detail = reader.detail(scores, tf=tf, group=group)
    resolution = detail.get("resolution") or {}
    if tf is not None and resolution.get("status") != "ok":
        cands = ", ".join(resolution.get("candidates") or []) or "none"
        return AdapterResult(execution_status="not_applicable", observations=[{"record": "query", **detail}],
                             message=f"qbic_tf_detail: {tf} is {resolution.get('status')} (candidates: {cands})")
    if group is not None and detail.get("group") is None:
        return AdapterResult(execution_status="not_applicable",
                             message=f"qbic_tf_detail: there is no model-sharing group {group}")
    models = detail["models"]
    head = {"record": "query", **{k: x for k, x in detail.items() if k != "models"}}
    if not models:
        return AdapterResult(retrieval_status="no_records_found", observations=[head], cached=True,
                             message=(f"{resolution.get('symbol') or tf} has no QBiC-SELEX model, own or "
                                      "CIS-BP-mapped: outside coverage, which says nothing about binding"))
    site = reader.site_strengths(scores, [m["model"] for m in models if m["status"] == "ok"], ctx.run_dir)
    models = [{**m, "site_strength": site.get(m["model"])} for m in models]
    gate = reader.gate(scores)
    aliases = list(getattr(ctx.graph, "variant_aliases", None) or {})
    evidence = [model_evidence(m, v, reader.settings_hash, gate.p_threshold, rsids=aliases)
                for m in models if m["passes_gate"]]
    subject = resolution.get("symbol") or (detail.get("group") or {}).get("group_id")
    return AdapterResult(
        retrieval_status="records_found", observations=[head, *({"record": "model", **m} for m in models)],
        coverage=Coverage(requested_scope=f"every QBiC-SELEX model of {subject} at {_where(v)}",
                          assessed_scope=f"{len(models)} models ({sum(m['status'] == 'ok' for m in models)} scored)",
                          limitations=[*QBIC_LIMITATIONS, "site strength (summed overlapping k-mers against random "
                                       "21-mers) is shown only, never used to order or filter"]),
        evidence=evidence, raw={"variant_key": scores.key, "provenance": reader.provenance(scores), **detail,
                                "models": models},
        message=(f"{subject}: {len(models)} models, {len(evidence)} past the Bonferroni gate"), cached=True)


# --- chip_occupancy -------------------------------------------------------------------------------------------------

CHIP_OCCUPANCY = ToolSpec(
    name="chip_occupancy", route="computational",
    description=("ChIP-seq peaks over the variant from ENCODE (Factorbook peaks) and ReMap 2022, one record per "
                 "experiment accession across both; peaks within 50 bp that do not contain the variant are listed "
                 "apart as nearby. Without tf: a survey of every factor with a peak (no Evidence)."),
    params={"tf": ParamSpec(normalise="upper", description="an HGNC TF symbol: per-experiment Evidence for this TF"),
            "biosample": ParamSpec(description=("scope to this biosample: experiments in it or in a proxy of it "
                                                "(HeLa-S3 for HeLa) count; default: every biosample"))},
    variant_types=["SNV"],
    provider="Factorbook (ENCODE TF ChIP-seq peaks); ENCODE experiment search; ReMap 2022 (UCSC track ReMapTFs)",
    dataset_release="Factorbook and ENCODE as retrieved (GRCh38); ReMap 2022 (hg38)",
    coverage_notes=("Peaks are thresholded calls, 200 to 1,000 bp wide: occupancy of the element, not of the base. "
                    "Factorbook peaks carry no summit; ReMap's do. A ChIP peak is not an allele-specific readout. No "
                    "measured nulls: a locus query cannot show that either aggregator processed an experiment with no "
                    "peak there, and the two disagree for experiments both process."),
    result_semantics=("records_found: Evidence (occupancy) per experiment with a peak containing the variant. ENCODE "
                      "assays of the TF with no peak in either aggregator are listed (per biosample in the requested "
                      "or supplied context, else counted), never Evidence. no_records_found: no peak containing the "
                      "variant, which is no evidence either way."),
    rate_policy="parallel", evidence_classes=["occupancy"], network=True)


def _symbol(name: str, reg: Any, memo: dict[str, str]) -> str:
    """A ChIP target label as an HGNC symbol when the registry resolves it unambiguously, else the label."""
    if name not in memo:
        hit = reg.resolve_tf(name)
        memo[name] = hit["symbol"] if hit["status"] == "ok" else name.upper()
    return memo[name]


def _biosample_key(name: str) -> str:
    """One name per biosample across sources (Hep-G2, HepG2 and Hep G2 agree)."""
    record = load_table().record(name)
    return record.name if record else re.sub(r"[\s_-]", "", name).lower()


def _remap_records(items: list[dict], v: Variant, reg: Any, memo: dict[str, str]) -> list[dict[str, Any]]:
    out = []
    for x in items:
        start, end, summit = int(x["chromStart"]), int(x["chromEnd"]), int(x["thickStart"])
        dataset, _, rest = str(x.get("name", "")).partition(".")
        biosample = str(x.get("Biotypes") or "")
        sample = rest.partition(".")[2]                      # e.g. HL-60_CEBPB_overexpressed
        condition = sample[len(biosample):].strip("_ ").replace("_", " ") if sample.startswith(biosample) else ""
        out.append({"source": "remap", "accession": dataset, "remap_name": x.get("name"),
                    "tf": _symbol(str(x.get("TF") or ""), reg, memo), "biosample": biosample,
                    "condition": condition or None, "peak_start": start + 1, "peak_end": end,
                    "summit_distance": abs(summit + 1 - v.pos), "contains": start < v.pos <= end})
    return out


@register_tool(CHIP_OCCUPANCY)
def chip_occupancy(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return _no_http(ctx.spec.name)
    cfg, v = _config(ctx), ctx.case.variant
    reg = reader_for(cfg).registry
    rec = _Recorder(ctx.http)
    occ, err = occupancy.fetch(_provider_case(ctx, rec), reg)
    if err is not None:
        return _failed(rec, "ENCODE/Factorbook")
    remap = rec.get(chipgrade.REMAP_URL.format(chrom=f"chr{v.chrom}", start=max(0, v.pos - 1 - REMAP_WINDOW),
                                               end=v.pos + REMAP_WINDOW), timeout=120)
    items = remap.data.get("ReMapTFs") if remap.ok and isinstance(remap.data, dict) else None
    experiments = (rec.get(ENCODE_SEARCH, timeout=180).data or {}).get("@graph") or []
    memo: dict[str, str] = {}
    peaks = [{"source": "factorbook", "accession": p["experiment_accession"], "file_accession": p["file_accession"],
              "tf": occ.symbol_of.get(p["target"]) or str(p["target"]).upper(), "biosample": p["biosample"],
              "condition": None, "peak_start": int(p["chrom_start"]) + 1, "peak_end": int(p["chrom_end"]),
              "summit_distance": None, "contains": True} for p in occ.peaks]
    remap_rows = _remap_records(items or [], v, reg, memo)
    want = None
    if params.get("tf"):
        want = _symbol(str(params["tf"]), reg, memo)
    scopes = _requested_scopes(ctx, params.get("biosample")) if params.get("biosample") else []
    element = local_ccre(f"chr{v.chrom}", v.pos, cfg.path("data", "ccres"))
    elements = [element["accession"]] if element and element["distance"] == 0 else []
    limitations = ["thresholded peak calls: a peak shows occupancy of the element, not allele-specific binding"]
    if items is None:
        limitations.append("ReMap could not be read (" + (remap.error or "no data") + "): Factorbook (ENCODE) peaks "
                           "only")
    truncated = len(occ.peaks) >= 5000
    if truncated:
        limitations.append("Factorbook returned its 5,000-peak limit: the list may be incomplete")

    def in_scope(r: dict) -> str | None:
        return _match(scopes, _context(r["biosample"], v, r["condition"])) if scopes else "any"

    containing = [r for r in peaks + [r for r in remap_rows if r["contains"]] if want is None or r["tf"] == want]
    nearby = [r for r in remap_rows if not r["contains"] and (want is None or r["tf"] == want)]
    status = "records_found" if items is not None and not truncated else "incomplete"
    raw = {"requests": rec.records(), "peaks": peaks, "remap": remap_rows, "query": {"tf": want, "biosample":
                                                                                      params.get("biosample")}}
    if want is None:                          # a survey: what has a peak here, in neutral (symbol) order
        by_tf: dict[str, list[dict]] = defaultdict(list)
        for r in containing:
            by_tf[r["tf"]].append(r)
        rows = [{"record": "factor", "tf": tf, "experiments": len({r["accession"] for r in rs}),
                 "biosamples": sorted({r["biosample"] for r in rs})[:NAMED],
                 "sources": sorted({r["source"] for r in rs}), "in_scope": sum(in_scope(r) is not None for r in rs)}
                for tf, rs in sorted(by_tf.items())]
        return AdapterResult(
            retrieval_status=status if rows or status == "incomplete" else "no_records_found", observations=rows,
            coverage=Coverage(requested_scope=f"every ChIP-seq target with a peak containing {_where(v)}",
                              assessed_scope=f"{len(rows)} factors, {len(containing)} peak records",
                              limitations=[*limitations, "a survey creates no Evidence: ask with tf=SYMBOL"]),
            raw=raw, message=f"survey: {len(rows)} factors have a peak containing the variant (no Evidence)",
            cached=rec.cached, retrieval_time=rec.retrieval_time())
    merged: dict[str, dict[str, Any]] = {}
    for r in sorted(containing, key=lambda r: (r["accession"], r["source"])):
        key = r["accession"] if r["accession"].startswith("ENCSR") else str(r.get("remap_name") or r["accession"])
        m = merged.setdefault(key, {**r, "sources": []})
        if r["source"] not in m["sources"]:
            m["sources"].append(r["source"])
        if r["summit_distance"] is not None:
            m["summit_distance"] = r["summit_distance"]
    evidence, observations = [], []
    # A peak containing this variant is an observation at its position: it names the variant, so it never stands for
    # another variant's site. No source here resolves alleles, so no item carries an allele or allele_specific.
    about = _case_names(ctx)
    for key, m in sorted(merged.items()):
        match = in_scope(m)
        observations.append({"record": "experiment", "experiment": key, **{k: m[k] for k in (
            "tf", "biosample", "condition", "peak_start", "peak_end", "summit_distance", "sources")},
            "match": match})
        if match is None:
            continue
        summit = f", summit {m['summit_distance']} bp from the variant" if m["summit_distance"] is not None else ""
        sources = " and ".join("Factorbook" if s == "factorbook" else "ReMap" for s in m["sources"])
        condition = f" ({m['condition']})" if m["condition"] else ""
        evidence.append(_evidence(
            evidence_class="occupancy", source_ids=[key],
            observed_result=(f"{sources} ChIP-seq for {want} in {m['biosample']}{condition} ({key}) has a peak "
                             f"containing {_where(v)} (chr{v.chrom}:{m['peak_start']}-{m['peak_end']}{summit})."),
            data={"experiment": key, "sources": m["sources"], "peak_start": m["peak_start"], "peak_end": m["peak_end"],
                  "summit_distance": m["summit_distance"], "biosample_label": m["biosample"], "assembly": "GRCh38"},
            context=_context(m["biosample"], v, m["condition"]), about_tfs=[want], about_elements=elements,
            about_variants=about, independence_group=f"CHIP:{key}"))
    observations += [{"record": "nearby_peak", "experiment": str(r.get("remap_name")), "tf": r["tf"],
                      "biosample": r["biosample"], "peak_start": r["peak_start"], "peak_end": r["peak_end"],
                      "summit_distance": r["summit_distance"]}
                     for r in sorted(nearby, key=lambda r: str(r["remap_name"]))]
    bound = {_biosample_key(m["biosample"]) for m in merged.values()}
    assayed: dict[str, list[str]] = defaultdict(list)
    names: dict[str, str] = {}
    for x in experiments:
        label = (x.get("target") or {}).get("label") or ""
        if label and _symbol(label, reg, memo) == want:
            name = (x.get("biosample_ontology") or {}).get("term_name") or ""
            assayed[_biosample_key(name)].append(x["accession"])
            names.setdefault(_biosample_key(name), name)
    # ENCODE assays of the TF with no aggregator peak: listed in the requested (else supplied) context, counted
    # elsewhere, never Evidence (see the coverage notes: absence from two aggregators is not a measured null).
    context = scopes or _requested_scopes(ctx, None)
    unbound = [(names[k], sorted(accs)) for k, accs in sorted(assayed.items()) if k not in bound]
    near = [(name, accs, _match(context, _context(name, v))) for name, accs in unbound] if context else []
    listed = [(name, accs, match) for name, accs, match in near if match]
    observations += [{"record": "assayed_no_peak", "tf": want, "biosample": name, "experiments": accs,
                      "match": match} for name, accs, match in listed]
    shown = {name for name, _, _ in listed}
    others = sorted(name for name, _ in unbound if name not in shown)
    if others:
        observations.append({"record": "assayed_no_peak_elsewhere", "tf": want, "biosamples": len(others),
                             "examples": others[:NAMED]})
    if unbound:
        limitations.append(f"ENCODE assayed {want} in {len(unbound)} biosample(s) where neither aggregator lists a "
                           "peak containing the variant: listed, not Evidence, because a locus query cannot show that "
                           "an aggregator processed those experiments")
    return AdapterResult(        # an unread source (ReMap down, Factorbook at its limit) leaves "no peak" unshown
        retrieval_status=status if evidence or status == "incomplete" else "no_records_found",
        observations=observations,
        coverage=Coverage(requested_scope=(f"ChIP-seq for {want} at {_where(v)}"
                                           + (f" in {params['biosample']} (exact or proxy)" if scopes else "")),
                          assessed_scope=(f"{len(merged)} experiments with a peak, {len(nearby)} nearby peaks, "
                                          f"{len(assayed)} biosamples assayed by ENCODE"),
                          limitations=limitations),
        evidence=evidence, raw=raw,
        message=(f"{want}: {len(evidence)} experiments with a peak containing the variant in scope; "
                 f"{len(unbound)} ENCODE-assayed biosamples without an aggregator peak (listed, not Evidence)"),
        cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- gtex_eqtl ------------------------------------------------------------------------------------------------------

GTEX_EQTL = ToolSpec(
    name="gtex_eqtl", route="computational",
    description=("GTEx v8 significant single-tissue eQTLs for the variant: per gene and tissue, NES (the alt allele "
                 "relative to ref; NES is not a fold change) and p."),
    params={"gene": ParamSpec(normalise="upper", description=("keep this gene only (its current HGNC symbol; GTEx "
                                                                "v8's 2017 names are mapped to it)")),
            "tissue": ParamSpec(description=("a GTEx tissue (Muscle_Skeletal, Nerve_Tibial; partial names match "
                                             "several)"))},
    variant_types=["SNV"], provider="GTEx Portal API v2", dataset_release="GTEx v8 (datasetId gtex_v8)",
    coverage_notes=("The endpoint lists significant eQTLs only (up to 250 per page), so a missing gene-tissue pair is "
                    "'not reported as significant', never a tested null. Variants below 1% MAF are not tested."),
    result_semantics=("records_found: Evidence (association) per gene-tissue eQTL, allele alt, direction the sign "
                      "of NES. no_records_found: no significant eQTL reported, or the variant was not tested: no "
                      "Evidence."),
    rate_policy="serial", evidence_classes=["association"], network=True)


@register_tool(GTEX_EQTL)
def gtex_eqtl(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return _no_http(ctx.spec.name)
    v = ctx.case.variant
    reg = reader_for(_config(ctx)).registry
    tissue = re.sub(r"^gtex:\s*", "", str(params["tissue"]), flags=re.I) if params.get("tissue") else None
    gene = _gene_symbol(reg, str(params["gene"])) if params.get("gene") else None
    rec = _Recorder(ctx.http)
    case = _provider_case(ctx, rec)
    result = genetics.eqtl_lookup(case, tissue)
    if not result.ok:
        if rec.failure() is not None:
            return _failed(rec, "GTEx")
        return AdapterResult(execution_status="not_applicable", message=f"GTEx: {result.full.get('error')}")
    variant_id = case.gtex
    rows = [(_gene_symbol(reg, str(r.get("geneSymbol", "")), r.get("gencodeId")), r) for r in result.full or []]
    rows = [(sym, r) for sym, r in rows if gene is None or sym == gene]
    scope = (f"GTEx v8 significant eQTLs of {variant_id}" + (f" for {gene}" if gene else "")
             + (f" in tissues matching '{tissue}'" if tissue else ""))
    pages = next(((r.data or {}).get("paging_info") or {} for _, _, r in rec.results
                  if r.ok and r.url.startswith(genetics.GTEX + "?")), {})
    more = int(pages.get("numberOfPages") or 1) > 1
    unread = ["only the first page of results was read"] if more else []
    if not rows:
        tested = result.status == "tested_negative" or bool(result.full)
        note = ("GTEx v8 genotyped the variant (MAF >= 1%), and the significant-only endpoint lists no eQTL in scope"
                + (" on the first page read" if more else "") + ": not reported as significant, which is not a "
                "tested null" if tested else result.summary)
        return AdapterResult(retrieval_status="incomplete" if more else "no_records_found",
                             coverage=Coverage(requested_scope=scope, assessed_scope=note, limitations=unread),
                             raw={"requests": rec.records()}, message=note[:300], cached=rec.cached,
                             retrieval_time=rec.retrieval_time())
    evidence, observations = [], []
    about = _case_names(ctx)                                   # the variant queried (GTEx's id names nothing)
    for sym, r in sorted(rows, key=lambda x: (x[0], x[1]["tissueSiteDetailId"])):
        t, nes, named = r["tissueSiteDetailId"], float(r["nes"]), str(r.get("geneSymbol", ""))
        alias = f" (GTEx v8 name {named})" if named.upper() != sym else ""
        observations.append({"record": "eqtl", "gene": sym, "gtex_symbol": named, "gencode_id": r.get("gencodeId"),
                             "tissue": t, "nes": nes, "p": r["pValue"], "effect_allele": v.alt})
        evidence.append(_evidence(
            evidence_class="association", source_ids=[f"GTEx:v8:{variant_id}"],
            observed_result=(f"GTEx v8 reports a significant single-tissue eQTL for {sym}{alias} in {t}: NES "
                             f"{nes:+.3f} for the {v.alt} allele relative to {v.ref} (p {float(r['pValue']):.2g}); NES "
                             "is a normalised effect size, not a fold change."),
            data={"gene": sym, "gencode_id": r.get("gencodeId"), "tissue": t, "nes": nes, "p": r["pValue"],
                  "dataset": "gtex_v8", "variant_id": variant_id},
            allele=v.alt, direction="increases" if nes > 0 else "decreases",
            context=_context(t.replace("_", " "), v), about_genes=[sym], about_variants=list(about),
            independence_group=_gtex_group(variant_id, r.get("gencodeId") or sym, t)))
    return AdapterResult(
        retrieval_status="incomplete" if more else "records_found", observations=observations,
        coverage=Coverage(requested_scope=scope, assessed_scope=f"{len(rows)} significant eQTLs",
                          limitations=["significant eQTLs only: absent pairs are not tested nulls",
                                       "association, not a causal element-gene or TF-gene link", *unread]),
        evidence=evidence, raw={"requests": rec.records(), "rows": [r for _, r in rows]},
        message=f"{len(rows)} significant GTEx v8 eQTLs (NES for the {v.alt} allele)", cached=rec.cached,
        retrieval_time=rec.retrieval_time())


# --- tf_expression and depmap_context (local) -----------------------------------------------------------------------

@lru_cache(maxsize=1)
def _gtex_tissues() -> tuple[str, ...]:
    return tuple(get_expression().gtex.columns)


def _expression_contexts(label: str, v: Variant) -> list[tuple[str, str]]:
    """(an Expression context string, the label of what it measures) for a context: the DepMap line of a cell line,
    else the GTEx tissue(s) of the same tissue, else nothing (unknown). A GTEx:<tissue> or DepMap:<id> label is taken
    as given (a DepMap line measures that line, by its name where the biosample table knows it)."""
    if re.match(r"(gtex|depmap):", label, re.I):
        body = label.split(":", 1)[1].strip()
        record = load_table().record(body) if label.lower().startswith("depmap:") else None
        return [(label, record.name if record else body)]
    expr = get_expression()
    scope = scope_from_label(label, variant=v)
    record = load_table().record(scope.biosample) if scope.biosample else None
    if record and record.depmap and record.depmap in expr.depmap.index:
        return [(f"DepMap:{record.depmap}", record.name)]
    exact = [t for t in _gtex_tissues() if compare_context(scope, scope_from_label(t)) == "exact"]
    if exact:
        return [(f"GTEx:{t}", t) for t in exact]
    same = [t for t in _gtex_tissues() if scope.tissue and scope_from_label(t).tissue == scope.tissue]
    return [(f"GTEx:{t}", t) for t in same]


def _line_set_scope(name: str, v: Variant) -> ContextScope:
    """The context of a median over a set of DepMap cancer cell lines (a lineage or a subtype), named as that set and
    of cell-line kind. It never matches an organ or any one line exactly: 27 liver-lineage cancer lines are neither
    liver tissue nor Hep3B. Where the name says an organ, the set is a proxy for that tissue."""
    scope = ContextScope(label=name, biosample=name, biosample_kind="cell_line", source="evidence")
    return normalise_scope(scope, variant=v) or scope


def _depmap_line_expression(gene: str, line: str, line_name: str, tpm: float, v: Variant) -> Evidence:
    """A gene's expression in one DepMap line. One matrix value is one observation, so tf_expression and
    depmap_context build the identical item and the graph keeps it once, in one independence group."""
    return _evidence(
        evidence_class="expression", source_ids=[f"DepMap:{line}"],
        observed_result=f"{gene} is expressed at {tpm:g} TPM in {line_name} (DepMap line {line}).",
        data={"tpm": tpm, "line": line, "source": "DepMap expression"}, context=_context(line_name, v),
        about_tfs=[gene], about_genes=[gene], independence_group=f"DEPMAP:{gene}:expression:{line}",
        limitations=["expression is permissive: it neither shows nor excludes occupancy"])


TF_EXPRESSION = ToolSpec(
    name="tf_expression", route="computational",
    description=("A TF's (or gene's) expression level in a context, from local data: the DepMap line of a cell line, "
                 "else GTEx v8 median TPM for the matching tissue. Reported as a level, never as a threshold call."),
    params={"tf": ParamSpec(required=True, normalise="upper", description="an HGNC symbol"),
            "context": ParamSpec(description="a cell line, tissue, GTEx:<tissue> or DepMap:<ACH id>; default: the "
                                             "supplied context")},
    assemblies=[], provider="local DepMap expression and GTEx v8 median TPM",
    dataset_release="GTEx v8 median TPM; DepMap expression (Biomni copy, release not stated)",
    coverage_notes=("Expression is permissive evidence, not occupancy; a low value never removes a TF. A context with "
                    "no matching line or tissue is reported as unknown."),
    result_semantics=("records_found: Evidence (expression) per resolved context, a TPM level with no direction. "
                      "no_records_found: no context, an unknown context or a gene absent from the data."),
    rate_policy="parallel", evidence_classes=["expression"])


@register_tool(TF_EXPRESSION)
def tf_expression(params: dict, ctx: ToolContext) -> AdapterResult:
    v = ctx.case.variant
    reg = reader_for(_config(ctx)).registry
    name = reg.resolve_tf(str(params["tf"]))
    symbol = name["symbol"] if name["status"] == "ok" else str(params["tf"])
    labels = [str(params["context"])] if params.get("context") else [
        s.label or s.biosample or s.tissue or "" for s in _requested_scopes(ctx, None)]
    observations, evidence = [], []
    expr = get_expression()
    for label in labels:
        resolved = _expression_contexts(label, v)
        if not resolved:
            observations.append({"record": "context", "context": label, "status": "unknown",
                                 "note": "no DepMap line or GTEx tissue matches this context"})
            continue
        for text, measured in resolved:
            try:
                parsed = expr.parse(text)
                value = expr.tf_expression([symbol], parsed)[symbol]
            except ContextError as e:            # a GTEx:/DepMap: label naming no tissue or line in the data
                observations.append({"record": "context", "context": label, "status": "unknown", "note": str(e)})
                continue
            observations.append({"record": "expression", "tf": symbol, "context": label, "source_context": text,
                                 "tpm": value.get("tpm"), "source": value["source"], **(
                                     {"n_lines": value["n_lines"]} if "n_lines" in value else {})})
            if value.get("tpm") is None:
                continue
            if parsed.kind == "depmap_line":
                evidence.append(_depmap_line_expression(symbol, str(parsed.value), measured, value["tpm"], v))
                continue
            subtype = parsed.kind == "depmap_subtype"
            where = (f"{value.get('n_lines')} DepMap {parsed.value} cancer cell lines (median)" if subtype
                     else measured)
            evidence.append(_evidence(
                evidence_class="expression", source_ids=[text],
                observed_result=f"{symbol} is expressed at {value['tpm']:g} TPM in {where} ({value['source']}).",
                data={"tpm": value["tpm"], "source": value["source"], "source_context": text,
                      **({"n_lines": value.get("n_lines")} if subtype else {})},
                context=_line_set_scope(f"DepMap {parsed.value} cell lines", v) if subtype else _context(measured, v),
                about_tfs=[symbol], about_genes=[symbol], independence_group=f"EXPRESSION:{text}:{symbol}",
                limitations=["expression is permissive: it neither shows nor excludes occupancy"]))
    if not labels:
        observations.append({"record": "context", "context": None, "status": "unknown",
                             "note": "no context was requested or supplied: expression says nothing without one"})
    return AdapterResult(
        retrieval_status="records_found" if evidence else "no_records_found", observations=observations,
        coverage=Coverage(requested_scope=f"{symbol} expression in {', '.join(labels) or 'no context'}",
                          assessed_scope=f"{len(evidence)} context(s) with a value",
                          limitations=["DepMap release not stated (Biomni copy); GTEx v8 medians"]),
        evidence=evidence, raw={"tf": symbol, "resolution": name["status"], "observations": observations},
        message=f"{symbol}: {len(evidence)} expression level(s)" if evidence else
        f"{symbol}: no expression value for the context")


DEPMAP_CONTEXT = ToolSpec(
    name="depmap_context", route="computational",
    description=("DepMap CRISPR gene effect (dependency) and expression of a gene in a cell line and its lineage, from "
                 "local data, as values: no dependency or expression call is made."),
    params={"gene": ParamSpec(required=True, normalise="upper", description="an HGNC symbol (a TF or a target gene)"),
            "lineage": ParamSpec(description="a DepMap Oncotree lineage (Kidney, Bowel, ...); default: the line's"),
            "context": ParamSpec(description="a cell line; default: the supplied context's DepMap line")},
    assemblies=[], provider="local DepMap (CRISPRGeneEffect, expression, models)",
    dataset_release=("DepMap CRISPRGeneEffect and expression (Biomni copies, release not stated); "
                     "CRISPRInferredCommonEssentials (Public 26Q3)"),
    coverage_notes=("Gene-level phenotypes and levels, not evidence of this variant's effect. Gene effect: 0 is no "
                    "effect, -1 the median of common-essential genes."),
    result_semantics=("records_found: Evidence (dependency_screen, expression) for the line and the lineage median. "
                      "no_records_found: no line or lineage, or the gene is absent from the screens."),
    rate_policy="parallel", evidence_classes=["dependency_screen", "expression"])


@register_tool(DEPMAP_CONTEXT)
def depmap_context(params: dict, ctx: ToolContext) -> AdapterResult:
    cfg, v, gene = _config(ctx), ctx.case.variant, str(params["gene"])
    models, effects, expr = depmap._models(), depmap._effects(), get_expression().depmap
    labels = [str(params["context"])] if params.get("context") else [
        s.label or s.biosample or "" for s in _requested_scopes(ctx, None)]
    records = [load_table().record(scope_from_label(x, variant=v).biosample or x) for x in labels]
    line = next((r.depmap for r in records if r and r.depmap), None)
    line_name = next((r.name for r in records if r and r.depmap), None)
    own_lineage = models.at[line, "OncotreeLineage"] if line in models.index else None
    lineage = params.get("lineage") or (own_lineage if isinstance(own_lineage, str) else None)
    members = list(models.index[models.OncotreeLineage.astype(str).str.casefold() == str(lineage).casefold()]) \
        if lineage else []
    entrez = next((e for e, s in reader_for(cfg).registry.entrez_to_symbol.items() if s == gene), None)
    common = depmap.is_common_essential(gene, entrez, cfg.path("data", "depmap_common_essentials"))
    values: dict[str, Any] = {"gene": gene, "line": line, "line_name": line_name, "lineage": lineage,
                              "common_essential": common}
    evidence = []
    group = f"DEPMAP:{gene}"
    lines_of = f"DepMap {lineage} lineage cell lines"          # a lineage median's context: the set, not an organ
    if gene in effects.columns:
        col = effects[gene].dropna()
        values["all_lines_median_effect"] = round(float(col.median()), 3)
        values["all_lines_n"] = int(len(col))
        if line in col.index:
            values["line_effect"] = round(float(col[line]), 3)
            evidence.append(_evidence(
                evidence_class="dependency_screen", source_ids=[f"DepMap:{line}"],
                observed_result=(f"DepMap CRISPR gene effect of {gene} in {line_name} ({line}) is "
                                 f"{values['line_effect']:+.2f} (0 = no effect, -1 = median common-essential gene)."),
                data={"gene_effect": values["line_effect"], "common_essential": common, "line": line},
                context=_context(line_name, v), about_genes=[gene], independence_group=f"{group}:crispr:{line}"))
        in_lineage = col[col.index.isin(members)]
        if len(in_lineage):
            values["lineage_median_effect"] = round(float(in_lineage.median()), 3)
            values["lineage_n"] = int(len(in_lineage))
            evidence.append(_evidence(
                evidence_class="dependency_screen", source_ids=[f"DepMap:lineage:{lineage}"],
                observed_result=(f"DepMap CRISPR gene effect of {gene} has a median of "
                                 f"{values['lineage_median_effect']:+.2f} across {len(in_lineage)} {lineage}-lineage "
                                 "cancer cell lines."),
                data={"median_gene_effect": values["lineage_median_effect"], "n_lines": len(in_lineage),
                      "lineage": lineage, "common_essential": common},
                context=_line_set_scope(lines_of, v), about_genes=[gene],
                independence_group=f"{group}:crispr:{lineage}"))
    if gene in expr.columns:
        if line in expr.index:
            values["line_tpm"] = round(float(expr.at[line, gene]), 2)
            evidence.append(_depmap_line_expression(gene, line, str(line_name), values["line_tpm"], v))
        lineage_tpm = expr.loc[expr.index.isin(members), gene]
        if len(lineage_tpm):
            values["lineage_median_tpm"] = round(float(lineage_tpm.median()), 2)
            evidence.append(_evidence(
                evidence_class="expression", source_ids=[f"DepMap:lineage:{lineage}"],
                observed_result=(f"{gene} has a median of {values['lineage_median_tpm']:g} TPM across "
                                 f"{len(lineage_tpm)} {lineage}-lineage cancer cell lines (DepMap)."),
                data={"median_tpm": values["lineage_median_tpm"], "n_lines": int(len(lineage_tpm)),
                      "lineage": lineage}, context=_line_set_scope(lines_of, v), about_genes=[gene],
                about_tfs=[gene], independence_group=f"{group}:expression:{lineage}"))
    note = None if line or lineage else "no cell line or lineage: give lineage, or supply a context with a DepMap line"
    return AdapterResult(
        retrieval_status="records_found" if evidence else "no_records_found",
        observations=[{"record": "depmap", **values, **({"note": note} if note else {})}],
        coverage=Coverage(requested_scope=f"{gene} in {line_name or 'no line'} / {lineage or 'no lineage'}",
                          assessed_scope=f"{len(evidence)} value(s)",
                          limitations=["gene-level phenotypes and levels: not evidence of this variant's effect",
                                       "DepMap release not stated (Biomni copies)"]),
        evidence=evidence, raw=values, message=note or f"{gene}: {len(evidence)} DepMap value(s)")


# --- gwas_associations ----------------------------------------------------------------------------------------------

GWAS_ASSOCIATIONS = ToolSpec(
    name="gwas_associations", route="computational",
    description=("GWAS Catalog associations reported for the variant's rsID (every page, up to 700 rows): study, "
                 "trait, effect allele, effect and p."),
    params={"trait": ParamSpec(description="keep associations whose trait matches (words or an EFO id)")},
    provider="GWAS Catalog REST v2", dataset_release="GWAS Catalog REST v2 (the API reports no release)",
    coverage_notes=("Exact rsID matches only: the supplied rsID, else the rsID dbSNP gives this exact variant (recorded "
                    "by fact collection). A tag-SNP association is not a causal assignment. Ancestry sits on the "
                    "study record, which is not fetched (one request per study). The effect allele of an A/T or C/G "
                    "variant is not placed (the Catalog does not fix its strand)."),
    result_semantics=("records_found: Evidence (association) per association row, with the effect allele and the "
                      "direction the Catalog states (beta or odds ratio). no_records_found: every association was "
                      "read and none is in scope, which is no record, not absence of a phenotype effect. incomplete: "
                      "some pages were not read (page cap or failure), whether or not rows in scope were found."),
    rate_policy="serial", evidence_classes=["association"], network=True)


def _rsid(ctx: ToolContext) -> tuple[str | None, list[str]]:
    """(the rsID the Catalog is searched by, the case's other recorded rsIDs): the supplied rsID, else the lowest
    rsID code recorded as the case variant's own (graph.variant_aliases: dbSNP's rsID at the exact position and
    alleles, from collect_facts). A rsID merely co-located with the variant may be another allele's, whose
    associations are not this variant's, so it is never used."""
    if ctx.case.variant.rsid:
        return ctx.case.variant.rsid, []
    aliases = sorted(ctx.graph.variant_aliases, key=lambda r: int(r[2:]))
    return (aliases[0], aliases[1:]) if aliases else (None, [])


def _gwas_effect(a: dict) -> tuple[float | None, str, str]:
    """(value, direction, text) of a Catalog row: a beta with "unit increase/decrease", or an odds ratio (the v2 API
    gives it as text, sometimes with a note: "1.23 (Oncoarray)"). OR > 1 means the effect allele raises the odds."""
    beta = str(a.get("beta") or "").strip()
    m = re.fullmatch(r"(\S+)\s*(.*?)\s*(increase|decrease)", beta)
    value = _number(m.group(1)) if m else None
    if m and value is not None and value >= 0:
        return value, "increases" if m.group(3) == "increase" else "decreases", beta
    odds = _number(a.get("or_value"))
    if odds is not None and odds > 0:
        text = f"OR {' '.join(str(a['or_value']).split())}"
        return odds, "increases" if odds > 1 else "decreases" if odds < 1 else "unspecified", text
    return None, "unspecified", "effect not stated"


def _effect_allele(stated: str | None, v: Variant) -> tuple[str | None, str | None]:
    """(the case allele the Catalog's effect allele names, why it cannot be placed). An A/T or C/G variant reads the
    same on both strands, and the Catalog does not fix which strand an author reported, so its allele is never placed
    (the direction would be inverted half the time). A base that is neither allele is not flipped to the other strand
    either: many rsIDs are multiallelic (rs1427407 is T/C/G), so it may name another allele."""
    if not stated or not re.fullmatch(r"[ACGT]+", stated):
        return None, None
    if {v.ref, v.alt} in STRAND_AMBIGUOUS:
        return None, (f"{v.ref}>{v.alt} reads the same on both strands, and the Catalog does not say which strand "
                      f"effect allele {stated} is on: not placed, so no direction")
    if stated in (v.ref, v.alt):
        return stated, None
    return None, (f"the stated effect allele {stated} is neither ref {v.ref} nor alt {v.alt} (another strand, or "
                  "another allele of the rsID): not placed, so no direction")


def _gwas_variants(a: dict, rsid: str) -> list[str]:
    """The variants a Catalog association row is about, as the Catalog names them: the rsID searched (the case
    variant's), then the row's other SNPs in its order (a haplotype or a SNP-SNP interaction lists several)."""
    names: dict[str, str] = {rsid.casefold(): rsid}
    for x in a.get("snp_allele") or []:
        name = " ".join(str(x.get("rs_id") or "").split())
        if name:
            names.setdefault(name.casefold(), name)
    return list(names.values())


def _gwas_evidence(a: dict, rsid: str, v: Variant) -> tuple[dict, Evidence]:
    """One Catalog association row: its observation and its association Evidence, in the study's independence group
    (shared with Open Targets' credible sets from the same study: one study is one measurement). about_variants names
    the row's own variants: a row of several SNPs (a haplotype, an interaction) is about all of them, says so, and
    is never written as an association of the searched rsID alone."""
    alleles = [x.get("effect_allele") for x in a.get("snp_allele") or [] if x.get("rs_id") == rsid]
    stated = str(alleles[0]).upper().strip() if alleles and alleles[0] else None
    allele, unplaced = _effect_allele(stated, v)
    value, direction, effect_text = _gwas_effect(a)
    if allele is None:
        direction = "unspecified"            # a direction with no placeable allele is not reported as one
    efo = [(t.get("efo_id"), t.get("efo_trait")) for t in a.get("efo_traits") or []]
    reported = [str(t) for t in a.get("reported_trait") or []]
    trait = reported[0] if reported else (efo[0][1] if efo else "trait not stated")
    pmid = a.get("pubmed_id")
    study = a.get("accession_id")
    p_text = (f"{a['pvalue_mantissa']}e{a['pvalue_exponent']}" if a.get("pvalue_mantissa") is not None
              and a.get("pvalue_exponent") is not None else str(a.get("p_value")))
    row = {"record": "association", "accession": study, "trait": trait, "reported_traits": reported,
           "efo": [{"id": i, "label": label} for i, label in efo], "effect_allele": stated, "effect": value,
           "effect_text": effect_text, "ci": [_number(a.get("ci_lower")), _number(a.get("ci_upper"))], "p": p_text,
           "risk_frequency": a.get("risk_frequency"), "pubmed_id": pmid, "first_author": a.get("first_author"),
           "mapped_genes": a.get("mapped_genes") or []}
    shown = stated if stated and stated != "?" else "not stated"
    variants = _gwas_variants(a, rsid)
    subject, several = rsid, []
    if len(variants) > 1:
        kind = ("haplotype" if a.get("multi_snp_haplotype") else
                "SNP-SNP interaction" if a.get("snp_interaction") else "multi-SNP association")
        subject = f"a {kind} of {len(variants)} variants including {rsid}"
        several = [f"the association is of a {kind} of {len(variants)} variants ({_named(variants)}), not of {rsid} "
                   "alone"]
        row["variants"] = variants
    ev = _evidence(
        evidence_class="association",
        source_ids=[f"GWAS:{study}"] + ([f"PMID:{pmid}"] if pmid else []),
        observed_result=(f"GWAS Catalog {study} ({a.get('first_author') or 'author not stated'}): {subject} is "
                         f"associated with {trait}; effect allele {shown}, {effect_text}, p {p_text}."),
        data={k: row[k] for k in ("accession", "effect_allele", "effect", "effect_text", "ci", "p", "risk_frequency",
                                  "mapped_genes")},
        allele=allele, direction=direction,
        about_traits=sorted({x for i, label in efo for x in (i, label) if x} | set(reported)), about_variants=variants,
        independence_group=f"GWAS-STUDY:{study}",
        limitations=["a tag-SNP association is not a causal assignment", "ancestry not fetched", *several,
                     *([unplaced] if unplaced else [])])
    return row, ev


def _trait_match(query: str, names: Iterable[str]) -> bool:
    """The query as whole words (or an exact id) in a trait name: "LDL cholesterol" matches "LDL cholesterol
    levels" but not "VLDL cholesterol"."""
    return trait_query_match(query, names)


@register_tool(GWAS_ASSOCIATIONS)
def gwas_associations(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return _no_http(ctx.spec.name)
    rsid, others = _rsid(ctx)
    if not rsid:
        return AdapterResult(execution_status="not_applicable",
                             message=("gwas_associations: no rsID for this variant (none supplied, and fact collection "
                                      "recorded no dbSNP rsID with its exact alleles); the Catalog is searched by "
                                      "rsID"))
    rec = _Recorder(ctx.http)
    url: str | None = f"{genetics.GWAS}?rs_id={rsid}&size={GWAS_PAGE_SIZE}"
    rows: list[dict] = []
    total, pages, broken = 0, 0, None
    while url and pages < GWAS_MAX_PAGES:
        r = rec.get(url, timeout=120)
        if not r.ok:
            broken = r
            break
        pages += 1
        data = r.data if isinstance(r.data, dict) else {}
        rows += (data.get("_embedded") or {}).get("associations") or []
        total = int((data.get("page") or {}).get("totalElements") or len(rows))
        url = ((data.get("_links") or {}).get("next") or {}).get("href")
    if pages == 0 and broken is not None:
        return _failed(rec, "GWAS Catalog", broken)
    trait = params.get("trait")
    built = [_gwas_evidence(a, rsid, ctx.case.variant) for a in rows]
    kept = [(row, ev) for row, ev in built if not trait or _trait_match(str(trait), ev.about_traits)]
    incomplete = len(rows) < total
    limitations = ["exact rsID matches only", "ancestry is on the study record, which this tool does not fetch"]
    if others:
        limitations.append(f"searched by {rsid}; the case variant's other recorded rsID(s) {', '.join(others)} were "
                           "not searched")
    if incomplete:
        limitations.append(f"read {len(rows)} of {total} associations ({pages} page(s); "
                           + (f"the next page failed: {broken.error}" if broken else f"cap {GWAS_MAX_PAGES} pages")
                           + ")")
    # Unread pages may hold associations in scope: "no record" only when every association was read.
    status = "incomplete" if incomplete else "records_found" if kept else "no_records_found"
    if kept:
        message = f"{rsid}: {len(kept)} GWAS Catalog associations" + (f" ({len(rows)} of {total} read)"
                                                                      if incomplete else "")
    elif incomplete:
        message = (f"{rsid}: no association in scope among the {len(rows)} of {total} read; the rest were not read, "
                   "so this is not a record of absence")
    else:
        message = f"{rsid}: no exact-rsID association in scope (no record, not a negative)"
    return AdapterResult(
        retrieval_status=status, observations=[row for row, _ in kept],
        coverage=Coverage(requested_scope=f"GWAS Catalog associations of {rsid}"
                          + (f" with traits matching '{trait}'" if trait else ""),
                          assessed_scope=f"{len(rows)} of {total} associations read; {len(kept)} in scope",
                          limitations=limitations),
        evidence=[ev for _, ev in kept], raw={"requests": rec.records(), "associations": rows},
        message=message, cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- credible_sets_l2g ----------------------------------------------------------------------------------------------

OT_QUERY = """query V2MCredibleSets($v: String!, $ids: [String!]!, $index: Int!) {
  meta { name apiVersion { x y z suffix } dataVersion { year month iteration } }
  variant(variantId: $v) {
    id rsIds referenceAllele alternateAllele
    credibleSets(page: {index: $index, size: %d}, studyTypes: [gwas]) {
      count
      rows {
        studyLocusId studyId finemappingMethod confidence variant { id }
        study { id traitFromSource projectId pubmedId publicationFirstAuthor publicationDate nSamples
                diseases { id name } discoverySamples { ancestry sampleSize } }
        locus(variantIds: $ids, page: {index: 0, size: 1}) {
          rows { variant { id } posteriorProbability is95CredibleSet is99CredibleSet beta } }
        l2GPredictions(page: {index: 0, size: %d}) { count rows { target { id approvedSymbol } score } }
        colocalisation(studyTypes: [eqtl, pqtl, sqtl], page: {index: 0, size: %d}) { count rows {
          colocalisationMethod rightStudyType h3 h4 clpp betaRatioSignAverage
          otherStudyLocus { studyLocusId studyType study { id projectId target { approvedSymbol }
                                                           biosample { biosampleName } } } } }
      }
    }
  }
}""" % (OT_PAGE_SIZE, OT_L2G_ROWS, OT_COLOC_ROWS)

CREDIBLE_SETS_L2G = ToolSpec(
    name="credible_sets_l2g", route="computational",
    description=("Open Targets GWAS credible sets containing the variant: per study locus, the variant's PIP, the "
                 "fine-mapping method, L2G gene scores and molecular-QTL colocalisations, with the release. Without a "
                 "trait (or a supplied disease) it returns a survey by trait and no Evidence."),
    params={"trait": ParamSpec(description="keep credible sets whose trait or disease matches (words or an EFO id)"),
            "gene": ParamSpec(normalise="upper", description="keep L2G rows and colocalisations of this gene")},
    variant_types=["SNV"], provider="Open Targets Platform GraphQL",
    dataset_release="Open Targets Platform (release read from meta at retrieval)",
    coverage_notes=("Scores stay per credible set: never a maximum across unrelated studies. L2G is a model output "
                    "whose features include colocalisation and distance, so it is not independent of them. Offline, "
                    "only the cached first 200 credible sets of an older query may exist (no release, no study-locus "
                    "ids, no colocalisation): marked incomplete."),
    result_semantics=("records_found: Evidence per credible set in scope (statistical_inference), per L2G row "
                      "(precomputed_prediction) and per colocalisation (statistical_inference), all in the GWAS "
                      "study's independence group (shared with the Catalog's rows of that study). no_records_found: "
                      "every credible set was read and none containing the variant is in scope. incomplete: some sets "
                      "were not read (or only the older cached query was), whether or not sets in scope were found."),
    rate_policy="serial", evidence_classes=["statistical_inference", "precomputed_prediction"], network=True)


def _ot_sets_v9(rec: _Recorder, vid: str) -> tuple[list[dict], int, str | None, HttpResult | None]:
    """Paged GWAS credible sets from the v9 query: (rows, count, release, failure of the first page or None)."""
    rows, count, release = [], 0, None
    for index in range(OT_MAX_PAGES):
        r = rec.query(genetics.OT, {"query": OT_QUERY, "variables": {"v": vid, "ids": [vid], "index": index}})
        data = (r.data or {}).get("data") if r.ok and isinstance(r.data, dict) else None
        if data is None:
            if index:
                rec.partial.append(f"credible-set page {index} failed: {r.error or 'no data'}")
            return rows, count, release, (r if index == 0 else None)
        meta = data.get("meta") or {}
        dv, api = meta.get("dataVersion") or {}, meta.get("apiVersion") or {}
        release = (f"Open Targets Platform {dv.get('year')}.{dv.get('month')} (API {api.get('x')}.{api.get('y')}."
                   f"{api.get('z')})") if dv else release
        sets = ((data.get("variant") or {}).get("credibleSets") or {})
        count = int(sets.get("count") or 0)
        rows += sets.get("rows") or []
        if len(rows) >= count or not sets.get("rows"):
            break
    return rows, count, release, None


def _ot_sets_legacy(rec: _Recorder, ctx: ToolContext) -> tuple[list[dict], int]:
    """The v8 query (first 200 credible sets of every type), through the provider: the only Open Targets response
    cached for the gold and development variants. GWAS sets only, in the v9 row shape (no study-locus ids)."""
    result = genetics.finemap_lookup(_provider_case(ctx, rec))
    if not result.ok or not isinstance(result.full, dict):
        return [], 0
    count = 0
    for _, _, r in rec.results:
        variant = ((r.data or {}).get("data") or {}).get("variant") if r.ok and isinstance(r.data, dict) else None
        if variant:
            count = int((variant.get("credibleSets") or {}).get("count") or 0)
    rows = [{"studyLocusId": None, "studyId": x["study"]["id"], "finemappingMethod": None, "confidence": None,
             "variant": None, "study": {"id": x["study"]["id"], "traitFromSource": x["study"].get("traitFromSource"),
                                        "diseases": []},
             "locus": x.get("locus"), "l2GPredictions": {"rows": [{"target": {"id": None, "approvedSymbol":
                                                                              p["target"]["approvedSymbol"]},
                                                                   "score": p["score"]}
                                                                  for p in x["l2GPredictions"]["rows"]]},
             "colocalisation": None} for x in result.full.get("gwas") or []]
    return rows, count


def _set_traits(row: dict) -> list[str]:
    study = row.get("study") or {}
    return [x for x in [study.get("traitFromSource")] + [d.get("name") for d in study.get("diseases") or []]
            + [d.get("id") for d in study.get("diseases") or []] if x]


def _pip(row: dict, vid: str) -> dict:
    hit = next((x for x in (row.get("locus") or {}).get("rows") or []
                if (x.get("variant") or {}).get("id", vid) == vid), None)
    return hit or {}


def _ot_evidence(row: dict, vid: str, release: str, gene: str | None, v: Variant,
                 about: list[str]) -> list[Evidence]:
    """Evidence of one credible set in scope: the set (PIP), its L2G rows and its molecular-QTL colocalisations, all
    in the GWAS study's independence group: L2G and colocalisation are derived from the credible set, the set from
    the study's summary statistics, and the GWAS Catalog's rows of the same study (GCST id) report that same
    measurement, so none of them counts as independent of the others. Every item names the case variant (`about`):
    the PIP is the case variant's own, and the set was found because it holds the case variant. The lead variant is
    named in the text and data only: naming it would let a set the case variant merely belongs to stand for the
    lead (and a lead alone would refuse the item for claims about the case variant)."""
    study = row.get("study") or {}
    sid, lead = row.get("studyLocusId"), (row.get("variant") or {}).get("id")
    traits = _set_traits(row)
    trait = study.get("traitFromSource") or (traits[0] if traits else "trait not stated")
    group = f"GWAS-STUDY:{study['id']}" if study.get("id") else f"OT:{sid}"
    ident = f"credible set {sid} of {study.get('id')}" if sid else f"a credible set of {study.get('id')}"
    locus = _pip(row, vid)
    pip = locus.get("posteriorProbability")
    sources = [f"OT:{sid}"] if sid else [f"OT:{study.get('id')}"]
    if study.get("pubmedId"):
        sources.append(f"PMID:{study['pubmedId']}")
    method = f"{row.get('finemappingMethod')}: {row.get('confidence')}" if row.get("finemappingMethod") else \
        "method not recorded"
    out = [_evidence(
        evidence_class="statistical_inference", source_ids=sources,
        observed_result=(f"Open Targets ({release}): {vid} is in {ident} ({trait}; {method}"
                         + (f"; lead variant {lead}" if lead else "") + ")"
                         + (f" with posterior inclusion probability {pip:.3g}." if pip is not None else ".")),
        data={"study_locus_id": sid, "study_id": study.get("id"), "pip": pip, "in_95_set": locus.get("is95CredibleSet"),
              "in_99_set": locus.get("is99CredibleSet"), "variant_beta": locus.get("beta"), "lead_variant": lead,
              "finemapping_method": row.get("finemappingMethod"), "confidence": row.get("confidence"),
              "n_samples": study.get("nSamples"), "ancestry": study.get("discoverySamples"), "release": release},
        about_traits=traits, about_variants=list(about), independence_group=group,
        limitations=["a PIP from a PICS set on a reported top hit is not comparable to a SuSiE PIP",
                     "the lead variant's statistics belong to the lead, not to this variant"])]
    for p in (row.get("l2GPredictions") or {}).get("rows") or []:
        symbol = str((p.get("target") or {}).get("approvedSymbol") or "").upper()
        if not symbol or (gene and symbol != gene):
            continue
        out.append(_evidence(
            evidence_class="precomputed_prediction", source_ids=sources,
            observed_result=(f"Open Targets L2G ({release}) scores {symbol} {p['score']:.3f} for {ident} ({trait})."),
            data={"study_locus_id": sid, "study_id": study.get("id"), "score": p["score"], "gene": symbol,
                  "gene_id": (p.get("target") or {}).get("id"), "release": release},
            about_genes=[symbol], about_traits=traits, about_variants=list(about), independence_group=group,
            limitations=["a model output per credible set and gene; its features include distance and "
                         "colocalisation, so it is not independent of them"]))
    for c in ((row.get("colocalisation") or {}).get("rows") or []):
        other = c.get("otherStudyLocus") or {}
        ostudy = other.get("study") or {}
        target = str(((ostudy.get("target") or {}).get("approvedSymbol")) or "").upper()
        if not target or (gene and target != gene):
            continue
        biosample = ((ostudy.get("biosample") or {}).get("biosampleName")) or ""
        h4 = c.get("h4")
        out.append(_evidence(
            evidence_class="statistical_inference", source_ids=[*sources, f"OT:{other.get('studyLocusId')}"],
            observed_result=(f"Open Targets ({release}): {ident} ({trait}) colocalises with the "
                             f"{c.get('rightStudyType')} credible set of {target} in "
                             f"{biosample or 'an unstated biosample'} "
                             f"({ostudy.get('projectId')}; {c.get('colocalisationMethod')}"
                             + (f", H4 {h4:.3f}" if h4 is not None else "")
                             + (f", CLPP {c['clpp']:.3f}" if c.get("clpp") is not None else "") + ")."),
            data={"study_locus_id": sid, "other_study_locus_id": other.get("studyLocusId"),
                  "other_study_id": ostudy.get("id"), "method": c.get("colocalisationMethod"), "h3": c.get("h3"),
                  "h4": h4, "clpp": c.get("clpp"), "beta_ratio_sign_average": c.get("betaRatioSignAverage"),
                  "qtl_type": c.get("rightStudyType"), "release": release},
            context=_context(biosample, v) if biosample else None, about_genes=[target], about_traits=traits,
            about_variants=list(about), independence_group=group))
    return out


@register_tool(CREDIBLE_SETS_L2G)
def credible_sets_l2g(params: dict, ctx: ToolContext) -> AdapterResult:
    if ctx.http is None:
        return _no_http(ctx.spec.name)
    v = ctx.case.variant
    vid = f"{v.chrom}_{v.pos}_{v.ref}_{v.alt}"
    rec = _Recorder(ctx.http)
    rows, count, release, failure = _ot_sets_v9(rec, vid)
    legacy = failure is not None and http9.is_cache_miss(failure)
    if legacy:
        rows, count = _ot_sets_legacy(rec, ctx)
        release = "release not recorded"
        if not rows and rec.failure() is not None and all(not r.ok for _, _, r in rec.results):
            return _failed(rec, "Open Targets", failure)
    elif failure is not None:
        return _failed(rec, "Open Targets", failure)
    release = release or "release not recorded"
    traits = [str(params["trait"])] if params.get("trait") else list(ctx.case.supplied_disease)
    gene = params.get("gene")
    scoped = [r for r in rows if traits and any(_trait_match(t, _set_traits(r)) for t in traits)]
    survey: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        survey[str((r.get("study") or {}).get("traitFromSource") or "trait not stated")].append(r)
    observations = [{"record": "summary", "credible_sets": count, "read": len(rows), "release": release,
                     "query": "earlier cached query (first 200 sets of every type)" if legacy else "v9 query",
                     "scope": traits}]
    for name, sets in sorted(survey.items()):
        pips = [p for p in (_pip(r, vid).get("posteriorProbability") for r in sets) if p is not None]
        l2g: dict[str, list[float]] = defaultdict(list)
        for r in sets:
            for p in (r.get("l2GPredictions") or {}).get("rows") or []:
                l2g[str((p.get("target") or {}).get("approvedSymbol"))].append(float(p["score"]))
        observations.append({"record": "trait", "trait": name, "credible_sets": len(sets),
                             "pip_range": [min(pips), max(pips)] if pips else None,
                             "methods": sorted({str(r.get("finemappingMethod")) for r in sets
                                                if r.get("finemappingMethod")}),
                             "l2g_ranges": {g: [min(s), max(s)] for g, s in sorted(l2g.items())}})
    about = _case_names(ctx)
    evidence = [e for r in scoped for e in _ot_evidence(r, vid, release, gene, v, about)]
    nested_truncation = []
    for row in scoped if traits else rows:
        for field in ("l2GPredictions", "colocalisation"):
            result = row.get(field) or {}
            read = len(result.get("rows") or [])
            if read < (result.get("count") or 0):
                nested_truncation.append({"study_locus_id": row.get("studyLocusId"), "field": field,
                                          "read": read, "count": result["count"]})
    incomplete = legacy or len(rows) < count or bool(rec.partial) or bool(nested_truncation)
    limitations = ["per credible set: never a maximum across unrelated studies"]
    if legacy:
        limitations.append("offline: an earlier cached query (first 200 credible sets of every type, no release, no "
                           "study-locus ids, no colocalisation)")
    elif len(rows) < count:
        limitations.append(f"read {len(rows)} of {count} credible sets (page cap {OT_MAX_PAGES})")
    if nested_truncation:
        limitations.append(f"{len(nested_truncation)} nested result lists truncated: first {OT_L2G_ROWS} L2G and "
                           f"{OT_COLOC_ROWS} colocalisation rows per set; a missing gene is not evidence of absence")
        observations.append({"record": "nested_coverage", "truncated": nested_truncation})
    limitations += _partial_notes(rec, "Open Targets")
    if not traits:
        limitations.append("no trait requested or disease supplied: a survey by trait, no Evidence")
    found = bool(scoped) if traits else bool(rows)
    # Unread sets may hold one in scope: "no record" only when every set was read.
    status = ("incomplete" if incomplete and (found or count or rec.partial) else
              "records_found" if found else "no_records_found")
    if not traits:
        message = f"survey of {len(rows)} credible sets by trait (no Evidence): name a trait"
    elif scoped or status != "incomplete":
        message = f"{len(scoped)} credible sets in scope of {count}"
    else:
        message = (f"no credible set in scope among the {len(rows)} of {count} read; the rest were not read, so this "
                   "is not a record of absence")
    return AdapterResult(
        retrieval_status=status, observations=observations,
        coverage=Coverage(requested_scope=f"Open Targets GWAS credible sets containing {vid}"
                          + (f" for {', '.join(traits)}" if traits else ""),
                          assessed_scope=f"{len(rows)} of {count} credible sets read; {len(scoped)} in scope",
                          limitations=limitations),
        evidence=evidence, raw={"requests": rec.records(), "credible_sets": rows, "release": release},
        dataset_release=release, message=message, cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- civic_lookup ---------------------------------------------------------------------------------------------------

CIVIC_BROWSE = ("query V2MCivicBrowse($gene: String!) { browseVariants(featureName: $gene, first: 100) "
                "{ nodes { id name featureName aliases { name } evidenceItemCount } } }")
CIVIC_VARIANT = ("query V2MCivicVariant($id: Int!) { variant(id: $id) { id name ... on GeneVariant { "
                 "alleleRegistryId hgvsDescriptions coordinates { referenceBuild chromosome start stop referenceBases "
                 "variantBases } singleVariantMolecularProfile { id name evidenceItems(first: %d) { totalCount nodes "
                 "{ id status evidenceType evidenceLevel evidenceDirection significance variantOrigin evidenceRating "
                 "disease { name doid } source { citationId sourceType } } } } } } }" % CIVIC_EVIDENCE_ROWS)

CIVIC_LOOKUP = ToolSpec(
    name="civic_lookup", route="computational",
    description=("CIViC clinical evidence by gene and variant name (e.g. BRAF, V600E). Without a variant name it lists "
                 "the gene's CIViC variants and creates no Evidence."),
    params={"genes": ParamSpec(type="list[str]", normalise="upper", description="gene symbols to search"),
            "variant": ParamSpec(description="a CIViC variant name or alias, such as V600E")},
    assemblies=[], provider="CIViC GraphQL", dataset_release="CIViC (live; the API reports no release)",
    coverage_notes=("Clinical lookup is by gene and variant name. Bounded SNV identity checks compare declared-build "
                    "coordinates only against verified case placements; never guess a shorthand's coordinate. "
                    "Clinical assertions do not replace a mechanism."),
    result_semantics=("records_found: Evidence (clinical_assertion) per evidence item of the named variant, with its "
                      "review status. no_records_found: no CIViC variant of that name."),
    rate_policy="serial", evidence_classes=["clinical_assertion"], network=True, tool_version="3")


@register_tool(CIVIC_LOOKUP)
def civic_lookup(params: dict, ctx: ToolContext) -> AdapterResult:
    genes, name = list(params.get("genes") or []), params.get("variant")
    if not genes:
        return AdapterResult(execution_status="not_applicable",
                             message="civic_lookup: no gene to search (CIViC is searched by gene and variant name)")
    if ctx.http is None:
        return _no_http(ctx.spec.name)
    rec = _Recorder(ctx.http)
    listed, evidence, observations = [], [], []
    for gene in genes:
        r = rec.query(CIVIC, {"query": CIVIC_BROWSE, "variables": {"gene": gene}})
        if not r.ok:
            return _failed(rec, "CIViC", r)
        nodes = (((r.data or {}).get("data") or {}).get("browseVariants") or {}).get("nodes") or []
        listed += [{"record": "civic_variant", "gene": gene, "id": n.get("id"), "name": n.get("name"),
                    "aliases": [a.get("name", "") if isinstance(a, dict) else str(a)
                                for a in n.get("aliases") or []], "evidence_items": n.get("evidenceItemCount")}
                   for n in sorted(nodes, key=lambda n: (str(n.get("name")), n.get("id") or 0))]
    if name is None:
        # Resolve a bounded set of catalogue SNV names against verified primary-assembly placements. Never infer
        # a coordinate from a shorthand's numeric suffix. This returns identity metadata, not clinical evidence.
        from .variant_identity import catalogue_identity, mappings
        identities = []
        candidates = [x for x in listed if re.fullmatch(r"[ACGT]\d+[ACGT]", str(x["name"]), re.I)]
        if mappings(ctx.graph):
            for hit in candidates[:6]:
                detail = rec.query(CIVIC, {"query": CIVIC_VARIANT, "variables": {"id": int(hit["id"])}})
                if detail.ok and not (detail.data or {}).get("errors"):
                    var = ((detail.data or {}).get("data") or {}).get("variant") or {}
                    identities.append(catalogue_identity(hit, var, ctx.graph))
        return AdapterResult(
            retrieval_status=_graphql_status(rec, bool(listed)), observations=[*identities, *listed],
            coverage=Coverage(requested_scope=f"CIViC variants of {', '.join(genes)}",
                              assessed_scope=f"{len(listed)} variants listed",
                              limitations=["name a variant to get clinical evidence; identity checks require an "
                                           "exact verified placement in the catalogue's stated build",
                                           f"identity detail cap: checked {len(identities)} of {len(candidates)} SNV names",
                                           *_partial_notes(rec, "CIViC")]),
            raw={"requests": rec.records()}, message=f"{len(listed)} CIViC variants listed (no Evidence)",
            cached=rec.cached, retrieval_time=rec.retrieval_time())
    wanted = str(name).casefold()
    hits = [x for x in listed if wanted in {str(x["name"]).casefold(), *(str(a).casefold() for a in x["aliases"])}]
    for hit in hits:
        r = rec.query(CIVIC, {"query": CIVIC_VARIANT, "variables": {"id": int(hit["id"])}})
        if not r.ok:
            return _failed(rec, "CIViC", r)
        var = ((r.data or {}).get("data") or {}).get("variant") or {}
        from .variant_identity import catalogue_identity
        observations.append(catalogue_identity(hit, var, ctx.graph))
        profile = var.get("singleVariantMolecularProfile") or {}
        items = (profile.get("evidenceItems") or {}).get("nodes") or []
        observations.append({"record": "civic_variant", **hit, "allele_registry_id": var.get("alleleRegistryId"),
                             "coordinates": var.get("coordinates"), "hgvs": var.get("hgvsDescriptions") or [],
                             "evidence_total": (profile.get("evidenceItems") or {}).get("totalCount")})
        # The assertions' variant as CIViC names it: gene and name, plus any rsID among its aliases. Its coordinates
        # and HGVS are GRCh37, so they are never written as a chrom:pos, which the graph reads as GRCh38.
        about = [f"{hit['gene']} {hit['name']}",
                 *sorted({str(a).strip().lower() for a in hit["aliases"] if RSID.fullmatch(str(a).strip())})]
        for e in sorted(items, key=lambda e: e.get("id") or 0):
            disease = e.get("disease") or {}
            source = e.get("source") or {}
            cite = (f"PMID:{source['citationId']}" if source.get("sourceType") == "PUBMED" and source.get("citationId")
                    else f"{source.get('sourceType')}:{source.get('citationId')}")
            observations.append({"record": "civic_evidence", "variant": hit["name"], "gene": hit["gene"], **{
                k: e.get(k) for k in ("id", "status", "evidenceType", "evidenceLevel", "evidenceDirection",
                                      "significance", "variantOrigin", "evidenceRating")},
                "disease": disease.get("name"), "doid": disease.get("doid"), "source": cite})
            evidence.append(_evidence(
                evidence_class="clinical_assertion", source_ids=[f"CIViC:EID{e.get('id')}", cite],
                observed_result=(f"CIViC evidence item EID{e.get('id')} ({e.get('status')}) on {hit['gene']} "
                                 f"{hit['name']}: {e.get('evidenceType')} evidence, level {e.get('evidenceLevel')}, "
                                 f"{e.get('evidenceDirection')} {e.get('significance')} in {disease.get('name')} "
                                 f"({e.get('variantOrigin')}; {cite})."),
                data={k: e.get(k) for k in ("status", "evidenceType", "evidenceLevel", "evidenceDirection",
                                            "significance", "variantOrigin", "evidenceRating")},
                about_genes=[hit["gene"]], about_traits=[x for x in (disease.get("name"),
                                                                     f"DOID:{disease['doid']}" if disease.get("doid")
                                                                     else None) if x],
                about_variants=list(about), independence_group=f"CIVIC-SOURCE:{cite}",
                limitations=["matched by gene and variant name, not by GRCh38 position",
                             *(["submitted, not yet accepted by CIViC editors"] if e.get("status") != "ACCEPTED"
                               else [])]))
    status = _graphql_status(rec, bool(evidence))
    return AdapterResult(
        retrieval_status=status, observations=observations or listed,
        coverage=Coverage(requested_scope=f"CIViC evidence for {', '.join(genes)} {name}",
                          assessed_scope=f"{len(hits)} matching variant(s), {len(evidence)} evidence items",
                          limitations=["CIViC is GRCh37 and transcript-named: the match is by name only",
                                       *_partial_notes(rec, "CIViC")]),
        evidence=evidence, raw={"requests": rec.records()},
        message=f"{len(evidence)} CIViC evidence items for {name}" if evidence else
        f"no CIViC variant named {name} for {', '.join(genes)}" + (" (no record)" if status == "no_records_found"
                                                                   else " in an answer that reported errors"),
        cached=rec.cached, retrieval_time=rec.retrieval_time())


# --- screen_online --------------------------------------------------------------------------------------------------

SCREEN_QUERY = ("query V2MScreen($chrom: String!, $start: Int!, $end: Int!) { getmaxZScoresQuery(assembly: \"grch38\", "
                "coordinates: [{chromosome: $chrom, start: $start, end: $end}]) { accession chromosome start stop "
                "ccre_group atac_max_zscore ctcf_max_zscore dnase_max_zscore h3k27ac_max_zscore h3k4me3_max_zscore } }")

SCREEN_ONLINE = ToolSpec(
    name="screen_online", route="computational",
    description=("The documented, authenticated SCREEN API: the cCRE containing the variant and its maximum signal "
                 "z-scores across biosamples. Needs the user's key; the local snapshot (ccre_overlap) is the default."),
    variant_types=["SNV"], provider="SCREEN GraphQL API (screen.api.wenglab.org)",
    dataset_release="SCREEN API (live; release not reported)",
    coverage_notes=("Enabled only when the key's environment variable is set (V2M_SCREEN_API_KEY by default); the key "
                    "travels in a header and is never logged or cached. The coordinate convention is not yet checked "
                    "against a live key. Biosample-specific z-scores are not requested."),
    result_semantics=("records_found: the containing cCRE (annotation, the local path's schema and independence "
                      "group) with maximum z-scores in data. unavailable: no key, or SCREEN refused it."),
    rate_policy="serial", evidence_classes=["annotation"], network=True)


@register_tool(SCREEN_ONLINE)
def screen_online(params: dict, ctx: ToolContext) -> AdapterResult:
    cfg = _config(ctx)
    env = str((cfg.get("v9") or {}).get("screen_api_key_env") or SCREEN_KEY_ENV)
    key = os.environ.get(env)
    if not key:
        return AdapterResult(execution_status="unavailable",
                             message=(f"screen_online needs a SCREEN API key in {env}, which is not set; the local "
                                      "SCREEN snapshot (ccre_overlap) is the contract"))
    if ctx.http is None:
        return _no_http(ctx.spec.name)
    v = ctx.case.variant
    rec = _Recorder(ctx.http)
    r = rec.query(SCREEN_API, {"query": SCREEN_QUERY, "variables": {"chrom": f"chr{v.chrom}", "start": v.pos - 1,
                                                                    "end": v.pos}},
                  headers={"Authorization": f"Bearer {key}"})
    if not r.ok:
        return _failed(rec, "SCREEN API", r)
    found = ((r.data or {}).get("data") or {}).get("getmaxZScoresQuery") or []
    rows = [x for x in found if int(x["start"]) < v.pos <= int(x["stop"])]
    observations = [{"record": "element", "accession": x["accession"], "class": x.get("ccre_group"),
                     "chrom": x["chromosome"], "start": int(x["start"]) + 1, "end": int(x["stop"]),
                     **{k: x.get(k) for k in x if k.endswith("_max_zscore")}} for x in rows]
    evidence = [_evidence(
        evidence_class="annotation", source_ids=[o["accession"], "SCREEN-API"],
        observed_result=(f"SCREEN API: {_where(v)} lies in cCRE {o['accession']} ({o['class']}), "
                         f"{o['chrom']}:{o['start']}-{o['end']}."),
        data={k: o[k] for k in o if k != "record"}, about_elements=[o["accession"]],
        about_variants=_case_names(ctx), independence_group=f"ENCODE-cCRE:{o['accession']}",
        limitations=["maximum z-scores across biosamples, not biosample-specific activity",
                     "coordinate convention assumed BED-like (0-based start); not yet checked with a live key"])
        for o in observations]
    return AdapterResult(
        retrieval_status=_graphql_status(rec, bool(rows)), observations=observations,
        coverage=Coverage(requested_scope=f"SCREEN cCREs containing {_where(v)}", assessed_scope=f"{len(rows)} cCREs",
                          limitations=_partial_notes(rec, "SCREEN")),
        evidence=evidence, raw={"requests": rec.records(), "elements": found},
        message=f"SCREEN API: {len(rows)} cCRE(s) contain the variant", cached=rec.cached,
        retrieval_time=rec.retrieval_time())


# --- code's fact collection (SPEC 6 step 2) and the inventory view (contract C2) -----------------------------------

def _consequence_genes(call: ToolCall) -> list[str]:
    """Genes with a VEP consequence, from a successful variant_annotation call (what CIViC is searched by)."""
    if call.execution_status != "success":
        return []
    return sorted({str(o["gene"]) for o in call.observations if o.get("record") == "consequence" and o.get("gene")})


def _observed(call: ToolCall, record: str, key: str) -> list[str]:
    """One field of a call's observation records of one kind (a list field flattened), from a successful call that
    found records; nothing from an empty, failed or refused call."""
    if call.execution_status != "success" or call.retrieval_status not in ("records_found", "incomplete"):
        return []
    values: list[str] = []
    for o in call.observations:
        if o.get("record") == record and o.get(key):
            values += [str(x) for x in o[key]] if isinstance(o[key], list) else [str(o[key])]
    return values


def _record_case_fact(add: Any, value: str, call: ToolCall, notes: dict[str, list[str]], kind: str) -> None:
    """Record one fact about the case variant through a graph method (add_variant_alias, add_variant_element). A
    refusal, such as dbSNP's rsID differing from a supplied one, is kept for the collect_facts event, never raised:
    the facts stand either way, and the request is never changed."""
    try:
        if add(value, call.tool_call_id):
            notes[kind].append(value)
    except GraphRefusal as e:
        notes["refused"].append(f"{value}: {e.reason}")


def collect_facts(case: Case, graph: ClaimGraph, runner: ToolRunner) -> list[ToolCall]:
    """SPEC 6 step 2, run as role "code" (charged to code's own counter): variant_annotation, ccre_overlap,
    qbic_inventory, then gtex_eqtl for a germline or unknown origin, or civic_lookup (by the genes VEP names) for a
    somatic one. Every step runs whatever the others returned: a failure is a recorded call, never a stop, and
    missingness is never a prerequisite.

    What the calls establish about the case variant is recorded in the graph, because a clean request may give
    coordinates only: each rsID dbSNP gives the exact position and alleles (variant_annotation's exact_rsids, never a
    co-located rsID of another allele) becomes the case variant's own (graph.add_variant_alias), so claims, papers
    and the GWAS Catalog naming it are about this variant; the cCRE containing the variant (ccre_overlap) is recorded
    with graph.add_variant_element, so evidence naming "the enhancer containing <rsID>" is about that element.
    case.variant is never changed. Logs one collect_facts event naming the calls and what was recorded or refused.
    Never raises."""
    notes: dict[str, list[str]] = {"aliases": [], "elements": [], "refused": []}
    annotation = runner.run(ToolRequest(tool="variant_annotation", purpose="consequences, reference check, nearby "
                                        "genes"), case, graph, "code")
    for rsid in _observed(annotation, "variant", "exact_rsids"):
        _record_case_fact(graph.add_variant_alias, rsid, annotation, notes, "aliases")
    overlap = runner.run(ToolRequest(tool="ccre_overlap", purpose="the regulatory element at the variant"), case,
                         graph, "code")
    for accession in _observed(overlap, "element", "accession"):
        _record_case_fact(graph.add_variant_element, accession, overlap, notes, "elements")
    inventory = runner.run(ToolRequest(tool="qbic_inventory", purpose="every model-sharing group's predicted allelic "
                                       "binding"), case, graph, "code")
    if case.origin == "somatic":
        genes = _consequence_genes(annotation)
        last = ToolRequest(tool="civic_lookup", params={"genes": genes} if genes else {},
                           purpose="clinical evidence for the genes VEP names")
    else:
        last = ToolRequest(tool="gtex_eqtl", purpose="allele-expression associations (GTEx v8)")
    calls = [annotation, overlap, inventory, runner.run(last, case, graph, "code")]
    summary = "; ".join(f"{c.tool_call_id} {c.tool_name}: {c.execution_status}/{c.retrieval_status}" for c in calls)
    recorded = "; ".join(f"{kind}: {', '.join(values)}" for kind, values in notes.items() if values)
    graph.log("collect_facts", "code", f"fact collection: {summary}" + (f" ({recorded})" if recorded else ""),
              target_ids=[c.tool_call_id for c in calls], evidence_ids=[e for c in calls for e in c.evidence_ids],
              details=notes)
    return calls


def inventory_rows(graph: ClaimGraph) -> list[dict[str, Any]]:
    """The latest successful qbic_inventory call's rows (contract C2), each with evidence_id: the E id of that
    group's Evidence (joined on data.group_id), None for a group with no model past the gate. A group whose
    gate-passing models disagree about the allele has one item per allele (data.discordant); the row describes its
    best model, so it joins the item for the allele the row names (binds_more). Neutral order kept."""
    calls = [t for t in graph.tool_calls.values() if t.tool_name == "qbic_inventory"
             and t.execution_status == "success"]
    if not calls:
        return []
    call = max(calls, key=lambda t: int(t.tool_call_id[1:]))
    items: dict[str, list[Evidence]] = defaultdict(list)
    for e in call.evidence_ids:
        if e in graph.evidence:
            items[str(graph.evidence[e].data.get("group_id"))].append(graph.evidence[e])
    v = graph.case.variant

    def joined(row: dict[str, Any]) -> str | None:
        group = items.get(str(row["group_id"])) or []
        allele = _allele_base(v, row["binds_more"])
        return next((e.evidence_id for e in group if e.allele == allele), group[0].evidence_id if group else None)

    return [{**row, "evidence_id": joined(row)} for row in call.observations]
