# rs6983267 and Colorectal cancer (8q24)

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.16 over 1 model calls; 68 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H1: G allele increases TCF7L2 binding at the MYC-335 (8q24.21) WNT-responsive enhancer, raising MYC expression in colonic epithelium (p = 0.45)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element MYC-335 enhancer (rs6983267-containing WNT-responsive element, chr8:127.40 Mb); gene MYC; cell type Colonic crypt epithelial / colorectal tumour cells (HCT 116 as model).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The risk (ref) G allele creates a better match to the TCF/LEF consensus and is bound more strongly by TCF7L2 than the T allele; TCF7L2 is chosen within the TCF/LEF specificity group because it is the dominant, highly expressed TCF/LEF member in colonic epithelium and colorectal lines such as HCT 116, and it is the member reported at this site by ChIP. No QBiC-SELEX evidence was supplied, so coverage is unverified. | missing | none |
| element | The variant sits in an enhancer (MYC-335) that is WNT-responsive and loops to the MYC promoter ~335 kb away. | missing | none |
| gene | Stronger TCF7L2 occupancy on the G allele increases enhancer activity and MYC transcription, giving modest allele-specific MYC expression in heterozygotes. | missing | none |
| cell_type | The effect is restricted to cells with active WNT/beta-catenin signalling and an open chromatin state at MYC-335, i.e. intestinal crypt/colorectal cancer cells. | missing | none |
| phenotype | Modestly elevated MYC in crypt progenitors increases proliferation and adenoma initiation, raising colorectal cancer risk for G carriers. | missing | none |

Predictions: Allele-specific TCF7L2 ChIP in heterozygous colorectal cells favours G; Deletion or CRISPRi of the MYC-335 element lowers MYC and reduces proliferation; Allele-specific MYC expression in heterozygous normal colonic mucosa, G>T; Enhancer reporter with G shows higher activity than T, and the difference is abolished by dominant-negative TCF or beta-catenin inhibition

Falsified if: No allelic difference in TCF7L2 occupancy or reporter activity; MYC-335 deletion leaves MYC expression unchanged in colonic cells; 4C/Hi-C shows no contact between the element and the MYC promoter

### 2. H4: Null: no TF-mediated effect of rs6983267 itself (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific binding, reporter activity or expression difference attributable to this base; Fine-mapping or allele-swap editing at rs6983267 leaves MYC/CCAT2 unchanged while a linked variant in the same haplotype block carries the signal

Falsified if: Isogenic single-base edit of G to T in colonic cells changes MYC or CCAT2 expression; Reproducible allele-specific TF binding at this base in heterozygotes

### 3. H2: Same TCF7L2 allelic binding difference acts mainly through the lncRNA CCAT2 transcribed from the locus (p = 0.17)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element rs6983267-containing element that also serves as the CCAT2 lncRNA body/promoter region; gene CCAT2; cell type Colorectal epithelial / colorectal cancer cells (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | G allele is bound more strongly by TCF7L2 (chosen within the TCF/LEF group on expression and ChIP grounds in colon). | missing | none |
| element | The variant lies within the transcribed CCAT2 lncRNA locus, so the allele is carried in the RNA itself as well as in the DNA element. | missing | none |
| gene | The G allele increases CCAT2 output and the G-form of the CCAT2 RNA feeds back on TCF7L2/WNT activity, indirectly raising MYC rather than MYC being the direct enhancer target. | missing | none |
| cell_type | Effect requires WNT-active colonic epithelium where CCAT2 is expressed. | missing | none |
| phenotype | Higher CCAT2 promotes WNT signalling, chromosomal instability and tumour growth, increasing colorectal cancer risk. | missing | none |

Predictions: CCAT2 shows strong allele-specific expression favouring G; ASO or shRNA knockdown of CCAT2 lowers MYC and WNT target genes; Ectopic G-form CCAT2 RNA raises MYC independently of the DNA element

Falsified if: CCAT2 knockdown leaves MYC and proliferation unchanged; CCAT2 is not detectably expressed in the relevant colonic cells; Enhancer effect on MYC persists when CCAT2 transcription is blocked

### 4. H3: LEF1, not TCF7L2, is the TCF/LEF member mediating the allelic effect on MYC (p = 0.13)

TF LEF1 (stated coverage not_checked; registry own_model), ref allele binds more; element MYC-335 enhancer; gene MYC; cell type Colorectal tumour cells with high LEF1 (WNT-high).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The G allele matches the shared TCF/LEF specificity; within that group LEF1 is selected because it is strongly induced in WNT-high colorectal tumours and is the most transcriptionally activating member, whereas TCF7L2 can act as a repressor in some contexts. | missing | none |
| element | LEF1 occupies the same MYC-335 WNT-responsive element with beta-catenin. | missing | none |
| gene | G-allele-biased LEF1 occupancy raises MYC transcription. | missing | none |
| cell_type | Dependence on LEF1 restricts the effect to LEF1-high tumour or progenitor cells; TCF7L2-only cells would show little allelic effect. | missing | none |
| phenotype | Increased MYC drives proliferation and colorectal tumorigenesis in G carriers. | missing | none |

Predictions: LEF1 knockdown abolishes the allelic reporter/expression difference while TCF7L2 knockdown does not; Allele-specific ChIP for LEF1 shows G bias at least as strong as for TCF7L2; Allelic effect size correlates with LEF1 expression across colorectal lines

Falsified if: LEF1 is not expressed or not bound at the element in colonic cells; TCF7L2 depletion alone removes the allelic effect

### 5. H5: Allelic enhancer acts on POU5F1B / another 8q24 gene rather than MYC (p = 0.00)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element rs6983267 enhancer within the 8q24 gene desert; gene POU5F1B; cell type Colorectal epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | G allele binds TCF7L2 (TCF/LEF group member chosen by colonic expression) more strongly. | missing | none |
| element | The element loops preferentially to the nearby POU5F1B promoter rather than to MYC in some colorectal cells. | missing | none |
| gene | G allele raises POU5F1B expression. | missing | none |
| cell_type | Restricted to colorectal epithelium where POU5F1B is detectably transcribed. | missing | none |
| phenotype | POU5F1B supports proliferation/stemness, contributing to colorectal cancer risk. | missing | none |

Predictions: 4C from the element shows dominant contact with POU5F1B; POU5F1B shows allele-specific expression; MYC does not; POU5F1B knockdown reduces growth while MYC is unaffected by element deletion

Falsified if: POU5F1B is not expressed in colonic cells; Element deletion changes MYC but not POU5F1B

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 | H5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 ChIP-qPCR in a rs6983267-heterozygous colorectal line | low | no | Clear G bias in bound DNA | No allelic bias | Clear G bias (same binding step) | Weak or no TCF7L2 bias; LEF1 ChIP shows the bias | G bias |
| ASO/siRNA knockdown of CCAT2 in HCT 116, then RT-qPCR of MYC and WNT targets | low | yes | MYC largely unchanged | Uninformative about the variant | MYC and WNT targets fall | MYC largely unchanged | MYC unchanged; POU5F1B unchanged |
| CRISPR single-base allele swap (G to T) in an isogenic colorectal line; RNA-seq for MYC, CCAT2, POU5F1B | high | yes | MYC drops with T | No expression change | CCAT2 drops first, MYC follows | MYC drops, LEF1-dependent | POU5F1B drops, MYC flat |
| Individual knockdown of TCF7L2 versus LEF1 followed by allelic reporter assay | medium | no | TCF7L2 knockdown removes allelic difference | No allelic difference to remove | TCF7L2 knockdown removes it | LEF1 knockdown removes it | TCF7L2 knockdown removes it |
| 4C-seq or Capture-C from the rs6983267 element in colorectal cells | medium | yes | Contact with MYC promoter | Uninformative | Local CCAT2 signal dominant | Contact with MYC promoter | Contact with POU5F1B |
| QBiC-SELEX detail lookup for TCF7L2 and LEF1 coverage and predicted allelic score | existing data | no | TCF7L2 own model predicting higher G binding supports H1 | No significant predicted effect supports null | Same prediction, does not distinguish | LEF1 model with comparable score keeps H3 open | Same binding prediction |

## Next experiment

ASO knockdown of CCAT2 in HCT 116 followed by RT-qPCR of MYC and canonical WNT targets: if MYC falls, the locus acts through the CCAT2 lncRNA (H2); if MYC is unchanged, the enhancer acts directly on MYC (H1). This is the cheapest assay that distinguishes the two leading chains, which share the same TCF7L2 G-biased binding step.

## Flags

- none

## Evidence
