# rs56007086 and Breast cancer (16q12)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.03 over 13 model calls; 267 s.

Variant `chr16:52565398:G>A` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z 12.52); SPDEF (bound here, z -7.0); NR2F2 (bound here, z 10.89, weak site); GATA3 (bound here, z 8.32, weak site); FOXA1 (bound here, z 6.27, weak site); CEBPB (bound here, z -1.64, no clear allelic change, weak site); NFIA (bound elsewhere, z 15.29); PITX1 (bound elsewhere, z 12.33); ZNF772 (bound elsewhere, z 9.58); AHDC1 (bound elsewhere, z 9.17). Occupancy unknown: ETV3 (z -47.67); SLC2A4RG (z -45.42); MTERF3 (z 24.43); PBX4 (z 18.55); SOX12 (z 17.9). Diagnostic, not shown to the model: 569 of 997 models pass Bonferroni.

## Ranked chains

### 1. H2: SPDEF loss of binding at a putative regulatory element (p = 0.43)

TF SPDEF (QBiC-SELEX coverage own_model), ref allele binds more; element Putative regulatory element at the variant; its identity with the nearby active dELS is unestablished.; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SPDEF is occupied over the variant in MCF-7, and its own QBiC-SELEX model detects a strong-site change favoring G over A. This is the strongest supplied TF-specific binding evidence, but it does not establish an in-cell allelic effect. | supported | [E07](#e07), [E21](#e21) |
| element | VEP annotates an enhancer feature at the variant, but no ENCODE cCRE overlaps it; the active dELS 38 bp away is not shown to be the same element. | weak | [E01](#e01), [E03](#e03) |
| gene | TOX3 is nearby and is a candidate target, but the evidence does not connect this variant or its putative element to TOX3 regulation; the locus-specific literature search found no functional evidence. | weak | [E02](#e02), [E39](#e39), [E40](#e40) |
| cell_type | SPDEF is expressed and has a ChIP-seq peak over the variant in MCF-7. | supported | [E07](#e07), [E21](#e21) |
| phenotype | TOX3 has gene-level breast-cancer association evidence, but no supplied evidence establishes a disease effect for this variant or a SPDEF-mediated mechanism. | weak | [E15](#e15), [E16](#e16), [E18a](#e18a), [E18b](#e18b), [E37](#e37) |

Predictions: An allele-specific SPDEF binding assay should favor G over A.; If this variant has a regulatory effect through SPDEF, perturbing SPDEF should alter that variant-dependent effect; the target gene and direction of expression change are not established.

Falsified if: Relevant-context assays find no G-over-A SPDEF binding difference.; A reproducible variant-dependent regulatory effect is unchanged by SPDEF perturbation.

### 2. H5: Null: no TF-mediated effect of this variant (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing G to A will not produce a reproducible TF-dependent regulatory effect in a relevant breast-cell context.; Any disease association could reflect linkage or another mechanism; the supplied evidence does not establish this variant as causal.

Falsified if: Variant editing produces a reproducible allele-dependent regulatory effect that depends on a specific TF in a relevant breast-cell context.

### 3. H1: TCF7L2-associated binding change at a putative regulatory element (p = 0.17)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element Putative regulatory element at the variant; its identity with the nearby active dELS is unestablished.; gene TOX3; cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is occupied over the variant in MCF-7. QBiC-SELEX models mapped from TCF7L1, TCF7 and LEF1 predict greater A binding, including a strong-site prediction, but there is no TCF7L2-specific model here; the direction for TCF7L2 is therefore tentative. | weak | [E10](#e10), [E20](#e20), [E38](#e38) |
| element | VEP annotates an enhancer feature at the variant, but no ENCODE cCRE overlaps it; the active dELS 38 bp away is not shown to be the same element. | weak | [E01](#e01), [E03](#e03) |
| gene | TOX3 is nearby and is a candidate target, but the evidence does not connect this variant or its putative element to TOX3 regulation; the locus-specific literature search found no functional evidence. | weak | [E02](#e02), [E39](#e39), [E40](#e40) |
| cell_type | TCF7L2 has a ChIP-seq peak over the variant in MCF-7, although its expression is relatively low in the supplied DepMap data. | supported | [E10](#e10), [E20](#e20) |
| phenotype | TOX3 has gene-level breast-cancer association evidence, but no supplied evidence links this variant or a TCF7L2-mediated effect to the disease. | weak | [E15](#e15), [E16](#e16), [E18a](#e18a), [E18b](#e18b), [E37](#e37) |

Predictions: A variant-specific TCF7L2 binding assay should favor A over G if the related-factor QBiC-SELEX predictions transfer to TCF7L2.; If causal, the variant-dependent regulatory effect should change with TCF7L2 perturbation; the regulated gene and expression direction are not established.

Falsified if: Relevant-context, factor-specific assays show no A-over-G TCF7L2 binding difference.; A reproducible variant-dependent regulatory effect is unchanged by TCF7L2 perturbation.

## Prediction matrix

| Test | Cost | Separates top two | H2 | H5 | H1 |
| --- | --- | --- | --- | --- | --- |
| Compare G- and A-allele reporter constructs with SPDEF present versus depleted in MCF-7 cells. | medium | yes | A reproducible allele-dependent reporter effect that changes with SPDEF depletion; binding evidence predicts stronger SPDEF binding to G, but does not specify the reporter-activity direction. | No reproducible TF-dependent allele effect. | No SPDEF-dependent allele effect is expected; an effect, if present, should instead depend on TCF7L2. |
| Measure allele-specific SPDEF binding to variant-centered G and A DNA probes. | low | yes | Greater SPDEF binding to the G probe. | No reproducible SPDEF allele difference supporting a TF-mediated effect. | No SPDEF-specific allele difference is predicted by this chain. |
| Measure allele-specific TCF7L2 binding to variant-centered G and A DNA probes. | low | no | No TCF7L2-specific allele difference is predicted by this chain. | No reproducible TCF7L2 allele difference supporting a TF-mediated effect. | Greater TCF7L2 binding to the A probe if the related-factor predictions transfer. |

## Next experiment

Run the low-cost allele-specific SPDEF binding assay with variant-centered G and A probes; it directly tests the strongest binding hypothesis against the null. A positive binding result would still need functional validation, such as the SPDEF-perturbed reporter test, to establish a TF-mediated regulatory effect.

## Refinement rounds

Stopped: round 3 left the top chain and the grades of its links unchanged.

### Round 1

- literature_search({"query": "TOX3 enhancer breast cancer functional validation target gene variant"}) for H1.gene, ran as [E35](#e35). Expected: If the search finds functional evidence linking a TOX3-region enhancer to TOX3, H1.gene and the TOX3-target claims in the other hypotheses gain support; if it finds only general association or review statements, those links remain weak.
- eqtl_lookup({"tissue": "Breast Mammary Tissue"}) for H1.gene, ran as [E36](#e36). Expected: A significant eQTL for this variant in breast mammary tissue would identify an expression link and potentially a target gene, changing the gene-link grades and chain ranking. No eQTL, or one without a clear relevant target, would leave the target assignment unresolved.
- gene_disease({"gene": "TOX3"}) for H1.phenotype, ran as [E37](#e37). Expected: Breast-cancer association evidence for TOX3 could strengthen the gene-level disease context, but would not establish this variant's effect or mechanism. Little or no association evidence would leave the phenotype link weak.

- Result of literature_search({"query":"TOX3 enhancer breast cancer functional validation target gene variant"}): E35 returned mainly review-level material. It repeated a general statement about TOX3 enhancer mutations and explicitly noted the need for functional validation; it did not provide functional evidence connecting this variant or element to TOX3. (as expected: yes)
- Result of eqtl_lookup({"tissue":"Breast Mammary Tissue"}): E36 found no significant GTEx v8 eQTL for this variant in breast mammary tissue, so the target-gene assignment remains unresolved. (as expected: yes)
- Result of gene_disease({"gene":"TOX3"}): E37 reported a TOX3–breast cancer overall score of 0.58, with genetic-association and literature evidence; this strengthens gene-level disease context but does not establish a causal effect of this variant. (as expected: yes)

Chains after revision: SPDEF 0.45; null 0.25; TCF7L2 0.16; GATA3 0.08; FOXA1 0.06. Link grades changed: H1.phenotype: weak → supported, H2.phenotype: weak → supported, H3.phenotype: weak → supported, H4.phenotype: weak → supported.

### Round 2

- qbic_tf_detail({"tf": "TCF7L2"}) for H1.binding, ran as [E38](#e38). Expected: If TCF7L2 has an applicable model that independently predicts stronger binding to A, H1.binding becomes better supported and H1 may rise relative to H2; if coverage is only through TCF7L1-mapped models or predicts no clear change, H1 remains weak or falls.
- literature_search({"query": "chr16:52565398 TOX3 breast cancer variant functional validation"}) for H1.gene, ran as [E39](#e39). Expected: If the search finds locus- or variant-specific evidence connecting this site or its regulatory element to TOX3, H1.gene improves; if it returns only general TOX3/breast-cancer literature, the link remains weak.

- Result of qbic_tf_detail({"tf":"TCF7L2"}) for H1.binding: E38 reports three mapped models (LEF1-, TCF7-, and TCF7L1-mapped), all predicting stronger binding to A. This adds proxy-model support for an A-favoring effect, but does not provide a TCF7L2-specific model. (as expected: unclear)
- Result of literature_search({"query":"chr16:52565398 TOX3 breast cancer variant functional validation"}) for H1.gene: E39 reports no literature hits for the locus- or variant-specific search; no variant-to-TOX3 regulatory evidence was found. (as expected: yes)

Chains after revision: SPDEF 0.37; null 0.31; TCF7L2 0.23; GATA3 0.05; FOXA1 0.04. Link grades changed: H1.phenotype: supported → weak, H2.phenotype: supported → weak, H3.phenotype: supported → weak, H4.phenotype: supported → weak.

### Round 3

- literature_search({"query": "chr16:52565398 TOX3 CASC16 enhancer target gene allele-specific functional validation breast cancer"}) for H2.gene, ran as [E40](#e40). Expected: If this search finds locus-specific functional evidence connecting the variant or its regulatory element to TOX3, H2.gene strengthens; evidence for another target would revise the gene claim. If it finds no such evidence, the proximity-based link remains weak.
- qbic_tf_detail({"tf": "GATA3"}) for H3.binding, ran as [E41](#e41). Expected: If additional GATA3-mapped models consistently predict a detectable allelic effect, H3.binding becomes more persuasive; if the lookup confirms only weak or conflicting mapped predictions, it remains weak.
- qbic_tf_detail({"tf": "FOXA1"}) for H4.binding, ran as [E42](#e42). Expected: If additional FOXA1-mapped models consistently support an A-favoring effect, H4.binding strengthens; if the lookup confirms only the weak FOXA2-mapped prediction or conflicting directions, it remains weak.

- Result of literature_search for locus-specific functional evidence connecting the variant or element to TOX3: E40 reports zero hits for the query. No locus-specific functional evidence was found, so the proximity-based TOX3 link remains weak. (as expected: yes)
- Result of qbic_tf_detail for GATA3: E41 shows no detectable effect in GATA3's own model (z -0.06). A GATA2-mapped model predicts a small A-favoring change, but its site is weak; the lookup does not provide persuasive GATA3-specific allelic binding evidence. (as expected: yes)
- Result of qbic_tf_detail for FOXA1: E42 shows no detectable effect in FOXA1's own model (z 1.25). A FOXA2-mapped model predicts a small A-favoring change at a weak site, while other mapped family models do not resolve a FOXA1-specific effect. (as expected: yes)

Chains after revision: SPDEF 0.43; null 0.40; TCF7L2 0.17. Link grades changed: H3.binding: weak → absent, H3.cell_type: supported → absent, H3.element: weak → absent, H3.gene: weak → absent, H3.phenotype: weak → absent, H4.binding: weak → absent, H4.cell_type: supported → absent, H4.element: weak → absent, H4.gene: weak → absent, H4.phenotype: weak → absent.

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

<a id="e35"></a>**E35** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TOX3%20enhancer%20breast%20cancer%20functional%20validation%20target%20gene%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T23:27:34+00:00)

> Europe PMC: 32 hits for 'TOX3 enhancer breast cancer functional validation target gene variant'; top 8 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 41668068 (2026): Deciphering the eRNA landscape and revealing target aberrant pathways in prostate cancer.
> PMID 41624772 (2025): Regulatory QTLs affecting miRNA-mRNA interactions in cancer: mechanisms, methods, and clinical implications.
> PMID 41596432 (2026): Bone Metastasis in Estrogen Receptor-Positive Breast Cancer: Molecular Insights and Therapeutic Advances.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 39777116 (2025): Identification of significant single-nucleotide polymorphisms associated with breast cancer recurrence and metastasis using GWAS.
> PMID 39341862 (2024): Identification of candidate causal variants and target genes at 41 breast cancer risk loci through differential allelic expression analysis.
> PMID 34741135 (2022): Functional annotation of breast cancer risk loci: current progress and future directions.

<a id="e35a"></a>**E35a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-26T23:27:34+00:00)

> Key examples include promoter mutations [e.g., rs[masked] (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs[masked] (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e35b"></a>**E35b** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-26T23:27:34+00:00)

> This Review also critically identifies the pressing need for more specific functional validation studies to fully elucidate their mechanistic roles.

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565398_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:27:56+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565398_G_A_b38 in tissues matching 'Breast Mammary Tissue'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e37"></a>**E37** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:34:32+00:00)

> Open Targets: TOX3 and breast cancer (MONDO_0007254), overall score 0.58; by evidence type: genetic_association 0.91, literature 0.89

<a id="e38"></a>**E38** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr16:52565398:G>A","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":0.492,"z":5.25,"p":1.5e-07,"rank_abs_z":"446/997","passed_gate":true,"site_strength":{"ref_percentile":82.3,"alt_percentile":96.7,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":0.531,"z":11.75,"p":6.7e-32,"rank_abs_z":"84/997","passed_gate":true,"site_strength":{"ref_percentile":90.0,"alt_percentile":80.7,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":0.745,"z":12.52,"p":6e-36,"rank_abs_z":"70/997","passed_gate":true,"site_strength":{"ref_percentile":57.0,"alt_percentile":97.8,"k":7}}]}

<a id="e39"></a>**E39** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr16%3A52565398%20TOX3%20breast%20cancer%20variant%20functional%20validation&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T23:28:55+00:00)

> Europe PMC: 0 hits for 'chr16:52565398 TOX3 breast cancer variant functional validation'; top 0 with PMIDs:

<a id="e40"></a>**E40** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr16%3A52565398%20TOX3%20CASC16%20enhancer%20target%20gene%20allele-specific%20functional%20validation%20breast%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T23:30:13+00:00)

> Europe PMC: 0 hits for 'chr16:52565398 TOX3 CASC16 enhancer target gene allele-specific functional validation breast cancer'; top 0 with PMIDs:

<a id="e41"></a>**E41** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GATA3","symbol":"GATA3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565398:G>A","gate_p":5.02e-05,"models":[{"model":"GATA3_NA_TGTCGT20NGA_ESAC_yang2017_0_4_7mer","mapping":"own","group":"G010 GATA, 6 models","quality":0.858,"effect":-0.004,"z":-0.06,"p":0.95,"rank_abs_z":"993/997","passed_gate":false,"site_strength":{"ref_percentile":87.4,"alt_percentile":87.8,"k":7}},{"model":"GATA1_eDBD_TTTAGA40NGGC_KN_yin2017_0_4_7mer","mapping":"CIS-BP (GATA1)","group":"G010 GATA, 6 models","quality":0.626,"effect":0.069,"z":0.43,"p":0.67,"rank_abs_z":"941/997","passed_gate":false,"site_strength":{"ref_percentile":81.3,"alt_percentile":71.0,"k":7}},{"model":"GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer","mapping":"CIS-BP (GATA2)","group":"G010 GATA, 6 models","quality":0.874,"effect":0.197,"z":8.32,"p":9.2e-17,"rank_abs_z":"216/997","passed_gate":true,"site_strength":{"ref_percentile":37.1,"alt_percentile":35.5,"k":7}},{"model":"GATA4_NA_TAAAAT20NAAA_Y_jolma2013_0_3_7mer","mapping":"CIS-BP (GATA4)","group":"G010 GATA, 6 models","quality":0.789,"effect":0.304,"z":2.3,"p":0.022,"rank_abs_z":"734/997","passed_gate":false,"site_strength":{"ref_percentile":65.0,"alt_percentile":73.6,"k":7}},{"model":"GATA5_NA_TAAATG20NTAA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (GATA5)","group":"G010 GATA, 6 models","quality":0.882,"effect":0.265,"z":2.16,"p":0.031,"rank_abs_z":"751/997","passed_gate":false,"site_strength":{"ref_percentile":83.7,"alt_percentile":88.9,"k":7}},{"model":"GATA6_eDBD_TCCATC40NTGA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (GATA6)","group":"G010 GATA, 6 models","quality":0.937,"effect":0.304,"z":5.53,"p":3.1e-08,"rank_abs_z":"423/997","passed_gate":true,"site_strength":{"ref_percentile":77.6,"alt_percentile":59.2,"k":7}}]}

<a id="e42"></a>**E42** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"FOXA1","symbol":"FOXA1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565398:G>A","gate_p":5.02e-05,"models":[{"model":"FOXA1_FL_TCCCAT40NTGT_KX_yin2017_0_4_7mer","mapping":"own","group":"G022 Forkhead, 4 models","quality":0.775,"effect":0.046,"z":1.25,"p":0.21,"rank_abs_z":"857/997","passed_gate":false,"site_strength":{"ref_percentile":96.4,"alt_percentile":98.5,"k":7}},{"model":"FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer","mapping":"CIS-BP (FOXA2)","group":"G022 Forkhead, 4 models","quality":0.83,"effect":0.131,"z":6.27,"p":3.7e-10,"rank_abs_z":"364/997","passed_gate":true,"site_strength":{"ref_percentile":90.2,"alt_percentile":81.8,"k":7}},{"model":"FOXA3_FL_TGTGGT40NGGC_KX_yin2017_0_3_7mer","mapping":"CIS-BP (FOXA3)","group":"G022 Forkhead, 4 models","quality":0.928,"effect":0.105,"z":1.4,"p":0.16,"rank_abs_z":"835/997","passed_gate":false,"site_strength":{"ref_percentile":80.1,"alt_percentile":87.8,"k":7}},{"model":"FOXB1_NA_TGAGCA30NCGA_ESAI_yang2017_0_4_7mer","mapping":"CIS-BP (FOXB1)","group":"G022 Forkhead, 4 models","quality":0.674,"effect":0.319,"z":4.58,"p":4.7e-06,"rank_abs_z":"518/997","passed_gate":true,"site_strength":{"ref_percentile":97.1,"alt_percentile":99.3,"k":7}}]}
