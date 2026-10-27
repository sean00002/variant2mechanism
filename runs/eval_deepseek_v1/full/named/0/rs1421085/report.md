# rs1421085 and Obesity (FTO)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.05 over 9 model calls; 251 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## QBiC-SELEX screen

425 of 997 models pass the gate. Top groups: Nuclear receptor, 3 models (best ESRRG, z 62.01); Homeodomain, 9 models (best PKNOX2, z 54.71); Nuclear receptor, 29 models (best NR4A3, z 32.74); Forkhead, 10 models (best FOXL1, z -32.62); bZIP, 3 models (best NFE2L3, z 28.3).

## Ranked chains

### 1. H4_null: Null: linked causal variant or no allelic TF effect (p = 0.58)

Null chain: no TF-mediated effect of this variant.

Predictions: No TF binds rs1421085 allele-specifically in the relevant adipose/preadipocyte context.; Reporter assays show no allelic difference for the rs1421085-containing enhancer.; The obesity association is explained by a linked causal variant rather than rs1421085 itself.

Falsified if: Allele-specific TF binding or enhancer reporter activity differs between ref T and alt C at rs1421085.; CRISPR allele swap at rs1421085 changes FTO or IRX3 expression in preadipocytes.; Conditional analysis shows the obesity signal is not explained by a linked causal variant.

### 2. H2_ESRRA: ESRRA repressor chain (p = 0.27)

TF ESRRA (stated coverage own_model; registry own_model), alt allele binds more; element distal enhancer-like cCRE EH38E3181208; gene FTO; cell type subcutaneous adipose / preadipocyte (proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ESRRA has an own QBiC-SELEX model in group G037 and is predicted to bind alt C more strongly. ESRRA is chosen within G037 over the group-leading ESRRG because ESRRA has much higher adipose expression (34.08 vs 0.06 TPM). No adipose ESRRA ChIP-seq peak contains the variant, so occupancy is unproven. | weak | [E08](#e08), [E20](#e20) |
| element | rs1421085 lies in the distal enhancer-like cCRE EH38E3181208 (dELS). | supported | [E03](#e03) |
| gene | FTO is the best L2G gene for the BMI credible sets at this locus, supporting FTO as the candidate target gene, though L2G does not prove enhancer-gene regulation. | supported | [E05](#e05) |
| cell_type | GTEx subcutaneous adipose is the supplied expression context and is used as a proxy for preadipocytes; preadipocyte-specific evidence is not supplied. | weak | [E07](#e07) |
| phenotype | rs1421085 is strongly associated with obesity/BMI with effect allele T in E04. If ESRRA represses FTO, stronger alt C binding would lower FTO and be protective, making ref T risk, but this repression is unproven. | weak | [E04](#e04), [E06b](#e06b), [E06c](#e06c) |

Predictions: ESRRA ChIP/CUT&RUN will show ESRRA occupancy at the rs1421085 enhancer in preadipocytes.; Allele-specific ESRRA binding will favor alt C.; ESRRA knockdown or inhibition will increase FTO expression if ESRRA is a repressor.; The alt C allele will be protective or lower risk in allele-resolved functional follow-up.

Falsified if: ESRRA does not occupy the rs1421085 enhancer in adipose or preadipocytes.; Allele-specific ESRRA binding does not favor alt C.; ESRRA perturbation does not change FTO expression or enhancer activity.

### 3. H3_FOXC1: FOXC1 activator chain (p = 0.10)

TF FOXC1 (stated coverage own_model; registry own_model), ref allele binds more; element distal enhancer-like cCRE EH38E3181208; gene IRX3; cell type subcutaneous adipose / preadipocyte (proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXC1 has an own QBiC-SELEX model in group G007 and is predicted to bind ref T more strongly (negative effect). FOXC1 is chosen within G007 because it has high adipose expression (22.42 TPM), but FOXL1 is the group leader and G007 members disagree on direction; occupancy is unproven. | weak | [E11](#e11) |
| element | rs1421085 lies in the distal enhancer-like cCRE EH38E3181208 (dELS). | supported | [E03](#e03) |
| gene | IRX3 is a nearby candidate gene, but E02 supports only proximity/distance, not enhancer-gene contact or FOXC1-dependent regulation. | weak | [E02](#e02) |
| cell_type | GTEx subcutaneous adipose is the supplied expression context and is used as a proxy for preadipocytes; preadipocyte-specific evidence is not supplied. | weak | [E07](#e07) |
| phenotype | rs1421085 is strongly associated with obesity/BMI with effect allele T in E04. If FOXC1 activates IRX3, stronger ref T binding would make ref T risk, but the activation sign is unproven. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: FOXC1 ChIP/CUT&RUN will show FOXC1 occupancy at the rs1421085 enhancer.; Allele-specific FOXC1 binding will favor ref T.; FOXC1 overexpression or knockdown will change IRX3 expression in preadipocytes.; The ref T allele will show higher enhancer activity in reporter assays if FOXC1 activates the element.

Falsified if: FOXC1 does not bind the rs1421085 enhancer in adipose or preadipocytes.; Allele-specific assays do not show stronger ref T binding.; FOXC1 perturbation does not affect IRX3 or the enhancer reporter.

### 4. H1_ARID5B_classic: ARID5B enhancer-derepression chain (p = 0.05)

TF ARID5B (stated coverage not_in_coverage; registry not_in_coverage), ref allele binds more; element distal enhancer-like cCRE EH38E3181208; gene IRX3; cell type subcutaneous adipose / preadipocyte (proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B is proposed to bind ref T more strongly than alt C, but QBiC-SELEX reports ARID5B as not_in_coverage and no ENCODE ARID5B ChIP-seq peak contains the variant; the supplied evidence does not support this binding change. | missing | [E18](#e18), [E19](#e19) |
| element | rs1421085 lies in the distal enhancer-like cCRE EH38E3181208 (dELS). | supported | [E03](#e03) |
| gene | IRX3 is a nearby candidate gene, but E02 supports only proximity/distance, not enhancer-gene contact or regulation. | weak | [E02](#e02) |
| cell_type | GTEx subcutaneous adipose is the supplied expression context and is used as a proxy for preadipocytes; preadipocyte-specific evidence is not supplied. | weak | [E07](#e07) |
| phenotype | rs1421085 is associated with obesity/BMI, but the allelic direction is unresolved: E04 reports effect allele T, while E06d reports the C allele associated with overweight/obesity. The classic ARID5B C-risk/derepression prediction is not supported by E04. | weak | [E04](#e04), [E06d](#e06d) |

Predictions: Allele-specific ARID5B EMSA/ChIP in preadipocytes will show stronger binding to ref T than alt C.; The C allele will increase IRX3 expression if ARID5B normally represses this enhancer.; The C allele will be the obesity-increasing allele in allele-resolved functional assays, which conflicts with E04's reported effect allele T.

Falsified if: ARID5B does not bind the rs1421085 region allele-specifically in preadipocytes.; Allele-specific reporter or CRISPR swap shows no functional difference between T and C.; IRX3 is not derepressed by the C allele in preadipocytes.

## Prediction matrix

| Test | Cost | Separates top two | H4_null | H2_ESRRA | H3_FOXC1 | H1_ARID5B_classic |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ESRRA EMSA with T vs C rs1421085 oligonucleotides | low | yes | No allele-specific ESRRA binding at rs1421085. | ESRRA binds alt C more strongly than ref T. | No ESRRA allele-specific binding at rs1421085. | No ESRRA allele-specific binding at rs1421085. |
| Allele-specific ARID5B EMSA with T vs C rs1421085 oligonucleotides | low | no | No allele-specific ARID5B binding at rs1421085. | No ARID5B allele-specific binding at rs1421085. | No ARID5B allele-specific binding at rs1421085. | ARID5B binds ref T more strongly than alt C. |
| Allele-specific FOXC1 EMSA with T vs C rs1421085 oligonucleotides | low | no | No allele-specific FOXC1 binding at rs1421085. | No FOXC1 allele-specific binding at rs1421085. | FOXC1 binds ref T more strongly than alt C. | No FOXC1 allele-specific binding at rs1421085. |
| Enhancer reporter or MPRA with ref T vs alt C rs1421085 in preadipocytes | medium | yes | No allelic difference in enhancer activity. | Alt C lowers enhancer activity if ESRRA is a repressor. | Ref T shows higher enhancer activity if FOXC1 is an activator. | Allelic enhancer activity difference, with C predicted to derepress activity if C is the ARID5B-loss risk allele. |
| ESRRA knockdown/inhibition in preadipocytes followed by FTO expression measurement | high | yes | No FTO expression change after ESRRA knockdown. | ESRRA knockdown increases FTO expression if ESRRA represses FTO. | No specific ESRRA-dependent effect; FOXC1 perturbation is the relevant test. | No specific ESRRA-dependent effect; ARID5B perturbation is the relevant test. |
| CRISPR allele swap at rs1421085 in preadipocytes with FTO/IRX3 expression readout | high | yes | No change, or the signal is explained by a linked variant rather than rs1421085. | C allele swap lowers FTO expression if ESRRA represses FTO. | T allele swap increases IRX3 expression if FOXC1 activates this enhancer. | C allele swap changes IRX3 expression if ARID5B represses this enhancer. |

## Next experiment

Allele-specific ESRRA EMSA with recombinant ESRRA on T vs C rs1421085 oligonucleotides is the cheapest experiment that separates the top two chains (H2_ESRRA vs H4_null). It tests the predicted alt-C-greater ESRRA binding directly; a follow-up ChIP-qPCR in heterozygous preadipocytes would test occupancy in chromatin.

## Investigate calls

- qbic_tf_detail({"tf": "ARID5B"})
- chip_peaks({"biosample": null, "tf": "ARID5B"})
- chip_peaks({"biosample": "adipose", "tf": "ESRRA"})

## Flags

- none

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

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 42440472 (https://europepmc.org/article/MED/42440472; retrieved 2026-10-25T17:29:18+00:00)

> ObjectivesThe aim of this study is to develop, validate, and apply a cost-effective 4-plex high-resolution melting (HRM) assay for simultaneous detection of FTO (rs9939609 and rs1421085) and PPAR-γ (rs1801282 and rs3856806) variants using standard laboratory equipment.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 41862896 (https://europepmc.org/article/MED/41862896; retrieved 2026-10-25T17:29:18+00:00)

> In the obesity group, the rs1421085 exhibited the strongest effect, with an odds ratio (OR) of 2.16 (95% CI: 1.58–2.95).

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 41862896 (https://europepmc.org/article/MED/41862896; retrieved 2026-10-25T17:29:18+00:00)

> CONCLUSION: This meta-analysis provides strong evidence that FTO polymorphisms, particularly rs1421085 and rs9939609, are significantly associated with increased susceptibility to obesity in adults, while their impact on overweight is comparatively weaker.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 41591493 (https://europepmc.org/article/MED/41591493; retrieved 2026-10-25T17:29:18+00:00)

> Based on findings that experimental manipulation of the RNA m6A methylation in animal experiments can affect anxiety, and given that the C-allele of FTO rs1421085 had a significant association with indicators of overweight and obesity in our previous study, we have examined the possible association of FTO rs1421085 genotype with neuroticism in the same longitudinally observed sample.

<a id="e06e"></a>**E06e** literature_search, Europe PMC abstract, PMID 41591493 (https://europepmc.org/article/MED/41591493; retrieved 2026-10-25T17:29:18+00:00)

> Statistically significant assocation between the FTO rs1421085 genotype and neuroticism emerged by age 25, with an additive effect of each T-allele.

<a id="e06f"></a>**E06f** literature_search, Europe PMC abstract, PMID 42534632 (https://europepmc.org/article/MED/42534632; retrieved 2026-10-25T17:29:18+00:00)

> LEP variants were not significantly associated with obesity in Malaysians, and FTO variants showed mixed results, with rs9939609 (OR = 3.72, P = 0.009) and rs1421085 (OR = 3.22, P < 0.001) variants being associated with obesity and higher body mass index (BMI) in Indonesians, but no significant findings in Malaysians.

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

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:30:39+00:00)

> No ENCODE ARID5B ChIP-seq peak contains chr16:53767042:T>C. Absence can also mean no ARID5B experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:44:29+00:00)

> No ENCODE ESRRA ChIP-seq peak contains chr16:53767042:T>C in biosamples matching 'adipose'. Absence can also mean no ESRRA experiment in that biosample. 0 peaks lie within 100 bp without containing it.
