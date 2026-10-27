# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.66 over 8 model calls; 245 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen

239 of 997 models pass the gate. Top groups: C2H2 ZF, 1 model (best ZNF43, z 35.83); bZIP, 1 model (best CEBPG, z 26.76); C2H2 ZF, 1 model (best ZNF696, z -24.85); RFX, 4 models (best RFX4, z 23.16); bZIP, 3 models (best CEBPB, z 22.81).

## Ranked chains

### 1. H1: Alt (T) allele creates a C/EBP site occupied by CEBPA in hepatocytes, raising SORT1 and lowering LDL-C and MI risk (p = 0.72)

TF CEBPA (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1374646 (dELS distal enhancer, chr1:109274794-109275142, within CELSR2 3'UTR region); gene SORT1; cell type hepatocyte (Hep 3B2.1-7 / HepG2 / primary human hepatocyte).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The T allele strongly raises predicted C/EBP affinity (group G035: CEBPA z 22.63, CEBPB z 22.81, effect +2.33; site strength 87.0th -> 99.8th percentile), and the site is directly covered by an ENCODE CEBPA ChIP-seq peak in HepG2 (ENCSR142IGM); published work states that rs12740374 creates a C/EBP binding site. CEBPA is chosen within the shared-specificity group on the combination of ChIP occupancy in a liver line and much higher expression in the hepatocyte context (141.33 TPM vs CEBPB 4.05, CEBPE 0.0); the QBiC model alone cannot separate CEBPA from CEBPB. | supported | [E12](#e12), [E18](#e18), [E20b](#e20b), [E07](#e07) |
| element | The variant lies in an active distal enhancer-like cCRE (EH38E1374646, DNase z 4.9, H3K27ac z 4.8; Ensembl enhancer ENSR1_CDSQQ); the cCRE z-scores are maxima across biosamples, but the HepG2 CEBPA peak shows the element is bound in a liver cell line. | supported | [E03](#e03), [E01](#e01), [E18](#e18) |
| gene | The element acts on SORT1: the variant is a strong liver SORT1 eQTL (NES +1.27, p 3.1e-54, alt T raising expression; PSRC1 +1.24, CELSR2 +1.04), SORT1 is the top fine-mapped gene (L2G 0.99), and hepatocyte/humanized-mouse work shows the minor allele sequence enhances SORT1 expression. SORT1 is not fully isolated from CELSR2/PSRC1, which are co-regulated in the same direction. | supported | [E19](#e19), [E05](#e05), [E20a](#e20a), [E20b](#e20b) |
| cell_type | The effect is hepatocyte-restricted: the eQTL is observed in liver, the CEBPA peak is in HepG2, and CEBPA is the dominant, highly expressed liver C/EBP in the expression context used. | weak | [E19](#e19), [E18](#e18), [E12](#e12) |
| phenotype | Alt T raises hepatic SORT1 and is the non-risk allele: GWAS lists G as the cholesterol-raising/risk allele (freq ~0.78) for high cholesterol and LDL-C, and the locus colocalizes with myocardial infarction (PH4 0.855). Direction is therefore T -> more SORT1 -> lower LDL-C -> lower MI risk. | supported | [E04](#e04), [E06b](#e06b), [E20a](#e20a) |

Predictions: Allele-specific CEBPA ChIP (or EMSA with C/EBP supershift) in hepatocytes shows T-preferential occupancy at chr1:109274968; CEBPA knockdown in hepatocytes flattens the G-vs-T reporter difference more than knockdown of CEBPG/CEBPD; Base-editing T->G at the endogenous site lowers SORT1 (and to a lesser degree PSRC1/CELSR2) in hepatocytes; T allele carriers show higher liver SORT1 and lower LDL-C

Falsified if: Allele-specific CEBPA ChIP/EMSA shows no preference for T at this site; Reporter allelic difference persists after depletion of CEBPA while being lost on depletion of a non-C/EBP factor; Endogenous editing of the site changes CELSR2/PSRC1 but leaves SORT1 unchanged

### 2. H5: Null: no TF-mediated effect of this variant itself (causal signal carried by a linked variant) (p = 0.11)

Null chain: no TF-mediated effect of this variant.

Predictions: Allelic reporter or base-edit assays show no difference between G and T in hepatocytes; The liver eQTL and GWAS signals are driven by a linked variant such as rs646776 after fine resolution; No allele-specific TF occupancy at chr1:109274968 in hepatocyte ChIP

Falsified if: Reporter or endogenous base-editing shows a reproducible allelic effect on enhancer activity or SORT1 expression; Allele-specific ChIP signal is detected at the site

### 3. H2: Same created C/EBP site, but CEBPG (or CEBPD) rather than CEBPA is the operative family member (p = 0.10)

TF CEBPG (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1374646 distal enhancer; gene SORT1; cell type hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Independent bZIP models show large alt-favoring changes for CEBPG (z 26.76, effect +2.32, 64.5th -> 99.4th percentile) and CEBPD (z 18.08), consistent with creation of a C/EBP half-site; CEBPG is picked over CEBPD on expression (46.37 vs 5.40 TPM). No ChIP evidence for CEBPG/CEBPD at this site is cited, whereas CEBPA is ChIP-supported, so this chain is the weaker version of the same motif class. | weak | [E09](#e09), [E16](#e16), [E20b](#e20b) |
| element | The variant sits in an active distal enhancer-like cCRE that is bound by C/EBP-family protein in a liver line. | weak | [E03](#e03), [E18](#e18) |
| gene | Liver eQTL shows alt T raises SORT1 (NES +1.27), with SORT1 the top fine-mapped gene (L2G 0.99). | supported | [E19](#e19), [E05](#e05) |
| cell_type | CEBPG is abundantly expressed in the hepatocyte context (46.37 TPM) and could heterodimerize at the created site. | weak | [E09](#e09) |
| phenotype | Higher hepatic SORT1 on the T allele lowers LDL-C; G is the cholesterol-raising allele and the locus colocalizes with MI. | supported | [E04](#e04), [E06b](#e06b), [E20a](#e20a) |

Predictions: CEBPG or CEBPD ChIP shows allele-specific signal at chr1:109274968 in hepatocytes while CEBPA allelic signal is weak; CEBPG knockdown, not CEBPA knockdown, abolishes the allelic reporter difference; CEBPA ChIP peak at the site reflects heterodimer capture rather than CEBPA-driven activation

Falsified if: CEBPA depletion alone abolishes the allelic effect; No CEBPG/CEBPD occupancy is detectable at this enhancer in hepatocytes

### 4. H3: Alt allele creates a high-affinity ZNF43 site that modulates enhancer output (p = 0.04)

TF ZNF43 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1374646 distal enhancer; gene SORT1; cell type hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The largest-magnitude passing QBiC model at this site is ZNF43 (own model, z 35.83, effect +3.43; 93.6th -> 99.9th percentile), a single-member C2H2 ZF group with no within-group ambiguity. This is an in-vitro prediction only; no ChIP or EMSA evidence is cited. | weak | [E08](#e08) |
| element | The site lies in an active distal enhancer cCRE where a KRAB-ZF could modulate activity; this is speculative given no occupancy data. | weak | [E03](#e03) |
| gene | The variant is a strong liver eQTL for SORT1 (alt raising, NES +1.27) with SORT1 the top fine-mapped gene. | supported | [E19](#e19), [E05](#e05) |
| cell_type | ZNF43 is expressed only modestly in the hepatocyte context (8.74 TPM). | weak | [E08](#e08) |
| phenotype | Changed hepatic SORT1 shifts LDL-C and MI risk at 1p13; under this chain the alt allele would still need to raise SORT1 to match the eQTL, implying activation rather than repression. | weak | [E04](#e04), [E19](#e19), [E06b](#e06b) |

Predictions: ZNF43 ChIP shows allele-preferential binding at this enhancer in hepatocytes; ZNF43 knockout changes SORT1 expression in an allele-dependent manner independent of C/EBP depletion; If ZNF43 acts as a repressor, the alt allele lowers reporter activity, contrary to the observed liver eQTL direction

Falsified if: No ZNF43 occupancy at the locus in hepatocyte ChIP data; Allelic enhancer activity is unchanged by ZNF43 loss; C/EBP depletion fully removes the allelic effect

### 5. H4: Alt allele strengthens an RFX5-family site acting on CELSR2 (p = 0.03)

TF RFX5 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1374646 distal enhancer; gene CELSR2; cell type hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | RFX group G094 passes with an alt-favoring effect (RFX7 z 18.73, RFX5 z 11.53; 84.8th -> 99.0th percentile); RFX5 is chosen over RFX7 on expression (41.14 vs 9.96 TPM), while group G028 is driven by RFX4, which is not expressed. No ChIP or EMSA support is cited, and RFX5's known biology (MHC class II) gives no lipid rationale. | weak | [E15](#e15), [E11](#e11) |
| element | The variant lies in an active distal enhancer-like cCRE; no RFX-specific occupancy evidence exists. | weak | [E03](#e03) |
| gene | The variant is in the CELSR2 3'UTR/gene body, is a liver CELSR2 eQTL (NES +1.04, p 9.4e-34), and CELSR2 has high L2G support (0.98), though SORT1 is stronger on both eQTL effect size and L2G. | weak | [E01](#e01), [E19](#e19), [E05](#e05) |
| cell_type | RFX5 is well expressed in the hepatocyte context (41.14 TPM). | weak | [E15](#e15) |
| phenotype | Altered hepatic CELSR2 expression would contribute to the LDL-C and MI association at 1p13. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: RFX5 ChIP shows allele-specific binding at the site in hepatocytes; Perturbing the element changes CELSR2 more than SORT1; RFX5 depletion flattens the allelic reporter difference while C/EBP depletion does not

Falsified if: Element perturbation changes SORT1 with little CELSR2 effect; No RFX occupancy at the site; C/EBP depletion abolishes the allelic effect

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ENCODE CEBPA ChIP-seq peak overlap in HepG2 at chr1:109274968 (E18) | existing data | no | Peak present (observed) - supports CEBPA occupancy | Peak may exist but no allelic difference | Peak may be present via heterodimer; CEBPA not required | CEBPA peak irrelevant; ZNF43 occupancy expected instead | CEBPA peak irrelevant; RFX occupancy expected |
| GTEx liver eQTL direction for SORT1/CELSR2/PSRC1 (E19) | existing data | no | Alt T raises SORT1 most (observed, NES +1.27) | eQTL explained by linked variant | Same direction predicted | Direction ambiguous; repressive ZNF43 predicts alt-lowering | CELSR2 should dominate over SORT1 |
| Query existing hepatocyte/HepG2 ChIP-seq (ENCODE, ChIP-Atlas) for CEBPG and CEBPD peaks at chr1:109274968 | existing data | yes | No or weak CEBPG/CEBPD peak while CEBPA peak is present | Peaks uninformative; no allelic effect | CEBPG (or CEBPD) peak present at the site | No C/EBP peaks required | No C/EBP peaks required |
| Allele-specific EMSA with HepG2 nuclear extract plus CEBPA- vs CEBPG-specific antibody supershift | low | yes | T-specific complex supershifted by anti-CEBPA | No allele-specific complex | T-specific complex supershifted by anti-CEBPG/CEBPD | No C/EBP supershift; different complex | No C/EBP supershift |
| siRNA knockdown of CEBPA vs CEBPG in hepatocytes with G/T luciferase reporter | medium | yes | CEBPA knockdown abolishes allelic difference | No allelic difference to begin with | CEBPG knockdown abolishes allelic difference | Neither knockdown changes the allelic difference | Neither knockdown changes the allelic difference |
| CRISPR base-edit T->G at endogenous site in hepatocytes, measure SORT1/CELSR2/PSRC1 | high | no | SORT1 falls sharply | No expression change | SORT1 falls sharply (same) | Effect present but C/EBP-independent | CELSR2 falls more than SORT1 |
| ZNF43 and RFX5 ChIP-seq at the locus in hepatocytes | medium | no | No peaks expected | No allele-specific peaks | No peaks expected | ZNF43 peak with T-preference | RFX5 peak with T-preference |

## Next experiment

Mine existing hepatocyte/HepG2 ChIP-seq (ENCODE plus ChIP-Atlas) for CEBPG and CEBPD peaks overlapping chr1:109274968 and compare with the known CEBPA peak (E18); this costs nothing and is the cheapest test that separates H1 (CEBPA) from H2 (CEBPG/CEBPD). If ambiguous, follow with the low-cost allele-specific EMSA supershift using CEBPA- and CEBPG-specific antibodies.

## Investigate calls

- chip_peaks({"tf": "CEBPA", "biosample": "HepG2"})
- eqtl_lookup({"tissue": "Liver"})
- literature_search({"query": "rs12740374 C/EBP SORT1 hepatocyte allele-specific enhancer"})

## Flags

- none

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

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 42019808 (https://europepmc.org/article/MED/42019808; retrieved 2026-10-25T17:29:12+00:00)

> Colocalization identified shared signals at the PSRC1-CELSR2-SORT1 locus, with lead variants rs12740347 and rs646776.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 40922271 (https://europepmc.org/article/MED/40922271; retrieved 2026-10-25T17:29:12+00:00)

> The co-localization analysis, based on two-sample Mendelian randomization results, revealed that single nucleotide polymorphism (SNP) rs12740374 (PH4 = 0.855) was causally associated with MI and a balanced diet(I eat all of the above), while SNP rs7528419 (PH4 = 0.716) was causally associated with CHD and a balanced diet.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 39858645 (https://europepmc.org/article/MED/39858645; retrieved 2026-10-25T17:29:12+00:00)

> GWASs and sequencing studies have identified key genetic variations associated with CAD, including JCAD/KIAA1462, GUCY1A3, PCSK9, and SORT1, which regulate inflammation, lipid metabolism, and vascular function.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:109274968:G>T: 997 models scored, 239 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 182 CIS-BP groups. Expression context: DepMap line ACH-000625. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 44 (GCM, 2 models z -44.12, Homeodomain, 3 models z -27.46, C2H2 ZF, 1 model z 21.63, Homeodomain, 2 models z -17.61, bHLH, 1 model z -14.43). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G510 (C2H2 ZF, 1 model): best model ZNF43_FL_GC40NTATAGG_YWRA_jolma2025_0_3_7mer (own model of ZNF43), z 35.83, effect 3.431 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF43 z 35.83. TFs this group covers (own and CIS-BP-mapped models): ZNF43 8.74 TPM; best model's site strength: ref 93.6th, alt 99.9th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G143 (bZIP, 1 model): best model CEBPG_eDBD_TACTTT40NTCT_KN_yin2017_0_4_7mer (own model of CEBPG), z 26.76, effect 2.321 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CEBPG z 26.76. TFs this group covers (own and CIS-BP-mapped models): CEBPG 46.37 TPM; best model's site strength: ref 64.5th, alt 99.4th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G570 (C2H2 ZF, 1 model): best model ZNF696_FL_AG40NTGGCTA_YWSA_jolma2025_0_2_7mer (own model of ZNF696), z -24.85, effect -0.713 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF696 z -24.85. TFs this group covers (own and CIS-BP-mapped models): ZNF696 5.1 TPM; best model's site strength: ref 99.8th, alt 88.3th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G028 (RFX, 4 models): best model RFX4_eDBD_TACTCG40NCAA_KAN_yin2017_0_3_7mer (own model of RFX4), z 23.16, effect 1.235 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: RFX4 z 23.16, RFX1 z 16.27, RFX2 z 4.8. TFs this group covers (own and CIS-BP-mapped models): RFX2 4.97 TPM, RFX1 4.13 TPM, RFX3 2.13 TPM, RFX6 0.35 TPM, RFX4 0.0 TPM; best model's site strength: ref 95.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G035 (bZIP, 3 models): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (own model of CEBPB), z 22.81, effect 2.331 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: CEBPB z 22.81, CEBPA z 22.63, CEBPE z 11.28. TFs this group covers (own and CIS-BP-mapped models): CEBPA 141.33 TPM, CEBPB 4.05 TPM, CEBPE 0.0 TPM; best model's site strength: ref 87.0th, alt 99.8th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (own model of TFAP2E), z -21.21, effect -0.98 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TFAP2E z -21.21, TFAP2B z -18.18, TFAP2A z -13.22, TFAP2C z -12.55. TFs this group covers (own and CIS-BP-mapped models): TFAP2A 7.65 TPM, TFAP2E 2.06 TPM, TFAP2B 0.04 TPM, TFAP2C 0.01 TPM, TFAP2D 0.0 TPM; best model's site strength: ref 99.8th, alt 98.8th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G491 (C2H2 ZF, 1 model): best model ZNF345_eDBD_TGTAAG40NACT_KT_yin2017_0_3_7mer (own model of ZNF345), z 20.62, effect 0.964 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF345 z 20.62. TFs this group covers (own and CIS-BP-mapped models): ZNF345 1.64 TPM; best model's site strength: ref 97.7th, alt 99.9th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G094 (RFX, 2 models): best model RFX7_eDBD_TCGTCC40NGCC_KT_yin2017_0_4_7mer (own model of RFX7), z 18.73, effect 0.788 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: RFX7 z 18.73, RFX5 z 11.53. TFs this group covers (own and CIS-BP-mapped models): RFX5 41.14 TPM, RFX7 9.96 TPM; best model's site strength: ref 84.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G142 (bZIP, 1 model): best model CEBPD_NA_TAATGA20NCG_ESY_yang2017_0_2_7mer (own model of CEBPD), z 18.08, effect 1.253 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CEBPD z 18.08. TFs this group covers (own and CIS-BP-mapped models): CEBPD 5.4 TPM; best model's site strength: ref 88.1th, alt 99.1th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G012 (bZIP, 6 models): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (own model of MAFG), z 16.34, effect 0.625 (alt binds more); 5 passing models (5 with the best model's sign). Passing members: MAFG z 16.34, MAF z 11.17, MAFK z 10.91, NRL z 10.31, MAFA z 9.36. TFs this group covers (own and CIS-BP-mapped models): MAFK 39.41 TPM, MAFG 19.11 TPM, NRL 0.83 TPM, MAF 0.52 TPM, MAFB 0.47 TPM, MAFA 0.04 TPM; best model's site strength: ref 94.7th, alt 97.4th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:30:36+00:00)

> 1 ENCODE CEBPA ChIP-seq peaks contain chr1:109274968:G>T in biosamples matching 'HepG2': biosamples HepG2; experiments ENCSR142IGM.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_109274968_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:36+00:00)

> 5 significant GTEx v8 single-tissue eQTLs for chr1_109274968_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).
> SORT1 in Liver: NES +1.27, p 3.1e-54
> PSRC1 in Liver: NES +1.24, p 1.1e-37
> CELSR2 in Liver: NES +1.04, p 9.4e-34
> ATXN7L2 in Liver: NES +0.40, p 5.9e-07
> SYPL2 in Liver: NES +0.50, p 1.2e-06

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20C/EBP%20SORT1%20hepatocyte%20allele-specific%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T18:06:40+00:00)

> Europe PMC: 9 hits for 'rs12740374 C/EBP SORT1 hepatocyte allele-specific enhancer'; top 8 with PMIDs:
> PMID 40250421 (2025): Characterization of non-coding variants associated with transcription-factor binding through ATAC-seq-defined footprint QTLs in liver.
> PMID 34784266 (2022): Emerging roles of sortilin in affecting the metabolism of glucose and lipid profiles.
> PMID 35724703 (2022): Sorting through the extensive and confusing roles of sortilin in metabolic disease.
> PMID 29097363 (2018): Interrogation of the Atherosclerosis-Associated <i>SORT1</i> (Sortilin 1) Locus With Primary Human Hepatocytes, Induced Pluripotent Stem Cell-Hepatocytes, and Locus-Humanized Mice.
> PMID 29915816 (2018): From Genotype to Phenotype: A Primer on the Functional Follow-up of Genome-Wide Association Studies in Cardiovascular Disease.
> PMID 24997396 (2014): Strategies to fine-map genetic associations with lipid levels by combining epigenomic annotations and liver-specific transcription profiles.
> PMID 20686566 (2010): From noncoding variant to phenotype via SORT1 at the 1p13 cholesterol locus.
> PMID 25473428 (2014): Approaches for establishing the function of regulatory genetic variants involved in disease.

<a id="e20a"></a>**E20a** literature_search, Europe PMC abstract, PMID 29097363 (https://europepmc.org/article/MED/29097363; retrieved 2026-10-25T18:06:40+00:00)

> The rs12740374 minor allele sequence enhances SORT1 expression in hepatocytes.

<a id="e20b"></a>**E20b** literature_search, Europe PMC abstract, PMID 20686566 (https://europepmc.org/article/MED/20686566; retrieved 2026-10-25T18:06:40+00:00)

> Here we show through a series of studies in human cohorts and human-derived hepatocytes that a common noncoding polymorphism at the 1p13 locus, rs12740374, creates a C/EBP (CCAAT/enhancer binding protein) transcription factor binding site and alters the hepatic expression of the SORT1 gene.

<a id="e20c"></a>**E20c** literature_search, Europe PMC abstract, PMID 24997396 (https://europepmc.org/article/MED/24997396; retrieved 2026-10-25T18:06:40+00:00)

> This method recognized the known SORT1 rs12740374 regulatory SNP associated with LDL-cholesterol, and highlighted candidate functional SNPs at 15 additional lipid loci.
