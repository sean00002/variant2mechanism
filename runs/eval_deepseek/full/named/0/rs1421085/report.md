# rs1421085 and Obesity (FTO)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 8 model calls; 197 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## QBiC-SELEX screen

425 of 997 models pass the gate. Top groups: Nuclear receptor, 3 models (best ESRRG, z 62.01); Homeodomain, 9 models (best PKNOX2, z 54.71); Nuclear receptor, 29 models (best NR4A3, z 32.74); Forkhead, 10 models (best FOXL1, z -32.62); bZIP, 3 models (best NFE2L3, z 28.3).

## Ranked chains

### 1. H4_null: Null: no TF-mediated allelic effect of rs1421085 (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: There is no allele-specific TF binding at this exact site, or any binding difference is not mechanistically connected to obesity.; The GWAS signal is explained by a linked causal variant or by a non-TF-mediated effect, such as a passenger variant in strong LD.; Regulatory assays at this site should not show an allele-dependent effect after controlling for linked variants.

Falsified if: Allele-specific TF ChIP, EMSA, or a regulatory assay shows a reproducible allele-dependent TF binding and enhancer activity that maps to this variant.; A molecular QTL or fine-mapping experiment shows this variant, rather than a linked variant, is the causal regulatory change.

### 2. H1_ARID5B_repressor_loss: ARID5B repressor loss at the dELS: risk T loses ARID5B binding and derepresses IRX3/IRX5 (p = 0.20)

TF ARID5B (stated coverage not_in_coverage; registry not_in_coverage), alt allele binds more; element dELS EH38E3181208; gene IRX3/IRX5; cell type subcutaneous adipose / preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | No QBiC-SELEX model covers ARID5B (E18), and no supplied ChIP, MPRA, or EMSA shows allele-specific ARID5B binding. If ARID5B represses IRX3/IRX5 and T is the GWAS effect/risk allele, the risk T must lose repression relative to alt C, predicting that alt C binds ARID5B more strongly than ref T; this is a hypothesis, not demonstrated by the supplied evidence. | missing | [E18](#e18) |
| element | The variant lies in cCRE EH38E3181208, a distal enhancer-like element, so it is in a plausible regulatory element. | supported | [E03](#e03) |
| gene | IRX3 is 520.4 kb downstream and is a long-range candidate target, but no enhancer-to-IRX3 contact is shown; IRX5 is not listed in E02, and E03 nearby genes do not include IRX3. E19 reports no significant adipose eQTL for this variant, so the gene link is not demonstrated. | weak | [E02](#e02), [E03](#e03), [E19](#e19) |
| cell_type | Subcutaneous adipose/preadipocyte is the presumed disease-relevant context, but E03 lacks biosample-specific z-scores and E19 found no adipose eQTL, so adipose enhancer activity at this element is not established. | weak | [E03](#e03), [E19](#e19) |
| phenotype | The variant is strongly associated with obesity/BMI and related metabolic traits; the GWAS effect/risk allele is T, which fits a model in which risk T loses ARID5B repression and derepresses IRX3/IRX5 only if the binding direction is as hypothesized. | supported | [E04](#e04), [E05](#e05) |

Predictions: Allele-specific ARID5B EMSA or ChIP-qPCR should show stronger ARID5B binding on alt C than ref T.; If ARID5B is a repressor at this element, risk T should permit higher IRX3/IRX5 expression than alt C in preadipocytes.; ARID5B knockdown or motif mutation should reduce or abolish the allele-dependent effect.

Falsified if: Allele-specific ARID5B EMSA or ChIP-qPCR shows no difference or shows ref T > alt C binding at this site.; Prime editing of ref T to alt C in preadipocytes does not change IRX3 or IRX5 expression.; ARID5B knockdown does not alter the allele-dependent enhancer or gene-expression effect.

### 3. H2_ESRRA_alt_binding: ESRRA binds the alt allele at the dELS and may alter FTO expression (p = 0.15)

TF ESRRA (stated coverage own_model; registry own_model), alt allele binds more; element dELS EH38E3181208; gene FTO; cell type subcutaneous adipose / preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | In QBiC-SELEX group G037, ESRRA has its own model and passes with alt-more binding (z 17.39), and the group's best model is also alt-more; this is an in vitro binding prediction only, not allele-specific ChIP or reporter evidence. | weak | [E08](#e08) |
| element | The variant lies in distal enhancer-like cCRE EH38E3181208. | supported | [E03](#e03) |
| gene | FTO is the strongest L2G gene at this locus and the variant is in the FTO gene body; however, FTO is not the nearest protein-coding gene by TSS distance, and E19 reports no significant adipose eQTL, so direct regulation of FTO is not demonstrated. | weak | [E02](#e02), [E05](#e05), [E19](#e19) |
| cell_type | ESRRA is expressed in subcutaneous adipose in the supplied QBiC context (34.08 TPM), but E20 reports no ENCODE ESRRA ChIP-seq peak containing this variant in adipose; E20 absence can also mean no ESRRA experiment in that biosample, so occupancy is not established. | weak | [E08](#e08), [E20](#e20) |
| phenotype | The variant is strongly associated with obesity/BMI and related metabolic traits. The GWAS effect/risk allele is T, whereas this chain predicts alt C binds ESRRA more; to fit risk T, ESRRA would need to repress FTO or the FTO direction would need to be opposite, and activity direction is not established. | weak | [E04](#e04), [E05](#e05) |

Predictions: Allele-specific ESRRA ChIP-qPCR should show stronger ESRRA occupancy on alt C than ref T in adipose or preadipocyte cells.; An allele-specific reporter/MPRA should show an ESRRA-dependent allele effect at this element.; If ESRRA represses FTO, alt C should lower FTO; if ESRRA activates FTO, the direction must be reconciled with T being the GWAS effect/risk allele.

Falsified if: Allele-specific ESRRA ChIP-qPCR shows no alt C > ref T binding difference in adipose or preadipocyte cells.; An allele-specific reporter/MPRA shows no ESRRA-dependent allele effect at this element.; ESRRA knockdown does not change the allele-dependent enhancer or FTO expression effect.

### 4. H3_NR4A1_alt_binding: NR4A1 binds the alt allele at the dELS and may alter FTO expression (p = 0.10)

TF NR4A1 (stated coverage own_model; registry own_model), alt allele binds more; element dELS EH38E3181208; gene FTO; cell type subcutaneous adipose / preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | In QBiC-SELEX group G002, NR4A1 has its own model and is listed as a passing member with z 16.25; the group's best model is alt-more, but the group contains directionally mixed members and NR4A1's individual sign is not explicitly separated. This is an in vitro binding prediction only. | weak | [E10](#e10) |
| element | The variant lies in distal enhancer-like cCRE EH38E3181208. | supported | [E03](#e03) |
| gene | FTO is the strongest L2G gene at this locus and the variant is in the FTO gene body; E19 reports no significant adipose eQTL, so direct regulation of FTO is not demonstrated. | weak | [E02](#e02), [E05](#e05), [E19](#e19) |
| cell_type | NR4A1 is highly expressed in subcutaneous adipose in the supplied QBiC context (139.74 TPM), making it a plausible adipocyte TF; no allele-specific NR4A1 ChIP data are supplied. | weak | [E10](#e10) |
| phenotype | The variant is strongly associated with obesity/BMI and related metabolic traits. The GWAS effect/risk allele is T, whereas this chain predicts alt C binds NR4A1 more; activity direction is unresolved and would need NR4A1 to repress FTO, or an opposite FTO effect, to fit risk T. | weak | [E04](#e04), [E05](#e05) |

Predictions: Allele-specific NR4A1 ChIP-qPCR should show stronger NR4A1 occupancy on alt C than ref T in adipose or preadipocyte cells.; An allele-specific reporter/MPRA should show an NR4A1-dependent allele effect at this element.; NR4A1 knockdown should reduce the allele-dependent enhancer or FTO expression effect.

Falsified if: Allele-specific NR4A1 ChIP-qPCR shows no alt C > ref T binding difference in adipose or preadipocyte cells.; An allele-specific reporter/MPRA shows no NR4A1-dependent allele effect at this element.; NR4A1 knockdown does not change the allele-dependent enhancer or FTO expression effect.

## Prediction matrix

| Test | Cost | Separates top two | H4_null | H1_ARID5B_repressor_loss | H2_ESRRA_alt_binding | H3_NR4A1_alt_binding |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B EMSA or ChIP-qPCR at chr16:53767042 ref T vs alt C in subcutaneous preadipocytes | medium | yes | No allele-specific ARID5B binding. | Alt C binds ARID5B more strongly than ref T. | No ARID5B allele-specific binding; ESRRA is the relevant TF instead. | No ARID5B allele-specific binding; NR4A1 is the relevant TF instead. |
| Allele-specific ESRRA ChIP-qPCR at chr16:53767042 in subcutaneous preadipocytes | medium | no | No allele-specific ESRRA binding. | No ESRRA allele-specific binding; ARID5B is the relevant TF instead. | Alt C binds ESRRA more strongly than ref T. | No ESRRA allele-specific binding; NR4A1 is the relevant TF instead. |
| Targeted MPRA of the dELS ref T vs alt C in preadipocytes, with and without ARID5B knockdown | medium | yes | No allele-dependent enhancer activity. | Alt C increases enhancer activity if ARID5B represses; ARID5B knockdown reduces the allele effect. | Alt-dependent enhancer activity is reduced by ESRRA knockdown. | Alt-dependent enhancer activity is reduced by NR4A1 knockdown. |
| Prime editing or heterozygous preadipocyte RNA-seq comparing ref T and alt C at this site | high | yes | No allele-dependent expression change after controlling for linked variants. | Allele-dependent change in IRX3/IRX5 expression. | Allele-dependent change in FTO expression. | Allele-dependent change in FTO expression. |

## Next experiment

Allele-specific ARID5B EMSA with recombinant ARID5B and ref T vs alt C probes, followed by ARID5B ChIP-qPCR in subcutaneous preadipocytes if the EMSA is positive.

## Investigate calls

- qbic_tf_detail({"tf": "ARID5B"})
- eqtl_lookup({"tissue": "Adipose - Subcutaneous"})
- chip_peaks({"biosample": "adipose", "tf": "ESRRA"})

## Flags

- quote_rejected: PMID 42440472: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:53767042-53767042:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:38:25+00:00)

> Variant chr16:53767042:T>C (GRCh38), allele string T/C
> Known IDs: rs1421085
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 2.55
> Transcript consequences: FTO (intron_variant, NMD_transcript_variant); FTO (intron_variant); FTO (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:52767042-54767042?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:38:17+00:00)

> 7 protein-coding genes within 1000 kb of chr16:53767042:T>C, by distance to TSS:
> RPGRIP1L: 63.1 kb from TSS (upstream, strand -1)
> FTO: 65.3 kb from TSS (in gene body, strand +1)
> AKTIP: 262.6 kb from TSS (upstream, strand -1)
> RBL2: 333.1 kb from TSS (downstream, strand +1)
> IRX3: 520.4 kb from TSS (downstream, strand -1)
> CHD9: 712.1 kb from TSS (downstream, strand +1)
> CHD9NB: 714.1 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:29:02+00:00)

> The variant lies in cCRE EH38E3181208 (dELS: distal enhancer-like), chr16:53766999-53767220.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3181207 dELS: DNase z 3.5, H3K27ac z 3.2, H3K4me3 z 1.5, CTCF z 1.5; nearby genes RPGRIP1L, FTO, AC007497.1
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs1421085&size=100; retrieved 2026-10-25T17:29:17+00:00)

> 100 GWAS Catalog associations for rs1421085, strongest first:
> Body mass index (BMI, mean, inv-normal transformed): p 9.9e-324, effect allele T, risk-allele frequency 0.669, PMID 39024449
> Body mass index (BMI, maximum, inv-normal transformed): p 9.9e-324, effect allele T, risk-allele frequency 0.669, PMID 39024449
> What is your weight? (pounds, inv-normal transformed): p 9.9e-324, effect allele T, risk-allele frequency 0.5909, PMID 39024449
> Weight (mean, inv-normal transformed): p 2.0e-300, effect allele T, risk-allele frequency 0.669, PMID 39024449
> Obesity (PheCode 278.1): p 6.0e-291, effect allele T, risk-allele frequency 0.593, PMID 39024449
> Body mass index (BMI, minimum, inv-normal transformed): p 2.0e-277, effect allele T, risk-allele frequency 0.669, PMID 39024449
> Overweight, obesity and other hyperalimentation (PheCode 278): p 4.0e-246, effect allele T, risk-allele frequency 0.5927, PMID 39024449
> Body shape phenotype PC1: p 2.0e-241, effect allele T, risk-allele frequency 0.596423, PMID 38640244
> Type 2 diabetes (PheCode 250.2): p 4.0e-211, effect allele T, risk-allele frequency 0.5926, PMID 39024449
> Diabetes mellitus (PheCode 250): p 8.0e-207, effect allele T, risk-allele frequency 0.5926, PMID 39024449
> Hemoglobin A1c (HbA1c, maximum, inv-norm transformed): p 8.0e-195, effect allele T, risk-allele frequency 0.5901, PMID 39024449
> Hemoglobin A1c (HbA1c, mean, inv-norm transformed): p 1.0e-185, effect allele T, risk-allele frequency 0.5901, PMID 39024449

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:10+00:00)

> 1701 credible sets contain 16_53767042_T_C: 200 GWAS, 0 molecular QTL.
> GWAS Body mass index (BMI, minimum, inv-normal transformed): PIP 0.85; L2G FTO 0.99, RPGRIP1L 0.20, CHD9 0.06
> GWAS Body mass index: PIP 0.80; L2G FTO 0.99, RPGRIP1L 0.25
> GWAS Impedance of leg left (UKB data field 23108): PIP 0.67; L2G FTO 0.99, RPGRIP1L 0.20
> GWAS Diabetes mellitus (PheCode 250): PIP 0.46; L2G FTO 0.99, RPGRIP1L 0.20, CHD9 0.06
> GWAS Impedance of leg left (UKB data field 23108): PIP 0.46; L2G FTO 0.99, RPGRIP1L 0.20
> GWAS Leg fat free mass left (UKB data field 23117): PIP 0.41; L2G FTO 0.99, RPGRIP1L 0.21, CHD9 0.07
> Best L2G gene scores across these sets: FTO 0.99, RPGRIP1L 0.36, CHD9 0.16

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1421085%20AND%20FTO%20AND%20%22obesity%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:18+00:00)

> Europe PMC: 653 hits for 'rs1421085 AND FTO AND "obesity"'; top 8 with PMIDs:
> PMID 42440472 (2026): A Rapid Genotyping Assay for &lt;i&gt;FTO&lt;/i&gt; and &lt;i&gt;PPAR-γ&lt;/i&gt; Nutrigenetic Variants in Thai Adults with Overweight/Obesity.
> PMID 41862896 (2026): Impact of fat mass and obesity-associated (FTO) gene variants on adult obesity and overweight: a comprehensive meta-analysis.
> PMID 41591493 (2026): Obesity-related RNA m&lt;sup&gt;6&lt;/sup&gt;A demethylase gene FTO rs1421085 is associated with neuroticism in a longitudinal birth cohort study.
> PMID 42197023 (2026): Associations Between FTO rs9939609 Genotype, Physical Activity, and Dietary Behaviors in Young Adults.
> PMID 42757464 (2026): Demethylase FTO attenuates atherosclerotic plaque via upregulating ABCA1 and ABCG1 expression by targeting ATG5.
> PMID 42299366 (2026): Hepatogenomics of MAFLD in Asian Population: Genetic Polymorphisms and Pathway-Based Insights.
> PMID 42534632 (2025): Genetic Polymorphisms Associated with Obesity in Southeast Asian Populations: A Systematic Review without Meta-Analysis.
> PMID 42245481 (2026): FTO in cardiovascular diseases: mechanisms, context dependence, and translational opportunities.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:53767042:T>C: 997 models scored, 425 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 275 CIS-BP groups. Expression context: GTEx tissue median Adipose - Subcutaneous. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 53 (CUT; Homeodomain, 3 models z -47.91, C2H2 ZF, 1 model z -42.95, Homeodomain, 2 models z -30.65, C2H2 ZF, 2 models z 21.18, Homeodomain; POU, 1 model z -19.44). Passing groups ranked below the ones shown: 212. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G037 (Nuclear receptor, 3 models): best model ESRRG_FL_TGAGCT40NGCA_KW_yin2017_0_3_7mer (own model of ESRRG), z 62.01, effect 2.149 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: ESRRG z 62.01, ESRRB z 25.92, ESRRA z 17.39. TFs this group covers: ESRRA (own model) 34.08 TPM, ESR1 (own model) 2.07 TPM, ESR2 (mapped) 0.83 TPM, ESRRB (own model) 0.16 TPM, ESRRG (own model) 0.06 TPM; best model's site strength: ref 94.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G008 (Homeodomain, 9 models): best model PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer (own model of PKNOX2), z 54.71, effect 3.047 (alt binds more); 9 passing models (9 with the best model's sign). Passing members: PKNOX2 z 54.71, TGIF2 z 42.72, MEIS3 z 40.95, TGIF2LX z 36.97, MEIS2 z 35.14 (+4 more). TFs this group covers: TGIF1 (own model) 13.07 TPM, TGIF2 (own model) 11.62 TPM, MEIS3 (own model) 9.23 TPM, PKNOX1 (own model) 7.35 TPM, MEIS2 (own model) 5.53 TPM, MEIS1 (own model) 4.65 TPM, PKNOX2 (own model) 2.8 TPM, TGIF2LX (own model) 0.0 TPM, TGIF2LY (own model) 0.0 TPM; best model's site strength: ref 95.5th, alt 99.7th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G002 (Nuclear receptor, 29 models): best model NR4A3_DBD_TTCGTA20NTA_KH_nitta2015_1_3_7mer (own model of NR4A3), z 32.74, effect 2.426 (alt binds more); 19 passing models (18 with the best model's sign); members disagree on direction. Passing members: NR4A3 z 32.74, NR2C1 z 21.97, NR5A1 z 21.36, NR4A1 z 16.25, NR4A2 z 15.74 (+14 more). TFs this group covers: NR4A1 (own model) 139.74 TPM, NR1D1 (own model) 118.5 TPM, PPARG (own model) 111.14 TPM, NR2F2 (own model) 101.24 TPM, NR1H2 (mapped) 73.96 TPM, RXRB (own model) 63.05 TPM, NR1H3 (own model) 53.67 TPM, THRA (own model) 41.46 TPM, RXRA (own model) 39.73 TPM, RARA (own model) 37.57 TPM (+28 more); best model's site strength: ref 99.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G007 (Forkhead, 10 models): best model FOXL1_NA_TGCTCG20NCTC_ESW_yang2017_0_2_7mer (own model of FOXL1), z -32.62, effect -1.076 (alt binds less); 7 passing models (6 with the best model's sign); members disagree on direction. Passing members: FOXL1 z -32.62, FOXC2 z -16.49, FOXG1 z -15.83, FOXC1 z -15.51, FOXF1 z 7.79 (+2 more). TFs this group covers: FOXJ3 (own model) 33.71 TPM, FOXJ2 (own model) 24.29 TPM, FOXC1 (own model) 22.42 TPM, FOXP4 (mapped) 20.41 TPM, FOXP1 (own model) 14.95 TPM, FOXK2 (mapped) 13.86 TPM, FOXK1 (own model) 10.32 TPM, FOXS1 (mapped) 4.39 TPM, FOXF2 (mapped) 3.25 TPM, FOXC2 (own model) 3.09 TPM (+18 more); best model's site strength: ref 99.9th, alt 98.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G043 (bZIP, 3 models): best model NFE2L3_FL_TACGAG20NAGC_KH_nitta2015_1_3_7mer (own model of NFE2L3), z 28.3, effect 1.411 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: NFE2L3 z 28.3, NFE2L1 z 8.62. TFs this group covers: NFE2L1 (own model) 185.6 TPM, NFE2L2 (mapped) 65.58 TPM, NFE2L3 (own model) 8.21 TPM, NFE2 (own model) 0.6 TPM; best model's site strength: ref 96.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G033 (bZIP, 3 models): best model ATF2_eDBD_TGAACC40NCCA_KP_yin2017_0_3_7mer (own model of ATF2), z 28.08, effect 1.047 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: ATF2 z 28.08, CREB5 z 27.01, ATF7 z 10.29. TFs this group covers: ATF7 (own model) 38.23 TPM, ATF2 (own model) 26.88 TPM, CREB5 (own model) 6.45 TPM, ATF7-NPFF (mapped); best model's site strength: ref 98.6th, alt 99.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G022 (Forkhead, 4 models): best model FOXB1_NA_TGAGCA30NCGA_ESAI_yang2017_0_4_7mer (own model of FOXB1), z -23.72, effect -1.232 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: FOXB1 z -23.72, FOXA1 z -13.3, FOXA3 z -8.79, FOXA2 z -7.96. TFs this group covers: FOXS1 (mapped) 4.39 TPM, FOXA3 (own model) 0.06 TPM, FOXA1 (own model) 0.05 TPM, FOXA2 (own model) 0.0 TPM, FOXB1 (own model) 0.0 TPM, FOXB2 (mapped) 0.0 TPM; best model's site strength: ref 99.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G048 (Homeodomain, 3 models): best model SIX1_eDBD_TTAACC40NCTA_KQ_yin2017_0_4_7mer (own model of SIX1), z -22.75, effect -0.856 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: SIX1 z -22.75, SIX2 z -19.68, SIX4 z -8.7. TFs this group covers: SIX5 (mapped) 16.4 TPM, SIX1 (own model) 8.49 TPM, SIX2 (own model) 5.54 TPM, SIX4 (own model) 0.69 TPM; best model's site strength: ref 99.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G009 (Paired box, 8 models): best model PAX7_FL_TCGTTT40NGTC_KAF_yin2017_0_4_7mer (own model of PAX7), z 22.55, effect 1.934 (alt binds more); 8 passing models (8 with the best model's sign). Passing members: PAX7 z 22.55, PAX3 z 16.01, PAX9 z 15.43, PAX8 z 15.39, PAX2 z 12.88 (+3 more). TFs this group covers: PAX8 (own model) 2.24 TPM, PAX3 (own model) 0.4 TPM, PAX9 (own model) 0.14 TPM, PAX5 (own model) 0.04 TPM, PAX1 (own model) 0.03 TPM, PAX2 (own model) 0.01 TPM, PAX6 (own model) 0.01 TPM, PAX4 (own model) 0.0 TPM, PAX7 (own model) 0.0 TPM; best model's site strength: ref 90.7th, alt 99.7th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G162 (Unknown, 1 model): best model DACH1_FL_TG40NTGTGTT_YWO_jolma2025_0_3_7mer (own model of DACH1), z 21.79, effect 0.795 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: DACH1 z 21.79. TFs this group covers: DACH1 (own model) 6.37 TPM; best model's site strength: ref 86.1th, alt 99.9th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ARID5B","symbol":"ARID5B","via":"hgnc_symbol","notes":[],"coverage":"not_in_coverage"}

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_53767042_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:38+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_53767042_T_C_b38 in tissues matching 'Adipose - Subcutaneous'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:44:29+00:00)

> No ENCODE ESRRA ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'adipose'. Absence can also mean no ESRRA experiment in that biosample. 0 peaks lie within 100 bp without containing it.
