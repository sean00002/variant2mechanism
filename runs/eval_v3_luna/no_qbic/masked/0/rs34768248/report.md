# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 147 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.91)

Null chain: no TF-mediated effect of this variant.

Predictions: In relevant cells, the variant will not produce a reproducible allele-specific TF-occupancy and downstream regulatory effect; any disease association could reflect linkage, another mechanism, or chance.

Falsified if: A variant-specific allele difference in TF occupancy is demonstrated in a relevant context and perturbing that TF or the variant changes regulation of a linked gene.

### 2. H1: Candidate JUN-dependent effect near TERT (p = 0.04)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps the computational ENSR5_C5GP enhancer annotation, but does not overlap a listed ENCODE cCRE; the specific regulatory element is unresolved.; gene TERT; cell type Glioblastoma cells, as a candidate context; JUN occupancy at the site in that context has not been shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is a candidate, not an established causal TF: it is expressed in the reported glioblastoma-line context and has variant-overlapping peaks only in other biosamples. No allele-specific assay or QBiC-SELEX result is supplied, so the proposed greater binding to alt A is an unverified, testable direction rather than an evidence-supported conclusion. JUN is prioritized only weakly among candidates because its reported expression is high and its peaks include A549; these do not establish occupancy in glioblastoma. | missing | [E04](#e04), [E05](#e05), [E19](#e19) |
| element | The site has a computational enhancer annotation, but no listed ENCODE cCRE overlaps it; nearby cCREs do not establish activity at this site in glioblastoma. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is very close to the variant and is a plausible candidate target, but no supplied evidence demonstrates regulation of TERT from this site. | weak | [E01](#e01), [E02](#e02) |
| cell_type | JUN is expressed in the stated glioblastoma DepMap context, but the reported site-overlapping JUN peaks are from A549, not that context. | weak | [E05](#e05), [E19](#e19) |
| phenotype | TERT biology is relevant to glioblastoma and melanoma generally, but the supplied evidence does not connect this variant or a JUN-mediated effect to any listed disease; it provides no specific support for bladder disease. | weak | [E18a](#e18a), [E18e](#e18e), [E18h](#e18h) |

Predictions: In a relevant glioblastoma model, this hypothesis predicts greater JUN occupancy on alt A than ref G at the variant. This binding direction is speculative because no allele-specific binding evidence is supplied.; If JUN occupancy is causal, perturbing JUN or the variant should alter regulation of a linked gene; the direction of any TERT-expression change cannot be inferred from the supplied evidence.

Falsified if: A sensitive assay in relevant cells finds no variant-overlapping JUN occupancy or no alt-favored JUN occupancy.; Despite confirmed JUN occupancy, perturbing JUN and the variant has no effect on regulation of a linked gene.

### 3. H2: Candidate CTCF-dependent local architecture (p = 0.03)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element A possible local regulatory or architectural region; the variant is outside the listed ENCODE cCREs, and a specific CTCF element is not established.; gene TERT; cell type Glioblastoma cells, conditionally; CTCF occupancy at the site in this context has not been shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF has variant-overlapping peaks in other biosamples and is expressed in the reported glioblastoma-line context. No matched-context allele-specific assay or QBiC-SELEX result is supplied; stronger binding to ref G is a speculative test direction, not an established allelic effect. | missing | [E04](#e04), [E06](#e06), [E20](#e20) |
| element | The variant has a computational enhancer annotation and nearby cCREs, but none of the listed cCREs overlaps the site; this does not establish a CTCF architectural element. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is nearby and a plausible candidate target, but no CTCF-mediated connection from this site to TERT is demonstrated. | weak | [E01](#e01), [E02](#e02) |
| cell_type | CTCF is expressed in the stated glioblastoma DepMap context, whereas the reported site-overlapping peaks are from H9 and neural progenitor cells. | weak | [E06](#e06), [E20](#e20) |
| phenotype | TERT promoter alterations are discussed in glioblastoma literature, but the evidence does not connect this variant or a CTCF-mediated effect to the listed diseases. | weak | [E18e](#e18e), [E18h](#e18h) |

Predictions: In a relevant glioblastoma model, this hypothesis predicts greater CTCF occupancy on ref G than alt A at the variant; this direction is speculative.; If causal, the allelic difference should track with CTCF-dependent local chromatin contacts or insulation and should be altered by CTCF perturbation. The direction of a TERT-expression change is not established.

Falsified if: A sensitive assay in relevant cells finds no variant-overlapping CTCF occupancy or no ref-favored occupancy.; Confirmed CTCF occupancy is not accompanied by allele-dependent local architecture or a CTCF-dependent regulatory effect.

### 4. H3: Candidate ZBTB33-dependent repression (p = 0.02)

TF ZBTB33 (QBiC-SELEX coverage own_model), ref allele binds more; element A candidate local regulatory region; the variant is annotated as enhancer-like computationally, but the nearby ENCODE cCREs do not overlap it.; gene TERT; cell type Glioblastoma cells, conditionally; ZBTB33 occupancy at the site in this context has not been shown..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZBTB33 has a variant-overlapping peak only in K562 and is expressed in the reported glioblastoma-line context. No matched-context allele-specific assay or QBiC-SELEX result is supplied; stronger binding to ref G is a speculative direction, not a supported allelic effect. | missing | [E04](#e04), [E12](#e12), [E21](#e21) |
| element | The site has a computational enhancer annotation, but the nearest listed ENCODE cCRE is 75 bp away and does not overlap; activity of a specific element in glioblastoma is unresolved. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is nearby and a plausible candidate target, but a regulatory connection from this site to TERT has not been demonstrated. | weak | [E01](#e01), [E02](#e02) |
| cell_type | ZBTB33 is expressed in the stated glioblastoma DepMap context, but its reported site-overlapping peak is from K562 rather than a matched context. | weak | [E12](#e12), [E21](#e21) |
| phenotype | General TERT/glioblastoma context makes the proposed target biologically plausible, but no evidence connects this variant or a ZBTB33-mediated effect to the listed diseases. | weak | [E18e](#e18e), [E18h](#e18h) |

Predictions: In a relevant glioblastoma model, this hypothesis predicts greater ZBTB33 occupancy on ref G than alt A at the variant; this direction is speculative.; If ZBTB33 acts here as a repressor, ref G should be associated with stronger repression than alt A, and the expression difference should diminish when ZBTB33 is depleted.

Falsified if: A sensitive assay in relevant cells finds no variant-overlapping ZBTB33 occupancy or no ref-favored occupancy.; ZBTB33 depletion does not alter a reproducible allele-associated regulatory effect.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific JUN CUT&RUN or targeted ChIP in genotyped glioblastoma cells, with reads assigned to ref G versus alt A | low | yes | No reproducible allele-specific JUN occupancy at the site. | JUN occupies the site and shows greater occupancy on alt A than ref G. | No required JUN allelic effect; JUN occupancy may be absent or not alt-favored. | No required JUN allelic effect; JUN occupancy may be absent or not alt-favored. |
| Allele-specific CTCF CUT&RUN or targeted ChIP in genotyped glioblastoma cells, with a local chromatin-contact or insulation readout | medium | no | No reproducible ref-favored CTCF occupancy linked to allele-dependent local architecture. | No required CTCF-dependent architectural effect. | Ref G shows greater CTCF occupancy, with an allele-dependent local architecture readout. | No required CTCF-dependent architectural effect. |
| Allele-specific ZBTB33 occupancy and TERT-expression measurement before and after ZBTB33 depletion in genotyped glioblastoma cells | medium | no | No reproducible ref-favored occupancy coupled to a ZBTB33-dependent allele-associated expression effect. | No required ZBTB33-dependent repression. | No required ZBTB33-dependent repression. | Ref G shows greater ZBTB33 occupancy and stronger repression; depletion diminishes the allele-associated expression difference. |

## Next experiment

Perform allele-specific JUN CUT&RUN (or targeted ChIP-qPCR with allele-resolved sequencing) in genotyped glioblastoma cells. It is the lowest-cost proposed test that directly distinguishes the leading non-null candidate, H1, from the null; greater JUN occupancy on alt A would support H1, while no reproducible allelic occupancy would favor H0.

## Investigate calls

- chip_peaks({"tf": "JUN", "biosample": "Glioblastoma"})
- chip_peaks({"tf": "CTCF", "biosample": "Glioblastoma"})
- chip_peaks({"tf": "ZBTB33", "biosample": "Glioblastoma"})

## Flags

- none

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

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> A major molecular feature of melanoma is abnormal telomerase activation; this is most often caused by telomerase reverse transcriptase (TERT) promoter mutations, which occur in 50-82% of cases and are the most common noncoding alteration in this cancer.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> Conclusions: Understanding both telomere-dependent and -independent TERT functions is essential for developing effective biomarkers and therapies that overcome resistance and slow melanoma progression.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> The genetic landscape of familial melanoma is heterogeneous.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> Mutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> The rs[masked] C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e18g"></a>**E18g** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e18h"></a>**E18h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e18i"></a>**E18i** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> The prognostic relevance of CDKN2A deletion may vary according to TERTp status, particularly for OS.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:33:47+00:00)

> No ENCODE JUN ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 2 JUN peaks do contain the variant: A549 (experiments ENCSR604CKQ, ENCSR628MQN).

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:33:47+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no CTCF experiment in that biosample. In other biosamples, 2 CTCF peaks do contain the variant: H9, neural progenitor cell (experiments ENCSR125NBL, ENCSR871MKQ).

<a id="e21"></a>**E21** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:25:43+00:00)

> No ENCODE ZBTB33 ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no ZBTB33 experiment in that biosample. In other biosamples, 1 ZBTB33 peaks do contain the variant: K562 (experiments ENCSR876GXA).
