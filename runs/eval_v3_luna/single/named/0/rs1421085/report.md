# rs1421085 and Obesity (FTO)

Configuration `single`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 1 model calls; 63 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. H3: Loss of ARID5B repression raises both IRX3 and IRX5 (p = 0.55)

TF ARID5B (QBiC-SELEX coverage not_in_coverage), ref allele binds more; element An intronic FTO-locus enhancer; gene IRX3 and IRX5; cell type Adipocyte progenitors.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is the leading TF based on reported allele-specific binding at this site; the ref T allele binds more strongly than alt C. I do not know of a verified QBiC-SELEX model for ARID5B here. | missing | none |
| element | The variant lies in an intronic enhancer at the FTO locus, and loss of ARID5B binding on C weakens repression of that element. | missing | none |
| gene | The enhancer affects both IRX3 and IRX5, with expression of both genes rising on the C allele. | missing | none |
| cell_type | The effect occurs in adipocyte progenitors, where increased IRX3 and IRX5 jointly shift cells away from thermogenic differentiation. | missing | none |
| phenotype | Reduced thermogenic capacity contributes to increased obesity risk. | missing | none |

Predictions: In isogenic C-allele cells, both IRX3 and IRX5 expression rise.; Restoring ARID5B occupancy or activity at the element reduces expression of both genes.

Falsified if: The C allele does not reduce ARID5B binding in relevant adipocyte progenitors.; Precise T-to-C editing reproducibly changes only one of IRX3 or IRX5, with no effect on the other.

### 2. H1: Loss of ARID5B repression primarily raises IRX3 (p = 0.18)

TF ARID5B (QBiC-SELEX coverage not_in_coverage), ref allele binds more; element An intronic FTO-locus enhancer; gene IRX3; cell type Adipocyte progenitors.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is the leading TF based on reported allele-specific binding at this site; the ref T allele binds more strongly than alt C. I do not know of a verified QBiC-SELEX model for ARID5B here. | missing | none |
| element | The variant lies in an intronic enhancer at the FTO locus, and loss of ARID5B binding on C weakens repression of that element. | missing | none |
| gene | The enhancer's principal affected target is IRX3, whose expression rises on the C allele. | missing | none |
| cell_type | The effect occurs in adipocyte progenitors, where increased IRX3 shifts cells away from thermogenic differentiation. | missing | none |
| phenotype | Reduced thermogenic capacity contributes to increased obesity risk. | missing | none |

Predictions: In isogenic C-allele cells, IRX3 expression rises more consistently than IRX5 expression.; Restoring ARID5B occupancy or activity at the element reduces the IRX3 increase.

Falsified if: The C allele does not reduce ARID5B binding in relevant adipocyte progenitors.; Precise T-to-C editing does not increase IRX3 expression in those cells.

### 3. H0: No TF-mediated effect of rs1421085 (p = 0.15)

Null chain: no TF-mediated effect of this variant.

Predictions: Precise editing of rs1421085 alone produces no reproducible change in IRX3 or IRX5 expression in relevant cells.; Any association with obesity is explained by linkage to another causal variant or by a non-causal association.

Falsified if: Precise editing produces a reproducible allele-dependent effect on TF occupancy and downstream gene expression in relevant cells.

### 4. H2: Loss of ARID5B repression primarily raises IRX5 (p = 0.12)

TF ARID5B (QBiC-SELEX coverage not_in_coverage), ref allele binds more; element An intronic FTO-locus enhancer; gene IRX5; cell type Adipocyte progenitors.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is the leading TF based on reported allele-specific binding at this site; the ref T allele binds more strongly than alt C. I do not know of a verified QBiC-SELEX model for ARID5B here. | missing | none |
| element | The variant lies in an intronic enhancer at the FTO locus, and loss of ARID5B binding on C weakens repression of that element. | missing | none |
| gene | The enhancer's principal affected target is IRX5, whose expression rises on the C allele. | missing | none |
| cell_type | The effect occurs in adipocyte progenitors, where increased IRX5 shifts cells away from thermogenic differentiation. | missing | none |
| phenotype | Reduced thermogenic capacity contributes to increased obesity risk. | missing | none |

Predictions: In isogenic C-allele cells, IRX5 expression rises more consistently than IRX3 expression.; Restoring ARID5B occupancy or activity at the element reduces the IRX5 increase.

Falsified if: The C allele does not reduce ARID5B binding in relevant adipocyte progenitors.; Precise T-to-C editing does not increase IRX5 expression in those cells.

## Prediction matrix

| Test | Cost | Separates top two | H3 | H1 | H0 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Precisely edit T to C in adipocyte progenitors and measure IRX3 and IRX5 RNA by targeted RT-qPCR. | medium | yes | Both IRX3 and IRX5 rise. | IRX3 rises more consistently than IRX5. | Neither gene shows a reproducible edit-dependent change. | IRX5 rises more consistently than IRX3. |
| Measure ARID5B occupancy at the variant in matched T/T and C/C adipocyte progenitors. | medium | no | Occupancy is higher on T than C. | Occupancy is higher on T than C. | No reproducible allele-dependent ARID5B occupancy difference. | Occupancy is higher on T than C. |

## Next experiment

Precisely edit T to C in adipocyte progenitors and use targeted RT-qPCR to measure IRX3 and IRX5. Both increasing supports the highest-probability dual-target chain; an IRX3-selective increase supports the runner-up.

## Flags

- none

## Evidence
