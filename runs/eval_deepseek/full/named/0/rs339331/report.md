# rs339331 and Prostate cancer (6q22)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 7 model calls; 195 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen

487 of 997 models pass the gate. Top groups: Homeodomain, 4 models (best HOXB13, z -103.49); Homeodomain, 18 models (best HOXC10, z -84.28); IRF, 2 models (best IRF6, z 56.39); C2H2 ZF, 1 model (best PRDM4, z 47.33); IRF, 1 model (best IRF3, z 44.89).

## Ranked chains

### 1. H1_AR_ref_T: AR binds the T allele more at the rs339331 enhancer and regulates RFX6 (p = 0.42)

TF AR (stated coverage not_checked; registry own_model), ref allele binds more; element dELS EH38E2496909; gene RFX6; cell type prostate cancer cells/tumors; LNCaP clone FGC (ACH-000977) is the supplied expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR binds the ref T allele more strongly than the alt C allele at rs339331 in prostate cancer chromatin; E06c reports that the T allele enhances AR chromatin occupancy. AR is not named in the supplied QBiC-SELEX screen rows, so its QBiC-SELEX coverage is not_checked; no AR own-model or mapped row is provided, and no other TF's binding change is used as AR evidence. | supported | [E06c](#e06c) |
| element | rs339331 lies within cCRE EH38E2496909, a distal enhancer-like element, making it a plausible allele-specific regulatory element. | supported | [E03](#e03) |
| gene | RFX6 is the nearest protein-coding gene and the strongest L2G gene in credible sets containing this variant; E06d reports an enhancer complex at rs339331 increasing RFX6. However, E20 found no significant GTEx v8 prostate eQTL for this variant, so a direct prostate eQTL link is not supported by that dataset. | weak | [E02](#e02), [E05](#e05), [E06d](#e06d), [E20](#e20) |
| cell_type | The relevant cell type is prostate cancer, with LNCaP (ACH-000977) as the supplied expression context and AR occupancy at this element described in prostate cancer tumors. E18 reports no ENCODE AR ChIP-seq peak containing rs339331 in LNCaP, with the caveat that absence can also mean no AR experiment in that biosample, so LNCaP-specific AR occupancy is not established by the supplied ChIP data. | weak | [E06c](#e06c), [E07](#e07), [E18](#e18) |
| phenotype | rs339331 is associated with prostate cancer risk at 6q22, and the locus has been repeatedly associated with prostate cancer across populations. The allelic direction is conflicting: E04 reports C as the strongest prostate-cancer effect allele, whereas E06c calls T the risk allele. | weak | [E04](#e04), [E05](#e05), [E06b](#e06b) |

Predictions: The T allele should show higher AR occupancy at the rs339331 enhancer than C.; If AR activates RFX6, T should increase RFX6; if AR represses RFX6, C with lower AR occupancy could increase RFX6 and fit the C effect allele reported in E04.; The chain predicts an AR-dependent, allele-specific enhancer effect at rs339331 in prostate cancer cells.

Falsified if: Allele-specific AR ChIP at rs339331 does not show higher AR occupancy on the T allele.; AR perturbation does not change RFX6 expression or enhancer activity in an rs339331-dependent manner.; The T-allele AR-occupancy report is not reproducible, or the C allele is shown to increase AR occupancy instead.

### 2. H4_null: Null: no TF-mediated effect of rs339331 (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No TF-mediated allelic effect of rs339331 on RFX6 or any other nearby gene.; The prostate cancer association is explained by a linked causal variant in the 6q22 credible set, by LD with another regulatory variant, or by a non-allelic mechanism.; E20 found no significant GTEx v8 prostate eQTL for rs339331, which is consistent with the null but does not prove it.

Falsified if: Allele-specific TF binding and reporter assays show a reproducible, RFX6-dependent effect of rs339331 itself rather than a linked variant.; Fine-mapping resolves the causal variant to rs339331 with a direct allelic regulatory effect.

### 3. H2_HOXB13_ref_T: HOXB13 binds the T allele more at the rs339331 enhancer and may modulate RFX6 (p = 0.18)

TF HOXB13 (stated coverage own_model; registry own_model), ref allele binds more; element dELS EH38E2496909; gene RFX6; cell type prostate cancer cells/tumors; LNCaP clone FGC (ACH-000977) expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 has an own QBiC-SELEX model in group G024; the best HOXB13 model scores z -103.49 with effect -4.771, meaning the alt C allele binds HOXB13 less and the ref T allele binds more. Within G024, HOXB13 is selected over related homeodomain TFs because it has the strongest own-model score and is highly expressed in the LNCaP context at 182.31 TPM; E06d also implicates HOXB13 at this enhancer. This is an in vitro binding prediction, not allele-specific ChIP evidence. | weak | [E08](#e08), [E06d](#e06d) |
| element | rs339331 lies in dELS EH38E2496909, and HOXB13 has been reported in a GATA2/SMAD4/HOXB13 transcriptional complex at the rs339331/6q22 enhancer. | supported | [E03](#e03), [E06d](#e06d) |
| gene | RFX6 is the nearest gene and best L2G target of the credible sets containing this variant; E06d reports that the HOXB13-containing complex at this enhancer increases RFX6 expression. E20 found no significant GTEx v8 prostate eQTL for this variant, so direct prostate eQTL support is absent. | supported | [E02](#e02), [E05](#e05), [E06d](#e06d), [E20](#e20) |
| cell_type | HOXB13 is expressed in the prostate cancer LNCaP expression context at 182.31 TPM. E19 reports no ENCODE HOXB13 ChIP-seq peak containing rs339331 in LNCaP, with the caveat that absence can also mean no HOXB13 experiment in that biosample, so LNCaP-specific HOXB13 occupancy is not established. | weak | [E07](#e07), [E08](#e08), [E19](#e19) |
| phenotype | rs339331 at the RFX6/6q22 locus is associated with prostate cancer risk. The direction is problematic: if T binds HOXB13 more and the HOXB13 complex increases RFX6, T would be expected to be risk, but E04 reports C as the strongest prostate-cancer effect allele. | weak | [E04](#e04), [E05](#e05), [E06b](#e06b) |

Predictions: The T allele should have more HOXB13 occupancy than C at this enhancer.; If HOXB13 is activating, T should increase RFX6; if HOXB13 is repressive in this context, C with less HOXB13 could increase RFX6 and fit the C effect allele from E04.; This chain distinguishes itself from the AR chain by depending on HOXB13, not AR, for the allele-specific occupancy.

Falsified if: Allele-specific HOXB13 ChIP at rs339331 does not show T > C binding.; HOXB13 loss-of-function does not change RFX6 expression or enhancer activity from this element.; The HOXB13-containing complex is shown not to act at this enhancer or not to affect RFX6.

### 4. H3_IRF6_alt_C: IRF6 binds the C allele more at the rs339331 enhancer and may regulate RFX6 (p = 0.10)

TF IRF6 (stated coverage own_model; registry own_model), alt allele binds more; element dELS EH38E2496909; gene RFX6; cell type prostate cancer LNCaP clone FGC (ACH-000977) expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | IRF6 has an own QBiC-SELEX model in group G080; the best IRF6 model scores z 56.39 with effect 2.918, meaning the alt C allele binds IRF6 more strongly. Within G080, IRF6 is selected over IRF5 because IRF6 has the stronger own-model score and higher expression in the LNCaP context at 38.37 TPM versus IRF5 at 5.53 TPM. This is an in vitro binding prediction only. | weak | [E10](#e10) |
| element | rs339331 lies within the distal enhancer-like cCRE EH38E2496909, so an allele-specific IRF6 site could act through this element. No IRF6 occupancy or allele-specific activity at this element is shown. | weak | [E03](#e03) |
| gene | RFX6 is the nearest gene and the strongest L2G target in credible sets containing rs339331; however, direct IRF6-to-RFX6 regulatory evidence is not provided, and E20 found no significant GTEx v8 prostate eQTL for this variant. | weak | [E02](#e02), [E05](#e05), [E20](#e20) |
| cell_type | IRF6 is expressed in the supplied prostate cancer LNCaP expression context at 38.37 TPM, making it a candidate TF in this cell type. | supported | [E07](#e07), [E10](#e10) |
| phenotype | rs339331 is associated with prostate cancer risk, and E04 reports C as the strongest prostate-cancer effect allele, which matches the IRF6 alt-C binding direction if IRF6 is activating. | weak | [E04](#e04), [E05](#e05), [E06b](#e06b) |

Predictions: The C allele should increase IRF6 occupancy at the rs339331 enhancer.; If IRF6 activates RFX6, C should increase RFX6 expression and provide a straightforward C-risk-allele mechanism.; If IRF6 represses RFX6, the predicted direction of RFX6 expression would reverse.

Falsified if: Allele-specific IRF6 ChIP at rs339331 does not show C > T binding.; IRF6 perturbation does not change RFX6 expression or enhancer activity in prostate cancer cells.; IRF6 is not expressed or not active in the relevant prostate cancer cell type.

## Prediction matrix

| Test | Cost | Separates top two | H1_AR_ref_T | H4_null | H2_HOXB13_ref_T | H3_IRF6_alt_C |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific AR ChIP-qPCR at rs339331 in LNCaP or AR-expressing prostate cancer cells | low | yes | T > C AR occupancy | No allele-specific AR occupancy | No AR allele-specific occupancy expected | No AR allele-specific occupancy expected |
| Allele-specific HOXB13 ChIP-qPCR at rs339331 in LNCaP | low | no | No HOXB13 allele-specific occupancy required | No allele-specific HOXB13 occupancy | T > C HOXB13 occupancy | No HOXB13 allele-specific occupancy expected |
| Allele-specific IRF6 ChIP-qPCR at rs339331 in LNCaP | low | no | No IRF6 allele-specific occupancy expected | No allele-specific IRF6 occupancy | No IRF6 allele-specific occupancy expected | C > T IRF6 occupancy |
| rs339331 T/C reporter assay in LNCaP with AR knockdown | medium | yes | T allele drives AR-dependent enhancer activity, with direction depending on whether AR activates or represses RFX6 | No allelic difference | No AR-dependent allelic effect; HOXB13-dependent effect if HOXB13 is tested | C allele drives IRF6-dependent activity if IRF6 is activating |
| RFX6 allelic expression or perturbation assay in prostate cancer cells | high | yes | AR perturbation changes RFX6 expression in an rs339331-dependent manner | No rs339331-RFX6 regulatory effect | HOXB13 perturbation changes RFX6 expression in an rs339331-dependent manner | IRF6 perturbation changes RFX6 expression in an rs339331-dependent manner |
| Fine-mapping and LD analysis at 6q22 | high | yes | rs339331 remains credible as the causal variant | Causal variant is a linked variant, not rs339331 | rs339331 remains credible as the causal variant | rs339331 remains credible as the causal variant |

## Next experiment

Allele-specific AR ChIP-qPCR at rs339331 in LNCaP or another AR-expressing prostate cancer cell line, comparing T versus C occupancy. H1_AR_ref_T predicts T > C AR binding; H4_null predicts no allele-specific AR binding. This is cheaper than reporter, eQTL, or fine-mapping experiments and directly separates the top two chains by probability.

## Investigate calls

- chip_peaks({"biosample": "LNCaP", "tf": "AR"})
- chip_peaks({"biosample": "LNCaP", "tf": "HOXB13"})
- eqtl_lookup({"tissue": "prostate"})

## Flags

- coverage_misstated: H1_AR_ref_T: stated not_checked, registry says own_model for AR

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs339331&size=100; retrieved 2026-10-25T17:26:01+00:00)

> 13 GWAS Catalog associations for rs339331, strongest first:
> Prostate cancer: p 5.0e-20, effect allele C, risk-allele frequency 0.367114986, PMID 32514122
> Phospholipids in small HDL: p 2.0e-13, effect allele C, risk-allele frequency NR, PMID 41044249
> Total lipids in small HDL: p 2.0e-13, effect allele C, risk-allele frequency NR, PMID 41044249
> Concentration of small HDL particles: p 5.0e-12, effect allele C, risk-allele frequency NR, PMID 41044249
> Cholesterol in Small HDL: p 1.0e-11, effect allele C, risk-allele frequency NR, PMID 41044249
> Prostate-specific antigen levels: p 4.0e-09, effect allele T, risk-allele frequency NR, PMID 39930085

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:00+00:00)

> 95 credible sets contain 6_116888889_T_C: 94 GWAS, 1 molecular QTL.
> GWAS Cancer of prostate (PheCode 185): PIP 0.23; L2G RFX6 0.87, GPRC6A 0.05
> GWAS Prostate cancer: PIP 0.07; L2G RFX6 0.42, GPRC6A 0.12
> GWAS Prostate cancer: PIP 0.07; L2G RFX6 0.75, GPRC6A 0.06
> GWAS Prostate cancer: PIP 0.06; L2G RFX6 0.27, GPRC6A 0.16
> GWAS Prostate cancer: PIP 0.06; L2G RFX6 0.61
> GWAS Cancer of prostate (PheCode 185): PIP 0.06; L2G RFX6 0.75
> pqtl for SCG2 (UKB_PPP_EUR_SCG2_P13521_OID21400_v1): PIP 0.01
> Best L2G gene scores across these sets: RFX6 0.87, NUS1 0.55, GPRC6A 0.38, ROS1 0.11

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20AND%20RFX6%20AND%20%22prostate%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:07+00:00)

> Europe PMC: 67 hits for 'rs339331 AND RFX6 AND "prostate cancer"'; top 7 with PMIDs:
> PMID 41422049 (2025): Multifaceted functions of transcription regulatory factor X6 (RFX6): from pancreatic development to cancer progression.
> PMID 38932472 (2024): An Inherited Allele Confers Prostate Cancer Progression and Drug Resistance via RFX6/HOXA10-Orchestrated TGFβ Signaling.
> PMID 40181298 (2025): Genetic associations of prostate cancer in China: a systematic review.
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 41374944 (2025): The Clinical Relevance of Tumor Biomarkers in Prostate Cancer-A Review.
> PMID 38052806 (2023): Prostate cancer genetic risk and associated aggressive disease in men of African ancestry.
> PMID 41432001 (2026): Insights into human history and complex traits from the genomes of African populations.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41422049 (https://europepmc.org/article/MED/41422049; retrieved 2026-10-25T17:26:07+00:00)

> Dysregulated expression or mutations of the RFX6 gene in prostate cancer, hepatocellular carcinoma, gastric cancer, melanoma, and other tumors have garnered significant interest, with studies showing that such alterations affect tumor cell proliferation, migration, and invasion, and are correlated with an unfavorable clinical prognosis in patients carrying RFX6 mutations.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-25T17:26:07+00:00)

> Here the FinnGen cohort phenome-wide analysis, along with multiple genome-wide association studies, has consistently identified the rs339331-RFX6/6q22 locus associated with prostate cancer (PCa) risk across diverse populations.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-25T17:26:07+00:00)

> It is uncovered that rs339331 resides in a reprogrammed androgen receptor (AR) binding site in PCa tumors, with the T risk allele enhancing AR chromatin occupancy.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-25T17:26:07+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs339331/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.

<a id="e06e"></a>**E06e** literature_search, Europe PMC abstract, PMID 38052806 (https://europepmc.org/article/MED/38052806; retrieved 2026-10-25T17:26:07+00:00)

> Notable genes of interest include HCP5, RFX6 and H3C1 for risk, and MKI67 and KLF5 for aggressive disease.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr6:116888889:T>C: 997 models scored, 487 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 361 CIS-BP groups. Expression context: DepMap line ACH-000977. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 91 (Homeodomain, 3 models z -77.59, IRF, 2 models z 70.98, Unknown, 1 model z -31.89, bHLH, 1 model z 17.52, Unknown, 1 model z 17.51). Passing groups ranked below the ones shown: 260. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G024 (Homeodomain, 4 models): best model HOXB13_NA_TGCCTG20NGA_ESY_yang2017_0_3_7mer (own model of HOXB13), z -103.49, effect -4.771 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: HOXB13 z -103.49, HOXA13 z -74.87, HOXD13 z -69.26, HOXC13 z -64.27. TFs this group covers: HOXB13 (own model) 182.31 TPM, HOXC13 (own model) 4.13 TPM, HOXA13 (own model) 0.01 TPM, HOXD13 (own model) 0.01 TPM; best model's site strength: ref 99.9th, alt 97.2th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G004 (Homeodomain, 18 models): best model HOXC10_FL_TTGGCC40NTCG_KX_yin2017_0_3_7mer (own model of HOXC10), z -84.28, effect -4.457 (alt binds less); 18 passing models (18 with the best model's sign). Passing members: HOXC10 z -84.28, HOXD10 z -80.29, HOXC12 z -75.59, HOXC9 z -71.63, HOXD11 z -68.62 (+13 more). TFs this group covers: HOXC6 (mapped) 18.43 TPM, MNX1 (own model) 8.35 TPM, HOXC12 (own model) 6.33 TPM, HOXC4 (own model) 5.27 TPM, HOXA10 (own model) 4.23 TPM, HOXA6 (own model) 2.75 TPM, HOXA5 (own model) 1.94 TPM, HOXC10 (own model) 1.89 TPM, HOXC9 (own model) 1.78 TPM, HOXB9 (own model) 1.77 TPM (+24 more); best model's site strength: ref 100.0th, alt 89.4th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G080 (IRF, 2 models): best model IRF6_eDBD_TCTAGT40NAAC_KS_yin2017_0_4_7mer (own model of IRF6), z 56.39, effect 2.918 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: IRF6 z 56.39, IRF5 z 16.69. TFs this group covers: IRF6 (own model) 38.37 TPM, IRF5 (own model) 5.53 TPM; best model's site strength: ref 73.0th, alt 98.5th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G302 (C2H2 ZF, 1 model): best model PRDM4_eDBD_TAAATC40NGTT_KT_yin2017_0_4_7mer (own model of PRDM4), z 47.33, effect 3.137 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: PRDM4 z 47.33. TFs this group covers: PRDM4 (own model) 10.83 TPM; best model's site strength: ref 99.3th, alt 100.0th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G213 (IRF, 1 model): best model IRF3_eDBD_TGAGAA40NGCG_KS_yin2017_0_4_7mer (own model of IRF3), z 44.89, effect 2.092 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: IRF3 z 44.89. TFs this group covers: IRF3 (own model) 54.41 TPM; best model's site strength: ref 80.5th, alt 100.0th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G228 (bHLH, 1 model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (own model of MAX), z 28.99, effect 1.595 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: MAX z 28.99. TFs this group covers: MAX (own model) 61.61 TPM; best model's site strength: ref 63.6th, alt 96.8th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G212 (IRF, 1 model): best model IRF2_FL_TTCATT40NTAT_KX_yin2017_0_3_7mer (own model of IRF2), z 25.39, effect 2.187 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: IRF2 z 25.39. TFs this group covers: IRF2 (own model) 8.32 TPM, IRF1 (mapped) 5.75 TPM; best model's site strength: ref 89.1th, alt 99.1th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G460 (C2H2 ZF, 1 model): best model ZNF230_FL_TG40NGACCTT_YWDA_jolma2025_0_3_7mer (own model of ZNF230), z -23.63, effect -0.439 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF230 z -23.63. TFs this group covers: ZNF230 (own model) 1.65 TPM; best model's site strength: ref 98.9th, alt 93.9th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G367 (Unknown, 1 model): best model THYN1_FL_TG40NCTGTGG_YWFA_jolma2025_0_4_7mer (own model of THYN1), z 22.24, effect 0.173 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: THYN1 z 22.24. TFs this group covers: THYN1 (own model) 37.42 TPM; best model's site strength: ref 36.3th, alt 74.1th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G467 (C2H2 ZF, 1 model): best model ZNF260_FL_AT40NCCTTGG_AATA_jolma2025_0_3_7mer (own model of ZNF260), z -20.85, effect -0.516 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF260 z -20.85. TFs this group covers: ZNF260 (own model) 13.26 TPM; best model's site strength: ref 99.5th, alt 92.9th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:23+00:00)

> No ENCODE AR ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP'. Absence can also mean no AR experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:22+00:00)

> No ENCODE HOXB13 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP'. Absence can also mean no HOXB13 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'prostate'. NES is the effect of the alt allele (C) relative to ref (T).
