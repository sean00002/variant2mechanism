# rs642961 and Cleft lip (IRF6)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 11 model calls; 398 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ZNF687 (bound elsewhere, z -0.21, no clear allelic change). Occupancy unknown: ETV2 (z 77.65); ETV3 (z 77.65); ETV3L (z 77.65); FEV (z 77.65); FLI1 (z 77.65). Diagnostic, not shown to the model: 222 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: TFAP2A drives altered IRF6 regulation via allele-specific enhancer binding (p = 0.60)

TF TFAP2A (QBiC-SELEX coverage own_model), alt allele binds more; element dELS (EH38E2863563); gene IRF6; cell type Oral epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele (G) increases TFAP2A binding in QBiC-SELEX models; literature reports that rs642961 abrogates AP2A binding at MCS9.7, consistent with the risk allele A reducing TFAP2A occupancy. ENCODE has no TFAP2A ChIP peak at this exact site, so occupancy is inferred from the literature rather than ENCODE. | supported | [E17](#e17), [E18](#e18), [E19f](#e19f) |
| element | The variant is located within an active distal enhancer-like region (dELS) with DNase and H3K27ac enhancer marks. | weak | [E3](#e3) |
| gene | TFAP2A binding at the MCS9.7 enhancer regulates IRF6, a gene required for oral epithelial development and orofacial cleft risk. | weak | [E19a](#e19a), [E19e](#e19e), [E19f](#e19f) |
| cell_type | The functional regulatory activity is relevant to oral epithelium, including fetal oral epithelial cells used in enhancer assays. | weak | [E19a](#e19a), [E19c](#e19c) |
| phenotype | Reduced TFAP2A binding and altered IRF6 enhancer activity contribute to orofacial cleft risk; rs642961 is associated with orofacial clefts with effect allele A. | weak | [E6](#e6), [E19e](#e19e) |

Predictions: The alt allele G increases TFAP2A binding at the variant site.; The risk allele A reduces TFAP2A occupancy and IRF6 enhancer activity in oral epithelial cells.

Falsified if: TFAP2A does not bind the rs642961-containing enhancer in oral epithelial cells.; The A and G alleles show no TFAP2A-dependent difference in IRF6 enhancer activity.

### 2. H2: ETV3 modulates IRF6 via increased alt allele binding affinity (p = 0.25)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element dELS (EH38E2863563); gene IRF6; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele (G) increases ETV3 binding in QBiC-SELEX through a CIS-BP-mapped ETV5 model; ETV3 occupancy at this site is unknown because no ETV3 ChIP peak is shown. | weak | [E13](#e13) |
| element | The variant is located within an active distal enhancer-like region (dELS). | weak | [E3](#e3) |
| gene | The alt allele G is associated with lower IRF6 expression in brain eQTL data; no craniofacial-cell eQTL is provided for ETV3-dependent IRF6 regulation. | weak | [E8](#e8) |
| cell_type | The regulatory effect would need to occur in cells relevant to craniofacial development, but no cell-type evidence is provided. | missing | none |
| phenotype | If ETV3 represses IRF6, increased alt-allele ETV3 binding would lower IRF6 and could contribute to cleft lip risk; however, the cleft association in E6 is with allele A, opposite the alt-G binding increase, so this chain is weak. | weak | [E6](#e6), [E8](#e8) |

Predictions: The alt allele G increases ETV3 binding at the variant site.; ETV3 occupancy at this element alters IRF6 expression in a craniofacial cell type.

Falsified if: ETV3 does not occupy the rs642961-containing enhancer in relevant cells.; Changing ETV3 binding does not affect IRF6 expression.

### 3. H0: Null Hypothesis: Variant acts via linkage or passenger effect (p = 0.15)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant rs642961 influences Cleft lip phenotype through a mechanism unrelated to direct TF binding at this specific enhancer element.

Falsified if: A functional TF-mediated regulatory change is identified at the variant locus affecting IRF6 or other critical downstream genes.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H0 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific enhancer reporter assay in HEPM fetal oral epithelial cells comparing A and G alleles, with and without TFAP2A knockdown | medium | yes | A/G difference in enhancer activity that is TFAP2A-dependent; alt G shows stronger TFAP2A binding. | A/G difference in enhancer activity that is not explained by TFAP2A; possible ETV3-dependent effect remains untested. | No allele-specific difference in enhancer activity. |
| ChIP-qPCR for TFAP2A and ETV3 at the rs642961 enhancer in HEPM cells | high | yes | TFAP2A occupancy is detected and is allele-dependent. | ETV3 occupancy is detected at the element; TFAP2A occupancy is not allele-dependent. | No specific TF occupancy at the variant-containing element. |

## Next experiment

Allele-specific enhancer reporter assay in HEPM fetal oral epithelial cells comparing A and G alleles, with and without TFAP2A knockdown

## Investigate calls

- qbic_tf_detail({"tf": "TFAP2A"})
- chip_peaks({"tf": "TFAP2A", "biosample": null})
- literature_search({"query": "rs642961 TFAP2A IRF6 cleft lip enhancer"})

## Flags

- unknown_evidence_id: H1.element cites ['E3'], not in this run's ledger
- failed_citation: H1.element: cited ['E3'] failed a check; supported -> weak
- unknown_evidence_id: H1.phenotype cites ['E6'], not in this run's ledger
- unknown_evidence_id: H2.element cites ['E3'], not in this run's ledger
- failed_citation: H2.element: cited ['E3'] failed a check; supported -> weak
- unknown_evidence_id: H2.gene cites ['E8'], not in this run's ledger
- unknown_evidence_id: H2.phenotype cites ['E6', 'E8'], not in this run's ledger

Citation support: 0.40 of links cite only evidence that passed every check.

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

> QBiC-SELEX screen of chr1:209815925:A>G, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (none: expression filter skipped), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 1 of 1 occupied, 5 of 249 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 572 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF687 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF687_FL_TA40NGTTAGC_YWL_jolma2025_0_3_7mer (its own model), z -0.21, effect -0.013: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). expression not filtered. Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR859FDL. Best model's site strength: ref 92.7th, alt 88.6th percentile of its k-mer coefficients.

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

<a id="e17"></a>**E17** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TFAP2A","symbol":"TFAP2A","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr1:209815925:A>G","gate_p":5.02e-05,"models":[{"model":"TCFAP2A_NA_TGATCC20NCG_ESP_yang2017_0_4_7mer","mapping":"own","group":"G030 AP-2, 4 models","quality":0.927,"effect":2.176,"z":11.94,"p":7.3e-33,"rank_abs_z":"41/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":100.0,"k":7}},{"model":"TFAP2B_FL_TGTCCG20NGA_KH_nitta2015_1_3_7mer","mapping":"CIS-BP (TFAP2B)","group":"G030 AP-2, 4 models","quality":0.77,"effect":1.688,"z":23.98,"p":4.3e-127,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":78.9,"alt_percentile":99.9,"k":7}},{"model":"TFAP2C_eDBD_TGAGCT40NGCA_KP_yin2017_0_4_7mer","mapping":"CIS-BP (TFAP2C)","group":"G030 AP-2, 4 models","quality":0.753,"effect":1.495,"z":17.39,"p":1.1e-67,"rank_abs_z":"22/997","passed_gate":true,"site_strength":{"ref_percentile":86.2,"alt_percentile":91.7,"k":7}},{"model":"TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer","mapping":"CIS-BP (TFAP2E)","group":"G030 AP-2, 4 models","quality":0.88,"effect":0.819,"z":13.97,"p":2.4e-44,"rank_abs_z":"33/997","passed_gate":true,"site_strength":{"ref_percentile":89.1,"alt_percentile":89.6,"k":7}}]}

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:31:05+00:00)

> No ENCODE TFAP2A ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no TFAP2A experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20TFAP2A%20IRF6%20cleft%20lip%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:40:17+00:00)

> Europe PMC: 24 hits for 'rs642961 TFAP2A IRF6 cleft lip enhancer'; top 8 with PMIDs:
> PMID 42799765 (2026): The orofacial cleft risk gene IRF6 is a target gene of SOX9 in cranial neural crest cells.
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 40918684 (2025): Functional Validation of Noncoding Variants Associated With Nonsyndromic Orofacial Cleft.
> PMID 34310873 (2021): Family based and case-control designs reveal an association of TFAP2A in nonsyndromic cleft lip only among Vietnamese population.
> PMID 35110662 (2022): Allele-specific transcription factor binding in a cellular model of orofacial clefting.
> PMID 35226783 (2022): Revisiting the embryogenesis of lip and palate development.
> PMID 29913133 (2018): IRF6 and AP2A Interaction Regulates Epidermal Development.
> PMID 30689861 (2019): The TFAP2A-IRF6-GRHL3 genetic pathway is conserved in neurulation.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 42799765 (https://europepmc.org/article/MED/42799765; retrieved 2026-10-26T02:40:17+00:00)

> Its expression in the oral epithelium depends on the transcription factor TFAP2A.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 42799765 (https://europepmc.org/article/MED/42799765; retrieved 2026-10-26T02:40:17+00:00)

> The IRF6 enhancer MCS-9.7 is bound and activated by the transcription factor SOX9, mutations of which cause Pierre Robin sequence, a craniofacial anomaly that includes cleft palate.

<a id="e19c"></a>**E19c** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-26T02:40:17+00:00)

> To identify candidates for functional SNPs at eight such loci we conduct a massively parallel reporter assay in a fetal oral epithelial cell line, revealing SNPs with allele-specific effects on enhancer activity.

<a id="e19d"></a>**E19d** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-26T02:40:17+00:00)

> Conditional analyses of GWAS data suggest the two functional SNPs near IRF6 account for the majority of risk for CL/P at this locus.

<a id="e19e"></a>**E19e** literature_search, Europe PMC abstract, PMID 29913133 (https://europepmc.org/article/MED/29913133; retrieved 2026-10-26T02:40:17+00:00)

> Additionally, a variant in an enhancer (MCS9.7) that regulates IRF6 is associated with risk for isolated orofacial clefting.

<a id="e19f"></a>**E19f** literature_search, Europe PMC abstract, PMID 29913133 (https://europepmc.org/article/MED/29913133; retrieved 2026-10-26T02:40:17+00:00)

> This variant (rs642961) abrogates AP2A protein binding at MCS9.7.

<a id="e19g"></a>**E19g** literature_search, Europe PMC abstract, PMID 34310873 (https://europepmc.org/article/MED/34310873; retrieved 2026-10-26T02:40:17+00:00)

> TFAP2A rs1675414 was associated with NSCLO, replicated by both case-control and family based tests.

<a id="e19h"></a>**E19h** literature_search, Europe PMC abstract, PMID 34310873 (https://europepmc.org/article/MED/34310873; retrieved 2026-10-26T02:40:17+00:00)

> The current investigation suggests an intriguing role of TFAP2A in the etiology of NSCLO among the Vietnamese population.

<a id="e19i"></a>**E19i** literature_search, Europe PMC abstract, PMID 35110662 (https://europepmc.org/article/MED/35110662; retrieved 2026-10-26T02:40:17+00:00)

> Analysing the craniofacial TF TFAP2A in human embryonic palatal mesenchyme (HEPM) cells, we identified 2845 TFAP2A ChIP-seq peaks, several of which were located near nsCL/P candidate genes (e.g. MSX1 and SPRY2).

<a id="e19j"></a>**E19j** literature_search, Europe PMC abstract, PMID 35110662 (https://europepmc.org/article/MED/35110662; retrieved 2026-10-26T02:40:17+00:00)

> Integration with nsCL/P GWAS data, however, did not show robust evidence for co-localization of common nsCL/P risk variants with TFAP2A ChIP-seq peaks.

<a id="e19k"></a>**E19k** literature_search, Europe PMC abstract, PMID 30689861 (https://europepmc.org/article/MED/30689861; retrieved 2026-10-26T02:40:17+00:00)

> Mutations in IRF6, TFAP2A and GRHL3 cause orofacial clefting syndromes in humans.
