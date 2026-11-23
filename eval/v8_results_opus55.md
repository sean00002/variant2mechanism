# v8 results (Claude Opus 5.5)

Each cell is k/n over runs: every repeat of a case counts once. TF-case columns cover the 9 TF cases and control columns the 6 controls; family_top1 is over the 8 TF cases whose gold TF QBiC-SELEX covers (ARID5B, at rs1421085, has no model). `attempted` counts failed attempts that were run again (`rerun`).

| arm | who | attempted | failed | rerun | runs | repeats | strict_top1 | family_top1 | gene_top1 | verdict_correct_tf | lenient_correct_tf | abstain_tf | precision_tf | verdict_correct_controls | overclaim_controls | tf_line_overclaim_controls | disease_line_ok | leaks | cost_per_run | minutes_per_run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| full_given | agent | 2 | 2 | 0 | 0 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| single | agent | 15 | 0 | 0 | 15 | 1 | 9/9 | 8/8 |  |  |  |  |  |  |  |  |  | 0 | 0.0198 | 0.21 |

## Controls: how often each line says "mechanism" (main arm, repeat 0)

- code only, control near miss: TF line 3/3, overall verdict 0/3
- code only, control random: TF line 0/3, overall verdict 0/3

## Planned comparisons (repeat 0, per case)


Memory test (no tools, no evidence): gold TF named first in 9/9 TF cases, its family in 9/9, anywhere in the list in 9/9.

Code only comes from the saved GPT-6 Luna grid: it makes no model call, so it is the same for every model. The earlier versions were Luna grids and are not compared here.

Attempts: 17, completed 15, failed 2; 0 failed attempts were run again.
Total spend: $0.296 over 15 completed runs (mean $0.0198), as each report records it.
