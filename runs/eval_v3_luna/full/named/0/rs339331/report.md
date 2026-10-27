# rs339331 and Prostate cancer (6q22)

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 9 model calls; 268 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: PKNOX1 (bound elsewhere, z 11.43, weak site). Occupancy unknown: HOXC13 (z -103.49); HOXA6 (z -84.28); HOXB9 (z -84.28); HOXC12 (z -84.28); HOXC6 (z -84.28). Diagnostic, not shown to the model: 487 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: HOXB13-associated enhancer activity increases RFX6 from the T allele (p = 0.75)

TF HOXB13 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E2496909, which the literature describes as an rs339331-associated enhancer.; gene RFX6; cell type Prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The literature reports greater HOXB13 binding at the T reference allele than at C; no HOXB13-specific QBiC-SELEX result is supplied, so this direction rests on the reported cellular evidence. | weak | [E19c](#e19c), [E19e](#e19e) |
| element | rs339331 lies in enhancer-like cCRE EH38E2496909, and the literature reports regulatory potential at the rs339331 region. | supported | [E03](#e03), [E19d](#e19d), [E19e](#e19e) |
| gene | The literature reports that the T allele increases RFX6 transcription, supporting RFX6 as a target of the rs339331 region, although it does not isolate HOXB13 as the sole mediator. | supported | [E19c](#e19c), [E19e](#e19e) |
| cell_type | The proposed effect is in prostate cancer cells; the cited studies report an rs339331 enhancer mechanism and HOXB13 binding in that disease context, but the supplied LNCaP ChIP-seq search shows no peak at the variant. | weak | [E04](#e04), [E19c](#e19c), [E19e](#e19e) |
| phenotype | The reported T-associated increase in RFX6 is a plausible contributor to prostate cancer susceptibility, but the supplied evidence does not establish that this mechanism alone causes the association. | weak | [E06](#e06), [E09b](#e09b), [E19e](#e19e) |

Predictions: In a relevant prostate cancer model, HOXB13 depletion should reduce the rs339331-dependent component of RFX6 expression; the T allele should show greater HOXB13 occupancy than C.; Editing T to C should reduce RFX6 expression if the reported allele-specific enhancer effect is reproduced.

Falsified if: A sensitive assay in a relevant prostate cancer model finds no HOXB13 occupancy at the element, and HOXB13 perturbation does not affect RFX6.; Isogenic T-to-C editing reproducibly leaves RFX6 expression unchanged in an appropriate model.

### 2. H4: No TF-mediated effect of rs339331 (p = 0.12)

Null chain: no TF-mediated effect of this variant.

Predictions: The association may reflect linkage to another causal variant, or rs339331 may not have a causal TF-mediated allelic effect.; Reported enhancer activity and allele-specific findings may not reproduce in the relevant disease context.

Falsified if: Isogenic editing of rs339331 produces a reproducible allele-dependent change in RFX6 regulation in a relevant prostate cancer model, with dependence on the implicated TF.

### 3. H3: AR occupancy is greater on the T allele (p = 0.08)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E2496909, and the literature places it in a reprogrammed AR-binding site in prostate cancer tumors.; gene RFX6; cell type Prostate cancer tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The literature reports greater AR chromatin occupancy on T than C in prostate cancer tumors, but the AR-specific QBiC-SELEX model shows no clear allelic change; the occupancy direction is therefore supported by the tumor report, not by QBiC-SELEX. | weak | [E17](#e17), [E19b](#e19b) |
| element | The variant falls within enhancer-like cCRE EH38E2496909, which the literature describes as an AR-binding site in prostate cancer tumors. | supported | [E03](#e03), [E19b](#e19b) |
| gene | RFX6 is prioritized at this locus, but the supplied evidence does not directly show that AR occupancy at rs339331 regulates RFX6. | weak | [E02](#e02), [E07](#e07), [E19b](#e19b) |
| cell_type | The AR occupancy claim is reported in prostate cancer tumors; the supplied matching LNCaP ChIP-seq search found no peak at the variant. | supported | [E04](#e04), [E19b](#e19b) |
| phenotype | The locus is associated with prostate cancer, and the literature calls T the risk allele, but a causal AR-to-RFX6 path is not established; the GWAS effect-allele entry alone does not specify risk direction. | weak | [E06](#e06), [E07](#e07), [E19b](#e19b) |

Predictions: Allele-resolved AR assays in prostate tumors should reproduce greater occupancy on T than C, even though the supplied AR QBiC-SELEX model does not predict a clear change.; If AR mediates the RFX6 effect, AR perturbation should alter rs339331-dependent RFX6 regulation.

Falsified if: Relevant tumor assays fail to reproduce greater AR occupancy on T than C.; AR perturbation has no effect on RFX6 regulation attributable to the rs339331 region.

### 4. H2: HOXC13 binding could contribute to enhancer activity (p = 0.05)

TF HOXC13 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E2496909; whether HOXC13 occupies this element is unknown.; gene RFX6; cell type LNCaP-like prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXC13's own QBiC-SELEX model predicts stronger in-vitro binding to T than C, but occupancy at the variant is unknown; this is distinct from the literature's HOXB13 result and does not establish HOXC13 binding in cells. | weak | [E12](#e12), [E18](#e18) |
| element | The variant lies within enhancer-like cCRE EH38E2496909, but the supplied evidence does not demonstrate HOXC13 occupancy there. | supported | [E03](#e03), [E12](#e12), [E18](#e18) |
| gene | RFX6 is a candidate target at this locus, but no supplied evidence directly links HOXC13 binding to RFX6 regulation. | weak | [E02](#e02), [E07](#e07) |
| cell_type | HOXC13 is expressed in the LNCaP context, but its occupancy or activity at this site is not shown. | supported | [E04](#e04), [E12](#e12) |
| phenotype | A HOXC13-mediated effect on RFX6 could contribute to prostate cancer susceptibility, but this chain is speculative because occupancy and regulatory activity are unverified. | weak | [E06](#e06), [E07](#e07), [E12](#e12), [E18](#e18) |

Predictions: If HOXC13 occupies the site, allele-resolved assays should show greater binding on T than C, consistent with its own QBiC-SELEX model.; HOXC13 depletion should alter the rs339331-dependent component of RFX6 expression if this chain is correct.

Falsified if: Relevant prostate cancer cells show no HOXC13 occupancy at the element despite adequate assay sensitivity.; HOXC13 perturbation has no allele-dependent effect on RFX6 regulation.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| In a relevant prostate cancer model, separately deplete HOXB13 and HOXC13 and measure RFX6 expression, including the rs339331-dependent component. | medium | yes | HOXB13 depletion reduces the rs339331-dependent RFX6 component more than HOXC13 depletion. | Neither HOXB13 nor HOXC13 depletion produces a reproducible rs339331-dependent change in RFX6. | Neither HOXB13 nor HOXC13 depletion is the primary predicted effect; AR perturbation should alter the rs339331-dependent component. | HOXC13 depletion reduces the rs339331-dependent RFX6 component; HOXB13 depletion is not the primary predicted dependency. |
| Measure allele-resolved HOXB13, HOXC13, and AR occupancy at rs339331 in prostate cancer tumor material or a relevant model. | medium | yes | HOXB13 occupancy is greater on T than C. | No reproducible allele-specific occupancy associated with a causal TF mechanism. | AR occupancy is greater on T than C. | HOXC13 occupancy is detectable and greater on T than C. |
| Use isogenic T-to-C editing in a prostate cancer model and measure RFX6 expression. | high | no | Changing T to C reduces RFX6 expression if the reported allele-specific enhancer effect is reproduced. | Changing T to C does not produce a reproducible RFX6 expression change. | Changing T to C alters RFX6 expression in an AR-dependent manner. | Changing T to C alters RFX6 expression if the HOXC13-associated enhancer effect is reproduced; the direction of the expression change is not established by its binding prediction alone. |

## Next experiment

In a relevant prostate cancer model, separately deplete HOXB13 and HOXC13 and measure the rs339331-dependent component of RFX6 expression. This medium-cost perturbation test most directly distinguishes the top two chains.

## Investigate calls

- qbic_tf_detail({"tf": "AR"})
- qbic_tf_detail({"tf": "HOXC13"})
- literature_search({"query": "rs339331 RFX6 prostate cancer allele-specific enhancer reporter expression AR"})

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

> {"tf":"AR","symbol":"AR","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr6:116888889:T>C","gate_p":5.02e-05,"models":[{"model":"AR_NA_TGCTCG20NGA_AF_jolma2013_1_3_7mer","mapping":"own","group":"G016 Nuclear receptor, 4 models","quality":0.601,"effect":0.035,"z":0.94,"p":0.35,"rank_abs_z":"866/997","passed_gate":false,"site_strength":{"ref_percentile":70.4,"alt_percentile":83.3,"k":7}},{"model":"GR_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer","mapping":"CIS-BP (NR3C1)","group":"G016 Nuclear receptor, 4 models","quality":0.913,"effect":0.083,"z":1.44,"p":0.15,"rank_abs_z":"799/997","passed_gate":false,"site_strength":{"ref_percentile":65.9,"alt_percentile":74.5,"k":7}},{"model":"NR3C2_eDBD_TGCTGG40NGCC_KT_yin2017_0_4_7mer","mapping":"CIS-BP (NR3C2)","group":"G016 Nuclear receptor, 4 models","quality":0.751,"effect":0.811,"z":9.5,"p":2e-21,"rank_abs_z":"135/997","passed_gate":true,"site_strength":{"ref_percentile":64.7,"alt_percentile":83.6,"k":7}},{"model":"PGR_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (PGR)","group":"G016 Nuclear receptor, 4 models","quality":0.544,"effect":0.108,"z":2.46,"p":0.014,"rank_abs_z":"660/997","passed_gate":false,"site_strength":{"ref_percentile":65.1,"alt_percentile":80.1,"k":7}}]}

<a id="e18"></a>**E18** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"HOXC13","symbol":"HOXC13","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr6:116888889:T>C","gate_p":5.02e-05,"models":[{"model":"HOXC13_NA_TCCCTC20NTCC_ESY_yang2017_0_3_7mer","mapping":"own","group":"G024 Homeodomain, 4 models","quality":0.855,"effect":-2.96,"z":-64.27,"p":0.0,"rank_abs_z":"11/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":91.9,"k":7}},{"model":"HOXA13_eDBD_TACTGA40NACC_KP_yin2017_1_2_7mer","mapping":"CIS-BP (HOXA13)","group":"G024 Homeodomain, 4 models","quality":0.643,"effect":-0.723,"z":-74.87,"p":0.0,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":78.0,"k":7}},{"model":"HOXB13_NA_TGCCTG20NGA_ESY_yang2017_0_3_7mer","mapping":"CIS-BP (HOXB13)","group":"G024 Homeodomain, 4 models","quality":0.914,"effect":-4.771,"z":-103.49,"p":0.0,"rank_abs_z":"1/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":97.2,"k":7}},{"model":"HOXD13_NA_TGATAA20NATA_ESAC_yang2017_0_4_7mer","mapping":"CIS-BP (HOXD13)","group":"G024 Homeodomain, 4 models","quality":0.696,"effect":-3.437,"z":-69.26,"p":0.0,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":92.8,"k":7}}]}

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20RFX6%20prostate%20cancer%20allele-specific%20enhancer%20reporter%20expression%20AR&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:33:37+00:00)

> Europe PMC: 12 hits for 'rs339331 RFX6 prostate cancer allele-specific enhancer reporter expression AR'; top 8 with PMIDs:
> PMID 38932472 (2024): An Inherited Allele Confers Prostate Cancer Progression and Drug Resistance via RFX6/HOXA10-Orchestrated TGFβ Signaling.
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 36428729 (2022): SNP-Target Genes Interaction Perturbing the Cancer Risk in the Post-GWAS.
> PMID 32443951 (2020): Enhancer Predictions and Genome-Wide Regulatory Circuits.
> PMID 32472759 (2020): Beyond the coding genome: non-coding mutations and cancer.
> PMID 26398868 (2015): CAUSEL: an epigenome- and genome-editing pipeline for establishing function of noncoding GWAS variants.
> PMID 27409348 (2016): Identification and validation of regulatory SNPs that modulate transcription factor chromatin binding and gene expression in prostate cancer.
> PMID 28120510 (2017): Predicting enhancer activity and variant impact using gkm-SVM.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T13:33:37+00:00)

> Here the FinnGen cohort phenome-wide analysis, along with multiple genome-wide association studies, has consistently identified the rs339331-RFX6/6q22 locus associated with prostate cancer (PCa) risk across diverse populations.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T13:33:37+00:00)

> It is uncovered that rs339331 resides in a reprogrammed androgen receptor (AR) binding site in PCa tumors, with the T risk allele enhancing AR chromatin occupancy.

<a id="e19c"></a>**E19c** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T13:33:37+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs339331/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.

<a id="e19d"></a>**E19d** literature_search, Europe PMC abstract, PMID 26398868 (https://europepmc.org/article/MED/26398868; retrieved 2026-10-26T13:33:37+00:00)

> Epigenome editing confirmed that the rs339331 region possessed regulatory potential.

<a id="e19e"></a>**E19e** literature_search, Europe PMC abstract, PMID 26398868 (https://europepmc.org/article/MED/26398868; retrieved 2026-10-26T13:33:37+00:00)

> Introduction of the 'T' risk allele increased transcription of the regulatory factor 6 (RFX6) gene, increased homeobox B13 (HOXB13) binding at the rs339331 region, and increased deposition of the enhancer-associated H3K4me2 histone mark at the rs339331 region compared to lines homozygous for the 'C' protective allele.
