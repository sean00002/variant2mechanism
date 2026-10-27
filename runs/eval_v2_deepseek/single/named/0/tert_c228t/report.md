# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 14 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. GABPA_activation: GABPA binds the C228T-created ETS motif and activates TERT (p = 0.50)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter C228T creates a de novo ETS/GGAA motif at the variant.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA binds the alt allele more strongly than the ref allele at TERT promoter C228T. No QBiC-SELEX model is supplied for GABPA here; this direction is inferred from the C228T-created ETS/GGAA motif and known TERT promoter biology, not from a QBiC-SELEX measurement. | missing | none |
| element | The variant lies in the TERT promoter and creates an ETS-factor binding element. | missing | none |
| gene | The element regulates TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, this promoter element can drive TERT expression. | missing | none |
| phenotype | Increased TERT expression supports telomere maintenance and tumor cell immortality, promoting glioblastoma. | missing | none |

Predictions: Alt allele shows higher GABPA ChIP signal than ref allele at the variant.; TERT expression is higher from the alt-bearing allele.; GABPA knockdown reduces TERT expression and/or the allelic TERT expression bias.

Falsified if: No reproducible GABPA occupancy over the variant in C228T-bearing cells.; No alt-allele enrichment in GABPA ChIP at the variant.; GABPA knockdown does not reduce TERT expression or does not remove the allelic TERT expression bias.

### 2. null_no_tf_mediated_effect: No TF-mediated allelic effect at C228T (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific GABPA, ETS1, or ELK1 ChIP signal over the variant.; No alt-specific TERT expression from the variant.; Any disease association is due to a linked causal variant, passenger mutation, or another non-TF mechanism.

Falsified if: Reproducible allele-specific occupancy of an ETS factor at the variant is demonstrated.; The alt allele shows a reproducible increase in TERT expression that depends on the variant.; Knockdown of the candidate ETS factor removes the allelic TERT expression bias.

### 3. ETS1_activation: ETS1 binds the C228T-created ETS motif and activates TERT (p = 0.15)

TF ETS1 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter C228T creates a de novo ETS/GGAA motif at the variant.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETS1 binds the alt allele more strongly than the ref allele at TERT promoter C228T. No QBiC-SELEX model is supplied for ETS1 here; the direction is inferred from the C228T-created ETS/GGAA motif. | missing | none |
| element | The variant lies in the TERT promoter and creates an ETS-factor binding element. | missing | none |
| gene | The element regulates TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, this promoter element can drive TERT expression. | missing | none |
| phenotype | Increased TERT expression supports telomere maintenance and tumor cell immortality, promoting glioblastoma. | missing | none |

Predictions: Alt allele shows higher ETS1 ChIP signal than ref allele at the variant.; TERT expression is higher from the alt-bearing allele.; ETS1 knockdown reduces TERT expression and/or the allelic TERT expression bias.

Falsified if: No reproducible ETS1 occupancy over the variant.; No alt-allele enrichment in ETS1 ChIP at the variant.; ETS1 knockdown does not affect TERT expression or the allelic TERT expression bias.

### 4. ELK1_activation: ELK1 binds the C228T-created ETS motif and activates TERT (p = 0.10)

TF ELK1 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter C228T creates a de novo ETS/GGAA motif at the variant.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ELK1 binds the alt allele more strongly than the ref allele at TERT promoter C228T. No QBiC-SELEX model is supplied for ELK1 here; the direction is inferred from the C228T-created ETS/GGAA motif. | missing | none |
| element | The variant lies in the TERT promoter and creates an ETS-factor binding element. | missing | none |
| gene | The element regulates TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, this promoter element can drive TERT expression. | missing | none |
| phenotype | Increased TERT expression supports telomere maintenance and tumor cell immortality, promoting glioblastoma. | missing | none |

Predictions: Alt allele shows higher ELK1 ChIP signal than ref allele at the variant.; TERT expression is higher from the alt-bearing allele.; ELK1 knockdown reduces TERT expression and/or the allelic TERT expression bias.

Falsified if: No reproducible ELK1 occupancy over the variant.; No alt-allele enrichment in ELK1 ChIP at the variant.; ELK1 knockdown does not affect TERT expression or the allelic TERT expression bias.

## Prediction matrix

| Test | Cost | Separates top two | GABPA_activation | null_no_tf_mediated_effect | ETS1_activation | ELK1_activation |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ChIP-qPCR for GABPA at the TERT promoter in C228T-heterozygous glioblastoma cells, with spike-in normalization; compare alt/ref DNA ratios in GABPA immunoprecipitate. | low | yes | GABPA ChIP alt/ref > 1 at the variant; TERT expression higher from alt allele; GABPA knockdown reduces TERT and allelic bias. | No allele-specific GABPA, ETS1, or ELK1 ChIP signal; no alt-specific TERT expression. | ETS1 ChIP alt/ref > 1; GABPA ChIP alt/ref approximately 1 or weaker; ETS1 knockdown reduces TERT. | ELK1 ChIP alt/ref > 1; GABPA and ETS1 ChIP alt/ref approximately 1 or weaker; ELK1 knockdown reduces TERT. |

## Next experiment

Allele-specific ChIP-qPCR for GABPA at TERT promoter C228T in heterozygous glioblastoma cells. The GABPA_activation chain predicts alt/ref > 1 in GABPA immunoprecipitate; the null predicts no allelic imbalance (alt/ref approximately 1). This is the cheapest direct separator of the top two chains.

## Flags

- none

## Evidence
