# v2m run report: GRCh38 chr3:12344838 C&gt;T

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (53 tool calls); a model was called only to read articles (13 model calls), so no hypothesis was proposed.

Case REQ-03d74ff1c164 · Live run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs4684847 (T1, variant\_annotation)
- Elements containing it, found by code: none recorded

## Answer: ranked mechanism chains

**4 chains tie for first: PRRX1 or ILF3 → PPARG or TIMP4. They differ in the transcription factor and the target gene and the gene to trait link.**

Measured: TF binding, regulatory activity. Association only: target gene, gene to trait, variant to trait.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | PRRX1, ILF3 (tied) | allele-resolved assay |
| Regulatory activity | the site of rs4684847 | allele-resolved assay |
| Target gene | PPARG, TIMP4 (tied) | association (blood plasma) |
| Gene to trait | PPARG → diabetes mellitus and 96 more | association |
| Variant to trait | diabetes mellitus and 61 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | PRRX1 → PPARG | allele-resolved assay | association | PPARG → diabetes mellitus, PPARG → body fat mass, PPARG → morbid obesity, and 53 more (tied): association | tied for first |
| 1= | PRRX1 → TIMP4 | allele-resolved assay | association (blood plasma) | TIMP4 → diabetes mellitus, TIMP4 → body fat mass, TIMP4 → cholesteryl esters in VLDL measurement, and 38 more (tied): association | tied for first |
| 1= | ILF3 → PPARG | allele-resolved assay | association | PPARG → diabetes mellitus, PPARG → body fat mass, PPARG → morbid obesity, and 53 more (tied): association | tied for first |
| 1= | ILF3 → TIMP4 | allele-resolved assay | association (blood plasma) | TIMP4 → diabetes mellitus, TIMP4 → body fat mass, TIMP4 → cholesteryl esters in VLDL measurement, and 38 more (tied): association | tied for first |
| 5 | PRRX1 → PPARG2 | allele-resolved assay | edit or perturbation | no claim | weaker on gene to trait; stronger on target gene |
| 6 | ILF3 → PPARG2 | allele-resolved assay | edit or perturbation | no claim | weaker on gene to trait; stronger on target gene |
| 7= | PRRX1 → SYN2 | allele-resolved assay | association | no claim | weaker on gene to trait |
| 7= | PRRX1 → FABP4 | allele-resolved assay | no claim | FABP4 → morbid obesity, FABP4 → calcium measurement, FABP4 → cholesterol to total lipids in medium VLDL percentage, and 15 more (tied): association | weaker on target gene |

4 more chains not shown, 4 of them tied at rank 7. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next. Last, a chain pairs a TF with a gene, and nothing above says the two belong together. Where an experiment read from an article changed the chain's TF and saw its gene's RNA or protein change, the chain comes before an otherwise equal one with no such record. That record shows the TF acting on the gene, not that it does so through this variant, so it only ever breaks a tie.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 4 tied for first: PRRX1 → PPARG. The run stated 5 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | PRRX1 | nothing found | not checked | supports: 3 (assay) |
| TF binding | The parts are in place | PRRX1 (not stated by the run) | nothing found | no source | nothing found (11 of 21 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 14 of the 31 experiments it returned did not pass code's checks) |
| Regulatory activity | The alleles differ | the site of rs4684847 | nothing found | no source | supports: 3 (assay); 8 set aside |
| Regulatory activity | The parts are in place | the variant's site (not stated by the run) | nothing found | no source | nothing found (11 of 21 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 14 of the 31 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | PPARG | supports: 140 (association) | no source | nothing found (11 of 21 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 14 of the 31 experiments it returned did not pass code's checks); 1 set aside |
| Target gene | The parts are in place | PPARG (not stated by the run) | nothing found | no source | nothing found (11 of 21 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 14 of the 31 experiments it returned did not pass code's checks); 1 set aside |
| Trait | The alleles differ | diabetes mellitus; body fat mass; morbid obesity and 59 more | supports: 87 (association) | no source | nothing found (11 of 21 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 14 of the 31 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | PPARG → diabetes mellitus; PPARG → body fat mass; PPARG → morbid obesity and 55 more | supports: 147 (association) | supports: 75 (prediction) | nothing found (11 of 21 articles found were read by the model; 7 not looked into (a review, no text, a failed call or the cap); 14 of the 31 experiments it returned did not pass code's checks); 1 set aside |

Literature: 21 articles naming the variant were found and 11 read, each once, by a model that returned 31 experiments; 17 passed code's checks against the text and were filed as records. Of the rest, 3 did not name the variant in the text retrieved, 4 were reviews, 3 were beyond the cap.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Literature | Articles read by the model | 3 | 3 experiments in 2 articles (PMID:24439387, PMID:28334807); the report quotes the sentences |
| Regulatory activity: the alleles differ | Literature | Articles read by the model | 3 | 3 experiments in 1 article (PMID:24439387); the report quotes the sentences |
| Target gene: the alleles differ | Database | GTEx eQTL | 4 | effect size +0.22 to +0.69 for T; p 6.6e-07 to 7.6e-05; tissues: Cells EBV-transformed lymphocytes, Esophagus Gastroesophageal Junction, Esophagus Mucosa, Esophagus Muscularis |
| Target gene: the alleles differ | Database | Open Targets colocalisations | 136 | probability of one shared causal variant (H4) 0.24 to 0.99; COLOC\_PIP\_ECAVIAR |
| Trait: the alleles differ | Database | Open Targets credible sets | 75 | fine-mapping probability 0.0049 to 0.099; in the 95% credible set in 75 of 75; SuSiE-inf, PICS |
| Trait: the alleles differ | Database | GWAS Catalog | 12 | p 7.0e-42 to 1.0e-10 |
| Trait: the parts are in place | Database | Open Targets colocalisations | 136 | probability of one shared causal variant (H4) 0.24 to 0.99; COLOC\_PIP\_ECAVIAR |
| Trait: the parts are in place | Database | Open Targets gene and disease records | 11 | source score 0.19 to 0.99; sources: gene burden, impc, eva, genomics england |
| Trait: the parts are in place | Model prediction | Open Targets locus-to-gene score | 75 | score 0.97 to 0.99 |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **The tie for first** (4 chains). Experiment: The tied chains differ in the transcription factor: PRRX1, ILF3. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: a measurement of the alleles' binding where there is only a prediction.
- **The tie for first** (4 chains). Experiment: The tied chains differ in the target gene: PPARG, TIMP4. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: the allele edited in the genome, with the RNA of each gene read out.
- **TF binding: the parts are in place** (nothing supports it). Experiment: Show each of the tied transcription factors at the site: ChIP in a cell type where the element is active.
- **TF binding: the parts are in place** (nothing supports it). Lookup: Give the run a cell context, and the expression of the transcription factor there is looked up.
- **Regulatory activity: the parts are in place** (nothing supports it). Experiment: The variant lies in no registered regulatory element. An accessibility or histone-mark assay at the site, in a cell type that matters for the trait, would show whether it is one.
- **Target gene: the parts are in place** (nothing supports it). Experiment: Silence or delete the element (the variant's site) and read out the RNA of PPARG, TIMP4.
- **Target gene: the alleles differ** (associated only). Experiment: Edit the allele in the genome and read out the RNA of PPARG, TIMP4. An association cannot separate this variant from the variants inherited with it.

### Going back for evidence

After the first reading the loop ran 1 round(s): code took its own menu in order. It was a dry run: the searches ran and nothing was read. The chains that are first did not change.

- Round 1, planned by code: 4 pair(s) of TF and gene searched, 4 search(es) for the tied candidates, 4 review(s) opened: 3 new article(s) listed, 0 read, 0 experiment(s) filed; no cell and no rank changed.

| Round | Searched for | Why | Listed | New | Read | Filed | Count for a claim | Join the pair |
|---|---|---|---|---|---|---|---|---|
| 1 | PRRX1 → PPARG | the TF changed and the gene read out | 0 | 0 | 0 | 0 | – | 0 |
| 1 | PRRX1 → TIMP4 | the TF changed and the gene read out | 0 | 0 | 0 | 0 | – | 0 |
| 1 | ILF3 → PPARG | the TF changed and the gene read out | 0 | 0 | 0 | 0 | – | 0 |
| 1 | ILF3 → TIMP4 | the TF changed and the gene read out | 0 | 0 | 0 | 0 | – | 0 |
| 1 | PRRX1 | the variant with a tied candidate | 5 | 0 | 0 | 0 | 0 | – |
| 1 | ILF3 | the variant with a tied candidate | 1 | 0 | 0 | 0 | 0 | – |
| 1 | PPARG | the variant with a tied candidate | 5 | 0 | 0 | 0 | 0 | – |
| 1 | TIMP4 | the variant with a tied candidate | 0 | 0 | 0 | 0 | 0 | – |
| 1 | PMID:39164015 (a review) | what a review cites | 0 | 0 | 0 | 0 | 0 | – |
| 1 | PMC6087882 (a review) | what a review cites | 0 | 0 | 0 | 0 | 0 | – |
| 1 | PMC8578350 (a review) | what a review cites | 0 | 0 | 0 | 0 | 0 | – |
| 1 | PMC8073710 (a review) | what a review cites | 4 | 3 | 0 | 0 | 0 | – |

Not in this version of the loop: reading on in a paragraph when a record was cut short, widening a lookup to more tissues, and anything that costs more than a reading (a model run, a cluster job).

## Outcome

**Multiple explanations**; stopped because converged.

4 chains tie for first: PRRX1 or ILF3 → PPARG or TIMP4. They differ in the transcription factor and the target gene and the gene to trait link. Measured: TF binding, regulatory activity. Association only: target gene, gene to trait, variant to trait. Filled by code from databases and model predictions, and from 11 of 21 article(s) found that name the variant, each read once by a model: 17 experiment(s) were filed as records. The loop then went back for evidence: in 1 round(s) it read 0 more article(s), from which 0 experiment(s) were filed; it stopped because a dry run: the first round was

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
