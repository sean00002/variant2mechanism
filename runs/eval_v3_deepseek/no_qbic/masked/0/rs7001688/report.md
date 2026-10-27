# rs7001688 and LDL cholesterol

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 7 model calls; 210 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (p = 0.95)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific CTCF or other TF ChIP-seq signal at chr8:57573391:G>T in hepatocyte, HepG2, or Hep 3B2.1-7 assays.; No liver active regulatory element or cCRE overlaps or is induced by the alt allele; the variant remains outside the nearest cCRE.; No reproducible liver eQTL or LDL GWAS/Open Targets signal tracks with this variant; any LDL association would be explained by a linked causal variant, chance, or a gene-level literature association not mediated by this base.

Falsified if: Allele-specific CTCF or another TF occupancy at this base is demonstrated in a relevant cell type, with a corresponding chromatin or expression change linked to LDL cholesterol.

### 2. H1: Alt allele creates a stronger CTCF site in a non-liver or ectopic context (p = 0.03)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element LNCAP-specific CTCF ChIP-seq peak, not a liver cCRE; gene FAM110B; cell type Hep 3B2.1-7 / hepatocyte expression context, but CTCF occupancy evidence is non-liver.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is the only TF with a ChIP-seq peak containing this variant in the provided evidence, but that peak is only in LNCAP; HepG2 has no CTCF peak over the variant. No QBiC-SELEX model is provided for CTCF, so the alt-more-strongly direction is speculative and not established by an allele-specific binding assay. | weak | [E04](#e04), [E05](#e05), [E10](#e10) |
| element | The variant does not overlap a cCRE; the nearest cCRE is 1544 bp away. The only CTCF peak containing the variant is LNCAP-specific, so this is at best a weak non-liver CTCF-associated element, not a supported liver regulatory element. | supported | [E03](#e03), [E04](#e04), [E05](#e05), [E10](#e10) |
| gene | FAM110B is the closest protein-coding gene at 420.6 kb upstream. E09 provides only a gene-level literature association between FAM110B and a pravastatin/cardiovascular study, not evidence that this variant regulates FAM110B; E12 reports no Open Targets association between FAM110B and free cholesterol in large LDL. | missing | [E02](#e02), [E09](#e09), [E12](#e12) |
| cell_type | CTCF is expressed in Hep 3B2.1-7 at 32.01 TPM, but the matching HepG2 biosample has zero CTCF ChIP-seq peaks over the variant; this weakens a liver-specific CTCF mechanism and confines the only occupancy signal to a non-liver context. | supported | [E04](#e04), [E05](#e05), [E10](#e10) |
| phenotype | No GTEx liver eQTL and no GTEx single-tissue eQTL are reported for this variant, and GWAS Catalog and Open Targets have no association; the LDL phenotype link is therefore not demonstrated and relies only on a distant gene-level literature hit. | missing | [E06](#e06), [E07](#e07), [E08](#e08), [E09](#e09), [E11](#e11), [E12](#e12) |

Predictions: Alt-specific CTCF ChIP-seq or ChIP-qPCR at this base in a heterozygous CTCF-expressing non-liver line such as LNCAP.; No or much weaker CTCF occupancy at this base in HepG2/Hep 3B2.1-7 unless a liver-specific co-factor recruits CTCF.; If the element is functional in liver, a positive FAM110B liver eQTL should track the alt allele; the current GTEx liver lookup does not show one.

Falsified if: No allele-specific CTCF binding is observed at this base even in LNCAP, or the variant does not alter CTCF-dependent chromatin/expression in any CTCF-relevant assay.

### 3. H2: Ref allele creates a stronger CTCF site and loss of insulation in liver (p = 0.02)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element LNCAP-specific CTCF ChIP-seq peak, not a liver cCRE; gene FAM110B; cell type Hep 3B2.1-7 / hepatocyte expression context, but CTCF occupancy evidence is non-liver.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is the only TF with a ChIP-seq peak containing this variant in the provided evidence, but that peak is only in LNCAP; HepG2 has no CTCF peak over the variant. No QBiC-SELEX model is provided for CTCF, so the ref-more-strongly direction is speculative and not established by an allele-specific binding assay. | weak | [E04](#e04), [E05](#e05), [E10](#e10) |
| element | The variant does not overlap a cCRE; the nearest cCRE is 1544 bp away. The only CTCF peak containing the variant is LNCAP-specific, so a liver insulator at this base is not supported by the epigenomic data. | supported | [E03](#e03), [E04](#e04), [E05](#e05), [E10](#e10) |
| gene | FAM110B is the closest protein-coding gene at 420.6 kb upstream. E09 provides only a gene-level literature association between FAM110B and a pravastatin/cardiovascular study, not evidence that a CTCF insulator at this variant regulates FAM110B; E12 reports no Open Targets association between FAM110B and free cholesterol in large LDL. | missing | [E02](#e02), [E09](#e09), [E12](#e12) |
| cell_type | CTCF is expressed in Hep 3B2.1-7 at 32.01 TPM, but the matching HepG2 biosample has zero CTCF ChIP-seq peaks over the variant; this weakens a liver-specific CTCF mechanism and confines the only occupancy signal to a non-liver context. | supported | [E04](#e04), [E05](#e05), [E10](#e10) |
| phenotype | No GTEx liver eQTL and no GTEx single-tissue eQTL are reported for this variant, and GWAS Catalog and Open Targets have no association; the LDL phenotype link is therefore not demonstrated and relies only on a distant gene-level literature hit. | missing | [E06](#e06), [E07](#e07), [E08](#e08), [E09](#e09), [E11](#e11), [E12](#e12) |

Predictions: Ref-specific CTCF ChIP-seq or ChIP-qPCR at this base in a heterozygous CTCF-expressing non-liver line such as LNCAP, with the alt allele reducing CTCF occupancy.; No or much weaker CTCF occupancy at this base in HepG2/Hep 3B2.1-7 unless a liver-specific co-factor recruits CTCF.; If the element is functional in liver, a negative FAM110B liver eQTL should track the alt allele; the current GTEx liver lookup does not show one.

Falsified if: No ref-specific CTCF binding is observed at this base even in LNCAP, or the variant does not alter CTCF-dependent chromatin/expression in any CTCF-relevant assay.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Reanalyze existing LNCAP CTCF ChIP-seq (ENCSR673WZL) for allele-specific read imbalance at chr8:57573391 in a heterozygous sample, or perform allele-specific CTCF ChIP-qPCR in LNCAP | low | yes | No allelic imbalance in CTCF occupancy at this base. | Alt allele shows higher CTCF occupancy. | Ref allele shows higher CTCF occupancy. |
| CTCF ChIP-seq or ChIP-qPCR over the variant in Hep 3B2.1-7 or HepG2 | medium | no | No CTCF peak over the variant. | No or weak liver CTCF peak, consistent with a non-liver/ectopic element. | No or weak liver CTCF peak, consistent with a non-liver/ectopic element. |
| Liver eQTL lookup for FAM110B or nearby genes using this variant | low | no | No liver eQTL. | If liver-relevant, positive alt-allele eQTL for FAM110B; if ectopic-only, no liver eQTL. | If liver-relevant, negative alt-allele eQTL for FAM110B; if ectopic-only, no liver eQTL. |
| MPRA or reporter assay with ref and alt alleles in CTCF-expressing cells | medium | yes | No allele-specific reporter activity. | Alt allele increases CTCF-dependent reporter activity. | Ref allele increases CTCF-dependent reporter activity. |
| CTCF perturbation with chromatin-loop or FAM110B expression readout in a CTCF-bound context | high | yes | No allele-dependent chromatin-loop or FAM110B expression change. | Alt allele strengthens a CTCF-dependent loop or changes FAM110B expression. | Ref allele strengthens a CTCF-dependent loop or changes FAM110B expression. |

## Next experiment

The cheapest test that separates the top two chains H0 and H1 is allele-specific reanalysis of existing LNCAP CTCF ChIP-seq (ENCSR673WZL) at chr8:57573391 in a heterozygous sample: H0 predicts no allelic imbalance, whereas H1 predicts alt-more CTCF occupancy and H2 predicts ref-more CTCF occupancy.

## Investigate calls

- chip_peaks({"tf": "CTCF", "biosample": "Hep 3B2.1-7"})
- eqtl_lookup({"tissue": "Liver"})
- gene_disease({"gene": "FAM110B"})

## Flags

- none

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

<a id="e11"></a>**E11** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e12"></a>**E12** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:41:58+00:00)

> Open Targets: no association between FAM110B and free cholesterol in large LDL measurement (EFO_0022176).
