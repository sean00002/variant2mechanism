# rs13078086 and Colorectal cancer

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 1 model calls; 34 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: Null: no TF-mediated allelic effect; linked causal variant or passenger signal (p = 0.45)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at the variant in HCT116.; No allele-specific enhancer activity; disease association reflects LD with another causal variant or chance.

Falsified if: Allele-specific TF binding at rs13078086 is reproducibly detected in HCT116 cells and tracks with an allele-specific enhancer/reporter signal.; CRISPR editing of rs13078086 T>G in HCT116 changes expression of a nearby gene in the predicted direction.

### 2. H1: CDX2 loss at the alt G allele reduces a 3q28 enhancer regulating TP63 (p = 0.30)

TF CDX2 (stated coverage not_checked; registry own_model), ref allele binds more; element rs13078086 lies in a distal non-coding enhancer element near the 3q28 CRC risk locus; the ref T allele preserves a CDX2-binding site and the alt G allele weakens it.; gene TP63; cell type HCT 116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CDX2 binds the ref T allele more strongly than the alt G allele at rs13078086; QBiC-SELEX coverage for CDX2 is not_checked because no screen row or qbic_tf_detail lookup is available in this no-evidence setting. | missing | none |
| element | The variant sits in a distal enhancer element whose activity is allele-dependent, with ref T supporting stronger CDX2-dependent enhancer activity. | missing | none |
| gene | This enhancer regulates a nearby 3q28 target gene, most plausibly TP63 in this locus context. | missing | none |
| cell_type | The effect is cell-type dependent and detectable in HCT116 colorectal carcinoma cells, where CDX2 is expressed. | missing | none |
| phenotype | Reduced CDX2-dependent enhancer activity at the alt G allele modestly increases colorectal cancer risk, consistent with the GWAS signal. | missing | none |

Predictions: Allele-specific CDX2 ChIP or EMSA: ref T > alt G.; Reporter/STARR-seq in HCT116: ref T enhancer activity > alt G.; CDX2 knockdown reduces enhancer activity and target-gene expression in HCT116.

Falsified if: Allele-specific ChIP/EMSA shows no CDX2 binding or no T>G preference at this position.; CRISPR-editing the variant does not alter the candidate target gene or enhancer activity.; CDX2 knockdown does not reduce enhancer activity in HCT116.

### 3. H2: FOXA1 gain at the alt G allele activates a 3q28 enhancer near FGF12 (p = 0.15)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element rs13078086 lies in a distal non-coding enhancer; the alt G allele creates or strengthens a FOXA1-binding site and increases enhancer activity.; gene FGF12; cell type HCT 116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 binds the alt G allele more strongly than the ref T allele at rs13078086; QBiC-SELEX coverage for FOXA1 is not_checked because no screen row or qbic_tf_detail lookup is available. | missing | none |
| element | The variant lies in a distal enhancer element whose activity is increased by the alt G allele in a FOXA1-dependent manner. | missing | none |
| gene | This enhancer regulates a nearby 3q28 gene, with FGF12 as an alternative candidate to TP63. | missing | none |
| cell_type | The effect is detectable in HCT116 colorectal carcinoma cells, where FOXA1 is expressed. | missing | none |
| phenotype | Gain of FOXA1-dependent enhancer activity at the alt G allele modestly increases colorectal cancer risk. | missing | none |

Predictions: Allele-specific FOXA1 ChIP or EMSA: alt G > ref T.; Reporter/STARR-seq in HCT116: alt G enhancer activity > ref T.; FOXA1 knockdown reduces alt-allele enhancer activity and target-gene expression.

Falsified if: Allele-specific ChIP/EMSA shows no FOXA1 binding or no G> T preference.; FOXA1 knockdown does not affect the candidate enhancer or target gene in HCT116.; Reporter assays show no alt-allele gain of enhancer activity.

### 4. H3: TFAP2A loss at the alt G allele reduces a 3q28 enhancer regulating TP63 (p = 0.10)

TF TFAP2A (stated coverage not_checked; registry own_model), ref allele binds more; element rs13078086 lies in a distal non-coding enhancer; the ref T allele supports stronger TFAP2A binding and enhancer activity.; gene TP63; cell type HCT 116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A binds the ref T allele more strongly than the alt G allele at rs13078086; QBiC-SELEX coverage for TFAP2A is not_checked because no screen row or qbic_tf_detail lookup is available. | missing | none |
| element | The variant lies in a distal enhancer element whose activity is allele-dependent, with ref T supporting stronger TFAP2A-dependent activity. | missing | none |
| gene | This enhancer regulates TP63 at the 3q28 locus. | missing | none |
| cell_type | The effect is detectable in HCT116 colorectal carcinoma cells, where TFAP2A is expressed. | missing | none |
| phenotype | Reduced TFAP2A-dependent enhancer activity at the alt G allele modestly increases colorectal cancer risk. | missing | none |

Predictions: Allele-specific TFAP2A ChIP or EMSA: ref T > alt G.; Reporter/STARR-seq in HCT116: ref T enhancer activity > alt G.; TFAP2A knockdown reduces enhancer activity and TP63 expression in HCT116.

Falsified if: Allele-specific ChIP/EMSA shows no TFAP2A binding or no T>G preference.; TFAP2A knockdown does not alter the candidate enhancer or target gene in HCT116.; CRISPR editing does not change TP63 or nearby gene expression.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA with HCT116 nuclear extract using ref-T and alt-G probes, plus anti-CDX2/anti-FOXA1 supershifts | low | yes | no allele-specific shift or supershift | ref T shift stronger; anti-CDX2 supershifts | alt G shift stronger; anti-FOXA1 supershifts | ref T shift stronger; anti-TFAP2A supershifts |

## Next experiment

Single cheapest experiment to separate the top two chains (H0 null vs H1 CDX2): allele-specific EMSA in HCT116 nuclear extract comparing ref-T and alt-G probes, with an anti-CDX2 supershift; a clear ref-T-specific CDX2 shift supports H1, while no reproducible allele-specific shift supports H0. Adding anti-FOXA1 in the same gel also separates H2 if needed.

## Flags

- none

## Evidence
