# rs2168101 and Neuroblastoma (LMO1)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 9 model calls; 141 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. H1: GATA2 binds the ref allele and activates LMO1 in neuroblastoma (p = 0.45)

TF GATA2 (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E1518342 distal enhancer-like cCRE; gene LMO1; cell type Neuroblastoma cells, especially adrenergic/MYCN-amplified context; SK-N-SH is the provided expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The plus-strand ref allele C corresponds to gene-strand G and preserves a GATA motif, whereas the alt allele A corresponds to gene-strand T and a TATA-like sequence. GATA2 is prioritized as a GATA-family factor because ENCODE GATA2 ChIP-seq has a peak containing rs2168101 in SK-N-SH (E07), but this peak does not itself demonstrate allele specificity. QBiC-SELEX coverage is not_checked because no QBiC screen row or qbic_tf_detail lookup is provided. | weak | [E06f](#e06f), [E06g](#e06g), [E07](#e07) |
| element | The variant lies in EH38E1518342, a distal enhancer-like cCRE with DNase and H3K27ac signal, consistent with an active intronic enhancer element. The SCREEN z-scores are maxima across biosamples, not SK-N-SH-specific. | supported | [E03](#e03) |
| gene | This enhancer is in the LMO1 gene body about 34.9 kb from the TSS, and credible-set L2G mapping supports LMO1 as the likely target gene. | supported | [E02](#e02), [E05](#e05), [E06f](#e06f) |
| cell_type | The proposed mechanism occurs in neuroblastoma cells, where LMO1/MYCN biology is documented and GATA2 ChIP-seq occupies this region in SK-N-SH. | supported | [E06b](#e06b), [E06i](#e06i), [E07](#e07) |
| phenotype | The literature supports an allele-level GATA-versus-TATA effect at rs2168101, with the GATA/ref state associated with higher LMO1 and increased neuroblastoma risk or penetrance and the TATA/alt state protective. Attributing this phenotype specifically to GATA2 remains a mechanistic inference, not a directly demonstrated GATA2-dependent effect. | supported | [E06e](#e06e), [E06f](#e06f), [E06g](#e06g), [E06i](#e06i) |

Predictions: Allele-specific GATA2 ChIP-qPCR shows stronger GATA2 occupancy on the ref C allele than the alt A allele in SK-N-SH or another relevant neuroblastoma context.; GATA2 knockdown reduces ref-allele-dependent LMO1 enhancer activity or LMO1 expression.; The alt allele weakens GATA2-dependent LMO1 regulation and is protective.

Falsified if: Allele-specific GATA2 occupancy at rs2168101 is not detected in SK-N-SH or another relevant neuroblastoma context.; GATA2 knockdown does not reduce ref-allele-dependent LMO1 enhancer activity or LMO1 expression.; A linked variant explains the neuroblastoma association after controlling for rs2168101.

### 2. H2: GATA3 binds the ref allele and activates LMO1 in neuroblastoma (p = 0.30)

TF GATA3 (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E1518342 distal enhancer-like cCRE; gene LMO1; cell type Neuroblastoma cells, especially adrenergic/MYCN-amplified context; SK-N-SH is the provided expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref allele C preserves a GATA motif on the gene strand, and the alt allele A creates a TATA-like sequence. GATA3 is an alternative GATA-family factor because ENCODE GATA3 ChIP-seq has a peak containing rs2168101 in SK-N-SH (E08), but this peak does not demonstrate allele specificity. QBiC-SELEX coverage is not_checked because no QBiC screen row or qbic_tf_detail lookup is provided. | weak | [E06f](#e06f), [E06g](#e06g), [E08](#e08) |
| element | The variant lies in EH38E1518342, a distal enhancer-like cCRE with DNase and H3K27ac signal, consistent with an active intronic enhancer element. The SCREEN z-scores are maxima across biosamples, not SK-N-SH-specific. | supported | [E03](#e03) |
| gene | This enhancer is in the LMO1 gene body about 34.9 kb from the TSS, and credible-set L2G mapping supports LMO1 as the likely target gene. | supported | [E02](#e02), [E05](#e05), [E06f](#e06f) |
| cell_type | The proposed mechanism occurs in neuroblastoma cells, where LMO1/MYCN biology is documented and GATA3 ChIP-seq occupies this region in SK-N-SH. | supported | [E06b](#e06b), [E06i](#e06i), [E08](#e08) |
| phenotype | The literature supports an allele-level GATA-versus-TATA effect at rs2168101, with the GATA/ref state associated with higher LMO1 and increased neuroblastoma risk or penetrance and the TATA/alt state protective. Attributing this phenotype specifically to GATA3 remains a mechanistic inference, not a directly demonstrated GATA3-dependent effect. | supported | [E06e](#e06e), [E06f](#e06f), [E06g](#e06g), [E06i](#e06i) |

Predictions: Allele-specific GATA3 ChIP-qPCR shows stronger GATA3 occupancy on the ref C allele than the alt A allele in SK-N-SH or another relevant neuroblastoma context.; GATA3 knockdown reduces ref-allele-dependent LMO1 enhancer activity or LMO1 expression.; The alt allele weakens GATA3-dependent LMO1 regulation and is protective.

Falsified if: Allele-specific GATA3 occupancy at rs2168101 is not detected in SK-N-SH or another relevant neuroblastoma context.; GATA3 knockdown does not reduce ref-allele-dependent LMO1 enhancer activity or LMO1 expression.; A linked variant explains the neuroblastoma association after controlling for rs2168101.

### 3. H4: Null: linked causal variant or no TF-mediated allelic effect (p = 0.20)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs2168101 after controlling for linked variants.; The neuroblastoma association is explained by a nearby causal variant or by indirect linkage disequilibrium.; LMO1 expression changes are not attributable to this single base.

Falsified if: Allele-specific TF binding at rs2168101 is demonstrated in neuroblastoma cells after controlling for linked variants.; The variant itself is shown to alter LMO1 enhancer activity and risk after controlling for linked variants.

### 4. H3: TBP binds the protective alt allele and reduces LMO1 (p = 0.05)

TF TBP (stated coverage not_checked; registry not_in_coverage), alt allele binds more; element EH38E1518342 distal enhancer-like cCRE; gene LMO1; cell type Neuroblastoma cells, including mesenchymal-like states.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt allele A corresponds to gene-strand T and creates a TATA-like sequence, so TBP is predicted to bind the alt allele more strongly than the ref allele. This is inferred from the literature naming a protective TATA allele, not from direct TBP binding evidence. ENCODE TBP ChIP-seq has no peak containing rs2168101 in SK-N-SH, although absence can also mean no TBP experiment in that biosample. QBiC-SELEX coverage is not_checked because no QBiC screen row or qbic_tf_detail lookup is provided. | weak | [E06f](#e06f), [E06g](#e06g), [E09](#e09) |
| element | The variant lies in EH38E1518342, a distal enhancer-like cCRE with DNase and H3K27ac signal, consistent with an active intronic enhancer element. The SCREEN z-scores are maxima across biosamples, not SK-N-SH-specific. | supported | [E03](#e03) |
| gene | This enhancer is in the LMO1 gene body about 34.9 kb from the TSS, and credible-set L2G mapping supports LMO1 as the likely target gene. | supported | [E02](#e02), [E05](#e05), [E06f](#e06f) |
| cell_type | The proposed TBP/TATA-dependent effect would occur in neuroblastoma cells, where the protective TATA allele has been linked to reduced MYCN-driven tumor penetrance. Direct TBP function in SK-N-SH is not shown. | weak | [E06b](#e06b), [E06g](#e06g), [E06i](#e06i), [E09](#e09) |
| phenotype | Alt-allele TBP binding is proposed to interfere with productive enhancer activity and reduce LMO1 expression, lowering neuroblastoma risk. The literature supports the protective direction of the TATA allele, but not the TBP-specific mechanism. | weak | [E06e](#e06e), [E06f](#e06f), [E06g](#e06g) |

Predictions: TBP or a TATA-box factor occupies the alt A allele more strongly than the ref C allele.; The alt allele reduces LMO1 enhancer activity in neuroblastoma cells.; The alt allele restricts or reduces adrenergic neuroblastoma phenotypes.

Falsified if: TBP or a TATA-box factor does not show preferential alt-allele occupancy at rs2168101.; The alt allele does not reduce LMO1 enhancer activity or LMO1 expression.; GATA-factor binding and function fully explain the allelic effect.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H4 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GATA2 ChIP-qPCR at rs2168101 in SK-N-SH or another heterozygous neuroblastoma context | medium | yes | Stronger GATA2 occupancy on ref C than alt A at rs2168101. | No allele-specific GATA2 occupancy; if anything, GATA3 carries the allele effect. | No allele-specific GATA2 occupancy at rs2168101. | No allele-specific GATA2 occupancy; TBP may instead prefer alt A. |
| Allele-specific GATA3 ChIP-qPCR at rs2168101 in SK-N-SH or another heterozygous neuroblastoma context | medium | yes | No allele-specific GATA3 occupancy; GATA2 carries the allele effect. | Stronger GATA3 occupancy on ref C than alt A at rs2168101. | No allele-specific GATA3 occupancy at rs2168101. | No allele-specific GATA3 occupancy; TBP may instead prefer alt A. |
| GATA2 versus GATA3 siRNA knockdown in SK-N-SH followed by LMO1 qPCR | low | yes | GATA2 knockdown reduces LMO1 expression or enhancer activity more than GATA3 knockdown. | GATA3 knockdown reduces LMO1 expression or enhancer activity more than GATA2 knockdown. | No allele-dependent or TF-dependent change in LMO1 expression after knockdown. | Neither GATA2 nor GATA3 knockdown strongly reduces the alt-allele effect; TBP/TATA factor perturbation is more relevant. |
| Ref versus alt enhancer reporter assay in SK-N-SH | low | no | Ref C increases enhancer reporter activity. | Ref C increases enhancer reporter activity. | No allele-specific enhancer reporter difference. | Alt A reduces enhancer reporter activity or changes TATA-factor dependence. |
| Allele-specific TBP or TATA-box factor occupancy at rs2168101 | medium | no | No preferential TBP occupancy on alt A. | No preferential TBP occupancy on alt A. | No allele-specific TBP occupancy. | Preferential TBP or TATA-box factor occupancy on alt A. |
| Conditional or linkage-disequilibrium fine-mapping with allele-specific functional validation | high | no | The neuroblastoma association remains attributable to rs2168101 after controlling for linked variants. | The neuroblastoma association remains attributable to rs2168101 after controlling for linked variants. | The neuroblastoma association is explained by a linked variant rather than rs2168101 itself. | The neuroblastoma association remains attributable to rs2168101 after controlling for linked variants. |

## Next experiment

GATA2 versus GATA3 siRNA knockdown in SK-N-SH followed by LMO1 qPCR is the cheapest experiment that separates the top two chains H1 and H2: H1 predicts the GATA2 knockdown effect, whereas H2 predicts the GATA3 knockdown effect.

## Investigate calls

- chip_peaks({"tf": "GATA2", "biosample": "SK-N-SH"})
- chip_peaks({"tf": "GATA3", "biosample": "SK-N-SH"})
- chip_peaks({"tf": "TBP", "biosample": "SK-N-SH"})

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

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:35+00:00)

> 1 ENCODE GATA2 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR706VOO. In other biosamples, 1 GATA2 peaks do contain the variant: SH-SY5Y (experiments ENCSR000EYB).

<a id="e08"></a>**E08** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:35+00:00)

> 1 ENCODE GATA3 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR000BTH. In other biosamples, 1 GATA3 peaks do contain the variant: SH-SY5Y (experiments ENCSR000EXZ).

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T01:37:35+00:00)

> No ENCODE TBP ChIP-seq peak contains chr11:8233861:C>A in biosamples matching 'SK-N-SH'. Absence can also mean no TBP experiment in that biosample. 0 peaks lie within 100 bp without containing it.
