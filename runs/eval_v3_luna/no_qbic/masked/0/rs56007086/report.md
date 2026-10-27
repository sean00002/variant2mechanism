# rs56007086 and Breast cancer (16q12)

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 9 model calls; 160 s.

Variant `chr16:52565398:G>A` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.70)

Null chain: no TF-mediated effect of this variant.

Predictions: There will be no reproducible allele-dependent TF occupancy or regulatory effect attributable to this base in relevant breast cells.; Any disease association, if present, will reflect another variant or another mechanism rather than a TF-mediated effect of this variant.

Falsified if: A reproducible allele-dependent TF-binding change is shown at this base and perturbation of the implicated TF changes linked regulatory output and a relevant gene-expression phenotype.

### 2. H1: FOXA1-dependent regulation of TOX3 (p = 0.18)

TF FOXA1 (QBiC-SELEX coverage own_model), ref allele binds more; element A CASC16 intronic site 38 bp from a dELS element; the dELS does not overlap the variant, and its reported activity maxima are not MCF-7-specific.; gene TOX3; cell type MCF-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is a leading candidate because it has multiple MCF-7 ChIP-seq peaks over the variant and is highly expressed; literature also mentions altered FOXA1 affinity in a TOX3 enhancer context. The ref-G direction is only a testable working hypothesis: no QBiC-SELEX result or other allele-specific binding evidence is supplied for this variant. | weak | [E05](#e05), [E20b](#e20b) |
| element | The variant lies in a CASC16 intron and near, but not within, an annotated dELS; the available activity maxima do not establish activity in MCF-7 or a variant-dependent effect. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is the nearest listed protein-coding gene, and a literature quote describes a FOXA1-affinity/TOX3 enhancer hypothesis at a masked locus; neither establishes that this variant or nearby dELS regulates TOX3, and no significant GTEx eQTL is reported. | weak | [E02](#e02), [E17](#e17), [E20b](#e20b) |
| cell_type | FOXA1 occupancy over the variant and high FOXA1 expression are reported in MCF-7, making it a relevant context in which to test this chain. | supported | [E05](#e05) |
| phenotype | TOX3 has breast-cancer association evidence, but no evidence here connects this variant to TOX3 expression or disease; TOX3 is not a CRISPR dependency in MCF7, which provides no support for an essential-growth mechanism. | supported | [E19](#e19), [E21](#e21), [E18a](#e18a), [E18b](#e18b) |

Predictions: Allele-resolved FOXA1 occupancy in MCF-7 will be higher on ref G than alt A; this direction is a hypothesis, not an evidence-based prediction.; If the site affects TOX3 through FOXA1, perturbing FOXA1 will alter the relevant regulatory output and TOX3 expression more than perturbing GATA3.

Falsified if: A sufficiently powered allele-resolved assay finds no FOXA1 occupancy imbalance or finds higher occupancy on alt A.; FOXA1 perturbation has no effect on the candidate regulatory output or TOX3 expression in a relevant assay.

### 3. H2: GATA3-dependent regulation of TOX3 (p = 0.08)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element A CASC16 intronic site 38 bp from a dELS element; the dELS does not overlap the variant, and its reported activity maxima are not MCF-7-specific.; gene TOX3; cell type MCF-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is a competing candidate because it has MCF-7 ChIP-seq peaks over the variant and is highly expressed there. The alt-A direction is only a testable working hypothesis; no QBiC-SELEX result or other allele-specific binding evidence is supplied for this variant. | weak | [E06](#e06) |
| element | The variant lies in a CASC16 intron and near, but not within, an annotated dELS; the available activity maxima do not establish activity in MCF-7 or a variant-dependent effect. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is the nearest listed protein-coding gene and has breast-cancer association evidence, but no supplied evidence links this variant or the nearby dELS to TOX3 regulation; no significant GTEx eQTL is reported. | weak | [E02](#e02), [E17](#e17), [E19](#e19) |
| cell_type | GATA3 occupancy over the variant and high GATA3 expression are reported in MCF-7, making this a relevant context in which to test the chain. | supported | [E06](#e06) |
| phenotype | TOX3 has breast-cancer association evidence, but no evidence here connects this variant to TOX3 expression or disease; TOX3 is not a CRISPR dependency in MCF7, which does not establish or exclude a regulatory disease effect. | supported | [E19](#e19), [E21](#e21), [E18a](#e18a), [E18b](#e18b) |

Predictions: Allele-resolved GATA3 occupancy in MCF-7 will be higher on alt A than ref G; this direction is a hypothesis, not an evidence-based prediction.; If the site affects TOX3 through GATA3, perturbing GATA3 will alter the relevant regulatory output and TOX3 expression more than perturbing FOXA1.

Falsified if: A sufficiently powered allele-resolved assay finds no GATA3 occupancy imbalance or finds higher occupancy on ref G.; GATA3 perturbation has no effect on the candidate regulatory output or TOX3 expression in a relevant assay.

### 4. H3: SPDEF-dependent regulation of TOX3 (p = 0.04)

TF SPDEF (QBiC-SELEX coverage own_model), ref allele binds more; element A CASC16 intronic site 38 bp from a dELS element; the dELS does not overlap the variant, and its reported activity maxima are not MCF-7-specific.; gene TOX3; cell type MCF-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SPDEF is a lower-priority candidate because one MCF-7 ChIP-seq peak contains the variant and SPDEF is expressed in MCF-7. The ref-G direction is only a testable working hypothesis; no QBiC-SELEX result or other allele-specific binding evidence is supplied for this variant. | weak | [E07](#e07) |
| element | The variant lies in a CASC16 intron and near, but not within, an annotated dELS; the available activity maxima do not establish activity in MCF-7 or a variant-dependent effect. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is the nearest listed protein-coding gene, but no supplied evidence connects this variant or the nearby dELS to TOX3 regulation; no significant GTEx eQTL is reported. | weak | [E02](#e02), [E17](#e17) |
| cell_type | SPDEF occupancy over the variant and SPDEF expression are reported in MCF-7, providing a context for testing this lower-priority candidate. | supported | [E07](#e07) |
| phenotype | TOX3 has breast-cancer association evidence, but no evidence here connects this variant to TOX3 expression or disease; TOX3 is not a CRISPR dependency in MCF7. | supported | [E19](#e19), [E21](#e21), [E18a](#e18a), [E18b](#e18b) |

Predictions: Allele-resolved SPDEF occupancy in MCF-7 will be higher on ref G than alt A; this direction is a hypothesis, not an evidence-based prediction.; If the site acts through SPDEF, perturbing SPDEF will alter the regulatory output more than perturbing FOXA1 or GATA3.

Falsified if: A sufficiently powered allele-resolved assay finds no SPDEF occupancy imbalance or finds higher occupancy on alt A.; SPDEF perturbation has no effect on the candidate regulatory output or TOX3 expression in a relevant assay.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-resolved FOXA1 and GATA3 CUT&RUN in MCF-7, with sequencing across the site | medium | yes | No reproducible allele-dependent occupancy is detected for these candidate TFs. | FOXA1 occupancy is higher on ref G than alt A. | GATA3 occupancy is higher on alt A than ref G. | Neither FOXA1 nor GATA3 shows the predicted chain-specific result; SPDEF occupancy should instead be higher on ref G. |
| Perturb FOXA1, GATA3, or SPDEF separately in MCF-7 and measure candidate-element activity and TOX3 expression | high | yes | No candidate TF perturbation produces a variant-linked regulatory effect on TOX3. | FOXA1 perturbation preferentially changes candidate-element activity and TOX3 expression. | GATA3 perturbation preferentially changes candidate-element activity and TOX3 expression. | SPDEF perturbation preferentially changes candidate-element activity and TOX3 expression. |
| CRISPRi the nearby dELS in MCF-7 and measure TOX3 expression | medium | no | No reproducible TOX3 effect attributable to repression of this candidate element. | If this nearby element mediates the chain, CRISPRi may alter TOX3 expression; the result is not specific to FOXA1 without an additional TF test. | If this nearby element mediates the chain, CRISPRi may alter TOX3 expression; the result is not specific to GATA3 without an additional TF test. | If this nearby element mediates the chain, CRISPRi may alter TOX3 expression; the result is not specific to SPDEF without an additional TF test. |

## Next experiment

Perform allele-resolved CUT&RUN for FOXA1 and GATA3 in MCF-7 and sequence the site to test for allelic imbalance. This directly distinguishes the two leading chains; the predicted binding directions remain unestablished until measured.

## Investigate calls

- gene_disease({"gene": "TOX3"})
- literature_search({"query": "TOX3 breast cancer enhancer variant regulatory element"})
- gene_dependency({"gene": "TOX3"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:52565398-52565398:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:25:34+00:00)

> Variant chr16:52565398:G>A (GRCh38), allele string G/A
> Known IDs: rs56007086
> Most severe consequence: intron_variant
> Regulatory features: ENSR16_9QTBS enhancer
> GERP conservation score at the site: -4.73
> Transcript consequences: CASC16 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:51565398-53565398?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:25:46+00:00)

> 6 protein-coding genes within 1000 kb of chr16:52565398:G>A, by distance to TSS:
> TOX3: 17.6 kb from TSS (upstream, strand -1)
> CHD9NB: 487.5 kb from TSS (downstream, strand -1)
> CHD9: 489.6 kb from TSS (upstream, strand +1)
> RBL2: 868.6 kb from TSS (upstream, strand +1)
> AKTIP: 939.0 kb from TSS (downstream, strand -1)
> HNRNPA1L3: 1012.0 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:25:06+00:00)

> No cCRE overlaps the variant; nearest is EH38E3180851 (dELS) 38 bp away.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3180851 dELS: DNase z 4.2, H3K27ac z 6.1, H3K4me3 z 1.8, CTCF z 1.9; nearby genes CASC16, TOX3, AC026462.5
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr16:52565398:G>A: 215 peaks contain the variant, from 162 factors in 7 biosamples. In the matching biosample MCF-7: 16 peaks from 11 factors. No cCRE contains the variant. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, ARID5B, ASH2L, BCL3, CBX5, CHD4, CTBP1, EP300, GATAD1, GZF1, HBP1, HDAC1 (+51 more). Bound, expressed TFs with a binding model: 79; listed one per row: FOXA1, GATA3, SPDEF, NR2F2, CEBPB, TCF7L2, MYBL2, SP1, YY1, MAX; also bound: JUND, GATAD2A, BHLHE40, ZGPAT, RXRA, ZNF609, RXRB, ZNF770, FOXP4, AHDC1, GMEB1, ZNF772, ZNF788P, HMG20B, ELF1, ELF3, RELA, TBX2, ERF, HMG20A, CREB1, MBD1, ATF1, CREM, FOSL2, THAP11, SOX13, MEF2A, ZNF703, FOXJ3 (+39 more). Bound but below 1 TPM: DLX6, ETS1, FOXA2, FOXA3, GFI1, HLF, HNF1A, HNF1B, HNF4A, MAFF. Assayed with no peak here: 49 TFs in the matching biosample, 425 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXA1: bound here. 5 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in A549, HepG2, liver (e.g. ENCSR126YEB). 88.38 TPM in DepMap:ACH-000019 (MCF7), rank 28 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATA3: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000EWV). 346.04 TPM in DepMap:ACH-000019 (MCF7), rank 5 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SPDEF: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR042GSX). 72.51 TPM in DepMap:ACH-000019 (MCF7), rank 40 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000BUY). 38.14 TPM in DepMap:ACH-000019 (MCF7), rank 103 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000BSR). 24.33 TPM in DepMap:ACH-000019 (MCF7), rank 169 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000EWT). 4.89 TPM in DepMap:ACH-000019 (MCF7), rank 642 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 49.2 TPM in DepMap:ACH-000019 (MCF7), rank 66 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, liver (e.g. ENCSR000BPE). 33.01 TPM in DepMap:ACH-000019 (MCF7), rank 122 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> YY1: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: liver (e.g. ENCSR382MOM). 61.08 TPM in DepMap:ACH-000019 (MCF7), rank 48 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: liver (e.g. ENCSR521IID). 76.95 TPM in DepMap:ACH-000019 (MCF7), rank 35 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs56007086&size=100; retrieved 2026-10-26T02:25:35+00:00)

> 0 GWAS Catalog associations for rs56007086, strongest first:

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:25:34+00:00)

> Open Targets has no record of 16_52565398_G_A.

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565398_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:27:56+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565398_G_A_b38. NES is the effect of the alt allele (A) relative to ref (G).

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

<a id="e19"></a>**E19** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:34:32+00:00)

> Open Targets: TOX3 and breast cancer (MONDO_0007254), overall score 0.58; by evidence type: genetic_association 0.91, literature 0.89

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TOX3%20breast%20cancer%20enhancer%20variant%20regulatory%20element&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:26:34+00:00)

> Europe PMC: 34 hits for 'TOX3 breast cancer enhancer variant regulatory element'; top 8 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 41596432 (2026): Bone Metastasis in Estrogen Receptor-Positive Breast Cancer: Molecular Insights and Therapeutic Advances.
> PMID 41624772 (2025): Regulatory QTLs affecting miRNA-mRNA interactions in cancer: mechanisms, methods, and clinical implications.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 35011637 (2021): Three-Dimensional Genome Organization in Breast and Gynecological Cancers: How Chromatin Folding Influences Tumorigenic Transcriptional Programs.
> PMID 34741135 (2022): Functional annotation of breast cancer risk loci: current progress and future directions.
> PMID 38982523 (2024): Mapping the influence of hydrocarbons mixture on molecular mechanisms, involved in breast and lung neoplasms: in silico toxicogenomic data-mining.
> PMID 31338012 (2019): Association of <i>rs[masked]-CASC16 (LOC643714 locus)</i> and <i>rs[masked]-ACSF3</i> polymorphisms and their association with breast cancer risk among Iranian population.

<a id="e20a"></a>**E20a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-26T20:26:34+00:00)

> Key examples include promoter mutations [e.g., rs[masked] (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs[masked] (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e20b"></a>**E20b** literature_search, Europe PMC abstract, PMID 31338012 (https://europepmc.org/article/MED/31338012; retrieved 2026-10-26T20:26:34+00:00)

> This is in line with other studies suggesting these SNPs as risk-associated polymorphisms which may lead to a change in the affinity of FOXA1, as a distal enhancer, to TOX3 and thus change in TOX3 expression, which can eventually affect the risk of breast cancer.

<a id="e21"></a>**E21** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for TOX3 (0 = no effect, -1 = median common-essential; < -0.5 called dependent). MCF7 (ACH-000019): 0.11. Breast lineage, 53 lines: median 0.04, 0% dependent. All 1183 lines: median 0.05, 0% dependent.
