# rs7001688 and LDL cholesterol

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 151 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H0: No TF-mediated effect of rs7001688 (p = 0.96)

Null chain: no TF-mediated effect of this variant.

Predictions: The G>T change will not produce reproducible allele-specific CTCF occupancy or a variant-dependent change in a target gene in a relevant liver-cell context.; Any LDL-cholesterol association, if one exists, will not be mediated by a TF effect of rs7001688.

Falsified if: Editing rs7001688 reproducibly changes CTCF occupancy and target-gene expression in a relevant liver-cell context, with evidence connecting the effect to LDL cholesterol.

### 2. H1: Speculative alt-favored CTCF regulation of CYP7A1 (p = 0.02)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element A possible CTCF-associated site at rs7001688; a regulatory element at this position is not established.; gene CYP7A1; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This chain tests the hypothesis that T (alt) binds CTCF more strongly than G (ref). CTCF is the only listed bound, expressed TF with a binding model, but the overlapping peak is from LNCaP, not the relevant liver-cell context; no QBiC-SELEX model or result is supplied here to support the direction. | weak | [E04](#e04), [E05](#e05), [E10](#e10) |
| element | A CTCF peak overlaps the variant in LNCaP, but no cCRE overlaps the site and the evidence does not establish an active regulatory element in Hep 3B2.1-7. | supported | [E03](#e03), [E04](#e04), [E10](#e10) |
| gene | CYP7A1 is an unvalidated candidate target, listed 926.8 kb from the variant by TSS distance; no variant-to-gene evidence is supplied. | weak | [E02](#e02), [E11](#e11) |
| cell_type | CTCF is expressed in Hep 3B2.1-7, but no overlapping CTCF peak is reported in the HepG2 proxy for this cell context. | supported | [E04](#e04), [E05](#e05) |
| phenotype | The supplied evidence does not establish a connection from rs7001688 or CYP7A1 regulation at this site to LDL cholesterol. | supported | [E06](#e06), [E07](#e07), [E08](#e08), [E11](#e11) |

Predictions: Unlike H0, this chain predicts that targeted allele comparison in a relevant liver-cell context will show greater CTCF occupancy on T than on G.; Unlike H2, this chain predicts that editing rs7001688 will preferentially alter CYP7A1 expression or its contact with the variant region, rather than FAM110B.

Falsified if: A relevant-cell allele-specific occupancy assay finds no reproducible CTCF binding difference, or finds stronger binding to G than T.; Variant perturbation produces no CYP7A1 expression or contact effect while producing a reproducible effect on another proposed target.

### 3. H2: Speculative ref-favored CTCF regulation of FAM110B (p = 0.02)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element A possible CTCF-associated site at rs7001688; a regulatory element at this position is not established.; gene FAM110B; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | This competing chain tests the hypothesis that G (ref) binds CTCF more strongly than T (alt). CTCF is the only listed bound, expressed TF with a binding model, but the overlapping peak is from LNCaP, not the relevant liver-cell context; no QBiC-SELEX model or result is supplied here to support the direction. | weak | [E04](#e04), [E05](#e05), [E10](#e10) |
| element | A CTCF peak overlaps the variant in LNCaP, but no cCRE overlaps the site and the evidence does not establish an active regulatory element in Hep 3B2.1-7. | supported | [E03](#e03), [E04](#e04), [E10](#e10) |
| gene | FAM110B is an unvalidated candidate target, listed 420.6 kb from the variant by TSS distance; the cited literature hit concerns differential pravastatin response and does not establish regulation by rs7001688. | weak | [E02](#e02), [E09](#e09), [E12](#e12) |
| cell_type | CTCF is expressed in Hep 3B2.1-7, but no overlapping CTCF peak is reported in the HepG2 proxy for this cell context. | supported | [E04](#e04), [E05](#e05) |
| phenotype | The supplied evidence does not establish a connection from rs7001688 or FAM110B regulation at this site to LDL cholesterol. | supported | [E06](#e06), [E07](#e07), [E08](#e08), [E09](#e09), [E12](#e12) |

Predictions: Unlike H0, this chain predicts that targeted allele comparison in a relevant liver-cell context will show greater CTCF occupancy on G than on T.; Unlike H1, this chain predicts that editing rs7001688 will preferentially alter FAM110B expression or its contact with the variant region, rather than CYP7A1.

Falsified if: A relevant-cell allele-specific occupancy assay finds no reproducible CTCF binding difference, or finds stronger binding to T than G.; Variant perturbation produces no FAM110B expression or contact effect while producing a reproducible effect on another proposed target.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific CTCF CUT&RUN or ChIP at rs7001688 in Hep 3B2.1-7 cells, with the alleles distinguished in the assay | low | yes | No reproducible allele-specific CTCF occupancy. | Greater occupancy on T (alt) than G (ref). | Greater occupancy on G (ref) than T (alt). |
| Edit rs7001688 in an isogenic liver-cell model and measure CYP7A1 and FAM110B expression | high | no | No reproducible expression change in either candidate gene attributable to the edit. | A reproducible CYP7A1 expression change, with little or no FAM110B change. | A reproducible FAM110B expression change, with little or no CYP7A1 change. |
| Measure allele-specific chromatin contact from the variant region to CYP7A1 and FAM110B in a relevant liver-cell model | medium | no | No reproducible allele-dependent contact to either candidate gene. | An allele-dependent contact to CYP7A1. | An allele-dependent contact to FAM110B. |

## Next experiment

Perform allele-specific CTCF CUT&RUN or ChIP at rs7001688 in Hep 3B2.1-7 cells, using an assay that distinguishes G and T reads. It is the lowest-cost proposed test that directly separates the highest-probability chain, H0, from H1; an occupancy result alone would not establish the target gene or LDL-cholesterol effect.

## Investigate calls

- chip_peaks({"tf": "CTCF", "biosample": "Hep 3B2.1-7"})
- literature_search({"query": "rs7001688 CYP7A1 FAM110B LDL cholesterol"})
- gene_disease({"gene": "FAM110B"})

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

> No ENCODE CTCF ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'Hep 3B2.1-7'. Absence can also mean no CTCF experiment in that biosample. In other biosamples, 1 CTCF peaks do contain the variant: LNCAP (experiments ENCSR673WZL).

<a id="e11"></a>**E11** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs7001688%20CYP7A1%20FAM110B%20LDL%20cholesterol&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:28:59+00:00)

> Europe PMC: 0 hits for 'rs7001688 CYP7A1 FAM110B LDL cholesterol'; top 0 with PMIDs:

<a id="e12"></a>**E12** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:41:58+00:00)

> Open Targets: no association between FAM110B and free cholesterol in large LDL measurement (EFO_0022176).
