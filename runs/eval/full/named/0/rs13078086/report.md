# rs13078086 and Colorectal cancer

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.61 over 7 model calls; 162 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen

209 of 997 models pass the gate. Top groups: EBF1, 2 models (best EBF4, z -60.28); C2H2 ZF, 1 model (best ZNF696, z 23.6); AP-2, 4 models (best TFAP2E, z -18.37); C2H2 ZF, 1 model (best ZNF343, z 15.69); Ets, 18 models (best ETV5, z 13.11).

## Ranked chains

### 1. H0: No TF-mediated effect: passenger or linked variant in a non-regulatory intron (p = 0.60)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific reporter or MPRA activity difference between T and G in colorectal lines; No differential band in EMSA with HCT 116 nuclear extract; No allele-specific accessibility or TF occupancy at chr3:191441666 in HCT 116; No colon eQTL for PYDC2, PYDC2-AS1, CCDC50 or other neighbours

Falsified if: A reproducible allele-specific reporter/MPRA or base-editing effect is seen in colorectal cells; Allele-specific ChIP, CUT&RUN or footprinting shows differential occupancy at the site

### 2. H5: Alt allele creates a TMF1 site near the distal enhancer (p = 0.13)

TF TMF1 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E2269392 (dELS); gene PYDC2-AS1 / PYDC2 (unresolved); cell type colorectal epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TMF1 own model (sole member of group G373) predicts a strong alt gain: z 10.65, effect +0.85, ref 66.7th to alt 98.2th percentile, the second-largest percentile jump among the groups shown; in vitro prediction only, with no ChIP evidence cited. TMF1 is included because the critic noted expressed single-TF groups (ZNF343, ZNF174, ZNF668, TMF1) were omitted; TMF1 has the largest site-strength change of these. | weak | [E17](#e17), [E07](#e07) |
| element | Same edge-of-element limitation as the other chains: no cCRE overlap, nearest dELS 42 bp away with weak H3K27ac. | weak | [E03](#e03), [E01](#e01) |
| gene | The variant is annotated only within PYDC2-AS1; PYDC2 is the nearest coding gene and is among the SCREEN-listed neighbours. No eQTL supports any target. | missing | [E01](#e01), [E02](#e02), [E03](#e03), [E18](#e18) |
| cell_type | TMF1 is expressed in HCT 116 at 14.51 TPM. | weak | [E17](#e17) |
| phenotype | No variant-level genetic association exists (GWAS Catalog and Open Targets empty), so the path to colorectal cancer is unsupported. | missing | [E04](#e04), [E05](#e05) |

Predictions: EMSA G-specific complex is supershifted or lost with TMF1 antibody/knockdown, not with ZNF696 or AP-2 reagents; TMF1 CUT&RUN shows alt-biased signal at the site; Allelic reporter difference persists after ZNF696 knockdown but disappears after TMF1 knockdown

Falsified if: TMF1 depletion leaves any allelic reporter/EMSA difference intact; No TMF1 occupancy at the locus

### 3. H1: Alt allele creates a ZNF696 site at the edge of a weak distal enhancer (p = 0.12)

TF ZNF696 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E2269392 (dELS, 42 bp from variant); gene CCDC50 or PYDC2 (enhancer target not resolved); cell type colorectal epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX ZNF696 own model predicts a large gain for the G allele (z 23.6, effect +0.733, ref 56.3th to alt 99.2th percentile); ZNF696 is the sole TF in group G570, so no within-group choice is needed. This is an in vitro prediction only, and Factorbook shows no ENCODE ZNF696 peak containing the site, though that may reflect no ZNF696 experiment in this biosample. | weak | [E09](#e09), [E07](#e07), [E20](#e20) |
| element | The variant overlaps no cCRE; the nearest annotation is EH38E2269392, a dELS 42 bp away with modest DNase (z 3.5) and weak H3K27ac (z 1.8) as maxima across biosamples, with no HCT 116-specific signal shown. | weak | [E03](#e03), [E01](#e01) |
| gene | SCREEN lists AC073365.1, PYDC2 and CCDC50 near this dELS; no eQTL, Hi-C or CRISPRi link is available, and GTEx shows no significant eQTL, so the target gene is unresolved. | missing | [E03](#e03), [E02](#e02), [E18](#e18) |
| cell_type | ZNF696 is expressed in HCT 116 at 8.26 TPM, so the predicted site could be bound in this line; expression only, no occupancy evidence. | weak | [E09](#e09), [E07](#e07) |
| phenotype | If enhancer output changed, altered dosage of a neighbouring gene could in principle affect colonic epithelium, but no GWAS or Open Targets record links this variant to colorectal cancer. | missing | [E04](#e04), [E05](#e05) |

Predictions: EMSA with HCT 116 nuclear extract shows a G-specific complex that supershifts or is lost on ZNF696 depletion; ZNF696 CUT&RUN in HCT 116 gives signal at the site with alt-biased occupancy in heterozygous cells; Allelic reporter difference (G > T if activating) is abolished by ZNF696 knockdown

Falsified if: ZNF696 CUT&RUN/ChIP in HCT 116 shows no occupancy at this locus; Reporter or EMSA shows no T vs G difference, or any difference is unaffected by ZNF696 depletion

### 4. H2: Ref allele maintains an RFX5 site; alt weakens RFX-dependent regulation (p = 0.08)

TF RFX5 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E2269392 (dELS); gene PYDC2 / PYDC2-AS1; cell type colorectal epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | RFX5 own model: z -11.73, effect -1.452, ref 99.3th vs alt 98.5th percentile, so T binds more strongly; RFX5 is chosen over RFX7 in G094 because it supplies the passing model and is higher expressed (20.42 TPM). The second RFX group G028 agrees in direction but shares the RFX motif, so it is not independent, and the percentile change is small. | weak | [E15](#e15), [E13](#e13) |
| element | The variant lies in no cCRE and in a poorly conserved position (GERP -1.82); the nearest annotation is the dELS 42 bp away, so the element assignment is weak. | missing | [E03](#e03), [E01](#e01) |
| gene | PYDC2 is the nearest protein-coding gene (19.5 kb) and the variant is intronic in PYDC2-AS1; proximity only, with no eQTL support. | weak | [E02](#e02), [E01](#e01), [E18](#e18) |
| cell_type | RFX5 is expressed in HCT 116 at 20.42 TPM; expression only, no occupancy data. | weak | [E15](#e15) |
| phenotype | PYDC2 is an inflammasome-related gene appearing in pyroptosis literature searches, but none of the retrieved papers ties PYDC2 or this variant to colorectal cancer risk. | missing | [E06](#e06), [E04](#e04), [E05](#e05) |

Predictions: EMSA shows a T-specific complex competed by an RFX consensus oligo; RFX5 (or RFXAP/RFXANK) depletion reduces ref-allele reporter activity specifically; RFX5 CUT&RUN shows ref-biased occupancy in heterozygous colorectal cells

Falsified if: No RFX5 occupancy at the locus in colorectal cells; Reporter shows alt >= ref activity or no RFX-dependence

### 5. H3: Ref allele binds AP-2 (TFAP2E/TFAP2A); alt slightly weakens an AP-2 site (p = 0.07)

TF TFAP2E (stated coverage own_model; registry own_model), ref allele binds more; element EH38E2269392 (dELS); gene CCDC50 or PYDC2 (unresolved); cell type colorectal epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AP-2 group G030 has four concordant passing models predicting less alt binding; within the group I now name TFAP2E rather than TFAP2A because TFAP2E supplies the best model (z -18.37, effect -0.765) and has the highest expression (8.5 TPM) of the AP-2 members in HCT 116. The models share one AP-2 motif and the site-strength change is negligible (99.7th to 99.6th percentile), so the predicted functional effect is small. | weak | [E10](#e10) |
| element | The variant is in no cCRE; the only regulatory annotation within 500 bp is the dELS 42 bp away, with no HCT 116-specific signal shown. | weak | [E03](#e03) |
| gene | SCREEN names AC073365.1, PYDC2 and CCDC50 for this dELS; no link data distinguish them and GTEx shows no eQTL. | missing | [E03](#e03), [E02](#e02), [E18](#e18) |
| cell_type | TFAP2E (8.5 TPM) and TFAP2A (6.18 TPM) are expressed in HCT 116; expression only. | weak | [E10](#e10) |
| phenotype | No GWAS or Open Targets evidence links this variant to colorectal cancer; the phenotype link is speculative. | missing | [E04](#e04), [E05](#e05) |

Predictions: AP-2 ChIP/CUT&RUN (TFAP2E or TFAP2A) shows a peak over the dELS with ref-biased signal; Reporter activity is ref > alt and AP-2 depletion flattens the difference; Effect direction opposite to the alt-gain chains H1 and H5

Falsified if: No AP-2 occupancy at the locus in colorectal cells; Reporter shows alt >= ref, contradicting a ref-specific AP-2 site

## Prediction matrix

| Test | Cost | Separates top two | H0 | H5 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EMSA with HCT 116 nuclear extract, T vs G probes (with antibody supershifts for ZNF696, RFX5, AP-2, TMF1) | low | yes | No differential complex between T and G probes | G-specific complex, TMF1 supershift | G-specific complex, supershifted/lost with ZNF696 reagent | T-specific complex, RFX-competed | Modest T-biased complex, AP-2 supershift |
| Allele-specific luciferase/MPRA of the 200 bp element in HCT 116 | medium | yes | No T vs G activity difference | Allelic difference (G-driven), lost on TMF1 knockdown | Allelic difference (G-driven), lost on ZNF696 knockdown | T > G activity, RFX5-dependent | Small T > G activity, AP-2-dependent |
| ZNF696 CUT&RUN or ChIP in HCT 116 at chr3:191441666 | medium | yes | No peak (consistent with E20) | No ZNF696 peak | Peak with alt-biased reads | No ZNF696 peak | No ZNF696 peak |
| Colon eQTL lookup for rs13078086 (GTEx Colon_Transverse/Sigmoid, larger colon cohorts) | existing data | no | No eQTL (already seen in E18) | eQTL for PYDC2-AS1/PYDC2 | eQTL for CCDC50 or PYDC2 | eQTL for PYDC2/PYDC2-AS1, ref-higher direction | eQTL for CCDC50/PYDC2, ref-higher direction |
| Base editing / HDR of the single base in HCT 116 followed by RNA-seq of PYDC2, PYDC2-AS1, CCDC50 | high | yes | No expression change in any neighbour | Change in PYDC2-AS1/PYDC2, TMF1-dependent | Change in CCDC50 or PYDC2, ZNF696-dependent | PYDC2 lower with G allele | Small decrease in CCDC50/PYDC2 with G allele |

## Next experiment

EMSA with HCT 116 nuclear extract comparing T and G 25-mer probes, with antibody supershift/competition panels for ZNF696, TMF1, RFX5 and AP-2: it is the cheapest assay that distinguishes the null (no differential complex) from H1/H5 (an allele-specific complex) and names the responsible factor.

## Investigate calls

- eqtl_lookup({"tissue": null})
- qbic_tf_detail({"tf": "ELF3"})
- chip_peaks({"tf": "ZNF696", "biosample": null})

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

<a id="e18"></a>**E18** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38. NES is the effect of the alt allele (G) relative to ref (T).

<a id="e19"></a>**E19** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ELF3","symbol":"ELF3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr3:191441666:T>G","gate_p":5.02e-05,"models":[{"model":"ELF3_NA_TCCGTG20NTGC_ESY_yang2017_0_4_7mer","mapping":"own","group":"G020 Ets, 4 models","quality":0.822,"effect":0.184,"z":2.8,"p":0.0052,"rank_abs_z":"378/997","passed_gate":false,"site_strength":{"ref_percentile":52.2,"alt_percentile":90.1,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":-0.231,"z":-7.84,"p":4.3e-15,"rank_abs_z":"28/997","passed_gate":true,"site_strength":{"ref_percentile":72.6,"alt_percentile":86.8,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":-0.705,"z":-4.96,"p":7e-07,"rank_abs_z":"139/997","passed_gate":true,"site_strength":{"ref_percentile":66.1,"alt_percentile":83.2,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":-0.291,"z":-3.78,"p":0.00016,"rank_abs_z":"250/997","passed_gate":false,"site_strength":{"ref_percentile":91.9,"alt_percentile":80.7,"k":7}},{"model":"ELF5_NA_TCTCGG20NGA_ESAF_yang2017_0_3_7mer","mapping":"CIS-BP (ELF5)","group":"G020 Ets, 4 models","quality":0.902,"effect":-0.08,"z":-0.99,"p":0.32,"rank_abs_z":"718/997","passed_gate":false,"site_strength":{"ref_percentile":93.2,"alt_percentile":93.8,"k":7}},{"model":"ETV6_NA_TGAGTG20NGA_ESAF_yang2017_0_3_7mer","mapping":"CIS-BP (ETV6)","group":"G020 Ets, 4 models","quality":0.897,"effect":-0.041,"z":-0.73,"p":0.46,"rank_abs_z":"779/997","passed_gate":false,"site_strength":{"ref_percentile":86.0,"alt_percentile":93.2,"k":7}},{"model":"ETV7_FL_TTAAGC40NAGT_KAE_yin2017_0_2_7mer","mapping":"CIS-BP (ETV7)","group":"G020 Ets, 4 models","quality":0.913,"effect":-0.073,"z":-5.42,"p":5.9e-08,"rank_abs_z":"101/997","passed_gate":true,"site_strength":{"ref_percentile":89.6,"alt_percentile":77.0,"k":7}}]}

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T22:31:49+00:00)

> No ENCODE ZNF696 ChIP-seq peak contains chr3:191441666:T>G. Absence can also mean no ZNF696 experiment in that biosample. 0 peaks lie within 100 bp without containing it.
