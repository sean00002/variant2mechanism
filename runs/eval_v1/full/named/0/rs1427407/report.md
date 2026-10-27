# rs1427407 and Fetal haemoglobin level, sickle cell severity (BCL11A)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.70 over 8 model calls; 272 s.

Variant `chr2:60490908:T>G` (germline); expression context: DepMap:ACH-000551 (K-562, erythroleukaemia; proxy for erythroid precursors).

## QBiC-SELEX screen

478 of 997 models pass the gate. Top groups: Ets, 4 models (best ETV7, z -45.38); C2H2 ZF, 1 model (best ZNF493, z 42.63); Rel, 1 model (best RELA, z -31.14); Rel, 2 models (best NFKB2, z -28.76); Rel, 4 models (best NFATC4, z -25.86).

## Ranked chains

### 1. H6: Alt G disrupts a GATA half-site/composite motif in the BCL11A erythroid enhancer (DHS +62), reducing GATA1 binding, lowering BCL11A and raising HbF (p = 0.38)

TF GATA1 (stated coverage not_checked; registry own_model), ref allele binds more; element BCL11A intron-2 erythroid enhancer, cCRE EH38E2001346 (chr2:60490828-60491157); gene BCL11A; cell type erythroid precursors (K-562 proxy, DepMap ACH-000551).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Fine-mapping of this BCL11A enhancer identified a motif-disrupting common variant with reduced TF binding, modestly lower BCL11A and higher HbF; ENCODE K562 GATA1 ChIP shows 2 peaks within 100 bp of the variant although none contains the exact base, consistent with a GATA-occupied region whose motif is weakened by the G allele. GATA1 was not among the QBiC-SELEX groups reported here, so no in vitro allelic score is cited for it | weak | [E20b](#e20b), [E19](#e19), [E20](#e20) |
| element | The variant lies in a distal enhancer-like cCRE (DNase z 5.1, H3K27ac z 3.4; biosample maxima) that the literature describes as the essential erythroid enhancer of BCL11A containing the GWAS SNPs | supported | [E03](#e03), [E20a](#e20a), [E20d](#e20d) |
| gene | The element is intronic to BCL11A, 63.6 kb from its TSS; credible sets containing this variant have PIP 1.00 with best L2G for BCL11A 0.89, and genome engineering showed the enhancer is required for BCL11A expression | supported | [E02](#e02), [E05](#e05), [E20d](#e20d) |
| cell_type | The enhancer is required in erythroid but not B-lymphoid cells, and the variant's associations are erythroid (MCH, RBC count, reticulocyte volume, HbF/F-cells) | supported | [E20c](#e20c), [E05](#e05), [E04](#e04) |
| phenotype | BCL11A is the repressor of gamma-globin; modestly reduced enhancer output lowers BCL11A and raises HbF, consistent with G being the HbF-raising effect allele and with milder sickle cell disease | weak | [E20e](#e20e), [E04](#e04), [E06a](#e06a) |

Predictions: Allele-specific GATA1 (and TAL1) ChIP in heterozygous erythroid cells shows T-biased occupancy at chr2:60490908; Single-base editing of T>G in HUDEP-2/CD34+ erythroid cells modestly lowers BCL11A and raises HBG1/2 without a myeloid or B-cell effect; Allelic MPRA of this enhancer fragment gives lower activity for G in erythroid but not lymphoid cells

Falsified if: Allele-specific GATA1/TAL1 ChIP shows no imbalance at this base; Isolated base editing of rs1427407 leaves BCL11A and HBG unchanged while a linked +58 edit does; No GATA motif sequence is present at or adjacent to the variant

### 2. H5: Null: rs1427407 has no TF-mediated effect of its own and tags a linked causal site in the same enhancer (e.g. the +58 GATA1 motif) (p = 0.27)

Null chain: no TF-mediated effect of this variant.

Predictions: Isolated base editing or allelic MPRA of rs1427407 gives little or no change in BCL11A/HBG, while editing the linked +58 GATA1 motif does; No allele-specific TF footprint or ChIP imbalance at chr2:60490908 in erythroid cells; Haplotypes carrying G but not the linked causal allele show normal HbF

Falsified if: Single-base editing of T>G alone changes BCL11A or HBG expression in erythroid cells; Allele-specific ChIP or footprinting shows clear imbalance at this exact base; Allelic MPRA shows enhancer activity difference for this variant alone

### 3. H1: Alt G weakens an ETS site in the BCL11A enhancer, lowering BCL11A and de-repressing HBG (p = 0.15)

TF ELF1 (stated coverage own_model; registry own_model), ref allele binds more; element BCL11A intron-2 enhancer cCRE EH38E2001346; gene BCL11A; cell type erythroid precursors (K-562 proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Many ETS models lose binding with G (G003 best model ETV3 z -22.74, ref 99.7th vs alt 87.2th percentile; ELF1 is a passing member, z -11.29, own model). ELF1 was chosen within the group on expression (32.2 TPM) rather than on a variant-specific ELF1 effect size, which is not given; ENCODE K562 ChIP shows no ELF1 peak at the variant, which weakens this chain | weak | [E16](#e16), [E18](#e18), [E07](#e07) |
| element | The variant lies in a distal enhancer-like cCRE with strong accessibility (biosample maxima, not erythroid-specific) | weak | [E03](#e03), [E01](#e01) |
| gene | The element is in BCL11A intron 2 and credible sets at this variant map to BCL11A (PIP 1.00, best L2G 0.89) | supported | [E02](#e02), [E05](#e05) |
| cell_type | The associated traits are erythroid red-cell indices and HbF; ETS factors are expressed in the K-562 proxy | weak | [E04](#e04), [E05](#e05), [E16](#e16) |
| phenotype | Reduced enhancer output lowers BCL11A and raises HbF, consistent with G as the HbF-raising allele | weak | [E04](#e04), [E06a](#e06a), [E20e](#e20e) |

Predictions: An ETS-family ChIP (ELF1/GABPA/ELF2) in erythroid cells shows a peak at the variant with T-allele bias; ETS core mutation at this exact base reduces enhancer reporter activity independently of any GATA motif; ETS factor knockdown shrinks the allelic BCL11A difference

Falsified if: No ETS footprint or ChIP peak overlaps the variant in erythroid cells (E18 already argues against ELF1); Allele-specific ETS ChIP shows equal or G-biased occupancy; Mutating the ETS core does not change enhancer activity

### 4. H2: Alt G creates a ZNF493 (KRAB-ZF) site that represses the BCL11A enhancer (p = 0.10)

TF ZNF493 (stated coverage own_model; registry own_model), alt allele binds more; element BCL11A intron-2 enhancer cCRE EH38E2001346; gene BCL11A; cell type erythroid precursors (K-562 proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | A single own 7-mer model of ZNF493 gains binding on G (z 42.63, effect 0.701, ref 86.1th to alt 100.0th percentile); this is an in vitro prediction from one model only, with no ChIP or allelic data | weak | [E09](#e09) |
| element | The gained site lies in a distal enhancer-like cCRE (z-scores are maxima across biosamples) | weak | [E03](#e03) |
| gene | The enhancer is intronic to BCL11A and credible sets assign the signal to BCL11A | supported | [E02](#e02), [E05](#e05) |
| cell_type | ZNF493 is expressed in the erythroid proxy line (17.9 TPM); no erythroid role is documented | weak | [E09](#e09), [E07](#e07) |
| phenotype | If a gained repressor lowers enhancer output, BCL11A falls and HbF rises, matching G as the HbF-raising allele; no evidence links ZNF493 to BCL11A or HbF | weak | [E04](#e04), [E06a](#e06a) |

Predictions: ZNF493 ChIP-exo in erythroid cells shows a G-allele-specific peak at this site; Local TRIM28/H3K9me3 gain on the G allele; ZNF493 knockdown abolishes the allelic BCL11A difference

Falsified if: No ZNF493 binding at the locus in erythroid cells; ZNF493 knockdown leaves the allelic BCL11A difference intact; The allelic effect is reproduced in cells not expressing ZNF493

### 5. H4: Alt G weakens an NF-kB (RELA/NFKB2) site, reducing enhancer activity and BCL11A (p = 0.10)

TF RELA (stated coverage own_model; registry own_model), ref allele binds more; element BCL11A intron-2 enhancer cCRE EH38E2001346; gene BCL11A; cell type erythroid precursors (K-562 proxy).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | RELA's own model loses binding with G (z -31.14, effect -1.256; ref 99.8th to alt 98.8th percentile, a small percentile drop, so weakening not abolition); NFKB2 shows a larger per-model effect (-1.964) but RELA is the best expressed Rel member (38.58 TPM vs NFKB2 17.6, REL 3.58, RELB 1.47), which is why RELA is named | weak | [E10](#e10), [E11](#e11) |
| element | The site is in a distal enhancer-like cCRE with high DNase signal (biosample maxima) | weak | [E03](#e03) |
| gene | The enhancer is intronic to BCL11A; credible sets favour BCL11A over the distant REL/PAPOLG (>265 kb) | supported | [E02](#e02), [E05](#e05) |
| cell_type | RELA is abundantly expressed in the erythroid proxy line; NF-kB activity in erythroid precursors is not shown | weak | [E10](#e10) |
| phenotype | Reduced BCL11A raises HbF and lessens sickle severity, consistent with G as the HbF-raising allele | weak | [E04](#e04), [E06a](#e06a), [E20e](#e20e) |

Predictions: RELA ChIP shows T-biased occupancy at the variant in erythroid cells; NF-kB pathway stimulation or IKK inhibition changes BCL11A in an allele-dependent way; Mutating the kB half-site lowers enhancer reporter activity

Falsified if: No RELA ChIP peak at this enhancer in erythroid cells; NF-kB perturbation does not alter BCL11A; kB-site mutation leaves enhancer activity unchanged

## Prediction matrix

| Test | Cost | Separates top two | H6 | H5 | H1 | H2 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reanalyse existing ENCODE/published GATA1 and TAL1 ChIP-seq in heterozygous erythroid cells for allelic imbalance at chr2:60490908 | existing data | yes | T-biased GATA1/TAL1 reads at the variant base | No allelic imbalance at this base (imbalance instead at a linked site) | No GATA imbalance required; prediction is neutral/absent | No GATA imbalance; possible G-biased repressive marks instead | No GATA imbalance |
| ELF1/GABPA ChIP-seq peak overlap and allelic bias at the variant in K562 or erythroid progenitors | existing data | no | No ETS peak needed; GATA-centred occupancy | No allelic ETS signal | ETS peak over the variant with T bias (E18 already shows no ELF1 peak in K562) | No ETS peak | No ETS peak |
| Single-base editing of T>G at rs1427407 alone in HUDEP-2/CD34+ erythroid cells, measuring BCL11A and HBG1/2 | high | yes | Modest BCL11A decrease and HBG increase | No change; change only when the linked +58 motif is edited | BCL11A decrease (mechanism indistinguishable without TF perturbation) | BCL11A decrease, dependent on ZNF493 | BCL11A decrease, dependent on NF-kB |
| Allelic MPRA of the enhancer fragment in erythroid vs lymphoid cells, with motif-swap variants (GATA, ETS, kB cores) | medium | yes | Lower G activity in erythroid only; abolished by GATA-core mutation | No allelic difference for this fragment | Allelic difference abolished by ETS-core mutation | G fragment lower, unaffected by GATA/ETS core mutation | Allelic difference abolished by kB-core mutation |
| siRNA/degron knockdown of ZNF493, RELA or ETS factors in heterozygous erythroid cells, measuring allele-specific BCL11A | medium | no | Allelic difference persists after all three knockdowns | No allelic difference to begin with | ETS knockdown removes the allelic difference | ZNF493 knockdown removes the allelic difference | RELA knockdown removes the allelic difference |

## Next experiment

Reanalyse existing GATA1/TAL1 ChIP-seq from heterozygous erythroid cells (and the 2 K562 GATA1 peaks within 100 bp noted in E19) for allele-specific reads at chr2:60490908: T-biased occupancy supports H6, no imbalance supports the tagging null H5, and the data already exist.

## Investigate calls

- chip_peaks({"tf": "ELF1", "biosample": "K562"})
- chip_peaks({"tf": "GATA1", "biosample": "K562"})
- literature_search({"query": "rs1427407 BCL11A enhancer DHS +62 allele-specific GATA1 fetal hemoglobin"})

## Flags

- coverage_misstated: H6: stated not_checked, registry says own_model for GATA1

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/2:60490908-60490908:1/G?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:29:32+00:00)

> Variant chr2:60490908:T>G (GRCh38), allele string T/G
> Known IDs: rs1427407
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 1.67
> Transcript consequences: BCL11A (intron_variant); BCL11A (intron_variant, non_coding_transcript_variant); BCL11A (intron_variant, NMD_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/2:59490908-61490908?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T18:05:11+00:00)

> 9 protein-coding genes within 1000 kb of chr2:60490908:T>G, by distance to TSS:
> BCL11A: 63.6 kb from TSS (in gene body, strand -1)
> PAPOLG: 265.3 kb from TSS (upstream, strand +1)
> REL: 390.6 kb from TSS (upstream, strand +1)
> PEX13: 526.1 kb from TSS (upstream, strand +1)
> PUS10: 527.4 kb from TSS (downstream, strand -1)
> SANBR: 575.0 kb from TSS (upstream, strand +1)
> C2orf74: 654.2 kb from TSS (upstream, strand +1)
> USP34: 980.2 kb from TSS (downstream, strand -1)
> XPO1: 1047.8 kb from TSS (downstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:29:10+00:00)

> The variant lies in cCRE EH38E2001346 (dELS: distal enhancer-like), chr2:60490828-60491157.
> SCREEN: 2 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2001346 dELS (contains the variant): DNase z 5.1, H3K27ac z 3.4, H3K4me3 z 1.9, CTCF z 1.3; nearby genes AC009970.1, BCL11A, AC007381.1
> EH38E3346277 dELS: DNase z 2.4, H3K27ac z 3.3, H3K4me3 z 2.0, CTCF z 1.7; nearby genes AC009970.1, BCL11A, AC007381.1
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs1427407&size=100; retrieved 2026-10-25T17:29:35+00:00)

> 25 GWAS Catalog associations for rs1427407, strongest first:
> KEL protein levels: p 7.0e-93, effect allele G, risk-allele frequency 0.84607813, PMID 39789286
> HEPACAM2 protein levels: p 5.0e-55, effect allele G, risk-allele frequency 0.84607813, PMID 39789286
> Fetal hemoglobin levels in sickle cell anemia: p 4.0e-53, effect allele ?, risk-allele frequency 0.78, PMID 25372704
> Pyruvate levels: p 2.0e-51, effect allele G, risk-allele frequency NR, PMID 41044249
> GALNT5 protein levels: p 6.0e-36, effect allele G, risk-allele frequency 0.84607813, PMID 39789286
> ALDH1A1/PKLR protein level ratio: p 2.0e-33, effect allele ?, risk-allele frequency NR, PMID 38412862
> GCHFR protein levels: p 1.0e-32, effect allele G, risk-allele frequency 0.84607813, PMID 39789286
> F-cell distribution: p 6.0e-31, effect allele ?, risk-allele frequency 0.14, PMID 17767159
> BLVRB/PKLR protein level ratio: p 7.0e-27, effect allele ?, risk-allele frequency NR, PMID 38412862
> Fetal hemoglobin in Sickle cell disease (HbSS or HbSB0) (transfusion-adjusted): p 2.0e-25, effect allele G, risk-allele frequency NR, PMID 34283174
> PKLR/PSMD9 protein level ratio: p 5.0e-23, effect allele ?, risk-allele frequency NR, PMID 38412862
> DNPH1/PKLR protein level ratio: p 2.0e-20, effect allele ?, risk-allele frequency NR, PMID 38412862

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:32+00:00)

> 47 credible sets contain 2_60490908_T_G: 39 GWAS, 8 molecular QTL.
> GWAS Mean sphered cell volume (UKB data field 30270): PIP 1.00; L2G BCL11A 0.64
> GWAS Mean corpuscular haemoglobin (UKB data field 30050): PIP 1.00; L2G BCL11A 0.71
> GWAS Red blood cell (erythrocyte) count (UKB data field 30010): PIP 1.00; L2G BCL11A 0.71
> GWAS Red blood cell count: PIP 1.00; L2G BCL11A 0.71
> GWAS Mean reticulocyte volume (UKB data field 30260): PIP 1.00; L2G BCL11A 0.71
> GWAS Fetal hemoglobin levels in sickle cell anemia: PIP 1.00; L2G BCL11A 0.70
> pqtl for HBZ (UKB_PPP_EUR_HBZ_P02008_OID30307_v1): PIP 1.00
> pqtl for KEL (UKB_PPP_EUR_KEL_P23276_OID20881_v1): PIP 1.00
> pqtl for CTSE (UKB_PPP_EUR_CTSE_P14091_OID30628_v1): PIP 1.00
> pqtl for GCHFR (UKB_PPP_EUR_GCHFR_P30047_OID30631_v1): PIP 1.00
> pqtl for HEPACAM2 (UKB_PPP_EUR_HEPACAM2_A8MVW5_OID31151_v1): PIP 1.00
> pqtl for GALNT5 (UKB_PPP_EUR_GALNT5_Q7Z7M9_OID30295_v1): PIP 0.95
> Best L2G gene scores across these sets: BCL11A 0.89

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1427407%20AND%20BCL11A%20AND%20%28%22fetal%20haemoglobin%20level%22%20OR%20%22sickle%20cell%20severity%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:39+00:00)

> Europe PMC: 6 hits for 'rs1427407 AND BCL11A AND ("fetal haemoglobin level" OR "sickle cell severity")'; top 4 with PMIDs:
> PMID 40025045 (2025): FLT1 and other candidate fetal haemoglobin modifying loci in sickle cell disease in African ancestries.
> PMID 32563256 (2020): High fetal hemoglobin level is associated with increased risk of cerebral vasculopathy in children with sickle cell disease in Mayotte.
> PMID 26375006 (2015): BCL11A enhancer dissection by Cas9-mediated in situ saturating mutagenesis.
> PMID 22641398 (2012): Genetic modifiers of sickle cell disease.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 32563256 (https://europepmc.org/article/MED/32563256; retrieved 2026-10-25T17:29:39+00:00)

> The Single Nucleotide Polymorphisms BCL11A rs4671393, BCL11A rs11886868, BCL11A rs1427407 and HMIP rs9399137 were associated with the group of children with HbF > 10%.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr2:60490908:T>G: 997 models scored, 478 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 322 CIS-BP groups. Expression context: DepMap line ACH-000551. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 84 (C2H2 ZF, 1 model z -35.32, Homeodomain, 1 model z -27.11, bHLH, 3 models z 22.18, Homeodomain, 3 models z -17.78, EBF1, 2 models z -16.89). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G020 (Ets, 4 models): best model ETV7_FL_TTAAGC40NAGT_KAE_yin2017_0_2_7mer (own model of ETV7), z -45.38, effect -0.511 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: ETV7 z -45.38, ELF3 z -17.65, ETV6 z -15.86, ELF5 z -7.71. TFs this group covers (own and CIS-BP-mapped models): ELF2 36.53 TPM, ELF1 32.2 TPM, ERF 24.63 TPM, ELF4 24.13 TPM, SPI1 23.05 TPM, ETV6 2.49 TPM, ELF3 1.49 TPM, EHF 0.76 TPM, ETV7 0.13 TPM, ELF5 0.01 TPM (+1 more); best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G521 (C2H2 ZF, 1 model): best model ZNF493_FL_TG40NTCTTGC_YWRA_jolma2025_0_2_7mer (own model of ZNF493), z 42.63, effect 0.701 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF493 z 42.63. TFs this group covers (own and CIS-BP-mapped models): ZNF493 17.91 TPM; best model's site strength: ref 86.1th, alt 100.0th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G315 (Rel, 1 model): best model RELA_DBD_TGATCC20NCTA_KI_nitta2015_1_3_7mer (own model of RELA), z -31.14, effect -1.256 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: RELA z -31.14. TFs this group covers (own and CIS-BP-mapped models): RELA 38.58 TPM, REL 3.58 TPM, RELB 1.47 TPM; best model's site strength: ref 99.8th, alt 98.8th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G088 (Rel, 2 models): best model NFKB2_eDBD_TCCCAA40NGAA_KS_yin2017_0_4_7mer (own model of NFKB2), z -28.76, effect -1.964 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: NFKB2 z -28.76, NFKB1 z -22.54. TFs this group covers (own and CIS-BP-mapped models): NFKB2 17.6 TPM, NFKB1 8.78 TPM, RELB 1.47 TPM; best model's site strength: ref 100.0th, alt 98.9th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G026 (Rel, 4 models): best model NFATC4_eDBD_TAGGTA40NGAT_KAN_yin2017_0_4_7mer (own model of NFATC4), z -25.86, effect -0.988 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: NFATC4 z -25.86, NFATC2 z -16.98, NFATC3 z -11.63. TFs this group covers (own and CIS-BP-mapped models): NFATC3 26.12 TPM, NFATC1 6.25 TPM, NFATC2 5.4 TPM, NFATC4 2.91 TPM; best model's site strength: ref 97.5th, alt 94.1th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G261 (Rel, 1 model): best model NFAT5_eDBD_TCGCAA40NTGT_KS_yin2017_0_4_7mer (own model of NFAT5), z -24.62, effect -0.955 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: NFAT5 z -24.62. TFs this group covers (own and CIS-BP-mapped models): NFAT5 10.83 TPM; best model's site strength: ref 99.2th, alt 75.8th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G031 (TEA, 4 models): best model TEAD1_FL_TCACGC40NACT_KW_yin2017_0_4_7mer (own model of TEAD1), z -24.43, effect -1.908 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: TEAD1 z -24.43, TEAD4 z -16.51, TEAD3 z -15.38, TEAD2 z -5.43. TFs this group covers (own and CIS-BP-mapped models): TEAD1 11.07 TPM, TEAD4 10.18 TPM, TEAD2 8.01 TPM, TEAD3 6.91 TPM; best model's site strength: ref 96.9th, alt 80.4th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G007 (Forkhead, 10 models): best model FOXL1_NA_TGCTCG20NCTC_ESW_yang2017_0_2_7mer (own model of FOXL1), z -23.39, effect -0.762 (alt binds less); 9 passing models (9 with the best model's sign). Passing members: FOXL1 z -23.39, FOXD3 z -22.59, FOXC1 z -19.62, FOXG1 z -17.58, FOXD2 z -16.09 (+4 more). TFs this group covers (own and CIS-BP-mapped models): FOXK2 35.89 TPM, FOXJ3 22.23 TPM, FOXP4 15.81 TPM, FOXK1 10.42 TPM, FOXP1 8.58 TPM, FOXL2 6.04 TPM, FOXJ2 4.98 TPM, FOXG1 2.57 TPM, FOXD3 1.77 TPM, FOXD2 0.67 TPM (+18 more); best model's site strength: ref 99.6th, alt 98.0th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G003 (Ets, 18 models): best model ETV3_NA_TCAGGA20NCG_ESW_yang2017_1_4_7mer (own model of ETV3), z -22.74, effect -0.678 (alt binds less); 13 passing models (13 with the best model's sign). Passing members: ETV3 z -22.74, ERF z -19.06, FEV z -12.14, ETV5 z -12.08, ELF1 z -11.29 (+8 more). TFs this group covers (own and CIS-BP-mapped models): ETV4 38.29 TPM, ELF2 36.53 TPM, ELF1 32.2 TPM, ELK1 29.64 TPM, ERF 24.63 TPM, ELF4 24.13 TPM, ETV1 21.16 TPM, ETV5 18.39 TPM, GABPA 18.17 TPM, ETS2 16.8 TPM (+15 more); best model's site strength: ref 99.7th, alt 87.2th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G049 (Ets, 3 models): best model SPIB_eDBD_TACGAT40NCCG_KR_yin2017_0_3_7mer (own model of SPIB), z 21.04, effect 0.975 (alt binds more); 3 passing models (1 with the best model's sign); members disagree on direction. Passing members: SPIB z 21.04, SPI1 z -14.11, SPIC z -7.99. TFs this group covers (own and CIS-BP-mapped models): SPI1 23.05 TPM, SPIB 0.57 TPM, ETV7 0.13 TPM, ELF5 0.01 TPM, SPIC 0.0 TPM; best model's site strength: ref 97.2th, alt 99.1th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T18:06:51+00:00)

> No ENCODE ELF1 ChIP-seq peak contains chr2:60490908:T>G in biosamples matching 'K562' (0 peaks within 100 bp). Absence can also mean no ELF1 experiment in that biosample.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:31:23+00:00)

> No ENCODE GATA1 ChIP-seq peak contains chr2:60490908:T>G in biosamples matching 'K562' (2 peaks within 100 bp). Absence can also mean no GATA1 experiment in that biosample.

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs1427407%20BCL11A%20enhancer%20DHS%20%2B62%20allele-specific%20GATA1%20fetal%20hemoglobin&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T18:06:52+00:00)

> Europe PMC: 8 hits for 'rs1427407 BCL11A enhancer DHS +62 allele-specific GATA1 fetal hemoglobin'; top 7 with PMIDs:
> PMID 32534791 (2020): In The Blood: Connecting Variant to Function In Human Hematopoiesis.
> PMID 33691767 (2021): Editing GWAS: experimental approaches to dissect and exploit disease-associated genetic variation.
> PMID 27340226 (2016): Hemoglobin genetics: recent contributions of GWAS and gene editing.
> PMID 24115442 (2013): An erythroid enhancer of BCL11A subject to genetic variation determines fetal hemoglobin level.
> PMID 28212192 (2017): Genetic control of erythropoiesis.
> PMID 26375765 (2015): Hemoglobin switching's surprise: the versatile transcription factor BCL11A is a master repressor of fetal hemoglobin.
> PMID 26375006 (2015): BCL11A enhancer dissection by Cas9-mediated in situ saturating mutagenesis.

<a id="e20a"></a>**E20a** literature_search, Europe PMC abstract, PMID 27340226 (https://europepmc.org/article/MED/27340226; retrieved 2026-10-25T18:06:52+00:00)

> GWAS-related single-nucleotide polymorphisms lie within an essential erythroid enhancer of the BCL11A gene.

<a id="e20b"></a>**E20b** literature_search, Europe PMC abstract, PMID 24115442 (https://europepmc.org/article/MED/24115442; retrieved 2026-10-25T18:06:52+00:00)

> Fine-mapping uncovers a motif-disrupting common variant associated with reduced transcription factor (TF) binding, modestly diminished BCL11A expression, and elevated HbF.

<a id="e20c"></a>**E20c** literature_search, Europe PMC abstract, PMID 24115442 (https://europepmc.org/article/MED/24115442; retrieved 2026-10-25T18:06:52+00:00)

> Genome engineering reveals the enhancer is required in erythroid but not B-lymphoid cells for BCL11A expression.

<a id="e20d"></a>**E20d** literature_search, Europe PMC abstract, PMID 26375006 (https://europepmc.org/article/MED/26375006; retrieved 2026-10-25T18:06:52+00:00)

> Previously, we identified an erythroid enhancer of human BCL11A, subject to common genetic variation associated with the fetal haemoglobin level, the mouse orthologue of which is necessary for erythroid BCL11A expression.

<a id="e20e"></a>**E20e** literature_search, Europe PMC abstract, PMID 26375765 (https://europepmc.org/article/MED/26375765; retrieved 2026-10-25T18:06:52+00:00)

> Recent genome-wide association studies implicated the zinc-finger transcriptional repressor BCL11A in fetal hemoglobin regulation.
