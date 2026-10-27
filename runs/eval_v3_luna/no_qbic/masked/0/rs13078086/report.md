# rs13078086 and Colorectal cancer

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 114 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: No TF-mediated effect (p = 0.80)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not produce a reproducible allele-dependent TF-binding and regulatory effect. Any disease association, if established, would need another explanation.

Falsified if: A reproducible allele-dependent TF effect at this variant is demonstrated and linked to altered regulation of a target gene in a relevant cell context.

### 2. H1: Testable CTCF–PYDC2 hypothesis, with greater binding to G (p = 0.10)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element Nearby candidate dELS cCRE EH38E2269392, 42 bp from but not overlapping the variant; gene PYDC2; cell type HCT 116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is a candidate to test because the nearby cCRE has a CTCF signal in the maximum-over-biosamples summary, but this does not show CTCF occupancy at the variant. The supplied evidence contains no QBiC-SELEX result for this variant; greater binding to G is an unsupported hypothesis. | missing | [E03](#e03), [E04](#e04) |
| element | EH38E2269392 is a nearby dELS candidate element, but it is 42 bp from the variant, does not overlap it, and its activity in HCT 116 is not established. | weak | [E03](#e03) |
| gene | PYDC2 is a candidate target because it is 19.5 kb from the variant and is listed near the cCRE; no variant-to-element or element-to-gene regulatory link is shown. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT 116 is the stated expression context, but the supplied evidence does not establish CTCF occupancy or variant-dependent regulation there; no CTCF peak over the variant was reported in HCT 116. | weak | [E04](#e04) |
| phenotype | A PYDC2-mediated colorectal cancer effect is speculative. The supplied sources report no variant association, significant eQTL, PYDC2–colorectal cancer association, or direct literature link supporting this chain. | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E08](#e08), [E09](#e09), [E11](#e11) |

Predictions: If this chain is correct, an allele-specific CTCF-binding assay should show greater binding to G than T.; Variant perturbation in HCT 116 should alter PYDC2 regulation; this chain predicts PYDC2 rather than CCDC50 as the relevant target.

Falsified if: A suitable allele-specific assay finds no greater CTCF binding to G than T, or finds greater binding to T.; Variant perturbation in a relevant context has no effect on PYDC2 regulation while assay controls work.

### 3. H2: Testable CTCF–CCDC50 hypothesis, with greater binding to T (p = 0.10)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element Nearby candidate dELS cCRE EH38E2269392, 42 bp from but not overlapping the variant; gene CCDC50; cell type HCT 116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is a candidate to test because the nearby cCRE has a CTCF signal in the maximum-over-biosamples summary, but this does not show CTCF occupancy at the variant. The supplied evidence contains no QBiC-SELEX result for this variant; greater binding to T is an unsupported hypothesis. | missing | [E03](#e03), [E04](#e04) |
| element | EH38E2269392 is a nearby dELS candidate element, but it is 42 bp from the variant, does not overlap it, and its activity in HCT 116 is not established. | weak | [E03](#e03) |
| gene | CCDC50 is a candidate target because it is listed near the cCRE and is 112.6 kb from the variant; neither proximity nor the cCRE annotation establishes that the variant or element regulates CCDC50. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT 116 is the stated expression context, but the supplied evidence does not establish CTCF occupancy or variant-dependent regulation there; no CTCF peak over the variant was reported in HCT 116. | weak | [E04](#e04) |
| phenotype | A CCDC50-mediated colorectal cancer effect is speculative. The supplied sources report no variant association, significant eQTL, CCDC50–colorectal cancer association, or direct literature link supporting this chain. | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E08](#e08), [E10](#e10), [E11](#e11) |

Predictions: If this chain is correct, an allele-specific CTCF-binding assay should show greater binding to T than G.; Variant perturbation in HCT 116 should alter CCDC50 regulation; this chain predicts CCDC50 rather than PYDC2 as the relevant target.

Falsified if: A suitable allele-specific assay finds no greater CTCF binding to T than G, or finds greater binding to G.; Variant perturbation in a relevant context has no effect on CCDC50 regulation while assay controls work.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| In vitro CTCF binding assay using matched T- and G-allele DNA probes | low | yes | No reproducible allele-dependent CTCF binding difference. | Greater CTCF binding to the G probe than the T probe. | Greater CTCF binding to the T probe than the G probe. |
| Allele-specific CTCF occupancy assay at the variant in HCT 116, if a suitable heterozygous cell line or edited model is available | medium | yes | No reproducible allele-specific CTCF occupancy at the variant. | Greater CTCF occupancy on G-bearing than T-bearing alleles. | Greater CTCF occupancy on T-bearing than G-bearing alleles. |
| Precisely edit T to G and G to T in an isogenic HCT 116 model, then measure CTCF occupancy and PYDC2 and CCDC50 expression | high | no | No reproducible variant-dependent CTCF occupancy or expression change in either candidate gene. | G increases CTCF occupancy and produces a reproducible PYDC2 regulatory change. | T increases CTCF occupancy and produces a reproducible CCDC50 regulatory change. |

## Next experiment

Run the low-cost matched-allele CTCF binding assay first. It tests the unsupported direction in H1 against the null and can also distinguish H1 from H2; a positive result would still need endogenous occupancy and regulatory validation.

## Investigate calls

- gene_disease({"gene": "PYDC2"})
- gene_disease({"gene": "CCDC50"})
- literature_search({"query": "chr3:191441666 T G PYDC2 CCDC50 colorectal cancer regulatory variant"})

## Flags

- none

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

<a id="e09"></a>**E09** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575).

<a id="e10"></a>**E10** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T13:27:56+00:00)

> Open Targets: no association between CCDC50 and colorectal cancer (MONDO_0005575).

<a id="e11"></a>**E11** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr3%3A191441666%20T%20G%20PYDC2%20CCDC50%20colorectal%20cancer%20regulatory%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:23:04+00:00)

> Europe PMC: 0 hits for 'chr3:191441666 T G PYDC2 CCDC50 colorectal cancer regulatory variant'; top 0 with PMIDs:
