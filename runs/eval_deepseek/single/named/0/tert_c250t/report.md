# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 33 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. GABPA_ETS_activation: C250T creates a stronger GABPA/ETS site that activates TERT (p = 0.45)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele at TERT promoter C250T creates or strengthens an ETS-family motif, and GABPA binds the alt allele more strongly than the ref allele. | missing | none |
| element | C250T lies in the TERT core promoter and acts as an allele-specific ETS-responsive regulatory element. | missing | none |
| gene | The alt allele increases TERT promoter activity and TERT transcription. | missing | none |
| cell_type | This mechanism is relevant in glioblastoma cells, the provided expression context, and plausibly in melanoma and bladder cancer where TERT promoter mutations occur. | missing | none |
| phenotype | Increased TERT/telomerase activity supports telomere maintenance, cell immortalization, and tumor growth in glioblastoma. | missing | none |

Predictions: Allele-specific GABPA ChIP at the TERT promoter enriches the alt allele over the ref allele.; GABPA knockdown reduces TERT expression preferentially in C250T-heterozygous glioblastoma cells.; A TERT promoter reporter carrying C250T shows higher activity than ref, and this difference is GABPA-dependent.

Falsified if: Allele-specific GABPA ChIP shows no alt-allele enrichment.; GABPA knockdown does not reduce TERT expression or reporter activity.; The C250T reporter effect persists unchanged after GABPA depletion.

### 2. null_no_tf_mediated_effect: C250T is not itself the TF-mediated causal variant (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at C250T distinguishes ref from alt.; TERT expression is driven by a linked causal variant, a passenger mutation at a mutational hotspot, or another non-allelic mechanism.; C250T reporter alleles show no differential activity, or any difference is not TF-dependent.

Falsified if: Allele-specific ChIP or EMSA demonstrates reproducible alt-allele enrichment for a specific TF.; Depletion of that TF reduces the C250T allele-specific reporter or TERT expression effect.

### 3. ETS1_ETS_activation: C250T creates a stronger ETS1 site that activates TERT (p = 0.15)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele at TERT promoter C250T creates or strengthens an ETS-family motif, and ETS1 binds the alt allele more strongly than the ref allele. | missing | none |
| element | C250T lies in the TERT core promoter and acts as an allele-specific ETS1-responsive regulatory element. | missing | none |
| gene | The alt allele increases TERT promoter activity and TERT transcription. | missing | none |
| cell_type | This mechanism is relevant in glioblastoma cells and possibly in melanoma and bladder cancer. | missing | none |
| phenotype | Increased TERT/telomerase activity supports telomere maintenance and tumor growth. | missing | none |

Predictions: Allele-specific ETS1 ChIP at the TERT promoter enriches the alt allele over the ref allele.; ETS1 knockdown reduces TERT expression preferentially in C250T-heterozygous glioblastoma cells.; GABPA ChIP does not show stronger alt-allele enrichment than ETS1 ChIP.

Falsified if: Allele-specific ETS1 ChIP shows no alt-allele enrichment.; ETS1 knockdown does not affect TERT expression or reporter activity.; GABPA, not ETS1, is the dominant allele-specific factor at this site.

### 4. ELF1_ETS_activation: C250T creates a stronger ELF1 site that activates TERT (p = 0.10)

TF ELF1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele at TERT promoter C250T creates or strengthens an ETS-family motif, and ELF1 binds the alt allele more strongly than the ref allele. | missing | none |
| element | C250T lies in the TERT core promoter and acts as an allele-specific ELF1-responsive regulatory element. | missing | none |
| gene | The alt allele increases TERT promoter activity and TERT transcription. | missing | none |
| cell_type | This mechanism is relevant in glioblastoma cells and possibly in melanoma and bladder cancer. | missing | none |
| phenotype | Increased TERT/telomerase activity supports telomere maintenance and tumor growth. | missing | none |

Predictions: Allele-specific ELF1 ChIP at the TERT promoter enriches the alt allele over the ref allele.; ELF1 knockdown reduces TERT expression preferentially in C250T-heterozygous glioblastoma cells.; GABPA and ETS1 ChIP do not show the same alt-allele enrichment.

Falsified if: Allele-specific ELF1 ChIP shows no alt-allele enrichment.; ELF1 knockdown does not affect TERT expression or reporter activity.; Another ETS factor accounts for the allele-specific binding.

## Prediction matrix

| Test | Cost | Separates top two | GABPA_ETS_activation | null_no_tf_mediated_effect | ETS1_ETS_activation | ELF1_ETS_activation |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP at TERT promoter | low | yes | alt > ref enrichment | no alt enrichment | no or weak alt enrichment; ETS1 ChIP would be needed | no or weak alt enrichment; ELF1 ChIP would be needed |

## Next experiment

Allele-specific GABPA ChIP-qPCR at the TERT C250T site in heterozygous glioblastoma cells, comparing alt and ref allele enrichment; this directly separates the top GABPA hypothesis from the null hypothesis.

## Flags

- none

## Evidence
