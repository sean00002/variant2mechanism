# rs339331 and Prostate cancer (6q22)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.05 over 7 model calls; 187 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: PKNOX1 (bound elsewhere, z 11.43). Occupancy unknown: HOXC13 (z -103.49); HOXA6 (z -84.28); HOXB9 (z -84.28); HOXC12 (z -84.28); HOXC6 (z -84.28). Diagnostic, not shown to the model: 487 of 997 models pass Bonferroni.

## Ranked chains

### 1. null: No TF-mediated effect (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: No transcription factor shows allele-specific occupancy at rs339331 in the relevant prostate cancer context.; RFX6 expression and prostate cancer risk are driven by a linked variant or by another element.

Falsified if: Allele-specific ChIP or reporter assays in prostate cancer cells show a reproducible rs339331 effect.; Fine-mapping isolates rs339331 as the causal variant rather than a linked variant.

### 2. AR: AR (p = 0.28)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element dELS enhancer EH38E2496909; gene RFX6; cell type Prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR occupies a reprogrammed AR binding site at rs339331 in prostate cancer tumors, and the T/ref allele increases AR chromatin occupancy; no AR QBiC-SELEX model is provided. | weak | [E09c](#e09c) |
| element | rs339331 lies within cCRE EH38E2496909, a distal enhancer-like element. | supported | [E03](#e03) |
| gene | RFX6 is the nearest listed gene and the top L2G candidate in prostate cancer credible sets, but this is proximity/L2G evidence rather than a prostate eQTL or enhancer-perturbation result. | weak | [E02](#e02), [E07](#e07) |
| cell_type | AR occupancy at this site is reported in prostate cancer tumors, supporting AR action in the prostate cancer context. | supported | [E09c](#e09c) |
| phenotype | rs339331 is associated with prostate cancer and the rs339331-RFX6 locus is implicated, but E06 reports C as the strongest prostate cancer effect allele while E09c calls T the risk allele and T the stronger AR-occupancy allele, so this chain has an unresolved direction conflict. | weak | [E06](#e06), [E09b](#e09b), [E09c](#e09c) |

Predictions: Allele-specific AR ChIP in prostate cancer cells will show stronger T than C occupancy at rs339331.; If AR mediates the effect, AR perturbation should alter RFX6 expression or enhancer activity in an AR-positive prostate cancer line.

Falsified if: Allele-specific AR ChIP shows no T/C difference at rs339331 in prostate cancer cells.; AR perturbation does not affect RFX6 expression or enhancer activity in an AR-positive prostate cancer line.

### 3. HOXB13: HOXB13 (p = 0.22)

TF HOXB13 (QBiC-SELEX coverage own_model), ref allele binds more; element dELS enhancer EH38E2496909; gene RFX6; cell type Prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 is reported in a GATA2/SMAD4/HOXB13 complex at the rs339331 enhancer in prostate cancer; no HOXB13 QBiC-SELEX model or direct allele-specific HOXB13 ChIP is provided, so the ref-T-more direction is an untested inference and not directly established. | weak | [E09d](#e09d) |
| element | rs339331 lies within cCRE EH38E2496909, a distal enhancer-like element. | supported | [E03](#e03) |
| gene | The GATA2/SMAD4/HOXB13-containing complex at this enhancer is reported to increase RFX6 expression. | supported | [E09d](#e09d) |
| cell_type | The HOXB13-containing complex is reported at the rs339331/6q22 prostate cancer risk enhancer with GATA2 and SMAD4, supporting a prostate cancer context. | supported | [E09d](#e09d) |
| phenotype | rs339331 is associated with prostate cancer and RFX6 is a candidate susceptibility gene, but if the HOXB13 complex increases RFX6 and ref T binds more, the risk direction conflicts with E06 reporting C as the strongest prostate cancer effect allele. | weak | [E06](#e06), [E09b](#e09b), [E09d](#e09d) |

Predictions: Allele-specific HOXB13 ChIP in prostate cancer cells will show stronger T than C occupancy at rs339331.; Disrupting HOXB13 or the GATA2/SMAD4/HOXB13 complex should reduce RFX6 expression.

Falsified if: HOXB13 ChIP does not occupy this element in prostate cancer cells.; Allele-specific HOXB13 ChIP shows no T/C difference at rs339331.; Disrupting the HOXB13/GATA2/SMAD4 complex does not reduce RFX6 expression.

### 4. PKNOX1: PKNOX1 (p = 0.10)

TF PKNOX1 (QBiC-SELEX coverage own_model), alt allele binds more; element dELS enhancer EH38E2496909; gene RFX6; cell type Prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | PKNOX1 QBiC-SELEX shows the alt C allele binds more strongly, but the best model is a CIS-BP-mapped TGIF2LX model and ENCODE ChIP shows PKNOX1 over this site only in HEK293T, not LNCaP, so occupancy in the disease context is absent and the binding evidence is weak. | weak | [E04](#e04), [E05](#e05), [E11](#e11) |
| element | rs339331 lies within cCRE EH38E2496909, a distal enhancer-like element. | supported | [E03](#e03) |
| gene | RFX6 is the nearest listed gene and the top L2G candidate in prostate cancer credible sets, but this is proximity/L2G evidence rather than a prostate eQTL or enhancer-perturbation result. | weak | [E02](#e02), [E07](#e07) |
| cell_type | PKNOX1 is expressed in LNCaP, but the provided LNCaP ChIP data do not show PKNOX1 occupancy at the variant; occupancy is only reported elsewhere. | weak | [E04](#e04), [E05](#e05), [E11](#e11) |
| phenotype | The alt C allele is the strongest prostate cancer GWAS effect allele and the allele that binds PKNOX1 more in QBiC-SELEX, but there is no evidence that PKNOX1 binding changes RFX6 expression. | weak | [E06](#e06), [E11](#e11) |

Predictions: Allele-specific PKNOX1 ChIP in LNCaP will show stronger C than T occupancy at rs339331.; PKNOX1 loss will reduce RFX6 expression if the enhancer is active in prostate cancer cells.

Falsified if: PKNOX1 ChIP shows no occupancy and no C>T allelic difference at rs339331 in LNCaP.; PKNOX1 knockdown does not alter RFX6 expression in LNCaP.

## Prediction matrix

| Test | Cost | Separates top two | null | AR | HOXB13 | PKNOX1 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific AR ChIP-qPCR at rs339331 in LNCaP or another AR-positive prostate cancer line, comparing T and C alleles. | low | yes | No allelic difference in AR occupancy at rs339331. | Stronger T than C AR occupancy at rs339331 in prostate cancer cells. | No AR-allele-specific prediction; AR ChIP does not test HOXB13. | No AR-allele-specific prediction; AR ChIP does not test PKNOX1. |
| Allele-specific HOXB13 ChIP-qPCR at rs339331 in LNCaP or another prostate cancer line, comparing T and C alleles. | medium | no | No allelic difference in HOXB13 occupancy at rs339331. | No HOXB13-allele-specific prediction; HOXB13 ChIP does not test AR. | Stronger T than C HOXB13 occupancy at rs339331 in prostate cancer cells. | No HOXB13-allele-specific prediction; HOXB13 ChIP does not test PKNOX1. |
| Allele-specific PKNOX1 ChIP-qPCR at rs339331 in LNCaP, comparing T and C alleles. | medium | no | No PKNOX1 occupancy or no allelic difference at rs339331. | No PKNOX1-allele-specific prediction; PKNOX1 ChIP does not test AR. | No PKNOX1-allele-specific prediction; PKNOX1 ChIP does not test HOXB13. | PKNOX1 occupies rs339331 in LNCaP, with stronger C than T binding. |
| Rs339331 T/C enhancer reporter assay or allele-specific RFX6 expression assay in LNCaP/prostate cancer cells. | medium | yes | No allele-specific effect of rs339331 on RFX6 expression or enhancer reporter activity. | Allele-specific RFX6 expression or enhancer reporter activity in prostate cancer cells, in a direction consistent with AR occupancy at the T allele. | Allele-specific RFX6 expression or reporter activity with the T allele increasing RFX6 if the HOXB13 complex is activating. | Allele-specific RFX6 expression or reporter activity with the C allele increasing RFX6 if PKNOX1 is activating. |
| CRISPRi/dCas9 repression or deletion of cCRE EH38E2496909 in LNCaP, followed by RFX6 expression measurement. | high | yes | Enhancer repression or deletion does not change RFX6 expression. | Enhancer repression or deletion reduces RFX6 expression in an AR-dependent manner. | Enhancer repression or deletion reduces RFX6 expression, consistent with the HOXB13/GATA2/SMAD4 complex. | Enhancer repression or deletion reduces RFX6 expression if the PKNOX1-bound element is active. |

## Next experiment

Allele-specific AR ChIP-qPCR at rs339331 in LNCaP or another AR-positive prostate cancer line, comparing T and C alleles; this directly separates the top two chains, AR versus null, at low cost.

## Investigate calls

- eqtl_lookup({"tissue": "Prostate"})
- tf_expression({"context": null, "tf": "RFX6"})
- gene_dependency({"gene": "RFX6"})

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

> QBiC-SELEX screen of chr6:116888889:T>C, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000977), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 1 of 1 occupied, 5 of 131 with unknown occupancy. Left out: 1 TFs assayed in the matching biosample and 569 assayed only elsewhere, none with a peak here; 2 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PKNOX1 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model TGIF2LX_eDBD_TGAGAA40NGCG_KO_yin2017_0_4_7mer (a CIS-BP-mapped model of TGIF2LX), z 11.43, effect 0.521: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.32 TPM, rank 573 of 1626 TFs in DepMap:ACH-000977 (LNCaP clone FGC). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HEK293T, e.g. ENCSR233FAG. Best model's site strength: ref 86.1th, alt 96.7th percentile of its k-mer coefficients.

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

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e18"></a>**E18** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> RFX6 in DepMap line ACH-000977: 0.11 TPM, rank 1238 of 1626 TFs (1 = highest); this context is at the 95.1th percentile of RFX6 across all DepMap lines.

<a id="e19"></a>**E19** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for RFX6 (0 = no effect, -1 = median common-essential; < -0.5 called dependent). LNCaP clone FGC (ACH-000977): -0.08. Prostate lineage, 10 lines: median -0.07, 0% dependent. All 1183 lines: median -0.04, 0% dependent.
