# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 121 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H0: Null: no TF-mediated effect of rs34768248 (p = 0.86)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at chr5:1295601 in glioblastoma-relevant cells.; The G>A change alone does not alter TERT expression or a disease-relevant phenotype.; Any TERT association is driven by a linked causal variant rather than this base.

Falsified if: Allele-specific CTCF ChIP or footprinting in glioblastoma cells shows reproducible ref-G enrichment at chr5:1295601.; An allele-specific reporter/MPRA in a TERT-expressing glioblastoma line shows a G>A effect at this base after controlling for linked variants.; CTCF perturbation at this element changes TERT expression in cis in a glioblastoma-relevant cell type.

### 2. H1: CTCF binding at a TERT upstream element (p = 0.08)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element TERT upstream ENSR5_C5GP enhancer/promoter-proximal region; variant is not inside an annotated ENCODE cCRE and lies 75 bp from a pELS; gene TERT; cell type glioblastoma/glial-lineage cells; CTCF occupancy has been seen only in H9 neural progenitor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is the candidate TF, with ref G hypothesized to bind more strongly than alt A. CTCF has no QBiC-SELEX model in the provided evidence, so the direction is not measured. CTCF ChIP peaks containing the variant are reported only in H9/neural progenitor cells, not in the glioblastoma expression context; E19 explicitly reports no glioblastoma CTCF peak. | weak | [E04](#e04), [E06](#e06), [E19](#e19) |
| element | The variant lies in the computationally annotated TERT upstream ENSR5_C5GP enhancer. It is not contained in an ENCODE cCRE; the nearest pELS is 75 bp away, so the active-element evidence does not overlap the base. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.5 kb upstream, and is the best L2G gene in the available credible set. Caveat: that credible set is for hypertension with PIP 0.00, not glioblastoma/melanoma/bladder cancer. | weak | [E02](#e02), [E16](#e16) |
| cell_type | CTCF is expressed in glioblastoma lines, but glioblastoma CTCF occupancy at this base is not established. The only reported CTCF peaks containing the variant are in H9 neural progenitor cells. | weak | [E04](#e04), [E06](#e06), [E19](#e19) |
| phenotype | TERT is broadly implicated in glioblastoma, melanoma and bladder cancer, but this variant has no direct GWAS Catalog association and no significant GTEx eQTL. Phenotype support is therefore gene-level and not variant-specific. | weak | [E15](#e15), [E17](#e17), [E18](#e18) |

Predictions: Allele-specific CTCF ChIP-qPCR in glioblastoma or neural progenitor cells will show preferential ref-G binding at chr5:1295601.; The ref-G allele preserves a CTCF-binding motif that alt A weakens.; CTCF perturbation at this element changes TERT expression in the relevant neural-lineage context.

Falsified if: Allele-specific CTCF ChIP-qPCR or footprinting in glioblastoma cells shows no occupancy or no ref-G enrichment at this base.; The G>A change does not alter CTCF binding in vitro or in a neural-lineage cell context.; CTCF perturbation at this element does not change TERT expression in the relevant cell type.

### 3. H2: JUN/AP-1 binding gain at the TERT upstream region (p = 0.06)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element TERT upstream ENSR5_C5GP enhancer/promoter-proximal region; variant is near active pELS elements but not inside an annotated cCRE; gene TERT; cell type glioblastoma cells; JUN occupancy at this base is reported only in A549.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is the candidate TF, with alt A hypothesized to bind more strongly than ref G. JUN has no QBiC-SELEX model in the provided evidence, so the direction is not measured. JUN ChIP peaks containing the variant are reported only in A549, not in the glioblastoma expression context. | weak | [E04](#e04), [E05](#e05), [E20](#e20) |
| element | The variant lies in the TERT upstream ENSR5_C5GP enhancer and near active pELS elements, but it is not contained in an ENCODE cCRE. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.5 kb upstream, and is the best L2G gene in the available credible set. Caveat: that credible set is for hypertension with PIP 0.00, not the disease context. | weak | [E02](#e02), [E16](#e16) |
| cell_type | JUN is highly expressed in glioblastoma lines, but the only JUN ChIP peak containing this variant is from A549; glioblastoma occupancy at this base is not established. | weak | [E04](#e04), [E05](#e05), [E20](#e20) |
| phenotype | TERT is implicated in the relevant cancers, but this variant lacks direct GWAS Catalog association and GTEx eQTL support. Phenotype support remains gene-level rather than variant-specific. | weak | [E15](#e15), [E17](#e17), [E18](#e18) |

Predictions: Allele-specific JUN ChIP-qPCR in glioblastoma cells will show preferential alt-A binding at chr5:1295601.; Alt A creates or improves an AP-1/JUN binding motif.; JUN inhibition reduces TERT expression specifically in cells carrying the alt allele.

Falsified if: JUN ChIP-qPCR or footprinting in glioblastoma cells shows no occupancy or no alt-A enrichment at this base.; The G>A change does not create or strengthen an AP-1/JUN-like site in an allele-specific reporter assay.; JUN perturbation does not change TERT expression in a glioblastoma cell line carrying the alt allele.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific CTCF ChIP-qPCR at rs34768248 in a glioblastoma cell line | low | yes | No reproducible allele-specific CTCF occupancy at chr5:1295601 in glioblastoma cells. | Ref-G enrichment in CTCF ChIP-qPCR or allele-specific footprinting in glioblastoma/neural-lineage cells. | No CTCF allele-specific effect; any signal would not support the JUN-gain model. |
| Allele-specific luciferase reporter or MPRA for G vs A in a TERT-expressing glioblastoma line | low | yes | No allele-specific reporter/MPRA effect for G>A. | Ref-G-dependent change consistent with CTCF binding, but activity direction could be activation or repression. | Alt-A-dependent change consistent with AP-1/JUN gain. |
| Allele-specific JUN ChIP-qPCR at rs34768248 in a glioblastoma cell line | medium | no | No alt-A-specific JUN occupancy at this base. | No JUN allele-specific effect; CTCF model unaffected. | Alt-A enrichment in JUN ChIP-qPCR in glioblastoma cells. |
| CRISPRi/dCas9 perturbation of the TERT upstream element plus TERT qPCR in glioblastoma cells | high | yes | No change in TERT expression after local CRISPRi/dCas9 perturbation of the element. | CTCF-dependent change in TERT expression, preferentially in the ref-G context. | JUN-dependent change in TERT expression, preferentially in the alt-A context. |

## Next experiment

The single cheapest experiment that separates the top two chains (H0 vs H1) is allele-specific CTCF ChIP-qPCR at rs34768248 in a glioblastoma cell line. H0 predicts no reproducible allele-specific CTCF occupancy; H1 predicts ref-G enrichment. If glioblastoma CTCF occupancy is absent, repeat in H9 neural progenitor cells as a lower-disease-relevance fallback to test the H1 binding link, but that fallback alone would not establish glioblastoma relevance.

## Investigate calls

- chip_peaks({"tf": "CTCF", "biosample": "glioblastoma"})
- chip_peaks({"tf": "JUN", "biosample": "glioblastoma"})
- literature_search({"query": "rs34768248 TERT allele-specific reporter"})

## Flags

- literature_fallback: no hits for 'rs34768248 AND TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; dropped the rsID
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
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:33:47+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'glioblastoma'. Absence can also mean no CTCF experiment in that biosample. In other biosamples, 2 CTCF peaks do contain the variant: H9, neural progenitor cell (experiments ENCSR125NBL, ENCSR871MKQ).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:33:47+00:00)

> No ENCODE JUN ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'glioblastoma'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 2 JUN peaks do contain the variant: A549 (experiments ENCSR604CKQ, ENCSR628MQN).

<a id="e21"></a>**E21** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs34768248%20TERT%20allele-specific%20reporter&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:33:47+00:00)

> Europe PMC: 0 hits for 'rs34768248 TERT allele-specific reporter'; top 0 with PMIDs:
