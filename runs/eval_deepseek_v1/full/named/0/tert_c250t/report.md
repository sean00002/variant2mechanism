# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 8 model calls; 140 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen

477 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 167.5); Ets, 4 models (best ELF3, z 114.84); Ets, 1 model (best SPDEF, z 78.05); MBD; CxxC ZF, 1 model (best MBD1, z -41.31); C2H2 ZF, 1 model (best ZNF654, z -35.62).

## Ranked chains

### 1. H1: GABPA/ETS gain-of-binding at the TERT promoter C250T allele (p = 0.60)

TF GABPA (stated coverage own_model; registry own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele strengthens GABPA binding: GABPA is an own-model ETS factor in QBiC group G003 with the group alt-more sign (z 71.32), GABPA ENCODE ChIP-seq peaks contain this site, and ETS factors are reported to bind mutant TERT promoters; GABPA was chosen over ETV5 because GABPA has ChIP evidence at this site while ETV5 does not. | weak | [E06](#e06), [E16](#e16), [E18a](#e18a) |
| element | The variant lies within the TERT promoter-like cCRE EH38E3622530 (PLS), a promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.0 kb from its TSS and upstream on the minus strand. | supported | [E01](#e01), [E02](#e02) |
| cell_type | GABPA is expressed in the glioblastoma DepMap subtype context at 15.52 TPM; the available GABPA ChIP peaks are from HepG2 and SK-N-SH, not glioblastoma. | supported | [E06](#e06), [E16](#e16) |
| phenotype | If GABPA binding at the alt allele raises TERT, this would fit the general association of TERT promoter mutations with telomerase activation in glioblastoma and melanoma; direct allele-specific TERT expression evidence is not provided. | weak | [E04a](#e04a), [E04d](#e04d), [E04g](#e04g), [E04h](#e04h), [E18a](#e18a) |

Predictions: Allele-specific GABPA ChIP-qPCR should show higher GABPA occupancy on the alt allele than on the ref allele in a C250T-heterozygous tumor cell line.; GABPA knockdown or CRISPR should reduce TERT expression preferentially in C250T-heterozygous glioblastoma/melanoma cells.; Mutating the ETS motif or blocking GABPA should reduce alt-allele-dependent TERT reporter activity.

Falsified if: Allele-specific GABPA ChIP or footprinting shows no difference between alt and ref at chr5:1295135 in relevant tumor cells.; GABPA knockdown/CRISPR in a C250T-heterozygous glioblastoma or melanoma line does not reduce TERT expression.

### 2. H4: No direct TF-mediated allelic effect (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: There should be no allele-specific TF binding at chr5:1295135 after controlling for linked variants.; TERT expression should not differ by this allele once linked causal variants in cis are accounted for.; The recurrent C250T observation should be explainable as a mutational hotspot/passenger marker or as a linked-variant signal rather than a direct TF-mediated effect.

Falsified if: Allele-specific GABPA/ETS occupancy at chr5:1295135 and allele-specific TERT expression persist after controlling for linked variants such as rs2853669 in cis.

### 3. H2: ETV5/ETS gain-of-binding at the TERT promoter C250T allele (p = 0.08)

TF ETV5 (stated coverage own_model; registry own_model), alt allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele binds ETV5 more strongly in QBiC-SELEX: ETV5 is the best own-model ETS model in group G003 (z 167.5, effect 2.421, alt more), but no ENCODE ETV5 ChIP-seq peak contains this site. | weak | [E06](#e06), [E17](#e17) |
| element | The variant lies within the TERT promoter-like cCRE EH38E3622530 (PLS). | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.0 kb from its TSS. | supported | [E01](#e01), [E02](#e02) |
| cell_type | ETV5 is expressed in the glioblastoma DepMap subtype context at 22.15 TPM. | supported | [E06](#e06) |
| phenotype | If ETV5 is the relevant ETS factor, the alt allele should increase TERT expression/telomerase activity, fitting the general TERT promoter mutation association; this is not directly tested here. | weak | [E04a](#e04a), [E04d](#e04d), [E04h](#e04h) |

Predictions: ETV5 ChIP-qPCR should show higher ETV5 occupancy on the alt allele than on the ref allele in relevant tumor cells.; ETV5 knockdown should reduce TERT expression preferentially in C250T-heterozygous cells.; The ETV5 motif model should outperform GABPA and other ETS models in allele-specific reporter assays.

Falsified if: ETV5 does not occupy this site allele-specifically in relevant tumor cells.; ETV5 perturbation does not affect TERT expression in C250T-heterozygous cells.

### 4. H3: MBD1 repressor-loss at the TERT promoter C250T allele (p = 0.02)

TF MBD1 (stated coverage own_model; registry own_model), ref allele binds more; element TERT promoter; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref G allele binds MBD1 more strongly than the alt A allele in QBiC-SELEX (MBD1 own model z -41.31, effect -1.236). | weak | [E09](#e09) |
| element | The variant lies within the TERT promoter-like cCRE EH38E3622530 (PLS). | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.0 kb from its TSS. | supported | [E01](#e01), [E02](#e02) |
| cell_type | MBD1 is expressed in the glioblastoma DepMap subtype context at 31.48 TPM. | supported | [E09](#e09) |
| phenotype | If MBD1 represses TERT, loss of MBD1 binding on the alt allele would de-repress TERT; no cited evidence establishes MBD1 occupancy at TERT or MBD1-dependent TERT repression. | missing | none |

Predictions: MBD1 ChIP-qPCR should show stronger MBD1 occupancy on the ref allele than on the alt allele.; MBD1 knockdown should increase TERT expression, mimicking the alt allele if MBD1 is a repressor.; The alt allele should increase TERT reporter activity through loss of MBD1 repression, not ETS activation.

Falsified if: MBD1 does not occupy this site or does not show stronger ref-allele binding.; MBD1 knockdown does not increase TERT expression, or MBD1 is not a TERT repressor.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR at chr5:1295135 in a C250T-heterozygous glioblastoma cell line | medium | yes | Higher GABPA occupancy on alt than ref allele. | No allele-specific GABPA occupancy. | No required GABPA allelic difference; ETV5 is the relevant factor if any. | No GABPA allelic difference. |
| Allele-specific ETV5 ChIP-qPCR at chr5:1295135 in glioblastoma cells | medium | no | No requirement for ETV5 allelic occupancy. | No allele-specific ETV5 occupancy. | Higher ETV5 occupancy on alt than ref allele. | No ETV5 allelic difference. |
| TERT promoter ref-vs-alt MPRA/reporter assay in glioblastoma cells with ETS-motif mutagenesis | medium | yes | Alt increases TERT reporter activity in an ETS/GABPA-dependent manner. | No allelic difference in TERT reporter activity after linked-variant control. | Alt increases TERT reporter activity, preferentially through ETV5 if that model is correct. | Alt increases TERT reporter activity through loss of MBD1 repression. |
| MBD1 ChIP-qPCR and MBD1 knockdown in C250T-heterozygous tumor cells | medium | no | No MBD1 allelic requirement. | No allele-specific MBD1 occupancy. | No MBD1 allelic requirement. | Ref allele shows stronger MBD1 occupancy; MBD1 knockdown increases TERT. |
| Allele-specific expression/eQTL or colocalization analysis controlling for rs2853669 in cis | low | yes | GABPA/ETS-dependent allelic effect remains after controlling rs2853669 in cis. | Signal is explained by linked variants such as rs2853669 in cis. | ETV5-dependent allelic effect remains after controlling rs2853669 in cis. | MBD1-dependent allelic effect remains after controlling rs2853669 in cis. |

## Next experiment

Allele-specific GABPA ChIP-qPCR at chr5:1295135 in a C250T-heterozygous glioblastoma cell line, comparing GABPA occupancy on the alt versus ref allele. This is the cheapest direct test separating H1 from H4: H1 predicts higher GABPA occupancy on the alt allele, while H4 predicts no allele-specific GABPA binding after linked-variant control.

## Investigate calls

- chip_peaks({"biosample": null, "tf": "GABPA"})
- chip_peaks({"biosample": null, "tf": "ETV5"})
- literature_search({"query": "GABPA ETS TERT promoter C250T mutation binding"})

## Flags

- none

Citation support: 0.93 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295135-1295135:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:00+00:00)

> Variant chr5:1295135:G>A (GRCh38), allele string G/A
> Known IDs: rs1561215364
> Most severe consequence: upstream_gene_variant
> Regulatory features: ENSR5_832QG promoter
> GERP conservation score at the site: -4.69
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295135-2295135?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:54+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295135:G>A, by distance to TSS:
> TERT: 0.0 kb from TSS (upstream, strand -1)
> CLPTM1L: 50.0 kb from TSS (downstream, strand -1)
> SLC6A18: 69.8 kb from TSS (downstream, strand +1)
> SLC6A19: 93.5 kb from TSS (downstream, strand +1)
> SLC12A7: 138.9 kb from TSS (upstream, strand -1)
> SLC6A3: 150.4 kb from TSS (downstream, strand -1)
> LPCAT1: 229.1 kb from TSS (downstream, strand -1)
> NKD2: 287.1 kb from TSS (downstream, strand +1)
> TRIP13: 402.3 kb from TSS (downstream, strand +1)
> BRD9: 402.3 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

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

> QBiC-SELEX screen of chr5:1295135:G>A: 997 models scored, 477 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 350 CIS-BP groups. Expression context: DepMap subtype median Glioblastoma. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 77 (C2H2 ZF, 1 model z -27.15, C2H2 ZF, 1 model z -21.76, bHLH, 1 model z -21.51, Homeodomain, 1 model z -19.2, Myb/SANT, 1 model z -18.88). Passing groups ranked below the ones shown: 263. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e06"></a>**E06** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 167.5, effect 2.421 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: ETV5 z 167.5, ELF1 z 164.23, ELF4 z 110.16, GABPA z 71.32, ELK4 z 62.15 (+13 more). TFs this group covers: ETS1 (own model) 61.01 TPM, ERF (own model) 39.81 TPM, ELK3 (own model) 30.24 TPM, ELK1 (own model) 26.81 TPM, ETV5 (own model) 22.15 TPM, ETS2 (own model) 21.07 TPM, ELF2 (own model) 18.42 TPM, ELF1 (own model) 17.41 TPM, GABPA (own model) 15.52 TPM, ELF4 (own model) 15.44 TPM (+15 more); best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G020 (Ets, 4 models): best model ELF3_NA_TCCGTG20NTGC_ESY_yang2017_0_4_7mer (own model of ELF3), z 114.84, effect 5.168 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: ELF3 z 114.84, ELF5 z 107.44, ETV7 z 49.98, ETV6 z 46.24. TFs this group covers: ERF (own model) 39.81 TPM, ELF2 (own model) 18.42 TPM, ELF1 (own model) 17.41 TPM, ELF4 (own model) 15.44 TPM, ETV6 (own model) 5.65 TPM, ELF3 (own model) 0.47 TPM, ETV7 (own model) 0.31 TPM, EHF (mapped) 0.17 TPM, SPI1 (own model) 0.05 TPM, ELF5 (own model) 0.03 TPM (+1 more); best model's site strength: ref 99.3th, alt 100.0th percentile of its k-mer coefficients.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G345 (Ets, 1 model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (own model of SPDEF), z 78.05, effect 2.184 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SPDEF z 78.05. TFs this group covers: ELF2 (own model) 18.42 TPM, ELF1 (own model) 17.41 TPM, ELF4 (own model) 15.44 TPM, SPDEF (own model) 0.05 TPM; best model's site strength: ref 99.2th, alt 100.0th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G229 (MBD; CxxC ZF, 1 model): best model MBD1_FL_TG40NTGATCT_YWQA_jolma2025_0_3_7mer (own model of MBD1), z -41.31, effect -1.236 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: MBD1 z -41.31. TFs this group covers: MBD1 (own model) 31.48 TPM; best model's site strength: ref 100.0th, alt 98.6th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G557 (C2H2 ZF, 1 model): best model ZNF654_DBD_AG40NTGGCTA_YWIA_jolma2025_0_4_7mer (own model of ZNF654), z -35.62, effect -0.857 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF654 z -35.62. TFs this group covers: ZNF654 (own model) 6.42 TPM; best model's site strength: ref 100.0th, alt 99.1th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G620 (C2H2 ZF, 1 model): best model ZNF92_FL_TC40NAATCTC_YWIA_jolma2025_0_3_7mer (own model of ZNF92), z -33.21, effect -0.623 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF92 z -33.21. TFs this group covers: ZNF92 (own model) 9.63 TPM; best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G409 (C2H2 ZF, 1 model): best model ZBTB5_FL_GA40NACTTTG_YWQA_jolma2025_0_2_7mer (own model of ZBTB5), z -24.38, effect -0.68 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB5 z -24.38. TFs this group covers: ZBTB5 (own model) 7.43 TPM; best model's site strength: ref 100.0th, alt 99.5th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G066 (EBF1, 2 models): best model EBF1_NA_TATAAG20NCG_AC_jolma2013_1_3_7mer (own model of EBF1), z -24.35, effect -0.646 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: EBF1 z -24.35. TFs this group covers: EBF1 (own model) 3.13 TPM, EBF4 (own model) 2.58 TPM, EBF2 (mapped) 0.02 TPM, EBF3 (mapped) 0.01 TPM; best model's site strength: ref 99.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G612 (C2H2 ZF, 1 model): best model ZNF845_DBD2_GC40NAGAGTT_YWIA_jolma2025_0_3_7mer (own model of ZNF845), z -24.25, effect -0.358 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF845 z -24.25. TFs this group covers: ZNF845 (own model) 3.41 TPM; best model's site strength: ref 100.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G575 (C2H2 ZF, 1 model): best model ZNF706_FL_CT40NTCTAGT_YWSA_jolma2025_0_3_7mer (own model of ZNF706), z -23.53, effect -0.618 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF706 z -23.53. TFs this group covers: ZNF706 (own model) 81.43 TPM; best model's site strength: ref 100.0th, alt 99.4th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295135:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:38:43+00:00)

> No ENCODE ETV5 ChIP-seq peak contains chr5:1295135:G>A. Absence can also mean no ETV5 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABPA%20ETS%20TERT%20promoter%20C250T%20mutation%20binding&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:38:44+00:00)

> Europe PMC: 66 hits for 'GABPA ETS TERT promoter C250T mutation binding'; top 8 with PMIDs:
> PMID 39183149 (2025): BRAF-induced EHF Expression Affects TERT in Aggressive Papillary Thyroid Cancer.
> PMID 41878440 (2026): Effect of co-occurring mutations in &lt;i&gt;TP53&lt;/i&gt; gene and &lt;i&gt;TERT&lt;/i&gt; promoter on the survival of bladder cancer patients.
> PMID 39557834 (2024): Mechanistic basis of atypical TERT promoter mutations.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 40241101 (2025): The ability of anexelekto (AXL) expression and TERT promoter mutation to predict radioiodine-refractory differentiated thyroid carcinoma.
> PMID 37741952 (2023): Pooled genetic screens to identify vulnerabilities in TERT-promoter-mutant glioblastoma.
> PMID 36713366 (2022): <i>TERT</i> promoter mutations and methylation for telomerase activation in urothelial carcinomas: New mechanistic insights and clinical significance.
> PMID 38735658 (2024): Coexisting RET/PTC and TERT Promoter Mutation Predict Poor Prognosis but Effective RET and MEK Targeting in Thyroid Cancer.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 39183149 (https://europepmc.org/article/MED/39183149; retrieved 2026-10-26T00:38:44+00:00)

> This effect is believed to arise from MAPK activation triggered by BRAFV600E, leading to the upregulation of ETS transcription factors that bind to the mutant TERT promoter.
