# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 215 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. chain1_CEBPB_SORT1_hepatocyte: CEBPB binds the T allele and increases SORT1 in hepatocytes (p = 0.48)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element distal enhancer; gene SORT1; cell type liver, plausibly hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB is the best-supported C/EBP-family candidate: CEBPB ChIP-seq peaks contain this variant in several non-liver ENCODE biosamples (E07), and rs12740374 is a known SORT1 regulatory SNP (E09a). The alt T allele is hypothesized to bind CEBPB more strongly because T increases SORT1 expression (E08), but direct allele-specific CEBPB binding is not shown. QBiC-SELEX coverage for CEBPB is not_checked because no QBiC-SELEX row or qbic_tf_detail lookup was provided. | weak | [E07](#e07), [E08](#e08), [E09a](#e09a) |
| element | The variant lies in the distal enhancer-like cCRE EH38E1374646, near CELSR2, PSRC1, and MYBPHL. | supported | [E01](#e01), [E03](#e03) |
| gene | SORT1 is the strongest L2G gene at this locus and has a liver eQTL in which the T allele increases expression. However, SORT1 is 123 kb away and is not listed among E03 nearby genes, so direct enhancer-SORT1 regulation is not demonstrated. | weak | [E02](#e02), [E03](#e03), [E05](#e05), [E08](#e08) |
| cell_type | The relevant context is liver, plausibly hepatocyte: a liver SORT1 eQTL is present (E08), a liver SORT1 sQTL credible set is reported (E05), and Hep 3B2.1-7 is the provided expression context. No Hep3B-specific ChIP evidence is available. | weak | [E05](#e05), [E08](#e08) |
| phenotype | The G allele is the risk allele for higher LDL/high cholesterol in most GWAS entries (E04), so the T allele is protective; T also increases liver SORT1 expression (E08). The causal step from SORT1 to LDL/MI is not directly shown by these evidence IDs. | weak | [E04](#e04), [E08](#e08) |

Predictions: Allele-specific CEBPB binding is stronger on T than G at the rs12740374-containing enhancer in liver-derived cells.; CEBPB knockdown reduces the T-allele-dependent increase in SORT1 expression.; The T allele increases SORT1 expression in liver and is associated with lower LDL cholesterol.

Falsified if: Allele-specific CEBPB binding at rs12740374 is absent in liver-derived cells.; The T allele does not increase SORT1 expression in liver or hepatocytes.; Conditioning on rs12740374 genotype abolishes the liver SORT1 eQTL signal.

### 2. null_no_tf_mediated_effect: No TF-mediated effect of rs12740374; linked or passenger association (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific CEBPB binding at rs12740374 in liver-derived cells.; The GWAS signal is explained by a linked causal variant or by a non-TF-mediated mechanism.; SORT1, CELSR2, and PSRC1 eQTLs are not allelic effects of rs12740374 itself after conditioning on linked variants.

Falsified if: Allele-specific C/EBP-family binding at rs12740374 is demonstrated in a relevant cell type.; An allele-specific reporter assay shows that rs12740374 itself changes enhancer activity.; Conditioning on rs12740374 genotype abolishes the SORT1 or CELSR2 liver eQTL signal.

### 3. chain3_CEBPB_CELSR2: CEBPB binds the T allele and alters CELSR2 (p = 0.14)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element distal enhancer; gene CELSR2; cell type liver or muscle.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB is the candidate C/EBP-family factor: CEBPB ChIP-seq peaks contain this variant in non-liver ENCODE biosamples (E07), and rs12740374 is a known regulatory SNP at this locus (E09a). The alt T allele is hypothesized to bind CEBPB more strongly, but allele-specific CEBPB binding is not shown. QBiC-SELEX coverage for CEBPB is not_checked. | weak | [E07](#e07), [E09a](#e09a) |
| element | The variant lies in the distal enhancer-like cCRE EH38E1374646, with CELSR2 among nearby genes. | supported | [E01](#e01), [E03](#e03) |
| gene | CELSR2 has strong L2G support and a liver eQTL in which the T allele increases expression, but direct regulation of CELSR2 by EH38E1374646 is not demonstrated. | weak | [E03](#e03), [E05](#e05), [E08](#e08) |
| cell_type | CELSR2 QTL credible sets include liver and muscle contexts, but no cell-type-specific enhancer assay establishes which cell type mediates the effect. | weak | [E05](#e05), [E08](#e08) |
| phenotype | The T allele is protective for LDL/high cholesterol in most GWAS entries (E04), and T increases liver CELSR2 expression (E08); however, a causal CELSR2-to-lipid effect is not shown by these evidence IDs. | weak | [E04](#e04), [E08](#e08) |

Predictions: The T allele changes CELSR2 expression in liver or muscle.; CEBPB binding at the element is allele-specific and CELSR2-linked.; CELSR2 expression correlates with LDL cholesterol independently of SORT1.

Falsified if: The T allele does not change CELSR2 expression in liver or muscle.; No allele-specific CEBPB binding is observed at the element.; The SORT1 eQTL fully explains the lipid association after conditioning on SORT1 expression.

### 4. chain4_CEBPB_PSRC1: CEBPB binds the T allele and alters PSRC1 (p = 0.08)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element distal enhancer; gene PSRC1; cell type liver, pancreas, or monocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB is the candidate C/EBP-family factor based on CEBPB ChIP-seq peaks containing this variant in non-liver biosamples (E07) and the known regulatory status of rs12740374 (E09a). The alt T allele is hypothesized to bind CEBPB more strongly, but allele-specific binding is not shown. QBiC-SELEX coverage for CEBPB is not_checked. | weak | [E07](#e07), [E09a](#e09a) |
| element | The variant lies in the distal enhancer-like cCRE EH38E1374646, with PSRC1 among nearby genes. | supported | [E01](#e01), [E03](#e03) |
| gene | PSRC1 has eQTL credible-set support and a liver eQTL in which the T allele increases expression, but the credible-set PIPs are weaker than for SORT1/CELSR2 and direct enhancer-PSRC1 regulation is not shown. | weak | [E03](#e03), [E05](#e05), [E08](#e08) |
| cell_type | PSRC1 QTL signals are reported in pancreas and monocyte contexts, and a liver eQTL is present (E08); no hepatocyte-specific enhancer assay is available. | weak | [E05](#e05), [E08](#e08) |
| phenotype | The T allele is protective for LDL/high cholesterol in most GWAS entries (E04), and T increases liver PSRC1 expression (E08); however, a causal PSRC1-to-lipid effect is not shown. | weak | [E04](#e04), [E08](#e08) |

Predictions: The T allele changes PSRC1 expression in a relevant tissue.; PSRC1 eQTL and lipid GWAS signals colocalize.; CEBPB binding at the element is allele-specific and PSRC1-linked.

Falsified if: PSRC1 expression is not affected by rs12740374 in any relevant tissue.; PSRC1 eQTL credible sets do not colocalize with the lipid GWAS signal.; No allele-specific CEBPB binding is observed at the element.

## Prediction matrix

| Test | Cost | Separates top two | chain1_CEBPB_SORT1_hepatocyte | null_no_tf_mediated_effect | chain3_CEBPB_CELSR2 | chain4_CEBPB_PSRC1 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CEBPB ChIP-qPCR or EMSA at rs12740374 in Hep 3B2.1-7 or primary hepatocytes | low | yes | Stronger CEBPB binding on T than G. | No allele-specific CEBPB binding at rs12740374. | Stronger CEBPB binding on T than G. | Stronger CEBPB binding on T than G. |
| Liver eQTL lookup and conditional fine-mapping for SORT1, CELSR2, and PSRC1 | low | yes | T allele increases SORT1 in liver; rs12740374 remains associated after conditioning on linked variants. | Variant-gene association is explained by a linked variant or is not specific to rs12740374. | T allele increases CELSR2 in liver or muscle. | T allele increases PSRC1 in a relevant tissue. |
| Literature search for rs12740374 CEBPB allele-specific reporter or EMSA evidence | low | yes | Literature or reporter evidence supports allele-specific CEBPB binding and SORT1 regulation at rs12740374. | No direct allele-specific CEBPB reporter evidence at rs12740374. | Literature supports CEBPB binding but not CELSR2 as the primary target. | Literature supports CEBPB binding but not PSRC1 as the primary target. |
| CRISPRi/dCas9 perturbation of EH38E1374646 followed by SORT1, CELSR2, and PSRC1 expression in Hep 3B2.1-7 | high | yes | CRISPRi at EH38E1374646 reduces SORT1 expression in hepatocytes. | CRISPRi at EH38E1374646 does not change SORT1, CELSR2, or PSRC1 expression. | CRISPRi at EH38E1374646 changes CELSR2 expression. | CRISPRi at EH38E1374646 changes PSRC1 expression. |
| CEBPB knockdown plus rs12740374 G/T reporter assay in Hep 3B2.1-7 | high | yes | CEBPB knockdown reduces T-allele-dependent SORT1 enhancer activity. | CEBPB knockdown does not alter allele-dependent enhancer activity. | CEBPB knockdown reduces T-allele-dependent CELSR2 enhancer activity. | CEBPB knockdown reduces T-allele-dependent PSRC1 enhancer activity. |

## Next experiment

Allele-specific CEBPB ChIP-qPCR or EMSA at rs12740374 in Hep 3B2.1-7 or primary hepatocytes: chain1 predicts stronger CEBPB binding on T than G, while the null predicts no allele-specific CEBPB binding.

## Investigate calls

- chip_peaks({"tf": "CEBPB", "biosample": "liver"})
- eqtl_lookup({"tissue": "Liver"})
- literature_search({"query": "rs12740374 CEBPB SORT1 allele-specific reporter"})

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

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T22:29:03+00:00)

> No ENCODE CEBPB ChIP-seq peak contains chr1:109274968:G>T in biosamples matching 'liver'. Absence can also mean no CEBPB experiment in that biosample. In other biosamples, 4 CEBPB peaks do contain the variant: A549, HeLa-S3, IMR-90, MCF-7 (experiments ENCSR000BSR, ENCSR000EDA, ENCSR000EFM, ENCSR752AQK).

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_109274968_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:36+00:00)

> 5 significant GTEx v8 single-tissue eQTLs for chr1_109274968_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).
> SORT1 in Liver: NES +1.27, p 3.1e-54
> PSRC1 in Liver: NES +1.24, p 1.1e-37
> CELSR2 in Liver: NES +1.04, p 9.4e-34
> ATXN7L2 in Liver: NES +0.40, p 5.9e-07
> SYPL2 in Liver: NES +0.50, p 1.2e-06

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20CEBPB%20SORT1%20allele-specific%20reporter&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:33:26+00:00)

> Europe PMC: 2 hits for 'rs12740374 CEBPB SORT1 allele-specific reporter'; top 2 with PMIDs:
> PMID 24997396 (2014): Strategies to fine-map genetic associations with lipid levels by combining epigenomic annotations and liver-specific transcription profiles.
> PMID 25835000 (2015): Lipid-induced epigenomic changes in human macrophages identify a coronary artery disease-associated variant that regulates PPAP2B Expression through Altered C/EBP-beta binding.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 24997396 (https://europepmc.org/article/MED/24997396; retrieved 2026-10-26T00:33:26+00:00)

> This method recognized the known SORT1 rs12740374 regulatory SNP associated with LDL-cholesterol, and highlighted candidate functional SNPs at 15 additional lipid loci.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 25835000 (https://europepmc.org/article/MED/25835000; retrieved 2026-10-26T00:33:26+00:00)

> OxLDL-regulated enhancers were enriched for several transcription factors including C/EBP-beta, which has no previously documented role in foam cell formation.

<a id="e09c"></a>**E09c** literature_search, Europe PMC abstract, PMID 25835000 (https://europepmc.org/article/MED/25835000; retrieved 2026-10-26T00:33:26+00:00)

> OxLDL increased C/EBP beta binding to this site and C/EBP beta binding and enhancer activity were stronger with the protective A allele of rs72664324.
