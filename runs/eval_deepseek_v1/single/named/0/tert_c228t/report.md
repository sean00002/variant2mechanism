# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 1 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1_GABPA_activation: GABPA binds the C228T-created ETS motif and activates TERT in glioblastoma (p = 0.45)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element The C228T alt allele lies in the TERT promoter and creates/strengthens an ETS-family cis-regulatory motif.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C228T alt allele creates/strengthens an ETS motif that binds GABPA more strongly than the ref G allele; GABPA QBiC-SELEX coverage is not_checked because no screen or qbic_tf_detail lookup was provided. | missing | none |
| element | The variant is in the TERT promoter proximal regulatory region and alters a cis-element rather than coding sequence. | missing | none |
| gene | Increased GABPA occupancy at the alt TERT promoter increases TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, the TERT promoter is active and GABPA is expressed, allowing this ETS motif to act. | missing | none |
| phenotype | Allele-specific TERT activation increases telomerase and contributes to glioblastoma development or progression. | missing | none |

Predictions: Alt allele shows higher GABPA occupancy than ref at the TERT promoter.; Alt allele shows higher TERT expression than ref in isogenic glioblastoma cells.; GABPA depletion reduces alt-dependent TERT expression.

Falsified if: Allele-specific GABPA ChIP-qPCR shows no alt-vs-ref occupancy difference at the TERT promoter.; Isogenic C228T knock-in does not increase TERT expression in glioblastoma cells.; GABPA knockdown does not reduce the alt-dependent TERT expression.

### 2. H4_null: No TF-mediated allelic effect; C228T is a passenger/linked or non-TF-associated variant (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at the TERT promoter.; No allele-specific TERT expression in isogenic cells.; Any disease association is due to a linked causal variant, passenger mutation, or non-TF mechanism.

Falsified if: Allele-specific GABPA ChIP-qPCR shows a reproducible alt-vs-ref occupancy difference at the TERT promoter.; Isogenic C228T knock-in causes allele-specific TERT expression that depends on an ETS TF.

### 3. H2_ELK1_activation: ELK1 binds the C228T-created ETS motif and activates TERT in glioblastoma (p = 0.10)

TF ELK1 (stated coverage not_checked; registry own_model), alt allele binds more; element The C228T alt allele lies in the TERT promoter and creates/strengthens an ETS-family cis-regulatory motif.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C228T alt allele creates/strengthens an ETS motif that binds ELK1 more strongly than the ref G allele; ELK1 QBiC-SELEX coverage is not_checked because no screen or qbic_tf_detail lookup was provided. | missing | none |
| element | The variant is in the TERT promoter proximal regulatory region and alters a cis-element rather than coding sequence. | missing | none |
| gene | Increased ELK1 occupancy at the alt TERT promoter increases TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, ELK1 is expressed and can access the active TERT promoter. | missing | none |
| phenotype | Allele-specific TERT activation increases telomerase and contributes to glioblastoma development or progression. | missing | none |

Predictions: Alt allele shows higher ELK1 occupancy than ref at the TERT promoter.; ELK1 depletion reduces alt-dependent TERT expression.; GABPA depletion has little effect on the allele-specific signal if ELK1 is the relevant factor.

Falsified if: Allele-specific ELK1 ChIP-qPCR shows no alt-vs-ref occupancy difference at the TERT promoter.; ELK1 knockdown does not reduce alt-dependent TERT expression in glioblastoma cells.; GABPA, but not ELK1, accounts for the allele-specific occupancy.

### 4. H3_ETS1_activation: ETS1 binds the C228T-created ETS motif and activates TERT in glioblastoma (p = 0.10)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element The C228T alt allele lies in the TERT promoter and creates/strengthens an ETS-family cis-regulatory motif.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C228T alt allele creates/strengthens an ETS motif that binds ETS1 more strongly than the ref G allele; ETS1 QBiC-SELEX coverage is not_checked because no screen or qbic_tf_detail lookup was provided. | missing | none |
| element | The variant is in the TERT promoter proximal regulatory region and alters a cis-element rather than coding sequence. | missing | none |
| gene | Increased ETS1 occupancy at the alt TERT promoter increases TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, ETS1 is expressed and can access the active TERT promoter. | missing | none |
| phenotype | Allele-specific TERT activation increases telomerase and contributes to glioblastoma development or progression. | missing | none |

Predictions: Alt allele shows higher ETS1 occupancy than ref at the TERT promoter.; ETS1 depletion reduces alt-dependent TERT expression.; GABPA and ELK1 depletion have little effect if ETS1 is the relevant factor.

Falsified if: Allele-specific ETS1 ChIP-qPCR shows no alt-vs-ref occupancy difference at the TERT promoter.; ETS1 knockdown does not reduce alt-dependent TERT expression in glioblastoma cells.; GABPA or ELK1, but not ETS1, accounts for the allele-specific occupancy.

## Prediction matrix

| Test | Cost | Separates top two | H1_GABPA_activation | H4_null | H2_ELK1_activation | H3_ETS1_activation |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR at the TERT promoter in a heterozygous C228T glioblastoma line, with alt-vs-ref occupancy quantified by digital PCR or spike-in normalization, followed by GABPA knockdown to test dependence. | low | yes | Alt-specific GABPA occupancy and alt-specific TERT expression | No alt-specific GABPA occupancy or TERT expression |  |  |

## Next experiment

Allele-specific GABPA ChIP-qPCR at the TERT promoter in a heterozygous C228T glioblastoma line, with alt-vs-ref occupancy quantified by digital PCR or spike-in normalization, followed by GABPA knockdown to test dependence. This separates the top GABPA-activation chain from the null by asking whether the alt allele has GABPA-dependent occupancy and TERT expression.

## Flags

- none

## Evidence
