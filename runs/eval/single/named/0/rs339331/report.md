# rs339331 and Prostate cancer (6q22)

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.11 over 1 model calls; 48 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. H1: T allele increases HOXB13 binding at an intronic RFX6 enhancer, raising RFX6 expression in AR-positive prostate epithelium (p = 0.45)

TF HOXB13 (stated coverage not_checked; registry own_model), ref allele binds more; element Intronic enhancer of RFX6 at 6q22.1 containing the rs339331 TTTA/HOXB13-like core; gene RFX6; cell type Androgen-receptor-positive luminal prostate epithelial cells (LNCaP as model).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref T allele restores a HOXB13 consensus core (TTA-containing homeodomain site) that is disrupted by the alt C, so HOXB13 binds the T allele more strongly; HOXB13 is the homeodomain TF chosen because it is the prostate-lineage-restricted member of the family highly expressed in LNCaP, whereas most other homeodomain TFs sharing this specificity group are not expressed there. | missing | none |
| element | The variant lies in an intronic element of RFX6 that behaves as an androgen-responsive enhancer bound by HOXB13 and FOXA1 in prostate cells; the T allele gives higher enhancer activity in reporter assays. | missing | none |
| gene | The enhancer loops to and up-regulates RFX6, the nearest gene, making rs339331 an eQTL for RFX6 in prostate tissue with T as the higher-expression allele. | missing | none |
| cell_type | The effect is restricted to AR/HOXB13/FOXA1-positive luminal prostate epithelium, the cell of origin of prostate adenocarcinoma. | missing | none |
| phenotype | Elevated RFX6 promotes proliferation and invasive behaviour of prostate epithelial cells, increasing prostate cancer risk and aggressiveness for T carriers. | missing | none |

Predictions: HOXB13 ChIP-seq in heterozygous prostate cells shows allelic imbalance favouring the T allele; HOXB13 knockdown abolishes the allelic difference in reporter activity and lowers RFX6; rs339331 is an RFX6 eQTL in prostate tissue with T as the high-expression allele

Falsified if: No HOXB13 occupancy at the locus by ChIP-seq, or no allelic imbalance in heterozygotes; HOXB13 knockdown leaves allele-specific enhancer activity unchanged

### 2. H4: Null: rs339331 has no TF-mediated allelic effect; the association is carried by a linked variant on the 6q22 haplotype (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allelic imbalance in any TF ChIP-seq or in ATAC at rs339331 in heterozygous prostate cells; Allele-swap (CRISPR knock-in) at rs339331 does not change RFX6 expression; Fine-mapping credible set keeps other variants with comparable posterior probability, and one of them shows the functional signal

Falsified if: CRISPR allele swap of rs339331 alone changes RFX6 expression or local chromatin accessibility; Reproducible allele-specific TF occupancy at the site in heterozygotes

### 3. H2: Allelic FOXA1 pioneer binding at the same element drives the RFX6 enhancer difference (p = 0.15)

TF FOXA1 (stated coverage not_checked; registry own_model), ref allele binds more; element Same 6q22.1 intronic RFX6 enhancer, within a composite forkhead/homeodomain module; gene RFX6; cell type AR-positive luminal prostate epithelial cells (LNCaP).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The T allele improves a forkhead-like core (TGTTT/AAACA family motif) so FOXA1 binds more; FOXA1 is chosen among forkhead factors because it is the dominant, highly expressed forkhead pioneer factor in LNCaP and prostate luminal cells. | missing | none |
| element | FOXA1 pioneering opens the chromatin of the element, and loss of the site on the C allele reduces accessibility and enhancer output. | missing | none |
| gene | Reduced accessibility lowers RFX6 transcription from the linked promoter. | missing | none |
| cell_type | FOXA1 dependence confines the effect to luminal prostate epithelium. | missing | none |
| phenotype | Allele-dependent RFX6 levels modulate prostate cancer susceptibility. | missing | none |

Predictions: ATAC/DNase allelic imbalance at the element favouring T even after HOXB13 depletion; FOXA1 ChIP-seq allelic imbalance favouring T; FOXA1 knockdown, not HOXB13 knockdown, collapses the allelic difference

Falsified if: FOXA1 ChIP shows no allelic imbalance at rs339331; Allelic enhancer activity persists after FOXA1 depletion

### 4. H3: The alt C allele creates a repressive site for an RFX-family factor that dampens the element (p = 0.10)

TF RFX6 (stated coverage not_checked; registry mapped), alt allele binds more; element Same intronic element, with a C-dependent X-box-like half site; gene RFX6; cell type Prostate luminal epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C allele generates a partial X-box (GTTRCC-like) recognised by RFX-family proteins; RFX6 is chosen within this specificity group because it is the family member expressed at the locus and in prostate tissue, giving a plausible local autoregulatory loop. | missing | none |
| element | RFX binding on the C allele represses the enhancer or competes with homeodomain/forkhead occupancy. | missing | none |
| gene | Negative autoregulation lowers RFX6 expression specifically from the C haplotype. | missing | none |
| cell_type | Restricted to cells expressing RFX6, chiefly prostate epithelium and pancreatic/intestinal endocrine cells. | missing | none |
| phenotype | Lower RFX6 on C haplotypes is protective; T carriers retain higher RFX6 and higher risk. | missing | none |

Predictions: RFX6 ChIP or motif-directed EMSA shows C-preferential binding; RFX6 knockdown raises reporter activity selectively for the C allele

Falsified if: No RFX-family occupancy at the element; C allele shows no gain of any protein complex in EMSA

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| HOXB13 ChIP-seq (or ChIP-qPCR with allele-specific readout) in rs339331-heterozygous prostate cells | existing data | yes | Clear allelic imbalance favouring T | No occupancy or balanced reads | Little or no HOXB13 imbalance; signal may be weak and FOXA1-dependent | No HOXB13 imbalance |
| Luciferase reporter with T vs C element in LNCaP, with and without HOXB13 or FOXA1 knockdown | low | yes | T > C activity, difference lost on HOXB13 knockdown | No allelic difference | T > C activity, difference lost on FOXA1 knockdown | C < T because C gains repression; difference lost on RFX6 knockdown |
| CRISPR allele swap of rs339331 in LNCaP and RFX6 qPCR | high | no | T knock-in raises RFX6 | No change in RFX6 | T knock-in raises RFX6 and accessibility | C knock-in lowers RFX6 |
| Prostate-tissue eQTL lookup for RFX6 at rs339331 | existing data | no | T associated with higher RFX6 | eQTL absent or fully explained by linked variants | T associated with higher RFX6 | T associated with higher RFX6 |

## Next experiment

Reanalyse existing LNCaP HOXB13 ChIP-seq (and matched FOXA1 ChIP-seq) reads overlapping rs339331 in heterozygous cells for allele-specific occupancy: it is essentially free, and T-biased HOXB13 reads support H1 while balanced reads with T-biased FOXA1 support H2 (and no occupancy at all supports the null).

## Flags

- none

## Evidence
