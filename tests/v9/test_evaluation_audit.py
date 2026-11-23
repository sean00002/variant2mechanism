"""The evaluator's audit of one run folder (SPEC 10): how the run ended (an explanation, an abstention or a
limitation; a run that assessed nothing is not scored), per-component denominators scored on the claims that stand
(by the graph's own claim frame), provisional scores until the spec is reviewed, the isolation check of the case as
supplied, candidate retention including inventory_only, eliminations by revision or supersession and reinstated
hypotheses, improper eliminations, unsupported causal claims, the evidence-fidelity sheet and efficiency; plus
write_evaluation, the audit command's call and the run_suite refusal.

The runs are hand-built for the development variant rs1427407 (chr2:60490908 T>G) through the ClaimGraph API, against
the stipulated rows of tests/v9/fixtures/evaluation/dev_gold.csv; TFs, genes and observations are stipulated for the
test and are not claims about that variant. One test runs the audit command on the committed gold spec, with a run
for a gold variant that holds no hypothesis: plumbing only, nothing is scored or chosen by it.
"""

import json
import math

import pytest

from variant2mechanism import cli
from variant2mechanism.config import REPO
from variant2mechanism.context.http import HttpResult
from variant2mechanism.v9 import bundle, compare
from variant2mechanism.v9.evaluation import (
    EVALUATION_FILE,
    MISSING_COVERAGE,
    MORE_IS_BETTER,
    RUN_FAILURES,
    SuiteRefusal,
    audit,
    build_gold_spec,
    find_label_strings,
    label_strings,
    load_gold_spec,
    run_suite,
    spec_entry,
    write_evaluation,
)
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, HypothesisChanges, HypothesisDraft
from variant2mechanism.v9.intake import Request, build_case
from variant2mechanism.v9.schemas import (
    ContextScope,
    Evidence,
    InferredCandidate,
    PairComparison,
    RunResult,
    ToolCall,
)

pytestmark = pytest.mark.data       # the spec and the family check read HGNC and the Lambert table

DEV_CSV = REPO / "tests" / "v9" / "fixtures" / "evaluation" / "dev_gold.csv"
VARIANT = EntityRef(kind="variant", label="the G allele")
ELEMENT = EntityRef(kind="element", label="EH38E0000001", canonical_id="EH38E0000001")
LIVER = ContextScope(label="liver")
WHEN = "2026-11-08T00:00:00+00:00"


def inventory_row(group_id: str, members: list[str], passes: bool, binds_more: str = "alt") -> dict:
    """One qbic_inventory observation in the C2 shape."""
    return {"group_id": group_id, "group_label": f"{group_id} test group", "dbd": "test",
            "members": [{"tf": m, "mapping": "own"} for m in members], "paralog_stem": None,
            "best_model": f"{members[0]}_test_model", "binds_more": binds_more, "z": 9.5 if passes else 1.2,
            "effect": 1.0, "p": 1e-6 if passes else 0.2, "n_pass": 1 if passes else 0, "n_models": 1,
            "passes_gate": passes}


INVENTORY = [inventory_row("G035", ["CEBPA", "CEBPB", "CEBPE"], True),
             inventory_row("G142", ["CEBPD"], True),
             inventory_row("G070", ["GCM1", "GCM2"], True, binds_more="ref"),
             inventory_row("G027", ["NFIA", "NFIB", "NFIC", "NFIX"], True),
             inventory_row("G999", ["ZNF999"], False)]
VEP = [{"id": "rs1427407", "location": "2:60490908-60490908", "allele_string": "T/G"}]   # a variant_annotation row


def record(g: ClaimGraph, tool: str, evidence=(), observations=(), role="code") -> ToolCall:
    tid = g.reserve_tool_call_id()
    return g.record_tool_call(ToolCall(tool_call_id=tid, tool_name=tool, execution_status="success",
                                       retrieval_status="records_found", requested_by=role,
                                       charged_to="code" if role == "code" else "agent",
                                       observations=list(observations)), list(evidence))


def tool_evidence(cls: str, text: str, group: str, **kw) -> Evidence:
    return Evidence(evidence_class=cls, observed_result=text, independence_group=group, origin="tool", **kw)


def group_ref(gid: str, members: list[str]) -> EntityRef:
    return EntityRef(kind="tf_group", label=f"group {gid}", canonical_id=gid, members=members)


def claim(g: ClaimGraph, subjects, relation, objects, **kw) -> str:
    return g.add_claim(ClaimDraft(subjects=subjects, relation=relation, objects=objects, **kw), "coordinator")


def annotate(g: ClaimGraph) -> str:
    """The code overlap fact for the element, and the supported overlap claim resting on it."""
    call = record(g, "ccre_overlap", [tool_evidence("annotation", "The variant lies in cCRE EH38E0000001.",
                                                    "CCRE:EH38E0000001", about_elements=["EH38E0000001"])])
    c_overlap = claim(g, [VARIANT], "overlaps", [ELEMENT])
    g.link(c_overlap, call.evidence_ids[0], "supports", "computational_investigator", rationale="the overlap")
    g.assess(c_overlap, "supported_in_scope", "the overlap", "critic", g.claims[c_overlap].version)
    return c_overlap


def lead(g: ClaimGraph, hid: str) -> None:
    g.set_disposition(hid, "leading", "the only hypothesis", "code")
    g.set_result(RunResult(outcome="partial_mechanism", stop_reason="converged", leading_ids=[hid]))


def supported_cebpa(g: ClaimGraph) -> tuple[str, str, str]:
    """The overlap fact, and a liver CEBPA binding claim supported by a matched EMSA that names the variant whose
    alleles it compared (the G allele binds more). Returns (overlap claim, binding claim, the EMSA's E id)."""
    c_overlap = annotate(g)
    emsa = record(g, "binding_test", role="computational_investigator", evidence=[tool_evidence(
        "binding_assay", "The G allele bound CEBPA more than T in liver nuclear extract.", "EMSA:test:CEBPA",
        allele="G", direction="increases", about_tfs=["CEBPA"], context=LIVER, about_variants=["chr2:60490908 T>G"])])
    c_cebpa = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label="CEBPA")], direction="increases",
                    context=LIVER)
    g.link(c_cebpa, emsa.evidence_ids[0], "supports", "computational_investigator", rationale="G binds CEBPA more")
    g.assess(c_cebpa, "supported_in_scope", "a matched binding assay", "critic", g.claims[c_cebpa].version)
    return c_overlap, c_cebpa, emsa.evidence_ids[0]


def cebpa_hypothesis(g: ClaimGraph, required: list[str]) -> str:
    return g.add_hypothesis(HypothesisDraft(title="CEBPA binding", required_claim_ids=required,
                                            mechanism_class="tf_binding"), "coordinator")


def build_graph(case, *, member_claim: bool = False) -> ClaimGraph:
    """H1 leads (C/EBP group -> element -> SORT1 -> LDL); H2 is deferred for missing ChIP; H3 is rejected by a
    matched perturbation; H4 is deferred by a z ranking; the G027 group is listed and never sketched."""
    g = ClaimGraph(case)
    rows = [r for r in INVENTORY if r["passes_gate"]]
    inv = record(g, "qbic_inventory", observations=INVENTORY, evidence=[tool_evidence(
        "prediction", f"QBiC-SELEX group {r['group_id']}: the {'G' if r['binds_more'] == 'alt' else 'T'} allele has "
                      "more predicted binding", f"QBIC:test:{r['group_id']}",
        about_tfs=[m["tf"] for m in r["members"]], allele="G" if r["binds_more"] == "alt" else "T",
        direction="increases", data={"group_id": r["group_id"], "z": r["z"]},
        about_variants=["chr2:60490908 T>G"]) for r in rows])
    pred = {g.evidence[e].data["group_id"]: e for e in inv.evidence_ids}
    annotation = record(g, "ccre_overlap", [tool_evidence("annotation", "The variant lies in cCRE EH38E0000001.",
                                                          "CCRE:EH38E0000001", about_elements=["EH38E0000001"])])
    eqtl = record(g, "gtex_eqtl", [tool_evidence("association", "Liver eQTL: G is associated with higher SORT1.",
                                                 "GTEX:liver:SORT1", allele="G", direction="increases",
                                                 about_genes=["SORT1"], context=LIVER,
                                                 about_elements=["EH38E0000001"])])   # an element-gene link names it
    raised = record(g, "crispr_test", role="computational_investigator", evidence=[tool_evidence(
        "perturbation", "Activating EH38E0000001 raised SORT1 in liver cells.", "CRISPR:test:SORT1",
        direction="increases", about_genes=["SORT1"], about_elements=["EH38E0000001"], context=LIVER)])
    lowered = record(g, "crispr_test_psrc1", role="computational_investigator", evidence=[tool_evidence(
        "perturbation", "Activating EH38E0000001 lowered PSRC1 in liver cells.", "CRISPR:test:PSRC1",
        direction="decreases", about_genes=["PSRC1"], about_elements=["EH38E0000001"], context=LIVER)])

    c_bind = claim(g, [VARIANT], "alters_binding", [group_ref("G035", ["CEBPA", "CEBPB", "CEBPE"])],
                   direction="increases", mechanism_class="tf_binding")
    c_overlap = claim(g, [VARIANT], "overlaps", [ELEMENT])
    sort1, psrc1 = EntityRef(kind="gene", label="SORT1"), EntityRef(kind="gene", label="PSRC1")
    c_reg = claim(g, [ELEMENT], "regulates", [sort1], direction="increases", context=LIVER)
    c_trait = claim(g, [sort1], "contributes_to_trait", [EntityRef(kind="phenotype", label="LDL cholesterol")],
                    direction="decreases")
    c_psrc1 = claim(g, [ELEMENT], "regulates", [psrc1], direction="increases", context=LIVER)
    c_cebpd = claim(g, [VARIANT], "alters_binding", [group_ref("G142", ["CEBPD"])], direction="increases")
    c_gcm = claim(g, [VARIANT], "alters_binding", [group_ref("G070", ["GCM1", "GCM2"])], direction="decreases")
    optional = [c_trait]
    if member_claim:
        optional.append(claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label="CEBPA")],
                              direction="increases"))

    h1 = g.add_hypothesis(HypothesisDraft(title="C/EBP binding raises SORT1", claim_ids=optional,
                                          required_claim_ids=[c_bind, c_overlap, c_reg], context=LIVER,
                                          endpoint="LDL cholesterol levels", mechanism_class="tf_binding",
                                          member_alternatives=["CEBPB"]), "coordinator")
    h2 = g.add_hypothesis(HypothesisDraft(title="CEBPD binding", required_claim_ids=[c_cebpd],
                                          mechanism_class="tf_binding", disposition="deferred",
                                          disposition_reason="no ChIP-seq peak for CEBPD in liver",
                                          revisit_trigger="a CEBPD ChIP-seq experiment in hepatocytes"),
                          "coordinator")
    h3 = g.add_hypothesis(HypothesisDraft(title="The element raises PSRC1", required_claim_ids=[c_overlap, c_psrc1],
                                          mechanism_class="regulatory"), "coordinator")
    h4 = g.add_hypothesis(HypothesisDraft(title="GCM binding", required_claim_ids=[c_gcm],
                                          mechanism_class="tf_binding"), "coordinator")

    for cid, eid, why in [(c_bind, pred["G035"], "QBiC-SELEX predicts more CEBPA binding to G"),
                          (c_overlap, annotation.evidence_ids[0], "the variant lies in the element"),
                          (c_reg, eqtl.evidence_ids[0], "a liver eQTL for SORT1"),
                          (c_reg, raised.evidence_ids[0], "activating the element raised SORT1"),
                          (c_cebpd, pred["G142"], "QBiC-SELEX predicts more CEBPD binding to G"),
                          (c_gcm, pred["G070"], "QBiC-SELEX predicts less GCM1 binding to G")]:
        g.link(cid, eid, "supports", "computational_investigator", rationale=why)
    if member_claim:
        g.link(optional[-1], pred["G035"], "supports", "computational_investigator", rationale="CEBPA model")
    g.link(c_psrc1, lowered.evidence_ids[0], "contradicts", "computational_investigator",
           rationale="activating the element lowered PSRC1")
    for cid, assessment in [(c_overlap, "supported_in_scope"), (c_reg, "supported_in_scope"),
                            (c_psrc1, "contradicted_in_scope")]:
        g.assess(cid, assessment, "assessed for the test", "critic", g.claims[cid].version)
    g.set_disposition(h4, "deferred", "a lower z-score than the C/EBP groups", "coordinator",
                      revisit_trigger="a GCM ChIP-seq experiment")
    g.set_disposition(h1, "leading", "preferred over H2 on the binding claim", "code")
    g.add_comparison(PairComparison(a=h1, b=h2, outcome="A_preferred", decisive_claim_ids=[c_bind],
                                    reason="the C/EBP group has the better-supported path"), "critic")
    g.set_result(RunResult(outcome="partial_mechanism", stop_reason="converged", leading_ids=[h1]))
    g.propagate()
    g.set_model_usage(5, 0.0123)
    assert g.hypotheses[h3].disposition == "rejected"
    return g


ENGINE_METRICS = {"model_calls": 5, "inventory": {"inventory_only": ["G027"]}}   # the engine's shape (C4, metrics)


def write_run(path, graph: ClaimGraph, metrics: dict | None = None):
    path.mkdir()
    (path / "graph.json").write_text(graph.to_json())
    (path / "metrics.json").write_text(json.dumps(ENGINE_METRICS if metrics is None else metrics))
    (path / "manifest.json").write_text(json.dumps({"mode": "fixture"}))
    return path


@pytest.fixture
def spec(v9_cfg) -> dict:
    return build_gold_spec(DEV_CSV, config=v9_cfg)


def case_for(row_spec: dict, arm: str, v9_cfg, **extra):
    request = Request(**{**row_spec["requests"][arm], **extra})
    return build_case(request, config=v9_cfg, http=None, mode="cache_only")


def recovery(result: dict) -> dict:
    return {k: (v["numerator"], v["denominator"]) for k, v in result["component_recovery"].items()}


# --- component recovery ---------------------------------------------------------------------------------------------

def test_each_component_has_its_own_denominator(spec, v9_cfg, tmp_path):
    entry = spec_entry(spec, "dev_member")
    result = audit(write_run(tmp_path / "run", build_graph(case_for(entry, "main", v9_cfg))), entry)
    assert recovery(result) == {"tf_member": (0, 1), "tf_group": (1, 1), "tf_family": (1, 1), "direction": (1, 1),
                                "target_gene": (1, 1), "context": (1, 1), "phenotype": (1, 1)}
    c = result["components"]
    assert c["tf_group"]["matched"] == ["CEBPA", "CEBPB", "CEBPE", "G035"]
    assert [(x["claim_id"], x["display"]) for x in c["tf_group"]["claims"]] == [("C1", "predicted")]
    assert c["direction"]["claims"][0]["alt_direction"] == "increases"
    assert c["context"]["level"] == "exact"
    assert c["phenotype"]["matched"] == ["LDL cholesterol"]
    assert result["answer_claims"] == {"standing": ["C4", "C1", "C2", "C3"], "excluded": []}
    assert result["isolation"] == {"clean": True, "problems": []}
    assert result["run"]["arm"] == "main" and result["run"]["answer"] == ["H1"]

    member = audit(write_run(tmp_path / "member", build_graph(case_for(entry, "main", v9_cfg), member_claim=True)),
                   entry)
    assert recovery(member)["tf_member"] == (1, 1)                       # strict credit needs the member itself


def test_scores_are_provisional_until_the_spec_is_reviewed(spec, v9_cfg, tmp_path):
    run = write_run(tmp_path / "run", build_graph(case_for(spec_entry(spec, "dev_member"), "main", v9_cfg)))
    unreviewed = audit(run, spec_entry(spec, "dev_member"))
    assert (unreviewed["spec"]["status"], unreviewed["spec"]["provisional"]) == ("unreviewed", True)
    assert all(c["provisional"] for c in unreviewed["component_recovery"].values() if c["denominator"])
    bare = audit(run, spec["cases"][0])                 # an entry taken without spec_entry carries no status
    assert (bare["spec"]["status"], bare["spec"]["provisional"]) == ("unreviewed", True)
    final = audit(run, spec_entry({**spec, "status": "reviewed"}, "dev_member"))
    assert (final["spec"]["status"], final["spec"]["provisional"]) == ("reviewed", False)
    # After the review only components still marked needs_review stay provisional: the CSV family is not the Lambert
    # DBD, and the notes name POU5F1B, a TF and a possible target gene.
    assert {k for k, c in final["component_recovery"].items() if c["provisional"]} == {"tf_member", "tf_family",
                                                                                         "target_gene"}


def test_inputs_controls_and_capability_gaps_leave_the_denominator(spec, v9_cfg, tmp_path):
    entry = spec_entry(spec, "dev_member")
    supplied = audit(write_run(tmp_path / "supplied", build_graph(case_for(entry, "supplied_disease", v9_cfg))),
                     entry)
    assert supplied["run"]["arm"] == "supplied_disease" and supplied["isolation"]["clean"]
    assert recovery(supplied)["phenotype"] == (0, 0)
    assert "given to the run as input" in supplied["components"]["phenotype"]["note"]

    graph = build_graph(case_for(entry, "main", v9_cfg))
    run = write_run(tmp_path / "main", graph)
    control = audit(run, spec_entry(spec, "dev_control"))
    assert all(d == 0 for _, d in recovery(control).values())
    assert control["control"]["outcome"] == "partial_mechanism"
    assert [(c["relation"], c["variant"]) for c in control["control"]["supported_causal_claims"]] == [
        ("regulates", None)]                                             # an element-gene link names no variant
    uncovered = audit(run, spec_entry(spec, "dev_uncovered"))
    assert recovery(uncovered)["tf_group"] == (0, 0) and recovery(uncovered)["tf_member"] == (0, 1)
    assert recovery(uncovered)["tf_family"] == (0, 0)
    assert "not in QBiC-SELEX coverage" in uncovered["components"]["tf_family"]["note"]
    ambiguous = audit(run, spec_entry(spec, "dev_ambiguous"))
    assert recovery(ambiguous)["direction"] == (0, 0)                    # "gain" names no allele: not assessable
    assert recovery(ambiguous)["target_gene"] == (1, 1)                  # SORT1 or PSRC1


def test_claims_the_run_contradicted_or_retired_earn_nothing(spec, v9_cfg, tmp_path):
    """A matched binding assay contradicts the CEBPA claim and the CEBPB claim is superseded; both stay in the
    leading hypothesis as optional claims, and neither gives member, group, family or direction credit."""
    entry = spec_entry(spec, "dev_member")
    g = ClaimGraph(case_for(entry, "main", v9_cfg))
    c_overlap = annotate(g)
    emsa = record(g, "binding_test", role="computational_investigator", evidence=[tool_evidence(
        "binding_assay", "The G allele bound CEBPA less than T in liver nuclear extract.", "EMSA:test:CEBPA",
        allele="G", direction="decreases", about_tfs=["CEBPA"], context=LIVER, about_variants=["chr2:60490908 T>G"])])
    c_cebpa = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label="CEBPA")], direction="increases",
                    context=LIVER)
    c_cebpb = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label="CEBPB")], direction="increases")
    h1 = g.add_hypothesis(HypothesisDraft(title="An element story with C/EBP side claims", claim_ids=[c_cebpa, c_cebpb],
                                          required_claim_ids=[c_overlap], mechanism_class="regulatory"), "coordinator")
    g.link(c_cebpa, emsa.evidence_ids[0], "contradicts", "computational_investigator",
           rationale="the G allele binds CEBPA less")
    g.assess(c_cebpa, "contradicted_in_scope", "a matched binding assay", "critic", g.claims[c_cebpa].version)
    c_cebpd = g.supersede_claim(c_cebpb, ClaimDraft(subjects=[VARIANT], relation="alters_binding",
                                                    objects=[EntityRef(kind="tf", label="CEBPD")],
                                                    direction="increases"),
                                "the CEBPB claim named the wrong paralog", "coordinator")
    lead(g, h1)
    result = audit(write_run(tmp_path / "run", g), entry)
    assert {x["claim_id"]: x["reason"] for x in result["answer_claims"]["excluded"]} == {
        c_cebpa: "contradicted in scope", c_cebpb: f"superseded by {c_cebpd}"}
    assert result["answer_claims"]["standing"] == [c_overlap]
    scores = recovery(result)
    assert (scores["tf_member"], scores["tf_group"], scores["tf_family"], scores["direction"]) == ((0, 1),) * 4


def rsid_graph(case, *, alias: bool) -> ClaimGraph:
    """A leading claim naming the variant by its rsID, which the clean request withheld; code's variant_annotation
    found it for the coordinates, and recorded it as the case variant's own only when alias is True."""
    g = ClaimGraph(case)
    vep = record(g, "variant_annotation", observations=VEP)
    if alias:
        assert g.add_variant_alias("rs1427407", vep.tool_call_id)
    c = claim(g, [EntityRef(kind="variant", label="rs1427407")], "alters_binding",
              [EntityRef(kind="tf", label="CEBPA")], direction="increases", effect_allele="G")
    lead(g, g.add_hypothesis(HypothesisDraft(title="CEBPA binding", required_claim_ids=[c],
                                             mechanism_class="tf_binding"), "coordinator"))
    return g


def test_only_claims_about_the_case_variant_score(spec, v9_cfg, tmp_path):
    entry = spec_entry(spec, "dev_member")
    other = audit(write_run(tmp_path / "other", rsid_graph(case_for(entry, "main", v9_cfg), alias=False)), entry)
    assert other["answer_claims"]["excluded"] == [{"claim_id": "C1", "reason": "about another variant"}]
    assert (recovery(other)["tf_member"], recovery(other)["direction"]) == ((0, 1), (0, 1))
    own = audit(write_run(tmp_path / "own", rsid_graph(case_for(entry, "main", v9_cfg), alias=True)), entry)
    assert own["run"]["variant_aliases"] == ["rs1427407"] and own["answer_claims"]["excluded"] == []
    assert (recovery(own)["tf_member"], recovery(own)["direction"]) == ((1, 1), (1, 1))
    assert own["isolation"]["clean"]                    # a tool finding the rsID is not a leak


@pytest.mark.parametrize("canonical, alias, frame", [
    ("rs1427407", True, "case"), ("RS1427407", True, "case"), ("chr2:60490908", False, "case"),
    ("2:60490908:T>G", False, "case"), ("rs1427407", False, "other"), ("chr2:60490908:T>C", True, "other")])
def test_a_canonical_id_naming_the_case_variant_earns_credit_in_a_clean_run(canonical, alias, frame, spec, v9_cfg,
                                                                            tmp_path):
    """A model may name the variant through a canonical id: the case's alias rsID once code recorded it, or its
    chrom:pos (with the case's alleles, when written). In a clean run (coordinates only) such a claim is about the
    case variant and earns credit; before the alias is recorded, or with another allele pair, it is another
    variant's and earns nothing."""
    entry = spec_entry(spec, "dev_member")
    g = ClaimGraph(case_for(entry, "main", v9_cfg))
    vep = record(g, "variant_annotation", observations=VEP)
    if alias:
        assert g.add_variant_alias("rs1427407", vep.tool_call_id)
    c = claim(g, [EntityRef(kind="variant", label="the variant", canonical_id=canonical)], "alters_binding",
              [EntityRef(kind="tf", label="CEBPA")], direction="increases", effect_allele="G")
    lead(g, cebpa_hypothesis(g, [c]))
    result = audit(write_run(tmp_path / "run", g), entry)
    assert g.claim_frame(c) == frame and result["isolation"]["clean"]
    if frame == "case":
        assert result["answer_claims"] == {"standing": [c], "excluded": []}
        assert (recovery(result)["tf_member"], recovery(result)["direction"]) == ((1, 1), (1, 1))
    else:
        assert result["answer_claims"]["excluded"] == [{"claim_id": c, "reason": "about another variant"}]
        assert (recovery(result)["tf_member"], recovery(result)["direction"]) == ((0, 1), (0, 1))


def test_the_audit_reads_the_graphs_claim_frame(spec, v9_cfg, tmp_path, monkeypatch):
    """The evaluator uses ClaimGraph.claim_frame, never a copy of its rule: whatever the graph says a claim is about,
    the audit excludes and labels it so."""
    entry = spec_entry(spec, "dev_member")
    run = write_run(tmp_path / "run", rsid_graph(case_for(entry, "main", v9_cfg), alias=True))
    assert audit(run, entry)["answer_claims"]["excluded"] == []
    monkeypatch.setattr(ClaimGraph, "claim_frame", lambda self, claim_id: "other")
    result = audit(run, entry)
    assert result["answer_claims"]["excluded"] == [{"claim_id": "C1", "reason": "about another variant"}]
    assert [c["variant"] for c in result["unsupported_causal_claims"]["claims"]] == ["other"]


def test_a_capability_case_gives_no_credit_for_a_relative(spec, v9_cfg, tmp_path):
    """dev_uncovered's TF (ARID5B) has no QBiC-SELEX model; naming a modelled TF of its family (ARID3A, group G121)
    is the substitution the case tests for, so it earns neither family nor direction credit."""
    entry = spec_entry(spec, "dev_uncovered")

    def scores(tf: str) -> dict:
        g = ClaimGraph(case_for(entry, "main", v9_cfg))
        c = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label=tf)], direction="decreases")
        lead(g, g.add_hypothesis(HypothesisDraft(title=f"{tf} binding lost", required_claim_ids=[c],
                                                 mechanism_class="tf_binding"), "coordinator"))
        return recovery(audit(write_run(tmp_path / tf, g), entry))

    relative = scores("ARID3A")
    assert (relative["tf_member"], relative["tf_family"], relative["direction"]) == ((0, 1), (0, 0), (0, 1))
    own = scores("ARID5B")
    assert (own["tf_member"], own["direction"]) == ((1, 1), (1, 1))


# --- how the run ended --------------------------------------------------------------------------------------------------

def test_run_failures_are_the_engines_limitation_stops():
    assert RUN_FAILURES == compare.LIMITATION_STOPS == {"engine_error", "cache_miss"}


def test_a_run_decided_without_a_final_comparison_names_no_answer(spec, v9_cfg, tmp_path):
    """A budget stop before the final comparison: the outcome comes from the graph alone and names no hypothesis, and
    the audit names none in its place. Nothing in the answer earns credit; the candidate stays retained."""
    entry = spec_entry(spec, "dev_member")
    g = ClaimGraph(case_for(entry, "main", v9_cfg))
    c_overlap, c_cebpa, _ = supported_cebpa(g)
    cebpa_hypothesis(g, [c_overlap, c_cebpa])
    decided = compare.decide(g, None, stop_reason="budget_model_calls", budget_stop=True, note="budget_model_calls")
    assert (decided.outcome, decided.leading_ids) == ("partial_mechanism", [])
    result = audit(write_run(tmp_path / "run", g), entry)
    assert result["run"]["answer"] == [] and result["answer_claims"] == {"standing": [], "excluded": []}
    outcome = result["outcome"]
    assert (outcome["kind"], outcome["limitation"], outcome["assessed"], outcome["names_answer"]) == (
        "explanation", None, True, False)
    assert "names no hypothesis" in outcome["note"]
    assert (recovery(result)["tf_member"], recovery(result)["direction"]) == ((0, 1), (0, 1))
    member = result["candidate_retention"]["kinds"]["member"]["candidates"][0]
    assert (member["name"], member["status"], member["stages"]["final"]) == ("CEBPA", "active", True)


@pytest.mark.parametrize("stop", sorted(RUN_FAILURES))
def test_a_run_that_assessed_nothing_is_a_limitation_not_an_abstention(stop, spec, v9_cfg, tmp_path):
    """engine_error and cache_miss runs assessed nothing: a case-level failure, so no component is scored (not a
    miss) and a control's empty answer is not a null (not an abstention), even where an engine before the review fix
    recorded the crash as no_supported_explanation. A run that assessed the case and found no supported explanation
    is the abstention: scored, and a control's null."""
    member, control = spec_entry(spec, "dev_member"), spec_entry(spec, "dev_control")

    def audited(name: str, end) -> tuple[dict, dict]:
        g = ClaimGraph(case_for(member, "main", v9_cfg))
        c_overlap = annotate(g)
        cebpa_hypothesis(g, [c_overlap, claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label="CEBPA")],
                                               direction="increases")])
        end(g)
        run = write_run(tmp_path / name, g)
        return audit(run, member), audit(run, control)

    failed, failed_control = audited("failed", lambda g: compare.decide(g, None, stop_reason=stop, budget_stop=False,
                                                                        note=f"{stop}: the run cannot go on"))
    older, older_control = audited("older", lambda g: g.set_result(RunResult(outcome="no_supported_explanation",
                                                                             stop_reason=stop)))
    abstained, abstained_control = audited("abstained", lambda g: compare.decide(g, None, stop_reason="converged",
                                                                                 budget_stop=False))
    assert failed["run"]["outcome"] == "input_or_capability_limitation"
    assert abstained["run"]["outcome"] == "no_supported_explanation"
    for result, recorded in ((failed, ""), (older, "it recorded no_supported_explanation")):
        assert {k: result["outcome"][k] for k in ("kind", "limitation", "assessed")} == {
            "kind": "limitation", "limitation": "run_failure", "assessed": False}
        assert f"stopped with {stop} and assessed nothing" in result["outcome"]["note"]
        assert recorded in result["outcome"]["note"]
        assert all(d == 0 for _, d in recovery(result).values())
        assert all(c["note"].startswith(f"not scored: the run stopped with {stop}")
                   for c in result["components"].values() if c["applicable"])
        member_candidate = result["candidate_retention"]["kinds"]["member"]["candidates"][0]
        assert member_candidate["status"] == "active"                    # retention is still reported
    for result in (failed_control, older_control):
        c = result["control"]
        assert (c["kind"], c["assessed"], c["supported_causal_claims"]) == ("limitation", False, [])
        assert c["note"].startswith(f"not a null: the run stopped with {stop}")
    assert {k: abstained["outcome"][k] for k in ("kind", "limitation", "assessed")} == {
        "kind": "abstention", "limitation": None, "assessed": True}
    assert recovery(abstained)["tf_member"] == (0, 1) and recovery(abstained)["tf_group"] == (0, 1)
    c = abstained_control["control"]
    assert (c["kind"], c["assessed"], c["note"], c["supported_causal_claims"]) == ("abstention", True, "", [])


def test_an_input_limitation_or_a_folder_without_a_result_is_not_scored(spec, v9_cfg, tmp_path):
    """A request refused as input assessed nothing, and an evidence bundle (facts, no result) answered nothing: neither
    is scored. A limitation the run concluded itself (the critic's judgement that the case cannot be assessed) is its
    answer, and is scored."""
    entry = spec_entry(spec, "dev_member")

    def audited(name: str, result: RunResult | None) -> dict:
        g = ClaimGraph(case_for(entry, "main", v9_cfg))
        record(g, "ccre_overlap", [tool_evidence("annotation", "The variant lies in cCRE EH38E0000001.",
                                                 "CCRE:EH38E0000001", about_elements=["EH38E0000001"])])
        if result is not None:
            g.set_result(result)
        return audit(write_run(tmp_path / name, g), entry)

    evidence = audited("evidence", None)
    assert {k: evidence["outcome"][k] for k in ("kind", "limitation", "assessed")} == {
        "kind": None, "limitation": "no_result", "assessed": False}
    refused = audited("refused", RunResult(outcome="input_or_capability_limitation", stop_reason="input_invalid"))
    assert {k: refused["outcome"][k] for k in ("kind", "limitation", "assessed")} == {
        "kind": "limitation", "limitation": "input", "assessed": False}
    for result in (evidence, refused):
        assert all(d == 0 for _, d in recovery(result).values())
    concluded = audited("concluded", RunResult(outcome="input_or_capability_limitation", stop_reason="converged"))
    assert {k: concluded["outcome"][k] for k in ("kind", "limitation", "assessed")} == {
        "kind": "limitation", "limitation": "capability", "assessed": True}
    assert recovery(concluded)["tf_member"] == (0, 1)


# --- isolation --------------------------------------------------------------------------------------------------------

class SavedEnsembl:
    """An offline client holding one saved Ensembl record for rs1427407 (stipulated)."""
    offline = True

    def get(self, url, **kw) -> HttpResult:
        if "/variation/human/rs1427407" in url:
            data = {"name": "rs1427407", "mappings": [{"assembly_name": "GRCh38", "seq_region_name": "2",
                                                       "start": 60490908, "end": 60490908, "strand": 1,
                                                       "allele_string": "T/G"}]}
            return HttpResult(True, 200, data, url, WHEN, cached=True)
        return HttpResult(False, None, None, url, WHEN, error=f"offline and not cached: GET {url}")


def test_isolation_checks_the_case_as_supplied(spec, v9_cfg, tmp_path):
    """Provenance notes and an rsID give the same opaque id as the clean request; the isolation check still sees
    them. What the run itself found or inferred is not a leak."""
    entry = spec_entry(spec, "dev_member")
    clean = entry["requests"]["main"]

    def isolation(name: str, graph: ClaimGraph) -> dict:
        return audit(write_run(tmp_path / name, graph), entry)["isolation"]

    noted = case_for(entry, "main", v9_cfg, provenance={"gold": "CEBPA via SORT1, PMID 12345678 (POU5F1B)"})
    problems = isolation("noted", ClaimGraph(noted))["problems"]
    assert any("provenance notes (gold)" in p for p in problems)
    leaked = next(p for p in problems if p.startswith("label-derived strings"))
    assert all(s in leaked for s in ("CEBPA", "SORT1", "12345678", "POU5F1B"))

    by_rsid = build_case(Request(**{**clean, "variant": "rs1427407"}), config=v9_cfg, http=SavedEnsembl(),
                         mode="cache_only")
    assert by_rsid.case_id == clean["request_id"]
    problems = isolation("rsid", ClaimGraph(by_rsid))["problems"]
    assert any("rsID rs1427407" in p for p in problems) and any("given as 'rs1427407'" in p for p in problems)

    g = ClaimGraph(case_for(entry, "main", v9_cfg))
    vep = record(g, "variant_annotation", observations=VEP)
    gwas = record(g, "gwas_associations", [tool_evidence(
        "association", "rs1427407 G is associated with higher LDL cholesterol.", "GWAS:test:LDL",
        about_traits=["LDL cholesterol"], allele="G", direction="increases")])
    assert g.add_variant_alias("rs1427407", vep.tool_call_id)
    assert g.add_inferred_candidate(InferredCandidate(kind="disease", label="LDL cholesterol",
                                                      basis_evidence_ids=gwas.evidence_ids), "coordinator")
    assert isolation("found", g) == {"clean": True, "problems": []}


def test_the_variants_the_run_names_are_not_leaks(spec, v9_cfg, tmp_path):
    """The rsID a tool found for the coordinates reaches the run's graph three ways: a recorded alias, the
    about_variants of evidence (C3-1), and claims naming the variant by it (a label or a canonical id). All are the
    run's own work: the gold row's identity string is in the graph, and the case as supplied is still clean."""
    entry = spec_entry(spec, "dev_member")
    g = rsid_graph(case_for(entry, "main", v9_cfg), alias=True)
    record(g, "gwas_associations", [tool_evidence(
        "association", "rs1427407 G is associated with higher LDL cholesterol.", "GWAS:test:LDL",
        about_traits=["LDL cholesterol"], allele="G", direction="increases", about_variants=["rs1427407"])])
    record(g, "qbic_inventory", observations=INVENTORY[:1], evidence=[tool_evidence(
        "prediction", "QBiC-SELEX group G035: the G allele has more predicted binding", "QBIC:test:G035",
        about_tfs=["CEBPA", "CEBPB", "CEBPE"], allele="G", direction="increases", data={"group_id": "G035"},
        about_variants=["rs1427407", "chr2:60490908 T>G"])])
    c = claim(g, [EntityRef(kind="variant", label="rs1427407", canonical_id="rs1427407")], "alters_binding",
              [EntityRef(kind="tf", label="CEBPB")], direction="increases")
    assert g.claim_frame(c) == "case"
    result = audit(write_run(tmp_path / "run", g), entry)
    assert "rs1427407" in find_label_strings(g.to_json(), label_strings(entry["row"]))
    assert result["isolation"] == {"clean": True, "problems": []}
    assert result["run"]["variant_aliases"] == ["rs1427407"]


def test_the_audit_checks_isolation_and_the_variant(spec, v9_cfg, tmp_path):
    entry = spec_entry(spec, "dev_member")
    leaked = ClaimGraph(case_for(entry, "main", v9_cfg, context=["HepG2"]))
    leaked.set_result(RunResult(outcome="no_supported_explanation", stop_reason="converged"))
    result = audit(write_run(tmp_path / "leaked", leaked), entry)
    assert not result["isolation"]["clean"] and "context" in result["isolation"]["problems"][0]
    assert any("HepG2" in p for p in result["isolation"]["problems"][1:])     # a gold context label
    assert result["run"]["answer"] == [] and recovery(result)["tf_group"] == (0, 1)    # still scored
    other = build_case(Request(variant="chr2:60490908:T>C"), config=v9_cfg, http=None, mode="cache_only")
    with pytest.raises(ValueError, match="the run is for"):
        audit(write_run(tmp_path / "other", ClaimGraph(other)), entry)
    with pytest.raises(FileNotFoundError, match="graph.json"):
        audit(tmp_path, entry)
    old = {k: v for k, v in entry.items() if k != "row"}
    with pytest.raises(ValueError, match="no CSV row"):
        audit(write_run(tmp_path / "old", ClaimGraph(case_for(entry, "main", v9_cfg))), old)


# --- candidate retention and eliminations -----------------------------------------------------------------------------

def test_candidate_retention_follows_each_stage(spec, v9_cfg, tmp_path):
    graph = build_graph(case_for(spec_entry(spec, "dev_member"), "main", v9_cfg))
    run = write_run(tmp_path / "run", graph)
    kinds = audit(run, spec_entry(spec, "dev_member"))["candidate_retention"]["kinds"]
    for kind in ("member", "group", "family", "gene"):
        assert kinds[kind]["available_after"] == dict.fromkeys(("inventory", "proposal", "activation", "final"),
                                                               True), kind
        assert kinds[kind]["candidates"][0]["status"] == "leading"
        assert kinds[kind]["candidates"][0]["dropped_by"] == []
    # A gold group listed by the inventory but never sketched is inventory_only; a gene only a rejected story named is
    # eliminated; neither is retained.
    retention = audit(run, stipulated(spec))["candidate_retention"]
    group = retention["kinds"]["group"]["candidates"][0]
    assert (group["status"], group["listed"], group["shown"]) == ("inventory_only", True, True)
    assert retention["kinds"]["group"]["available_after"] == {"inventory": True, "proposal": False,
                                                              "activation": False, "final": False}
    gene = retention["kinds"]["gene"]["candidates"][0]
    assert gene["status"] == "eliminated" and gene["hypotheses"] == {"H3": "rejected"} and gene["reinstated"] == []
    assert retention["kinds"]["gene"]["available_after"]["proposal"]
    assert retention["inventory"] == {"groups": 5, "gate_passing": 4, "sketched": 3, "inventory_only": 1,
                                      "inventory_only_groups": ["G027"], "agrees_with_metrics": {"inventory": True}}


def stipulated(spec: dict) -> dict:
    """dev_member with stipulated candidates build_graph's stories reach differently: NFIA (group G027, listed and
    never sketched) and the gene PSRC1 (named only by H3, which a matched perturbation rejects)."""
    return spec_entry(spec, "dev_member") | {"components": {
        **spec_entry(spec, "dev_member")["components"],
        "tf_member": {"applicable": True, "tfs": ["NFIA"], "needs_review": False, "review_reasons": []},
        "tf_group": {"applicable": True, "groups": [{"id": "G027", "label": "", "dbd": "SMAD",
                                                     "tfs": ["NFIA", "NFIB", "NFIC", "NFIX"]}],
                     "needs_review": False, "review_reasons": []},
        "target_gene": {"applicable": True, "genes": ["PSRC1"], "needs_review": False, "review_reasons": []}}}


def withdraw(g: ClaimGraph, claim_id: str, evidence_id: str) -> None:
    """The critic finds the contradicting passage misread and relinks it as context only: code resets the claim."""
    g.link(claim_id, evidence_id, "context_only", "critic", rationale="misread: the readout was another construct")
    assert g.claims[claim_id].assessment == "unresolved"


def test_a_reinstated_hypothesis_is_not_eliminated(spec, v9_cfg, tmp_path):
    """H3's rejection rested on C5's contradiction by E8. The critic withdraws it and code reinstates H3 as deferred:
    PSRC1 stays retained, the deferral that restored H3 is no elimination whatever its reason says (this one mentions
    an expression readout), and the reinstatement is listed for a person to check. A second rejection is final even
    when its contradiction is withdrawn again: that stale rejection is flagged."""
    g = build_graph(case_for(spec_entry(spec, "dev_member"), "main", v9_cfg))
    rejection = next(e for e in g.events if e.action == "reject" and "H3" in e.target_ids).event_id
    withdraw(g, "C5", "E8")
    reason = "the contradiction of C5 was withdrawn: the PSRC1 expression readout came from another construct"
    assert MISSING_COVERAGE.search(reason) and g.reinstate("H3", reason)
    reinstated = g.events[-1].event_id
    result = audit(write_run(tmp_path / "reinstated", g), stipulated(spec))
    gene = result["candidate_retention"]["kinds"]["gene"]["candidates"][0]
    assert (gene["name"], gene["status"], gene["hypotheses"], gene["reinstated"]) == (
        "PSRC1", "deferred", {"H3": "deferred"}, ["H3"])
    assert gene["stages"]["final"]
    assert {f["hypothesis_id"] for f in result["improper_elimination"]} == {"H2", "H4"}
    assert result["reinstatements"] == [{
        "hypothesis_id": "H3", "version": 1, "event_id": reinstated, "rejected_by": rejection, "claims": ["C5"],
        "reason": reason, "disposition": "deferred", "names_acceptable": ["gene:PSRC1"], "verdict": None}]

    g.link("C5", "E8", "contradicts", "critic", rationale="the readout stands after all")
    g.assess("C5", "contradicted_in_scope", "a matched activation after all", "critic", g.claims["C5"].version)
    assert g.hypotheses["H3"].disposition == "rejected"
    withdraw(g, "C5", "E8")
    assert g.reinstate("H3", "withdrawn again") is False                # a second rejection is final
    result = audit(write_run(tmp_path / "again", g), stipulated(spec))
    gene = result["candidate_retention"]["kinds"]["gene"]["candidates"][0]
    assert (gene["status"], gene["reinstated"]) == ("eliminated", ["H3"])
    [stale] = [f for f in result["improper_elimination"] if f["hypothesis_id"] == "H3"]
    assert (stale["step"], stale["contradicted"], stale["reinstated"]) == ("rejected", [], [reinstated])
    assert stale["flags"] == {"withdrawn_contradiction": ["C2: supported_in_scope", "C5: unresolved"]}
    assert stale["reasons"] == ["required claim C5 contradicted in scope (evidence E8)"]
    assert stale["names_acceptable"] == ["gene:PSRC1"]


@pytest.mark.parametrize("step", ["supersession", "revision"])
def test_a_candidate_a_revision_dropped_is_eliminated_not_inventory_only(step, spec, v9_cfg, tmp_path):
    """CEBPA is proposed, activated, then swapped for HNF4A because it is 'not expressed' and has 'no ChIP-seq
    peak': it was sketched and eliminated (never inventory_only), and the reason is flagged for review."""
    entry = spec_entry(spec, "dev_member")
    g = ClaimGraph(case_for(entry, "main", v9_cfg))
    record(g, "qbic_inventory", observations=INVENTORY)
    c_overlap = annotate(g)
    c_cebpa = claim(g, [VARIANT], "alters_binding", [EntityRef(kind="tf", label="CEBPA")], direction="increases")
    h1 = g.add_hypothesis(HypothesisDraft(title="CEBPA binding", required_claim_ids=[c_overlap, c_cebpa],
                                          mechanism_class="tf_binding"), "coordinator")
    reason = "CEBPA is not expressed in liver (TPM 0.3) and has no ChIP-seq peak here"
    hnf4a = ClaimDraft(subjects=[VARIANT], relation="alters_binding", objects=[EntityRef(kind="tf", label="HNF4A")],
                       direction="increases")
    if step == "supersession":
        g.supersede_claim(c_cebpa, hnf4a, reason, "coordinator", hypothesis_ids=[h1])
    else:
        g.revise_hypothesis(h1, HypothesisChanges(replace_claims={c_cebpa: g.add_claim(hnf4a, "coordinator")}),
                            reason, "coordinator")
    lead(g, h1)
    result = audit(write_run(tmp_path / "run", g, {"inventory": {"inventory_only": ["G142", "G070", "G027"]}}),
                   entry)
    retention = result["candidate_retention"]
    member = retention["kinds"]["member"]["candidates"][0]
    assert (member["name"], member["status"], member["hypotheses"]) == ("CEBPA", "eliminated", {})
    assert member["dropped_by"] == [{"hypothesis_id": h1, "version": 2, "step": step, "reason": reason}]
    assert member["stages"] == {"inventory": True, "proposal": True, "activation": True, "final": False}
    assert retention["kinds"]["group"]["candidates"][0]["status"] == "eliminated"
    assert retention["inventory"]["inventory_only_groups"] == ["G142", "G070", "G027"]   # G035 was sketched
    assert retention["inventory"]["agrees_with_metrics"] == {"inventory": True}
    [flagged] = [f for f in result["improper_elimination"] if f["step"] == step]
    assert (flagged["hypothesis_id"], flagged["reasons"], list(flagged["flags"])) == (h1, [reason],
                                                                                     ["missing_coverage"])
    assert {"member:CEBPA", "group:G035", "family:bZIP"} <= set(flagged["names_acceptable"])
    assert "HNF4A" not in flagged["dropped"] and "CEBPA" in flagged["dropped"]


def test_inventory_only_is_checked_against_a_written_bundle(spec, v9_cfg, tmp_path):
    """The audit reads inventory_only where bundle.write_bundle puts it: the bundle's own count ("inventory") and the
    engine's ("engine.inventory"). A member alternative sketches its group, so an engine count that missed it shows
    as a disagreement."""
    entry = spec_entry(spec, "dev_member")
    plain = build_graph(case_for(entry, "main", v9_cfg))
    bundle.write_bundle(plain, ENGINE_METRICS, {"mode": "fixture"}, tmp_path / "plain")
    inventory = audit(tmp_path / "plain", entry)["candidate_retention"]["inventory"]
    assert inventory["inventory_only_groups"] == ["G027"]
    assert inventory["agrees_with_metrics"] == {"inventory": True, "engine.inventory": True}

    alternative = build_graph(case_for(entry, "main", v9_cfg))
    c = claim(alternative, [VARIANT], "overlaps", [EntityRef(kind="element", label="EH38E0000002",
                                                             canonical_id="EH38E0000002")])
    alternative.add_hypothesis(HypothesisDraft(title="NFI as an alternative", required_claim_ids=[c],
                                               mechanism_class="regulatory", member_alternatives=["NFIA"]),
                               "coordinator")
    bundle.write_bundle(alternative, ENGINE_METRICS, {"mode": "fixture"}, tmp_path / "alternative")
    inventory = audit(tmp_path / "alternative", entry)["candidate_retention"]["inventory"]
    assert inventory["inventory_only_groups"] == []
    assert inventory["agrees_with_metrics"] == {"inventory": True, "engine.inventory": False}
    assert audit(write_run(tmp_path / "bare", plain, {}), entry)["candidate_retention"]["inventory"][
        "agrees_with_metrics"] == {}                                     # nothing recorded, nothing checked


def test_eliminations_for_missing_coverage_or_rankings_are_flagged(spec, v9_cfg, tmp_path):
    entry = spec_entry(spec, "dev_member")
    findings = audit(write_run(tmp_path / "run", build_graph(case_for(entry, "main", v9_cfg))),
                     entry)["improper_elimination"]
    by_id = {f["hypothesis_id"]: f for f in findings}
    assert set(by_id) == {"H2", "H4"}                     # H3's rejection rests on a matched contradiction
    assert (by_id["H2"]["step"], list(by_id["H2"]["flags"])) == ("deferred", ["missing_coverage"])
    assert "family:bZIP" in by_id["H2"]["names_acceptable"]
    assert (by_id["H4"]["step"], list(by_id["H4"]["flags"])) == ("deferred", ["more_is_better"])
    assert all(f["verdict"] is None for f in findings)


@pytest.mark.parametrize("reason", [
    "no ChIP-seq peak for CEBPD in liver", "absence of ChIP-seq signal at the locus",
    "ChIP-seq data unavailable for this TF", "TPM below 1 in liver", "CEBPD expression is low in HepG2",
    "expression is negligible in hepatocytes", "not detected by ChIP in HepG2", "zero peaks in ENCODE",
    "no evidence of occupancy", "occupancy not observed", "insufficient expression in the tissue",
    "absent from GTEx liver", "no GWAS records near the locus", "the element is not annotated as a cCRE"])
def test_reasons_citing_coverage_are_flagged(reason):
    assert MISSING_COVERAGE.search(reason)


@pytest.mark.parametrize("reason", [
    "a lower z-score than the C/EBP groups", "the smallest effect among gate-passing groups",
    "weakest predicted change", "ranked below CEBPA by |z|", "z is only 2.1, below the other groups",
    "least predicted binding change", "outranked by groups with larger effects", "the highest TPM of the paralogs"])
def test_reasons_citing_a_ranking_are_flagged(reason):
    assert MORE_IS_BETTER.search(reason)


@pytest.mark.parametrize("reason", ["a matched perturbation in hepatocytes contradicted the element-gene link",
                                    "required claim C5 contradicted in scope (evidence E8)"])
def test_a_reason_resting_on_a_contradiction_is_not_flagged(reason):
    assert not MISSING_COVERAGE.search(reason) and not MORE_IS_BETTER.search(reason)


# --- unsupported claims, fidelity, efficiency, output -----------------------------------------------------------------

def test_unsupported_causal_claims_and_the_fidelity_sheet(spec, v9_cfg, tmp_path):
    entry = spec_entry(spec, "dev_member")
    result = audit(write_run(tmp_path / "run", build_graph(case_for(entry, "main", v9_cfg))), entry)
    unsupported = result["unsupported_causal_claims"]
    assert (unsupported["count"], unsupported["required"]) == (2, 1)
    assert unsupported["by_relation"] == {"alters_binding": 1, "contributes_to_trait": 1}
    assert {(c["relation"], c["variant"]) for c in unsupported["claims"]} == {("alters_binding", "case"),
                                                                              ("contributes_to_trait", None)}
    sheet = result["evidence_fidelity"]
    assert sheet["auto_scored"] is False
    rows = [(r["claim_id"], r["evidence_id"], r["stance"]) for r in sheet["rows"]]
    assert [r[0] for r in rows] == ["C2", "C1", "C3", "C3", "C5"]       # relation order, then ids
    assert ("C5", "E8", "contradicts") in rows                           # the contradiction behind H3's rejection
    binding = next(r for r in sheet["rows"] if r["claim_id"] == "C1")
    assert binding["why_decisive"] == ["required claim of the answer H1", "decisive in comparison P1"]
    assert all(set(r["review"].values()) <= {None, ""} for r in sheet["rows"])


def test_the_fidelity_sheet_shows_which_variant_each_item_names(spec, v9_cfg, tmp_path):
    """Each decisive row says which variant the claim is about and which its evidence names. The graph now refuses a
    link from evidence about another variant; a graph written before it did may hold one, and the row shows the
    mismatch for the person checking the source (recovery counts what the answer names, never its links)."""
    entry = spec_entry(spec, "dev_member")
    g = ClaimGraph(case_for(entry, "main", v9_cfg))
    c_overlap, c_cebpa, emsa = supported_cebpa(g)
    lead(g, cebpa_hypothesis(g, [c_overlap, c_cebpa]))

    def rows(path) -> dict:
        return {(r["claim_id"], r["evidence_id"]): (r["claim_variant"], r["about_variants"], r["evidence_variant"])
                for r in audit(path, entry)["evidence_fidelity"]["rows"]}

    assert rows(write_run(tmp_path / "run", g)) == {(c_overlap, "E1"): ("case", [], None),
                                                    (c_cebpa, emsa): ("case", ["chr2:60490908 T>G"], "case")}
    state = json.loads(g.to_json())
    state["evidence"][emsa]["about_variants"] = ["rs629301"]        # an LD partner's EMSA, linked before C3-1
    legacy = tmp_path / "legacy"
    legacy.mkdir()
    (legacy / "graph.json").write_text(json.dumps(state))
    assert rows(legacy)[(c_cebpa, emsa)] == ("case", ["rs629301"], "other")
    assert recovery(audit(legacy, entry))["tf_member"] == (1, 1)


def test_efficiency_comes_from_the_metrics_and_the_graph(spec, v9_cfg, tmp_path):
    entry = spec_entry(spec, "dev_member")
    result = audit(write_run(tmp_path / "run", build_graph(case_for(entry, "main", v9_cfg))), entry)
    eff = result["efficiency"]
    assert eff["metrics"] == ENGINE_METRICS
    assert (eff["graph"]["model_calls"], eff["graph"]["cost_usd"]) == (5, 0.0123)
    assert (eff["graph"]["tool_calls_code"], eff["graph"]["tool_calls_agent"]) == (3, 2)
    assert eff["graph"]["tool_calls_by_status"] == {"success": 5}
    assert result["run"]["mode"] == "fixture"


def test_write_evaluation_is_deterministic_and_never_overwrites(spec, v9_cfg, tmp_path):
    entry = spec_entry(spec, "dev_member")
    run = write_run(tmp_path / "run", build_graph(case_for(entry, "main", v9_cfg)))
    path = write_evaluation(run, entry)
    assert path == run / EVALUATION_FILE
    assert json.loads(path.read_text()) == audit(run, entry) == audit(run, entry)
    with pytest.raises(FileExistsError, match="never overwritten"):
        write_evaluation(run, entry)


def test_the_audit_command_is_the_documented_call(v9_cfg, tmp_path, capsys):
    """`v2m v9 audit --run DIR --case ID` is write_evaluation(DIR, spec_entry(load_gold_spec(config=cfg), ID),
    config=cfg): the call works on the committed (unreviewed) spec, and the command writes the same evaluation.json.
    The run is for a gold variant and holds no hypothesis: plumbing only, nothing is chosen by it."""
    case_id = "rs12740374"
    entry = spec_entry(load_gold_spec(config=v9_cfg), case_id)

    def run(name: str):
        g = ClaimGraph(case_for(entry, "main", v9_cfg))
        g.set_result(RunResult(outcome="no_supported_explanation", stop_reason="converged"))
        return write_run(tmp_path / name, g)

    called = write_evaluation(run("called"), spec_entry(load_gold_spec(config=v9_cfg), case_id), config=v9_cfg)
    content = json.loads(called.read_text())
    assert (content["spec"]["case_id"], content["spec"]["status"], content["spec"]["provisional"]) == (
        case_id, "unreviewed", True)
    assert content["isolation"] == {"clean": True, "problems": []} and content["run"]["arm"] == "main"
    assert content["outcome"]["kind"] == "abstention" and content["outcome"]["assessed"]
    command = run("command")
    assert cli.main(["v9", "audit", "--run", str(command), "--case", case_id]) == 0
    assert capsys.readouterr().out.strip() == str(command / EVALUATION_FILE)
    assert json.loads((command / EVALUATION_FILE).read_text()) == content


@pytest.mark.parametrize("cap", [None, 0, -1.0, math.nan, math.inf, True, "5"])
def test_run_suite_refuses_without_a_positive_cap(cap, tmp_path):
    with pytest.raises(SuiteRefusal, match="explicit positive currency cap"):
        run_suite(tmp_path / "suite.json", cap)


def test_run_suite_stops_short_of_running_with_a_cap(tmp_path):
    with pytest.raises(NotImplementedError, match="approved cap and profile"):
        run_suite(tmp_path / "suite.json", 5.0)
