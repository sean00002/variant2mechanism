# rs73706717 and Colorectal cancer (8q24)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 1 model calls; 30 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0_null: No TF-mediated effect of rs73706717; association is linked or passenger (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at rs73706717 in HCT116.; Any 8q24 CRC signal is explained by a linked causal variant or by LD with a nearby variant such as rs6983267.; CRISPR allele swap at rs73706717 alone does not change enhancer activity or MYC expression.

Falsified if: A robust allele-specific TF binding and enhancer/MYC effect is seen at rs73706717 in HCT116.; CRISPR swap of rs73706717 alone changes MYC expression.; The effect remains after controlling for linked 8q24 variants.

### 2. H1_TCF7L2_alt: Alt C increases TCF7L2 binding at the 8q24 enhancer, raising MYC in HCT116 and promoting CRC (p = 0.25)

TF TCF7L2 (stated coverage not_checked; registry mapped), alt allele binds more; element 8q24.21 enhancer near MYC; gene MYC; cell type HCT116 colorectal adenocarcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt C allele creates or strengthens a TCF7L2/TCF4-family binding site in the 8q24.21 enhancer; TCF7L2 binds alt C more strongly than ref T. | missing | none |
| element | This variant lies in an 8q24.21 enhancer element active in colorectal cancer cells; the alt C allele increases enhancer output. | missing | none |
| gene | The enhancer contacts and regulates MYC, so increased TCF7L2 binding at alt C raises MYC transcription. | missing | none |
| cell_type | HCT116 has active Wnt/TCF7L2 signaling and expresses MYC, making this enhancer-TF axis plausible in this cell line. | missing | none |
| phenotype | Higher MYC output in colorectal epithelium increases colorectal cancer risk or progression. | missing | none |

Predictions: Allele-specific TCF7L2 ChIP or EMSA shows alt C > ref T binding in HCT116.; An enhancer reporter in HCT116 shows alt C > ref T activity.; MYC mRNA is higher in cells carrying alt C at this element.; TCF7L2 knockdown reduces the alt-C-specific enhancer/MYC effect.

Falsified if: Alt C does not increase TCF7L2 binding in HCT116.; The allelic enhancer or MYC effect disappears after TCF7L2 knockdown.; The association is fully explained by a linked variant such as rs6983267.

### 3. H2_LEF1_alt: Alt C increases LEF1 binding at the same 8q24 enhancer, raising MYC in HCT116 (p = 0.10)

TF LEF1 (stated coverage not_checked; registry own_model), alt allele binds more; element 8q24.21 enhancer near MYC; gene MYC; cell type HCT116 colorectal adenocarcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt C allele creates or strengthens a LEF1 binding site; LEF1 binds alt C more strongly than ref T. | missing | none |
| element | The variant sits in an 8q24.21 enhancer and alt C increases its activity in colorectal cells. | missing | none |
| gene | Increased LEF1-bound enhancer activity raises MYC transcription. | missing | none |
| cell_type | HCT116 has Wnt/TCF-LEF activity and is a relevant colorectal cancer model. | missing | none |
| phenotype | Increased MYC promotes colorectal cancer. | missing | none |

Predictions: Allele-specific LEF1 binding shows alt C > ref T.; LEF1 knockdown, but not TCF7L2 knockdown, reduces the alt-C enhancer effect.; TCF7L2 supershift/ChIP does not show the allele-specific binding.

Falsified if: LEF1 does not bind the element allele-specifically.; The allelic effect is TCF7L2-dependent rather than LEF1-dependent.; No enhancer or MYC effect is seen.

### 4. H3_CTCF_alt: Alt C alters CTCF binding at 8q24, changing enhancer-insulator topology and MYC (p = 0.10)

TF CTCF (stated coverage not_checked; registry own_model), alt allele binds more; element 8q24.21 CTCF/insulator or enhancer boundary near MYC; gene MYC; cell type HCT116 colorectal adenocarcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt C allele changes a CTCF binding site; CTCF binds alt C more strongly than ref T. | missing | none |
| element | Altered CTCF binding changes insulator/boundary function at 8q24.21. | missing | none |
| gene | Changed boundary function alters MYC enhancer-promoter contacts and MYC expression. | missing | none |
| cell_type | HCT116 has CTCF-bound 8q24 architecture and expresses MYC. | missing | none |
| phenotype | Altered MYC regulation contributes to colorectal cancer. | missing | none |

Predictions: Allele-specific CTCF ChIP shows alt C > ref T.; Hi-C or 3C in HCT116 shows altered MYC contact frequency.; CTCF knockdown or dCas9 boundary perturbation changes MYC.

Falsified if: No allele-specific CTCF binding is detected.; 8q24 topology and MYC expression are unchanged.; TCF7L2/LEF1 binding explains the allelic effect better.

## Prediction matrix

| Test | Cost | Separates top two | H0_null | H1_TCF7L2_alt | H2_LEF1_alt | H3_CTCF_alt |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 binding in HCT116 | low | yes | no allele-specific TCF7L2 binding | alt C > ref T | no TCF7L2 allele effect; LEF1 alt > ref | no TCF7L2 allele effect; CTCF alt > ref |
| Enhancer reporter in HCT116 | medium | no | no allelic reporter difference | alt C reporter higher; TCF7L2 knockdown reduces it | alt C reporter higher; LEF1 knockdown reduces it | allele-specific topology or insulator reporter effect, not simple enhancer activity |
| CRISPR allele swap at rs73706717 in HCT116 | high | no | no change in enhancer activity or MYC | alt-to-ref lowers TCF7L2 binding and MYC mRNA | alt-to-ref lowers LEF1 binding and MYC mRNA | alt-to-ref changes CTCF binding/topology and MYC, without TCF/LEF dependence |

## Next experiment

Allele-specific EMSA/oligo pull-down with HCT116 nuclear extract, using T and C probes, plus a TCF7L2 supershift or TCF7L2 immunodepletion. If alt C shows stronger TCF7L2-dependent binding, H1 is supported. If there is no reproducible allele-specific TCF7L2 binding, the null is favored and linkage/CRISPR testing is needed before claiming a TCF7L2 mechanism.

## Flags

- none

## Evidence
