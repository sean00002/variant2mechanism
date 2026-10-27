# rs13078086 and Colorectal cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 136 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: Null: no TF-mediated effect of rs13078086 (p = 0.99)

Null chain: no TF-mediated effect of this variant.

Predictions: There will be no reproducible allele-specific TF binding effect attributable to this variant and no variant-dependent regulatory effect on PYDC2 or CCDC50.; Any colorectal cancer association, if one exists, is not established by the supplied evidence and could reflect another variant or mechanism.

Falsified if: The variant is shown to cause reproducible allele-specific TF binding and a linked, variant-dependent effect on a regulatory element and target gene.

### 2. H1: Low-confidence CTCF–nearby element–PYDC2 model: alt binding (p = 0.00)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element Nearby dELS cCRE EH38E2269392; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This speculative model proposes that CTCF binds the alt G allele more strongly than the ref T allele. The supplied evidence does not support that direction: no CTCF peak overlaps the variant, and no CTCF QBiC-SELEX result is supplied. The CTCF signal reported for the nearby cCRE is not evidence of occupancy at the variant. | missing | [E03](#e03), [E04](#e04) |
| element | The variant might influence dELS cCRE EH38E2269392, but it is 42 bp away and does not overlap the cCRE. | weak | [E03](#e03) |
| gene | PYDC2 is a speculative target because it is relatively close to the variant and is listed near the cCRE; no evidence establishes that the cCRE regulates PYDC2. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT 116 is the expression context proposed for this model, but no variant-overlapping CTCF peak or HCT 116-specific activity of the nearby cCRE is shown. | missing | [E03](#e03), [E04](#e04) |
| phenotype | A PYDC2 regulatory effect contributing to colorectal cancer is only a hypothesis; the supplied evidence does not connect this variant or PYDC2 to the disease. | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E09](#e09), [E10](#e10) |

Predictions: A direct binding assay using the variant sequence would show greater CTCF binding to G than T.; If the proposed regulatory chain is correct, editing T to G in HCT 116 would produce a reproducible change in PYDC2 expression, dependent on the nearby element.

Falsified if: A direct allele-specific binding assay finds no CTCF binding difference or finds greater binding to T.; Precise T-to-G editing produces no reproducible PYDC2 expression change, or the change is unaffected by perturbation of the nearby element.

### 3. H2: Low-confidence CTCF–nearby element–CCDC50 model: ref binding (p = 0.00)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element Nearby dELS cCRE EH38E2269392; gene CCDC50; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This distinct speculative model proposes that CTCF binds the ref T allele more strongly than the alt G allele. The supplied evidence does not support that direction: no CTCF peak overlaps the variant, and no CTCF QBiC-SELEX result is supplied. The CTCF signal reported for the nearby cCRE is not evidence of occupancy at the variant. | missing | [E03](#e03), [E04](#e04) |
| element | The variant might influence dELS cCRE EH38E2269392, but it is 42 bp away and does not overlap the cCRE. | weak | [E03](#e03) |
| gene | CCDC50 is a speculative target because it is listed near the cCRE and is within the broader variant neighborhood; no evidence establishes that the cCRE regulates CCDC50. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT 116 is the expression context proposed for this model, but no variant-overlapping CTCF peak or HCT 116-specific activity of the nearby cCRE is shown. | missing | [E03](#e03), [E04](#e04) |
| phenotype | A CCDC50 regulatory effect contributing to colorectal cancer is only a hypothesis; the supplied evidence does not connect this variant or CCDC50 to the disease. | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E09](#e09), [E11](#e11) |

Predictions: A direct binding assay using the variant sequence would show greater CTCF binding to T than G.; If the proposed regulatory chain is correct, editing T to G in HCT 116 would produce a reproducible change in CCDC50 expression, dependent on the nearby element.

Falsified if: A direct allele-specific binding assay finds no CTCF binding difference or finds greater binding to G.; Precise T-to-G editing produces no reproducible CCDC50 expression change, or the change is unaffected by perturbation of the nearby element.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| In vitro allele-specific CTCF binding assay using otherwise identical oligonucleotides carrying T or G | low | yes | No reproducible allele-specific CTCF binding difference. | Greater CTCF binding to G than T. | Greater CTCF binding to T than G. |
| Precise T-to-G editing in HCT 116 followed by expression measurement of PYDC2 and CCDC50 | medium | no | No reproducible expression change attributable to the edit in either gene. | A reproducible expression change in PYDC2; this test alone would not establish that CTCF or the nearby cCRE mediates it. | A reproducible expression change in CCDC50; this test alone would not establish that CTCF or the nearby cCRE mediates it. |
| After editing, perturb EH38E2269392 and measure the proposed target-gene response | high | no | No variant-dependent target-gene effect for perturbation to reduce or eliminate. | The PYDC2 expression effect of the edit is reduced or lost when the nearby element is perturbed. | The CCDC50 expression effect of the edit is reduced or lost when the nearby element is perturbed. |

## Next experiment

Run the low-cost in vitro allele-specific CTCF binding assay with matched T- and G-allele oligonucleotides. It directly distinguishes the top two chains’ opposite binding-direction predictions, although a positive result would not by itself establish occupancy in HCT 116 or the proposed element-to-gene and disease links.

## Investigate calls

- literature_search({"query": "\"rs13078086\" OR \"chr3:191441666\" colorectal cancer"})
- gene_disease({"gene": "PYDC2"})
- gene_disease({"gene": "CCDC50"})

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

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22rs13078086%22%20OR%20%22chr3%3A191441666%22%20colorectal%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:27:53+00:00)

> Europe PMC: 616488 hits for '"rs13078086" OR "chr3:191441666" colorectal cancer'; top 6 with PMIDs:
> PMID 42684553 (2026): Spermidine in Colorectal cancer: friend or foe?
> PMID 42763869 (2027): A Straightforward and Reliable Mouse Model of Colorectal Cancer by Orthotopic Transplantation.
> PMID 42892023 (2026): Operability and survival in resectable colorectal cancer: A retrospective propensity score-matched study impact of operability in colorectal cancer.
> PMID 42617478 (2026): Microparticles and colorectal cancer.
> PMID 42705241 (2026): [Colorectal Cancer].
> PMID 42827107 (2026): Single-cell epigenomics of colorectal cancer.

<a id="e10"></a>**E10** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575).

<a id="e11"></a>**E11** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T13:27:56+00:00)

> Open Targets: no association between CCDC50 and colorectal cancer (MONDO_0005575).
