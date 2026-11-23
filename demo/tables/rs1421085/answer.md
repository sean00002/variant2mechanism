# v2m run report: GRCh38 chr16:53767042 T&gt;C

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (33 tool calls); a model was called only to read articles (13 model calls), so no hypothesis was proposed.

Case REQ-78ffee415395 · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs1421085 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E3181208 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**12 chains tie for first: G121 (ARID3A, ARID3B, ARID3C), G103 (USF1, USF2), G021 (FOS, FOSB, FOSL1 and 1 more) or 9 more → IRX3. They differ only in the transcription factor.**

Reading the tie. No experiment on file names one of the tied candidates beyond the records the table counts, so nothing read from the articles separates the tied chains.

Measured: regulatory activity, target gene. Association only: gene to trait, variant to trait. Predicted only: TF binding.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G121 (ARID3A, ARID3B, ARID3C), G103 (USF1, USF2), G021 (FOS, FOSB, FOSL1 and 1 more), G040 (JUN, JUNB, JUND), and 8 more (tied) | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | EH38E3181208 | allele-resolved assay |
| Target gene | IRX3 | edit or perturbation |
| Gene to trait | IRX3 → atrial fibrillation and 1 more | association |
| Variant to trait | body weights and measures and 141 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | G121 (ARID3A, ARID3B, ARID3C) → IRX3 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | edit or perturbation | IRX3 → atrial fibrillation, IRX3 → cataract (tied): association | tied for first |
| 1= | G103 (USF1, USF2) → IRX3 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | edit or perturbation | IRX3 → atrial fibrillation, IRX3 → cataract (tied): association | tied for first |
| 1= | G021 (FOS, FOSB, FOSL1 and 1 more) → IRX3 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | edit or perturbation | IRX3 → atrial fibrillation, IRX3 → cataract (tied): association | tied for first |
| 1= | G040 (JUN, JUNB, JUND) → IRX3 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | edit or perturbation | IRX3 → atrial fibrillation, IRX3 → cataract (tied): association | tied for first |
| 1= | G055 (ATF3, JDP2) → IRX3 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | edit or perturbation | IRX3 → atrial fibrillation, IRX3 → cataract (tied): association | tied for first |
| 1= | G047 (ONECUT1, ONECUT2, ONECUT3) → IRX3 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | edit or perturbation | IRX3 → atrial fibrillation, IRX3 → cataract (tied): association | tied for first |
| 1= | G007 (FOXC1, FOXC2, FOXD1 and 25 more) → IRX3 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | edit or perturbation | IRX3 → atrial fibrillation, IRX3 → cataract (tied): association | tied for first |
| 1= | G022 (FOXA1, FOXA2, FOXA3 and 3 more) → IRX3 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | edit or perturbation | IRX3 → atrial fibrillation, IRX3 → cataract (tied): association | tied for first |

2742 more chains not shown, 4 of them tied at rank 1. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 12 tied for first: G121 (ARID3A, ARID3B, ARID3C) → IRX3. The run stated 7 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G121 (ARID3A, ARID3B, ARID3C) | nothing found | supports: 1 (prediction) | nothing found (9 of 19 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 19 of the 54 experiments it returned did not pass code's checks) |
| TF binding | The parts are in place | G121 (ARID3A, ARID3B, ARID3C) | supports: 1 (occupancy) | no source | nothing found (9 of 19 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 19 of the 54 experiments it returned did not pass code's checks) |
| Regulatory activity | The alleles differ | EH38E3181208 | nothing found | no source | supports: 1 (assay); 26 set aside |
| Regulatory activity | The parts are in place | EH38E3181208 | supports: 1 (annotation) | no source | nothing found (9 of 19 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 19 of the 54 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | IRX3 | supports: 2 (association) | no source | supports: 5 (edit); 5 set aside |
| Target gene | The parts are in place | IRX3 (not stated by the run) | nothing found | no source | nothing found (9 of 19 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 19 of the 54 experiments it returned did not pass code's checks); 12 set aside |
| Trait | The alleles differ | body weights and measures; waist circumference; urate measurement and 139 more | supports: 296 (association) | no source | nothing found (9 of 19 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 19 of the 54 experiments it returned did not pass code's checks); 1 set aside |
| Trait | The parts are in place | IRX3 → atrial fibrillation; IRX3 → cataract; IRX3 → urate measurement and 3 more | supports: 2 (association) | supports: 4 (prediction) | nothing found (9 of 19 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 19 of the 54 experiments it returned did not pass code's checks); 10 set aside |

Literature: 19 articles naming the variant were found and 9 read, each once, by a model that returned 54 experiments; 35 passed code's checks against the text and were filed as records. Of the rest, 3 did not name the variant in the text retrieved, 7 were reviews.

Second reading: a second model, from another provider, read 2 of the 2 experiments that are the only record behind a cell, each with its paragraph and the claims it counts for (code counts 7 in all, and an answer on any other could not change a cell). Of 2 claims checked it found 2 shown, 0 not shown and could not tell for 0. A record is not counted for a claim it found not shown; it can add nothing.

The table passes every rule of docs/chain-table.md.

## Outcome

**Multiple explanations**; stopped because converged.

12 chains tie for first: G121 (ARID3A, ARID3B, ARID3C), G103 (USF1, USF2), G021 (FOS, FOSB, FOSL1 and 1 more) or 9 more → IRX3. They differ only in the transcription factor. Measured: regulatory activity, target gene. Association only: gene to trait, variant to trait. Predicted only: TF binding. Filled by code from databases and model predictions, and from 9 of 19 article(s) found that name the variant, each read once by a model: 35 experiment(s) were filed as records. A second model, from another provider, read 2 of the 2 experiment(s) that are the only record behind a cell (code counts 7 in

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
