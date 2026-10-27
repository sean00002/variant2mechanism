# rs11629191 and Breast cancer

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 243 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: CREB3L2 (z -60.99); CREB3L4 (z -49.16); TET3 (z -44.11); MEIS3 (z -38.69); TGIF1 (z -38.69). Diagnostic, not shown to the model: 445 of 997 models pass Bonferroni.

## Ranked chains

### 1. H4: Null: no TF-mediated effect of rs11629191 (p = 0.95)

Null chain: no TF-mediated effect of this variant.

Predictions: Relevant-cell assays will show no reproducible allele-dependent TF occupancy or TF-mediated regulatory effect of editing this base.; Any later disease association may be absent or may arise from another linked variant or mechanism rather than a TF-mediated effect of rs11629191.

Falsified if: Relevant-cell experiments demonstrate allele-dependent TF occupancy and a causal TF-dependent regulatory effect of editing rs11629191.

### 2. H1: Candidate CREB3L4-mediated effect at an unannotated site (p = 0.02)

TF CREB3L4 (QBiC-SELEX coverage own_model), ref allele binds more; element A regulatory element overlapping the variant is hypothetical.; gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger binding to ref C than alt T using a model mapped from CREB3L2, but there is no occupancy evidence. CREB3L4 is retained as a testable candidate because it is expressed in MCF7 and more highly expressed there than CREB3L2; that does not establish which factor, if any, binds this site. | weak | [E04](#e04), [E09](#e09), [E10](#e10), [E11](#e11), [E15](#e15) |
| element | No annotated cCRE overlaps the variant, so a regulatory element at this position remains hypothetical. | supported | [E01](#e01), [E03](#e03) |
| gene | PELI2 is a provisional target because it is the closest listed protein-coding gene by TSS, but the supplied data do not connect this variant to its expression; the reported molecular QTL is low-PIP and in brain, and there is no significant GTEx eQTL. | weak | [E02](#e02), [E06](#e06), [E07](#e07), [E16](#e16) |
| cell_type | MCF7 is a context in which CREB3L4 is expressed, but binding at the variant or activity of a local element in this cell line has not been shown. | supported | [E04](#e04), [E11](#e11), [E15](#e15) |
| phenotype | A contribution to breast-cancer risk is speculative: no supplied evidence links this variant to breast cancer or establishes a PELI2-mediated effect on the disease. | supported | [E05](#e05), [E08a](#e08a), [E17](#e17) |

Predictions: If this chain is correct, a sensitive CREB3L4 occupancy assay in relevant breast cells should detect binding at the site, with greater occupancy on ref than alt.; Editing ref to alt should produce a CREB3L4-dependent regulatory effect and, if PELI2 is the target, a reproducible change in PELI2 expression; the expression direction is not predicted by binding alone.

Falsified if: Sensitive assays detect no CREB3L4 occupancy at the site in relevant cells, and allele editing produces no CREB3L4-dependent local regulatory or PELI2 expression effect.

### 3. H2: Candidate TGIF1-mediated effect at an unannotated site (p = 0.01)

TF TGIF1 (QBiC-SELEX coverage own_model), ref allele binds more; element A regulatory element overlapping the variant is hypothetical.; gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger binding to ref C than alt T using a TGIF2-mapped model, but there is no TGIF1 occupancy evidence and the model does not distinguish TGIF1 from related factors such as MEIS3. TGIF1 is a testable candidate because it is expressed in MCF7, not because expression establishes it as the binder. | weak | [E04](#e04), [E09](#e09), [E13](#e13), [E14](#e14) |
| element | No annotated cCRE overlaps the variant, so a regulatory element at this position remains hypothetical. | supported | [E01](#e01), [E03](#e03) |
| gene | PELI2 is a provisional target based on proximity alone; the supplied data do not show that this variant regulates it. | weak | [E02](#e02), [E06](#e06), [E07](#e07), [E16](#e16) |
| cell_type | TGIF1 is expressed in MCF7, but neither occupancy at the variant nor activity of a local element in this cell line is demonstrated. | supported | [E04](#e04), [E14](#e14) |
| phenotype | A TGIF1-dependent effect on PELI2 contributing to breast-cancer risk is speculative and is not established by the supplied evidence. | supported | [E05](#e05), [E08a](#e08a), [E17](#e17) |

Predictions: If this chain is correct, a sensitive TGIF1 occupancy assay should detect binding at the site, greater on ref than alt; a MEIS3-specific assay would not account for the proposed TGIF1-dependent effect.; TGIF1 perturbation should diminish any allele-dependent regulatory effect of editing the site and any resulting PELI2 expression change.

Falsified if: TGIF1 does not occupy the site in relevant cells, or allele editing produces no TGIF1-dependent regulatory effect.

### 4. H3: Candidate TET3-mediated effect at an unannotated site (p = 0.01)

TF TET3 (QBiC-SELEX coverage own_model), ref allele binds more; element A regulatory element overlapping the variant is hypothetical.; gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger binding to ref C than alt T using a model mapped from CXXC4. TET3 is expressed in MCF7, but its occupancy at the variant is unknown; the in-vitro prediction does not establish TET3 binding in cells. | weak | [E04](#e04), [E09](#e09), [E12](#e12) |
| element | No annotated cCRE overlaps the variant, so a regulatory element at this position remains hypothetical. | supported | [E01](#e01), [E03](#e03) |
| gene | PELI2 is a provisional target based on proximity alone; the supplied data do not show that this variant regulates it. | weak | [E02](#e02), [E06](#e06), [E07](#e07), [E16](#e16) |
| cell_type | TET3 is expressed in MCF7, but occupancy at the variant and local element activity in this cell line are not demonstrated. | supported | [E04](#e04), [E12](#e12) |
| phenotype | A TET3-dependent effect on PELI2 contributing to breast-cancer risk is speculative and is not established by the supplied evidence. | supported | [E05](#e05), [E08a](#e08a), [E17](#e17) |

Predictions: If this chain is correct, a sensitive TET3 occupancy assay should detect binding at the site, greater on ref than alt.; TET3 perturbation should modify any allele-dependent regulatory effect of editing the site and any resulting PELI2 expression change.

Falsified if: TET3 does not occupy the site in relevant cells, or allele editing produces no TET3-dependent regulatory effect.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Targeted allele-specific CREB3L4 CUT&RUN-qPCR at rs11629191 in MCF7, with suitable positive controls | low | yes | No reproducible CREB3L4 occupancy at the site. | Detect CREB3L4 occupancy at the site, with greater signal from ref than alt. | No specific prediction of CREB3L4 occupancy; TGIF1 is the proposed factor. | No specific prediction of CREB3L4 occupancy; TET3 is the proposed factor. |
| Allele-specific CUT&RUN or CUT&Tag for TGIF1 at the variant in MCF7 | medium | no | No reproducible TGIF1 occupancy at the site. | No specific prediction of TGIF1 occupancy; CREB3L4 is the proposed factor. | Detect TGIF1 occupancy at the site, with greater signal from ref than alt. | No specific prediction of TGIF1 occupancy; TET3 is the proposed factor. |
| Allele-specific CUT&RUN or CUT&Tag for TET3 at the variant in MCF7 | medium | no | No reproducible TET3 occupancy at the site. | No specific prediction of TET3 occupancy; CREB3L4 is the proposed factor. | No specific prediction of TET3 occupancy; TGIF1 is the proposed factor. | Detect TET3 occupancy at the site, with greater signal from ref than alt. |
| Base-edit rs11629191 in isogenic MCF7 cells and measure local regulatory activity and PELI2 expression, with TF perturbation | high | no | Editing causes no reproducible TF-dependent local regulatory or PELI2 expression effect. | Editing causes a CREB3L4-dependent regulatory effect and possibly a PELI2 expression change; the direction of expression change is unspecified. | Editing causes a TGIF1-dependent regulatory effect and possibly a PELI2 expression change; the direction of expression change is unspecified. | Editing causes a TET3-dependent regulatory effect and possibly a PELI2 expression change; the direction of expression change is unspecified. |

## Next experiment

Perform targeted allele-specific CREB3L4 CUT&RUN-qPCR at rs11629191 in MCF7, with positive controls. It is the cheapest proposed test that directly distinguishes the top two chains, H4 and H1; a negative result would weaken H1 but would not by itself prove the null.

## Investigate calls

- chip_peaks({"tf": "CREB3L4", "biosample": "MCF-7"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- gene_disease({"gene": "PELI2"})

## Flags

- literature_fallback: no hits for 'rs11629191 AND PELI2 AND "breast cancer"'; dropped the rsID

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/14:55887040-55887040:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:32:49+00:00)

> Variant chr14:55887040:C>T (GRCh38), allele string C/T
> Known IDs: rs11629191
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: -3.12
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/14:54887040-56887040?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:40+00:00)

> 14 protein-coding genes within 1000 kb of chr14:55887040:C>T, by distance to TSS:
> PELI2: 230.8 kb from TSS (upstream, strand +1)
> KTN1: 328.0 kb from TSS (downstream, strand +1)
> TBPL2: 430.3 kb from TSS (upstream, strand -1)
> ATG14: 475.2 kb from TSS (upstream, strand -1)
> TMEM260: 601.3 kb from TSS (upstream, strand +1)
> CHMP4BP1: 615.7 kb from TSS (downstream, strand +1)
> FBXO34: 615.7 kb from TSS (downstream, strand +1)
> DLGAP5: 695.4 kb from TSS (upstream, strand -1)
> LGALS3: 765.7 kb from TSS (downstream, strand +1)
> MAPK1IP1L: 835.4 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:13+00:00)

> No cCRE overlaps the variant; nearest is EH38E1716463 (dELS) 1868 bp away.
> SCREEN: 0 cCREs within 500 bp (max z-score across ENCODE biosamples):
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> No ENCODE TF ChIP-seq peak contains chr14:55887040:C>T in any biosample. In the matching biosample MCF-7: 0 peaks from 0 factors. No cCRE contains the variant. Of the TFs with a binding model, 65 were assayed in the matching biosample and 508 only elsewhere, all without a peak here; 536 were never assayed.

<a id="e05"></a>**E05** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs11629191&size=100; retrieved 2026-10-25T17:32:50+00:00)

> 0 GWAS Catalog associations for rs11629191, strongest first:

<a id="e06"></a>**E06** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:49+00:00)

> 1 credible sets contain 14_55887040_C_T: 0 GWAS, 1 molecular QTL.
> eqtl for ENSG00000259868 (gtex-v10_ge_brain_nucleus_accumbens_ensg0000025986): PIP 0.03

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e08"></a>**E08** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PELI2%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:50+00:00)

> Europe PMC: 178 hits for 'PELI2 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41023515 (2025): Pellino ubiquitin ligases: double-edged swords in hematologic malignancies-from oncogenic stabilizers to therapeutic vulnerabilities.
> PMID 41331176 (2025): Construction and validation of risk models of prognostic genes associated with parthanatos in papillary thyroid carcinoma based on bioinformatics.
> PMID 40362379 (2025): &lt;i&gt;O&lt;/i&gt;-Desmethyltramadol Enhanced Anti-Cancer Efficacy over Tramadol Through Non-μ-Opioid Receptor and Differential Cellular Contexts of Human Breast Cancer Cells.
> PMID 42757486 (2026): Pemetrexed increases BRCA1 protein stability and sensitizes TNBC cells to radiotherapy.
> PMID 42734444 (2027): Anesthesia inhalation agent sevoflurane induces perioperative cognitive impairment: Apelin/early growth response 1 axis induces ferritinophagy and exacerbates ferroptosis.
> PMID 41079921 (2025): PRMT1/PRMT5-Mediated Differential Arginine Methylation of CRIP1 Promotes the Recurrence of Small Cell Lung Cancer after Chemotherapy.
> PMID 42380137 (2026): HOXC9 accelerates esophageal squamous cell carcinoma progression via OTUD1-FABP5-mediated lipid metabolic reprogramming.

<a id="e08a"></a>**E08a** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-25T17:32:50+00:00)

> ResultsSeven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr14:55887040:C>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000019), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 0 of 0 occupied (0 with a strong site), 5 of 113 with unknown occupancy. Left out: 65 TFs assayed in the matching biosample and 508 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element. No ENCODE TF ChIP-seq peak contains this variant in any biosample; QBiC-SELEX changes below have no occupancy support.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CREB3L2 (bZIP, 4 models; QBiC-SELEX coverage: own model): best model CREB3L1_NA_TAAACA20NCAA_ESY_yang2017_0_3_7mer (a CIS-BP-mapped model of CREB3L1), z -60.99, effect -2.258: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.06 TPM, rank 534 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 99.6th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CREB3L4 (bZIP, 4 models; QBiC-SELEX coverage: own model): best model CREB3L2_NA_TAACGG20NGCA_ESZ_yang2017_0_4_7mer (a CIS-BP-mapped model of CREB3L2), z -49.16, effect -2.335: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 48.8 TPM, rank 68 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 91.6th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TET3 (CxxC, 2 models; QBiC-SELEX coverage: own model): best model CXXC4_FL_GG40NTAGTTT_YWKC_jolma2025_0_4_7mer (a CIS-BP-mapped model of CXXC4), z -44.11, effect -2.102: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.96 TPM, rank 419 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 98.8th, alt 70.2th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MEIS3 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model TGIF2_eDBD_TTGCAA40NGTG_KO_yin2017_0_4_7mer (a CIS-BP-mapped model of TGIF2), z -38.69, effect -2.43: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.61 TPM, rank 272 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.8th, alt 94.1th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TGIF1 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): best model TGIF2_eDBD_TTGCAA40NGTG_KO_yin2017_0_4_7mer (a CIS-BP-mapped model of TGIF2), z -38.69, effect -2.43: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 39.86 TPM, rank 95 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.8th, alt 94.1th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:50:38+00:00)

> No ENCODE CREB3L4 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no CREB3L4 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e16"></a>**E16** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e17"></a>**E17** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:03+00:00)

> Open Targets: PELI2 and breast cancer (MONDO_0007254), overall score 0.00; by evidence type: literature 0.01
