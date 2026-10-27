# rs2168101 and Neuroblastoma (LMO1)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 23 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. A: GATA2 alt-stronger repressor chain (p = 0.45)

TF GATA2 (stated coverage not_checked; registry own_model), alt allele binds more; element The variant lies in a cis-regulatory enhancer in the LMO1 locus; increased GATA2 occupancy at the alt allele raises enhancer output.; gene LMO1; cell type SK-N-SH.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 binds the alt A allele more strongly than the ref C allele at rs2168101, proposed through an A-created or A-enhanced GATA motif. QBiC-SELEX coverage for GATA2 is not_checked because no screen row or qbic_tf_detail lookup was supplied. | missing | none |
| element | rs2168101 lies in a cis-regulatory enhancer element in the LMO1 locus; stronger GATA2 binding at the alt allele increases enhancer activity. | missing | none |
| gene | Increased enhancer activity raises LMO1 transcription in cis. | missing | none |
| cell_type | In SK-N-SH adrenergic neuroblastoma cells, GATA2 and LMO1 are in a regulatory circuit relevant to LMO1 expression. | missing | none |
| phenotype | Higher LMO1 dosage promotes neuroblastoma, so the alt allele increases disease risk. | missing | none |

Predictions: GATA2 ChIP or allele-specific binding shows alt > ref.; LMO1 enhancer reporter shows alt > ref in SK-N-SH.; GATA2 knockdown reduces the alt-allele enhancer effect.

Falsified if: No allele-specific GATA2 binding is detected at rs2168101.; The alt allele does not increase enhancer activity in SK-N-SH cells.; GATA2 knockdown does not reduce the alt-allele enhancer effect.

### 2. D: Null: linked causal variant or no direct TF-mediated allelic effect (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific GATA2 binding at rs2168101.; No allele-specific LMO1 enhancer activity when only rs2168101 is changed.; The disease association is explained by a linked causal variant or by no direct TF-mediated allelic effect.

Falsified if: Allele-specific GATA2 binding and allele-specific LMO1 enhancer activity are demonstrated at rs2168101.; The signal disappears after conditioning on the linked causal variant.

### 3. B: GATA2 alt-stronger repressor chain (p = 0.15)

TF GATA2 (stated coverage not_checked; registry own_model), alt allele binds more; element The variant lies in a cis-regulatory element in the LMO1 locus; increased GATA2 occupancy at the alt allele represses the element.; gene LMO1; cell type SK-N-SH.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 binds the alt A allele more strongly than the ref C allele at rs2168101. QBiC-SELEX coverage for GATA2 is not_checked because no screen row or qbic_tf_detail lookup was supplied. | missing | none |
| element | The element is a repressive GATA2-responsive cis-regulatory element in the LMO1 locus, and stronger alt-allele GATA2 binding lowers its activity. | missing | none |
| gene | Lower enhancer or regulatory activity reduces LMO1 transcription in cis. | missing | none |
| cell_type | In SK-N-SH neuroblastoma cells, GATA2 can act as a repressor at this LMO1 regulatory element. | missing | none |
| phenotype | Lower LMO1 dosage reduces neuroblastoma risk, so the alt allele is protective. | missing | none |

Predictions: GATA2 binding shows alt > ref.; LMO1 expression or reporter activity shows alt < ref.; GATA2 knockdown increases alt-allele reporter activity.

Falsified if: LMO1 expression is not lower from the alt allele.; GATA2 knockdown does not relieve repression of the alt allele.; GATA2 binding is not alt-allele-preferential.

### 4. C: GATA2 ref-stronger activator chain (p = 0.10)

TF GATA2 (stated coverage not_checked; registry own_model), ref allele binds more; element The variant lies in a cis-regulatory enhancer in the LMO1 locus; the ref C allele preserves stronger GATA2 binding and enhancer activity.; gene LMO1; cell type SK-N-SH.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 binds the ref C allele more strongly than the alt A allele at rs2168101. QBiC-SELEX coverage for GATA2 is not_checked because no screen row or qbic_tf_detail lookup was supplied. | missing | none |
| element | rs2168101 lies in a GATA2-responsive enhancer of LMO1; the ref C allele gives stronger enhancer activity than the alt A allele. | missing | none |
| gene | Stronger ref-allele enhancer activity raises LMO1 transcription in cis. | missing | none |
| cell_type | In SK-N-SH neuroblastoma cells, this GATA2-responsive element contributes to LMO1 expression. | missing | none |
| phenotype | The alt allele lowers LMO1 dosage and is protective against neuroblastoma. | missing | none |

Predictions: GATA2 binding shows ref > alt.; LMO1 reporter activity shows ref > alt.; The alt allele reduces LMO1 expression relative to ref.

Falsified if: GATA2 binding is stronger on the alt allele, not the ref allele.; The ref allele does not increase LMO1 reporter activity.; No allele-specific GATA2 binding is detected.

## Prediction matrix

| Test | Cost | Separates top two | A | D | B | C |
| --- | --- | --- | --- | --- | --- | --- |
| allele-specific GATA2 binding | low | yes | alt > ref reporter activity and GATA2 dependence | no rs2168101 allele effect or no GATA2 dependence |  |  |

## Next experiment

Cheapest single discriminating experiment: dual-luciferase reporter in SK-N-SH comparing a short LMO1 enhancer fragment with rs2168101 ref C versus alt A, with and without GATA2 siRNA. It separates hypothesis A from the null D: A predicts alt>ref reporter activity that is reduced by GATA2 knockdown; D predicts no rs2168101 allele effect or no GATA2 dependence.

## Flags

- none

## Evidence
