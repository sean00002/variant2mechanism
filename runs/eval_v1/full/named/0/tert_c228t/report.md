# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.61 over 8 model calls; 185 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen

310 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 166.19); Ets, 4 models (best ELF3, z 70.12); Ets, 1 model (best SPDEF, z 47.58); AP-2, 4 models (best TFAP2E, z -36.84); C2H2 ZF, 1 model (best ZNF582, z 22.77).

## Ranked chains

### 1. H1: C228T creates a de novo ETS site occupied by GABPA (GABP complex), activating TERT in glioblastoma (p = 0.65)

TF GABPA (stated coverage own_model; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS), chr5:1294945-1295294; gene TERT; cell type Glioblastoma tumor cells (IDH-wildtype).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | 18 ETS-specificity models pass the QBiC gate, all alt-preferring, and the site rises from the 97.1th to the 99.3th percentile of k-mer coefficients; within this shared-specificity group GABPA is chosen because it is the only member with direct occupancy evidence at this exact base (two ENCODE ChIP-seq peaks containing chr5:1295113 in HepG2 and SK-N-SH), has its own passing model (z 68.47) and is expressed at 15.5 TPM in glioblastoma lines; the literature also states that canonical TERT promoter mutations create de novo ETS-family binding sites | weak | [E05](#e05), [E06](#e06), [E16](#e16), [E17a](#e17a) |
| element | The variant lies in an active promoter-like cCRE at the TERT TSS with high DNase, H3K4me3 and H3K27ac (z-scores are maxima across biosamples, not glioblastoma-specific), and VEP annotates a promoter regulatory feature | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is 0 kb from the variant and is the only gene whose TSS the cCRE abuts; literature states these promoter mutations promote TERT expression partly by generating novel TF binding sites. Support beyond proximity plus literature is still indirect (no eQTL or isogenic knock-in data here) | weak | [E01](#e01), [E02](#e02), [E17c](#e17c) |
| cell_type | GABPA is expressed at 15.5 TPM across 54 glioblastoma lines and the promoter cCRE is in an accessible, active state, so the created site can be occupied; GABPA is a DepMap common essential, so its strong knockout effect in CNS lines is not lineage-specific evidence | weak | [E06](#e06), [E03](#e03), [E18](#e18) |
| phenotype | Telomerase reactivation averts replicative senescence; TERT promoter mutations are among the most frequent alterations in IDH-wildtype glioblastoma and occur in 50-82% of melanomas. These quotes concern TERT promoter mutations generally, not GABP specifically | weak | [E04a](#e04a), [E04f](#e04f), [E04e](#e04e) |

Predictions: Allele-specific GABPA/GABPB1 ChIP or CUT&RUN in a C228T-heterozygous glioblastoma line shows occupancy only on the mutant allele; GABPB1 (not common-essential) knockdown lowers TERT mRNA specifically in C228T-mutant lines, not in promoter-wild-type lines; Reporter activity gain requires the created ETS core; mutating it abolishes the gain

Falsified if: No GABP subunit occupancy at the mutant promoter by ChIP/CUT&RUN in mutant lines; GABPB1/GABPA depletion leaves TERT unchanged in mutant cells; Isogenic knock-in of the alt allele does not raise TERT

### 2. H5: Null: no TF-mediated effect of this base change; recurrence reflects a mutational hotspot or a linked driver (p = 0.13)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-specific reporter and ChIP assays show no allelic difference at this base; TERT mRNA is unrelated to mutation status once linked promoter variants such as rs2853669 are accounted for; Recurrence is explained by a UV/CC>TT-prone hotspot rather than a functional gain; note that hotspot formation and function are not mutually exclusive (E17a describes a hotspot effect caused by the created ETS site)

Falsified if: Allele-specific TF occupancy or reporter activity is demonstrated at this base; Isogenic knock-in of the alt allele raises TERT expression

### 3. H2: Another expressed ETS factor (ETS1) occupies the created site and drives TERT (p = 0.12)

TF ETS1 (stated coverage mapped; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt-preferring ETS specificity of group G003 is shared across family members; ETS1 is covered only through a CIS-BP-mapped model and is not among the listed passing members, so the group z-scores belong to ETV5/ELF1/GABPA and are not model-specific evidence for ETS1. ETS1 is nominated solely because it is the highest-expressed covered member (61.0 TPM) in glioblastoma lines, consistent with ETS-site creation reported in the literature | weak | [E05](#e05), [E06](#e06), [E17a](#e17a) |
| element | The created site lies in the active TERT promoter cCRE with strong H3K4me3/H3K27ac/DNase signal | supported | [E03](#e03) |
| gene | Occupancy of the new site by ETS1 would raise TERT transcription from the adjacent TSS; only proximity supports the gene assignment | weak | [E02](#e02), [E17c](#e17c) |
| cell_type | ETS1 is the most abundant covered ETS-group TF in glioblastoma lines (61.0 TPM), so it is available to bind; no occupancy data support it at this base, unlike GABPA | weak | [E06](#e06), [E16](#e16) |
| phenotype | Telomerase reactivation sustains proliferation in glioblastoma and melanoma | weak | [E04a](#e04a), [E04f](#e04f) |

Predictions: ETS1 ChIP signal, not GABP, is detected at the mutant promoter; ETS1 knockdown lowers TERT in mutant lines while GABPB1 knockdown does not; TERT induction tracks with ETS1 level across mutant lines

Falsified if: ETS1 depletion does not change TERT in C228T lines; GABP subunits, not ETS1, are the factors detected at the mutant allele

### 4. H4: The mutation destroys an AP-2 (TFAP2A) site, relieving repression at the TERT promoter (p = 0.06)

TF TFAP2A (stated coverage own_model; registry own_model), ref allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Four AP-2 models pass with a ref-preferring sign (TFAP2E z -36.84; site falls from 99.5th to 96.5th percentile); TFAP2A is chosen as the member with its own passing model (z -28.06) and real expression in glioblastoma lines (9.65 TPM). This is an in vitro prediction only and is much smaller in magnitude than the ETS gain | weak | [E05](#e05), [E09](#e09) |
| element | Loss of a TF site inside the active promoter cCRE could change factor composition at the TSS; no evidence shows AP-2 acts at this element | weak | [E03](#e03) |
| gene | If AP-2 is repressive here, its displacement would de-repress TERT; the literature mentions displacement of negative regulators as one mechanism of TERT promoter mutations, but names no specific factor | weak | [E02](#e02), [E17c](#e17c) |
| cell_type | TFAP2A (9.65 TPM) and TFAP2C (6.49 TPM) are expressed in glioblastoma lines, so the reference site could be occupied in wild-type cells | weak | [E09](#e09) |
| phenotype | Higher telomerase activity supports immortalization in glioblastoma and melanoma | weak | [E04a](#e04a), [E04f](#e04f) |

Predictions: AP-2 ChIP signal present on the reference allele and lost on the mutant allele; TFAP2A overexpression suppresses the wild-type but not the mutant promoter in reporters; Reporter gain survives mutation of the created ETS core as long as the AP-2 site stays broken

Falsified if: No AP-2 occupancy at the wild-type TERT promoter; TFAP2A perturbation does not alter TERT; Reporter gain requires the intact created ETS core

### 5. H3: The new ETS-type site is bound by ETV6, whose repressive occupancy modulates rather than drives TERT output (p = 0.04)

TF ETV6 (stated coverage own_model; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumor cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Group G020 shows a large alt-preferring effect (ELF3 model, effect 3.463); within it ELF3/ELF5/EHF/SPDEF are essentially unexpressed (<0.5 TPM), leaving ETV6 (5.65 TPM, own passing model z 46.32) as the plausible binder | weak | [E05](#e05), [E07](#e07) |
| element | The created site is in the active TERT promoter cCRE; no evidence identifies ETV6 activity at this element | weak | [E03](#e03) |
| gene | Because alt binds ETV6 more, this chain predicts dampening, not activation, of TERT; it can only explain variable TERT levels among mutant tumors through competition with activating ETS factors, not the overall gain | missing | [E02](#e02) |
| cell_type | ETV6 is expressed only modestly (5.65 TPM) in glioblastoma lines, limiting its influence relative to the abundant activating ETS factors | weak | [E07](#e07), [E06](#e06) |
| phenotype | Differences in TERT expression and survival among promoter-mutant tumors exist (shown for cis rs2853669), but no cited evidence links that variability to ETV6 | missing | [E04c](#e04c), [E04d](#e04d) |

Predictions: ETV6 ChIP shows occupancy at the mutant allele; ETV6 knockdown further raises TERT in mutant cells; TERT induction by the mutation is larger in ETV6-low lines

Falsified if: No ETV6 binding at the mutant promoter; ETV6 knockdown does not change TERT levels

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H4 | H3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query existing ENCODE/Factorbook TF ChIP-seq peaks overlapping chr5:1295113 for GABPA vs ETS1/ELF1/ETV5/TFAP2A/ETV6 | existing data | yes | GABPA peaks overlap the site (already observed in HepG2 and SK-N-SH, E16) | No consistent allele-linked TF occupancy at this base | ETS1 peaks should overlap at least as consistently as GABPA | TFAP2A peaks overlap in wild-type cells; ETS peaks not required | ETV6 peaks overlap the site |
| Allele-specific CUT&RUN for GABPA/GABPB1 and ETS1 in a C228T-heterozygous glioblastoma line | medium | yes | GABP reads strongly skewed to the mutant allele; ETS1 not | No allelic skew for any factor | ETS1 reads skewed to the mutant allele; GABP flat | Neither ETS factor skewed; AP-2 signal skewed to reference allele | ETV6 skewed to mutant allele |
| siRNA knockdown of GABPB1 vs ETS1 in C228T-mutant and wild-type glioblastoma lines, measure TERT mRNA | low | yes | GABPB1 knockdown lowers TERT only in mutant lines; ETS1 knockdown has little effect | No mutation-status-dependent effect of any knockdown | ETS1 knockdown lowers TERT in mutant lines; GABPB1 knockdown does not | Neither knockdown changes TERT; TFAP2A overexpression lowers wild-type promoter only | ETV6 knockdown raises TERT; ETS knockdowns have modest effects |
| Luciferase reporter with ref vs alt promoter, plus a version with the created ETS core disrupted | low | no | Alt > ref; gain abolished when the created ETS core is disrupted | No allelic difference | Alt > ref; gain abolished by the same ETS-core disruption (indistinguishable from H1 here) | Alt > ref even when the created ETS core is disrupted, as long as the AP-2 site stays broken | Little or no gain, or a decrease, from the alt allele |
| Isogenic CRISPR knock-in of the alt allele into a TERT-promoter-wild-type glioblastoma line; measure TERT mRNA and telomerase activity | high | no | TERT rises; rise is GABP-dependent | TERT unchanged | TERT rises; rise is ETS1-dependent | TERT rises and is sensitive to TFAP2A level | TERT unchanged or lower |
| eQTL/expression lookup linking allele status to TERT expression in brain or tumor cohorts | existing data | no | Mutant tumors show higher TERT | No association after controlling for linked variants | Mutant tumors show higher TERT (same direction) | Mutant tumors show higher TERT (same direction) | No consistent increase, or decrease, with mutation |

## Next experiment

Cheapest separator of H1 vs H2: first mine existing ENCODE/Factorbook ChIP-seq (existing data) for ETS1/ELF1/ETV5 peaks overlapping chr5:1295113 to compare with the GABPA peaks already found (E16); if that is uninformative, run a low-cost siRNA knockdown of GABPB1 versus ETS1 in a C228T-mutant and a wild-type glioblastoma line and measure TERT mRNA (GABPB1 avoids the common-essential confound of GABPA, E18).

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": null})
- literature_search({"query": "TERT promoter mutation C228T GABP ETS binding site recruitment"})
- gene_dependency({"gene": "GABPA"})

## Flags

- coverage_misstated: H2: stated mapped, registry says own_model for ETS1

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

> QBiC-SELEX screen of chr5:1295113:G>A: 997 models scored, 310 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 230 CIS-BP groups. Expression context: DepMap subtype median Glioblastoma. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 47 (Ets, 3 models z 16.96, Myb/SANT, 1 model z -16.15, Homeodomain, 1 model z -15.52, bHLH, 1 model z -14.2, bHLH, 1 model z -14.2). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e06"></a>**E06** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 166.19, effect 2.121 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: ETV5 z 166.19, ELF1 z 124.32, ELF4 z 85.47, GABPA z 68.47, ELK4 z 56.2 (+13 more). TFs this group covers (own and CIS-BP-mapped models): ETS1 61.01 TPM, ERF 39.81 TPM, ELK3 30.24 TPM, ELK1 26.81 TPM, ETV5 22.15 TPM, ETS2 21.07 TPM, ELF2 18.42 TPM, ELF1 17.41 TPM, GABPA 15.52 TPM, ELF4 15.44 TPM (+15 more); best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G020 (Ets, 4 models): best model ELF3_NA_TCCGTG20NTGC_ESY_yang2017_0_4_7mer (own model of ELF3), z 70.12, effect 3.463 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: ELF3 z 70.12, ELF5 z 66.13, ETV6 z 46.32, ETV7 z 43.37. TFs this group covers (own and CIS-BP-mapped models): ERF 39.81 TPM, ELF2 18.42 TPM, ELF1 17.41 TPM, ELF4 15.44 TPM, ETV6 5.65 TPM, ELF3 0.47 TPM, ETV7 0.31 TPM, EHF 0.17 TPM, SPI1 0.05 TPM, ELF5 0.03 TPM (+1 more); best model's site strength: ref 99.2th, alt 100.0th percentile of its k-mer coefficients.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G345 (Ets, 1 model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (own model of SPDEF), z 47.58, effect 1.511 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SPDEF z 47.58. TFs this group covers (own and CIS-BP-mapped models): ELF2 18.42 TPM, ELF1 17.41 TPM, ELF4 15.44 TPM, SPDEF 0.05 TPM; best model's site strength: ref 98.5th, alt 99.9th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (own model of TFAP2E), z -36.84, effect -1.289 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TFAP2E z -36.84, TFAP2B z -30.5, TFAP2A z -28.06, TFAP2C z -24.32. TFs this group covers (own and CIS-BP-mapped models): TFAP2A 9.65 TPM, TFAP2C 6.49 TPM, TFAP2E 0.49 TPM, TFAP2B 0.0 TPM, TFAP2D 0.0 TPM; best model's site strength: ref 99.5th, alt 96.5th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G541 (C2H2 ZF, 1 model): best model ZNF582_FL_CT40NCGGAGA_AATBA_jolma2025_0_3_7mer (own model of ZNF582), z 22.77, effect 0.322 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF582 z 22.77. TFs this group covers (own and CIS-BP-mapped models): ZNF582 2.16 TPM; best model's site strength: ref 59.5th, alt 91.2th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G032 (C2H2 ZF, 4 models): best model ZIC4_eDBD_TGCGTA40NTCA_KT_yin2017_1_3_7mer (own model of ZIC4), z -20.85, effect -0.916 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: ZIC4 z -20.85, ZIC1 z -17.64, ZIC3 z -8.6. TFs this group covers (own and CIS-BP-mapped models): ZIC1 13.23 TPM, ZIC2 3.7 TPM, ZIC4 1.37 TPM, ZIC5 0.53 TPM, ZIC3 0.0 TPM; best model's site strength: ref 99.8th, alt 97.4th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G575 (C2H2 ZF, 1 model): best model ZNF706_FL_CT40NTCTAGT_YWSA_jolma2025_0_3_7mer (own model of ZNF706), z -19.9, effect -0.524 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF706 z -19.9. TFs this group covers (own and CIS-BP-mapped models): ZNF706 81.43 TPM; best model's site strength: ref 99.9th, alt 99.4th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G245 (mTERF, 1 model): best model MTERF3_FL_GG40NTAGTTT_YWJA_jolma2025_0_3_7mer (own model of MTERF3), z 18.39, effect 0.175 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: MTERF3 z 18.39. TFs this group covers (own and CIS-BP-mapped models): MTERF3 20.63 TPM; best model's site strength: ref 65.8th, alt 79.7th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G620 (C2H2 ZF, 1 model): best model ZNF92_FL_TC40NAATCTC_YWIA_jolma2025_0_3_7mer (own model of ZNF92), z -18.29, effect -0.342 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF92 z -18.29. TFs this group covers (own and CIS-BP-mapped models): ZNF92 9.63 TPM; best model's site strength: ref 99.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G544 (C2H2 ZF, 1 model): best model ZNF596_FL_GA40NTGTATC_AATA_jolma2025_0_3_7mer (own model of ZNF596), z -18.26, effect -0.275 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF596 z -18.26. TFs this group covers (own and CIS-BP-mapped models): ZNF596 3.59 TPM; best model's site strength: ref 100.0th, alt 99.5th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295113:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e17"></a>**E17** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20mutation%20C228T%20GABP%20ETS%20binding%20site%20recruitment&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T16:31:05+00:00)

> Europe PMC: 35 hits for 'TERT promoter mutation C228T GABP ETS binding site recruitment'; top 8 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 39557834 (2024): Mechanistic basis of atypical TERT promoter mutations.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 38201248 (2023): The Biological and Clinical Role of the Telomerase Reverse Transcriptase Gene in Glioblastoma: A Potential Therapeutic Target?
> PMID 38285162 (2024): Mechanisms of telomere maintenance and associated therapeutic vulnerabilities in malignant gliomas.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 35903534 (2022): TERT Promoter Mutations and Telomerase in Melanoma.
> PMID 38278800 (2024): The regulations of telomerase reverse transcriptase (TERT) in cancer.

<a id="e17a"></a>**E17a** literature_search, Europe PMC abstract, PMID 39557834 (https://europepmc.org/article/MED/39557834; retrieved 2026-10-25T16:31:05+00:00)

> Canonical TERTp mutations create de novo binding sites for ETS family transcription factors that induce favourable conditions for DNA damage formation by UV light, thus creating a hotspot effect but only after a first mutational hit.

<a id="e17b"></a>**E17b** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-25T16:31:05+00:00)

> Specifically, AURKB, via REST, is recruited to TERTp MUT by TRIM28.

<a id="e17c"></a>**E17c** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-25T16:31:05+00:00)

> These mutations promote TERT gene expression by multiple mechanisms, including the generation of novel binding sites for nuclear transcription factors, displacement of negative regulators from DNA G-quadruplexes, recruitment of epigenetic activators and disruption of long-range interactions between TERT locus and telomeres.

<a id="e18"></a>**E18** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for GABPA (0 = no effect, -1 = median common-essential; < -0.5 called dependent). CNS/Brain lineage, 50 lines: median -0.87, 94% dependent. All 1183 lines: median -0.87, 97% dependent. common-essential in DepMap: a strong knockout effect here is not evidence for a lineage-specific role.
