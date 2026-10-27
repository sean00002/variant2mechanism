# rs2168101 and Neuroblastoma (LMO1)

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.13 over 1 model calls; 56 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. H1: Ref (C; = G on the LMO1 sense strand) creates a GATA3 site in the LMO1 intron-1 enhancer, driving LMO1 expression in adrenergic neuroblastoma cells (p = 0.50)

TF GATA3 (stated coverage not_checked; registry own_model), ref allele binds more; element LMO1 intron 1 / super-enhancer element at chr11:8233861; gene LMO1; cell type Adrenergic (noradrenergic) neuroblastoma cells, e.g. SK-N-SH / sympathoadrenal neuroblast precursors.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref C allele (G on the opposite strand, the orientation used in the original report) completes a canonical GATA (WGATAA) motif that GATA3 binds; the alt A allele disrupts the core and abolishes binding, so binding is higher on ref. | missing | none |
| element | The variant sits in an intron-1 enhancer of LMO1 that is part of a neuroblastoma super-enhancer marked by H3K27ac and occupied by the adrenergic core regulatory circuit; allele-specific enhancer activity follows the GATA motif. | missing | none |
| gene | The enhancer loops to and activates the LMO1 promoter, so the ref allele yields higher LMO1 mRNA in cis (allelic imbalance in heterozygotes). | missing | none |
| cell_type | GATA3 is highly expressed and essential in adrenergic neuroblastoma cells such as SK-N-SH, making the effect cell-type restricted to the sympathoadrenal lineage. | missing | none |
| phenotype | LMO1 is a neuroblastoma oncogene; higher LMO1 from the ref allele increases neuroblastoma risk, and the alt allele is protective. | missing | none |

Predictions: GATA3 ChIP-seq/ChIP-qPCR in heterozygous neuroblastoma lines shows strong ref-allele-biased occupancy at chr11:8233861; GATA3 knockdown reduces LMO1 expression and enhancer H3K27ac specifically in lines carrying the ref allele; Reporter assay: ref construct >> alt construct in adrenergic but not mesenchymal or non-neural cells; Allele-specific LMO1 expression in heterozygous tumors favors the ref haplotype

Falsified if: No allelic bias in GATA3 ChIP at the site; GATA3 depletion leaves LMO1 unchanged while another GATA-family or non-GATA factor accounts for the effect; Ref and alt reporters behave identically

### 2. H4: Null: no TF-binding effect of rs2168101 itself (p = 0.28)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific ChIP signal for any TF at the site; Reporter constructs for ref and alt are indistinguishable; Any LMO1 association tracks a different variant on the same haplotype after fine-mapping or CRISPR tiling

Falsified if: Clear allele-specific TF occupancy or reporter difference at this exact base; Base editing of only this position changes LMO1 expression

### 3. H2: Same GATA motif, but GATA2 is the occupying family member (p = 0.14)

TF GATA2 (stated coverage not_checked; registry own_model), ref allele binds more; element LMO1 intron 1 enhancer at chr11:8233861; gene LMO1; cell type Neuroblastoma cells of the sympathoadrenal lineage.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 shares the WGATAA specificity; a SELEX-based prediction names the GATA group, not a single TF. Within the group GATA2 is the alternative candidate because it is also expressed in sympathetic neuroblasts; ref binds more, alt disrupts. | missing | none |
| element | The same intron-1 enhancer is bound by GATA2 in some neuroblastoma backgrounds, with ref-allele-preferential occupancy. | missing | none |
| gene | GATA2 occupancy activates LMO1 transcription in cis. | missing | none |
| cell_type | GATA2 participates in the sympathoadrenal transcriptional program; effect limited to that lineage. | missing | none |
| phenotype | Elevated LMO1 promotes neuroblastoma, so the ref allele confers risk. | missing | none |

Predictions: GATA2, not GATA3, ChIP signal is allele-biased at the site; GATA2 knockdown lowers LMO1 while GATA3 knockdown does not; GATA2 expression in SK-N-SH comparable to or higher than GATA3

Falsified if: GATA2 is not expressed or not bound at the locus in neuroblastoma lines; GATA2 depletion does not change LMO1 while GATA3 depletion does

### 4. H3: The GATA site acts as the anchor of a GATA/TAL1-type composite complex; TAL1 recruitment is the functional readout (p = 0.08)

TF TAL1 (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element LMO1 intron 1 enhancer at chr11:8233861; gene LMO1; cell type Neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TAL1 does not read the GATA core directly but is tethered through a GATA partner at a composite E-box-GATA element; the ref allele supports complex assembly and the alt allele does not, so ref binds more. | missing | none |
| element | The enhancer behaves as a composite element whose activity depends on the intact GATA half-site. | missing | none |
| gene | Loss of complex assembly on the alt allele reduces LMO1 transcription. | missing | none |
| cell_type | TAL1-containing complexes with LMO proteins are active in neuroblastoma and related lineages. | missing | none |
| phenotype | Reduced LMO1 on the alt allele lowers neuroblastoma risk. | missing | none |

Predictions: TAL1 ChIP shows allele-biased occupancy that is lost upon GATA-factor depletion; An intact adjacent E-box is required for reporter activity; Co-IP shows GATA factor and TAL1 at the locus

Falsified if: No TAL1 occupancy at the element; Reporter activity is unaffected by E-box mutation while GATA mutation abolishes it

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Mine existing neuroblastoma GATA3 and GATA2 ChIP-seq plus RNA-seq (e.g. SK-N-SH, Kelly, NGP) for reads overlapping chr11:8233861 and for relative TF expression | existing data | yes | GATA3 peak at the site with ref-biased reads; GATA3 >> GATA2 expression | No TF peak, or a peak with no allelic bias in heterozygous lines | GATA2 peak with ref-biased reads; GATA2 expressed at least as highly as GATA3 | GATA peak accompanied by a coincident TAL1 peak |
| Luciferase reporter with ref vs alt 300 bp element in SK-N-SH and a non-neural control line | low | no | Ref >> alt in SK-N-SH only | No difference between alleles | Ref >> alt in SK-N-SH only (indistinguishable from H1) | Ref >> alt and loss of activity when the neighbouring E-box is mutated |
| siRNA/shRNA knockdown of GATA3 vs GATA2 in SK-N-SH, then LMO1 qPCR | low | yes | LMO1 drops with GATA3 knockdown only | LMO1 may drop, but with no allele dependence in heterozygous lines | LMO1 drops with GATA2 knockdown only | LMO1 drops with either GATA knockdown and with TAL1 knockdown |
| CRISPR base editing / HDR conversion of C to A at the endogenous site in a heterozygous line, with allele-specific LMO1 qPCR | high | no | LMO1 falls from the edited allele | No change in LMO1 | LMO1 falls from the edited allele | LMO1 falls from the edited allele |
| QBiC-SELEX lookup of GATA3 and GATA2 models for this 12-mer context | existing data | no | GATA3 own or mapped model predicts strong ref-preferential binding | No significant predicted binding change | GATA2 model predicts the same shared GATA specificity; cannot discriminate within family | No TAL1 effect predicted (indirect tethering) |

## Next experiment

Interrogate already-public neuroblastoma GATA3 and GATA2 ChIP-seq plus matched RNA-seq/WGS at chr11:8233861 in heterozygous lines: allele-counted reads tell you whether GATA3 or GATA2 occupies the site and whether occupancy is ref-biased at all, separating H1 from H2 (and from the null) at essentially zero bench cost.

## Flags

- none

## Evidence
