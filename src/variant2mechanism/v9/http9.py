"""The v9 HTTP layer (SPEC 13.3, contract C1): context.http.Http with per-provider rules and a per-run request cap.

Why v9 has its own request loop: the shared Http retries every HTTP 500 six times with up to a minute of backoff, and
context.base.call_tool then re-runs the whole tool after 60-second waits. Two providers make that a stall, not a
recovery: Europe PMC answers a full-text request for an article outside its open-access subset with HTTP 500 and a
JSON error body, and SCREEN answers 401/403 until a key is supplied. Neither changes on a retry, so both are reported
at once as "unavailable: ...". The GWAS Catalog has returned 30-second 500s for hours, so it gets two tries.

What stays as in Http: the response cache (one file per sha256 of method, URL and body; only HTTP 200 is cached), so a
saved response serves Http and Http9 alike; offline mode never touches the network; errors are returned, never
raised. What v9 adds:
- a per-run cap on network sends (default 150), so a run cannot fan out without bound;
- throttles: GTEx one request at a time, NCBI at most 3 a second, Europe PMC at most 10 a second;
- a User-Agent with no contact address, and a refusal to send any URL that carries a credential or an e-mail address
  (the cache stores URLs; keys travel in headers, which are never cached or logged);
- counters (requests_made, cache_hits) for the run's metrics.

classify() maps a result to what an adapter reports: success, no_records (HTTP 404), unavailable (a stated refusal,
an outage that outlasted the retries, the request cap, or a response missing from the cache in an offline run) or
error. execution_status() turns that into the ToolCall's execution_status, keeping a cache miss distinct.
"""

import json
import os
import threading
import time
from collections.abc import Callable
from contextlib import nullcontext
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal
from urllib.parse import parse_qsl, urlsplit

import requests

from ..config import Config
from ..context.http import RETRY_STATUS, Http, HttpResult, cache_key

USER_AGENT = "variant2mechanism/0.9 (research software)"
DEFAULT_REQUEST_CAP = 150
DEFAULT_TRIES = 4            # 2 + 4 + 8 s of backoff: an outage costs seconds, not the run's wall time
DEFAULT_MAX_WAIT = 60.0      # the longest Retry-After honoured
OFFLINE_MISS = "offline and not cached"
UNAVAILABLE = "unavailable:"
# Query parameters that would put a credential or a contact address into a cached, logged URL.
FORBIDDEN_PARAMS = frozenset({"api_key", "apikey", "access_token", "token", "key", "email"})

Classification = Literal["success", "no_records", "unavailable", "error"]


@dataclass(frozen=True)
class HostRule:
    """How one provider is called. `name` keys the throttle and the serial lock, so hosts of one provider share them."""
    name: str
    host: str
    path: str = ""                       # path prefix within the host
    tries: int | None = None             # None: the client's default
    per_second: float | None = None      # throttle: at most this many sends a second
    serial: bool = False                 # one request at a time
    json_500_unavailable: bool = False   # HTTP 500 with a JSON body is a stated refusal, not an outage
    auth_unavailable: bool = False       # HTTP 401/403 means a key is needed, not a retry


RULES: tuple[HostRule, ...] = (
    HostRule("gwas_catalog", "www.ebi.ac.uk", "/gwas/", tries=2),
    HostRule("europe_pmc", "www.ebi.ac.uk", "/europepmc/", per_second=10.0, json_500_unavailable=True),
    HostRule("ncbi", "eutils.ncbi.nlm.nih.gov", per_second=3.0),
    HostRule("ncbi", "www.ncbi.nlm.nih.gov", per_second=3.0),
    HostRule("gtex", "gtexportal.org", serial=True),
    HostRule("screen", "screen.api.wenglab.org", auth_unavailable=True),
    HostRule("screen", "screen-beta-api.wenglab.org", auth_unavailable=True),
)


def rule_for(url: str) -> HostRule | None:
    """The provider rule for a URL (host match, then the longest path prefix), or None for the defaults."""
    parts = urlsplit(url)
    host, path = (parts.hostname or "").lower(), parts.path or "/"
    hits = [r for r in RULES if r.host == host and path.startswith(r.path or "/")]
    return max(hits, key=lambda r: len(r.path), default=None)


def credential_problem(url: str) -> str | None:
    """Why a URL must not be sent (a key, token or e-mail address in its query string), or None."""
    names = {name.lower() for name, _ in parse_qsl(urlsplit(url).query, keep_blank_values=True)}
    bad = sorted(names & FORBIDDEN_PARAMS)
    if bad:
        return (f"the URL carries {', '.join(bad)}: credentials and contact addresses never go in a URL, because "
                "the response cache stores URLs (send keys in a header)")
    return None


def _now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def _retry_after(headers: Any) -> float | None:
    if not headers:
        return None
    value = headers.get("Retry-After") or headers.get("retry-after")
    try:
        return max(0.0, float(value)) if value is not None else None
    except (TypeError, ValueError):
        return None


def _json_body(response: Any) -> bool:
    """Whether an error response carries a JSON object (Europe PMC's way of saying "not open access")."""
    content_type = str((getattr(response, "headers", None) or {}).get("Content-Type", "")).lower()
    if "json" in content_type:
        return True
    try:
        return isinstance(json.loads(getattr(response, "text", "") or ""), dict)
    except ValueError:
        return False


class Http9(Http):
    """context.http.Http with the v9 rules in the module docstring. Same request/get/post/graphql, returning
    HttpResult and never raising; `offline`, `requests_made` (network sends) and `cache_hits` are public."""

    def __init__(self, cache_dir: str | Path, *, offline: bool, refresh: bool = False, session=None,
                 sleep: Callable[[float], None] = time.sleep, clock: Callable[[], float] = time.monotonic,
                 request_cap: int = DEFAULT_REQUEST_CAP, tries: int = DEFAULT_TRIES,
                 max_wait: float = DEFAULT_MAX_WAIT):
        super().__init__(cache_dir, refresh=refresh, offline=offline, session=session, sleep=sleep, tries=tries,
                         max_wait=max_wait)
        self.clock = clock
        self.request_cap = request_cap
        self.requests_made = 0
        self.cache_hits = 0
        self._lock = threading.Lock()
        self._serial: dict[str, threading.Lock] = {}
        self._next_send: dict[str, float] = {}

    @classmethod
    def from_config(cls, cfg: Config, *, offline: bool) -> "Http9":
        """The run's client on config's tools.http_cache (an isolated temporary copy in tests), with the request cap
        from v9.limits.http_requests (default 150)."""
        limits = (cfg.get("v9") or {}).get("limits") or {}
        return cls(cfg.path("tools", "http_cache"), offline=offline,
                   request_cap=int(limits.get("http_requests", DEFAULT_REQUEST_CAP)))

    # --- the request loop ------------------------------------------------------------------------------------------

    def request(self, method: str, url: str, json_body: Any = None, timeout: float = 60,
                headers: dict | None = None) -> HttpResult:
        if problem := credential_problem(url):
            return HttpResult(False, None, None, url, _now(), error=f"refused: {problem}")
        path = self.cache_dir / f"{cache_key(method, url, json_body)}.json"
        if path.exists() and not self.refresh:
            rec = json.loads(path.read_text())
            with self._lock:
                self.cache_hits += 1
            return HttpResult(True, rec["status"], rec["data"], url, rec["retrieved_utc"], cached=True)
        if self.offline:
            return HttpResult(False, None, None, url, _now(), error=f"{OFFLINE_MISS}: {method} {url}")
        rule = rule_for(url)
        tries = rule.tries if rule is not None and rule.tries else self.tries
        last_error, retry_after = "no attempt made", None
        for attempt in range(tries):
            if not self._reserve():
                return HttpResult(False, None, None, url, _now(),
                                  error=f"{UNAVAILABLE} per-run HTTP request cap ({self.request_cap}) reached")
            try:
                response = self._send(rule, method, url, json_body, timeout, headers)
            except requests.RequestException as e:
                last_error = f"{type(e).__name__}: {str(e)[:200]}"
            else:
                status = response.status_code
                if status == 200:
                    return self._store(path, method, url, json_body, response)
                text = (getattr(response, "text", "") or "")[:200]
                if status in (401, 403):     # access, not an outage: never retried
                    return HttpResult(False, status, None, url, _now(), error=f"{UNAVAILABLE} HTTP {status}: {text}")
                if status == 500 and rule is not None and rule.json_500_unavailable and _json_body(response):
                    return HttpResult(False, status, None, url, _now(),
                                      error=f"{UNAVAILABLE} HTTP 500 with a JSON body (the provider declines this "
                                            f"request): {text}")
                last_error = f"HTTP {status}: {text}"
                if status not in RETRY_STATUS:
                    return HttpResult(False, status, None, url, _now(), error=last_error)
                retry_after = _retry_after(getattr(response, "headers", None))
            if attempt < tries - 1:
                self.sleep(min(self.max_wait, retry_after if retry_after is not None else 2 ** (attempt + 1)))
                retry_after = None
        return HttpResult(False, None, None, url, _now(), error=f"failed after {tries} tries: {last_error}",
                          retryable=True)

    def _reserve(self) -> bool:
        """Count one network send, unless the run's cap is reached."""
        with self._lock:
            if self.requests_made >= self.request_cap:
                return False
            self.requests_made += 1
            return True

    def _send(self, rule: HostRule | None, method: str, url: str, json_body: Any, timeout: float,
              headers: dict | None):
        serial = self._serial_lock(rule.name) if rule is not None and rule.serial else nullcontext()
        with serial:
            if rule is not None and rule.per_second:
                self._throttle(rule)
            sent = {"User-Agent": USER_AGENT, **({"Content-Type": "application/json"} if json_body is not None else {}),
                    **(headers or {})}
            return self.session.request(method, url, json=json_body, timeout=timeout, headers=sent)

    def _serial_lock(self, name: str) -> threading.Lock:
        with self._lock:
            return self._serial.setdefault(name, threading.Lock())

    def _throttle(self, rule: HostRule) -> None:
        """Book the provider's next send slot, then wait for it (outside the lock, so other hosts are not held)."""
        interval = 1.0 / float(rule.per_second or 1.0)
        with self._lock:
            now = self.clock()
            slot = max(now, self._next_send.get(rule.name, now))
            self._next_send[rule.name] = slot + interval
        if slot > now:
            self.sleep(slot - now)

    def _store(self, path: Path, method: str, url: str, json_body: Any, response) -> HttpResult:
        """Cache an HTTP 200 in the shared format (method, url, body, status, retrieved_utc, data); never headers."""
        try:
            data = response.json()
        except ValueError:
            data = response.text
        now = _now()
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        tmp = path.with_name(f"{path.name}.{os.getpid()}-{threading.get_ident()}.tmp")
        tmp.write_text(json.dumps({"method": method, "url": url, "body": json_body, "status": 200,
                                   "retrieved_utc": now, "data": data}))
        os.replace(tmp, path)     # atomic: a concurrent reader never sees half a file
        return HttpResult(True, 200, data, url, now)


# --- what a result means for an adapter ------------------------------------------------------------------------------

def is_cache_miss(result: HttpResult) -> bool:
    """The response is not in the cache and the client is offline (cache-only mode): nothing was sent."""
    return not result.ok and (result.error or "").startswith(OFFLINE_MISS)


def classify(result: HttpResult) -> Classification:
    """success; no_records (HTTP 404: the resource does not exist); unavailable (a stated refusal such as Europe PMC's
    500-JSON or SCREEN's 401/403, the request cap, an outage that outlasted the retries, or a cache miss in an offline
    run: use is_cache_miss() to tell that one apart); or error (anything else, such as HTTP 400 or a refused URL)."""
    if result.ok:
        return "success"
    if result.status == 404:
        return "no_records"
    error = result.error or ""
    if error.startswith(UNAVAILABLE) or is_cache_miss(result) or result.retryable or result.status in (401, 403):
        return "unavailable"
    return "error"


def execution_status(result: HttpResult) -> Literal["success", "unavailable", "cache_miss", "error"]:
    """The ToolCall execution_status for one response: a 404 is a successful retrieval of no records."""
    kind = classify(result)
    if kind in ("success", "no_records"):
        return "success"
    if kind == "unavailable":
        return "cache_miss" if is_cache_miss(result) else "unavailable"
    return "error"
