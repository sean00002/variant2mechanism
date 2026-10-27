# rs4784227 and Breast cancer (16q12)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 228 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GATA3 (bound here, z 18.65); FOXA1 (bound here, z 15.4); NR2F2 (bound here, z 9.51); TCF7L2 (bound here, z 8.45); SPDEF (bound here, z 5.89); MAFK (bound elsewhere, z 71.57); HOMEZ (bound elsewhere, z -49.09); MNX1 (bound elsewhere, z -27.02); PITX1 (bound elsewhere, z -21.39); TFAP4 (bound elsewhere, z 19.55). Occupancy unknown: MAFA (z 71.57); MAFB (z 71.57); LHX2 (z 28.05); LHX4 (z 28.05); LMX1B (z 28.05). Diagnostic, not shown to the model: 290 of 997 models pass Bonferroni.

## Ranked chains

### 1. chain_GATA3: GATA3 binds the T risk allele more strongly at the same TOX3 enhancer (p = 0.37)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element dELS enhancer EH38E3180851; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is predicted to bind the alt T allele more strongly than the ref C allele. GATA3 has its own QBiC-SELEX model at this base with a positive alt-allele effect (effect 0.783, z 10.91), and GATA3 has ENCODE ChIP-seq occupancy over the variant in MCF7 and is very highly expressed there. The QBiC-SELEX effect is in vitro and the ChIP evidence is peak-level, not allele-specific at this base. | supported | [E36](#e36), [E06](#e06), [E04](#e04) |
| element | The variant lies in EH38E3180851, a distal enhancer-like cCRE with active chromatin and cofactor occupancy, consistent with a GATA3-occupied regulatory element. The E03 chromatin z-scores are maxima across ENCODE biosamples, not MCF7-specific. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | TOX3 is the nearest protein-coding gene at 17.5 kb and the best L2G gene in breast cancer credible sets. No significant GTEx v8 eQTL is reported for this SNP, so the enhancer-to-TOX3 assignment is indirect. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E18a](#e18a) |
| cell_type | GATA3 is very highly expressed in MCF7 and has MCF7 ChIP-seq peaks containing this variant, matching the breast luminal cell context. | supported | [E06](#e06), [E04](#e04) |
| phenotype | The alt T allele is the risk allele in strong breast cancer GWAS and in a meta-analysis, giving a disease direction in which T increases risk. One E15 maternal breast-cancer entry uses effect allele C and would need harmonization. | supported | [E15](#e15), [E18b](#e18b) |

Predictions: Allele-specific GATA3 ChIP or footprinting at this base in MCF7 or another C/T heterozygous breast cancer line should show stronger GATA3 occupancy on T than C.; In an enhancer reporter in MCF7, the T-vs-C activity difference should be sensitive to mutation of the GATA3 motif if GATA3 mediates the effect; activity direction could be activation or repression.; If GATA3 acts through this element, CRISPR allele swap from C to T should change TOX3 expression or enhancer activity in a GATA3-dependent way.

Falsified if: GATA3 ChIP or footprinting is not allele-specific at this base in breast cancer cells.; The T-vs-C enhancer activity difference remains after GATA3 motif mutation or GATA3 depletion.; The GATA3 ChIP peak over the variant is not resolved to the variant base or is not seen in breast contexts.

### 2. chain_FOXA1: FOXA1 binds the T risk allele more strongly at a TOX3 enhancer (p = 0.33)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element dELS enhancer EH38E3180851; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is predicted to bind the alt T allele more strongly than the ref C allele. FOXA1 has its own QBiC-SELEX model at this base with a positive alt-allele effect (effect 0.314, z 9.34), and FOXA1 has ENCODE ChIP-seq occupancy over the variant in MCF7 and is highly expressed there. This is still a motif-plus-occupancy prediction, not allele-specific occupancy measured at this base. | supported | [E35](#e35), [E05](#e05), [E04](#e04) |
| element | The variant lies in EH38E3180851, a distal enhancer-like cCRE with DNase, H3K27ac and active-element cofactor ChIP signal, so it is a plausible regulatory element rather than a coding change. The E03 chromatin z-scores are maxima across ENCODE biosamples, not MCF7-specific. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | TOX3 is the nearest protein-coding gene at 17.5 kb and is the best L2G gene in breast cancer credible sets. There is no significant GTEx v8 eQTL for this SNP, so the enhancer-to-TOX3 link rests on proximity, L2G and literature, not a direct expression QTL. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E18a](#e18a) |
| cell_type | MCF7 is a relevant breast cancer context: FOXA1 is highly expressed in DepMap MCF7 and FOXA1 ChIP-seq peaks in MCF7 contain this variant. | supported | [E05](#e05), [E04](#e04) |
| phenotype | The alt T allele is the risk allele in the strongest breast cancer GWAS associations and in a meta-analysis, giving a disease direction in which T increases risk. One E15 maternal breast-cancer entry uses effect allele C and would need harmonization. | supported | [E15](#e15), [E18b](#e18b) |

Predictions: Allele-specific FOXA1 ChIP or footprinting at this base in MCF7 or another C/T heterozygous breast cancer line should show stronger FOXA1 occupancy on T than C.; In an enhancer reporter in MCF7, the T-vs-C activity difference should be sensitive to mutation of the FOXA1 motif if FOXA1 mediates the effect; activity direction could be activation or repression.; If FOXA1 acts through this element, CRISPR allele swap from C to T should change TOX3 expression or enhancer activity in a FOXA1-dependent way.

Falsified if: FOXA1 ChIP or footprinting is not allele-specific at this base in breast cancer cells.; The T-vs-C enhancer activity difference remains after FOXA1 motif mutation or FOXA1 depletion.; Allele-specific FOXA1 binding is seen only outside breast contexts and not in MCF7 or breast tumors.

### 3. null_no_TF_mediated_effect: No TF-mediated allelic effect at this base (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: There is no allele-specific occupancy or activity at this exact base for FOXA1, GATA3 or other candidate TFs.; The breast cancer association is explained by a linked causal variant in the same credible set or by haplotype effects rather than by rs4784227 itself.; CRISPR allele swap at rs4784227 alone should not change TOX3 expression or enhancer activity in MCF7.

Falsified if: Allele-specific TF binding and enhancer activity are demonstrated at this base in breast cells.; CRISPR editing of rs4784227 alone changes TOX3 expression or a breast cancer-relevant phenotype.; The variant is shown to be the causal base within the credible set rather than a passenger or linked marker.

## Prediction matrix

| Test | Cost | Separates top two | chain_GATA3 | chain_FOXA1 | null_no_TF_mediated_effect |
| --- | --- | --- | --- | --- | --- |
| Allele-specific ChIP-qPCR for FOXA1 and GATA3 at rs4784227 in a C/T heterozygous breast cancer line (or MCF7 if heterozygous), reporting T/C allelic ratios. | low | yes | GATA3 shows a T>C allelic occupancy skew at this base; FOXA1 is not required to show one. | FOXA1 shows a T>C allelic occupancy skew at this base; GATA3 is not required to show one. | Neither FOXA1 nor GATA3 shows allele-specific occupancy at this base. |
| Enhancer reporter or MPRA of the EH38E3180851 element with C vs T alleles, comparing wild-type sequence to separate FOXA1-motif and GATA3-motif mutations in MCF7. | medium | yes | T-vs-C activity difference is lost or strongly reduced by GATA3-motif mutation, but not by FOXA1-motif mutation. | T-vs-C activity difference is lost or strongly reduced by FOXA1-motif mutation, but not by GATA3-motif mutation. | No reproducible T-vs-C activity difference, or any difference is not attributable to either motif. |
| CRISPR C>T allele swap at rs4784227 in MCF7 followed by TOX3 expression and enhancer-activity measurement. | high | no | Allele swap changes TOX3 expression or enhancer activity, with GATA3 dependence if GATA3 is perturbed. | Allele swap changes TOX3 expression or enhancer activity, with FOXA1 dependence if FOXA1 is perturbed. | No change in TOX3 expression or enhancer activity after editing rs4784227 alone. |

## Next experiment

Allele-specific ChIP-qPCR for FOXA1 and GATA3 at rs4784227 in a C/T heterozygous breast cancer cell line, reporting T/C allelic ratios, is the cheapest single experiment that separates the top two chains.

## Investigate calls

- qbic_tf_detail({"tf": "FOXA1"})
- qbic_tf_detail({"tf": "GATA3"})
- qbic_tf_detail({"tf": "SPDEF"})

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

> The pooled ORs regarding the association between the rs4784227-CASC16 polymorphism and breast cancer risk were statistically significant [T vs C: OR = 1.244, 95% CI = 1.202-1.287; TT vs CT + CC: OR = 1.407, 95% CI = 1.296-1.528; CC vs CT + TT: OR = 0.777, 95% CI = 0.745-0.811; TT vs CC: OR = 1.544, 95% CI = 1.419-1.681; CT vs CC: OR = 1.244, 95% CI = 1.189-1.301].

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> Our pooled analysis showed a significant association between the rs4784227- (T) allele and breast cancer susceptibility in Asian and North American populations, and intervention with this mutation might be a new therapeutic strategy for breast cancer.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:52565276:C>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000019), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 95 occupied, 5 of 75 with unknown occupancy. Left out: 45 TFs assayed in the matching biosample and 411 assayed only elsewhere, none with a peak here; 22 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (a CIS-BP-mapped model of GATA2), z 18.65, effect 0.283: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 346.04 TPM, rank 5 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWV. Best model's site strength: ref 92.3th, alt 98.6th percentile of its k-mer coefficients.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXA1 (Forkhead, 4 models; QBiC-SELEX coverage: own model): best model FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer (a CIS-BP-mapped model of FOXA2), z 15.4, effect 0.296: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 88.38 TPM, rank 28 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR126YEB. Best model's site strength: ref 91.3th, alt 98.8th percentile of its k-mer coefficients.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model PPARG_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of PPARG), z 9.51, effect 0.22: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 38.14 TPM, rank 103 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000BUY. Best model's site strength: ref 95.4th, alt 97.7th percentile of its k-mer coefficients.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer (a CIS-BP-mapped model of TCF7), z 8.45, effect 0.455: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.89 TPM, rank 642 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWT. Best model's site strength: ref 81.2th, alt 97.6th percentile of its k-mer coefficients.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SPDEF (Ets, 18 models; QBiC-SELEX coverage: own model): best model ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer (a CIS-BP-mapped model of ELF1), z 5.89, effect 0.213: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 72.51 TPM, rank 40 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR042GSX. Best model's site strength: ref 79.2th, alt 76.3th percentile of its k-mer coefficients.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAFK (bZIP, 6 models; QBiC-SELEX coverage: own model): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (a CIS-BP-mapped model of MAFG), z 71.57, effect 2.788: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 16.96 TPM, rank 253 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000EEB. Best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOMEZ (Homeodomain, 1 model; QBiC-SELEX coverage: own model): best model HOMEZ_NA_TCGATC20NTAT_ESY_yang2017_0_3_7mer (its own model), z -49.09, effect -2.698: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR117CHD. Best model's site strength: ref 99.4th, alt 89.9th percentile of its k-mer coefficients.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MNX1 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model BARHL2_NA_TATTGT20NGTG_ESAC_yang2017_0_2_7mer (a CIS-BP-mapped model of BARHL2), z -27.02, effect -0.936: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.78 TPM, rank 791 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR108MKR. Best model's site strength: ref 99.9th, alt 95.5th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PITX1 (Homeodomain, 11 models; QBiC-SELEX coverage: own model): best model TPRX1_DBD_TG40NGACCTT_YWCB_jolma2025_0_2_7mer (a CIS-BP-mapped model of TPRX1), z -21.39, effect -0.283: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.1 TPM, rank 702 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR374MAS. Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP4 (bHLH, 1 model; QBiC-SELEX coverage: own model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (its own model), z 19.55, effect 1.433: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.85 TPM, rank 542 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR103SZL. Best model's site strength: ref 83.4th, alt 100.0th percentile of its k-mer coefficients.

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

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"FOXA1","symbol":"FOXA1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565276:C>T","gate_p":5.02e-05,"models":[{"model":"FOXA1_FL_TCCCAT40NTGT_KX_yin2017_0_4_7mer","mapping":"own","group":"G022 Forkhead, 4 models","quality":0.775,"effect":0.314,"z":9.34,"p":9.6e-21,"rank_abs_z":"82/997","passed_gate":true,"site_strength":{"ref_percentile":99.0,"alt_percentile":99.8,"k":7}},{"model":"FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer","mapping":"CIS-BP (FOXA2)","group":"G022 Forkhead, 4 models","quality":0.83,"effect":0.296,"z":15.4,"p":1.6e-53,"rank_abs_z":"37/997","passed_gate":true,"site_strength":{"ref_percentile":91.3,"alt_percentile":98.8,"k":7}},{"model":"FOXA3_FL_TGTGGT40NGGC_KX_yin2017_0_3_7mer","mapping":"CIS-BP (FOXA3)","group":"G022 Forkhead, 4 models","quality":0.928,"effect":0.144,"z":1.85,"p":0.065,"rank_abs_z":"569/997","passed_gate":false,"site_strength":{"ref_percentile":79.5,"alt_percentile":98.7,"k":7}},{"model":"FOXB1_NA_TGAGCA30NCGA_ESAI_yang2017_0_4_7mer","mapping":"CIS-BP (FOXB1)","group":"G022 Forkhead, 4 models","quality":0.674,"effect":0.045,"z":0.7,"p":0.49,"rank_abs_z":"814/997","passed_gate":false,"site_strength":{"ref_percentile":72.5,"alt_percentile":94.6,"k":7}}]}

<a id="e36"></a>**E36** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GATA3","symbol":"GATA3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565276:C>T","gate_p":5.02e-05,"models":[{"model":"GATA3_NA_TGTCGT20NGA_ESAC_yang2017_0_4_7mer","mapping":"own","group":"G010 GATA, 6 models","quality":0.858,"effect":0.783,"z":10.91,"p":1.1e-27,"rank_abs_z":"65/997","passed_gate":true,"site_strength":{"ref_percentile":83.3,"alt_percentile":98.0,"k":7}},{"model":"GATA1_eDBD_TTTAGA40NGGC_KN_yin2017_0_4_7mer","mapping":"CIS-BP (GATA1)","group":"G010 GATA, 6 models","quality":0.626,"effect":1.507,"z":12.45,"p":1.3e-35,"rank_abs_z":"57/997","passed_gate":true,"site_strength":{"ref_percentile":95.2,"alt_percentile":98.2,"k":7}},{"model":"GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer","mapping":"CIS-BP (GATA2)","group":"G010 GATA, 6 models","quality":0.874,"effect":0.283,"z":18.65,"p":1.3e-77,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":92.3,"alt_percentile":98.6,"k":7}},{"model":"GATA4_NA_TAAAAT20NAAA_Y_jolma2013_0_3_7mer","mapping":"CIS-BP (GATA4)","group":"G010 GATA, 6 models","quality":0.789,"effect":0.772,"z":8.04,"p":9.1e-16,"rank_abs_z":"116/997","passed_gate":true,"site_strength":{"ref_percentile":92.0,"alt_percentile":97.4,"k":7}},{"model":"GATA5_NA_TAAATG20NTAA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (GATA5)","group":"G010 GATA, 6 models","quality":0.882,"effect":0.733,"z":7.92,"p":2.3e-15,"rank_abs_z":"117/997","passed_gate":true,"site_strength":{"ref_percentile":99.5,"alt_percentile":99.4,"k":7}},{"model":"GATA6_eDBD_TCCATC40NTGA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (GATA6)","group":"G010 GATA, 6 models","quality":0.937,"effect":0.764,"z":14.98,"p":1e-50,"rank_abs_z":"40/997","passed_gate":true,"site_strength":{"ref_percentile":97.4,"alt_percentile":98.7,"k":7}}]}

<a id="e37"></a>**E37** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"SPDEF","symbol":"SPDEF","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565276:C>T","gate_p":5.02e-05,"models":[{"model":"SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer","mapping":"own","group":"G345 Ets, 1 model","quality":0.736,"effect":0.096,"z":2.03,"p":0.042,"rank_abs_z":"538/997","passed_gate":false,"site_strength":{"ref_percentile":69.2,"alt_percentile":95.0,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":0.213,"z":5.89,"p":3.8e-09,"rank_abs_z":"181/997","passed_gate":true,"site_strength":{"ref_percentile":79.2,"alt_percentile":76.3,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":0.568,"z":4.39,"p":1.1e-05,"rank_abs_z":"267/997","passed_gate":true,"site_strength":{"ref_percentile":72.2,"alt_percentile":92.2,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":0.062,"z":0.64,"p":0.52,"rank_abs_z":"827/997","passed_gate":false,"site_strength":{"ref_percentile":84.2,"alt_percentile":69.2,"k":7}}]}
