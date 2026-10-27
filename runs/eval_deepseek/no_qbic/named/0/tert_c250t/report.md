# TERT promoter C250T and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 7 model calls; 118 s.

Variant `chr5:1295135:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H0: Null: no allele-specific TF-mediated effect at C250T; recurrent somatic TERT promoter hotspot or linked causal variant. (p = 0.48)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding difference between ref G and alt A at C250T; No allele-specific effect on TERT expression attributable to this variant; Disease association is explained by the recurrent somatic TERT promoter hotspot or a linked causal variant, not by a TF-mediated allelic effect

Falsified if: Robust allele-specific TF binding at C250T is demonstrated and perturbing that TF changes TERT expression in the relevant cell context; The disease association is shown to be caused by this allele acting through a TF rather than by the recurrent somatic hotspot or a linked causal variant

### 2. H1: C250T is proposed to strengthen a GABPA-bound ETS site and increase TERT in glioblastoma. (p = 0.27)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter PLS cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA is nominated as the ETS-family TF, and the alt A allele is predicted to bind GABPA more strongly. E05 shows GABPA ChIP peaks containing the variant in HepG2 and SK-N-SH, but no GABPA peak in glioblastoma and no allele-specific binding test. QBiC-SELEX coverage for GABPA is not_checked because no screen row or qbic_tf_detail lookup was supplied. | weak | [E05](#e05) |
| element | The variant lies in the TERT promoter ENSR5_832QG and in promoter-like cCRE EH38E3622530, so a putative ETS-site change would act in a TERT promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.0 kb from its TSS upstream on the minus-strand gene; CLPTM1L is 50 kb away. | supported | [E01](#e01), [E02](#e02) |
| cell_type | The relevant cell type is glioblastoma per the case context, but E03 gives maxima over ENCODE biosamples rather than glioblastoma-specific activity, and E05 provides no glioblastoma GABPA peak; glioblastoma-specific GABPA occupancy is therefore unproven. | missing | [E03](#e03), [E05](#e05) |
| phenotype | TERT activation is a plausible oncogenic mechanism in glioblastoma, and E04 contains general TERT-glioblastoma literature, but no C250T-specific or GABPA-specific TERT activation evidence is supplied. | weak | [E04](#e04) |

Predictions: Allele-specific GABPA ChIP-qPCR, EMSA or reporter assays show alt A > ref G at C250T in glioblastoma cells; GABPA knockdown or knockout reduces TERT expression in glioblastoma cells carrying the alt allele; Disrupting the predicted ETS motif abolishes the allele-specific effect

Falsified if: No allele-specific GABPA binding is detectable at C250T in a relevant cellular context; GABPA perturbation does not change TERT expression in cells carrying the alt allele; Mutating the predicted ETS motif does not abolish any allele-specific effect

### 3. H3: C250T is proposed to weaken CTCF binding at the TERT promoter cCRE, altering promoter architecture and TERT expression. (p = 0.15)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element TERT promoter PLS cCRE EH38E3622530; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is nominated as the architectural TF, and the ref G allele is predicted to bind CTCF more strongly than alt A. E03 gives only a maximum CTCF z-score of 2.0 in the containing cCRE, and E07 reports no CTCF peak containing the variant in glioblastoma but 2 CTCF peaks containing it in DOHH2 and endodermal cells; neither test is allele-specific. QBiC-SELEX coverage for CTCF is not_checked because no screen row or qbic_tf_detail lookup was supplied. | weak | [E03](#e03), [E07](#e07) |
| element | The variant lies in promoter-like cCRE EH38E3622530 and the TERT promoter ENSR5_832QG, so a CTCF change would affect a TERT promoter/architectural element. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene at 0.0 kb from its TSS, and E01 annotates the variant as upstream of TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | The supplied context is glioblastoma, but E03 lacks glioblastoma-specific CTCF occupancy or cCRE activity, and E07 provides no glioblastoma CTCF peak; glioblastoma-specific CTCF action is therefore unproven. | missing | [E03](#e03), [E07](#e07) |
| phenotype | Altered TERT promoter architecture could change TERT expression and contribute to glioblastoma, but E04 links TERT to glioblastoma only generally and does not establish a CTCF-dependent mechanism or the direction of TERT expression change. | weak | [E04](#e04) |

Predictions: Allele-specific CTCF ChIP shows ref G > alt A at C250T in glioblastoma cells; The alt allele changes promoter contact or insulation in glioblastoma cells; CTCF depletion alters TERT expression or promoter architecture in the presence of the ref allele

Falsified if: No allele-specific CTCF binding difference is detected at C250T; CTCF perturbation does not alter TERT promoter architecture or TERT expression; The ref allele does not preserve a functional CTCF site better than the alt allele

### 4. H2: C250T is proposed to strengthen an ETS1-bound ETS site and increase TERT in melanoma or bladder cancer. (p = 0.10)

TF ETS1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter PLS cCRE EH38E3622530; gene TERT; cell type Melanoma and bladder cancer.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETS1 is an alternative ETS-family TF, and the alt A allele is predicted to bind ETS1 more strongly. E06 reports no ETS1 ChIP peak containing the variant in melanoma and no peak within 100 bp without containing it, so ETS1 occupancy at this element is unsupported. QBiC-SELEX coverage for ETS1 is not_checked because no screen row or qbic_tf_detail lookup was supplied. | missing | [E06](#e06) |
| element | The variant is in the TERT promoter ENSR5_832QG and promoter-like cCRE EH38E3622530, placing any ETS1 effect at a TERT promoter element. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene at 0.0 kb from its TSS; E01 annotates the variant as upstream of TERT. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Melanoma and bladder cancer are in the case header, but E04 contains only general TERT/melanoma literature with no bladder-specific top hit, and E06 provides no melanoma ETS1 occupancy; cell-type-specific ETS1 action is not established. | missing | [E04](#e04), [E06](#e06) |
| phenotype | TERT activation is linked generally to melanoma in E04, but there is no C250T- or ETS1-specific TERT activation evidence in melanoma or bladder cancer. | weak | [E04](#e04) |

Predictions: ETS1 binds the alt allele more strongly than ref at C250T in melanoma or bladder assays; ETS1 knockdown reduces TERT expression in cells carrying the alt allele; The effect is weaker or absent in glioblastoma compared with a GABPA-dependent effect

Falsified if: ETS1 does not bind the alt allele more strongly than ref in melanoma or bladder assays; ETS1 perturbation does not alter TERT expression in cells carrying the alt allele; The variant shows no ETS1-dependent allele-specific effect in the relevant disease context

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA ChIP-qPCR at C250T in heterozygous glioblastoma cells | low | yes | No reproducible allelic difference in GABPA ChIP signal at C250T | Alt A shows stronger GABPA ChIP signal than ref G at C250T in glioblastoma cells | No GABPA-specific allelic difference | No GABPA-specific allelic difference; ETS1, if tested separately, would be the relevant factor |
| GABPA knockdown or knockout in glioblastoma cells carrying the alt allele, measuring TERT expression | medium | yes | No change in TERT expression | TERT expression decreases | No GABPA-dependent TERT decrease | No or weaker TERT decrease than for GABPA |
| Allele-specific ETS1 ChIP-qPCR at C250T in melanoma cells | low | no | No reproducible allelic difference | No ETS1-specific allelic difference | No ETS1-specific allelic difference | Alt A shows stronger ETS1 ChIP signal than ref G at C250T in melanoma cells |
| Allele-specific CTCF ChIP-qPCR at C250T in glioblastoma cells | low | no | No reproducible allelic difference | No CTCF-specific allelic difference | Ref G shows stronger CTCF ChIP signal than alt A at C250T in glioblastoma cells | No CTCF-specific allelic difference |
| TERT promoter reporter assay with ref versus alt allele and ETS-motif mutation in glioblastoma cells | medium | yes | No allele-specific reporter difference | Alt A increases reporter activity, and ETS-motif mutation abolishes the increase | Ref allele shows higher CTCF-dependent architectural or reporter effect | An allele-specific increase may be seen, but it is not GABPA-dependent and requires ETS1 perturbation to support H2 |

## Next experiment

Allele-specific GABPA ChIP-qPCR at C250T in heterozygous glioblastoma cells is the cheapest experiment that separates H0 from H1: H1 predicts alt A > ref G GABPA binding, whereas H0 predicts no reproducible allelic difference.

## Investigate calls

- chip_peaks({"biosample": "glioblastoma", "tf": "GABPA"})
- chip_peaks({"biosample": "melanoma", "tf": "ETS1"})
- chip_peaks({"biosample": "glioblastoma", "tf": "CTCF"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

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

<a id="e05"></a>**E05** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:26+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'glioblastoma'. Absence can also mean no GABPA experiment in that biosample. In other biosamples, 2 GABPA peaks do contain the variant: HepG2, SK-N-SH (experiments ENCSR000BJK, ENCSR000BTG).

<a id="e06"></a>**E06** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:35:22+00:00)

> No ENCODE ETS1 ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'melanoma'. Absence can also mean no ETS1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:35:22+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr5:1295135:G>A in biosamples matching 'glioblastoma'. Absence can also mean no CTCF experiment in that biosample. In other biosamples, 2 CTCF peaks do contain the variant: DOHH2, endodermal cell (experiments ENCSR084RDK, ENCSR398RET).
