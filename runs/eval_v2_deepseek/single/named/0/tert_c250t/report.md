# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 1 model calls; 28 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: GABPA gains an alt-specific TERT promoter site and activates TERT in glioblastoma (p = 0.55)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter C250T (chr5:1295135 G>A); gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA binds the alt A allele more strongly than the ref G allele because C250T creates a de novo ETS/GABP motif. GABPA is chosen as the canonical ETS-family DNA-binding subunit recruited by TERT promoter mutations; no QBiC-SELEX model is given here, so this is motif- and literature-based and requires occupancy testing. | missing | none |
| element | The variant lies in the TERT promoter and alters a cis-regulatory ETS/GABP motif. | missing | none |
| gene | The element regulates TERT transcription. | missing | none |
| cell_type | Glioblastoma cells commonly carry TERT promoter mutations and express TERT. | missing | none |
| phenotype | Increased TERT transcription and telomerase activity support immortalization and tumor maintenance, contributing to glioblastoma. | missing | none |

Predictions: GABPA ChIP enriches the alt A allele over ref G at chr5:1295135 in a heterozygous glioblastoma line.; The alt allele increases TERT reporter expression, and GABPA knockdown reduces this alt-specific increase.; TERT expression is higher in glioblastoma lines carrying C250T than in ref lines, other things being equal.

Falsified if: GABPA shows no allele-specific occupancy at the variant in heterozygous glioblastoma cells.; The alt allele does not increase TERT reporter activity, or GABPA knockdown does not reduce any alt-specific effect.

### 2. H4: Null: no TF-mediated allelic effect from C250T (p = 0.22)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy is detected at chr5:1295135.; Ref G and alt A TERT promoter reporters behave equivalently in the relevant cell type.; Any disease association is explained by a linked causal variant, passenger mutation at a recurrent TERT promoter hotspot, or no allelic effect.

Falsified if: Allele-specific GABPA or another ETS-factor occupancy is demonstrated at the variant and paired with an allelic TERT expression effect.

### 3. H2: ETS1 gains an alt-specific site and activates TERT in glioblastoma (p = 0.15)

TF ETS1 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter C250T (chr5:1295135 G>A); gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETS1 binds the alt A allele more strongly than the ref G allele through the ETS motif created by C250T. ETS1 shares ETS-family specificity with GABPA; no QBiC-SELEX model is given for ETS1 here, so this is weaker than the GABPA explanation and needs occupancy evidence. | missing | none |
| element | The variant lies in the TERT promoter and creates a candidate ETS1-binding site. | missing | none |
| gene | The element regulates TERT transcription. | missing | none |
| cell_type | Glioblastoma cells express ETS-family factors and express TERT. | missing | none |
| phenotype | ETS1-driven TERT activation increases telomerase activity and supports tumor maintenance in glioblastoma. | missing | none |

Predictions: ETS1 ChIP enriches the alt A allele over ref G at the variant, while GABPA does not.; ETS1 knockdown, not GABPA knockdown, reduces the alt-specific TERT reporter increase.

Falsified if: ETS1 shows no allele-specific occupancy at the variant.; GABPA, rather than ETS1, is the ETS factor whose knockdown reverses the alt-specific TERT increase.

### 4. H3: GABPA binds the alt allele but does not activate TERT in glioblastoma (p = 0.08)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter C250T (chr5:1295135 G>A); gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA binds the alt A allele more strongly than ref G, but this binding may be repressive or context-dependent rather than activating. No QBiC-SELEX model is given, so the direction is motif-based and requires occupancy and functional testing. | missing | none |
| element | The variant lies in the TERT promoter and alters a GABPA-binding ETS motif. | missing | none |
| gene | The element is in the TERT promoter, but the allelic effect on TERT transcription is not necessarily activating. | missing | none |
| cell_type | Glioblastoma cells can have TERT promoter mutations without a simple proportional increase in TERT from the mutant allele. | missing | none |
| phenotype | Any disease contribution would not be through increased TERT activation from this allele, or would require additional context. | missing | none |

Predictions: GABPA ChIP enriches the alt A allele, but the alt allele does not increase TERT reporter expression.; GABPA knockdown does not reduce TERT expression in C250T-heterozygous glioblastoma cells, or increases it.

Falsified if: The alt allele increases TERT reporter activity and GABPA knockdown specifically reduces that increase.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ChIP-qPCR for GABPA and ETS1 at chr5:1295135, with TERT expression readout, in a heterozygous glioblastoma line | low | yes | GABPA enriches the alt A allele over ref G, and TERT expression is higher from the alt allele. | Neither GABPA nor ETS1 shows allele-specific occupancy, and there is no allelic TERT expression difference. | ETS1 enriches the alt A allele over ref G, while GABPA does not, and TERT expression is higher from the alt allele. | GABPA enriches the alt A allele, but TERT expression is not higher from the alt allele. |
| TERT promoter luciferase reporter with ref G versus alt A, plus GABPA or ETS1 knockdown, in glioblastoma cells | medium | yes | Alt increases reporter activity, and GABPA knockdown reduces the alt-specific increase. | Ref and alt reporters are equivalent. | Alt increases reporter activity, and ETS1 knockdown reduces the alt-specific increase, while GABPA knockdown does not. | Alt does not increase reporter activity despite GABPA occupancy. |
| Reanalyze existing glioblastoma ChIP-seq/ATAC data for GABPA and ETS1 occupancy over the TERT promoter variant | existing data | no | A GABPA occupancy peak overlaps the variant. | No relevant TF occupancy or open-chromatin signal overlaps the variant. | An ETS1 occupancy peak overlaps the variant without a GABPA peak. |  |

## Next experiment

Allele-specific ChIP-qPCR for GABPA and ETS1 at chr5:1295135 in a heterozygous glioblastoma line, with a TERT expression readout; this is the cheapest direct test separating the GABPA and ETS1 chains.

## Flags

- none

## Evidence
