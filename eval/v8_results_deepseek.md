# v8 results (DeepSeek V4.1 Flash)

| arm | who | runs | seeds | strict_top1 | family_top1 | gene_top1 | verdict_correct_tf | lenient_correct_tf | abstain_tf | precision_tf | verdict_correct_controls | overclaim_controls | disease_line_ok | leaks | cost_per_run | minutes_per_run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ablation | agent | 9 | 1 | 0.0 | 0.222 | 0.778 | 0.0 | 0.111 | 0.222 | 0.0 |  |  | 1.0 | 0 | 0.021 | 4.58 |
| ablation | code only | 9 | 1 | 0.0 | 0.222 | 0.667 | 0.0 | 0.111 | 0.222 | 0.0 |  |  | 1.0 | 0 | 0.0 | 0.08 |
| full_given | agent | 44 | 3 | 0.222 | 0.407 | 0.815 | 0.222 | 0.333 | 0.222 | 0.286 | 1.0 | 0.0 | 1.0 | 0 | 0.0166 | 3.63 |
| full_given | code only | 15 | 1 | 0.222 | 0.444 | 0.667 | 0.222 | 0.333 | 0.222 | 0.286 | 1.0 | 0.0 | 1.0 | 0 | 0.0 | 0.06 |
| full_inferred | agent | 15 | 1 | 0.333 | 0.556 | 0.889 | 0.333 | 0.556 | 0.0 | 0.333 | 1.0 | 0.0 | 1.0 | 0 | 0.0239 | 4.29 |
| full_inferred | code only | 15 | 1 | 0.222 | 0.444 | 0.444 | 0.222 | 0.444 | 0.0 | 0.222 | 1.0 | 0.0 | 1.0 | 0 | 0.0 | 0.06 |
| named_given | agent | 15 | 1 | 0.222 | 0.444 | 0.889 | 0.222 | 0.333 | 0.222 | 0.286 | 1.0 | 0.0 | 1.0 | 2 | 0.0225 | 3.88 |
| named_given | code only | 15 | 1 | 0.222 | 0.444 | 0.667 | 0.222 | 0.333 | 0.222 | 0.286 | 1.0 | 0.0 | 1.0 | 2 | 0.0 | 0.06 |
| noqbic_given | agent | 15 | 1 | 0.222 | 0.444 | 0.778 | 0.222 | 0.333 | 0.222 | 0.286 | 1.0 | 0.0 | 1.0 | 0 | 0.0171 | 3.71 |
| noqbic_given | code only | 15 | 1 | 0.111 | 0.333 | 0.667 | 0.111 | 0.222 | 0.222 | 0.143 | 1.0 | 0.0 | 1.0 | 0 | 0.0 | 0.04 |
| single | agent | 15 | 1 | 0.778 | 0.778 |  |  |  |  |  |  |  |  | 0 | 0.0025 | 0.62 |
| single_rules | agent | 14 | 1 | 1.0 | 0.875 |  |  |  |  |  |  |  |  | 0 | 0.0019 | 0.42 |

## Planned comparisons

- agent vs code-only (full, given), verdict_correct: A 0.5 vs B 0.5 over 14 cases; A better in 0, B in 0; sign test p 1.0
- agent vs code-only (full, given), strict_top1: A nan vs B nan over 14 cases; A better in 0, B in 0; sign test p 1.0
- agent vs code-only (full, given), family_top1: A nan vs B nan over 14 cases; A better in 0, B in 1; sign test p 1.0
- full vs no QBiC-SELEX (given), verdict_correct: A 0.5 vs B 0.5 over 14 cases; A better in 1, B in 1; sign test p 1.0
- full vs no QBiC-SELEX (given), strict_top1: A nan vs B nan over 14 cases; A better in 1, B in 1; sign test p 1.0
- full vs no QBiC-SELEX (given), family_top1: A nan vs B nan over 14 cases; A better in 1, B in 2; sign test p 1.0
- given vs inferred context, verdict_correct: A 0.5 vs B 0.571 over 14 cases; A better in 1, B in 2; sign test p 1.0
- given vs inferred context, strict_top1: A nan vs B nan over 14 cases; A better in 1, B in 2; sign test p 1.0
- given vs inferred context, family_top1: A nan vs B nan over 14 cases; A better in 1, B in 3; sign test p 0.625
- masked vs named (real-use reference), verdict_correct: A 0.5 vs B 0.5 over 14 cases; A better in 0, B in 0; sign test p 1.0
- masked vs named (real-use reference), strict_top1: A nan vs B nan over 14 cases; A better in 0, B in 0; sign test p 1.0
- masked vs named (real-use reference), family_top1: A nan vs B nan over 14 cases; A better in 0, B in 1; sign test p 1.0
- full vs ablation (gold TF's rows removed), verdict_correct: A 0.222 vs B 0.0 over 9 cases; A better in 2, B in 0; sign test p 0.5
- full vs ablation (gold TF's rows removed), strict_top1: A 0.222 vs B 0.0 over 9 cases; A better in 2, B in 0; sign test p 0.5
- full vs ablation (gold TF's rows removed), family_top1: A 0.333 vs B 0.222 over 9 cases; A better in 2, B in 1; sign test p 1.0

Best earlier version: v3; v8 better on 1 cases, earlier better on 2 (p 1.0).
Total spend: $1.935 over 196 runs (mean $0.0099).
