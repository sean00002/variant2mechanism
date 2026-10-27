# rs11629191 and Breast cancer

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 139 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: CREB3L2 (z -60.99); CREB3L4 (z -49.16); TET3 (z -44.11); MEIS3 (z -38.69); TGIF1 (z -38.69). Diagnostic, not shown to the model: 445 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated allelic effect at this site (p = 0.84)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF occupancy at chr14:55887040 in MCF7 or other ENCODE biosamples.; No allele-specific regulatory activity or breast-tissue eQTL tracks this base.; Any breast-cancer association at this locus would reflect a linked causal variant, weak chance signal, or passenger status rather than this base.

Falsified if: Allele-specific ChIP/CUT&RUN or MPRA shows a reproducible TF binding difference at this exact base in a breast-cancer cell type.; A breast-tissue eQTL or allelic-expression assay for a nearby gene tracks this variant and is lost when the site is mutated.

### 2. H1: CREB3L4 binds the ref allele at an unannotated element and modulates PELI2 (p = 0.08)

TF CREB3L4 (QBiC-SELEX coverage own_model), ref allele binds more; element non-annotated intergenic element at chr14:55887040; gene PELI2; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB3L4 binds the ref C allele more strongly than the alt T allele. QBiC-SELEX gives CREB3L4 its own model with effect -1.314 and a CIS-BP-mapped CREB3L2 model with effect -2.335; both are ref-higher and above the gate. No ENCODE ChIP-seq peak contains this variant in any biosample, so occupancy is unknown. CREB3L4 is preferred over CREB3L2 because CREB3L4 has its own QBiC-SELEX model and is much more highly expressed in MCF7. | weak | [E15](#e15), [E11](#e11), [E04](#e04), [E09](#e09) |
| element | The variant lies in a non-coding, non-annotated region with no overlapping cCRE; the nearest dELS is 1868 bp away, so any CREB3L4 response element here would be unannotated. | supported | [E01](#e01), [E03](#e03) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb upstream, but GTEx v8 reports no significant eQTL for this variant in any tissue and no breast-tissue eQTL; Open Targets lists only a weak molecular QTL (PIP 0.03) for ENSG00000259868, not PELI2. The variant-to-PELI2 link is therefore indirect. | weak | [E02](#e02), [E07](#e07), [E17](#e17), [E06](#e06), [E08b](#e08b) |
| cell_type | MCF7 cells express CREB3L4 at 48.8 TPM, but no MCF-7 ChIP-seq peak is reported at this site, so expression is present while occupancy in the stated cell type is not established. | weak | [E15](#e15), [E11](#e11), [E04](#e04) |
| phenotype | Altered PELI2 expression could plausibly affect breast-cancer biology because PELI2 is a Pellino E3 ubiquitin ligase with cancer-prognostic literature, but no breast-cancer-specific evidence links this variant to PELI2 or phenotype. | weak | [E08](#e08), [E08a](#e08a), [E08b](#e08b) |

Predictions: Allele-specific CREB3L4 ChIP/CUT&RUN in MCF7 should show stronger ref C than alt T occupancy at this base if the QBiC-SELEX prediction is realized in cells.; An MCF7 reporter carrying the ref vs alt sequence should show ref-higher activity that is reduced by CREB3L4 knockdown.; If CREB3L4 activates PELI2, the alt allele should lower PELI2 expression; if CREB3L4 represses PELI2, the alt allele should increase it.

Falsified if: CREB3L4 shows no allele-specific binding at this base in a direct assay.; CREB3L4 occupancy is absent at this site in MCF7 and PELI2 expression is not allele-linked.; The QBiC-SELEX signal is reproduced only by another bZIP factor and not by CREB3L4 itself.

### 3. H2: TGIF1 binds the ref allele at an unannotated element and represses PELI2 (p = 0.04)

TF TGIF1 (QBiC-SELEX coverage own_model), ref allele binds more; element non-annotated intergenic element at chr14:55887040; gene PELI2; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TGIF1 binds the ref C allele more strongly than the alt T allele. QBiC-SELEX reports effect -2.43 (ref higher, above gate) using a CIS-BP-mapped TGIF2 model; no ENCODE TGIF1 ChIP-seq peak contains the variant in MCF-7, and no ENCODE TF peak contains it in any biosample, so occupancy is unknown. | weak | [E14](#e14), [E16](#e16), [E04](#e04) |
| element | The variant is in a non-coding region with no overlapping cCRE; the nearest annotated dELS is 1868 bp away, so this would be an unannotated regulatory element. | supported | [E01](#e01), [E03](#e03) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb upstream, but GTEx v8 reports no significant eQTL and no breast-tissue eQTL for this variant; Open Targets' weak molecular QTL is for ENSG00000259868, not PELI2. | weak | [E02](#e02), [E07](#e07), [E17](#e17), [E06](#e06), [E08b](#e08b) |
| cell_type | TGIF1 is expressed in MCF7 at 39.86 TPM, but no MCF-7 TGIF1 ChIP-seq peak is reported here; absence can also mean no TGIF1 experiment in that biosample. | weak | [E14](#e14), [E16](#e16), [E04](#e04) |
| phenotype | Because TGIF1 is a transcriptional repressor, loss of TGIF1 binding on the alt allele could de-repress PELI2 and contribute to breast-cancer biology; this is speculative and relies on generic Pellino/PELI2 cancer literature. | weak | [E08](#e08), [E08a](#e08a), [E08b](#e08b) |

Predictions: Allele-specific TGIF1 ChIP/CUT&RUN should show stronger ref C than alt T binding at this site if TGIF1 occupies it in MCF7.; If TGIF1 represses PELI2, the alt allele should increase PELI2 expression in MCF7 cells.; The allele-specific effect should be reduced when TGIF1 is knocked down.

Falsified if: TGIF1 does not occupy this site or shows no allele-specific binding in a direct assay.; The alt allele does not change PELI2 expression in a TGIF1-dependent manner.; The shared TGIF2/MEIS3 model signal is shown to be driven by another factor.

### 4. H3: CREB3L2 binds the ref allele at an unannotated element (p = 0.04)

TF CREB3L2 (QBiC-SELEX coverage own_model), ref allele binds more; element non-annotated intergenic element at chr14:55887040; gene PELI2; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB3L2 binds the ref C allele more strongly than the alt T allele. QBiC-SELEX reports effect -2.258 with z -60.99 (ref higher) using a CIS-BP-mapped CREB3L1 model; no ENCODE ChIP-seq peak contains this variant, so occupancy is unknown and this is in vitro binding evidence only. | weak | [E10](#e10), [E04](#e04), [E09](#e09) |
| element | The variant is not in an annotated cCRE and the nearest dELS is 1868 bp away, so any CREB3L2 element would be unannotated. | supported | [E01](#e01), [E03](#e03) |
| gene | PELI2 is the nearest protein-coding gene, 230.8 kb upstream, but direct evidence that this variant regulates PELI2 is absent; GTEx reports no significant eQTL and no breast-tissue eQTL, and Open Targets' weak molecular QTL is not for PELI2. | weak | [E02](#e02), [E07](#e07), [E17](#e17), [E06](#e06), [E08b](#e08b) |
| cell_type | CREB3L2 is expressed in MCF7 at only 7.06 TPM, and no MCF-7 ChIP-seq peak is reported at this site; the cell-type link is expression-only. | weak | [E10](#e10), [E04](#e04) |
| phenotype | If CREB3L2 regulates PELI2, altered PELI2 dosage could affect breast-cancer biology through Pellino E3 ligase function, but this link is unproven and supported only by generic cancer literature. | weak | [E08](#e08), [E08a](#e08a), [E08b](#e08b) |

Predictions: Allele-specific CREB3L2 ChIP/CUT&RUN should show stronger ref C than alt T binding at this base if CREB3L2 occupies it in MCF7.; The effect should be weaker in MCF7 than for CREB3L4 because CREB3L2 is expressed at lower levels.; If CREB3L2 activates PELI2, the alt allele should lower PELI2 expression.

Falsified if: CREB3L2 does not bind this site in a direct assay despite the QBiC-SELEX prediction.; The QBiC-SELEX signal is not reproduced for CREB3L2 itself and instead reflects a related bZIP factor.; No allele-specific PELI2 expression change is observed.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CREB3L4 ChIP-qPCR or CUT&RUN in MCF7 at chr14:55887040 | medium | yes | No reproducible ref>alt CREB3L4 occupancy at this base. | Reproducible ref>alt CREB3L4 occupancy at this base. | No CREB3L4 occupancy; any occupancy would be TGIF1, not CREB3L4. | No CREB3L4 occupancy; any bZIP occupancy would be CREB3L2, not CREB3L4. |
| MCF7 reporter/MPRA with 200-bp ref vs alt sequence and CREB3L4 knockdown | medium | yes | No reproducible allele-specific reporter activity. | Ref-higher activity that is reduced by CREB3L4 knockdown. | TGIF1-dependent, not CREB3L4-dependent, allele-specific activity if any. | CREB3L2-dependent, not CREB3L4-dependent, allele-specific activity if any. |
| Allele-specific TGIF1 ChIP-qPCR or CUT&RUN in MCF7 at chr14:55887040 | medium | no | No reproducible TGIF1 occupancy difference. | No TGIF1 occupancy; CREB3L4 is the candidate bZIP. | Reproducible ref>alt TGIF1 occupancy at this base. | No TGIF1 occupancy; CREB3L2 is the candidate bZIP. |
| Breast-tissue eQTL or allelic-expression assay for PELI2 in heterozygous samples | existing data | yes | No allele-specific PELI2 expression; current GTEx breast data show no significant eQTL. | If CREB3L4 activates PELI2, alt T associates with lower PELI2; no eQTL weakens H1. | If TGIF1 represses PELI2, alt T associates with higher PELI2; no eQTL weakens H2. | If CREB3L2 activates PELI2, alt T associates with lower PELI2; no eQTL weakens H3. |

## Next experiment

Perform allele-specific CREB3L4 ChIP-qPCR or CUT&RUN in MCF7 at chr14:55887040; this is the cheapest direct test that separates H0 (no allelic CREB3L4 occupancy) from H1 (ref C binds CREB3L4 more strongly than alt T).

## Investigate calls

- qbic_tf_detail({"tf": "CREB3L4"})
- chip_peaks({"tf": "TGIF1", "biosample": "MCF-7"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})

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

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:41:39+00:00)

> No ENCODE TGIF1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7'. Absence can also mean no TGIF1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
