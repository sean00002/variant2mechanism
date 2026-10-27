# rs6983267 and Colorectal cancer (8q24)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.69 over 7 model calls; 196 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen

421 of 997 models pass the gate. Top groups: Nuclear receptor, 1 model (best NR2E1, z 53.69); C2H2 ZF, 1 model (best ZNF493, z -34.16); C2H2 ZF, 2 models (best GFI1B, z -31.27); T-box, 2 models (best TBX19, z 26.18); C2H2 ZF, 1 model (best ZBTB43, z -23.26).

## Ranked chains

### 1. H1: Ref G allele strengthens a TCF/LEF site bound by TCF7L2 in the 8q24 enhancer, raising MYC/CCAT2 output in colonic epithelium (p = 0.44)

TF TCF7L2 (stated coverage mapped; registry mapped), ref allele binds more; element EH38E3858447 (pELS enhancer, ENSR8_CGMBX); gene MYC; cell type colonic epithelial / colorectal cancer cells (HCT 116, ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | A qbic_tf_detail lookup of TCF7L2 shows it is covered only through CIS-BP-mapped models of related HMG/Sox factors (LEF1, TCF7, TCF7L1), i.e. coverage 'mapped'. Two of these models pass the gate with negative effects (LEF1 effect -0.47, z -4.66; TCF7 effect -0.229, z -4.59), so the reference G allele is predicted to bind the TCF/LEF specificity more strongly; the effects are modest and rank only ~350/997, so this is weak binding evidence on its own. ENCODE ChIP-seq shows one TCF7L2 peak in HCT116 containing the variant (and three in HepG2), so the factor does occupy this site in the relevant line. | weak | [E18](#e18), [E19](#e19) |
| element | The variant lies in pELS cCRE EH38E3858447 with high DNase (z 5.2) and H3K27ac (z 4.8) and in Ensembl enhancer ENSR8_CGMBX; the z-scores are maxima over biosamples, but TCF7L2 occupancy in HCT116 shows the site is bound in a colon line. | supported | [E01](#e01), [E03](#e03), [E19](#e19) |
| gene | The element sits in the 8q24 gene desert; MYC is the nearest classical oncogene at 334 kb and a colon goblet-cell sceQTL for PVT1 (PIP 0.95) is in the same credible set, consistent with action on the MYC/PVT1 region. This is distance- and QTL-adjacent support only: L2G scores MYC 0.05 against POU5F1B 0.89, and no cited eQTL or CRISPR links this element to MYC. | weak | [E02](#e02), [E05](#e05) |
| cell_type | HCT116 is a Wnt-pathway-active colorectal line in which TCF7L2 binds this exact position (ENCSR000EUV); no cited evidence demonstrates colon-specific enhancer activity beyond that. | weak | [E19](#e19), [E03](#e03) |
| phenotype | Most colorectal rows in the GWAS Catalog list G as the effect allele (colorectal cancer or advanced adenoma p 3e-64, benign neoplasm of colon, colon polyps, colon cancer), matching a G-preferring TCF7L2 site; the top row lists T, so the sign convention is not internally consistent and the direction remains unresolved by cited evidence. | weak | [E04](#e04), [E06a](#e06a) |

Predictions: Allelic imbalance in existing HCT116 TCF7L2 ChIP-seq reads favours G; CRISPRi of EH38E3858447 lowers MYC/PVT1 more than POU5F1B; Wnt/TCF inhibition abolishes the allelic reporter difference; TCF7L2 knockdown removes the allelic difference

Falsified if: Allele-specific TCF7L2 ChIP or EMSA shows no G/T difference; Enhancer perturbation changes POU5F1B but not MYC/PVT1; TCF7L2 depletion leaves allelic reporter activity unchanged

### 2. H5: Null: no TF-mediated effect of this variant; the colorectal signal is carried by a linked variant or another cCRE (p = 0.23)

Null chain: no TF-mediated effect of this variant.

Predictions: Allelic reporter assays at EH38E3858447 show no significant G/T difference in colon cells; Causal signal maps to another variant in the 8q24 credible set or to EH38E3858446/8; No allele-specific accessibility or ChIP signal at the site in heterozygous colon samples; Base editing the single position leaves MYC, CCAT2 and POU5F1B unchanged

Falsified if: Base editing this position in a heterozygous colon line changes MYC/CCAT2/POU5F1B expression; Allele-specific ChIP or accessibility at the site is reproducibly imbalanced

### 3. H4: Alt T allele creates a T-box site that raises POU5F1B, the eQTL- and L2G-nominated effector gene (p = 0.17)

TF TBX19 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3858447 (pELS enhancer); gene POU5F1B; cell type colorectal cancer cells (HCT 116) / transverse colon.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G101 (T-box) shows a large alt gain (TBX19 own model, z 26.18, effect +4.18; site strength ref 79.0th to alt 99.9th percentile). Within the group TBXT is 0 TPM and TBX19 1.92 TPM in this line, so TBX19 is named by expression alone; the choice is weak and no ChIP or EMSA evidence supports T-box occupancy here. | weak | [E11](#e11) |
| element | The site is an active pELS enhancer (DNase z 5.2, H3K27ac z 4.8) in which a de novo high-affinity T-box site could raise activity. | weak | [E03](#e03) |
| gene | GTEx v8 shows a significant colon-transverse eQTL in which the alt T allele raises POU5F1B (NES +0.20, p 8.2e-06), the same direction as the predicted alt binding gain; Open Targets L2G nominates POU5F1B (0.82-0.89) and the variant lies in the POU5F1B gene body. | supported | [E20](#e20), [E05](#e05), [E02](#e02), [E01](#e01), [E06b](#e06b) |
| cell_type | The effect gene is measured in transverse colon, the disease-relevant tissue, and TBX19 is expressed (1.92 TPM) in the HCT 116 context; expression only, no occupancy shown. | weak | [E20](#e20), [E11](#e11) |
| phenotype | POU5F1B fosters proliferation and metastatic potential of CRC cells, so higher POU5F1B on the T allele could raise risk; however most colorectal GWAS rows name G as the effect allele, which conflicts with this direction. | weak | [E06c](#e06c), [E06b](#e06b), [E04](#e04) |

Predictions: T allele gains T-box factor binding in EMSA with colon nuclear extract; CRISPRi of the element lowers POU5F1B specifically; TBX19 depletion removes the allelic reporter difference; Allelic imbalance in POU5F1B RNA favours T in heterozygous colon

Falsified if: No T-box factor binds the locus or TBX19 depletion has no effect; Element perturbation changes MYC/CCAT2 but not POU5F1B

### 4. H3: Ref G allele is bound by the BTB-ZF factor ZBTB43, whose loss on the T allele de-represses the enhancer (p = 0.09)

TF ZBTB43 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E3858447 (pELS enhancer); gene POU5F1B; cell type colorectal cancer cells (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G404 contains only ZBTB43 (own model), z -23.26, effect -1.724: the reference G allele binds more strongly (ref 99.8th vs alt 87.9th percentile). No within-group choice is needed, but this is a binding prediction alone with no ChIP or EMSA support, and the repressor role of ZBTB43 is an assumption. | weak | [E12](#e12) |
| element | The variant sits in an active pELS enhancer; loss of a repressive BTB-ZF site there would raise its activity. | weak | [E03](#e03) |
| gene | Higher activity on the T allele matches the only cited colon eQTL, POU5F1B up on T (NES +0.20), and POU5F1B is the L2G-nominated gene; the connection of ZBTB43 to that gene is not shown. | weak | [E20](#e20), [E05](#e05) |
| cell_type | ZBTB43 is expressed at 8.32 TPM in the HCT 116 context; expression only, no occupancy shown. | weak | [E12](#e12) |
| phenotype | Increased 8q24 enhancer output in colonic epithelium is consistent with the strong colorectal associations at rs6983267, though the risk-allele direction across GWAS rows is inconsistent. | weak | [E04](#e04) |

Predictions: ZBTB43 CUT&RUN shows G-biased occupancy at the cCRE; ZBTB43 knockdown raises reporter activity only for the G allele; The allelic difference is independent of TCF/LEF and of Wnt inhibition

Falsified if: ZBTB43 does not occupy the locus in colon cells; ZBTB43 depletion has no effect on reporter activity or on POU5F1B/MYC

### 5. H2: Alt T allele strengthens a nuclear-receptor half-site read by HNF4A, altering enhancer output on CCAT2/POU5F1B (p = 0.07)

TF HNF4A (stated coverage own_model; registry own_model), alt allele binds more; element EH38E3858447 (pELS enhancer); gene CCAT2; cell type colorectal epithelial cells (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G372 (nuclear receptor specificity) shows a very strong alt-preferring change (best model NR2E1, z 53.69, effect +1.968; ref 96.7th to alt 99.6th percentile). The group names a shared specificity: its only passing member NR2E1 is 0 TPM, while the group row lists HNF4A (own model, 2.95 TPM) and HNF4G (own model, 2.24 TPM) as expressed, and HNF4A is the dominant intestinal nuclear receptor, so HNF4A is chosen by expression plus tissue identity. No model of HNF4A itself is reported as passing, so its direction is inferred from the shared specificity and is weak. A broader nuclear-receptor group (G002) also shows alt gain but with members disagreeing on direction. | weak | [E08](#e08), [E14](#e14) |
| element | The variant lies in an active pELS enhancer (DNase z 5.2, H3K27ac z 4.8), where a gained nuclear-receptor site could change output. | weak | [E03](#e03) |
| gene | The variant is exonic in CCAT2 and the cCRE's nearby genes are CCAT2/PCAT1/POU5F1B; the only cited allele-dependent expression in colon is POU5F1B (alt-raising), so CCAT2 rests on proximity alone. | weak | [E01](#e01), [E03](#e03), [E20](#e20) |
| cell_type | HNF4A is expressed in this colorectal line (2.95 TPM) whereas NR2E1 is not; expression only, no occupancy shown. | weak | [E08](#e08) |
| phenotype | CCAT2 is repeatedly implicated in gastrointestinal cancer progression, so a change in CCAT2 level could alter CRC risk; no cited quote ties CCAT2 level to this allele. | weak | [E06](#e06) |

Predictions: HNF4A ChIP-seq at the cCRE shows T-allele bias in heterozygous colon lines; HNF4A knockdown removes the allelic reporter difference; The allelic difference survives Wnt/TCF inhibition; CCAT2, not MYC or POU5F1B, responds to element perturbation

Falsified if: No HNF4A occupancy at EH38E3858447 in colon ChIP-seq; T allele shows no nuclear-receptor binding gain in EMSA

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H4 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allelic-imbalance re-analysis of existing ENCODE HCT116 TCF7L2 ChIP-seq (ENCSR000EUV) reads at chr8:127401060 | existing data | yes | Reads at the peak are skewed toward G | Balanced reads; no allelic skew | No TCF7L2 allelic skew (T-box factor, not TCF7L2, drives the difference) | No TCF7L2 skew | No TCF7L2 skew, or skew toward T if any |
| CRISPRi/deletion of EH38E3858447 in HCT116 with RT-qPCR of MYC, PVT1, CCAT2 and POU5F1B | medium | yes | MYC/PVT1 (and CCAT2) fall most | Element may matter but single-base allele has no effect; gene changes do not track the variant | POU5F1B falls most | POU5F1B/MYC rise or fall only modestly; repressive site loss predicts limited activation effect | CCAT2 falls most |
| Allelic MPRA/luciferase of the 300 bp element (G vs T) in HCT116 with and without a Wnt/TCF inhibitor | medium | yes | G > T activity; difference abolished by Wnt/TCF inhibition | No significant G vs T difference | T > G activity; difference persists under Wnt inhibition | T > G activity; lost on ZBTB43 knockdown | T > G activity; persists under Wnt inhibition, lost on HNF4A knockdown |
| TF knockdown panel (TCF7L2, TBX19, HNF4A, ZBTB43) with allelic reporter readout | high | yes | Only TCF7L2 knockdown collapses the difference | No knockdown changes an allelic difference because none exists | Only TBX19 knockdown collapses the difference | Only ZBTB43 knockdown collapses the difference | Only HNF4A knockdown collapses the difference |
| Existing GTEx colon eQTL direction for POU5F1B/CASC8 (E20) | existing data | no | POU5F1B eQTL is a bystander; MYC/PVT1 is the true target (not directly tested) | eQTL could be driven by a linked variant | Alt T raises POU5F1B in colon, matching the alt-gain binding prediction | Alt (repressor loss) raises nearby gene expression | Alt effect on a nearby transcript, CCAT2 not assayed |

## Next experiment

Re-analyse the existing ENCODE HCT116 TCF7L2 ChIP-seq (ENCSR000EUV) reads overlapping chr8:127401060 for allele-specific imbalance (cost: existing data). A G-skew supports H1 over H4; balanced reads, or no heterozygosity requiring a quick targeted TCF7L2 CUT&RUN in a heterozygous colon line, argues against the TCF7L2 chain.

## Investigate calls

- qbic_tf_detail({"tf": "TCF7L2"})
- chip_peaks({"tf": "TCF7L2", "biosample": "HCT116"})
- eqtl_lookup({"tissue": null})

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

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401060:G>T","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.47,"z":-4.66,"p":3.2e-06,"rank_abs_z":"351/997","passed_gate":true,"site_strength":{"ref_percentile":98.8,"alt_percentile":98.4,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.229,"z":-4.59,"p":4.4e-06,"rank_abs_z":"367/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.275,"z":-3.47,"p":0.00052,"rank_abs_z":"486/997","passed_gate":false,"site_strength":{"ref_percentile":83.5,"alt_percentile":92.1,"k":7}}]}

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T16:35:30+00:00)

> 1 ENCODE TCF7L2 ChIP-seq peaks contain chr8:127401060:G>T in biosamples matching 'HCT116': biosamples HCT116; experiments ENCSR000EUV. In other biosamples, 3 TCF7L2 peaks do contain the variant: HepG2 (experiments ENCSR000EVQ, ENCSR346BOD).

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 2 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).
> CASC8 in Whole_Blood: NES -0.32, p 6.3e-10
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06
