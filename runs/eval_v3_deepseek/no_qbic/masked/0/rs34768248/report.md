# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 9 model calls; 272 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H_Null: No confirmed TF-mediated effect of chr5:1295601:G>A in glioblastoma; the variant may be linked, passenger, or have an effect too weak/context-dependent to detect. (p = 0.48)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy or regulatory activity at chr5:1295601:G>A in glioblastoma cells.; Any association with TERT or disease is explained by linkage or proximity rather than a direct allele-specific TF effect at this base.

Falsified if: A glioblastoma-relevant TF is shown to occupy this site in an allele-specific manner and perturbation of that TF changes TERT expression or a TERT-dependent phenotype.

### 2. H_Max_TERT: The variant alters MAX binding at the TERT upstream/THOR region, changing TERT regulation in glioblastoma cells. (p = 0.22)

TF MAX (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR5_C5GP enhancer / region 75 bp from nearest pELS; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MAX is the best-supported non-null candidate among the listed TFs because it is highly expressed in glioblastoma (58.6 TPM, rank 48/1626), has an ENCODE peak containing the variant in H1 (E08/E19), and c-Myc/MAX is literature-linked to hTERT promoter activation via Ets/E-box motifs (E21e/E21f). However, no glioblastoma ChIP peak at this site is provided, E04 says no ENCODE biosample matches the expression context, and no QBiC-SELEX/allele-specific data exist; the hypothesized direction that alt A binds MAX more strongly is a model prediction, not established. | missing | [E08](#e08), [E19](#e19), [E04](#e04), [E21e](#e21e), [E21f](#e21f) |
| element | VEP annotates ENSR5_C5GP enhancer at the variant (E01), but E03 reports that no ENCODE cCRE overlaps the variant and the nearest pELS is 75 bp away, so the element assignment is uncertain and the variant may sit adjacent to, rather than inside, the active element. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is only 0.5 kb from the TSS (E02), and MAX/Myc literature supports hTERT promoter activation (E21e/E21f), but there is no Hi-C/3C, reporter, or perturbation evidence in this case linking this specific upstream site to TERT. | weak | [E02](#e02), [E21e](#e21e), [E21f](#e21f) |
| cell_type | Glioblastoma is the supplied expression context and MAX is expressed there (E08), but there is no glioblastoma ChIP at this site (E04) and no TERT expression data in glioblastoma are supplied. | weak | [E08](#e08), [E04](#e04) |
| phenotype | TERT is repeatedly implicated in glioblastoma/melanoma/bladder cancer in the literature (E18), but the genetic support here is weak: E16 is a hypertension credible set with PIP 0.00, and E20 shows TERT is not commonly essential in CNS lines (median -0.00, 2% dependent). | missing | [E18](#e18), [E16](#e16), [E20](#e20) |

Predictions: MAX occupies chr5:1295601 in glioblastoma cells, with stronger binding to the A allele than the G allele.; Allele-specific MAX perturbation or E-box mutation reduces the allele-dependent TERT reporter/expression effect.

Falsified if: MAX does not occupy the variant site in glioblastoma cells, or the G/A change has no effect on MAX binding or TERT regulation.

### 3. H_JUN_TERT: The variant alters JUN/AP-1 binding at the TERT upstream region, changing TERT regulation in glioblastoma cells. (p = 0.18)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR5_C5GP enhancer / region 75 bp from nearest pELS; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is the highest-expressed listed TF in glioblastoma (91.65 TPM, rank 16/1626) and has two ENCODE peaks containing the variant in A549 (E05), making it a plausible AP-1 factor. But there is no glioblastoma ChIP at this site (E04), no QBiC-SELEX or allele-specific data, and the hypothesized alt-A-greater binding direction is unsubstantiated. | missing | [E05](#e05), [E04](#e04) |
| element | VEP annotates ENSR5_C5GP enhancer at the variant (E01), but E03 reports no overlapping cCRE and a nearest pELS 75 bp away, so the element call is uncertain. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is 0.5 kb from the TSS (E02), but no functional data in this case connect this specific site or JUN binding to TERT expression. | weak | [E02](#e02) |
| cell_type | JUN is expressed in glioblastoma (E05), but no glioblastoma occupancy at this site and no TERT expression data are supplied (E04). | weak | [E05](#e05), [E04](#e04) |
| phenotype | A JUN-driven change in TERT is not directly supported; TERT-cancer literature is generic (E18), E16 is hypertension with PIP 0.00, and TERT is not commonly essential in CNS lines (E20). | missing | [E18](#e18), [E16](#e16), [E20](#e20) |

Predictions: JUN occupies chr5:1295601 in glioblastoma cells and the A allele increases JUN binding.; JUN knockdown or AP-1 site mutation reduces allele-specific TERT reporter activity.

Falsified if: JUN does not occupy the variant site in glioblastoma cells, or JUN perturbation does not affect TERT expression in an allele-dependent manner.

### 4. H_CTCF_Chromatin_Mediated_Effect: The variant alters CTCF binding/chromatin looping near the TERT upstream region, changing TERT regulation in glioblastoma cells. (p = 0.12)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element region 75 bp from nearest pELS/PLS; ENSR5_C5GP annotation uncertain; gene TERT; cell type Glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is expressed in glioblastoma (26.45 TPM, rank 163/1626) and has ENCODE peaks containing the variant in H9/neural progenitor cells (E06); the nearby pELS also has a CTCF z-score of 2.8 (E03). But there is no glioblastoma CTCF peak at this base and no QBiC-SELEX/allele-specific data; the hypothesized direction is that ref G preserves CTCF binding and alt A disrupts it, which is a prediction rather than an established effect. | missing | [E06](#e06), [E03](#e03), [E04](#e04) |
| element | The variant is 75 bp from the nearest pELS/PLS and E03 says no cCRE overlaps it, while E01 calls ENSR5_C5GP enhancer; any CTCF effect would therefore likely involve a nearby element rather than this base being inside a canonical CTCF site. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is 0.5 kb away (E02), but no Hi-C/3C or perturbation data link this CTCF-proximal region to TERT looping or expression. | weak | [E02](#e02) |
| cell_type | CTCF is expressed in glioblastoma (E06), but no glioblastoma occupancy or chromatin-looping data at this site are provided. | weak | [E06](#e06), [E04](#e04) |
| phenotype | A CTCF/insulator effect on TERT in glioblastoma is not directly supported; only generic TERT-cancer literature (E18) and an unrelated hypertension credible set (E16) are supplied. | missing | [E18](#e18), [E16](#e16) |

Predictions: CTCF occupies the nearby pELS but not necessarily the variant base; the A allele reduces CTCF binding at the variant if it is in a CTCF site.; Disrupting CTCF or the variant changes local chromatin looping and TERT expression in glioblastoma cells.

Falsified if: CTCF occupancy and local chromatin looping are unchanged across alleles in glioblastoma cells, or CTCF perturbation does not affect TERT.

## Prediction matrix

| Test | Cost | Separates top two | H_Null | H_Max_TERT | H_JUN_TERT | H_CTCF_Chromatin_Mediated_Effect |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific MAX ChIP-qPCR at chr5:1295601 in a glioblastoma line heterozygous G/A | medium | yes | No MAX occupancy at the variant, or no difference between G and A alleles. | MAX occupies the site and the A allele shows stronger MAX binding than the G allele. | No MAX occupancy; JUN may occupy the site instead. | No MAX occupancy; CTCF may act at the nearby pELS rather than this base. |
| Allele-specific JUN ChIP-qPCR at chr5:1295601 in the same glioblastoma line | medium | no | No JUN occupancy or no allele difference. | No JUN occupancy at the variant. | JUN occupies the site and the A allele shows stronger JUN binding. | No JUN occupancy at the variant. |
| TERT enhancer/reporter assay with G vs A alleles in glioblastoma cells | medium | yes | No allele-specific difference in TERT reporter activity. | Allele-specific TERT reporter activity that is reduced by MAX perturbation or E-box mutation. | Allele-specific TERT reporter activity that is reduced by JUN perturbation or AP-1 site mutation. | No allele-specific reporter effect unless chromatin/looping context is preserved. |
| DepMap TERT CRISPR dependency in CNS/glioblastoma lines | existing data | no | Consistent with weak TERT dependency in CNS lines (median -0.00, 2% dependent). | Weak TERT dependency does not support a strong TERT-driven phenotype in most glioblastoma lines. | Weak TERT dependency does not support a strong TERT-driven phenotype in most glioblastoma lines. | Weak TERT dependency does not support a strong TERT-driven phenotype in most glioblastoma lines. |

## Next experiment

Perform allele-specific MAX ChIP-qPCR at chr5:1295601 in a glioblastoma cell line heterozygous G/A; this directly tests whether MAX occupies the site in the disease-relevant cell type and whether the A allele binds MAX more strongly, separating H_Max_TERT from H_Null.

## Investigate calls

- chip_peaks({"tf": "MAX", "biosample": "Glioblastoma"})
- gene_dependency({"gene": "TERT"})
- literature_search({"query": "TERT upstream enhancer variant allele-specific reporter luciferase rs2853669 glioblastoma"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295601-1295601:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:22:30+00:00)

> Variant chr5:1295601:G>A (GRCh38), allele string G/A
> Known IDs: rs34768248
> Most severe consequence: intron_variant
> Regulatory features: ENSR5_C5GP enhancer
> GERP conservation score at the site: 2.04
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295601-2295601?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:22:31+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295601:G>A, by distance to TSS:
> TERT: 0.5 kb from TSS (upstream, strand -1)
> CLPTM1L: 49.5 kb from TSS (downstream, strand -1)
> SLC6A18: 70.2 kb from TSS (downstream, strand +1)
> SLC6A19: 94.0 kb from TSS (downstream, strand +1)
> SLC12A7: 139.4 kb from TSS (upstream, strand -1)
> SLC6A3: 149.9 kb from TSS (downstream, strand -1)
> LPCAT1: 228.7 kb from TSS (downstream, strand -1)
> NKD2: 287.6 kb from TSS (downstream, strand +1)
> TRIP13: 402.8 kb from TSS (downstream, strand +1)
> BRD9: 402.8 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:21:44+00:00)

> No cCRE overlaps the variant; nearest is EH38E3622531 (pELS) 75 bp away.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622532 pELS: DNase z 2.2, H3K27ac z 3.9, H3K4me3 z 4.4, CTCF z 1.5; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622530 PLS: DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr5:1295601:G>A: 35 peaks contain the variant, from 27 factors in 9 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. No cCRE contains the variant. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, BCL3, DNMT1, DPF2, EZH2, EZH2phosphoT487, GABPB1, IKZF1, KDM4A, MAZ, MTA1, RBBP5 (+5 more). Bound, expressed TFs with a binding model: 10; listed one per row: JUN, CTCF, ZNF687, MAX, CREB1, NR2C2, RXRA, ZBTB33, ZNF800, NKRF. Assayed with no peak here: 0 TFs in the matching biosample, 563 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549 (e.g. ENCSR604CKQ). 91.65 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 16 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: H9, neural progenitor cell (e.g. ENCSR125NBL). 26.45 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 163 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR647PSR). 10.74 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 436 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: H1 (e.g. ENCSR000BSJ). 58.6 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 48 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CREB1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: H1 (e.g. ENCSR000BSN). 30.94 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 132 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C2: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR559ZKI). 20.46 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 223 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> RXRA: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR416HDG). 13.1 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 354 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZBTB33: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: K562 (e.g. ENCSR876GXA). 12.18 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 381 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF800: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR701WPG). 11.64 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 400 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NKRF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR732PJX). 8.69 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 522 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs34768248&size=100; retrieved 2026-10-26T02:22:30+00:00)

> 0 GWAS Catalog associations for rs34768248, strongest first:

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:22:30+00:00)

> 1 credible sets contain 5_1295601_G_A: 1 GWAS, 0 molecular QTL.
> GWAS Hypertension: PIP 0.00; L2G TERT 0.84
> Best L2G gene scores across these sets: TERT 0.84

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295601_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:24:03+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295601_G_A_b38. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs[masked] potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:30:21+00:00)

> No ENCODE MAX ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no MAX experiment in that biosample. In other biosamples, 1 MAX peaks do contain the variant: H1 (experiments ENCSR000BSJ).

<a id="e20"></a>**E20** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for TERT (0 = no effect, -1 = median common-essential; < -0.5 called dependent). CNS/Brain lineage, 50 lines: median -0.00, 2% dependent. All 1183 lines: median -0.02, 1% dependent.

<a id="e21"></a>**E21** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20upstream%20enhancer%20variant%20allele-specific%20reporter%20luciferase%20rs2853669%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:30:22+00:00)

> Europe PMC: 8 hits for 'TERT upstream enhancer variant allele-specific reporter luciferase rs[masked] glioblastoma'; top 6 with PMIDs:
> PMID 37993930 (2023): Targeting oncogenic TERT promoter variants by allele-specific epigenome editing.
> PMID 31408918 (2019): Spectrum of TERT promoter mutations and mechanisms of activation in thyroid cancer.
> PMID 32518154 (2020): ETS variant transcription factor 5 and c-Myc cooperate in derepressing the human telomerase gene promoter via composite ETS/E-box motifs.
> PMID 31903880 (2020): Telomere-related Markers for Cancer.
> PMID 26846696 (2016): Reactivation of telomerase in cancer.
> PMID 31592543 (2019): 17th International Congress of Immunology, 19-23 October 2019, Beijing, China. [no abstract]

<a id="e21a"></a>**E21a** literature_search, Europe PMC abstract, PMID 37993930 (https://europepmc.org/article/MED/37993930; retrieved 2026-10-26T20:30:22+00:00)

> We chose the hepatoblastoma cell line Hep-G2 and the lung cancer cell line A-549 for this proof-of-principle study, as they contained two different kinds of variants, namely the activating mutation C228T in the TERT core promoter and the common SNP rs[masked] in the THOR region, respectively.

<a id="e21b"></a>**E21b** literature_search, Europe PMC abstract, PMID 37993930 (https://europepmc.org/article/MED/37993930; retrieved 2026-10-26T20:30:22+00:00)

> These variants were targeted in an allele-specific manner using sgRNA-guided dCas9-DNMT3A-3L complexes.

<a id="e21c"></a>**E21c** literature_search, Europe PMC abstract, PMID 31408918 (https://europepmc.org/article/MED/31408918; retrieved 2026-10-26T20:30:22+00:00)

> They generate de novo binding sites for E-twenty-six (ETS) transcription factors causing increased TERT transcription.

<a id="e21d"></a>**E21d** literature_search, Europe PMC abstract, PMID 31408918 (https://europepmc.org/article/MED/31408918; retrieved 2026-10-26T20:30:22+00:00)

> The luciferase reporter assay was used to functionally characterize the identified alterations.

<a id="e21e"></a>**E21e** literature_search, Europe PMC abstract, PMID 32518154 (https://europepmc.org/article/MED/32518154; retrieved 2026-10-26T20:30:22+00:00)

> Using chromatinized bacterial artificial chromosome (BAC) reporters in human fibroblasts, we found that ETV5 and c-Myc/MYC-associated factor X (MAX) synergistically activate the hTERT promoter via two identical, but inverted, composite Ets/E-box motifs enclosing the core promoter.

<a id="e21f"></a>**E21f** literature_search, Europe PMC abstract, PMID 32518154 (https://europepmc.org/article/MED/32518154; retrieved 2026-10-26T20:30:22+00:00)

> Mutations of Ets or E-box sites in either DNA motif abolished the activation and reduced or eliminated the synergism.

<a id="e21g"></a>**E21g** literature_search, Europe PMC abstract, PMID 26846696 (https://europepmc.org/article/MED/26846696; retrieved 2026-10-26T20:30:22+00:00)

> Newly described non-coding mutations in the Tert promoter region of many cancer cells (19 %) in two key positions, C250T and C228T, have added another layer of complexity to telomerase reactivation.

<a id="e21h"></a>**E21h** literature_search, Europe PMC abstract, PMID 26846696 (https://europepmc.org/article/MED/26846696; retrieved 2026-10-26T20:30:22+00:00)

> These mutations create novel consensus sequences for transcription factors which can enhance Tert expression.
