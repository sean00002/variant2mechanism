"""Bounded Open Targets requests and honest coverage on truncation/failure."""

from copy import deepcopy

from variant2mechanism.v9.adapters import OT_MAX_PAGES, OT_PAGE_SIZE
from variant2mechanism.v9.graph import ClaimGraph

from .test_adapters_tools import DEV, Session, case, evidence, live, run


def page(index, count, *, nested_count=1):
    rows = [{"studyLocusId": f"locus-{i}", "studyId": f"study-{i}",
             "study": {"id": f"study-{i}", "traitFromSource": "Fetal hemoglobin levels"},
             "locus": {"rows": [{"variant": {"id": "2_60490908_T_G"}, "posteriorProbability": 0.2}]},
             "l2GPredictions": {"count": nested_count, "rows": [{"target": {"approvedSymbol": "GENE1"},
                                                                "score": 0.3}]},
             "colocalisation": {"count": 0, "rows": []}}
            for i in range(index * OT_PAGE_SIZE, min((index + 1) * OT_PAGE_SIZE, count))]
    return {"data": {"meta": {"dataVersion": {"year": "26", "month": "09"},
                              "apiVersion": {"x": "26", "y": "9", "z": "0"}},
                     "variant": {"credibleSets": {"count": count, "rows": rows}}}}


def test_scoped_pagination_reads_second_page_and_keeps_scores_per_study(v9_cfg, tmp_path):
    session = Session(lambda m, u, b: (200, page(b["variables"]["index"], 39)))
    graph = ClaimGraph(case(DEV))
    call = run(live(v9_cfg, tmp_path, session), graph, "credible_sets_l2g", trait="fetal haemoglobin")
    assert call.retrieval_status == "records_found"
    assert [c["json"]["variables"]["index"] for c in session.calls] == [0, 1]
    assert "size: 25" in session.calls[0]["json"]["query"]
    assert "locus(variantIds: $ids, page: {index: 0, size: 1})" in session.calls[0]["json"]["query"]
    assert len({e.independence_group for e in evidence(graph, call)}) == 39


def test_unread_sets_cannot_be_reported_as_no_records(v9_cfg, tmp_path):
    session = Session(lambda m, u, b: (200, page(b["variables"]["index"], 100)))
    graph = ClaimGraph(case(DEV))
    call = run(live(v9_cfg, tmp_path, session), graph, "credible_sets_l2g", trait="unrelated trait")
    assert len(session.calls) == OT_MAX_PAGES
    assert call.retrieval_status == "incomplete" and not call.evidence_ids
    assert call.observations[0]["read"] == OT_PAGE_SIZE * OT_MAX_PAGES


def test_nested_gene_truncation_is_explicit(v9_cfg, tmp_path):
    session = Session(lambda m, u, b: (200, page(0, 1, nested_count=12)))
    graph = ClaimGraph(case(DEV))
    call = run(live(v9_cfg, tmp_path, session), graph, "credible_sets_l2g",
               trait="fetal haemoglobin", gene="NOT_RETURNED")
    assert call.retrieval_status == "incomplete"
    assert next(o for o in call.observations if o["record"] == "nested_coverage")["truncated"] == [
        {"study_locus_id": "locus-0", "field": "l2GPredictions", "read": 1, "count": 12}]


def test_later_page_failure_retains_partial_evidence(v9_cfg, tmp_path):
    error = {"errors": [{"message": "Query is too expensive"}]}
    session = Session(lambda m, u, b: (400, deepcopy(error)) if b["variables"]["index"] else (200, page(0, 39)))
    graph = ClaimGraph(case(DEV))
    call = run(live(v9_cfg, tmp_path, session), graph, "credible_sets_l2g", trait="fetal haemoglobin")
    assert call.retrieval_status == "incomplete" and call.evidence_ids
    assert call.observations[0]["read"] == 25


def test_first_page_api_error_is_not_biological_absence(v9_cfg, tmp_path):
    session = Session(lambda m, u, b: (400, {"errors": [{"message": "Query is too expensive"}]}))
    graph = ClaimGraph(case(DEV))
    call = run(live(v9_cfg, tmp_path, session), graph, "credible_sets_l2g", trait="fetal haemoglobin")
    assert call.execution_status != "success" and not call.evidence_ids
    assert call.retrieval_status != "no_records_found"
