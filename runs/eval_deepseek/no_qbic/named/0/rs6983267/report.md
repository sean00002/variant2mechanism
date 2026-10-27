# rs6983267 and Colorectal cancer (8q24)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 7 model calls; 183 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H2: TCF7L2 binds the ref G allele at rs6983267 in HCT 116; loss of binding on alt T derepresses POU5F1B in colon and increases colorectal cancer risk (p = 0.45)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element proximal enhancer-like cCRE EH38E3858447; gene POU5F1B; cell type HCT 116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref G allele more strongly than the alt T allele at rs6983267. E07 shows a TCF7L2 ENCODE ChIP-seq peak containing the variant in HCT 116, but does not itself resolve allelic binding; the ref-G-more direction is inferred from E08, in which alt T is associated with higher POU5F1B expression, under a model where TCF7L2 binding at G represses POU5F1B. QBiC-SELEX coverage for TCF7L2 is not_checked: no screen row or qbic_tf_detail lookup was supplied, and E07 is ChIP-seq, not QBiC-SELEX. | weak | [E07](#e07), [E08](#e08) |
| element | rs6983267 lies in proximal enhancer-like cCRE EH38E3858447 with DNase, H3K27ac and CTCF signal, and the HCT 116 TCF7L2 ChIP-seq peak overlaps this region. This supports enhancer localization and TCF7L2 occupancy, not allele-specific enhancer activity. | supported | [E01](#e01), [E03](#e03), [E07](#e07) |
| gene | POU5F1B is 78.9 kb from its TSS, is the best L2G gene across credible sets at 0.89, and is a TWAS candidate; however, the listed L2G credible sets are mostly prostate cancer/PSA, not colorectal cancer. GTEx Colon-Transverse reports NES +0.20 for the alt T allele on POU5F1B expression. This links the allele to POU5F1B expression in colon but does not prove this enhancer targets POU5F1B. | weak | [E02](#e02), [E05](#e05), [E06b](#e06b), [E08](#e08) |
| cell_type | HCT 116 is the stated expression context and E07 provides HCT 116 TCF7L2 ChIP-seq occupancy at the variant-containing peak. E09 shows POU5F1B is not essential in HCT 116 (gene effect -0.09) and 0% of bowel lineage lines are dependent, so cell-type-specific essentiality support is limited. | weak | [E07](#e07), [E09](#e09) |
| phenotype | The strongest colorectal cancer GWAS record has effect allele T (p 2.0e-122), matching alt T higher POU5F1B expression, and E06d reports that POU5F1B fosters colorectal cancer proliferation and metastatic potential. Direction is not uniform across all E04 colon records, and E09 weakens the HCT 116 essentiality component, so the phenotype link is association plus literature, not proof of mediation. | weak | [E04](#e04), [E06d](#e06d), [E09](#e09) |

Predictions: Allele-specific TCF7L2 ChIP in HCT 116 will show more ref G than alt T occupancy at rs6983267.; In colon or HCT 116, alt T will associate with higher POU5F1B expression, consistent with E08 NES +0.20, because loss of TCF7L2 binding derepresses POU5F1B.; POU5F1B perturbation will affect colorectal cancer phenotypes in at least some contexts, although E09 predicts little effect in HCT 116 itself.

Falsified if: No allele-specific TCF7L2 binding is seen at rs6983267 in colorectal cells.; POU5F1B expression is not allele-dependent in colon or HCT 116.; The enhancer does not contact or regulate POU5F1B.; POU5F1B loss has no colorectal cancer phenotype in contexts where the chain claims it does.

### 2. H0: No TCF7L2-mediated allelic effect at rs6983267; the association reflects a linked causal variant, haplotype context, or no functional difference at this base (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TCF7L2 binding at rs6983267 in colorectal cells.; The E08 POU5F1B colon eQTL is explained by a linked variant or 8q24 haplotype rather than this base change.; Enhancer reporter or CRISPR allele-swap shows no TCF7L2-dependent allelic effect on POU5F1B, MYC, CCAT2 or PCAT1.

Falsified if: Allele-specific TCF7L2 binding plus an enhancer-reporter difference and a target-gene change are demonstrated for rs6983267.

### 3. H1: TCF7L2 binds the ref G allele at rs6983267 and alters MYC expression in colorectal cells, promoting colorectal cancer (p = 0.12)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element proximal enhancer-like cCRE EH38E3858447; gene MYC; cell type HCT 116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref G allele more strongly than the alt T allele at rs6983267. E07 supports TCF7L2 occupancy in a variant-containing HCT 116 ChIP-seq peak but not allele specificity; the ref-G-more direction is inferred, not directly shown. QBiC-SELEX coverage for TCF7L2 is not_checked. | weak | [E07](#e07), [E08](#e08) |
| element | rs6983267 lies in proximal enhancer-like cCRE EH38E3858447 with DNase, H3K27ac and CTCF signal, and the HCT 116 TCF7L2 ChIP-seq peak overlaps it. This is enhancer localization and occupancy, not allele-specific activity. | supported | [E01](#e01), [E03](#e03), [E07](#e07) |
| gene | MYC is 334.4 kb upstream of the variant. This is proximity only; E08 reports a significant colon eQTL only for POU5F1B, not MYC, so there is no direct variant-MYC expression link in the supplied evidence. | missing | [E02](#e02), [E08](#e08) |
| cell_type | HCT 116 is the stated expression context and E07 shows TCF7L2 ChIP-seq occupancy in HCT 116, but no HCT 116 MYC expression, contact or perturbation evidence links this element to MYC. | weak | [E07](#e07) |
| phenotype | rs6983267 is associated with colorectal cancer and colon phenotypes. The strongest colorectal cancer record has effect allele T, while several colon PheCode records have effect allele G; the phenotype link is association-level and direction is not uniform. | weak | [E04](#e04) |

Predictions: Allele-specific TCF7L2 ChIP in HCT 116 will show more ref G than alt T occupancy at rs6983267.; MYC expression or enhancer-MYC contact will differ by allele in colorectal cells.; MYC perturbation will attenuate the allele-dependent colorectal cancer phenotype.

Falsified if: No allele-specific TCF7L2 binding is seen at rs6983267.; MYC expression or enhancer-MYC contact is not allele-dependent in colorectal cells.; MYC perturbation does not affect the allele-dependent phenotype.

### 4. H3: TCF7L2 binds the ref G allele at rs6983267 and alters CCAT2 or PCAT1 non-coding transcript expression, promoting colorectal cancer (p = 0.08)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element proximal enhancer-like cCRE EH38E3858447; gene CCAT2/PCAT1; cell type HCT 116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref G allele more strongly than the alt T allele at rs6983267. E07 supports TCF7L2 occupancy in a variant-containing HCT 116 ChIP-seq peak but not allele specificity; the ref-G-more direction is inferred, not directly shown. QBiC-SELEX coverage for TCF7L2 is not_checked. | weak | [E07](#e07) |
| element | rs6983267 lies in proximal enhancer-like cCRE EH38E3858447, and E03 lists CCAT2 and PCAT1 among nearby genes for this cCRE cluster. This supports genomic proximity, not allele-specific enhancer activity or lncRNA targeting. | supported | [E01](#e01), [E03](#e03) |
| gene | E01 annotates the variant in a CCAT2 non-coding exon and in a PCAT1 intron/downstream region, and E06 includes CCAT2 gastrointestinal-cancer review hits. Gene-body overlap and review titles do not show that this enhancer regulates CCAT2 or PCAT1, and no variant-specific eQTL or 3D contact is supplied. | missing | [E01](#e01), [E03](#e03), [E06](#e06) |
| cell_type | HCT 116 is the stated expression context and E07 shows TCF7L2 ChIP-seq occupancy in HCT 116, but no HCT 116 CCAT2/PCAT1 expression, contact or perturbation evidence links these transcripts to the variant. | weak | [E07](#e07) |
| phenotype | rs6983267 is associated with colorectal cancer and colon phenotypes, and E06 includes review-level discussion of CCAT2 in gastrointestinal cancer. There is no functional evidence that CCAT2 or PCAT1 mediate the rs6983267 association. | weak | [E04](#e04), [E06](#e06) |

Predictions: Allele-specific TCF7L2 ChIP in HCT 116 will show more ref G than alt T occupancy at rs6983267.; CCAT2 or PCAT1 expression will differ by allele in colorectal cells.; The enhancer will physically contact the CCAT2 or PCAT1 locus more than MYC or POU5F1B.

Falsified if: No allele-specific TCF7L2 binding is seen at rs6983267.; CCAT2 and PCAT1 expression are not allele-dependent in colorectal cells.; The enhancer does not contact CCAT2 or PCAT1.; Knockdown of these transcripts does not affect colorectal cancer phenotypes.

## Prediction matrix

| Test | Cost | Separates top two | H2 | H0 | H1 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| EMSA with recombinant TCF7L2 and ref/alt rs6983267 oligos | low | yes | shifted |  |  |  |

## Next experiment

EMSA with recombinant TCF7L2 and ref/alt rs6983267 oligos

## Investigate calls

- chip_peaks({"tf": "TCF7L2", "biosample": "HCT 116"})
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

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T16:35:30+00:00)

> 1 ENCODE TCF7L2 ChIP-seq peaks contain chr8:127401060:G>T in biosamples matching 'HCT 116': biosamples HCT116; experiments ENCSR000EUV. In other biosamples, 3 TCF7L2 peaks do contain the variant: HepG2 (experiments ENCSR000EVQ, ENCSR346BOD).

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (T) relative to ref (G).
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

<a id="e09"></a>**E09** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for POU5F1B (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): -0.09. Bowel lineage, 31 lines: median -0.06, 0% dependent. All 351 lines: median -0.05, 3% dependent.
