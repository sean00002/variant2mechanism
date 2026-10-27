# rs56007086 and Breast cancer (16q12)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 223 s.

Variant `chr16:52565398:G>A` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen

569 of 997 models pass the gate. Top groups: C2H2 ZF, 1 model (best ZNF395, z -53.42); Ets, 18 models (best ETV5, z -47.67); C2H2 ZF, 1 model (best SLC2A4RG, z -45.42); mTERF, 1 model (best MTERF3, z 24.43); bHLH, 2 models (best SREBF1, z 24.29).

## Ranked chains

### 1. null: No TF-mediated allelic effect at rs56007086 (p = 0.50)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at the variant in breast cancer cells.; No reproducible TOX3 expression difference between rs56007086 alleles in breast tissue or breast cancer cells.; Any 16q12 breast cancer association is explained by linkage to another causal variant, a passenger event, or an effect not mediated by allele-specific TF binding at this base.

Falsified if: Allele-specific binding of a candidate TF is demonstrated at this position in an appropriate breast cell system.; The alt allele reproducibly changes TOX3 expression in an allele-specific manner in breast cells.

### 2. TFAP2C: Alt allele strengthens TFAP2C binding at a TOX3 enhancer (p = 0.15)

TF TFAP2C (stated coverage own_model; registry own_model), alt allele binds more; element ENSR16_9QTBS enhancer / nearby dELS EH38E3180851; gene TOX3; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2C has its own QBiC-SELEX model in AP-2 group G030, and all four AP-2 models pass with positive alt effect; TFAP2C itself has z 10.07 with predicted_effect > 0 meaning alt binds more. However, no ENCODE TFAP2C ChIP-seq peak contains this variant in MCF7; absence is not definitive because there may be no TFAP2C experiment in that biosample. | weak | [E17](#e17), [E18](#e18) |
| element | The variant lies in the VEP-predicted enhancer ENSR16_9QTBS and 38 bp from the active dELS EH38E3180851, but no ENCODE cCRE directly overlaps the variant base, so the enhancer assignment is plausible but not fully resolved. | weak | [E01](#e01), [E03](#e03) |
| gene | TOX3 is proposed as the target because it is the nearest protein-coding gene at 17.6 kb upstream and CASC16 is the local intronic transcript. There is no breast-tissue eQTL for this variant and no enhancer-promoter interaction evidence. | weak | [E02](#e02), [E03](#e03), [E19](#e19) |
| cell_type | MCF7 is the DepMap expression context; TFAP2C is directly reported as expressed at 44.3 TPM in ACH-000019, so it is present in this breast cancer cell line. | supported | [E07](#e07), [E17](#e17) |
| phenotype | TOX3 is a literature-supported breast cancer locus and 16q12 is a breast cancer risk region, but rs56007086 itself has no GWAS Catalog or Open Targets record and no breast-tissue eQTL, so the phenotype link is indirect. | weak | [E06a](#e06a), [E06b](#e06b), [E04](#e04), [E05](#e05), [E19](#e19) |

Predictions: Allele-specific TFAP2C ChIP-qPCR shows stronger TFAP2C binding to the alt allele at this element in MCF7 or another heterozygous breast cancer line.; An allele-specific TOX3 enhancer reporter shows higher activity from the alt allele in MCF7.; Mutation of the AP-2 motif abolishes the alt-allele reporter effect.

Falsified if: TFAP2C does not occupy this element in breast cancer cells.; The alt allele does not increase TOX3 reporter activity, or the effect is not AP-2-motif dependent.; TFAP2C knockdown does not reduce TOX3 expression from this locus.

### 3. PBX1: Alt allele strengthens PBX1 binding at a TOX3 enhancer (p = 0.14)

TF PBX1 (stated coverage own_model; registry own_model), alt allele binds more; element ENSR16_9QTBS enhancer / nearby dELS EH38E3180851; gene TOX3; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | PBX1 has its own QBiC-SELEX model in homeodomain group G274, with z 18.55 and effect 0.733, meaning alt binds more strongly. PBX1 is chosen because it has the own model and is expressed in the MCF7 context; PBX2-4 are only mapped in this group. | weak | [E14](#e14) |
| element | The variant is within the VEP enhancer ENSR16_9QTBS and near the active dELS EH38E3180851, making an enhancer mechanism plausible but not cCRE-confirmed at the variant base. | weak | [E01](#e01), [E03](#e03) |
| gene | TOX3 is proposed as the target because it is the closest protein-coding gene at 17.6 kb upstream, with CASC16 also present; there is no breast eQTL and no demonstrated enhancer-promoter interaction. | weak | [E02](#e02), [E03](#e03), [E19](#e19) |
| cell_type | MCF7 expresses PBX1 at 53.19 TPM in the ACH-000019 expression context, so PBX1 is present in the relevant breast cancer cell line. | supported | [E07](#e07), [E14](#e14) |
| phenotype | TOX3 is a known breast cancer locus, so alt-enhanced PBX1 binding could increase TOX3 and contribute to 16q12 risk, but rs56007086 itself has no GWAS or Open Targets record and no breast eQTL. | weak | [E06a](#e06a), [E06b](#e06b), [E04](#e04), [E05](#e05), [E19](#e19) |

Predictions: PBX1 ChIP-qPCR or allelic imbalance assays show stronger PBX1 binding to the alt allele.; Mutation of the homeodomain motif reduces the allele-specific enhancer activity.; PBX1 knockdown lowers TOX3 expression in MCF7.

Falsified if: PBX1 does not occupy the element in breast cancer cells.; The homeodomain motif is dispensable for the allele effect.; PBX1 knockdown does not change TOX3 expression.

### 4. ZNF395: Alt allele weakens ZNF395 binding and may derepress TOX3 (p = 0.12)

TF ZNF395 (stated coverage own_model; registry own_model), ref allele binds more; element ENSR16_9QTBS enhancer / nearby dELS EH38E3180851; gene TOX3; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF395 has its own QBiC-SELEX model in group G504 and binds the ref allele more strongly: z -53.42 with effect -0.776, meaning alt binds less. This is the strongest QBiC group shown, but ZNF395 is expressed at only 4.59 TPM in MCF7, so cellular relevance is weak. | weak | [E08](#e08) |
| element | The variant lies in the VEP-predicted ENSR16_9QTBS enhancer and 38 bp from an active dELS; no ENCODE cCRE directly overlaps the variant, so the element call is inferred. | weak | [E01](#e01), [E03](#e03) |
| gene | The element is proposed to regulate TOX3 by proximity at 17.6 kb upstream, with CASC16 at the locus; there is no breast eQTL for the variant and no demonstrated ZNF395 regulation of TOX3. | weak | [E02](#e02), [E03](#e03), [E19](#e19) |
| cell_type | MCF7 is the expression context and expresses ZNF395 at 4.59 TPM, low but detectable; this limits confidence in a ZNF395-driven mechanism in this cell line. | supported | [E07](#e07), [E08](#e08) |
| phenotype | If ZNF395 represses TOX3, loss of ZNF395 binding on the alt allele could increase TOX3 and contribute to the 16q12 phenotype, but ZNF395 repressor activity on TOX3 is unproven and rs56007086 has no variant-specific association or breast eQTL. | weak | [E06a](#e06a), [E06b](#e06b), [E04](#e04), [E05](#e05), [E19](#e19) |

Predictions: ZNF395 ChIP-qPCR shows stronger binding to the ref allele at this element.; If ZNF395 is a repressor, the alt allele increases TOX3 expression and ZNF395 knockdown increases TOX3.; The allele effect depends on the ZNF395 motif.

Falsified if: ZNF395 does not bind the element in breast cancer cells.; ZNF395 knockdown does not change TOX3 expression.; The alt allele decreases rather than increases TOX3, or ZNF395 acts as an activator rather than a repressor.

### 5. ELF1: Alt allele strengthens ELF1 binding at a TOX3 enhancer (p = 0.09)

TF ELF1 (stated coverage own_model; registry own_model), alt allele binds more; element ENSR16_9QTBS enhancer / nearby dELS EH38E3180851; gene TOX3; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ELF1 has its own QBiC-SELEX model and is a passing member of ETS group G003 with positive alt effect z 4.97, meaning alt binds more. This is weak because the leading ETV5 model has the opposite sign and ETS group members disagree on direction; ELF1 is chosen because it is a high-expression passing ETS member in MCF7. | weak | [E09](#e09) |
| element | The variant is in the VEP-predicted ENSR16_9QTBS enhancer and close to an active dELS, though no ENCODE cCRE directly overlaps the variant base. | weak | [E01](#e01), [E03](#e03) |
| gene | TOX3 is proposed by proximity at 17.6 kb upstream, with CASC16 also in the immediate locus; there is no breast-tissue eQTL for the variant and no direct enhancer-to-TOX3 evidence. | weak | [E02](#e02), [E03](#e03), [E19](#e19) |
| cell_type | MCF7 is the expression context and expresses ELF1 at 57.44 TPM, supporting ELF1 as a candidate ETS factor in this breast cancer line. | supported | [E07](#e07), [E09](#e09) |
| phenotype | TOX3 is repeatedly implicated in breast cancer, so an ELF1-driven increase in TOX3 could contribute to the 16q12 signal, but rs56007086 has no variant-specific association record and no breast eQTL. | weak | [E06a](#e06a), [E06b](#e06b), [E04](#e04), [E05](#e05), [E19](#e19) |

Predictions: ELF1 ChIP-qPCR shows stronger ELF1 binding to the alt allele at this element.; The alt allele increases TOX3 reporter activity through an ETS motif.; ELF1 knockdown reduces the alt-allele-dependent TOX3 signal.

Falsified if: ELF1 does not bind this element in breast cancer cells.; The ETS motif is not required for the allele effect.; ELF1 knockdown does not affect TOX3 expression from this locus.

## Prediction matrix

| Test | Cost | Separates top two | null | TFAP2C | PBX1 | ZNF395 | ELF1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TFAP2C ChIP-qPCR at rs56007086 in a heterozygous breast cancer line (e.g., MCF7 if heterozygous, otherwise a suitable heterozygous line) | medium | yes | No reproducible allelic imbalance in TFAP2C occupancy (alt approximately equals ref, or no TFAP2C occupancy at the element). | TFAP2C occupancy is higher on the alt allele than on the ref allele at this element. | No TFAP2C allelic imbalance; any allele effect in this assay is not attributable to TFAP2C. | No TFAP2C allelic imbalance, or if TFAP2C binds, it does not show the ZNF395 ref-preference pattern. | No TFAP2C allelic imbalance; any allele effect in this assay is not attributable to TFAP2C. |
| Allele-specific reporter assay of the ~200-500 bp element containing rs56007086 (ref vs alt) in MCF7, with and without mutation of the AP-2 motif | medium | yes | No reproducible alt-versus-ref difference in reporter activity. | The alt allele increases reporter activity; this increase is reduced or abolished when the AP-2 motif is mutated. | If an allele effect is seen, it depends on the homeodomain motif rather than the AP-2 motif. | If an allele effect is seen, the ref allele may give higher activity in a repression context, or the effect depends on the ZNF395 motif rather than the AP-2 motif. | If an allele effect is seen, it depends on the ETS motif rather than the AP-2 motif; AP-2 motif mutation does not abolish the alt effect. |
| TOX3 eQTL association for rs56007086 in breast mammary tissue (GTEx or a larger breast-tissue eQTL dataset) | low | no | No significant association between rs56007086 and TOX3 expression in breast tissue. | The alt allele is associated with higher TOX3 expression in breast tissue, consistent with stronger TFAP2C binding and activation. | The alt allele is associated with higher TOX3 expression, but this does not distinguish PBX1 from other activating TFs. | If ZNF395 is a repressor, the alt allele is associated with higher TOX3 expression; if not, no association or the opposite direction. | The alt allele is associated with higher TOX3 expression, but this does not distinguish ELF1 from other activating TFs. |
| TFAP2C knockdown or degradation in MCF7 followed by TOX3 expression measurement | medium | yes | TOX3 expression is unchanged by TFAP2C depletion, or any change is not allele-dependent at this locus. | TFAP2C depletion reduces TOX3 expression, consistent with TFAP2C acting as an activator at this element. | TFAP2C depletion does not reduce TOX3 expression; PBX1 depletion, not TFAP2C depletion, affects TOX3. | TFAP2C depletion does not reduce TOX3 expression; ZNF395 depletion may increase TOX3 if ZNF395 is a repressor. | TFAP2C depletion does not reduce TOX3 expression; ELF1 depletion, not TFAP2C depletion, affects TOX3. |

## Next experiment

The cheapest experiment that separates the top two chains is an allele-specific reporter assay of the rs56007086-containing element (ref vs alt) in MCF7, with and without mutation of the AP-2 motif. It is cheaper and faster than allele-specific ChIP and directly tests whether the alt allele increases enhancer activity through the TFAP2C/AP-2 motif: the null predicts no alt-versus-ref difference, whereas the TFAP2C chain predicts an alt-dependent increase that is abolished by AP-2 motif mutation.

## Investigate calls

- chip_peaks({"biosample": "MCF7", "tf": "TFAP2C"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})

## Flags

- literature_fallback: no hits for 'rs56007086 AND TOX3 AND "breast cancer"'; dropped the rsID

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:52565398-52565398:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:25:34+00:00)

> Variant chr16:52565398:G>A (GRCh38), allele string G/A
> Known IDs: rs56007086
> Most severe consequence: intron_variant
> Regulatory features: ENSR16_9QTBS enhancer
> GERP conservation score at the site: -4.73
> Transcript consequences: CASC16 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:51565398-53565398?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:25:46+00:00)

> 6 protein-coding genes within 1000 kb of chr16:52565398:G>A, by distance to TSS:
> TOX3: 17.6 kb from TSS (upstream, strand -1)
> CHD9NB: 487.5 kb from TSS (downstream, strand -1)
> CHD9: 489.6 kb from TSS (upstream, strand +1)
> RBL2: 868.6 kb from TSS (upstream, strand +1)
> AKTIP: 939.0 kb from TSS (downstream, strand -1)
> HNRNPA1L3: 1012.0 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:25:06+00:00)

> No cCRE overlaps the variant; nearest is EH38E3180851 (dELS) 38 bp away.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3180851 dELS: DNase z 4.2, H3K27ac z 6.1, H3K4me3 z 1.8, CTCF z 1.9; nearby genes CASC16, TOX3, AC026462.5
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs56007086&size=100; retrieved 2026-10-26T02:25:35+00:00)

> 0 GWAS Catalog associations for rs56007086, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:25:34+00:00)

> Open Targets has no record of 16_52565398_G_A.

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TOX3%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:25:47+00:00)

> Europe PMC: 586 hits for 'TOX3 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 41849381 (2026): A transcription regulator atlas identifies TOX3 as an Atoh1 coactivator in cerebellar development and tumorigenesis.
> PMID 41595182 (2026): Identification and Characterisation of Canine Osteosarcoma Biomarkers and Therapeutic Targets.
> PMID 41596432 (2026): Bone Metastasis in Estrogen Receptor-Positive Breast Cancer: Molecular Insights and Therapeutic Advances.
> PMID 40932605 (2025): Molecular signatures of breast cancer in the Iranian population: a review of cell growth and cell cycle regulators.
> PMID 42700350 (2026): Interactions between circular RNAs (circRNAs) and the Hippo pathway in cancer.
> PMID 41871294 (2026): A reanalysis of a genome-wide association study on breast cancer in Asian populations using the SG10K_Health reference panel for imputation: a multi-Centre case-control analysis.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-26T02:25:47+00:00)

> Key examples include promoter mutations [e.g., rs2279744 (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs4784227 (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 41871294 (https://europepmc.org/article/MED/41871294; retrieved 2026-10-26T02:25:47+00:00)

> Differences in panel performance influenced association signals, including breast cancer candidate loci such as FGFR2, TOX3, and ESR1.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:52565398:G>A: 997 models scored, 569 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 429 CIS-BP groups. Expression context: DepMap line ACH-000019. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 124 (C2H2 ZF, 1 model z -24.69, bHLH, 2 models z 20.32, C2H2 ZF, 1 model z 18.72, Homeodomain, 1 model z 18.7, Unknown, 1 model z 18.58). Passing groups ranked below the ones shown: 295. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G504 (C2H2 ZF, 1 model): best model ZNF395_FL_TG40NGACCTT_YWRA_jolma2025_0_1_7mer (own model of ZNF395), z -53.42, effect -0.776 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF395 z -53.42. TFs this group covers: ZNF395 (own model) 4.59 TPM; best model's site strength: ref 100.0th, alt 86.6th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z -47.67, effect -0.77 (alt binds less); 9 passing models (4 with the best model's sign); members disagree on direction. Passing members: ETV5 z -47.67, ETS1 z 9.91, ETV1 z 9.66, FEV z -9.06, ELF1 z 4.97 (+4 more). TFs this group covers: SPDEF (own model) 72.51 TPM, ELF1 (own model) 57.44 TPM, ELF3 (own model) 48.08 TPM, ERF (own model) 35.09 TPM, ETS2 (own model) 24.52 TPM, ELF2 (own model) 19.07 TPM, ELK1 (own model) 16.67 TPM, ELK4 (own model) 14.05 TPM, ELF4 (own model) 12.15 TPM, GABPA (own model) 8.21 TPM (+15 more); best model's site strength: ref 95.8th, alt 86.8th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G332 (C2H2 ZF, 1 model): best model SLC2A4RG_FL_CT40NGCGCTA_YWPA_jolma2025_0_3_7mer (own model of SLC2A4RG), z -45.42, effect -4.513 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: SLC2A4RG z -45.42. TFs this group covers: SLC2A4RG (own model) 148.81 TPM; best model's site strength: ref 99.9th, alt 93.5th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G245 (mTERF, 1 model): best model MTERF3_FL_GG40NTAGTTT_YWJA_jolma2025_0_3_7mer (own model of MTERF3), z 24.43, effect 0.234 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: MTERF3 z 24.43. TFs this group covers: MTERF3 (own model) 19.0 TPM; best model's site strength: ref 71.0th, alt 83.4th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G100 (bHLH, 2 models): best model SREBF1_eDBD_TCTCCT40NCCT_KT_yin2017_0_3_7mer (own model of SREBF1), z 24.29, effect 0.415 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SREBF1 z 24.29. TFs this group covers: SREBF1 (own model) 211.24 TPM, SREBF2 (own model) 39.91 TPM; best model's site strength: ref 95.9th, alt 97.3th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G513 (C2H2 ZF, 1 model): best model ZNF449_eDBD_TGCGAG40NTTC_KT_yin2017_0_3_7mer (own model of ZNF449), z 22.52, effect 0.807 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF449 z 22.52. TFs this group covers: ZNF449 (own model) 3.48 TPM; best model's site strength: ref 62.6th, alt 99.7th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G274 (Homeodomain, 1 model): best model PBX1_eDBD_TAAGTC40NCGT_KR_yin2017_0_4_7mer (own model of PBX1), z 18.55, effect 0.733 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: PBX1 z 18.55. TFs this group covers: PBX1 (own model) 53.19 TPM, PBX2 (mapped) 39.0 TPM, PBX3 (mapped) 10.37 TPM, PBX4 (mapped) 3.15 TPM; best model's site strength: ref 75.2th, alt 97.8th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G005 (HMG/Sox, 18 models): best model SOX18_eDBD_TCACGC40NACT_KP_yin2017_0_4_7mer (own model of SOX18), z 17.9, effect 0.672 (alt binds more); 8 passing models (7 with the best model's sign); members disagree on direction. Passing members: SOX18 z 17.9, SOX15 z 11.03, SOX14 z 8.6, SOX5 z 7.75, SOX10 z 6.66 (+3 more). TFs this group covers: SOX13 (mapped) 19.82 TPM, SOX4 (own model) 16.17 TPM, SOX12 (own model) 9.17 TPM, SOX3 (own model) 3.69 TPM, SOX2 (own model) 1.44 TPM, SOX15 (own model) 0.82 TPM, SOX9 (own model) 0.73 TPM, SOX11 (own model) 0.7 TPM, SOX18 (own model) 0.43 TPM, SOX10 (own model) 0.11 TPM (+10 more); best model's site strength: ref 74.4th, alt 82.6th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G566 (C2H2 ZF, 1 model): best model ZNF684_FL_TACCGG40NAGT_KAF_yin2017_0_3_7mer (own model of ZNF684), z 17.79, effect 0.453 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF684 z 17.79. TFs this group covers: ZNF684 (own model) 2.71 TPM; best model's site strength: ref 48.0th, alt 97.7th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (own model of TFAP2E), z 17.67, effect 0.779 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: TFAP2E z 17.67, TFAP2B z 14.95, TFAP2C z 10.07, TFAP2A z 7.74. TFs this group covers: TFAP2C (own model) 44.3 TPM, TFAP2A (own model) 39.73 TPM, TFAP2E (own model) 0.36 TPM, TFAP2B (own model) 0.01 TPM, TFAP2D (mapped) 0.0 TPM; best model's site strength: ref 97.8th, alt 90.3th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:31:21+00:00)

> No ENCODE TFAP2C ChIP-seq peak contains chr16:52565398:G>A in biosamples matching 'MCF7'. Absence can also mean no TFAP2C experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565398_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:27:56+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565398_G_A_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (A) relative to ref (G).
