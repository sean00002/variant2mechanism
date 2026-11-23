# Saved v9 runs and development reports

Each folder is a v9 run folder: the bundle (`manifest.json`, `graph.json`, `evidence.jsonl`, `events.jsonl`,
`tool_calls.jsonl`, `metrics.json` and the raw tool results in `raw/`) and its two reports. Neither needs a key, the
network or `data/` to be read.

| Folder | Size | What it is |
|---|---|---|
| `synthetic_repair/` | 0.2 MB | The engine on the synthetic repair fixture, with scripted role outputs. Not biological evidence. |
| `rs12740374_evidence/` | 5.3 MB | The evidence bundle of chr1:109274968 G>T (rs12740374), made offline. No model call, no hypothesis. |
| [`three-case-demo-20261110/`](three-case-demo-20261110/index.html) | Small portable HTML + audit JSON | Historical partial GATA1/TAL1 support and two new live checks; retrieval and variant-mapping failures reported explicitly. |
| [`recovery-check-20261110/`](recovery-check-20261110/index.html) | Portable HTML + audit JSON | Earlier recovery check: primary papers found, but extraction and identity failures remain; $5 ceiling audit. |
| [`repair-alias-check-20261110/`](repair-alias-check-20261110/index.html) | Portable HTML + audit JSON | Latest: source-local extraction repair and verified aliases; both frozen reruns retain supported partial mechanisms, with complete chains still unresolved. |

## `synthetic_repair/`

Made with `v2m v9 fixture synthetic --out demo/v9/synthetic_repair` (no model, network or `data/`). The synthetic
variant V lies in element E (C1, supported). H1 requires that activating E decreases gene X (C2) and that the decrease
explains phenotype P (C3, which depends on C2). The fixture's matched experiment shows X increasing, so C2 is
contradicted in scope and code rejects H1 at that assessment; C3 is flagged as unsupported because its premise failed,
not contradicted. A regenerated restatement of H1 is refused (same structure), H2 (E regulates gene Y) stays
unresolved, the coordinator stops and the run ends with no supported explanation.

`trace.jsonl` lists the seven scripted calls. The fixture run's cache of scripted replies and its budget file are left
out: the scripts are in `src/variant2mechanism/v9/fixtures/synthetic_repair.json`.

## `rs12740374_evidence/`

Code's fact collection for the variant given by coordinates only, in cache-only mode (saved HTTP responses and
`cache/qbic.sqlite`; nothing was fetched), then copied with `v2m v9 export` (the public copy; nothing needed cutting):

```
v2m v9 evidence --variant chr1:109274968:G>T --mode cache-only --out runs/dev_v9_release/m1_evidence_rs12740374
v2m v9 export --run runs/dev_v9_release/m1_evidence_rs12740374 --out demo/v9/rs12740374_evidence
```

| Tool | Status | Result |
|---|---|---|
| variant_annotation | success | VEP: 3' UTR variant of CELSR2; rs12740374 at these alleles (recorded as the variant's rsID); reference allele verified |
| ccre_overlap | success | lies in cCRE EH38E1374646 (dELS), recorded as the variant's element; 86 SCREEN gene links |
| qbic_inventory | success | 631 model-sharing groups in a neutral order (DNA-binding domain, then group id); 182 pass the Bonferroni gate, each with Evidence (four whose gate-passing models disagree about the allele have one item per allele: 186 items) |
| gtex_eqtl | success | 39 significant GTEx v8 eQTLs |
| chip_occupancy | success | survey: 471 factors have a peak containing the variant (a survey makes no Evidence) |
| credible_sets_l2g | success, incomplete | survey by trait of 189 of 2316 credible sets (an earlier cached query); no trait given, so no Evidence |
| gwas_associations | success, incomplete | 100 of 698 associations: the next page is not in the HTTP cache |
| screen_online | unavailable | no SCREEN API key; the local SCREEN snapshot (ccre_overlap) is used |

Tools that need an argument (a TF, gene, trait or query) are not run for an evidence bundle.

## Opening, rendering and replaying

- Open `report.html` in a browser. It loads nothing from elsewhere; its links go to the sources (PubMed, ENCODE).
  `report.md` is the text version.
- Render the reports again from the bundle alone: `v2m v9 report --run demo/v9/<folder> --out <new folder>`.
- Replay: `v2m v9 replay demo/v9/<folder> --out <new folder>` re-runs the run from its saved tool answers (and, for the
  fixture, its scripts) and compares the graphs. Both folders replay identically (exit 0), also without `data/` and
  the caches. A replay exits 2 and names what is missing when it needs something the folder and caches do not hold:
  a model reply that is not in the response cache, a raw result (a public copy of a run that read articles keeps
  only the verified passages), or the fixture file a run was made from. It exits 1 when the result differs or a
  saved file changed.
- A new run is not a replay: without the HTTP cache and `data/`, a cache-only run records each tool's missing input
  in its tool call (cache_miss, unavailable, or an error naming the missing file) and fetches nothing.
