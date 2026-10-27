# rs6983267 and Colorectal cancer (8q24)

Configuration `single`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 1 model calls; 57 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H1: G-allele TCF7L2 binding increases MYC enhancer output (p = 0.70)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element The rs6983267-containing 8q24 regulatory element acts as an enhancer for MYC.; gene MYC; cell type Colorectal cancer cells, including HCT 116 cells with active Wnt signaling..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 (also called TCF4) is the leading TF because prior work at this locus reports allele-sensitive TCF7L2 binding; the reference G allele is favored over T. No case-specific QBiC-SELEX result is supplied here. | missing | none |
| element | The variant lies in an 8q24 regulatory element whose enhancer activity is greater with the G allele. | missing | none |
| gene | The element increases MYC expression, the best-established candidate target of the rs6983267 enhancer. | missing | none |
| cell_type | In colorectal cells such as HCT 116, Wnt/β-catenin signaling can support TCF7L2-dependent enhancer activity. | missing | none |
| phenotype | Higher MYC expression could promote colorectal tumor development, making the G allele the risk-increasing allele under this model. | missing | none |

Predictions: At the same genomic background, changing G to T will reduce enhancer output and MYC transcription.; The variant-containing element will show preferential TCF7L2 occupancy on the G-bearing allele.

Falsified if: Isogenic G-to-T editing leaves MYC transcription and enhancer output unchanged in an adequately powered colorectal-cell assay.; Allele-resolved occupancy or binding assays show no G preference for TCF7L2.

### 2. H2: G-allele TCF7L2 binding increases CCAT2 expression (p = 0.17)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element The rs6983267-containing regulatory region within the CCAT2 locus acts in cis on CCAT2 transcription.; gene CCAT2; cell type Colorectal cancer cells, including HCT 116 cells..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is the leading TF based on prior locus-specific allele-sensitive binding reports; the reference G allele is favored over T. No case-specific QBiC-SELEX result is supplied here. | missing | none |
| element | The variant-containing region acts as a cis-regulatory element for the overlapping CCAT2 long noncoding RNA locus. | missing | none |
| gene | Greater activity of the G-bearing element increases CCAT2 expression. | missing | none |
| cell_type | In colorectal cancer cells, increased CCAT2 could influence oncogenic Wnt-related programs. | missing | none |
| phenotype | If the CCAT2 change is consequential, the G allele could increase colorectal cancer risk through CCAT2 rather than primarily through MYC enhancer output. | missing | none |

Predictions: Isogenic G-to-T editing will reduce CCAT2 transcription; this effect should be more direct or larger than any primary change in MYC.; Perturbing the element will alter CCAT2 expression in cis.

Falsified if: Isogenic G-to-T editing has no reproducible effect on CCAT2 transcription.; Element perturbation changes MYC but not CCAT2 expression.

### 3. H0: No TF-mediated effect of rs6983267 (p = 0.13)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing G to T will not produce a reproducible TF-dependent change in MYC or CCAT2 expression.; Any disease association may reflect a linked causal variant or another mechanism rather than an effect of this base.

Falsified if: A reproducible allele-dependent effect is demonstrated by isogenic editing and is attributable to TF binding at this element.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H0 |
| --- | --- | --- | --- | --- | --- |
| Isogenic G-to-T editing in HCT 116 followed by nascent-RNA or RT-qPCR measurement of both MYC and CCAT2 | medium | yes | MYC decreases; CCAT2 need not show a primary change. | CCAT2 decreases; MYC need not show a primary change. | Neither transcript shows a reproducible editing-dependent change. |
| Allele-resolved TCF7L2 CUT&RUN or ChIP at rs6983267 in a heterozygous colorectal cell line | medium | no | Greater TCF7L2 occupancy on the G-bearing allele. | Greater TCF7L2 occupancy on the G-bearing allele. | No reproducible allele-specific TCF7L2 occupancy attributable to this variant. |
| Perturb the variant-containing region and measure enhancer-promoter contacts to MYC and CCAT2 | high | yes | The region preferentially engages the MYC regulatory domain. | The region acts in cis at the CCAT2 locus, without a dominant MYC contact. | No functional contact change attributable to the element. |

## Next experiment

The cheapest direct discriminator of the two leading chains is isogenic G-to-T editing in HCT 116 followed by measurement of both MYC and CCAT2 RNA. A selective MYC decrease favors H1; a selective CCAT2 decrease favors H2. Include unedited and mock-edited controls.

## Flags

- none

## Evidence
