# rs4784227 and Breast cancer (16q12)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 9 model calls; 247 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H4_null_linked_or_passenger: No TF-mediated allelic effect of rs4784227; the association reflects a linked causal variant or a passenger regulatory change (p = 0.48)

Null chain: no TF-mediated effect of this variant.

Predictions: rs4784227 does not itself alter allele-specific TF binding or enhancer activity in the relevant breast-cancer cell type.; The breast-cancer association is explained by linkage disequilibrium with another causal variant at 16q12.; FOXA1 occupancy at the element (E07) is not allele-specific and does not mediate a TOX3 expression change; absence of a breast-mammary eQTL (E09) and absence of an MCF7 ESR1 peak (E08) are consistent with no direct allelic mechanism.

Falsified if: A robust allele-specific TF-binding difference at rs4784227 is demonstrated in breast-cancer cells.; The variant itself reproducibly changes enhancer activity and TOX3 expression in a relevant context.; The allelic effect tracks the breast-cancer risk allele after controlling for linked variants.

### 2. H1_FOXA1_enhancer_activation: Alt T may increase FOXA1 binding at a distal enhancer, altering TOX3 expression and breast-cancer risk (p = 0.34)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element Distal enhancer EH38E3180851 (dELS) containing rs4784227; gene TOX3; cell type ER-positive/luminal breast cancer, including MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies the rs4784227-containing element in MCF7 (E07); the allele-specific direction, alt T binding more strongly than ref C, remains a prediction rather than a demonstrated effect. | weak | [E07](#e07) |
| element | rs4784227 lies within a distal enhancer-like cCRE (EH38E3180851) with H3K27ac signal, consistent with an enhancer context; E03 z-scores are maxima across ENCODE biosamples and do not establish MCF7-specific or allele-specific activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is the closest protein-coding gene and the leading L2G target, but E09 finds no significant GTEx breast-mammary eQTL for this variant, so an effect on TOX3 expression is not demonstrated. | weak | [E02](#e02), [E05](#e05), [E09](#e09) |
| cell_type | MCF7 is a relevant context because a FOXA1 ChIP-seq peak contains the variant in MCF7 (E07) and the breast-cancer GWAS/L2G evidence supports ER-positive/luminal relevance (E05), although E06 is title-level only. | weak | [E05](#e05), [E06](#e06), [E07](#e07) |
| phenotype | The T allele is associated with increased breast-cancer risk in the strongest breast-cancer GWAS entries. | supported | [E04](#e04), [E05](#e05) |

Predictions: Allele-specific FOXA1 ChIP-qPCR in MCF7 or another heterozygous ER-positive breast-cancer line shows higher FOXA1 signal on the alt T allele.; An enhancer reporter with the T allele has higher activity than the C allele in MCF7, and this difference is reduced by FOXA1 depletion.; FOXA1 knockdown reduces the allele-specific enhancer or expression effect at this locus.

Falsified if: No allele-specific FOXA1 binding is detected at rs4784227 in breast-cancer cells.; The T allele does not increase enhancer activity or TOX3 expression in a relevant context.; The allelic effect persists unchanged after FOXA1 knockdown.

### 3. H2_ESR1_enhancer_activation: Alt T may increase ESR1/ER-alpha binding at the enhancer, altering TOX3 expression in ER-positive breast cancer (p = 0.10)

TF ESR1 (stated coverage not_checked; registry own_model), alt allele binds more; element Distal enhancer EH38E3180851 (dELS) containing rs4784227; gene TOX3; cell type ER-positive/luminal breast cancer, including MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alt T binding ESR1 more strongly than ref C is proposed but unsupported; no allele-specific ESR1 data are available, and no ESR1 ChIP-seq peak contains the variant in MCF7 (E08). | missing | none |
| element | rs4784227 lies in a distal enhancer-like cCRE (EH38E3180851), so an allele-specific ESR1 effect could alter enhancer activity if ESR1 bound there; this is not shown. | weak | [E01](#e01), [E03](#e03) |
| gene | TOX3 is the closest and leading L2G gene, but E09 finds no significant GTEx breast-mammary eQTL for this variant, so an ESR1-dependent change in TOX3 expression is unproven. | weak | [E02](#e02), [E05](#e05), [E09](#e09) |
| cell_type | ER-positive breast cancer is relevant from GWAS subtype evidence (E05), but E08 does not support ESR1 occupancy at this element in MCF7, and E06 is title-level only. | weak | [E05](#e05), [E06](#e06), [E08](#e08) |
| phenotype | The T allele is associated with increased breast-cancer risk in the strongest breast-cancer GWAS entries. | supported | [E04](#e04), [E05](#e05) |

Predictions: Allele-specific ESR1 ChIP-qPCR in MCF7 or another ER-positive line shows higher ESR1 signal on the alt T allele.; The enhancer or expression effect is stronger in ER-positive breast-cancer cells and is reduced by ER antagonist treatment.; ESR1 depletion reduces any allele-specific enhancer effect.

Falsified if: No allele-specific ESR1 binding is detected at rs4784227.; The allelic effect is unchanged after ESR1 depletion or ER blockade.; TOX3 expression is not altered by ESR1 manipulation in this context.

### 4. H3_CTCF_insulator_loss: Ref C may strengthen CTCF binding at the enhancer, while alt T weakens CTCF and may alter TOX3 enhancer contact (p = 0.08)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element Distal enhancer EH38E3180851 (dELS) containing rs4784227, with a reported CTCF z-score in the cCRE registry; gene TOX3; cell type Breast cancer, including MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Ref C binding CTCF more strongly than alt T is proposed but unsupported; E03 reports only a maximum CTCF z-score of 1.9 in the cCRE and provides no allele-specific CTCF binding data. | missing | none |
| element | rs4784227 lies in a distal enhancer-like cCRE with some CTCF signal (E03), but insulator function and allele-specific CTCF occupancy are not shown. | weak | [E01](#e01), [E03](#e03) |
| gene | TOX3 is the nearest and leading L2G gene, but there is no evidence that CTCF loss on the T allele increases enhancer contact with TOX3, and E09 finds no breast-mammary eQTL. | weak | [E02](#e02), [E05](#e05), [E09](#e09) |
| cell_type | Breast-cancer relevance is supported by GWAS/L2G evidence (E05), but MCF7-specific CTCF activity at this element is not shown; E06 is title-level only. | weak | [E05](#e05), [E06](#e06) |
| phenotype | The T allele is associated with increased breast-cancer risk in the strongest breast-cancer GWAS entries. | supported | [E04](#e04), [E05](#e05) |

Predictions: Allele-specific CTCF ChIP-qPCR shows higher CTCF signal on the ref C allele than on alt T.; Alt T increases enhancer-promoter contact or TOX3 expression in a chromatin-contact assay.; CTCF depletion mimics the alt T allele's effect on TOX3 or chromatin contact.

Falsified if: No allele-specific CTCF binding is detected at the variant.; Alt T does not increase enhancer contact or TOX3 expression.; CTCF depletion does not alter TOX3 expression or chromatin contact from this enhancer.

## Prediction matrix

| Test | Cost | Separates top two | H4_null_linked_or_passenger | H1_FOXA1_enhancer_activation | H2_ESR1_enhancer_activation | H3_CTCF_insulator_loss |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific FOXA1 ChIP-qPCR at rs4784227 in MCF7 (or another heterozygous ER-positive breast-cancer line) | low | yes | No allele-specific FOXA1 difference at rs4784227. | Higher FOXA1 signal on the alt T allele than on ref C. | No allele-specific FOXA1 difference; ESR1 is the proposed factor. | No allele-specific FOXA1 difference; CTCF is the proposed factor. |
| Allele-specific ESR1 ChIP-qPCR at rs4784227 in MCF7 | low | no | No allele-specific ESR1 difference at rs4784227. | No allele-specific ESR1 difference; FOXA1 is the proposed factor. | Higher ESR1 signal on the alt T allele than on ref C. | No allele-specific ESR1 difference; CTCF is the proposed factor. |
| Enhancer reporter assay comparing C and T alleles at rs4784227 in MCF7, with and without FOXA1 knockdown | high | yes | No reproducible allelic reporter difference; any difference is not attributable to rs4784227. | T allele has higher reporter activity than C, and the difference is reduced by FOXA1 knockdown. | T allele may have higher reporter activity, but it is reduced by ER blockade rather than FOXA1 knockdown. | Reporter activity alone is not expected to model CTCF insulation; no CTCF-dependent allelic reporter effect is predicted. |
| GTEx breast-mammary eQTL lookup for TOX3 at rs4784227 (already performed in E09) | low | yes | No significant TOX3 eQTL in breast mammary tissue, consistent with no direct expression effect. | A detectable TOX3 eQTL would be expected if the enhancer changes TOX3 expression; E09 observed none. | A detectable TOX3 eQTL would be expected if ESR1 changes TOX3 expression; E09 observed none. | A detectable TOX3 eQTL would be expected if CTCF loss changes TOX3 expression; E09 observed none. |

## Next experiment

Allele-specific FOXA1 ChIP-qPCR at rs4784227 in MCF7 (or another heterozygous ER-positive breast-cancer line): H1 predicts higher FOXA1 signal on alt T, whereas H4 predicts no allele-specific difference.

## Investigate calls

- chip_peaks({"tf": "FOXA1", "biosample": "MCF7"})
- chip_peaks({"tf": "ESR1", "biosample": "MCF7"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})

## Flags

- quote_rejected: PMID 41230718: not an exact substring of the abstract

Citation support: 0.87 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:52565276-52565276:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:24+00:00)

> Variant chr16:52565276:C>T (GRCh38), allele string C/T
> Known IDs: rs4784227
> Most severe consequence: intron_variant
> Regulatory features: ENSR16_9QTBS enhancer
> GERP conservation score at the site: -2
> Transcript consequences: CASC16 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:51565276-53565276?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:47+00:00)

> 6 protein-coding genes within 1000 kb of chr16:52565276:C>T, by distance to TSS:
> TOX3: 17.5 kb from TSS (upstream, strand -1)
> CHD9NB: 487.6 kb from TSS (downstream, strand -1)
> CHD9: 489.7 kb from TSS (upstream, strand +1)
> RBL2: 868.7 kb from TSS (upstream, strand +1)
> AKTIP: 939.1 kb from TSS (downstream, strand -1)
> HNRNPA1L3: 1011.8 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E3180851 (dELS: distal enhancer-like), chr16:52565011-52565360.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3180851 dELS (contains the variant): DNase z 4.2, H3K27ac z 6.1, H3K4me3 z 1.8, CTCF z 1.9; nearby genes CASC16, TOX3, AC026462.5
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs4784227&size=100; retrieved 2026-10-25T17:26:28+00:00)

> 34 GWAS Catalog associations for rs4784227, strongest first:
> Breast cancer: p 2.0e-240, effect allele T, risk-allele frequency NR, PMID 32139696
> Postmenopausal breast cancer: p 5.0e-50, effect allele T, risk-allele frequency NR, PMID 38538606
> Breast cancer (estrogen-receptor negative): p 2.0e-26, effect allele T, risk-allele frequency 0.24, PMID 29058716
> Biological Mother:  Cancer, Breast: p 2.0e-25, effect allele C, risk-allele frequency 0.7783, PMID 39024449
> Breast cancer (estrogen-receptor positive): p 1.0e-13, effect allele T, risk-allele frequency 0.06, PMID 38741014
> Parkinson's disease: p 1.0e-10, effect allele T, risk-allele frequency 0.265, PMID 28892059
> Systolic blood pressure: p 1.0e-09, effect allele T, risk-allele frequency 0.2398, PMID 33230300
> BRCA1/2-negative high-risk breast cancer: p 2.0e-09, effect allele T, risk-allele frequency 0.26, PMID 30323354
> Pulse pressure: p 2.0e-08, effect allele T, risk-allele frequency 0.2354, PMID 33230300
> Cancer: p 3.0e-08, effect allele ?, risk-allele frequency NR, PMID 34290314

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:25+00:00)

> 83 credible sets contain 16_52565276_C_T: 74 GWAS, 9 molecular QTL.
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, excluding all cancers (control: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.93
> GWAS Breast cancer (luminal A): PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, ER-positive, excluding all can: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer [female] (PheCode 174.1): PIP 1.00; L2G TOX3 0.92
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_spinal_cord_ensg00000285800_1_): PIP 0.07
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_hippocampus_ensg00000285800): PIP 0.06
> tuqtl for TOX3 (gtex-v10_txrev_brain_hippocampus_ensg00000103460_g): PIP 0.05
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_spinal_cord_ensg00000285800): PIP 0.04
> tuqtl for TOX3 (gtex-v10_txrev_brain_substantia_nigra_ensg00000103): PIP 0.04
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_hippocampus_ensg00000285800_1_): PIP 0.03
> Best L2G gene scores across these sets: TOX3 0.96

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20AND%20TOX3%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:28+00:00)

> Europe PMC: 77 hits for 'rs4784227 AND TOX3 AND "breast cancer"'; top 8 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 40932605 (2025): Molecular signatures of breast cancer in the Iranian population: a review of cell growth and cell cycle regulators.
> PMID 42001218 (2026): Prioritizing context-specific genetic risk mechanisms in 11 solid cancers.
> PMID 36042591 (2022): Association between the rs4784227-CASC16 polymorphism and the risk of breast cancer: A meta-analysis.
> PMID 39777116 (2025): Identification of significant single-nucleotide polymorphisms associated with breast cancer recurrence and metastasis using GWAS.
> PMID 38741014 (2024): Genome-wide association analyses of breast cancer in women of African ancestry identify new susceptibility loci and improve risk prediction.
> PMID 39587695 (2024): The shared genetic landscape of polycystic ovary syndrome and breast cancer: convergence on ER + breast cancer but not ER- breast cancer.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:50+00:00)

> 1 ENCODE FOXA1 ChIP-seq peaks contain chr16:52565276:C>T in biosamples matching 'MCF7': biosamples MCF-7; experiments ENCSR126YEB. In other biosamples, 7 FOXA1 peaks do contain the variant: A549, HepG2, liver (experiments ENCSR000BLE, ENCSR000BMO, ENCSR000BRD, ENCSR324RCI, ENCSR735KEY, ENCSR865RXA).

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:29:55+00:00)

> No ENCODE ESR1 ChIP-seq peak contains chr16:52565276:C>T in biosamples matching 'MCF7'. Absence can also mean no ESR1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
