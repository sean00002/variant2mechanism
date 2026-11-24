# v2m run report: GRCh38 chr11:8233861 C&gt;A

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (26 tool calls); a model was called only to read articles (11 model calls), so no hypothesis was proposed.

Case REQ-d88069fdc35c · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs2168101 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E1518342 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**Leading chain: G010 (GATA1, GATA2, GATA3 and 3 more) → LMO1.**

Measured: TF binding, regulatory activity. Association only: target gene, gene to trait, variant to trait.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G010 (GATA1, GATA2, GATA3 and 3 more) | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to C; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | EH38E1518342 | allele-resolved assay |
| Target gene | LMO1 | association |
| Gene to trait | LMO1 → body height and 5 more | association |
| Variant to trait | calcium measurement and 36 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1 | G010 (GATA1, GATA2, GATA3 and 3 more) → LMO1 | allele-resolved assay + QBiC-SELEX prediction; QBiC-SELEX predicts more binding to C; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | LMO1 → body height, LMO1 → HbA1c measurement, LMO1 → serum albumin amount, and 3 more (tied): association | leads |
| 2= | G618 (ZNF8) → LMO1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | LMO1 → body height, LMO1 → HbA1c measurement, LMO1 → serum albumin amount, and 3 more (tied): association | weaker on TF binding |
| 2= | G007 (FOXC1, FOXC2, FOXD1 and 25 more) → LMO1 | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | association | LMO1 → body height, LMO1 → HbA1c measurement, LMO1 → serum albumin amount, and 3 more (tied): association | weaker on TF binding |
| 4= | G228 (MAX) → LMO1 | predicted by QBiC-SELEX; in place: a ChIP-seq peak over the variant | association | LMO1 → body height, LMO1 → HbA1c measurement, LMO1 → serum albumin amount, and 3 more (tied): association | weaker on TF binding |
| 4= | G035 (CEBPA, CEBPB, CEBPE) → LMO1 | predicted by QBiC-SELEX; in place: a ChIP-seq peak over the variant | association | LMO1 → body height, LMO1 → HbA1c measurement, LMO1 → serum albumin amount, and 3 more (tied): association | weaker on TF binding |
| 4= | G040 (JUN, JUNB, JUND) → LMO1 | predicted by QBiC-SELEX; in place: a ChIP-seq peak over the variant | association | LMO1 → body height, LMO1 → HbA1c measurement, LMO1 → serum albumin amount, and 3 more (tied): association | weaker on TF binding |
| 4= | G015 (SP1, SP3, SP4 and 5 more) → LMO1 | predicted by QBiC-SELEX; in place: a ChIP-seq peak over the variant | association | LMO1 → body height, LMO1 → HbA1c measurement, LMO1 → serum albumin amount, and 3 more (tied): association | weaker on TF binding |
| 4= | G420 (ZFP3) → LMO1 | predicted by QBiC-SELEX; in place: a ChIP-seq peak over the variant | association | LMO1 → body height, LMO1 → HbA1c measurement, LMO1 → serum albumin amount, and 3 more (tied): association | weaker on TF binding |

673 more chains not shown, 11 of them tied at rank 4. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain: G010 (GATA1, GATA2, GATA3 and 3 more) → LMO1. The run stated 7 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G010 (GATA1, GATA2, GATA3 and 3 more) | nothing found | supports: 1 (prediction) | supports: 1 (assay) |
| TF binding | The parts are in place | G010 (GATA1, GATA2, GATA3 and 3 more) | supports: 24 (occupancy) | no source | supports: 3 (occupancy) |
| Regulatory activity | The alleles differ | EH38E1518342 | nothing found | no source | supports: 1 (assay); 1 set aside |
| Regulatory activity | The parts are in place | EH38E1518342 | supports: 1 (annotation) | no source | nothing found (8 of 19 articles found were read by the model; 9 not looked into (a review, no text, a failed call or the cap); 9 of the 18 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | LMO1 | supports: 15 (association) | no source | supports: 2 (association); 3 set aside |
| Target gene | The parts are in place | LMO1 (not stated by the run) | nothing found | no source | nothing found (8 of 19 articles found were read by the model; 9 not looked into (a review, no text, a failed call or the cap); 9 of the 18 experiments it returned did not pass code's checks); 5 set aside |
| Trait | The alleles differ | calcium measurement; glucose measurement; body height and 34 more | supports: 146 (association) | no source | nothing found (8 of 19 articles found were read by the model; 9 not looked into (a review, no text, a failed call or the cap); 9 of the 18 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | LMO1 → body height; LMO1 → HbA1c measurement; LMO1 → serum albumin amount and 28 more | supports: 13 (association) | supports: 75 (prediction) | nothing found (8 of 19 articles found were read by the model; 9 not looked into (a review, no text, a failed call or the cap); 9 of the 18 experiments it returned did not pass code's checks); 3 set aside |

Literature: 19 articles naming the variant were found and 8 read, each once, by a model that returned 18 experiments; 9 passed code's checks against the text and were filed as records. Of the rest, 2 did not name the variant in the text retrieved, 6 were reviews, 3 could not be retrieved.

Second reading: a second model, from another provider, read 2 of the 2 experiments that are the only record behind a cell, each with its paragraph and the claims it counts for (code counts 6 in all, and an answer on any other could not change a cell). Of 3 claims checked it found 3 shown, 0 not shown and could not tell for 0. A record is not counted for a claim it found not shown; it can add nothing.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 1 | group G010 (GATA); more binding to C; \|z\| 56.1; p below 1e-300; 6 of 6 models past the gate; in the top 10% for this group |
| TF binding: the alleles differ | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:26560027); the report quotes the sentences |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 24 | a peak over the variant in 24 experiments; TFs: GATA2, GATA3, GATA6; cell types: SH-SY5Y, SK-N-SH, ESF, primary-endometrial-stromal-cell and 11 more; summits 1 to 134 bp from the variant |
| TF binding: the parts are in place | Literature | Articles read by the model | 3 | 3 experiments in 2 articles (PMID:26560027, PMID:38653778); the report quotes the sentences |
| Regulatory activity: the alleles differ | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:26560027); the report quotes the sentences |
| Regulatory activity: the parts are in place | Database | ENCODE registry of regulatory elements | 1 | EH38E1518342; distal enhancer-like (dELS) |
| Target gene: the alleles differ | Database | SCREEN eQTL links | 1 | effect size -0.13 for A; p 1.7e-26; tissues: Muscle Skeletal |
| Target gene: the alleles differ | Database | GTEx eQTL | 1 | effect size -0.13 for A; p 1.6e-09; tissues: Muscle Skeletal |
| Target gene: the alleles differ | Database | Open Targets colocalisations | 13 | probability of one shared causal variant (H4) 0.83 to 1.00; COLOC\_PIP\_ECAVIAR |
| Target gene: the alleles differ | Literature | Articles read by the model | 2 | 2 experiments in 1 article (PMID:26560027); the report quotes the sentences |
| Trait: the alleles differ | Database | Open Targets credible sets | 75 | fine-mapping probability 0.019 to 1; in the 95% credible set in 75 of 75; SuSiE-inf, PICS |
| Trait: the alleles differ | Database | GWAS Catalog | 71 | p 2.0e-208 to 3.0e-08 |
| Trait: the parts are in place | Database | Open Targets colocalisations | 13 | probability of one shared causal variant (H4) 0.83 to 1.00; COLOC\_PIP\_ECAVIAR |
| Trait: the parts are in place | Model prediction | Open Targets locus-to-gene score | 75 | score 0.70 to 0.92 |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **Target gene: the parts are in place** (nothing supports it). Experiment: Silence or delete the element (EH38E1518342) and read out the RNA of LMO1.
- **Target gene: the alleles differ** (associated only). Experiment: Edit the allele in the genome and read out the RNA of LMO1. An association cannot separate this variant from the variants inherited with it.

## Outcome

**Leading explanation**; stopped because converged.

Leading chain: G010 (GATA1, GATA2, GATA3 and 3 more) → LMO1. Measured: TF binding, regulatory activity. Association only: target gene, gene to trait, variant to trait. Filled by code from databases and model predictions, and from 8 of 19 article(s) found that name the variant, each read once by a model: 9 experiment(s) were filed as records. A second model, from another provider, read 2 of the 2 experiment(s) that are the only record behind a cell (code counts 6 in all) against the claims they count for: of 3 claim(s) checked it found 0 not shown by the text, and those were not counted.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
