# rs7001688 and LDL cholesterol

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 9 model calls; 135 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: CTCF (bound elsewhere, z -1.87, no clear allelic change). Occupancy unknown: CASZ1 (z 32.75); SETBP1 (z 29.74); SRCAP (z 29.74); NME2 (z 28.95); TCF20 (z -20.49). Diagnostic, not shown to the model: 441 of 997 models pass Bonferroni.

## Ranked chains

### 1. null_no_tf_mediated_effect: Null: no TF-mediated allelic effect at rs7001688 (p = 0.82)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this base in liver cells; the only reported ENCODE peak is CTCF in LNCAP, not the matching liver line, and CTCF shows no clear QBiC-SELEX allelic change.; No cCRE overlaps the variant, no VEP regulatory feature is reported, and there is no GWAS Catalog, Open Targets, or GTEx eQTL support at rs7001688.; Any disease association would be due to a linked causal variant or would not be allele-specific at this base.

Falsified if: Allele-specific TF ChIP, CUT&RUN, or MPRA shows reproducible differential binding or activity at rs7001688 in Hep 3B2.1-7 or primary hepatocytes.; A liver eQTL for FAM110B, CYP7A1, or another nearby gene maps to this variant.; Fine-mapping shows rs7001688 itself, not a linked variant, drives the LDL signal.

### 2. NME2_alt_CYP7A1: NME2 binds the alt allele more strongly and may act on CYP7A1 (p = 0.08)

TF NME2 (QBiC-SELEX coverage own_model), alt allele binds more; element Same candidate unannotated distal element: no ENCODE cCRE overlaps the variant, nearest CA-H3K4me3 cCRE 1544 bp away, no VEP regulatory feature.; gene CYP7A1; cell type Hep 3B2.1-7 liver cancer line; NME2 is highly expressed there (928.15 TPM, rank 1/1626 TFs)..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NME2 is predicted by QBiC-SELEX to bind the alt T allele more strongly: own model z=28.95, effect=0.573 (alt > ref). No ENCODE NME2 ChIP-seq peak is reported over this variant in the matching liver biosample, though absence can mean no NME2 experiment there; occupancy is therefore unknown. This is SELEX-only evidence. | weak | [E15](#e15), [E19](#e19) |
| element | The variant sits in a noncoding region with no ENCODE cCRE overlap; the nearest cCRE is 1544 bp away and VEP reports no regulatory feature. It is only a candidate unannotated element, not an established active regulatory element. | supported | [E01](#e01), [E03](#e03) |
| gene | CYP7A1 lies 926.8 kb downstream of the variant, but there is no eQTL for this variant in GTEx, and Open Targets reports no association between CYP7A1 and free cholesterol in large LDL. The target-gene link is distal and speculative. | weak | [E02](#e02), [E08](#e08), [E18](#e18) |
| cell_type | NME2 is extremely highly expressed in Hep 3B2.1-7 (928.15 TPM, rank 1/1626 TFs), so it could occupy an accessible site in liver cells if one exists, but there is no direct occupancy evidence at this variant. | weak | [E15](#e15), [E19](#e19) |
| phenotype | Alt T is predicted to increase NME2 binding and could alter CYP7A1 expression and LDL cholesterol, but there is no GWAS Catalog, Open Targets, or GTEx eQTL support for rs7001688 and LDL cholesterol. The phenotype link is unsupported. | missing | [E06](#e06), [E07](#e07), [E08](#e08) |

Predictions: Alt T should increase NME2 occupancy at this site in liver cells.; NME2 perturbation should change CYP7A1 expression.; The mechanism should be sensitive to NME2 levels, which are very high in Hep 3B2.1-7.

Falsified if: NME2 ChIP, CUT&RUN, or allele-specific reporter assays in liver cells fail to show alt-specific binding at this base.; NME2 perturbation does not affect CYP7A1 expression.; No liver eQTL or fine-mapped signal links this variant to CYP7A1.

### 3. CASZ1_alt_FAM110B: CASZ1 binds the alt allele more strongly and may act on FAM110B (p = 0.06)

TF CASZ1 (QBiC-SELEX coverage own_model), alt allele binds more; element Candidate unannotated distal element: no ENCODE cCRE overlaps the variant; nearest cCRE is CA-H3K4me3 1544 bp away, and VEP reports no regulatory feature.; gene FAM110B; cell type Hep 3B2.1-7 liver cancer line; CASZ1 is expressed at low level (4.18 TPM)..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CASZ1 is predicted by QBiC-SELEX to bind the alt T allele more strongly: own model z=32.75, effect=2.741 (alt > ref). ENCODE has never assayed CASZ1 here, so occupancy is unknown; CASZ1 expression is low in Hep 3B2.1-7 (4.18 TPM). This is SELEX-only binding evidence and is weak without occupancy. | weak | [E12](#e12) |
| element | The variant sits in a noncoding region with no ENCODE cCRE overlap; the nearest cCRE is a CA-H3K4me3 1544 bp away, and VEP reports no regulatory feature. This is only a candidate unannotated element, not an established active regulatory element. | supported | [E01](#e01), [E03](#e03) |
| gene | FAM110B is the closest protein-coding gene at 420.6 kb upstream, but distance is very indirect; GTEx reports no significant eQTL for this variant, and the Europe PMC hit is a keyword match that does not establish a mechanistic FAM110B-LDL link. | weak | [E02](#e02), [E08](#e08), [E09](#e09) |
| cell_type | Hep 3B2.1-7 is a liver-cancer line, and CASZ1 is expressed there at low level (4.18 TPM), but there is no evidence that CASZ1 occupies this site in liver cells or that this line is the relevant LDL context. | weak | [E12](#e12) |
| phenotype | Alt T is predicted to increase CASZ1 binding and, through FAM110B, alter LDL cholesterol, but there is no GWAS Catalog, Open Targets, or GTEx eQTL support connecting rs7001688 to LDL cholesterol. The phenotype link is speculative. | missing | [E06](#e06), [E07](#e07), [E08](#e08) |

Predictions: Alt T should increase CASZ1 occupancy at this site in Hep 3B2.1-7 or primary hepatocytes.; CASZ1 knockdown or overexpression should change FAM110B expression.; The effect should be liver-specific and absent for other nearby genes.

Falsified if: CASZ1 ChIP, CUT&RUN, or allele-specific reporter assays in liver cells fail to show alt-specific binding at this base.; CASZ1 perturbation does not affect FAM110B expression.; No liver eQTL or fine-mapped signal connects this element to FAM110B.

### 4. TCF20_ref_FAM110B: TCF20 binds the ref allele more strongly and may act on FAM110B (p = 0.04)

TF TCF20 (QBiC-SELEX coverage own_model), ref allele binds more; element Same candidate unannotated distal element: no ENCODE cCRE overlaps the variant, nearest CA-H3K4me3 cCRE 1544 bp away, no VEP regulatory feature.; gene FAM110B; cell type Hep 3B2.1-7 liver cancer line; TCF20 is expressed there at 23.44 TPM..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF20 is predicted by QBiC-SELEX to bind the ref G allele more strongly: own model z=-20.49, effect=-0.151 (ref > alt). The effect is small, and E16 reports a higher alt site-strength percentile despite the negative effect, so the direction/strength is internally inconsistent. ENCODE has never assayed TCF20 here, so occupancy is unknown. | weak | [E16](#e16) |
| element | The variant sits in a noncoding region with no ENCODE cCRE overlap; the nearest cCRE is 1544 bp away and VEP reports no regulatory feature. It is only a candidate unannotated element, not an established active regulatory element. | supported | [E01](#e01), [E03](#e03) |
| gene | FAM110B is the closest protein-coding gene at 420.6 kb upstream, but distance is very indirect; GTEx reports no significant eQTL for this variant, and E09 does not establish a verified FAM110B-LDL mechanism. | weak | [E02](#e02), [E08](#e08), [E09](#e09) |
| cell_type | Hep 3B2.1-7 expresses TCF20 at 23.44 TPM, so TCF20 could act in this liver-cancer context if the site is occupied, but there is no occupancy evidence at this variant. | weak | [E16](#e16) |
| phenotype | Higher ref G binding of TCF20 may repress or activate FAM110B; alt T would lower TCF20 binding, but the direction of any LDL effect is unknown. There is no GWAS Catalog, Open Targets, or GTEx eQTL support for rs7001688 and LDL cholesterol. | missing | [E06](#e06), [E07](#e07), [E08](#e08) |

Predictions: Ref G should show higher TCF20 occupancy at this site than alt T in liver cells.; TCF20 perturbation should change FAM110B expression.; The direction of the LDL effect may be opposite to a simple activating model because TCF20 can act as a co-regulator.

Falsified if: TCF20 ChIP, CUT&RUN, or allele-specific reporter assays in liver cells fail to show ref-specific binding at this base.; TCF20 perturbation does not affect FAM110B expression.; No liver eQTL or fine-mapped signal connects this variant to FAM110B.

## Prediction matrix

| Test | Cost | Separates top two | null_no_tf_mediated_effect | NME2_alt_CYP7A1 | CASZ1_alt_FAM110B | TCF20_ref_FAM110B |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific NME2 ChIP-qPCR or CUT&RUN at rs7001688 in Hep 3B2.1-7 or primary hepatocytes | medium | yes | No alt-vs-ref NME2 occupancy difference at rs7001688. | Alt T shows higher NME2 occupancy than ref G. | No NME2 occupancy difference; this test does not address CASZ1. | No NME2 occupancy difference; this test does not address TCF20. |
| Allele-specific CASZ1 ChIP-qPCR, CUT&RUN, or reporter at rs7001688 in liver cells | medium | no | No alt-vs-ref CASZ1 occupancy difference at rs7001688. | No CASZ1 occupancy difference; this test does not address NME2. | Alt T shows higher CASZ1 occupancy than ref G. | No CASZ1 occupancy difference; this test does not address TCF20. |
| Allele-specific TCF20 ChIP-qPCR, CUT&RUN, or reporter at rs7001688 in liver cells | medium | no | No ref-vs-alt TCF20 occupancy difference at rs7001688. | No TCF20 occupancy difference; this test does not address NME2. | No TCF20 occupancy difference; this test does not address CASZ1. | Ref G shows higher TCF20 occupancy than alt T. |
| Liver eQTL or allele-specific reporter linking rs7001688 to CYP7A1 | high | yes | No rs7001688-associated CYP7A1 expression change in liver. | Alt T is associated with altered CYP7A1 expression in liver. | No CYP7A1 eQTL; any expression effect would be on FAM110B, not CYP7A1. | No CYP7A1 eQTL; any expression effect would be on FAM110B, not CYP7A1. |
| MPRA of rs7001688 in Hep 3B2.1-7 or primary hepatocytes | medium | no | No allele-specific regulatory activity at rs7001688. | Alt T changes regulatory activity, but this does not identify NME2. | Alt T increases regulatory activity in a liver-cell reporter. | Ref G may increase activity or repression, but the direction is not specified by TCF20 binding alone. |

## Next experiment

The single cheapest experiment that separates the top two chains is allele-specific NME2 ChIP-qPCR or CUT&RUN at rs7001688 in Hep 3B2.1-7 or primary hepatocytes. It directly tests whether the alt T allele increases NME2 occupancy at this base, as the NME2 chain predicts, versus no allele-specific occupancy as the null predicts.

## Investigate calls

- literature_search({"query": "FAM110B LDL cholesterol pravastatin"})
- gene_disease({"gene": "CYP7A1"})
- chip_peaks({"tf": "NME2", "biosample": "Hep 3B2.1-7"})

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

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:57573391:G>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000625), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 1 of 1 occupied, 5 of 112 with unknown occupancy. Left out: 382 TFs assayed in the matching biosample and 190 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z -1.87, effect -0.18: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 32.01 TPM, rank 162 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in LNCAP, e.g. ENCSR673WZL. Best model's site strength: ref 79.0th, alt 72.6th percentile of its k-mer coefficients.

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

<a id="e17"></a>**E17** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=FAM110B%20LDL%20cholesterol%20pravastatin&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:41:53+00:00)

> Europe PMC: 1 hits for 'FAM110B LDL cholesterol pravastatin'; top 1 with PMIDs:
> PMID 22666496 (2012): Genome-wide study of gene variants associated with differential cardiovascular event reduction by pravastatin therapy.

<a id="e17a"></a>**E17a** literature_search, Europe PMC abstract, PMID 22666496 (https://europepmc.org/article/MED/22666496; retrieved 2026-10-26T02:41:53+00:00)

> We have investigated the effect of genetic variation on the reduction of CHD events by pravastatin.

<a id="e17b"></a>**E17b** literature_search, Europe PMC abstract, PMID 22666496 (https://europepmc.org/article/MED/22666496; retrieved 2026-10-26T02:41:53+00:00)

> We found that one of these SNPs (rs13279522) was associated with differential CHD event reduction by pravastatin therapy in all 3 studies: P = 0.002 in CARE, P = 0.01 in WOSCOPS, P = 0.002 in PROSPER/PHASE.

<a id="e18"></a>**E18** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:31+00:00)

> Open Targets: no association between CYP7A1 and free cholesterol in large LDL measurement (EFO_0022176).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:41:57+00:00)

> No ENCODE NME2 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'Hep 3B2.1-7'. Absence can also mean no NME2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.
