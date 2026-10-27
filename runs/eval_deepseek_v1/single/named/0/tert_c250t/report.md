# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 1 model calls; 22 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: GABPA binds the C250T alt allele and activates TERT (p = 0.55)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter C250T de novo ETS motif; gene TERT; cell type glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele is predicted to create a de novo ETS motif that GABPA binds more strongly than the ref G allele; QBiC-SELEX coverage was not checked and no QBiC evidence was supplied. | missing | none |
| element | C250T lies in the TERT promoter and is proposed to act as an allele-specific GABPA-responsive promoter element. | missing | none |
| gene | Increased GABPA occupancy at the alt allele is proposed to increase TERT transcription. | missing | none |
| cell_type | The effect is proposed in glioblastoma cells, matching the DepMap glioblastoma expression context; melanoma and bladder cancer may share the mechanism. | missing | none |
| phenotype | Increased TERT expression and telomerase activity would support immortalization and tumor growth. | missing | none |

Predictions: Allele-specific GABPA ChIP-qPCR or ChIP-seq shows enrichment on the alt allele over ref at the TERT promoter.; GABPA knockdown or CRISPRi reduces TERT expression preferentially in C250T-heterozygous glioblastoma cells.; Ref versus alt TERT promoter reporters differ in activity in a GABPA-dependent manner.

Falsified if: The alt allele is not preferentially bound by GABPA in an appropriate heterozygous cell system.; GABPA loss does not reduce TERT expression or reporter activity from the alt promoter.; Allele-specific TERT expression is explained by a linked variant rather than C250T.

### 2. H4: No TF-mediated allelic effect; C250T is passenger or linked to the causal variant (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at C250T is detectable.; Ref and alt TERT promoter reporters show no reproducible allelic difference.; Any TERT association is explained by a linked causal variant or by passenger mutation at a mutational hotspot.

Falsified if: Allele-specific GABPA binding and GABPA-dependent TERT activation are demonstrated for C250T.

### 3. H2: ETS1 binds the C250T alt allele and activates TERT (p = 0.10)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter C250T de novo ETS motif; gene TERT; cell type glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele is predicted to create an ETS motif bound more strongly by ETS1 than the ref G allele; QBiC-SELEX coverage was not checked. | missing | none |
| element | C250T is proposed to form an allele-specific ETS1-responsive element in the TERT promoter. | missing | none |
| gene | Increased ETS1 occupancy at the alt allele is proposed to increase TERT transcription. | missing | none |
| cell_type | This chain is proposed in glioblastoma cells, with possible relevance to melanoma and bladder cancer. | missing | none |
| phenotype | Increased TERT/telomerase would promote replicative immortality. | missing | none |

Predictions: Allele-specific ETS1 ChIP shows preferential binding to the alt allele.; ETS1 knockdown reduces TERT expression or alt-promoter reporter activity.

Falsified if: ETS1 does not bind the C250T alt allele preferentially.; ETS1 loss does not affect TERT expression from the alt promoter.

### 4. H3: ETS2 binds the C250T alt allele and activates TERT (p = 0.10)

TF ETS2 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter C250T de novo ETS motif; gene TERT; cell type glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele is predicted to create an ETS motif bound more strongly by ETS2 than the ref G allele; QBiC-SELEX coverage was not checked. | missing | none |
| element | C250T is proposed to form an allele-specific ETS2-responsive element in the TERT promoter. | missing | none |
| gene | Increased ETS2 occupancy at the alt allele is proposed to increase TERT transcription. | missing | none |
| cell_type | This chain is proposed in glioblastoma cells, with possible relevance to melanoma and bladder cancer. | missing | none |
| phenotype | Increased TERT/telomerase would support tumor cell immortalization. | missing | none |

Predictions: Allele-specific ETS2 ChIP shows preferential binding to the alt allele.; ETS2 knockdown reduces TERT expression or alt-promoter reporter activity.

Falsified if: ETS2 does not bind the C250T alt allele preferentially.; ETS2 loss does not affect TERT expression from the alt promoter.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR or ChIP-seq at the TERT promoter in heterozygous C250T glioblastoma cells | medium | yes | alt allele is enriched over ref for GABPA | no allele-specific TF enrichment | ETS1, not GABPA, shows preferential alt-allele binding | ETS2, not GABPA, shows preferential alt-allele binding |
| GABPA knockdown or CRISPRi followed by TERT qPCR in C250T-heterozygous versus TERT-wild-type glioblastoma cells | medium | yes | TERT decreases preferentially in C250T-heterozygous cells | no TERT change | no GABPA-dependent TERT change | no GABPA-dependent TERT change |
| Ref versus alt TERT promoter luciferase reporter in a glioblastoma line, with and without GABPA knockdown | low | yes | alt reporter is higher and the difference is GABPA-dependent | no reproducible ref/alt difference | alt reporter is higher but GABPA-independent | alt reporter is higher but GABPA-independent |

## Next experiment

Run a ref-versus-alt TERT promoter luciferase reporter assay in a glioblastoma line, with and without GABPA knockdown; this is the cheapest test that separates GABPA-dependent activation (H1) from no allelic effect (H4).

## Flags

- none

## Evidence
