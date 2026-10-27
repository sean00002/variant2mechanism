# rs339331 and Prostate cancer (6q22)

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 172 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. H0: No TF-mediated effect at this variant (p = 0.83)

Null chain: no TF-mediated effect of this variant.

Predictions: The T>C change has no TF-mediated regulatory effect. The prostate-cancer association could arise from linkage to another causal variant or another mechanism.; Allele-specific PKNOX1 binding and precise editing of this base will not produce a reproducible, PKNOX1-dependent expression change in a relevant prostate model.

Falsified if: Precise T/C editing reproducibly changes TF binding and target-gene expression, and the effect depends on PKNOX1 or another identified TF.

### 2. H1: Hypothesized PKNOX1 binding increase and RFX6 activation (p = 0.11)

TF PKNOX1 (QBiC-SELEX coverage own_model), alt allele binds more; element cCRE EH38E2496909, a distal enhancer-like element; gene RFX6; cell type Prostate cancer cells; activity and PKNOX1 occupancy at this element in prostate cells are unestablished..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | PKNOX1 is a candidate because it is the only reported TF with a binding model that is both bound at the variant and expressed above 1 TPM; MEIS2 is reported below 1 TPM. However, the PKNOX1 peak is only in HEK293T, not LNCaP, and no PKNOX1 QBiC-SELEX result or allele-specific binding evidence is supplied. C-more-than-T binding is a speculative direction, not an observed result. | missing | [E04](#e04), [E05](#e05) |
| element | The variant lies in distal enhancer-like cCRE EH38E2496909, but the reported chromatin scores are maxima across biosamples and do not establish activity in prostate cells. | supported | [E03](#e03) |
| gene | RFX6 is a candidate target because it is near the variant and is repeatedly favored by credible-set gene prioritization. Direct regulation by this cCRE is not shown, and there is no significant GTEx prostate eQTL for the variant. | supported | [E02](#e02), [E07](#e07), [E10](#e10) |
| cell_type | A prostate-cell mechanism is hypothesized, not demonstrated: PKNOX1 is expressed in LNCaP, but no matching-biosample peak over the variant is reported, and prostate-specific cCRE activity is not established. | weak | [E03](#e03), [E04](#e04), [E05](#e05) |
| phenotype | If C increases RFX6 activity, this could be consistent with the reported C risk allele and literature linking RFX6 to prostate-cancer progression. The supplied evidence does not show that this variant changes RFX6 or that such a change mediates risk. | weak | [E06](#e06), [E09b](#e09b), [E09c](#e09c), [E11](#e11) |

Predictions: In a relevant prostate model, the C allele will bind PKNOX1 more strongly than T; if the element is active, editing T to C will increase RFX6 expression.; The expression effect will depend on PKNOX1 or the cCRE and will be more evident for RFX6 than for GPRC6A.

Falsified if: A PKNOX1 allele-specific binding assay shows equal binding or stronger binding to T.; Precise T/C editing produces no RFX6 change, or any RFX6 change is not dependent on PKNOX1 or the cCRE.

### 3. H2: Hypothesized PKNOX1 binding decrease and RFX6 reduction (p = 0.04)

TF PKNOX1 (QBiC-SELEX coverage own_model), ref allele binds more; element cCRE EH38E2496909, a distal enhancer-like element; gene RFX6; cell type Prostate cancer cells; activity and PKNOX1 occupancy at this element in prostate cells are unestablished..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | PKNOX1 is a candidate because it is the only reported TF with a binding model that is both bound at the variant and expressed above 1 TPM; MEIS2 is reported below 1 TPM. The PKNOX1 peak is only in HEK293T, not LNCaP, and no PKNOX1 QBiC-SELEX result or allele-specific binding evidence is supplied. T-more-than-C binding is a speculative direction. | missing | [E04](#e04), [E05](#e05) |
| element | The variant lies in distal enhancer-like cCRE EH38E2496909, but the reported chromatin scores do not establish that it is active in prostate cells. | supported | [E03](#e03) |
| gene | RFX6 is a candidate target based on proximity and repeated credible-set prioritization, but direct regulation by this cCRE is unproven and no significant GTEx prostate eQTL is reported. | supported | [E02](#e02), [E07](#e07), [E10](#e10) |
| cell_type | A prostate-cell mechanism is hypothesized, not demonstrated: PKNOX1 is expressed in LNCaP, but no matching-biosample peak over the variant is reported, and prostate-specific cCRE activity is not established. | weak | [E03](#e03), [E04](#e04), [E05](#e05) |
| phenotype | This model predicts that C reduces RFX6. That direction is not supported by the supplied evidence and may conflict with literature describing RFX6 as promoting prostate-cancer progression; the variant's risk association alone does not establish this mechanism. | missing | [E06](#e06), [E09b](#e09b), [E09c](#e09c), [E11](#e11) |

Predictions: In a relevant prostate model, the T allele will bind PKNOX1 more strongly than C; if the element is active, editing T to C will reduce RFX6 expression.; Any RFX6 expression difference will depend on PKNOX1 or the cCRE.

Falsified if: A PKNOX1 allele-specific binding assay shows equal binding or stronger binding to C.; Precise T/C editing does not reduce RFX6 expression, or any expression change is not dependent on PKNOX1 or the cCRE.

### 4. H3: Hypothesized PKNOX1-mediated regulation of GPRC6A (p = 0.02)

TF PKNOX1 (QBiC-SELEX coverage own_model), alt allele binds more; element cCRE EH38E2496909, a distal enhancer-like element; gene GPRC6A; cell type Prostate cancer cells; activity and PKNOX1 occupancy at this element in prostate cells are unestablished..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | PKNOX1 is a candidate because it is the only reported TF with a binding model that is both bound at the variant and expressed above 1 TPM; MEIS2 is reported below 1 TPM. The PKNOX1 peak is only in HEK293T, not LNCaP, and no PKNOX1 QBiC-SELEX result or allele-specific binding evidence is supplied. C-more-than-T binding is speculative. | missing | [E04](#e04), [E05](#e05) |
| element | The variant lies in distal enhancer-like cCRE EH38E2496909, but its activity in prostate cells is not established. | supported | [E03](#e03) |
| gene | GPRC6A is nearby and is a possible target, but credible-set gene prioritization favors RFX6 and direct regulation of GPRC6A by this cCRE is not shown. | weak | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | A prostate-cell mechanism is hypothesized, not demonstrated: no matching-biosample LNCaP peak over the variant or prostate-specific cCRE activity is reported. | missing | [E03](#e03), [E04](#e04) |
| phenotype | The variant is associated with prostate cancer, and GPRC6A has a modest overall gene-disease score that is mostly literature-based. The supplied evidence does not establish a GPRC6A-mediated effect of this variant on prostate-cancer risk. | weak | [E06](#e06), [E12](#e12) |

Predictions: In a relevant prostate model, the C allele will bind PKNOX1 more strongly than T and alter GPRC6A expression, with no corresponding RFX6 expression change.; Editing the variant or perturbing the cCRE will affect GPRC6A more than RFX6.

Falsified if: A PKNOX1 allele-specific binding assay shows equal binding or stronger binding to T.; Precise T/C editing or cCRE perturbation affects RFX6 but not GPRC6A.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Compare T- and C-allele PKNOX1 binding by EMSA using the two variant-containing DNA probes. | low | yes | No reproducible allele-specific PKNOX1 binding difference. | C probe binds PKNOX1 more strongly. | T probe binds PKNOX1 more strongly. | C probe binds PKNOX1 more strongly. |
| Precisely edit T to C (and the reciprocal edit where feasible) in a prostate cancer cell model; measure RFX6 and GPRC6A expression, with and without PKNOX1 perturbation. | high | no | No reproducible, PKNOX1-dependent expression difference attributable to the edited base. | C increases RFX6 expression, and the difference is reduced by PKNOX1 perturbation. | C decreases RFX6 expression, and the difference is reduced by PKNOX1 perturbation. | C alters GPRC6A expression more than RFX6, with the difference reduced by PKNOX1 perturbation. |
| Measure allele-specific PKNOX1 occupancy at the cCRE in a prostate model heterozygous for the variant, alongside local chromatin accessibility. | medium | yes | No reproducible allele-specific PKNOX1 occupancy attributable to this base. | Greater PKNOX1 occupancy on C, with the cCRE accessible in the tested cells. | Greater PKNOX1 occupancy on T, with the cCRE accessible in the tested cells. | Greater PKNOX1 occupancy on C, with the cCRE accessible in the tested cells. |

## Next experiment

Run the low-cost allele-specific PKNOX1 EMSA using otherwise identical T- and C-containing probes. Stronger binding to C would favor H1 over H2; stronger binding to T would favor H2. This tests the top two chains' differing binding-direction predictions, but would not establish PKNOX1 occupancy or regulatory activity in prostate cells.

## Investigate calls

- eqtl_lookup({"tissue": "Prostate"})
- gene_disease({"gene": "RFX6"})
- gene_disease({"gene": "GPRC6A"})

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

<a id="e10"></a>**E10** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e11"></a>**E11** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T20:19:57+00:00)

> Open Targets: RFX6 and prostate cancer (MONDO_0008315), overall score 0.41; by evidence type: genetic_association 0.66, literature 0.22

<a id="e12"></a>**E12** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T20:19:57+00:00)

> Open Targets: GPRC6A and prostate cancer (MONDO_0008315), overall score 0.12; by evidence type: literature 0.80, genetic_association 0.12
