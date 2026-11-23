"""Source-local extraction repair and alias resolution: report saved development runs only."""

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
    audit = json.loads((source.parent / "repair-audit.json").read_text())
    rows, panels, tabs, summaries, identity_rows, repair_rows = [], [], [], [], [], []
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
        checkpoints = audit[case["case_id"]]
        repair_rows.append(
            f"<tr><th>{esc(case['case_id'])}</th>"
            f"<td>{len(checkpoints['repair_model_calls'])}</td>"
            f"<td>{esc(', '.join(e['evidence_id'] for e in checkpoints['source_spans']) or 'none')}</td>"
            f"<td>{esc(reviews[case['case_id']]['repair_result'])}</td></tr>"
        )
        for eid, ev in graph.evidence.items():
            proof = ev.data.get("variant_identity")
            if proof:
                identity_rows.append(
                    f"<tr><td>{esc(case['case_id'])} · {eid}</td><td>{esc(proof['paper_variant'])} · {esc(proof['placement_assembly'])}</td>"
                    f"<td>{esc(proof['case_key'])}</td><td>{esc(proof['paper_allele'])} → {esc(proof['case_allele'])}</td>"
                    f'<td><a href="{esc(proof["source"])}">Verified identity source</a> · {esc(proof["tool_call"])}</td></tr>'
                )
    summary = verification["conclusion"]
    spend = verification["budget_after"]["dev"]["spent"]
    page = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>v2m · Extraction repair and variant identity</title><style>
:root{--ink:#172d36;--muted:#53666d;--line:#d9e0dc;--green:#16675a}*{box-sizing:border-box}body{margin:0;background:#f3f5f0;color:var(--ink);font:16px/1.6 system-ui,-apple-system,sans-serif}main{max-width:1160px;margin:auto;padding:40px 24px 70px}header{padding:18px 0 30px}h1{font-size:clamp(2.2rem,5vw,3.7rem);line-height:1.12;letter-spacing:-.035em;max-width:900px}h2{font-size:1.8rem;line-height:1.25}section,.card{background:white;border:1px solid var(--line);border-radius:14px;padding:24px;margin:20px 0}.lead{font-size:20px}.eyebrow{text-transform:uppercase;letter-spacing:.12em;color:var(--green);font-size:12px;font-weight:700}.fine,.meta,small{font-size:13px;color:var(--muted)}a{color:var(--green)}nav,.stages{display:flex;gap:10px;flex-wrap:wrap;margin:22px 0}button{border:1px solid var(--line);border-radius:24px;padding:11px 18px;background:white;font:inherit;color:var(--ink);cursor:pointer}button.selected{background:var(--ink);color:white}button:focus-visible{outline:3px solid #e8bd73;outline-offset:3px}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{padding:12px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}th{background:#f4f6f2}.verdict{background:#e8f3ed;border-left:4px solid var(--green);padding:16px 20px;display:flex;flex-direction:column}.nodes{display:grid;grid-template-columns:1fr 2fr 1fr;gap:16px;align-items:center;text-align:center}.nodes>b{background:#f2f4f1;border:1px solid var(--line);border-radius:9px;padding:16px;overflow-wrap:anywhere}.claim{border:1px solid var(--line);border-left:4px solid #986722;border-radius:9px;padding:18px;margin:14px 0}.claim.supported{border-left-color:var(--green)}.claim.contradicted{border-left-color:#a64747}.claim.early{border-left-color:#71858b}.connection{border-bottom:2px dashed #986722;padding-bottom:10px;overflow-wrap:anywhere}.supported .connection{border-bottom:2px solid var(--green)}.connection small{display:block}.support{font-size:12px;margin-top:8px}details{border-top:1px solid var(--line);padding:16px 0}summary{font-weight:650;cursor:pointer}li{margin:8px 0}code{font-size:.85em;overflow-wrap:anywhere}[hidden]{display:none!important}@media(max-width:700px){main{padding:24px 14px}.nodes{grid-template-columns:1fr;gap:8px}section{padding:18px}.claim{padding:12px}}@media print{.case[hidden],.stage[hidden]{display:block!important}nav,.stages{display:none}body{background:white}}
</style></head><body><noscript><style>.case[hidden],.stage[hidden]{display:block!important}</style></noscript><main>
<header><div class="eyebrow">variant2mechanism · development audit · 10 November 2026</div><h1>Repair the source. Resolve the variant. Keep the evidence.</h1><p class="lead">CONCLUSION</p><p>Two new runs used only variant coordinates, alleles and origin. The implementation was frozen before both. Expected factors, genes and paper identifiers were not supplied to the agents.</p></header>
<section><h2>Before and after</h2><div class="scroll"><table><thead><tr><th>Run</th><th>Supported molecular claims</th><th>Accepted literature records</th><th>Model / tools / reads</th><th>Input tokens, cumulative</th><th>Cost</th><th>Stop reason</th></tr></thead><tbody>ROWS</tbody></table></div><p class="fine">A literature record is an extracted assay, not an independent paper. Several claims can share the same observation. Caching and different agent decisions confound this comparison; it is not a controlled ablation.</p></section>
<section><h2>What changed in this revision</h2><ol>
<li><b>Source-local repair.</b> A newly refused extraction receives one bounded retry per source/location before another discovery round. The retry includes the exact failure, original read ID and whole-sentence selectors. Code copies the selected sentence verbatim, then applies the existing assay, scope, identity and direction checks. Accepted experiments and earlier failed attempts remain auditable.</li>
<li><b>Three-state identity.</b> Same variant, different variant and unresolved are separate outcomes. A bounded set of catalogue SNV names is checked against exact NCBI placements in the catalogue's declared build. The names and their identity status are visible to every investigator; only verified matches establish a case alias. A numeric suffix or a complementary name alone never establishes identity.</li>
<li><b>Paper-scoped observations survive.</b> A nucleotide shorthand actually named in a promoter/sequence experiment can be retained in that paper's namespace. Without a verified mapping, it cannot support or contradict a case-variant claim. Exact catalogue name, gene and ordered alleles can supply a mapping; original notation and strand conversion remain in provenance.</li>
<li><b>No-change reading control.</b> Repeated abstract text now participates in the same content-based check as full text. New source passages or genuinely different claim scopes remain investigable. The original call and currency caps still apply, including the audit and final-comparison reserve.</li>
</ol><p>These are general rules. No variant-specific genes, factors, expected answers or primary-paper lists were added to production code. Both new runs received only coordinates, alleles and origin; prior runs and gold files remain unchanged.</p></section>
<section><h2>Did the repair run in practice?</h2><p><b>Refused extraction → original saved source → one repair attempt → normal verification → retained evidence or an explicit processing gap.</b> No additional HTTP request is needed for this repair. A valid copied sentence still has to pass the scientific checks.</p><div class="scroll"><table><thead><tr><th>Case</th><th>Repair calls</th><th>Accepted source-span records</th><th>Observed result</th></tr></thead><tbody>REPAIRS</tbody></table></div><p class="fine">Repair calls and failures are included in the costs above. A repair can fail; the loop is bounded rather than retried until it produces a desired answer.</p></section>
<nav aria-label="Choose a rerun">TABS</nav>PANELS
<section><h2>Verified paper-to-case mappings in the new runs</h2><div class="scroll"><table><thead><tr><th>Record</th><th>Paper position / matched assembly</th><th>Case</th><th>Effect allele</th><th>Provenance</th></tr></thead><tbody>IDENTITY</tbody></table></div><p class="fine">Identity mapping does not establish a biological effect or transfer an assay to another cellular context. When the paper omits the build, the record explicitly retains that omission and requires one matching primary-assembly placement.</p></section>
<section><h2>How to read the result</h2><p>Finding a paper, retaining an experiment, mapping its variant and supporting a claim are separate checkpoints. An unresolved paper-scoped assay is useful progress, but it is not case-specific molecular recovery. A reporter result cannot establish an endogenous mechanism, and binding support cannot by itself complete a disease chain.</p><p>The case audits above identify the actual remaining gaps and refused updates. No run was repeated simply until a desired biological answer appeared. Before/after comparisons use known positive development cases and different agent decisions; they do not establish generalisation or isolate a causal effect for each change.</p></section>
<section><h2>What still needs work</h2><ol><li><b>Separate experimental comparisons within a passage.</b> The rs12740374 paragraph describes both minor-versus-major binding and antibody-induced impairment. The original direction check conflated them; repair retained a direction-unspecified observation. A future comparison-scoped representation should identify the intervention, comparator and endpoint for each result before assigning polarity.</li><li><b>Resolve paper-local allele labels explicitly.</b> Minor/major labels still cannot be turned into T/G without an audited definition. Search existing figure captions, tables and sequence legends for that definition, retaining each location. An image-only definition needs an image-capable evidence route; otherwise leave it unresolved.</li><li><b>Reuse claims and correct invalid links.</b> Unassessed duplicate reporter drafts remain beside their supported successors. Group-level prediction links were refused because their rationale did not identify the model's members; the critic noticed this but the final graph did not repair the link. These are graph-update problems, not missing biology.</li><li><b>Make alias searches more selective.</b> The TERT run issued a loosely grouped OR query before finding the primary study. A query builder that quotes aliases and groups Boolean clauses could reduce irrelevant results. This was not changed after seeing the rerun.</li></ol><p>These are remaining limitations and suggested next steps, not additional fixes claimed as complete. Neither adding more agents nor simply increasing the currency budget resolves them.</p></section>
<section><h2>Validation, budget and limits</h2><p>TESTS. Previous graphs and gold labels were preserved; the frozen implementation hashes match both reruns. The two new runs cost <b>NEWSPEND</b>; cumulative development spend is <b>SPEND / $5.000000</b>, leaving <b>REMAINING</b>. No cluster prediction jobs were submitted; computational predictions used saved QBiC-SELEX results.</p><p>Both runs stopped under the existing guarded model-call allowance, not because $5 was exhausted. Each used 17 sends; the configured ceiling is 24, but retries, audit and final comparison capacity are reserved conservatively. The unchanged guard can stop new investigations before all 24 sends are spent.</p><p>These are known positive development examples. They cannot establish specificity, clinical validity or generalisation. Unsupported links stay open, and the critic's whole-hypothesis outcome is shown separately from supported molecular claims. Browser rendering was not visually checked; structural and interaction checks are reported in the accompanying validation file.</p><p>Audit: <a href="results.json">results</a> · <a href="verification.json">preservation and budget checks</a> · <a href="manual-review.json">case audit</a> · <a href="repair-audit.json">repair and identity checkpoints</a> · <a href="html-validation.json">HTML checks</a> · <a href="test-results.txt">test log</a>.</p><p>API references: <a href="https://dev.europepmc.org/RestfulWebService">Europe PMC REST search</a> · <a href="https://civicdb.org/api/graphiql">CIViC GraphQL</a> · <a href="https://www.ncbi.nlm.nih.gov/variation/notation/">NCBI variation notation</a>.</p></section>
</main><script>
document.querySelectorAll('[data-case]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('.case').forEach(x=>x.hidden=x.id!==button.dataset.case);document.querySelectorAll('[data-case]').forEach(x=>x.classList.toggle('selected',x===button));}));
document.querySelectorAll('[data-stage]').forEach(button=>button.addEventListener('click',()=>{const section=button.closest('.case');section.querySelectorAll('[data-view]').forEach(x=>x.hidden=x.dataset.view!==button.dataset.stage);section.querySelectorAll('[data-stage]').forEach(x=>x.classList.toggle('selected',x===button));}));
</script></body></html>"""
    for key, value in {
        "CONCLUSION": esc(summary),
        "ROWS": "".join(rows),
        "TABS": "".join(tabs),
        "PANELS": "".join(panels),
        "REPAIRS": "".join(repair_rows),
        "NEWSPEND": f"${verification['this_task_cost']:.6f}",
        "REMAINING": f"${verification['remaining_budget_usd']:.6f}",
        "SPEND": f"${spend:.6f}",
        "TESTS": esc(verification["tests"]),
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
