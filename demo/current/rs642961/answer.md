# v2m run report: GRCh38 chr1:209815925 A&gt;G

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (39 tool calls); a model was called only to read articles (15 model calls), so no hypothesis was proposed.

Case REQ-45ce1e858e9c · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs642961 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E2863563 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**4 chains tie for first: G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → UTP25, IRF6, SYT14 or TRAF3IP3. They differ in the target gene and the gene to trait link.**

Measured: TF binding. Association only: target gene, gene to trait, variant to trait. No claim: regulatory activity.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | – | no claim |
| Target gene | UTP25, IRF6, SYT14, TRAF3IP3 (tied) | association |
| Gene to trait | UTP25 → systolic blood pressure and 10 more | association |
| Variant to trait | systolic blood pressure and 7 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → UTP25 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | UTP25 → systolic blood pressure, UTP25 → hematological measurement, UTP25 → mean arterial pressure (tied): association | tied for first |
| 1= | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → IRF6 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | IRF6 → systolic blood pressure, IRF6 → cleft lip (tied): association | tied for first |
| 1= | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → SYT14 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SYT14 → systolic blood pressure, SYT14 → mean arterial pressure (tied): association | tied for first |
| 1= | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → TRAF3IP3 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | TRAF3IP3 → systolic blood pressure, TRAF3IP3 → hematological measurement, TRAF3IP3 → mean arterial pressure, and 1 more (tied): association | tied for first |
| 5 | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → C1ORF74 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to G; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | C1ORF74 → systolic blood pressure, C1ORF74 → hematological measurement, C1ORF74 → orofacial cleft (tied): predicted | weaker on gene to trait |
| 6= | G105 (ZNF143, ZNF76) → UTP25 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | UTP25 → systolic blood pressure, UTP25 → hematological measurement, UTP25 → mean arterial pressure (tied): association | weaker on TF binding |
| 6= | G105 (ZNF143, ZNF76) → IRF6 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | IRF6 → systolic blood pressure, IRF6 → cleft lip (tied): association | weaker on TF binding |
| 6= | G105 (ZNF143, ZNF76) → SYT14 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | SYT14 → systolic blood pressure, SYT14 → mean arterial pressure (tied): association | weaker on TF binding |

692 more chains not shown, 13 of them tied at rank 6. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 4 tied for first: G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → UTP25. The run stated 6 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) | nothing found | supports: 1 (prediction) | supports: 1 (assay) |
| TF binding | The parts are in place | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) | supports: 2 (occupancy) | no source | supports: 1 (occupancy) |
| Regulatory activity | The alleles differ | ENSR1\_B3JM9C; EH38E2863563 (not stated by the run) | nothing found | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks); 2 set aside |
| Regulatory activity | The parts are in place | ENSR1\_B3JM9C; EH38E2863563 | supports: 2 (annotation) | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | UTP25 | supports: 44 (association) | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |
| Target gene | The parts are in place | UTP25 (not stated by the run) | nothing found | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |
| Trait | The alleles differ | systolic blood pressure; hematological measurement; mean arterial pressure and 5 more | supports: 22 (association) | no source | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | UTP25 → systolic blood pressure; UTP25 → hematological measurement; UTP25 → mean arterial pressure and 1 more | supports: 28 (association) | supports: 14 (prediction) | nothing found (14 of 19 articles found were read by the model; 3 not looked into (a review, no text, a failed call or the cap); 4 of the 10 experiments it returned did not pass code's checks) |

Literature: 19 articles naming the variant were found and 14 read, each once, by a model that returned 10 experiments; 6 passed code's checks against the text and were filed as records. Of the rest, 2 did not name the variant in the text retrieved, 3 were reviews.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 1 | group G030 (AP-2); more binding to G; \|z\| 24.0; p 4.3e-127; 4 of 4 models past the gate; in the top 10% for this group |
| TF binding: the alleles differ | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:18836445); the report quotes the sentences |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 2 | a peak over the variant in 2 experiments; TFs: TFAP2C; cell types: UCLA1-hESCs, HCC1954; summits 27 to 690 bp from the variant |
| TF binding: the parts are in place | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:18836445); the report quotes the sentences |
| Regulatory activity: the parts are in place | Database | Ensembl annotation | 1 | regulatory region variant |
| Regulatory activity: the parts are in place | Database | ENCODE registry of regulatory elements | 1 | EH38E2863563; distal enhancer-like (dELS) |
| Target gene: the alleles differ | Database | SCREEN eQTL links | 8 | effect size -0.23 to +0.35 for G; p 3.5e-31 to 6.6e-06; tissues: Adipose Subcutaneous, Adipose Visceral Omentum, Artery Tibial, Brain Cortex and 4 more |
| Target gene: the alleles differ | Database | GTEx eQTL | 8 | effect size -0.23 to +0.35 for G; p 1.9e-14 to 2.5e-05; tissues: Adipose Subcutaneous, Adipose Visceral Omentum, Artery Tibial, Brain Cortex and 4 more |
| Target gene: the alleles differ | Database | Open Targets colocalisations | 28 | probability of one shared causal variant (H4) 0.20 to 0.97; COLOC\_PIP\_ECAVIAR |
| Trait: the alleles differ | Database | Open Targets credible sets | 14 | fine-mapping probability 0.0089 to 0.1; in the 95% credible set in 14 of 14; SuSiE-inf, PICS |
| Trait: the alleles differ | Database | GWAS Catalog | 8 | p 6.0e-12 to 2.0e-06 |
| Trait: the parts are in place | Database | Open Targets colocalisations | 28 | probability of one shared causal variant (H4) 0.20 to 0.97; COLOC\_PIP\_ECAVIAR |
| Trait: the parts are in place | Model prediction | Open Targets locus-to-gene score | 14 | score 0.07 to 0.75 |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **The tie for first** (4 chains). Experiment: The tied chains differ in the target gene: UTP25, IRF6, SYT14 and 1 more. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: the allele edited in the genome, with the RNA of each gene read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Experiment: Compare the regulatory activity of the two alleles: a reporter assay with both, or the allele edited in the genome with accessibility or enhancer marks read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Model run: No model in this version predicts the alleles' regulatory activity. A sequence-to-activity model would give this cell a prediction.
- **Target gene: the parts are in place** (nothing supports it). Experiment: Silence or delete the element (ENSR1\_B3JM9C, EH38E2863563) and read out the RNA of UTP25, IRF6, SYT14, TRAF3IP3.
- **Target gene: the alleles differ** (associated only). Experiment: Edit the allele in the genome and read out the RNA of UTP25, IRF6, SYT14, TRAF3IP3. An association cannot separate this variant from the variants inherited with it.

## Outcome

**Partial mechanism**; stopped because converged.

4 chains tie for first: G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → UTP25, IRF6, SYT14 or TRAF3IP3. They differ in the target gene and the gene to trait link. Measured: TF binding. Association only: target gene, gene to trait, variant to trait. No claim: regulatory activity. Filled by code from databases and model predictions, and from 14 of 19 article(s) found that name the variant, each read once by a model: 6 experiment(s) were filed as records.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
