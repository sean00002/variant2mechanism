# rs13078086 and Colorectal cancer

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 18 model calls; 278 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

**Verdict: undetermined.** The null leads, but nothing tested counts against TFAP2E, EBF4.

Association with the disease (not part of the verdict): GWAS Catalog tested, negative; Open Targets fine-mapping not tested.

Pairwise ranking (Bradley-Terry strengths): H2 0.44, H1 0.30, H3 0.20, H4 0.06. 0 of 6 pairs came out differently in the two orders.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: EBF4 (z -60.28); TFAP2A (z -18.37); TFAP2C (z -18.37); TFAP2E (z -18.37); ETV3 (z 13.11). Diagnostic, not shown to the model: 209 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: No demonstrated TF-mediated effect (p = 0.90)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not show a reproducible allele-dependent TF effect in its relevant chromatin context; it may be noncausal or linked to another causal factor.; Editing the variant will not reproducibly change nearby-gene expression or a colorectal-cancer-related phenotype.

Falsified if: A relevant-cell assay shows allele-specific TF occupancy at the variant, and variant editing reproducibly changes a linked gene's expression and a disease-relevant phenotype.

### 2. H3: TFAP2-family binding is reduced on the alternate allele (p = 0.05)

TF TFAP2E (QBiC-SELEX coverage own_model), ref allele binds more; element The variant is near, but does not overlap, a dELS cCRE; whether either site participates in the same regulatory element is unknown.; gene PYDC2; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger binding to ref than alt using a TFAP2E model. TFAP2A, TFAP2C, and TFAP2E share the mapped-model result, so it does not identify which family member, if any, binds in cells. TFAP2E is the nominated candidate because it has its own model and the highest reported HCT116 expression of the three; occupancy remains unknown. | weak | [E09](#e09), [E11](#e11), [E12](#e12), [E13](#e13) |
| element | The variant is intronic in PYDC2-AS1 and 42 bp from a dELS cCRE, but does not overlap it; a functional connection to that cCRE is unshown. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is a nearby candidate target, but proximity and nearby-gene annotation do not establish regulation by this variant; GTEx found no significant single-tissue eQTL. | weak | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | HCT116 is a candidate context because TFAP2E is expressed there, but ENCODE provides no TFAP2E occupancy evidence at the variant in this cell line. | weak | [E04](#e04), [E13](#e13) |
| phenotype | A colorectal-cancer effect through TFAP2E and PYDC2 is speculative: the supplied results show no PYDC2–colorectal cancer association in Open Targets, and the literature hits do not establish this connection. | missing | [E05](#e05), [E08](#e08), [E15](#e15) |

Predictions: If a TFAP2-family member occupies the variant, its occupancy should favor ref over alt; direct assays would be needed to identify the family member.; Editing T to G could change local regulatory activity and PYDC2 expression in a TFAP2-dependent manner, but the direction of any expression change is not established.

Falsified if: Relevant-cell assays show no TFAP2-family occupancy at the site or no ref-over-alt occupancy difference.; Variant editing produces no TFAP2-dependent effect on local regulatory activity or PYDC2 expression.

### 3. H2: EBF4 binding is reduced on the alternate allele (p = 0.04)

TF EBF4 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant is near, but does not overlap, a dELS cCRE; whether either site participates in the same regulatory element is unknown.; gene PYDC2; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts substantially stronger EBF4 binding to ref than alt in vitro. EBF4 is expressed at low level in HCT116, but it was never assayed by ENCODE, so occupancy at the variant is unknown; the prediction does not establish cellular binding. | weak | [E09](#e09), [E10](#e10) |
| element | The variant is intronic in PYDC2-AS1 and 42 bp from a dELS cCRE, but does not overlap it; a functional connection to that cCRE is unshown. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is a nearby candidate target, but proximity and nearby-gene annotation do not establish regulation by this variant; GTEx found no significant single-tissue eQTL. | weak | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | HCT116 is a candidate context because EBF4 is expressed there, but there is no EBF4 occupancy evidence at the variant in this cell line. | weak | [E04](#e04), [E10](#e10) |
| phenotype | A colorectal-cancer effect through EBF4 and PYDC2 is speculative: the supplied results show no PYDC2–colorectal cancer association in Open Targets, and the literature hits do not establish this connection. | missing | [E05](#e05), [E08](#e08), [E15](#e15) |

Predictions: If EBF4 occupies the variant, its occupancy should favor ref over alt.; Editing T to G could change local regulatory activity and PYDC2 expression, but the direction of any expression change is not established.

Falsified if: Sensitive assays in relevant cells show no EBF4 occupancy at the site or show no ref-over-alt occupancy difference.; Variant editing has no EBF4-dependent effect on local regulatory activity or PYDC2 expression under conditions where EBF4 is present.

### 4. H4: ETV3 binding is modestly increased on the alternate allele (p = 0.01)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant is near, but does not overlap, a dELS cCRE; whether either site participates in the same regulatory element is unknown.; gene PYDC2; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts a modest alt-over-ref binding increase using an ETV5-mapped ETS model, not an ETV3-specific model; this does not establish ETV3 binding in cells. ETV3 is expressed in HCT116, but occupancy at the variant is unknown. | weak | [E09](#e09), [E14](#e14) |
| element | The variant is intronic in PYDC2-AS1 and 42 bp from a dELS cCRE, but does not overlap it; a functional connection to that cCRE is unshown. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is a nearby candidate target, but proximity and nearby-gene annotation do not establish regulation by this variant; GTEx found no significant single-tissue eQTL. | weak | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | HCT116 is a candidate context because ETV3 is expressed there, but there is no ETV3 occupancy evidence at the variant in this cell line. | weak | [E04](#e04), [E14](#e14) |
| phenotype | A colorectal-cancer effect through ETV3 and PYDC2 is speculative: the supplied results show no PYDC2–colorectal cancer association in Open Targets, and the literature hits do not establish this connection. | missing | [E05](#e05), [E08](#e08), [E15](#e15) |

Predictions: If ETV3 occupies the variant, occupancy should favor alt over ref, but the in-vitro prediction comes from an ETV5-mapped model.; Editing T to G could change local regulatory activity and PYDC2 expression in an ETS-factor-dependent manner, but the direction of any expression change is not established.

Falsified if: Relevant-cell assays show no ETV3 occupancy at the site or show occupancy that favors ref rather than alt.; Variant editing produces no ETV3-dependent effect on local regulatory activity or PYDC2 expression.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H3 | H2 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Measure allele-specific TFAP2E occupancy at the variant in HCT116 with targeted CUT&RUN or CUT&Tag. | medium | yes | No reproducible TFAP2E occupancy or allele-specific difference is expected. | TFAP2E occupancy favoring ref over alt is predicted. | No specific TFAP2E occupancy is predicted; this chain instead predicts ref-favored EBF4 binding if EBF4 occupies the site. | No specific TFAP2E occupancy is predicted; this chain instead predicts alt-favored ETV3 binding if ETV3 occupies the site. |
| Edit the variant in isogenic HCT116 cells and measure PYDC2 expression, with and without perturbing the candidate TF. | high | no | No reproducible variant-dependent PYDC2 expression effect is expected. | A variant-dependent PYDC2 expression effect that depends on TFAP2E is possible, but its direction is not established. | A variant-dependent PYDC2 expression effect that depends on EBF4 is possible, but its direction is not established. | A variant-dependent PYDC2 expression effect that depends on ETV3 is possible, but its direction is not established. |
| Test allele-specific regulatory activity of the local sequence in a reporter assay, with candidate-TF perturbation. | medium | yes | No reproducible allele-dependent, TF-dependent reporter effect is expected. | If TFAP2E acts through the sequence, the alleles may differ in a TFAP2E-dependent manner; activity direction is unknown. | If EBF4 acts through the sequence, the alleles may differ in an EBF4-dependent manner; activity direction is unknown. | If ETV3 acts through the sequence, the alleles may differ in an ETV3-dependent manner; activity direction is unknown. |

## Next experiment

Perform targeted TFAP2E CUT&RUN or CUT&Tag in HCT116 and quantify occupancy at the variant, ideally comparing ref and alt alleles. This is the cheapest proposed cellular test that directly distinguishes the top-ranked null hypothesis from H3; a positive ref-favored signal would support, but not by itself prove, the full regulatory chain.

## Refinement rounds

Stopped: round 1 left the top chain and the grades of its links unchanged.

### Round 1

- gene_disease({"gene": "PYDC2"}) for H2.phenotype, ran as [E15](#e15). Expected: If Open Targets reports colorectal-cancer association evidence for PYDC2, this would support a disease connection for the proposed target gene and raise H2 modestly, without proving that this variant regulates PYDC2. If no association is reported, it adds no support.
- gene_dependency({"gene": "PYDC2"}) for H2.phenotype, ran as [E16](#e16) (not tested). Expected: If PYDC2 shows a colorectal-lineage CRISPR dependency, that would support a possible cancer-relevant role for the gene and modestly strengthen the proposed phenotype link; if it is not a dependency, this would not rule out a regulatory or disease effect.

- Result of gene_disease({"gene":"PYDC2"}): E15: Open Targets reports no association between PYDC2 and colorectal cancer. This adds no support for the proposed disease link. (as expected: yes)
- Result of gene_dependency({"gene":"PYDC2"}): E16: DepMap CRISPRGeneEffect has no data for PYDC2, so dependency was not tested and the result is uninformative. (as expected: unclear)

Chains after revision: null 0.90; TFAP2E 0.05; EBF4 0.04; ETV3 0.01. Link grades changed: none.

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

<a id="e03"></a>**E03** ccre_lookup (tested, negative), ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:05+00:00)

> No cCRE overlaps the variant; nearest is EH38E2269392 (dELS) 42 bp away.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2269392 dELS: DNase z 3.5, H3K27ac z 1.8, H3K4me3 z 1.5, CTCF z 1.5; nearby genes AC073365.1, PYDC2, CCDC50
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy (tested, negative), ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> No ENCODE TF ChIP-seq peak contains chr3:191441666:T>G in any biosample. In the matching biosample HCT116: 0 peaks from 0 factors. No cCRE contains the variant. Of the TFs with a binding model, 16 were assayed in the matching biosample and 557 only elsewhere, all without a peak here; 536 were never assayed.

<a id="e05"></a>**E05** gwas_lookup (tested, negative), GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs13078086&size=100; retrieved 2026-10-25T17:32:10+00:00)

> 0 GWAS Catalog associations for rs13078086. The Catalog lists reported associations only, often just the lead variant of each signal, so this is weak evidence against an association.

<a id="e06"></a>**E06** finemap_lookup (not tested), Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:09+00:00)

> Open Targets has no record of 3_191441666_T_G, so it says nothing about fine-mapping here.

<a id="e07"></a>**E07** eqtl_lookup (tested, negative), GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> GTEx v8 tested chr3_191441666_T_G_b38: no significant single-tissue eQTL in any tissue.

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

<a id="e15"></a>**E15** gene_disease (tested, negative), Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575); no evidence there links them.

<a id="e16"></a>**E16** gene_dependency (not tested), DepMap CRISPRGeneEffect (local files; retrieved local)

> DepMap's CRISPR screen has no data for PYDC2, so it says nothing about dependency here.
