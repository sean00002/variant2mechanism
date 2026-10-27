# rs6983267 and Colorectal cancer (8q24)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 23 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. C1: TCF7L2 binds the G risk allele more strongly and activates MYC (p = 0.45)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element rs6983267 lies in a candidate 8q24 enhancer element whose activity is allele-dependent.; gene MYC; cell type HCT 116 colorectal carcinoma epithelial cell line (DepMap ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref G allele more strongly than the alt T allele at rs6983267; TCF7L2 is chosen as the canonical TCF/LEF-family colorectal enhancer factor, but no QBiC-SELEX evidence list was supplied. | missing | none |
| element | The ref G allele increases activity of the candidate 8q24 enhancer element containing rs6983267. | missing | none |
| gene | The enhancer element regulates the nearby MYC oncogene, increasing MYC expression when the G allele is present. | missing | none |
| cell_type | The effect occurs in colorectal carcinoma epithelial cells, represented by HCT 116. | missing | none |
| phenotype | G allele-dependent TCF7L2 enhancer activity and higher MYC expression increase colorectal cancer risk. | missing | none |

Predictions: Allele-specific TCF7L2 ChIP or EMSA shows ref G > alt T binding at rs6983267.; A G-versus-T enhancer reporter shows higher activity for G in HCT 116 cells.; MYC expression is higher with the G allele in an allele-sensitive colorectal cell context.; G is the risk-associated allele for colorectal cancer.

Falsified if: TCF7L2 binding is not stronger on the ref G allele than the alt T allele at rs6983267.; The G allele does not increase enhancer activity or MYC expression in HCT 116 cells.; The disease association is fully explained by a linked variant and not by rs6983267.

### 2. C4: Null: no TF-mediated allelic effect at rs6983267 (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs6983267.; No allele-specific enhancer activity or MYC expression difference attributable to rs6983267.; Any colorectal cancer association is due to a linked causal variant, a passenger event, or no allelic effect.

Falsified if: A reproducible allele-specific TF binding difference and allele-specific enhancer/MYC effect are shown at rs6983267 in colorectal cells.; The disease association at rs6983267 is shown to be independent of linked variants and dependent on this variant's enhancer activity.

### 3. C2: TCF7L2 binds the T allele more strongly and represses MYC (p = 0.15)

TF TCF7L2 (stated coverage not_checked; registry mapped), alt allele binds more; element rs6983267 lies in a candidate 8q24 enhancer element whose activity is allele-dependent.; gene MYC; cell type HCT 116 colorectal carcinoma epithelial cell line (DepMap ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the alt T allele more strongly than the ref G allele at rs6983267; this is a competing direction-of-effect model. | missing | none |
| element | The alt T allele increases TCF7L2-bound enhancer activity, but the enhancer acts as a repressive element in this context. | missing | none |
| gene | TCF7L2-bound repression lowers MYC expression. | missing | none |
| cell_type | The repressive effect occurs in colorectal carcinoma epithelial cells, represented by HCT 116. | missing | none |
| phenotype | Lower MYC expression associated with the alt T allele reduces colorectal cancer risk. | missing | none |

Predictions: Allele-specific TCF7L2 binding shows alt T > ref G at rs6983267.; A T-versus-G enhancer reporter is more active for T, but MYC expression is lower with T.; T is protective relative to G for colorectal cancer.; TCF7L2 knockdown reverses the allele-dependent MYC effect.

Falsified if: TCF7L2 binding is not stronger on the alt T allele than the ref G allele at rs6983267.; The T allele does not reduce MYC expression in HCT 116 cells.; The variant effect is not repressive or is not mediated by TCF7L2.

### 4. C3: A related TCF/LEF factor TCF7L1 mediates the G-allele effect (p = 0.10)

TF TCF7L1 (stated coverage not_checked; registry own_model), ref allele binds more; element rs6983267 lies in a candidate 8q24 enhancer element whose activity is allele-dependent.; gene MYC; cell type HCT 116 colorectal carcinoma epithelial cell line (DepMap ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | A related TCF/LEF-family factor, TCF7L1, rather than TCF7L2, binds the ref G allele more strongly at rs6983267; this competing family member is not distinguished without QBiC-SELEX, expression, and ChIP evidence. | missing | none |
| element | The G allele increases activity of the candidate 8q24 enhancer element through TCF7L1. | missing | none |
| gene | TCF7L1-bound enhancer activity increases MYC expression. | missing | none |
| cell_type | The effect occurs in colorectal carcinoma epithelial cells, represented by HCT 116. | missing | none |
| phenotype | G allele-dependent TCF7L1 activity and higher MYC expression increase colorectal cancer risk. | missing | none |

Predictions: Allele-specific ChIP shows TCF7L1 binding is G > T at rs6983267.; TCF7L1 knockdown, but not TCF7L2 knockdown, reduces the allele-dependent enhancer/MYC effect.; The G allele remains risk-associated in colorectal cancer.

Falsified if: TCF7L1 binding is not stronger on the ref G allele at rs6983267.; TCF7L2, rather than TCF7L1, accounts for the allele-specific binding and enhancer effect.; The MYC effect is not TCF7L1-dependent.

## Prediction matrix

| Test | Cost | Separates top two | C1 | C4 | C2 | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 binding assay at rs6983267 in HCT 116: EMSA with ref-G and alt-T probes, or allele-specific ChIP-qPCR if the cells are heterozygous. | low | yes | ref G binds TCF7L2 more than alt T | no allele-specific TF binding at rs6983267 | alt T binds TCF7L2 more than ref G | ref G binds TCF7L1 more than alt T |
| G-versus-T enhancer luciferase reporter in HCT 116 cells, with and without TCF7L2 knockdown. | low | no | G enhancer is more active and increases MYC reporter activity | no allele-specific enhancer activity | T enhancer is more active but represses MYC reporter activity | G enhancer activity is TCF7L1-dependent |
| Allele-specific MYC expression measurement after CRISPR base editing or allele-specific enhancer perturbation at the endogenous 8q24 locus in HCT 116. | medium | no | G allele raises endogenous MYC | no rs6983267-dependent MYC difference | T allele lowers endogenous MYC | G allele raises endogenous MYC in a TCF7L1-dependent way |

## Next experiment

The single cheapest first experiment separating the top two chains, C1 and C4, is an allele-specific TCF7L2 binding assay at rs6983267 in HCT 116: EMSA with ref-G and alt-T probes, or allele-specific ChIP-qPCR if HCT 116 is heterozygous. It tests whether ref G binds TCF7L2 more strongly, as C1 predicts, or whether there is no allelic binding difference, as C4 predicts. It does not by itself test enhancer activity, MYC expression, or a linked causal variant; those require reporter/expression or LD/fine-mapping follow-up.

## Flags

- none

## Evidence
