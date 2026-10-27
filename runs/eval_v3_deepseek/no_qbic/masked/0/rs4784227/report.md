# rs4784227 and Breast cancer (16q12)

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 144 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H1: Risk T allele strengthens a GATA3-bound TOX3 enhancer (p = 0.34)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851 dELS; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is occupied at the variant in MCF-7 (5 MCF-7 peaks, E21; E06) and is one of the most highly expressed TFs there (346 TPM, rank 5). No QBiC-SELEX model or direct allele-specific GATA3 assay is provided, so the proposal that the alt T allele strengthens GATA3 binding is an inference from T being the reported risk/effect allele, not a measured affinity change. Occupancy plus high expression favor GATA3 over other GATA-motif factors, but this remains correlational. | weak | [E06](#e06), [E21](#e21), [E15](#e15) |
| element | The variant lies inside EH38E3180851, a distal enhancer-like cCRE with DNase and H3K27ac marks, consistent with an active regulatory element. | supported | [E03](#e03) |
| gene | TOX3 is the nearest protein-coding gene (17.5 kb upstream) and receives strong fine-mapping/L2G support as the target of this breast cancer signal. GTEx v8 shows no significant eQTL at this base, but those data are not from breast cancer cells and do not test this context. | supported | [E02](#e02), [E16](#e16), [E18a](#e18a), [E17](#e17), [E20](#e20) |
| cell_type | MCF-7 is a luminal breast cancer line in which GATA3 is bound at this element and very highly expressed. | supported | [E06](#e06), [E21](#e21) |
| phenotype | The locus is strongly associated with breast cancer, with the T allele reported as the effect allele in the strongest breast cancer associations; L2G links the credible set to TOX3. | supported | [E15](#e15), [E16](#e16) |

Predictions: The alt T allele improves the GATA3 motif score and shows stronger allele-specific GATA3 binding than C in MCF-7 cells.; CRISPR C>T increases enhancer activity and TOX3 expression in breast cancer cells, and GATA3 depletion reduces this effect.

Falsified if: Allele-specific GATA3 assays show equal or stronger binding on the C allele.; The C/T change does not alter enhancer activity or TOX3 expression in breast cancer cells.; GATA3 perturbation does not affect the enhancer or TOX3 expression.; Fine-mapping shows a different linked variant, not this base, is causal.

### 2. H2: Risk T allele strengthens a FOXA1-bound TOX3 enhancer (p = 0.30)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851 dELS; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is occupied at the variant in MCF-7 (8 MCF-7 peaks, E05) and expressed there (rank 28). No QBiC-SELEX model or direct allele-specific FOXA1 assay is provided, so the claim that the alt T allele strengthens FOXA1 binding is inferred from T being the reported risk allele and from occupancy, not measured. FOXA1 is a pioneer TF that can act with GATA3 at the same element. | weak | [E05](#e05), [E15](#e15) |
| element | The variant is in EH38E3180851, an active distal enhancer-like element marked by DNase and H3K27ac. | supported | [E03](#e03) |
| gene | TOX3 is the nearest protein-coding gene and is the best-supported target from genetic fine-mapping/L2G. GTEx v8 lacks a significant eQTL here, but those tissues are not breast cancer cells. | supported | [E02](#e02), [E16](#e16), [E18a](#e18a), [E17](#e17), [E20](#e20) |
| cell_type | MCF-7 breast cancer cells show FOXA1 ChIP occupancy at this element and express FOXA1. | supported | [E05](#e05) |
| phenotype | This locus is a strong breast cancer susceptibility signal, with T reported as the effect allele in the strongest breast cancer GWAS associations. | supported | [E15](#e15), [E16](#e16) |

Predictions: The alt T allele improves the FOXA1 motif score and shows stronger allele-specific FOXA1 binding than C in MCF-7 cells.; FOXA1 depletion reduces T-allele enhancer activity and TOX3 expression.

Falsified if: FOXA1 binds equally to both alleles or preferentially to the C allele.; FOXA1 perturbation does not alter enhancer activity or TOX3 expression.; A different linked variant is shown to be causal.

### 3. H4: Null: no TF-mediated effect of this exact variant (p = 0.28)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at chr16:52565276 is found for a relevant breast cancer TF.; The GWAS signal is explained by a linked causal variant in the credible set rather than this base.; The C/T change does not alter enhancer activity or TOX3 expression in relevant breast cancer cells.

Falsified if: Allele-specific binding of a relevant TF at this exact base is demonstrated together with an enhancer/TOX3 expression effect.; CRISPR or reporter assays show the C/T change itself alters regulatory activity in breast cancer cells.

### 4. H3: Risk T allele strengthens an SPDEF-bound TOX3 enhancer (p = 0.08)

TF SPDEF (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851 dELS; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SPDEF is occupied at the variant in MCF-7 (2 peaks, E07) and expressed (rank 40). No QBiC-SELEX model or direct allele-specific SPDEF assay is provided, so the proposal that the alt T allele strengthens SPDEF binding is inferred from the risk allele and occupancy, not measured. Occupancy support is weaker than for GATA3 or FOXA1. | weak | [E07](#e07), [E15](#e15) |
| element | The variant lies in an active distal enhancer-like cCRE, EH38E3180851. | supported | [E03](#e03) |
| gene | TOX3 is the nearest protein-coding gene and receives strong L2G support as the target of the breast cancer signal. | supported | [E02](#e02), [E16](#e16) |
| cell_type | SPDEF ChIP peaks containing the variant are present in MCF-7 cells, where SPDEF is expressed. | supported | [E07](#e07) |
| phenotype | The variant is associated with breast cancer risk, with T the reported effect allele in major breast cancer GWAS. | supported | [E15](#e15) |

Predictions: SPDEF ChIP or binding is stronger on the T allele than the C allele at this element in MCF-7 cells.; SPDEF knockdown reduces T-allele enhancer activity or TOX3 expression.

Falsified if: SPDEF binding is not allele-specific at this base.; SPDEF perturbation does not affect the enhancer or TOX3 expression.; SPDEF occupancy is explained entirely by another factor at the element.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H4 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| PWM motif analysis of ref C vs alt T for GATA3 and FOXA1 motifs using existing genomic sequence | existing data | yes | Alt T improves the GATA3 motif score; FOXA1 motif is unchanged or weaker. | Alt T improves the FOXA1 motif score; GATA3 motif is unchanged. | No relevant TF motif change at the base. | Neither GATA3 nor FOXA1 motif changes; an SPDEF-like motif may change instead. |
| Allele-specific GATA3 and FOXA1 ChIP (or EMSA) at the variant in MCF-7 cells | medium | yes | GATA3 binds T more strongly than C; FOXA1 shows no allele preference. | FOXA1 binds T more strongly than C; GATA3 shows no allele preference. | No allele-specific binding for any tested TF. | GATA3 and FOXA1 show no allele preference; SPDEF may bind T more strongly. |
| CRISPR C>T knock-in in MCF-7 followed by TOX3 expression and enhancer-activity measurement | high | no | T allele increases TOX3 expression/enhancer activity in a GATA3-dependent manner. | T allele increases TOX3 expression/enhancer activity in a FOXA1-dependent manner. | No change in TOX3 expression or enhancer activity. | T allele increases TOX3 expression/enhancer activity in an SPDEF-dependent manner. |
| Depletion of GATA3 vs FOXA1 vs SPDEF in MCF-7, measuring TOX3 and T-allele enhancer activity | medium | yes | GATA3 depletion reduces TOX3/enhancer activity; FOXA1 and SPDEF depletion do not. | FOXA1 depletion reduces TOX3/enhancer activity; GATA3 and SPDEF depletion do not. | No TF depletion affects TOX3/enhancer activity at this base. | SPDEF depletion reduces TOX3/enhancer activity; GATA3 and FOXA1 depletion do not. |

## Next experiment

Run the cheapest separating test first: compute ref/alt PWM scores for the GATA3 and FOXA1 motifs from the existing genomic sequence. If the alt T changes only one motif, that directly favors H1 or H2; if neither changes, proceed to allele-specific GATA3/FOXA1 ChIP or EMSA in MCF-7 cells.

## Investigate calls

- literature_search({"query": "rs3803662 TOX3 enhancer FOXA1 GATA3 allele-specific binding breast cancer"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- chip_peaks({"tf": "GATA3", "biosample": "MCF-7"})

## Flags

- quote_rejected: PMID 30116257: not an exact substring of the abstract

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

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr16:52565276:C>T: 276 peaks contain the variant, from 193 factors in 7 biosamples. In the matching biosample MCF-7: 14 peaks from 9 factors. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, ARID5B, ASH2L, BCL3, CBX5, CHD4, CTBP1, DPF2, EP300, GATAD1, GZF1, HBP1 (+64 more). Bound, expressed TFs with a binding model: 95; listed one per row: FOXA1, GATA3, SPDEF, NR2F2, TCF7L2, SP1, MYBL2, MAX, JUND, RXRA; also bound: YY1, GATAD2A, ZGPAT, CREM, FOSL2, ZNF609, ZNF703, TEAD1, RXRB, FOXP4, EGR1, MEF2D, ZNF800, AHDC1, GMEB1, ZNF772, ZNF788P, HMG20B, ELF1, TRAFD1, E2F4, ELF3, RELA, MLX, TBX2, ERF, HMG20A, BHLHE40, CREB1, ZBTB7B (+55 more). Bound but below 1 TPM: DLX6, ETS1, FOXA2, FOXA3, GATA4, GFI1, HLF, HNF1A, HNF1B, HNF4A. Assayed with no peak here: 45 TFs in the matching biosample, 411 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXA1: bound here. 8 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in A549, HepG2, liver (e.g. ENCSR126YEB). 88.38 TPM in DepMap:ACH-000019 (MCF7), rank 28 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATA3: bound here. 7 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in A549, T47D (e.g. ENCSR000EWV). 346.04 TPM in DepMap:ACH-000019 (MCF7), rank 5 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SPDEF: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR042GSX). 72.51 TPM in DepMap:ACH-000019 (MCF7), rank 40 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in HepG2 (e.g. ENCSR000BUY). 38.14 TPM in DepMap:ACH-000019 (MCF7), rank 103 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000EWT). 4.89 TPM in DepMap:ACH-000019 (MCF7), rank 642 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound elsewhere. 6 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, HepG2, liver (e.g. ENCSR386YIH). 33.01 TPM in DepMap:ACH-000019 (MCF7), rank 122 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 5 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BRO). 49.2 TPM in DepMap:ACH-000019 (MCF7), rank 66 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, liver (e.g. ENCSR521IID). 76.95 TPM in DepMap:ACH-000019 (MCF7), rank 35 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUND: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, liver (e.g. ENCSR000BGK). 44.21 TPM in DepMap:ACH-000019 (MCF7), rank 83 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> RXRA: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, liver (e.g. ENCSR352QSB). 30.65 TPM in DepMap:ACH-000019 (MCF7), rank 132 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs4784227&size=100; retrieved 2026-10-25T17:26:28+00:00)

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

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:25+00:00)

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

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TOX3%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:25:47+00:00)

> Europe PMC: 586 hits for 'TOX3 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 41849381 (2026): A transcription regulator atlas identifies TOX3 as an Atoh1 coactivator in cerebellar development and tumorigenesis.
> PMID 41595182 (2026): Identification and Characterisation of Canine Osteosarcoma Biomarkers and Therapeutic Targets.
> PMID 41596432 (2026): Bone Metastasis in Estrogen Receptor-Positive Breast Cancer: Molecular Insights and Therapeutic Advances.
> PMID 40932605 (2025): Molecular signatures of breast cancer in the Iranian population: a review of cell growth and cell cycle regulators.
> PMID 42700350 (2026): Interactions between circular RNAs (circRNAs) and the Hippo pathway in cancer.
> PMID 41871294 (2026): A reanalysis of a genome-wide association study on breast cancer in Asian populations using the SG10K_Health reference panel for imputation: a multi-Centre case-control analysis.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-26T02:25:47+00:00)

> Key examples include promoter mutations [e.g., rs[masked] (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs[masked] (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41871294 (https://europepmc.org/article/MED/41871294; retrieved 2026-10-26T02:25:47+00:00)

> Differences in panel performance influenced association signals, including breast cancer candidate loci such as FGFR2, TOX3, and ESR1.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs3803662%20TOX3%20enhancer%20FOXA1%20GATA3%20allele-specific%20binding%20breast%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:18:14+00:00)

> Europe PMC: 3 hits for 'rs[masked] TOX3 enhancer FOXA1 GATA3 allele-specific binding breast cancer'; top 2 with PMIDs:
> PMID 30116257 (2018): Elucidating the Underlying Functional Mechanisms of Breast Cancer Susceptibility Through Post-GWAS Analyses.
> PMID 28377418 (2017): Characterizing Genetic Susceptibility to Breast Cancer in Women of African Ancestry.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e21"></a>**E21** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:50+00:00)

> 5 ENCODE GATA3 ChIP-seq peaks contain chr16:52565276:C>T in biosamples matching 'MCF-7': biosamples MCF-7; experiments ENCSR000BST, ENCSR000EWV, ENCSR423RTK. In other biosamples, 2 GATA3 peaks do contain the variant: A549, T47D (experiments ENCSR000BMX, ENCSR000BTI).
