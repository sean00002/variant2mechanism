# rs339331 and Prostate cancer (6q22)

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 270 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: PKNOX1 (bound elsewhere, z 11.43, weak site). Occupancy unknown: HOXC13 (z -103.49); HOXA6 (z -84.28); HOXB9 (z -84.28); HOXC12 (z -84.28); HOXC6 (z -84.28). Diagnostic, not shown to the model: 487 of 997 models pass Bonferroni.

## Ranked chains

### 1. null_no_tf_effect: Null: no TF-mediated effect of this base (p = 0.46)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy or reporter activity at this exact base in prostate cancer cells/tumors.; The GWAS signal is explained by a linked causal variant, a passenger mutation, or an element whose activity is set elsewhere.; The QBiC-SELEX predictions for HOXC6/PKNOX1 do not translate into occupancy at this base, and the AR literature reflects a different tumor context or a linked site.

Falsified if: Allele-specific AR, HOXC6, or PKNOX1 ChIP or reporter assays in prostate cancer cells/tumors demonstrate a direct effect of this base.; Fine-mapping or functional assays show this variant, rather than a linked variant, drives the prostate cancer signal.; Perturbation of a candidate TF changes RFX6 expression in an allele-dependent manner.

### 2. AR_RFX6_enhancer: AR occupies the dELS more strongly on ref T, but base-level AR binding is not supported by QBiC-SELEX (p = 0.32)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element dELS; gene RFX6; cell type prostate cancer tumor/PDX cells with reprogrammed AR occupancy.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR is the candidate TF, with ref T predicted to support stronger AR occupancy in prostate tumor chromatin (E09d). However, AR's own QBiC-SELEX model at this base shows no significant allelic change (effect 0.035, z 0.94, weak site; E17), and E04 reports no LNCaP ChIP peak at this base. Thus AR occupancy could be element-level rather than a direct readout of this base. | weak | [E09d](#e09d), [E17](#e17), [E04](#e04) |
| element | The variant lies in the distal enhancer-like cCRE EH38E2496909, and E09d places it in a reprogrammed AR binding site in prostate cancer tumors. | supported | [E03](#e03), [E09d](#e09d) |
| gene | RFX6 is the nearest protein-coding gene and the strongest L2G target at this locus. The enhancer-to-RFX6 link remains positional/genetic, however, because no prostate eQTL is reported in E19 and the only significant GTEx eQTL is for FAM162B in adipose tissue (E08). | weak | [E02](#e02), [E07](#e07), [E09c](#e09c), [E19](#e19), [E08](#e08) |
| cell_type | The AR chain depends on prostate tumor-context occupancy with reprogrammed AR binding. LNCaP is a prostate cancer expression context, but E04 reports no LNCaP ChIP peak at this base, so this chain is not supported by LNCaP ChIP. | weak | [E09d](#e09d), [E04](#e04) |
| phenotype | The locus is strongly associated with prostate cancer, but allelic direction is unresolved: E06's strongest prostate cancer GWAS lists C as the effect allele, E06's PSA association lists T, and E09d reports that T enhances AR occupancy. | supported | [E06](#e06), [E07](#e07), [E09d](#e09d) |

Predictions: Allele-specific AR ChIP or reporter in prostate tumor/PDX cells shows higher AR occupancy/activity on ref T than alt C.; AR perturbation in the same prostate cancer context changes RFX6 expression.; If AR mediates disease risk, the T allele should track with the functional risk direction, but this must be reconciled with E06 listing C as the strongest prostate cancer effect allele.

Falsified if: Allele-specific AR ChIP or reporter assays in prostate cancer tumor/PDX cells show no difference between T and C, or show alt C binds/activates AR more strongly.; AR perturbation does not alter RFX6 expression in the relevant prostate cancer context.; Fine-mapping or functional assays show this variant is not causal.

### 3. HOXC6_RFX6_enhancer: HOXC6 binds ref T more strongly at the dELS, but occupancy in prostate cancer cells is unproven (p = 0.14)

TF HOXC6 (QBiC-SELEX coverage mapped), ref allele binds more; element dELS; gene RFX6; cell type LNCaP prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXC6 is predicted to bind ref T more strongly than alt C. E16 gives a QBiC-SELEX mapped model (CIS-BP-mapped HOXC10 model) with z -84.28 and effect -4.457, ref site 100.0th versus alt 89.4th percentile. HOXC6 is expressed in LNCaP at 18.43 TPM, the highest among the identical shared-model homeodomain TFs in E13-E16. HOXC6 has no own model in this evidence and no occupancy evidence; E18 reports no HOXC6 ChIP peak in LNCaP, though absence can reflect no experiment. | weak | [E16](#e16), [E18](#e18), [E13](#e13), [E14](#e14), [E15](#e15) |
| element | The variant lies in the distal enhancer-like cCRE EH38E2496909, a class consistent with allele-specific TF binding. | supported | [E03](#e03), [E04](#e04) |
| gene | RFX6 is the nearest coding gene and strongest L2G target, so an enhancer effect at this element is most plausibly on RFX6; however, no prostate eQTL is reported (E19), so this target link is positional/genetic rather than functionally demonstrated. | weak | [E02](#e02), [E07](#e07), [E09c](#e09c), [E19](#e19) |
| cell_type | HOXC6 is expressed in LNCaP at 18.43 TPM, making LNCaP a plausible expression context. Occupancy at this base in LNCaP is not established. | supported | [E16](#e16), [E18](#e18) |
| phenotype | The locus is associated with prostate cancer risk. There is no evidence that HOXC6 binding at this element changes RFX6 expression or disease direction, so the phenotype link is a plausible mechanism rather than a supported one. | weak | [E06](#e06), [E07](#e07) |

Predictions: Allele-specific HOXC6 ChIP or reporter in LNCaP shows higher HOXC6 binding/activity on ref T than alt C.; HOXC6 perturbation in LNCaP changes RFX6 expression.; The effect should be strongest where HOXC6 is highly expressed, such as LNCaP.

Falsified if: HOXC6 ChIP or reporter assays show no allele-specific binding at this element in prostate cancer cells.; HOXC6 perturbation does not affect RFX6 expression in prostate cancer cells.; The HOXC6 QBiC-SELEX prediction does not translate to occupancy at this base.

### 4. PKNOX1_RFX6_enhancer: PKNOX1 binds alt C more strongly at a weak QBiC-SELEX site, with occupancy only outside LNCaP (p = 0.08)

TF PKNOX1 (QBiC-SELEX coverage own_model), alt allele binds more; element dELS; gene RFX6; cell type LNCaP prostate cancer cells (expression context only).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | PKNOX1 is predicted to bind alt C more strongly than ref T. E11 reports QBiC-SELEX z 11.43 and effect 0.521 (alt binds more), but the best model is a CIS-BP-mapped TGIF2LX model and the site is weak on both alleles (ref 86.1th, alt 96.7th percentile). E05 shows PKNOX1 ChIP over the variant only in HEK293T, and E04 reports no LNCaP peak at this base. | weak | [E11](#e11), [E05](#e05), [E04](#e04) |
| element | The variant lies in the distal enhancer-like cCRE EH38E2496909. | supported | [E03](#e03) |
| gene | RFX6 is the nearest coding gene and the strongest L2G target at this locus, making it the best local candidate target for this element. No prostate eQTL supports this enhancer-to-RFX6 link (E19). | weak | [E02](#e02), [E07](#e07), [E09c](#e09c), [E19](#e19) |
| cell_type | PKNOX1 is expressed in LNCaP at 8.32 TPM, so prostate cancer cells are a plausible context, but the reported ChIP evidence is from HEK293T rather than LNCaP. | supported | [E05](#e05) |
| phenotype | The locus is associated with prostate cancer risk; an allele-specific PKNOX1 effect on RFX6 would connect the variant to disease, but the binding evidence is weak and not in LNCaP. | weak | [E06](#e06), [E07](#e07) |

Predictions: Allele-specific PKNOX1 ChIP or reporter in prostate cancer cells shows higher binding/activity on alt C than ref T.; PKNOX1 perturbation changes RFX6 expression in prostate cancer cells.; The effect is weak because the PKNOX1 site is weak on both alleles and the only reported ChIP peak is in HEK293T.

Falsified if: PKNOX1 ChIP or reporter assays in prostate cancer cells show no allele-specific binding at this element.; PKNOX1 perturbation does not change RFX6 expression.; The weak QBiC-SELEX site is shown not to be occupied by PKNOX1 in prostate cancer cells.

## Prediction matrix

| Test | Cost | Separates top two | null_no_tf_effect | AR_RFX6_enhancer | HOXC6_RFX6_enhancer | PKNOX1_RFX6_enhancer |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific AR ChIP-qPCR at chr6:116888889 in prostate tumor/PDX or AR-positive prostate cancer cells | medium | yes | null_no_tf_effect | AR_RFX6_enhancer | HOXC6_RFX6_enhancer | PKNOX1_RFX6_enhancer |

## Next experiment

Allele-specific AR ChIP-qPCR at chr6:116888889 in an AR-positive prostate cancer tumor/PDX model with a heterozygous T/C genotype, comparing ref T versus alt C AR occupancy. If tumor material is unavailable, an AR reporter assay in LNCaP with AR expression is the cheaper proxy, but it is less AR-specific.

## Investigate calls

- qbic_tf_detail({"tf": "AR"})
- chip_peaks({"tf": "HOXC6", "biosample": "LNCaP clone FGC"})
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

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=RFX6%20AND%20%22prostate%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:18:46+00:00)

> Europe PMC: 148 hits for 'RFX6 AND "prostate cancer"'; top 7 with PMIDs:
> PMID 41422049 (2025): Multifaceted functions of transcription regulatory factor X6 (RFX6): from pancreatic development to cancer progression.
> PMID 41716817 (2026): RFX6 expression is central to the development and function of the neuroendocrine compartments of the pancreas and intestine and strongly affects diabetes risk.
> PMID 42676892 (2026): The function of phosphoglycerate mutase 1 (PGAM1) and its role in diseases.
> PMID 38932472 (2024): An Inherited Allele Confers Prostate Cancer Progression and Drug Resistance via RFX6/HOXA10-Orchestrated TGFβ Signaling.
> PMID 40181298 (2025): Genetic associations of prostate cancer in China: a systematic review.
> PMID 41374944 (2025): The Clinical Relevance of Tumor Biomarkers in Prostate Cancer-A Review.
> PMID 42588668 (2026): Sub-Saharan African Prostate Cancer Patient-Derived Cell Lines and High-Throughput Drug Screening: Addressing Ancestry Underrepresentation in Oncobiology Research.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 41422049 (https://europepmc.org/article/MED/41422049; retrieved 2026-10-26T20:18:46+00:00)

> Dysregulated expression or mutations of the RFX6 gene in prostate cancer, hepatocellular carcinoma, gastric cancer, melanoma, and other tumors have garnered significant interest, with studies showing that such alterations affect tumor cell proliferation, migration, and invasion, and are correlated with an unfavorable clinical prognosis in patients carrying RFX6 mutations.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 41422049 (https://europepmc.org/article/MED/41422049; retrieved 2026-10-26T20:18:46+00:00)

> Furthermore, examination of RFX6 target genes reveals a potential association with tumor development, indicating that RFX6 may play a role in cancer progression.

<a id="e09c"></a>**E09c** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T20:18:46+00:00)

> Here the FinnGen cohort phenome-wide analysis, along with multiple genome-wide association studies, has consistently identified the rs[masked]-RFX6/6q22 locus associated with prostate cancer (PCa) risk across diverse populations.

<a id="e09d"></a>**E09d** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T20:18:46+00:00)

> It is uncovered that rs[masked] resides in a reprogrammed androgen receptor (AR) binding site in PCa tumors, with the T risk allele enhancing AR chromatin occupancy.

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

> {"tf":"AR","symbol":"AR","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr6:116888889:T>C","gate_p":5.02e-05,"models":[{"model":"AR_NA_TGCTCG20NGA_AF_jolma2013_1_3_7mer","mapping":"own","group":"G016 Nuclear receptor, 4 models","quality":0.601,"effect":0.035,"z":0.94,"p":0.35,"rank_abs_z":"866/997","passed_gate":false,"site_strength":{"ref_percentile":70.4,"alt_percentile":83.3,"k":7}},{"model":"GR_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer","mapping":"CIS-BP (NR3C1)","group":"G016 Nuclear receptor, 4 models","quality":0.913,"effect":0.083,"z":1.44,"p":0.15,"rank_abs_z":"799/997","passed_gate":false,"site_strength":{"ref_percentile":65.9,"alt_percentile":74.5,"k":7}},{"model":"NR3C2_eDBD_TGCTGG40NGCC_KT_yin2017_0_4_7mer","mapping":"CIS-BP (NR3C2)","group":"G016 Nuclear receptor, 4 models","quality":0.751,"effect":0.811,"z":9.5,"p":2e-21,"rank_abs_z":"135/997","passed_gate":true,"site_strength":{"ref_percentile":64.7,"alt_percentile":83.6,"k":7}},{"model":"PGR_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (PGR)","group":"G016 Nuclear receptor, 4 models","quality":0.544,"effect":0.108,"z":2.46,"p":0.014,"rank_abs_z":"660/997","passed_gate":false,"site_strength":{"ref_percentile":65.1,"alt_percentile":80.1,"k":7}}]}

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:29:03+00:00)

> No ENCODE HOXC6 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP clone FGC'. Absence can also mean no HOXC6 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).
