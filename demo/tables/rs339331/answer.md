# v2m run report: GRCh38 chr6:116888889 T&gt;C

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (37 tool calls); a model was called only to read articles (16 model calls), so no hypothesis was proposed.

Case REQ-12f98a50d718 · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs339331 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E2496909 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**Leading chain: G024 (HOXA13, HOXB13, HOXC13 and 1 more) → RFX6.**

Measured: TF binding, target gene. Association only: gene to trait, variant to trait. No claim: regulatory activity.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G024 (HOXA13, HOXB13, HOXC13 and 1 more) | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to T; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | – | no claim |
| Target gene | RFX6 | edit or perturbation |
| Gene to trait | RFX6 → prostate carcinoma and 3 more | association |
| Variant to trait | concentration of small HDL particles measurement and 26 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1 | G024 (HOXA13, HOXB13, HOXC13 and 1 more) → RFX6 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to T; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | edit or perturbation | RFX6 → prostate carcinoma, RFX6 → platelet count, RFX6 → prostate cancer, and 1 more (tied): association | leads |
| 2= | G010 (GATA1, GATA2, GATA3 and 3 more) → RFX6 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to C; in place: a ChIP-seq peak over the variant | edit or perturbation | RFX6 → prostate carcinoma, RFX6 → platelet count, RFX6 → prostate cancer, and 1 more (tied): association | the same kinds of evidence on every link; no strong prediction (a change in the top 10% for the TF group, with a ChIP-seq peak over the variant) |
| 2= | G016 (AR, NR3C1, NR3C2 and 1 more) → RFX6 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to C; in place: a ChIP-seq peak over the variant | edit or perturbation | RFX6 → prostate carcinoma, RFX6 → platelet count, RFX6 → prostate cancer, and 1 more (tied): association | the same kinds of evidence on every link; no strong prediction (a change in the top 10% for the TF group, with a ChIP-seq peak over the variant) |
| 4 | SMAD4 → RFX6 | allele-resolved assay; QBiC-SELEX: no model for it; in place: a ChIP-seq peak over the variant | edit or perturbation | RFX6 → prostate carcinoma, RFX6 → platelet count, RFX6 → prostate cancer, and 1 more (tied): association | weaker on TF binding (no QBiC-SELEX prediction in support) |
| 5= | G024 (HOXA13, HOXB13, HOXC13 and 1 more) → GOPC | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to T; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | GOPC → prostate carcinoma, GOPC → diabetes mellitus (tied): association | weaker on target gene |
| 5= | G024 (HOXA13, HOXB13, HOXC13 and 1 more) → MARCKS | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to T; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | MARCKS → diabetes mellitus: association | weaker on target gene |
| 5= | G024 (HOXA13, HOXB13, HOXC13 and 1 more) → CEP85L | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to T; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | CEP85L → diabetes mellitus: association | weaker on target gene |
| 8= | G010 (GATA1, GATA2, GATA3 and 3 more) → GOPC | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to C; in place: a ChIP-seq peak over the variant | association | GOPC → prostate carcinoma, GOPC → diabetes mellitus (tied): association | weaker on target gene |

4336 more chains not shown, 5 of them tied at rank 8. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain: G024 (HOXA13, HOXB13, HOXC13 and 1 more) → RFX6. The run stated 7 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G024 (HOXA13, HOXB13, HOXC13 and 1 more) | supports: 1 (assay) | supports: 1 (prediction) | supports: 4 (assay) |
| TF binding | The parts are in place | G024 (HOXA13, HOXB13, HOXC13 and 1 more) | supports: 33 (occupancy) | no source | supports: 8 (occupancy) |
| Regulatory activity | The alleles differ | EH38E2496909 (not stated by the run) | nothing found | no source | nothing found (12 of 17 articles found were read by the model; 5 not looked into (a review, no text, a failed call or the cap); 12 of the 77 experiments it returned did not pass code's checks); 11 set aside |
| Regulatory activity | The parts are in place | EH38E2496909 | supports: 1 (annotation) | no source | nothing found (12 of 17 articles found were read by the model; 5 not looked into (a review, no text, a failed call or the cap); 12 of the 77 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | RFX6 | supports: 6 (association) | no source | supports: 3 (edit); 8 set aside |
| Target gene | The parts are in place | RFX6 | nothing found | no source | supports: 4 (edit); 27 set aside |
| Trait | The alleles differ | concentration of small HDL particles measurement; prostate carcinoma; secretogranin-1 measurement and 24 more | supports: 88 (association) | no source | nothing found (12 of 17 articles found were read by the model; 5 not looked into (a review, no text, a failed call or the cap); 12 of the 77 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | RFX6 → prostate carcinoma; RFX6 → platelet count; RFX6 → prostate cancer and 23 more | supports: 8 (association) | supports: 74 (prediction) | nothing found (12 of 17 articles found were read by the model; 5 not looked into (a review, no text, a failed call or the cap); 12 of the 77 experiments it returned did not pass code's checks); 18 set aside |

Literature: 17 articles naming the variant were found and 12 read, each once, by a model that returned 77 experiments; 65 passed code's checks against the text and were filed as records. Of the rest, 4 were reviews, 1 could not be retrieved.

Second reading: a second model, from another provider, read 1 of the 1 experiments that are the only record behind a cell, each with its paragraph and the claims it counts for (code counts 28 in all, and an answer on any other could not change a cell). Of 2 claims checked it found 1 shown, 0 not shown and could not tell for 1. A record is not counted for a claim it found not shown; it can add nothing.

The table passes every rule of docs/chain-table.md.

## Outcome

**Partial mechanism**; stopped because converged.

Leading chain: G024 (HOXA13, HOXB13, HOXC13 and 1 more) → RFX6. Measured: TF binding, target gene. Association only: gene to trait, variant to trait. No claim: regulatory activity. Filled by code from databases and model predictions, and from 12 of 17 article(s) found that name the variant, each read once by a model: 65 experiment(s) were filed as records. A second model, from another provider, read 1 of the 1 experiment(s) that are the only record behind a cell (code counts 28 in all) against the claims they count for: of 2 claim(s) checked it found 0 not shown by the text, and those were

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
