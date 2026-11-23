"""The run folder (SPEC 8, 13.4, 13.11, 13.16): new folders only, exclusive writes, what replay reads, a manifest with
no secrets and a fingerprint that covers untracked code, normalised metrics (candidate retention over every
hypothesis version, full-text reads as the budget counts them), the replay comparison and a public export that copies
only what the run wrote."""

import copy
import hashlib
import json
import re
import shutil
import subprocess

import pytest

from variant2mechanism.config import Config
from variant2mechanism.v9 import bundle
from variant2mechanism.v9.fixtures import FixtureToolRunner, load_fixture
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, HypothesisDraft
from variant2mechanism.v9.schemas import Evidence, ExperimentRecord, RunResult, ToolCall, ToolRequest
from variant2mechanism.v9.tools import AdapterResult, RecordedToolRunner, ToolRegistry, ToolSpec

from .test_report_support import (
    ELEMENT,
    VARIANT,
    claim,
    dev_case,
    discordant_inventory,
    gene,
    inventory_call,
    inventory_row,
    rich_graph,
    runner_for,
    synthetic_graph,
    synthetic_run,
    synthetic_steps,
    tf,
    tool_evidence,
    write_run,
)


def sha256(path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_a_run_folder_is_new_or_refused(tmp_path):
    run = bundle.new_run_dir(tmp_path / "runs" / "one")
    assert run.is_dir() and list(run.iterdir()) == []
    with pytest.raises(FileExistsError, match="never reused or overwritten"):
        bundle.new_run_dir(run)
    (tmp_path / "a file").write_text("x")
    with pytest.raises(FileExistsError):
        bundle.new_run_dir(tmp_path / "a file")
    assert (tmp_path / "a file").read_text() == "x"


def test_the_bundle_holds_exactly_what_replay_reads(tmp_path):
    g, run = synthetic_run(tmp_path)
    assert sorted(p.name for p in run.iterdir()) == sorted([*bundle.BUNDLE_FILES, "raw"])
    lines = {name: (run / name).read_text().splitlines() for name in ("tool_calls.jsonl", "evidence.jsonl",
                                                                      "events.jsonl")}
    assert lines["tool_calls.jsonl"] == [t.model_dump_json() for t in g.tool_calls.values()]
    assert lines["evidence.jsonl"] == [e.model_dump_json() for e in g.evidence.values()]
    assert lines["events.jsonl"] == [e.model_dump_json() for e in g.events]
    assert (run / "graph.json").read_text() == g.to_json()
    manifest = json.loads((run / "manifest.json").read_text())
    assert manifest["files"] == {name: sha256(run / name) for name in bundle.BUNDLE_FILES[:-1]}
    for call in g.tool_calls.values():          # raw/ is the runner's, kept as written
        assert sha256(run / call.raw_result_path) == call.raw_result_hash


def test_bundle_files_are_never_overwritten(tmp_path):
    g, _ = synthetic_graph()
    run = bundle.new_run_dir(tmp_path / "run")
    (run / "metrics.json").write_text("someone else's metrics")
    with pytest.raises(FileExistsError, match="metrics.json"):
        write_run(g, run)
    assert (run / "metrics.json").read_text() == "someone else's metrics"
    assert not (run / "graph.json").exists()                  # refused before anything was written
    other = write_run(g, tmp_path / "other")
    before = {p.name: p.read_bytes() for p in other.iterdir()}
    with pytest.raises(FileExistsError):
        write_run(g, other)
    assert {p.name: p.read_bytes() for p in other.iterdir()} == before


def test_load_bundle_round_trips_and_tolerates_missing_optional_files(tmp_path):
    g, run = synthetic_run(tmp_path)
    loaded = bundle.load_bundle(run)
    assert loaded.graph.to_json() == g.to_json() and loaded.graph.to_state() == g.to_state()
    assert loaded.manifest["mode"] == "fixture" and loaded.metrics["metrics_format"] == bundle.METRICS_FORMAT
    assert loaded.evaluation is None
    (run / "evaluation.json").write_text(json.dumps({"component_recovery": {}}))
    assert bundle.load_bundle(run).evaluation == {"component_recovery": {}}
    bare = tmp_path / "bare"
    bare.mkdir()
    (bare / "graph.json").write_text(g.to_json())
    only_graph = bundle.load_bundle(bare)
    assert (only_graph.manifest, only_graph.metrics, only_graph.evaluation) == ({}, {}, None)
    with pytest.raises(FileNotFoundError, match="not a v9 run folder"):
        bundle.load_bundle(tmp_path)


def test_the_manifest_fingerprints_the_code_and_holds_no_secrets(tmp_path, monkeypatch, v9_cfg):
    monkeypatch.setenv("V2M_SCREEN_API_KEY", "sk-test-secret-value-123")
    cfg = Config({**v9_cfg, "v9": {"limits": {"max_model_calls": 24, "max_tool_calls": 24},
                                   "tools": ["variant_annotation", "qbic_inventory"],
                                   "screen": {"api_key_env": "V2M_SCREEN_API_KEY"}, "token": "tok-123",
                                   "roles": {"coordinator": "generator"}}})
    g = ClaimGraph(dev_case())
    tool_evidence(g, "annotation", "The variant lies in cCRE EH38E0000001.", tool="ccre_overlap",
                  about_elements=["EH38E0000001"])
    manifest = bundle.build_manifest(
        request={"variant": "chr2:60490908:T>G", "origin": "unknown", "api_key": "sk-request-key"},
        case=g.case, mode="cache_only", config=cfg, graph=g, profile="release",
        manifest_parts={"prompts": {"coordinator_system": "ab" * 32}, "limits": {"max_model_calls": 24},
                        "roles": {"critic": {"key": "critic", "model": "openai/gpt-6-luna", "max_tokens": 16000}},
                        "stop_reason": "converged", "auth_header": "Bearer x", "access_key": "AKIA-SECRET"},
        created="2026-11-08T12:00:00+00:00")
    text = json.dumps(manifest)
    for secret in ("sk-test-secret-value-123", "V2M_SCREEN_API_KEY", "sk-request-key", "tok-123", "Bearer",
                   "AKIA-SECRET"):
        assert secret not in text
    assert manifest["engine"]["roles"]["critic"] == {"key": "critic", "model": "openai/gpt-6-luna",
                                                     "max_tokens": 16000}     # a client key name is not a secret
    assert manifest["config"]["v9"]["limits"] == {"max_model_calls": 24, "max_tool_calls": 24}
    assert manifest["config"]["v9"]["tools"] == ["variant_annotation", "qbic_inventory"]
    assert manifest["config"]["models"]["generator"] == v9_cfg["llm"]["generator"]
    assert manifest["engine"]["stop_reason"] == "converged" and manifest["created"] == "2026-11-08T12:00:00+00:00"
    assert manifest["request"] == {"variant": "chr2:60490908:T>G", "origin": "unknown"}
    code = manifest["code"]
    v9_dir = bundle.V9_DIR
    for name in ("graph.py", "bundle.py", "report.py", "report_template.html", "fixtures/synthetic_repair.json"):
        assert code["v9_sources"][name] == sha256(v9_dir / name)
    assert re.fullmatch(r"[0-9a-f]{64}", code["v9_sources_sha256"])
    git = code["git"]
    assert git["head"] is None or re.fullmatch(r"[0-9a-f]{40}", git["head"])
    assert git["dirty"] in (True, False, None)
    assert git["diff_sha256"] is None or re.fullmatch(r"[0-9a-f]{64}", git["diff_sha256"])
    assert manifest["dataset_releases"] == [{"tool": "ccre_overlap", "provider": "test provider",
                                             "dataset_release": "r1", "tool_version": ""}]
    assert "offline" in manifest["cache_policy"]["http"] and manifest["mode"] == "cache_only"
    assert manifest["engine_version"] == "v9.0"


def test_metrics_come_from_the_graph_and_keep_the_engines_usage(tmp_path):
    g, _ = synthetic_graph()
    engine = {"model_calls": 5, "cost_usd": 0.0123, "wall_seconds": 12.5, "nan_value": float("nan"),
              "model_usage_by_role": {     # as investigate.Engine reports it
                  "critic": {"calls": 2, "cost_usd": 0.01, "failures": 0, "prompt_tokens": 100,
                             "completion_tokens": 50, "latency_s": 1.5},
                  "coordinator": {"calls": 3, "cost_usd": 0.0023, "failures": 1, "prompt_tokens": 300,
                                  "completion_tokens": 70, "latency_s": 0.5}},
              "custom": {"x": 1}}
    m = bundle.normalise_metrics(engine, g)
    assert (m["model"]["calls"], m["model"]["cost_usd"], m["model"]["input_tokens"], m["model"]["output_tokens"],
            m["model"]["latency_s"], m["model"]["failures"]) == (5, 0.0123, 400, 120, 2.0, 1)
    assert m["model"]["by_role"]["critic"] == {"calls": 2, "cost_usd": 0.01, "input_tokens": 100, "output_tokens": 50,
                                              "latency_s": 1.5, "failures": 0}
    assert m["tools"]["by_retrieval_status"] == {"no_records_found": 1, "records_found": 2}
    assert (m["tools"]["executed"], m["tools"]["refused"], m["tools"]["cached"]) == (3, 0, 3)
    assert m["evidence"]["by_class"] == {"synthetic": 2} and m["evidence"]["unique_sources"] == 2
    assert m["graph"]["refused_updates"] == 1 and m["graph"]["hypotheses_by_disposition"] == {"active": 1,
                                                                                               "rejected": 1}
    assert m["wall_seconds"] == 12.5 and m["engine"]["nan_value"] is None and m["engine"]["custom"] == {"x": 1}
    json.dumps(m, allow_nan=False)
    assert bundle.normalise_metrics(m, g) == m                               # normalising twice changes nothing
    bare = bundle.normalise_metrics(None, g)
    assert bare["model"]["calls"] == g.model_usage.calls and bare["engine"] == {}


def test_inventory_groups_no_hypothesis_sketched_are_counted(tmp_path):
    g = ClaimGraph(dev_case())
    inventory_call(g, [inventory_row(1, True, [{"tf": "CEBPA", "mapping": "own"}, {"tf": "CEBPB", "mapping": "own"}]),
                       inventory_row(2, True), inventory_row(3, False)])
    binding = claim(g, [VARIANT], "alters_binding", [tf("CEBPA")], "increases")
    g.add_hypothesis(HypothesisDraft(title="CEBPA binding", required_claim_ids=[binding], mechanism_class="tf_binding"),
                     "coordinator")
    assert bundle.normalise_metrics({}, g)["inventory"] == {"groups": 3, "gate_passing": 2, "below_gate": 1,
                                                           "sketched": ["G001"], "inventory_only": ["G002"]}


def retention_graph() -> ClaimGraph:
    """Three gate-passing groups on the development case: G035 (CEBPA, CEBPB, CEBPE), G372 (HNF4A, HNF4G, NR2E1)
    and G900, which no hypothesis below ever names."""
    g = ClaimGraph(dev_case())
    own = lambda *tfs: [{"tf": t, "mapping": "own"} for t in tfs]       # noqa: E731
    inventory_call(g, [inventory_row(35, True, own("CEBPA", "CEBPB", "CEBPE")),
                       inventory_row(372, True, own("HNF4A", "HNF4G", "NR2E1")), inventory_row(900, True)])
    return g


def binding(g: ClaimGraph, symbol: str) -> str:
    return claim(g, [VARIANT], "alters_binding", [tf(symbol)], "increases")


def binding_draft(symbol: str) -> ClaimDraft:
    return ClaimDraft(subjects=[VARIANT], relation="alters_binding", objects=[tf(symbol)], direction="increases")


def test_candidate_retention_counts_every_hypothesis_version():
    def retention(g: ClaimGraph) -> tuple[list[str], list[str]]:
        inventory = bundle.normalise_metrics({}, g)["inventory"]
        return inventory["sketched"], inventory["inventory_only"]

    expected = (["G035", "G372"], ["G900"])
    # a local repair swaps the CEBPA claim for an HNF4A one: G035 was sketched by the hypothesis's first version
    g = retention_graph()
    h = g.add_hypothesis(HypothesisDraft(title="CEBPA binding", required_claim_ids=[binding(g, "CEBPA")],
                                         mechanism_class="tf_binding"), "coordinator")
    g.replace_required_claim(h, "C1", binding(g, "HNF4A"), "HNF4A fits the context better", "coordinator")
    assert g.hypotheses[h].claim_ids == ["C2"] and retention(g) == expected
    # two supersessions, CEBPA -> HNF4G -> HNF4A, each naming the hypothesis
    g = retention_graph()
    h = g.add_hypothesis(HypothesisDraft(title="CEBPA binding", required_claim_ids=[binding(g, "CEBPA")],
                                         mechanism_class="tf_binding"), "coordinator")
    second = g.supersede_claim("C1", binding_draft("HNF4G"), "a paralog", "coordinator", [h])
    g.supersede_claim(second, binding_draft("HNF4A"), "a paralog", "coordinator", [h])
    assert retention(g) == expected
    # a supersession made outside any hypothesis: the claim a hypothesis later took up still names its predecessor
    g = retention_graph()
    replacement = g.supersede_claim(binding(g, "CEBPA"), binding_draft("HNF4A"), "a paralog", "coordinator")
    g.add_hypothesis(HypothesisDraft(title="HNF4A binding", required_claim_ids=[replacement],
                                     mechanism_class="tf_binding"), "coordinator")
    assert retention(g) == expected
    # a member alternative names a group as much as a claim does
    g = retention_graph()
    g.add_hypothesis(HypothesisDraft(title="HNF4A binding", required_claim_ids=[binding(g, "HNF4A")],
                                     mechanism_class="tf_binding", member_alternatives=[" cebpb "]), "coordinator")
    assert retention(g) == expected
    assert bundle.sketched_groups(g, bundle.inventory_table(g)) == {"G035", "G372"}


def test_full_text_reads_are_counted_as_the_budget_counts_them(monkeypatch):
    g = ClaimGraph(dev_case())

    def read(param: str, ids: list[str], *, fulltext: bool = True) -> None:
        g.record_tool_call(ToolCall(tool_call_id=g.reserve_tool_call_id(), tool_name="literature_read",
                                    query_parameters={"id": param}, execution_status="success",
                                    retrieval_status="records_found", requested_by="literature_investigator",
                                    charged_to="agent", fulltext_article=param if fulltext else None,
                                    read_article=param, article_ids=ids))

    read("PMC100", ["11111", "PMC100", "10.1000/x"])
    read("11111", ["11111", "PMC100"])                         # the same article, requested again by its PMID
    read("22222", ["22222"], fulltext=False)                   # another article, abstract only
    read("33333", ["33333"], fulltext=False)                   # an abstract first ...
    read("PMC300", ["PMC300", "33333"])                        # ... then the same article in full, by its PMCID
    before = g.to_json()
    tools = bundle.normalise_metrics({"fulltext_reads": g.budget_snapshot().fulltext_reads}, g)["tools"]
    assert tools["fulltext_reads"] == g.budget_snapshot().fulltext_reads == len(g.fulltext_articles()) == 2
    assert tools["articles_read"] == 3 and g.to_json() == before          # the graph is read, never changed
    # both counts are the graph's own grouping (ClaimGraph.fulltext_articles), never a second copy of the rule
    monkeypatch.setattr(ClaimGraph, "fulltext_articles",
                        lambda self: [frozenset({tid}) for tid in self.tool_calls])
    tools = bundle.normalise_metrics({}, g)["tools"]
    assert tools["fulltext_reads"] == tools["articles_read"] == 5


def test_the_bundle_re_exports_the_graphs_retention_rule():
    from variant2mechanism.v9 import evaluation
    from variant2mechanism.v9 import graph as graph_module

    # one rule for the engine, metrics.json and the evaluator: the graph's functions, never a copy (C3-6)
    assert bundle.sketched_groups is graph_module.sketched_groups is evaluation.sketched_groups
    assert bundle.hypothesis_versions is graph_module.hypothesis_versions


def test_a_discordant_groups_row_joins_the_item_for_its_allele():
    from variant2mechanism.v9 import adapters  # imported here: rendering itself never loads the adapters

    g = ClaimGraph(dev_case())
    g_item, t_item, agree = discordant_inventory(g).evidence_ids
    rows = bundle.inventory_table(g)
    assert rows == adapters.inventory_rows(g)
    # G049's row names its best model's allele (G): its item, although the T item came later in the call
    assert [r["evidence_id"] for r in rows] == [g_item, agree, None]
    assert bundle.inventory_items(g) == {"G049": [g_item, t_item], "G002": [agree]}
    assert bundle.inventory_summary(g) == {"groups": 3, "gate_passing": 2, "below_gate": 1, "sketched": [],
                                           "inventory_only": ["G049", "G002"]}       # one row per group, as before


@pytest.mark.skipif(shutil.which("git") is None, reason="git is not installed")
def test_the_fingerprint_covers_untracked_sources(tmp_path):
    repo = tmp_path / "repo"
    (repo / "src" / "pkg").mkdir(parents=True)
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True, capture_output=True)
    (repo / ".gitignore").write_text("*.pyc\n")
    module = repo / "src" / "pkg" / "transport.py"
    module.write_text("def send():\n    return 1\n")
    (repo / "src" / "pkg" / "transport.pyc").write_bytes(b"ignored by git")
    before = bundle.code_fingerprint(repo)["git"]
    assert before["head"] is None and set(before["untracked"]) == {"src/pkg/transport.py"}
    module.write_text("def send():\n    return 2  # changed behaviour, never committed\n")
    after = bundle.code_fingerprint(repo)["git"]
    assert after["untracked"]["src/pkg/transport.py"] == sha256(module)
    assert after["untracked_sha256"] != before["untracked_sha256"]


def test_the_public_export_copies_only_what_the_run_wrote(tmp_path):
    def fresh(name: str):
        g, run = synthetic_run(tmp_path / name)
        return run, run / g.tool_calls["T1"].raw_result_path

    outside = tmp_path / "private-notes.txt"
    outside.write_text("PRIVATE-NOTES-OUTSIDE-THE-RUN")
    run, raw = fresh("linked-file")
    raw.unlink()
    raw.symlink_to(outside)
    with pytest.raises(ValueError, match="never follows a link"):
        bundle.export_public(run, tmp_path / "out-1")
    run, raw = fresh("linked-folder")              # raw/ itself a link to a byte-identical copy outside the run
    shutil.copytree(run / "raw", tmp_path / "raw-elsewhere")
    shutil.rmtree(run / "raw")
    (run / "raw").symlink_to(tmp_path / "raw-elsewhere")
    with pytest.raises(ValueError, match="never follows a link"):
        bundle.export_public(run, tmp_path / "out-2")
    run, raw = fresh("rewritten-raw")
    raw.write_text(json.dumps({"note": "PRIVATE-NOTES-OUTSIDE-THE-RUN"}))
    with pytest.raises(ValueError, match="raw_result_hash"):
        bundle.export_public(run, tmp_path / "out-3")
    run, _ = fresh("edited-graph")
    with open(run / "graph.json", "a", encoding="utf-8") as f:
        f.write("\n")
    with pytest.raises(ValueError, match="graph.json has changed"):
        bundle.export_public(run, tmp_path / "out-4")
    assert not any((tmp_path / f"out-{i}").exists() for i in range(1, 5))      # refused before anything was written
    run, raw = fresh("missing-raw")                # a missing raw file publishes nothing and is recorded
    raw.unlink()
    out = bundle.export_public(run, tmp_path / "out-5")
    export = bundle.load_bundle(out).manifest["public_export"]
    assert export["raw_files_missing"] == ["raw/T1.json"] and export["files_verified"] is True
    assert "PRIVATE-NOTES" not in every_text(out)


def test_the_inventory_rows_are_the_adapters_rows():
    from variant2mechanism.v9 import adapters  # imported here: rendering itself never loads the adapters

    g = rich_graph()
    assert bundle.inventory_table(g) == adapters.inventory_rows(g)
    assert [r["evidence_id"] for r in bundle.inventory_table(g)] == ["E1", "E2", None]
    assert bundle.inventory_call(g).tool_call_id == "T1" and bundle.inventory_table(ClaimGraph(dev_case())) == []


def test_the_recorded_runner_reads_a_written_bundle_back(tmp_path):
    original, run = synthetic_run(tmp_path)
    registry = FixtureToolRunner(load_fixture("synthetic_repair")).registry
    replayed = ClaimGraph(original.case)
    recorded = RecordedToolRunner(run, registry=registry, run_dir=tmp_path / "replay",
                                  clock=lambda: "2026-11-09T00:00:00+00:00")
    synthetic_steps(replayed, recorded)
    assert recorded.misses == []
    strip = {"retrieval_time", "cached"}
    assert [t.model_dump(exclude=strip) for t in replayed.tool_calls.values()] == [
        t.model_dump(exclude=strip) for t in original.tool_calls.values()]
    assert replayed.evidence == original.evidence
    for call in original.tool_calls.values():
        assert sha256(tmp_path / "replay" / call.raw_result_path) == call.raw_result_hash
    assert bundle.compare_graph_json(json.loads(original.to_json()), json.loads(replayed.to_json())) == []
    miss = recorded.run(ToolRequest(tool="syn_element_perturbation", params={"gene": "Z"}), replayed.case, replayed,
                        "computational_investigator")
    assert miss.execution_status == "cache_miss" and len(recorded.misses) == 1


def test_the_replay_comparison_ignores_volatile_fields_but_not_science():
    g = rich_graph()
    a = json.loads(g.to_json())
    b = copy.deepcopy(a)
    for call in b["tool_calls"].values():
        call["retrieval_time"], call["cached"] = "2030-01-01T00:00:00+00:00", not call["cached"]
    b["model_usage"]["cost_usd"] = 9.99
    for event in b["events"]:
        event["budget_snapshot"]["cost_usd"] = 1.5
        event["details"]["latency_s"] = 3.2
    b["created"] = "later"
    assert bundle.compare_graph_json(a, b) == []
    changed = copy.deepcopy(b)
    changed["claims"]["C3"]["assessment"] = "supported_in_scope"
    assert bundle.compare_graph_json(a, changed) == [
        '/claims/C3/assessment: "unassessed" -> "supported_in_scope"']
    flipped = copy.deepcopy(b)
    flipped["claims"]["C1"]["evidence_links"][0]["corrected"] = 0           # False and 0 are not the same flag
    flipped["hypotheses"]["H1"]["disposition"] = "active"
    del flipped["events"][-1]
    out = bundle.compare_graph_json(a, flipped)
    assert "/claims/C1/evidence_links[0]/corrected: false -> 0" in out
    assert '/hypotheses/H1/disposition: "rejected" -> "active"' in out
    assert any(line.startswith("/events:") for line in out)


FULL_TEXT = ("Results. " + " ".join(f"Sentence {i} describes the assay in detail." for i in range(60))
             + " ARTICLE-ONLY-SENTENCE: this text was never quoted as a passage.")
LONG_PASSAGE = FULL_TEXT[9:960]
SHORT_PASSAGE = "Sentence 3 describes the assay in detail."
UNVERIFIED = "UNVERIFIED-QUOTE that the run refused to accept as a passage"


def read_adapter(params, ctx) -> AdapterResult:
    """A literature read shaped as literature.py returns one (contract C3): the parsed Article as the raw result, a
    header and focus passages as observations."""
    from variant2mechanism.v9.literature import Article, ArticleSection

    article = Article(pmid="11111", pmcid=str(params["pmcid"]), title="An assay study", route="europepmc_fulltext",
                      access="full_text", sections=[ArticleSection(location="sec1/p1", heading="Results",
                                                                   text=FULL_TEXT)])
    return AdapterResult(retrieval_status="records_found", raw_bytes=article.model_dump_json().encode(),
                         observations=[{"kind": "article", "pmid": "11111", "pmcid": params["pmcid"],
                                        "title": "An assay study", "outline": [{"location": "sec1/p1",
                                                                                "heading": "Results"}]},
                                       {"kind": "passage", "location": "sec1/p1", "heading": "Results",
                                        "text": FULL_TEXT, "matched": ["assay"], "excerpt": False}])


def literature_run(tmp_path):
    """A development-case run with a literature read (full text in raw/ and in the read's observations), two
    extracted experiments with verified passages (one longer than the public bound), an annotation call and a refused
    extraction recorded in the events."""
    from variant2mechanism.v9.literature import READ_SPEC

    reg = ToolRegistry()
    reg.register(READ_SPEC, read_adapter)
    reg.register(ToolSpec(name="ccre_overlap", route="computational", provider="test"),
                 lambda params, ctx: AdapterResult(retrieval_status="records_found", raw={"ccre": "EH38E0000001"},
                                                   evidence=[Evidence(evidence_class="annotation", origin="tool",
                                                                      observed_result="The variant lies in a cCRE.",
                                                                      independence_group="ccre",
                                                                      about_elements=["EH38E0000001"])]))
    run = bundle.new_run_dir(tmp_path / "run")
    g = ClaimGraph(dev_case())
    runner = runner_for(reg, run)
    annotation = runner.run(ToolRequest(tool="ccre_overlap"), g.case, g, "code")
    read = runner.run(ToolRequest(tool="literature_read", params={"pmcid": "PMC100"}), g.case, g,
                      "literature_investigator")
    assert read.execution_status == "success" and read.read_article == "PMC100"
    ids = []
    for passage, endpoint in ((LONG_PASSAGE, "activity"), (SHORT_PASSAGE, "binding")):
        ids.append(g.add_evidence(Evidence(
            evidence_class="reporter_assay", origin="literature", access="full_text", retrieval_ref=read.tool_call_id,
            observed_result=f"A reporter assay measured {endpoint}.", source_ids=["PMID:11111", "PMCID:PMC100"],
            independence_group=f"PMID:11111#reporter/{endpoint}", about_elements=["EH38E0000001"],
            experiment=ExperimentRecord(source_id="PMID:11111", pmcid="PMC100", access="full_text",
                                        location="sec1/p1", passage=passage, intervention="reporter",
                                        endpoint=endpoint)), "literature_investigator"))
    g.log("refuse_update", "literature_investigator", "the passage was not found in the article",
          details={"experiment": {"passage": UNVERIFIED, "location": "sec9/p9"}})
    write_run(g, run)
    return g, run, annotation, read, ids


def every_text(folder) -> str:
    return "\n".join(p.read_text(encoding="utf-8") for p in sorted(folder.rglob("*")) if p.is_file())


def test_the_public_export_keeps_verified_passages_and_drops_article_text(tmp_path):
    from variant2mechanism.v9.literature import PUBLIC_PASSAGE_LIMIT, Article

    g, run, annotation, read, (long_id, short_id) = literature_run(tmp_path)
    assert "ARTICLE-ONLY-SENTENCE" in every_text(run)
    (run / "evaluation.json").write_text(json.dumps({"gold": "evaluator-only"}))
    out = bundle.export_public(run, tmp_path / "public")
    text = every_text(out)
    for gone in ("ARTICLE-ONLY-SENTENCE", UNVERIFIED, LONG_PASSAGE[-40:], "evaluator-only"):
        assert gone not in text
    assert not (out / "evaluation.json").exists()
    assert (out / annotation.raw_result_path).read_bytes() == (run / annotation.raw_result_path).read_bytes()
    public = bundle.load_bundle(out)
    passages = {eid: public.graph.evidence[eid].experiment.passage for eid in (long_id, short_id)}
    assert passages[short_id] == SHORT_PASSAGE
    assert len(passages[long_id]) <= PUBLIC_PASSAGE_LIMIT
    assert LONG_PASSAGE.startswith(passages[long_id].rstrip("…"))
    stub = Article.model_validate_json((out / read.raw_result_path).read_bytes())
    assert {s.text for s in stub.sections} == {passages[long_id], SHORT_PASSAGE}      # verified passages only
    call = public.graph.tool_calls[read.tool_call_id]
    assert call.observations[0]["title"] == "An assay study" and call.observations[1]["text"] == ""
    export = public.manifest["public_export"]
    assert export["raw_files_rewritten"] == [read.raw_result_path] and call.raw_result_hash == read.raw_result_hash
    assert (export["evidence_text_cut"], export["tool_calls_text_removed"]) == ([long_id], [read.tool_call_id])
    assert len(export["events_scrubbed"]) == 1 and export["evaluation_left_out"] is True
    assert export["source_run"] == "run" and str(tmp_path) not in json.dumps(export)
    assert (out / "report.html").exists() and (out / "report.md").exists()
    assert "Public export." in (out / "report.html").read_text()
    assert bundle.compare_graph_json(json.loads(g.to_json()), json.loads(public.graph.to_json()))   # it differs
    with pytest.raises(FileExistsError):
        bundle.export_public(run, out)
    with pytest.raises(ValueError, match="outside the run folder"):
        bundle.export_public(run, run / "public")


def test_the_export_manifest_names_every_text_it_cut(tmp_path):
    """The excerpt policy bounds every long text, not only verified passages: the manifest names an evidence item
    whose observation was cut as it names one whose passage was, and the claims, hypotheses and result whose text an
    agent wrote at length. A replay's source run is named by its folder alone, as source_run is."""
    from variant2mechanism.v9.literature import PUBLIC_PASSAGE_LIMIT

    long = "A long observation that no export may carry whole. " * 40
    assert len(long) > PUBLIC_PASSAGE_LIMIT
    g = ClaimGraph(dev_case())
    tool_evidence(g, "annotation", "The variant lies in cCRE EH38E0000001.", tool="ccre_overlap",
                  about_elements=["EH38E0000001"])
    long_evidence = tool_evidence(g, "annotation", long, tool="ccre_overlap", about_elements=["EH38E0000001"])
    overlap = claim(g, [VARIANT], "overlaps", [ELEMENT], assertion_text="rs1427407 lies in the enhancer")
    long_claim = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", assertion_text=long)
    h = g.add_hypothesis(HypothesisDraft(title="The enhancer story", summary=long, required_claim_ids=[overlap],
                                         mechanism_class="regulatory"), "coordinator")
    g.set_result(RunResult(outcome="no_supported_explanation", stop_reason="converged", summary=long))
    saved = tmp_path / "runs" / "REQ-SAVED"
    run = write_run(g, tmp_path / "replay", extra={"replay_of": {"run_folder": str(saved), "status": "identical",
                                                                 "differences": 0}})
    manifest = bundle.load_bundle(bundle.export_public(run, tmp_path / "public")).manifest
    export = manifest["public_export"]
    assert export["evidence_text_cut"] == [long_evidence] and "passages_changed" not in export
    assert export["agent_text_cut"] == [long_claim, h, "result"]
    assert manifest["replay_of"] == {"run_folder": "REQ-SAVED", "status": "identical", "differences": 0}
