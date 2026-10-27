# rs13078086 and Colorectal cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 101 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. null: No TF-mediated effect (p = 0.88)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at chr3:191441666 T>G.; No allele-specific regulatory effect distinguishable from linked variation or background.; The negative genetic evidence remains the best summary: E04 reports 0 GWAS Catalog associations, E05 reports no Open Targets record, E08 reports 0 colon-transverse eQTLs, and E09 reports no PYDC2 colorectal cancer association.; E07 provides no HCT116 CTCF ChIP-seq peak containing the variant, consistent with no CTCF-mediated effect at this site.

Falsified if: Allele-specific TF binding is demonstrated at chr3:191441666 in colorectal cells.; Chromatin contact, allele-specific expression, or eQTL evidence links the variant to a target gene in colorectal tissue.; A genetic association for the variant or its target gene in colorectal cancer is established.

### 2. ctcf_alt_PYDC2_AS1: Alt allele creates stronger CTCF binding and alters PYDC2-AS1 lncRNA regulation (p = 0.07)

TF CTCF (stated coverage not_checked; registry own_model), alt allele binds more; element The variant is intronic in PYDC2-AS1 and 42 bp from dELS EH38E2269392; this is proximity/annotation only, not evidence that the element is functional or allele-specifically perturbed.; gene PYDC2-AS1; cell type HCT 116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF binds the alt G allele more strongly than the ref T allele at the intronic site; this is an unsupported speculative claim with no positive binding evidence. | missing | none |
| element | The variant is intronic in PYDC2-AS1 and 42 bp from dELS EH38E2269392, making local lncRNA regulatory context a candidate element. | weak | [E01](#e01), [E03](#e03) |
| gene | The variant is annotated as a PYDC2-AS1 intron variant, so PYDC2-AS1 is the candidate transcript. | supported | [E01](#e01) |
| cell_type | The stated expression context is HCT 116 colorectal cancer cells. | missing | none |
| phenotype | Altered PYDC2-AS1 regulation could affect colorectal cancer biology, but no direct variant-disease or gene-disease association is shown. | missing | none |

Predictions: Allele-specific CTCF binding is stronger on G than T at the PYDC2-AS1 intronic site.; The G allele changes PYDC2-AS1 expression or isoform usage in colorectal cells.; If CTCF is repressive at this element, stronger G-allele CTCF binding could reduce PYDC2-AS1 expression.

Falsified if: No allele-specific CTCF binding is detected at the PYDC2-AS1 intronic site in HCT116 or colorectal cells.; The dELS EH38E2269392 does not contact the PYDC2-AS1 locus in colorectal cells.; PYDC2-AS1 expression or isoform usage is not allele-dependent in colorectal cells.

### 3. ctcf_ref_CCDC50: Ref allele preserves CTCF binding and alters CCDC50 through a nearby dELS (p = 0.05)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element The variant is 42 bp from dELS EH38E2269392; this is proximity only, not evidence that the ref allele preserves a CTCF site or that changing it alters the element.; gene CCDC50; cell type HCT 116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF binds the ref T allele more strongly than the alt G allele at the intronic site; this is an unsupported speculative claim with no positive binding evidence. | missing | none |
| element | The variant is 42 bp from dELS EH38E2269392, a candidate regulatory element that could lose CTCF occupancy when the ref allele is changed. | weak | [E03](#e03) |
| gene | CCDC50 is a nearby protein-coding gene, 112.6 kb downstream of the variant; this is proximity only. | weak | [E02](#e02) |
| cell_type | The stated expression context is HCT 116 colorectal cancer cells. | missing | none |
| phenotype | Allele-dependent CCDC50 regulation could contribute to colorectal cancer, but no direct variant-disease or gene-disease association is shown. | missing | none |

Predictions: Allele-specific CTCF binding is stronger on T than G.; The G allele reduces CTCF occupancy and changes CCDC50 expression.; The EH38E2269392 element contacts CCDC50 rather than PYDC2-AS1 in colorectal cells.

Falsified if: CTCF binding is stronger to G than T, or no allele-specific CTCF binding is seen.; The dELS EH38E2269392 does not contact CCDC50 in colorectal cells.; CCDC50 expression is not allele-dependent in colorectal cells.

## Prediction matrix

| Test | Cost | Separates top two | null | ctcf_alt_PYDC2_AS1 | ctcf_ref_CCDC50 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific CTCF binding assay, e.g. EMSA or competitive binding with HCT116 nuclear extract, using T and G probes | low | yes | No reproducible allele-specific CTCF binding; no difference between T and G, or no binding. | G allele binds CTCF more strongly than T. | T allele binds CTCF more strongly than G. |
| HCT116 CTCF ChIP-qPCR or allele-specific reanalysis of HCT116 CTCF ChIP-seq at chr3:191441666 | low | yes | No CTCF ChIP-seq peak or allele-specific read imbalance at chr3:191441666 in HCT116; consistent with E07. | CTCF ChIP signal at the variant with G-allele bias, if heterozygous. | CTCF ChIP signal at the variant with T-allele bias, if heterozygous. |
| Colon-transverse eQTL or allele-specific expression assay for PYDC2-AS1 and CCDC50 | medium | yes | No allele-specific expression effect on PYDC2-AS1 or CCDC50 in colon/HCT116; consistent with E08. | G allele associates with altered PYDC2-AS1 expression or isoform usage. | G allele associates with altered CCDC50 expression. |
| 4C/Hi-C or CRISPR allele-swap perturbation of the variant and dELS EH38E2269392 in HCT116 | high | yes | No allele-specific chromatin contact or regulatory change at the locus. | EH38E2269392 contacts the PYDC2-AS1 locus, and the G allele changes that contact or PYDC2-AS1 expression. | EH38E2269392 contacts CCDC50, and the G allele reduces CTCF occupancy and changes CCDC50 expression. |

## Next experiment

Cheapest separating experiment: allele-specific CTCF binding assay using T and G probes with HCT116 nuclear extract. It directly tests the initiating binding claim of the top non-null chain against the null and is cheaper than chromatin-contact or CRISPR assays.

## Investigate calls

- chip_peaks({"tf": "CTCF", "biosample": "HCT 116"})
- eqtl_lookup({"tissue": "Colon - Transverse"})
- gene_disease({"gene": "PYDC2"})

## Flags

- literature_fallback: no hits for 'rs13078086 AND PYDC2 AND "colorectal cancer"'; dropped the rsID

Citation support: 0.40 of links cite only evidence that passed every check.

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs13078086&size=100; retrieved 2026-10-25T17:32:10+00:00)

> 0 GWAS Catalog associations for rs13078086, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:09+00:00)

> Open Targets has no record of 3_191441666_T_G.

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PYDC2%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:10+00:00)

> Europe PMC: 16 hits for 'PYDC2 AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 40026444 (2025): Correlation Analysis of Pyroptosis-Related Genes CASP1, NLRP3, AIM2, and NLRP1 With Lung Adenocarcinoma.
> PMID 41154652 (2025): Oncogenic Role of SAMD4B in Breast Cancer Progression by Activating Wnt/β-Catenin Pathway.
> PMID 36319832 (2022): A novel refined pyroptosis and inflammasome-related genes signature for predicting prognosis and immune microenvironment in pancreatic ductal adenocarcinoma.
> PMID 36341349 (2022): The strategies of NLRP3 inflammasome to combat <i>Toxoplasma gondii</i>.
> PMID 36732864 (2023): RNA binding protein SAMD4: current knowledge and future perspectives.
> PMID 39561929 (2024): Optimizing iNKT-driven immune responses against cancer by modulating CD1d in tumor and antigen presenting cells.
> PMID 35159382 (2022): Metabolomics of Acute vs. Chronic Spinach Intake in an Apc-Mutant Genetic Background: Linoleate and Butanoate Metabolites Targeting HDAC Activity and IFN-γ Signaling.
> PMID 35338151 (2022): PUMILIO proteins promote colorectal cancer growth via suppressing p21.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:26:42+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT 116'. Absence can also mean no CTCF experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (G) relative to ref (T).

<a id="e09"></a>**E09** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575).
