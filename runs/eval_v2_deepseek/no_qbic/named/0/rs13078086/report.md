# rs13078086 and Colorectal cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 134 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H1: Null: no TF-mediated allelic effect; the variant is non-functional or linked to a causal variant (p = 0.94)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs13078086 in HCT116; No allele-specific regulatory effect on nearby genes attributable to this variant

Falsified if: A well-controlled allele-specific assay detects TF binding at chr3:191441666 in HCT116; A reporter or endogenous allele-specific assay shows a reproducible regulatory effect of T>G on a nearby gene in HCT116

### 2. H2: CTCF binding at a nearby dELS affects PYDC2 (p = 0.03)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element Nearby dELS EH38E2269392, 42 bp from the variant; the variant itself is not in a cCRE; gene PYDC2; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is the only TF with any nearby element signal: the nearest dELS has CTCF z 1.5. However, no ENCODE CTCF ChIP-seq peak contains the variant in any biosample, including HCT116, and no QBiC-SELEX model or allele-specific CTCF assay is supplied. The proposed ref T > alt G binding direction is therefore an untested hypothesis, not an observed effect. | missing | [E03](#e03), [E04](#e04) |
| element | The variant is intronic and does not overlap an annotated cCRE. It could only act through an unproven distal effect on the dELS 42 bp away; no allele-specific regulatory assay is supplied. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb, but no chromatin-contact, reporter, perturbation, or eQTL evidence connects this variant or the nearby dELS to PYDC2. | missing | [E02](#e02), [E07](#e07) |
| cell_type | The mechanism is proposed in HCT116, the supplied expression context. There is no positive HCT116 evidence for CTCF occupancy at this site; ENCODE HCT116 has zero TF ChIP-seq peaks over the variant. | missing | [E04](#e04) |
| phenotype | Altered PYDC2 regulation is hypothesized to affect colorectal cancer biology, but there is no GWAS, eQTL, Open Targets, or direct variant-specific colorectal cancer evidence supporting this link. | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E11](#e11) |

Predictions: Alt G reduces CTCF occupancy at chr3:191441666 or the nearby dELS in HCT116; Alt G changes PYDC2 expression in HCT116 in a CTCF-dependent manner

Falsified if: Allele-specific CTCF ChIP, EMSA, or reporter assays show no ref-favored CTCF binding at chr3:191441666; A reporter or endogenous assay shows no allele-specific effect of T>G on PYDC2 expression in HCT116

### 3. H3: NFKB1 binding at the intronic variant affects PYDC2 (p = 0.02)

TF NFKB1 (QBiC-SELEX coverage own_model), alt allele binds more; element Intronic PYDC2-AS1 sequence with no overlapping cCRE; possible weak or context-specific distal regulatory activity; gene PYDC2; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NFKB1 is proposed to bind the alt G allele more strongly than ref T. This is speculative: no NFKB1 ChIP-seq peak contains the variant, no QBiC-SELEX model is supplied for NFKB1, and no motif or allele-specific assay supports the direction. | missing | [E04](#e04) |
| element | The variant lies in an intron of PYDC2-AS1 and does not overlap an annotated cCRE, so it would need to act through unproven weak or cell-type-specific regulatory sequence. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb, but no chromatin-contact, reporter, perturbation, or eQTL evidence connects this intronic variant to PYDC2. | missing | [E02](#e02), [E07](#e07) |
| cell_type | NFKB1 is expressed in HCT116 (26.26 TPM, rank 205 of 1626 TFs), so expression does not exclude it. However, there is no HCT116 NFKB1 ChIP-seq occupancy over the variant. | weak | [E09](#e09), [E04](#e04) |
| phenotype | PYDC2 has no Open Targets association with colorectal cancer, and the Europe PMC hits are not variant-specific and do not establish that NFKB1-dependent PYDC2 regulation affects colorectal cancer. | missing | [E11](#e11), [E08](#e08) |

Predictions: Alt G increases NFKB1 occupancy at chr3:191441666 in HCT116; Alt G increases PYDC2 expression in an NFKB1-dependent manner

Falsified if: NFKB1 ChIP, EMSA, or reporter assays show no alt-favored NFKB1 binding at chr3:191441666; No allele-specific effect on PYDC2 expression is observed in an NFKB1-dependent assay

### 4. H4: STAT3 binding at the intronic variant affects PYDC2 (p = 0.01)

TF STAT3 (QBiC-SELEX coverage not_in_coverage), alt allele binds more; element Intronic PYDC2-AS1 sequence; no cCRE overlap and no TF ChIP peak over the variant; gene PYDC2; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | STAT3 is proposed to bind the alt G allele more strongly than ref T. This is speculative: no STAT3 ChIP-seq peak contains the variant, no QBiC-SELEX model is supplied for STAT3, and no motif or allele-specific assay supports the direction. | missing | [E04](#e04) |
| element | The variant is intronic in PYDC2-AS1 and does not overlap a cCRE, making any STAT3-dependent element unproven and at best weak or context-specific. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb, but no chromatin-contact, reporter, perturbation, or eQTL evidence connects this variant to PYDC2. | missing | [E02](#e02), [E07](#e07) |
| cell_type | STAT3 is expressed in HCT116 (24.86 TPM, rank 224 of 1626 TFs), but at the 26.3rd percentile across DepMap lines, and there is no HCT116 STAT3 ChIP-seq occupancy over the variant. | weak | [E10](#e10), [E04](#e04) |
| phenotype | PYDC2 has no Open Targets colorectal cancer association, and the Europe PMC hits do not provide variant-specific or STAT3-dependent evidence linking PYDC2 regulation to colorectal cancer. | missing | [E11](#e11), [E08](#e08) |

Predictions: Alt G increases STAT3 occupancy at chr3:191441666 in HCT116; Alt G changes PYDC2 expression in a STAT3-dependent manner

Falsified if: STAT3 ChIP, EMSA, or reporter assays show no alt-favored STAT3 binding at chr3:191441666; No allele-specific STAT3-dependent effect on PYDC2 expression is observed

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CTCF ChIP-qPCR or EMSA at rs13078086 in HCT116 cells heterozygous for T/G | low | yes | No allele-specific CTCF occupancy at chr3:191441666 in HCT116. | Ref T shows stronger CTCF occupancy than alt G at chr3:191441666 or the nearby dELS in HCT116. | No allele-specific CTCF occupancy at chr3:191441666; NFKB1, not CTCF, would be tested separately. | No allele-specific CTCF occupancy at chr3:191441666; STAT3, not CTCF, would be tested separately. |
| PYDC2 promoter/reporter or endogenous allele-specific expression assay with T vs G in HCT116 | medium | yes | No reproducible T>G allele effect on PYDC2 expression. | Reproducible T>G allele effect on PYDC2 expression in HCT116, CTCF-dependent. | Reproducible T>G allele effect on PYDC2 expression, NFKB1-dependent. | Reproducible T>G allele effect on PYDC2 expression, STAT3-dependent. |
| Allele-specific NFKB1 ChIP-qPCR at rs13078086 in HCT116 | low | no | No allele-specific NFKB1 occupancy. | No allele-specific NFKB1 occupancy. | Alt G shows stronger NFKB1 occupancy than ref T at chr3:191441666. | No allele-specific NFKB1 occupancy. |
| Allele-specific STAT3 ChIP-qPCR at rs13078086 in HCT116 | low | no | No allele-specific STAT3 occupancy. | No allele-specific STAT3 occupancy. | No allele-specific STAT3 occupancy. | Alt G shows stronger STAT3 occupancy than ref T at chr3:191441666. |
| CRISPR deletion or reporter perturbation of dELS EH38E2269392 with PYDC2 expression readout in HCT116 | high | yes | Deletion or perturbation of the nearby dELS does not alter PYDC2 expression in HCT116. | Deletion or perturbation of the nearby dELS alters PYDC2 expression in a CTCF-dependent manner. | No dELS-dependent effect; any NFKB1 effect would require a different, unannotated element. | No dELS-dependent effect; any STAT3 effect would require a different, unannotated element. |

## Next experiment

The cheapest experiment separating the top two chains (H1 vs H2) is an allele-specific CTCF ChIP-qPCR or EMSA at rs13078086 in HCT116 cells heterozygous for T/G. Cost: low. It directly tests H2's required ref-favored CTCF binding; absence of allele-specific CTCF binding falsifies H2 and supports the null H1.

## Investigate calls

- tf_expression({"tf": "NFKB1", "context": "DepMap:ACH-000971"})
- tf_expression({"tf": "STAT3", "context": "DepMap:ACH-000971"})
- gene_disease({"gene": "PYDC2"})

## Flags

- literature_fallback: no hits for 'rs13078086 AND PYDC2 AND "colorectal cancer"'; dropped the rsID

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/3:191441666-191441666:1/G?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:32:09+00:00)

> Variant chr3:191441666:T>G (GRCh38), allele string T/G
> Known IDs: rs13078086
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: -1.82
> Transcript consequences: PYDC2-AS1 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/3:190441666-192441666?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:06+00:00)

> 8 protein-coding genes within 1000 kb of chr3:191441666:T>G, by distance to TSS:
> PYDC2: 19.5 kb from TSS (upstream, strand +1)
> UTS2B: 111.1 kb from TSS (upstream, strand -1)
> CCDC50: 112.6 kb from TSS (downstream, strand +1)
> OSTN: 242.4 kb from TSS (downstream, strand +1)
> GMNC: 549.2 kb from TSS (upstream, strand -1)
> IL1RAP: 954.2 kb from TSS (downstream, strand +1)
> TMEM207: 991.8 kb from TSS (upstream, strand -1)
> FGF12: 1326.1 kb from TSS (downstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:05+00:00)

> No cCRE overlaps the variant; nearest is EH38E2269392 (dELS) 42 bp away.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2269392 dELS: DNase z 3.5, H3K27ac z 1.8, H3K4me3 z 1.5, CTCF z 1.5; nearby genes AC073365.1, PYDC2, CCDC50
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> No ENCODE TF ChIP-seq peak contains chr3:191441666:T>G in any biosample. In the matching biosample HCT116: 0 peaks from 0 factors. No cCRE contains the variant. Of the TFs with a binding model, 16 were assayed in the matching biosample and 557 only elsewhere, all without a peak here; 536 were never assayed.

<a id="e05"></a>**E05** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs13078086&size=100; retrieved 2026-10-25T17:32:10+00:00)

> 0 GWAS Catalog associations for rs13078086, strongest first:

<a id="e06"></a>**E06** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:09+00:00)

> Open Targets has no record of 3_191441666_T_G.

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38. NES is the effect of the alt allele (G) relative to ref (T).

<a id="e08"></a>**E08** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PYDC2%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:10+00:00)

> Europe PMC: 16 hits for 'PYDC2 AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 40026444 (2025): Correlation Analysis of Pyroptosis-Related Genes CASP1, NLRP3, AIM2, and NLRP1 With Lung Adenocarcinoma.
> PMID 41154652 (2025): Oncogenic Role of SAMD4B in Breast Cancer Progression by Activating Wnt/β-Catenin Pathway.
> PMID 36319832 (2022): A novel refined pyroptosis and inflammasome-related genes signature for predicting prognosis and immune microenvironment in pancreatic ductal adenocarcinoma.
> PMID 36341349 (2022): The strategies of NLRP3 inflammasome to combat <i>Toxoplasma gondii</i>.
> PMID 36732864 (2023): RNA binding protein SAMD4: current knowledge and future perspectives.
> PMID 39561929 (2024): Optimizing iNKT-driven immune responses against cancer by modulating CD1d in tumor and antigen presenting cells.
> PMID 35159382 (2022): Metabolomics of Acute vs. Chronic Spinach Intake in an Apc-Mutant Genetic Background: Linoleate and Butanoate Metabolites Targeting HDAC Activity and IFN-γ Signaling.
> PMID 35338151 (2022): PUMILIO proteins promote colorectal cancer growth via suppressing p21.

<a id="e09"></a>**E09** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> NFKB1 in DepMap line ACH-000971: 26.26 TPM, rank 205 of 1626 TFs (1 = highest); this context is at the 82.4th percentile of NFKB1 across all DepMap lines.

<a id="e10"></a>**E10** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> STAT3 in DepMap line ACH-000971: 24.86 TPM, rank 224 of 1626 TFs (1 = highest); this context is at the 26.3th percentile of STAT3 across all DepMap lines.

<a id="e11"></a>**E11** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575).
