"""Discovery regressions use invented papers/variants, not the development case or its known factors."""

import json

from variant2mechanism.v9 import literature as lit
from variant2mechanism.v9 import progress
from variant2mechanism.v9.graph import ClaimGraph
from variant2mechanism.v9.mechanistic_gaps import gap_lines
from variant2mechanism.v9.schemas import Claim, Entity

from .test_evidence_adoption import observation_graph
from .test_literature_fakes import FakeHttp, case, records, runner, search, search_response
from .test_read_progress import reading

JATS = '''<article article-type="review-article"><front><article-meta>
<article-id pub-id-type="pmcid">PMC9900001</article-id></article-meta></front>
<body><sec><title>Regulation</title><p>The deletion of a regulatory region reduced expression
<xref ref-type="bibr" rid="arbitrary-id">8</xref>.</p><p>Other results
<xref ref-type="bibr" rid="other-id">2</xref>.</p></sec></body><back><ref-list>
<ref id="arbitrary-id"><label>8</label><element-citation><article-title>An invented primary experiment</article-title>
<pub-id pub-id-type="pmid">99000002</pub-id><pub-id pub-id-type="doi">10.5555/synthetic</pub-id>
</element-citation></ref><ref id="other-id"><label>2</label><mixed-citation>Unindexed paper without identifiers.</mixed-citation></ref>
</ref-list></back></article>'''


def test_bibliography_is_followable_but_never_an_extractable_result():
    article = lit.parse_jats(JATS, "europepmc_fulltext")
    assert article.sections[0].reference_ids == ["arbitrary-id"]
    assert article.references[0].pmid == "99000002"
    assert article.section("arbitrary-id") is None
    assert not any("invented primary" in s.text for s in article.sections)
    obs = lit._read_observations(article, ["reference 8"], [])
    ref = next(o for o in obs if o.get("kind") == "reference")
    assert ref["reference_id"] == "arbitrary-id" and ref["cited_by_locations"] == ["sec1/p1"]
    assert ref["doi"] == "10.5555/synthetic"
    assert "not experimental evidence" in obs[0]["reference_note"]
    assert len(json.dumps(obs, ensure_ascii=False, separators=(",", ":"))) <= lit.RETURN_LIMIT


def test_idless_reference_stays_a_discovery_pointer():
    article = lit.parse_jats(JATS, "europepmc_fulltext")
    obs = lit._read_observations(article, ["other-id"], [])
    ref = next(o for o in obs if o.get("kind") == "reference")
    assert ref["reference_id"] == "other-id"
    assert ref["pmid"] is None and "Unindexed paper" in ref["citation"]


def test_review_only_search_tries_one_bounded_nonreview_lane_and_records_provenance(tmp_path):
    base = records()["PMC9000002"]
    review = {**base, "pmid": "99000001", "pmcid": "PMC9900001", "pubTypeList": {"pubType": ["Review"]}}
    primary = {**base, "pmid": "99000002", "pmcid": "PMC9900002", "pubTypeList": {"pubType": ["Journal Article"]}}
    query = "rs12345678"
    url = lit.search_url(query, lit.DEFAULT_RESULTS)
    extra = lit.search_url(f"({query}) NOT PUB_TYPE:review", lit.MAX_RESULTS)
    http = FakeHttp({url: search_response([review]), extra: search_response([primary])})
    graph = ClaimGraph(case())
    call = search(runner(http, tmp_path), graph, query)
    assert http.calls == [url, extra]
    assert [o["pmid"] for o in call.observations] == ["99000002", "99000001"]
    raw = json.loads((tmp_path / call.raw_result_path).read_text())
    assert raw["discovery"]["query"] == f"({query}) NOT PUB_TYPE:review"
    assert graph.evidence == {} and call.evidence_ids == []


def test_failed_fallback_retains_review_and_marks_search_incomplete():
    review = {**records()["PMC9000002"], "pubTypeList": {"pubType": ["Review"]}}
    http = FakeHttp({lit.search_url("generic locus", lit.DEFAULT_RESULTS): search_response([review])})
    graph = ClaimGraph(case())
    call = search(runner(http), graph, "generic locus")
    assert len(http.calls) == 2 and call.retrieval_status == "incomplete"
    assert call.observations[0]["publication_type"] == "Review"
    assert not graph.evidence


def test_new_citation_pointer_is_progress_but_same_pointer_is_not():
    graph = observation_graph()
    q1, t1 = reading(graph, "activity")
    q2, t2 = reading(graph, "reference 8")
    ref = {"kind": "reference", "reference_id": "abc", "pmid": "99000002"}
    graph.tool_calls[t2].observations.append(ref)
    assert progress.read_state(graph, q1, [t1]) != progress.read_state(graph, q2, [t2])
    graph.tool_calls[t1].observations.append({**ref, "cited_by_locations": ["body/p1"]})
    assert progress.read_state(graph, q1, [t1]) == progress.read_state(graph, q2, [t2])


def test_gap_checks_distinguish_localisation_activity_and_mediation_without_creating_claims():
    graph = ClaimGraph(case())
    graph.entities = {"V": Entity(entity_id="V", kind="variant", label="variant"),
                      "E": Entity(entity_id="E", kind="element", label="region")}
    graph.claims = {"C1": Claim(claim_id="C1", subject_ids=["V"], object_ids=["E"], relation="overlaps",
                                proposed_by="coordinator"),
                    "C2": Claim(claim_id="C2", subject_ids=["V"], object_ids=["E"],
                                relation="alters_regulatory_activity", proposed_by="coordinator")}
    before = {k: c.model_dump() for k, c in graph.claims.items()}
    lines = "\n".join(gap_lines(graph, graph.claims))
    assert "localisation is not an allelic effect" in lines
    assert "HOW unresolved" in lines and "TF binding is optional" in lines
    assert "not proposed" in lines and "does not establish mediation" in lines
    assert {k: c.model_dump() for k, c in graph.claims.items()} == before


def test_public_search_export_drops_abstracts_in_all_discovery_lanes():
    raw = {"records": [{"abstract": "private text"}], "original_records": [{"abstractText": "private text"}],
           "discovery": {"records": [{"abstract": "private text"}]}}
    out = lit.public_raw({"tool_name": "literature_search"}, json.dumps(raw).encode(), [])
    assert b"private text" not in out


def test_numbered_reference_with_punctuation_and_no_id_can_be_found_by_label():
    article = lit.parse_jats(JATS.replace('<label>8</label>', '<label>8.</label>'), "ncbi_efetch")
    observations = lit._read_observations(article, ["reference 8"], [])
    assert observations[1]["reference_id"] == "arbitrary-id"


def test_many_references_and_long_paragraphs_keep_the_read_within_its_budget():
    sections = [lit.ArticleSection(location=f"sec1/p{i}", text="regulation " * 1000,
                                  reference_ids=[f"r{i}"]) for i in range(60)]
    refs = [lit.ArticleReference(reference_id=f"r{i}", title="title " * 50, citation="citation " * 60)
            for i in range(60)]
    article = lit.Article(route="europepmc_fulltext", access="full_text", sections=sections, references=refs)
    observations = lit._read_observations(article, ["regulation"], [])
    assert len(json.dumps(observations, ensure_ascii=False, separators=(",", ":"))) <= lit.RETURN_LIMIT
    assert observations[0]["references_total"] == 60
    assert observations[0]["references_shown"] <= 8
    assert observations[0]["passages_shown"] > 0


def test_body_bibliography_and_structured_external_identifiers_are_preserved():
    xml = JATS.replace('</body><back>', '<sec><title>References</title>')
    xml = xml.replace('</back></article>', '</sec></body></article>')
    xml = xml.replace('<pub-id pub-id-type="pmid">99000002</pub-id>',
                      '<ext-link xmlns:xlink="http://www.w3.org/1999/xlink" ext-link-type="pmid" '
                      'xlink:href="99000002"/>')
    article = lit.parse_jats(xml, "ncbi_efetch")
    assert len(article.references) == 2 and article.references[0].pmid == "99000002"
    assert not any("invented primary" in s.text for s in article.sections)


def test_subarticle_references_are_not_attributed_to_the_main_article():
    xml = JATS.replace('</article>', '<sub-article><back><ref-list><ref id="unrelated">'
                       '<label>1</label><mixed-citation>Unrelated citation</mixed-citation>'
                       '</ref></ref-list></back></sub-article></article>')
    article = lit.parse_jats(xml, "ncbi_efetch")
    assert {r.reference_id for r in article.references} == {"arbitrary-id", "other-id"}


def test_unread_leads_survive_rounds_and_retire_only_after_full_text_read():
    from variant2mechanism.v9.discovery import context_lines, unread_leads
    from variant2mechanism.v9.schemas import ToolCall

    graph = observation_graph()
    tid = graph.reserve_tool_call_id()
    graph.record_tool_call(ToolCall(tool_call_id=tid, tool_name="literature_search", execution_status="success",
        retrieval_status="records_found", requested_by="literature_investigator",
        query_parameters={"query": "invented locus"}, observations=[
            {"pmid": "99000001", "title": "Review", "publication_type": "Review"},
            {"pmid": "99000002", "pmcid": "PMC123", "title": "Primary candidate", "publication_type": "Article"}
        ]), [])
    assert unread_leads(graph)[0]['pmid'] == "99000002"
    assert 'NOT evidence' in context_lines(graph)[0]
    assert unread_leads(graph) == unread_leads(graph)
    _, t = reading(graph, "activity")
    graph.tool_calls[t].observations[0]["access"] = "abstract_only"
    assert any(x['pmid'] == '99000002' for x in unread_leads(graph))
    graph.tool_calls[t].observations[0]["access"] = "full_text"
    assert not any(x['pmid'] == '99000002' for x in unread_leads(graph))
    assert unread_leads(graph)[0]['pmid'] == '99000001'
