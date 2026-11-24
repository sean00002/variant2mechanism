# v2m run report: GRCh38 chr5:1295113 G&gt;A

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (17 tool calls); a model was called only to read articles (3 model calls), so no hypothesis was proposed.

Case REQ-9b6f5f51abae · Cache-only run · origin somatic · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs1242535815 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E3622530 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**8 chains tie for first: G032 (ZIC1, ZIC2, ZIC3 and 2 more), G161 (CTCF), G410 (ZBTB7A) or 5 more → no target gene named. They differ only in the transcription factor.**

Reading the tie. No experiment on file names one of the tied candidates beyond the records the table counts, so nothing read from the articles separates the tied chains.

Predicted only: TF binding. No claim: regulatory activity, target gene, gene to trait, variant to trait.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G032 (ZIC1, ZIC2, ZIC3 and 2 more), G161 (CTCF), G410 (ZBTB7A), G003 (EHF, ELF1, ELF2 and 22 more), and 4 more (tied) | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | – | no claim |
| Target gene | – | no claim |
| Gene to trait | – | no claim |
| Variant to trait | – | no claim |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | G032 (ZIC1, ZIC2, ZIC3 and 2 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G161 (CTCF) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G410 (ZBTB7A) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G003 (EHF, ELF1, ELF2 and 22 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G020 (EHF, ELF1, ELF2 and 8 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G345 (ELF1, ELF2, ELF4 and 1 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G049 (ELF5, ETV7, SPI1 and 2 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G329 (SKI) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |

222 more chains not shown. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 8 tied for first: G032 (ZIC1, ZIC2, ZIC3 and 2 more) → no target gene named. The run stated 3 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G032 (ZIC1, ZIC2, ZIC3 and 2 more) | nothing found | supports: 1 (prediction) | nothing found (3 of 4 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 4 of the 4 experiments it returned did not pass code's checks) |
| TF binding | The parts are in place | G032 (ZIC1, ZIC2, ZIC3 and 2 more) | supports: 1 (occupancy) | no source | nothing found (3 of 4 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 4 of the 4 experiments it returned did not pass code's checks) |
| Regulatory activity | The alleles differ | ENSR5\_832QG; EH38E3622530 (not stated by the run) | nothing found | no source | nothing found (3 of 4 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 4 of the 4 experiments it returned did not pass code's checks) |
| Regulatory activity | The parts are in place | ENSR5\_832QG; EH38E3622530 | supports: 2 (annotation) | no source | nothing found (3 of 4 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 4 of the 4 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | no gene named (not stated by the run) | nothing found | no source | nothing found (3 of 4 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 4 of the 4 experiments it returned did not pass code's checks) |
| Target gene | The parts are in place | no gene named (not stated by the run) | nothing found | no source | nothing found (3 of 4 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 4 of the 4 experiments it returned did not pass code's checks) |
| Trait | The alleles differ | no trait named (not stated by the run) | nothing found | no source | nothing found (3 of 4 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 4 of the 4 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | no gene named → no trait named (not stated by the run) | nothing found | nothing found | nothing found (3 of 4 articles found were read by the model; 1 not looked into (a review, no text, a failed call or the cap); 4 of the 4 experiments it returned did not pass code's checks) |

Literature: 4 articles naming the variant were found and 3 read, each once, by a model that returned 4 experiments; 0 passed code's checks against the text and were filed as records. Of the rest, 1 were reviews.

Second reading: no experiment from an article was up for counting, so the critic read none.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 1 | group G032 (C2H2 ZF); more binding to G; \|z\| 20.8; p 1.6e-96; 3 of 4 models past the gate; in the top 10% for this group |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 1 | a peak over the variant in 1 experiment; TFs: ZIC2; cell types: HEK293 |
| Regulatory activity: the parts are in place | Database | Ensembl annotation | 1 | regulatory region variant |
| Regulatory activity: the parts are in place | Database | ENCODE registry of regulatory elements | 1 | EH38E3622530; promoter-like (PLS) |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **The tie for first** (8 chains). Experiment: The tied chains differ in the transcription factor: G032 (ZIC1, ZIC2, ZIC3 and 2 more), G161 (CTCF), G410 (ZBTB7A) and 5 more. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: a measurement of the alleles' binding where there is only a prediction.
- **Regulatory activity: the alleles differ** (nothing supports it). Experiment: Compare the regulatory activity of the two alleles: a reporter assay with both, or the allele edited in the genome with accessibility or enhancer marks read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Model run: No model in this version predicts the alleles' regulatory activity. A sequence-to-activity model would give this cell a prediction.
- **Target gene: the alleles differ** (nothing supports it). Experiment: No source names a gene whose RNA differs between the alleles. An eQTL cannot exist for a somatic mutation. The allele edited in the genome, or tumours with and without the mutation compared, with the RNA of nearby genes read out, would name one.
- **Trait: the alleles differ** (nothing supports it). Source: The sources this run reads hold inherited variants, not somatic mutations. How often the mutation recurs in tumours, by cancer type, would be the matching record, and no such source is connected yet.
- **TF binding: the alleles differ** (predicted only). Experiment: Compare the binding of each of the tied transcription factors to the G and A alleles directly: a binding assay with both alleles, or ChIP reads counted by allele in cells that carry both.

## Outcome

**Partial mechanism**; stopped because converged.

8 chains tie for first: G032 (ZIC1, ZIC2, ZIC3 and 2 more), G161 (CTCF), G410 (ZBTB7A) or 5 more → no target gene named. They differ only in the transcription factor. Predicted only: TF binding. No claim: regulatory activity, target gene, gene to trait, variant to trait. Filled by code from databases and model predictions, and from 3 of 4 article(s) found that name the variant, each read once by a model: 0 experiment(s) were filed as records. No experiment on file names one of the tied candidates beyond the records the table counts, so nothing read from the articles separates the tied chains.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
