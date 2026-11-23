"""Literature extraction in the engine (contract C4 over C3), with a stub of the literature module.

The triage call asks for a read; the engine runs it at once and makes one extraction call (with the `extraction`
role key, the summariser by default). Each extracted experiment goes through literature.find_read (the read of the
article it cites), literature.load_article and literature.evidence_from_experiment (given the graph's HGNC resolver),
then graph.add_evidence; a refused experiment is logged with its reason, and an update that names it by
experiment_index is refused too. The strict experiment carries what the experiment manipulated and the elements and
variants it concerns (CORE-CHANGES-2 C2-8, CORE-CHANGES-3 C3-1), so a claim about element E can take it, while an
assay of another variant, an allele comparison that names no variant, or a TF knockdown never bears on what the case
variant's alleles do (C3-1, C3-2). Article text is stipulated, not biological evidence.
"""

import copy
import json
import sys
import types
from pathlib import Path

from variant2mechanism.agent.llm import strict_schema
from variant2mechanism.v9 import roles
from variant2mechanism.v9.fixtures import Fixture
from variant2mechanism.v9.schemas import ContextScope, Evidence

from .test_engine_support import events, run_fixture

PASSAGE = "Activating element E increased gene X expression in context X cells."
ARTICLE = f"Methods were as before. {PASSAGE} The effect was reproducible."


def experiment(passage: str, location: str, source: str = "PMID:100", pmcid: str | None = "PMC100") -> dict:
    return {"source_id": source, "pmcid": pmcid, "doi": None, "publication_type": "research article",
            "access": "full_text", "location": location, "passage": passage, "organism": "human",
            "tissue_or_cell": "context X", "treatment": "", "genotype_or_allele": "",
            "intervention": "activation of element E", "endpoint": "gene X expression", "comparator": "control",
            "result": "Activating element E increased gene X expression in context X.", "direction": "increases",
            "scope_supports": "element E regulates gene X in context X", "scope_does_not_test": "the variant's allele",
            "about_tfs": [], "about_genes": ["X"], "about_elements": ["E"], "about_traits": [], "about_variants": [],
            "manipulated": "element", "compared_allele": None, "authors_hypothesis_vs_result": "result"}


def attach(index: int, suggested: str | None, claim: str = "C1") -> dict:
    return {"kind": "attach_evidence", "claim_id": claim, "base_version": 1 if suggested else None,
            "evidence_id": None, "experiment_index": index, "stance": "supports", "applicability": None,
            "rationale": "a matched activation of element E raises gene X in context X", "limitations": [],
            "suggested_assessment": suggested, "new_claim": None}


def answer(status: str, experiments=(), updates=(), follow_up=()) -> dict:
    return {"question_id": "Q1", "status": status, "answer_summary": "a primary study tests element E on gene X",
            "claim_ids": ["C1"], "tool_call_ids": [], "experiments": list(experiments),
            "proposed_updates": list(updates), "remaining_gap": "", "next_question": "",
            "follow_up_actions": list(follow_up)}


ELEMENT = {"kind": "element", "label": "E", "canonical_id": "SYN:E", "members": []}
FIXTURE = Fixture.model_validate({
    "description": "Literature extraction (engine test): stipulated, not biological data.",
    "case": {"case_id": "SYN-5", "variant": {"chrom": "SYN", "pos": 5, "ref": "A", "alt": "G"}},
    "tools": {
        "literature_search": {
            "spec": {"route": "literature", "assemblies": [], "description": "Synthetic search.",
                     "params": {"query": {"type": "str", "required": True}}},
            "responses": [{"params": {"query": "element E gene X"},
                           "observations": [{"pmid": "100", "pmcid": "PMC100", "title": "A stipulated study"}]}]},
        "literature_read": {
            "spec": {"route": "literature", "assemblies": [], "description": "Synthetic full-text read.",
                     "params": {"pmcid": {"type": "str", "required": True}, "focus": {"type": "list[str]"}},
                     "fulltext_params": ["pmcid"]},
            "responses": [{"params": {"pmcid": "PMC100", "focus": ["gene X"]},
                           "observations": [{"location": "sec1/p1", "text": ARTICLE}]}]}},
    "roles": {
        "coordinator": [
            {"directions": ["literature-led"], "inferred_candidates": [], "fourth_active_reason": None,
             "reactivate": [],
             "hypotheses": [{
                 "key": "h", "title": "Element E raises gene X", "summary": "", "mechanism_class": "regulatory",
                 "endpoint": "molecular", "context": {"label": "context X", "species": "human", "condition": None},
                 "activate": True, "deferral_reason": None, "revisit_trigger": None,
                 "reason_kind": "literature_report", "reason_detail": "a stipulated study may test element E",
                 "member_alternatives": [], "missing_links": [], "assumptions": [], "replaces": None,
                 "reuse_claims": [],
                 "claims": [{"key": "reg", "subjects": [ELEMENT], "relation": "regulates",
                             "objects": [{"kind": "gene", "label": "X", "canonical_id": None, "members": []}],
                             "direction": "increases", "effect_allele": None,
                             "context": {"label": "context X", "species": "human", "condition": None},
                             "assertion_text": "Activating element E increases gene X in context X",
                             "required": True, "depends_on": [], "initial_links": []}]}],
             "questions": [{"text": "Has a perturbation of element E been tested on gene X?", "route": "literature",
                            "target_claims": ["reg"], "hypotheses": ["h"],
                            "rubric": {"consequence": "high", "discrimination": "high", "applicability": "high",
                                       "cost": "low"},
                            "possible_outcomes": ["a matched perturbation", "nothing found"],
                            "actions": [{"tool": "literature_search", "params_json": '{"query": "element E gene X"}',
                                         "purpose": "find a primary study"}]}]},
            {"hypothesis_updates": [], "assessments": [], "questions": [],
             "stop": {"stop": True, "reason": "the study answers the question"}}],
        "literature_investigator": [
            {"answers": [answer("needs_follow_up", follow_up=[
                {"tool": "literature_read", "params_json": '{"pmcid": "PMC100", "focus": ["gene X"]}',
                 "purpose": "read the primary study"}])]},
            {"answers": [answer("answered", [experiment(PASSAGE, "sec1/p1"),
                                             experiment("A sentence that the article does not contain.", "sec1/p2"),
                                             experiment(PASSAGE, "sec1/p1", source="PMID:999", pmcid=None)],
                                [attach(0, "supported_in_scope"), attach(1, None), attach(2, None)])]}],
        "critic": [
            {"challenges": [], "passage_checks": [], "activation_flags": [], "reportable_ids": ["H1"],
             "consequential": False},
            {"comparisons": [], "outcome": {"category": "leading_explanation", "leading_ids": ["H1"],
                                            "summary": "a matched activation supports the link",
                                            "weakest_links": [], "next_experiments": []}}]}})

CLASS_OF = {"tf": "perturbation", "gene": "perturbation", "element": "perturbation", "allele": "binding_assay",
            "none": "occupancy"}


def literature_stub(calls: list, resolvers: list | None = None) -> types.SimpleNamespace:
    """Contract C3 in miniature: find the read of the cited article (by PMCID or PMID), load the article it saved,
    refuse a passage it does not contain. The Evidence carries what the record names (TFs, genes, elements and
    variants, as evidence_from_experiment copies them) and, for an allele comparison, the compared allele; `resolvers`
    collects the resolver each call was given."""

    class ExtractionRefused(Exception):
        def __init__(self, reason: str):
            super().__init__(reason)
            self.reason = reason

    def find_read(graph, record):
        cited = {record.pmcid, record.source_id.removeprefix("PMID:")} - {None}
        reads = [t for t in graph.tool_calls.values() if t.execution_status == "success" and t.read_article
                 and cited & {t.read_article, *t.article_ids}]
        if not reads:
            raise ExtractionRefused(f"no literature read in this run returned {record.source_id}")
        return reads[0]

    def load_article(run_dir, call):
        calls.append((Path(run_dir), call.tool_call_id, call.read_article))
        raw = json.loads((Path(run_dir) / call.raw_result_path).read_text())
        return {"pmcid": call.read_article, "text": " ".join(o["text"] for o in raw["observations"])}

    def evidence_from_experiment(record, call, article, *, resolver=None):
        if resolvers is not None:
            resolvers.append(resolver)
        if record.passage not in article["text"]:
            raise ExtractionRefused("the passage is not in the article")
        return Evidence(evidence_class=CLASS_OF[record.manipulated],
                        source_ids=[record.source_id, f"PMCID:{article['pmcid']}"],
                        observed_result=record.result, direction=record.direction, about_tfs=record.about_tfs,
                        about_genes=record.about_genes, about_elements=record.about_elements,
                        about_variants=record.about_variants, allele=record.compared_allele,
                        context=ContextScope(label=record.system.tissue_or_cell, source="evidence"),
                        independence_group=f"{record.source_id}#{record.intervention}/{record.endpoint}",
                        origin="literature", access="full_text", experiment=record,
                        retrieval_ref=call.tool_call_id)

    return types.SimpleNamespace(ExtractionRefused=ExtractionRefused, find_read=find_read, load_article=load_article,
                                 evidence_from_experiment=evidence_from_experiment)


def test_extracted_experiments_become_evidence_and_refusals_are_logged(v9_cfg, tmp_path, monkeypatch):
    calls: list = []
    resolvers: list = []
    monkeypatch.setitem(sys.modules, "variant2mechanism.v9.literature", literature_stub(calls, resolvers))
    result, scripted, caller = run_fixture(v9_cfg, FIXTURE, tmp_path)
    g = result.graph
    read = next(t for t in g.tool_calls.values() if t.tool_name == "literature_read")
    assert read.read_article == "PMC100" and read.requested_by == "literature_investigator"
    assert calls == [(tmp_path / "run", read.tool_call_id, "PMC100")] * 3  # two experiments + repair source check
    # every extraction is given the graph's HGNC resolver (a paper may name a TF or gene by a previous symbol)
    assert len(resolvers) == 2 and g.resolver is not None and all(r is g.resolver for r in resolvers)

    extracted = [e for e in g.evidence.values() if e.origin == "literature"]
    assert len(extracted) == 1 and extracted[0].experiment.passage == PASSAGE
    assert extracted[0].retrieval_ref == read.tool_call_id
    record = extracted[0].experiment                             # the strict fields reach the record (C2-8, C3-1)
    assert (record.about_elements, record.manipulated, record.compared_allele, record.about_variants) == (
        ["E"], "element", None, [])
    link = g.claims["C1"].evidence_links[0]
    assert link.evidence_id == extracted[0].evidence_id and g.claims["C1"].assessment == "supported_in_scope"

    refusals = [e.concise_reason for e in events(result, "refuse_update") if e.role == "literature_investigator"]
    assert any("experiment 1" in r and "the passage is not in the article" in r for r in refusals)
    assert any("experiment 1 of the answer to Q1 was not accepted" in r for r in refusals)
    assert any("experiment 2" in r and "no literature read in this run returned PMID:999" in r for r in refusals)
    assert g.questions["Q1"].status == "deferred"  # the stub has no source sections to repair the refused quote

    # triage, then one extraction call: with the extraction key (summariser) and the article inside <data>
    extract = [b for b in scripted.sent if b["messages"][1]["content"].startswith(
        "Role: literature_investigator; stage: extract")]
    assert len(extract) == 1 and extract[0]["max_tokens"] == v9_cfg["llm"]["max_tokens"]["summariser"]
    assert PASSAGE in extract[0]["messages"][1]["content"].split("<data>", 2)[1]
    assert caller.usage["literature_investigator"]["calls"] == 2
    assert g.result.outcome == "leading_explanation"


# --- which variant an experiment tested (C3-1) and what a perturbation can say about the alleles (C3-2) -----------

LD_PARTNER = "In EMSA, TFA bound the G allele of rs9000077 more strongly than the A allele."
CASE_EMSA = "In EMSA, TFA bound the G allele of SYN:5 more strongly than the A allele."
UNNAMED_EMSA = "In a second EMSA, TFA bound the G probe more strongly than the A probe."
KNOCKDOWN = "Knockdown of TFA lowered the activity of element E in context X cells."
ALLELE_ARTICLE = f"Results. {LD_PARTNER} {CASE_EMSA} {UNNAMED_EMSA} {KNOCKDOWN}"
V5 = {"kind": "variant", "label": "V5", "canonical_id": None, "members": []}
TFA = {"kind": "tf", "label": "TFA", "canonical_id": None, "members": []}


def assay(passage: str, *, manipulated: str, variants: list[str], allele: str | None, endpoint: str,
          direction: str = "increases") -> dict:
    return {**experiment(passage, "sec2/p1"), "intervention": "EMSA with both alleles" if manipulated == "allele"
            else "TFA knockdown", "endpoint": endpoint, "result": passage, "direction": direction,
            "scope_supports": "as stated", "scope_does_not_test": "the endogenous locus", "about_tfs": ["TFA"],
            "about_genes": [], "about_elements": [], "about_variants": variants, "manipulated": manipulated,
            "compared_allele": allele}


def allele_fixture() -> Fixture:
    """H1: V5 alters TFA binding (C1, required) and the activity of element E (C2). The paper reports an EMSA of a
    nearby variant, an EMSA of the case variant, an allele comparison that names no variant, and a TF knockdown."""
    base = FIXTURE.model_dump(mode="json")
    sketch = copy.deepcopy(base["roles"]["coordinator"][0]["hypotheses"][0])
    sketch.update(key="h", title="V5 changes TFA binding and element E activity", mechanism_class="tf_binding",
                  endpoint="molecular", context=None, reason_kind="literature_report",
                  reason_detail="a stipulated EMSA may compare the two alleles of V5", claims=[
                      {"key": "bind", "subjects": [V5], "relation": "alters_binding", "objects": [TFA],
                       "direction": "increases", "effect_allele": None, "context": None,
                       "assertion_text": "The G allele of V5 binds TFA more than the A allele", "required": True,
                       "depends_on": [], "initial_links": []},
                      {"key": "act", "subjects": [V5], "relation": "alters_regulatory_activity",
                       "objects": [ELEMENT], "direction": "increases", "effect_allele": None, "context": None,
                       "assertion_text": "The G allele of V5 raises the activity of element E", "required": False,
                       "depends_on": [], "initial_links": []}])
    propose = {**base["roles"]["coordinator"][0], "hypotheses": [sketch]}
    propose["questions"][0].update(text="Has an EMSA compared the two alleles of V5?", target_claims=["bind", "act"])
    extract = answer("answered", [
        assay(LD_PARTNER, manipulated="allele", variants=["rs9000077"], allele="G", endpoint="TFA binding"),
        assay(CASE_EMSA, manipulated="allele", variants=["SYN:5"], allele="G", endpoint="TFA binding"),
        assay(UNNAMED_EMSA, manipulated="allele", variants=[], allele="G", endpoint="TFA binding"),
        assay(KNOCKDOWN, manipulated="tf", variants=[], allele=None, endpoint="element E activity",
              direction="decreases")],
        [attach(0, None), attach(1, None), attach(2, None), attach(3, None, claim="C2")])
    base["tools"]["literature_read"]["responses"][0]["observations"] = [{"location": "sec2/p1",
                                                                        "text": ALLELE_ARTICLE}]
    base["roles"].update(
        coordinator=[propose, base["roles"]["coordinator"][1]],
        literature_investigator=[base["roles"]["literature_investigator"][0], {"answers": [extract]}],
        critic=[base["roles"]["critic"][0], {"comparisons": [], "outcome": {
            "category": "no_supported_explanation", "leading_ids": [], "summary": "binding is linked, not assessed",
            "weakest_links": [], "next_experiments": []}}])
    return Fixture.model_validate(base)


def test_an_assay_of_another_variant_or_a_tf_knockdown_never_bears_on_the_case_alleles(v9_cfg, tmp_path,
                                                                                         monkeypatch):
    """The strict experiment names the variant it tested (about_variants, required, may be empty); the graph then
    refuses an EMSA of a nearby variant, an allele comparison that names no variant, and a TF knockdown offered as
    support for what the case variant's alleles do, and accepts the EMSA that names the case variant."""
    monkeypatch.setitem(sys.modules, "variant2mechanism.v9.literature", literature_stub([]))
    result, scripted, _ = run_fixture(v9_cfg, allele_fixture(), tmp_path)
    g = result.graph
    by_passage = {e.experiment.passage: e for e in g.evidence.values() if e.origin == "literature"}
    assert set(by_passage) == {LD_PARTNER, CASE_EMSA, UNNAMED_EMSA, KNOCKDOWN}        # all four extracted
    assert by_passage[LD_PARTNER].about_variants == ["rs9000077"]                     # as the passage names it
    assert by_passage[CASE_EMSA].experiment.about_variants == ["SYN:5"]
    assert g.claim_frame("C1") == "case" and g.claim_frame("C2") == "case"

    linked = [(x.evidence_id, x.stance, x.strength) for x in g.claims["C1"].evidence_links]
    assert linked == [(by_passage[CASE_EMSA].evidence_id, "supports", "direct")]       # only the case variant's EMSA
    assert g.claims["C2"].evidence_links == []
    refusals = [e.concise_reason for e in events(result, "refuse_update") if e.role == "literature_investigator"]
    assert any("is about rs9000077, not the case variant" in r for r in refusals)
    assert any("compares alleles but names no variant" in r for r in refusals)
    assert any("a TF perturbation does not test what the variant's alleles do" in r for r in refusals)

    # later packets show the variant each item is about
    plan = next(p for p in scripted.packets() if p.startswith("Role: coordinator; stage: plan"))
    assert "variants SYN:5" in plan and "variants rs9000077" in plan


def test_the_strict_experiment_and_the_prompts_ask_which_variant_was_tested():
    schema = json.dumps(strict_schema(roles.V9Investigate))
    assert "about_variants" in roles.V9Experiment.model_fields and roles.V9Experiment.model_fields[
        "about_variants"].is_required()
    assert "the variant(s) the experiment tested" in schema
    record = roles.experiment_record(roles.V9Experiment.model_validate(
        {**experiment(PASSAGE, "sec1/p1"), "about_variants": [" rs9000077 ", "", "chr1:100  A>G"]}))
    assert record.about_variants == ["rs9000077", "chr1:100 A>G"]
    literature = " ".join(roles.prompt("investigator_literature").split())
    for rule in ("about_variants", "must name the variant", "never tests an element or an allele",
                 "not from the Introduction or Discussion", "Keep any negation", "only when the paper names that rsID",
                 "loss-of-function",
                 # what literature.evidence_from_experiment keeps (C3-1): the passage's own variant, the one variant of
                 # a one-variant paper, one variant per allele comparison, positions as GRCh38
                 "When the passage names a variant, name that one", "a passage need not repeat it",
                 "one experiment per variant", "preserve paper coordinates and strand"):
        assert rule in literature, rule
    rules = " ".join(roles.prompt("rules").split())
    assert "Evidence about one variant never supports or contradicts a claim about another" in rules
    assert "A TF or gene perturbation (knockdown, knockout, overexpression) cannot support or contradict" in rules
    matrix = roles.class_matrix_text()
    assert "a TF or gene perturbation (knockdown, knockout, overexpression) is context only" in matrix
    assert "for alters_binding, alters_regulatory_activity and alters_rna claims" in matrix
