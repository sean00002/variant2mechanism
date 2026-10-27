# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 128 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen

296 of 997 models pass the gate. Top groups: bHLH, 3 models (best TCF3, z 87.39); Homeodomain, 81 models (best HOXD4, z 67.98); bHLH, 1 model (best TFAP4, z 38.6); C2H2 ZF, 1 model (best ZBTB18, z 37.09); C2H2 ZF, 4 models (best ZIC1, z 25.12).

## Ranked chains

### 1. H4_null: No TF-mediated effect of rs34768248; linked or nonfunctional variant (p = 0.62)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs34768248 in relevant cells; No genotype-TERT expression association after controlling for linked variants; The QBiC-SELEX binding change is not functional in the relevant chromatin context

Falsified if: allele-specific TF occupancy at this base is reproducibly shown and perturbs TERT expression; a reporter assay shows the G/A change directly alters enhancer activity; fine-mapping excludes linked variants and supports a direct allelic effect

### 2. H1_TCF3: TCF3 binds the alt allele more strongly at a TERT enhancer (p = 0.25)

TF TCF3 (stated coverage own_model; registry own_model), alt allele binds more; element the variant lies in an annotated enhancer near TERT; gene TERT; cell type glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G051's best model is TCF3 (own_model, z 87.39, effect +3.341), supporting stronger binding of alt A than ref G in vitro; TCF3 is chosen within the shared bHLH specificity because it is the best model and has the highest group expression (57.23 TPM). No ENCODE TCF3 ChIP-seq peak contains the variant, so in vivo occupancy is unproven. | weak | [E08](#e08), [E07](#e07), [E19](#e19) |
| element | rs34768248 lies in ENSR5_C5GP enhancer and near a cCRE cluster by TERT; no cCRE directly overlaps the variant, but the nearest pELS is 75 bp away. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.5 kb from its TSS; however, the only L2G signal is from a hypertension credible set with PIP 0.00, GWAS Catalog has 0 associations for rs34768248, GTEx brain shows 0 significant eQTLs, and the targeted rs34768248-TERT literature does not establish TERT association. The variant-to-TERT expression link is therefore not established. | missing | [E02](#e02), [E05](#e05), [E04](#e04), [E18](#e18), [E20](#e20) |
| cell_type | The DepMap glioblastoma subtype context expresses TCF3 at 57.23 TPM, but the broad TERT-cancer literature does not establish a TCF3-TERT axis in glioblastoma, melanoma, or bladder cancer. | missing | [E08](#e08), [E07](#e07), [E06](#e06) |
| phenotype | No evidence shows that TCF3 binding at rs34768248 changes TERT expression, telomerase activity, or disease risk; if TCF3 activates, alt-A binding might increase TERT, while if TCF3 represses, the direction would be opposite. | missing | none |

Predictions: Allele-specific reporter/MPRA shows a G/A difference in glioblastoma cells; Allele-specific TCF3 ChIP/CUT&RUN shows stronger TCF3 occupancy at A than G; TCF3 perturbation changes TERT expression in the relevant cell context

Falsified if: allele-specific reporter or MPRA shows no G/A difference in glioblastoma cells; allele-specific TCF3 ChIP/CUT&RUN shows no preferential TCF3 occupancy at A; TCF3 perturbation does not alter TERT expression in the relevant cell context

### 3. H2_TCF12: TCF12 binds the alt allele more strongly at a TERT enhancer (p = 0.08)

TF TCF12 (stated coverage own_model; registry own_model), alt allele binds more; element the variant lies in an annotated enhancer near TERT; gene TERT; cell type glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G051 covers TCF12 as own_model (z 71.51) with the same sign as the best model, so alt A is predicted to bind TCF12 more strongly than ref G in vitro; however, the shared bHLH motif cannot distinguish TCF12 from TCF3, and no allele-specific TCF12 occupancy data are provided. | weak | [E08](#e08), [E07](#e07) |
| element | rs34768248 lies in ENSR5_C5GP enhancer and near a cCRE cluster by TERT; no cCRE directly overlaps the variant, but the nearest pELS is 75 bp away. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.5 kb from its TSS; however, the only L2G signal is from a hypertension credible set with PIP 0.00, GWAS Catalog has 0 associations for rs34768248, GTEx brain shows 0 significant eQTLs, and the targeted rs34768248-TERT literature does not establish TERT association. The variant-to-TERT expression link is therefore not established. | missing | [E02](#e02), [E05](#e05), [E04](#e04), [E18](#e18), [E20](#e20) |
| cell_type | The DepMap glioblastoma subtype context expresses TCF12 at 54.67 TPM, but the broad TERT-cancer literature does not establish a TCF12-TERT axis in glioblastoma, melanoma, or bladder cancer. | missing | [E08](#e08), [E07](#e07), [E06](#e06) |
| phenotype | No evidence shows that TCF12 binding at rs34768248 changes TERT expression, telomerase activity, or disease risk; the phenotype link remains speculative and direction depends on activator versus repressor function. | missing | none |

Predictions: Allele-specific TCF12 ChIP/CUT&RUN shows stronger TCF12 occupancy at A than G; TCF12 knockdown reduces TERT expression more than TCF3 knockdown in the same cells; The relevant glioblastoma cells favor TCF12 over TCF3 at this element

Falsified if: allele-specific assays show no TCF12 binding difference; TCF12 perturbation does not change TERT expression; TCF3, not TCF12, is the dominant factor at this element by allele-specific ChIP

### 4. H3_TCF4: TCF4 binds the alt allele more strongly at a TERT enhancer (p = 0.05)

TF TCF4 (stated coverage own_model; registry own_model), alt allele binds more; element the variant lies in an annotated enhancer near TERT; gene TERT; cell type glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G051 covers TCF4 as own_model (z 20.2) with the same sign as the best model, so alt A is predicted to bind TCF4 more strongly than ref G in vitro; however, TCF4 is the lowest-ranked shown member and the shared bHLH motif cannot distinguish it from TCF3/TCF12. | weak | [E08](#e08), [E07](#e07) |
| element | rs34768248 lies in ENSR5_C5GP enhancer and near a cCRE cluster by TERT; no cCRE directly overlaps the variant, but the nearest pELS is 75 bp away. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.5 kb from its TSS; however, the only L2G signal is from a hypertension credible set with PIP 0.00, GWAS Catalog has 0 associations for rs34768248, GTEx brain shows 0 significant eQTLs, and the targeted rs34768248-TERT literature does not establish TERT association. The variant-to-TERT expression link is therefore not established. | missing | [E02](#e02), [E05](#e05), [E04](#e04), [E18](#e18), [E20](#e20) |
| cell_type | The DepMap glioblastoma subtype context expresses TCF4 at 27.41 TPM, but the broad TERT-cancer literature does not establish a TCF4-TERT axis in glioblastoma, melanoma, or bladder cancer. | missing | [E08](#e08), [E07](#e07), [E06](#e06) |
| phenotype | No evidence shows that TCF4 binding at rs34768248 changes TERT expression, telomerase activity, or disease risk; the phenotype link remains speculative and direction depends on activator versus repressor function. | missing | none |

Predictions: Allele-specific TCF4 ChIP/CUT&RUN shows stronger TCF4 occupancy at A than G; TCF4 knockdown reduces TERT expression or telomerase activity; TCF4 motifs are enriched at the accessible TERT upstream region in the relevant cells

Falsified if: allele-specific assays show no TCF4 binding difference; TCF4 perturbation does not affect TERT expression; TCF3 or TCF12, not TCF4, occupies this element in relevant cells

## Prediction matrix

| Test | Cost | Separates top two | H4_null | H1_TCF3 | H2_TCF12 | H3_TCF4 |
| --- | --- | --- | --- | --- | --- | --- |
| DepMap glioblastoma: regress TERT expression on rs34768248 genotype in existing lines | low | yes |  |  |  |  |
| Allele-specific reporter or MPRA for G vs A in glioblastoma cells | medium | yes |  |  |  |  |
| Allele-specific TCF3 ChIP/CUT&RUN in glioblastoma cells | high | yes |  |  |  |  |
| TCF3 knockdown/CRISPRi followed by TERT qPCR in glioblastoma cells | medium | no |  |  |  |  |

## Next experiment

Query existing DepMap glioblastoma lines to test whether rs34768248 genotype is associated with TERT expression; this is the cheapest test that separates the top two chains (H1_TCF3 vs H4_null).

## Investigate calls

- eqtl_lookup({"tissue": "Brain"})
- chip_peaks({"tf": "TCF3", "biosample": null})
- literature_search({"query": "rs34768248 TERT"})

## Flags

- literature_fallback: no hits for 'rs34768248 AND TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; dropped the rsID
- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 0.80 of links cite only evidence that passed every check.

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs34768248&size=100; retrieved 2026-10-26T02:22:30+00:00)

> 0 GWAS Catalog associations for rs34768248, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:22:30+00:00)

> 1 credible sets contain 5_1295601_G_A: 1 GWAS, 0 molecular QTL.
> GWAS Hypertension: PIP 0.00; L2G TERT 0.84
> Best L2G gene scores across these sets: TERT 0.84

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295601:G>A: 997 models scored, 296 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 229 CIS-BP groups. Expression context: DepMap subtype median Glioblastoma. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 53 (bHLH, 2 models z 147.37, bHLH, 2 models z 62.92, bHLH, 1 model z 45.4, bHLH, 1 model z 38.43, bHLH, 1 model z 37.19). Passing groups ranked below the ones shown: 166. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G051 (bHLH, 3 models): best model TCF3_NA_TACCCG20NCCC_ESY_yang2017_0_2_7mer (own model of TCF3), z 87.39, effect 3.341 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: TCF3 z 87.39, TCF12 z 71.51, TCF4 z 20.2. TFs this group covers: TCF3 (own model) 57.23 TPM, TCF12 (own model) 54.67 TPM, TCF4 (own model) 27.41 TPM; best model's site strength: ref 96.3th, alt 99.9th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G001 (Homeodomain, 81 models): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (own model of HOXD4), z 67.98, effect 2.073 (alt binds more); 14 passing models (12 with the best model's sign); members disagree on direction. Passing members: HOXD4 z 67.98, LHX1 z 9.84, MSX2 z 9.43, HMX2 z 8.34, BARHL1 z 7.26 (+9 more). TFs this group covers: PRRX1 (own model) 33.14 TPM, HOXB3 (own model) 14.88 TPM, HOXB7 (own model) 14.34 TPM, PITX1 (own model) 13.59 TPM, DLX1 (own model) 12.0 TPM, HOXB2 (own model) 10.25 TPM, SHOX2 (own model) 9.84 TPM, HOXC6 (mapped) 5.85 TPM, HOXB6 (mapped) 5.72 TPM, MSX1 (own model) 5.29 TPM (+103 more); best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G354 (bHLH, 1 model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (own model of TFAP4), z 38.6, effect 2.785 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: TFAP4 z 38.6. TFs this group covers: TFAP4 (own model) 5.49 TPM; best model's site strength: ref 95.8th, alt 99.4th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G393 (C2H2 ZF, 1 model): best model ZBTB18_eDBD_TACTCC40NGTA_KR_yin2017_0_3_7mer (own model of ZBTB18), z 37.09, effect 2.696 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZBTB18 z 37.09. TFs this group covers: ZBTB18 (own model) 10.9 TPM; best model's site strength: ref 90.4th, alt 99.8th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G032 (C2H2 ZF, 4 models): best model ZIC1_FL_TTTATT40NATC_KW_yin2017_0_3_7mer (own model of ZIC1), z 25.12, effect 1.864 (alt binds more); 3 passing models (3 with the best model's sign). Passing members: ZIC1 z 25.12, ZIC4 z 16.62, ZIC3 z 9.02. TFs this group covers: ZIC1 (own model) 13.23 TPM, ZIC2 (mapped) 3.7 TPM, ZIC4 (own model) 1.37 TPM, ZIC5 (own model) 0.53 TPM, ZIC3 (own model) 0.0 TPM; best model's site strength: ref 83.3th, alt 99.4th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G320 (C2H2 ZF, 1 model): best model RLF_DBD2_AG40NGGAATC_YWPA_jolma2025_0_3_7mer (own model of RLF), z -24.34, effect -1.279 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: RLF z -24.34. TFs this group covers: RLF (own model) 8.96 TPM; best model's site strength: ref 97.9th, alt 80.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G211 (Unknown, 1 model): best model ID4_NA_CTACA14N_U_jolma2013_1_3_7mer (own model of ID4), z 17.3, effect 0.819 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ID4 z 17.3. TFs this group covers: ID4 (own model) 1.46 TPM; best model's site strength: ref 99.1th, alt 100.0th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G401 (C2H2 ZF, 1 model): best model ZBTB37_eDBD_TATGTC40NGGA_KR_yin2017_0_4_7mer (own model of ZBTB37), z -16.47, effect -1.806 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB37 z -16.47. TFs this group covers: ZBTB37 (own model) 1.72 TPM; best model's site strength: ref 91.8th, alt 51.8th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G432 (Homeodomain, 1 model): best model ZHX3_DBD2_CT40NTCTAGT_YWQA_jolma2025_0_2_7mer (own model of ZHX3), z -15.37, effect -0.381 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZHX3 z -15.37. TFs this group covers: ZHX3 (own model) 12.73 TPM; best model's site strength: ref 99.1th, alt 73.2th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G086 (bHLH, 2 models): best model MSC_eDBD_TACTTA40NCTA_KR_yin2017_0_4_7mer (own model of MSC), z 15.31, effect 0.661 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: MSC z 15.31, TCF21 z 7.13. TFs this group covers: MSC (own model) 5.11 TPM, TCF21 (own model) 0.05 TPM; best model's site strength: ref 97.5th, alt 99.6th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295601_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:24:03+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295601_G_A_b38 in tissues matching 'Brain'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:29:02+00:00)

> No ENCODE TCF3 ChIP-seq peak contains chr5:1295601:G>A. Absence can also mean no TCF3 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs34768248%20TERT&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:29:03+00:00)

> Europe PMC: 1 hits for 'rs34768248 TERT'; top 1 with PMIDs:
> PMID 27814745 (2016): Deep targeted sequencing of 12 breast cancer susceptibility regions in 4611 women across four different ethnicities.
