# rs6983267 and Colorectal cancer (8q24)

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 9 model calls; 184 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H1: No TF-mediated effect at this variant (p = 0.62)

Null chain: no TF-mediated effect of this variant.

Predictions: There will be no reproducible, variant-dependent TF-binding effect that explains a change in POU5F1B expression.; The colorectal-cancer association may reflect linkage or another mechanism not mediated by TF binding at this base.

Falsified if: Changing G to T reproducibly alters binding of a TF at this site and produces a corresponding TF-dependent change in POU5F1B expression.

### 2. H2: TCF7L2-mediated effect at the enhancer-like element, with POU5F1B as a candidate target (p = 0.16)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is a candidate because it is expressed in HCT116 and has ChIP-seq peaks overlapping the variant there. Alt (T) is a working direction for this hypothesis, not an observed binding effect: no QBiC-SELEX result or allele-specific binding result is supplied. | weak | [E04](#e04), [E05](#e05) |
| element | The variant overlaps the pELS cCRE EH38E3858447, with DNase and H3K27ac signal among ENCODE biosamples; the supplied maxima do not establish activity of this element in HCT116. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is a plausible, not established, target: T is associated with higher POU5F1B expression in transverse colon, and POU5F1B has the strongest L2G score in the listed sets, but the L2G evidence is predominantly prostate-related and no evidence directly connects this cCRE to the gene. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | TCF7L2 occupancy overlapping the variant is reported in HCT116; this supports occupancy in this cell line, not an allele-specific effect. | supported | [E05](#e05) |
| phenotype | T is reported as the risk allele in a colorectal-cancer association, although other listed colorectal or colon traits report G as the effect allele. POU5F1B has some gene-level colorectal-cancer support, but its cited functional literature concerns a different regulatory mechanism; a TCF7L2-mediated route from this variant to disease is unproven. | weak | [E15](#e15), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E20](#e20) |

Predictions: A controlled comparison of G and T will show a reproducible TCF7L2-binding difference at this sequence, with the working prediction that T binds more strongly.; If this chain is correct, disrupting TCF7L2 or the variant-containing element will alter POU5F1B expression in an appropriate colorectal context.

Falsified if: A sensitive controlled assay finds no G-versus-T difference in TCF7L2 binding, and TCF7L2 or element perturbation does not affect POU5F1B expression.

### 3. H3: SP1-mediated effect at the enhancer-like element, with POU5F1B as a candidate target (p = 0.14)

TF SP1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 is a candidate because it is expressed in HCT116 and has ChIP-seq peaks overlapping the variant there. Alt (T) is a working direction for this hypothesis, not an observed binding effect: no QBiC-SELEX result or allele-specific binding result is supplied. | weak | [E04](#e04), [E06](#e06) |
| element | The variant overlaps the pELS cCRE EH38E3858447, with DNase and H3K27ac signal among ENCODE biosamples; the supplied maxima do not establish activity of this element in HCT116. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is a plausible, not established, target: T is associated with higher POU5F1B expression in transverse colon, and POU5F1B has the strongest L2G score in the listed sets, but the L2G evidence is predominantly prostate-related and no evidence directly connects this cCRE to the gene. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | SP1 occupancy overlapping the variant is reported in HCT116; this supports occupancy in this cell line, not an allele-specific effect. | supported | [E06](#e06) |
| phenotype | T is reported as the risk allele in a colorectal-cancer association, although other listed colorectal or colon traits report G as the effect allele. Gene-level POU5F1B support and literature about a different regulatory mechanism do not establish an SP1-mediated route from this variant to disease. | weak | [E15](#e15), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E20](#e20) |

Predictions: A controlled comparison of G and T will show a reproducible SP1-binding difference at this sequence, with the working prediction that T binds more strongly.; If this chain is correct, SP1 or element perturbation will alter the variant-associated change in POU5F1B expression.

Falsified if: A sensitive controlled assay finds no G-versus-T difference in SP1 binding, and SP1 or element perturbation does not affect POU5F1B expression.

### 4. H4: YY1-mediated effect at the enhancer-like element, with POU5F1B as a candidate target (p = 0.08)

TF YY1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | YY1 is a candidate because it is expressed in HCT116 and has a ChIP-seq peak overlapping the variant there. Alt (T) is a working direction for this hypothesis, not an observed binding effect: no QBiC-SELEX result or allele-specific binding result is supplied. The single reported HCT116 peak does not distinguish YY1 as causal. | weak | [E04](#e04), [E07](#e07) |
| element | The variant overlaps the pELS cCRE EH38E3858447, with DNase and H3K27ac signal among ENCODE biosamples; the supplied maxima do not establish activity of this element in HCT116. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is a plausible, not established, target: T is associated with higher POU5F1B expression in transverse colon, and POU5F1B has the strongest L2G score in the listed sets, but the L2G evidence is predominantly prostate-related and no evidence directly connects this cCRE to the gene. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | YY1 occupancy overlapping the variant is reported in HCT116; this supports occupancy in this cell line, not an allele-specific effect. | supported | [E07](#e07) |
| phenotype | T is reported as the risk allele in a colorectal-cancer association, although other listed colorectal or colon traits report G as the effect allele. Gene-level POU5F1B support and literature about a different regulatory mechanism do not establish a YY1-mediated route from this variant to disease. | weak | [E15](#e15), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E20](#e20) |

Predictions: A controlled comparison of G and T will show a reproducible YY1-binding difference at this sequence, with the working prediction that T binds more strongly.; If this chain is correct, YY1 or element perturbation will alter the variant-associated change in POU5F1B expression.

Falsified if: A sensitive controlled assay finds no G-versus-T difference in YY1 binding, and YY1 or element perturbation does not affect POU5F1B expression.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 EMSA using G and T probes with a TCF7L2 supershift or equivalent specificity control | low | yes | No reproducible TCF7L2 binding difference between the probes. | Reproducible TCF7L2 binding difference between the probes, with the working prediction that T binds more strongly. | No TCF7L2 binding difference that explains the proposed SP1-mediated chain. | No TCF7L2 binding difference that explains the proposed YY1-mediated chain. |
| Compare allele-specific TCF7L2, SP1, and YY1 occupancy at the locus in HCT116, with adequate controls for allele representation | medium | no | No reproducible variant-linked allelic occupancy difference for the proposed TFs. | A TCF7L2 allelic occupancy difference supports H2 more than the SP1 or YY1 alternatives. | An SP1 allelic occupancy difference supports H3 more than the TCF7L2 or YY1 alternatives. | A YY1 allelic occupancy difference supports H4 more than the TCF7L2 or SP1 alternatives. |
| Perturb EH38E3858447 in a colorectal model and measure POU5F1B expression, with a matched control region | medium | no | No reproducible POU5F1B change attributable to perturbing this element. | Element perturbation changes POU5F1B expression; this alone does not identify TCF7L2 as the mediator. | Element perturbation changes POU5F1B expression; this alone does not identify SP1 as the mediator. | Element perturbation changes POU5F1B expression; this alone does not identify YY1 as the mediator. |

## Next experiment

The cheapest direct test of the top two chains (H1 null versus H2 TCF7L2) is an allele-specific TCF7L2 EMSA using G and T probes with a TCF7L2 specificity control. A differential result would support sequence-dependent binding, but would not by itself establish chromatin occupancy, regulation of POU5F1B, or disease causality.

## Investigate calls

- literature_search({"query": "chr8:127401060 colorectal cancer allele-specific enhancer TCF7L2 SP1 YY1"})
- gene_disease({"gene": "POU5F1B"})
- eqtl_lookup({"tissue": "Colon - Transverse"})

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

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 42465001 (https://europepmc.org/article/MED/42465001; retrieved 2026-10-26T02:21:59+00:00)

> Circ_0075829 acted as a molecular sponge for microRNA-576-3p (miR-576-3p), thereby upregulating the expression of POU class 5 homeobox 1B (POU5F1B) in colon cancer cells.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 42465001 (https://europepmc.org/article/MED/42465001; retrieved 2026-10-26T02:21:59+00:00)

> Collectively, circ_0075829 promotes proliferation, invasion, and angiogenesis, while inhibiting apoptosis in colon cancer by modulating POU5F1B levels through miR-576-3p sponging.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 41930642 (https://europepmc.org/article/MED/41930642; retrieved 2026-10-26T02:21:59+00:00)

> A few potential regulatory influences on CRC development associated with genes and variants, such as POU5F1B and rs[masked], were identified.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 40506516 (https://europepmc.org/article/MED/40506516; retrieved 2026-10-26T02:21:59+00:00)

> Four regions mapped to POU5F1B, POU2AF2 (c11orf53)/POU2AF3 (COLCA2), GREM1 and CABLES2 were previously identified.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr8%3A127401060%20colorectal%20cancer%20allele-specific%20enhancer%20TCF7L2%20SP1%20YY1&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:18:14+00:00)

> Europe PMC: 0 hits for 'chr8:127401060 colorectal cancer allele-specific enhancer TCF7L2 SP1 YY1'; top 0 with PMIDs:

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14

<a id="e21"></a>**E21** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (T) relative to ref (G).
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06
