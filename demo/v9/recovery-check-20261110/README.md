# Evidence recovery check — 10 November 2026

Open `index.html`. Styles and case/stage controls are embedded; without JavaScript all cases are shown.
The HTML can be shared alone. Keep the JSON files alongside it for audit links. No website was published.

Same frozen implementation, coordinates/alleles/origin only, one final run per case:

- rs12740374: primary paper found, but two extractions failed quote validation and no literature evidence was retained.
- TERT C228T: primary GABP paper found, but shorthand-to-case identity was unresolved and no literature evidence was retained.

The earlier rs12740374 integration failure is included in `intermediate-run.json`. No attempts were discarded.
The changes improve evidence presentation, discovery and API/identity plumbing; end-to-end molecular recovery
still fails in these two development examples. They are not a blind benchmark or a controlled ablation.

1,110 unique tests passed, one real-cluster test skipped. Six mock-cluster tests passed after correcting the
subprocess Python environment. HTML structure, links and JavaScript interactions were checked; visual rendering
was not checked. This task cost $0.101298. Cumulative ledger: $0.566387 / $5, with no reservations remaining.

Source runs remain in `runs/dev_v9_release/dev10_rs12740374_general_recovery_20261110`,
`dev11_rs12740374_general_recovery_20261110` and `dev12_tert_c228t_general_recovery_20261110`.
This summary does not package full article bodies, model caches or credentials, and is not a standalone replay.
`scripts/v9_recovery_report.py` renders it from saved graphs and audit files without model/network calls.
