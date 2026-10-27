# rs13078086 and Colorectal cancer

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 92 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: EBF4 (z -60.28); TFAP2A (z -18.37); TFAP2C (z -18.37); TFAP2E (z -18.37); ETV3 (z 13.11). Diagnostic, not shown to the model: 209 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0_null: No TF-mediated effect of rs13078086 (p = 0.72)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at this base.; No allele-specific regulatory activity attributable to rs13078086 in HCT116.; Any disease signal is explained by a linked causal variant, a passenger event, or no allelic regulatory effect.

Falsified if: Allele-specific TF occupancy at rs13078086 is demonstrated in HCT116 or another relevant colorectal cancer model.; A validated regulatory assay shows the T>G base itself changes target gene expression, and the effect is lost when the implicated TF is depleted.

### 2. H2_TFAP2E_ref: TFAP2E binds the ref allele more strongly through an AP-2 motif near a dELS (p = 0.16)

TF TFAP2E (QBiC-SELEX coverage own_model), ref allele binds more; element The variant is 42 bp from dELS EH38E2269392 and does not overlap a cCRE; it may alter an AP-2 site within or next to that element, but this is not established.; gene PYDC2; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2E is nominated because its own QBiC-SELEX model shows the ref T allele binds more strongly than the alt G allele (z -18.37, effect -0.765), and TFAP2E is the highest-expressed AP-2 candidate in HCT116 at 8.5 TPM. The AP-2 family shares binding specificity, and mapped AP-2 models also detect the same ref-more effect for TFAP2A and TFAP2C, so TFAP2E-specific attribution is not established. No ENCODE TFAP2E ChIP data exist and no ChIP peak contains this site, so occupancy is unknown. | weak | [E13](#e13), [E16](#e16), [E11](#e11), [E12](#e12), [E04](#e04) |
| element | The variant is 42 bp from dELS EH38E2269392 and may modify an AP-2 site in or adjacent to that element; because the variant does not overlap a cCRE, direct regulatory-element perturbation is not shown. | weak | [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb and the variant is intronic in PYDC2-AS1; no significant GTEx v8 single-tissue eQTL for this variant is reported, so target-gene linkage is not demonstrated. | weak | [E01](#e01), [E02](#e02), [E07](#e07) |
| cell_type | The mechanism would require TFAP2E occupancy in HCT116; TFAP2E is expressed there, but ENCODE has no TFAP2E ChIP data in HCT116 and no occupancy is shown at the variant. | weak | [E13](#e13), [E16](#e16), [E04](#e04) |
| phenotype | Colorectal cancer relevance is speculative: rs13078086 has no GWAS Catalog association and no Open Targets record. | missing | [E05](#e05), [E06](#e06) |

Predictions: The ref T allele shows stronger TFAP2E binding than the alt G allele.; TFAP2E occupancy at or near rs13078086 would be detectable if assayed in HCT116.; The alt G allele would reduce TFAP2E occupancy and may change PYDC2 expression.

Falsified if: TFAP2E ChIP/CUT&RUN in HCT116 shows no occupancy at rs13078086.; Allele-specific assays show equal TFAP2E binding for T and G.; The AP-2 motif effect is shown to be driven by TFAP2A or TFAP2C rather than TFAP2E.

### 3. H1_EBF4_ref: EBF4 binds the ref allele more strongly at a nearby dELS and may regulate PYDC2 (p = 0.09)

TF EBF4 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant is 42 bp from dELS EH38E2269392 and does not overlap a cCRE; it may perturb an adjacent element, but direct element overlap is not demonstrated.; gene PYDC2; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | EBF4 is nominated because its own QBiC-SELEX model gives the largest allelic effect and shows the ref T allele binds more strongly than the alt G allele (z -60.28, effect -1.954). This is weak without occupancy: no ENCODE TF ChIP-seq peak contains the site in any biosample, EBF4 has no ENCODE HCT116 ChIP data, and EBF4 is expressed at only 1.22 TPM in HCT116. | weak | [E10](#e10), [E04](#e04), [E15](#e15) |
| element | The variant is 42 bp from the dELS EH38E2269392 and may modify an EBF4 site within or adjacent to that element; because no cCRE overlaps the variant, this is proximity evidence only. | weak | [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene, 19.5 kb upstream, and the variant lies in a PYDC2-AS1 intron; however, there are no significant GTEx v8 single-tissue eQTLs for this variant, so the variant-to-PYDC2 link is proximity-based only. | weak | [E01](#e01), [E02](#e02), [E07](#e07) |
| cell_type | The proposed mechanism would require EBF4 occupancy in HCT116; EBF4 is expressed there at low level, but there is no EBF4 ChIP data in HCT116 and no ENCODE peak at the variant. | weak | [E10](#e10), [E04](#e04), [E15](#e15) |
| phenotype | Colorectal cancer relevance is unproven: rs13078086 has no GWAS Catalog association and no Open Targets record. | missing | [E05](#e05), [E06](#e06) |

Predictions: The ref T allele shows stronger EBF4 binding than the alt G allele.; EBF4 occupancy, if assayed in HCT116, would be detectable at or very near rs13078086.; The alt G allele would reduce EBF4 occupancy and may alter PYDC2 or nearby target expression.

Falsified if: EBF4 ChIP/CUT&RUN in HCT116 or a relevant colorectal model shows no occupancy at rs13078086.; Allele-specific assays show no difference in EBF4 binding between T and G.; CRISPR, reporter, or eQTL evidence shows no effect of this base on PYDC2 or another nearby gene.

### 4. H3_ETV3_alt: ETV3 binds the alt allele more strongly, but the signal is mostly ETV5-mapped (p = 0.03)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant is 42 bp from dELS EH38E2269392 and does not overlap a cCRE; an ETV3/ETV5-like site in or near that element is hypothetical.; gene PYDC2; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3 is nominated but not established: the QBiC-SELEX alt-more signal in E14 (z 13.11, effect 0.251) comes from a CIS-BP-mapped ETV5 model, while ETV3's own model shows only a subthreshold alt-more trend (z 3.5, effect 0.115) and does not pass the gate. No ENCODE TF ChIP-seq peak contains the site and ETV3 has no HCT116 ChIP data, so occupancy is unknown. | missing | [E14](#e14), [E17](#e17), [E04](#e04) |
| element | The variant is 42 bp from dELS EH38E2269392 and may perturb an Ets site near that element; no cCRE directly overlaps the variant. | weak | [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene and the variant lies in a PYDC2-AS1 intron, but no significant GTEx v8 single-tissue eQTL is reported for this variant. | weak | [E01](#e01), [E02](#e02), [E07](#e07) |
| cell_type | ETV3 is expressed in HCT116 at 16.34 TPM, but there is no ENCODE ETV3 ChIP data in HCT116 and no occupancy evidence at the variant; the cell-type mechanism remains conditional. | weak | [E14](#e14), [E17](#e17), [E04](#e04) |
| phenotype | Colorectal cancer relevance is unproven: rs13078086 has no GWAS Catalog association and no Open Targets record. | missing | [E05](#e05), [E06](#e06) |

Predictions: The alt G allele shows stronger ETV3 binding than the ref T allele if ETV3 itself acts at this site.; ETV3 own-model allele-specific assays would show alt > ref, not only the ETV5-mapped model.; ETV3 occupancy at or near rs13078086 would be detectable if assayed in HCT116.

Falsified if: ETV3 own-model allele-specific assays show no difference between T and G.; ETV3 ChIP/CUT&RUN in HCT116 shows no occupancy at rs13078086.; The alt-more QBiC-SELEX signal is shown to be driven by ETV5 rather than ETV3.

## Prediction matrix

| Test | Cost | Separates top two | H0_null | H2_TFAP2E_ref | H1_EBF4_ref | H3_ETV3_alt |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA or competitive binding with TFAP2E, using T and G oligos; ideally HCT116 nuclear extract plus TFAP2E antibody supershift. | low | yes | No allele-specific TFAP2E binding difference between T and G. | The ref T allele binds TFAP2E more strongly than the alt G allele. | No TFAP2E-specific difference expected; this test does not assess EBF4. | No TFAP2E-specific difference expected; this test does not assess ETV3. |
| Targeted TFAP2E ChIP-qPCR or CUT&RUN-qPCR at rs13078086 in HCT116. | medium | yes | No TFAP2E enrichment and no allele-specific occupancy at rs13078086. | TFAP2E occupancy is detectable at or near rs13078086, with ref > alt if the cells are heterozygous. | No TFAP2E enrichment at rs13078086. | No TFAP2E enrichment at rs13078086. |
| Targeted EBF4 ChIP-qPCR or CUT&RUN-qPCR at rs13078086 in HCT116. | medium | no | No EBF4 enrichment and no allele-specific occupancy at rs13078086. | No EBF4 enrichment at rs13078086. | EBF4 occupancy is detectable at or near rs13078086, with ref > alt if heterozygous. | No EBF4 enrichment at rs13078086. |
| Allele-specific EMSA or ETV3 own-model reporter assay for ETV3 binding at T versus G. | low | no | No allele-specific ETV3 binding difference between T and G. | No ETV3-specific difference expected. | No ETV3-specific difference expected. | The alt G allele binds ETV3 more strongly than the ref T allele in ETV3 own-model assays. |
| Allele-specific MPRA or reporter assay with T and G in HCT116, with and without TFAP2E depletion. | medium | yes | No allele-specific regulatory activity for T versus G in HCT116. | Allele-specific regulatory activity is present and is reduced by TFAP2E depletion. | Allele-specific regulatory activity is present and is reduced by EBF4 depletion. | Allele-specific regulatory activity is present and tracks the ETV3/ETV5 alt-more motif effect. |

## Next experiment

The cheapest single experiment separating the top two chains, H0_null and H2_TFAP2E_ref, is an allele-specific TFAP2E EMSA or competitive binding assay with T and G oligos in HCT116 nuclear extract, ideally with TFAP2E antibody supershift. It is binding-only: a positive result supports H2_TFAP2E_ref at the binding link but does not prove occupancy; a negative result falsifies H2_TFAP2E_ref's central TFAP2E-binding claim.

## Investigate calls

- chip_peaks({"tf": "EBF4", "biosample": "HCT116"})
- qbic_tf_detail({"tf": "TFAP2E"})
- qbic_tf_detail({"tf": "ETV3"})

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

<a id="e15"></a>**E15** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:39:46+00:00)

> No ENCODE EBF4 ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT116'. Absence can also mean no EBF4 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e16"></a>**E16** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TFAP2E","symbol":"TFAP2E","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr3:191441666:T>G","gate_p":5.02e-05,"models":[{"model":"TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer","mapping":"own","group":"G030 AP-2, 4 models","quality":0.88,"effect":-0.765,"z":-18.37,"p":2.5e-75,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":99.7,"alt_percentile":99.6,"k":7}},{"model":"TCFAP2A_NA_TGATCC20NCG_ESP_yang2017_0_4_7mer","mapping":"CIS-BP (TFAP2A)","group":"G030 AP-2, 4 models","quality":0.927,"effect":-2.475,"z":-16.2,"p":4.7e-59,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":99.8,"alt_percentile":99.4,"k":7}},{"model":"TFAP2B_FL_TGTCCG20NGA_KH_nitta2015_1_3_7mer","mapping":"CIS-BP (TFAP2B)","group":"G030 AP-2, 4 models","quality":0.77,"effect":-0.77,"z":-13.18,"p":1.2e-39,"rank_abs_z":"8/997","passed_gate":true,"site_strength":{"ref_percentile":99.8,"alt_percentile":98.8,"k":7}},{"model":"TFAP2C_eDBD_TGAGCT40NGCA_KP_yin2017_0_4_7mer","mapping":"CIS-BP (TFAP2C)","group":"G030 AP-2, 4 models","quality":0.753,"effect":-0.336,"z":-5.14,"p":2.7e-07,"rank_abs_z":"126/997","passed_gate":true,"site_strength":{"ref_percentile":97.2,"alt_percentile":98.2,"k":7}}]}

<a id="e17"></a>**E17** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ETV3","symbol":"ETV3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr3:191441666:T>G","gate_p":5.02e-05,"models":[{"model":"ETV3_NA_TCAGGA20NCG_ESW_yang2017_1_4_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.775,"effect":0.115,"z":3.5,"p":0.00047,"rank_abs_z":"283/997","passed_gate":false,"site_strength":{"ref_percentile":72.7,"alt_percentile":95.9,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":-0.231,"z":-7.84,"p":4.3e-15,"rank_abs_z":"28/997","passed_gate":true,"site_strength":{"ref_percentile":72.6,"alt_percentile":86.8,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":-0.705,"z":-4.96,"p":7e-07,"rank_abs_z":"139/997","passed_gate":true,"site_strength":{"ref_percentile":66.1,"alt_percentile":83.2,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":-0.291,"z":-3.78,"p":0.00016,"rank_abs_z":"250/997","passed_gate":false,"site_strength":{"ref_percentile":91.9,"alt_percentile":80.7,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":0.124,"z":0.97,"p":0.33,"rank_abs_z":"725/997","passed_gate":false,"site_strength":{"ref_percentile":68.6,"alt_percentile":70.8,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":0.149,"z":1.6,"p":0.11,"rank_abs_z":"594/997","passed_gate":false,"site_strength":{"ref_percentile":74.8,"alt_percentile":96.5,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":0.138,"z":2.01,"p":0.044,"rank_abs_z":"527/997","passed_gate":false,"site_strength":{"ref_percentile":75.0,"alt_percentile":74.1,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.125,"z":3.97,"p":7.3e-05,"rank_abs_z":"222/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":94.1,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":0.217,"z":1.72,"p":0.085,"rank_abs_z":"571/997","passed_gate":false,"site_strength":{"ref_percentile":80.6,"alt_percentile":93.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":-0.236,"z":-3.54,"p":0.00039,"rank_abs_z":"275/997","passed_gate":false,"site_strength":{"ref_percentile":95.1,"alt_percentile":95.7,"k":7}}],"n_models_trimmed":8}
