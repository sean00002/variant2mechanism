# rs56007086 and Breast cancer (16q12)

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 167 s.

Variant `chr16:52565398:G>A` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. C4: Null: no TF-mediated allelic effect of this variant; the signal is due to a linked causal variant, a passenger event, or no allelic effect (p = 0.43)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-specific TF ChIP/CUT&RUN and reporter/MPRA at this exact base will show no reproducible allelic effect after controlling for linked variants.; Base editing ref G to alt A alone will not change TOX3 expression or a breast cancer phenotype in an isogenic system.; Any breast cancer association at this locus will be explained by a nearby linked variant rather than chr16:52565398:G>A itself.

Falsified if: A robust allele-specific TF binding or enhancer-activity difference is demonstrated for this exact base in breast cancer cells.; Editing ref G to alt A alone changes TOX3 expression or a breast cancer phenotype in an isogenic system.; Fine-mapping shows this variant is the causal variant independently of linked signals.

### 2. C1: FOXA1 binds the alt A allele more strongly at a TOX3 enhancer and increases TOX3 in breast cancer cells (p = 0.38)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element enhancer; gene TOX3; cell type MCF7 breast cancer cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is the candidate TF because it has MCF-7 ChIP-seq peaks containing this base (E05) and is highly expressed in MCF7 (E05); E04 lists many co-bound TFs, so FOXA1 is selected as a strongly expressed breast-lineage factor with occupancy, not because an allelic assay exists. The alt A allele is predicted to bind FOXA1 more strongly, but no QBiC-SELEX model or allele-specific ChIP/reporter/MPRA for this exact base is supplied (E19), so ref/alt direction is only a motif-based hypothesis. | weak | [E04](#e04), [E05](#e05), [E19](#e19) |
| element | The variant lies in an Ensembl-annotated enhancer (ENSR16_9QTBS) and in dense MCF-7 TF-bound chromatin near a dELS, but no cCRE directly overlaps the base and the nearest dELS is 38 bp away. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | TOX3 is the nearest protein-coding gene at 17.6 kb and is a breast cancer-associated locus (E21), but the exact SNP has no significant GTEx v8 eQTL in the supplied data (E17, E20), and no contact or perturbation evidence directly links this base to TOX3. | weak | [E02](#e02), [E17](#e17), [E20](#e20), [E21](#e21) |
| cell_type | MCF-7 is the relevant breast cancer cell context because FOXA1 is bound over the variant in MCF-7 and is highly expressed there (E05), with matching active MCF-7 TF ChIP context at the element (E04). | supported | [E05](#e05), [E04](#e04) |
| phenotype | Breast cancer is the phenotype at the TOX3 locus: TOX3 has Open Targets breast cancer evidence (E21) and literature support (E18a, E18b), but the exact variant has no GWAS Catalog or Open Targets record in the supplied evidence (E15, E16), so this is locus-level rather than exact-variant phenotype evidence. | weak | [E21](#e21), [E15](#e15), [E16](#e16), [E18a](#e18a), [E18b](#e18b) |

Predictions: Allele-specific FOXA1 ChIP/CUT&RUN or reporter/MPRA at the exact base will show stronger FOXA1 occupancy/activity on alt A than ref G.; Base editing ref G to alt A in MCF-7 or isogenic breast cancer cells will increase TOX3 expression or enhancer activity.; The alt A allele will track with increased TOX3 expression in breast tissue or breast cancer models if this element is active there.

Falsified if: Allele-specific FOXA1 ChIP/CUT&RUN or reporter/MPRA shows no difference between ref G and alt A, or shows ref G binds FOXA1 more strongly.; Base editing this exact base in an isogenic system does not change TOX3 expression or enhancer activity.; Fine-mapping or allele-specific assays show the disease signal tracks with a different linked variant independently of FOXA1 binding.

### 3. C2: GATA3 binds the ref G allele more strongly at the same enhancer and regulates TOX3 (p = 0.12)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element enhancer; gene TOX3; cell type MCF7 breast cancer cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is the candidate TF because it has MCF-7 ChIP-seq peaks containing this base and is very highly expressed in MCF7 (E06); among the many co-bound TFs in E04 it is selected by breast-lineage identity and extremely high expression. The ref G allele is predicted to bind GATA3 more strongly, but no QBiC-SELEX model or allele-specific ChIP/reporter/MPRA for this exact base is supplied (E19), so ref/alt direction is only a motif-based hypothesis. | weak | [E04](#e04), [E06](#e06), [E19](#e19) |
| element | The variant lies in an Ensembl-annotated enhancer (ENSR16_9QTBS) and in active MCF-7 TF-bound chromatin near a dELS, though no cCRE directly overlaps the base. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | TOX3 is the nearest protein-coding gene at 17.6 kb and is a breast cancer-associated locus (E21), but the exact SNP has no significant GTEx v8 eQTL in the supplied data (E17, E20), and no contact or perturbation evidence directly links this base to TOX3. | weak | [E02](#e02), [E17](#e17), [E20](#e20), [E21](#e21) |
| cell_type | MCF-7 is the relevant cell context because GATA3 is bound over the variant in MCF-7 and is highly expressed there (E06), with matching active MCF-7 TF ChIP context at the element (E04). | supported | [E06](#e06), [E04](#e04) |
| phenotype | Breast cancer is the phenotype at the TOX3 locus (E21, E18a, E18b), but the exact variant has no GWAS Catalog or Open Targets record in the supplied evidence (E15, E16), so the phenotype link is locus-level and indirect. | weak | [E21](#e21), [E15](#e15), [E16](#e16), [E18a](#e18a), [E18b](#e18b) |

Predictions: Allele-specific GATA3 ChIP/CUT&RUN or reporter/MPRA at the exact base will show stronger GATA3 occupancy/activity on ref G than alt A.; GATA3 perturbation will reduce the ref G-dependent enhancer activity or TOX3 expression in breast cancer cells.; The ref G allele will correlate with GATA3-dependent TOX3 expression in breast tissue or breast cancer models.

Falsified if: Allele-specific GATA3 ChIP/CUT&RUN or reporter/MPRA shows no allele difference or stronger GATA3 binding on alt A.; GATA3 perturbation does not affect enhancer activity or TOX3 expression in breast cancer cells.; Fine-mapping shows the signal is independent of GATA3 binding at this base.

### 4. C3: SPDEF binds the ref G allele more strongly at the element and contributes to TOX3 regulation (p = 0.07)

TF SPDEF (QBiC-SELEX coverage own_model), ref allele binds more; element enhancer; gene TOX3; cell type MCF7 breast cancer cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SPDEF is a weak candidate TF: it has one MCF-7 ChIP-seq peak containing this base and is expressed in MCF7 (E07), but it is only one of many co-bound TFs in E04. The ref G allele is predicted to bind SPDEF more strongly, but no QBiC-SELEX model or allele-specific ChIP/reporter/MPRA for this exact base is supplied (E19), so ref/alt direction is only a motif-based hypothesis. | weak | [E04](#e04), [E07](#e07), [E19](#e19) |
| element | The variant lies in an Ensembl-annotated enhancer (ENSR16_9QTBS) and in active MCF-7 TF-bound chromatin near a dELS, though no cCRE directly overlaps the base. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | TOX3 is the nearest protein-coding gene at 17.6 kb and is a breast cancer-associated locus (E21), but the exact SNP has no significant GTEx v8 eQTL in the supplied data (E17, E20), and no contact or perturbation evidence directly links this base to TOX3. | weak | [E02](#e02), [E17](#e17), [E20](#e20), [E21](#e21) |
| cell_type | MCF-7 is the relevant cell context because SPDEF is bound over the variant in MCF-7 and expressed there (E07), with matching active MCF-7 TF ChIP context at the element (E04). | supported | [E07](#e07), [E04](#e04) |
| phenotype | Breast cancer is the phenotype at the TOX3 locus (E21, E18a, E18b), but the exact variant has no GWAS Catalog or Open Targets record in the supplied evidence (E15, E16), so the phenotype link is locus-level and indirect. | weak | [E21](#e21), [E15](#e15), [E16](#e16), [E18a](#e18a), [E18b](#e18b) |

Predictions: Allele-specific SPDEF ChIP/CUT&RUN or reporter/MPRA at the exact base will show stronger SPDEF occupancy/activity on ref G than alt A.; SPDEF perturbation will alter enhancer activity or TOX3 expression in breast cancer cells.; SPDEF binding at this element will be breast-cancer-cell-context dependent.

Falsified if: Allele-specific SPDEF ChIP/CUT&RUN or reporter/MPRA shows no difference or stronger SPDEF binding on alt A.; SPDEF loss does not affect the element or TOX3 expression in breast cancer cells.; The variant is not in an active enhancer in MCF-7.

## Prediction matrix

| Test | Cost | Separates top two | C4 | C1 | C2 | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific FOXA1 ChIP-qPCR/CUT&RUN or FOXA1 reporter/MPRA at the exact base in MCF-7 or isogenic cells | low | yes | C4 predicts no reproducible allele-specific FOXA1 binding/activity at this exact base after controlling for linked variants. | C1 predicts stronger FOXA1 occupancy/activity on alt A than ref G at the exact base. | C2 predicts no reproducible FOXA1 allelic effect at this base. | C3 predicts no reproducible FOXA1 allelic effect at this base. |
| Allele-specific GATA3 ChIP-qPCR/CUT&RUN or GATA3 reporter/MPRA at the exact base | low | no | C4 predicts no reproducible allele-specific GATA3 binding/activity. | C1 predicts no reproducible GATA3 allelic effect at this base. | C2 predicts stronger GATA3 occupancy/activity on ref G than alt A. | C3 predicts no reproducible GATA3 allelic effect at this base. |
| Allele-specific SPDEF ChIP-qPCR/CUT&RUN or SPDEF reporter/MPRA at the exact base | low | no | C4 predicts no reproducible allele-specific SPDEF binding/activity. | C1 predicts no reproducible SPDEF allelic effect at this base. | C2 predicts no reproducible SPDEF allelic effect at this base. | C3 predicts stronger SPDEF occupancy/activity on ref G than alt A. |
| CRISPR base edit ref G to alt A in MCF-7 or isogenic breast cancer cells, then measure TOX3 expression and enhancer activity | high | yes | C4 predicts no change in TOX3 expression or enhancer activity from editing this base alone. | C1 predicts alt A increases TOX3 expression/enhancer activity relative to ref G. | C2 predicts a ref G-dependent GATA3 effect on TOX3 expression/enhancer activity, lost or reduced on alt A. | C3 predicts a ref G-dependent SPDEF effect on TOX3 expression/enhancer activity, lost or reduced on alt A. |
| Breast mammary tissue eQTL or allele-specific expression for the exact SNP | low | yes | C4 predicts no significant exact-SNP TOX3 eQTL in breast tissue, or the signal is explained by a linked variant. | C1 predicts the alt A allele tracks with increased TOX3 expression in breast tissue. | C2 predicts the ref G allele tracks with GATA3-dependent TOX3 expression. | C3 predicts the ref G allele tracks with SPDEF-dependent TOX3 expression. |

## Next experiment

Allele-specific FOXA1 ChIP-qPCR (or FOXA1 CUT&RUN with SNP discrimination) at chr16:52565398 in MCF-7 or an isogenic cell line, comparing alt A vs ref G occupancy at the exact base.

## Investigate calls

- literature_search({"query": "chr16:52565398 OR TOX3 enhancer FOXA1 GATA3 SPDEF allele-specific breast cancer"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- gene_disease({"gene": "TOX3"})

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

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr16%3A52565398%20OR%20TOX3%20enhancer%20FOXA1%20GATA3%20SPDEF%20allele-specific%20breast%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:32:20+00:00)

> Europe PMC: 5 hits for 'chr16:52565398 OR TOX3 enhancer FOXA1 GATA3 SPDEF allele-specific breast cancer'; top 5 with PMIDs:
> PMID 30116257 (2018): Elucidating the Underlying Functional Mechanisms of Breast Cancer Susceptibility Through Post-GWAS Analyses.
> PMID 35091282 (2022): Distribution of copy number variations and rearrangement endpoints in human cancers with a review of literature.
> PMID 31592543 (2019): 17th International Congress of Immunology, 19-23 October 2019, Beijing, China. [no abstract]
> PMID 35181845 (2022): SRI 2022: Scientific Abstracts. [no abstract]
> PMID 32030671 (2020): Vision 20/20 for the Second Leap of Reproductive Sciences. [no abstract]

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 30116257 (https://europepmc.org/article/MED/30116257; retrieved 2026-10-26T20:32:20+00:00)

> Despite these achievements, however, understanding of each variant's underlying mechanism and how these SNPs predispose women to breast cancer remains limited and represents a major challenge in the field, particularly since the vast majority of the GWAS-identified SNPs are located in non-coding regions of the genome and are merely tags for the causal variants.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 30116257 (https://europepmc.org/article/MED/30116257; retrieved 2026-10-26T20:32:20+00:00)

> In recent years, fine-scale mapping studies followed by functional evaluation of putative causal variants have begun to elucidate the biological function of several GWAS-identified variants.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565398_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:27:56+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565398_G_A_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e21"></a>**E21** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:34:32+00:00)

> Open Targets: TOX3 and breast cancer (MONDO_0007254), overall score 0.58; by evidence type: genetic_association 0.91, literature 0.89
