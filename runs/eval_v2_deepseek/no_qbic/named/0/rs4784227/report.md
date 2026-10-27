# rs4784227 and Breast cancer (16q12)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 254 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H1_FOXA1_alt: FOXA1-bound enhancer: alt T increases FOXA1 binding and TOX3 expression (p = 0.45)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR16_9QTBS / EH38E3180851 dELS; gene TOX3; cell type MCF-7 / ER-positive luminal breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies this element in MCF-7 (E05); the alt T allele is predicted to bind FOXA1 more strongly than ref C. FOXA1 is selected because it is a pioneer TF with MCF-7 ChIP peaks containing the variant (E05), high MCF-7 expression (E05), the variant lies in a dELS (E03), and E19 includes PMID 23001124 reporting that breast cancer risk SNPs modulate FOXA1 chromatin affinity and gene expression. No QBiC-SELEX model for FOXA1 is supplied, and the exact allele direction at this base is not measured in the provided evidence; bulk ChIP cannot prove allelic imbalance. | weak | [E05](#e05), [E03](#e03), [E19](#e19) |
| element | The variant lies in ENSR16_9QTBS and in cCRE EH38E3180851, a distal enhancer-like element, and FOXA1 ChIP peaks containing the variant place FOXA1 at this element in MCF-7; this supports a FOXA1-bound distal enhancer-like element in the relevant cell type, though the cCRE z-scores are maxima across biosamples. | supported | [E01](#e01), [E03](#e03), [E05](#e05) |
| gene | TOX3 is the best-nominated target because it is the nearest protein-coding gene at 17.5 kb upstream (E02), Open Targets L2G gives TOX3 the top score in breast cancer credible sets (E16), and E18a links rs4784227/TOX3 as an enhancer example; however, direct regulatory linkage is not established because GTEx v8 shows no significant single-tissue or breast eQTL for this exact variant (E17, E20), and TOX3 is not essential in MCF7 or breast lineage lines by DepMap (E21), so this is target nomination rather than demonstrated rs4784227-to-TOX3 regulation. | weak | [E02](#e02), [E16](#e16), [E18a](#e18a), [E17](#e17), [E20](#e20), [E21](#e21) |
| cell_type | MCF-7 is a relevant ER-positive luminal breast cancer context: FOXA1 ChIP-seq is present in MCF-7 at this element (E05), FOXA1 is highly expressed there (E05), the expression context is DepMap:ACH-000019 (MCF7), and the GWAS signal is strong for breast cancer including ER-positive disease (E15, E16). | supported | [E05](#e05), [E15](#e15), [E16](#e16) |
| phenotype | The alt T allele is the breast cancer risk allele in the strongest GWAS and meta-analysis evidence (T vs C OR about 1.24; E15, E18b), and one E15 entry reports effect allele C, likely reflecting effect-allele coding inconsistency rather than contradicting the T-risk direction. If alt T increases FOXA1-bound enhancer activity and TOX3 expression, this would be expected to raise risk, especially ER-positive breast cancer, but the causal steps from FOXA1 binding to TOX3 expression to disease are inferential, and TOX3 perturbation does not affect MCF7 fitness in DepMap (E21). | supported | [E15](#e15), [E18b](#e18b), [E16](#e16), [E21](#e21) |

Predictions: Allele-specific FOXA1 binding assays show alt T > ref C at this base.; An enhancer reporter carrying alt T has higher activity than ref C in MCF-7 cells.; TOX3 expression is higher with the T allele in an appropriate ER-positive breast context.; FOXA1 knockdown or CRISPRi reduces TOX3 expression in MCF-7 cells.; CRISPRi or deletion of this dELS lowers TOX3 expression in MCF-7 cells.

Falsified if: FOXA1 binding is not allele-specific at this base.; Ref C binds FOXA1 more strongly than alt T.; The T allele does not change TOX3 expression or enhancer activity.; Direct perturbation of the element does not affect TOX3.

### 2. H5_null: Null: no TF-mediated allelic effect of rs4784227 itself (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: rs4784227 is a marker in linkage disequilibrium with the true causal variant rather than the causal base.; No allele-specific TF binding difference is detectable at chr16:52565276 in relevant breast cells.; The GWAS signal is explained by another variant in the TOX3/CASC16 enhancer region or by a non-TF-mediated mechanism.; GTEx v8 shows no significant single-tissue or breast eQTL for this exact variant (E17, E20), consistent with the variant not being the direct regulatory base.; TOX3 is not essential in MCF7 or breast lineage lines by DepMap (E21), so the disease mechanism may not require a strong TOX3 expression change.

Falsified if: Allele-specific FOXA1 or GATA3 binding is demonstrated at this exact base.; A reporter or CRISPR edit shows that rs4784227 itself changes enhancer activity.; The T allele changes TOX3 expression in an allele-specific manner in a relevant breast cell context.

### 3. H2_GATA3_alt: GATA3-bound enhancer: alt T increases GATA3 binding and TOX3 expression (p = 0.15)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR16_9QTBS / EH38E3180851 dELS; gene TOX3; cell type MCF-7 / ER-positive luminal breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 occupies this element in MCF-7 (E06); the alt T allele is predicted to bind GATA3 more strongly than ref C. GATA3 is extremely highly expressed in MCF-7 (rank 5 of 1626 TFs; E06) and has MCF-7 ChIP peaks containing the variant, but E04 shows many other bound, expressed TFs and no QBiC-SELEX or allele-specific binding data for GATA3 are supplied, so the allelic direction is a hypothesis rather than a measured effect. | weak | [E06](#e06), [E04](#e04) |
| element | The variant lies in the dELS EH38E3180851 (E03), and GATA3 ChIP peaks containing the variant place GATA3 at this enhancer-like element in MCF-7 (E06). | supported | [E03](#e03), [E06](#e06) |
| gene | TOX3 is the best-nominated target because it is the nearest protein-coding gene at 17.5 kb upstream (E02), Open Targets L2G gives TOX3 the top score in breast cancer credible sets (E16), and E18a links rs4784227/TOX3 as an enhancer example; however, direct regulatory linkage is not established because GTEx v8 shows no significant single-tissue or breast eQTL for this exact variant (E17, E20), and TOX3 is not essential in MCF7 or breast lineage lines by DepMap (E21), so this is target nomination rather than demonstrated rs4784227-to-TOX3 regulation. | weak | [E02](#e02), [E16](#e16), [E18a](#e18a), [E17](#e17), [E20](#e20), [E21](#e21) |
| cell_type | MCF-7 is a relevant ER-positive luminal breast cancer context: GATA3 is very highly expressed and bound at this element in MCF-7 (E06), and the GWAS signal is strong for breast cancer including ER-positive disease (E15, E16). | supported | [E06](#e06), [E15](#e15), [E16](#e16) |
| phenotype | The alt T allele is associated with increased breast cancer risk (E15, E18b); if alt T increases GATA3-bound enhancer activity and TOX3 expression, this could increase risk in ER-positive breast cancer, but whether GATA3 binding at this element increases TOX3 and whether that changes risk is not directly shown, and TOX3 perturbation does not affect MCF7 fitness in DepMap (E21). | supported | [E15](#e15), [E18b](#e18b), [E16](#e16), [E21](#e21) |

Predictions: Allele-specific GATA3 binding shows alt T > ref C at this element.; An enhancer reporter carrying alt T is more active in a GATA3-dependent breast cancer cell line.; GATA3 knockdown reduces TOX3 expression in MCF-7 cells.; GATA3 ChIP signal at this element correlates with TOX3 expression across ER-positive models.

Falsified if: GATA3 binding is not allele-specific at this base.; Ref C binds GATA3 more strongly than alt T.; GATA3 knockdown does not affect TOX3 expression.; The element's activity is FOXA1-dependent but GATA3-independent.

## Prediction matrix

| Test | Cost | Separates top two | H1_FOXA1_alt | H5_null | H2_GATA3_alt |
| --- | --- | --- | --- | --- | --- |
| Allele-specific FOXA1 binding at chr16:52565276 (ChIP-qPCR/ChIP-seq or EMSA) in MCF-7 or heterozygous breast cells | medium | yes | alt T > ref C FOXA1 occupancy | no FOXA1 allelic difference | no FOXA1 allelic difference expected; GATA3 is the proposed TF |
| Transient enhancer reporter with ref C vs alt T in MCF-7 cells | low | yes | alt T reporter activity higher than ref C | no allelic difference in reporter activity | alt T may also increase activity if GATA3 is causal; this test alone does not distinguish H1 from H2 |
| Allele-specific GATA3 binding at chr16:52565276 in MCF-7 or heterozygous breast cells | medium | no | no GATA3 allelic difference expected | no GATA3 allelic difference | alt T > ref C GATA3 occupancy |
| FOXA1 knockdown or CRISPRi in MCF-7, measuring TOX3 expression | medium | yes | TOX3 expression decreases | no TOX3 decrease | no or minimal TOX3 decrease |
| CRISPRi or deletion of the EH38E3180851 dELS in MCF-7, measuring TOX3 expression | high | yes | TOX3 expression decreases | no change in TOX3 expression | TOX3 expression decreases |
| Allele-specific TOX3 expression or breast-tissue eQTL for rs4784227 in heterozygous relevant tissue | high | yes | T allele associates with higher TOX3 expression | no allele-specific TOX3 expression difference | T allele associates with higher TOX3 expression |

## Next experiment

The cheapest experiment separating the top two chains (H1_FOXA1_alt vs H5_null) is a transient enhancer reporter in MCF-7 comparing ref C and alt T at chr16:52565276: H1 predicts higher activity for alt T, while H5 predicts no allelic difference.

## Investigate calls

- literature_search({"query": "rs4784227 allele-specific FOXA1 TOX3 enhancer reporter"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- gene_dependency({"gene": "TOX3"})

## Flags

- quote_rejected: PMID 23001124: not an exact substring of the abstract

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

> The pooled ORs regarding the association between the rs4784227-CASC16 polymorphism and breast cancer risk were statistically significant [T vs C: OR = 1.244, 95% CI = 1.202-1.287; TT vs CT + CC: OR = 1.407, 95% CI = 1.296-1.528; CC vs CT + TT: OR = 0.777, 95% CI = 0.745-0.811; TT vs CC: OR = 1.544, 95% CI = 1.419-1.681; CT vs CC: OR = 1.244, 95% CI = 1.189-1.301].

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> Our pooled analysis showed a significant association between the rs4784227- (T) allele and breast cancer susceptibility in Asian and North American populations, and intervention with this mutation might be a new therapeutic strategy for breast cancer.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20allele-specific%20FOXA1%20TOX3%20enhancer%20reporter&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:26:05+00:00)

> Europe PMC: 8 hits for 'rs4784227 allele-specific FOXA1 TOX3 enhancer reporter'; top 8 with PMIDs:
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 35011637 (2021): Three-Dimensional Genome Organization in Breast and Gynecological Cancers: How Chromatin Folding Influences Tumorigenic Transcriptional Programs.
> PMID 30116257 (2018): Elucidating the Underlying Functional Mechanisms of Breast Cancer Susceptibility Through Post-GWAS Analyses.
> PMID 23001124 (2012): Breast cancer risk-associated SNPs modulate the affinity of chromatin for FOXA1 and alter gene expression.
> PMID 27807102 (2016): Emergence of the Noncoding Cancer Genome: A Target of Genetic and Epigenetic Alterations.
> PMID 29215763 (2018): Breast cancer: The translation of big genomic data to cancer precision medicine.
> PMID 25976354 (2015): Human Enhancers Are Fragile and Prone to Deactivating Mutations.
> PMID 25288875 (2014): Functional annotation of putative regulatory elements at cancer susceptibility Loci.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e21"></a>**E21** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for TOX3 (0 = no effect, -1 = median common-essential; < -0.5 called dependent). MCF7 (ACH-000019): 0.11. Breast lineage, 53 lines: median 0.04, 0% dependent. All 1183 lines: median 0.05, 0% dependent.
