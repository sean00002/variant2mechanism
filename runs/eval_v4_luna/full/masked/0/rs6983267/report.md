# rs6983267 and Colorectal cancer (8q24)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.03 over 13 model calls; 288 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -4.66); SRF (bound here, z -7.74, weak site); SP1 (bound here, z -4.76, weak site); JUND (bound here, z -3.01, no clear allelic change, weak site); CEBPB (bound here, z 1.9, no clear allelic change, weak site); MAX (bound here, z -0.97, no clear allelic change, weak site); YY1 (bound here, z -0.43, no clear allelic change, weak site); HNF4A (bound elsewhere, z 53.69); GFI1 (bound elsewhere, z -31.27); NR2F2 (bound elsewhere, z 20.82). Occupancy unknown: ZNF493 (z -34.16); TBX19 (z 26.18); MBNL2 (z -22.42); NR1D1 (z 20.82); NR1D2 (z 20.82). Diagnostic, not shown to the model: 421 of 997 models pass Bonferroni.

## Ranked chains

### 1. H3: No TF-mediated effect of this variant (p = 0.65)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing G to T will not produce a reproducible TF-mediated occupancy and regulatory-output change attributable to this base.; The disease association may reflect linkage to another causal variant or a mechanism other than TF binding at this base; the cCRE and gene-level evidence need not identify the causal chain.; POU5F1B need not be a knockout dependency in colorectal cancer cells for a germline risk mechanism to exist.

Falsified if: Isogenic variant editing reproducibly changes TF occupancy and regulatory output, and perturbing the implicated TF removes the allele-dependent effect.

### 2. H1: Candidate TCF7L2-dependent regulation at the POU5F1B-associated enhancer (p = 0.23)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element The variant lies in pELS cCRE EH38E3858447; its target gene is unresolved.; gene POU5F1B; cell type HCT116 is a testable context, but the mechanism is not established in primary colorectal tissue..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is occupied over the variant and expressed in HCT116. The ref-favoring QBiC-SELEX result comes from LEF1- and TCF7-mapped models, not a TCF7L2-specific model; it makes ref G a tentative binding direction rather than demonstrating TCF7L2-specific allelic binding. | weak | [E04](#e04), [E05](#e05), [E20](#e20), [E35](#e35) |
| element | The variant overlaps the enhancer-like pELS cCRE EH38E3858447, whose target gene is not assigned by the available evidence. | supported | [E01](#e01), [E03](#e03), [E42](#e42) |
| gene | POU5F1B is a candidate target because it is nearby and the T allele is associated with increased POU5F1B expression in transverse colon; neither observation shows that this cCRE mediates that eQTL. | supported | [E02](#e02), [E17](#e17), [E37](#e37) |
| cell_type | HCT116 is a relevant testing context because TCF7L2 occupancy over the variant is reported there, but this does not establish the mechanism in primary colorectal tissue. | supported | [E04](#e04), [E05](#e05) |
| phenotype | A TCF7L2-to-POU5F1B regulatory effect could contribute to colorectal-cancer susceptibility, but no evidence connects this full chain to the disease association or establishes whether TCF7L2 activates or represses the element. | weak | [E15](#e15), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E37](#e37) |

Predictions: An endogenous allele-specific occupancy assay should show greater TCF7L2 occupancy on ref G than alt T if the proposed binding effect is real.; If this chain explains the transverse-colon eQTL, variant editing should make alt T increase POU5F1B expression; a repressive effect of ref-bound TCF7L2 is one possible, unproven explanation.; A reproducible allele-dependent regulatory effect attributed to this chain should be reduced by TCF7L2 perturbation.

Falsified if: A sufficiently powered endogenous assay finds no ref-versus-alt TCF7L2 occupancy difference.; Variant editing produces no reproducible POU5F1B regulatory effect, or TCF7L2 perturbation fails to alter an observed allele-dependent response.

### 3. H2: Weak alternative: possible SP1-dependent regulation at the candidate enhancer (p = 0.07)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in pELS cCRE EH38E3858447; its target gene is unresolved.; gene POU5F1B; cell type HCT116 is a context for testing because SP1 occupancy is reported there..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 is expressed and ChIP-bound over the variant in HCT116, but its own QBiC-SELEX model does not pass the change gate. The ref-favoring result is from a CIS-BP-mapped SP4 model at a weak site, so ref G is only a tentative direction and an SP1-specific allelic effect is not established. | weak | [E06](#e06), [E22](#e22), [E36](#e36) |
| element | The variant overlaps the enhancer-like pELS cCRE EH38E3858447, whose target gene is not assigned by the available evidence. | supported | [E01](#e01), [E03](#e03), [E42](#e42) |
| gene | POU5F1B is a candidate target based on proximity and its positive T-allele transverse-colon eQTL, but mediation by this cCRE is unshown. | supported | [E02](#e02), [E17](#e17), [E37](#e37) |
| cell_type | HCT116 is a context for testing this alternative because SP1 occupancy over the variant is reported there; this does not establish the mechanism in primary colorectal tissue. | supported | [E04](#e04), [E06](#e06) |
| phenotype | An SP1-dependent effect on POU5F1B could contribute to colorectal-cancer susceptibility, but no evidence connects this full regulatory chain to disease or establishes the regulatory direction. | weak | [E15](#e15), [E18c](#e18c), [E37](#e37) |

Predictions: If SP1 mediates the effect, endogenous assays should find a functionally relevant ref-G versus alt-T difference in SP1 occupancy despite the lack of a clear SP1-specific QBiC-SELEX change.; SP1 perturbation should alter any allele-dependent regulatory response attributed to this chain; a T-associated increase in POU5F1B would require, for example, ref-bound SP1 to repress, which is untested.; An SP1-mediated response may persist after TCF7L2 perturbation but should diminish after SP1 perturbation.

Falsified if: A sufficiently powered endogenous assay finds no meaningful SP1 occupancy difference between the alleles.; SP1 perturbation does not alter a reproducible allele-dependent regulatory response.

### 4. H4: Low-confidence alternative: NR2F2-related binding favors the alt allele (p = 0.05)

TF NR2F2 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in pELS cCRE EH38E3858447; its target gene is unresolved.; gene POU5F1B; cell type HCT116 is not supported as an NR2F2-occupied context at this site; occupancy there remains unestablished..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reported strong alt-favoring QBiC-SELEX change for NR2F2 comes from a model mapped to NR2F6, while the variant-overlapping NR2F2 ChIP peak is reported in HepG2 and no such peak is reported in HCT116; this is weak evidence for NR2F2-mediated binding in HCT116. | weak | [E04](#e04), [E29](#e29), [E43](#e43) |
| element | The variant overlaps the enhancer-like pELS cCRE EH38E3858447, whose target gene is not assigned by the available evidence. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is a candidate target because it is nearby and has a positive T-allele transverse-colon eQTL, but the link from this cCRE to POU5F1B is unproven. | supported | [E02](#e02), [E17](#e17), [E37](#e37) |
| cell_type | The available evidence does not establish NR2F2 occupancy at this site in HCT116; the reported variant-overlapping NR2F2 peak is from HepG2. | supported | [E29](#e29), [E43](#e43) |
| phenotype | An NR2F2-related effect could contribute to colorectal-cancer susceptibility only if the binding prediction operates in a relevant tissue and affects a disease-relevant target; neither connection is demonstrated. | weak | [E15](#e15), [E29](#e29), [E37](#e37) |

Predictions: If this chain operates in HCT116, a sensitive occupancy assay should detect NR2F2 at the site and show greater binding on alt T.; If the chain explains the POU5F1B eQTL, variant editing should alter POU5F1B expression and the effect should depend on NR2F2.; The alt-favoring prediction should not be treated as evidence for this chain unless occupancy in the relevant context is demonstrated.

Falsified if: Sensitive assays find no NR2F2 occupancy at the site in a relevant context.; There is no reproducible allele-dependent regulatory effect, or NR2F2 perturbation does not alter such an effect.

## Prediction matrix

| Test | Cost | Separates top two | H3 | H1 | H2 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 CUT&RUN or ChIP at the variant in HCT116 | low | yes | No reproducible allele-dependent TCF7L2 occupancy. | Greater occupancy on ref G than alt T. | No specific TCF7L2 allelic effect is required; an effect may instead track SP1. | No TCF7L2-dependent allelic effect is required; NR2F2 occupancy is the proposed alternative. |
| Isogenic G-to-T editing in HCT116, measuring POU5F1B expression with and without TCF7L2 perturbation | medium | yes | No reproducible variant-dependent POU5F1B response attributable to these TFs. | Editing changes POU5F1B expression, with the response reduced by TCF7L2 perturbation; an increase with T is consistent with, but does not prove, ref-bound repression. | An allele-dependent expression response is possible but should track SP1 perturbation rather than TCF7L2 perturbation. | An allele-dependent response should track NR2F2 perturbation if this chain operates. |
| Test physical contact between EH38E3858447 and the POU5F1B promoter in colorectal-relevant cells | high | no | A contact could still occur without a TF-mediated allelic effect. | Contact is compatible with the proposed target-gene link but does not establish TCF7L2 mediation. | Contact is compatible with the proposed target-gene link but does not establish SP1 mediation. | Contact is compatible with the proposed target-gene link but does not establish NR2F2 mediation. |

## Next experiment

Perform allele-specific TCF7L2 CUT&RUN at the variant in HCT116. It is the cheapest direct test separating the leading non-null chain (H1) from the null (H3): H1 predicts greater occupancy on ref G, whereas H3 predicts no reproducible allelic occupancy difference. A positive result would support only the binding step, not the enhancer-to-gene or disease links.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- qbic_tf_detail({"tf": "TCF7L2"}) for H1.binding, ran as [E35](#e35). Expected: If the detail confirms TCF7L2 has no own QBiC-SELEX model and the ref-favoring result is only from the mapped LEF1 model, H1.binding remains indirect; evidence of an applicable TCF7L2-specific model with the same direction would strengthen it, while no relevant allelic effect would weaken H1.
- qbic_tf_detail({"tf": "SP1"}) for H2.binding, ran as [E36](#e36). Expected: If SP1 has no own model and its only detected change is the weak-site SP4-mapped prediction, H2.binding remains weak; an SP1-specific model with a clear ref-favoring change would strengthen it, while no relevant allelic effect would weaken H2.
- gene_disease({"gene": "POU5F1B"}) for H1.gene, ran as [E37](#e37). Expected: If Open Targets reports colorectal-cancer association evidence for POU5F1B, H1.gene gains support beyond proximity and the eQTL, though the cCRE-to-gene link remains unproven; absent or weak disease evidence leaves the candidate-gene grade unchanged.

- Result of qbic_tf_detail({"tf": "TCF7L2"}) for H1.binding: E35 reports no TCF7L2-specific model: the detected ref-favoring changes come from CIS-BP-mapped LEF1 and TCF7 models. The LEF1-mapped model has a strong predicted site; the result remains indirect for TCF7L2. (as expected: yes)
- Result of qbic_tf_detail({"tf": "SP1"}) for H2.binding: E36 reports that SP1's own model does not pass the change-detection gate. The ref-favoring result is from a CIS-BP-mapped SP4 model at a weak site, leaving SP1-specific support weak. (as expected: yes)
- Result of gene_disease({"gene": "POU5F1B"}) for H1.gene: E37 reports an Open Targets overall POU5F1B–colorectal cancer score of 0.54, with genetic association evidence score 0.87. This adds gene-level support but does not link the variant-containing cCRE to POU5F1B. (as expected: yes)

Chains after revision: null 0.48; TCF7L2 0.40; SP1 0.12. Link grades changed: none.

### Round 2

- literature_search({"query": "chr8:127401060 colorectal cancer enhancer POU5F1B functional assay"}) for H1.phenotype, ran as [E38](#e38). Expected: If a report links this variant or its overlapping element to colorectal-cancer-relevant functional effects, H1.phenotype strengthens and the result may also refine the proposed target gene; if not, the phenotype link remains weak.
- literature_search({"query": "rs6983267 TCF7L2 MYC colorectal cancer enhancer allele-specific binding"}) for H1.gene, ran as [E39](#e39). Expected: If studies show that this locus's enhancer regulates MYC through allele-specific TCF7L2 binding, the POU5F1B target claim should be reconsidered in favor of MYC and a TCF7L2 mechanism; if not, the current target remains only a candidate.
- gene_disease({"gene": "MYC"}) for H1.phenotype, ran as [E40](#e40). Expected: A strong MYC–colorectal cancer association would support MYC as a disease-relevant alternative target, but would not by itself show that this cCRE regulates MYC or that the variant acts through TCF7L2.

- Result of literature_search for chr8:127401060 colorectal cancer enhancer POU5F1B functional assay: E38 returned zero hits for the query. No variant- or element-specific functional report was found in this search; the phenotype link therefore remains weak. (as expected: yes)
- Result of literature_search for rs6983267 TCF7L2 MYC colorectal cancer enhancer allele-specific binding: E39 returned literature hits, including a general report that CCAT2 can affect MYC-related pathways, but no cited result establishes that this variant's cCRE regulates MYC through allele-specific TCF7L2 binding. The POU5F1B target remains a candidate, not an established target. (as expected: yes)
- Result of gene_disease for MYC and colorectal cancer: E40 reports an overall MYC–colorectal cancer score of 0.12, with most support from literature and little genetic-association support. This does not strongly support MYC as the target of this variant or show regulation by this cCRE. (as expected: yes)

Chains after revision: null 0.62; TCF7L2 0.28; SP1 0.10. Link grades changed: none.

### Round 3

- gene_dependency({"gene": "POU5F1B"}) for H1.phenotype, ran as [E41](#e41). Expected: If POU5F1B shows a CRC-lineage knockout dependency, its disease-relevance link gains support and H1 (and H2, which share this target) rises modestly; no dependency would weaken that support but would not rule out a germline risk mechanism.
- literature_search({"query": "POU5F1B colorectal cancer risk variant chr8:127401060 enhancer target gene allele-specific"}) for H1.element, ran as [E42](#e42). Expected: A direct report linking this variant or its cCRE to POU5F1B would support or revise the enhancer-to-gene claim; a report identifying another target could change the gene link and ranking. No such result leaves the target unresolved.
- chip_peaks({"tf": "NR2F2", "biosample": "HCT116"}) for H4.binding, ran as [E43](#e43). Expected: If NR2F2 has a peak over the variant in HCT116, its strong alt-favoring QBiC-SELEX prediction and expression become more relevant, supporting a competing TF chain and potentially lowering H1/H2. No peak would leave the in-vitro prediction weak for this context.

- Result of gene_dependency({"gene":"POU5F1B"}) for H1.phenotype: E41 reports a CRISPR gene-effect score of -0.09 in HCT116, bowel-lineage median -0.06, and 0% dependent bowel-lineage lines. This does not support POU5F1B as a cancer-cell dependency, though it does not rule out a germline risk mechanism. (as expected: yes)
- Result of literature_search({"query":"POU5F1B colorectal cancer risk variant chr8:127401060 enhancer target gene allele-specific"}) for H1.element: E42 reports no literature hits for this query; the enhancer target remains unresolved. (as expected: yes)
- Result of chip_peaks({"tf":"NR2F2","biosample":"HCT116"}) for H4.binding: E43 reports no NR2F2 peak over the variant in HCT116; a variant-overlapping peak is reported in HepG2. The alt-favoring mapped-model prediction therefore remains weak for HCT116. (as expected: yes)

Chains after revision: null 0.65; TCF7L2 0.23; SP1 0.07; NR2F2 0.05. Link grades changed: H4.binding: absent → weak, H4.cell_type: absent → supported, H4.element: absent → supported, H4.gene: absent → supported, H4.phenotype: absent → weak.

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401060-127401060:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T16:33:46+00:00)

> Variant chr8:127401060:G>T (GRCh38), allele string G/T
> Known IDs: rs6983267
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: 1.54
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401060-128401060?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T16:33:42+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401060:G>T, by distance to TSS:
> POU5F1B: 78.9 kb from TSS (in gene body, strand +1)
> MYC: 334.4 kb from TSS (upstream, strand +1)
> LRATD2: 842.6 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T16:32:58+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:127401060:G>T: 330 peaks contain the variant, from 116 factors in 64 biosamples. In the matching biosample HCT116: 10 peaks from 9 factors. cCRE class at the variant: pELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID5B, ASH2L, CHD4, EHMT2, EP300, HDAC1, HDAC2, HMGXB4, KAT8, KDM1A, KDM6A, LCOR (+34 more). Bound, expressed TFs with a binding model: 64; listed one per row: TCF7L2, SP1, YY1, MAX, SRF, JUND, CEBPB, CTCF, MYBL2, ERF; also bound: NR2F6, NR2F1, ELF1, NR2C2, KLF16, CREM, TFAP4, RXRB, ATF2, RXRA, ZNF609, AHDC1, ZNF652, NFIA, HNF4A, MNX1, HNF1B, ZNF362, FOXA1, HMG20B, NR2F2, KLF6, NFIC, ATF1, TEAD4, ETV5, ZNF317, NFIL3, THAP11, ZBTB7B (+24 more). Bound but below 1 TPM: FOXA2, HNF1A, MIXL1, ONECUT1, SOX6, TBX2. Assayed with no peak here: 6 TFs in the matching biosample, 497 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000EUV). 63.61 TPM in DepMap:ACH-000971 (HCT 116), rank 53 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2, liver (e.g. ENCSR000BSF). 38.96 TPM in DepMap:ACH-000971 (HCT 116), rank 118 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> YY1: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BNX). 84.45 TPM in DepMap:ACH-000971 (HCT 116), rank 34 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSH). 42.59 TPM in DepMap:ACH-000971 (HCT 116), rank 102 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SRF: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSC). 25.61 TPM in DepMap:ACH-000971 (HCT 116), rank 217 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUND: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSA). 18.66 TPM in DepMap:ACH-000971 (HCT 116), rank 300 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSD). 13.15 TPM in DepMap:ACH-000971 (HCT 116), rank 408 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 150 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: 22Rv1, A549, A673, B cell, C4-2B, CD14-positive monocyte (+53 more) (e.g. ENCSR072EUE). 50.0 TPM in DepMap:ACH-000971 (HCT 116), rank 78 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 67.51 TPM in DepMap:ACH-000971 (HCT 116), rank 46 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ERF: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR159DQO). 46.58 TPM in DepMap:ACH-000971 (HCT 116), rank 90 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs6983267&size=100; retrieved 2026-10-25T16:33:55+00:00)

> 69 GWAS Catalog associations for rs6983267, strongest first:
> Colorectal cancer: p 2.0e-122, effect allele T, risk-allele frequency NR, PMID 36539618
> Prostate-specific antigen levels: p 9.0e-121, effect allele T, risk-allele frequency NR, PMID 39930085
> Prostate cancer: p 1.0e-113, effect allele G, risk-allele frequency NR, PMID 33398198
> Elevated prostate specific antigen [PSA] (PheCode 796): p 2.0e-96, effect allele G, risk-allele frequency 0.5087, PMID 39024449
> prostate-specific antigen (PSA, maximum, inv-norm transformed): p 7.0e-74, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Cancer (pleiotropy): p 8.0e-74, effect allele G, risk-allele frequency NR, PMID 32887889
> prostate-specific antigen (PSA, mean, inv-norm transformed): p 1.0e-72, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Colorectal cancer or advanced adenoma: p 3.0e-64, effect allele G, risk-allele frequency 0.5228, PMID 30510241
> prostate-specific antigen (PSA, minimum, inv-norm transformed): p 6.0e-52, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Benign neoplasm of colon (PheCode 208): p 2.0e-48, effect allele G, risk-allele frequency 0.5088, PMID 39024449
> Colon polyps: p 6.0e-30, effect allele G, risk-allele frequency 0.566, PMID 39024449
> Colon cancer (PheCode 153.2): p 8.0e-26, effect allele G, risk-allele frequency 0.5899, PMID 39024449

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T16:33:46+00:00)

> 92 credible sets contain 8_127401060_G_T: 91 GWAS, 1 molecular QTL.
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Cancer of prostate (PheCode 185): PIP 1.00; L2G POU5F1B 0.82
> GWAS Elevated prostate specific antigen [PSA] (PheCode 796): PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> sceqtl for PVT1 (OTAR2057_IBDverse_ge_Colon_Goblet_MUC2+_SPDEF+_ENS): PIP 0.95
> Best L2G gene scores across these sets: POU5F1B 0.89, MYC 0.05

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 2 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).
> CASC8 in Whole_Blood: NES -0.32, p 6.3e-10
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:21:59+00:00)

> Europe PMC: 150 hits for 'POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 42465001 (2026): Circ_0075829 affects POU5F1B expression through sponging miR-576-3p to promote growth, invasion, and angiogenesis of colon cancer cells.
> PMID 41993623 (2026): Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research.
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 41930642 (2026): Systematic Identification and Characterization of Causal Risk Genes Implicated in Colorectal Cancer by Integrating GWAS, eQTL, and mQTL Data.
> PMID 42686757 (2026): Phase separation of ecDNA condensates establishes in-trans contact domains that boost selective MYC regulatory interactions.
> PMID 40506516 (2025): Association between methylation quantitative trait loci and colorectal cancer risk, survival and cancer recurrence.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 41196428 (2025): Combined CHK1 and PD-L1 blockade as a novel therapeutic strategy against stemness and immunosuppression in ovarian cancer.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 42465001 (https://europepmc.org/article/MED/42465001; retrieved 2026-10-26T02:21:59+00:00)

> Circ_0075829 acted as a molecular sponge for microRNA-576-3p (miR-576-3p), thereby upregulating the expression of POU class 5 homeobox 1B (POU5F1B) in colon cancer cells.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 42465001 (https://europepmc.org/article/MED/42465001; retrieved 2026-10-26T02:21:59+00:00)

> Collectively, circ_0075829 promotes proliferation, invasion, and angiogenesis, while inhibiting apoptosis in colon cancer by modulating POU5F1B levels through miR-576-3p sponging.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 41930642 (https://europepmc.org/article/MED/41930642; retrieved 2026-10-26T02:21:59+00:00)

> A few potential regulatory influences on CRC development associated with genes and variants, such as POU5F1B and rs[masked], were identified.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 40506516 (https://europepmc.org/article/MED/40506516; retrieved 2026-10-26T02:21:59+00:00)

> Four regions mapped to POU5F1B, POU2AF2 (c11orf53)/POU2AF3 (COLCA2), GREM1 and CABLES2 were previously identified.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:127401060:G>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 64 occupied (19 with a strong site), 5 of 133 with unknown occupancy. Left out: 6 TFs assayed in the matching biosample and 497 assayed only elsewhere, none with a peak here; 6 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer (a CIS-BP-mapped model of LEF1), z -4.66, effect -0.47: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 63.61 TPM, rank 53 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000EUV. Best model's site strength: ref 98.8th, alt 98.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SRF (MADS box, 1 model; QBiC-SELEX coverage: own model): best model SRF_eDBD_TGCCAC40NGCC_KR_yin2017_0_3_7mer (its own model), z -7.74, effect -1.191: ref allele binds more (|z| above the gate), but between weak k-mers. 25.61 TPM, rank 217 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSC. Best model's site strength: ref 95.1th, alt 91.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): best model SP4_NA_TTATGT20NGTA_ESAE_yang2017_0_3_7mer (a CIS-BP-mapped model of SP4), z -4.76, effect -0.211: ref allele binds more (|z| above the gate), but between weak k-mers. 38.96 TPM, rank 118 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSF. Best model's site strength: ref 95.8th, alt 75.9th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUND (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUN_FL_TCAGTG40NGAT_KAE_yin2017_0_3_7mer (a CIS-BP-mapped model of JUN), z -3.01, effect -0.059: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 18.66 TPM, rank 300 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSA. Best model's site strength: ref 89.3th, alt 96.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPB (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (its own model), z 1.9, effect 0.205: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 13.15 TPM, rank 408 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSD. Best model's site strength: ref 75.7th, alt 85.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z -0.97, effect -0.058: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 42.59 TPM, rank 102 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSH. Best model's site strength: ref 91.8th, alt 95.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> YY1 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model YY1_FL_GG40NGTGAGA_YWKA_jolma2025_0_3_7mer (its own model), z -0.43, effect -0.033: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 84.45 TPM, rank 34 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BNX. Best model's site strength: ref 91.3th, alt 88.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF4A (Nuclear receptor, 1 model; QBiC-SELEX coverage: own model): best model TLX_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2E1), z 53.69, effect 1.968: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.95 TPM, rank 850 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, liver, e.g. ENCSR445QRF. Best model's site strength: ref 96.7th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GFI1 (C2H2 ZF, 2 models; QBiC-SELEX coverage: own model): best model GFI1B_eDBD_TTCTCA40NCCT_KR_yin2017_0_3_7mer (a CIS-BP-mapped model of GFI1B), z -31.27, effect -2.144: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.9 TPM, rank 857 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR849FVL. Best model's site strength: ref 99.9th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 61.74 TPM, rank 58 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BVM. Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF493 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF493_FL_TG40NTCTTGC_YWRA_jolma2025_0_2_7mer (its own model), z -34.16, effect -0.598: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.33 TPM, rank 977 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 88.9th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TBX19 (T-box, 2 models; QBiC-SELEX coverage: own model): best model TBX19_eDBD_TCTTGT40NCAG_KP_yin2017_0_4_7mer (its own model), z 26.18, effect 4.18: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.92 TPM, rank 936 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 79.0th, alt 99.9th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MBNL2 (CCCH ZF, 1 model; QBiC-SELEX coverage: own model): best model MBNL2_FL_TCTAAG40NTTA_KZ_yin2017_0_4_7mer (its own model), z -22.42, effect -2.708: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.09 TPM, rank 209 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.1th, alt 51.1th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1D1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 14.85 TPM, rank 361 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1D2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 37.06 TPM, rank 132 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401060:G>T","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.47,"z":-4.66,"p":3.2e-06,"rank_abs_z":"351/997","passed_gate":true,"site_strength":{"ref_percentile":98.8,"alt_percentile":98.4,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.229,"z":-4.59,"p":4.4e-06,"rank_abs_z":"367/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.275,"z":-3.47,"p":0.00052,"rank_abs_z":"486/997","passed_gate":false,"site_strength":{"ref_percentile":83.5,"alt_percentile":92.1,"k":7}}]}

<a id="e36"></a>**E36** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"SP1","symbol":"SP1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr8:127401060:G>T","gate_p":5.02e-05,"models":[{"model":"SP1_eDBD_TCTCTA40NCAC_KV_yin2017_0_3_7mer","mapping":"own","group":"G015 C2H2 ZF, 5 models","quality":0.891,"effect":-0.169,"z":-3.04,"p":0.0024,"rank_abs_z":"539/997","passed_gate":false,"site_strength":{"ref_percentile":95.4,"alt_percentile":93.6,"k":7}},{"model":"SP3_eDBD_TTCACC40NGCT_KR_yin2017_0_3_7mer","mapping":"CIS-BP (SP3)","group":"G015 C2H2 ZF, 5 models","quality":0.813,"effect":-0.119,"z":-2.52,"p":0.012,"rank_abs_z":"606/997","passed_gate":false,"site_strength":{"ref_percentile":70.1,"alt_percentile":75.3,"k":7}},{"model":"SP4_NA_TTATGT20NGTA_ESAE_yang2017_0_3_7mer","mapping":"CIS-BP (SP4)","group":"G015 C2H2 ZF, 5 models","quality":0.825,"effect":-0.211,"z":-4.76,"p":1.9e-06,"rank_abs_z":"344/997","passed_gate":true,"site_strength":{"ref_percentile":95.8,"alt_percentile":75.9,"k":7}},{"model":"SP8_NA_TGCTCG20NCTC_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (SP8)","group":"G015 C2H2 ZF, 5 models","quality":0.672,"effect":0.189,"z":2.99,"p":0.0028,"rank_abs_z":"545/997","passed_gate":false,"site_strength":{"ref_percentile":91.2,"alt_percentile":92.4,"k":7}},{"model":"SP9_eDBD_TACCGA40NATA_KP_yin2017_0_4_7mer","mapping":"CIS-BP (SP9)","group":"G015 C2H2 ZF, 5 models","quality":0.936,"effect":-0.228,"z":-2.8,"p":0.0051,"rank_abs_z":"571/997","passed_gate":false,"site_strength":{"ref_percentile":94.1,"alt_percentile":97.2,"k":7}}]}

<a id="e37"></a>**E37** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14

<a id="e38"></a>**E38** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr8%3A127401060%20colorectal%20cancer%20enhancer%20POU5F1B%20functional%20assay&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:05:42+00:00)

> Europe PMC: 0 hits for 'chr8:127401060 colorectal cancer enhancer POU5F1B functional assay'; top 0 with PMIDs:

<a id="e39"></a>**E39** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20TCF7L2%20MYC%20colorectal%20cancer%20enhancer%20allele-specific%20binding&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:05:42+00:00)

> Europe PMC: 86 hits for 'rs[masked] TCF7L2 MYC colorectal cancer enhancer allele-specific binding'; top 8 with PMIDs:
> PMID 41655184 (2026): LncRNA CCAT2 role in female-related cancer progression and diagnosis: a comprehensive review.
> PMID 41310609 (2025): The CCAT2 enigma: pioneering insights into colorectal cancer pathophysiology and therapeutic innovation.
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 41719390 (2026): Systematic analysis of functional genetic and epigenetic variants in colorectal cancer.
> PMID 39965570 (2025): An evolving understanding of multiple causal variants underlying genetic association signals.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 36428729 (2022): SNP-Target Genes Interaction Perturbing the Cancer Risk in the Post-GWAS.
> PMID 38670944 (2024): Fine-mapping analysis including over 254,000 East Asian and European descendants identifies 136 putative colorectal cancer susceptibility genes.

<a id="e39a"></a>**E39a** literature_search, Europe PMC abstract, PMID 41310609 (https://europepmc.org/article/MED/41310609; retrieved 2026-10-26T22:05:42+00:00)

> CCAT2 regulates gene expression and preserves chromosomal stability by modulating key oncogenic signaling pathways, including Wnt/β-catenin and MYC.

<a id="e39b"></a>**E39b** literature_search, Europe PMC abstract, PMID 41719390 (https://europepmc.org/article/MED/41719390; retrieved 2026-10-26T22:05:42+00:00)

> Colorectal cancer (CRC) is a leading cause of cancer-related mortality worldwide, yet the functional impact of noncoding variants on enhancer activity remains largely unexplored.

<a id="e40"></a>**E40** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T13:23:01+00:00)

> Open Targets: MYC and colorectal cancer (MONDO_0005575), overall score 0.12; by evidence type: literature 0.89, genetic_association 0.05

<a id="e41"></a>**E41** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for POU5F1B (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): -0.09. Bowel lineage, 31 lines: median -0.06, 0% dependent. All 351 lines: median -0.05, 3% dependent.

<a id="e42"></a>**E42** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20colorectal%20cancer%20risk%20variant%20chr8%3A127401060%20enhancer%20target%20gene%20allele-specific&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:07:27+00:00)

> Europe PMC: 0 hits for 'POU5F1B colorectal cancer risk variant chr8:127401060 enhancer target gene allele-specific'; top 0 with PMIDs:

<a id="e43"></a>**E43** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:12:23+00:00)

> No ENCODE NR2F2 ChIP-seq peak contains chr8:127401060:G>T in biosamples matching 'HCT116'. Absence can also mean no NR2F2 experiment in that biosample. In other biosamples, 1 NR2F2 peaks do contain the variant: HepG2 (experiments ENCSR000BVM).
