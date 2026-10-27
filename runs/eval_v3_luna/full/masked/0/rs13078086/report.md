# rs13078086 and Colorectal cancer

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 115 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: EBF4 (z -60.28); TFAP2A (z -18.37); TFAP2C (z -18.37); TFAP2E (z -18.37); ETV3 (z 13.11). Diagnostic, not shown to the model: 209 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.94)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant has no material TF-mediated regulatory effect. Any disease association, if present, could reflect another variant or cause.; Tests of the variant in relevant cells will not establish a reproducible allele-specific TF effect connected to a target gene.

Falsified if: Experiments show that this variant changes occupancy of a specific TF and that the change alters a relevant target gene's expression or regulation.

### 2. H1: Candidate TFAP2E binding change near a dELS element (p = 0.04)

TF TFAP2E (QBiC-SELEX coverage own_model), ref allele binds more; element A possible regulatory element 42 bp away, EH38E2269392; the variant does not overlap it.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | If TFAP2E occupies the variant, QBiC-SELEX predicts stronger binding to ref T than alt G. This is an in-vitro prediction without occupancy support. TFAP2A and TFAP2C have the same reported mapped-model change, so the model does not distinguish these related factors; TFAP2E is retained as the candidate because the listed prediction uses its own model and it has the highest reported expression of the three in HCT 116. | weak | [E04](#e04), [E11](#e11), [E12](#e12), [E13](#e13), [E15](#e15) |
| element | A nearby dELS cCRE could be relevant, but it is 42 bp from the variant and its reported activity is a maximum across biosamples, not evidence of activity or a variant effect in HCT 116. | weak | [E03](#e03) |
| gene | PYDC2 is a proximity-based candidate target, not a demonstrated target of the nearby cCRE or variant; no significant variant eQTL is reported for colon tissues. | weak | [E02](#e02), [E03](#e03), [E07](#e07), [E16](#e16) |
| cell_type | HCT 116 is a plausible context because TFAP2E is expressed there, but no variant-overlapping TFAP2E occupancy or regulatory effect is shown. | weak | [E04](#e04), [E13](#e13), [E15](#e15) |
| phenotype | A TFAP2E–PYDC2 contribution to colorectal cancer is speculative; the supplied evidence reports no variant association and no PYDC2–colorectal-cancer association. | missing | [E05](#e05), [E06](#e06), [E17](#e17) |

Predictions: If this chain is correct, TFAP2E should occupy the variant in relevant cells and show greater binding to ref than alt; perturbing the variant or TFAP2E should affect a linked regulatory readout.; The binding-model result alone does not predict whether PYDC2 expression rises or falls, because stronger TF binding need not mean greater transcriptional activity.

Falsified if: Sensitive assays find no TFAP2E occupancy at the variant in relevant cells, or find no reproducible ref-favored binding.; Perturbing the variant or the proposed element has no effect on a linked regulatory readout or PYDC2 expression.

### 3. H2: Candidate EBF4 binding change near a dELS element (p = 0.01)

TF EBF4 (QBiC-SELEX coverage own_model), ref allele binds more; element A possible regulatory element 42 bp away, EH38E2269392; the variant does not overlap it.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | If EBF4 occupies the variant, its QBiC-SELEX model predicts substantially stronger binding to ref T than alt G. This is an in-vitro prediction; EBF4 occupancy at the site is unknown and it was not assayed by ENCODE. | weak | [E04](#e04), [E10](#e10) |
| element | A nearby dELS cCRE could be relevant, but it does not overlap the variant and its reported activity is not specific to HCT 116. | weak | [E03](#e03) |
| gene | PYDC2 is a proximity-based candidate target; the evidence does not establish that the variant or nearby cCRE regulates it, and no significant variant eQTL is reported for colon tissues. | weak | [E02](#e02), [E03](#e03), [E07](#e07), [E16](#e16) |
| cell_type | EBF4 is expressed in HCT 116, but there is no evidence of its occupancy or regulatory action at this site in that cell line. | weak | [E04](#e04), [E10](#e10) |
| phenotype | An EBF4–PYDC2 contribution to colorectal cancer is speculative; the supplied evidence reports no variant association and no PYDC2–colorectal-cancer association. | missing | [E05](#e05), [E06](#e06), [E17](#e17) |

Predictions: If this chain is correct, EBF4 should occupy the variant and show greater binding to ref than alt; an EBF4-dependent regulatory effect should be detectable.; The QBiC-SELEX result does not determine the direction of any expression effect.

Falsified if: Sensitive assays find no EBF4 occupancy at the variant in relevant cells, or find no reproducible ref-favored binding.; EBF4 or variant perturbation has no effect on the proposed regulatory readout or PYDC2 expression.

### 4. H3: Candidate ETV3 binding change near a dELS element (p = 0.01)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element A possible regulatory element 42 bp away, EH38E2269392; the variant does not overlap it.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | If ETV3 occupies the variant, the QBiC-SELEX entry predicts stronger binding to alt G than ref T. It uses a CIS-BP-mapped ETV5 model, so the prediction is uncertain as to TF-specific attribution; no occupancy at the variant is reported. | weak | [E04](#e04), [E14](#e14) |
| element | A nearby dELS cCRE could be relevant, but it is 42 bp from the variant and its reported activity is not specific to HCT 116. | weak | [E03](#e03) |
| gene | PYDC2 is a proximity-based candidate target, not a demonstrated target of the variant or cCRE; no significant variant eQTL is reported for colon tissues. | weak | [E02](#e02), [E03](#e03), [E07](#e07), [E16](#e16) |
| cell_type | ETV3 is expressed in HCT 116, but its occupancy or regulatory action at this site has not been shown. | weak | [E04](#e04), [E14](#e14) |
| phenotype | An ETV3–PYDC2 contribution to colorectal cancer is speculative; the supplied evidence reports no variant association and no PYDC2–colorectal-cancer association. | missing | [E05](#e05), [E06](#e06), [E17](#e17) |

Predictions: If this chain is correct, ETV3 should occupy the variant and show greater binding to alt than ref; an ETV3-dependent regulatory effect should be detectable.; The QBiC-SELEX result does not determine the direction of any expression effect.

Falsified if: Sensitive assays find no ETV3 occupancy at the variant in relevant cells, or find no reproducible alt-favored binding.; ETV3 or variant perturbation has no effect on the proposed regulatory readout or PYDC2 expression.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TFAP2E CUT&RUN-qPCR (or targeted CUT&Tag) around the variant in HCT 116, with the cell-line genotype confirmed. | low | yes | No reproducible TFAP2E occupancy with a ref-favored allelic imbalance. | TFAP2E occupancy is detected, with greater occupancy on the ref allele. | No specific prediction of TFAP2E occupancy; this chain instead predicts EBF4 occupancy with ref favored. | No specific prediction of TFAP2E occupancy; this chain instead predicts ETV3 occupancy with alt favored. |
| Test whether editing the variant changes PYDC2 expression in HCT 116, using matched ref-to-alt and alt-to-ref edits and appropriate controls. | medium | yes | No reproducible PYDC2 expression change attributable to the variant. | A reproducible PYDC2 expression change follows the edit; its direction is not specified by the binding prediction. | A reproducible PYDC2 expression change follows the edit if the proposed EBF4 chain is functional; its direction is unspecified. | A reproducible PYDC2 expression change follows the edit if the proposed ETV3 chain is functional; its direction is unspecified. |
| Measure allele-specific occupancy of EBF4 and ETV3 at the variant in HCT 116 using TF-specific CUT&RUN or CUT&Tag. | medium | no | No reproducible variant-centered occupancy with the predicted allelic imbalance. | No specific prediction of EBF4 or ETV3 occupancy. | EBF4 occupancy is detected, with greater occupancy on the ref allele. | ETV3 occupancy is detected, with greater occupancy on the alt allele. |

## Next experiment

Perform allele-specific TFAP2E CUT&RUN-qPCR (or targeted CUT&Tag) around the variant in HCT 116, after confirming the cell-line genotype. It is the lowest-cost listed test that directly distinguishes the leading TFAP2E chain from the null by testing for occupancy and the predicted ref-favored allelic imbalance.

## Investigate calls

- chip_peaks({"tf": "TFAP2E", "biosample": "HCT 116"})
- eqtl_lookup({"tissue": "Colon - Sigmoid"})
- gene_disease({"gene": "PYDC2"})

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

> No ENCODE TFAP2E ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT 116'. Absence can also mean no TFAP2E experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e16"></a>**E16** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38 in tissues matching 'Colon - Sigmoid'. NES is the effect of the alt allele (G) relative to ref (T).

<a id="e17"></a>**E17** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575).
