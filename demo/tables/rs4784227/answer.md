# v2m run report: GRCh38 chr16:52565276 C&gt;T

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (27 tool calls); a model was called only to read articles (18 model calls), so no hypothesis was proposed.

Case REQ-9a2766479625 · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs4784227 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E3180851 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**6 chains tie for first: G022 (FOXA1, FOXA2, FOXA3 and 3 more) or G002 (ESR1, ESR2, ESRRA and 35 more) → TOX3, ENSG00000285800 or RBL2. They differ in the transcription factor and the target gene and the gene to trait link.**

Reading the tie. A second model read the experiments that no cell of the table counts (2 experiments on 1 tied candidate, asked twice with the candidates in opposite orders and kept only where both readings agree; each time it also had to turn down a made-up candidate): no answer that is kept ties a tied candidate to this variant's site, so the tie stands as it is.

Measured: TF binding. Association only: target gene, gene to trait, variant to trait. No claim: regulatory activity.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G022 (FOXA1, FOXA2, FOXA3 and 3 more), G002 (ESR1, ESR2, ESRRA and 35 more) (tied) | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX: G022 (FOXA1, FOXA2, FOXA3 and 3 more), predicts more binding to T; G002 (ESR1, ESR2, ESRRA and 35 more), predicts more binding to C or T; in place: a ChIP-seq peak over the variant |
| Regulatory activity | – | no claim |
| Target gene | TOX3, ENSG00000285800, RBL2 (tied) | association |
| Gene to trait | TOX3 → estrogen-receptor positive breast cancer and 40 more | association |
| Variant to trait | brain volume and 27 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | G022 (FOXA1, FOXA2, FOXA3 and 3 more) → TOX3 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to T; in place: a ChIP-seq peak over the variant | association | TOX3 → estrogen-receptor positive breast cancer, TOX3 → mean arterial pressure, TOX3 → systolic blood pressure, and 11 more (tied): association | tied for first |
| 1= | G022 (FOXA1, FOXA2, FOXA3 and 3 more) → ENSG00000285800 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to T; in place: a ChIP-seq peak over the variant | association | ENSG00000285800 → brain volume, ENSG00000285800 → estrogen-receptor positive breast cancer, ENSG00000285800 → mean arterial pressure, and 23 more (tied): association | tied for first |
| 1= | G022 (FOXA1, FOXA2, FOXA3 and 3 more) → RBL2 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to T; in place: a ChIP-seq peak over the variant | association | RBL2 → systolic blood pressure: association | tied for first |
| 1= | G002 (ESR1, ESR2, ESRRA and 35 more) → TOX3 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to C or T; in place: a ChIP-seq peak over the variant | association | TOX3 → estrogen-receptor positive breast cancer, TOX3 → mean arterial pressure, TOX3 → systolic blood pressure, and 11 more (tied): association | tied for first |
| 1= | G002 (ESR1, ESR2, ESRRA and 35 more) → ENSG00000285800 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to C or T; in place: a ChIP-seq peak over the variant | association | ENSG00000285800 → brain volume, ENSG00000285800 → estrogen-receptor positive breast cancer, ENSG00000285800 → mean arterial pressure, and 23 more (tied): association | tied for first |
| 1= | G002 (ESR1, ESR2, ESRRA and 35 more) → RBL2 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to C or T; in place: a ChIP-seq peak over the variant | association | RBL2 → systolic blood pressure: association | tied for first |
| 7= | GROUCHO/TLE → TOX3 | allele-resolved assay; QBiC-SELEX: no model for it; in place: a ChIP-seq peak over the variant | association | TOX3 → estrogen-receptor positive breast cancer, TOX3 → mean arterial pressure, TOX3 → systolic blood pressure, and 11 more (tied): association | weaker on TF binding (no QBiC-SELEX prediction in support) |
| 7= | GROUCHO/TLE → ENSG00000285800 | allele-resolved assay; QBiC-SELEX: no model for it; in place: a ChIP-seq peak over the variant | association | ENSG00000285800 → brain volume, ENSG00000285800 → estrogen-receptor positive breast cancer, ENSG00000285800 → mean arterial pressure, and 23 more (tied): association | weaker on TF binding (no QBiC-SELEX prediction in support) |

514 more chains not shown, 1 of them tied at rank 7. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 6 tied for first: G022 (FOXA1, FOXA2, FOXA3 and 3 more) → TOX3. The run stated 6 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G022 (FOXA1, FOXA2, FOXA3 and 3 more) | supports: 1 (assay) | supports: 3 (prediction) | supports: 1 (assay) |
| TF binding | The parts are in place | G022 (FOXA1, FOXA2, FOXA3 and 3 more) | supports: 139 (occupancy) | no source | supports: 1 (occupancy) |
| Regulatory activity | The alleles differ | ENSR16\_9QTBS; EH38E3180851 (not stated by the run) | nothing found | no source | nothing found (11 of 18 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 21 of the 25 experiments it returned did not pass code's checks) |
| Regulatory activity | The parts are in place | ENSR16\_9QTBS; EH38E3180851 | supports: 2 (annotation) | no source | nothing found (11 of 18 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 21 of the 25 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | TOX3 | supports: 28 (association) | no source | supports: 1 (association) |
| Target gene | The parts are in place | TOX3 (not stated by the run) | nothing found | no source | nothing found (11 of 18 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 21 of the 25 experiments it returned did not pass code's checks); 2 set aside |
| Trait | The alleles differ | brain volume; estrogen-receptor positive breast cancer; mean arterial pressure and 25 more | supports: 108 (association) | no source | nothing found (11 of 18 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 21 of the 25 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | TOX3 → estrogen-receptor positive breast cancer; TOX3 → mean arterial pressure; TOX3 → systolic blood pressure and 24 more | supports: 28 (association) | supports: 74 (prediction) | nothing found (11 of 18 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 21 of the 25 experiments it returned did not pass code's checks); 1 beside; 1 set aside |

Literature: 18 articles naming the variant were found and 11 read, each once, by a model that returned 25 experiments; 4 passed code's checks against the text and were filed as records. Of the rest, 7 were reviews.

Second reading: a second model, from another provider, read 4 of the 4 experiments that are the only record behind a cell, each with its paragraph and the claims it counts for (code counts 4 in all, and an answer on any other could not change a cell). Of 6 claims checked it found 6 shown, 0 not shown and could not tell for 0. A record is not counted for a claim it found not shown; it can add nothing.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Database | ADASTRA, ChIP-seq reads counted by allele | 1 | FOXA1: reads favour T; FDR 0.044; effect size 0.92; 262 experiments |
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 3 | group G007 (Forkhead); more binding to T; \|z\| 17.1; p 6.8e-66; 6 of 10 models past the gate; not in the top 10% for this group / group G022 (Forkhead); more binding to T; \|z\| 15.4; p 1.6e-53; 2 of 4 models past the gate; not in the top 10% for this group / and 1 more record |
| TF binding: the alleles differ | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:23001124); the report quotes the sentences |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 139 | a peak over the variant in 139 experiments; TFs: FOXA1, FOXA2, FOXA3; cell types: HepG2, A-549, A549, MCF-7 and 19 more; summits 1 to 271 bp from the variant |
| TF binding: the parts are in place | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:23001124); the report quotes the sentences |
| Regulatory activity: the parts are in place | Database | Ensembl annotation | 1 | regulatory region variant |
| Regulatory activity: the parts are in place | Database | ENCODE registry of regulatory elements | 1 | EH38E3180851; distal enhancer-like (dELS) |
| Target gene: the alleles differ | Database | Open Targets colocalisations | 28 | probability of one shared causal variant (H4) 0.94 to 0.99; COLOC\_PIP\_ECAVIAR |
| Target gene: the alleles differ | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:23001124); the report quotes the sentences |
| Trait: the alleles differ | Database | Open Targets credible sets | 74 | fine-mapping probability 0.00031 to 1; in the 95% credible set in 74 of 74; SuSiE-inf, SuSie, PICS |
| Trait: the alleles differ | Database | GWAS Catalog | 34 | p 2.0e-240 to 7.0e-06 |
| Trait: the parts are in place | Database | Open Targets colocalisations | 28 | probability of one shared causal variant (H4) 0.94 to 0.99; COLOC\_PIP\_ECAVIAR |
| Trait: the parts are in place | Model prediction | Open Targets locus-to-gene score | 74 | score 0.77 to 0.96 |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **The tie for first** (6 chains). Experiment: The tied chains differ in the transcription factor: G022 (FOXA1, FOXA2, FOXA3 and 3 more), G002 (ESR1, ESR2, ESRRA and 35 more). They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: a measurement of the alleles' binding where there is only a prediction.
- **The tie for first** (6 chains). Experiment: The tied chains differ in the target gene: TOX3, ENSG00000285800, RBL2. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: the allele edited in the genome, with the RNA of each gene read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Experiment: Compare the regulatory activity of the two alleles: a reporter assay with both, or the allele edited in the genome with accessibility or enhancer marks read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Model run: No model in this version predicts the alleles' regulatory activity. A sequence-to-activity model would give this cell a prediction.
- **Target gene: the parts are in place** (nothing supports it). Experiment: Silence or delete the element (ENSR16\_9QTBS, EH38E3180851) and read out the RNA of TOX3, ENSG00000285800, RBL2.
- **Target gene: the alleles differ** (associated only). Experiment: Edit the allele in the genome and read out the RNA of TOX3, ENSG00000285800, RBL2. An association cannot separate this variant from the variants inherited with it.

## Outcome

**Partial mechanism**; stopped because converged.

6 chains tie for first: G022 (FOXA1, FOXA2, FOXA3 and 3 more) or G002 (ESR1, ESR2, ESRRA and 35 more) → TOX3, ENSG00000285800 or RBL2. They differ in the transcription factor and the target gene and the gene to trait link. Measured: TF binding. Association only: target gene, gene to trait, variant to trait. No claim: regulatory activity. Filled by code from databases and model predictions, and from 11 of 18 article(s) found that name the variant, each read once by a model: 4 experiment(s) were filed as records. A second model, from another provider, read 4 of the 4 experiment(s) that are the

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
