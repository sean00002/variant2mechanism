# v8 on Claude Opus 5.5 (3 November 2026)

Profile `opus55_v8`: Claude Opus 5.5 in all three roles, through OpenRouter (served by "Claude Platform on AWS"), on
the same 15 cases as the GPT-6 Luna grid, with the code as of M1. Spend: $0.52, under a $12 cap. Runs:
`runs/eval_v8_opus55/`; tables: `eval/v8_results_opus55.md`.

## Main arm: stopped by the content filter

- A two-case pilot of the main arm (`full_given`, repeat 0) stopped both times with the finish reason
  `content_filter`: rs339331 at the generate stage, after 1,170 output tokens; TERT C228T at the critique stage,
  after 632 (its generate stage had finished). The two runs cost $0.22 and left `error.json` and `trace.jsonl`.
- The other 13 cases were not run. The stopped runs were not retried, and the prompts were not changed to get past
  the filter.
- The earlier agent met the same filter on 25 October (`config.yaml`, profile `claude`: Opus 5.5 "declined the
  revise stage twice"), which is why that profile uses Opus 5.

## Memory test: 15 of 15 completed

- With no tools, no evidence and the rsID masked, Opus 5.5 names the gold TF first at 9/9 TF cases, as Luna does. Its
  top TF is the same as Luna's at all 15 cases, controls included.
- It writes the masked rsID in its reasons at all 7 TF cases that have one (rs6983267, rs4784227, rs339331,
  rs2168101, rs12740374, rs1421085, rs642961) and at none of the 6 controls. Luna does so at 1 of 13. The coordinates
  and the disease identify a famous variant whether or not its rsID is shown.
- $0.020 per run, against Luna's $0.0009.

## What it means

- As it stands, Opus 5.5 cannot run the v8 workflow through OpenRouter: the filter stops the generator or the critic
  part-way through.
- On these 15 cases the stronger model knows exactly what the weaker one knows, so the development set cannot
  separate models by what their tools add. That needs cases published after the models' training data, or anonymous
  variants.
