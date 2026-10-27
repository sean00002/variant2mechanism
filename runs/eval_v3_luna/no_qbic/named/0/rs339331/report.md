# rs339331 and Prostate cancer (6q22)

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 9 model calls; 153 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. H4: HOXB13 binding at the T allele contributes to RFX6 regulation (p = 0.42)

TF HOXB13 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E2496909, which the literature describes as an rs339331-associated prostate cancer risk enhancer.; gene RFX6; cell type Prostate cancer cells in which the reported rs339331 enhancer and HOXB13 binding are active; activity in LNCaP clone FGC is not established..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 is the candidate because the literature reports increased HOXB13 binding at the rs339331 region in T-risk versus C-protective homozygous cell lines. This supports greater binding for T (ref), but does not isolate HOXB13 from other enhancer-complex members in every context. No QBiC-SELEX result is provided. | weak | [E10d](#e10d) |
| element | The variant lies within enhancer-like cCRE EH38E2496909, and the literature places a HOXB13-containing transcriptional complex at the rs339331-associated enhancer. | supported | [E03](#e03), [E09d](#e09d), [E10d](#e10d) |
| gene | RFX6 is the proposed target: the literature reports increased RFX6 transcription associated with T and increased HOXB13 binding at the region, and RFX6 has strong locus-to-gene support. | supported | [E07](#e07), [E10d](#e10d) |
| cell_type | The proposed binding and regulatory effect is in prostate cancer cells represented by the cited functional studies; the supplied evidence does not establish HOXB13 occupancy in LNCaP clone FGC. | weak | [E04](#e04), [E10d](#e10d) |
| phenotype | The reported T-associated HOXB13 binding and RFX6 transcription could connect the enhancer to prostate cancer, but a causal contribution to risk is not established. The reported T-risk direction conflicts with the C effect allele listed for prostate cancer in the GWAS Catalog. | weak | [E06](#e06), [E10d](#e10d), [E09d](#e09d) |

Predictions: In relevant prostate cancer cells, allele-specific assays will show greater HOXB13 occupancy on T than C, and HOXB13 perturbation will reduce the corresponding allele-dependent RFX6 effect.; HOXB13 occupancy and perturbation will explain the allele-dependent effect better than AR occupancy and perturbation do.

Falsified if: Allele-specific assays in a relevant prostate cancer context show no greater HOXB13 binding on T than C.; HOXB13 perturbation leaves the allele-dependent enhancer activity and RFX6 expression unchanged, while AR perturbation removes the effect.

### 2. H1: AR occupancy at the T allele contributes to RFX6 regulation (p = 0.33)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E2496909; literature describes the site as an AR-binding site in prostate cancer tumors.; gene RFX6; cell type Prostate cancer tumor cells with the reported reprogrammed AR-binding state; this state is not established in LNCaP clone FGC..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR is a candidate because the literature reports greater AR chromatin occupancy for T (ref) than C (alt) at rs339331 in prostate cancer tumors. No QBiC-SELEX result is provided. ENCODE reports no TF peaks in LNCaP clone FGC, so occupancy in that cell line is unconfirmed. | weak | [E04](#e04), [E09c](#e09c) |
| element | The variant lies within enhancer-like cCRE EH38E2496909. The cCRE's reported SCREEN scores are maxima across biosamples and do not establish activity in the proposed tumor state. | supported | [E03](#e03), [E09c](#e09c) |
| gene | RFX6 is the leading target candidate because it is nearby, has the strongest locus-to-gene support among the listed genes, and is linked in the literature to this prostate cancer locus. | supported | [E02](#e02), [E07](#e07), [E09b](#e09b), [E10b](#e10b) |
| cell_type | This model requires prostate cancer tumor cells with the reported reprogrammed AR-bound state; the supplied ENCODE data do not show TF occupancy at the variant in LNCaP clone FGC. | supported | [E04](#e04), [E09c](#e09c) |
| phenotype | Greater AR occupancy on T could contribute to prostate cancer risk through altered RFX6 regulation, but that causal chain is not directly established. The reported T risk direction conflicts with the C effect allele listed for prostate cancer in the GWAS Catalog. | weak | [E06](#e06), [E09c](#e09c), [E10b](#e10b) |

Predictions: In prostate tumor cells with the reported AR-bound state, allele-specific assays will show greater AR occupancy on T than C.; AR perturbation will reduce the T-associated regulatory effect more than HOXB13 perturbation does; this has not been demonstrated by the supplied evidence.

Falsified if: Allele-specific assays in a relevant prostate tumor context show no greater AR occupancy on T than C.; AR perturbation leaves the allele-dependent enhancer activity and RFX6 expression unchanged in the proposed context.

### 3. H3: No TF-mediated effect of this variant (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not produce a reproducible allele-specific TF-occupancy change that alters enhancer activity or RFX6 expression in relevant prostate cells.; The association may reflect linkage to another causal variant or another mechanism not mediated by TF binding at this base.

Falsified if: Isogenic allele replacement or allele-specific assays reproducibly show that changing this base changes TF occupancy and enhancer activity or RFX6 expression in relevant prostate cells.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H3 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific AR and HOXB13 CUT&RUN (or ChIP) at rs339331 in a relevant prostate cancer model heterozygous for T/C | medium | yes | Greater HOXB13 occupancy on T than C; the HOXB13 allelic difference is the distinguishing result. | Greater AR occupancy on T than C; the AR allelic difference is the distinguishing result. | No reproducible allelic occupancy difference for either TF. |
| Perturb AR and HOXB13 separately in the same prostate cancer model, then measure allele-specific enhancer activity and RFX6 expression | high | no | HOXB13 perturbation preferentially reduces the allele-dependent enhancer or RFX6 effect. | AR perturbation preferentially reduces the allele-dependent enhancer or RFX6 effect. | Neither perturbation reveals a reproducible variant-dependent regulatory effect. |
| Isogenic T-to-C and C-to-T editing followed by RFX6 expression and enhancer-activity measurement in a relevant prostate cancer model | high | no | Editing changes enhancer activity or RFX6 expression in a direction consistent with the T-associated HOXB13 model. | Editing changes enhancer activity or RFX6 expression in a direction consistent with the T-associated AR model. | Editing produces no reproducible regulatory change attributable to this base. |

## Next experiment

The cheapest proposed test that separates the two leading chains is allele-specific AR and HOXB13 CUT&RUN at rs339331 in a relevant T/C-heterozygous prostate cancer model. It directly compares the competing TF-occupancy predictions; LNCaP clone FGC is not an established occupancy-positive context in the supplied data.

## Investigate calls

- literature_search({"query": "rs339331 T C allele risk AR occupancy RFX6 expression allele-specific prostate cancer"})
- chip_peaks({"tf": "GATA2", "biosample": "LNCaP clone FGC"})
- literature_search({"query": "rs339331 GATA2 SMAD4 HOXB13 allele-specific binding perturbation RFX6 prostate cancer"})

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

<a id="e10"></a>**E10** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20T%20C%20allele%20risk%20AR%20occupancy%20RFX6%20expression%20allele-specific%20prostate%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:24:23+00:00)

> Europe PMC: 8 hits for 'rs339331 T C allele risk AR occupancy RFX6 expression allele-specific prostate cancer'; top 8 with PMIDs:
> PMID 38932472 (2024): An Inherited Allele Confers Prostate Cancer Progression and Drug Resistance via RFX6/HOXA10-Orchestrated TGFβ Signaling.
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 32443951 (2020): Enhancer Predictions and Genome-Wide Regulatory Circuits.
> PMID 26398868 (2015): CAUSEL: an epigenome- and genome-editing pipeline for establishing function of noncoding GWAS variants.
> PMID 28598379 (2017): Genomic Insight into the Role of lncRNA in Cancer Susceptibility.
> PMID 27409348 (2016): Identification and validation of regulatory SNPs that modulate transcription factor chromatin binding and gene expression in prostate cancer.
> PMID 30033361 (2018): Biology and Clinical Implications of the 19q13 Aggressive Prostate Cancer Susceptibility Locus.

<a id="e10a"></a>**E10a** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T13:24:23+00:00)

> It is uncovered that rs339331 resides in a reprogrammed androgen receptor (AR) binding site in PCa tumors, with the T risk allele enhancing AR chromatin occupancy.

<a id="e10b"></a>**E10b** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T13:24:23+00:00)

> RFX6, an AR-regulated gene linked to rs339331, exhibits synergistic prognostic value for PCa recurrence and metastasis.

<a id="e10c"></a>**E10c** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T13:24:23+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs339331/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.

<a id="e10d"></a>**E10d** literature_search, Europe PMC abstract, PMID 26398868 (https://europepmc.org/article/MED/26398868; retrieved 2026-10-26T13:24:23+00:00)

> Introduction of the 'T' risk allele increased transcription of the regulatory factor 6 (RFX6) gene, increased homeobox B13 (HOXB13) binding at the rs339331 region, and increased deposition of the enhancer-associated H3K4me2 histone mark at the rs339331 region compared to lines homozygous for the 'C' protective allele.

<a id="e11"></a>**E11** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:26:35+00:00)

> No ENCODE GATA2 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP clone FGC'. Absence can also mean no GATA2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e12"></a>**E12** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20GATA2%20SMAD4%20HOXB13%20allele-specific%20binding%20perturbation%20RFX6%20prostate%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:24:26+00:00)

> Europe PMC: 1 hits for 'rs339331 GATA2 SMAD4 HOXB13 allele-specific binding perturbation RFX6 prostate cancer'; top 1 with PMIDs:
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.

<a id="e12a"></a>**E12a** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T13:24:26+00:00)

> Functional experiments demonstrated that GATA2 physically interacted and cooperated with SMAD4 for genome-wide chromatin co-occupancy and co-regulation of PCa genes and metastasis pathways like TGFβ signaling.

<a id="e12b"></a>**E12b** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T13:24:26+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs339331/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.
