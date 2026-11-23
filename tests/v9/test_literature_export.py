"""The public-export excerpt policy (SPEC 13.11): verified passages (each at most 600 characters) are kept, article
text is dropped from tool calls, raw files and event details, and the run folder's own copies are left untouched."""

import json

from variant2mechanism.v9 import literature as lit
from variant2mechanism.v9.graph import ClaimGraph, GraphState

from .test_literature_extract import CHIP, binding_claim, emsa
from .test_literature_fakes import FakeHttp, case, read, records, routes, runner, search, search_response


def test_public_export_keeps_verified_passages_and_drops_article_text(tmp_path):
    graph = ClaimGraph(case())
    run_dir = tmp_path / "run"
    table = {**routes(), lit.search_url("GATA1", lit.DEFAULT_RESULTS): search_response([records()["PMC9000001"]])}
    run = runner(FakeHttp(table), run_dir)
    searched = search(run, graph, "GATA1")
    call = read(run, graph, pmcid="PMC9000001", focus=["gata1", "luciferase"])
    eid = graph.add_evidence(lit.evidence_from_experiment(emsa(), call, lit.load_article(run_dir, call)),
                             "literature_investigator")
    verified = graph.evidence[eid].experiment.passage
    graph.log("refuse_update", "code", "an extraction whose passage was not verified",
              details={"experiment": {"passage": CHIP, "location": "sec1.4/p1", "result": "long " * 300}})
    state = json.loads(graph.to_json())
    public = lit.public_graph_state(state)

    read_obs = public["tool_calls"][call.tool_call_id]["observations"]
    assert read_obs[0]["pmcid"] == "PMC9000001" and read_obs[0]["outline"]          # ids, titles, outline stay
    assert all(o["text"] == "" and o["text_dropped"] for o in read_obs[1:])
    assert all(o["abstract"] == "" for o in public["tool_calls"][searched.tool_call_id]["observations"])
    assert public["evidence"][eid]["experiment"]["passage"] == verified
    refused = public["events"][-1]["details"]["experiment"]
    assert refused["passage"] == lit.REMOVED and CHIP not in json.dumps(public["events"])   # never verified
    assert refused["location"] == "sec1.4/p1" and len(refused["result"]) <= lit.PUBLIC_PASSAGE_LIMIT
    assert state["tool_calls"][call.tool_call_id]["observations"][1]["text"]        # the run's copy is untouched

    raw = (run_dir / call.raw_result_path).read_bytes()
    stub_bytes = lit.public_raw(state["tool_calls"][call.tool_call_id], raw, state["evidence"].values())
    stub = lit.Article.model_validate_json(stub_bytes)
    assert [(s.location, s.text) for s in stub.sections] == [("sec1.1/p1", verified)]
    assert (stub.pmid, stub.doi) == ("90000001", "10.5555/v2m.test.1") and stub.title
    assert b"luciferase" not in stub_bytes.lower() and b"base editing" not in stub_bytes.lower()
    search_raw = (run_dir / searched.raw_result_path).read_bytes()
    public_search = json.loads(lit.public_raw(state["tool_calls"][searched.tool_call_id], search_raw, []))
    assert public_search["records"] and all(r["abstract"] == "" for r in public_search["records"])
    other = b'{"nes": 1.2}'
    assert lit.public_raw({"tool_name": "gtex_eqtl", "tool_call_id": "T9"}, other, []) == other
    assert json.loads(lit.public_raw(state["tool_calls"][call.tool_call_id], b"not an article", [])) == {
        "text_dropped": True, "tool_call_id": call.tool_call_id}


def test_public_evidence_cuts_a_long_passage_verbatim_and_leaves_other_evidence_alone():
    long = {"origin": "literature", "experiment": {"passage": "word " * 400}}
    out = lit.public_evidence(long)["experiment"]["passage"]
    assert 0 < len(out) <= lit.PUBLIC_PASSAGE_LIMIT
    assert long["experiment"]["passage"].startswith(out) and out.endswith("word")   # still source text, nothing added
    assert len(long["experiment"]["passage"]) == 2000                     # the input is not modified
    tool = {"origin": "tool", "observed_result": "GTEx: NES 1.2 in liver"}
    assert lit.public_evidence(tool) == tool


def strings(value):
    if isinstance(value, dict):
        return [s for v in value.values() for s in strings(v)]
    if isinstance(value, list):
        return [s for v in value for s in strings(v)]
    return [value] if isinstance(value, str) else []


def test_no_free_text_field_carries_article_text_into_a_public_export(tmp_path):
    """Review finding 9: the extractor's fields (result, scope, comparator, system) and agent text (rationales,
    answers) were exported unbounded, so pasted paragraphs left in a 'public' bundle. Extraction now bounds them and
    the export cuts every string, from older runs too."""
    graph = ClaimGraph(case())
    run_dir = tmp_path / "run"
    call = read(runner(FakeHttp(routes()), run_dir), graph, pmcid="PMC9000001", focus=["gata1"])
    article = lit.load_article(run_dir, call)
    pasted = " ".join(s.text for s in article.sections)
    eid = graph.add_evidence(lit.evidence_from_experiment(emsa().model_copy(update={
        "result": pasted, "comparator": pasted, "scope_supports": pasted * 3, "scope_does_not_test": pasted}),
        call, article), "literature_investigator")
    claim = binding_claim(graph)
    graph.link(claim, eid, "supports", "literature_investigator", "EMSA. " + pasted)
    state = json.loads(graph.to_json())
    public = lit.public_graph_state(state)
    assert all(len(s) <= lit.PUBLIC_PASSAGE_LIMIT for part in ("evidence", "claims") for s in strings(public[part]))
    rationale = public["claims"][claim]["evidence_links"][0]["rationale"]
    assert ("EMSA. " + pasted).startswith(rationale)                     # a verbatim prefix, nothing added
    old = {**state["evidence"][eid], "experiment": {**state["evidence"][eid]["experiment"], "result": pasted * 2}}
    assert all(len(s) <= lit.PUBLIC_PASSAGE_LIMIT for s in strings(lit.public_evidence(old)))
    assert ClaimGraph.from_state(GraphState.model_validate(public)).evidence[eid].experiment.passage    # still loads
