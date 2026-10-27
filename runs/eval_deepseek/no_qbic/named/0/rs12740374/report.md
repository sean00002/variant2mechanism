# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 9 model calls; 368 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. CEBPA_alt_SORT1_protective: CEBPA binds the protective T allele at the EH38E1374646 enhancer and raises SORT1 (p = 0.45)

TF CEBPA (stated coverage not_checked; registry own_model), alt allele binds more; element EH38E1374646 dELS enhancer; gene SORT1; cell type hepatocyte / liver.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA is proposed to bind the alt T allele more strongly than the ref G allele through a C/EBP-family bZIP motif. E07 is a bZIP DNA-binding specificity study retrieved by the rs12740374/CEBPA/CEBPB query; it supports C/EBP-family motif binding generally, but it does not by itself demonstrate allele-specific CEBPA binding at this exact site. QBiC-SELEX coverage for CEBPA is not_checked: no CEBPA screen row or qbic_tf_detail lookup is provided, so this is not an own-model or mapped QBiC-SELEX claim. | weak | [E07](#e07) |
| element | rs12740374 lies within dELS EH38E1374646, an enhancer-like cCRE with DNase and H3K27ac signal, making allele-dependent enhancer activity plausible. The ENCODE z-scores are maxima over biosamples, not liver-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | EH38E1374646 is proposed to regulate SORT1. SORT1 has the strongest L2G score at the locus and a liver sQTL credible set, and E08 shows that the alt T allele is associated with higher SORT1 expression in liver. This supports variant-to-SORT1 association but not direct enhancer-to-SORT1 physical regulation. | weak | [E05](#e05), [E08](#e08) |
| cell_type | The relevant cell type is hepatocyte/liver. CEBPA is highly expressed in the stated Hep3B2.1-7 context (141.33 TPM, rank 18 of 1626 TFs, 99.2th percentile), and rs12740374 has liver eQTL effects on SORT1 and other locus genes. | supported | [E08](#e08), [E09](#e09) |
| phenotype | In this chain, the protective T allele increases CEBPA-dependent SORT1 expression in liver and thereby lowers LDL cholesterol and MI risk. E04 lists G as the effect/risk allele in the strongest high-cholesterol and LDLC rows, and E08 shows T is associated with higher liver SORT1 expression. The causal step from CEBPA binding to SORT1 to LDL is not directly demonstrated by the provided evidence. | weak | [E04](#e04), [E05](#e05), [E08](#e08) |

Predictions: CEBPA ChIP, EMSA, or an allele-specific reporter shows stronger CEBPA binding to the T allele than to the G allele in Hep3B2.1-7 or primary hepatocytes.; CEBPA knockdown or CRISPRi reduces T-allele-dependent SORT1 enhancer activity and SORT1 expression in liver cells.; The T allele is associated with lower LDL cholesterol and lower MI risk, with SORT1 expression in the protective direction.

Falsified if: Allele-specific CEBPA binding at rs12740374 is absent in Hep3B2.1-7 or primary hepatocytes.; CEBPA perturbation does not alter T-allele-dependent SORT1 enhancer activity or SORT1 expression in liver cells.; SORT1 perturbation does not change LDL cholesterol or MI risk in the expected direction.

### 2. null_linked_or_no_TF_effect: Null: rs12740374 is a marker for a linked causal variant or has no TF-mediated allelic effect (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs12740374 in liver-relevant cells.; The association is explained by a linked causal variant or by a non-TF mechanism.; The G/T allele difference does not directly alter enhancer activity or target-gene expression.

Falsified if: Direct allele-specific TF binding at rs12740374 is demonstrated in liver cells and perturbation of that TF changes SORT1 or another causal gene.; Fine-mapping and functional assays show rs12740374 itself, not a linked variant, is causal.

### 3. CEBPA_alt_PSRC1_protective: CEBPA binds the protective T allele and acts through PSRC1 (p = 0.10)

TF CEBPA (stated coverage not_checked; registry own_model), alt allele binds more; element EH38E1374646 dELS enhancer; gene PSRC1; cell type hepatocyte / liver.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA is proposed to bind the alt T allele more strongly than the ref G allele through a C/EBP-family bZIP motif. E07 supports C/EBP-family DNA-binding specificity generally, but direct allele-specific CEBPA binding at rs12740374 is not shown. QBiC-SELEX coverage for CEBPA is not_checked; no CEBPA screen row or qbic_tf_detail lookup is provided. | weak | [E07](#e07) |
| element | rs12740374 lies within dELS EH38E1374646, an enhancer-like cCRE with DNase and H3K27ac signal, making allele-dependent enhancer activity plausible. The ENCODE z-scores are maxima over biosamples, not liver-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | This chain proposes that EH38E1374646 acts through PSRC1. PSRC1 is close to the variant and has L2G support, and E08 shows that the alt T allele is associated with higher PSRC1 expression in liver. The evidence does not establish PSRC1 as the target of this specific enhancer. | weak | [E05](#e05), [E08](#e08) |
| cell_type | The relevant cell type is hepatocyte/liver. CEBPA is highly expressed in Hep3B2.1-7, and rs12740374 has a liver eQTL for PSRC1. | supported | [E08](#e08), [E09](#e09) |
| phenotype | In this chain, the T allele increases PSRC1 expression in liver and, if PSRC1 is causal, contributes to lower LDL cholesterol and MI risk. E04 supports the locus-level association and E08 gives the T-to-higher-PSRC1 direction, but the causal direction from PSRC1 to LDL/MI is not established by the provided evidence. | weak | [E04](#e04), [E05](#e05), [E08](#e08) |

Predictions: Allele-specific CEBPA binding at the enhancer is detected in liver cells.; CEBPA perturbation changes PSRC1 expression or PSRC1 enhancer activity, with little or no effect on SORT1.; PSRC1 perturbation changes LDL cholesterol or MI risk in the expected direction.

Falsified if: Allele-specific CEBPA binding at rs12740374 is absent in liver cells.; CEBPA perturbation does not alter PSRC1 expression or PSRC1 enhancer activity in liver cells.; PSRC1 perturbation does not affect LDL cholesterol or MI risk in the expected direction.

### 4. CEBPA_alt_CELSR2_protective: CEBPA binds the protective T allele and acts through CELSR2 (p = 0.10)

TF CEBPA (stated coverage not_checked; registry own_model), alt allele binds more; element EH38E1374646 dELS enhancer; gene CELSR2; cell type liver or other lipid-relevant tissue.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA is proposed to bind the alt T allele more strongly than the ref G allele through a C/EBP-family bZIP motif. E07 supports C/EBP-family DNA-binding specificity generally, but direct allele-specific CEBPA binding at rs12740374 is not shown. QBiC-SELEX coverage for CEBPA is not_checked; no CEBPA screen row or qbic_tf_detail lookup is provided. | weak | [E07](#e07) |
| element | rs12740374 lies within dELS EH38E1374646, an enhancer-like cCRE with DNase and H3K27ac signal, making allele-dependent enhancer activity plausible. The ENCODE z-scores are maxima over biosamples, not liver-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | This chain proposes that EH38E1374646 acts through CELSR2 rather than SORT1. CELSR2 has strong L2G support and multiple QTL credible sets, and E08 shows that the alt T allele is associated with higher CELSR2 expression in liver. However, SORT1 has a slightly higher best L2G score than CELSR2, so the evidence does not establish CELSR2 as the target of this enhancer over SORT1. | weak | [E05](#e05), [E08](#e08) |
| cell_type | The relevant cell type is liver or another lipid-relevant tissue. CEBPA is highly expressed in Hep3B2.1-7, and rs12740374 has liver eQTL effects on CELSR2, but the strongest CELSR2 QTLs reported are not liver-specific. | weak | [E08](#e08), [E09](#e09) |
| phenotype | In this chain, the T allele increases CELSR2 expression in liver and, if CELSR2 is causal, contributes to lower LDL cholesterol and MI risk. E04 supports the locus-level association, and E08 gives the T-to-higher-CELSR2 direction, but the direction of any causal CELSR2 effect on LDL/MI is not established by the provided evidence. | weak | [E04](#e04), [E05](#e05), [E08](#e08) |

Predictions: Allele-specific CEBPA binding at the enhancer is detected in the relevant tissue.; CEBPA perturbation changes CELSR2 expression or CELSR2 enhancer activity, with little or no effect on SORT1.; CELSR2 perturbation changes LDL cholesterol or MI risk in the expected direction.

Falsified if: Allele-specific CEBPA binding at rs12740374 is absent in the relevant tissue.; CEBPA perturbation does not alter CELSR2 expression or CELSR2 enhancer activity in the relevant tissue.; CELSR2 perturbation does not affect LDL cholesterol or MI risk in the expected direction.

## Prediction matrix

| Test | Cost | Separates top two | CEBPA_alt_SORT1_protective | null_linked_or_no_TF_effect | CEBPA_alt_PSRC1_protective | CEBPA_alt_CELSR2_protective |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CEBPA binding by EMSA or ChIP using ref G and alt T oligos in Hep3B2.1-7 or primary hepatocytes | low | yes | Stronger CEBPA binding to T than G. | No allele-specific CEBPA binding at rs12740374. | Stronger CEBPA binding to T than G. | Stronger CEBPA binding to T than G. |
| CEBPA knockdown/CRISPRi plus allele-specific enhancer reporter or target-gene expression in Hep3B2.1-7 | medium | yes | CEBPA knockdown/CRISPRi reduces T-dependent SORT1 enhancer activity or SORT1 expression. | No CEBPA-dependent, allele-specific effect on SORT1, CELSR2, or PSRC1. | CEBPA knockdown/CRISPRi reduces T-dependent PSRC1 enhancer activity or PSRC1 expression, with little effect on SORT1. | CEBPA knockdown/CRISPRi reduces T-dependent CELSR2 enhancer activity or CELSR2 expression, with little effect on SORT1. |
| Liver eQTL/sQTL direction for SORT1, CELSR2, and PSRC1 | low | no | T is associated with higher SORT1 expression in liver. | An allelic expression effect may still be present if a linked variant is causal; this test does not by itself distinguish direct TF binding from linkage. | T is associated with higher PSRC1 expression in liver. | T is associated with higher CELSR2 expression in liver. |
| Allele-specific MPRA of EH38E1374646 ref G versus alt T in Hep3B2.1-7 | medium | yes | T increases EH38E1374646 enhancer activity, and the effect is CEBPA-motif dependent. | No allele-specific enhancer activity difference at rs12740374. | T increases EH38E1374646 enhancer activity, and the effect is CEBPA-motif dependent. | T increases EH38E1374646 enhancer activity, and the effect is CEBPA-motif dependent. |
| Perturb SORT1, CELSR2, and PSRC1 in hepatocyte models and measure LDL cholesterol or MI-relevant phenotypes | high | yes | SORT1 perturbation changes LDL cholesterol or MI risk; CELSR2/PSRC1 perturbation has weaker or no effect. | No target-gene perturbation gives the allele-consistent LDL/MI effect. | PSRC1 perturbation changes LDL cholesterol or MI risk; SORT1/CELSR2 perturbation has weaker or no effect. | CELSR2 perturbation changes LDL cholesterol or MI risk; SORT1/PSRC1 perturbation has weaker or no effect. |

## Next experiment

Allele-specific CEBPA binding EMSA/ChIP with rs12740374 ref G and alt T oligos in Hep3B2.1-7 or primary hepatocytes is the cheapest experiment that separates the top two chains: it tests the central CEBPA/T-allele binding claim of the main chain against the null.

## Investigate calls

- literature_search({"query": "rs12740374 CEBPA CEBPB allele-specific binding SORT1 liver"})
- eqtl_lookup({"tissue": "Liver"})
- tf_expression({"tf": "CEBPA", "context": "DepMap:ACH-000625"})

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

<a id="e07"></a>**E07** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20CEBPA%20CEBPB%20allele-specific%20binding%20SORT1%20liver&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T01:39:10+00:00)

> Europe PMC: 1 hits for 'rs12740374 CEBPA CEBPB allele-specific binding SORT1 liver'; top 1 with PMIDs:
> PMID 28186491 (2017): Combinatorial bZIP dimers display complex DNA-binding specificity landscapes.

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_109274968_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:36+00:00)

> 5 significant GTEx v8 single-tissue eQTLs for chr1_109274968_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).
> SORT1 in Liver: NES +1.27, p 3.1e-54
> PSRC1 in Liver: NES +1.24, p 1.1e-37
> CELSR2 in Liver: NES +1.04, p 9.4e-34
> ATXN7L2 in Liver: NES +0.40, p 5.9e-07
> SYPL2 in Liver: NES +0.50, p 1.2e-06

<a id="e09"></a>**E09** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> CEBPA in DepMap line ACH-000625: 141.33 TPM, rank 18 of 1626 TFs (1 = highest); this context is at the 99.2th percentile of CEBPA across all DepMap lines.
