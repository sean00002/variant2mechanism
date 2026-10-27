# rs11629191 and Breast cancer

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 157 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: CREB3L2 (z -60.99); CREB3L4 (z -49.16); TET3 (z -44.11); MEIS3 (z -38.69); TGIF1 (z -38.69). Diagnostic, not shown to the model: 445 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.95)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not show a reproducible, endogenous allele-dependent TF effect in relevant breast cells; any disease association would require another explanation.

Falsified if: A reproducible allele-dependent TF effect at this locus is demonstrated in relevant cells and connected to a target gene and breast-cancer-relevant phenotype.

### 2. H1: Candidate CREB3L4-mediated effect; regulatory element and target unresolved (p = 0.04)

TF CREB3L4 (QBiC-SELEX coverage own_model), ref allele binds more; element None; gene None; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB3L4 is the leading named candidate here because it is expressed in MCF7 and has an own-model QBiC-SELEX result predicting stronger in-vitro binding to ref C than alt T; a separate model mapped from CREB3L2 also favors ref, but neither result establishes occupancy, and no variant-overlapping CREB3L4 peak is reported. | weak | [E04](#e04), [E11](#e11), [E15](#e15), [E16](#e16) |
| element | A regulatory element overlapping the variant is not established; this chain would require an unannotated element not detected in the supplied annotations. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | No target gene can be assigned from the supplied evidence; PELI2 is nearby, but proximity does not establish regulation by this variant. | supported | [E02](#e02) |
| cell_type | MCF7 is a candidate context because CREB3L4 is expressed there, although locus occupancy or activity in MCF7 is not shown. | supported | [E04](#e04), [E11](#e11), [E16](#e16) |
| phenotype | A breast-cancer consequence is hypothetical; the supplied evidence does not connect this variant or a target gene to breast cancer. | supported | [E05](#e05), [E17](#e17) |

Predictions: If this chain is correct, an endogenous-locus assay in relevant breast cells should detect CREB3L4 occupancy, with more occupancy on ref C than alt T.; A regulatory effect should depend on CREB3L4 more than on TGIF1 or TET3; the target gene and the direction of any expression change are not specified by current evidence.

Falsified if: Sensitive assays in relevant cells find no CREB3L4 occupancy or no ref-favoring allelic occupancy at the locus.; CREB3L4 perturbation does not alter a reproducible variant-dependent regulatory effect.

### 3. H2: Candidate TGIF1-mediated effect; regulatory element and target unresolved (p = 0.01)

TF TGIF1 (QBiC-SELEX coverage own_model), ref allele binds more; element None; gene None; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TGIF1 is expressed in MCF7, and a QBiC-SELEX model mapped from TGIF2 predicts stronger in-vitro binding to ref C than alt T; TGIF1 occupancy at the variant is not shown. | weak | [E04](#e04), [E14](#e14) |
| element | A regulatory element overlapping the variant is not established; this chain would require an unannotated element not detected in the supplied annotations. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | No target gene can be assigned from the supplied evidence; proximity of PELI2 does not establish a regulatory connection. | supported | [E02](#e02) |
| cell_type | MCF7 is a candidate context because TGIF1 is expressed there, although locus occupancy or activity in MCF7 is not shown. | supported | [E04](#e04), [E14](#e14) |
| phenotype | A breast-cancer consequence is hypothetical; the supplied evidence does not connect this variant or a target gene to breast cancer. | supported | [E05](#e05), [E17](#e17) |

Predictions: If this chain is correct, an endogenous-locus assay should detect TGIF1 occupancy with more occupancy on ref C than alt T.; The variant-dependent effect should depend on TGIF1 more than on CREB3L4 or TET3; the target gene and direction of any expression change remain unspecified.

Falsified if: Sensitive assays in relevant cells find no TGIF1 occupancy or no ref-favoring allelic occupancy at the locus.; TGIF1 perturbation does not alter a reproducible variant-dependent regulatory effect.

### 4. H3: Candidate TET3-mediated effect; regulatory element and target unresolved (p = 0.01)

TF TET3 (QBiC-SELEX coverage own_model), ref allele binds more; element None; gene None; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TET3 is expressed in MCF7, and a QBiC-SELEX model mapped from CXXC4 predicts stronger in-vitro binding to ref C than alt T; TET3 occupancy at the variant is not shown. | weak | [E04](#e04), [E12](#e12) |
| element | A regulatory element overlapping the variant is not established; this chain would require an unannotated element not detected in the supplied annotations. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | No target gene can be assigned from the supplied evidence; proximity of PELI2 does not establish a regulatory connection. | supported | [E02](#e02) |
| cell_type | MCF7 is a candidate context because TET3 is expressed there, although locus occupancy or activity in MCF7 is not shown. | supported | [E04](#e04), [E12](#e12) |
| phenotype | A breast-cancer consequence is hypothetical; the supplied evidence does not connect this variant or a target gene to breast cancer. | supported | [E05](#e05), [E17](#e17) |

Predictions: If this chain is correct, an endogenous-locus assay should detect TET3 occupancy with more occupancy on ref C than alt T.; The variant-dependent effect should depend on TET3 more than on CREB3L4 or TGIF1; the target gene and direction of any expression change remain unspecified.

Falsified if: Sensitive assays in relevant cells find no TET3 occupancy or no ref-favoring allelic occupancy at the locus.; TET3 perturbation does not alter a reproducible variant-dependent regulatory effect.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Targeted TF-specific CUT&RUN-qPCR at the endogenous locus in MCF7 cells, measuring allelic occupancy for CREB3L4, TGIF1, and TET3 (using a suitable heterozygous line or reciprocal allele-edited cells). | medium | yes | No reproducible variant-overlapping occupancy with a consistent allele imbalance for these candidate TFs. | CREB3L4 occupancy is detected and is higher on ref C than alt T. | TGIF1 occupancy is detected and is higher on ref C than alt T. | TET3 occupancy is detected and is higher on ref C than alt T. |
| Compare C and T locus-fragment reporter constructs in MCF7 cells with and without individual CREB3L4, TGIF1, or TET3 perturbation. | medium | yes | No reproducible allele-dependent reporter effect, or no candidate-TF-specific dependence. | A reproducible C-versus-T reporter difference is reduced by CREB3L4 perturbation; the direction of reporter activity is not specified by the binding evidence. | A reproducible C-versus-T reporter difference is reduced by TGIF1 perturbation; the direction of reporter activity is not specified by the binding evidence. | A reproducible C-versus-T reporter difference is reduced by TET3 perturbation; the direction of reporter activity is not specified by the binding evidence. |

## Next experiment

Run targeted TF-specific CUT&RUN-qPCR at the endogenous locus in MCF7 cells, testing allelic occupancy for CREB3L4, TGIF1, and TET3. This is the least costly direct test proposed here that distinguishes the highest-probability null from the leading CREB3L4 candidate; first confirm that the cells or edited clones allow allelic comparison.

## Investigate calls

- qbic_tf_detail({"tf": "CREB3L4"})
- chip_peaks({"tf": "CREB3L4", "biosample": "MCF-7"})
- gene_disease({"gene": "PELI2"})

## Flags

- none

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

<a id="e15"></a>**E15** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"CREB3L4","symbol":"CREB3L4","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr14:55887040:C>T","gate_p":5.02e-05,"models":[{"model":"CREB3L4_eDBD_TAGGCT40NACC_KO_yin2017_0_3_7mer","mapping":"own","group":"G017 bZIP, 4 models","quality":0.941,"effect":-1.314,"z":-37.55,"p":1.4e-308,"rank_abs_z":"12/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":100.0,"k":7}},{"model":"CREB3L2_NA_TAACGG20NGCA_ESZ_yang2017_0_4_7mer","mapping":"CIS-BP (CREB3L2)","group":"G017 bZIP, 4 models","quality":0.796,"effect":-2.335,"z":-49.16,"p":0.0,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":91.6,"k":7}}]}

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:50:38+00:00)

> No ENCODE CREB3L4 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no CREB3L4 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e17"></a>**E17** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:03+00:00)

> Open Targets: PELI2 and breast cancer (MONDO_0007254), overall score 0.00; by evidence type: literature 0.01
