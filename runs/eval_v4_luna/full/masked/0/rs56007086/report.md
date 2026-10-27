# rs56007086 and Breast cancer (16q12)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 13 model calls; 246 s.

Variant `chr16:52565398:G>A` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z 12.52); SPDEF (bound here, z -7.0); NR2F2 (bound here, z 10.89, weak site); GATA3 (bound here, z 8.32, weak site); FOXA1 (bound here, z 6.27, weak site); CEBPB (bound here, z -1.64, no clear allelic change, weak site); NFIA (bound elsewhere, z 15.29); PITX1 (bound elsewhere, z 12.33); ZNF772 (bound elsewhere, z 9.58); AHDC1 (bound elsewhere, z 9.17). Occupancy unknown: ETV3 (z -47.67); SLC2A4RG (z -45.42); MTERF3 (z 24.43); PBX4 (z 18.55); SOX12 (z 17.9). Diagnostic, not shown to the model: 569 of 997 models pass Bonferroni.

## Ranked chains

### 1. H5: Null: no TF-mediated effect of this variant (p = 0.57)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not produce a reproducible TF-dependent regulatory effect attributable to this base.; Any disease association, if established, could arise from linkage to another causal variant or a mechanism other than TF-mediated action at this site.

Falsified if: Editing the variant produces a reproducible allele-dependent regulatory effect that is dependent on a specific TF in a relevant breast-cell context.

### 2. H2: SPDEF binding loss; downstream regulatory and disease consequences unresolved (p = 0.29)

TF SPDEF (QBiC-SELEX coverage own_model), ref allele binds more; element A functional regulatory element at the variant is not established; the nearby dELS may be distinct.; gene None; cell type MCF-7 cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SPDEF has an MCF-7 ChIP peak over the variant, and its own QBiC-SELEX model predicts stronger binding to G than A at a strong site; this is in-vitro evidence for an allelic binding difference, not proof of altered regulatory activity. | supported | [E07](#e07), [E21](#e21) |
| element | A regulatory feature is annotated at the site, but no ENCODE cCRE overlaps the variant and the nearby dELS is not established as the same element. | supported | [E01](#e01), [E03](#e03) |
| gene | No target gene is established. Literature raises a possible FOXA1-related TOX3 regulatory route at the locus, but does not connect this variant or SPDEF to TOX3 regulation. | weak | [E02](#e02), [E18a](#e18a), [E18b](#e18b), [E36](#e36), [E38](#e38), [E41a](#e41a), [E41b](#e41b) |
| cell_type | SPDEF is expressed in MCF-7 and has a ChIP-seq peak over the variant in that biosample. | supported | [E07](#e07), [E21](#e21) |
| phenotype | SPDEF has weak gene-level breast-cancer evidence, but no variant-to-gene or SPDEF-mediated variant-to-disease effect is established; TOX3 is not selectively required in MCF-7 in the supplied dependency data. | supported | [E15](#e15), [E16](#e16), [E17](#e17), [E35](#e35), [E37](#e37), [E42](#e42), [E43](#e43) |

Predictions: An allele-specific SPDEF binding assay should favor G over A.; If this chain is correct, a variant-dependent regulatory effect should respond to SPDEF perturbation; the target gene and direction of expression change remain unknown.

Falsified if: A sensitive assay finds no G-over-A SPDEF binding difference.; There is no reproducible variant-dependent regulatory effect, or a detected effect is unchanged by SPDEF perturbation.

### 3. H3: Possible FOXA1-associated allelic effect at the TOX3 locus; variant-specific link unresolved (p = 0.08)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element A functional regulatory element at the variant is not established; the nearby dELS may be distinct.; gene TOX3; cell type MCF-7 cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies the variant in MCF-7. QBiC-SELEX has no FOXA1-specific model here; a mapped FOXA2 model predicts a small A-binding gain at a weak site, so it is only indirect evidence for FOXA1-specific allelic binding. Locus literature proposes that SNPs may alter FOXA1 binding, but does not securely identify this exact variant. | weak | [E05](#e05), [E24](#e24), [E41a](#e41a), [E41b](#e41b) |
| element | A regulatory feature is annotated at the site, but no ENCODE cCRE overlaps the variant; the nearby dELS is not shown to be the element described in the locus-level literature. | supported | [E01](#e01), [E03](#e03), [E41a](#e41a), [E41b](#e41b) |
| gene | TOX3 is a plausible locus-level candidate, and literature suggests FOXA1-related regulation of TOX3, but regulation of TOX3 by this exact variant is unproven. | weak | [E02](#e02), [E18a](#e18a), [E18b](#e18b), [E36](#e36), [E41a](#e41a), [E41b](#e41b) |
| cell_type | FOXA1 is highly expressed in MCF-7 and has a ChIP-seq peak over the variant in that biosample. | supported | [E05](#e05), [E24](#e24) |
| phenotype | TOX3 has gene-level breast-cancer context, but no supplied result establishes a functional effect of this variant or a FOXA1-mediated disease effect. | supported | [E15](#e15), [E16](#e16), [E17](#e17), [E18a](#e18a), [E18b](#e18b), [E35](#e35), [E36](#e36), [E37](#e37), [E38](#e38), [E41a](#e41a), [E41b](#e41b) |

Predictions: An allele-specific FOXA1 binding assay may favor A, but this is uncertain because the available QBiC-SELEX result is from a related TF model at a weak site.; If this route is correct, a variant-dependent regulatory effect should respond to FOXA1 perturbation and may alter TOX3 expression; the expression direction is not established.

Falsified if: A sensitive assay finds no A-over-G FOXA1 binding difference.; There is no reproducible variant-dependent regulatory effect, or a detected effect is unchanged by FOXA1 perturbation and does not affect TOX3.

### 4. H1: Possible TCF7L2-associated binding gain; regulatory and disease consequences unresolved (p = 0.06)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element A functional regulatory element at the variant is not established; the nearby dELS may be distinct.; gene None; cell type MCF-7 cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 has an MCF-7 ChIP peak over the variant. QBiC-SELEX models mapped from related factors predict stronger A binding, but there is no TCF7L2-specific model and the models differ in site-strength predictions; this is indirect, uncertain evidence for a TCF7L2-specific allelic effect. | weak | [E10](#e10), [E20](#e20), [E39](#e39) |
| element | A regulatory feature is annotated at the site, but no ENCODE cCRE overlaps the variant and the nearby dELS is not shown to be the same element. | supported | [E01](#e01), [E03](#e03) |
| gene | No target gene is established; TOX3 is nearby and has breast-cancer context, but this variant is not shown to regulate it. | weak | [E02](#e02), [E18a](#e18a), [E18b](#e18b), [E36](#e36), [E38](#e38) |
| cell_type | TCF7L2 is expressed in MCF-7 and has a ChIP peak over the variant in that biosample. | supported | [E10](#e10), [E20](#e20) |
| phenotype | A TCF7L2-mediated effect of this variant on breast cancer is not established. | supported | [E15](#e15), [E16](#e16), [E17](#e17), [E35](#e35), [E37](#e37), [E38](#e38) |

Predictions: An allele-specific assay may show greater TCF7L2 binding to A than G, but this is uncertain because the QBiC-SELEX models are from related factors.; A variant-dependent regulatory effect, if present, should respond to TCF7L2 perturbation; the target gene and expression direction are not specified.

Falsified if: A sensitive assay finds no A-over-G TCF7L2 binding difference.; There is no reproducible variant-dependent regulatory effect, or a detected effect is unchanged by TCF7L2 perturbation.

## Prediction matrix

| Test | Cost | Separates top two | H5 | H2 | H3 | H1 |
| --- | --- | --- | --- | --- | --- | --- |
| Dual-allele reporter assay using a sequence spanning the variant in MCF-7, with SPDEF perturbation | medium | yes | No reproducible allele-dependent, SPDEF-dependent reporter effect is expected. | The G and A constructs should differ in reporter activity, and the difference should be reduced or altered by SPDEF perturbation; the direction of reporter activity is not predicted from binding alone. | No SPDEF-specific reporter effect is expected; this chain instead predicts a possible FOXA1-dependent effect, which this test does not directly resolve. | No SPDEF-specific reporter effect is expected; this chain instead predicts a possible TCF7L2-dependent effect, which this test does not directly resolve. |
| Allele-specific SPDEF occupancy assay at the endogenous locus in MCF-7 | low | no | A binding difference could occur without a TF-mediated regulatory effect, so occupancy alone need not distinguish this chain. | SPDEF occupancy should favor G over A. | No specific SPDEF allelic preference is predicted by this chain. | No specific SPDEF allelic preference is predicted by this chain. |

## Next experiment

Run the medium-cost dual-allele reporter assay in MCF-7 with and without SPDEF perturbation. It tests whether the predicted SPDEF binding difference is accompanied by a SPDEF-dependent regulatory effect, distinguishing H2 from the null more directly than an occupancy assay alone.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- eqtl_lookup({"tissue": "Breast Mammary Tissue"}) for H1.gene, ran as [E35](#e35). Expected: If this variant is a significant breast-tissue eQTL and the effect implicates TOX3, the variant-to-expression link becomes better supported and TOX3 rises as a target; if there is no signal, the current weak grade remains.
- gene_disease({"gene": "TOX3"}) for H1.gene, ran as [E36](#e36). Expected: If Open Targets reports strong breast-cancer evidence for TOX3, that strengthens its disease relevance but does not establish that this variant regulates it; weak or absent evidence leaves the target claim weak.
- literature_search({"query": "chr16:52565398 TOX3 breast cancer variant enhancer"}) for H1.phenotype, ran as [E37](#e37). Expected: If the literature identifies this specific variant and reports an association or functional effect in breast cancer, the phenotype link could gain support; if results are only broad TOX3 context or unrelated variants, it remains unsupported.

- Result of eqtl_lookup({"tissue":"Breast Mammary Tissue"}): E35 reports 0 significant GTEx v8 eQTLs in Breast Mammary Tissue for this variant. (as expected: yes)
- Result of gene_disease({"gene":"TOX3"}): E36 reports a TOX3–breast cancer overall score of 0.58, with genetic_association 0.91 and literature 0.89; this is gene-level evidence, not evidence that this variant regulates TOX3. (as expected: yes)
- Result of literature_search({"query":"chr16:52565398 TOX3 breast cancer variant enhancer"}): E37 reports 0 literature hits for the specific variant, TOX3, breast cancer, and enhancer query. (as expected: yes)

Chains after revision: null 0.45; SPDEF 0.30; TCF7L2 0.12; GATA3 0.07; FOXA1 0.06. Link grades changed: H1.gene: weak → missing, H2.gene: weak → missing, H3.gene: weak → missing, H4.gene: weak → missing.

### Round 2

- literature_search({"query": "chr16:52565398 TOX3 enhancer breast cancer MCF-7 variant functional regulation"}) for H1.gene; also H2.gene, H3.gene, and H4.gene, ran as [E38](#e38). Expected: If the search finds functional evidence connecting this exact variant or its element to TOX3, the gene links become supported and the corresponding chains rise; if not, the gene links remain missing.
- qbic_tf_detail({"tf": "TCF7L2"}) for H1.binding, ran as [E39](#e39). Expected: If the detail shows a TCF7L2-specific model or additional concordant evidence for stronger A binding, H1.binding strengthens; if coverage is only the already-reported TCF7L1-mapped model, the indirect interpretation remains weak.
- qbic_tf_detail({"tf": "GATA3"}) for H3.binding, ran as [E40](#e40). Expected: If the detail reveals a GATA3-specific model with a detectable, concordant A-favoring effect, H3.binding strengthens; if it confirms only mapped models or weak-site predictions, the indirect binding evidence remains weak.

- Result of literature_search("chr16:52565398 TOX3 enhancer breast cancer MCF-7 variant functional regulation"): E38 reports zero hits for the exact-variant/TOX3 functional-regulation query; no variant-to-TOX3 evidence was found. (as expected: yes)
- Result of qbic_tf_detail({"tf": "TCF7L2"}): E39 reports mapped models only, including TCF7L1-, TCF7-, and LEF1-mapped models. Several predict stronger A binding, but none is TCF7L2-specific, and their site-strength patterns are not fully concordant. (as expected: yes)
- Result of qbic_tf_detail({"tf": "GATA3"}): E40 reports no detectable effect from the GATA3-specific model. The detectable A-favoring result is from a GATA2-mapped model, with weak site-strength percentiles. (as expected: yes)

Chains after revision: null 0.58; SPDEF 0.32; TCF7L2 0.10. Link grades changed: H1.element: weak → supported, H1.gene: missing → supported, H1.phenotype: missing → supported, H2.element: weak → supported, H2.gene: missing → supported, H2.phenotype: missing → supported, H3.binding: weak → absent, H3.cell_type: supported → absent, H3.element: weak → absent, H3.gene: missing → absent, H3.phenotype: missing → absent, H4.binding: weak → absent, H4.cell_type: supported → absent, H4.element: weak → absent, H4.gene: missing → absent, H4.phenotype: missing → absent.

### Round 3

- literature_search({"query": "TOX3 locus enhancer CASC16 breast cancer regulatory element"}) for H2.gene, ran as [E41](#e41). Expected: If literature identifies a regulatory element at this locus that contacts or regulates TOX3, H2.gene and possibly H2.element gain support; if it provides only gene-level associations, those links remain unresolved.
- gene_dependency({"gene": "TOX3"}) for H2.phenotype, ran as [E42](#e42). Expected: If TOX3 is selectively required in breast-cancer models including MCF7, TOX3-mediated disease relevance becomes more plausible, but this would not establish that the variant regulates TOX3. If it is not required, that provides little support for this route.
- gene_disease({"gene": "SPDEF"}) for H2.phenotype, ran as [E43](#e43). Expected: If Open Targets reports breast-cancer evidence for SPDEF, H2 gains gene-level disease context but not a variant-to-disease link; absent evidence leaves the phenotype link unresolved.

- Result of literature_search: TOX3 locus enhancer CASC16 breast cancer regulatory element: E41 reports literature proposing that CASC16-locus SNPs may alter FOXA1 binding and thereby affect TOX3 expression. It does not establish that this exact variant lies in a functional element or regulates TOX3. (as expected: yes)
- Result of gene_dependency: TOX3: E42 reports a CRISPR gene-effect score of 0.11 in MCF-7, with 0% of breast-lineage and all tested lines classified as TOX3-dependent. (as expected: yes)
- Result of gene_disease: SPDEF: E43 reports a low overall Open Targets score of 0.11 for SPDEF and breast cancer, with the evidence attributed to literature. (as expected: yes)

Chains after revision: null 0.57; SPDEF 0.29; FOXA1 0.08; TCF7L2 0.06. Link grades changed: H1.gene: supported → weak, H2.gene: supported → weak, H3.binding: absent → weak, H3.cell_type: absent → supported, H3.element: absent → supported, H3.gene: absent → weak, H3.phenotype: absent → supported.

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

<a id="e35"></a>**E35** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565398_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:27:56+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565398_G_A_b38 in tissues matching 'Breast Mammary Tissue'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e36"></a>**E36** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:34:32+00:00)

> Open Targets: TOX3 and breast cancer (MONDO_0007254), overall score 0.58; by evidence type: genetic_association 0.91, literature 0.89

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr16%3A52565398%20TOX3%20breast%20cancer%20variant%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:35:01+00:00)

> Europe PMC: 0 hits for 'chr16:52565398 TOX3 breast cancer variant enhancer'; top 0 with PMIDs:

<a id="e38"></a>**E38** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr16%3A52565398%20TOX3%20enhancer%20breast%20cancer%20MCF-7%20variant%20functional%20regulation&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:18:53+00:00)

> Europe PMC: 0 hits for 'chr16:52565398 TOX3 enhancer breast cancer MCF-7 variant functional regulation'; top 0 with PMIDs:

<a id="e39"></a>**E39** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr16:52565398:G>A","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":0.492,"z":5.25,"p":1.5e-07,"rank_abs_z":"446/997","passed_gate":true,"site_strength":{"ref_percentile":82.3,"alt_percentile":96.7,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":0.531,"z":11.75,"p":6.7e-32,"rank_abs_z":"84/997","passed_gate":true,"site_strength":{"ref_percentile":90.0,"alt_percentile":80.7,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":0.745,"z":12.52,"p":6e-36,"rank_abs_z":"70/997","passed_gate":true,"site_strength":{"ref_percentile":57.0,"alt_percentile":97.8,"k":7}}]}

<a id="e40"></a>**E40** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GATA3","symbol":"GATA3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565398:G>A","gate_p":5.02e-05,"models":[{"model":"GATA3_NA_TGTCGT20NGA_ESAC_yang2017_0_4_7mer","mapping":"own","group":"G010 GATA, 6 models","quality":0.858,"effect":-0.004,"z":-0.06,"p":0.95,"rank_abs_z":"993/997","passed_gate":false,"site_strength":{"ref_percentile":87.4,"alt_percentile":87.8,"k":7}},{"model":"GATA1_eDBD_TTTAGA40NGGC_KN_yin2017_0_4_7mer","mapping":"CIS-BP (GATA1)","group":"G010 GATA, 6 models","quality":0.626,"effect":0.069,"z":0.43,"p":0.67,"rank_abs_z":"941/997","passed_gate":false,"site_strength":{"ref_percentile":81.3,"alt_percentile":71.0,"k":7}},{"model":"GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer","mapping":"CIS-BP (GATA2)","group":"G010 GATA, 6 models","quality":0.874,"effect":0.197,"z":8.32,"p":9.2e-17,"rank_abs_z":"216/997","passed_gate":true,"site_strength":{"ref_percentile":37.1,"alt_percentile":35.5,"k":7}},{"model":"GATA4_NA_TAAAAT20NAAA_Y_jolma2013_0_3_7mer","mapping":"CIS-BP (GATA4)","group":"G010 GATA, 6 models","quality":0.789,"effect":0.304,"z":2.3,"p":0.022,"rank_abs_z":"734/997","passed_gate":false,"site_strength":{"ref_percentile":65.0,"alt_percentile":73.6,"k":7}},{"model":"GATA5_NA_TAAATG20NTAA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (GATA5)","group":"G010 GATA, 6 models","quality":0.882,"effect":0.265,"z":2.16,"p":0.031,"rank_abs_z":"751/997","passed_gate":false,"site_strength":{"ref_percentile":83.7,"alt_percentile":88.9,"k":7}},{"model":"GATA6_eDBD_TCCATC40NTGA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (GATA6)","group":"G010 GATA, 6 models","quality":0.937,"effect":0.304,"z":5.53,"p":3.1e-08,"rank_abs_z":"423/997","passed_gate":true,"site_strength":{"ref_percentile":77.6,"alt_percentile":59.2,"k":7}}]}

<a id="e41"></a>**E41** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TOX3%20locus%20enhancer%20CASC16%20breast%20cancer%20regulatory%20element&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:20:12+00:00)

> Europe PMC: 2 hits for 'TOX3 locus enhancer CASC16 breast cancer regulatory element'; top 2 with PMIDs:
> PMID 31338012 (2019): Association of <i>rs[masked]-CASC16 (LOC643714 locus)</i> and <i>rs[masked]-ACSF3</i> polymorphisms and their association with breast cancer risk among Iranian population.
> PMID 29215763 (2018): Breast cancer: The translation of big genomic data to cancer precision medicine.

<a id="e41a"></a>**E41a** literature_search, Europe PMC abstract, PMID 31338012 (https://europepmc.org/article/MED/31338012; retrieved 2026-10-26T22:20:12+00:00)

> rs[masked]-CASC16 and rs[masked]-ACSF3, as single nucleotide polymorphisms (SNPs), located at the 16q may affect the FOXA1 DNA binding sequence change and therefore may enhance the FOXA1-binding affinity to the promoter of TOX3 gene.

<a id="e41b"></a>**E41b** literature_search, Europe PMC abstract, PMID 31338012 (https://europepmc.org/article/MED/31338012; retrieved 2026-10-26T22:20:12+00:00)

> This is in line with other studies suggesting these SNPs as risk-associated polymorphisms which may lead to a change in the affinity of FOXA1, as a distal enhancer, to TOX3 and thus change in TOX3 expression, which can eventually affect the risk of breast cancer.

<a id="e42"></a>**E42** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for TOX3 (0 = no effect, -1 = median common-essential; < -0.5 called dependent). MCF7 (ACH-000019): 0.11. Breast lineage, 53 lines: median 0.04, 0% dependent. All 1183 lines: median 0.05, 0% dependent.

<a id="e43"></a>**E43** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T22:20:15+00:00)

> Open Targets: SPDEF and breast cancer (MONDO_0007254), overall score 0.11; by evidence type: literature 0.91
