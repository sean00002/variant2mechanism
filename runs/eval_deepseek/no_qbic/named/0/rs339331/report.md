# rs339331 and Prostate cancer (6q22)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 10 model calls; 210 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. H4: AR binds the ref T allele more but is repressive/competitive; the alt C allele permits enhancer activation of RFX6 and matches C as the GWAS risk allele (p = 0.46)

TF AR (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E2496909 dELS; gene RFX6; cell type prostate cancer / LNCaP-like prostate tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR binds more strongly to the ref T allele than to the alt C allele at rs339331; E06c reports T-enhanced AR chromatin occupancy. H4 uses this as occupancy evidence only and proposes that AR is repressive or competes with an activating complex. | supported | [E06c](#e06c) |
| element | rs339331 lies within the distal enhancer-like cCRE EH38E2496909 (dELS) near RFX6 and GPRC6A. | supported | [E03](#e03) |
| gene | RFX6 is the best-supported target: nearest gene, top L2G score, and E06d links the rs339331 enhancer complex to increased RFX6 expression. H4 proposes that the C allele relieves AR-mediated repression/competition and raises RFX6. | weak | [E01](#e01), [E02](#e02), [E05](#e05), [E06d](#e06d) |
| cell_type | The relevant context is prostate cancer/tumor cells, where rs339331 is an AR binding site and RFX6 is implicated; however, LNCaP-specific AR occupancy is not shown by the ENCODE data in E07, whose absence can mean no AR experiment in that biosample. | weak | [E06a](#e06a), [E06c](#e06c), [E07](#e07) |
| phenotype | E04 gives C as the prostate-cancer effect allele, consistent with C increasing RFX6 if RFX6 is oncogenic; H4 reconciles E06c's T-enhanced AR occupancy by treating AR as repressive/competitive rather than activating. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c), [E06d](#e06d) |

Predictions: Allele-specific AR ChIP at rs339331 is stronger on T than C in PCa cells; The C allele increases RFX6 enhancer activity/expression relative to T; AR knockdown or loss of AR binding increases RFX6 expression at the T allele

Falsified if: C allele does not increase RFX6 enhancer activity or expression relative to T; AR is not repressive or competitive at the rs339331 enhancer; rs339331 shows no allele-specific AR binding in PCa cells

### 2. H3: Null: no TF-mediated effect of rs339331 itself (p = 0.42)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs339331; The GWAS signal is explained by a linked causal variant in LD; RFX6 expression tracks the linked variant rather than rs339331 itself; E08's negative GTEx prostate eQTL is consistent with no detectable allele-specific expression effect in normal prostate

Falsified if: rs339331 itself shows allele-specific AR binding in PCa cells; allele-specific editing at rs339331 changes RFX6 enhancer activity or expression; fine-mapping shows rs339331 is the causal variant rather than a linked proxy

### 3. H1: AR binds the ref T allele at rs339331 and activates RFX6, predicting T as the enhancing/risk allele (discordant with E04) (p = 0.12)

TF AR (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E2496909 dELS; gene RFX6; cell type prostate cancer / AR-dependent prostate tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR binds more strongly to the ref T allele than to the alt C allele at rs339331; E06c reports that the T allele enhances AR chromatin occupancy in PCa tumors. This is literature-reported occupancy, not a perturbation shown here. | supported | [E06c](#e06c) |
| element | rs339331 lies within the distal enhancer-like cCRE EH38E2496909 (dELS) near RFX6 and GPRC6A. | supported | [E03](#e03) |
| gene | RFX6 is the strongest candidate target: it is the nearest gene, has the top L2G score, and E06d links the rs339331 enhancer complex to increased RFX6 expression. | supported | [E01](#e01), [E02](#e02), [E05](#e05), [E06d](#e06d) |
| cell_type | The mechanism is expected in prostate cancer cells/tumors, where rs339331 is described as a reprogrammed AR binding site and RFX6 is implicated in disease. | supported | [E06a](#e06a), [E06c](#e06c) |
| phenotype | rs339331 is associated with prostate cancer risk at 6q22, but E04 gives C as the prostate-cancer effect allele while E06c calls T the risk allele; H1 therefore predicts T-risk activation and is directionally discordant with E04. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c) |

Predictions: AR ChIP at rs339331 is stronger on T than C in PCa cells; T allele or T-associated enhancer activity increases RFX6 expression; CRISPR editing T>C lowers AR occupancy and RFX6 enhancer activity/expression

Falsified if: rs339331 shows no allele-specific AR binding in PCa cells; CRISPR T>C editing does not change AR occupancy in PCa cells; AR knockdown does not change RFX6 expression or enhancer activity

## Prediction matrix

| Test | Cost | Separates top two | H4 | H3 | H1 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific AR ChIP-qPCR at rs339331 in LNCaP or another heterozygous PCa line | medium | yes | AR occupancy at rs339331 is stronger on T than C | No allelic difference in AR occupancy | AR occupancy at rs339331 is stronger on T than C |
| CRISPR T>C edit or allele-specific enhancer reporter at rs339331 in LNCaP, read RFX6 reporter/expression | high | yes | C allele gives higher RFX6 enhancer activity/expression | No allele-specific change in RFX6 enhancer activity/expression | T allele gives higher RFX6 enhancer activity/expression |
| Prostate eQTL for RFX6, ideally in tumor or PCa-relevant prostate tissue; note E08 is already negative in GTEx normal prostate | low | yes | C allele associates with higher RFX6 expression | No RFX6 eQTL for rs339331 | T allele associates with higher RFX6 expression |
| AR knockdown or CRISPRi in LNCaP followed by RFX6 RT-qPCR | medium | yes | AR knockdown increases RFX6 expression | No change in RFX6 expression after AR knockdown | AR knockdown decreases RFX6 expression |

## Next experiment

Allele-specific AR ChIP-qPCR at rs339331 in LNCaP (or another heterozygous PCa line) is the cheapest single experiment separating the top two chains: H4 predicts T>C AR occupancy, while H3 predicts no allelic difference. Cost is medium.

## Investigate calls

- chip_peaks({"biosample": "LNCaP clone FGC", "tf": "AR"})
- eqtl_lookup({"tissue": "Prostate"})
- literature_search({"query": "rs339331 allele-specific enhancer reporter OR CRISPR AR RFX6 prostate cancer risk allele"})

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

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:23+00:00)

> No ENCODE AR ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP clone FGC'. Absence can also mean no AR experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20allele-specific%20enhancer%20reporter%20OR%20CRISPR%20AR%20RFX6%20prostate%20cancer%20risk%20allele&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T01:37:44+00:00)

> Europe PMC: 20 hits for 'rs339331 allele-specific enhancer reporter OR CRISPR AR RFX6 prostate cancer risk allele'; top 8 with PMIDs:
> PMID 41422049 (2025): Multifaceted functions of transcription regulatory factor X6 (RFX6): from pancreatic development to cancer progression.
> PMID 38932472 (2024): An Inherited Allele Confers Prostate Cancer Progression and Drug Resistance via RFX6/HOXA10-Orchestrated TGFβ Signaling.
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 36428729 (2022): SNP-Target Genes Interaction Perturbing the Cancer Risk in the Post-GWAS.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 32443951 (2020): Enhancer Predictions and Genome-Wide Regulatory Circuits.
> PMID 32472759 (2020): Beyond the coding genome: non-coding mutations and cancer.
> PMID 27409348 (2016): Identification and validation of regulatory SNPs that modulate transcription factor chromatin binding and gene expression in prostate cancer.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T01:37:44+00:00)

> Here the FinnGen cohort phenome-wide analysis, along with multiple genome-wide association studies, has consistently identified the rs339331-RFX6/6q22 locus associated with prostate cancer (PCa) risk across diverse populations.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T01:37:44+00:00)

> It is uncovered that rs339331 resides in a reprogrammed androgen receptor (AR) binding site in PCa tumors, with the T risk allele enhancing AR chromatin occupancy.

<a id="e09c"></a>**E09c** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T01:37:44+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs339331/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.

<a id="e09d"></a>**E09d** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T01:37:44+00:00)

> Tumor cellular assays, qRT-PCR, western blot, ChIP, luciferase assays and CRISPR-Cas9 editing methods were performed to mechanistically understand the cooperation of GATA2 with SMAD4 in promoting TGFβ1 and AR signaling and mediating inherited PCa risk and progression.

<a id="e09e"></a>**E09e** literature_search, Europe PMC abstract, PMID 41422049 (https://europepmc.org/article/MED/41422049; retrieved 2026-10-26T01:37:44+00:00)

> Dysregulated expression or mutations of the RFX6 gene in prostate cancer, hepatocellular carcinoma, gastric cancer, melanoma, and other tumors have garnered significant interest, with studies showing that such alterations affect tumor cell proliferation, migration, and invasion, and are correlated with an unfavorable clinical prognosis in patients carrying RFX6 mutations.

<a id="e09f"></a>**E09f** literature_search, Europe PMC abstract, PMID 27409348 (https://europepmc.org/article/MED/27409348; retrieved 2026-10-26T01:37:44+00:00)

> In addition, 5 SNPs (rs2659051, rs10936845, rs9925556, rs6057110 and rs2742624) are selected for experimental validation using Chromatin immunoprecipitation (ChIP), dual-luciferase reporter assay in LNCaP cells, showing allele-specific enhancer activity.

<a id="e09g"></a>**E09g** literature_search, Europe PMC abstract, PMID 27409348 (https://europepmc.org/article/MED/27409348; retrieved 2026-10-26T01:37:44+00:00)

> Furthermore, we delete the rs2742624-containing region using CRISPR/Cas9 genome editing and observe the drastic downregulation of its target gene UPK3A.
