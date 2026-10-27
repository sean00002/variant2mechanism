# rs13078086 and Colorectal cancer

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 108 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: EBF4 (z -60.28); TFAP2A (z -18.37); TFAP2C (z -18.37); TFAP2E (z -18.37); ETV3 (z 13.11). Diagnostic, not shown to the model: 209 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.96)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not produce a reproducible TF-dependent allelic effect in the relevant cells. Any disease association, if present, would require another explanation.

Falsified if: A variant-dependent TF occupancy or regulatory effect is demonstrated in cells and linked to a target-gene change.

### 2. H1: TFAP2E binding change with a possible nearby regulatory effect (p = 0.03)

TF TFAP2E (QBiC-SELEX coverage own_model), ref allele binds more; element A possible nearby regulatory element, including the dELS cCRE 42 bp away; the variant does not overlap the cCRE.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2E is a tentative candidate: its own QBiC-SELEX model predicts stronger in-vitro binding to ref T than alt G. Related TFAP2 factors have the same mapped-model prediction; TFAP2E is favored here because it has an own-model result and the highest reported HCT 116 expression among TFAP2A, TFAP2C, and TFAP2E. Occupancy at the variant is unestablished. | weak | [E11](#e11), [E12](#e12), [E13](#e13) |
| element | The nearby dELS cCRE is a possible regulatory context, but it is 42 bp from the variant and its reported activity is a maximum across biosamples, not evidence that the variant affects it in HCT 116. | weak | [E03](#e03) |
| gene | PYDC2 is a tentative candidate target based on proximity to the variant and its inclusion among genes near the cCRE; regulation of PYDC2 by this variant or cCRE has not been shown. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT 116 is a plausible context because TFAP2E is expressed there, but expression alone does not establish occupancy or regulatory activity at this site. | supported | [E13](#e13) |
| phenotype | A TFAP2E-to-PYDC2 contribution to colorectal cancer remains speculative; the supplied evidence does not establish this path or a direction of expression or disease effect. | missing | none |

Predictions: If this chain is correct, a variant-dependent TFAP2E effect should be detectable in relevant cells, with greater binding to ref than alt; any effect on PYDC2 expression remains directionally unspecified.; TFAP2E-specific occupancy or perturbation should be more informative for this chain than EBF4-specific occupancy or perturbation.

Falsified if: A sufficiently sensitive assay in relevant cells finds no TFAP2E occupancy or variant-dependent TFAP2E effect.; Perturbing the variant or its regulatory context produces no TFAP2E-dependent regulatory or target-gene effect.

### 3. H2: EBF4 binding change with a possible nearby regulatory effect (p = 0.01)

TF EBF4 (QBiC-SELEX coverage own_model), ref allele binds more; element A possible nearby regulatory element, including the dELS cCRE 42 bp away; the variant does not overlap the cCRE.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | EBF4 is a tentative candidate because its own QBiC-SELEX model predicts substantially stronger in-vitro binding to ref T than alt G. The prediction is not supported by demonstrated occupancy at the variant. | weak | [E10](#e10) |
| element | The nearby dELS cCRE is a possible regulatory context, but it is 42 bp from the variant and its reported activity is not specific to HCT 116 or evidence of an effect from this variant. | weak | [E03](#e03) |
| gene | PYDC2 is a tentative candidate target based on proximity and nearby-gene annotation; regulation by this variant or cCRE has not been demonstrated. | weak | [E02](#e02), [E03](#e03) |
| cell_type | HCT 116 is a possible context because EBF4 is expressed there, but expression does not establish occupancy or regulatory activity at the variant. | supported | [E10](#e10) |
| phenotype | An EBF4-to-PYDC2 contribution to colorectal cancer is unsupported by the supplied evidence, which gives no direction for a gene-expression or disease effect. | missing | none |

Predictions: If this chain is correct, a variant-dependent EBF4 effect should be detectable in relevant cells, with greater binding to ref than alt; any effect on PYDC2 expression remains directionally unspecified.; EBF4-specific occupancy or perturbation should be more informative for this chain than TFAP2E-specific occupancy or perturbation.

Falsified if: A sufficiently sensitive assay in relevant cells finds no EBF4 occupancy or variant-dependent EBF4 effect.; Perturbing the variant or its regulatory context produces no EBF4-dependent regulatory or target-gene effect.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Measure TFAP2E occupancy by allele-specific CUT&RUN-qPCR in HCT 116 cells carrying the variant, or in matched isogenic ref and alt cells. | medium | yes | No reproducible variant-dependent TFAP2E occupancy difference. | TFAP2E occupancy is greater at ref than alt. | No TFAP2E-specific ref-versus-alt occupancy difference; this chain instead predicts an EBF4-dependent effect. |
| Measure EBF4 occupancy by allele-specific CUT&RUN-qPCR in HCT 116 cells carrying the variant, or in matched isogenic ref and alt cells. | medium | no | No reproducible variant-dependent EBF4 occupancy difference. | No EBF4-specific ref-versus-alt occupancy difference; this chain instead predicts a TFAP2E-dependent effect. | EBF4 occupancy is greater at ref than alt. |

## Next experiment

Perform allele-specific TFAP2E CUT&RUN-qPCR in HCT 116 cells carrying the variant, comparing ref and alt occupancy. It is the most direct listed test of the leading non-null chain against the null; a ref-biased result would support H1, though it would not by itself establish a target-gene or disease effect.

## Refinement rounds

Stopped: round 1 left the top chain and the grades of its links unchanged.

### Round 1

- gene_disease({"gene": "PYDC2"}) for H1.phenotype, ran as [E15](#e15). Expected: If Open Targets reports colorectal-cancer association evidence for PYDC2, this would support the proposed gene-to-disease link and raise H1; no association would leave the phenotype link unsupported.
- literature_search({"query": "PYDC2 colorectal cancer"}) for H2.phenotype, ran as [E16](#e16). Expected: If abstracts provide direct evidence connecting PYDC2 to colorectal cancer, H2’s phenotype link gains support; if not, it remains missing. This may also inform the phenotype link for the other PYDC2 chains.
- qbic_tf_detail({"tf": "ETV3"}) for H3.binding, ran as [E17](#e17). Expected: If the detailed result confirms ETV3-specific QBiC-SELEX coverage and the alt-favored prediction, H3.binding is better supported as an in-vitro prediction; if the entry is only an indirect or ambiguous model mapping, H3 falls relative to the other TF candidates.

- Result of gene_disease({"gene":"PYDC2"}): E15 reports no Open Targets association between PYDC2 and colorectal cancer. (as expected: yes)
- Result of literature_search({"query":"PYDC2 colorectal cancer"}): E16 lists literature hits, but the supplied titles do not provide direct evidence connecting PYDC2 to colorectal cancer. (as expected: yes)
- Result of qbic_tf_detail({"tf":"ETV3"}): E17 gives an ETV3 own-model effect that is below the detection gate (z 3.5); other ETS-family model results are mixed and do not establish an ETV3-specific alt-favored effect. This weakens the prior ETV3 chain. (as expected: yes)

Chains after revision: null 0.96; TFAP2E 0.03; EBF4 0.01. Link grades changed: H1.cell_type: weak → supported, H2.cell_type: weak → supported, H3.binding: weak → absent, H3.cell_type: weak → absent, H3.element: weak → absent, H3.gene: weak → absent, H3.phenotype: missing → absent.

## Flags

- none

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

<a id="e15"></a>**E15** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575).

<a id="e16"></a>**E16** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PYDC2%20colorectal%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T23:24:45+00:00)

> Europe PMC: 20 hits for 'PYDC2 colorectal cancer'; top 8 with PMIDs:
> PMID 40026444 (2025): Correlation Analysis of Pyroptosis-Related Genes CASP1, NLRP3, AIM2, and NLRP1 With Lung Adenocarcinoma.
> PMID 41154652 (2025): Oncogenic Role of SAMD4B in Breast Cancer Progression by Activating Wnt/β-Catenin Pathway.
> PMID 36319832 (2022): A novel refined pyroptosis and inflammasome-related genes signature for predicting prognosis and immune microenvironment in pancreatic ductal adenocarcinoma.
> PMID 39561929 (2024): Optimizing iNKT-driven immune responses against cancer by modulating CD1d in tumor and antigen presenting cells.
> PMID 36341349 (2022): The strategies of NLRP3 inflammasome to combat <i>Toxoplasma gondii</i>.
> PMID 41023436 (2025): Highly multiplexed 3D profiling of cell states and immune niches in human tumors.
> PMID 36732864 (2023): RNA binding protein SAMD4: current knowledge and future perspectives.
> PMID 35338151 (2022): PUMILIO proteins promote colorectal cancer growth via suppressing p21.

<a id="e17"></a>**E17** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ETV3","symbol":"ETV3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr3:191441666:T>G","gate_p":5.02e-05,"models":[{"model":"ETV3_NA_TCAGGA20NCG_ESW_yang2017_1_4_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.775,"effect":0.115,"z":3.5,"p":0.00047,"rank_abs_z":"283/997","passed_gate":false,"site_strength":{"ref_percentile":72.7,"alt_percentile":95.9,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":-0.231,"z":-7.84,"p":4.3e-15,"rank_abs_z":"28/997","passed_gate":true,"site_strength":{"ref_percentile":72.6,"alt_percentile":86.8,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":-0.705,"z":-4.96,"p":7e-07,"rank_abs_z":"139/997","passed_gate":true,"site_strength":{"ref_percentile":66.1,"alt_percentile":83.2,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":-0.291,"z":-3.78,"p":0.00016,"rank_abs_z":"250/997","passed_gate":false,"site_strength":{"ref_percentile":91.9,"alt_percentile":80.7,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":0.124,"z":0.97,"p":0.33,"rank_abs_z":"725/997","passed_gate":false,"site_strength":{"ref_percentile":68.6,"alt_percentile":70.8,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":0.149,"z":1.6,"p":0.11,"rank_abs_z":"594/997","passed_gate":false,"site_strength":{"ref_percentile":74.8,"alt_percentile":96.5,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":0.138,"z":2.01,"p":0.044,"rank_abs_z":"527/997","passed_gate":false,"site_strength":{"ref_percentile":75.0,"alt_percentile":74.1,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.125,"z":3.97,"p":7.3e-05,"rank_abs_z":"222/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":94.1,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":0.217,"z":1.72,"p":0.085,"rank_abs_z":"571/997","passed_gate":false,"site_strength":{"ref_percentile":80.6,"alt_percentile":93.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":-0.236,"z":-3.54,"p":0.00039,"rank_abs_z":"275/997","passed_gate":false,"site_strength":{"ref_percentile":95.1,"alt_percentile":95.7,"k":7}}],"n_models_trimmed":8}
