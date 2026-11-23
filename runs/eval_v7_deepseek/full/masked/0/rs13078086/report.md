# rs13078086 and Colorectal cancer

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 18 model calls; 258 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

**Verdict: undetermined.** The null leads, but nothing tested counts against TFAP2E, EBF4.

Association with the disease (not part of the verdict): GWAS Catalog tested, negative; Open Targets fine-mapping not tested.

Pairwise ranking (Bradley-Terry strengths): H4 0.62, H1 0.15, H2 0.15, H3 0.08. 2 of 6 pairs came out differently in the two orders.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: EBF4 (z -60.28); TFAP2A (z -18.37); TFAP2C (z -18.37); TFAP2E (z -18.37); ETV3 (z 13.11). Diagnostic, not shown to the model: 209 of 997 models pass Bonferroni.

## Ranked chains

### 1. H4: No TF-mediated effect of this variant (p = 0.62)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy or regulatory activity at chr3:191441666 should be detectable in HCT116 or other relevant colorectal cancer cells.; Any observed disease association would be better explained by a linked causal variant, a passenger event, or no causal effect.; The QBiC-SELEX changes should not translate into occupancy because there is no ENCODE ChIP-seq peak and no directly overlapping cCRE; negative eQTL, GWAS, and gene-disease results further favor no demonstrated mechanism.

Falsified if: Allele-specific ChIP, MPRA, or reporter assays demonstrate a TF-dependent effect at this base.; CRISPR or eQTL evidence ties this variant to PYDC2 expression in colorectal cancer cells.; A validated causal variant is shown to be this variant rather than a linked polymorphism.

### 2. H2: AP-2 family TF TFAP2E has a ref-favoring in vitro binding change, but occupancy and target regulation are unproven (p = 0.15)

TF TFAP2E (QBiC-SELEX coverage own_model), ref allele binds more; element PYDC2-AS1 intron near dELS EH38E2269392; gene PYDC2; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts that the ref allele binds an AP-2 model more strongly than the alt allele (effect -0.765, z -18.37), and TFAP2E has its own model with the highest HCT116 expression among the AP-2 candidates (8.5 TPM). However, TFAP2A and TFAP2C share the same mapped AP-2 model, and occupancy at this variant is unknown because no ENCODE ChIP-seq peak contains the site. | weak | [E13](#e13), [E11](#e11), [E12](#e12), [E04](#e04), [E09](#e09) |
| element | The variant is in a PYDC2-AS1 intron 42 bp from dELS EH38E2269392, making it a candidate AP-2-responsive element, but no annotated cCRE directly overlaps the base and the dELS evidence is not HCT116-specific. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb and the variant lies within PYDC2-AS1, but there is no direct regulatory evidence linking this variant to PYDC2; GTEx reports no significant eQTL. | missing | [E01](#e01), [E02](#e02), [E07](#e07) |
| cell_type | TFAP2E is expressed in HCT116 at 8.5 TPM, making an AP-2-mediated effect in this cell line plausible, but expression alone does not demonstrate TFAP2E activity at this element. | weak | [E13](#e13), [E09](#e09) |
| phenotype | Open Targets reports no association between PYDC2 and colorectal cancer, and the cited literature does not directly establish a TFAP2E-PYDC2 colorectal cancer pathway; the phenotype link is speculative. | missing | [E16](#e16), [E08](#e08) |

Predictions: AP-2/TFAP2E ChIP or reporter assays should show stronger occupancy or activity for the ref T allele than the alt G allele.; TFAP2E perturbation in HCT116 should alter PYDC2 expression if this chain is correct.; The element should show AP-2 motif-dependent allele-specific activity in colorectal cancer cells.

Falsified if: TFAP2E or pan-AP-2 ChIP shows no occupancy at this element in HCT116.; Ref and alt alleles show equal AP-2-dependent reporter activity.; TFAP2E knockdown does not change PYDC2 expression.

### 3. H1: EBF4 has a ref-favoring in vitro binding change at this variant, but occupancy is unsupported (p = 0.12)

TF EBF4 (QBiC-SELEX coverage own_model), ref allele binds more; element PYDC2-AS1 intron near dELS EH38E2269392; gene PYDC2; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts that the ref allele binds EBF4 more strongly than the alt allele (effect -1.954, z -60.28), but this is an in vitro binding prediction only. EBF4 occupancy at the variant is unsupported: ENCODE never assayed EBF4 in HCT116, no ENCODE ChIP-seq peak contains the variant, and ReMap has no EBF4 peak over it. EBF4 is also very lowly expressed in HCT116 (1.22 TPM). | weak | [E10](#e10), [E15](#e15), [E04](#e04), [E09](#e09) |
| element | The variant lies in a PYDC2-AS1 intron and 42 bp from dELS EH38E2269392, so it is a candidate regulatory element, but no annotated cCRE directly overlaps the variant and the dELS z-scores are biosample maxima rather than HCT116-specific evidence. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb and the variant lies within PYDC2-AS1, but there is no direct regulatory evidence linking this variant to PYDC2; GTEx reports no significant eQTL. | missing | [E01](#e01), [E02](#e02), [E07](#e07) |
| cell_type | EBF4 is expressed in HCT116, but at only 1.22 TPM, so an EBF4-dependent effect in this colorectal cancer cell line is weakly supported. | weak | [E10](#e10), [E09](#e09) |
| phenotype | Open Targets reports no association between PYDC2 and colorectal cancer, and the cited literature does not establish a direct PYDC2 colorectal cancer mechanism; any phenotype link remains speculative. | missing | [E16](#e16), [E08](#e08) |

Predictions: Allele-specific EBF4 ChIP or reporter assays should show stronger binding or activity for the ref T allele than the alt G allele.; EBF4 perturbation in HCT116 should change PYDC2 expression if this chain is correct.; The variant should lie in an active regulatory element in HCT116 despite the current lack of a directly overlapping cCRE.

Falsified if: EBF4 ChIP shows no occupancy at this element in HCT116 or equal binding to ref and alt alleles.; EBF4 knockdown or knockout does not affect PYDC2 expression in HCT116.; The nearby dELS is not active in colorectal cancer cells and the variant has no measurable regulatory activity.

### 4. H3: ETV3 has an indirect alt-favoring Ets-model binding prediction, but ETV3-specific binding is weak (p = 0.11)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element PYDC2-AS1 intron near dELS EH38E2269392; gene PYDC2; cell type HCT116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The strongest QBiC-SELEX alt-favoring signal for ETV3 (effect 0.251, z 13.11) comes from an ETV5-mapped Ets model, not from ETV3's own model. ETV3 has its own QBiC-SELEX model, but that model does not pass the gate (effect 0.115, z 3.5), and ETV3 occupancy at the variant is unknown because no ENCODE ChIP-seq peak contains the site. | weak | [E17](#e17), [E14](#e14), [E04](#e04), [E09](#e09) |
| element | The variant lies in a PYDC2-AS1 intron 42 bp from dELS EH38E2269392, giving a candidate Ets-responsive element, but no cCRE directly overlaps the variant and the dELS signal is not shown to be active in HCT116. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the closest protein-coding gene at 19.5 kb and the host transcript is PYDC2-AS1, but there is no direct evidence that an ETV3-bound element here regulates PYDC2; GTEx reports no significant eQTL. | missing | [E01](#e01), [E02](#e02), [E07](#e07) |
| cell_type | ETV3 is expressed in HCT116 at 16.34 TPM, which is compatible with a role, but there is no allele-specific ETV3 functional evidence in this cell line. | weak | [E14](#e14), [E09](#e09), [E17](#e17) |
| phenotype | Open Targets reports no association between PYDC2 and colorectal cancer, and the cited literature does not demonstrate an ETV3-PYDC2 colorectal cancer pathway; the phenotype link is speculative. | missing | [E16](#e16), [E08](#e08) |

Predictions: Allele-specific ETV3 or Ets ChIP or reporter assays should show stronger binding or activity for the alt G allele than the ref T allele.; ETV3 perturbation in HCT116 should change PYDC2 expression if this chain is correct.; The element should show Ets-motif-dependent allele-specific activity in colorectal cancer cells.

Falsified if: ETV3 ChIP shows no occupancy at this element in HCT116.; Ref and alt alleles show equal ETV3-dependent reporter activity or the ref allele binds more.; ETV3 knockdown does not alter PYDC2 expression.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H2 | H1 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific MPRA or reporter assay in HCT116 comparing ref T and alt G at chr3:191441666, with AP-2 motif mutation | medium | yes | No allele-specific regulatory activity for either allele. | Ref allele shows stronger AP-2-dependent regulatory activity than alt; AP-2 motif mutation reduces the effect. | No AP-2-dependent allele-specific activity; EBF4-specific assays would still be needed. | No AP-2-dependent allele-specific activity; an Ets-dependent effect would need separate testing. |
| Allele-specific EBF4 ChIP-qPCR or EBF4 reporter assay in HCT116 | medium | no | No EBF4 occupancy or allele-specific activity. | No EBF4 allele-specific binding or activity. | Stronger EBF4 binding or activity for the ref T allele than the alt G allele. | No EBF4 allele-specific binding or activity. |
| Allele-specific ETV3 or Ets ChIP-qPCR or reporter assay in HCT116 | medium | no | No ETV3/Ets occupancy or allele-specific activity. | No ETV3/Ets allele-specific binding or activity. | No ETV3/Ets allele-specific binding or activity. | Stronger ETV3/Ets binding or activity for the alt G allele than the ref T allele. |
| CRISPRi or knockout of TFAP2E with PYDC2 expression measurement in HCT116 | high | yes | No change in PYDC2 expression after TFAP2E perturbation. | PYDC2 expression changes after TFAP2E perturbation. | No change in PYDC2 expression after TFAP2E perturbation. | No change in PYDC2 expression after TFAP2E perturbation. |

## Next experiment

Perform an allele-specific MPRA or reporter assay in HCT116 comparing the ref T and alt G alleles at chr3:191441666, including an AP-2 motif mutant, to test whether the variant drives allele-specific regulatory activity consistent with TFAP2E binding. This is the cheapest available test that separates the top two chains, H4 and H2.

## Refinement rounds

Stopped: round 1 left the top chain and the grades of its links unchanged.

### Round 1

- chip_peaks({"tf": "EBF4", "biosample": "HCT116"}) for H1.binding, ran as [E15](#e15) (not tested). Expected: If an ENCODE EBF4 ChIP-seq peak containing this variant exists in HCT116, H1.binding becomes supported and H1 rises. If EBF4 was not assayed in HCT116 or no peak contains the variant, H1.binding remains weak and H1 does not gain occupancy support.
- gene_disease({"gene": "PYDC2"}) for H1.phenotype, ran as [E16](#e16). Expected: If Open Targets reports a direct PYDC2 association with colorectal cancer, the phenotype link shared by H1-H3 becomes supported and all non-null chains rise modestly. If there is no association or only indirect evidence, the phenotype link remains missing and the null keeps more weight.
- qbic_tf_detail({"tf": "ETV3"}) for H3.binding, ran as [E17](#e17). Expected: If ETV3 has its own QBiC-SELEX model and an alt-favoring change passes the gate, H3.binding becomes less indirect and H3 rises. If ETV3 is only covered through the ETV5-mapped model or has no ETV3-specific model, H3.binding remains weak and H3 falls relative to H1/H2.

- Result of chip_peaks(EBF4, HCT116): E15: ENCODE has no EBF4 ChIP-seq experiment in HCT116 because EBF4 was never assayed, and ReMap has no EBF4 peak over the variant. There is no EBF4 occupancy evidence at this site. (as expected: yes)
- Result of gene_disease(PYDC2): E16: Open Targets reports no association between PYDC2 and colorectal cancer (MONDO_0005575). (as expected: yes)
- Result of qbic_tf_detail(ETV3): E17: ETV3 has an own QBiC-SELEX model, but its own-model change does not pass the gate (effect 0.115, z 3.5). The strongest alt-favoring signal (effect 0.251, z 13.11) is from an ETV5-mapped Ets model, so ETV3-specific binding remains weak. (as expected: yes)

Chains after revision: null 0.62; TFAP2E 0.15; EBF4 0.12; ETV3 0.11. Link grades changed: H1.gene: weak → missing, H2.gene: weak → missing, H3.gene: weak → missing.

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

<a id="e15"></a>**E15** chip_peaks (not tested), ENCODE experiment search; ReMap 2022 (UCSC track ReMapTFs) (https://www.encodeproject.org/search/?type=Experiment&assay_title=TF+ChIP-seq&status=released&assembly=GRCh38&format=json&limit=all&field=target.label&field=biosample_ontology.term_name&field=accession; retrieved local)

> ENCODE has no EBF4 ChIP-seq experiment in biosamples matching 'HCT116', so ENCODE says nothing about it there, for or against. ENCODE never assayed EBF4. ReMap 2022 has no EBF4 peak over the variant (ReMap lists peaks only, so this is no evidence against binding).

<a id="e16"></a>**E16** gene_disease (tested, negative), Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575); no evidence there links them.

<a id="e17"></a>**E17** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ETV3","symbol":"ETV3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr3:191441666:T>G","gate_p":5.02e-05,"models":[{"model":"ETV3_NA_TCAGGA20NCG_ESW_yang2017_1_4_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.775,"effect":0.115,"z":3.5,"p":0.00047,"rank_abs_z":"283/997","passed_gate":false,"site_strength":{"ref_percentile":72.7,"alt_percentile":95.9,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":-0.231,"z":-7.84,"p":4.3e-15,"rank_abs_z":"28/997","passed_gate":true,"site_strength":{"ref_percentile":72.6,"alt_percentile":86.8,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":-0.705,"z":-4.96,"p":7e-07,"rank_abs_z":"139/997","passed_gate":true,"site_strength":{"ref_percentile":66.1,"alt_percentile":83.2,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":-0.291,"z":-3.78,"p":0.00016,"rank_abs_z":"250/997","passed_gate":false,"site_strength":{"ref_percentile":91.9,"alt_percentile":80.7,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":0.124,"z":0.97,"p":0.33,"rank_abs_z":"725/997","passed_gate":false,"site_strength":{"ref_percentile":68.6,"alt_percentile":70.8,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":0.149,"z":1.6,"p":0.11,"rank_abs_z":"594/997","passed_gate":false,"site_strength":{"ref_percentile":74.8,"alt_percentile":96.5,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":0.138,"z":2.01,"p":0.044,"rank_abs_z":"527/997","passed_gate":false,"site_strength":{"ref_percentile":75.0,"alt_percentile":74.1,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.125,"z":3.97,"p":7.3e-05,"rank_abs_z":"222/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":94.1,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":0.217,"z":1.72,"p":0.085,"rank_abs_z":"571/997","passed_gate":false,"site_strength":{"ref_percentile":80.6,"alt_percentile":93.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":-0.236,"z":-3.54,"p":0.00039,"rank_abs_z":"275/997","passed_gate":false,"site_strength":{"ref_percentile":95.1,"alt_percentile":95.7,"k":7}}],"n_models_trimmed":8}
