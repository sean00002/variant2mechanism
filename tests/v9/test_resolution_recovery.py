"""Partial molecular support is not chain completion; semantic claim errors do not destroy verified assays."""
import copy

import pytest

from variant2mechanism.agent.schemas import SchemaCheckError
from variant2mechanism.v9 import roles
from variant2mechanism.v9.graph import ClaimGraph
from variant2mechanism.v9.investigate import Engine, _Run
from variant2mechanism.v9.resolution import support_summary

from .test_engine_compare import binding, hypothesis, regulates
from .test_engine_literature import experiment
from .test_investigator_claim_application import answer_case
from .test_literature_extract import EMSA
from .test_literature_fakes import FakeHttp, case, read, routes, runner


def test_optional_molecular_support_is_visible_without_promoting_a_chain():
    g = ClaimGraph(case())
    bind, reg = binding(g, 'TFX'), regulates(g, 'GENE1')
    hid = hypothesis(g, [reg], 'Unsettled regulatory mechanism')
    g.hypotheses[hid].claim_ids.append(bind)
    before = g.to_state().model_dump(mode='json')
    s = support_summary(g)
    assert s['molecular_label'] == 'Supported partial mechanism'
    assert s['supported_molecular_claim_ids'] == [bind]
    assert s['required_link_status'] == 'unresolved'
    assert s['required_gaps'][hid] == [reg]
    assert g.to_state().model_dump(mode='json') == before


def test_required_link_completion_is_not_automatically_disease_mediation():
    g = ClaimGraph(case())
    bind = binding(g, 'TFX')
    hid = hypothesis(g, [bind], 'Binding only')
    s = support_summary(g)
    assert s['supported_required_path_ids'] == [hid]
    assert 'molecular-only endpoint is not disease mediation' in s['note']


@pytest.mark.parametrize('change', ['dependency', 'context_only', 'prediction', 'superseded'])
def test_resolution_does_not_upgrade_weak_or_invalid_support(change):
    g = ClaimGraph(case())
    bind = binding(g, 'TFX')
    c = g.claims[bind]
    if change == 'dependency':
        c.dependency_flag = 'unsupported_due_to_dependency'
    elif change == 'context_only':
        c.evidence_links[0].stance = 'context_only'
    elif change == 'prediction':
        g.evidence[c.evidence_links[0].evidence_id].evidence_class = 'prediction'
    else:
        c.superseded_by = 'C99'
    assert not support_summary(g)['supported_molecular_claim_ids']


def test_bad_claim_is_refused_but_a_valid_sibling_is_applied():
    g, raw = answer_case()
    bad = copy.deepcopy(raw['answers'][0]['proposed_updates'][0])
    bad['new_claim']['key'] = 'bad_factor'
    bad['new_claim']['objects'][0]['kind'] = 'gene'
    raw['answers'][0]['proposed_updates'].insert(0, bad)
    qid = raw['answers'][0]['question_id']
    g.questions[qid].route = 'literature'
    parsed = roles.V9Investigate.model_validate(raw)
    roles.investigate_check(g, 'literature', [qid], {})(parsed)
    Engine.__new__(Engine)._apply_answers(_Run(g, 0), 'literature', parsed, 'extract')
    assert g.claims['C2'].assessment == 'supported_in_scope'
    assert len(g.claims) == 2
    qid = raw['answers'][0]['question_id']
    assert g.questions[qid].status == 'deferred'
    assert 'tf object' in g.questions[qid].remaining_gap
    assert any(e.details.get('kind') == 'invalid_proposal' for e in g.events)


def test_invalid_claim_and_dependent_link_do_not_discard_a_verified_experiment(tmp_path):
    g, raw = answer_case(nested=False)
    answer = raw['answers'][0]
    qid = answer['question_id']
    g.questions[qid].route = 'literature'
    call = read(runner(FakeHttp(routes()), tmp_path), g, ['GATA1'], pmcid='PMC9000001')
    answer['tool_call_ids'] = [call.tool_call_id]
    x = experiment(EMSA, 'sec1.1/p1', source='PMID:90000001', pmcid='PMC9000001')
    x.update(intervention='EMSA with K562 nuclear extract', endpoint='GATA1 binding',
             comparator='G allele probe', direction='increases', result='T probe binds more strongly',
             tissue_or_cell='K562', about_tfs=['GATA1'], about_genes=[], about_elements=[],
             about_variants=['rs1427407'], manipulated='allele', compared_allele='T')
    answer['experiments'] = [x]
    answer['proposed_updates'][0]['new_claim']['objects'][0]['kind'] = 'gene'
    parsed = roles.V9Investigate.model_validate(raw)
    roles.investigate_check(g, 'literature', [qid], {})(parsed)
    assert set(parsed._proposal_errors) == {(0, 0), (0, 1)}
    engine = Engine.__new__(Engine)
    engine.run_dir = tmp_path
    engine._apply_answers(_Run(g, 0), 'literature', parsed, 'extract')
    accepted = [e for e in g.evidence.values() if e.origin == 'literature']
    assert len(accepted) == 1 and accepted[0].evidence_class == 'binding_assay'
    assert accepted[0].allele == 'T' and accepted[0].direction == 'increases'
    assert len(g.claims) == 1 and not g.claims['C1'].evidence_links
    assert g.questions[qid].status == 'deferred'


def test_unknown_question_still_rejects_the_entire_envelope():
    g, raw = answer_case()
    raw['answers'][0]['question_id'] = 'Q999'
    with pytest.raises(SchemaCheckError, match='answer only the questions given'):
        roles.investigate_check(g, 'literature', ['Q1'], {})(roles.V9Investigate.model_validate(raw))


def test_native_html_and_markdown_show_both_resolution_axes(tmp_path):
    from variant2mechanism.v9 import bundle, report
    from variant2mechanism.v9.schemas import RunResult

    from .test_report_support import write_run

    g = ClaimGraph(case())
    bind, reg = binding(g, 'TFX'), regulates(g, 'GENE1')
    hid = hypothesis(g, [reg], 'Regulation not yet established')
    g.hypotheses[hid].claim_ids.append(bind)
    g.set_result(RunResult(outcome='no_supported_explanation', stop_reason='converged'), 'code')
    p = tmp_path / 'run'
    write_run(g, p)
    b = bundle.load_bundle(p)
    for rendered in (report.render_html(b), report.render_markdown(b)):
        assert 'Supported partial mechanism' in rendered
        assert 'Complete mechanism chain unresolved' in rendered
        assert 'No supported explanation' in rendered
    assert g.result.outcome == 'no_supported_explanation'
