# rs6983267 and Colorectal cancer (8q24)

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 9 model calls; 340 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H1: Null: no TF-mediated effect of rs6983267 (p = 0.62)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing rs6983267 alone will not reproducibly change allele-specific TF occupancy or produce a linked change in target-gene expression or CRC-relevant phenotype.

Falsified if: Isogenic editing of rs6983267 reproducibly changes TF occupancy and a downstream expression or functional readout in a manner attributable to the edited base.

### 2. H2: TCF7L2-mediated regulation of POU5F1B (p = 0.22)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element EH38E3858447 pELS cCRE; gene POU5F1B; cell type HCT116 for observed TCF7L2 occupancy; a relevant colonic context for the reported POU5F1B eQTL.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies the variant in HCT116 and is expressed there; ref-G-preferential binding is only a provisional prediction, not a measured allelic effect. No QBiC-SELEX result is supplied. TCF7L2 is retained as a candidate because it is directly occupied in HCT116, but SP1 also has occupancy evidence and the distinction is weak. | weak | [E05](#e05), [E06](#e06) |
| element | The variant overlaps the pELS cCRE EH38E3858447; the supplied chromatin scores are maxima across biosamples and do not establish enhancer activity in HCT116. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate target supported indirectly by a positive T-allele eQTL in transverse colon and CRC-related gene-prioritization evidence, but none shows that this element or TCF7L2 regulates POU5F1B. | weak | [E16](#e16), [E17](#e17), [E18b](#e18b), [E20](#e20) |
| cell_type | TCF7L2 occupancy is reported in HCT116, and the POU5F1B eQTL is reported in transverse colon; neither result establishes the complete regulatory route in those contexts. | supported | [E05](#e05), [E17](#e17) |
| phenotype | rs6983267 is associated with CRC, and POU5F1B has CRC-related evidence, but the supplied evidence does not show that TCF7L2-mediated regulation of POU5F1B explains the association. | weak | [E15](#e15), [E18a](#e18a), [E18d](#e18d), [E20](#e20) |

Predictions: Allele-specific TCF7L2 occupancy will favor ref G; this is a hypothesis to test, not a direction supported by the supplied evidence.; Editing rs6983267 will alter POU5F1B expression; if it follows the reported transverse-colon eQTL direction, the T allele will increase expression.

Falsified if: A well-powered allele-specific assay finds no TCF7L2 occupancy imbalance or finds stronger occupancy on alt T.; Isogenic editing produces no reproducible POU5F1B expression change in an appropriate colonic context.

### 3. H3: TCF7L2-mediated regulation of MYC (p = 0.10)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element EH38E3858447 pELS cCRE; gene MYC; cell type HCT116 for observed TCF7L2 occupancy; MYC regulation in this context is unshown.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies the variant in HCT116. Ref-G-preferential binding is a provisional prediction only; no allele-specific binding or QBiC-SELEX result is supplied. | weak | [E05](#e05) |
| element | The variant overlaps pELS cCRE EH38E3858447, but the evidence does not establish activity in HCT116 or a connection to MYC. | supported | [E03](#e03) |
| gene | MYC is a nearby candidate, but proximity is indirect and the supplied gene-prioritization evidence favors POU5F1B over MYC. | weak | [E02](#e02), [E16](#e16), [E21](#e21) |
| cell_type | TCF7L2 occupancy at the variant is reported in HCT116; MYC regulation by this element in those cells is not shown. | supported | [E05](#e05) |
| phenotype | The variant is associated with CRC and MYC has CRC-related evidence, but the supplied data do not connect this variant, element, and TF to MYC-mediated risk. | weak | [E15](#e15), [E21](#e21) |

Predictions: Allele-specific TCF7L2 occupancy will favor ref G; this predicted direction is unmeasured.; Editing rs6983267 will alter MYC expression or its contact with the element, without requiring a POU5F1B expression change; the direction of any MYC expression change is not established.

Falsified if: Allele-specific assays show no TCF7L2 occupancy imbalance or show stronger occupancy on alt T.; Isogenic editing and TCF7L2 perturbation show no rs6983267-dependent effect on MYC expression or enhancer contact in relevant cells.

### 4. H4: SP1-mediated regulation of POU5F1B (p = 0.06)

TF SP1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447 pELS cCRE; gene POU5F1B; cell type HCT116 for observed SP1 occupancy; a relevant colonic context for the reported POU5F1B eQTL.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 occupies the variant in HCT116 and is expressed there. Alt-T-preferential binding is a provisional prediction only; no allele-specific binding or QBiC-SELEX result is supplied. SP1 remains an alternative to TCF7L2, not a better-supported causal factor. | weak | [E06](#e06) |
| element | The variant overlaps pELS cCRE EH38E3858447; the supplied chromatin scores do not establish activity in HCT116. | supported | [E03](#e03) |
| gene | POU5F1B is an indirect candidate target based on its transverse-colon eQTL and CRC-related prioritization, but these data do not show SP1 regulation from this element. | weak | [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | SP1 occupancy is reported in HCT116; SP1-dependent POU5F1B regulation in HCT116 or colon is not shown. | supported | [E06](#e06) |
| phenotype | rs6983267 is associated with CRC, but the supplied evidence does not connect the association to an SP1-to-POU5F1B regulatory route. | weak | [E15](#e15), [E18a](#e18a), [E20](#e20) |

Predictions: Allele-specific SP1 occupancy will favor alt T; this is a hypothesis to test, not a measured direction.; SP1 perturbation and editing rs6983267 will jointly affect POU5F1B expression if this route is correct; the direction is not established by the supplied evidence.

Falsified if: A well-powered allele-specific assay finds no SP1 occupancy imbalance or finds stronger occupancy on ref G.; SP1 perturbation and isogenic editing show no rs6983267-dependent effect on POU5F1B expression.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 occupancy at rs6983267 in heterozygous HCT116 cells, using phased ChIP-qPCR or CUT&RUN reads. | low | yes | No reproducible occupancy imbalance attributable to rs6983267. | Ref-G-enriched TCF7L2 occupancy. | Ref-G-enriched TCF7L2 occupancy. | No required TCF7L2 imbalance; this chain instead predicts an SP1 effect. |
| Isogenic G-to-T and T-to-G editing in HCT116, followed by POU5F1B and MYC expression measurement. | medium | yes | No reproducible allele-dependent expression change in either gene. | POU5F1B changes; if concordant with the reported colon eQTL, T increases expression. | MYC changes; the direction is not specified by the supplied evidence. | POU5F1B changes in an SP1-dependent manner; the direction is not specified. |
| Allele-specific SP1 occupancy at rs6983267 in heterozygous HCT116 cells, followed by SP1 perturbation. | medium | no | No reproducible SP1 imbalance or rs6983267-dependent SP1 effect. | No SP1 imbalance is required; a TCF7L2-dependent effect is predicted instead. | No SP1 imbalance is required; a TCF7L2-dependent effect is predicted instead. | Alt-T-enriched SP1 occupancy and an SP1-dependent POU5F1B effect. |
| Isogenic editing with TCF7L2 perturbation and measurement of enhancer contact and MYC/POU5F1B expression. | high | yes | No reproducible allele-dependent, TCF7L2-dependent contact or expression effect. | A TCF7L2-dependent POU5F1B effect, with T predicted to increase expression if concordant with the reported eQTL. | A TCF7L2-dependent MYC effect; expression direction is unspecified. | No required TCF7L2-dependent effect; an SP1-dependent POU5F1B effect is predicted instead. |

## Next experiment

Perform allele-specific TCF7L2 ChIP-qPCR or CUT&RUN in heterozygous HCT116 cells, using phased reads across rs6983267. This is the cheapest proposed test that directly distinguishes the top-ranked null from H2; a ref-G occupancy bias would support H2's binding prediction, while no bias would weaken it.

## Investigate calls

- literature_search({"query": "rs6983267 allele-specific enhancer target gene TCF7L2 SP1 MYC POU5F1B colorectal cancer functional assay"})
- gene_disease({"gene": "POU5F1B"})
- gene_disease({"gene": "MYC"})

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

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20allele-specific%20enhancer%20target%20gene%20TCF7L2%20SP1%20MYC%20POU5F1B%20colorectal%20cancer%20functional%20assay&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:22:57+00:00)

> Europe PMC: 2 hits for 'rs6983267 allele-specific enhancer target gene TCF7L2 SP1 MYC POU5F1B colorectal cancer functional assay'; top 2 with PMIDs:
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 27379672 (2016): Fine-Mapping of Common Genetic Variants Associated with Colorectal Tumor Risk Identified Potential Functional Variants.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 39284974 (https://europepmc.org/article/MED/39284974; retrieved 2026-10-26T13:22:57+00:00)

> We link these variants to 208 target genes by analyzing colon-specific quantitative trait loci and implementing the activity-by-contact model, which integrates epigenomic features and Micro-C data, to predict enhancer-gene connections.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 27379672 (https://europepmc.org/article/MED/27379672; retrieved 2026-10-26T13:22:57+00:00)

> Bioinformatics analysis of SNPs showing smaller P-values in each region revealed 21 functional candidates in 12 loci (5q31.1, 8q24, 11q13.4, 11q23, 12p13.32, 12q24.21, 14q22.2, 15q13, 18q21, 19q13.1, 20p12.3, and 20q13.33).

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14

<a id="e21"></a>**E21** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T13:23:01+00:00)

> Open Targets: MYC and colorectal cancer (MONDO_0005575), overall score 0.12; by evidence type: literature 0.89, genetic_association 0.05
