"""Ensembl: rsID to GRCh38, VEP with GERP (`variant_annotation`), nearby genes (`nearest_genes`)."""

from ..qbic.variants import Variant, VariantError
from .base import Case, ToolResult, failed

REST = "https://rest.ensembl.org"


def resolve_rsid(http, rsid: str, alt: str | None = None) -> Variant:
    """rsID to a GRCh38 plus-strand SNV; more than one alternate allele needs `alt`."""
    r = http.get(f"{REST}/variation/human/{rsid}?content-type=application/json")
    if not r.ok:
        raise VariantError(f"Ensembl could not resolve {rsid}: {r.error}")
    maps = [m for m in r.data.get("mappings", []) if m.get("assembly_name") == "GRCh38"
            and len(m.get("seq_region_name", "")) <= 2]
    if not maps:
        raise VariantError(f"{rsid} has no GRCh38 chromosome mapping in Ensembl.")
    m = maps[0]
    alleles = m["allele_string"].split("/")
    if m.get("strand", 1) != 1:
        raise VariantError(f"{rsid} maps to the minus strand in Ensembl; give chr:pos:ref>alt on the plus strand.")
    ref, alts = alleles[0], alleles[1:]
    if alt is None:
        if len(alts) != 1:
            raise VariantError(f"{rsid} has alternate alleles {', '.join(alts)}; choose one with --alt.")
        alt = alts[0]
    elif alt not in alts:
        raise VariantError(f"{alt} is not an alternate allele of {rsid} ({', '.join(alts)}).")
    return Variant.make(m["seq_region_name"], m["start"], ref, alt)


def variant_annotation(case: Case) -> ToolResult:
    v = case.variant
    url = f"{REST}/vep/human/region/{case.ensembl}-{v.pos}:1/{v.alt}?content-type=application/json&Conservation=1"
    args = {"variant": v.key()}
    r = case.http.get(url)
    if not r.ok:
        return failed("variant_annotation", args, "Ensembl VEP", "computational", r)
    d = r.data[0]
    rsids = [c["id"] for c in d.get("colocated_variants", []) if str(c.get("id", "")).startswith("rs")]
    regs = d.get("regulatory_feature_consequences") or []
    gerp = next((x.get("conservation") for x in regs + d.get("transcript_consequences", [])
                 if x.get("conservation") is not None), None)
    genes = []
    for t in d.get("transcript_consequences", []):
        label = f"{t.get('gene_symbol')} ({', '.join(t.get('consequence_terms', []))})"
        if t.get("gene_symbol") and label not in genes:
            genes.append(label)
    ref_vep = d.get("allele_string", "").split("/")[0]
    lines = [f"Variant {v.key()} (GRCh38), allele string {d.get('allele_string')}"
             + ("" if ref_vep == v.ref else f"; WARNING: Ensembl reference is {ref_vep}, input ref is {v.ref}"),
             f"Known IDs: {', '.join(rsids) or 'none'}",
             f"Most severe consequence: {d.get('most_severe_consequence')}",
             "Regulatory features: " + ("; ".join(f"{x.get('regulatory_feature_id')} {x.get('biotype')}" for x in regs)
                                        or "none"),
             f"GERP conservation score at the site: {gerp if gerp is not None else 'not reported'}",
             "Transcript consequences: " + ("; ".join(genes[:6]) or "none (intergenic)")]
    return ToolResult("variant_annotation", args, "\n".join(lines), r.data, "Ensembl VEP (GRCh38)", url,
                      "computational", retrieved_utc=r.retrieved_utc)


def nearest_genes(case: Case, window: int = 1_000_000) -> ToolResult:
    v = case.variant
    s, e = max(1, v.pos - window), v.pos + window
    url = (f"{REST}/overlap/region/human/{v.chrom_bare}:{s}-{e}"
           "?feature=gene;biotype=protein_coding;content-type=application/json")
    args = {"variant": v.key(), "window_bp": window}
    r = case.http.get(url)
    if not r.ok:
        return failed("nearest_genes", args, "Ensembl overlap", "computational", r)
    genes = []
    for g in r.data:
        tss = g["start"] if g["strand"] == 1 else g["end"]
        upstream = (v.pos < tss) if g["strand"] == 1 else (v.pos > tss)
        inside = g["start"] <= v.pos <= g["end"]
        genes.append({"gene": g.get("external_name") or g["id"], "ensembl": g["id"], "strand": g["strand"],
                      "tss": tss, "distance_to_tss": abs(v.pos - tss),
                      "position": "in gene body" if inside else ("upstream" if upstream else "downstream")})
    genes.sort(key=lambda x: x["distance_to_tss"])
    lines = [f"{len(genes)} protein-coding genes within {window // 1000} kb of {v.key()}, by distance to TSS:"]
    lines += [f"{g['gene']}: {g['distance_to_tss'] / 1000:.1f} kb from TSS ({g['position']}, strand {g['strand']:+d})"
              for g in genes[:10]]
    return ToolResult("nearest_genes", args, "\n".join(lines), genes, "Ensembl overlap (protein_coding)", url,
                      "computational", retrieved_utc=r.retrieved_utc)
