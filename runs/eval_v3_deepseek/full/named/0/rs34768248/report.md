# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 9 model calls; 267 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: NKRF (bound elsewhere, z -12.31); CREB1 (bound elsewhere, z 6.24); MAX (bound elsewhere, z -2.15, no clear allelic change); ZBTB33 (bound elsewhere, z -1.92, no clear allelic change); NR2C2 (bound elsewhere, z 7.56, weak site); ZNF800 (bound elsewhere, z 6.43, weak site); RXRA (bound elsewhere, z 6.03, weak site); JUN (bound elsewhere, z 5.95, weak site); ZNF687 (bound elsewhere, z -5.31, weak site); CTCF (bound elsewhere, z -0.78, no clear allelic change, weak site). Occupancy unknown: EN1 (z 67.98); HOXA1 (z 67.98); HOXA2 (z 67.98); HOXA4 (z 67.98); HOXB2 (z 67.98). Diagnostic, not shown to the model: 296 of 997 models pass Bonferroni.

## Ranked chains

### 1. null_no_tf_mediated_effect: No TF-mediated effect of rs34768248 (p = 0.53)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this base in the relevant cell type.; No direct effect of this SNP on TERT expression after controlling for linked variants.; Any disease association is due to a linked causal variant, passenger status, or no true allelic effect.

Falsified if: A matched-biosample ChIP or reporter assay shows allele-specific TF occupancy at this base.; A cis-eQTL or fine-mapping experiment shows this variant directly changes TERT expression.; Functional dissection shows the disease signal is caused by this variant rather than a linked variant.

### 2. NKRF_loss_of_repression: NKRF-binding loss may derepress TERT (p = 0.26)

TF NKRF (QBiC-SELEX coverage own_model), ref allele binds more; element ENSR5_C5GP enhancer near TERT-associated cCREs; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NKRF is the leading non-null candidate but occupancy in the disease context is unresolved: NKRF has its own QBiC-SELEX model and the ref G allele binds more strongly than alt A (effect -0.514, z -12.31), with the ref allele at the 99.0th percentile, a strong site. ENCODE ChIP-seq has an NKRF peak over the variant only in GM12878, not glioblastoma; E36 reports no glioblastoma-matching NKRF peak, and E04 states no ENCODE biosample matches the expression context. NKRF is chosen over other ChIP-positive expressed TFs because it has the clearest strong-site allelic effect in this set, but this is not evidence of NKRF occupancy in glioblastoma. | weak | [E20](#e20), [E14](#e14), [E36](#e36), [E04](#e04) |
| element | The variant lies within the Ensembl enhancer ENSR5_C5GP and within 75 bp of TERT-associated pELS/PLS cCREs; no cCRE directly overlaps the variant, so the element assignment is annotation-level. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene at 0.5 kb upstream and has the best L2G score, 0.84; the L2G comes from a hypertension credible set with PIP 0.00, not a cancer GWAS or molecular QTL. | weak | [E02](#e02), [E16](#e16) |
| cell_type | NKRF is expressed in DepMap glioblastoma lines, but only at 8.69 TPM, rank 522 of 1626 TFs; glioblastoma is the provided expression context, and TERT is broadly relevant in glioblastoma, melanoma, and bladder cancer literature. | weak | [E20](#e20), [E18](#e18) |
| phenotype | The phenotype link is conditional and unproven: if NKRF represses TERT, weaker NKRF binding on alt A would derepress TERT and increase telomerase activity. E35 did not identify direct NKRF-TERT repression evidence, so this direction remains an assumption. | missing | [E18](#e18), [E35](#e35) |

Predictions: NKRF occupies this element in glioblastoma cells and ref G binds NKRF more than alt A.; If NKRF represses TERT, alt A increases TERT expression and NKRF depletion mimics the alt allele.; The alt-associated TERT increase is reduced or abolished when NKRF is overexpressed.

Falsified if: Allele-specific NKRF ChIP shows no NKRF occupancy or no ref-greater binding at this base in glioblastoma cells.; NKRF depletion does not change TERT expression in glioblastoma cells.; NKRF acts as an activator rather than a repressor of TERT.

### 3. CREB1_gain_of_activation: CREB1-binding gain may activate TERT (p = 0.14)

TF CREB1 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR5_C5GP enhancer near TERT-associated cCREs; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CREB1 is a secondary candidate: its QBiC-SELEX model is CIS-BP-mapped from CREM, so it reflects CREB/CREM family specificity rather than a CREB1-only model. It shows alt A binds more strongly than ref G (effect 0.244, z 6.24), with the alt allele at the 98.7th percentile, a strong site. ENCODE ChIP-seq has a CREB1 peak over the variant only in H1, not glioblastoma; occupancy in the disease context is not established. | weak | [E21](#e21), [E09](#e09), [E04](#e04) |
| element | The variant lies within ENSR5_C5GP and near TERT-associated pELS/PLS cCREs, consistent with a TERT regulatory element, though no cCRE directly overlaps the variant. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene at 0.5 kb upstream and the best L2G gene at this locus, with the same hypertension/PIP 0.00 caveat. | weak | [E02](#e02), [E16](#e16) |
| cell_type | CREB1 is expressed in DepMap glioblastoma lines at 30.94 TPM, rank 132 of 1626 TFs; TERT relevance in glioblastoma, melanoma, and bladder cancer is supported only by broad literature. | weak | [E21](#e21), [E18](#e18) |
| phenotype | The phenotype link is conditional and unproven: if CREB1 activates TERT, stronger CREB1 binding on alt A would increase TERT expression. E37 did not provide specific CREB1-TERT activation evidence, so this direction remains an assumption. | missing | [E18](#e18), [E37](#e37) |

Predictions: CREB1 occupies this element in a permissive cell type and alt A increases CREB1 occupancy.; If CREB1 activates TERT, alt A increases TERT expression and CREB1 knockdown reduces the alt-associated increase.; The effect requires the CREB/CREM family site at this base.

Falsified if: CREB1 does not occupy this element in glioblastoma cells.; Allele-specific CREB1 ChIP shows no alt-greater binding at this base.; CREB1 perturbation does not affect TERT expression in the relevant cells.

### 4. JUN_weak_gain_of_activation: JUN weak-site gain may activate TERT (p = 0.07)

TF JUN (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR5_C5GP enhancer near TERT-associated cCREs; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | JUN has its own QBiC-SELEX model showing alt A binds more strongly than ref G (effect 0.111, z 5.95), but the site is weak on both alleles, with the better allele at only the 85.4th percentile. ENCODE ChIP-seq has a JUN peak over the variant only in A549, not glioblastoma; JUN is highly expressed in glioblastoma, but the weak site makes it unlikely that JUN acts through this exact base. | weak | [E27](#e27), [E05](#e05), [E04](#e04) |
| element | The variant lies within ENSR5_C5GP and near TERT-associated pELS/PLS cCREs, consistent with a TERT regulatory element, though direct regulatory function in glioblastoma is not shown. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene and best L2G gene at this locus, with the hypertension/PIP 0.00 caveat. | weak | [E02](#e02), [E16](#e16) |
| cell_type | JUN is strongly expressed in DepMap glioblastoma lines at 91.65 TPM, rank 16 of 1626 TFs; TERT disease relevance rests on broad literature only. | weak | [E27](#e27), [E18](#e18) |
| phenotype | The phenotype link is conditional and unproven: if JUN activates TERT through this element, the small alt-gain in JUN binding would weakly increase TERT expression. No cited evidence establishes JUN-TERT regulation at this element. | missing | [E18](#e18) |

Predictions: JUN occupancy at this element is weak and alt A produces at most a small increase.; JUN perturbation changes TERT expression only if this element is active in the tested cell type.; The effect is smaller than for a strong-site TF such as NKRF.

Falsified if: JUN does not occupy this element in glioblastoma cells.; The site is too weak for JUN to act through this base in vivo.; JUN perturbation does not change TERT expression.

## Prediction matrix

| Test | Cost | Separates top two | null_no_tf_mediated_effect | NKRF_loss_of_repression | CREB1_gain_of_activation | JUN_weak_gain_of_activation |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific NKRF ChIP-qPCR in a glioblastoma line heterozygous at rs34768248 | medium | yes | No allele-specific NKRF occupancy at this base; no TF-mediated effect. | NKRF occupies the element and ref G has higher NKRF signal than alt A. | No NKRF allele-specific occupancy; CREB1 is not tested by this assay. | No NKRF allele-specific occupancy; JUN is not tested by this assay. |
| NKRF knockdown or overexpression followed by TERT expression in glioblastoma cells | medium | yes | No NKRF-dependent TERT expression change and no allele-specific effect. | NKRF depletion increases TERT and mimics the alt allele; NKRF overexpression reduces TERT. | NKRF perturbation does not explain the TERT effect; CREB1 would need separate perturbation. | NKRF perturbation does not explain the TERT effect; JUN would need separate perturbation. |
| CREB1 ChIP-qPCR in glioblastoma cells at this element | medium | no | No allele-specific CREB1 occupancy at this base. | No CREB1 allele-specific occupancy required; NKRF chain remains untested. | CREB1 occupies the element and alt A has higher CREB1 signal than ref G. | No CREB1 allele-specific occupancy required; JUN chain remains untested. |
| JUN ChIP-qPCR in glioblastoma cells at this element | medium | no | No allele-specific JUN occupancy at this base. | No JUN allele-specific occupancy required; NKRF chain remains untested. | No JUN allele-specific occupancy required; CREB1 chain remains untested. | JUN occupies the element weakly and alt A may have slightly higher JUN signal. |
| TERT reporter assay comparing ref G and alt A in glioblastoma cells, with and without NKRF perturbation | high | yes | No allele-specific reporter difference after controlling for linked sequences. | Alt A increases TERT reporter activity; NKRF knockdown increases activity and reduces the ref/alt difference; NKRF overexpression reduces activity. | Alt A increases TERT reporter activity; CREB1 perturbation, not NKRF perturbation, affects the difference. | Alt A produces at most a small increase; JUN perturbation, not NKRF perturbation, affects the difference. |
| TERT expression by rs34768248 genotype in glioblastoma cohorts or cell lines | low | yes | No direct genotype-TERT expression association after controlling for linked variants. | Alt A associates with higher TERT expression, consistent with loss of NKRF repression. | Alt A associates with higher TERT expression, consistent with gain of CREB1 activation. | Alt A associates with a small or no increase in TERT expression. |

## Next experiment

Allele-specific NKRF ChIP-qPCR in a glioblastoma cell line heterozygous for rs34768248, using an NKRF antibody and allele-discriminating ddPCR. This directly tests the top non-null chain's key missing link, NKRF occupancy and ref-greater binding in the disease context, and separates it from the null chain. Existing ENCODE data do not provide a glioblastoma NKRF peak, and E36 notes that absence may reflect no experiment rather than no occupancy.

## Investigate calls

- literature_search({"query": "NKRF TERT repression telomerase"})
- chip_peaks({"tf": "NKRF", "biosample": "glioblastoma"})
- literature_search({"query": "TERT promoter CREB1 transcription activation glioblastoma"})

## Flags

- literature_fallback: no hits for 'rs34768248 AND TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; dropped the rsID
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
> PMID 42804732 (2026): SNP rs2853669 potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
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

<a id="e35"></a>**E35** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=NKRF%20TERT%20repression%20telomerase&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:24:13+00:00)

> Europe PMC: 3 hits for 'NKRF TERT repression telomerase'; top 2 with PMIDs:
> PMID 40320716 (2025): Recent advances in nuclear actin research.
> PMID 34131406 (2021): Progress of Breast Cancer basic research in China.

<a id="e36"></a>**E36** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:44:40+00:00)

> No ENCODE NKRF ChIP-seq peak contains chr5:1295601:G>A in biosamples matching 'glioblastoma'. Absence can also mean no NKRF experiment in that biosample. In other biosamples, 1 NKRF peaks do contain the variant: GM12878 (experiments ENCSR732PJX).

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20promoter%20CREB1%20transcription%20activation%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:24:14+00:00)

> Europe PMC: 70 hits for 'TERT promoter CREB1 transcription activation glioblastoma'; top 8 with PMIDs:
> PMID 42274584 (2026): The Signaling Networks of TIM-3, TGF-β, and STING in Glioblastoma.
> PMID 42186257 (2026): Natural Plant Bioactives as Regulators of Histone Modifications: Bridging Epigenetics and Anticancer Therapy.
> PMID 40205485 (2025): ELK4 induced upregulation of HOMER3 promotes the proliferation and metastasis in glioma via Wnt/β-catenin/EMT signaling pathway.
> PMID 40959438 (2025): The evolution and application of multi-omic analysis for pituitary neuroendocrine tumors.
> PMID 39525666 (2024): Bioinformatic and clinical experimental assay uncovers resistance and susceptibility mechanisms of human glioblastomas to temozolomide and identifies new combined and individual survival biomarkers outperforming <i>MGMT</i> promoter methylation.
> PMID 42287329 (2026): The Hippo signaling pathway in pediatric brain tumors: molecular mechanisms and therapeutic opportunities.
> PMID 42764959 (2026): Deconvoluting the multi-faceted roles of alternative splicing events in cancer: From underlying mechanisms to innovative therapeutics.
> PMID 42706376 (2026): Immune pathway activation in gastric cancers with LINE-1 retrotransposon overexpression and homologous recombination deficiency.
