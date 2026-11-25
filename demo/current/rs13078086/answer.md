# v2m run report: GRCh38 chr3:191441666 T&gt;G

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (18 tool calls); no model was called, so no hypothesis was proposed.

Case REQ-3de2796567aa · Cache-only run · origin germline · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs13078086 (T1, variant\_annotation)
- Elements containing it, found by code: none recorded

## Answer: ranked mechanism chains

**Leading chain: G022 (FOXA1, FOXA2, FOXA3 and 3 more) → no target gene named.**

Predicted only: TF binding. No claim: regulatory activity, target gene, gene to trait, variant to trait.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G022 (FOXA1, FOXA2, FOXA3 and 3 more) | predicted by QBiC-SELEX; in place: a ChIP-seq peak over the variant |
| Regulatory activity | – | no claim |
| Target gene | – | no claim |
| Gene to trait | – | no claim |
| Variant to trait | – | no claim |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1 | G022 (FOXA1, FOXA2, FOXA3 and 3 more) → no target gene named | predicted by QBiC-SELEX; in place: a ChIP-seq peak over the variant | no claim | no claim | leads |
| 2= | G030 (TFAP2A, TFAP2B, TFAP2C and 2 more) → no target gene named | predicted by QBiC-SELEX | no claim | no claim | the same kinds of evidence on every link; no record of a ChIP-seq peak over the variant |
| 2= | G112 (AHCTF1) → no target gene named | predicted by QBiC-SELEX | no claim | no claim | the same kinds of evidence on every link; no record of a ChIP-seq peak over the variant |
| 2= | G139 (CBX2) → no target gene named | predicted by QBiC-SELEX | no claim | no claim | the same kinds of evidence on every link; no record of a ChIP-seq peak over the variant |
| 2= | G308 (PRR12) → no target gene named | predicted by QBiC-SELEX | no claim | no claim | the same kinds of evidence on every link; no record of a ChIP-seq peak over the variant |
| 2= | G387 (ZBED1) → no target gene named | predicted by QBiC-SELEX | no claim | no claim | the same kinds of evidence on every link; no record of a ChIP-seq peak over the variant |
| 2= | G059 (BHLHE22, BHLHE23) → no target gene named | predicted by QBiC-SELEX | no claim | no claim | the same kinds of evidence on every link; no record of a ChIP-seq peak over the variant |
| 2= | G060 (BHLHE40, BHLHE41) → no target gene named | predicted by QBiC-SELEX | no claim | no claim | the same kinds of evidence on every link; no record of a ChIP-seq peak over the variant |

166 more chains not shown, 166 of them tied at rank 2. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain: G022 (FOXA1, FOXA2, FOXA3 and 3 more) → no target gene named. The run stated 2 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G022 (FOXA1, FOXA2, FOXA3 and 3 more) | nothing found | supports: 3 (prediction) | not checked (the search for articles naming the variant did not complete, so none was looked for) |
| TF binding | The parts are in place | G022 (FOXA1, FOXA2, FOXA3 and 3 more) | supports: 3 (occupancy) | no source | not checked (the search for articles naming the variant did not complete, so none was looked for) |
| Regulatory activity | The alleles differ | the variant's site (not stated by the run) | nothing found | no source | not checked (the search for articles naming the variant did not complete, so none was looked for) |
| Regulatory activity | The parts are in place | the variant's site (not stated by the run) | nothing found | no source | not checked (the search for articles naming the variant did not complete, so none was looked for) |
| Target gene | The alleles differ | no gene named (not stated by the run) | nothing found | no source | not checked (the search for articles naming the variant did not complete, so none was looked for) |
| Target gene | The parts are in place | no gene named (not stated by the run) | nothing found | no source | not checked (the search for articles naming the variant did not complete, so none was looked for) |
| Trait | The alleles differ | no trait named (not stated by the run) | nothing found | no source | not checked (the search for articles naming the variant did not complete, so none was looked for) |
| Trait | The parts are in place | no gene named → no trait named (not stated by the run) | nothing found | nothing found | not checked (the search for articles naming the variant did not complete, so none was looked for) |

Literature: the search for articles naming the variant did not complete, so none was looked for.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 3 | group G007 (Forkhead); more binding to T; \|z\| 6.0; p 1.5e-09; 2 of 10 models past the gate; not in the top 10% for this group / group G007 (Forkhead); more binding to G; \|z\| 5.2; p 2.3e-07; 2 of 10 models past the gate; not in the top 10% for this group / and 1 more record |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 3 | a peak over the variant in 3 experiments; TFs: FOXA2; cell types: BJ1-hTERT; summits 124 to 141 bp from the variant |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **Regulatory activity: the alleles differ** (nothing supports it). Experiment: Compare the regulatory activity of the two alleles: a reporter assay with both, or the allele edited in the genome with accessibility or enhancer marks read out.
- **Regulatory activity: the alleles differ** (nothing supports it). Model run: No model in this version predicts the alleles' regulatory activity. A sequence-to-activity model would give this cell a prediction.
- **Regulatory activity: the parts are in place** (nothing supports it). Experiment: The variant lies in no registered regulatory element. An accessibility or histone-mark assay at the site, in a cell type that matters for the trait, would show whether it is one.
- **Target gene: the alleles differ** (nothing supports it). Experiment: No source names a gene whose RNA differs between the alleles. An eQTL of this variant, or the allele edited in the genome with the RNA of nearby genes read out, would name one.
- **Trait: the alleles differ** (nothing supports it). Source: No association of this variant with a trait is on file in the sources this run reads.
- **TF binding: the alleles differ** (predicted only). Experiment: Compare the binding of FOXA1, FOXA2, FOXA3, FOXB1 and 2 more to the T and G alleles directly: a binding assay with both alleles, or ChIP reads counted by allele in cells that carry both.

## Outcome

**Partial mechanism**; stopped because converged.

Leading chain: G022 (FOXA1, FOXA2, FOXA3 and 3 more) → no target gene named. Predicted only: TF binding. No claim: regulatory activity, target gene, gene to trait, variant to trait. Filled by code from databases and model predictions. The search for articles that name the variant did not complete, so none was read.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
