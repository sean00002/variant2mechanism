# rs11629191 and Breast cancer

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 13 model calls; 209 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: CREB3L2 (z -60.99); CREB3L4 (z -49.16); TET3 (z -44.11); MEIS3 (z -38.69); TGIF1 (z -38.69). Diagnostic, not shown to the model: 445 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.96)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible variant-dependent TF occupancy and regulatory effect will be found in relevant breast cells. Any disease association, if present, would need another explanation, such as a linked causal variant.

Falsified if: A reproducible effect of this base on TF occupancy and gene regulation is shown in relevant cells, with evidence that the effect depends on a named TF.

### 2. H1: Speculative CREB3L4-mediated regulation (p = 0.03)

TF CREB3L4 (QBiC-SELEX coverage own_model), ref allele binds more; element A regulatory element overlapping the variant is required by this chain but is not supported by the supplied annotations.; gene None; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB3L4 is expressed in MCF7, and its own QBiC-SELEX model predicts stronger in-vitro binding to ref C than alt T; a CREB3L2-mapped model gives the same direction. Neither result establishes occupancy, and no CREB3L4 peak at the variant is reported. | weak | [E11](#e11), [E15](#e15), [E16](#e16), [E04](#e04) |
| element | A regulatory element at the variant is only a possibility: no regulatory feature or cCRE overlaps it, and no TF ChIP-seq peak contains it. | missing | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | No target gene is established. PELI2 and other genes are nearby, but proximity does not show regulation by this variant; the reported molecular QTL is in brain and has low PIP. | missing | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is a plausible context because CREB3L4 is expressed there, but locus occupancy or regulatory activity in MCF7 is not demonstrated. | weak | [E11](#e11), [E16](#e16) |
| phenotype | A breast-cancer effect through this variant is unestablished. CREB3L4 literature cited here concerns gastric cancer, not a demonstrated breast-cancer effect of this variant. | missing | [E05](#e05), [E17](#e17), [E18a](#e18a), [E18b](#e18b) |

Predictions: A targeted assay should find CREB3L4-dependent, ref-favoring activity from the variant sequence; that activity should diminish when CREB3L4 is reduced.; This chain predicts a CREB3L4-dependent effect, unlike the TGIF1- or TET3-specific effects proposed by H2 and H3; it does not specify a target gene.

Falsified if: Sensitive assays in relevant cells find no CREB3L4 occupancy or no ref-favoring allele-specific effect.; A reproducible allele-dependent regulatory signal is unchanged by CREB3L4 perturbation.

### 3. H3: Speculative TET3-mediated regulation (p = 0.01)

TF TET3 (QBiC-SELEX coverage own_model), ref allele binds more; element A regulatory element overlapping the variant is required by this chain but is not supported by the supplied annotations.; gene None; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TET3 is expressed in MCF7. A QBiC-SELEX model mapped from CXXC4 predicts stronger in-vitro binding to ref C than alt T; this is not a TET3-specific model, and no occupancy at the variant is shown. | weak | [E12](#e12), [E04](#e04), [E09](#e09) |
| element | A regulatory element at the variant is only a possibility: no regulatory feature or cCRE overlaps it, and no TF ChIP-seq peak contains it. | missing | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | No target gene is established. Nearby genes are not shown to be regulated by this variant, and the reported low-PIP molecular QTL is in brain. | missing | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is a plausible context because TET3 is expressed there, but TET3 occupancy or regulatory activity at this locus is not demonstrated. | weak | [E12](#e12), [E04](#e04) |
| phenotype | The supplied literature gives breast-cancer context for TET-family changes and reports a TET3-related demethylation pathway implicated in TNBC progression. This makes a TET3 disease role biologically plausible, but does not connect this variant or its predicted binding change to that role. | weak | [E20a](#e20a), [E20b](#e20b), [E20c](#e20c), [E20d](#e20d), [E20e](#e20e), [E20f](#e20f) |

Predictions: If this chain is correct, a TET3-specific assay should show ref-favoring occupancy or activity, and perturbing TET3 should reduce the allele-dependent effect.; The effect should depend on TET3 rather than CREB3L4 or TGIF1; no target gene is specified.

Falsified if: TET3-specific occupancy or allele-dependent activity is absent in relevant cells.; TET3 perturbation does not change a reproducible allele-dependent regulatory signal.

### 4. H2: Speculative TGIF1-mediated regulation (p = 0.01)

TF TGIF1 (QBiC-SELEX coverage own_model), ref allele binds more; element A regulatory element overlapping the variant is required by this chain but is not supported by the supplied annotations.; gene None; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TGIF1 is expressed in MCF7. A QBiC-SELEX model mapped from TGIF2 predicts stronger in-vitro binding to ref C than alt T; this is not a TGIF1-specific model, and no occupancy at the variant is shown. | weak | [E14](#e14), [E04](#e04), [E09](#e09) |
| element | A regulatory element at the variant is only a possibility: no regulatory feature or cCRE overlaps it, and no TF ChIP-seq peak contains it. | missing | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | No target gene is established; gene proximity does not show that the variant regulates PELI2 or another nearby gene. | missing | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | MCF7 is a plausible context because TGIF1 is expressed there, but TGIF1 occupancy or regulatory activity at this locus is not demonstrated. | weak | [E14](#e14), [E04](#e04) |
| phenotype | The supplied literature includes breast-cancer-related findings involving MEIS inhibitors and TGIF1 expression, but does not show that TGIF1 perturbation mediates a breast-cancer phenotype at this variant. | weak | [E05](#e05), [E19a](#e19a), [E19b](#e19b) |

Predictions: If this chain is correct, a TGIF1-specific assay should show ref-favoring occupancy or activity, and perturbing TGIF1 should reduce the allele-dependent effect.; The effect should depend on TGIF1 rather than CREB3L4 or TET3; no target gene is specified.

Falsified if: TGIF1-specific occupancy or allele-dependent activity is absent in relevant cells.; TGIF1 perturbation does not change a reproducible allele-dependent regulatory signal.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Paired ref-C and alt-T reporter constructs in MCF7, tested with control treatment and CREB3L4 reduction | medium | yes | No reproducible allele-dependent reporter effect specifically reduced by CREB3L4 perturbation. | Ref construct has a CREB3L4-dependent activity difference relative to alt; reducing CREB3L4 weakens that difference. | No specific loss of the allele-dependent effect after CREB3L4 reduction; a TET3-dependent effect would require a separate test. | No specific loss of the allele-dependent effect after CREB3L4 reduction; a TGIF1-dependent effect would require a separate test. |
| Allele-resolved CUT&RUN or equivalent occupancy assay at the locus in MCF7 for CREB3L4, TGIF1, and TET3 | high | yes | No reproducible variant-overlapping occupancy supporting an allele-specific TF effect. | CREB3L4 occupancy is detected and favors ref C. | TET3 occupancy is detected and favors ref C. | TGIF1 occupancy is detected and favors ref C. |
| Isogenic editing of C to T and T to C in MCF7, followed by expression and chromatin profiling to identify a target | high | yes | No reproducible variant-dependent chromatin or gene-expression change attributable to this base. | Editing produces a reproducible regulatory change that depends on CREB3L4; the affected target remains to be identified. | Editing produces a reproducible regulatory change that depends on TET3; the affected target remains to be identified. | Editing produces a reproducible regulatory change that depends on TGIF1; the affected target remains to be identified. |

## Next experiment

Run the paired ref/alt reporter assay in MCF7 with and without CREB3L4 reduction. It is the least costly proposed test that directly distinguishes the leading non-null chain from the null, while recognizing that a reporter result would not by itself prove an endogenous target-gene or disease effect.

## Refinement rounds

Stopped: round 3: no new call to run (No available call is likely to change a link grade or separate the chains. ENCODE reports no variant-overlapping TF peak in any biosample (E04), so additional Factorbook checks for TGIF1 or TET3 would not supply the missing occupancy evidence. GTEx reports no significant single-tissue eQTLs (E07), and further QBiC or expression queries would not establish an element, target gene, or variant-mediated disease effect.).

### Round 1

- qbic_tf_detail({"tf": "CREB3L4"}) for H1.binding, ran as [E15](#e15). Expected: If the detail confirms that the ref-favoring prediction is not specifically supported by a CREB3L4 model, H1.binding remains weak and H1 gains no advantage over the alternatives; a direct CREB3L4-specific prediction would strengthen that link, though occupancy would still be unshown.
- chip_peaks({"tf": "CREB3L4", "biosample": "MCF-7"}) for H1.binding, ran as [E16](#e16). Expected: A peak overlapping the variant in MCF-7 would add occupancy support and strengthen H1.binding; no peak would leave the QBiC-SELEX result unsupported by occupancy and H1 weak.
- gene_disease({"gene": "PELI2"}) for H1.phenotype, ran as [E17](#e17). Expected: Breast-cancer association evidence for PELI2 could strengthen the proposed phenotype link, while no relevant association would leave it unsupported; either result would be gene-level evidence, not proof that this variant regulates PELI2.

- Result of qbic_tf_detail({"tf":"CREB3L4"}): E15 reports a CREB3L4 own-model QBiC-SELEX effect favoring ref C (effect -1.314), as well as a stronger ref-favoring prediction from a model mapped from CREB3L2. This modestly strengthens the CREB3L4 binding prediction, but does not establish occupancy. (as expected: yes)
- Result of chip_peaks({"tf":"CREB3L4","biosample":"MCF-7"}): E16 reports no CREB3L4 ChIP-seq peak containing the variant in MCF-7 and no peak within 100 bp that contains it; absence may also reflect lack of a CREB3L4 experiment in that biosample. (as expected: yes)
- Result of gene_disease({"gene":"PELI2"}): E17 reports an Open Targets overall score of 0.00 for PELI2 and breast cancer, with literature evidence score 0.01. (as expected: yes)

Chains after revision: null 0.94; CREB3L4 0.04; TGIF1 0.01; TET3 0.01. Link grades changed: H1.cell_type: supported → weak, H2.cell_type: supported → weak, H3.cell_type: supported → weak.

### Round 2

- literature_search({"query": "CREB3L4 breast cancer"}) for H1.phenotype, ran as [E18](#e18). Expected: If the abstracts report CREB3L4 perturbation affecting breast-cancer-relevant phenotypes, H1.phenotype gains support and H1 rises modestly; if not, it remains unsupported.
- literature_search({"query": "TGIF1 breast cancer"}) for H2.phenotype, ran as [E19](#e19). Expected: If the abstracts report TGIF1 perturbation affecting breast-cancer-relevant phenotypes, H2.phenotype gains support; otherwise H2 remains weak and unsupported at this link.
- literature_search({"query": "TET3 breast cancer"}) for H3.phenotype, ran as [E20](#e20). Expected: If the abstracts report TET3 perturbation affecting breast-cancer-relevant phenotypes, H3.phenotype gains support; otherwise H3 remains weak and unsupported at this link.

- Result of literature_search({"query":"CREB3L4 breast cancer"}) for H1.phenotype: The results describe CREB3L4 regulation of BAG3 and effects on autophagy and cisplatin resistance in gastric cancer cells, not a demonstrated breast-cancer effect. H1.phenotype remains unsupported for this variant. (as expected: yes)
- Result of literature_search({"query":"TGIF1 breast cancer"}) for H2.phenotype: The results include a breast-cancer-cell study reporting TGIF1 upregulation alongside MEIS inhibition and a computational MCF7 network result, but no direct TGIF1 perturbation establishing a breast-cancer phenotype through this variant. H2 remains weak at this link. (as expected: yes)
- Result of literature_search({"query":"TET3 breast cancer"}) for H3.phenotype: The results provide breast-cancer context for TET3, including reported TET3-related demethylation and TNBC progression, but do not connect this variant or its predicted binding change to the phenotype. This modestly supports biological plausibility, not the full chain. (as expected: yes)

Chains after revision: null 0.96; CREB3L4 0.03; TET3 0.01; TGIF1 0.01. Link grades changed: H2.phenotype: missing → weak, H3.phenotype: missing → weak.

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

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=CREB3L4%20breast%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:14:41+00:00)

> Europe PMC: 189 hits for 'CREB3L4 breast cancer'; top 8 with PMIDs:
> PMID 42098970 (2026): Knockdown of CREB3L4 Inhibits Autophagy and Reduces Cisplatin Resistance in Gastric Cancer Cells by Downregulating BAG3.
> PMID 41096831 (2025): Candidate Transcript Panel in Semen Extracellular Vesicles Can Improve Prediction of Aggressiveness of Prostate Cancer.
> PMID 41155247 (2025): &lt;i&gt;Jumping Translocation Breakpoint&lt;/i&gt; Expression in Midgestation Mouse Embryos.
> PMID 42794669 (2026): Special Issue "Molecular Biomarkers in Cancers: Advances and Challenges".
> PMID 41370125 (2025): Mutant GNAS drives a pyloric metaplasia with tumor suppressive glycans in intraductal papillary mucinous neoplasia.
> PMID 41301006 (2025): The Unfolded Protein Response-Novel Mechanisms, Challenges, and Key Considerations for Therapeutic Intervention.
> PMID 39254691 (2024): Identification of novel protein biomarkers and therapeutic targets for ankylosing spondylitis using human circulating plasma proteomics and genome analysis.
> PMID 38796598 (2024): Oncofetal SNRPE promotes HCC tumorigenesis by regulating the FGFR4 expression through alternative splicing.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 42098970 (https://europepmc.org/article/MED/42098970; retrieved 2026-10-26T22:14:41+00:00)

> CREB3L4 is an endoplasmic reticulum membrane-bound transcription factor that has been shown to regulate the expression of Bcl-2 associated athanogene 3 (BAG3), a co-chaperone protein involved in autophagy and survival signaling in various cancers.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 42098970 (https://europepmc.org/article/MED/42098970; retrieved 2026-10-26T22:14:41+00:00)

> Notably, knockdown of CREB3L4 inhibited autophagy and alleviated cisplatin resistance in gastric cancer cells by down-regulating BAG3.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TGIF1%20breast%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:14:46+00:00)

> Europe PMC: 394 hits for 'TGIF1 breast cancer'; top 8 with PMIDs:
> PMID 42178868 (2026): TG-interacting factor 1 mediates TNF-induced Ccl2 expression in adipocytes to promote prostate cancer progression.
> PMID 41696444 (2025): STC2 promotes anoikis resistance by modulating TGIF1 mRNA stability in colorectal cancer.
> PMID 42356499 (2026): Synthesis and Development of Novel Small-Molecule MEIS2 Inhibitors That Induce Cell Death in Breast Cancer Cells by Targeting the Homeobox Domain.
> PMID 42735560 (2026): 11-Oxo-mogroside V attenuates lung adenocarcinoma progression by disrupting metabolic homeostasis and suppressing TGFβ2/Myc-dependent oncogenic signaling.
> PMID 41832702 (2026): A Computational Strategy to Identify Hub Genes in Pathway Analysis of Gamma Tocotrienol-treated MCF-7 Cells and Molecular Docking Study Using Selected Phytochemicals as Therapeutic Agents.
> PMID 42382743 (2026): &lt;i&gt;HK2&lt;/i&gt; knockdown is associated with context-dependent inflammatory and angiogenesis-related transcriptional programmes in glioblastoma cells.
> PMID 42516037 (2026): Myeloid cell reprogramming combined with zoledronic acid effectively suppresses bone metastasis.
> PMID 41516419 (2026): Haplotype GWAS in Colorectal Cancer Patients with a Family History of Gastric or Prostate Cancer.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 42356499 (https://europepmc.org/article/MED/42356499; retrieved 2026-10-26T22:14:46+00:00)

> Our results demonstrate that MEISi-2E, MEISi-3, and MEISi-4 significantly suppress MEIS-driven luciferase activity and downregulate the expression of Meis1, Meis2, and downstream genes such as IL17RB, CDH1, EGR2, PAX6, and SERPINE1 while upregulating negative regulator TGIF1 and SOX3.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 41832702 (https://europepmc.org/article/MED/41832702; retrieved 2026-10-26T22:14:46+00:00)

> Protein- protein interaction (PPI) network analysis further revealed four key gene candidates: EGR1, JUN, SREBF1, and TGIF1.

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TET3%20breast%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:14:51+00:00)

> Europe PMC: 1542 hits for 'TET3 breast cancer'; top 7 with PMIDs:
> PMID 42316271 (2026): Changes in active DNA demethylation pathway components during neoadjuvant chemotherapy and their prognostic significance in breast cancer.
> PMID 42612286 (2026): Validating raloxifene-mediated restoration of DNMT-TET epigenetic balance in breast and lung cancer.
> PMID 42555815 (2026): Clinical Significance of SOX2 Promoter Methylation in Breast Cancer Prognosis.
> PMID 42212683 (2026): Oncogenic BRAF and KRAS Promote Global DNA Hypomethylation Through a Directed Pathway That Upregulates TET3.
> PMID 42173327 (2026): GALNT6 coordinates glycolysis and α-KG-dependent DNA methylation to promote TNBC progression.
> PMID 42725027 (2026): Chaperone-mediated autophagy as a regulator of hallmarks of cancer.
> PMID 42359646 (2026): Regulatory function of ten‑eleven translocation‑2 in transcriptional mechanisms of demethylated myeloma cells.

<a id="e20a"></a>**E20a** literature_search, Europe PMC abstract, PMID 42316271 (https://europepmc.org/article/MED/42316271; retrieved 2026-10-26T22:14:51+00:00)

> During chemotherapy, increases in the levels of 5-methyl-2'-deoxycytidine (5-mdC), 5-formyl-2'-deoxycytidine (5-fdC), and 5-carboxyl-2'-deoxycytidine (5-cadC) and decreases in the expression of genes encoding TET (ten-eleven translocation) proteins, TDG (thymine DNA glycosylase), and AID (activation-induced cytidine deaminase) were observed in peripheral blood leukocytes.

<a id="e20b"></a>**E20b** literature_search, Europe PMC abstract, PMID 42612286 (https://europepmc.org/article/MED/42612286; retrieved 2026-10-26T22:14:51+00:00)

> In both tumour types, DNMT1 was consistently over-expressed, while the TET family demethylases (TET1, TET2, TET3) were coordinately down-regulated, resulting in a striking increase in the DNMT/TET balance index and a transcriptional programme that is biased towards CpG hypermethylation.

<a id="e20c"></a>**E20c** literature_search, Europe PMC abstract, PMID 42555815 (https://europepmc.org/article/MED/42555815; retrieved 2026-10-26T22:14:51+00:00)

> Additionally, a positive association between deregulated TET3 and TGFβ1 highlights a positive feedback loop in the dynamic tumor microenvironment.

<a id="e20d"></a>**E20d** literature_search, Europe PMC abstract, PMID 42555815 (https://europepmc.org/article/MED/42555815; retrieved 2026-10-26T22:14:51+00:00)

> Reduced TET3 and miR200b expression correlated with poor outcomes, and their integration with SOX2 formed a tri-gene signature that enhanced patient stratification.

<a id="e20e"></a>**E20e** literature_search, Europe PMC abstract, PMID 42173327 (https://europepmc.org/article/MED/42173327; retrieved 2026-10-26T22:14:51+00:00)

> This depletion inhibits TET3-mediated DNA demethylation, thereby elevating 5mC levels, which in turn activates genes such as KIF14 to promote TNBC progression.

<a id="e20f"></a>**E20f** literature_search, Europe PMC abstract, PMID 42173327 (https://europepmc.org/article/MED/42173327; retrieved 2026-10-26T22:14:51+00:00)

> Our study uncovers GALNT6 as a key regulator of metabolic reprogramming (glycolysis/TCA cycle) and epigenetic remodeling (5mC/TET3) to accelerate TNBC progression, suggesting that targeting the GALNT6-mediated metabolic-epigenetic axis may provide a novel therapeutic strategy for TNBC.
