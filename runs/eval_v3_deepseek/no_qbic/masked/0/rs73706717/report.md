# rs73706717 and Colorectal cancer (8q24)

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 9 model calls; 180 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H1: TCF7L2 binding at an 8q24 enhancer regulates MYC (p = 0.40)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element proximal enhancer-like pELS EH38E3858447; gene MYC; cell type colorectal cancer cell line HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies this element in HCT116. The hypothesis is that the alt C allele binds TCF7L2 more strongly than the ref T allele. No QBiC-SELEX model for TCF7L2 was supplied and no allele-specific binding data are given, so the direction is an untested inference, not direct evidence. | weak | [E04](#e04), [E05](#e05), [E19](#e19) |
| element | The variant lies in an active proximal enhancer-like cCRE, EH38E3858447, with DNase and H3K27ac signal consistent with a regulatory element. | supported | [E01](#e01), [E03](#e03) |
| gene | The proposed target is MYC, 334.2 kb upstream. MYC is a plausible 8q24/CRC gene, but there is no direct enhancer-promoter evidence supplied; MYC knockout has a strong growth effect in HCT116 but MYC is common-essential, so this does not establish enhancer specificity. | missing | [E02](#e02), [E18](#e18), [E21](#e21) |
| cell_type | HCT116 is the relevant colorectal cancer cell line because TCF7L2 occupancy at this element and TCF7L2 expression are observed there. | supported | [E04](#e04), [E05](#e05) |
| phenotype | Altered TCF7L2-dependent enhancer activity at 8q24 could affect MYC expression and colorectal cancer biology, but the supplied evidence is general CRC literature rather than variant-specific mechanism. | missing | [E18](#e18), [E21](#e21) |

Predictions: Allele-specific TCF7L2 ChIP or EMSA shows stronger binding to the C allele than the T allele.; CRISPR editing of the variant or deletion of EH38E3858447 changes MYC expression in HCT116.; TCF7L2 depletion reduces MYC expression and colorectal cancer cell growth.

Falsified if: allele-specific TCF7L2 ChIP or reporter assays show no difference between T and C; TCF7L2 knockdown or enhancer deletion does not change MYC in HCT116; the variant is shown to be in complete linkage with another causal variant that explains the signal

### 2. H4: Null: no TF-mediated effect of this variant (p = 0.38)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding or enhancer activity difference at chr8:127401265 T>C.; Any disease association is explained by a linked variant, 8q24 context, or no allelic effect at this base.

Falsified if: allele-specific reporter or TF ChIP assays show no reproducible T/C effect at this base; a linked causal variant is excluded and this variant is shown to directly alter TF binding and gene expression

### 3. H2: SP1 binding at the same enhancer regulates POU5F1B (p = 0.22)

TF SP1 (QBiC-SELEX coverage own_model), alt allele binds more; element proximal enhancer-like pELS EH38E3858447; gene POU5F1B; cell type colorectal cancer cell line HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 occupies this element in HCT116. The hypothesis is that the alt C allele binds SP1 more strongly than the ref T allele. No QBiC-SELEX model for SP1 was supplied and no allele-specific binding data are given, so the direction is an untested inference. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies in the active pELS EH38E3858447, a plausible SP1-responsive enhancer. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is 79.1 kb away and is the best L2G gene in the supplied credible sets, but those credible sets are for PSA and urinary incontinence, not colorectal cancer; no GTEx eQTL for this SNP was supplied. | missing | [E02](#e02), [E16](#e16), [E17](#e17) |
| cell_type | HCT116 is the matching colorectal cancer cell line with SP1 occupancy at the element and SP1 expression. | supported | [E04](#e04), [E06](#e06) |
| phenotype | POU5F1B has literature support in colorectal cancer, but the supplied evidence does not establish a variant-specific SP1-POU5F1B disease mechanism. | missing | [E18](#e18) |

Predictions: Allele-specific SP1 binding is higher on the C allele.; SP1 knockdown reduces POU5F1B expression in HCT116.; The enhancer contacts the POU5F1B promoter in HCT116.

Falsified if: SP1 ChIP or reporter assays show no allele-specific effect; SP1 depletion does not affect POU5F1B expression in HCT116; POU5F1B is not expressed or not regulated from this enhancer in colorectal cells

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific enhancer luciferase reporter with T vs C in HCT116 | low | yes | Reproducible T/C allelic difference in enhancer reporter activity, direction consistent with TCF7L2 effect. | No reproducible allelic difference. | Reproducible T/C allelic difference in enhancer reporter activity, direction consistent with SP1 effect. |
| Allele-specific TCF7L2 ChIP or EMSA at chr8:127401265 | medium | yes | C allele shows stronger TCF7L2 binding than T. | No allele-specific TCF7L2 binding. | No TCF7L2 allele-specific binding. |
| SP1 knockdown with POU5F1B expression in HCT116 | medium | no | Little or no change in POU5F1B after SP1 knockdown. | No variant-dependent SP1-POU5F1B effect. | POU5F1B expression decreases after SP1 knockdown. |
| CRISPR variant editing or enhancer deletion with MYC and POU5F1B expression | high | yes | MYC expression changes after editing the variant or deleting EH38E3858447. | Neither MYC nor POU5F1B changes reproducibly. | POU5F1B expression changes; MYC change not necessarily. |
| Chromosome conformation assay in HCT116 | high | yes | Enhancer contacts MYC. | No allele-specific contact change. | Enhancer contacts POU5F1B. |

## Next experiment

Allele-specific enhancer reporter with T vs C in HCT116; low cost; H1 predicts a reproducible allelic activity difference while H4 predicts none. This is the cheapest experiment that separates the current top two chains H1 and H4.

## Investigate calls

- chip_peaks({"tf": "TCF7L2", "biosample": "HCT116"})
- chip_peaks({"tf": "CTCF", "biosample": "HCT116"})
- gene_dependency({"gene": "MYC"})

## Flags

- quote_rejected: PMID 42465001: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401265-127401265:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:21:56+00:00)

> Variant chr8:127401265:T>C (GRCh38), allele string T/C
> Known IDs: rs73706717
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: -2.8
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401265-128401265?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:21:59+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401265:T>C, by distance to TSS:
> POU5F1B: 79.1 kb from TSS (in gene body, strand +1)
> MYC: 334.2 kb from TSS (upstream, strand +1)
> LRATD2: 842.8 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:21:42+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:127401265:T>C: 149 peaks contain the variant, from 83 factors in 25 biosamples. In the matching biosample HCT116: 3 peaks from 3 factors. cCRE class at the variant: pELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, CHD4, EP300, HDAC1, HDAC2, HMGXB4, KDM1A, KDM6A, LCORL, LIN54, MED1, MED13 (+26 more). Bound, expressed TFs with a binding model: 40; listed one per row: TCF7L2, SP1, CTCF, CEBPB, MYBL2, NR2C2, TFAP4, ISL2, NR2F2, ERF; also bound: NR2F6, NFIC, ELF1, ZNF317, NFIL3, ZBTB7B, KLF16, PITX1, JUNB, SKI, CREM, RXRB, ATF2, ZNF609, ZNF280D, ZNF12, AHDC1, ZNF652, PHF21A, ETS1, NFIA, NR3C1, BCL6, PRDM10, HOXA3, HNF4A, MNX1, HNF1B, ZNF362, FOXA1. Bound but below 1 TPM: FOXA2, HNF1A, ONECUT1, SOX6, TBX2. Assayed with no peak here: 11 TFs in the matching biosample, 517 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000EUV). 63.61 TPM in DepMap:ACH-000971 (HCT 116), rank 53 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000BSF). 38.96 TPM in DepMap:ACH-000971 (HCT 116), rank 118 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 34 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, C4-2B, Panc1, RWPE2, adrenal gland, astrocyte (+13 more) (e.g. ENCSR173IEA). 50.0 TPM in DepMap:ACH-000971 (HCT 116), rank 78 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BQI). 13.15 TPM in DepMap:ACH-000971 (HCT 116), rank 408 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 67.51 TPM in DepMap:ACH-000971 (HCT 116), rank 46 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR559ZKI). 22.6 TPM in DepMap:ACH-000971 (HCT 116), rank 244 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TFAP4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR587BVQ). 19.72 TPM in DepMap:ACH-000971 (HCT 116), rank 283 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ISL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR492IHH). 2.77 TPM in DepMap:ACH-000971 (HCT 116), rank 862 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BVM). 61.74 TPM in DepMap:ACH-000971 (HCT 116), rank 58 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ERF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR159DQO). 46.58 TPM in DepMap:ACH-000971 (HCT 116), rank 90 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs73706717&size=100; retrieved 2026-10-26T02:21:56+00:00)

> 0 GWAS Catalog associations for rs73706717, strongest first:

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:21:56+00:00)

> 2 credible sets contain 8_127401265_T_C: 2 GWAS, 0 molecular QTL.
> GWAS prostate-specific antigen (PSA, maximum, inv-norm transforme: PIP 0.04; L2G POU5F1B 0.83
> GWAS Urinary incontinence (PheCode 599.4): PIP 0.04; L2G POU5F1B 0.78
> Best L2G gene scores across these sets: POU5F1B 0.83

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38. NES is the effect of the alt allele (C) relative to ref (T).

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

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:23:31+00:00)

> 1 ENCODE TCF7L2 ChIP-seq peaks contain chr8:127401265:T>C in biosamples matching 'HCT116': biosamples HCT116; experiments ENCSR000EUV. In other biosamples, 3 TCF7L2 peaks do contain the variant: HepG2 (experiments ENCSR000EVQ, ENCSR346BOD).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:23:02+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr8:127401265:T>C in biosamples matching 'HCT116'. Absence can also mean no CTCF experiment in that biosample. In other biosamples, 34 CTCF peaks do contain the variant: A549, C4-2B, Panc1, RWPE2, adrenal gland, astrocyte, brain, breast epithelium, endothelial cell, epithelial cell of prostate, esophagus squamous epithelium, excitatory neuron, left lung, mesothelial cell of epicardium, middle frontal area 46, stomach, testis, thoracic aorta, tibial nerve (experiments ENCSR031PXV, ENCSR037GKL, ENCSR073BPG, ENCSR130TQM, ENCSR173IEA, ENCSR188XCX).

<a id="e21"></a>**E21** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for MYC (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): -1.27. Bowel lineage, 63 lines: median -1.89, 98% dependent. All 1183 lines: median -1.83, 95% dependent. common-essential in DepMap: a strong knockout effect here is not evidence for a lineage-specific role.
