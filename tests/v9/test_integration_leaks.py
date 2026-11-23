"""Gold isolation end to end (SPEC 10, 13.12): nothing derived from a gold label reaches what an agent sees.

The evaluator's tests show that a clean request, and the case lines of a packet, carry no label string. These follow
the same strings through the engine's own path to the model, for all 15 gold rows:

- (A) the Case that intake builds from each row's clean request, in both arms, holds none of `label_strings(row)`;
- (B) the first request the engine sends for that Case with no tool data (the system prompt and the propose packet:
  case, tool specs, limits, budgets and the coordinator's instructions) holds none either, apart from method
  vocabulary that reaches the label strings only through a row's notes or its CIS-BP mapping wording;
- (C) with the offline facts of rs12740374 (code's fact collection in cache-only mode), the propose request holds no
  gold-only string: the row's PMIDs, notes, mechanism text, expression context, bracketed disease text, or any label
  cell of more than one word as written. TF and gene symbols, traits and the rsID are what the tools report about
  the variant, so they may appear;
- (D) no registered tool spec (computational or literature) holds a gold label string, in any field or in the form the
  packets show.

The model is never called: a transport records the request and refuses it, so the run stops with cache_miss. The gold
CSV is read, never edited, and only to show that nothing derived from it gets through.
"""

import csv
import json
from pathlib import Path
from typing import Any

import pytest

import variant2mechanism.v9.adapters  # noqa: F401  (registers the computational tools)
import variant2mechanism.v9.literature  # noqa: F401  (registers the literature tools)
from variant2mechanism.config import REPO
from variant2mechanism.evaluation.gold import NEVER_IN_PROMPT
from variant2mechanism.v9 import commands, roles
from variant2mechanism.v9.bundle import new_run_dir
from variant2mechanism.v9.evaluation import (
    ARMS,
    clean_request,
    find_label_strings,
    label_strings,
    label_strings_by_kind,
)
from variant2mechanism.v9.http9 import Http9
from variant2mechanism.v9.intake import build_case
from variant2mechanism.v9.replay import ReplayMiss
from variant2mechanism.v9.schemas import Case
from variant2mechanism.v9.tools import REGISTRY

GOLD = REPO / "data" / "gold_set.csv"
with open(GOLD, newline="") as _f:
    ROWS = list(csv.DictReader(_f))
BY_ID = {r["case_id"]: r for r in ROWS}
TOOLS = {"variant_annotation", "ccre_overlap", "qbic_inventory", "qbic_tf_detail", "chip_occupancy", "gtex_eqtl",
         "tf_expression", "gwas_associations", "credible_sets_l2g", "depmap_context", "civic_lookup", "screen_online",
         "literature_search", "literature_read", "evidence_inspect"}
# Method and resource vocabulary that prompts and tool specs cannot do without. It reaches the label strings only as
# identifier-like tokens of a row's free-text notes, or as the CIS-BP mapping wording of its model and score columns
# (which SPEC 13.5 puts in every prompt), never as a case's TF, gene, group, context, disease, variant or source.
METHOD_TERMS = {"notes_tokens": {"chip", "dbsnp", "encode", "eqtl", "eqtls", "gtex", "hgnc", "l2g", "pip", "snp"},
                "tf": {"cis-bp", "cis-bp-mapped"}, "other": {"mapped"}}
ROW_IDS = [r["case_id"] for r in ROWS]


def leaks(text: str, row: dict, arm: str, cfg) -> list[tuple[str, str]]:
    """(kind, string) for every label string of this arm found in the text, method vocabulary allowed by kind."""
    allowed = label_strings(row, arm=arm, config=cfg)
    return sorted((kind, s) for kind, strings in label_strings_by_kind(row, config=cfg).items()
                  for s in find_label_strings(text, strings & allowed)
                  if s.casefold() not in METHOD_TERMS.get(kind, set()))


def first_request(cfg, run_dir: Path, case: Case, monkeypatch, *, facts=None) -> tuple[dict, Any]:
    """The first request body the engine sends for `case` in cache-only mode (the coordinator's proposal), and the
    run's graph. The transport records it and refuses it (ReplayMiss), so nothing is sent and the run stops."""
    sent: list[dict] = []

    def capture(body: dict) -> dict:
        sent.append(json.loads(json.dumps(body)))
        raise ReplayMiss("recorded by the isolation test; nothing is sent")

    monkeypatch.setattr(commands, "refusing", lambda what: capture)
    w = commands.wire(cfg, "cache_only", new_run_dir(run_dir), http=Http9.from_config(cfg, offline=True))
    if facts is not None:
        w.facts = facts
    result = w.engine().run(case)
    assert result.graph.result.stop_reason == "cache_miss" and sent, "the engine sent no request"
    assert sent[0]["response_format"]["json_schema"]["schema"]["title"] == "V9Propose"
    return sent[0], result.graph


def request_text(body: dict) -> str:
    return "\n".join(str(m.get("content") or "") for m in body["messages"])


def packet(body: dict) -> str:
    return next(m["content"] for m in body["messages"] if m["role"] == "user")


def no_facts(case, graph, runner) -> list:
    return []


# --- (A) the case ------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("arm", ARMS)
@pytest.mark.parametrize("row", ROWS, ids=ROW_IDS)
def test_a_the_case_built_from_a_clean_request_holds_no_label_string(row, arm, v9_cfg):
    request = clean_request(row, arm)
    case = build_case(request, config=v9_cfg, http=Http9.from_config(v9_cfg, offline=True), mode="cache_only")
    assert case.case_id == request.request_id and case.supplied_context == []
    assert find_label_strings(case.model_dump_json(), label_strings(row, arm=arm, config=v9_cfg)) == []


# --- (B) the propose request with no tool data ---------------------------------------------------------------------------

@pytest.mark.parametrize("row", ROWS, ids=ROW_IDS)
def test_b_the_first_request_with_no_tool_data_holds_no_label_string(row, v9_cfg, tmp_path, monkeypatch):
    for arm in ARMS:
        case = build_case(clean_request(row, arm), config=v9_cfg, http=None, mode="cache_only")
        body, graph = first_request(v9_cfg, tmp_path / arm, case, monkeypatch, facts=no_facts)
        assert graph.tool_calls == {} and graph.evidence == {}
        text = request_text(body)
        assert "Role: coordinator; stage: propose" in text and "Tools, computational route" in text
        assert ("Supplied disease: none supplied" in text) is (arm == "main")
        assert leaks(text, row, arm, v9_cfg) == [], arm
        # the check sees a label string when one is there (the row's notes and source, put into the same text)
        planted = leaks(f"{text}\n{row['notes']}\nPMID:{row['source_pmid_or_ref']}", row, arm, v9_cfg)
        assert ("notes", " ".join(row["notes"].split())) in planted, arm
        assert any(kind == "source" for kind, _ in planted), arm


def test_b_the_method_terms_allowed_are_never_a_case_label(v9_cfg):
    """The allowance above holds only for method vocabulary: none of its terms is any row's TF, gene, group, context,
    disease, variant, bracketed text or source."""
    allowed = set().union(*METHOD_TERMS.values())
    for row in ROWS:
        kinds = label_strings_by_kind(row, config=v9_cfg)
        for kind in ("identity", "gene", "group", "context", "disease", "bracketed", "source"):
            assert not {s.casefold() for s in kinds[kind]} & allowed, (row["case_id"], kind)
        assert not find_label_strings(f"{row['causal_tf']} | {row['tf_family']}", allowed), row["case_id"]


# --- (C) the propose packet with rs12740374's offline facts ---------------------------------------------------------------

def gold_only(row: dict, cfg) -> set[str]:
    """What only the gold row can say about the case: its source (PMIDs), notes, mechanism text (direction, label class,
    score level), expression context (every string the evaluator derives from that cell), bracketed disease text, and
    every label cell of more than one word as written. Bare TF and gene symbols, traits and rsIDs are left out: tools
    report them about the variant itself."""
    kinds = label_strings_by_kind(row, config=cfg)
    blank = {key: "" for key in row}
    expression = label_strings_by_kind({**blank, "expression_context": row["expression_context"]}, config=cfg)
    cells = {" ".join(row[c].split()) for c in (*NEVER_IN_PROMPT, "expression_context")}
    whole = {c for c in cells if " " in c}          # a cell as written: a bare symbol is what tools report too
    strings = kinds["source"] | kinds["notes"] | kinds["other"] | kinds["bracketed"] | expression["context"] | whole
    return {s for s in strings if len(s) >= 3}


@pytest.mark.data
@pytest.mark.parametrize("arm", ARMS)
def test_c_the_propose_packet_with_offline_facts_holds_no_gold_only_string(arm, v9_cfg, tmp_path, monkeypatch,
                                                                           http_cache_names):
    if not http_cache_names:
        pytest.skip("the HTTP cache (cache/http) is not present: no offline facts to show")
    row = BY_ID["rs12740374"]
    http = Http9.from_config(v9_cfg, offline=True)
    case = build_case(clean_request(row, arm), config=v9_cfg, http=http, mode="cache_only")
    body, graph = first_request(v9_cfg, tmp_path / "run", case, monkeypatch)
    tools = {t.tool_name: t.execution_status for t in graph.tool_calls.values()}
    if tools.get("qbic_inventory") != "success" or tools.get("variant_annotation") != "success":
        pytest.skip(f"the offline facts of rs12740374 are not cached here: {tools}")
    text = packet(body)
    # the facts are in the packet: the rsID VEP reports, the cCRE, the inventory with the C/EBP group's members
    assert "rsID rs12740374 at these coordinates and alleles" in text and "EH38E1374646" in text
    assert "G035" in text and "CEBPA (own)" in text and "QBiC-SELEX inventory" in text
    strings = gold_only(BY_ID["rs12740374"], v9_cfg)
    assert {"20686566", "PMID:20686566", "(1p13)", "ACH-000625", "Hep 3B2.1-7", row["notes"], row["direction"],
            row["qbic_model"]} <= strings
    assert not strings & {"rs12740374", "CEBPA", "CEBPB", "SORT1", "LDL cholesterol"}     # what tools report
    assert find_label_strings(request_text(body), strings) == []
    assert find_label_strings(f"{text} (1p13) ACH-000625", strings) == ["(1p13)", "1p13", "ACH-000625"]


# --- (D) tool specs ------------------------------------------------------------------------------------------------------

def spec_texts() -> dict[str, str]:
    """Everything a registered spec holds (each serialised field, and describe()), per tool, plus the tool list as
    every packet shows it (roles.tools_text)."""
    texts = {name: json.dumps(REGISTRY.spec(name).model_dump()) + json.dumps(REGISTRY.spec(name).describe())
             for name in REGISTRY.names()}
    specs = {route: REGISTRY.specs(route) for route in ("computational", "literature")}
    return {**texts, "packet tool list": roles.tools_text(specs, ("computational", "literature"))}


def test_d_no_registered_tool_spec_holds_a_gold_label_string(v9_cfg):
    texts = spec_texts()
    assert set(texts) - {"packet tool list"} == TOOLS
    assert all(name in texts["packet tool list"] for name in TOOLS)
    found = [(row["case_id"], tool, kind, s) for row in ROWS for tool, text in texts.items()
             for kind, s in leaks(text, row, "main", v9_cfg)]
    assert found == []
    # the check sees a gold label in a spec: a description naming a gold context and a gold TF's group
    planted = leaks(texts["ccre_overlap"] + " e.g. Hep3B or G035", BY_ID["rs12740374"], "main", v9_cfg)
    assert {("context", "Hep3B"), ("group", "G035")} <= set(planted)
