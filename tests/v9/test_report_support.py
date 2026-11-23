"""Graphs and bundles shared by the report tests (this module holds builders only, no tests).

Biological cases use the development variant rs1427407 (chr2:60490908 T>G), never a gold case. TF, gene and trait
names, observations and inventory rows are stipulated for the tests and are not claims about that variant.
"""

from pathlib import Path

from variant2mechanism.config import load_config
from variant2mechanism.v9 import bundle
from variant2mechanism.v9.fixtures import FixtureToolRunner, load_fixture
from variant2mechanism.v9.graph import ClaimDraft, ClaimGraph, EntityRef, GraphUpdate, HypothesisDraft
from variant2mechanism.v9.schemas import (
    Case,
    ContextScope,
    Evidence,
    NextExperiment,
    PairComparison,
    Question,
    RunResult,
    ToolCall,
    ToolRequest,
    Variant,
    WeakLink,
)
from variant2mechanism.v9.tools import ToolRunner

VARIANT = EntityRef(kind="variant", label="rs1427407")
ELEMENT = EntityRef(kind="element", label="enhancer", canonical_id="EH38E0000001")
HEPG2 = ContextScope(label="HepG2", source="supplied")


def dev_case() -> Case:
    return Case(case_id="DEV-1", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G", rsid="rs1427407"))


def tf(symbol: str) -> EntityRef:
    return EntityRef(kind="tf", label=symbol)


def gene(symbol: str) -> EntityRef:
    return EntityRef(kind="gene", label=symbol)


def claim(g: ClaimGraph, subjects, relation, objects, direction="unspecified", context=None, deps=(), **kw) -> str:
    return g.add_claim(ClaimDraft(subjects=subjects, relation=relation, objects=objects, direction=direction,
                                  context=context, dependencies=list(deps), **kw), "coordinator")


def tool_evidence(g: ClaimGraph, cls: str, text: str, *, tool: str = "test_tool", group: str | None = None,
                  **fields) -> str:
    """One Evidence item recorded with its own tool call (how adapter evidence enters a graph)."""
    ev = Evidence(evidence_class=cls, observed_result=text, independence_group=group or text, origin="tool", **fields)
    call = g.record_tool_call(ToolCall(tool_call_id=g.reserve_tool_call_id(), tool_name=tool, provider="test provider",
                                       dataset_release="r1", execution_status="success",
                                       retrieval_status="records_found", requested_by="computational_investigator",
                                       charged_to="agent"), [ev])
    return call.evidence_ids[0]


def inventory_call(g: ClaimGraph, rows: list[dict]) -> ToolCall:
    """A qbic_inventory call shaped as contract C2 fixes it: one observation per group, Evidence for the groups that
    pass the gate (class prediction, about every member, data.group_id)."""
    evidence = [Evidence(evidence_class="prediction", origin="tool", independence_group=f"QBIC:test:{r['group_id']}",
                         observed_result=f"QBiC-SELEX group {r['group_id']}: the {r['binds_more']} allele binds more "
                                         f"(best model {r['best_model']}, z {r['z']}).",
                         about_tfs=[m["tf"] for m in r["members"]], allele="G" if r["binds_more"] == "alt" else "T",
                         direction="increases", about_variants=["rs1427407"],
                         data={"group_id": r["group_id"], "best_model": r["best_model"], "z": r["z"],
                               "mapping": {m["tf"]: m["mapping"] for m in r["members"]}})
                for r in rows if r["passes_gate"]]
    return g.record_tool_call(ToolCall(tool_call_id=g.reserve_tool_call_id(), tool_name="qbic_inventory",
                                       provider="QBiC-SELEX cache", dataset_release="primary collection",
                                       execution_status="success", retrieval_status="records_found",
                                       observations=rows, requested_by="code", charged_to="code"), evidence)


def discordant_inventory(g: ClaimGraph) -> ToolCall:
    """A qbic_inventory call shaped as the adapters write one: group G049's gate-passing models disagree about the
    allele, so it has one Evidence item per allele (data.discordant), the item for the row's allele (G, the alt that
    its best model favours) first; G002's models agree (one item); G003 does not pass the gate (none)."""
    members = [{"tf": "ELF5", "mapping": "cisbp"}, {"tf": "SPI1", "mapping": "own"}, {"tf": "SPIB", "mapping": "own"}]
    split = {**inventory_row(49, True, members, z=21.04), "best_model": "SPIB_MODEL", "binds_more": "alt"}
    agree, below = inventory_row(2, True), inventory_row(3, False)

    def item(row: dict, allele: str, tfs: list[str], z: float, discordant: bool) -> Evidence:
        return Evidence(evidence_class="prediction", origin="tool", independence_group=f"QBIC:test:{row['group_id']}",
                        observed_result=f"QBiC-SELEX group {row['group_id']}: models of {', '.join(tfs)} predict more "
                                        f"binding to {allele} (z {z}).",
                        about_tfs=tfs, allele=allele, direction="increases", about_variants=["rs1427407"],
                        data={"group_id": row["group_id"], "z": z, "discordant": discordant})

    evidence = [item(split, "G", ["SPI1", "SPIB"], 21.04, True), item(split, "T", ["ELF5", "SPI1"], -14.1, True),
                item(agree, "G", ["TF2A", "TF2B"], agree["z"], False)]
    return g.record_tool_call(ToolCall(tool_call_id=g.reserve_tool_call_id(), tool_name="qbic_inventory",
                                       provider="QBiC-SELEX cache", dataset_release="primary collection",
                                       execution_status="success", retrieval_status="records_found",
                                       observations=[split, agree, below], requested_by="code", charged_to="code"),
                              evidence)


def inventory_row(i: int, passes: bool, members=None, z: float | None = None) -> dict:
    members = members or [{"tf": f"TF{i}A", "mapping": "own"}, {"tf": f"TF{i}B", "mapping": "cisbp"}]
    return {"group_id": f"G{i:03d}", "group_label": f"bZIP, {len(members)} models", "dbd": "bZIP",
            "members": members, "paralog_stem": None, "best_model": f"MODEL_{i}", "binds_more": "alt",
            "z": z if z is not None else round(3.0 + (i * 37 % 11), 2), "effect": 0.5, "p": 1e-9, "n_pass": 1 if passes
            else 0, "n_models": len(members), "passes_gate": passes}


def rich_graph() -> ClaimGraph:
    """A development-case graph with every display status (supported, predicted, associated, contested,
    contradicted, unresolved), a broken premise, a superseded claim, a refused update, rejected, deferred, leading and
    active hypotheses, a comparison, a question, an inventory and a result."""
    g = ClaimGraph(dev_case())
    hepg2 = ContextScope(label="HepG2", source="evidence")
    inventory = inventory_call(g, [inventory_row(1, True, [{"tf": "TFX", "mapping": "own"},
                                                           {"tf": "TFZ", "mapping": "cisbp"}], z=5.1),
                                   inventory_row(2, True), inventory_row(3, False)])
    c_overlap = claim(g, [VARIANT], "overlaps", [ELEMENT], assertion_text="rs1427407 lies in enhancer EH38E0000001")
    c_bind = claim(g, [VARIANT], "alters_binding", [tf("TFX")], "increases", assertion_text="G increases TFX binding")
    c_reg = claim(g, [ELEMENT], "regulates", [gene("GENE1")], "increases", HEPG2,
                  assertion_text="The enhancer raises GENE1 in HepG2")
    c_act = claim(g, [VARIANT], "alters_regulatory_activity", [ELEMENT], "increases", HEPG2,
                  assertion_text="G raises enhancer activity in HepG2")
    c_down = claim(g, [ELEMENT], "regulates", [gene("GENE2")], "decreases", HEPG2,
                   assertion_text="The enhancer represses GENE2 in HepG2")
    c_trait = claim(g, [gene("GENE2")], "contributes_to_trait", [EntityRef(kind="phenotype", label="LDL cholesterol")],
                    "decreases", deps=[c_down], assertion_text="Lower GENE2 lowers LDL cholesterol")
    c_proc = claim(g, [gene("GENE1")], "affects_process", [EntityRef(kind="process", label="lipid uptake")],
                   "increases", assertion_text="GENE1 raises lipid uptake")
    h_reject = g.add_hypothesis(HypothesisDraft(title="The enhancer represses GENE2, lowering LDL",
                                                claim_ids=[c_overlap], required_claim_ids=[c_down, c_trait],
                                                mechanism_class="regulatory", endpoint="LDL cholesterol",
                                                reason_for_inclusion="eQTL direction"), "coordinator")
    h_lead = g.add_hypothesis(HypothesisDraft(title="G raises enhancer activity and GENE1",
                                              claim_ids=[c_bind, c_act, c_proc], required_claim_ids=[c_overlap, c_reg],
                                              mechanism_class="regulatory", reason_for_inclusion="overlap and eQTL"),
                              "coordinator")
    h_defer = g.add_hypothesis(HypothesisDraft(title="GENE1 drives lipid uptake", required_claim_ids=[c_proc],
                                               mechanism_class="other", disposition="deferred",
                                               disposition_reason="lower priority than the gene link",
                                               revisit_trigger="a GENE1 perturbation becomes available"),
                               "coordinator")
    h_other = g.add_hypothesis(HypothesisDraft(title="G raises activity", required_claim_ids=[c_act],
                                               mechanism_class="regulatory", reason_for_inclusion="reporter data"),
                               "coordinator")
    e_overlap = tool_evidence(g, "annotation", "The variant lies in cCRE EH38E0000001.", tool="ccre_overlap",
                              about_elements=["EH38E0000001"], source_ids=["ENCSR000AAA"])
    e_pred = inventory.evidence_ids[0]
    e_eqtl = tool_evidence(g, "association", "GTEx: G is associated with higher GENE1 (NES 0.4).", tool="gtex_eqtl",
                           about_genes=["GENE1"], allele="G", direction="increases", source_ids=["GTEx:rs1427407"],
                           about_elements=["EH38E0000001"],     # an element-gene link names the element it is about
                           context=ContextScope(label="Liver", source="evidence"))
    e_rep1 = tool_evidence(g, "reporter_assay", "Luciferase: the G construct is twice as active in HepG2.",
                           allele="G", direction="increases", context=hepg2, about_elements=["EH38E0000001"],
                           source_ids=["PMID:11111"], about_variants=["rs1427407"])
    e_rep2 = tool_evidence(g, "reporter_assay", "MPRA: the G allele lowers activity in HepG2.", allele="G",
                           direction="decreases", context=hepg2, about_elements=["EH38E0000001"],
                           source_ids=["PMCID:PMC22222"], about_variants=["rs1427407"])
    e_crispr = tool_evidence(g, "perturbation", "CRISPRi of the enhancer lowers GENE2 in HepG2.", direction="increases",
                             context=hepg2, about_genes=["GENE2"], about_elements=["EH38E0000001"],
                             source_ids=["doi:10.1000/test.1"])
    tool_evidence(g, "expression", "TFX is expressed in liver (TPM 12).", tool="tf_expression", about_tfs=["TFX"],
                  context=ContextScope(label="Liver", source="evidence"))
    critic = "critic"
    g.link(c_overlap, e_overlap, "supports", "computational_investigator", "the cCRE contains the variant")
    g.assess(c_overlap, "supported_in_scope", "annotation overlap", critic, g.claims[c_overlap].version)
    g.link(c_bind, e_pred, "supports", "computational_investigator", "the TFX model favours G")
    g.link(c_reg, e_eqtl, "supports", "computational_investigator", "same direction in liver")
    g.link(c_act, e_rep1, "supports", "literature_investigator", "construct more active")
    g.link(c_act, e_rep2, "contradicts", "literature_investigator", "MPRA disagrees")
    g.assess(c_act, "contested", "reporters disagree", critic, g.claims[c_act].version)
    g.apply_updates([GraphUpdate(kind="attach_evidence", claim_id=c_down, evidence_id=e_crispr, stance="supports",
                                 rationale="misread")], "computational_investigator")
    g.link(c_down, e_crispr, "contradicts", "computational_investigator", "CRISPRi raises the opposite expectation")
    g.assess(c_down, "contradicted_in_scope", "direct perturbation disagrees", critic, g.claims[c_down].version)
    g.propagate()
    g.supersede_claim(c_bind, ClaimDraft(subjects=[VARIANT], relation="alters_binding", objects=[tf("TFZ")],
                                         direction="increases", assertion_text="G increases TFZ binding"),
                      "the group's mapped member TFZ fits the context better", "coordinator", [h_lead])
    g.add_question(Question(text="Is the GENE1 link causal?", target_claim_ids=[c_reg], hypothesis_ids=[h_lead],
                            route="literature"), "coordinator")
    g.add_comparison(PairComparison(a=h_lead, b=h_other, outcome="A_preferred", decisive_claim_ids=[c_reg],
                                    decisive_gaps=["no GENE1 perturbation"], reason="H2 has gene-level support"),
                     critic)
    g.set_disposition(h_lead, "leading", "preferred over the reporter-only story", "code")
    g.set_result(RunResult(outcome="partial_mechanism", stop_reason="converged", leading_ids=[h_lead],
                           summary="The enhancer story leads; its gene link is associated only.",
                           weakest_links=[WeakLink(hypothesis_id=h_lead, claim_id=c_reg, why="associated only (eQTL)")],
                           next_experiments=[NextExperiment(text="CRISPRi of the enhancer in HepG2, measuring GENE1",
                                                            distinguishes=[h_lead, h_other], claim_ids=[c_reg])],
                           uninvestigated_questions=["Does TFZ occupy the enhancer in HepG2?"]))
    assert {g.hypotheses[h_reject].disposition, g.hypotheses[h_defer].disposition} == {"rejected", "deferred"}
    return g


def synthetic_graph(run_dir: Path | None = None) -> tuple[ClaimGraph, FixtureToolRunner]:
    """The plan's synthetic repair scenario, its tool data answered by FixtureToolRunner (raw files in run_dir)."""
    fixture = load_fixture("synthetic_repair")
    g = ClaimGraph(fixture.case)
    runner = FixtureToolRunner(fixture, run_dir=run_dir)
    synthetic_steps(g, runner)
    return g, runner


def synthetic_steps(g: ClaimGraph, runner: ToolRunner) -> None:
    """The scenario's claims, tool calls, links and decisions, against any runner (fixture or recorded replay)."""
    v, e = EntityRef(kind="variant", label="V"), EntityRef(kind="element", label="E", canonical_id="SYN:E")
    x, y, p = gene("X"), gene("Y"), EntityRef(kind="phenotype", label="phenotype P")
    cx = ContextScope(label="context X", biosample="context X", source="supplied")
    f0 = claim(g, [v], "overlaps", [e], mechanism_class="regulatory", assertion_text="V overlaps element E")
    f1 = claim(g, [e], "regulates", [x], "decreases", cx, mechanism_class="regulatory",
               assertion_text="Activating element E decreases gene X expression in context X")
    f2 = claim(g, [x], "contributes_to_trait", [p], "decreases", deps=[f1], mechanism_class="regulatory",
               assertion_text="The decrease in gene X explains phenotype P")
    g.add_hypothesis(HypothesisDraft(title="E represses X, which explains P", claim_ids=[f0],
                                     required_claim_ids=[f1, f2], mechanism_class="regulatory",
                                     endpoint="phenotype P"), "coordinator")
    role = "computational_investigator"
    s0 = runner.run(ToolRequest(tool="syn_element_overlap"), g.case, g, role)
    s1 = runner.run(ToolRequest(tool="syn_element_perturbation", params={"gene": "x"}), g.case, g, role)
    runner.run(ToolRequest(tool="syn_element_perturbation", params={"gene": "Y"}), g.case, g, role)
    g.apply_updates([
        GraphUpdate(kind="attach_evidence", claim_id=f0, evidence_id=s0.evidence_ids[0], stance="supports",
                    rationale="S0 places V inside E", suggested_assessment="supported_in_scope", base_version=1),
        GraphUpdate(kind="attach_evidence", claim_id=f1, evidence_id=s1.evidence_ids[0], stance="supports",
                    rationale="misread"),
        GraphUpdate(kind="attach_evidence", claim_id=f1, evidence_id=s1.evidence_ids[0], stance="contradicts",
                    rationale="the matched intervention increases X", suggested_assessment="contradicted_in_scope",
                    base_version=1)], role)
    f3 = claim(g, [e], "regulates", [y], context=cx, mechanism_class="regulatory",
               assertion_text="Element E regulates gene Y")
    h2 = g.add_hypothesis(HypothesisDraft(title="E regulates Y", claim_ids=[f0], required_claim_ids=[f3],
                                          mechanism_class="regulatory", origin="regenerated", endpoint="phenotype P"),
                          "coordinator")
    g.assess(f3, "unresolved", "the fixture has no perturbation record for gene Y", "critic", 1)
    g.propagate()
    g.set_result(RunResult(outcome="no_supported_explanation", stop_reason="regeneration_limit",
                           summary="H1 was rejected by a matched contradiction; H2 stays unresolved.",
                           next_experiments=[NextExperiment(text="Perturb element E and measure gene Y in context X",
                                                            distinguishes=[h2], claim_ids=[f3])]))


def reinstatement_graph() -> ClaimGraph:
    """Code rejections whose contradictions were withdrawn, on the development case (stipulated observations).
    H1 is rejected when C1 (the enhancer represses GENE1 in HepG2) is contradicted in scope; C1 is reassessed as
    misread and code reinstates H1 as deferred. H2 is rejected on C2, reinstated, rejected again by the same rule, and
    its contradiction withdrawn again: a second rejection is final, so H2 stays rejected although its rejection no
    longer stands (the engine's audit note records it). Q2 repeats Q1, which was answered, and code closes it as
    refused."""
    g = ClaimGraph(dev_case())
    hepg2 = ContextScope(label="HepG2", source="evidence")
    critic = "critic"
    represses = [claim(g, [ELEMENT], "regulates", [gene(symbol)], "decreases", HEPG2,
                       assertion_text=f"The enhancer represses {symbol} in HepG2") for symbol in ("GENE1", "GENE2")]
    h1, h2 = (g.add_hypothesis(HypothesisDraft(title=f"The enhancer represses {symbol}", required_claim_ids=[c],
                                               mechanism_class="regulatory"), "coordinator")
              for symbol, c in zip(("GENE1", "GENE2"), represses, strict=True))
    for c, symbol in zip(represses, ("GENE1", "GENE2"), strict=True):
        raised = tool_evidence(g, "perturbation", f"Activating the enhancer raised {symbol} in HepG2.",
                               direction="increases", context=hepg2, about_genes=[symbol],
                               about_elements=["EH38E0000001"])
        g.link(c, raised, "contradicts", "computational_investigator", f"a matched activation raises {symbol}")
    f1, f2 = represses
    g.assess(f1, "contradicted_in_scope", "matched contradiction", critic, g.claims[f1].version)
    g.assess(f1, "unresolved", "the activation used another construct: misread", critic, g.claims[f1].version)
    assert g.reinstate(h1, "the activation used another construct") is True
    for assessment in ("contradicted_in_scope", "unresolved", "contradicted_in_scope", "unresolved"):
        g.assess(f2, assessment, f"reviewed again: {assessment}", critic, g.claims[f2].version)
        if assessment == "unresolved" and g.hypotheses[h2].disposition == "rejected":
            g.reinstate(h2, "")
    assert g.hypotheses[h2].disposition == "rejected" and g.reinstate(h2, "withdrawn again") is False
    why = "it was reinstated once already, and a second rejection is final"      # as the engine notes it
    g.log("audit", "code", f"the rejection of {h2} no longer stands: none of its required claims ({f2}) is "
                           f"contradicted in scope now; code did not reinstate it ({why}), so it is disclosed, not "
                           "reversed", target_ids=[h2], details={"stale_rejection": h2, "reinstated": False, "why": why})
    question = "Does an allele-specific reporter assay of the enhancer exist?"
    q1 = g.add_question(Question(text=question, target_claim_ids=[f1], hypothesis_ids=[h1], route="literature"),
                        "coordinator")
    g.update_question(q1, "answered", "literature_investigator", "No allele-specific reporter assay was found.")
    q2 = g.add_question(Question(text=question, target_claim_ids=[f1], hypothesis_ids=[h1], route="literature"),
                        "coordinator")
    g.update_question(q2, "refused", "code", f"not asked again: it repeats {q1} (same route, tool requests and target "
                                             f"claims, none changed since); see {q1}'s answer")
    g.set_result(RunResult(outcome="no_supported_explanation", stop_reason="converged",
                           summary="No hypothesis is supported; H1 was reinstated after a misread contradiction."))
    assert [g.hypotheses[h].disposition for h in (h1, h2)] == ["deferred", "rejected"]
    return g


def write_run(g: ClaimGraph, run_dir: Path, mode: str = "cache_only", metrics: dict | None = None,
              parts: dict | None = None, extra: dict | None = None) -> Path:
    """manifest + bundle files for a graph, into run_dir (created when missing). A graph with a result is written as
    an engine run (engine parts in the manifest, `parts` when given); one without, as `v2m v9 evidence` writes its
    bundle (no parts). `extra` adds manifest keys (a replay's replay_of)."""
    if parts is None:
        parts = {"stop_reason": g.result.stop_reason} if g.result else {}
    manifest = bundle.build_manifest(request={"variant": g.case.variant.input_text or g.case.variant.key},
                                     case=g.case, mode=mode, config=load_config(), manifest_parts=parts,
                                     graph=g, profile="release", created="2026-11-08T12:00:00+00:00")
    return bundle.write_bundle(g, metrics or {"model_calls": 0}, {**manifest, **(extra or {})}, run_dir)


def synthetic_run(tmp_path: Path) -> tuple[ClaimGraph, Path]:
    run = bundle.new_run_dir(tmp_path / "synthetic")
    g, _ = synthetic_graph(run)
    write_run(g, run, mode="fixture")
    return g, run


def runner_for(registry, run_dir: Path | None = None) -> ToolRunner:
    return ToolRunner(mode="cache_only", run_dir=run_dir, registry=registry, clock=lambda: "2026-11-08T12:00:00+00:00")
