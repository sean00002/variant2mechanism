# rs2168101 and Neuroblastoma (LMO1)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 16 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. H1_GATA3_alt_activator: GATA3 alt-A activator chain (p = 0.42)

TF GATA3 (stated coverage not_checked; registry own_model), alt allele binds more; element The rs2168101 alt A allele strengthens or creates a GATA3-binding site in an LMO1 enhancer element.; gene LMO1; cell type Neuroblastoma cells, represented by SK-N-SH, which are compatible with neural-crest-derived sympathetic lineage expression of GATA3..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 binds the alt A allele more strongly than ref C at rs2168101. | missing | none |
| element | rs2168101 lies in an LMO1 enhancer whose activity is increased by the alt A allele. | missing | none |
| gene | Increased enhancer activity raises LMO1 expression. | missing | none |
| cell_type | This occurs in neuroblastoma cells such as SK-N-SH. | missing | none |
| phenotype | Higher LMO1 promotes neuroblastoma risk or malignant phenotype. | missing | none |

Predictions: GATA3 binds A probe more than C probe; GATA3 occupies the LMO1 enhancer in SK-N-SH; GATA3 loss decreases LMO1 expression; A allele associates with higher LMO1 expression

Falsified if: Allele-specific EMSA shows no differential GATA3 binding between C and A.; GATA3 ChIP-seq/ChIP-qPCR at the LMO1 locus does not show GATA3 occupancy or allele preference.; GATA3 knockdown does not reduce LMO1 expression in SK-N-SH.

### 2. H0_null: Null: linked causal variant, passenger, or no allelic effect (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs2168101; No allele-specific effect on LMO1 expression attributable to this variant; Association is explained by linkage disequilibrium with another causal variant or by no causal effect

Falsified if: A robust allele-specific TF binding difference and TF-dependent LMO1 expression change are demonstrated.

### 3. H2_GATA2_ref_repressor_loss: GATA2 ref-C repressor-loss chain (p = 0.16)

TF GATA2 (stated coverage not_checked; registry own_model), ref allele binds more; element The ref C allele preserves a stronger GATA2-binding site in an LMO1 enhancer; the alt A allele weakens it.; gene LMO1; cell type Neuroblastoma cells, represented by SK-N-SH..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 binds the ref C allele more strongly than alt A at rs2168101. | missing | none |
| element | The ref C allele maintains a GATA2-responsive repressive or modulatory LMO1 enhancer element. | missing | none |
| gene | Loss of GATA2 binding from the alt A allele derepresses LMO1. | missing | none |
| cell_type | This occurs in neuroblastoma cells such as SK-N-SH. | missing | none |
| phenotype | Derepressed LMO1 increases neuroblastoma risk or malignant phenotype. | missing | none |

Predictions: C probe binds GATA2 more than A probe; GATA2 occupancy is stronger on the C allele; GATA2 knockdown increases LMO1 if GATA2 is repressive; A allele associates with higher LMO1 expression

Falsified if: EMSA supershift shows GATA3 rather than GATA2 binding at the variant.; GATA2 knockdown has no effect on LMO1 expression.; There is no allele-specific GATA2 binding.

### 4. H3_SOX10_alt_enhancer: SOX10 alt-A enhancer chain (p = 0.12)

TF SOX10 (stated coverage not_checked; registry own_model), alt allele binds more; element The alt A allele alters an LMO1 enhancer element recognized by SOX10 rather than by GATA factors.; gene LMO1; cell type Neuroblastoma cells, represented by SK-N-SH, with neural-crest transcription factor activity..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SOX10 binds the alt A allele more strongly than ref C at rs2168101. | missing | none |
| element | The alt A allele increases activity of a SOX10-responsive LMO1 enhancer element. | missing | none |
| gene | Increased enhancer activity raises LMO1 expression. | missing | none |
| cell_type | This occurs in neural-crest-derived neuroblastoma cells such as SK-N-SH. | missing | none |
| phenotype | Higher LMO1 promotes neuroblastoma risk or malignant phenotype. | missing | none |

Predictions: SOX10 binds A probe more than C probe; SOX10 occupies the LMO1 enhancer; SOX10 loss decreases LMO1 expression; GATA3/GATA2 antibodies do not supershift the allele-specific complex

Falsified if: SOX10 does not bind either allele at rs2168101.; SOX10 knockdown does not change LMO1 expression.; GATA3/GATA2 supershift explains the allele-specific binding.

## Prediction matrix

| Test | Cost | Separates top two | H1_GATA3_alt_activator | H0_null | H2_GATA2_ref_repressor_loss | H3_SOX10_alt_enhancer |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA with SK-N-SH nuclear extract plus GATA3 and GATA2 antibody supershifts | low | yes | A probe shifted more; GATA3 antibody supershifts the allele-specific complex | No reproducible allele-specific shifted complex | C probe shifted more; GATA2 antibody supershifts the allele-specific complex | A probe shifted more; SOX10 antibody supershifts, GATA antibodies do not |

## Next experiment

Cheapest single experiment separating H1 from H2: allele-specific EMSA using C and A rs2168101 probes with SK-N-SH nuclear extract, followed by anti-GATA3 and anti-GATA2 supershifts to determine both the preferred allele and the responsible TF.

## Flags

- none

## Evidence
