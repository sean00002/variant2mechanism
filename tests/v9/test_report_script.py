"""The report's script, executed: Node runs report.html's code on a minimal DOM that refuses every HTML-parsing API
(tests/v9/fixtures/report/run_report_script.js), clicks every claim, steps through every graph version, drives the
filters, checks where keyboard focus lands and what a printout holds. Skipped where Node is not installed."""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

from variant2mechanism.v9 import bundle, report
from variant2mechanism.v9.graph import ClaimGraph, HypothesisDraft
from variant2mechanism.v9.schemas import RunResult

from .test_report_render import PAYLOAD
from .test_report_support import (
    ELEMENT,
    VARIANT,
    claim,
    dev_case,
    discordant_inventory,
    inventory_call,
    inventory_row,
    reinstatement_graph,
    rich_graph,
    synthetic_run,
    tf,
    tool_evidence,
    write_run,
)

DRIVER = Path(__file__).parent / "fixtures" / "report" / "run_report_script.js"
NODE = shutil.which("node")
pytestmark = pytest.mark.skipif(NODE is None, reason="Node.js is not installed")


def run_script(run_dir: Path) -> dict:
    html, _ = report.write_reports(run_dir)
    done = subprocess.run([NODE, str(DRIVER), str(html)], capture_output=True, text=True, timeout=120, check=True)
    out = json.loads(done.stdout)
    assert out["errors"] == [], out["errors"]
    assert out["html_class"] == "js" and out["created"].get("img") is None and out["created"]["script"] == 1
    return out


def test_the_script_draws_a_full_run_and_steps_through_its_versions(tmp_path):
    g = rich_graph()
    out = run_script(write_run(g, tmp_path / "run"))
    start = out["start"]
    assert start["chips"] == start["claim_buttons"] == len(g.claims)
    assert start["hypothesis_rows"] == len(g.hypotheses) and start["events"] == len(g.events)
    assert start["inventory_tables"] == 1 and start["inventory_rows"] == 3 and start["inventory_shown"] == 2
    assert out["inventory_all_shown"] == 3
    assert start["archive_items"] == 3                 # the rejected and deferred hypotheses, one superseded claim
    assert start["selected"].startswith("C3 ")                     # the leading hypothesis's weakest link
    versions = out["versions"]
    assert versions["0"] == 0 and versions[str(g.version)] == len(g.claims)
    assert [versions[str(v)] for v in range(g.version + 1)] == sorted(versions.values())   # claims only accrue
    assert set(out["inspected"]) == set(g.claims)
    assert "premise failed" in out["inspected"]["C6"]["claim"]
    assert "Contradicts (1)" in out["inspected"]["C5"]["evidence"]


def test_keyboard_focus_follows_the_activated_control(tmp_path):
    out = run_script(write_run(rich_graph(), tmp_path / "run"))
    focus = out["focus"]
    # a redrawn control hands focus to its redrawn twin, never to the top of the page
    for name, within, tag in (("claim_button", "claim-buttons", "button"), ("chip", "mechanism-graph", "g"),
                              ("highlight", "hypothesis-table", "button")):
        assert focus[name]["now"] == {"id": focus[name]["clicked"], "tag": tag, "connected": True,
                                      "within": within}, name
    # a claim link elsewhere jumps to the graph, and focus goes with it to that claim's button
    assert focus["claim_link"]["now"] == {"id": focus["claim_link"]["clicked"], "tag": "button", "connected": True,
                                          "within": "claim-buttons"}
    assert focus["show_version"]["id"] == "version"            # "Show version" lands on the version slider


def test_a_printout_holds_every_claims_evidence(tmp_path):
    g = rich_graph()
    out = run_script(write_run(g, tmp_path / "run"))
    printed = out["printed"]
    assert printed["claims"] == len(g.claims)                    # every claim, not only the selected one
    assert printed["evidence_items"] == sum(len(c.evidence_links) for c in g.claims.values())
    for c in g.claims.values():
        assert c.assertion_text in printed["text"]
    assert "CRISPRi of the enhancer lowers GENE2 in HepG2." in printed["text"]     # the evidence that rejected H1
    assert printed["details_open"] is True and printed["emptied_after"] is True


def test_the_script_draws_a_synthetic_run(tmp_path):
    g, run = synthetic_run(tmp_path)
    out = run_script(run)
    assert out["start"]["chips"] == len(g.claims) and out["start"]["inventory_rows"] == 0
    assert "No QBiC-SELEX inventory in this run." in out["text"]
    # the archive keeps C3, whose premise C2 was contradicted, apart from the retained claims
    assert "Retained claims: C1 (supported in scope)Not retained, a premise failed: C3 (unresolved; rests on C2" \
           in out["text"]


def test_the_script_draws_an_evidence_only_bundle(tmp_path):
    g = ClaimGraph(dev_case())
    tool_evidence(g, "annotation", "The variant lies in cCRE EH38E0000001.", about_elements=["EH38E0000001"])
    inventory_call(g, [inventory_row(i, i % 3 != 0) for i in range(1, 31)])
    out = run_script(write_run(g, tmp_path / "run"))
    assert out["start"]["chips"] == 0 and out["start"]["hypothesis_rows"] == 0
    assert out["start"]["other_evidence_rows"] == 1 and out["start"]["inventory_rows"] == 30
    assert "No claims: this bundle holds evidence only." in out["text"]
    assert "No hypotheses in this run. Facts collected by code (2 tool calls); no model was called" in out["text"]


def test_the_script_says_why_a_stopped_run_has_no_hypotheses(tmp_path):
    g = ClaimGraph(dev_case())
    tool_evidence(g, "annotation", "The variant lies in cCRE EH38E0000001.", about_elements=["EH38E0000001"])
    g.set_model_usage(4, 0.0)
    g.set_result(RunResult(outcome="no_supported_explanation", stop_reason="regeneration_limit",
                           summary="Every proposal failed validation."), "code")
    out = run_script(write_run(g, tmp_path / "run", metrics={"model_calls": 4}))
    page_text = out["text"].split('{"format":')[0]          # the page, without the embedded data that follows it
    assert "evidence bundle" not in page_text.lower()
    assert ("No hypotheses in this run. The run stopped before any hypothesis was proposed (regeneration limit "
            "reached; 4 model calls).") in out["text"]


def test_the_script_shows_reinstatements_stale_rejections_and_refused_questions(tmp_path):
    g = reinstatement_graph()
    out = run_script(write_run(g, tmp_path / "run"))
    page = out["text"].split('{"format":')[0]              # the page, without the embedded data that follows it
    data = report.report_data(bundle.load_bundle(tmp_path / "run"))
    h1, h2 = data["hypotheses"]
    assert out["start"]["archive_items"] == 2              # H1 deferred (reinstated), H2 rejected
    assert "reinstated " + h1["reinstated_notes"][0] in page                    # a tag, then the sentence
    assert "rejection no longer stands " + h2["stale_note"] in page
    assert "Evidence the withdrawn rejection cited: E1" in page and "Decisive evidence: E2" in page
    assert ("Questions closed without being asked" in page and "not asked again: it repeats Q1 (same route, tool "
            "requests and target claims, none changed since); see Q1's answer" in page)


def test_the_script_shows_the_variants_evidence_is_about_and_both_alleles_of_a_split_group(tmp_path):
    g = ClaimGraph(dev_case())
    g_item, t_item, _ = discordant_inventory(g).evidence_ids
    eid = tool_evidence(g, "annotation", "The enhancer holding rs1427407 and rs629301.", tool="ccre_overlap",
                        about_elements=["EH38E0000001"], about_variants=["rs1427407", "rs629301", "the G allele"])
    c = claim(g, [VARIANT], "overlaps", [ELEMENT], assertion_text="rs1427407 lies in the enhancer")
    g.link(c, eid, "supports", "computational_investigator", "names the case variant and the element")
    binds_t = claim(g, [VARIANT], "alters_binding", [tf("SPI1")], "increases", effect_allele="T")
    g.link(binds_t, t_item, "supports", "computational_investigator", "SPI1's own model favours T")
    out = run_script(write_run(g, tmp_path / "run"))
    assert ("variants: rs1427407 (the case variant), rs629301 (another variant), the G allele; elements: "
            "EH38E0000001") in out["inspected"][c]["evidence"]
    assert "variants: rs1427407 (the case variant)" in out["inspected"][binds_t]["evidence"]
    page = out["text"].split('{"format":')[0]
    assert (f"{g_item}: G binds more (models of SPI1, SPIB); {t_item}: T binds more (models of ELF5, SPI1) models "
            f"disagree · linked: {binds_t}") in page
    assert out["start"]["inventory_rows"] == 3 and out["start"]["other_evidence_rows"] == 0


def test_the_script_shows_hostile_text_as_text(tmp_path):
    g = ClaimGraph(dev_case())
    eid = tool_evidence(g, "annotation", PAYLOAD, about_elements=["EH38E0000001"])
    c = claim(g, [VARIANT], "overlaps", [ELEMENT], assertion_text=PAYLOAD)
    g.link(c, eid, "supports", "computational_investigator", PAYLOAD)
    g.add_hypothesis(HypothesisDraft(title=PAYLOAD, required_claim_ids=[c], mechanism_class="regulatory"),
                     "coordinator")
    out = run_script(write_run(g, tmp_path / "run"))
    assert PAYLOAD in out["text"] and PAYLOAD in out["inspected"][c]["evidence"]
