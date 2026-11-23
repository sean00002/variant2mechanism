"""The tool contract: validation, dedupe, budgets, raw files, never raising, adapter-level replay and fixtures."""

import hashlib
import json
import socket

import numpy as np
import pytest

from variant2mechanism.context.http import Http
from variant2mechanism.v9.fixtures import (
    FixtureToolRunner,
    ScriptedResponses,
    ScriptExhausted,
    load_fixture,
)
from variant2mechanism.v9.graph import ClaimGraph
from variant2mechanism.v9.schemas import Case, Evidence, ToolRequest, Variant
from variant2mechanism.v9.tools import (
    REGISTRY,
    AdapterResult,
    ParamSpec,
    RecordedToolRunner,
    ToolLimits,
    ToolRegistry,
    ToolRunner,
    ToolSpec,
    canonical_params,
)

ECHO = ToolSpec(name="echo", route="computational", description="test adapter: echoes its text as an annotation",
                params={"text": ParamSpec(type="str", required=True), "tags": ParamSpec(type="list[str]",
                                                                                       normalise="upper"),
                        "n": ParamSpec(type="int"), "mode": ParamSpec(choices=["fast", "slow"])},
                provider="test", dataset_release="r1", evidence_classes=["annotation"])
READ = ToolSpec(name="read", route="literature", assemblies=[], params={"pmcid": ParamSpec(required=True),
                                                                        "focus": ParamSpec(type="list[str]")},
                fulltext_params=["pmcid"], provider="test")
SNV_ONLY = ToolSpec(name="snv_only", route="computational", variant_types=["SNV"])


def echo(params, ctx) -> AdapterResult:
    text = str(params["text"])
    if text == "boom":
        raise ValueError("adapter exploded")
    if text == "wrong type":
        return {"not": "an AdapterResult"}
    if text == "network":
        socket.create_connection(("example.org", 80), timeout=1)
    if text == "empty":
        return AdapterResult(retrieval_status="no_records_found", raw={"hits": []})
    if text == "bad contract":     # evidence from an empty retrieval: the runner must refuse it
        return AdapterResult(retrieval_status="no_records_found", evidence=[annotation("nothing")])
    return AdapterResult(retrieval_status="records_found", observations=[{"text": text}],
                         raw={"text": text, "tags": params.get("tags", [])}, evidence=[annotation(text)])


def annotation(text: str) -> Evidence:
    return Evidence(evidence_class="annotation", observed_result=f"echo: {text}", independence_group=f"echo:{text}",
                    origin="tool")


def read(params, ctx) -> AdapterResult:
    return AdapterResult(retrieval_status="records_found", raw={"pmcid": params["pmcid"]},
                         fulltext_read=params["pmcid"] != "PMC-ABSTRACT")


@pytest.fixture
def registry() -> ToolRegistry:
    reg = ToolRegistry()
    reg.register(ECHO, echo)
    reg.register(READ, read)
    reg.register(SNV_ONLY, lambda params, ctx: AdapterResult(retrieval_status="records_found"))
    return reg


@pytest.fixture
def case() -> Case:
    return Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"))


@pytest.fixture
def graph(case) -> ClaimGraph:
    return ClaimGraph(case)


def runner(registry, tmp_path, **kw) -> ToolRunner:
    return ToolRunner(mode="cache_only", run_dir=tmp_path / "run", registry=registry, clock=lambda: "T0", **kw)


def call(r: ToolRunner, graph, tool="echo", role="computational_investigator", **params):
    return r.run(ToolRequest(tool=tool, params=params), graph.case, graph, role)


def test_registry_is_ordered_and_refuses_duplicates(registry):
    assert registry.names() == ["echo", "read", "snv_only"] and registry.names("literature") == ["read"]
    with pytest.raises(ValueError, match="already registered"):
        registry.register(ECHO, echo)
    assert ECHO.describe()["params"]["mode"] == {"type": "str", "required": False, "description": "",
                                                 "choices": ["fast", "slow"]}
    assert "echo" not in REGISTRY.names()                                 # no test adapter in the default registry


def test_canonical_params_normalise_and_refuse_clearly():
    assert canonical_params(ECHO, {"text": "  a  b ", "tags": ["y", "x", " X "], "n": 2.0}) == {
        "n": 2, "tags": ["X", "Y"], "text": "a b"}
    for params, message in [({}, "missing required parameter text"), ({"text": "a", "colour": "red"},
                                                                       "unknown parameter"),
                            ({"text": 3}, "must be a string"), ({"text": "a", "n": True}, "must be an integer"),
                            ({"text": "a", "mode": "medium"}, "must be one of fast, slow")]:
        with pytest.raises(Exception, match=message):
            canonical_params(ECHO, params)


def test_identical_requests_return_the_earlier_call_without_counting(registry, tmp_path, graph):
    r = runner(registry, tmp_path)
    first = call(r, graph, text="hello", tags=["b", "a"])
    again = call(r, graph, text=" hello ", tags=["A", "B"])
    assert again.tool_call_id == first.tool_call_id and len(graph.tool_calls) == 1
    assert r.budget(graph).tool_calls_used == 1
    assert first.evidence_ids == ["E1"] and graph.evidence["E1"].retrieval_ref == first.tool_call_id


def test_bad_requests_are_refused_recorded_and_not_counted(registry, tmp_path, graph):
    r = runner(registry, tmp_path, allowed_tools=["echo", "read"])
    refusals = [call(r, graph, tool="nope", text="x"), call(r, graph, text="x", colour="red"),
                call(r, graph), call(r, graph, tool="read", pmcid="PMC1"),
                call(r, graph, tool="snv_only")]
    assert [c.execution_status for c in refusals] == ["not_applicable"] * 5
    assert "unknown tool 'nope'" in refusals[0].message and "unknown parameter" in refusals[1].message
    assert "missing required" in refusals[2].message
    assert "the computational investigator cannot request it" in refusals[3].message
    assert "allowlist" in refusals[4].message
    assert all(c.charged_to == "none" and c.tool_call_id in graph.tool_calls for c in refusals)
    assert r.budget(graph).tool_calls_used == 0 and graph.evidence == {}


def test_variant_types_the_tool_does_not_cover_are_not_applicable(registry, tmp_path):
    indel = Case(case_id="DEV-2", variant=Variant(chrom="2", pos=100, ref="T", alt="TG"))
    g = ClaimGraph(indel)
    out = call(runner(registry, tmp_path), g, tool="snv_only")
    assert out.execution_status == "not_applicable" and "covers SNV only" in out.message and out.charged_to == "none"


def test_agent_tool_budget_and_separate_code_counter(registry, tmp_path, graph):
    r = runner(registry, tmp_path, limits=ToolLimits(max_tool_calls=2))
    call(r, graph, text="a")
    call(r, graph, text="b")
    over = call(r, graph, text="c")
    assert over.execution_status == "not_applicable" and "tool budget exhausted (2 of 2" in over.message
    code = call(r, graph, role="code", text="c")
    assert code.execution_status == "success" and code.charged_to == "code"
    assert call(r, graph, text="a").tool_call_id == "T1"                 # a repeat is still free
    b = r.budget(graph)
    assert (b.tool_calls_used, b.tool_calls_left, b.code_tool_calls) == (2, 0, 1)


def test_full_text_budget_counts_unique_articles(registry, tmp_path, graph):
    r = runner(registry, tmp_path, limits=ToolLimits(fulltext_soft=1, fulltext_hard=1))
    lit = "literature_investigator"
    abstract = call(r, graph, tool="read", role=lit, pmcid="PMC-ABSTRACT")   # only the abstract: not counted
    assert abstract.execution_status == "success" and abstract.fulltext_article is None
    first = call(r, graph, tool="read", role=lit, pmcid="PMC1", focus=["binding"])
    reread = call(r, graph, tool="read", role=lit, pmcid="PMC1", focus=["luciferase"])
    assert first.fulltext_article == reread.fulltext_article == "PMC1" and reread.execution_status == "success"
    second = call(r, graph, tool="read", role=lit, pmcid="PMC2")
    assert second.execution_status == "not_applicable" and "full-text budget exhausted" in second.message
    b = r.budget(graph)
    assert (b.fulltext_used, b.fulltext_left, b.fulltext_soft_reached, b.tool_calls_used) == (1, 0, True, 3)


def test_runner_never_raises(registry, tmp_path, graph):
    r = runner(registry, tmp_path)
    boom = call(r, graph, text="boom")
    assert boom.execution_status == "error" and boom.message == "ValueError: adapter exploded"
    wrong = call(r, graph, text="wrong type")
    assert wrong.execution_status == "error" and "not AdapterResult" in wrong.message
    blocked = call(r, graph, text="network")
    assert blocked.execution_status == "error" and "network access is blocked" in blocked.message
    broken = call(r, graph, text="bad contract")
    assert broken.execution_status == "error" and broken.message.startswith("adapter contract:")
    assert broken.evidence_ids == [] and graph.evidence == {}
    assert all(c.charged_to == "agent" for c in (boom, wrong, blocked, broken))


def test_missing_adapter_is_unavailable(tmp_path, graph):
    reg = ToolRegistry()
    reg.register(ToolSpec(name="later", route="computational"), None)
    out = call(runner(reg, tmp_path), graph, tool="later")
    assert out.execution_status == "unavailable" and "no adapter" in out.message


def test_raw_results_are_written_once_with_their_hash(registry, tmp_path, graph):
    r = runner(registry, tmp_path)
    out = call(r, graph, text="hello")
    path = tmp_path / "run" / out.raw_result_path
    assert out.raw_result_path == "raw/T1.json"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == out.raw_result_hash
    assert json.loads(path.read_text()) == {"tags": [], "text": "hello"}
    (tmp_path / "run" / "raw" / "T2.json").write_text("someone else's file")
    clash = call(r, graph, text="other")
    assert clash.execution_status == "error" and "FileExistsError" in clash.message
    assert (tmp_path / "run" / "raw" / "T2.json").read_text() == "someone else's file"   # never overwritten
    no_dir = ToolRunner(registry=registry, clock=lambda: "T0")
    in_memory = call(no_dir, ClaimGraph(graph.case), text="hello")
    assert in_memory.raw_result_path is None and in_memory.raw_result_hash == out.raw_result_hash


def bundle_from(graph: ClaimGraph, folder) -> None:
    """What bundle.py writes for replay: graph.json (it names the case), one ToolCall and one Evidence per line (raw/
    is already in the folder)."""
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "graph.json").write_text(graph.to_json())
    (folder / "tool_calls.jsonl").write_text("".join(t.model_dump_json() + "\n" for t in graph.tool_calls.values()))
    (folder / "evidence.jsonl").write_text("".join(e.model_dump_json() + "\n" for e in graph.evidence.values()))


def test_recorded_runner_replays_hits_and_reports_misses(registry, tmp_path, case):
    original = ClaimGraph(case)
    live = ToolRunner(run_dir=tmp_path / "saved", registry=registry, clock=lambda: "2026-11-08T10:00:00+00:00")
    calls = [call(live, original, text="hello"), call(live, original, text="empty"),
             call(live, original, tool="nope"), call(live, original, text="boom")]
    bundle_from(original, tmp_path / "saved")

    replayed = ClaimGraph(case)
    recorded = RecordedToolRunner(tmp_path / "saved", run_dir=tmp_path / "replay", registry=registry,
                                  clock=lambda: "later")
    again = [call(recorded, replayed, text="hello"), call(recorded, replayed, text="empty"),
             call(recorded, replayed, tool="nope"), call(recorded, replayed, text="boom")]
    strip = {"retrieval_time", "cached"}
    assert [c.model_dump(exclude=strip) for c in again] == [c.model_dump(exclude=strip) for c in calls]
    assert all(c.cached for c in again[:2]) and replayed.evidence == original.evidence
    raw = "raw/T1.json"
    assert (tmp_path / "replay" / raw).read_bytes() == (tmp_path / "saved" / raw).read_bytes()
    miss = call(recorded, replayed, text="never asked")
    assert miss.execution_status == "cache_miss" and miss.evidence_ids == [] and len(recorded.misses) == 1


def test_a_malformed_adapter_result_is_a_charged_error_that_is_never_rerun(tmp_path, case):
    runs = {"n": 0}

    def malformed(params, ctx) -> AdapterResult:
        runs["n"] += 1                            # in a real adapter: one more HTTP request each time
        good = annotation("variant lies in element E")
        kinds = {"dict": {"not": "evidence"}, "field": good.model_copy(update={"context": "HepG2"})}
        observations = [{"z": np.int64(3)}] if params["text"] == "numpy" else []
        raw = {"z": float("nan")} if params["text"] == "nan" else {"n": runs["n"]}
        return AdapterResult(retrieval_status="records_found", observations=observations, raw=raw,
                             evidence=[good, kinds[params["text"]]] if params["text"] in kinds else [good])

    reg = ToolRegistry()
    reg.register(ECHO.model_copy(update={"name": "malformed"}), malformed)
    graph = ClaimGraph(case)
    r = runner(reg, tmp_path, limits=ToolLimits(max_tool_calls=10))
    first = call(r, graph, tool="malformed", text="field")
    repeats = [call(r, graph, tool="malformed", text="field") for _ in range(4)]
    assert first.execution_status == "error" and first.charged_to == "agent" and "ValidationError" in first.message
    assert {c.tool_call_id for c in repeats} == {first.tool_call_id} and runs["n"] == 1
    assert graph.evidence == {} and r.budget(graph).tool_calls_used == 1          # no orphan evidence, one charge
    for text, problem in (("dict", "where Evidence belongs"), ("numpy", "adapter contract"), ("nan", "JSON")):
        out = call(r, graph, tool="malformed", text=text)
        assert out.execution_status == "error" and problem in out.message and out.evidence_ids == []
    assert graph.evidence == {} and r.budget(graph).tool_calls_used == 4
    bundle_from(graph, tmp_path / "run")
    replay = RecordedToolRunner(tmp_path / "run", registry=reg, run_dir=tmp_path / "replay", clock=lambda: "T0")
    again = call(replay, ClaimGraph(case), tool="malformed", text="field")
    assert again.execution_status == "error" and again.message == first.message and replay.misses == []


def test_cache_only_mode_refuses_an_http_client_that_can_reach_the_network(tmp_path):
    with pytest.raises(ValueError, match="offline"):
        ToolRunner(mode="cache_only", http=Http(tmp_path / "http"))
    assert ToolRunner(mode="cache_only", http=Http(tmp_path / "http", offline=True)).http.offline
    assert ToolRunner(mode="live", http=Http(tmp_path / "http")).mode == "live"


def test_the_recorded_runner_answers_only_the_case_it_recorded(registry, tmp_path, case):
    original = ClaimGraph(case)
    call(ToolRunner(run_dir=tmp_path / "saved", registry=registry, clock=lambda: "T0"), original, text="hello")
    bundle_from(original, tmp_path / "saved")
    recorded = RecordedToolRunner(tmp_path / "saved", registry=registry, clock=lambda: "T0")
    other = ClaimGraph(Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490909, ref="C", alt="A")))
    miss = call(recorded, other, text="hello")
    assert miss.execution_status == "cache_miss" and "saved bundle answers" in miss.message
    assert miss.evidence_ids == [] and len(recorded.misses) == 1


def test_an_unknown_role_is_refused_without_raising(registry, tmp_path, graph):
    out = call(runner(registry, tmp_path), graph, role="summariser", text="hello")
    assert (out.execution_status, out.requested_by, out.charged_to) == ("not_applicable", "code", "none")
    assert "unknown role" in out.message and out.tool_call_id in graph.tool_calls


def test_fixture_runner_answers_from_the_fixture(tmp_path):
    fixture = load_fixture("synthetic_repair")
    g = ClaimGraph(fixture.case)
    r = FixtureToolRunner(fixture, run_dir=tmp_path)
    assert [s.name for s in r.specs()] == ["syn_element_overlap", "syn_element_perturbation"]
    x = call(r, g, tool="syn_element_perturbation", gene="x")
    assert x.execution_status == "success" and x.retrieval_time == fixture.retrieval_time and x.cached
    ev = g.evidence[x.evidence_ids[0]]
    assert (ev.evidence_class, ev.origin, ev.direction, ev.context.biosample) == ("synthetic", "fixture", "increases",
                                                                                  "context X")
    unscripted = call(r, g, tool="syn_element_perturbation", gene="Z")
    assert unscripted.execution_status == "cache_miss" and unscripted.evidence_ids == []
    biological = ClaimGraph(Case(case_id="DEV-1", variant=fixture.case.variant))
    refused = call(r, biological, tool="syn_element_overlap")
    assert refused.execution_status == "not_applicable" and "synthetic cases" in refused.message
    with pytest.raises(ValueError, match="SYN-"):
        type(fixture).model_validate({**fixture.model_dump(), "case": {**fixture.case.model_dump(),
                                                                       "case_id": "REAL-1"}})


def test_scripted_responses_by_role_and_call_index():
    script = ScriptedResponses({"critic": [{"b": 1, "a": 2}, "{\"done\": true}"], "coordinator": ["{}"]})
    assert script.get("critic", 0) == '{"a": 2, "b": 1}'                   # canonical JSON text
    assert script.next("critic") == '{"a": 2, "b": 1}' and script.next("critic") == '{"done": true}'
    assert script.remaining("critic") == 0
    with pytest.raises(ScriptExhausted, match="critic call 3"):
        script.next("critic")
    send = script.transport(lambda body: body["role"])
    reply = send({"role": "coordinator", "model": "m"})
    assert reply["choices"][0]["message"]["content"] == "{}" and reply["usage"]["cost"] == 0.0
    assert script.served == [("critic", 0), ("critic", 1), ("coordinator", 0)]
    scripted = load_fixture("synthetic_repair").roles
    fresh = ScriptedResponses.from_fixture("synthetic_repair")
    assert scripted.get("coordinator") and fresh.remaining("coordinator") == len(scripted["coordinator"])
    assert fresh.remaining("no_such_role") == 0
