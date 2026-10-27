# rs6983267 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 8 model calls; 1 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen

421 of 997 models pass the gate. Top groups: Nuclear receptor, 1 model (best NR2E1, z 53.69); C2H2 ZF, 1 model (best ZNF493, z -34.16); C2H2 ZF, 2 models (best GFI1B, z -31.27); T-box, 2 models (best TBX19, z 26.18); C2H2 ZF, 1 model (best ZBTB43, z -23.26).

## Ranked chains

### 1. H0: Null: no TF-mediated allelic effect at rs6983267 (p = 0.36)

Null chain: no TF-mediated effect of this variant.

Predictions: There is no allele-specific TF occupancy at rs6983267 that changes enhancer activity in colorectal cells.; The colorectal cancer association is explained by a linked causal variant, a passenger event, or another non-TF mechanism at 8q24.; QBiC-SELEX binding differences at the site do not translate into a functional allele-specific effect in the relevant cell type.

Falsified if: A robust allele-specific TF occupancy and enhancer activity difference is demonstrated at rs6983267 in colorectal cells.; Perturbing that TF changes the expected target gene and a colorectal cancer-relevant phenotype.

### 2. H5: NR2F6 binds the alt T allele at the 8q24 pELS and activates POU5F1B in colorectal cells (p = 0.32)

TF NR2F6 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NR2F6 has its own QBiC-SELEX model in group G002 (best model z 20.82, effect +1.92), predicting that the alt T allele binds NR2F6 more strongly; NR2F6 is expressed at 37.02 TPM in the supplied HCT116 context. This is an in vitro binding prediction, not allele-specific ChIP evidence. | weak | [E14](#e14) |
| element | rs6983267 lies in the proximal enhancer-like cCRE EH38E3858447 with DNase and H3K27ac signal consistent with an active enhancer. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is the nearest protein-coding gene, has the strongest supplied L2G score, is a TWAS candidate with CRC growth/metastasis literature support, and the alt T allele is associated with higher POU5F1B expression in Colon-Transverse (NES +0.20); direct enhancer-POU5F1B contact is not shown. | weak | [E02](#e02), [E05](#e05), [E06b](#e06b), [E06c](#e06c), [E06d](#e06d), [E20](#e20) |
| cell_type | NR2F6 is expressed at 37.02 TPM in the supplied HCT116 colorectal cancer expression context, supporting this cell type as a relevant test system. | supported | [E14](#e14) |
| phenotype | The variant is strongly associated with colorectal cancer at 8q24.21; the strongest CRC GWAS row lists effect allele T, and the alt T allele is associated with higher POU5F1B in colon transverse, but effect alleles across colon phenotypes are mixed. | supported | [E04](#e04), [E06a](#e06a), [E20](#e20) |

Predictions: The alt T allele shows stronger NR2F6 binding than the ref G allele at rs6983267.; NR2F6 occupies the EH38E3858447 enhancer in colorectal cells and NR2F6 perturbation changes POU5F1B expression.; An allele-specific enhancer reporter shows higher alt-T activity in an NR2F6-dependent manner.

Falsified if: NR2F6 does not bind the variant allele-specifically in colorectal cells.; The alt T allele does not increase NR2F6 occupancy or NR2F6-dependent enhancer activity.; NR2F6 perturbation does not change POU5F1B expression or the enhancer reporter.

### 3. H1: TCF7L2 occupies the 8q24 pELS in HCT116; proposed ref-G binding and MYC regulation (p = 0.19)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element EH38E3858447 pELS; gene MYC; cell type colorectal epithelial/cancer cells (HCT116 context).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | An ENCODE TCF7L2 ChIP-seq peak in HCT116 contains chr8:127401060:G>T, supporting TCF7L2 occupancy at the element, but this does not establish allele specificity. The chain proposes that the ref G allele binds TCF7L2 more strongly; no TCF7L2 QBiC-SELEX row or qbic_tf_detail lookup is supplied, so QBiC coverage is not_checked and no QBiC direction is claimed. | weak | [E19](#e19) |
| element | rs6983267 lies in the proximal enhancer-like cCRE EH38E3858447 with DNase and H3K27ac signal consistent with an active enhancer. | supported | [E01](#e01), [E03](#e03) |
| gene | MYC lies about 334 kb upstream and is a plausible 8q24 target, but no 3D contact, reporter, CRISPR, or allele-specific assay links this enhancer to MYC. | weak | [E02](#e02) |
| cell_type | HCT116 is the supplied DepMap expression context and has a TCF7L2 ChIP-seq peak containing the variant, supporting HCT116 as a relevant colorectal model, though TCF7L2 expression is not quantified in the supplied evidence. | weak | [E07](#e07), [E19](#e19) |
| phenotype | The variant is strongly associated with colorectal cancer at 8q24.21, but the strongest CRC row lists effect allele T whereas some colon rows list G, creating direction tension with a ref-G TCF7L2-binding/MYC-raising model. | weak | [E04](#e04), [E06a](#e06a) |

Predictions: TCF7L2 occupies chr8:127401060 in HCT116, consistent with the ENCODE peak.; If allele-specific, the ref G allele shows stronger TCF7L2 binding than the alt T allele.; TCF7L2 perturbation reduces MYC enhancer activity or MYC expression in colorectal cells.

Falsified if: TCF7L2 does not occupy the variant-containing element allele-specifically in colorectal cells.; The ref G allele does not increase TCF7L2 occupancy or MYC enhancer activity.; TCF7L2 perturbation does not change MYC expression or the enhancer reporter.

### 4. H3: GFI1 binds the ref G allele at the pELS and may repress POU5F1B (p = 0.13)

TF GFI1 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GFI1 has its own QBiC-SELEX model in group G071 and passes with the same sign as the best model (GFI1 z -29.52), meaning the alt T allele binds less and the ref G allele binds more; GFI1 is expressed at 2.9 TPM in the supplied HCT116 context. This is an in vitro binding prediction, not allele-specific ChIP evidence. | weak | [E10](#e10) |
| element | rs6983267 lies in the proximal enhancer-like cCRE EH38E3858447. | supported | [E03](#e03) |
| gene | POU5F1B is the nearest protein-coding gene and has the strongest supplied L2G score; the alt T allele is associated with higher POU5F1B expression in Colon-Transverse, but no evidence directly links GFI1 occupancy at this enhancer to POU5F1B regulation. | weak | [E02](#e02), [E05](#e05), [E20](#e20) |
| cell_type | GFI1 is expressed at 2.9 TPM in the supplied HCT116 expression context, making this chain testable in colorectal cancer cells. | supported | [E10](#e10) |
| phenotype | The variant is associated with colorectal cancer and colon phenotypes, but effect alleles are mixed across traits and the GFI1-dependent direction is not established. | weak | [E04](#e04) |

Predictions: The ref G allele shows stronger GFI1 binding than the alt T allele.; GFI1 occupancy at the enhancer is detectable in colorectal cells and GFI1 perturbation changes POU5F1B expression.; If GFI1 represses, the ref G allele gives lower enhancer output and the alt T allele gives higher POU5F1B.

Falsified if: GFI1 does not bind the variant allele-specifically.; The ref G allele does not increase GFI1 occupancy.; GFI1 perturbation has no effect on POU5F1B expression or the enhancer reporter.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H5 | H1 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific NR2F6 ChIP-qPCR at rs6983267 in a heterozygous colorectal line | low | yes |  |  |  |  |
| Allele-specific TCF7L2 ChIP-qPCR at rs6983267 in HCT116 | low | no |  |  |  |  |
| Allelic enhancer reporter with NR2F6 knockdown/overexpression | medium | yes |  |  |  |  |
| POU5F1B expression after NR2F6 perturbation in colorectal cells | medium | yes |  |  |  |  |
| CRISPR deletion of the EH38E3858447 enhancer with POU5F1B and MYC expression readout | high | yes |  |  |  |  |

## Next experiment

Allele-specific NR2F6 ChIP-qPCR at rs6983267 in HCT116 or another heterozygous colorectal cancer line; H5 predicts alt T > ref G occupancy, while H0 predicts no allele-specific NR2F6 occupancy.

## Investigate calls

- qbic_tf_detail({"tf": "HNF4A"})
- chip_peaks({"tf": "TCF7L2", "biosample": "HCT116"})
- eqtl_lookup({"tissue": "Colon - Transverse"})

## Flags

- coverage_misstated: H1: stated not_checked, registry says mapped for TCF7L2

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs6983267&size=100; retrieved 2026-10-25T16:33:55+00:00)

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

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T16:33:46+00:00)

> 92 credible sets contain 8_127401060_G_T: 91 GWAS, 1 molecular QTL.
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Cancer of prostate (PheCode 185): PIP 1.00; L2G POU5F1B 0.82
> GWAS Elevated prostate specific antigen [PSA] (PheCode 796): PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> sceqtl for PVT1 (OTAR2057_IBDverse_ge_Colon_Goblet_MUC2+_SPDEF+_ENS): PIP 0.95
> Best L2G gene scores across these sets: POU5F1B 0.89, MYC 0.05

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20AND%20POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T16:33:56+00:00)

> Europe PMC: 52 hits for 'rs6983267 AND POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 35812248 (2022): Genome-Wide Association and Transcriptome-Wide Association Studies Identify Novel Susceptibility Genes Contributing to Colorectal Cancer.
> PMID 35987910 (2022): Transposon-activated POU5F1B promotes colorectal cancer growth and metastasis.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 39921239 (2025): System genetic analysis of intestinal cancer and periodontitis development as influenced by aging and diabesity using Collaborative Cross mice.
> PMID 36103972 (2022): Long non-coding RNA colon cancer-associated transcript 2: role and function in human cancers.
> PMID 34594420 (2021): Repurposing non-invasive prenatal testing data: Population study of single nucleotide variants associated with colorectal cancer and Lynch syndrome.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 35812248 (https://europepmc.org/article/MED/35812248; retrieved 2026-10-25T16:33:56+00:00)

> In the post-GWAS analyses, we first identified new genome-wide significant associations: three genomic risk loci were identified at 8q24.21 (rs6983267, P = 6.98 × 10-12), 15q13.3 (rs58658771, P = 1.40 × 10-10), and 18q21.1 (rs6507874, P = 1.91 × 10-14).

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 35812248 (https://europepmc.org/article/MED/35812248; retrieved 2026-10-25T16:33:56+00:00)

> In addition, the TWAS also identified four loci statistically significantly associated with CRC risk, largely explained by expression regulation, including six candidate genes (DUSP10, POU5F1B, C11orf53, COLCA1, COLCA2, and GREM1-AS1).

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 35987910 (https://europepmc.org/article/MED/35987910; retrieved 2026-10-25T16:33:56+00:00)

> Here, upon characterizing cancer-specific transposable element-driven transpochimeric gene transcripts (TcGTs) produced by this tumor in the SYSCOL cohort, we find that expression of the hominid-restricted retrogene POU5F1B through aberrant activation of a primate-specific endogenous retroviral promoter is a strong negative prognostic biomarker.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 35987910 (https://europepmc.org/article/MED/35987910; retrieved 2026-10-25T16:33:56+00:00)

> Correlating this observation, we demonstrate that POU5F1B fosters the proliferation and metastatic potential of CRC cells.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:127401060:G>T: 997 models scored, 421 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 348 CIS-BP groups. Expression context: DepMap line ACH-000971. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 79 (C2H2 ZF, 1 model z -47.51, C2H2 ZF, 1 model z 44.45, IRF, 2 models z 24.49, Nuclear receptor, 1 model z 21.74, C2H2 ZF, 1 model z -14.52). Passing groups ranked below the ones shown: 259. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G372 (Nuclear receptor, 1 model): best model TLX_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (own model of NR2E1), z 53.69, effect 1.968 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: NR2E1 z 53.69. TFs this group covers: HNF4A (own model) 2.95 TPM, HNF4G (own model) 2.24 TPM, NR2E1 (own model) 0.0 TPM; best model's site strength: ref 96.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G521 (C2H2 ZF, 1 model): best model ZNF493_FL_TG40NTCTTGC_YWRA_jolma2025_0_2_7mer (own model of ZNF493), z -34.16, effect -0.598 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF493 z -34.16. TFs this group covers: ZNF493 (own model) 1.33 TPM; best model's site strength: ref 100.0th, alt 88.9th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G071 (C2H2 ZF, 2 models): best model GFI1B_eDBD_TTCTCA40NCCT_KR_yin2017_0_3_7mer (own model of GFI1B), z -31.27, effect -2.144 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: GFI1B z -31.27, GFI1 z -29.52. TFs this group covers: GFI1 (own model) 2.9 TPM, GFI1B (own model) 0.05 TPM; best model's site strength: ref 99.9th, alt 99.6th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G101 (T-box, 2 models): best model TBX19_eDBD_TCTTGT40NCAG_KP_yin2017_0_4_7mer (own model of TBX19), z 26.18, effect 4.18 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: TBX19 z 26.18, TBXT z 11.73. TFs this group covers: TBX19 (own model) 1.92 TPM, TBXT (own model) 0.0 TPM; best model's site strength: ref 79.0th, alt 99.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G404 (C2H2 ZF, 1 model): best model ZBTB43_eDBD_TACGGT40NTAC_KR_yin2017_0_3_7mer (own model of ZBTB43), z -23.26, effect -1.724 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB43 z -23.26. TFs this group covers: ZBTB43 (own model) 8.32 TPM; best model's site strength: ref 99.8th, alt 87.9th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G233 (CCCH ZF, 1 model): best model MBNL2_FL_TCTAAG40NTTA_KZ_yin2017_0_4_7mer (own model of MBNL2), z -22.42, effect -2.708 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: MBNL2 z -22.42. TFs this group covers: MBNL2 (own model) 26.09 TPM; best model's site strength: ref 99.1th, alt 51.1th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G002 (Nuclear receptor, 29 models): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (own model of NR2F6), z 20.82, effect 1.92 (alt binds more); 11 passing models (9 with the best model's sign); members disagree on direction. Passing members: NR2F6 z 20.82, NR2C1 z 7.56, THRA z 7.37, NR2C2 z -6.01, NR4A1 z 6.0 (+6 more). TFs this group covers: NR2F2 (own model) 61.74 TPM, PPARG (own model) 47.9 TPM, ESRRA (own model) 38.54 TPM, NR1D2 (own model) 37.06 TPM, NR2F6 (own model) 37.02 TPM, RARG (own model) 31.32 TPM, NR2F1 (own model) 28.42 TPM, NR2C2 (own model) 22.6 TPM, NR1H2 (mapped) 20.86 TPM, PPARD (own model) 20.8 TPM (+28 more); best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G413 (C2H2 ZF, 1 model): best model ZBTB8A_DBD_GG40NGGTTTA_YWEA_jolma2025_0_2_7mer (own model of ZBTB8A), z -19.7, effect -0.603 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB8A z -19.7. TFs this group covers: ZBTB8A (own model) 6.4 TPM; best model's site strength: ref 97.8th, alt 62.5th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G037 (Nuclear receptor, 3 models): best model ESRRG_FL_TGAGCT40NGCA_KW_yin2017_0_3_7mer (own model of ESRRG), z 19.58, effect 0.719 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: ESRRG z 19.58, ESRRB z 7.9. TFs this group covers: ESRRA (own model) 38.54 TPM, ESRRB (own model) 0.41 TPM, ESR2 (mapped) 0.23 TPM, ESR1 (own model) 0.0 TPM, ESRRG (own model) 0.0 TPM; best model's site strength: ref 97.9th, alt 99.0th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G077 (AT hook, 2 models): best model SETBP1_DBD2_TC40NGGCTGT_YWHA_jolma2025_0_4_7mer (own model of SETBP1), z -16.06, effect -0.331 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: SETBP1 z -16.06. TFs this group covers: HMGA1 (own model) 1349.55 TPM, HMGA2 (mapped) 125.72 TPM, SRCAP (mapped) 32.16 TPM, ASH1L (mapped) 18.03 TPM, SETBP1 (own model) 0.01 TPM; best model's site strength: ref 95.5th, alt 68.2th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"HNF4A","symbol":"HNF4A","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr8:127401060:G>T","gate_p":5.02e-05,"models":[{"model":"HNF4A_NA_TGACAG20NGA_AF_jolma2013_1_3_7mer","mapping":"own","group":"G078 Nuclear receptor, 2 models","quality":0.709,"effect":-0.108,"z":-2.98,"p":0.0029,"rank_abs_z":"546/997","passed_gate":false,"site_strength":{"ref_percentile":78.0,"alt_percentile":75.7,"k":7}},{"model":"COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer","mapping":"CIS-BP (NR2F2)","group":"G002 Nuclear receptor, 29 models","quality":0.896,"effect":0.089,"z":2.25,"p":0.024,"rank_abs_z":"644/997","passed_gate":false,"site_strength":{"ref_percentile":94.6,"alt_percentile":90.7,"k":7}},{"model":"HNF4G_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (HNF4G)","group":"G078 Nuclear receptor, 2 models","quality":0.731,"effect":0.1,"z":3.05,"p":0.0023,"rank_abs_z":"537/997","passed_gate":false,"site_strength":{"ref_percentile":90.1,"alt_percentile":81.6,"k":7}},{"model":"NR2F1_NA_TCTGAC30NAGG_ESAI_yang2017_1_4_7mer","mapping":"CIS-BP (NR2F1)","group":"G002 Nuclear receptor, 29 models","quality":0.879,"effect":-0.079,"z":-1.16,"p":0.24,"rank_abs_z":"797/997","passed_gate":false,"site_strength":{"ref_percentile":64.5,"alt_percentile":57.0,"k":7}},{"model":"NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer","mapping":"CIS-BP (NR2F6)","group":"G002 Nuclear receptor, 29 models","quality":0.764,"effect":1.92,"z":20.82,"p":3.1e-96,"rank_abs_z":"12/997","passed_gate":true,"site_strength":{"ref_percentile":98.6,"alt_percentile":100.0,"k":7}},{"model":"NR6A1_eDBD_TTGATG40NATC_KT_yin2017_0_3_7mer","mapping":"CIS-BP (NR6A1)","group":"G002 Nuclear receptor, 29 models","quality":0.914,"effect":-0.114,"z":-2.32,"p":0.021,"rank_abs_z":"632/997","passed_gate":false,"site_strength":{"ref_percentile":95.5,"alt_percentile":93.1,"k":7}},{"model":"RXRB_NA_TGAGCA20NGA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (RXRB)","group":"G002 Nuclear receptor, 29 models","quality":0.667,"effect":-0.063,"z":-1.42,"p":0.16,"rank_abs_z":"764/997","passed_gate":false,"site_strength":{"ref_percentile":99.4,"alt_percentile":87.4,"k":7}},{"model":"RXRG_NA_TGGAAT20NGA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (RXRG)","group":"G002 Nuclear receptor, 29 models","quality":0.783,"effect":-0.517,"z":-1.71,"p":0.087,"rank_abs_z":"711/997","passed_gate":false,"site_strength":{"ref_percentile":99.8,"alt_percentile":93.5,"k":7}},{"model":"TLX_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer","mapping":"CIS-BP (NR2E1)","group":"G372 Nuclear receptor, 1 model","quality":0.88,"effect":1.968,"z":53.69,"p":0.0,"rank_abs_z":"1/997","passed_gate":true,"site_strength":{"ref_percentile":96.7,"alt_percentile":99.6,"k":7}}]}

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T16:35:30+00:00)

> 1 ENCODE TCF7L2 ChIP-seq peaks contain chr8:127401060:G>T in biosamples matching 'HCT116': biosamples HCT116; experiments ENCSR000EUV. In other biosamples, 3 TCF7L2 peaks do contain the variant: HepG2 (experiments ENCSR000EVQ, ENCSR346BOD).

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (T) relative to ref (G).
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06
