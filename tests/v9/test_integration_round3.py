"""The round-3 fields across modules (the reconcile step; each module's own tests pin its side of the seams):

- about_variants: the literature investigator's strict experiment (roles.V9Experiment) -> roles.experiment_record ->
  the real literature module (find_read, load_article, evidence_from_experiment: a variant is kept only where the
  paper names it for that experiment) -> graph.add_evidence -> graph.link (evidence about one variant never bears on
  a claim about another; an allele comparison must say which variant's alleles it compared) -> the bundle -> the
  report's evidence inspector (each name read by graph.variant_mention);
- reinstatements: graph.reinstate in the engine -> its metrics -> the bundle that `v2m v9 fixture` writes -> the
  report (run summary, hypothesis states, timeline) and the evaluator's reading -> `v2m v9 replay`, identical; and a
  stale rejection the graph keeps, read alike by the engine and the report (compare.stale_rejections);
- the sketched-groups rule: the engine's metrics, the bundle's metrics.json and the evaluator read one rule
  (graph.sketched_groups) over the rows adapters.inventory_rows joins (a discordant group has one item per allele).

Everything is synthetic (SYN- cases, stipulated article text and scripted roles): not biological evidence. No network,
no provider, no data/ beyond what the isolated test config points at.
"""

import copy
import json
from pathlib import Path

from variant2mechanism import cli
from variant2mechanism.v9 import bundle, compare, evaluation, graph, investigate
from variant2mechanism.v9.bundle import build_manifest, load_bundle, write_bundle
from variant2mechanism.v9.fixtures import Fixture, load_fixture
from variant2mechanism.v9.literature import Article, ArticleSection
from variant2mechanism.v9.report import report_data

from .test_engine_support import events, run_fixture

# --- about_variants, from the strict experiment to the report ------------------------------------------------------

CASE_RSID, LD_PARTNER_RSID = "rs9000006", "rs9000077"
CASE_EMSA = f"In EMSA, TFA bound the G allele of {CASE_RSID} more strongly than the A allele."
LD_EMSA = f"In a second EMSA, TFA bound the C allele of {LD_PARTNER_RSID} more strongly than the T allele."
KNOCKDOWN = "Knockdown of TFA lowered the activity of element E in context X cells."
ARTICLE = Article(pmid="90000006", pmcid="PMC9000006", title="Two variants near element E (a stipulated study)",
                  publication_type="research article", route="europepmc_fulltext", access="full_text",
                  sections=[ArticleSection(location="abstract/p1", heading="Abstract",
                                           text=f"We tested {CASE_RSID} and a nearby variant, {LD_PARTNER_RSID}."),
                            ArticleSection(location="sec2/p1", heading="Results", text=CASE_EMSA),
                            ArticleSection(location="sec2/p2", heading="Results", text=LD_EMSA),
                            ArticleSection(location="sec2/p3", heading="Results", text=KNOCKDOWN)])
V6 = {"kind": "variant", "label": "V6", "canonical_id": None, "members": []}
TFA = {"kind": "tf", "label": "TFA", "canonical_id": None, "members": []}
ELEMENT = {"kind": "element", "label": "E", "canonical_id": "SYN:E", "members": []}


def experiment(passage: str, location: str, *, variants: list[str], manipulated: str, allele: str | None,
               intervention: str, endpoint: str, direction: str = "increases") -> dict:
    """A strict V9Experiment as the literature investigator returns it."""
    return {"source_id": "PMID:90000006", "pmcid": "PMC9000006", "doi": None, "publication_type": "research article",
            "access": "full_text", "location": location, "passage": passage, "organism": "human",
            "tissue_or_cell": "context X", "treatment": "", "genotype_or_allele": "", "intervention": intervention,
            "endpoint": endpoint, "comparator": "the other allele" if manipulated == "allele" else "control",
            "result": passage, "direction": direction, "scope_supports": "as stated",
            "scope_does_not_test": "the endogenous locus", "about_tfs": ["TFA"], "about_genes": [],
            "about_elements": ["E"] if manipulated == "tf" else [], "about_traits": [], "about_variants": variants,
            "manipulated": manipulated, "compared_allele": allele, "authors_hypothesis_vs_result": "result"}


def attach(index: int, claim: str) -> dict:
    return {"kind": "attach_evidence", "claim_id": claim, "base_version": None, "evidence_id": None,
            "experiment_index": index, "stance": "supports", "applicability": None,
            "rationale": "the extracted experiment, offered for this claim", "limitations": [],
            "suggested_assessment": None, "new_claim": None}


def answer(status: str, experiments=(), updates=(), follow_up=()) -> dict:
    return {"question_id": "Q1", "status": status, "answer_summary": "a stipulated study compares alleles",
            "claim_ids": ["C1"], "tool_call_ids": [], "experiments": list(experiments),
            "proposed_updates": list(updates), "remaining_gap": "", "next_question": "",
            "follow_up_actions": list(follow_up)}


def literature_fixture() -> Fixture:
    """SYN-6 (rsID supplied): H1 says V6 alters TFA binding (C1, required) and the activity of element E (C2). The
    paper's Results report an EMSA of V6, an EMSA of a nearby variant and a TFA knockdown. The extraction offers five
    records: the EMSA of V6 as the passage names it; the nearby variant's EMSA as the passage names it; the same
    EMSA mislabelled as V6's (a record the paper does not support); an allele comparison naming no variant; and the
    knockdown offered for what V6's alleles do."""
    read = {"pmcid": "PMC9000006", "focus": ["TFA"]}
    extract = answer("answered", [
        experiment(CASE_EMSA, "sec2/p1", variants=[CASE_RSID], manipulated="allele", allele="G",
                   intervention="EMSA with both alleles", endpoint="TFA binding"),
        experiment(LD_EMSA, "sec2/p2", variants=[LD_PARTNER_RSID], manipulated="allele", allele="C",
                   intervention="EMSA with both alleles", endpoint="TFA binding"),
        experiment(LD_EMSA, "sec2/p2", variants=[CASE_RSID], manipulated="allele", allele="C",
                   intervention="EMSA with both alleles", endpoint="TFA binding"),
        experiment(CASE_EMSA, "sec2/p1", variants=[], manipulated="allele", allele="G",
                   intervention="EMSA with both alleles", endpoint="TFA binding"),
        experiment(KNOCKDOWN, "sec2/p3", variants=[], manipulated="tf", allele=None,
                   intervention="TFA knockdown", endpoint="element E activity", direction="decreases")],
        [attach(0, "C1"), attach(1, "C1"), attach(2, "C1"), attach(3, "C1"), attach(4, "C2")])
    sketch = {"key": "h", "title": "V6 changes TFA binding and element E activity", "summary": "",
              "mechanism_class": "tf_binding", "endpoint": "molecular", "context": None, "activate": True,
              "deferral_reason": None, "revisit_trigger": None, "reason_kind": "literature_report",
              "reason_detail": "a stipulated EMSA may compare the two alleles of V6", "member_alternatives": [],
              "missing_links": [], "assumptions": [], "replaces": None, "reuse_claims": [],
              "claims": [{"key": "bind", "subjects": [V6], "relation": "alters_binding", "objects": [TFA],
                          "direction": "increases", "effect_allele": None, "context": None,
                          "assertion_text": "The G allele of V6 binds TFA more than the A allele", "required": True,
                          "depends_on": [], "initial_links": []},
                         {"key": "act", "subjects": [V6], "relation": "alters_regulatory_activity",
                          "objects": [ELEMENT], "direction": "increases", "effect_allele": None, "context": None,
                          "assertion_text": "The G allele of V6 raises the activity of element E", "required": False,
                          "depends_on": [], "initial_links": []}]}
    question = {"text": "Has an EMSA compared the two alleles of V6?", "route": "literature",
                "target_claims": ["bind", "act"], "hypotheses": ["h"],
                "rubric": {"consequence": "high", "discrimination": "high", "applicability": "high", "cost": "low"},
                "possible_outcomes": ["an allele comparison", "nothing found"],
                "actions": [{"tool": "literature_search", "params_json": '{"query": "TFA V6"}',
                             "purpose": "find a primary study"}]}
    return Fixture.model_validate({
        "description": "about_variants across modules (reconcile test): stipulated, not biological data.",
        "case": {"case_id": "SYN-6", "variant": {"chrom": "SYN", "pos": 6, "ref": "A", "alt": "G",
                                                 "rsid": CASE_RSID}},
        "tools": {
            "literature_search": {
                "spec": {"route": "literature", "assemblies": [], "description": "Synthetic search.",
                         "params": {"query": {"type": "str", "required": True}}},
                "responses": [{"params": {"query": "TFA V6"},
                               "observations": [{"pmid": "90000006", "pmcid": "PMC9000006",
                                                 "title": ARTICLE.title}]}]},
            "literature_read": {
                "spec": {"route": "literature", "assemblies": [], "description": "Synthetic full-text read.",
                         "params": {"pmcid": {"type": "str", "required": True}, "focus": {"type": "list[str]"}},
                         "fulltext_params": ["pmcid"]},
                "responses": [{"params": read, "raw": ARTICLE.model_dump(mode="json"),
                               "observations": [{"kind": "passage", "location": s.location, "heading": s.heading,
                                                 "text": s.text} for s in ARTICLE.sections]}]}},
        "roles": {
            "coordinator": [
                {"directions": ["literature-led"], "inferred_candidates": [], "fourth_active_reason": None,
                 "reactivate": [], "hypotheses": [sketch], "questions": [question]},
                {"hypothesis_updates": [], "assessments": [], "questions": [],
                 "stop": {"stop": True, "reason": "the study is read"}}],
            "literature_investigator": [
                {"answers": [answer("needs_follow_up", follow_up=[
                    {"tool": "literature_read", "params_json": json.dumps(read), "purpose": "read the study"}])]},
                {"answers": [extract]},
                {"answers": [{**answer("answered"), "answer_summary":
                    "Source-local repair confirms that the mislabelled records cannot be linked to the case; "
                    "the correctly scoped experiments were already retained."}]}],
            "critic": [
                {"challenges": [], "passage_checks": [], "activation_flags": [], "reportable_ids": ["H1"],
                 "consequential": False},
                {"comparisons": [], "outcome": {"category": "no_supported_explanation", "leading_ids": [],
                                                "summary": "binding is linked, not assessed", "weakest_links": [],
                                                "next_experiments": []}}]}})


def test_about_variants_from_the_strict_experiment_through_literature_to_the_report(v9_cfg, tmp_path):
    fixture = literature_fixture()
    result, scripted, _ = run_fixture(v9_cfg, fixture, tmp_path)
    g = result.graph
    refusals = [e.concise_reason for e in events(result, "refuse_update") if e.role == "literature_investigator"]

    # literature keeps a variant only where the paper names it for the experiment, and stores it as the graph reads it
    extracted = {(e.experiment.passage, tuple(e.about_variants)): e for e in g.evidence.values()
                 if e.origin == "literature"}
    assert set(extracted) == {(CASE_EMSA, (CASE_RSID,)), (LD_EMSA, (LD_PARTNER_RSID,)), (KNOCKDOWN, ())}, refusals
    case_emsa = extracted[(CASE_EMSA, (CASE_RSID,))]
    ld_emsa = extracted[(LD_EMSA, (LD_PARTNER_RSID,))]
    knockdown = extracted[(KNOCKDOWN, ())]
    assert case_emsa.experiment.about_variants == [CASE_RSID] and case_emsa.allele == "G"
    assert case_emsa.evidence_class == "binding_assay" and knockdown.evidence_class == "perturbation"
    # the mislabelled record (the nearby variant's EMSA filed under V6) and the comparison naming no variant never
    # became evidence: literature refuses both before the graph sees them
    mislabelled = next(r for r in refusals if r.startswith("experiment 2 "))
    assert "names no variant the paper names for this experiment" in mislabelled
    assert f"{CASE_RSID} not kept: the passage names {LD_PARTNER_RSID}" in mislabelled
    assert "names no variant the paper names" in next(r for r in refusals if r.startswith("experiment 3 "))

    # the graph: only the EMSA of V6 bears on V6's alleles
    assert g.claim_frame("C1") == g.claim_frame("C2") == "case"
    assert [(x.evidence_id, x.stance, x.strength) for x in g.claims["C1"].evidence_links] == [
        (case_emsa.evidence_id, "supports", "direct")]
    assert g.claims["C2"].evidence_links == []
    assert any(f"is about {LD_PARTNER_RSID}, not the case variant" in r for r in refusals)
    assert any("a TF perturbation does not test what the variant's alleles do" in r for r in refusals)
    assert g.link_strength("C2", knockdown.evidence_id) == "context"

    # later packets name the variant each item is about
    plan = next(p for p in scripted.packets() if p.startswith("Role: coordinator; stage: plan"))
    assert f"variants {CASE_RSID}" in plan and f"variants {LD_PARTNER_RSID}" in plan

    # the bundle and the report's inspector: each name read by the graph's own variant rule
    run = tmp_path / "run"
    manifest = build_manifest(request={"fixture": "test"}, case=fixture.case, mode="fixture", config=v9_cfg,
                              manifest_parts=result.manifest_parts, graph=g, profile=None)
    write_bundle(g, result.metrics, manifest, run)
    data = report_data(load_bundle(run))
    shown = data["evidence"]
    assert shown[case_emsa.evidence_id]["variants"] == [{"text": CASE_RSID, "frame": "case"}]
    assert shown[ld_emsa.evidence_id]["variants"] == [{"text": LD_PARTNER_RSID, "frame": "other"}]
    assert shown[knockdown.evidence_id]["variants"] == []
    assert shown[case_emsa.evidence_id]["about"]["variants"] == [CASE_RSID]


# --- a reinstatement, from the graph to the report and a replay -----------------------------------------------------

def misread_fixture(tmp_path: Path) -> Path:
    """The synthetic fixture as a file, with an audit that finds the passage behind H1's only contradiction (E2 on C2)
    misread: C2 falls back to unresolved and code reinstates H1 as deferred, once."""
    data = load_fixture("synthetic_repair").model_dump(mode="json")
    data["roles"]["critic"][0]["passage_checks"] = [{"evidence_id": "E2", "verdict": "misread",
                                                     "note": "the record describes another intervention"}]
    path = tmp_path / "fixtures" / "synthetic_misread.json"
    path.parent.mkdir()
    path.write_text(json.dumps(data, indent=1))
    return path


def test_a_reinstatement_reaches_the_bundle_the_report_and_an_identical_replay(tmp_path, capsys):
    run, again = tmp_path / "run", tmp_path / "replay"
    assert cli.main(["v9", "fixture", str(misread_fixture(tmp_path)), "--out", str(run)]) == 0
    b = load_bundle(run)
    g = b.graph
    h1 = g.hypotheses["H1"]
    assert (h1.disposition, g.claims["C2"].assessment) == ("deferred", "unresolved")
    back = [e for e in g.events if e.action == "reinstate"]
    assert len(back) == 1 and back[0].role == "code" and back[0].details["claims"] == ["C2"]
    entry = next(x for x in h1.history if x["kind"] == "reinstatement")
    assert entry["event_id"] == back[0].event_id and entry["rejected_by"] == back[0].details["rejected_by"]

    # metrics.json: the engine's own record kept whole beside the bundle's counts
    assert b.metrics["engine"]["reinstated"] == compare.reinstated(g) == ["H1"]
    assert b.metrics["engine"]["stale_rejections"] == [] and b.metrics["graph"]["hypotheses_by_disposition"][
        "deferred"] >= 1

    # the report: the version stepper follows the reinstatement, the timeline files it under decisions, the summary and
    # report.md say it, and the evaluator would read the same history entry
    data = report_data(b)
    view = next(h for h in data["hypotheses"] if h["id"] == "H1")
    assert [s["disposition"] for s in view["states"]][-2:] == ["rejected", "deferred"]
    assert [x["event"] for x in view["reinstated"]] == [back[0].event_id] and view["stale_rejection"] is None
    assert next(e for e in data["events"] if e["action"] == "reinstate")["group"] == "decisions"
    assert "Reinstated" in (run / "report.html").read_text() and "reinstated" in (run / "report.md").read_text()
    assert [e["event_id"] for e in evaluation._reinstatements(h1)] == [back[0].event_id]

    # replayed from its bundle and the fixture's scripts: the same graph, reinstatement included
    capsys.readouterr()
    assert cli.main(["v9", "replay", str(run), "--out", str(again)]) == 0
    assert "identical" in capsys.readouterr().out
    replayed = load_bundle(again)
    assert replayed.manifest["replay_of"]["status"] == "identical" and replayed.metrics["engine"]["reinstated"] == ["H1"]


# --- one sketched-groups rule: the engine, the bundle and the evaluator ---------------------------------------------

def retention_fixture() -> Fixture:
    """An inventory whose group G010 is discordant (the gate-passing models of TFA favour T, those of TFB favour C: one
    item per allele, as adapters writes it) and a plan that revises H1 with TFD (group G005) as a member alternative."""
    from .test_engine_roles import ROWS, inventory_fixture

    data = inventory_fixture().model_dump(mode="json")
    response = data["tools"]["qbic_inventory"]["responses"][0]
    g010 = response["evidence"][0]
    tfb = {**copy.deepcopy(g010), "allele": "C", "about_tfs": ["TFB"],
           "observed_result": "Group G010's TFB models predict more binding of C."}
    g010.update(about_tfs=["TFA"], data={**g010["data"], "discordant": True})
    tfb["data"] = {**tfb["data"], "discordant": True}
    response["evidence"] = [g010, tfb, *response["evidence"][1:]]
    assert ROWS[0]["group_id"] == "G010" and ROWS[0]["binds_more"] == "alt"
    data["roles"]["coordinator"][1]["hypothesis_updates"] = [{
        "hypothesis_id": "H1", "action": "revise", "reason": "TFD's group predicts the same allele", "claim_id": None,
        "new_claim": None, "new_claim_id": None, "required": False, "revisit_trigger": None,
        "revision": {"title": None, "summary": None, "endpoint": None, "assumptions": None,
                     "member_alternatives": ["TFD"], "missing_links": None, "remove_claim_ids": []}}]
    return Fixture.model_validate(data)


def test_one_retention_rule_for_the_engine_the_bundle_and_the_evaluator(v9_cfg, tmp_path):
    """The real adapters.inventory_rows joins G010's row to the item for its binds_more allele; the engine's packets
    show both items; candidate retention is the same everywhere: the engine's metrics, the bundle's metrics.json
    (recomputed from graph.json) and the evaluator's reading of the saved bundle, by graph.sketched_groups."""
    from variant2mechanism.v9 import adapters
    from variant2mechanism.v9.graph import GroupRegistry

    fixture = retention_fixture()
    groups = GroupRegistry({"G010": ["TFA", "TFB"], "G005": ["TFD"], "G003": ["TFC"], "G007": ["TFE"]})
    result, scripted, _ = run_fixture(v9_cfg, fixture, tmp_path, groups=groups)
    g = result.graph
    rows = adapters.inventory_rows(g)
    items = bundle.inventory_items(g)["G010"]
    assert len(items) == 2 and rows[0]["evidence_id"] == next(e for e in items if g.evidence[e].allele == "T")
    assert rows == bundle.inventory_table(g)
    propose = scripted.packets()[0]
    assert "the gate-passing models disagree about the allele: E1 favours T (alt), E2 favours C (ref)" in propose

    expected = {"groups": 4, "gate_passing": 3, "below_gate": 1, "sketched": ["G010", "G005"],
                "inventory_only": ["G003"]}
    assert result.metrics["inventory"] == expected
    assert investigate.sketched_groups is bundle.sketched_groups is evaluation.sketched_groups is graph.sketched_groups
    run = tmp_path / "run"
    manifest = build_manifest(request={"fixture": "test"}, case=fixture.case, mode="fixture", config=v9_cfg,
                              manifest_parts=result.manifest_parts, graph=g, profile=None)
    write_bundle(g, result.metrics, manifest, run)
    saved = load_bundle(run)
    assert saved.metrics["inventory"] == saved.metrics["engine"]["inventory"] == expected
    reading = evaluation._inventory_summary(evaluation._Run(saved.graph, None), saved.metrics)
    assert reading["inventory_only_groups"] == ["G003"]
    assert reading["agrees_with_metrics"] == {"inventory": True, "engine.inventory": True}
    shown = next(r for r in report_data(saved)["inventory"]["rows"] if r["group"] == "G010")
    assert shown["discordant"] is True and [i["id"] for i in shown["items"]] == items


def test_a_stale_rejection_the_graph_keeps_reads_the_same_in_the_engine_and_the_report(v9_cfg, tmp_path, monkeypatch):
    """When graph.reinstate keeps the rejection (here it returns False, as for a second rejection), the engine
    discloses it once (an audit event with details.why) and the report shows the same hypothesis as a rejection that
    no longer stands, with the engine's reason: one predicate (compare.stale_rejections) on both sides."""
    monkeypatch.setattr(graph.ClaimGraph, "reinstate", lambda self, hid, reason, role="code": False)
    fixture = load_fixture(misread_fixture(tmp_path))
    result, _, _ = run_fixture(v9_cfg, fixture, tmp_path)
    g = result.graph
    noted = [e for e in events(result, "audit") if e.details.get("stale_rejection")]
    assert compare.stale_rejections(g) == result.metrics["stale_rejections"] == ["H1"] and len(noted) == 1
    run = tmp_path / "run"
    manifest = build_manifest(request={"fixture": "test"}, case=fixture.case, mode="fixture", config=v9_cfg,
                              manifest_parts=result.manifest_parts, graph=g, profile=None)
    write_bundle(g, result.metrics, manifest, run)
    views = {h["id"]: h for h in report_data(load_bundle(run))["hypotheses"]}
    assert [hid for hid, h in views.items() if h["stale_rejection"]] == compare.stale_rejections(g)
    stale = views["H1"]["stale_rejection"]
    assert stale["noted_by"] == [noted[0].event_id] and stale["why_still_rejected"] == [noted[0].details["why"]]
    assert views["H1"]["reinstated"] == [] and result.metrics["reinstated"] == []
