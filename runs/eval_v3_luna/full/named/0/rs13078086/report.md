# rs13078086 and Colorectal cancer

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 349 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: EBF4 (z -60.28); TFAP2A (z -18.37); TFAP2C (z -18.37); TFAP2E (z -18.37); ETV3 (z 13.11). Diagnostic, not shown to the model: 209 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect of rs13078086 (p = 0.95)

Null chain: no TF-mediated effect of this variant.

Predictions: The T-to-G change does not cause a meaningful TF-mediated regulatory effect; any colorectal-cancer association, if one exists, would need another explanation, such as a linked variant.; There should be no reproducible TF-dependent allelic effect at the endogenous locus or in an appropriate regulatory assay.

Falsified if: Experiments at the endogenous locus show allele-specific TF occupancy and a corresponding, TF-dependent regulatory effect of rs13078086.

### 2. H1: TFAP2E may bind the ref allele more strongly (p = 0.03)

TF TFAP2E (QBiC-SELEX coverage own_model), ref allele binds more; element The variant is outside the nearest reported dELS, 42 bp away; an effect on that element is possible but unshown.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2E is a weak candidate: its own QBiC-SELEX model predicts stronger binding to ref T than alt G, but there is no occupancy evidence; it is favored over related TFAP2A and TFAP2C because it has the highest reported HCT 116 expression and an own-model result. | weak | [E04](#e04), [E09](#e09), [E11](#e11), [E12](#e12), [E13](#e13), [E15](#e15) |
| element | The variant does not overlap a reported cCRE, and the nearest dELS is 42 bp away with activity values that are maxima across biosamples rather than HCT 116-specific evidence. | supported | [E03](#e03), [E04](#e04) |
| gene | PYDC2 is a candidate target by proximity, but no evidence establishes regulation of PYDC2 by this variant or the nearby dELS. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT 116 is a plausible context because TFAP2E is expressed there, but TFAP2E occupancy or variant activity in this cell line is not shown. | weak | [E04](#e04), [E13](#e13), [E15](#e15) |
| phenotype | A colorectal-cancer effect through this chain is unsupported by the supplied evidence. | supported | [E05](#e05), [E06](#e06), [E07](#e07), [E16](#e16), [E17](#e17) |

Predictions: If TFAP2E occupies the site, its occupancy should be greater on T than G; a TFAP2E-dependent allelic regulatory effect would support this chain.; This chain predicts TFAP2E-specific involvement, unlike the EBF4 and ETV3 candidates; it does not establish the direction of any PYDC2 expression change.

Falsified if: Sensitive assays in a relevant context find no TFAP2E occupancy at the locus or no ref-versus-alt occupancy difference.; Changing the allele produces no TFAP2E-dependent regulatory effect in an appropriate assay.

### 3. H2: EBF4 may bind the ref allele more strongly (p = 0.01)

TF EBF4 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant is outside the nearest reported dELS, 42 bp away; an effect on that element is possible but unshown.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | EBF4's own QBiC-SELEX model predicts much stronger binding to ref T than alt G, but EBF4 occupancy is unknown and its expression in HCT 116 is relatively low, so the in-vitro prediction alone is weak evidence for binding in cells. | weak | [E04](#e04), [E09](#e09), [E10](#e10) |
| element | The variant does not overlap a reported cCRE, and no evidence shows that it affects the nearby dELS. | supported | [E03](#e03), [E04](#e04) |
| gene | PYDC2 is a candidate target by proximity, but no evidence establishes regulation of PYDC2 by this variant or the nearby dELS. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT 116 is a possible context because EBF4 is expressed there, although occupancy at the locus has not been shown. | weak | [E04](#e04), [E10](#e10) |
| phenotype | A colorectal-cancer effect through this chain is unsupported by the supplied evidence. | supported | [E05](#e05), [E06](#e06), [E07](#e07), [E16](#e16), [E17](#e17) |

Predictions: If EBF4 occupies the site, its occupancy should be greater on T than G; an EBF4-dependent allelic regulatory effect would support this chain.; This chain predicts EBF4-specific involvement, distinguishing it from the TFAP2E candidate despite their shared ref-favoring direction.

Falsified if: Sensitive assays in a relevant context find no EBF4 occupancy at the locus or no ref-versus-alt occupancy difference.; Changing the allele produces no EBF4-dependent regulatory effect in an appropriate assay.

### 4. H3: ETV3 may bind the alt allele more strongly (p = 0.01)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant is outside the nearest reported dELS, 42 bp away; an effect on that element is possible but unshown.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3 is a very weak candidate: the QBiC-SELEX result predicts modestly stronger binding to alt G using a CIS-BP-mapped ETV5 model, not an ETV3-specific model, and there is no occupancy evidence. | weak | [E04](#e04), [E09](#e09), [E14](#e14) |
| element | The variant does not overlap a reported cCRE, and no evidence shows that it affects the nearby dELS. | supported | [E03](#e03), [E04](#e04) |
| gene | PYDC2 is a candidate target by proximity, but no evidence establishes regulation of PYDC2 by this variant or the nearby dELS. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT 116 is a possible context because ETV3 is expressed there, but occupancy at the variant has not been shown. | weak | [E04](#e04), [E14](#e14) |
| phenotype | A colorectal-cancer effect through this chain is unsupported by the supplied evidence. | supported | [E05](#e05), [E06](#e06), [E07](#e07), [E16](#e16), [E17](#e17) |

Predictions: If ETV3 occupies the site and the mapped-model prediction applies to ETV3, its occupancy should be greater on G than T.; This chain predicts an alt-favoring direction, unlike the TFAP2E and EBF4 candidates; it does not establish the direction of any target-gene expression change.

Falsified if: Sensitive assays in a relevant context find no ETV3 occupancy at the locus or no alt-versus-ref occupancy difference.; Direct ETV3 binding assays do not reproduce the mapped-model direction, or changing the allele produces no ETV3-dependent regulatory effect.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Paired T- and G-allele reporter assay in HCT 116, comparing control cells with TFAP2E-depleted cells. | low | yes | No reproducible TFAP2E-dependent difference between the T and G constructs. | A T-versus-G reporter difference that is reduced by TFAP2E depletion; the direction of reporter activity is not specified by the binding prediction. | No TFAP2E-dependent allelic difference; an EBF4-dependent effect is possible but is not tested by this perturbation. | No TFAP2E-dependent allelic difference; an ETV3-dependent effect is possible but is not tested by this perturbation. |
| Measure allele-resolved TFAP2E, EBF4, and ETV3 occupancy at the endogenous locus in an informative HCT 116 model, using targeted CUT&RUN or equivalent. | medium | yes | No reproducible TF occupancy difference between alleles. | TFAP2E occupancy is detected and favors T over G. | EBF4 occupancy is detected and favors T over G. | ETV3 occupancy is detected and favors G over T. |
| Create isogenic T- and G-allele HCT 116 cells and measure expression of PYDC2 and other nearby genes, with and without TFAP2E perturbation. | high | yes | No reproducible allele-dependent, TFAP2E-dependent expression change. | An allele-dependent expression change that is reduced by TFAP2E perturbation; the direction and target gene remain to be determined. | No TFAP2E-dependent change predicted; an EBF4-dependent change remains possible. | No TFAP2E-dependent change predicted; an ETV3-dependent change remains possible. |

## Next experiment

The lowest-cost test that separates the top two hypotheses (H0 and H1) is a paired T/G reporter assay in HCT 116 with and without TFAP2E depletion. A TFAP2E-dependent allelic difference would support H1, although a reporter result would not by itself establish endogenous target-gene or colorectal-cancer effects.

## Investigate calls

- chip_peaks({"tf": "TFAP2E", "biosample": "HCT116"})
- literature_search({"query": "rs13078086 colorectal cancer"})
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

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr3:191441666:T>G, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 0 of 0 occupied (0 with a strong site), 5 of 85 with unknown occupancy. Left out: 16 TFs assayed in the matching biosample and 557 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element. No ENCODE TF ChIP-seq peak contains this variant in any biosample; QBiC-SELEX changes below have no occupancy support.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EBF4 (EBF1, 2 models; QBiC-SELEX coverage: own model): best model EBF4_FL_TCGATT40NTTG_KK_nitta2015_1_3_7mer (its own model), z -60.28, effect -1.954: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.22 TPM, rank 988 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2A (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -18.37, effect -0.765: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.18 TPM, rank 657 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2C (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -18.37, effect -0.765: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.59 TPM, rank 883 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2E (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (its own model), z -18.37, effect -0.765: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.5 TPM, rank 553 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 13.11, effect 0.251: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 16.34 TPM, rank 334 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.6th, alt 95.3th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:42:51+00:00)

> No ENCODE TFAP2E ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT116'. Absence can also mean no TFAP2E experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e16"></a>**E16** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs13078086%20colorectal%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:37:55+00:00)

> Europe PMC: 0 hits for 'rs13078086 colorectal cancer'; top 0 with PMIDs:

<a id="e17"></a>**E17** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575).
