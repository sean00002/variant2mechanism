# v2m run report: GRCh38 chr1:209815925 A&gt;G

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (34 tool calls); a model was called only to read articles (19 model calls), so no hypothesis was proposed.

Case REQ-45ce1e858e9c · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs642961 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E2863563 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**4 chains tie for first: AP-2Α → UTP25, IRF6, SYT14 or TRAF3IP3. They differ in the target gene and the gene to trait link.**

Reading the tie. A second model read the experiments that no cell of the table counts (2 experiments on 1 tied candidate, asked twice with the candidates in opposite orders and kept only where both readings agree; each time it also had to turn down a made-up candidate): no answer that is kept ties a tied candidate to this variant's site, so the tie stands as it is. It could not tell for the gene IRF6.

Measured: TF binding. Association only: target gene, gene to trait, variant to trait. No claim: regulatory activity.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | AP-2Α | allele-resolved assay; QBiC-SELEX: no model for it; in place: a ChIP-seq peak over the variant |
| Regulatory activity | – | no claim |
| Target gene | UTP25, IRF6, SYT14, TRAF3IP3 (tied) | association |
| Gene to trait | UTP25 → systolic blood pressure and 10 more | association |
| Variant to trait | systolic blood pressure and 7 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | AP-2Α → UTP25 | allele-resolved assay; QBiC-SELEX: no model for it; in place: a ChIP-seq peak over the variant | association | UTP25 → systolic blood pressure, UTP25 → hematological measurement, UTP25 → mean arterial pressure (tied): association | tied for first |
| 1= | AP-2Α → IRF6 | allele-resolved assay; QBiC-SELEX: no model for it; in place: a ChIP-seq peak over the variant | association | IRF6 → systolic blood pressure, IRF6 → cleft lip (tied): association | tied for first |
| 1= | AP-2Α → SYT14 | allele-resolved assay; QBiC-SELEX: no model for it; in place: a ChIP-seq peak over the variant | association | SYT14 → systolic blood pressure, SYT14 → mean arterial pressure (tied): association | tied for first |
| 1= | AP-2Α → TRAF3IP3 | allele-resolved assay; QBiC-SELEX: no model for it; in place: a ChIP-seq peak over the variant | association | TRAF3IP3 → systolic blood pressure, TRAF3IP3 → hematological measurement, TRAF3IP3 → mean arterial pressure, and 1 more (tied): association | tied for first |
| 5 | AP-2Α → C1ORF74 | allele-resolved assay; QBiC-SELEX: no model for it; in place: a ChIP-seq peak over the variant | association | C1ORF74 → systolic blood pressure, C1ORF74 → hematological measurement, C1ORF74 → orofacial cleft (tied): predicted | weaker on gene to trait |
| 6= | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → UTP25 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | UTP25 → systolic blood pressure, UTP25 → hematological measurement, UTP25 → mean arterial pressure (tied): association | weaker on TF binding |
| 6= | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → IRF6 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | IRF6 → systolic blood pressure, IRF6 → cleft lip (tied): association | weaker on TF binding |
| 6= | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → SYT14 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SYT14 → systolic blood pressure, SYT14 → mean arterial pressure (tied): association | weaker on TF binding |

697 more chains not shown, 17 of them tied at rank 6. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 4 tied for first: AP-2Α → UTP25. The run stated 6 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | AP-2Α | nothing found | no source (no QBiC-SELEX model covers it) | supports: 1 (assay) |
| TF binding | The parts are in place | AP-2Α | nothing found | no source | supports: 1 (occupancy) |
| Regulatory activity | The alleles differ | ENSR1\_B3JM9C; EH38E2863563 (not stated by the run) | nothing found | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks); 2 set aside |
| Regulatory activity | The parts are in place | ENSR1\_B3JM9C; EH38E2863563 | supports: 2 (annotation) | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | UTP25 | supports: 44 (association) | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |
| Target gene | The parts are in place | UTP25 (not stated by the run) | nothing found | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |
| Trait | The alleles differ | systolic blood pressure; hematological measurement; mean arterial pressure and 5 more | supports: 22 (association) | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | UTP25 → systolic blood pressure; UTP25 → hematological measurement; UTP25 → mean arterial pressure and 1 more | supports: 28 (association) | supports: 14 (prediction) | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |

Literature: 19 articles naming the variant were found and 14 read, each once, by a model that returned 10 experiments; 6 passed code's checks against the text and were filed as records. Of the rest, 2 did not name the variant in the text retrieved, 3 were reviews.

Second reading: a second model, from another provider, read 2 of the 2 experiments that are the only record behind a cell, each with its paragraph and the claims it counts for (code counts 2 in all, and an answer on any other could not change a cell). Of 2 claims checked it found 2 shown, 0 not shown and could not tell for 0. A record is not counted for a claim it found not shown; it can add nothing.

The table passes every rule of docs/chain-table.md.

## Outcome

**Partial mechanism**; stopped because converged.

4 chains tie for first: AP-2Α → UTP25, IRF6, SYT14 or TRAF3IP3. They differ in the target gene and the gene to trait link. Measured: TF binding. Association only: target gene, gene to trait, variant to trait. No claim: regulatory activity. Filled by code from databases and model predictions, and from 14 of 19 article(s) found that name the variant, each read once by a model: 6 experiment(s) were filed as records. A second model, from another provider, read 2 of the 2 experiment(s) that are the only record behind a cell (code counts 2 in all) against the claims they count for: of 2 claim(s)

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
