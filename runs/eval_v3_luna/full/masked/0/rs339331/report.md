# rs339331 and Prostate cancer (6q22)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 129 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: PKNOX1 (bound elsewhere, z 11.43, weak site). Occupancy unknown: HOXC13 (z -103.49); HOXA6 (z -84.28); HOXB9 (z -84.28); HOXC12 (z -84.28); HOXC6 (z -84.28). Diagnostic, not shown to the model: 487 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: No TF-mediated effect at this variant (p = 0.72)

Null chain: no TF-mediated effect of this variant.

Predictions: In relevant prostate cells, the T-to-C change will not produce a reproducible allele-dependent TF-binding effect that drives regulation of RFX6.; The prostate-cancer association may reflect linkage to another causal variant or a mechanism other than TF-mediated activity at this base.

Falsified if: Isogenic T-to-C editing produces a reproducible allele-dependent molecular effect at this element, and disrupting the implicated TF or its binding site removes that effect.

### 2. H2: PKNOX1 preferentially binds C and may alter RFX6 regulation (p = 0.15)

TF PKNOX1 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in the enhancer-like cCRE EH38E2496909; activity of this element in LNCaP is not established.; gene RFX6; cell type LNCaP-like prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | PKNOX1 is the expressed, modelled TF with a reported variant-overlapping peak, and its QBiC-SELEX model predicts stronger binding to C; however, the peak is from HEK293T, the predicted site is weak, and neither result establishes PKNOX1 occupancy at this base in LNCaP. | weak | [E04](#e04), [E05](#e05), [E10](#e10), [E11](#e11) |
| element | The variant overlaps enhancer-like cCRE EH38E2496909, but the available biosample-maximum scores do not establish activity in LNCaP. | supported | [E03](#e03) |
| gene | RFX6 is a candidate target because the variant is intronic to RFX6 and prostate-cancer credible sets prioritize it, although neither a direct cCRE-to-RFX6 link nor a significant prostate RFX6 eQTL is shown. | supported | [E01](#e01), [E02](#e02), [E07](#e07), [E19](#e19) |
| cell_type | This is a candidate mechanism in LNCaP-like cells, where PKNOX1 is expressed, but ENCODE reports no matching-biosample peak over the variant. | supported | [E04](#e04), [E05](#e05) |
| phenotype | A PKNOX1-dependent effect on RFX6 could contribute to prostate-cancer risk, but the locus association and RFX6 literature do not establish this specific causal chain or the direction of its regulatory effect. | weak | [E06](#e06), [E07](#e07), [E09a](#e09a), [E09b](#e09b) |

Predictions: If PKNOX1 mediates an effect at this base in prostate cells, C will show greater PKNOX1 occupancy than T, and disrupting PKNOX1 or its local binding site will reduce the allele-dependent effect.; The predicted binding difference alone does not specify whether RFX6 expression rises or falls.

Falsified if: A sensitive allele-resolved assay in relevant prostate cells detects no PKNOX1 occupancy difference between C and T, and PKNOX1 perturbation does not alter any variant-dependent molecular effect.

### 3. H3: HOXC6 preferentially binds T and may alter RFX6 regulation (p = 0.08)

TF HOXC6 (QBiC-SELEX coverage mapped), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E2496909; its activity in prostate cells is not established.; gene RFX6; cell type LNCaP-like prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | A QBiC-SELEX model mapped to HOXC6 predicts stronger binding to T than C, but the model is not HOXC6-specific occupancy evidence, and no variant-overlapping HOXC6 peak is reported in LNCaP. | weak | [E10](#e10), [E16](#e16), [E17](#e17) |
| element | The variant overlaps enhancer-like cCRE EH38E2496909, but the available biosample-maximum scores do not establish activity in LNCaP. | supported | [E03](#e03) |
| gene | RFX6 is a candidate target prioritized by location and prostate-cancer credible-set gene scores, but a direct cCRE-to-RFX6 link and a significant prostate RFX6 eQTL are not shown. | supported | [E01](#e01), [E02](#e02), [E07](#e07), [E19](#e19) |
| cell_type | HOXC6 is expressed in LNCaP, but its occupancy at the variant and activity of the element in that context are unestablished. | supported | [E03](#e03), [E16](#e16), [E17](#e17) |
| phenotype | If HOXC6-dependent regulation of RFX6 occurs, it could be relevant to prostate-cancer risk, but the association and RFX6 literature do not demonstrate this chain or its regulatory direction. | weak | [E06](#e06), [E07](#e07), [E09a](#e09a), [E09b](#e09b) |

Predictions: If HOXC6 mediates an effect at this base, T will show greater HOXC6 occupancy than C, and HOXC6 perturbation will alter the allele-dependent molecular effect.; The proposed factor is HOXC6, not HOXC13; the mapped binding model does not by itself distinguish these related homeodomain factors.

Falsified if: Relevant prostate cells show no HOXC6 occupancy difference between T and C, or HOXC6 perturbation leaves any allele-dependent molecular effect unchanged.

### 4. H4: HOXC13 preferentially binds T and may alter RFX6 regulation (p = 0.05)

TF HOXC13 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E2496909; its activity in prostate cells is not established.; gene RFX6; cell type LNCaP-like prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | A QBiC-SELEX model mapped from HOXB13 predicts stronger binding to T than C for HOXC13, but this is not HOXC13 occupancy evidence, and no variant-overlapping HOXC13 peak is reported in LNCaP. | weak | [E10](#e10), [E12](#e12), [E18](#e18) |
| element | The variant overlaps enhancer-like cCRE EH38E2496909, but the available biosample-maximum scores do not establish activity in LNCaP. | supported | [E03](#e03) |
| gene | RFX6 is a candidate target prioritized by location and prostate-cancer credible-set gene scores, but a direct cCRE-to-RFX6 link and a significant prostate RFX6 eQTL are not shown. | supported | [E01](#e01), [E02](#e02), [E07](#e07), [E19](#e19) |
| cell_type | HOXC13 is expressed in LNCaP, but its occupancy at the variant and activity of the element in that context are unestablished. | supported | [E03](#e03), [E12](#e12), [E18](#e18) |
| phenotype | If HOXC13-dependent regulation of RFX6 occurs, it could be relevant to prostate-cancer risk, but the association and RFX6 literature do not demonstrate this chain or its regulatory direction. | weak | [E06](#e06), [E07](#e07), [E09a](#e09a), [E09b](#e09b) |

Predictions: If HOXC13 mediates an effect at this base, T will show greater HOXC13 occupancy than C, and HOXC13 perturbation will alter the allele-dependent molecular effect.; The proposed factor is HOXC13, not HOXC6; the related mapped binding models do not independently establish which factor, if either, occupies the site.

Falsified if: Relevant prostate cells show no HOXC13 occupancy difference between T and C, or HOXC13 perturbation leaves any allele-dependent molecular effect unchanged.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Measure allele-resolved PKNOX1 occupancy at the variant by targeted CUT&RUN-qPCR in variant-heterozygous LNCaP cells. | medium | yes | No reproducible C-versus-T PKNOX1 occupancy difference. | Greater PKNOX1 occupancy on C than T. | No C-biased PKNOX1 occupancy; this chain instead predicts a T-biased HOXC6 effect. | No C-biased PKNOX1 occupancy; this chain instead predicts a T-biased HOXC13 effect. |
| Measure allele-resolved HOXC6 and HOXC13 occupancy at the variant in relevant prostate cells. | medium | no | No reproducible allele-dependent occupancy attributable to either proposed factor. | No allele-dependent HOXC6 or HOXC13 occupancy is predicted; the proposed factor is PKNOX1. | HOXC6 occupancy is greater on T than C. | HOXC13 occupancy is greater on T than C. |
| In matched T and C isogenic LNCaP models, measure RFX6 expression with and without perturbation of the proposed TF. | high | yes | No reproducible allele-dependent RFX6 expression effect that depends on one of the proposed TFs. | An allele-dependent RFX6 effect is reduced by PKNOX1 perturbation; the direction of expression change is not specified by the binding evidence. | An allele-dependent RFX6 effect is reduced by HOXC6 perturbation; the direction of expression change is not specified by the binding evidence. | An allele-dependent RFX6 effect is reduced by HOXC13 perturbation; the direction of expression change is not specified by the binding evidence. |

## Next experiment

Perform allele-resolved PKNOX1 CUT&RUN-qPCR at the variant in variant-heterozygous LNCaP cells. It is the most direct, lower-cost test of the top non-null chain against the null: H2 predicts greater occupancy on C, whereas H1 predicts no reproducible allele-dependent occupancy.

## Investigate calls

- chip_peaks({"tf": "HOXC6", "biosample": "LNCaP clone FGC"})
- chip_peaks({"tf": "HOXC13", "biosample": "LNCaP clone FGC"})
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

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T20:18:46+00:00)

> Here the FinnGen cohort phenome-wide analysis, along with multiple genome-wide association studies, has consistently identified the rs[masked]-RFX6/6q22 locus associated with prostate cancer (PCa) risk across diverse populations.

<a id="e09c"></a>**E09c** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T20:18:46+00:00)

> Mechanistically, RFX6 upregulates HOXA10 that profoundly correlates with adverse PCa outcomes and is pivotal in RFX6-mediated PCa progression, facilitating the epithelial-mesenchymal transition (EMT) and modulating the TGFβ/SMAD signaling axis.

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

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:29:03+00:00)

> No ENCODE HOXC6 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP clone FGC'. Absence can also mean no HOXC6 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:29:03+00:00)

> No ENCODE HOXC13 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP clone FGC'. Absence can also mean no HOXC13 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).
