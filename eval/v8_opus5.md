# v8 on Claude Opus 5 through the Anthropic API (3 November 2026)

Profile `opus5_v8`: Claude Opus 5 (`claude-opus-5`) in all three roles, called directly through the Anthropic API
(`agent/anthropic_api.py`, `llm.api: anthropic`, key `V2M_ANTHROPIC_API_KEY`), on the 15 cases of the main arm
(`full_given`, repeat 0), with the code as of M1. The settings are Luna's: effort medium for the generator and critic,
low for the summariser, with Opus 5's default adaptive thinking and the strict JSON schemas as structured output.
Spend: $11.19 under a $14 cap ($10 at first, raised after the two-case pilot). Runs: `runs/eval_v8_opus5/`; tables:
`eval/v8_results_opus5.md` and `eval/v8_cases_opus5.md`.

## Results: the same as GPT-6 Luna

- The gold TF is named first at 2/9 TF cases (TCF7L2 and HOXB13), as in Luna's repeat 0 and the code-only baseline:
  all 9 cases tie. The gold family is first at 4/8 covered TF cases and the target gene at 7/9, both as Luna.
- Controls: "no mechanism" overall at 6/6. The TF line says "mechanism" at all 3 near-miss controls, as Luna's does,
  so only the disease line rejects them.
- Against Luna's repeat 0: the same overall verdict at 15/15 cases, the same top TF at 12/15, the same chain TFs at
  12/15 and the same order at 9/15. The three different top TFs are wrong answers or controls: FOXS1 for ONECUT1 at
  rs1421085 (the gold ARID5B has no QBiC-SELEX model), TFAP2E for ZNF696 at rs13078086, and CTCF, code's choice, for
  TCF7L2 at rs73706717.

| Case | Gold TF | Opus 5 | GPT-6 Luna, repeat 0 | Code only | Opus 5: TF line, overall | Cost |
|---|---|---|---|---|---|---|
| tert_c228t | GABPA | E2F1 ✗ | E2F1 ✗ | E2F1 ✗ | mechanism, mechanism | $0.80 |
| tert_c250t | GABPA | E2F1 ✗ | E2F1 ✗ | E2F1 ✗ | mechanism, mechanism | $0.79 |
| rs6983267 | TCF7L2 | TCF7L2 ✓ | TCF7L2 ✓ | TCF7L2 ✓ | mechanism, mechanism | $0.53 |
| rs4784227 | FOXA1 | GATA3 ✗ | GATA3 ✗ | MSX2 ✗ | mechanism, mechanism | $0.69 |
| rs339331 | HOXB13 | HOXB13 ✓ | HOXB13 ✓ | HOXB13 ✓ | mechanism, mechanism | $0.80 |
| rs2168101 | GATA3 | GATA2 ✗ | GATA2 ✗ | GATA2 ✗ | mechanism, mechanism | $0.97 |
| rs12740374 | CEBPA | HNF4A ✗ | HNF4A ✗ | HNF4A ✗ | mechanism, mechanism | $0.87 |
| rs1421085 | ARID5B | FOXS1 ✗ | ONECUT1 ✗ | ONECUT1 ✗ | undetermined, undetermined | $0.78 |
| rs642961 | TFAP2A | TFAP2C ✗ | TFAP2C ✗ | TFAP2C ✗ | undetermined, undetermined | $0.59 |
| rs13078086 | control | TFAP2E | ZNF696 | ZNF696 | no mechanism, no mechanism | $0.52 |
| rs11629191 | control | XBP1 | XBP1 | XBP1 | no mechanism, no mechanism | $0.82 |
| rs7001688 | control | RELA | RELA | RELA | no mechanism, no mechanism | $0.60 |
| rs73706717 | control | CTCF | TCF7L2 | CTCF | mechanism, no mechanism | $0.82 |
| rs34768248 | control | TCF3 | TCF3 | TCF3 | mechanism, no mechanism | $0.88 |
| rs56007086 | control | ESR1 | ESR1 | ESR1 | mechanism, no mechanism | $0.73 |

## Where Opus 5 differs from Luna

- **It overrides code's choice of member.** Opus 5 replaced code's choice in 3 of its 75 chains; Luna never did (0 of
  225 main-arm chains).
  - At rs12740374 it replaced the HMG/SOX chain with C/EBP and named CEBPA, the gold TF, citing the strongest family
    signal (z 22.81) and expression of 141 TPM. Code still ranked CEBPA last of five. CEBPA's ChIP-seq peak in the
    context has no summit within 50 bp of the variant (binding tier 2), while HNF4A has a summit 15 bp away (tier 3),
    and occupancy comes first.
  - At rs1421085 it named PPARG instead of NR4A1 in the nuclear-receptor family, for expression in adipocytes.
  - At rs642961 it replaced the ZNF143 chain with IRF2, for a ChIP peak in keratinocytes.
- **Code rejected 2 of its eliminations**; it rejected none of Luna's. Both cited only rows with status "found": the
  family screen's ChIP counts at rs11629191, and a site-strength percentile at TERT C250T. An elimination needs a
  tested-negative row. Neither rejection changed a verdict.
- **Five generate retries**, against Luna's one in its 15 repeat-0 runs. Each time one chain had a sixth link (a step
  repeated at the end), which the schema check refused; the one retry fixed every case.

## Refusals, cost and time

- No refusals: all 75 calls ended normally, and none reached max_tokens. Claude Opus 5.5, through OpenRouter, was
  stopped by the content filter in both of its pilot runs (`eval/v8_opus55.md`).
- $11.19 for 15 runs: $0.75 per run ($0.52 to $0.97), against Luna's $0.0099, so about 75 times more. 4.0 minutes per
  run, against Luna's 2.2.
- 828,193 input and 281,895 output tokens, 1.8 and 1.4 times Luna's for the same runs. Thinking was 13% of the output
  (36,859 tokens) at medium effort; most of the output is the chains' JSON.
- All 15 runs replay offline from the cache with `v2m replay`, identical apart from seconds and cost.

## What it means

- A stronger model does not change v8's answers. Code's tiers and ordering decide the top TF, so Opus 5 ties Luna and
  the code-only baseline at every case, at 75 times the cost.
- Where the model's judgement reached the gold TF that code had missed (CEBPA at rs12740374), occupancy-first ordering
  undid it. One case is not evidence, but it is the pattern the v9 plan addresses: the model names the lead family and
  member, and code checks that choice instead of re-ranking it.
- Opus 5 runs v8 through the Anthropic API without refusals, so it can be the Claude arm of later evaluations; Opus 5.5
  cannot at present.
