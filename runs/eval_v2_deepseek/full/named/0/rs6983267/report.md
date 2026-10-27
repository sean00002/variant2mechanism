# rs6983267 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 9 model calls; 0 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: SRF (bound here, z -7.74); SP1 (bound here, z -4.76); TCF7L2 (bound here, z -4.66); JUND (bound here, z -3.01, no clear allelic change); CEBPB (bound here, z 1.9, no clear allelic change); MAX (bound here, z -0.97, no clear allelic change); YY1 (bound here, z -0.43, no clear allelic change); HNF4A (bound elsewhere, z 53.69); GFI1 (bound elsewhere, z -31.27); NR2F2 (bound elsewhere, z 20.82). Occupancy unknown: ZNF493 (z -34.16); TBX19 (z 26.18); MBNL2 (z -22.42); NR1D1 (z 20.82); NR1D2 (z 20.82). Diagnostic, not shown to the model: 421 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated allelic effect; the variant is a linked or passenger marker (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-specific TF occupancy is not detected at chr8:127401060.; Allele-specific enhancer reporter activity is not detected.; Any ChIP peak over the variant reflects element occupancy rather than an allelic effect.

Falsified if: Allele-specific binding of a candidate TF is validated at the variant.; Allele-specific enhancer reporter activity is demonstrated.; A causal variant elsewhere in the credible set fails to explain the signal.

### 2. H4: TCF7L2 binds the ref G allele and activates CCAT2 to promote colorectal cancer (p = 0.30)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element pELS EH38E3858447; gene CCAT2; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref G allele more strongly than the alt T allele. TCF7L2 has HCT116 ChIP-seq occupancy over the variant (E05) and is highly expressed in HCT116. TCF7L2 has no own QBiC-SELEX model in this evidence set, so the mapped LEF1 row is not used as own-model allelic evidence. The ref>alt direction is inferred from the literature linking rs6983267/8q24 to allele-specific TCF7L2 binding (E37) and from the CCAT2-TCF7L2-MYC literature (E37a), not from an own-model QBiC measurement. | weak | [E05](#e05), [E37](#e37), [E37a](#e37a) |
| element | The variant lies in proximal enhancer-like cCRE EH38E3858447 with DNase and H3K27ac signal, and TCF7L2 occupancy overlaps this element in HCT116 (E03, E04, E05). The ENCODE z-scores are maxima over biosamples, so the HCT116-specific chromatin state is inferred from the HCT116 ChIP context rather than directly stated in E03. | weak | [E03](#e03), [E04](#e04), [E05](#e05) |
| gene | CCAT2 is directly overlapped by the variant (E01), and literature places CCAT2 as a TCF7L2 regulator and enhancer of MYC/Wnt with allele-specific features at rs6983267 (E37a, E37b). No CCAT2 eQTL in colon or HCT116 is provided, so this gene link is literature- and overlap-based rather than expression-QTL-based. | weak | [E01](#e01), [E37a](#e37a), [E37b](#e37b) |
| cell_type | HCT116 colorectal cancer cells have open chromatin context at the variant and TCF7L2 occupancy over it (E04, E05). | supported | [E04](#e04), [E05](#e05) |
| phenotype | The locus is associated with colorectal cancer (E15). Several E15 CRC records report G as the effect allele (colorectal cancer or advanced adenoma p 3.0e-64; colon polyps; PheCode 153.2), while the strongest CRC record reports T (p 2.0e-122), so the risk-allele direction is not fully resolved. If G is the risk allele, stronger TCF7L2 binding on G raising CCAT2 and downstream MYC/Wnt is a coherent mechanism (E37a). | weak | [E15](#e15), [E37a](#e37a) |

Predictions: The G allele shows stronger TCF7L2 occupancy at chr8:127401060 in HCT116.; The G allele gives higher CCAT2 expression in colorectal cells.; TCF7L2 knockdown lowers CCAT2 expression.

Falsified if: No allele-specific TCF7L2 occupancy is detected at the variant.; CCAT2 expression is not allele-specific or not TCF7L2-responsive in colorectal cells.; G is not the colorectal cancer risk allele in the relevant colorectal context.

### 3. H1: SRF binds the ref G allele and represses POU5F1B at the 8q24 enhancer (p = 0.22)

TF SRF (QBiC-SELEX coverage own_model), ref allele binds more; element pELS EH38E3858447; gene POU5F1B; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SRF binds the ref G allele more strongly than the alt T allele. SRF has HCT116 ENCODE ChIP-seq occupancy over the variant (E09) and an own QBiC-SELEX model showing ref>alt binding above the gate (z -7.74, effect -1.191; E20), with SRF expressed in HCT116 (25.61 TPM; E20). QBiC-SELEX is in vitro, so allele-specific occupancy in HCT116 remains a prediction. | supported | [E09](#e09), [E20](#e20) |
| element | The variant lies in proximal enhancer-like cCRE EH38E3858447 with DNase and H3K27ac signal, and active-element ChIP factors are present over the element in HCT116 (E03, E04). E03 z-scores are maxima over biosamples, not HCT116-specific. | weak | [E03](#e03), [E04](#e04) |
| gene | POU5F1B has a colon transverse eQTL in which the alt T allele increases expression (NES +0.20; E17) and is TWAS-implicated in colorectal cancer (E18b); POU5F1B is also oncogenic in CRC models (E18c, E18d). The L2G score of 0.89 is driven mainly by prostate-cancer and PSA credible sets, not CRC, and no chromatin contact in HCT116 links this element to POU5F1B. | weak | [E16](#e16), [E17](#e17), [E18b](#e18b), [E18c](#e18c), [E18d](#e18d) |
| cell_type | HCT116 colorectal cancer cells have open chromatin context at the variant and SRF occupancy over it (E04, E09). | supported | [E04](#e04), [E09](#e09) |
| phenotype | The strongest CRC GWAS record reports T as the effect allele (E15), and the T allele raises POU5F1B in colon transverse (E17); POU5F1B is oncogenic (E18d). This chain therefore requires SRF to repress POU5F1B so that loss of SRF binding on T raises POU5F1B and risk. Other E15 CRC records report G as the effect allele, so the risk-allele direction is not fully resolved. | weak | [E15](#e15), [E17](#e17), [E18d](#e18d) |

Predictions: The G allele shows stronger SRF occupancy at chr8:127401060 in HCT116.; POU5F1B expression is higher on the T allele if SRF represses POU5F1B.; SRF knockdown increases POU5F1B expression in colorectal cells.

Falsified if: No allele-specific SRF occupancy is detected at the variant.; POU5F1B expression is not higher on the T allele in colorectal cells.; SRF acts as an activator rather than a repressor at this element.

### 4. H2: SP1 binds the ref G allele and activates CASC8 at the 8q24 enhancer (p = 0.08)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element pELS EH38E3858447; gene CASC8; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 binds the ref G allele more strongly than the alt T allele, but this allelic claim is weak. SP1 has HCT116 ChIP-seq occupancy over the variant (E06), but its own QBiC-SELEX model is below the gate (effect -0.169, z -3.04; E36), and the gate-passing row is a CIS-BP-mapped SP4 model rather than an SP1 own-model measurement. I therefore treat the allelic direction as weak, occupancy-supported but not established. | weak | [E06](#e06), [E36](#e36) |
| element | The variant lies in pELS EH38E3858447 with enhancer chromatin marks, and SP1 occupancy overlaps the element in HCT116 (E03, E04, E06). E03 z-scores are maxima over biosamples. | weak | [E03](#e03), [E04](#e04), [E06](#e06) |
| gene | The variant is an intronic CASC8 variant (E01), and CASC8 has a significant whole-blood eQTL where the alt T allele decreases expression (NES -0.32; E17). No colon or HCT116 CASC8 eQTL or chromatin-contact evidence links this element to CASC8. | weak | [E01](#e01), [E17](#e17) |
| cell_type | HCT116 colorectal cancer cells have open chromatin context at the variant and SP1 occupancy over it (E04, E06). | supported | [E04](#e04), [E06](#e06) |
| phenotype | This chain requires T to be the colorectal cancer risk allele and SP1 to activate CASC8, with lower CASC8 increasing risk. The T-risk direction is supported by the strongest CRC record but contradicted by several other E15 CRC records with G as effect allele, and no evidence supports a protective role for CASC8. | weak | [E15](#e15), [E17](#e17) |

Predictions: The G allele shows stronger SP1 occupancy at chr8:127401060 in HCT116.; CASC8 expression is higher on the G allele and lower on the T allele.; SP1 knockdown reduces CASC8 expression.

Falsified if: No allele-specific SP1 occupancy is detected at the variant.; CASC8 expression does not track the SP1-bound allele.; SP1 knockdown does not affect CASC8 expression.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H4 | H1 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 ChIP-qPCR at rs6983267 in HCT116 | low | yes | No allelic difference in TCF7L2 occupancy | G > T TCF7L2 occupancy at the variant | No TCF7L2 allelic difference; SRF, not TCF7L2, is the candidate | No TCF7L2 allelic difference |
| Allele-specific SRF ChIP-qPCR at rs6983267 in HCT116 | low | no | No allelic difference in SRF occupancy | No SRF allelic difference | G > T SRF occupancy at the variant | No SRF allelic difference |
| POU5F1B allele-specific expression in HCT116 or colon tissue | medium | no | No allele-specific POU5F1B expression | No allele-specific POU5F1B expression | T allele gives higher POU5F1B expression | No allele-specific POU5F1B expression |
| CCAT2 allele-specific expression and TCF7L2 knockdown in HCT116 | high | yes | No allele-specific CCAT2 expression and no TCF7L2 response | G allele gives higher CCAT2 expression and TCF7L2 knockdown lowers CCAT2 | No CCAT2 allele-specific expression | No CCAT2 allele-specific expression |
| Enhancer reporter with ref G vs alt T in HCT116 | medium | yes | G and T alleles have equal activity | G allele has higher enhancer activity | T allele has higher activity if SRF represses | G allele has higher activity if SP1 activates |
| Allele-specific SP1 ChIP-qPCR at rs6983267 in HCT116 | low | no | No allelic difference | No SP1 allelic difference | No SP1 allelic difference | G > T SP1 occupancy |

## Next experiment

Allele-specific TCF7L2 ChIP-qPCR in HCT116: immunoprecipitate TCF7L2, then quantify ref G vs alt T at rs6983267 with allele-specific qPCR/ddPCR. Cost: $$.

## Investigate calls

- eqtl_lookup({"tissue": "Colon_Transverse"})
- qbic_tf_detail({"tf": "SP1"})
- literature_search({"query": "rs6983267 allele-specific TCF7L2 binding 8q24 enhancer MYC reporter colorectal"})

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

> QBiC-SELEX screen of chr8:127401060:G>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 64 occupied, 5 of 133 with unknown occupancy. Left out: 6 TFs assayed in the matching biosample and 497 assayed only elsewhere, none with a peak here; 6 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SRF (MADS box, 1 model; QBiC-SELEX coverage: own model): best model SRF_eDBD_TGCCAC40NGCC_KR_yin2017_0_3_7mer (its own model), z -7.74, effect -1.191: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 25.61 TPM, rank 217 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSC. Best model's site strength: ref 95.1th, alt 91.3th percentile of its k-mer coefficients.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): best model SP4_NA_TTATGT20NGTA_ESAE_yang2017_0_3_7mer (a CIS-BP-mapped model of SP4), z -4.76, effect -0.211: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 38.96 TPM, rank 118 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSF. Best model's site strength: ref 95.8th, alt 75.9th percentile of its k-mer coefficients.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer (a CIS-BP-mapped model of LEF1), z -4.66, effect -0.47: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 63.61 TPM, rank 53 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000EUV. Best model's site strength: ref 98.8th, alt 98.4th percentile of its k-mer coefficients.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUND (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUN_FL_TCAGTG40NGAT_KAE_yin2017_0_3_7mer (a CIS-BP-mapped model of JUN), z -3.01, effect -0.059: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 18.66 TPM, rank 300 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSA. Best model's site strength: ref 89.3th, alt 96.8th percentile of its k-mer coefficients.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPB (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (its own model), z 1.9, effect 0.205: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 13.15 TPM, rank 408 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSD. Best model's site strength: ref 75.7th, alt 85.6th percentile of its k-mer coefficients.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z -0.97, effect -0.058: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 42.59 TPM, rank 102 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSH. Best model's site strength: ref 91.8th, alt 95.3th percentile of its k-mer coefficients.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> YY1 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model YY1_FL_GG40NGTGAGA_YWKA_jolma2025_0_3_7mer (its own model), z -0.43, effect -0.033: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 84.45 TPM, rank 34 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BNX. Best model's site strength: ref 91.3th, alt 88.8th percentile of its k-mer coefficients.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF4A (Nuclear receptor, 1 model; QBiC-SELEX coverage: own model): best model TLX_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2E1), z 53.69, effect 1.968: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.95 TPM, rank 850 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, liver, e.g. ENCSR445QRF. Best model's site strength: ref 96.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GFI1 (C2H2 ZF, 2 models; QBiC-SELEX coverage: own model): best model GFI1B_eDBD_TTCTCA40NCCT_KR_yin2017_0_3_7mer (a CIS-BP-mapped model of GFI1B), z -31.27, effect -2.144: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.9 TPM, rank 857 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR849FVL. Best model's site strength: ref 99.9th, alt 99.6th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 61.74 TPM, rank 58 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BVM. Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients.

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

<a id="e35"></a>**E35** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38 in tissues matching 'Colon_Transverse'. NES is the effect of the alt allele (T) relative to ref (G).
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

<a id="e36"></a>**E36** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"SP1","symbol":"SP1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr8:127401060:G>T","gate_p":5.02e-05,"models":[{"model":"SP1_eDBD_TCTCTA40NCAC_KV_yin2017_0_3_7mer","mapping":"own","group":"G015 C2H2 ZF, 5 models","quality":0.891,"effect":-0.169,"z":-3.04,"p":0.0024,"rank_abs_z":"539/997","passed_gate":false,"site_strength":{"ref_percentile":95.4,"alt_percentile":93.6,"k":7}},{"model":"SP3_eDBD_TTCACC40NGCT_KR_yin2017_0_3_7mer","mapping":"CIS-BP (SP3)","group":"G015 C2H2 ZF, 5 models","quality":0.813,"effect":-0.119,"z":-2.52,"p":0.012,"rank_abs_z":"606/997","passed_gate":false,"site_strength":{"ref_percentile":70.1,"alt_percentile":75.3,"k":7}},{"model":"SP4_NA_TTATGT20NGTA_ESAE_yang2017_0_3_7mer","mapping":"CIS-BP (SP4)","group":"G015 C2H2 ZF, 5 models","quality":0.825,"effect":-0.211,"z":-4.76,"p":1.9e-06,"rank_abs_z":"344/997","passed_gate":true,"site_strength":{"ref_percentile":95.8,"alt_percentile":75.9,"k":7}},{"model":"SP8_NA_TGCTCG20NCTC_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (SP8)","group":"G015 C2H2 ZF, 5 models","quality":0.672,"effect":0.189,"z":2.99,"p":0.0028,"rank_abs_z":"545/997","passed_gate":false,"site_strength":{"ref_percentile":91.2,"alt_percentile":92.4,"k":7}},{"model":"SP9_eDBD_TACCGA40NATA_KP_yin2017_0_4_7mer","mapping":"CIS-BP (SP9)","group":"G015 C2H2 ZF, 5 models","quality":0.936,"effect":-0.228,"z":-2.8,"p":0.0051,"rank_abs_z":"571/997","passed_gate":false,"site_strength":{"ref_percentile":94.1,"alt_percentile":97.2,"k":7}}]}

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20allele-specific%20TCF7L2%20binding%208q24%20enhancer%20MYC%20reporter%20colorectal&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:15:49+00:00)

> Europe PMC: 28 hits for 'rs6983267 allele-specific TCF7L2 binding 8q24 enhancer MYC reporter colorectal'; top 8 with PMIDs:
> PMID 41719390 (2026): Systematic analysis of functional genetic and epigenetic variants in colorectal cancer.
> PMID 39965570 (2025): An evolving understanding of multiple causal variants underlying genetic association signals.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 36103972 (2022): Long non-coding RNA colon cancer-associated transcript 2: role and function in human cancers.
> PMID 34830370 (2021): The Roles of the Colon Cancer Associated Transcript 2 (CCAT2) Long Non-Coding RNA in Cancer: A Comprehensive Characterization of the Tumorigenic and Molecular Functions.
> PMID 32523949 (2020): Significance of Single-Nucleotide Variants in Long Intergenic Non-protein Coding RNAs.
> PMID 30794691 (2019): The Crohn's disease associated SNP rs6651252 impacts MYC gene expression in human colonic epithelial cells.
> PMID 30470303 (2018): The MYC Enhancer-ome: Long-Range Transcriptional Regulation of MYC in Cancer.

<a id="e37a"></a>**E37a** literature_search, Europe PMC abstract, PMID 34830370 (https://europepmc.org/article/MED/34830370; retrieved 2026-10-26T02:15:49+00:00)

> The definitory mechanisms of CCAT2 are its role as a regulator of the TCF7L2 transcription factor, enhancer of MYC expression, and activator of the WNT/β-catenin pathway, as well as a role in promoting and maintaining chromosome instability through the BOP1-AURKB pathway.

<a id="e37b"></a>**E37b** literature_search, Europe PMC abstract, PMID 34830370 (https://europepmc.org/article/MED/34830370; retrieved 2026-10-26T02:15:49+00:00)

> Additionally, we highlight how the encompassing rs6983267 SNP has been shown to confer CCAT2 with allele-specific functional and structural particularities, such as the allelic-specific reprogramming of glutamine metabolism.

<a id="e37c"></a>**E37c** literature_search, Europe PMC abstract, PMID 30794691 (https://europepmc.org/article/MED/30794691; retrieved 2026-10-26T02:15:49+00:00)

> We demonstrate that rs6651252 resides within a Wnt responsive DNA enhancer element (WRE) and that the disease associated allele augments binding of the TCF7L2 transcription factor to this region.

<a id="e37d"></a>**E37d** literature_search, Europe PMC abstract, PMID 30794691 (https://europepmc.org/article/MED/30794691; retrieved 2026-10-26T02:15:49+00:00)

> Using CRISPR/Cas9 directed gene editing and epigenetic modulation, we find that the rs6651252 enhancer regulates expression of the c-MYC proto-oncogene (MYC).

<a id="e37e"></a>**E37e** literature_search, Europe PMC abstract, PMID 30470303 (https://europepmc.org/article/MED/30470303; retrieved 2026-10-26T02:15:49+00:00)

> However, recent studies have identified numerous tissue-specific noncoding enhancers of MYC that play major roles in cancer, highlighting long-range transcriptional regulation of MYC as a critical novel mechanism leading to MYC hyperactivation and as a potential target for new therapeutic strategies in the near future.
