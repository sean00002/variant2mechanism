# rs11629191 and Breast cancer

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 124 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: CREB3L2 (z -60.99); CREB3L4 (z -49.16); TET3 (z -44.11); MEIS3 (z -38.69); TGIF1 (z -38.69). Diagnostic, not shown to the model: 445 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.92)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not produce a reproducible allele-dependent TF-mediated regulatory effect in relevant breast cells. Any disease association would require another explanation.

Falsified if: A reproducible, variant-dependent TF occupancy and regulatory effect is demonstrated and linked to a target gene and breast-cancer-relevant phenotype.

### 2. H1: Speculative CREB3L4-mediated regulation (p = 0.04)

TF CREB3L4 (QBiC-SELEX coverage own_model), ref allele binds more; element Unestablished regulatory element overlapping the variant; gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB3L4 is expressed in MCF7, and its QBiC-SELEX result, based on a CREB3L1-mapped model rather than a direct CREB3L4 model, predicts stronger binding to ref C than alt T; occupancy at this site is unknown. | weak | [E11](#e11) |
| element | This chain hypothesizes a regulatory element at the variant, but no overlapping regulatory annotation or cCRE is reported. | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is a speculative target because it is the nearest listed protein-coding gene; no regulatory connection from the variant to PELI2 is shown. | weak | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is a nominated context because CREB3L4 is expressed there, not because locus occupancy or regulatory activity is established. | weak | [E11](#e11) |
| phenotype | A PELI2-mediated breast-cancer consequence is unestablished: Open Targets reports no association score, and the cited PELI2 literature does not establish this proposed breast-cancer mechanism. | missing | [E15](#e15), [E16](#e16), [E16a](#e16a), [E16b](#e16b) |

Predictions: A reporter containing the ref and alt sequences should show an allele-dependent effect that is reduced by CREB3L4 depletion; the direction of reporter activity is not established by the binding prediction.; If PELI2 is the target, perturbing the variant or CREB3L4 should alter PELI2 regulation more consistently than other nearby genes.

Falsified if: A suitably sensitive assay finds no CREB3L4-dependent allele effect at the sequence or endogenous locus.; Perturbing the variant or CREB3L4 has no detectable effect on PELI2 regulation.

### 3. H2: Speculative TGIF1-mediated regulation (p = 0.03)

TF TGIF1 (QBiC-SELEX coverage own_model), ref allele binds more; element Unestablished regulatory element overlapping the variant; gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TGIF1 is expressed in MCF7. Its own QBiC-SELEX model weakly predicts alt-favoring binding but does not pass the detection gate; related-factor mapped models, including the TGIF2 model, predict ref-favoring binding. Thus ref is the tentative direction from the mapped models, not a robust TGIF1-specific result, and occupancy is unknown. | weak | [E14](#e14), [E17](#e17) |
| element | This chain hypothesizes a regulatory element at the variant, but no overlapping regulatory annotation or cCRE is reported. | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is a speculative target based on proximity alone; no variant-to-PELI2 regulatory connection is shown. | weak | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is a nominated context because TGIF1 is expressed there; locus occupancy or regulatory activity has not been established. | weak | [E14](#e14), [E17](#e17) |
| phenotype | A PELI2-mediated breast-cancer consequence is unestablished; the available association and literature results do not establish this mechanism. | missing | [E15](#e15), [E16](#e16), [E16a](#e16a), [E16b](#e16b) |

Predictions: A TGIF1-specific perturbation should change any allele-dependent regulatory effect more than CREB3L4 or TET3 perturbation; the direction of downstream activity is unknown.; If PELI2 is the target, the allele-dependent effect should be detectable at PELI2 rather than inferred from proximity alone.

Falsified if: TGIF1-specific assays show no allele-dependent binding or regulatory effect at the locus.; TGIF1 or variant perturbation does not alter PELI2 regulation.

### 4. H3: Speculative TET3-mediated regulation (p = 0.02)

TF TET3 (QBiC-SELEX coverage own_model), ref allele binds more; element Unestablished regulatory element overlapping the variant; gene PELI2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TET3 is expressed in MCF7, and a QBiC-SELEX model mapped from CXXC4 predicts stronger binding to ref C than alt T; this is an in-vitro prediction, not direct evidence of TET3 occupancy. | weak | [E12](#e12) |
| element | This chain hypothesizes a regulatory element at the variant, but no overlapping regulatory annotation or cCRE is reported. | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is a speculative target based on proximity alone; no variant-to-PELI2 regulatory connection is shown. | weak | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is a nominated context because TET3 is expressed there; locus occupancy or regulatory activity has not been established. | weak | [E12](#e12) |
| phenotype | A PELI2-mediated breast-cancer consequence is unestablished; the available association and literature results do not establish this mechanism. | missing | [E15](#e15), [E16](#e16), [E16a](#e16a), [E16b](#e16b) |

Predictions: A TET3-specific perturbation should change any allele-dependent regulatory effect more than CREB3L4 or TGIF1 perturbation; the direction of downstream activity is unknown.; If PELI2 is the target, the allele-dependent effect should be detectable at PELI2 rather than inferred from proximity alone.

Falsified if: TET3-specific assays show no allele-dependent binding or regulatory effect at the locus.; TET3 or variant perturbation does not alter PELI2 regulation.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Dual-allele sequence reporter in MCF7 with and without CREB3L4 depletion | medium | yes | No reproducible allele-dependent reporter effect, or any effect is not specifically changed by CREB3L4 depletion. | An allele-dependent reporter effect is reduced by CREB3L4 depletion; the direction of activity is not predicted. | No CREB3L4-specific dependence; an effect, if present, should instead depend on TGIF1. | No CREB3L4-specific dependence; an effect, if present, should instead depend on TET3. |
| Allele-specific CUT&RUN or ChIP for CREB3L4, TGIF1, and TET3 in relevant breast cells | high | yes | No reproducible variant-centered, allele-biased occupancy for the candidate TFs. | CREB3L4 occupancy is detected and favors ref C. | TGIF1 occupancy is detected; the mapped-model direction predicts ref C, but its own model does not give a detectable direction. | TET3 occupancy is detected and favors ref C. |
| Endogenous allele editing followed by expression measurement of PELI2 and other nearby genes, with candidate-TF perturbation | high | yes | Editing produces no reproducible candidate-TF-dependent expression change. | Editing changes PELI2 regulation in a CREB3L4-dependent manner. | Editing changes PELI2 regulation in a TGIF1-dependent manner. | Editing changes PELI2 regulation in a TET3-dependent manner. |

## Next experiment

Run the dual-allele sequence reporter in MCF7 with and without CREB3L4 depletion. It is the least costly proposed test of the top two chains, H0 and H1; a reproducible CREB3L4-dependent allele effect would distinguish H1 from the null, though it would not by itself establish PELI2 as the target.

## Refinement rounds

Stopped: round 1 left the top chain and the grades of its links unchanged.

### Round 1

- gene_disease({"gene": "PELI2"}) for H1.phenotype, ran as [E15](#e15). Expected: If Open Targets reports breast-cancer association evidence for PELI2, this modestly supports the proposed gene-to-disease link for H1 and the other PELI2 chains, but does not establish that this variant regulates PELI2. If it reports none, the phenotype link remains unsupported.
- literature_search({"query": "PELI2 breast cancer functional mechanism"}) for H2.phenotype, ran as [E16](#e16). Expected: If abstracts provide direct evidence that PELI2 affects breast-cancer biology, the phenotype link gains gene-level support for PELI2 chains, without proving a variant-to-gene mechanism. If results are absent or indirect, the link remains weak.
- qbic_tf_detail({"tf": "TGIF1"}) for H2.binding, ran as [E17](#e17). Expected: If TGIF1 has a TF-specific model with a detectable ref-favoring effect, H2.binding gains more direct support and H2 may rise relative to chains relying only on related-TF models. If coverage is only mapped from TGIF2 or the direction is unclear, H2 remains prediction-only and does not gain an advantage.

- Result of gene_disease({"gene":"PELI2"}) for H1.phenotype: E15 reports an overall Open Targets score of 0.00 for PELI2 and breast cancer, with literature evidence scored 0.01. This does not support a breast-cancer link for PELI2. (as expected: yes)
- Result of literature_search({"query":"PELI2 breast cancer functional mechanism"}) for H2.phenotype: E16 returns search hits but no direct PELI2 breast-cancer functional mechanism in the supplied results. E16a and E16b describe PELI2 as a negative regulator of STING signaling, not a link to this variant or breast cancer. (as expected: yes)
- Result of qbic_tf_detail({"tf":"TGIF1"}) for H2.binding: E17 shows a TGIF1 own-model effect that weakly favors alt T but does not pass the detection gate. Several related-factor mapped models favor ref C, including the TGIF2 model; this does not provide a detectable TGIF1-specific advantage. (as expected: yes)

Chains after revision: null 0.92; CREB3L4 0.04; TGIF1 0.03; TET3 0.02. Link grades changed: none.

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

<a id="e15"></a>**E15** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:03+00:00)

> Open Targets: PELI2 and breast cancer (MONDO_0007254), overall score 0.00; by evidence type: literature 0.01

<a id="e16"></a>**E16** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PELI2%20breast%20cancer%20functional%20mechanism&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T23:25:28+00:00)

> Europe PMC: 137 hits for 'PELI2 breast cancer functional mechanism'; top 7 with PMIDs:
> PMID 41023515 (2025): Pellino ubiquitin ligases: double-edged swords in hematologic malignancies-from oncogenic stabilizers to therapeutic vulnerabilities.
> PMID 41331176 (2025): Construction and validation of risk models of prognostic genes associated with parthanatos in papillary thyroid carcinoma based on bioinformatics.
> PMID 42060612 (2026): Unraveling the role of ChREBP in lung adenocarcinoma: Expression, regulatory networks, and potential functional impact.
> PMID 42757486 (2026): Pemetrexed increases BRCA1 protein stability and sensitizes TNBC cells to radiotherapy.
> PMID 42734444 (2027): Anesthesia inhalation agent sevoflurane induces perioperative cognitive impairment: Apelin/early growth response 1 axis induces ferritinophagy and exacerbates ferroptosis.
> PMID 40362379 (2025): &lt;i&gt;O&lt;/i&gt;-Desmethyltramadol Enhanced Anti-Cancer Efficacy over Tramadol Through Non-μ-Opioid Receptor and Differential Cellular Contexts of Human Breast Cancer Cells.
> PMID 38917796 (2024): PELI2 is a negative regulator of STING signaling that is dynamically repressed during viral infection.

<a id="e16a"></a>**E16a** literature_search, Europe PMC abstract, PMID 38917796 (https://europepmc.org/article/MED/38917796; retrieved 2026-10-26T23:25:28+00:00)

> Here, we discover PELI2 as a crucial negative regulator of STING.

<a id="e16b"></a>**E16b** literature_search, Europe PMC abstract, PMID 38917796 (https://europepmc.org/article/MED/38917796; retrieved 2026-10-26T23:25:28+00:00)

> Mechanistically, PELI2 inhibits the transcription factor IRF3 by binding to phosphorylated Thr354 and Thr356 on the C-terminal tail of STING, leading to ubiquitination and inhibition of the kinase TBK1.

<a id="e17"></a>**E17** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TGIF1","symbol":"TGIF1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr14:55887040:C>T","gate_p":5.02e-05,"models":[{"model":"TGIF1_NA_TATGGG20NGGG_ESY_yang2017_0_4_7mer","mapping":"own","group":"G008 Homeodomain, 9 models","quality":0.695,"effect":0.176,"z":3.51,"p":0.00045,"rank_abs_z":"501/997","passed_gate":false,"site_strength":{"ref_percentile":88.5,"alt_percentile":76.2,"k":7}},{"model":"MEIS1_NA_TGACCT20NGA_O_jolma2013_0_4_7mer","mapping":"CIS-BP (MEIS1)","group":"G008 Homeodomain, 9 models","quality":0.864,"effect":-1.129,"z":-10.67,"p":1.4e-26,"rank_abs_z":"91/997","passed_gate":true,"site_strength":{"ref_percentile":99.4,"alt_percentile":84.0,"k":7}},{"model":"MEIS2_FL_TTGTCG40NACC_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (MEIS2)","group":"G008 Homeodomain, 9 models","quality":0.833,"effect":-0.325,"z":-10.67,"p":1.4e-26,"rank_abs_z":"92/997","passed_gate":true,"site_strength":{"ref_percentile":96.6,"alt_percentile":83.1,"k":7}},{"model":"MEIS3_NA_TGGGTA20NGA_ESY_yang2017_0_2_7mer","mapping":"CIS-BP (MEIS3)","group":"G008 Homeodomain, 9 models","quality":0.858,"effect":-0.968,"z":-23.79,"p":4.6e-125,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":98.3,"alt_percentile":88.8,"k":7}},{"model":"PKNOX1_FL_TCGTCC40NGCC_KW_yin2017_0_4_7mer","mapping":"CIS-BP (PKNOX1)","group":"G008 Homeodomain, 9 models","quality":0.824,"effect":0.133,"z":3.99,"p":6.5e-05,"rank_abs_z":"449/997","passed_gate":false,"site_strength":{"ref_percentile":98.0,"alt_percentile":97.6,"k":7}},{"model":"PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (PKNOX2)","group":"G008 Homeodomain, 9 models","quality":0.673,"effect":-1.29,"z":-19.46,"p":2.5e-84,"rank_abs_z":"31/997","passed_gate":true,"site_strength":{"ref_percentile":98.6,"alt_percentile":80.8,"k":7}},{"model":"TGIF2_eDBD_TTGCAA40NGTG_KO_yin2017_0_4_7mer","mapping":"CIS-BP (TGIF2)","group":"G008 Homeodomain, 9 models","quality":0.877,"effect":-2.43,"z":-38.69,"p":0.0,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":99.8,"alt_percentile":94.1,"k":7}},{"model":"TGIF2LX_eDBD_TGAGAA40NGCG_KO_yin2017_0_4_7mer","mapping":"CIS-BP (TGIF2LX)","group":"G008 Homeodomain, 9 models","quality":0.762,"effect":-0.655,"z":-15.65,"p":3.4e-55,"rank_abs_z":"38/997","passed_gate":true,"site_strength":{"ref_percentile":98.3,"alt_percentile":83.0,"k":7}},{"model":"TGIF2LY_eDBD_TTGGCA40NTCG_KT_yin2017_0_4_7mer","mapping":"CIS-BP (TGIF2LY)","group":"G008 Homeodomain, 9 models","quality":0.957,"effect":-1.304,"z":-17.27,"p":8.5e-67,"rank_abs_z":"32/997","passed_gate":true,"site_strength":{"ref_percentile":97.8,"alt_percentile":90.9,"k":7}}]}
