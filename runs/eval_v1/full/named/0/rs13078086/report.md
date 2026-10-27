# rs13078086 and Colorectal cancer

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.66 over 8 model calls; 192 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen

209 of 997 models pass the gate. Top groups: EBF1, 2 models (best EBF4, z -60.28); C2H2 ZF, 1 model (best ZNF696, z 23.6); AP-2, 4 models (best TFAP2E, z -18.37); C2H2 ZF, 1 model (best ZNF343, z 15.69); Ets, 18 models (best ETV5, z 13.11).

## Ranked chains

### 1. H1: Null: no TF-mediated effect of rs13078086 (passenger / linked variant) (p = 0.70)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific reporter activity for the 200 bp window around chr3:191441666 in HCT 116 or other colorectal lines.; No allele-specific accessibility or TF ChIP/CUT&RUN signal at the exact position in HCT 116 or colon tissue; consistent with E19 (no TFAP2A peak) and E03 (no cCRE overlap).; No colon eQTL for PYDC2, PYDC2-AS1 or CCDC50 (consistent with E18), and no GWAS/Open Targets record (E04, E05).; Single-base editing of rs13078086 in HCT 116 changes no neighbouring gene by more than assay noise; any true signal in the locus maps to a different, linked base.

Falsified if: A reproducible allele-specific reporter, ATAC or ChIP difference is shown at this exact position in a colorectal context.; A colon eQTL or a credible-set GWAS association for rs13078086 emerges.; Prime-edited T>G clones show a reproducible expression change in a nearby gene.

### 2. H4: Ref allele binds AP-2 (TFAP2E) more; alt reduces AP-2 input to the nearby element (p = 0.11)

TF TFAP2E (stated coverage own_model; registry own_model), ref allele binds more; element Sequence 42 bp from distal enhancer-like cCRE EH38E2269392; gene PYDC2; cell type Colorectal carcinoma epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | All four AP-2 models in group G030 agree that the T (ref) allele binds more (best model TFAP2E own model, z -18.37, effect -0.765; TFAP2A z -16.2). Within the group TFAP2E is named because it has both the best-scoring model and the highest expression in this context (8.5 TPM vs TFAP2A 6.18, TFAP2C 2.59, TFAP2B 0); the earlier TFAP2A choice rested on prior knowledge, not evidence. Caveat: both alleles sit near the 99.6-99.7th k-mer percentile, so the predicted occupancy change is small despite the large z. | weak | [E10](#e10) |
| element | The variant lies outside any cCRE, 42 bp from dELS EH38E2269392, whose signal is a maximum across biosamples; no colon- or HCT 116-specific chromatin evidence is available. | missing | [E03](#e03), [E01](#e01) |
| gene | PYDC2 is taken as the candidate on proximity (19.5 kb) and on being listed for the cCRE; CCDC50 is deprioritised because it is further (112.6 kb) and shows no dependency in bowel lines, and no eQTL supports either. | weak | [E02](#e02), [E03](#e03), [E18](#e18), [E20](#e20) |
| cell_type | TFAP2E and TFAP2A are expressed in the HCT 116 context, so AP-2 input is possible; however, no ENCODE TFAP2A peak contains the variant, which weakens the case (though no TFAP2A experiment may exist in colorectal biosamples). | weak | [E10](#e10), [E19](#e19) |
| phenotype | No phenotype evidence: the site is not conserved (GERP -1.82), and there is no GWAS or Open Targets association, so any disease contribution would be negligible. | missing | [E01](#e01), [E04](#e04), [E05](#e05) |

Predictions: TFAP2E/TFAP2A CUT&RUN in HCT 116 shows a peak overlapping the variant with T-allele preference.; AP-2 (TFAP2E + TFAP2A) depletion abolishes the allelic reporter difference.; Direction is opposite to H2: T allele gives higher activity than G.

Falsified if: No AP-2 occupancy at this locus in colorectal or epithelial ChIP/CUT&RUN data (E19 already shows no TFAP2A peak).; Allelic reporter difference persists after AP-2 depletion.

### 3. H2: Alt allele creates a ZNF696 site in a weak distal element near PYDC2/PYDC2-AS1 (p = 0.10)

TF ZNF696 (stated coverage own_model; registry own_model), alt allele binds more; element Intron of PYDC2-AS1, 42 bp from dELS EH38E2269392; gene PYDC2; cell type Colorectal carcinoma epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts the G (alt) allele binds ZNF696 much more strongly (own model, z 23.6, effect +0.733), with the site moving from the 56.3rd to the 99.2nd k-mer percentile; group G570 contains only ZNF696, so no within-group TF choice is needed. This is in vitro prediction only, with no ChIP or allelic assay. | weak | [E09](#e09), [E07](#e07) |
| element | The variant overlaps no cCRE; the only regulatory annotation nearby is dELS EH38E2269392 42 bp away, whose DNase/H3K27ac z-scores are maxima over all biosamples, not colon-specific. Element involvement is therefore assumed, not shown. | missing | [E03](#e03), [E01](#e01) |
| gene | Target is assigned by proximity only: PYDC2 is the nearest protein-coding gene (19.5 kb) and is among the genes listed for EH38E2269392; no enhancer-gene link, eQTL (E18 shows none) or perturbation evidence supports it. | weak | [E02](#e02), [E03](#e03), [E18](#e18) |
| cell_type | ZNF696 is expressed at 8.26 TPM in the DepMap HCT 116 context used for the screen, so the created site could be bound there; no chromatin evidence for activity at this locus in colon. | weak | [E09](#e09), [E07](#e07) |
| phenotype | No phenotype support: there is no GWAS or Open Targets record for the variant and no literature tying PYDC2 to colorectal cancer; any effect would have to be very small. | missing | [E04](#e04), [E05](#e05), [E06](#e06) |

Predictions: ZNF696 CUT&RUN in HCT 116 shows G-allele-preferential signal at chr3:191441666.; Allelic reporter difference (G > T or G < T) is abolished by ZNF696 knockout.; Prime-edited G/G clones shift PYDC2 or PYDC2-AS1 expression, not CCDC50.

Falsified if: No ZNF696 occupancy at this locus in colorectal cells.; ZNF696 knockout leaves any allelic reporter difference intact.; Allele-edited clones show no change in PYDC2/PYDC2-AS1.

### 4. H3: Ref allele binds RFX5 more; alt weakens an RFX5-dependent site near PYDC2-AS1 (p = 0.09)

TF RFX5 (stated coverage own_model; registry own_model), ref allele binds more; element PYDC2-AS1 intronic sequence adjacent to dELS EH38E2269392; gene PYDC2-AS1; cell type Colorectal carcinoma epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts the T (ref) allele binds RFX5 more strongly (own model, z -11.73, effect -1.452); within group G094 RFX5 rather than RFX7 is named because only the RFX5 model passes and RFX5 is well expressed (20.42 TPM). The percentile shift is small (99.3rd to 98.5th), and the separate RFX2 group (E13) is not evidence for RFX5. | weak | [E15](#e15) |
| element | No cCRE overlaps the variant; the nearest dELS is 42 bp away, so the existence of an RFX-dependent element here is an assumption with no supporting chromatin evidence. | missing | [E03](#e03), [E01](#e01) |
| gene | The variant lies in a PYDC2-AS1 intron, making that non-coding transcript the most proximal candidate; no eQTL or enhancer-gene link supports any target. | weak | [E01](#e01), [E02](#e02), [E18](#e18) |
| cell_type | RFX5 is expressed at 20.42 TPM in the HCT 116 context, so the TF is present; locus activity in colon is unknown. | weak | [E15](#e15) |
| phenotype | No evidence connects this locus or PYDC2-AS1 to colorectal cancer; the E06 hits are about other pyroptosis genes and there is no GWAS or Open Targets record. | missing | [E04](#e04), [E05](#e05), [E06](#e06) |

Predictions: RFX5 ChIP/CUT&RUN shows T-allele-preferential signal at the variant.; RFX5 knockdown reduces reporter activity for the T but not the G construct.; Direction: T allele gives higher element activity than G.

Falsified if: No RFX5 occupancy at the locus in colorectal cells.; Allelic reporter difference persists after RFX5 depletion, or runs in the opposite direction.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| GTEx v8 colon (Transverse/Sigmoid) eQTL lookup for chr3_191441666_T_G | existing data | no | No significant eQTL (as observed in E18) | Expects a PYDC2 eQTL with lower expression on G; absence is mildly disconfirming | Expects a PYDC2/PYDC2-AS1 eQTL; absence is mildly disconfirming | Expects a PYDC2-AS1 eQTL; absence is mildly disconfirming |
| Allele-specific luciferase/MPRA of the 200 bp window (T vs G) in HCT 116 | low | yes | No allelic difference | T > G activity | G allele differs from T (gain-of-site effect) | T > G activity |
| TFAP2E/TFAP2A CUT&RUN in HCT 116 at chr3:191441666 | medium | yes | No peak (consistent with E19) | AP-2 peak overlapping the variant, T-allele preferential | No AP-2 peak required | No AP-2 peak required |
| ZNF696 CUT&RUN in HCT 116 at the variant | medium | no | No allele-preferential signal | No ZNF696 signal expected | G-allele-preferential ZNF696 signal | No ZNF696 signal expected |
| RFX5 CUT&RUN plus RFX5 knockdown reporter test | medium | no | No occupancy, no knockdown effect | No RFX5 dependence | No RFX5 dependence | T-preferential RFX5 signal; allelic difference lost on knockdown |
| Prime-edited T/T vs G/G HCT 116 clones, RNA-seq of PYDC2, PYDC2-AS1, CCDC50 | high | yes | No expression change | Lower PYDC2 in G/G clones | PYDC2/PYDC2-AS1 change in G/G clones | Lower PYDC2-AS1 in G/G clones |
| DepMap CRISPR dependency for CCDC50 in bowel lines | existing data | no | No dependency (observed: 0.49 in HCT 116, 0% dependent lines, E20) | Neutral; CCDC50 deprioritised as target | Neutral; CCDC50 deprioritised as target | Neutral |

## Next experiment

A low-cost allele-specific luciferase/MPRA in HCT 116 comparing the T and G 200 bp constructs: if there is no reproducible allelic difference, the null (H1) stands over H4 and all TF chains; a T > G difference would support H4 (and H3), while a G-driven gain would point to H2.

## Investigate calls

- eqtl_lookup({"tissue": null})
- chip_peaks({"tf": "TFAP2A", "biosample": null})
- gene_dependency({"gene": "CCDC50"})

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

> QBiC-SELEX screen of chr3:191441666:T>G: 997 models scored, 209 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 174 CIS-BP groups. Expression context: DepMap line ACH-000971. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 37 (C2H2 ZF, 1 model z 38.3, Ets, 3 models z -10.94, bHLH, 2 models z -10.76, C2H2 ZF, 1 model z 7.66, bHLH, 1 model z -7.64). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G066 (EBF1, 2 models): best model EBF4_FL_TCGATT40NTTG_KK_nitta2015_1_3_7mer (own model of EBF4), z -60.28, effect -1.954 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: EBF4 z -60.28, EBF1 z -28.35. TFs this group covers (own and CIS-BP-mapped models): EBF4 1.22 TPM, EBF2 0.73 TPM, EBF1 0.18 TPM, EBF3 0.06 TPM; best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G570 (C2H2 ZF, 1 model): best model ZNF696_FL_AG40NTGGCTA_YWSA_jolma2025_0_2_7mer (own model of ZNF696), z 23.6, effect 0.733 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF696 z 23.6. TFs this group covers (own and CIS-BP-mapped models): ZNF696 8.26 TPM; best model's site strength: ref 56.3th, alt 99.2th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (own model of TFAP2E), z -18.37, effect -0.765 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TFAP2E z -18.37, TFAP2A z -16.2, TFAP2B z -13.18, TFAP2C z -5.14. TFs this group covers (own and CIS-BP-mapped models): TFAP2E 8.5 TPM, TFAP2A 6.18 TPM, TFAP2C 2.59 TPM, TFAP2B 0.0 TPM, TFAP2D 0.0 TPM; best model's site strength: ref 99.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G490 (C2H2 ZF, 1 model): best model ZNF343_eDBD_TGGCGT40NCCT_KT_yin2017_0_3_7mer (own model of ZNF343), z 15.69, effect 0.778 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF343 z 15.69. TFs this group covers (own and CIS-BP-mapped models): ZNF343 9.63 TPM; best model's site strength: ref 98.3th, alt 98.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 13.11, effect 0.251 (alt binds more); 4 passing models (2 with the best model's sign); members disagree on direction. Passing members: ETV5 z 13.11, ELF1 z -7.84, FLI1 z 5.19, ELF2 z -4.96. TFs this group covers (own and CIS-BP-mapped models): EHF 88.58 TPM, ELK3 51.39 TPM, ERF 46.58 TPM, ETV4 36.17 TPM, ELF3 33.75 TPM, ELK1 26.37 TPM, ETS2 25.48 TPM, ETV5 25.15 TPM, ELF1 24.76 TPM, ELF2 19.32 TPM (+15 more); best model's site strength: ref 94.6th, alt 95.3th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G028 (RFX, 4 models): best model RFX2_NA_TAACCC20NCCA_ESY_yang2017_0_3_7mer (own model of RFX2), z -12.18, effect -1.006 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: RFX2 z -12.18, RFX1 z -6.72, RFX4 z -4.83. TFs this group covers (own and CIS-BP-mapped models): RFX2 6.73 TPM, RFX1 3.61 TPM, RFX3 2.61 TPM, RFX4 0.01 TPM, RFX6 0.0 TPM; best model's site strength: ref 98.8th, alt 96.5th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G449 (C2H2 ZF, 1 model): best model ZNF174_eDBD_TACCGA40NATA_KS_yin2017_1_3_7mer (own model of ZNF174), z 11.98, effect 0.325 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF174 z 11.98. TFs this group covers (own and CIS-BP-mapped models): ZNF174 7.86 TPM; best model's site strength: ref 92.7th, alt 94.5th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G094 (RFX, 2 models): best model RFX5_eDBD_TTGATG40NATC_KO_yin2017_0_4_7mer (own model of RFX5), z -11.73, effect -1.452 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: RFX5 z -11.73. TFs this group covers (own and CIS-BP-mapped models): RFX5 20.42 TPM, RFX7 10.12 TPM; best model's site strength: ref 99.3th, alt 98.5th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G560 (C2H2 ZF, 1 model): best model ZNF668_FL_TC40NGTTTTG_YWSA_jolma2025_0_3_7mer (own model of ZNF668), z 10.82, effect 0.699 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF668 z 10.82. TFs this group covers (own and CIS-BP-mapped models): ZNF668 8.44 TPM; best model's site strength: ref 84.5th, alt 95.3th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G373 (Unknown, 1 model): best model TMF1_DBD_CA40NTCGATG_YWPA_jolma2025_0_2_7mer (own model of TMF1), z 10.65, effect 0.85 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: TMF1 z 10.65. TFs this group covers (own and CIS-BP-mapped models): TMF1 14.51 TPM; best model's site strength: ref 66.7th, alt 98.2th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38. NES is the effect of the alt allele (G) relative to ref (T).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:34:00+00:00)

> No ENCODE TFAP2A ChIP-seq peak contains chr3:191441666:T>G (0 peaks within 100 bp). Absence can also mean no TFAP2A experiment in that biosample.

<a id="e20"></a>**E20** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for CCDC50 (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): 0.49. Bowel lineage, 63 lines: median 0.18, 0% dependent. All 1183 lines: median 0.19, 0% dependent.
