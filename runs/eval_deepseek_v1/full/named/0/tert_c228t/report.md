# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 176 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen

310 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 166.19); Ets, 4 models (best ELF3, z 70.12); Ets, 1 model (best SPDEF, z 47.58); AP-2, 4 models (best TFAP2E, z -36.84); C2H2 ZF, 1 model (best ZNF582, z 22.77).

## Ranked chains

### 1. H1_GABPA: GABPA binds the alt allele more strongly and promotes TERT expression (p = 0.62)

TF GABPA (stated coverage own_model; registry own_model), alt allele binds more; element Promoter-like cCRE EH38E3622530 containing the variant; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA has its own QBiC-SELEX model and is a passing member in the ETS group with alt-more binding (z 68.47, effect 4.01 alt more; group G003 passing models have the alt-more sign). GABPA is chosen over other ETS factors because E18b directly reports that the C228T mutation recruited GA-binding protein and engendered low-level TERT expression; E17 adds that GABPA ChIP peaks contain this variant in HepG2 and SK-N-SH, though no glioblastoma GABPA peak is reported and absence there is ambiguous. | supported | [E16](#e16), [E06](#e06), [E18b](#e18b), [E17](#e17) |
| element | The variant lies in promoter-like cCRE EH38E3622530 at the TERT promoter. | supported | [E03](#e03), [E01](#e01) |
| gene | TERT is the nearest protein-coding gene, 0.0 kb from its TSS, and the variant is annotated as an upstream TERT promoter variant. | supported | [E02](#e02), [E01](#e01) |
| cell_type | The relevant expression context is glioblastoma, and TERT promoter mutations are common in IDH-wildtype glioblastoma. | supported | [E05](#e05), [E04d](#e04d), [E04g](#e04g), [E04h](#e04h) |
| phenotype | E18b directly supports that the C228T mutation recruits GABP and engenders low-level TERT expression, consistent with a GABPA-mediated increase in TERT/telomerase in tumors; E18a and E04a support TERT promoter mutations as a cause of TERT activation. E18d cautions that pooled screens did not detect a TERT or ETS-factor dependency, so the functional magnitude and necessity of GABPA remain uncertain. | supported | [E18b](#e18b), [E18a](#e18a), [E04a](#e04a), [E18d](#e18d) |

Predictions: GABPA ChIP is stronger on the alt allele at chr5:1295113 in heterozygous glioblastoma cells.; Allele-resolved TERT expression is higher from the alt allele.; GABPA depletion reduces TERT expression preferentially in alt-allele glioblastoma cells.

Falsified if: Allele-specific GABPA ChIP does not show alt > ref at this promoter in a relevant cell type.; GABPA depletion does not reduce TERT expression in glioblastoma cells carrying the alt allele.; Allele-resolved TERT expression does not show the alt allele higher in heterozygous glioblastoma cells.

### 2. H4_null: No TF-mediated allelic effect; linked or passenger explanation (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at chr5:1295113 after controlling for linked variants.; TERT expression is not allele-specific at this base.; The disease association is explained by another linked variant, a passenger event at a mutational hotspot, or no allelic effect.

Falsified if: Allele-specific GABPA or ETS ChIP shows a reproducible alt > ref difference at this exact base in a relevant cell type.; Allele-resolved TERT expression shows the alt allele is expressed higher in the relevant cell context.; A linked causal variant is excluded and the base itself changes TF binding and TERT expression.

### 3. H2_ETS1: ETS1 binds the alt allele more strongly and activates TERT (p = 0.08)

TF ETS1 (stated coverage own_model; registry own_model), alt allele binds more; element Promoter-like cCRE EH38E3622530 containing the variant; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETS1 is named as an own-model-covered ETS factor in E06 at 61.01 TPM in the glioblastoma expression context, but E06 does not explicitly enumerate ETS1 among the passing members or give an ETS1-specific z-score/effect sign. The alt-more direction is therefore extrapolated from the group G003 alt-more sign and remains weak until ETS1-specific QBiC-SELEX detail is checked. | weak | [E06](#e06) |
| element | The variant lies in promoter-like cCRE EH38E3622530 at the TERT promoter. | supported | [E03](#e03), [E01](#e01) |
| gene | TERT is the nearest protein-coding gene, 0.0 kb from its TSS, and the variant is annotated as an upstream TERT promoter variant. | supported | [E02](#e02), [E01](#e01) |
| cell_type | The relevant expression context is glioblastoma, and TERT promoter mutations are common in IDH-wildtype glioblastoma. | supported | [E05](#e05), [E04d](#e04d), [E04g](#e04g), [E04h](#e04h) |
| phenotype | If ETS1 were the functional ETS factor, stronger alt-allele binding would increase TERT expression. However, E18d explicitly reports that pooled screens did not detect dependency on an ETS factor known to activate TPMs, so this chain is disfavored relative to GABPA. | missing | [E18d](#e18d) |

Predictions: ETS1-specific binding is stronger on the alt allele at chr5:1295113.; ETS1 depletion reduces TERT expression in glioblastoma cells carrying the alt allele.; The allele-specific effect is not explained by GABPA.

Falsified if: ETS1-specific QBiC-SELEX or allele-specific ETS1 ChIP does not show alt > ref at this base.; ETS1 knockdown does not affect TERT expression in the relevant glioblastoma context.; GABPA accounts for all allele-specific ETS-family binding at this promoter.

### 4. H3_TFAP2A: TFAP2A binds the ref allele more strongly and may repress TERT (p = 0.05)

TF TFAP2A (stated coverage own_model; registry own_model), ref allele binds more; element Promoter-like cCRE EH38E3622530 containing the variant; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A has its own QBiC-SELEX model in the AP-2 group and is a passing member with z -28.06; the group's passing models have the alt-less sign, so TFAP2A is predicted to bind the ref allele more strongly. This is an in vitro binding prediction only. | weak | [E09](#e09) |
| element | The variant lies in promoter-like cCRE EH38E3622530 at the TERT promoter. | supported | [E03](#e03), [E01](#e01) |
| gene | TERT is the nearest protein-coding gene, 0.0 kb from its TSS, and the variant is annotated as an upstream TERT promoter variant. | supported | [E02](#e02), [E01](#e01) |
| cell_type | The relevant expression context is glioblastoma, and TERT promoter mutations are common in IDH-wildtype glioblastoma. | supported | [E05](#e05), [E04d](#e04d), [E04g](#e04g), [E04h](#e04h) |
| phenotype | No supplied evidence shows that TFAP2A represses TERT. If TFAP2A were a repressor, loss of its ref-allele binding on the alt allele would derepress TERT and increase telomerase activity, but this remains speculative. | missing | none |

Predictions: TFAP2A ChIP is stronger on the ref allele at chr5:1295113.; TFAP2A depletion increases TERT expression in the relevant cells.; The alt allele increases TERT expression by losing a repressive AP-2 site.

Falsified if: TFAP2A ChIP does not show ref > alt at this promoter.; TFAP2A is not a repressor of TERT in the relevant cell context.; Loss of TFAP2A binding on the alt allele does not increase TERT expression.

## Prediction matrix

| Test | Cost | Separates top two | H1_GABPA | H4_null | H2_ETS1 | H3_TFAP2A |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR at chr5:1295113 in heterozygous TERT promoter-mutant glioblastoma cells | medium | yes | GABPA ChIP is stronger on the alt allele than the ref allele at chr5:1295113. | No allele-specific TF binding at this base. | No GABPA allele-specific effect; ETS1 may instead show alt > ref. | No GABPA allele-specific effect; TFAP2A may show ref > alt. |
| Allele-resolved TERT expression by RNA-seq or RT-PCR in glioblastoma cells heterozygous for C228T | low | yes | TERT RNA is expressed more from the alt allele than the ref allele. | No allele-specific TERT expression at this base. | TERT RNA is expressed more from the alt allele if ETS1 is functional. | TERT RNA is expressed more from the alt allele if TFAP2A represses TERT. |
| GABPA knockdown in alt-allele glioblastoma cells followed by TERT mRNA and telomerase activity measurement | medium | yes | GABPA knockdown reduces TERT mRNA and telomerase activity. | GABPA knockdown does not change TERT expression. | GABPA knockdown does not reduce TERT; ETS1 knockdown would be the relevant test. | GABPA knockdown does not reduce TERT; TFAP2A depletion may increase TERT. |
| Allele-specific TFAP2A ChIP at chr5:1295113 | medium | no | No TFAP2A allele-specific effect. | No TFAP2A allele-specific effect. | No TFAP2A allele-specific effect. | TFAP2A ChIP is stronger on the ref allele. |
| TERT promoter reporter assay with ref vs alt C228T in glioblastoma cells, with GABPA overexpression or knockdown | medium | yes | The alt reporter is stronger and the effect is GABPA-dependent. | No ref-vs-alt reporter difference. | The alt reporter may be stronger but not GABPA-dependent; ETS1-dependent. | The ref reporter is repressed and the alt derepressed in a TFAP2A-dependent way. |
| Query public ENCODE GABPA ChIP-seq in glioblastoma biosamples at this element | low | no | A GABPA peak is present at the element if a glioblastoma GABPA experiment exists. | No GABPA peak expected. | No GABPA peak expected. | No GABPA peak expected. |

## Next experiment

Allele-resolved TERT expression by RNA-seq or RT-PCR in glioblastoma cells heterozygous for C228T, using phased heterozygous SNPs to assign TERT reads to ref versus alt alleles. It is the cheapest because it uses RNA rather than ChIP or perturbation and directly separates H1_GABPA from H4_null: H1 predicts higher TERT expression from the alt allele, whereas H4 predicts no allelic difference. It does not by itself prove GABPA, so a positive result would then require allele-specific GABPA ChIP.

## Investigate calls

- qbic_tf_detail({"tf": "GABPA"})
- chip_peaks({"biosample": "glioblastoma", "tf": "GABPA"})
- literature_search({"query": "GABPA TERT promoter mutation C228T binding glioblastoma telomerase"})

## Flags

- none

Citation support: 0.93 of links cite only evidence that passed every check.

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

<a id="e04a"></a>**E04a** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> A major molecular feature of melanoma is abnormal telomerase activation; this is most often caused by telomerase reverse transcriptase (TERT) promoter mutations, which occur in 50-82% of cases and are the most common noncoding alteration in this cancer.

<a id="e04b"></a>**E04b** literature_search, Europe PMC abstract, PMID 41744838 (https://europepmc.org/article/MED/41744838; retrieved 2026-10-25T11:57:36+00:00)

> Understanding both telomere-dependent and -independent TERT functions is essential for developing effective biomarkers and therapies that overcome resistance and slow melanoma progression.

<a id="e04c"></a>**E04c** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e04d"></a>**E04d** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> Mutations in the telomerase reverse transcriptase (TERT) promoter region (TPM), particularly C228T and C250T, are common in IDH-wildtype glioblastoma (GBM).

<a id="e04e"></a>**E04e** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> The rs2853669 C allele may increase GBM susceptibility and, when in cis with TPM, is associated with reduced TERT expression and poorer prognosis, underscoring its biological and clinical significance in TPM-mutant GBM.

<a id="e04f"></a>**E04f** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e04g"></a>**E04g** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

<a id="e04h"></a>**E04h** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> Among 112 patients, 70 (62.5%) harbored TERTp mutations.

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

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABPA%20TERT%20promoter%20mutation%20C228T%20binding%20glioblastoma%20telomerase&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:38:42+00:00)

> Europe PMC: 50 hits for 'GABPA TERT promoter mutation C228T binding glioblastoma telomerase'; top 8 with PMIDs:
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 37741952 (2023): Pooled genetic screens to identify vulnerabilities in TERT-promoter-mutant glioblastoma.
> PMID 41303422 (2025): Telomere Maintenance and Oncogenesis.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 36713366 (2022): <i>TERT</i> promoter mutations and methylation for telomerase activation in urothelial carcinomas: New mechanistic insights and clinical significance.
> PMID 40272676 (2025): TERT Amplification a Risk Stratification Marker in Papillary Thyroid Carcinoma, Significantly Correlated with Tumor Recurrence and Survival.
> PMID 35325218 (2022): TERT promoter C228T mutation in neural progenitors confers growth advantage following telomere shortening in vivo.
> PMID 39239547 (2024): Telomeres and telomerase in Sarcoma disease and therapy.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 35325218 (https://europepmc.org/article/MED/35325218; retrieved 2026-10-26T00:38:42+00:00)

> Heterozygous TERT (telomerase reverse transcriptase) promoter mutations (TPMs) facilitate TERT expression and are the most frequent mutation in glioblastoma (GBM).

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 35325218 (https://europepmc.org/article/MED/35325218; retrieved 2026-10-26T00:38:42+00:00)

> However, the mutation recruited GA-Binding Protein and engendered low-level TERT expression resulting in enhanced tumorigenesis and maintenance of short telomeres upon secondary passage as observed in human GBM.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 37741952 (https://europepmc.org/article/MED/37741952; retrieved 2026-10-26T00:38:42+00:00)

> Here we used pooled CRISPR/Cas9-based approaches to identify vulnerabilities associated with telomerase reverse transcriptase (TERT) promoter mutations (TPMs) found in >80% of glioblastomas.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 37741952 (https://europepmc.org/article/MED/37741952; retrieved 2026-10-26T00:38:42+00:00)

> However, we could not detect dependencies on either TERT itself or on an E-twenty six transcription (ETS) factor known to activate TPMs.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T00:38:42+00:00)

> Point mutations in the core promoter region of the telomerase reverse transcriptase (TERT) gene have been found to occur at high frequencies in several tumour types and considered a primary cause of telomerase reactivation in cancer cells.

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T00:38:42+00:00)

> These mutations promote TERT gene expression by multiple mechanisms, including the generation of novel binding sites for nuclear transcription factors, displacement of negative regulators from DNA G-quadruplexes, recruitment of epigenetic activators and disruption of long-range interactions between TERT locus and telomeres.
