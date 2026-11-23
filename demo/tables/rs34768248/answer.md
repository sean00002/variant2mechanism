# v2m run report: GRCh38 chr5:1295601 G&gt;A

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (16 tool calls); no model was called, so no hypothesis was proposed.

Case REQ-250b6f4391bd · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs34768248 (T1, variant\_annotation)
- Elements containing it, found by code: none recorded

## Answer: ranked mechanism chains

**8 chains tie for first: G051 (TCF12, TCF3, TCF4), G335 (SNAI2), G001 (ALX1, ALX3, ALX4 and 110 more) or G265 (NKRF) → PDCD6 or AHRR. They differ in the transcription factor and the target gene and the gene to trait link.**

Reading the tie. No experiment on file names one of the tied candidates beyond the records the table counts, so nothing read from the articles separates the tied chains.

Association only: target gene, gene to trait, variant to trait. Predicted only: TF binding. No claim: regulatory activity.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G051 (TCF12, TCF3, TCF4), G335 (SNAI2), G001 (ALX1, ALX3, ALX4 and 110 more), G265 (NKRF) (tied) | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | – | no claim |
| Target gene | PDCD6, AHRR (tied) | association |
| Gene to trait | PDCD6 → hypertensive disorder and 1 more | association |
| Variant to trait | hypertensive disorder | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | G051 (TCF12, TCF3, TCF4) → PDCD6 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | PDCD6 → hypertensive disorder: association | tied for first |
| 1= | G051 (TCF12, TCF3, TCF4) → AHRR | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | AHRR → hypertensive disorder: association | tied for first |
| 1= | G335 (SNAI2) → PDCD6 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | PDCD6 → hypertensive disorder: association | tied for first |
| 1= | G335 (SNAI2) → AHRR | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | AHRR → hypertensive disorder: association | tied for first |
| 1= | G001 (ALX1, ALX3, ALX4 and 110 more) → PDCD6 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | PDCD6 → hypertensive disorder: association | tied for first |
| 1= | G001 (ALX1, ALX3, ALX4 and 110 more) → AHRR | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | AHRR → hypertensive disorder: association | tied for first |
| 1= | G265 (NKRF) → PDCD6 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | PDCD6 → hypertensive disorder: association | tied for first |
| 1= | G265 (NKRF) → AHRR | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | AHRR → hypertensive disorder: association | tied for first |

679 more chains not shown. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 8 tied for first: G051 (TCF12, TCF3, TCF4) → PDCD6. The run stated 6 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G051 (TCF12, TCF3, TCF4) | nothing found | supports: 1 (prediction) | nothing found (a search for the variant's names listed no article) |
| TF binding | The parts are in place | G051 (TCF12, TCF3, TCF4) | supports: 1 (occupancy) | no source | nothing found (a search for the variant's names listed no article) |
| Regulatory activity | The alleles differ | ENSR5\_C5GP (not stated by the run) | nothing found | no source | nothing found (a search for the variant's names listed no article) |
| Regulatory activity | The parts are in place | ENSR5\_C5GP | supports: 1 (annotation) | no source | nothing found (a search for the variant's names listed no article) |
| Target gene | The alleles differ | PDCD6 | supports: 2 (association) | no source | nothing found (a search for the variant's names listed no article) |
| Target gene | The parts are in place | PDCD6 (not stated by the run) | nothing found | no source | nothing found (a search for the variant's names listed no article) |
| Trait | The alleles differ | hypertensive disorder | supports: 1 (association) | no source | nothing found (a search for the variant's names listed no article) |
| Trait | The parts are in place | PDCD6 → hypertensive disorder | supports: 2 (association) | nothing found | nothing found (a search for the variant's names listed no article) |

Literature: a search for the variant's names listed no article.

Second reading: no experiment from an article was up for counting, so the critic read none.

The table passes every rule of docs/chain-table.md.

## Outcome

**Partial mechanism**; stopped because converged.

8 chains tie for first: G051 (TCF12, TCF3, TCF4), G335 (SNAI2), G001 (ALX1, ALX3, ALX4 and 110 more) or G265 (NKRF) → PDCD6 or AHRR. They differ in the transcription factor and the target gene and the gene to trait link. Association only: target gene, gene to trait, variant to trait. Predicted only: TF binding. No claim: regulatory activity. Filled by code from databases and model predictions. A search found no article that names the variant, so none was read. No experiment on file names one of the tied candidates beyond the records the table counts, so nothing read from the articles

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
