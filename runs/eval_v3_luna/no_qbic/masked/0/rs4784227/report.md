# rs4784227 and Breast cancer (16q12)

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 124 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.76)

Null chain: no TF-mediated effect of this variant.

Predictions: There will be no reproducible allele-specific TF occupancy or TF-dependent enhancer effect attributable to this C-to-T change in relevant breast cells.; The strong breast-cancer association may reflect a linked causal change, a non-TF mechanism, or another effect not mediated by this variant.

Falsified if: In relevant breast cells, the variant shows reproducible allele-specific binding by a TF and variant- or TF-perturbation demonstrates a corresponding allele-dependent regulatory effect.

### 2. H1: Hypothesized alt-enhanced FOXA1 binding affects a TOX3-linked enhancer (p = 0.14)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies the variant-containing site in MCF-7; this chain hypothesizes stronger binding to alt T, but the supplied evidence has no allele-specific measurement or FOXA1 QBiC-SELEX result establishing that direction. FOXA1 is selected as a candidate because it is expressed and has MCF-7 occupancy at the site, not because it is shown to be the variant-sensitive factor. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies in distal enhancer-like cCRE EH38E3180851, with activity marks reported among ENCODE biosamples; these maxima do not establish activity in MCF-7 specifically. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is a plausible target based on proximity and high breast-cancer L2G scores, but no supplied evidence directly links this cCRE to TOX3; the reported GTEx results do not provide a significant eQTL for the variant. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | MCF-7 is a plausible context because FOXA1 is abundant there and ChIP-seq peaks containing the variant are reported in MCF-7; this does not establish MCF-7-specific activity of the cCRE or allele-specific binding. | supported | [E05](#e05) |
| phenotype | This chain proposes that greater FOXA1 binding on T increases enhancer output and TOX3 expression, potentially contributing to breast-cancer risk. The variant is strongly associated with breast cancer and T is reported as the effect allele in several associations, but the regulatory chain and its effect on risk are untested; one listed association reports C as the effect allele. | weak | [E15](#e15), [E16](#e16), [E21](#e21) |

Predictions: If the binding hypothesis is correct, allele-informative MCF-7 FOXA1 ChIP-seq or CUT&RUN reads will be enriched for T over C at this site.; A variant-dependent FOXA1 or enhancer perturbation will change enhancer output and, if TOX3 is the target, TOX3 expression preferentially from the T-bearing haplotype.

Falsified if: Adequately powered allele-specific measurements show no FOXA1 enrichment on T, or show enrichment on C.; FOXA1 or enhancer perturbation produces no variant-dependent effect on enhancer output or on TOX3 expression.

### 3. H2: Hypothesized alt-enhanced GATA3 binding represses a TOX3-linked enhancer (p = 0.10)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3180851; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 occupies the variant-containing site in MCF-7; this chain hypothesizes stronger binding to alt T, but the supplied evidence has no allele-specific measurement or GATA3 QBiC-SELEX result establishing that direction. GATA3 is a candidate because it is highly expressed and has MCF-7 occupancy here, not because it is shown to be the variant-sensitive factor. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies in distal enhancer-like cCRE EH38E3180851, with activity marks reported among ENCODE biosamples; these maxima do not establish activity in MCF-7 specifically. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is a plausible target based on proximity and high breast-cancer L2G scores, but no supplied evidence directly links this cCRE to TOX3; the reported GTEx results do not provide a significant eQTL for the variant. | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20) |
| cell_type | MCF-7 is a plausible context because GATA3 is highly expressed there and ChIP-seq peaks containing the variant are reported in MCF-7; this does not establish MCF-7-specific activity of the cCRE or allele-specific binding. | supported | [E06](#e06) |
| phenotype | This chain proposes that greater GATA3 binding on T represses enhancer output and lowers TOX3 expression, potentially contributing to breast-cancer risk. Neither repression nor the expression effect is established, and the risk association does not establish this mechanism; one listed association reports C as the effect allele. | weak | [E15](#e15), [E16](#e16), [E21](#e21) |

Predictions: If the binding hypothesis is correct, allele-informative MCF-7 GATA3 ChIP-seq or CUT&RUN reads will be enriched for T over C at this site.; Greater GATA3 activity or occupancy will reduce enhancer output and, if TOX3 is the target, reduce TOX3 expression preferentially from the T-bearing haplotype.

Falsified if: Adequately powered allele-specific measurements show no GATA3 enrichment on T, or show enrichment on C.; GATA3 or enhancer perturbation does not produce the predicted allele-dependent reduction in enhancer output or TOX3 expression.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Reanalyze allele-informative MCF-7 FOXA1 ChIP-seq reads spanning the variant for allelic imbalance, accounting for mapping bias. | existing data | yes | No reproducible T-versus-C FOXA1 occupancy imbalance. | More FOXA1 reads from the T-bearing allele. | No required FOXA1 imbalance; GATA3, rather than FOXA1, is the proposed allele-sensitive factor. |
| Measure allele-specific GATA3 occupancy at the site in MCF-7 using allele-informative ChIP-seq or CUT&RUN reads. | existing data | no | No reproducible T-versus-C GATA3 occupancy imbalance. | No required GATA3 imbalance; FOXA1 is the proposed allele-sensitive factor. | More GATA3 occupancy from the T-bearing allele. |
| Perturb the variant-containing cCRE in MCF-7 and measure allele-specific enhancer output and TOX3 expression. | high | yes | No reproducible variant-dependent TF-mediated change in enhancer output or TOX3 expression. | A FOXA1-dependent increase in enhancer output and TOX3 expression on the T-bearing haplotype. | A GATA3-dependent decrease in enhancer output and TOX3 expression on the T-bearing haplotype. |

## Next experiment

The cheapest discriminator between the top two hypotheses (H0 and H1) is allele-specific reanalysis of existing MCF-7 FOXA1 ChIP-seq reads spanning the variant, if the reads and genotype are informative. Test for T-allele enrichment while controlling mapping bias; no enrichment would favor H0 over H1, whereas reproducible T enrichment would support H1's binding prediction but would not by itself prove enhancer activity, TOX3 targeting, or disease mediation.

## Investigate calls

- literature_search({"query": "chr16:52565276 TOX3 breast cancer variant enhancer functional study allele-specific"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- gene_disease({"gene": "TOX3"})

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

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr16%3A52565276%20TOX3%20breast%20cancer%20variant%20enhancer%20functional%20study%20allele-specific&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:17:42+00:00)

> Europe PMC: 0 hits for 'chr16:52565276 TOX3 breast cancer variant enhancer functional study allele-specific'; top 0 with PMIDs:

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e21"></a>**E21** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:34:32+00:00)

> Open Targets: TOX3 and breast cancer (MONDO_0007254), overall score 0.58; by evidence type: genetic_association 0.91, literature 0.89
