"""report.html and report.md from a bundle only (SPEC 9): escaping, fidelity to the graph (ids, statuses, past states
at every version), the synthetic banner, evidence-only bundles versus runs that stopped early, the case as supplied,
inferred and found by code, labels for every schema value, one inventory table, deterministic layout, offline
rendering, changed bundle files and never overwriting a report."""

import json
import re
import shutil
import socket
from html.parser import HTMLParser
from typing import get_args

import pytest

from variant2mechanism.v9 import bundle, report
from variant2mechanism.v9.graph import ClaimGraph, HypothesisDraft
from variant2mechanism.v9.schemas import (
    Case,
    ComparisonOutcome,
    Direction,
    DisplayStatus,
    Disposition,
    Evidence,
    InferredCandidate,
    Outcome,
    Relation,
    RunMode,
    RunResult,
    StopReason,
    ToolCall,
    Variant,
)

from .conftest import NetworkBlocked
from .test_report_support import (
    ELEMENT,
    VARIANT,
    claim,
    dev_case,
    discordant_inventory,
    gene,
    inventory_call,
    inventory_row,
    reinstatement_graph,
    rich_graph,
    synthetic_graph,
    synthetic_run,
    tf,
    tool_evidence,
    write_run,
)

PAYLOAD = '</script><script>alert("x")</script><img src=x onerror=alert(1)> & "quoted" | piped'


class Page(HTMLParser):
    """The tags of a rendered page, the text of its JSON data block and its no-script tables."""

    def __init__(self, text: str):
        super().__init__()
        self.tags: list[tuple[str, dict]] = []
        self.data_text = ""
        self._in_data = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        self.tags.append((tag, a))
        self._in_data = tag == "script" and a.get("id") == "v2m-data"

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_data = False

    def handle_data(self, data):
        if self._in_data:
            self.data_text += data


def static_tables(html: str) -> list[str]:
    """The no-script fallback's tables (noscript content is not parsed as markup when scripting is on)."""
    inner = re.search(r"<noscript>(.*?)</noscript>", html, re.S).group(1)
    return re.findall(r"<table.*?</table>", inner, re.S)


def data_of(html: str) -> dict:
    return json.loads(Page(html).data_text)


def render(g: ClaimGraph, tmp_path, name: str = "run", mode: str = "cache_only", metrics: dict | None = None,
           parts: dict | None = None, extra: dict | None = None) -> tuple[str, str, dict]:
    run = write_run(g, tmp_path / name, mode=mode, metrics=metrics, parts=parts, extra=extra)
    b = bundle.load_bundle(run)
    html = report.render_html(b)
    return html, report.render_markdown(b), data_of(html)


def summary_rows(html: str) -> dict[str, str]:
    """The run summary's rows (server-rendered, so they read the same without script), as {title: cell HTML}."""
    summary = re.search(r'<dl class="facts">(.*?)</dl>', html, re.S).group(1)
    return dict(re.findall(r"<dt>(.*?)</dt><dd>(.*?)</dd>", summary))


def test_text_is_escaped_in_every_format(tmp_path):
    g = ClaimGraph(dev_case())
    eid = tool_evidence(g, "annotation", PAYLOAD, tool="ccre_overlap", about_elements=["EH38E0000001"],
                        source_ids=["<b>PMID:1</b>", "javascript:alert(1)"])
    c = claim(g, [VARIANT], "overlaps", [ELEMENT], assertion_text=PAYLOAD)
    g.link(c, eid, "supports", "computational_investigator", PAYLOAD)
    g.add_hypothesis(HypothesisDraft(title=PAYLOAD, required_claim_ids=[c], mechanism_class="regulatory"),
                     "coordinator")
    html, md, data = render(g, tmp_path)
    page = Page(html)
    assert [t for t, _ in page.tags if t == "script"] == ["script", "script"]        # the template's two only
    assert not [t for t, _ in page.tags if t in ("img", "iframe", "object", "embed")]
    assert not any(k.startswith("on") for _, attrs in page.tags for k in attrs)
    assert "<" not in page.data_text and ">" not in page.data_text
    assert data["evidence"][eid]["observed"] == PAYLOAD and data["claims"][c]["assertion"] == PAYLOAD
    assert data["hypotheses"][0]["title"] == PAYLOAD
    assert [s["url"] for s in data["evidence"][eid]["sources"]] == [None, None]     # never a link from data
    assert "&lt;img src=x onerror=alert(1)&gt;" in html                               # the no-script tables escape it
    assert "<img" not in md and "<script" not in md and "\\| piped" in md
    template = report.TEMPLATE.read_text()
    for unsafe in ("innerHTML", "outerHTML", "insertAdjacentHTML", "document.write", "eval(", "new Function"):
        assert unsafe not in template


def test_embedded_data_names_every_claim_and_evidence_with_the_graphs_statuses(tmp_path):
    g = rich_graph()
    _, _, data = render(g, tmp_path)
    assert set(data["claims"]) == set(g.claims) and set(data["evidence"]) == set(g.evidence)
    assert [e["id"] for e in data["events"]] == [e.event_id for e in g.events]
    assert {h["id"] for h in data["hypotheses"]} == set(g.hypotheses)
    for cid, c in data["claims"].items():
        shown = g.display(cid)
        assert (c["status"], c["basis"], c["flag"]) == (shown.status, shown.basis, shown.dependency_flag)
        last = c["states"][-1]                    # the rebuilt history ends where the graph is now
        assert (last["status"], last["basis"], last["assessment"], last["flag"], last["superseded_by"]) == (
            shown.status, shown.basis, g.claims[cid].assessment, g.claims[cid].dependency_flag,
            g.claims[cid].superseded_by)
        current = {x["evidence"]: x["stance"] for x in c["links"]}
        assert current == {x.evidence_id: x.stance for x in g.claims[cid].evidence_links}
    statuses = {c["status"] for c in data["claims"].values()}
    assert statuses == {"supported", "predicted", "associated", "contested", "contradicted", "unresolved"}
    assert data["final_version"] == g.version


def test_past_states_follow_the_record(tmp_path):
    g, run = synthetic_run(tmp_path)
    data = report.report_data(bundle.load_bundle(run))
    version = {e.event_id: e.graph_version_after for e in g.events}
    assess = next(e for e in g.events if e.action == "assess" and e.target_ids == ["C2"])
    states = data["claims"]["C2"]["states"]
    assert states[0]["status"] == "unresolved" and states[0]["assessment"] == "unassessed"
    assert [s for s in states if s["status"] == "contradicted"][0]["v"] == version[assess.event_id]
    propagate = next(e for e in g.events if e.action == "propagate")
    flagged = [s for s in data["claims"]["C3"]["states"] if s["flag"] != "none"][0]
    assert flagged["v"] == version[propagate.event_id] and flagged["status"] == "unresolved"   # never contradicted
    reject = next(e for e in g.events if e.action == "reject")
    h1 = next(h for h in data["hypotheses"] if h["id"] == "H1")
    assert h1["states"] == [{"v": h1["states"][0]["v"], "disposition": "active"},
                            {"v": version[reject.event_id], "disposition": "rejected"}]
    # C3 rests on the contradicted C2: its premise failed, so it is listed apart and never as a retained subclaim
    assert h1["reject_evidence"] == reject.evidence_ids and h1["retained"] == ["C1"]
    assert h1["premise_failed"] == ["C3"]
    refused_link = [x for x in data["claims"]["C2"]["links"] if x["stance"] == "supports"]
    assert refused_link == []                     # a refused update never became a link


def test_synthetic_runs_carry_a_prominent_banner(tmp_path):
    _, run = synthetic_run(tmp_path)
    b = bundle.load_bundle(run)
    html, md = report.render_html(b), report.render_markdown(b)
    header = html.split("<noscript>")[0]          # in the page itself, before any script runs
    assert 'class="banner synthetic"' in header and "Synthetic fixture, not biological evidence." in header
    assert "Synthetic fixture, not biological evidence." in md.split("\n## ")[0]
    assert data_of(html)["meta"]["synthetic"] is True
    biological, _, data = render(rich_graph(), tmp_path, "biological")
    assert "banner synthetic" not in biological and data["meta"]["synthetic"] is False


def test_an_evidence_only_bundle_renders(tmp_path):
    g = ClaimGraph(dev_case())
    tool_evidence(g, "annotation", "The variant lies in cCRE EH38E0000001.", tool="ccre_overlap",
                  about_elements=["EH38E0000001"], source_ids=["ENCSR000AAA"])
    inventory_call(g, [inventory_row(1, True), inventory_row(2, False)])
    html, md, data = render(g, tmp_path)
    assert data["meta"]["evidence_only"] is True and data["result"] is None and data["hypotheses"] == []
    assert data["layout"]["nodes"] == [] and data["claims"] == {}
    assert "Evidence bundle." in html and "Evidence bundle." in md
    assert "E1" in md and "https://www.encodeproject.org/ENCSR000AAA/" in md
    assert data["inventory"]["groups"] == 2 and data["inventory"]["gate_passing"] == 1


def test_a_folder_with_only_its_graph_still_renders(tmp_path):
    g = rich_graph()
    folder = tmp_path / "bare"
    folder.mkdir()
    (folder / "graph.json").write_text(g.to_json())
    html, md = report.write_reports(folder)
    data = data_of(html.read_text())
    assert data["meta"]["manifest_missing"] is True and data["meta"]["mode_label"] == "Mode not recorded"
    assert "No manifest." in html.read_text() and data["provenance"] == {"manifest": {}, "metrics": {}}
    assert set(data["claims"]) == set(g.claims) and "## Claims" in md.read_text()


def test_a_400_group_inventory_is_one_table_in_its_recorded_order(tmp_path):
    g = ClaimGraph(dev_case())
    rows = [inventory_row(i, i <= 400) for i in range(1, 441)]
    call = inventory_call(g, rows)
    linked = claim(g, [VARIANT], "alters_binding", [tf("TF7A")], "increases")
    g.link(linked, call.evidence_ids[6], "supports", "computational_investigator", "TF7A's group favours G")
    html, md, data = render(g, tmp_path)
    inventory = data["inventory"]
    assert [r["group"] for r in inventory["rows"]] == [r["group_id"] for r in rows]      # never re-sorted (by z)
    assert inventory["gate_passing"] == 400 and inventory["linked"] == 1
    assert inventory["rows"][6]["claims"] == [linked] and inventory["rows"][0]["members"][1]["mapping"] == "cisbp"
    assert sum(e["inventory"] for e in data["evidence"].values()) == 400
    tables = [t for t in static_tables(html) if 'class="inventory"' in t]
    assert len(tables) == 1 and tables[0].count("<tr>") == 1 + 400                      # header + gate-passing rows
    evidence_table = next(t for t in static_tables(html) if "<caption>Evidence" in t)
    assert evidence_table.count("<tr>") == 1 + 1          # unlinked inventory items are not one panel each
    assert html.count('id="inventory-body"') == 1
    assert len([line for line in md.splitlines() if re.match(r"\| G\d{3} ", line)]) == 400
    assert "(CIS-BP-mapped)" in md


def test_rendering_needs_only_the_folder_and_no_network(tmp_path):
    g, run = synthetic_run(tmp_path)
    with pytest.raises(NetworkBlocked):
        socket.create_connection(("example.org", 80), timeout=1)
    copy = tmp_path / "elsewhere" / "copy"
    shutil.copytree(run, copy)
    paths = report.write_reports(copy, tmp_path / "rendered")
    html = paths[0].read_text()
    assert data_of(html)["meta"]["render_only"] is True and "Render-only" in html
    template = report.TEMPLATE.read_text()
    assert not re.search(r"<link\b|<script\s+src|<img\b|<iframe\b|@import|url\((?!#)", template)   # url(#x) is local
    assert data_of(html)["raw_base"] == "../elsewhere/copy/"


def test_reports_are_never_overwritten(tmp_path):
    _, run = synthetic_run(tmp_path)
    html, md = report.write_reports(run)
    assert (html.name, md.name) == ("report.html", "report.md") and html.parent == run
    before = html.read_bytes()
    with pytest.raises(FileExistsError, match="never overwritten"):
        report.write_reports(run)
    assert html.read_bytes() == before
    report.write_reports(run, tmp_path / "out")
    with pytest.raises(FileExistsError):
        report.write_reports(run, tmp_path / "out")


def test_the_layout_is_deterministic_and_in_columns_by_kind():
    g = rich_graph()
    first = report.layout(g)
    assert report.layout(g) == first
    x = {n["kind"]: n["x"] for n in first["nodes"]}
    assert x["variant"] < x["tf"] < x["element"] < x["gene"] < x["process"] < x["phenotype"]
    genes = [n for n in first["nodes"] if n["kind"] == "gene"]
    assert [n["y"] for n in genes] == sorted(n["y"] for n in genes)
    assert [int(n["id"][1:]) for n in genes] == sorted(int(n["id"][1:]) for n in genes)   # rows in id order
    assert [e["claim"] for e in first["edges"]] == list(g.claims)
    chips = [e["chip"] for e in first["edges"]]
    for i, a in enumerate(chips):                 # no claim's label covers another's
        for b in chips[i + 1:]:
            assert abs(a["cx"] - b["cx"]) >= a["w"] + 4 or abs(a["cy"] - b["cy"]) >= a["h"]
    claim(g, [ELEMENT], "regulates", [gene("GENE9")], "increases")
    later = {n["id"]: (n["x"], n["y"]) for n in report.layout(g)["nodes"]}
    assert all(later[n["id"]] == (n["x"], n["y"]) for n in first["nodes"])          # a new claim moves no node


def test_markdown_is_a_compact_equivalent(tmp_path):
    g = rich_graph()
    _, md, data = render(g, tmp_path)
    assert "**Partial mechanism**" in md and "stopped because converged" in md
    for h in g.hypotheses:
        assert f"| {h} " in md
    for cid in g.claims:
        assert f"| {cid} |" in md
    c5 = next(line for line in md.splitlines() if line.startswith("| C5 |"))
    assert "contradicted (perturbation)" in c5 and "E7" in c5
    c6 = next(line for line in md.splitlines() if line.startswith("| C6 |"))
    assert "premise failed" in c6 and "contradicted" not in c6
    assert "## Next discriminating evidence (suggested, not performed)" in md
    assert "CRISPRi of the enhancer in HepG2, measuring GENE1" in md


def test_source_links_are_built_from_ids_only():
    cases = {"PMID:20686566": "https://pubmed.ncbi.nlm.nih.gov/20686566/",
             "pmcid:pmc3062476": "https://pmc.ncbi.nlm.nih.gov/articles/PMC3062476/",
             "doi:10.1038/nature09266": "https://doi.org/10.1038/nature09266",
             "https://doi.org/10.1038/nature09266": "https://doi.org/10.1038/nature09266",
             "ENCSR000AAA": "https://www.encodeproject.org/ENCSR000AAA/",
             "GTEx:rs12740374": "https://gtexportal.org/home/snp/rs12740374",
             "GTEx:ENSG00000134243": "https://gtexportal.org/home/gene/ENSG00000134243",
             "GCST90000123": "https://www.ebi.ac.uk/gwas/studies/GCST90000123"}
    for source, url in cases.items():
        assert report.source_link(source) == {"text": source, "url": url}
    for unsafe in ("javascript:alert(1)", "https://example.org/x", "PMID:1 onerror=x", "SYN-ANNOTATION-1"):
        assert report.source_link(unsafe)["url"] is None


def record_every_version(monkeypatch) -> dict[int, dict[int, dict]]:
    """Make every graph event record the graph as it stands right after it, keyed by graph id and then graph version:
    each claim's display status and basis, assessment, dependency flag, supersession and current links, and each
    hypothesis's disposition. A rolled-back mutation's record is overwritten by what is committed at that version, and
    one past the final version is never compared."""
    seen: dict[int, dict[int, dict]] = {}
    original = ClaimGraph._event

    def recording(self, *args, **kwargs):
        event = original(self, *args, **kwargs)
        seen.setdefault(id(self), {})[self.version] = {
            "claims": {cid: (self.display(cid).status, self.display(cid).basis, c.assessment, c.dependency_flag,
                             c.superseded_by, {x.evidence_id: x.stance for x in c.evidence_links})
                       for cid, c in self.claims.items()},
            "hypotheses": {hid: h.disposition for hid, h in self.hypotheses.items()}}
        return event

    monkeypatch.setattr(ClaimGraph, "_event", recording)
    return seen


def test_past_states_match_the_graph_at_every_version(tmp_path, monkeypatch):
    seen = record_every_version(monkeypatch)
    graphs = {"synthetic": synthetic_graph()[0], "rich": rich_graph(), "reinstated": reinstatement_graph()}
    for name, g in graphs.items():
        data = report.report_data(bundle.load_bundle(write_run(g, tmp_path / name)))
        versions = {v: snap for v, snap in seen[id(g)].items() if v <= g.version}
        assert set(versions) == set(range(1, g.version + 1))          # every version the stepper can show
        for v, snap in versions.items():
            for cid, (status, basis, assessment, flag, superseded_by, links) in snap["claims"].items():
                c = data["claims"][cid]
                then = [s for s in c["states"] if s["v"] <= v][-1]
                assert (then["status"], then["basis"], then["assessment"], then["flag"], then["superseded_by"]) == (
                    status, basis, assessment, flag, superseded_by), (name, v, cid)
                current = {}
                for x in c["links"]:
                    if x["v"] <= v:
                        current[x["evidence"]] = x["stance"]
                assert current == links, (name, v, cid)
            for cid in set(data["claims"]) - set(snap["claims"]):         # not yet proposed at this version
                assert not [s for s in data["claims"][cid]["states"] if s["v"] <= v], (name, v, cid)
            for h in data["hypotheses"]:
                if h["id"] in snap["hypotheses"]:
                    then = [s for s in h["states"] if s["v"] <= v][-1]["disposition"]
                    assert then == snap["hypotheses"][h["id"]], (name, v, h["id"])


LABELLED = [(StopReason, report.STOP_LABELS), (Outcome, report.OUTCOME_LABELS),
            (Disposition, report.DISPOSITION_LABELS), (Relation, report.RELATION_LABELS),
            (Relation, report.RELATION_SHORT), (DisplayStatus, report.STATUS_LABELS),
            (Direction, report.DIRECTION_MARKS), (RunMode, report.MODE_LABELS)]


def test_every_schema_value_has_a_label_and_an_unknown_one_still_renders(tmp_path, monkeypatch):
    for literal, table in LABELLED:
        assert set(get_args(literal)) <= set(table), set(get_args(literal)) - set(table)
    assert set(get_args(ComparisonOutcome)) - {"A_preferred", "B_preferred"} <= set(report.COMPARISON_LABELS)
    # a saved run whose values a table does not know (a newer schema) renders them as words, never a KeyError
    for table, value in ((report.STOP_LABELS, "converged"), (report.OUTCOME_LABELS, "partial_mechanism"),
                         (report.DISPOSITION_LABELS, "leading"), (report.RELATION_LABELS, "alters_binding"),
                         (report.RELATION_SHORT, "alters_binding"), (report.STATUS_LABELS, "contested"),
                         (report.COMPARISON_LABELS, "tied")):
        monkeypatch.delitem(table, value)
    html, md, data = render(rich_graph(), tmp_path)
    assert data["result"]["stop_label"] == "converged" and data["result"]["outcome_label"] == "partial mechanism"
    assert "**partial mechanism**; stopped because converged" in md
    assert {h["disposition_label"] for h in data["hypotheses"] if h["disposition"] == "leading"} == {"leading"}
    binding = next(c for c in data["claims"].values() if c["relation"] == "alters_binding")
    assert binding["relation_label"] == "alters binding" and "alters binding" in binding["chip"]
    assert {c["status_label"] for c in data["claims"].values() if c["status"] == "contested"} == {"contested"}


def test_a_run_stopped_by_an_engine_error_renders_and_exports(tmp_path):
    g, _ = synthetic_graph()
    g.set_result(RunResult(outcome="input_or_capability_limitation", stop_reason="engine_error",
                           summary="The run stopped on an internal error."), "code")
    run = write_run(g, tmp_path / "run", mode="fixture")
    html, md = report.write_reports(run)
    label = report.STOP_LABELS["engine_error"]
    assert label in html.read_text() and f"stopped because {label}" in md.read_text()
    out = bundle.export_public(run, tmp_path / "public")
    assert (out / "report.html").exists() and (out / "report.md").exists()


def test_an_engine_error_names_unusable_model_output_as_well_as_internal_failures(tmp_path):
    # engine_error ends a run that got no usable proposal or plan from the model, not only one that crashed
    label = report.STOP_LABELS["engine_error"]
    assert "unusable model output" in label and "internal failure" in label
    for detail in ("no usable proposal from the coordinator in 2 attempts", "internal error (KeyError)"):
        g = stopped_early("engine_error", tool_calls=1, model_calls=2)
        g.log("stop", "code", f"engine_error: {detail}", details={"stop_reason": "engine_error", "round": 0,
                                                                  "detail": detail})
        stop = next(e for e in g.events if e.action == "stop").event_id
        html, md, data = render(g, tmp_path, detail[:8].replace(" ", "-"), metrics={"model_calls": 2})
        assert (data["result"]["stop_event"], data["result"]["stop_detail"]) == (stop, detail)
        assert summary_rows(html)["Stopped because"] == report._h(f"{label} ({stop}: {detail})")
        assert f"stopped because {report._md(label)} ({stop}: {report._md(detail)})." in md
        assert label in data["meta"]["hypotheses_note"]


def stopped_early(stop_reason: str, *, tool_calls: int, model_calls: int) -> ClaimGraph:
    """A run that ended before the coordinator proposed anything: facts collected, a result, no hypothesis."""
    g = ClaimGraph(dev_case())
    for i in range(tool_calls):
        tool_evidence(g, "annotation", f"Fact {i} about the variant.", tool="ccre_overlap",
                      about_elements=["EH38E0000001"])
    g.set_model_usage(model_calls, 0.0)
    g.set_result(RunResult(outcome="no_supported_explanation", stop_reason=stop_reason,
                           summary="No hypothesis could be proposed."), "code")
    return g


def test_a_run_that_stopped_before_proposing_is_not_an_evidence_bundle(tmp_path):
    g = stopped_early("regeneration_limit", tool_calls=2, model_calls=4)
    html, md, data = render(g, tmp_path, "failed", metrics={"model_calls": 4, "stop_reason": "regeneration_limit"})
    meta = data["meta"]
    assert meta["evidence_only"] is False and meta["model_calls"] == 4
    assert "regeneration limit reached" in meta["hypotheses_note"] and "4 model calls" in meta["hypotheses_note"]
    for text in (html.split("<noscript>")[0], md):
        assert "Evidence bundle" not in text and "No hypotheses." in text and "4 model calls" in text
    # an invalid input stops before any fact is collected: nothing claims that code collected facts
    _, md, data = render(stopped_early("input_invalid", tool_calls=0, model_calls=0), tmp_path, "invalid")
    assert data["meta"]["evidence_only"] is False and "Facts collected" not in md
    assert "the input was invalid; no model call" in data["meta"]["hypotheses_note"]
    # what `v2m v9 evidence` writes (no engine, no result, no model call) is still an evidence bundle
    evidence = ClaimGraph(dev_case())
    tool_evidence(evidence, "annotation", "The variant lies in cCRE EH38E0000001.", tool="ccre_overlap",
                  about_elements=["EH38E0000001"])
    _, md, data = render(evidence, tmp_path, "evidence")
    assert data["meta"]["evidence_only"] is True and "1 tool call)" in data["meta"]["hypotheses_note"]
    assert "**Evidence bundle.**" in md


def test_the_case_keeps_supplied_inferred_and_found_by_code_apart(tmp_path):
    g = ClaimGraph(Case(case_id="DEV-2", variant=Variant(chrom="2", pos=60490908, ref="T", alt="G")))
    annotation = g.record_tool_call(ToolCall(
        tool_call_id=g.reserve_tool_call_id(), tool_name="variant_annotation", execution_status="success",
        retrieval_status="records_found", observations=[{"rsid": "rs1427407", "alleles": "T/G"}],
        requested_by="code", charged_to="code"))
    overlap = g.record_tool_call(ToolCall(
        tool_call_id=g.reserve_tool_call_id(), tool_name="ccre_overlap", execution_status="success",
        retrieval_status="records_found", requested_by="code", charged_to="code"),
        [Evidence(evidence_class="annotation", origin="tool", observed_result="The variant lies in cCRE EH38E0000001.",
                  independence_group="ccre", about_elements=["EH38E0000001"])])
    assert g.add_variant_alias("rs1427407", annotation.tool_call_id)
    assert g.add_variant_element("EH38E0000001", overlap.tool_call_id)
    assert g.add_inferred_candidate(InferredCandidate(kind="disease", label="LDL cholesterol",
                                                      basis_evidence_ids=overlap.evidence_ids,
                                                      note="a trait near the element"), "coordinator")
    html, md, data = render(g, tmp_path)
    case = data["case"]
    assert case["aliases"] == [{"rsid": "rs1427407", "tool_call": "T1", "tool": "variant_annotation"}]
    assert case["elements"] == [{"element": "EH38E0000001", "tool_call": "T2", "tool": "ccre_overlap"}]
    assert case["supplied_disease"] == [] and case["variant"]["rsid"] is None       # the request stays as supplied
    summary = re.search(r'<dl class="facts">(.*?)</dl>', html, re.S).group(1)
    rows = dict(re.findall(r"<dt>(.*?)</dt><dd>(.*?)</dd>", summary))
    assert rows["rsID, found by code"] == "rs1427407 (T1, variant_annotation)"
    assert rows["Elements containing it, found by code"] == "EH38E0000001 (T2, ccre_overlap)"
    assert rows["Disease, inferred"] == "LDL cholesterol (inferred; from E1): a trait near the element"
    assert "none supplied" in rows["Disease, supplied"]
    assert "rs1427407" not in re.search(r"<h1>(.*?)</h1>", html).group(1)     # never shown as the supplied rsID
    assert "- rsID, found by code: rs1427407 (T1, variant\\_annotation)" in md
    assert "- Disease, inferred: LDL cholesterol (inferred; from E1): a trait near the element" in md


def test_a_report_says_when_bundle_files_changed_after_the_run(tmp_path):
    _, run = synthetic_run(tmp_path)
    assert bundle.load_bundle(run).integrity == ()
    with open(run / "metrics.json", "a", encoding="utf-8") as f:
        f.write(" ")
    assert bundle.load_bundle(run).integrity == ("metrics.json has changed since the run was written",)
    html, md = report.write_reports(run)
    assert "Changed after the run." in html.read_text().split("<noscript>")[0]
    assert "metrics.json has changed since the run was written" in md.read_text()


def test_whether_a_run_can_be_replayed_is_the_engines_record_with_its_reasons(tmp_path):
    g = rich_graph()
    reasons = ["critic final comparison: a max_tokens retry sent the call twice",
               "the run stopped on its wall-time limit, which a replay would not reach at the same point"]
    html, md, data = render(g, tmp_path, "unreplayable", parts={"stop_reason": "converged", "replayable": False,
                                                                 "not_replayable": reasons})
    assert data["meta"]["replay"] == {"replayable": False, "reasons": reasons, "of": None}
    assert summary_rows(html)["Replay"] == report._h("not replayable: " + "; ".join(reasons))
    assert f"- Replay: not replayable: {report._md(reasons[0])}; " in md
    html, md, _ = render(g, tmp_path, "replayable", parts={"stop_reason": "converged", "replayable": True,
                                                           "not_replayable": []})
    assert summary_rows(html)["Replay"].startswith("replayable: no model reply was retried, refused or lost")
    assert "- Replay: replayable: " in md
    # nothing is said where nothing was recorded (an evidence bundle, an older run)
    html, md, data = render(g, tmp_path, "unrecorded")
    assert data["meta"]["replay"]["replayable"] is None and "Replay" not in summary_rows(html)
    # a folder that `v2m v9 replay` wrote names the run it re-executed, by folder, and how that came out
    html, md, data = render(g, tmp_path, "replay", extra={"replay_of": {
        "run_folder": str(tmp_path / "runs" / "REQ-1"), "status": "identical", "differences": 0}})
    assert data["meta"]["replay"]["of"] == {"run": "REQ-1", "status": "identical",
                                            "status_label": "identical to the saved run", "differences": 0}
    assert '<span class="tag mode">Replay</span>' in html.split("<noscript>")[0]
    assert summary_rows(html)["Replay of"] == "REQ-1: identical to the saved run (0 differences)"
    assert data["provenance"]["manifest"]["replay_of"]["status"] == "identical"


def test_reinstated_hypotheses_and_rejections_that_no_longer_stand_are_shown(tmp_path):
    g = reinstatement_graph()
    html, md, data = render(g, tmp_path)
    h1, h2 = data["hypotheses"]
    reinstate = [e for e in g.events if e.action == "reinstate"]
    rejects = [e for e in g.events if e.action == "reject"]
    audit = next(e for e in g.events if e.action == "audit").event_id
    assert [e.target_ids[0] for e in reinstate] == ["H1", "H2"] and len(rejects) == 3
    # H1: rejected, its contradiction withdrawn, reinstated by code as deferred
    assert h1["disposition"] == "deferred" and h1["stale_rejection"] is None
    assert [(x["event"], x["rejected_by"], x["claims"]) for x in h1["reinstated"]] == [
        (reinstate[0].event_id, rejects[0].event_id, ["C1"])]
    assert h1["reinstated_notes"] == [f"H1 was reinstated as deferred by {reinstate[0].event_id}: the contradiction "
                                      f"of C1 that rejected it ({rejects[0].event_id}) was withdrawn."]
    assert h1["reason"] == "the activation used another construct"           # the reason recorded with it
    assert [s["disposition"] for s in h1["states"]] == ["active", "rejected", "deferred"]
    # H2: reinstated once, rejected again, withdrawn again: the second rejection is final, and no longer stands
    assert h2["disposition"] == "rejected" and [r["event"] for r in h2["rejections"]] == [rejects[1].event_id,
                                                                                         rejects[2].event_id]
    assert [s["disposition"] for s in h2["states"]] == ["active", "rejected", "deferred", "rejected"]
    stale = h2["stale_rejection"]
    assert (stale["claims"], stale["rested_on"], stale["rejected_by"], stale["noted_by"]) == (
        ["C2"], ["C2"], rejects[2].event_id, [audit])
    note = (f"The rejection of H2 no longer stands: none of its required claims (C2) is contradicted in scope now; it "
            f"was rejected by {rejects[2].event_id} on C2; the engine noted this in {audit}; ")
    assert h2["stale_note"] == note + "it was reinstated once already, and a second rejection is final."
    # without the engine's recorded reason (an older note), the report says what the graph shows
    state = json.loads(g.to_json())
    del next(e for e in state["events"] if e["event_id"] == audit)["details"]["why"]
    _, _, older = render(ClaimGraph.from_json(json.dumps(state)), tmp_path, "older-note")
    assert older["hypotheses"][1]["stale_note"] == note + (f"it was reinstated once already "
                                                           f"({reinstate[1].event_id}), so this later rejection is "
                                                           "final.")
    rows = summary_rows(html)
    assert rows["Reinstated"] == report._h(" ".join(h1["reinstated_notes"] + h2["reinstated_notes"]))
    assert rows["Rejections that no longer stand"] == report._h(h2["stale_note"])
    assert f"- Rejections that no longer stand: {report._md(h2['stale_note'])}" in md
    hypotheses = next(t for t in static_tables(html) if "<caption>Hypotheses" in t)
    assert report._h(h2["stale_note"]) in hypotheses and report._h(h1["reinstated_notes"][0]) in hypotheses
    reinstate_events = [e for e in data["events"] if e["action"] == "reinstate"]
    assert [e["group"] for e in reinstate_events] == ["decisions", "decisions"]


def test_questions_code_closed_as_refused_are_listed_with_their_reason(tmp_path):
    g = reinstatement_graph()
    html, md, data = render(g, tmp_path)
    refused = [q for q in data["questions"] if q["status"] == "refused"]
    assert [q["id"] for q in refused] == ["Q2"] and refused[0]["answer"].startswith("not asked again: it repeats Q1")
    line = ("Q2 (literature): Does an allele-specific reporter assay of the enhancer exist? Not asked again: it "
            "repeats Q1 (same route, tool requests and target claims, none changed since); see Q1's answer.")
    assert f"<li>{report._h(line)}</li>" in re.search(r"<noscript>(.*?)</noscript>", html, re.S).group(1)
    assert f"## Questions closed without being asked (refused)\n\n- {report._md(line)}" in md
    _, md, _ = render(rich_graph(), tmp_path, "none-refused")
    assert "closed without being asked" not in md


def test_evidence_names_the_variants_it_is_about(tmp_path):
    g = ClaimGraph(dev_case())
    eid = tool_evidence(g, "annotation", "The enhancer holding rs1427407 and rs629301.", tool="ccre_overlap",
                        about_elements=["EH38E0000001"],
                        about_variants=["rs1427407", "chr2:60490908 T>G", "rs629301", "the G allele"])
    other = tool_evidence(g, "annotation", "A cCRE overlap about another variant.", tool="ccre_overlap",
                          about_elements=["EH38E0000002"], about_variants=["chr2:60490908 T>C"])
    c = claim(g, [VARIANT], "overlaps", [ELEMENT], assertion_text="rs1427407 lies in the enhancer")
    g.link(c, eid, "supports", "computational_investigator", "names the case variant and the element")
    _, _, data = render(g, tmp_path)
    assert data["evidence"][eid]["about"]["variants"] == ["rs1427407", "chr2:60490908 T>G", "rs629301",
                                                          "the G allele"]
    assert [x["frame"] for x in data["evidence"][eid]["variants"]] == ["case", "case", "other", None]
    assert data["evidence"][other]["variants"] == [{"text": "chr2:60490908 T>C", "frame": "other"}]


def test_a_discordant_group_shows_both_items_and_counts_as_linked_through_either(tmp_path):
    g = ClaimGraph(dev_case())
    g_item, t_item, agree = discordant_inventory(g).evidence_ids
    binds_t = claim(g, [VARIANT], "alters_binding", [tf("SPI1")], "increases", effect_allele="T",
                    assertion_text="T increases SPI1 binding")
    g.link(binds_t, t_item, "supports", "computational_investigator", "SPI1's own model favours T")
    html, md, data = render(g, tmp_path)
    split = data["inventory"]["rows"][0]
    assert (split["group"], split["evidence"], split["discordant"]) == ("G049", g_item, True)
    assert split["items"] == [{"id": g_item, "allele": "G", "tfs": ["SPI1", "SPIB"]},
                              {"id": t_item, "allele": "T", "tfs": ["ELF5", "SPI1"]}]
    assert split["claims"] == [binds_t] and data["inventory"]["linked"] == 1     # linked through the T item
    assert data["inventory"]["rows"][1]["discordant"] is False
    assert data["evidence"][g_item]["inventory"] and data["evidence"][t_item]["inventory"]
    evidence_table = next(t for t in static_tables(html) if "<caption>Evidence" in t)
    assert f"<td>{g_item}</td>" not in evidence_table    # the unlinked allele's item stays in the inventory table
    assert f"<td>{t_item}</td>" in evidence_table        # the linked one is listed with the claims' evidence
    cell = (f"{g_item}: G binds more (models of SPI1, SPIB); {t_item}: T binds more (models of ELF5, SPI1); the "
            f"group's gate-passing models disagree (linked: {binds_t})")
    assert report._h(cell) in html and report._md(cell) in md


def test_the_page_wraps_long_tokens_and_always_prints_light():
    css = re.search(r"<style>(.*?)</style>", report.TEMPLATE.read_text(), re.S).group(1)
    # long ids (QBiC-SELEX model names, HGVS, URLs) wrap inside main instead of widening the page at phone width
    assert re.search(r"(?:^|[}\s])main\{[^}]*overflow-wrap:anywhere", css)
    # dark tokens apply on screen only, so a printout is light whichever theme the reader chose
    dark = [m.start() for m in re.finditer(r"--bg:#0f1719", css)]
    screens = [(m.start(), m.end()) for m in re.finditer(r"@media screen[^{]*\{:root[^{]*\{[^}]*\}\}", css)]
    assert len(dark) == 2 and all(any(a <= i < b for a, b in screens) for i in dark)
    printing = re.search(r"@media print\{(.*)", css, re.S).group(1)
    assert ".print-only{display:block}" in printing and ".inspector" in printing.split("{display:none")[0]
