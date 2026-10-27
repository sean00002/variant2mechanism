# rs6983267 and Colorectal cancer (8q24)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 19 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. chain1: TCF7L2-bound ref G enhancer activates MYC (p = 0.45)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element 8q24 enhancer containing rs6983267; gene MYC; cell type HCT116 colorectal carcinoma cells / colon epithelial lineage.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2, selected within the TCF/LEF QBiC-SELEX specificity group using colon/HCT116 expression and known Wnt/TCF biology, binds the ref G allele more strongly than alt T at rs6983267; QBiC-SELEX coverage not_checked. | missing | none |
| element | The variant lies in a distal 8q24 enhancer whose activity is higher on the ref G allele. | missing | none |
| gene | The ref G enhancer increases MYC expression. | missing | none |
| cell_type | This occurs in colorectal carcinoma cells such as HCT116, consistent with the stated expression context. | missing | none |
| phenotype | Increased MYC expression raises colorectal cancer risk. | missing | none |

Predictions: ref G shows stronger TCF7L2 binding than alt T; ref G shows higher enhancer activity than alt T; ref G associates with higher MYC expression in HCT116; knockdown of TCF7L2 reduces the allele-specific enhancer effect

Falsified if: Allele-specific TCF7L2 binding is absent or alt T binds TCF7L2 more strongly.; The rs6983267 region does not show allele-dependent enhancer activity in HCT116 cells.; MYC is not affected by the rs6983267 enhancer in colorectal cells.

### 2. null: No TF-mediated effect of rs6983267 (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs6983267; No allele-specific enhancer activity attributable to rs6983267; Any association with MYC or colorectal cancer is due to a linked causal variant or another non-TF mechanism

Falsified if: Allele-specific TF binding and enhancer activity at rs6983267 are demonstrated in HCT116 cells.; MYC expression is shown to be causally affected by the rs6983267 allele.

### 3. chain2: TCF7L2-bound alt T enhancer activates MYC (p = 0.20)

TF TCF7L2 (stated coverage not_checked; registry mapped), alt allele binds more; element 8q24 enhancer containing rs6983267; gene MYC; cell type HCT116 colorectal carcinoma cells / colon epithelial lineage.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2, selected within the TCF/LEF QBiC-SELEX specificity group, binds the alt T allele more strongly than ref G at rs6983267; QBiC-SELEX coverage not_checked. | missing | none |
| element | The rs6983267 alt T allele creates a stronger 8q24 enhancer in colorectal cells. | missing | none |
| gene | The alt T enhancer increases MYC expression. | missing | none |
| cell_type | This occurs in HCT116 colorectal carcinoma cells. | missing | none |
| phenotype | Higher MYC expression raises colorectal cancer risk. | missing | none |

Predictions: alt T shows stronger TCF7L2 binding than ref G; alt T shows higher enhancer activity than ref G; alt T associates with higher MYC expression in HCT116; TCF7L2 knockdown reduces the alt T-specific enhancer effect

Falsified if: TCF7L2 binds ref G more strongly than alt T.; Alt T does not increase enhancer activity or MYC expression.; TCF7L2 knockdown does not change the alt T-specific effect.

### 4. chain3: LEF1-bound ref G enhancer activates MYC (p = 0.10)

TF LEF1 (stated coverage not_checked; registry own_model), ref allele binds more; element 8q24 enhancer containing rs6983267; gene MYC; cell type HCT116 colorectal carcinoma cells / colon epithelial lineage.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | LEF1, another TCF/LEF family factor, binds the ref G allele more strongly than alt T at rs6983267; QBiC-SELEX coverage not_checked. This chain is less favored because TCF7L2 is the better-supported colorectal Wnt factor. | missing | none |
| element | The ref G allele increases 8q24 enhancer activity through LEF1. | missing | none |
| gene | LEF1-bound enhancer activity increases MYC expression. | missing | none |
| cell_type | This occurs in HCT116 colorectal carcinoma cells. | missing | none |
| phenotype | Increased MYC expression raises colorectal cancer risk. | missing | none |

Predictions: LEF1, not TCF7L2, shows the stronger allele-specific binding; LEF1 knockdown reduces enhancer activity and MYC expression; ref G shows higher enhancer activity than alt T

Falsified if: LEF1 does not bind the rs6983267 region allele-specifically in HCT116 cells.; The enhancer effect is not LEF1-dependent.; MYC is not the target gene.

## Prediction matrix

| Test | Cost | Separates top two | chain1 | null | chain2 | chain3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 EMSA with ref G and alt T probes using HCT116 nuclear extract, with anti-TCF7L2 supershift | low | yes | ref G > alt T TCF7L2 binding supports chain1 | no allele-specific binding supports null | alt T > ref G TCF7L2 binding supports chain2 |  |

## Next experiment

Cheapest single experiment separating chain1 from the null: allele-specific TCF7L2 EMSA using ref G and alt T probes with HCT116 nuclear extract and anti-TCF7L2 supershift. If ref G binds TCF7L2 more strongly, chain1 is supported and the null and opposite-direction chain2 are disfavored; if there is no allele-specific binding, the null is favored. A follow-up luciferase/reporter assay would test enhancer activity rather than binding alone.

## Flags

- none

## Evidence
