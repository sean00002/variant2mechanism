# rs7001688 and LDL cholesterol

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 198 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: CTCF (bound elsewhere, z -1.87, no clear allelic change, weak site). Occupancy unknown: CASZ1 (z 32.75); SETBP1 (z 29.74); SRCAP (z 29.74); NME2 (z 28.95); TCF20 (z -20.49). Diagnostic, not shown to the model: 441 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0_null_linked_or_passenger: No TF-mediated allelic effect at this base (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at chr8:57573391 in Hep 3B2.1-7 or HepG2, including no allele-specific NME2 or CASZ1 binding.; No allele-specific chromatin contact or eQTL for nearby genes, including FAM110B and CYP7A1.; Any LDL-cholesterol association at this locus is due to a linked causal variant or a passenger mutation, not to this base.

Falsified if: Allele-specific TF occupancy and allele-specific target-gene regulation are demonstrated at this exact base in hepatocyte-like cells.; A distal contact or eQTL specifically tracks the G/T allele and is abolished when the base is edited.

### 2. H1_NME2_FAM110B: NME2 binds the alt allele more strongly and distally regulates FAM110B (p = 0.22)

TF NME2 (QBiC-SELEX coverage own_model), alt allele binds more; element poorly annotated distal non-cCRE element; gene FAM110B; cell type Hep 3B2.1-7 hepatocyte-like liver cancer line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NME2 is predicted to bind the alt T allele more strongly than the ref G allele: its own QBiC-SELEX model detects an alt-favoring change (z 28.95, effect +0.573; gate passed), and the alt site is strong (99.1st versus ref 65.7th percentile). NME2 is highly expressed in Hep 3B2.1-7 (928.15 TPM, rank 1/1626). However, ENCODE did not assay NME2 here and reports no NME2 ChIP peak over the variant in HepG2, so occupancy is unknown; this is SELEX-plus-expression evidence, not ChIP occupancy. | weak | [E15](#e15), [E17](#e17) |
| element | The variant lies in a poorly annotated distal non-coding region: it is intronic/intergenic with no overlapping cCRE, the nearest cCRE is 1544 bp away, and there is no HepG2 ChIP peak over the variant in the supplied ENCODE call. This describes the element but does not demonstrate enhancer activity. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | The distal element could regulate FAM110B, the nearest protein-coding gene at 420.6 kb upstream, and FAM110B is the only nearby gene with an LDL-cholesterol literature hit in the supplied evidence. But GTEx reports no significant eQTL globally or in liver, and the literature hit is not variant-specific, so the element-to-FAM110B link is unsupported. | missing | [E02](#e02), [E08](#e08), [E19](#e19), [E09](#e09) |
| cell_type | The relevant cell context is the hepatocyte-like liver cancer line Hep 3B2.1-7, with HepG2 as the ENCODE stand-in; NME2 is highly expressed in this line. | supported | [E04](#e04), [E15](#e15) |
| phenotype | Allele-specific NME2 binding could alter FAM110B expression and thereby LDL cholesterol, but this variant has no GWAS Catalog record, no Open Targets record, and no significant GTEx eQTL globally or in liver. The phenotype link is plausible but not established. | missing | [E06](#e06), [E07](#e07), [E08](#e08), [E19](#e19), [E09](#e09) |

Predictions: NME2 ChIP/CUT&RUN or allele-specific footprinting at the variant in Hep 3B2.1-7 shows stronger NME2 occupancy on the alt T allele.; Chromatin contact methods show a loop between chr8:57573391 and the FAM110B promoter in hepatocyte-like cells.; FAM110B expression is allele-specifically altered in hepatocyte-like cells in a NME2-dependent manner.

Falsified if: NME2 does not occupy the variant or shows no allele-specific binding in Hep 3B2.1-7.; No chromatin contact or allele-specific FAM110B expression is detected.; NME2 perturbation does not change FAM110B expression or the LDL-relevant phenotype.

### 3. H3_CASZ1_FAM110B: CASZ1 binds the alt allele more strongly and distally regulates FAM110B (p = 0.15)

TF CASZ1 (QBiC-SELEX coverage own_model), alt allele binds more; element poorly annotated distal non-cCRE element; gene FAM110B; cell type Hep 3B2.1-7 hepatocyte-like liver cancer line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CASZ1 is predicted to bind the alt T allele more strongly than the ref G allele: its own QBiC-SELEX model gives a strong alt-favoring change (z 32.75, effect +2.741; gate passed) and a strong alt site (99.8th versus ref 99.1st percentile). CASZ1 is expressed at only 4.18 TPM (rank 776/1626) in Hep 3B2.1-7, and ENCODE never assayed CASZ1 here; no CASZ1 ChIP peak is reported over the variant in HepG2. Occupancy is therefore unknown, and the low expression makes this claim weak. | weak | [E12](#e12), [E18](#e18) |
| element | The variant lies in a poorly annotated distal non-coding region: it is intronic/intergenic with no overlapping cCRE, the nearest cCRE is 1544 bp away, and there is no HepG2 ChIP peak over the variant. This describes the element but does not demonstrate regulatory activity. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | The distal element could regulate FAM110B, the nearest protein-coding gene at 420.6 kb upstream, and FAM110B is the only nearby gene with an LDL-cholesterol literature hit in the supplied evidence. But GTEx reports no significant eQTL globally or in liver, and the literature hit is not variant-specific, so the element-to-FAM110B link is unsupported. | missing | [E02](#e02), [E08](#e08), [E19](#e19), [E09](#e09) |
| cell_type | The relevant cell context is the hepatocyte-like liver cancer line Hep 3B2.1-7, with HepG2 as the ENCODE stand-in; CASZ1 is expressed there at a low but detectable level. | supported | [E04](#e04), [E12](#e12) |
| phenotype | Allele-specific CASZ1 binding could alter FAM110B expression and thereby LDL cholesterol, but this variant has no GWAS Catalog record, no Open Targets record, and no significant GTEx eQTL globally or in liver. The phenotype link is speculative. | missing | [E06](#e06), [E07](#e07), [E08](#e08), [E19](#e19), [E09](#e09) |

Predictions: CASZ1 ChIP/CUT&RUN in Hep 3B2.1-7 shows allele-specific occupancy at the variant if CASZ1 is expressed and occupies the site.; Chromatin contact methods show a loop between chr8:57573391 and the FAM110B promoter.; CASZ1 perturbation changes FAM110B expression, whereas NME2 perturbation does not.

Falsified if: CASZ1 does not occupy the variant in Hep 3B2.1-7 or shows no allele-specific binding.; CASZ1 expression is too low to support occupancy and no chromatin contact is found.; NME2, rather than CASZ1, explains allele-specific occupancy and FAM110B regulation.

### 4. H2_NME2_CYP7A1: NME2 binds the alt allele more strongly and distally regulates CYP7A1 (p = 0.08)

TF NME2 (QBiC-SELEX coverage own_model), alt allele binds more; element poorly annotated distal non-cCRE element; gene CYP7A1; cell type Hep 3B2.1-7 hepatocyte-like liver cancer line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NME2 is predicted to bind the alt T allele more strongly than the ref G allele: its own QBiC-SELEX model detects an alt-favoring change (z 28.95, effect +0.573; gate passed), and the alt site is strong. NME2 is highly expressed in Hep 3B2.1-7. However, ENCODE did not assay NME2 here and reports no NME2 ChIP peak over the variant in HepG2, so occupancy is unknown; this is SELEX-plus-expression evidence only. | weak | [E15](#e15), [E17](#e17) |
| element | The variant lies in a poorly annotated distal non-coding region: it is intronic/intergenic with no overlapping cCRE, the nearest cCRE is 1544 bp away, and there is no HepG2 ChIP peak over the variant. This describes the element but does not demonstrate regulatory activity. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | The distal element could instead regulate CYP7A1, which lies 926.8 kb downstream and is a biological LDL-cholesterol candidate, but there is no chromatin-contact, perturbation, or eQTL evidence linking this variant to CYP7A1. GTEx reports no significant eQTL globally or in liver. | missing | [E02](#e02), [E08](#e08), [E19](#e19) |
| cell_type | The relevant cell context is the hepatocyte-like liver cancer line Hep 3B2.1-7, with HepG2 as the ENCODE stand-in; NME2 is highly expressed in this line. | supported | [E04](#e04), [E15](#e15) |
| phenotype | Distal NME2-dependent regulation of CYP7A1 in hepatocytes could change bile-acid synthesis and LDL cholesterol, but there is no variant-level GWAS, Open Targets, or eQTL evidence at this variant. The phenotype link is speculative. | missing | [E06](#e06), [E07](#e07), [E08](#e08), [E19](#e19) |

Predictions: NME2 occupies the variant allele-specifically in Hep 3B2.1-7.; Chromatin contact methods show a loop between chr8:57573391 and the CYP7A1 promoter, not the FAM110B promoter.; CYP7A1 expression is allele-specifically altered in hepatocyte-like cells.

Falsified if: No chromatin contact between the variant and CYP7A1 is detected.; CYP7A1 expression is not allele-specifically changed in hepatocyte-like cells.; The contact is instead to FAM110B or another gene.

## Prediction matrix

| Test | Cost | Separates top two | H0_null_linked_or_passenger | H1_NME2_FAM110B | H3_CASZ1_FAM110B | H2_NME2_CYP7A1 |
| --- | --- | --- | --- | --- | --- | --- |
| NME2 ChIP-qPCR or CUT&RUN over chr8:57573391 in Hep 3B2.1-7, with allele-specific readout if the line is heterozygous | low | yes | No NME2 occupancy at the variant, or occupancy with no allelic bias. | NME2 occupies the variant and, if heterozygous, binds the alt T allele more strongly. | No requirement for NME2 occupancy; NME2 may be absent or non-allelic. | NME2 occupies the variant and, if heterozygous, binds the alt T allele more strongly. |
| CASZ1 ChIP-qPCR or CUT&RUN over chr8:57573391 in Hep 3B2.1-7, with allele-specific readout if heterozygous | low | no | No CASZ1 occupancy at the variant, or no allelic bias. | No requirement for CASZ1 occupancy; CASZ1 may be absent or non-allelic. | CASZ1 occupies the variant and, if heterozygous, binds the alt T allele more strongly. | No requirement for CASZ1 occupancy; CASZ1 may be absent or non-allelic. |
| Liver eQTL or allele-specific expression assay for FAM110B and CYP7A1 in hepatocyte-like cells | medium | yes | No allele-specific expression of FAM110B or CYP7A1 tracking the G/T allele. | Allele-specific FAM110B expression in liver/hepatocyte-like cells. | Allele-specific FAM110B expression in liver/hepatocyte-like cells. | Allele-specific CYP7A1 expression in liver/hepatocyte-like cells. |
| Chromatin contact assay (Hi-C, 4C, or promoter capture) from chr8:57573391 to FAM110B or CYP7A1 in hepatocyte-like cells | high | yes | No specific contact between the variant and either promoter beyond background. | Specific contact between the variant and the FAM110B promoter. | Specific contact between the variant and the FAM110B promoter. | Specific contact between the variant and the CYP7A1 promoter. |

## Next experiment

The cheapest experiment separating the top two chains (H0 null vs H1_NME2_FAM110B) is NME2 ChIP-qPCR or CUT&RUN over chr8:57573391 in Hep 3B2.1-7, ideally with allele-specific readout in a heterozygous line. H1 predicts NME2 occupancy with stronger alt T binding; H0 predicts no NME2 occupancy or no allelic bias.

## Investigate calls

- chip_peaks({"tf": "NME2", "biosample": "HepG2"})
- chip_peaks({"tf": "CASZ1", "biosample": "HepG2"})
- eqtl_lookup({"tissue": "Liver"})

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

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:41:57+00:00)

> No ENCODE NME2 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no NME2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:39:54+00:00)

> No ENCODE CASZ1 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no CASZ1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).
