# rs7001688 and LDL cholesterol

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 133 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen

441 of 997 models pass the gate. Top groups: Rel, 1 model (best RELA, z 33.95); C2H2 ZF, 1 model (best CASZ1, z 32.75); AT hook, 2 models (best HMGA1, z 29.74); C2H2 ZF, 1 model (best ZNF580, z -29.06); Unknown, 1 model (best NME2, z 28.95).

## Ranked chains

### 1. chain_4_null: No TF-mediated effect of rs7001688 (p = 0.78)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs7001688 in relevant chromatin.; No regulatory effect of the variant in hepatocyte models.; Any observed LDL association is due to a linked causal variant or is not mediated by this variant.

Falsified if: Allele-specific RELA, HMGA1, or other TF ChIP-seq/CUT&RUN, MPRA, or CRISPR editing shows a reproducible TF-dependent regulatory effect at rs7001688.; An eQTL or functional assay links this exact variant to LDL cholesterol through a TF.

### 2. chain_1_RELA_FAM110B: RELA binds the alt allele at an unannotated element and may alter FAM110B (p = 0.12)

TF RELA (stated coverage own_model; registry own_model), alt allele binds more; element No annotated cCRE overlaps rs7001688 and the nearest cCRE is 1544 bp away. This shows absence of annotated regulatory annotation, not positive evidence for a functional unannotated RELA-responsive element.; gene FAM110B; cell type Hep 3B2.1-7 is the provided expression context and expresses RELA at 73.44 TPM; this does not establish Hep3B as LDL-relevant or that RELA regulates FAM110B there..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G315 names RELA as an own-model TF and predicts that the alt T allele binds RELA more strongly than ref G (z 33.95, effect 1.34). RELA is chosen over mapped RELB and REL because it has an own model, the strongest positive group score, and expression in Hep3B; this is in vitro binding only, and no ENCODE RELA ChIP-seq peak contains the site, although absence is not conclusive. | weak | [E08](#e08), [E07](#e07), [E19](#e19) |
| element | The variant has no annotated cCRE overlap and lies 1544 bp from the nearest cCRE, so any RELA effect would require an unannotated element rather than a known regulatory region. | supported | [E01](#e01), [E03](#e03) |
| gene | FAM110B is the nearest listed protein-coding gene at 420.6 kb, but distance alone is not target-gene evidence. E06 is only a literature-search hit about pravastatin cardiovascular response, not direct evidence that rs7001688 regulates FAM110B. | missing | [E02](#e02), [E06](#e06) |
| cell_type | Hep 3B2.1-7 is the provided expression context and expresses RELA at 73.44 TPM in the QBiC-SELEX RNA context, but the evidence does not show that Hep3B is the disease-relevant cell type for LDL cholesterol or that RELA regulates FAM110B in Hep3B. | weak | [E07](#e07), [E08](#e08) |
| phenotype | There is no provided genetic or perturbation evidence linking rs7001688 to LDL cholesterol through RELA or FAM110B; GWAS Catalog and Open Targets have no record for the variant, and E06 is only an indirect literature title. | supported | [E04](#e04), [E05](#e05), [E06](#e06) |

Predictions: Allele-specific RELA occupancy at rs7001688 in Hep3B cells, with alt greater than ref.; RELA-dependent regulatory activity or FAM110B expression change after editing rs7001688.; A measurable LDL-cholesterol effect mediated by this RELA-bound element and FAM110B.

Falsified if: No RELA occupancy or allele-specific RELA binding at rs7001688 in Hep3B cells.; No RELA-dependent regulatory or expression effect after editing rs7001688.; No link between the edited variant and LDL cholesterol in a relevant model.

### 3. chain_2_HMGA1_FAM110B: HMGA1 binds the alt allele at an unannotated element and may alter FAM110B (p = 0.10)

TF HMGA1 (stated coverage own_model; registry own_model), alt allele binds more; element No annotated cCRE overlaps rs7001688 and the nearest cCRE is 1544 bp away, so this chain requires an unannotated AT-rich element; the evidence does not positively establish such an element.; gene FAM110B; cell type Hep 3B2.1-7 is the provided expression context and expresses HMGA1 at 238.96 TPM; this does not establish disease-relevant HMGA1 function or HMGA1 regulation of FAM110B..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX group G077 names HMGA1 as an own-model TF and predicts that the alt T allele binds HMGA1 more strongly than ref G (z 29.74, effect 2.006). HMGA1 is chosen by own-model status, strongest positive score, and high Hep3B expression, but the group contains SETBP1 with the opposite direction, and this is in vitro binding only; no ENCODE HMGA1 ChIP-seq peak contains the site, although absence is not conclusive. | weak | [E10](#e10), [E07](#e07), [E20](#e20) |
| element | The variant has no annotated cCRE overlap and lies 1544 bp from the nearest cCRE, so an HMGA1 effect would have to act through an unannotated element. | supported | [E01](#e01), [E03](#e03) |
| gene | FAM110B is the nearest listed protein-coding gene at 420.6 kb, but distance alone is not target-gene evidence. E06 is only a literature-search hit about pravastatin cardiovascular response, not direct evidence that rs7001688 regulates FAM110B. | missing | [E02](#e02), [E06](#e06) |
| cell_type | Hep 3B2.1-7 expresses HMGA1 at high levels in the QBiC-SELEX RNA context, but the evidence does not show that Hep3B is disease-relevant for LDL cholesterol or that HMGA1 regulates FAM110B there. | weak | [E07](#e07), [E10](#e10) |
| phenotype | There is no provided genetic or perturbation evidence linking rs7001688 to LDL cholesterol through HMGA1 or FAM110B; GWAS Catalog and Open Targets have no record for the variant, and E06 is only an indirect literature title. | supported | [E04](#e04), [E05](#e05), [E06](#e06) |

Predictions: Allele-specific HMGA1 occupancy at rs7001688 in Hep3B cells, with alt greater than ref.; HMGA1-dependent chromatin accessibility or regulatory activity difference between ref and alt alleles.; HMGA1-dependent FAM110B expression change and LDL-cholesterol effect.

Falsified if: No HMGA1 occupancy or allele-specific HMGA1 binding at rs7001688 in Hep3B cells.; No HMGA1-dependent regulatory or expression effect after editing rs7001688.; No link between the edited variant and LDL cholesterol in a relevant model.

## Prediction matrix

| Test | Cost | Separates top two | chain_4_null | chain_1_RELA_FAM110B | chain_2_HMGA1_FAM110B |
| --- | --- | --- | --- | --- | --- |
| Allele-specific RELA ChIP-qPCR or CUT&RUN-qPCR at rs7001688 in Hep3B cells heterozygous for the variant | medium | yes | No allele-specific RELA occupancy at rs7001688. | Allele-specific RELA occupancy at rs7001688, alt greater than ref. | No allele-specific RELA occupancy at rs7001688. |
| Allele-specific HMGA1 ChIP-qPCR or CUT&RUN-qPCR at rs7001688 in Hep3B cells heterozygous for the variant | medium | no | No allele-specific HMGA1 occupancy at rs7001688. | No allele-specific HMGA1 occupancy at rs7001688. | Allele-specific HMGA1 occupancy at rs7001688, alt greater than ref. |
| CRISPR edit rs7001688 to ref/ref versus alt/alt in Hep3B and measure FAM110B expression | high | yes | No reproducible change in FAM110B expression after editing rs7001688 in Hep3B. | Editing rs7001688 changes FAM110B expression in a RELA-dependent direction. | Editing rs7001688 changes FAM110B expression in an HMGA1-dependent direction. |
| Allele-specific MPRA reporter assay for the rs7001688 ref and alt alleles in Hep3B cells | medium | yes | No allele-specific reporter activity difference. | Alt allele shows higher reporter activity, potentially RELA-dependent. | Alt allele shows higher reporter activity, potentially HMGA1-dependent. |

## Next experiment

The single cheapest experiment that separates the top two chains is allele-specific RELA ChIP-qPCR or CUT&RUN-qPCR at rs7001688 in Hep3B cells heterozygous for the variant: alt-greater-than-ref RELA occupancy supports the RELA chain, while no allele-specific RELA occupancy supports the null over the RELA chain (chain costs medium).

## Investigate calls

- eqtl_lookup({"tissue": null})
- chip_peaks({"tf": "RELA", "biosample": null})
- chip_peaks({"tf": "HMGA1", "biosample": null})

## Flags

- literature_fallback: no hits for 'rs7001688 AND FAM110B AND "ldl cholesterol"'; dropped the rsID

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:57573391-57573391:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:33:20+00:00)

> Variant chr8:57573391:G>T (GRCh38), allele string G/T
> Known IDs: rs7001688
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 0.267
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:56573391-58573391?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:33+00:00)

> 5 protein-coding genes within 1000 kb of chr8:57573391:G>T, by distance to TSS:
> FAM110B: 420.6 kb from TSS (upstream, strand +1)
> BPNT2: 579.5 kb from TSS (upstream, strand -1)
> UBXN2B: 838.0 kb from TSS (upstream, strand +1)
> CYP7A1: 926.8 kb from TSS (downstream, strand -1)
> SDCBP: 979.5 kb from TSS (upstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:27+00:00)

> No cCRE overlaps the variant; nearest is EH38E3835076 (CA-H3K4me3) 1544 bp away.
> SCREEN: 0 cCREs within 500 bp (max z-score across ENCODE biosamples):
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs7001688&size=100; retrieved 2026-10-25T17:33:20+00:00)

> 0 GWAS Catalog associations for rs7001688, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:33:20+00:00)

> Open Targets has no record of 8_57573391_G_T.

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=FAM110B%20AND%20%22ldl%20cholesterol%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:33:21+00:00)

> Europe PMC: 1 hits for 'FAM110B AND "ldl cholesterol"'; top 1 with PMIDs:
> PMID 22666496 (2012): Genome-wide study of gene variants associated with differential cardiovascular event reduction by pravastatin therapy.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:57573391:G>T: 997 models scored, 441 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 316 CIS-BP groups. Expression context: DepMap line ACH-000625. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 73 (BED ZF, 1 model z 24.73, C2H2 ZF, 1 model z -21.17, DM, 5 models z -18.3, C2H2 ZF, 1 model z 16.96, C2H2 ZF, 1 model z -16.13). Passing groups ranked below the ones shown: 233. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G315 (Rel, 1 model): best model RELA_DBD_TGATCC20NCTA_KI_nitta2015_1_3_7mer (own model of RELA), z 33.95, effect 1.34 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: RELA z 33.95. TFs this group covers: RELA (own model) 73.44 TPM, RELB (mapped) 17.37 TPM, REL (mapped) 4.27 TPM; best model's site strength: ref 97.4th, alt 99.8th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G138 (C2H2 ZF, 1 model): best model CASZ1_FL_AG40NGGAATC_YWKC_jolma2025_0_4_7mer (own model of CASZ1), z 32.75, effect 2.741 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CASZ1 z 32.75. TFs this group covers: CASZ1 (own model) 4.18 TPM; best model's site strength: ref 99.1th, alt 99.8th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G077 (AT hook, 2 models): best model HMGA1_FL_GA40NCTGATT_YWPA_jolma2025_0_3_7mer (own model of HMGA1), z 29.74, effect 2.006 (alt binds more); 2 passing models (1 with the best model's sign); members disagree on direction. Passing members: HMGA1 z 29.74, SETBP1 z -15.21. TFs this group covers: HMGA1 (own model) 238.96 TPM, HMGA2 (mapped) 97.36 TPM, SRCAP (mapped) 41.42 TPM, ASH1L (mapped) 21.18 TPM, SETBP1 (own model) 1.24 TPM; best model's site strength: ref 67.3th, alt 96.4th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G540 (C2H2 ZF, 1 model): best model ZNF580_FL_TGGCCA40NTTC_KAE_yin2017_0_4_7mer (own model of ZNF580), z -29.06, effect -1.205 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF580 z -29.06. TFs this group covers: ZNF580 (own model) 8.54 TPM; best model's site strength: ref 100.0th, alt 94.4th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G266 (Unknown, 1 model): best model NME2_FL_TA40NTCACTC_YWDA_jolma2025_0_4_7mer (own model of NME2), z 28.95, effect 0.573 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: NME2 z 28.95. TFs this group covers: NME2 (own model) 928.15 TPM; best model's site strength: ref 65.7th, alt 99.1th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G460 (C2H2 ZF, 1 model): best model ZNF230_FL_TG40NGACCTT_YWDA_jolma2025_0_3_7mer (own model of ZNF230), z 26.94, effect 0.512 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF230 z 26.94. TFs this group covers: ZNF230 (own model) 1.96 TPM; best model's site strength: ref 70.8th, alt 96.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G018 (E2F, 4 models): best model E2F4_eDBD_TCAGGG40NGCA_KO_yin2017_1_3_7mer (own model of E2F4), z 25.88, effect 1.189 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: E2F4 z 25.88, E2F3 z 17.58. TFs this group covers: E2F4 (own model) 58.99 TPM, E2F3 (own model) 36.15 TPM, E2F5 (mapped) 18.97 TPM, E2F6 (mapped) 18.07 TPM, E2F1 (own model) 11.74 TPM, E2F2 (own model) 2.06 TPM; best model's site strength: ref 98.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G499 (C2H2 ZF, 1 model): best model ZNF384_FL_GG40NTAGTTT_AATBA_jolma2025_0_3_7mer (own model of ZNF384), z -24.76, effect -0.523 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF384 z -24.76. TFs this group covers: ZNF384 (own model) 82.82 TPM; best model's site strength: ref 82.1th, alt 68.4th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G031 (TEA, 4 models): best model TEAD1_FL_TCACGC40NACT_KW_yin2017_0_4_7mer (own model of TEAD1), z 23.14, effect 1.505 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: TEAD1 z 23.14, TEAD4 z 10.66, TEAD2 z 9.59, TEAD3 z 8.07. TFs this group covers: TEAD2 (own model) 34.44 TPM, TEAD1 (own model) 29.24 TPM, TEAD4 (own model) 28.13 TPM, TEAD3 (own model) 17.77 TPM; best model's site strength: ref 84.6th, alt 99.2th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G338 (Unknown, 1 model): best model SNAPC5_FL_CA40NAGCGTA_YWDA_jolma2025_0_3_7mer (own model of SNAPC5), z 22.9, effect 0.368 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SNAPC5 z 22.9. TFs this group covers: SNAPC5 (own model) 86.73 TPM; best model's site strength: ref 80.4th, alt 98.2th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:34:31+00:00)

> No ENCODE RELA ChIP-seq peak contains chr8:57573391:G>T. Absence can also mean no RELA experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:45:05+00:00)

> No ENCODE HMGA1 ChIP-seq peak contains chr8:57573391:G>T. Absence can also mean no HMGA1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.
