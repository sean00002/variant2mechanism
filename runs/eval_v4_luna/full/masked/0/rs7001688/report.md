# rs7001688 and LDL cholesterol

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 13 model calls; 280 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: CTCF (bound elsewhere, z -1.87, no clear allelic change, weak site). Occupancy unknown: CASZ1 (z 32.75); SETBP1 (z 29.74); SRCAP (z 29.74); NME2 (z 28.95); TCF20 (z -20.49). Diagnostic, not shown to the model: 441 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect (p = 0.95)

Null chain: no TF-mediated effect of this variant.

Predictions: In a relevant liver context, the variant will not produce a reproducible TF-dependent allelic regulatory effect. Any LDL association, if present, could arise from another variant or another mechanism.

Falsified if: A reproducible allelic regulatory effect at this site is demonstrated in a relevant liver context and shown to depend on a TF.

### 2. H2: CASZ1-mediated gain of binding (p = 0.03)

TF CASZ1 (QBiC-SELEX coverage own_model), alt allele binds more; element A regulatory element overlapping the variant has not been established by the supplied ENCODE cCRE data.; gene CYP7A1 (speculative); cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CASZ1's own QBiC-SELEX model predicts a strong T-favoring binding change. Occupancy is unknown: no variant-overlapping CASZ1 peak is reported in the HepG2 proxy or in the liver-biosample search, and the latter negative result may reflect limited assay coverage. | weak | [E10](#e10), [E12](#e12), [E17](#e17), [E22](#e22) |
| element | No ENCODE cCRE overlaps the variant, so the supplied data do not establish an overlapping regulatory element; this does not exclude an unannotated element. | supported | [E03](#e03) |
| gene | CYP7A1 is a speculative candidate based on cholesterol biology, not a demonstrated target: it is 926.8 kb away, several listed genes are closer, and no supplied evidence links the variant to CYP7A1 regulation. | missing | [E02](#e02), [E08](#e08), [E19](#e19) |
| cell_type | CASZ1 is expressed in Hep 3B2.1-7, but occupancy or regulatory activity at this site in that context has not been shown. | weak | [E12](#e12), [E17](#e17), [E22](#e22) |
| phenotype | CYP7A1 has general cholesterol and LDL relevance, but the evidence does not connect this variant or the proposed CASZ1 chain to LDL cholesterol. | missing | [E06](#e06), [E07](#e07), [E21c](#e21c), [E21e](#e21e) |

Predictions: In a relevant liver context, CASZ1 should occupy the site with greater binding to T than G, and a site-dependent allelic regulatory effect should change with CASZ1 perturbation. The direction of transcriptional activity and the target gene remain uncertain.

Falsified if: A sensitive assay in a relevant liver context finds no CASZ1 occupancy or no reproducible T-favoring binding.; CASZ1 perturbation leaves any reproducible allele-dependent regulatory effect unchanged.

### 3. H1: NME2-mediated gain of binding (p = 0.01)

TF NME2 (QBiC-SELEX coverage own_model), alt allele binds more; element A regulatory element overlapping the variant has not been established by the supplied ENCODE cCRE data.; gene CYP7A1 (speculative); cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NME2's own QBiC-SELEX model predicts stronger binding to T, and NME2 is highly expressed in the stated cell line; however, no NME2 occupancy at the variant is reported, including in the liver-biosample search, whose negative result may reflect limited assay coverage. | weak | [E15](#e15), [E20](#e20), [E23](#e23) |
| element | No ENCODE cCRE overlaps the variant, so the supplied data do not establish an overlapping regulatory element; this does not exclude an unannotated element. | supported | [E03](#e03) |
| gene | CYP7A1 is a speculative candidate based on cholesterol biology, not a demonstrated target: it is 926.8 kb away, several listed genes are closer, and no supplied evidence links the variant to CYP7A1 regulation. | missing | [E02](#e02), [E08](#e08), [E19](#e19) |
| cell_type | NME2 is highly expressed in Hep 3B2.1-7, but occupancy or regulatory activity at this site in that context has not been shown. | weak | [E15](#e15), [E23](#e23) |
| phenotype | CYP7A1 has general cholesterol and LDL relevance, but the evidence does not connect this variant or the proposed NME2 chain to LDL cholesterol. | missing | [E06](#e06), [E07](#e07), [E21c](#e21c), [E21e](#e21e) |

Predictions: In a relevant liver context, NME2 should bind the site more strongly with T than G, and an allele-dependent regulatory effect should change when NME2 is perturbed. The target gene and direction of transcriptional activity remain unspecified.

Falsified if: A sensitive assay in a relevant liver context finds no NME2 occupancy or no reproducible T-favoring binding.; NME2 perturbation leaves any reproducible allele-dependent regulatory effect unchanged.

### 4. H3: TCF20-mediated loss of binding (p = 0.01)

TF TCF20 (QBiC-SELEX coverage own_model), ref allele binds more; element A regulatory element overlapping the variant has not been established by the supplied ENCODE cCRE data.; gene CYP7A1 (speculative); cell type Hep 3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF20's own QBiC-SELEX model passes the stated detection gate and predicts stronger binding to G than T. Occupancy at the variant is unknown, so this in-vitro prediction alone is weak evidence for a mechanism. | weak | [E10](#e10), [E16](#e16) |
| element | No ENCODE cCRE overlaps the variant, so the supplied data do not establish an overlapping regulatory element; this does not exclude an unannotated element. | supported | [E03](#e03) |
| gene | CYP7A1 is a speculative candidate based on cholesterol biology, not a demonstrated target: it is 926.8 kb away, several listed genes are closer, and no supplied evidence links the variant to CYP7A1 regulation. | missing | [E02](#e02), [E08](#e08), [E19](#e19) |
| cell_type | TCF20 is expressed in Hep 3B2.1-7, but occupancy or regulatory activity at this site in that context has not been shown. | weak | [E16](#e16) |
| phenotype | CYP7A1 has general cholesterol and LDL relevance, but the evidence does not connect this variant or the proposed TCF20 chain to LDL cholesterol. | missing | [E06](#e06), [E07](#e07), [E21c](#e21c), [E21e](#e21e) |

Predictions: In a relevant liver context, TCF20 should occupy the site with greater binding to G than T, and a site-dependent allelic regulatory effect should change with TCF20 perturbation. The direction of transcriptional activity and the target gene remain uncertain.

Falsified if: A sensitive assay in a relevant liver context finds no TCF20 occupancy or no reproducible G-favoring binding.; TCF20 perturbation leaves any reproducible allele-dependent regulatory effect unchanged.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H2 | H1 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Measure allele-specific regulatory activity from G and T constructs in Hep 3B2.1-7, with TF-specific depletion and rescue for the candidate TFs. | medium | yes | No reproducible allele-dependent regulatory effect, or any effect is not dependent on the tested TFs. | A T-versus-G regulatory difference is present and changes with CASZ1 depletion or rescue. | A T-versus-G regulatory difference is present and changes with NME2 depletion or rescue. | A T-versus-G regulatory difference is present and changes with TCF20 depletion or rescue. |
| Use a sensitive allele-specific occupancy assay at the endogenous site in a relevant liver model, testing NME2, CASZ1, and TCF20. | medium | yes | No candidate TF shows relevant occupancy with a reproducible allelic difference. | CASZ1 occupies the site, with greater occupancy on T than G. | NME2 occupies the site, with greater occupancy on T than G. | TCF20 occupies the site, with greater occupancy on G than T. |
| Map the variant's target gene using endogenous perturbation of the site and measure nearby gene expression. | high | yes | No reproducible site-dependent expression change attributable to the variant. | A site-dependent expression effect is found and is CASZ1-dependent; CYP7A1 is only a candidate, not a required outcome. | A site-dependent expression effect is found and is NME2-dependent; CYP7A1 is only a candidate, not a required outcome. | A site-dependent expression effect is found and is TCF20-dependent; CYP7A1 is only a candidate, not a required outcome. |

## Next experiment

Run the medium-cost allele-specific regulatory assay in Hep 3B2.1-7 with CASZ1 depletion and rescue, comparing the G and T alleles. It most directly distinguishes the top two hypotheses, H0 and H2, by testing for a reproducible CASZ1-dependent allelic effect; a positive result would still require endogenous validation.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- chip_peaks({"tf": "CASZ1", "biosample": "HepG2"}) for H2.binding, ran as [E17](#e17). Expected: If a CASZ1 ChIP-seq peak overlaps the variant in HepG2, H2.binding gains occupancy support alongside the alt-favoring QBiC-SELEX result and H2 rises; if no peak is found, H2 remains weak or falls.
- gene_disease({"gene": "CYP7A1"}) for H2.phenotype, ran as [E18](#e18). Expected: If Open Targets reports LDL-cholesterol association evidence for CYP7A1, the proposed target's relevance to the phenotype gains support, though this would not establish regulation by the variant; if not, H2.phenotype remains speculative.
- literature_search({"query": "chr8:57573391 CYP7A1 LDL cholesterol"}) for H2.gene, ran as [E19](#e19). Expected: If the literature identifies direct evidence linking this locus or variant to CYP7A1 regulation, H2.gene gains support and H2 rises; if no such evidence appears, the gene link remains based only on distant proximity.

- Result of chip_peaks({"tf":"CASZ1","biosample":"HepG2"}): E17 reports no CASZ1 ChIP-seq peak containing the variant in HepG2 and no peak within 100 bp; this may also reflect lack of a CASZ1 experiment in that biosample. (as expected: yes)
- Result of gene_disease({"gene":"CYP7A1"}): E18 reports no Open Targets association between CYP7A1 and free cholesterol in large LDL measurement. (as expected: yes)
- Result of literature_search({"query":"chr8:57573391 CYP7A1 LDL cholesterol"}): E19 reports zero literature hits for a direct locus/variant-to-CYP7A1 LDL connection. (as expected: yes)

Chains after revision: null 0.87; CASZ1 0.06; NME2 0.04; TCF20 0.03. Link grades changed: H1.cell_type: supported → weak, H1.gene: supported → weak, H1.phenotype: supported → missing, H2.cell_type: supported → weak, H2.gene: supported → weak, H2.phenotype: supported → missing, H3.cell_type: supported → weak, H3.gene: supported → weak, H3.phenotype: supported → missing.

### Round 2

- chip_peaks({"tf": "NME2", "biosample": "HepG2"}) for H1.binding, ran as [E20](#e20). Expected: If an NME2 peak overlaps the variant in HepG2, H1 gains relevant-context occupancy support, though allele-specific binding remains unproven; if no peak is found, H1.binding weakens further.
- literature_search({"query": "CYP7A1 LDL cholesterol"}) for H2.phenotype, ran as [E21](#e21). Expected: If the literature supports a CYP7A1 connection to LDL cholesterol, it could improve the gene-to-trait plausibility of H2, but would not establish this variant's effect; if it yields no relevant evidence, the phenotype link remains unsupported.

- Result of chip_peaks({"tf":"NME2","biosample":"HepG2"}) for H1.binding: E20 reports no NME2 ChIP-seq peak overlapping the variant in the matching HepG2 biosample; assay availability may limit the meaning of this absence. (as expected: yes)
- Result of literature_search({"query":"CYP7A1 LDL cholesterol"}) for H2.phenotype: E21 includes literature linking CYP7A1 activity to cholesterol handling and reporting lower LDL-C when CYP7A1 expression is restored in a mouse model. This supports pathway plausibility but does not connect the variant to CYP7A1 or LDL. (as expected: yes)

Chains after revision: null 0.94; CASZ1 0.03; TCF20 0.02; NME2 0.01. Link grades changed: H1.cell_type: weak → supported, H1.phenotype: missing → weak, H2.cell_type: weak → supported, H2.phenotype: missing → weak, H3.cell_type: weak → supported, H3.phenotype: missing → weak.

### Round 3

- chip_peaks({"tf": "CASZ1", "biosample": "liver"}) for H2.binding, ran as [E22](#e22). Expected: If ENCODE reports a CASZ1 peak containing the variant in a liver biosample, H2.binding gains occupancy support and H2 rises relative to the other candidates; if no peak is found, H2 remains weak, though absence may reflect limited assay coverage.
- chip_peaks({"tf": "NME2", "biosample": "liver"}) for H1.binding, ran as [E23](#e23). Expected: If a liver-biosample NME2 peak contains the variant, H1.binding gains occupancy support for the T-favoring QBiC-SELEX prediction and H1 rises; if none is found, H1 remains weak, subject to assay coverage.

- Result of chip_peaks({"tf":"CASZ1","biosample":"liver"}): E22 reports no CASZ1 ChIP-seq peak containing the variant in liver-matching biosamples; it also notes that CASZ1 may not have been assayed. (as expected: yes)
- Result of chip_peaks({"tf":"NME2","biosample":"liver"}): E23 reports no NME2 ChIP-seq peak containing the variant in liver-matching biosamples; it also notes that NME2 may not have been assayed. (as expected: yes)

Chains after revision: null 0.95; CASZ1 0.03; NME2 0.01; TCF20 0.01. Link grades changed: H1.cell_type: supported → weak, H1.gene: weak → missing, H1.phenotype: weak → missing, H2.cell_type: supported → weak, H2.gene: weak → missing, H2.phenotype: weak → missing, H3.cell_type: supported → weak, H3.gene: weak → missing, H3.phenotype: weak → missing.

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

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:39:54+00:00)

> No ENCODE CASZ1 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no CASZ1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:31+00:00)

> Open Targets: no association between CYP7A1 and free cholesterol in large LDL measurement (EFO_0022176).

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr8%3A57573391%20CYP7A1%20LDL%20cholesterol&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:33:27+00:00)

> Europe PMC: 0 hits for 'chr8:57573391 CYP7A1 LDL cholesterol'; top 0 with PMIDs:

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:41:57+00:00)

> No ENCODE NME2 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no NME2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e21"></a>**E21** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=CYP7A1%20LDL%20cholesterol&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:24:27+00:00)

> Europe PMC: 3955 hits for 'CYP7A1 LDL cholesterol'; top 6 with PMIDs:
> PMID 42754810 (2026): CRISPR/dCas9-induced upregulation of endogenous apolipoprotein A1 and paraoxonase 1 genes reduces the aortic lipid deposits in apoE&lt;sup&gt;-/-&lt;/sup&gt; mice.
> PMID 42650834 (2026): Freeze-Dried &lt;i&gt;Poecilobdella manillensis&lt;/i&gt; Powder Regulates Cholesterol Homeostasis to Alleviate Hyperlipidemia.
> PMID 42796552 (2026): Modulation of Hepatic Cholesterol-Related Pathways by &lt;i&gt;Ophiocordyceps sinensis&lt;/i&gt; and Coenzyme Q10 in a Sequential Gut-Liver In Vitro Model.
> PMID 42397177 (2026): HDAC9 promotes atherosclerosis by suppressing CYP7A1 and impairing hepatic cholesterol excretion.
> PMID 42721809 (2026): Thermosonication-induced structural remodeling of faba bean protein: Improved functionality, digestibility, and cholesterol metabolism regulation for cardiovascular health.
> PMID 42819684 (2026): &lt;i&gt;Lactobacillus plantarum&lt;/i&gt; and &lt;i&gt;Bacillus licheniformis&lt;/i&gt; Ameliorate High-Carbohydrate-High-Fat-Induced Glycolipid Disorders in Common Carp in Association With the Gut Microbiota and Bile Acid Axis.

<a id="e21a"></a>**E21a** literature_search, Europe PMC abstract, PMID 42754810 (https://europepmc.org/article/MED/42754810; retrieved 2026-10-26T20:24:27+00:00)

> These mice also exhibited high levels of hepatic, gallbladder and feces cholesterol, in part due to the upregulation of hepatic scavenger receptor class-B1, cholesterol 7-alpha-hydroxylase, and ATP-binding cassette sub-family-G-member-8 transporter.

<a id="e21b"></a>**E21b** literature_search, Europe PMC abstract, PMID 42650834 (https://europepmc.org/article/MED/42650834; retrieved 2026-10-26T20:24:27+00:00)

> FDPMP administration significantly improved serum lipid profiles by reducing triglycerides, total cholesterol, and low-density lipoprotein cholesterol, while increasing high-density lipoprotein cholesterol levels.

<a id="e21c"></a>**E21c** literature_search, Europe PMC abstract, PMID 42650834 (https://europepmc.org/article/MED/42650834; retrieved 2026-10-26T20:24:27+00:00)

> Mechanistically, FDPMP restored cholesterol homeostasis through dual regulation of cholesterol metabolism, characterized by upregulation of cholesterol 7α-hydroxylase (CYP7A1) to promote bile acid-mediated cholesterol excretion, alongside downregulation of 3-hydroxy-3-methylglutaryl-CoA reductase (HMGCR) and synthase (HMGCS1) to inhibit cholesterol biosynthesis.

<a id="e21d"></a>**E21d** literature_search, Europe PMC abstract, PMID 42796552 (https://europepmc.org/article/MED/42796552; retrieved 2026-10-26T20:24:27+00:00)

> These functional outcomes were accompanied by coordinated changes in protein abundance: a decrease in sterol regulatory element-binding protein 2 (SREBP-2), 3-hydroxy-3-methylglutaryl-CoA reductase (HMGR), and proprotein convertase subtilisin/kexin type 9 (PCSK9) levels, alongside increased low-density lipoprotein receptor (LDLR), cytochrome P450 family 7 subfamily A member 1 (CYP7A1), and ATP-binding cassette transporter A1 (ABCA1) expression.

<a id="e21e"></a>**E21e** literature_search, Europe PMC abstract, PMID 42397177 (https://europepmc.org/article/MED/42397177; retrieved 2026-10-26T20:24:27+00:00)

> Pharmacological inhibition of HDAC9 (TMP195) or liver-targeted AAV8-shHdac9 knockdown restored CYP7A1 expression, reduced plasma LDL-C, and attenuated aortic plaque burden in HFD-fed ApoE-/- mice.

<a id="e21f"></a>**E21f** literature_search, Europe PMC abstract, PMID 42397177 (https://europepmc.org/article/MED/42397177; retrieved 2026-10-26T20:24:27+00:00)

> Mechanistically, HDAC9 transcriptionally represses Cyp7a1, as the cholesterol-lowering effect of Hdac9 knockdown was abolished by concomitant Cyp7a1 silencing.

<a id="e21g"></a>**E21g** literature_search, Europe PMC abstract, PMID 42721809 (https://europepmc.org/article/MED/42721809; retrieved 2026-10-26T20:24:27+00:00)

> The expression analyses further confirmed that UH-FPI upregulated the expression of cholesterol efflux-related proteins (ABCG5 and ABCG8), hepatic cholesterol metabolism regulators (LXR-α, CYP7A1, and LDL-R), and downregulated the expression of the intestinal cholesterol uptake-related protein NPC1L1 upon normalization with the HF group.

<a id="e22"></a>**E22** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:39:54+00:00)

> No ENCODE CASZ1 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'liver'. Absence can also mean no CASZ1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e23"></a>**E23** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T02:41:57+00:00)

> No ENCODE NME2 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'liver'. Absence can also mean no NME2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.
