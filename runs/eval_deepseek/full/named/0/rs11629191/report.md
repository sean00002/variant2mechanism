# rs11629191 and Breast cancer

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 222 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen

445 of 997 models pass the gate. Top groups: bZIP, 1 model (best XBP1, z -91.69); bZIP, 4 models (best CREB3, z -76.89); SAND, 2 models (best SP140L, z -57.31); bZIP, 3 models (best ATF2, z -49.19); CxxC, 2 models (best CXXC4, z -44.11).

## Ranked chains

### 1. H0_null: Null: no TF-mediated effect of rs11629191 on breast cancer (p = 0.75)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at chr14:55887040 that matters in breast cancer cells.; No reproducible cCRE or chromatin-state change attributable to this variant.; No credible PELI2 or nearby eQTL driven by this variant in relevant tissues.

Falsified if: Strong allele-specific TF binding and a reproducible target-gene eQTL are demonstrated in breast cancer cells.; A validated regulatory element overlapping the variant shows allele-dependent activity.

### 2. H1_XBP1_PELI2: XBP1 loss-of-binding at an unannotated element perturbs PELI2 in MCF7 (p = 0.12)

TF XBP1 (stated coverage own_model; registry own_model), ref allele binds more; element Unannotated regulatory element; gene PELI2; cell type MCF7 breast cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G382 is an XBP1 own-model bZIP model with z -91.69 and effect -3.167, so alt T binds XBP1 less strongly than ref C. XBP1 is the own-model TF named in this group. Cellular occupancy is not supported by the available ENCODE XBP1 ChIP-seq data in MCF7: no peak contains the variant, though absence may also reflect no XBP1 experiment in that biosample. | weak | [E07](#e07), [E08](#e08), [E18](#e18) |
| element | The variant is an intron_variant with no annotated regulatory feature, no overlapping cCRE, and the nearest dELS is 1868 bp away. This chain therefore requires an unannotated or cryptic XBP1-responsive element; the current epigenomic evidence is negative for a canonical element. | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb, but there is no breast mammary tissue eQTL for this variant and the only Open Targets molecular QTL is a weak brain eQTL for ENSG00000259868 with PIP 0.03, not PELI2. The variant-to-PELI2 link is therefore speculative and long-range. | missing | [E02](#e02), [E05](#e05), [E20](#e20) |
| cell_type | XBP1 is expressed at 636.57 TPM in the MCF7/ACH-000019 expression context, so an allele-specific XBP1 effect is cell-type plausible in principle. However, no ENCODE XBP1 ChIP-seq peak containing this variant is reported in MCF7, so cellular occupancy at this site remains untested or unsupported. | weak | [E07](#e07), [E08](#e08), [E18](#e18) |
| phenotype | PELI2 is a Pellino-family E3 ubiquitin ligase and has appeared among prognostic genes in a cancer bioinformatics model, but the supplied literature does not connect rs11629191 or PELI2 to breast cancer. The phenotype link is indirect. | weak | [E06](#e06), [E06a](#e06a), [E06b](#e06b) |

Predictions: Ref C binds XBP1 more strongly than alt T at the variant.; If the variant is in a functional XBP1 element, XBP1 perturbation in MCF7 should change PELI2 or nearby-locus expression.; The variant should sit in an accessible regulatory element in MCF7 despite current negative cCRE annotation.

Falsified if: XBP1 does not bind the ref allele more strongly than alt T at this sequence in vitro or in cells.; XBP1 perturbation in MCF7 does not alter PELI2 or nearby-locus expression.; The variant lies in closed chromatin with no regulatory activity in breast cancer cells.

### 3. H2_CREB3L4_PELI2: CREB3L4 loss-of-binding at the variant affects a nearby breast-cancer locus (p = 0.08)

TF CREB3L4 (stated coverage own_model; registry own_model), ref allele binds more; element Unannotated regulatory element; gene PELI2; cell type MCF7 breast cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G017 contains CREB3, CREB3L1, CREB3L2 and CREB3L4 own models; the best model is CREB3 with effect -1.64, and CREB3L4 is a passing own-model member with z -37.55, consistent with alt T binding less than ref C. The CREB3L4-specific effect is not directly shown. No ENCODE CREB3L4 ChIP-seq peak contains the variant in MCF7, although absence may reflect no experiment. | weak | [E07](#e07), [E09](#e09), [E19](#e19) |
| element | No cCRE overlaps the variant, no SCREEN cCRE lies within 500 bp, and the nearest dELS is 1868 bp away. This chain posits a non-canonical CREB3L4-responsive element rather than a validated ENCODE cCRE; the current epigenomic evidence is negative. | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is only the nearest protein-coding gene at 230.8 kb. There is no significant breast mammary tissue eQTL at this variant, and the only Open Targets molecular QTL is a weak brain eQTL for ENSG00000259868 with PIP 0.03, not PELI2. The gene assignment is weak. | missing | [E02](#e02), [E05](#e05), [E20](#e20) |
| cell_type | CREB3L4 is expressed at 48.8 TPM in the MCF7/ACH-000019 expression context, supporting potential activity in this cell line. However, no ENCODE CREB3L4 ChIP-seq peak containing the variant is reported in MCF7, so cellular occupancy is not established. | weak | [E07](#e07), [E09](#e09), [E19](#e19) |
| phenotype | A CREB3L4-dependent change in PELI2 could plausibly touch cancer biology through Pellino-family signaling, but the supplied breast-cancer evidence is indirect and does not link this variant, CREB3L4, or PELI2 to breast cancer. | weak | [E06](#e06), [E06a](#e06a), [E06b](#e06b) |

Predictions: Ref C binds CREB3L4 more strongly than alt T at the variant, if CREB3L4 itself is the relevant group member.; CREB3L4 perturbation in MCF7 should change PELI2 or nearby-locus expression.; The variant should act through an unannotated CREB3L4-responsive element in MCF7.

Falsified if: CREB3L4 does not bind the ref allele more strongly than alt T in vitro or in cells.; CREB3L4 perturbation in MCF7 has no effect on PELI2 or nearby gene expression.; The variant is not in an accessible regulatory element in MCF7.

### 4. H3_CREB1_PELI2: CREB1 loss-of-binding at a weak distal element alters a nearby locus (p = 0.05)

TF CREB1 (stated coverage own_model; registry own_model), ref allele binds more; element Unannotated regulatory element; gene PELI2; cell type MCF7 breast cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G062 is a bZIP group with CREB1 and CREM own models; CREB1 is the best model with z -37.47 and effect -2.019, so alt T binds less than ref C. CREB1 is chosen over CREM because it has the stronger passing model and higher MCF7 expression. | weak | [E07](#e07), [E16](#e16) |
| element | The variant has no annotated regulatory feature and no overlapping cCRE, and the nearest dELS is 1868 bp away. A functional CREB1 element would have to be unannotated or poorly captured; the current epigenomic evidence is negative. | missing | [E01](#e01), [E03](#e03) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb, but no breast mammary tissue eQTL links this variant to PELI2, and the only Open Targets molecular QTL is a weak brain eQTL for ENSG00000259868 with PIP 0.03. The target-gene link is speculative. | missing | [E02](#e02), [E05](#e05), [E20](#e20) |
| cell_type | CREB1 is expressed at 30.28 TPM in the MCF7/ACH-000019 expression context, so an allele-specific CREB1 effect is cell-type plausible. | weak | [E07](#e07), [E16](#e16) |
| phenotype | This chain would require CREB1-dependent regulation of a Pellino-family gene to influence breast cancer. The supplied literature establishes the Pellino-family context but does not connect CREB1 to PELI2 or to rs11629191 in breast cancer. | missing | [E06](#e06), [E06a](#e06a) |

Predictions: Ref C binds CREB1 more strongly than alt T at the variant.; CREB1 perturbation in MCF7 should change PELI2 or nearby-locus expression if this chain is correct.; The variant should have allele-dependent regulatory activity in breast cancer cells despite negative cCRE annotation.

Falsified if: CREB1 binding is not allele-specific at the variant.; CREB1 perturbation does not affect PELI2 or nearby expression in MCF7.; The variant has no regulatory activity in breast cancer cells.

## Prediction matrix

| Test | Cost | Separates top two | H0_null | H1_XBP1_PELI2 | H2_CREB3L4_PELI2 | H3_CREB1_PELI2 |
| --- | --- | --- | --- | --- | --- | --- |
| Multiplexed allele-specific ChIP-qPCR/EMSA for XBP1 and CREB3L4 at chr14:55887040 in MCF7 | low | yes | Neither XBP1 nor CREB3L4 shows allele-specific binding | Ref C shows stronger XBP1 binding than alt T; CREB3L4 shows no allele-specific binding | Ref C shows stronger CREB3L4 binding than alt T; XBP1 shows no allele-specific binding | Neither XBP1 nor CREB3L4 shows strong allele-specific binding |
| Breast mammary tissue eQTL for PELI2 or nearby genes | medium | yes | No reproducible breast eQTL at this variant | A reproducible cis-eQTL exists for PELI2 or a nearby locus; direction must be determined | A reproducible cis-eQTL exists for PELI2 or a nearby locus; direction must be determined | A reproducible cis-eQTL exists for PELI2 or a nearby locus; direction must be determined |
| Chromatin accessibility and cCRE activity at the variant in MCF7 | medium | yes | Closed or inert chromatin at the variant in MCF7 | Accessible regulatory element in MCF7; supports a non-canonical element | Accessible regulatory element in MCF7; supports a non-canonical element | Accessible regulatory element in MCF7; supports a non-canonical element |
| Targeted XBP1 versus CREB3L4 perturbation followed by PELI2/nearby-locus expression in MCF7 | high | yes | No TF perturbation changes PELI2 or nearby-locus expression | XBP1 perturbation changes PELI2 or nearby-locus expression; CREB3L4 perturbation does not | CREB3L4 perturbation changes PELI2 or nearby-locus expression; XBP1 perturbation does not | CREB1 perturbation changes PELI2 or nearby-locus expression |

## Next experiment

Targeted multiplexed allele-specific ChIP-qPCR for XBP1 and CREB3L4 at chr14:55887040 in MCF7

## Investigate calls

- chip_peaks({"tf": "XBP1", "biosample": "MCF7"})
- chip_peaks({"tf": "CREB3L4", "biosample": "MCF7"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})

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

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41023515 (https://europepmc.org/article/MED/41023515; retrieved 2026-10-25T17:32:50+00:00)

> The Pellino protein family is an evolutionarily conserved group of E3 ubiquitin ligases comprising Pellino1, Pellino2, and Pellino3.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-25T17:32:50+00:00)

> Seven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 40362379 (https://europepmc.org/article/MED/40362379; retrieved 2026-10-25T17:32:50+00:00)

> Hence, we sought to examine whether the cytotoxic effect of O-desmethyltramadol was better than tramadol on breast cancer cells.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 42757486 (https://europepmc.org/article/MED/42757486; retrieved 2026-10-25T17:32:50+00:00)

> Although pathogenic BRCA1 mutations are relatively uncommon, decreased BRCA1 protein expression, which is typically driven by accelerated proteasomal degradation, is implicated in aggressive breast cancer (BC), particularly triple‑negative (TN)BC.

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

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:50:38+00:00)

> No ENCODE CREB3L4 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF7'. Absence can also mean no CREB3L4 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
