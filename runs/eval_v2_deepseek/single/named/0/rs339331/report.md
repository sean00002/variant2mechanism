# rs339331 and Prostate cancer (6q22)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 2 model calls; 80 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. H_null: No TF-mediated allelic effect; linked causal variant or passenger (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy over rs339331 in prostate cells.; Ref and alt reporter constructs show similar activity in LNCaP.; RFX6 expression is not associated with rs339331 genotype after controlling for linked variants.

Falsified if: Allele-specific HOXB13 occupancy at rs339331 is reproducibly detected and the element shows HOXB13-dependent allele-specific reporter activity.

### 2. H_hoxb13_ref: HOXB13 binds ref T more, increasing RFX6 in prostate cells (p = 0.35)

TF HOXB13 (QBiC-SELEX coverage own_model), ref allele binds more; element prostate enhancer at 6q22 containing rs339331; gene RFX6; cell type LNCaP prostate adenocarcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 binds the ref T allele more strongly than alt C at rs339331. HOXB13 was chosen as a prostate-lineage TF with a literature-linked HOXB13/RFX6 mechanism at 6q22; no QBiC-SELEX evidence is provided, so this is not based on a QBiC-SELEX model. | missing | none |
| element | rs339331 lies in a cis-regulatory enhancer element at 6q22; the ref allele preserves a stronger HOXB13 binding site. | missing | none |
| gene | Increased HOXB13 occupancy at this enhancer increases RFX6 transcription; this assumes HOXB13 acts as an activator at this element. | missing | none |
| cell_type | LNCaP prostate adenocarcinoma cells have prostate-lineage chromatin and express HOXB13/RFX6, making this element relevant in the DepMap LNCaP context. | missing | none |
| phenotype | Higher RFX6 expression in prostate epithelium increases prostate cancer risk or progression. | missing | none |

Predictions: Ref T allele shows stronger HOXB13 occupancy than alt C at rs339331.; Ref reporter is more active than alt in LNCaP and this difference is reduced by HOXB13 knockdown.; RFX6 expression is higher with the ref allele.

Falsified if: No ref>alt HOXB13 occupancy is detected at rs339331, or the reporter/expression difference is not HOXB13-dependent.

### 3. H_hoxb13_alt: HOXB13 binds alt C more, increasing RFX6 in prostate cells (p = 0.15)

TF HOXB13 (QBiC-SELEX coverage own_model), alt allele binds more; element prostate enhancer at 6q22 containing rs339331; gene RFX6; cell type LNCaP prostate adenocarcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 binds the alt C allele more strongly than ref T at rs339331. HOXB13 was chosen as above; no QBiC-SELEX evidence is provided, so this direction is a competing sequence-context hypothesis. | missing | none |
| element | rs339331 lies in a cis-regulatory enhancer element at 6q22; the alt allele creates a stronger HOXB13 binding site. | missing | none |
| gene | Increased HOXB13 occupancy at this enhancer increases RFX6 transcription; this assumes HOXB13 acts as an activator at this element. | missing | none |
| cell_type | LNCaP prostate adenocarcinoma cells have prostate-lineage chromatin and express HOXB13/RFX6, making this element relevant in the DepMap LNCaP context. | missing | none |
| phenotype | Higher RFX6 expression in prostate epithelium increases prostate cancer risk or progression. | missing | none |

Predictions: Alt C allele shows stronger HOXB13 occupancy than ref T at rs339331.; Alt reporter is more active than ref in LNCaP and this difference is reduced by HOXB13 knockdown.; RFX6 expression is higher with the alt allele.

Falsified if: No alt>ref HOXB13 occupancy is detected at rs339331, or the reporter/expression difference is not HOXB13-dependent.

### 4. H_foxa1_alt: FOXA1 binds alt C more at the 6q22 element and alters RFX6 (p = 0.10)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element prostate enhancer at 6q22 containing rs339331; gene RFX6; cell type LNCaP prostate adenocarcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 binds the alt C allele more strongly than ref T at rs339331. FOXA1 was chosen as a prostate pioneer TF that can occupy prostate enhancers; no QBiC-SELEX evidence is provided. | missing | none |
| element | rs339331 lies in a cis-regulatory enhancer element at 6q22; the alt allele creates a stronger FOXA1 binding site. | missing | none |
| gene | Increased FOXA1 occupancy at this enhancer increases RFX6 transcription or accessibility; this assumes FOXA1 acts as an activator at this element. | missing | none |
| cell_type | LNCaP prostate adenocarcinoma cells have FOXA1 and prostate-lineage chromatin, making this element relevant in the DepMap LNCaP context. | missing | none |
| phenotype | Higher RFX6 expression in prostate epithelium increases prostate cancer risk or progression. | missing | none |

Predictions: Alt C allele shows stronger FOXA1 occupancy than ref T at rs339331.; Alt reporter is more active than ref in LNCaP and this difference is reduced by FOXA1 knockdown.; RFX6 expression is higher with the alt allele.

Falsified if: No FOXA1 occupancy is detected at rs339331, or the alt-specific reporter/expression effect is not FOXA1-dependent.

## Prediction matrix

| Test | Cost | Separates top two | H_null | H_hoxb13_ref | H_hoxb13_alt | H_foxa1_alt |
| --- | --- | --- | --- | --- | --- | --- |
| allele_specific_HOXB13_ChIP | low | yes | no allelic imbalance | ref > alt | alt > ref | no HOXB13 imbalance; FOXA1 alt > ref |

## Next experiment

Allele-specific HOXB13 ChIP-qPCR over rs339331 in LNCaP (or a heterozygous prostate cell line if LNCaP is homozygous). It is the cheapest direct separator: the null predicts no allelic HOXB13 imbalance, while the HOXB13-ref chain predicts ref T > alt C occupancy.

## Flags

- none

## Evidence
