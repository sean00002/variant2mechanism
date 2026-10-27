# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 259 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.60)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not produce a reproducible TF-dependent change in TERT expression; any association may reflect another cause or a linked alteration.

Falsified if: In an appropriate tumor-cell context, the variant reproducibly changes TERT expression and that change depends on allele-specific binding by a TF.

### 2. H1: Candidate GABPA-mediated increase in TERT promoter activity (p = 0.30)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: the alt allele binds GABPA more strongly. GABPA is the leading candidate because the literature mentions GABPA-augmented identification of a TERT promoter mutation and ETS motif gains, and GABPA peaks overlap this site in other biosamples. This does not establish the allele direction or occupancy in glioblastoma: no allele-specific binding result or QBiC-SELEX result/model is supplied, and no matching U-87 MG peak is reported. | weak | [E04](#e04), [E11](#e11), [E16b](#e16b), [E17](#e17) |
| element | The variant lies in a promoter-like cCRE, but its reported chromatin signals are maxima across biosamples rather than glioblastoma-specific measurements. | supported | [E03](#e03) |
| gene | TERT is the nearest annotated gene and the variant is upstream of its transcript; this makes TERT a candidate target but does not show regulation by this variant. | weak | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is a proposed context based on the supplied expression context, but matching GABPA occupancy and cCRE activity are not established. | weak | [E03](#e03), [E04](#e04), [E17](#e17) |
| phenotype | If this mechanism increases TERT activity, it could be relevant to tumor biology. The cited literature supports broader relevance of TERT promoter mutations in glioblastoma and melanoma, not this GABPA mechanism or a mechanism in bladder disease. | weak | [E15a](#e15a), [E15e](#e15e), [E15h](#e15h) |

Predictions: In an appropriate glioblastoma context, the alt allele will show greater GABPA binding and higher TERT promoter activity than ref; reducing GABPA will diminish the allele-dependent activity difference.; The predicted effect will depend on GABPA rather than MAX or JUN.

Falsified if: Allele-specific assays show no greater GABPA binding to alt, or the allele-dependent TERT expression effect persists when GABPA is reduced.

### 3. H2: Alternative MAX-mediated TERT promoter regulation (p = 0.06)

TF MAX (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Low-confidence hypothesis: the alt allele binds MAX more strongly. MAX is expressed and has peaks overlapping the site in other biosamples, but no allele-specific binding or QBiC-SELEX result is supplied, and no matching U-87 MG peak is reported. These data do not establish the proposed direction. | weak | [E04](#e04), [E05](#e05), [E18](#e18) |
| element | The variant lies in a promoter-like cCRE with chromatin signals reported across biosamples; activity in glioblastoma is not established. | supported | [E03](#e03) |
| gene | TERT is the nearest annotated gene and the variant is upstream of its transcript, but direct regulation is not shown. | weak | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is a proposed context, but matching MAX occupancy and cCRE activity are not established. | weak | [E03](#e03), [E04](#e04), [E18](#e18) |
| phenotype | A MAX-dependent change in TERT could be relevant to tumor biology, but the cited literature does not establish this variant-specific mechanism or a mechanism in bladder disease. | weak | [E15a](#e15a), [E15e](#e15e) |

Predictions: The alt allele will show greater MAX binding and a MAX-dependent change in TERT expression; reducing MAX will diminish the allele-dependent effect.; The effect will depend on MAX rather than GABPA or JUN.

Falsified if: Allele-specific assays show no greater MAX binding to alt, or the allele-dependent TERT expression effect persists when MAX is reduced.

### 4. H3: Alternative JUN-mediated TERT promoter regulation (p = 0.04)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type glioblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Low-confidence hypothesis: the alt allele binds JUN more strongly. JUN peaks overlap the site in another biosample, and the cited literature notes that AP-1 binding changes explain some allele-specific chromatin-accessibility variants generally. Neither establishes JUN binding or an allelic effect at this variant; no QBiC-SELEX result is supplied. | weak | [E04](#e04), [E06](#e06), [E16a](#e16a) |
| element | The variant lies in a promoter-like cCRE with chromatin signals reported across biosamples; glioblastoma-specific activity is not established. | supported | [E03](#e03) |
| gene | TERT is the nearest annotated gene and the variant is upstream of its transcript, but direct regulation is not shown. | weak | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is a proposed context, but matching JUN occupancy and cCRE activity are not established. | weak | [E03](#e03), [E04](#e04), [E06](#e06) |
| phenotype | A JUN-dependent change in TERT could be relevant to tumor biology, but the cited evidence does not establish this variant-specific mechanism or a mechanism in bladder disease. | weak | [E15a](#e15a), [E15e](#e15e) |

Predictions: The alt allele will show greater JUN binding and a JUN-dependent change in TERT expression; reducing JUN will diminish the allele-dependent effect.; The effect will depend on JUN rather than GABPA or MAX.

Falsified if: Allele-specific assays show no greater JUN binding to alt, or the allele-dependent TERT expression effect persists when JUN is reduced.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Compare ref and alt TERT-promoter reporters in a glioblastoma cell line with control versus GABPA depletion; measure reporter activity. | medium | yes | No reproducible allele-dependent activity difference, or any difference is not specifically reduced by GABPA depletion. | Alt reporter activity exceeds ref with control treatment, and the difference is reduced by GABPA depletion. | No specific GABPA-dependent difference; a reporter effect, if present, should instead depend on MAX. | No specific GABPA-dependent difference; a reporter effect, if present, should instead depend on JUN. |
| Measure allele-specific GABPA occupancy at the variant in a suitable heterozygous glioblastoma model, with allele-aware CUT&RUN or ChIP-seq. | high | no | No reproducible alt-enriched GABPA occupancy. | Greater GABPA occupancy on alt than ref. | No specific prediction of alt-enriched GABPA occupancy. | No specific prediction of alt-enriched GABPA occupancy. |
| Use isogenic base editing to exchange ref and alt in glioblastoma cells; measure TERT expression with and without the predicted TF perturbation. | high | no | Editing produces no reproducible TF-dependent TERT expression change. | Alt increases TERT expression relative to ref, and the increase is reduced by GABPA perturbation. | Any editing-associated TERT change is reduced by MAX perturbation rather than GABPA perturbation. | Any editing-associated TERT change is reduced by JUN perturbation rather than GABPA perturbation. |

## Next experiment

Compare ref and alt TERT-promoter reporters in a glioblastoma cell line with and without GABPA depletion. This is the cheapest proposed test that directly distinguishes the leading GABPA-mediated chain from the null by asking whether an alt-associated activity increase depends on GABPA.

## Investigate calls

- literature_search({"query": "TERT C250T allele-specific TF binding reporter assay GABPA MAX JUN glioblastoma"})
- chip_peaks({"tf": "GABPA", "biosample": "U-87 MG"})
- chip_peaks({"tf": "MAX", "biosample": "U-87 MG"})

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
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e15a"></a>**E15a** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> A major molecular feature of melanoma is abnormal telomerase activation; this is most often caused by telomerase reverse transcriptase (TERT) promoter mutations, which occur in 50-82% of cases and are the most common noncoding alteration in this cancer.

<a id="e15b"></a>**E15b** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> Conclusions: Understanding both telomere-dependent and -independent TERT functions is essential for developing effective biomarkers and therapies that overcome resistance and slow melanoma progression.

<a id="e15c"></a>**E15c** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> The genetic landscape of familial melanoma is heterogeneous.

<a id="e15d"></a>**E15d** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e15e"></a>**E15e** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> BackgroundMutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e15f"></a>**E15f** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> ConclusionThe rs2853669 C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e15g"></a>**E15g** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e15h"></a>**E15h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e15i"></a>**E15i** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> The prognostic relevance of CDKN2A deletion may vary according to TERTp status, particularly for OS.

<a id="e16"></a>**E16** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20C250T%20allele-specific%20TF%20binding%20reporter%20assay%20GABPA%20MAX%20JUN%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:20:15+00:00)

> Europe PMC: 4 hits for 'TERT C250T allele-specific TF binding reporter assay GABPA MAX JUN glioblastoma'; top 1 with PMIDs:
> PMID 33832990 (2021): Interpretation of allele-specific chromatin accessibility using cell state-aware deep learning.

<a id="e16a"></a>**E16a** literature_search, Europe PMC abstract, PMID 33832990 (https://europepmc.org/article/MED/33832990; retrieved 2026-10-26T13:20:15+00:00)

> A considerable fraction of ASCAVs are caused by changes in AP-1 binding, as confirmed by matched ChIP-seq data to identify allele-specific binding of JUN and FOSL1.

<a id="e16b"></a>**E16b** literature_search, Europe PMC abstract, PMID 33832990 (https://europepmc.org/article/MED/33832990; retrieved 2026-10-26T13:20:15+00:00)

> Finally, by augmenting the DeepMEL2 model with ChIP-seq data for GABPA, the TERT promoter mutation, as well as additional ETS motif gains, can be identified with high confidence.

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'U-87 MG'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:20:19+00:00)

> No ENCODE MAX ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'U-87 MG'. Absence can also mean no MAX experiment in that biosample. In other biosamples, 12 MAX peaks do contain the variant: A549, HCT116, HepG2, Ishikawa, K562, NB4, SK-N-SH (experiments ENCSR000BLP, ENCSR000BSH, ENCSR000BTJ, ENCSR000BTM, ENCSR000BTY, ENCSR000BVD).
