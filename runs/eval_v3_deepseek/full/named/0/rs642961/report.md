# rs642961 and Cleft lip (IRF6)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 9 model calls; 457 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ZNF687 (bound elsewhere, z -0.21, no clear allelic change, weak site). Occupancy unknown: ETV2 (z 77.65); ETV3 (z 77.65); ETV3L (z 77.65); FEV (z 77.65); FLI1 (z 77.65). Diagnostic, not shown to the model: 222 of 997 models pass Bonferroni.

## Ranked chains

### 1. H2_ETV3_IRF6: ETV3 binding change alters IRF6 expression, contributing to cleft lip risk. (p = 0.35)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR1_B3JM9C enhancer; gene IRF6; cell type Brain/Neural.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3 binds the ENSR1_B3JM9C enhancer more strongly to the alt allele G. | weak | [E13](#e13) |
| element | The ENSR1_B3JM9C enhancer is an active regulatory element. | supported | [E03](#e03) |
| gene | The altered binding of ETV3 regulates IRF6 transcription. | missing | none |
| cell_type | IRF6 expression changes are relevant in neural tissue development. | weak | [E08](#e08) |
| phenotype | Altered IRF6 expression contributes to the risk of orofacial clefting. | weak | [E06](#e06), [E09](#e09) |

Predictions: The alt allele G increases ETV3 binding, altering IRF6 expression (NES: -0.62) in brain tissues.; The ETV3-mediated functional change links the G allele and cleft risk.

Falsified if: Functional assays show ETV3 does not regulate IRF6 transcription.; Directional functional assays show the G allele increases IRF6 expression relative to the A allele.

### 2. H3_ETV2_IRF6: ETV2 binding change alters IRF6 expression, contributing to cleft lip risk. (p = 0.30)

TF ETV2 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR1_B3JM9C enhancer; gene IRF6; cell type Brain/Neural.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV2 binds the ENSR1_B3JM9C enhancer more strongly to the alt allele G. | weak | [E12](#e12) |
| element | The ENSR1_B3JM9C enhancer is an active regulatory element. | supported | [E03](#e03) |
| gene | The altered binding of ETV2 regulates IRF6 transcription. | missing | none |
| cell_type | IRF6 expression changes are relevant in neural tissue development. | weak | [E08](#e08) |
| phenotype | Altered IRF6 expression contributes to the risk of orofacial clefting. | weak | [E06](#e06), [E09](#e09) |

Predictions: The alt allele G increases ETV2 binding, leading to dysregulation of IRF6.; ETV2 binding changes at the variant site mediates the association between the G allele and disease risk.

Falsified if: Functional assays demonstrate that ETV2 binding at this locus is independent of the G allele.; Alternative TFs (like ETV3) are the dominant regulators of IRF6 at this locus.

### 3. H4_ETV3L_UTP25: ETV3L binding change regulates UTP25 expression, contributing to developmental risk. (p = 0.20)

TF ETV3L (QBiC-SELEX coverage mapped), alt allele binds more; element ENSR1_B3JM9C enhancer; gene UTP25; cell type Developmental.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3L binds the ENSR1_B3JM9C enhancer more strongly to the alt allele G. | weak | [E14](#e14) |
| element | The ENSR1_B3JM9C enhancer is an active regulatory element. | supported | [E03](#e03) |
| gene | The altered binding of ETV3L regulates UTP25 transcription. | missing | [E07](#e07) |
| cell_type | UTP25 regulation is relevant in developmental processes. | missing | [E07](#e07) |
| phenotype | The altered regulation of UTP25 contributes to orofacial clefting risk. | missing | [E06](#e06) |

Predictions: The alt allele G increases ETV3L binding, causing a functional alteration in UTP25 expression.; This regulatory change in UTP25 correlates with orofacial clefting risk.

Falsified if: Functional assays show ETV3L does not regulate UTP25 transcription.; UTP25 does not exhibit a significant eQTL or L2G link in this context.

### 4. H1_Null: The variant rs642961 acts as a passenger or is linked to a causal variant. No TF-mediated effect. (p = 0.15)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant has no direct, TF-mediated regulatory function in relation to the disease phenotype.

Falsified if: A direct, TF-mediated functional link between the variant and the expression or activity of a nearby gene can be established.

## Prediction matrix

| Test | Cost | Separates top two | H2_ETV3_IRF6 | H3_ETV2_IRF6 | H4_ETV3L_UTP25 | H1_Null |
| --- | --- | --- | --- | --- | --- | --- |
| Literature search: Does ETV3 transcription factor bind or regulate IRF6 near the ENSR1_B3JM9C enhancer? | medium | yes | Positive (Support) | Negative (No direct evidence) | Negative (Unrelated to IRF6) |  |
| Literature search: Does ETV2 transcription factor bind or regulate IRF6 near the ENSR1_B3JM9C enhancer? | medium | yes | Negative (No direct evidence) | Positive (Support) | Negative (Unrelated to IRF6) |  |
| Functional CRISPR perturbation: Does the G allele (vs A) increase or decrease IRF6 expression in relevant neural cells? | high | yes | Negative (Down/Decrease) | Negative (Down/Decrease) | N/A (Different gene) |  |
| ChIP-seq analysis: Does ZNF687 show enrichment at the variant site in Brain tissue? | low | no | N/A (Not relevant) | N/A (Not relevant) | N/A (Not relevant) |  |

## Next experiment

literature_search({"query": "ETV3 IRF6 enhancer"})

## Investigate calls

- literature_search({"query": "ETV3 IRF6 enhancer"})
- chip_peaks({"tf": "ZNF687", "biosample": "Brain"})
- literature_search({"query": "ETV2 UTP25 enhancer"})

## Flags

- none

Citation support: 0.87 of links cite only evidence that passed every check.

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

<a id="e17"></a>**E17** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=ETV3%20IRF6%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:17:20+00:00)

> Europe PMC: 9 hits for 'ETV3 IRF6 enhancer'; top 8 with PMIDs:
> PMID 40998781 (2025): Disease-linked regulatory DNA variants and homeostatic transcription factors in epidermis.
> PMID 41918732 (2026): A comparative analysis of HMGB1 and pCTS-L immunomodulatory properties in human peripheral blood mononuclear cells.
> PMID 41896729 (2026): An RNA-sequencing analysis to determine potential upstream transcriptional regulators of essential amino acid deficiency responses in bovine mammary epithelial cells.
> PMID 31172578 (2019): A systematic genetic analysis and visualization of phenotypic heterogeneity among orofacial cleft GWAS signals.
> PMID 34572451 (2021): Stationed or Relocating: The Seesawing EMT/MET Determinants from Embryonic Development to Cancer Metastasis.
> PMID 20049431 (2010): Regulation of immunity and oncogenesis by the IRF transcription factor family.
> PMID 27919694 (2017): Neuron-specific SUMO knockdown suppresses global gene expression response and worsens functional outcome after transient forebrain ischemia in mice.
> PMID 24726753 (2014): Sox2 promotes malignancy in glioblastoma by regulating plasticity and astrocytic differentiation.

<a id="e17a"></a>**E17a** literature_search, Europe PMC abstract, PMID 40998781 (https://europepmc.org/article/MED/40998781; retrieved 2026-10-26T13:17:20+00:00)

> Identifying noncoding single nucleotide variants (SNVs) in regulatory DNA linked to polygenic disease risk, the transcription factors (TFs) they bind, and the genes they dysregulate is a goal in polygenic disease research.

<a id="e17b"></a>**E17b** literature_search, Europe PMC abstract, PMID 40998781 (https://europepmc.org/article/MED/40998781; retrieved 2026-10-26T13:17:20+00:00)

> Population sampling CUT&RUN of 27 homeostatic TFs identified allele-specific DNA binding (ASB) differences at daSNVs enriched near epidermal homeostasis and monogenic skin disease genes, with notable representation of SP/KLF and AP-1/2 TFs.

<a id="e17c"></a>**E17c** literature_search, Europe PMC abstract, PMID 20049431 (https://europepmc.org/article/MED/20049431; retrieved 2026-10-26T13:17:20+00:00)

> Nine interferon regulatory factors (IRFs) compose a family of transcription factors in mammals.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:17:42+00:00)

> No ENCODE ZNF687 ChIP-seq peak contains chr1:209815925:A>G in biosamples matching 'Brain'. Absence can also mean no ZNF687 experiment in that biosample. In other biosamples, 1 ZNF687 peaks do contain the variant: GM12878 (experiments ENCSR859FDL).

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=ETV2%20UTP25%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:17:42+00:00)

> Europe PMC: 0 hits for 'ETV2 UTP25 enhancer'; top 0 with PMIDs:
