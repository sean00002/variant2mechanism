# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.06 over 9 model calls; 245 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H1_GABPA_gain: GABPA gain-of-binding at the C228T ETS site activates TERT (p = 0.45)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter cCRE; gene TERT; cell type GABPA.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA occupies the TERT promoter element containing C228T in ENCODE HepG2 and SK-N-SH ChIP-seq peaks (E06), and GABPA is expressed in glioblastoma DepMap lines (E07); the alt A allele is the expected stronger GABPA/ETS binder, but the supplied evidence lacks an allele-specific GABPA binding assay. | weak | [E06](#e06), [E07](#e07) |
| element | The variant lies in promoter-like cCRE EH38E3622530, and GABPA occupancy of this element (E06) makes an allele-specific GABPA site a plausible modulator of TERT promoter activity; direct reporter or MPRA evidence is absent. | weak | [E01](#e01), [E03](#e03), [E06](#e06) |
| gene | The cCRE is at the TERT TSS (0.0 kb) and is annotated near TERT, consistent with TERT as the target gene; direct CRISPR or reporter evidence for this element is absent. | weak | [E02](#e02), [E03](#e03) |
| cell_type | GABPA is expressed in glioblastoma DepMap lines (E07), and TERT promoter mutations including C228T are common in glioblastoma and melanoma (E04a, E04d, E04g); melanoma GABPA expression or occupancy is not supplied. | weak | [E07](#e07), [E04a](#e04a), [E04d](#e04d), [E04g](#e04g) |
| phenotype | TERT promoter mutations and telomerase activation are associated with tumor progression in melanoma and glioblastoma (E04a, E04b, E04d, E04g, E04h); this supports a general TERT/telomerase phenotype, not GABPA-specific causality. | weak | [E04a](#e04a), [E04b](#e04b), [E04d](#e04d), [E04g](#e04g), [E04h](#e04h) |

Predictions: Allele-specific GABPA EMSA or ChIP shows stronger GABPA binding to the alt A allele than the ref G allele at C228T.; A TERT promoter reporter carrying C228T has higher activity than ref, and this gain is reduced by GABPA knockdown.; GABPA loss reduces TERT expression or telomerase activity preferentially in C228T-mutant tumor cells.

Falsified if: Allele-specific GABPA binding is not detected at C228T in glioblastoma or melanoma cells.; GABPA knockdown or loss does not reduce TERT expression or telomerase activity from the alt allele.; A TERT promoter reporter carrying C228T does not show higher activity than ref, or the gain is not GABPA-dependent.

### 2. H0_null: No TF-mediated allelic effect; linked or passenger explanation (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding or promoter activity difference is found between ref and alt at C228T.; TERT expression in tumors is explained by linked variants such as rs2853669 in cis (E04e), by other TERT promoter mutations (E04d, E04h), or by passenger/recurrent-mutation selection rather than by this allele's TF binding.

Falsified if: Allele-specific GABPA or ETS binding and mutant-specific TERT reporter activity are demonstrated at C228T.; GABPA or ETS loss reduces TERT expression only in C228T-mutant cells.

### 3. H3_CTCF_repressor_loss: Loss of a CTCF-associated repressive site at C228T derepresses TERT (p = 0.13)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element TERT promoter cCRE; gene TERT; cell type CTCF.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The cCRE has a CTCF z-score of 2.0 as a maximum over ENCODE biosamples (E03), suggesting CTCF may occupy the region; if so, the ref G allele could bind CTCF more strongly than the alt A allele, but this is not allele-specific and is not shown at the variant. | weak | [E03](#e03) |
| element | The variant lies in promoter-like cCRE EH38E3622530, which has some CTCF signal, so loss of a hypothetical repressive CTCF site could increase promoter activity; a repressive role is not established. | weak | [E01](#e01), [E03](#e03) |
| gene | The cCRE is at the TERT TSS and is annotated near TERT, consistent with TERT as the target gene; direct evidence that CTCF loss here derepresses TERT is absent. | weak | [E02](#e02), [E03](#e03) |
| cell_type | TERT promoter-mutant glioblastoma and melanoma are the relevant disease contexts (E04a, E04d, E04g), but no supplied evidence shows CTCF expression or CTCF-mediated repression in these tumor cells. | missing | [E04a](#e04a), [E04d](#e04d), [E04g](#e04g) |
| phenotype | Derepressed TERT would be expected to increase telomerase and support tumor progression; the supplied literature supports general TERT/telomerase biology, not CTCF-loss causality at C228T. | missing | [E04a](#e04a), [E04b](#e04b), [E04d](#e04d) |

Predictions: CTCF ChIP-seq or EMSA shows ref > alt binding at C228T.; CTCF knockdown increases TERT expression specifically from the ref promoter.

Falsified if: CTCF binding is not allele-specific at C228T.; CTCF loss does not derepress TERT, or the alt allele does not weaken CTCF binding.

### 4. H2_ELK1_gain: Alternative ETS factor ELK1 gains binding at C228T (p = 0.07)

TF ELK1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter cCRE; gene TERT; cell type ELK1.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele could create an ETS motif bound by ELK1, but no supplied evidence shows ELK1 occupancy, an ELK1 motif change, or allele-specific ELK1 binding at C228T. | missing | none |
| element | The variant lies in promoter-like cCRE EH38E3622530, so an ETS-factor gain here could in principle increase TERT promoter activity; direct ELK1-specific evidence is absent. | weak | [E01](#e01), [E03](#e03) |
| gene | The cCRE is at the TERT TSS and is annotated near TERT, consistent with TERT as the target gene; direct regulation by ELK1 is not shown. | weak | [E02](#e02), [E03](#e03) |
| cell_type | TERT promoter-mutant glioblastoma and melanoma are the relevant disease contexts (E04a, E04d, E04g), but no supplied evidence shows ELK1 expression, occupancy, or activity in these tumor cells. | missing | [E04a](#e04a), [E04d](#e04d), [E04g](#e04g) |
| phenotype | If ELK1 drove TERT expression, it would be expected to increase telomerase and support tumor maintenance; the supplied literature supports general TERT/telomerase biology, not ELK1-specific causality. | missing | [E04a](#e04a), [E04b](#e04b), [E04d](#e04d), [E04g](#e04g) |

Predictions: ELK1 ChIP-seq or EMSA shows allele-specific binding at C228T with alt > ref.; ELK1 depletion reduces TERT expression in cells carrying the mutant allele.

Falsified if: ELK1 does not bind the alt allele preferentially at C228T.; ELK1 depletion does not affect mutant TERT expression while GABPA loss does.

## Prediction matrix

| Test | Cost | Separates top two | H1_GABPA_gain | H0_null | H3_CTCF_repressor_loss | H2_ELK1_gain |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA EMSA or allele-specific GABPA ChIP at C228T using ref vs alt oligos or alleles in glioblastoma/melanoma cells | low | yes | alt > ref GABPA binding at C228T | no allele-specific GABPA binding; ref = alt | no GABPA allele-specific binding | no GABPA allele-specific binding; ELK1 not addressed |
| TERT promoter reporter assay with ref vs alt C228T allele, with and without GABPA knockdown | medium | yes | alt reporter higher than ref; GABPA knockdown reduces the alt-specific gain | no reproducible ref vs alt reporter difference | alt reporter higher than ref via CTCF loss; GABPA knockdown does not reduce the gain | alt reporter higher than ref via ELK1; GABPA knockdown does not reduce the gain |
| GABPA ChIP-seq in glioblastoma/melanoma cells for occupancy of the C228T-containing element | medium | no | GABPA peak at the element in glioblastoma/melanoma cells | GABPA peak may be present but would not establish an allelic effect | no GABPA peak expected at the element | no GABPA peak expected at the element |
| ELK1 ChIP-seq or EMSA at C228T | low | no | no ELK1 allele-specific binding expected | no ELK1 allele-specific binding | no ELK1 allele-specific binding expected | alt > ref ELK1 binding at C228T |
| Allele-specific CTCF EMSA or ChIP at C228T | low | no | no allele-specific CTCF binding expected | no allele-specific CTCF binding | ref > alt CTCF binding at C228T | no allele-specific CTCF binding expected |
| Genotype rs2853669 in cis and test whether TERT expression or reporter activity remains C228T allele-specific after conditioning on the linked haplotype | medium | yes | C228T/GABPA-associated effect remains after conditioning on rs2853669 genotype | TERT expression is explained by rs2853669 or linked haplotype, with no residual C228T allele-specific effect | C228T-associated effect remains and is CTCF-dependent | C228T-associated effect remains and is ELK1-dependent |

## Next experiment

Allele-specific GABPA EMSA using ref and alt C228T oligos, ideally with GABPA antibody in nuclear extract from a TERT-expressing glioblastoma or melanoma line; this is the cheapest test that directly separates H1_GABPA_gain (alt > ref GABPA binding) from H0_null (no allele-specific GABPA binding).

## Investigate calls

- literature_search({"query": "GABPA TERT promoter C228T allele-specific binding ETS"})
- chip_peaks({"biosample": null, "tf": "GABPA"})
- tf_expression({"context": "DepMap:subtype=Glioblastoma", "tf": "GABPA"})

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

<a id="e05"></a>**E05** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABPA%20TERT%20promoter%20C228T%20allele-specific%20binding%20ETS&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:28:52+00:00)

> Europe PMC: 41 hits for 'GABPA TERT promoter C228T allele-specific binding ETS'; top 8 with PMIDs:
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 39557834 (2024): Mechanistic basis of atypical TERT promoter mutations.
> PMID 37741952 (2023): Pooled genetic screens to identify vulnerabilities in TERT-promoter-mutant glioblastoma.
> PMID 36713366 (2022): <i>TERT</i> promoter mutations and methylation for telomerase activation in urothelial carcinomas: New mechanistic insights and clinical significance.
> PMID 40241101 (2025): The ability of anexelekto (AXL) expression and TERT promoter mutation to predict radioiodine-refractory differentiated thyroid carcinoma.
> PMID 41639451 (2026): Regulatory grammar in human promoters uncovered by MPRA-based deep learning.
> PMID 36394204 (2022): Thyroid carcinoma-featured telomerase activation and telomere maintenance: Biology and translational/clinical significance.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.

<a id="e05a"></a>**E05a** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T00:28:52+00:00)

> Telomere length maintenance, critical for cancer progression, can be driven by TERT promoter mutations (TERTp MUT ), which are markers of poor prognosis across multiple cancers.

<a id="e06"></a>**E06** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> 2 ENCODE GABPA ChIP-seq peaks contain chr5:1295113:G>A: biosamples HepG2, SK-N-SH; experiments ENCSR000BJK, ENCSR000BTG.

<a id="e07"></a>**E07** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> GABPA in DepMap subtype median Glioblastoma: 15.52 TPM, rank 303 of 1626 TFs (1 = highest); this context is at the 58.4th percentile of GABPA across all DepMap lines; median of 54 lines.
