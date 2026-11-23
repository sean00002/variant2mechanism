# Extraction repair and variant identity — 10 November 2026

Open `index.html`. Styles and case/stage controls are embedded; without JavaScript all cases are shown.
The HTML can be shared alone. Keep the JSON and test log alongside it for audit links. No website was published.

Both new runs used the same frozen implementation and only coordinates, alleles and origin:

- rs12740374: supported in-vitro binding difference and Hep3B reporter effect; genomic direction and the complete
  disease chain remain unresolved. Five literature records from one primary paper were retained.
- TERT C228T: verified alias and allele-resolved reporter effect; endogenous regulation, a specific TF and disease
  mediation remain unresolved. One primary-paper experiment was retained.

Source-local retries were exercised in both runs. One rs12740374 retry still failed an invalid span selection;
the refusal and subsequent ordinary extraction are retained in the audit. No run was repeated until a desired
answer appeared. These are known positive development examples, not a blind benchmark or controlled ablation.

1,120 tests passed, one real-cluster test skipped. Lint passed. The source/configuration, previous graphs and
gold labels were hash-checked. HTML structure, links and JavaScript interactions were checked; visual rendering
was not checked. This task cost $0.124541. Cumulative ledger: $0.690928 / $5, with no reservations remaining.

Source runs remain in `runs/dev_v9_release/dev13_rs12740374_source_repair_20261110` and
`dev14_tert_c228t_alias_repair_20261110`. Before/after baselines are dev11/dev12. The summary includes extracted
passages and failure records; it does not package complete article bodies, model caches or credentials and is
not a standalone replay. `scripts/v9_repair_alias_report.py` renders it without model/network calls.
