# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.50 over 7 model calls; 154 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: C250T creates a de novo ETS site bound by GABPA (with GABPB1), activating the TERT promoter (p = 0.62)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS), chr5:1294945-1295294; gene TERT; cell type Glioblastoma tumour cells (IDH-wildtype).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The G>A change is predicted to create an ETS core (GGAA) and the alt allele is proposed to bind more strongly. Within the ETS binding-specificity group I pick GABPA because ENCODE ChIP-seq shows GABPA peaks that physically contain chr5:1295135 in two biosamples (HepG2, SK-N-SH) and because GABPA is well expressed in glioblastoma lines (rank 303/1626 TFs). Caveat: those ChIP peaks are from cells presumed wild-type at this position, so they show the promoter is a GABPA-occupied region but not an allele-specific gain; no QBiC-SELEX row or detail lookup was available, so coverage is not_checked and the allele direction remains an inference, not a measurement. | weak | [E05](#e05), [E06](#e06), [E01](#e01) |
| element | The variant lies in an active promoter-like element (Ensembl ENSR5_832QG; ENCODE cCRE EH38E3622530, PLS) with high DNase, H3K4me3 and H3K27ac maxima across biosamples; z-scores are maxima, not glioblastoma-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | The element is the TERT core promoter (TERT TSS 0.0 kb; TERT listed as nearby gene for the cCRE), so TERT is the most likely cis target rather than CLPTM1L (50 kb). This is proximity plus promoter annotation only, with no eQTL or CRISPRi link. | weak | [E02](#e02), [E03](#e03) |
| cell_type | TERT promoter mutations are among the most frequent alterations in IDH-wildtype glioblastoma, and GABPA is expressed in the glioblastoma DepMap context (15.52 TPM, 58th percentile across lines), so the proposed activator is present where the mutation occurs. The literature quote does not name C250T specifically. | weak | [E04f](#e04f), [E06](#e06) |
| phenotype | Increased TERT transcription would restore telomerase activity and avert senescence; TERT promoter mutations are the commonest noncoding alteration in melanoma and loss of TERT triggers senescence. Note DepMap short-term CRISPR shows essentially no TERT dependency (median -0.00 in CNS lines), consistent with telomere-driven phenotypes being slow and not captured in such screens. | weak | [E04a](#e04a), [E04e](#e04e), [E07](#e07) |

Predictions: Allele-specific GABPA/GABPB1 CUT&RUN or ChIP shows occupancy on the mutant allele in C250T heterozygous lines; GABPA or GABPB1L knockdown lowers TERT mRNA in C250T-mutant but not wild-type lines; Reporter assays show the alt allele raises promoter activity, abolished by disrupting the created GGAA core

Falsified if: No allele-specific GABP occupancy at chr5:1295135 in mutant cells; GABPA/GABPB1 depletion leaves TERT mRNA unchanged in C250T-mutant cells while another ETS factor's depletion lowers it

### 2. H0: Null: no TF-mediated allelic effect of this variant at this site (p = 0.18)

Null chain: no TF-mediated effect of this variant.

Predictions: Reporter or base-edited isogenic assays show no allele-specific TERT promoter activity; No allele-specific TF footprint or occupancy difference at chr5:1295135; GABPA peaks are present on both alleles equally; TERT expression tracks with a linked variant (e.g. rs2853669 haplotype), amplification or methylation rather than with C250T

Falsified if: Luciferase or base-edited isogenic lines show a reproducible allele-specific increase in TERT promoter activity; Allele-specific TF binding is demonstrated at the mutant site

### 3. H2: The created GGAA site is bound mainly by ETS1, driving TERT in MAPK-active tumours (p = 0.10)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Melanoma cells with active MAPK signalling (and glioblastoma).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Within the same ETS binding-specificity group, ETS1 rather than GABPA occupies the new site on the alt allele. No evidence provided shows ETS1 binding here; the only overlapping ChIP data name GABPA, which argues against this pick. No ETS1 expression value or QBiC row was supplied, so coverage is not_checked. | missing | none |
| element | The new site lies in an active promoter-like cCRE; this is generic element context, not ETS1-specific. | weak | [E03](#e03) |
| gene | The element is the TERT TSS, so any factor acting there acts in cis on TERT. | weak | [E02](#e02) |
| cell_type | Melanoma carries TERT promoter mutations in 50-82% of cases; MAPK-driven ETS activity in melanoma is asserted from prior knowledge, not from cited evidence. | weak | [E04a](#e04a) |
| phenotype | Elevated TERT sustains telomerase activity in melanoma, where telomerase activation is a major molecular feature. | weak | [E04a](#e04a) |

Predictions: ETS1 knockdown, not GABPA knockdown, reduces mutant-allele TERT expression; MEK inhibition reduces mutant-promoter activity in proportion to ETS1 occupancy; Allelic effect is larger in melanoma lines than in glioblastoma lines

Falsified if: ETS1 ChIP/CUT&RUN shows no enrichment at the mutant promoter; ETS1 depletion leaves TERT mRNA unchanged while GABPA depletion lowers it

### 4. H3: A ternary-complex factor (ELK1/ELK3/ELK4 group, representative ELK4) reads the de novo site and activates TERT (p = 0.06)

TF ELK4 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The created GGAA core matches the TCF/ELK specificity shared by ELK1/ELK3/ELK4; ELK4 is named only as a representative of that redundant group, so the within-group choice is weak and no cited data support it. The one ChIP dataset overlapping the variant names GABPA, not an ELK factor. Coverage not_checked. | missing | none |
| element | Any such binding would occur in the active promoter-like element containing the variant. | weak | [E03](#e03) |
| gene | TERT is the gene whose TSS coincides with the element (0.0 kb). | weak | [E02](#e02) |
| cell_type | TERT promoter mutations are frequent in IDH-wildtype glioblastoma; no ELK-family expression evidence in this context was provided. | weak | [E04f](#e04f) |
| phenotype | Higher TERT prevents senescence and supports tumour growth. | weak | [E04e](#e04e) |

Predictions: ELK-family, not GABP, occupancy at the mutant allele in ChIP/CUT&RUN; Serum or MAPK stimulation modulates mutant-allele TERT output; Only combined ELK1/ELK3/ELK4 knockdown lowers mutant-allele TERT (redundancy), single knockdowns do nothing

Falsified if: No TCF-family binding is detected at the site; Single GABPA/GABPB1 depletion fully abolishes the mutant-allele effect

### 5. H4: The ref allele binds a repressive factor (CTCF-type) that the mutation destroys, de-repressing TERT (p = 0.04)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element TERT core promoter cCRE EH38E3622530, which shows modest CTCF signal (z 2.0); gene TERT; cell type Glioblastoma and bladder tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Instead of gain of an activator, the G>A change weakens binding of a repressive factor on the ref allele; CTCF is named only because the containing cCRE has a modest CTCF z-score (2.0, a maximum over biosamples). No allele-specific or CTCF-motif evidence supports this, and the overlapping ChIP evidence names GABPA, which is an activator-gain model. Coverage not_checked. | missing | [E03](#e03) |
| element | The variant lies in the promoter-like element that also carries low CTCF signal across biosamples; context only, not allele-specific. | weak | [E03](#e03) |
| gene | Loss of repression at this element would raise TERT, the gene at the element. | weak | [E02](#e02) |
| cell_type | TERT promoter mutations are enriched in IDH-wildtype glioblastoma; the cited quotes do not mention bladder or silenced telomerase. | weak | [E04f](#e04f) |
| phenotype | De-repressed TERT would enable telomere maintenance; this is generic and not specific to repressor loss. | weak | [E04a](#e04a), [E04e](#e04e) |

Predictions: Allele-specific repressor (CTCF) ChIP signal is higher on the ref allele; Repressor knockdown raises TERT in wild-type but not mutant cells; No new activator footprint appears at the mutant allele

Falsified if: ChIP shows equal or higher CTCF binding on the alt allele, or no CTCF footprint at the site; A gain-of-binding activator footprint (e.g. GABP) is demonstrated at the mutant allele

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA/GABPB1 CUT&RUN in C250T-heterozygous glioblastoma or melanoma lines | medium | yes | Strong mutant-allele-biased GABPA/GABPB1 signal at chr5:1295135 | No allelic bias in occupancy for any factor | No GABPA allelic bias; signal instead from ETS1 | No GABPA allelic bias; ELK-family signal instead | No activator gain; any allelic bias favours ref allele (CTCF) |
| Luciferase reporter of the 250-bp TERT promoter, ref vs alt, with and without disruption of the created GGAA core | low | no | Alt > ref activity; gain lost when GGAA core is disrupted | No reproducible difference between ref and alt | Alt > ref, GGAA-dependent, but larger in MAPK-high melanoma background | Alt > ref, GGAA-dependent, and serum/MAPK-responsive | Alt > ref only in cells expressing the repressor; GGAA disruption has no effect |
| siRNA/CRISPRi knockdown panel (GABPA, GABPB1L, ETS1, ELK1/3/4) with TERT mRNA readout in C250T-mutant vs wild-type lines | medium | yes | GABPA/GABPB1L knockdown lowers TERT selectively in mutant lines | No knockdown produces a mutant-specific TERT change | ETS1 knockdown lowers TERT in mutant lines; GABPA knockdown does not | Only combined ELK1/3/4 knockdown lowers TERT in mutant lines | No activator knockdown matters; CTCF knockdown raises TERT in wild-type lines |
| QBiC-SELEX detail lookup for GABPA, ETS1 and ELK4 at chr5:1295135 (predicted allelic binding change and coverage) | existing data | yes | GABPA (own model or mapped) predicts a large alt-allele gain | No model predicts a meaningful allelic binding change | ETS1 model predicts the largest alt gain of the group | ELK-family model predicts the largest alt gain | CTCF model predicts a ref-allele loss of binding |
| CTCF ChIP-seq / allele-specific CTCF signal at the TERT promoter in mutant lines | medium | no | No allele-specific CTCF signal | No allele-specific CTCF signal | No allele-specific CTCF signal | No allele-specific CTCF signal | Ref-allele-biased CTCF occupancy |

## Next experiment

Run the QBiC-SELEX detail lookup (existing data, no bench cost) for GABPA versus ETS1 at chr5:1295135: it reports coverage and the predicted direction and magnitude of the allelic binding change for each factor, directly separating H1 from H2 before committing to the more expensive allele-specific CUT&RUN or knockdown panel.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": null})
- tf_expression({"tf": "GABPA", "context": null})
- gene_dependency({"gene": "TERT"})

## Flags

- none

Citation support: 0.90 of links cite only evidence that passed every check.

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

<a id="e05"></a>**E05** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295135:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e06"></a>**E06** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> GABPA in DepMap subtype median Glioblastoma: 15.52 TPM, rank 303 of 1626 TFs (1 = highest); this context is at the 58.4th percentile of GABPA across all DepMap lines; median of 54 lines.

<a id="e07"></a>**E07** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for TERT (0 = no effect, -1 = median common-essential; < -0.5 called dependent). CNS/Brain lineage, 50 lines: median -0.00, 2% dependent. All 1183 lines: median -0.02, 1% dependent.
