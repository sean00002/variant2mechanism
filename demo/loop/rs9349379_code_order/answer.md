# v2m run report: GRCh38 chr6:12903725 A&gt;G

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (90 tool calls); a model was called only to read articles (16 model calls), so no hypothesis was proposed.

Case REQ-872bed827d24 · Live run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs9349379 (T1, variant\_annotation)
- Elements containing it, found by code: none recorded

## Answer: ranked mechanism chains

**3 chains tie for first: no TF named → PHACTR1, TBC1D7 or ENSG00000272379. They differ in the target gene and the gene to trait link.**

Association only: target gene, gene to trait, variant to trait. No claim: TF binding, regulatory activity.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | – | no claim |
| Regulatory activity | – | no claim |
| Target gene | PHACTR1, TBC1D7, ENSG00000272379 (tied) | association |
| Gene to trait | PHACTR1 → coronary artery disorder and 62 more | association |
| Variant to trait | coronary artery disorder and 41 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | no TF named → PHACTR1 | no claim | association | PHACTR1 → coronary artery disorder, PHACTR1 → intermediate coronary syndrome, PHACTR1 → spontaneous coronary artery dissection, and 24 more (tied): association | tied for first |
| 1= | no TF named → TBC1D7 | no claim | association | TBC1D7 → coronary artery disorder, TBC1D7 → intermediate coronary syndrome, TBC1D7 → systolic blood pressure, and 9 more (tied): association | tied for first |
| 1= | no TF named → ENSG00000272379 | no claim | association | ENSG00000272379 → coronary artery disorder, ENSG00000272379 → intermediate coronary syndrome, ENSG00000272379 → spontaneous coronary artery dissection, and 21 more (tied): association | tied for first |
| 4 | no TF named → GFOD1 | no claim | association | GFOD1 → coronary artery disorder, GFOD1 → intermediate coronary syndrome, GFOD1 → systolic blood pressure, and 8 more (tied): predicted | weaker on gene to trait |
| 5 | no TF named → EDN1 | no claim | edit or perturbation | no claim | weaker on gene to trait; stronger on target gene |
| 6 | no TF named → RP1-257A7.4 | no claim | association | no claim | weaker on gene to trait |

Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 3 tied for first: no TF named → PHACTR1. The run stated 3 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | no TF named (not stated by the run) | nothing found | not checked | nothing found (16 of 45 articles found were read by the model; 12 not looked into (a review, no text, a failed call or the cap); 13 of the 28 experiments it returned did not pass code's checks) |
| TF binding | The parts are in place | no TF named (not stated by the run) | nothing found | no source | nothing found (16 of 45 articles found were read by the model; 12 not looked into (a review, no text, a failed call or the cap); 13 of the 28 experiments it returned did not pass code's checks) |
| Regulatory activity | The alleles differ | the variant's site (not stated by the run) | nothing found | no source | nothing found (16 of 45 articles found were read by the model; 12 not looked into (a review, no text, a failed call or the cap); 13 of the 28 experiments it returned did not pass code's checks); 10 set aside |
| Regulatory activity | The parts are in place | the variant's site (not stated by the run) | nothing found | no source | nothing found (16 of 45 articles found were read by the model; 12 not looked into (a review, no text, a failed call or the cap); 13 of the 28 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | PHACTR1 | supports: 138 (association) | no source | nothing found (16 of 45 articles found were read by the model; 12 not looked into (a review, no text, a failed call or the cap); 13 of the 28 experiments it returned did not pass code's checks); 1 set aside |
| Target gene | The parts are in place | PHACTR1 (not stated by the run) | nothing found | no source | nothing found (16 of 45 articles found were read by the model; 12 not looked into (a review, no text, a failed call or the cap); 13 of the 28 experiments it returned did not pass code's checks); 6 set aside |
| Trait | The alleles differ | coronary artery disorder; intermediate coronary syndrome; spontaneous coronary artery dissection and 39 more | supports: 210 (association) | no source | nothing found (16 of 45 articles found were read by the model; 12 not looked into (a review, no text, a failed call or the cap); 13 of the 28 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | PHACTR1 → coronary artery disorder; PHACTR1 → intermediate coronary syndrome; PHACTR1 → spontaneous coronary artery dissection and 24 more | supports: 134 (association) | supports: 75 (prediction) | nothing found (16 of 45 articles found were read by the model; 12 not looked into (a review, no text, a failed call or the cap); 13 of the 28 experiments it returned did not pass code's checks); 3 set aside |

Literature: 45 articles naming the variant were found and 16 read, each once, by a model that returned 28 experiments; 15 passed code's checks against the text and were filed as records. Of the rest, 17 did not name the variant in the text retrieved, 12 were reviews.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| Target gene: the alleles differ | Database | GTEx eQTL | 4 | effect size -0.39 to +0.22 for G; p 8.0e-42 to 5.2e-07; tissues: Artery Aorta, Artery Coronary, Artery Tibial, Heart Atrial Appendage |
| Target gene: the alleles differ | Database | Open Targets colocalisations | 134 | probability of one shared causal variant (H4) 0.90 to 1.00; COLOC\_PIP\_ECAVIAR |
| Trait: the alleles differ | Database | Open Targets credible sets | 75 | fine-mapping probability 0.0086 to 1; in the 95% credible set in 75 of 75; SuSiE-inf, PICS, SuSie |
| Trait: the alleles differ | Database | GWAS Catalog | 135 | p 4.0e-114 to 6.0e-06 |
| Trait: the parts are in place | Database | Open Targets colocalisations | 134 | probability of one shared causal variant (H4) 0.90 to 1.00; COLOC\_PIP\_ECAVIAR |
| Trait: the parts are in place | Model prediction | Open Targets locus-to-gene score | 75 | score 0.81 to 0.95 |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **The tie for first** (3 chains). Experiment: The tied chains differ in the target gene: PHACTR1, TBC1D7, ENSG00000272379. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: the allele edited in the genome, with the RNA of each gene read out.
- **TF binding: the alleles differ** (nothing supports it). Experiment: Compare the binding of the transcription factor to the A and G alleles directly: a binding assay with both alleles, or ChIP reads counted by allele in cells that carry both.
- **TF binding: the parts are in place** (nothing supports it). Experiment: Show the transcription factor (the transcription factor) at the site: ChIP in a cell type where the element is active.
- **TF binding: the parts are in place** (nothing supports it). Lookup: Give the run a cell context, and the expression of the transcription factor there is looked up.
- **Regulatory activity: the alleles differ** (nothing supports it). Experiment: Compare the regulatory activity of the two alleles: a reporter assay with both, or the allele edited in the genome with accessibility or enhancer marks read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Model run: No model in this version predicts the alleles' regulatory activity. A sequence-to-activity model would give this cell a prediction.
- **Regulatory activity: the parts are in place** (nothing supports it). Experiment: The variant lies in no registered regulatory element. An accessibility or histone-mark assay at the site, in a cell type that matters for the trait, would show whether it is one.
- **Target gene: the parts are in place** (nothing supports it). Experiment: Silence or delete the element (the variant's site) and read out the RNA of PHACTR1, TBC1D7, ENSG00000272379.
- **Target gene: the alleles differ** (associated only). Experiment: Edit the allele in the genome and read out the RNA of PHACTR1, TBC1D7, ENSG00000272379. An association cannot separate this variant from the variants inherited with it.

### Going back for evidence

After the first reading the loop ran 1 round(s): code took its own menu in order. It read 2 more article(s), from which 3 experiment(s) were filed: 0 count for a claim. It stopped because a round changed no cell and no rank. The chains that are first did not change.

- Round 1, planned by code: 2 search(es) for the tied candidates, 4 review(s) opened: 20 new article(s) listed, 2 read, 3 experiment(s) filed; no cell and no rank changed.

| Round | Searched for | Why | Listed | New | Read | Filed | Count for a claim | Join the pair |
|---|---|---|---|---|---|---|---|---|
| 1 | PHACTR1 | the variant with a tied candidate | 5 | 1 | 1 | 0 | 0 | – |
| 1 | TBC1D7 | the variant with a tied candidate | 2 | 1 | 0 | 0 | 0 | – |
| 1 | PMC10196206 (a review) | what a review cites | 26 | 5 | 0 | 0 | 0 | – |
| 1 | PMC12965744 (a review) | what a review cites | 6 | 5 | 1 | 3 | 0 | – |
| 1 | PMC12069897 (a review) | what a review cites | 6 | 5 | 0 | 0 | 0 | – |
| 1 | PMC10527262 (a review) | what a review cites | 4 | 3 | 0 | 0 | 0 | – |

Not in this version of the loop: reading on in a paragraph when a record was cut short, widening a lookup to more tissues, and anything that costs more than a reading (a model run, a cluster job).

## Outcome

**Partial mechanism**; stopped because converged.

3 chains tie for first: no TF named → PHACTR1, TBC1D7 or ENSG00000272379. They differ in the target gene and the gene to trait link. Association only: target gene, gene to trait, variant to trait. No claim: TF binding, regulatory activity. Filled by code from databases and model predictions, and from 16 of 45 article(s) found that name the variant, each read once by a model: 15 experiment(s) were filed as records. The loop then went back for evidence: in 1 round(s) it read 2 more article(s), from which 3 experiment(s) were filed; it stopped because a round changed no cell and no rank.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
