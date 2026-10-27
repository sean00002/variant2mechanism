# rs339331 and Prostate cancer (6q22)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 7 model calls; 148 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. null_linked_or_no_tf_effect: No TF-mediated effect at rs339331; linked causal variant or passenger signal (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: There is no allele-specific TF occupancy at rs339331 in the relevant prostate cancer cell type; the GWAS signal is driven by a linked causal variant or by RFX6 regulatory variation elsewhere.; The only covered ENCODE TF ChIP peak at the variant is PKNOX1 in HEK293T, not LNCaP, and PKNOX1 has no provided QBiC-SELEX model or LNCaP occupancy here.; The provided eQTL is for FAM162B in adipose, not RFX6 in prostate, and there is no GTEx prostate RFX6 eQTL for this variant.

Falsified if: Allele-specific TF ChIP or reporter assays in relevant prostate cancer cells show a clear TF-mediated allelic effect at rs339331.; A linked causal variant is excluded and rs339331 itself is shown to alter RFX6 expression in prostate cells.; The LNCaP-negative ENCODE result is shown to be irrelevant because a specific prostate tumor context has strong allele-specific occupancy.

### 2. GATA2_HOXB13_enhancer_RFX6: GATA2/HOXB13 complex binds the C allele at rs339331 and raises RFX6 (p = 0.33)

TF GATA2 (QBiC-SELEX coverage own_model), alt allele binds more; element rs339331/6q22 enhancer element within cCRE EH38E2496909; gene RFX6; cell type prostate cancer cells or tumors where a GATA2/SMAD4/HOXB13 complex acts.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | A GATA2-containing complex is reported at the rs339331/6q22 enhancer. I infer stronger binding on the C (alt) allele because C is the GWAS prostate cancer effect allele and the complex is reported to increase RFX6, but direct allele-specific GATA2 binding is absent; no QBiC-SELEX GATA2 model is provided and ENCODE has no GATA2 peak containing the variant. | weak | [E09d](#e09d), [E06](#e06), [E11](#e11), [E04](#e04) |
| element | rs339331 lies in a distal enhancer-like cCRE and is reported as a prostate cancer risk-associated enhancer bound by a GATA2/SMAD4/HOXB13 transcriptional complex. | supported | [E03](#e03), [E09d](#e09d) |
| gene | The GATA2/SMAD4/HOXB13 complex at this enhancer is reported to increase expression of the nearby susceptibility gene RFX6. | supported | [E09d](#e09d), [E02](#e02), [E07](#e07) |
| cell_type | The mechanism is proposed in prostate cancer cells or tumors, the disease context in which the GATA2/SMAD4/HOXB13 complex at rs339331 was described; LNCaP has no ENCODE ChIP peak at the variant, so cell-type specificity remains indirect. | weak | [E09d](#e09d), [E04](#e04) |
| phenotype | Increased RFX6 expression downstream of the 6q22 enhancer is proposed to contribute to prostate cancer risk; E06 supports C as the prostate cancer effect allele, but causality in prostate cells is not directly shown. | weak | [E06](#e06), [E09a](#e09a), [E09b](#e09b), [E09d](#e09d) |

Predictions: GATA2 and/or HOXB13 ChIP is stronger at rs339331 on the C allele in prostate cancer cells.; GATA2 or HOXB13 knockdown reduces enhancer activity and RFX6 expression.; The rs339331 enhancer depends on an intact GATA2/SMAD4/HOXB13 complex.

Falsified if: GATA2 or HOXB13 ChIP does not show allele-specific occupancy at rs339331 in prostate cancer cells or shows stronger binding on T rather than C.; Disrupting the GATA2/HOXB13/SMAD4 complex does not alter RFX6 expression from this enhancer.; The previously reported complex at 6q22 maps to a different linked variant and not rs339331.

### 3. AR_T_enhancer_RFX6: AR binds the T allele at the rs339331 enhancer and raises RFX6, with allele-direction conflict unresolved (p = 0.27)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element distal enhancer-like cCRE EH38E2496909 containing rs339331; gene RFX6; cell type prostate cancer tumor cells with reprogrammed AR occupancy; LNCaP has no ENCODE AR peak at this base.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR is proposed to bind the rs339331 sequence more strongly on the T (ref) allele, based on literature reporting T-allele-enhanced AR chromatin occupancy at a reprogrammed AR site. No QBiC-SELEX AR model is provided; ENCODE has no AR ChIP peak containing this variant and no LNCaP peak at this base, so AR occupancy here is literature-only and weak. | weak | [E09c](#e09c), [E10](#e10), [E04](#e04) |
| element | rs339331 lies in a distal enhancer-like cCRE, EH38E2496909, and is reported as part of a reprogrammed AR binding site in prostate cancer. | supported | [E03](#e03), [E09c](#e09c) |
| gene | RFX6 is the nearest protein-coding gene at 11.7 kb in the gene body and the top Open Targets L2G gene across prostate cancer credible sets, but no direct enhancer-to-RFX6 assay or prostate RFX6 eQTL is provided. | weak | [E02](#e02), [E07](#e07), [E09b](#e09b), [E12](#e12) |
| cell_type | The proposed context is prostate cancer tumor cells with reprogrammed AR occupancy, but this is not demonstrated in the case cell type LNCaP, where ENCODE reports 0 ChIP peaks at the variant. | weak | [E09c](#e09c), [E04](#e04) |
| phenotype | AR-dependent RFX6 regulation is proposed to affect prostate cancer risk or progression, but the allele direction is unresolved: E06 reports C as the prostate cancer effect allele, while E09c calls T the AR-occupancy risk allele. | weak | [E06](#e06), [E09a](#e09a), [E09b](#e09b), [E09c](#e09c) |

Predictions: Allele-specific AR ChIP is stronger at rs339331 on the T allele in AR-positive prostate cancer cells or tumors.; An rs339331 enhancer reporter shows higher AR-dependent activity for T than C.; AR loss-of-function reduces RFX6 expression in the relevant prostate cancer context.

Falsified if: Allele-specific AR ChIP or reporter assays show stronger AR binding or activity on the C allele rather than T at rs339331.; AR knockdown or deletion does not reduce RFX6 expression in relevant prostate cancer cells.; A linked causal variant is shown to explain the rs339331-T association with no AR occupancy at this base.

## Prediction matrix

| Test | Cost | Separates top two | null_linked_or_no_tf_effect | GATA2_HOXB13_enhancer_RFX6 | AR_T_enhancer_RFX6 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific AR ChIP-qPCR or ChIP-seq at rs339331 in LNCaP or AR-positive prostate cancer cells | medium | no | No allele-specific AR occupancy at rs339331. | No allele-specific AR occupancy expected. | Allele-specific AR occupancy, stronger on T at rs339331. |
| Allele-specific GATA2 or HOXB13 ChIP-qPCR or ChIP-seq at rs339331 in prostate cancer cells | medium | yes | No allele-specific GATA2/HOXB13 occupancy at rs339331. | Allele-specific GATA2 or HOXB13 occupancy, stronger on C at rs339331. | No allele-specific GATA2/HOXB13 occupancy expected. |
| Allele-specific rs339331 enhancer reporter in LNCaP or prostate cancer cells with AR versus GATA2/HOXB13 knockdown | medium | yes | No allele-dependent enhancer activity at rs339331. | C allele gives higher GATA2/HOXB13-dependent enhancer activity. | T allele gives higher AR-dependent enhancer activity. |
| RFX6 allele-specific expression or prostate tumor eQTL stratified by rs339331 genotype | low | yes | No allelic effect on RFX6 expression in prostate tissue or tumor cells. | C allele gives higher RFX6 expression. | An allelic RFX6 expression effect is expected, but the direction is unresolved because the AR/T literature conflicts with the GWAS C effect allele. |

## Next experiment

Cheapest experiment to separate the top two chains (GATA2_HOXB13_enhancer_RFX6 versus null_linked_or_no_tf_effect): genotype existing prostate tumor RNA-seq or targeted RFX6 expression data by rs339331 and test for an allele-specific RFX6 expression effect; a C-allele RFX6 increase supports the GATA2/HOXB13 chain, while no allelic RFX6 effect supports the null.

## Investigate calls

- chip_peaks({"biosample": null, "tf": "AR"})
- chip_peaks({"biosample": null, "tf": "GATA2"})
- eqtl_lookup({"tissue": "Prostate"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/6:116888889-116888889:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:00+00:00)

> Variant chr6:116888889:T>C (GRCh38), allele string T/C
> Known IDs: rs339331
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 1.28
> Transcript consequences: RFX6 (intron_variant); RFX6 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/6:115888889-117888889?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:26:06+00:00)

> 24 protein-coding genes within 1000 kb of chr6:116888889:T>C, by distance to TSS:
> RFX6: 11.7 kb from TSS (in gene body, strand +1)
> GPRC6A: 59.8 kb from TSS (upstream, strand -1)
> FAM162B: 123.1 kb from TSS (upstream, strand -1)
> KPNA5: 207.7 kb from TSS (downstream, strand +1)
> ZUP1: 220.1 kb from TSS (upstream, strand -1)
> RSPH4A: 272.4 kb from TSS (downstream, strand +1)
> RWDD1: 317.5 kb from TSS (downstream, strand +1)
> TRAPPC3L: 343.2 kb from TSS (upstream, strand -1)
> CALHM4: 359.9 kb from TSS (downstream, strand +1)
> VGLL2: 376.7 kb from TSS (upstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E2496909 (dELS: distal enhancer-like), chr6:116888741-116889057.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2496909 dELS (contains the variant): DNase z 2.2, H3K27ac z 1.7, H3K4me3 z 1.4, CTCF z 1.5; nearby genes RFX6, GPRC6A, FAM162B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr6:116888889:T>C: 6 peaks contain the variant, from 6 factors in 3 biosamples. In the matching biosample LNCaP clone FGC, LNCaP: 0 peaks from 0 factors. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): CTBP1, PRDM6, ZSCAN5C. Bound, expressed TFs with a binding model: 1; listed one per row: PKNOX1. Bound but below 1 TPM: FEZF1, MEIS2. Assayed with no peak here: 1 TFs in the matching biosample, 569 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> PKNOX1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HEK293T (e.g. ENCSR233FAG). 8.32 TPM in DepMap:ACH-000977 (LNCaP clone FGC), rank 573 of 1626 TFs.

<a id="e06"></a>**E06** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs339331&size=100; retrieved 2026-10-25T17:26:01+00:00)

> 13 GWAS Catalog associations for rs339331, strongest first:
> Prostate cancer: p 5.0e-20, effect allele C, risk-allele frequency 0.367114986, PMID 32514122
> Phospholipids in small HDL: p 2.0e-13, effect allele C, risk-allele frequency NR, PMID 41044249
> Total lipids in small HDL: p 2.0e-13, effect allele C, risk-allele frequency NR, PMID 41044249
> Concentration of small HDL particles: p 5.0e-12, effect allele C, risk-allele frequency NR, PMID 41044249
> Cholesterol in Small HDL: p 1.0e-11, effect allele C, risk-allele frequency NR, PMID 41044249
> Prostate-specific antigen levels: p 4.0e-09, effect allele T, risk-allele frequency NR, PMID 39930085

<a id="e07"></a>**E07** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:00+00:00)

> 95 credible sets contain 6_116888889_T_C: 94 GWAS, 1 molecular QTL.
> GWAS Cancer of prostate (PheCode 185): PIP 0.23; L2G RFX6 0.87, GPRC6A 0.05
> GWAS Prostate cancer: PIP 0.07; L2G RFX6 0.42, GPRC6A 0.12
> GWAS Prostate cancer: PIP 0.07; L2G RFX6 0.75, GPRC6A 0.06
> GWAS Prostate cancer: PIP 0.06; L2G RFX6 0.27, GPRC6A 0.16
> GWAS Prostate cancer: PIP 0.06; L2G RFX6 0.61
> GWAS Cancer of prostate (PheCode 185): PIP 0.06; L2G RFX6 0.75
> pqtl for SCG2 (UKB_PPP_EUR_SCG2_P13521_OID21400_v1): PIP 0.01
> Best L2G gene scores across these sets: RFX6 0.87, NUS1 0.55, GPRC6A 0.38, ROS1 0.11

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38. NES is the effect of the alt allele (C) relative to ref (T).
> FAM162B in Adipose_Subcutaneous: NES +0.14, p 3.2e-04

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20AND%20RFX6%20AND%20%22prostate%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:07+00:00)

> Europe PMC: 67 hits for 'rs339331 AND RFX6 AND "prostate cancer"'; top 7 with PMIDs:
> PMID 41422049 (2025): Multifaceted functions of transcription regulatory factor X6 (RFX6): from pancreatic development to cancer progression.
> PMID 38932472 (2024): An Inherited Allele Confers Prostate Cancer Progression and Drug Resistance via RFX6/HOXA10-Orchestrated TGFβ Signaling.
> PMID 40181298 (2025): Genetic associations of prostate cancer in China: a systematic review.
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 41374944 (2025): The Clinical Relevance of Tumor Biomarkers in Prostate Cancer-A Review.
> PMID 38052806 (2023): Prostate cancer genetic risk and associated aggressive disease in men of African ancestry.
> PMID 41432001 (2026): Insights into human history and complex traits from the genomes of African populations.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 41422049 (https://europepmc.org/article/MED/41422049; retrieved 2026-10-25T17:26:07+00:00)

> Dysregulated expression or mutations of the RFX6 gene in prostate cancer, hepatocellular carcinoma, gastric cancer, melanoma, and other tumors have garnered significant interest, with studies showing that such alterations affect tumor cell proliferation, migration, and invasion, and are correlated with an unfavorable clinical prognosis in patients carrying RFX6 mutations.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-25T17:26:07+00:00)

> Here the FinnGen cohort phenome-wide analysis, along with multiple genome-wide association studies, has consistently identified the rs339331-RFX6/6q22 locus associated with prostate cancer (PCa) risk across diverse populations.

<a id="e09c"></a>**E09c** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-25T17:26:07+00:00)

> It is uncovered that rs339331 resides in a reprogrammed androgen receptor (AR) binding site in PCa tumors, with the T risk allele enhancing AR chromatin occupancy.

<a id="e09d"></a>**E09d** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-25T17:26:07+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs339331/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.

<a id="e09e"></a>**E09e** literature_search, Europe PMC abstract, PMID 38052806 (https://europepmc.org/article/MED/38052806; retrieved 2026-10-25T17:26:07+00:00)

> Notable genes of interest include HCP5, RFX6 and H3C1 for risk, and MKI67 and KLF5 for aggressive disease.

<a id="e10"></a>**E10** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:23+00:00)

> No ENCODE AR ChIP-seq peak contains chr6:116888889:T>C. Absence can also mean no AR experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e11"></a>**E11** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:26:35+00:00)

> No ENCODE GATA2 ChIP-seq peak contains chr6:116888889:T>C. Absence can also mean no GATA2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e12"></a>**E12** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).
