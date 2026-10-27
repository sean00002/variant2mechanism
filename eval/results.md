# Results

Draft, 25 October 2026. The named `single` and `no_qbic` runs have not been made yet; their results, the
calibration plot and the case reports go here at checkpoint 6.

## Own and mapped QBiC-SELEX models

**The question.** Many TFs have a QBiC-SELEX model of their own and also CIS-BP-mapped models (models of related
TFs with a similar DNA-binding domain). A mapped model is sometimes the better-validated one. Should the workflow
use it for that TF?

**What the workflow does now.**

- `qbic_coverage` records provenance only: `own_model` if the TF has a model of its own (even when a mapped model is
  better), `mapped` if it has only mapped models, `not_in_coverage` otherwise.
- The screen groups models by CIS-BP group and shows each group's best model by |z|, which may be a mapped model.
  Model quality is not used to choose.
- `qbic_tf_detail` returns a TF's own and mapped models together (up to 10; the rest are counted), each with its
  quality, effect, z, gate result and site strength. The prompts do not say how to weigh them.

Reproduce everything below with `uv run python scripts/own_vs_mapped.py` (offline: Table S6 and the committed
QBiC-SELEX cache).

### 1. Model quality in the primary collection

478 TFs have their own model and CIS-BP-mapped models. A mapped model has the higher cross-experiment r in 369 of
them (77%), and is higher by more than 0.05 in 266. For example: GABPA's own model 0.66 against ELK4 0.92; FOXA1's
0.78 against FOXA3 0.93; GATA3's 0.86 against GATA6 0.94.

Cross-experiment r measures each model on its own TF's data, so it does not say how well a mapped model stands in
for another TF.

### 2. SNP-SELEX

Table S6 gives SNP-SELEX Pearson r for the secondary collection: 243 models, none of them in the primary
collection. Per TF that has its own model and at least one mapped model scored:

| | First batch | Novel batch |
|---|---|---|
| TFs | 64 | 116 |
| Mapped models per TF, median | 4 | 6 |
| Own model, median r | 0.60 | 0.49 |
| Mapped models, median r | 0.63 | 0.56 |
| Median mapped model beats own | 53% | 47% |
| Highest-quality mapped model beats own | 48% (Wilcoxon p 0.71) | 47% (Wilcoxon p 0.35) |
| Best mapped model, chosen after the fact, beats own | 75% | 75% |
| Spearman, model quality vs SNP-SELEX r (all rows) | 0.39 | 0.31 |

For three TFs in four, some mapped model predicts the TF's allelic binding better than its own model. But choosing
that model by quality is a coin flip, because quality is only weakly related to SNP-SELEX performance. The 75% is
optimistic: it is the best of about 4 to 6 noisy values.

Two limits: these are secondary-collection models, not the primary ones the workflow uses; and the table holds
per-model correlations, so it cannot say whether combining own and mapped models beats the own model alone.

### 3. The gold set

Own and mapped models at each gold variant, from the cache:

| Case | TF | Label | Own model | Mapped models | Passing models agreeing with the label | Highest-quality model |
|---|---|---|---|---|---|---|
| tert_c228t | GABPA | alt | z +68.5, quality 0.66 | 9 (+8 not shown), 9 pass | 10 of 10 | ELK4 (0.92): z +56.2 |
| tert_c250t | GABPA | alt | z +71.3, quality 0.66 | 9 (+8 not shown), 9 pass | 10 of 10 | ELK4 (0.92): z +62.1 |
| rs6983267 | TCF7L2 | ref | none | 3, 2 pass | 2 of 2 | TCF7 (0.73): z -4.6 |
| rs4784227 | FOXA1 | alt | z +9.3, quality 0.78 | 3, 1 pass | 2 of 2 | FOXA3 (0.93): z +1.9, fails the gate |
| rs339331 | HOXB13 | ref | z -103.5, quality 0.91 | 3, 3 pass | 4 of 4 | HOXB13 (0.91): z -103.5 |
| rs2168101 | GATA3 | ref | z -54.1, quality 0.86 | 5, 5 pass | 6 of 6 | GATA6 (0.94): z -53.7 |
| rs12740374 | CEBPA | alt | z +22.6, quality 0.95 | 2, 2 pass | 3 of 3 | CEBPA (0.95): z +22.6 |
| rs1421085 | ARID5B | ref | none: not in coverage | | | |
| rs642961 | TFAP2A | alt | z +11.9, quality 0.93 | 3, 3 pass | 4 of 4 | TCFAP2A (0.93): z +11.9 |

In all 8 covered cases, every passing model, own or mapped, agrees with the labelled direction. Adding mapped models
would add support but would not change any direction call here. FOXA1 shows the risk of choosing by quality: its
highest-quality model, FOXA3, fails the gate at rs4784227, while FOXA2 (z +15.4) and FOXA1's own model (z +9.3)
pass. "Not shown" counts the models `qbic_tf_detail` trims to stay within its size limit.

### Decision

Frozen as it is for this evaluation (decided on 25 October 2026). A change to the tool output or the
prompts would mean repeating the full runs, and on this gold set it would change no direction call. Scoring each TF
on a panel of its own and mapped models is the next design step (README, "Next steps").
