# rs4784227 and Breast cancer (16q12)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.03 over 15 model calls; 298 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GATA3 (bound here, z 18.65); FOXA1 (bound here, z 15.4); NR2F2 (bound here, z 9.51); TCF7L2 (bound here, z 8.45); SPDEF (bound here, z 5.89, weak site); MAFK (bound elsewhere, z 71.57); HOMEZ (bound elsewhere, z -49.09); MNX1 (bound elsewhere, z -27.02); PITX1 (bound elsewhere, z -21.39); TFAP4 (bound elsewhere, z 19.55). Occupancy unknown: MAFA (z 71.57); MAFB (z 71.57); LHX2 (z 28.05); LHX4 (z 28.05); LMX1B (z 28.05). Diagnostic, not shown to the model: 290 of 997 models pass Bonferroni.

## Ranked chains

### 1. FOXA1: T-favored forkhead-family binding contributes to regulation of TOX3 at the breast-cancer risk locus (p = 0.40)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is expressed and has a ChIP-seq peak over the variant in MCF-7. A FOXA2-mapped QBiC-SELEX model predicts stronger in-vitro binding to T than C at a strong site. This supports a forkhead-family sequence effect, but does not establish FOXA1-specific allele-dependent occupancy. FOXA1 is prioritized over the other candidates partly because the literature search returned a report connecting FOXA1 affinity variation with TOX3 expression at the 16q12.1 risk locus; the masked variant identifier limits confirmation that this is this exact SNP. | supported | [E04](#e04), [E05](#e05), [E21](#e21), [E40a](#e40a), [E40b](#e40b) |
| element | The variant lies in distal enhancer-like cCRE EH38E3180851. The reported activity scores are maxima across biosamples, not measurements specific to MCF-7, and the evidence does not establish that this cCRE is the element involved in the literature-reported TOX3 effect. | supported | [E01](#e01), [E03](#e03), [E40b](#e40b) |
| gene | TOX3 is nearby and strongly prioritized by breast-cancer locus-to-gene analyses. The literature search returned a report describing a risk-locus SNP effect on TOX3 and FOXA1-affinity changes at distal regulatory elements, but the SNP identifier is masked and the evidence does not directly connect EH38E3180851 to TOX3. No significant relevant GTEx eQTL is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E35](#e35), [E36](#e36), [E39](#e39), [E40a](#e40a), [E40b](#e40b) |
| cell_type | MCF-7 is a plausible test context because FOXA1 is expressed and has a ChIP-seq peak over the variant there; neither result establishes allele-specific occupancy. | supported | [E05](#e05), [E21](#e21) |
| phenotype | The variant is strongly associated with breast cancer, and the strongest listed associations identify T as the effect allele, compatible with the predicted T-favored in-vitro binding. A breast-cancer-related association also reports C, and the evidence does not establish FOXA1 mediation of disease risk. | supported | [E15](#e15), [E16](#e16), [E21](#e21) |

Predictions: In heterozygous MCF-7 cells, allele-resolved FOXA1 occupancy should favor T over C if this chain is active; compared with the GATA3 chain, FOXA1 should show the more prominent variant-associated allelic occupancy effect.; Editing C to T should alter enhancer output if the variant is functional, and may alter TOX3 expression; the direction of the expression change is not established.; The proposed route predicts that perturbing EH38E3180851 should affect TOX3 regulation, although the element-to-gene connection remains unproven.

Falsified if: A suitably powered allele-resolved assay in relevant breast cells finds no T-favored FOXA1 occupancy.; Precise variant editing shows no reproducible regulatory effect, or element perturbation and contact or expression assays fail to support a link from EH38E3180851 to TOX3.

### 2. NULL: No TF-mediated effect of this variant (p = 0.27)

Null chain: no TF-mediated effect of this variant.

Predictions: The breast-cancer association may arise from another causal change or a mechanism not mediated by TF binding altered by this variant.; The in-vitro binding predictions may not produce allele-specific occupancy or regulatory output at the endogenous locus; the reported literature result may concern a different masked variant or regulatory element.

Falsified if: Precise variant editing reproducibly changes endogenous allele-specific TF occupancy and enhancer output in relevant breast cells, and experiments connect that effect to TOX3 regulation and the disease-associated locus.

### 3. GATA3: T-favored GATA-family binding contributes to regulation at the TOX3-associated locus (p = 0.22)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is highly expressed and occupies the variant in MCF-7. A GATA2-mapped QBiC-SELEX model predicts stronger in-vitro binding to T than C at a strong site. This supports a GATA-family sequence effect, not GATA3-specific allele-dependent occupancy. The FOXA1-related literature result makes FOXA1 a stronger current candidate, but does not rule out GATA3. | supported | [E04](#e04), [E06](#e06), [E20](#e20), [E40a](#e40a), [E40b](#e40b) |
| element | The variant lies in distal enhancer-like cCRE EH38E3180851. Its reported chromatin activity scores are maxima across biosamples, not MCF-7-specific measurements; the connection of this cCRE to the literature-reported TOX3 effect is unresolved. | supported | [E01](#e01), [E03](#e03), [E40b](#e40b) |
| gene | TOX3 is nearby and strongly prioritized by breast-cancer locus-to-gene analyses. A literature search returned a report of a risk-locus SNP effect on TOX3, but its variant identifier is masked and it does not directly connect EH38E3180851 to TOX3. No significant relevant GTEx eQTL is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E35](#e35), [E36](#e36), [E39](#e39), [E40b](#e40b) |
| cell_type | MCF-7 is a plausible test context because GATA3 is highly expressed and has a ChIP-seq peak over the variant there; neither result demonstrates allele-specific occupancy. | supported | [E06](#e06), [E20](#e20) |
| phenotype | The strongest listed breast-cancer associations identify T as the effect allele, compatible with T-favored in-vitro binding. Another breast-cancer-related association reports C, and no evidence establishes GATA3 mediation. | supported | [E15](#e15), [E16](#e16), [E20](#e20) |

Predictions: In heterozygous MCF-7 cells, allele-resolved GATA3 occupancy should favor T over C if this chain is active; compared with the FOXA1 chain, GATA3 should show the more prominent variant-associated allelic occupancy effect.; Editing C to T should alter enhancer output if the variant is functional, and may alter TOX3 expression; the direction of the expression change is not established.

Falsified if: A suitably powered allele-resolved assay in relevant breast cells finds no T-favored GATA3 occupancy.; Precise variant editing shows no reproducible regulatory effect, or experiments fail to support a link from this element to TOX3.

### 4. NR2F2: T-favored nuclear-receptor-family binding contributes to regulation at the TOX3-associated locus (p = 0.07)

TF NR2F2 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NR2F2 is expressed and occupies the variant in MCF-7. A PPARG-mapped QBiC-SELEX model predicts stronger in-vitro binding to T than C at a strong site. This supports a nuclear-receptor-family sequence effect, not NR2F2-specific allele-dependent occupancy. Its lower expression and fewer reported matching-cell peaks make it a lower-priority candidate than FOXA1 or GATA3. | supported | [E04](#e04), [E08](#e08), [E22](#e22) |
| element | The variant lies in distal enhancer-like cCRE EH38E3180851. The activity scores are maxima across biosamples, not MCF-7-specific measurements, and the element-to-TOX3 link is unresolved. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is nearby and strongly prioritized by breast-cancer locus-to-gene analyses, but there is no direct evidence connecting this cCRE to TOX3. No significant relevant GTEx eQTL is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E35](#e35), [E36](#e36), [E39](#e39) |
| cell_type | MCF-7 is a possible test context because NR2F2 is expressed and has a ChIP-seq peak over the variant there; neither result shows allele-specific occupancy. | supported | [E08](#e08), [E22](#e22) |
| phenotype | The strongest listed breast-cancer associations identify T as the effect allele, compatible with T-favored in-vitro binding. Another breast-cancer-related association reports C, and no evidence establishes NR2F2 mediation. | supported | [E15](#e15), [E16](#e16), [E22](#e22) |

Predictions: If this chain is active, allele-resolved NR2F2 occupancy in heterozygous MCF-7 cells should favor T over C.; Editing C to T should alter enhancer output if the variant is functional, and may alter TOX3 expression; the direction of the expression change is not established.

Falsified if: A suitably powered allele-resolved assay in relevant breast cells finds no T-favored NR2F2 occupancy.; Precise variant editing shows no reproducible regulatory effect, or experiments fail to support a link from this element to TOX3.

### 5. TCF7L2: T-favored HMG-family binding contributes to regulation at the TOX3-associated locus (p = 0.04)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 has a reported MCF-7 peak over the variant, and a TCF7-mapped QBiC-SELEX model predicts stronger in-vitro binding to T than C at a strong site. This supports an HMG-family sequence effect, not TCF7L2-specific allele-dependent occupancy. Its low reported expression makes it a lower-priority candidate. | supported | [E04](#e04), [E09](#e09), [E23](#e23) |
| element | The variant lies in distal enhancer-like cCRE EH38E3180851. The activity scores are maxima across biosamples, not MCF-7-specific measurements, and the element-to-TOX3 link is unresolved. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is nearby and strongly prioritized by breast-cancer locus-to-gene analyses, but there is no direct evidence connecting this cCRE to TOX3. No significant relevant GTEx eQTL is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E35](#e35), [E36](#e36), [E39](#e39) |
| cell_type | MCF-7 is a possible test context because a TCF7L2 ChIP-seq peak over the variant is reported there; low reported expression and the absence of allele-specific occupancy limit the inference. | supported | [E09](#e09), [E23](#e23) |
| phenotype | The strongest listed breast-cancer associations identify T as the effect allele, compatible with T-favored in-vitro binding. Another breast-cancer-related association reports C, and no evidence establishes TCF7L2 mediation. | supported | [E15](#e15), [E16](#e16), [E23](#e23) |

Predictions: If this chain is active, allele-resolved TCF7L2 occupancy in heterozygous MCF-7 cells should favor T over C.; Editing C to T should alter enhancer output if the variant is functional, and may alter TOX3 expression; the direction of the expression change is not established.

Falsified if: A suitably powered allele-resolved assay in relevant breast cells finds no T-favored TCF7L2 occupancy.; Precise variant editing shows no reproducible regulatory effect, or experiments fail to support a link from this element to TOX3.

## Prediction matrix

| Test | Cost | Separates top two | FOXA1 | NULL | GATA3 | NR2F2 | TCF7L2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-resolved FOXA1 and GATA3 CUT&RUN or ChIP in heterozygous MCF-7 cells, comparing T:C occupancy at the variant | medium | yes | T-favored FOXA1 occupancy, with a stronger variant-associated allelic imbalance for FOXA1 than for GATA3. | Neither factor shows reproducible variant-linked allelic occupancy, or observed imbalance is not attributable to the variant. | T-favored GATA3 occupancy, with a stronger variant-associated allelic imbalance for GATA3 than for FOXA1. | No uniquely predicted FOXA1- or GATA3-dominant imbalance; this test does not directly assess the proposed NR2F2 effect. | No uniquely predicted FOXA1- or GATA3-dominant imbalance; this test does not directly assess the proposed TCF7L2 effect. |
| Precise C-to-T editing in MCF-7 cells followed by enhancer activity and TOX3 expression measurements | high | no | Editing produces a reproducible regulatory change; the direction of TOX3 expression change is not specified. | No reproducible variant-dependent enhancer or TOX3 expression change. | Editing produces a reproducible regulatory change; the direction of TOX3 expression change is not specified. | Editing produces a reproducible regulatory change; the direction of TOX3 expression change is not specified. | Editing produces a reproducible regulatory change; the direction of TOX3 expression change is not specified. |
| Perturb EH38E3180851 and assay TOX3 expression or enhancer-promoter contact in MCF-7 cells | medium | no | Perturbation changes TOX3 regulation or supports a contact between this element and TOX3, though it does not by itself prove FOXA1 mediation. | No detectable element-to-TOX3 regulatory effect; a negative result would not rule out other targets or contexts. | Perturbation changes TOX3 regulation or supports a contact between this element and TOX3, though it does not by itself prove GATA3 mediation. | Perturbation changes TOX3 regulation or supports a contact between this element and TOX3, though it does not by itself prove NR2F2 mediation. | Perturbation changes TOX3 regulation or supports a contact between this element and TOX3, though it does not by itself prove TCF7L2 mediation. |

## Next experiment

Perform allele-resolved FOXA1 and GATA3 CUT&RUN or ChIP in heterozygous MCF-7 cells and compare T:C occupancy for both factors. This is the cheapest direct test among the proposed experiments for distinguishing the top two chains; it tests occupancy but would not by itself establish enhancer output or TOX3 regulation.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- literature_search({"query": "chr16:52565276 TOX3 EH38E3180851 breast cancer enhancer functional validation"}) for GATA3.gene, ran as [E35](#e35). Expected: If the search finds variant- or element-specific functional evidence connecting EH38E3180851 to TOX3, the shared TOX3 gene link gains support; if not, it remains weak.
- eqtl_lookup({"tissue": "breast mammary tissue"}) for FOXA1.gene, ran as [E36](#e36). Expected: If a relevant-tissue eQTL links this variant to TOX3 or another plausible target, it could strengthen or redirect the gene link and provide an expression-effect direction; if none is found, the link remains weak.

- Result of literature_search({"query": "chr16:52565276 TOX3 EH38E3180851 breast cancer enhancer functional validation"}) for GATA3.gene: E35 reports zero literature hits for the variant/element-specific functional-validation search. (as expected: yes)
- Result of eqtl_lookup({"tissue": "breast mammary tissue"}) for FOXA1.gene: E36 reports zero significant GTEx v8 eQTLs for this variant in breast mammary tissue. (as expected: yes)

Chains after revision: null 0.55; GATA3 0.17; FOXA1 0.16; NR2F2 0.12. Link grades changed: none.

### Round 2

- literature_search({"query": "rs4784227 FOXA1 GATA3 allele-specific binding TOX3 breast cancer"}) for FOXA1.binding, ran as [E37](#e37). Expected: If the literature reports variant-specific functional evidence favoring FOXA1 over GATA3, FOXA1.binding and its relative ranking rise; if it contradicts the predicted T-favored effect or provides no site-specific support, that chain falls or remains based on indirect evidence.
- literature_search({"query": "rs4784227 TOX3 enhancer promoter interaction breast cancer functional validation"}) for GATA3.gene, ran as [E38](#e38). Expected: If functional studies link this variant-containing enhancer to TOX3, the gene-link grade strengthens for the non-null chains; if they implicate another target or show no direct connection, the TOX3 links remain weak or fall.
- gene_disease({"gene": "TOX3"}) for FOXA1.gene, ran as [E39](#e39). Expected: If Open Targets shows strong breast-cancer evidence for TOX3, this strengthens target-gene plausibility but does not establish that this cCRE regulates TOX3; weak or absent gene-level evidence leaves the gene link weak.

- Result of literature_search({"query": "rs4784227 FOXA1 GATA3 allele-specific binding TOX3 breast cancer"}): E37 returned broad reviews and post-GWAS analyses, including no site-specific result in the supplied quotes that favors FOXA1 over GATA3 or validates allele-specific binding at this variant. (as expected: yes)
- Result of literature_search({"query": "rs4784227 TOX3 enhancer promoter interaction breast cancer functional validation"}): E38 includes broad review statements about enhancer variants and the need for functional validation, but supplies no direct evidence that this variant-containing cCRE regulates TOX3. (as expected: yes)
- Result of gene_disease({"gene": "TOX3"}): E39 reports an Open Targets overall TOX3–breast cancer score of 0.58, with genetic-association and literature scores of 0.91 and 0.89. This supports TOX3 as a disease-relevant gene but does not link EH38E3180851 to TOX3. (as expected: yes)

Chains after revision: null 0.32; GATA3 0.27; FOXA1 0.25; NR2F2 0.10; TCF7L2 0.06. Link grades changed: FOXA1.phenotype: supported → weak, GATA3.phenotype: supported → weak, NR2F2.phenotype: supported → weak, TCF7L2.binding: absent → supported, TCF7L2.cell_type: absent → supported, TCF7L2.element: absent → supported, TCF7L2.gene: absent → weak, TCF7L2.phenotype: absent → weak.

### Round 3

- literature_search({"query": "rs4784227 TOX3 enhancer allele-specific reporter assay chromatin interaction breast cancer"}) for GATA3.gene, ran as [E40](#e40). Expected: If this finds variant- or EH38E3180851-specific reporter, perturbation, or chromatin-contact evidence linking the element to TOX3, the gene link becomes better supported and the GATA3 chain rises; if it finds no direct evidence, the gene link remains weak.

- Result of literature_search({"query":"rs4784227 TOX3 enhancer allele-specific reporter assay chromatin interaction breast cancer"}) for GATA3.gene: E40 returned literature quotes describing breast-cancer risk variants that alter FOXA1 affinity and allele-specific gene expression, with a masked SNP example affecting TOX3 at the 16q12.1 risk locus. The returned text does not identify the SNP or EH38E3180851 unambiguously and does not report a direct assay of this specific element. (as expected: unclear)

Chains after revision: FOXA1 0.40; null 0.27; GATA3 0.22; NR2F2 0.07; TCF7L2 0.04. Link grades changed: FOXA1.phenotype: weak → supported, GATA3.phenotype: weak → supported, NR2F2.phenotype: weak → supported, TCF7L2.phenotype: weak → supported.

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:52565276-52565276:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:24+00:00)

> Variant chr16:52565276:C>T (GRCh38), allele string C/T
> Known IDs: rs4784227
> Most severe consequence: intron_variant
> Regulatory features: ENSR16_9QTBS enhancer
> GERP conservation score at the site: -2
> Transcript consequences: CASC16 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:51565276-53565276?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:47+00:00)

> 6 protein-coding genes within 1000 kb of chr16:52565276:C>T, by distance to TSS:
> TOX3: 17.5 kb from TSS (upstream, strand -1)
> CHD9NB: 487.6 kb from TSS (downstream, strand -1)
> CHD9: 489.7 kb from TSS (upstream, strand +1)
> RBL2: 868.7 kb from TSS (upstream, strand +1)
> AKTIP: 939.1 kb from TSS (downstream, strand -1)
> HNRNPA1L3: 1011.8 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E3180851 (dELS: distal enhancer-like), chr16:52565011-52565360.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3180851 dELS (contains the variant): DNase z 4.2, H3K27ac z 6.1, H3K4me3 z 1.8, CTCF z 1.9; nearby genes CASC16, TOX3, AC026462.5
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr16:52565276:C>T: 276 peaks contain the variant, from 193 factors in 7 biosamples. In the matching biosample MCF-7: 14 peaks from 9 factors. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, ARID5B, ASH2L, BCL3, CBX5, CHD4, CTBP1, DPF2, EP300, GATAD1, GZF1, HBP1 (+64 more). Bound, expressed TFs with a binding model: 95; listed one per row: FOXA1, GATA3, SPDEF, NR2F2, TCF7L2, SP1, MYBL2, MAX, JUND, RXRA; also bound: YY1, GATAD2A, ZGPAT, CREM, FOSL2, ZNF609, ZNF703, TEAD1, RXRB, FOXP4, EGR1, MEF2D, ZNF800, AHDC1, GMEB1, ZNF772, ZNF788P, HMG20B, ELF1, TRAFD1, E2F4, ELF3, RELA, MLX, TBX2, ERF, HMG20A, BHLHE40, CREB1, ZBTB7B (+55 more). Bound but below 1 TPM: DLX6, ETS1, FOXA2, FOXA3, GATA4, GFI1, HLF, HNF1A, HNF1B, HNF4A. Assayed with no peak here: 45 TFs in the matching biosample, 411 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXA1: bound here. 8 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in A549, HepG2, liver (e.g. ENCSR126YEB). 88.38 TPM in DepMap:ACH-000019 (MCF7), rank 28 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATA3: bound here. 7 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in A549, T47D (e.g. ENCSR000EWV). 346.04 TPM in DepMap:ACH-000019 (MCF7), rank 5 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SPDEF: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR042GSX). 72.51 TPM in DepMap:ACH-000019 (MCF7), rank 40 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in HepG2 (e.g. ENCSR000BUY). 38.14 TPM in DepMap:ACH-000019 (MCF7), rank 103 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000EWT). 4.89 TPM in DepMap:ACH-000019 (MCF7), rank 642 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound elsewhere. 6 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, HepG2, liver (e.g. ENCSR386YIH). 33.01 TPM in DepMap:ACH-000019 (MCF7), rank 122 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 5 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BRO). 49.2 TPM in DepMap:ACH-000019 (MCF7), rank 66 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, liver (e.g. ENCSR521IID). 76.95 TPM in DepMap:ACH-000019 (MCF7), rank 35 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUND: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, liver (e.g. ENCSR000BGK). 44.21 TPM in DepMap:ACH-000019 (MCF7), rank 83 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> RXRA: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, liver (e.g. ENCSR352QSB). 30.65 TPM in DepMap:ACH-000019 (MCF7), rank 132 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs4784227&size=100; retrieved 2026-10-25T17:26:28+00:00)

> 34 GWAS Catalog associations for rs4784227, strongest first:
> Breast cancer: p 2.0e-240, effect allele T, risk-allele frequency NR, PMID 32139696
> Postmenopausal breast cancer: p 5.0e-50, effect allele T, risk-allele frequency NR, PMID 38538606
> Breast cancer (estrogen-receptor negative): p 2.0e-26, effect allele T, risk-allele frequency 0.24, PMID 29058716
> Biological Mother:  Cancer, Breast: p 2.0e-25, effect allele C, risk-allele frequency 0.7783, PMID 39024449
> Breast cancer (estrogen-receptor positive): p 1.0e-13, effect allele T, risk-allele frequency 0.06, PMID 38741014
> Parkinson's disease: p 1.0e-10, effect allele T, risk-allele frequency 0.265, PMID 28892059
> Systolic blood pressure: p 1.0e-09, effect allele T, risk-allele frequency 0.2398, PMID 33230300
> BRCA1/2-negative high-risk breast cancer: p 2.0e-09, effect allele T, risk-allele frequency 0.26, PMID 30323354
> Pulse pressure: p 2.0e-08, effect allele T, risk-allele frequency 0.2354, PMID 33230300
> Cancer: p 3.0e-08, effect allele ?, risk-allele frequency NR, PMID 34290314

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:25+00:00)

> 83 credible sets contain 16_52565276_C_T: 74 GWAS, 9 molecular QTL.
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, excluding all cancers (control: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.93
> GWAS Breast cancer (luminal A): PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, ER-positive, excluding all can: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer [female] (PheCode 174.1): PIP 1.00; L2G TOX3 0.92
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_spinal_cord_ensg00000285800_1_): PIP 0.07
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_hippocampus_ensg00000285800): PIP 0.06
> tuqtl for TOX3 (gtex-v10_txrev_brain_hippocampus_ensg00000103460_g): PIP 0.05
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_spinal_cord_ensg00000285800): PIP 0.04
> tuqtl for TOX3 (gtex-v10_txrev_brain_substantia_nigra_ensg00000103): PIP 0.04
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_hippocampus_ensg00000285800_1_): PIP 0.03
> Best L2G gene scores across these sets: TOX3 0.96

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TOX3%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:25:47+00:00)

> Europe PMC: 586 hits for 'TOX3 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 41849381 (2026): A transcription regulator atlas identifies TOX3 as an Atoh1 coactivator in cerebellar development and tumorigenesis.
> PMID 41595182 (2026): Identification and Characterisation of Canine Osteosarcoma Biomarkers and Therapeutic Targets.
> PMID 41596432 (2026): Bone Metastasis in Estrogen Receptor-Positive Breast Cancer: Molecular Insights and Therapeutic Advances.
> PMID 40932605 (2025): Molecular signatures of breast cancer in the Iranian population: a review of cell growth and cell cycle regulators.
> PMID 42700350 (2026): Interactions between circular RNAs (circRNAs) and the Hippo pathway in cancer.
> PMID 41871294 (2026): A reanalysis of a genome-wide association study on breast cancer in Asian populations using the SG10K_Health reference panel for imputation: a multi-Centre case-control analysis.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-26T02:25:47+00:00)

> Key examples include promoter mutations [e.g., rs[masked] (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs[masked] (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41871294 (https://europepmc.org/article/MED/41871294; retrieved 2026-10-26T02:25:47+00:00)

> Differences in panel performance influenced association signals, including breast cancer candidate loci such as FGFR2, TOX3, and ESR1.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:52565276:C>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000019), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 95 occupied (27 with a strong site), 5 of 75 with unknown occupancy. Left out: 45 TFs assayed in the matching biosample and 411 assayed only elsewhere, none with a peak here; 22 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (a CIS-BP-mapped model of GATA2), z 18.65, effect 0.283: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 346.04 TPM, rank 5 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWV. Best model's site strength: ref 92.3th, alt 98.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXA1 (Forkhead, 4 models; QBiC-SELEX coverage: own model): best model FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer (a CIS-BP-mapped model of FOXA2), z 15.4, effect 0.296: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 88.38 TPM, rank 28 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR126YEB. Best model's site strength: ref 91.3th, alt 98.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model PPARG_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of PPARG), z 9.51, effect 0.22: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 38.14 TPM, rank 103 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000BUY. Best model's site strength: ref 95.4th, alt 97.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer (a CIS-BP-mapped model of TCF7), z 8.45, effect 0.455: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.89 TPM, rank 642 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWT. Best model's site strength: ref 81.2th, alt 97.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SPDEF (Ets, 18 models; QBiC-SELEX coverage: own model): best model ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer (a CIS-BP-mapped model of ELF1), z 5.89, effect 0.213: alt allele binds more (|z| above the gate), but between weak k-mers. 72.51 TPM, rank 40 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR042GSX. Best model's site strength: ref 79.2th, alt 76.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAFK (bZIP, 6 models; QBiC-SELEX coverage: own model): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (a CIS-BP-mapped model of MAFG), z 71.57, effect 2.788: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 16.96 TPM, rank 253 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000EEB. Best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOMEZ (Homeodomain, 1 model; QBiC-SELEX coverage: own model): best model HOMEZ_NA_TCGATC20NTAT_ESY_yang2017_0_3_7mer (its own model), z -49.09, effect -2.698: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR117CHD. Best model's site strength: ref 99.4th, alt 89.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MNX1 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model BARHL2_NA_TATTGT20NGTG_ESAC_yang2017_0_2_7mer (a CIS-BP-mapped model of BARHL2), z -27.02, effect -0.936: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.78 TPM, rank 791 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR108MKR. Best model's site strength: ref 99.9th, alt 95.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PITX1 (Homeodomain, 11 models; QBiC-SELEX coverage: own model): best model TPRX1_DBD_TG40NGACCTT_YWCB_jolma2025_0_2_7mer (a CIS-BP-mapped model of TPRX1), z -21.39, effect -0.283: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.1 TPM, rank 702 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR374MAS. Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP4 (bHLH, 1 model; QBiC-SELEX coverage: own model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (its own model), z 19.55, effect 1.433: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.85 TPM, rank 542 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR103SZL. Best model's site strength: ref 83.4th, alt 100.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAFA (bZIP, 6 models; QBiC-SELEX coverage: own model): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (a CIS-BP-mapped model of MAFG), z 71.57, effect 2.788: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.07 TPM, rank 953 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAFB (bZIP, 6 models; QBiC-SELEX coverage: own model): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (a CIS-BP-mapped model of MAFG), z 71.57, effect 2.788: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.09 TPM, rank 773 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> LHX2 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model LHX8_FL_TTGCGA40NGTA_KW_yin2017_0_4_7mer (a CIS-BP-mapped model of LHX8), z 28.05, effect 2.175: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.59 TPM, rank 898 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.6th, alt 99.3th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> LHX4 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model LHX8_FL_TTGCGA40NGTA_KW_yin2017_0_4_7mer (a CIS-BP-mapped model of LHX8), z 28.05, effect 2.175: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.58 TPM, rank 900 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.6th, alt 99.3th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> LMX1B (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model LHX8_FL_TTGCGA40NGTA_KW_yin2017_0_4_7mer (a CIS-BP-mapped model of LHX8), z 28.05, effect 2.175: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 11.66 TPM, rank 366 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.6th, alt 99.3th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr16%3A52565276%20TOX3%20EH38E3180851%20breast%20cancer%20enhancer%20functional%20validation&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:28:22+00:00)

> Europe PMC: 0 hits for 'chr16:52565276 TOX3 EH38E3180851 breast cancer enhancer functional validation'; top 0 with PMIDs:

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'breast mammary tissue'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20FOXA1%20GATA3%20allele-specific%20binding%20TOX3%20breast%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:05:52+00:00)

> Europe PMC: 9 hits for 'rs[masked] FOXA1 GATA3 allele-specific binding TOX3 breast cancer'; top 8 with PMIDs:
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 32765587 (2020): ABC-GWAS: Functional Annotation of Estrogen Receptor-Positive Breast Cancer Genetic Variants.
> PMID 31757997 (2019): Identification of two novel breast cancer loci through large-scale genome-wide association study in the Japanese population.
> PMID 30116257 (2018): Elucidating the Underlying Functional Mechanisms of Breast Cancer Susceptibility Through Post-GWAS Analyses.
> PMID 26001967 (2015): Global transcription network incorporating distal regulator binding reveals selective cooperation of cancer drivers and risk genes.
> PMID 29215763 (2018): Breast cancer: The translation of big genomic data to cancer precision medicine.
> PMID 27807102 (2016): Emergence of the Noncoding Cancer Genome: A Target of Genetic and Epigenetic Alterations.
> PMID 25327703 (2014): Genome-wide association study of breast cancer in Latinas identifies novel protective variants on 6q25.

<a id="e37a"></a>**E37a** literature_search, Europe PMC abstract, PMID 38902506 (https://europepmc.org/article/MED/38902506; retrieved 2026-10-26T22:05:52+00:00)

> This review provides an overview of somatic and germline non-coding single nucleotide alterations affecting transcription factor binding sites in GREs, specifically involved in cancer biology.

<a id="e37b"></a>**E37b** literature_search, Europe PMC abstract, PMID 32765587 (https://europepmc.org/article/MED/32765587; retrieved 2026-10-26T22:05:52+00:00)

> By integrating large-scale multi-omics datasets such as the Cancer Genome Atlas (TCGA) and the Encyclopedia of DNA Elements (ENCODE), we performed multivariate linear regression analysis of expression quantitative trait loci, sequence permutation test of transcription factor binding perturbation, and modeling of three-dimensional chromatin interactions to analyze the potential molecular functions of 2,813 single nucleotide variants in 93 genomic loci associated with estrogen receptor-positive breast cancer.

<a id="e37c"></a>**E37c** literature_search, Europe PMC abstract, PMID 26001967 (https://europepmc.org/article/MED/26001967; retrieved 2026-10-26T22:05:52+00:00)

> Furthermore, cancer risk alleles tended to increase the susceptibility of the transcription of their associated genes.

<a id="e37d"></a>**E37d** literature_search, Europe PMC abstract, PMID 26001967 (https://europepmc.org/article/MED/26001967; retrieved 2026-10-26T22:05:52+00:00)

> These findings suggest that transcriptional cancer drivers selectively induce a combinatorial misregulation of downstream risk genes, and that genetic risk factors, mostly residing in distal regulatory regions, increase transcriptional susceptibility to upstream cancer-driving somatic changes.

<a id="e38"></a>**E38** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20TOX3%20enhancer%20promoter%20interaction%20breast%20cancer%20functional%20validation&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:05:58+00:00)

> Europe PMC: 12 hits for 'rs[masked] TOX3 enhancer promoter interaction breast cancer functional validation'; top 8 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 38967009 (2024): Integration of chromosome locations and functional aspects of enhancers and topologically associating domains in knowledge graphs enables versatile queries about gene regulation.
> PMID 32765587 (2020): ABC-GWAS: Functional Annotation of Estrogen Receptor-Positive Breast Cancer Genetic Variants.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 25473424 (2014): Enhancer variants: evaluating functions in common disease.
> PMID 28722347 (2017): FOXO3 longevity interactome on chromosome 6.
> PMID 24661571 (2014): Laying a solid foundation for Manhattan--'setting the functional basis for the post-GWAS era'.

<a id="e38a"></a>**E38a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-26T22:05:58+00:00)

> Key examples include promoter mutations [e.g., rs[masked] (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs[masked] (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e38b"></a>**E38b** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-26T22:05:58+00:00)

> This Review also critically identifies the pressing need for more specific functional validation studies to fully elucidate their mechanistic roles.

<a id="e38c"></a>**E38c** literature_search, Europe PMC abstract, PMID 32765587 (https://europepmc.org/article/MED/32765587; retrieved 2026-10-26T22:05:58+00:00)

> By integrating large-scale multi-omics datasets such as the Cancer Genome Atlas (TCGA) and the Encyclopedia of DNA Elements (ENCODE), we performed multivariate linear regression analysis of expression quantitative trait loci, sequence permutation test of transcription factor binding perturbation, and modeling of three-dimensional chromatin interactions to analyze the potential molecular functions of 2,813 single nucleotide variants in 93 genomic loci associated with estrogen receptor-positive breast cancer.

<a id="e39"></a>**E39** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:34:32+00:00)

> Open Targets: TOX3 and breast cancer (MONDO_0007254), overall score 0.58; by evidence type: genetic_association 0.91, literature 0.89

<a id="e40"></a>**E40** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20TOX3%20enhancer%20allele-specific%20reporter%20assay%20chromatin%20interaction%20breast%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:07:34+00:00)

> Europe PMC: 9 hits for 'rs[masked] TOX3 enhancer allele-specific reporter assay chromatin interaction breast cancer'; top 8 with PMIDs:
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 30116257 (2018): Elucidating the Underlying Functional Mechanisms of Breast Cancer Susceptibility Through Post-GWAS Analyses.
> PMID 27807102 (2016): Emergence of the Noncoding Cancer Genome: A Target of Genetic and Epigenetic Alterations.
> PMID 23001124 (2012): Breast cancer risk-associated SNPs modulate the affinity of chromatin for FOXA1 and alter gene expression.
> PMID 25473424 (2014): Enhancer variants: evaluating functions in common disease.
> PMID 25288875 (2014): Functional annotation of putative regulatory elements at cancer susceptibility Loci.
> PMID 29382703 (2018): Common Genetic Variation and Breast Cancer Risk-Past, Present, and Future.
> PMID 25976354 (2015): Human Enhancers Are Fragile and Prone to Deactivating Mutations.

<a id="e40a"></a>**E40a** literature_search, Europe PMC abstract, PMID 23001124 (https://europepmc.org/article/MED/23001124; retrieved 2026-10-26T22:07:34+00:00)

> Our results show that breast cancer risk-associated SNPs are enriched in the cistromes of FOXA1 and ESR1 and the epigenome of histone H3 lysine 4 monomethylation (H3K4me1) in a cancer- and cell type-specific manner.

<a id="e40b"></a>**E40b** literature_search, Europe PMC abstract, PMID 23001124 (https://europepmc.org/article/MED/23001124; retrieved 2026-10-26T22:07:34+00:00)

> Furthermore, the majority of the risk-associated SNPs modulate the affinity of chromatin for FOXA1 at distal regulatory elements, thereby resulting in allele-specific gene expression, which is exemplified by the effect of the rs[masked] SNP on the TOX3 gene within the 16q12.1 risk locus.
