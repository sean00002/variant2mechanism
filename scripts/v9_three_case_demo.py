"""Render a portable, evidence-linked demo from saved runs; never runs an agent or loads gold into one."""

import argparse
import hashlib
import html
import json
from pathlib import Path

from variant2mechanism.v9.graph import ClaimGraph
from variant2mechanism.v9.resolution import MOLECULAR, support_summary


def esc(x):
    return html.escape(str(x), quote=True)


def number(identifier):
    return int(identifier[1:])


def source_link(e):
    for source in e.source_ids:
        if source.startswith("PMID:"):
            return f'<a href="https://pubmed.ncbi.nlm.nih.gov/{esc(source[5:])}/">{esc(source)}</a>'
        if source.startswith("DOI:"):
            return f'<a href="https://doi.org/{esc(source[4:])}">{esc(source)}</a>'
    return esc(", ".join(e.source_ids[:2]))


def load_case(name, path, historical, review):
    graph = ClaimGraph.from_json((path / "graph.json").read_text())
    metrics = json.loads((path / "metrics.json").read_text())
    boundary = next(
        (
            number(e.event_id)
            for e in graph.events
            if e.action == "tool_call"
            and any(x in graph.tool_calls and graph.tool_calls[x].charged_to == "agent" for x in e.target_ids)
        ),
        10**9,
    )
    initial = {c.claim_id for c in graph.claims.values() if c.history and number(c.history[0].event_id) < boundary}
    final = support_summary(graph)
    summary = {
        "case": name,
        "historical": historical,
        "origin": graph.case.origin,
        "request": {
            "variant": graph.case.variant.key,
            "supplied_disease": graph.case.supplied_disease,
            "supplied_context": [x.model_dump(mode="json") for x in graph.case.supplied_context],
        },
        "run_folder": path.name,
        "graph_sha256": hashlib.sha256((path / "graph.json").read_bytes()).hexdigest(),
        "resolution": final,
        "stored_outcome": graph.result.outcome,
        "stop_reason": graph.result.stop_reason,
        "cost": metrics["model"]["cost_usd"],
        "model_calls": metrics["model"]["calls"],
        "tool_calls": metrics["tools"]["executed"],
        "literature_reads": metrics["tools"]["by_tool"].get("literature_read", {}).get("executed", 0),
        "accepted_literature_records": sum(e.origin == "literature" for e in graph.evidence.values()),
        "review": review,
        "initial_claim_ids": sorted(initial, key=number),
        "claim_count": len(graph.claims),
        "evidence_count": len(graph.evidence),
    }
    return graph, summary


def edge(graph, c, early=False):
    ids = [x.evidence_id for x in c.evidence_links]
    status = "proposed structure" if early else graph.display(c.claim_id).status
    style = (
        "early"
        if early
        else (
            "supported"
            if status in ("supported", "supported_with_proxy")
            else "contradicted"
            if "contradicted" in status
            else "open"
        )
    )
    scope = c.context_scope.label if c.context_scope else "context unspecified"
    support = (
        "Initial structure; evidence status intentionally hidden"
        if early
        else "<br>".join(
            f"{esc(x.evidence_id)} · {esc(x.stance)} · {esc(x.strength)}/{esc(x.applicability)} · "
            f"{source_link(graph.evidence[x.evidence_id])}"
            for x in c.evidence_links[:4]
        )
        or "No accepted evidence link"
    )
    if not early and len(ids) > 4:
        support += f"<br>{len(ids) - 4} further links in the saved graph"
    left = " + ".join(graph.entities[e].label for e in c.subject_ids)
    right = " + ".join(graph.entities[e].label for e in c.object_ids)
    return f"""<div class="claim {style}"><div class="nodes"><b>{esc(left)}</b><div class="connection">
<strong>{esc(c.relation.replace("_", " "))} →</strong><small>{esc(c.direction)} · allele {esc(c.effect_allele or "not applicable")}</small>
<div class="support">{support}</div></div><b>{esc(right)}</b></div><p class="meta">{esc(c.claim_id)} · {esc(status)} · {esc(scope)}</p></div>"""


def panel(graph, summary, index):
    review = summary["review"]
    molecular = summary["resolution"]
    claims = list(graph.claims.values())
    shown = [c for c in claims if c.relation in MOLECULAR | {"regulates"}]
    early = "".join(edge(graph, c, True) for c in shown if c.claim_id in summary["initial_claim_ids"])
    final = "".join(edge(graph, c) for c in shown)
    rows = "".join(
        f"<tr><td>{esc(c.claim_id)}</td><td>{esc(' + '.join(graph.entities[e].label for e in c.subject_ids))}</td>"
        f"<td>{esc(c.relation)}</td><td>{esc(' + '.join(graph.entities[e].label for e in c.object_ids))}</td>"
        f"<td>{esc(c.assessment)}</td><td>{esc(', '.join(x.evidence_id for x in c.evidence_links) or 'none')}</td></tr>"
        for c in claims
    )
    hyps = "".join(
        f"<tr><td>{esc(h.hypothesis_id)}</td><td>{esc(h.title)}</td><td>{esc(h.disposition)}</td>"
        f"<td>{esc(', '.join(h.required_claim_ids))}</td><td>{esc(', '.join(h.claim_ids))}</td></tr>"
        for h in graph.hypotheses.values()
    )
    refuses = "".join(
        f"<li><b>{esc(e.event_id)}</b> {esc(e.concise_reason)}</li>"
        for e in graph.events
        if e.action == "refuse_update"
    )
    lit = "".join(
        f"<tr><td>{esc(e.evidence_id)}</td><td>{source_link(e)}</td><td>{esc(e.evidence_class)}</td>"
        f"<td>{esc(e.direction)} · {esc(e.allele)}</td><td>{esc(', '.join(e.about_tfs))}</td></tr>"
        for e in graph.evidence.values()
        if e.origin == "literature"
    )
    reads = "".join(
        f"<li><b>{esc(t.tool_call_id)}</b> {esc(t.tool_name)}: {esc(json.dumps(t.query_parameters))}</li>"
        for t in graph.tool_calls.values()
        if t.tool_name in ("literature_search", "literature_read")
    )
    notes = "".join(f"<li>{esc(n)}</li>" for n in review.get("notes", []))
    return f"""<section id="case-{index}" class="case" {"hidden" if index else ""}>
<div class="eyebrow">{"Historical run · new report view only" if summary["historical"] else "New live development check · frozen implementation"}</div>
<h2>{esc(summary["case"])}</h2><p>{esc(summary["request"]["variant"])} · {esc(summary["origin"])} · no supplied disease or tissue</p>
<div class="verdict"><strong>{esc(molecular["molecular_label"])}</strong><span>{esc(molecular["required_link_label"])}</span></div>
<p>{esc(review.get("verdict", "Review pending"))}</p><ul>{notes}</ul>
<p class="fine">Stored whole-hypothesis outcome: <code>{esc(summary["stored_outcome"])}</code>. Stop reason: <code>{esc(summary["stop_reason"])}</code>. Molecular findings and ranking are separate; unchanged required-link thresholds still apply.</p>
<div class="stages"><button data-stage="early">Initial candidate structure</button><button data-stage="final" class="selected">Final evidence graph</button></div>
<div class="stage" data-view="early" hidden><p>Claims proposed before the first agent-requested tool call. This view shows their structure, not reconstructed initial evidence assessments.</p>{early or "<p>No molecular claim was proposed at this stage.</p>"}</div>
<div class="stage" data-view="final"><p>All binding, regulatory-activity, RNA and regulatory-target claims. The complete claim inventory, including association branches, is below.</p>{final or "<p>No molecular claim was retained.</p>"}</div>
<details><summary>All {summary["claim_count"]} claims and their evidence IDs</summary><div class="scroll"><table><thead><tr><th>Claim</th><th>From</th><th>Relation</th><th>To</th><th>Assessment</th><th>Evidence</th></tr></thead><tbody>{rows}</tbody></table></div></details>
<details><summary>Hypotheses: required versus retained claims</summary><div class="scroll"><table><thead><tr><th>ID</th><th>Hypothesis</th><th>Disposition</th><th>Required claims</th><th>All retained claims</th></tr></thead><tbody>{hyps}</tbody></table></div></details>
<details><summary>Accepted literature evidence</summary><div class="scroll"><table><thead><tr><th>ID</th><th>Source</th><th>Class</th><th>Direction / allele</th><th>Factors</th></tr></thead><tbody>{lit or '<tr><td colspan="5">No literature experiment accepted.</td></tr>'}</tbody></table></div></details>
<details><summary>Literature tool trace</summary><ol>{reads or "<li>No literature calls.</li>"}</ol></details>
<details><summary>Refused updates and reasons</summary><ul>{refuses or "<li>No refused updates recorded.</li>"}</ul></details>
<p class="fine">Run: {esc(summary["run_folder"])}<br>Graph SHA-256: <code>{summary["graph_sha256"]}</code></p></section>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    manifest = Path(args.manifest)
    inputs = json.loads(manifest.read_text())
    review = json.loads((manifest.parent / "manual-review.json").read_text())
    checks = json.loads((manifest.parent / "verification.json").read_text())
    cases = [("rs1427407", Path(inputs["rs1427407_run"]), True)] + [
        (c["case_id"], Path(c["run"]), False) for c in inputs["cases"]
    ]
    loaded = [load_case(n, p, old, review[n]) for n, p, old in cases]
    summaries = [s for _, s in loaded]
    buttons = "".join(
        f'<button data-case="case-{i}" class="{"selected" if not i else ""}">{esc(s["case"])}</button>'
        for i, s in enumerate(summaries)
    )
    rows = "".join(
        f"<tr><th>{esc(s['case'])}</th><td>{'Historical' if s['historical'] else 'New live'}</td>"
        f"<td>{esc(', '.join(s['resolution']['supported_molecular_claim_ids']) or 'none')}</td>"
        f"<td>{esc(s['review'].get('factor_recovery', 'See audit'))}</td><td>{s['model_calls']} / {s['tool_calls']} / {s['literature_reads']}</td><td>${s['cost']:.6f}</td></tr>"
        for s in summaries
    )
    panels = "".join(panel(g, s, i) for i, (g, s) in enumerate(loaded))
    spent = checks["budget_after"]["dev"]["spent"]
    page = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>v2m · From variant to an auditable partial mechanism</title><style>
:root{--ink:#172d36;--muted:#53666d;--green:#16675a;--amber:#986722;--line:#d9e0dc}*{box-sizing:border-box}body{margin:0;background:#f3f5f0;color:var(--ink);font:16px/1.6 system-ui,-apple-system,sans-serif}main{max-width:1160px;margin:auto;padding:42px 26px 70px}header{padding:30px 0 42px}h1{font-size:clamp(2.2rem,5vw,3.7rem);max-width:900px;line-height:1.12;letter-spacing:-.035em;margin:14px 0 24px}h2{font-size:2rem;margin:12px 0}h3{font-size:1.15rem}.eyebrow{text-transform:uppercase;letter-spacing:.12em;font-size:12px;color:var(--green);font-weight:750}.lead{font-size:20px;max-width:840px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.tile,section{background:#fff;border:1px solid var(--line);border-radius:14px;padding:24px;margin-bottom:20px}.tile p{margin-bottom:0}.tile{margin:0}nav,.stages{display:flex;flex-wrap:wrap;gap:10px;margin:26px 0}button{border:1px solid var(--line);background:#fff;color:var(--ink);border-radius:30px;padding:11px 18px;font:inherit;cursor:pointer}button.selected{background:var(--ink);color:white;border-color:var(--ink)}button:focus-visible{outline:3px solid #e8bd73;outline-offset:3px}.verdict{background:#e8f3ed;border-left:4px solid var(--green);padding:16px 20px;display:flex;flex-direction:column;gap:4px}.fine,.meta,small{font-size:13px;color:var(--muted)}.nodes{display:grid;grid-template-columns:1fr 2fr 1fr;gap:18px;align-items:center;text-align:center}.nodes>b{background:#f2f4f1;border:1px solid var(--line);border-radius:9px;padding:16px;overflow-wrap:anywhere}.claim{border:1px solid var(--line);border-left:4px solid var(--amber);border-radius:9px;padding:18px;margin:14px 0}.claim.supported{border-left-color:var(--green)}.claim.contradicted{border-left-color:#a64747}.claim.early{border-left-color:#71858b}.connection{border-bottom:2px dashed var(--amber);padding-bottom:10px;overflow-wrap:anywhere}.supported .connection{border-bottom:2px solid var(--green)}.connection small{display:block}.support{font-size:12px;margin-top:8px}.meta{margin-bottom:0}a{color:var(--green)}details{border-top:1px solid var(--line);padding:16px 0}summary{font-weight:650;cursor:pointer}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px;margin:14px 0}th,td{padding:11px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}th{background:#f4f6f2}code{overflow-wrap:anywhere;font-size:.85em}li{margin:7px 0}.key{display:flex;flex-wrap:wrap;gap:20px;font-size:13px}.key span:before{content:'— ';color:var(--green)}.key span:nth-child(2):before{content:'┄ ';color:var(--amber)}[hidden]{display:none!important}@media(max-width:700px){main{padding:24px 14px}.grid{grid-template-columns:1fr}.nodes{grid-template-columns:1fr;gap:8px}section{padding:18px}h2{font-size:1.7rem}.claim{padding:12px}}@media print{body{background:white}.case[hidden],.stage[hidden]{display:block!important}nav,.stages{display:none}section{break-inside:avoid}main{padding:0}details>*{display:block!important}}
</style></head><body><noscript><style>.case[hidden],.stage[hidden]{display:block!important}</style></noscript><main>
<header><div class="eyebrow">variant2mechanism · small open-source agent demo · 10 November 2026</div>
<h1>From a variant to an auditable partial mechanism.</h1><p class="lead">Agents propose claims, inspect experiments and revise hypotheses. Every accepted link keeps its evidence and scope. Missing links stay visible.</p>
<p>Three known-variant examples: one historical development run and two new checks with the implementation frozen beforehand. Only coordinates, alleles and germline/somatic origin were supplied.</p>
<p><b>Current result:</b> the historical case retains two supported binding claims. Neither new case recovered a supported molecular claim within its resource limits. This is a transparent engineering demo with diagnosed failures, not evidence that mechanism recovery is reliable yet.</p></header>
<div class="grid"><div class="tile"><h3>1 · Propose</h3><p>Build candidate mechanism chains from variant annotation, regulatory databases and saved QBiC predictions.</p></div><div class="tile"><h3>2 · Investigate and repair</h3><p>Read primary studies, follow citations, verify experiments and repair individual claims without discarding valid evidence.</p></div><div class="tile"><h3>3 · Report two things</h3><p>Which molecular claims are supported? Which required links remain unresolved? A partial finding need not be a complete disease explanation.</p></div></div>
<section style="margin-top:24px"><h2>What these runs demonstrate</h2><p>Finding a paper, accepting an experiment and adopting it into a hypothesis are separate checkpoints. Factor recovery below refers to evidence-linked claims, not a name appearing in generated prose.</p><div class="scroll"><table><thead><tr><th>Case</th><th>Run type</th><th>Supported molecular claims</th><th>Factor recovery audit</th><th>Model / tools / reads</th><th>Recorded cost</th></tr></thead><tbody>ROWS</tbody></table></div><p class="fine">Counts include cached calls; timings and costs are not controlled performance comparisons. Gold labels remain outside agent inputs. The existing gold specification is unreviewed, so this is an engineering demonstration, not a validated benchmark.</p></section>
<nav aria-label="Choose a case">BUTTONS</nav><div class="key"><span>Supported claim in its stated scope</span><span>Unresolved / limited evidence</span></div>PANELS
<section id="bottlenecks"><h2>Where the new checks stalled</h2>
<div class="scroll"><table><thead><tr><th>Checkpoint</th><th>rs12740374</th><th>TERT C228T</th></tr></thead><tbody>
<tr><th>Candidate generation</th><td>SORT1, PSRC1, CELSR2 and GSTM2 candidates; a C/EBP model-sharing group was proposed, with no supported member assignment.</td><td>Promoter activity and TERT expression candidates. Annotation overlap was supported, but this does not establish an allelic effect.</td></tr>
<tr><th>Primary experiment discovery</th><td>The expected 2010 mechanistic study was not read. Both selected reads had abstract-only access.</td><td>A review led to the 2013 Huang reporter study; its full text and figure captions were available.</td></tr>
<tr><th>Evidence acceptance</th><td>No literature experiment accepted.</td><td>Two extractions of the same reporter result were refused. The result paragraph used C228T/C250T; the coordinates were defined elsewhere in the paper. The local identity check did not join those statements.</td></tr>
<tr><th>Case mapping and scope</th><td>No supported C/EBP binding claim or completed target mechanism.</td><td>No verified paper-to-case build/strand mapping entered the graph. A promoter reporter would also need its own assay-scoped claim; it cannot silently establish endogenous cCRE activity.</td></tr>
<tr><th>Resource constraint</th><td>698 GWAS records contributed to 1,013 evidence records; 534,710 input tokens were processed across model calls. The next planner request needed a $0.1120 worst-case reservation and was refused.</td><td>17 model calls completed. Investigation stopped at the call-reservation guard, which protects repair, audit and final-comparison capacity; it did not use all 24 permitted calls.</td></tr>
</tbody></table></div>
<p>The TERT run also encountered a CIViC GraphQL schema error. GTEx had no genotype for the queried variant; that is missing coverage, not a negative expression result. The final critic preserved uncertainty, but recommending a new experiment before resolving a literature identity problem is inefficient.</p>
<p>The reporter study is <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4423787/">Huang et al. (2013)</a>. This audit uses saved tool responses and refusal events; it does not add evidence to either run.</p>
<h3>Small, general changes to test next</h3><ol>
<li><b>Bound the evidence shown to each model.</b> Preserve every raw record and candidate. Group repeated associations by trait, target, tissue and source; pass a compact index with evidence IDs and allow focused expansion. Check retrieval coverage and token use on the same frozen inputs. Reducing repeated payload is different from rejecting weak candidates.</li>
<li><b>Resolve paper-local names, then map to the case.</b> Store an explicit source-backed mapping from a paper's shorthand to its stated coordinate and allele. Separately verify assembly conversion and strand orientation using a trusted variant resource. Multiple mutations in one article require separate mappings; ambiguous mappings stay unresolved. Test synthetic aliases, two nearby variants, opposite strands and incomplete build information, not only TERT.</li>
<li><b>Refine the claim to the assay.</b> Retain a verified reporter result as a reporter-scoped molecular claim while leaving the endogenous mechanism unresolved. Article identity, case identity and assay applicability are three separate checks.</li>
<li><b>Repair the CIViC adapter and add a recorded-response contract check.</b> Treat API errors separately from an empty result. Then evaluate one fixed revision under a separately agreed budget, including unresolved or negative controls.</li>
</ol><p>No extra agents or biological exceptions were added after these results. The two runs were not repeated until successful.</p></section>
<section><h2>What changed in this version</h2><ul><li>Partial molecular findings—including optional claims—are reported separately from the whole-hypothesis comparison. Winner criteria and required-link thresholds are unchanged.</li><li>A malformed literature claim update is refused individually. Experiments still pass passage, assay, allele, context and direction checks; valid experiments and valid sibling updates survive.</li><li>Typed binding-claim and allele-direction instructions provide targeted repair guidance. Computational-investigator version checks retain their existing strict repair behaviour.</li></ul>
<h3>Verification and limits</h3><p>TESTS. The source, configuration and previous-run checks are recorded in the accompanying verification artifact. Browser rendering was not checked; HTML structure and links were checked.</p><p>Cumulative development spend: <b>SPEND / $0.500000</b>. These two new positive cases cannot measure specificity, exclude memorisation or establish generalisation. Retrieval and extraction failures remain explicit. All earlier runs and gold labels were preserved.</p><p>Biological references: <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4018826/">Bauer et al. (2013)</a> · <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3062476/">Musunuru et al. (2010)</a> · <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4456397/">Bell et al. (2015)</a>.</p></section>
<p class="fine">Audit files: <a href="results.json">case summaries</a> · <a href="verification.json">preservation and budget checks</a> · <a href="evaluation-plan.json">predeclared evaluation</a> · <a href="manual-review.json">manual audit</a>. This HTML file contains its own styles and interactions; source links need internet access and the audit files are optional companions.</p>
</main><script>
document.querySelectorAll('[data-case]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('.case').forEach(x=>x.hidden=x.id!==button.dataset.case);document.querySelectorAll('[data-case]').forEach(x=>x.classList.toggle('selected',x===button));}));
document.querySelectorAll('[data-stage]').forEach(button=>button.addEventListener('click',()=>{const section=button.closest('.case');section.querySelectorAll('[data-view]').forEach(x=>x.hidden=x.dataset.view!==button.dataset.stage);section.querySelectorAll('[data-stage]').forEach(x=>x.classList.toggle('selected',x===button));}));
</script></body></html>"""
    for key, value in {
        "ROWS": rows,
        "BUTTONS": buttons,
        "PANELS": panels,
        "TESTS": esc(checks["tests"]),
        "SPEND": f"${spent:.6f}",
    }.items():
        page = page.replace(key, value)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page)
    (out / "results.json").write_text(json.dumps({"cases": summaries, "verification": checks}, indent=2) + "\n")
    print(out / "index.html")


if __name__ == "__main__":
    main()
