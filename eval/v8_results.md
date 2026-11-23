# v8 results (GPT-6 Luna)

Each cell is k/n over runs: every repeat of a case counts once. TF-case columns cover the 9 TF cases and control columns the 6 controls; family_top1 is over the 8 TF cases whose gold TF QBiC-SELEX covers (ARID5B, at rs1421085, has no model). `attempted` counts failed attempts that were run again (`rerun`).

| arm | who | attempted | failed | rerun | runs | repeats | strict_top1 | family_top1 | gene_top1 | verdict_correct_tf | lenient_correct_tf | abstain_tf | precision_tf | verdict_correct_controls | overclaim_controls | tf_line_overclaim_controls | disease_line_ok | leaks | cost_per_run | minutes_per_run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ablation | agent | 11 | 0 | 2 | 9 | 1 | 0/9 | 2/8 | 7/9 | 0/9 | 1/9 | 2/9 | 0/7 |  |  |  | 9/9 | 0 | 0.0109 | 2.22 |
| ablation | code only | 9 | 0 | 0 | 9 | 1 | 0/9 | 2/8 | 6/9 | 0/9 | 1/9 | 2/9 | 0/7 |  |  |  | 9/9 | 0 | 0.0 | 0.04 |
| full_given | agent | 45 | 0 | 0 | 45 | 3 | 6/27 | 12/24 | 21/27 | 6/27 | 9/27 | 6/27 | 6/21 | 18/18 | 0/18 | 9/18 | 45/45 | 0 | 0.0099 | 2.22 |
| full_given | code only | 15 | 0 | 0 | 15 | 1 | 2/9 | 4/8 | 6/9 | 2/9 | 3/9 | 2/9 | 2/7 | 6/6 | 0/6 | 3/6 | 15/15 | 0 | 0.0 | 0.03 |
| full_inferred | agent | 15 | 0 | 0 | 15 | 1 | 3/9 | 4/8 | 7/9 | 3/9 | 4/9 | 0/9 | 3/9 | 6/6 | 0/6 | 3/6 | 15/15 | 0 | 0.0105 | 2.11 |
| full_inferred | code only | 15 | 0 | 0 | 15 | 1 | 2/9 | 4/8 | 4/9 | 2/9 | 4/9 | 0/9 | 2/9 | 6/6 | 0/6 | 3/6 | 15/15 | 0 | 0.0 | 0.03 |
| named_given | agent | 15 | 0 | 0 | 15 | 1 | 2/9 | 4/8 | 8/9 | 2/9 | 3/9 | 2/9 | 2/7 | 6/6 | 0/6 | 3/6 | 15/15 | 2 | 0.0112 | 2.38 |
| named_given | code only | 15 | 0 | 0 | 15 | 1 | 2/9 | 4/8 | 6/9 | 2/9 | 3/9 | 2/9 | 2/7 | 6/6 | 0/6 | 3/6 | 15/15 | 2 | 0.0 | 0.04 |
| noqbic_given | agent | 15 | 0 | 0 | 15 | 1 | 2/9 | 4/8 | 8/9 | 2/9 | 3/9 | 2/9 | 2/7 | 6/6 | 0/6 | 2/6 | 15/15 | 0 | 0.0093 | 2.15 |
| noqbic_given | code only | 15 | 0 | 0 | 15 | 1 | 1/9 | 3/8 | 6/9 | 1/9 | 2/9 | 2/9 | 1/7 | 6/6 | 0/6 | 2/6 | 15/15 | 0 | 0.0 | 0.02 |
| single | agent | 17 | 0 | 2 | 15 | 1 | 9/9 | 8/8 |  |  |  |  |  |  |  |  |  | 0 | 0.0009 | 0.33 |
| single_rules | agent | 15 | 0 | 0 | 15 | 1 | 2/9 | 2/8 |  |  |  |  |  |  |  |  |  | 0 | 0.0004 | 0.12 |

## Controls: how often each line says "mechanism" (main arm, repeat 0)

- agent, control near miss: TF line 3/3, overall verdict 0/3
- agent, control random: TF line 0/3, overall verdict 0/3
- code only, control near miss: TF line 3/3, overall verdict 0/3
- code only, control random: TF line 0/3, overall verdict 0/3

## Planned comparisons (repeat 0, per case)

- agent vs code-only (full, given), verdict_correct (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 0, B in 0, tied in 9; sign test p 1.0
- agent vs code-only (full, given), strict_top1 (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 0, B in 0, tied in 9; sign test p 1.0
- agent vs code-only (full, given), family_top1 (covered TF cases): A 0.5 vs B 0.5 over 8 cases; A better in 0, B in 0, tied in 8; sign test p 1.0
- agent vs code-only (full, given), verdict_correct (controls): A 1.0 vs B 1.0 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- agent vs code-only (full, given), tf_line_overclaim (controls): A 0.5 vs B 0.5 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- full vs no QBiC-SELEX (given), verdict_correct (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 1, B in 1, tied in 7; sign test p 1.0
- full vs no QBiC-SELEX (given), strict_top1 (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 1, B in 1, tied in 7; sign test p 1.0
- full vs no QBiC-SELEX (given), family_top1 (covered TF cases): A 0.5 vs B 0.5 over 8 cases; A better in 1, B in 1, tied in 6; sign test p 1.0
- full vs no QBiC-SELEX (given), verdict_correct (controls): A 1.0 vs B 1.0 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- full vs no QBiC-SELEX (given), tf_line_overclaim (controls): A 0.5 vs B 0.333 over 6 cases; A better in 1, B in 0, tied in 5; sign test p 1.0
- given vs inferred context, verdict_correct (TF cases): A 0.222 vs B 0.333 over 9 cases; A better in 1, B in 2, tied in 6; sign test p 1.0
- given vs inferred context, strict_top1 (TF cases): A 0.222 vs B 0.333 over 9 cases; A better in 1, B in 2, tied in 6; sign test p 1.0
- given vs inferred context, family_top1 (covered TF cases): A 0.5 vs B 0.5 over 8 cases; A better in 2, B in 2, tied in 4; sign test p 1.0
- given vs inferred context, verdict_correct (controls): A 1.0 vs B 1.0 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- given vs inferred context, tf_line_overclaim (controls): A 0.5 vs B 0.5 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- masked vs named (real-use reference), verdict_correct (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 0, B in 0, tied in 9; sign test p 1.0
- masked vs named (real-use reference), strict_top1 (TF cases): A 0.222 vs B 0.222 over 9 cases; A better in 0, B in 0, tied in 9; sign test p 1.0
- masked vs named (real-use reference), family_top1 (covered TF cases): A 0.5 vs B 0.5 over 8 cases; A better in 0, B in 0, tied in 8; sign test p 1.0
- masked vs named (real-use reference), verdict_correct (controls): A 1.0 vs B 1.0 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- masked vs named (real-use reference), tf_line_overclaim (controls): A 0.5 vs B 0.5 over 6 cases; A better in 0, B in 0, tied in 6; sign test p 1.0
- full vs ablation (gold TF's rows removed), verdict_correct (TF cases): A 0.222 vs B 0.0 over 9 cases; A better in 2, B in 0, tied in 7; sign test p 0.5
- full vs ablation (gold TF's rows removed), strict_top1 (TF cases): A 0.222 vs B 0.0 over 9 cases; A better in 2, B in 0, tied in 7; sign test p 0.5
- full vs ablation (gold TF's rows removed), family_top1 (covered TF cases): A 0.5 vs B 0.25 over 8 cases; A better in 2, B in 0, tied in 6; sign test p 0.5

Memory test (no tools, no evidence): gold TF named first in 9/9 TF cases, its family in 9/9, anywhere in the list in 9/9.

Best earlier version: v3; v8 better on 1 cases, earlier better on 0 (p 1.0).
Attempts: 202, completed 198, failed 0; 4 failed attempts were run again.
Total spend: $1.026 over 198 completed runs (mean $0.0052), as each report records it.
