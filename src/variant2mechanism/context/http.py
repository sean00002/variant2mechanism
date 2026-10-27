"""HTTP with an on-disk response cache and retries (spec 2, section 6).

Responses are cached under `<cache_dir>/<sha256 of method, URL and body>.json`, so reruns are deterministic and
free. `refresh=True` bypasses the cache for reads (and rewrites it); `offline=True` never touches the network,
which is how the tests replay recorded fixtures. Errors are returned, never raised.
"""

import hashlib
import json
import os
import threading
import time
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import requests

UA = {"User-Agent": "variant2mechanism/0.1 (research demo; contact shengyu.li@duke.edu)"}
RETRY_STATUS = {429, 500, 502, 503, 504, 529}


@dataclass
class HttpResult:
    ok: bool
    status: int | None
    data: Any                  # parsed JSON, or text
    url: str
    retrieved_utc: str
    cached: bool = False
    error: str | None = None
    retryable: bool = False             # the failure may be transient (timeout, connection, 429, 5xx)


def cache_key(method: str, url: str, body: Any = None) -> str:
    blob = json.dumps([method.upper(), url, body], sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode()).hexdigest()


class Http:
    def __init__(self, cache_dir: str | Path, refresh: bool = False, offline: bool = False, session=None,
                 sleep=time.sleep, tries: int = 6, max_wait: float = 120):
        self.cache_dir = Path(cache_dir)
        self.refresh, self.offline = refresh, offline
        self.session = session or requests.Session()
        self.sleep, self.tries, self.max_wait = sleep, tries, max_wait

    def request(self, method: str, url: str, json_body: Any = None, timeout: float = 60,
                headers: dict | None = None) -> HttpResult:
        key = cache_key(method, url, json_body)
        path = self.cache_dir / f"{key}.json"
        if path.exists() and not self.refresh:
            rec = json.loads(path.read_text())
            return HttpResult(True, rec["status"], rec["data"], url, rec["retrieved_utc"], cached=True)
        if self.offline:
            return HttpResult(False, None, None, url, _now(), error=f"offline and not cached: {method} {url}")
        last_err, retry_after = None, None
        for attempt in range(self.tries):
            try:
                r = self.session.request(method, url, json=json_body, timeout=timeout,
                                         headers={**UA, **({"Content-Type": "application/json"} if json_body else {}),
                                                  **(headers or {})})
            except requests.RequestException as e:
                last_err, status = f"{type(e).__name__}: {str(e)[:200]}", None
            else:
                status = r.status_code
                if status == 200:
                    try:
                        data = r.json()
                    except ValueError:
                        data = r.text
                    now = _now()
                    self.cache_dir.mkdir(parents=True, exist_ok=True)
                    tmp = path.with_name(f"{path.name}.{os.getpid()}-{threading.get_ident()}.tmp")
                    tmp.write_text(json.dumps({"method": method, "url": url, "body": json_body, "status": status,
                                               "retrieved_utc": now, "data": data}))
                    os.replace(tmp, path)   # atomic: a run fetching the same URL at once never reads half a file
                    return HttpResult(True, status, data, url, now)
                last_err = f"HTTP {status}: {r.text[:200]}"
                if status not in RETRY_STATUS:
                    return HttpResult(False, status, None, url, _now(), error=last_err)
                retry_after = _retry_after(getattr(r, "headers", None) or {})
            if attempt < self.tries - 1:
                # 2, 4, 8, 16, 32 s (about a minute over 6 tries); a server's Retry-After wins, up to max_wait
                self.sleep(min(self.max_wait, retry_after if retry_after is not None else 2 ** (attempt + 1)))
                retry_after = None
        return HttpResult(False, None, None, url, _now(), error=f"failed after {self.tries} tries: {last_err}",
                          retryable=True)

    def get(self, url: str, **kw) -> HttpResult:
        return self.request("GET", url, **kw)

    def post(self, url: str, body: Any, **kw) -> HttpResult:
        return self.request("POST", url, json_body=body, **kw)

    def graphql(self, url: str, query: str, **kw) -> HttpResult:
        r = self.post(url, {"query": query}, **kw)
        if r.ok and isinstance(r.data, dict) and r.data.get("errors") and not r.data.get("data"):
            return HttpResult(False, r.status, r.data, url, r.retrieved_utc, r.cached,
                              error=f"GraphQL error: {str(r.data['errors'])[:200]}")
        return r


def _retry_after(headers) -> float | None:
    value = headers.get("Retry-After") or headers.get("retry-after")
    try:
        return max(0.0, float(value)) if value is not None else None
    except (TypeError, ValueError):
        return None


def _now() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")
