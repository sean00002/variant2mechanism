# v2m run report: GRCh38 chr8:127401265 T&gt;C

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (20 tool calls); a model was called only to read articles (1 model call), so no hypothesis was proposed.

Case REQ-84a7f2e7e3fd · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs73706717 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E3858447 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**6 chains tie for first: G051 (TCF12, TCF3, TCF4), G161 (CTCF), G468 (ZNF263) or 3 more → POU5F1B. They differ only in the transcription factor.**

Association only: variant to trait. Predicted only: TF binding, gene to trait. No claim: regulatory activity, target gene.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G051 (TCF12, TCF3, TCF4), G161 (CTCF), G468 (ZNF263), G038 (HMBOX1, HNF1A, HNF1B), and 2 more (tied) | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | – | no claim |
| Target gene | POU5F1B | no claim |
| Gene to trait | POU5F1B → Urinary incontinence and 1 more | predicted |
| Variant to trait | Urinary incontinence and 1 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | G051 (TCF12, TCF3, TCF4) → POU5F1B | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | POU5F1B → Urinary incontinence, POU5F1B → prostate specific antigen amount (tied): predicted | tied for first |
| 1= | G161 (CTCF) → POU5F1B | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | POU5F1B → Urinary incontinence, POU5F1B → prostate specific antigen amount (tied): predicted | tied for first |
| 1= | G468 (ZNF263) → POU5F1B | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | POU5F1B → Urinary incontinence, POU5F1B → prostate specific antigen amount (tied): predicted | tied for first |
| 1= | G038 (HMBOX1, HNF1A, HNF1B) → POU5F1B | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | POU5F1B → Urinary incontinence, POU5F1B → prostate specific antigen amount (tied): predicted | tied for first |
| 1= | G027 (NFIA, NFIB, NFIC and 1 more) → POU5F1B | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | POU5F1B → Urinary incontinence, POU5F1B → prostate specific antigen amount (tied): predicted | tied for first |
| 1= | G098 (SMAD1, SMAD3, SMAD5 and 1 more) → POU5F1B | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | POU5F1B → Urinary incontinence, POU5F1B → prostate specific antigen amount (tied): predicted | tied for first |
| 7= | G086 (MSC, TCF21) → POU5F1B | predicted by QBiC-SELEX; in place: a ChIP-seq peak over the variant | no claim | POU5F1B → Urinary incontinence, POU5F1B → prostate specific antigen amount (tied): predicted | the same kinds of evidence on every link; no strong prediction (a change in the top 10% for the TF group, with a ChIP-seq peak over the variant) |
| 7= | G100 (SREBF1, SREBF2) → POU5F1B | predicted by QBiC-SELEX; in place: a ChIP-seq peak over the variant | no claim | POU5F1B → Urinary incontinence, POU5F1B → prostate specific antigen amount (tied): predicted | the same kinds of evidence on every link; no strong prediction (a change in the top 10% for the TF group, with a ChIP-seq peak over the variant) |

209 more chains not shown, 36 of them tied at rank 7. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 6 tied for first: G051 (TCF12, TCF3, TCF4) → POU5F1B. The run stated 5 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G051 (TCF12, TCF3, TCF4) | nothing found | supports: 1 (prediction) | nothing found (1 of 1 articles found were read by the model; 1 of the 1 experiments it returned did not pass code's checks) |
| TF binding | The parts are in place | G051 (TCF12, TCF3, TCF4) | supports: 1 (occupancy) | no source | nothing found (1 of 1 articles found were read by the model; 1 of the 1 experiments it returned did not pass code's checks) |
| Regulatory activity | The alleles differ | ENSR8\_CGMBX; EH38E3858447 (not stated by the run) | nothing found | no source | nothing found (1 of 1 articles found were read by the model; 1 of the 1 experiments it returned did not pass code's checks) |
| Regulatory activity | The parts are in place | ENSR8\_CGMBX; EH38E3858447 | supports: 2 (annotation) | no source | nothing found (1 of 1 articles found were read by the model; 1 of the 1 experiments it returned did not pass code's checks) |
| Target gene | The alleles differ | POU5F1B (not stated by the run) | nothing found | no source | nothing found (1 of 1 articles found were read by the model; 1 of the 1 experiments it returned did not pass code's checks) |
| Target gene | The parts are in place | POU5F1B (not stated by the run) | nothing found | no source | nothing found (1 of 1 articles found were read by the model; 1 of the 1 experiments it returned did not pass code's checks) |
| Trait | The alleles differ | Urinary incontinence; prostate specific antigen amount | supports: 2 (association) | no source | nothing found (1 of 1 articles found were read by the model; 1 of the 1 experiments it returned did not pass code's checks) |
| Trait | The parts are in place | POU5F1B → Urinary incontinence; POU5F1B → prostate specific antigen amount | nothing found | supports: 2 (prediction) | nothing found (1 of 1 articles found were read by the model; 1 of the 1 experiments it returned did not pass code's checks) |

Literature: 1 articles naming the variant were found and 1 read, each once, by a model that returned 1 experiments; 0 passed code's checks against the text and were filed as records.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 1 | group G051 (bHLH); more binding to T; \|z\| 22.5; p 2.2e-112; 2 of 3 models past the gate; in the top 10% for this group |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 1 | a peak over the variant in 1 experiment; TFs: TCF4; cell types: LS180; summits 195 bp from the variant |
| Regulatory activity: the parts are in place | Database | Ensembl annotation | 1 | regulatory region variant |
| Regulatory activity: the parts are in place | Database | ENCODE registry of regulatory elements | 1 | EH38E3858447; proximal enhancer-like (pELS) |
| Trait: the alleles differ | Database | Open Targets credible sets | 2 | fine-mapping probability 0.035 to 0.036; in the 95% credible set in 2 of 2; SuSiE-inf |
| Trait: the parts are in place | Model prediction | Open Targets locus-to-gene score | 2 | score 0.78 to 0.83 |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **The tie for first** (6 chains). Experiment: The tied chains differ in the transcription factor: G051 (TCF12, TCF3, TCF4), G161 (CTCF), G468 (ZNF263) and 3 more. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: a measurement of the alleles' binding where there is only a prediction.
- **Regulatory activity: the alleles differ** (nothing supports it). Experiment: Compare the regulatory activity of the two alleles: a reporter assay with both, or the allele edited in the genome with accessibility or enhancer marks read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Model run: No model in this version predicts the alleles' regulatory activity. A sequence-to-activity model would give this cell a prediction.
- **Target gene: the alleles differ** (nothing supports it). Experiment: Edit the allele in the genome and read out the RNA of POU5F1B. An association cannot separate this variant from the variants inherited with it.
- **Target gene: the parts are in place** (nothing supports it). Experiment: Silence or delete the element (ENSR8\_CGMBX, EH38E3858447) and read out the RNA of POU5F1B.
- **TF binding: the alleles differ** (predicted only). Experiment: Compare the binding of each of the tied transcription factors to the T and C alleles directly: a binding assay with both alleles, or ChIP reads counted by allele in cells that carry both.
- **Trait: the parts are in place** (predicted only). Experiment: Perturb POU5F1B and read out the trait, or the cell behaviour behind it. Genetic evidence that ties the gene itself to the trait would be an association for the same claim.

## Outcome

**Partial mechanism**; stopped because converged.

6 chains tie for first: G051 (TCF12, TCF3, TCF4), G161 (CTCF), G468 (ZNF263) or 3 more → POU5F1B. They differ only in the transcription factor. Association only: variant to trait. Predicted only: TF binding, gene to trait. No claim: regulatory activity, target gene. Filled by code from databases and model predictions, and from 1 of 1 article(s) found that name the variant, each read once by a model: 0 experiment(s) were filed as records.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
