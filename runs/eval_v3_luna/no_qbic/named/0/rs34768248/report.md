# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 167 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: No TF-mediated effect of rs34768248 (p = 0.90)

Null chain: no TF-mediated effect of this variant.

Predictions: There will be no reproducible allele-specific TF-binding and regulatory effect attributable to this base in disease-relevant cells.; Any disease association, if one exists, will be due to another variant or mechanism; the supplied evidence does not establish an association for rs34768248.

Falsified if: A reproducible allele-specific TF-binding change at rs34768248 is linked to a regulatory effect on a disease-relevant gene in relevant cells.

### 2. H2: Candidate JUN-mediated regulation near TERT (p = 0.04)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element The variant may act through a nearby regulatory region, but its enhancer annotation is computational and no ENCODE cCRE overlaps the base.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is a candidate because it is expressed in the stated glioblastoma context and has ChIP peaks over the variant in A549. These data do not establish JUN occupancy in glioblastoma, and no allele-specific assay or QBiC-SELEX result is supplied. Alt-more binding is an unsupported working prediction, not an evidence-based direction; the supplied evidence does not distinguish JUN from the other reported candidates. | weak | [E04](#e04), [E05](#e05) |
| element | VEP annotates an enhancer feature at the variant, but this is computational evidence; no ENCODE cCRE overlaps the base, and the nearest listed cCRE is 75 bp away. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is about 0.5 kb from the variant by the reported TSS distance, making it a plausible candidate target but not establishing regulation by this variant. | weak | [E02](#e02) |
| cell_type | Glioblastoma is a proposed context based on the expression context, but the supplied JUN peaks are from A549 and no matching glioblastoma occupancy is shown. | weak | [E04](#e04), [E05](#e05) |
| phenotype | TERT has general relevance to cancer, including glioblastoma, but the supplied evidence does not connect rs34768248 or JUN-mediated regulation to the listed diseases; no rs34768248 GWAS association or significant GTEx eQTL is reported. | missing | [E15](#e15), [E17](#e17), [E18a](#e18a), [E18e](#e18e), [E18h](#e18h), [E20](#e20) |

Predictions: A JUN-specific assay using ref and alt sequences will show greater binding to the alt allele if this working hypothesis is correct; this direction is not supported by current binding evidence.; In relevant cells, editing the variant or perturbing JUN may change TERT regulation, but neither the direction nor the existence of that effect is established.

Falsified if: A sufficiently sensitive JUN-specific assay finds no reproducible ref-versus-alt binding difference.; Editing the variant and perturbing JUN in relevant cells produce no linked change in TERT regulation.

### 3. H3: Candidate CTCF-mediated regulation near TERT (p = 0.03)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element The variant may affect a nearby regulatory region, but its enhancer annotation is computational and no ENCODE cCRE overlaps the base.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is a candidate because it has ChIP peaks over the variant in neural progenitor cells and is expressed in the stated glioblastoma context. This does not establish glioblastoma occupancy, and no allele-specific assay or QBiC-SELEX result is supplied. Alt-more binding is an unsupported working prediction, not an evidence-based direction; the supplied evidence does not distinguish CTCF from the other reported candidates. | weak | [E04](#e04), [E06](#e06) |
| element | VEP annotates an enhancer feature at the variant, but this is computational evidence; no ENCODE cCRE overlaps the base, and the nearest listed cCRE is 75 bp away. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is about 0.5 kb from the variant by the reported TSS distance, but proximity does not establish a regulatory or chromatin-architecture effect on TERT. | weak | [E02](#e02) |
| cell_type | Glioblastoma is a proposed context, but the reported CTCF peaks are from neural progenitor cells and do not demonstrate occupancy in glioblastoma. | weak | [E04](#e04), [E06](#e06) |
| phenotype | General literature supports TERT relevance to cancer, but does not connect rs34768248 or a CTCF-mediated effect to the listed diseases; no rs34768248 GWAS association or significant GTEx eQTL is reported. | missing | [E15](#e15), [E17](#e17), [E18a](#e18a), [E18e](#e18e), [E18h](#e18h), [E20](#e20) |

Predictions: A CTCF-specific assay using ref and alt sequences will show greater binding to the alt allele if this working hypothesis is correct; this direction is not supported by current binding evidence.; In relevant cells, editing the variant or perturbing CTCF may change local regulation, but no effect on chromatin contacts or TERT is established.

Falsified if: A sufficiently sensitive CTCF-specific assay finds no reproducible ref-versus-alt binding difference.; Editing the variant and perturbing CTCF in relevant cells produce no linked regulatory effect.

### 4. H4: Candidate MAX-mediated regulation near TERT (p = 0.03)

TF MAX (QBiC-SELEX coverage own_model), alt allele binds more; element The variant may act through a nearby regulatory region, but its enhancer annotation is computational and no ENCODE cCRE overlaps the base.; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MAX is a candidate because it is expressed in the stated glioblastoma context and has a ChIP peak over the variant in H1. This does not establish MAX occupancy in glioblastoma, and no allele-specific assay or QBiC-SELEX result is supplied. Alt-more binding is an unsupported working prediction, not an evidence-based direction; the supplied evidence does not distinguish MAX from the other reported candidates. | weak | [E04](#e04), [E08](#e08) |
| element | VEP annotates an enhancer feature at the variant, but this is computational evidence; no ENCODE cCRE overlaps the base, and the nearest listed cCRE is 75 bp away. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is about 0.5 kb from the variant by the reported TSS distance, making it a plausible candidate target but not establishing regulation by this variant. | weak | [E02](#e02) |
| cell_type | Glioblastoma is a proposed context, but the reported MAX peak is from H1 and does not demonstrate MAX occupancy in glioblastoma. | weak | [E04](#e04), [E08](#e08) |
| phenotype | General literature supports TERT relevance to cancer, but does not connect rs34768248 or a MAX-mediated effect to the listed diseases; no rs34768248 GWAS association or significant GTEx eQTL is reported. | missing | [E15](#e15), [E17](#e17), [E18a](#e18a), [E18e](#e18e), [E18h](#e18h), [E20](#e20) |

Predictions: A MAX-specific assay using ref and alt sequences will show greater binding to the alt allele if this working hypothesis is correct; this direction is not supported by current binding evidence.; In relevant cells, editing the variant or perturbing MAX may change TERT regulation, but neither the direction nor the existence of that effect is established.

Falsified if: A sufficiently sensitive MAX-specific assay finds no reproducible ref-versus-alt binding difference.; Editing the variant and perturbing MAX in relevant cells produce no linked change in TERT regulation.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Low-cost TF-specific EMSA or equivalent ref-versus-alt binding assay using glioblastoma nuclear extract, with JUN, CTCF, and MAX identified by specific supershift or equivalent detection. | low | yes | No reproducible allele-specific binding difference for the candidate TFs. | A reproducible JUN-dependent difference, with greater binding to alt under this chain's unsupported working prediction. | A reproducible CTCF-dependent difference, with greater binding to alt under this chain's unsupported working prediction. | A reproducible MAX-dependent difference, with greater binding to alt under this chain's unsupported working prediction. |
| Edit ref to alt and alt to ref in a relevant glioblastoma model; measure TERT expression with and without perturbation of the candidate TFs. | high | no | No reproducible variant-dependent TERT effect linked to JUN, CTCF, or MAX perturbation. | A variant-dependent TERT effect that changes with JUN perturbation. | A variant-dependent TERT or local-regulatory effect that changes with CTCF perturbation. | A variant-dependent TERT effect that changes with MAX perturbation. |

## Next experiment

Run the low-cost ref-versus-alt TF-specific binding assay with glioblastoma nuclear extract, testing JUN, CTCF, and MAX. It is the cheapest direct test separating the highest-probability null chain from the JUN candidate, while also comparing the other plausible TFs. The alt-more direction is only a provisional working prediction. A positive binding difference would still need follow-up in chromatin and with a regulatory readout to establish a disease mechanism.

## Investigate calls

- chip_peaks({"tf": "JUN", "biosample": "Glioblastoma"})
- literature_search({"query": "rs34768248 (glioblastoma OR melanoma OR bladder)"})
- gene_disease({"gene": "TERT"})

## Flags

- literature_fallback: no hits for 'rs34768248 AND TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; dropped the rsID
- tool_failed: E21 gene_disease: Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'

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

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> A major molecular feature of melanoma is abnormal telomerase activation; this is most often caused by telomerase reverse transcriptase (TERT) promoter mutations, which occur in 50-82% of cases and are the most common noncoding alteration in this cancer.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> Conclusions: Understanding both telomere-dependent and -independent TERT functions is essential for developing effective biomarkers and therapies that overcome resistance and slow melanoma progression.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> The genetic landscape of familial melanoma is heterogeneous.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> BackgroundMutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> ConclusionThe rs2853669 C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e18g"></a>**E18g** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e18h"></a>**E18h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e18i"></a>**E18i** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> The prognostic relevance of CDKN2A deletion may vary according to TERTp status, particularly for OS.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:33:47+00:00)

> No ENCODE JUN ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 2 JUN peaks do contain the variant: A549 (experiments ENCSR604CKQ, ENCSR628MQN).

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs34768248%20%28glioblastoma%20OR%20melanoma%20OR%20bladder%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:30:11+00:00)

> Europe PMC: 0 hits for 'rs34768248 (glioblastoma OR melanoma OR bladder)'; top 0 with PMIDs:

<a id="e21"></a>**E21** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'
