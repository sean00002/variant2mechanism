# v8 results (Claude Opus 5)

Each cell is k/n over runs: every repeat of a case counts once. TF-case columns cover the 9 TF cases and control columns the 6 controls; family_top1 is over the 8 TF cases whose gold TF QBiC-SELEX covers (ARID5B, at rs1421085, has no model). `attempted` counts failed attempts that were run again (`rerun`).

| arm | who | attempted | failed | rerun | runs | repeats | strict_top1 | family_top1 | gene_top1 | verdict_correct_tf | lenient_correct_tf | abstain_tf | precision_tf | verdict_correct_controls | overclaim_controls | tf_line_overclaim_controls | disease_line_ok | leaks | cost_per_run | minutes_per_run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| full_given | agent | 15 | 0 | 0 | 15 | 1 | 2/9 | 4/8 | 7/9 | 2/9 | 3/9 | 2/9 | 2/7 | 6/6 | 0/6 | 3/6 | 15/15 | 0 | 0.7459 | 4.01 |

## Controls: how often each line says "mechanism" (main arm, repeat 0)

- agent, control near miss: TF line 3/3, overall verdict 0/3
- agent, control random: TF line 0/3, overall verdict 0/3
- code only, control near miss: TF line 3/3, overall verdict 0/3
- code only, control random: TF line 0/3, overall verdict 0/3

## Planned comparisons (repeat 0, per case)

- Claude Opus 5 vs GPT-6 Luna (full, given), verdict_correct (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 0, B in 0, tied in 9; sign test p 1.0
- Claude Opus 5 vs GPT-6 Luna (full, given), strict_top1 (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 0, B in 0, tied in 9; sign test p 1.0
- Claude Opus 5 vs GPT-6 Luna (full, given), family_top1 (covered TF cases): A 0.5 vs B 0.5 over 8 cases; A better in 0, B in 0, tied in 8; sign test p 1.0
- Claude Opus 5 vs GPT-6 Luna (full, given), verdict_correct (controls): A 1.0 vs B 1.0 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- Claude Opus 5 vs GPT-6 Luna (full, given), tf_line_overclaim (controls): A 0.5 vs B 0.5 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- agent vs code-only (full, given), verdict_correct (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 0, B in 0, tied in 9; sign test p 1.0
- agent vs code-only (full, given), strict_top1 (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 0, B in 0, tied in 9; sign test p 1.0
- agent vs code-only (full, given), family_top1 (covered TF cases): A 0.5 vs B 0.5 over 8 cases; A better in 0, B in 0, tied in 8; sign test p 1.0
- agent vs code-only (full, given), verdict_correct (controls): A 1.0 vs B 1.0 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- agent vs code-only (full, given), tf_line_overclaim (controls): A 0.5 vs B 0.5 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0

Code only comes from the saved GPT-6 Luna grid: it makes no model call, so it is the same for every model. The earlier versions were Luna grids and are not compared here.

Attempts: 15, completed 15, failed 0; 0 failed attempts were run again.
Total spend: $11.188 over 15 completed runs (mean $0.7459), as each report records it.
