"""Isolation for every v9 test (SPEC 13.15): no API keys, no network, nothing written inside the repository.

The autouse fixture removes the model and SCREEN keys, makes any IPv4/IPv6 socket connect raise NetworkBlocked, and
points config.yaml's writable paths (the QBiC call log, budget state files, run folders, the SCREEN and job caches,
and the model-response cache) at a temporary folder through V2M_CONFIG. The HTTP cache stays readable without being
writable: the temporary cache/http is a real folder holding one link per saved response in the repository's cache.
Reads follow the links; a write (a fake session's response, or a refresh, which replaces a link atomically) creates a
file in the temporary folder, never in the repository.
"""

import copy
import json
import socket

import pytest
import yaml

from variant2mechanism.config import REPO, Config, load_config

KEYS = ("OPENROUTER_API_KEY", "V2M_ANTHROPIC_API_KEY", "V2M_SCREEN_API_KEY")
WRITABLE = ("log", "state_file", "dev_dir", "runs_dir", "screen_cache", "jobs_dir")
INET = (socket.AF_INET, socket.AF_INET6)


class NetworkBlocked(RuntimeError):
    """Raised by any network connection attempted during a v9 test."""


def _redirect(node: dict, root, path: tuple = ()) -> None:
    """Point every writable path at `root`, except the saved v8 grid (read by replay) and remote cluster paths."""
    for key, value in node.items():
        here = (*path, key)
        if isinstance(value, dict):
            _redirect(value, root, here)
        elif (key in WRITABLE and isinstance(value, str) and here[-2:] != ("v8", "runs_dir")
              and "cluster" not in here):
            node[key] = str(root / "_".join(map(str, here)))


@pytest.fixture(scope="session")
def http_cache_names() -> list[str]:
    """The saved responses in the repository's HTTP cache (listed once per test session)."""
    source = REPO / "cache" / "http"
    return sorted(p.name for p in source.iterdir()) if source.is_dir() else []


@pytest.fixture(autouse=True)
def v9_isolation(tmp_path, monkeypatch, http_cache_names):
    for key in KEYS:
        monkeypatch.delenv(key, raising=False)
    original_connect, original_connect_ex = socket.socket.connect, socket.socket.connect_ex

    def connect(sock, address, *args):
        if sock.family in INET:
            raise NetworkBlocked(f"network access is blocked in v9 tests: {address}")
        return original_connect(sock, address, *args)

    def connect_ex(sock, address, *args):
        if sock.family in INET:
            raise NetworkBlocked(f"network access is blocked in v9 tests: {address}")
        return original_connect_ex(sock, address, *args)

    monkeypatch.setattr(socket.socket, "connect", connect)
    monkeypatch.setattr(socket.socket, "connect_ex", connect_ex)
    # create_connection resolves names before socket.connect. Block DNS too, so isolation is deterministic
    # without network access and never leaks a DNS lookup from an allegedly offline test.
    def getaddrinfo(*args, **kwargs):
        raise NetworkBlocked(f"network access is blocked in v9 tests: DNS {args[:2]}")

    monkeypatch.setattr(socket, "getaddrinfo", getaddrinfo)
    root = tmp_path / "isolated"
    http = root / "cache" / "http"
    http.mkdir(parents=True)
    for name in http_cache_names:
        (http / name).symlink_to(REPO / "cache" / "http" / name)
    cfg = copy.deepcopy(dict(load_config()))
    _redirect(cfg, root)
    cfg["tools"] = {**cfg["tools"], "http_cache": str(root / "cache" / "http")}   # model cache: root/cache/llm
    path = root / "config.yaml"
    path.write_text(yaml.safe_dump(cfg, sort_keys=False))
    monkeypatch.setenv("V2M_CONFIG", str(path))
    monkeypatch.chdir(tmp_path)
    load_config.cache_clear()
    yield root
    load_config.cache_clear()


@pytest.fixture
def v9_cfg(v9_isolation) -> Config:
    """The isolated configuration (writable paths under the test's temporary folder)."""
    return load_config()


@pytest.fixture
def force_cache_miss(monkeypatch):
    """An explicit absent response, independent of new live entries in the shared developer cache."""
    from variant2mechanism.context.http import HttpResult

    def force(http, url_fragment, body_fragment=None):
        original = http.request

        def request(method, url, *args, **kwargs):
            body = kwargs.get("json_body", args[0] if args else None)
            if url_fragment in url and (body_fragment is None or body_fragment in json.dumps(body)):
                return HttpResult(False, None, None, url, "fixture", error=f"offline and not cached: {method} {url}")
            return original(method, url, *args, **kwargs)

        monkeypatch.setattr(http, "request", request)

    return force
