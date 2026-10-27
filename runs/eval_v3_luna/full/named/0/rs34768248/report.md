# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 135 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: NKRF (bound elsewhere, z -12.31); CREB1 (bound elsewhere, z 6.24); MAX (bound elsewhere, z -2.15, no clear allelic change); ZBTB33 (bound elsewhere, z -1.92, no clear allelic change); NR2C2 (bound elsewhere, z 7.56, weak site); ZNF800 (bound elsewhere, z 6.43, weak site); RXRA (bound elsewhere, z 6.03, weak site); JUN (bound elsewhere, z 5.95, weak site); ZNF687 (bound elsewhere, z -5.31, weak site); CTCF (bound elsewhere, z -0.78, no clear allelic change, weak site). Occupancy unknown: EN1 (z 67.98); HOXA1 (z 67.98); HOXA2 (z 67.98); HOXA4 (z 67.98); HOXB2 (z 67.98). Diagnostic, not shown to the model: 296 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: No TF-mediated effect of rs34768248 (p = 0.75)

Null chain: no TF-mediated effect of this variant.

Predictions: In relevant tumor cells, the variant will not show a reproducible allele-specific TF occupancy effect that explains a regulatory change.; Any disease association, if present, will not be caused by TF-mediated effects of this base; the variant could be nonfunctional or linked to another causal change.

Falsified if: A relevant-cell experiment reproducibly shows allele-specific occupancy of a particular TF at the variant and a corresponding regulatory effect attributable to editing this base.

### 2. H2: NKRF preferentially binds the reference allele, with an unproven local regulatory effect (p = 0.15)

TF NKRF (QBiC-SELEX coverage own_model), ref allele binds more; element ENSR5_C5GP enhancer annotation; functional element assignment is uncertain; gene TERT; cell type Glioblastoma cells (candidate context; occupancy is unconfirmed).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NKRF is the leading binding candidate in this chain because its own QBiC-SELEX model predicts stronger binding to ref G at a strong site. A variant-overlapping NKRF ChIP peak exists in GM12878, but no matching glioblastoma peak is reported, so NKRF occupancy in glioblastoma is unconfirmed. | weak | [E14](#e14), [E20](#e20), [E35](#e35) |
| element | The variant is annotated within ENSR5_C5GP, but it overlaps no ENCODE cCRE; the nearest pELS is 75 bp away, so the functional element assignment is uncertain. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest listed gene and is named among the nearby cCRE genes, but no supplied evidence demonstrates that this variant or element regulates TERT; no significant GTEx eQTL is reported. | weak | [E02](#e02), [E03](#e03), [E17](#e17) |
| cell_type | Glioblastoma is a candidate context because NKRF is expressed in the DepMap glioblastoma subtype, but the supplied evidence does not establish NKRF occupancy or regulatory activity there. | weak | [E04](#e04), [E20](#e20), [E35](#e35) |
| phenotype | TERT has general relevance to melanoma and glioblastoma in the cited literature, but no evidence here connects rs34768248 to either disease; no bladder-cancer connection for this variant is established. | missing | [E15](#e15), [E18a](#e18a), [E18e](#e18e), [E18h](#e18h) |

Predictions: If NKRF occupies the site in relevant tumor cells, allele-specific occupancy should favor G over A; this differs from H3, which predicts an A-favoring CREB1 effect.; If the variant has a local regulatory consequence through this chain, perturbing the base should produce an NKRF-dependent regulatory change; the direction of TERT expression cannot be inferred from binding direction alone.

Falsified if: A sensitive relevant-cell assay detects no NKRF occupancy at the variant, or detects occupancy without the predicted G-over-A difference.; Editing the variant produces no reproducible NKRF-dependent local regulatory effect.

### 3. H3: CREB1 preferentially binds the alternate allele, with an unproven local regulatory effect (p = 0.10)

TF CREB1 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR5_C5GP enhancer annotation; functional element assignment is uncertain; gene TERT; cell type Glioblastoma cells (candidate context; occupancy is unconfirmed).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB1 is a secondary binding candidate: the QBiC-SELEX result predicts stronger binding to alt A, but uses a CREM-mapped model rather than a CREB1-specific model. A variant-overlapping CREB1 ChIP peak exists in H1, not in glioblastoma; relevant-cell occupancy is unconfirmed. | weak | [E09](#e09), [E21](#e21), [E36](#e36) |
| element | The variant is annotated within ENSR5_C5GP, but it overlaps no ENCODE cCRE; the nearest pELS is 75 bp away, so the functional element assignment is uncertain. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest listed gene and is named among the nearby cCRE genes, but no supplied evidence demonstrates that this variant or element regulates TERT; no significant GTEx eQTL is reported. | weak | [E02](#e02), [E03](#e03), [E17](#e17) |
| cell_type | Glioblastoma is a candidate context because CREB1 is expressed in the DepMap glioblastoma subtype, but the supplied evidence does not establish CREB1 occupancy or regulatory activity there. | weak | [E04](#e04), [E21](#e21), [E36](#e36) |
| phenotype | TERT has general relevance to melanoma and glioblastoma in the cited literature, but no evidence here connects rs34768248 to either disease; no bladder-cancer connection for this variant is established. | missing | [E15](#e15), [E18a](#e18a), [E18e](#e18e), [E18h](#e18h) |

Predictions: If CREB1 occupies the site in relevant tumor cells, allele-specific occupancy should favor A over G; this differs from H2, which predicts G-favoring NKRF occupancy.; If the variant has a local regulatory consequence through this chain, perturbing the base should produce a CREB1-dependent regulatory change; the direction of TERT expression cannot be inferred from binding direction alone.

Falsified if: A sensitive relevant-cell assay detects no CREB1 occupancy at the variant, or detects occupancy without the predicted A-over-G difference.; Editing the variant produces no reproducible CREB1-dependent local regulatory effect.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- |
| Targeted allele-specific NKRF CUT&RUN at the variant in a glioblastoma model, using a naturally heterozygous line if available | medium | yes | No reproducible variant-centered NKRF occupancy with G-over-A allelic enrichment. | NKRF occupies the variant and shows greater occupancy on G than A. | No G-over-A NKRF occupancy pattern is required; CREB1, not NKRF, is the proposed allele-sensitive factor. |
| Targeted allele-specific CREB1 CUT&RUN at the variant in a glioblastoma model, using a naturally heterozygous line if available | medium | no | No reproducible variant-centered CREB1 occupancy with A-over-G allelic enrichment. | No A-over-G CREB1 occupancy pattern is required; NKRF, not CREB1, is the proposed allele-sensitive factor. | CREB1 occupies the variant and shows greater occupancy on A than G. |
| Edit G to A and A to G in an isogenic glioblastoma model; measure local regulatory activity and TERT expression with and without NKRF perturbation | high | no | Editing produces no reproducible NKRF-dependent regulatory or TERT-expression difference attributable to this base. | Editing produces a reproducible regulatory difference that depends on NKRF; its direction for TERT expression is not specified in advance. | Any reproducible effect is not specifically dependent on NKRF; a CREB1-dependent effect would instead favor H3. |

## Next experiment

The cheapest listed experiment that separates the top two hypotheses (H1 null and H2 NKRF) is targeted allele-specific NKRF CUT&RUN at the variant in a glioblastoma model, preferably a naturally heterozygous line. H2 predicts greater NKRF occupancy on G than A; H1 predicts no reproducible allele-specific occupancy effect.

## Investigate calls

- chip_peaks({"tf": "NKRF", "biosample": "Glioblastoma"})
- chip_peaks({"tf": "CREB1", "biosample": "Glioblastoma"})
- gene_disease({"gene": "TERT"})

## Flags

- literature_fallback: no hits for 'rs34768248 AND TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; dropped the rsID
- tool_failed: E37 gene_disease: Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'

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

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295601:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap subtype median Glioblastoma), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 10 occupied (4 with a strong site), 5 of 109 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 563 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NKRF (Unknown, 1 model; QBiC-SELEX coverage: own model): best model NKRF_DBD_CA40NCTTTGA_YWPA_jolma2025_0_3_7mer (its own model), z -12.31, effect -0.514: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.69 TPM, rank 522 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR732PJX. Best model's site strength: ref 99.0th, alt 80.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CREB1 (bZIP, 2 models; QBiC-SELEX coverage: own model): best model CREM_eDBD_TGAAGA40NATG_KO_yin2017_0_4_7mer (a CIS-BP-mapped model of CREM), z 6.24, effect 0.244: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 30.94 TPM, rank 132 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in H1, e.g. ENCSR000BSN. Best model's site strength: ref 92.9th, alt 98.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z -2.15, effect -0.147: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 58.6 TPM, rank 48 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in H1, e.g. ENCSR000BSJ. Best model's site strength: ref 99.7th, alt 94.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB33 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB33_eDBD_TAGCTG40NCTA_KR_yin2017_0_4_7mer (its own model), z -1.92, effect -0.069: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 12.18 TPM, rank 381 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in K562, e.g. ENCSR876GXA. Best model's site strength: ref 98.3th, alt 61.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model Rev-ErbA-Alpha_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of NR1D1), z 7.56, effect 0.305: alt allele binds more (|z| above the gate), but between weak k-mers. 20.46 TPM, rank 223 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR559ZKI. Best model's site strength: ref 88.5th, alt 85.0th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF800 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF800_FL_GT40NTTGGTG_YWSA_jolma2025_0_3_7mer (its own model), z 6.43, effect 0.24: alt allele binds more (|z| above the gate), but between weak k-mers. 11.64 TPM, rank 400 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR701WPG. Best model's site strength: ref 89.6th, alt 91.4th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> RXRA (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model THRB_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of THRB), z 6.03, effect 0.271: alt allele binds more (|z| above the gate), but between weak k-mers. 13.1 TPM, rank 354 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR416HDG. Best model's site strength: ref 80.3th, alt 84.4th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUN (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUN_FL_TCAGTG40NGAT_KAE_yin2017_0_3_7mer (its own model), z 5.95, effect 0.111: alt allele binds more (|z| above the gate), but between weak k-mers. 91.65 TPM, rank 16 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, e.g. ENCSR604CKQ. Best model's site strength: ref 79.1th, alt 85.4th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF687 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF687_FL_TA40NGTTAGC_YWL_jolma2025_0_3_7mer (its own model), z -5.31, effect -0.304: ref allele binds more (|z| above the gate), but between weak k-mers. 10.74 TPM, rank 436 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR647PSR. Best model's site strength: ref 96.9th, alt 85.7th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z -0.78, effect -0.094: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 26.45 TPM, rank 163 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in H9, neural progenitor cell, e.g. ENCSR125NBL. Best model's site strength: ref 87.7th, alt 93.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EN1 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.13 TPM, rank 810 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXA1 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.76 TPM, rank 1026 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXA2 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.08 TPM, rank 1100 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXA4 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.44 TPM, rank 875 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXB2 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 10.25 TPM, rank 454 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:44:40+00:00)

> No ENCODE NKRF ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no NKRF experiment in that biosample. In other biosamples, 1 NKRF peaks do contain the variant: GM12878 (experiments ENCSR732PJX).

<a id="e36"></a>**E36** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:44:41+00:00)

> No ENCODE CREB1 ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no CREB1 experiment in that biosample. In other biosamples, 1 CREB1 peaks do contain the variant: H1 (experiments ENCSR000BSN).

<a id="e37"></a>**E37** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'
