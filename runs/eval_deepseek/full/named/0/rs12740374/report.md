# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 391 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen

239 of 997 models pass the gate. Top groups: C2H2 ZF, 1 model (best ZNF43, z 35.83); bZIP, 1 model (best CEBPG, z 26.76); C2H2 ZF, 1 model (best ZNF696, z -24.85); RFX, 4 models (best RFX4, z 23.16); bZIP, 3 models (best CEBPB, z 22.81).

## Ranked chains

### 1. H1: CEBPA binds the alt T allele at a SORT1 enhancer and increases SORT1, lowering LDL risk (p = 0.52)

TF CEBPA (stated coverage own_model; registry own_model), alt allele binds more; element distal enhancer-like cCRE EH38E1374646; gene SORT1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele strengthens the C/EBP bZIP binding specificity in QBiC-SELEX group G035, where CEBPA is an own-model passing member with alt-more direction (z 22.63); CEBPA also has an ENCODE ChIP-seq peak containing rs12740374 in HepG2. This supports CEBPA occupancy but does not by itself prove allele-specific binding. | weak | [E12](#e12), [E18](#e18), [E07](#e07) |
| element | rs12740374 lies within EH38E1374646, a distal enhancer-like cCRE with DNase, H3K27ac and H3K4me3 signal, making it a plausible allele-sensitive regulatory element. | supported | [E03](#e03), [E01](#e01) |
| gene | SORT1 is the top L2G gene for the credible sets and has a liver sQTL; the alt T allele also increases liver SORT1 expression in GTEx, making SORT1 the leading candidate target. | supported | [E05](#e05), [E20](#e20), [E02](#e02) |
| cell_type | Hep3B is the stated expression context, CEBPA is highly expressed there, and CEBPA ChIP-seq occupancy is seen in HepG2, supporting a hepatocyte CEBPA-dependent mechanism. | supported | [E07](#e07), [E12](#e12), [E18](#e18) |
| phenotype | The G allele is the high-cholesterol risk allele, while the alt T allele increases liver SORT1 expression; this is consistent with the T allele being LDL-lowering/protective at the 1p13 locus, though GWAS effect sizes do not fully resolve LDL direction. | weak | [E04](#e04), [E20](#e20), [E06](#e06) |

Predictions: CEBPA occupancy at rs12740374 is stronger on the T allele than on the G allele in hepatocytes.; CEBPA knockdown or CEBPA motif mutation reduces the T-allele enhancer activity and SORT1 expression effect.; Editing rs12740374 alone changes SORT1 expression in a CEBPA-dependent manner.

Falsified if: Allele-specific CEBPA occupancy is not stronger on the T allele at rs12740374 in a hepatocyte line.; CEBPA knockdown or motif mutation does not reduce the T-allele enhancer/SORT1 effect.; CRISPR editing of rs12740374 alone does not change SORT1 expression in hepatocytes.

### 2. H0: Null: no TF-mediated effect of rs12740374 (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No TF-mediated allelic effect at rs12740374; the association is explained by a linked causal variant or another non-TF mechanism.; Allele-specific binding predictions do not translate into an allele-specific enhancer or SORT1 effect.; CRISPR editing of rs12740374 alone does not change SORT1 expression in hepatocytes.

Falsified if: Allele-specific TF binding and a corresponding enhancer/SORT1 expression effect are demonstrated for rs12740374.; Editing the variant alone changes enhancer activity or SORT1 expression in hepatocytes.

### 3. H2: CEBPB binds the alt T allele at a SORT1 enhancer and increases SORT1, lowering LDL risk (p = 0.12)

TF CEBPB (stated coverage own_model; registry own_model), alt allele binds more; element distal enhancer-like cCRE EH38E1374646; gene SORT1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele strengthens binding in QBiC-SELEX group G035, whose best model is CEBPB (own model, z 22.81, effect 2.331, alt-more); CEBPB is expressed in Hep3B, but no CEBPB ChIP-seq evidence at this variant is cited. | weak | [E12](#e12), [E07](#e07) |
| element | The variant lies in the distal enhancer-like cCRE EH38E1374646, a candidate allele-sensitive regulatory element. | supported | [E03](#e03), [E01](#e01) |
| gene | SORT1 is the top L2G gene and has a liver sQTL; the alt T allele increases liver SORT1 expression in GTEx. | supported | [E05](#e05), [E20](#e20), [E02](#e02) |
| cell_type | Hep3B is the expression context and CEBPB is expressed there, though at lower levels than CEBPA, so a hepatocyte CEBPB mechanism remains possible. | weak | [E07](#e07), [E12](#e12) |
| phenotype | The G allele is the high-cholesterol risk allele and the alt T allele increases liver SORT1; this is consistent with T being the non-risk/LDL-lowering allele, though LDL effect direction is not fully resolved by GWAS alone. | weak | [E04](#e04), [E20](#e20), [E06](#e06) |

Predictions: CEBPB ChIP is stronger on the T allele at rs12740374 in hepatocytes.; CEBPB knockdown reduces the T-allele enhancer/SORT1 effect.; CEBPA occupancy is not allele-specific at this site.

Falsified if: CEBPB does not occupy rs12740374 allele-specifically in hepatocytes.; CEBPB loss or motif mutation does not alter the T-allele enhancer/SORT1 effect.

### 4. H3: CEBPG binds the alt T allele at a SORT1 enhancer and increases SORT1, lowering LDL risk (p = 0.07)

TF CEBPG (stated coverage own_model; registry own_model), alt allele binds more; element distal enhancer-like cCRE EH38E1374646; gene SORT1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele strengthens CEBPG binding in QBiC-SELEX group G143: CEBPG has its own model, z 26.76 with effect 2.321 (alt binds more), and is expressed at 46.37 TPM in the Hep3B context. | weak | [E09](#e09), [E07](#e07) |
| element | rs12740374 sits in EH38E1374646, a distal enhancer-like cCRE with active chromatin marks. | supported | [E03](#e03), [E01](#e01) |
| gene | SORT1 is the best L2G target and has a liver sQTL; the alt T allele increases liver SORT1 expression. | supported | [E05](#e05), [E20](#e20), [E02](#e02) |
| cell_type | CEBPG is expressed in Hep3B, so a hepatocyte CEBPG-dependent mechanism is plausible. | supported | [E09](#e09), [E07](#e07) |
| phenotype | The G allele is the high-cholesterol risk allele and the alt T allele increases liver SORT1; this is consistent with T being the non-risk/LDL-lowering allele, though LDL effect direction is not fully resolved. | weak | [E04](#e04), [E20](#e20), [E06](#e06) |

Predictions: CEBPG ChIP is stronger on the T allele at rs12740374.; CEBPG loss reduces T-allele enhancer activity and SORT1 expression.; CEBPA and CEBPB are not the allele-specific factors at this site.

Falsified if: CEBPG does not occupy rs12740374 allele-specifically in hepatocytes.; CEBPG perturbation does not affect the T-allele enhancer or SORT1 expression.

### 5. H4: RFX5 binds the alt T allele at a SORT1 enhancer and increases SORT1, lowering LDL risk (p = 0.04)

TF RFX5 (stated coverage own_model; registry own_model), alt allele binds more; element distal enhancer-like cCRE EH38E1374646; gene SORT1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele strengthens RFX binding in QBiC-SELEX group G094; RFX5 has its own model and passes with z 11.53 in the alt-more direction, and it is expressed at 41.14 TPM in Hep3B. | weak | [E15](#e15), [E07](#e07) |
| element | The variant lies within the distal enhancer-like cCRE EH38E1374646. | supported | [E03](#e03), [E01](#e01) |
| gene | SORT1 is the top L2G gene and has a liver sQTL; the alt T allele increases liver SORT1 expression. | supported | [E05](#e05), [E20](#e20), [E02](#e02) |
| cell_type | RFX5 is expressed in Hep3B, making a hepatocyte RFX5 mechanism possible. | supported | [E15](#e15), [E07](#e07) |
| phenotype | The G allele is the high-cholesterol risk allele and the alt T allele increases liver SORT1; this is consistent with T being the non-risk/LDL-lowering allele, though LDL direction is not fully resolved. | weak | [E04](#e04), [E20](#e20), [E06](#e06) |

Predictions: RFX5 occupancy is higher on the T allele at rs12740374.; RFX5 knockdown weakens the T-allele enhancer/SORT1 effect.; C/EBP-family occupancy is not allele-specific at this site.

Falsified if: RFX5 does not occupy rs12740374 allele-specifically.; RFX5 perturbation does not alter the enhancer or SORT1 effect.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CEBPA ChIP-qPCR or CUT&RUN at rs12740374 in a heterozygous hepatocyte line | medium | yes | CEBPA occupancy is stronger on T than G at rs12740374. | No allele-specific TF occupancy at rs12740374. | CEBPA is not allele-specific; CEBPB may instead be stronger on T. | CEBPA is not allele-specific. | CEBPA is not allele-specific. |
| Allele-specific CEBPB ChIP-qPCR at rs12740374 in hepatocytes | medium | no | CEBPB is not allele-specific; CEBPA is stronger on T. | No allele-specific TF occupancy. | CEBPB occupancy is stronger on T than G. | CEBPB is not allele-specific. | CEBPB is not allele-specific. |
| Allele-specific CEBPG ChIP-qPCR at rs12740374 in hepatocytes | medium | no | No CEBPG allele-specific effect; CEBPA is stronger on T. | No allele-specific TF occupancy. | No CEBPG allele-specific effect; CEBPB may be stronger on T. | CEBPG occupancy is stronger on T. | No CEBPG allele-specific effect. |
| Allele-specific reporter/MPRA with G vs T enhancer and CEBPA knockdown or CEBPA motif mutation | medium | yes | T allele increases enhancer activity and the effect is reduced by CEBPA knockdown/motif mutation. | No allele-specific enhancer activity. | T allele increases enhancer activity and the effect is reduced by CEBPB knockdown/motif mutation. | T allele increases enhancer activity and the effect is reduced by CEBPG knockdown/motif mutation. | T allele increases enhancer activity and the effect is reduced by RFX5 knockdown/motif mutation. |
| CRISPR base editing of rs12740374 alone in a hepatocyte line, measuring SORT1 expression | high | yes | Editing rs12740374 alone changes SORT1 expression in a CEBPA-dependent direction. | Editing rs12740374 alone does not change SORT1 expression. | Editing rs12740374 alone changes SORT1 expression in a CEBPB-dependent direction. | Editing rs12740374 alone changes SORT1 expression in a CEBPG-dependent direction. | Editing rs12740374 alone changes SORT1 expression in an RFX5-dependent direction. |

## Next experiment

Allele-specific CEBPA ChIP-qPCR or CUT&RUN at rs12740374 in a hepatocyte line heterozygous for the variant is the cheapest single experiment that directly separates H1 from H0: H1 predicts stronger CEBPA occupancy on T, while H0 predicts no allele-specific TF occupancy. Cost: medium.

## Investigate calls

- chip_peaks({"tf": "CEBPA", "biosample": "HepG2"})
- literature_search({"query": "rs12740374 CEBP SORT1 allele-specific enhancer reporter"})
- eqtl_lookup({"tissue": "liver"})

## Flags

- quote_rejected: PMID 42019808: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/1:109274968-109274968:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T18:05:00+00:00)

> Variant chr1:109274968:G>T (GRCh38), allele string G/T
> Known IDs: rs12740374
> Most severe consequence: 3_prime_UTR_variant
> Regulatory features: ENSR1_CDSQQ enhancer
> GERP conservation score at the site: -0.782
> Transcript consequences: CELSR2 (3_prime_UTR_variant); PSRC1 (downstream_gene_variant); CELSR2 (downstream_gene_variant); CELSR2 (non_coding_transcript_exon_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/1:108274968-110274968?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T18:05:25+00:00)

> 41 protein-coding genes within 1000 kb of chr1:109274968:G>T, by distance to TSS:
> PSRC1: 9.1 kb from TSS (downstream, strand -1)
> CELSR2: 25.4 kb from TSS (in gene body, strand +1)
> MYBPHL: 32.2 kb from TSS (downstream, strand -1)
> SARS1: 61.1 kb from TSS (downstream, strand +1)
> SORT1: 123.0 kb from TSS (downstream, strand -1)
> PSMA5: 151.5 kb from TSS (downstream, strand -1)
> CFAP276: 161.1 kb from TSS (upstream, strand -1)
> ELAPOR1: 161.8 kb from TSS (downstream, strand +1)
> TMEM167B: 184.6 kb from TSS (downstream, strand +1)
> SYPL2: 191.6 kb from TSS (upstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:28:56+00:00)

> The variant lies in cCRE EH38E1374646 (dELS: distal enhancer-like), chr1:109274794-109275142.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E1374646 dELS (contains the variant): DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 4.2, CTCF z 1.9; nearby genes CELSR2, PSRC1, MYBPHL
> EH38E2829474 dELS: DNase z 3.2, H3K27ac z 4.8, H3K4me3 z 4.4, CTCF z 1.9; nearby genes CELSR2, PSRC1, MYBPHL
> EH38E2829475 dELS: DNase z 4.6, H3K27ac z 4.5, H3K4me3 z 3.7, CTCF z 1.6; nearby genes CELSR2, PSRC1, MYBPHL
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs12740374&size=100; retrieved 2026-10-25T17:29:12+00:00)

> 100 GWAS Catalog associations for rs12740374, strongest first:
> High cholesterol: p 9.9e-324, effect allele G, risk-allele frequency 0.7788, PMID 39024449
> Takes medication for high cholesterol?: p 6.0e-297, effect allele G, risk-allele frequency 0.7815, PMID 39024449
> Disorders of lipid metabolism (PheCode 272): p 7.0e-262, effect allele G, risk-allele frequency 0.778, PMID 39024449
> Circulating TNFSF13 levels: p 4.0e-260, effect allele ?, risk-allele frequency NR, PMID 42097137
> Hyperlipidemia (PheCode 272.1): p 6.0e-259, effect allele G, risk-allele frequency 0.778, PMID 39024449
> total cholesterol (minimum, inv-norm transformed): p 1.0e-208, effect allele G, risk-allele frequency 0.7774, PMID 39024449
> low density lipoprotein cholesterol (LDLC, maximum, inv-norm transformed): p 4.0e-164, effect allele G, risk-allele frequency 0.7453, PMID 39024449
> low density lipoprotein cholesterol (LDLC, mean, inv-norm transformed): p 4.0e-154, effect allele G, risk-allele frequency 0.7454, PMID 39024449
> Circulating LAG3 levels (id: OID05553_OID21315): p 1.0e-153, effect allele ?, risk-allele frequency NR, PMID 42097137
> Circulating LAG3 levels (id: OID01023_OID21315): p 1.0e-152, effect allele ?, risk-allele frequency NR, PMID 42097137
> LDL cholesterol levels: p 2.0e-137, effect allele T, risk-allele frequency NR, PMID 39414775
> total cholesterol (maximum, inv-norm transformed): p 2.0e-123, effect allele G, risk-allele frequency 0.7453, PMID 39024449

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:04+00:00)

> 2316 credible sets contain 1_109274968_G_T: 189 GWAS, 11 molecular QTL.
> GWAS Total cholines levels (UKB data field 23436): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Apolipoprotein B levels (UKB data field 23439): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Total cholesterol levels: PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Cholesterol to total lipids in large HDL percentage (UKB dat: PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Total lipids in small VLDL (UKB data field 23510): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Triglycerides in medium VLDL (UKB data field 23508): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> sqtl for SORT1 (gtex-v10_majiq_liver_ensg00000134243_s_109314672-1): PIP 0.72
> sqtl for CELSR2 (gtex-v10_majiq_muscle_ensg00000143126_s_109273436-): PIP 0.49
> eqtl for PSRC1 (gtex-v10_ge_pancreas_ensg00000134222): PIP 0.41
> eqtl for CELSR2 (gtex-v10_exon_esophagus_mucosa_ensg00000143126_8_1): PIP 0.37
> tuqtl for CELSR2 (gtex-v10_txrev_liver_ensg00000143126_grp_2_contain): PIP 0.32
> eqtl for PSRC1 (fairfax_2014_microarray_monocyte_naive_ilmn_231596): PIP 0.25
> Best L2G gene scores across these sets: SORT1 0.99, CELSR2 0.98, PSRC1 0.66

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20AND%20SORT1%20AND%20%28%22ldl%20cholesterol%22%20OR%20%22myocardial%20infarction%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:12+00:00)

> Europe PMC: 127 hits for 'rs12740374 AND SORT1 AND ("ldl cholesterol" OR "myocardial infarction")'; top 8 with PMIDs:
> PMID 42019808 (2026): Causal statistical association between remnant cholesterol and coronary heart disease: genetic insights into the PSRC1-CELSR2-SORT1 gene cluster.
> PMID 42820291 (2026): Clinical trials in a dish: cardiometabolic drug development with biological and digital twins.
> PMID 40922271 (2025): Effect of dietary habits on multiple cardiovascular diseases: A comprehensive Mendelian randomization study.
> PMID 41380003 (2025): Computationally efficient whole-genome quantile regression at biobank scale.
> PMID 39858645 (2025): Research Progress and Clinical Translation Potential of Coronary Atherosclerosis Diagnostic Markers from a Genomic Perspective.
> PMID 42211154 (2026): Treatment Target Discovery From Vasculo-Protective Phenotypes.
> PMID 41991941 (2026): Genetic and molecular factors underlying human longevity and epigenetic aging.
> PMID 38266112 (2024): Genome-Wide Genetic Associations Prioritize Evaluation of Causal Mechanisms of Atherosclerotic Disease Risk.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:109274968:G>T: 997 models scored, 239 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 182 CIS-BP groups. Expression context: DepMap line ACH-000625. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 44 (GCM, 2 models z -44.12, Homeodomain, 3 models z -27.46, C2H2 ZF, 1 model z 21.63, Homeodomain, 2 models z -17.61, bHLH, 1 model z -14.43). Passing groups ranked below the ones shown: 128. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G510 (C2H2 ZF, 1 model): best model ZNF43_FL_GC40NTATAGG_YWRA_jolma2025_0_3_7mer (own model of ZNF43), z 35.83, effect 3.431 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF43 z 35.83. TFs this group covers: ZNF43 (own model) 8.74 TPM; best model's site strength: ref 93.6th, alt 99.9th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G143 (bZIP, 1 model): best model CEBPG_eDBD_TACTTT40NTCT_KN_yin2017_0_4_7mer (own model of CEBPG), z 26.76, effect 2.321 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CEBPG z 26.76. TFs this group covers: CEBPG (own model) 46.37 TPM; best model's site strength: ref 64.5th, alt 99.4th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G570 (C2H2 ZF, 1 model): best model ZNF696_FL_AG40NTGGCTA_YWSA_jolma2025_0_2_7mer (own model of ZNF696), z -24.85, effect -0.713 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF696 z -24.85. TFs this group covers: ZNF696 (own model) 5.1 TPM; best model's site strength: ref 99.8th, alt 88.3th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G028 (RFX, 4 models): best model RFX4_eDBD_TACTCG40NCAA_KAN_yin2017_0_3_7mer (own model of RFX4), z 23.16, effect 1.235 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: RFX4 z 23.16, RFX1 z 16.27, RFX2 z 4.8. TFs this group covers: RFX2 (own model) 4.97 TPM, RFX1 (own model) 4.13 TPM, RFX3 (own model) 2.13 TPM, RFX6 (mapped) 0.35 TPM, RFX4 (own model) 0.0 TPM; best model's site strength: ref 95.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G035 (bZIP, 3 models): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (own model of CEBPB), z 22.81, effect 2.331 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: CEBPB z 22.81, CEBPA z 22.63, CEBPE z 11.28. TFs this group covers: CEBPA (own model) 141.33 TPM, CEBPB (own model) 4.05 TPM, CEBPE (own model) 0.0 TPM; best model's site strength: ref 87.0th, alt 99.8th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (own model of TFAP2E), z -21.21, effect -0.98 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TFAP2E z -21.21, TFAP2B z -18.18, TFAP2A z -13.22, TFAP2C z -12.55. TFs this group covers: TFAP2A (own model) 7.65 TPM, TFAP2E (own model) 2.06 TPM, TFAP2B (own model) 0.04 TPM, TFAP2C (own model) 0.01 TPM, TFAP2D (mapped) 0.0 TPM; best model's site strength: ref 99.8th, alt 98.8th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G491 (C2H2 ZF, 1 model): best model ZNF345_eDBD_TGTAAG40NACT_KT_yin2017_0_3_7mer (own model of ZNF345), z 20.62, effect 0.964 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF345 z 20.62. TFs this group covers: ZNF345 (own model) 1.64 TPM; best model's site strength: ref 97.7th, alt 99.9th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G094 (RFX, 2 models): best model RFX7_eDBD_TCGTCC40NGCC_KT_yin2017_0_4_7mer (own model of RFX7), z 18.73, effect 0.788 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: RFX7 z 18.73, RFX5 z 11.53. TFs this group covers: RFX5 (own model) 41.14 TPM, RFX7 (own model) 9.96 TPM; best model's site strength: ref 84.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G142 (bZIP, 1 model): best model CEBPD_NA_TAATGA20NCG_ESY_yang2017_0_2_7mer (own model of CEBPD), z 18.08, effect 1.253 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CEBPD z 18.08. TFs this group covers: CEBPD (own model) 5.4 TPM; best model's site strength: ref 88.1th, alt 99.1th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G012 (bZIP, 6 models): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (own model of MAFG), z 16.34, effect 0.625 (alt binds more); 5 passing models (5 with the best model's sign). Passing members: MAFG z 16.34, MAF z 11.17, MAFK z 10.91, NRL z 10.31, MAFA z 9.36. TFs this group covers: MAFK (own model) 39.41 TPM, MAFG (own model) 19.11 TPM, NRL (own model) 0.83 TPM, MAF (own model) 0.52 TPM, MAFB (own model) 0.47 TPM, MAFA (own model) 0.04 TPM; best model's site strength: ref 94.7th, alt 97.4th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:30:36+00:00)

> 1 ENCODE CEBPA ChIP-seq peaks contain chr1:109274968:G>T in biosamples matching 'HepG2': biosamples HepG2; experiments ENCSR142IGM.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20CEBP%20SORT1%20allele-specific%20enhancer%20reporter&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T01:49:17+00:00)

> Europe PMC: 5 hits for 'rs12740374 CEBP SORT1 allele-specific enhancer reporter'; top 5 with PMIDs:
> PMID 34038741 (2021): Genetic effects on liver chromatin accessibility identify disease regulatory variants.
> PMID 34024118 (2021): Single-Cell Epigenomics and Functional Fine-Mapping of Atherosclerosis GWAS Loci.
> PMID 31317254 (2020): Identifying causal variants and genes using functional genomics in specialized cell types and contexts.
> PMID 25835000 (2015): Lipid-induced epigenomic changes in human macrophages identify a coronary artery disease-associated variant that regulates PPAP2B Expression through Altered C/EBP-beta binding.
> PMID 32687525 (2020): Cross-species regulatory sequence activity prediction.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 34038741 (https://europepmc.org/article/MED/34038741; retrieved 2026-10-26T01:49:17+00:00)

> The caQTL variants are enriched in liver tissue promoter and enhancer states and frequently disrupt binding motifs of transcription factors expressed in liver.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 34038741 (https://europepmc.org/article/MED/34038741; retrieved 2026-10-26T01:49:17+00:00)

> At the LITAF LDL-cholesterol GWAS locus, we validated that a caQTL variant showed allelic differences in protein binding and transcriptional activity.

<a id="e19c"></a>**E19c** literature_search, Europe PMC abstract, PMID 25835000 (https://europepmc.org/article/MED/25835000; retrieved 2026-10-26T01:49:17+00:00)

> OxLDL increased C/EBP beta binding to this site and C/EBP beta binding and enhancer activity were stronger with the protective A allele of rs72664324.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_109274968_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:36+00:00)

> 5 significant GTEx v8 single-tissue eQTLs for chr1_109274968_G_T_b38 in tissues matching 'liver'. NES is the effect of the alt allele (T) relative to ref (G).
> SORT1 in Liver: NES +1.27, p 3.1e-54
> PSRC1 in Liver: NES +1.24, p 1.1e-37
> CELSR2 in Liver: NES +1.04, p 9.4e-34
> ATXN7L2 in Liver: NES +0.40, p 5.9e-07
> SYPL2 in Liver: NES +0.50, p 1.2e-06
