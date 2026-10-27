# rs7001688 and LDL cholesterol

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 166 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. null_no_TF_effect: No TF-mediated effect; variant is nonfunctional or linked to an unrepresented causal variant (p = 0.97)

Null chain: no TF-mediated effect of this variant.

Predictions: no allele-specific TF binding at rs7001688; no reproducible association of rs7001688 with LDL cholesterol after accounting for linked variants; the variant behaves as a nonfunctional or passenger intronic/intergenic variant

Falsified if: a nearby linked variant is shown to be the causal LDL-cholesterol variant; allele-specific TF binding and a target-gene effect are demonstrated for rs7001688 in hepatocytes; rs7001688 is shown to be functional in a hepatocyte LDL-cholesterol assay

### 2. HNF4A_ref_CYP7A1: HNF4A binds ref G at a cryptic distal element and alters CYP7A1 (p = 0.01)

TF HNF4A (stated coverage not_checked; registry own_model), ref allele binds more; element cryptic distal HNF4A site in an intronic/intergenic segment; gene CYP7A1; cell type Hep3B2.1-7 hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HNF4A is proposed to bind the ref G allele more strongly than the alt T allele. No positive QBiC-SELEX, ChIP-seq, MPRA, or reporter evidence supports this. QBiC-SELEX coverage is not_checked because no QBiC-SELEX row or TF lookup was provided. E07 reports no ENCODE HNF4A ChIP-seq peak containing rs7001688, although absence can also reflect no HNF4A experiment in the relevant biosample; this remains a low-confidence motif hypothesis. | missing | [E07](#e07) |
| element | E01 places rs7001688 as an intron_variant/intergenic variant with no regulatory feature, and E03 reports no overlapping cCRE; the nearest cCRE is 1544 bp away. These support only the genomic location and absence of an annotated cCRE, not the existence of a functional cryptic HNF4A element. | missing | [E01](#e01), [E03](#e03) |
| gene | CYP7A1 is proposed as a long-range target because it is the nearest cholesterol/bile-acid gene among the listed genes, but E02 gives only distance to TSS (926.8 kb downstream) and no chromatin-contact, eQTL, or perturbation evidence links rs7001688 to CYP7A1. | missing | [E02](#e02) |
| cell_type | The proposed cellular context is Hep3B2.1-7 hepatocyte (DepMap ACH-000625), as given in the case expression context; no cited evidence shows HNF4A expression, chromatin accessibility, or allele-specific regulatory activity at this locus in that cell type. | missing | none |
| phenotype | If ref G increases HNF4A binding and HNF4A activates CYP7A1, then the alt T allele would reduce CYP7A1 and raise LDL cholesterol. This direction is speculative: HNF4A can activate or repress, and no evidence links rs7001688 to CYP7A1 expression or LDL cholesterol. | missing | none |

Predictions: allele-specific HNF4A EMSA or reporter assays would show ref G > alt T binding at rs7001688; chromatin-contact assays in Hep3B2.1-7 would link the rs7001688 region to the CYP7A1 promoter; the alt T allele would associate with lower CYP7A1 expression and higher LDL cholesterol

Falsified if: allele-specific HNF4A EMSA or reporter assays show no ref G > alt T binding difference at rs7001688; chromatin-contact assays in Hep3B2.1-7 do not link rs7001688 to the CYP7A1 promoter; rs7001688 genotype does not correlate with CYP7A1 expression in hepatocytes

### 3. SREBF2_alt_FAM110B: SREBF2 binds alt T at a cryptic element and alters FAM110B (p = 0.01)

TF SREBF2 (stated coverage not_checked; registry own_model), alt allele binds more; element cryptic distal SREBF2 motif candidate in an intronic/intergenic segment; gene FAM110B; cell type Hep3B2.1-7 hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SREBF2 is proposed to bind the alt T allele more strongly than the ref G allele. No positive QBiC-SELEX, ChIP-seq, MPRA, or reporter evidence supports this. QBiC-SELEX coverage is not_checked because no QBiC-SELEX row or TF lookup was provided. E08 reports no ENCODE SREBF2 ChIP-seq peak containing rs7001688, although absence can also reflect no SREBF2 experiment in the relevant biosample; this remains a low-confidence motif hypothesis. | missing | [E08](#e08) |
| element | E01 places rs7001688 as an intron_variant/intergenic variant with no regulatory feature, and E03 reports no overlapping cCRE; the nearest cCRE is 1544 bp away. These support only the genomic location and absence of an annotated cCRE, not the existence of a functional cryptic SREBF2 element. | missing | [E01](#e01), [E03](#e03) |
| gene | FAM110B is proposed as a distal target because it is the nearest listed protein-coding gene, 420.6 kb away, but E02 provides only distance. E06 reports a literature hit for FAM110B and LDL cholesterol/cardiovascular event reduction, but it does not mention rs7001688 or establish this variant as regulatory. | missing | [E02](#e02), [E06](#e06) |
| cell_type | The proposed cellular context is Hep3B2.1-7 hepatocyte (DepMap ACH-000625), as given in the case expression context; no cited evidence shows SREBF2 expression, activity, or allele-specific regulation at this locus in that cell type. | missing | none |
| phenotype | If alt T increases SREBF2-dependent FAM110B expression and this perturbs hepatic lipid handling, the alt T allele could raise LDL cholesterol. This is speculative; no evidence links rs7001688 to FAM110B expression or to an LDL-cholesterol effect, and SREBF2 effects on LDL are not simply directional. | missing | none |

Predictions: allele-specific SREBF2 EMSA or reporter assays would show alt T > ref G binding at rs7001688; rs7001688 genotype would correlate with FAM110B expression in hepatocytes; the alt T allele would associate with higher LDL cholesterol

Falsified if: allele-specific SREBF2 EMSA or reporter assays show no alt T > ref G binding difference at rs7001688; rs7001688 genotype does not correlate with FAM110B expression in hepatocytes; chromatin-contact or perturbation assays do not connect rs7001688 to FAM110B regulation

### 4. FOXA1_alt_CYP7A1: FOXA1 binds alt T at a cryptic element and represses CYP7A1 (p = 0.01)

TF FOXA1 (stated coverage not_checked; registry own_model), alt allele binds more; element cryptic distal FOXA1 pioneer-site candidate in an intronic/intergenic segment; gene CYP7A1; cell type Hep3B2.1-7 hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is proposed to bind the alt T allele more strongly than the ref G allele. No positive QBiC-SELEX, ChIP-seq, MPRA, or reporter evidence supports this. QBiC-SELEX coverage is not_checked because no QBiC-SELEX row or TF lookup was provided. E09 reports no ENCODE FOXA1 ChIP-seq peak containing rs7001688, although absence can also reflect no FOXA1 experiment in the relevant biosample; this remains a low-confidence motif hypothesis. | missing | [E09](#e09) |
| element | E01 places rs7001688 as an intron_variant/intergenic variant with no regulatory feature, and E03 reports no overlapping cCRE; the nearest cCRE is 1544 bp away. These support only the genomic location and absence of an annotated cCRE, not the existence of a functional cryptic FOXA1 element. | missing | [E01](#e01), [E03](#e03) |
| gene | CYP7A1 is proposed as a long-range target because it is a plausible cholesterol/bile-acid gene, but E02 gives only distance to TSS (926.8 kb downstream) and no chromatin-contact, eQTL, or perturbation evidence links rs7001688 to CYP7A1. | missing | [E02](#e02) |
| cell_type | The proposed cellular context is Hep3B2.1-7 hepatocyte (DepMap ACH-000625), as given in the case expression context; no cited evidence shows FOXA1 expression, pioneer activity, chromatin accessibility, or allele-specific regulation at this locus in that cell type. | missing | none |
| phenotype | If alt T increases FOXA1 binding and FOXA1 represses CYP7A1, then alt T would reduce bile-acid synthesis and raise LDL cholesterol. This is speculative; no evidence links rs7001688 to FOXA1 binding, CYP7A1 repression, or LDL cholesterol. | missing | none |

Predictions: allele-specific FOXA1 EMSA or reporter assays would show alt T > ref G binding at rs7001688; the rs7001688 region would be chromatin-accessible in hepatocytes; the alt T allele would associate with lower CYP7A1 expression and higher LDL cholesterol

Falsified if: allele-specific FOXA1 EMSA or reporter assays show no alt T > ref G binding difference at rs7001688; the rs7001688 region is not chromatin-accessible in hepatocytes; rs7001688 genotype does not affect CYP7A1 expression or LDL cholesterol

## Prediction matrix

| Test | Cost | Separates top two | null_no_TF_effect | HNF4A_ref_CYP7A1 | SREBF2_alt_FAM110B | FOXA1_alt_CYP7A1 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific HNF4A EMSA or reporter assay with rs7001688 ref/alt oligos in Hep3B2.1-7 nuclear extract | low | yes | no allelic difference in HNF4A binding | ref G > alt T HNF4A binding | no HNF4A-specific allelic difference | no HNF4A-specific allelic difference |
| Allele-specific SREBF2 EMSA or reporter assay with rs7001688 ref/alt oligos in Hep3B2.1-7 nuclear extract | low | no | no allelic difference in SREBF2 binding | no SREBF2-specific allelic difference | alt T > ref G SREBF2 binding | no SREBF2-specific allelic difference |
| Allele-specific FOXA1 EMSA or reporter assay with rs7001688 ref/alt oligos in Hep3B2.1-7 nuclear extract | low | no | no allelic difference in FOXA1 binding | no FOXA1-specific allelic difference | no FOXA1-specific allelic difference | alt T > ref G FOXA1 binding |
| Hepatocyte chromatin-contact assay (4C/Hi-C) between rs7001688 and the CYP7A1 promoter | medium | yes | no specific contact between rs7001688 and the CYP7A1 promoter | specific chromatin contact between rs7001688 and the CYP7A1 promoter | no specific CYP7A1 promoter contact; possible FAM110B contact instead | specific chromatin contact between rs7001688 and the CYP7A1 promoter |
| rs7001688 genotype versus CYP7A1 expression in hepatocytes (eQTL or allele-specific expression) | medium | yes | no effect of rs7001688 genotype on CYP7A1 expression | alt T associates with lower CYP7A1 expression | no effect of rs7001688 genotype on CYP7A1 expression | alt T associates with lower CYP7A1 expression |
| rs7001688 genotype versus FAM110B expression in hepatocytes (eQTL or allele-specific expression) | medium | no | no effect of rs7001688 genotype on FAM110B expression | no effect of rs7001688 genotype on FAM110B expression | alt T associates with higher FAM110B expression | no effect of rs7001688 genotype on FAM110B expression |
| Conditional genetic association of rs7001688 with LDL cholesterol accounting for linked variants | high | yes | no association of rs7001688 with LDL cholesterol after conditioning on linked variants | alt T associates with higher LDL cholesterol | alt T associates with higher LDL cholesterol | alt T associates with higher LDL cholesterol |

## Next experiment

The cheapest experiment separating the top two chains (null_no_TF_effect versus HNF4A_ref_CYP7A1) is an allele-specific HNF4A EMSA using rs7001688 ref/alt oligos and Hep3B2.1-7 nuclear extract. The null predicts no allelic binding difference; the HNF4A chain predicts ref G > alt T binding. This is low cost and directly tests the first unsupported link of the top non-null chain.

## Investigate calls

- chip_peaks({"tf": "HNF4A", "biosample": null})
- chip_peaks({"tf": "SREBF2", "biosample": null})
- chip_peaks({"tf": "FOXA1", "biosample": null})

## Flags

- literature_fallback: no hits for 'rs7001688 AND FAM110B AND "ldl cholesterol"'; dropped the rsID

Citation support: 0.60 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:57573391-57573391:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:33:20+00:00)

> Variant chr8:57573391:G>T (GRCh38), allele string G/T
> Known IDs: rs7001688
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 0.267
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:56573391-58573391?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:33+00:00)

> 5 protein-coding genes within 1000 kb of chr8:57573391:G>T, by distance to TSS:
> FAM110B: 420.6 kb from TSS (upstream, strand +1)
> BPNT2: 579.5 kb from TSS (upstream, strand -1)
> UBXN2B: 838.0 kb from TSS (upstream, strand +1)
> CYP7A1: 926.8 kb from TSS (downstream, strand -1)
> SDCBP: 979.5 kb from TSS (upstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:27+00:00)

> No cCRE overlaps the variant; nearest is EH38E3835076 (CA-H3K4me3) 1544 bp away.
> SCREEN: 0 cCREs within 500 bp (max z-score across ENCODE biosamples):
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs7001688&size=100; retrieved 2026-10-25T17:33:20+00:00)

> 0 GWAS Catalog associations for rs7001688, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:33:20+00:00)

> Open Targets has no record of 8_57573391_G_T.

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=FAM110B%20AND%20%22ldl%20cholesterol%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:33:21+00:00)

> Europe PMC: 1 hits for 'FAM110B AND "ldl cholesterol"'; top 1 with PMIDs:
> PMID 22666496 (2012): Genome-wide study of gene variants associated with differential cardiovascular event reduction by pravastatin therapy.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:31:22+00:00)

> No ENCODE HNF4A ChIP-seq peak contains chr8:57573391:G>T. Absence can also mean no HNF4A experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:37:21+00:00)

> No ENCODE SREBF2 ChIP-seq peak contains chr8:57573391:G>T. Absence can also mean no SREBF2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:37:21+00:00)

> No ENCODE FOXA1 ChIP-seq peak contains chr8:57573391:G>T. Absence can also mean no FOXA1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.
