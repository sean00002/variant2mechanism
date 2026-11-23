"""The v9 test isolation itself (SPEC 13.15): no keys, no network, writable paths outside the repository."""

import os
import socket

import pytest

from variant2mechanism.config import REPO, load_config
from variant2mechanism.context.http import Http, cache_key

from .conftest import KEYS, NetworkBlocked


class FakeResponse:
    status_code = 200
    text = "{}"
    headers: dict = {}

    def json(self):
        return {"hits": 1}


class FakeSession:
    """Answers every request with HTTP 200, as an injected session in an adapter test would."""

    def request(self, *args, **kwargs):
        return FakeResponse()


def test_keys_are_removed():
    assert not any(k in os.environ for k in KEYS)


def test_network_connections_raise():
    with pytest.raises(NetworkBlocked):
        socket.create_connection(("example.org", 443), timeout=1)


def test_writable_paths_point_at_the_temporary_folder(v9_isolation):
    cfg = load_config()
    for section, key in [("cache", "log"), ("budget_usd", "state_file"), ("runs", "dev_dir"), ("eval", "runs_dir"),
                         ("v8", "screen_cache"), ("v8", "dev_dir")]:
        assert cfg.path(section, key).is_relative_to(v9_isolation), (section, key)
    for profile in cfg.get("profiles", {}).values():
        state = (profile.get("budget_usd") or {}).get("state_file")
        assert state is None or not state.startswith(str(REPO))
    http = cfg.path("tools", "http_cache")
    assert http.is_relative_to(v9_isolation) and not http.is_symlink()       # a real folder of per-file links
    repo_cache = REPO / "cache" / "http"            # git-ignored: a fresh checkout has no saved responses yet
    saved = sorted(p.name for p in repo_cache.iterdir()) if repo_cache.is_dir() else []
    assert sorted(p.name for p in http.iterdir()) == saved
    assert all((http / name).resolve() == (REPO / "cache" / "http" / name).resolve() for name in saved[:5])
    assert (http.parent / "llm").is_relative_to(v9_isolation)                 # where LLMClient caches replies
    assert cfg.path("cache", "db") == REPO / "cache" / "qbic.sqlite"          # read-only inputs stay where they are
    assert cfg.path("v8", "runs_dir").is_relative_to(REPO)                    # the saved v8 grid is read by replay


def test_http_writes_land_in_the_temporary_cache_never_in_the_repository(tmp_path):
    http = load_config().path("tools", "http_cache")
    assert not http.is_symlink()                    # so no write below can pass through to the repository's cache
    url = "https://example.org/v9-isolation-probe?q=1"
    name = f"{cache_key('GET', url)}.json"
    assert not (REPO / "cache" / "http" / name).exists()
    assert Http(http, session=FakeSession()).get(url).ok
    assert (http / name).exists() and not (http / name).is_symlink()
    assert not (REPO / "cache" / "http" / name).exists()
    saved = tmp_path / "saved.json"                 # a refresh replaces a link, never the file it points to
    saved.write_text('{"status": 200, "data": "original", "retrieved_utc": "T0"}')
    refreshed = f"{cache_key('GET', url + '&r=1')}.json"
    (http / refreshed).symlink_to(saved)
    assert Http(http, refresh=True, session=FakeSession()).get(url + "&r=1").data == {"hits": 1}
    assert not (http / refreshed).is_symlink() and "original" in saved.read_text()
