# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 310 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: NKRF (bound elsewhere, z -12.31); CREB1 (bound elsewhere, z 6.24); MAX (bound elsewhere, z -2.15, no clear allelic change); ZBTB33 (bound elsewhere, z -1.92, no clear allelic change); NR2C2 (bound elsewhere, z 7.56, weak site); ZNF800 (bound elsewhere, z 6.43, weak site); RXRA (bound elsewhere, z 6.03, weak site); JUN (bound elsewhere, z 5.95, weak site); ZNF687 (bound elsewhere, z -5.31, weak site); CTCF (bound elsewhere, z -0.78, no clear allelic change, weak site). Occupancy unknown: EN1 (z 67.98); HOXA1 (z 67.98); HOXA2 (z 67.98); HOXA4 (z 67.98); HOXB2 (z 67.98). Diagnostic, not shown to the model: 296 of 997 models pass Bonferroni.

## Ranked chains

### 1. H4: Null: no TF-mediated effect of this variant (p = 0.60)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at chr5:1295601 in disease-relevant cells.; No significant TERT eQTL for this exact variant.; Any disease association is explained by a linked causal variant, another mechanism, or chance.

Falsified if: Allele-specific TF occupancy at this site is demonstrated in glioblastoma cells.; The variant changes TERT expression in an allele-specific reporter assay.; A molecular QTL or functional assay links this exact base to TERT regulation.

### 2. H1: CREB1 binds the alt allele more strongly and activates TERT (p = 0.15)

TF CREB1 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR5_C5GP enhancer near the TERT TSS; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB1 is an expressed, occupied-elsewhere candidate, but its QBiC-SELEX model is CIS-BP-mapped from CREM and shows only an in vitro alt-greater change (z 6.24, effect +0.244; alt site 98.7th percentile). ENCODE ChIP-seq over this variant is in H1 only, not glioblastoma, so CREB1 occupancy at this base in the disease context is not demonstrated. | weak | [E21](#e21), [E09](#e09), [E04](#e04) |
| element | VEP annotates the variant in an ENSR5_C5GP enhancer upstream of TERT, but no ENCODE cCRE contains the variant (nearest pELS 75 bp away), so the element assignment is annotation-only and not functionally established in glioblastoma. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, 0.5 kb from its TSS, and has the top L2G score in the only credible set, although that set is hypertension with PIP 0.00. | weak | [E02](#e02), [E16](#e16) |
| cell_type | CREB1 is expressed in glioblastoma lines (30.94 TPM) and TERT is linked to glioblastoma, but expression alone does not show CREB1 activity at this element in glioblastoma. | weak | [E21](#e21), [E18](#e18) |
| phenotype | Generic TERT-cancer literature supports a plausible telomerase-driven phenotype, but there is no variant-specific, CREB1-specific, or TERT-regulatory evidence for this base; GWAS and GTEx support are absent. | missing | [E18](#e18), [E15](#e15), [E17](#e17) |

Predictions: Alt allele A increases CREB1 occupancy at chr5:1295601 in glioblastoma cells.; CREB1 knockdown or mutation of the predicted CREB1 site reduces TERT expression.; An allele-specific TERT reporter shows higher activity for A than G in glioblastoma cells.

Falsified if: No allele-specific CREB1 binding at this site in glioblastoma cells.; CREB1 perturbation does not change TERT expression.; The G>A variant has no effect in an allele-specific TERT reporter.

### 3. H3: NKRF binds the ref allele and represses TERT; alt relieves repression (p = 0.09)

TF NKRF (QBiC-SELEX coverage own_model), ref allele binds more; element ENSR5_C5GP enhancer near the TERT TSS; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NKRF has its own QBiC-SELEX model and shows a strong ref-greater change (z -12.31, effect -0.514; ref site 99.0th percentile), but ENCODE NKRF ChIP-seq over the variant is only in GM12878 and NKRF is lowly expressed in glioblastoma (8.69 TPM), so relevant occupancy is not established. | weak | [E20](#e20), [E14](#e14), [E04](#e04) |
| element | The variant is annotated in an ENSR5_C5GP enhancer near TERT, but no ENCODE cCRE contains the variant, so this remains annotation-only in the relevant cell type. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is the closest gene and top L2G candidate, with the caveat that the credible set is hypertension with PIP 0.00. | weak | [E02](#e02), [E16](#e16) |
| cell_type | Glioblastoma is the stated context, but low NKRF expression weakens the case for an NKRF-mediated mechanism in this cell type. | weak | [E14](#e14), [E20](#e20) |
| phenotype | If NKRF represses TERT, alt-mediated loss of NKRF binding would derepress TERT and promote cancer; however, NKRF repression of TERT is not demonstrated here. | missing | [E18](#e18) |

Predictions: Ref allele G shows stronger NKRF binding than alt A.; NKRF overexpression reduces TERT expression.; Alt allele A increases TERT reporter activity by relieving NKRF repression.

Falsified if: NKRF does not bind this element in relevant cells.; NKRF activation does not repress TERT.; Alt allele does not increase TERT expression.

### 4. H2: JUN binds the alt allele more strongly and activates TERT (p = 0.08)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR5_C5GP enhancer near the TERT TSS; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN is highly expressed in glioblastoma and QBiC-SELEX reports an alt-greater change (z 5.95, effect +0.111), but the site is weak (alt 85.4th percentile). ENCODE JUN ChIP-seq over the variant is only in A549, not glioblastoma, so occupancy here is not demonstrated. | weak | [E27](#e27), [E05](#e05), [E04](#e04) |
| element | The variant is annotated as part of an ENSR5_C5GP enhancer near TERT, but no ENCODE cCRE contains the base, leaving the element assignment plausible but unproven. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is 0.5 kb from its TSS and is the best L2G gene, though the credible set has PIP 0.00 and is for hypertension. | weak | [E02](#e02), [E16](#e16) |
| cell_type | JUN expression is high in glioblastoma lines (91.65 TPM), but there is no JUN occupancy or activity evidence at this element in glioblastoma. | weak | [E05](#e05), [E27](#e27) |
| phenotype | AP-1 activation of TERT could in principle promote telomerase in these cancers, but the phenotype link is generic and not variant- or JUN-specific. | missing | [E18](#e18) |

Predictions: Alt allele A increases JUN occupancy at the variant in glioblastoma cells.; JUN knockdown reduces TERT expression.; The JUN effect, if present, is weaker than the CREB1 effect because the QBiC-SELEX site is weak.

Falsified if: No JUN occupancy at this site in glioblastoma cells.; No allele-specific JUN binding in vitro.; JUN perturbation does not affect TERT.

### 5. H5: A homeodomain TF such as HOXB2 binds the alt allele much more strongly and activates TERT (p = 0.08)

TF HOXB2 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR5_C5GP enhancer near the TERT TSS; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB2 has a QBiC-SELEX model (best model CIS-BP-mapped from HOXD4) with a very large alt-greater change (z 67.98, effect +2.073; alt site 100th percentile), but ENCODE never assayed HOXB2, so occupancy is unknown and the in vitro effect alone is weak evidence. | weak | [E34](#e34), [E04](#e04) |
| element | The variant is in an ENSR5_C5GP enhancer by VEP annotation, but no cCRE contains it and there is no glioblastoma chromatin evidence for this element. | weak | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene and highest L2G candidate, although the credible set is hypertension with PIP 0.00. | weak | [E02](#e02), [E16](#e16) |
| cell_type | HOXB2 is expressed at low-to-moderate levels in glioblastoma lines (10.25 TPM), so cell-type relevance is possible but not established. | weak | [E34](#e34) |
| phenotype | A homeodomain-TF-driven increase in TERT could contribute to telomerase activation in these cancers, but no HOXB2-TERT or variant-specific functional evidence is provided. | missing | [E18](#e18) |

Predictions: Alt allele A increases HOXB2 or related homeodomain-TF occupancy at chr5:1295601 in glioblastoma cells.; HOXB2 knockdown or mutation of the predicted site reduces TERT expression.; An allele-specific TERT reporter shows higher activity for A than G.

Falsified if: No homeodomain-TF occupancy at this site in glioblastoma cells.; HOXB2 perturbation does not affect TERT.; The G>A variant has no allele-specific effect in a TERT reporter.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H3 | H2 | H5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TERT enhancer reporter assay comparing G and A in glioblastoma cells | medium | yes | No allele-specific difference in reporter activity. | Alt A increases reporter activity, consistent with CREB1 activation if CREB1 is present. | Alt A increases reporter activity, consistent with relief of NKRF repression. | Alt A increases reporter activity, consistent with JUN activation. | Alt A increases reporter activity, consistent with homeodomain-TF activation. |
| CREB1 ChIP-qPCR or allele-specific ChIP at chr5:1295601 in glioblastoma cells | medium | yes | No allele-specific CREB1 occupancy. | Alt-biased CREB1 occupancy is detected. | No CREB1 occupancy. | No CREB1 occupancy. | No CREB1 occupancy. |
| JUN ChIP-qPCR or allele-specific ChIP at chr5:1295601 in glioblastoma cells | medium | no | No allele-specific JUN occupancy. | No JUN occupancy. | No JUN occupancy. | Alt-biased JUN occupancy is detected. | No JUN occupancy. |
| NKRF allele-specific binding and NKRF overexpression in glioblastoma cells | medium | no | No allele-specific NKRF effect. | No NKRF-dependent effect. | Ref allele binds NKRF more; NKRF overexpression represses TERT. | No NKRF-dependent effect. | No NKRF-dependent effect. |
| HOXB2 ChIP or knockdown in glioblastoma cells | high | no | No allele-specific HOXB2 occupancy or TERT effect. | No HOXB2-dependent effect. | No HOXB2-dependent effect. | No HOXB2-dependent effect. | Alt-biased HOXB2 occupancy and HOXB2-dependent TERT expression are detected. |

## Next experiment

Allele-specific TERT enhancer reporter assay comparing G and A in glioblastoma cells, with CREB1 knockdown as a secondary arm to test whether any alt-greater activity depends on CREB1.

## Investigate calls

- chip_peaks({"tf": "CREB1", "biosample": "glioblastoma"})
- chip_peaks({"tf": "JUN", "biosample": "glioblastoma"})
- literature_search({"query": "CREB1 TERT promoter transcription glioblastoma"})

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

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

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr5:1295601:G>A: 35 peaks contain the variant, from 27 factors in 9 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. No cCRE contains the variant. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, BCL3, DNMT1, DPF2, EZH2, EZH2phosphoT487, GABPB1, IKZF1, KDM4A, MAZ, MTA1, RBBP5 (+5 more). Bound, expressed TFs with a binding model: 10; listed one per row: JUN, CTCF, ZNF687, MAX, CREB1, NR2C2, RXRA, ZBTB33, ZNF800, NKRF. Assayed with no peak here: 0 TFs in the matching biosample, 563 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549 (e.g. ENCSR604CKQ). 91.65 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 16 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: H9, neural progenitor cell (e.g. ENCSR125NBL). 26.45 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 163 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR647PSR). 10.74 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 436 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: H1 (e.g. ENCSR000BSJ). 58.6 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 48 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CREB1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: H1 (e.g. ENCSR000BSN). 30.94 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 132 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C2: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR559ZKI). 20.46 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 223 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> RXRA: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR416HDG). 13.1 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 354 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZBTB33: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: K562 (e.g. ENCSR876GXA). 12.18 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 381 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF800: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR701WPG). 11.64 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 400 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NKRF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR732PJX). 8.69 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 522 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs34768248&size=100; retrieved 2026-10-26T02:22:30+00:00)

> 0 GWAS Catalog associations for rs34768248, strongest first:

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:22:30+00:00)

> 1 credible sets contain 5_1295601_G_A: 1 GWAS, 0 molecular QTL.
> GWAS Hypertension: PIP 0.00; L2G TERT 0.84
> Best L2G gene scores across these sets: TERT 0.84

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr5_1295601_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:24:03+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr5_1295601_G_A_b38. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs[masked] potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295601:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap subtype median Glioblastoma), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 10 occupied (4 with a strong site), 5 of 109 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 563 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NKRF (Unknown, 1 model; QBiC-SELEX coverage: own model): best model NKRF_DBD_CA40NCTTTGA_YWPA_jolma2025_0_3_7mer (its own model), z -12.31, effect -0.514: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.69 TPM, rank 522 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR732PJX. Best model's site strength: ref 99.0th, alt 80.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CREB1 (bZIP, 2 models; QBiC-SELEX coverage: own model): best model CREM_eDBD_TGAAGA40NATG_KO_yin2017_0_4_7mer (a CIS-BP-mapped model of CREM), z 6.24, effect 0.244: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 30.94 TPM, rank 132 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in H1, e.g. ENCSR000BSN. Best model's site strength: ref 92.9th, alt 98.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z -2.15, effect -0.147: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 58.6 TPM, rank 48 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in H1, e.g. ENCSR000BSJ. Best model's site strength: ref 99.7th, alt 94.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB33 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB33_eDBD_TAGCTG40NCTA_KR_yin2017_0_4_7mer (its own model), z -1.92, effect -0.069: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 12.18 TPM, rank 381 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in K562, e.g. ENCSR876GXA. Best model's site strength: ref 98.3th, alt 61.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model Rev-ErbA-Alpha_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of NR1D1), z 7.56, effect 0.305: alt allele binds more (|z| above the gate), but between weak k-mers. 20.46 TPM, rank 223 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR559ZKI. Best model's site strength: ref 88.5th, alt 85.0th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF800 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF800_FL_GT40NTTGGTG_YWSA_jolma2025_0_3_7mer (its own model), z 6.43, effect 0.24: alt allele binds more (|z| above the gate), but between weak k-mers. 11.64 TPM, rank 400 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR701WPG. Best model's site strength: ref 89.6th, alt 91.4th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> RXRA (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model THRB_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of THRB), z 6.03, effect 0.271: alt allele binds more (|z| above the gate), but between weak k-mers. 13.1 TPM, rank 354 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR416HDG. Best model's site strength: ref 80.3th, alt 84.4th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUN (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUN_FL_TCAGTG40NGAT_KAE_yin2017_0_3_7mer (its own model), z 5.95, effect 0.111: alt allele binds more (|z| above the gate), but between weak k-mers. 91.65 TPM, rank 16 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, e.g. ENCSR604CKQ. Best model's site strength: ref 79.1th, alt 85.4th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF687 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF687_FL_TA40NGTTAGC_YWL_jolma2025_0_3_7mer (its own model), z -5.31, effect -0.304: ref allele binds more (|z| above the gate), but between weak k-mers. 10.74 TPM, rank 436 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR647PSR. Best model's site strength: ref 96.9th, alt 85.7th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z -0.78, effect -0.094: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 26.45 TPM, rank 163 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in H9, neural progenitor cell, e.g. ENCSR125NBL. Best model's site strength: ref 87.7th, alt 93.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EN1 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.13 TPM, rank 810 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXA1 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.76 TPM, rank 1026 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXA2 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.08 TPM, rank 1100 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXA4 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.44 TPM, rank 875 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXB2 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model HOXD4_FL_TTTACT40NACA_KV_yin2017_0_3_7mer (a CIS-BP-mapped model of HOXD4), z 67.98, effect 2.073: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 10.25 TPM, rank 454 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:44:41+00:00)

> No ENCODE CREB1 ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'glioblastoma'. Absence can also mean no CREB1 experiment in that biosample. In other biosamples, 1 CREB1 peaks do contain the variant: H1 (experiments ENCSR000BSN).

<a id="e36"></a>**E36** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:33:47+00:00)

> No ENCODE JUN ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'glioblastoma'. Absence can also mean no JUN experiment in that biosample. In other biosamples, 2 JUN peaks do contain the variant: A549 (experiments ENCSR604CKQ, ENCSR628MQN).

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=CREB1%20TERT%20promoter%20transcription%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:47:21+00:00)

> Europe PMC: 75 hits for 'CREB1 TERT promoter transcription glioblastoma'; top 8 with PMIDs:
> PMID 40205485 (2025): ELK4 induced upregulation of HOMER3 promotes the proliferation and metastasis in glioma via Wnt/β-catenin/EMT signaling pathway.
> PMID 42186257 (2026): Natural Plant Bioactives as Regulators of Histone Modifications: Bridging Epigenetics and Anticancer Therapy.
> PMID 42274584 (2026): The Signaling Networks of TIM-3, TGF-β, and STING in Glioblastoma.
> PMID 40959438 (2025): The evolution and application of multi-omic analysis for pituitary neuroendocrine tumors.
> PMID 39525666 (2024): Bioinformatic and clinical experimental assay uncovers resistance and susceptibility mechanisms of human glioblastomas to temozolomide and identifies new combined and individual survival biomarkers outperforming <i>MGMT</i> promoter methylation.
> PMID 39327692 (2024): What's new in neuropathology 2024: CNS WHO 5th edition updates.
> PMID 42287329 (2026): The Hippo signaling pathway in pediatric brain tumors: molecular mechanisms and therapeutic opportunities.
> PMID 42764959 (2026): Deconvoluting the multi-faceted roles of alternative splicing events in cancer: From underlying mechanisms to innovative therapeutics.
