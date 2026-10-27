# rs73706717 and Colorectal cancer (8q24)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 204 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. chain_1_null: No TF-mediated allelic effect at rs73706717; 8q24 signal is linked/passenger (p = 0.66)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding is detected at the exact rs73706717 base.; The 8q24 signal tracks a linked variant in the same enhancer rather than this base change.; Reporter assays comparing ref T and alt C show no differential enhancer activity.

Falsified if: Allele-specific TCF7L2 ChIP, EMSA, or reporter assays show a reproducible ref-vs-alt difference at rs73706717 itself.; An allele-specific cis-regulatory assay shows rs73706717 changes MYC, POU5F1B, CCAT2, or PCAT1 expression independently of a linked variant.

### 2. chain_2_TCF7L2_MYC: Alt C strengthens TCF7L2 binding in the 8q24 enhancer and raises MYC (p = 0.17)

TF TCF7L2 (stated coverage not_checked; registry mapped), alt allele binds more; element EH38E3858447 is a proximal enhancer-like cCRE in the 8q24 region and is contained within a TCF7L2 ENCODE ChIP-seq peak in HCT 116.; gene MYC; cell type colorectal cancer cells, with HCT 116 as the provided expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is hypothesized to bind the alt C allele more strongly than ref T. E07 supports TCF7L2 occupancy of an element containing this variant in HCT 116, but it does not establish allele-specific binding. QBiC-SELEX coverage for TCF7L2 is not_checked because no QBiC screen row or qbic_tf_detail lookup is provided; no QBiC binding-change evidence is cited. | weak | [E07](#e07) |
| element | The variant lies in the proximal enhancer-like cCRE EH38E3858447, and E07 places this region in a TCF7L2 ChIP-seq peak in HCT 116. | supported | [E01](#e01), [E03](#e03), [E07](#e07) |
| gene | MYC is 334.2 kb upstream of the variant, and the provided literature includes general 8q24/MYC colorectal cancer relevance. No provided eQTL, reporter, CRISPR, or chromatin-interaction evidence directly links this cCRE/variant to MYC. | weak | [E02](#e02), [E06](#e06) |
| cell_type | The proposed mechanism is in colorectal cancer cells. E07 places TCF7L2 at this element in HCT 116, but the allele-specific mechanism is not demonstrated in HCT 116. | weak | [E07](#e07) |
| phenotype | Increased MYC activity is a plausible colorectal cancer-promoting mechanism in general, but no provided evidence ties rs73706717 to MYC expression or to colorectal cancer risk. | weak | [E06](#e06) |

Predictions: Allele-specific TCF7L2 ChIP or EMSA shows stronger binding to alt C than ref T.; An enhancer reporter carrying alt C has higher activity than ref T in colorectal cancer cells.; MYC expression is higher in cells carrying alt C at this position.

Falsified if: Allele-specific TCF7L2 binding at rs73706717 is absent or shows ref T > alt C.; The alt C allele does not change enhancer activity or MYC expression.; The TCF7L2 ChIP signal is explained by a linked variant rather than rs73706717.

### 3. chain_4_TCF7L2_POU5F1B: Alt C strengthens TCF7L2 binding at the pELS and alters POU5F1B (p = 0.10)

TF TCF7L2 (stated coverage not_checked; registry mapped), alt allele binds more; element EH38E3858447 is a proximal enhancer-like cCRE in the 8q24 region and is contained within a TCF7L2 ENCODE ChIP-seq peak in HCT 116.; gene POU5F1B; cell type colorectal cancer cells, with HCT 116 as the provided expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is hypothesized to bind the alt C allele more strongly than ref T. E07 supports TCF7L2 occupancy of an element containing this variant in HCT 116, but it does not establish allele-specific binding. QBiC-SELEX coverage for TCF7L2 is not_checked because no QBiC screen row or qbic_tf_detail lookup is provided; no QBiC binding-change evidence is cited. | weak | [E07](#e07) |
| element | The variant lies in the proximal enhancer-like cCRE EH38E3858447, and E07 places this region in a TCF7L2 ChIP-seq peak in HCT 116. | supported | [E01](#e01), [E03](#e03), [E07](#e07) |
| gene | POU5F1B is the closest protein-coding gene, the variant lies in its gene body, and POU5F1B has the best L2G score in the provided credible sets. Those credible sets are non-CRC with PIP 0.04, and no direct regulatory link from this element to POU5F1B is provided. | weak | [E02](#e02), [E05](#e05), [E06](#e06) |
| cell_type | The proposed mechanism is in colorectal cancer cells. E07 places TCF7L2 at this element in HCT 116, but the allele-specific effect on POU5F1B is not demonstrated. | weak | [E07](#e07) |
| phenotype | POU5F1B has colorectal cancer literature and an Open Targets colorectal cancer score of 0.54, making it a plausible disease-relevant target, but no provided evidence ties rs73706717 to POU5F1B expression or colorectal cancer. | weak | [E06](#e06), [E09](#e09) |

Predictions: Allele-specific TCF7L2 ChIP or EMSA shows stronger binding to alt C than ref T.; POU5F1B expression changes with the alt C allele in colorectal cancer cells.; MYC expression is not the primary downstream readout of this element.

Falsified if: Allele-specific TCF7L2 binding at rs73706717 is absent or shows ref T > alt C.; POU5F1B expression is unchanged by the variant or by TCF7L2 perturbation.; The POU5F1B L2G signal is explained by a different linked variant or by a non-CRC trait.

### 4. chain_3_CTCF_POU5F1B: Alt C alters CTCF occupancy at the pELS and affects POU5F1B (p = 0.07)

TF CTCF (stated coverage not_checked; registry own_model), alt allele binds more; element EH38E3858447 contains CTCF ChIP signal and overlaps a proximal enhancer-like cCRE; altered CTCF occupancy could change insulator/architectural activity at this element.; gene POU5F1B; cell type colorectal cancer cells, with HCT 116 as the provided expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is hypothesized to bind the alt C allele more strongly than ref T. E03 reports CTCF ChIP signal at the containing cCRE, but the values are maxima across ENCODE biosamples and are not allele-specific. QBiC-SELEX coverage for CTCF is not_checked because no QBiC screen row or qbic_tf_detail lookup is provided; no QBiC binding-change evidence is cited. | weak | [E03](#e03) |
| element | The variant lies in cCRE EH38E3858447, a pELS with CTCF ChIP signal, so altered CTCF occupancy could change local enhancer or insulator behavior. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is the closest protein-coding gene, the variant lies in its gene body, and POU5F1B has the best L2G score in the provided credible sets. However, those credible sets are for PSA and urinary incontinence with PIP 0.04, not colorectal cancer, and no direct regulatory link is provided. | weak | [E02](#e02), [E05](#e05), [E06](#e06) |
| cell_type | The proposed effect is in colorectal cancer cells, but the CTCF ChIP evidence is from ENCODE biosample maxima and is not HCT 116-specific. POU5F1B has general colorectal cancer literature support. | weak | [E03](#e03), [E06](#e06) |
| phenotype | POU5F1B has colorectal cancer literature and an Open Targets colorectal cancer score of 0.54, but no provided evidence establishes a causal rs73706717 effect. If CTCF acts as an insulator, stronger CTCF would be predicted to reduce POU5F1B expression. | weak | [E06](#e06), [E09](#e09) |

Predictions: Allele-specific CTCF ChIP or EMSA shows stronger binding to alt C than ref T.; CTCF depletion or mutation of the CTCF site changes POU5F1B expression in an allele-dependent manner.; If CTCF is insulating, the alt C allele is associated with lower POU5F1B expression.

Falsified if: CTCF binding at rs73706717 is not allele-specific.; POU5F1B expression is unchanged by the variant or by CTCF depletion.; The Open Targets L2G signal is explained by a different linked variant.

## Prediction matrix

| Test | Cost | Separates top two | chain_1_null | chain_2_TCF7L2_MYC | chain_4_TCF7L2_POU5F1B | chain_3_CTCF_POU5F1B |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 EMSA using ref T and alt C oligos, or allele-specific TCF7L2 ChIP in a heterozygous colorectal cancer line | low | yes | No reproducible ref-vs-alt TCF7L2 binding difference | Alt C binds TCF7L2 more strongly than ref T | Alt C binds TCF7L2 more strongly than ref T | No TCF7L2 allele-specific binding difference |
| Allele-specific CTCF EMSA or allele-specific CTCF ChIP at rs73706717 | low | no | No reproducible ref-vs-alt CTCF binding difference | No CTCF allele-specific binding difference required | No CTCF allele-specific binding difference required | Alt C binds CTCF more strongly than ref T |
| Enhancer reporter assay comparing ref T and alt C in HCT 116 | medium | yes | Ref T and alt C reporters have equal activity | Alt C reporter has higher activity than ref T | Alt C reporter has higher activity than ref T | Alt C reporter changes activity, potentially lower if CTCF insulating |
| Endogenous allele swap or CRISPR knock-in at rs73706717 in HCT 116, measuring MYC and POU5F1B expression | high | yes | No allele-dependent change in MYC or POU5F1B expression after allele swap | Alt C increases MYC expression in an allele-specific manner | Alt C changes POU5F1B expression; MYC is not the primary readout | Alt C changes POU5F1B expression, predicted lower if CTCF insulating |
| Colon eQTL lookup for rs73706717 and nearby 8q24 genes in additional colon tissues | low | no | No colon eQTL for this variant affecting MYC, POU5F1B, CCAT2, or PCAT1 | A colon eQTL links the alt C allele to higher MYC | A colon eQTL links the alt C allele to altered POU5F1B | A colon eQTL links the alt C allele to altered POU5F1B |

## Next experiment

The cheapest experiment that separates the top two chains is an allele-specific TCF7L2 EMSA using ref T and alt C oligos, or allele-specific TCF7L2 ChIP in a heterozygous colorectal cancer line. It directly tests whether chain_2_TCF7L2_MYC has the required allele-specific TCF7L2 binding step, while chain_1_null predicts no reproducible ref-vs-alt difference.

## Investigate calls

- chip_peaks({"biosample": "HCT 116", "tf": "TCF7L2"})
- eqtl_lookup({"tissue": "Colon - Transverse"})
- gene_disease({"gene": "POU5F1B"})

## Flags

- literature_fallback: no hits for 'rs73706717 AND POU5F1B AND "colorectal cancer"'; dropped the rsID
- quote_rejected: PMID 42465001: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401265-127401265:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:21:56+00:00)

> Variant chr8:127401265:T>C (GRCh38), allele string T/C
> Known IDs: rs73706717
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: -2.8
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401265-128401265?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:21:59+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401265:T>C, by distance to TSS:
> POU5F1B: 79.1 kb from TSS (in gene body, strand +1)
> MYC: 334.2 kb from TSS (upstream, strand +1)
> LRATD2: 842.8 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:21:42+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs73706717&size=100; retrieved 2026-10-26T02:21:56+00:00)

> 0 GWAS Catalog associations for rs73706717, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:21:56+00:00)

> 2 credible sets contain 8_127401265_T_C: 2 GWAS, 0 molecular QTL.
> GWAS prostate-specific antigen (PSA, maximum, inv-norm transforme: PIP 0.04; L2G POU5F1B 0.83
> GWAS Urinary incontinence (PheCode 599.4): PIP 0.04; L2G POU5F1B 0.78
> Best L2G gene scores across these sets: POU5F1B 0.83

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:21:59+00:00)

> Europe PMC: 150 hits for 'POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 42465001 (2026): Circ_0075829 affects POU5F1B expression through sponging miR-576-3p to promote growth, invasion, and angiogenesis of colon cancer cells.
> PMID 41993623 (2026): Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research.
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 41930642 (2026): Systematic Identification and Characterization of Causal Risk Genes Implicated in Colorectal Cancer by Integrating GWAS, eQTL, and mQTL Data.
> PMID 42686757 (2026): Phase separation of ecDNA condensates establishes in-trans contact domains that boost selective MYC regulatory interactions.
> PMID 40506516 (2025): Association between methylation quantitative trait loci and colorectal cancer risk, survival and cancer recurrence.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 41196428 (2025): Combined CHK1 and PD-L1 blockade as a novel therapeutic strategy against stemness and immunosuppression in ovarian cancer.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:23:31+00:00)

> 1 ENCODE TCF7L2 ChIP-seq peaks contain chr8:127401265:T>C in biosamples matching 'HCT 116': biosamples HCT116; experiments ENCSR000EUV. In other biosamples, 3 TCF7L2 peaks do contain the variant: HepG2 (experiments ENCSR000EVQ, ENCSR346BOD).

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e09"></a>**E09** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14
