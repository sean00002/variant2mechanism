# rs11629191 and Breast cancer

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 295 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: CREB3L2 (z -60.99); CREB3L4 (z -49.16); TET3 (z -44.11); MEIS3 (z -38.69); TGIF1 (z -38.69). Diagnostic, not shown to the model: 445 of 997 models pass Bonferroni.

## Ranked chains

### 1. null: Null: no TF-mediated allelic effect from rs11629191 (p = 0.87)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at chr14:55887040 in MCF-7 or other breast cells.; No reproducible allele-dependent reporter activity for this base.; No breast-tissue eQTL or colocalization attributable to this variant.

Falsified if: Allele-specific CUT&RUN/ChIP at this exact base in MCF-7 shows a reproducible ref-vs-alt occupancy difference for a specific TF.; An allele-swap reporter or MPRA shows a reproducible, TF-dependent expression change at PELI2 or another nearby locus.; A reproducible breast eQTL for this variant colocalizes with a breast cancer signal.

### 2. CREB3L4_ref_PELI2: CREB3L4 binds the ref C allele more strongly at an unannotated element and alters PELI2 (p = 0.08)

TF CREB3L4 (QBiC-SELEX coverage own_model), ref allele binds more; element unannotated intronic/intergenic segment; no cCRE overlap; cryptic element unproven; gene PELI2; cell type MCF7 (DepMap ACH-000019) breast cancer cells; relevance unproven.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX has a CREB3L4 own-model hit at this base: effect -1.314, z -37.55, meaning the ref C allele binds CREB3L4 more strongly than the alt T allele in vitro; a CIS-BP-mapped CREB3L2 model also reports ref>alt. No ENCODE ChIP-seq peak contains this base and CREB3L4 was not assayed in MCF-7, so occupancy is unknown. I choose CREB3L4 as the top non-null because it has an own-model QBiC signal and is well expressed in MCF7 (48.8 TPM, rank 68/1626), not because occupancy is demonstrated. | weak | [E15](#e15), [E11](#e11), [E04](#e04), [E09](#e09) |
| element | The variant is an intronic/intergenic base with no overlapping cCRE; the nearest dELS is 1,868 bp away, GERP is -3.12, and no ENCODE TF peak contains the base. This establishes only that no annotated element overlaps the variant; a functional cryptic element in MCF-7 is not demonstrated. | weak | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb, but GTEx v8 reports no eQTL for this variant, the only molecular QTL is for ENSG00000259868 with PIP 0.03 in brain nucleus accumbens, and PELI2 is not a dependency in breast lines. PELI2 is therefore a proximity-based candidate only, not a supported target. | missing | [E02](#e02), [E06](#e06), [E07](#e07), [E16](#e16) |
| cell_type | MCF7 is the expression context, where CREB3L4 is expressed at 48.8 TPM (rank 68/1626); however, no MCF-7 ENCODE ChIP-seq peak is present at this base. The choice of MCF-7 as the relevant cell type is plausible from expression but not proven by occupancy. | weak | [E11](#e11), [E04](#e04) |
| phenotype | rs11629191 has no GWAS Catalog association and no GTEx v8 eQTL; PELI2 literature is generic Pellino biology or a papillary thyroid carcinoma prognostic signature, and PELI2 is not a breast-line dependency. A CREB3L4-dependent effect on breast cancer through PELI2 is speculative. | missing | [E05](#e05), [E07](#e07), [E08](#e08), [E16](#e16) |

Predictions: CREB3L4 CUT&RUN/ChIP in MCF-7 or a heterozygous breast line shows stronger occupancy on the ref C allele than the alt T allele at chr14:55887040.; CREB3L4 knockdown reduces allele-dependent reporter activity if this element regulates PELI2 or a nearby gene.; The effect should be more detectable in breast cells with high CREB3L4 expression, such as MCF-7 (48.8 TPM, rank 68/1626).

Falsified if: Allele-specific CREB3L4 CUT&RUN/ChIP shows no ref>alt occupancy at this base in MCF-7 or a heterozygous breast line.; CREB3L4 knockdown does not affect allele-dependent reporter activity.; No reproducible breast eQTL or expression change at PELI2 or nearby genes is found for this variant.

### 3. CREB3L2_ref_PELI2: CREB3L2 binds the ref C allele more strongly at an unannotated element and alters PELI2 (p = 0.03)

TF CREB3L2 (QBiC-SELEX coverage own_model), ref allele binds more; element unannotated intronic/intergenic segment; no cCRE overlap; cryptic element unproven; gene PELI2; cell type MCF7 (DepMap ACH-000019) breast cancer cells; relevance unproven.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The QBiC-SELEX line listed for CREB3L2 uses a CIS-BP-mapped CREB3L1 bZIP model (effect -2.258, z -60.99), not a CREB3L2-specific model; if that mapped model reflects CREB3L2, the ref C allele binds more strongly than the alt T allele in vitro. No ENCODE ChIP-seq peak contains this base and CREB3L2 was not assayed, so occupancy is unknown. I retain CREB3L2 only as a weaker bZIP competitor because the mapped signal is strong but MCF7 expression is low (7.06 TPM, rank 534/1626). | weak | [E10](#e10), [E04](#e04), [E09](#e09) |
| element | The variant is an intronic/intergenic base with no overlapping cCRE; the nearest dELS is 1,868 bp away, GERP is -3.12, and no ENCODE TF peak contains the base. This establishes only that no annotated element overlaps the variant; a functional cryptic element in MCF-7 is not demonstrated. | weak | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb, but GTEx v8 reports no eQTL for this variant, the only molecular QTL is for ENSG00000259868 with PIP 0.03 in brain nucleus accumbens, and PELI2 is not a dependency in breast lines. PELI2 is therefore a proximity-based candidate only, not a supported target. | missing | [E02](#e02), [E06](#e06), [E07](#e07), [E16](#e16) |
| cell_type | MCF7 is the expression context, where CREB3L2 is expressed at only 7.06 TPM (rank 534/1626); no MCF-7 ENCODE ChIP-seq peak is present at this base. Low expression plus no occupancy makes the MCF-7 relevance of this chain weak. | weak | [E10](#e10), [E04](#e04) |
| phenotype | rs11629191 has no GWAS Catalog association and no GTEx v8 eQTL; PELI2 literature is generic Pellino biology or a papillary thyroid carcinoma prognostic signature, and PELI2 is not a breast-line dependency. A CREB3L2-dependent effect on breast cancer through PELI2 is speculative. | missing | [E05](#e05), [E07](#e07), [E08](#e08), [E16](#e16) |

Predictions: CREB3L2 CUT&RUN/ChIP in MCF-7 shows stronger occupancy on the ref C allele than the alt T allele at chr14:55887040, if the mapped CREB3L1 model reflects CREB3L2 binding.; CREB3L2 knockdown reduces allele-dependent reporter activity.; Because CREB3L2 is expressed at only 7.06 TPM in MCF-7, any effect should be weaker than for a well-expressed paralog unless CREB3L2 is locally enriched.

Falsified if: Allele-specific CREB3L2 CUT&RUN/ChIP shows no ref>alt occupancy at this base in MCF-7.; CREB3L2 knockdown does not affect allele-dependent reporter activity.; No reproducible breast eQTL or expression change at PELI2 or nearby genes is found for this variant.

### 4. TGIF1_ref_PELI2: TGIF1 binds the ref C allele more strongly at an unannotated element and alters PELI2 (p = 0.02)

TF TGIF1 (QBiC-SELEX coverage own_model), ref allele binds more; element unannotated intronic/intergenic segment; no cCRE overlap; cryptic element unproven; gene PELI2; cell type MCF7 (DepMap ACH-000019) breast cancer cells; relevance unproven.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX lists a TGIF1 line with effect -2.43, z -38.69, meaning the ref C allele binds more strongly than the alt T allele in vitro, but the best model is a CIS-BP-mapped TGIF2 model shared with MEIS3, not a TGIF1-specific model. TGIF1 was never assayed by ENCODE and no peak contains this base, so occupancy is unknown. Choosing TGIF1 over MEIS3 by expression alone (39.86 vs 15.61 TPM) does not establish which paralog binds; this is weak evidence. | weak | [E14](#e14), [E13](#e13), [E04](#e04), [E09](#e09) |
| element | The variant is an intronic/intergenic base with no overlapping cCRE; the nearest dELS is 1,868 bp away, GERP is -3.12, and no ENCODE TF peak contains the base. This establishes only that no annotated element overlaps the variant; a functional cryptic element in MCF-7 is not demonstrated. | weak | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | PELI2 is the nearest protein-coding gene at 230.8 kb, but GTEx v8 reports no eQTL for this variant, the only molecular QTL is for ENSG00000259868 with PIP 0.03 in brain nucleus accumbens, and PELI2 is not a dependency in breast lines. PELI2 is therefore a proximity-based candidate only, not a supported target. | missing | [E02](#e02), [E06](#e06), [E07](#e07), [E16](#e16) |
| cell_type | MCF7 is the expression context, where TGIF1 is expressed at 39.86 TPM (rank 95/1626); however, no MCF-7 ENCODE ChIP-seq peak is present at this base. Expression in MCF-7 does not establish allele-specific TGIF1 occupancy. | weak | [E14](#e14), [E04](#e04) |
| phenotype | rs11629191 has no GWAS Catalog association and no GTEx v8 eQTL; PELI2 literature is generic Pellino biology or a papillary thyroid carcinoma prognostic signature, and PELI2 is not a breast-line dependency. A TGIF1-dependent effect on breast cancer through PELI2 is speculative. | missing | [E05](#e05), [E07](#e07), [E08](#e08), [E16](#e16) |

Predictions: TGIF1 CUT&RUN/ChIP in MCF-7 shows stronger occupancy on the ref C allele than the alt T allele at chr14:55887040, if the shared TGIF2 model reflects TGIF1 binding.; TGIF1 knockdown reduces allele-dependent reporter activity.; Because the QBiC model is shared with MEIS3, a paralog-specific CUT&RUN/ChIP would be needed to distinguish TGIF1 from MEIS3.

Falsified if: Allele-specific TGIF1 CUT&RUN/ChIP shows no ref>alt occupancy at this base in MCF-7.; TGIF1 knockdown does not affect allele-dependent reporter activity.; MEIS3, rather than TGIF1, accounts for any shared-model allele-specific occupancy.

## Prediction matrix

| Test | Cost | Separates top two | null | CREB3L4_ref_PELI2 | CREB3L2_ref_PELI2 | TGIF1_ref_PELI2 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CREB3L4 CUT&RUN/ChIP-qPCR in MCF-7 or a heterozygous breast line at rs11629191 | medium | yes | Null chain predicts no reproducible ref-vs-alt difference in CREB3L4 occupancy at this base, and likely no CREB3L4 occupancy at all. | CREB3L4 chain predicts stronger CREB3L4 occupancy on the ref C allele than on the alt T allele at the variant. | CREB3L2 chain predicts no CREB3L4-specific ref>alt occupancy; any signal should follow CREB3L2, not CREB3L4. | TGIF1 chain predicts no CREB3L4-specific ref>alt occupancy; any allele-specific signal should follow TGIF1/MEIS3, not CREB3L4. |
| Allele-specific reporter or MPRA in MCF-7 with CREB3L4 knockdown | high | yes | Null chain predicts no reproducible allele-dependent reporter activity and no effect of CREB3L4 knockdown. | CREB3L4 chain predicts higher activity from the ref C allele than the alt T allele, and this difference is reduced by CREB3L4 knockdown. | CREB3L2 chain predicts no CREB3L4-dependent allele effect; any effect should require CREB3L2 knockdown instead. | TGIF1 chain predicts no CREB3L4-dependent allele effect; any effect should require TGIF1/MEIS3 knockdown instead. |
| Allele-specific CREB3L2 CUT&RUN/ChIP-qPCR in MCF-7 at rs11629191 | medium | no | Null chain predicts no allele-specific CREB3L2 occupancy. | CREB3L4 chain predicts no allele-specific CREB3L2 occupancy. | CREB3L2 chain predicts ref C > alt T CREB3L2 occupancy, though expression is low in MCF-7 and the QBiC model is a mapped CREB3L1 model. | TGIF1 chain predicts no allele-specific CREB3L2 occupancy. |
| Allele-specific TGIF1 and MEIS3 CUT&RUN/ChIP-qPCR in MCF-7 at rs11629191 | medium | no | Null chain predicts no allele-specific TGIF1 or MEIS3 occupancy. | CREB3L4 chain predicts no allele-specific TGIF1 or MEIS3 occupancy. | CREB3L2 chain predicts no allele-specific TGIF1 or MEIS3 occupancy. | TGIF1 chain predicts ref C > alt T TGIF1 occupancy; because the QBiC model is a CIS-BP-mapped TGIF2 model shared with MEIS3, MEIS3 may also show the same allele preference, so paralog-specific follow-up would be required. |
| Breast-tissue eQTL/colocalization for rs11629191 with PELI2 or nearby genes | low | yes | Null chain predicts no reproducible breast eQTL and no colocalization with breast cancer signals. | CREB3L4 chain predicts a reproducible breast eQTL for PELI2 or a nearby gene if this cryptic element is functional in breast cells; absence weakens the gene link. | CREB3L2 chain predicts the same eQTL pattern, but with no CREB3L2-specific support unless occupancy is also shown. | TGIF1 chain predicts the same eQTL pattern, but with no TGIF1-specific support unless occupancy is also shown. |

## Next experiment

CREB3L4 CUT&RUN or ChIP-qPCR in an MCF-7/breast line heterozygous for rs11629191, with allele-specific readout at the variant

## Investigate calls

- qbic_tf_detail({"tf": "CREB3L4"})
- gene_dependency({"gene": "PELI2"})
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

> QBiC-SELEX screen of chr14:55887040:C>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000019), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 0 of 0 occupied, 5 of 113 with unknown occupancy. Left out: 65 TFs assayed in the matching biosample and 508 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. No ENCODE TF ChIP-seq peak contains this variant in any biosample; QBiC-SELEX changes below have no occupancy support.

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

<a id="e16"></a>**E16** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for PELI2 (0 = no effect, -1 = median common-essential; < -0.5 called dependent). MCF7 (ACH-000019): 0.01. Breast lineage, 53 lines: median -0.02, 0% dependent. All 1183 lines: median -0.03, 0% dependent.

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).
