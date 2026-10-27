# rs4784227 and Breast cancer (16q12)

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 301 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H4: No demonstrated TF-mediated effect of rs4784227 (p = 0.75)

Null chain: no TF-mediated effect of this variant.

Predictions: The breast cancer association may arise from a linked causal variant or another mechanism, without a TF-mediated effect of this base.; Allele-specific perturbation of rs4784227 may show no reproducible change in TF occupancy, enhancer output, or target-gene expression.

Falsified if: Precise allele replacement reproducibly changes TF binding and enhancer activity at this base, and links that change to a target gene and a breast-cancer-relevant phenotype.

### 2. H1: FOXA1-dependent enhancer effect on TOX3 (p = 0.15)

TF FOXA1 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3180851, a distal enhancer-like element overlapping rs4784227; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This hypothesis provisionally predicts that FOXA1 binds ref C more strongly than alt T; FOXA1 occupies the site and is abundant in MCF-7, but no supplied evidence measures allele-specific binding or provides a QBiC-SELEX result establishing this direction. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies in enhancer-like cCRE EH38E3180851, but allele-dependent activity or FOXA1 dependence has not been demonstrated. | supported | [E01](#e01), [E03](#e03), [E05](#e05) |
| gene | TOX3 is the leading candidate target by proximity and genetic prioritization, but this cCRE has not been directly linked to TOX3; no significant GTEx eQTL is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | FOXA1 occupancy and high expression make MCF-7 a plausible context for this proposed mechanism. | supported | [E05](#e05) |
| phenotype | Alt T is associated with breast cancer risk, and TOX3 has gene-level breast cancer support, but the evidence does not connect FOXA1 binding at this element to TOX3 regulation or risk. | weak | [E15](#e15), [E16](#e16), [E21](#e21) |

Predictions: In allele-specific FOXA1 occupancy assays in MCF-7, C should show greater occupancy than T; this is a proposed direction, not an observed result.; If FOXA1 mediates the variant effect, FOXA1 perturbation should reduce the allele-dependent enhancer or TOX3 response. The direction of the TOX3 response is not established by the supplied evidence.

Falsified if: A well-powered allele-specific assay shows equal FOXA1 occupancy or greater occupancy on T.; FOXA1 perturbation has no allele-dependent effect on enhancer output or TOX3 expression.

### 3. H2: GATA3-dependent enhancer effect on TOX3 (p = 0.07)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851, a distal enhancer-like element overlapping rs4784227; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This hypothesis provisionally predicts that GATA3 binds alt T more strongly than ref C; GATA3 occupies the site and is abundant in MCF-7, but no supplied evidence measures allele-specific binding or provides a QBiC-SELEX result establishing this direction. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies in enhancer-like cCRE EH38E3180851, but allele-dependent activity or GATA3 dependence has not been demonstrated. | supported | [E01](#e01), [E03](#e03), [E06](#e06) |
| gene | TOX3 is the leading candidate target by proximity and genetic prioritization, but this cCRE has not been directly linked to TOX3; no significant GTEx eQTL is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | GATA3 occupancy and high expression make MCF-7 a plausible context for this proposed mechanism. | supported | [E06](#e06) |
| phenotype | Alt T is associated with breast cancer risk, and TOX3 has gene-level breast cancer support, but the evidence does not connect GATA3 binding at this element to TOX3 regulation or risk. | weak | [E15](#e15), [E16](#e16), [E21](#e21) |

Predictions: In allele-specific GATA3 occupancy assays in MCF-7, T should show greater occupancy than C; this is a proposed direction, not an observed result.; If GATA3 mediates the variant effect, GATA3 perturbation should reduce the allele-dependent enhancer or TOX3 response. The direction of the TOX3 response is not established by the supplied evidence.

Falsified if: A well-powered allele-specific assay shows equal GATA3 occupancy or greater occupancy on C.; GATA3 perturbation has no allele-dependent effect on enhancer output or TOX3 expression.

### 4. H3: SPDEF-dependent enhancer effect on TOX3 (p = 0.03)

TF SPDEF (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851, a distal enhancer-like element overlapping rs4784227; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This hypothesis provisionally predicts that SPDEF binds alt T more strongly than ref C; SPDEF occupies the site and is expressed in MCF-7, but no supplied evidence measures allele-specific binding or provides a QBiC-SELEX result establishing this direction. | weak | [E04](#e04), [E07](#e07) |
| element | The variant lies in enhancer-like cCRE EH38E3180851, but allele-dependent activity or SPDEF dependence has not been demonstrated. | supported | [E01](#e01), [E03](#e03), [E07](#e07) |
| gene | TOX3 is the leading candidate target by proximity and genetic prioritization, but this cCRE has not been directly linked to TOX3; no significant GTEx eQTL is reported. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | SPDEF occupancy and expression make MCF-7 a plausible context for this proposed mechanism, although fewer MCF-7 peaks are reported than for FOXA1 or GATA3. | supported | [E07](#e07) |
| phenotype | Alt T is associated with breast cancer risk, and TOX3 has gene-level breast cancer support, but the evidence does not connect SPDEF binding at this element to TOX3 regulation or risk. | weak | [E15](#e15), [E16](#e16), [E21](#e21) |

Predictions: In allele-specific SPDEF occupancy assays in MCF-7, T should show greater occupancy than C; this is a proposed direction, not an observed result.; If SPDEF mediates the variant effect, SPDEF perturbation should reduce the allele-dependent enhancer or TOX3 response. The direction of the TOX3 response is not established by the supplied evidence.

Falsified if: A well-powered allele-specific assay shows equal SPDEF occupancy or greater occupancy on C.; SPDEF perturbation has no allele-dependent effect on enhancer output or TOX3 expression.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Measure allele-specific FOXA1, GATA3, and SPDEF occupancy at rs4784227 in MCF-7 (for example, targeted ChIP-qPCR or CUT&RUN with allele-aware readout). | medium | yes | No reproducible allele-specific occupancy for these candidate TFs. | FOXA1 occupancy is greater on C than T. | GATA3 occupancy is greater on T than C. | SPDEF occupancy is greater on T than C. |
| Perturb EH38E3180851 (for example, CRISPRi) in MCF-7 and measure TOX3 expression alongside enhancer activity. | medium | no | No reproducible enhancer-dependent change in TOX3 expression. | Perturbation changes enhancer activity and TOX3 expression; a FOXA1-dependent component is expected, but its direction is not established. | Perturbation changes enhancer activity and TOX3 expression; a GATA3-dependent component is expected, but its direction is not established. | Perturbation changes enhancer activity and TOX3 expression; a SPDEF-dependent component is expected, but its direction is not established. |
| Precisely edit C to T and T to C in an isogenic MCF-7 model; measure candidate-TF occupancy, enhancer output, and TOX3 expression. | high | no | The edit produces no reproducible TF-mediated change in occupancy, enhancer output, or TOX3 expression. | The edit changes FOXA1 occupancy in the predicted C-greater-than-T direction and produces an allele-dependent enhancer or TOX3 response. | The edit changes GATA3 occupancy in the predicted T-greater-than-C direction and produces an allele-dependent enhancer or TOX3 response. | The edit changes SPDEF occupancy in the predicted T-greater-than-C direction and produces an allele-dependent enhancer or TOX3 response. |

## Next experiment

The cheapest experiment that separates the two highest-probability chains is allele-specific FOXA1 and GATA3 occupancy measurement at rs4784227 in MCF-7 (targeted ChIP-qPCR or CUT&RUN with allele-aware readout). H1 predicts greater FOXA1 occupancy on C; H2 predicts greater GATA3 occupancy on T. Neither direction is established by current evidence.

## Investigate calls

- literature_search({"query": "rs4784227 allele-specific FOXA1 GATA3 SPDEF enhancer TOX3 breast cancer functional assay"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- gene_disease({"gene": "TOX3"})

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

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20AND%20TOX3%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:28+00:00)

> Europe PMC: 77 hits for 'rs4784227 AND TOX3 AND "breast cancer"'; top 8 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 40932605 (2025): Molecular signatures of breast cancer in the Iranian population: a review of cell growth and cell cycle regulators.
> PMID 42001218 (2026): Prioritizing context-specific genetic risk mechanisms in 11 solid cancers.
> PMID 36042591 (2022): Association between the rs4784227-CASC16 polymorphism and the risk of breast cancer: A meta-analysis.
> PMID 39777116 (2025): Identification of significant single-nucleotide polymorphisms associated with breast cancer recurrence and metastasis using GWAS.
> PMID 38741014 (2024): Genome-wide association analyses of breast cancer in women of African ancestry identify new susceptibility loci and improve risk prediction.
> PMID 39587695 (2024): The shared genetic landscape of polycystic ovary syndrome and breast cancer: convergence on ER + breast cancer but not ER- breast cancer.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-25T17:26:28+00:00)

> Key examples include promoter mutations [e.g., rs2279744 (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs4784227 (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> ObjectiveAlthough several studies have identified an association between the rs4784227-cancer susceptibility candidate gene 16 (CASC16) polymorphism and breast cancer, the results remain inconclusive.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> Our pooled analysis showed a significant association between the rs4784227- (T) allele and breast cancer susceptibility in Asian and North American populations, and intervention with this mutation might be a new therapeutic strategy for breast cancer.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20allele-specific%20FOXA1%20GATA3%20SPDEF%20enhancer%20TOX3%20breast%20cancer%20functional%20assay&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:20:17+00:00)

> Europe PMC: 1 hits for 'rs4784227 allele-specific FOXA1 GATA3 SPDEF enhancer TOX3 breast cancer functional assay'; top 1 with PMIDs:
> PMID 30116257 (2018): Elucidating the Underlying Functional Mechanisms of Breast Cancer Susceptibility Through Post-GWAS Analyses.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 30116257 (https://europepmc.org/article/MED/30116257; retrieved 2026-10-26T13:20:17+00:00)

> Despite these achievements, however, understanding of each variant's underlying mechanism and how these SNPs predispose women to breast cancer remains limited and represents a major challenge in the field, particularly since the vast majority of the GWAS-identified SNPs are located in non-coding regions of the genome and are merely tags for the causal variants.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 30116257 (https://europepmc.org/article/MED/30116257; retrieved 2026-10-26T13:20:17+00:00)

> In recent years, fine-scale mapping studies followed by functional evaluation of putative causal variants have begun to elucidate the biological function of several GWAS-identified variants.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e21"></a>**E21** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:34:32+00:00)

> Open Targets: TOX3 and breast cancer (MONDO_0007254), overall score 0.58; by evidence type: genetic_association 0.91, literature 0.89
