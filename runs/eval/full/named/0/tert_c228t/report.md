# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.63 over 8 model calls; 179 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen

310 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 166.19); Ets, 4 models (best ELF3, z 70.12); Ets, 1 model (best SPDEF, z 47.58); AP-2, 4 models (best TFAP2E, z -36.84); C2H2 ZF, 1 model (best ZNF582, z 22.77).

## Ranked chains

### 1. H1: C228T creates a de novo ETS site selectively used by the GABP complex (GABPA with GABPB1), activating TERT transcription (p = 0.72)

TF GABPA (stated coverage own_model; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells (also melanoma, bladder urothelium).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The G>A change creates a GGAA ETS core: the whole Ets group G003 predicts stronger alt binding (best model ETV5 z 166.19, effect +2.12; site strength ref 97.1th -> alt 99.3th percentile), and GABPA has its own QBiC-SELEX model in that group (z 68.47, 15.52 TPM in glioblastoma lines). The Ets group is one shared specificity, so I choose GABPA within it on two external lines of evidence rather than on the group z-scores: ENCODE ChIP-seq places GABPA peaks directly over this position in two biosamples (E16) while no ETS1 peak contains it (E17), and the literature reports that the GABP tetramer, not other ETS factors, is responsible for activation at TERTp mutations across 53 cell lines and 6 recurrent mutations (E18b, E18c, E18d). GABPB1 coverage was not shown by any screen row and is not claimed here. | supported | [E05](#e05), [E06](#e06), [E16](#e16), [E17](#e17), [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E18d](#e18d) |
| element | The variant lies in an ENCODE promoter-like cCRE (EH38E3622530) with high DNase, H3K4me3 and H3K27ac, i.e. the active TERT core promoter, and VEP annotates a promoter regulatory feature there. | supported | [E01](#e01), [E03](#e03) |
| gene | The affected promoter coincides with the TERT TSS (0.0 kb; CLPTM1L is 50 kb away), so TERT is the regulated gene; this rests on proximity plus the promoter annotation, not on eQTL or perturbation data. | weak | [E01](#e01), [E02](#e02), [E03](#e03) |
| cell_type | TERTp mutations are frequent in IDH-wildtype glioblastoma and in melanoma (50-82% of cases); GABPA is expressed in glioblastoma lines (15.52 TPM) and the GABP mechanism was shown across many cancer types. No cited evidence covers bladder specifically. | weak | [E04a](#e04a), [E04f](#e04f), [E06](#e06), [E18b](#e18b) |
| phenotype | Promoter activation by the recruited GABP complex raises TERT expression and reactivates telomerase, which supports continued proliferation; the cited evidence shows the activation mechanism and that low TERT triggers senescence, not a direct allele-specific expression measurement. | weak | [E04a](#e04a), [E04e](#e04e), [E18b](#e18b), [E18f](#e18f) |

Predictions: Allele-specific GABPA/GABPB1 ChIP signal at the TERT promoter only on the mutant allele and only in C228T-containing lines; GABPA or GABPB1 knockdown lowers TERT mRNA and telomerase activity selectively in C228T-mutant cells, with little effect in wild-type lines; Reporter gain of the A allele is abolished by destroying the created GGAA core while leaving flanks intact

Falsified if: GABPA/GABPB1 show no allele-specific occupancy at the mutant promoter; GABPA loss does not reduce TERT in C228T-mutant cells, or reduces it equally in wild-type cells; The A allele shows no increase in reporter activity

### 2. H5: Null: no TF-mediated effect of this variant at this site (p = 0.09)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-specific reporter and endogenous base-editing experiments show no change in TERT promoter output; No allele-specific TF occupancy at the site; Any association reflects a linked variant (for example the rs2853669 haplotype) or recurrent mutagenesis at a hotspot

Falsified if: Reporter or base-edited cells show the A allele drives higher TERT expression; Allele-specific ChIP identifies a factor bound only on the mutant allele

### 3. H2: The created ETS site is used by another abundant ETS factor (ETS1 or ELF1) rather than GABP (p = 0.08)

TF ETS1 (stated coverage own_model; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Group G003 predicts stronger alt binding for 18 ETS models; ETS1 has its own model and the highest expression in glioblastoma lines (61.0 TPM), so on expression alone it could occupy the created GGAA. Against this, no ENCODE ETS1 peak contains the site (absence may reflect missing experiments), and multiple ETS factors bind the -124C>T sequence in vitro without necessarily driving activation. | weak | [E05](#e05), [E06](#e06), [E17](#e17), [E18e](#e18e) |
| element | The created site lies inside the active TERT promoter-like cCRE with strong DNase/H3K4me3/H3K27ac signal. | supported | [E03](#e03) |
| gene | TERT is the gene whose TSS coincides with this promoter. | weak | [E02](#e02), [E03](#e03) |
| cell_type | ETS1 is abundant in glioblastoma lines (61 TPM); abundance is not occupancy, and no ChIP evidence supports binding here. | weak | [E06](#e06), [E17](#e17) |
| phenotype | If ETS1 occupied the new site it would activate TERT and sustain telomerase; no cited ETS1 perturbation or reporter data support this step. | missing | none |

Predictions: ETS1 (or ELF1) ChIP, not GABPA, shows mutant-allele-specific binding at the TERT promoter; ETS1 knockdown reduces TERT selectively in mutant lines while GABPA knockdown does not; Allelic effect size tracks ETS1 expression across tumour lines

Falsified if: GABPA/GABPB1 but not ETS1/ELF1 occupy the mutant site; ETS1 depletion leaves TERT unchanged in C228T-mutant cells

### 4. H4: The mutation reduces ZNF148 binding at the wild-type promoter, relieving repression of TERT (p = 0.07)

TF ZNF148 (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF148 was identified as a wild-type TERT promoter binder with reduced interaction with the -124C>T (C228T) allele, so the reference allele binds it more. ZNF148 does not appear in any screen row shown and has not been looked up, so its QBiC-SELEX coverage is not_checked and no QBiC direction is claimed for it. | weak | [E18e](#e18e) |
| element | The site is within the active TERT promoter cCRE. | supported | [E03](#e03) |
| gene | TERT is the gene at this promoter (TSS 0.0 kb). | weak | [E02](#e02), [E03](#e03) |
| cell_type | No cited evidence gives ZNF148 expression or occupancy in glioblastoma lines; the cell-type step is unsupported. | missing | none |
| phenotype | If ZNF148 restrains the wild-type promoter, its reduced binding would de-repress TERT; the cited work shows reduced interaction only, not a repressor function or an expression change. | weak | [E18e](#e18e) |

Predictions: ZNF148 ChIP shows reference-allele-specific binding at the TERT promoter; ZNF148 knockdown raises TERT from the reference promoter but not from the mutant promoter; Reporter gain of the A allele survives destruction of the created GGAA core, because the driver is loss of ZNF148 rather than ETS gain

Falsified if: ZNF148 shows no allele-specific binding at this site; ZNF148 depletion does not change TERT output from the reference promoter; Reporter gain requires an intact GGAA core

### 5. H3: The mutation destroys an AP-2 (TFAP2A) site, relieving repression of TERT (p = 0.04)

TF TFAP2A (stated coverage own_model; registry own_model), ref allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells (and melanoma).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AP-2 group G030 predicts weaker alt binding (best model TFAP2E z -36.84, effect -1.289; ref 99.5th -> alt 96.5th percentile); within the group TFAP2A has its own model, the highest expression in glioblastoma lines (9.65 TPM) and z -28.06, so it is the plausible lost factor. This is an in vitro prediction only. | weak | [E05](#e05), [E09](#e09) |
| element | The predicted lost site lies in the active TERT promoter cCRE; no evidence shows an AP-2 site is functional there. | weak | [E03](#e03) |
| gene | TERT is the promoter's own gene. | weak | [E02](#e02), [E03](#e03) |
| cell_type | TFAP2A is expressed in glioblastoma lines (9.65 TPM); no cited evidence supports an AP-2 role in melanoma TERT regulation. | weak | [E09](#e09) |
| phenotype | If AP-2 repressed this promoter, its loss would raise TERT; no cited evidence supports a repressor role for AP-2 here, and this chain does not explain the created GGAA. | missing | none |

Predictions: TFAP2A ChIP signal at the TERT promoter is reduced on the mutant allele; TFAP2A overexpression lowers output from the reference but not the mutant promoter; Mutating only the AP-2 half-site, without creating GGAA, raises promoter activity

Falsified if: No AP-2 occupancy at the TERT promoter in these cell types; TFAP2A perturbation does not alter TERT promoter activity; Reporter gain requires an intact GGAA core

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H4 | H3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific luciferase reporter: ref vs alt TERT promoter fragment in glioblastoma cells | low | yes | Alt allele gives clearly higher promoter activity | No difference between alleles | Alt allele gives higher activity | Alt allele gives higher activity (de-repression) | Alt allele gives higher activity (de-repression) |
| Reporter with the created GGAA core destroyed on the alt background | low | yes | Gain abolished | No gain to abolish | Gain abolished | Gain retained | Gain retained |
| Allele-specific reanalysis of existing ENCODE GABPA ChIP-seq (E16) in lines genotyped at chr5:1295113 | existing data | yes | Reads carrying A are enriched in GABPA peaks | No allelic skew for any factor | No allelic skew for GABPA | No allelic skew for GABPA | No allelic skew for GABPA |
| siRNA knockdown of GABPA/GABPB1 vs ETS1 in C228T-mutant and wild-type glioblastoma lines, TERT qPCR | medium | yes | GABPA/GABPB1 loss lowers TERT only in mutant lines; ETS1 loss has little effect | Any effect is equal in mutant and wild-type lines | ETS1 loss lowers TERT in mutant lines; GABPA loss does not | Neither lowers TERT selectively | Neither lowers TERT selectively |
| ZNF148 and TFAP2A ChIP-qPCR at the TERT promoter in heterozygous or isogenic ref/alt cells | medium | no | No reference-allele-specific ZNF148 or TFAP2A signal that explains activity | No allele-specific binding by either factor | No reference-allele-specific signal | ZNF148 bound preferentially on the ref allele | TFAP2A bound preferentially on the ref allele |
| Base-edit C228T into a wild-type glioblastoma line and measure TERT mRNA and telomerase activity | high | yes | TERT and telomerase rise; rise lost on GABPA/GABPB1 depletion | No change in TERT | TERT rises; rise lost on ETS1 depletion | TERT rises; unaffected by ETS factor depletion | TERT rises; unaffected by ETS factor depletion |
| qbic_tf_detail lookup of GABPB1 and ZNF148 | existing data | no | Clarifies GABPB1 coverage; H1 does not depend on it (GABPB1 binds via GABPA, not DNA sequence here) | Unaffected | Unaffected | Would replace ZNF148 not_checked with a stated coverage and possible direction | Unaffected |

## Next experiment

Allele-specific reanalysis of the existing ENCODE GABPA ChIP-seq datasets that already contain peaks over chr5:1295113 (E16), counting ref- versus alt-carrying reads in lines genotyped at this position. It uses existing data, and it separates the top two chains: H1 predicts mutant-allele-skewed GABPA occupancy, the null predicts no allelic skew. If genotyped reads are unavailable, the cheapest wet experiment is the ref-vs-alt luciferase reporter in a glioblastoma line.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": null})
- chip_peaks({"tf": "ETS1", "biosample": null})
- literature_search({"query": "GABPA TERT promoter mutation allele-specific recruitment glioblastoma"})

## Flags

- coverage_misstated: H4: stated not_checked, registry says not_in_coverage for ZNF148

Citation support: 0.85 of links cite only evidence that passed every check.

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

<a id="e04b"></a>**E04b** literature_search, Europe PMC abstract, PMID 42577103 (https://europepmc.org/article/MED/42577103; retrieved 2026-10-25T11:57:36+00:00)

> CDKN2A and CDK4 mutations act through UV-dependent and cell cycle disruption pathways, while BAP1, POT1, and TERT mutations are considered UV-independent.

<a id="e04c"></a>**E04c** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> The single nucleotide polymorphism (SNP) rs2853669, also located in the TERT promoter, may influence telomerase activity, though its clinical relevance in GBM remains unclear.

<a id="e04d"></a>**E04d** literature_search, Europe PMC abstract, PMID 42804732 (https://europepmc.org/article/MED/42804732; retrieved 2026-10-25T11:57:36+00:00)

> Patients carrying the SNP and TPM on the same allele (C/C and T/C cis) had shorter overall survival than those carrying them on different alleles (T/T or T/C trans; 19 vs 25 months, p = 0.048), and TERT expression was also lower in this group (p = 0.038).

<a id="e04e"></a>**E04e** literature_search, Europe PMC abstract, PMID 42807929 (https://europepmc.org/article/MED/42807929; retrieved 2026-10-25T11:57:36+00:00)

> Additionally, loss of either USP10 or FOXM1 suppresses the expression of the downstream target Telomerase reverse transcriptase (TERT), triggering cellular senescence.

<a id="e04f"></a>**E04f** literature_search, Europe PMC abstract, PMID 42859331 (https://europepmc.org/article/MED/42859331; retrieved 2026-10-25T11:57:36+00:00)

> TERT promoter (TERTp) mutations are among the most frequent molecular alterations in isocitrate dehydrogenase (IDH) wild-type glioblastoma (GBM), yet the molecular profiles and prognostic implications associated with TERTp status remain incompletely characterized.

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

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295113:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T22:26:15+00:00)

> No ENCODE ETS1 ChIP-seq peak contains chr5:1295113:G>A. Absence can also mean no ETS1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABPA%20TERT%20promoter%20mutation%20allele-specific%20recruitment%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T22:26:15+00:00)

> Europe PMC: 40 hits for 'GABPA TERT promoter mutation allele-specific recruitment glioblastoma'; top 8 with PMIDs:
> PMID 40513567 (2025): The immortality mechanism of TERT promoter mutant cancers is self-reinforcing and reversible.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 37918959 (2023): E4F1 and ZNF148 are transcriptional activators of the -57A &gt; C and wild-type &lt;i&gt;TERT&lt;/i&gt; promoter.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 36114166 (2022): Conserved features of TERT promoter duplications reveal an activation mechanism that mimics hotspot mutations in cancer.
> PMID 38285162 (2024): Mechanisms of telomere maintenance and associated therapeutic vulnerabilities in malignant gliomas.
> PMID 35568649 (2022): Emerging mechanisms of telomerase reactivation in cancer.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-25T22:26:15+00:00)

> TERT promoter (TERTp) mutations create a de novo E26 transformation-specific (ETS) transcription factor binding motif.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-25T22:26:15+00:00)

> Here, we analyzed 53 cell lines representing 16 cancer types and 6 recurrent TERTp mutations and found that the GA-binding protein (GABP) tetramer is responsible for promoter activation in all cases.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 36114166 (https://europepmc.org/article/MED/36114166; retrieved 2026-10-25T22:26:15+00:00)

> Beyond the two most common point mutations, which selectively recruit the ETS factor GABP to activate TERT, the significance of other variants is unknown.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 36114166 (https://europepmc.org/article/MED/36114166; retrieved 2026-10-25T22:26:15+00:00)

> The duplications recruit a GABP tetramer by virtue of the native ETS motif and its precisely spaced duplicated counterpart, activate the promoter and are clonal in a TERT expressing multifocal glioblastoma.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 37918959 (https://europepmc.org/article/MED/37918959; retrieved 2026-10-25T22:26:15+00:00)

> Although we confirmed binding of multiple ETS factors to the mutant -146C > T and -124C > T sequences, we identified E4F1 as a -57A > C-specific binder and ZNF148 as a TERT wild-type (WT) promoter binder that showed reduced interaction with the -124C > T allele.

<a id="e18f"></a>**E18f** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-25T22:26:15+00:00)

> These mutations promote TERT gene expression by multiple mechanisms, including the generation of novel binding sites for nuclear transcription factors, displacement of negative regulators from DNA G-quadruplexes, recruitment of epigenetic activators and disruption of long-range interactions between TERT locus and telomeres.

<a id="e18g"></a>**E18g** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-25T22:26:15+00:00)

> Specifically, AURKB, via REST, is recruited to TERTp MUT by TRIM28.
