"""Schemas, ledger, model client, budget guard, investigate loop, citations, masking and an offline run."""

import json
import re
import threading
from pathlib import Path

import pytest
from fake_llm import NULL, PLANS, FakeTransport, chain, default_chains, message, text

from variant2mechanism.agent import schemas
from variant2mechanism.agent.case import CaseSpec
from variant2mechanism.agent.ledger import Ledger
from variant2mechanism.agent.llm import Budget, BudgetExceeded, LLMClient, LLMError, Refused, strict_schema
from variant2mechanism.context.base import ToolResult
from variant2mechanism.context.http import Http
from variant2mechanism.qbic.variants import Variant

FIXTURES = Path(__file__).parent / "fixtures" / "http"
RS = CaseSpec("rs6983267", "rs6983267", Variant.make("chr8", 127401060, "G", "T"), "germline",
              "Colorectal cancer (8q24)", "DepMap:ACH-000971 (HCT 116)", "rs6983267")


# -- schemas --------------------------------------------------------------------------------------------------


def _open_objects(s):
    if isinstance(s, dict):
        bad = [s.get("title")] if ("properties" in s and s.get("additionalProperties") is not False) else []
        return bad + [x for v in s.values() for x in _open_objects(v)]
    if isinstance(s, list):
        return [x for v in s for x in _open_objects(v)]
    return []


@pytest.mark.parametrize("model", [schemas.Chains, schemas.CritiqueOut, schemas.Plan, schemas.Revised,
                                   schemas.RevisedRound, schemas.Quotes])
def test_schemas_are_closed(model):
    assert _open_objects(strict_schema(model)) == []


def hyps(chains):
    return [schemas.Hypothesis(**c) for c in chains]


def test_chain_rules_and_normalisation():
    out = schemas.check_chains(hyps(default_chains()))
    assert sum(h.probability for h in out) == pytest.approx(1.0)
    with pytest.raises(schemas.SchemaCheckError, match="exactly one"):
        schemas.check_chains(hyps([chain("H1", "A", "ref", .5), chain("H2", "B", "alt", .5),
                                   chain("H3", "C", "alt", .5)]))
    bad = chain("H1", "A", "ref", .5)
    bad["links"] = bad["links"][:4]
    with pytest.raises(schemas.SchemaCheckError, match="five steps"):
        schemas.check_chains(hyps([bad, chain("H2", "B", "alt", .3), NULL]))
    with pytest.raises(schemas.SchemaCheckError, match="3 to 5"):
        schemas.check_chains(hyps([chain("H1", "A", "ref", .5), NULL]))


# -- ledger ---------------------------------------------------------------------------------------------------


def tr(tool):
    return ToolResult(tool, {}, f"{tool} summary", {"x": 1}, "src", "url", "computational")


def test_every_write_leaves_an_event(tmp_path):
    led = Ledger(tmp_path)
    a = led.add_evidence("gather", tr("variant_annotation"))
    led.add_quote("gather", a, "123", "A sentence.", "u")
    led.add_chains("generate", 0, hyps(default_chains()))
    led.add_grades("critique", 0, "critic", [schemas.LinkGrade(hypothesis_id="H1", step="binding",
                                                               status="weak", reason="r")])
    led.add_checks("critique", [{"tool": "t", "args_json": "{}", "resolves": "H1.gene", "why": "w", "kept": True}])
    actions = [e[1] for e in led.events()]
    assert actions == ["add_evidence", "add_quote", "add_chains", "add_grades", "add_checks"]
    assert [e.id for e in led.evidence()] == ["E01", "E01a"]


@pytest.mark.data
def test_gather_numbering_follows_fixed_order(agent_cfg, tmp_path, monkeypatch):
    """Tools finish in any order; evidence is numbered in the fixed order."""
    import time

    from variant2mechanism.agent.case import RunState
    from variant2mechanism.agent.stages import gather as g
    from variant2mechanism.context.base import Case

    def slow(fn, delay):
        def wrapped(case, *a, **k):
            time.sleep(delay)
            return fn(case, *a, **k)
        return wrapped
    monkeypatch.setattr(g, "variant_annotation", slow(g.variant_annotation, 0.3))
    monkeypatch.setattr(g, "ccre_lookup", lambda case: tr("ccre_lookup"))
    http = Http(FIXTURES, offline=True)
    state = RunState(RS, "no_qbic", False, tmp_path, Ledger(tmp_path), LLMClient(agent_cfg, FakeTransport()),
                     Case(RS.variant, RS.disease, RS.origin, RS.rsid, RS.expression_context, http))
    g.gather(state)
    tools = [(e.id, e.tool) for e in state.ledger.evidence() if e.quote is None]
    names = [t for _, t in tools]
    n_occ = names.count("occupancy")                                  # the element line, then one row per bound TF
    assert names == (["variant_annotation", "nearest_genes", "ccre_lookup"] + ["occupancy"] * n_occ
                     + ["gwas_lookup", "finemap_lookup", "eqtl_lookup", "literature_search"]) and n_occ == 11
    assert [i for i, _ in tools] == [f"E{k:02d}" for k in range(1, len(tools) + 1)]
    lit = tools[-1][0]
    assert any(e.id == f"{lit}a" for e in state.ledger.evidence()) and state.occupancy is not None


# -- model client ---------------------------------------------------------------------------------------------


def test_validation_error_retries_once(agent_cfg):
    replies = [message("{not json"), message(text({"quotes": []}))]
    calls = []
    llm = LLMClient(agent_cfg, transport=lambda p: (calls.append(p), replies.pop(0))[1])
    res = llm.call("summariser", "t", "s", [{"role": "user", "content": "hi"}], output_model=schemas.Quotes)
    assert res.parsed.quotes == [] and len(calls) == 2 and "failed validation" in json.dumps(calls[1]["messages"])
    bad = [message("{}")] * 2
    with pytest.raises(LLMError, match="twice"):
        LLMClient(agent_cfg, transport=lambda p: bad.pop(0)).call(
            "summariser", "t2", "s", [{"role": "user", "content": "x"}], output_model=schemas.Quotes)


def test_max_tokens_retries_with_double(agent_cfg):
    seen = []

    def t(p):
        seen.append(p["max_tokens"])
        return message(text({"quotes": []}), "length" if len(seen) == 1 else "stop")
    LLMClient(agent_cfg, transport=t).call("summariser", "t", "s", [{"role": "user", "content": "x"}],
                                           output_model=schemas.Quotes)
    assert seen == [4000, 8000]


def test_refusal_fails_the_stage(agent_cfg):
    with pytest.raises(Refused):
        LLMClient(agent_cfg, transport=lambda p: message(None, "content_filter")).call(
            "critic", "critique", "s", [{"role": "user", "content": "x"}])


def test_cached_call_is_free(agent_cfg):
    n = []
    llm = LLMClient(agent_cfg, transport=lambda p: (n.append(1), message(text({"quotes": []})))[1])
    a = llm.call("summariser", "t", "s", [{"role": "user", "content": "same"}], output_model=schemas.Quotes)
    b = LLMClient(agent_cfg, transport=lambda p: 1 / 0).call(
        "summariser", "t", "s", [{"role": "user", "content": "same"}], output_model=schemas.Quotes)
    assert a.cost > 0 and b.cached and b.cost == 0 and len(n) == 1


def test_budget_refuses_before_sending(agent_cfg, tmp_path):
    budget = Budget(tmp_path / "b.json", {"dev": 0.01})
    sent = []
    llm = LLMClient(agent_cfg, transport=lambda p: sent.append(p), budget=budget)
    with pytest.raises(BudgetExceeded):
        llm.call("generator", "generate", "s", [{"role": "user", "content": "x"}])   # 32k tokens at $1.20/M > $0.01
    assert sent == []


def test_budget_holds_with_four_concurrent_callers(tmp_path):
    budget = Budget(tmp_path / "b.json", {"dev": 1.0})
    ok, refused = [], []
    barrier = threading.Barrier(4)

    def worker():
        barrier.wait()
        try:
            rid = budget.reserve("dev", 0.4)
            ok.append(rid)
        except BudgetExceeded:
            refused.append(1)
    ts = [threading.Thread(target=worker) for _ in range(4)]
    [t.start() for t in ts]
    [t.join() for t in ts]
    assert len(ok) == 2 and len(refused) == 2
    for rid in ok:
        budget.settle("dev", rid, 0.4)
    assert budget.spent("dev") == pytest.approx(0.8)


# -- investigate, citations, masking: offline runs ------------------------------------------------------------


def run(agent_cfg, tmp_path, config="no_qbic", masked=False, transport=None, spec=RS):
    from variant2mechanism.agent.run import run_case
    t = transport or FakeTransport()
    report = run_case(spec, config, masked=masked, cfg=agent_cfg, transport=t, http=Http(FIXTURES, offline=True),
                      run_dir=tmp_path / "run")
    return report, t


def schema_title(params):
    return ((params.get("response_format") or {}).get("json_schema") or {}).get("schema", {}).get("title")


@pytest.mark.data
def test_rounds_plan_act_and_remember(agent_cfg, tmp_path):
    t = FakeTransport(revise_probs=[[0.2, 0.6, 0.2], [0.7, 0.1, 0.2]])     # the top chain changes each round
    report, _ = run(agent_cfg, tmp_path, transport=t)
    calls = report["investigate_calls"]
    assert [(c["round"], c["tool"], c["status"]) for c in calls] == [
        (1, "chip_peaks", "run"), (1, "eqtl_lookup", "run"), (2, "gene_disease", "run"),
        (2, "chip_peaks", "repeat"), (2, "nope", "invalid: unknown tool nope")]
    assert all(c["expected"] for c in calls) and re.fullmatch(r"E\d+", calls[0]["evidence_id"])
    assert [r["round"] for r in report["rounds"]] == [1, 2]
    assert report["stop_reason"] == "round 3: no new call to run (Nothing left could change a grade.)"
    plans = [c for c in t.calls if schema_title(c) == "Plan"]
    assert len(plans) == 3
    memory = plans[2]["messages"][1]["content"].split("Calls already made:")[1]
    assert "round 1: chip_peaks(" in memory and "round 2: gene_disease(" in memory   # carried between rounds
    revisions = [c for c in t.calls if schema_title(c) == "RevisedRound"]
    assert "expected: a TCF7L2 peak in HCT116 supports H1" in revisions[0]["messages"][1]["content"]
    assert report["rounds"][0]["check_results"][0]["as_expected"] == "yes"
    assert report["rounds"][1]["max_probability_change"] == pytest.approx(0.5)
    led = [e["tool"] for e in report["evidence"] if e["tool"] in ("chip_peaks", "eqtl_lookup", "gene_disease")]
    assert sorted(led) == ["chip_peaks", "eqtl_lookup", "eqtl_lookup", "gene_disease"]   # the repeat never ran
    md = (tmp_path / "run" / "report.md").read_text()
    assert "## Refinement rounds" in md and "not run: repeat" in md


@pytest.mark.data
def test_rounds_stop_when_the_answer_holds(agent_cfg, tmp_path):
    plans = [PLANS[0], [("gene_disease", {"gene": "MYC"}, "H1.phenotype", "MYC supports H1")], [PLANS[1][0]]]
    t = FakeTransport(plans=plans, revise_probs=[[0.2, 0.6, 0.2], [0.25, 0.55, 0.2]])
    report, _ = run(agent_cfg, tmp_path, transport=t)
    assert [r["round"] for r in report["rounds"]] == [1, 2]                 # H2 led after round 1 and still does
    assert report["stop_reason"] == "round 2 left the top chain and the grades of its links unchanged"


@pytest.mark.data
def test_not_tested_is_not_news(agent_cfg, tmp_path):
    """ENCODE never assayed HOXB13 in LNCaP or TFAP2A at all: those answers do not use up a call, and a round of
    nothing else ends the loop."""
    none_here = ("chip_peaks", {"tf": "HOXB13", "biosample": "LNCaP clone FGC"}, "H1.binding", "a HOXB13 peak")
    plans = [[none_here, PLANS[0][0], PLANS[0][1], PLANS[1][0]],
             [("chip_peaks", {"tf": "TFAP2A"}, "H2.binding", "a TFAP2A peak")]]
    t = FakeTransport(plans=plans, revise_probs=[[0.2, 0.6, 0.2]])
    report, _ = run(agent_cfg, tmp_path, transport=t)
    assert [(c["round"], c["status"]) for c in report["investigate_calls"]] == [
        (1, "not tested"), (1, "run"), (1, "run"), (1, "run"), (2, "not tested")]
    assert len(report["rounds"]) == 1 and report["stop_reason"] == "round 2: its calls brought no new information"
    ev = {e["id"]: e for e in report["evidence"]}
    assert "for or against" in ev[report["investigate_calls"][0]["evidence_id"]]["summary"]


@pytest.mark.data
def test_rounds_stop_at_the_limit(agent_cfg, tmp_path):
    plans = [[c] for c in PLANS[0]] + [[PLANS[1][0]], [PLANS[1][0]]]
    t = FakeTransport(plans=plans, revise_probs=[[0.2, 0.6, 0.2], [0.6, 0.2, 0.2], [0.2, 0.6, 0.2]])
    report, _ = run(agent_cfg, tmp_path, transport=t)
    assert len(report["rounds"]) == 3 and report["stop_reason"] == "round limit (3)"
    assert sum(c["run"] for c in report["investigate_calls"]) == 3


@pytest.mark.data
def test_offline_no_qbic_run_and_report(agent_cfg, tmp_path):
    report, _ = run(agent_cfg, tmp_path)
    run_dir = tmp_path / "run"
    assert (run_dir / "report.md").exists() and (run_dir / "ledger.sqlite").exists()
    assert len((run_dir / "trace.jsonl").read_text().splitlines()) >= 6
    assert [c["rank"] for c in report["chains"]] == [1, 2, 3] and report["chains"][0]["tf"] == "TCF7L2"
    assert sum(c["probability"] for c in report["chains"]) == pytest.approx(1.0)
    assert report["checks"][0]["tool"] == "chip_peaks" and len(report["checks"]) == 1   # bad tool dropped
    phen = report["chains"][0]["links"][-1]
    assert phen["evidence_ids"] == [] and phen["status"] == "missing"
    assert any(f["flag"] == "no_citation" for f in report["flags"])


@pytest.mark.data
def test_citation_checks_catch_problems(agent_cfg, tmp_path):
    c1 = chain("H1", "ARID5B", "ref", 0.5, ev="E99")       # E99 does not exist
    c2 = chain("H2", "LEF1", "ref", 0.3)
    report, _ = run(agent_cfg, tmp_path, transport=FakeTransport(chains=[c1, c2, NULL], plans=[]))
    flags = {f["flag"] for f in report["flags"]}
    assert {"unknown_evidence_id", "failed_citation"} <= flags and "coverage_misstated" not in flags
    assert all("qbic_coverage" not in c for c in report["chains"])            # code fills coverage_status instead
    assert {c["coverage_status"] for c in report["chains"] if not c["is_null"]} == {"not_in_coverage", "own_model"}
    h1 = next(c for c in report["chains"] if c["id"] == "H1")
    assert h1["coverage_status"] == "not_in_coverage" and h1["links"][0]["status"] == "weak"


@pytest.mark.data
def test_edited_quote_rejected_and_coverage_violation(agent_cfg, tmp_path):
    from variant2mechanism.agent.stages.citations import citation_check, evidence_checks
    report, _ = run(agent_cfg, tmp_path, transport=FakeTransport(quote_from_abstract=False, plans=[]))
    assert any(f["flag"] == "quote_rejected" for f in report["flags"])
    # now an edited quote already in a ledger, and a not-in-coverage TF citing QBiC-SELEX evidence
    from variant2mechanism.agent.case import RunState
    led = Ledger(tmp_path / "run2")
    lit = led.add_evidence("gather", ToolResult("literature_search", {}, "s",
                                                [{"pmid": "1", "abstract": "The real sentence here."}], "EPMC", "u",
                                                "literature"))
    led.add_quote("gather", lit, "1", "The edited sentence here.", "u")
    q = led.add_evidence("screen", ToolResult("qbic_screen", {}, "s", {}, "QBiC", "u", "computational"))
    state = RunState(RS, "full", False, tmp_path / "run2", led, None, None)
    assert evidence_checks(state)["E01a"][0] is False
    own = led.add_evidence("investigate", ToolResult("qbic_tf_detail", {"tf": "ARID5B"}, "not_in_coverage", {},
                                                     "QBiC", "u", "computational"))
    honest = chain("H1", "ARID5B", "ref", 0.5, ev=own.id)
    state_h = RunState(RS, "full", False, tmp_path / "run2", led, None, None)
    state_h.revised = schemas.Revised(hypotheses=hyps([honest, chain("H2", "LEF1", "ref", .3),
                                                       NULL]), matrix=[], next_experiment="x")
    state_h.grades1 = []
    citation_check(state_h)          # citing its own lookup ("not in coverage") is honest, not a violation
    assert not any(f["flag"] == "coverage_violation" for f in state_h.flags)
    c = chain("H1", "ARID5B", "ref", 0.5, ev=q.id)
    state.revised = schemas.Revised(hypotheses=hyps([c, chain("H2", "LEF1", "ref", .3), NULL]),
                                    matrix=[], next_experiment="x")
    state.grades1 = []
    citation_check(state)
    assert any(f["flag"] == "coverage_violation" for f in state.flags)


@pytest.mark.data
def test_masked_prompts_hide_ids(agent_cfg, tmp_path):
    report, t = run(agent_cfg, tmp_path, masked=True, transport=FakeTransport(plans=[]))
    # the masked literature query is not in the fixtures, so that tool fails offline and the report says so
    assert any(f["flag"] == "tool_failed" and "literature_search" in f["detail"] for f in report["flags"])
    for call in t.calls:
        blob = json.dumps(call["messages"])
        assert not re.search(r"rs\d+", blob), "an rsID reached a masked prompt"
        assert "rs6983267" not in blob and "(8q24)" not in blob
