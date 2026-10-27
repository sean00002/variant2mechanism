# rs2168101 and Neuroblastoma (LMO1)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 278 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## QBiC-SELEX screen

334 of 997 models pass the gate. Top groups: Unknown, 1 model (best CPEB1, z 78.94); bZIP, 1 model (best DBP, z 61.62); GATA, 6 models (best GATA2, z -56.07); bZIP, 2 models (best TEF, z 52.06); bZIP, 1 model (best NFIL3, z 51.94).

## Ranked chains

### 1. H1_GATA2_alt_loss: GATA2 motif loss at the LMO1 enhancer (p = 0.60)

TF GATA2 (stated coverage own_model; registry own_model), ref allele binds more; element distal enhancer-like cCRE containing rs2168101; gene LMO1; cell type neuroblastoma / SK-N-SH adrenergic-lineage cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | On the plus strand rs2168101 is C>A; because LMO1 is on the minus strand, this is G>T on the transcript strand, so the protective TATA allele corresponds to plus-strand alt A. Alt A reduces GATA2 binding at the rs2168101 sequence. GATA2 is the best-supported GATA factor here: it has an own QBiC-SELEX model (own_model), is the highest-expressed GATA factor in SK-N-SH (133.07 TPM), and an ENCODE GATA2 ChIP-seq peak in SK-N-SH contains the variant. The GATA QBiC-SELEX group shows alt binding less (effect -0.816), and the literature independently links rs2168101 to a GATA motif. | supported | [E10](#e10), [E18](#e18), [E07](#e07), [E06f](#e06f), [E20a](#e20a) |
| element | rs2168101 lies within EH38E1518342, a distal enhancer-like cCRE with DNase and H3K27ac signal in the LMO1 intron. The ENCODE cCRE z-scores are maxima across biosamples, so SK-N-SH-specific enhancer activity is not directly proven by this row. | supported | [E03](#e03), [E01](#e01) |
| gene | The enhancer is assigned to LMO1 by proximity and Open Targets L2G; LMO1 is the strongest candidate gene at this locus (best L2G score 0.92), far above RIC3. | supported | [E02](#e02), [E05](#e05) |
| cell_type | The relevant expression context is neuroblastoma SK-N-SH, where GATA2 is highly expressed, GATA2 occupies the variant-containing region, and LMO1 is a known neuroblastoma oncogenic co-regulator. | supported | [E10](#e10), [E18](#e18), [E06a](#e06a), [E06i](#e06i) |
| phenotype | The literature supports the direction: the risk G allele is favoured in allelic-imbalance assays in tumours, conversion of the GATA motif to the protective TATA allele reduces neuroblastoma initiation, and the protective TATA allele reduces MYCN-driven tumour penetrance in zebrafish. Thus alt A is predicted to lower GATA2-dependent LMO1 expression and reduce neuroblastoma risk. This is not a direct human C>A GATA2-dependence experiment. | weak | [E20b](#e20b), [E20c](#e20c), [E20d](#e20d), [E06f](#e06f), [E06g](#e06g), [E06e](#e06e) |

Predictions: GATA2 occupies the rs2168101 enhancer in SK-N-SH.; The ref C allele shows stronger GATA2 binding than alt A.; Alt A associates with lower LMO1 enhancer activity/LMO1 expression and a less adrenergic, lower-risk neuroblastoma phenotype.

Falsified if: Allele-specific GATA2 binding at rs2168101 is absent or alt A binds more than ref C.; GATA2 occupancy at EH38E1518342 is not seen in SK-N-SH or is not allele-specific.; Editing ref C to alt A does not reduce LMO1 enhancer activity or LMO1 expression, or GATA2 depletion does not modify the effect.

### 2. H0_null: No TF-mediated allelic effect (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at rs2168101.; Any disease association is explained by linkage to another causal variant, a passenger event, or no allelic effect on TF activity.

Falsified if: A direct allele-specific TF-binding assay at rs2168101 shows a reproducible effect that tracks with LMO1 expression.; Fine-mapping or editing excludes a linked causal variant and shows the C>A change itself is functional.

### 3. H2_GATA3_alt_loss: GATA3 motif loss at the LMO1 enhancer (p = 0.15)

TF GATA3 (stated coverage own_model; registry own_model), ref allele binds more; element distal enhancer-like cCRE containing rs2168101; gene LMO1; cell type neuroblastoma / SK-N-SH adrenergic-lineage cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alt A reduces GATA3 binding at the rs2168101 sequence. GATA3 has an own QBiC-SELEX model (own_model), is expressed at 51.82 TPM in SK-N-SH, and an ENCODE GATA3 ChIP-seq peak in SK-N-SH contains the variant. GATA3 is a plausible alternative GATA factor, but it is lower expressed than GATA2 and the literature does not identify GATA3 specifically at this motif. | weak | [E10](#e10), [E19](#e19), [E07](#e07), [E06f](#e06f), [E20a](#e20a) |
| element | rs2168101 lies within EH38E1518342, a distal enhancer-like cCRE with DNase and H3K27ac signal in the LMO1 intron. The ENCODE cCRE z-scores are maxima across biosamples, not SK-N-SH-specific. | supported | [E03](#e03), [E01](#e01) |
| gene | The enhancer is assigned to LMO1 by proximity and Open Targets L2G; LMO1 is the strongest candidate gene at this locus. | supported | [E02](#e02), [E05](#e05) |
| cell_type | SK-N-SH is a neuroblastoma expression context in which GATA3 is expressed and occupies the variant-containing region, and LMO1 is neuroblastoma-relevant. | supported | [E10](#e10), [E19](#e19), [E06i](#e06i) |
| phenotype | If GATA3 rather than GATA2 is the relevant GATA factor, alt A is predicted to reduce GATA3-dependent LMO1 expression and reduce neuroblastoma risk by analogy to the GATA-to-TATA protective-allele literature. This factor-specific phenotype is not directly tested. | weak | [E06f](#e06f), [E20a](#e20a), [E20b](#e20b), [E06g](#e06g) |

Predictions: GATA3 occupies the rs2168101 enhancer in SK-N-SH and shows allele-specific binding.; The ref C allele shows stronger GATA3 binding than alt A.; GATA3 perturbation changes LMO1 enhancer activity or expression.

Falsified if: GATA3 does not occupy the locus in SK-N-SH or shows no allele-specific binding.; GATA3 depletion does not alter LMO1 enhancer activity or LMO1 expression.; Allele-specific GATA3 binding is absent or alt A binds more than ref C.

## Prediction matrix

| Test | Cost | Separates top two | H1_GATA2_alt_loss | H0_null | H2_GATA3_alt_loss |
| --- | --- | --- | --- | --- | --- |
| Allele-specific luciferase reporter in SK-N-SH: EH38E1518342 ref C vs alt A, with and without GATA2 knockdown. | low | yes | Alt A lowers enhancer activity; GATA2 depletion reduces or abolishes the difference. | No reproducible allele-specific enhancer activity difference. | Alt A lowers enhancer activity; GATA3 depletion rather than GATA2 depletion reduces the difference. |
| Allele-specific GATA2 ChIP-qPCR in SK-N-SH cells heterozygous at rs2168101. | medium | yes | GATA2 ChIP-qPCR at the enhancer shows occupancy and ref C > alt A in heterozygous cells. | No allele-specific GATA2 occupancy. | GATA2 occupancy may be present but no GATA2 allele-specific imbalance; GATA3 carries the allele-specific signal. |
| GATA2 knockout/knockdown in SK-N-SH followed by LMO1 expression and enhancer-activity measurement. | medium | yes | GATA2 knockout/knockdown reduces LMO1 expression or enhancer activity and modifies the ref-vs-alt effect. | No allele-specific effect and no TF-dependent LMO1 change. | GATA2 perturbation has little effect; GATA3 perturbation changes LMO1. |
| Allele-specific GATA3 ChIP-qPCR in SK-N-SH. | medium | no | No or weak allele-specific GATA3 binding; GATA2 remains the better factor. | No allele-specific GATA3 occupancy. | GATA3 ChIP-qPCR shows occupancy and ref C > alt A at the enhancer. |
| CRISPR knock-in of ref C vs alt A at the endogenous rs2168101 locus, with LMO1 expression and chromatin readouts. | high | yes | CRISPR editing of the C>A allele itself changes LMO1 enhancer activity/expression; linked-variant model is excluded. | Editing the C>A allele has no effect; a linked causal variant explains the association. | Editing changes LMO1 in a GATA3-dependent rather than GATA2-dependent way. |

## Next experiment

Cheapest separating experiment for the top two chains H1_GATA2_alt_loss and H0_null: allele-specific luciferase reporter in SK-N-SH using the EH38E1518342 enhancer with ref C versus alt A, performed with and without GATA2 knockdown. H1 predicts alt A lowers enhancer activity and that GATA2 depletion reduces the allelic difference; H0 predicts no reproducible allele-specific activity.

## Investigate calls

- chip_peaks({"tf": "GATA2", "biosample": "SK-N-SH"})
- chip_peaks({"tf": "GATA3", "biosample": "SK-N-SH"})
- literature_search({"query": "rs2168101 allele-specific reporter LMO1 GATA neuroblastoma"})

## Flags

- quote_rejected: PMID 33870932: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/11:8233861-8233861:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:14+00:00)

> Variant chr11:8233861:C>A (GRCh38), allele string C/A
> Known IDs: rs2168101
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: 6.43
> Transcript consequences: LMO1 (intron_variant); LMO1 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/11:7233861-9233861?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:26:12+00:00)

> 25 protein-coding genes within 1000 kb of chr11:8233861:C>A, by distance to TSS:
> LMO1: 34.9 kb from TSS (in gene body, strand -1)
> RIC3: 64.8 kb from TSS (upstream, strand -1)
> TUB: 214.7 kb from TSS (downstream, strand +1)
> EIF3F: 263.6 kb from TSS (downstream, strand +1)
> NLRP10: 268.4 kb from TSS (upstream, strand -1)
> OR10A3: 292.2 kb from TSS (upstream, strand -1)
> OR10A6: 302.6 kb from TSS (upstream, strand -1)
> STK33: 360.4 kb from TSS (downstream, strand -1)
> OR5P3: 403.0 kb from TSS (upstream, strand -1)
> OR5P2: 436.9 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E1518342 (dELS: distal enhancer-like), chr11:8233740-8234086.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E1518342 dELS (contains the variant): DNase z 4.5, H3K27ac z 4.0, H3K4me3 z 2.7, CTCF z 1.4; nearby genes LMO1, AC091013.1, RIC3
> EH38E1518343 dELS: DNase z 4.4, H3K27ac z 3.9, H3K4me3 z 2.9, CTCF z 1.6; nearby genes LMO1, AC091013.1, RIC3
> EH38E2943027 dELS: DNase z 2.8, H3K27ac z 4.0, H3K4me3 z 1.8, CTCF z 1.6; nearby genes LMO1, AC091013.1, RIC3
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs2168101&size=100; retrieved 2026-10-25T17:26:22+00:00)

> 71 GWAS Catalog associations for rs2168101, strongest first:
> Glutamine levels: p 2.0e-208, effect allele A, risk-allele frequency NR, PMID 41044249
> Alanine levels: p 2.0e-151, effect allele A, risk-allele frequency NR, PMID 41044249
> Glycine levels: p 3.0e-43, effect allele A, risk-allele frequency NR, PMID 41044249
> Fasting blood glucose: p 2.0e-42, effect allele A, risk-allele frequency NR, PMID 40436827
> Tyrosine levels: p 2.0e-40, effect allele A, risk-allele frequency NR, PMID 41044249
> Height (maximum, inv-normal transformed): p 5.0e-37, effect allele C, risk-allele frequency 0.7115, PMID 39024449
> Glutamine levels (UKB data field 23461): p 4.0e-33, effect allele A, risk-allele frequency 0.308564, PMID 36764567
> height (mean, inv-normal transformed): p 9.0e-33, effect allele C, risk-allele frequency 0.7115, PMID 39024449
> Alanine levels (UKB data field 23460): p 7.0e-27, effect allele A, risk-allele frequency 0.308491, PMID 36764567
> height (minimum, inv-normal transformed): p 1.0e-24, effect allele C, risk-allele frequency 0.7115, PMID 39024449
> Albumin levels: p 2.0e-24, effect allele A, risk-allele frequency NR, PMID 40436827
> Histidine levels: p 5.0e-23, effect allele A, risk-allele frequency NR, PMID 41044249

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:15+00:00)

> 158 credible sets contain 11_8233861_C_A: 157 GWAS, 1 molecular QTL.
> GWAS Height: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Hemoglobin A1c levels: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Tyrosine levels: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Total concentration of branched-chain amino acids (leucine +: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS chloride  (minimum, inv-norm transformed): PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Diastolic blood pressure x short total sleep time interactio: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> pqtl for CFC1 (UKB_PPP_EUR_CFC1_P0CG37_OID21261_v1): PIP 1.00
> Best L2G gene scores across these sets: LMO1 0.92, RIC3 0.08

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20AND%20LMO1%20AND%20%22neuroblastoma%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:22+00:00)

> Europe PMC: 51 hits for 'rs2168101 AND LMO1 AND "neuroblastoma"'; top 7 with PMIDs:
> PMID 41858882 (2026): LMO1 expression in neuroblastoma cells reprograms tumor-associated macrophages to promote metastasis.
> PMID 38937681 (2024): LMO family gene polymorphisms and Wilms tumor susceptibility in Chinese children: a five-center case-control study.
> PMID 40078563 (2025): Improving neuroblastoma risk prediction through a polygenic risk score derived from genome-wide association study-identified loci.
> PMID 37183825 (2023): Genetic predisposition to neuroblastoma results from a regulatory polymorphism that promotes the adrenergic cell state.
> PMID 40340897 (2025): Genetic variants of m&lt;sup&gt;1&lt;/sup&gt;A modification genes and the risk of neuroblastoma: novel insights from a Chinese case-control study.
> PMID 37183823 (2023): Back to the future: evolutionary biology reveals a key regulatory switch in neuroblastoma pathogenesis.
> PMID 37849756 (2023): Two bullets in the gun: combining immunotherapy with chemotherapy to defeat neuroblastoma by targeting adrenergic-mesenchymal plasticity.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41858882 (https://europepmc.org/article/MED/41858882; retrieved 2026-10-25T17:26:22+00:00)

> To better understand this synergy, we performed single-cell RNA sequencing analysis on primary tumors from transgenic zebrafish overexpressing MYCN alone or with LMO1.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 41858882 (https://europepmc.org/article/MED/41858882; retrieved 2026-10-25T17:26:22+00:00)

> Our data suggest that LMO1 overexpression in MYCN-amplified NB cells increases the pro-metastatic properties of macrophages in the tumor-cell microenvironment, which is important for driving NB metastasis.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 38937681 (https://europepmc.org/article/MED/38937681; retrieved 2026-10-25T17:26:22+00:00)

> We found LMO1 rs2168101 G > T and rs11603024 C > T as well as LMO2 rs7933499 G > A were significantly associated with Wilms tumor risk.

<a id="e06d"></a>**E06d** literature_search, Europe PMC abstract, PMID 38937681 (https://europepmc.org/article/MED/38937681; retrieved 2026-10-25T17:26:22+00:00)

> Stratified analysis demonstrated a protective role of rs2168101 GT/TT genotypes against Wilms tumor in the subgroups of age ≤ 18 months, males and clinical stages I/II compared to the rs2168101 GG genotype.

<a id="e06e"></a>**E06e** literature_search, Europe PMC abstract, PMID 40078563 (https://europepmc.org/article/MED/40078563; retrieved 2026-10-25T17:26:22+00:00)

> Fourteen loci, including ten protective polymorphisms from CASC15, BARD1, LMO1, HSD17B12, and HACE1, and four risk variants from BARD1, RSRC1, CPZ and MMP20 were significantly associated with neuroblastoma risk.

<a id="e06f"></a>**E06f** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T17:26:22+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e06g"></a>**E06g** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T17:26:22+00:00)

> Here, we showed that WT zebrafish with the GATA genotype developed adrenergic neuroblastoma, while knock-in of the protective TATA allele at this locus reduced the penetrance of MYCN-driven tumors, which were restricted to the mesenchymal cell state.

<a id="e06h"></a>**E06h** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T17:26:22+00:00)

> They now demonstrate experimentally, using genome-edited zebrafish, that a polymorphism in the human rs2168101 locus of the LMO1 gene determines which CRC is active in a tumor.

<a id="e06i"></a>**E06i** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T17:26:22+00:00)

> The authors previously showed that overexpression of LIM-domain-only 1 (LMO1), a transcriptional coregulator, synergizes with MYCN to accelerate tumor formation and metastasis in an NBL-zebrafish model.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr11:8233861:C>A: 997 models scored, 334 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 227 CIS-BP groups. Expression context: DepMap line ACH-000149. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 39 (Homeodomain, 4 models z 59.17, Homeodomain, 3 models z 38.75, Homeodomain; POU, 1 model z 20.28, C2H2 ZF, 1 model z 19.82, C2H2 ZF, 1 model z -17.92). Passing groups ranked below the ones shown: 178. In the group rows, 'own model' means the TF has its own QBiC-SELEX model and 'mapped' that it is covered only through CIS-BP-mapped models of related TFs. A TF not named in any group row may still have its own model, even one that passes the gate: look it up with qbic_tf_detail before stating its coverage or a QBiC-SELEX direction for it. predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G153 (Unknown, 1 model): best model CPEB1_NA_TAACCC20NCG_ESAC_yang2017_0_3_7mer (own model of CPEB1), z 78.94, effect 3.719 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CPEB1 z 78.94. TFs this group covers: CPEB1 (own model) 4.79 TPM; best model's site strength: ref 99.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G164 (bZIP, 1 model): best model DBP_NA_TGCGGG20NGGC_AE_jolma2013_0_2_7mer (own model of DBP), z 61.62, effect 4.82 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: DBP z 61.62. TFs this group covers: DBP (own model) 6.19 TPM; best model's site strength: ref 99.3th, alt 99.9th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G010 (GATA, 6 models): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (own model of GATA2), z -56.07, effect -0.816 (alt binds less); 6 passing models (6 with the best model's sign). Passing members: GATA2 z -56.07, GATA3 z -54.11, GATA6 z -53.73, GATA5 z -52.75, GATA1 z -49.7 (+1 more). TFs this group covers: GATA2 (own model) 133.07 TPM, GATA3 (own model) 51.82 TPM, GATA4 (own model) 13.8 TPM, GATA6 (own model) 0.07 TPM, GATA5 (own model) 0.01 TPM, GATA1 (own model) 0.0 TPM; best model's site strength: ref 100.0th, alt 77.3th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G076 (bZIP, 2 models): best model TEF_NA_TATAAG20NTA_ESQ_yang2017_0_2_7mer (own model of TEF), z 52.06, effect 2.175 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: TEF z 52.06, HLF z 27.84. TFs this group covers: TEF (own model) 3.72 TPM, HLF (own model) 0.68 TPM; best model's site strength: ref 92.2th, alt 99.7th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G262 (bZIP, 1 model): best model NFIL3_NA_TAGACG20NCG_ESY_yang2017_0_2_7mer (own model of NFIL3), z 51.94, effect 2.575 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: NFIL3 z 51.94. TFs this group covers: NFIL3 (own model) 8.07 TPM; best model's site strength: ref 99.4th, alt 99.8th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G589 (C2H2 ZF, 1 model): best model ZNF75A_FL_TTGCTG40NCTA_KW_yin2017_0_4_7mer (own model of ZNF75A), z 48.81, effect 1.176 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF75A z 48.81. TFs this group covers: ZNF75A (own model) 15.12 TPM, ZNF75D (mapped) 3.0 TPM; best model's site strength: ref 96.4th, alt 99.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G004 (Homeodomain, 18 models): best model HOXC12_NA_TCATGC20NGTA_ESY_yang2017_0_4_7mer (own model of HOXC12), z 42.95, effect 2.352 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: HOXC12 z 42.95, HOXC11 z 40.23, HOXD11 z 35.99, HOXC9 z 29.07, HOXC10 z 29.06 (+13 more). TFs this group covers: HOXD8 (own model) 15.75 TPM, HOXC4 (own model) 8.52 TPM, HOXD9 (own model) 7.58 TPM, HOXC6 (mapped) 5.8 TPM, HOXC9 (own model) 5.16 TPM, HOXC5 (mapped) 3.65 TPM, HOXD4 (own model) 3.42 TPM, HOXD3 (own model) 3.11 TPM, HOXC8 (own model) 1.99 TPM, HOXB3 (own model) 1.38 TPM (+24 more); best model's site strength: ref 91.7th, alt 99.7th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G367 (Unknown, 1 model): best model THYN1_FL_TG40NCTGTGG_YWFA_jolma2025_0_4_7mer (own model of THYN1), z -34.07, effect -0.261 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: THYN1 z -34.07. TFs this group covers: THYN1 (own model) 40.98 TPM; best model's site strength: ref 51.4th, alt 9.7th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G418 (C2H2 ZF, 1 model): best model ZFP1_eDBD_TGAACT40NAAG_KT_yin2017_0_4_7mer (own model of ZFP1), z 31.88, effect 2.621 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZFP1 z 31.88. TFs this group covers: ZFP1 (own model) 9.99 TPM; best model's site strength: ref 94.2th, alt 99.8th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G393 (C2H2 ZF, 1 model): best model ZBTB18_eDBD_TACTCC40NGTA_KR_yin2017_0_3_7mer (own model of ZBTB18), z -31.2, effect -2.791 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB18 z -31.2. TFs this group covers: ZBTB18 (own model) 17.06 TPM; best model's site strength: ref 99.4th, alt 78.4th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:35+00:00)

> 1 ENCODE GATA2 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR706VOO. In other biosamples, 1 GATA2 peaks do contain the variant: SH-SY5Y (experiments ENCSR000EYB).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:35+00:00)

> 1 ENCODE GATA3 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR000BTH. In other biosamples, 1 GATA3 peaks do contain the variant: SH-SY5Y (experiments ENCSR000EXZ).

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20allele-specific%20reporter%20LMO1%20GATA%20neuroblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T01:45:35+00:00)

> Europe PMC: 9 hits for 'rs2168101 allele-specific reporter LMO1 GATA neuroblastoma'; top 8 with PMIDs:
> PMID 37183825 (2023): Genetic predisposition to neuroblastoma results from a regulatory polymorphism that promotes the adrenergic cell state.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 33870932 (2021): LIM domain only 1: an oncogenic transcription cofactor contributing to the tumorigenesis of multiple cancer types.
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.
> PMID 37180836 (2023): Variant rs8400 enhances ALKBH5 expression through disrupting miR-186 binding and promotes neuroblastoma progression.
> PMID 26560027 (2015): Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism.
> PMID 36152315 (2023): Genetic regulatory and biological implications of the 10q24.32 schizophrenia risk locus.
> PMID 29589100 (2018): Genetic susceptibility to neuroblastoma: current knowledge and future directions.

<a id="e20a"></a>**E20a** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-26T01:45:35+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e20b"></a>**E20b** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-26T01:45:35+00:00)

> Thus, conversion of the regulatory GATA to a TATA allele in the first intron of LMO1 reduced the neuroblastoma-initiation rate by preventing formation of the adrenergic cell state.

<a id="e20c"></a>**E20c** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T01:45:35+00:00)

> We show that SNP rs2168101 G>T is the most highly associated variant (combined P = 7.47 × 10(-29), odds ratio 0.65, 95% confidence interval 0.60-0.70), and resides in a super-enhancer defined by extensive acetylation of histone H3 lysine 27 within the first intron of LMO1.

<a id="e20d"></a>**E20d** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T01:45:35+00:00)

> We demonstrate allelic imbalance favouring the G-containing strand in tumours heterozygous for this SNP, as demonstrated both by RNA sequencing (P < 0.0001) and reporter assays (P = 0.002).
