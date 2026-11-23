"""Europe PMC search (`literature_search`). Saves titles and abstracts; the summariser picks quotes later."""

import re
from datetime import date, timedelta
from urllib.parse import quote

from .base import Case, ToolResult, failed

EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
RSID = re.compile(r"rs\d+", re.IGNORECASE)


def mask_rsids(text: str) -> str:
    return RSID.sub("rs[masked]", text or "")


def published(row: dict) -> str:
    """A Europe PMC row's first publication date (YYYY-MM-DD); with only a year, its last day; '' if undated."""
    first = str(row.get("firstPublicationDate") or "")[:10]
    year = str(row.get("pubYear") or "")
    return first or (f"{year}-12-31" if year.isdigit() else "")


def literature_search(case: Case, query: str, page_size: int = 8, masked: bool = False,
                      before: str | None = None) -> ToolResult:
    """With `before` (YYYY-MM-DD), only papers first published before that day: the query asks Europe PMC for them,
    and a row with no date or a later one is dropped as well, so the cut-off fails closed."""
    args = {"query": query} | ({"before": before} if before else {})
    q = query
    if before:
        last = (date.fromisoformat(before) - timedelta(days=1)).isoformat()
        q = f"({query}) AND FIRST_PDATE:[1800-01-01 TO {last}]"
    # results come in relevance order by default; adding sort=RELEVANCE makes Europe PMC return a spurious 503
    url = f"{EPMC}?query={quote(q)}&format=json&pageSize={page_size}&resultType=core"
    r = case.http.get(url)
    if not r.ok:
        return failed("literature_search", args, "Europe PMC", "literature", r)
    papers = []
    for x in r.data.get("resultList", {}).get("result", []):
        if not x.get("pmid"):
            continue
        if before and not (published(x) and published(x) < before):
            continue
        title, abstract = x.get("title", ""), re.sub(r"<[^>]+>", "", x.get("abstractText") or "")
        if masked:
            title, abstract = mask_rsids(title), mask_rsids(abstract)
        papers.append({"pmid": x["pmid"], "title": title, "year": x.get("pubYear"), "abstract": abstract,
                       "journal": (x.get("journalInfo") or {}).get("journal", {}).get("title")})
    lines = [f"Europe PMC: {r.data.get('hitCount', 0)} hits for '{mask_rsids(query) if masked else query}'"
             + (f", published before {before}" if before else "") + f"; top {len(papers)} with PMIDs:"]
    lines += [f"PMID {p['pmid']} ({p['year']}): {p['title']}" + ("" if p["abstract"] else " [no abstract]")
              for p in papers]
    if not papers:
        lines.append("No papers: weak evidence, since the literature is incomplete and searches miss papers.")
    return ToolResult("literature_search", args, "\n".join(lines), papers, "Europe PMC REST", url, "literature",
                      retrieved_utc=r.retrieved_utc, status="found" if papers else "tested_negative")
