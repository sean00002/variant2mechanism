# rs339331 and Prostate cancer (6q22)

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 263 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. H1: AR-bound distal enhancer regulates RFX6 (p = 0.47)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element dELS; gene RFX6; cell type AR-positive prostate cancer/tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR is proposed to bind the ref T allele more strongly than the alt C allele. This relies on the literature quote reporting allele-specific AR chromatin occupancy with the T allele enhancing AR binding (E09d), not on a supplied AR QBiC-SELEX model; no AR QBiC-SELEX model is supplied, and E10 shows no AR ChIP-seq peak over this exact variant in LNCaP, so the binding evidence is weak. | weak | [E09d](#e09d), [E10](#e10) |
| element | The variant lies inside EH38E2496909, a distal enhancer-like cCRE (dELS), consistent with an active regulatory element; the ENCODE z-scores are maxima across biosamples, not LNCaP-specific. | supported | [E03](#e03) |
| gene | RFX6 is the nearest gene and the strongest L2G target at the locus (E02, E07, E09c), but no RFX6 prostate eQTL is shown and E11 reports no significant prostate eQTL for this variant; an element-to-RFX6 regulatory link is therefore plausible but unproven. | weak | [E02](#e02), [E07](#e07), [E09c](#e09c), [E11](#e11) |
| cell_type | The relevant context is AR-positive prostate cancer/tumor cells; E09d supports AR-driven chromatin in prostate tumors, but the supplied LNCaP ENCODE data show no TF ChIP peak containing this variant (E04), including no AR peak (E10), so LNCaP-specific occupancy is not demonstrated. | weak | [E09d](#e09d), [E04](#e04), [E10](#e10) |
| phenotype | The locus is associated with prostate cancer (E06) and RFX6 is supported by L2G and literature as a candidate target (E07, E09a-c), but a causal AR-dependent RFX6 mechanism is not directly demonstrated; allele direction is contested because E09d calls T the risk/AR-enhancing allele while E06 reports C as the prostate cancer effect allele. | weak | [E06](#e06), [E07](#e07), [E09a](#e09a), [E09b](#e09b), [E09c](#e09c), [E09d](#e09d) |

Predictions: Allele-specific AR occupancy at this element is higher on the ref T allele than the alt C allele in AR-positive prostate cancer cells/tumors.; RFX6 expression or an RFX6-dependent phenotype tracks the AR-high T allele/AR activity in prostate cancer models; the direction may be activation or repression.; The dELS contacts RFX6 and perturbation of the element alters RFX6 expression.

Falsified if: No allele-specific AR occupancy is observed at this base in AR-positive prostate cancer cells or tumors.; No RFX6 eQTL, chromatin contact, or perturbation effect links this dELS to RFX6.; The prostate cancer association is fully explained by a linked variant with no AR effect at this base.

### 2. H0: No TF-mediated allelic effect at this variant (p = 0.41)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific AR occupancy at this base in AR-positive prostate cancer cells or tumors.; No RFX6 or GPRC6A prostate eQTL or allele-dependent regulatory effect attributable to this base.; The PKNOX1 peak is only in HEK293T and not in LNCaP, so it does not explain the prostate cancer signal.; The association is driven by a linked causal variant or another element.

Falsified if: Allele-specific AR occupancy at this base and an RFX6 or GPRC6A regulatory effect are demonstrated in prostate cancer cells or tumors.

### 3. H2: AR-bound distal enhancer regulates GPRC6A (p = 0.12)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element dELS; gene GPRC6A; cell type AR-positive prostate cancer/tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR is proposed to bind the ref T allele more strongly than the alt C allele, based on the literature quote for allele-specific AR occupancy (E09d). No AR QBiC-SELEX model is supplied, and E10 shows no AR ChIP-seq peak over this exact variant in LNCaP, so the binding evidence is weak. | weak | [E09d](#e09d), [E10](#e10) |
| element | The variant lies inside EH38E2496909, a distal enhancer-like cCRE (dELS), consistent with an active regulatory element; the ENCODE z-scores are maxima across biosamples, not LNCaP-specific. | supported | [E03](#e03) |
| gene | GPRC6A is nearby and has secondary L2G support (E02, E07), but RFX6 has much stronger L2G support and no GPRC6A eQTL, chromatin contact, or perturbation evidence is supplied; E11 also shows no prostate eQTL for this variant. | weak | [E02](#e02), [E07](#e07), [E11](#e11) |
| cell_type | The relevant context is AR-positive prostate cancer/tumor cells; E09d supports AR-driven tumor chromatin, but the supplied LNCaP ENCODE data show no TF ChIP peak containing this variant (E04), including no AR peak (E10), so LNCaP-specific occupancy and GPRC6A relevance are not demonstrated. | weak | [E09d](#e09d), [E04](#e04), [E10](#e10) |
| phenotype | The locus is associated with prostate cancer and GPRC6A has secondary L2G support (E06, E07), but no GPRC6A-specific disease or perturbation evidence is supplied; allele direction is contested because E09d calls T the risk/AR-enhancing allele while E06 reports C as the prostate cancer effect allele. | weak | [E06](#e06), [E07](#e07), [E09d](#e09d) |

Predictions: Allele-specific AR occupancy at this element is higher on the ref T allele than the alt C allele in AR-positive prostate cancer cells/tumors.; GPRC6A expression or a GPRC6A-dependent phenotype tracks the AR-high T allele in prostate cancer models.; The dELS contacts GPRC6A rather than RFX6.

Falsified if: No allele-specific AR occupancy is observed at this base in AR-positive prostate cancer cells or tumors.; No GPRC6A eQTL, chromatin contact, or perturbation effect links this dELS to GPRC6A.; The dELS contacts and regulates RFX6 rather than GPRC6A.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific AR ChIP-qPCR/ChIP-seq at chr6:116888889 in AR-positive prostate cancer cells or tumor heterozygous T/C | low | yes | Higher AR occupancy on ref T than alt C | No allele-specific AR occupancy at this base | Higher AR occupancy on ref T than alt C |
| RFX6 eQTL or allele-specific RFX6 expression in prostate tissue/cells | medium | yes | RFX6 expression differs by genotype in prostate and tracks AR activity | No RFX6 eQTL or allele-specific RFX6 expression effect | No RFX6 eQTL or allele-specific RFX6 expression effect |
| Chromatin contact or CRISPR perturbation of the dELS to RFX6 vs GPRC6A in prostate cancer cells | high | yes | The dELS contacts RFX6 and perturbation alters RFX6 expression | No allele-dependent RFX6 or GPRC6A regulatory effect from this base | The dELS contacts GPRC6A and perturbation alters GPRC6A expression |
| GPRC6A eQTL, allele-specific GPRC6A expression, or GPRC6A chromatin contact in prostate | medium | no | No GPRC6A regulatory effect | No GPRC6A regulatory effect | GPRC6A expression or contact tracks the AR-high allele |

## Next experiment

Allele-specific AR ChIP-qPCR at chr6:116888889 in LNCaP clone FGC or another AR-positive prostate cancer cell/tumor sample heterozygous T/C, comparing ref T vs alt C occupancy. Reanalysis of existing LNCaP AR ChIP-seq for allele-specific reads at this base is even cheaper if raw reads are available.

## Investigate calls

- chip_peaks({"tf": "AR", "biosample": "LNCaP clone FGC"})
- eqtl_lookup({"tissue": "Prostate"})
- literature_search({"query": "RFX6 AR binding site prostate cancer allele-specific chromatin occupancy rs339331"})

## Flags

- quote_rejected: PMID 38932472: not an exact substring of the abstract

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

<a id="e10"></a>**E10** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:23+00:00)

> No ENCODE AR ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP clone FGC'. Absence can also mean no AR experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e11"></a>**E11** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr6_116888889_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:22+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr6_116888889_T_C_b38 in tissues matching 'Prostate'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e12"></a>**E12** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=RFX6%20AR%20binding%20site%20prostate%20cancer%20allele-specific%20chromatin%20occupancy%20rs339331&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:21:05+00:00)

> Europe PMC: 8 hits for 'RFX6 AR binding site prostate cancer allele-specific chromatin occupancy rs[masked]'; top 8 with PMIDs:
> PMID 38932472 (2024): An Inherited Allele Confers Prostate Cancer Progression and Drug Resistance via RFX6/HOXA10-Orchestrated TGFβ Signaling.
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 32443951 (2020): Enhancer Predictions and Genome-Wide Regulatory Circuits.
> PMID 26398868 (2015): CAUSEL: an epigenome- and genome-editing pipeline for establishing function of noncoding GWAS variants.
> PMID 28598379 (2017): Genomic Insight into the Role of lncRNA in Cancer Susceptibility.
> PMID 27409348 (2016): Identification and validation of regulatory SNPs that modulate transcription factor chromatin binding and gene expression in prostate cancer.
> PMID 30033361 (2018): Biology and Clinical Implications of the 19q13 Aggressive Prostate Cancer Susceptibility Locus.
