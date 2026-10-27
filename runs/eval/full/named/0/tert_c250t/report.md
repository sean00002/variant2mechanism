# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.59 over 8 model calls; 173 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen

477 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 167.5); Ets, 4 models (best ELF3, z 114.84); Ets, 1 model (best SPDEF, z 78.05); MBD; CxxC ZF, 1 model (best MBD1, z -41.31); C2H2 ZF, 1 model (best ZNF654, z -35.62).

## Ranked chains

### 1. H1: C250T creates a de novo ETS site occupied by GABPA (GABP complex), activating TERT (p = 0.62)

TF GABPA (stated coverage own_model; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells (IDH-wildtype).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele creates a GGAA ETS core: Ets group G003 passes strongly with alt binding more (best model ETV5 z 167.5; site strength ref 94.8th to alt 99.9th percentile), and GABPA has its own passing QBiC-SELEX model (z 71.32) and is expressed at 15.5 TPM in glioblastoma lines. Within this group I chose GABPA over ETV5/ELF1 on two pieces of cited evidence rather than on the SELEX ranking: ENCODE ChIP-seq shows GABPA peaks containing this exact position in two biosamples (E16), while no ELF1 peak contains or lies within 100 bp of it (E17), and the published mechanism at mutant TERT promoters is selective GABPA recruitment (E18b). The GABP heterotetramer/second-ETS-site spacing model is background knowledge, not shown by the cited evidence. | weak | [E05](#e05), [E06](#e06), [E16](#e16), [E17](#e17), [E18b](#e18b), [E18a](#e18a) |
| element | The variant lies inside promoter-like cCRE EH38E3622530 with high DNase, H3K4me3 and H3K27ac (z-scores are maxima across biosamples, so GBM-specific activity is not shown), and VEP annotates a promoter regulatory feature; GABPA ChIP peaks in HepG2 and SK-N-SH show this element is TF-occupied in at least some cell types. | weak | [E01](#e01), [E03](#e03), [E16](#e16) |
| gene | The element is the TERT core promoter (TERT TSS 0 kb); CLPTM1L is 50 kb away. Assignment is by promoter identity and proximity only - no eQTL, CRISPR or allele-specific expression evidence is cited, and the cCRE also lists MIR4457 and CLPTM1L. | weak | [E01](#e01), [E02](#e02), [E03](#e03) |
| cell_type | GABPA is expressed in glioblastoma lines (15.5 TPM) and TERT promoter mutations are among the most frequent alterations in IDH-wildtype GBM; occupancy of this site has been shown in HepG2 and SK-N-SH, not in GBM tumour cells, so lineage specificity is inferred, not demonstrated. | weak | [E06](#e06), [E16](#e16), [E04f](#e04f) |
| phenotype | If TERT is transcriptionally reactivated, telomerase activity is restored, which is the common molecular feature of TERTp-mutant melanoma and GBM and whose loss triggers senescence; the cited quotes are generic to TERTp mutations and do not test GABPA specifically. | weak | [E04a](#e04a), [E04e](#e04e), [E04f](#e04f) |

Predictions: Allele-specific GABPA/GABPB1 ChIP in a heterozygous C250T line shows occupancy biased to the mutant allele; GABPB1L or GABPA depletion lowers TERT specifically in TERTp-mutant lines; Reporter gain from C250T is lost when the created GGAA is disrupted

Falsified if: GABPA ChIP shows equal occupancy on mutant and wild-type alleles; GABPA/GABPB1 depletion leaves mutant TERT expression unchanged; Editing the created GGAA core does not abolish the reporter gain

### 2. H5: Null: no TF-mediated allelic effect of this variant at this site (p = 0.19)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-specific reporter or prime-edited isogenic lines show no TERT promoter activity difference between G and A; No TF shows allele-specific occupancy; recurrence reflects a UV/mutational hotspot effect at this position, and expression differences in mutant tumours trace to linked haplotype context such as rs2853669

Falsified if: Luciferase or isogenic editing shows reproducible TERT activation by C250T alone; Allele-specific ChIP demonstrates a TF bound only on the mutant allele

### 3. H2: A different class I ETS factor (ELF1/ETV5-type) occupies the new site and drives TERT (p = 0.09)

TF ELF1 (stated coverage own_model; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Group G003 predicts a large alt-preferring gain and ELF1 has its own passing model (z 164.23) with 17.4 TPM in GBM lines; the SELEX screen cannot separate ELF1 from GABPA. Against this chain, no ENCODE ELF1 peak contains the position or lies within 100 bp, although absence may reflect missing experiments in the relevant biosample. | weak | [E05](#e05), [E06](#e06), [E17](#e17) |
| element | The gained site sits in the active promoter-like cCRE EH38E3622530 at the TERT TSS. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is the promoter's own gene at 0 kb; assignment is proximity-based only. | weak | [E02](#e02) |
| cell_type | ELF1 and related class I ETS factors listed in G003 are expressed at tens of TPM in glioblastoma lines; no occupancy evidence in this lineage is cited. | weak | [E06](#e06) |
| phenotype | Higher TERT transcription restores telomerase and supports tumour growth; the cited quotes do not implicate ELF1. | weak | [E04a](#e04a), [E04f](#e04f) |

Predictions: ELF1 (not GABPA) ChIP shows mutant-allele-specific binding once an ELF1 experiment is run in a TERTp-mutant line; TERT stays induced after GABPB1L knockdown but falls after ELF1 knockdown

Falsified if: ELF1 ChIP in a TERTp-mutant line shows no allelic bias; TERT induction is fully GABP-dependent

### 4. H3: Loss of MBD1 binding de-represses the TERT promoter (p = 0.06)

TF MBD1 (stated coverage own_model; registry own_model), ref allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MBD1 has its own QBiC-SELEX model that loses binding on the alt allele (z -41.31, effect -1.236; ref 100th to alt 98.6th percentile) and is expressed at 31.5 TPM; the SELEX assay uses unmethylated DNA, so this does not demonstrate methyl-CpG-dependent binding at this site. | weak | [E05](#e05), [E09](#e09) |
| element | The site lies in the TERT promoter-like cCRE; no methylation or CpG-density evidence is cited for this element. | weak | [E03](#e03) |
| gene | If MBD1 represses at the TERT core promoter, its loss would raise TERT; no cited evidence shows MBD1 regulates TERT. | missing | [E01](#e01), [E02](#e02) |
| cell_type | MBD1 is expressed in glioblastoma lines (31.5 TPM); occupancy at TERT is not shown. | weak | [E09](#e09) |
| phenotype | De-repressed TERT would restore telomerase and avert senescence; the cited quotes are generic. | weak | [E04a](#e04a), [E04e](#e04e) |

Predictions: MBD1 ChIP shows occupancy on the wild-type but not the mutant allele; MBD1 knockdown raises TERT in promoter-wild-type GBM cells, phenocopying C250T; Reporter gain from C250T persists when the created GGAA is disrupted

Falsified if: MBD1 does not occupy the TERT promoter in GBM cells; MBD1 depletion does not change TERT expression; The C250T reporter gain requires the created ETS core

### 5. H4: ELF3/ETV6-type ETS specificity (group G020) mediates the gain, with ETV6 the only expressed member (p = 0.04)

TF ETV6 (stated coverage own_model; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Group G020 has the largest per-model effect (5.168 for ELF3, alt binds more); ELF3/ELF5/ETV7 are below 0.5 TPM, so within the group I chose ETV6 (own model, z 46.24, 5.65 TPM) as the only expressed member - the large effect size belongs to ELF3, not ETV6, so the quantitative support for ETV6 is weaker. | weak | [E05](#e05), [E07](#e07) |
| element | The gained site is inside the active promoter-like cCRE at TERT. | weak | [E03](#e03) |
| gene | TERT is the gene of this promoter; proximity only. | weak | [E02](#e02) |
| cell_type | ETV6 expression in glioblastoma lines is low (5.65 TPM) and no occupancy at this site is shown. | weak | [E07](#e07) |
| phenotype | ETV6 is generally a repressor, so gained ETV6 binding would be expected to lower rather than raise TERT; this chain therefore does not readily explain telomerase reactivation in TERTp-mutant tumours. | missing | [E04a](#e04a) |

Predictions: ETV6 ChIP shows mutant-allele-specific binding at the TERT promoter; ETV6 depletion raises mutant TERT (repressor direction) rather than lowering it

Falsified if: ETV6 is not bound at the TERT promoter; TERT induction persists unchanged after ETV6 loss

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA/GABPB1 ChIP-seq (or ChIP-PCR) in a heterozygous C250T line | medium | yes | Strong mutant-allele bias in GABPA occupancy | No allelic bias for any TF | No or weak GABPA bias; bias seen for ELF1 instead | No GABPA bias | No GABPA bias |
| Luciferase reporter of the TERT promoter, G vs A at chr5:1295135, in a GBM line | low | yes | A allele gives higher activity; gain lost if the created GGAA is mutated | No reproducible difference between G and A | A allele gives higher activity; gain lost if GGAA mutated | Little or no gain in an unmethylated plasmid reporter; gain independent of the GGAA core | No gain or a decrease in activity |
| GABPB1L knockdown and TERT qPCR in TERTp-mutant vs wild-type lines | medium | yes | TERT falls selectively in mutant lines | No mutant-selective effect | TERT largely unchanged in mutant lines | No mutant-selective effect | No mutant-selective effect |
| ELF1 ChIP-seq in a TERTp-mutant GBM line (currently absent from ENCODE at this site, E17) | medium | no | No ELF1 allelic bias, or bias weaker than GABPA | No ELF1 bias | Clear ELF1 mutant-allele bias | No ELF1 bias | No ELF1 bias |
| MBD1 ChIP plus MBD1 knockdown with TERT qPCR and bisulfite methylation of the promoter | medium | no | No MBD1 occupancy or effect | No MBD1 effect | No MBD1 occupancy or effect | MBD1 bound on ref allele; knockdown raises TERT | No MBD1 effect |
| eQTL / allele-specific expression lookup linking chr5:1295135 genotype to TERT vs CLPTM1L | existing data | yes | Mutant allele associated with higher TERT, not CLPTM1L | No allelic association with TERT, or association attributable to a linked variant | Same direction as H1 (does not separate from H1) | Higher TERT on mutant allele | Lower or unchanged TERT |

## Next experiment

Run the low-cost luciferase reporter comparing G and A at chr5:1295135 in a glioblastoma line, with a paired construct in which the created GGAA core is disrupted: a reproducible A-allele gain that depends on the ETS core supports H1 and falsifies the null (H5), which is the cheapest test separating the top two chains.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": null})
- chip_peaks({"tf": "ELF1", "biosample": null})
- literature_search({"query": "GABP TERT promoter mutation C250T allele-specific recruitment"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

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

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T22:26:16+00:00)

> No ENCODE ELF1 ChIP-seq peak contains chr5:1295135:G>A. Absence can also mean no ELF1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABP%20TERT%20promoter%20mutation%20C250T%20allele-specific%20recruitment&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T22:26:17+00:00)

> Europe PMC: 25 hits for 'GABP TERT promoter mutation C250T allele-specific recruitment'; top 8 with PMIDs:
> PMID 39557834 (2024): Mechanistic basis of atypical TERT promoter mutations.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 38201248 (2023): The Biological and Clinical Role of the Telomerase Reverse Transcriptase Gene in Glioblastoma: A Potential Therapeutic Target?
> PMID 38285162 (2024): Mechanisms of telomere maintenance and associated therapeutic vulnerabilities in malignant gliomas.
> PMID 35903534 (2022): TERT Promoter Mutations and Telomerase in Melanoma.
> PMID 36979671 (2023): Deciphering the Functions of Telomerase Reverse Transcriptase in Head and Neck Cancer.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 33483600 (2021): Synergistic activation of mutant TERT promoter by Sp1 and GABPA in BRAF<sup>V600E</sup>-driven human cancers.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 39557834 (https://europepmc.org/article/MED/39557834; retrieved 2026-10-25T22:26:17+00:00)

> Canonical TERTp mutations create de novo binding sites for ETS family transcription factors that induce favourable conditions for DNA damage formation by UV light, thus creating a hotspot effect but only after a first mutational hit.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 33483600 (https://europepmc.org/article/MED/33483600; retrieved 2026-10-25T22:26:17+00:00)

> Here, we report that transcription factor GABPA mediates the regulation of BRAFV600E/MAPK signaling on TERT reactivation by selectively recruiting activated ERK to mutant TERT promoter, where activated ERK can phosphorylate Sp1, thereby resulting in HDAC1 dissociation and an active chromatin state.
