# rs56007086 and Breast cancer (16q12)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 247 s.

Variant `chr16:52565398:G>A` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z 12.52); SPDEF (bound here, z -7.0); NR2F2 (bound here, z 10.89, weak site); GATA3 (bound here, z 8.32, weak site); FOXA1 (bound here, z 6.27, weak site); CEBPB (bound here, z -1.64, no clear allelic change, weak site); NFIA (bound elsewhere, z 15.29); PITX1 (bound elsewhere, z 12.33); ZNF772 (bound elsewhere, z 9.58); AHDC1 (bound elsewhere, z 9.17). Occupancy unknown: ETV3 (z -47.67); SLC2A4RG (z -45.42); MTERF3 (z 24.43); PBX4 (z 18.55); SOX12 (z 17.9). Diagnostic, not shown to the model: 569 of 997 models pass Bonferroni.

## Ranked chains

### 1. H2_SPDEF: Ref allele preserves a stronger SPDEF site in the TOX3 enhancer (p = 0.46)

TF SPDEF (QBiC-SELEX coverage own_model), ref allele binds more; element ENSR16_9QTBS / dELS EH38E3180851 regulatory element; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SPDEF binds the ref G allele more strongly than the alt A allele. SPDEF has an MCF-7 ChIP-seq peak over the variant and high expression (E07), and its own QBiC-SELEX model gives a gate-passing ref-favoring change with a strong ref site (E21). | supported | [E07](#e07), [E21](#e21) |
| element | The variant lies in the ENSR16_9QTBS enhancer and SPDEF occupies the variant-containing element in MCF-7, although the nearest cCRE is a dELS 38 bp away rather than overlapping the variant. | supported | [E01](#e01), [E03](#e03), [E04](#e04), [E07](#e07) |
| gene | The most likely target is TOX3, the nearest protein-coding gene at 17.6 kb; this is proximity- and locus-literature-based, since there is no GTEx eQTL for this exact SNP in any tissue or breast mammary tissue. | weak | [E02](#e02), [E17](#e17), [E36](#e36), [E18a](#e18a), [E18b](#e18b) |
| cell_type | SPDEF is expressed at high levels and is ChIP-bound at the variant-containing element in MCF-7 breast cancer cells. | supported | [E07](#e07) |
| phenotype | If SPDEF represses this TOX3 element, loss of SPDEF binding on the alt allele could increase TOX3 activity and contribute to breast cancer risk at 16q12; the exact SNP has no GWAS Catalog or Open Targets record, so this is locus-level inference from the TOX3 breast cancer association. | weak | [E15](#e15), [E16](#e16), [E18a](#e18a), [E18b](#e18b), [E37](#e37) |

Predictions: Allele-specific SPDEF ChIP or CUT&RUN at this base shows higher SPDEF occupancy on the ref G allele than on the alt A allele in MCF-7 cells.; A G-vs-A enhancer reporter in MCF-7 cells shows stronger SPDEF-dependent activity on the ref allele.; SPDEF knockdown reduces the ref-allele-specific enhancer signal; if SPDEF represses TOX3, the alt allele associates with higher TOX3 expression.

Falsified if: Allele-specific SPDEF binding at this exact base is not reproducible.; The ref allele does not produce stronger SPDEF-dependent activity in MCF-7 cells.; SPDEF knockdown has no effect on the element or TOX3 expression.

### 2. H5_NULL: No TF-mediated allelic effect of rs56007086 (p = 0.42)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at the variant base.; Any observed enhancer or expression effect is due to a linked causal variant rather than rs56007086.; The SNP is a passenger or non-functional intronic variant near TOX3.

Falsified if: Allele-specific binding of a relevant TF at this exact base is demonstrated.; Allele-specific enhancer activity and TOX3 expression are reproducibly shown.; Fine-mapping and functional editing separate rs56007086 from linked variants.

### 3. H3_FOXA1: FOXA1 allele-specific binding at a weak site in the TOX3 enhancer (p = 0.07)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR16_9QTBS / dELS EH38E3180851 regulatory element; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is ChIP-bound over the variant in MCF-7 and highly expressed (E05), but its QBiC-SELEX evidence is only a weak site and the best model is CIS-BP-mapped FOXA2 (E24); the alt-favoring direction is therefore weak and the ChIP peak may reflect another site in the element. | weak | [E05](#e05), [E24](#e24) |
| element | The variant lies in the ENSR16_9QTBS enhancer and FOXA1 occupies the variant-containing element in MCF-7; the cCRE evidence is nearby rather than overlapping. | supported | [E01](#e01), [E03](#e03), [E04](#e04), [E05](#e05) |
| gene | TOX3 is the nearest protein-coding gene at 17.6 kb, but there is no GTEx eQTL for this exact SNP, so the variant-to-TOX3 link is proximity- and locus-literature-based. | weak | [E02](#e02), [E17](#e17), [E36](#e36), [E18a](#e18a), [E18b](#e18b) |
| cell_type | FOXA1 is highly expressed and ChIP-bound at this locus in MCF-7 breast cancer cells. | supported | [E05](#e05) |
| phenotype | FOXA1-dependent regulation of TOX3 could influence breast cancer risk at 16q12, but the exact SNP has no direct GWAS or Open Targets record and the TOX3 association is locus-level. | weak | [E15](#e15), [E16](#e16), [E18a](#e18a), [E18b](#e18b), [E37](#e37) |

Predictions: Allele-specific FOXA1 ChIP or CUT&RUN shows higher FOXA1 occupancy on the alt A allele at this base.; The alt allele increases FOXA1-dependent reporter activity in MCF-7 cells.; FOXA1 knockdown changes TOX3 expression or the enhancer signal.

Falsified if: FOXA1 ChIP signal at this base is not allele-specific.; The weak QBiC weak-site prediction is not confirmed by allele-specific FOXA1 binding.; FOXA1 knockdown has no effect on the element or TOX3.

### 4. H4_GATA3: GATA3 allele-specific binding at a weak site in the TOX3 enhancer (p = 0.05)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR16_9QTBS / dELS EH38E3180851 regulatory element; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is ChIP-bound over the variant in MCF-7 and very highly expressed (E06), but its QBiC-SELEX evidence is only a weak site and the best model is CIS-BP-mapped GATA2 (E23); the alt-favoring direction is therefore weak and the ChIP peak may reflect another site in the element. | weak | [E06](#e06), [E23](#e23) |
| element | The variant lies in the ENSR16_9QTBS enhancer and GATA3 occupies the variant-containing element in MCF-7, though the nearest cCRE is 38 bp away rather than overlapping. | supported | [E01](#e01), [E03](#e03), [E04](#e04), [E06](#e06) |
| gene | TOX3 is the nearest protein-coding gene at 17.6 kb; there is no GTEx eQTL for this exact SNP, so target assignment is proximity- and locus-literature-based. | weak | [E02](#e02), [E17](#e17), [E36](#e36), [E18a](#e18a), [E18b](#e18b) |
| cell_type | GATA3 is highly expressed and ChIP-bound at this locus in MCF-7 breast cancer cells. | supported | [E06](#e06) |
| phenotype | GATA3-dependent TOX3 regulation could contribute to breast cancer risk at 16q12, but the exact SNP has no direct GWAS or Open Targets record and the TOX3 association is locus-level. | weak | [E15](#e15), [E16](#e16), [E18a](#e18a), [E18b](#e18b), [E37](#e37) |

Predictions: Allele-specific GATA3 ChIP or CUT&RUN shows higher GATA3 occupancy on the alt A allele at this base.; The alt allele changes GATA3-dependent enhancer activity in MCF-7 cells.; GATA3 knockdown alters TOX3 expression or the enhancer signal.

Falsified if: GATA3 ChIP signal at this base is not allele-specific.; The weak QBiC weak-site prediction is not confirmed by allele-specific GATA3 binding.; GATA3 knockdown has no effect on the element or TOX3.

## Prediction matrix

| Test | Cost | Separates top two | H2_SPDEF | H5_NULL | H3_FOXA1 | H4_GATA3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific SPDEF ChIP-qPCR or CUT&RUN at rs56007086 in MCF-7 cells, comparing ref G and alt A. | low | yes | Ref G allele shows higher SPDEF occupancy than alt A. | No allele-specific SPDEF occupancy at this base. | No allele-specific SPDEF occupancy; FOXA1, not SPDEF, is the candidate. | No allele-specific SPDEF occupancy; GATA3, not SPDEF, is the candidate. |
| Allele-specific FOXA1 ChIP-qPCR or CUT&RUN at rs56007086 in MCF-7 cells. | medium | no | No allele-specific FOXA1 occupancy. | No allele-specific FOXA1 occupancy. | Alt A allele shows higher FOXA1 occupancy than ref G. | No allele-specific FOXA1 occupancy. |
| Allele-specific GATA3 ChIP-qPCR or CUT&RUN at rs56007086 in MCF-7 cells. | medium | no | No allele-specific GATA3 occupancy. | No allele-specific GATA3 occupancy. | No allele-specific GATA3 occupancy. | Alt A allele shows higher GATA3 occupancy than ref G. |
| G-vs-A enhancer reporter assay in MCF-7 cells with and without SPDEF knockdown. | medium | yes | Ref allele gives stronger SPDEF-dependent enhancer activity; SPDEF knockdown reduces the allele difference. | No reproducible allele-specific enhancer activity. | Alt allele gives stronger FOXA1-dependent activity; SPDEF knockdown has no effect. | Alt allele gives stronger GATA3-dependent activity; SPDEF knockdown has no effect. |
| TOX3 allele-specific expression or eQTL in breast/mammary tissue or MCF-7 cells. | high | yes | If SPDEF represses TOX3, alt A associates with higher TOX3 expression. | No allele-specific TOX3 expression effect for rs56007086. | Alt A associates with FOXA1-dependent TOX3 expression change. | Alt A associates with GATA3-dependent TOX3 expression change. |

## Next experiment

Allele-specific SPDEF ChIP-qPCR or CUT&RUN at rs56007086 in MCF-7 cells, comparing ref G and alt A, is the cheapest experiment that separates the top two chains H2_SPDEF and H5_NULL.

## Investigate calls

- qbic_tf_detail({"tf": "TCF7L2"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- gene_disease({"gene": "TOX3"})

## Flags

- literature_fallback: no hits for 'rs56007086 AND TOX3 AND "breast cancer"'; dropped the rsID

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

> Key examples include promoter mutations [e.g., rs2279744 (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs4784227 (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41871294 (https://europepmc.org/article/MED/41871294; retrieved 2026-10-26T02:25:47+00:00)

> Differences in panel performance influenced association signals, including breast cancer candidate loci such as FGFR2, TOX3, and ESR1.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:52565398:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000019), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 79 occupied (16 with a strong site), 5 of 137 with unknown occupancy. Left out: 49 TFs assayed in the matching biosample and 425 assayed only elsewhere, none with a peak here; 20 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer (a CIS-BP-mapped model of TCF7L1), z 12.52, effect 0.745: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.89 TPM, rank 642 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWT. Best model's site strength: ref 57.0th, alt 97.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SPDEF (Ets, 1 model; QBiC-SELEX coverage: own model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (its own model), z -7.0, effect -0.244: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 72.51 TPM, rank 40 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR042GSX. Best model's site strength: ref 99.7th, alt 95.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model PPARD_eDBD_TGTCTT40NTTC_KR_yin2017_0_2_7mer (a CIS-BP-mapped model of PPARD), z 10.89, effect 0.436: alt allele binds more (|z| above the gate), but between weak k-mers. 38.14 TPM, rank 103 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000BUY. Best model's site strength: ref 77.8th, alt 91.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (a CIS-BP-mapped model of GATA2), z 8.32, effect 0.197: alt allele binds more (|z| above the gate), but between weak k-mers. 346.04 TPM, rank 5 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWV. Best model's site strength: ref 37.1th, alt 35.5th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXA1 (Forkhead, 4 models; QBiC-SELEX coverage: own model): best model FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer (a CIS-BP-mapped model of FOXA2), z 6.27, effect 0.131: alt allele binds more (|z| above the gate), but between weak k-mers. 88.38 TPM, rank 28 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR126YEB. Best model's site strength: ref 90.2th, alt 81.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPB (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (its own model), z -1.64, effect -0.203: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 24.33 TPM, rank 169 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000BSR. Best model's site strength: ref 76.8th, alt 75.0th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NFIA (SMAD, 4 models; QBiC-SELEX coverage: own model): best model NFIX_FL_TTGAGC40NGTC_KAE_yin2017_1_3_7mer (a CIS-BP-mapped model of NFIX), z 15.29, effect 0.957: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.35 TPM, rank 931 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR226QQM. Best model's site strength: ref 85.7th, alt 97.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PITX1 (Homeodomain, 11 models; QBiC-SELEX coverage: own model): best model PITX3_eDBD_TCACAT40NATG_KR_yin2017_0_3_7mer (a CIS-BP-mapped model of PITX3), z 12.33, effect 0.611: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.1 TPM, rank 702 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR374MAS. Best model's site strength: ref 99.3th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF772 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF772_FL_GC40NCTTGTA_YWSA_jolma2025_0_3_7mer (its own model), z 9.58, effect 0.34: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.6 TPM, rank 806 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR248WAU. Best model's site strength: ref 98.1th, alt 99.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> AHDC1 (AT hook, 1 model; QBiC-SELEX coverage: own model): best model AHDC1_FL_GG40NTAGTTT_YWO_jolma2025_0_4_7mer (its own model), z 9.17, effect 0.313: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 5.44 TPM, rank 609 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR168AUX. Best model's site strength: ref 98.0th, alt 99.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z -47.67, effect -0.77: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.33 TPM, rank 516 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.8th, alt 86.8th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SLC2A4RG (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model SLC2A4RG_FL_CT40NGCGCTA_YWPA_jolma2025_0_3_7mer (its own model), z -45.42, effect -4.513: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 148.81 TPM, rank 15 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.9th, alt 93.5th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MTERF3 (mTERF, 1 model; QBiC-SELEX coverage: own model): best model MTERF3_FL_GG40NTAGTTT_YWJA_jolma2025_0_3_7mer (its own model), z 24.43, effect 0.234: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 19.0 TPM, rank 217 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 71.0th, alt 83.4th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PBX4 (Homeodomain, 1 model; QBiC-SELEX coverage: mapped models only): best model PBX1_eDBD_TAAGTC40NCGT_KR_yin2017_0_4_7mer (a CIS-BP-mapped model of PBX1), z 18.55, effect 0.733: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.15 TPM, rank 766 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 75.2th, alt 97.8th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SOX12 (HMG/Sox, 18 models; QBiC-SELEX coverage: own model): best model SOX18_eDBD_TCACGC40NACT_KP_yin2017_0_4_7mer (a CIS-BP-mapped model of SOX18), z 17.9, effect 0.672: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.17 TPM, rank 439 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 74.4th, alt 82.6th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr16:52565398:G>A","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":0.492,"z":5.25,"p":1.5e-07,"rank_abs_z":"446/997","passed_gate":true,"site_strength":{"ref_percentile":82.3,"alt_percentile":96.7,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":0.531,"z":11.75,"p":6.7e-32,"rank_abs_z":"84/997","passed_gate":true,"site_strength":{"ref_percentile":90.0,"alt_percentile":80.7,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":0.745,"z":12.52,"p":6e-36,"rank_abs_z":"70/997","passed_gate":true,"site_strength":{"ref_percentile":57.0,"alt_percentile":97.8,"k":7}}]}

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565398_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:27:56+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565398_G_A_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e37"></a>**E37** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:34:32+00:00)

> Open Targets: TOX3 and breast cancer (MONDO_0007254), overall score 0.58; by evidence type: genetic_association 0.91, literature 0.89
