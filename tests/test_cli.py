import pytest

from variant2mechanism.cli import build_parser


def test_parser_accepts_documented_commands():
    p = build_parser()
    assert p.parse_args(["run", "--case", "tert_c228t", "--config", "full"]).case == "tert_c228t"
    assert p.parse_args(["eval", "--pilot"]).pilot
    grid = p.parse_args(["eval", "--grid", "named", "--configs", "single", "no_qbic", "--concurrency", "1"])
    assert grid.configs == ["single", "no_qbic"] and grid.concurrency == 1
    assert p.parse_args(["qbic", "import", "20261025T091500Z-3f9a1c"]).run_id.endswith("3f9a1c")


def test_parser_rejects_unknown_config():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["run", "--case", "x", "--config", "grid"])


def test_eval_grid_runs_each_seed_on_the_chosen_cases(monkeypatch):
    from variant2mechanism import cli
    from variant2mechanism.evaluation import runner
    seen = []

    def fake_grid(cases, configs, masked, seed, cfg, concurrency):
        seen.append((cases, configs, masked, seed))
        return [{"case_id": c, "config": configs[0], "status": "ok"} for c in cases]
    monkeypatch.setattr(runner, "run_grid", fake_grid)
    argv = ["eval", "--grid", "masked", "--configs", "full", "--cases", "rs6983267", "tert_c228t", "--seeds", "0", "2"]
    assert cli.main(argv) == 0
    assert seen == [(["tert_c228t", "rs6983267"], ["full"], True, 0), (["tert_c228t", "rs6983267"], ["full"], True, 2)]
    assert cli.main(["eval", "--grid", "masked", "--cases", "rs0"]) == 2               # not a gold-set case


def test_eval_grid_stops_seeds_at_the_budget(monkeypatch):
    from variant2mechanism import cli
    from variant2mechanism.evaluation import runner
    seen = []
    monkeypatch.setattr(runner, "run_grid", lambda cases, configs, masked, seed, cfg, concurrency:
                        seen.append(seed) or [{"case_id": cases[0], "status": "budget"}])
    assert cli.main(["eval", "--grid", "named", "--cases", "rs6983267", "--seeds", "0", "1", "2"]) == 0
    assert seen == [0]


def test_the_default_profile_is_release_with_luna_and_its_own_folders():
    from variant2mechanism.config import load_config, profile_config
    cfg = profile_config()
    assert {cfg["llm"][r] for r in ("generator", "critic", "summariser")} == {"openai/gpt-6-luna"}
    assert cfg["budget_usd"]["dev"] > 0 and cfg["budget_usd"]["state_file"] == "state/budget_release.json"
    saved = load_config()["v8"]["runs_dir"]                  # the saved grid that `v2m replay` reads
    assert saved == "runs/eval_v8_luna" and saved not in (cfg["v8"]["runs_dir"], cfg["v8"]["dev_dir"])
    assert profile_config("none") is load_config()
    assert profile_config("luna_v8")["v8"]["runs_dir"] == saved


def test_a_single_v8_run_goes_to_the_dev_folder(monkeypatch):
    from variant2mechanism import cli
    from variant2mechanism.v8 import run as v8run
    seen = {}

    def fake(spec, **kw):
        seen.update(kw)
        return {"case_id": spec.case_id, "arm": kw["arm"], "cost_usd": 0.0, "seconds": 0.0, "model_calls": 0}
    monkeypatch.setattr(v8run, "run_case8", fake)
    assert cli.main(["v8", "run", "--case", "rs339331", "--code-only"]) == 0
    assert str(seen["run_dir"]).endswith("runs/dev_v8_release/code/full_given/0/rs339331") and seen["phase"] == "dev"
    assert cli.main(["v8", "run", "--case", "rs339331", "--profile", "luna_v8", "--repeats", "2"]) == 0
    assert str(seen["run_dir"]).endswith("runs/dev_v8_luna/full_given/2/rs339331") and seen["seed"] == 2
