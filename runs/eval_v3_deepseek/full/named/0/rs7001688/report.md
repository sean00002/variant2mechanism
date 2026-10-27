# rs7001688 and LDL cholesterol

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 142 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: CTCF (bound elsewhere, z -1.87, no clear allelic change, weak site). Occupancy unknown: CASZ1 (z 32.75); SETBP1 (z 29.74); SRCAP (z 29.74); NME2 (z 28.95); TCF20 (z -20.49). Diagnostic, not shown to the model: 441 of 997 models pass Bonferroni.

## Ranked chains

### 1. null_no_tf_effect: No TF-mediated effect of rs7001688 (p = 0.88)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this base in liver cells.; The only ChIP-supported TF, CTCF, is bound over the variant only in LNCAP, has no clear QBiC-SELEX allelic change, and has no HepG2 peak, so it does not support a liver allele-specific mechanism.; Any LDL-cholesterol association would be due to linkage disequilibrium with another causal variant, or rs7001688 would be a passenger variant.

Falsified if: Allele-specific TF occupancy, a reporter assay, or CRISPR base editing shows that this exact variant changes expression in liver cells.; Fine-mapping or functional assays show that rs7001688 itself, rather than a linked variant, is causal for LDL cholesterol.

### 2. NME2_alt_cryptic_site: NME2 gains binding on the alt allele at a cryptic site and changes FAM110B expression (p = 0.07)

TF NME2 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in an unannotated intronic/intergenic region with no overlapping cCRE and no cCRE within 500 bp; the nearest H3K4me3 cCRE is 1544 bp away. The QBiC-SELEX summary also notes that no occupied TF has a strong site at the variant, so a functional cryptic NME2 element is unproven.; gene FAM110B; cell type Hepatocyte/liver-cancer line context (Hep 3B2.1-7; HepG2 as ENCODE liver-cancer stand-in).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NME2 is predicted to bind the alt T allele more strongly in vitro: its own QBiC-SELEX model gives z=28.95, effect=0.573, and the alt site reaches the 99.1st percentile. NME2 is very highly expressed in Hep 3B2.1-7 (928.15 TPM, rank 1/1626 TFs). However, ENCODE has no NME2 ChIP peak in HepG2, and absence can also mean no NME2 experiment in that biosample, so occupancy at this variant is unknown. | weak | [E15](#e15), [E18](#e18), [E04](#e04) |
| element | The variant is not in an annotated cCRE and no cCRE is within 500 bp, so this would require an unannotated allele-specific NME2 binding element. The QBiC-SELEX summary adds that no occupied TF has a strong site at the variant, leaving the element speculative. | weak | [E01](#e01), [E03](#e03), [E04](#e04), [E10](#e10) |
| gene | FAM110B is the nearest protein-coding gene at 420.6 kb, but there is no liver eQTL for the variant, no GWAS Catalog or Open Targets record for the variant, and no Open Targets association between FAM110B and free cholesterol in large LDL. E09 is only gene-level literature and does not establish variant-to-FAM110B regulation. | weak | [E02](#e02), [E08](#e08), [E17](#e17), [E19](#e19), [E09](#e09), [E06](#e06), [E07](#e07) |
| cell_type | The liver/hepatocyte-like context is expression-compatible because NME2 is highly expressed in Hep 3B2.1-7, but NME2 occupancy at this variant is untested and no NME2 ChIP peak is reported in HepG2. | weak | [E15](#e15), [E18](#e18), [E04](#e04) |
| phenotype | Allele-specific NME2 binding could alter FAM110B expression and LDL cholesterol, but this is inferential: there is no variant-level LDL cholesterol or statin-response evidence for rs7001688, and the FAM110B disease link is weak or absent in Open Targets. | weak | [E09](#e09), [E06](#e06), [E07](#e07), [E19](#e19) |

Predictions: Allele-specific NME2 ChIP or CUT&RUN in liver cells should show stronger T-allele occupancy at rs7001688.; A liver eQTL or allele-specific reporter should show that the T allele alters FAM110B expression if this chain is correct.

Falsified if: NME2 ChIP/CUT&RUN in liver cells shows no occupancy or no allele-specific binding at rs7001688.; Allele-specific reporter or CRISPR base editing shows no effect of the T allele on FAM110B expression or an LDL-related readout.; No eQTL, chromatin-loop, or perturbation evidence connects this variant to FAM110B.

### 3. CASZ1_alt_cryptic_site: CASZ1 gains binding on the alt allele at a non-canonical site (p = 0.03)

TF CASZ1 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant is in an unannotated intronic/intergenic region with no overlapping cCRE and no cCRE within 500 bp, so a CASZ1-bound element here would be unannotated and unproven.; gene FAM110B; cell type Hepatocyte/liver-cancer line context (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CASZ1 is predicted to bind the alt T allele more strongly in vitro: its own QBiC-SELEX model gives z=32.75, effect=2.741, and the alt site reaches the 99.8th percentile. CASZ1 is only lowly expressed in Hep 3B2.1-7 (4.18 TPM, rank 776/1626), and ENCODE never assayed CASZ1, so occupancy is unknown. | weak | [E12](#e12), [E04](#e04), [E10](#e10) |
| element | No cCRE overlaps the variant and no cCRE is within 500 bp; the nearest H3K4me3 cCRE is 1544 bp away. This supports only an unannotated region, not a functional CASZ1 element. | weak | [E01](#e01), [E03](#e03), [E10](#e10) |
| gene | FAM110B is the nearest protein-coding gene at 420.6 kb, but there is no liver eQTL for the variant and no variant-level GWAS/Open Targets record; Open Targets also shows no FAM110B association with free cholesterol in large LDL. Direct CASZ1-to-FAM110B regulation is not established. | weak | [E02](#e02), [E08](#e08), [E17](#e17), [E19](#e19), [E09](#e09), [E06](#e06), [E07](#e07) |
| cell_type | CASZ1 expression is detectable in Hep 3B2.1-7, but at low level, so this chain requires a functional effect despite low TF abundance and unknown occupancy. | weak | [E12](#e12) |
| phenotype | If the alt allele increases CASZ1 binding and CASZ1 regulates FAM110B, this could contribute to LDL cholesterol variation, but the direction and target gene are hypothetical and lack variant-level LDL evidence. | weak | [E09](#e09), [E06](#e06), [E07](#e07), [E19](#e19) |

Predictions: CASZ1 occupancy at rs7001688 should be detectable in liver cells despite low CASZ1 expression.; An alt-specific CASZ1 reporter or CRISPR edit should alter FAM110B expression if this chain is correct.

Falsified if: CASZ1 ChIP/CUT&RUN in liver cells shows no occupancy or no allele-specific binding at rs7001688.; Reporter or CRISPR base editing shows no T-allele effect in liver cells.; No eQTL or perturbation evidence connects the variant to FAM110B.

### 4. TCF20_ref_repressor_loss: TCF20 loses repressive binding on the alt allele and derepresses FAM110B (p = 0.02)

TF TCF20 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant is not in an annotated cCRE and no cCRE is within 500 bp, so a functional TCF20 element here would be cryptic and unproven.; gene FAM110B; cell type Hepatocyte/liver-cancer line context (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF20 is predicted to bind the ref G allele slightly more strongly in vitro: its own QBiC-SELEX model gives z=-20.49, effect=-0.151, with the ref site at the 76.7th and alt at the 78.8th percentile. The site is weak on both alleles, QBiC-SELEX detects a change but the effect size is small, and TCF20 occupancy is unknown because ENCODE never assayed TCF20. | weak | [E16](#e16), [E04](#e04), [E10](#e10) |
| element | No cCRE overlaps the variant and no cCRE is within 500 bp, so this would require an unannotated TCF20 element; the evidence does not show that such an element is functional in liver cells. | weak | [E01](#e01), [E03](#e03), [E10](#e10) |
| gene | If TCF20 represses FAM110B, loss of ref-allele TCF20 binding on the alt allele could increase FAM110B expression. However, FAM110B is 420.6 kb away, there is no liver eQTL for the variant, no variant-level GWAS/Open Targets record, and no Open Targets FAM110B association with free cholesterol in large LDL. | weak | [E02](#e02), [E08](#e08), [E17](#e17), [E19](#e19), [E09](#e09), [E06](#e06), [E07](#e07) |
| cell_type | TCF20 is expressed in Hep 3B2.1-7 (23.44 TPM), making a liver-cell repressor mechanism expression-compatible, but occupancy and repressor function at this variant are untested. | weak | [E16](#e16) |
| phenotype | Altered TCF20 repression of FAM110B could affect LDL cholesterol, but the direction and target gene are speculative and there is no variant-level LDL or statin-response evidence. | weak | [E09](#e09), [E06](#e06), [E07](#e07), [E19](#e19) |

Predictions: TCF20 ChIP or a reporter assay should show stronger G-allele binding and, if repressive, lower reporter activity.; The T allele should reduce TCF20 occupancy and increase FAM110B expression if this chain is correct.

Falsified if: TCF20 ChIP/CUT&RUN in liver cells shows no occupancy or no ref-allele preference at rs7001688.; A reporter or CRISPR edit shows no T-allele derepression of FAM110B.; No eQTL or perturbation evidence connects the variant to FAM110B.

## Prediction matrix

| Test | Cost | Separates top two | null_no_tf_effect | NME2_alt_cryptic_site | CASZ1_alt_cryptic_site | TCF20_ref_repressor_loss |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific NME2 ChIP-qPCR or CUT&RUN at rs7001688 in Hep 3B2.1-7 with heterozygous G/T | medium | yes | No allele-specific NME2 occupancy | T allele shows higher NME2 occupancy at rs7001688 | No NME2 occupancy or no allele-specific NME2 effect | No NME2 occupancy or no allele-specific NME2 effect |
| Liver eQTL lookup for rs7001688 and FAM110B in GTEx liver or a larger liver dataset | low | yes | No significant liver eQTL for rs7001688 and FAM110B | T allele associates with altered FAM110B expression | T allele associates with altered FAM110B expression if CASZ1 mediates the effect | T allele associates with increased FAM110B expression if TCF20 represses FAM110B |
| Allele-specific reporter or MPRA of rs7001688 G versus T in liver cells | medium | yes | No allelic reporter activity | Allele-specific reporter activity with the T allele; direction depends on whether NME2 activates or represses | Allele-specific reporter activity with the T allele if CASZ1 binds functionally | T allele increases reporter activity if TCF20 represses |
| CRISPR base editing of rs7001688 G>T in Hep3B, measuring FAM110B expression and an LDL/cholesterol readout | high | yes | No change in FAM110B expression or LDL-related readout | T edit changes FAM110B expression and/or an LDL-related readout | T edit changes FAM110B expression only if CASZ1 mediates the effect | T edit increases FAM110B expression if TCF20 repression is lost |
| CTCF ChIP in liver cells or HepG2 over rs7001688 | medium | no | No liver CTCF occupancy at the variant; if any occupancy, not allele-specific | No CTCF allele-specific effect expected | No CTCF allele-specific effect expected | No CTCF allele-specific effect expected |

## Next experiment

Allele-specific NME2 ChIP-qPCR in Hep 3B2.1-7 at rs7001688, with genotyping to distinguish G/T; this directly tests the NME2 binding step that separates the top two chains (null versus NME2 alt-binding).

## Investigate calls

- eqtl_lookup({"tissue": "Liver"})
- chip_peaks({"tf": "NME2", "biosample": "HepG2"})
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

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:41:57+00:00)

> No ENCODE NME2 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no NME2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T01:41:58+00:00)

> Open Targets: no association between FAM110B and free cholesterol in large LDL measurement (EFO_0022176).
