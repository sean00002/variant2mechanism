"""Europe PMC search (`literature_search`). Saves titles and abstracts; the summariser picks quotes later."""

import re
from urllib.parse import quote

from .base import Case, ToolResult, failed

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
RSID = re.compile(r"rs\d+", re.IGNORECASE)


def mask_rsids(text: str) -> str:
    return RSID.sub("rs[masked]", text or "")


def literature_search(case: Case, query: str, page_size: int = 8, masked: bool = False) -> ToolResult:
    args = {"query": query}
    # results come in relevance order by default; adding sort=RELEVANCE makes Europe PMC return a spurious 503
    url = f"{EPMC}?query={quote(query)}&format=json&pageSize={page_size}&resultType=core"
    r = case.http.get(url)
    if not r.ok:
        return failed("literature_search", args, "Europe PMC", "literature", r)
    papers = []
    for x in r.data.get("resultList", {}).get("result", []):
        if not x.get("pmid"):
            continue
        title, abstract = x.get("title", ""), re.sub(r"<[^>]+>", "", x.get("abstractText") or "")
        if masked:
            title, abstract = mask_rsids(title), mask_rsids(abstract)
        papers.append({"pmid": x["pmid"], "title": title, "year": x.get("pubYear"), "abstract": abstract,
                       "journal": (x.get("journalInfo") or {}).get("journal", {}).get("title")})
    lines = [f"Europe PMC: {r.data.get('hitCount', 0)} hits for '{mask_rsids(query) if masked else query}'; "
             f"top {len(papers)} with PMIDs:"]
    lines += [f"PMID {p['pmid']} ({p['year']}): {p['title']}" + ("" if p["abstract"] else " [no abstract]")
              for p in papers]
    if not papers:
        lines.append("No papers: weak evidence, since the literature is incomplete and searches miss papers.")
    return ToolResult("literature_search", args, "\n".join(lines), papers, "Europe PMC REST", url, "literature",
                      retrieved_utc=r.retrieved_utc, status="found" if papers else "tested_negative")
