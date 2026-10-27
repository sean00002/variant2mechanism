# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 122 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. GABPA_alt: GABPA binds the alt allele and activates TERT (p = 0.44)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element The variant lies in ENSR5_832QG TERT promoter and promoter-like cCRE EH38E3622530, consistent with an allele-dependent promoter element (E01, E03).; gene TERT; cell type Glioblastoma DepMap context has GABPA expressed (median 15.52 TPM, rank 303/1626, 58.4th percentile), and TERT promoter mutations are reported across glioblastoma, melanoma and bladder cancer (E04, E05c, E05f, E07)..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele is predicted to create a de novo ETS-family motif and bind GABPA more strongly than ref G. GABPA ChIP-seq peaks containing this position in HepG2 and SK-N-SH show that GABPA can occupy the site, although this is not allele-resolved and no glioblastoma GABPA peak is reported; absence of a glioblastoma peak may reflect no GABPA experiment in that biosample. GABPA QBiC-SELEX coverage is not_checked: no QBiC-SELEX screen row or qbic_tf_detail lookup is supplied. | weak | [E05d](#e05d), [E06](#e06) |
| element | The variant lies in the TERT promoter and a promoter-like cCRE, consistent with an allele-dependent promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | This promoter element is at the TERT TSS and is annotated near TERT, making TERT the direct target gene. | supported | [E02](#e02), [E03](#e03) |
| cell_type | Glioblastoma is the supplied expression context; GABPA is expressed in DepMap glioblastoma, and TERT promoter mutations are reported in glioblastoma, melanoma and bladder cancer. | weak | [E04](#e04), [E05c](#e05c), [E05f](#e05f), [E07](#e07) |
| phenotype | If alt-enhanced GABPA binding increases TERT transcription, it is predicted to raise telomerase activity and support tumor progression. Literature supports TERT promoter mutations as activating and poor-prognosis lesions, but does not by itself prove GABPA-specific allelic activation. | weak | [E05a](#e05a), [E05f](#e05f), [E05g](#e05g) |

Predictions: GABPA ChIP-qPCR or allele-specific EMSA shows stronger GABPA binding to the alt allele than the ref allele.; In a ref/alt TERT reporter in GABPA-expressing glioblastoma cells, the alt allele gives higher activity and GABPA knockdown or ETS-motif mutation reduces the alt-dependent signal.

Falsified if: Allele-specific GABPA binding at this site is not detectable in a heterozygous glioblastoma line.; GABPA knockdown or mutation of the predicted ETS motif does not reduce alt-dependent TERT reporter activity.

### 2. null: Null: no TF-mediated allelic effect (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific GABPA, ETS1, or ELK1 binding at this site.; Any TERT expression or disease association is due to a linked causal variant, a passenger mutation at a mutational hotspot, or no allelic effect.

Falsified if: Reproducible alt-specific GABPA binding and GABPA-dependent allelic TERT reporter/expression are demonstrated in a relevant cell type.; A linked causal variant is excluded and the alt allele itself reproducibly drives TF-dependent TERT expression.

### 3. ETS1_alt: ETS1 binds the alt allele and activates TERT (p = 0.15)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element The variant lies in ENSR5_832QG TERT promoter and promoter-like cCRE EH38E3622530, consistent with an allele-dependent promoter element (E01, E03).; gene TERT; cell type Glioblastoma is the supplied expression context; TERT promoter mutations are reported in these cancers, but no ETS1-specific expression or allele-specific activity evidence is supplied (E04, E05c, E05f)..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele may create an ETS-family motif, but there is no ETS1-specific allele-binding evidence; E05d supports de novo ETS-family motifs generally, not ETS1 specifically. ETS1 QBiC-SELEX coverage is not_checked: no QBiC-SELEX screen row or qbic_tf_detail lookup is supplied. | missing | none |
| element | The variant lies in the TERT promoter and a promoter-like cCRE, consistent with an allele-dependent promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | This promoter element is at the TERT TSS and is annotated near TERT, making TERT the direct target gene. | supported | [E02](#e02), [E03](#e03) |
| cell_type | Glioblastoma is the supplied expression context; TERT promoter mutations are reported in these cancers, but ETS1-specific activity in this context is not established by the supplied evidence. | missing | [E04](#e04), [E05c](#e05c), [E05f](#e05f) |
| phenotype | If alt-enhanced ETS1 binding increases TERT transcription, it is predicted to raise telomerase activity and support progression. The supplied literature supports TERT promoter mutation activation generally, not ETS1-specific allelic activation. | weak | [E05a](#e05a), [E05f](#e05f), [E05g](#e05g) |

Predictions: ETS1 ChIP or allele-specific EMSA shows stronger ETS1 binding to the alt allele than the ref allele.; ETS1 knockdown reduces alt-dependent TERT reporter activity more than ref-dependent activity.

Falsified if: Allele-specific ETS1 binding at this site is not detectable.; ETS1 knockdown or ETS-motif mutation does not reduce alt-dependent TERT reporter activity.

### 4. ELK1_alt: ELK1 binds the alt allele and activates TERT (p = 0.11)

TF ELK1 (stated coverage not_checked; registry own_model), alt allele binds more; element The variant lies in ENSR5_832QG TERT promoter and promoter-like cCRE EH38E3622530, consistent with an allele-dependent promoter element (E01, E03).; gene TERT; cell type Glioblastoma is the supplied expression context; TERT promoter mutations are reported in these cancers, but no ELK1-specific expression or allele-specific activity evidence is supplied (E04, E05c, E05f)..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt A allele may create an ETS-family motif, but there is no ELK1-specific allele-binding evidence; E05d supports de novo ETS-family motifs generally, not ELK1 specifically. ELK1 QBiC-SELEX coverage is not_checked: no QBiC-SELEX screen row or qbic_tf_detail lookup is supplied. | missing | none |
| element | The variant lies in the TERT promoter and a promoter-like cCRE, consistent with an allele-dependent promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | This promoter element is at the TERT TSS and is annotated near TERT, making TERT the direct target gene. | supported | [E02](#e02), [E03](#e03) |
| cell_type | Glioblastoma is the supplied expression context; TERT promoter mutations are reported in these cancers, but ELK1-specific activity in this context is not established by the supplied evidence. | missing | [E04](#e04), [E05c](#e05c), [E05f](#e05f) |
| phenotype | If alt-enhanced ELK1 binding increases TERT transcription, it is predicted to raise telomerase activity and support progression. The supplied literature supports TERT promoter mutation activation generally, not ELK1-specific allelic activation. | weak | [E05a](#e05a), [E05f](#e05f), [E05g](#e05g) |

Predictions: ELK1 ChIP or allele-specific EMSA shows stronger ELK1 binding to the alt allele than the ref allele.; ELK1 knockdown reduces alt-dependent TERT reporter activity more than ref-dependent activity.

Falsified if: Allele-specific ELK1 binding at this site is not detectable.; ELK1 knockdown or ETS-motif mutation does not reduce alt-dependent TERT reporter activity.

## Prediction matrix

| Test | Cost | Separates top two | GABPA_alt | null | ETS1_alt | ELK1_alt |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA or GABPA ChIP-qPCR with ref and alt oligos in a glioblastoma line heterozygous for the variant | low | yes |  |  |  |  |
| Ref/alt TERT luciferase reporter in glioblastoma cells with GABPA knockdown or ETS-motif mutation | medium | yes |  |  |  |  |
| ETS1 and ELK1 allele-specific ChIP/EMSA or knockdown in the same reporter system | medium | no |  |  |  |  |
| Allele-specific TERT expression or telomerase activity measurement in heterozygous tumor lines or patient samples | high | yes |  |  |  |  |
| Fine-mapping or sequencing of linked variants at the TERT locus to exclude a linked causal variant | high | yes |  |  |  |  |

## Next experiment

The cheapest first-pass experiment separating GABPA_alt from null is an allele-specific EMSA with recombinant GABPA (or GABPA ChIP-qPCR in a heterozygous glioblastoma line) using ref and alt oligos: GABPA_alt predicts alt > ref binding, while null predicts no allele-specific GABPA binding.

## Investigate calls

- literature_search({"query": "TERT promoter C228T GABPA allele-specific binding ETS motif mutant"})
- chip_peaks({"biosample": "glioblastoma", "tf": "GABPA"})
- tf_expression({"context": "DepMap:subtype=Glioblastoma", "tf": "GABPA"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 0.87 of links cite only evidence that passed every check.

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

<a id="e05"></a>**E05** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20C228T%20GABPA%20allele-specific%20binding%20ETS%20motif%20mutant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T01:35:12+00:00)

> Europe PMC: 28 hits for 'TERT promoter C228T GABPA allele-specific binding ETS motif mutant'; top 8 with PMIDs:
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 39557834 (2024): Mechanistic basis of atypical TERT promoter mutations.
> PMID 41639451 (2026): Regulatory grammar in human promoters uncovered by MPRA-based deep learning.
> PMID 36713366 (2022): <i>TERT</i> promoter mutations and methylation for telomerase activation in urothelial carcinomas: New mechanistic insights and clinical significance.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 36394204 (2022): Thyroid carcinoma-featured telomerase activation and telomere maintenance: Biology and translational/clinical significance.
> PMID 38285162 (2024): Mechanisms of telomere maintenance and associated therapeutic vulnerabilities in malignant gliomas.
> PMID 38030698 (2023): Functional analysis of recurrent CDC20 promoter variants in human melanoma.

<a id="e05a"></a>**E05a** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T01:35:12+00:00)

> Telomere length maintenance, critical for cancer progression, can be driven by TERT promoter mutations (TERTp MUT ), which are markers of poor prognosis across multiple cancers.

<a id="e05b"></a>**E05b** literature_search, Europe PMC abstract, PMID 40822359 (https://europepmc.org/article/MED/40822359; retrieved 2026-10-26T01:35:12+00:00)

> Specifically, AURKB, via REST, is recruited to TERTp MUT by TRIM28.

<a id="e05c"></a>**E05c** literature_search, Europe PMC abstract, PMID 39557834 (https://europepmc.org/article/MED/39557834; retrieved 2026-10-26T01:35:12+00:00)

> Non-coding mutations in the TERT promoter (TERTp), typically at one of two bases -124 and -146 bp upstream of the start codon, are among the most prevalent driver mutations in human cancer.

<a id="e05d"></a>**E05d** literature_search, Europe PMC abstract, PMID 39557834 (https://europepmc.org/article/MED/39557834; retrieved 2026-10-26T01:35:12+00:00)

> Canonical TERTp mutations create de novo binding sites for ETS family transcription factors that induce favourable conditions for DNA damage formation by UV light, thus creating a hotspot effect but only after a first mutational hit.

<a id="e05e"></a>**E05e** literature_search, Europe PMC abstract, PMID 36713366 (https://europepmc.org/article/MED/36713366; retrieved 2026-10-26T01:35:12+00:00)

> Recent mechanistic explorations have revealed important roles for TERT promoter mutations and aberrant methylation in activation of TERT transcription and telomerase in UCs.

<a id="e05f"></a>**E05f** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T01:35:12+00:00)

> Point mutations in the core promoter region of the telomerase reverse transcriptase (TERT) gene have been found to occur at high frequencies in several tumour types and considered a primary cause of telomerase reactivation in cancer cells.

<a id="e05g"></a>**E05g** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-26T01:35:12+00:00)

> These mutations promote TERT gene expression by multiple mechanisms, including the generation of novel binding sites for nuclear transcription factors, displacement of negative regulators from DNA G-quadruplexes, recruitment of epigenetic activators and disruption of long-range interactions between TERT locus and telomeres.

<a id="e05h"></a>**E05h** literature_search, Europe PMC abstract, PMID 36394204 (https://europepmc.org/article/MED/36394204; retrieved 2026-10-26T01:35:12+00:00)

> The genomic alterations of the TERT loci including TERT promoter's gain-of-function mutations, copy number gain, fusion and rearrangements, have recently been identified in TCs as mechanisms to induce TERT expression and to activate telomerase.

<a id="e05i"></a>**E05i** literature_search, Europe PMC abstract, PMID 36394204 (https://europepmc.org/article/MED/36394204; retrieved 2026-10-26T01:35:12+00:00)

> Importantly, numerous studies have consistently shown that TERT promoter mutations and TERT expression occur in all TC subtypes, and are robustly associated with TC malignancy, aggressiveness, treatment failure and poor outcomes.

<a id="e05j"></a>**E05j** literature_search, Europe PMC abstract, PMID 38030698 (https://europepmc.org/article/MED/38030698; retrieved 2026-10-26T01:35:12+00:00)

> Melanoma is heavily burdened by non-coding variants, representing over 99% of total genetic variation, including the well-characterized TERT promoter mutation.

<a id="e05k"></a>**E05k** literature_search, Europe PMC abstract, PMID 38030698 (https://europepmc.org/article/MED/38030698; retrieved 2026-10-26T01:35:12+00:00)

> We found that variants in the promoter of CDC20, which putatively disrupt an ETS motif, lead to lower transcriptional activity in reporter assays.

<a id="e06"></a>**E06** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T11:58:44+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295113:G>A in biosamples matching 'glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e07"></a>**E07** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> GABPA in DepMap subtype median Glioblastoma: 15.52 TPM, rank 303 of 1626 TFs (1 = highest); this context is at the 58.4th percentile of GABPA across all DepMap lines; median of 54 lines.
