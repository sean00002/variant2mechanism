# v2m run report: GRCh38 chr5:1295113 G&gt;A

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (39 tool calls); a model was called only to read articles (10 model calls), so no hypothesis was proposed.

Case REQ-9b6f5f51abae · Cache-only run · origin somatic · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs1242535815 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E3622530 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**Leading chain: ELF1 → no target gene named.**

Measured: TF binding, regulatory activity. Association only: variant to trait. No claim: target gene, gene to trait.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | ELF1 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to A; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | EH38E3622530 and 1 more | allele-resolved assay |
| Target gene | – | no claim |
| Gene to trait | – | no claim |
| Variant to trait | Glioma and 21 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1 | ELF1 → no target gene named | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to A; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | leads |
| 2 | G476 (ZNF281) → no target gene named | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G | no claim | no claim | the same kinds of evidence on every link; no strong prediction (a change in the top 10% for the TF group, with a ChIP-seq peak over the variant) |
| 3 | ZNF148 → no target gene named | allele-resolved assay; QBiC-SELEX: no model for it | no claim | no claim | weaker on TF binding (no QBiC-SELEX prediction in support) |
| 4= | G032 (ZIC1, ZIC2, ZIC3 and 2 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | weaker on TF binding |
| 4= | G161 (CTCF) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | weaker on TF binding |
| 4= | G410 (ZBTB7A) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | weaker on TF binding |
| 4= | G003 (EHF, ELF1, ELF2 and 22 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | weaker on TF binding |
| 4= | G020 (EHF, ELF1, ELF2 and 8 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | weaker on TF binding |

224 more chains not shown, 3 of them tied at rank 4. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain: ELF1 → no target gene named. The run stated 5 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | ELF1 | nothing found | supports: 3 (prediction) | supports: 1 (assay) |
| TF binding | The parts are in place | ELF1 | supports: 5 (occupancy) | no source | nothing found (9 of 14 articles found were read by the model; 4 not looked into (a review, no text, a failed call or the cap); 18 of the 32 experiments it returned did not pass code's checks) |
| Regulatory activity | The alleles differ | EH38E3622530; TERT promoter constructs containing upstream regulatory elements | supports: 4 (assay) | no source | supports: 2 (assay); 2 set aside |
| Regulatory activity | The parts are in place | ENSR5\_832QG; EH38E3622530 | supports: 2 (annotation) | no source | nothing found (9 of 14 articles found were read by the model; 4 not looked into (a review, no text, a failed call or the cap); 18 of the 32 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | no gene named (not stated by the run) | nothing found | no source | nothing found (9 of 14 articles found were read by the model; 4 not looked into (a review, no text, a failed call or the cap); 18 of the 32 experiments it returned did not pass code's checks); 10 set aside |
| Target gene | The parts are in place | no gene named (not stated by the run) | nothing found | no source | nothing found (9 of 14 articles found were read by the model; 4 not looked into (a review, no text, a failed call or the cap); 18 of the 32 experiments it returned did not pass code's checks); 3 set aside |
| Trait | The alleles differ | Glioma; Bladder Cancer; Thyroid Cancer and 19 more | supports: 22 (association) | no source | nothing found (9 of 14 articles found were read by the model; 4 not looked into (a review, no text, a failed call or the cap); 18 of the 32 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | no gene named → Glioma; Bladder Cancer; Thyroid Cancer and 19 more (not stated by the run) | nothing found | nothing found | nothing found (9 of 14 articles found were read by the model; 4 not looked into (a review, no text, a failed call or the cap); 18 of the 32 experiments it returned did not pass code's checks); 2 set aside |

Literature: 14 articles naming the variant were found and 9 read, each once, by a model that returned 32 experiments; 14 passed code's checks against the text and were filed as records. Of the rest, 1 did not name the variant in the text retrieved, 4 were reviews.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 3 | group G003 (Ets); more binding to A; \|z\| 166.2; p below 1e-300; 18 of 18 models past the gate; in the top 10% for this group / group G020 (Ets); more binding to A; \|z\| 70.1; p below 1e-300; 4 of 4 models past the gate; in the top 10% for this group / and 1 more record |
| TF binding: the alleles differ | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:37918959); the report quotes the sentences |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 5 | a peak over the variant in 5 experiments; TFs: ELF1; cell types: GM12878, Hep-G2, ME-1; summits 36 to 229 bp from the variant |
| Regulatory activity: the alleles differ | Database | MaveDB, saturation-mutagenesis reporter assays | 4 | log2 effect on reporter activity +1.99 to +2.90, as each set records it; p below 1e-300; 464 to 476 barcodes; cells, where a set names them: HEK293T; 4 score sets: 00000031-a-1, 00000031-b-1, 00000031-c-1, 00000031-d-1 |
| Regulatory activity: the alleles differ | Literature | Articles read by the model | 2 | 2 experiments in 1 article (PMID:34944589); the report quotes the sentences |
| Regulatory activity: the parts are in place | Database | Ensembl annotation | 1 | regulatory region variant |
| Regulatory activity: the parts are in place | Database | ENCODE registry of regulatory elements | 1 | EH38E3622530; promoter-like (PLS) |
| Trait: the alleles differ | Database | cBioPortal, tumours of the MSK-IMPACT 2017 cohort | 22 | called in the tumours of 257 of 514 patients with Glioma, 214 of 406 patients with Bladder Cancer, 123 of 226 patients with Thyroid Cancer, 72 of 350 patients with Melanoma and 18 more |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **Target gene: the alleles differ** (nothing supports it). Experiment: No source names a gene whose RNA differs between the alleles. An eQTL cannot exist for a somatic mutation. The allele edited in the genome, or tumours with and without the mutation compared, with the RNA of nearby genes read out, would name one.

## Outcome

**Partial mechanism**; stopped because converged.

Leading chain: ELF1 → no target gene named. Measured: TF binding, regulatory activity. Association only: variant to trait. No claim: target gene, gene to trait. Filled by code from databases and model predictions, and from 9 of 14 article(s) found that name the variant, each read once by a model: 14 experiment(s) were filed as records.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
