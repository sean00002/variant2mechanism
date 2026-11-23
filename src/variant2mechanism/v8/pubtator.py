"""Literature (v8): PubTator3 search, abstracts with normalised entities, and tags for the parts of a chain each paper
names. Evaluation runs pass a cut-off date (the year of the case's source paper), which the workflow applies without
ever seeing the gold set. Europe PMC is the fallback when PubTator3 fails.
"""

import re
from urllib.parse import quote

from ..context.base import ToolResult, failed
from ..context.literature import literature_search, mask_rsids
from .intake import trait_matches

SEARCH = "https://www.ncbi.nlm.nih.gov/research/pubtator3-api/search/?text={q}&page={page}"
EXPORT = "https://www.ncbi.nlm.nih.gov/research/pubtator3-api/publications/export/biocjson?pmids={ids}"
SOURCE = "PubTator3 (NCBI)"
RS = re.compile(r"RS#:(\d+)")


def _papers(docs: list[dict]) -> dict[str, dict]:
    out = {}
    for d in docs:
        pmid = str(d.get("pmid") or d.get("id"))
        title = abstract = ""
        genes, variants, diseases = set(), set(), set()
        for p in d.get("passages", []):
            kind = (p.get("infons") or {}).get("type")
            if kind == "title":
                title = p.get("text", "")
            elif kind == "abstract":
                abstract += (" " if abstract else "") + p.get("text", "")
            for a in p.get("annotations", []):
                inf = a.get("infons") or {}
                if inf.get("type") == "Gene" and inf.get("name"):
                    genes.add(str(inf["name"]).upper())
                elif inf.get("type") == "Variant":
                    variants |= {f"rs{x}" for x in RS.findall(str(inf.get("identifier", "")))}
                    if str(a.get("text", "")).lower().startswith("rs"):
                        variants.add(str(a["text"]).lower())
                elif inf.get("type") == "Disease" and inf.get("name"):
                    diseases.add(str(inf["name"]))
        out[pmid] = {"pmid": pmid, "title": title, "abstract": abstract, "date": str(d.get("date", ""))[:10],
                     "year": str(d.get("date", ""))[:4], "journal": d.get("journal"), "genes": sorted(genes),
                     "variants": sorted(variants), "diseases": sorted(diseases)}
    return out


def pubtator_search(case, query: str, masked: bool = False, before: str | None = None,
                    max_papers: int = 8) -> ToolResult:
    """Up to `max_papers` papers, in PubTator3's relevance order, published before `before` (YYYY-MM-DD) if given.
    When PubTator3 fails, Europe PMC answers under the same cut-off; when both fail, the search fails."""
    args = {"query": query} | ({"before": before} if before else {})
    hits, total, url = [], 0, ""
    for page in (1, 2, 3):
        url = SEARCH.format(q=quote(query), page=page)
        r = case.http.get(url, timeout=60)
        if not r.ok:
            if page == 1:
                fb = literature_search(case, query, masked=masked, before=before)
                fb.summary = "PubTator3 failed; Europe PMC instead.\n" + fb.summary
                return fb
            break
        total = r.data.get("count", 0)
        for x in r.data.get("results", []):
            date = str(x.get("date", ""))[:10]
            if before and (not date or date >= before):
                continue
            hits.append(str(x["pmid"]))
        if len(hits) >= max_papers or page >= int(r.data.get("total_pages") or 1):
            break
    hits = hits[:max_papers]
    papers = []
    if hits:
        e = case.http.get(EXPORT.format(ids=",".join(hits)), timeout=60)
        if not e.ok:
            return failed("literature_search", args, SOURCE, "literature", e)
        found = _papers(e.data.get("PubTator3", []) if isinstance(e.data, dict) else [])
        papers = [found[p] for p in hits if p in found]
    if masked:
        for p in papers:
            p["title"], p["abstract"] = mask_rsids(p["title"]), mask_rsids(p["abstract"])
    shown_q = mask_rsids(query) if masked else query
    head = f"PubTator3: {total} hits for '{shown_q}'" + (f"; kept those published before {before}" if before else "")
    lines = [f"{head}; top {len(papers)} with PMIDs:"]
    lines += [f"PMID {p['pmid']} ({p['year']}): {p['title']}" + ("" if p["abstract"] else " [no abstract]")
              for p in papers]
    if not papers:
        lines.append("No papers: weak evidence, since the literature is incomplete and searches miss papers.")
    return ToolResult("literature_search", args, "\n".join(lines), papers, SOURCE, url, "literature",
                      status="found" if papers else "not_tested")


def chain_tags(paper: dict, rsid: str | None, tfs: list[str], genes: list[str], disease: str) -> dict:
    """Which parts of a chain a paper names: the variant, a TF, a target gene, the disease; and the flags
    "variant and TF" (the key link is published) and "complete chain" (variant, TF and gene)."""
    text = f"{paper.get('title', '')} {paper.get('abstract', '')}"
    upper = {g.upper() for g in paper.get("genes", [])}
    names_variant = bool(rsid) and (rsid.lower() in {v.lower() for v in paper.get("variants", [])}
                                    or rsid.lower() in text.lower())
    tf_hit = sorted({t for t in tfs if t and (t.upper() in upper or re.search(rf"\b{re.escape(t)}\b", text))})
    gene_hit = sorted({g for g in genes if g and (g.upper() in upper or re.search(rf"\b{re.escape(g)}\b", text))})
    disease_hit = any(trait_matches(d, disease) for d in paper.get("diseases", [])) or trait_matches(text, disease)
    flags = []
    if names_variant and tf_hit:
        flags.append("variant and TF")
        if gene_hit:
            flags.append("complete chain")
    return {"pmid": paper.get("pmid"), "variant": names_variant, "tfs": tf_hit, "genes": gene_hit,
            "disease": disease_hit, "flags": flags}
