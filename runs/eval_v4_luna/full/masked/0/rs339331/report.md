# rs339331 and Prostate cancer (6q22)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 14 model calls; 284 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: PKNOX1 (bound elsewhere, z 11.43, weak site). Occupancy unknown: HOXC13 (z -103.49); HOXA6 (z -84.28); HOXB9 (z -84.28); HOXC12 (z -84.28); HOXC6 (z -84.28). Diagnostic, not shown to the model: 487 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: No TF-mediated effect at this variant (p = 0.62)

Null chain: no TF-mediated effect of this variant.

Predictions: Isogenic T/C enhancer reporters will show no reproducible allele-dependent activity attributable to AR or PKNOX1.; The prostate-cancer association may reflect linkage or another mechanism rather than TF-mediated activity at this base.

Falsified if: A reproducible allele-dependent effect is demonstrated at the endogenous locus and specifically depends on a TF acting through this sequence.

### 2. H2: AR occupancy is stronger on T and may contribute to regulation at the RFX6 locus (p = 0.32)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2496909, a distal enhancer-like cCRE overlapping the variant; activity in the tested prostate-cell context is not established.; gene RFX6; cell type Prostate cancer cells, including tumors with a reprogrammed AR binding site.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | A literature quote reports that the T risk allele enhances AR chromatin occupancy at a reprogrammed AR binding site. This supports stronger occupancy on ref T, but the evidence provided does not identify the assay or establish occupancy in LNCaP; no AR QBiC-SELEX result is provided. The reported T risk allele also differs from the C effect allele listed for prostate cancer in the GWAS Catalog. | weak | [E06](#e06), [E24b](#e24b) |
| element | The variant overlaps enhancer-like cCRE EH38E2496909. The registry scores are maxima across biosamples and do not establish activity in LNCaP. | supported | [E03](#e03), [E24b](#e24b) |
| gene | RFX6 is a candidate target because the variant is intronic to RFX6 and prostate-cancer credible-set analyses prioritize it; the supplied AR quote does not itself demonstrate AR-dependent regulation of RFX6. | supported | [E01](#e01), [E02](#e02), [E07](#e07), [E24b](#e24b) |
| cell_type | Prostate cancer cells are a plausible context because the literature describes AR occupancy at the site in prostate tumors, but occupancy and allele-specific activity in LNCaP are not established by the supplied ChIP results. | supported | [E04](#e04), [E20](#e20), [E24b](#e24b) |
| phenotype | The variant is associated with prostate cancer, but the conflicting reported risk/effect alleles and absence of a demonstrated AR-to-RFX6 regulatory effect leave the direction and causal contribution to risk unresolved. | supported | [E06](#e06), [E07](#e07), [E24a](#e24a), [E24b](#e24b) |

Predictions: In a relevant prostate-cell context, T should show greater AR occupancy than C, and an allele-dependent regulatory effect should diminish when AR is disrupted.; AR disruption should affect the allele-dependent result more than PKNOX1 disruption; the direction of any RFX6 expression or cancer-risk effect is not predicted by occupancy alone.

Falsified if: A suitable prostate-cell assay finds no AR occupancy or T-biased occupancy at the site, and AR disruption leaves any allele-dependent regulatory effect unchanged.

### 3. H4: PKNOX1 may bind C more strongly and alter RFX6 regulation (p = 0.06)

TF PKNOX1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2496909, a distal enhancer-like cCRE overlapping the variant; activity in LNCaP is not established.; gene RFX6; cell type LNCaP-like prostate cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger C binding using a TGIF2LX-mapped model, but the predicted site is weak and does not establish PKNOX1 binding at this base. PKNOX1 has a variant-overlapping ChIP peak in HEK293T, not LNCaP; related-model provenance limits TF-specific interpretation. | weak | [E04](#e04), [E05](#e05), [E10](#e10), [E11](#e11), [E20](#e20) |
| element | The variant overlaps enhancer-like cCRE EH38E2496909, but the reported activity scores are biosample maxima and do not establish activity in LNCaP. | supported | [E03](#e03) |
| gene | RFX6 is a candidate target based on the intronic location and prostate-cancer credible-set prioritization, but direct PKNOX1-dependent regulation by this cCRE is not shown. | supported | [E01](#e01), [E02](#e02), [E07](#e07), [E19](#e19) |
| cell_type | LNCaP is a candidate context because PKNOX1 is expressed there, but no matching-biosample peak over the variant was reported. | weak | [E04](#e04), [E05](#e05), [E20](#e20) |
| phenotype | The variant is associated with prostate cancer and RFX6 has locus and disease support, but no evidence establishes a PKNOX1-dependent effect of this variant on cancer risk. | supported | [E06](#e06), [E07](#e07), [E09a](#e09a), [E09b](#e09b), [E21](#e21) |

Predictions: A C-versus-T difference in PKNOX1 occupancy or enhancer activity should be detectable in a relevant prostate-cell context and should diminish with PKNOX1 disruption.; The allele-dependent result should track PKNOX1 perturbation rather than AR perturbation.

Falsified if: Sensitive assays find no PKNOX1 occupancy or allele-dependent activity in relevant prostate cells, and PKNOX1 perturbation does not alter an allele-dependent effect.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H4 |
| --- | --- | --- | --- | --- | --- |
| Matched T/C enhancer reporters in prostate cancer cells, tested with control, AR, and PKNOX1 perturbation | low | yes | No reproducible allele-dependent reporter effect, or no TF-specific perturbation changes an allele-dependent effect. | An allele-dependent reporter effect is reduced by AR perturbation; the literature-based binding prediction is greater AR occupancy on T. | An allele-dependent reporter effect is reduced by PKNOX1 perturbation, with C favored by the binding prediction. |
| Allele-specific AR CUT&RUN or ChIP in prostate cancer cells, paired with an isogenic T/C edit | medium | yes | No reproducible AR occupancy difference attributable to the edited base. | Greater AR occupancy on T than C, consistent with the reported literature direction. | No AR-specific allele effect is required; this chain instead predicts dependence on PKNOX1. |

## Next experiment

Run the matched T/C enhancer reporter in prostate cancer cells with AR perturbation as the primary comparison. It is the lowest-cost proposed test that distinguishes the top-ranked null chain from the AR chain; a positive result should be followed by an endogenous-locus assay.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- chip_peaks({"tf": "HOXC6", "biosample": "LNCaP clone FGC"}) for H3.binding, ran as [E17](#e17). Expected: If a variant-overlapping HOXC6 peak is found in LNCaP clone FGC, H3 gains relevant-context occupancy support and rises relative to chains lacking it; if none is found, H3 remains a mapped-model-only hypothesis and falls.
- chip_peaks({"tf": "HOXC13", "biosample": "LNCaP clone FGC"}) for H4.binding, ran as [E18](#e18). Expected: If a variant-overlapping HOXC13 peak is found in LNCaP clone FGC, H4 gains relevant-context occupancy support and is better distinguished from the related homeodomain-model hypotheses; if none is found, H4 remains weak and falls.
- eqtl_lookup({"tissue": "Prostate"}) for H3.gene, ran as [E19](#e19). Expected: If the variant is associated with RFX6 expression in prostate tissue, the proposed target-gene link gains support for H3 and other RFX6 chains; an association with another nearby gene would shift support toward that target, while no prostate eQTL leaves the link unresolved.

- Result of chip_peaks(HOXC6, LNCaP clone FGC) for H3.binding: E17 reports no ENCODE HOXC6 peak containing the variant in matching LNCaP clone FGC biosamples and no peak within 100 bp without containing it. This absence may also reflect no HOXC6 experiment in that biosample. (as expected: yes)
- Result of chip_peaks(HOXC13, LNCaP clone FGC) for H4.binding: E18 reports no ENCODE HOXC13 peak containing the variant in matching LNCaP clone FGC biosamples and no peak within 100 bp without containing it. This absence may also reflect no HOXC13 experiment in that biosample. (as expected: yes)
- Result of eqtl_lookup(Prostate) for H3.gene: E19 reports zero significant GTEx v8 single-tissue eQTLs for this variant in tissues matching Prostate; the proposed RFX6 target link remains unresolved. (as expected: yes)

Chains after revision: null 0.76; HOXC6 0.10; PKNOX1 0.08; HOXC13 0.06. Link grades changed: H2.cell_type: weak → supported, H3.cell_type: weak → supported, H4.cell_type: weak → supported.

### Round 2

- chip_peaks({"tf": "PKNOX1", "biosample": "LNCaP clone FGC"}) for H2.binding, ran as [E20](#e20). Expected: If a variant-overlapping PKNOX1 peak is found in LNCaP, H2.binding gains matching-context occupancy support and H2 rises relative to the other TF chains; if none is found, the occupancy gap remains and H2 does not gain support.
- gene_disease({"gene": "RFX6"}) for H2.phenotype, ran as [E21](#e21). Expected: If Open Targets reports prostate-cancer evidence linking RFX6 to the disease, the RFX6-to-phenotype part of H2 gains support, though this would not establish a PKNOX1-mediated variant effect; absent or weak evidence leaves the link weak.

- Result of chip_peaks({"tf":"PKNOX1","biosample":"LNCaP clone FGC"}) for H2.binding: E20 reports no variant-overlapping PKNOX1 peak in matching LNCaP biosamples; the one reported peak is in HEK293T. (as expected: yes)
- Result of gene_disease({"gene":"RFX6"}) for H2.phenotype: E21 reports an overall RFX6–prostate cancer score of 0.41, with genetic-association evidence scored 0.66 and literature evidence 0.22; this supports the gene–disease link but does not establish a PKNOX1-mediated variant effect. (as expected: yes)

Chains after revision: null 0.85; HOXC6 0.07; PKNOX1 0.04; HOXC13 0.04. Link grades changed: H2.cell_type: supported → weak, H2.phenotype: weak → supported, H3.cell_type: supported → weak, H3.phenotype: weak → supported, H4.cell_type: supported → weak, H4.phenotype: weak → supported.

### Round 3

- chip_peaks({"tf": "HOXC6", "biosample": "22Rv1"}) for H3.binding, ran as [E22](#e22). Expected: A variant-overlapping HOXC6 peak in 22Rv1 would strengthen the occupancy evidence for H3 in a prostate-cancer context; no peak would leave the binding link weak.
- chip_peaks({"tf": "HOXC13", "biosample": "22Rv1"}) for H4.binding, ran as [E23](#e23). Expected: A variant-overlapping HOXC13 peak in 22Rv1 would strengthen the occupancy evidence for H4 in a prostate-cancer context; no peak would leave the binding link weak.
- literature_search({"query": "RFX6 prostate cancer inherited allele variant enhancer reporter allele-specific expression"}) for H2.gene, ran as [E24](#e24). Expected: Quoted evidence of reporter activity, allele-specific expression, or perturbation linking this locus or cCRE to RFX6 would strengthen the target-gene link and could shift weight among chains; no such evidence would leave RFX6 as a prioritized candidate without direct regulatory support.

- Result of chip_peaks(tf=HOXC6, biosample=22Rv1) for H3.binding: E22 reports no variant-overlapping HOXC6 ChIP-seq peak in 22Rv1; absence may also reflect lack of an assay in that biosample. (as expected: yes)
- Result of chip_peaks(tf=HOXC13, biosample=22Rv1) for H4.binding: E23 reports no variant-overlapping HOXC13 ChIP-seq peak in 22Rv1; absence may also reflect lack of an assay in that biosample. (as expected: yes)
- Result of literature_search(query=RFX6 prostate cancer inherited allele variant enhancer reporter allele-specific expression) for H2.gene: E24 includes a quote reporting that the T risk allele enhances AR occupancy at a reprogrammed AR site, and another reporting a GATA2/SMAD4/HOXB13 complex at the risk-associated enhancer that leads to increased RFX6 expression. This strengthens the enhancer-to-RFX6 link, but does not establish an allele-dependent effect of this nucleotide on RFX6. (as expected: yes)

Chains after revision: null 0.62; AR 0.32; PKNOX1 0.06. Link grades changed: H2.cell_type: weak → supported, H3.binding: weak → absent, H3.cell_type: weak → absent, H3.element: supported → absent, H3.gene: supported → absent, H3.phenotype: supported → absent.

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

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T22:09:37+00:00)

> No ENCODE PKNOX1 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP clone FGC'. Absence can also mean no PKNOX1 experiment in that biosample. In other biosamples, 1 PKNOX1 peaks do contain the variant: HEK293T (experiments ENCSR233FAG).

<a id="e21"></a>**E21** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T20:19:57+00:00)

> Open Targets: RFX6 and prostate cancer (MONDO_0008315), overall score 0.41; by evidence type: genetic_association 0.66, literature 0.22

<a id="e22"></a>**E22** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:29:03+00:00)

> No ENCODE HOXC6 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching '22Rv1'. Absence can also mean no HOXC6 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e23"></a>**E23** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:29:03+00:00)

> No ENCODE HOXC13 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching '22Rv1'. Absence can also mean no HOXC13 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e24"></a>**E24** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=RFX6%20prostate%20cancer%20inherited%20allele%20variant%20enhancer%20reporter%20allele-specific%20expression&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:10:59+00:00)

> Europe PMC: 20 hits for 'RFX6 prostate cancer inherited allele variant enhancer reporter allele-specific expression'; top 7 with PMIDs:
> PMID 38932472 (2024): An Inherited Allele Confers Prostate Cancer Progression and Drug Resistance via RFX6/HOXA10-Orchestrated TGFβ Signaling.
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 34890839 (2023): Computational Assessment of the Expression-modulating Potential for Non-coding Variants.
> PMID 33691767 (2021): Editing GWAS: experimental approaches to dissect and exploit disease-associated genetic variation.
> PMID 29727686 (2018): The Post-GWAS Era: From Association to Function.
> PMID 29652634 (2018): Emerging applications of genome-editing technology to examine functionality of GWAS-associated variants for complex traits.
> PMID 36443337 (2022): Extensive germline-somatic interplay contributes to prostate cancer progression through HNF1B co-option of TMPRSS2-ERG.

<a id="e24a"></a>**E24a** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T22:10:59+00:00)

> Here the FinnGen cohort phenome-wide analysis, along with multiple genome-wide association studies, has consistently identified the rs[masked]-RFX6/6q22 locus associated with prostate cancer (PCa) risk across diverse populations.

<a id="e24b"></a>**E24b** literature_search, Europe PMC abstract, PMID 38932472 (https://europepmc.org/article/MED/38932472; retrieved 2026-10-26T22:10:59+00:00)

> It is uncovered that rs[masked] resides in a reprogrammed androgen receptor (AR) binding site in PCa tumors, with the T risk allele enhancing AR chromatin occupancy.

<a id="e24c"></a>**E24c** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T22:10:59+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs[masked]/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.
