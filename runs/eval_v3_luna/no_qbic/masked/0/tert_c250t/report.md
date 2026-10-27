# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 9 model calls; 197 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.88)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not produce a reproducible TF-dependent difference in TERT regulation; any disease association could arise from linkage or another process.

Falsified if: Changing this base alone reproducibly alters TERT regulation in relevant cells, and the effect depends on a specific TF.

### 2. H1: Candidate MAX-mediated effect at the TERT promoter (p = 0.06)

TF MAX (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3622530, a promoter-like cCRE overlapping the variant; gene TERT; cell type Glioblastoma cells (candidate context; occupancy is not established there).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The provisional direction for this candidate is greater MAX binding to alt than ref, but this is an untested assumption: MAX has variant-overlapping ChIP peaks only in other biosamples, and no QBiC-SELEX allele-effect result is supplied. MAX is a candidate because it is expressed in the glioblastoma DepMap context and has those ChIP records. | missing | [E04](#e04), [E05](#e05), [E16](#e16) |
| element | The variant overlaps promoter-like cCRE EH38E3622530, whose reported active-chromatin scores are maxima across biosamples rather than glioblastoma-specific measurements. | supported | [E03](#e03) |
| gene | TERT is immediately adjacent to the variant and near the overlapping promoter-like element, making it a plausible but unproven target; no brain-cortex eQTL is reported. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E17](#e17) |
| cell_type | MAX is expressed in the glioblastoma DepMap context, but the reported variant-overlapping MAX peaks are from other biosamples and do not establish occupancy in glioblastoma cells. | weak | [E04](#e04), [E05](#e05), [E16](#e16) |
| phenotype | TERT promoter mutations are relevant to glioblastoma generally, but the evidence does not connect this variant or MAX to the disease. | weak | [E15d](#e15d), [E15h](#e15h), [E18](#e18) |

Predictions: A TERT-promoter reporter carrying the two alleles should differ in a glioblastoma cell line, with greater MAX binding to alt as the provisional direction; MAX depletion should reduce or remove the reporter difference. The direction of any TERT-expression effect is not established.; Unlike the JUN and GABPA candidates, a MAX-dependent reporter effect is predicted.

Falsified if: A reproducible allele-dependent reporter effect persists unchanged after MAX depletion, or no allele-dependent effect is detected under conditions with demonstrable MAX activity.; A relevant-cell binding assay shows greater MAX binding to ref rather than alt.

### 3. H2: Candidate JUN-mediated effect at the TERT promoter (p = 0.04)

TF JUN (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E3622530, a promoter-like cCRE overlapping the variant; gene TERT; cell type Glioblastoma cells (candidate context; occupancy is not established there).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The provisional direction for this candidate is greater JUN binding to ref than alt, but this is an untested assumption: JUN has variant-overlapping ChIP peaks only in A549, and no QBiC-SELEX allele-effect result is supplied. JUN is a candidate because it is expressed in the glioblastoma DepMap context and has those ChIP records. | missing | [E04](#e04), [E06](#e06) |
| element | The variant overlaps promoter-like cCRE EH38E3622530, whose reported active-chromatin scores are maxima across biosamples rather than glioblastoma-specific measurements. | supported | [E03](#e03) |
| gene | TERT is immediately adjacent to the variant and near the overlapping promoter-like element, making it a plausible but unproven target; no brain-cortex eQTL is reported. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E17](#e17) |
| cell_type | JUN is expressed in the glioblastoma DepMap context, but its reported variant-overlapping peaks are from A549 rather than a matching context. | weak | [E04](#e04), [E06](#e06) |
| phenotype | TERT promoter mutations are relevant to glioblastoma generally, but the evidence does not connect this variant or JUN to the disease. | weak | [E15d](#e15d), [E15h](#e15h), [E18](#e18) |

Predictions: A TERT-promoter reporter carrying the two alleles should differ in a glioblastoma cell line, with greater JUN binding to ref as the provisional direction; JUN depletion should reduce or remove the reporter difference. The direction of any TERT-expression effect is not established.; Unlike the MAX and GABPA candidates, a JUN-dependent reporter effect is predicted.

Falsified if: A reproducible allele-dependent reporter effect persists unchanged after JUN depletion, or no allele-dependent effect is detected under conditions with demonstrable JUN activity.; A relevant-cell binding assay shows greater JUN binding to alt rather than ref.

### 4. H3: Candidate GABPA-mediated effect at the TERT promoter (p = 0.03)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3622530, a promoter-like cCRE overlapping the variant; gene TERT; cell type Glioblastoma cells (candidate context; occupancy is not established there).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The provisional direction for this candidate is greater GABPA binding to alt than ref, but this is an untested assumption: GABPA has variant-overlapping ChIP peaks only in other biosamples, and no QBiC-SELEX allele-effect result is supplied. GABPA is a candidate because it is expressed in the glioblastoma DepMap context and has those ChIP records. | missing | [E04](#e04), [E11](#e11) |
| element | The variant overlaps promoter-like cCRE EH38E3622530, whose reported active-chromatin scores are maxima across biosamples rather than glioblastoma-specific measurements. | supported | [E03](#e03) |
| gene | TERT is immediately adjacent to the variant and near the overlapping promoter-like element, making it a plausible but unproven target; no brain-cortex eQTL is reported. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E17](#e17) |
| cell_type | GABPA is expressed in the glioblastoma DepMap context, but its reported variant-overlapping peaks are from other biosamples and do not establish occupancy in glioblastoma cells. | weak | [E04](#e04), [E11](#e11) |
| phenotype | TERT promoter mutations are relevant to glioblastoma generally, but the evidence does not connect this variant or GABPA to the disease. | weak | [E15d](#e15d), [E15h](#e15h), [E18](#e18) |

Predictions: A TERT-promoter reporter carrying the two alleles should differ in a glioblastoma cell line, with greater GABPA binding to alt as the provisional direction; GABPA depletion should reduce or remove the reporter difference. The direction of any TERT-expression effect is not established.; Unlike the MAX and JUN candidates, a GABPA-dependent reporter effect is predicted.

Falsified if: A reproducible allele-dependent reporter effect persists unchanged after GABPA depletion, or no allele-dependent effect is detected under conditions with demonstrable GABPA activity.; A relevant-cell binding assay shows greater GABPA binding to ref rather than alt.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Query existing ENCODE data for MAX occupancy at the variant in glioblastoma-matched biosamples | existing data | no | No matching MAX peak is expected, though a peak alone would not rule out the null because occupancy need not be causal. | A matching MAX peak is expected, but it would not establish an allelic binding difference or a functional effect. | No matching MAX peak is specifically predicted; JUN-dependent activity could occur independently. | No matching MAX peak is specifically predicted; GABPA-dependent activity could occur independently. |
| Compare ref- and alt-allele DNA probes in a TF-specific binding assay for MAX, JUN, and GABPA | low | no | No reproducible TF-specific allele difference is expected, although an in-vitro binding difference alone would not establish a functional effect. | A MAX-specific allele-binding difference is expected, provisionally stronger for alt. | A JUN-specific allele-binding difference is expected, provisionally stronger for ref. | A GABPA-specific allele-binding difference is expected, provisionally stronger for alt. |
| In a glioblastoma cell line, compare ref- and alt-allele TERT-promoter reporters with control or TF-specific depletion of MAX, JUN, or GABPA | medium | yes | No reproducible allele-dependent reporter difference, or any difference does not depend specifically on one of these TFs. | An allele-dependent reporter difference is reduced or lost with MAX depletion; alt is provisionally predicted to bind MAX more strongly. | An allele-dependent reporter difference is reduced or lost with JUN depletion; ref is provisionally predicted to bind JUN more strongly. | An allele-dependent reporter difference is reduced or lost with GABPA depletion; alt is provisionally predicted to bind GABPA more strongly. |
| Precisely edit the variant in a glioblastoma cell line and measure TERT expression and allele-specific TF occupancy | high | yes | Editing the base produces no reproducible change in TERT expression or TF occupancy attributable to this variant. | Editing produces a reproducible change in TERT expression linked to MAX occupancy or MAX perturbation. | Editing produces a reproducible change in TERT expression linked to JUN occupancy or JUN perturbation. | Editing produces a reproducible change in TERT expression linked to GABPA occupancy or GABPA perturbation. |

## Next experiment

Run the medium-cost ref/alt TERT-promoter reporter assay in a glioblastoma cell line with control and separate MAX, JUN, and GABPA depletion. This is the cheapest listed experiment expected to distinguish the leading null hypothesis from the leading TF-mediated candidate while testing which, if any, TF dependence is specific.

## Investigate calls

- chip_peaks({"tf": "MAX", "biosample": "Glioblastoma"})
- eqtl_lookup({"tissue": "Brain - Cortex"})
- literature_search({"query": "chr5:1295135 G>A TERT glioblastoma melanoma bladder variant"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295135-1295135:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:00+00:00)

> Variant chr5:1295135:G>A (GRCh38), allele string G/A
> Known IDs: rs1561215364
> Most severe consequence: upstream_gene_variant
> Regulatory features: ENSR5_832QG promoter
> GERP conservation score at the site: -4.69
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295135-2295135?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:54+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295135:G>A, by distance to TSS:
> TERT: 0.0 kb from TSS (upstream, strand -1)
> CLPTM1L: 50.0 kb from TSS (downstream, strand -1)
> SLC6A18: 69.8 kb from TSS (downstream, strand +1)
> SLC6A19: 93.5 kb from TSS (downstream, strand +1)
> SLC12A7: 138.9 kb from TSS (upstream, strand -1)
> SLC6A3: 150.4 kb from TSS (downstream, strand -1)
> LPCAT1: 229.1 kb from TSS (downstream, strand -1)
> NKD2: 287.1 kb from TSS (downstream, strand +1)
> TRIP13: 402.3 kb from TSS (downstream, strand +1)
> BRD9: 402.3 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E3622530 (PLS: promoter-like), chr5:1294945-1295294.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622530 PLS (contains the variant): DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622529 pELS: DNase z 3.7, H3K27ac z 4.1, H3K4me3 z 4.6, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr5:1295135:G>A: 113 peaks contain the variant, from 47 factors in 22 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: PLS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, BCL3, DMAP1, EZH2, EZH2phosphoT487, GABPB1, HDAC1, HNRNPK, IKZF1, KDM4A, LIN54, MAZ (+16 more). Bound, expressed TFs with a binding model: 18; listed one per row: MAX, JUN, BHLHE40, E2F4, EGR1, CTCF, GABPA, ZNF687, NR2C1, ZNF143; also bound: SP2, TGIF2, MNT, ZBTB7A, E2F5, ZBTB26, KLF12, ZNF48. Bound but below 1 TPM: ZFHX2. Assayed with no peak here: 0 TFs in the matching biosample, 554 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 12 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, HCT116, HepG2, Ishikawa, K562, NB4 (+1 more) (e.g. ENCSR000BLP). 58.6 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 48 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 11 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549 (e.g. ENCSR022WVP). 91.65 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 16 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> BHLHE40: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR000DZJ). 68.33 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 33 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> E2F4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878, HepG2 (e.g. ENCSR000DYY). 58.31 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 49 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> EGR1: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, Ishikawa (e.g. ENCSR000BSQ). 28.32 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 151 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: DOHH2, endodermal cell (e.g. ENCSR084RDK). 26.45 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 163 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GABPA: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, SK-N-SH (e.g. ENCSR000BJK). 15.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 303 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR647PSR). 10.74 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 436 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR784VIQ). 18.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 251 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF143: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR936XTK). 15.92 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 297 of 1626 TFs.

<a id="e15"></a>**E15** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs[masked] potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e15a"></a>**E15a** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> A major molecular feature of melanoma is abnormal telomerase activation; this is most often caused by telomerase reverse transcriptase (TERT) promoter mutations, which occur in 50-82% of cases and are the most common noncoding alteration in this cancer.

<a id="e15b"></a>**E15b** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> Understanding both telomere-dependent and -independent TERT functions is essential for developing effective biomarkers and therapies that overcome resistance and slow melanoma progression.

<a id="e15c"></a>**E15c** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e15d"></a>**E15d** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> Mutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e15e"></a>**E15e** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> The rs[masked] C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e15f"></a>**E15f** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e15g"></a>**E15g** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Taken together, these findings highlight the pro-tumorigenic role of USP10 in melanoma and suggest that disrupting the USP10/FOXM1 signaling axis could represent a viable therapeutic approach for treating this aggressive cancer.

<a id="e15h"></a>**E15h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e15i"></a>**E15i** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> The prognostic relevance of CDKN2A deletion may vary according to TERTp status, particularly for OS.

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:20:19+00:00)

> No ENCODE MAX ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no MAX experiment in that biosample. In other biosamples, 12 MAX peaks do contain the variant: A549, HCT116, HepG2, Ishikawa, K562, NB4, SK-N-SH (experiments ENCSR000BLP, ENCSR000BSH, ENCSR000BTJ, ENCSR000BTM, ENCSR000BTY, ENCSR000BVD).

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295135_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T20:17:52+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295135_G_A_b38 in tissues matching 'Brain - Cortex'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr5%3A1295135%20G%3EA%20TERT%20glioblastoma%20melanoma%20bladder%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:18:10+00:00)

> Europe PMC: 0 hits for 'chr5:1295135 G>A TERT glioblastoma melanoma bladder variant'; top 0 with PMIDs:
