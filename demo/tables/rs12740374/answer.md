# v2m run report: GRCh38 chr1:109274968 G&gt;T

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (76 tool calls); a model was called only to read articles (23 model calls), so no hypothesis was proposed.

Case REQ-281b030b14ff · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs12740374 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E1374646 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**12 chains tie for first: G030 (TFAP2A, TFAP2B, TFAP2C and 2 more), G122 (ARNT, ARNT2), G012 (MAF, MAFA, MAFB and 3 more) or 9 more → SORT1. They differ only in the transcription factor.**

Reading the tie. Among the tied chains, experiments that no cell of the table counts point to the TF group G035 (CEBPA, CEBPB, CEBPE) (the difference between the alleles, or the haplotypes that carry them, depends on it). This is a second model's reading of 7 experiments on 1 tied candidate, asked twice with the candidates in opposite orders and kept only where both readings agree; each time it also had to turn down a made-up candidate; it changes no cell and no rank.

Measured: regulatory activity, gene to trait. Association only: target gene, variant to trait. Predicted only: TF binding.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more), G122 (ARNT, ARNT2), G012 (MAF, MAFA, MAFB and 3 more), G035 (CEBPA, CEBPB, CEBPE), and 8 more (tied) | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | EH38E1374646 and 1 more | allele-resolved assay |
| Target gene | SORT1 | association |
| Gene to trait | SORT1 → total plasma cholesterol and 6 more | edit or perturbation |
| Variant to trait | catalase measurement and 247 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → SORT1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SORT1 → total plasma cholesterol, SORT1 → LDL-C, SORT1 → very small LDL particles, and 4 more (tied): edit or perturbation | tied for first |
| 1= | G122 (ARNT, ARNT2) → SORT1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SORT1 → total plasma cholesterol, SORT1 → LDL-C, SORT1 → very small LDL particles, and 4 more (tied): edit or perturbation | tied for first |
| 1= | G012 (MAF, MAFA, MAFB and 3 more) → SORT1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SORT1 → total plasma cholesterol, SORT1 → LDL-C, SORT1 → very small LDL particles, and 4 more (tied): edit or perturbation | tied for first |
| 1= | G035 (CEBPA, CEBPB, CEBPE) → SORT1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SORT1 → total plasma cholesterol, SORT1 → LDL-C, SORT1 → very small LDL particles, and 4 more (tied): edit or perturbation | tied for first |
| 1= | G142 (CEBPD) → SORT1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SORT1 → total plasma cholesterol, SORT1 → LDL-C, SORT1 → very small LDL particles, and 4 more (tied): edit or perturbation | tied for first |
| 1= | G143 (CEBPG) → SORT1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SORT1 → total plasma cholesterol, SORT1 → LDL-C, SORT1 → very small LDL particles, and 4 more (tied): edit or perturbation | tied for first |
| 1= | G227 (MAFF) → SORT1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SORT1 → total plasma cholesterol, SORT1 → LDL-C, SORT1 → very small LDL particles, and 4 more (tied): edit or perturbation | tied for first |
| 1= | G071 (GFI1, GFI1B) → SORT1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SORT1 → total plasma cholesterol, SORT1 → LDL-C, SORT1 → very small LDL particles, and 4 more (tied): edit or perturbation | tied for first |

8364 more chains not shown, 4 of them tied at rank 1. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 12 tied for first: G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → SORT1. The run stated 7 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) | nothing found | supports: 1 (prediction) | nothing found (15 of 18 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 13 of the 38 experiments it returned did not pass code's checks) |
| TF binding | The parts are in place | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) | supports: 7 (occupancy) | no source | nothing found (15 of 18 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 13 of the 38 experiments it returned did not pass code's checks) |
| Regulatory activity | The alleles differ | EH38E1374646; proximal 2.1 kb region | supports: 1 (assay) | no source | supports: 1 (assay); 10 set aside |
| Regulatory activity | The parts are in place | ENSR1\_CDSQQ; EH38E1374646 | supports: 2 (annotation) | no source | nothing found (15 of 18 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 13 of the 38 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | SORT1 | supports: 29 (association) | no source | nothing found (15 of 18 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 13 of the 38 experiments it returned did not pass code's checks); 7 set aside |
| Target gene | The parts are in place | SORT1 (not stated by the run) | nothing found | no source | nothing found (15 of 18 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 13 of the 38 experiments it returned did not pass code's checks); 14 set aside |
| Trait | The alleles differ | catalase measurement; fatty acid amount; apolipoprotein B to apolipoprotein A1 ratio and 245 more | supports: 773 (association) | no source | nothing found (15 of 18 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 13 of the 38 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | SORT1 → total plasma cholesterol; SORT1 → LDL-C; SORT1 → very small LDL particles and 61 more | supports: 22 (association) | supports: 75 (prediction) | supports: 4 (edit); 9 set aside |

Literature: 18 articles naming the variant were found and 15 read, each once, by a model that returned 38 experiments; 25 passed code's checks against the text and were filed as records. Of the rest, 2 did not name the variant in the text retrieved, 1 were reviews.

Second reading: a second model, from another provider, read 5 of the 5 experiments that are the only record behind a cell, each with its paragraph and the claims it counts for (code counts 6 in all, and an answer on any other could not change a cell). Of 10 claims checked it found 10 shown, 0 not shown and could not tell for 0. A record is not counted for a claim it found not shown; it can add nothing.

The table passes every rule of docs/chain-table.md.

## Outcome

**Multiple explanations**; stopped because converged.

12 chains tie for first: G030 (TFAP2A, TFAP2B, TFAP2C and 2 more), G122 (ARNT, ARNT2), G012 (MAF, MAFA, MAFB and 3 more) or 9 more → SORT1. They differ only in the transcription factor. Measured: regulatory activity, gene to trait. Association only: target gene, variant to trait. Predicted only: TF binding. Filled by code from databases and model predictions, and from 15 of 18 article(s) found that name the variant, each read once by a model: 25 experiment(s) were filed as records. A second model, from another provider, read 5 of the 5 experiment(s) that are the only record behind a cell

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
