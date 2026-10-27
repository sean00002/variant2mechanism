# rs4784227 and Breast cancer (16q12)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 177 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H1_FOXA1_alt_TOX3: Risk allele T strengthens a FOXA1-bound TOX3 enhancer (p = 0.45)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7 luminal breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies the rs4784227-containing element in MCF7 (E07); the alt T allele is hypothesized to bind FOXA1 more strongly than the ref C allele, but allele-specific binding is not demonstrated. FOXA1 QBiC-SELEX coverage is not_checked. | weak | [E07](#e07) |
| element | rs4784227 lies in the distal enhancer-like cCRE EH38E3180851, and a FOXA1 ChIP-seq peak in MCF7 contains this element, consistent with a FOXA1-bound enhancer; allele-specific enhancer activity is not yet shown. | supported | [E01](#e01), [E03](#e03), [E07](#e07) |
| gene | TOX3 is the nearest protein-coding gene and the best L2G gene for breast cancer credible sets at this locus; however, no significant breast eQTL was detected, so the enhancer-gene link remains indirect. | weak | [E02](#e02), [E05](#e05), [E06a](#e06a), [E09](#e09) |
| cell_type | MCF7 is the provided DepMap expression context, and MCF7 has an ENCODE FOXA1 ChIP-seq peak containing rs4784227. | supported | [E07](#e07) |
| phenotype | T is the reported breast-cancer risk/effect allele; if T increases FOXA1-bound TOX3 enhancer activity in luminal breast cells, this could increase risk, but the causal chain is not directly shown. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: Allele-specific FOXA1 ChIP shows higher FOXA1 occupancy on T than C at rs4784227 in MCF7 or another heterozygous luminal breast line.; A C-vs-T enhancer reporter in MCF7 shows higher activity for T, and the difference is reduced by FOXA1 knockdown.; Endogenous base editing or enhancer perturbation shows T increases TOX3 expression in luminal breast cells.

Falsified if: Allele-specific FOXA1 ChIP shows equal binding or stronger binding on C than T.; Reporter assays show no T-vs-C enhancer activity difference or higher activity on C.; TOX3 expression is not higher in T-allele carriers or T-edited luminal breast cell models.

### 2. H5_null: No TF-mediated allelic effect at rs4784227 (p = 0.38)

Null chain: no TF-mediated effect of this variant.

Predictions: rs4784227 is a marker for a linked causal variant elsewhere at 16q12 rather than a functional TF-binding allele.; Allele-specific FOXA1 binding and enhancer activity at rs4784227 are absent after controlling for linked variants.; Breast-cancer association at this locus is explained by TOX3 regulatory variation not mediated by rs4784227 itself.

Falsified if: Robust allele-specific FOXA1 binding is demonstrated at rs4784227.; Reporter assays show rs4784227 allele-dependent enhancer activity in breast cells.; CRISPR base editing of rs4784227 changes TOX3 expression and a breast-cancer-relevant phenotype.

### 3. H3_FOXA1_ref_TOX3: Protective C allele strengthens a FOXA1-bound TOX3 enhancer (p = 0.10)

TF FOXA1 (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E3180851; gene TOX3; cell type MCF7 luminal breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies the rs4784227-containing element in MCF7 (E07); the ref C allele is hypothesized to bind FOXA1 more strongly than the alt T allele, opposite to H1, but allele-specific binding is not demonstrated. FOXA1 QBiC-SELEX coverage is not_checked. | weak | [E07](#e07) |
| element | rs4784227 lies in the distal enhancer-like cCRE EH38E3180851, and FOXA1 occupies this element in MCF7; stronger FOXA1 binding on C is proposed to increase enhancer activity, but this is not shown. | weak | [E01](#e01), [E03](#e03), [E07](#e07) |
| gene | The enhancer is proposed to regulate TOX3, supported indirectly by proximity and L2G mapping; no significant breast eQTL was detected. | weak | [E02](#e02), [E05](#e05), [E06a](#e06a), [E09](#e09) |
| cell_type | The proposed effect is in MCF7/luminal breast cancer cells, where FOXA1 occupies this element. | supported | [E07](#e07) |
| phenotype | C is protective in breast-cancer GWAS/meta-analysis; if C strengthens a FOXA1-bound TOX3 enhancer that increases a protective TOX3 output, this would fit the genetic direction, but the mechanism is unsupported. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: Allele-specific FOXA1 ChIP shows higher FOXA1 occupancy on C than T.; A C-vs-T enhancer reporter in MCF7 shows higher activity for C.; TOX3 expression is higher in C-allele carriers or C-edited luminal breast cell models.

Falsified if: Allele-specific FOXA1 ChIP shows stronger binding on T than C.; Reporter assays show higher enhancer activity on T than C.; TOX3 expression is not higher with the C allele.

### 4. H4_FOXA1_alt_CASC16: Risk allele T strengthens a FOXA1-bound enhancer controlling CASC16 lncRNA (p = 0.07)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element EH38E3180851; gene CASC16; cell type MCF7 luminal breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies the rs4784227-containing element in MCF7 (E07); the alt T allele is hypothesized to bind FOXA1 more strongly than ref C, but allele-specific binding is not demonstrated. FOXA1 QBiC-SELEX coverage is not_checked. | weak | [E07](#e07) |
| element | rs4784227 lies in the distal enhancer-like cCRE EH38E3180851, and FOXA1 occupies this element in MCF7, consistent with a FOXA1-bound enhancer; allele-specific activity is not shown. | supported | [E01](#e01), [E03](#e03), [E07](#e07) |
| gene | rs4784227 is annotated as a CASC16 intronic variant and CASC16 is nearby, so the enhancer could regulate CASC16; however, the strongest L2G gene is TOX3, making this target less supported. | weak | [E01](#e01), [E03](#e03), [E05](#e05) |
| cell_type | The proposed effect is in MCF7/luminal breast cancer cells, where FOXA1 occupies this element; CASC16-specific expression in MCF7 is not shown. | weak | [E07](#e07) |
| phenotype | T is the reported breast-cancer risk allele; allele-specific CASC16 lncRNA regulation could contribute to risk, but this is not directly supported. | weak | [E04](#e04), [E06b](#e06b) |

Predictions: Allele-specific FOXA1 ChIP shows higher FOXA1 occupancy on T than C.; CASC16 lncRNA expression, more than TOX3 expression, differs by rs4784227 genotype in breast cell models.; The EH38E3180851 enhancer physically contacts the CASC16 locus.

Falsified if: The enhancer does not contact or regulate CASC16.; CASC16 expression is unchanged by allele-specific enhancer activity.; TOX3, not CASC16, explains the allele-specific effect.

## Prediction matrix

| Test | Cost | Separates top two | H1_FOXA1_alt_TOX3 | H5_null | H3_FOXA1_ref_TOX3 | H4_FOXA1_alt_CASC16 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific FOXA1 ChIP-qPCR or ChIP-seq at rs4784227 in MCF7 or another heterozygous luminal breast line | low | yes | Higher FOXA1 occupancy on T than C | Equal FOXA1 occupancy on C and T | Higher FOXA1 occupancy on C than T | Higher FOXA1 occupancy on T than C |
| C-vs-T enhancer reporter or MPRA in MCF7 cells | medium | yes | T allele gives higher enhancer activity; reduced by FOXA1 knockdown | No allele-specific enhancer activity | C allele gives higher enhancer activity | T allele gives higher enhancer activity |
| CRISPR base editing of rs4784227 C>T in an endogenous luminal breast cell line with TOX3 and CASC16 expression readouts | high | yes | T edit increases TOX3 expression | No allele-specific change in TOX3 or CASC16 | C edit increases TOX3 expression | T edit increases CASC16 more than TOX3 |
| Allele-specific expression or eQTL analysis for TOX3 and CASC16 in breast tissue | medium | yes | T allele associates with higher TOX3 expression | No cis-association with TOX3 or CASC16 | C allele associates with higher TOX3 expression | T allele associates with CASC16 expression |

## Next experiment

Allele-specific FOXA1 ChIP-qPCR at rs4784227 in MCF7 or another heterozygous luminal breast cell line, comparing FOXA1 occupancy on the C and T alleles; this is the cheapest test that directly separates H1_FOXA1_alt_TOX3 from H5_null.

## Investigate calls

- chip_peaks({"tf": "FOXA1", "biosample": "MCF7"})
- chip_peaks({"tf": "ESR1", "biosample": "MCF7"})
- eqtl_lookup({"tissue": "breast"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

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

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-25T17:26:28+00:00)

> Key examples include promoter mutations [e.g., rs2279744 (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs4784227 (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> The pooled ORs regarding the association between the rs4784227-CASC16 polymorphism and breast cancer risk were statistically significant [T vs C: OR = 1.244, 95% CI = 1.202-1.287; TT vs CT + CC: OR = 1.407, 95% CI = 1.296-1.528; CC vs CT + TT: OR = 0.777, 95% CI = 0.745-0.811; TT vs CC: OR = 1.544, 95% CI = 1.419-1.681; CT vs CC: OR = 1.244, 95% CI = 1.189-1.301].

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> Our pooled analysis showed a significant association between the rs4784227- (T) allele and breast cancer susceptibility in Asian and North American populations, and intervention with this mutation might be a new therapeutic strategy for breast cancer.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:50+00:00)

> 1 ENCODE FOXA1 ChIP-seq peaks contain chr16:52565276:C>T in biosamples matching 'MCF7': biosamples MCF-7; experiments ENCSR126YEB. In other biosamples, 7 FOXA1 peaks do contain the variant: A549, HepG2, liver (experiments ENCSR000BLE, ENCSR000BMO, ENCSR000BRD, ENCSR324RCI, ENCSR735KEY, ENCSR865RXA).

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:29:55+00:00)

> No ENCODE ESR1 ChIP-seq peak contains chr16:52565276:C>T in biosamples matching 'MCF7'. Absence can also mean no ESR1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'breast'. NES is the effect of the alt allele (T) relative to ref (C).
