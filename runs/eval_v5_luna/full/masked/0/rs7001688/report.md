# rs7001688 and LDL cholesterol

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 6 model calls; 109 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: CTCF (bound elsewhere, z -1.87, no clear allelic change, weak site). Occupancy unknown: CASZ1 (z 32.75); SETBP1 (z 29.74); SRCAP (z 29.74); NME2 (z 28.95); TCF20 (z -20.49). Diagnostic, not shown to the model: 441 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect (p = 0.80)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not produce a reproducible allele-specific TF-binding and downstream regulatory effect in a relevant liver context; any LDL association, if present, may be due to another variant or may not be causal.

Falsified if: A relevant TF shows reproducible allele-specific occupancy at this variant in liver cells and perturbing the variant or TF produces a linked cis-regulatory effect.

### 2. H1: NME2-mediated gain of binding (p = 0.12)

TF NME2 (QBiC-SELEX coverage own_model), alt allele binds more; element No regulatory element overlapping the variant is established; a functional element remains hypothetical.; gene None; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NME2 is a candidate because it is highly expressed in Hep 3B2.1-7 and its own QBiC-SELEX model predicts stronger in-vitro binding to alt T, but relevant-site occupancy is unknown. | weak | [E10](#e10), [E15](#e15) |
| element | No ENCODE cCRE overlaps the variant, so an active regulatory element at this position is not established. | supported | [E03](#e03) |
| gene | No target gene is supported; CYP7A1 is only a distant proximity candidate and no eQTL link is reported. | supported | [E02](#e02), [E08](#e08) |
| cell_type | Hep 3B2.1-7 is the stated expression context and NME2 is expressed there, but occupancy or regulatory action in this cell type has not been shown. | supported | [E15](#e15) |
| phenotype | A connection from this variant or a proposed regulatory effect to LDL cholesterol is not established. | supported | [E06](#e06), [E07](#e07) |

Predictions: NME2 should occupy the variant in relevant liver cells, with greater occupancy on alt T; disrupting the site or reducing NME2 should reduce an allele-dependent cis-regulatory effect.

Falsified if: NME2 shows no relevant-site occupancy or no alt-favoring occupancy in an adequately powered liver-cell assay.; Perturbing the variant or NME2 produces no linked cis-regulatory effect.

### 3. H2: CASZ1-mediated gain of binding (p = 0.05)

TF CASZ1 (QBiC-SELEX coverage own_model), alt allele binds more; element No regulatory element overlapping the variant is established; a functional element remains hypothetical.; gene None; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CASZ1 is a candidate because its own QBiC-SELEX model predicts a strong in-vitro increase in binding to alt T, but occupancy at the site is unknown and its expression is modest in the stated line. | weak | [E10](#e10), [E12](#e12) |
| element | No ENCODE cCRE overlaps the variant, so an active regulatory element at this position is not established. | supported | [E03](#e03) |
| gene | No target gene is supported; CYP7A1 is only a distant proximity candidate and no eQTL link is reported. | supported | [E02](#e02), [E08](#e08) |
| cell_type | CASZ1 is detected in Hep 3B2.1-7, but relevant-site occupancy or regulatory action in this cell type has not been shown. | supported | [E12](#e12) |
| phenotype | A connection from this variant or a proposed regulatory effect to LDL cholesterol is not established. | supported | [E06](#e06), [E07](#e07) |

Predictions: CASZ1 should occupy the variant in relevant liver cells, with greater occupancy on alt T; a variant-dependent cis-regulatory effect should depend on CASZ1.

Falsified if: CASZ1 shows no relevant-site occupancy or no alt-favoring occupancy in an adequately powered liver-cell assay.; Perturbing the variant or CASZ1 produces no linked cis-regulatory effect.

### 4. H3: TCF20-mediated loss of binding (p = 0.03)

TF TCF20 (QBiC-SELEX coverage own_model), ref allele binds more; element No regulatory element overlapping the variant is established; a functional element remains hypothetical.; gene None; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF20 is a lower-confidence candidate because its own QBiC-SELEX model detects slightly stronger in-vitro binding to ref G, but occupancy is unknown and the predicted site is weak. | weak | [E10](#e10), [E16](#e16) |
| element | No ENCODE cCRE overlaps the variant, so an active regulatory element at this position is not established. | supported | [E03](#e03) |
| gene | No target gene is supported; CYP7A1 is only a distant proximity candidate and no eQTL link is reported. | supported | [E02](#e02), [E08](#e08) |
| cell_type | TCF20 is expressed in Hep 3B2.1-7, but occupancy or regulatory action at this site in this cell type has not been shown. | supported | [E16](#e16) |
| phenotype | A connection from this variant or a proposed regulatory effect to LDL cholesterol is not established. | supported | [E06](#e06), [E07](#e07) |

Predictions: TCF20 should occupy the variant in relevant liver cells, with greater occupancy on ref G; a variant-dependent cis-regulatory effect should depend on TCF20.

Falsified if: TCF20 shows no relevant-site occupancy or no ref-favoring occupancy in an adequately powered liver-cell assay.; Perturbing the variant or TCF20 produces no linked cis-regulatory effect.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Measure NME2 occupancy at the variant in liver cells carrying both alleles, using targeted allele-specific CUT&RUN or an equivalent assay. | medium | yes | No reproducible alt-favoring NME2 occupancy at the variant. | NME2 occupies the variant and shows greater occupancy on alt T. | No NME2-specific alt-favoring occupancy; CASZ1, rather than NME2, is the proposed mediator. | No NME2-specific alt-favoring occupancy; TCF20, rather than NME2, is the proposed mediator. |
| Measure CASZ1 and TCF20 occupancy at the variant in relevant liver cells, with allele resolution where possible. | medium | no | No reproducible candidate-specific, allele-biased occupancy linked to the variant. | No CASZ1- or TCF20-specific allelic occupancy is expected; NME2 is the proposed mediator. | CASZ1 occupancy is detected and favors alt T. | TCF20 occupancy is detected and favors ref G. |
| Create isogenic ref and alt liver-cell lines and test for variant-dependent local chromatin or cis-expression changes, with candidate-TF perturbation. | high | yes | No reproducible variant-dependent cis-regulatory effect. | A variant-dependent cis-regulatory effect is observed and is reduced by NME2 perturbation. | A variant-dependent cis-regulatory effect is observed and is reduced by CASZ1 perturbation. | A variant-dependent cis-regulatory effect is observed and is reduced by TCF20 perturbation. |

## Next experiment

The cheapest direct test separating the top two chains is targeted allele-specific NME2 occupancy measurement at the variant in a relevant liver-cell context. A reproducible alt-favoring occupancy result would support H1 over H0; no such result would favor H0, though a negative result should be interpreted with assay sensitivity in mind.

## Refinement rounds

Stopped: round 1 left the top chain and the grades of its links unchanged.

### Round 1

- gene_disease({"gene": "CYP7A1"}) for H2.phenotype, ran as [E17](#e17). Expected: If Open Targets reports evidence linking CYP7A1 to LDL cholesterol, the phenotype link gains gene-level support for the proposed target; this would not establish that the variant regulates CYP7A1 or distinguish the TF chains. If no such evidence is returned, the phenotype link remains unsupported.

- Result of gene_disease({"gene":"CYP7A1"}): E17 reports no Open Targets association between CYP7A1 and free cholesterol in large LDL measurement. (as expected: yes)

Chains after revision: null 0.80; NME2 0.12; CASZ1 0.05; TCF20 0.03. Link grades changed: H1.element: missing → supported, H1.gene: weak → supported, H1.phenotype: missing → supported, H2.element: missing → supported, H2.gene: weak → supported, H2.phenotype: missing → supported, H3.element: missing → supported, H3.gene: weak → supported, H3.phenotype: missing → supported.

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

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:57573391:G>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000625), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 1 of 1 occupied (0 with a strong site), 5 of 112 with unknown occupancy. Left out: 382 TFs assayed in the matching biosample and 190 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element. No occupied TF has a strong site at the variant.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z -1.87, effect -0.18: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 32.01 TPM, rank 162 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in LNCAP, e.g. ENCSR673WZL. Best model's site strength: ref 79.0th, alt 72.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CASZ1 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CASZ1_FL_AG40NGGAATC_YWKC_jolma2025_0_4_7mer (its own model), z 32.75, effect 2.741: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.18 TPM, rank 776 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.1th, alt 99.8th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SETBP1 (AT hook, 2 models; QBiC-SELEX coverage: own model): best model HMGA1_FL_GA40NCTGATT_YWPA_jolma2025_0_3_7mer (a CIS-BP-mapped model of HMGA1), z 29.74, effect 2.006: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.24 TPM, rank 1043 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 67.3th, alt 96.4th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SRCAP (AT hook, 2 models; QBiC-SELEX coverage: mapped models only): best model HMGA1_FL_GA40NCTGATT_YWPA_jolma2025_0_3_7mer (a CIS-BP-mapped model of HMGA1), z 29.74, effect 2.006: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 41.42 TPM, rank 114 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 67.3th, alt 96.4th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NME2 (Unknown, 1 model; QBiC-SELEX coverage: own model): best model NME2_FL_TA40NTCACTC_YWDA_jolma2025_0_4_7mer (its own model), z 28.95, effect 0.573: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 928.15 TPM, rank 1 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.7th, alt 99.1th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF20 (Unknown, 1 model; QBiC-SELEX coverage: own model): best model TCF20_DBD_CT40NGCGCTA_YWCB_jolma2025_0_3_7mer (its own model), z -20.49, effect -0.151: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 23.44 TPM, rank 236 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 76.7th, alt 78.8th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:31+00:00)

> Open Targets: no association between CYP7A1 and free cholesterol in large LDL measurement (EFO_0022176).
