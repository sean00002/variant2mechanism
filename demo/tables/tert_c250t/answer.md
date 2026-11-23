# v2m run report: GRCh38 chr5:1295135 G&gt;A

> **Public export.** Verified passages and every other long text are cut to 600 characters, and article text is removed.

> **No hypotheses.** Code stated every claim a record on file can count for and linked the records (14 tool calls); no model was called, so no hypothesis was proposed.

Case REQ-9287615eba24 · Cache-only run · origin somatic · engine v9.0

- Disease, supplied: none supplied
- Disease, inferred: none inferred
- Context, supplied: none supplied
- Context, inferred: none inferred
- rsID, found by code: rs1561215364 (T1, variant\_annotation)
- Elements containing it, found by code: EH38E3622530 (T2, ccre\_overlap)

## Answer: ranked mechanism chains

**11 chains tie for first: G120 (ARID2), G122 (ARNT, ARNT2), G011 (KLF1, KLF12, KLF2 and 6 more) or 8 more → no target gene named. They differ only in the transcription factor.**

Reading the tie. No experiment on file names one of the tied candidates beyond the records the table counts, so nothing read from the articles separates the tied chains.

Predicted only: TF binding. No claim: regulatory activity, target gene, gene to trait, variant to trait.

| Link | Filled by | Kind of evidence |
|---|---|---|
| TF binding | G120 (ARID2), G122 (ARNT, ARNT2), G011 (KLF1, KLF12, KLF2 and 6 more), G105 (ZNF143, ZNF76), and 7 more (tied) | predicted by QBiC-SELEX; strong prediction: the QBiC-SELEX change is in the top 10% for this TF group, with a ChIP-seq peak over the variant; in place: a ChIP-seq peak over the variant |
| Regulatory activity | – | no claim |
| Target gene | – | no claim |
| Gene to trait | – | no claim |
| Variant to trait | – | no claim |

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

The leading chain, one of 11 tied for first: G120 (ARID2) → no target gene named. The run stated 3 of its 8 claims.

| Step | Claim | Names | Database | Model prediction | Literature |
|---|---|---|---|---|---|
| TF binding | The alleles differ | G120 (ARID2) | nothing found | supports: 1 (prediction) | nothing found (a search for the variant's names listed no article) |
| TF binding | The parts are in place | G120 (ARID2) | supports: 2 (occupancy) | no source | nothing found (a search for the variant's names listed no article) |
| Regulatory activity | The alleles differ | ENSR5\_832QG; EH38E3622530 (not stated by the run) | nothing found | no source | nothing found (a search for the variant's names listed no article) |
| Regulatory activity | The parts are in place | ENSR5\_832QG; EH38E3622530 | supports: 2 (annotation) | no source | nothing found (a search for the variant's names listed no article) |
| Target gene | The alleles differ | no gene named (not stated by the run) | nothing found | no source | nothing found (a search for the variant's names listed no article) |
| Target gene | The parts are in place | no gene named (not stated by the run) | nothing found | no source | nothing found (a search for the variant's names listed no article) |
| Trait | The alleles differ | no trait named (not stated by the run) | nothing found | no source | nothing found (a search for the variant's names listed no article) |
| Trait | The parts are in place | no gene named → no trait named (not stated by the run) | nothing found | nothing found | nothing found (a search for the variant's names listed no article) |

Literature: a search for the variant's names listed no article.

Second reading: no experiment from an article was up for counting, so the critic read none.

The table passes every rule of docs/chain-table.md.

## Outcome

**Partial mechanism**; stopped because converged.

11 chains tie for first: G120 (ARID2), G122 (ARNT, ARNT2), G011 (KLF1, KLF12, KLF2 and 6 more) or 8 more → no target gene named. They differ only in the transcription factor. Predicted only: TF binding. No claim: regulatory activity, target gene, gene to trait, variant to trait. Filled by code from databases and model predictions. A search found no article that names the variant, so none was read. No experiment on file names one of the tied candidates beyond the records the table counts, so nothing read from the articles separates the tied chains.

- Replay: replayable: no model reply was retried, refused or lost, so v2m v9 replay can re-execute the run from this folder's tool results and the saved model replies

---

This page is the top of the run's report. The whole report, with the sentences quoted from the articles, can be rendered from `graph.json.gz` in this folder (see the folder's README).
