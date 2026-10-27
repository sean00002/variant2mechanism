# rs642961 and Cleft lip (IRF6)

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 191 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ZNF687 (bound elsewhere, z -0.21, no clear allelic change, weak site). Occupancy unknown: ETV2 (z 77.65); ETV3 (z 77.65); ETV3L (z 77.65); FEV (z 77.65); FLI1 (z 77.65). Diagnostic, not shown to the model: 222 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect of rs642961 (p = 0.90)

Null chain: no TF-mediated effect of this variant.

Predictions: The cleft association may reflect linkage to another causal variant, or rs642961 may have no material TF-mediated regulatory effect.; The cCRE annotation and ChIP peaks do not require this base to alter TF binding or gene regulation in relevant cells; ZNF687 has no clear QBiC-SELEX allelic change at this weak site.

Falsified if: A relevant-cell experiment reproducibly shows that changing rs642961 alters occupancy of a specific TF and causes an allele-dependent regulatory effect on a target gene.

### 2. H1: Possible ETV2-mediated binding gain at the IRF6-region enhancer (p = 0.06)

TF ETV2 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2863563; gene IRF6; cell type Embryonic craniofacial or oral epithelial cells (hypothesized; not established).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger binding to G than A using a CIS-BP-mapped ETV5 model, not an ETV2-specific demonstration. ETV2 occupancy at the variant is unknown; no craniofacial-matched peak is reported, and the available data do not establish ETV2 as the factor that binds here. | weak | [E12](#e12), [E17](#e17) |
| element | The variant lies in enhancer-like cCRE EH38E2863563, but the reported chromatin signals are maxima across biosamples and do not establish activity in craniofacial tissue. | supported | [E03](#e03) |
| gene | IRF6 is a nearby candidate target and is prioritized in some cleft credible-set results, but neither proximity nor L2G directly shows that this cCRE regulates IRF6; other nearby genes are also prioritized. | weak | [E02](#e02), [E07](#e07) |
| cell_type | Embryonic craniofacial or oral epithelial cells are a plausible context for a cleft mechanism, but the supplied evidence does not establish ETV2 expression or occupancy, or activity of this element, in those cells. | missing | none |
| phenotype | rs642961 is associated with orofacial clefts, but this does not establish the proposed ETV2 mechanism. The reported cleft effect allele is A, while the in-vitro binding prediction favors G; no evidence here connects that binding direction to the direction of disease risk. | weak | [E06](#e06), [E09a](#e09a) |

Predictions: In an appropriate oral epithelial model, the allele-dependent regulatory effect should depend on ETV2; direct occupancy or perturbation evidence should support ETV2 at this element.; The direction of any resulting change in IRF6 expression or enhancer activity is not determined by the binding prediction.

Falsified if: ETV2 is absent from an appropriate model or cannot be detected at the element under relevant conditions.; A relevant-cell assay finds no reproducible ETV2-dependent allelic effect at the site or no regulatory consequence of the allele difference.

### 3. H2: Possible ETV3-mediated binding gain at the IRF6-region enhancer (p = 0.04)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2863563; gene IRF6; cell type Embryonic craniofacial or oral epithelial cells (hypothesized; not established).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger binding to G than A using the same CIS-BP-mapped ETV5 model reported for several ETS factors. This does not distinguish ETV3 from those factors or demonstrate ETV3 occupancy; no craniofacial-matched ETV3 peak is reported. | weak | [E13](#e13), [E18](#e18) |
| element | The variant lies in enhancer-like cCRE EH38E2863563, but the reported chromatin signals are maxima across biosamples and do not establish activity in craniofacial tissue. | supported | [E03](#e03) |
| gene | IRF6 is a nearby candidate target and is prioritized in some cleft credible-set results, but neither proximity nor L2G directly shows that this cCRE regulates IRF6; other nearby genes are also prioritized. | weak | [E02](#e02), [E07](#e07) |
| cell_type | Embryonic craniofacial or oral epithelial cells are a plausible context for a cleft mechanism, but the supplied evidence does not establish ETV3 expression or occupancy, or activity of this element, in those cells. | missing | none |
| phenotype | rs642961 is associated with orofacial clefts, but this does not establish the proposed ETV3 mechanism. The reported cleft effect allele is A, while the in-vitro binding prediction favors G; no evidence here connects that binding direction to the direction of disease risk. | weak | [E06](#e06), [E09a](#e09a) |

Predictions: In an appropriate oral epithelial model, the allele-dependent regulatory effect should depend on ETV3; direct occupancy or perturbation evidence should support ETV3 at this element.; An ETV3-dependent result would distinguish this chain from the ETV2 chain; the shared QBiC-SELEX model alone does not distinguish them.; The direction of any resulting change in IRF6 expression or enhancer activity is not determined by the binding prediction.

Falsified if: ETV3 is absent from an appropriate model or cannot be detected at the element under relevant conditions.; A relevant-cell assay finds no reproducible ETV3-dependent allelic effect at the site or no regulatory consequence of the allele difference.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Paired-allele reporter assay in an oral epithelial model with ETV2 depletion and rescue | medium | yes | No reproducible allele-dependent, ETV2-dependent reporter effect. | A reproducible allele-dependent reporter effect that is reduced by ETV2 depletion and restored by rescue; the direction of the effect is not specified in advance. | No ETV2-specific dependence is expected; an allele-dependent effect could instead depend on ETV3. |
| Compare ETV2 and ETV3 occupancy at the variant in a relevant oral epithelial model, including allele-specific occupancy where feasible | high | yes | No reproducible variant-dependent occupancy of the proposed factor that supports a regulatory mechanism. | ETV2 occupancy at the element, with greater occupancy on G than A if the predicted binding difference operates in these cells. | ETV3 occupancy at the element, with greater occupancy on G than A if the predicted binding difference operates in these cells. |
| Edit A and G alleles in an appropriate oral epithelial model and measure IRF6 and nearby candidate-gene expression | high | yes | No reproducible expression effect attributable to the edited base. | An allele-dependent expression effect is possible, but its direction and whether IRF6 is the affected gene are not established by current evidence. | An allele-dependent expression effect is possible, but its direction and whether IRF6 is the affected gene are not established by current evidence. |

## Next experiment

Run the paired-allele reporter assay in an oral epithelial model with ETV2 depletion and rescue. It is the least costly proposed test that can distinguish the two highest-probability chains: H1 predicts an ETV2-dependent allele effect, whereas H0 predicts none. A positive result would still require endogenous validation.

## Investigate calls

- chip_peaks({"tf": "ETV2", "biosample": "craniofacial"})
- chip_peaks({"tf": "ETV3", "biosample": "craniofacial"})
- literature_search({"query": "rs642961 IRF6 enhancer allele-specific binding reporter craniofacial"})

## Flags

- none

Citation support: 0.80 of links cite only evidence that passed every check.

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

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20AND%20UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:43+00:00)

> Europe PMC: 2 hits for 'rs642961 AND UTP25 AND "cleft lip"'; top 2 with PMIDs:
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-25T17:29:43+00:00)

> Conditional analyses of GWAS data suggest the two functional SNPs near IRF6 account for the majority of risk for CL/P at this locus.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 37161310 (https://europepmc.org/article/MED/37161310; retrieved 2026-10-25T17:29:43+00:00)

> This study revealed that the SNP rs12403599, within the IRF6 promoter, is associated with all phenotypes of NSCL/P, especially nonsyndromic cleft lip (NSCLO) and a subphenotype of it, microform cleft lip (MCL).

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

> No ENCODE ETV2 ChIP-seq peak contains chr1:209815925:A>G in biosamples matching 'craniofacial'. Absence can also mean no ETV2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:36:37+00:00)

> No ENCODE ETV3 ChIP-seq peak contains chr1:209815925:A>G in biosamples matching 'craniofacial'. Absence can also mean no ETV3 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20IRF6%20enhancer%20allele-specific%20binding%20reporter%20craniofacial&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:36:37+00:00)

> Europe PMC: 17 hits for 'rs642961 IRF6 enhancer allele-specific binding reporter craniofacial'; top 8 with PMIDs:
> PMID 42799765 (2026): The orofacial cleft risk gene IRF6 is a target gene of SOX9 in cranial neural crest cells.
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 40918684 (2025): Functional Validation of Noncoding Variants Associated With Nonsyndromic Orofacial Cleft.
> PMID 39500877 (2024): High incidence and geographic distribution of cleft palate in Finland are associated with the IRF6 gene.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.
> PMID 36008388 (2022): Chromatin conformation of human oral epithelium can identify orofacial cleft missing functional variants.
> PMID 35226783 (2022): Revisiting the embryogenesis of lip and palate development.
> PMID 32031521 (2020): Analysis of zebrafish periderm enhancers facilitates identification of a regulatory variant near human <i>KRT8/18</i>.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-26T13:36:37+00:00)

> To identify candidates for functional SNPs at eight such loci we conduct a massively parallel reporter assay in a fetal oral epithelial cell line, revealing SNPs with allele-specific effects on enhancer activity.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-26T13:36:37+00:00)

> For two SNPs near IRF6 and one near FOXE1, we engineer the genome of induced pluripotent stem cells, differentiate the cells into embryonic oral epithelium, and discover allele-specific effects on the levels of effector gene expression, and, in two cases, the binding affinity of transcription factors FOXE1 or ETS2.

<a id="e19c"></a>**E19c** literature_search, Europe PMC abstract, PMID 39500877 (https://europepmc.org/article/MED/39500877; retrieved 2026-10-26T13:36:37+00:00)

> The risk allele of rs570516915 alters a conserved binding site for the transcription factor IRF6 within an enhancer (MCS-9.7) upstream of the IRF6 gene and diminishes the enhancer activity.

<a id="e19d"></a>**E19d** literature_search, Europe PMC abstract, PMID 39500877 (https://europepmc.org/article/MED/39500877; retrieved 2026-10-26T13:36:37+00:00)

> Oral epithelial cells derived from CRISPR-Cas9 edited induced pluripotent stem cells demonstrate that the CP-associated allele of rs570516915 concomitantly decreases the binding of IRF6 and the expression level of IRF6, suggesting impaired IRF6 autoregulation as a molecular mechanism underlying the risk for CP.

<a id="e19e"></a>**E19e** literature_search, Europe PMC abstract, PMID 42799765 (https://europepmc.org/article/MED/42799765; retrieved 2026-10-26T13:36:37+00:00)

> The IRF6 enhancer MCS-9.7 is bound and activated by the transcription factor SOX9, mutations of which cause Pierre Robin sequence, a craniofacial anomaly that includes cleft palate.

<a id="e19f"></a>**E19f** literature_search, Europe PMC abstract, PMID 42799765 (https://europepmc.org/article/MED/42799765; retrieved 2026-10-26T13:36:37+00:00)

> This SOX9-dependent activation is influenced by the single nucleotide variant rs76145088 that is associated with orofacial clefting.
