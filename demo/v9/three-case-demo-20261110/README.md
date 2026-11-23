# Three-case development demo — 10 November 2026

Open `index.html` in a browser. The case tabs and initial/final claim diagrams use inline JavaScript; styles and data
are embedded, with a no-JavaScript fallback showing all cases. The HTML can be shared alone. Keep the JSON files
alongside it to use its audit links. Source-paper links need internet access. No website has been published.

The report contains one historical run rendered under the new partial-support view and two new live checks:

| Case | Request supplied to agents | Result |
|---|---|---|
| rs1427407 | GRCh38 chr2:60490908 T>G; germline | Historical run: GATA1/TAL1 occupancy claims supported; required mechanism links unresolved. |
| rs12740374 | GRCh38 chr1:109274968 G>T; germline | New run: C/EBP group proposed, no supported molecular claim; stopped at currency reservation guard. |
| TERT C228T | GRCh38 chr5:1295113 G>A; somatic | New run: primary reporter study found, extraction/variant mapping unresolved; stopped at call reservation guard. |

No disease, tissue, TF, target gene, paper identifier or gold evaluation file was supplied. The implementation was
frozen before both new runs. These are known positive development cases, not a blind or validated benchmark.
Neither new case recovered an evidence-supported molecular claim, and neither was repeated until successful.

The new code separates partial molecular support from required-link completion and whole-hypothesis ranking.
Literature experiments can survive an invalid sibling claim update, provided they independently pass the existing
evidence checks. This behaviour passed offline regression tests; the two live checks do not establish a recovery
rate. The report explains the remaining retrieval-volume and variant-identity limitations.

Validation: 1,098 tests passed, 1 deselected; v9 lint passed. HTML structure, local links, JavaScript syntax and
case/stage interaction logic were checked. Browser rendering was not visually checked.

New live spend: $0.107888. Shared development ledger: $0.465089 / $0.50, with no outstanding reservations.
Costs include caching and cannot be used as controlled comparisons between cases.

Files:

- `results.json`: graph-derived summaries and manual audit; original graph hashes.
- `evaluation-plan.json`: checklist recorded before the two new runs.
- `manual-review.json`: scope-aware interpretation of the saved outcomes.
- `verification.json`: source freeze, previous graph, configuration, gold and budget checks.
- `density-diagnostic.json`, `tert-diagnostic.json`: observed failure checkpoints.
- `test-results.txt`: full test summary.

The source runs remain in `runs/dev_v9_release/dev7_rs1427407_discovery_leads_20261110`,
`dev8_rs12740374_demo_20261110` and `dev9_tert_c228t_demo_20261110`. This public-sized summary deliberately
does not package full article bodies, model-response caches or credentials. It is not a standalone engine replay.
`scripts/v9_three_case_demo.py` renders from saved graph files and a local input manifest; it makes no model or
network calls. It does not change the saved graphs or their original outcome values.
