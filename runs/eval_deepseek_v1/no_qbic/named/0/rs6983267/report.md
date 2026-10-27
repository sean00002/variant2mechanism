# rs6983267 and Colorectal cancer (8q24)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 7 model calls; 225 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. TCF7L2_POU5F1B_enhancer: TCF7L2 binds the G allele more and represses the 8q24 enhancer controlling POU5F1B; the T allele derepresses POU5F1B (p = 0.52)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element ENSR8_CGMBX / EH38E3858447 pELS enhancer; gene POU5F1B; cell type HCT116 colorectal cancer cells (DepMap:ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies the rs6983267-containing element in HCT116 (E07), and TCF7L2 is highly expressed in HCT116 (E09). I propose that the ref G allele binds TCF7L2 more strongly than the alt T allele; E07 does not resolve allele specificity. QBiC-SELEX coverage for TCF7L2 is not_checked because no QBiC screen row or qbic_tf_detail lookup is supplied. | weak | [E07](#e07), [E09](#e09) |
| element | rs6983267 lies in the ENSR8_CGMBX enhancer and within ENCODE pELS cCRE EH38E3858447. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is 78.9 kb from the variant, is the best Open Targets L2G gene (0.89), and is a TWAS candidate; in colon transverse, the alt T allele associates with higher POU5F1B expression (NES +0.20), consistent with T allele loss of TCF7L2-mediated repression. | weak | [E02](#e02), [E05](#e05), [E06b](#e06b), [E08](#e08) |
| cell_type | HCT116 expresses TCF7L2 at 63.61 TPM (rank 53/1626, 99.5th percentile) and has a TCF7L2 ChIP-seq peak containing the variant. | supported | [E07](#e07), [E09](#e09) |
| phenotype | rs6983267 is strongly associated with colorectal cancer; the strongest CRC row lists T as the effect allele, and POU5F1B promotes CRC proliferation and metastatic potential. The T-risk direction fits T-higher POU5F1B, although other E04 rows list G, so allelic direction is not fully resolved. | weak | [E04](#e04), [E06c](#e06c), [E08](#e08) |

Predictions: Allele-specific TCF7L2 ChIP shows higher binding on G than T at rs6983267 in HCT116.; TCF7L2 knockdown increases POU5F1B expression in HCT116.; The T allele increases POU5F1B expression in colon/HCT116, consistent with loss of TCF7L2-mediated repression.

Falsified if: TCF7L2 binding is not allele-specific or is higher on the T allele.; TCF7L2 knockdown does not change POU5F1B expression or changes it in the opposite direction.; Allele substitution at rs6983267 does not change POU5F1B expression.

### 2. null_no_tf_effect: Null: no TF-mediated effect of rs6983267 (p = 0.24)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs6983267 in HCT116 beyond what is explained by a linked variant.; No allele-specific enhancer activity in reporter assays.; The 8q24 GWAS signal is explained by a linked causal variant in LD, not by rs6983267 itself.

Falsified if: Allele-specific TCF7L2 binding is experimentally demonstrated at rs6983267 in HCT116.; CRISPR allele substitution at rs6983267 changes POU5F1B expression in CRC cells.

### 3. TCF7L2_MYC_enhancer: TCF7L2 binds the G allele more and activates MYC through the 8q24 enhancer (p = 0.12)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element ENSR8_CGMBX / EH38E3858447 pELS enhancer; gene MYC; cell type HCT116 colorectal cancer cells (DepMap:ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies the rs6983267-containing element in HCT116 (E07), and TCF7L2 is highly expressed in HCT116 (E09). I propose that the ref G allele binds TCF7L2 more strongly than the alt T allele; E07 does not resolve allele specificity. QBiC-SELEX coverage for TCF7L2 is not_checked because no QBiC screen row or qbic_tf_detail lookup is supplied. | weak | [E07](#e07), [E09](#e09) |
| element | rs6983267 lies in the ENSR8_CGMBX enhancer and within ENCODE pELS cCRE EH38E3858447. | supported | [E01](#e01), [E03](#e03) |
| gene | MYC is 334.4 kb upstream of the variant, but Open Targets L2G for MYC is only 0.05 and E08 provides no MYC colon eQTL; this is proximity prioritization, not demonstrated enhancer contact. | missing | [E02](#e02), [E05](#e05) |
| cell_type | HCT116 expresses TCF7L2 at 63.61 TPM (rank 53/1626, 99.5th percentile) and has a TCF7L2 ChIP-seq peak containing the variant. | supported | [E07](#e07), [E09](#e09) |
| phenotype | rs6983267 is associated with colorectal cancer, but this chain requires the G allele to be risk and higher-binding/activating, which conflicts with the strongest CRC row listing T as effect allele and with the T-higher POU5F1B eQTL direction. | missing | [E04](#e04), [E06a](#e06a) |

Predictions: Allele-specific TCF7L2 ChIP shows higher binding on G than T at rs6983267 in HCT116.; TCF7L2 knockdown decreases MYC expression in HCT116.; The enhancer contacts the MYC promoter in HCT116.

Falsified if: TCF7L2 binding is not allele-specific or is higher on the T allele.; The enhancer does not contact the MYC promoter in CRC cells.; TCF7L2 knockdown or allele substitution does not change MYC expression.

### 4. TCF7L2_CCAT2_enhancer: TCF7L2 binds the G allele more and represses CCAT2 lncRNA through the 8q24 enhancer (p = 0.12)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element ENSR8_CGMBX / EH38E3858447 pELS enhancer; gene CCAT2; cell type HCT116 colorectal cancer cells (DepMap:ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies the rs6983267-containing element in HCT116 (E07), and TCF7L2 is highly expressed in HCT116 (E09). I propose that the ref G allele binds TCF7L2 more strongly than the alt T allele; E07 does not resolve allele specificity. QBiC-SELEX coverage for TCF7L2 is not_checked because no QBiC screen row or qbic_tf_detail lookup is supplied. | weak | [E07](#e07), [E09](#e09) |
| element | rs6983267 lies in the ENSR8_CGMBX enhancer and within ENCODE pELS cCRE EH38E3858447, and is annotated as a CCAT2 non-coding transcript exon variant. | supported | [E01](#e01), [E03](#e03) |
| gene | CCAT2 overlaps the regulatory region and is repeatedly implicated in gastrointestinal cancer, but there is no supplied evidence that this enhancer controls CCAT2 or that rs6983267 allele-specifically regulates CCAT2. | missing | [E01](#e01), [E03](#e03), [E06](#e06) |
| cell_type | HCT116 expresses TCF7L2 at 63.61 TPM (rank 53/1626, 99.5th percentile) and has a TCF7L2 ChIP-seq peak containing the variant. | supported | [E07](#e07), [E09](#e09) |
| phenotype | rs6983267 is associated with colorectal cancer and CCAT2 has gastrointestinal-cancer literature support, but no quote directly links rs6983267 to CCAT2 regulation or CRC phenotype. | weak | [E04](#e04), [E06](#e06) |

Predictions: Allele-specific TCF7L2 ChIP shows higher binding on G than T at rs6983267 in HCT116.; TCF7L2 knockdown increases CCAT2 expression in HCT116.; Allele substitution at rs6983267 changes CCAT2 expression.

Falsified if: CCAT2 expression is not allele-specifically regulated by the enhancer.; The enhancer does not contact the CCAT2 locus in CRC cells.; TCF7L2 knockdown or allele substitution does not change CCAT2 expression.

## Prediction matrix

| Test | Cost | Separates top two | TCF7L2_POU5F1B_enhancer | null_no_tf_effect | TCF7L2_MYC_enhancer | TCF7L2_CCAT2_enhancer |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 ChIP in HCT116 at rs6983267 (existing ENCSR000EUV re-analysis or targeted ChIP-qPCR) | low | yes | TCF7L2 binds ref G more than alt T. | No allele-specific TCF7L2 occupancy; any peak is not rs6983267-dependent. | TCF7L2 binds ref G more than alt T, if MYC is the target. | TCF7L2 binds ref G more than alt T, if CCAT2 is the target. |
| Colon eQTL / allele-specific expression for POU5F1B, MYC and CCAT2 | low | yes | Alt T associates with higher POU5F1B expression in colon, as in E08. | No rs6983267-specific expression effect; any signal is explained by a linked variant. | No strong MYC eQTL; MYC is not the primary allele-specific target. | No strong CCAT2 eQTL; CCAT2 is not the primary allele-specific target. |
| TCF7L2 knockdown in HCT116 followed by qPCR for POU5F1B, MYC and CCAT2 | medium | yes | TCF7L2 knockdown increases POU5F1B expression, consistent with TCF7L2-mediated repression. | No change in POU5F1B, MYC or CCAT2 expression. | TCF7L2 knockdown decreases MYC expression, consistent with TCF7L2-mediated activation. | TCF7L2 knockdown increases CCAT2 expression, consistent with TCF7L2-mediated repression. |
| CRISPR allele substitution at rs6983267 in HCT116 with expression readout | high | yes | T allele increases POU5F1B expression. | No allele-dependent change in POU5F1B, MYC or CCAT2. | Allele substitution changes MYC expression. | Allele substitution changes CCAT2 expression. |

## Next experiment

Allele-specific read-count analysis of the existing HCT116 TCF7L2 ChIP-seq peak containing rs6983267 (ENCSR000EUV), with targeted TCF7L2 ChIP-qPCR if allelic coverage is insufficient.

## Investigate calls

- chip_peaks({"tf": "TCF7L2", "biosample": "HCT 116"})
- eqtl_lookup({"tissue": "Colon"})
- tf_expression({"tf": "TCF7L2", "context": "DepMap:ACH-000971"})

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

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 35987910 (https://europepmc.org/article/MED/35987910; retrieved 2026-10-25T16:33:56+00:00)

> We further determine that POU5F1B, in spite of its phylogenetic relationship with the POU5F1/OCT4 transcription factor, is a membrane-enriched protein that associates with protein kinases and known targets or interactors as well as with cytoskeleton-related molecules, and induces intracellular signaling events and the release of trans-acting factors involved in cell growth and cell adhesion.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T16:35:30+00:00)

> 1 ENCODE TCF7L2 ChIP-seq peaks contain chr8:127401060:G>T in biosamples matching 'HCT 116': biosamples HCT116; experiments ENCSR000EUV. In other biosamples, 3 TCF7L2 peaks do contain the variant: HepG2 (experiments ENCSR000EVQ, ENCSR346BOD).

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38 in tissues matching 'Colon'. NES is the effect of the alt allele (T) relative to ref (G).
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

<a id="e09"></a>**E09** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> TCF7L2 in DepMap line ACH-000971: 63.61 TPM, rank 53 of 1626 TFs (1 = highest); this context is at the 99.5th percentile of TCF7L2 across all DepMap lines.
