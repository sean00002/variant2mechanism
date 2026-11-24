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

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 1 | group G051 (bHLH); more binding to A; \|z\| 87.4; p below 1e-300; 3 of 3 models past the gate; in the top 10% for this group |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 1 | a peak over the variant in 1 experiment; TFs: TCF12; cell types: GM12878; summits 86 bp from the variant |
| Regulatory activity: the parts are in place | Database | Ensembl annotation | 1 | regulatory region variant |
| Target gene: the alleles differ | Database | Open Targets colocalisations | 2 | probability of one shared causal variant (H4) 0.01 to 0.19; COLOC\_PIP\_ECAVIAR |
| Trait: the alleles differ | Database | Open Targets credible sets | 1 | fine-mapping probability 0.00011; in the 95% credible set in 1 of 1; SuSie |
| Trait: the parts are in place | Database | Open Targets colocalisations | 2 | probability of one shared causal variant (H4) 0.01 to 0.19; COLOC\_PIP\_ECAVIAR |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **The tie for first** (8 chains). Experiment: The tied chains differ in the transcription factor: G051 (TCF12, TCF3, TCF4), G335 (SNAI2), G001 (ALX1, ALX3, ALX4 and 110 more) and 1 more. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: a measurement of the alleles' binding where there is only a prediction.
- **The tie for first** (8 chains). Experiment: The tied chains differ in the target gene: PDCD6, AHRR. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: the allele edited in the genome, with the RNA of each gene read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Experiment: Compare the regulatory activity of the two alleles: a reporter assay with both, or the allele edited in the genome with accessibility or enhancer marks read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Model run: No model in this version predicts the alleles' regulatory activity. A sequence-to-activity model would give this cell a prediction.
- **Target gene: the parts are in place** (nothing supports it). Experiment: Silence or delete the element (ENSR5\_C5GP) and read out the RNA of PDCD6, AHRR.
- **TF binding: the alleles differ** (predicted only). Experiment: Compare the binding of each of the tied transcription factors to the G and A alleles directly: a binding assay with both alleles, or ChIP reads counted by allele in cells that carry both.
- **Target gene: the alleles differ** (associated only). Experiment: Edit the allele in the genome and read out the RNA of PDCD6, AHRR. An association cannot separate this variant from the variants inherited with it.

## Outcome

**Partial mechanism**; stopped because converged.

8 chains tie for first: G051 (TCF12, TCF3, TCF4), G335 (SNAI2), G001 (ALX1, ALX3, ALX4 and 110 more) or G265 (NKRF) → PDCD6 or AHRR. They differ in the transcription factor and the target gene and the gene to trait link. Association only: target gene, gene to trait, variant to trait. Predicted only: TF binding. No claim: regulatory activity. Filled by code from databases and model predictions. A search found no article that names the variant, so none was read. No experiment on file names one of the tied candidates beyond the records the table counts, so nothing read from the articles

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
