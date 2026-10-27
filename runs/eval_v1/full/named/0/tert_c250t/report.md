# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.61 over 8 model calls; 196 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen

477 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 167.5); Ets, 4 models (best ELF3, z 114.84); Ets, 1 model (best SPDEF, z 78.05); MBD; CxxC ZF, 1 model (best MBD1, z -41.31); C2H2 ZF, 1 model (best ZNF654, z -35.62).

## Ranked chains

### 1. H1: C250T creates a de novo ETS site occupied by GABPA (GABP complex), activating TERT transcription in glioblastoma (p = 0.56)

TF GABPA (stated coverage own_model; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells (IDH-wildtype).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele gains ETS-class binding: group G003 has 18/18 passing models concordant for alt binding more (best model ETV5 z 167.5, effect 2.42; site strength ref 94.8th to alt 99.9th percentile). Within this shared-specificity group I choose GABPA, not because it is the top model (it is not; ETV5, ELF1, ELF4 score higher) but because it is the only group member with direct ChIP evidence of occupancy at this exact position: two ENCODE GABPA peaks (HepG2, SK-N-SH) contain chr5:1295135, and GABPA has its own passing QBiC model (z 71.3) and is expressed in glioblastoma lines (15.5 TPM). The ChIP peaks are from wild-type, non-glioma biosamples, so they show the promoter is a GABPA-bound region, not that binding is allele-specific. | weak | [E05](#e05), [E06](#e06), [E16](#e16) |
| element | The variant lies in ENCODE cCRE EH38E3622530, a promoter-like signature with high DNase, H3K4me3 and H3K27ac (z-scores are maxima across biosamples, not glioblastoma-specific), i.e. the TERT core promoter; two flanking pELS elements are also annotated but no second native ETS site is documented in the evidence. | supported | [E01](#e01), [E03](#e03) |
| gene | The variant is 0.0 kb from the TERT TSS and inside the TERT promoter cCRE, so cis action on TERT is far more likely than on CLPTM1L (50 kb) or other neighbours; this is proximity only, with no eQTL or allele-specific expression evidence cited. | weak | [E02](#e02), [E03](#e03) |
| cell_type | GABPA is expressed in glioblastoma lines (15.5 TPM) and TERTp mutations are among the most frequent alterations in IDH-wildtype GBM, which is consistent with but does not prove cell-type-specific action here. | weak | [E06](#e06), [E04f](#e04f), [E18a](#e18a) |
| phenotype | Literature reports that the hotspot promoter mutations C228T and C250T are recurrent across melanoma, bladder and CNS tumours and act by generating novel TF binding sites that raise TERT expression and telomerase activity; note that DepMap CRISPR shows no short-term TERT dependency in CNS lines (median -0.00), consistent with telomerase acting over many divisions rather than as an acute essential gene. | weak | [E18c](#e18c), [E18d](#e18d), [E18e](#e18e), [E04a](#e04a), [E17](#e17) |

Predictions: Allele-specific GABPA/GABPB1 ChIP or CUT&RUN signal on the mutant but not the wild-type allele in heterozygous C250T lines; GABPB1L or GABPA knockdown selectively lowers TERT mRNA in C250T lines but not in promoter-wild-type lines; Luciferase reporter gains activity with the A allele and the gain is abolished by mutating the created GGAA core; No acute proliferation defect on TERT loss in short-term CRISPR screens, with a delayed crisis phenotype on long passage

Falsified if: No allele-specific GABP occupancy at the mutant promoter; TERT expression unchanged after GABPA/GABPB1 depletion in C250T-mutant cells; Reporter assays show no gain of activity for the A/T allele

### 2. H5: Null: no TF-mediated allelic effect of this base; recurrence reflects a mutational hotspot or a linked haplotype variant (p = 0.23)

Null chain: no TF-mediated effect of this variant.

Predictions: Luciferase and base-edited isogenic lines show no reproducible difference in TERT promoter activity between G and A; No allele-specific TF occupancy by ChIP/CUT&RUN at the mutant allele; Any association is carried by a linked promoter variant such as rs2853669, whose cis/trans configuration modulates TERT level and survival; GERP -4.69 indicates no constraint at this base, consistent with a passenger at a UV/CpG-prone position

Falsified if: Isogenic base-edited lines show allele-specific gain of TERT promoter activity or expression; Allele-specific TF binding is demonstrated at the mutant promoter

### 3. H2: A different, highly expressed ETS factor (ETS1 or ELK/ETV class) is the functional binder at the created site (p = 0.10)

TF ETS1 (stated coverage mapped; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | G003 predicts a large concordant alt-allele gain for the whole Ets specificity group; ETS1 is covered only through CIS-BP-mapped models (no own passing model) and is selected within the group solely because it is the most highly expressed covered member in glioblastoma lines (61.0 TPM). This is a binding prediction plus expression, and the evidence cannot distinguish ETS1 from ERF, ELK1/3 or ETV5. | weak | [E05](#e05), [E06](#e06) |
| element | The gained site sits in the active promoter-like cCRE of TERT; nothing in the evidence is ETS1-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | Occupancy at this cCRE would act on TERT, whose TSS coincides with the variant. | weak | [E02](#e02) |
| cell_type | ETS1 is abundant in glioblastoma lines, a lineage in which TERTp mutations are frequent. | weak | [E06](#e06), [E04f](#e04f) |
| phenotype | Any ETS-driven reactivation of TERT raises telomerase and supports continued proliferation in the tumour types listed. | weak | [E18c](#e18c), [E18e](#e18e), [E04a](#e04a) |

Predictions: ETS1 (or ELK1/ERF), not GABPA, shows allele-specific occupancy at the mutant promoter; ETS1 knockdown lowers mutant-allele TERT while GABPB1 knockdown does not; Monomeric ETS binding suffices; no requirement for a second native ETS site

Falsified if: GABPB1L depletion abolishes mutant TERT expression while ETS1 depletion does not; No ETS1 occupancy detectable at the TERT promoter

### 4. H3: An ELF-class ETS factor (ELF1) with the strongest predicted gain binds the created site (p = 0.07)

TF ELF1 (stated coverage own_model; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ELF1 has its own passing model in G003 (z 164.2, alt binds more), close to the group best. Groups G020 and G345 give even larger per-model effects (ELF3 effect 5.17; SPDEF 2.18) but their named factors are essentially unexpressed in glioblastoma (<0.5 TPM), so within those specificities the expressed covered members are ELF1/ELF2/ELF4. ELF1 is chosen by expression plus own-model rank; this remains a binding prediction alone with no ChIP support at this site. | weak | [E06](#e06), [E07](#e07), [E08](#e08) |
| element | The site is in the TERT promoter-like cCRE with high DNase and H3K4me3 across biosamples. | supported | [E03](#e03) |
| gene | TERT is the gene whose TSS coincides with this cCRE. | weak | [E02](#e02) |
| cell_type | ELF1 is expressed in glioblastoma lines (17.4 TPM) while the epithelial members ELF3/ELF5/SPDEF are not; the evidence contains no bladder or melanoma expression data, so lineage-specific claims cannot be made. | weak | [E06](#e06), [E07](#e07), [E08](#e08) |
| phenotype | Increased TERT transcription from the mutant promoter sustains telomerase and tumour cell proliferation. | weak | [E18c](#e18c), [E04a](#e04a) |

Predictions: ELF1 ChIP shows allele-specific gain at the mutant promoter; ELF1 depletion lowers mutant TERT expression independently of GABP; TERT induction by the mutation persists in GABPB1L-null cells

Falsified if: ELF1 depletion has no effect on mutant TERT expression; Only GABP occupancy is detected at the mutant allele

### 5. H4: Loss of a repressor interaction (MBD1) at the mutated base de-represses TERT (p = 0.04)

TF MBD1 (stated coverage own_model; registry own_model), ref allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | MBD1 (31.5 TPM) has an own passing model predicting weaker alt binding (z -41.3, effect -1.24; ref at 100th, alt 98.6th percentile). Caveat: QBiC-SELEX models unmethylated DNA while MBD1's repressive role depends on methyl-CpG, and no methylation data are cited; the loss-of-repressor direction also runs opposite to the much larger ETS gain-of-binding signal. | weak | [E05](#e05), [E09](#e09) |
| element | The variant is in the TERT promoter cCRE; the evidence provides no CpG-island or methylation annotation for this element. | weak | [E01](#e01), [E03](#e03) |
| gene | Reduced repressor occupancy at this promoter would raise TERT; no evidence cited links MBD1 to TERT. | missing | [E02](#e02) |
| cell_type | MBD1 is expressed in glioblastoma lines; whether the TERT promoter is MBD1-repressed there is untested in the cited evidence. | missing | [E09](#e09) |
| phenotype | De-repression of TERT would raise telomerase activity, the proposed consequence of hotspot promoter mutations; the cited literature attributes this to new TF sites and displacement of negative regulators, so a repressor-loss route is possible but not demonstrated for this base. | weak | [E18e](#e18e) |

Predictions: MBD1 or repressive marks occupy the wild-type but not the mutant allele; MBD1 knockout raises TERT in promoter-wild-type cells, partially phenocopying the mutation; Mutant TERT induction survives combined ETS-factor depletion

Falsified if: TERT induction by the mutation requires GABP/ETS factors and is unaffected by MBD1 loss; No allelic difference in MBD1 occupancy or promoter methylation

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Luciferase reporter of the TERT promoter fragment, G vs A allele, in glioblastoma cells | low | yes | A allele gives clear gain of activity; gain lost if the created GGAA core is destroyed | No reproducible difference between alleles | A allele gives gain (same direction as H1) | A allele gives gain (same direction as H1) | Little or no gain on unmethylated plasmid; gain only if the reporter is methylated in vitro |
| Allele-specific GABPA/GABPB1 ChIP or CUT&RUN in heterozygous C250T glioblastoma lines | medium | yes | Strong mutant-allele-biased GABPA/GABPB1 signal | No allele-specific occupancy by any factor | GABPA signal not allele-biased; ETS1/ELK1 signal is | GABPA signal not allele-biased; ELF1 signal is | No allelic ETS bias; MBD1/repressive-mark bias toward the reference allele |
| GABPB1L knockdown vs ETS1, ELF1 and MBD1 knockdown, measuring allele-specific TERT mRNA | medium | yes | Only GABPB1L/GABPA loss reduces mutant-allele TERT | No knockdown changes allele-specific TERT | Only ETS1/ELK loss reduces mutant-allele TERT | Only ELF1 loss reduces mutant-allele TERT | No ETS knockdown effect; MBD1 loss raises TERT from the reference allele |
| Base editing the mutation into a TERTp-wild-type line and reverting it in a C250T line; measure TERT mRNA and telomerase | high | yes | Introduction raises TERT; reversion lowers it; effect GABP-dependent | No change in TERT on introduction or reversion | Same direction, ETS1-dependent | Same direction, ELF1-dependent | Effect appears only in methylated/repressed chromatin context |
| Bisulfite/methylation profiling of the TERT promoter plus MBD1 ChIP at the site | medium | no | No informative methylation difference required | No allelic methylation or MBD1 difference | No informative methylation difference required | No informative methylation difference required | CpG methylation present on the reference allele with MBD1 occupancy lost on the mutant allele |
| Re-inspection of existing ENCODE GABPA ChIP peaks and QBiC model detail at this position | existing data | no | GABPA peaks contain the site (observed, HepG2 and SK-N-SH) and GABPA has an own alt-gain model | Peaks in wild-type cells show binding without the variant, i.e. no allelic claim | Compatible, since GABPA peaks could reflect the general ETS-bound promoter in wild-type cells | Compatible, same caveat | Unaffected |

## Next experiment

Transient luciferase reporter assay in a TERTp-wild-type glioblastoma line comparing the G and A promoter fragments (plus a version with the created GGAA core destroyed). It is the cheapest test that separates H1 (allele-specific gain of promoter activity, lost when the ETS core is destroyed) from the null H5 (no allelic difference).

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": null})
- gene_dependency({"gene": "TERT"})
- literature_search({"query": "GABP TERT promoter mutation C250T C228T allele-specific recruitment glioblastoma"})

## Flags

- coverage_misstated: H2: stated mapped, registry says own_model for ETS1

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

> QBiC-SELEX screen of chr5:1295135:G>A: 997 models scored, 477 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 350 CIS-BP groups. Expression context: DepMap subtype median Glioblastoma. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 77 (C2H2 ZF, 1 model z -27.15, C2H2 ZF, 1 model z -21.76, bHLH, 1 model z -21.51, Homeodomain, 1 model z -19.2, Myb/SANT, 1 model z -18.88). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e06"></a>**E06** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 167.5, effect 2.421 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: ETV5 z 167.5, ELF1 z 164.23, ELF4 z 110.16, GABPA z 71.32, ELK4 z 62.15 (+13 more). TFs this group covers (own and CIS-BP-mapped models): ETS1 61.01 TPM, ERF 39.81 TPM, ELK3 30.24 TPM, ELK1 26.81 TPM, ETV5 22.15 TPM, ETS2 21.07 TPM, ELF2 18.42 TPM, ELF1 17.41 TPM, GABPA 15.52 TPM, ELF4 15.44 TPM (+15 more); best model's site strength: ref 94.8th, alt 99.9th percentile of its k-mer coefficients.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G020 (Ets, 4 models): best model ELF3_NA_TCCGTG20NTGC_ESY_yang2017_0_4_7mer (own model of ELF3), z 114.84, effect 5.168 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: ELF3 z 114.84, ELF5 z 107.44, ETV7 z 49.98, ETV6 z 46.24. TFs this group covers (own and CIS-BP-mapped models): ERF 39.81 TPM, ELF2 18.42 TPM, ELF1 17.41 TPM, ELF4 15.44 TPM, ETV6 5.65 TPM, ELF3 0.47 TPM, ETV7 0.31 TPM, EHF 0.17 TPM, SPI1 0.05 TPM, ELF5 0.03 TPM (+1 more); best model's site strength: ref 99.3th, alt 100.0th percentile of its k-mer coefficients.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G345 (Ets, 1 model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (own model of SPDEF), z 78.05, effect 2.184 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SPDEF z 78.05. TFs this group covers (own and CIS-BP-mapped models): ELF2 18.42 TPM, ELF1 17.41 TPM, ELF4 15.44 TPM, SPDEF 0.05 TPM; best model's site strength: ref 99.2th, alt 100.0th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G229 (MBD; CxxC ZF, 1 model): best model MBD1_FL_TG40NTGATCT_YWQA_jolma2025_0_3_7mer (own model of MBD1), z -41.31, effect -1.236 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: MBD1 z -41.31. TFs this group covers (own and CIS-BP-mapped models): MBD1 31.48 TPM; best model's site strength: ref 100.0th, alt 98.6th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G557 (C2H2 ZF, 1 model): best model ZNF654_DBD_AG40NTGGCTA_YWIA_jolma2025_0_4_7mer (own model of ZNF654), z -35.62, effect -0.857 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF654 z -35.62. TFs this group covers (own and CIS-BP-mapped models): ZNF654 6.42 TPM; best model's site strength: ref 100.0th, alt 99.1th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G620 (C2H2 ZF, 1 model): best model ZNF92_FL_TC40NAATCTC_YWIA_jolma2025_0_3_7mer (own model of ZNF92), z -33.21, effect -0.623 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF92 z -33.21. TFs this group covers (own and CIS-BP-mapped models): ZNF92 9.63 TPM; best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G409 (C2H2 ZF, 1 model): best model ZBTB5_FL_GA40NACTTTG_YWQA_jolma2025_0_2_7mer (own model of ZBTB5), z -24.38, effect -0.68 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB5 z -24.38. TFs this group covers (own and CIS-BP-mapped models): ZBTB5 7.43 TPM; best model's site strength: ref 100.0th, alt 99.5th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G066 (EBF1, 2 models): best model EBF1_NA_TATAAG20NCG_AC_jolma2013_1_3_7mer (own model of EBF1), z -24.35, effect -0.646 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: EBF1 z -24.35. TFs this group covers (own and CIS-BP-mapped models): EBF1 3.13 TPM, EBF4 2.58 TPM, EBF2 0.02 TPM, EBF3 0.01 TPM; best model's site strength: ref 99.9th, alt 99.7th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G612 (C2H2 ZF, 1 model): best model ZNF845_DBD2_GC40NAGAGTT_YWIA_jolma2025_0_3_7mer (own model of ZNF845), z -24.25, effect -0.358 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF845 z -24.25. TFs this group covers (own and CIS-BP-mapped models): ZNF845 3.41 TPM; best model's site strength: ref 100.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G575 (C2H2 ZF, 1 model): best model ZNF706_FL_CT40NTCTAGT_YWSA_jolma2025_0_3_7mer (own model of ZNF706), z -23.53, effect -0.618 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF706 z -23.53. TFs this group covers (own and CIS-BP-mapped models): ZNF706 81.43 TPM; best model's site strength: ref 100.0th, alt 99.4th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295135:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e17"></a>**E17** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for TERT (0 = no effect, -1 = median common-essential; < -0.5 called dependent). CNS/Brain lineage, 50 lines: median -0.00, 2% dependent. All 1183 lines: median -0.02, 1% dependent.

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABP%20TERT%20promoter%20mutation%20C250T%20C228T%20allele-specific%20recruitment%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:27:27+00:00)

> Europe PMC: 17 hits for 'GABP TERT promoter mutation C250T C228T allele-specific recruitment glioblastoma'; top 8 with PMIDs:
> PMID 38201248 (2023): The Biological and Clinical Role of the Telomerase Reverse Transcriptase Gene in Glioblastoma: A Potential Therapeutic Target?
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 35903534 (2022): TERT Promoter Mutations and Telomerase in Melanoma.
> PMID 38285162 (2024): Mechanisms of telomere maintenance and associated therapeutic vulnerabilities in malignant gliomas.
> PMID 36979671 (2023): Deciphering the Functions of Telomerase Reverse Transcriptase in Head and Neck Cancer.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 32981294 (2020): Mechanisms of TERT Reactivation and Its Interaction with BRAFV600E.
> PMID 27028424 (2016): Telomerase reactivation in cancers: Mechanisms that govern transcriptional activation of the wild-type vs. mutant TERT promoters.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 38201248 (https://europepmc.org/article/MED/38201248; retrieved 2026-10-25T17:27:27+00:00)

> The telomerase reverse transcriptase gene (TERT) is the most frequently altered gene in solid tumors, including brain tumors and GBM IDH-wildtype.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-25T17:27:27+00:00)

> Specifically, AURKB, via REST, is recruited to TERTp MUT by TRIM28.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 35903534 (https://europepmc.org/article/MED/35903534; retrieved 2026-10-25T17:27:27+00:00)

> A growing number of recent studies suggest that the most common mutations in the TERT promoter (ATG start site -124C>T and -146C>T) are associated with increased TERT mRNA expression, telomerase activity, telomere length, and poor prognosis.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 36979671 (https://europepmc.org/article/MED/36979671; retrieved 2026-10-25T17:27:27+00:00)

> Two major hotspot TERT promoter mutations (C228T and C250T) have been reported in different malignancies such as melanoma, genitourinary cancers, CNS tumors, hepatocellular carcinoma, thyroid cancers, sarcomas, and HNCs.

<a id="e18e"></a>**E18e** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-25T17:27:27+00:00)

> These mutations promote TERT gene expression by multiple mechanisms, including the generation of novel binding sites for nuclear transcription factors, displacement of negative regulators from DNA G-quadruplexes, recruitment of epigenetic activators and disruption of long-range interactions between TERT locus and telomeres.
