# rs2168101 and Neuroblastoma (LMO1)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 8 model calls; 129 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## QBiC-SELEX screen

334 of 997 models pass the gate. Top groups: Unknown, 1 model (best CPEB1, z 78.94); bZIP, 1 model (best DBP, z 61.62); GATA, 6 models (best GATA2, z -56.07); bZIP, 2 models (best TEF, z 52.06); bZIP, 1 model (best NFIL3, z 51.94).

## Ranked chains

### 1. H1_GATA2_ref_more: GATA2 at the LMO1 intronic dELS (p = 0.65)

TF GATA2 (stated coverage own_model; registry own_model), ref allele binds more; element dELS enhancer EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma/adrenergic-lineage context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is the best-supported GATA-factor candidate for this GATA motif: QBiC-SELEX shows the alt A allele binds the GATA group less strongly than ref C (effect -0.816), with GATA2 as the best-scoring own-model member and the highest-expressed GATA factor in ACH-000149 (133.07 TPM). GATA2 ChIP-seq in SK-N-SH contains the variant, supporting occupancy but not allele specificity. The literature reports a GATA/TATA motif in the LMO1 first intron; on the LMO1 minus strand, plus-strand ref C corresponds to G and alt A to T. This is a binding prediction plus occupancy, not direct allele-specific GATA2 binding. | weak | [E10](#e10), [E18](#e18), [E06f](#e06f) |
| element | The variant lies within distal enhancer-like cCRE EH38E1518342 (dELS), with DNase, H3K27ac and H3K4me3 signal in ENCODE/SCREEN, making it a plausible regulatory element. | supported | [E03](#e03) |
| gene | This element is assigned to LMO1: LMO1 is the nearest protein-coding gene (34.9 kb, in gene body) and is the best L2G gene across credible sets. | supported | [E02](#e02), [E05](#e05) |
| cell_type | The relevant cell context is neuroblastoma, specifically the adrenergic state: the case expression context is ACH-000149/SK-N-SH, GATA2 ChIP-seq occupies the variant in SK-N-SH, and the literature links the LMO1 intronic GATA/TATA switch to adrenergic neuroblastoma initiation. | supported | [E07](#e07), [E18](#e18), [E06g](#e06g) |
| phenotype | The ref C/GATA allele is expected to preserve GATA-driven LMO1 enhancer activity and adrenergic-state initiation, while the alt A/TATA allele reduces it and lowers initiation risk. E06f/E06g support a GATA/TATA switch affecting neuroblastoma initiation, and E20 provides an allele-specific eQTL in skeletal muscle with alt A associated with lower LMO1 expression, consistent in direction but not neuroblastoma-specific. GATA2-specific causation is not established by these data. | supported | [E06f](#e06f), [E06g](#e06g), [E20](#e20) |

Predictions: Allele-specific GATA2 EMSA or GATA2 ChIP shows stronger GATA2 binding on ref C than alt A at rs2168101.; Reporter or MPRA assays in SK-N-SH show higher enhancer activity for ref C than alt A.; LMO1 expression is higher with ref C than alt A in adrenergic neuroblastoma cells, consistent with the E20 eQTL direction.; GATA2 perturbation reduces LMO1 and/or adrenergic-state markers in the relevant cell context.

Falsified if: Allele-specific EMSA, GATA2 ChIP, or reporter assays show no ref-vs-alt difference in GATA2 binding at rs2168101.; The alt A allele increases rather than decreases LMO1 enhancer activity or LMO1 expression in SK-N-SH or adrenergic neuroblastoma cells.; GATA2 perturbation does not reduce LMO1 or adrenergic-state markers in the relevant cell context.

### 2. H4_null_no_TF_effect: Null: no TF-mediated allelic effect (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs2168101 after controlling for linked variants.; No allele-specific LMO1 enhancer activity or LMO1 expression attributable to rs2168101 itself.; Any disease association is driven by a linked causal variant or by passenger status rather than a direct TF-mediated effect of rs2168101.

Falsified if: Allele-specific GATA2 binding and allele-specific LMO1 enhancer activity or expression are reproducibly demonstrated at rs2168101.; Genome editing of rs2168101 alone changes LMO1 enhancer activity or neuroblastoma-relevant phenotypes.

### 3. H2_GATA3_ref_more: GATA3 alternative GATA-factor chain (p = 0.10)

TF GATA3 (stated coverage own_model; registry own_model), ref allele binds more; element dELS enhancer EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is a plausible alternative GATA factor: it is an own-model passing member of the GATA QBiC-SELEX group with alt A binding less than ref C (z -54.11), it is expressed in ACH-000149 at 51.82 TPM (lower than GATA2), and GATA3 ChIP-seq in SK-N-SH contains the variant. This supports occupancy but not allele-specific GATA3 binding; GATA2 is favored by higher expression and ChIP, so this is a secondary GATA-factor chain. | weak | [E10](#e10), [E19](#e19), [E06f](#e06f) |
| element | The variant lies in distal enhancer-like cCRE EH38E1518342 with ENCODE/SCREEN enhancer marks. | supported | [E03](#e03) |
| gene | The element is linked to LMO1 by proximity and by L2G scoring. | supported | [E02](#e02), [E05](#e05) |
| cell_type | The relevant disease cell context is neuroblastoma; SK-N-SH is the provided expression context, GATA3 ChIP-seq occupies the variant in SK-N-SH, and the literature connects the LMO1 regulatory GATA/TATA switch to adrenergic neuroblastoma. | supported | [E07](#e07), [E19](#e19), [E06g](#e06g) |
| phenotype | If GATA3 rather than GATA2 mediates the effect, the same GATA/TATA direction is expected: ref C preserves GATA-driven LMO1 expression and adrenergic phenotype, while alt A lowers it and reduces initiation risk. E06f/E06g support the motif-switch direction, and E20 provides a directionally consistent allele-specific LMO1 eQTL, but no data establish GATA3 specificity. | weak | [E06f](#e06f), [E06g](#e06g), [E20](#e20) |

Predictions: Allele-specific GATA3 ChIP or EMSA shows stronger GATA3 binding on ref C than alt A at EH38E1518342.; GATA3 knockdown reduces LMO1 in SK-N-SH.; GATA3 binding, more than GATA2 binding, tracks allele-specific enhancer activity at rs2168101.

Falsified if: GATA3 is not expressed or not bound at this cCRE in SK-N-SH.; GATA3 knockdown has no effect on LMO1 expression or enhancer activity.; Allele-specific GATA binding at rs2168101 is fully explained by GATA2 and not GATA3.

## Prediction matrix

| Test | Cost | Separates top two | H1_GATA2_ref_more | H4_null_no_TF_effect | H2_GATA3_ref_more |
| --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA with GATA2 protein and ref/alt rs2168101 oligos | low | yes | GATA2 binds ref C more strongly than alt A. | No allele-specific GATA2 binding at rs2168101. | GATA2 allele-specific binding is not required; a GATA3-specific assay would be needed to test this chain. |
| Allele-specific GATA2 ChIP-qPCR at rs2168101 in SK-N-SH | medium | yes | Allele-specific GATA2 ChIP shows stronger occupancy on ref C than alt A. | No allele-specific GATA2 occupancy at rs2168101. | GATA2 allele-specific occupancy is not required; GATA3-specific ChIP would be the relevant test. |
| Allele-specific reporter or MPRA assay for rs2168101 in SK-N-SH | medium | yes | Ref C has higher enhancer activity than alt A. | No allele-specific enhancer activity at rs2168101. | Ref C has higher enhancer activity than alt A, but activity is GATA3-dependent. |
| Allele-specific LMO1 expression measurement after rs2168101 genome editing in neuroblastoma cells | high | yes | Alt A is associated with lower LMO1 expression than ref C. | No allele-specific LMO1 expression attributable to rs2168101. | Alt A is associated with lower LMO1 expression than ref C, but the effect is GATA3-dependent. |

## Next experiment

Allele-specific EMSA with GATA2 protein and ref/alt rs2168101 oligos: lowest-cost test that separates H1_GATA2_ref_more from H4_null_no_TF_effect because H1 predicts stronger ref C binding and H4 predicts no allele-specific binding.

## Investigate calls

- chip_peaks({"tf": "GATA2", "biosample": "SK-N-SH"})
- chip_peaks({"tf": "GATA3", "biosample": "SK-N-SH"})
- eqtl_lookup({"tissue": null})

## Flags

- none

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

> Interestingly, we found that the macrophage populations from the two tumor types were transcriptionally distinct, and LMO1 increased cancer-cell secretion of cytokines associated with metastasis and angiogenesis.

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

> Thus, conversion of the regulatory GATA to a TATA allele in the first intron of LMO1 reduced the neuroblastoma-initiation rate by preventing formation of the adrenergic cell state.

<a id="e06h"></a>**E06h** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T17:26:22+00:00)

> They now demonstrate experimentally, using genome-edited zebrafish, that a polymorphism in the human rs2168101 locus of the LMO1 gene determines which CRC is active in a tumor.

<a id="e06i"></a>**E06i** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T17:26:22+00:00)

> In some cases, LMO3 compensated for LMO1 loss and drove the adrenergic CRC in MYCN-positive NBL.

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

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr11_8233861_C_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T00:40:54+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr11_8233861_C_A_b38. NES is the effect of the alt allele (A) relative to ref (C).
> LMO1 in Muscle_Skeletal: NES -0.13, p 1.6e-09
