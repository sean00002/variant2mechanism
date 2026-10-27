# rs7001688 and LDL cholesterol

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 9 model calls; 147 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen

441 of 997 models pass the gate. Top groups: Rel, 1 model (best RELA, z 33.95); C2H2 ZF, 1 model (best CASZ1, z 32.75); AT hook, 2 models (best HMGA1, z 29.74); C2H2 ZF, 1 model (best ZNF580, z -29.06); Unknown, 1 model (best NME2, z 28.95).

## Ranked chains

### 1. H0: Null: no TF-mediated allelic effect (p = 0.77)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at chr8:57573391:G>T mediates an LDL-cholesterol effect in hepatocytes.; Any association with LDL cholesterol is due to a linked causal variant, a passenger mutation, or no true allelic effect.

Falsified if: Allele-specific TF occupancy at chr8:57573391:G>T is demonstrated and causally linked to LDL cholesterol in a relevant hepatocyte context.; A local regulatory element at this variant is shown to regulate a nearby gene and LDL cholesterol independently of a linked causal variant.

### 2. H2: HMGA1 binding at a speculative distal element alters FAM110B (p = 0.11)

TF HMGA1 (stated coverage own_model; registry own_model), alt allele binds more; element Speculative unannotated distal element; no cCRE overlap (E01, E03); gene FAM110B; cell type Hep3B2.1-7 hepatocyte-like cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HMGA1 is predicted to bind the alt allele more strongly than ref in QBiC group G077 (AT hook, own model, z=29.74, effect=2.006; HMGA1 expression 238.96 TPM). The group is not uniformly directional because SETBP1 has the opposite sign, and E19 reports no HMGA1 ENCODE ChIP-seq peak containing the variant in HepG2, although absence can reflect no HMGA1 experiment in that biosample. | weak | [E10](#e10), [E19](#e19) |
| element | The variant could lie in an unannotated distal regulatory element, but E01 reports no regulatory features and E03 reports no cCRE overlap, with the nearest cCRE 1544 bp away. This element claim is speculative. | missing | [E01](#e01), [E03](#e03) |
| gene | FAM110B is the nearest protein-coding gene at 420.6 kb, and E06 is a literature-search hit connecting FAM110B with LDL/statine response, but no quote or direct functional evidence is provided. E20 finds no significant liver eQTL, so the variant-to-FAM110B link is not supported by GTEx liver eQTL. | missing | [E02](#e02), [E06](#e06), [E20](#e20) |
| cell_type | Hep3B2.1-7 expresses HMGA1 at high levels, supporting cell-type availability, but functional relevance of this architectural TF at this site is not demonstrated. | supported | [E10](#e10) |
| phenotype | No direct evidence shows allele-dependent FAM110B expression or an LDL-cholesterol effect. E04 and E05 are null for genetic support, and E20 is negative for liver eQTL; the phenotype direction is not established. | missing | [E04](#e04), [E05](#e05), [E20](#e20) |

Predictions: HMGA1 occupancy is higher on the alt allele than ref at rs7001688 in a hepatocyte model.; FAM110B expression changes with the allele in a hepatocyte or liver model.; LDL cholesterol tracks the FAM110B expression change if the link is causal.

Falsified if: Allele-specific HMGA1 occupancy at rs7001688 is absent in a hepatocyte model.; FAM110B expression is unchanged by the allele in a hepatocyte or liver model.; No chromatin-contact or perturbation evidence links this element to FAM110B.

### 3. H1: RELA binding at a speculative distal element represses CYP7A1 (p = 0.06)

TF RELA (stated coverage own_model; registry own_model), alt allele binds more; element Speculative unannotated distal element; no cCRE overlap (E01, E03); gene CYP7A1; cell type Hep3B2.1-7 hepatocyte-like cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | RELA is predicted to bind the alt allele more strongly than ref in QBiC group G315 (Rel, own model, z=33.95, effect=1.34; RELA expression 73.44 TPM). This is in vitro SELEX evidence only; E18 reports no RELA ENCODE ChIP-seq peak containing the variant in HepG2, although absence can reflect no RELA experiment in that biosample. | weak | [E08](#e08), [E18](#e18) |
| element | The variant could lie in an unannotated distal regulatory element, but E01 reports no regulatory features and E03 reports no cCRE overlap, with the nearest cCRE 1544 bp away. The element claim is therefore speculative. | missing | [E01](#e01), [E03](#e03) |
| gene | An altered RELA site could in principle regulate CYP7A1, a cholesterol/bile-acid gene 926.8 kb away, but E02 provides only genomic distance and E20 finds no significant liver eQTL. No contact or perturbation evidence connects this variant to CYP7A1. | missing | [E02](#e02), [E20](#e20) |
| cell_type | Hep3B2.1-7 expresses RELA, making a hepatic RELA mechanism possible, but this does not establish hepatocyte-like LDL/cholesterol handling by this site. | supported | [E08](#e08) |
| phenotype | No direct evidence links RELA binding at this variant to CYP7A1 expression, bile-acid synthesis, or LDL cholesterol. E04 and E05 are null for genetic support, and the direction of any LDL effect is not established. | missing | [E04](#e04), [E05](#e05), [E20](#e20) |

Predictions: RELA occupancy is higher on the alt allele than ref at rs7001688 in a hepatocyte model.; CYP7A1 expression is reduced when the alt allele is present, if RELA represses CYP7A1.; LDL cholesterol is higher with the alt allele if CYP7A1 repression is causal.

Falsified if: Allele-specific RELA occupancy at rs7001688 is absent in a hepatocyte model.; CYP7A1 expression or bile-acid output is unchanged by the allele in a hepatocyte model.; Genetic colocalization or perturbation shows no causal link between this locus and LDL cholesterol.

### 4. H3: TEAD1 binding at a speculative distal element activates CYP7A1 (p = 0.03)

TF TEAD1 (stated coverage own_model; registry own_model), alt allele binds more; element Speculative unannotated distal element; no cCRE overlap (E01, E03); gene CYP7A1; cell type Hep3B2.1-7 hepatocyte-like cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TEAD1 is predicted to bind the alt allele more strongly than ref in QBiC group G031 (TEA, own model, z=23.14, effect=1.505; TEAD1 expression 29.24 TPM), but TEAD2/TEAD3/TEAD4 also pass and TEAD-family redundancy weakens the specific TEAD1 claim. | weak | [E16](#e16) |
| element | The variant could lie in an unannotated distal regulatory element, but E01 reports no regulatory features and E03 reports no cCRE overlap, with the nearest cCRE 1544 bp away. The element claim is speculative. | missing | [E01](#e01), [E03](#e03) |
| gene | An altered TEAD1 site could in principle act over long distance on CYP7A1, 926.8 kb away, but E02 provides only distance and E20 finds no significant liver eQTL. No contact or perturbation evidence supports this link. | missing | [E02](#e02), [E20](#e20) |
| cell_type | Hep3B2.1-7 expresses TEAD1, making a hepatic TEAD mechanism possible, but this does not establish that this site mediates hepatic cholesterol handling. | supported | [E16](#e16) |
| phenotype | No direct evidence connects TEAD1 binding at this locus to CYP7A1 expression or LDL cholesterol. E04 and E05 are null for genetic support, and the phenotype direction is not established. | missing | [E04](#e04), [E05](#e05), [E20](#e20) |

Predictions: TEAD1 occupancy is higher on the alt allele than ref at rs7001688.; CYP7A1 expression is increased when the alt allele is present, if TEAD1 activates CYP7A1.; LDL cholesterol is lower with the alt allele if CYP7A1 activation is causal.

Falsified if: Allele-specific TEAD1 occupancy at rs7001688 is absent.; CYP7A1 expression is unchanged by the allele in a hepatocyte model.; TEAD2/TEAD3/TEAD4, rather than TEAD1, account for any allelic binding effect at this site.

### 5. H4: ZNF580 loss of binding at a speculative distal element derepresses FAM110B (p = 0.03)

TF ZNF580 (stated coverage own_model; registry own_model), ref allele binds more; element Speculative unannotated distal element; no cCRE overlap (E01, E03); gene FAM110B; cell type Hep3B2.1-7 hepatocyte-like cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF580 is predicted to bind the ref allele more strongly than alt in QBiC group G540 (C2H2 ZF, own model, z=-29.06, effect=-1.205; ZNF580 expression 8.54 TPM). This is in vitro SELEX evidence only and ZNF580 expression is low. | weak | [E11](#e11) |
| element | The variant could alter an unannotated distal regulatory element, but E01 reports no regulatory features and E03 reports no cCRE overlap, with the nearest cCRE 1544 bp away. The element claim is speculative. | missing | [E01](#e01), [E03](#e03) |
| gene | Loss of a ZNF580 site could affect FAM110B, 420.6 kb upstream, but E02 gives only genomic distance; no direct ZNF580-FAM110B evidence or liver eQTL support is provided. | missing | [E02](#e02), [E20](#e20) |
| cell_type | Hep3B2.1-7 expresses ZNF580 at low levels, making this a weaker cell-type rationale than for higher-expression candidates. | supported | [E11](#e11) |
| phenotype | If ZNF580 normally represses a target gene, loss of ZNF580 binding on the alt allele could derepress the target and alter LDL cholesterol, but no evidence establishes this direction or the phenotype link. | missing | [E04](#e04), [E05](#e05), [E20](#e20) |

Predictions: ZNF580 occupancy is higher on the ref allele than alt at rs7001688.; The target gene is derepressed on the alt allele if ZNF580 represses it.; LDL cholesterol differs according to the target-gene direction.

Falsified if: ZNF580 occupancy is not higher on the ref allele.; FAM110B or another target gene is unchanged when the ZNF580 site is lost.; ZNF580 is not expressed or functional in the relevant hepatocyte context.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H2 | H1 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific HMGA1 ChIP-qPCR at rs7001688 in Hep3B2.1-7 | medium | yes | No allele-specific HMGA1 occupancy at rs7001688. | HMGA1 occupancy is higher on the alt allele than ref. | No allele-specific HMGA1 occupancy; RELA, not HMGA1, is the candidate TF. | No allele-specific HMGA1 occupancy; TEAD1 is the candidate TF. | No allele-specific HMGA1 occupancy; ZNF580 is the candidate TF. |
| Allele-specific RELA ChIP-qPCR at rs7001688 in Hep3B2.1-7 | medium | no | No allele-specific RELA occupancy at rs7001688. | No allele-specific RELA occupancy; HMGA1 is the candidate TF. | RELA occupancy is higher on the alt allele than ref. | No allele-specific RELA occupancy; TEAD1 is the candidate TF. | No allele-specific RELA occupancy; ZNF580 is the candidate TF. |
| Allele-specific expression or liver eQTL for FAM110B by rs7001688 genotype | medium | yes | No allele-dependent FAM110B expression in liver or hepatocyte models. | FAM110B expression changes with the allele, consistent with an HMGA1-linked effect. | No allele-dependent FAM110B expression; CYP7A1 is the proposed target. | No allele-dependent FAM110B expression; CYP7A1 is the proposed target. | FAM110B is derepressed on the alt allele if ZNF580 represses it. |

## Next experiment

Allele-specific HMGA1 ChIP-qPCR at rs7001688 in Hep3B2.1-7 is the cheapest experiment that separates the top two chains H0 and H2: H0 predicts no allele-specific HMGA1 occupancy, whereas H2 predicts higher HMGA1 occupancy on the alt allele.

## Investigate calls

- chip_peaks({"tf": "RELA", "biosample": "HepG2"})
- chip_peaks({"tf": "HMGA1", "biosample": "HepG2"})
- eqtl_lookup({"tissue": "Liver"})

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

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:34:31+00:00)

> No ENCODE RELA ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no RELA experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:45:05+00:00)

> No ENCODE HMGA1 ChIP-seq peak contains chr8:57573391:G>T in biosamples matching 'HepG2'. Absence can also mean no HMGA1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_57573391_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:31+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_57573391_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).
