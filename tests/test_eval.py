"""Gold-set handling (controls, prompt columns), metrics on hand-made reports, and the runner with a fake model."""

import json
from pathlib import Path

import pytest
from fake_llm import NULL, FakeTransport, chain

from variant2mechanism.evaluation.gold import NEVER_IN_PROMPT, PROMPT_COLUMNS, is_control, load_gold, scoring_tf

FIXTURES = Path(__file__).parent / "fixtures" / "http"


def test_controls_and_scoring_tf():
    gold = {r["case_id"]: r for r in load_gold().to_dict("records")}
    controls = [c for c, r in gold.items() if is_control(r)]
    assert set(controls) >= {"rs13078086", "rs11629191", "rs7001688"}
    assert all(scoring_tf(gold[c]) is None for c in controls)
    assert scoring_tf(gold["rs6983267"]) == "TCF7L2" and "rs1427407" not in gold
    assert scoring_tf({"causal_tf": "GATA1, TAL1", "label_class": "tf_mechanism_other"}) == "GATA1"
    assert is_control({"label_class": "control_binding_only", "causal_tf": "X"})
    assert not set(PROMPT_COLUMNS) & set(NEVER_IN_PROMPT)


def test_case_spec_uses_prompt_columns_only():
    from variant2mechanism.agent.case import load_gold_case
    spec = load_gold_case("rs13078086")
    header = spec.header(masked=False)
    row = next(r for r in load_gold().to_dict("records") if r["case_id"] == "rs13078086")
    for col in NEVER_IN_PROMPT:
        if len(row[col]) > 4:
            assert row[col] not in header, col


def label_strings(case_ids):
    rows = [r for r in load_gold().to_dict("records") if r["case_id"] in case_ids]
    # gene symbols can appear in evidence legitimately; check the long free-text label values
    return {(r["case_id"], c): r[c] for r in rows for c in NEVER_IN_PROMPT
            if len(r[c]) > 12 and c not in ("causal_tf", "target_gene", "tf_family")}


@pytest.mark.data
@pytest.mark.parametrize("case_id", ["rs6983267", "rs13078086"])
def test_no_label_notes_or_source_in_any_prompt(agent_cfg, tmp_path, case_id):
    from variant2mechanism.agent.case import load_gold_case
    from variant2mechanism.agent.run import run_case
    from variant2mechanism.context.http import Http
    t = FakeTransport(plans=[])
    run_case(load_gold_case(case_id), "no_qbic", cfg=agent_cfg, transport=t, http=Http(FIXTURES, offline=True),
             run_dir=tmp_path / "run")
    blob = json.dumps([c["messages"] for c in t.calls] + [c.get("system") for c in t.calls])
    for key, value in label_strings({case_id}).items():
        assert value not in blob, f"{key} reached a prompt"


# -- metrics -----------------------------------------------------------------------------------------------------


def report(case_id, chains, flags=()):
    for i, c in enumerate(chains, 1):
        c["rank"] = i
    return {"case_id": case_id, "config": "full", "mode": "named", "seed": 0, "cost_usd": 0.5, "seconds": 120,
            "chains": chains, "flags": [{"flag": f, "detail": d} for f, d in flags], "citation_support": 0.8,
            "investigate_calls": [{"tool": "chip_peaks", "run": True}], "chains_v0": [], "grades_v0": [],
            "grades_final": []}


def gold_row(case_id):
    return next(r for r in load_gold().to_dict("records") if r["case_id"] == case_id)


@pytest.fixture(scope="module")
def reg():
    from variant2mechanism.qbic.registry import get_registry
    return get_registry()


@pytest.mark.data
def test_tcf7l2_matches_but_tcf4_does_not(reg):
    from variant2mechanism.evaluation.metrics import load_direction_labels, score_run
    labels = load_direction_labels()
    good = score_run(report("rs6983267", [chain("H1", "TCF7L2", "ref", .6), chain("H2", "LEF1", "ref", .2), NULL]),
                     gold_row("rs6983267"), labels, reg)
    assert good["top1"] and good["direction_correct"] and good["p_correct"] == 0.6
    assert good["group_recovery"] is True                    # TCF7L2's mapped models are its group
    bad = score_run(report("rs6983267", [chain("H1", "TCF4", "ref", .6), chain("H2", "LEF1", "ref", .2), NULL]),
                    gold_row("rs6983267"), labels, reg)
    assert bad["top1"] is False and bad["correct_rank"] is None and bad["brier"] == 1.0


@pytest.mark.data
def test_not_in_coverage_scoring_and_coverage_honesty(reg):
    from variant2mechanism.evaluation.metrics import load_direction_labels, score_run
    chains = [chain("H1", "ARID5B", "ref", .5), chain("H2", "CUX1", "ref", .3), NULL]
    r = score_run(report("rs1421085", chains), gold_row("rs1421085"), load_direction_labels(), reg)
    assert r["top1"] and r["direction_correct"] and r["coverage_honest"] is True
    bad = report("rs1421085", chains, flags=[("coverage_violation", "H1: ARID5B is not in QBiC-SELEX coverage")])
    assert score_run(bad, gold_row("rs1421085"), None, reg)["coverage_honest"] is False


@pytest.mark.data
def test_control_is_scored_against_the_null(reg):
    from variant2mechanism.evaluation.metrics import score_run
    n = dict(NULL, probability=0.7)
    r = score_run(report("rs13078086", [n, chain("H1", "CTCF", "ref", .2), chain("H2", "SP1", "alt", .1)]),
                  gold_row("rs13078086"), None, reg)
    assert r["control"] and r["null_top1"] and r["overclaim"] == pytest.approx(0.3)
    assert r["brier"] == pytest.approx(0.09) and r["top1"] is None and r["direction_correct"] is None
    r2 = score_run(report("rs13078086", [chain("H1", "CTCF", "ref", .8), dict(NULL, probability=.1),
                                          chain("H2", "SP1", "alt", .1)]), gold_row("rs13078086"), None, reg)
    assert r2["null_top1"] is False and r2["overclaim"] == pytest.approx(0.9)


@pytest.mark.data
def test_summary_keeps_controls_apart(reg):
    import pandas as pd

    from variant2mechanism.evaluation.metrics import score_run, summarise
    rows = [score_run(report("rs6983267", [chain("H1", "TCF7L2", "ref", .6), chain("H2", "LEF1", "ref", .2), NULL]),
                      gold_row("rs6983267"), None, reg),
            score_run(report("rs13078086", [dict(NULL, probability=.7), chain("H1", "CTCF", "ref", .2),
                                            chain("H2", "SP1", "alt", .1)]), gold_row("rs13078086"), None, reg)]
    s = summarise(pd.DataFrame(rows)).iloc[0]
    assert s.n_tf_cases == 1 and s.n_controls == 1 and s.top1 == 1.0 and s.null_top1_controls == 1.0


def excluding(case_id):
    import copy

    from variant2mechanism.config import Config, load_config
    cfg = Config(copy.deepcopy(dict(load_config())))
    cfg["eval"] = {**cfg["eval"], "exclude": {case_id: "test"}}
    return cfg


def test_excluded_case_stays_in_the_gold_set_but_is_not_scored():
    from variant2mechanism.evaluation.gold import scored_cases
    gold = load_gold()
    kept = scored_cases(gold, excluding("rs4784227")).case_id.tolist()
    assert "rs4784227" in gold.case_id.tolist() and "rs4784227" not in kept and len(kept) == len(gold) - 1


@pytest.mark.data
def test_collect_skips_excluded_cases(reg, tmp_path):
    from variant2mechanism.evaluation.gold import scored_cases
    from variant2mechanism.evaluation.metrics import collect
    for case_id, tf in (("rs6983267", "TCF7L2"), ("rs4784227", "FOXA1")):
        d = tmp_path / "full" / "named" / "0" / case_id
        d.mkdir(parents=True)
        (d / "report.json").write_text(json.dumps(report(case_id, [chain("H1", tf, "ref", .6), NULL])))
    gold = scored_cases(load_gold(), excluding("rs4784227"))
    assert collect(tmp_path, reg, gold).case_id.tolist() == ["rs6983267"]


# -- runner ------------------------------------------------------------------------------------------------------


def test_pilot_includes_a_control():
    from variant2mechanism.evaluation.runner import pilot_cases
    cases = pilot_cases(load_gold())
    assert cases[:4] == ["tert_c228t", "rs6983267", "rs4784227", "rs1421085"] and cases[4] == "rs13078086"


@pytest.mark.data
def test_runner_is_resumable(agent_cfg, tmp_path, monkeypatch):
    from variant2mechanism.context import http as http_mod
    from variant2mechanism.evaluation import runner
    agent_cfg["eval"] = {**agent_cfg["eval"], "runs_dir": str(tmp_path / "eval")}
    monkeypatch.setattr(runner, "REPO", Path("/"))
    real_http = http_mod.Http
    monkeypatch.setattr("variant2mechanism.agent.run.Http",
                        lambda *a, **k: real_http(FIXTURES, offline=True))
    first = runner.run_grid(["rs6983267"], ["no_qbic"], cfg=agent_cfg, transport=FakeTransport(plans=[]))
    assert [r["status"] for r in first] == ["ok"]
    again = runner.run_grid(["rs6983267"], ["no_qbic"], cfg=agent_cfg, transport=FakeTransport())
    assert [r["status"] for r in again] == ["skipped (done)"]


@pytest.mark.data
def test_summed_tf_scoring_and_audit(reg):
    from variant2mechanism.evaluation.metrics import load_direction_labels, score_run
    h5 = chain("H5", "TCF7L2", "ref", .22)
    rep = report("rs6983267", [chain("H1", "TCF7L2", "ref", .35), dict(NULL, probability=.30), h5,
                               chain("H4", "ZBTB43", "ref", .13)])
    rep["evidence"] = [{"tool": "literature_search", "summary": "PMID 1: the risk allele enhances TCF4 binding"}]
    rep["investigate_calls"] = [{"tool": "qbic_tf_detail", "args": {"tf": "TCF7L2"}, "run": True}]
    r = score_run(rep, gold_row("rs6983267"), load_direction_labels(), reg)
    assert r["p_correct"] == 0.35 and r["p_tf_sum"] == pytest.approx(0.57) and r["p_tf_dir_sum"] == pytest.approx(0.57)
    assert r["top1_by_tf"] and r["brier_tf_sum"] == pytest.approx(0.43 ** 2)
    assert r["answer_in_evidence"] and r["agent_asked_for_tf"]     # TCF4 is an old name of TCF7L2
