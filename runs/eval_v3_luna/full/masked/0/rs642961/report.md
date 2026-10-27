# rs642961 and Cleft lip (IRF6)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 140 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ZNF687 (bound elsewhere, z -0.21, no clear allelic change, weak site). Occupancy unknown: ETV2 (z 77.65); ETV3 (z 77.65); ETV3L (z 77.65); FEV (z 77.65); FLI1 (z 77.65). Diagnostic, not shown to the model: 222 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: Null: no TF-mediated effect of this variant (p = 0.82)

Null chain: no TF-mediated effect of this variant.

Predictions: In relevant craniofacial cells, the A>G change will not produce a reproducible TF-dependent effect on enhancer output or a linked target gene; the cleft association may reflect linkage or another mechanism.

Falsified if: Precise A/G allele editing produces a reproducible molecular effect at this element that depends on a TF and alters a target gene in a manner consistent with the disease association.

### 2. H3: Tentative FLI1-dependent enhancer effect on UTP25 (p = 0.13)

TF FLI1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2863563; gene UTP25; cell type Craniofacial developmental cells; activity and FLI1 occupancy in this context are not established.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FLI1 is a tentative ETS-family candidate. Its QBiC-SELEX entry predicts stronger binding to G, but the best-scoring result uses an ETV5-mapped model and does not show FLI1 occupancy at this site. The shared ETS-family result does not distinguish FLI1 from other candidates. | weak | [E16](#e16) |
| element | The variant lies in the enhancer-like cCRE EH38E2863563; its reported activity maxima are not specific to craniofacial developmental cells. | supported | [E01](#e01), [E03](#e03) |
| gene | UTP25 is a candidate target because it is nearby and has the highest reported best L2G score across the listed sets. The UTP25–cleft gene score and broad enhancer literature add plausibility, but do not show that this variant regulates UTP25. | weak | [E02](#e02), [E07](#e07), [E09a](#e09a), [E19](#e19) |
| cell_type | Craniofacial developmental cells are a plausible context for the trait, but the evidence does not demonstrate FLI1 occupancy, element activity, or UTP25 regulation in those cells. | weak | [E03](#e03), [E09a](#e09a) |
| phenotype | The variant is associated with orofacial clefts, but this does not establish a cleft-lip-specific causal effect or that altered UTP25 regulation mediates the association. | supported | [E06](#e06), [E07](#e07) |

Predictions: If this chain is correct, FLI1 should occupy the element in relevant cells and show greater binding to G. The variant should produce an FLI1-dependent change in UTP25 regulation; the direction of the expression change cannot be inferred from the binding prediction.

Falsified if: Relevant-cell assays show no FLI1 occupancy, or precise allele editing shows no FLI1-dependent effect on UTP25.

### 3. H2: Tentative ETV3-dependent enhancer effect on IRF6 (p = 0.03)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2863563; gene IRF6; cell type Craniofacial developmental cells; activity and ETV3 occupancy in this context are not established.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3 is an unconfirmed candidate: its QBiC-SELEX result predicts stronger binding to G using an ETV5-mapped model, but does not establish ETV3 occupancy. No ETV3 peak was reported in cranial neural crest cells; the evidence notes that this may reflect lack of an experiment. The shared ETS-family prediction does not distinguish ETV3 from the other candidates. | weak | [E13](#e13), [E17](#e17) |
| element | The variant lies in the enhancer-like cCRE EH38E2863563; the reported activity scores are maxima across biosamples, not evidence of activity in craniofacial cells. | supported | [E01](#e01), [E03](#e03) |
| gene | IRF6 is a candidate target based on proximity and L2G results, but the supplied evidence does not establish that this variant's cCRE regulates IRF6. The literature search found no variant-specific result linking this site to IRF6. | weak | [E02](#e02), [E07](#e07), [E09a](#e09a), [E18](#e18) |
| cell_type | Craniofacial developmental cells are a plausible context for the cleft association, but this element's activity and ETV3 occupancy in those cells are not demonstrated. | weak | [E03](#e03), [E09a](#e09a), [E17](#e17) |
| phenotype | The variant has a reported orofacial-cleft association; the evidence does not establish a cleft-lip-specific causal effect or an ETV3–IRF6 mechanism. | supported | [E06](#e06), [E07](#e07) |

Predictions: If this chain is correct, ETV3 should occupy the element in relevant cells, with greater binding to G, and an allele-dependent effect on IRF6 regulation should depend on ETV3.

Falsified if: Relevant-cell assays show no ETV3 occupancy or no reproducible ETV3-dependent allele effect on IRF6.

### 4. H4: Tentative ETV2-dependent enhancer effect on TRAF3IP3 (p = 0.02)

TF ETV2 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2863563; gene TRAF3IP3; cell type Craniofacial developmental cells; activity and ETV2 occupancy in this context are not established.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV2 is an unconfirmed ETS-family candidate. Its QBiC-SELEX result predicts stronger binding to G using an ETV5-mapped model, but there is no evidence here of ETV2 occupancy at the variant. The same model result is reported for related ETS factors and does not select ETV2. | weak | [E12](#e12) |
| element | The variant lies in enhancer-like cCRE EH38E2863563; the reported activity scores do not identify a craniofacial cell type with activity at this element. | supported | [E01](#e01), [E03](#e03) |
| gene | TRAF3IP3 is a candidate target because it is nearby and appears in L2G results. Its reported eQTLs are in blood-related contexts, and neither those results nor the broad literature establishes this cCRE as its target. | weak | [E02](#e02), [E07](#e07), [E08](#e08), [E09a](#e09a), [E18](#e18) |
| cell_type | Craniofacial developmental cells are a plausible context for the trait, but ETV2 binding and TRAF3IP3 regulation in those cells are not demonstrated. | weak | [E03](#e03), [E09a](#e09a) |
| phenotype | The variant has a reported orofacial-cleft association; the evidence does not establish a cleft-lip-specific causal effect or an ETV2–TRAF3IP3 mechanism. | supported | [E06](#e06), [E07](#e07) |

Predictions: If this chain is correct, ETV2 should occupy the element in relevant cells, with greater binding to G, and an allele-dependent effect on TRAF3IP3 regulation should depend on ETV2.

Falsified if: Relevant-cell assays show no ETV2 occupancy or no reproducible ETV2-dependent allele effect on TRAF3IP3.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H3 | H2 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Paired A/G enhancer reporter assay in cranial neural crest-like cells, with and without FLI1 depletion; measure reporter output | medium | yes | No reproducible allele-dependent reporter effect that depends on FLI1. | A reproducible allele-dependent reporter effect should be altered or lost with FLI1 depletion; its direction is not specified. | Any reproducible allele-dependent effect should depend on ETV3, not specifically FLI1. | Any reproducible allele-dependent effect should depend on ETV2, not specifically FLI1. |
| Measure allele-specific expression of IRF6, UTP25, and TRAF3IP3 after precise A/G editing in cranial neural crest-like cells | high | yes | No reproducible target-gene expression change attributable to the edit. | An allele-dependent UTP25 expression effect, predicted to depend on FLI1. | An allele-dependent IRF6 expression effect, predicted to depend on ETV3. | An allele-dependent TRAF3IP3 expression effect, predicted to depend on ETV2. |

## Next experiment

The cheapest direct functional discriminator for the top two chains is a paired A/G enhancer reporter assay in cranial neural crest-like cells with and without FLI1 depletion (medium cost). H3 predicts an allele-dependent effect that changes with FLI1 depletion; H1 predicts no reproducible FLI1-dependent allele effect. The direction of reporter output is not assumed from stronger predicted binding.

## Investigate calls

- chip_peaks({"tf": "ETV3", "biosample": "cranial neural crest cells"})
- literature_search({"query": "\"chr1:209815925\" OR \"209815925\" IRF6 UTP25 TRAF3IP3 orofacial cleft PMID 42873673"})
- gene_disease({"gene": "UTP25"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/1:209815925-209815925:1/G?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:29:41+00:00)

> Variant chr1:209815925:A>G (GRCh38), allele string A/G
> Known IDs: rs642961
> Most severe consequence: regulatory_region_variant
> Regulatory features: ENSR1_B3JM9C enhancer
> GERP conservation score at the site: 0.516
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/1:208815925-210815925?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:29:25+00:00)

> 13 protein-coding genes within 1000 kb of chr1:209815925:A>G, by distance to TSS:
> IRF6: 9.7 kb from TSS (upstream, strand -1)
> ENSG00000289700: 9.7 kb from TSS (upstream, strand -1)
> UTP25: 12.0 kb from TSS (upstream, strand +1)
> C1orf74: 31.3 kb from TSS (upstream, strand -1)
> TRAF3IP3: 60.4 kb from TSS (downstream, strand +1)
> SYT14: 85.0 kb from TSS (upstream, strand +1)
> HSD11B1: 129.8 kb from TSS (downstream, strand +1)
> G0S2: 140.5 kb from TSS (downstream, strand +1)
> LAMB3: 162.8 kb from TSS (upstream, strand -1)
> CAMK1G: 232.2 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:29:16+00:00)

> The variant lies in cCRE EH38E2863563 (dELS: distal enhancer-like), chr1:209815915-209816264.
> SCREEN: 2 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2863563 dELS (contains the variant): DNase z 5.3, H3K27ac z 5.0, H3K4me3 z 2.4, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> EH38E2863562 dELS: DNase z 3.2, H3K27ac z 4.9, H3K4me3 z 1.9, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr1:209815925:A>G: 15 peaks contain the variant, from 6 factors in 6 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): DPF2, MYC, POLR2A, POLR2AphosphoS5, STAT3. Bound, expressed TFs with a binding model: 1; listed one per row: ZNF687. Assayed with no peak here: 0 TFs in the matching biosample, 572 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR859FDL). expression not filtered (no expression data for this context).

<a id="e06"></a>**E06** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs642961&size=100; retrieved 2026-10-25T17:29:42+00:00)

> 8 GWAS Catalog associations for rs642961, strongest first:
> Systolic blood pressure: p 6.0e-12, effect allele G, risk-allele frequency NR, PMID 38689001
> Hypertension: p 2.0e-08, effect allele A, risk-allele frequency 0.1951, PMID 33230300
> Pulse pressure: p 1.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Diastolic blood pressure: p 3.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Orofacial clefts: p 2.0e-06, effect allele A, risk-allele frequency NR, PMID 19270707

<a id="e07"></a>**E07** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:41+00:00)

> 18 credible sets contain 1_209815925_A_G: 14 GWAS, 4 molecular QTL.
> GWAS Systolic blood pressure: PIP 0.10; L2G TRAF3IP3 0.11, IRF6 0.11, UTP25 0.10
> GWAS Systolic blood pressure: PIP 0.09; L2G IRF6 0.67, UTP25 0.14, TRAF3IP3 0.08
> GWAS Systolic blood pressure, combined automated + manual reading: PIP 0.05; L2G IRF6 0.13, UTP25 0.10, C1orf74 0.10
> GWAS Orofacial clefts: PIP 0.05; L2G IRF6 0.16, TRAF3IP3 0.12, C1orf74 0.10
> GWAS Systolic blood pressure: PIP 0.05; L2G IRF6 0.13, C1orf74 0.09, UTP25 0.08
> GWAS Systolic blood pressure (MTAG): PIP 0.05; L2G IRF6 0.17, C1orf74 0.09, UTP25 0.08
> eqtl for TRAF3IP3 (blueprint_tx_monocyte_enst00000460314): PIP 0.04
> eqtl for TRAF3IP3 (twinsuk_tx_blood_enst00000367023): PIP 0.02
> eqtl for TRAF3IP3 (twinsuk_exon_blood_ensg00000009790_15_1_209782056_): PIP 0.02
> eqtl for TRAF3IP3 (schmiedel_2018_exon_treg_naive_ensg00000009790_15_): PIP 0.02
> Best L2G gene scores across these sets: UTP25 0.75, IRF6 0.67, TRAF3IP3 0.53, C1orf74 0.10

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_209815925_A_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T22:31:38+00:00)

> 15 significant GTEx v8 single-tissue eQTLs for chr1_209815925_A_G_b38. NES is the effect of the alt allele (G) relative to ref (A).
> SYT14 in Nerve_Tibial: NES -0.50, p 6.7e-20
> DIEXF in Cells_Cultured_fibroblasts: NES -0.23, p 1.9e-14
> DIEXF in Artery_Tibial: NES -0.23, p 1.2e-10
> TRAF3IP3 in Whole_Blood: NES +0.24, p 5.9e-10
> IRF6 in Brain_Cerebellum: NES -0.62, p 2.2e-07
> DIEXF in Whole_Blood: NES -0.15, p 2.9e-07
> SYT14 in Brain_Hippocampus: NES +0.53, p 3.3e-07
> DIEXF in Adipose_Subcutaneous: NES -0.20, p 7.5e-07
> SYT14 in Brain_Spinal_cord_cervical_c-1: NES +0.72, p 2.7e-06
> DIEXF in Lung: NES -0.11, p 3.2e-06
> IRF6 in Brain_Cerebellar_Hemisphere: NES -0.61, p 3.3e-06
> DIEXF in Brain_Frontal_Cortex_BA9: NES +0.35, p 4.6e-06
> DIEXF in Brain_Cortex: NES +0.33, p 7.0e-06
> DIEXF in Adipose_Visceral_Omentum: NES -0.16, p 2.5e-05
> C1orf74 in Whole_Blood: NES +0.15, p 8.6e-05

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:21:47+00:00)

> Europe PMC: 7 hits for 'UTP25 AND "cleft lip"'; top 6 with PMIDs:
> PMID 42873673 (2026): Genetic Heterogeneity in Cleft Lip and/or Palate With Alveolar Cleft: A Targeted Analysis of NHEK-Active Enhancer Variants.
> PMID 41075272 (2025): Genetic heterogeneity and homogeneity among orofacial cleft subtypes: genome-wide association studies in the cleft collective.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 33987535 (2021): Wavelet Screening identifies regions highly enriched for differentially methylated loci for orofacial clefts.
> PMID 30760477 (2019): Wnt signaling in orofacial clefts: crosstalk, pathogenesis and models.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 42873673 (https://europepmc.org/article/MED/42873673; retrieved 2026-10-26T20:21:47+00:00)

> All three variants overlap NHEK-active enhancers and regulate craniofacial development genes (IRF6, UTP25, TRAF3IP3, BNIP3, JAKMIP3, PPP2R2D) through chromatin looping, pluripotency factor binding, and FOX family transcription factor recruitment.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:209815925:A>G, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (none: expression filter skipped), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 1 of 1 occupied (0 with a strong site), 5 of 249 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 572 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element. No occupied TF has a strong site at the variant.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF687 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF687_FL_TA40NGTTAGC_YWL_jolma2025_0_3_7mer (its own model), z -0.21, effect -0.013: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). expression not filtered. Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR859FDL. Best model's site strength: ref 92.7th, alt 88.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV2 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3L (Ets, 18 models; QBiC-SELEX coverage: mapped models only): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FEV (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FLI1 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:36:37+00:00)

> No ENCODE ETV3 ChIP-seq peak contains chr1:209815925:A>G in biosamples matching 'cranial neural crest cells'. Absence can also mean no ETV3 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22chr1%3A209815925%22%20OR%20%22209815925%22%20IRF6%20UTP25%20TRAF3IP3%20orofacial%20cleft%20PMID%2042873673&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:31:22+00:00)

> Europe PMC: 0 hits for '"chr1:209815925" OR "209815925" IRF6 UTP25 TRAF3IP3 orofacial cleft PMID 42873673'; top 0 with PMIDs:

<a id="e19"></a>**E19** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T20:22:47+00:00)

> Open Targets: UTP25 and cleft lip (EFO_0003959), overall score 0.35; by evidence type: genetic_association 0.57, literature 0.04
