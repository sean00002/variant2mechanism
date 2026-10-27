# rs2168101 and Neuroblastoma (LMO1)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 10 model calls; 240 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. C1: GATA2-bound LMO1 distal enhancer promotes adrenergic neuroblastoma (p = 0.75)

TF GATA2 (stated coverage not_checked; registry own_model), ref allele binds more; element dELS cCRE EH38E1518342 in LMO1 intron 1; gene LMO1; cell type adrenergic neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | On the LMO1 minus strand, plus-strand ref C corresponds to G and retains a GATA motif, whereas plus-strand alt A corresponds to T and creates TATA. GATA2 is the proposed allele-specific factor: the literature supports a GATA-to-TATA switch at this SNP affecting neuroblastoma initiation, and E07 directly reports a GATA2 ChIP-seq peak containing chr11:8233861 in SK-N-SH. This supports ref-greater GATA2 binding, though allele-specific GATA2 occupancy is not itself shown. QBiC-SELEX coverage for GATA2 was not_checked because no QBiC screen row or qbic_tf_detail lookup was provided. | weak | [E06f](#e06f), [E06g](#e06g), [E07](#e07), [E09d](#e09d) |
| element | The variant lies in distal enhancer-like cCRE EH38E1518342, a super-enhancer region in LMO1 intron 1 with DNase and H3K27ac signal. | supported | [E01](#e01), [E03](#e03), [E09c](#e09c) |
| gene | The element is proposed to regulate LMO1, the nearest protein-coding gene and the strongest L2G gene at this locus; direct enhancer-promoter contact is not provided. | weak | [E02](#e02), [E05](#e05), [E09c](#e09c) |
| cell_type | The relevant context is the adrenergic neuroblastoma state, supported by the GATA/TATA regulatory switch literature and by GATA2 ChIP-seq occupancy at the variant in SK-N-SH. | supported | [E06g](#e06g), [E06h](#e06h), [E07](#e07) |
| phenotype | The ref C/GATA allele is predicted to increase GATA2-bound LMO1 enhancer activity and LMO1 expression in adrenergic neuroblastoma cells, promoting the adrenergic state and increasing neuroblastoma initiation/risk; the alt A/TATA allele is protective. The allele direction is supported by GATA-to-TATA functional literature and allelic imbalance favoring the G-containing strand, but the GATA2-specific activity and LMO1 expression change remain inferred. | weak | [E06f](#e06f), [E06g](#e06g), [E09c](#e09c), [E09d](#e09d) |

Predictions: Allele-specific GATA2 ChIP-qPCR or ChIP-seq shows stronger GATA2 occupancy on the ref C/G-containing allele than on the alt A/T allele at EH38E1518342 in SK-N-SH or adrenergic neuroblastoma cells.; Allele-specific reporter assays show higher enhancer activity for ref C than alt A in neuroblastoma cells, and GATA2 perturbation reduces this activity.; LMO1 expression is higher with the ref C/G allele, and CRISPR editing of rs2168101 changes LMO1 expression and adrenergic-state markers.; The EH38E1518342 element contacts the LMO1 promoter in neuroblastoma cells.

Falsified if: Allele-specific GATA2 occupancy at the rs2168101-containing element is not detected in SK-N-SH or other adrenergic neuroblastoma cells.; Reporter assays or CRISPR SNP editing show no ref-vs-alt effect on LMO1 enhancer activity or LMO1 expression in neuroblastoma cells.; The element does not contact the LMO1 promoter in neuroblastoma cells.

### 2. C4: Null: no TF-mediated allelic effect at rs2168101 (p = 0.15)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific transcription-factor binding at rs2168101.; No allele-specific effect of rs2168101 on LMO1 enhancer activity or LMO1 expression.; The GWAS signal is explained by linkage disequilibrium with another causal variant, by a passenger mutation, or by no functional allelic effect at this site.

Falsified if: Allele-specific GATA2 binding at the element is demonstrated.; The ref C/G allele is shown to increase LMO1 enhancer activity and LMO1 expression in neuroblastoma cells.; Functional assays show that rs2168101 itself, rather than a linked variant, changes neuroblastoma-relevant phenotypes.

### 3. C2: Alternative GATA3-mediated LMO1 enhancer mechanism (p = 0.10)

TF GATA3 (stated coverage not_checked; registry own_model), ref allele binds more; element dELS cCRE EH38E1518342 in LMO1 intron 1; gene LMO1; cell type adrenergic neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref C/G allele retains a GATA motif and the alt A/T allele creates TATA, so a GATA-family factor is predicted to bind ref more strongly. GATA3 is proposed as an alternative GATA-family factor because the motif literature does not resolve which GATA factor binds. However, the provided GATA2 ChIP-seq peak in SK-N-SH argues more directly for GATA2, and no GATA3 expression, ChIP, or perturbation evidence is provided. QBiC-SELEX coverage for GATA3 was not_checked because no QBiC screen row or qbic_tf_detail lookup was provided. | weak | [E06f](#e06f), [E06g](#e06g) |
| element | The variant lies in the same distal enhancer-like cCRE EH38E1518342 in LMO1 intron 1. | supported | [E01](#e01), [E03](#e03) |
| gene | The enhancer is proposed to regulate LMO1, the nearest gene and top L2G gene; direct contact is not shown. | weak | [E02](#e02), [E05](#e05) |
| cell_type | The relevant context is the adrenergic neuroblastoma state, supported by the GATA/TATA switch literature, but GATA3-specific involvement is not supported. | weak | [E06g](#e06g), [E06h](#e06h) |
| phenotype | Ref C would increase GATA3-dependent LMO1 enhancer activity and LMO1 expression in adrenergic neuroblastoma cells, promoting neuroblastoma risk; alt A would be protective. This is an alternative factor hypothesis, not a directly supported GATA3 mechanism. | weak | [E06f](#e06f), [E06g](#e06g) |

Predictions: GATA3 is expressed in SK-N-SH or adrenergic neuroblastoma cells and binds the ref C/G allele more strongly than the alt A/T allele.; GATA3 knockdown or inhibition reduces LMO1 enhancer activity and LMO1 expression in neuroblastoma cells.; The ref allele increases reporter activity in a GATA3-dependent manner, while GATA2 perturbation has little effect.

Falsified if: GATA2, not GATA3, is shown to be the allele-specific factor at this element.; GATA3 is not expressed in SK-N-SH or adrenergic neuroblastoma cells, or GATA3 perturbation does not alter LMO1 enhancer activity or expression.

## Prediction matrix

| Test | Cost | Separates top two | C1 | C4 | C2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific luciferase reporter assay in SK-N-SH comparing ref C and alt A enhancer constructs | low | yes | Ref C/G enhancer construct gives higher reporter activity than alt A/T in SK-N-SH or adrenergic neuroblastoma cells. | Ref C/G and alt A/T give similar reporter activity. | Ref C/G gives higher reporter activity, but the effect is GATA3-dependent rather than GATA2-dependent. |
| Allele-specific GATA2 ChIP-qPCR or ChIP-seq at EH38E1518342 in SK-N-SH | medium | yes | GATA2 occupies the element allele-specifically, with stronger binding to the ref C/G allele. | No allele-specific GATA2 or GATA3 occupancy is detected at the element. | GATA3, not GATA2, occupies the element allele-specifically; GATA2 binding is weak or non-allelic. |
| GATA2 and GATA3 knockdown in SK-N-SH with LMO1 expression and enhancer-activity readout | medium | yes | GATA2 knockdown reduces LMO1 expression and/or enhancer activity, especially from the ref C/G allele. | Neither GATA2 nor GATA3 knockdown changes allele-specific LMO1 expression or enhancer activity. | GATA3 knockdown reduces LMO1 expression and/or enhancer activity, while GATA2 knockdown has little effect. |
| CRISPR SNP editing of rs2168101 in SK-N-SH or an adrenergic neuroblastoma model, measuring LMO1 expression and adrenergic-state markers | high | yes | CRISPR editing of rs2168101 from ref C/G to alt A/T reduces LMO1 expression and adrenergic-state markers. | CRISPR editing of rs2168101 does not change LMO1 expression or neuroblastoma-relevant phenotypes. | CRISPR editing changes LMO1 expression in a GATA3-dependent manner, with GATA2 perturbation having little effect. |
| GATA3 expression and perturbation in SK-N-SH | medium | no | GATA3 is not required for the allele-specific effect; GATA2 occupancy or perturbation explains LMO1 regulation. | No GATA-family factor shows allele-specific functional effects at this element. | GATA3 is expressed in SK-N-SH and GATA3 perturbation alters LMO1 enhancer activity or expression. |

## Next experiment

Allele-specific luciferase reporter assay in SK-N-SH comparing ref C and alt A enhancer constructs, with GATA2 perturbation as a secondary arm; this is the cheapest test that separates the top two chains C1 and C4 by asking whether rs2168101 itself confers allele-specific enhancer activity in the relevant cell context.

## Investigate calls

- chip_peaks({"tf": "GATA2", "biosample": "SK-N-SH"})
- tf_expression({"tf": "GATA3", "context": "ACH-000149"})
- literature_search({"query": "rs2168101 GATA LMO1 allele-specific reporter neuroblastoma"})

## Flags

- tool_failed: E08 tf_expression: local DepMap/GTEx lookup failed: Unknown expression context 'ACH-000149'. Use DepMap:<ModelID>, DepMap:subtype=<Oncotree subtype>, GTEx:<tissue> or none.

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

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:35+00:00)

> 1 ENCODE GATA2 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR706VOO. In other biosamples, 1 GATA2 peaks do contain the variant: SH-SY5Y (experiments ENCSR000EYB).

<a id="e08"></a>**E08** tf_expression (failed), local DepMap/GTEx (; retrieved local)

> local DepMap/GTEx lookup failed: Unknown expression context 'ACH-000149'. Use DepMap:<ModelID>, DepMap:subtype=<Oncotree subtype>, GTEx:<tissue> or none.

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20GATA%20LMO1%20allele-specific%20reporter%20neuroblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:33:41+00:00)

> Europe PMC: 9 hits for 'rs2168101 GATA LMO1 allele-specific reporter neuroblastoma'; top 8 with PMIDs:
> PMID 37183825 (2023): Genetic predisposition to neuroblastoma results from a regulatory polymorphism that promotes the adrenergic cell state.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 33870932 (2021): LIM domain only 1: an oncogenic transcription cofactor contributing to the tumorigenesis of multiple cancer types.
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.
> PMID 37180836 (2023): Variant rs8400 enhances ALKBH5 expression through disrupting miR-186 binding and promotes neuroblastoma progression.
> PMID 26560027 (2015): Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism.
> PMID 36152315 (2023): Genetic regulatory and biological implications of the 10q24.32 schizophrenia risk locus.
> PMID 29589100 (2018): Genetic susceptibility to neuroblastoma: current knowledge and future directions.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-26T00:33:41+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-26T00:33:41+00:00)

> Thus, conversion of the regulatory GATA to a TATA allele in the first intron of LMO1 reduced the neuroblastoma-initiation rate by preventing formation of the adrenergic cell state.

<a id="e09c"></a>**E09c** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T00:33:41+00:00)

> We show that SNP rs2168101 G>T is the most highly associated variant (combined P = 7.47 × 10(-29), odds ratio 0.65, 95% confidence interval 0.60-0.70), and resides in a super-enhancer defined by extensive acetylation of histone H3 lysine 27 within the first intron of LMO1.

<a id="e09d"></a>**E09d** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T00:33:41+00:00)

> We demonstrate allelic imbalance favouring the G-containing strand in tumours heterozygous for this SNP, as demonstrated both by RNA sequencing (P < 0.0001) and reporter assays (P = 0.002).

<a id="e09e"></a>**E09e** literature_search, Europe PMC abstract, PMID 33870932 (https://europepmc.org/article/MED/33870932; retrieved 2026-10-26T00:33:41+00:00)

> Studies indicated that LMO1 plays a critical oncogenic role in various types of cancers, including T-cell acute lymphoblastic leukemia, neuroblastoma, gastric cancer, lung cancer, and prostate cancer.
