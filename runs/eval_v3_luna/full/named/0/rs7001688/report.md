# rs7001688 and LDL cholesterol

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 8 model calls; 248 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: CTCF (bound elsewhere, z -1.87, no clear allelic change, weak site). Occupancy unknown: CASZ1 (z 32.75); SETBP1 (z 29.74); SRCAP (z 29.74); NME2 (z 28.95); TCF20 (z -20.49). Diagnostic, not shown to the model: 441 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect of rs7001688 (p = 0.93)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will show no reproducible allele-dependent TF occupancy linked to a regulatory effect in relevant hepatic cells.; Any LDL association, if present, will be absent from these data or attributable to another linked variant or mechanism.

Falsified if: A relevant TF is shown to bind the variant with reproducible allele-dependent occupancy in hepatic cells, and variant editing produces a linked regulatory change.

### 2. H1: NME2 may gain binding at rs7001688 and affect CYP7A1 regulation (p = 0.03)

TF NME2 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant could lie in an unannotated regulatory sequence, but no cCRE overlaps it and NME2 occupancy at the site has not been measured.; gene CYP7A1; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NME2 is a candidate because it is highly expressed in Hep 3B2.1-7 and its own QBiC-SELEX model predicts stronger binding to alt T; however, occupancy is unknown, so this in-vitro result does not establish binding in cells. | weak | [E15](#e15) |
| element | A regulatory role for the sequence is unestablished: there is no overlapping cCRE or matching-biosample TF peak, and the reported CTCF peak is from LNCAP rather than HepG2. | supported | [E03](#e03), [E04](#e04), [E05](#e05) |
| gene | CYP7A1 is a speculative target based on proximity; the supplied evidence does not connect this variant to CYP7A1 regulation. | weak | [E02](#e02) |
| cell_type | NME2 is highly expressed in the stated cell line, but expression alone does not establish occupancy or a regulatory effect there. | supported | [E15](#e15) |
| phenotype | A CYP7A1-mediated LDL effect is possible but unsupported for this variant; no variant-level GWAS association or significant GTEx eQTL is reported, and Open Targets reports no CYP7A1 association for the specified free-cholesterol measurement. | missing | [E06](#e06), [E08](#e08), [E18](#e18) |

Predictions: In relevant hepatic cells, NME2 occupancy at the site should be greater on T than G.; If CYP7A1 is the target, editing the variant should alter CYP7A1 expression; the direction of that expression change is not determined by the binding prediction.

Falsified if: A suitably sensitive assay finds no NME2 occupancy at the site in relevant hepatic cells.; Editing the variant produces no reproducible change in CYP7A1 expression or a linked regulatory readout.

### 3. H2: CASZ1 may gain binding at rs7001688 and affect FAM110B regulation (p = 0.03)

TF CASZ1 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant could fall in an unannotated regulatory sequence, but neither regulatory activity nor CASZ1 occupancy in hepatic cells is established.; gene FAM110B; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CASZ1's own QBiC-SELEX model predicts a strong alt-favoring binding change, but occupancy is unknown; CASZ1 was not assayed in matching HepG2 and its expression in the stated line is relatively low. | weak | [E12](#e12), [E17](#e17) |
| element | The evidence does not establish a regulatory element at the variant: no cCRE overlaps it and no matching-biosample TF peak is reported. | supported | [E03](#e03), [E04](#e04) |
| gene | FAM110B is a speculative candidate because it is the closest listed gene; the pravastatin literature search hit does not establish FAM110B as a target of this variant. | weak | [E02](#e02), [E09](#e09), [E19](#e19) |
| cell_type | CASZ1 is expressed at a relatively low level in Hep 3B2.1-7, and the supplied evidence does not show occupancy in this line or matching HepG2. | supported | [E12](#e12), [E17](#e17) |
| phenotype | A FAM110B-mediated effect on LDL cholesterol is unsupported here; no variant-level GWAS association or significant GTEx eQTL is reported. | missing | [E06](#e06), [E08](#e08) |

Predictions: If this chain is correct, CASZ1 should occupy the site in relevant hepatic cells, with greater occupancy on T than G.; If FAM110B is the target, editing the variant should alter FAM110B expression; the direction is not inferable from the binding prediction.

Falsified if: CASZ1 shows no occupancy at the site in a suitably sensitive assay in relevant hepatic cells.; Editing the variant produces no reproducible change in FAM110B expression or a linked regulatory readout.

### 4. H3: CTCF occupancy may be slightly favored by the reference allele (p = 0.01)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element A CTCF peak overlaps the variant in LNCAP, but this does not establish a functional regulatory element or occupancy in the relevant hepatic context.; gene FAM110B; cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF is expressed and has a reported peak over the variant in LNCAP, but its QBiC-SELEX model predicts only a small ref-favoring change below the detection gate at a weak site; this argues against a substantial allelic effect through CTCF binding. | weak | [E05](#e05), [E11](#e11) |
| element | The variant overlaps a CTCF ChIP-seq peak in LNCAP, but there is no matching HepG2 peak or overlapping cCRE, so regulatory function in hepatic cells is unestablished. | supported | [E03](#e03), [E04](#e04), [E05](#e05) |
| gene | FAM110B is only a tentative target based on distance; neither the literature search hit nor the supplied evidence links it to this variant or to CTCF regulation. | weak | [E02](#e02), [E09](#e09), [E19](#e19) |
| cell_type | CTCF is expressed in Hep 3B2.1-7, but the reported variant-overlapping occupancy is from LNCAP, not matching HepG2. | supported | [E04](#e04), [E05](#e05) |
| phenotype | A CTCF-mediated effect on LDL cholesterol is unsupported; no variant-level GWAS association or significant GTEx eQTL is reported. | missing | [E06](#e06), [E08](#e08) |

Predictions: If this chain is correct, CTCF occupancy in relevant hepatic cells should be detectable and should be modestly greater on G than T.; If FAM110B is the target, perturbing the site should affect FAM110B expression, although the supplied evidence does not establish that target.

Falsified if: Relevant hepatic assays find no CTCF occupancy or no reproducible allele-dependent occupancy.; Editing the variant produces no reproducible regulatory change in the proposed target.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Measure allele-specific NME2 occupancy at rs7001688 by targeted CUT&RUN with amplicon sequencing in heterozygous Hep 3B2.1-7 cells. | medium | yes | No reproducible allele-dependent NME2 occupancy linked to the variant. | NME2 occupies the site and occupancy is greater on T than G. | No NME2-specific T-favoring occupancy; this chain instead predicts CASZ1 occupancy. | No NME2-specific T-favoring occupancy; this chain instead predicts CTCF occupancy, potentially modestly greater on G. |
| Test CASZ1 occupancy at rs7001688 by targeted CUT&RUN or ChIP-qPCR in HepG2 or Hep 3B2.1-7 cells. | medium | no | No reproducible CASZ1 occupancy linked to the variant. | No CASZ1-specific occupancy predicted. | CASZ1 occupancy is detected; allele-specific follow-up should show greater occupancy on T. | No CASZ1-specific occupancy predicted. |
| Edit rs7001688 between G and T in Hep 3B2.1-7 cells and measure CYP7A1 and FAM110B expression. | high | yes | No reproducible variant-dependent change in either gene is expected. | CYP7A1 expression changes reproducibly; the direction is not specified by the binding prediction. | FAM110B expression changes reproducibly; the direction is not specified by the binding prediction. | A FAM110B change is possible under the proposed target assignment, but the evidence gives little basis to expect one. |

## Next experiment

The highest-probability chain is H0 and the next is H1. The cheapest listed discriminating experiment is targeted allele-specific NME2 CUT&RUN with amplicon sequencing at rs7001688 in heterozygous Hep 3B2.1-7 cells. Greater NME2 occupancy on T would support H1 over H0, although occupancy alone would not establish a regulatory or LDL effect.

## Investigate calls

- chip_peaks({"tf": "CASZ1", "biosample": "HepG2"})
- gene_disease({"gene": "CYP7A1"})
- literature_search({"query": "FAM110B pravastatin LDL cholesterol"})

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

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:39:54+00:00)

> No ENCODE CASZ1 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no CASZ1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:31+00:00)

> Open Targets: no association between CYP7A1 and free cholesterol in large LDL measurement (EFO_0022176).

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=FAM110B%20pravastatin%20LDL%20cholesterol&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:39:55+00:00)

> Europe PMC: 1 hits for 'FAM110B pravastatin LDL cholesterol'; top 1 with PMIDs:
> PMID 22666496 (2012): Genome-wide study of gene variants associated with differential cardiovascular event reduction by pravastatin therapy.
