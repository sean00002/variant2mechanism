# rs6983267 and Colorectal cancer (8q24)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 20 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. A: TCF7L2-bound enhancer activates MYC (p = 0.55)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element rs6983267 lies in an allele-specific distal enhancer at 8q24; the ref G allele increases enhancer activity.; gene MYC; cell type colorectal cancer epithelial cells, represented by HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref G allele more strongly than the alt T allele at rs6983267; the G allele matches the TCF7L2/TCF4 motif and TCF7L2 is expressed in HCT116. No QBiC-SELEX evidence ID is supplied. | missing | none |
| element | rs6983267 is in a distal enhancer whose activity is higher on the ref G allele. | missing | none |
| gene | The enhancer regulates MYC. | missing | none |
| cell_type | The relevant cell type is colorectal cancer epithelium, represented by HCT116. | missing | none |
| phenotype | Higher TCF7L2 binding on the G allele increases MYC expression and raises colorectal cancer risk. | missing | none |

Predictions: TCF7L2 ChIP is higher on G than T at this base.; An allele-specific enhancer reporter gives G > T activity in HCT116.; MYC expression is higher with G than T in an isogenic HCT116 background.; The G allele is the colorectal cancer risk allele.

Falsified if: The G allele does not show stronger TCF7L2 occupancy than the T allele in an allele-specific assay.; The G allele does not increase enhancer reporter activity or MYC expression in HCT116.; Loss of TCF7L2 does not reduce the G-allele-specific enhancer effect.

### 2. B: TCF7L2-bound enhancer represses MYC (p = 0.25)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element rs6983267 lies in an allele-specific distal enhancer at 8q24; the ref G allele increases TCF7L2 occupancy but this occupancy is repressive.; gene MYC; cell type colorectal cancer epithelial cells, represented by HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref G allele more strongly than the alt T allele at rs6983267; the G allele matches the TCF7L2/TCF4 motif and TCF7L2 is expressed in HCT116. No QBiC-SELEX evidence ID is supplied. | missing | none |
| element | rs6983267 is in a distal enhancer whose regulatory output is altered by TCF7L2 occupancy. | missing | none |
| gene | The enhancer regulates MYC. | missing | none |
| cell_type | The relevant cell type is colorectal cancer epithelium, represented by HCT116. | missing | none |
| phenotype | TCF7L2 binding on the G allele represses MYC, and this context-dependent change raises colorectal cancer risk. | missing | none |

Predictions: TCF7L2 ChIP is higher on G than T at this base.; An allele-specific enhancer reporter gives G < T activity in HCT116.; MYC expression is lower with G than T in an isogenic HCT116 background.; The G allele is still the colorectal cancer risk allele, but not through increased MYC.

Falsified if: The G allele increases rather than decreases enhancer reporter activity or MYC expression in HCT116.; TCF7L2 loss does not relieve repression on the G allele.

### 3. NULL: No TCF7L2-mediated allelic effect at this base (p = 0.20)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TCF7L2 occupancy at rs6983267.; No allele-specific enhancer reporter activity for the isolated SNP.; No allele-specific MYC expression change when only rs6983267 is swapped.; Any colorectal cancer association is explained by a linked causal variant or another non-TF mechanism.

Falsified if: An allele-specific TCF7L2 occupancy assay shows G > T binding at this base.; An isolated rs6983267 G vs T enhancer reporter shows allele-specific activity in HCT116.; Isogenic allele replacement changes MYC expression in HCT116.

## Prediction matrix

| Test | Cost | Separates top two | A | B | NULL |
| --- | --- | --- | --- | --- | --- |
| allele-specific enhancer reporter | high | yes |  |  |  |

## Next experiment

Allele-specific luciferase reporter containing the rs6983267 G or T enhancer plus a MYC promoter in HCT116 cells: G > T supports chain A, G < T supports chain B, and no allelic difference supports the null.

## Flags

- none

## Evidence
