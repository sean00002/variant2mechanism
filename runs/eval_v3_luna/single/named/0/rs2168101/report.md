# rs2168101 and Neuroblastoma (LMO1)

Configuration `single`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 1 model calls; 67 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. H1: Alt allele creates a GATA3-responsive LMO1 enhancer (p = 0.65)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in a cis-regulatory element that acts as an enhancer.; gene LMO1; cell type Neuroblastoma cells, including SK-N-SH..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is the leading TF candidate; alt A corresponds to T on the opposite strand, the allele reported to create a GATA3-binding site. No QBiC-SELEX result is supplied here. | missing | none |
| element | Greater GATA3 binding at alt A increases activity of the variant-containing enhancer. | missing | none |
| gene | The enhancer increases LMO1 expression. | missing | none |
| cell_type | This effect occurs in neuroblastoma cells such as SK-N-SH, where LMO1 can contribute to tumor biology. | missing | none |
| phenotype | Increased LMO1 expression raises neuroblastoma susceptibility. | missing | none |

Predictions: An alt-A enhancer reporter has greater activity than a ref-C reporter in SK-N-SH cells.; Changing alt A to ref C reduces LMO1 expression; reducing GATA3 should weaken the allelic difference.

Falsified if: Matched ref-C and alt-A reporters show no reproducible activity difference.; Editing alt A to ref C does not reduce LMO1 expression in an appropriate neuroblastoma model.

### 2. H0: Null: no TF-mediated effect of this variant (p = 0.22)

Null chain: no TF-mediated effect of this variant.

Predictions: Ref-C and alt-A constructs show no reproducible difference in enhancer activity.; Editing this base does not produce a consistent change in LMO1 expression; any association could reflect linkage or another cause.

Falsified if: A reproducible allele-dependent effect is observed in an appropriate cellular assay and is linked to TF occupancy or perturbation.

### 3. H2: GATA3 binding represses the LMO1 enhancer (p = 0.08)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant-containing element is a GATA3-responsive enhancer whose activity is repressed by GATA3.; gene LMO1; cell type Neuroblastoma cells, including SK-N-SH..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is the candidate TF, and alt A is predicted to bind it more strongly based on the reported allele-specific binding-site interpretation; no QBiC-SELEX result is supplied here. | missing | none |
| element | Greater GATA3 binding at alt A represses the variant-containing element. | missing | none |
| gene | Repression of the element reduces LMO1 expression. | missing | none |
| cell_type | The effect occurs in neuroblastoma cells in which GATA3 and LMO1 are expressed. | missing | none |
| phenotype | Reduced LMO1 expression lowers neuroblastoma susceptibility. | missing | none |

Predictions: An alt-A enhancer reporter has lower activity than a ref-C reporter in SK-N-SH cells.; Changing ref C to alt A increases GATA3 occupancy but reduces LMO1 expression.

Falsified if: The alt-A reporter is more active than the ref-C reporter.; GATA3 depletion fails to change the allelic expression effect despite confirmed GATA3 expression.

### 4. H3: A related GATA factor, rather than GATA3, activates LMO1 (p = 0.05)

TF GATA2 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant-containing element is an enhancer responsive to GATA2.; gene LMO1; cell type Neuroblastoma cells, including SK-N-SH..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is a speculative alternative because it is related to GATA3; alt A is hypothesized to bind it more strongly from the proposed GATA motif change. No GATA2-specific QBiC-SELEX result is supplied here. | missing | none |
| element | Greater GATA2 binding at alt A increases enhancer activity. | missing | none |
| gene | The enhancer increases LMO1 expression. | missing | none |
| cell_type | The effect occurs in neuroblastoma cells that express GATA2 and LMO1. | missing | none |
| phenotype | Increased LMO1 expression raises neuroblastoma susceptibility. | missing | none |

Predictions: The alt-A enhancer reporter is more active than the ref-C reporter.; GATA2 perturbation changes the allelic effect more than GATA3 perturbation does.

Falsified if: GATA2 is not expressed in the relevant cells or does not occupy the element.; GATA2 perturbation has no effect on the allelic enhancer or LMO1 expression difference.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Matched ref-C versus alt-A enhancer reporter in SK-N-SH cells | low | yes | Alt-A reporter activity is higher than ref-C. | No reproducible activity difference. | Alt-A reporter activity is lower than ref-C. | Alt-A reporter activity is higher than ref-C. |
| Isogenic editing of the variant followed by LMO1 expression measurement in SK-N-SH | medium | yes | A-to-C editing reduces LMO1 expression. | Editing has no consistent effect on LMO1 expression. | A-to-C editing increases LMO1 expression. | A-to-C editing reduces LMO1 expression, with the effect dependent on GATA2. |
| Compare GATA3 and GATA2 occupancy and perturbation effects at the element | high | yes | GATA3 occupancy or perturbation tracks the alt-A effect more strongly than GATA2. | No convincing allele-dependent occupancy or perturbation effect. | GATA3 occupancy tracks the effect, while its perturbation supports repression. | GATA2 occupancy or perturbation tracks the alt-A effect more strongly than GATA3. |

## Next experiment

Run a matched ref-C versus alt-A enhancer reporter assay in SK-N-SH cells. It is the cheapest proposed test of the top two chains: H1 predicts higher alt-A activity, whereas the null predicts no reproducible difference. A reporter result would not by itself establish endogenous chromatin effects or identify the responsible TF.

## Flags

- none

## Evidence
