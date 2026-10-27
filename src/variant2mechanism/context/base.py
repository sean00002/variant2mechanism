"""Shared types for the context tools: the case they run on and what they return."""

import time
from dataclasses import dataclass, field
from typing import Any

from ..qbic.variants import Variant
from .http import Http, HttpResult

SUMMARY_LIMIT = 2000


@dataclass
class Case:
    """What code binds for every tool call; the model never chooses the variant."""
    variant: Variant
    disease: str
    origin: str = "germline"                 # germline or somatic
    rsid: str | None = None
    expression_context: str | None = None
    http: Http | None = None
    extra: dict = field(default_factory=dict)
    retry_rounds: int = 2                    # whole-tool re-runs after a failure that may be transient
    retry_wait: float = 60                   # seconds before each re-run

    # API-specific variant formats
    @property
    def ensembl(self) -> str:
        return f"{self.variant.chrom_bare}:{self.variant.pos}"

    @property
    def opentargets(self) -> str:
        v = self.variant
        return f"{v.chrom_bare}_{v.pos}_{v.ref}_{v.alt}"

    @property
    def gtex(self) -> str:
        v = self.variant
        return f"{v.chrom}_{v.pos}_{v.ref}_{v.alt}_b38"

    @property
    def gnomad(self) -> str:
        v = self.variant
        return f"{v.chrom_bare}-{v.pos}-{v.ref}-{v.alt}"


@dataclass
class ToolResult:
    tool: str
    args: dict
    summary: str
    full: Any
    source: str
    url: str
    kind: str                    # computational, epigenomic, genetic, literature, expression
    ok: bool = True
    retrieved_utc: str | None = None
    limit: int = SUMMARY_LIMIT          # QBiC-SELEX results use their own 3,000-character limit
    retryable: bool = False             # failed, but a later attempt might succeed
    attempts: int = 1

    def __post_init__(self):
        if len(self.summary) > self.limit:
            self.summary = self.summary[: self.limit - 15].rstrip() + "\n[truncated]"


def failed(tool: str, args: dict, source: str, kind: str, r: HttpResult | None = None, message: str | None = None):
    msg = message or (r.error if r else "unknown error")
    return ToolResult(tool, args, f"{source} lookup failed: {msg}", {"error": msg}, source, r.url if r else "", kind,
                      ok=False, retrieved_utc=r.retrieved_utc if r else None, retryable=bool(r and r.retryable))


def call_tool(fn, case: Case, *args, **kwargs) -> ToolResult:
    """Run a context tool; after a failure that may be transient, wait and run it again (case.retry_rounds times).
    Each request inside already retries with backoff, so this covers outages longer than about a minute."""
    res = fn(case, *args, **kwargs)
    sleep = case.http.sleep if case.http is not None else time.sleep
    for attempt in range(2, case.retry_rounds + 2):
        if res.ok or not res.retryable:
            break
        sleep(case.retry_wait)
        res = fn(case, *args, **kwargs)
        res.attempts = attempt
    return res


def fmt_p(p) -> str:
    try:
        return f"{float(p):.1e}"
    except (TypeError, ValueError):
        return str(p)
