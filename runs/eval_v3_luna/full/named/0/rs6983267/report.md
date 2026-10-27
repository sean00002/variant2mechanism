# rs6983267 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 9 model calls; 0 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -4.66); SRF (bound here, z -7.74, weak site); SP1 (bound here, z -4.76, weak site); JUND (bound here, z -3.01, no clear allelic change, weak site); CEBPB (bound here, z 1.9, no clear allelic change, weak site); MAX (bound here, z -0.97, no clear allelic change, weak site); YY1 (bound here, z -0.43, no clear allelic change, weak site); HNF4A (bound elsewhere, z 53.69); GFI1 (bound elsewhere, z -31.27); NR2F2 (bound elsewhere, z 20.82). Occupancy unknown: ZNF493 (z -34.16); TBX19 (z 26.18); MBNL2 (z -22.42); NR1D1 (z 20.82); NR1D2 (z 20.82). Diagnostic, not shown to the model: 421 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: TCF7L2-associated enhancer effect on POU5F1B (p = 0.45)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element rs6983267 lies in the pELS cCRE EH38E3858447, a candidate enhancer.; gene POU5F1B; cell type Colorectal cancer cells; HCT116 is the directly supported occupancy context..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is a plausible, not uniquely established, TF candidate: it is expressed and occupies the variant in HCT116, and a LEF1-mapped QBiC-SELEX model predicts stronger binding to ref G than alt T at a strong modeled site. This is not a TCF7L2-specific QBiC-SELEX result. | weak | [E05](#e05), [E20](#e20), [E35](#e35) |
| element | The variant lies in pELS cCRE EH38E3858447; the reported chromatin maxima do not establish activity specifically in HCT116. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate target based on a T-increasing transverse-colon eQTL and gene-prioritization/TWAS evidence, but a direct link from this cCRE to POU5F1B is not shown. The eQTL direction would be compatible with the predicted lower TCF7L2 binding on T only if TCF7L2 represses POU5F1B; that regulatory sign is not established here. | weak | [E16](#e16), [E17](#e17), [E18b](#e18b) |
| cell_type | TCF7L2 occupancy over the variant is reported in HCT116; this supports that cell line as a test context, not a general claim about colorectal tumors or normal colon. | supported | [E05](#e05) |
| phenotype | rs6983267 is associated with colorectal cancer, and POU5F1B has been reported to promote CRC-cell proliferation and metastatic potential; the supplied evidence does not show that this variant acts through POU5F1B. | weak | [E15](#e15), [E18d](#e18d) |

Predictions: Allele-specific TCF7L2 occupancy at the site should favor G over T in HCT116, if the mapped QBiC-SELEX result reflects TCF7L2 binding there.; If this binding difference mediates the reported POU5F1B eQTL, T should increase POU5F1B relative to G; this requires a repressive effect of TCF7L2 that has not been demonstrated.; Editing the variant or perturbing TCF7L2 should alter POU5F1B regulation more than MYC regulation under this chain.

Falsified if: A sensitive allele-specific assay finds no G-favored TCF7L2 occupancy, or finds greater occupancy on T.; Precise editing or TCF7L2 perturbation has no effect on POU5F1B expression or enhancer activity in a relevant colorectal model.; The element reproducibly regulates MYC but not POU5F1B.

### 2. H4: Null: no TF-mediated effect of this variant (p = 0.36)

Null chain: no TF-mediated effect of this variant.

Predictions: The G/T substitution has no reproducible TF-mediated effect on enhancer activity or target-gene expression in relevant colorectal cells.; The CRC association may reflect linkage to another causal variant or a mechanism not mediated by TF binding at this base.

Falsified if: Precise G/T editing reproducibly changes TF occupancy and enhancer activity, with the effect depending on perturbation of the implicated TF.; The edited site produces a consistent allele-dependent change in a linked gene in a relevant colorectal model.

### 3. H3: SRF-associated enhancer effect on POU5F1B (p = 0.12)

TF SRF (QBiC-SELEX coverage own_model), ref allele binds more; element rs6983267 lies in the pELS cCRE EH38E3858447, hypothesized here to affect POU5F1B.; gene POU5F1B; cell type Colorectal cancer cells; HCT116 is the directly supported occupancy context..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SRF is a lower-confidence candidate: it is expressed and occupies the variant in HCT116, and its own QBiC-SELEX model predicts stronger binding to ref G. The modeled site is weak, so the ChIP peak may reflect binding elsewhere in the element rather than at this base. | supported | [E09](#e09), [E21](#e21) |
| element | The variant lies in pELS cCRE EH38E3858447; the reported chromatin maxima do not establish activity specifically in HCT116. | supported | [E03](#e03) |
| gene | POU5F1B is a candidate target based on the transverse-colon eQTL and gene-prioritization/TWAS evidence, but direct regulation by this element is unshown. | weak | [E16](#e16), [E17](#e17), [E18b](#e18b) |
| cell_type | SRF occupancy over the variant is reported in HCT116; this does not establish allele-specific function or activity across colorectal tissues. | supported | [E09](#e09) |
| phenotype | rs6983267 is associated with colorectal cancer, but a causal SRF-to-POU5F1B route is not demonstrated. | weak | [E15](#e15) |

Predictions: If SRF binding at this base mediates the effect, allele-specific SRF occupancy should favor G over T and SRF perturbation should reduce the allele-dependent POU5F1B effect.; The POU5F1B effect should depend more on SRF than on TCF7L2, distinguishing this chain from H1.; Because the modeled SRF site is weak, a robust absence of allele-specific SRF occupancy would weigh strongly against this chain.

Falsified if: Allele-specific assays find no SRF difference at the base or find greater occupancy on T.; SRF perturbation leaves the variant-dependent POU5F1B effect unchanged while TCF7L2 perturbation removes it.; Editing the variant does not alter POU5F1B expression or element activity in a relevant colorectal model.

### 4. H2: TCF7L2-associated enhancer effect on MYC (p = 0.07)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element rs6983267 lies in the pELS cCRE EH38E3858447, hypothesized here to regulate MYC.; gene MYC; cell type Colorectal cancer cells; HCT116 is the directly supported occupancy context..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is a plausible TF candidate because it is expressed and occupies the variant in HCT116. A LEF1-mapped QBiC-SELEX model predicts stronger binding to ref G, but does not establish TCF7L2-specific allelic binding. | weak | [E05](#e05), [E20](#e20), [E35](#e35) |
| element | The variant lies in pELS cCRE EH38E3858447; the reported biosample maxima do not establish activity in HCT116. | supported | [E03](#e03) |
| gene | MYC is a possible but weakly supported target: it is within 1 Mb, and MYC and POU5F1B were both identified in prostate cancer cell lines at this locus. The supplied gene-prioritization evidence favors POU5F1B, and no direct link from this element to MYC is shown. | weak | [E02](#e02), [E16](#e16), [E36e](#e36e) |
| cell_type | TCF7L2 occupancy over the variant is reported in HCT116, making this a testable model context. | supported | [E05](#e05) |
| phenotype | rs6983267 is associated with colorectal cancer, but the supplied evidence does not establish MYC as the mediator. | weak | [E15](#e15) |

Predictions: If the mapped binding prediction reflects TCF7L2 at this site, allele-specific occupancy should favor G over T in HCT116.; Editing the variant or perturbing the element should affect MYC regulation more than POU5F1B regulation under this chain.; A functional element-to-MYC connection should be detectable in the relevant colorectal context, rather than inferred from proximity alone.

Falsified if: Precise editing or element perturbation has no detectable effect on MYC in a relevant colorectal model.; The element reproducibly regulates POU5F1B but not MYC.; Allele-specific occupancy contradicts the predicted G-favored TCF7L2 binding.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| G/T allele-specific reporter assay in HCT116, with and without TCF7L2 depletion | low | yes | Predicts G-favored activity if TCF7L2 activates the reporter, or T-favored activity if it represses it; the allelic difference should diminish with TCF7L2 depletion. | Predicts no reproducible allele-dependent reporter activity or TCF7L2-dependent difference. | Does not specifically predict that the allelic reporter difference depends on TCF7L2. | Predicts a TCF7L2-dependent allele difference in reporter activity, but this assay alone does not identify MYC as the endogenous target. |
| Allele-specific TCF7L2 occupancy assay at rs6983267 in HCT116 | medium | yes | Predicts greater TCF7L2 occupancy on G than T, if the mapped QBiC-SELEX result applies to TCF7L2 at this site. | Predicts no reproducible allele-specific TCF7L2 occupancy difference. | Does not require an allele-specific TCF7L2 occupancy difference. | Predicts greater TCF7L2 occupancy on G than T, if the mapped result applies at this site. |
| Precise G/T editing in HCT116 followed by POU5F1B and MYC expression measurement | high | yes | Predicts an allele-dependent POU5F1B change; if it mediates the reported eQTL, T should increase expression relative to G. | Predicts no reproducible expression change attributable to the edited base. | Predicts an allele-dependent POU5F1B change that is SRF-dependent. | Predicts an allele-dependent MYC change more than a POU5F1B change. |
| Perturb EH38E3858447 and assay enhancer contacts or linked-gene expression | medium | yes | Predicts a functional connection to POU5F1B, potentially with a TCF7L2-dependent component. | Predicts no reproducible TF-mediated target-gene effect from perturbing this element. | Predicts a POU5F1B connection with an SRF-dependent component. | Predicts a functional connection to MYC rather than primarily POU5F1B. |

## Next experiment

Run a low-cost G/T allele-specific reporter assay in HCT116 with and without TCF7L2 depletion. H1 predicts an allele-dependent reporter effect that diminishes with TCF7L2 depletion; the null predicts no reproducible allele-dependent effect. Reporter results would be a first test, not proof of endogenous enhancer-to-gene regulation.

## Investigate calls

- qbic_tf_detail({"tf": "TCF7L2"})
- literature_search({"query": "rs6983267 colorectal cancer enhancer MYC POU5F1B functional variant target gene"})
- literature_search({"query": "rs6983267 POU5F1B enhancer colorectal cancer allele-specific expression"})

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

<a id="e36"></a>**E36** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20colorectal%20cancer%20enhancer%20MYC%20POU5F1B%20functional%20variant%20target%20gene&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:11:12+00:00)

> Europe PMC: 15 hits for 'rs6983267 colorectal cancer enhancer MYC POU5F1B functional variant target gene'; top 8 with PMIDs:
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 38670944 (2024): Fine-mapping analysis including over 254,000 East Asian and European descendants identifies 136 putative colorectal cancer susceptibility genes.
> PMID 36103972 (2022): Long non-coding RNA colon cancer-associated transcript 2: role and function in human cancers.
> PMID 34830370 (2021): The Roles of the Colon Cancer Associated Transcript 2 (CCAT2) Long Non-Coding RNA in Cancer: A Comprehensive Characterization of the Tumorigenic and Molecular Functions.
> PMID 26934861 (2016): 4C-seq revealed long-range interactions of a functional enhancer at the 8q24 prostate cancer risk locus.

<a id="e36a"></a>**E36a** literature_search, Europe PMC abstract, PMID 34830370 (https://europepmc.org/article/MED/34830370; retrieved 2026-10-26T13:11:12+00:00)

> The definitory mechanisms of CCAT2 are its role as a regulator of the TCF7L2 transcription factor, enhancer of MYC expression, and activator of the WNT/β-catenin pathway, as well as a role in promoting and maintaining chromosome instability through the BOP1-AURKB pathway.

<a id="e36b"></a>**E36b** literature_search, Europe PMC abstract, PMID 34830370 (https://europepmc.org/article/MED/34830370; retrieved 2026-10-26T13:11:12+00:00)

> Additionally, we highlight how the encompassing rs6983267 SNP has been shown to confer CCAT2 with allele-specific functional and structural particularities, such as the allelic-specific reprogramming of glutamine metabolism.

<a id="e36c"></a>**E36c** literature_search, Europe PMC abstract, PMID 39284974 (https://europepmc.org/article/MED/39284974; retrieved 2026-10-26T13:11:12+00:00)

> Here, we perform statistical fine-mapping incorporating tissue-specific epigenetic annotations and massively parallel reporter assays to systematically prioritize functional variants for each CRC risk locus.

<a id="e36d"></a>**E36d** literature_search, Europe PMC abstract, PMID 39284974 (https://europepmc.org/article/MED/39284974; retrieved 2026-10-26T13:11:12+00:00)

> We link these variants to 208 target genes by analyzing colon-specific quantitative trait loci and implementing the activity-by-contact model, which integrates epigenomic features and Micro-C data, to predict enhancer-gene connections.

<a id="e36e"></a>**E36e** literature_search, Europe PMC abstract, PMID 26934861 (https://europepmc.org/article/MED/26934861; retrieved 2026-10-26T13:11:12+00:00)

> Common genes (e.g. MYC and POU5F1B) were identified in both prostate cancer cell lines.

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20POU5F1B%20enhancer%20colorectal%20cancer%20allele-specific%20expression&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:11:21+00:00)

> Europe PMC: 26 hits for 'rs6983267 POU5F1B enhancer colorectal cancer allele-specific expression'; top 8 with PMIDs:
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 38670944 (2024): Fine-mapping analysis including over 254,000 East Asian and European descendants identifies 136 putative colorectal cancer susceptibility genes.
> PMID 36103972 (2022): Long non-coding RNA colon cancer-associated transcript 2: role and function in human cancers.
> PMID 34830370 (2021): The Roles of the Colon Cancer Associated Transcript 2 (CCAT2) Long Non-Coding RNA in Cancer: A Comprehensive Characterization of the Tumorigenic and Molecular Functions.
> PMID 34199840 (2021): Role of Long Non-Coding RNA Polymorphisms in Cancer Chemotherapeutic Response.
> PMID 30794691 (2019): The Crohn's disease associated SNP rs6651252 impacts MYC gene expression in human colonic epithelial cells.

<a id="e37a"></a>**E37a** literature_search, Europe PMC abstract, PMID 34830370 (https://europepmc.org/article/MED/34830370; retrieved 2026-10-26T13:11:21+00:00)

> Additionally, we highlight how the encompassing rs6983267 SNP has been shown to confer CCAT2 with allele-specific functional and structural particularities, such as the allelic-specific reprogramming of glutamine metabolism.
