"""Smoke test for every external API the demo's tools call.

Each check makes one real request with a known variant (rs6983267, GRCh38 chr8:127401060 G>T),
records HTTP status, latency and a one-line summary of what came back. Nothing is downloaded
beyond the API responses themselves. Run: uv run python scripts/check_apis.py [out.json]
"""
import json
import sys
import time

import requests

UA = {"User-Agent": "variant2mechanism-apicheck/0.1"}
VAR = {"chrom": "8", "pos": 127401060, "ref": "G", "alt": "T", "rsid": "rs6983267"}
OT = "https://api.platform.opentargets.org/api/v4/graphql"


def call(method, url, **kw):
    t0 = time.time()
    r = requests.request(method, url, headers={**UA, **kw.pop("headers", {})}, timeout=60, **kw)
    return r, round(time.time() - t0, 2)


def gql(url, query):
    return call("POST", url, json={"query": query}, headers={"Content-Type": "application/json"})


def ensembl_variation():
    r, t = call("GET", f"https://rest.ensembl.org/variation/human/{VAR['rsid']}?content-type=application/json")
    m = [x for x in r.json()["mappings"] if x["assembly_name"] == "GRCh38"][0]
    return r.status_code, t, f"{m['seq_region_name']}:{m['start']} {m['allele_string']}"


def ensembl_vep():
    url = (f"https://rest.ensembl.org/vep/human/region/{VAR['chrom']}:{VAR['pos']}-{VAR['pos']}:1/{VAR['alt']}"
           "?content-type=application/json&Conservation=1")
    r, t = call("GET", url)
    d = r.json()[0]
    reg = d.get("regulatory_feature_consequences") or [{}]
    return r.status_code, t, f"{d['most_severe_consequence']}; regulatory {reg[0].get('biotype')}; GERP {reg[0].get('conservation')}"


def ensembl_genes():
    s, e = VAR["pos"] - 1_000_000, VAR["pos"] + 1_000_000
    url = (f"https://rest.ensembl.org/overlap/region/human/{VAR['chrom']}:{s}-{e}"
           "?feature=gene;biotype=protein_coding;content-type=application/json")
    r, t = call("GET", url)
    g = r.json()
    near = sorted(g, key=lambda x: abs((x["start"] if x["strand"] == 1 else x["end"]) - VAR["pos"]))[:2]
    names = ", ".join(f"{x.get('external_name')} {abs((x['start'] if x['strand'] == 1 else x['end']) - VAR['pos']) // 1000} kb" for x in near)
    return r.status_code, t, f"{len(g)} protein-coding genes within 1 Mb; nearest TSS {names}"


def ensembl_sequence():
    url = f"https://rest.ensembl.org/sequence/region/human/{VAR['chrom']}:{VAR['pos']-10}..{VAR['pos']+10}:1?content-type=application/json"
    r, t = call("GET", url)
    s = r.json()["seq"]
    return r.status_code, t, f"21 bp context, centre base {s[10]}"


def screen_ccre():
    body = {"assembly": "GRCh38", "coord_chrom": f"chr{VAR['chrom']}", "coord_start": VAR["pos"] - 500, "coord_end": VAR["pos"] + 500}
    r, t = call("POST", "https://screen-beta-api.wenglab.org/dataws/cre_table", json=body)
    c = r.json()["cres"]
    top = ", ".join(f"{x['pct']} DNase z {x['dnase_zscore']:.1f}" for x in c[:2])
    return r.status_code, t, f"{len(c)} cCREs within 500 bp; {top}"


def factorbook_chip():
    q = ("{ peaksrange(assembly: \"GRCh38\", target: \"TCF7L2\", range: [{chrom: \"chr8\", chrom_start: %d, chrom_end: %d}], limit: 200) { data } }"
         % (VAR["pos"] - 100, VAR["pos"] + 100))
    r, t = gql("https://factorbook.api.wenglab.org/graphql", q)
    rows = r.json()["data"]["peaksrange"]["data"]
    bios = sorted({x["biosample"] for x in rows})
    return r.status_code, t, f"{len(rows)} TCF7L2 peaks over the SNP, in {', '.join(bios)}"


def gwas_v2():
    r, t = call("GET", f"https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id={VAR['rsid']}&size=100")
    a = r.json()["_embedded"]["associations"]
    traits = sorted({x["reported_trait"][0] for x in a})[:3]
    return r.status_code, t, f"{len(a)} associations, e.g. {'; '.join(traits)}"


def ot_variant():
    vid = f"{VAR['chrom']}_{VAR['pos']}_{VAR['ref']}_{VAR['alt']}"
    q = ('query { variant(variantId: "%s") { credibleSets(page:{index:0,size:200}) { count rows { study { studyType traitFromSource } '
         'locus(variantIds:["%s"]) { rows { posteriorProbability } } l2GPredictions(page:{index:0,size:1}) { rows { target { approvedSymbol } score } } } } } }' % (vid, vid))
    r, t = gql(OT, q)
    cs = r.json()["data"]["variant"]["credibleSets"]
    best = max(cs["rows"], key=lambda x: x["locus"]["rows"][0]["posteriorProbability"] if x["locus"]["rows"] else 0)
    l2g = best["l2GPredictions"]["rows"][0] if best["l2GPredictions"]["rows"] else {}
    return r.status_code, t, (f"{cs['count']} credible sets; best PIP {best['locus']['rows'][0]['posteriorProbability']:.2f} "
                              f"({best['study']['traitFromSource'][:30]}); L2G {l2g.get('target', {}).get('approvedSymbol')} {l2g.get('score', 0):.2f}")


def ot_gene_disease():
    r0, t0 = gql(OT, 'query { search(queryString: "colorectal cancer", entityNames: ["disease"], page:{index:0,size:1}) { hits { id name } } }')
    did = r0.json()["data"]["search"]["hits"][0]["id"]
    q = ('query { target(ensemblId: "ENSG00000136997") { approvedSymbol associatedDiseases(Bs: ["%s"]) '
         '{ rows { disease { name } score datatypeScores { id score } } } } }' % did)
    r, t = gql(OT, q)
    row = r.json()["data"]["target"]["associatedDiseases"]["rows"][0]
    kinds = ", ".join(f"{x['id']} {x['score']:.2f}" for x in sorted(row["datatypeScores"], key=lambda x: -x["score"])[:2])
    return r.status_code, round(t + t0, 2), f"disease name to {did}; MYC and {row['disease']['name']}: score {row['score']:.2f} ({kinds})"


def gtex_expression():
    r1, t1 = call("GET", "https://gtexportal.org/api/v2/reference/gene?geneId=TCF7L2&gencodeVersion=v26&genomeBuild=GRCh38%2Fhg38")
    gid = r1.json()["data"][0]["gencodeId"]
    r, t = call("GET", f"https://gtexportal.org/api/v2/expression/medianGeneExpression?gencodeId={gid}&datasetId=gtex_v8&itemsPerPage=100")
    rows = {x["tissueSiteDetailId"]: x["median"] for x in r.json()["data"]}
    return r.status_code, round(t + t1, 2), f"TCF7L2 median TPM in 54 tissues; colon transverse {rows.get('Colon_Transverse', 0):.1f}"


def gtex_eqtl():
    vid = f"chr{VAR['chrom']}_{VAR['pos']}_{VAR['ref']}_{VAR['alt']}_b38"
    r, t = call("GET", f"https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId={vid}&datasetId=gtex_v8")
    rows = r.json().get("data", [])
    genes = sorted({x["geneSymbol"] for x in rows})
    return r.status_code, t, f"{len(rows)} significant eQTLs ({', '.join(genes) or 'none'})"


def gnomad():
    q = ('{ variant(variantId: "%s-%d-%s-%s", dataset: gnomad_r4) { rsids genome { ac an } } }'
         % (VAR["chrom"], VAR["pos"], VAR["ref"], VAR["alt"]))
    r, t = gql("https://gnomad.broadinstitute.org/api", q)
    g = r.json()["data"]["variant"]["genome"]
    return r.status_code, t, f"genome allele frequency {g['ac'] / g['an']:.2f} (gnomAD v4)"


def europepmc():
    url = ("https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20AND%20TCF7L2"
           "&format=json&pageSize=5&resultType=core")
    r, t = call("GET", url)
    d = r.json()
    has_abs = sum(1 for x in d["resultList"]["result"] if x.get("abstractText"))
    return r.status_code, t, f"{d['hitCount']} hits; {has_abs} of first 5 with abstracts"


def hpa():
    r, t = call("GET", "https://www.proteinatlas.org/ENSG00000148737.json")
    d = r.json()
    keys = [k for k in d if "cell line" in k.lower()][:2]
    return r.status_code, t, f"gene record with {len(d)} fields, e.g. {'; '.join(keys)}"


CHECKS = [
    ("Ensembl variation", "variant_annotation", ensembl_variation),
    ("Ensembl VEP + GERP", "variant_annotation", ensembl_vep),
    ("Ensembl overlap (genes)", "nearest_genes", ensembl_genes),
    ("Ensembl sequence", "qbic_screen input", ensembl_sequence),
    ("SCREEN cCRE table", "ccre_lookup", screen_ccre),
    ("Factorbook ChIP peaks", "chip_peaks", factorbook_chip),
    ("GWAS Catalog v2", "gwas_lookup", gwas_v2),
    ("Open Targets variant", "finemap_lookup", ot_variant),
    ("Open Targets associations", "gene_disease", ot_gene_disease),
    ("GTEx median expression", "tf_expression", gtex_expression),
    ("GTEx eQTL", "eqtl_lookup", gtex_eqtl),
    ("gnomAD", "variant_annotation (optional)", gnomad),
    ("Europe PMC", "literature_search", europepmc),
    ("Human Protein Atlas", "tf_expression (optional)", hpa),
]

def head_size(url):
    r = requests.head(url, headers=UA, timeout=60, allow_redirects=True)
    return r.status_code, int(r.headers.get("Content-Length", 0))


def encode_size(acc):
    r = requests.get(f"https://www.encodeproject.org/files/{acc}/?format=json", headers={**UA, "Accept": "application/json"}, timeout=60)
    return r.status_code, int(r.json()["file_size"])


def zenodo_sizes(record="23482275"):
    r = requests.get(f"https://zenodo.org/api/records/{record}", headers=UA, timeout=60)
    return {f["key"]: int(f["size"]) for f in r.json()["files"]}


S3 = "https://biomni-release.s3.amazonaws.com/data_lake/"
DATASETS = [
    ("ENCODE v4 cCRE registry, GRCh38 (ENCFF420VPZ)", lambda: encode_size("ENCFF420VPZ")),
    ("DepMap expression, TPM log (Biomni copy)", lambda: head_size(S3 + "DepMap_OmicsExpressionProteinCodingGenesTPMLogp1.csv")),
    ("DepMap model metadata (Biomni copy)", lambda: head_size(S3 + "DepMap_Model.csv")),
    ("DepMap CRISPR gene effect (Biomni copy)", lambda: head_size(S3 + "DepMap_CRISPRGeneEffect.csv")),
    ("GTEx tissue TPM (Biomni copy, optional)", lambda: head_size(S3 + "gtex_tissue_gene_tpm.parquet")),
    ("Human Protein Atlas table (Biomni copy, optional)", lambda: head_size(S3 + "proteinatlas.tsv")),
    ("GENCODE v46 basic GTF (optional, offline genes)", lambda: head_size("https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_46/gencode.v46.basic.annotation.gtf.gz")),
    ("dbSNP b151 common SNPs, GRCh38 (background option)", lambda: head_size("https://ftp.ncbi.nih.gov/snp/organisms/human_9606_b151_GRCh38p7/VCF/00-common_all.vcf.gz")),
    ("Ensembl GRCh38 genome FASTA (only for local QBiC)", lambda: head_size("https://ftp.ensembl.org/pub/release-112/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz")),
]


if __name__ == "__main__":
    results = []
    for name, tool, fn in CHECKS:
        try:
            status, secs, summary = fn()
        except Exception as e:  # report and carry on
            status, secs, summary = "error", None, f"{type(e).__name__}: {str(e)[:150]}"
        results.append({"api": name, "tool": tool, "status": status, "seconds": secs, "summary": summary})
        print(f"{name:28} {str(status):6} {str(secs):6} {summary}")
    sizes = []
    for name, fn in DATASETS:
        try:
            status, n = fn()
        except Exception as e:
            status, n = f"error {type(e).__name__}", 0
        sizes.append({"dataset": name, "status": status, "bytes": n})
        print(f"{name:52} {str(status):6} {n / 1e6:10.1f} MB")
    z = zenodo_sizes()
    for key, n in sorted(z.items()):
        sizes.append({"dataset": f"QBiC-SELEX Zenodo: {key}", "status": 200, "bytes": n})
    print(f"QBiC-SELEX Zenodo record: {len(z)} files, {sum(z.values()) / 1e9:.1f} GB in total")
    if len(sys.argv) > 1:
        json.dump({"apis": results, "datasets": sizes}, open(sys.argv[1], "w"), indent=1)
