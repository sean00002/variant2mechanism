# rs13078086 and Colorectal cancer

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 161 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen

209 of 997 models pass the gate. Top groups: EBF1, 2 models (best EBF4, z -60.28); C2H2 ZF, 1 model (best ZNF696, z 23.6); AP-2, 4 models (best TFAP2E, z -18.37); C2H2 ZF, 1 model (best ZNF343, z 15.69); Ets, 18 models (best ETV5, z 13.11).

## Ranked chains

### 1. null: Null: no TF-mediated effect of rs13078086 (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs13078086 in HCT116.; No allele-specific enhancer/reporter activity for the variant or the adjacent dELS in HCT116.; No colon eQTL or colorectal-cancer association attributable to rs13078086.

Falsified if: Allele-specific ZNF696, TFAP2E, or RFX5 occupancy at rs13078086 is demonstrated in HCT116 or isogenic T/G cells and is lost or gained with the alt allele.; A nearby dELS or the variant itself shows allele-specific regulatory activity that changes PYDC2 or another nearby gene in colorectal cells.; A causal colorectal-cancer association is shown to act through this variant rather than a linked variant or passenger event.

### 2. ZNF696_alt: ZNF696 binds the alt allele more strongly near a dELS (p = 0.17)

TF ZNF696 (stated coverage own_model; registry own_model), alt allele binds more; element The variant is intronic and lies 42 bp from dELS EH38E2269392, not within a cCRE; E03 gives only maxima across ENCODE biosamples, so HCT116-specific activity and allele-specific enhancer function are not established.; gene PYDC2; cell type HCT116 colorectal carcinoma cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF696 has its own QBiC-SELEX model in group G570 and binds the alt G allele more strongly than ref T in vitro (effect 0.733, alt binds more); no ZNF696 ChIP or allele-specific occupancy assay is available. | weak | [E09](#e09), [E07](#e07) |
| element | The candidate element is the dELS EH38E2269392 42 bp away; the variant does not overlap a cCRE, and HCT116-specific enhancer activity is not shown. | weak | [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene and is listed near the dELS, but the variant is intronic in PYDC2-AS1 and GTEx reports no colon-transverse eQTL for this variant; the gene link is proximity-only. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E19](#e19) |
| cell_type | ZNF696 is expressed in the HCT116 DepMap context at 8.26 TPM, supporting expression in the relevant cell type but not occupancy or function. | supported | [E07](#e07), [E09](#e09) |
| phenotype | No GWAS Catalog or Open Targets association supports rs13078086, and Open Targets reports no PYDC2 colorectal-cancer association; the phenotype link is speculative, and the downstream direction of ZNF696 activity is unknown. | missing | [E04](#e04), [E05](#e05), [E06](#e06), [E20](#e20) |

Predictions: ZNF696 ChIP/CUT&RUN is stronger at the alt G allele than the ref T allele at rs13078086 in HCT116 or isogenic T/G cells.; An allele-specific reporter/MPRA containing the variant shows alt-dependent ZNF696-sensitive activity if ZNF696 acts as an activator.; ZNF696 perturbation changes PYDC2 or nearby gene expression; the sign depends on whether ZNF696 activates or represses.

Falsified if: ZNF696 does not bind the rs13078086 region in HCT116 or isogenic T/G cells.; ZNF696 occupancy is not higher on the alt G allele than the ref T allele.; ZNF696 perturbation does not alter PYDC2 or another nearby gene in colorectal cells.

### 3. RFX5_RFX_ref: RFX5 binds the ref allele more strongly near a dELS (p = 0.15)

TF RFX5 (stated coverage own_model; registry own_model), ref allele binds more; element The variant lies 42 bp from dELS EH38E2269392 and does not overlap a cCRE; E03 does not establish HCT116-specific activity, contact with PYDC2, or allele-specific enhancer function.; gene PYDC2; cell type HCT116 colorectal carcinoma cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | RFX5 has its own QBiC-SELEX model in RFX group G094 and binds the ref T allele more strongly than alt G in vitro (effect -1.452, alt binds less); no RFX5 ChIP or allele-specific occupancy assay is available. | weak | [E15](#e15), [E07](#e07) |
| element | The candidate element is the dELS EH38E2269392 42 bp away; no cCRE overlaps the variant, and HCT116-specific activity is not shown. | weak | [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene and a cCRE-nearby gene, but the variant is intronic in PYDC2-AS1 and no colon-transverse eQTL supports regulation; the gene link is proximity-only. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E19](#e19) |
| cell_type | RFX5 is strongly expressed in the HCT116 DepMap context at 20.42 TPM, supporting cell-type expression but not allele-specific occupancy. | supported | [E07](#e07), [E15](#e15) |
| phenotype | No GWAS Catalog or Open Targets association supports rs13078086, and PYDC2 has no Open Targets colorectal-cancer association; the phenotype link is speculative. | missing | [E04](#e04), [E05](#e05), [E06](#e06), [E20](#e20) |

Predictions: RFX5 ChIP/CUT&RUN is stronger at the ref T allele than the alt G allele at rs13078086 in HCT116 or isogenic T/G cells.; The alt allele reduces RFX5-dependent reporter activity if the nearby dELS is tested.; RFX5 knockdown changes PYDC2 or nearby gene expression if this chain is correct.

Falsified if: RFX5 does not occupy the rs13078086 region in HCT116 or isogenic T/G cells.; RFX5 occupancy is not higher on the ref T allele than the alt G allele.; RFX5 perturbation does not affect the nearby dELS or PYDC2/nearby gene expression.

### 4. TFAP2E_AP2_ref: AP-2/TFAP2E binds the ref allele more strongly at a dELS near PYDC2 (p = 0.13)

TF TFAP2E (stated coverage own_model; registry own_model), ref allele binds more; element The variant is 42 bp from dELS EH38E2269392 and does not overlap a cCRE; E03 reports only maxima across ENCODE biosamples, so HCT116-specific dELS activity and allele-specific function remain unproven.; gene PYDC2; cell type HCT116 colorectal carcinoma cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2E has its own QBiC-SELEX model in AP-2 group G030 and binds the ref T allele more strongly than alt G in vitro (effect -0.765, alt binds less); however, Factorbook reports no TFAP2E ChIP-seq peak containing rs13078086 in HCT116, which weakens the occupancy claim. | weak | [E10](#e10), [E07](#e07), [E18](#e18) |
| element | The candidate element is the dELS EH38E2269392 42 bp away; the variant does not overlap a cCRE, and HCT116-specific enhancer activity is not established. | weak | [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene and is listed near the dELS, but the variant is intronic in PYDC2-AS1 and no colon-transverse eQTL supports regulation; the gene link is proximity-only. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E19](#e19) |
| cell_type | TFAP2E is expressed in the HCT116 DepMap context at 8.5 TPM, supporting expression but not occupancy or allele-specific function. | supported | [E07](#e07), [E10](#e10) |
| phenotype | No GWAS Catalog or Open Targets association supports rs13078086, and PYDC2 has no Open Targets colorectal-cancer association; the phenotype link is speculative. | missing | [E04](#e04), [E05](#e05), [E06](#e06), [E20](#e20) |

Predictions: TFAP2E ChIP/CUT&RUN is stronger at the ref T allele than the alt G allele at rs13078086 in HCT116 or isogenic T/G cells.; The dELS EH38E2269392 shows allele-specific enhancer activity if tested in HCT116.; PYDC2 expression is sensitive to TFAP2E perturbation if this chain is correct.

Falsified if: TFAP2E does not occupy the rs13078086 region in HCT116 or isogenic T/G cells when assayed.; TFAP2E occupancy is not higher on the ref T allele than the alt G allele.; Editing T>G does not reduce TFAP2E-dependent reporter activity or alter nearby gene expression.

## Prediction matrix

| Test | Cost | Separates top two | null | ZNF696_alt | RFX5_RFX_ref | TFAP2E_AP2_ref |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ZNF696 ChIP-qPCR or CUT&RUN-qPCR at rs13078086 in HCT116 or isogenic T/G cells | medium | yes | No allele-specific ZNF696 occupancy at rs13078086. | ZNF696 occupancy is higher on the alt G allele than the ref T allele. | No allele-specific ZNF696 occupancy; RFX5 may show ref-more binding. | No allele-specific ZNF696 occupancy; TFAP2E may show ref-more binding if detectable. |
| Allele-specific TFAP2E ChIP-qPCR or CUT&RUN-qPCR at rs13078086 in HCT116 or isogenic T/G cells | medium | no | No allele-specific TFAP2E occupancy at rs13078086. | No allele-specific TFAP2E occupancy. | No allele-specific TFAP2E occupancy. | TFAP2E occupancy is higher on the ref T allele than the alt G allele. |
| Allele-specific RFX5 ChIP-qPCR or CUT&RUN-qPCR at rs13078086 in HCT116 or isogenic T/G cells | medium | no | No allele-specific RFX5 occupancy at rs13078086. | No allele-specific RFX5 occupancy. | RFX5 occupancy is higher on the ref T allele than the alt G allele. | No allele-specific RFX5 occupancy. |
| Allele-specific reporter/MPRA of a 200-500 bp region around rs13078086 in HCT116 | medium | yes | No allele-specific reporter activity for the variant or adjacent dELS. | Alt-dependent reporter activity is present if ZNF696 acts as an activator; direction depends on ZNF696 function. | Ref-dependent reporter activity is reduced by the alt allele. | Ref-dependent reporter activity is reduced by the alt allele. |
| ZNF696 knockdown or overexpression followed by PYDC2/nearby gene expression in HCT116 | medium | yes | No change in PYDC2 or nearby gene expression after ZNF696 perturbation. | PYDC2 or a nearby gene changes after ZNF696 knockdown/overexpression; sign depends on activator versus repressor. | No change after ZNF696 perturbation; change may follow RFX5 perturbation. | No change after ZNF696 perturbation; change may follow TFAP2E perturbation. |

## Next experiment

The single cheapest experiment that separates the top two chains is allele-specific ZNF696 ChIP-qPCR or CUT&RUN-qPCR at rs13078086 in HCT116 or isogenic T/G cells; it directly tests the null prediction of no allele-specific ZNF696 occupancy against the ZNF696_alt prediction of stronger alt-allele binding.

## Investigate calls

- chip_peaks({"tf": "TFAP2E", "biosample": "HCT116"})
- eqtl_lookup({"tissue": "Colon - Transverse"})
- gene_disease({"gene": "PYDC2"})

## Flags

- literature_fallback: no hits for 'rs13078086 AND PYDC2 AND "colorectal cancer"'; dropped the rsID

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/3:191441666-191441666:1/G?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:32:09+00:00)

> Variant chr3:191441666:T>G (GRCh38), allele string T/G
> Known IDs: rs13078086
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: -1.82
> Transcript consequences: PYDC2-AS1 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/3:190441666-192441666?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:06+00:00)

> 8 protein-coding genes within 1000 kb of chr3:191441666:T>G, by distance to TSS:
> PYDC2: 19.5 kb from TSS (upstream, strand +1)
> UTS2B: 111.1 kb from TSS (upstream, strand -1)
> CCDC50: 112.6 kb from TSS (downstream, strand +1)
> OSTN: 242.4 kb from TSS (downstream, strand +1)
> GMNC: 549.2 kb from TSS (upstream, strand -1)
> IL1RAP: 954.2 kb from TSS (downstream, strand +1)
> TMEM207: 991.8 kb from TSS (upstream, strand -1)
> FGF12: 1326.1 kb from TSS (downstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:05+00:00)

> No cCRE overlaps the variant; nearest is EH38E2269392 (dELS) 42 bp away.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2269392 dELS: DNase z 3.5, H3K27ac z 1.8, H3K4me3 z 1.5, CTCF z 1.5; nearby genes AC073365.1, PYDC2, CCDC50
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs13078086&size=100; retrieved 2026-10-25T17:32:10+00:00)

> 0 GWAS Catalog associations for rs13078086, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:09+00:00)

> Open Targets has no record of 3_191441666_T_G.

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PYDC2%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:10+00:00)

> Europe PMC: 16 hits for 'PYDC2 AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 40026444 (2025): Correlation Analysis of Pyroptosis-Related Genes CASP1, NLRP3, AIM2, and NLRP1 With Lung Adenocarcinoma.
> PMID 41154652 (2025): Oncogenic Role of SAMD4B in Breast Cancer Progression by Activating Wnt/β-Catenin Pathway.
> PMID 36319832 (2022): A novel refined pyroptosis and inflammasome-related genes signature for predicting prognosis and immune microenvironment in pancreatic ductal adenocarcinoma.
> PMID 36341349 (2022): The strategies of NLRP3 inflammasome to combat <i>Toxoplasma gondii</i>.
> PMID 36732864 (2023): RNA binding protein SAMD4: current knowledge and future perspectives.
> PMID 39561929 (2024): Optimizing iNKT-driven immune responses against cancer by modulating CD1d in tumor and antigen presenting cells.
> PMID 35159382 (2022): Metabolomics of Acute vs. Chronic Spinach Intake in an Apc-Mutant Genetic Background: Linoleate and Butanoate Metabolites Targeting HDAC Activity and IFN-γ Signaling.
> PMID 35338151 (2022): PUMILIO proteins promote colorectal cancer growth via suppressing p21.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr3:191441666:T>G: 997 models scored, 209 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 174 CIS-BP groups. Expression context: DepMap line ACH-000971. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 37 (C2H2 ZF, 1 model z 38.3, Ets, 3 models z -10.94, bHLH, 2 models z -10.76, C2H2 ZF, 1 model z 7.66, bHLH, 1 model z -7.64). Passing groups ranked below the ones shown: 127. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G066 (EBF1, 2 models): best model EBF4_FL_TCGATT40NTTG_KK_nitta2015_1_3_7mer (own model of EBF4), z -60.28, effect -1.954 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: EBF4 z -60.28, EBF1 z -28.35. TFs this group covers: EBF4 (own model) 1.22 TPM, EBF2 (mapped) 0.73 TPM, EBF1 (own model) 0.18 TPM, EBF3 (mapped) 0.06 TPM; best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G570 (C2H2 ZF, 1 model): best model ZNF696_FL_AG40NTGGCTA_YWSA_jolma2025_0_2_7mer (own model of ZNF696), z 23.6, effect 0.733 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF696 z 23.6. TFs this group covers: ZNF696 (own model) 8.26 TPM; best model's site strength: ref 56.3th, alt 99.2th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (own model of TFAP2E), z -18.37, effect -0.765 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TFAP2E z -18.37, TFAP2A z -16.2, TFAP2B z -13.18, TFAP2C z -5.14. TFs this group covers: TFAP2E (own model) 8.5 TPM, TFAP2A (own model) 6.18 TPM, TFAP2C (own model) 2.59 TPM, TFAP2B (own model) 0.0 TPM, TFAP2D (mapped) 0.0 TPM; best model's site strength: ref 99.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G490 (C2H2 ZF, 1 model): best model ZNF343_eDBD_TGGCGT40NCCT_KT_yin2017_0_3_7mer (own model of ZNF343), z 15.69, effect 0.778 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF343 z 15.69. TFs this group covers: ZNF343 (own model) 9.63 TPM; best model's site strength: ref 98.3th, alt 98.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 13.11, effect 0.251 (alt binds more); 4 passing models (2 with the best model's sign); members disagree on direction. Passing members: ETV5 z 13.11, ELF1 z -7.84, FLI1 z 5.19, ELF2 z -4.96. TFs this group covers: EHF (mapped) 88.58 TPM, ELK3 (own model) 51.39 TPM, ERF (own model) 46.58 TPM, ETV4 (own model) 36.17 TPM, ELF3 (own model) 33.75 TPM, ELK1 (own model) 26.37 TPM, ETS2 (own model) 25.48 TPM, ETV5 (own model) 25.15 TPM, ELF1 (own model) 24.76 TPM, ELF2 (own model) 19.32 TPM (+15 more); best model's site strength: ref 94.6th, alt 95.3th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G028 (RFX, 4 models): best model RFX2_NA_TAACCC20NCCA_ESY_yang2017_0_3_7mer (own model of RFX2), z -12.18, effect -1.006 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: RFX2 z -12.18, RFX1 z -6.72, RFX4 z -4.83. TFs this group covers: RFX2 (own model) 6.73 TPM, RFX1 (own model) 3.61 TPM, RFX3 (own model) 2.61 TPM, RFX4 (own model) 0.01 TPM, RFX6 (mapped) 0.0 TPM; best model's site strength: ref 98.8th, alt 96.5th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G449 (C2H2 ZF, 1 model): best model ZNF174_eDBD_TACCGA40NATA_KS_yin2017_1_3_7mer (own model of ZNF174), z 11.98, effect 0.325 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF174 z 11.98. TFs this group covers: ZNF174 (own model) 7.86 TPM; best model's site strength: ref 92.7th, alt 94.5th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G094 (RFX, 2 models): best model RFX5_eDBD_TTGATG40NATC_KO_yin2017_0_4_7mer (own model of RFX5), z -11.73, effect -1.452 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: RFX5 z -11.73. TFs this group covers: RFX5 (own model) 20.42 TPM, RFX7 (own model) 10.12 TPM; best model's site strength: ref 99.3th, alt 98.5th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G560 (C2H2 ZF, 1 model): best model ZNF668_FL_TC40NGTTTTG_YWSA_jolma2025_0_3_7mer (own model of ZNF668), z 10.82, effect 0.699 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF668 z 10.82. TFs this group covers: ZNF668 (own model) 8.44 TPM; best model's site strength: ref 84.5th, alt 95.3th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G373 (Unknown, 1 model): best model TMF1_DBD_CA40NTCGATG_YWPA_jolma2025_0_2_7mer (own model of TMF1), z 10.65, effect 0.85 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: TMF1 z 10.65. TFs this group covers: TMF1 (own model) 14.51 TPM; best model's site strength: ref 66.7th, alt 98.2th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:42:51+00:00)

> No ENCODE TFAP2E ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT116'. Absence can also mean no TFAP2E experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (G) relative to ref (T).

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575).
