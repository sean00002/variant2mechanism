# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 0 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: Alt-specific GABPA binding activates TERT (p = 0.42)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele creates or strengthens an ETS-family binding site, with GABPA binding more strongly than ref. GABPA is chosen from the ETS family because TERT promoter mutations are canonical de novo ETS motifs and GABPA/GABPB is a plausible activator in glioblastoma. QBiC-SELEX coverage: not_checked, since no evidence list or screen row was provided. | missing | none |
| element | The alt allele lies within the TERT promoter and alters a local cis-regulatory element. | missing | none |
| gene | Increased GABPA binding at the mutant TERT promoter increases TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, this GABPA-dependent TERT promoter activation increases telomerase activity. | missing | none |
| phenotype | Increased telomerase activity supports telomere maintenance and tumor cell immortalization in glioblastoma. | missing | none |

Predictions: Alt allele shows stronger GABPA binding than ref.; GABPA occupies the mutant TERT promoter in glioblastoma cells.; GABPA loss reduces alt-linked TERT expression and telomerase activity.

Falsified if: Allele-specific binding assays show no alt-dependent GABPA enrichment in glioblastoma cells.; GABPA is not expressed or not nuclear in the relevant glioblastoma context.; Alt-specific TERT expression is unaffected by GABPA knockdown or inhibition.

### 2. H0: No TF-mediated effect of this variant (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No TF-mediated allelic effect at this variant.; Any disease association is due to a linked causal variant, a passenger mutation at a mutational hotspot, or no allelic effect.

Falsified if: Allele-specific reporter or binding assays show a reproducible alt-dependent TF effect at this exact variant.; The variant is shown to be the causal allele rather than a linked passenger or hotspot mutation.

### 3. H2: Alt-specific ETS1 binding activates TERT (p = 0.18)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele creates or strengthens an ETS-family binding site that binds ETS1 more strongly than ref. ETS1 is an alternative ETS-family member that could recognize the same mutant motif. QBiC-SELEX coverage: not_checked; no evidence list or screen row was provided. | missing | none |
| element | The variant is in the TERT promoter and changes a cis-regulatory element. | missing | none |
| gene | Alt-specific ETS1 binding increases TERT transcription. | missing | none |
| cell_type | In glioblastoma cells, ETS1-dependent activation of TERT increases telomerase activity. | missing | none |
| phenotype | Higher telomerase activity promotes telomere maintenance and tumor growth. | missing | none |

Predictions: Alt allele shows stronger ETS1 binding than ref.; ETS1 occupies the mutant TERT promoter in glioblastoma cells.; ETS1 loss reduces alt-linked TERT expression.

Falsified if: No alt-specific ETS1 binding is detected at the TERT promoter.; ETS1 knockdown does not change alt-linked TERT expression.; ETS1 is not expressed in the relevant glioblastoma cells.

### 4. H3: Alt-specific ELK1 binding modulates TERT (p = 0.10)

TF ELK1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele creates or strengthens an ETS-family site that binds ELK1 more strongly than ref. ELK1 is another ETS-family candidate for the mutant motif, but this chain is less likely without direct evidence. QBiC-SELEX coverage: not_checked; no evidence list or screen row was provided. | missing | none |
| element | The variant is in the TERT promoter and alters a cis-regulatory element. | missing | none |
| gene | Alt-specific ELK1 binding modulates TERT transcription; the direction may depend on context, so this chain does not assume binding equals activation without evidence. | missing | none |
| cell_type | In glioblastoma cells, ELK1-dependent regulation of TERT changes telomerase activity. | missing | none |
| phenotype | Altered telomerase activity contributes to telomere maintenance and tumor phenotype. | missing | none |

Predictions: Alt allele shows stronger ELK1 binding than ref.; ELK1 occupies the mutant TERT promoter.; ELK1 perturbation changes TERT expression in the relevant cells.

Falsified if: ELK1 does not bind the alt allele preferentially.; ELK1 loss does not alter TERT expression in glioblastoma cells.; The effect is fully explained by another ETS factor.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA or biotinylated-oligo pull-down with glioblastoma nuclear extract, comparing ref and alt TERT promoter oligos, followed by anti-GABPA supershift; if needed, run anti-ETS1 in parallel to separate H1 from H2/H3. | low | yes | Alt-specific shift supershifted by anti-GABPA | No alt-specific shift | Alt-specific shift not supershifted by anti-GABPA | Alt-specific shift not supershifted by anti-GABPA |

## Next experiment

Allele-specific EMSA or DNA pull-down using ref versus alt TERT promoter oligos and glioblastoma nuclear extract, with anti-GABPA supershift. This directly separates the top two chains, H1 (alt-specific GABPA binding) and H0 (no TF-mediated allelic effect), at low cost; adding anti-ETS1 in the same experiment would also help distinguish H2 from H1.

## Flags

- none

## Evidence
