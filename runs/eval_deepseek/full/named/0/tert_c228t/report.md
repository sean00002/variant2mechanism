# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 127 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen

310 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 166.19); Ets, 4 models (best ELF3, z 70.12); Ets, 1 model (best SPDEF, z 47.58); AP-2, 4 models (best TFAP2E, z -36.84); C2H2 ZF, 1 model (best ZNF582, z 22.77).

## Ranked chains

### 1. H1: GABPA binds the alt allele more strongly and activates TERT (p = 0.50)

TF GABPA (stated coverage own_model; registry own_model), alt allele binds more; element TERT promoter PLS EH38E3622530; gene TERT; cell type Glioblastoma expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA has its own QBiC-SELEX model at this variant with predicted effect 4.01, meaning the alt A allele binds GABPA more strongly than the ref G allele; E16 is a GABPA-specific own-model lookup, not only a group-level Ets signal. GABPA is also an own-model passing member of Ets group G003 in E06, and I choose GABPA as the Ets factor because it has a GABPA-specific own-model prediction and is expressed in the glioblastoma context. | weak | [E16](#e16), [E06](#e06) |
| element | The variant lies in the TERT promoter PLS EH38E3622530, a promoter-like cCRE annotated at the TERT upstream promoter, so an allele-specific Ets-site change would occur in a promoter regulatory element. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.0 kb from the TSS, and the variant is annotated as a TERT upstream_gene_variant, making TERT the direct candidate target gene. | supported | [E01](#e01), [E02](#e02) |
| cell_type | GABPA is expressed at 15.52 TPM in the DepMap glioblastoma subtype expression context used for the QBiC-SELEX screen. GABPA ChIP-seq peaks containing this variant exist in HepG2 and SK-N-SH, but not in glioblastoma, so glioblastoma occupancy at this element is not demonstrated; E03 cCRE z-scores are maxima over ENCODE biosamples and are not glioblastoma-specific. | weak | [E06](#e06), [E17](#e17), [E03](#e03) |
| phenotype | TERT and TERT promoter mutations are implicated in glioblastoma and melanoma in the cited literature, but E04 does not provide GABPA-specific functional evidence or bladder-cancer evidence. The disease mechanism is therefore a prediction, not an established GABPA-dependent phenotype. | weak | [E04](#e04) |

Predictions: Allele-specific GABPA ChIP-qPCR shows higher GABPA occupancy on the alt A allele than on the ref G allele at chr5:1295113 in a glioblastoma-relevant cell line.; A TERT promoter ref-vs-alt reporter assay shows higher alt-allele activity in glioblastoma cells.; GABPA knockdown or CRISPRi reduces the alt-allele-dependent increase in TERT reporter activity or allele-specific TERT expression.

Falsified if: Allele-specific GABPA occupancy at chr5:1295113 is not observed in glioblastoma-relevant cells.; The alt allele does not increase TERT promoter activity or endogenous TERT expression in a GABPA-dependent manner.; GABPA knockdown or Ets-site mutation does not reduce the alt-allele effect.

### 2. H0: No TF-mediated effect of this variant (p = 0.27)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding or TERT expression effect is attributable to this variant.; Any disease association is explained by a linked causal variant, a passenger event, or no functional allelic difference.

Falsified if: Allele-specific TF occupancy and allele-specific TERT expression are reproducibly demonstrated at this variant.; A linked variant is excluded and the single-base change alone alters TERT promoter activity in a TF-dependent manner.

### 3. H4: ETV5 binds the alt allele more strongly and activates TERT (p = 0.15)

TF ETV5 (stated coverage own_model; registry own_model), alt allele binds more; element TERT promoter PLS EH38E3622530; gene TERT; cell type Glioblastoma expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV5 is the best model in QBiC-SELEX Ets group G003, with own-model z 166.19 and predicted effect 2.121, meaning the alt A allele binds ETV5 more strongly than the ref G allele. I choose ETV5 within the Ets group because it is the group's best model and is expressed at 22.15 TPM in the glioblastoma context; no ETV5 ChIP-seq evidence at this site is provided. | weak | [E06](#e06) |
| element | The variant lies in the TERT promoter PLS EH38E3622530, so an allele-specific ETV5-site change would occur in a promoter regulatory element. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is 0.0 kb from the TSS and is the direct candidate target gene. | supported | [E01](#e01), [E02](#e02) |
| cell_type | ETV5 is expressed at 22.15 TPM in the DepMap glioblastoma subtype expression context, but no ETV5 ChIP-seq or perturbation data in glioblastoma are cited, so this is expression context only. | weak | [E06](#e06) |
| phenotype | TERT is implicated in glioblastoma and melanoma in the cited literature, but E04 does not provide ETV5-specific functional evidence or bladder-cancer evidence. The ETV5-dependent disease mechanism is therefore predicted, not shown. | weak | [E04](#e04) |

Predictions: Allele-specific ETV5 ChIP-qPCR shows higher ETV5 occupancy on the alt A allele than on the ref G allele.; ETV5 knockdown or CRISPRi reduces alt-allele-driven TERT reporter activity or allele-specific TERT expression.; GABPA knockdown does not reduce the alt-allele effect if ETV5 is the functional factor.

Falsified if: Allele-specific ETV5 occupancy is not higher on the alt allele at chr5:1295113.; ETV5 knockdown or CRISPRi does not reduce alt-allele-driven TERT expression or reporter activity.; The alt-allele effect is fully explained by GABPA or another factor.

### 4. H3: Loss of ref-allele TFAP2A binding on the alt allele derepresses TERT (p = 0.08)

TF TFAP2A (stated coverage own_model; registry own_model), ref allele binds more; element TERT promoter PLS EH38E3622530; gene TERT; cell type Glioblastoma expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A has its own passing QBiC-SELEX model in AP-2 group G030 with z -28.06 and negative effect, meaning the ref G allele binds TFAP2A/AP-2 models more strongly than the alt A allele. I choose TFAP2A within the AP-2 group because it has an own-model prediction and is expressed at 9.65 TPM, whereas TFAP2B is 0.0 TPM and TFAP2E is 0.49 TPM. | weak | [E09](#e09) |
| element | The variant lies in the TERT promoter PLS EH38E3622530, so loss of an AP-2 site on the alt allele would alter a promoter regulatory element. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is 0.0 kb from the TSS and is the direct candidate target gene. | supported | [E01](#e01), [E02](#e02) |
| cell_type | TFAP2A is expressed at 9.65 TPM in the DepMap glioblastoma subtype expression context, but no TFAP2A ChIP-seq peak contains this variant in glioblastoma and there are 0 TFAP2A peaks within 100 bp without containing it; glioblastoma occupancy is therefore not supported by the cited ChIP evidence. | weak | [E09](#e09), [E18](#e18) |
| phenotype | A repressive AP-2 site at the TERT promoter is not shown by any cited evidence. E04 links TERT to glioblastoma and melanoma generically but does not establish TFAP2A-mediated repression or derepression of TERT. The phenotype is therefore a hypothesis that requires direct repression evidence. | missing | [E04](#e04) |

Predictions: Allele-specific TFAP2A ChIP-qPCR shows higher TFAP2A occupancy on the ref G allele than on the alt A allele.; The alt allele reduces TFAP2A binding in an allele-specific reporter or MPRA assay.; TFAP2A knockdown or CRISPRi increases TERT expression if this AP-2 site is repressive.

Falsified if: TFAP2A occupancy is not higher on the ref G allele than on the alt A allele at chr5:1295113.; The alt allele does not reduce TFAP2A binding in an allele-specific assay.; TFAP2A knockdown does not increase TERT expression in glioblastoma-relevant cells, or TFAP2A does not repress this TERT promoter element.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H4 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR at chr5:1295113 in a glioblastoma-relevant cell line | medium | yes | Higher GABPA occupancy on alt A allele than ref G allele. | No allele-specific GABPA occupancy. | No GABPA allele-specific occupancy. | No GABPA allele-specific occupancy. |
| TERT promoter ref-vs-alt luciferase reporter assay in a glioblastoma cell line | low | yes | Alt A allele increases TERT promoter reporter activity. | No difference between ref G and alt A alleles. | Alt A allele increases TERT promoter reporter activity. | Alt A allele increases TERT promoter reporter activity if AP-2 is repressive. |
| GABPA knockdown or CRISPRi in glioblastoma cells with allele-specific TERT expression or ref-vs-alt reporter readout | medium | yes | GABPA knockdown reduces alt-allele-driven TERT expression/reporter activity. | No alt-allele effect to reduce. | GABPA knockdown does not reduce the alt-allele effect. | GABPA knockdown does not reduce the alt-allele effect. |
| Allele-specific ETV5 ChIP-qPCR at chr5:1295113 in glioblastoma-relevant cells | medium | no | No ETV5 allele-specific occupancy required. | No allele-specific ETV5 occupancy. | Higher ETV5 occupancy on alt A allele than ref G allele. | No ETV5 allele-specific occupancy. |
| Allele-specific TFAP2A ChIP-qPCR at chr5:1295113 in glioblastoma-relevant cells | medium | no | No TFAP2A ref-allele occupancy required. | No allele-specific TFAP2A occupancy. | No TFAP2A ref-allele occupancy required. | Higher TFAP2A occupancy on ref G allele than alt A allele. |
| TFAP2A knockdown or CRISPRi with TERT expression readout in glioblastoma-relevant cells | medium | no | TFAP2A knockdown does not increase TERT. | No TF-dependent TERT effect. | TFAP2A knockdown does not increase TERT. | TFAP2A knockdown increases TERT expression if the site is repressive. |
| ETV5 knockdown or CRISPRi with allele-specific TERT expression or ref-vs-alt reporter readout | medium | no | No ETV5 dependence. | No alt-allele effect to reduce. | ETV5 knockdown reduces alt-allele-driven TERT expression/reporter activity. | No ETV5 dependence. |

## Next experiment

TERT promoter ref-vs-alt luciferase reporter assay in a glioblastoma cell line. It is the cheapest test that separates the top two chains H1 and H0, because H1 predicts higher reporter activity from the alt A allele whereas H0 predicts no allelic difference.

## Investigate calls

- qbic_tf_detail({"tf": "GABPA"})
- chip_peaks({"biosample": "Glioblastoma", "tf": "GABPA"})
- chip_peaks({"biosample": "Glioblastoma", "tf": "TFAP2A"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295113-1295113:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T11:57:36+00:00)

> Variant chr5:1295113:G>A (GRCh38), allele string G/A
> Known IDs: rs1242535815
> Most severe consequence: upstream_gene_variant
> Regulatory features: ENSR5_832QG promoter
> GERP conservation score at the site: -7.45
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295113-2295113?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T11:57:33+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295113:G>A, by distance to TSS:
> TERT: 0.0 kb from TSS (upstream, strand -1)
> CLPTM1L: 50.0 kb from TSS (downstream, strand -1)
> SLC6A18: 69.7 kb from TSS (downstream, strand +1)
> SLC6A19: 93.5 kb from TSS (downstream, strand +1)
> SLC12A7: 138.9 kb from TSS (upstream, strand -1)
> SLC6A3: 150.4 kb from TSS (downstream, strand -1)
> LPCAT1: 229.2 kb from TSS (downstream, strand -1)
> NKD2: 287.1 kb from TSS (downstream, strand +1)
> TRIP13: 402.3 kb from TSS (downstream, strand +1)
> BRD9: 402.3 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T11:57:31+00:00)

> The variant lies in cCRE EH38E3622530 (PLS: promoter-like), chr5:1294945-1295294.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622530 PLS (contains the variant): DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622529 pELS: DNase z 3.7, H3K27ac z 4.1, H3K4me3 z 4.6, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e05"></a>**E05** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295113:G>A: 997 models scored, 310 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 230 CIS-BP groups. Expression context: DepMap subtype median Glioblastoma. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 47 (Ets, 3 models z 16.96, Myb/SANT, 1 model z -16.15, Homeodomain, 1 model z -15.52, bHLH, 1 model z -14.2, bHLH, 1 model z -14.2). Passing groups ranked below the ones shown: 173. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e06"></a>**E06** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 166.19, effect 2.121 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: ETV5 z 166.19, ELF1 z 124.32, ELF4 z 85.47, GABPA z 68.47, ELK4 z 56.2 (+13 more). TFs this group covers: ETS1 (own model) 61.01 TPM, ERF (own model) 39.81 TPM, ELK3 (own model) 30.24 TPM, ELK1 (own model) 26.81 TPM, ETV5 (own model) 22.15 TPM, ETS2 (own model) 21.07 TPM, ELF2 (own model) 18.42 TPM, ELF1 (own model) 17.41 TPM, GABPA (own model) 15.52 TPM, ELF4 (own model) 15.44 TPM (+15 more); best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G020 (Ets, 4 models): best model ELF3_NA_TCCGTG20NTGC_ESY_yang2017_0_4_7mer (own model of ELF3), z 70.12, effect 3.463 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: ELF3 z 70.12, ELF5 z 66.13, ETV6 z 46.32, ETV7 z 43.37. TFs this group covers: ERF (own model) 39.81 TPM, ELF2 (own model) 18.42 TPM, ELF1 (own model) 17.41 TPM, ELF4 (own model) 15.44 TPM, ETV6 (own model) 5.65 TPM, ELF3 (own model) 0.47 TPM, ETV7 (own model) 0.31 TPM, EHF (mapped) 0.17 TPM, SPI1 (own model) 0.05 TPM, ELF5 (own model) 0.03 TPM (+1 more); best model's site strength: ref 99.2th, alt 100.0th percentile of its k-mer coefficients.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G345 (Ets, 1 model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (own model of SPDEF), z 47.58, effect 1.511 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SPDEF z 47.58. TFs this group covers: ELF2 (own model) 18.42 TPM, ELF1 (own model) 17.41 TPM, ELF4 (own model) 15.44 TPM, SPDEF (own model) 0.05 TPM; best model's site strength: ref 98.5th, alt 99.9th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (own model of TFAP2E), z -36.84, effect -1.289 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TFAP2E z -36.84, TFAP2B z -30.5, TFAP2A z -28.06, TFAP2C z -24.32. TFs this group covers: TFAP2A (own model) 9.65 TPM, TFAP2C (own model) 6.49 TPM, TFAP2E (own model) 0.49 TPM, TFAP2B (own model) 0.0 TPM, TFAP2D (mapped) 0.0 TPM; best model's site strength: ref 99.5th, alt 96.5th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G541 (C2H2 ZF, 1 model): best model ZNF582_FL_CT40NCGGAGA_AATBA_jolma2025_0_3_7mer (own model of ZNF582), z 22.77, effect 0.322 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF582 z 22.77. TFs this group covers: ZNF582 (own model) 2.16 TPM; best model's site strength: ref 59.5th, alt 91.2th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G032 (C2H2 ZF, 4 models): best model ZIC4_eDBD_TGCGTA40NTCA_KT_yin2017_1_3_7mer (own model of ZIC4), z -20.85, effect -0.916 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: ZIC4 z -20.85, ZIC1 z -17.64, ZIC3 z -8.6. TFs this group covers: ZIC1 (own model) 13.23 TPM, ZIC2 (mapped) 3.7 TPM, ZIC4 (own model) 1.37 TPM, ZIC5 (own model) 0.53 TPM, ZIC3 (own model) 0.0 TPM; best model's site strength: ref 99.8th, alt 97.4th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G575 (C2H2 ZF, 1 model): best model ZNF706_FL_CT40NTCTAGT_YWSA_jolma2025_0_3_7mer (own model of ZNF706), z -19.9, effect -0.524 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF706 z -19.9. TFs this group covers: ZNF706 (own model) 81.43 TPM; best model's site strength: ref 99.9th, alt 99.4th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G245 (mTERF, 1 model): best model MTERF3_FL_GG40NTAGTTT_YWJA_jolma2025_0_3_7mer (own model of MTERF3), z 18.39, effect 0.175 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: MTERF3 z 18.39. TFs this group covers: MTERF3 (own model) 20.63 TPM; best model's site strength: ref 65.8th, alt 79.7th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G620 (C2H2 ZF, 1 model): best model ZNF92_FL_TC40NAATCTC_YWIA_jolma2025_0_3_7mer (own model of ZNF92), z -18.29, effect -0.342 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF92 z -18.29. TFs this group covers: ZNF92 (own model) 9.63 TPM; best model's site strength: ref 99.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G544 (C2H2 ZF, 1 model): best model ZNF596_FL_GA40NTGTATC_AATA_jolma2025_0_3_7mer (own model of ZNF596), z -18.26, effect -0.275 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF596 z -18.26. TFs this group covers: ZNF596 (own model) 3.59 TPM; best model's site strength: ref 100.0th, alt 99.5th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GABPA","symbol":"GABPA","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr5:1295113:G>A","gate_p":5.02e-05,"models":[{"model":"GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.658,"effect":4.01,"z":68.47,"p":0.0,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":99.8,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":2.514,"z":124.32,"p":0.0,"rank_abs_z":"2/997","passed_gate":true,"site_strength":{"ref_percentile":92.6,"alt_percentile":100.0,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":4.515,"z":35.9,"p":2.7e-282,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":97.8,"alt_percentile":100.0,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":3.97,"z":85.47,"p":0.0,"rank_abs_z":"3/997","passed_gate":true,"site_strength":{"ref_percentile":97.0,"alt_percentile":100.0,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":1.363,"z":12.45,"p":1.4e-35,"rank_abs_z":"63/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.4,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":2.56,"z":31.23,"p":4.6e-214,"rank_abs_z":"16/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":100.0,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":3.273,"z":56.2,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":92.2,"alt_percentile":99.6,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.63,"z":23.53,"p":2.2e-122,"rank_abs_z":"23/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.7,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":2.323,"z":22.12,"p":2e-108,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":1.97,"z":40.46,"p":0.0,"rank_abs_z":"12/997","passed_gate":true,"site_strength":{"ref_percentile":98.7,"alt_percentile":100.0,"k":7}}],"n_models_trimmed":8}

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:42:29+00:00)

> No ENCODE TFAP2A ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'Glioblastoma'. Absence can also mean no TFAP2A experiment in that biosample. 0 peaks lie within 100 bp without containing it.
