# rs6983267 and Colorectal cancer (8q24)

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 8 model calls; 250 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: No TF-mediated allelic effect; linked causal variant or passenger (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific change in TF occupancy at this exact base after controlling for linked variants.; The GWAS and eQTL signals are explained by a nearby causal variant in linkage disequilibrium or by a passenger event at a mutational hotspot.; TF knockdown does not alter an allele-specific expression effect at this base.

Falsified if: Allele-specific reporter or ChIP assays show a reproducible TF-dependent allelic effect at this exact base.; Fine-mapping separates the colorectal cancer signal from this variant and identifies a different causal variant in the same enhancer.; POU5F1B eQTL and colorectal cancer GWAS signals remain after conditioning on the candidate TF-binding allele.

### 2. H1: TCF7L2 occupancy at a colonic 8q24 enhancer with hypothesized ref-G-preferential binding and repression of POU5F1B (p = 0.36)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element pELS enhancer; gene POU5F1B; cell type colorectal carcinoma / HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is the leading TF candidate: it is expressed in HCT116 (63.61 TPM, rank 53/1626) and has four ENCODE ChIP-seq peaks containing the variant in HCT116 (E05; E19). This demonstrates occupancy, not allelic specificity. No QBiC-SELEX model or allele-specific binding measurement for TCF7L2 is provided here, so the claim that ref G binds TCF7L2 more strongly than alt T is an explicit, untested hypothesis, not a measured allele effect. | missing | [E04](#e04), [E05](#e05), [E19](#e19) |
| element | The variant lies in an active proximal enhancer-like cCRE with DNase and H3K27ac signal, and TCF7L2 occupies this base in HCT116. CTCF is bound at this base only in other biosamples, not in HCT116, so the element is better supported as a pELS occupied by TCF7L2 than as a CTCF boundary in the relevant cell type. | supported | [E01](#e01), [E03](#e03), [E04](#e04), [E05](#e05), [E12](#e12) |
| gene | POU5F1B is the best-supported target in this region: it is 78.9 kb from the variant, has the top L2G score (0.89), and has a colon transverse eQTL in which alt T increases POU5F1B (NES +0.20). For this chain to fit that eQTL direction, TCF7L2 would have to act as a repressor at this element, so loss of ref-G TCF7L2 binding on alt T would de-repress POU5F1B. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E18](#e18), [E20](#e20) |
| cell_type | HCT116 colorectal carcinoma is a relevant context because TCF7L2 is expressed and bound at the variant there, and colon eQTL data link the variant to POU5F1B. | supported | [E05](#e05), [E17](#e17), [E18](#e18), [E20](#e20) |
| phenotype | The variant is strongly associated with colorectal cancer in GWAS, with T as the reported colorectal cancer effect allele. This chain proposes that allele-specific TCF7L2 occupancy at this enhancer changes POU5F1B expression and thereby colorectal cancer risk. | supported | [E15](#e15), [E16](#e16), [E21i](#e21i) |

Predictions: QBiC-SELEX or allele-specific ChIP/CUT&RUN shows ref G > alt T TCF7L2 binding at this base.; TCF7L2 knockdown in HCT116 increases POU5F1B if TCF7L2 is repressive at this element.; The alt-T increase in POU5F1B is attenuated when the TCF7L2 site is mutated.

Falsified if: QBiC-SELEX or allele-specific ChIP/CUT&RUN shows alt T binds TCF7L2 more strongly than ref G.; TCF7L2 knockdown or loss of the TCF7L2 site decreases rather than increases POU5F1B in HCT116.; TCF7L2 occupancy at this exact base is not reproducible in HCT116.

### 3. H2: SP1 activation at the 8q24 enhancer increases POU5F1B (p = 0.14)

TF SP1 (QBiC-SELEX coverage own_model), alt allele binds more; element pELS enhancer; gene POU5F1B; cell type colorectal carcinoma / HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 is a competing candidate: it is expressed in HCT116 (38.96 TPM, rank 118/1626) and has four ENCODE ChIP-seq peaks containing the variant in HCT116 (E06). No QBiC-SELEX model or allele-specific data for SP1 is provided here; the claim that alt T binds SP1 more strongly than ref G is a hypothesis, not a measured allele effect. | missing | [E04](#e04), [E06](#e06) |
| element | The variant sits in an active pELS enhancer with DNase and H3K27ac signal, and SP1 occupies this base in HCT116, consistent with an SP1-responsive enhancer element. | supported | [E01](#e01), [E03](#e03), [E04](#e04), [E06](#e06) |
| gene | POU5F1B is the best L2G target and has a colon eQTL with alt T increasing POU5F1B (NES +0.20). In this chain, alt-T-enhanced SP1 binding would activate POU5F1B. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E18](#e18), [E20](#e20) |
| cell_type | HCT116 colorectal carcinoma is relevant because SP1 is expressed and bound there, and colon eQTL data link the variant to POU5F1B. | supported | [E06](#e06), [E17](#e17), [E20](#e20) |
| phenotype | The variant is strongly associated with colorectal cancer; this chain proposes that SP1-mediated activation of POU5F1B contributes to risk. | supported | [E15](#e15), [E16](#e16) |

Predictions: Allele-specific SP1 ChIP/CUT&RUN shows alt T > ref G SP1 occupancy at this base in HCT116.; SP1 knockdown reduces POU5F1B expression in colon epithelial cells.; The alt-T effect on POU5F1B is attenuated when the SP1 site is mutated.

Falsified if: Allele-specific assays show ref G binds SP1 more strongly than alt T.; SP1 knockdown does not reduce POU5F1B in HCT116.; SP1 occupancy at this exact base is absent or not reproducible in HCT116.

### 4. H3: YY1 repression at the 8q24 enhancer controls POU5F1B (p = 0.10)

TF YY1 (QBiC-SELEX coverage own_model), ref allele binds more; element pELS enhancer; gene POU5F1B; cell type colorectal carcinoma / HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | YY1 is a competing candidate: it is highly expressed in HCT116 (84.45 TPM, rank 34/1626) and has one ENCODE ChIP-seq peak containing the variant in HCT116 (E07). No QBiC-SELEX model or allele-specific data for YY1 is provided here; the claim that ref G binds YY1 more strongly than alt T is a hypothesis, not a measured allele effect. | missing | [E04](#e04), [E07](#e07) |
| element | The variant lies in an active pELS enhancer with DNase and H3K27ac signal, and YY1 occupies this base in HCT116, consistent with YY1 acting at this element. | supported | [E01](#e01), [E03](#e03), [E04](#e04), [E07](#e07) |
| gene | POU5F1B is the strongest L2G target and has a colon eQTL with alt T increasing POU5F1B (NES +0.20). In this chain, ref-G YY1 binding is repressive, so loss of YY1 binding on alt T de-represses POU5F1B. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E18](#e18), [E20](#e20) |
| cell_type | HCT116 colorectal carcinoma is relevant because YY1 is expressed and bound there, and colon eQTL data support POU5F1B as the target. | supported | [E07](#e07), [E17](#e17), [E20](#e20) |
| phenotype | The variant is strongly associated with colorectal cancer; this chain proposes that allele-specific YY1 repression of POU5F1B modifies colorectal cancer risk. | supported | [E15](#e15), [E16](#e16) |

Predictions: Allele-specific YY1 ChIP/CUT&RUN shows ref G > alt T YY1 occupancy at this base in HCT116.; YY1 knockdown increases POU5F1B expression in colon epithelial cells.; The alt-T increase in POU5F1B is reduced by restoring YY1 binding at the site.

Falsified if: Allele-specific assays show alt T binds YY1 more strongly than ref G.; YY1 knockdown decreases rather than increases POU5F1B in HCT116.; YY1 occupancy at this base is not reproducible in HCT116.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| QBiC-SELEX for TCF7L2 with ref-G versus alt-T oligos | low | yes | No significant allele-specific TCF7L2 binding for G vs T. | Ref G > alt T TCF7L2 binding. | No allele-specific TCF7L2 binding; SP1/YY1 hypotheses remain untested by this assay. | No allele-specific TCF7L2 binding; SP1/YY1 hypotheses remain untested by this assay. |
| Allele-specific TCF7L2 ChIP-qPCR/CUT&RUN at the variant in HCT116 or edited heterozygous clones | medium | yes | No reproducible allele-specific TCF7L2 occupancy at this base. | Ref G > alt T TCF7L2 occupancy at this base in HCT116. | No allele-specific TCF7L2 occupancy; SP1 alt-T occupancy would be the predicted effect. | No allele-specific TCF7L2 occupancy; YY1 ref-G occupancy would be the predicted effect. |
| TCF7L2 knockdown/CRISPRi in HCT116 followed by allele-specific POU5F1B expression | medium | yes | No allele-specific TCF7L2-dependent change in POU5F1B. | TCF7L2 loss increases POU5F1B and reduces the alt-T versus ref-G expression difference, consistent with TCF7L2 repression. | No TCF7L2-dependent POU5F1B change; SP1 perturbation is the relevant test. | No TCF7L2-dependent POU5F1B change; YY1 perturbation is the relevant test. |
| Allele-specific SP1 ChIP-qPCR/CUT&RUN at the variant in HCT116 | medium | no | No allele-specific SP1 occupancy at this base. | No allele-specific SP1 occupancy; TCF7L2 ref-G occupancy is the predicted effect. | Alt T > ref G SP1 occupancy at this base in HCT116. | No allele-specific SP1 occupancy; YY1 ref-G occupancy is the predicted effect. |
| Allele-specific YY1 ChIP-qPCR/CUT&RUN at the variant in HCT116 | medium | no | No allele-specific YY1 occupancy at this base. | No allele-specific YY1 occupancy; TCF7L2 ref-G occupancy is the predicted effect. | No allele-specific YY1 occupancy; SP1 alt-T occupancy is the predicted effect. | Ref G > alt T YY1 occupancy at this base in HCT116. |

## Next experiment

QBiC-SELEX for TCF7L2 with ref-G versus alt-T oligos. It is cheap and directly tests the top two chains H0 versus H1 at the binding link: H1 predicts ref G > alt T TCF7L2 binding, while H0 predicts no significant allele-specific TCF7L2 binding. A positive result would still need allele-specific ChIP/CUT&RUN in HCT116 to establish occupancy rather than in vitro binding alone.

## Investigate calls

- chip_peaks({"biosample": "HCT116", "tf": "TCF7L2"})
- eqtl_lookup({"tissue": "Colon - Transverse"})
- literature_search({"query": "rs6983267 TCF7L2 TCF4 binding risk allele 8q24 enhancer MYC colorectal cancer allele-specific"})

## Flags

- quote_rejected: PMID 42465001: not an exact substring of the abstract

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

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:21:59+00:00)

> Europe PMC: 150 hits for 'POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 42465001 (2026): Circ_0075829 affects POU5F1B expression through sponging miR-576-3p to promote growth, invasion, and angiogenesis of colon cancer cells.
> PMID 41993623 (2026): Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research.
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 41930642 (2026): Systematic Identification and Characterization of Causal Risk Genes Implicated in Colorectal Cancer by Integrating GWAS, eQTL, and mQTL Data.
> PMID 42686757 (2026): Phase separation of ecDNA condensates establishes in-trans contact domains that boost selective MYC regulatory interactions.
> PMID 40506516 (2025): Association between methylation quantitative trait loci and colorectal cancer risk, survival and cancer recurrence.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 41196428 (2025): Combined CHK1 and PD-L1 blockade as a novel therapeutic strategy against stemness and immunosuppression in ovarian cancer.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T16:35:30+00:00)

> 1 ENCODE TCF7L2 ChIP-seq peaks contain chr8:127401060:G>T in biosamples matching 'HCT116': biosamples HCT116; experiments ENCSR000EUV. In other biosamples, 3 TCF7L2 peaks do contain the variant: HepG2 (experiments ENCSR000EVQ, ENCSR346BOD).

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (T) relative to ref (G).
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

<a id="e21"></a>**E21** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20TCF7L2%20TCF4%20binding%20risk%20allele%208q24%20enhancer%20MYC%20colorectal%20cancer%20allele-specific&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:19:09+00:00)

> Europe PMC: 31 hits for 'rs[masked] TCF7L2 TCF4 binding risk allele 8q24 enhancer MYC colorectal cancer allele-specific'; top 8 with PMIDs:
> PMID 41655184 (2026): LncRNA CCAT2 role in female-related cancer progression and diagnosis: a comprehensive review.
> PMID 41310609 (2025): The CCAT2 enigma: pioneering insights into colorectal cancer pathophysiology and therapeutic innovation.
> PMID 39965570 (2025): An evolving understanding of multiple causal variants underlying genetic association signals.
> PMID 34429773 (2021): A nuclear polymorphism at the 8q24 region is associated with improved survival time and chemo-response in high-grade serous ovarian cancer.
> PMID 37443779 (2023): Rewired Metabolism Caused by the Oncogenic Deregulation of MYC as an Attractive Therapeutic Target in Cancers.
> PMID 32523949 (2020): Significance of Single-Nucleotide Variants in Long Intergenic Non-protein Coding RNAs.
> PMID 30170403 (2018): Cumulative evidence for relationships between multiple variants in 8q24 and colorectal cancer incidence.
> PMID 30470303 (2018): The MYC Enhancer-ome: Long-Range Transcriptional Regulation of MYC in Cancer.

<a id="e21a"></a>**E21a** literature_search, Europe PMC abstract, PMID 41310609 (https://europepmc.org/article/MED/41310609; retrieved 2026-10-26T20:19:09+00:00)

> Among these, the lncRNA colon cancer-associated transcript 2 (CCAT2) has recently been recognized as a critical driver of CRC growth and metastasis.

<a id="e21b"></a>**E21b** literature_search, Europe PMC abstract, PMID 41310609 (https://europepmc.org/article/MED/41310609; retrieved 2026-10-26T20:19:09+00:00)

> CCAT2 regulates gene expression and preserves chromosomal stability by modulating key oncogenic signaling pathways, including Wnt/β-catenin and MYC.

<a id="e21c"></a>**E21c** literature_search, Europe PMC abstract, PMID 39965570 (https://europepmc.org/article/MED/39965570; retrieved 2026-10-26T20:19:09+00:00)

> The experimental and analytical difficulty in identifying the "causal variant" among the co-inherited variants has traditionally led mechanistic studies to focus on relatively simple loci, where a single functional variant is presumed to explain most of the association signal and affect a target gene.

<a id="e21d"></a>**E21d** literature_search, Europe PMC abstract, PMID 39965570 (https://europepmc.org/article/MED/39965570; retrieved 2026-10-26T20:19:09+00:00)

> However, emerging evidence powered by high-throughput experimental tools and context-specific functional databases argues that even a single independent signal may involve multiple functional variants in strong LD, each contributing to the observed genetic association.

<a id="e21e"></a>**E21e** literature_search, Europe PMC abstract, PMID 34429773 (https://europepmc.org/article/MED/34429773; retrieved 2026-10-26T20:19:09+00:00)

> One single nucleotide polymorphism that is associated with ovarian cancer in this region is rs[masked], located within the long non-coding RNA colon cancer associated transcript 2 (CCAT2).

<a id="e21f"></a>**E21f** literature_search, Europe PMC abstract, PMID 34429773 (https://europepmc.org/article/MED/34429773; retrieved 2026-10-26T20:19:09+00:00)

> The results revealed that patients with HGSOC and the TT genotype at the rs[masked] locus had improved survival time compared with patients with genotypes containing a G allele [hazard ratio=0.59; 95% confidence interval (CI), 0.36-0.97; P=0.039] and were significantly associated with International Federation of Gynecology and Obstetrics stage [odds ratio (OR)=5.34; 95% CI, 1.50-22.62; P=0.014] and positive chemo-response (OR=4.51; 95% CI, 1.40-18.00; P=0.018).

<a id="e21g"></a>**E21g** literature_search, Europe PMC abstract, PMID 32523949 (https://europepmc.org/article/MED/32523949; retrieved 2026-10-26T20:19:09+00:00)

> Some pivotal variants may serve as risk factors for the development of various disorders, especially cancer.

<a id="e21h"></a>**E21h** literature_search, Europe PMC abstract, PMID 32523949 (https://europepmc.org/article/MED/32523949; retrieved 2026-10-26T20:19:09+00:00)

> They may also act as important regulatory signatures involved in the modulation of lincRNAs in a tissue- or disorder-specific manner.

<a id="e21i"></a>**E21i** literature_search, Europe PMC abstract, PMID 30170403 (https://europepmc.org/article/MED/30170403; retrieved 2026-10-26T20:19:09+00:00)

> In particular, both homozygous TT and heterozygous CT genotypes of rs[masked], as well as the GG and TG genotypes of rs[masked], were associated with risk of colorectal cancer.

<a id="e21j"></a>**E21j** literature_search, Europe PMC abstract, PMID 30170403 (https://europepmc.org/article/MED/30170403; retrieved 2026-10-26T20:19:09+00:00)

> Our study provides summary evidence that common variants in the 8q24 are associated with risk of colorectal cancer in this large-scale research synopsis and meta-analysis.

<a id="e21k"></a>**E21k** literature_search, Europe PMC abstract, PMID 30470303 (https://europepmc.org/article/MED/30470303; retrieved 2026-10-26T20:19:09+00:00)

> However, recent studies have identified numerous tissue-specific noncoding enhancers of MYC that play major roles in cancer, highlighting long-range transcriptional regulation of MYC as a critical novel mechanism leading to MYC hyperactivation and as a potential target for new therapeutic strategies in the near future.

<a id="e21l"></a>**E21l** literature_search, Europe PMC abstract, PMID 30470303 (https://europepmc.org/article/MED/30470303; retrieved 2026-10-26T20:19:09+00:00)

> Here we summarize the regions and mechanisms involved in the long-range transcriptional regulation of MYC, underscoring the relevance of MYC enhancers both in normal physiological development and in MYC-driven cancer initiation and progression.
