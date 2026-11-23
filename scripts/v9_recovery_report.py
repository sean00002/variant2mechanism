"""Portable before/after audit of two frozen development reruns; reads saved artefacts only."""

import argparse
import html
import json
from pathlib import Path

from v9_three_case_demo import load_case, panel, source_link


def esc(value):
    return html.escape(str(value), quote=True)


def experiment_audit(graph):
    rows = []
    for ev in graph.evidence.values():
        if ev.origin != "literature" or ev.experiment is None:
            continue
        ex = ev.experiment
        rows.append(
            f"<tr><td>{esc(ev.evidence_id)} · {source_link(ev)}<br>{esc(ev.retrieval_ref)} / {esc(ex.location)}</td>"
            f"<td>{esc(ex.intervention)}<br>{esc(ex.system.tissue_or_cell)}</td>"
            f"<td>{esc(ev.observed_result)}</td><td>{esc(ex.scope_does_not_test)}</td></tr>"
        )
    return '<details><summary>What the accepted experiments actually test</summary><div class="scroll"><table>' + (
        '<thead><tr><th>Evidence / source / tool</th><th>Assay and system</th><th>Extracted result</th>'
        '<th>Unresolved scope</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></div></details>"
        if rows else "<tbody><tr><td>No literature experiment accepted.</td></tr></tbody></table></div></details>"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    source = Path(args.inputs)
    data = json.loads(source.read_text())
    root = Path(data["repo"])
    reviews = json.loads((source.parent / "manual-review.json").read_text())
    verification = json.loads((source.parent / "verification.json").read_text())
    diagnostics = json.loads((source.parent / "packet-diagnostic.json").read_text())
    intermediate = json.loads((source.parent / "intermediate-run.json").read_text())
    rows, panels, tabs, summaries, identity_rows = [], [], [], [], []
    for i, case in enumerate(data["cases"]):
        before_graph, before = load_case(case["case_id"], root / "runs/dev_v9_release" / case["before"], True, {})
        graph, after = load_case(
            case["case_id"], root / "runs/dev_v9_release" / case["after"], False, reviews[case["case_id"]]
        )
        rendered = panel(graph, after, i)
        panels.append(rendered.rsplit("</section>", 1)[0] + experiment_audit(graph) + "</section>")
        tabs.append(
            f'<button data-case="case-{i}" class="{"selected" if i == 0 else ""}">{esc(case["case_id"])}</button>'
        )
        for label, result in [("Before", before), ("After", after)]:
            metrics = json.loads((root / "runs/dev_v9_release" / result["run_folder"] / "metrics.json").read_text())
            rows.append(
                f"<tr><th>{esc(case['case_id'])} · {label}</th><td>{esc(', '.join(result['resolution']['supported_molecular_claim_ids']) or 'none')}</td>"
                f"<td>{result['accepted_literature_records']}</td><td>{result['model_calls']} / {result['tool_calls']} / {result['literature_reads']}</td>"
                f"<td>{metrics['model']['input_tokens']:,}</td><td>${result['cost']:.6f}</td><td>{esc(result['stop_reason'])}</td></tr>"
            )
        summaries.append({"case": case["case_id"], "before": before, "after": after})
        for eid, ev in graph.evidence.items():
            proof = ev.data.get("variant_identity")
            if proof:
                identity_rows.append(
                    f"<tr><td>{esc(case['case_id'])} · {eid}</td><td>{esc(proof['paper_variant'])} · {esc(proof['placement_assembly'])}</td>"
                    f"<td>{esc(proof['case_key'])}</td><td>{esc(proof['paper_allele'])} → {esc(proof['case_allele'])}</td>"
                    f'<td><a href="{esc(proof["source"])}">NCBI placement</a> · {esc(proof["tool_call"])}</td></tr>'
                )
    summary = verification["conclusion"]
    spend = verification["budget_after"]["dev"]["spent"]
    page = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>v2m · Evidence recovery checks</title><style>
:root{--ink:#172d36;--muted:#53666d;--line:#d9e0dc;--green:#16675a}*{box-sizing:border-box}body{margin:0;background:#f3f5f0;color:var(--ink);font:16px/1.6 system-ui,-apple-system,sans-serif}main{max-width:1160px;margin:auto;padding:40px 24px 70px}header{padding:18px 0 30px}h1{font-size:clamp(2.2rem,5vw,3.7rem);line-height:1.12;letter-spacing:-.035em;max-width:900px}h2{font-size:1.8rem;line-height:1.25}section,.card{background:white;border:1px solid var(--line);border-radius:14px;padding:24px;margin:20px 0}.lead{font-size:20px}.eyebrow{text-transform:uppercase;letter-spacing:.12em;color:var(--green);font-size:12px;font-weight:700}.fine,.meta,small{font-size:13px;color:var(--muted)}a{color:var(--green)}nav,.stages{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0}button{border:1px solid var(--line);border-radius:24px;padding:11px 18px;background:white;font:inherit;color:var(--ink);cursor:pointer}button.selected{background:var(--ink);color:white}button:focus-visible{outline:3px solid #e8bd73;outline-offset:3px}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:12px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}th{background:#f4f6f2}.verdict{background:#e8f3ed;border-left:4px solid var(--green);padding:16px 20px;display:flex;flex-direction:column}.nodes{display:grid;grid-template-columns:1fr 2fr 1fr;gap:16px;align-items:center;text-align:center}.nodes>b{background:#f2f4f1;border:1px solid var(--line);border-radius:9px;padding:16px;overflow-wrap:anywhere}.claim{border:1px solid var(--line);border-left:4px solid #986722;border-radius:9px;padding:18px;margin:14px 0}.claim.supported{border-left-color:var(--green)}.claim.contradicted{border-left-color:#a64747}.claim.early{border-left-color:#71858b}.connection{border-bottom:2px dashed #986722;padding-bottom:10px;overflow-wrap:anywhere}.supported .connection{border-bottom:2px solid var(--green)}.connection small{display:block}.support{font-size:12px;margin-top:8px}details{border-top:1px solid var(--line);padding:16px 0}summary{font-weight:650;cursor:pointer}li{margin:8px 0}code{font-size:.85em;overflow-wrap:anywhere}[hidden]{display:none!important}@media(max-width:700px){main{padding:24px 14px}.nodes{grid-template-columns:1fr;gap:8px}section{padding:18px}.claim{padding:12px}}@media print{.case[hidden],.stage[hidden]{display:block!important}nav,.stages{display:none}body{background:white}}
</style></head><body><noscript><style>.case[hidden],.stage[hidden]{display:block!important}</style></noscript><main>
<header><div class="eyebrow">variant2mechanism · development audit · 10 November 2026</div><h1>Can discovered evidence become a usable claim?</h1><p class="lead">CONCLUSION</p><p>Two new runs used only variant coordinates, alleles and origin. The implementation was frozen before both. Expected factors, genes and paper identifiers were not supplied to the agents.</p></header>
<section><h2>Before and after</h2><div class="scroll"><table><thead><tr><th>Run</th><th>Supported molecular claims</th><th>Accepted literature records</th><th>Model / tools / reads</th><th>Input tokens, cumulative</th><th>Cost</th><th>Stop reason</th></tr></thead><tbody>ROWS</tbody></table></div><p class="fine">A literature record is an extracted assay, not an independent paper. Several claims can share the same observation. The $5 currency ceiling, caching and different agent decisions confound this comparison; it is not a controlled ablation.</p></section>
<section><h2>One failed integration check is retained</h2><p>Before the final two reruns, an rs12740374 check stopped with a planning error: compact views were incompatible with validation that still demanded individual decisions on hundreds of records. That run cost INTERIMCOST and remains saved as INTERIMRUN. The final revision uses an explicit six-group review queue; all other observations stay pending. A second correction preserves every returned paper identifier when search metadata is shortened. Neither correction inserts a biological answer.</p><p><a href="intermediate-run.json">Intermediate result and diagnostic</a>. The implementation was frozen again before the final two reruns. All attempts are included in the budget.</p></section>
<section><h2>What changed</h2><ol>
<li><b>Compact evidence views.</b> Keep all raw records. Show bounded details plus an index, with a local evidence_inspect tool to retrieve omitted records by ID or text/page. On the same saved evidence set, the evidence section changed from OLDCHARS to NEWCHARS characters (REDUCTION% smaller). This is a packet diagnostic, not a live token benchmark.</li>
<li><b>Discovery diversity.</b> A broad, truncated literature search can mix relevance-ranked and citation-ranked results under the same query. The additional retrieval and its status are recorded. Citation count helps locate papers; it never contributes biological support.</li>
<li><b>Source-backed variant identity.</b> An explicit article-local mutation definition can identify the tested coordinate. NCBI primary-assembly placements separately verify the exact input substitution and the strand conversion. The paper notation remains in the experiment record. Ambiguous aliases, wrong alleles and unsupported builds remain unresolved.</li>
<li><b>Claims follow assay scope.</b> Agents are instructed to retain a reporter-scoped claim while leaving endogenous activity and disease mediation open. A reporter does not directly settle an explicitly endogenous activity claim. No factor or target is inserted by code.</li>
<li><b>CIViC schema repair.</b> Alias objects are requested with their name field and converted to names before matching. Browse and variant-detail queries passed a public-API contract check. API failures stay separate from empty searches.</li>
</ol></section>
<nav aria-label="Choose a rerun">TABS</nav>PANELS
<section><h2>Verified paper-to-case mappings in the new runs</h2><div class="scroll"><table><thead><tr><th>Record</th><th>Paper position / matched assembly</th><th>Case</th><th>Effect allele</th><th>Provenance</th></tr></thead><tbody>IDENTITY</tbody></table></div><p class="fine">Identity mapping does not establish a biological effect or transfer an assay to another cellular context. When the paper omits the build, the record explicitly retains that omission and requires one matching primary-assembly placement.</p></section>
<section><h2>The next improvement suggested by these traces</h2><p><b>Make a failed extraction a repair task against the same source.</b> The rs12740374 run found the correct primary paper, but failed passage verification and then spent four reads on another paper's abstract. More currency did not fix this decision loop.</p><ol><li>Retain the failed read ID, passage location and specific validator error in a repair queue. Repair quote selection or scope before launching a new discovery search.</li><li>Have the model select source sentence IDs or verified spans; copy the source text in code. This avoids altered punctuation and overlong quotations without weakening provenance checks.</li><li>Keep a measured allele difference separate from its unresolved mapping to the case's reference/alternate allele. Do not infer minor equals alternate, or treat uncertainty about direction as evidence that the assay never happened.</li><li>Stop repeated abstract-only reads when they return no new information; follow an available full-text section, supplement or citation instead. Show identity metadata separately from biological evidence.</li></ol><p class="fine">These are recommendations from the final audit, not changes made between the two frozen reruns. No additional agents, TF exceptions or case-specific source lists are needed for this repair.</p></section>
<section><h2>Validation, budget and limits</h2><p>TESTS. Previous graphs and gold labels were preserved; the frozen implementation hashes match both reruns. Cumulative development spend: <b>SPEND / $5.000000</b>. No cluster prediction jobs were submitted; computational predictions used saved QBiC-SELEX results.</p><p>These are known positive development examples. They cannot establish specificity, clinical validity or generalisation. Unsupported links stay open, and the critic's whole-hypothesis outcome is shown separately from supported molecular claims. Browser rendering was not visually checked; structural and interaction checks are reported in the accompanying validation file.</p><p>Audit: <a href="results.json">results</a> · <a href="verification.json">preservation and budget checks</a> · <a href="manual-review.json">case audit</a> · <a href="packet-diagnostic.json">packet diagnostic</a> · <a href="html-validation.json">HTML checks</a>.</p><p>API references: <a href="https://dev.europepmc.org/RestfulWebService">Europe PMC REST search</a> · <a href="https://civicdb.org/api/graphiql">CIViC GraphQL</a> · <a href="https://www.ncbi.nlm.nih.gov/variation/notation/">NCBI variation notation</a>.</p></section>
</main><script>
document.querySelectorAll('[data-case]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('.case').forEach(x=>x.hidden=x.id!==button.dataset.case);document.querySelectorAll('[data-case]').forEach(x=>x.classList.toggle('selected',x===button));}));
document.querySelectorAll('[data-stage]').forEach(button=>button.addEventListener('click',()=>{const section=button.closest('.case');section.querySelectorAll('[data-view]').forEach(x=>x.hidden=x.dataset.view!==button.dataset.stage);section.querySelectorAll('[data-stage]').forEach(x=>x.classList.toggle('selected',x===button));}));
</script></body></html>"""
    for key, value in {
        "CONCLUSION": esc(summary),
        "ROWS": "".join(rows),
        "TABS": "".join(tabs),
        "PANELS": "".join(panels),
        "OLDCHARS": f"{diagnostics['old_characters']:,}",
        "NEWCHARS": f"{diagnostics['new_characters']:,}",
        "REDUCTION": str(diagnostics["reduction_percent"]),
        "SPEND": f"${spend:.6f}",
        "TESTS": esc(verification["tests"]),
        "INTERIMCOST": f'${intermediate["metrics"]["cost_usd"]:.6f}',
        "INTERIMRUN": esc(intermediate["run"]),
        "IDENTITY": "".join(identity_rows)
        or '<tr><td colspan="5">No mapped experiment retained in these runs.</td></tr>',
    }.items():
        page = page.replace(key, value)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page)
    (out / "results.json").write_text(
        json.dumps({"comparisons": summaries, "verification": verification}, indent=2) + "\n"
    )
    print(out / "index.html")


if __name__ == "__main__":
    main()
