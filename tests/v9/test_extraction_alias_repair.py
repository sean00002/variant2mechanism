"""General source repair and identity-state contracts; all new catalogue/variant identities are invented."""

import copy

import pytest

from variant2mechanism.v9 import extraction_repair as repair
from variant2mechanism.v9 import literature as lit
from variant2mechanism.v9 import roles
from variant2mechanism.v9.graph import ClaimDraft, EntityRef, GraphRefusal
from variant2mechanism.v9.investigate import Engine, _Run
from variant2mechanism.v9.schemas import ToolCall
from variant2mechanism.v9.variant_identity import catalogue_identity, identity_lines, normalise_evidence

from .test_engine_literature import experiment
from .test_general_recovery import mapped_graph, paper
from .test_literature_extract import EMSA
from .test_literature_fakes import FakeHttp, read, routes, runner
from .test_resolution_recovery import answer_case


def catalogue(graph, *, base="A", gene="GENE1", build="GRCH37", pos=2345778):
    hit = {"gene": gene, "id": 987654, "name": "C87T", "aliases": ["-87C>T"]}
    detail = {"coordinates": {"referenceBuild": build, "chromosome": "7", "start": pos, "stop": pos,
                              "referenceBases": "G", "variantBases": base}}
    return catalogue_identity(hit, detail, graph)


def catalogue_call(graph, row):
    graph.tool_calls["T900002"] = ToolCall(tool_call_id="T900002", tool_name="civic_lookup", requested_by="code",
        charged_to="code", execution_status="success", retrieval_status="records_found", observations=[row])


def test_source_span_copies_whole_sentence_and_preserves_negation(tmp_path):
    call, article, rec = paper(tmp_path, result="The mutant C87T promoter did not increase luciferase activity. "
                              "A control construct increased luciferase activity in K562 cells.")
    text = article.sections[-1].text
    choice = repair.spans(text)[0]
    selected = repair.materialise(rec.model_copy(update={"passage": choice["selector"]}), article)
    assert selected.passage == text[:text.index(" A control")]
    assert "did not" in selected.passage
    # Cutting off the negative clause is not a selectable sentence.
    cut = f"@span:{text.index('increase')}:{text.index(' A control')}"
    with pytest.raises(lit.ExtractionRefused, match="whole-sentence"):
        repair.materialise(rec.model_copy(update={"passage": cut}), article)
    with pytest.raises(lit.ExtractionRefused, match="whole-sentence"):
        repair.materialise(rec.model_copy(update={"passage": "@span:0:99999"}), article)


def test_unknown_shorthand_survives_in_paper_scope_but_cannot_support_case(tmp_path):
    call, article, rec = paper(tmp_path, definition="A synthetic GENE1 promoter experiment.")
    graph = mapped_graph()
    ev = lit.evidence_from_experiment(rec, call, article)
    assert ev.data["variant_identity_status"] == "unresolved"
    assert ev.about_variants == ["paper:PMC9000007:C87T"]
    graph.tool_calls[call.tool_call_id] = call
    eid = graph.add_evidence(ev, "literature_investigator")
    cid = graph.add_claim(ClaimDraft(subjects=[EntityRef(kind="variant", label=graph.case.variant.key)],
        objects=[EntityRef(kind="element", label="GENE1 promoter reporter")], relation="alters_regulatory_activity",
        effect_allele="A", direction="increases", context=ev.context, assertion_text="Reporter activity increases"),
        "coordinator")
    with pytest.raises(GraphRefusal, match="unresolved, not verified different"):
        graph.link(cid, eid, "supports", "critic", "needs identity")
    assert graph.link(cid, eid, "context_only", "critic", "paper scope").stance == "context_only"


def test_exact_catalogue_alias_and_gene_verify_build_and_strand_without_guessing(tmp_path):
    call, article, rec = paper(tmp_path, definition="A synthetic GENE1 promoter experiment.")
    article = article.model_copy(update={"title": "GENE1 promoter experiments"})
    graph = mapped_graph()
    row = catalogue(graph)
    assert row["status"] == "verified_same"
    catalogue_call(graph, row)
    ev = lit.evidence_from_experiment(rec, call, article)
    mapped = normalise_evidence(ev, graph, article=article)
    assert mapped.about_variants == [graph.case.variant.key] and mapped.allele == "A"
    assert mapped.experiment.compared_allele == "T"
    assert mapped.data["variant_identity"]["source"].endswith("/987654")
    assert mapped.data["variant_identity_status"] == "verified_same"
    # A complementary name is NOT invented from the catalogue entry, nor is a numeric suffix a coordinate.
    wrong = ev.model_copy(update={"data": {**ev.data, "paper_variant_names": ["G87A"]}})
    assert normalise_evidence(wrong, graph, article=article) is wrong
    assert normalise_evidence(ev, graph, article=article.model_copy(update={"title": "GENE2 study"})) is ev


@pytest.mark.parametrize("kwargs,state", [({"base": "C"}, "verified_different"),
    ({"pos": 2345800}, "verified_different"), ({"build": "GRCH36"}, "unresolved")])
def test_wrong_allele_position_or_unsupported_build_never_becomes_same(kwargs, state):
    row = catalogue(mapped_graph(), **kwargs)
    assert row["status"] == state and row["placement"] is None


def test_catalogue_query_uses_verified_coordinates_for_bounded_snv_candidates(v9_cfg, tmp_path):
    from .test_adapters_tools import Session, live, run
    graph = mapped_graph()
    listing = {"data": {"browseVariants": {"nodes": [{"id": 987654, "name": "C87T",
               "aliases": [{"name": "-87C>T"}], "evidenceItemCount": 0}]}}}
    detail = {"data": {"variant": {"coordinates": catalogue(graph)["coordinates"]}}}
    session = Session(lambda m, u, b: (200, listing if "Browse" in b["query"] else detail))
    call = run(live(v9_cfg, tmp_path, session), graph, "civic_lookup", genes=["GENE1"])
    assert len(session.calls) == 2 and call.observations[0]["status"] == "verified_same"
    assert call.evidence_ids == []
    assert "C87T" in " ".join(identity_lines(graph))


def test_engine_repairs_failed_quote_against_original_read_once_without_new_tool(tmp_path):
    graph, raw = answer_case(nested=False)
    answer = raw["answers"][0]
    qid = answer["question_id"]
    graph.questions[qid].route = "literature"
    tool = read(runner(FakeHttp(routes()), tmp_path), graph, ["GATA1"], pmcid="PMC9000001")
    x = experiment(EMSA, "sec1.1/p1", source="PMID:90000001", pmcid="PMC9000001")
    x.update(intervention="EMSA with K562 nuclear extract", endpoint="GATA1 binding", comparator="G allele probe",
             direction="increases", result="T probe binds more strongly", tissue_or_cell="K562", about_tfs=["GATA1"],
             about_genes=[], about_elements=[], about_variants=["rs1427407"], manipulated="allele", compared_allele="T")
    answer.update(experiments=[{**x, "passage": "A fabricated quotation that does not occur in this paper."}],
                  proposed_updates=[], follow_up_actions=[], tool_call_ids=[tool.tool_call_id], status="answered")
    engine = Engine.__new__(Engine)
    engine.run_dir = tmp_path
    engine._blocker = lambda *a, **kw: None
    st = _Run(graph, 0)
    st.question_calls[qid] = [tool.tool_call_id]
    original_calls = set(graph.tool_calls)
    seen = []
    def ask(state, route, ids, step, extra=""):
        seen.append((step, extra))
        result = copy.deepcopy(raw)
        if step == "repair":
            assert "sec1.1/p1" in extra and tool.tool_call_id in extra and "fabricated" in extra
            source = lit.load_article(tmp_path, tool)
            section = next(s for s in source.sections if s.location == "sec1.1/p1")
            selected = repair.spans(section.text)[0]["selector"]
            result["answers"][0]["experiments"] = [{**x, "passage": selected}]
        return roles.V9Investigate.model_validate(result)
    engine._ask_investigator = ask
    engine._answer(st, "literature", [qid])
    assert [s for s, _ in seen] == ["answer", "repair"]
    assert len([e for e in graph.evidence.values() if e.origin == "literature"]) == 1
    assert set(graph.tool_calls) == original_calls
    engine._repair_extractions(st, 0)
    assert len(seen) == 2


def test_repair_cannot_spend_final_reserved_calls(tmp_path):
    graph, raw = answer_case(nested=False)
    qid = raw["answers"][0]["question_id"]
    ex = experiment(EMSA, "sec1.1/p1")
    graph.log("refuse_update", "literature_investigator", "bad quote", details={"kind": "add_evidence",
        "question_id": qid, "experiment": roles.experiment_record(roles.V9Experiment.model_validate(ex)).model_dump()})
    engine = Engine.__new__(Engine)
    engine._blocker = lambda *a, **kw: "budget_model_calls"
    engine._ask_investigator = lambda *a, **kw: pytest.fail("must not send a model request")
    engine._repair_extractions(_Run(graph, 0), 0)
    assert graph.questions[qid].status == "deferred"


def test_unchanged_abstract_is_a_repeated_read_but_new_fulltext_is_not():
    from variant2mechanism.v9.progress import read_state
    graph, raw = answer_case(nested=False)
    qid = raw["answers"][0]["question_id"]
    graph.tool_calls["T1"] = ToolCall(tool_call_id="T1", tool_name="literature_read", requested_by="code",
        execution_status="success", retrieval_status="records_found", observations=[
            {"kind": "article", "pmid": "991111", "access": "abstract_only"},
            {"kind": "passage", "location": "abstract/p1", "text": "An observed result."}])
    first = read_state(graph, qid, ["T1"])
    assert first is not None
    graph.tool_calls["T1"].observations.append({"kind": "passage", "location": "results/p1", "text": "A new assay."})
    second = read_state(graph, qid, ["T1"])
    assert not second[1] <= first[1]
