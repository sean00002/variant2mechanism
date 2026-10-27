# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 213 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H4_null: No TF-mediated effect of rs34768248; association may reflect linkage or weak/passenger annotation (p = 0.65)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific GABPA or CTCF binding at chr5:1295601.; No allele-specific effect on TERT expression or chromatin in relevant cells.; Any disease association is explained by a linked causal variant or the broader TERT/CLPTM1L locus, not by this base change.

Falsified if: A reproducible allele-specific TF binding difference is shown at rs34768248.; The variant reproducibly changes TERT expression or regulatory activity in relevant cancer cells.

### 2. H1_GABPA_alt: Alt A may strengthen a GABPA/ETS site in the TERT upstream enhancer and increase TERT in TERT-dependent cancers (p = 0.18)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT upstream enhancer/promoter cCRE region; gene TERT; cell type GABPA-expressing glioblastoma/melanoma/bladder cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: alt A strengthens a GABPA/ETS site at chr5:1295601. No QBiC-SELEX row for GABPA was provided, so coverage is not_checked. GABPA is expressed in DepMap glioblastoma (median 15.52 TPM), but ENCODE GABPA ChIP-seq has no peak containing the variant in the cited 'null' biosamples; absence is not conclusive and no allele-specific binding assay is given. | missing | [E07](#e07), [E09](#e09) |
| element | The variant lies in an ENSR5 enhancer and within 500 bp of pELS/PLS cCREs near TERT, although no cCRE directly overlaps the variant. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest TSS at 0.5 kb and the best L2G gene, but the credible set is hypertension with PIP 0.00 and E04 reports no GWAS Catalog association for rs34768248; TERT assignment is therefore indirect. | weak | [E02](#e02), [E05](#e05), [E04](#e04) |
| cell_type | GABPA is expressed in the DepMap glioblastoma context, and TERT has broad literature relevance in melanoma/glioblastoma, but the evidence does not establish a GABPA-TERT axis in bladder cancer or in the cited DepMap subtype. | weak | [E09](#e09), [E06](#e06) |
| phenotype | If alt A increased GABPA-driven TERT expression, higher telomerase activity could promote TERT-dependent cancer phenotypes; however, E06 is only generic TERT/telomerase literature and gives no rs34768248-specific or allele-specific phenotype evidence. | weak | [E06](#e06) |

Predictions: Allele-specific GABPA binding is higher for alt A than ref G at chr5:1295601.; TERT expression or regulatory activity is higher in cells carrying alt A, especially GABPA-expressing glioblastoma/melanoma/bladder cancer lines.; GABPA knockdown or mutation of the ETS site reduces the alt-A-specific effect.

Falsified if: No allele-specific GABPA binding is detected at chr5:1295601.; TERT expression or regulatory activity does not differ by allele in GABPA-expressing relevant cells.; GABPA knockdown or ETS-site mutation does not reduce any alt-A-specific effect.

### 3. H3_CTCF_alt: Alt A may alter CTCF occupancy near the TERT upstream cCRE and change chromatin insulation or promoter-enhancer contact (p = 0.10)

TF CTCF (stated coverage not_checked; registry own_model), alt allele binds more; element TERT upstream enhancer/promoter cCRE region with nearby CTCF signal; gene TERT; cell type glioblastoma/melanoma/bladder cancer cells with CTCF occupancy near TERT.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: alt A strengthens a CTCF site at chr5:1295601. No QBiC-SELEX row for CTCF was provided, so coverage is not_checked. E03 reports CTCF signal at nearby pELS/PLS cCREs, but no cCRE overlaps the variant and no allele-specific CTCF assay is given. | weak | [E03](#e03) |
| element | The variant lies in an ENSR5 enhancer near pELS/PLS cCREs with CTCF signal, but the CTCF z-scores are maxima over ENCODE biosamples and no cCRE directly overlaps the variant. | supported | [E01](#e01), [E03](#e03) |
| gene | The element is near TERT and TERT is the best L2G gene, but the credible set is hypertension with PIP 0.00 and no molecular QTL, so a CTCF-to-TERT regulatory link is speculative. | weak | [E02](#e02), [E05](#e05) |
| cell_type | TERT has broad cancer literature relevance, but CTCF-dependent TERT regulation, bladder cancer relevance, and the DepMap glioblastoma context are not established by the cited evidence. | weak | [E06](#e06) |
| phenotype | Allele-specific CTCF occupancy could alter TERT promoter-enhancer contacts and TERT expression, but E06 provides only generic TERT literature and no evidence linking this variant, CTCF, and cancer phenotype. | weak | [E06](#e06) |

Predictions: CTCF binding is higher for alt A than ref G at chr5:1295601.; Alt A changes chromatin contact or insulator behavior around the TERT promoter.; TERT expression changes in a CTCF-dependent manner.

Falsified if: CTCF does not bind the variant-containing sequence allele-specifically.; No chromatin-contact or TERT expression difference is seen with alt A.; CTCF depletion does not modify any allele effect.

### 4. H2_GABPA_ref: Ref G may be the stronger GABPA/ETS site; alt A may reduce GABPA binding and TERT expression (p = 0.07)

TF GABPA (stated coverage not_checked; registry own_model), ref allele binds more; element TERT upstream enhancer/promoter cCRE region; gene TERT; cell type GABPA-expressing glioblastoma/melanoma/bladder cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: ref G preserves a stronger GABPA/ETS site than alt A. No QBiC-SELEX row for GABPA was provided, so coverage is not_checked. GABPA is expressed in DepMap glioblastoma, but no allele-specific GABPA ChIP, EMSA, or reporter data are given; E07 reports no GABPA ChIP peak containing the variant in the cited 'null' biosamples. | missing | [E07](#e07), [E09](#e09) |
| element | The variant lies in an ENSR5 enhancer and near pELS/PLS cCREs at TERT, making an allele-specific regulatory effect plausible, though no cCRE directly overlaps the variant. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest TSS and best L2G gene, but the credible set is hypertension with PIP 0.00 and no GWAS Catalog association is reported for rs34768248, so the TERT link is indirect. | weak | [E02](#e02), [E05](#e05), [E04](#e04) |
| cell_type | TERT is broadly relevant in some cancers in the literature, and GABPA is expressed in DepMap glioblastoma, but bladder-specific and GABPA-dependent TERT regulation are not shown. | weak | [E06](#e06), [E09](#e09) |
| phenotype | If alt A reduced GABPA-driven TERT expression, telomerase activity would fall; this chain requires the alt allele to be protective or disease risk to act in the opposite direction, but no such direction or protective-allele evidence is provided. | missing | none |

Predictions: Allele-specific GABPA binding is higher for ref G than alt A at chr5:1295601.; TERT expression or regulatory activity is lower in cells carrying alt A.; Restoring the GABPA site reverses the alt-A-associated reduction.

Falsified if: GABPA binds alt A more strongly than ref G at chr5:1295601.; TERT expression or regulatory activity is not lower with alt A in relevant cells.; The variant has no allele-specific effect on the element.

## Prediction matrix

| Test | Cost | Separates top two | H4_null | H1_GABPA_alt | H3_CTCF_alt | H2_GABPA_ref |
| --- | --- | --- | --- | --- | --- | --- |
| Recombinant GABPA EMSA or DNA pulldown with ref vs alt oligos spanning chr5:1295601 | low | yes | No allele-specific GABPA binding. | Alt A shows stronger recombinant GABPA binding than ref G. | No GABPA-specific allele difference; CTCF is not tested by this assay. | Ref G shows stronger recombinant GABPA binding than alt A. |
| Allele-specific GABPA ChIP-qPCR in a heterozygous GABPA-expressing glioblastoma cell line | medium | yes | No allele-specific GABPA occupancy. | GABPA ChIP is higher on the alt A haplotype. | No GABPA allele effect; CTCF may show an allele effect if this chain is true. | GABPA ChIP is higher on the ref G haplotype. |
| TERT upstream enhancer/promoter MPRA or luciferase assay with ref vs alt in GABPA-expressing glioblastoma cells | medium | yes | No allele-specific reporter activity. | Alt A increases reporter activity in GABPA-expressing glioblastoma cells. | No simple GABPA-dependent change; any effect may be CTCF/contact-mediated. | Alt A decreases reporter activity. |
| CTCF EMSA or allele-specific CTCF ChIP at chr5:1295601 | low | no | No allele-specific CTCF binding. | No CTCF allele-specific binding. | Alt A shows stronger CTCF binding than ref G. | No CTCF allele-specific binding. |
| Allele-specific TERT expression or eQTL analysis in heterozygous glioblastoma, melanoma, and bladder cancer samples | high | yes | No allele-specific TERT expression effect. | Alt A is associated with higher TERT expression. | No simple expression effect, or an effect explained by chromatin contact rather than GABPA. | Alt A is associated with lower TERT expression. |

## Next experiment

Recombinant GABPA EMSA or DNA pulldown with ref vs alt oligos spanning chr5:1295601 is the cheapest test that separates the top two chains, H1_GABPA_alt and H4_null. H1 predicts stronger GABPA binding to alt A; the null predicts no allele-specific GABPA binding.

## Investigate calls

- chip_peaks({"tf": "GABPA", "biosample": "null"})
- eqtl_lookup({"tissue": "null"})
- tf_expression({"tf": "GABPA", "context": "DepMap:subtype=Glioblastoma"})

## Flags

- literature_fallback: no hits for 'rs34768248 AND TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; dropped the rsID
- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 0.93 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295601-1295601:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:22:30+00:00)

> Variant chr5:1295601:G>A (GRCh38), allele string G/A
> Known IDs: rs34768248
> Most severe consequence: intron_variant
> Regulatory features: ENSR5_C5GP enhancer
> GERP conservation score at the site: 2.04
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295601-2295601?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:22:31+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295601:G>A, by distance to TSS:
> TERT: 0.5 kb from TSS (upstream, strand -1)
> CLPTM1L: 49.5 kb from TSS (downstream, strand -1)
> SLC6A18: 70.2 kb from TSS (downstream, strand +1)
> SLC6A19: 94.0 kb from TSS (downstream, strand +1)
> SLC12A7: 139.4 kb from TSS (upstream, strand -1)
> SLC6A3: 149.9 kb from TSS (downstream, strand -1)
> LPCAT1: 228.7 kb from TSS (downstream, strand -1)
> NKD2: 287.6 kb from TSS (downstream, strand +1)
> TRIP13: 402.8 kb from TSS (downstream, strand +1)
> BRD9: 402.8 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:21:44+00:00)

> No cCRE overlaps the variant; nearest is EH38E3622531 (pELS) 75 bp away.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622532 pELS: DNase z 2.2, H3K27ac z 3.9, H3K4me3 z 4.4, CTCF z 1.5; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622530 PLS: DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs34768248&size=100; retrieved 2026-10-26T02:22:30+00:00)

> 0 GWAS Catalog associations for rs34768248, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:22:30+00:00)

> 1 credible sets contain 5_1295601_G_A: 1 GWAS, 0 molecular QTL.
> GWAS Hypertension: PIP 0.00; L2G TERT 0.84
> Best L2G gene scores across these sets: TERT 0.84

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:24:02+00:00)

> No ENCODE GABPA ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'null'. Absence can also mean no GABPA experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295601_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:24:03+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295601_G_A_b38 in tissues matching 'null'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e09"></a>**E09** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> GABPA in DepMap subtype median Glioblastoma: 15.52 TPM, rank 303 of 1626 TFs (1 = highest); this context is at the 58.4th percentile of GABPA across all DepMap lines; median of 54 lines.
