# rs11629191 and Breast cancer

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 196 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen

445 of 997 models pass the gate. Top groups: bZIP, 1 model (best XBP1, z -91.69); bZIP, 4 models (best CREB3, z -76.89); SAND, 2 models (best SP140L, z -57.31); bZIP, 3 models (best ATF2, z -49.19); CxxC, 2 models (best CXXC4, z -44.11).

## Ranked chains

### 1. null_no_TF_effect: No TF-mediated effect of rs11629191 in breast cancer (p = 0.64)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs11629191 is detectable in MCF7 chromatin.; No allelic difference is seen in reporter assays in MCF7.; No breast-tissue eQTL for PELI2 or ENSG00000259868 is attributable to this variant.; PELI2 perturbation has no breast-cancer-relevant growth phenotype, consistent with DepMap non-dependency.

Falsified if: Allele-specific TF binding at rs11629191 is demonstrated in MCF7 cells.; A reproducible allelic effect on a target gene or reporter is shown in a breast-cell context.; ChIP, CUT&RUN, or reporter assays contradict the no-effect prediction.

### 2. XBP1_ref_more_binds: XBP1 binds the ref C allele more strongly at a candidate non-cCRE motif (p = 0.16)

TF XBP1 (stated coverage own_model; registry own_model), ref allele binds more; element candidate_intronic_XBP1_motif_no_cCRE; gene PELI2; cell type MCF7_breast_cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | XBP1 is the strongest QBiC-SELEX group member: group G382 reports XBP1 own model with z=-91.69 and effect=-3.167, meaning the alt T allele binds less than ref C, and XBP1 is expressed at 636.57 TPM in the MCF7 context. E18 reports no ENCODE XBP1 ChIP-seq peak containing the variant in MCF7, but absence can also mean no XBP1 experiment in that biosample, so cellular occupancy is unproven. | weak | [E07](#e07), [E08](#e08), [E18](#e18) |
| element | The variant is an intronic/intergenic variant with no overlapping ENCODE cCRE; the nearest cCRE is 1,868 bp away. This is at most a candidate XBP1 motif outside a chromatin-defined regulatory element. | weak | [E01](#e01), [E03](#e03), [E08](#e08) |
| gene | PELI2 is the nearest protein-coding gene but lies 230.8 kb upstream, and no provided evidence directly links rs11629191 or XBP1 to PELI2. E19 reports no significant GTEx v8 breast eQTL for this variant, E05 contains only a PIP 0.03 brain-nucleus-accumbens eQTL for ENSG00000259868, and E20 shows PELI2 is not a common-essential gene in breast lines. | missing | [E02](#e02), [E05](#e05), [E19](#e19), [E20](#e20) |
| cell_type | XBP1 is expressed at 636.57 TPM in DepMap ACH-000019 (MCF7), so XBP1 is present at high levels in the relevant cell context. | supported | [E08](#e08) |
| phenotype | No provided evidence connects XBP1 at this locus to breast cancer: E04 shows zero GWAS Catalog associations for rs11629191, E06 is only a PELI2 keyword-hit list without a demonstrated XBP1-rs11629191-PELI2 axis, and E20 shows PELI2 non-dependency in breast lines. The phenotype link remains speculative. | missing | [E04](#e04), [E06](#e06), [E20](#e20) |

Predictions: XBP1 ChIP-qPCR or CUT&RUN in MCF7 shows occupancy at rs11629191.; The ref C allele has higher XBP1 occupancy than the alt T allele.; An allele-specific reporter in MCF7 shows higher activity from the C allele.; XBP1 perturbation changes PELI2 expression only if PELI2 is the long-range target.

Falsified if: XBP1 does not occupy the locus in MCF7 in a targeted ChIP-qPCR or CUT&RUN assay.; The T allele does not reduce XBP1 binding or reporter activity in MCF7.; No allele-specific effect is seen in an independent cellular assay.; XBP1 perturbation does not affect PELI2 expression if PELI2 is claimed as the target.

### 3. CREB3L4_ref_more_binds: CREB3L4 binds the ref C allele more strongly at a candidate bZIP motif (p = 0.12)

TF CREB3L4 (stated coverage own_model; registry own_model), ref allele binds more; element candidate_intronic_CREB3_family_motif_no_cCRE; gene ENSG00000259868; cell type MCF7_breast_cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The G017 CREB3-family bZIP group binds the ref C allele more strongly than the alt T allele: best model CREB3 has z=-76.89 and effect=-1.64 (alt binds less), and CREB3L4 is an own-model member with the same direction (z=-37.55). CREB3L4 is chosen because it is the highest-expressed member in MCF7 at 48.8 TPM, but this remains in vitro SELEX without cellular occupancy data. | weak | [E07](#e07), [E09](#e09) |
| element | The variant is intronic/intergenic and does not overlap an ENCODE cCRE; the nearest cCRE is 1,868 bp away. The element claim is therefore a candidate CREB3-family motif, not a validated regulatory element. | weak | [E01](#e01), [E03](#e03), [E09](#e09) |
| gene | The only molecular QTL in the credible set is a PIP 0.03 eQTL for ENSG00000259868 in brain nucleus accumbens, which is very weak and in a non-breast tissue. E19 reports no significant breast GTEx eQTL for this variant, so no breast variant-to-gene link is established. | weak | [E05](#e05), [E19](#e19) |
| cell_type | CREB3L4 is expressed at 48.8 TPM in DepMap ACH-000019 (MCF7), making it a plausibly expressed member of the G017 group in this cell context. | supported | [E09](#e09) |
| phenotype | No provided evidence directly connects CREB3L4 at rs11629191 to breast cancer; E04 shows zero GWAS Catalog associations for the variant. Breast cancer relevance is inferred only from the case context. | missing | [E04](#e04) |

Predictions: CREB3L4 ChIP or reporter assays show allele-specific CREB3L4 binding at rs11629191.; The ref C allele has higher CREB3-family binding than the alt T allele.; The ENSG00000259868 eQTL replicates in breast tissue or MCF7.; CREB3L4 perturbation changes ENSG00000259868 expression.

Falsified if: CREB3L4 does not bind the locus in MCF7.; CREB3L4-specific assays do not show allele-specific binding.; The ENSG00000259868 eQTL does not replicate in breast tissue or MCF7.; CREB3L4 perturbation does not affect ENSG00000259868.

### 4. ATF2_ref_more_binds: ATF2 binds the ref C allele more strongly at a candidate AP-1/bZIP motif (p = 0.08)

TF ATF2 (stated coverage own_model; registry own_model), ref allele binds more; element candidate_intronic_ATF2_AP1_motif_no_cCRE; gene PELI2; cell type MCF7_breast_cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | G033 reports ATF2 own model with z=-49.19 and effect=-1.348, meaning the alt T allele binds less than ref C, and ATF2 is expressed at 16.22 TPM in MCF7. ATF2 is the best model in the group, but ATF7 is also an own-model member and is slightly more highly expressed (20.81 TPM), so the ATF2 choice is not strongly distinguished by expression. | weak | [E07](#e07), [E11](#e11) |
| element | The variant is intronic/intergenic without an overlapping cCRE; the element evidence is only an in vitro ATF2/AP-1 motif disruption, not a chromatin-defined regulatory element. | weak | [E01](#e01), [E03](#e03), [E11](#e11) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb upstream, but no ATF2-PELI2 or variant-PELI2 QTL or perturbation evidence is provided. E19 reports no significant breast GTEx eQTL for this variant, and E20 shows PELI2 is not a common-essential gene in breast lines. | missing | [E02](#e02), [E19](#e19), [E20](#e20) |
| cell_type | ATF2 is expressed at 16.22 TPM in DepMap ACH-000019 (MCF7), supporting ATF2 as an expressed group member in this cell context. | supported | [E11](#e11) |
| phenotype | No provided evidence connects ATF2 at rs11629191 to breast cancer: E04 shows zero GWAS Catalog associations, E06 is only a PELI2 keyword list, and E20 shows PELI2 non-dependency in breast lines. The phenotype link is speculative. | missing | [E04](#e04), [E06](#e06), [E20](#e20) |

Predictions: ATF2 ChIP-seq or CUT&RUN in MCF7 shows allele-specific occupancy at rs11629191.; The ref C allele has higher ATF2 binding than the alt T allele.; An allele-specific reporter in MCF7 shows higher activity from the C allele.; ATF2 perturbation changes PELI2 expression only if PELI2 is the long-range target.

Falsified if: ATF2 does not bind the locus in MCF7.; The T allele does not reduce ATF2 binding or reporter activity.; ATF2 perturbation does not affect PELI2 if PELI2 is claimed as the target.; The PELI2 link is not reproducible.

## Prediction matrix

| Test | Cost | Separates top two | null_no_TF_effect | XBP1_ref_more_binds | CREB3L4_ref_more_binds | ATF2_ref_more_binds |
| --- | --- | --- | --- | --- | --- | --- |
| XBP1 ChIP-qPCR or CUT&RUN in MCF7 at rs11629191 with allele-specific readout | medium | yes | No XBP1 occupancy or no allelic bias is detected at the locus in MCF7. | XBP1 occupancy is detected and is higher on the ref C allele than the alt T allele. |  |  |
| Allele-specific reporter or MPRA with rs11629191 C vs T in MCF7 | medium | yes | No allelic difference in reporter activity is detected. | The ref C allele drives higher reporter activity than the alt T allele. |  |  |
| Breast-tissue eQTL lookup for PELI2 and ENSG00000259868 | low | no | No significant breast eQTL is detected for PELI2 or ENSG00000259868. | No significant breast eQTL is detected for PELI2; the only QTL remains the weak brain ENSG00000259868 eQTL (PIP 0.03). |  |  |
| PELI2 CRISPR knockout growth assay in MCF7 or breast-lineage lines | low | no | PELI2 knockout has no measurable growth effect, consistent with DepMap non-dependency. | PELI2 knockout has no measurable growth effect, weakening the PELI2 phenotype link but not the binding claim. |  |  |

## Next experiment

skip

## Investigate calls

- chip_peaks({"tf": "XBP1", "biosample": "MCF7"})
- eqtl_lookup({"tissue": "breast"})
- gene_dependency({"gene": "PELI2"})

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs11629191&size=100; retrieved 2026-10-25T17:32:50+00:00)

> 0 GWAS Catalog associations for rs11629191, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:49+00:00)

> 1 credible sets contain 14_55887040_C_T: 0 GWAS, 1 molecular QTL.
> eqtl for ENSG00000259868 (gtex-v10_ge_brain_nucleus_accumbens_ensg0000025986): PIP 0.03

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PELI2%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:50+00:00)

> Europe PMC: 178 hits for 'PELI2 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41023515 (2025): Pellino ubiquitin ligases: double-edged swords in hematologic malignancies-from oncogenic stabilizers to therapeutic vulnerabilities.
> PMID 41331176 (2025): Construction and validation of risk models of prognostic genes associated with parthanatos in papillary thyroid carcinoma based on bioinformatics.
> PMID 40362379 (2025): &lt;i&gt;O&lt;/i&gt;-Desmethyltramadol Enhanced Anti-Cancer Efficacy over Tramadol Through Non-μ-Opioid Receptor and Differential Cellular Contexts of Human Breast Cancer Cells.
> PMID 42757486 (2026): Pemetrexed increases BRCA1 protein stability and sensitizes TNBC cells to radiotherapy.
> PMID 42734444 (2027): Anesthesia inhalation agent sevoflurane induces perioperative cognitive impairment: Apelin/early growth response 1 axis induces ferritinophagy and exacerbates ferroptosis.
> PMID 41079921 (2025): PRMT1/PRMT5-Mediated Differential Arginine Methylation of CRIP1 Promotes the Recurrence of Small Cell Lung Cancer after Chemotherapy.
> PMID 42380137 (2026): HOXC9 accelerates esophageal squamous cell carcinoma progression via OTUD1-FABP5-mediated lipid metabolic reprogramming.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr14:55887040:C>T: 997 models scored, 445 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 324 CIS-BP groups. Expression context: DepMap line ACH-000019. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 95 (GCM, 2 models z 44.55, C2H2 ZF, 1 model z 33.3, bZIP, 1 model z -32.97, bZIP, 1 model z -29.97, bHLH, 1 model z -16.81). Passing groups ranked below the ones shown: 219. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G382 (bZIP, 1 model): best model XBP1_eDBD_TCCTTG40NGGT_KAN_yin2017_0_4_7mer (own model of XBP1), z -91.69, effect -3.167 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: XBP1 z -91.69. TFs this group covers: XBP1 (own model) 636.57 TPM; best model's site strength: ref 100.0th, alt 98.7th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G017 (bZIP, 4 models): best model CREB3_NA_TAGAAC20NCG_ESAD_yang2017_0_3_7mer (own model of CREB3), z -76.89, effect -1.64 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: CREB3 z -76.89, CREB3L1 z -60.99, CREB3L2 z -49.16, CREB3L4 z -37.55. TFs this group covers: CREB3L4 (own model) 48.8 TPM, CREB3 (own model) 45.81 TPM, CREB3L2 (own model) 7.06 TPM, CREB3L1 (own model) 0.09 TPM; best model's site strength: ref 99.9th, alt 98.2th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G099 (SAND, 2 models): best model SP140L_FL_TG40NGACCTT_YWPA_jolma2025_0_2_7mer (own model of SP140L), z -57.31, effect -1.491 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: SP140L z -57.31, SP140 z -16.92. TFs this group covers: SP140L (own model) 7.63 TPM, SP140 (own model) 0.86 TPM; best model's site strength: ref 99.9th, alt 72.0th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G033 (bZIP, 3 models): best model ATF2_eDBD_TGAACC40NCCA_KP_yin2017_0_3_7mer (own model of ATF2), z -49.19, effect -1.348 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: ATF2 z -49.19, CREB5 z -6.61. TFs this group covers: ATF7 (own model) 20.81 TPM, ATF2 (own model) 16.22 TPM, CREB5 (own model) 0.02 TPM, ATF7-NPFF (mapped); best model's site strength: ref 99.7th, alt 95.7th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G064 (CxxC, 2 models): best model CXXC4_FL_GG40NTAGTTT_YWKC_jolma2025_0_4_7mer (own model of CXXC4), z -44.11, effect -2.102 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: CXXC4 z -44.11, TET3 z -20.67. TFs this group covers: CXXC5 (mapped) 77.02 TPM, TET3 (own model) 9.96 TPM, CXXC4 (own model) 0.33 TPM; best model's site strength: ref 98.8th, alt 70.2th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G008 (Homeodomain, 9 models): best model TGIF2_eDBD_TTGCAA40NGTG_KO_yin2017_0_4_7mer (own model of TGIF2), z -38.69, effect -2.43 (alt binds less); 7 passing models (7 with the best model's sign). Passing members: TGIF2 z -38.69, MEIS3 z -23.79, PKNOX2 z -19.46, TGIF2LY z -17.27, TGIF2LX z -15.65 (+2 more). TFs this group covers: TGIF1 (own model) 39.86 TPM, TGIF2 (own model) 20.51 TPM, MEIS3 (own model) 15.61 TPM, PKNOX1 (own model) 7.53 TPM, MEIS2 (own model) 6.32 TPM, MEIS1 (own model) 1.52 TPM, PKNOX2 (own model) 0.05 TPM, TGIF2LX (own model) 0.0 TPM, TGIF2LY (own model) 0.0 TPM; best model's site strength: ref 99.8th, alt 94.1th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G012 (bZIP, 6 models): best model NRL_eDBD_TGGAGA40NCCA_KR_yin2017_0_4_7mer (own model of NRL), z -38.05, effect -1.53 (alt binds less); 6 passing models (6 with the best model's sign). Passing members: NRL z -38.05, MAF z -34.57, MAFG z -27.77, MAFB z -27.66, MAFK z -24.11 (+1 more). TFs this group covers: MAFK (own model) 16.96 TPM, MAFG (own model) 8.48 TPM, MAFB (own model) 3.09 TPM, MAFA (own model) 1.07 TPM, NRL (own model) 0.98 TPM, MAF (own model) 0.23 TPM; best model's site strength: ref 100.0th, alt 99.5th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G381 (bHLH, 1 model): best model USF3_DBD_CG40NACGGTT_YWCB_jolma2025_0_1_7mer (own model of USF3), z -37.78, effect -0.258 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: USF3 z -37.78. TFs this group covers: USF3 (own model) 3.82 TPM; best model's site strength: ref 100.0th, alt 59.5th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G062 (bZIP, 2 models): best model CREB1_eDBD_TTTGAC40NGGT_KR_yin2017_0_3_7mer (own model of CREB1), z -37.47, effect -2.019 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: CREB1 z -37.47, CREM z -29.21. TFs this group covers: CREB1 (own model) 30.28 TPM, ATF1 (mapped) 25.91 TPM, CREM (own model) 24.59 TPM; best model's site strength: ref 99.2th, alt 91.5th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G019 (C2H2 ZF, 4 models): best model EGR2_NA_TCGGCC20NGA_ESW_yang2017_0_3_7mer (own model of EGR2), z -30.48, effect -1.1 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: EGR2 z -30.48, EGR3 z -23.43, EGR1 z -6.33. TFs this group covers: EGR3 (own model) 12.82 TPM, EGR1 (own model) 10.78 TPM, EGR2 (own model) 0.23 TPM, EGR4 (own model) 0.0 TPM; best model's site strength: ref 100.0th, alt 76.4th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:34:02+00:00)

> No ENCODE XBP1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF7'. Absence can also mean no XBP1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38 in tissues matching 'breast'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e20"></a>**E20** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for PELI2 (0 = no effect, -1 = median common-essential; < -0.5 called dependent). MCF7 (ACH-000019): 0.01. Breast lineage, 53 lines: median -0.02, 0% dependent. All 1183 lines: median -0.03, 0% dependent.
