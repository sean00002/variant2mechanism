# rs7001688 and LDL cholesterol

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.54 over 7 model calls; 209 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen

441 of 997 models pass the gate. Top groups: Rel, 1 model (best RELA, z 33.95); C2H2 ZF, 1 model (best CASZ1, z 32.75); AT hook, 2 models (best HMGA1, z 29.74); C2H2 ZF, 1 model (best ZNF580, z -29.06); Unknown, 1 model (best NME2, z 28.95).

## Ranked chains

### 1. H0: No TF-mediated effect of this variant (passenger, or tag for a causal variant elsewhere) (p = 0.72)

Null chain: no TF-mediated effect of this variant.

Predictions: Allelic reporter (luciferase/MPRA) of the 200 bp around chr8:57573391 shows no reproducible allele-specific activity in Hep 3B2.1-7 or HepG2.; No allele-specific ATAC or TF ChIP signal at the site in liver cells; consistent with E19 (no RELA peak in HepG2) and E03 (no cCRE).; No liver eQTL appears for any gene within 1 Mb, as already observed (E18); any LDL signal in this 1 Mb window, if real, maps to another variant near a lipid gene such as CYP7A1 (927 kb away, E02).; CRISPRi at the site leaves FAM110B, BPNT2, UBXN2B, CYP7A1 and SDCBP expression unchanged.

Falsified if: An MPRA or base-edited allelic comparison shows reproducible allele-specific regulatory activity at this exact position in hepatocytes.; Allele-specific ATAC/ChIP occupancy or a liver eQTL/Hi-C contact for rs7001688 is demonstrated.; A fine-mapped GWAS credible set for LDL cholesterol includes rs7001688.

### 2. H2: Alt allele increases HMGA1 AT-hook binding at a local, weakly annotated site (p = 0.09)

TF HMGA1 (stated coverage own_model; registry own_model), alt allele binds more; element AT-rich unannotated site at chr8:57573391 (no cCRE); gene unresolved (no eQTL or contact evidence for any gene within 1 Mb); cell type Hepatocyte (Hep 3B2.1-7, ACH-000625).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The HMGA1 own model predicts stronger alt binding (z 29.74, 67.3th -> 96.4th percentile). Within AT-hook group G077, HMGA1 is named over HMGA2 (97.4 TPM), SRCAP, ASH1L and SETBP1 because it is both the best-scoring own model and the most expressed; however SETBP1 in the same group predicts the opposite direction, and HMGA2 cannot be excluded, so the TF call is weak. | weak | [E10](#e10) |
| element | No cCRE overlaps the site and GERP is 0.267, so there is no positive evidence of a regulatory element; AT-hook proteins do bind low-specificity AT-rich DNA without canonical enhancer marks. | missing | [E01](#e01), [E03](#e03) |
| gene | No gene is linked: no significant liver eQTL for this variant and no Open Targets record; all protein-coding genes are >=420 kb away. | missing | [E18](#e18), [E05](#e05), [E02](#e02) |
| cell_type | HMGA1 is very highly expressed (239 TPM) in this hepatocyte line, so occupancy is possible, but occupancy at this site is not shown. | weak | [E10](#e10) |
| phenotype | No evidence ties this site or any candidate target to LDL cholesterol; GWAS Catalog and Open Targets have no record for the variant. | missing | [E04](#e04), [E05](#e05) |

Predictions: HMGA1 CUT&RUN shows alt-preferential signal at the site; effect is broad/architectural rather than a sharp enhancer switch.; HMGA1 knockdown abolishes any allelic difference in reporter assays, while NF-kB or YAP manipulation does not.; Allelic effect persists in cells with low Hippo/YAP activity.

Falsified if: No HMGA1 occupancy at the locus, or ref-preferential occupancy (SETBP1 direction).; HMGA1 knockdown leaves any allelic difference intact.

### 3. H3: Alt allele strengthens a TEAD-family site (TEAD1 named) at an unannotated hepatic site (p = 0.08)

TF TEAD1 (stated coverage own_model; registry own_model), alt allele binds more; element Unannotated site at chr8:57573391 (no cCRE); gene unresolved (FAM110B 421 kb and BPNT2 580 kb are distance-only candidates); cell type Hepatocyte (Hep 3B2.1-7, ACH-000625).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | All four models in TEA group G031 agree on stronger alt binding (TEAD1 z 23.14, effect 1.505, 84.6th -> 99.2th percentile; TEAD4, TEAD2, TEAD3 same sign). Direction is the group-level call; TEAD1 is named only because it is the best-scoring own model, and the paralogs are expressed at similar levels (17-34 TPM), so the specific TF within the family is not resolved. | weak | [E16](#e16) |
| element | No cCRE and no VEP regulatory feature overlap the site, so no element is demonstrated. | missing | [E01](#e01), [E03](#e03) |
| gene | No gene link: no significant liver eQTL and no Open Targets record for this variant; candidates rest on distance alone. | missing | [E18](#e18), [E05](#e05), [E02](#e02) |
| cell_type | TEAD1-4 are all expressed in this hepatocyte line, but Hippo/YAP pathway activity and occupancy at this site are unverified. | weak | [E16](#e16) |
| phenotype | No genetic association supports a route from this variant to LDL cholesterol; Open Targets also shows no CYP7A1-lipid association for the queried trait. | missing | [E04](#e04), [E05](#e05), [E20](#e20) |

Predictions: TEAD/YAP-TAZ CUT&RUN shows alt-preferential signal; allelic reporter difference depends on YAP/TAZ activity.; Verteporfin or YAP/TAZ knockdown abolishes the allelic difference, while HMGA1 or RELA perturbation does not.; Effect is visible only in Hippo-inactive (YAP-on) hepatocyte states.

Falsified if: No TEAD/YAP occupancy at the locus in liver data.; Allelic reporter difference is independent of YAP/TAZ manipulation.

### 4. H4: Ref allele is the high-affinity ZNF580 site; alt reduces binding (p = 0.06)

TF ZNF580 (stated coverage own_model; registry own_model), ref allele binds more; element Unannotated site at chr8:57573391 (no cCRE); gene unresolved (no eQTL or contact evidence); cell type Hepatocyte (Hep 3B2.1-7, ACH-000625).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF580 (sole member of group G540, own model) is the strongest loss-of-binding prediction (z -29.06, effect -1.205), ref at the 100.0th and alt at the 94.4th percentile; both alleles remain high-affinity, so the predicted change is modest, and ZNF580 expression is low (8.5 TPM). | weak | [E11](#e11) |
| element | No cCRE or regulatory feature overlaps the site, so no element is demonstrated. | missing | [E03](#e03), [E01](#e01) |
| gene | No gene link: no significant liver eQTL and no Open Targets record for this variant. | missing | [E18](#e18), [E05](#e05) |
| cell_type | ZNF580 is expressed but at low level in this line; occupancy at this site is not shown. | weak | [E11](#e11) |
| phenotype | No cited evidence ties ZNF580 or any candidate target gene to LDL cholesterol. | missing | [E04](#e04), [E05](#e05) |

Predictions: Occupancy and/or reporter activity are ref-preferential, the opposite direction to H1-H3.; ZNF580 knockdown specifically reduces ref-allele reporter activity.; In an allelic MPRA, ref > alt activity.

Falsified if: Allele-specific assays show alt-preferential binding or activity.; ZNF580 depletion has no effect on either allele.

### 5. H1: Alt allele creates a stronger NF-kB (RELA) site in an unannotated hepatic element (p = 0.05)

TF RELA (stated coverage own_model; registry own_model), alt allele binds more; element Unannotated site at chr8:57573391; no cCRE overlap, nearest cCRE EH38E3835076 1544 bp away; gene unresolved (no gene linked by eQTL or contact data; FAM110B at 421 kb is only the nearest); cell type Hepatocyte (Hep 3B2.1-7, ACH-000625).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The RELA own model predicts stronger alt binding (z 33.95, effect 1.34; site strength 97.4th -> 99.8th percentile). Within Rel group G315 RELA is named over RELB (17.4 TPM) and REL (4.3 TPM) because it is the most expressed member in this line and is the model with its own SELEX data. This is an in vitro prediction only. | weak | [E08](#e08), [E07](#e07) |
| element | No evidence of an element: no cCRE overlaps the site and VEP reports no regulatory feature; any element here would be unannotated and cell-type restricted. | missing | [E01](#e01), [E03](#e03) |
| gene | No target gene is supported: no liver eQTL for this variant and no Open Targets record; FAM110B at 421 kb is a distance-only guess. | missing | [E18](#e18), [E05](#e05), [E02](#e02) |
| cell_type | RELA is abundant (73.4 TPM) in this hepatocyte line, but no RELA ChIP peak contains the site in HepG2, which argues against baseline occupancy (absence may also reflect no suitable experiment). | weak | [E08](#e08), [E19](#e19) |
| phenotype | No evidence links this variant or FAM110B to LDL cholesterol; E06 is a pravastatin cardiovascular-event study retrieved by keyword and does not show a FAM110B-LDL variant effect, and E04/E05 report no association. | missing | [E04](#e04), [E05](#e05), [E06](#e06) |

Predictions: Allele-specific RELA ChIP/CUT&RUN signal (alt > ref) appears only after TNF or IL-1 stimulation of hepatocytes, not at baseline.; Allelic reporter difference emerges under NF-kB activation and is abolished by IKK inhibition.; Uniquely among these chains, the allelic effect is stimulus-dependent rather than constitutive.

Falsified if: No RELA occupancy at this locus in stimulated hepatocyte ChIP data.; Allelic reporter difference is present at baseline and unchanged by NF-kB stimulation or IKK inhibition.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H2 | H3 | H4 | H1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Liver eQTL lookup for rs7001688 (GTEx v8) - already done (E18) | existing data | yes | No significant eQTL (observed) - consistent | Absence weakens | Absence weakens | Absence weakens | Expected an eQTL for a nearby gene; absence weakens |
| RELA ChIP-seq peak overlap in HepG2 (Factorbook) - already done (E19) | existing data | no | No peak (observed) - consistent | Uninformative | Uninformative | Uninformative | No baseline peak; H1 survives only as stimulus-dependent |
| Allelic luciferase/MPRA of the 200 bp around chr8:57573391 in Hep 3B2.1-7 at baseline | medium | yes | No allelic difference, and little or no enhancer activity over empty vector | Modest alt > ref activity at baseline | alt > ref at baseline, YAP-activity dependent | ref > alt at baseline | Little difference at baseline (difference only after TNF/IL-1) |
| Same allelic reporter with and without TNF stimulation (NF-kB on/off) | medium | no | No allelic difference in either condition | Allelic difference unchanged by TNF | Allelic difference unchanged by TNF | Allelic difference unchanged by TNF | Allelic difference appears or increases with TNF |
| HMGA1 CUT&RUN and HMGA1 knockdown in Hep 3B2.1-7 | high | yes | No site-specific signal; knockdown has no allelic effect | alt-preferential HMGA1 signal; knockdown abolishes allelic difference | No HMGA1 dependence | No HMGA1 dependence | No HMGA1 dependence |
| YAP/TAZ knockdown or verteporfin during allelic reporter assay | medium | no | No allelic difference to abolish | Allelic difference persists | Allelic difference abolished | Allelic difference persists | Allelic difference persists |
| CRISPRi tiling of the site plus RT-qPCR of FAM110B, BPNT2, UBXN2B, CYP7A1, SDCBP | high | yes | No gene changes | Target gene changes modestly | Target gene changes | Target gene changes | Target gene (if any) decreases |

## Next experiment

A baseline allele-specific luciferase/MPRA of the ~200 bp window centred on chr8:57573391 in Hep 3B2.1-7 (both alleles, >=6 replicates, empty-vector control). It is the cheapest assay that distinguishes H0 (no allelic activity, the current leader) from the leading mechanistic chain H2 (modest alt > ref activity), and its direction also separates H4 (ref > alt) from H2/H3.

## Investigate calls

- eqtl_lookup({"tissue": "Liver"})
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

> QBiC-SELEX screen of chr8:57573391:G>T: 997 models scored, 441 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 316 CIS-BP groups. Expression context: DepMap line ACH-000625. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 73 (BED ZF, 1 model z 24.73, C2H2 ZF, 1 model z -21.17, DM, 5 models z -18.3, C2H2 ZF, 1 model z 16.96, C2H2 ZF, 1 model z -16.13). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G315 (Rel, 1 model): best model RELA_DBD_TGATCC20NCTA_KI_nitta2015_1_3_7mer (own model of RELA), z 33.95, effect 1.34 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: RELA z 33.95. TFs this group covers (own and CIS-BP-mapped models): RELA 73.44 TPM, RELB 17.37 TPM, REL 4.27 TPM; best model's site strength: ref 97.4th, alt 99.8th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G138 (C2H2 ZF, 1 model): best model CASZ1_FL_AG40NGGAATC_YWKC_jolma2025_0_4_7mer (own model of CASZ1), z 32.75, effect 2.741 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CASZ1 z 32.75. TFs this group covers (own and CIS-BP-mapped models): CASZ1 4.18 TPM; best model's site strength: ref 99.1th, alt 99.8th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G077 (AT hook, 2 models): best model HMGA1_FL_GA40NCTGATT_YWPA_jolma2025_0_3_7mer (own model of HMGA1), z 29.74, effect 2.006 (alt binds more); 2 passing models (1 with the best model's sign); members disagree on direction. Passing members: HMGA1 z 29.74, SETBP1 z -15.21. TFs this group covers (own and CIS-BP-mapped models): HMGA1 238.96 TPM, HMGA2 97.36 TPM, SRCAP 41.42 TPM, ASH1L 21.18 TPM, SETBP1 1.24 TPM; best model's site strength: ref 67.3th, alt 96.4th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G540 (C2H2 ZF, 1 model): best model ZNF580_FL_TGGCCA40NTTC_KAE_yin2017_0_4_7mer (own model of ZNF580), z -29.06, effect -1.205 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF580 z -29.06. TFs this group covers (own and CIS-BP-mapped models): ZNF580 8.54 TPM; best model's site strength: ref 100.0th, alt 94.4th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G266 (Unknown, 1 model): best model NME2_FL_TA40NTCACTC_YWDA_jolma2025_0_4_7mer (own model of NME2), z 28.95, effect 0.573 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: NME2 z 28.95. TFs this group covers (own and CIS-BP-mapped models): NME2 928.15 TPM; best model's site strength: ref 65.7th, alt 99.1th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G460 (C2H2 ZF, 1 model): best model ZNF230_FL_TG40NGACCTT_YWDA_jolma2025_0_3_7mer (own model of ZNF230), z 26.94, effect 0.512 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF230 z 26.94. TFs this group covers (own and CIS-BP-mapped models): ZNF230 1.96 TPM; best model's site strength: ref 70.8th, alt 96.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G018 (E2F, 4 models): best model E2F4_eDBD_TCAGGG40NGCA_KO_yin2017_1_3_7mer (own model of E2F4), z 25.88, effect 1.189 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: E2F4 z 25.88, E2F3 z 17.58. TFs this group covers (own and CIS-BP-mapped models): E2F4 58.99 TPM, E2F3 36.15 TPM, E2F5 18.97 TPM, E2F6 18.07 TPM, E2F1 11.74 TPM, E2F2 2.06 TPM; best model's site strength: ref 98.4th, alt 100.0th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G499 (C2H2 ZF, 1 model): best model ZNF384_FL_GG40NTAGTTT_AATBA_jolma2025_0_3_7mer (own model of ZNF384), z -24.76, effect -0.523 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZNF384 z -24.76. TFs this group covers (own and CIS-BP-mapped models): ZNF384 82.82 TPM; best model's site strength: ref 82.1th, alt 68.4th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G031 (TEA, 4 models): best model TEAD1_FL_TCACGC40NACT_KW_yin2017_0_4_7mer (own model of TEAD1), z 23.14, effect 1.505 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: TEAD1 z 23.14, TEAD4 z 10.66, TEAD2 z 9.59, TEAD3 z 8.07. TFs this group covers (own and CIS-BP-mapped models): TEAD2 34.44 TPM, TEAD1 29.24 TPM, TEAD4 28.13 TPM, TEAD3 17.77 TPM; best model's site strength: ref 84.6th, alt 99.2th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G338 (Unknown, 1 model): best model SNAPC5_FL_CA40NAGCGTA_YWDA_jolma2025_0_3_7mer (own model of SNAPC5), z 22.9, effect 0.368 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SNAPC5 z 22.9. TFs this group covers (own and CIS-BP-mapped models): SNAPC5 86.73 TPM; best model's site strength: ref 80.4th, alt 98.2th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:34:31+00:00)

> No ENCODE RELA ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2' (0 peaks within 100 bp). Absence can also mean no RELA experiment in that biosample.

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:31+00:00)

> Open Targets: no association between CYP7A1 and free cholesterol in large LDL measurement (EFO_0022176).
