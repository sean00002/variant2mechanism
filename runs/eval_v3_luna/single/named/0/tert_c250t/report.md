# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 1 model calls; 37 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: The mutant promoter creates a GABPA-responsive TERT site (p = 0.65)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element The TERT promoter hotspot acts as a mutant-allele ETS-family binding element.; gene TERT; cell type Glioblastoma tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is the leading candidate because the C250T hotspot is known to create an ETS-family site with mutant-allele binding; the case supplies no QBiC-SELEX result or occupancy data to confirm GABPA at this site. | missing | none |
| element | The altered TERT promoter sequence increases the likelihood of GABPA binding and functions as a cis-regulatory element. | missing | none |
| gene | GABPA binding at the mutant promoter increases TERT transcription in cis. | missing | none |
| cell_type | This effect occurs in glioblastoma tumor cells, the expression context specified for the case. | missing | none |
| phenotype | Increased TERT expression supports telomerase activity and tumor-cell persistence, contributing to glioblastoma. | missing | none |

Predictions: In a heterozygous tumor model, GABPA occupancy is greater at the alt allele than at the ref allele.; Disrupting GABPA binding reduces mutant-allele TERT transcription.

Falsified if: Allele-specific occupancy assays show no GABPA enrichment at the alt allele despite adequate assay sensitivity.; Selective disruption of GABPA does not reduce TERT expression attributable to the mutant promoter.

### 2. H3: No TF-mediated effect of this variant (p = 0.23)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant does not cause reproducible allele-specific TF occupancy or a cis change in TERT expression.; Any association with tumor phenotype could instead reflect a linked cause, another mechanism, or no causal effect.

Falsified if: A reproducible alt-allele-specific TF occupancy difference is shown to cause a cis increase in TERT expression.

### 3. H2: A different ETS factor drives the mutant promoter (p = 0.12)

TF ETS1 (QBiC-SELEX coverage own_model), alt allele binds more; element The TERT promoter hotspot acts as a mutant-allele ETS-family binding element.; gene TERT; cell type Glioblastoma tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETS1 is an alternative ETS-family candidate that could bind the created motif more strongly on the alt allele; the case supplies no ETS1 occupancy or QBiC-SELEX result. | missing | none |
| element | The altered TERT promoter sequence creates or strengthens an ETS-responsive cis-regulatory element. | missing | none |
| gene | ETS1 binding at the mutant promoter increases TERT transcription in cis. | missing | none |
| cell_type | This effect occurs in glioblastoma tumor cells. | missing | none |
| phenotype | Increased TERT expression supports telomerase activity and tumor-cell persistence, contributing to glioblastoma. | missing | none |

Predictions: In a heterozygous tumor model, ETS1 occupancy is greater at the alt allele than at the ref allele.; Disrupting ETS1 binding reduces mutant-allele TERT transcription, whereas disrupting GABPA has a smaller effect.

Falsified if: Allele-specific occupancy assays show no ETS1 enrichment at the alt allele despite adequate assay sensitivity.; Selective disruption of ETS1 does not reduce TERT expression attributable to the mutant promoter.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H3 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific CUT&RUN or ChIP-qPCR for GABPA and ETS1 in a heterozygous TERT-promoter-mutant glioblastoma model | low | yes | Alt-allele GABPA enrichment exceeds ETS1 enrichment. | Neither factor shows reproducible alt-allele enrichment. | Alt-allele ETS1 enrichment exceeds GABPA enrichment. |

## Next experiment

Perform allele-specific CUT&RUN or ChIP-qPCR for GABPA and ETS1 in a heterozygous TERT-promoter-mutant glioblastoma model, using matched input and allele-aware quantification. This is a low-cost way to distinguish the leading GABPA chain from the ETS1 alternative; occupancy alone would not establish the downstream TERT-expression or disease effects.

## Flags

- none

## Evidence
