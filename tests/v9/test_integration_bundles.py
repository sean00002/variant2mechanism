"""The demo artefacts and the M1 evidence bundle (the plan's M1 and M3 exits).

- M1: code's fact collection for rs12740374 in cache-only mode (saved HTTP responses and cache/qbic.sqlite only)
  makes an inspectable evidence bundle. Every tool that needs no argument runs, nothing is fetched (anything not saved
  is a cache_miss or unavailable call), the QBiC-SELEX inventory lists every gate-passing model-sharing group in a
  neutral order with its Evidence, and the report renders. Skipped where the caches or data/ are absent.
- M3: demo/v9 displays with no key, network or dataset. Each report.html is self-contained (no script, style, image,
  font or frame from elsewhere; links are fine), a render-only report needs only the folder, and a replay of each
  folder either reproduces the run (exit 0) or exits 2 naming exactly what the folder lacks, here with data/ and the
  HTTP and model caches pointed at nothing, as in a fresh checkout. A public copy without its article text names the
  raw results and the fixture file a replay would need.

The demo folders are only read: every replay and render goes to the test's own folder.
"""

import hashlib
import json
import os
import re
import shutil
from html.parser import HTMLParser
from pathlib import Path

import pytest
import yaml

from variant2mechanism import cli
from variant2mechanism.config import REPO, load_config
from variant2mechanism.v9 import adapters, commands
from variant2mechanism.v9.bundle import BUNDLE_FILES, compare_graph_json, inventory_items, inventory_table, load_bundle
from variant2mechanism.v9.graph import ClaimGraph
from variant2mechanism.v9.report import write_reports
from variant2mechanism.v9.tools import REGISTRY

from .test_integration_round3 import literature_fixture

DEMO = REPO / "demo" / "v9"
SYNTHETIC = DEMO / "synthetic_repair"
EVIDENCE = DEMO / "rs12740374_evidence"
DEMOS = [SYNTHETIC, EVIDENCE]
CASE_VARIANT = "chr1:109274968:G>T"          # rs12740374, by coordinates only
DEMO_LIMIT = 8_000_000                       # bytes: demo/v9 holds bundles and reports, no full texts or caches
LOCAL_PATH = re.compile(r"/Users/|/home/|/private/|/tmp/|/var/folders/|[A-Za-z]:\\\\Users")
FACT_TOOLS = {"variant_annotation", "ccre_overlap", "qbic_inventory", "gtex_eqtl"}


def v2m(capsys, *argv) -> tuple[int, str, str]:
    code = cli.main([str(a) for a in argv])
    out = capsys.readouterr()
    return code, out.out, out.err


def snapshot(folder: Path) -> dict[str, str]:
    return {str(p.relative_to(folder)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(folder.rglob("*")) if p.is_file()}


def needs_demo() -> None:
    if not all((d / "manifest.json").is_file() for d in DEMOS):
        pytest.skip("demo/v9 is not present")


# --- what a report.html loads ----------------------------------------------------------------------------------------

LOADS = {"img": ("src", "srcset"), "iframe": ("src",), "frame": ("src",), "embed": ("src",), "object": ("data",),
         "source": ("src", "srcset"), "video": ("src", "poster"), "audio": ("src",), "track": ("src",),
         "input": ("src",), "image": ("href", "xlink:href"), "use": ("href", "xlink:href"), "link": ("href",)}
REMOTE = re.compile(r"^\s*(?:[a-z][a-z0-9+.-]*:)?//", re.I)
CSS_REMOTE = re.compile(r"url\(\s*['\"]?\s*(?:[a-z][a-z0-9+.-]*:)?//|@import", re.I)
SCRIPT_FETCH = re.compile(r"\b(?:fetch|XMLHttpRequest|importScripts|WebSocket|EventSource|sendBeacon)\s*\(|"
                          r"\bimport\s*\(", re.I)


class Loads(HTMLParser):
    """Every resource a page would fetch by itself: src/href of scripts, styles, images, fonts, frames and media,
    CSS url() and @import (style blocks and attributes), a meta refresh, and network calls in inline scripts. A plain
    link (<a href>) loads nothing and is counted apart."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.found: list[str] = []
        self.links = 0
        self.open: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = {k: v or "" for k, v in attrs}
        self.open.append(tag)
        self.found += [f"<{tag} {k}={a[k]}>" for k in LOADS.get(tag, ()) if a.get(k) and REMOTE.search(a[k])]
        if tag == "link" and a.get("href") and not REMOTE.search(a["href"]) and a["href"].endswith(".css"):
            self.found.append(f"<link href={a['href']}> (a stylesheet beside the page)")
        if tag == "script" and a.get("src"):
            self.found.append(f"<script src={a['src']}>")
        if a.get("style") and CSS_REMOTE.search(a["style"]):
            self.found.append(f"style={a['style']}")
        if tag == "meta" and a.get("http-equiv", "").lower() == "refresh":
            self.found.append(f"<meta refresh {a.get('content')}>")
        if tag == "a" and REMOTE.search(a.get("href", "")):
            self.links += 1

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.open.pop()

    def handle_endtag(self, tag):
        if tag in self.open:
            while self.open.pop() != tag:
                pass

    def handle_data(self, data):
        here = self.open[-1] if self.open else ""
        if here == "style" and CSS_REMOTE.search(data):
            self.found.append(f"<style> {CSS_REMOTE.search(data).group(0)}")
        if here == "script":
            self.found += [f"<script> {m.group(0)}" for m in SCRIPT_FETCH.finditer(data)]


def external_loads(html: str) -> tuple[list[str], int]:
    page = Loads()
    page.feed(html)
    page.close()
    return page.found, page.links


def test_the_load_check_finds_what_a_page_would_fetch():
    found, links = external_loads(
        '<html><head><script src="https://cdn.example/x.js"></script><link rel="stylesheet" href="//fonts.example/f">'
        '<style>body{background:url("https://img.example/b.png")}</style></head><body>'
        '<img src="http://img.example/a.png"><a href="https://pubmed.ncbi.nlm.nih.gov/1/">PMID 1</a>'
        '<div style="background:url(//x.example/y)"></div><script>fetch("https://x.example")</script></body></html>')
    assert len(found) == 6 and links == 1


# --- the demo folders ------------------------------------------------------------------------------------------------

def test_demo_folders_hold_bundles_and_reports_only():
    needs_demo()
    total = sum(p.stat().st_size for p in DEMO.rglob("*") if p.is_file())
    assert total < DEMO_LIMIT, f"demo/v9 holds {total} bytes"
    for folder in DEMOS:
        b = load_bundle(folder)
        assert b.integrity == () and b.evaluation is None
        names = {p.name for p in folder.iterdir()}
        assert {*BUNDLE_FILES, "report.html", "report.md", "raw"} <= names
        assert not names & {"llm", "budget.json", "budget.json.lock", "evaluation.json"}     # no caches or state
        named = {t.raw_result_path for t in b.graph.tool_calls.values() if t.raw_result_path}
        assert {f"raw/{p.name}" for p in (folder / "raw").iterdir()} == named             # nothing unreferenced
        for p in folder.rglob("*"):
            if p.is_file():
                assert not LOCAL_PATH.search(p.read_text(encoding="utf-8", errors="replace")), p
        reads = [t for t in b.graph.tool_calls.values() if t.tool_name == "literature_read" and t.raw_result_path]
        if reads:                          # a demo with literature is a public export: verified passages only
            assert {t.raw_result_path for t in reads} <= set(b.manifest["public_export"]["raw_files_rewritten"])
    assert sum(p.stat().st_size for p in SYNTHETIC.rglob("*") if p.is_file()) < 1_000_000


@pytest.mark.parametrize("folder", DEMOS, ids=lambda p: p.name)
def test_each_demo_report_loads_nothing_from_elsewhere(folder, tmp_path):
    needs_demo()
    found, links = external_loads((folder / "report.html").read_text(encoding="utf-8"))
    assert found == []
    assert links > 0 or folder != EVIDENCE                  # links to sources (PubMed, ENCODE) are fine
    rendered = write_reports(folder, tmp_path / "rendered")     # render-only: the folder alone
    assert [p.name for p in rendered] == ["report.html", "report.md"]
    assert external_loads(rendered[0].read_text(encoding="utf-8"))[0] == []


def fresh_checkout(tmp_path: Path, monkeypatch) -> None:
    """The isolated config with every data/ file, the HTTP cache (and the model cache beside it) and the local QBiC
    paths pointed at a folder that does not exist: what a fresh checkout has (cache/qbic.sqlite, cache/groups.json and
    the gold CSV are tracked, so they stay)."""
    cfg = yaml.safe_load(Path(os.environ["V2M_CONFIG"]).read_text())
    absent = tmp_path / "absent"
    tracked = {"model_list"}
    cfg["data"] = {k: (v if k in tracked or not isinstance(v, str) else str(absent / "data" / k))
                   for k, v in cfg["data"].items()}
    cfg["local"] = {k: (str(absent / "local" / k) if isinstance(v, str) else v) for k, v in cfg["local"].items()}
    cfg["tools"] = {**cfg["tools"], "http_cache": str(absent / "cache" / "http")}
    fresh = tmp_path / "fresh.yaml"
    fresh.write_text(yaml.safe_dump(cfg, sort_keys=False))
    monkeypatch.setenv("V2M_CONFIG", str(fresh))
    load_config.cache_clear()
    assert not Path(load_config().path("data", "hgnc")).exists()


def expected_missing(folder: Path) -> set[str]:
    """What a replay of this folder lacks, by the folder's own record: raw results a public export rewrote or never
    had, and a fixture file that is neither in v9/fixtures nor here."""
    m = json.loads((folder / "manifest.json").read_text())
    export = m.get("public_export") or {}
    lacks = set(export.get("raw_files_rewritten") or []) | set(export.get("raw_files_missing") or [])
    fixture = (m.get("request") or {}).get("fixture")
    if m.get("mode") == "fixture" and fixture and not (re.fullmatch(r"[A-Za-z0-9_]+", fixture) and (
            REPO / "src" / "variant2mechanism" / "v9" / "fixtures" / f"{fixture}.json").is_file()):
        lacks.add(fixture)
    return lacks


def missing_lines(text: str) -> list[str]:
    return [line.removeprefix("  missing: ") for line in text.splitlines() if line.startswith("  missing: ")]


@pytest.mark.parametrize("folder", DEMOS, ids=lambda p: p.name)
def test_each_demo_replays_in_a_fresh_checkout_or_names_what_it_lacks(folder, tmp_path, monkeypatch, capsys):
    needs_demo()
    fresh_checkout(tmp_path, monkeypatch)
    before = snapshot(folder)
    out = tmp_path / "replay"
    code, text, _ = v2m(capsys, "v9", "replay", folder, "--out", out)
    lacks = expected_missing(folder)
    if lacks:
        assert code == 2 and not out.exists(), text
        named = missing_lines(text)
        assert len(named) == len(lacks) and all(any(x in line for line in named) for x in lacks), text
    else:
        again = load_bundle(out)
        original = json.loads((folder / "graph.json").read_text())
        if "hypothesis_families" not in original:
            # Retained pre-scope exports report genuine format/signature differences. Do not rewrite them or
            # weaken the production replay comparator. All other scientific state must still match.
            diffs = compare_graph_json(original, json.loads((out / "graph.json").read_text()))
            allowed = re.compile(r"/(?:claim_refinements|hypothesis_families|hypotheses/H\d+/signature|"
                                 r"events\[\d+\]/details/signature):")
            for diff in diffs:
                signature_reason = bool(re.match(r"/events\[\d+\]/concise_reason:", diff)
                                        and "repeats rejected hypothesis" in diff and "scoped:" in diff)
                assert allowed.match(diff) or signature_reason, diff
            assert code == 1 and again.manifest["replay_of"]["status"] == "different", text
        else:
            assert code == 0 and "identical" in text, text
            assert again.manifest["replay_of"]["status"] == "identical"
        assert (out / "report.html").is_file()
    assert snapshot(folder) == before                                     # the demo is only read


def test_the_synthetic_demo_shows_the_fixture_story():
    """SPEC 11: F1 contradicted in scope, H1 rejected by code at that assessment, F2 flagged (not contradicted), the
    regenerated copy of H1 refused, H2 unresolved, F0 kept; no supported explanation, with the stop recorded."""
    needs_demo()
    b = load_bundle(SYNTHETIC)
    g, r = b.graph, b.graph.result
    assert g.case.case_id.startswith("SYN-") and b.manifest["mode"] == "fixture"
    assert b.manifest["request"]["fixture"] == "synthetic_repair"           # a name in v9/fixtures, not a path
    assert (r.outcome, r.budget_stop) == ("no_supported_explanation", False) and r.stop_reason
    f0, f1, f2 = (next(c for c in g.claims.values() if c.relation == rel) for rel in
                  ("overlaps", "regulates", "contributes_to_trait"))
    assert f1.assessment == "contradicted_in_scope" and f0.assessment == "supported_in_scope"
    assert f2.dependency_flag == "unsupported_due_to_dependency" and f2.assessment != "contradicted_in_scope"
    h1 = next(h for h in g.hypotheses.values() if f1.claim_id in h.required_claim_ids)
    h2 = next(h for h in g.hypotheses.values() if h.origin == "regenerated")
    assert h1.disposition == "rejected" and h1.path_status[f2.claim_id] == "premise_failed"
    order = [e.event_id for e in g.events]
    assess = next(e for e in g.events if e.action == "assess" and e.target_ids == [f1.claim_id]
                  and e.details.get("to") == "contradicted_in_scope")
    reject = next(e for e in g.events if e.action == "reject" and h1.hypothesis_id in e.target_ids)
    assert reject.role == "code" and reject.details["rule"] == "contradicted_required_claim"
    assert order.index(reject.event_id) == order.index(assess.event_id) + 1
    assert any(e.action == "refuse_update" and e.role == "coordinator" and f"rejected hypothesis {h1.hypothesis_id}"
               in e.concise_reason for e in g.events)
    assert [g.claims[c].assessment for c in h2.required_claim_ids] == ["unresolved"]
    stop = next(e for e in g.events if e.action == "stop")
    assert stop.details["stop_reason"] == r.stop_reason and order.index(stop.event_id) < order.index(
        next(e for e in g.events if e.action == "decide").event_id)
    html = (SYNTHETIC / "report.html").read_text(encoding="utf-8")
    assert "synthetic fixture" in html.lower() and "not biological evidence" in html.lower()


# --- the evidence bundle -----------------------------------------------------------------------------------------------

def applicable_tools(graph: ClaimGraph) -> set[str]:
    """The tools `v2m v9 evidence` runs: code's fact collection, then every computational tool that needs no argument
    and covers the variant (commands.evidence_requests)."""
    specs = REGISTRY.specs("computational")
    return FACT_TOOLS | {s.name for s in specs if s.name not in commands.LEFT_TO_FACTS and not s.one_of
                         and not any(p.required for p in s.params.values()) and commands._applies(s, graph.case)}


def check_evidence_bundle(folder: Path) -> None:
    """M1 on a saved evidence bundle of rs12740374 (by coordinates): the tools, the fact records and the inventory."""
    b = load_bundle(folder)
    g = b.graph
    assert b.integrity == () and b.manifest["mode"] == "cache_only" and b.manifest["engine"] == {}
    assert g.result is None and g.hypotheses == {} and g.claims == {}           # evidence only: no agent, no claim
    calls = list(g.tool_calls.values())
    assert {t.tool_name for t in calls} == applicable_tools(g) and len(calls) == len({t.tool_name for t in calls})
    assert all(t.charged_to == "code" for t in calls)
    statuses = {t.tool_name: t.execution_status for t in calls}
    assert set(statuses.values()) <= {"success", "cache_miss", "unavailable", "not_applicable"}, statuses
    assert statuses["screen_online"] == "unavailable"                          # no key here: the local snapshot is used
    assert b.metrics["engine"]["http"]["requests_made"] == 0                   # nothing was fetched
    assert all(t.evidence_ids == [] for t in calls if t.execution_status != "success")
    # the variant's identity, as code's own tools found it
    vep = next(t for t in calls if t.tool_name == "variant_annotation")
    overlap = next(t for t in calls if t.tool_name == "ccre_overlap")
    assert g.variant_aliases == {"rs12740374": vep.tool_call_id}
    assert g.variant_elements == {"EH38E1374646": overlap.tool_call_id}
    # the QBiC-SELEX inventory: every gate-passing group carries Evidence (one item per allele when its gate-passing
    # models disagree), in the neutral order (DNA-binding domain, then group id)
    call = next(t for t in calls if t.tool_name == "qbic_inventory")
    rows = call.observations
    passing = [r for r in rows if r["passes_gate"]]
    assert (len(rows), len(passing)) == (631, 182)
    assert [(r["dbd"].casefold(), r["group_id"]) for r in rows] == sorted((r["dbd"].casefold(), r["group_id"])
                                                                           for r in rows)
    items = inventory_items(g)
    assert set(items) == {r["group_id"] for r in passing}
    assert sum(len(v) for v in items.values()) == len(call.evidence_ids)
    order = [g.evidence[e].data["group_id"] for e in call.evidence_ids]
    assert list(dict.fromkeys(order)) == [r["group_id"] for r in passing]
    for gid, eids in items.items():
        evs = [g.evidence[e] for e in eids]
        assert all(e.about_variants == ["rs12740374", "chr1:109274968 G>T"] for e in evs)
        assert len({e.independence_group for e in evs}) == 1 and evs[0].independence_group.endswith(f":{gid}")
        if len(evs) > 1:
            assert len(evs) == 2 and {e.allele for e in evs} == {"G", "T"} and all(e.data["discordant"] for e in evs)
        else:
            assert not evs[0].data.get("discordant")
    assert adapters.inventory_rows(g) == inventory_table(g)
    by_id = {r["group_id"]: r for r in rows}
    members = {gid: {m["tf"] for m in r["members"]} for gid, r in by_id.items()}
    assert members["G035"] == {"CEBPA", "CEBPB", "CEBPE"} and by_id["G035"]["passes_gate"]
    for tf in ("CEBPD", "CEBPG"):
        own = [gid for gid, tfs in members.items() if tf in tfs]
        assert len(own) == 1 and own[0] != "G035" and members[own[0]] == {tf}, (tf, own)
    for gid in ("G035", *(gid for gid, tfs in members.items() if tfs & {"CEBPD", "CEBPG"})):
        assert by_id[gid]["paralog_stem"] == "CEBP"


def test_the_evidence_demo_is_the_m1_bundle():
    needs_demo()
    check_evidence_bundle(EVIDENCE)
    export = load_bundle(EVIDENCE).manifest["public_export"]
    assert export["source_run"] and export["files_verified"] is True and export["raw_files_missing"] == []


@pytest.mark.data
def test_the_offline_rs12740374_evidence_bundle_renders_and_replays(tmp_path, capsys, http_cache_names):
    if not http_cache_names:
        pytest.skip("the HTTP cache (cache/http) is not present: no offline facts to collect")
    run = tmp_path / "evidence"
    code, text, err = v2m(capsys, "v9", "evidence", "--variant", CASE_VARIANT, "--mode", "cache-only", "--out", run)
    assert code == 0, err
    statuses = {t.tool_name: t.execution_status for t in load_bundle(run).graph.tool_calls.values()}
    if statuses.get("variant_annotation") != "success" or statuses.get("qbic_inventory") != "success":
        pytest.skip(f"the offline facts of rs12740374 are not cached here: {statuses}")
    check_evidence_bundle(run)
    for name in ("report.html", "report.md"):
        assert (run / name).stat().st_size > 0
    assert external_loads((run / "report.html").read_text(encoding="utf-8"))[0] == []
    code, text, _ = v2m(capsys, "v9", "replay", run, "--out", tmp_path / "replay")
    assert code == 0 and "identical" in text and "evidence run" in text


# --- what a replay needs and a folder may lack ---------------------------------------------------------------------------

def test_a_folder_without_a_raw_result_names_it_and_runs_nothing(tmp_path, capsys):
    needs_demo()
    copy = tmp_path / "copy"
    shutil.copytree(SYNTHETIC, copy)
    gone = sorted((copy / "raw").iterdir())[-1]
    gone.unlink()
    code, text, _ = v2m(capsys, "v9", "replay", copy, "--out", tmp_path / "replay")
    assert code == 2 and "not re-executed" in text and not (tmp_path / "replay").exists()
    assert [line.split(":")[0] for line in missing_lines(text)] == [f"raw/{gone.name}"]


def test_a_raw_result_changed_after_the_run_is_refused(tmp_path, capsys):
    needs_demo()
    copy = tmp_path / "copy"
    shutil.copytree(SYNTHETIC, copy)
    changed = sorted((copy / "raw").iterdir())[0]
    changed.write_text(changed.read_text() + " ")
    code, text, _ = v2m(capsys, "v9", "replay", copy, "--out", tmp_path / "replay")
    assert code == 1 and f"raw/{changed.name} changed after the run wrote it" in text
    assert not (tmp_path / "replay").exists()


def test_a_public_copy_without_article_text_names_what_a_replay_lacks(tmp_path, capsys):
    """A fixture run with a literature read, started from a file: its public copy keeps only the verified passages of
    the read and names the fixture by file name, so a replay of the copy runs nothing and names both, while the run
    itself replays identically."""
    source = tmp_path / "fixtures" / "literature_case.json"
    source.parent.mkdir()
    source.write_text(json.dumps(literature_fixture().model_dump(mode="json"), indent=1))
    run, public = tmp_path / "run", tmp_path / "public"
    assert v2m(capsys, "v9", "fixture", source, "--out", run)[0] == 0
    assert v2m(capsys, "v9", "export", "--run", run, "--out", public)[0] == 0
    export = load_bundle(public).manifest["public_export"]
    read = next(t for t in load_bundle(run).graph.tool_calls.values() if t.tool_name == "literature_read")
    assert read.raw_result_path in export["raw_files_rewritten"]
    code, text, _ = v2m(capsys, "v9", "replay", public, "--out", tmp_path / "replay_public")
    assert code == 2 and not (tmp_path / "replay_public").exists()
    named = missing_lines(text)
    assert sorted(line.split(":")[0] for line in named if line.startswith("raw/")) == sorted(
        export["raw_files_rewritten"])
    assert [line for line in named if not line.startswith("raw/")] == [
        "the fixture literature_case.json the run was made from: it is neither in v9/fixtures nor a file here"]
    assert expected_missing(public) == {*export["raw_files_rewritten"], "literature_case.json"}
    code, text, _ = v2m(capsys, "v9", "replay", run, "--out", tmp_path / "replay_run")
    assert code == 0 and "identical" in text
