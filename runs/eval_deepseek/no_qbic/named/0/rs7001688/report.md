# rs7001688 and LDL cholesterol

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 110 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H0: No TF-mediated effect; linked causal variant or no allelic effect (p = 0.92)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs7001688.; No reproducible liver eQTL for nearby genes attributable to rs7001688.; Any LDL association is due to a linked causal variant or chance, not to this variant's own TF-mediated effect.

Falsified if: An allele-specific TF binding assay at rs7001688 shows reproducible differential binding in a hepatocyte context and the bound TF regulates an LDL-relevant target gene.; A liver eQTL or chromatin-contact assay connects rs7001688 to an LDL-relevant gene and perturbation confirms the phenotype.

### 2. H1: HNF4A binds the alt allele at a weak intronic element and alters FAM110B (p = 0.04)

TF HNF4A (stated coverage not_checked; registry own_model), alt allele binds more; element weak intronic sequence near a CA-H3K4me3 cCRE, not overlapping an ENCODE cCRE; gene FAM110B; cell type hepatocyte / Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HNF4A is proposed to bind the alt T allele more strongly than the ref G allele at rs7001688. No QBiC-SELEX, MPRA, reporter, or allele-specific binding evidence is provided. E08 found no ENCODE HNF4A ChIP-seq peak containing the variant in HepG2, which weakens but does not exclude this chain because absence may also reflect no HNF4A experiment in that biosample. HNF4A was chosen as the only TF directly queried by a provided ChIP row; its QBiC coverage is not checked because no QBiC-SELEX evidence was supplied. | missing | [E08](#e08) |
| element | The variant is an intronic variant with no annotated regulatory feature and no ENCODE cCRE overlap; the nearest cCRE is a CA-H3K4me3 element 1544 bp away, so any regulatory element would be weak or indirect. | supported | [E01](#e01), [E03](#e03) |
| gene | FAM110B is the nearest protein-coding gene at 420.6 kb, but distance alone does not establish regulation. There are no significant liver GTEx eQTLs for this variant, no Open Targets association between FAM110B and free cholesterol in large LDL, and the Europe PMC hit is not variant-specific. | supported | [E02](#e02), [E06](#e06), [E07](#e07), [E09](#e09) |
| cell_type | Hep 3B2.1-7 is a hepatocyte-derived line, but the provided evidence contains no HNF4A expression, ChIP, or perturbation data in this cell type. | missing | none |
| phenotype | A change in FAM110B regulation could in principle influence LDL cholesterol, but there is no rs7001688-specific evidence. E06 is an indirect literature hit, E09 does not support a FAM110B free-cholesterol association, and E04/E05 report no variant-disease record. | supported | [E04](#e04), [E05](#e05), [E06](#e06), [E09](#e09) |

Predictions: HNF4A binds the alt T allele more strongly than ref G at rs7001688 in a hepatocyte context.; The region contacts FAM110B or another LDL-relevant gene in hepatocytes.; Modulating the element or FAM110B changes LDL cholesterol.

Falsified if: Allele-specific HNF4A binding assays in hepatocyte nuclear extract show no difference between alt T and ref G.; HNF4A ChIP-qPCR in Hep 3B2.1-7 shows no enrichment at the rs7001688 element.; No chromatin-contact or eQTL evidence links the region to FAM110B, or FAM110B perturbation does not affect LDL cholesterol.

### 3. H2: SREBF2 binds the ref allele at a weak intronic element and alters FAM110B (p = 0.02)

TF SREBF2 (stated coverage not_checked; registry own_model), ref allele binds more; element weak intronic sequence near a CA-H3K4me3 cCRE, not overlapping an ENCODE cCRE; gene FAM110B; cell type hepatocyte / Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SREBF2 is proposed to bind the ref G allele more strongly than the alt T allele at rs7001688, as a speculative sterol-responsive TF hypothesis. No QBiC-SELEX, MPRA, reporter, ChIP, or allele-specific binding evidence is provided, and SREBF2 QBiC coverage is not checked because no QBiC-SELEX evidence was supplied. | missing | none |
| element | The variant is an intronic variant with no annotated regulatory feature and no ENCODE cCRE overlap; the nearest cCRE is 1544 bp away, so this would require a weak or long-range regulatory element. | supported | [E01](#e01), [E03](#e03) |
| gene | FAM110B is the nearest protein-coding gene at 420.6 kb, but no liver eQTL, chromatin-contact, or perturbation evidence links rs7001688 to FAM110B. E06 is not variant-specific, and E09 does not support a FAM110B free-cholesterol association. | supported | [E02](#e02), [E06](#e06), [E07](#e07), [E09](#e09) |
| cell_type | Hep 3B2.1-7 is a hepatocyte-derived line, but the provided evidence contains no SREBF2 expression, ChIP, or perturbation data in this cell type. | missing | none |
| phenotype | A sterol-regulated change in FAM110B could in principle affect LDL cholesterol, but no provided evidence shows rs7001688 alters SREBF2 binding or FAM110B regulation in a way that changes LDL. | supported | [E04](#e04), [E05](#e05), [E06](#e06), [E09](#e09) |

Predictions: SREBF2 binds the ref G allele more strongly than alt T at rs7001688.; The element responds to sterol depletion in hepatocytes.; SREBF2 perturbation changes FAM110B or another LDL-relevant target.

Falsified if: Allele-specific SREBF2 binding assays show no difference between ref G and alt T.; The element does not respond to sterol depletion in hepatocytes.; No chromatin-contact or eQTL evidence links the region to FAM110B, or SREBF2 perturbation does not change the proposed target gene.

### 4. H3: CEBPB binds the alt allele at a weak intronic element and alters CYP7A1 (p = 0.02)

TF CEBPB (stated coverage not_checked; registry own_model), alt allele binds more; element weak intronic sequence near a CA-H3K4me3 cCRE, not overlapping an ENCODE cCRE; gene CYP7A1; cell type hepatocyte / Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB is proposed to bind the alt T allele more strongly than the ref G allele at rs7001688, as a speculative liver-enriched TF hypothesis. No QBiC-SELEX, MPRA, reporter, ChIP, or allele-specific binding evidence is provided, and CEBPB QBiC coverage is not checked because no QBiC-SELEX evidence was supplied. | missing | none |
| element | The variant lies in an intronic region with no cCRE overlap and only a nearby CA-H3K4me3 mark 1544 bp away, so any enhancer would be weak or indirect. | supported | [E01](#e01), [E03](#e03) |
| gene | CYP7A1 lies 926.8 kb downstream, but no eQTL, chromatin-contact, or perturbation evidence connects rs7001688 to CYP7A1. The distance alone is very large and does not establish regulation. | supported | [E02](#e02), [E07](#e07) |
| cell_type | Hep 3B2.1-7 is a hepatocyte-derived line, but the provided evidence contains no CEBPB expression, ChIP, or perturbation data in this cell type. | missing | none |
| phenotype | CYP7A1 is involved in bile acid synthesis and can influence LDL cholesterol, but no provided evidence directly connects rs7001688 to CYP7A1 expression or to LDL cholesterol through this variant. | supported | [E02](#e02), [E04](#e04), [E05](#e05), [E07](#e07) |

Predictions: CEBPB binds the alt T allele more strongly than ref G at rs7001688.; Chromatin contact or eQTL data connect this region to CYP7A1 in hepatocytes.; CEBPB perturbation changes CYP7A1 expression or LDL cholesterol.

Falsified if: Allele-specific CEBPB binding assays show no difference between alt T and ref G.; No chromatin-contact or eQTL evidence connects the region to CYP7A1 in hepatocytes.; CEBPB perturbation does not alter CYP7A1 expression or LDL cholesterol.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA with Hep 3B2.1-7 nuclear extract and HNF4A antibody supershift at rs7001688 | low | yes | No allele-specific HNF4A binding at rs7001688. | HNF4A binds the alt T allele more strongly than ref G. | No HNF4A allele-specific effect; SREBF2 hypothesis not tested by this assay. | No HNF4A allele-specific effect; CEBPB hypothesis not tested by this assay. |
| Liver eQTL lookup for rs7001688 and nearby genes, especially FAM110B | low | yes | No liver eQTL for FAM110B or other nearby LDL-relevant genes attributable to rs7001688. | A liver eQTL links rs7001688 to FAM110B in the direction predicted by altered HNF4A binding. | A liver eQTL links rs7001688 to FAM110B, but not necessarily through SREBF2. | A liver eQTL links rs7001688 to CYP7A1, not FAM110B. |
| HNF4A ChIP-qPCR at rs7001688 in Hep 3B2.1-7 | medium | yes | No HNF4A ChIP enrichment at the rs7001688 element. | HNF4A ChIP enrichment at the rs7001688 element, with stronger signal on the alt T allele if allele-specific. | No HNF4A ChIP enrichment at the rs7001688 element. | No HNF4A ChIP enrichment at the rs7001688 element. |
| FAM110B CRISPR perturbation in Hep 3B2.1-7 with an LDL cholesterol readout | high | yes | FAM110B perturbation has no reproducible effect on LDL cholesterol. | FAM110B perturbation changes LDL cholesterol or LDL uptake/secretion in hepatocytes. | FAM110B perturbation changes LDL cholesterol or LDL uptake/secretion in hepatocytes. | FAM110B perturbation has no effect; CYP7A1 perturbation would be the relevant test. |
| Allele-specific SREBF2 binding assay at rs7001688 | low | no | No allele-specific SREBF2 binding at rs7001688. | No SREBF2 allele-specific effect; HNF4A hypothesis not tested by this assay. | SREBF2 binds the ref G allele more strongly than alt T. | No SREBF2 allele-specific effect; CEBPB hypothesis not tested by this assay. |
| Allele-specific CEBPB binding assay at rs7001688 | low | no | No allele-specific CEBPB binding at rs7001688. | No CEBPB allele-specific effect; HNF4A hypothesis not tested by this assay. | No CEBPB allele-specific effect; SREBF2 hypothesis not tested by this assay. | CEBPB binds the alt T allele more strongly than ref G. |

## Next experiment

Allele-specific EMSA with Hep 3B2.1-7 nuclear extract and HNF4A antibody supershift at rs7001688. It is the cheapest direct test that separates the top two chains: H0 predicts no allele-specific HNF4A binding, whereas H1 predicts stronger HNF4A binding to the alt T allele.

## Investigate calls

- eqtl_lookup({"tissue": "Liver"})
- chip_peaks({"tf": "HNF4A", "biosample": "HepG2"})
- gene_disease({"gene": "FAM110B"})

## Flags

- literature_fallback: no hits for 'rs7001688 AND FAM110B AND "ldl cholesterol"'; dropped the rsID

Citation support: 0.67 of links cite only evidence that passed every check.

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

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:31:22+00:00)

> No ENCODE HNF4A ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no HNF4A experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e09"></a>**E09** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:41:58+00:00)

> Open Targets: no association between FAM110B and free cholesterol in large LDL measurement (EFO_0022176).
