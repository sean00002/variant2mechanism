# rs7001688 and LDL cholesterol

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.38 over 7 model calls; 97 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen

441 of 997 models pass the gate. Top groups: Rel, 1 model (best RELA, z 33.95); C2H2 ZF, 1 model (best CASZ1, z 32.75); AT hook, 2 models (best HMGA1, z 29.74); C2H2 ZF, 1 model (best ZNF580, z -29.06); Unknown, 1 model (best NME2, z 28.95).

## Ranked chains

### 1. H0: No TF-mediated effect: isolated non-coding variant with no cCRE, no GWAS/eQTL signal (p = 0.72)

Null chain: no TF-mediated effect of this variant.

Predictions: MPRA/luciferase of the 200 bp window shows no allelic activity difference in Hep3B or HepG2, with or without TNF stimulation; No allele-specific ATAC or TF ChIP signal at this position in liver cells (consistent with E19, no RELA peak in HepG2); No liver eQTL for FAM110B, BPNT2, UBXN2B, CYP7A1 or SDCBP tied to rs7001688 (consistent with E18); No LDL association statistic appears for rs7001688 or tight proxies (consistent with E04, E05)

Falsified if: A reproducible allelic reporter effect at this exact site in hepatocytes; Allele-specific TF occupancy or accessibility at the site in liver cells; A credible LDL association for rs7001688 or a tight proxy

### 2. H1: Alt allele creates a stronger RELA (NF-kB) site in an unannotated, stimulation-dependent liver element (p = 0.08)

TF RELA (stated coverage own_model; registry own_model), alt allele binds more; element Unannotated site at chr8:57573391; no cCRE overlap, nearest cCRE EH38E3835076 1544 bp away; gene CYP7A1 (unverified; nearest LDL-plausible gene at 927 kb); cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts markedly stronger alt-allele binding for RELA (own model, z 33.95, effect +1.34; site 97.4th to 99.8th percentile). Within the Rel group RELA was chosen because it is the only member with its own model and the best expressed in this line (73.4 TPM) versus mapped RELB (17.4) and REL (4.3). This is an in vitro prediction only; no ChIP or allelic binding data support it, and E19 finds no RELA peak at this position in HepG2 | weak | [E08](#e08), [E07](#e07), [E19](#e19) |
| element | No regulatory element is demonstrated: no cCRE overlaps the variant and VEP reports no regulatory feature, so any element would have to be one missed by the registries. This link is unsupported | missing | [E01](#e01), [E03](#e03) |
| gene | No target gene is demonstrated: CYP7A1 is assigned only by being the nearest LDL-relevant gene (927 kb), with no eQTL (E18) and no contact data | missing | [E02](#e02), [E18](#e18) |
| cell_type | RELA is expressed in this hepatoma line (73.4 TPM), which is permissive only; NF-kB activity would additionally require stimulation | weak | [E08](#e08) |
| phenotype | No cited evidence links this locus or CYP7A1 to LDL here; Open Targets shows no CYP7A1 association for the queried lipid trait and the variant has no GWAS or Open Targets record, so the direction to higher LDL is asserted, not shown | missing | [E20](#e20), [E04](#e04), [E05](#e05) |

Predictions: Allelic reporter difference in Hep3B emerges only after TNF/IL-1 stimulation; RELA ChIP-qPCR in stimulated hepatocytes shows a peak with allele-preferential occupancy for T; Effect is abolished by IKK inhibition or RELA knockdown

Falsified if: No RELA occupancy at the locus in stimulated hepatocytes; Reporter shows equal G and T activity under NF-kB activation; No physical contact between the variant region and any candidate gene

### 3. H2: Alt allele increases HMGA1 architectural binding at an AT-rich site, with a local chromatin effect (p = 0.07)

TF HMGA1 (stated coverage own_model; registry own_model), alt allele binds more; element Unannotated AT-rich site at chr8:57573391 (no cCRE overlap); gene FAM110B (unverified; nearest protein-coding TSS, 420.6 kb away); cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger alt binding for HMGA1 (own model, z 29.74, effect +2.006; 67.3th to 96.4th percentile). HMGA1 was chosen within the AT-hook group as the only highly expressed member with its own model (239 TPM); the group disagrees in direction (SETBP1 z -15.21), and HMGA1 binds AT-rich DNA with low sequence specificity, so this prediction is weak | weak | [E10](#e10) |
| element | No element is demonstrated: no cCRE overlaps the variant and no regulatory feature is annotated | missing | [E03](#e03), [E01](#e01) |
| gene | The variant is not inside FAM110B; it is 420.6 kb from its TSS and VEP reports no transcript consequences. FAM110B is assigned by proximity alone, with no liver eQTL | missing | [E02](#e02), [E01](#e01), [E18](#e18) |
| cell_type | HMGA1 is very highly expressed in this hepatoma line (239 TPM), which is permissive only | weak | [E10](#e10) |
| phenotype | No evidence ties FAM110B to LDL cholesterol; E06 is a keyword hit on a pravastatin-response study and does not establish the gene or a direction | missing | [E06](#e06), [E04](#e04) |

Predictions: Allele-specific HMGA1 ChIP signal and a local nucleosome/accessibility change at the site; Any allelic reporter effect is independent of inflammatory stimulation and of YAP/TAZ status; Effect size is small and sequence-context (AT-richness) dependent

Falsified if: No HMGA1 occupancy or chromatin difference at the site; HMGA1 knockdown does not change any allelic difference

### 4. H4: Alt allele weakens a high-affinity ZNF580 site (p = 0.07)

TF ZNF580 (stated coverage own_model; registry own_model), ref allele binds more; element High-affinity ZNF580 k-mer at chr8:57573391 (ref 100.0th percentile), not in any cCRE; gene unverified (no eQTL; FAM110B nearest at 420.6 kb); cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts loss of binding with the alt allele for ZNF580 (own model, z -29.06, effect -1.205), starting from a ref site at the 100.0th percentile of the model's k-mers; ZNF580 is the sole member of its group, so no within-group TF choice is needed. Prediction only, no ChIP support | weak | [E11](#e11) |
| element | No element is demonstrated: no cCRE overlaps the site and occupancy of the predicted site is not shown | missing | [E03](#e03), [E01](#e01) |
| gene | No target gene is supported: no significant liver eQTL for this variant, and the nearest gene is 420.6 kb away | missing | [E18](#e18), [E02](#e02) |
| cell_type | ZNF580 is expressed at a low but detectable level (8.5 TPM) in this line; permissive only | weak | [E11](#e11) |
| phenotype | No evidence links this variant or any nearby gene to LDL cholesterol (no GWAS or Open Targets record), so no direction can be stated | missing | [E04](#e04), [E05](#e05) |

Predictions: Reporter activity is higher for the alt allele if ZNF580 acts as a repressor at this site, and lower if it activates; ZNF580 knockdown abolishes any allelic reporter difference; Loss-of-binding signature: ref allele shows greater protein occupancy in EMSA with nuclear extract

Falsified if: No ZNF580 binding detectable at the site by EMSA or ChIP; Allelic reporter difference unchanged by ZNF580 depletion

### 5. H5: Alt allele creates a strong site for the top-ranked, very highly expressed NME2 model (p = 0.06)

TF NME2 (stated coverage own_model; registry own_model), alt allele binds more; element Unannotated site at chr8:57573391 (no cCRE overlap); gene unverified (no significant liver eQTL for any gene in the window); cell type Hepatocyte (Hep 3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts stronger alt binding for NME2 (own model, z 28.95, effect +0.573; site 65.7th to 99.1th percentile), the sole member of its group, so no within-group TF choice is required; NME2 is by far the most abundant candidate in this line (928 TPM). Effect size is modest and this is an in vitro prediction only | weak | [E12](#e12), [E07](#e07) |
| element | No element is demonstrated: no cCRE overlaps the variant and no regulatory feature is annotated | missing | [E03](#e03), [E01](#e01) |
| gene | No target gene is supported: no significant liver eQTL for this variant; all candidate genes are 420 kb or more away | missing | [E18](#e18), [E02](#e02) |
| cell_type | NME2 is expressed at 928 TPM in Hep 3B2.1-7, the highest of any candidate; permissive only | weak | [E12](#e12) |
| phenotype | No evidence connects this variant or NME2 activity here to LDL cholesterol | missing | [E04](#e04), [E05](#e05) |

Predictions: EMSA with Hep3B nuclear extract shows an alt-preferential complex that supershifts with anti-NME2; NME2 knockdown removes any allelic reporter difference, whereas RELA, HMGA1 or ZNF580 knockdown does not; Effect is independent of TNF stimulation and of YAP/TAZ status

Falsified if: No NME2 occupancy at the site; Allelic difference persists after NME2 depletion

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H4 | H5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GTEx/other liver eQTL lookup for rs7001688 (existing data, E18) | existing data | yes | No significant liver eQTL for any gene (observed in E18): consistent | Requires a CYP7A1 eQTL (possibly condition-specific); currently absent, disfavoured | Requires a FAM110B eQTL; currently absent, disfavoured | Requires some local eQTL; currently absent, disfavoured | Requires some local eQTL; currently absent, disfavoured |
| Allelic luciferase/MPRA of the 200 bp window in Hep3B, unstimulated and +TNF | medium | yes | No allelic difference in either condition | Allelic difference appears only (or mainly) after TNF stimulation | Small allelic difference, stimulation-independent | Allelic difference, stimulation-independent; alt higher if ZNF580 represses | Allelic difference, stimulation-independent, alt higher |
| EMSA with Hep3B nuclear extract, ref vs alt probe, with supershift antibodies (RELA, HMGA1, ZNF580, NME2) | medium | yes | No differential complex between alleles | Alt-preferential complex supershifted by anti-RELA (stimulated extract) | Alt-preferential complex supershifted by anti-HMGA1 | Ref-preferential complex supershifted by anti-ZNF580 | Alt-preferential complex supershifted by anti-NME2 |
| ChIP-seq/ChIP-qPCR peak check at chr8:57573391 in liver lines (RELA done, E19) | existing data | yes | No peak for any TF: consistent (E19 shows none for RELA) | Predicts a RELA peak; E19 finds none in HepG2, disfavouring H1 (though no stimulated experiment may exist) | Predicts broad HMGA1 occupancy, not tested by E19 | Predicts ZNF580 occupancy, not tested by E19 | Predicts NME2 occupancy, not tested by E19 |
| Open chromatin/ATAC and 4C or promoter-capture Hi-C from the variant region in hepatocytes | high | no | Region is closed and makes no specific contact with a lipid gene promoter | Contact with the CYP7A1 promoter at 927 kb | Local chromatin/nucleosome change; contact with the FAM110B domain | Contact with a nearby promoter; accessibility change on alt allele | Accessibility change without a specific long-range contact requirement |
| TF knockdown panel (RELA, HMGA1, ZNF580, NME2) with allelic reporter readout | high | no | No allelic difference to lose under any knockdown | RELA knockdown abolishes the allelic difference | HMGA1 knockdown abolishes it | ZNF580 knockdown abolishes it | NME2 knockdown abolishes it |

## Next experiment

Cheapest separating test beyond existing data: a dual-luciferase allelic reporter of the 200 bp window around chr8:57573391 (ref G vs alt T) in Hep 3B2.1-7, assayed unstimulated and after TNF. No allelic difference in either condition supports H0 (currently the leading chain); a TNF-dependent difference supports H1, and a stimulation-independent difference points to H2, H4 or H5, to be resolved by the subsequent EMSA/supershift and knockdown panel.

## Investigate calls

- eqtl_lookup({"tissue": null})
- chip_peaks({"tf": "RELA", "biosample": "HepG2"})
- gene_disease({"gene": "CYP7A1"})

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs7001688&size=100; retrieved 2026-10-25T17:33:20+00:00)

> 0 GWAS Catalog associations for rs7001688, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:33:20+00:00)

> Open Targets has no record of 8_57573391_G_T.

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=FAM110B%20AND%20%22ldl%20cholesterol%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:33:21+00:00)

> Europe PMC: 1 hits for 'FAM110B AND "ldl cholesterol"'; top 1 with PMIDs:
> PMID 22666496 (2012): Genome-wide study of gene variants associated with differential cardiovascular event reduction by pravastatin therapy.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:57573391:G>T: 997 models scored, 441 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 316 CIS-BP groups. Expression context: DepMap line ACH-000625. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 73 (BED ZF, 1 model z 24.73, C2H2 ZF, 1 model z -21.17, DM, 5 models z -18.3, C2H2 ZF, 1 model z 16.96, C2H2 ZF, 1 model z -16.13). Passing groups ranked below the ones shown: 233. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G315 (Rel, 1 model): best model RELA_DBD_TGATCC20NCTA_KI_nitta2015_1_3_7mer (own model of RELA), z 33.95, effect 1.34 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: RELA z 33.95. TFs this group covers: RELA (own model) 73.44 TPM, RELB (mapped) 17.37 TPM, REL (mapped) 4.27 TPM; best model's site strength: ref 97.4th, alt 99.8th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G138 (C2H2 ZF, 1 model): best model CASZ1_FL_AG40NGGAATC_YWKC_jolma2025_0_4_7mer (own model of CASZ1), z 32.75, effect 2.741 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CASZ1 z 32.75. TFs this group covers: CASZ1 (own model) 4.18 TPM; best model's site strength: ref 99.1th, alt 99.8th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G077 (AT hook, 2 models): best model HMGA1_FL_GA40NCTGATT_YWPA_jolma2025_0_3_7mer (own model of HMGA1), z 29.74, effect 2.006 (alt binds more); 2 passing models (1 with the best model's sign); members disagree on direction. Passing members: HMGA1 z 29.74, SETBP1 z -15.21. TFs this group covers: HMGA1 (own model) 238.96 TPM, HMGA2 (mapped) 97.36 TPM, SRCAP (mapped) 41.42 TPM, ASH1L (mapped) 21.18 TPM, SETBP1 (own model) 1.24 TPM; best model's site strength: ref 67.3th, alt 96.4th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G540 (C2H2 ZF, 1 model): best model ZNF580_FL_TGGCCA40NTTC_KAE_yin2017_0_4_7mer (own model of ZNF580), z -29.06, effect -1.205 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF580 z -29.06. TFs this group covers: ZNF580 (own model) 8.54 TPM; best model's site strength: ref 100.0th, alt 94.4th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G266 (Unknown, 1 model): best model NME2_FL_TA40NTCACTC_YWDA_jolma2025_0_4_7mer (own model of NME2), z 28.95, effect 0.573 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: NME2 z 28.95. TFs this group covers: NME2 (own model) 928.15 TPM; best model's site strength: ref 65.7th, alt 99.1th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G460 (C2H2 ZF, 1 model): best model ZNF230_FL_TG40NGACCTT_YWDA_jolma2025_0_3_7mer (own model of ZNF230), z 26.94, effect 0.512 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF230 z 26.94. TFs this group covers: ZNF230 (own model) 1.96 TPM; best model's site strength: ref 70.8th, alt 96.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G018 (E2F, 4 models): best model E2F4_eDBD_TCAGGG40NGCA_KO_yin2017_1_3_7mer (own model of E2F4), z 25.88, effect 1.189 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: E2F4 z 25.88, E2F3 z 17.58. TFs this group covers: E2F4 (own model) 58.99 TPM, E2F3 (own model) 36.15 TPM, E2F5 (mapped) 18.97 TPM, E2F6 (mapped) 18.07 TPM, E2F1 (own model) 11.74 TPM, E2F2 (own model) 2.06 TPM; best model's site strength: ref 98.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G499 (C2H2 ZF, 1 model): best model ZNF384_FL_GG40NTAGTTT_AATBA_jolma2025_0_3_7mer (own model of ZNF384), z -24.76, effect -0.523 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF384 z -24.76. TFs this group covers: ZNF384 (own model) 82.82 TPM; best model's site strength: ref 82.1th, alt 68.4th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G031 (TEA, 4 models): best model TEAD1_FL_TCACGC40NACT_KW_yin2017_0_4_7mer (own model of TEAD1), z 23.14, effect 1.505 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: TEAD1 z 23.14, TEAD4 z 10.66, TEAD2 z 9.59, TEAD3 z 8.07. TFs this group covers: TEAD2 (own model) 34.44 TPM, TEAD1 (own model) 29.24 TPM, TEAD4 (own model) 28.13 TPM, TEAD3 (own model) 17.77 TPM; best model's site strength: ref 84.6th, alt 99.2th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G338 (Unknown, 1 model): best model SNAPC5_FL_CA40NAGCGTA_YWDA_jolma2025_0_3_7mer (own model of SNAPC5), z 22.9, effect 0.368 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SNAPC5 z 22.9. TFs this group covers: SNAPC5 (own model) 86.73 TPM; best model's site strength: ref 80.4th, alt 98.2th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:34:31+00:00)

> No ENCODE RELA ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no RELA experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:31+00:00)

> Open Targets: no association between CYP7A1 and free cholesterol in large LDL measurement (EFO_0022176).
