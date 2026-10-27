# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.51 over 7 model calls; 165 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1: C228T creates a de novo GGAA ETS site bound by GABPA (with GABPB1), reactivating TERT (p = 0.66)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS), chr5:1294945-1295294; gene TERT; cell type Glioblastoma tumour cells (also melanoma, bladder urothelium).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ENCODE GABPA ChIP-seq peaks in two biosamples (HepG2, SK-N-SH) directly contain chr5:1295113, so GABPA occupies this base; within the ETS/GGAA specificity group GABPA is chosen on this direct occupancy evidence plus its expression in glioblastoma (15.52 TPM, rank 303/1626 TFs), not on memory alone. The alt (A) allele is predicted to bind more strongly because it converts the sequence to a GGAA ETS core, but no QBiC-SELEX row or allele-specific binding assay was provided, so the direction of the allelic effect is inferred, not shown, and coverage is not_checked. Note the peaks are from non-glioblastoma, likely wild-type-promoter lines, so they show GABPA can reach this promoter region but not allele specificity. | weak | [E05](#e05), [E06](#e06), [E01](#e01) |
| element | The variant lies inside an active promoter-like cCRE (EH38E3622530, PLS; DNase z 4.8, H3K4me3 z 4.5, H3K27ac z 4.2) annotated as the TERT promoter; these z-scores are maxima over ENCODE biosamples, not glioblastoma-specific. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT's TSS is 0.0 kb from the variant and the cCRE is annotated to TERT; all other protein-coding genes are >=50 kb away. This is proximity plus promoter annotation only, with no eQTL or perturbation link for this somatic base. | weak | [E02](#e02), [E03](#e03) |
| cell_type | The relevant cells are IDH wild-type glioblastoma and melanoma tumour cells, where TERT promoter mutations are among the most frequent alterations (50-82% of melanoma), and where GABPA is expressed at 15.52 TPM (58.4th percentile across DepMap lines). No evidence here is specific to bladder. | weak | [E04a](#e04a), [E04f](#e04f), [E06](#e06) |
| phenotype | Reactivated TERT restores telomerase activity and prevents replicative senescence, permitting unlimited proliferation; conversely, lowering TERT triggers senescence in melanoma cells. The senescence evidence is from a USP10/FOXM1 study, not from this variant. | weak | [E04a](#e04a), [E04e](#e04e) |

Predictions: GABPA/GABPB1 CUT&RUN in C228T-heterozygous glioblastoma lines shows reads at this base skewed to the A allele; GABPA or GABPB1 knockdown lowers TERT mRNA and telomerase activity selectively in C228T-mutant lines; Reporter A allele gives several-fold higher TERT promoter activity, abolished by destroying the created GGAA core; The gain requires a second native ETS site nearby (GABP tetramer requirement)

Falsified if: No allele-specific GABPA/GABPB1 occupancy in sensitive allele-resolved assays; GABPA/GABPB1 depletion leaves TERT unchanged in C228T-mutant cells; The A allele gives no reporter gain

### 2. H5: Null: no TF-mediated allelic effect of this base; association reflects linked variation or co-occurring alterations (p = 0.16)

Null chain: no TF-mediated effect of this variant.

Predictions: Isogenic reporter and base-editing experiments show no allele-specific difference in TERT promoter activity; TERT expression differences between mutant and wild-type tumours track the rs2853669 haplotype or co-occurring alterations such as CDKN2A deletion rather than this base; No allele-specific TF occupancy is detected at chr5:1295113

Falsified if: Isogenic introduction of the A allele alone raises TERT expression and telomerase activity; Allele-specific TF occupancy and allele-specific TERT transcription are demonstrated at this base

### 3. H2: The created GGAA site is bound mainly by ETS1 rather than GABPA, activating TERT (p = 0.10)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma and melanoma cells with high ETS1.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele creates a GGAA core read by the shared ETS specificity group; within that group ETS1 is selected on measured expression (61.01 TPM, rank 43/1626 TFs in glioblastoma, 73.9th percentile), which is far higher than GABPA, and because ETS1 binds single GGAA sites without GABP's tetramer requirement. No ETS1 ChIP peak at this base and no QBiC-SELEX row were provided, so coverage is not_checked and binding is inferred. | weak | [E07](#e07) |
| element | The created site lies in the active TERT promoter cCRE with strong DNase/H3K4me3/H3K27ac maxima. | weak | [E03](#e03) |
| gene | TERT is at 0 kb and is the cCRE's annotated gene; proximity only. | weak | [E02](#e02), [E03](#e03) |
| cell_type | ETS1 is abundantly expressed in glioblastoma lines, and TERT promoter mutations are frequent in melanoma and IDH-wt GBM, so an ETS1-driven effect is plausible in these lineages. | weak | [E07](#e07), [E04a](#e04a), [E04f](#e04f) |
| phenotype | Increased TERT transcription sustains telomerase and blocks senescence. | weak | [E04a](#e04a), [E04e](#e04e) |

Predictions: ETS1 knockdown reduces mutant-allele TERT while GABPA/GABPB1 knockdown does not; Allele-specific ETS1 ChIP/CUT&RUN signal at chr5:1295113; Effect size tracks ETS1 rather than GABPB1 expression across lines

Falsified if: GABPA/GABPB1 depletion, not ETS1 depletion, abolishes mutant TERT expression; No ETS1 occupancy at the mutant promoter

### 4. H3: The created ETS site is bound by a TCF-class factor (ELK4/ELK1), making TERT induction MAPK-dependent (p = 0.05)

TF ELK4 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma cells with active RTK/RAS/MAPK signalling.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The GGAA core created by the alt allele is also the recognition sequence of ternary complex factors; ELK4 is picked within the ETS group as a MAPK-responsive member, which would make the new site signalling-dependent. No ChIP peak, expression lookup or QBiC-SELEX row for ELK4 was provided, so this choice rests on literature knowledge only and coverage is not_checked. | missing | none |
| element | The site lies in the promoter-like cCRE containing the TERT TSS. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT, 0 kb from the variant, is the regulated gene; proximity only. | weak | [E02](#e02) |
| cell_type | IDH wild-type glioblastoma, where TERT promoter mutations are frequent, is the proposed context; no evidence here shows MAPK activity or ELK4 expression in these cells. | missing | [E04f](#e04f) |
| phenotype | Signal-dependent TERT induction maintains telomeres and prevents senescence. | weak | [E04a](#e04a), [E04e](#e04e) |

Predictions: MEK/ERK inhibition selectively reduces TERT output from the mutant allele; ELK1/ELK4 ChIP shows mutant-allele-specific occupancy, with no GABPA allele skew; Serum or growth-factor stimulation changes mutant-allele TERT more than wild-type

Falsified if: Mutant-allele TERT is insensitive to MAPK inhibition; No TCF-class ETS occupancy at the site while GABPA shows allele-specific occupancy

### 5. H4: The ref G allele binds a repressive factor whose loss de-represses TERT (p = 0.03)

TF ZNF143 (stated coverage not_checked; registry own_model), ref allele binds more; element TERT core promoter cCRE EH38E3622530 (PLS); gene TERT; cell type Glioblastoma, melanoma and bladder tumour cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Under this alternative the G>A change destroys a ref-preferring site for a repressive promoter factor such as ZNF143, so activation would be loss of repression rather than gain of an ETS site. No binding evidence of any kind supports this: the only ChIP data at this base are GABPA peaks, which argue for the activator-gain reading. Coverage is not_checked and the TF choice is a placeholder. | missing | [E05](#e05) |
| element | The variant lies in the TERT promoter cCRE; the CTCF z of 2.0 is a weak maximum over biosamples and does not itself indicate repressor occupancy. | weak | [E03](#e03) |
| gene | TERT's TSS coincides with the element; proximity only. | weak | [E02](#e02), [E03](#e03) |
| cell_type | TERT is repressed in normal somatic cells and reactivated in these tumour types; the cited evidence gives mutation frequency, not loss of a repressor. | missing | [E04a](#e04a) |
| phenotype | De-repression of TERT restores telomerase and blocks senescence. | weak | [E04a](#e04a), [E04e](#e04e) |

Predictions: Footprinting or ChIP shows a factor occupying the ref but not the alt promoter; Destroying the created GGAA core without restoring the ref base still yields high activity; Knockdown of the candidate repressor raises TERT from the wild-type allele to mutant-like levels

Falsified if: Disrupting the created GGAA core abolishes the activity gain; No factor shows preferential ref-allele occupancy

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-resolved GABPA/GABPB1 CUT&RUN at chr5:1295113 in C228T-heterozygous glioblastoma lines | medium | yes | Strong read skew toward the A allele | No allele-specific occupancy by any factor | Little or no GABPA skew; ETS1 shows the skew instead | No GABPA skew; ELK1/ELK4 skew | No gained occupancy; any skew favours the ref allele for another factor |
| Luciferase reporter with ref vs alt 300 bp TERT promoter, plus a version with the created GGAA core destroyed | low | no | Alt > ref several-fold; gain lost when GGAA core is destroyed | No difference between ref and alt | Alt > ref, gain lost when GGAA core is destroyed (same as H1) | Alt > ref, gain lost when GGAA destroyed and attenuated by MEK inhibitor | Alt > ref but gain persists when GGAA core is destroyed |
| siRNA/degron knockdown of GABPA, GABPB1 and ETS1 separately, measuring TERT mRNA in C228T-mutant vs wild-type lines | medium | yes | GABPA/GABPB1 loss lowers TERT only in mutant lines; ETS1 loss has little effect | No mutant-specific effect of any knockdown | ETS1 loss lowers TERT in mutant lines; GABPA/GABPB1 loss does not | Neither alone is sufficient; TERT falls with MEK inhibition | No activator knockdown effect specific to mutant lines |
| Base editing of A back to G at chr5:1295113 in an isogenic C228T-mutant glioblastoma line | high | no | TERT mRNA and telomerase activity drop sharply | TERT essentially unchanged | TERT drops sharply (same as H1) | TERT drops, with residual MAPK dependence | TERT drops, and the repressor regains occupancy |
| MEK/ERK inhibitor treatment with allele-specific TERT transcript readout | low | no | Mutant-allele TERT largely unchanged | No allele-specific transcript to measure | Modest or no change | Marked selective loss of mutant-allele TERT | No selective change |
| DepMap CRISPR dependency of GABPA, GABPB1 and ETS1 across TERT-promoter-mutant vs wild-type glioblastoma lines | existing data | yes | GABPA/GABPB1 dependency enriched in promoter-mutant lines | No dependency difference by promoter genotype | ETS1 dependency enriched instead | No enrichment for either; MAPK pathway genes enriched | No activator dependency enrichment |

## Next experiment

Query existing DepMap CRISPR dependency data for GABPA, GABPB1 and ETS1, stratifying glioblastoma lines by TERT promoter mutation status: this costs nothing, and a mutant-selective GABPA/GABPB1 versus ETS1 dependency separates H1 from H2 before any bench work (confirm with allele-resolved GABPA CUT&RUN).

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": null})
- tf_expression({"tf": "GABPA", "context": "DepMap:subtype=Glioblastoma"})
- tf_expression({"tf": "ETS1", "context": "DepMap:subtype=Glioblastoma"})

## Flags

- none

Citation support: 0.95 of links cite only evidence that passed every check.

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

<a id="e05"></a>**E05** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295113:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e06"></a>**E06** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> GABPA in DepMap subtype median Glioblastoma: 15.52 TPM, rank 303 of 1626 TFs (1 = highest); this context is at the 58.4th percentile of GABPA across all DepMap lines; median of 54 lines.

<a id="e07"></a>**E07** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> ETS1 in DepMap subtype median Glioblastoma: 61.01 TPM, rank 43 of 1626 TFs (1 = highest); this context is at the 73.9th percentile of ETS1 across all DepMap lines; median of 54 lines.
