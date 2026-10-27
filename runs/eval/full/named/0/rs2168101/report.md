# rs2168101 and Neuroblastoma (LMO1)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.65 over 8 model calls; 176 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## QBiC-SELEX screen

334 of 997 models pass the gate. Top groups: Unknown, 1 model (best CPEB1, z 78.94); bZIP, 1 model (best DBP, z 61.62); GATA, 6 models (best GATA2, z -56.07); bZIP, 2 models (best TEF, z 52.06); bZIP, 1 model (best NFIL3, z 51.94).

## Ranked chains

### 1. H1: Ref C (G on the LMO1 minus strand) preserves a GATA motif bound by GATA3, sustaining the LMO1 intron-1 enhancer and the adrenergic state (p = 0.48)

TF GATA3 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E1518342 (dELS distal enhancer-like cCRE, chr11:8233740-8234086, LMO1 intron 1); gene LMO1; cell type Neuroblastoma cells with an adrenergic core regulatory circuit (SK-N-SH / SH-SY5Y, ACH-000149).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | All six GATA-group QBiC-SELEX models agree the alt A allele binds GATA factors less (best model GATA2 own model z -56.07, effect -0.816; site strength 100.0th -> 77.3rd percentile), i.e. ref C carries the intact GATA motif; within this shared-specificity group I name GATA3 because ENCODE ChIP-seq places a GATA3 peak over this exact base in SK-N-SH and SH-SY5Y and GATA3 is well expressed here (51.8 TPM). GATA2 is equally supported by ChIP (see H2), so the split between the two is not resolved by present evidence | weak | [E10](#e10), [E18](#e18), [E20c](#e20c) |
| element | The variant lies in dELS EH38E1518342 with high DNase (z 4.5) and H3K27ac (z 4.0) and is intronic to LMO1; the published mechanism is a GATA motif in LMO1 intron 1, and GATA2/GATA3 ChIP peaks in SK-N-SH show the element is occupied in a neuroblastoma line (cCRE z-scores themselves are maxima across biosamples) | supported | [E03](#e03), [E01](#e01), [E20c](#e20c), [E18](#e18), [E19](#e19) |
| gene | The enhancer acts on LMO1: the variant is intronic to LMO1, LMO1 is the best L2G gene (0.92) across 158 credible sets, and the literature ties this SNP to LMO1 expression levels; stronger GATA3 occupancy on the C (G) allele gives higher LMO1 | supported | [E01](#e01), [E02](#e02), [E05](#e05), [E20c](#e20c), [E06a](#e06a) |
| cell_type | GATA3 is expressed (51.8 TPM) and occupies this site in SK-N-SH and SH-SY5Y neuroblastoma cells; genome-edited zebrafish show the allele determines which core regulatory circuit is active in the tumor | weak | [E10](#e10), [E18](#e18), [E20e](#e20e), [E06b](#e06b) |
| phenotype | Conversion of the regulatory GATA allele to the TATA allele (G>T on the LMO1 strand, i.e. ref C -> alt A here) reduced the neuroblastoma-initiation rate by preventing formation of the adrenergic state; so the GATA-preserving ref C is the risk allele and alt A is protective, matching reports of protective LMO1 polymorphisms | supported | [E20d](#e20d), [E20a](#e20a), [E20b](#e20b), [E06c](#e06c) |

Predictions: Allele-specific GATA3 ChIP-seq or ChIP-qPCR in a C/A heterozygous neuroblastoma line shows C-allele-biased GATA3 reads at chr11:8233861; GATA3 knockdown lowers LMO1 in C-carrying adrenergic lines and flattens the allelic difference, while GATA2 knockdown has a smaller effect; Reporter/STARR assay of the 347 bp cCRE gives higher activity for the C allele in adrenergic but not mesenchymal neuroblastoma cells

Falsified if: Allele-specific GATA3 ChIP shows no C-allele bias at this base despite the peak; GATA3 depletion leaves LMO1 unchanged while GATA2 depletion abolishes the allelic difference; Isogenic C>A editing does not change LMO1 expression

### 2. H2: Same GATA-motif mechanism mediated by GATA2, the most abundant GATA factor in this line and also ChIP-bound at the site (p = 0.27)

TF GATA2 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E1518342 (dELS, LMO1 intron 1); gene LMO1; cell type Neuroblastoma cells (SK-N-SH / SH-SY5Y, ACH-000149).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The best model of the GATA specificity group is GATA2's own model (z -56.07, effect -0.816, alt binds less); within the group I name GATA2 because it is by far the highest-expressed GATA factor in the context line (133.07 TPM) and an ENCODE GATA2 ChIP-seq peak in SK-N-SH (and SH-SY5Y) contains this base | weak | [E10](#e10), [E19](#e19) |
| element | The motif lies in the LMO1 intron-1 distal enhancer-like cCRE, which is GATA2-occupied in SK-N-SH | supported | [E03](#e03), [E01](#e01), [E19](#e19) |
| gene | Loss of GATA2 binding on the A allele lowers output of this enhancer at LMO1, the dominant L2G gene for the variant | weak | [E05](#e05), [E02](#e02), [E20c](#e20c) |
| cell_type | GATA2 is strongly expressed (133.07 TPM) and bound at this site in two neuroblastoma lines, so the binding change is realizable there | weak | [E10](#e10), [E19](#e19) |
| phenotype | Reduced LMO1 on the A (TATA) allele reduces neuroblastoma initiation by preventing the adrenergic state | weak | [E20d](#e20d), [E20a](#e20a), [E06c](#e06c) |

Predictions: Allele-specific GATA2 ChIP shows stronger C-allele bias than GATA3 at this base; GATA2 knockdown, not GATA3 knockdown, abolishes the allelic difference in LMO1 expression; GATA2 degron/rapid depletion reduces H3K27ac at EH38E1518342

Falsified if: Allele-specific GATA2 reads are balanced while GATA3 reads are C-biased; GATA2 depletion leaves LMO1 unchanged

### 3. H5: Null: no TF-mediated effect of this base itself (linked causal variant or pleiotropic signal) (p = 0.16)

Null chain: no TF-mediated effect of this variant.

Predictions: Allelic reporter and base editing at chr11:8233861 show no difference in enhancer activity or LMO1 expression; Allele-specific GATA2/GATA3 ChIP reads are balanced despite the peak; Neuroblastoma fine-mapping points to another variant in the same LD block; the 158 credible sets for amino acids, height and HbA1c reflect a linked or pleiotropic variant acting through another gene

Falsified if: Isogenic C vs A editing changes LMO1 expression or enhancer activity; Allele-specific GATA ChIP imbalance is demonstrated at this exact base

### 4. H3: The alt A allele creates a PAR-bZIP (NFIL3) site that represses the LMO1 enhancer (p = 0.06)

TF NFIL3 (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1518342 (dELS, LMO1 intron 1); gene LMO1; cell type Neuroblastoma cells (SK-N-SH, ACH-000149).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts a gain of bZIP binding on the alt allele (NFIL3 own model z 51.94, effect +2.575; TEF z 52.06 and DBP z 61.62 agree in direction). Within these PAR-bZIP groups the choice of NFIL3 is weak: it is the best-expressed member (8.07 TPM vs DBP 6.19, TEF 3.72) and a known repressor, but no ChIP or occupancy evidence supports any of them here | weak | [E12](#e12), [E11](#e11), [E09](#e09) |
| element | The gained site lies in the active distal enhancer-like cCRE in LMO1 intron 1 | weak | [E03](#e03), [E01](#e01) |
| gene | If NFIL3 binds the A allele and represses, LMO1 output falls; no evidence in hand shows NFIL3 acting on this enhancer, only that LMO1 is the likely target gene | missing | [E05](#e05), [E02](#e02) |
| cell_type | NFIL3 is expressed in the context line at 8.07 TPM; no occupancy data | weak | [E12](#e12) |
| phenotype | Lower LMO1 on the A allele reduces neuroblastoma risk, the same direction as the GATA account but via a gained repressor rather than a lost activator | missing | [E20d](#e20d), [E06c](#e06c) |

Predictions: NFIL3 (or TEF/DBP) ChIP shows A-allele-specific occupancy at the site; Mutating the gained bZIP core in the A-allele reporter restores activity to C-allele levels; GATA motif disruption alone does not fully explain the reporter difference

Falsified if: No PAR-bZIP occupancy at this cCRE in neuroblastoma cells; Mutating the gained bZIP core leaves A-allele reporter activity unchanged; The zebrafish GATA-to-TATA swap fully reproduces the effect without any bZIP site

### 5. H4: Loss of a ZBTB18 site on the alt allele de-represses the LMO1 enhancer (opposite direction) (p = 0.03)

TF ZBTB18 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E1518342 (dELS, LMO1 intron 1); gene LMO1; cell type Neuroblastoma cells (SK-N-SH, ACH-000149).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZBTB18's own QBiC-SELEX model predicts weaker binding on the alt allele (z -31.2, effect -2.791; 99.4th -> 78.4th percentile); this is a binding prediction only, with no ChIP support | weak | [E17](#e17) |
| element | The site is within the LMO1 intron-1 distal enhancer-like cCRE | weak | [E03](#e03), [E01](#e01) |
| gene | If ZBTB18 represses this element, its loss on the A allele would raise LMO1; no evidence shows ZBTB18 acting on this enhancer | missing | [E05](#e05), [E02](#e02) |
| cell_type | ZBTB18 (a C2H2 zinc finger) is expressed at 17.06 TPM in the context line | weak | [E17](#e17) |
| phenotype | This model predicts the A allele raises LMO1 and risk, which contradicts the published zebrafish result that the TATA (A) allele lowers neuroblastoma initiation; it is retained only as a directional control | missing | [E20d](#e20d) |

Predictions: Allele-specific expression shows higher LMO1 from the A allele; ZBTB18 ChIP shows C-allele-biased occupancy and ZBTB18 depletion raises LMO1

Falsified if: LMO1 expression and risk track the C allele, as E20d indicates; No ZBTB18 binding at this enhancer

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H5 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GATA3 ChIP-seq read counts at chr11:8233861 in a C/A heterozygous neuroblastoma line (reanalysis of ENCSR000BTH plus one new ChIP) | low | yes | Clear C-allele bias in GATA3 reads | GATA3 reads near balanced or weakly biased; bias concentrated in GATA2 | Balanced reads for both GATA factors | No or weak GATA3 bias | No GATA3 bias |
| Allele-specific GATA2 ChIP-seq read counts at the same base (ENCSR706VOO reanalysis) | low | yes | Some bias possible but weaker than GATA3 | Strong C-allele bias in GATA2 reads | Balanced | No GATA2 bias | No GATA2 bias |
| siRNA/degron knockdown of GATA3 vs GATA2 in an adrenergic neuroblastoma line, measure LMO1 mRNA and enhancer H3K27ac | medium | yes | GATA3 loss lowers LMO1 more than GATA2 loss | GATA2 loss lowers LMO1 more than GATA3 loss | LMO1 may change with GATA levels but no allelic component | Neither strongly changes LMO1; NFIL3 knockdown raises it | Neither; ZBTB18 knockdown raises LMO1 |
| Allelic luciferase/STARR reporter of the 347 bp cCRE (C vs A, plus GATA-core and bZIP-core mutants) | medium | no | C > A; GATA-core mutation abolishes the difference | C > A; same GATA-core dependence (not distinguished from H1) | No allelic difference | C > A but bZIP-core mutation in the A construct restores activity | A > C |
| Isogenic base editing C>A at chr11:8233861 in an adrenergic line; LMO1 expression and adrenergic CRC markers | high | no | LMO1 falls, adrenergic markers fall | LMO1 falls, adrenergic markers fall | No change | LMO1 falls, reversible by NFIL3 depletion | LMO1 rises |
| DepMap LMO1 gene dependency across neuroblastoma lines | existing data | no | LMO1 dependency in adrenergic neuroblastoma lines | Same expectation | Uninformative about this base | Same expectation | Same expectation |

## Next experiment

Reanalyze the existing ENCODE GATA3 (ENCSR000BTH) and GATA2 (ENCSR706VOO) SK-N-SH ChIP-seq BAMs for allele-specific read counts at chr11:8233861 in the heterozygous line: this is near-zero cost, tests whether either factor shows C-allele-biased occupancy (vs the null's balanced reads), and the relative bias between GATA3 and GATA2 separates H1 from H2.

## Investigate calls

- chip_peaks({"tf": "GATA3", "biosample": "SK-N-SH"})
- chip_peaks({"tf": "GATA2", "biosample": "SK-N-SH"})
- literature_search({"query": "rs2168101 LMO1 GATA risk allele G protective T neuroblastoma"})

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

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T17:26:22+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T17:26:22+00:00)

> They now demonstrate experimentally, using genome-edited zebrafish, that a polymorphism in the human rs2168101 locus of the LMO1 gene determines which CRC is active in a tumor.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 40078563 (https://europepmc.org/article/MED/40078563; retrieved 2026-10-25T17:26:22+00:00)

> Fourteen loci, including ten protective polymorphisms from CASC15, BARD1, LMO1, HSD17B12, and HACE1, and four risk variants from BARD1, RSRC1, CPZ and MMP20 were significantly associated with neuroblastoma risk.

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

> 1 ENCODE GATA3 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR000BTH. In other biosamples, 1 GATA3 peaks do contain the variant: SH-SY5Y (experiments ENCSR000EXZ).

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:35+00:00)

> 1 ENCODE GATA2 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR706VOO. In other biosamples, 1 GATA2 peaks do contain the variant: SH-SY5Y (experiments ENCSR000EYB).

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20LMO1%20GATA%20risk%20allele%20G%20protective%20T%20neuroblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T22:29:05+00:00)

> Europe PMC: 17 hits for 'rs2168101 LMO1 GATA risk allele G protective T neuroblastoma'; top 8 with PMIDs:
> PMID 38937681 (2024): LMO family gene polymorphisms and Wilms tumor susceptibility in Chinese children: a five-center case-control study.
> PMID 37183825 (2023): Genetic predisposition to neuroblastoma results from a regulatory polymorphism that promotes the adrenergic cell state.
> PMID 37183823 (2023): Back to the future: evolutionary biology reveals a key regulatory switch in neuroblastoma pathogenesis.
> PMID 37849756 (2023): Two bullets in the gun: combining immunotherapy with chemotherapy to defeat neuroblastoma by targeting adrenergic-mesenchymal plasticity.
> PMID 38653778 (2024): Lineage specific transcription factor waves reprogram neuroblastoma from self-renewal to differentiation.
> PMID 38587919 (2024): Super-enhancers: drivers of cells' identities and cells' debacles.
> PMID 33870932 (2021): LIM domain only 1: an oncogenic transcription cofactor contributing to the tumorigenesis of multiple cancer types.
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.

<a id="e20a"></a>**E20a** literature_search, Europe PMC abstract, PMID 38937681 (https://europepmc.org/article/MED/38937681; retrieved 2026-10-25T22:29:05+00:00)

> We found LMO1 rs2168101 G > T and rs11603024 C > T as well as LMO2 rs7933499 G > A were significantly associated with Wilms tumor risk.

<a id="e20b"></a>**E20b** literature_search, Europe PMC abstract, PMID 38937681 (https://europepmc.org/article/MED/38937681; retrieved 2026-10-25T22:29:05+00:00)

> Stratified analysis demonstrated a protective role of rs2168101 GT/TT genotypes against Wilms tumor in the subgroups of age ≤ 18 months, males and clinical stages I/II compared to the rs2168101 GG genotype.

<a id="e20c"></a>**E20c** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T22:29:05+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e20d"></a>**E20d** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T22:29:05+00:00)

> Thus, conversion of the regulatory GATA to a TATA allele in the first intron of LMO1 reduced the neuroblastoma-initiation rate by preventing formation of the adrenergic cell state.

<a id="e20e"></a>**E20e** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T22:29:05+00:00)

> They now demonstrate experimentally, using genome-edited zebrafish, that a polymorphism in the human rs2168101 locus of the LMO1 gene determines which CRC is active in a tumor.
