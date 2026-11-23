# Scores of runs/fill_reader_critic_judge_20261122_b against the gold specification

Specification status: unreviewed; every number is provisional until it is reviewed. The rule is in scripts/v9_table_score.py and was fixed before any table of the fill was scored.

"Named" counts a case when a first-ranked chain names the gold answer. "Share" is the matching candidates over the candidates the first-ranked chains name, summed over cases: what picking one candidate from each tie at random would get.

## All gold cases (9)

| Component | Cases it applies to | Named | Share | Named, with the judge | Share, with the judge |
|---|---|---|---|---|---|
| TF, as the member | 9 | 0 | 0.00 | 0 | 0.00 |
| TF, as its group | 8 | 7 | 3.95 | 7 | 4.86 |
| TF, as its family | 8 | 7 | 4.28 | 7 | 4.86 |
| Target gene | 9 | 6 | 4.58 | 6 | 4.58 |
| Both in one chain | 9 | 4 | 2.25 | 4 | 3.17 |
| Trait | 9 | 7 | 7.00 | 7 | 7.00 |

## Without the two cases the earlier engine was built on (7)

| Component | Cases it applies to | Named | Share | Named, with the judge | Share, with the judge |
|---|---|---|---|---|---|
| TF, as the member | 7 | 0 | 0.00 | 0 | 0.00 |
| TF, as its group | 6 | 5 | 3.36 | 5 | 3.36 |
| TF, as its family | 6 | 5 | 3.36 | 5 | 3.36 |
| Target gene | 7 | 5 | 3.58 | 5 | 3.58 |
| Both in one chain | 7 | 3 | 2.17 | 3 | 2.17 |
| Trait | 7 | 6 | 6.00 | 6 | 6.00 |

## Gold cases, one by one

| Case | Chains tied for first | TF candidates | Gene candidates | TF as member | TF as group | Target gene | Both in one chain | Trait | The judge points to | Claims with support (of 8) | Allele claims measured (of 4) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tert_c228t | 8 | 8 | 1 | 0 of 8 | 4 of 8 | 0 of 1 | 0 of 8 | 0 of 1 | - | 3 | 0 |
| tert_c250t | 11 | 11 | 1 | 0 of 11 | 4 of 11 | 0 of 1 | 0 of 11 | 0 of 1 | - | 3 | 0 |
| rs6983267 | 2 | 2 | 1 | 0 of 2 | 1 of 2 | 0 of 1 | 0 of 2 | 1 of 1 | - | 7 | 2 |
| rs4784227 | 6 | 2 | 3 | 0 of 2 | 1 of 2 | 1 of 3 | 1 of 6 | 1 of 1 | - | 6 | 1 |
| rs339331 | 1 | 1 | 1 | 0 of 1 | 1 of 1 | 1 of 1 | 1 of 1 | 1 of 1 | - | 7 | 2 |
| rs2168101 | 1 | 1 | 1 | 0 of 1 | 1 of 1 | 1 of 1 | 1 of 1 | 1 of 1 | - | 7 | 2 |
| rs12740374 | 12 | 12 | 1 | 0 of 12; with the judge 0 of 1 | 1 of 12; with the judge 1 of 1 | 1 of 1 | 1 of 12; with the judge 1 of 1 | 1 of 1 | tf G035 (CEBPA, CEBPB, CEBPE) | 7 | 1 |
| rs1421085 | 12 | 12 | 1 | 0 of 12 | does not apply | 1 of 1 | 0 of 12 | 1 of 1 | - | 7 | 2 |
| rs642961 | 4 | 1 | 4 | 0 of 1 | 0 of 1 | 1 of 4 | 0 of 4 | 1 of 1 | - | 6 | 1 |

## Controls and gold cases, without labels

| Set | Cases | First chain: claims with support, mean of 8 | Cases whose first chain has a measured allele claim |
|---|---|---|---|
| Gold | 9 | 5.9 | 7 |
| Controls | 6 | 3.2 | 1 (rs56007086) |

| Control | Class | Chains tied for first | Claims with support (of 8) | Allele claims measured (of 4) |
|---|---|---|---|---|
| rs13078086 | control_random | 1 | 2 | 0 |
| rs11629191 | control_random | 1 | 2 | 0 |
| rs7001688 | control_random | 316 | 1 | 0 |
| rs73706717 | control_near_miss | 6 | 5 | 0 |
| rs34768248 | control_near_miss | 8 | 6 | 0 |
| rs56007086 | control_near_miss | 1 | 3 | 1 |
