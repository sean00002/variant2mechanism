# Chain tables of 15 saved runs

Runs read from `runs/fill_reader_critic_judge_20261122_b`. Each row is the run's first chain; a chain has 8 claims and 24 cells. "Claims stated" counts the claims a claim of the run states; the others are asked by the table and answered from the run's lookups and the records on file. "Records not judged" counts, over that chain's cells, the records the run holds that name what a claim names and were neither counted, listed beside it nor set aside. "Other rules broken" and the Rules table at the end count every chain of the run.

| Run | Chains (tied first) | Claims stated | With support | Supports | Disagrees or both | Nothing found | Not checked | No source | Records not judged | Other rules broken |
|---|---|---|---|---|---|---|---|---|---|---|
| rs11629191 | 324 (1) | 2 of 8 | 2 | 2 | 0 | 16 | 0 | 6 | 0 | 0 |
| rs12740374 | 8372 (12) | 7 of 8 | 7 | 10 | 0 | 8 | 0 | 6 | 0 | 0 |
| rs13078086 | 174 (1) | 2 of 8 | 2 | 2 | 0 | 16 | 0 | 6 | 0 | 0 |
| rs1421085 | 2750 (12) | 7 of 8 | 7 | 9 | 0 | 9 | 0 | 6 | 0 | 0 |
| rs2168101 | 681 (1) | 7 of 8 | 7 | 11 | 0 | 7 | 0 | 6 | 0 | 0 |
| rs339331 | 4344 (1) | 7 of 8 | 7 | 12 | 0 | 6 | 0 | 6 | 0 | 0 |
| rs34768248 | 687 (8) | 6 of 8 | 6 | 6 | 0 | 12 | 0 | 6 | 0 | 0 |
| rs4784227 | 522 (6) | 6 of 8 | 6 | 11 | 0 | 7 | 0 | 6 | 0 | 0 |
| rs56007086 | 430 (1) | 3 of 8 | 3 | 4 | 0 | 14 | 0 | 6 | 0 | 0 |
| rs642961 | 705 (4) | 6 of 8 | 6 | 7 | 0 | 10 | 0 | 7 | 0 | 0 |
| rs6983267 | 1392 (2) | 7 of 8 | 7 | 9 | 0 | 9 | 0 | 6 | 0 | 0 |
| rs7001688 | 316 (316) | 1 of 8 | 1 | 1 | 0 | 17 | 0 | 6 | 0 | 0 |
| rs73706717 | 217 (6) | 5 of 8 | 5 | 5 | 0 | 13 | 0 | 6 | 0 | 0 |
| tert_c228t | 230 (8) | 3 of 8 | 3 | 3 | 0 | 15 | 0 | 6 | 0 | 0 |
| tert_c250t | 350 (11) | 3 of 8 | 3 | 3 | 0 | 15 | 0 | 6 | 0 | 0 |
| **All 15** | | 72 of 120 | 72 | 95 | 0 | 174 | 0 | 91 | 0 | 0 |

## By kind of claim

| Claims | Stated by the run | With support |
|---|---|---|
| The alleles differ | 36 of 60 | 36 of 60 |
| The parts are in place | 36 of 60 | 36 of 60 |

## By claim

| Claim | Stated by the run | With support | Strongest kind of record, by run count |
|---|---|---|---|
| TF binding: alleles differ | 15 of 15 | 15 | prediction 9, assay 6 |
| TF binding: in place | 14 of 15 | 14 | recorded 14, none 1 |
| Regulatory activity: alleles differ | 4 of 15 | 4 | none 11, assay 4 |
| Regulatory activity: in place | 12 of 15 | 12 | recorded 12, none 3 |
| Target gene: alleles differ | 8 of 15 | 8 | none 7, association 6, edit 2 |
| Target gene: in place | 1 of 15 | 1 | none 14, edit 1 |
| Trait: alleles differ | 9 of 15 | 9 | association 9, none 6 |
| Trait: in place | 9 of 15 | 9 | none 6, association 6, edit 2, prediction 1 |

## By cell

The first chain's cells over the runs.

| Claim | Database | Model prediction | Literature |
|---|---|---|---|
| TF binding: alleles differ | supports 4, nothing found 11 | supports 14, no source 1 | supports 4, nothing found 11 |
| TF binding: in place | supports 13, nothing found 2 | no source 15 | supports 4, nothing found 11 |
| Regulatory activity: alleles differ | supports 2, nothing found 13 | no source 15 | supports 4, nothing found 11 |
| Regulatory activity: in place | supports 12, nothing found 3 | no source 15 | nothing found 15 |
| Target gene: alleles differ | supports 7, nothing found 8 | no source 15 | supports 5, nothing found 10 |
| Target gene: in place | nothing found 15 | no source 15 | supports 1, nothing found 14 |
| Trait: alleles differ | supports 9, nothing found 6 | no source 15 | nothing found 15 |
| Trait: in place | supports 7, nothing found 8 | supports 7, nothing found 8 | supports 2, nothing found 13 |

## By kind of record

| Kind | Cells with a source | Cells with support |
|---|---|---|
| Database | 120 | 54 |
| Model prediction | 30 | 21 |
| Literature | 120 | 20 |

## Records on file and records used

| Source | Records on file | Counted for a claim | Listed beside a claim |
|---|---|---|---|
| `qbic_inventory` | 4109 | 4109 | 0 |
| `tf_occupancy_set` | 2923 | 2923 | 0 |
| `credible_sets_all` | 2328 | 2328 | 0 |
| `gwas_associations` | 1114 | 1114 | 0 |
| `ccre_overlap` | 434 | 70 | 0 |
| `literature_read` | 166 | 58 | 2 |
| `gene_disease` | 75 | 75 | 0 |
| `gtex_eqtl` | 60 | 60 | 0 |
| `variant_annotation` | 38 | 9 | 0 |
| `adastra_asb` | 7 | 7 | 0 |
| **All** | 11254 | 10753 | 2 |

## Literature: from searches to records

| Run | Searches | Reads | Articles read | Reads of an article already read | Experiments filed or refused | Accepted | Linked to a claim |
|---|---|---|---|---|---|---|---|
| rs11629191 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs12740374 | 2 | 17 | 17 | 0 | 38 | 25 | 6 |
| rs13078086 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs1421085 | 2 | 12 | 12 | 0 | 54 | 35 | 7 |
| rs2168101 | 2 | 10 | 10 | 0 | 18 | 9 | 6 |
| rs339331 | 2 | 12 | 12 | 0 | 77 | 65 | 28 |
| rs34768248 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs4784227 | 2 | 11 | 11 | 0 | 25 | 4 | 4 |
| rs56007086 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs642961 | 2 | 16 | 16 | 0 | 10 | 6 | 2 |
| rs6983267 | 2 | 16 | 16 | 0 | 35 | 22 | 7 |
| rs7001688 | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs73706717 | 2 | 1 | 1 | 0 | 1 | 0 | 0 |
| tert_c228t | 2 | 3 | 3 | 0 | 4 | 0 | 0 |
| tert_c250t | 2 | 0 | 0 | 0 | 0 | 0 | 0 |
| **All 15** | 30 | 98 | 98 | 0 | 262 | 166 | 60 |

## The reader: what became of the articles found

Code searched for the variant's names and a model read each article once. "Read by the model" is also the number of model calls. An experiment the model returned is filed as a record only when code finds its sentences in the article and its fields agree with the text.

| Run | Articles found | Read by the model | Sent back once for its pointers | Variant not named in the text | Reviews | Text not retrieved | Model call failed | Beyond the cap | Experiments returned | Filed as records |
|---|---|---|---|---|---|---|---|---|---|---|
| rs11629191 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs12740374 | 18 | 15 | 1 | 2 | 1 | 0 | 0 | 0 | 38 | 25 |
| rs13078086 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs1421085 | 19 | 9 | 2 | 3 | 7 | 0 | 0 | 0 | 54 | 35 |
| rs2168101 | 19 | 8 | 1 | 2 | 6 | 3 | 0 | 0 | 18 | 9 |
| rs339331 | 17 | 12 | 3 | 0 | 4 | 1 | 0 | 0 | 77 | 65 |
| rs34768248 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs4784227 | 18 | 11 | 1 | 0 | 7 | 0 | 0 | 0 | 25 | 4 |
| rs56007086 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs642961 | 19 | 14 | 1 | 2 | 3 | 0 | 0 | 0 | 10 | 6 |
| rs6983267 | 19 | 14 | 2 | 2 | 3 | 0 | 0 | 0 | 35 | 22 |
| rs7001688 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs73706717 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| tert_c228t | 4 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 4 | 0 |
| tert_c250t | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **All 15** | 134 | 87 | 11 | 11 | 32 | 4 | 0 | 0 | 262 | 166 |

## The critic: a second reading of what would be counted

Before the experiments from articles are linked, a second model from another provider reads each one that would be the only record counted for, or against, some claim: its quotation in its paragraph, against each claim code would count it for. An experiment with another record beside it under every such claim is not sent, because no answer on it could change a cell (a run made before 22 November 2026 sent every experiment, and shows none in that column). "Read by the critic" is also the number of its model calls. A claim it answers "not shown" does not get the record. With "shown" it may name further sentences of the paragraph as the ones that state the result, and code copies them into the quotation. It can add no record.

| Run | Experiments up for counting | Not alone behind a claim: not sent | Read by the critic | Call failed | Beyond the cap | Alone and not read | Claims checked | Shown | Shown, quotation extended | Not shown | Cannot tell | Experiments counted for nothing after it |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rs11629191 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs12740374 | 6 | 1 | 5 | 0 | 0 | 0 | 10 | 10 | 0 | 0 | 0 | 0 |
| rs13078086 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs1421085 | 7 | 5 | 2 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 |
| rs2168101 | 6 | 4 | 2 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 |
| rs339331 | 28 | 27 | 1 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 1 | 0 |
| rs34768248 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs4784227 | 4 | 0 | 4 | 0 | 0 | 0 | 6 | 6 | 0 | 0 | 0 | 0 |
| rs56007086 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs642961 | 2 | 0 | 2 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 |
| rs6983267 | 7 | 3 | 4 | 0 | 0 | 0 | 5 | 5 | 0 | 0 | 0 | 0 |
| rs7001688 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| rs73706717 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| tert_c228t | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| tert_c250t | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **All 15** | 60 | 40 | 20 | 0 | 0 | 0 | 30 | 29 | 0 | 0 | 1 | 0 |

## The judge: reading a tie for first

Where chains tie for first, code lists the TFs and genes they differ in and, for each, the experiments read from articles that name it and that no cell counts for it. A second model reads them and says for each candidate whether an experiment ties it to the variant's site. It is asked twice, with the candidates in opposite orders and one made-up candidate among them; only an answer both readings give is kept, and nothing is kept from a tie where a reading accepts the made-up candidate. No cell, rank or count of tied chains changes. A run with one leading chain is not listed.

| Run | Chains tied for first | Tied TFs and genes | With experiments no cell counts | Read by the judge | Experiments read | Readings (orders) | Tied to the site | An experiment changed nothing | Not tied | Cannot tell | Readings disagreed | Made-up candidate accepted | No answer | Points to | Points away from | Undecided |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rs12740374 | 12 | 12 | 1 | 1 | 7 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | TF G035 (CEBPA, CEBPB, CEBPE) | - | - |
| rs1421085 | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - | - |
| rs34768248 | 8 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - | - |
| rs4784227 | 6 | 5 | 1 | 1 | 2 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | - | - | - |
| rs642961 | 4 | 4 | 1 | 1 | 2 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | - | - | gene IRF6 |
| rs6983267 | 2 | 2 | 1 | 1 | 4 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | - | - | - |
| rs7001688 | 316 | 316 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - | - |
| rs73706717 | 6 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - | - |
| tert_c228t | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - | - |
| tert_c250t | 11 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | - | - | - |

## Rules

| Rule | Times broken | What it says |
|---|---|---|
| shape | 0 | Every chain has its four steps, each with both claims; every claim has three cells; every cell is in one of the six states. |
| record | 0 | A cell that reports support or disagreement cites its records, and no other cell counts any. Each record is in the run's files, of the cell's kind, and from a source the map lists for that cell. |
| variant | 0 | A record counted for a claim that the alleles differ names this variant. |
| looked | 0 | "Nothing found" cites a lookup that completed. "No source" appears only where the map has no source, or says why this claim has none. |
| unjudged | 0 | No record on file that names the claim's TF, element, gene or trait is left without a judgement: it is counted in the cell, listed beside it, or set aside with a reason. |
| quoted | 0 | A literature record carries the passage it was read from and the article it came from. |
