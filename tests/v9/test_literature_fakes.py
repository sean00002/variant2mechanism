"""Test doubles shared by the literature tests (no tests here).

FakeHttp stands in for Http9 (contract C1): it answers from a URL map, never sends, records every URL it was asked for,
and fails the way C1 says Http9 does (an offline miss has no HTTP status; an access limit's error starts with
"unavailable:"). The fixtures under fixtures/literature/ are synthetic: invented text and test-only identifiers.
"""

import json
from pathlib import Path
from typing import Any

from variant2mechanism.context.http import HttpResult
from variant2mechanism.v9 import literature as lit
from variant2mechanism.v9.graph import ClaimGraph
from variant2mechanism.v9.schemas import Case, ExperimentRecord, ExperimentSystem, ToolCall, ToolRequest, Variant
from variant2mechanism.v9.tools import ToolLimits, ToolRunner

FIXTURES = Path(__file__).parent / "fixtures" / "literature"
NOW = "2026-11-08T12:00:00+00:00"
UNAVAILABLE_500 = "unavailable: Europe PMC returned HTTP 500 with a JSON body (no open-access full text)"


def case() -> Case:
    """The development case (rs1427407, not a gold case)."""
    return Case(case_id="DEV-LIT-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"))


def text(name: str) -> str:
    return (FIXTURES / name).read_text()


def records() -> dict[str, Any]:
    return json.loads((FIXTURES / "europepmc_records.json").read_text())


def search_response(rows: list[dict[str, Any]], hit_count: int | None = None) -> dict[str, Any]:
    """A Europe PMC search envelope (resultType=core) around result rows."""
    return {"version": "6.9", "hitCount": len(rows) if hit_count is None else hit_count,
            "request": {"resultType": "CORE", "cursorMark": "*", "pageSize": 25, "synonym": False},
            "resultList": {"result": rows}}


def unavailable(url: str, error: str = UNAVAILABLE_500, status: int | None = 500) -> HttpResult:
    """What Http9 returns for a non-retryable access limit (Europe PMC's 500 with a JSON body)."""
    return HttpResult(False, status, None, url, NOW, error=error)


def failed(url: str, status: int = 503) -> HttpResult:
    """A failure as Http9 reports it: an outage that outlasted the retries, or any other status as it came."""
    if status in (429, 500, 502, 503, 504):
        return HttpResult(False, None, None, url, NOW, error=f"failed after 4 tries: HTTP {status}: down",
                          retryable=True)
    return HttpResult(False, status, None, url, NOW, error=f"HTTP {status}: refused")


class FakeHttp:
    """An Http9 double: `routes` maps URL -> payload (served as a cached 200) or an HttpResult (served as is)."""

    def __init__(self, routes: dict[str, Any], *, offline: bool = True):
        self.routes, self.offline = dict(routes), offline
        self.calls: list[str] = []
        self.requests_made = 0
        self.cache_hits = 0

    def get(self, url: str, **kw: Any) -> HttpResult:
        self.calls.append(url)
        answer = self.routes.get(url)
        if isinstance(answer, HttpResult):
            return answer
        if answer is None:
            if self.offline:
                return HttpResult(False, None, None, url, NOW, error=f"offline and not cached: GET {url}")
            self.requests_made += 1
            return HttpResult(False, 404, None, url, NOW, error="HTTP 404: not found")
        self.cache_hits += 1
        return HttpResult(True, 200, answer, url, NOW, cached=True)


def routes() -> dict[str, Any]:
    """Every synthetic article as Europe PMC and NCBI would serve it: metadata by PMCID (and by PMID for the two
    papers the tests read by PMID), fullTextXML for the open-access papers, efetch for the others."""
    rec = records()
    out: dict[str, Any] = {}
    for pmcid in ("PMC9000001", "PMC9000002", "PMC9000003", "PMC9000004", "PMC9000005", "PMC9000007", "PMC9000008"):
        out[lit.metadata_url(pmcid, None)] = search_response([rec[pmcid]])
    out[lit.metadata_url(None, "90000001")] = search_response([rec["PMC9000001"]])
    out[lit.metadata_url(None, "90000006")] = search_response([rec["PMID90000006"]])
    out[lit.fulltext_url("PMC9000001")] = text("oa_fulltext.xml")
    out[lit.fulltext_url("PMC9000005")] = text("oa_hostile.xml")
    out[lit.fulltext_url("PMC9000007")] = text("oa_cases.xml")
    out[lit.fulltext_url("PMC9000008")] = text("oa_variants.xml")
    out[lit.efetch_url("PMC9000002")] = text("efetch_manuscript.xml")
    out[lit.efetch_url("PMC9000003")] = text("efetch_no_body.xml")
    out[lit.efetch_url("PMC9000004")] = text("efetch_review.xml")
    return out


def runner(http: FakeHttp, run_dir: Path | None = None, **limits: int) -> ToolRunner:
    return ToolRunner(mode="cache_only" if http.offline else "live", http=http, run_dir=run_dir,
                      limits=ToolLimits(**limits), clock=lambda: NOW)


def read(run: ToolRunner, graph: ClaimGraph, focus: list[str] | None = None, **ids: str) -> ToolCall:
    params: dict[str, Any] = {**ids, **({"focus": focus} if focus else {})}
    return run.run(ToolRequest(tool=lit.READ_TOOL, params=params, purpose="test"), graph.case, graph,
                   "literature_investigator")


def search(run: ToolRunner, graph: ClaimGraph, query: str, **params: Any) -> ToolCall:
    return run.run(ToolRequest(tool=lit.SEARCH_TOOL, params={"query": query, **params}, purpose="test"), graph.case,
                   graph, "literature_investigator")


def record(passage: str, *, intervention: str, endpoint: str = "", result: str = "an invented result",
           source_id: str = "PMID:90000001", cell: str = "K562", organism: str = "human", genotype: str = "",
           comparator: str = "", direction: str = "unspecified", **fields: Any) -> ExperimentRecord:
    """An extracted experiment as the literature investigator would return it (`genotype` is the context's genotype;
    the allele a direction refers to is `compared_allele`)."""
    return ExperimentRecord(source_id=source_id, access="full_text", location=fields.pop("location", "sec1/p1"),
                            passage=passage, intervention=intervention, endpoint=endpoint, result=result,
                            comparator=comparator, direction=direction,
                            system=ExperimentSystem(organism=organism, tissue_or_cell=cell,
                                                    genotype_or_allele=genotype),
                            **fields)


def cases(run_dir: Path, pmcid: str = "PMC9000007") -> tuple[ClaimGraph, ToolCall, "lit.Article"]:
    """A graph, a successful read of an article and its saved text: by default the extraction-cases article
    (oa_cases.xml, PMC9000007, which names one variant); PMC9000008 is oa_variants.xml (several variants)."""
    graph = ClaimGraph(case())
    call = read(runner(FakeHttp(routes()), run_dir), graph, pmcid=pmcid, focus=["gata1"])
    return graph, call, lit.load_article(run_dir, call)
