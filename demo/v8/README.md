# Three saved v8 runs

Each folder is one run of the main arm (`full_given`, repeat 0) from the GPT-6 Luna grid in `runs/eval_v8_luna`: the
rsID was masked and the literature cut at the year of the case's source paper.

| Folder | Case | What it shows |
|---|---|---|
| `rs339331/` | rs339331, prostate cancer, LNCaP | A supported lead: HOXB13 has by far the largest QBiC-SELEX effect (\|z\| 103) and a ChIP-seq summit at the variant; verdict "mechanism" with HOXB13 |
| `tert_c228t/` | TERT promoter C228T, glioblastoma | The right family ranked low: the ETS family has the largest effect (\|z\| 166) but no ETS1 summit in the context, so E2F1 ranks first; the gold TF, GABPA, is an ETS member |
| `rs73706717/` | rs73706717, colorectal cancer, HCT116 | A near-miss control: the TF line says "mechanism" with TCF7L2, and only the absence of a disease association makes the verdict "no mechanism" |

In each folder:

- `report.html`: the mechanism map (variant, chains, element, genes, disease, with every link's tier and the evidence
  behind it). It is self-contained: open it in a browser.
- `report.md`: the verdict, the chains and their tiers, the family screen.
- `report.json`: everything, including every evidence row the models saw.
- `trace.jsonl`: one line per model call, with tokens, cost and time.

The HTML and Markdown were rendered again from `report.json` (`v2m replay <folder> --render-only`). To re-execute a run
offline from the caches and compare it with its saved report: `v2m replay rs339331` (needs the local `data/` folder and
caches).
