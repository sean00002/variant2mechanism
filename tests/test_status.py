"""The shared status of tool answers (found, tested_negative, not_tested, failed) and how the ledger and loop read it."""

import sqlite3

import pytest

from variant2mechanism.agent.ledger import Ledger
from variant2mechanism.agent.stages.investigate import outcome, qbic_status
from variant2mechanism.context.base import ToolResult


def tr(status="", ok=True):
    return ToolResult("eqtl_lookup", {}, "summary", {}, "source", "url", "genetic", ok=ok, status=status)


def test_status_defaults_and_checks():
    assert tr().status == "found" and tr(ok=False).status == "failed"
    assert tr(status="not_tested", ok=False).status == "failed"          # a failed call never claims more
    with pytest.raises(ValueError):
        tr(status="absent")


def test_the_loop_counts_tested_answers_as_news():
    assert [outcome(tr(s)) for s in ("found", "tested_negative", "not_tested")] == ["new", "new", "not tested"]
    assert outcome(tr(ok=False)) == "failed"


def test_qbic_status():
    assert qbic_status({"coverage": "own_model", "models": [{"z": 5.1, "passed_gate": True},
                                                            {"z": 0.3, "passed_gate": False}]}) == "found"
    assert qbic_status({"coverage": "own_model", "models": [{"z": 0.3, "passed_gate": False}]}) == "tested_negative"
    assert qbic_status({"coverage": "not_in_coverage"}) == "not_tested"
    assert qbic_status({"coverage": "mapped", "models": [{"status": "not_scored"}]}) == "not_tested"
    assert qbic_status({"tf": "X", "status": "ambiguous", "candidates": []}) == "not_tested"    # name not resolved
    assert qbic_status({"error": "boom"}) == "failed"


def test_ledger_keeps_the_status_and_shows_it(tmp_path):
    led = Ledger(tmp_path)
    ev = led.add_evidence("investigate", tr("not_tested"))
    assert led.get(ev.id).status == "not_tested"
    assert led.get(ev.id).prompt_line() == f"{ev.id} [genetic, not tested] source:\nsummary"
    led.close()


def test_ledger_from_before_statuses_still_opens(tmp_path):
    con = sqlite3.connect(tmp_path / "ledger.sqlite")
    con.execute("CREATE TABLE evidence(id TEXT PRIMARY KEY, seq INTEGER, stage TEXT, tool TEXT, args TEXT, "
                "source TEXT, url TEXT, retrieved_utc TEXT, kind TEXT, summary TEXT, full_path TEXT, quote TEXT, "
                "pmid TEXT, parent TEXT, ok INTEGER)")
    con.execute("INSERT INTO evidence VALUES ('E01', 1, 'gather', 't', '{}', 's', 'u', NULL, 'genetic', 'x', NULL, "
                "NULL, NULL, NULL, 1)")
    con.commit()
    con.close()
    led = Ledger(tmp_path)
    assert led.get("E01").status == "found"
    assert led.add_evidence("investigate", tr("tested_negative")).id == "E02"
    assert led.get("E02").status == "tested_negative"
    led.close()
