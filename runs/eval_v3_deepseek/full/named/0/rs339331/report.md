# rs339331 and Prostate cancer (6q22)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 8 model calls; 261 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: PKNOX1 (bound elsewhere, z 11.43, weak site). Occupancy unknown: HOXC13 (z -103.49); HOXA6 (z -84.28); HOXB9 (z -84.28); HOXC12 (z -84.28); HOXC6 (z -84.28). Diagnostic, not shown to the model: 487 of 997 models pass Bonferroni.

## Ranked chains

### 1. H2_HOXB13: HOXB13 binds the T allele at the rs339331 enhancer and modulates RFX6 in prostate cells (p = 0.38)

TF HOXB13 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2496909 dELS; gene RFX6; cell type prostate cancer (LNCaP clone FGC and PCa tumors).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 has its own QBiC-SELEX model, and the ref T allele binds more strongly (effect -4.771, z -103.49; ref site 99.9th vs alt 97.2nd percentile). E09d places a HOXB13-containing GATA2/SMAD4 complex at the rs339331 enhancer, but base-level allele-specific HOXB13 occupancy is not directly shown. | weak | [E17](#e17), [E09d](#e09d) |
| element | rs339331 lies in dELS EH38E2496909, and E09d reports a HOXB13/GATA2/SMAD4 complex at this 6q22 enhancer. | supported | [E03](#e03), [E09d](#e09d) |
| gene | The HOXB13-containing complex at this enhancer is reported to increase RFX6 expression; RFX6 is also the nearest protein-coding gene and the top L2G gene at the locus. | supported | [E09d](#e09d), [E02](#e02), [E07](#e07) |
| cell_type | The proposed mechanism is in prostate cancer cells/tumors, where HOXB13 is a lineage factor; the case expression context is LNCaP clone FGC. | weak | [E09d](#e09d), [E09b](#e09b) |
| phenotype | rs339331 is strongly associated with prostate cancer and the rs339331-RFX6/6q22 locus is implicated in PCa risk/progression, but the allelic direction is unresolved: E06 reports C as the effect allele, while this chain's QBiC prediction is that T binds HOXB13 more. | weak | [E06](#e06), [E09b](#e09b), [E09d](#e09d) |

Predictions: Allele-specific HOXB13 ChIP or footprinting in prostate cancer cells shows more HOXB13 on the T allele than the C allele at rs339331.; RFX6 expression or enhancer activity is higher with the T allele and is reduced by HOXB13 loss in this context.; A T-vs-C reporter assay at the rs339331 enhancer shows allele-specific activity that depends on the HOXB13 site.

Falsified if: HOXB13 does not occupy rs339331 in prostate cancer cells.; The C allele, not T, shows higher HOXB13 occupancy at this base.; HOXB13 loss does not change RFX6 expression or enhancer activity at this element.

### 2. H4_null: No TF-mediated allelic effect at rs339331 (p = 0.32)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy is found at the rs339331 base itself in prostate cancer cells.; Any prostate cancer signal at 6q22 is driven by a linked causal variant or by RFX6 regulation elsewhere, not by this base.; RFX6 expression is not allele-specific at rs339331 after controlling for linked variants.

Falsified if: Allele-specific HOXB13 or AR occupancy at rs339331 is demonstrated in prostate cancer cells.; RFX6 expression or enhancer activity is shown to track the rs339331 allele in prostate cancer cells.; A linked variant is excluded and this base alone changes TF binding and RFX6 function.

### 3. H1_AR: AR binds the T allele at rs339331 and increases RFX6 in prostate cancer (p = 0.22)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2496909 dELS; gene RFX6; cell type prostate cancer / LNCaP clone FGC.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Literature reports rs339331 in a reprogrammed AR binding site and the T allele enhancing AR occupancy (E09c), but AR has no QBiC-SELEX model in the provided evidence, and E04/E18 find no LNCaP AR ChIP peak over the variant. AR occupancy in LNCaP is therefore not established. | weak | [E09c](#e09c), [E04](#e04), [E18](#e18) |
| element | rs339331 lies in dELS EH38E2496909, and E09c places rs339331 in a reprogrammed AR binding site in prostate cancer tumors. | supported | [E03](#e03), [E09c](#e09c) |
| gene | RFX6 is the nearest protein-coding gene and the top L2G gene at the locus, and E09b names the rs339331-RFX6/6q22 locus. | weak | [E02](#e02), [E07](#e07), [E09b](#e09b) |
| cell_type | The AR mechanism is proposed in prostate cancer tumors, not specifically in LNCaP clone FGC; E04 reports 0 LNCaP ChIP peaks over the variant. | weak | [E09c](#e09c), [E04](#e04) |
| phenotype | The prostate cancer association is strong, but the direction is unresolved: E06 reports C as the effect allele, while E09c calls T the risk allele and says T increases AR occupancy. | weak | [E06](#e06), [E09c](#e09c) |

Predictions: Allele-specific AR ChIP in prostate cancer cells shows more AR on the T allele than the C allele at rs339331.; RFX6 expression or enhancer activity is AR-dependent and tracks the T allele in AR-positive prostate cancer cells.; AR perturbation reduces RFX6 expression or the relevant prostate cancer phenotype.

Falsified if: AR does not occupy this base in prostate cancer cells.; The C allele, not T, shows higher AR occupancy.; RFX6 expression is not affected by AR or by this allele in prostate cancer cells.

### 4. H3_PKNOX1: PKNOX1 binds the C allele weakly at rs339331 outside prostate context (p = 0.08)

TF PKNOX1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2496909 dELS; gene RFX6; cell type prostate cancer / LNCaP clone FGC.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | PKNOX1 QBiC-SELEX predicts the alt C allele binds more strongly (z 11.43, effect +0.521, above the gate), but the best site is weak on both alleles (ref 86.1st, alt 96.7th percentile). PKNOX1 ChIP contains the variant only in HEK293T, not LNCaP, so prostate-cell occupancy is not established. | weak | [E11](#e11), [E05](#e05), [E10](#e10) |
| element | The variant lies in dELS EH38E2496909, and PKNOX1 ChIP-seq peaks containing the variant exist in other biosamples. | supported | [E03](#e03), [E05](#e05) |
| gene | RFX6 is the nearest gene and the best-supported L2G target, but there is no direct PKNOX1-to-RFX6 evidence; this gene link is conditional. | weak | [E02](#e02), [E07](#e07) |
| cell_type | PKNOX1 is expressed in LNCaP clone FGC (8.32 TPM), but the only ChIP peak over the variant is from HEK293T; the prostate-cell link is weak. | weak | [E05](#e05) |
| phenotype | The locus is associated with prostate cancer, but a PKNOX1-mediated route through this weak, non-prostate-occupied site is speculative. | weak | [E06](#e06) |

Predictions: PKNOX1 ChIP in prostate cancer cells shows occupancy at rs339331, preferably on the C allele.; PKNOX1 perturbation changes RFX6 expression or enhancer activity in prostate cells.; The weak QBiC site is not functional unless another factor or co-factor stabilizes PKNOX1 binding.

Falsified if: PKNOX1 does not occupy this base in prostate cancer cells.; There is no allele-specific PKNOX1 binding at rs339331.; PKNOX1 loss does not affect RFX6 or enhancer activity.

## Prediction matrix

| Test | Cost | Separates top two | H2_HOXB13 | H4_null | H1_AR | H3_PKNOX1 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific HOXB13 ChIP-qPCR at rs339331 in LNCaP clone FGC (T vs C) | medium | yes | T allele shows higher HOXB13 occupancy at rs339331. | No allele-specific HOXB13 occupancy at this base. | No HOXB13 occupancy; if any allele-specific occupancy is seen, it is AR rather than HOXB13. | No HOXB13 occupancy at rs339331. |
| Allele-specific AR ChIP-qPCR at rs339331 in LNCaP clone FGC (T vs C) | medium | no | No AR occupancy at this base. | No allele-specific AR occupancy at this base. | T allele shows higher AR occupancy at rs339331. | No AR occupancy at this base. |
| T-vs-C rs339331 enhancer reporter assay in LNCaP cells with HOXB13 knockdown | medium | yes | T allele gives higher enhancer activity, and the effect is reduced by HOXB13 knockdown. | No allele-specific enhancer activity. | T allele gives higher enhancer activity, and the effect is reduced by AR knockdown rather than HOXB13 knockdown. | C allele gives higher enhancer activity, and the effect is reduced by PKNOX1 knockdown. |
| Allele-specific RFX6 expression or eQTL analysis in prostate/PCa cells after controlling for linked variants | low | yes | T allele associates with higher RFX6 expression in a HOXB13-dependent manner. | No allelic RFX6 effect after linked-variant control. | T allele associates with higher RFX6 expression in an AR-dependent manner. | C allele associates with higher RFX6 expression or PKNOX1-dependent RFX6 regulation. |
| PKNOX1 ChIP-qPCR at rs339331 in LNCaP clone FGC | medium | no | No PKNOX1 occupancy at this base. | No allele-specific PKNOX1 occupancy. | No PKNOX1 occupancy at this base. | C allele shows higher PKNOX1 occupancy at rs339331. |

## Next experiment

Allele-specific HOXB13 ChIP-qPCR at rs339331 in LNCaP clone FGC, with AR ChIP and input controls, is the cheapest targeted experiment that directly tests the top chain's base-level occupancy and separates it from the null.

## Investigate calls

- qbic_tf_detail({"tf": "HOXB13"})
- chip_peaks({"tf": "AR", "biosample": null})
- literature_search({"query": "rs339331 risk allele T AR RFX6 prostate cancer direction"})

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

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr6:116888889:T>C, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000977), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 1 of 1 occupied (0 with a strong site), 5 of 131 with unknown occupancy. Left out: 1 TFs assayed in the matching biosample and 569 assayed only elsewhere, none with a peak here; 2 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element. No occupied TF has a strong site at the variant.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PKNOX1 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model TGIF2LX_eDBD_TGAGAA40NGCG_KO_yin2017_0_4_7mer (a CIS-BP-mapped model of TGIF2LX), z 11.43, effect 0.521: alt allele binds more (|z| above the gate), but between weak k-mers. 8.32 TPM, rank 573 of 1626 TFs in DepMap:ACH-000977 (LNCaP clone FGC). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HEK293T, e.g. ENCSR233FAG. Best model's site strength: ref 86.1th, alt 96.7th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXC13 (Homeodomain, 4 models; QBiC-SELEX coverage: own model): best model HOXB13_NA_TGCCTG20NGA_ESY_yang2017_0_3_7mer (a CIS-BP-mapped model of HOXB13), z -103.49, effect -4.771: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.13 TPM, rank 821 of 1626 TFs in DepMap:ACH-000977 (LNCaP clone FGC). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.9th, alt 97.2th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXA6 (Homeodomain, 18 models; QBiC-SELEX coverage: own model): best model HOXC10_FL_TTGGCC40NTCG_KX_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXC10), z -84.28, effect -4.457: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.75 TPM, rank 915 of 1626 TFs in DepMap:ACH-000977 (LNCaP clone FGC). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 89.4th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXB9 (Homeodomain, 18 models; QBiC-SELEX coverage: own model): best model HOXC10_FL_TTGGCC40NTCG_KX_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXC10), z -84.28, effect -4.457: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.77 TPM, rank 1003 of 1626 TFs in DepMap:ACH-000977 (LNCaP clone FGC). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 89.4th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXC12 (Homeodomain, 18 models; QBiC-SELEX coverage: own model): best model HOXC10_FL_TTGGCC40NTCG_KX_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXC10), z -84.28, effect -4.457: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.33 TPM, rank 676 of 1626 TFs in DepMap:ACH-000977 (LNCaP clone FGC). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 89.4th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXC6 (Homeodomain, 18 models; QBiC-SELEX coverage: mapped models only): best model HOXC10_FL_TTGGCC40NTCG_KX_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXC10), z -84.28, effect -4.457: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 18.43 TPM, rank 295 of 1626 TFs in DepMap:ACH-000977 (LNCaP clone FGC). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 89.4th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"HOXB13","symbol":"HOXB13","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr6:116888889:T>C","gate_p":5.02e-05,"models":[{"model":"HOXB13_NA_TGCCTG20NGA_ESY_yang2017_0_3_7mer","mapping":"own","group":"G024 Homeodomain, 4 models","quality":0.914,"effect":-4.771,"z":-103.49,"p":0.0,"rank_abs_z":"1/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":97.2,"k":7}},{"model":"HOXA13_eDBD_TACTGA40NACC_KP_yin2017_1_2_7mer","mapping":"CIS-BP (HOXA13)","group":"G024 Homeodomain, 4 models","quality":0.643,"effect":-0.723,"z":-74.87,"p":0.0,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":78.0,"k":7}},{"model":"HOXC13_NA_TCCCTC20NTCC_ESY_yang2017_0_3_7mer","mapping":"CIS-BP (HOXC13)","group":"G024 Homeodomain, 4 models","quality":0.855,"effect":-2.96,"z":-64.27,"p":0.0,"rank_abs_z":"11/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":91.9,"k":7}},{"model":"HOXD13_NA_TGATAA20NATA_ESAC_yang2017_0_4_7mer","mapping":"CIS-BP (HOXD13)","group":"G024 Homeodomain, 4 models","quality":0.696,"effect":-3.437,"z":-69.26,"p":0.0,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":92.8,"k":7}}]}

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:23+00:00)

> No ENCODE AR ChIP-seq peak contains chr6:116888889:T>C. Absence can also mean no AR experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20risk%20allele%20T%20AR%20RFX6%20prostate%20cancer%20direction&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:12:36+00:00)

> Europe PMC: 2 hits for 'rs339331 risk allele T AR RFX6 prostate cancer direction'; top 2 with PMIDs:
> PMID 27986209 (2017): Prostate Cancer Genetics: Variation by Race, Ethnicity, and Geography.
> PMID 30033361 (2018): Biology and Clinical Implications of the 19q13 Aggressive Prostate Cancer Susceptibility Locus.
