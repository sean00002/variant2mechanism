# rs642961 and Cleft lip (IRF6)

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.12 over 1 model calls; 49 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. H1: Alt G preserves an AP-2α (TFAP2A) site in the IRF6 enhancer MCS9.7; ref A disrupts it, lowering IRF6 in oral periderm/keratinocytes (p = 0.50)

TF TFAP2A (stated coverage not_checked; registry own_model), alt allele binds more; element MCS9.7 / IRF6 enhancer ~10 kb upstream of IRF6 (chr1q32.2); gene IRF6; cell type oral periderm / embryonic epidermal keratinocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The G (alt) allele matches the AP-2 consensus (GCCNNNGGC-like) and is bound by TFAP2A, while the A (ref, risk) allele weakens or abolishes that binding; TFAP2A is chosen within the AP-2 specificity group because it is the family member mutated in branchio-oculo-facial syndrome with orofacial clefting and is expressed in surface ectoderm. | missing | none |
| element | The variant lies in the conserved MCS9.7 enhancer, which drives reporter expression in oral periderm, medial edge epithelium and other IRF6 domains. | missing | none |
| gene | Reduced TFAP2A occupancy lowers enhancer output and hence IRF6 transcription in cis. | missing | none |
| cell_type | IRF6 dosage is critical in the periderm/keratinocytes of the fusing lip and palate shelves. | missing | none |
| phenotype | Partial IRF6 loss impairs periderm differentiation and epithelial fusion, raising risk of non-syndromic cleft lip with or without cleft palate. | missing | none |

Predictions: Allele-specific TFAP2A ChIP (or ChIP-qPCR) in keratinocytes shows preferential occupancy on the G allele; TFAP2A knockdown reduces MCS9.7 reporter activity for the G construct much more than for the A construct; MCS9.7-A reporter gives lower activity than MCS9.7-G in oral keratinocytes; IRF6 allelic expression imbalance in heterozygous lip/palate epithelium favouring the G chromosome

Falsified if: EMSA/ChIP shows equal or A-favouring occupancy by AP-2 proteins; TFAP2A knockdown leaves allelic reporter difference unchanged; No allelic difference in MCS9.7 enhancer activity in relevant epithelial cells

### 2. H4: No TF-mediated effect of this variant itself: risk is carried by a linked variant in the IRF6 locus (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allelic difference in MCS9.7 reporter activity or TF occupancy; Fine-mapping/conditional analysis points to another variant in the same haplotype block; Base-editing the single position in keratinocytes leaves IRF6 expression unchanged

Falsified if: Reproducible allele-specific enhancer activity or TF binding at this exact position; Isogenic single-base edit changes IRF6 expression

### 3. H2: Same enhancer and direction, but the AP-2 family member acting at the site is TFAP2C (p = 0.12)

TF TFAP2C (stated coverage not_checked; registry own_model), alt allele binds more; element MCS9.7 IRF6 enhancer; gene IRF6; cell type oral periderm / embryonic epidermal keratinocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The AP-2 motif affected is bound in surface ectoderm mainly by TFAP2C, which shares the AP-2 binding specificity; alt G binds more strongly than ref A. TFAP2C is chosen because it is highly expressed in embryonic basal keratinocytes and periderm and can be the dominant family member there. | missing | none |
| element | MCS9.7 contains the AP-2 site and functions as an epithelial enhancer. | missing | none |
| gene | Loss of TFAP2C binding on the A allele reduces IRF6 enhancer activity. | missing | none |
| cell_type | TFAP2C is the predominant AP-2 paralog in periderm at the stage of lip fusion. | missing | none |
| phenotype | Reduced IRF6 in periderm predisposes to cleft lip. | missing | none |

Predictions: TFAP2C, not TFAP2A, knockdown abolishes the allelic reporter difference; TFAP2C ChIP shows stronger signal than TFAP2A at MCS9.7 in keratinocytes; Supershift of the G-allele EMSA complex by anti-TFAP2C but not anti-TFAP2A antibody

Falsified if: TFAP2C is not expressed or not bound at MCS9.7 in relevant cells; Allelic effect persists unchanged after TFAP2C depletion

### 4. H3: The variant alters a p63 (TP63)-dependent regulatory module rather than an AP-2 site (p = 0.08)

TF TP63 (stated coverage not_checked; registry own_model), alt allele binds more; element MCS9.7 IRF6 enhancer, adjacent p63 response element; gene IRF6; cell type basal keratinocytes of the oral epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt G allele supports stronger occupancy of a p63 (TP63, ΔNp63 isoform) half-site or cooperative complex at MCS9.7; the A allele weakens it. | missing | none |
| element | MCS9.7 carries a functional p63 response element and p63 is a known direct activator of IRF6 through this enhancer. | missing | none |
| gene | Weaker p63-dependent activation on the A allele lowers IRF6 expression. | missing | none |
| cell_type | ΔNp63 is the master regulator of embryonic oral basal keratinocytes. | missing | none |
| phenotype | The p63–IRF6 regulatory loop is disrupted in orofacial clefting syndromes, so reduced IRF6 raises cleft lip risk. | missing | none |

Predictions: Allele-specific p63 ChIP shows G-allele preference at the variant; TP63 knockdown removes the allelic reporter difference while AP-2 knockdown does not; Mutating the AP-2 core alone does not abolish allelic difference

Falsified if: p63 binding at MCS9.7 is allele-independent; The variant lies outside any p63 motif footprint

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Luciferase reporter of MCS9.7 with A vs G allele in oral/epidermal keratinocytes | low | yes | G construct clearly more active than A | No reproducible allelic difference | G construct clearly more active than A | G construct more active, effect lost in TP63-null cells |
| EMSA with keratinocyte nuclear extract plus anti-TFAP2A and anti-TFAP2C supershift | low | no | G-allele complex supershifted by anti-TFAP2A | Equal complexes on both alleles | G-allele complex supershifted by anti-TFAP2C | No AP-2 supershift; distinct larger complex |
| Allele-specific ChIP-qPCR for TFAP2A, TFAP2C and TP63 in heterozygous keratinocytes | medium | no | TFAP2A imbalance toward G | No imbalance for any factor | TFAP2C imbalance toward G | TP63 imbalance toward G |
| Isogenic base editing A<->G at the endogenous locus, then IRF6 qPCR | high | yes | A allele lowers IRF6 | IRF6 unchanged | A allele lowers IRF6 | A allele lowers IRF6 |

## Next experiment

Transient luciferase assay of the MCS9.7 enhancer carrying A versus G in oral keratinocytes: a reproducible allelic difference in enhancer output supports H1 (and H2/H3), while no difference supports the null H4, at minimal cost.

## Flags

- none

## Evidence
