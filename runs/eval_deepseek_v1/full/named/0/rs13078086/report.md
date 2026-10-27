# rs13078086 and Colorectal cancer

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 99 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen

209 of 997 models pass the gate. Top groups: EBF1, 2 models (best EBF4, z -60.28); C2H2 ZF, 1 model (best ZNF696, z 23.6); AP-2, 4 models (best TFAP2E, z -18.37); C2H2 ZF, 1 model (best ZNF343, z 15.69); Ets, 18 models (best ETV5, z 13.11).

## Ranked chains

### 1. null_no_tf_mediated_effect: No TF-mediated effect of rs13078086; indirect or linked association only (p = 0.78)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at rs13078086.; QBiC-SELEX signals are in vitro only and do not translate into chromatin or expression effects.; Any disease association, if real, is due to a linked variant, a passenger event, or no causal effect at this site.

Falsified if: Allele-specific TF binding at rs13078086 is demonstrated together with a reproducible effect on PYDC2-AS1/PYDC2 expression or chromatin state in colorectal cancer cells.

### 2. EBF4_ref_less_alt: EBF4 binds ref more at a PYDC2-AS1 intronic site; local regulatory consequence unproven (p = 0.09)

TF EBF4 (stated coverage own_model; registry own_model), ref allele binds more; element rs13078086 lies in a PYDC2-AS1 intron, does not overlap an annotated cCRE, and is 42 bp from dELS EH38E2269392, so any EBF4 site would be in flanking sequence near but not within the annotated element core.; gene PYDC2-AS1/PYDC2; cell type HCT116 is the supplied expression context; EBF4 is expressed at only 1.22 TPM, lower than several other candidates, and no EBF4 ChIP-seq data are provided, so occupancy in HCT116 is unproven..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | EBF4 binds the ref T allele more strongly than the alt G allele; QBiC-SELEX group G066 has best own model EBF4, z -60.28, effect -1.954, with EBF1 agreeing in direction. EBF4 is chosen within the EBF group because it has the best own-model score and the highest expression among group members listed (1.22 TPM versus EBF1 0.18, EBF2 0.73, EBF3 0.06). | weak | [E08](#e08), [E07](#e07) |
| element | The variant is in a PYDC2-AS1 intron with no cCRE overlap and 42 bp from dELS EH38E2269392, allowing only a nearby/flanking EBF4 site model rather than an annotated cCRE-core site. | supported | [E01](#e01), [E03](#e03) |
| gene | The nearest plausible targets are PYDC2-AS1 and PYDC2, 19.5 kb upstream, but no colon transverse eQTL for this variant was detected, so the gene link remains proximity-only. | supported | [E01](#e01), [E02](#e02), [E20](#e20) |
| cell_type | HCT116 expresses EBF4 at 1.22 TPM, so an EBF4-dependent effect is possible in the supplied cell type, but no EBF4 chromatin occupancy data are provided and expression is low. | weak | [E07](#e07), [E08](#e08) |
| phenotype | There is no GWAS Catalog or Open Targets association for rs13078086, and the literature hits do not establish an EBF4- or PYDC2-AS1/PYDC2-specific colorectal cancer mechanism; any disease effect is speculative and indirect. | supported | [E04](#e04), [E05](#e05), [E06](#e06) |

Predictions: Recombinant EBF4 binds the ref T oligo more strongly than the alt G oligo at rs13078086.; EBF4 ChIP-qPCR or CUT&RUN enriches at the variant or nearby dELS in a colorectal cancer line, if EBF4 is expressed/active there.; Allele-specific perturbation of the element changes PYDC2-AS1 or PYDC2 expression, with direction not specified by binding alone.

Falsified if: Recombinant EBF4 shows no allele-specific binding to rs13078086 ref versus alt.; EBF4 ChIP-qPCR or CUT&RUN does not enrich at the variant or nearby dELS in HCT116 or another colorectal cancer line.; Allele-specific perturbation of the element does not change local PYDC2-AS1/PYDC2 expression.

### 3. TFAP2E_ref_less_alt: TFAP2E binds ref more at a PYDC2-AS1 intronic site; local output unproven (p = 0.07)

TF TFAP2E (stated coverage own_model; registry own_model), ref allele binds more; element rs13078086 is in a PYDC2-AS1 intron and does not overlap an annotated cCRE; it is 42 bp from dELS EH38E2269392, so an AP-2 site would be at the element edge or in flanking sequence.; gene PYDC2-AS1/PYDC2; cell type HCT116 expresses TFAP2E at 8.5 TPM, but no ENCODE TFAP2E ChIP-seq peak containing the variant is reported in HCT116; absence may reflect no experiment, so occupancy remains untested..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2E binds the ref T allele more strongly than alt G; the best AP-2 group model is TFAP2E, z -18.37, effect -0.765, and TFAP2A/B/C models agree in direction. | weak | [E10](#e10), [E07](#e07) |
| element | The variant is a PYDC2-AS1 intronic variant with no annotated cCRE overlap and 42 bp from dELS EH38E2269392; an AP-2 site would have to sit at the element edge or in flanking sequence. | supported | [E01](#e01), [E03](#e03) |
| gene | PYDC2-AS1 contains the variant and PYDC2 is 19.5 kb upstream, but no colon transverse eQTL for the variant was detected, so a TFAP2E-to-gene effect is not established. | supported | [E01](#e01), [E02](#e02), [E20](#e20) |
| cell_type | HCT116 expresses TFAP2E at 8.5 TPM, making TFAP2E present in the supplied context; however, no HCT116 TFAP2E ChIP-seq peak is reported at the variant, so occupancy is unproven. | weak | [E07](#e07), [E10](#e10), [E18](#e18) |
| phenotype | No GWAS Catalog or Open Targets association exists for rs13078086, and the literature does not establish a PYDC2-AS1/PYDC2 colorectal cancer mechanism; the disease link is indirect and speculative. | supported | [E04](#e04), [E05](#e05), [E06](#e06) |

Predictions: Recombinant TFAP2E/AP-2 binds the ref T oligo more strongly than the alt G oligo at rs13078086.; Allele-specific TFAP2E/AP-2 ChIP or reporter activity is detectable in a colorectal cancer line.; If the element is functional, allele-specific perturbation changes PYDC2-AS1 or PYDC2 expression, with direction not specified by binding alone.

Falsified if: Allele-specific TFAP2E/AP-2 binding at rs13078086 is not detected.; TFAP2E ChIP-qPCR or CUT&RUN does not enrich at the variant or nearby dELS in a colorectal cancer line.; Allele-specific perturbation does not change PYDC2-AS1/PYDC2 expression.

### 4. RFX5_ref_less_alt: RFX5 binds ref more near a PYDC2-AS1 intronic dELS edge; chromatin and gene effects unproven (p = 0.06)

TF RFX5 (stated coverage own_model; registry own_model), ref allele binds more; element The variant is 42 bp from dELS EH38E2269392 and does not overlap a cCRE; an RFX5 site would reside in flanking non-cCRE sequence near that element.; gene PYDC2-AS1/PYDC2; cell type HCT116 expresses RFX5 at 20.42 TPM, but no ENCODE RFX5 ChIP-seq peak containing the variant is reported in HCT116; absence may reflect no experiment, so occupancy remains untested..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | RFX5 binds the ref T allele more strongly than alt G; RFX5 has its own QBiC-SELEX model, z -11.73, effect -1.452 (alt binds less). | weak | [E15](#e15), [E07](#e07) |
| element | The variant is in a PYDC2-AS1 intron with no cCRE overlap and 42 bp from dELS EH38E2269392, so it could only affect a flanking RFX site near that element, not the annotated cCRE core. | supported | [E01](#e01), [E03](#e03) |
| gene | The nearest plausible targets are PYDC2-AS1/PYDC2, but no colon transverse eQTL for the variant was detected, so no expression link to RFX5 is established. | supported | [E01](#e01), [E02](#e02), [E20](#e20) |
| cell_type | RFX5 is expressed in HCT116 at 20.42 TPM, supporting that RFX5 could act in this cell type if its motif is accessible; however, no HCT116 RFX5 ChIP-seq peak is reported at the variant, so occupancy is unproven. | weak | [E07](#e07), [E15](#e15), [E19](#e19) |
| phenotype | No direct GWAS or Open Targets association exists for rs13078086, and no evidence establishes an RFX5-dependent colorectal cancer mechanism through this locus. | supported | [E04](#e04), [E05](#e05), [E06](#e06) |

Predictions: Recombinant RFX5 binds the ref T oligo more strongly than the alt G oligo at rs13078086.; RFX5 ChIP-qPCR or CUT&RUN enriches at the variant or nearby dELS in colorectal cancer cells.; Allele-specific perturbation changes PYDC2-AS1 or PYDC2 expression, with direction not specified by binding alone.

Falsified if: RFX5 does not bind the rs13078086 sequence allele-specifically.; RFX5 ChIP-qPCR or CUT&RUN does not enrich at the variant or nearby dELS in colorectal cancer cells.; Allele-specific perturbation does not change PYDC2-AS1/PYDC2 expression.

## Prediction matrix

| Test | Cost | Separates top two | null_no_tf_mediated_effect | EBF4_ref_less_alt | TFAP2E_ref_less_alt | RFX5_ref_less_alt |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA with recombinant EBF4 DNA-binding domain on ref versus alt rs13078086 oligos | low | yes | No reproducible allele-specific EBF4 binding. | Ref T oligo shows stronger EBF4 binding than alt G. | No EBF4-specific allele difference expected; this test does not address TFAP2E. | No EBF4-specific allele difference expected; this test does not address RFX5. |
| Allele-specific EMSA with recombinant TFAP2E/AP-2 on ref versus alt rs13078086 oligos | low | no | No reproducible allele-specific TFAP2E/AP-2 binding. | No TFAP2E/AP-2-specific allele difference expected. | Ref T oligo shows stronger TFAP2E/AP-2 binding than alt G. | No TFAP2E/AP-2-specific allele difference expected. |
| Allele-specific EMSA with recombinant RFX5 on ref versus alt rs13078086 oligos | low | no | No reproducible allele-specific RFX5 binding. | No RFX5-specific allele difference expected. | No RFX5-specific allele difference expected. | Ref T oligo shows stronger RFX5 binding than alt G. |
| EBF4 ChIP-qPCR or CUT&RUN in HCT116 at rs13078086 and nearby dELS EH38E2269392 | medium | yes | No enrichment above background at the variant or nearby dELS. | EBF4 ChIP-qPCR or CUT&RUN enriches at the variant or nearby dELS in HCT116. | No EBF4-specific enrichment expected. | No EBF4-specific enrichment expected. |
| Allele-specific MPRA or reporter assay for the rs13078086 ref versus alt sequence in HCT116 | medium | yes | No reproducible allele-specific reporter activity. | Allele-specific reporter activity is detected, direction not specified by binding alone. | Allele-specific reporter activity is detected, direction not specified by binding alone. | Allele-specific reporter activity is detected, direction not specified by binding alone. |
| Larger colon eQTL or allele-specific expression analysis for rs13078086 and PYDC2-AS1/PYDC2 | medium | no | No local eQTL, consistent with the current negative colon transverse result. | A local PYDC2-AS1/PYDC2 eQTL may be present in a larger or different colon dataset; current colon transverse data show none. | A local PYDC2-AS1/PYDC2 eQTL may be present in a larger or different colon dataset; current colon transverse data show none. | A local PYDC2-AS1/PYDC2 eQTL may be present in a larger or different colon dataset; current colon transverse data show none. |

## Next experiment

Allele-specific EMSA with recombinant EBF4 DNA-binding domain on ref T versus alt G oligos is the cheapest experiment that separates the top two chains (null versus EBF4). A positive ref-biased result supports EBF4 binding but not by itself disease causality; a negative result supports the null at the binding step.

## Investigate calls

- chip_peaks({"tf": "TFAP2E", "biosample": "HCT116"})
- chip_peaks({"tf": "RFX5", "biosample": "HCT116"})
- eqtl_lookup({"tissue": "Colon - Transverse"})

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

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:42:52+00:00)

> No ENCODE RFX5 ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT116'. Absence can also mean no RFX5 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (G) relative to ref (T).
