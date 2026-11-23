"""Core contract additions after the stage-2 reviews, each tested as behaviour and as the scientific invariant it keeps.

- full-text reads: a read counts only when it returned the article, and one article is one read whichever identifier
  (PMID, PMCID, DOI) requested it, so a re-read is never refused at the hard cap and never counted twice;
- one_of parameter groups: exactly one of each group, refused before anything runs;
- the engine_error stop reason;
- inferred candidates are stored on the case, never as supplied input;
- the display rule is a pure function of a claim and the evidence its links name;
- variant types from the alleles;
- what a literature experiment is about (elements, what it manipulated, the compared allele);
- the case variant's rsID found by code, and the elements code places over the variant;
- a claim about what an element does needs evidence that names that element.

Round 3 (CORE-CHANGES-3):
- which variant evidence is about (about_variants): evidence about one variant never supports or contradicts a claim
  about another, and allele-comparing evidence must say whose alleles it compared;
- a TF or gene perturbation never tests what the variant's alleles do, and an experiment that compares no alleles is at
  most indirect for a claim that they differ;
- a canonical id naming the case variant (alias rsID, chrom:pos) is the case variant;
- the public claim frame;
- a code rejection whose contradiction was withdrawn is reinstated as deferred, once;
- one sketched-groups rule, in graph.py.

Biological cases use the development variant rs1427407 (chr2:60490908 T>G); symbols, elements, articles and
observations are stipulated for the tests and are not claims about that variant. One round-3 test replays the
motivating example of C3-1 (rs12740374 and an LD partner, rs629301) as plumbing, with stipulated observations.
"""

import inspect
import json
from typing import get_args

import pytest
from pydantic import ValidationError

from variant2mechanism.v9 import bundle, compare
from variant2mechanism.v9 import graph as graph_module
from variant2mechanism.v9.graph import (
    ClaimDraft,
    ClaimGraph,
    EntityRef,
    GraphRefusal,
    GraphState,
    HypothesisChanges,
    HypothesisDraft,
    article_key,
    display_of,
    hypothesis_versions,
    sketched_groups,
)
from variant2mechanism.v9.schemas import (
    Case,
    ContextScope,
    EventAction,
    Evidence,
    ExperimentRecord,
    ExperimentSystem,
    InferredCandidate,
    RunResult,
    StopReason,
    ToolCall,
    ToolRequest,
    Variant,
)
from variant2mechanism.v9.tools import (
    AdapterResult,
    ParamSpec,
    RecordedToolRunner,
    ToolLimits,
    ToolRefusal,
    ToolRegistry,
    ToolRunner,
    ToolSpec,
    canonical_params,
)

from . import test_graph as core_graph_tests
from . import test_graph_invariants as core_invariant_tests
from .test_engine_support import run_fixture

E_ID = "EH38E0000001"
ELEMENT = EntityRef(kind="element", label="+58 enhancer", canonical_id=E_ID)
VARIANT = EntityRef(kind="variant", label="rs1427407")


def dev_case() -> Case:
    return Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"))


def coordinates_case() -> Case:
    """A clean request: coordinates only, no rsID."""
    return Case(case_id="REQ-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G"))


def ctx(label: str) -> ContextScope:
    return ContextScope(label=label, source="supplied")


def tf(symbol: str) -> EntityRef:
    return EntityRef(kind="tf", label=symbol)


def gene(symbol: str) -> EntityRef:
    return EntityRef(kind="gene", label=symbol)


def claim(g: ClaimGraph, subjects, relation, objects, direction="unspecified", context=None, **kw) -> str:
    return g.add_claim(ClaimDraft(subjects=subjects, relation=relation, objects=objects, direction=direction,
                                  context=context, **kw), "coordinator")


def hypothesis(g: ClaimGraph, required) -> str:
    return g.add_hypothesis(HypothesisDraft(title="H", required_claim_ids=list(required),
                                            mechanism_class="regulatory"), "coordinator")


def record(g: ClaimGraph, evidence=(), *, tool="test_tool", requested_by="computational_investigator",
           status="success", retrieval="records_found", **fields) -> ToolCall:
    """A tool call recorded the way the runner records it, with its evidence."""
    charged = "code" if requested_by == "code" else "agent"
    return g.record_tool_call(ToolCall(tool_call_id=g.reserve_tool_call_id(), tool_name=tool, execution_status=status,
                                       retrieval_status=retrieval, requested_by=requested_by, charged_to=charged,
                                       **fields), list(evidence))


def tool_evidence(cls: str, text: str, **kw) -> Evidence:
    return Evidence(evidence_class=cls, observed_result=text, independence_group=text, origin="tool", **kw)


def evidence(g: ClaimGraph, cls: str, text: str, **kw) -> str:
    return record(g, [tool_evidence(cls, text, **kw)]).evidence_ids[0]


def overlap_call(g: ClaimGraph, element: str = E_ID, requested_by: str = "code") -> ToolCall:
    """ccre_overlap as code's fact collection reports it: the variant lies in an element."""
    return record(g, [tool_evidence("annotation", f"The variant lies in cCRE {element} ({requested_by}).",
                                    about_elements=[element])], tool="ccre_overlap", requested_by=requested_by)


def annotation_call(g: ClaimGraph, rsids=("rs1427407",), **kw) -> ToolCall:
    """variant_annotation as code's fact collection reports it: the dbSNP id at the case's coordinates and alleles."""
    return record(g, tool="variant_annotation", requested_by=kw.pop("requested_by", "code"),
                  observations=[{"id": r, "allele_string": "T/G"} for r in rsids], **kw)


# --- full-text reads: what counts, and one article whatever id names it ------------------------------------------------

ARTICLES = (("111", "PMC1", "10.1000/One"), ("222", "PMC2", "10.1000/two"), ("333", None, None))
READ = ToolSpec(name="read_article", route="literature", assemblies=[], provider="test",
                params={"pmcid": ParamSpec(normalise="upper"), "pmid": ParamSpec(),
                        "focus": ParamSpec(type="list[str]")},
                fulltext_params=["pmcid", "pmid"])


def read_adapter(params, ctx) -> AdapterResult:
    """A stand-in for literature_read: full text for an article with a PMCID, the abstract for one without, nothing
    for an unknown id (fulltext_read left at its default), an error for PMID 500; it reports every id of what it
    read."""
    if params.get("pmid") == "500":
        raise RuntimeError("upstream error")
    wanted = {article_key(params.get("pmcid"), pmcid=True), article_key(params.get("pmid"))} - {None}
    for pmid, pmcid, doi in ARTICLES:
        ids = [f"PMID:{pmid}", *([f"PMCID:{pmcid}"] if pmcid else []), *([f"DOI:{doi}"] if doi else [])]
        if wanted & {article_key(i) for i in ids}:
            key = pmcid or f"PMID:{pmid}"
            return AdapterResult(retrieval_status="records_found", raw={"article": key}, fulltext_article=key,
                                 fulltext_read=pmcid is not None, article_ids=ids)
    return AdapterResult(retrieval_status="no_records_found", raw={"article": None})


def read_runner(tmp_path, hard: int = 1, folder: str = "run") -> ToolRunner:
    registry = ToolRegistry()
    registry.register(READ, read_adapter)
    return ToolRunner(mode="cache_only", run_dir=tmp_path / folder, registry=registry, clock=lambda: "T0",
                      limits=ToolLimits(fulltext_soft=hard, fulltext_hard=hard))


def read(runner: ToolRunner, g: ClaimGraph, **params) -> ToolCall:
    return runner.run(ToolRequest(tool="read_article", params=params), g.case, g, "literature_investigator")


def test_article_ids_have_one_form():
    assert {article_key(x) for x in ("PMID:111", "pmid 111", " 111 ")} == {"111"}
    assert {article_key(x) for x in ("PMC1", "pmc1", "PMCID:PMC1", "PMCID: 1")} == {"PMC1"}
    assert article_key("1", pmcid=True) == "PMC1" and article_key("1") == "1"     # bare digits: a PMID by default
    assert {article_key(x) for x in ("DOI:10.1000/One", "doi:10.1000/one", "https://doi.org/10.1000/ONE",
                                     "10.1000/one")} == {"10.1000/one"}
    assert article_key("") is None and article_key(None) is None


def test_a_read_counts_only_when_it_returned_the_article(tmp_path):
    g = ClaimGraph(dev_case())
    r = read_runner(tmp_path)
    missing, failed = read(r, g, pmid="404"), read(r, g, pmid="500")
    assert (missing.execution_status, missing.retrieval_status, failed.execution_status) == (
        "success", "no_records_found", "error")
    for empty in (missing, failed):
        assert (empty.read_article, empty.fulltext_article, empty.article_ids) == (None, None, [])
        assert empty.charged_to == "agent"                               # still a charged agent call
    assert r.budget(g).fulltext_used == g.budget_snapshot().fulltext_reads == 0
    abstract = read(r, g, pmid="333")
    assert (abstract.read_article, abstract.fulltext_article, abstract.article_ids) == ("PMID:333", None, ["333"])
    assert read(r, g, pmcid="PMC1").fulltext_article == "PMC1" and r.budget(g).fulltext_used == 1
    extraction = Evidence(evidence_class="perturbation", observed_result="an experiment from a paper never read",
                          independence_group="PMID:404#x", origin="literature", source_ids=["PMID:404"],
                          retrieval_ref=missing.tool_call_id,
                          experiment=ExperimentRecord(source_id="PMID:404", access="abstract_only",
                                                      location="abstract/p1", passage="p"))
    with pytest.raises(GraphRefusal, match="not a literature read"):
        g.add_evidence(extraction, "literature_investigator")


@pytest.mark.parametrize("first, again", [({"pmcid": "PMC1"}, {"pmid": "111"}),
                                          ({"pmid": "111"}, {"pmcid": "pmc1"}),
                                          ({"pmcid": "PMC1"}, {"pmcid": "1"})])
def test_one_article_is_one_read_whichever_id_requests_it(tmp_path, first, again):
    g = ClaimGraph(dev_case())
    r = read_runner(tmp_path, hard=1)
    counted = read(r, g, **first)
    assert counted.fulltext_article == "PMC1" and counted.article_ids == ["10.1000/one", "111", "PMC1"]
    at_cap = read(r, g, **again)                     # a first request by another id, with the hard cap reached
    assert (at_cap.execution_status, at_cap.charged_to, at_cap.fulltext_article) == ("success", "agent", "PMC1")
    assert at_cap.tool_call_id != counted.tool_call_id
    assert g.budget_snapshot().fulltext_reads == r.budget(g).fulltext_used == 1
    assert g.fulltext_articles() == [frozenset({"10.1000/one", "111", "PMC1"})]
    new = read(r, g, pmid="222")                     # a genuinely new article is refused at the cap
    assert (new.execution_status, new.charged_to) == ("not_applicable", "none")
    assert "full-text budget exhausted" in new.message and g.budget_snapshot().fulltext_reads == 1


def test_reads_sharing_any_identifier_are_counted_as_one_article():
    g = ClaimGraph(dev_case())

    def counted(article: str, ids: list[str], full: bool = True) -> None:
        record(g, tool="read_article", requested_by="literature_investigator", read_article=article,
               fulltext_article=article if full else None, article_ids=ids)

    counted("PMC1", ["PMC1"])
    counted("DOI:10.1000/one", ["10.1000/one"])
    assert g.budget_snapshot().fulltext_reads == 2                       # nothing ties them together yet
    counted("PMID:111", ["10.1000/one", "111", "PMC1"])                  # one read names all three ids
    assert g.budget_snapshot().fulltext_reads == 1 and len(g.fulltext_articles()) == 1
    counted("PMC9", ["PMC9"], full=False)                                # an abstract-only read is never counted
    counted("PMC2", ["PMC2"])
    assert g.fulltext_articles() == [frozenset({"10.1000/one", "111", "PMC1"}), frozenset({"PMC2"})]


def test_replay_reproduces_the_article_ids(tmp_path):
    original = ClaimGraph(dev_case())
    live = read_runner(tmp_path, hard=8)
    saved = [read(live, original, pmid="111"), read(live, original, pmid="404")]
    folder = tmp_path / "run"
    (folder / "graph.json").write_text(original.to_json())
    (folder / "tool_calls.jsonl").write_text("".join(t.model_dump_json() + "\n" for t in original.tool_calls.values()))
    (folder / "evidence.jsonl").write_text("".join(e.model_dump_json() + "\n" for e in original.evidence.values()))
    recorded = RecordedToolRunner(folder, run_dir=tmp_path / "replay", registry=live.registry, clock=lambda: "T0",
                                  limits=live.limits)
    replayed = ClaimGraph(dev_case())
    again = [read(recorded, replayed, pmid="111"), read(recorded, replayed, pmid="404")]
    assert [c.model_dump(exclude={"cached"}) for c in again] == [c.model_dump(exclude={"cached"}) for c in saved]
    assert again[0].article_ids == ["10.1000/one", "111", "PMC1"] and recorded.misses == []
    assert replayed.budget_snapshot() == original.budget_snapshot()


# --- one_of parameter groups -------------------------------------------------------------------------------------------

DETAIL = ToolSpec(name="detail", route="computational", provider="test",
                  params={"tf": ParamSpec(normalise="upper"), "group": ParamSpec(normalise="upper")},
                  one_of=[["tf", "group"]])


def test_one_of_groups_take_exactly_one_parameter_and_refuse_without_charge(tmp_path):
    assert canonical_params(DETAIL, {"tf": " cebpa "}) == {"tf": "CEBPA"}
    for params, given in (({}, "none"), ({"tf": "CEBPA", "group": "G035"}, "tf, group"), ({"tf": "  "}, "none")):
        with pytest.raises(ToolRefusal, match=f"exactly one of tf, group \\(got {given}\\)"):
            canonical_params(DETAIL, params)
    registry = ToolRegistry()
    registry.register(DETAIL, lambda params, ctx: AdapterResult(retrieval_status="records_found",
                                                                observations=[dict(params)]))
    g = ClaimGraph(dev_case())
    runner = ToolRunner(mode="cache_only", registry=registry, clock=lambda: "T0")
    both = runner.run(ToolRequest(tool="detail", params={"tf": "CEBPA", "group": "G035"}), g.case, g,
                      "computational_investigator")
    assert (both.execution_status, both.charged_to) == ("not_applicable", "none") and "exactly one" in both.message
    one = runner.run(ToolRequest(tool="detail", params={"group": "g035"}), g.case, g, "computational_investigator")
    assert (one.execution_status, one.charged_to, one.observations) == ("success", "agent", [{"group": "G035"}])
    assert runner.budget(g).tool_calls_used == 1
    assert DETAIL.describe()["one_of"] == [["tf", "group"]] and "one_of" not in READ.describe()
    with pytest.raises(ValueError, match="unknown parameter"):
        ToolSpec(name="bad", route="computational", params={"tf": ParamSpec()}, one_of=[["tf", "gene"]])


# --- the engine_error stop ---------------------------------------------------------------------------------------------

def test_an_internal_error_is_a_stop_reason_the_graph_keeps():
    assert "engine_error" in get_args(StopReason)
    g = ClaimGraph(dev_case())
    g.set_result(RunResult(outcome="no_supported_explanation", stop_reason="engine_error",
                           summary="an internal error stopped the run; nothing was decided"))
    assert g.events[-1].details["stop_reason"] == "engine_error"
    assert ClaimGraph.from_json(g.to_json()).result.stop_reason == "engine_error"


# --- inferred candidates -----------------------------------------------------------------------------------------------

def test_inferred_candidates_are_kept_on_the_case_and_never_become_input():
    request = dev_case().model_copy(update={"supplied_disease": ["LDL cholesterol"],
                                            "supplied_context": [ctx("HepG2")]})
    g = ClaimGraph(request)
    eqtl = evidence(g, "association", "Liver eQTL: G is associated with higher GENE1.", about_genes=["GENE1"],
                    allele="G", direction="increases", context=ctx("GTEx:Liver"))
    version = g.version
    liver = InferredCandidate(kind="context", label=" liver ", basis_evidence_ids=[eqtl, eqtl], note="eQTL tissue")
    assert g.add_inferred_candidate(liver, "coordinator") is True
    assert [(c.kind, c.label, c.basis_evidence_ids) for c in g.case.inferred_candidates] == [
        ("context", "liver", [eqtl])]
    event = g.events[-1]
    assert (event.action, event.role, event.evidence_ids, g.version) == (
        "add_inferred_candidate", "coordinator", [eqtl], version + 1)
    assert (g.case.supplied_disease, g.case.supplied_context) == (request.supplied_disease, request.supplied_context)
    assert request.inferred_candidates == []                             # the request object is untouched
    n_events = len(g.events)
    for kind, label in (("context", "liver tissue"), ("context", "Hep G2 cells"), ("disease", "LDL-cholesterol")):
        assert g.add_inferred_candidate(InferredCandidate(kind=kind, label=label), "code") is False   # known
    assert len(g.events) == n_events and len(g.case.inferred_candidates) == 1
    assert g.add_inferred_candidate(InferredCandidate(kind="disease", label="coronary artery disease"), "code")
    before = g.to_json()
    for candidate, role, reason in (
            (InferredCandidate(kind="disease", label="obesity"), "critic", "coordinator or code"),
            (InferredCandidate(kind="disease", label="obesity"), "computational_investigator", "coordinator or code"),
            (InferredCandidate(kind="disease", label="obesity", basis_evidence_ids=["E99"]), "coordinator",
             "unknown evidence E99"),
            (InferredCandidate(kind="context", label="unknown"), "coordinator", "needs a label")):
        with pytest.raises(GraphRefusal, match=reason):
            g.add_inferred_candidate(candidate, role)
    assert g.to_json() == before
    again = ClaimGraph.from_json(before)
    assert again.to_json() == before and again.case.inferred_candidates == g.case.inferred_candidates


# --- the display rule as a pure function -------------------------------------------------------------------------------

def assert_display_of_agrees(graph: ClaimGraph) -> None:
    """display_of on a claim and the evidence alone, and on their serialised copies, gives what graph.display shows."""
    state = GraphState.model_validate_json(graph.to_json())
    for cid, claim_ in graph.claims.items():
        shown = graph.display(cid)
        assert display_of(claim_, graph.evidence) == shown == display_of(state.claims[cid], state.evidence), cid


def graph_test_functions() -> list:
    """Every test of the core graph test modules: each builds its graphs from a fresh case (g), a folder, or itself."""
    return [pytest.param(fn, id=f"{module.__name__.rsplit('.', 1)[-1]}::{name}")
            for module in (core_graph_tests, core_invariant_tests) for name, fn in sorted(vars(module).items())
            if name.startswith("test_") and inspect.isfunction(fn)
            and set(inspect.signature(fn).parameters) <= {"g", "tmp_path"}]


@pytest.mark.parametrize("test", graph_test_functions())
def test_display_of_agrees_with_the_graph_on_every_core_test_graph(test, tmp_path, monkeypatch):
    built: list[ClaimGraph] = []
    init = ClaimGraph.__init__

    def recording_init(self, *args, **kwargs):
        init(self, *args, **kwargs)
        built.append(self)

    given = {"g": lambda: ClaimGraph(dev_case()), "tmp_path": lambda: tmp_path}
    with monkeypatch.context() as patch:                # every graph the test builds, including reloaded copies
        patch.setattr(ClaimGraph, "__init__", recording_init)
        test(**{name: given[name]() for name in inspect.signature(test).parameters})
    for graph in built:
        assert_display_of_agrees(graph)


def test_display_of_on_the_synthetic_fixture_run(v9_cfg, tmp_path):
    result, _, _ = run_fixture(v9_cfg, "synthetic_repair", tmp_path)
    g = result.graph
    assert_display_of_agrees(g)
    shown = {cid: display_of(g.claims[cid], g.evidence) for cid in ("C1", "C2", "C3", "C4")}
    assert [d.status for d in shown.values()] == ["supported", "contradicted", "unresolved", "unresolved"]
    assert (shown["C1"].basis, shown["C2"].basis) == ("synthetic", "synthetic")
    assert shown["C3"].dependency_flag == "unsupported_due_to_dependency"   # flagged, never contradicted
    before = g.claims["C2"].model_copy(update={"assessment": "unassessed"})  # F1 before it was assessed
    assert display_of(before, g.evidence).status == "unresolved"


def test_display_of_shows_a_claim_as_it_stood_earlier():
    g = ClaimGraph(dev_case())
    c = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", ctx("HepG2"))
    crispr = evidence(g, "perturbation", "CRISPRi of the enhancer lowers GENE1 in HepG2", about_genes=["GENE1"],
                      about_elements=[E_ID], direction="increases", context=ctx("HepG2"))
    activation = evidence(g, "perturbation", "CRISPRa of the enhancer lowers GENE1 in HepG2", about_genes=["GENE1"],
                          about_elements=[E_ID], direction="decreases", context=ctx("HepG2"))
    g.link(c, crispr, "supports", "computational_investigator", "CRISPRi")
    g.assess(c, "supported_in_scope", "CRISPRi in HepG2", "critic", g.claims[c].version)
    g.link(c, activation, "contradicts", "computational_investigator", "CRISPRa disagrees")
    g.assess(c, "contested", "the two perturbations disagree", "critic", g.claims[c].version)
    now = g.claims[c]
    then = now.model_copy(update={"assessment": "supported_in_scope",
                                  "evidence_links": [x for x in now.evidence_links if x.evidence_id == crispr]})
    assert display_of(now, g.evidence).status == "contested"
    assert (display_of(then, g.evidence).status, display_of(then, g.evidence).basis) == ("supported", "perturbation")


# --- variant types ------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("ref, alt, expected", [
    ("A", "G", "SNV"), ("a", "t", "SNV"), ("TA", "T", "indel"), ("T", "TGG", "indel"),
    ("TA", "GC", "other"), ("N", "A", "other"), ("A", "-", "other"), ("A", "<DEL>", "other"), ("", "A", "other")])
def test_the_variant_type_follows_the_alleles(ref, alt, expected):
    assert Variant(chrom="2", pos=1, ref=ref, alt=alt).variant_type == expected
    assert Variant(chrom="2", pos=1, ref=ref, alt=alt, variant_type="indel").variant_type == "indel"   # kept


def test_a_multi_base_substitution_is_not_run_by_snv_only_tools():
    registry = ToolRegistry()
    registry.register(ToolSpec(name="snv_only", route="computational", variant_types=["SNV"]),
                      lambda params, ctx: AdapterResult(retrieval_status="records_found"))
    g = ClaimGraph(Case(case_id="DEV-3", variant=Variant(chrom="2", pos=60490908, ref="TA", alt="GC")))
    out = ToolRunner(mode="cache_only", registry=registry, clock=lambda: "T0").run(
        ToolRequest(tool="snv_only"), g.case, g, "computational_investigator")
    assert (out.execution_status, out.charged_to) == ("not_applicable", "none") and "this variant is other" in out.message


# --- what a literature experiment is about ------------------------------------------------------------------------------

def test_experiment_records_say_what_was_manipulated_and_which_allele_was_compared():
    bare = ExperimentRecord(source_id="PMID:7", access="full_text", location="sec2/p3", passage="p")
    assert (bare.about_elements, bare.manipulated, bare.compared_allele) == ([], "none", None)
    old = {"source_id": "PMID:7", "access": "full_text", "location": "sec2/p3", "passage": "p"}
    assert ExperimentRecord.model_validate(old) == bare                 # a record written before still loads
    deletion = ExperimentRecord(
        source_id="PMID:7", pmcid="PMC7", access="full_text", location="sec2/p3",
        passage="Deleting the enhancer lowered BCL11A in HUDEP-2 cells (TT at rs1427407).",
        system=ExperimentSystem(tissue_or_cell="HUDEP-2", genotype_or_allele="TT"),
        intervention="CRISPR deletion of the enhancer", endpoint="BCL11A mRNA", direction="decreases",
        about_genes=["BCL11A"], about_elements=["the enhancer containing rs1427407"], manipulated="element")
    allelic = deletion.model_copy(update={
        "location": "fig3", "passage": "Base editing T to G raised BCL11A.", "intervention": "base editing",
        "manipulated": "allele", "compared_allele": "G", "direction": "increases"})
    for rec in (deletion, allelic):
        assert ExperimentRecord.model_validate_json(rec.model_dump_json()) == rec
    assert (deletion.compared_allele, deletion.system.genotype_or_allele) == (None, "TT")   # a genotype is context
    with pytest.raises(ValidationError):
        ExperimentRecord.model_validate({**old, "manipulated": "variant"})
    g = ClaimGraph(dev_case())
    read_call = record(g, tool="literature_read", requested_by="literature_investigator", read_article="PMC7",
                       fulltext_article="PMC7", article_ids=["7", "PMC7"])
    eid = g.add_evidence(Evidence(evidence_class="perturbation", observed_result=deletion.passage,
                                  independence_group="PMID:7#deletion/BCL11A/HUDEP-2", origin="literature",
                                  source_ids=["PMID:7"], experiment=deletion, retrieval_ref=read_call.tool_call_id,
                                  about_genes=["BCL11A"], about_elements=deletion.about_elements,
                                  direction="decreases", access="full_text"), "literature_investigator")
    assert ClaimGraph.from_json(g.to_json()).evidence[eid].experiment == deletion


# --- the case variant's rsID found by code -----------------------------------------------------------------------------

def test_an_rsid_code_found_at_the_case_coordinates_names_the_case_variant():
    g = ClaimGraph(coordinates_case())
    case_variant = g.variant_entity()
    rs = EntityRef(kind="variant", label="rs1427407")
    before = claim(g, [rs], "alters_binding", [tf("TFX")], "increases")
    assert g.claims[before].subject_ids != [case_variant] and g.claims[before].effect_allele is None
    ref_binds_more = evidence(g, "binding_assay", "EMSA: TFX binds the T allele more strongly", about_tfs=["TFX"],
                              allele="T", direction="increases", about_variants=["rs1427407"])
    with pytest.raises(GraphRefusal, match="cannot be placed"):          # another variant: no allele frame to check
        g.link(before, ref_binds_more, "supports", "computational_investigator", "EMSA")
    vep = annotation_call(g)
    version = g.version
    assert g.add_variant_alias("RS1427407", vep.tool_call_id) is True
    assert g.variant_aliases == {"rs1427407": vep.tool_call_id} and g.version == version + 1
    assert (g.events[-1].action, g.events[-1].role) == ("add_variant_alias", "code")
    assert g.case.variant.rsid is None                                   # the request stays as supplied
    after = claim(g, [rs], "alters_binding", [tf("TFX")], "increases")
    assert after != before and g.claims[after].subject_ids == [case_variant]
    assert g.claims[after].effect_allele == "G"                          # the alt allele unless stated
    assert claim(g, [rs], "alters_binding", [tf("TFX")], "decreases", effect_allele="T") == after   # ref frame
    with pytest.raises(GraphRefusal, match="neither ref T nor alt G"):
        claim(g, [rs], "alters_binding", [tf("TFX")], "increases", effect_allele="C")
    with pytest.raises(GraphRefusal, match="opposite"):                  # the allele frame now applies
        g.link(after, ref_binds_more, "supports", "computational_investigator", "EMSA")
    for label in ("rs999", "chr5:60490908 T>G"):                        # another rsID, another chromosome
        assert g.claims[claim(g, [EntityRef(kind="variant", label=label)], "overlaps", [ELEMENT])].subject_ids != [
            case_variant]
    version = g.version
    assert g.add_variant_alias("rs1427407", vep.tool_call_id) is False and g.version == version   # idempotent


def test_an_alias_comes_only_from_code_that_reports_it_and_never_replaces_a_supplied_rsid():
    g = ClaimGraph(coordinates_case())
    agent = annotation_call(g, requested_by="computational_investigator")
    empty = annotation_call(g, rsids=(), retrieval="no_records_found")
    failed = annotation_call(g, rsids=(), status="error", retrieval="unknown")
    longer = annotation_call(g, rsids=("rs14274070",))                  # a longer rsID is not this one
    before = g.to_json()
    for rsid, tid, reason in (("rs1427407", "T99", "unknown tool call"),
                              ("rs1427407", agent.tool_call_id, "requested by the computational investigator"),
                              ("rs1427407", empty.tool_call_id, "found records"),
                              ("rs1427407", failed.tool_call_id, "found records"),
                              ("rs1427407", longer.tool_call_id, "do not name rs1427407"),
                              ("1427407", longer.tool_call_id, "not an rsID")):
        with pytest.raises(GraphRefusal, match=reason):
            g.add_variant_alias(rsid, tid)
    assert g.to_json() == before and g.variant_aliases == {}
    supplied = ClaimGraph(dev_case())
    vep = annotation_call(supplied, rsids=("rs1427407", "rs999"))
    with pytest.raises(GraphRefusal, match="conflicts with the case's supplied rsID rs1427407"):
        supplied.add_variant_alias("rs999", vep.tool_call_id)
    assert supplied.add_variant_alias("rs1427407", vep.tool_call_id) is False and supplied.variant_aliases == {}


def test_aliases_and_variant_elements_are_saved_with_the_graph():
    g = ClaimGraph(coordinates_case())
    g.add_variant_alias("rs1427407", annotation_call(g).tool_call_id)
    g.add_variant_element(E_ID, overlap_call(g).tool_call_id)
    text = g.to_json()
    again = ClaimGraph.from_json(text)
    assert again.to_json() == text
    assert (again.variant_aliases, again.variant_elements) == (g.variant_aliases, g.variant_elements) != ({}, {})
    named = claim(again, [EntityRef(kind="variant", label="rs1427407")], "overlaps", [ELEMENT])
    assert again.claims[named].subject_ids == [again.variant_entity()]
    legacy = json.loads(text)
    del legacy["variant_aliases"], legacy["variant_elements"]           # a graph.json written before these fields
    old = ClaimGraph.from_json(json.dumps(legacy))
    assert (old.variant_aliases, old.variant_elements) == ({}, {})


def test_a_failure_inside_the_case_mutations_rolls_them_back(monkeypatch):
    g = ClaimGraph(coordinates_case())
    vep, ccre = annotation_call(g), overlap_call(g)
    before = g.to_json()

    def broken(*args, **kwargs):
        raise RuntimeError("the event log failed")

    with monkeypatch.context() as patch:
        patch.setattr(g, "_event", broken)
        for mutate in (lambda: g.add_variant_alias("rs1427407", vep.tool_call_id),
                       lambda: g.add_variant_element(E_ID, ccre.tool_call_id),
                       lambda: g.add_inferred_candidate(InferredCandidate(kind="disease", label="LDL cholesterol"),
                                                        "coordinator")):
            with pytest.raises(RuntimeError, match="event log failed"):
                mutate()
    assert (g.variant_aliases, g.variant_elements, g.case.inferred_candidates) == ({}, {}, [])
    assert g.to_json() == before


# --- element claims need evidence about that element ---------------------------------------------------------------

def test_a_tf_knockdown_never_tests_what_an_element_does():
    g = ClaimGraph(dev_case())
    reg = claim(g, [ELEMENT], "regulates", [gene("BCL11A")], "increases", ctx("K562"))
    h = hypothesis(g, [reg])
    knockdown = evidence(g, "perturbation", "siRNA knockdown of GATA1 reduced BCL11A mRNA in K562 cells",
                         about_tfs=["GATA1"], about_genes=["BCL11A"], direction="increases", context=ctx("K562"))
    null = evidence(g, "perturbation", "siRNA knockdown of GATA1 did not change BCL11A mRNA in K562 cells",
                    about_tfs=["GATA1"], about_genes=["BCL11A"], context=ctx("K562"),
                    result_kind="null_in_assessed_scope", assessed_relation="regulates")
    for eid, stance in ((knockdown, "supports"), (null, "contradicts")):
        with pytest.raises(GraphRefusal, match="needs evidence that names that element"):
            g.link(reg, eid, stance, "literature_investigator", "the knockdown and BCL11A in matched K562 cells")
    assert g.claims[reg].evidence_links == [] and g.hypotheses[h].disposition == "active"   # no false rejection
    assert g.link(reg, knockdown, "context_only", "literature_investigator", "a TF-level result").stance == \
        "context_only"


def test_evidence_naming_the_variants_element_is_about_the_element_recorded_over_it():
    g = ClaimGraph(dev_case())
    reg = claim(g, [ELEMENT], "regulates", [gene("BCL11A")], "increases", ctx("K562"))

    def deletion(region: str) -> str:
        return evidence(g, "perturbation", f"Deleting {region} lowered BCL11A in K562 cells", about_genes=["BCL11A"],
                        about_elements=[region], direction="increases", context=ctx("K562"))

    by_rsid = deletion("the enhancer containing rs1427407")
    with pytest.raises(GraphRefusal, match="recorded as containing it are none"):
        g.link(reg, by_rsid, "supports", "literature_investigator", "the deletion")
    ccre = overlap_call(g)
    assert g.add_variant_element(E_ID, ccre.tool_call_id) is True
    link = g.link(reg, by_rsid, "supports", "literature_investigator", "deleting the element lowered BCL11A")
    assert (link.stance, link.strength, link.applicability) == ("supports", "direct", "exact")
    assert g.link(reg, deletion("the enhancer at chr2:60490908"), "supports", "literature_investigator",
                  "the same element, named by position").strength == "direct"
    for other in ("EH38E0000002", "the enhancer containing rs999", "the enhancer at chr5:60490908"):
        with pytest.raises(GraphRefusal, match=f"not {E_ID}"):
            g.link(reg, deletion(other), "supports", "literature_investigator", "another element")


def test_a_recorded_alias_lets_its_rsid_name_the_variants_element():
    g = ClaimGraph(coordinates_case())
    g.add_variant_element(E_ID, overlap_call(g).tool_call_id)
    reg = claim(g, [ELEMENT], "regulates", [gene("BCL11A")], "increases", ctx("K562"))
    named = evidence(g, "perturbation", "Deleting the enhancer containing rs1427407 lowered BCL11A in K562 cells",
                     about_genes=["BCL11A"], about_elements=["the enhancer containing rs1427407"],
                     direction="increases", context=ctx("K562"))
    with pytest.raises(GraphRefusal, match=f"not {E_ID}"):              # until code finds it, another variant's rsID
        g.link(reg, named, "supports", "literature_investigator", "the deletion")
    g.add_variant_alias("rs1427407", annotation_call(g).tool_call_id)
    assert g.link(reg, named, "supports", "literature_investigator", "the deletion").strength == "direct"


def test_element_objects_keep_the_earlier_rule():
    g = ClaimGraph(dev_case())
    activity = claim(g, [VARIANT], "alters_regulatory_activity", [ELEMENT], "increases", ctx("HepG2"))
    construct = evidence(g, "reporter_assay", "Luciferase: the G construct is 3x higher in HepG2", allele="G",
                         direction="increases", context=ctx("HepG2"), about_variants=["rs1427407"])
    assert g.link(activity, construct, "supports", "computational_investigator", "constructs").strength == "direct"
    elsewhere = evidence(g, "reporter_assay", "Luciferase: EH38E0000002 G construct 3x higher in HepG2", allele="G",
                         about_elements=["EH38E0000002"], direction="increases", context=ctx("HepG2"),
                         about_variants=["rs1427407"])
    with pytest.raises(GraphRefusal, match=f"not {E_ID}"):
        g.link(activity, elsewhere, "supports", "computational_investigator", "another element")
    occupancy = claim(g, [tf("TFX")], "occupies", [ELEMENT], context=ctx("HepG2"))
    chip = evidence(g, "occupancy", "TFX ChIP-seq peak over the variant in HepG2", about_tfs=["TFX"],
                    context=ctx("HepG2"))
    assert g.link(occupancy, chip, "supports", "computational_investigator", "a peak").strength == "direct"
    overlap = claim(g, [VARIANT], "overlaps", [ELEMENT])
    with pytest.raises(GraphRefusal, match=f"not {E_ID}"):
        g.link(overlap, evidence(g, "annotation", "the variant lies in a cCRE"), "supports",
               "computational_investigator", "an unnamed overlap")


def test_variant_elements_come_only_from_code_calls_that_name_them():
    g = ClaimGraph(dev_case())
    ccre, agent = overlap_call(g), overlap_call(g, requested_by="computational_investigator")
    empty = record(g, tool="ccre_overlap", requested_by="code", retrieval="no_records_found")
    before = g.to_json()
    for element, tid, reason in ((E_ID, "T99", "unknown tool call"),
                                 (E_ID, agent.tool_call_id, "requested by the computational investigator"),
                                 (E_ID, empty.tool_call_id, "found records"),
                                 ("EH38E0000009", ccre.tool_call_id, "names element EH38E0000009"),
                                 (" ", ccre.tool_call_id, "needs its id")):
        with pytest.raises(GraphRefusal, match=reason):
            g.add_variant_element(element, tid)
    assert g.to_json() == before
    version = g.version
    assert g.add_variant_element(E_ID, ccre.tool_call_id) is True and g.variant_elements == {E_ID: ccre.tool_call_id}
    event = g.events[-1]
    assert (event.action, event.role, event.evidence_ids, g.version) == (
        "add_variant_element", "code", ccre.evidence_ids, version + 1)
    assert g.add_variant_element(E_ID.lower(), ccre.tool_call_id) is False and g.version == version + 1


# ======================================================================================================================
# Round 3 (CORE-CHANGES-3)
# ======================================================================================================================

ALIAS = ["rs1427407"]                                    # how most evidence below names the case variant
E2 = EntityRef(kind="element", label="EH38E0000042", canonical_id="EH38E0000042")


def ld_case() -> Case:
    """C3-1's motivating example, as plumbing: rs12740374 (chr1:109274968 G>T) and an LD partner tested in the same
    paper (rs629301). Every observation below is stipulated."""
    return Case(case_id="DEV-LD", variant=Variant(chrom="1", pos=109274968, ref="G", alt="T", rsid="rs12740374"))


def read_paper(g: ClaimGraph) -> ToolCall:
    """A successful full-text read of PMC7 (PMID 7): what an extracted experiment must cite."""
    found = next((t for t in g.tool_calls.values() if t.read_article == "PMC7"), None)
    return found or record(g, tool="literature_read", requested_by="literature_investigator", read_article="PMC7",
                           fulltext_article="PMC7", article_ids=["7", "PMC7"])


def extracted(g: ClaimGraph, cls: str, passage: str, *, manipulated: str, location: str, allele: str | None = None,
              about_variants=(), **fields) -> str:
    """An experiment extracted from PMC7, entering through add_evidence as the literature route adds it, with the
    record's variants copied into the evidence (as evidence_from_experiment will)."""
    x = ExperimentRecord(source_id="PMID:7", pmcid="PMC7", access="full_text", location=location, passage=passage,
                         intervention=passage, manipulated=manipulated, about_variants=list(about_variants),
                         compared_allele=allele if manipulated == "allele" else None,
                         about_tfs=fields.get("about_tfs", []), about_genes=fields.get("about_genes", []),
                         about_elements=fields.get("about_elements", []))
    return g.add_evidence(Evidence(evidence_class=cls, observed_result=passage, independence_group=f"PMID:7#{location}",
                                   origin="literature", source_ids=["PMID:7"], experiment=x, access="full_text",
                                   retrieval_ref=read_paper(g).tool_call_id, allele=allele,
                                   about_variants=list(about_variants), **fields), "literature_investigator")


# --- C3-1: which variant evidence is about ----------------------------------------------------------------------------

@pytest.mark.parametrize("text, expected", [
    ("rs1427407", "case"), ("RS1427407", "case"), ("chr2:60490908", "case"), ("2:60490908:T>G", "case"),
    ("chr2:60490908 G/T", "case"), ("chr2:60490908 T/C/G", "case"), ("GRCh38:2:60490908:T:G", "case"),
    ("the enhancer containing rs1427407", "case"),
    ("rs999", "other"), ("rs14274070", "other"), ("chr5:60490908", "other"), ("chr2:60490909", "other"),
    ("chr2:60490908:T>C", "other"), ("rs1427407 and rs999", "other"), ("rs1427407 at chr5:60490908", "other"),
    ("the G allele", None), ("", None), ("EH38E0000001", None)])
def test_one_rule_reads_every_text_that_names_a_variant(text, expected):
    assert ClaimGraph(dev_case()).variant_mention(text) == expected


def test_a_case_on_any_chromosome_is_named_by_its_position():
    synthetic = ClaimGraph(Case(case_id="SYN-9", variant=Variant(chrom="SYN", pos=2, ref="C", alt="T")))
    assert [synthetic.variant_mention(t) for t in ("SYN:2", "SYN:2 C>T", "GRCh38:SYN:2:C:T", "SYN:1", "SYN:2:C:G",
                                                  "V2", "SYN:E2")] == ["case", "case", "case", "other", "other",
                                                                       None, None]
    assert ClaimGraph(coordinates_case()).variant_mention("rs1427407") == "other"     # no rsID yet: another variant


def test_evidence_about_an_ld_partner_never_bears_on_a_claim_about_the_case_variant():
    g = ClaimGraph(ld_case())
    binds = claim(g, [EntityRef(kind="variant", label="rs12740374")], "alters_binding", [tf("TFX")], "increases",
                  ctx("HepG2"))
    assert g.claim_frame(binds) == "case"
    fields = dict(about_tfs=["TFX"], allele="T", direction="increases", context=ctx("HepG2"))
    partner = evidence(g, "binding_assay", "EMSA (same figure): TFX binds the T allele of rs629301 more strongly",
                       about_variants=["rs629301"], **fields)
    for stance in ("supports", "contradicts"):
        with pytest.raises(GraphRefusal, match=r"is about rs629301, not the case variant \(rs12740374, "
                                               r"chr1:109274968 G>T\): evidence about one variant cannot"):
            g.link(binds, partner, stance, "literature_investigator", "the EMSA")
    assert g.claims[binds].evidence_links == []
    assert g.link(binds, partner, "context_only", "literature_investigator", "an LD partner's EMSA").stance == \
        "context_only"                                   # recording what was read is never refused
    own = evidence(g, "binding_assay", "EMSA (same figure): TFX binds the T allele of rs12740374 more strongly",
                   about_variants=["rs12740374"], **fields)
    link = g.link(binds, own, "supports", "literature_investigator", "the EMSA of this variant")
    assert (link.stance, link.strength, link.applicability) == ("supports", "direct", "exact")
    both = evidence(g, "binding_assay", "EMSA of both variants in one gel: T binds TFX more",
                    about_variants=["rs629301", "chr1:109274968"], **fields)
    assert g.link(binds, both, "supports", "literature_investigator", "it names the case variant").stance == "supports"


def test_evidence_naming_the_variant_by_an_alias_counts_once_code_records_it():
    g = ClaimGraph(coordinates_case())
    activity = claim(g, [EntityRef(kind="variant", label="chr2:60490908")], "alters_regulatory_activity", [ELEMENT],
                     "increases", ctx("HepG2"))
    reporter = evidence(g, "reporter_assay", "Luciferase: the rs1427407 G construct is 3x higher in HepG2", allele="G",
                        direction="increases", context=ctx("HepG2"), about_variants=ALIAS)
    with pytest.raises(GraphRefusal, match="is about rs1427407, not the case variant"):   # not yet the case's own
        g.link(activity, reporter, "supports", "computational_investigator", "the constructs")
    g.add_variant_alias("rs1427407", annotation_call(g).tool_call_id)
    assert g.link(activity, reporter, "supports", "computational_investigator", "the constructs").strength == "direct"
    tiles = evidence(g, "reporter_assay", "MPRA: the G tile of chr2:60490908:T>G is 2x higher in HepG2", allele="G",
                     direction="increases", context=ctx("HepG2"), about_variants=["chr2:60490908:T>G"])
    assert g.link(activity, tiles, "supports", "computational_investigator", "the tiles").strength == "direct"
    other_alt = evidence(g, "reporter_assay", "MPRA: the C tile of chr2:60490908:T>C is 2x higher in HepG2", allele="T",
                         direction="decreases", context=ctx("HepG2"), about_variants=["chr2:60490908:T>C"])
    with pytest.raises(GraphRefusal, match="is about chr2:60490908:T>C, not the case variant"):
        g.link(activity, other_alt, "supports", "computational_investigator", "another allele at the site")


def test_allele_comparing_evidence_must_say_whose_alleles_it_compared():
    g = ClaimGraph(dev_case())
    activity = claim(g, [VARIANT], "alters_regulatory_activity", [ELEMENT], "increases", ctx("HepG2"))
    unnamed = evidence(g, "reporter_assay", "Luciferase: the G construct is 3x higher in HepG2", allele="G",
                       direction="increases", context=ctx("HepG2"))
    with pytest.raises(GraphRefusal, match="compares alleles but names no variant .*state which variant's alleles"):
        g.link(activity, unnamed, "supports", "computational_investigator", "constructs")
    vague = evidence(g, "reporter_assay", "Luciferase: the risk-allele construct is 3x higher in HepG2", allele="G",
                     direction="increases", context=ctx("HepG2"), about_variants=["the risk allele"])
    with pytest.raises(GraphRefusal, match="names no variant"):   # an entry with no rsID or position names nothing
        g.link(activity, vague, "contradicts", "computational_investigator", "constructs")
    edited = extracted(g, "perturbation", "Base editing at the site raised enhancer activity in HepG2",
                       manipulated="allele", location="fig2", context=ctx("HepG2"))      # an allele edit, no base named
    with pytest.raises(GraphRefusal, match="names no variant"):
        g.link(activity, edited, "supports", "literature_investigator", "base editing")
    for eid in (unnamed, vague, edited):
        assert g.link(activity, eid, "context_only", "critic", "recorded, not weighed").stance == "context_only"
    trait = claim(g, [VARIANT], "associated_with_trait", [EntityRef(kind="phenotype", label="LDL cholesterol")],
                  "increases")
    gwas = evidence(g, "association", "GWAS: G associated with higher LDL cholesterol", allele="G",
                    direction="increases", about_traits=["LDL cholesterol"])                 # not an allelic relation
    assert g.link(trait, gwas, "supports", "computational_investigator", "a GWAS row").strength == "direct"


def test_a_claim_about_another_variant_takes_only_evidence_naming_it():
    g = ClaimGraph(dev_case())
    partner = EntityRef(kind="variant", label="rs999")
    binds = claim(g, [partner], "alters_binding", [tf("TFX")], "increases", effect_allele="A")
    assert g.claim_frame(binds) == "other" and g.claims[binds].effect_allele == "A"
    fields = dict(about_tfs=["TFX"], allele="A", direction="increases")
    own = evidence(g, "binding_assay", "EMSA: TFX binds the rs999 A allele more", about_variants=["rs999"], **fields)
    assert g.link(binds, own, "supports", "literature_investigator", "the partner's EMSA").strength == "direct"
    for named, what in ((["rs1427407"], "the case variant's"), (["rs888"], "a third variant's"),
                        (["chr2:60490000"], "another position's")):
        ev = evidence(g, "binding_assay", f"EMSA: TFX binds {what} A allele more", about_variants=named, **fields)
        with pytest.raises(GraphRefusal, match=f"is about {named[0]}, not rs999"):
            g.link(binds, ev, "supports", "literature_investigator", "an EMSA")
    unnamed = evidence(g, "binding_assay", "EMSA: TFX binds the A allele more", **fields)
    with pytest.raises(GraphRefusal, match="names no variant .*is about rs999"):
        g.link(binds, unnamed, "supports", "literature_investigator", "an EMSA")
    trait = claim(g, [partner], "associated_with_trait", [EntityRef(kind="phenotype", label="LDL cholesterol")])
    gwas = evidence(g, "association", "GWAS: rs999 is associated with LDL cholesterol", about_traits=["LDL cholesterol"])
    assert g.link(trait, gwas, "supports", "computational_investigator", "no variant named, no alleles compared"
                  ).stance == "supports"


def test_about_variants_are_kept_apart_saved_with_the_graph_and_older_graphs_still_load():
    g = ClaimGraph(dev_case())
    fields = dict(about_tfs=["TFX"], allele="G", direction="increases")
    eid = evidence(g, "binding_assay", "EMSA: TFX binds the G allele more", about_variants=[" rs1427407 ",
                                                                                         "rs1427407", "chr2:60490908 T>G"],
                   **fields)
    assert g.evidence[eid].about_variants == ["rs1427407", "chr2:60490908 T>G"]      # collapsed, de-duplicated
    assert evidence(g, "binding_assay", "EMSA: TFX binds the G allele more", about_variants=["rs999"], **fields) != eid
    lit = extracted(g, "binding_assay", "EMSA with T and G probes: TFX binds G more", manipulated="allele",
                    location="fig1", allele="G", direction="increases", about_tfs=["TFX"], about_variants=ALIAS)
    partner = extracted(g, "binding_assay", "EMSA with T and G probes: TFX binds G more", manipulated="allele",
                        location="fig1", allele="G", direction="increases", about_tfs=["TFX"], about_variants=["rs999"])
    assert partner != lit                                # one figure testing two variants is two experiments
    text = g.to_json()
    again = ClaimGraph.from_json(text)
    assert again.to_json() == text and again.evidence[lit].experiment.about_variants == ALIAS
    legacy = json.loads(text)
    for item in legacy["evidence"].values():             # a graph.json written before the field existed
        del item["about_variants"]
        if item["experiment"]:
            del item["experiment"]["about_variants"]
    old = ClaimGraph.from_json(json.dumps(legacy))
    assert all(e.about_variants == [] and (e.experiment is None or e.experiment.about_variants == [])
               for e in old.evidence.values())


# --- C3-2: what a perturbation can say about the variant's alleles -------------------------------------------------

def test_a_tf_or_gene_perturbation_never_tests_what_the_variants_alleles_do():
    """The literature fixer's reproduction (scratchpad/litfix/check_variant_claim_gap.py): a GATA1 knockdown naming no
    element made "the case variant alters the regulatory activity of E" supported in scope, direct and exact."""
    g = ClaimGraph(dev_case())
    activity = claim(g, [EntityRef(kind="variant", label="chr2:60490908")], "alters_regulatory_activity", [E2],
                     context=ctx("K562"))
    knockdown = extracted(g, "perturbation", "siRNA knockdown of GATA1 in K562 cells reduced BCL11A mRNA by half",
                          manipulated="tf", location="sec2.1/p1", about_tfs=["GATA1"], about_genes=["BCL11A"],
                          direction="increases", context=ctx("K562"))
    assert g.link_strength(activity, knockdown) == "context"
    for stance in ("supports", "contradicts"):
        with pytest.raises(GraphRefusal, match="a TF perturbation does not test what the variant's alleles do.*"
                                               "link it as context_only"):
            g.link(activity, knockdown, stance, "literature_investigator", "the knockdown")
    assert g.link(activity, knockdown, "context_only", "literature_investigator", "the TF matters").stance == \
        "context_only"
    with pytest.raises(GraphRefusal, match="supported_in_scope needs"):
        g.assess(activity, "supported_in_scope", "a perturbation", "critic", g.claims[activity].version)
    knockout = extracted(g, "perturbation", "Knocking out BCL11A in K562 cells lowered its spliced transcript",
                         manipulated="gene", location="sec2.3/p1", about_genes=["BCL11A"], context=ctx("K562"))
    rna = claim(g, [VARIANT], "alters_rna", [gene("BCL11A")], context=ctx("K562"))
    with pytest.raises(GraphRefusal, match="a gene perturbation does not test"):
        g.link(rna, knockout, "supports", "literature_investigator", "the knockout")
    partner = claim(g, [EntityRef(kind="variant", label="rs999")], "alters_regulatory_activity", [E2],
                    context=ctx("K562"))
    assert g.link_strength(partner, knockdown) == "context"          # another variant's alleles neither


def test_an_experiment_that_compares_no_alleles_is_indirect_for_a_claim_that_they_differ():
    g = ClaimGraph(dev_case())
    activity = claim(g, [VARIANT], "alters_regulatory_activity", [ELEMENT], context=ctx("K562"))
    deletion = extracted(g, "perturbation", "Deleting the enhancer containing rs1427407 lowered BCL11A in K562 cells",
                         manipulated="element", location="sec2.2/p1", about_genes=["BCL11A"], about_elements=[E_ID],
                         direction="increases", context=ctx("K562"))
    link = g.link(activity, deletion, "supports", "literature_investigator", "the deletion")
    assert (link.strength, g.link_strength(activity, deletion)) == ("indirect", "indirect")
    assert any("does not compare the variant's alleles" in note for note in g.events[-1].details["notes"])
    with pytest.raises(GraphRefusal, match=r"indirect \(perturbation\).*does not compare the variant's alleles"):
        g.assess(activity, "supported_in_scope", "the deletion", "critic", g.claims[activity].version)
    assert g.display(activity).status == "unresolved"
    single = extracted(g, "reporter_assay", "A luciferase reporter carrying the enhancer was active in K562 cells",
                       manipulated="element", location="fig4", about_elements=[E_ID], context=ctx("K562"))
    assert g.link(activity, single, "supports", "literature_investigator", "one construct").strength == "indirect"
    binding = claim(g, [VARIANT], "alters_binding", [tf("GATA1")], context=ctx("K562"))
    probe = extracted(g, "binding_assay", "GATA1 bound a probe spanning the site in K562 nuclear extract",
                      manipulated="none", location="fig5", about_tfs=["GATA1"], context=ctx("K562"))
    assert g.link(binding, probe, "supports", "literature_investigator", "a single probe").strength == "indirect"


def test_allele_comparisons_tool_evidence_and_claims_about_elements_or_factors_keep_the_class_matrix():
    g = ClaimGraph(dev_case())
    binding = claim(g, [VARIANT], "alters_binding", [tf("GATA1")], "increases", ctx("K562"))
    emsa = extracted(g, "binding_assay", "EMSA with T and G probes: GATA1 bound the G probe more in K562 extract",
                     manipulated="allele", location="fig1", allele="G", about_tfs=["GATA1"], direction="increases",
                     context=ctx("K562"), about_variants=ALIAS)
    assert g.link(binding, emsa, "supports", "literature_investigator", "EMSA").strength == "direct"
    g.assess(binding, "supported_in_scope", "an allele comparison", "critic", g.claims[binding].version)
    activity = claim(g, [VARIANT], "alters_regulatory_activity", [ELEMENT], "increases", ctx("K562"))
    reporter = extracted(g, "reporter_assay", "Luciferase: the G construct was 3x the T construct in K562 cells",
                         manipulated="allele", location="fig2", allele="G", direction="increases", context=ctx("K562"),
                         about_variants=ALIAS)
    assert g.link(activity, reporter, "supports", "literature_investigator", "constructs").strength == "direct"
    screen = evidence(g, "perturbation", "SCREEN: CRISPRi of the cCRE changed GENE1 in K562", about_genes=["GENE1"],
                      about_elements=[E_ID], context=ctx("K562"))           # tool output: no experiment record
    assert g.link(activity, screen, "supports", "computational_investigator", "a screen").strength == "direct"
    element = claim(g, [ELEMENT], "regulates", [gene("BCL11A")], "increases", ctx("K562"))
    deletion = extracted(g, "perturbation", "Deleting the enhancer lowered BCL11A in K562 cells", manipulated="element",
                         location="sec2.2/p1", about_genes=["BCL11A"], about_elements=[E_ID], direction="increases",
                         context=ctx("K562"))
    assert g.link(element, deletion, "supports", "literature_investigator", "the deletion").strength == "direct"
    factor = claim(g, [tf("GATA1")], "regulates", [gene("BCL11A")], "increases", ctx("K562"))
    knockdown = extracted(g, "perturbation", "GATA1 knockdown lowered BCL11A in K562 cells", manipulated="tf",
                          location="sec2.1/p1", about_tfs=["GATA1"], about_genes=["BCL11A"], direction="increases",
                          context=ctx("K562"))
    assert g.link(factor, knockdown, "supports", "literature_investigator", "the knockdown").strength == "direct"


# --- C3-3: canonical ids that name the case variant -------------------------------------------------------------------

def test_a_canonical_id_naming_the_case_variant_resolves_to_it():
    g = ClaimGraph(coordinates_case())
    case_variant = g.variant_entity()

    def subject(canonical: str, label: str = "the variant", **kw) -> str:
        ref = EntityRef(kind="variant", label=label, canonical_id=canonical)
        return g.claims[claim(g, [ref], "alters_binding", [tf("TFX")], "increases", **kw)].subject_ids[0]

    before = subject("rs1427407")
    assert before != case_variant and g.entities[before].canonical_id == "rs1427407"    # not yet the case's own
    g.add_variant_alias("rs1427407", annotation_call(g).tool_call_id)
    after = claim(g, [EntityRef(kind="variant", label="the variant", canonical_id="RS1427407")], "alters_binding",
                  [tf("TFX")], "increases")
    assert g.claims[after].subject_ids == [case_variant] and g.claim_frame(after) == "case"
    assert g.claims[after].effect_allele == "G"                          # the case's allele rules apply
    with pytest.raises(GraphRefusal, match="neither ref T nor alt G"):
        subject("rs1427407", effect_allele="C")
    for canonical in ("chr2:60490908", "2:60490908:T>G", "chr2:60490908 G/T", "GRCh38:2:60490908:T:G"):
        assert subject(canonical) == case_variant, canonical
    for canonical in ("chr2:60490908:T>C", "chr5:60490908", "rs999"):
        assert subject(canonical) != case_variant, canonical
    assert subject("chr2:60490908", label="rs999") != case_variant      # a label naming another variant wins
    by_label = claim(g, [EntityRef(kind="variant", label="the G allele")], "alters_binding", [tf("TFY")], "increases")
    assert claim(g, [EntityRef(kind="variant", canonical_id="chr2:60490908")], "alters_binding", [tf("TFY")],
                 "increases") == by_label                               # the lookup finds the same claim
    assert g.ref_is_case_variant(EntityRef(kind="variant", label="x", canonical_id="chr2:60490908:T:G"))
    assert g.ref_is_case_variant(EntityRef(kind="variant", entity_id=case_variant))
    assert not g.ref_is_case_variant(EntityRef(kind="variant", label="rs999"))
    assert not g.ref_is_case_variant(EntityRef(kind="tf", label="TFX"))


# --- C3-4: the public claim frame ---------------------------------------------------------------------------------------

def test_the_claim_frame_is_public():
    g = ClaimGraph(dev_case())
    about_case = claim(g, [VARIANT], "overlaps", [ELEMENT])
    about_other = claim(g, [EntityRef(kind="variant", label="rs999")], "overlaps", [ELEMENT])
    about_none = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases")
    assert [g.claim_frame(c) for c in (about_case, about_other, about_none)] == ["case", "other", None]
    with pytest.raises(KeyError):
        g.claim_frame("C99")


# --- C3-5: reinstating a code rejection whose contradiction no longer stands ------------------------------------------

def rejected(g: ClaimGraph) -> tuple[str, str, str, str]:
    """F1 (the element represses GENE1) is required by H; a matched activation that raises GENE1 contradicts F1, and
    code rejects H at that assessment. Returns (F1, H's other required claim, H, the contradicting evidence)."""
    f1 = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    keep = claim(g, [VARIANT], "overlaps", [ELEMENT])
    h = hypothesis(g, [f1, keep])
    up = evidence(g, "perturbation", "Activating the enhancer raised GENE1 in HepG2", about_genes=["GENE1"],
                  about_elements=[E_ID], direction="increases", context=ctx("HepG2"))
    g.link(f1, up, "contradicts", "computational_investigator", "a matched activation")
    g.assess(f1, "contradicted_in_scope", "matched contradiction", "critic", g.claims[f1].version)
    assert g.hypotheses[h].disposition == "rejected"
    return f1, keep, h, up


def rejection(g: ClaimGraph, hid: str):
    return [e for e in g.events if e.action == "reject" and hid in e.target_ids][-1]


def test_a_rejection_whose_contradiction_was_withdrawn_is_reinstated_once():
    assert "reinstate" in get_args(EventAction)
    g = ClaimGraph(dev_case())
    f1, keep, h, _ = rejected(g)
    first = rejection(g, h)
    assert (first.role, first.details["rule"], first.details["claims"]) == ("code", "contradicted_required_claim", [f1])
    before = g.to_json()
    assert g.reinstate(h, "the contradiction still stands") is False and g.to_json() == before
    g.assess(f1, "unresolved", "the activation used another construct: misread", "critic", g.claims[f1].version)
    assert compare.stale_rejections(g) == [h]
    version = g.version
    assert g.reinstate(h, "the contradiction of F1 was withdrawn on review") is True
    hyp, event = g.hypotheses[h], g.events[-1]
    assert (hyp.disposition, hyp.disposition_reason) == ("deferred", "the contradiction of F1 was withdrawn on review")
    assert f1 in hyp.revisit_trigger and first.event_id in hyp.revisit_trigger
    assert (event.action, event.role, event.target_ids, g.version) == ("reinstate", "code", [h, f1], version + 1)
    assert (event.details["rejected_by"], event.details["claims"]) == (first.event_id, [f1])
    entry = hyp.history[-1]
    assert (entry["kind"], entry["from"], entry["to"], entry["rejected_by"], entry["claims"], entry["event_id"]) == (
        "reinstatement", "rejected", "deferred", first.event_id, [f1], event.event_id)
    assert compare.stale_rejections(g) == []
    assert ClaimGraph.from_json(g.to_json()).to_json() == g.to_json()
    assert hypothesis(g, [f1, keep]) == h                # the anti-repeat block lifted: the same story merges into H
    g.assess(f1, "contradicted_in_scope", "the activation stands after all", "critic", g.claims[f1].version)
    assert g.hypotheses[h].disposition == "rejected"     # rejected again, by the same rule
    g.assess(f1, "unresolved", "misread again", "critic", g.claims[f1].version)
    before = g.to_json()
    assert g.reinstate(h, "withdrawn again") is False and g.to_json() == before     # never twice: no oscillation
    with pytest.raises(GraphRefusal, match=f"repeats rejected hypothesis {h}"):
        hypothesis(g, [f1, keep])
    with pytest.raises(GraphRefusal, match="final"):
        g.set_disposition(h, "deferred", "try again", "coordinator", revisit_trigger="later")


def test_a_replaced_link_that_withdraws_the_contradiction_also_reinstates():
    g = ClaimGraph(dev_case())
    f1, _, h, up = rejected(g)
    g.link(f1, up, "context_only", "critic", "the passage was misread: another construct")
    assert g.claims[f1].assessment == "unresolved"        # code reset it: its contradicts link was replaced
    assert g.reinstate(h, " ") is True
    assert g.hypotheses[h].disposition_reason == f"the contradiction of {f1} that rejected {h} was withdrawn"


def test_only_codes_own_rule_based_rejections_are_reinstated():
    g = ClaimGraph(dev_case())
    f1, _, h, _ = rejected(g)
    g.assess(f1, "unresolved", "misread", "critic", g.claims[f1].version)
    active = hypothesis(g, [claim(g, [VARIANT], "overlaps", [E2])])
    for hid, role, reason in ((h, "critic", "only code reinstates"), (h, "coordinator", "only code reinstates"),
                              ("H99", "code", "unknown hypothesis H99"), (active, "code", "not rejected")):
        with pytest.raises(GraphRefusal, match=reason):
            g.reinstate(hid, "x", role)
    state = json.loads(g.to_json())
    first = rejection(g, h).event_id

    def edited(change) -> ClaimGraph:
        copy_ = json.loads(json.dumps(state))
        change(next(e for e in copy_["events"] if e["event_id"] == first))
        return ClaimGraph.from_json(json.dumps(copy_))

    for change in (lambda e: e.update(role="critic"), lambda e: e["details"].update(rule="another rule")):
        with pytest.raises(GraphRefusal, match="not rejected by code for a contradicted required claim"):
            edited(change).reinstate(h, "x")

    def legacy(e) -> None:                                # a graph written before rejections named their rule
        del e["details"]["rule"], e["details"]["claims"]

    old = edited(legacy)
    assert old.reinstate(h, "read from the rejection's reason") is True and old.events[-1].details["claims"] == [f1]


def test_an_open_hypothesis_in_another_scope_does_not_block_reinstatement():
    g = ClaimGraph(dev_case())
    f1 = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("HepG2"))
    h1 = hypothesis(g, [f1])
    twin = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "decreases", ctx("liver"))  # different scope
    h2 = hypothesis(g, [claim(g, [ELEMENT], "regulates", [gene("GENE2")], "decreases", ctx("liver"))])
    g.revise_hypothesis(h2, HypothesisChanges(replace_claims={g.hypotheses[h2].required_claim_ids[0]: twin}),
                        "the liver claim", "coordinator")
    assert g.hypotheses[h2].signature != g.hypotheses[h1].signature
    up = evidence(g, "perturbation", "Activating the enhancer raised GENE1 in HepG2", about_genes=["GENE1"],
                  about_elements=[E_ID], direction="increases", context=ctx("HepG2"))
    g.link(f1, up, "contradicts", "computational_investigator", "a matched activation")
    g.assess(f1, "contradicted_in_scope", "matched", "critic", g.claims[f1].version)
    g.assess(f1, "unresolved", "misread", "critic", g.claims[f1].version)
    assert (g.hypotheses[h1].disposition, g.hypotheses[h2].disposition) == ("rejected", "active")
    assert g.reinstate(h1, "withdrawn") is True and g.hypotheses[h1].disposition == "deferred"


# --- C3-6: one sketched-groups rule -------------------------------------------------------------------------------------

def test_sketched_groups_count_every_version_supersession_and_member_alternative():
    g = ClaimGraph(dev_case())
    rows = [{"group_id": gid, "members": [{"tf": m, "mapping": "own"} for m in members]}
            for gid, members in (("G035", ["CEBPA", "CEBPB"]), ("G142", ["CEBPD"]), ("G070", ["GCM1"]),
                                 ("G027", ["NFIA"]), ("G300", ["ZNF300"]), ("G400", ["ZNF400"]),
                                 ("G999", ["ZNF999"]))]
    group = EntityRef(kind="tf_group", label="group G035", canonical_id="G035", members=["CEBPA", "CEBPB"])
    first = claim(g, [VARIANT], "alters_binding", [group], "increases")
    h1 = g.add_hypothesis(HypothesisDraft(title="C/EBP", required_claim_ids=[first], mechanism_class="tf_binding"),
                          "coordinator")
    cebpd = claim(g, [VARIANT], "alters_binding", [tf("CEBPD")], "increases")
    g.revise_hypothesis(h1, HypothesisChanges(replace_claims={first: cebpd}, member_alternatives=["znf300 "]),
                        "a local repair: the member is CEBPD", "coordinator")
    gcm = claim(g, [VARIANT], "alters_binding", [tf("GCM1")], "decreases")
    h2 = g.add_hypothesis(HypothesisDraft(title="GCM1", required_claim_ids=[gcm], mechanism_class="tf_binding"),
                          "coordinator")
    g.supersede_claim(gcm, ClaimDraft(subjects=[VARIANT], relation="alters_binding", objects=[tf("NFIA")],
                                      direction="decreases"), "the assay was for NFIA", "coordinator", [h2])
    never = claim(g, [VARIANT], "alters_binding", [tf("ZNF400")], "increases")       # in no hypothesis itself
    replacement = g.supersede_claim(never, ClaimDraft(subjects=[VARIANT], relation="alters_binding",
                                                      objects=[tf("ZNF401")], direction="increases"),
                                    "another member", "coordinator")
    g.add_hypothesis(HypothesisDraft(title="ZNF401", required_claim_ids=[replacement], mechanism_class="tf_binding"),
                     "coordinator")
    assert hypothesis_versions(g.hypotheses[h1]) == [([first], []), ([cebpd], ["znf300 "])]
    assert sketched_groups(g, rows) == {"G035", "G142", "G070", "G027", "G300", "G400"}   # G999: never named
    assert sketched_groups(g, []) == set()
    assert (bundle.sketched_groups, bundle.hypothesis_versions) == (graph_module.sketched_groups,
                                                                     graph_module.hypothesis_versions)
