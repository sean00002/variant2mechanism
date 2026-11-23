"""`v2m replay` (v9/replay.py): the report comparison, the output-folder rule, and (data-marked: they read the local
caches and the saved v8 runs) the guard, a cache miss and the offline re-render."""

import json
import shutil

import pytest

from variant2mechanism.v9.replay import _check_out, differences


def test_differences_ignore_time_and_cost_and_list_new_fields():
    saved = {"seconds": 10, "cost_usd": 0.01, "verdict": {"tf": "mechanism"}, "chains": [{"tf": "HOXB13"}]}
    same = {"seconds": 2, "cost_usd": 0.0, "verdict": {"tf": "mechanism"}, "chains": [{"tf": "HOXB13"}]}
    added: list[str] = []
    assert differences(saved, same | {"repeat": 0}, added=added) == [] and added == ["/repeat"]
    changed = {**same, "verdict": {"tf": "no mechanism"}, "chains": []}
    assert differences(saved, changed) == ['/verdict/tf: "mechanism" -> "no mechanism"',
                                           "/chains: 1 items saved, 0 now"]
    assert differences(saved, {"verdict": {}}) == ["/verdict/tf: missing now", "/chains: missing now"]


def test_replay_never_writes_into_the_saved_run(tmp_path):
    saved = tmp_path / "runs" / "full_given" / "0" / "rs1"
    with pytest.raises(ValueError, match="outside the saved run"):
        _check_out(saved, saved)
    with pytest.raises(ValueError, match="outside the saved run"):
        _check_out(saved, saved / "replay")
    _check_out(saved, tmp_path / "replay")


@pytest.mark.data
def test_guard_replays_match_the_saved_runs(tmp_path):
    """Run before and after every change to v8: the main arm's code-only baselines and three agent runs re-execute
    from the caches and give the saved reports, apart from seconds and cost."""
    from variant2mechanism.v9.replay import guard
    results = guard(out=tmp_path)
    assert len(results) == 18
    bad = [(r.line(), r.differences[:3]) for r in results if r.status != "identical"]
    assert not bad
    assert all(not r.http_misses for r in results)
    assert sum(r.model_calls for r in results) == 14              # 5 + 3 + 6, every one from the cache


@pytest.mark.data
def test_an_uncached_repeat_is_a_miss_and_costs_nothing(tmp_path):
    from variant2mechanism.v9.replay import find_run, replay
    saved = tmp_path / "saved" / "full_given" / "7" / "rs339331"
    saved.mkdir(parents=True)
    rep = json.loads((find_run("rs339331") / "report.json").read_text())
    (saved / "report.json").write_text(json.dumps(rep | {"seed": 7}))      # a repeat never run: no cached calls
    r = replay(saved, tmp_path / "out")
    assert r.status == "miss" and r.code == 2 and "paid model call" in r.message
    budget = json.loads((tmp_path / "out" / "budget.json").read_text())
    assert budget["eval"]["spent"] == 0.0 and not budget["eval"]["reserved"]


@pytest.mark.data
def test_render_only_needs_no_caches_and_is_stable(tmp_path):
    from variant2mechanism.v9.replay import find_run, render
    saved = tmp_path / "saved"
    shutil.copytree(find_run("tert_c228t"), saved, ignore=lambda d, names: [n for n in names if n != "report.json"])
    first = [p.read_text() for p in render(saved, tmp_path / "a")]
    second = [p.read_text() for p in render(saved, tmp_path / "b")]
    assert first == second and len(first) == 2
    assert "tert_c228t" in first[1] and "TERT" in first[0]
