# rs13078086 and Colorectal cancer

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.47 over 7 model calls; 144 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: No TF-mediated effect: passenger intronic variant or linkage to a different causal variant (p = 0.74)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific binding in EMSA or allele-specific ChIP at chr3:191441666 in HCT 116 or colon epithelium.; No allelic imbalance in MPRA/luciferase for the 200 bp window around the variant.; No colon eQTL for PYDC2, CCDC50 or PYDC2-AS1 appears with larger sample sizes; no genome-wide significant colorectal cancer association emerges.

Falsified if: A reproducible allele-specific binding or reporter-activity difference between T and G is demonstrated.; Allelic base editing in colon cells or organoids changes expression of any neighbouring gene.; A colon eQTL or a credible colorectal cancer association for rs13078086 is reported.

### 2. H3: Loss of an intestinal homeobox (CDX2) site in the PYDC2-AS1 intron lowers PYDC2/PYDC2-AS1 expression (p = 0.18)

TF CDX2 (stated coverage not_checked; registry own_model), ref allele binds more; element PYDC2-AS1 intron, 42 bp from EH38E2269392 (dELS); gene PYDC2; cell type Colonic epithelium / HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The T allele is proposed to form an AT-rich CDX-family motif lost on T>G; within that homeobox specificity group CDX2 is picked as the intestine-restricted member. No motif scan, ChIP or QBiC-SELEX evidence was available for this site, so the binding claim and its direction are currently unsupported; coverage is not_checked. | missing | none |
| element | The variant sits in a PYDC2-AS1 intron immediately beside a DNase-accessible enhancer-like cCRE, but it overlaps no cCRE or regulatory feature itself and sits at a non-conserved position (GERP -1.82). | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the closest protein-coding TSS (19.5 kb) and is in the cCRE's nearby-gene list, and the variant lies in its antisense transcript; this is proximity only, and no GTEx eQTL supports it. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | Colon specificity is asserted from CDX2's known intestinal restriction; no cited data show CDX2 occupancy or element activity in HCT 116 or colon. | missing | none |
| phenotype | A PYDC2-inflammasome route to colorectal cancer is not supported by the literature search, whose hits concern other genes and cancers, and no GWAS or Open Targets signal exists. | missing | [E06](#e06), [E04](#e04), [E05](#e05) |

Predictions: A CDX/homeobox motif overlaps the variant in a PWM/QBiC scan, with T preferred.; Allelic imbalance in CDX2 ChIP favouring T, lost after CDX2 knockdown.; Base editing in colon organoids changes PYDC2/PYDC2-AS1 rather than CCDC50.

Falsified if: No CDX-family motif is affected by T>G.; CDX2 ChIP/CUT&RUN in colon cells shows no binding at the locus.; PYDC2 and PYDC2-AS1 expression are unchanged by allelic editing.

### 3. H1: Weakened CTCF binding beside the distal enhancer alters local insulation and CCDC50/PYDC2 expression (p = 0.04)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element Sequence 42 bp from EH38E2269392 (dELS), inside the PYDC2-AS1 intron; gene CCDC50; cell type Colorectal carcinoma epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF was the only TF with any signal near this element (CTCF z 1.5 at EH38E2269392, a maximum over biosamples), but ENCODE ChIP-seq shows no CTCF peak containing the variant and none within 100 bp, so there is no evidence of CTCF occupancy here; the proposed stronger binding on T is unsupported and QBiC-SELEX coverage for CTCF was not checked. | missing | [E03](#e03), [E08](#e08) |
| element | The variant lies outside every cCRE; the nearest enhancer-like element (DNase z 3.5, H3K27ac z 1.8, biosample maxima only) is 42 bp away, so any boundary or looping role is speculative. | weak | [E03](#e03), [E01](#e01) |
| gene | CCDC50 is listed as a nearby gene of EH38E2269392 and sits 112.6 kb downstream, but no eQTL links the variant to it in any GTEx tissue, including colon. | missing | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | No biosample-specific data show this element is active in HCT 116 or colon; the DepMap context is given but untested here. | missing | [E03](#e03) |
| phenotype | No GWAS Catalog or Open Targets evidence connects this variant to colorectal cancer, so any CCDC50-mediated risk effect is hypothetical. | missing | [E04](#e04), [E05](#e05) |

Predictions: A CTCF motif overlapping the variant would be scored by PWM/QBiC, with T preferred.; Allele-specific CTCF ChIP or CUT&RUN signal at this position in a colon line with the heterozygous genotype.; Allelic editing changes CCDC50 rather than PYDC2, and perturbs a local loop detectable by 4C/Hi-C.

Falsified if: No CTCF motif overlaps chr3:191441666 in a PWM/QBiC scan.; CUT&RUN or deeper CTCF ChIP in colon cells shows no occupancy at this site (E08 already argues against it).; CRISPR deletion of the adjacent element leaves CCDC50 unchanged.

### 4. H2: Alt allele creates a TCF7L2 (Wnt effector) site feeding the adjacent enhancer (p = 0.04)

TF TCF7L2 (stated coverage not_checked; registry mapped), alt allele binds more; element Sequence adjacent to EH38E2269392 (dELS); gene CCDC50; cell type Wnt-active colorectal carcinoma epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 was chosen within the TCF/LEF specificity group as the dominant colorectal family member, but this rests on prior knowledge only: ENCODE shows no TCF7L2 peak containing the variant and none within 100 bp, and no motif scan or QBiC model was consulted. | missing | [E09](#e09), [E01](#e01) |
| element | The nearest enhancer-like cCRE is 42 bp away with accessibility and H3K27ac in some biosample; the variant itself is in no cCRE. | weak | [E03](#e03) |
| gene | CCDC50 appears only as a nearby-gene annotation of that cCRE at 112.6 kb; PYDC2 is closer (19.5 kb) and no eQTL distinguishes them. | missing | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | No cited evidence demonstrates Wnt-dependent activity of this element in HCT 116; the Wnt context is assumed from the cell line's known biology. | missing | none |
| phenotype | No GWAS or Open Targets association supports a colorectal cancer effect. | missing | [E04](#e04), [E05](#e05) |

Predictions: A TCF/LEF motif is created by T>G in a motif scan.; Reporter activity higher for G specifically in Wnt-active colorectal lines, abolished by beta-catenin or TCF7L2 knockdown.; Allele-specific TCF7L2 occupancy favouring G in a deeper or different colorectal TCF7L2 experiment.

Falsified if: No TCF/LEF motif is created by T>G.; No allelic difference, or T stronger, in colorectal reporter assays.; TCF7L2 occupancy remains absent in colorectal lines (E09 already argues against it).

## Prediction matrix

| Test | Cost | Separates top two | H0 | H3 | H1 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| QBiC-SELEX / PWM scan of the 25 bp window around chr3:191441666 for all TF models (which TF families change, and in which direction) | low | yes | No substantial predicted binding change for any TF expressed in colon, or changes only for TFs absent from colon | CDX/homeobox AT-rich model loses binding on T>G (T preferred) | CTCF-family model loses binding on T>G (T preferred) | TCF/LEF model gains binding on T>G (G preferred) |
| CDX2 ChIP-seq / CUT&RUN peak lookup at chr3:191441666 in HCT 116 or colon tissue | existing data | yes | No CDX2 peak at the variant | CDX2 peak contains or abuts the variant | No CDX2 peak required | No CDX2 peak required |
| CTCF ChIP-seq peak lookup in HCT 116 (already run, E08) | existing data | no | No peak (observed) | No peak expected | Peak expected; none found, so H1 is largely falsified | No peak expected |
| TCF7L2 ChIP-seq peak lookup in HCT 116 (already run, E09) | existing data | no | No peak (observed) | No peak expected | No peak expected | Peak expected; none found, so H2 is largely falsified |
| GTEx colon eQTL lookup for chr3_191441666_T_G (already run, E07) | existing data | no | No significant eQTL (observed), consistent with null | PYDC2/PYDC2-AS1 eQTL expected; absent (may be hidden by low colon expression) | CCDC50 eQTL expected; absent | CCDC50 eQTL expected; absent |
| Luciferase/MPRA of the 200 bp window, T versus G, in HCT 116 and colon organoids | medium | yes | No allelic difference | T higher, dependent on CDX2 | Little difference in episomal reporter (insulator effects are chromatin-dependent) | G higher, dependent on Wnt/TCF7L2 |
| Allelic base editing (T>G) in colon organoids, then RNA-seq of PYDC2, PYDC2-AS1 and CCDC50 | high | yes | No expression change | PYDC2/PYDC2-AS1 decreases | CCDC50 changes | CCDC50 increases |

## Next experiment

Run a QBiC-SELEX / PWM scan of the 25 bp window around chr3:191441666 for all TF models. It is the cheapest test that separates the top two chains: the null predicts no meaningful predicted binding change for a colon-expressed TF, while H3 requires a CDX/homeobox site with the T allele preferred (and would also check the CTCF and TCF/LEF options already undercut by E08 and E09).

## Investigate calls

- eqtl_lookup({"tissue": null})
- chip_peaks({"tf": "CTCF", "biosample": null})
- chip_peaks({"tf": "TCF7L2", "biosample": null})

## Flags

- literature_fallback: no hits for 'rs13078086 AND PYDC2 AND "colorectal cancer"'; dropped the rsID

Citation support: 0.80 of links cite only evidence that passed every check.

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

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38. NES is the effect of the alt allele (G) relative to ref (T).

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:26:42+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr3:191441666:T>G. Absence can also mean no CTCF experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:26:42+00:00)

> No ENCODE TCF7L2 ChIP-seq peak contains chr3:191441666:T>G. Absence can also mean no TCF7L2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.
