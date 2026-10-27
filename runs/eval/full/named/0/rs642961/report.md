# rs642961 and Cleft lip (IRF6)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.64 over 7 model calls; 174 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## QBiC-SELEX screen

222 of 997 models pass the gate. Top groups: Ets, 18 models (best ETV5, z 77.65); Ets, 1 model (best SPDEF, z 42.64); TEA, 4 models (best TEAD1, z -40.19); HSF, 5 models (best HSF5, z -29.76); HSF, 3 models (best HSF1, z -29.65).

## Ranked chains

### 1. H1: Risk allele A weakens an AP-2 (TFAP2A) site in the distal IRF6 enhancer, lowering IRF6 in oral epithelium/periderm (p = 0.35)

TF TFAP2A (stated coverage own_model; registry own_model), alt allele binds more; element Distal enhancer-like cCRE EH38E2863563 (Ensembl enhancer ENSR1_B3JM9C) ~10 kb upstream of IRF6; gene IRF6; cell type Oral epithelium/periderm of the developing lip (asserted from literature, not from data in this case).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A has its own QBiC-SELEX model that passes the gate at this variant with effect +2.176 (z 11.94, rank 41/997; ref 96.3th vs alt 100.0th percentile k-mer strength), so the alt G allele binds AP-2 more and the cleft risk allele A binds less; the whole AP-2 group agrees in direction (TFAP2B z 23.98, TFAP2C, TFAP2E). TFAP2A is chosen within the group from its known craniofacial-ectoderm role, not from data here; no ENCODE ChIP peak supports occupancy, though no relevant biosample may have been assayed | weak | [E18](#e18), [E13](#e13), [E19](#e19), [E07](#e07) |
| element | The variant lies in a distal enhancer-like cCRE (DNase z 5.3, H3K27ac z 5.0, maxima across biosamples) and is annotated as a regulatory_region_variant in an Ensembl enhancer | supported | [E01](#e01), [E03](#e03) |
| gene | IRF6 is 9.7 kb from the element and is a leading L2G gene (up to 0.67; 0.16 in the orofacial cleft set), and the variant is a significant IRF6 eQTL in GTEx brain (NES -0.62); but UTP25/DIEXF has the highest L2G (0.75) and more eQTL tissues, so the IRF6 assignment is not settled, and the brain eQTL direction (alt G lowers IRF6) runs opposite to the AP-2 gain-of-binding prediction | weak | [E02](#e02), [E05](#e05), [E20](#e20) |
| cell_type | No expression context was supplied and no craniofacial epigenome data are cited; the oral epithelium/periderm assignment rests only on prior IRF6 cleft literature, which concerns other SNPs at the locus | missing | [E06a](#e06a) |
| phenotype | The A allele is the orofacial cleft risk allele (p 2e-06, PIP 0.05), and literature states that functional SNPs near IRF6 account for most of the cleft risk at this locus, although rs642961 is not named in the quoted text; a tissue-specific drop in enhancer output is the proposed, not demonstrated, mechanism | weak | [E04](#e04), [E06a](#e06a) |

Predictions: Allelic luciferase/MPRA in oral keratinocytes: A gives lower activity than G; TFAP2A EMSA or ChIP in keratinocytes shows G-biased occupancy; TFAP2A knockdown removes the allelic reporter difference; CRISPRi of EH38E2863563 in oral keratinocytes lowers IRF6 more than UTP25

Falsified if: No AP-2 occupancy at the element in a relevant epithelial cell, or occupancy favouring A; Allelic reporter/MPRA shows no difference or A > G in epithelial cells; Endogenous allelic editing changes UTP25 but not IRF6

### 2. H5: Null: no TF-mediated effect of this variant; the cleft signal comes from a linked functional variant (p = 0.33)

Null chain: no TF-mediated effect of this variant.

Predictions: Allelic reporter/MPRA shows no A vs G difference in oral keratinocytes; No allele-specific TF occupancy at the element in any assayed cell type; Conditional analysis attributes cleft risk to other nearby variants (e.g. the IRF6 promoter SNP rs12403599); Cleft fine-mapping PIP for rs642961 remains low (0.05)

Falsified if: Episomal or endogenous allelic editing changes IRF6 (or UTP25) expression in a relevant cell type; Allele-specific TF occupancy is demonstrated at the element; Cleft fine-mapping assigns high PIP to rs642961

### 3. H6: Same AP-2 binding change, but the regulated gene is UTP25/DIEXF (and TRAF3IP3), not IRF6 (p = 0.12)

TF TFAP2A (stated coverage own_model; registry own_model), alt allele binds more; element Distal enhancer cCRE EH38E2863563, 12.0 kb from the UTP25 TSS; gene UTP25 (DIEXF); cell type Broadly expressed cell types; no craniofacial data available.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Same QBiC-SELEX AP-2 signal as H1: TFAP2A own model effect +2.176, z 11.94, alt G binds more; TFAP2B z 23.98 agrees | weak | [E18](#e18), [E13](#e13) |
| element | Active distal enhancer-like cCRE whose SCREEN-linked genes include UTP25 and C1orf74 as well as IRF6 | supported | [E03](#e03), [E01](#e01) |
| gene | UTP25/DIEXF has the best L2G score across credible sets (0.75) and the most consistent GTEx eQTLs (fibroblasts NES -0.23, artery, blood, lung, adipose), and TRAF3IP3 has four molecular-QTL credible sets and a whole-blood eQTL; the alt G allele lowers DIEXF in most tissues, matching a gain of a repressive or redistributed AP-2 input | supported | [E05](#e05), [E20](#e20), [E02](#e02) |
| cell_type | eQTL effects are seen in fibroblasts, artery, blood and adipose, not in a craniofacial tissue, so the cell type relevant to cleft risk is not identified | weak | [E20](#e20) |
| phenotype | The variant's strongest GWAS signals are blood pressure traits (SBP p 6e-12, effect allele G), consistent with a vascular/fibroblast gene such as DIEXF or TRAF3IP3; under this chain the cleft association at the same SNP is either secondary or driven by a different, linked variant | weak | [E04](#e04), [E05](#e05) |

Predictions: CRISPRi of EH38E2863563 lowers UTP25/DIEXF (and/or TRAF3IP3) more than IRF6; Allelic editing in fibroblasts changes DIEXF expression but not IRF6; Oral-keratinocyte reporter shows little or no allelic difference despite the eQTL

Falsified if: Enhancer perturbation changes IRF6 only; Allele-specific expression in craniofacial epithelium shows IRF6 but not UTP25/DIEXF effects

### 4. H2: Alt allele creates an ETS (ELF3) site absent on the risk allele A, reducing IRF6 enhancer output (p = 0.12)

TF ELF3 (stated coverage own_model; registry own_model), alt allele binds more; element Distal enhancer cCRE EH38E2863563 upstream of IRF6; gene IRF6; cell type Epithelial cells of the developing oral cavity (not demonstrated here).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Ets group G003 passes very strongly with alt binding more (best model ETV5 z 77.65, effect +1.32; ref 65.0th vs alt 99.2th percentile) and a second Ets group led by SPDEF agrees (z 42.64, effect +1.62). ELF3 is listed as having its own model within G003 but its individual z and effect were not retrieved; ELF3 is chosen within the group only because it is the epithelium-restricted ETS factor, not from data in this case | weak | [E08](#e08), [E09](#e09), [E07](#e07) |
| element | The site is a distal enhancer-like cCRE with high DNase and H3K27ac (maxima over biosamples) | supported | [E03](#e03), [E01](#e01) |
| gene | IRF6 is the nearest gene (9.7 kb) and has L2G 0.16 in the orofacial cleft credible set; UTP25 scores higher overall, so the target is uncertain | weak | [E02](#e02), [E05](#e05) |
| cell_type | No expression or chromatin data for ETS factors in craniofacial tissue were provided; the epithelial assignment is unsupported by cited evidence | missing | none |
| phenotype | If the ETS input is activating, its loss on the A allele would lower IRF6 and raise cleft risk; only the A-allele cleft association is cited evidence | weak | [E04](#e04) |

Predictions: ELF3 or SPDEF ChIP shows G-biased occupancy at the element; Mutating the ETS core abolishes the allelic reporter difference while an AP-2 core mutation does not; ELF3 knockdown in oral keratinocytes selectively reduces G-allele activity

Falsified if: No ETS factor occupies the element in epithelial cells; ETS core mutation leaves the allelic difference intact; qbic_tf_detail for ELF3 shows no passing model or the opposite direction

### 5. H3: Risk allele A retains a strong TEAD site lost on G; TEAD input sets enhancer activity at IRF6 (p = 0.08)

TF TEAD1 (stated coverage own_model; registry own_model), ref allele binds more; element Distal enhancer cCRE EH38E2863563 upstream of IRF6; gene IRF6; cell type Craniofacial epithelium (not supported by data here).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The TEA group loses binding on alt (TEAD1 own model z -40.19, effect -2.547; ref 99.4th vs alt 75.7th percentile), so the risk allele A binds TEAD more; TEAD1 is chosen as the strongest of four covered paralogues, with no expression data to pick among them | weak | [E10](#e10), [E07](#e07) |
| element | The variant lies in an active distal enhancer-like cCRE | supported | [E03](#e03), [E01](#e01) |
| gene | IRF6 is 9.7 kb away with moderate L2G support, but UTP25 has the higher L2G score | weak | [E02](#e02), [E05](#e05) |
| cell_type | No evidence in this case bears on TEAD/YAP activity in craniofacial tissue | missing | none |
| phenotype | Only the A-allele cleft association is cited; whether more TEAD binding raises or lowers IRF6 is not established, so the direction of this chain is incomplete | weak | [E04](#e04) |

Predictions: TEAD1 EMSA/ChIP shows A-biased binding at the element; TEAD or YAP/TAZ perturbation changes the size of the allelic reporter difference; Allelic difference persists after TFAP2A depletion

Falsified if: No TEAD occupancy at the element; Allelic reporter difference unchanged by TEAD perturbation; EMSA shows G-biased binding

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H6 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allelic luciferase/MPRA of EH38E2863563 (A vs G) in oral keratinocytes | low | yes | G > A activity | No difference | Little or no difference in keratinocytes | G > A activity | Difference present, direction uncertain |
| TFAP2A EMSA/ChIP allele-specific occupancy at the element in keratinocytes | medium | yes | G-biased AP-2 occupancy | No allele-specific occupancy | G-biased AP-2 occupancy (but in fibroblasts) | No or weak AP-2 occupancy | No AP-2 bias; TEAD binds A |
| Existing ENCODE TFAP2A ChIP-seq peak overlap (E19) | existing data | no | No peak; uninformative because craniofacial biosamples may be absent | No peak, consistent | No peak; uninformative | No peak expected | No peak expected |
| CRISPRi of the enhancer with RT-qPCR of IRF6, UTP25/DIEXF, TRAF3IP3 | medium | no | IRF6 down | Enhancer may act but no allelic effect; gene changes without allele dependence | UTP25/DIEXF or TRAF3IP3 down, IRF6 unchanged | IRF6 down | IRF6 changed |
| qbic_tf_detail lookup of ELF3 (own model z, effect sign) | existing data | no | Irrelevant to AP-2 call | Any in vitro result remains non-functional | Irrelevant | ELF3 model passes with alt binding more | Irrelevant |
| Motif-core mutagenesis in reporter (AP-2 core vs ETS core vs TEAD core) | medium | yes | AP-2 core mutation abolishes allelic difference | No allelic difference to abolish | AP-2 core matters only in fibroblasts | ETS core mutation abolishes it | TEAD core mutation abolishes it |

## Next experiment

A low-cost allele-specific luciferase/MPRA test of the 350 bp cCRE EH38E2863563 (A vs G) in oral keratinocytes (e.g. HaCaT or primary oral epithelium): a reproducible G > A activity difference supports H1 over the null H5, while no difference supports the null.

## Investigate calls

- qbic_tf_detail({"tf": "TFAP2A"})
- chip_peaks({"tf": "TFAP2A", "biosample": null})
- eqtl_lookup({"tissue": null})

## Flags

- none

Citation support: 0.90 of links cite only evidence that passed every check.

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

> QBiC-SELEX screen of chr1:209815925:A>G: 997 models scored, 222 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 140 CIS-BP groups. Expression context: none: expression filter skipped. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 0. Passing groups ranked below the ones shown: 130. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (own model of ETV5), z 77.65, effect 1.32 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: ETV5 z 77.65, ETS2 z 47.72, ETV2 z 31.41, ETV4 z 30.23, ETS1 z 27.66 (+13 more). TFs this group covers: EHF (mapped), ELF1 (own model), ELF2 (own model), ELF3 (own model), ELF4 (own model), ELF5 (own model), ELK1 (own model), ELK3 (own model), ELK4 (own model), ERF (own model) (+15 more); best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G345 (Ets, 1 model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (own model of SPDEF), z 42.64, effect 1.62 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: SPDEF z 42.64. TFs this group covers: ELF1 (own model), ELF2 (own model), ELF4 (own model), SPDEF (own model); best model's site strength: ref 89.2th, alt 99.8th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G031 (TEA, 4 models): best model TEAD1_FL_TCACGC40NACT_KW_yin2017_0_4_7mer (own model of TEAD1), z -40.19, effect -2.547 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TEAD1 z -40.19, TEAD2 z -39.78, TEAD3 z -32.45, TEAD4 z -26.55. TFs this group covers: TEAD1 (own model), TEAD2 (own model), TEAD3 (own model), TEAD4 (own model); best model's site strength: ref 99.4th, alt 75.7th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G014 (HSF, 5 models): best model HSF5_eDBD_TATGCT40NACT_KT_yin2017_0_3_7mer (own model of HSF5), z -29.76, effect -0.875 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: HSF5 z -29.76, HSFY2 z -12.29. TFs this group covers: HSF5 (own model), HSFX1 (own model), HSFX2 (own model), HSFY1 (own model), HSFY2 (own model); best model's site strength: ref 99.4th, alt 92.8th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G039 (HSF, 3 models): best model HSF1_eDBD_TCTAAA40NCGC_KN_yin2017_0_4_7mer (own model of HSF1), z -29.65, effect -1.427 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: HSF1 z -29.65, HSF4 z -26.38, HSF2 z -25.12. TFs this group covers: HSF1 (own model), HSF2 (own model), HSF4 (own model); best model's site strength: ref 100.0th, alt 90.6th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G030 (AP-2, 4 models): best model TFAP2B_FL_TGTCCG20NGA_KH_nitta2015_1_3_7mer (own model of TFAP2B), z 23.98, effect 1.688 (alt binds more); 4 passing models (4 with the best model's sign). Passing members: TFAP2B z 23.98, TFAP2C z 17.39, TFAP2E z 13.97, TFAP2A z 11.94. TFs this group covers: TFAP2A (own model), TFAP2B (own model), TFAP2C (own model), TFAP2D (mapped), TFAP2E (own model); best model's site strength: ref 78.9th, alt 99.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G226 (CSD, 1 model): best model LIN28B_FL_TTTGAC40NGGT_KV_yin2017_0_4_7mer (own model of LIN28B), z 23.9, effect 1.4 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: LIN28B z 23.9. TFs this group covers: LIN28A (mapped), LIN28B (own model); best model's site strength: ref 91.1th, alt 99.8th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G624 (C2H2 ZF, 1 model): best model ZSCAN1_eDBD_TGCTCC40NCCG_KP_yin2017_0_3_7mer (own model of ZSCAN1), z 22.54, effect 1.648 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZSCAN1 z 22.54. TFs this group covers: ZSCAN1 (own model); best model's site strength: ref 98.4th, alt 99.8th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G005 (HMG/Sox, 18 models): best model SOX2_FL_GT40NGCGTGT_YWEA_jolma2025_0_4_7mer (own model of SOX2), z -22.53, effect -1.646 (alt binds less); 10 passing models (9 with the best model's sign); members disagree on direction. Passing members: SOX2 z -22.53, SOX15 z -15.68, SOX14 z -13.1, SOX7 z -11.77, SRY z -8.47 (+5 more). TFs this group covers: SOX1 (own model), SOX10 (own model), SOX11 (own model), SOX12 (own model), SOX13 (mapped), SOX14 (own model), SOX15 (own model), SOX17 (own model), SOX18 (own model), SOX2 (own model) (+10 more); best model's site strength: ref 99.6th, alt 82.8th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G066 (EBF1, 2 models): best model EBF4_FL_TCGATT40NTTG_KK_nitta2015_1_3_7mer (own model of EBF4), z 17.47, effect 0.682 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: EBF4 z 17.47, EBF1 z 13.33. TFs this group covers: EBF1 (own model), EBF2 (mapped), EBF3 (mapped), EBF4 (own model); best model's site strength: ref 99.7th, alt 99.7th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TFAP2A","symbol":"TFAP2A","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr1:209815925:A>G","gate_p":5.02e-05,"models":[{"model":"TCFAP2A_NA_TGATCC20NCG_ESP_yang2017_0_4_7mer","mapping":"own","group":"G030 AP-2, 4 models","quality":0.927,"effect":2.176,"z":11.94,"p":7.3e-33,"rank_abs_z":"41/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":100.0,"k":7}},{"model":"TFAP2B_FL_TGTCCG20NGA_KH_nitta2015_1_3_7mer","mapping":"CIS-BP (TFAP2B)","group":"G030 AP-2, 4 models","quality":0.77,"effect":1.688,"z":23.98,"p":4.3e-127,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":78.9,"alt_percentile":99.9,"k":7}},{"model":"TFAP2C_eDBD_TGAGCT40NGCA_KP_yin2017_0_4_7mer","mapping":"CIS-BP (TFAP2C)","group":"G030 AP-2, 4 models","quality":0.753,"effect":1.495,"z":17.39,"p":1.1e-67,"rank_abs_z":"22/997","passed_gate":true,"site_strength":{"ref_percentile":86.2,"alt_percentile":91.7,"k":7}},{"model":"TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer","mapping":"CIS-BP (TFAP2E)","group":"G030 AP-2, 4 models","quality":0.88,"effect":0.819,"z":13.97,"p":2.4e-44,"rank_abs_z":"33/997","passed_gate":true,"site_strength":{"ref_percentile":89.1,"alt_percentile":89.6,"k":7}}]}

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:31:05+00:00)

> No ENCODE TFAP2A ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no TFAP2A experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_209815925_A_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T22:31:38+00:00)

> 15 significant GTEx v8 single-tissue eQTLs for chr1_209815925_A_G_b38. NES is the effect of the alt allele (G) relative to ref (A).
> SYT14 in Nerve_Tibial: NES -0.50, p 6.7e-20
> DIEXF in Cells_Cultured_fibroblasts: NES -0.23, p 1.9e-14
> DIEXF in Artery_Tibial: NES -0.23, p 1.2e-10
> TRAF3IP3 in Whole_Blood: NES +0.24, p 5.9e-10
> IRF6 in Brain_Cerebellum: NES -0.62, p 2.2e-07
> DIEXF in Whole_Blood: NES -0.15, p 2.9e-07
> SYT14 in Brain_Hippocampus: NES +0.53, p 3.3e-07
> DIEXF in Adipose_Subcutaneous: NES -0.20, p 7.5e-07
> SYT14 in Brain_Spinal_cord_cervical_c-1: NES +0.72, p 2.7e-06
> DIEXF in Lung: NES -0.11, p 3.2e-06
> IRF6 in Brain_Cerebellar_Hemisphere: NES -0.61, p 3.3e-06
> DIEXF in Brain_Frontal_Cortex_BA9: NES +0.35, p 4.6e-06
> DIEXF in Brain_Cortex: NES +0.33, p 7.0e-06
> DIEXF in Adipose_Visceral_Omentum: NES -0.16, p 2.5e-05
> C1orf74 in Whole_Blood: NES +0.15, p 8.6e-05
