# rs13078086 and Colorectal cancer

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 1 model calls; 23 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: Null: no TF-mediated allelic effect at rs13078086 (p = 0.38)

Null chain: no TF-mediated effect of this variant.

Predictions: Ref and alt alleles show no reproducible allele-specific TF occupancy or enhancer activity in HCT116.; Any colorectal cancer association is explained by linkage disequilibrium with a nearby causal variant or by a passenger event, not by this base.

Falsified if: A robust ref-vs-alt difference in TF occupancy and enhancer activity is reproduced in colorectal cells.; The allelic effect is abolished by knockdown of the proposed TF.

### 2. H1: CDX2 binds the ref allele more strongly and activates a CCDC50 enhancer (p = 0.24)

TF CDX2 (QBiC-SELEX coverage own_model), ref allele binds more; element Putative CCDC50-associated enhancer at chr3:191441666; gene CCDC50; cell type HCT116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CDX2 is the best-supported intestinal TF for this site by motif similarity and colorectal expression; the ref T allele is predicted to bind CDX2 more strongly than the alt G allele. No CDX2 QBiC-SELEX model or ChIP data were supplied, so this is motif-based inference only. | missing | none |
| element | rs13078086 lies in a putative regulatory element near CCDC50, and the ref allele is predicted to preserve higher CDX2-dependent enhancer activity. | missing | none |
| gene | Altered enhancer activity changes CCDC50 expression in colorectal cells; CCDC50 is the nearest plausible target at this locus. | missing | none |
| cell_type | HCT116 is a colorectal carcinoma line with intestinal TF expression, making CDX2-dependent regulation plausible in this context. | missing | none |
| phenotype | Lower CDX2-dependent CCDC50 enhancer activity in carriers of the alt allele may modestly alter colorectal cancer cell behavior. | missing | none |

Predictions: Ref allele shows higher CDX2 ChIP signal than alt allele in HCT116.; Ref allele drives higher reporter activity, and CDX2 knockdown reduces ref reporter activity toward the alt level.; CCDC50 expression correlates with the ref allele in colorectal cell models.

Falsified if: No allele-specific CDX2 occupancy is detected at the variant.; Ref and alt reporters are equal, or the difference is not CDX2-dependent.

### 3. H2: TCF7L2 binds the alt allele more strongly and creates a Wnt-responsive CCDC50 element (p = 0.15)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element Putative CCDC50-associated enhancer at chr3:191441666; gene CCDC50; cell type HCT116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is a colorectal Wnt effector with a TCF/LEF motif related to the sequence context; the alt G allele is predicted to create or strengthen TCF7L2 binding relative to ref T. No TCF7L2 QBiC-SELEX model or ChIP data were supplied, so this is motif-based inference only. | missing | none |
| element | The alt allele is predicted to increase Wnt-responsive enhancer activity at this CCDC50-associated element. | missing | none |
| gene | Increased enhancer activity raises CCDC50 expression in colorectal cells. | missing | none |
| cell_type | HCT116 has active Wnt signaling, so TCF7L2-dependent enhancer effects are plausible in this line. | missing | none |
| phenotype | Alt-allele-associated CCDC50 upregulation may contribute to colorectal cancer phenotypes through Wnt-linked growth effects. | missing | none |

Predictions: Alt allele shows higher TCF7L2 ChIP signal than ref allele in HCT116.; Alt reporter is more active, and TCF7L2 knockdown reduces alt reporter activity.; Wnt stimulation increases the allelic reporter difference.

Falsified if: No allele-specific TCF7L2 occupancy is detected.; The reporter difference is not TCF7L2- or Wnt-dependent.

### 4. H3: FOXA1 binds the ref allele more strongly and maintains CCDC50 enhancer activity (p = 0.13)

TF FOXA1 (QBiC-SELEX coverage own_model), ref allele binds more; element Putative CCDC50-associated enhancer at chr3:191441666; gene CCDC50; cell type HCT116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is an endoderm/colorectal lineage TF with a T-rich motif; the ref T allele is predicted to bind FOXA1 more strongly than alt G. No FOXA1 QBiC-SELEX model or ChIP data were supplied, so this is motif-based inference only. | missing | none |
| element | The ref allele is predicted to preserve FOXA1-dependent enhancer activity at this CCDC50-associated element. | missing | none |
| gene | FOXA1-dependent enhancer activity alters CCDC50 expression in colorectal cells. | missing | none |
| cell_type | FOXA1 is expressed in colorectal epithelial cells and HCT116, making this regulatory route plausible. | missing | none |
| phenotype | Reduced FOXA1-dependent CCDC50 expression in alt carriers may modify colorectal cancer phenotypes. | missing | none |

Predictions: Ref allele shows higher FOXA1 ChIP signal than alt allele.; Ref reporter is more active, and FOXA1 knockdown reduces ref reporter activity.; FOXA1 depletion changes CCDC50 expression in HCT116.

Falsified if: No allele-specific FOXA1 occupancy is detected.; FOXA1 knockdown does not affect the allelic reporter difference.

### 5. H4: CTCF binds the ref allele more strongly and alters a CCDC50 chromatin boundary (p = 0.10)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element Putative CCDC50-associated CTCF boundary element at chr3:191441666; gene CCDC50; cell type HCT116 colorectal carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is a chromatin-boundary factor; the ref T allele is predicted to bind CTCF more strongly than alt G at this site. No CTCF QBiC-SELEX model or ChIP data were supplied, so this is motif-based inference only. | missing | none |
| element | The variant lies in a putative CTCF boundary element whose occupancy is reduced by the alt allele. | missing | none |
| gene | Altered CTCF boundary activity changes CCDC50 regulatory contacts or expression in colorectal cells. | missing | none |
| cell_type | CTCF occupancy and chromatin looping are measurable in HCT116 colorectal carcinoma cells. | missing | none |
| phenotype | Disrupted CTCF-dependent CCDC50 regulation in alt carriers may contribute to colorectal cancer risk or progression. | missing | none |

Predictions: Ref allele shows higher CTCF ChIP signal than alt allele.; Alt allele alters local chromatin contacts or CCDC50 expression without changing a simple enhancer reporter.; CTCF knockdown mimics the alt-allele chromatin state.

Falsified if: No allele-specific CTCF occupancy is detected.; Chromatin contact or expression differences do not track the allele.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific enhancer reporter in HCT116 with and without CDX2 knockdown | medium | yes | Ref and alt reporters are equal; no CDX2-dependent allelic effect. | Ref reporter is higher; CDX2 knockdown reduces ref toward alt. | Alt reporter is higher; TCF7L2 knockdown reduces alt. | Ref reporter is higher and FOXA1 knockdown selectively reduces ref. | No simple reporter difference, but CTCF occupancy or chromatin contacts differ by allele. |
| Allele-specific CDX2 ChIP-qPCR over rs13078086 in HCT116 | medium | yes | No reproducible ref-vs-alt CDX2 occupancy difference. | Ref allele shows higher CDX2 occupancy. | No CDX2 allelic difference; TCF7L2 may instead show alt-specific occupancy. | CDX2 allelic difference is absent or weaker than FOXA1 allelic difference. | No CDX2 allelic difference; CTCF shows ref-specific occupancy. |
| CRISPRi of the rs13078086 element in HCT116 followed by CCDC50 expression | high | no | No allele-dependent change in CCDC50 expression. | Element repression lowers CCDC50 more strongly on the ref allele in a CDX2-dependent manner. | Element repression lowers CCDC50 more strongly on the alt allele in a TCF7L2-dependent manner. | Element repression lowers CCDC50 more strongly on the ref allele in a FOXA1-dependent manner. | Element repression changes chromatin contacts more than steady-state CCDC50 expression. |

## Next experiment

Cheapest discriminating experiment: allele-specific luciferase reporter for ref vs alt in HCT116, with and without CDX2 siRNA. A ref-higher, CDX2-dependent signal supports H1; no allelic difference supports H0.

## Flags

- none

## Evidence
