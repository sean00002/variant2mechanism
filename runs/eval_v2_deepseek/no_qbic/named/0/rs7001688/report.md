# rs7001688 and LDL cholesterol

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 7 model calls; 119 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H0_null: No TF-mediated effect; linked causal variant or non-regulatory passenger (p = 0.89)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific CTCF occupancy at rs7001688 in liver-derived cells.; The variant does not overlap a liver cCRE and does not reproducibly contact FAM110B or CYP7A1 in hepatocytes.; No significant liver or other-tissue eQTL is found for rs7001688.; Any LDL association is better explained by a linked causal variant rather than this base.

Falsified if: An allele-specific CTCF ChIP, reporter assay, or other occupancy assay in hepatocytes shows differential CTCF binding at rs7001688.; A liver eQTL or chromatin-contact assay connects rs7001688 to a nearby gene in a genotype-dependent way.

### 2. H1_CTCF_ref_FAM110B: CTCF ref-gain at a cryptic element with distal FAM110B effect (p = 0.07)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element cryptic or condition-specific CTCF-bound element outside called cCREs; gene FAM110B; cell type Hep3B2.1-7 / hepatocyte context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is the only listed bound, expressed TF with a binding model at this site, chosen because E04/E05/E10 report CTCF occupancy and expression, but the only peak containing the variant is in LNCAP, not liver; no QBiC-SELEX evidence for CTCF at this base is supplied, so the hypothesis that ref G binds CTCF more strongly than alt T is speculative. | missing | [E04](#e04), [E05](#e05), [E10](#e10) |
| element | The variant is an intronic/intergenic site with no overlapping cCRE; the nearest cCRE is 1544 bp away, and the only CTCF peak containing the variant is outside liver, so any CTCF-bound element here would be cryptic or condition-specific rather than a canonical liver regulatory element. | weak | [E01](#e01), [E03](#e03), [E04](#e04), [E05](#e05), [E10](#e10) |
| gene | FAM110B is the nearest protein-coding gene at 420.6 kb, but GTEx reports no significant eQTL for rs7001688 and the only literature link is a statin-response study involving FAM110B, not a direct rs7001688-to-FAM110B expression link. | missing | [E02](#e02), [E08](#e08), [E09](#e09), [E11](#e11) |
| cell_type | CTCF is expressed in Hep3B2.1-7, but ENCODE reports no CTCF ChIP peak at this site in the HepG2 liver proxy; the chain requires hepatocyte-specific or condition-specific CTCF occupancy that is not demonstrated. | missing | [E04](#e04), [E05](#e05), [E10](#e10) |
| phenotype | If hepatocyte CTCF binding at this cryptic element changed FAM110B expression, it could influence LDL cholesterol, but there is no rs7001688 GWAS, Open Targets, or eQTL support for this variant-to-phenotype link. | missing | [E06](#e06), [E07](#e07), [E08](#e08), [E11](#e11) |

Predictions: Ref G allele shows higher CTCF occupancy than alt T at rs7001688 in Hep3B2.1-7 or primary hepatocytes.; The variant-containing region contacts the FAM110B locus in hepatocytes.; FAM110B expression is allele-dependent with rs7001688 genotype in liver-derived cells.

Falsified if: CTCF ChIP or reporter assays in liver-derived cells show no ref-specific gain of CTCF binding at rs7001688.; Chromatin-contact assays do not link this site to FAM110B, or FAM110B expression is not allele-dependent in hepatocytes.

### 3. H2_CTCF_alt_CYP7A1: CTCF alt-gain at a cryptic element with distal CYP7A1 effect (p = 0.04)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element cryptic or condition-specific CTCF-bound element outside called cCREs; gene CYP7A1; cell type Hep3B2.1-7 / hepatocyte context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is the only listed bound, expressed TF with a binding model at this site, chosen because E04/E05/E10 report CTCF occupancy and expression, but the only peak containing the variant is in LNCAP, not liver; no QBiC-SELEX evidence for CTCF at this base is supplied, so the hypothesis that alt T binds CTCF more strongly than ref G is speculative. | missing | [E04](#e04), [E05](#e05), [E10](#e10) |
| element | The variant does not overlap a cCRE and the nearest cCRE is 1544 bp away; the only CTCF peak containing the variant is non-liver, so any CTCF-dependent element would be cryptic or condition-specific. | weak | [E01](#e01), [E03](#e03), [E04](#e04), [E05](#e05), [E10](#e10) |
| gene | CYP7A1 is 926.8 kb downstream, but GTEx reports no significant eQTL for rs7001688 and no chromatin-contact evidence is supplied; the CYP7A1 link relies on distance and external LDL biology, not on direct variant-to-gene evidence. | missing | [E02](#e02), [E08](#e08), [E11](#e11) |
| cell_type | CTCF is expressed in Hep3B2.1-7, but no CTCF ChIP peak is seen at this site in HepG2; the proposed distal effect requires liver-specific CTCF occupancy and long-range looping not shown here. | missing | [E04](#e04), [E05](#e05), [E10](#e10) |
| phenotype | If alt-specific CTCF binding altered a distal contact with CYP7A1, changed CYP7A1 expression could influence LDL cholesterol, but there is no rs7001688 GWAS, Open Targets, or eQTL support for this variant-to-phenotype link. | missing | [E06](#e06), [E07](#e07), [E08](#e08), [E11](#e11) |

Predictions: Alt T allele shows higher CTCF occupancy than ref G at rs7001688 in Hep3B2.1-7 or primary hepatocytes.; The variant-containing region contacts the CYP7A1 locus in hepatocytes.; CYP7A1 expression is allele-dependent with rs7001688 genotype in liver-derived cells.

Falsified if: CTCF ChIP or reporter assays in liver-derived cells show no alt-specific gain of CTCF binding at rs7001688.; Chromatin-contact assays do not link this site to CYP7A1, or CYP7A1 expression is not allele-dependent in hepatocytes.

## Prediction matrix

| Test | Cost | Separates top two | H0_null | H1_CTCF_ref_FAM110B | H2_CTCF_alt_CYP7A1 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific CTCF ChIP-qPCR at rs7001688 in Hep3B2.1-7 or primary hepatocytes | low | yes | No allele-specific CTCF occupancy at rs7001688. | Ref G > alt T CTCF occupancy at rs7001688. | Alt T > ref G CTCF occupancy at rs7001688. |
| CTCF ChIP-seq with cCRE overlap at rs7001688 in HepG2/Hep3B2.1-7 | low | yes | No CTCF ChIP peak and no cCRE over the variant in liver-derived cells. | CTCF ChIP peak over the variant in liver-derived cells, consistent with a cryptic liver element. | CTCF ChIP peak over the variant in liver-derived cells, consistent with a cryptic liver element. |
| Chromatin conformation assay (4C/Hi-C or promoter capture) in hepatocytes | high | yes | No reproducible contact between rs7001688 and FAM110B or CYP7A1. | Reproducible contact between rs7001688 and the FAM110B locus in hepatocytes. | Reproducible contact between rs7001688 and the CYP7A1 locus in hepatocytes. |
| Liver eQTL or hepatocyte genotype-expression panel for rs7001688 | high | yes | No significant eQTL for rs7001688 in liver or hepatocyte panels. | Significant liver eQTL linking rs7001688 to FAM110B expression. | Significant liver eQTL linking rs7001688 to CYP7A1 expression. |

## Next experiment

The single cheapest experiment that separates the top two chains (H0_null and H1_CTCF_ref_FAM110B) is allele-specific CTCF ChIP-qPCR at rs7001688 in Hep3B2.1-7 or primary hepatocytes: H0 predicts no allele-specific occupancy, while H1 predicts ref G > alt T CTCF occupancy.

## Investigate calls

- chip_peaks({"tf": "CTCF", "biosample": "HepG2"})
- eqtl_lookup({"tissue": "Liver"})
- literature_search({"query": "rs7001688"})

## Flags

- literature_fallback: no hits for 'rs7001688 AND FAM110B AND "ldl cholesterol"'; dropped the rsID

Citation support: 1.00 of links cite only evidence that passed every check.

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

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:57573391:G>T: 1 peaks contain the variant, from 1 factors in 1 biosamples. In the matching biosample HepG2 (HepG2 stands in for Hep 3B2.1-7 (both liver cancer lines)): 0 peaks from 0 factors. No cCRE contains the variant. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): none. Bound, expressed TFs with a binding model: 1; listed one per row: CTCF. Assayed with no peak here: 382 TFs in the matching biosample, 190 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: LNCAP (e.g. ENCSR673WZL). 32.01 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 162 of 1626 TFs.

<a id="e06"></a>**E06** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs7001688&size=100; retrieved 2026-10-25T17:33:20+00:00)

> 0 GWAS Catalog associations for rs7001688, strongest first:

<a id="e07"></a>**E07** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:33:20+00:00)

> Open Targets has no record of 8_57573391_G_T.

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=FAM110B%20AND%20%22ldl%20cholesterol%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:33:21+00:00)

> Europe PMC: 1 hits for 'FAM110B AND "ldl cholesterol"'; top 1 with PMIDs:
> PMID 22666496 (2012): Genome-wide study of gene variants associated with differential cardiovascular event reduction by pravastatin therapy.

<a id="e10"></a>**E10** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:32:53+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no CTCF experiment in that biosample. In other biosamples, 1 CTCF peaks do contain the variant: LNCAP (experiments ENCSR673WZL).

<a id="e11"></a>**E11** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e12"></a>**E12** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs7001688&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:32:53+00:00)

> Europe PMC: 0 hits for 'rs7001688'; top 0 with PMIDs:
