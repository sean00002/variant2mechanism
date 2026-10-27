# rs6983267 and Colorectal cancer (8q24)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 279 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H1: TCF7L2-bound 8q24 enhancer represses POU5F1B; alt T loses repression and raises CRC risk (p = 0.36)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element pELS enhancer containing rs6983267; gene POU5F1B; cell type colorectal cancer cells (HCT116/colon).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is occupied over the variant in HCT116 and is highly expressed (E05), making it a leading candidate; however, there is no QBiC-SELEX model or allele-specific occupancy assay for TCF7L2 here, so the ref-G > alt-T binding direction is assumed, not measured. E04 shows many other expressed TFs also bound, so occupancy alone does not uniquely select TCF7L2. | weak | [E04](#e04), [E05](#e05) |
| element | rs6983267 lies in the ENSR8_CGMBX enhancer and in pELS EH38E3858447, which has DNase and H3K27ac signal consistent with an active enhancer. | supported | [E01](#e01), [E03](#e03) |
| gene | The variant-bearing enhancer is assigned to POU5F1B: POU5F1B is 78.9 kb away/in the gene body, has the best L2G score (0.89), and shows a significant colon eQTL in which alt T increases POU5F1B expression (NES +0.20). | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | The mechanism is relevant to colorectal cells: TCF7L2 is occupied at the variant in HCT116, the element is a pELS, and the POU5F1B eQTL evidence comes from colon tissue. | supported | [E03](#e03), [E04](#e04), [E05](#e05), [E17](#e17) |
| phenotype | The top CRC association in E15 uses effect allele T, and alt T increases POU5F1B in colon (E17/E20), while POU5F1B has been reported to promote CRC growth/metastasis (E18d). But allele direction is heterogeneous across CRC/colon traits in E15 and POU5F1B is not a common essential in bowel lines (E21), so the phenotype step is plausible but weak. | weak | [E15](#e15), [E17](#e17), [E18d](#e18d), [E21](#e21) |

Predictions: TCF7L2 ChIP/EMSA at rs6983267 shows stronger binding on ref G than alt T in colorectal cells.; TCF7L2 knockdown or CRISPRi increases POU5F1B expression, consistent with repression.; The alt T allele associates with higher POU5F1B expression in colon tissue.; The rs6983267 element physically contacts the POU5F1B promoter or gene body in colorectal cells.

Falsified if: TCF7L2 occupancy is not allele-specific at rs6983267 or is stronger on alt T rather than ref G.; TCF7L2 loss decreases or does not change POU5F1B expression rather than increasing it.; The element does not contact POU5F1B in colorectal cells.

### 2. H0: Null: no TF-mediated allelic effect at rs6983267 (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at the variant after controlling for linked variants.; The CRC association is explained by a linked causal variant in the 8q24 enhancer cluster rather than rs6983267 itself.; rs6983267 behaves as a passenger or marker SNP with no measurable allelic effect on POU5F1B, MYC, or other nearby targets.

Falsified if: A robust allele-specific TF binding assay shows differential occupancy at rs6983267.; Allele-specific expression or reporter assays show that rs6983267 itself changes a target gene in colorectal cells.; Fine-mapping excludes linked variants and leaves rs6983267 as the causal variant.

### 3. H3: SP1 binds the alt T allele and activates POU5F1B (p = 0.17)

TF SP1 (QBiC-SELEX coverage own_model), alt allele binds more; element pELS enhancer containing rs6983267; gene POU5F1B; cell type colorectal cancer cells (HCT116/colon).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 is occupied over the variant in HCT116 and expressed there (E06), but no QBiC-SELEX model or allele-specific assay is provided; alt-T > ref-G SP1 binding is inferred from the alt-T POU5F1B eQTL and is not measured. E04 shows other bound TFs, so this TF choice is not uniquely supported. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies in an active pELS enhancer, EH38E3858447, within the ENSR8_CGMBX enhancer, with DNase and H3K27ac signal. | supported | [E01](#e01), [E03](#e03) |
| gene | The enhancer is linked to POU5F1B by proximity/gene-body location, best L2G score 0.89, and a colon eQTL in which alt T increases POU5F1B. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | SP1 is occupied at the variant in HCT116 and the POU5F1B eQTL is from colon tissue, supporting relevance to colorectal cells. | supported | [E04](#e04), [E06](#e06), [E17](#e17) |
| phenotype | Alt T is the strongest CRC effect allele in E15, increases POU5F1B in colon, and POU5F1B has been reported to promote CRC. However, allele direction is heterogeneous across E15 CRC/colon entries and POU5F1B is not a common essential in bowel lines (E21), so the phenotype link is weak. | weak | [E15](#e15), [E17](#e17), [E18d](#e18d), [E21](#e21) |

Predictions: SP1 ChIP/EMSA at rs6983267 shows stronger binding on alt T than ref G.; SP1 knockdown reduces POU5F1B expression in colorectal cells.; The alt T allele increases POU5F1B expression in colon tissue.; The SP1-bound element contacts POU5F1B.

Falsified if: SP1 binding is not allele-specific at rs6983267.; SP1 knockdown does not affect POU5F1B.; SP1 occupancy is weaker on alt T than ref G.

### 4. H4: YY1 binds the ref G allele and represses POU5F1B; alt T loses repression (p = 0.12)

TF YY1 (QBiC-SELEX coverage own_model), ref allele binds more; element pELS enhancer containing rs6983267; gene POU5F1B; cell type colorectal cancer cells (HCT116/colon).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | YY1 is occupied over the variant in HCT116 and is highly expressed (E07), but no QBiC-SELEX model or allele-specific assay is provided; ref-G > alt-T YY1 binding and a repressive role are assumptions. E04 shows many other bound TFs. | weak | [E04](#e04), [E07](#e07) |
| element | The variant lies in the active pELS EH38E3858447 within the ENSR8_CGMBX enhancer. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is the best-supported target by proximity/gene-body location, L2G 0.89, and the colon eQTL showing alt T increases POU5F1B. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | YY1 is occupied at the variant in HCT116 and the target eQTL is in colon tissue. | supported | [E04](#e04), [E07](#e07), [E17](#e17) |
| phenotype | If ref-G-bound YY1 represses POU5F1B, alt T would derepress POU5F1B; alt T is the strongest CRC effect allele in E15 and POU5F1B has been reported to promote CRC. But the repressor role is unmeasured, E15 allele direction is heterogeneous, and POU5F1B is not a common essential in bowel lines (E21), so this phenotype link is weak. | weak | [E15](#e15), [E17](#e17), [E18d](#e18d), [E21](#e21) |

Predictions: YY1 ChIP/EMSA at rs6983267 shows stronger binding on ref G than alt T.; YY1 knockdown increases POU5F1B expression, consistent with repression.; The alt T allele has lower YY1 occupancy and higher POU5F1B expression in colon.; The YY1-bound element contacts POU5F1B.

Falsified if: YY1 binding is not allele-specific at rs6983267.; YY1 loss decreases rather than increases POU5F1B.; The alt T allele does not show higher POU5F1B expression.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 binding at rs6983267 (EMSA or ChIP-qPCR in HCT116/colorectal cells), ref G vs alt T | low | yes | TCF7L2 binds ref G more than alt T | No allele-specific TCF7L2 binding | No TCF7L2 allelic difference (SP1 is the proposed factor) | No TCF7L2 allelic difference |
| Allele-specific SP1 binding at rs6983267, ref G vs alt T | low | no | No SP1 allelic difference or SP1 is not the proposed mechanism | No allele-specific SP1 binding | SP1 binds alt T more than ref G | No SP1 allelic difference |
| Allele-specific YY1 binding at rs6983267, ref G vs alt T | low | no | No YY1 allelic difference | No allele-specific YY1 binding | No YY1 allelic difference | YY1 binds ref G more than alt T |
| Allele-specific POU5F1B expression/reporter assay in colorectal cells, ref G vs alt T | medium | yes | Alt T gives higher POU5F1B expression/activity (derepression) | No allelic effect on POU5F1B | Alt T gives higher POU5F1B expression/activity (SP1 activation) | Alt T gives higher POU5F1B expression/activity (loss of YY1 repression) |
| TCF7L2 knockdown or CRISPRi, measure POU5F1B in colorectal cells | medium | yes | TCF7L2 loss increases POU5F1B expression | No change in POU5F1B | No change or SP1-dependent change in POU5F1B | No change in POU5F1B |
| Chromatin contact (3C/Hi-C) between the rs6983267 element and POU5F1B promoter | medium | no | Contact present | Contact may be present but is not allele-specific | Contact present | Contact present |

## Next experiment

Allele-specific TCF7L2 binding assay at rs6983267 (EMSA with ref-G and alt-T oligos, or allele-specific ChIP-qPCR in a heterozygous colorectal line). H1 predicts ref G > alt T TCF7L2 binding; H0 predicts no allelic difference.

## Investigate calls

- literature_search({"query": "rs6983267 allele-specific TCF7L2 binding colorectal enhancer reporter assay"})
- eqtl_lookup({"tissue": "Colon - Transverse"})
- gene_dependency({"gene": "POU5F1B"})

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

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20allele-specific%20TCF7L2%20binding%20colorectal%20enhancer%20reporter%20assay&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:25:44+00:00)

> Europe PMC: 30 hits for 'rs6983267 allele-specific TCF7L2 binding colorectal enhancer reporter assay'; top 8 with PMIDs:
> PMID 41719390 (2026): Systematic analysis of functional genetic and epigenetic variants in colorectal cancer.
> PMID 39965570 (2025): An evolving understanding of multiple causal variants underlying genetic association signals.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 34830370 (2021): The Roles of the Colon Cancer Associated Transcript 2 (CCAT2) Long Non-Coding RNA in Cancer: A Comprehensive Characterization of the Tumorigenic and Molecular Functions.
> PMID 36103972 (2022): Long non-coding RNA colon cancer-associated transcript 2: role and function in human cancers.
> PMID 34358319 (2021): Wnt target enhancer regulation by a CDX/TCF transcription factor collective and a novel DNA motif.
> PMID 32523949 (2020): Significance of Single-Nucleotide Variants in Long Intergenic Non-protein Coding RNAs.
> PMID 30794691 (2019): The Crohn's disease associated SNP rs6651252 impacts MYC gene expression in human colonic epithelial cells.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 41719390 (https://europepmc.org/article/MED/41719390; retrieved 2026-10-26T02:25:44+00:00)

> In this study, we adapted and applied two high-throughput techniques, SNP-STARR-seq and Methyl-STARR-seq, to systematically evaluate the influence of 30,790 noncoding SNPs and more than 134,000 CpG sites on enhancer activity in primary and metastatic CRC cells.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 39284974 (https://europepmc.org/article/MED/39284974; retrieved 2026-10-26T02:25:44+00:00)

> Here, we perform statistical fine-mapping incorporating tissue-specific epigenetic annotations and massively parallel reporter assays to systematically prioritize functional variants for each CRC risk locus.

<a id="e19c"></a>**E19c** literature_search, Europe PMC abstract, PMID 34830370 (https://europepmc.org/article/MED/34830370; retrieved 2026-10-26T02:25:44+00:00)

> The definitory mechanisms of CCAT2 are its role as a regulator of the TCF7L2 transcription factor, enhancer of MYC expression, and activator of the WNT/β-catenin pathway, as well as a role in promoting and maintaining chromosome instability through the BOP1-AURKB pathway.

<a id="e19d"></a>**E19d** literature_search, Europe PMC abstract, PMID 34830370 (https://europepmc.org/article/MED/34830370; retrieved 2026-10-26T02:25:44+00:00)

> Additionally, we highlight how the encompassing rs6983267 SNP has been shown to confer CCAT2 with allele-specific functional and structural particularities, such as the allelic-specific reprogramming of glutamine metabolism.

<a id="e19e"></a>**E19e** literature_search, Europe PMC abstract, PMID 34358319 (https://europepmc.org/article/MED/34358319; retrieved 2026-10-26T02:25:44+00:00)

> Transcriptional regulation by Wnt signalling is primarily thought to be accomplished by a complex of β-catenin and TCF family transcription factors (TFs).

<a id="e19f"></a>**E19f** literature_search, Europe PMC abstract, PMID 34358319 (https://europepmc.org/article/MED/34358319; retrieved 2026-10-26T02:25:44+00:00)

> We characterised a Wnt-responsive element (WRE) downstream of the Wnt target gene Axin2 and found that TCFs and Caudal type homeobox (CDX) proteins were required for its activation.

<a id="e19g"></a>**E19g** literature_search, Europe PMC abstract, PMID 30794691 (https://europepmc.org/article/MED/30794691; retrieved 2026-10-26T02:25:44+00:00)

> We demonstrate that rs6651252 resides within a Wnt responsive DNA enhancer element (WRE) and that the disease associated allele augments binding of the TCF7L2 transcription factor to this region.

<a id="e19h"></a>**E19h** literature_search, Europe PMC abstract, PMID 30794691 (https://europepmc.org/article/MED/30794691; retrieved 2026-10-26T02:25:44+00:00)

> Using CRISPR/Cas9 directed gene editing and epigenetic modulation, we find that the rs6651252 enhancer regulates expression of the c-MYC proto-oncogene (MYC).

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (T) relative to ref (G).
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

<a id="e21"></a>**E21** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for POU5F1B (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): -0.09. Bowel lineage, 31 lines: median -0.06, 0% dependent. All 351 lines: median -0.05, 3% dependent.
