# rs2168101 and Neuroblastoma (LMO1)

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.63 over 8 model calls; 204 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## QBiC-SELEX screen

334 of 997 models pass the gate. Top groups: Unknown, 1 model (best CPEB1, z 78.94); bZIP, 1 model (best DBP, z 61.62); GATA, 6 models (best GATA2, z -56.07); bZIP, 2 models (best TEF, z 52.06); bZIP, 1 model (best NFIL3, z 51.94).

## Ranked chains

### 1. H1: Ref C (= G on minus strand) completes a GATA motif in the LMO1 intron-1 enhancer bound by GATA3; alt A (= T) converts it to TATA, losing GATA3 binding and lowering LMO1 in adrenergic neuroblastoma cells (p = 0.42)

TF GATA3 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E1518342 (dELS) in LMO1 intron 1, chr11:8233740-8234086; gene LMO1; cell type Adrenergic-state neuroblastoma / sympathoadrenal neuroblast (SK-N-SH, ACH-000149).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | All 6 GATA models lose binding on alt (best GATA2 z -56.07; ref 100th to alt 77.3rd percentile), matching the published GATA-to-TATA conversion at this exact locus. The QBiC group names a shared GATA specificity, not one TF; I pick GATA3 because an ENCODE GATA3 ChIP-seq peak in SK-N-SH contains this position (E18), GATA3 is expressed there (51.8 TPM) and the published mechanism is adrenergic-CRC dependent. Note GATA2 is also peaked (E19) and more abundant, so the choice is not settled by binding scores, which are near-identical across GATA models | weak | [E10](#e10), [E18](#e18), [E20a](#e20a), [E20b](#e20b) |
| element | The variant lies in an ENCODE distal enhancer-like cCRE (DNase z 4.5, H3K27ac z 4.0; z-scores are maxima over biosamples) in LMO1 intron 1 at a conserved base (GERP 6.43), and GATA factors are actually bound there in SK-N-SH | supported | [E03](#e03), [E01](#e01), [E18](#e18), [E19](#e19) |
| gene | The element acts on LMO1: the variant is intronic to LMO1, LMO1 is the best L2G gene (0.92; credible sets are for non-neuroblastoma traits), and published work ties this polymorphism to LMO1 expression levels | supported | [E01](#e01), [E02](#e02), [E05](#e05), [E20a](#e20a) |
| cell_type | The effect operates in GATA3-expressing adrenergic neuroblastoma cells; GATA3 is expressed in SK-N-SH and occupies the site there, and the published zebrafish work shows the allele selects which core regulatory circuit is active in tumors. Restriction to the adrenergic state is supported by the published CRC claim but not directly measured here | weak | [E10](#e10), [E18](#e18), [E20b](#e20b), [E20c](#e20c) |
| phenotype | Loss of GATA binding on the alt (A = T) allele reduces enhancer activity and LMO1 levels; genome-edited animals with the TATA allele showed reduced neuroblastoma initiation, so alt is protective and ref C confers risk | supported | [E20b](#e20b), [E20a](#e20a), [E06c](#e06c) |

Predictions: Allele-specific GATA3 ChIP reads in heterozygous neuroblastoma cells favour the C allele; GATA3 knockdown in SK-N-SH lowers LMO1 more than, or comparably to, GATA2 knockdown; Base editing C>A lowers LMO1 mRNA without changing RIC3 or TUB; Reporter allelic difference is lost in GATA3-depleted or mesenchymal (GATA3-low) cells

Falsified if: GATA3 depletion leaves LMO1 unchanged while GATA2 depletion lowers it; No allelic imbalance in GATA3 ChIP at this element; Allele swap does not change LMO1 expression

### 2. H2: Same GATA-motif disruption, but the occupying factor is GATA2, the most abundant GATA factor in this line and also ChIP-peaked at the element (p = 0.26)

TF GATA2 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E1518342 (dELS) in LMO1 intron 1; gene LMO1; cell type SK-N-SH neuroblastoma cells (GATA2 133 TPM).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The best-scoring model in the GATA group is GATA2 (z -56.07, alt binds less, ref 100th to alt 77.3rd percentile), and an ENCODE GATA2 ChIP-seq peak in SK-N-SH contains the variant. Within the shared GATA specificity I pick GATA2 on expression (133 TPM, ~2.5x GATA3) plus direct occupancy; the model z-scores cannot discriminate GATA2 from GATA3 | weak | [E10](#e10), [E19](#e19) |
| element | The disrupted site is in a DNase/H3K27ac-marked distal enhancer-like cCRE in LMO1 intron 1 with demonstrated GATA2 occupancy in SK-N-SH | supported | [E03](#e03), [E19](#e19) |
| gene | LMO1 is the dominant L2G gene (0.92) and the variant lies in its first intron; the published GATA motif is tied to LMO1 expression | supported | [E05](#e05), [E01](#e01), [E20a](#e20a) |
| cell_type | GATA2 is the dominant expressed GATA factor in this neuroblastoma line and is bound at the element there | weak | [E10](#e10), [E19](#e19) |
| phenotype | Reduced GATA2 occupancy on the alt allele lowers LMO1 enhancer output; the GATA-to-TATA allele reduced neuroblastoma initiation, so alt is protective | weak | [E20b](#e20b), [E06c](#e06c) |

Predictions: GATA2 ChIP signal at this cCRE is stronger than GATA3 signal and shows C-allele imbalance; GATA2 knockdown reduces LMO1 more than GATA3 knockdown in SK-N-SH; Allelic reporter effect persists in GATA3-low cells that retain GATA2

Falsified if: GATA2 depletion leaves LMO1 unchanged while GATA3 depletion lowers it; GATA2 peak is not allele-sensitive in heterozygous cells

### 3. H5: Null: no TF-mediated effect of this variant itself (tags a linked causal variant in the adjacent cCREs, or the signal is pleiotropic metabolic/height biology unrelated to the neuroblastoma mechanism) (p = 0.22)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-swapped isogenic neuroblastoma cells show no change in LMO1 expression, enhancer activity or GATA occupancy; Fine-mapping of neuroblastoma risk resolves to a neighbouring variant in EH38E1518343/EH38E2943027; Allelic effects track metabolic/height traits (credible sets with PIP 1.00) through another gene rather than LMO1 in neural cells

Falsified if: Single-base editing C>A alone changes LMO1 expression and GATA occupancy; MPRA shows a reproducible allelic difference for this exact 1-bp change

### 4. H3: Alt allele creates a PAR-bZIP/D-box site (DBP/TEF/NFIL3) that gains a repressive factor and lowers LMO1 (p = 0.06)

TF DBP (stated coverage own_model; registry own_model), alt allele binds more; element EH38E1518342 (dELS) in LMO1 intron 1; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | PAR-bZIP/D-box models gain binding on alt (DBP z 61.6, effect 4.82; TEF z 52.1; NFIL3 z 51.9; alt ~99.9th percentile). Within this shared bZIP specificity I now pick DBP as the strongest-scoring model that is also expressed (6.19 TPM); the choice among DBP/TEF/NFIL3 is not resolved by the evidence. This is an in vitro prediction only, with no ChIP evidence for any of these TFs here | weak | [E09](#e09), [E11](#e11), [E12](#e12) |
| element | The gained site lies in a distal enhancer-like cCRE that is demonstrably bound by TFs in SK-N-SH | weak | [E03](#e03), [E18](#e18) |
| gene | The element is intronic to LMO1, the top L2G gene | supported | [E05](#e05), [E02](#e02), [E01](#e01) |
| cell_type | DBP and related PAR-bZIPs are expressed in SK-N-SH, so a new site could be occupied there; occupancy is not shown | weak | [E09](#e09), [E11](#e11), [E12](#e12) |
| phenotype | If the gained D-box factor represses the enhancer, LMO1 falls on the alt allele, matching the protective direction; no cited evidence supports repression by these TFs at this element, and the published mechanism is GATA-motif loss | missing | [E20b](#e20b) |

Predictions: DBP/TEF/NFIL3 ChIP shows alt-specific binding at the element; Depleting PAR-bZIPs abolishes the allelic reporter difference while GATA depletion does not; Allelic effect is seen in cells lacking GATA factors

Falsified if: No PAR-bZIP occupancy at the element; Allelic reporter effect persists after DBP/TEF/NFIL3 depletion; GATA depletion alone abolishes the allelic difference

### 5. H4: Alt allele loses ZBTB18 binding, de-repressing the LMO1 intronic enhancer (direction opposite to the published effect) (p = 0.04)

TF ZBTB18 (stated coverage own_model; registry own_model), ref allele binds more; element EH38E1518342 (dELS) in LMO1 intron 1; gene LMO1; cell type SK-N-SH neuroblastoma cells (ZBTB18 17.1 TPM).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ZBTB18 own model loses binding on alt (z -31.2, effect -2.79; ref 99.4th to alt 78.4th percentile); this is a weaker signal than the GATA models and there is no ChIP evidence for ZBTB18 here | weak | [E17](#e17) |
| element | The site is in a DNase/H3K27ac-marked distal enhancer-like cCRE | weak | [E03](#e03) |
| gene | The enhancer is intronic to LMO1, the dominant L2G gene | supported | [E01](#e01), [E05](#e05) |
| cell_type | ZBTB18 is expressed in this neuroblastoma line; occupancy is not shown | weak | [E17](#e17) |
| phenotype | If ZBTB18 represses, its loss on alt would raise LMO1, the opposite of the reported protective effect of the TATA allele, so this chain is unlikely | missing | [E20b](#e20b) |

Predictions: ZBTB18 ChIP shows ref-preferential binding and ZBTB18 knockdown increases LMO1; Alt allele gives higher, not lower, enhancer activity in reporters

Falsified if: Alt allele lowers LMO1 in isogenic cells; ZBTB18 depletion does not change LMO1

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H5 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific read counts at chr11:8233861 in existing ENCODE SK-N-SH GATA3 (ENCSR000BTH) and GATA2 (ENCSR706VOO) ChIP, if the line is heterozygous | existing data | no | C-allele imbalance in GATA3 ChIP reads | C-allele imbalance in GATA2 ChIP reads (likely stronger signal) | No allelic imbalance at either ChIP | No GATA allelic imbalance required; GATA peaks allele-neutral | No GATA allelic imbalance; effect would be at a ZBTB18 site |
| siRNA/shRNA knockdown of GATA3 versus GATA2 in SK-N-SH, LMO1 mRNA by qPCR plus ChIP-qPCR at EH38E1518342 | medium | yes | GATA3 knockdown lowers LMO1 and reduces occupancy at the element; GATA2 knockdown has little effect | GATA2 knockdown lowers LMO1 and reduces occupancy; GATA3 knockdown has little effect | GATA knockdowns may change LMO1 but no allele dependence exists | Neither GATA knockdown changes LMO1 appreciably | Neither GATA knockdown changes LMO1; ZBTB18 knockdown raises it |
| MPRA or luciferase reporter of the 347 bp cCRE with C versus A allele in SK-N-SH | medium | no | A allele lower activity, GATA-dependent | A allele lower activity, GATA-dependent | No allelic difference | A allele lower activity, PAR-bZIP-dependent | A allele higher activity |
| CRISPR base editing of C>A in an isogenic adrenergic neuroblastoma line, RNA-seq for LMO1/RIC3/TUB | high | no | LMO1 down, neighbours unchanged | LMO1 down, neighbours unchanged | No change in LMO1 | LMO1 down | LMO1 up |
| PAR-bZIP (DBP/TEF/NFIL3) and ZBTB18 ChIP-qPCR at EH38E1518342 in SK-N-SH | medium | no | No specific PAR-bZIP or ZBTB18 occupancy | No specific PAR-bZIP or ZBTB18 occupancy | No allele-dependent occupancy | DBP/TEF/NFIL3 occupancy, alt-biased | ZBTB18 occupancy, ref-biased |
| LMO1 eQTL lookup for rs2168101 in neural/adrenal tissues and neuroblastoma tumours | existing data | no | A allele associated with lower LMO1 | A allele associated with lower LMO1 | No LMO1 eQTL, or effect attributable to a linked variant | A allele associated with lower LMO1 | A allele associated with higher LMO1 |

## Next experiment

Parallel siRNA knockdown of GATA3 and of GATA2 in SK-N-SH, reading out LMO1 mRNA by qPCR and GATA occupancy at EH38E1518342 by ChIP-qPCR: both factors are already shown to bind the element (E18, E19) and only a factor-specific perturbation can separate H1 from H2.

## Investigate calls

- chip_peaks({"tf": "GATA3", "biosample": "SK-N-SH"})
- chip_peaks({"tf": "GATA2", "biosample": "SK-N-SH"})
- literature_search({"query": "rs2168101 GATA LMO1 G allele risk T allele protective neuroblastoma"})

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

> QBiC-SELEX screen of chr11:8233861:C>A: 997 models scored, 334 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 227 CIS-BP groups. Expression context: DepMap line ACH-000149. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 39 (Homeodomain, 4 models z 59.17, Homeodomain, 3 models z 38.75, Homeodomain; POU, 1 model z 20.28, C2H2 ZF, 1 model z 19.82, C2H2 ZF, 1 model z -17.92). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G153 (Unknown, 1 model): best model CPEB1_NA_TAACCC20NCG_ESAC_yang2017_0_3_7mer (own model of CPEB1), z 78.94, effect 3.719 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: CPEB1 z 78.94. TFs this group covers (own and CIS-BP-mapped models): CPEB1 4.79 TPM; best model's site strength: ref 99.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G164 (bZIP, 1 model): best model DBP_NA_TGCGGG20NGGC_AE_jolma2013_0_2_7mer (own model of DBP), z 61.62, effect 4.82 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: DBP z 61.62. TFs this group covers (own and CIS-BP-mapped models): DBP 6.19 TPM; best model's site strength: ref 99.3th, alt 99.9th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G010 (GATA, 6 models): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (own model of GATA2), z -56.07, effect -0.816 (alt binds less); 6 passing models (6 with the best model's sign). Passing members: GATA2 z -56.07, GATA3 z -54.11, GATA6 z -53.73, GATA5 z -52.75, GATA1 z -49.7 (+1 more). TFs this group covers (own and CIS-BP-mapped models): GATA2 133.07 TPM, GATA3 51.82 TPM, GATA4 13.8 TPM, GATA6 0.07 TPM, GATA5 0.01 TPM, GATA1 0.0 TPM; best model's site strength: ref 100.0th, alt 77.3th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G076 (bZIP, 2 models): best model TEF_NA_TATAAG20NTA_ESQ_yang2017_0_2_7mer (own model of TEF), z 52.06, effect 2.175 (alt binds more); 2 passing models (2 with the best model's sign). Passing members: TEF z 52.06, HLF z 27.84. TFs this group covers (own and CIS-BP-mapped models): TEF 3.72 TPM, HLF 0.68 TPM; best model's site strength: ref 92.2th, alt 99.7th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G262 (bZIP, 1 model): best model NFIL3_NA_TAGACG20NCG_ESY_yang2017_0_2_7mer (own model of NFIL3), z 51.94, effect 2.575 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: NFIL3 z 51.94. TFs this group covers (own and CIS-BP-mapped models): NFIL3 8.07 TPM; best model's site strength: ref 99.4th, alt 99.8th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G589 (C2H2 ZF, 1 model): best model ZNF75A_FL_TTGCTG40NCTA_KW_yin2017_0_4_7mer (own model of ZNF75A), z 48.81, effect 1.176 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZNF75A z 48.81. TFs this group covers (own and CIS-BP-mapped models): ZNF75A 15.12 TPM, ZNF75D 3.0 TPM; best model's site strength: ref 96.4th, alt 99.9th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G004 (Homeodomain, 18 models): best model HOXC12_NA_TCATGC20NGTA_ESY_yang2017_0_4_7mer (own model of HOXC12), z 42.95, effect 2.352 (alt binds more); 18 passing models (18 with the best model's sign). Passing members: HOXC12 z 42.95, HOXC11 z 40.23, HOXD11 z 35.99, HOXC9 z 29.07, HOXC10 z 29.06 (+13 more). TFs this group covers (own and CIS-BP-mapped models): HOXD8 15.75 TPM, HOXC4 8.52 TPM, HOXD9 7.58 TPM, HOXC6 5.8 TPM, HOXC9 5.16 TPM, HOXC5 3.65 TPM, HOXD4 3.42 TPM, HOXD3 3.11 TPM, HOXC8 1.99 TPM, HOXB3 1.38 TPM (+24 more); best model's site strength: ref 91.7th, alt 99.7th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G367 (Unknown, 1 model): best model THYN1_FL_TG40NCTGTGG_YWFA_jolma2025_0_4_7mer (own model of THYN1), z -34.07, effect -0.261 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: THYN1 z -34.07. TFs this group covers (own and CIS-BP-mapped models): THYN1 40.98 TPM; best model's site strength: ref 51.4th, alt 9.7th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G418 (C2H2 ZF, 1 model): best model ZFP1_eDBD_TGAACT40NAAG_KT_yin2017_0_4_7mer (own model of ZFP1), z 31.88, effect 2.621 (alt binds more); 1 passing models (1 with the best model's sign). Passing members: ZFP1 z 31.88. TFs this group covers (own and CIS-BP-mapped models): ZFP1 9.99 TPM; best model's site strength: ref 94.2th, alt 99.8th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G393 (C2H2 ZF, 1 model): best model ZBTB18_eDBD_TACTCC40NGTA_KR_yin2017_0_3_7mer (own model of ZBTB18), z -31.2, effect -2.791 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: ZBTB18 z -31.2. TFs this group covers (own and CIS-BP-mapped models): ZBTB18 17.06 TPM; best model's site strength: ref 99.4th, alt 78.4th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:35+00:00)

> 1 ENCODE GATA3 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR000BTH.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:35+00:00)

> 1 ENCODE GATA2 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR706VOO.

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20GATA%20LMO1%20G%20allele%20risk%20T%20allele%20protective%20neuroblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:27:36+00:00)

> Europe PMC: 17 hits for 'rs2168101 GATA LMO1 G allele risk T allele protective neuroblastoma'; top 8 with PMIDs:
> PMID 38937681 (2024): LMO family gene polymorphisms and Wilms tumor susceptibility in Chinese children: a five-center case-control study.
> PMID 37183825 (2023): Genetic predisposition to neuroblastoma results from a regulatory polymorphism that promotes the adrenergic cell state.
> PMID 37183823 (2023): Back to the future: evolutionary biology reveals a key regulatory switch in neuroblastoma pathogenesis.
> PMID 37849756 (2023): Two bullets in the gun: combining immunotherapy with chemotherapy to defeat neuroblastoma by targeting adrenergic-mesenchymal plasticity.
> PMID 38653778 (2024): Lineage specific transcription factor waves reprogram neuroblastoma from self-renewal to differentiation.
> PMID 38587919 (2024): Super-enhancers: drivers of cells' identities and cells' debacles.
> PMID 33870932 (2021): LIM domain only 1: an oncogenic transcription cofactor contributing to the tumorigenesis of multiple cancer types.
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.

<a id="e20a"></a>**E20a** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T17:27:36+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e20b"></a>**E20b** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-25T17:27:36+00:00)

> Thus, conversion of the regulatory GATA to a TATA allele in the first intron of LMO1 reduced the neuroblastoma-initiation rate by preventing formation of the adrenergic cell state.

<a id="e20c"></a>**E20c** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-25T17:27:36+00:00)

> They now demonstrate experimentally, using genome-edited zebrafish, that a polymorphism in the human rs2168101 locus of the LMO1 gene determines which CRC is active in a tumor.

<a id="e20d"></a>**E20d** literature_search, Europe PMC abstract, PMID 38937681 (https://europepmc.org/article/MED/38937681; retrieved 2026-10-25T17:27:36+00:00)

> We found LMO1 rs2168101 G > T and rs11603024 C > T as well as LMO2 rs7933499 G > A were significantly associated with Wilms tumor risk.
