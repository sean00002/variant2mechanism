# rs339331 and Prostate cancer (6q22)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 7 model calls; 217 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. hypothesis_1: AR binds the ref T allele at the rs339331 enhancer; if AR is repressive, the alt C allele derepresses RFX6 and is risk-associated (p = 0.35)

TF AR (stated coverage not_checked; registry own_model), ref allele binds more; element distal enhancer-like cCRE EH38E2496909; gene RFX6; cell type prostate cancer/epithelial cells, with LNCaP as an extrapolation.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR occupies the rs339331 enhancer allele-specifically, with the ref T allele binding AR more strongly than the alt C allele; this is reported in E06c, while E08 does not provide an AR ChIP-seq peak in LNCaP. | supported | [E06c](#e06c), [E08](#e08) |
| element | rs339331 lies inside the distal enhancer-like cCRE EH38E2496909 and is described as a reprogrammed AR-bound prostate cancer enhancer. | supported | [E03](#e03), [E06c](#e06c) |
| gene | The rs339331 enhancer is assigned to RFX6 by proximity, L2G, and 6q22 literature, but AR-specific regulation of RFX6 is not directly shown and GTEx prostate has no significant rs339331 eQTL. | weak | [E02](#e02), [E05](#e05), [E06b](#e06b), [E06d](#e06d), [E07](#e07) |
| cell_type | Prostate cancer cells/tumors are the reported context for AR occupancy at rs339331; LNCaP is an extrapolation because E08 lacks an AR peak there. | weak | [E06c](#e06c), [E06d](#e06d), [E08](#e08) |
| phenotype | The alt C allele is the prostate-cancer effect allele in E04; if AR binding at the ref T allele is repressive, loss of AR on C would increase RFX6 and risk, consistent with RFX6/6q22 association with prostate cancer. | weak | [E04](#e04), [E05](#e05), [E06a](#e06a), [E06b](#e06b) |

Predictions: Allele-specific AR ChIP in a heterozygous prostate cancer line should show higher AR occupancy on the ref T allele at rs339331.; If AR is repressive at this element, AR depletion or inhibition should increase RFX6 expression.; An allele-specific RFX6 reporter should show higher RFX6 expression from the alt C allele than from the ref T allele if AR repression is the mechanism.

Falsified if: allele-specific AR ChIP or reporter assays show no stronger AR occupancy on the ref T allele at rs339331; AR perturbation does not change RFX6 expression in the direction required by this model; the alt C allele is shown to lower RFX6 and be protective despite being the E04 prostate-cancer effect allele, which would make the derepression model untenable

### 2. hypothesis_2: HOXB13 within the GATA2/SMAD4/HOXB13 complex binds the ref T allele and activates RFX6 (p = 0.27)

TF HOXB13 (stated coverage not_checked; registry own_model), ref allele binds more; element rs339331-containing distal enhancer EH38E2496909; gene RFX6; cell type prostate cancer cells/tumors.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 is reported in a GATA2/SMAD4/HOXB13 complex at the rs339331 enhancer, but allele-specific HOXB13 binding is not measured; ref T over alt C is a model, and E09 shows no HOXB13 ChIP-seq peak in LNCaP. | weak | [E06d](#e06d), [E09](#e09) |
| element | rs339331 is inside the dELS EH38E2496909, and a HOXB13-containing transcriptional complex is reported at this prostate cancer risk enhancer. | supported | [E03](#e03), [E06d](#e06d) |
| gene | The GATA2/SMAD4/HOXB13 complex at rs339331 is reported to increase RFX6 expression, and L2G independently prioritizes RFX6. | supported | [E05](#e05), [E06d](#e06d) |
| cell_type | The rs339331 enhancer and RFX6 regulation were described in prostate cancer cells/tumors. | supported | [E06c](#e06c), [E06d](#e06d) |
| phenotype | RFX6/6q22 is associated with prostate cancer risk and RFX6 dysregulation is linked to cancer, but if HOXB13 activates RFX6, the ref T allele should raise RFX6 and risk, conflicting with E04 listing C as the prostate-cancer effect allele. | missing | [E04](#e04), [E05](#e05), [E06a](#e06a), [E06b](#e06b) |

Predictions: Allele-specific HOXB13 ChIP or reporter assays should show stronger HOXB13 occupancy on the ref T allele at rs339331.; HOXB13 knockdown should lower RFX6 expression in prostate cancer cells.; If HOXB13 activates RFX6, the ref T allele should associate with higher RFX6 expression, which is in tension with E04 if C is the prostate-cancer risk allele.

Falsified if: allele-specific HOXB13 ChIP or reporter assays show no differential HOXB13 binding at rs339331; HOXB13 loss does not reduce RFX6 expression in prostate cancer cells; the GATA2/SMAD4/HOXB13 complex is shown not to occupy this cCRE or not to regulate RFX6

### 3. hypothesis_4: Null: no direct TF-mediated effect of rs339331 (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs339331 in prostate cancer cells.; The GWAS signal is explained by a linked causal variant, a passenger mutation, or no direct allelic effect of this base change.; RFX6 expression is not directly affected by the T-to-C change at rs339331.

Falsified if: allele-specific TF ChIP or reporter assays show differential binding at rs339331 in prostate cancer cells; CRISPR base editing at rs339331 alone changes RFX6 expression or a prostate cancer phenotype; fine-mapping shows rs339331 itself is the causal variant rather than a linked variant

### 4. hypothesis_3: GATA2 binds the alt C allele in the rs339331 enhancer complex and activates RFX6 (p = 0.13)

TF GATA2 (stated coverage not_checked; registry own_model), alt allele binds more; element rs339331-containing distal enhancer EH38E2496909; gene RFX6; cell type prostate cancer cells/tumors.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is reported in the GATA2/SMAD4/HOXB13 complex at rs339331, but allele-specific GATA2 binding is not measured; alt C over ref T is a model, not established. | weak | [E06d](#e06d) |
| element | rs339331 lies in the dELS EH38E2496909, and a GATA2-containing transcriptional complex is reported at this enhancer. | supported | [E03](#e03), [E06d](#e06d) |
| gene | The GATA2-containing complex at rs339331 is reported to increase RFX6 expression, and L2G prioritizes RFX6. | supported | [E05](#e05), [E06d](#e06d) |
| cell_type | The relevant context is prostate cancer cells/tumors, where the rs339331 enhancer complex and RFX6 regulation were described. | supported | [E06c](#e06c), [E06d](#e06d) |
| phenotype | The alt C allele is the E04 prostate-cancer effect allele; GATA2 activation on C would increase RFX6 and fit the association, although direct perturbation evidence is lacking. | weak | [E04](#e04), [E05](#e05), [E06a](#e06a), [E06b](#e06b) |

Predictions: Allele-specific GATA2 ChIP or reporter assays should show stronger GATA2 occupancy on the alt C allele at rs339331.; GATA2 knockdown should reduce RFX6 expression in prostate cancer cells.; The alt C allele should associate with higher RFX6 expression if GATA2-mediated activation is causal.

Falsified if: GATA2 ChIP or reporter assays show no allele-specific GATA2 binding at rs339331; GATA2 knockdown does not change RFX6 expression in prostate cancer cells; GATA2 is shown not to be part of the functional complex at this enhancer

## Prediction matrix

| Test | Cost | Separates top two | hypothesis_1 | hypothesis_2 | hypothesis_4 | hypothesis_3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific AR ChIP-qPCR at rs339331 in a heterozygous prostate cancer line such as LNCaP | medium | yes | AR occupancy is higher on the ref T allele at rs339331. | No AR occupancy or no AR allele-specific effect at rs339331. | No allele-specific TF binding at rs339331. | No AR occupancy or no AR allele-specific effect at rs339331. |
| Allele-specific HOXB13 ChIP-qPCR at rs339331 in a heterozygous prostate cancer line | medium | yes | No HOXB13 occupancy or no HOXB13 allele-specific effect at rs339331. | HOXB13 occupancy is higher on the ref T allele at rs339331. | No allele-specific TF binding at rs339331. | No HOXB13 occupancy or no HOXB13 allele-specific effect at rs339331. |
| Allele-specific GATA2 ChIP-qPCR at rs339331 in a heterozygous prostate cancer line | medium | no | No GATA2 occupancy or no GATA2 allele-specific effect at rs339331. | No GATA2 occupancy or no GATA2 allele-specific effect at rs339331. | No allele-specific TF binding at rs339331. | GATA2 occupancy is higher on the alt C allele at rs339331. |
| Allele-specific RFX6 reporter assay in prostate cancer cells, or a well-powered prostate eQTL analysis | low | yes | If AR is repressive, the alt C allele gives higher RFX6 expression than ref T. | The ref T allele gives higher RFX6 expression than alt C. | No allele-specific difference in RFX6 expression. | The alt C allele gives higher RFX6 expression than ref T. |
| CRISPR base editing of rs339331 from T to C in a heterozygous prostate cancer cell line | high | yes | Editing T to C reduces AR occupancy and, if AR is repressive, increases RFX6 expression. | Editing T to C reduces HOXB13 occupancy and lowers RFX6 expression. | Editing T to C has no effect on TF occupancy or RFX6 expression. | Editing T to C increases GATA2 occupancy and increases RFX6 expression. |

## Next experiment

The single cheapest experiment separating the top two chains (hypothesis_1 AR vs hypothesis_2 HOXB13) is allele-specific AR ChIP-qPCR at rs339331 in a heterozygous prostate cancer line such as LNCaP: hypothesis_1 predicts AR occupancy higher on ref T, whereas hypothesis_2 predicts no AR occupancy or no AR allele-specific effect at this element.

## Investigate calls

- eqtl_lookup({"tissue": "Prostate"})
- chip_peaks({"biosample": "LNCaP", "tf": "AR"})
- chip_peaks({"biosample": "LNCaP", "tf": "HOXB13"})

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

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:23+00:00)

> No ENCODE AR ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP'. Absence can also mean no AR experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:22+00:00)

> No ENCODE HOXB13 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP'. Absence can also mean no HOXB13 experiment in that biosample. 0 peaks lie within 100 bp without containing it.
