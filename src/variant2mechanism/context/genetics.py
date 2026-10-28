"""Germline genetics: GWAS Catalog (`gwas_lookup`), Open Targets fine-mapping (`finemap_lookup`), GTEx eQTLs
(`eqtl_lookup`) and Open Targets gene-disease evidence (`gene_disease`)."""

from .base import Case, ToolResult, failed, fmt_p

GWAS = "https://www.ebi.ac.uk/gwas/rest/api/v2/associations"
OT = "https://api.platform.opentargets.org/api/v4/graphql"
GTEX_API = "https://gtexportal.org/api/v2"
GTEX = f"{GTEX_API}/association/singleTissueEqtl"
GTEX_VARIANT = f"{GTEX_API}/dataset/variant"           # is the variant in GTEx, and common enough to be tested?
GTEX_TISSUES = f"{GTEX_API}/dataset/tissueSiteDetail"


def gwas_lookup(case: Case) -> ToolResult:
    args = {"rsid": case.rsid}
    if not case.rsid:
        return failed("gwas_lookup", args, "GWAS Catalog", "genetic", message="no rsID for this variant")
    url = f"{GWAS}?rs_id={case.rsid}&size=100"
    r = case.http.get(url, timeout=120)       # this endpoint has taken up to a minute
    if not r.ok:
        return failed("gwas_lookup", args, "GWAS Catalog v2", "genetic", r)
    assoc = (r.data.get("_embedded") or {}).get("associations", [])
    assoc.sort(key=lambda a: a.get("p_value") or 1)
    if not assoc:
        return ToolResult("gwas_lookup", args, f"0 GWAS Catalog associations for {case.rsid}. The Catalog lists "
                          "reported associations only, often just the lead variant of each signal, so this is weak "
                          "evidence against an association.", [], "GWAS Catalog REST v2", url, "genetic",
                          retrieved_utc=r.retrieved_utc, status="tested_negative")
    lines = [f"{len(assoc)} GWAS Catalog associations for {case.rsid}, strongest first:"]
    seen = set()
    for a in assoc:
        trait = (a.get("reported_trait") or ["?"])[0]
        if trait in seen:
            continue
        seen.add(trait)
        eff = ", ".join(x.get("effect_allele", "?") for x in a.get("snp_allele", []))
        lines.append(f"{trait}: p {fmt_p(a.get('p_value'))}, effect allele {eff or '?'}, "
                     f"risk-allele frequency {a.get('risk_frequency') or '?'}, PMID {a.get('pubmed_id')}")
        if len(seen) >= 12:
            break
    full = [{k: a.get(k) for k in ("reported_trait", "p_value", "snp_allele", "risk_frequency", "pubmed_id",
                                   "accession_id", "mapped_genes", "beta")} for a in assoc]
    return ToolResult("gwas_lookup", args, "\n".join(lines), full, "GWAS Catalog REST v2", url, "genetic",
                      retrieved_utc=r.retrieved_utc)


def finemap_lookup(case: Case) -> ToolResult:
    vid = case.opentargets
    args = {"variant": vid}
    q = ('query { variant(variantId: "%s") { credibleSets(page:{index:0,size:200}) { count rows { '
         'study { id studyType traitFromSource target { approvedSymbol } } '
         'locus(variantIds:["%s"]) { rows { posteriorProbability } } '
         'l2GPredictions(page:{index:0,size:3}) { rows { target { approvedSymbol } score } } } } } }' % (vid, vid))
    r = case.http.graphql(OT, q)
    if not r.ok:
        return failed("finemap_lookup", args, "Open Targets", "genetic", r)
    var = (r.data.get("data") or {}).get("variant")
    if not var:
        return ToolResult("finemap_lookup", args, f"Open Targets has no record of {vid}, so it says nothing about "
                          "fine-mapping here.", r.data, "Open Targets Platform", OT, "genetic",
                          retrieved_utc=r.retrieved_utc, status="not_tested")
    rows = var["credibleSets"]["rows"]

    def pip(x):
        loc = x["locus"]["rows"]
        return loc[0]["posteriorProbability"] if loc else 0.0

    gwas = sorted([x for x in rows if x["study"]["studyType"] == "gwas"], key=pip, reverse=True)
    qtl = sorted([x for x in rows if x["study"]["studyType"] != "gwas"], key=pip, reverse=True)
    lines = [f"{var['credibleSets']['count']} credible sets contain {vid}: {len(gwas)} GWAS, {len(qtl)} molecular QTL."]
    if not rows:
        lines.append("Open Targets has the variant, but no credible set contains it.")
    for x in gwas[:6]:
        l2g = ", ".join(f"{p['target']['approvedSymbol']} {p['score']:.2f}" for p in x["l2GPredictions"]["rows"])
        lines.append(f"GWAS {x['study']['traitFromSource'][:60]}: PIP {pip(x):.2f}; L2G {l2g or 'none'}")
    for x in qtl[:6]:
        gene = (x["study"].get("target") or {}).get("approvedSymbol") or x["study"]["traitFromSource"]
        lines.append(f"{x['study']['studyType']} for {gene} ({x['study']['id'][:50]}): PIP {pip(x):.2f}")
    l2g_all = {}
    for x in gwas:
        for p in x["l2GPredictions"]["rows"]:
            g = p["target"]["approvedSymbol"]
            l2g_all[g] = max(l2g_all.get(g, 0), p["score"])
    if l2g_all:
        best = sorted(l2g_all.items(), key=lambda kv: -kv[1])[:4]
        lines.append("Best L2G gene scores across these sets: " + ", ".join(f"{g} {s:.2f}" for g, s in best))
    return ToolResult("finemap_lookup", args, "\n".join(lines),
                      {"gwas": gwas, "qtl": qtl, "best_l2g": l2g_all}, "Open Targets Platform (credible sets, L2G)",
                      OT, "genetic", retrieved_utc=r.retrieved_utc, status="found" if rows else "tested_negative")


def eqtl_lookup(case: Case, tissue: str | None = None) -> ToolResult:
    url = f"{GTEX}?variantId={case.gtex}&datasetId=gtex_v8"
    args = {"variant": case.gtex, "tissue": tissue}
    r = case.http.get(url)
    if not r.ok:
        return failed("eqtl_lookup", args, "GTEx", "genetic", r)
    rows = r.data.get("data", [])
    where = ""
    if tissue:
        t = tissue.lower().replace(" - ", "_").replace(" ", "_")
        tr = case.http.get(f"{GTEX_TISSUES}?datasetId=gtex_v8&itemsPerPage=250")
        if not tr.ok:
            return failed("eqtl_lookup", args, "GTEx", "genetic", tr)
        known = [x["tissueSiteDetailId"] for x in tr.data.get("data", [])]
        matched = [k for k in known if t in k.lower()]
        if not matched:
            return failed("eqtl_lookup", args, "GTEx", "genetic",
                          message=f"no GTEx v8 tissue matches '{tissue}'; tissues include {', '.join(known[:15])}")
        rows = [x for x in rows if x["tissueSiteDetailId"] in matched]
        where = f" in {', '.join(matched)}"
    rows.sort(key=lambda x: x["pValue"])
    if rows:
        status = "found"
        lines = [f"{len(rows)} significant GTEx v8 single-tissue eQTLs for {case.gtex}{where}. NES is the effect of the "
                 f"alt allele ({case.variant.alt}) relative to ref ({case.variant.ref})."]
        lines += [f"{x['geneSymbol']} in {x['tissueSiteDetailId']}: NES {x['nes']:+.2f}, p {fmt_p(x['pValue'])}"
                  for x in rows[:15]]
    else:                                   # no eQTL listed: was the variant tested at all?
        vr = case.http.get(f"{GTEX_VARIANT}?variantId={case.gtex}&datasetId=gtex_v8")
        if not vr.ok:
            return failed("eqtl_lookup", args, "GTEx", "genetic", vr)
        info = (vr.data.get("data") or [None])[0]
        if info is None:
            status, text = "not_tested", f"GTEx v8 has no genotype for {case.gtex}, so it says nothing about eQTLs here."
        elif not info.get("maf01"):
            status, text = "not_tested", (f"{case.gtex} is below 1% minor-allele frequency in GTEx v8, which maps eQTLs "
                                          "for common variants only, so GTEx says nothing about eQTLs here.")
        else:
            status, text = "tested_negative", (f"GTEx v8 tested {case.gtex}: no significant single-tissue eQTL"
                                               f"{where or ' in any tissue'}.")
        lines = [text]
    return ToolResult("eqtl_lookup", args, "\n".join(lines), rows, "GTEx Portal API v2 (gtex_v8)", url, "genetic",
                      retrieved_utc=r.retrieved_utc, status=status)


def gene_disease(case: Case, gene: str, ensembl_id: str | None = None) -> ToolResult:
    args = {"gene": gene, "disease": case.disease}
    disease = case.disease.split("(")[0].strip()
    r0 = case.http.graphql(OT, 'query { search(queryString: "%s", entityNames: ["disease"], page:{index:0,size:1}) '
                               '{ hits { id name } } }' % disease.replace('"', ""))
    if not r0.ok:
        return failed("gene_disease", args, "Open Targets", "genetic", r0)
    hits = r0.data["data"]["search"]["hits"]
    if not hits:
        return failed("gene_disease", args, "Open Targets", "genetic", message=f"no disease matches '{disease}'")
    did, dname = hits[0]["id"], hits[0]["name"]
    if ensembl_id is None:
        from ..qbic.registry import get_registry
        ensembl_id = get_registry().ensembl_by_symbol.get(gene)
    if not ensembl_id:
        return failed("gene_disease", args, "Open Targets", "genetic", message=f"no Ensembl ID for {gene}")
    q = ('query { target(ensemblId: "%s") { approvedSymbol associatedDiseases(Bs: ["%s"]) '
         '{ rows { disease { name } score datatypeScores { id score } } } } }' % (ensembl_id, did))
    r = case.http.graphql(OT, q)
    if not r.ok:
        return failed("gene_disease", args, "Open Targets", "genetic", r)
    rows = r.data["data"]["target"]["associatedDiseases"]["rows"]
    if not rows:
        summary = (f"Open Targets: no association between {gene} and {dname} ({did}); no evidence there links "
                   "them.")
    else:
        x = rows[0]
        kinds = ", ".join(f"{d['id']} {d['score']:.2f}" for d in sorted(x["datatypeScores"], key=lambda d: -d["score"]))
        summary = (f"Open Targets: {gene} and {x['disease']['name']} ({did}), overall score {x['score']:.2f}; "
                   f"by evidence type: {kinds}")
    return ToolResult("gene_disease", args, summary, {"disease_id": did, "rows": rows}, "Open Targets Platform", OT,
                      "genetic", retrieved_utc=r.retrieved_utc, status="found" if rows else "tested_negative")
