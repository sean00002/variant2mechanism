# rs642961 and Cleft lip (IRF6)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.59 over 8 model calls; 191 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## QBiC-SELEX screen

222 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 77.65); Ets, 1 model (best SPDEF, z 42.64); TEA, 4 models (best TEAD1, z -40.19); HSF, 5 models (best HSF5, z -29.76); HSF, 3 models (best HSF1, z -29.65).

## Ranked chains

### 1. H1: Risk allele A disrupts an AP-2alpha (TFAP2A) site in the MCS9.7-type IRF6 enhancer, lowering IRF6 in oral periderm (p = 0.60)

TF TFAP2A (stated coverage mapped; registry own_model), alt allele binds more; element EH38E2863563 / ENSR1_B3JM9C distal enhancer ~9.7 kb upstream of IRF6 (the MCS9.7-type enhancer); gene IRF6; cell type oral periderm / embryonic craniofacial ectoderm.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC AP-2 group G030 predicts the alt G allele binds AP-2 proteins more strongly than ref A (effect +1.69; ref 78.9th vs alt 99.9th k-mer percentile), i.e. the cleft-risk A allele weakens an AP-2 site; within this specificity group TFAP2A is named not because it is the top-scoring model (it is the weakest member, z 11.94, and TFAP2A is listed only among the group's covered own/CIS-BP-mapped TFs) but because published EMSA and ChIP at this exact enhancer show the risk allele disrupts an AP-2alpha binding site; note no ENCODE TFAP2A ChIP peak covers the variant, which may reflect biosample coverage | supported | [E13](#e13), [E19b](#e19b), [E19d](#e19d), [E18](#e18) |
| element | The variant lies in an ENCODE distal enhancer-like cCRE (EH38E2863563, DNase z 5.3, H3K27ac z 5.0, maxima across biosamples) and an Ensembl enhancer, and this element was independently identified by multispecies comparison as an IRF6 enhancer whose activity in mouse is craniofacial and limb | supported | [E01](#e01), [E03](#e03), [E19c](#e19c), [E19d](#e19d) |
| gene | The element is 9.7 kb from the IRF6 TSS and IRF6 is the gene whose enhancer this was shown to be in reporter mice; L2G gives IRF6 up to 0.67 but UTP25 scores higher (0.75) and the cleft-specific set gives IRF6 only 0.16, so the gene assignment rests mainly on the published enhancer work plus IRF6's established cleft association (Open Targets 0.54, genetic_association 0.72) | weak | [E02](#e02), [E05](#e05), [E19c](#e19c), [E19d](#e19d), [E20](#e20) |
| cell_type | Mouse expression analysis localises this enhancer's activity to craniofacial and limb structures, which is the only cell-type evidence available; the cited QTLs here are blood/monocyte TRAF3IP3 only, and there is no periderm eQTL or expression context in this case | weak | [E19d](#e19d), [E05](#e05) |
| phenotype | Reduced AP-2alpha-driven IRF6 in periderm impairs epithelial differentiation and lip fusion, matching the A risk allele for orofacial clefts (p 2e-06, PIP only 0.05) and the common-variant risk attributed to rs642961 at this locus | weak | [E04](#e04), [E19a](#e19a), [E06a](#e06a) |

Predictions: Allele-specific EMSA/ChIP shows AP-2alpha binds the G allele and not (or much less) the A allele at this position; Luciferase/MPRA of this enhancer in keratinocyte or periderm-like cells gives lower activity for A; TFAP2A knockdown reduces enhancer activity and abolishes the allelic difference, whereas ETS or TEAD knockdown does not; Enhancer deletion or A/G base editing changes IRF6, not UTP25 or TRAF3IP3, in oral epithelial cells

Falsified if: EMSA/ChIP shows equal or A-preferential AP-2alpha binding at this site; Allelic reporter difference is absent or reversed in oral epithelial cells; TFAP2A depletion leaves the allelic difference intact

### 2. H5: Null: no TF-mediated effect of rs642961 itself; the cleft signal reflects a linked causal variant (e.g. the IRF6 promoter SNP) or another gene (p = 0.23)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-specific reporter and TF occupancy assays show no difference between A and G at this position; Fine-mapping PIP stays low (orofacial clefts PIP 0.05) and the functional effect tracks a neighbouring variant such as the IRF6 promoter SNP rs12403599; Molecular QTL signal at this locus maps to TRAF3IP3 in blood rather than IRF6 in epithelium; The strongest association at this SNP (blood pressure) is unrelated to IRF6 enhancer function

Falsified if: Allele-specific enhancer activity or TF occupancy at rs642961 is demonstrated in epithelial cells; Base editing of this single position alters IRF6 expression or periderm phenotype

### 3. H2: Alt allele creates an Ets site (ETV5/ELF-family specificity) that raises enhancer output; risk allele A is the low-Ets allele (p = 0.12)

TF ETV5 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E2863563 distal enhancer upstream of IRF6; gene IRF6; cell type embryonic oral/facial epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The largest QBiC signal at this site is Ets group G003 (18/18 concordant models; ETV5 own model z 77.65, effect +1.32; ref 65.0th vs alt 99.2th percentile), with a second Ets group G345 (SPDEF own model, effect +1.62) also alt-preferring; ETV5 is named only as the group's best own model, and no expression or ChIP evidence here distinguishes it from ELF/EHF members covered by the same specificity | weak | [E08](#e08), [E09](#e09) |
| element | The predicted Ets gain lies within an active distal enhancer-like cCRE with high DNase/H3K27ac (biosample maxima) | weak | [E01](#e01), [E03](#e03) |
| gene | IRF6 is 9.7 kb away and the element has reporter-validated IRF6 enhancer activity, though UTP25 has the higher best L2G (0.75 vs 0.67) | weak | [E02](#e02), [E05](#e05), [E19c](#e19c) |
| cell_type | No cell-type evidence is cited for Ets factor expression in embryonic oral epithelium; the only available QTLs are blood/monocyte TRAF3IP3 | missing | [E05](#e05) |
| phenotype | Lower Ets-driven IRF6 on the A allele would reduce periderm IRF6 and raise cleft risk, direction-consistent with the A effect allele for orofacial clefts | weak | [E04](#e04) |

Predictions: Mutating only the Ets core, leaving the AP-2 core intact, abolishes the allelic reporter difference; ETS-family (ETV5/ELF3) ChIP shows allele-biased occupancy favouring G; Knockdown of an epithelial Ets factor, not TFAP2A, removes the allelic effect

Falsified if: No Ets occupancy or footprint on either allele; Allelic effect persists after Ets-core mutagenesis; TFAP2A depletion alone removes the entire allelic difference

### 4. H3: Ref (risk) allele A preferentially binds TEAD factors that dampen the enhancer (p = 0.05)

TF TEAD1 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E2863563 distal enhancer upstream of IRF6; gene IRF6; cell type embryonic craniofacial epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC TEA group G031 shows all four TEADs binding ref A more strongly (TEAD1 own model z -40.19, effect -2.55; ref 99.4th vs alt 75.7th percentile); TEAD1 is chosen as the best-scoring own model, with no expression or ChIP evidence to pick among TEAD1-4 | weak | [E10](#e10) |
| element | The site is an active distal enhancer-like cCRE; TEAD occupancy there is not shown by any cited data | weak | [E01](#e01), [E03](#e03) |
| gene | The enhancer drives IRF6 in reporter assays and is 9.7 kb from its TSS, although UTP25 has the higher L2G | weak | [E02](#e02), [E05](#e05), [E19c](#e19c) |
| cell_type | No cited evidence for TEAD/Hippo activity in craniofacial tissue at this element | missing | none |
| phenotype | If TEAD acts as a repressor here, gained occupancy on A would lower IRF6 and raise cleft risk, consistent in direction with the A-allele association but with the repressor role unproven | weak | [E04](#e04) |

Predictions: TEAD1 ChIP shows A-preferential binding at this element; YAP/TEAD inhibition changes reporter activity in an allele-dependent way; AP-2alpha perturbation leaves part of the allelic difference intact

Falsified if: No TEAD occupancy at the element in craniofacial cells; Allelic reporter difference is unaffected by TEAD knockdown; AP-2alpha depletion removes the entire allelic difference

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA plus ChIP for TFAP2A on A vs G oligos/alleles in a craniofacial epithelial line | low | yes | G-preferential AP-2alpha binding; A allele loses the site | No allelic binding difference for any TF | No or weak AP-2alpha allelic bias; Ets factor bias instead | No AP-2alpha bias; A-preferential TEAD binding |
| Luciferase/MPRA of the enhancer, A vs G, in keratinocyte/periderm-like cells | low | yes | A gives lower activity | No allelic difference | A gives lower activity | A gives lower activity only if TEAD represses |
| TFAP2A knockdown versus ETS (ETV5/ELF3) knockdown versus TEAD knockdown, each with allelic reporter | medium | no | Only TFAP2A knockdown abolishes the allelic difference | No allelic difference to abolish | Only Ets knockdown abolishes it | Only TEAD/YAP perturbation changes it |
| Motif-core mutagenesis: disrupt AP-2 core only, or Ets core only, in the reporter | low | no | AP-2 core mutation removes the allelic difference; Ets core mutation does not | No allelic difference in any construct | Ets core mutation removes it; AP-2 core mutation does not | Neither removes it |
| Base editing A>G at the endogenous site (or enhancer deletion) in oral epithelial cells with RNA-seq of IRF6, UTP25, TRAF3IP3 | high | yes | IRF6 rises with G; UTP25/TRAF3IP3 unchanged | No expression change at this single position | IRF6 rises with G (same direction, different TF dependence) | IRF6 rises with G if TEAD represses |
| ENCODE/Factorbook query for TFAP2A peaks at the variant (existing data) | existing data | no | No peak found; explained as missing craniofacial biosample | No peak expected | No TFAP2A peak expected | No TFAP2A peak expected |

## Next experiment

Allele-specific EMSA (A vs G probes) with TFAP2A supershift, plus allelic ChIP in a craniofacial/keratinocyte line: cheapest assay that distinguishes H1 (G-preferential AP-2alpha binding) from the null H5 (no allelic binding difference).

## Investigate calls

- chip_peaks({"tf": "TFAP2A", "biosample": null})
- literature_search({"query": "rs642961 IRF6 enhancer AP-2alpha binding site cleft lip"})
- gene_disease({"gene": "IRF6"})

## Flags

- coverage_misstated: H1: stated mapped, registry says own_model for TFAP2A

Citation support: 0.93 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/1:209815925-209815925:1/G?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:29:41+00:00)

> Variant chr1:209815925:A>G (GRCh38), allele string A/G
> Known IDs: rs642961
> Most severe consequence: regulatory_region_variant
> Regulatory features: ENSR1_B3JM9C enhancer
> GERP conservation score at the site: 0.516
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/1:208815925-210815925?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:29:25+00:00)

> 13 protein-coding genes within 1000 kb of chr1:209815925:A>G, by distance to TSS:
> IRF6: 9.7 kb from TSS (upstream, strand -1)
> ENSG00000289700: 9.7 kb from TSS (upstream, strand -1)
> UTP25: 12.0 kb from TSS (upstream, strand +1)
> C1orf74: 31.3 kb from TSS (upstream, strand -1)
> TRAF3IP3: 60.4 kb from TSS (downstream, strand +1)
> SYT14: 85.0 kb from TSS (upstream, strand +1)
> HSD11B1: 129.8 kb from TSS (downstream, strand +1)
> G0S2: 140.5 kb from TSS (downstream, strand +1)
> LAMB3: 162.8 kb from TSS (upstream, strand -1)
> CAMK1G: 232.2 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:29:16+00:00)

> The variant lies in cCRE EH38E2863563 (dELS: distal enhancer-like), chr1:209815915-209816264.
> SCREEN: 2 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2863563 dELS (contains the variant): DNase z 5.3, H3K27ac z 5.0, H3K4me3 z 2.4, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> EH38E2863562 dELS: DNase z 3.2, H3K27ac z 4.9, H3K4me3 z 1.9, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs642961&size=100; retrieved 2026-10-25T17:29:42+00:00)

> 8 GWAS Catalog associations for rs642961, strongest first:
> Systolic blood pressure: p 6.0e-12, effect allele G, risk-allele frequency NR, PMID 38689001
> Hypertension: p 2.0e-08, effect allele A, risk-allele frequency 0.1951, PMID 33230300
> Pulse pressure: p 1.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Diastolic blood pressure: p 3.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Orofacial clefts: p 2.0e-06, effect allele A, risk-allele frequency NR, PMID 19270707

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:41+00:00)

> 18 credible sets contain 1_209815925_A_G: 14 GWAS, 4 molecular QTL.
> GWAS Systolic blood pressure: PIP 0.10; L2G TRAF3IP3 0.11, IRF6 0.11, UTP25 0.10
> GWAS Systolic blood pressure: PIP 0.09; L2G IRF6 0.67, UTP25 0.14, TRAF3IP3 0.08
> GWAS Systolic blood pressure, combined automated + manual reading: PIP 0.05; L2G IRF6 0.13, UTP25 0.10, C1orf74 0.10
> GWAS Orofacial clefts: PIP 0.05; L2G IRF6 0.16, TRAF3IP3 0.12, C1orf74 0.10
> GWAS Systolic blood pressure: PIP 0.05; L2G IRF6 0.13, C1orf74 0.09, UTP25 0.08
> GWAS Systolic blood pressure (MTAG): PIP 0.05; L2G IRF6 0.17, C1orf74 0.09, UTP25 0.08
> eqtl for TRAF3IP3 (blueprint_tx_monocyte_enst00000460314): PIP 0.04
> eqtl for TRAF3IP3 (twinsuk_tx_blood_enst00000367023): PIP 0.02
> eqtl for TRAF3IP3 (twinsuk_exon_blood_ensg00000009790_15_1_209782056_): PIP 0.02
> eqtl for TRAF3IP3 (schmiedel_2018_exon_treg_naive_ensg00000009790_15_): PIP 0.02
> Best L2G gene scores across these sets: UTP25 0.75, IRF6 0.67, TRAF3IP3 0.53, C1orf74 0.10

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20AND%20UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:43+00:00)

> Europe PMC: 2 hits for 'rs642961 AND UTP25 AND "cleft lip"'; top 2 with PMIDs:
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-25T17:29:43+00:00)

> Conditional analyses of GWAS data suggest the two functional SNPs near IRF6 account for the majority of risk for CL/P at this locus.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 37161310 (https://europepmc.org/article/MED/37161310; retrieved 2026-10-25T17:29:43+00:00)

> The single-nucleotide polymorphism (SNP) rs2235371 (IRF6 V274I) is associated with nonsyndromic cleft lip with or without cleft palate (NSCL/P) in Han Chinese and other populations but appears to be without a functional effect.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 37161310 (https://europepmc.org/article/MED/37161310; retrieved 2026-10-25T17:29:43+00:00)

> This study revealed that the SNP rs12403599, within the IRF6 promoter, is associated with all phenotypes of NSCL/P, especially nonsyndromic cleft lip (NSCLO) and a subphenotype of it, microform cleft lip (MCL).

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:209815925:A>G: 997 models scored, 222 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 140 CIS-BP groups. Expression context: none: expression filter skipped. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 0. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 77.65, effect 1.32 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: ETV5 z 77.65, ETS2 z 47.72, ETV2 z 31.41, ETV4 z 30.23, ETS1 z 27.66 (+13 more). TFs this group covers (own and CIS-BP-mapped models): EHF, ELF1, ELF2, ELF3, ELF4, ELF5, ELK1, ELK3, ELK4, ERF (+15 more); best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G345 (Ets, 1 model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (own model of SPDEF), z 42.64, effect 1.62 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SPDEF z 42.64. TFs this group covers (own and CIS-BP-mapped models): ELF1, ELF2, ELF4, SPDEF; best model's site strength: ref 89.2th, alt 99.8th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G031 (TEA, 4 models): best model TEAD1_FL_TCACGC40NACT_KW_yin2017_0_4_7mer (own model of TEAD1), z -40.19, effect -2.547 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TEAD1 z -40.19, TEAD2 z -39.78, TEAD3 z -32.45, TEAD4 z -26.55. TFs this group covers (own and CIS-BP-mapped models): TEAD1, TEAD2, TEAD3, TEAD4; best model's site strength: ref 99.4th, alt 75.7th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G014 (HSF, 5 models): best model HSF5_eDBD_TATGCT40NACT_KT_yin2017_0_3_7mer (own model of HSF5), z -29.76, effect -0.875 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: HSF5 z -29.76, HSFY2 z -12.29. TFs this group covers (own and CIS-BP-mapped models): HSF5, HSFX1, HSFX2, HSFY1, HSFY2; best model's site strength: ref 99.4th, alt 92.8th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G039 (HSF, 3 models): best model HSF1_eDBD_TCTAAA40NCGC_KN_yin2017_0_4_7mer (own model of HSF1), z -29.65, effect -1.427 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: HSF1 z -29.65, HSF4 z -26.38, HSF2 z -25.12. TFs this group covers (own and CIS-BP-mapped models): HSF1, HSF2, HSF4; best model's site strength: ref 100.0th, alt 90.6th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2B_FL_TGTCCG20NGA_KH_nitta2015_1_3_7mer (own model of TFAP2B), z 23.98, effect 1.688 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: TFAP2B z 23.98, TFAP2C z 17.39, TFAP2E z 13.97, TFAP2A z 11.94. TFs this group covers (own and CIS-BP-mapped models): TFAP2A, TFAP2B, TFAP2C, TFAP2D, TFAP2E; best model's site strength: ref 78.9th, alt 99.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G226 (CSD, 1 model): best model LIN28B_FL_TTTGAC40NGGT_KV_yin2017_0_4_7mer (own model of LIN28B), z 23.9, effect 1.4 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: LIN28B z 23.9. TFs this group covers (own and CIS-BP-mapped models): LIN28A, LIN28B; best model's site strength: ref 91.1th, alt 99.8th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G624 (C2H2 ZF, 1 model): best model ZSCAN1_eDBD_TGCTCC40NCCG_KP_yin2017_0_3_7mer (own model of ZSCAN1), z 22.54, effect 1.648 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZSCAN1 z 22.54. TFs this group covers (own and CIS-BP-mapped models): ZSCAN1; best model's site strength: ref 98.4th, alt 99.8th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G005 (HMG/Sox, 18 models): best model SOX2_FL_GT40NGCGTGT_YWEA_jolma2025_0_4_7mer (own model of SOX2), z -22.53, effect -1.646 (alt binds less); 10 passing models (9 with the best model's sign); members disagree on direction. Passing members: SOX2 z -22.53, SOX15 z -15.68, SOX14 z -13.1, SOX7 z -11.77, SRY z -8.47 (+5 more). TFs this group covers (own and CIS-BP-mapped models): SOX1, SOX10, SOX11, SOX12, SOX13, SOX14, SOX15, SOX17, SOX18, SOX2 (+10 more); best model's site strength: ref 99.6th, alt 82.8th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G066 (EBF1, 2 models): best model EBF4_FL_TCGATT40NTTG_KK_nitta2015_1_3_7mer (own model of EBF4), z 17.47, effect 0.682 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: EBF4 z 17.47, EBF1 z 13.33. TFs this group covers (own and CIS-BP-mapped models): EBF1, EBF2, EBF3, EBF4; best model's site strength: ref 99.7th, alt 99.7th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:31:05+00:00)

> No ENCODE TFAP2A ChIP-seq peak contains chr1:209815925:A>G (0 peaks within 100 bp). Absence can also mean no TFAP2A experiment in that biosample.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20IRF6%20enhancer%20AP-2alpha%20binding%20site%20cleft%20lip&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:31:05+00:00)

> Europe PMC: 2 hits for 'rs642961 IRF6 enhancer AP-2alpha binding site cleft lip'; top 2 with PMIDs:
> PMID 26332872 (2016): Toward an orofacial gene regulatory network.
> PMID 18836445 (2008): Disruption of an AP-2alpha binding site in an IRF6 enhancer is associated with cleft lip.

<a id="e19a"></a>**E19a** literature_search, Europe PMC abstract, PMID 26332872 (https://europepmc.org/article/MED/26332872; retrieved 2026-10-25T17:31:05+00:00)

> In addition, a common variant (rs642961) in the IRF6 locus is found in 30% of the world's population and contributes risk for isolated orofacial clefting.

<a id="e19b"></a>**E19b** literature_search, Europe PMC abstract, PMID 26332872 (https://europepmc.org/article/MED/26332872; retrieved 2026-10-25T17:31:05+00:00)

> Biochemical studies revealed that rs642961 abrogates one of four AP-2alpha binding sites.

<a id="e19c"></a>**E19c** literature_search, Europe PMC abstract, PMID 18836445 (https://europepmc.org/article/MED/18836445; retrieved 2026-10-25T17:31:05+00:00)

> Here, we use multispecies sequence comparisons to identify a common SNP (rs642961, G>A) in a newly identified IRF6 enhancer.

<a id="e19d"></a>**E19d** literature_search, Europe PMC abstract, PMID 18836445 (https://europepmc.org/article/MED/18836445; retrieved 2026-10-25T17:31:05+00:00)

> EMSA and ChIP assays demonstrate that the risk allele disrupts the binding site of transcription factor AP-2alpha and expression analysis in the mouse localizes the enhancer activity to craniofacial and limb structures.

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:31:08+00:00)

> Open Targets: IRF6 and cleft lip (EFO_0003959), overall score 0.54; by evidence type: genetic_association 0.72, genetic_literature 0.61, animal_model 0.54, literature 0.35
