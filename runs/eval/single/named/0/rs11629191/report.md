# rs11629191 and Breast cancer

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.16 over 1 model calls; 73 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H5: Null: no TF-mediated effect of this variant (p = 0.43)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific binding for any TF in heterozygous cells; No allelic difference in reporter assays or in MPRA; Base editing/prime editing of the single base in MCF7 changes no neighbouring gene's expression; Fine-mapping credible set contains a better-supported linked variant, or the association is driven by LD with a coding/other regulatory variant

Falsified if: Reproducible allele-specific binding plus a concordant allelic reporter or editing effect is demonstrated

### 2. H1: Alt T creates a stronger FOXA1 (forkhead) site in a luminal enhancer, raising expression of a nearby 14q22.1 gene (p = 0.22)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element Putative distal enhancer at chr14:55,887,040 active in ER+ luminal breast epithelium (MCF7); gene SAMD4A (alternatives: GCH1, FBXO34, WDHD1); cell type ER-positive luminal breast epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C>T change is predicted to improve match to the forkhead core motif (TGTTT/GTAAACA family), so the alt allele is bound more strongly by FOXA1; FOXA1 is chosen within the forkhead specificity group because it is the dominant, highly expressed forkhead factor in MCF7 and in luminal breast tissue (FOXA2/FOXA3 are essentially absent). | missing | none |
| element | The variant lies in a non-coding region expected to carry luminal enhancer marks (H3K27ac, ATAC accessibility) co-bound by FOXA1 in MCF7. | missing | none |
| gene | Stronger FOXA1 pioneering increases accessibility and looping of this enhancer to a 14q22.1 promoter, most plausibly SAMD4A, raising its transcription. | missing | none |
| cell_type | The effect is restricted to FOXA1-expressing luminal breast cells, where the enhancer is open. | missing | none |
| phenotype | Altered dosage of the FOXA1-driven target gene modestly shifts proliferation/differentiation of luminal progenitors, contributing to ER+ breast cancer risk. | missing | none |

Predictions: Allele-specific FOXA1 ChIP-seq signal in heterozygous breast cells favours the T allele; EMSA supershift with FOXA1 antibody shows stronger complex on the T probe; FOXA1 knockdown abolishes the allelic reporter difference; Reporter activity higher for T than C in MCF7, no difference in FOXA1-negative cells (e.g. MDA-MB-231)

Falsified if: No allelic imbalance in FOXA1 ChIP or no FOXA1 occupancy at the locus; Reporter shows no allelic difference, or the C allele is more active; QBiC-SELEX forkhead models show the ref allele is the stronger binder

### 3. H2: Ref C preserves a GATA3 site; alt T disrupts it, lowering enhancer output (p = 0.16)

TF GATA3 (stated coverage not_checked; registry own_model), ref allele binds more; element Same putative luminal enhancer at chr14:55,887,040; gene SAMD4A (alternatives: GCH1, FBXO34); cell type ER-positive luminal breast epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C allele can complete a WGATAA-like core that the T allele breaks, so GATA3 binds the ref allele more; within the GATA specificity group GATA3 is chosen because it is the only GATA factor highly expressed in MCF7 and luminal breast tissue. | missing | none |
| element | GATA3 co-occupies FOXA1/ER enhancers in luminal cells, and this site is expected to fall in such a cluster. | missing | none |
| gene | Loss of GATA3 binding on the risk allele reduces enhancer activity and lowers expression of the looped 14q22.1 target. | missing | none |
| cell_type | Restricted to GATA3-high luminal cells; no effect in basal/mesenchymal lines. | missing | none |
| phenotype | Reduced target-gene expression weakens luminal differentiation control, increasing ER+ breast cancer risk. | missing | none |

Predictions: Allele-specific GATA3 ChIP favours the C allele; GATA3 knockdown removes the allelic reporter difference while FOXA1 knockdown does not; Reporter activity lower for T than C

Falsified if: No GATA3 occupancy or no allelic imbalance at the site; T allele shows equal or higher reporter activity; Motif analysis shows no GATA core is created or destroyed

### 4. H3: Alt T weakens an ESR1 half-site/ERE, blunting oestrogen-responsive enhancer activity (p = 0.10)

TF ESR1 (stated coverage not_checked; registry own_model), ref allele binds more; element Oestrogen-responsive enhancer at chr14:55,887,040; gene GCH1 (alternative: SAMD4A); cell type ER-positive breast cancer cells (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The variant sits in or beside an ERE half-site (GGTCA-like) that the C allele matches better, so ESR1 binds the ref allele more; ESR1 rather than ESR2 because ESR2 is not meaningfully expressed in MCF7. | missing | none |
| element | The element is expected to be an E2-inducible ER binding site in MCF7. | missing | none |
| gene | Weaker ER recruitment on the alt allele reduces E2-induced transcription of the nearby target gene. | missing | none |
| cell_type | Effect confined to ER+ cells and dependent on oestrogen stimulation. | missing | none |
| phenotype | Altered oestrogen-responsive gene dosage shifts hormone-driven proliferation and ER+ breast cancer risk. | missing | none |

Predictions: Allelic reporter difference appears only after E2 treatment and is lost with fulvestrant; ER ChIP shows E2-dependent occupancy with C-allele bias; No allelic effect in ER-negative cells even if FOXA1 is present

Falsified if: No ER binding at the locus in E2-treated MCF7; Allelic reporter difference is identical with and without oestrogen

### 5. H4: Alt T disrupts a CTCF site, altering TAD/loop insulation at 14q22.1 (p = 0.09)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element CTCF-bound insulator/loop anchor at chr14:55,887,040; gene SAMD4A / GCH1 (enhancer-promoter rewiring within the sub-TAD); cell type Broadly expressed; phenotype read out in breast epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C>T change falls in the core CTCF 19-mer and weakens binding, so the ref allele binds CTCF more; CTCF is a single-member specificity (CTCFL is testis-restricted and not expressed in MCF7). | missing | none |
| element | The element acts as a constitutive loop anchor rather than a cell-type-specific enhancer. | missing | none |
| gene | Weaker insulation on the alt allele lets an adjacent enhancer contact a different promoter, changing expression of a 14q22.1 gene. | missing | none |
| cell_type | CTCF binding is ubiquitous, but the expression consequence is seen where the neighbouring enhancers are active, i.e. breast epithelium. | missing | none |
| phenotype | Rewired enhancer-promoter contacts alter target dosage and contribute to breast cancer risk. | missing | none |

Predictions: Allele-specific CTCF ChIP/CUT&RUN favours C across many cell types, not just breast; 4C/Hi-C shows allele-dependent contact changes; Episomal reporter shows little or no allelic difference (insulators act in chromatin context)

Falsified if: No CTCF peak at the variant in any ENCODE cell type; Allelic effect is breast-restricted and reporter-detectable

## Prediction matrix

| Test | Cost | Separates top two | H5 | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QBiC-SELEX lookup of FOXA1, GATA3, ESR1 and CTCF at this variant (direction and magnitude of predicted binding change) | existing data | yes | No model shows a meaningful allelic difference | Forkhead model predicts stronger binding to T | GATA model predicts stronger binding to C | Nuclear-receptor model predicts stronger binding to C | CTCF model predicts stronger binding to C |
| Allele-specific analysis of existing MCF7/breast FOXA1, GATA3, ER and CTCF ChIP-seq at heterozygous sites, plus overlap with ENCODE H3K27ac/ATAC | existing data | yes | No peak or balanced reads | FOXA1 peak present with reads biased to T | GATA3 peak with reads biased to C | ER peak, E2-dependent, biased to C | CTCF peak biased to C, present across cell types |
| Allelic luciferase reporter (C vs T, ~500 bp) in MCF7 ± oestrogen and in MDA-MB-231 | low | yes | No allelic difference in any condition | T > C in MCF7 only, E2-independent | C > T in MCF7 only | C > T only after E2 | No or minimal allelic difference episomally |
| EMSA/competition with MCF7 nuclear extract plus FOXA1 and GATA3 supershift | medium | yes | Equal binding, no specific complex | Stronger T complex, supershifted by anti-FOXA1 | Stronger C complex, supershifted by anti-GATA3 | Stronger C complex, supershifted by anti-ER | Stronger C complex, supershifted by anti-CTCF |
| Prime-edit C/T homozygous MCF7 clones and measure 1 Mb neighbourhood expression by RNA-seq | high | yes | No expression change | Target gene up in T clones | Target gene down in T clones | Target gene down in T clones only with E2 | Shift in which neighbouring promoter responds; contact changes on Hi-C |

## Next experiment

Mine existing MCF7/breast ChIP-seq (FOXA1, GATA3, ER, CTCF) for allele-specific read imbalance at chr14:55,887,040 in heterozygous samples, together with a QBiC-SELEX lookup of these TFs. This costs nothing new and immediately separates the null (no peak or balanced reads) from the FOXA1 chain (T-biased FOXA1 occupancy).

## Flags

- none

## Evidence
