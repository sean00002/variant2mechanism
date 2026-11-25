# v2m run report: GRCh38 chr5:1295135 G&gt;A

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (19 tool calls); no model was called, so no hypothesis was proposed.

Case REQ-9287615eba24 · Cache-only run · origin somatic · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs1561215364 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E3622530 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**11 chains tie for first: G120 (ARID2), G122 (ARNT, ARNT2), G011 (KLF1, KLF12, KLF2 and 6 more) or 8 more → no target gene named. They differ only in the transcription factor.**

Measured: regulatory activity. Association only: variant to trait. Predicted only: TF binding. No claim: target gene, gene to trait.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G120 (ARID2), G122 (ARNT, ARNT2), G011 (KLF1, KLF12, KLF2 and 6 more), G105 (ZNF143, ZNF76), and 7 more (tied) | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | EH38E3622530 | allele-resolved assay |
| Target gene | – | no claim |
| Gene to trait | – | no claim |
| Variant to trait | Glioma and 15 more | association |

| Rank | Chain | TF binding | Target gene | Gene to trait | Against the leading chain |
|---|---|---|---|---|---|
| 1= | G120 (ARID2) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G122 (ARNT, ARNT2) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G011 (KLF1, KLF12, KLF2 and 6 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G105 (ZNF143, ZNF76) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G344 (SP2) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G003 (EHF, ELF1, ELF2 and 22 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G020 (EHF, ELF1, ELF2 and 8 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |
| 1= | G345 (ELF1, ELF2, ELF4 and 1 more) → no target gene named | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant | no claim | no claim | tied for first |

342 more chains not shown, 3 of them tied at rank 1. Regulatory activity and variant to trait are the same in every chain, so they are given once, in the link-by-link view of the leading chain.

Code assembles each chain: one transcription factor and one target gene (every pair), the strongest claims on the regulatory activity and variant to trait links, and the gene to trait claims that name its gene. Chains are ordered by their weakest link, then their next weakest, and so on. In that comparison only the kind of evidence counts: the size of z, effect size, ChIP signal, expression level and the number of records do not enter it. A significant QBiC-SELEX prediction is support: alone it makes a binding link predicted, and beside a measurement or an association that agrees with it, it lifts that link above an equal one without it. A factor with no model, or none past the gate, loses nothing. Chains with the same kinds of evidence are then ordered by two things that only break ties. First, a strong prediction: the QBiC-SELEX change is in the top 10% of what that TF group predicts across 21.8 million background variants, and a ChIP-seq peak lies over the variant. Second, whether a record shows the factor in place: a ChIP-seq peak over the variant, and expression in the stated context. Each is a yes or a no, never the size of the signal or the level, and a factor without it stays in the list. Chains still equal tie. Each link is a separate claim: nothing here shows that one link causes the next.

## Chain table

Every chain is eight small claims: at each of four steps, that the two alleles differ and that the parts are in place. Each claim has one cell per kind of record. "Nothing found" means a source was asked; "not checked" means nobody looked, or records on file were never judged; "no source" means the workflow has none of that kind for the claim.

The leading chain, one of 11 tied for first: G120 (ARID2) → no target gene named. The run stated 5 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G120 (ARID2) | nothing found | supports: 1 (prediction) | nothing found (a search for the variant's names listed no article) |
| TF binding | The parts are in place | G120 (ARID2) | supports: 2 (occupancy) | no source | nothing found (a search for the variant's names listed no article) |
| Regulatory activity | The alleles differ | EH38E3622530 | supports: 4 (assay) | no source | nothing found (a search for the variant's names listed no article) |
| Regulatory activity | The parts are in place | ENSR5\_832QG; EH38E3622530 | supports: 2 (annotation) | no source | nothing found (a search for the variant's names listed no article) |
| Target gene | The alleles differ | no gene named (not stated by the run) | nothing found | no source | nothing found (a search for the variant's names listed no article) |
| Target gene | The parts are in place | no gene named (not stated by the run) | nothing found | no source | nothing found (a search for the variant's names listed no article) |
| Trait | The alleles differ | Glioma; Melanoma; Bladder Cancer and 13 more | supports: 16 (association) | no source | nothing found (a search for the variant's names listed no article) |
| Trait | The parts are in place | no gene named → Glioma; Melanoma; Bladder Cancer and 13 more (not stated by the run) | nothing found | nothing found | nothing found (a search for the variant's names listed no article) |

Literature: a search for the variant's names listed no article.

The table passes every rule of docs/chain-table.md.

### The numbers behind the cells

What each source returned for the claims of the leading chain. Code copied every number from the saved record, and no model typed one. The numbers are shown and never ranked on: a chain's place rests on the kind of evidence under each claim, not on its size.

| Claim | Kind of record | Source | Records | What it returned |
|---|---|---|---|---|
| TF binding: the alleles differ | Model prediction | QBiC-SELEX | 1 | group G120 (ARID/BRIGHT; RFX); more binding to G; \|z\| 7.4; p 1.4e-13; 1 of 1 models past the gate; in the top 10% for this group |
| TF binding: the parts are in place | Database | ReMap ChIP-seq peaks | 2 | a peak over the variant in 2 experiments; TFs: ARID2; cell types: Aska-SS, BIN-67; summits 140 to 232 bp from the variant |
| Regulatory activity: the alleles differ | Database | MaveDB, saturation-mutagenesis reporter assays | 4 | log2 effect on reporter activity +1.42 to +2.47, as each set records it; p below 1e-300; 293 to 306 barcodes; cells, where a set names them: HEK293T; 4 score sets: 00000031-a-1, 00000031-b-1, 00000031-c-1, 00000031-d-1 |
| Regulatory activity: the parts are in place | Database | Ensembl annotation | 1 | regulatory region variant |
| Regulatory activity: the parts are in place | Database | ENCODE registry of regulatory elements | 1 | EH38E3622530; promoter-like (PLS) |
| Trait: the alleles differ | Database | cBioPortal, tumours of the MSK-IMPACT 2017 cohort | 16 | called in the tumours of 79 of 514 patients with Glioma, 78 of 350 patients with Melanoma, 45 of 406 patients with Bladder Cancer, 17 of 144 patients with Skin Cancer, Non-Melanoma and 12 more |

### What would fill the gaps

Suggested, not performed. For each claim of the leading chain that no measurement supports, the kind of record that would. Code wrote these from the table's rule for which record counts for which claim, with the names on file. No model wrote them.

- **The tie for first** (11 chains). Experiment: The tied chains differ in the transcription factor: G120 (ARID2), G122 (ARNT, ARNT2), G011 (KLF1, KLF12, KLF2 and 6 more) and 8 more. They hold the same kinds of evidence, so a stronger kind of record for one of them would separate them: a measurement of the alleles' binding where there is only a prediction.
- **Target gene: the alleles differ** (nothing supports it). Experiment: No source names a gene whose RNA differs between the alleles. An eQTL cannot exist for a somatic mutation. The allele edited in the genome, or tumours with and without the mutation compared, with the RNA of nearby genes read out, would name one.
- **TF binding: the alleles differ** (predicted only). Experiment: Compare the binding of each of the tied transcription factors to the G and A alleles directly: a binding assay with both alleles, or ChIP reads counted by allele in cells that carry both.

## Outcome

**Partial mechanism**; stopped because converged.

11 chains tie for first: G120 (ARID2), G122 (ARNT, ARNT2), G011 (KLF1, KLF12, KLF2 and 6 more) or 8 more → no target gene named. They differ only in the transcription factor. Measured: regulatory activity. Association only: variant to trait. Predicted only: TF binding. No claim: target gene, gene to trait. Filled by code from databases and model predictions. A search found no article that names the variant, so none was read.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
