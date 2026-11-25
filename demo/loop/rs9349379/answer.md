# v2m run report: GRCh38 chr6:12903725 A&gt;G

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (118 tool calls); a model was called only to read articles (20 model calls), so no hypothesis was proposed.

Case REQ-872bed827d24 · Live run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs9349379 (T1, variant\_annotation)
- Elements containing it, found by code: none recorded

## Answer: ranked mechanism chains

**Leading chain: MEF2 → PHACTR1.**

Measured: TF binding, target gene. Association only: gene to trait, variant to trait. No claim: regulatory activity.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | MEF2 | allele-resolved assay |
| Regulatory activity | – | no claim |
| Target gene | PHACTR1 | edit or perturbation |
| Gene to trait | PHACTR1 → coronary artery disorder and 26 more | association |
| Variant to trait | coronary artery disorder and 41 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1 | MEF2 → PHACTR1 | allele-resolved assay | edit or perturbation | PHACTR1 → coronary artery disorder, PHACTR1 → intermediate coronary syndrome, PHACTR1 → spontaneous coronary artery dissection, and 24 more (tied): association | leads |
| 2= | MEF2 → TBC1D7 | allele-resolved assay | association | TBC1D7 → coronary artery disorder, TBC1D7 → intermediate coronary syndrome, TBC1D7 → systolic blood pressure, and 9 more (tied): association | weaker on target gene |
| 2= | MEF2 → ENSG00000272379 | allele-resolved assay | association | ENSG00000272379 → coronary artery disorder, ENSG00000272379 → intermediate coronary syndrome, ENSG00000272379 → spontaneous coronary artery dissection, and 21 more (tied): association | weaker on target gene |
| 4 | MEF2 → GFOD1 | allele-resolved assay | association | GFOD1 → coronary artery disorder, GFOD1 → intermediate coronary syndrome, GFOD1 → systolic blood pressure, and 8 more (tied): predicted | weaker on target gene, gene to trait |
| 5 | MEF2 → EDN1 | allele-resolved assay | edit or perturbation | no claim | weaker on gene to trait |
| 6 | MEF2 → RP1-257A7.4 | allele-resolved assay | association | no claim | weaker on target gene, gene to trait |

Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain: MEF2 → PHACTR1. The run stated 5 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | MEF2 | nothing found | not checked | supports: 1 (assay) |
| TF binding | The parts are in place | MEF2 (not stated by the run) | nothing found | no source | nothing found (18 of 60 articles found were read by the model; 18 not looked into (a review, no text, a failed call or the cap); 15 of the 35 experiments it returned did not pass code's checks) |
| Regulatory activity | The alleles differ | the variant's site (not stated by the run) | nothing found | no source | nothing found (18 of 60 articles found were read by the model; 18 not looked into (a review, no text, a failed call or the cap); 15 of the 35 experiments it returned did not pass code's checks); 11 set aside |
| Regulatory activity | The parts are in place | the variant's site (not stated by the run) | nothing found | no source | nothing found (18 of 60 articles found were read by the model; 18 not looked into (a review, no text, a failed call or the cap); 15 of the 35 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | PHACTR1 | supports: 138 (association) | no source | nothing found (18 of 60 articles found were read by the model; 18 not looked into (a review, no text, a failed call or the cap); 15 of the 35 experiments it returned did not pass code's checks); 2 set aside |
| Target gene | The parts are in place | PHACTR1 | nothing found | no source | supports: 1 (edit); 9 set aside |
| Trait | The alleles differ | coronary artery disorder; intermediate coronary syndrome; spontaneous coronary artery dissection and 39 more | supports: 210 (association) | no source | nothing found (18 of 60 articles found were read by the model; 18 not looked into (a review, no text, a failed call or the cap); 15 of the 35 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | PHACTR1 → coronary artery disorder; PHACTR1 → intermediate coronary syndrome; PHACTR1 → spontaneous coronary artery dissection and 24 more | supports: 134 (association) | supports: 75 (prediction) | nothing found (18 of 60 articles found were read by the model; 18 not looked into (a review, no text, a failed call or the cap); 15 of the 35 experiments it returned did not pass code's checks); 7 set aside |

Literature: 60 articles naming the variant were found and 18 read, each once, by a model that returned 35 experiments; 20 passed code's checks against the text and were filed as records. Of the rest, 24 did not name the variant in the text retrieved, 18 were reviews.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:25838425); the report quotes the sentences |
| Target gene: the alleles differ | Database | GTEx eQTL | 4 | effect size -0.39 to +0.22 for G; p 8.0e-42 to 5.2e-07; tissues: Artery Aorta, Artery Coronary, Artery Tibial, Heart Atrial Appendage |
| Target gene: the alleles differ | Database | Open Targets colocalisations | 134 | probability of one shared causal variant (H4) 0.90 to 1.00; COLOC\_PIP\_ECAVIAR |
| Target gene: the parts are in place | Literature | Articles read by the model | 1 | 1 experiment in 1 article (PMID:25838425); the report quotes the sentences |
| Trait: the alleles differ | Database | Open Targets credible sets | 75 | fine-mapping probability 0.0086 to 1; in the 95% credible set in 75 of 75; SuSiE-inf, PICS, SuSie |
| Trait: the alleles differ | Database | GWAS Catalog | 135 | p 4.0e-114 to 6.0e-06 |
| Trait: the parts are in place | Database | Open Targets colocalisations | 134 | probability of one shared causal variant (H4) 0.90 to 1.00; COLOC\_PIP\_ECAVIAR |
| Trait: the parts are in place | Model prediction | Open Targets locus-to-gene score | 75 | score 0.81 to 0.95 |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **TF binding: the parts are in place** (nothing supports it). Experiment: Show the transcription factor (MEF2) at the site: ChIP in a cell type where the element is active.
- **TF binding: the parts are in place** (nothing supports it). Lookup: Give the run a cell context, and the expression of the transcription factor there is looked up.
- **Regulatory activity: the alleles differ** (nothing supports it). Experiment: Compare the regulatory activity of the two alleles: a reporter assay with both, or the allele edited in the genome with accessibility or enhancer marks read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Model run: No model in this version predicts the alleles' regulatory activity. A sequence-to-activity model would give this cell a prediction.
- **Regulatory activity: the parts are in place** (nothing supports it). Experiment: The variant lies in no registered regulatory element. An accessibility or histone-mark assay at the site, in a cell type that matters for the trait, would show whether it is one.
- **Target gene: the alleles differ** (associated only). Experiment: Edit the allele in the genome and read out the RNA of PHACTR1. An association cannot separate this variant from the variants inherited with it.

### Going back for evidence

After the first reading the loop ran 2 round(s): a planner model picked from the menu code listed. It read 4 more article(s), from which 8 experiment(s) were filed: 2 count for a claim. It stopped because a round changed no cell and no rank. First before: no TF named → PHACTR1; no TF named → TBC1D7; no TF named → ENSG00000272379. First after: MEF2 → PHACTR1.

- Round 1, planned by the planner: 2 search(es) for the tied candidates, 4 review(s) opened, 2 search(es) for names from the planner's memory: 25 new article(s) listed, 4 read, 8 experiment(s) filed; 2 cell(s) changed; the first chains changed.
- Round 2, planned by the planner: 1 pair(s) of TF and gene searched, 1 search(es) for what a weak claim names, 4 review(s) opened: 10 new article(s) listed, 0 read, 0 experiment(s) filed; no cell and no rank changed.

| Round | Searched for | Why | Listed | New | Read | Filed | Count for a claim | Join the pair |
|---|---|---|---|---|---|---|---|---|
| 1 | PHACTR1 | the variant with a tied candidate: This directly tests the tied target-gene candidates and could find experiments that connect the variant to a gene. | 5 | 1 | 1 | 0 | 0 | – |
| 1 | TBC1D7 | the variant with a tied candidate: This directly tests the tied target-gene candidates and could find experiments that connect the variant to a gene. | 2 | 1 | 0 | 0 | 0 | – |
| 1 | PMC10196206 (a review) | what a review cites: The cited primary articles may contain experiments that fill the otherwise unsupported TF-binding or regulatory-activity gaps. | 26 | 5 | 0 | 0 | 0 | – |
| 1 | PMC12965744 (a review) | what a review cites: The cited primary articles may contain experiments that fill the otherwise unsupported TF-binding or regulatory-activity gaps. | 6 | 5 | 1 | 3 | 0 | – |
| 1 | PMC12069897 (a review) | what a review cites: The cited primary articles may contain experiments that fill the otherwise unsupported TF-binding or regulatory-activity gaps. | 6 | 5 | 0 | 0 | 0 | – |
| 1 | PMC10527262 (a review) | what a review cites: The cited primary articles may contain experiments that fill the otherwise unsupported TF-binding or regulatory-activity gaps. | 4 | 3 | 0 | 0 | 0 | – |
| 1 | MEF2A (from memory) | the variant with a name from the planner's memory | 4 | 4 | 2 | 5 | 2 | – |
| 1 | EDN1 (from memory) | the variant with a name from the planner's memory | 5 | 1 | 0 | 0 | 0 | – |
| 2 | MEF2 → PHACTR1 | the TF changed and the gene read out: This directly tests the unresolved MEF2–PHACTR1 pair, which could connect the factor and gene in the chain. | 1 | 0 | 0 | 0 | – | 0 |
| 2 | MEF2 | the variant with what a weak claim names: Variant-specific assays involving MEF2 could support the otherwise unsupported claim that MEF2 is in place at the variant. | 5 | 2 | 0 | 0 | 0 | – |
| 2 | PMC7948363 (a review) | what a review cites: Cited articles may contain experiments that address the unsupported regulatory-activity claims or otherwise strengthen the chain. | 0 | 0 | 0 | 0 | 0 | – |
| 2 | PMC12126237 (a review) | what a review cites: Cited articles may contain experiments that address the unsupported regulatory-activity claims or otherwise strengthen the chain. | 6 | 5 | 0 | 0 | 0 | – |
| 2 | PMC10038164 (a review) | what a review cites: Cited articles may contain experiments that address the unsupported regulatory-activity claims or otherwise strengthen the chain. | 4 | 3 | 0 | 0 | 0 | – |
| 2 | PMC8829969 (a review) | what a review cites: Cited articles may contain experiments that address the unsupported regulatory-activity claims or otherwise strengthen the chain. | 0 | 0 | 0 | 0 | 0 | – |

Proposed by the planner from memory, and used as search terms only: MEF2A (tf, round 1); EDN1 (gene, round 1); EDN1 (gene, round 2).

Not in this version of the loop: reading on in a paragraph when a record was cut short, widening a lookup to more tissues, and anything that costs more than a reading (a model run, a cluster job).

## Outcome

**Partial mechanism**; stopped because converged.

Leading chain: MEF2 → PHACTR1. Measured: TF binding, target gene. Association only: gene to trait, variant to trait. No claim: regulatory activity. Filled by code from databases and model predictions, and from 18 of 60 article(s) found that name the variant, each read once by a model: 20 experiment(s) were filed as records. The loop then went back for evidence: in 2 round(s) it read 4 more article(s), from which 8 experiment(s) were filed; it stopped because a round changed no cell and no rank.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
