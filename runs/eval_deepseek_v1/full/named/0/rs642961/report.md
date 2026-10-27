# rs642961 and Cleft lip (IRF6)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 6 model calls; 130 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## QBiC-SELEX screen

222 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 77.65); Ets, 1 model (best SPDEF, z 42.64); TEA, 4 models (best TEAD1, z -40.19); HSF, 5 models (best HSF5, z -29.76); HSF, 3 models (best HSF1, z -29.65).

## Ranked chains

### 1. H0: Null Hypothesis: No TF-mediated effect of rs642961 on IRF6 or nearby genes influencing Cleft Lip. (p = 0.43)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant rs642961 functions as a passenger mutation or is linked to a truly causal variant, independent of TF binding at this locus.

Falsified if: Any specific TF is shown to be differentially bound by the A or G allele at this enhancer region, affecting target gene expression.

### 2. H2: A allele increases binding to SOX2, leading to protective regulatory changes in IRF6 expression. (p = 0.24)

TF SOX2 (stated coverage own_model; registry own_model), ref allele binds more; element cCRE EH38E2863563 (dELS); gene IRF6; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref allele (A) binds to SOX2 more strongly than the alt allele (G). | weak | [E16](#e16) |
| element | The variant is located in a highly active dELS (EH38E2863563). | supported | [E03](#e03) |
| gene | The differential binding by SOX2 influences the regulatory state of IRF6. | weak | [E02](#e02), [E05](#e05) |
| cell_type | The impact occurs within a relevant developmental cell type. | missing | none |
| phenotype | The regulatory consequence leads to an increased risk of Orofacial cleft associated with the A allele. | weak | [E04](#e04), [E06](#e06) |

Predictions: Increased binding affinity of the A allele (ref) for SOX2 leads to altered IRF6 regulation, consistent with E04.

Falsified if: Ref binding to SOX2 is unaffected by the A>G substitution.; The directionality of the SOX2 binding change is inconsistent across QBiC-SELEX models (E06).

### 3. H4: Reference allele (A) increases binding to TEAD1, disrupting developmental transcription factor activity affecting IRF6. (p = 0.19)

TF TEAD1 (stated coverage own_model; registry own_model), ref allele binds more; element cCRE EH38E2863563 (dELS); gene IRF6; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref allele (A) binds to TEAD1 more strongly than the alt allele (G). | weak | [E10](#e10) |
| element | The variant is located in a regulatory enhancer element (dELS). | supported | [E03](#e03) |
| gene | The binding change influences the regulatory output of IRF6. | weak | [E02](#e02), [E05](#e05) |
| cell_type | The functional impact occurs within a relevant developmental cell type. | missing | none |
| phenotype | The resulting alteration in IRF6 regulation contributes to the risk of Orofacial cleft associated with the A allele. | weak | [E04](#e04), [E06](#e06) |

Predictions: TEAD1 binding is increased by the A allele, leading to altered IRF6 regulation and consistent with E04.

Falsified if: TEAD1 binding is unaffected by the A>G substitution.

### 4. H3: G allele increases binding to ETV5, affecting IRF6 expression in developmental pathways (Directional Conflict). (p = 0.10)

TF ETV5 (stated coverage own_model; registry own_model), alt allele binds more; element cCRE EH38E2863563 (dELS); gene IRF6; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele (G) binds to ETV5 more strongly than the ref allele (A). | weak | [E08](#e08) |
| element | The variant is located in a functional regulatory element (dELS). | supported | [E03](#e03) |
| gene | The binding change affects the regulatory landscape of IRF6. | weak | [E02](#e02), [E05](#e05) |
| cell_type | The functional impact occurs within a relevant developmental cell type. | missing | none |
| phenotype | The alteration in IRF6 regulation contributes to the risk of Orofacial cleft associated with the G allele. | missing | [E04](#e04) |

Predictions: ETV5 binding is increased by the G allele, leading to altered IRF6 regulation and contributing to Cleft Lip risk.

Falsified if: ETV5 binding is unaffected by the A>G substitution.; The effect allele for Orofacial cleft is found to be A (E04).

### 5. H1: G allele increases binding to TFAP2B, altering developmental gene regulation leading to Cleft Lip risk (Directional Conflict). (p = 0.05)

TF TFAP2B (stated coverage own_model; registry own_model), alt allele binds more; element cCRE EH38E2863563 (dELS); gene IRF6; cell type None.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele (G) binds to TFAP2B more strongly than the ref allele (A). | weak | [E13](#e13) |
| element | The variant disrupts the regulatory function of the enhancer EH38E2863563, which is a dELS. | weak | [E03](#e03) |
| gene | The binding change at the dELS influences the expression of the developmental gene IRF6. | weak | [E02](#e02), [E05](#e05) |
| cell_type | The functional impact occurs within a relevant developmental cell type. | missing | none |
| phenotype | This altered regulation leads to an increased risk of Orofacial cleft (Cleft Lip) associated with the G allele. | missing | [E04](#e04), [E06](#e06) |

Predictions: The G allele increases TFAP2B occupancy at the enhancer, altering the regulatory output towards IRF6.; The G allele increases risk of ORAL cleft.

Falsified if: TFAP2B binding is unaffected by the A>G substitution.; IRF6 expression remains unchanged despite altered TFAP2B binding.; The effect allele for Orofacial cleft is found to be A (E04).

## Prediction matrix

| Test | Cost | Separates top two | H0 | H2 | H4 | H3 | H1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Literature search to find functional evidence of TF binding changes (e.g., EMSA, Reporter assays) related to rs642961 and IRF6. | low | no |  | No direct evidence of functional TF binding difference found. | No direct evidence of functional TF binding difference found. | No direct evidence of functional TF binding difference found. | No direct evidence of functional TF binding difference found. |
| GTEx eQTL lookup for IRF6 associated with rs642961. | medium | yes | No eQTL association found. | eQTL association found. | eQTL association found. | No eQTL association found. | No eQTL association found. |
| CRISPR perturbation of IRF6 expression using guide RNAs in relevant developmental cell lines. | high | yes | No phenotypic effect observed. | Phenotype changes (Cleft Lip related) observed. | Phenotype changes (Cleft Lip related) observed. | Phenotype changes (Cleft Lip related) observed. | Phenotype changes (Cleft Lip related) observed. |

## Next experiment

literature_search

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs642961&size=100; retrieved 2026-10-25T17:29:42+00:00)

> 8 GWAS Catalog associations for rs642961, strongest first:
> Systolic blood pressure: p 6.0e-12, effect allele G, risk-allele frequency NR, PMID 38689001
> Hypertension: p 2.0e-08, effect allele A, risk-allele frequency 0.1951, PMID 33230300
> Pulse pressure: p 1.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Diastolic blood pressure: p 3.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Orofacial clefts: p 2.0e-06, effect allele A, risk-allele frequency NR, PMID 19270707

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:41+00:00)

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

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20AND%20UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:43+00:00)

> Europe PMC: 2 hits for 'rs642961 AND UTP25 AND "cleft lip"'; top 2 with PMIDs:
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:209815925:A>G: 997 models scored, 222 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 140 CIS-BP groups. Expression context: none: expression filter skipped. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 0. Passing groups ranked below the ones shown: 130. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 77.65, effect 1.32 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: ETV5 z 77.65, ETS2 z 47.72, ETV2 z 31.41, ETV4 z 30.23, ETS1 z 27.66 (+13 more). TFs this group covers: EHF (mapped), ELF1 (own model), ELF2 (own model), ELF3 (own model), ELF4 (own model), ELF5 (own model), ELK1 (own model), ELK3 (own model), ELK4 (own model), ERF (own model) (+15 more); best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G345 (Ets, 1 model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (own model of SPDEF), z 42.64, effect 1.62 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SPDEF z 42.64. TFs this group covers: ELF1 (own model), ELF2 (own model), ELF4 (own model), SPDEF (own model); best model's site strength: ref 89.2th, alt 99.8th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G031 (TEA, 4 models): best model TEAD1_FL_TCACGC40NACT_KW_yin2017_0_4_7mer (own model of TEAD1), z -40.19, effect -2.547 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TEAD1 z -40.19, TEAD2 z -39.78, TEAD3 z -32.45, TEAD4 z -26.55. TFs this group covers: TEAD1 (own model), TEAD2 (own model), TEAD3 (own model), TEAD4 (own model); best model's site strength: ref 99.4th, alt 75.7th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G014 (HSF, 5 models): best model HSF5_eDBD_TATGCT40NACT_KT_yin2017_0_3_7mer (own model of HSF5), z -29.76, effect -0.875 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: HSF5 z -29.76, HSFY2 z -12.29. TFs this group covers: HSF5 (own model), HSFX1 (own model), HSFX2 (own model), HSFY1 (own model), HSFY2 (own model); best model's site strength: ref 99.4th, alt 92.8th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G039 (HSF, 3 models): best model HSF1_eDBD_TCTAAA40NCGC_KN_yin2017_0_4_7mer (own model of HSF1), z -29.65, effect -1.427 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: HSF1 z -29.65, HSF4 z -26.38, HSF2 z -25.12. TFs this group covers: HSF1 (own model), HSF2 (own model), HSF4 (own model); best model's site strength: ref 100.0th, alt 90.6th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2B_FL_TGTCCG20NGA_KH_nitta2015_1_3_7mer (own model of TFAP2B), z 23.98, effect 1.688 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: TFAP2B z 23.98, TFAP2C z 17.39, TFAP2E z 13.97, TFAP2A z 11.94. TFs this group covers: TFAP2A (own model), TFAP2B (own model), TFAP2C (own model), TFAP2D (mapped), TFAP2E (own model); best model's site strength: ref 78.9th, alt 99.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G226 (CSD, 1 model): best model LIN28B_FL_TTTGAC40NGGT_KV_yin2017_0_4_7mer (own model of LIN28B), z 23.9, effect 1.4 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: LIN28B z 23.9. TFs this group covers: LIN28A (mapped), LIN28B (own model); best model's site strength: ref 91.1th, alt 99.8th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G624 (C2H2 ZF, 1 model): best model ZSCAN1_eDBD_TGCTCC40NCCG_KP_yin2017_0_3_7mer (own model of ZSCAN1), z 22.54, effect 1.648 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZSCAN1 z 22.54. TFs this group covers: ZSCAN1 (own model); best model's site strength: ref 98.4th, alt 99.8th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G005 (HMG/Sox, 18 models): best model SOX2_FL_GT40NGCGTGT_YWEA_jolma2025_0_4_7mer (own model of SOX2), z -22.53, effect -1.646 (alt binds less); 10 passing models (9 with the best model's sign); members disagree on direction. Passing members: SOX2 z -22.53, SOX15 z -15.68, SOX14 z -13.1, SOX7 z -11.77, SRY z -8.47 (+5 more). TFs this group covers: SOX1 (own model), SOX10 (own model), SOX11 (own model), SOX12 (own model), SOX13 (mapped), SOX14 (own model), SOX15 (own model), SOX17 (own model), SOX18 (own model), SOX2 (own model) (+10 more); best model's site strength: ref 99.6th, alt 82.8th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G066 (EBF1, 2 models): best model EBF4_FL_TCGATT40NTTG_KK_nitta2015_1_3_7mer (own model of EBF4), z 17.47, effect 0.682 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: EBF4 z 17.47, EBF1 z 13.33. TFs this group covers: EBF1 (own model), EBF2 (mapped), EBF3 (mapped), EBF4 (own model); best model's site strength: ref 99.7th, alt 99.7th percentile of its k-mer coefficients.
