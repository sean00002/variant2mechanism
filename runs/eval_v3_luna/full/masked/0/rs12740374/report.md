# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 7 model calls; 145 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: CEBPG (bound here, z 26.76); CEBPA (bound here, z 22.81); MLX (bound here, z -15.37); GFI1 (bound here, z 14.71); KLF6 (bound here, z -13.34); KLF12 (bound here, z -13.34); HNF4A (bound here, z 11.41); NR2F6 (bound here, z 11.41); RXRB (bound here, z 11.41); RXRA (bound here, z 11.41). Occupancy unknown: ZNF43 (z 35.83); RFX2 (z 23.16); TFAP2A (z -21.21); TFAP2E (z -21.21); ZNF345 (z 20.62). Diagnostic, not shown to the model: 239 of 997 models pass Bonferroni.

## Ranked chains

### 1. H5: No TF-mediated effect of this variant (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: Changing this base alone will not reproducibly produce a TF-dependent change in enhancer activity or target-gene expression; the association may reflect linkage or another mechanism.; The reported occupancy and in-vitro binding predictions will not translate into a variant-specific molecular effect in relevant liver cells.

Falsified if: Precise editing of G to T reproducibly changes enhancer activity or target-gene expression in relevant liver cells and the effect depends on a specific TF.

### 2. H1: Alt-enhanced CEBPA binding increases enhancer activity (p = 0.27)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in enhancer-like cCRE EH38E1374646; its reported activity scores are maxima across biosamples, not liver-specific measurements.; gene SORT1 is the strongest locus-level target candidate, but direct regulation of SORT1 by this cCRE is not shown.; cell type A candidate effect in liver cells is supported by CEBPA occupancy in HepG2 and CEBPA expression in Hep 3B2.1-7..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA is reported to occupy the site in HepG2, and QBiC-SELEX predicts stronger alt-T binding; importantly, E35 includes an alt-increasing CEBPA-specific model as well as a mapped CEBPB model, so the direction is not based only on the related-factor model. | supported | [E21](#e21), [E35](#e35) |
| element | The variant lies in the distal enhancer-like cCRE EH38E1374646, although the reported chromatin activity maxima are not liver-specific. | supported | [E03](#e03) |
| gene | SORT1 is a leading candidate target based on locus-to-gene scores and an alt-increasing liver eQTL, but these data do not connect this cCRE directly to SORT1. | supported | [E16](#e16), [E17](#e17) |
| cell_type | CEBPA occupancy in HepG2 and its high expression in Hep 3B2.1-7 support, but do not establish, a liver-cell mechanism. | supported | [E21](#e21) |
| phenotype | An alt-associated increase in SORT1 is directionally compatible with the alt-increasing liver eQTL and the predominantly G-risk cholesterol associations; mediation to cholesterol traits or myocardial infarction is not established. | weak | [E15](#e15), [E17](#e17), [E18b](#e18b) |

Predictions: An allele-specific assay should show stronger CEBPA binding to T than G; reducing CEBPA should reduce the T-versus-G difference in enhancer activity if CEBPA mediates it.; If CEBPA activates this element, precise G-to-T editing should increase SORT1 expression, provided this cCRE regulates SORT1 in the tested liver cells.

Falsified if: A well-controlled allele-specific assay finds no CEBPA preference for T, or CEBPA perturbation leaves the variant-dependent enhancer effect unchanged.; Precise editing produces no reproducible variant-dependent molecular effect in a relevant liver-cell assay.

### 3. H4: Loss of ref-preferred KLF6 binding relieves enhancer repression (p = 0.17)

TF KLF6 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E1374646; its liver-specific activity is not established.; gene SORT1 is the leading locus-level target candidate, but direct regulation by this cCRE is not shown.; cell type KLF6 occupancy in HepG2 and expression in Hep 3B2.1-7 support a candidate liver-cell mechanism..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | KLF6 is reported to occupy the variant in HepG2, and its own QBiC-SELEX model predicts stronger ref-G binding at a strong site; this does not establish allele-specific occupancy in cells. | supported | [E24](#e24) |
| element | The variant lies in the distal enhancer-like cCRE EH38E1374646, with activity-associated chromatin scores reported across biosamples rather than specifically in liver. | supported | [E03](#e03) |
| gene | SORT1 is a candidate target based on its high locus-to-gene support and positive liver eQTL for T, but the evidence does not link this cCRE directly to SORT1. | supported | [E16](#e16), [E17](#e17) |
| cell_type | KLF6 occupancy in HepG2 and expression in Hep 3B2.1-7 support a candidate liver-cell role. | supported | [E24](#e24) |
| phenotype | If KLF6 represses this element, reduced binding on T could be consistent with increased liver SORT1 expression and the cholesterol-association direction, but repression and trait mediation are not demonstrated. | weak | [E15](#e15), [E17](#e17), [E18b](#e18b) |

Predictions: An allele-specific assay should show stronger KLF6 binding to G; KLF6 depletion should preferentially relieve repression on G if this TF is the mediator.; KLF6 perturbation should affect the allele-dependent enhancer effect, unlike a model mediated by MLX or CEBPA.

Falsified if: KLF6 lacks a ref-G preference in an allele-specific assay, or KLF6 perturbation leaves the variant-dependent effect unchanged.; KLF6 activates rather than represses the element and no alternative mechanism explains the proposed direction.

### 4. H3: Loss of ref-preferred MLX binding relieves enhancer repression (p = 0.12)

TF MLX (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E1374646; liver-specific activity is not provided.; gene SORT1 is a candidate target from locus-level evidence, but this cCRE has not been directly linked to it.; cell type MLX occupancy in HepG2 and expression in Hep 3B2.1-7 support a candidate liver-cell mechanism..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MLX is reported to occupy the variant in HepG2, and its QBiC-SELEX model predicts stronger binding to ref G at a strong site; this is an in-vitro binding prediction, not allele-specific occupancy. | supported | [E22](#e22) |
| element | The site is within the distal enhancer-like cCRE EH38E1374646, whose reported activity scores are across biosamples. | supported | [E03](#e03) |
| gene | SORT1 is a candidate target based on locus-to-gene scores and an alt-increasing liver eQTL, but direct regulation by this cCRE remains unshown. | supported | [E16](#e16), [E17](#e17) |
| cell_type | MLX occupancy in HepG2 and expression in Hep 3B2.1-7 support a candidate liver-cell setting. | supported | [E22](#e22) |
| phenotype | If MLX represses the element, loss of its binding on T could fit the liver eQTL and cholesterol-association direction; MLX repression and mediation to the trait are not established. | weak | [E15](#e15), [E17](#e17), [E18b](#e18b) |

Predictions: An allele-specific assay should show stronger MLX binding to G; MLX depletion should preferentially relieve repression on G if the proposed repressor model is correct.; MLX perturbation should change the allele-dependent enhancer effect; this dependence distinguishes the model from the CEBPA and KLF6 models.

Falsified if: MLX lacks a ref-G binding preference in a relevant allele-specific assay, or MLX perturbation does not affect the variant-dependent effect.; MLX activates rather than represses the element and no alternative mechanism explains the proposed direction.

### 5. H2: Loss of ref-preferred HNF4A binding changes enhancer repression (p = 0.09)

TF HNF4A (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in enhancer-like cCRE EH38E1374646; its liver-specific activity has not been established.; gene SORT1 is a plausible locus-level target, but regulation of SORT1 by this cCRE is unproven.; cell type HNF4A occupancy in HepG2 and expression in Hep 3B2.1-7 make a liver-cell mechanism plausible..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HNF4A is reported bound at the site; its own QBiC-SELEX model predicts a modest ref-G preference, whereas the stronger alt-increasing signal comes from an NR2F2-mapped model and does not establish HNF4A's allele preference. | supported | [E26](#e26), [E36](#e36) |
| element | The variant lies in the distal enhancer-like cCRE EH38E1374646, with activity-associated chromatin scores reported across biosamples rather than specifically in liver. | supported | [E03](#e03) |
| gene | SORT1 is supported as a locus-level candidate by L2G scores and an alt-increasing liver eQTL, but direct cCRE-to-SORT1 regulation is not shown. | supported | [E16](#e16), [E17](#e17) |
| cell_type | HNF4A occupancy in HepG2 and expression in Hep 3B2.1-7 support a candidate liver-cell setting. | supported | [E26](#e26) |
| phenotype | If ref-preferred HNF4A represses this element, reduced binding on T could be consistent with increased liver SORT1 expression and the cholesterol association direction, but neither repression nor trait mediation is demonstrated. | weak | [E15](#e15), [E17](#e17), [E18b](#e18b) |

Predictions: An HNF4A-specific allele-binding assay should show a ref preference, and HNF4A perturbation should alter the G-versus-T enhancer effect if HNF4A mediates it.; Under the proposed repressor model, HNF4A depletion should preferentially relieve repression on G and reduce the expression difference between alleles.

Falsified if: An HNF4A-specific assay finds no ref preference and HNF4A perturbation does not affect the allele-dependent enhancer effect.; HNF4A is shown to activate rather than repress this element, with no alternative account of the proposed direction.

## Prediction matrix

| Test | Cost | Separates top two | H5 | H1 | H4 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CEBPA binding assay using ref/alt oligos and CEBPA-specific detection | low | yes | No reproducible variant-dependent CEBPA binding difference. | T binds more strongly than G. | No CEBPA-specific T preference is predicted; the proposed mediator is KLF6. | No CEBPA-specific T preference is predicted; the proposed mediator is MLX. | No CEBPA-specific T preference is predicted; the proposed mediator is HNF4A. |
| Perturb CEBPA, MLX, KLF6, or HNF4A individually in a liver-cell enhancer assay and compare ref/alt activity | medium | yes | No reproducible variant-dependent effect or TF-specific dependence. | The T-versus-G activity difference is reduced by CEBPA perturbation. | The allele-dependent effect is altered by KLF6 perturbation, with the proposed model predicting preferential relief on G. | The allele-dependent effect is altered by MLX perturbation, with the proposed model predicting preferential relief on G. | The allele-dependent effect is altered by HNF4A perturbation, with the proposed model predicting loss of ref-associated repression. |
| Precisely edit G to T in a liver-cell model and measure SORT1 expression and local enhancer activity | high | yes | No reproducible change attributable to editing this base. | If this cCRE regulates SORT1 and CEBPA activates it, T increases enhancer activity and SORT1 expression. | If KLF6 represses the element, T reduces KLF6 binding and increases enhancer activity and SORT1 expression. | If MLX represses the element, T reduces MLX binding and increases enhancer activity and SORT1 expression. | If HNF4A represses the element, T reduces HNF4A binding and increases enhancer activity and SORT1 expression. |

## Next experiment

Run the low-cost allele-specific CEBPA binding assay on ref-G and alt-T oligos with CEBPA-specific detection. The CEBPA model predicts stronger binding to T, whereas the null predicts no reproducible allele-dependent CEBPA binding.

## Investigate calls

- qbic_tf_detail({"tf": "CEBPA"})
- qbic_tf_detail({"tf": "HNF4A"})
- gene_disease({"gene": "SORT1"})

## Flags

- tool_failed: E37 gene_disease: Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'

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

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SORT1%20AND%20%28%22ldl%20cholesterol%22%20OR%20%22myocardial%20infarction%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:19:55+00:00)

> Europe PMC: 868 hits for 'SORT1 AND ("ldl cholesterol" OR "myocardial infarction")'; top 8 with PMIDs:
> PMID 41892715 (2026): Genome-Wide Association Studies of Myocardial Infarction: A Systematic Literature Review.
> PMID 42615437 (2026): South Asian Cardiovascular Risk: Role of Coronary Artery Calcium Scoring and Computed Tomography Angiography.
> PMID 42820291 (2026): Clinical trials in a dish: cardiometabolic drug development with biological and digital twins.
> PMID 42019808 (2026): Causal statistical association between remnant cholesterol and coronary heart disease: genetic insights into the PSRC1-CELSR2-SORT1 gene cluster.
> PMID 41999980 (2026): From lipoprotein metabolism to blood clotting: Highlights of the 2025 Fredrickson lipid research conference.
> PMID 42358645 (2026): The role of sortilin in cardiovascular calcification: mechanisms and therapeutic potential.
> PMID 39858645 (2025): Research Progress and Clinical Translation Potential of Coronary Atherosclerosis Diagnostic Markers from a Genomic Perspective.
> PMID 42511725 (2026): Special Issue "Advances in Molecular Forensic Pathology and Toxicology: An Update".

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 42019808 (https://europepmc.org/article/MED/42019808; retrieved 2026-10-26T20:19:55+00:00)

> Colocalization identified shared signals at the PSRC1-CELSR2-SORT1 locus, with lead variants rs[masked] and rs[masked].

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 42019808 (https://europepmc.org/article/MED/42019808; retrieved 2026-10-26T20:19:55+00:00)

> Hepatic expression of PSRC1-CELSR2-SORT1 protects against CHD via RC reduction, independent of LDL-C, supporting RC as promising target for CHD prevention.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 42358645 (https://europepmc.org/article/MED/42358645; retrieved 2026-10-26T20:19:55+00:00)

> Sortilin (encoded by SORT1), a multi-ligand intracellular trafficking receptor, has recently emerged as a critical molecular mediator linking metabolic risk factors-such as dyslipidemia, diabetes, hypertension, and chronic kidney disease-to pro-calcific cellular responses.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 39858645 (https://europepmc.org/article/MED/39858645; retrieved 2026-10-26T20:19:55+00:00)

> GWASs and sequencing studies have identified key genetic variations associated with CAD, including JCAD/KIAA1462, GUCY1A3, PCSK9, and SORT1, which regulate inflammation, lipid metabolism, and vascular function.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:109274968:G>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000625), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 140 occupied (63 with a strong site), 5 of 78 with unknown occupancy. Left out: 251 TFs assayed in the matching biosample and 170 assayed only elsewhere, none with a peak here; 12 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPG (bZIP, 1 model; QBiC-SELEX coverage: own model): best model CEBPG_eDBD_TACTTT40NTCT_KN_yin2017_0_4_7mer (its own model), z 26.76, effect 2.321: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 46.37 TPM, rank 103 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR639IIZ. Best model's site strength: ref 64.5th, alt 99.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPA (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (a CIS-BP-mapped model of CEBPB), z 22.81, effect 2.331: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 141.33 TPM, rank 18 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR142IGM. Best model's site strength: ref 87.0th, alt 99.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MLX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MLX_eDBD_TAGGCT40NACC_KAN_yin2017_0_4_6mer (its own model), z -15.37, effect -0.496: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 57.97 TPM, rank 73 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR125DAD. Best model's site strength: ref 99.4th, alt 82.1th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GFI1 (C2H2 ZF, 2 models; QBiC-SELEX coverage: own model): best model GFI1_eDBD_TCTGCT40NTGT_KR_yin2017_1_2_7mer (its own model), z 14.71, effect 0.372: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.47 TPM, rank 921 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR849FVL. Best model's site strength: ref 87.9th, alt 97.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> KLF6 (C2H2 ZF, 6 models; QBiC-SELEX coverage: own model): best model KLF6_eDBD_TGCTCC40NCCG_KW_yin2017_0_3_7mer (its own model), z -13.34, effect -0.351: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 46.95 TPM, rank 99 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR757EKM. Best model's site strength: ref 98.6th, alt 82.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> KLF12 (C2H2 ZF, 6 models; QBiC-SELEX coverage: own model): best model KLF6_eDBD_TGCTCC40NCCG_KW_yin2017_0_3_7mer (a CIS-BP-mapped model of KLF6), z -13.34, effect -0.351: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.14 TPM, rank 1054 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR552YWL. Best model's site strength: ref 98.6th, alt 82.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF4A (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2F2), z 11.41, effect 0.416: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 90.19 TPM, rank 38 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR469FBY. Best model's site strength: ref 95.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F6 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2F2), z 11.41, effect 0.416: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 47.82 TPM, rank 98 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR798IJO. Best model's site strength: ref 95.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> RXRB (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2F2), z 11.41, effect 0.416: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 32.41 TPM, rank 159 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR560SEP. Best model's site strength: ref 95.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> RXRA (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2F2), z 11.41, effect 0.416: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 31.42 TPM, rank 167 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR416HDG. Best model's site strength: ref 95.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF43 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF43_FL_GC40NTATAGG_YWRA_jolma2025_0_3_7mer (its own model), z 35.83, effect 3.431: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.74 TPM, rank 525 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 93.6th, alt 99.9th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> RFX2 (RFX, 4 models; QBiC-SELEX coverage: own model): best model RFX4_eDBD_TACTCG40NCAA_KAN_yin2017_0_3_7mer (a CIS-BP-mapped model of RFX4), z 23.16, effect 1.235: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.97 TPM, rank 708 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2A (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -21.21, effect -0.98: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.65 TPM, rank 570 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.8th, alt 98.8th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2E (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (its own model), z -21.21, effect -0.98: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.06 TPM, rank 961 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.8th, alt 98.8th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF345 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF345_eDBD_TGTAAG40NACT_KT_yin2017_0_3_7mer (its own model), z 20.62, effect 0.964: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.64 TPM, rank 1005 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.7th, alt 99.9th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"CEBPA","symbol":"CEBPA","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr1:109274968:G>T","gate_p":5.02e-05,"models":[{"model":"CEBPA_NA_lib5_20N_rm2017_0_3_7mer","mapping":"own","group":"G035 bZIP, 3 models","quality":0.948,"effect":2.803,"z":22.63,"p":2.2e-113,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":66.0,"alt_percentile":98.8,"k":7}},{"model":"CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (CEBPB)","group":"G035 bZIP, 3 models","quality":0.748,"effect":2.331,"z":22.81,"p":3.9e-115,"rank_abs_z":"8/997","passed_gate":true,"site_strength":{"ref_percentile":87.0,"alt_percentile":99.8,"k":7}},{"model":"CEBPE_eDBD_TTAGGC40NATA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (CEBPE)","group":"G035 bZIP, 3 models","quality":0.817,"effect":1.731,"z":11.28,"p":1.7e-29,"rank_abs_z":"28/997","passed_gate":true,"site_strength":{"ref_percentile":77.0,"alt_percentile":99.3,"k":7}}]}

<a id="e36"></a>**E36** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"HNF4A","symbol":"HNF4A","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr1:109274968:G>T","gate_p":5.02e-05,"models":[{"model":"HNF4A_NA_TGACAG20NGA_AF_jolma2013_1_3_7mer","mapping":"own","group":"G078 Nuclear receptor, 2 models","quality":0.709,"effect":-0.141,"z":-4.69,"p":2.8e-06,"rank_abs_z":"185/997","passed_gate":true,"site_strength":{"ref_percentile":90.8,"alt_percentile":67.2,"k":7}},{"model":"COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer","mapping":"CIS-BP (NR2F2)","group":"G002 Nuclear receptor, 29 models","quality":0.896,"effect":0.416,"z":11.41,"p":3.8e-30,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":95.5,"alt_percentile":99.6,"k":7}},{"model":"HNF4G_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (HNF4G)","group":"G078 Nuclear receptor, 2 models","quality":0.731,"effect":-0.074,"z":-2.24,"p":0.025,"rank_abs_z":"473/997","passed_gate":false,"site_strength":{"ref_percentile":97.4,"alt_percentile":89.8,"k":7}},{"model":"NR2F1_NA_TCTGAC30NAGG_ESAI_yang2017_1_4_7mer","mapping":"CIS-BP (NR2F1)","group":"G002 Nuclear receptor, 29 models","quality":0.879,"effect":-0.022,"z":-0.36,"p":0.72,"rank_abs_z":"900/997","passed_gate":false,"site_strength":{"ref_percentile":95.0,"alt_percentile":79.2,"k":7}},{"model":"NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer","mapping":"CIS-BP (NR2F6)","group":"G002 Nuclear receptor, 29 models","quality":0.764,"effect":0.465,"z":5.42,"p":5.9e-08,"rank_abs_z":"137/997","passed_gate":true,"site_strength":{"ref_percentile":86.9,"alt_percentile":98.0,"k":7}},{"model":"NR6A1_eDBD_TTGATG40NATC_KT_yin2017_0_3_7mer","mapping":"CIS-BP (NR6A1)","group":"G002 Nuclear receptor, 29 models","quality":0.914,"effect":0.128,"z":2.84,"p":0.0044,"rank_abs_z":"377/997","passed_gate":false,"site_strength":{"ref_percentile":98.3,"alt_percentile":81.5,"k":7}},{"model":"RXRB_NA_TGAGCA20NGA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (RXRB)","group":"G002 Nuclear receptor, 29 models","quality":0.667,"effect":-0.121,"z":-3.2,"p":0.0014,"rank_abs_z":"322/997","passed_gate":false,"site_strength":{"ref_percentile":87.6,"alt_percentile":75.5,"k":7}},{"model":"RXRG_NA_TGGAAT20NGA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (RXRG)","group":"G002 Nuclear receptor, 29 models","quality":0.783,"effect":0.408,"z":1.59,"p":0.11,"rank_abs_z":"594/997","passed_gate":false,"site_strength":{"ref_percentile":76.2,"alt_percentile":95.7,"k":7}},{"model":"TLX_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer","mapping":"CIS-BP (NR2E1)","group":"G372 Nuclear receptor, 1 model","quality":0.88,"effect":0.107,"z":2.41,"p":0.016,"rank_abs_z":"444/997","passed_gate":false,"site_strength":{"ref_percentile":85.5,"alt_percentile":95.9,"k":7}}]}

<a id="e37"></a>**E37** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'
