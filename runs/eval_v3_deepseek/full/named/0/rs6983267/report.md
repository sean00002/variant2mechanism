# rs6983267 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 405 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -4.66); SRF (bound here, z -7.74, weak site); SP1 (bound here, z -4.76, weak site); JUND (bound here, z -3.01, no clear allelic change, weak site); CEBPB (bound here, z 1.9, no clear allelic change, weak site); MAX (bound here, z -0.97, no clear allelic change, weak site); YY1 (bound here, z -0.43, no clear allelic change, weak site); HNF4A (bound elsewhere, z 53.69); GFI1 (bound elsewhere, z -31.27); NR2F2 (bound elsewhere, z 20.82). Occupancy unknown: ZNF493 (z -34.16); TBX19 (z 26.18); MBNL2 (z -22.42); NR1D1 (z 20.82); NR1D2 (z 20.82). Diagnostic, not shown to the model: 421 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1_TCF7L2_ref_G: TCF7L2 binds the ref G allele more at the 8q24 enhancer and lowers POU5F1B to modulate CRC risk (p = 0.45)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element None; gene POU5F1B; cell type colorectal carcinoma / colon.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref G allele more strongly than the alt T allele if the HMG/Sox family model reflects TCF7L2. TCF7L2 has ENCODE ChIP-seq occupancy over the variant in HCT116 and is well expressed there (E05). However, TCF7L2 has no own QBiC-SELEX model; E35 uses CIS-BP-mapped LEF1/TCF7/TCF7L1 models, with best effect -0.47 (ref > alt; z -4.66) and a strong site. I therefore treat the allelic direction as family-level and weak, not as a TCF7L2 own-model measurement. | weak | [E05](#e05), [E35](#e35), [E04](#e04) |
| element | rs6983267 lies in the active proximal enhancer-like cCRE EH38E3858447, and TCF7L2 has a ChIP-seq peak over this region in HCT116. E03 z-scores are maxima across biosamples, so HCT116-specific enhancer activity is not directly proven. | weak | [E03](#e03), [E05](#e05) |
| gene | The element is linked to POU5F1B by L2G (best gene score 0.89) and by a colon transverse eQTL in which alt T is associated with higher POU5F1B (NES +0.20). POU5F1B is a literature-supported colorectal cancer oncogene. This chain requires TCF7L2 to repress POU5F1B so that lower TCF7L2 binding on T fits higher POU5F1B on T; that repression is an assumption, not shown by perturbation or reporter evidence. L2G is also dominated by prostate/PSA credible sets, not CRC-specific credible sets. | weak | [E16](#e16), [E17](#e17), [E18b](#e18b), [E18c](#e18c), [E18d](#e18d) |
| cell_type | The relevant context is colorectal: HCT116 is the matching ENCODE/DepMap colorectal carcinoma line with TCF7L2 expression and occupancy, and GTEx colon transverse shows the POU5F1B eQTL. HCT116 is a carcinoma line, not normal colon. | supported | [E05](#e05), [E17](#e17) |
| phenotype | The strongest CRC GWAS endpoint lists the alt T allele as the effect allele. If T reduces TCF7L2 occupancy and TCF7L2 represses POU5F1B, T would raise POU5F1B and increase CRC risk. E15 also contains CRC/colon endpoints with G as the effect allele, so the disease-allele direction is not fully consistent across studies. | weak | [E15](#e15), [E18c](#e18c), [E18d](#e18d) |

Predictions: Allele-specific TCF7L2 ChIP or footprinting will show stronger TCF7L2 occupancy on ref G than alt T in colorectal cells.; TCF7L2 knockdown or CRISPR perturbation should change POU5F1B expression in a direction consistent with TCF7L2 repressing POU5F1B at this element.; Editing G>T in HCT116 should alter POU5F1B expression and enhancer activity in a TCF7L2-dependent manner.

Falsified if: TCF7L2 ChIP or footprinting is not allele-specific at this base.; TCF7L2 perturbation does not affect POU5F1B expression in colorectal cells.; The CRC association is fully explained by another variant in LD that changes a different TF or element.

### 2. H4_null: No TF-mediated effect of rs6983267; the association is due to a linked causal variant or another element (p = 0.43)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at the rs6983267 base in colorectal cells.; The CRC association is explained by another variant in LD within the 8q24 enhancer cluster.; Editing only rs6983267 should not change enhancer activity or POU5F1B expression.

Falsified if: Allele-specific TF occupancy or enhancer activity is demonstrated at this exact base.; CRISPR editing of rs6983267 alone changes POU5F1B expression or a CRC-relevant phenotype.; The eQTL and GWAS signals are shown to depend on this base rather than a linked variant.

### 3. H3_NR2F2_alt_T: NR2F2 binds the alt T allele more and activates POU5F1B in colorectal cells (p = 0.07)

TF NR2F2 (QBiC-SELEX coverage own_model), alt allele binds more; element None; gene POU5F1B; cell type colorectal carcinoma / colon.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NR2F2 is predicted to bind the alt T allele more strongly by QBiC-SELEX: effect +1.92 (alt > ref; z 20.82), with a strong site. However, the best model is a CIS-BP-mapped NR2F6 model, not clearly an NR2F2 own model, and the same QBiC model/effect appears for NR1D1/NR1D2 in E33/E34, so NR2F2 specificity is weak. E36 reports no NR2F2 ChIP-seq peak over the variant in HCT116; the only reported peak is in HepG2/liver. Occupancy in the matching colorectal cell line is therefore missing. | weak | [E29](#e29), [E36](#e36), [E04](#e04) |
| element | The variant is in the active pELS EH38E3858447, but the claim that this is an NR2F2-responsive enhancer rests on a CIS-BP-mapped NR2F6 model and is not validated by NR2F2 occupancy in colorectal cells. E36 provides no HCT116 NR2F2 peak over the variant. | weak | [E03](#e03), [E36](#e36) |
| gene | The element is linked to POU5F1B by L2G and by a colon transverse eQTL where alt T increases POU5F1B. This chain assumes NR2F2 activates POU5F1B, so stronger NR2F2 binding on T would fit the eQTL direction. That activation step is not supported by perturbation or reporter evidence. | weak | [E16](#e16), [E17](#e17), [E18b](#e18b), [E18c](#e18c), [E18d](#e18d) |
| cell_type | NR2F2 is expressed in HCT116, and the eQTL is in colon transverse, but direct NR2F2 occupancy in colorectal cells is not established by the given evidence; E36 reports only HepG2 occupancy. | weak | [E29](#e29), [E17](#e17), [E36](#e36) |
| phenotype | If alt T increases NR2F2 binding and NR2F2 activates POU5F1B, T would increase POU5F1B and promote colorectal cancer. The chain is limited because NR2F2 occupancy at this base in HCT116 is not shown and the NR2F2 motif specificity is weak. | weak | [E15](#e15), [E18c](#e18c), [E18d](#e18d) |

Predictions: NR2F2 should occupy this element in colorectal cells, with stronger binding on alt T than ref G.; NR2F2 perturbation should change POU5F1B expression in the direction expected for an activator.; The effect should be absent in cells that do not express NR2F2.

Falsified if: NR2F2 does not occupy this element in colorectal cells.; NR2F2 binding is not allele-specific at this base.; NR2F2 perturbation does not affect POU5F1B expression.

### 4. H2_SRF_ref_G: SRF binds the ref G allele more at the same enhancer and represses POU5F1B (p = 0.05)

TF SRF (QBiC-SELEX coverage own_model), ref allele binds more; element None; gene POU5F1B; cell type colorectal carcinoma / colon.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SRF binds the ref G allele more strongly than alt T in its own QBiC-SELEX model: effect -1.191 (ref > alt; z -7.74), and SRF has an ENCODE ChIP-seq peak over the variant in HCT116 and is expressed there. However, E21 reports the best SRF site is weak on both alleles (ref 95.1st, alt 91.3rd percentile; neither reaches 97.5th), so the ChIP peak more likely reflects another site in the element. Allele-specific SRF occupancy is not shown. | weak | [E21](#e21), [E09](#e09) |
| element | The variant lies in the active pELS EH38E3858447, and SRF has a ChIP-seq peak over this region in HCT116. This supports element localization, not allele-specific SRF function. | weak | [E03](#e03), [E09](#e09) |
| gene | The element is linked to POU5F1B by L2G and by a colon transverse eQTL in which alt T increases POU5F1B. This chain assumes that SRF represses POU5F1B, so lower SRF binding on T would fit higher POU5F1B on T. The SRF-repression step is not supported by perturbation or reporter evidence. | weak | [E16](#e16), [E17](#e17), [E18b](#e18b), [E18c](#e18c), [E18d](#e18d) |
| cell_type | SRF is expressed and bound in HCT116, and the eQTL context is colon transverse, making a colorectal cell context plausible. This does not establish allele-specific SRF function. | supported | [E09](#e09), [E17](#e17) |
| phenotype | If alt T lowers SRF occupancy and SRF represses POU5F1B, T would increase POU5F1B and could contribute to CRC risk. The phenotype link is weak because the SRF motif is weak on both alleles and no SRF-specific CRC or POU5F1B perturbation evidence is provided. | weak | [E15](#e15), [E18c](#e18c), [E18d](#e18d) |

Predictions: Allele-specific SRF ChIP should show stronger SRF occupancy on ref G than alt T in HCT116 or colon cells.; SRF knockdown should change POU5F1B expression if SRF acts through this element.; The SRF effect should be weaker than TCF7L2 because the SRF site is weak on both alleles by QBiC-SELEX.

Falsified if: SRF does not occupy the variant base by allele-specific ChIP or footprinting.; SRF perturbation does not alter POU5F1B expression.; The SRF ChIP peak is explained entirely by a nearby site rather than the variant.

## Prediction matrix

| Test | Cost | Separates top two | H1_TCF7L2_ref_G | H4_null | H3_NR2F2_alt_T | H2_SRF_ref_G |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 ChIP-qPCR or footprinting at rs6983267 in HCT116/colorectal cells | medium | yes | ref G shows stronger TCF7L2 occupancy than alt T | no allele-specific TF occupancy at the rs6983267 base | no TCF7L2 allele-specific occupancy; NR2F2 may occupy the element with alt T > ref G if it acts here | no TCF7L2 allele-specific occupancy; SRF may show allele-specific occupancy instead |
| CRISPR base editing of rs6983267 G>T in HCT116 with measurement of POU5F1B expression and enhancer reporter activity | high | yes | T allele increases POU5F1B expression/activity in a TCF7L2-dependent direction consistent with TCF7L2 repressing POU5F1B | editing rs6983267 alone does not change POU5F1B expression or enhancer activity | T allele increases POU5F1B and NR2F2 perturbation reduces the effect | T allele changes POU5F1B only if SRF is present; SRF perturbation mimics the effect |
| TCF7L2 knockdown/CRISPRi in HCT116 followed by POU5F1B expression measurement | medium | yes | TCF7L2 loss changes POU5F1B expression in the direction expected if TCF7L2 represses POU5F1B at this element | TCF7L2 loss has no effect on POU5F1B through this element | TCF7L2 loss has little or no effect on POU5F1B; NR2F2 perturbation is the relevant test | TCF7L2 loss has little or no effect on POU5F1B; SRF perturbation is the relevant test |
| NR2F2 ChIP-qPCR in HCT116 at the rs6983267 element | medium | no | no NR2F2 occupancy or no allele specificity | no NR2F2 allele-specific occupancy at this base | NR2F2 occupies the element in HCT116, ideally with alt T > ref G | no NR2F2 occupancy or no allele specificity |
| Fine-mapping plus CRISPR perturbation of linked 8q24 variants in the same enhancer cluster | high | yes | rs6983267 remains the functional variant after controlling for linked variants | a linked variant, not rs6983267, explains the enhancer/expression effect | rs6983267 remains functional but NR2F2-dependent | rs6983267 remains functional but SRF-dependent |

## Next experiment

Targeted allele-specific TCF7L2 ChIP-qPCR (or footprinting) at rs6983267 in HCT116 colorectal carcinoma cells: compare TCF7L2 occupancy on ref G versus alt T.

## Investigate calls

- qbic_tf_detail({"tf": "TCF7L2"})
- chip_peaks({"tf": "NR2F2", "biosample": "HCT116"})
- literature_search({"query": "rs6983267 allele-specific TCF7L2 ChIP CRISPR reporter POU5F1B colorectal"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401060-127401060:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T16:33:46+00:00)

> Variant chr8:127401060:G>T (GRCh38), allele string G/T
> Known IDs: rs6983267
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: 1.54
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401060-128401060?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T16:33:42+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401060:G>T, by distance to TSS:
> POU5F1B: 78.9 kb from TSS (in gene body, strand +1)
> MYC: 334.4 kb from TSS (upstream, strand +1)
> LRATD2: 842.6 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T16:32:58+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:127401060:G>T: 330 peaks contain the variant, from 116 factors in 64 biosamples. In the matching biosample HCT116: 10 peaks from 9 factors. cCRE class at the variant: pELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID5B, ASH2L, CHD4, EHMT2, EP300, HDAC1, HDAC2, HMGXB4, KAT8, KDM1A, KDM6A, LCOR (+34 more). Bound, expressed TFs with a binding model: 64; listed one per row: TCF7L2, SP1, YY1, MAX, SRF, JUND, CEBPB, CTCF, MYBL2, ERF; also bound: NR2F6, NR2F1, ELF1, NR2C2, KLF16, CREM, TFAP4, RXRB, ATF2, RXRA, ZNF609, AHDC1, ZNF652, NFIA, HNF4A, MNX1, HNF1B, ZNF362, FOXA1, HMG20B, NR2F2, KLF6, NFIC, ATF1, TEAD4, ETV5, ZNF317, NFIL3, THAP11, ZBTB7B (+24 more). Bound but below 1 TPM: FOXA2, HNF1A, MIXL1, ONECUT1, SOX6, TBX2. Assayed with no peak here: 6 TFs in the matching biosample, 497 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000EUV). 63.61 TPM in DepMap:ACH-000971 (HCT 116), rank 53 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2, liver (e.g. ENCSR000BSF). 38.96 TPM in DepMap:ACH-000971 (HCT 116), rank 118 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> YY1: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BNX). 84.45 TPM in DepMap:ACH-000971 (HCT 116), rank 34 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSH). 42.59 TPM in DepMap:ACH-000971 (HCT 116), rank 102 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SRF: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSC). 25.61 TPM in DepMap:ACH-000971 (HCT 116), rank 217 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUND: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSA). 18.66 TPM in DepMap:ACH-000971 (HCT 116), rank 300 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSD). 13.15 TPM in DepMap:ACH-000971 (HCT 116), rank 408 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 150 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: 22Rv1, A549, A673, B cell, C4-2B, CD14-positive monocyte (+53 more) (e.g. ENCSR072EUE). 50.0 TPM in DepMap:ACH-000971 (HCT 116), rank 78 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 67.51 TPM in DepMap:ACH-000971 (HCT 116), rank 46 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ERF: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR159DQO). 46.58 TPM in DepMap:ACH-000971 (HCT 116), rank 90 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs6983267&size=100; retrieved 2026-10-25T16:33:55+00:00)

> 69 GWAS Catalog associations for rs6983267, strongest first:
> Colorectal cancer: p 2.0e-122, effect allele T, risk-allele frequency NR, PMID 36539618
> Prostate-specific antigen levels: p 9.0e-121, effect allele T, risk-allele frequency NR, PMID 39930085
> Prostate cancer: p 1.0e-113, effect allele G, risk-allele frequency NR, PMID 33398198
> Elevated prostate specific antigen [PSA] (PheCode 796): p 2.0e-96, effect allele G, risk-allele frequency 0.5087, PMID 39024449
> prostate-specific antigen (PSA, maximum, inv-norm transformed): p 7.0e-74, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Cancer (pleiotropy): p 8.0e-74, effect allele G, risk-allele frequency NR, PMID 32887889
> prostate-specific antigen (PSA, mean, inv-norm transformed): p 1.0e-72, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Colorectal cancer or advanced adenoma: p 3.0e-64, effect allele G, risk-allele frequency 0.5228, PMID 30510241
> prostate-specific antigen (PSA, minimum, inv-norm transformed): p 6.0e-52, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Benign neoplasm of colon (PheCode 208): p 2.0e-48, effect allele G, risk-allele frequency 0.5088, PMID 39024449
> Colon polyps: p 6.0e-30, effect allele G, risk-allele frequency 0.566, PMID 39024449
> Colon cancer (PheCode 153.2): p 8.0e-26, effect allele G, risk-allele frequency 0.5899, PMID 39024449

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T16:33:46+00:00)

> 92 credible sets contain 8_127401060_G_T: 91 GWAS, 1 molecular QTL.
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Cancer of prostate (PheCode 185): PIP 1.00; L2G POU5F1B 0.82
> GWAS Elevated prostate specific antigen [PSA] (PheCode 796): PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> sceqtl for PVT1 (OTAR2057_IBDverse_ge_Colon_Goblet_MUC2+_SPDEF+_ENS): PIP 0.95
> Best L2G gene scores across these sets: POU5F1B 0.89, MYC 0.05

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 2 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).
> CASC8 in Whole_Blood: NES -0.32, p 6.3e-10
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20AND%20POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T16:33:56+00:00)

> Europe PMC: 52 hits for 'rs6983267 AND POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 35812248 (2022): Genome-Wide Association and Transcriptome-Wide Association Studies Identify Novel Susceptibility Genes Contributing to Colorectal Cancer.
> PMID 35987910 (2022): Transposon-activated POU5F1B promotes colorectal cancer growth and metastasis.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 39921239 (2025): System genetic analysis of intestinal cancer and periodontitis development as influenced by aging and diabesity using Collaborative Cross mice.
> PMID 36103972 (2022): Long non-coding RNA colon cancer-associated transcript 2: role and function in human cancers.
> PMID 34594420 (2021): Repurposing non-invasive prenatal testing data: Population study of single nucleotide variants associated with colorectal cancer and Lynch syndrome.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 35812248 (https://europepmc.org/article/MED/35812248; retrieved 2026-10-25T16:33:56+00:00)

> In the post-GWAS analyses, we first identified new genome-wide significant associations: three genomic risk loci were identified at 8q24.21 (rs6983267, P = 6.98 × 10-12), 15q13.3 (rs58658771, P = 1.40 × 10-10), and 18q21.1 (rs6507874, P = 1.91 × 10-14).

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 35812248 (https://europepmc.org/article/MED/35812248; retrieved 2026-10-25T16:33:56+00:00)

> In addition, the TWAS also identified four loci statistically significantly associated with CRC risk, largely explained by expression regulation, including six candidate genes (DUSP10, POU5F1B, C11orf53, COLCA1, COLCA2, and GREM1-AS1).

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 35987910 (https://europepmc.org/article/MED/35987910; retrieved 2026-10-25T16:33:56+00:00)

> Here, upon characterizing cancer-specific transposable element-driven transpochimeric gene transcripts (TcGTs) produced by this tumor in the SYSCOL cohort, we find that expression of the hominid-restricted retrogene POU5F1B through aberrant activation of a primate-specific endogenous retroviral promoter is a strong negative prognostic biomarker.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 35987910 (https://europepmc.org/article/MED/35987910; retrieved 2026-10-25T16:33:56+00:00)

> Correlating this observation, we demonstrate that POU5F1B fosters the proliferation and metastatic potential of CRC cells.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:127401060:G>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 64 occupied (19 with a strong site), 5 of 133 with unknown occupancy. Left out: 6 TFs assayed in the matching biosample and 497 assayed only elsewhere, none with a peak here; 6 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer (a CIS-BP-mapped model of LEF1), z -4.66, effect -0.47: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 63.61 TPM, rank 53 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000EUV. Best model's site strength: ref 98.8th, alt 98.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SRF (MADS box, 1 model; QBiC-SELEX coverage: own model): best model SRF_eDBD_TGCCAC40NGCC_KR_yin2017_0_3_7mer (its own model), z -7.74, effect -1.191: ref allele binds more (|z| above the gate), but between weak k-mers. 25.61 TPM, rank 217 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSC. Best model's site strength: ref 95.1th, alt 91.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): best model SP4_NA_TTATGT20NGTA_ESAE_yang2017_0_3_7mer (a CIS-BP-mapped model of SP4), z -4.76, effect -0.211: ref allele binds more (|z| above the gate), but between weak k-mers. 38.96 TPM, rank 118 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSF. Best model's site strength: ref 95.8th, alt 75.9th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUND (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUN_FL_TCAGTG40NGAT_KAE_yin2017_0_3_7mer (a CIS-BP-mapped model of JUN), z -3.01, effect -0.059: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 18.66 TPM, rank 300 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSA. Best model's site strength: ref 89.3th, alt 96.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPB (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (its own model), z 1.9, effect 0.205: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 13.15 TPM, rank 408 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSD. Best model's site strength: ref 75.7th, alt 85.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z -0.97, effect -0.058: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 42.59 TPM, rank 102 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSH. Best model's site strength: ref 91.8th, alt 95.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> YY1 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model YY1_FL_GG40NGTGAGA_YWKA_jolma2025_0_3_7mer (its own model), z -0.43, effect -0.033: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 84.45 TPM, rank 34 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BNX. Best model's site strength: ref 91.3th, alt 88.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF4A (Nuclear receptor, 1 model; QBiC-SELEX coverage: own model): best model TLX_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2E1), z 53.69, effect 1.968: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.95 TPM, rank 850 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, liver, e.g. ENCSR445QRF. Best model's site strength: ref 96.7th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GFI1 (C2H2 ZF, 2 models; QBiC-SELEX coverage: own model): best model GFI1B_eDBD_TTCTCA40NCCT_KR_yin2017_0_3_7mer (a CIS-BP-mapped model of GFI1B), z -31.27, effect -2.144: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.9 TPM, rank 857 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR849FVL. Best model's site strength: ref 99.9th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 61.74 TPM, rank 58 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BVM. Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF493 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF493_FL_TG40NTCTTGC_YWRA_jolma2025_0_2_7mer (its own model), z -34.16, effect -0.598: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.33 TPM, rank 977 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 88.9th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TBX19 (T-box, 2 models; QBiC-SELEX coverage: own model): best model TBX19_eDBD_TCTTGT40NCAG_KP_yin2017_0_4_7mer (its own model), z 26.18, effect 4.18: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.92 TPM, rank 936 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 79.0th, alt 99.9th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MBNL2 (CCCH ZF, 1 model; QBiC-SELEX coverage: own model): best model MBNL2_FL_TCTAAG40NTTA_KZ_yin2017_0_4_7mer (its own model), z -22.42, effect -2.708: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.09 TPM, rank 209 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.1th, alt 51.1th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1D1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 14.85 TPM, rank 361 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1D2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 37.06 TPM, rank 132 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401060:G>T","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.47,"z":-4.66,"p":3.2e-06,"rank_abs_z":"351/997","passed_gate":true,"site_strength":{"ref_percentile":98.8,"alt_percentile":98.4,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.229,"z":-4.59,"p":4.4e-06,"rank_abs_z":"367/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.275,"z":-3.47,"p":0.00052,"rank_abs_z":"486/997","passed_gate":false,"site_strength":{"ref_percentile":83.5,"alt_percentile":92.1,"k":7}}]}

<a id="e36"></a>**E36** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:12:23+00:00)

> No ENCODE NR2F2 ChIP-seq peak contains chr8:127401060:G>T in biosamples matching 'HCT116'. Absence can also mean no NR2F2 experiment in that biosample. In other biosamples, 1 NR2F2 peaks do contain the variant: HepG2 (experiments ENCSR000BVM).

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20allele-specific%20TCF7L2%20ChIP%20CRISPR%20reporter%20POU5F1B%20colorectal&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:12:25+00:00)

> Europe PMC: 2 hits for 'rs6983267 allele-specific TCF7L2 ChIP CRISPR reporter POU5F1B colorectal'; top 2 with PMIDs:
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 30794691 (2019): The Crohn's disease associated SNP rs6651252 impacts MYC gene expression in human colonic epithelial cells.

<a id="e37a"></a>**E37a** literature_search, Europe PMC abstract, PMID 30794691 (https://europepmc.org/article/MED/30794691; retrieved 2026-10-26T13:12:25+00:00)

> We demonstrate that rs6651252 resides within a Wnt responsive DNA enhancer element (WRE) and that the disease associated allele augments binding of the TCF7L2 transcription factor to this region.

<a id="e37b"></a>**E37b** literature_search, Europe PMC abstract, PMID 30794691 (https://europepmc.org/article/MED/30794691; retrieved 2026-10-26T13:12:25+00:00)

> Using CRISPR/Cas9 directed gene editing and epigenetic modulation, we find that the rs6651252 enhancer regulates expression of the c-MYC proto-oncogene (MYC).
