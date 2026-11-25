# v2m run report: GRCh38 chr8:127401060 G&gt;T

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (37 tool calls); a model was called only to read articles (16 model calls), so no hypothesis was proposed.

Case REQ-1c2bf76164ac · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs6983267 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E3858447 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**Leading chain: G041 (LEF1, TCF7, TCF7L1 and 1 more) → CCAT2.**

Measured: TF binding, regulatory activity, gene to trait. Association only: target gene, variant to trait.

**Joined.** 1 experiment(s) read from articles changed this chain's TF and saw its gene change (PMID:23796952), which puts it before 1 chain(s) that are otherwise its equal.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G041 (LEF1, TCF7, TCF7L1 and 1 more) | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; in place: a ChIP-seq peak over the variant |
| Regulatory activity | EH38E3858447 and 1 more | allele-resolved assay |
| Target gene | CCAT2 | association |
| Gene to trait | CCAT2 → tumor growth | edit or perturbation |
| Variant to trait | colorectal carcinoma and 37 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1 | G041 (LEF1, TCF7, TCF7L1 and 1 more) → CCAT2 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; in place: a ChIP-seq peak over the variant | association | CCAT2 → tumor growth: edit or perturbation | leads |
| 2 | G022 (FOXA1, FOXA2, FOXA3 and 3 more) → CCAT2 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; in place: a ChIP-seq peak over the variant | association | CCAT2 → tumor growth: edit or perturbation | the same kinds of evidence on every link |
| 3= | G022 (FOXA1, FOXA2, FOXA3 and 3 more) → CASC8 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; in place: a ChIP-seq peak over the variant | association | CASC8 → benign prostatic hyperplasia: association | weaker on gene to trait |
| 3= | G041 (LEF1, TCF7, TCF7L1 and 1 more) → CASC8 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; in place: a ChIP-seq peak over the variant | association | CASC8 → benign prostatic hyperplasia: association | weaker on gene to trait |
| 5= | G220 (KDM5B) → CCAT2 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | CCAT2 → tumor growth: edit or perturbation | weaker on TF binding |
| 5= | G071 (GFI1, GFI1B) → CCAT2 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | CCAT2 → tumor growth: edit or perturbation | weaker on TF binding |
| 5= | G549 (ZNF609) → CCAT2 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | CCAT2 → tumor growth: edit or perturbation | weaker on TF binding |
| 5= | G188 (GATAD2B) → CCAT2 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | CCAT2 → tumor growth: edit or perturbation | weaker on TF binding |

1384 more chains not shown, 5 of them tied at rank 5. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next. Last, a chain pairs a TF with a gene, and nothing above says the two belong together. Where an experiment read from an article changed the chain's TF and saw its gene's RNA or protein change, the chain comes before an otherwise equal one with no such record. That record shows the TF acting on the gene, not that it does so through this variant, so it only ever breaks a tie.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain: G041 (LEF1, TCF7, TCF7L1 and 1 more) → CCAT2. The run stated 7 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G041 (LEF1, TCF7, TCF7L1 and 1 more) | nothing found | supports: 1 (prediction) | supports: 1 (assay) |
| TF binding | The parts are in place | G041 (LEF1, TCF7, TCF7L1 and 1 more) | supports: 8 (occupancy) | no source | supports: 2 (occupancy) |
| Regulatory activity | The alleles differ | EH38E3858447; 8q24 CRC risk region | supports: 1 (assay) | no source | supports: 1 (assay); 1 set aside |
| Regulatory activity | The parts are in place | ENSR8\_CGMBX; EH38E3858447 | supports: 2 (annotation) | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 13 of the 35 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | CCAT2 | nothing found | no source | supports: 2 (association); 1 set aside |
| Target gene | The parts are in place | CCAT2 (not stated by the run) | nothing found | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 13 of the 35 experiments it returned did not pass code's checks); 15 set aside |
| Trait | The alleles differ | colorectal carcinoma; benign colon neoplasm; benign prostatic hyperplasia and 35 more | supports: 144 (association) | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 13 of the 35 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | CCAT2 → tumor growth; CCAT2 → liver metastasis | nothing found | nothing found | supports: 1 (edit); 1 beside; 9 set aside |

Literature: 19 articles naming the variant were found and 14 read, each once, by a model that returned 35 experiments; 22 passed code's checks against the text and were filed as records. Of the rest, 2 did not name the variant in the text retrieved, 3 were reviews.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 1 | group G041 (HMG/Sox); more binding to G; \|z\| 4.7; p 3.2e-06; 2 of 3 models past the gate; not in the top 10% for this group |
| TF binding: the alleles differ | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:19561607); the report quotes the sentences |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 8 | a peak over the variant in 8 experiments; TFs: TCF7, TCF7L2; cell types: HepG2, HCT116, HCT-116, LNCaP; summits 7 to 22 bp from the variant |
| TF binding: the parts are in place | Literature | Articles read by the model | 2 | 2 experiments in 1 article (PMID:19561607); the report quotes the sentences |
| Regulatory activity: the alleles differ | Database | ADASTRA, ChIP-seq reads counted by allele | 1 | CTNNB1: reads favour G; FDR 0.038; effect size 2.13; 19 experiments |
| Regulatory activity: the alleles differ | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:19561607); the report quotes the sentences |
| Regulatory activity: the parts are in place | Database | Ensembl annotation | 1 | regulatory region variant |
| Regulatory activity: the parts are in place | Database | ENCODE registry of regulatory elements | 1 | EH38E3858447; proximal enhancer-like (pELS) |
| Target gene: the alleles differ | Literature | Articles read by the model | 2 | 2 experiments in 1 article (PMID:23796952); the report quotes the sentences |
| Trait: the alleles differ | Database | Open Targets credible sets | 75 | fine-mapping probability 0.025 to 1; in the 95% credible set in 75 of 75; PICS, SuSiE-inf, SuSie |
| Trait: the alleles differ | Database | GWAS Catalog | 69 | p below 1e-300 to 9.0e-06 |
| Trait: the parts are in place | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:23796952); the report quotes the sentences |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **Target gene: the parts are in place** (nothing supports it). Experiment: Silence or delete the element (ENSR8\_CGMBX, EH38E3858447) and read out the RNA of CCAT2.
- **Target gene: the alleles differ** (associated only). Experiment: Edit the allele in the genome and read out the RNA of CCAT2. An association cannot separate this variant from the variants inherited with it.

## Outcome

**Leading explanation**; stopped because converged.

Leading chain: G041 (LEF1, TCF7, TCF7L1 and 1 more) → CCAT2. Measured: TF binding, regulatory activity, gene to trait. Association only: target gene, variant to trait. 1 experiment(s) read from articles changed this chain's TF and saw its gene change (PMID:23796952), which puts it before 1 chain(s) that are otherwise its equal. Filled by code from databases and model predictions, and from 14 of 19 article(s) found that name the variant, each read once by a model: 22 experiment(s) were filed as records.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
