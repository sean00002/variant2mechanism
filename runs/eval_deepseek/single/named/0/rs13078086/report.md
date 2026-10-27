# rs13078086 and Colorectal cancer

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 1 model calls; 32 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H4: No TF-mediated allelic effect; linked causal variant or passenger (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding is seen at rs13078086.; LPP expression is not associated with rs13078086 genotype after controlling for linked variants.; Perturbing the local element does not produce an allele-dependent LPP or colorectal cancer phenotype.

Falsified if: A reproducible allele-specific TF binding effect and allele-dependent LPP expression are demonstrated at rs13078086.

### 2. H1: Alt G strengthens a TCF7L2 site in a 3q28 enhancer and raises LPP (p = 0.30)

TF TCF7L2 (stated coverage not_checked; registry mapped), alt allele binds more; element 3q28 enhancer near LPP; gene LPP; cell type HCT116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt G allele at rs13078086 is predicted to bind TCF7L2 more strongly than the ref T allele. | missing | none |
| element | The variant lies in a cis-regulatory enhancer at 3q28 near LPP. | missing | none |
| gene | Stronger TCF7L2 binding at this element increases LPP transcription. | missing | none |
| cell_type | HCT116 cells have active Wnt/TCF7L2 signaling and express LPP. | missing | none |
| phenotype | Increased LPP expression promotes colorectal cancer risk. | missing | none |

Predictions: Allele-specific TCF7L2 binding assays in HCT116 nuclear extract show G > T binding at rs13078086.; The G allele increases enhancer reporter activity and LPP expression in colorectal cells.; CRISPRi of the 3q28 element reduces LPP expression in HCT116.

Falsified if: No reproducible allele-specific TCF7L2 binding is seen at rs13078086.; The variant does not affect LPP expression or enhancer activity in colorectal cells.

### 3. H2: Ref T strengthens a CDX2 site in the same 3q28 element and raises LPP (p = 0.15)

TF CDX2 (stated coverage not_checked; registry own_model), ref allele binds more; element 3q28 enhancer near LPP; gene LPP; cell type HCT116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref T allele at rs13078086 is predicted to bind CDX2 more strongly than the alt G allele. | missing | none |
| element | The variant lies in an intestinal enhancer at 3q28 near LPP. | missing | none |
| gene | CDX2 binding at this element increases LPP transcription. | missing | none |
| cell_type | HCT116 is a colorectal cell line with CDX2 expression. | missing | none |
| phenotype | Altered LPP expression changes colorectal cancer risk. | missing | none |

Predictions: Allele-specific CDX2 binding shows T > G at rs13078086.; The T allele increases enhancer reporter activity, and CDX2 knockdown reduces LPP.; The effect is attenuated by CDX2 depletion but not by TCF7L2 depletion.

Falsified if: CDX2 binding is not allele-specific at this variant.; CDX2 knockdown does not change LPP expression from this element.

### 4. H3: Alt G strengthens an HNF4A site that represses LPP (p = 0.15)

TF HNF4A (stated coverage not_checked; registry own_model), alt allele binds more; element 3q28 enhancer near LPP; gene LPP; cell type HCT116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt G allele at rs13078086 is predicted to bind HNF4A more strongly than the ref T allele. | missing | none |
| element | The variant lies in a regulatory element at 3q28 near LPP. | missing | none |
| gene | Stronger HNF4A binding represses LPP transcription. | missing | none |
| cell_type | HCT116 cells express HNF4A and use it in colorectal regulatory programs. | missing | none |
| phenotype | Reduced LPP expression modifies colorectal cancer risk. | missing | none |

Predictions: Allele-specific HNF4A binding shows G > T at rs13078086.; The G allele reduces LPP expression in reporter and endogenous assays.; HNF4A knockdown increases LPP expression.

Falsified if: HNF4A binding is not allele-specific at this variant.; The G allele does not reduce LPP expression, or HNF4A knockdown does not increase LPP.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA or oligo pull-down for TCF7L2 with HCT116 nuclear extract, comparing T and G probes | low | yes | No reproducible allele-specific TCF7L2 binding | G probe shows stronger TCF7L2 binding than T |  |  |
| TCF7L2 ChIP-qPCR at the rs13078086 element in HCT116 with allelic imbalance measurement | low | yes | No TCF7L2 enrichment or no allelic imbalance | Element is TCF7L2-bound and ChIP shows allelic imbalance favoring G |  |  |
| Enhancer reporter assay with T versus G alleles in HCT116 | medium | no | No allele-dependent reporter activity | G allele increases reporter activity |  |  |
| eQTL or allele-specific expression lookup for LPP by rs13078086 genotype in colorectal datasets | existing data | yes | No association after controlling linked variants | G allele associates with higher LPP expression |  |  |

## Next experiment

Cheapest discriminating test: allele-specific EMSA or oligo pull-down with HCT116 nuclear extract and anti-TCF7L2, comparing ref-T and alt-G probes at rs13078086; a G-specific TCF7L2 shift supports H1, while no reproducible allele difference supports the null.

## Flags

- none

## Evidence
