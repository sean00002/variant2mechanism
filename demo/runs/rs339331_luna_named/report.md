# rs339331 and Prostate cancer (6q22)

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 17 model calls; 280 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: PKNOX1 (bound elsewhere, z 11.43, weak site). Occupancy unknown: HOXC13 (z -103.49); HOXA6 (z -84.28); HOXB9 (z -84.28); HOXC12 (z -84.28); HOXC6 (z -84.28). Diagnostic, not shown to the model: 487 of 997 models pass Bonferroni.

## Ranked chains

### 1. H2: HOXB13 binding at the enhancer contributes to increased RFX6 expression with T (p = 0.78)

TF HOXB13 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E2496909, which literature identifies as an rs339331 prostate-cancer risk-associated enhancer involving HOXB13.; gene RFX6; cell type Prostate cancer context; literature reports HOXB13 involvement at the enhancer, but the supplied evidence does not establish HOXB13 occupancy in LNCaP or VCaP cells..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 is favored over related homeodomain candidates because its own QBiC-SELEX model predicts stronger in-vitro binding to ref T than alt C, and literature reports increased HOXB13 binding at the region with T. The in-vitro prediction does not establish occupancy. | supported | [E18](#e18), [E19e](#e19e) |
| element | The variant lies in enhancer-like cCRE EH38E2496909, and literature places HOXB13 in a transcriptional complex at the rs339331 risk-associated enhancer. | supported | [E03](#e03), [E19c](#e19c) |
| gene | Literature reports that an enhancer-associated GATA2/SMAD4/HOXB13 complex increases RFX6 expression and separately reports increased RFX6 transcription with T. The supplied evidence does not show that HOXB13 alone mediates the expression effect. | supported | [E19c](#e19c), [E19e](#e19e), [E24a](#e24a) |
| cell_type | The proposed context is prostate cancer, where literature reports the enhancer complex and allele-associated effects. No variant-overlapping HOXB13 peak is reported in the supplied LNCaP or VCaP searches; for VCaP, the evidence does not establish whether a suitable experiment was performed. | supported | [E19c](#e19c), [E19e](#e19e), [E21](#e21), [E23](#e23) |
| phenotype | The locus is associated with prostate cancer, and literature describes T as the risk allele. The GWAS Catalog lists C as the effect allele but provides no effect direction here, so that record neither confirms nor contradicts the literature's risk-allele direction. The supplied evidence does not establish that the HOXB13-to-RFX6 mechanism causes the risk association. | supported | [E06](#e06), [E07](#e07), [E09b](#e09b), [E19e](#e19e), [E25a](#e25a) |

Predictions: In a relevant prostate cancer model, allele-resolved assays should find greater HOXB13 occupancy with T than C, and the T-associated RFX6 expression effect should depend at least partly on HOXB13.; Changing the endogenous allele from T to C should reduce the allele-associated RFX6 effect; HOXB13 perturbation should diminish its HOXB13-dependent component. This differs from an AR-mediated response and from the null.

Falsified if: Adequately sensitive assays in relevant prostate cancer cells find no HOXB13 occupancy at the element and no greater occupancy with T.; Endogenous allele editing produces no reproducible RFX6 change, or the allele-associated RFX6 response persists unchanged after HOXB13 perturbation.

### 2. H4: No TF-mediated effect of rs339331 (p = 0.17)

Null chain: no TF-mediated effect of this variant.

Predictions: The prostate cancer association may reflect linkage to another causal variant, or rs339331 may have no causal TF-mediated allelic effect.; Reported occupancy and enhancer observations may not produce an endogenous TF-dependent change in RFX6 regulation in relevant prostate cells.

Falsified if: Endogenous allele editing reproducibly changes RFX6 regulation in a relevant prostate cancer model, and the effect depends on an implicated TF.

### 3. H1: AR occupancy may contribute to RFX6 regulation (p = 0.05)

TF AR (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E2496909, and prostate-tumor literature places it in a reprogrammed AR-binding site.; gene RFX6; cell type Prostate cancer tumor cells; AR occupancy is reported in literature, but not demonstrated by the supplied matching LNCaP ChIP-seq search..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Literature reports greater AR chromatin occupancy with T (ref) than C (alt). The AR-specific QBiC-SELEX model shows no significant effect; the significant result from an NR3C2-mapped model cannot be attributed to AR. | weak | [E09c](#e09c), [E17](#e17) |
| element | The variant lies in enhancer-like cCRE EH38E2496909, which literature describes as a reprogrammed AR-binding site in prostate tumors. | supported | [E03](#e03), [E09c](#e09c) |
| gene | RFX6 is prioritized at the locus, and allele-editing literature reports increased RFX6 transcription with T; the supplied evidence does not establish that AR mediates this change. | supported | [E02](#e02), [E07](#e07), [E19e](#e19e) |
| cell_type | The proposed context is prostate cancer tumors, where literature reports AR occupancy at the site; the supplied LNCaP search found no AR peak at the variant. | supported | [E04](#e04), [E09c](#e09c) |
| phenotype | The locus is associated with prostate cancer, but an AR-mediated contribution to risk is unproven. Literature calls T the risk allele; the GWAS Catalog's C effect-allele field has no effect direction in the supplied record. | supported | [E06](#e06), [E07](#e07), [E09c](#e09c) |

Predictions: Allele-resolved assays in relevant prostate tumors should find greater AR occupancy with T than C if the reported AR mechanism is active.; If AR mediates the RFX6 effect, perturbing AR should reduce or eliminate the variant-associated RFX6 response; this differs from an HOXB13-dependent response.

Falsified if: Sensitive allele-resolved assays in relevant prostate tumors consistently show no greater AR occupancy with T, or show greater occupancy with C.; The variant-associated RFX6 response is unchanged by AR perturbation in an appropriate model.

## Prediction matrix

| Test | Cost | Separates top two | H2 | H4 | H1 |
| --- | --- | --- | --- | --- | --- |
| Isogenic endogenous T-to-C and C-to-T editing in a prostate cancer model; measure RFX6 expression with and without HOXB13 perturbation. | high | yes | Allele editing changes RFX6 expression, with a T-associated component that is reduced by HOXB13 perturbation. | Editing produces no reproducible allele-dependent RFX6 change attributable to HOXB13 or AR. | An allele-associated RFX6 change is reduced by AR perturbation rather than specifically by HOXB13 perturbation. |
| Allele-resolved HOXB13 and AR CUT&RUN or ChIP at the element in a relevant prostate cancer model. | medium | no | HOXB13 occupancy is greater on T than C. | No allele-specific occupancy difference that supports a TF-mediated effect is detected. | AR occupancy is greater on T than C; HOXB13 occupancy is not the defining signal. |

## Next experiment

The cheapest decisive experiment separating the top two hypotheses (H2 and the null) is an endogenous rs339331 allele swap in a relevant prostate cancer model, followed by RFX6 expression measurement with and without HOXB13 perturbation. A reproducible allele-dependent expression effect that is reduced by HOXB13 perturbation would support H2; no such effect would favor the null.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- qbic_tf_detail({"tf": "AR"}) for H1.binding, ran as [E17](#e17). Expected: If an AR-specific model predicts stronger binding to T, it adds allele-direction support to the tumor occupancy report and strengthens H1.binding; if it predicts C binding or has no model, the binding claim remains weak or becomes less consistent.
- qbic_tf_detail({"tf": "HOXB13"}) for H2.binding, ran as [E18](#e18). Expected: If HOXB13 has a strong ref-over-alt prediction, it could support revising H2's TF attribution from HOXC13 to HOXB13, especially given the literature's HOXB13 mention; absent a relevant model or with a conflicting direction, H2.binding remains weak.
- literature_search({"query": "rs339331 RFX6 prostate cancer allele-specific enhancer reporter expression AR"}) for H1.gene, ran as [E19](#e19). Expected: If the search finds direct evidence that rs339331 or AR occupancy at this element changes RFX6 expression, H1.gene strengthens; if it finds only locus association or indirect prioritization, the link remains weak.

- Result of qbic_tf_detail({"tf":"AR"}): The AR own-model result is not significant (effect 0.035, z 0.94); the strong C-favoring prediction is from an NR3C2-mapped model, not an AR model. The tumor report of greater T-allele AR occupancy therefore remains the directional evidence. (as expected: yes)
- Result of qbic_tf_detail({"tf":"HOXB13"}): HOXB13's own QBiC-SELEX model strongly predicts greater binding to T than C, with a strong site prediction; occupancy is not established by this assay. (as expected: yes)
- Result of literature_search({"query":"rs339331 RFX6 prostate cancer allele-specific enhancer reporter expression AR"}): The search returned literature reporting that T increases RFX6 transcription and HOXB13 binding at the region, and that HOXB13 participates in a complex at the risk-associated enhancer. This supports a rs339331-to-RFX6 link but does not show that AR occupancy mediates it. (as expected: unclear)

Chains after revision: HOXB13 0.70; null 0.17; AR 0.10; PKNOX1 0.03. Link grades changed: H1.gene: weak → supported, H2.binding: weak → supported, H2.cell_type: weak → supported, H2.gene: weak → supported, H3.gene: weak → supported, H3.phenotype: weak → missing.

### Round 2

- literature_search({"query": "rs339331 AR allele-specific occupancy perturbation RFX6 expression prostate cancer"}) for H1.binding, ran as [E20](#e20). Expected: If the results provide direct allele-resolved AR occupancy or AR perturbation evidence linked to RFX6 regulation, H1.binding gains support and H1 rises relative to H2; if they only repeat the existing occupancy association, H1 remains weak.
- chip_peaks({"tf": "HOXB13", "biosample": "LNCaP clone FGC"}) for H2.cell_type, ran as [E21](#e21). Expected: A variant-overlapping HOXB13 peak in LNCaP would strengthen H2.cell_type and distinguish H2 from the less-supported alternatives; no peak would leave occupancy in this context unconfirmed and modestly lower H2.
- literature_search({"query": "rs339331 prostate cancer T risk allele C protective allele GWAS effect allele direction"}) for H2.phenotype, ran as [E22](#e22). Expected: If the literature or study details reconcile the reported T risk allele with the catalog's C effect allele, H2.phenotype gains directional support; if the discrepancy remains unresolved, the phenotype link stays weak.

- Result of literature_search({"query":"rs339331 AR allele-specific occupancy perturbation RFX6 expression prostate cancer"}): E20 repeats the report that GATA2/SMAD4 form a complex with HOXB13 at the enhancer and increase RFX6 expression; it provides no direct AR perturbation evidence or new AR-to-RFX6 link. (as expected: yes)
- Result of chip_peaks({"tf":"HOXB13","biosample":"LNCaP clone FGC"}): E21 reports no HOXB13 ChIP-seq peak containing the variant in matching LNCaP data, while noting that this could reflect no HOXB13 experiment in that biosample. (as expected: yes)
- Result of literature_search({"query":"rs339331 prostate cancer T risk allele C protective allele GWAS effect allele direction"}): E22 provides no reconciliation of the literature's T risk-allele claim with the GWAS C effect allele; the cited meta-analysis quote only notes rs339331 among positive variants. (as expected: yes)

Chains after revision: HOXB13 0.76; null 0.12; AR 0.10; PKNOX1 0.02. Link grades changed: H1.phenotype: weak → supported, H3.gene: supported → missing.

### Round 3

- chip_peaks({"tf": "HOXB13", "biosample": "VCaP"}) for H2.cell_type, ran as [E23](#e23). Expected: If a variant-overlapping HOXB13 peak is found in VCaP, this adds prostate-cancer-cell occupancy evidence and strengthens H2.cell_type; no peak would leave the literature support intact but provide no additional occupancy support.
- literature_search({"query": "rs339331 HOXB13 perturbation allele-specific RFX6 expression prostate cancer enhancer"}) for H2.gene, ran as [E24](#e24). Expected: If the literature reports that HOXB13 perturbation reduces the T-associated RFX6 response, H2.gene gains direct mediation support and H2 rises relative to the AR chain; if it reports no such dependence or conflicting results, H2.gene remains indirect.
- literature_search({"query": "rs339331 T allele C allele prostate cancer odds ratio risk allele effect direction"}) for H2.phenotype, ran as [E25](#e25). Expected: If allele-resolved association results identify T as the risk allele, they clarify the GWAS effect-allele field and strengthen the phenotype link; if they identify C or leave direction unresolved, H2.phenotype remains uncertain.

- Result of chip_peaks({"tf":"HOXB13","biosample":"VCaP"}): E23 reports no ENCODE HOXB13 ChIP-seq peak containing the variant in matching VCaP biosamples, and no peak within 100 bp. The evidence notes that this may also reflect no HOXB13 experiment in that biosample. (as expected: yes)
- Result of literature_search({"query":"rs339331 HOXB13 perturbation allele-specific RFX6 expression prostate cancer enhancer"}): E24 repeats the report of a GATA2/SMAD4/HOXB13 complex at the enhancer associated with increased RFX6 expression, but provides no result showing that HOXB13 perturbation reduces the T-associated RFX6 response. (as expected: yes)
- Result of literature_search({"query":"rs339331 T allele C allele prostate cancer odds ratio risk allele effect direction"}): E25 provides an association report for rs339331 but no allele-specific odds ratio or risk-allele direction. It does not resolve the direction in the GWAS Catalog effect-allele field. (as expected: yes)

Chains after revision: HOXB13 0.78; null 0.17; AR 0.05. Link grades changed: H2.phenotype: weak → supported, H3.binding: weak → absent, H3.cell_type: supported → absent, H3.element: supported → absent, H3.gene: missing → absent, H3.phenotype: missing → absent.

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

> {"tf":"HOXB13","symbol":"HOXB13","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr6:116888889:T>C","gate_p":5.02e-05,"models":[{"model":"HOXB13_NA_TGCCTG20NGA_ESY_yang2017_0_3_7mer","mapping":"own","group":"G024 Homeodomain, 4 models","quality":0.914,"effect":-4.771,"z":-103.49,"p":0.0,"rank_abs_z":"1/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":97.2,"k":7}},{"model":"HOXA13_eDBD_TACTGA40NACC_KP_yin2017_1_2_7mer","mapping":"CIS-BP (HOXA13)","group":"G024 Homeodomain, 4 models","quality":0.643,"effect":-0.723,"z":-74.87,"p":0.0,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":78.0,"k":7}},{"model":"HOXC13_NA_TCCCTC20NTCC_ESY_yang2017_0_3_7mer","mapping":"CIS-BP (HOXC13)","group":"G024 Homeodomain, 4 models","quality":0.855,"effect":-2.96,"z":-64.27,"p":0.0,"rank_abs_z":"11/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":91.9,"k":7}},{"model":"HOXD13_NA_TGATAA20NATA_ESAC_yang2017_0_4_7mer","mapping":"CIS-BP (HOXD13)","group":"G024 Homeodomain, 4 models","quality":0.696,"effect":-3.437,"z":-69.26,"p":0.0,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":92.8,"k":7}}]}

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

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20AR%20allele-specific%20occupancy%20perturbation%20RFX6%20expression%20prostate%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:05:53+00:00)

> Europe PMC: 3 hits for 'rs339331 AR allele-specific occupancy perturbation RFX6 expression prostate cancer'; top 3 with PMIDs:
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 32443951 (2020): Enhancer Predictions and Genome-Wide Regulatory Circuits.

<a id="e20a"></a>**E20a** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T22:05:53+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs339331/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.

<a id="e20b"></a>**E20b** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T22:05:53+00:00)

> Our study prioritizes causal genomic amplification genes with prognostic values in PCa and reveals the pivotal roles of GATA2 in transcriptionally activating the expression of its own and TGFβ1, thereby co-opting to TGFβ1/SMAD4 signaling and RFX6 at 6q22 to modulate PCa predisposition and progression.

<a id="e21"></a>**E21** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:22+00:00)

> No ENCODE HOXB13 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'LNCaP clone FGC'. Absence can also mean no HOXB13 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e22"></a>**E22** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20prostate%20cancer%20T%20risk%20allele%20C%20protective%20allele%20GWAS%20effect%20allele%20direction&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:05:56+00:00)

> Europe PMC: 3 hits for 'rs339331 prostate cancer T risk allele C protective allele GWAS effect allele direction'; top 3 with PMIDs:
> PMID 38052806 (2023): Prostate cancer genetic risk and associated aggressive disease in men of African ancestry.
> PMID 26967244 (2016): Systematic meta-analyses of gene-specific genetic association studies in prostate cancer.
> PMID 23555315 (2013): Genome-wide testing of putative functional exonic variants in relationship with breast and prostate cancer risk in a multiethnic population.

<a id="e22a"></a>**E22a** literature_search, Europe PMC abstract, PMID 26967244 (https://europepmc.org/article/MED/26967244; retrieved 2026-10-26T22:05:56+00:00)

> Of these positive variants, FOXP4 rs1983891, LMTK2 rs6465657 and RFX6 rs339331 had not been previously meta-analyzed.

<a id="e23"></a>**E23** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:22+00:00)

> No ENCODE HOXB13 ChIP-seq peak contains chr6:116888889:T>C in biosamples matching 'VCaP'. Absence can also mean no HOXB13 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e24"></a>**E24** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20HOXB13%20perturbation%20allele-specific%20RFX6%20expression%20prostate%20cancer%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:07:32+00:00)

> Europe PMC: 5 hits for 'rs339331 HOXB13 perturbation allele-specific RFX6 expression prostate cancer enhancer'; top 5 with PMIDs:
> PMID 37550764 (2023): GATA2 co-opts TGFβ1/SMAD4 oncogenic signaling and inherited variants at 6q22 to modulate prostate cancer progression.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 32443951 (2020): Enhancer Predictions and Genome-Wide Regulatory Circuits.
> PMID 31200487 (2019): Dysregulated Transcriptional Control in Prostate Cancer.
> PMID 30181359 (2018): Genetics and biology of prostate cancer.

<a id="e24a"></a>**E24a** literature_search, Europe PMC abstract, PMID 37550764 (https://europepmc.org/article/MED/37550764; retrieved 2026-10-26T22:07:32+00:00)

> Strinkingly, GATA2 and SMAD4 globally mediated inherited PCa risk and formed a transcriptional complex with HOXB13 at the PCa risk-associated rs339331/6q22 enhancer, leading to increased expression of the PCa susceptibility gene RFX6.

<a id="e25"></a>**E25** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs339331%20T%20allele%20C%20allele%20prostate%20cancer%20odds%20ratio%20risk%20allele%20effect%20direction&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:07:36+00:00)

> Europe PMC: 13 hits for 'rs339331 T allele C allele prostate cancer odds ratio risk allele effect direction'; top 8 with PMIDs:
> PMID 38052806 (2023): Prostate cancer genetic risk and associated aggressive disease in men of African ancestry.
> PMID 39930085 (2025): Genome-wide association study of prostate-specific antigen levels in 392,522 men identifies new loci and improves prediction across ancestry groups.
> PMID 29434975 (2018): Validation of the novel susceptibility loci for prostate cancer in a Chinese population.
> PMID 26068399 (2015): An analysis of the association between prostate cancer risk loci, PSA levels, disease aggressiveness and disease-specific mortality.
> PMID 30033361 (2018): Biology and Clinical Implications of the 19q13 Aggressive Prostate Cancer Susceptibility Locus.
> PMID 27986209 (2017): Prostate Cancer Genetics: Variation by Race, Ethnicity, and Geography.
> PMID 29061142 (2017): Systematic identification of regulatory variants associated with cancer risk.
> PMID 22056501 (2012): Replication of five prostate cancer loci identified in an Asian population--results from the NCI Breast and Prostate Cancer Cohort Consortium (BPC3).

<a id="e25a"></a>**E25a** literature_search, Europe PMC abstract, PMID 22056501 (https://europepmc.org/article/MED/22056501; retrieved 2026-10-26T22:07:36+00:00)

> Four SNPs (rs13385191, rs12653946, rs1983891, and rs339331) were significantly associated with prostate cancer risk (P values ranging from 0.01 to 1.1 × 10(-5)).
