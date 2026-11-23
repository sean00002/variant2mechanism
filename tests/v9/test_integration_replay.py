"""v9 replay (SPEC 8, 13.4): a saved run re-executes offline from its own bundle and the response cache, and the
exit code says whether it reproduced the run (0), differs or cannot be trusted (1), or would need something the saved
run and the caches do not hold (2). `v2m replay` sends a v9 run folder here and leaves v8 runs on their own path.

The bundles are the synthetic fixture (scripted roles) and, offline, the development variant in cache-only mode (an
evidence bundle, and an engine run whose model replies come from a fake transport and are cached in the test's own
response cache). Nothing reaches the network or a provider.
"""

import hashlib
import json
from pathlib import Path

import pytest

from variant2mechanism import cli
from variant2mechanism.v9 import commands
from variant2mechanism.v9 import replay as v8_replay
from variant2mechanism.v9.bundle import load_bundle
from variant2mechanism.v9.fixtures import FIXTURE_DIR
from variant2mechanism.v9.replay9 import replay

DEV_VARIANT = "chr2:60490908:T>G"         # rs1427407, the development case (not in the gold set)


def v2m(capsys, *argv) -> tuple[int, str, str]:
    code = cli.main([str(a) for a in argv])
    out = capsys.readouterr()
    return code, out.out, out.err


def snapshot(folder: Path) -> dict[str, str]:
    """Every file under a folder with its sha256: a replay must leave the saved run exactly as it was."""
    return {str(p.relative_to(folder)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(folder.rglob("*")) if p.is_file()}


def rewrite(run: Path, name: str, text: str) -> None:
    """Change a bundle file and record its new hash in the manifest, as if the run itself had written it."""
    (run / name).write_text(text)
    manifest = json.loads((run / "manifest.json").read_text())
    manifest["files"][name] = hashlib.sha256(text.encode()).hexdigest()
    (run / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")


@pytest.fixture
def synthetic(tmp_path, capsys) -> Path:
    run = tmp_path / "saved" / "syn"
    assert v2m(capsys, "v9", "fixture", "synthetic", "--out", run)[0] == 0
    return run


# --- the synthetic fixture ---------------------------------------------------------------------------------------------

def test_the_synthetic_run_replays_identically(synthetic, tmp_path, capsys):
    before = snapshot(synthetic)
    out = tmp_path / "replay"
    code, text, _ = v2m(capsys, "v9", "replay", synthetic, "--out", out)
    assert code == 0 and "identical" in text and "fixture run" in text
    assert snapshot(synthetic) == before                                   # the saved run is only read
    again = load_bundle(out)
    assert again.integrity == () and again.manifest["replay_of"]["status"] == "identical"
    assert again.graph.result.outcome == "no_supported_explanation" and (out / "report.html").is_file()
    assert v2m(capsys, "v9", "replay", synthetic, "--out", out)[0] == 1     # an existing replay folder is refused


def test_v2m_replay_sends_a_v9_run_folder_to_the_v9_replay(synthetic, tmp_path, capsys):
    code, text, _ = v2m(capsys, "replay", synthetic, "--out", tmp_path / "replay")
    assert code == 0 and "identical" in text and (tmp_path / "replay" / "graph.json").is_file()
    code, text, _ = v2m(capsys, "replay", synthetic, "--render-only", "--out", tmp_path / "rendered")
    assert code == 0 and (tmp_path / "rendered" / "report.html").is_file()
    assert not (tmp_path / "rendered" / "graph.json").exists()             # render-only re-runs nothing


def test_a_tampered_graph_differs(synthetic, tmp_path, capsys):
    graph = json.loads((synthetic / "graph.json").read_text())
    graph["result"]["outcome"] = "leading_explanation"
    rewrite(synthetic, "graph.json", json.dumps(graph, indent=2))
    code, text, _ = v2m(capsys, "v9", "replay", synthetic, "--out", tmp_path / "replay")
    assert code == 1 and "/result/outcome" in text and "difference" in text


def test_a_bundle_file_changed_after_the_run_is_refused(synthetic, tmp_path, capsys):
    metrics = synthetic / "metrics.json"
    metrics.write_text(metrics.read_text().replace('"metrics_format": 1', '"metrics_format": 1 '))
    code, text, _ = v2m(capsys, "v9", "replay", synthetic, "--out", tmp_path / "replay")
    assert code == 1 and "changed after it was written" in text and not (tmp_path / "replay").exists()


def test_a_tool_call_the_saved_run_no_longer_holds_is_a_miss(synthetic, tmp_path, capsys):
    lines = (synthetic / "tool_calls.jsonl").read_text().splitlines()
    kept = [x for x in lines if json.loads(x)["tool_name"] != "syn_element_perturbation"]
    assert len(kept) < len(lines)
    rewrite(synthetic, "tool_calls.jsonl", "\n".join(kept) + "\n")
    code, text, _ = v2m(capsys, "v9", "replay", synthetic, "--out", tmp_path / "replay")
    assert code == 2 and "cache miss" in text and "never made" in text
    assert load_bundle(tmp_path / "replay").graph.result.stop_reason == "cache_miss"


def test_a_model_reply_the_fixture_no_longer_scripts_is_a_miss(tmp_path, capsys):
    fixture = json.loads((FIXTURE_DIR / "synthetic_repair.json").read_text())
    path = tmp_path / "my_fixture.json"
    path.write_text(json.dumps(fixture))
    run = tmp_path / "saved"
    assert v2m(capsys, "v9", "fixture", path, "--out", run)[0] == 0
    assert load_bundle(run).manifest["request"]["fixture"] == str(path.resolve())
    fixture["roles"]["critic"] = fixture["roles"]["critic"][:-1]         # the final comparison's reply is gone
    path.write_text(json.dumps(fixture))
    code, text, _ = v2m(capsys, "v9", "replay", run, "--out", tmp_path / "replay")
    assert code == 2 and "cache miss" in text and "fixture file changed" in text
    assert load_bundle(tmp_path / "replay").graph.result.stop_reason == "cache_miss"


def test_a_run_that_says_it_cannot_be_replayed_is_not_re_executed(synthetic, tmp_path, capsys):
    manifest = json.loads((synthetic / "manifest.json").read_text())
    why = "critic final: a reply cut by max_tokens was retried; the cut reply is not cached"
    manifest["engine"].update(replayable=False, not_replayable=[why])
    (synthetic / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    code, text, _ = v2m(capsys, "v9", "replay", synthetic, "--out", tmp_path / "replay")
    assert code == 2 and "not replayable" in text and why in text and not (tmp_path / "replay").exists()


def test_a_replay_never_writes_inside_the_saved_run(synthetic, capsys):
    before = snapshot(synthetic)
    code, text, _ = v2m(capsys, "v9", "replay", synthetic, "--out", synthetic / "replay")
    assert code == 1 and "outside the saved run" in text and snapshot(synthetic) == before


def test_the_replay_result_reports_its_kind_and_counts(synthetic, tmp_path):
    saved = load_bundle(synthetic)
    r = replay(synthetic, tmp_path / "replay")
    assert (r.status, r.code, r.kind) == ("identical", 0, "fixture")
    assert r.model_calls == saved.metrics["engine"]["model_calls"] > 0
    assert r.tool_calls == sum(t.charged_to != "none" for t in saved.graph.tool_calls.values()) > 0
    assert r.written and not r.differences and not r.tool_misses


# --- the v8 path -------------------------------------------------------------------------------------------------------

def test_v2m_replay_on_a_v8_run_folder_still_goes_the_v8_way(tmp_path, capsys, monkeypatch):
    seen = []

    def v8(saved, out, base=None):
        seen.append((Path(saved), Path(out)))
        return v8_replay.Replay(Path(saved), Path(out), status="identical")

    def not_v9(*_args, **_kwargs):
        raise AssertionError("a v8 run folder reached the v9 replay")

    monkeypatch.setattr(v8_replay, "replay", v8)
    monkeypatch.setattr(commands, "replay_folder", not_v9)
    saved = tmp_path / "runs" / "full_given" / "0" / "rs1"
    saved.mkdir(parents=True)
    (saved / "report.json").write_text(json.dumps({"version": "v8"}))
    assert v2m(capsys, "replay", saved, "--out", tmp_path / "out")[0] == 0
    (saved / "manifest.json").write_text(json.dumps({"engine_version": "v8"}))    # not a v9 manifest
    assert v2m(capsys, "replay", saved, "--out", tmp_path / "out2")[0] == 0
    assert seen == [(saved, tmp_path / "out"), (saved, tmp_path / "out2")]


# --- offline bundles of the development variant -------------------------------------------------------------------------

def test_a_code_only_fill_replays_its_lookups_and_fills_the_same_table(tmp_path, capsys):
    saved = tmp_path / "fill"
    assert v2m(capsys, "v9", "fill", "--variant", DEV_VARIANT, "--origin", "germline", "--mode", "cache-only",
               "--out", saved)[0] == 0
    code, text, _ = v2m(capsys, "v9", "replay", saved, "--out", tmp_path / "replayed")
    assert code == 0 and "fill run" in text and "identical" in text and "0 model call(s)" in text
    assert (tmp_path / "replayed" / "table.json").read_text() == (saved / "table.json").read_text()


def test_an_evidence_bundle_replays_its_tool_calls(tmp_path, capsys):
    saved = tmp_path / "evidence"
    assert v2m(capsys, "v9", "evidence", "--variant", DEV_VARIANT, "--mode", "cache-only", "--out", saved)[0] == 0
    code, text, _ = v2m(capsys, "v9", "replay", saved, "--out", tmp_path / "replay")
    assert code == 0 and "evidence run" in text and "0 model call(s)" in text
    assert load_bundle(tmp_path / "replay").manifest["engine"] == {}
    lines = (saved / "tool_calls.jsonl").read_text().splitlines()
    rewrite(saved, "tool_calls.jsonl", "\n".join(lines[1:]) + "\n")          # variant_annotation is gone
    assert v2m(capsys, "v9", "replay", saved, "--out", tmp_path / "replay2")[0] == 2


def fake_replies(body: dict) -> dict:
    """A provider stand-in whose replies never validate: the run ends with engine_error after the proposal and its
    retry, and every reply sits in the response cache like a real one."""
    return {"id": "fake", "model": body.get("model"), "provider": "Fake", "usage": {"prompt_tokens": 1,
                                                                                    "completion_tokens": 1, "cost": 0.0},
            "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": "{}"}}]}


def test_an_engine_run_replays_from_the_response_cache_and_a_lost_reply_is_a_miss(tmp_path, capsys, monkeypatch,
                                                                                    v9_cfg):
    saved = tmp_path / "run"
    with monkeypatch.context() as m:                      # the original run's model is a fake (cached replies)
        m.setattr(commands, "refusing", lambda what: fake_replies)
        code, _, _ = v2m(capsys, "v9", "run", "--variant", DEV_VARIANT, "--mode", "cache-only", "--out", saved)
    b = load_bundle(saved)
    assert code == 1 and b.graph.result.stop_reason == "engine_error"
    assert b.manifest["engine"]["replayable"] is True and b.metrics["engine"]["model_calls"] >= 2
    code, text, _ = v2m(capsys, "v9", "replay", saved, "--out", tmp_path / "replay")
    assert code == 0 and "identical" in text and "engine run" in text
    cache = Path(v9_cfg.path("tools", "http_cache")).parent / "llm"
    replies = sorted(cache.glob("*.json"))
    assert replies
    replies[0].unlink()                                                      # one reply is no longer cached
    code, text, _ = v2m(capsys, "v9", "replay", saved, "--out", tmp_path / "replay2")
    assert code == 2 and "cache miss" in text
    lost = load_bundle(tmp_path / "replay2")
    assert lost.graph.result.stop_reason == "cache_miss" and lost.metrics["engine"]["cache_miss"] is True
