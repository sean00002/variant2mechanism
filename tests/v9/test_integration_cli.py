"""`v2m v9 ...` and config.yaml's v9 block (SPEC 12, 13.9, 13.10, 13.16): the commands run offline end to end.

Nothing here reaches the network or a provider: the synthetic fixture answers with its scripts, and the other runs
use cache-only mode (Http9 offline, a model transport that refuses to send). The autouse isolation in conftest.py
blocks sockets and keeps every write in the test's temporary folder.
"""

import json
import socket
from pathlib import Path

import pytest
import yaml

from variant2mechanism import cli
from variant2mechanism.config import REPO, Config, ConfigError, load_config, profile_config
from variant2mechanism.v9 import commands
from variant2mechanism.v9.bundle import BUNDLE_FILES, load_bundle
from variant2mechanism.v9.investigate import EngineLimits
from variant2mechanism.v9.report import report_data
from variant2mechanism.v9.roles import GUARD, model_call_limits, role_keys
from variant2mechanism.v9.tools import REGISTRY

DEV_VARIANT = "chr2:60490908:T>G"         # rs1427407, the development case (not in the gold set)
LIMITS = {"max_sketches": 8, "max_active": 3, "max_regenerations": 1,
          "max_new_hypotheses_per_plan": 2, "max_additional_hypotheses": 4, "reserve_audit_calls": 4,
          "max_model_calls": 24, "call_guard": 4,
          "reserve_model_calls": 2, "max_tool_calls": 24, "fulltext_soft": 5, "fulltext_hard": 8,
          "http_requests": 150, "wall_seconds": 1200}


def v2m(capsys, *argv: str) -> tuple[int, str, str]:
    code = cli.main([str(a) for a in argv])
    out = capsys.readouterr()
    return code, out.out, out.err


# --- config.yaml -----------------------------------------------------------------------------------------------------

def test_the_v9_block_loads_and_merges_with_the_release_profile():
    saved = load_config(str(REPO / "config.yaml"))            # the file itself (the tests' copy redirects folders)
    v9 = saved["v9"]
    assert v9["limits"] == LIMITS and v9["runs_dir"] == "runs/dev_v9_release"
    assert v9["roles"] == {"coordinator": "generator", "computational_investigator": "generator",
                           "literature_investigator": "generator", "critic": "critic", "extraction": "summariser"}
    assert v9["literature"] == {"max_results": 10, "read_chars": 14000, "passage_chars": 600}
    assert v9["screen_api_key_env"] == "V2M_SCREEN_API_KEY"
    release = profile_config(None, cfg=saved)                  # default_profile: release
    assert release["v9"]["runs_dir"] == "runs/dev_v9_release" and release["v9"]["limits"] == LIMITS
    assert release["v9"]["tool_allowlist"] == v9["tool_allowlist"]
    assert {release["llm"][k] for k in ("generator", "critic", "summariser")} == {"openai/gpt-6-luna"}
    assert profile_config("none", cfg=saved)["v9"] == v9
    # what the modules read from the merged config
    assert EngineLimits.from_config(release) == EngineLimits(**{k: v for k, v in LIMITS.items()
                                                                if k in EngineLimits.model_fields})
    assert model_call_limits(release) == (24, 2) and role_keys(release) == v9["roles"]


def test_only_the_v9_block_and_the_release_entry_were_added():
    """Every other value of config.yaml is as it was: the v9 block is additive."""
    raw = yaml.safe_load((REPO / "config.yaml").read_text())
    release = raw["profiles"]["release"]
    assert release["v9"] == {"runs_dir": "runs/dev_v9_release"}
    assert release["v8"] == {"runs_dir": "runs/eval_v8_release", "dev_dir": "runs/dev_v8_release"}
    assert raw["v8"]["runs_dir"] == "runs/eval_v8_luna" and raw["default_profile"] == "release"
    assert release["budget_usd"]["dev"] == 5.0 and release["budget_usd"]["eval"] == 0.0


def test_the_tests_config_keeps_v9_folders_in_the_temporary_folder(v9_isolation):
    cfg = profile_config()
    assert str(cfg.path("v9", "runs_dir")).startswith(str(v9_isolation))


def test_the_allowlist_names_every_registered_tool_and_nothing_else():
    commands.register_tools()
    assert sorted(commands.allowlist(load_config())) == sorted(REGISTRY.names())
    commands.check_config(profile_config())                      # the shipped block passes its own check


@pytest.mark.parametrize("change, message", [
    (("limits", "call_guard", 3), "call_guard is 3"),
    (("literature", "read_chars", 9000), "read_chars is 9000"),
    (("literature", "pages", 2), "not a setting of the literature route"),
    (("tool_allowlist", None, ["variant_annotation", "no_such_tool"]), "do not exist: no_such_tool"),
])
def test_a_v9_block_claiming_what_the_code_does_not_do_is_refused(change, message):
    section, key, value = change
    v9 = json.loads(json.dumps(load_config()["v9"]))
    if key is None:
        v9[section] = value
    else:
        v9[section][key] = value
    with pytest.raises(ConfigError, match=message):
        commands.check_config(Config({**load_config(), "v9": v9}))


def test_the_call_guard_in_config_is_the_code_s():
    assert load_config()["v9"]["limits"]["call_guard"] == GUARD


# --- the factory -------------------------------------------------------------------------------------------------------

def test_the_factory_wires_each_mode_to_its_own_sources(tmp_path):
    """Built only, never run: live sends through agent/'s own transport on the profile's dev budget; cache-only is
    offline with a transport that refuses and a budget in the run folder; a fixture keeps everything in its folder."""
    from variant2mechanism.v9.fixtures import FixtureToolRunner, load_fixture
    from variant2mechanism.v9.replay import ReplayMiss
    cfg = profile_config()
    live = commands.wire(cfg, "live", tmp_path / "live")
    assert live.http.offline is False and live.runner.mode == "live" and live.client._transport is None
    assert live.client.budget.path == cfg.path("budget_usd", "state_file")
    assert live.client.cache_dir == cfg.path("tools", "http_cache").parent / "llm"
    assert live.runner.allowed_tools == sorted(cfg["v9"]["tool_allowlist"])
    assert live.runner.limits == EngineLimits.from_config(cfg).tool_limits()
    assert live.roles.max_calls == 24 and live.roles.reserve == 2 and live.facts.__name__ == "collect_facts"
    offline = commands.wire(cfg, "cache_only", tmp_path / "offline")
    assert offline.http.offline is True and offline.client.budget.path == tmp_path / "offline" / "budget.json"
    with pytest.raises(ReplayMiss):
        offline.client.transport({"model": "m"})
    evidence = commands.wire(cfg, "cache_only", tmp_path / "evidence", models=False)
    assert evidence.client is None and evidence.roles is None
    with pytest.raises(ValueError, match="no model client"):
        evidence.engine()
    fixture = commands.wire(cfg, "fixture", tmp_path / "fixture", fixture=load_fixture("synthetic_repair"))
    assert isinstance(fixture.runner, FixtureToolRunner) and fixture.http is None
    assert fixture.client.cache_dir == tmp_path / "fixture" / "llm"
    assert fixture.client.budget.path == tmp_path / "fixture" / "budget.json"
    assert not any(p.exists() for p in (tmp_path / "live", tmp_path / "offline", tmp_path / "fixture"))


# --- the parser --------------------------------------------------------------------------------------------------------

def test_the_parser_knows_every_v9_command():
    p = cli.build_parser()
    run = p.parse_args(["v9", "run", "--variant", DEV_VARIANT, "--disease", "a", "--disease", "b", "--context", "c",
                        "--mode", "cache-only"])
    assert (run.v9_command, run.mode, run.disease, run.context, run.origin) == ("run", "cache-only", ["a", "b"],
                                                                                ["c"], "unknown")
    assert p.parse_args(["v9", "evidence", "--variant", "rs1427407", "--origin", "germline"]).mode == "live"
    filled = p.parse_args(["v9", "fill", "--variant", DEV_VARIANT, "--context", "K562", "--mode", "cache-only"])
    assert (filled.v9_command, filled.context, filled.disease, filled.mode) == ("fill", ["K562"], [], "cache-only")
    assert p.parse_args(["v9", "report", "--run", "r", "--out", "o"]).out == "o"
    assert p.parse_args(["v9", "replay", "r"]).run_dir == "r"
    assert p.parse_args(["v9", "fixture", "synthetic", "--out", "o"]).fixture == "synthetic"
    assert p.parse_args(["v9", "export", "--run", "r", "--out", "o"]).run == "r"
    assert p.parse_args(["v9", "audit", "--run", "r", "--case", "c"]).case == "c"
    assert p.parse_args(["v9", "eval", "--suite", "m", "--budget-usd", "1.5"]).budget_usd == 1.5
    for argv in (["v9"], ["v9", "run"], ["v9", "run", "--variant", "x", "--mode", "offline"],
                 ["v9", "fixture", "synthetic"]):
        with pytest.raises(SystemExit):
            p.parse_args(argv)


# --- the fixture command -------------------------------------------------------------------------------------------------

def test_the_synthetic_fixture_runs_into_a_new_folder_and_refuses_an_existing_one(tmp_path, capsys, v9_cfg):
    out = tmp_path / "syn"
    code, text, _ = v2m(capsys, "v9", "fixture", "synthetic", "--out", out)
    assert code == 0 and "no_supported_explanation" in text
    for name in (*BUNDLE_FILES, "report.html", "report.md"):
        assert (out / name).is_file(), name
    assert sorted(p.name for p in (out / "raw").iterdir()) == ["T1.json", "T2.json", "T3.json"]
    b = load_bundle(out)
    assert b.integrity == () and b.manifest["mode"] == "fixture" and b.graph.case.case_id == "SYN-1"
    assert b.manifest["request"]["fixture"] == "synthetic_repair" and b.manifest["engine"]["replayable"] is True
    assert b.graph.result.outcome == "no_supported_explanation"
    assert "synthetic fixture, not biological evidence" in (out / "report.html").read_text().lower()
    # the scripted replies stay in the run folder, never in the shared model cache or the profile's budget
    assert any((out / "llm").iterdir()) and (out / "budget.json").is_file() and (out / "trace.jsonl").is_file()
    assert not (Path(v9_cfg.path("tools", "http_cache")).parent / "llm").exists()
    assert not profile_config().path("budget_usd", "state_file").exists()
    before = sorted(p.name for p in out.iterdir())
    code, _, err = v2m(capsys, "v9", "fixture", "synthetic", "--out", out)
    assert code == 2 and "already exists" in err and sorted(p.name for p in out.iterdir()) == before


def test_an_unknown_fixture_is_refused(tmp_path, capsys):
    code, _, err = v2m(capsys, "v9", "fixture", "no_such_fixture", "--out", tmp_path / "x")
    assert code == 2 and "synthetic_repair" in err and not (tmp_path / "x").exists()


def test_report_renders_into_a_new_folder_and_never_overwrites(tmp_path, capsys):
    run = tmp_path / "syn"
    assert v2m(capsys, "v9", "fixture", "synthetic", "--out", run)[0] == 0
    code, text, _ = v2m(capsys, "v9", "report", "--run", run, "--out", tmp_path / "again")
    assert code == 0 and (tmp_path / "again" / "report.html").is_file() and "report.md" in text
    assert v2m(capsys, "v9", "report", "--run", run)[0] == 2                     # reports exist in the run folder
    assert v2m(capsys, "v9", "report", "--run", tmp_path / "nothing")[0] == 2


def test_export_makes_a_public_copy_and_refuses_an_existing_folder(tmp_path, capsys):
    run = tmp_path / "syn"
    assert v2m(capsys, "v9", "fixture", "synthetic", "--out", run)[0] == 0
    code, _, _ = v2m(capsys, "v9", "export", "--run", run, "--out", tmp_path / "public")
    assert code == 0 and "public_export" in json.loads((tmp_path / "public" / "manifest.json").read_text())
    assert v2m(capsys, "v9", "export", "--run", run, "--out", tmp_path / "public")[0] == 2


def test_a_public_copy_names_a_fixture_file_without_its_local_path(tmp_path, capsys):
    """A fixture run started from a file records the file's local path (so a replay can find it again); its public
    copy names the file only, in the manifest and both reports, and still identifies it by its sha256."""
    from variant2mechanism.v9.fixtures import FIXTURE_DIR
    local = tmp_path / "private folder" / "my_fixture.json"
    local.parent.mkdir()
    local.write_bytes((FIXTURE_DIR / "synthetic_repair.json").read_bytes())
    run = tmp_path / "run"
    assert v2m(capsys, "v9", "fixture", local, "--out", run)[0] == 0
    saved = load_bundle(run).manifest["request"]
    assert saved["fixture"] == str(local.resolve())                         # the local run keeps the path
    assert v2m(capsys, "v9", "export", "--run", run, "--out", tmp_path / "public")[0] == 0
    public = load_bundle(tmp_path / "public").manifest["request"]
    assert public == {**saved, "fixture": "my_fixture.json"}
    for name in ("manifest.json", "report.html", "report.md"):
        assert "private folder" not in (tmp_path / "public" / name).read_text(encoding="utf-8"), name


# --- the evaluator's commands --------------------------------------------------------------------------------------------

def test_eval_refuses_without_a_budget_and_stops_at_the_unbuilt_runner(tmp_path, capsys):
    code, _, err = v2m(capsys, "v9", "eval", "--suite", tmp_path / "suite.json")
    assert code == 2 and "--budget-usd" in err
    code, _, err = v2m(capsys, "v9", "eval", "--suite", tmp_path / "suite.json", "--budget-usd", "0")
    assert code == 2 and "--budget-usd" in err
    code, _, err = v2m(capsys, "v9", "eval", "--suite", tmp_path / "suite.json", "--budget-usd", "2")
    assert code == 2 and "not built yet" in err


def test_audit_refuses_a_case_it_cannot_score(tmp_path, capsys):
    """The audit's refusals (a case not in the gold specification, a run about another variant, a specification
    whose sources changed) exit 2 and write nothing into the run folder."""
    run = tmp_path / "syn"
    assert v2m(capsys, "v9", "fixture", "synthetic", "--out", run)[0] == 0
    before = sorted(p.name for p in run.iterdir())
    code, _, err = v2m(capsys, "v9", "audit", "--run", run, "--case", "no_such_case")
    assert code == 2 and err.startswith("v9 audit:")
    assert sorted(p.name for p in run.iterdir()) == before


# --- offline runs on the development variant -----------------------------------------------------------------------------

@pytest.fixture
def no_network(monkeypatch) -> list:
    """Every attempted connection, recorded (and still refused)."""
    attempts: list = []

    def refuse(sock, address, *args):
        attempts.append(address)
        raise OSError("network access is blocked in this test")

    monkeypatch.setattr(socket.socket, "connect", refuse)
    monkeypatch.setattr(socket.socket, "connect_ex", refuse)
    return attempts


def test_a_cache_only_run_reaches_no_network_and_stops_at_the_first_uncached_reply(tmp_path, capsys, no_network,
                                                                                    v9_cfg):
    """cache-only: Http9 offline and a model transport that refuses. The proposal's reply is not cached, so the run
    stops with cache_miss (exit 2) without a provider call; everything code collected is kept in the bundle."""
    out = tmp_path / "run"
    code, text, _ = v2m(capsys, "v9", "run", "--variant", DEV_VARIANT, "--mode", "cache-only", "--out", out)
    assert code == 2 and "cache_miss" in text
    assert no_network == []
    b = load_bundle(out)
    r = b.graph.result
    assert (r.outcome, r.stop_reason) == ("input_or_capability_limitation", "cache_miss")
    assert b.manifest["mode"] == "cache_only" and b.metrics["engine"]["http"]["requests_made"] == 0
    assert b.metrics["engine"]["model_calls"] == 0 and b.metrics["engine"]["cost_usd"] == 0
    assert [f["kind"] for f in b.metrics["engine"]["role_failures"]] == ["replay_miss"]
    calls = list(b.graph.tool_calls.values())
    assert [t.tool_name for t in calls][:3] == ["variant_annotation", "ccre_overlap", "qbic_inventory"]
    assert all("blocked" not in t.message.lower() for t in calls)
    # nothing was spent or cached anywhere: the budget state is the run folder's own
    assert json.loads((out / "budget.json").read_text())["dev"]["spent"] == 0.0
    assert not profile_config().path("budget_usd", "state_file").exists()
    llm = Path(v9_cfg.path("tools", "http_cache")).parent / "llm"
    assert not llm.exists() or not any(llm.iterdir())


def test_an_evidence_bundle_is_code_s_facts_alone(tmp_path, capsys, no_network):
    out = tmp_path / "evidence"
    code, text, _ = v2m(capsys, "v9", "evidence", "--variant", DEV_VARIANT, "--mode", "cache-only", "--out", out)
    assert code == 0 and "evidence bundle" in text and no_network == []
    b = load_bundle(out)
    assert b.manifest["engine"] == {} and b.graph.result is None and not b.graph.hypotheses
    assert b.graph.model_usage.calls == 0 and report_data(b)["meta"]["evidence_only"] is True
    tools = [t.tool_name for t in b.graph.tool_calls.values()]
    assert tools[:4] == ["variant_annotation", "ccre_overlap", "qbic_inventory", "gtex_eqtl"]   # collect_facts
    assert {"chip_occupancy", "credible_sets_l2g", "gwas_associations", "screen_online"} <= set(tools[4:])
    assert tools[4:] == sorted(tools[4:]) and len(tools) == len(set(tools))
    assert not {"qbic_tf_detail", "tf_expression", "depmap_context", "civic_lookup"} & set(tools)   # need a name
    assert all(t.requested_by == "code" and t.charged_to == "code" for t in b.graph.tool_calls.values())
    screen = next(t for t in b.graph.tool_calls.values() if t.tool_name == "screen_online")
    assert screen.execution_status == "unavailable"                  # no key in tests: nothing is sent
    assert b.metrics["engine"]["http"]["requests_made"] == 0
    assert v2m(capsys, "v9", "evidence", "--variant", DEV_VARIANT, "--mode", "cache-only", "--out", out)[0] == 2


@pytest.mark.data                    # reads the saved responses and the data/ folder
def test_a_fill_is_the_evidence_bundle_taken_to_a_table_by_code_alone(tmp_path, capsys, no_network):
    from variant2mechanism.v9 import fill, fill_tools
    from variant2mechanism.v9 import table as T
    out = tmp_path / "fill"
    code, text, err = v2m(capsys, "v9", "fill", "--variant", DEV_VARIANT, "--origin", "germline", "--mode",
                          "cache-only", "--out", out)
    assert code == 0 and "0 model call(s)" in text and "table breaks" not in err and no_network == []
    b = load_bundle(out)
    g = b.graph
    assert b.manifest["engine"]["driver"] == fill.DRIVER and b.manifest["engine"]["replayable"] is True
    assert g.model_usage.calls == 0 and not g.hypotheses and g.result.stop_reason == "converged"
    assert all(c.proposed_by == "code" for c in g.claims.values()) and g.claims
    assert all(t.requested_by == "code" for t in g.tool_calls.values())
    tools = {t.tool_name for t in g.tool_calls.values()}
    assert "credible_sets_all" in tools and not {"literature_search", "literature_read"} & tools
    assert tools <= set(fill_tools.registry().names())
    table = T.Table.model_validate_json((out / "table.json").read_text(encoding="utf-8"))
    assert table == T.from_graph(g) and T.check(table, g) == []
    assert all(c.stated == bool(c.graph_claims) for c in table.claims.values())
    assert "The table passes every rule." in (out / "table.md").read_text(encoding="utf-8")
    data = report_data(b)
    assert data["meta"]["evidence_only"] is False and "no model was called" in data["meta"]["hypotheses_note"]
    assert len(data["chain"]["ranked"]["chains"]) <= 8 and b.metrics["engine"]["fill"]["driver"] == fill.DRIVER
    assert v2m(capsys, "v9", "fill", "--variant", DEV_VARIANT, "--mode", "cache-only", "--out", out)[0] == 2


def test_a_somatic_evidence_bundle_leaves_civic_to_fact_collection(tmp_path, capsys, no_network):
    out = tmp_path / "somatic"
    code, _, _ = v2m(capsys, "v9", "evidence", "--variant", DEV_VARIANT, "--origin", "somatic", "--mode",
                     "cache-only", "--out", out)
    assert code == 0
    tools = [t.tool_name for t in load_bundle(out).graph.tool_calls.values()]
    assert tools.count("civic_lookup") == 1 and tools[3] == "civic_lookup" and "gtex_eqtl" in tools[4:]


def test_the_default_run_folder_is_the_request_id_under_runs_dir(tmp_path, capsys, no_network, v9_cfg):
    code, _, _ = v2m(capsys, "v9", "evidence", "--variant", DEV_VARIANT, "--mode", "cache-only", "--request-id",
                     "dev-1")
    assert code == 0 and (profile_config().path("v9", "runs_dir") / "dev-1" / "graph.json").is_file()
    assert v2m(capsys, "v9", "evidence", "--variant", DEV_VARIANT, "--mode", "cache-only", "--request-id",
               "dev-1")[0] == 2                                         # the same request's folder exists


@pytest.mark.parametrize("variant, message", [("chr2:60490908", "chr2:60490908:T>G"),
                                              ("hg19:chr2:60490908:T>G", "GRCh38"),
                                              ("rs999999999999", "")])
def test_a_request_intake_refuses_exits_2_and_leaves_no_folder(tmp_path, capsys, no_network, variant, message):
    out = tmp_path / "run"
    code, _, err = v2m(capsys, "v9", "run", "--variant", variant, "--mode", "cache-only", "--out", out)
    assert code == 2 and err.startswith("v9 run:") and message in err and not out.exists()
    assert no_network == []


@pytest.mark.data
def test_a_reference_mismatch_ends_as_an_input_limitation(tmp_path, capsys, no_network):
    """The stated reference allele is G; GRCh38 (the cached 21-mer) has T: no tool runs, exit 2."""
    out = tmp_path / "evidence"
    code, text, _ = v2m(capsys, "v9", "evidence", "--variant", "chr2:60490908:G>T", "--mode", "cache-only",
                        "--out", out)
    b = load_bundle(out)
    assert code == 2 and "input_invalid" in text
    assert (b.graph.result.outcome, b.graph.result.stop_reason) == ("input_or_capability_limitation", "input_invalid")
    assert not b.graph.tool_calls and report_data(b)["meta"]["evidence_only"] is False
