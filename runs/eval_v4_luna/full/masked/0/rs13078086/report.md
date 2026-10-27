# rs13078086 and Colorectal cancer

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 12 model calls; 263 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: EBF4 (z -60.28); TFAP2A (z -18.37); TFAP2C (z -18.37); TFAP2E (z -18.37); ETV3 (z 13.11). Diagnostic, not shown to the model: 209 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.97)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant has no material TF-mediated effect. Any disease relationship, if one exists, is absent or due to another cause, such as a linked variant.

Falsified if: Allele-specific experiments show that this base changes TF occupancy or regulatory activity and that the change affects a relevant target gene.

### 2. H4: TFAP2A-mediated effect near a possible regulatory element (p = 0.01)

TF TFAP2A (QBiC-SELEX coverage own_model), ref allele binds more; element A possible nearby regulatory element, including the dELS cCRE 42 bp away; the variant does not overlap the cCRE.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A's own QBiC-SELEX model predicts stronger in-vitro binding to ref T than alt G. This provides a TFAP2A-specific model result, unlike the TFAP2E-mapped result, but does not establish occupancy; no ENCODE peak contains the variant. | weak | [E04](#e04), [E19](#e19) |
| element | The variant lies in a PYDC2-AS1 intron and is 42 bp from a dELS cCRE, but does not overlap it; the cCRE's reported activity is not HCT 116-specific. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is a proximity-based candidate target, but no regulatory connection is shown and no significant GTEx eQTL is reported. | weak | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | TFAP2A is expressed in HCT 116, but its occupancy or regulatory activity there is not established. | supported | [E04](#e04), [E19](#e19) |
| phenotype | A TFAP2A–PYDC2 contribution to colorectal cancer is speculative; the supplied evidence does not support this phenotype link. | missing | [E05](#e05), [E15](#e15), [E16](#e16), [E17](#e17), [E20](#e20) |

Predictions: If this chain is correct, TFAP2A should occupy the variant in relevant cells, with greater binding to ref than alt, and variant or TFAP2A perturbation should affect a nearby regulatory output. The direction of any PYDC2 expression or disease effect is not established.

Falsified if: A sensitive, validated assay finds no TFAP2A occupancy at the variant in relevant cells.; Allele-specific testing finds no ref-over-alt TFAP2A binding difference, or variant and TFAP2A perturbation show no relevant regulatory effect.

### 3. H2: EBF4-mediated effect near a possible regulatory element (p = 0.01)

TF EBF4 (QBiC-SELEX coverage own_model), ref allele binds more; element A possible nearby regulatory element, including the dELS cCRE 42 bp away; the variant does not overlap the cCRE.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | EBF4's own QBiC-SELEX model predicts stronger in-vitro binding to ref T than alt G. This is a binding prediction only; no occupancy at the variant is reported. | weak | [E04](#e04), [E10](#e10) |
| element | The variant lies in a PYDC2-AS1 intron and is 42 bp from a dELS cCRE, but does not overlap it; the cCRE's reported activity is not HCT 116-specific. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is a proximity-based candidate target, but no regulatory connection is shown and no significant GTEx eQTL is reported. | weak | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | EBF4 is expressed in HCT 116, but its occupancy or regulatory activity there is not established. | supported | [E04](#e04), [E10](#e10) |
| phenotype | An EBF4–PYDC2 contribution to colorectal cancer is speculative; the supplied evidence does not support this phenotype link. | missing | [E05](#e05), [E15](#e15), [E16](#e16), [E17](#e17), [E20](#e20) |

Predictions: If this chain is correct, EBF4 should occupy the variant in relevant cells, with greater binding to ref than alt, and variant or EBF4 perturbation should affect a nearby regulatory output. The direction of any PYDC2 expression or disease effect is not established.

Falsified if: A sensitive, validated assay finds no EBF4 occupancy at the variant in relevant cells.; Allele-specific testing finds no ref-over-alt EBF4 binding difference, or variant and EBF4 perturbation show no relevant regulatory effect.

### 4. H1: TFAP2E-mediated effect near a possible regulatory element (p = 0.01)

TF TFAP2E (QBiC-SELEX coverage own_model), ref allele binds more; element A possible nearby regulatory element, including the dELS cCRE 42 bp away; the variant does not overlap the cCRE.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The TFAP2E QBiC-SELEX model predicts stronger in-vitro binding to ref T than alt G. The same mapped-model prediction is reported for TFAP2A and TFAP2C, so the evidence does not distinguish TFAP2E; none has occupancy evidence at the variant. | weak | [E04](#e04), [E11](#e11), [E12](#e12), [E13](#e13) |
| element | The variant lies in a PYDC2-AS1 intron and is 42 bp from a dELS cCRE, but does not overlap it; the cCRE's reported activity is not HCT 116-specific. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is a proximity-based candidate target, but no regulatory connection is shown and no significant GTEx eQTL is reported. | weak | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | TFAP2E is expressed in HCT 116, but its occupancy or regulatory activity there is not established. | supported | [E04](#e04), [E13](#e13) |
| phenotype | A TFAP2E–PYDC2 contribution to colorectal cancer is speculative; the supplied evidence does not support this phenotype link. | missing | [E05](#e05), [E15](#e15), [E16](#e16), [E17](#e17), [E20](#e20) |

Predictions: If this chain is correct, TFAP2E should occupy the variant in relevant cells, with greater binding to ref than alt, and variant or TFAP2E perturbation should affect a nearby regulatory output. The direction of any PYDC2 expression or disease effect is not established.

Falsified if: A sensitive, validated assay finds no TFAP2E occupancy at the variant in relevant cells.; Allele-specific testing finds no ref-over-alt TFAP2E binding difference, or variant and TFAP2E perturbation show no relevant regulatory effect.

### 5. H3: ETV3-mediated effect near a possible regulatory element (p = 0.00)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element A possible nearby regulatory element, including the dELS cCRE 42 bp away; the variant does not overlap the cCRE.; gene PYDC2; cell type HCT 116.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reported ETV3 alt-over-ref prediction comes from a CIS-BP-mapped ETV5 model, not an ETV3-specific result. ETV3's own QBiC-SELEX model has an alt-over-ref effect below the detection gate; no occupancy at the variant is reported. | missing | [E04](#e04), [E14](#e14), [E18](#e18) |
| element | The variant lies in a PYDC2-AS1 intron and is 42 bp from a dELS cCRE, but does not overlap it; the cCRE's reported activity is not HCT 116-specific. | weak | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is a proximity-based candidate target, but no regulatory connection is shown and no significant GTEx eQTL is reported. | weak | [E02](#e02), [E03](#e03), [E07](#e07) |
| cell_type | ETV3 is expressed in HCT 116, but its occupancy or regulatory activity there is not established. | supported | [E04](#e04), [E14](#e14) |
| phenotype | An ETV3–PYDC2 contribution to colorectal cancer is speculative; the supplied evidence does not support this phenotype link. | missing | [E05](#e05), [E15](#e15), [E16](#e16), [E17](#e17), [E20](#e20) |

Predictions: If this chain is correct, ETV3 should occupy the variant in relevant cells and show greater binding to alt than ref in an ETV3-specific assay. Variant or ETV3 perturbation should affect a nearby regulatory output. The direction of any PYDC2 expression or disease effect is not established.

Falsified if: A sensitive, validated assay finds no ETV3 occupancy at the variant in relevant cells.; ETV3-specific allele testing finds no alt-over-ref binding difference, or variant and ETV3 perturbation show no relevant regulatory effect.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H4 | H2 | H1 | H3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TFAP2A CUT&RUN or ChIP-qPCR at the variant in genotyped HCT 116 cells | medium | yes | No TFAP2A occupancy attributable to the variant, or no ref-versus-alt occupancy imbalance. | TFAP2A occupancy at the site, with greater occupancy on the ref allele. | No specific TFAP2A occupancy prediction; this chain instead predicts EBF4 occupancy. | No specific TFAP2A occupancy prediction; this chain instead predicts TFAP2E occupancy. | No specific TFAP2A occupancy prediction; this chain instead predicts ETV3 occupancy. |
| Precise T-to-G base editing, followed by TFAP2A perturbation and measurement of local candidate-gene expression | high | yes | Editing has no reproducible TFAP2A-dependent regulatory effect. | Editing produces a regulatory effect that is reduced or altered by TFAP2A perturbation; the expression direction is not established. | Any reproducible TF-dependent effect is expected to depend on EBF4 rather than TFAP2A. | Any reproducible TF-dependent effect is expected to depend on TFAP2E rather than TFAP2A. | Any reproducible TF-dependent effect is expected to depend on ETV3 rather than TFAP2A. |

## Next experiment

Perform allele-specific TFAP2A CUT&RUN or ChIP-qPCR at the variant in genotyped HCT 116 cells, comparing occupancy on ref and alt alleles. This is the cheapest proposed test that distinguishes the leading null chain from the leading TF-mediated chain, although it would not by itself establish a target gene or disease effect.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- gene_disease({"gene": "PYDC2"}) for H1.phenotype (and the shared PYDC2-to-colorectal-cancer link in H2 and H3), ran as [E15](#e15). Expected: If Open Targets reports colorectal-cancer association evidence for PYDC2, the phenotype link gains support and the PYDC2 chains rise relative to the null; if it reports no association, the phenotype link remains unsupported.

- Result of gene_disease({"gene":"PYDC2"}): Open Targets reports no association between PYDC2 and colorectal cancer (E15). The phenotype link therefore remains unsupported. (as expected: yes)

Chains after revision: null 0.94; TFAP2E 0.03; EBF4 0.02; ETV3 0.01. Link grades changed: H1.cell_type: weak → supported, H2.cell_type: weak → supported, H3.cell_type: weak → supported.

### Round 2

- literature_search({"query": "chr3:191441666 colorectal cancer regulatory variant"}) for H1.phenotype, ran as [E16](#e16). Expected: If the search finds variant-specific functional or colorectal-cancer evidence, H1.phenotype could improve and the null probability could fall; if it finds no relevant evidence, the phenotype link remains missing.
- literature_search({"query": "TFAP2E EBF4 ETV3 PYDC2 colorectal cancer HCT 116 regulation"}) for H1.gene, ran as [E17](#e17). Expected: If abstracts report direct regulation of PYDC2 or relevant perturbation evidence in colorectal cancer cells, the gene link could improve and help distinguish the TF hypotheses; if not, proximity remains the only support for PYDC2.

- Result of literature_search({"query": "chr3:191441666 colorectal cancer regulatory variant"}) for H1.phenotype: E16 reports zero literature hits for the query; no variant-specific functional or colorectal-cancer evidence was found. (as expected: yes)
- Result of literature_search({"query": "TFAP2E EBF4 ETV3 PYDC2 colorectal cancer HCT 116 regulation"}) for H1.gene: E17 reports zero literature hits for the query; no direct PYDC2 regulation or relevant colorectal-cancer cell perturbation evidence was found. (as expected: yes)

Chains after revision: null 0.98; EBF4 0.01; TFAP2E 0.01; ETV3 0.01. Link grades changed: H1.element: weak → supported, H2.element: weak → supported, H3.element: weak → supported.

### Round 3

- qbic_tf_detail({"tf": "ETV3"}) for H3.binding, ran as [E18](#e18). Expected: If ETV3 has an ETV3-specific QBiC-SELEX model with the same alt-over-ref effect, H3.binding becomes more specifically supported and H3 rises; if it is represented only by the mapped ETV5 model or has no covered model, the claim remains weak or falls.
- qbic_tf_detail({"tf": "TFAP2A"}) for H1.binding, ran as [E19](#e19). Expected: If TFAP2A has a distinct model or stronger allele-specific evidence than TFAP2E, that could favor TFAP2A over H1's TF choice; if it shares only the TFAP2E-mapped prediction, it confirms that the current evidence does not distinguish TFAP2E from related AP-2 factors.
- literature_search({"query": "PYDC2 colorectal cancer TFAP2E EBF4 ETV3 regulation"}) for H1.phenotype, ran as [E20](#e20). Expected: If the search finds direct evidence connecting PYDC2 or TFAP2E to colorectal cancer regulation, H1.phenotype could gain support and the null could lose weight; if it returns no relevant mechanistic evidence, the phenotype link remains missing.

- Result of qbic_tf_detail({"tf":"ETV3"}): ETV3's own model has an alt-over-ref effect but does not pass the detection gate; the stronger gated mapped-model results are from other ETS-family models. The ETV5-mapped signal therefore does not establish an ETV3-specific effect. (as expected: yes)
- Result of qbic_tf_detail({"tf":"TFAP2A"}): TFAP2A has its own model predicting ref-over-alt binding, while the TFAP2E-mapped result is also seen for related AP-2 factors. This gives a TFAP2A-specific model result but still no occupancy evidence. (as expected: yes)
- Result of literature_search({"query":"PYDC2 colorectal cancer TFAP2E EBF4 ETV3 regulation"}): The search returned no relevant literature hits, adding no support for a PYDC2 or TF-mediated colorectal-cancer phenotype link. (as expected: yes)

Chains after revision: null 0.97; TFAP2A 0.01; EBF4 0.01; TFAP2E 0.01; ETV3 0.00. Link grades changed: H1.element: supported → weak, H2.element: supported → weak, H3.binding: weak → missing, H3.element: supported → weak, H4.binding: absent → weak, H4.cell_type: absent → supported, H4.element: absent → weak, H4.gene: absent → weak, H4.phenotype: absent → missing.

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

<a id="e15"></a>**E15** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:40:48+00:00)

> Open Targets: no association between PYDC2 and colorectal cancer (MONDO_0005575).

<a id="e16"></a>**E16** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr3%3A191441666%20colorectal%20cancer%20regulatory%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:14:33+00:00)

> Europe PMC: 0 hits for 'chr3:191441666 colorectal cancer regulatory variant'; top 0 with PMIDs:

<a id="e17"></a>**E17** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TFAP2E%20EBF4%20ETV3%20PYDC2%20colorectal%20cancer%20HCT%20116%20regulation&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:14:33+00:00)

> Europe PMC: 0 hits for 'TFAP2E EBF4 ETV3 PYDC2 colorectal cancer HCT 116 regulation'; top 0 with PMIDs:

<a id="e18"></a>**E18** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ETV3","symbol":"ETV3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr3:191441666:T>G","gate_p":5.02e-05,"models":[{"model":"ETV3_NA_TCAGGA20NCG_ESW_yang2017_1_4_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.775,"effect":0.115,"z":3.5,"p":0.00047,"rank_abs_z":"283/997","passed_gate":false,"site_strength":{"ref_percentile":72.7,"alt_percentile":95.9,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":-0.231,"z":-7.84,"p":4.3e-15,"rank_abs_z":"28/997","passed_gate":true,"site_strength":{"ref_percentile":72.6,"alt_percentile":86.8,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":-0.705,"z":-4.96,"p":7e-07,"rank_abs_z":"139/997","passed_gate":true,"site_strength":{"ref_percentile":66.1,"alt_percentile":83.2,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":-0.291,"z":-3.78,"p":0.00016,"rank_abs_z":"250/997","passed_gate":false,"site_strength":{"ref_percentile":91.9,"alt_percentile":80.7,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":0.124,"z":0.97,"p":0.33,"rank_abs_z":"725/997","passed_gate":false,"site_strength":{"ref_percentile":68.6,"alt_percentile":70.8,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":0.149,"z":1.6,"p":0.11,"rank_abs_z":"594/997","passed_gate":false,"site_strength":{"ref_percentile":74.8,"alt_percentile":96.5,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":0.138,"z":2.01,"p":0.044,"rank_abs_z":"527/997","passed_gate":false,"site_strength":{"ref_percentile":75.0,"alt_percentile":74.1,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.125,"z":3.97,"p":7.3e-05,"rank_abs_z":"222/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":94.1,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":0.217,"z":1.72,"p":0.085,"rank_abs_z":"571/997","passed_gate":false,"site_strength":{"ref_percentile":80.6,"alt_percentile":93.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":-0.236,"z":-3.54,"p":0.00039,"rank_abs_z":"275/997","passed_gate":false,"site_strength":{"ref_percentile":95.1,"alt_percentile":95.7,"k":7}}],"n_models_trimmed":8}

<a id="e19"></a>**E19** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TFAP2A","symbol":"TFAP2A","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr3:191441666:T>G","gate_p":5.02e-05,"models":[{"model":"TCFAP2A_NA_TGATCC20NCG_ESP_yang2017_0_4_7mer","mapping":"own","group":"G030 AP-2, 4 models","quality":0.927,"effect":-2.475,"z":-16.2,"p":4.7e-59,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":99.8,"alt_percentile":99.4,"k":7}},{"model":"TFAP2B_FL_TGTCCG20NGA_KH_nitta2015_1_3_7mer","mapping":"CIS-BP (TFAP2B)","group":"G030 AP-2, 4 models","quality":0.77,"effect":-0.77,"z":-13.18,"p":1.2e-39,"rank_abs_z":"8/997","passed_gate":true,"site_strength":{"ref_percentile":99.8,"alt_percentile":98.8,"k":7}},{"model":"TFAP2C_eDBD_TGAGCT40NGCA_KP_yin2017_0_4_7mer","mapping":"CIS-BP (TFAP2C)","group":"G030 AP-2, 4 models","quality":0.753,"effect":-0.336,"z":-5.14,"p":2.7e-07,"rank_abs_z":"126/997","passed_gate":true,"site_strength":{"ref_percentile":97.2,"alt_percentile":98.2,"k":7}},{"model":"TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer","mapping":"CIS-BP (TFAP2E)","group":"G030 AP-2, 4 models","quality":0.88,"effect":-0.765,"z":-18.37,"p":2.5e-75,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":99.7,"alt_percentile":99.6,"k":7}}]}

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PYDC2%20colorectal%20cancer%20TFAP2E%20EBF4%20ETV3%20regulation&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:16:07+00:00)

> Europe PMC: 0 hits for 'PYDC2 colorectal cancer TFAP2E EBF4 ETV3 regulation'; top 0 with PMIDs:
