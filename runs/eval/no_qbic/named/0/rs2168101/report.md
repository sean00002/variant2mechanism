# rs2168101 and Neuroblastoma (LMO1)

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.51 over 8 model calls; 153 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## Ranked chains

### 1. H1: Ref C (G on the LMO1 sense strand) keeps an intact GATA motif bound by GATA3 in SK-N-SH, sustaining LMO1 expression in the adrenergic state (p = 0.47)

TF GATA3 (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E1518342 (dELS) in LMO1 intron 1, chr11:8233740-8234086; gene LMO1; cell type Adrenergic-state neuroblastoma / sympathoadrenal neuroblast (SK-N-SH).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The variant falls inside a GATA motif in LMO1 intron 1 (E06a/E09a); the reference C on the plus strand is G on the LMO1 sense strand, keeping the canonical GATA intact, while the alt A gives a TATA-type allele (E09b), so a GATA factor binds the reference allele more. Within the GATA binding-specificity group I pick GATA3 because an ENCODE GATA3 ChIP-seq peak in SK-N-SH (and in SH-SY5Y) contains this exact base (E07); no QBiC-SELEX row or qbic_tf_detail lookup for GATA3 was provided, so coverage is not_checked. The ref>alt direction is inferred from the motif conversion, not from measured allelic binding. | weak | [E06a](#e06a), [E09a](#e09a), [E09b](#e09b), [E07](#e07), [E01](#e01) |
| element | The base lies in a distal enhancer-like cCRE (EH38E1518342; DNase z 4.5, H3K27ac z 4.0, maxima across biosamples) at a highly conserved position (GERP 6.43); the GATA3 peak in SK-N-SH indicates the element is occupied in this cell line. | supported | [E03](#e03), [E01](#e01), [E07](#e07) |
| gene | The enhancer acts on LMO1: the variant is intronic to LMO1 (nearest TSS 34.9 kb) and L2G gives LMO1 0.92 vs RIC3 0.08; the literature ties this SNP to LMO1 expression levels. | supported | [E01](#e01), [E02](#e02), [E05](#e05), [E06a](#e06a) |
| cell_type | The effect is cell-state dependent: genome-edited zebrafish show the allele determines which core regulatory circuit is active, and the adrenergic state is the permissive one; SK-N-SH carries the GATA3 occupancy (E07). | weak | [E09b](#e09b), [E09c](#e09c), [E07](#e07) |
| phenotype | GATA-allele-driven LMO1 expression promotes the adrenergic state and neuroblastoma initiation, so the TATA (alt A) allele is protective; the quote states that converting GATA to TATA reduced neuroblastoma initiation. | supported | [E09b](#e09b), [E06a](#e06a), [E06c](#e06c) |

Predictions: Allele-specific GATA3 ChIP or EMSA at chr11:8233861 shows higher occupancy on C(ref); CRISPR conversion C>A in an adrenergic line lowers LMO1 mRNA and enhancer reporter output; GATA3 knockdown reduces LMO1 preferentially in C/C cells; QBiC-SELEX GATA3 (own model or CIS-BP-mapped GATA) predicts a large ref>alt score

Falsified if: No allele-specific GATA3 binding at this base; Single-base editing leaves LMO1 unchanged in adrenergic cells; GATA3 depletion does not affect the element's activity while another factor does

### 2. H4: Null: rs2168101 has no TF-mediated effect of its own; association reflects a linked variant or non-TF pleiotropy (p = 0.27)

Null chain: no TF-mediated effect of this variant.

Predictions: Editing only chr11:8233861 changes neither LMO1 expression nor reporter activity; Allele-specific effects track a linked variant in adjacent, equally active cCREs (EH38E1518343, EH38E2943027); The GATA3 peak (E07) is unchanged in height between alleles in heterozygous cells; The dominant GWAS signals here (amino acids, height, glucose; no neuroblastoma association shown in E04/E05) are driven by a different causal base or a non-TF mechanism

Falsified if: Single-base editing alters LMO1 expression or enhancer reporter output; Allele-specific GATA occupancy is demonstrated at this exact base

### 3. H2: Same GATA element, but GATA2 is the functionally dominant GATA factor in this context (p = 0.20)

TF GATA2 (stated coverage not_checked; registry own_model), ref allele binds more; element EH38E1518342 (dELS) in LMO1 intron 1; gene LMO1; cell type Sympathetic neuroblast lineage / neuroblastoma (SK-N-SH).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The motif changed is a GATA site (E06a/E09a/E09b) and all GATA factors share one binding specificity, so motif data cannot resolve the family member. GATA2 is chosen within the group on expression: it is at 133 TPM in SK-N-SH, rank 17 of 1626 TFs and the 97.3th percentile across DepMap lines (E08). The ENCODE peak at this base is a GATA3 experiment (E07), so direct occupancy evidence favours GATA3; GATA2 would have to co-occupy or compete. Coverage not_checked (no QBiC row or lookup). | weak | [E08](#e08), [E06a](#e06a), [E09b](#e09b), [E07](#e07) |
| element | The same distal enhancer-like cCRE with strong DNase/H3K27ac at a conserved base (GERP 6.43) is the element. | supported | [E03](#e03), [E01](#e01) |
| gene | LMO1 is the regulated gene: intronic location and L2G 0.92 vs RIC3 0.08. | supported | [E01](#e01), [E05](#e05) |
| cell_type | High GATA2 levels specifically in this neuroblastoma line make the element's output lineage-restricted; the allele-dependent circuit choice was shown in edited zebrafish. | weak | [E08](#e08), [E09c](#e09c) |
| phenotype | Loss of GATA binding on the alt (TATA) allele lowers LMO1 and reduces neuroblastoma initiation, matching LMO1 variants being reported as protective. | weak | [E09b](#e09b), [E06c](#e06c) |

Predictions: GATA2 ChIP-seq in SK-N-SH shows a peak at this element at least as strong as GATA3's; GATA2 knockdown reduces LMO1 more than GATA3 knockdown; Allelic GATA2 occupancy (C>A) is detectable in heterozygous cells

Falsified if: GATA2 ChIP shows no peak at EH38E1518342; GATA3 depletion alone abolishes the allelic LMO1 difference while GATA2 depletion does not

### 4. H3: The alt A allele creates a TATA-type element that recruits a different factor and actively represses/retargets the enhancer, rather than merely losing GATA binding (p = 0.06)

TF TBP (stated coverage not_checked; registry not_in_coverage), alt allele binds more; element EH38E1518342 (dELS) in LMO1 intron 1; gene LMO1; cell type Neuroblastoma cells of either state (SK-N-SH).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The cited mechanism describes conversion of the regulatory GATA allele to a 'TATA' allele (E09b); under this chain the alt A allele gains binding for a TATA-box-binding factor (TBP) rather than simply losing GATA. No motif scan, SELEX or ChIP row supports TBP occupancy here, so this binding claim is speculative; coverage not_checked. | missing | [E09b](#e09b) |
| element | The site is an active distal enhancer-like cCRE whose output could be redirected by a gained core-promoter-type element. | weak | [E03](#e03) |
| gene | Whatever factor binds, the element's target remains LMO1 (intronic, L2G 0.92). | supported | [E01](#e01), [E05](#e05) |
| cell_type | Allele-dependent circuit choice was shown in edited zebrafish, implying the effect is read out in neuroblastoma-competent cells. | weak | [E09c](#e09c) |
| phenotype | If the alt allele gains a repressive/retargeting element, LMO1 stays low and neuroblastoma initiation is reduced, the same net protective direction. | weak | [E09b](#e09b), [E06c](#e06c) |

Predictions: A TATA-box/TBP footprint or peak appears only on the A allele; Reporter assays show the A allele has activity below a motif-deleted control (active repression, not just loss); GATA3/GATA2 depletion does not fully equalise the two alleles

Falsified if: A-allele reporter activity equals a motif-scrambled control (pure loss of function); No new factor binds the A allele in footprinting or ChIP

## Prediction matrix

| Test | Cost | Separates top two | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| qbic_tf_detail lookup for GATA3 and GATA2 (own model vs mapped vs not in coverage) and predicted ref/alt binding score at chr11:8233861 | existing data | no | GATA model predicts large ref>alt loss of binding; GATA3 covered by own or mapped model | Little or no predicted binding change at this base | Same ref>alt GATA score (family specificity shared, so this cannot separate GATA3 from GATA2) | GATA score drops but a TATA-type gain is also predicted for other models |
| GATA2 ChIP-seq (or re-analysis of existing GATA2 data) in SK-N-SH at EH38E1518342 | low | yes | No or weak GATA2 peak; GATA3 peak dominates (E07) | Peaks present but not allele-dependent | Clear GATA2 peak at the element, comparable to or stronger than GATA3 | Either GATA peak present on ref; new factor on alt |
| Allele-specific ChIP (GATA3 and GATA2) in a heterozygous C/A neuroblastoma line | medium | yes | GATA3 reads strongly biased to C; GATA2 bias absent or secondary | No allelic imbalance for either factor | GATA2 reads strongly biased to C, exceeding GATA3 bias | Modest GATA bias plus a new alt-specific footprint |
| siRNA/degron knockdown of GATA3 vs GATA2 in SK-N-SH, measuring LMO1 mRNA | medium | yes | GATA3 loss lowers LMO1 more | LMO1 may change but independent of this base | GATA2 loss lowers LMO1 more | Neither fully explains allelic difference |
| CRISPR single-base conversion C>A at chr11:8233861 plus LMO1 qPCR and luciferase reporter of both alleles | high | no | LMO1 and reporter drop on A, to about the level of a motif-scrambled control | No change in LMO1 or reporter activity | Same drop on A (direction identical to H1) | A-allele activity falls below the scrambled control (active repression) |
| eQTL lookup for rs2168101 and LMO1 in neural/adrenal tissue with allele direction | existing data | no | C allele associated with higher LMO1 | No LMO1 eQTL, or signal colocalises with a linked variant | C allele associated with higher LMO1 (same direction) | C higher, with larger-than-additive loss on A |

## Next experiment

Re-analyse or run GATA2 ChIP-seq in SK-N-SH and ask whether a peak covers chr11:8233861 at EH38E1518342; ENCODE already shows a GATA3 peak there (E07), so a GATA2 peak absent or much weaker favours H1 while a comparable or stronger GATA2 peak favours H2. This is the cheapest test separating the top two chains.

## Investigate calls

- chip_peaks({"tf": "GATA3", "biosample": "SK-N-SH"})
- tf_expression({"tf": "GATA2", "context": "DepMap:ACH-000149"})
- literature_search({"query": "rs2168101 LMO1 GATA motif G allele risk neuroblastoma"})

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

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:27:35+00:00)

> 1 ENCODE GATA3 ChIP-seq peaks contain chr11:8233861:C>A in biosamples matching 'SK-N-SH': biosamples SK-N-SH; experiments ENCSR000BTH. In other biosamples, 1 GATA3 peaks do contain the variant: SH-SY5Y (experiments ENCSR000EXZ).

<a id="e08"></a>**E08** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> GATA2 in DepMap line ACH-000149: 133.07 TPM, rank 17 of 1626 TFs (1 = highest); this context is at the 97.3th percentile of GATA2 across all DepMap lines.

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs2168101%20LMO1%20GATA%20motif%20G%20allele%20risk%20neuroblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:15:36+00:00)

> Europe PMC: 14 hits for 'rs2168101 LMO1 GATA motif G allele risk neuroblastoma'; top 8 with PMIDs:
> PMID 38937681 (2024): LMO family gene polymorphisms and Wilms tumor susceptibility in Chinese children: a five-center case-control study.
> PMID 37183825 (2023): Genetic predisposition to neuroblastoma results from a regulatory polymorphism that promotes the adrenergic cell state.
> PMID 37183823 (2023): Back to the future: evolutionary biology reveals a key regulatory switch in neuroblastoma pathogenesis.
> PMID 38653778 (2024): Lineage specific transcription factor waves reprogram neuroblastoma from self-renewal to differentiation.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 38587919 (2024): Super-enhancers: drivers of cells' identities and cells' debacles.
> PMID 33870932 (2021): LIM domain only 1: an oncogenic transcription cofactor contributing to the tumorigenesis of multiple cancer types.
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-26T00:15:36+00:00)

> Both LMO1 expression levels and the risk of developing neuroblastoma in children are associated with a single nucleotide polymorphism, G/T, that affects a GATA motif in the first intron of LMO1.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 37183825 (https://europepmc.org/article/MED/37183825; retrieved 2026-10-26T00:15:36+00:00)

> Thus, conversion of the regulatory GATA to a TATA allele in the first intron of LMO1 reduced the neuroblastoma-initiation rate by preventing formation of the adrenergic cell state.

<a id="e09c"></a>**E09c** literature_search, Europe PMC abstract, PMID 37183823 (https://europepmc.org/article/MED/37183823; retrieved 2026-10-26T00:15:36+00:00)

> They now demonstrate experimentally, using genome-edited zebrafish, that a polymorphism in the human rs2168101 locus of the LMO1 gene determines which CRC is active in a tumor.
