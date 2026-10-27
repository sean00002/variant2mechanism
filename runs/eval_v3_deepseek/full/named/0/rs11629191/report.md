# rs11629191 and Breast cancer

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 10 model calls; 411 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: CREB3L2 (z -60.99); CREB3L4 (z -49.16); TET3 (z -44.11); MEIS3 (z -38.69); TGIF1 (z -38.69). Diagnostic, not shown to the model: 445 of 997 models pass Bonferroni.

## Ranked chains

### 1. NULL: Null: no TF-mediated effect of rs11629191 (p = 0.60)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF occupancy at chr14:55887040 in MCF-7 or other breast models.; No allele-dependent reporter activity for the C vs T allele in MCF-7.; No significant eQTL for this variant in breast tissue or MCF-7.

Falsified if: A reproducible allele-specific ChIP/CUT&RUN or reporter assay in MCF-7 shows TF occupancy at this base with a clear C vs T difference.

### 2. CREB3L2: CREB3L2 binds the C allele at an unannotated intronic site; target and phenotype unproven (p = 0.24)

TF CREB3L2 (QBiC-SELEX coverage own_model), ref allele binds more; element Unannotated intronic sequence with no cCRE overlap.; gene PELI2 (nearest protein-coding gene; unproven); cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB3L2 binds the ref C allele more strongly: its own QBiC-SELEX model gives z -49.16 and effect -2.335 (ref site 100th vs alt 91.6th percentile), while a CREB3L1-mapped model gives a larger z -60.99 and effect -2.258. I chose CREB3L2 because it has an own model and a strong ref-preferring effect, but ENCODE has no ChIP-seq peak at this base in any biosample, so occupancy is unknown and this is only a binding prediction. | weak | [E16](#e16), [E04](#e04) |
| element | The variant is intronic and no cCRE overlaps it; the nearest dELS is 1,868 bp away and GERP is -3.12, so there is no epigenomic support for an active regulatory element at this base. | supported | [E01](#e01), [E03](#e03) |
| gene | PELI2 is only the nearest protein-coding gene at 230.8 kb; GTEx v8 shows no significant eQTL, and the only molecular QTL is weak for ENSG00000259868 in brain (PIP 0.03), so the target gene is unproven. | supported | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | CREB3L2 is expressed in MCF-7 (7.06 TPM; rank 534 of 1,626 TFs), so the cell context is permissive, though expression is modest. | supported | [E10](#e10) |
| phenotype | There is no GWAS association for rs11629191, and the PELI2 breast-cancer literature is not variant-specific, so any breast-cancer link remains unproven. | supported | [E05](#e05), [E08](#e08) |

Predictions: CREB3L2 ChIP-qPCR/CUT&RUN shows enrichment at chr14:55887040 in MCF-7.; Allele-specific EMSA shows stronger binding of CREB3L2 to the C allele than the T allele.; Allele-dependent reporter activity in MCF-7 is reduced by CREB3L2 knockdown/knockout; the direction of activity is not asserted.

Falsified if: CREB3L2 does not occupy this locus in MCF-7, or an allele-specific assay shows no C-vs-T binding difference.

### 3. CREB3L4: CREB3L4 binds the C allele at an unannotated intronic site; target and phenotype unproven (p = 0.16)

TF CREB3L4 (QBiC-SELEX coverage own_model), ref allele binds more; element Unannotated intronic sequence with no cCRE overlap.; gene PELI2 (nearest protein-coding gene; unproven); cell type MCF-7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB3L4 binds the ref C allele more strongly: its own QBiC-SELEX model gives z -37.55 and effect -1.314, while its top mapped model is CREB3L2-derived and gives effect -2.335. I chose CREB3L4 because it has an own model and high MCF-7 expression, but ENCODE has no ChIP-seq peak at this base in any biosample, so occupancy is unknown and this is only a binding prediction. | weak | [E15](#e15), [E04](#e04) |
| element | The variant is intronic and no cCRE overlaps it; the nearest dELS is 1,868 bp away and GERP is -3.12, so there is no epigenomic support for an active regulatory element at this base. | supported | [E01](#e01), [E03](#e03) |
| gene | PELI2 is only the nearest protein-coding gene at 230.8 kb; GTEx v8 shows no significant eQTL, and the only molecular QTL is weak for ENSG00000259868 in brain (PIP 0.03), so the target gene is unproven. | supported | [E02](#e02), [E06](#e06), [E07](#e07) |
| cell_type | CREB3L4 is expressed in MCF-7 (48.8 TPM; rank 68 of 1,626 TFs), so the cell context is permissive. | supported | [E11](#e11) |
| phenotype | There is no GWAS association for rs11629191, and the PELI2 breast-cancer literature is not variant-specific, so any breast-cancer link remains unproven. | supported | [E05](#e05), [E08](#e08) |

Predictions: CREB3L4 ChIP-qPCR/CUT&RUN shows enrichment at chr14:55887040 in MCF-7.; Allele-specific EMSA shows stronger binding of CREB3L4 to the C allele than the T allele.; Allele-dependent reporter activity in MCF-7 is reduced by CREB3L4 knockdown/knockout; the direction of activity is not asserted.

Falsified if: CREB3L4 does not occupy this locus in MCF-7, or an allele-specific assay shows no C-vs-T binding difference.

## Prediction matrix

| Test | Cost | Separates top two | NULL | CREB3L2 | CREB3L4 |
| --- | --- | --- | --- | --- | --- |
| CREB3L2 ChIP-qPCR at chr14:55887040 in MCF-7 with IgG/input controls | low | yes | No enrichment over input and no allele-specific signal at the variant. | Enrichment over input at the variant; allele-specific ChIP shows stronger signal on the C allele than the T allele. | No CREB3L2 enrichment at the variant. |
| Allele-specific EMSA with CREB3L2 protein and C vs T probes | low | yes | No reproducible C-vs-T difference in CREB3L2 binding. | CREB3L2 binds the C allele more strongly than the T allele. | No CREB3L2-specific C-vs-T binding difference. |
| CREB3L4 ChIP-qPCR at chr14:55887040 in MCF-7 with IgG/input controls | low | no | No enrichment over input at the variant. | No CREB3L4 enrichment at the variant. | Enrichment over input at the variant; allele-specific ChIP shows stronger signal on the C allele than the T allele. |
| Allele-specific reporter assay in MCF-7 with CREB3L2 knockdown or knockout | medium | yes | No allele-dependent reporter activity difference between C and T. | Allele-dependent reporter activity is present and is reduced or abolished by CREB3L2 knockdown/knockout; direction of activity is not asserted. | Allele-dependent reporter activity, if any, is not dependent on CREB3L2. |

## Next experiment

CREB3L2 ChIP-qPCR at chr14:55887040 in MCF-7 with IgG and input controls

## Investigate calls

- qbic_tf_detail({"tf": "CREB3L4"})
- qbic_tf_detail({"tf": "CREB3L2"})
- qbic_tf_detail({"tf": "TGIF1"})

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

<a id="e08a"></a>**E08a** literature_search, Europe PMC abstract, PMID 41023515 (https://europepmc.org/article/MED/41023515; retrieved 2026-10-25T17:32:50+00:00)

> The Pellino protein family is an evolutionarily conserved group of E3 ubiquitin ligases comprising Pellino1, Pellino2, and Pellino3.

<a id="e08b"></a>**E08b** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-25T17:32:50+00:00)

> Seven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.

<a id="e08c"></a>**E08c** literature_search, Europe PMC abstract, PMID 40362379 (https://europepmc.org/article/MED/40362379; retrieved 2026-10-25T17:32:50+00:00)

> Hence, we sought to examine whether the cytotoxic effect of O-desmethyltramadol was better than tramadol on breast cancer cells.

<a id="e08d"></a>**E08d** literature_search, Europe PMC abstract, PMID 42757486 (https://europepmc.org/article/MED/42757486; retrieved 2026-10-25T17:32:50+00:00)

> Although pathogenic BRCA1 mutations are relatively uncommon, decreased BRCA1 protein expression, which is typically driven by accelerated proteasomal degradation, is implicated in aggressive breast cancer (BC), particularly triple‑negative (TN)BC.

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

<a id="e16"></a>**E16** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"CREB3L2","symbol":"CREB3L2","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr14:55887040:C>T","gate_p":5.02e-05,"models":[{"model":"CREB3L2_NA_TAACGG20NGCA_ESZ_yang2017_0_4_7mer","mapping":"own","group":"G017 bZIP, 4 models","quality":0.796,"effect":-2.335,"z":-49.16,"p":0.0,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":91.6,"k":7}},{"model":"CREB3L1_NA_TAAACA20NCAA_ESY_yang2017_0_3_7mer","mapping":"CIS-BP (CREB3L1)","group":"G017 bZIP, 4 models","quality":0.893,"effect":-2.258,"z":-60.99,"p":0.0,"rank_abs_z":"3/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":99.6,"k":7}},{"model":"CREB3L4_eDBD_TAGGCT40NACC_KO_yin2017_0_3_7mer","mapping":"CIS-BP (CREB3L4)","group":"G017 bZIP, 4 models","quality":0.941,"effect":-1.314,"z":-37.55,"p":1.4e-308,"rank_abs_z":"12/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":100.0,"k":7}}]}

<a id="e17"></a>**E17** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TGIF1","symbol":"TGIF1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr14:55887040:C>T","gate_p":5.02e-05,"models":[{"model":"TGIF1_NA_TATGGG20NGGG_ESY_yang2017_0_4_7mer","mapping":"own","group":"G008 Homeodomain, 9 models","quality":0.695,"effect":0.176,"z":3.51,"p":0.00045,"rank_abs_z":"501/997","passed_gate":false,"site_strength":{"ref_percentile":88.5,"alt_percentile":76.2,"k":7}},{"model":"MEIS1_NA_TGACCT20NGA_O_jolma2013_0_4_7mer","mapping":"CIS-BP (MEIS1)","group":"G008 Homeodomain, 9 models","quality":0.864,"effect":-1.129,"z":-10.67,"p":1.4e-26,"rank_abs_z":"91/997","passed_gate":true,"site_strength":{"ref_percentile":99.4,"alt_percentile":84.0,"k":7}},{"model":"MEIS2_FL_TTGTCG40NACC_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (MEIS2)","group":"G008 Homeodomain, 9 models","quality":0.833,"effect":-0.325,"z":-10.67,"p":1.4e-26,"rank_abs_z":"92/997","passed_gate":true,"site_strength":{"ref_percentile":96.6,"alt_percentile":83.1,"k":7}},{"model":"MEIS3_NA_TGGGTA20NGA_ESY_yang2017_0_2_7mer","mapping":"CIS-BP (MEIS3)","group":"G008 Homeodomain, 9 models","quality":0.858,"effect":-0.968,"z":-23.79,"p":4.6e-125,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":98.3,"alt_percentile":88.8,"k":7}},{"model":"PKNOX1_FL_TCGTCC40NGCC_KW_yin2017_0_4_7mer","mapping":"CIS-BP (PKNOX1)","group":"G008 Homeodomain, 9 models","quality":0.824,"effect":0.133,"z":3.99,"p":6.5e-05,"rank_abs_z":"449/997","passed_gate":false,"site_strength":{"ref_percentile":98.0,"alt_percentile":97.6,"k":7}},{"model":"PKNOX2_eDBD_TAACGT40NGAT_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (PKNOX2)","group":"G008 Homeodomain, 9 models","quality":0.673,"effect":-1.29,"z":-19.46,"p":2.5e-84,"rank_abs_z":"31/997","passed_gate":true,"site_strength":{"ref_percentile":98.6,"alt_percentile":80.8,"k":7}},{"model":"TGIF2_eDBD_TTGCAA40NGTG_KO_yin2017_0_4_7mer","mapping":"CIS-BP (TGIF2)","group":"G008 Homeodomain, 9 models","quality":0.877,"effect":-2.43,"z":-38.69,"p":0.0,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":99.8,"alt_percentile":94.1,"k":7}},{"model":"TGIF2LX_eDBD_TGAGAA40NGCG_KO_yin2017_0_4_7mer","mapping":"CIS-BP (TGIF2LX)","group":"G008 Homeodomain, 9 models","quality":0.762,"effect":-0.655,"z":-15.65,"p":3.4e-55,"rank_abs_z":"38/997","passed_gate":true,"site_strength":{"ref_percentile":98.3,"alt_percentile":83.0,"k":7}},{"model":"TGIF2LY_eDBD_TTGGCA40NTCG_KT_yin2017_0_4_7mer","mapping":"CIS-BP (TGIF2LY)","group":"G008 Homeodomain, 9 models","quality":0.957,"effect":-1.304,"z":-17.27,"p":8.5e-67,"rank_abs_z":"32/997","passed_gate":true,"site_strength":{"ref_percentile":97.8,"alt_percentile":90.9,"k":7}}]}
