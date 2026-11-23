"""Http9 (contract C1): offline never sends, the per-run cap, stated refusals classified without retries, throttles,
and no contact address or credential in anything sent or cached. Fake sessions only: nothing here needs data."""

import json
import threading
import time

from variant2mechanism.context.http import HttpResult
from variant2mechanism.v9.http9 import (
    USER_AGENT,
    Http9,
    classify,
    execution_status,
    is_cache_miss,
    rule_for,
)

EPMC_FULLTEXT = "https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3062476/fullTextXML"
GWAS = "https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs1427407&size=100"
SCREEN = "https://screen.api.wenglab.org/graphql"
NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={}&tool=variant2mechanism"
GTEX = "https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr2_{}_T_G_b38&datasetId=gtex_v8"


class FakeResponse:
    def __init__(self, status: int = 200, body=None, text: str | None = None, headers: dict | None = None):
        self.status_code = status
        self._body = body
        self.text = text if text is not None else (json.dumps(body) if body is not None else "")
        self.headers = headers or {}

    def json(self):
        if self._body is None:
            raise ValueError("not JSON")
        return self._body


class FakeSession:
    """Answers from a queue of responses (then HTTP 200), recording every request it is sent."""

    def __init__(self, *responses: FakeResponse, delay: float = 0.0):
        self.queue = list(responses)
        self.calls: list[dict] = []
        self.delay = delay
        self.active = self.peak = 0
        self.lock = threading.Lock()

    def request(self, method, url, json=None, timeout=None, headers=None):
        with self.lock:
            self.calls.append({"method": method, "url": url, "json": json, "headers": dict(headers or {})})
            self.active += 1
            self.peak = max(self.peak, self.active)
            response = self.queue.pop(0) if self.queue else FakeResponse(200, {"ok": True})
        time.sleep(self.delay)
        with self.lock:
            self.active -= 1
        return response


def test_offline_never_sends_and_reports_a_cache_miss(tmp_path):
    session = FakeSession()
    http = Http9(tmp_path / "http", offline=True, session=session)
    miss = http.get("https://rest.ensembl.org/vep/human/region/2:60490908-60490908:1/G")
    assert not miss.ok and is_cache_miss(miss)
    assert (classify(miss), execution_status(miss)) == ("unavailable", "cache_miss")
    assert session.calls == [] and http.requests_made == 0
    online = Http9(tmp_path / "http", offline=False, session=FakeSession(FakeResponse(200, {"saved": 1})))
    assert online.get("https://rest.ensembl.org/a").ok and online.requests_made == 1
    hit = http.get("https://rest.ensembl.org/a")
    assert hit.ok and hit.cached and hit.data == {"saved": 1}
    assert (http.cache_hits, http.requests_made, session.calls) == (1, 0, [])


def test_the_request_cap_stops_sending(tmp_path):
    session = FakeSession()
    http = Http9(tmp_path, offline=False, session=session, request_cap=2)
    assert http.get("https://rest.ensembl.org/1").ok and http.get("https://rest.ensembl.org/2").ok
    capped = http.get("https://rest.ensembl.org/3")
    assert capped.error == "unavailable: per-run HTTP request cap (2) reached"
    assert classify(capped) == "unavailable" and execution_status(capped) == "unavailable"
    assert len(session.calls) == 2 and http.requests_made == 2
    assert http.get("https://rest.ensembl.org/1").cached          # saved responses are still served
    assert len(session.calls) == 2


def test_europe_pmc_500_with_json_is_unavailable_and_not_retried(tmp_path):
    body = {"timestamp": "2026-11-08", "status": 500, "error": "Internal Server Error", "path": "/PMC3062476"}
    sleeps: list[float] = []
    session = FakeSession(FakeResponse(500, body, headers={"Content-Type": "application/json"}))
    http = Http9(tmp_path / "http", offline=False, session=session, sleep=sleeps.append)
    r = http.get(EPMC_FULLTEXT)
    assert not r.ok and r.error.startswith("unavailable:") and classify(r) == "unavailable"
    assert len(session.calls) == 1 and sleeps == [] and not (tmp_path / "http").exists()
    outage = FakeSession(*[FakeResponse(500, text="<html>busy</html>")] * 4)      # a real outage is retried
    r2 = Http9(tmp_path / "h2", offline=False, session=outage, sleep=sleeps.append).get(EPMC_FULLTEXT)
    assert not r2.ok and r2.retryable and len(outage.calls) == 4 and classify(r2) == "unavailable"


def test_screen_401_and_403_are_unavailable_without_retrying(tmp_path):
    for status in (401, 403):
        sleeps: list[float] = []
        session = FakeSession(FakeResponse(status, {"error": "request not allowed"}))
        r = Http9(tmp_path / str(status), offline=False, session=session, sleep=sleeps.append).post(
            SCREEN, {"query": "{ __typename }"})
        assert r.error.startswith("unavailable:") and classify(r) == "unavailable"
        assert len(session.calls) == 1 and sleeps == []


def test_gwas_catalog_gets_two_tries(tmp_path):
    sleeps: list[float] = []
    session = FakeSession(*[FakeResponse(500, text="timeout")] * 5)
    r = Http9(tmp_path, offline=False, session=session, sleep=sleeps.append).get(GWAS)
    assert len(session.calls) == 2 and sleeps == [2] and "after 2 tries" in r.error
    assert classify(r) == "unavailable"


def test_no_contact_address_and_no_credential_in_a_url_or_the_cache(tmp_path):
    session = FakeSession()
    http = Http9(tmp_path / "http", offline=False, session=session)
    assert http.get(NCBI.format(3062476)).ok
    sent = session.calls[0]["headers"]
    assert sent["User-Agent"] == USER_AGENT
    assert not any("@" in str(v) or "contact" in str(v).lower() for v in sent.values())
    for url in (NCBI.format(1) + "&email=someone%40example.org", NCBI.format(2) + "&api_key=abc"):
        refused = http.get(url)
        assert refused.error.startswith("refused:") and classify(refused) == "error"
    assert len(session.calls) == 1                                  # the refused URLs were never sent
    assert http.post(SCREEN, {"query": "{ x }"}, headers={"Authorization": "Bearer secret-123"}).ok
    assert session.calls[-1]["headers"]["Authorization"] == "Bearer secret-123"
    saved = "".join(p.read_text() for p in (tmp_path / "http").iterdir())
    assert "secret-123" not in saved and "Authorization" not in saved and "@" not in saved


def test_throttles_space_ncbi_and_europe_pmc_sends(tmp_path):
    sleeps: list[float] = []
    http = Http9(tmp_path, offline=False, session=FakeSession(), sleep=sleeps.append, clock=lambda: 100.0)
    for i in range(3):
        http.get(NCBI.format(i))
    assert [round(s, 3) for s in sleeps] == [0.333, 0.667]
    sleeps.clear()
    for i in range(3):
        http.get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=q{i}&format=json")
    assert [round(s, 3) for s in sleeps] == [0.1, 0.2]
    sleeps.clear()
    for i in range(3):
        http.get(f"https://rest.ensembl.org/{i}")
    assert sleeps == []


def test_gtex_requests_are_serial(tmp_path):
    session = FakeSession(delay=0.03)
    http = Http9(tmp_path, offline=False, session=session)
    threads = [threading.Thread(target=http.get, args=(GTEX.format(60490908 + i),)) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert len(session.calls) == 4 and session.peak == 1


def test_classify_maps_each_outcome():
    def result(ok=False, status=None, error=None, retryable=False):
        return HttpResult(ok, status, None, "https://x", "T0", error=error, retryable=retryable)

    table = [(result(ok=True, status=200), "success", "success"),
             (result(status=404, error="HTTP 404: not found"), "no_records", "success"),
             (result(status=400, error="HTTP 400: bad request"), "error", "error"),
             (result(error="failed after 4 tries: HTTP 503: busy", retryable=True), "unavailable", "unavailable"),
             (result(error="offline and not cached: GET https://x"), "unavailable", "cache_miss"),
             (result(status=403, error="unavailable: HTTP 403: no"), "unavailable", "unavailable")]
    assert [(classify(r), execution_status(r)) for r, *_ in table] == [(c, s) for _, c, s in table]


def test_rules_tell_providers_on_one_host_apart():
    assert rule_for(GWAS).name == "gwas_catalog" and rule_for(EPMC_FULLTEXT).name == "europe_pmc"
    assert rule_for("https://rest.ensembl.org/vep") is None


def test_from_config_uses_the_isolated_cache_and_the_default_cap(v9_cfg, v9_isolation):
    http = Http9.from_config(v9_cfg, offline=True)
    assert http.offline and http.request_cap == 150
    assert http.cache_dir == v9_cfg.path("tools", "http_cache") and http.cache_dir.is_relative_to(v9_isolation)
