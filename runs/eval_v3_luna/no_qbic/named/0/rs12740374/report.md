# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 151 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H1: Candidate CEBPA-mediated effect on SORT1 (p = 0.48)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646; gene SORT1; cell type Liver-cell context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA is among the bound, expressed TFs reported at this site in the matching HepG2 context. I select it as a candidate, not as a proven causal TF: the evidence does not distinguish it from FOXA1, FOXA2, or other occupied factors, and the literature search returned no relevant hits. This chain hypothesizes stronger binding to T than G; no allele-specific occupancy or QBiC-SELEX result establishing that direction is supplied. | weak | [E04](#e04), [E19](#e19) |
| element | The variant lies within the enhancer-like cCRE EH38E1374646; its reported activity scores are maxima across biosamples and do not establish activity in this specific liver-cell context. | supported | [E03](#e03) |
| gene | SORT1 is the leading candidate target based on strong locus-to-gene scores and a positive T-allele liver eQTL. These data do not directly connect EH38E1374646 to SORT1. | weak | [E16](#e16), [E17](#e17) |
| cell_type | A liver-cell context is plausible because CEBPA occupancy is reported in HepG2 and the SORT1 eQTL is in bulk liver; neither establishes a hepatocyte-specific mechanism. | weak | [E04](#e04), [E17](#e17) |
| phenotype | This chain predicts that a T-associated increase in SORT1 contributes to lipid-trait effects. Several associations report G as the high-cholesterol risk allele, but the supplied associations are not entirely directionally uniform, and they do not establish a CEBPA-to-SORT1 causal path. The literature quote concerns the hepatic expression of the gene cluster collectively, not SORT1 alone. | weak | [E15](#e15), [E17](#e17), [E18b](#e18b) |

Predictions: In a relevant liver-cell model, allele-specific CEBPA occupancy should be greater on T than G.; A G-to-T edit should increase SORT1 expression, and reducing CEBPA should diminish that allele-dependent increase.

Falsified if: A suitably powered allele-specific assay finds no greater CEBPA occupancy on T, or finds greater occupancy on G.; Isogenic editing produces no allele-dependent SORT1 change, or the change is unaffected by CEBPA perturbation.

### 2. H4: Null: no TF-mediated effect of rs12740374 (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: There will be no reproducible allele-dependent occupancy by the candidate TFs that explains a cis-regulatory effect of this nucleotide.; The strong association and eQTL evidence may reflect another mechanism or may not establish a TF-mediated causal path through this variant.

Falsified if: Isogenic editing demonstrates an allele-dependent regulatory effect that depends on a specific TF and changes a relevant target gene's expression.

### 3. H2: Candidate FOXA1-mediated effect on SORT1 (p = 0.13)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646; gene SORT1; cell type Liver-cell context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is occupied at the variant and expressed in the stated cell line, making it a plausible candidate. The evidence does not show that FOXA1 binds T more strongly than G; greater T binding is a hypothesis, with no allele-specific occupancy or QBiC-SELEX result supplied. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies within the enhancer-like cCRE EH38E1374646, but the supplied activity maxima do not establish liver-specific activity. | supported | [E03](#e03) |
| gene | SORT1 is a plausible candidate target given its strong locus-to-gene scores and positive T-allele liver eQTL; direct regulation by this cCRE is not shown. | weak | [E16](#e16), [E17](#e17) |
| cell_type | The evidence is consistent with a liver-cell context through FOXA1 occupancy in HepG2 and a SORT1 eQTL in bulk liver, but does not establish hepatocyte-specific action. | weak | [E05](#e05), [E17](#e17) |
| phenotype | This chain predicts that T-associated SORT1 expression contributes to lipid-trait effects, but the supplied evidence does not establish that FOXA1-mediated SORT1 regulation causes the phenotype. Association direction is not fully uniform across the listed results. | weak | [E15](#e15), [E17](#e17) |

Predictions: Allele-specific FOXA1 occupancy should be greater on T than G in a relevant liver-cell model.; A G-to-T edit should increase SORT1 expression, and FOXA1 perturbation should reduce that allele-dependent increase; unlike H1, the effect should not specifically depend on CEBPA.

Falsified if: A suitably powered allele-specific assay finds no greater FOXA1 occupancy on T, or finds greater occupancy on G.; Isogenic editing produces no allele-dependent SORT1 change, or FOXA1 perturbation does not affect the change.

### 4. H3: Candidate FOXA2-mediated effect on PSRC1 (p = 0.09)

TF FOXA2 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646; gene PSRC1; cell type Liver-cell context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA2 is occupied at the variant and expressed in the stated cell line. This makes it a candidate, but does not distinguish it from FOXA1, CEBPA, or other occupied factors. Greater binding to T is hypothetical; no allele-specific occupancy or QBiC-SELEX result establishing that direction is supplied. | weak | [E04](#e04), [E09](#e09) |
| element | The variant lies within the enhancer-like cCRE EH38E1374646, near the PSRC1-CELSR2-MYBPHL cluster; the evidence does not assign the cCRE to PSRC1. | supported | [E03](#e03) |
| gene | PSRC1 is an alternative candidate because its expression is higher with T in liver, but locus-to-gene support is weaker than for SORT1 and direct cCRE-to-PSRC1 regulation is not shown. | weak | [E16](#e16), [E17](#e17) |
| cell_type | A liver-cell context is plausible from FOXA2 occupancy in HepG2 and the PSRC1 bulk-liver eQTL; these do not establish hepatocyte-specific action. | weak | [E09](#e09), [E17](#e17) |
| phenotype | This chain predicts that variant-dependent PSRC1 regulation contributes to lipid-trait effects, but the evidence does not isolate PSRC1 as a mediator. The cited cluster-level literature does not demonstrate a PSRC1-specific effect. | weak | [E15](#e15), [E18b](#e18b) |

Predictions: Allele-specific FOXA2 occupancy should be greater on T than G.; A G-to-T edit should alter PSRC1 expression, with a FOXA2-dependent effect; unlike H1 and H2, the primary expression effect should be on PSRC1 rather than SORT1.

Falsified if: A suitably powered allele-specific assay finds no greater FOXA2 occupancy on T, or finds greater occupancy on G.; Isogenic editing affects SORT1 but not PSRC1, or FOXA2 perturbation does not affect an allele-dependent PSRC1 response.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Dual-luciferase assay using otherwise matched G and T cCRE constructs in HepG2, with and without CEBPA knockdown. | low | yes | T construct has higher activity than G, and the difference is reduced by CEBPA knockdown. | No reproducible G-versus-T activity difference attributable to the variant. | T may have higher activity, but the difference should not specifically depend on CEBPA; FOXA1 perturbation would be the more relevant follow-up. | T may have higher activity, but the proposed effect is FOXA2-dependent and linked to PSRC1 rather than specifically CEBPA-dependent. |
| Allele-specific CEBPA CUT&RUN or ChIP in a heterozygous liver-cell model, with reads assigned to G and T. | medium | yes | Greater CEBPA occupancy on T than G. | No reproducible allele-specific CEBPA occupancy supporting a TF-mediated effect. | No specific prediction of greater CEBPA occupancy on T; FOXA1 is the proposed factor. | No specific prediction of greater CEBPA occupancy on T; FOXA2 is the proposed factor. |
| Isogenic G-to-T editing in HepG2 followed by SORT1 and PSRC1 expression measurement, with matched TF perturbations. | high | yes | T increases SORT1, and CEBPA perturbation attenuates that increase. | No reproducible edit-dependent, TF-dependent change in the measured genes. | T increases SORT1, and FOXA1 perturbation attenuates that increase. | T changes PSRC1, and FOXA2 perturbation attenuates that change. |

## Next experiment

Run the low-cost matched G-versus-T dual-luciferase assay in HepG2 with and without CEBPA knockdown. A T-specific activity increase that is reduced by CEBPA knockdown would distinguish the leading CEBPA chain from the null, while recognizing that a reporter assay does not establish the endogenous target gene.

## Investigate calls

- literature_search({"query": "rs12740374 liver allele-specific enhancer TF SORT1 FOXA1 CEBPA functional assay"})
- gene_disease({"gene": "SORT1"})
- gene_disease({"gene": "PSRC1"})

## Flags

- tool_failed: E20 gene_disease: Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'
- tool_failed: E21 gene_disease: Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'

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

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr1:109274968:G>T: 501 peaks contain the variant, from 261 factors in 25 biosamples. In the matching biosample HepG2 (HepG2 stands in for Hep 3B2.1-7 (both liver cancer lines)): 224 peaks from 188 factors. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): AFF1, ARID4A, ARID5B, ASH2L, BCL3, BRD4, CBFA2T3, CTBP1, DMAP1, DPF2, EED, EP300 (+97 more). Bound, expressed TFs with a binding model: 140; listed one per row: FOXA1, MAX, SP1, TCF7L2, FOXA2, USF1, JUND, RXRA, NR2F2, TCF12; also bound: ELF1, CREB1, EGR1, ATF3, NRF1, NCOA1, HNF4A, E2F4, YY1, NR2F6, ZNF281, MEIS2, FOXK2, FOXJ3, FOXA3, ZNF687, HNF1B, SOX6, FOXP1, ZHX2, MEF2D, CREM, ZBTB33, FOSL2, KLF9, CEBPA, KDM2A, MYBL2, ERF, ELF3 (+100 more). Bound but below 1 TPM: EGR2, ESR1, HOXD1, KLF1, KLF11, KLF4, MITF, MSX2, NKX3-1, NR5A1. Assayed with no peak here: 251 TFs in the matching biosample, 170 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXA1: bound here. 9 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, Ishikawa, MCF-7, T47D (+1 more) (e.g. ENCSR865RXA). 53.15 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 84 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound here. 8 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, HeLa-S3, K562, MCF-7 (e.g. ENCSR168DYA). 33.54 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 153 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 7 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, HCT116, liver (e.g. ENCSR000BJX). 23.48 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 234 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 6 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in HeLa-S3, MCF-7, Panc1 (e.g. ENCSR346BOD). 24.15 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 229 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXA2: bound here. 6 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, liver (e.g. ENCSR066EBK). 22.07 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 253 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> USF1: bound here. 5 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, K562 (e.g. ENCSR099FCQ). 85.08 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 42 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUND: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, K562, MCF-7 (e.g. ENCSR000BGK). 48.46 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 97 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> RXRA: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in liver (e.g. ENCSR416HDG). 31.42 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 167 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in MCF-7 (e.g. ENCSR000BVM). 22.86 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 243 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF12: bound here. 3 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, MCF-7 (e.g. ENCSR000BJG). 40.85 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 123 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs12740374&size=100; retrieved 2026-10-25T17:29:12+00:00)

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

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:04+00:00)

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

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_109274968_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:36+00:00)

> 39 significant GTEx v8 single-tissue eQTLs for chr1_109274968_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).
> CELSR2 in Muscle_Skeletal: NES +0.54, p 2.3e-76
> SORT1 in Liver: NES +1.27, p 3.1e-54
> PSRC1 in Liver: NES +1.24, p 1.1e-37
> CELSR2 in Liver: NES +1.04, p 9.4e-34
> PSRC1 in Esophagus_Mucosa: NES +0.40, p 1.8e-24
> CELSR2 in Esophagus_Mucosa: NES +0.31, p 1.1e-16
> PSRC1 in Whole_Blood: NES +0.30, p 4.0e-16
> PSRC1 in Pancreas: NES +0.53, p 2.2e-13
> CELSR2 in Pancreas: NES +0.32, p 2.8e-13
> PSRC1 in Muscle_Skeletal: NES +0.35, p 1.5e-12
> PSRC1 in Skin_Not_Sun_Exposed_Suprapubic: NES +0.29, p 2.0e-12
> PSRC1 in Testis: NES +0.35, p 9.0e-12
> CELSR2 in Skin_Sun_Exposed_Lower_leg: NES +0.12, p 5.1e-11
> SORT1 in Esophagus_Mucosa: NES +0.13, p 8.4e-11
> PSRC1 in Brain_Cortex: NES +0.34, p 2.5e-09

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20AND%20SORT1%20AND%20%28%22ldl%20cholesterol%22%20OR%20%22myocardial%20infarction%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:12+00:00)

> Europe PMC: 127 hits for 'rs12740374 AND SORT1 AND ("ldl cholesterol" OR "myocardial infarction")'; top 8 with PMIDs:
> PMID 42019808 (2026): Causal statistical association between remnant cholesterol and coronary heart disease: genetic insights into the PSRC1-CELSR2-SORT1 gene cluster.
> PMID 42820291 (2026): Clinical trials in a dish: cardiometabolic drug development with biological and digital twins.
> PMID 40922271 (2025): Effect of dietary habits on multiple cardiovascular diseases: A comprehensive Mendelian randomization study.
> PMID 41380003 (2025): Computationally efficient whole-genome quantile regression at biobank scale.
> PMID 39858645 (2025): Research Progress and Clinical Translation Potential of Coronary Atherosclerosis Diagnostic Markers from a Genomic Perspective.
> PMID 42211154 (2026): Treatment Target Discovery From Vasculo-Protective Phenotypes.
> PMID 41991941 (2026): Genetic and molecular factors underlying human longevity and epigenetic aging.
> PMID 38266112 (2024): Genome-Wide Genetic Associations Prioritize Evaluation of Causal Mechanisms of Atherosclerotic Disease Risk.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 42019808 (https://europepmc.org/article/MED/42019808; retrieved 2026-10-25T17:29:12+00:00)

> Colocalization identified shared signals at the PSRC1-CELSR2-SORT1 locus, with lead variants rs12740347 and rs646776.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 42019808 (https://europepmc.org/article/MED/42019808; retrieved 2026-10-25T17:29:12+00:00)

> Hepatic expression of PSRC1-CELSR2-SORT1 protects against CHD via RC reduction, independent of LDL-C, supporting RC as promising target for CHD prevention.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 40922271 (https://europepmc.org/article/MED/40922271; retrieved 2026-10-25T17:29:12+00:00)

> The co-localization analysis, based on two-sample Mendelian randomization results, revealed that single nucleotide polymorphism (SNP) rs12740374 (PH4 = 0.855) was causally associated with MI and a balanced diet(I eat all of the above), while SNP rs7528419 (PH4 = 0.716) was causally associated with CHD and a balanced diet.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 40922271 (https://europepmc.org/article/MED/40922271; retrieved 2026-10-25T17:29:12+00:00)

> Moreover, 2 SNPs, rs7528419 and rs12740374, were identified as drivers of common motifs in 6 genes.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 39858645 (https://europepmc.org/article/MED/39858645; retrieved 2026-10-25T17:29:12+00:00)

> GWASs and sequencing studies have identified key genetic variations associated with CAD, including JCAD/KIAA1462, GUCY1A3, PCSK9, and SORT1, which regulate inflammation, lipid metabolism, and vascular function.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20liver%20allele-specific%20enhancer%20TF%20SORT1%20FOXA1%20CEBPA%20functional%20assay&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:25:24+00:00)

> Europe PMC: 0 hits for 'rs12740374 liver allele-specific enhancer TF SORT1 FOXA1 CEBPA functional assay'; top 0 with PMIDs:

<a id="e20"></a>**E20** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'

<a id="e21"></a>**E21** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'
