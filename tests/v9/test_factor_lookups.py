"""The factor lookups: what code asks about every TF a binding claim names after the decision, and how the report
lists what came back. TF, gene and context names and every observation are stipulated for the tests."""

import json

from variant2mechanism.v9 import bundle, chain, report
from variant2mechanism.v9.graph import ClaimGraph, EntityRef, GroupRegistry, SymbolResolver
from variant2mechanism.v9.investigate import FACTOR_PURPOSE, Engine, _Run
from variant2mechanism.v9.schemas import ContextScope, RunResult, ToolCall, ToolRequest

from .test_chain_view import binding_assay, eqtl, group
from .test_report_support import HEPG2, VARIANT, claim, dev_case, tf, write_run


class Spec:
    def __init__(self, name: str):
        self.name = name


class Runner:
    """Stands in for a ToolRunner: records every request as a successful call with no observations."""

    def __init__(self, tools: list[str], fail: bool = False):
        self.tools, self.fail, self.requests = tools, fail, []

    def specs(self, route: str) -> list[Spec]:
        return [Spec(name) for name in self.tools]

    def run(self, request: ToolRequest, case, graph: ClaimGraph, role: str) -> ToolCall:
        if self.fail:
            raise RuntimeError("no runner")
        self.requests.append((request.tool, dict(request.params), role))
        return graph.record_tool_call(ToolCall(
            tool_call_id=graph.reserve_tool_call_id(), tool_name=request.tool, query_parameters=request.params,
            purpose=request.purpose, execution_status="success", retrieval_status="no_records_found",
            requested_by="code", charged_to="code"))


def engine(runner: Runner) -> Engine:
    return Engine({}, "cache_only", None, runner, None, resolver=SymbolResolver({}), groups=GroupRegistry({}))


def decided() -> ClaimGraph:
    g = ClaimGraph(dev_case())
    binding_assay(g, "TFA")
    claim(g, [VARIANT], "alters_binding", [group(7, ["TFB", "TFC"])], "increases")
    eqtl(g, "GENE1")
    g.set_result(RunResult(outcome="multiple_explanations", stop_reason="converged"), "code")
    return g


def call(g: ClaimGraph, tool: str, params: dict, observations: list[dict]) -> None:
    g.record_tool_call(ToolCall(tool_call_id=g.reserve_tool_call_id(), tool_name=tool, query_parameters=params,
                                execution_status="success", retrieval_status="records_found",
                                observations=observations, requested_by="code", charged_to="code"))


def test_named_factors_are_the_tfs_and_groups_of_live_binding_claims_about_the_case_variant():
    g = decided()
    claim(g, [EntityRef(kind="variant", label="rs7606173")], "alters_binding", [tf("TFZ")], "increases")
    named = chain.named_factors(g)
    assert named["tfs"] == ["TFA"] and named["groups"] == [{"id": "G007", "members": ["TFB", "TFC"]}]
    assert named["listed"] == ["TFA", "TFB", "TFC"] and named["not_listed"] == 0     # TFZ: about another variant
    many = ClaimGraph(dev_case())
    claim(many, [VARIANT], "alters_binding", [group(1, [f"TF{i}" for i in range(30)])], "increases")
    capped = chain.named_factors(many)
    assert len(capped["listed"]) == chain.FACTOR_CAP and capped["not_listed"] == 30 - chain.FACTOR_CAP


def test_expression_contexts_come_from_the_case_then_the_claims_that_name_a_biosample():
    g = decided()
    assert chain.lookup_contexts(g) == [HEPG2.label]          # the binding assay's claim is stated in HepG2
    claim(g, [VARIANT], "alters_binding", [tf("TFQ")], "increases", ContextScope(label="an unnamed cell system"))
    assert chain.lookup_contexts(g) == [HEPG2.label]          # no biosample or tissue: nothing to look up


def test_after_the_decision_code_looks_up_every_named_factor_and_changes_nothing_else():
    g = decided()
    runner = Runner(["chip_occupancy", "qbic_tf_detail", "tf_expression"])
    before = (g.result.model_dump(), {c: (x.assessment, len(x.evidence_links)) for c, x in g.claims.items()},
              [h.disposition for h in g.hypotheses.values()])
    engine(runner)._factor_lookups(_Run(graph=g, started=0.0))
    assert runner.requests == [
        ("chip_occupancy", {}, "code"),
        ("qbic_tf_detail", {"tf": "TFA"}, "code"), ("qbic_tf_detail", {"group": "G007"}, "code"),
        *(("tf_expression", {"tf": name, "context": HEPG2.label}, "code") for name in ("TFA", "TFB", "TFC"))]
    assert before == (g.result.model_dump(), {c: (x.assessment, len(x.evidence_links)) for c, x in g.claims.items()},
                      [h.disposition for h in g.hypotheses.values()])
    event = g.events[-1]
    assert (event.action, event.role) == ("collect_facts", "code") and "shown only" in event.concise_reason
    assert len(event.target_ids) == 6 and event.details["factors"] == ["TFA", "TFB", "TFC"]
    assert all(t.purpose == FACTOR_PURPOSE for t in g.tool_calls.values() if t.tool_name == "tf_expression")


def test_the_lookups_skip_missing_tools_undecided_runs_and_never_raise():
    g = decided()
    partial = Runner(["tf_expression"])
    engine(partial)._factor_lookups(_Run(graph=g, started=0.0))
    assert {tool for tool, _, _ in partial.requests} == {"tf_expression"}
    undecided = ClaimGraph(dev_case())
    binding_assay(undecided, "TFA")
    idle = Runner(["chip_occupancy", "qbic_tf_detail", "tf_expression"])
    engine(idle)._factor_lookups(_Run(graph=undecided, started=0.0))                  # no result: nothing is asked
    stopped = _Run(graph=decided(), started=0.0)
    stopped.stop_reason = "cache_miss"
    engine(idle)._factor_lookups(stopped)
    nothing = ClaimGraph(dev_case())                                                  # no binding claim at all
    eqtl(nothing, "GENE1")
    nothing.set_result(RunResult(outcome="no_supported_explanation", stop_reason="converged"), "code")
    engine(idle)._factor_lookups(_Run(graph=nothing, started=0.0))
    assert idle.requests == []
    events = len(g.events)
    engine(Runner(["chip_occupancy"], fail=True))._factor_lookups(_Run(graph=g, started=0.0))
    assert len(g.events) == events                                                    # the failure was swallowed


def test_the_report_lists_what_the_lookups_returned_beside_the_answer(tmp_path):
    g = decided()
    assert chain.chain_view(g)["factors"]["rows"] == []                               # nothing was looked up yet
    call(g, "chip_occupancy", {}, [{"record": "factor", "tf": "TFA", "experiments": 2, "biosamples": ["HepG2", "K562"]}])
    call(g, "qbic_tf_detail", {"tf": "TFA"}, [
        {"record": "model", "model": "TFA_m1", "status": "ok", "z": 6.0, "effect": 0.4, "binds_more": "alt",
         "passes_gate": True, "maps_to": ["TFA"], "site_strength": {"ref": 60.0, "alt": 91.5}},
        {"record": "model", "model": "TFA_m2", "status": "ok", "z": -30.0, "effect": -1.2, "binds_more": "ref",
         "passes_gate": True, "maps_to": ["TFA", "TFB"], "site_strength": {"ref": 99.0, "alt": 70.0}}])
    call(g, "tf_expression", {"tf": "TFA", "context": "HepG2"}, [
        {"record": "expression", "tf": "TFA", "context": "HepG2", "source_context": "DepMap:ACH-1", "tpm": 12.5,
         "source": "DepMap HepG2"}])
    call(g, "tf_expression", {"tf": "TFC", "context": "HepG2"}, [
        {"record": "context", "context": "HepG2", "status": "unknown"}])
    view = chain.chain_view(g)
    assert chain.factor_rows(view, "T", "G") == [
        ["TFA", "2 of 2 models past the gate; largest |z|: more binding to T (z -30.0, effect -1.20); site strength "
                "T 99 → G 70", "peak in 2 experiments: HepG2, K562", "12.5 TPM, DepMap HepG2"],
        ["TFB", "1 of 1 model past the gate; largest |z|: more binding to T (z -30.0, effect -1.20); site strength "
                "T 99 → G 70", "no peak in ENCODE or ReMap", "no level for the contexts looked up"],
        ["TFC", "no model", "no peak in ENCODE or ReMap", "no level for the contexts looked up"]]
    ranked_before = json.dumps(chain.chain_view(decided())["ranked"])
    assert json.dumps(view["ranked"]) == ranked_before                                # the lookups order nothing
    loaded = bundle.load_bundle(write_run(g, tmp_path / "run"))
    for rendered in (report.render_html(loaded), report.render_markdown(loaded)):
        assert "what the lookups returned (shown, never ranked)" in rendered
        assert "peak in 2 experiments: HepG2, K562" in rendered and "12.5 TPM, DepMap HepG2" in rendered
        assert "no peak here is not evidence of absence" in rendered
