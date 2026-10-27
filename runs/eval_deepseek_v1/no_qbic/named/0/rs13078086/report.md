# rs13078086 and Colorectal cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 7 model calls; 124 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: No TF-mediated effect of rs13078086; linked causal variant, passenger variant, or no allelic effect (p = 0.90)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific CTCF or NFKB1 binding at chr3:191441666 T>G in HCT116 or related colorectal cells.; No allele-specific effect on nearby gene expression in colon tissue; E09 already found no colon transverse eQTL.; No allele-dependent enhancer reporter activity at the nearby dELS EH38E2269392.

Falsified if: A reproducible allele-specific CTCF or NFKB1 binding difference is found at chr3:191441666 T>G in HCT116 or colorectal cells and is linked to a nearby gene expression change.; The variant itself shows allele-dependent enhancer activity, or it is in strong linkage disequilibrium with a functional regulatory variant that explains the signal.

### 2. H1: CTCF binds the alt allele near a dELS and alters PYDC2/CCDC50 regulation (p = 0.07)

TF CTCF (stated coverage not_checked; registry own_model), alt allele binds more; element Nearby dELS EH38E2269392, 42 bp away, with weak biosample-max CTCF z-score and no cCRE overlapping the variant.; gene PYDC2 or CCDC50; cell type HCT 116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is the candidate TF and, under H1, the alt G allele binds CTCF more strongly than the ref T allele. QBiC-SELEX coverage is not_checked because no CTCF screen row or qbic_tf_detail lookup is provided. Direct support is absent: E03 gives only a nearby dELS with a weak biosample-max CTCF z-score, and E07 reports no HCT116 CTCF ChIP-seq peak containing the variant. | missing | [E03](#e03), [E07](#e07) |
| element | The variant is 42 bp from dELS EH38E2269392, but no cCRE overlaps the variant itself, so any effect would be on a nearby element rather than a promoter-overlapping site. | weak | [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb upstream and CCDC50 is 112.6 kb downstream, but E09 found no colon transverse eQTL, so the gene link remains proximity-only and unsupported. | missing | [E02](#e02), [E09](#e09) |
| cell_type | HCT 116 is the provided expression context, but E07 found no HCT116 CTCF ChIP-seq peak containing the variant and no HCT116-specific CTCF, reporter, or expression evidence is provided. | missing | [E07](#e07) |
| phenotype | A CTCF-dependent effect on PYDC2 or CCDC50 contributing to colorectal cancer is not established; E04 has zero GWAS Catalog associations and E05 has no Open Targets record for this variant. | missing | [E04](#e04), [E05](#e05) |

Predictions: Alt G shows stronger CTCF binding in an allele-specific EMSA or CTCF ChIP assay in HCT116.; The dELS EH38E2269392 shows allele-dependent enhancer activity, with the G allele changing reporter output.; CTCF knockdown or mutation of the CTCF motif changes PYDC2 or CCDC50 expression in HCT116.

Falsified if: Allele-specific CTCF binding assays show no preferential binding of the alt G allele at this site.; Reporter or CRISPR assays show no allele-dependent enhancer activity at EH38E2269392.; CTCF perturbation does not alter PYDC2 or CCDC50 expression in HCT116 cells.

### 3. H2: NFKB1 binds the alt allele near PYDC2 and alters inflammasome/pyroptosis signaling (p = 0.03)

TF NFKB1 (stated coverage not_checked; registry own_model), alt allele binds more; element PYDC2-AS1 intron and nearby dELS EH38E2269392, 42 bp from the variant.; gene PYDC2; cell type HCT 116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NFKB1 is the candidate TF and, under H2, the alt G allele binds NFKB1 more strongly than the ref T allele. QBiC-SELEX coverage is not_checked because no NFKB1 screen row or qbic_tf_detail lookup is provided. Direct support is absent: E08 reports no HCT116 NFKB1 ChIP-seq peak containing the variant. | missing | [E08](#e08) |
| element | The variant is intronic in PYDC2-AS1 and 42 bp from dELS EH38E2269392, but no cCRE overlaps the variant and the element's inflammatory regulatory role is not shown. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb, but E09 found no colon transverse eQTL connecting rs13078086 to PYDC2 or other nearby genes. | missing | [E02](#e02), [E09](#e09) |
| cell_type | HCT 116 is the provided expression context, but E08 found no HCT116 NFKB1 ChIP-seq peak containing the variant and no HCT116-specific NFKB1 or PYDC2 assay is provided. | missing | [E08](#e08) |
| phenotype | An NFKB1-dependent PYDC2 effect on pyroptosis or inflammasome signaling in colorectal cancer is not established; E04 has zero GWAS Catalog associations and E05 has no Open Targets record. | missing | [E04](#e04), [E05](#e05) |

Predictions: Alt G increases NFKB1 binding at the variant or nearby dELS in HCT116.; NFKB1 perturbation changes PYDC2 expression in colorectal cells.; The variant associates with pyroptosis/inflammasome-related expression signatures in colorectal cancer models.

Falsified if: Allele-specific NFKB1 binding is not detected at the variant or nearby element in colorectal cells.; NFKB1 perturbation does not affect PYDC2 expression in colorectal cells.; The pyroptosis/inflammasome link to PYDC2 is not supported in colorectal cancer models.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA or competitive EMSA with HCT116 nuclear extract and CTCF antibody or recombinant CTCF at chr3:191441666 T>G. | low | yes | No reproducible allele-specific CTCF binding difference at the T/G site. | Alt G shows stronger CTCF binding than ref T. | No CTCF-specific allele difference; any binding would be NFKB1-specific. |
| CTCF ChIP-qPCR at rs13078086 in HCT116 cells. | medium | yes | No CTCF occupancy or allele bias at the variant in HCT116. | CTCF ChIP-qPCR shows occupancy with stronger alt G signal. | No CTCF occupancy or allele bias; NFKB1 is the candidate instead. |
| Colon transverse eQTL lookup for rs13078086 versus PYDC2 and CCDC50 expression, already performed as E09. | low | yes | No colon transverse eQTL for PYDC2 or CCDC50, matching E09. | An allele-specific effect on PYDC2 or CCDC50 expression in colon tissue. | An allele-specific effect on PYDC2 expression in colon tissue. |
| NFKB1 ChIP-qPCR at rs13078086 in HCT116 cells. | medium | no | No NFKB1 occupancy or allele bias at the variant in HCT116. | No NFKB1-specific allele bias; CTCF is the candidate instead. | NFKB1 ChIP-qPCR shows occupancy with stronger alt G signal. |

## Next experiment

The single cheapest experiment that separates the top two chains, H0 and H1, is an allele-specific EMSA or competitive EMSA using HCT116 nuclear extract and CTCF antibody or recombinant CTCF at chr3:191441666 T>G. H1 predicts stronger CTCF binding to alt G, whereas H0 predicts no reproducible allele-specific CTCF binding.

## Investigate calls

- chip_peaks({"tf": "CTCF", "biosample": "HCT116"})
- chip_peaks({"tf": "NFKB1", "biosample": "HCT116"})
- eqtl_lookup({"tissue": "Colon - Transverse"})

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

> No ENCODE CTCF ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT116'. Absence can also mean no CTCF experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:36:09+00:00)

> No ENCODE NFKB1 ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT116'. Absence can also mean no NFKB1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (G) relative to ref (T).
