# rs2168101 and Neuroblastoma (LMO1)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.03 over 13 model calls; 246 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GATA2 (bound here, z -56.07); GATA3 (bound here, z -56.07); ZNF8 (bound here, z 16.02); FOXJ3 (bound here, z 14.24); GLIS3 (bound here, z 1.73, no clear allelic change); MAX (bound here, z -4.96, weak site); TEAD4 (bound here, z -4.85, weak site); YY1 (bound here, z 3.73, no clear allelic change, weak site); BACH2 (bound here, z -2.45, no clear allelic change, weak site); TSHZ2 (bound here, z -0.28, no clear allelic change, weak site). Occupancy unknown: CPEB1 (z 78.94); HOXC9 (z 40.23); HOXD9 (z 40.23); ZBTB18 (z -31.2); HOXC5 (z 29.07). Diagnostic, not shown to the model: 334 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: No TF-mediated effect of this variant on neuroblastoma (p = 0.45)

Null chain: no TF-mediated effect of this variant.

Predictions: The variant will not show a reproducible TF-dependent allelic regulatory effect that connects to LMO1 in relevant neuroblastoma cells.; The gene-level and broader trait associations will not establish a causal neuroblastoma mechanism for this variant.

Falsified if: A TF-specific perturbation reproducibly removes a variant-dependent regulatory effect, and the variant-containing element is shown to regulate LMO1 in neuroblastoma cells.

### 2. H1: Reduced GATA2 binding contributes to a possible LMO1-region regulatory effect (p = 0.23)

TF GATA2 (QBiC-SELEX coverage own_model), ref allele binds more; element cCRE EH38E1518342, an enhancer-like element containing the variant; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is occupied over the variant and highly expressed in SK-N-SH; its own QBiC-SELEX model predicts stronger binding to ref C than alt A. GATA3 is also occupied, expressed, and has its own-model prediction favoring ref, so current evidence does not identify which GATA factor, if either, mediates an effect. | supported | [E05](#e05), [E20](#e20), [E06](#e06), [E35](#e35) |
| element | The variant lies in enhancer-like cCRE EH38E1518342, but its reported activity scores are maxima across biosamples and do not establish activity in SK-N-SH. | supported | [E03](#e03) |
| gene | LMO1 is a plausible target because the variant is intronic to LMO1, the cCRE lists LMO1 nearby, and Open Targets prioritizes LMO1; no evidence directly shows this cCRE regulates LMO1 in SK-N-SH. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E16](#e16) |
| cell_type | GATA2 occupancy over the variant and high expression are reported in SK-N-SH. | supported | [E05](#e05), [E20](#e20) |
| phenotype | LMO1 has broader neuroblastoma relevance, but the evidence does not establish that this variant or a GATA2-mediated effect changes neuroblastoma risk. | weak | [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E37](#e37) |

Predictions: If this mechanism is correct, a variant-dependent regulatory readout should be reduced more by GATA2 depletion than by GATA3 depletion; the direction of the readout cannot be inferred from stronger binding alone.; The variant-containing element should show a functional connection to LMO1 in SK-N-SH for this proposed chain to hold.

Falsified if: Sensitive assays show no ref-over-alt GATA2 binding difference in SK-N-SH.; GATA2 depletion leaves the variant-dependent regulatory readout unchanged while GATA3 depletion specifically removes it.; The element is not functionally connected to LMO1 in SK-N-SH.

### 3. H2: Reduced GATA3 binding contributes to a possible LMO1-region regulatory effect (p = 0.20)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element cCRE EH38E1518342, an enhancer-like element containing the variant; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is occupied over the variant and expressed in SK-N-SH; its own QBiC-SELEX model predicts stronger binding to ref C than alt A. GATA2 is also occupied, highly expressed, and has a model prediction favoring ref, so current evidence does not identify which GATA factor, if either, mediates an effect. | supported | [E06](#e06), [E35](#e35), [E05](#e05), [E20](#e20) |
| element | The variant lies in enhancer-like cCRE EH38E1518342, but its reported activity scores are maxima across biosamples and do not establish activity in SK-N-SH. | supported | [E03](#e03) |
| gene | LMO1 is a plausible target because the variant is intronic to LMO1, the cCRE lists LMO1 nearby, and Open Targets prioritizes LMO1; no evidence directly shows this cCRE regulates LMO1 in SK-N-SH. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E16](#e16) |
| cell_type | GATA3 occupancy over the variant and expression are reported in SK-N-SH. | supported | [E06](#e06), [E35](#e35) |
| phenotype | LMO1 has broader neuroblastoma relevance, but the evidence does not establish that this variant or a GATA3-mediated effect changes neuroblastoma risk. | weak | [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E37](#e37) |

Predictions: If this mechanism is correct, a variant-dependent regulatory readout should be reduced more by GATA3 depletion than by GATA2 depletion; the direction of the readout cannot be inferred from stronger binding alone.; The variant-containing element should show a functional connection to LMO1 in SK-N-SH for this proposed chain to hold.

Falsified if: Sensitive assays show no ref-over-alt GATA3 binding difference in SK-N-SH.; GATA3 depletion leaves the variant-dependent regulatory readout unchanged while GATA2 depletion specifically removes it.; The element is not functionally connected to LMO1 in SK-N-SH.

### 4. H3: Increased FOXJ3 binding contributes to a possible LMO1-region regulatory effect (p = 0.12)

TF FOXJ3 (QBiC-SELEX coverage own_model), alt allele binds more; element cCRE EH38E1518342, an enhancer-like element containing the variant; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXJ3 is occupied over the variant and expressed in SK-N-SH; its own QBiC-SELEX model predicts stronger binding to alt A than ref C. This supports a binding prediction, not a functional effect. | supported | [E07](#e07), [E36](#e36) |
| element | The variant lies in enhancer-like cCRE EH38E1518342, but its reported activity scores are maxima across biosamples and do not establish activity in SK-N-SH. | supported | [E03](#e03) |
| gene | LMO1 is a plausible target because the variant is intronic to LMO1, the cCRE lists LMO1 nearby, and Open Targets prioritizes LMO1; no evidence directly shows this cCRE regulates LMO1 in SK-N-SH. | weak | [E01](#e01), [E02](#e02), [E03](#e03), [E16](#e16) |
| cell_type | FOXJ3 occupancy over the variant and expression are reported in SK-N-SH. | supported | [E07](#e07), [E36](#e36) |
| phenotype | LMO1 has broader neuroblastoma relevance, but the evidence does not establish that this variant or a FOXJ3-mediated effect changes neuroblastoma risk. | weak | [E18a](#e18a), [E18b](#e18b), [E18c](#e18c), [E37](#e37) |

Predictions: If this mechanism is correct, a variant-dependent regulatory readout should be reduced by FOXJ3 depletion; stronger alt binding alone does not predict the direction of the readout.; The variant-containing element should show a functional connection to LMO1 in SK-N-SH for this proposed chain to hold.

Falsified if: Sensitive assays show no alt-over-ref FOXJ3 binding difference in SK-N-SH.; FOXJ3 depletion leaves the variant-dependent regulatory readout unchanged.; The element is not functionally connected to LMO1 in SK-N-SH.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| In SK-N-SH, compare ref and alt variant-containing reporter output under control, GATA2 depletion, and GATA3 depletion; measure whether either depletion specifically removes an allelic difference. | medium | yes | No reproducible allelic reporter difference, or no selective effect of either GATA depletion. | A reproducible allelic reporter difference is preferentially reduced by GATA2 depletion. | A reproducible allelic reporter difference is preferentially reduced by GATA3 depletion. | Any allelic difference is not preferentially reduced by GATA2 or GATA3 depletion; FOXJ3 depletion would be the more relevant follow-up. |
| Measure allele-specific GATA2, GATA3, and FOXJ3 occupancy at the variant in heterozygous SK-N-SH cells. | medium | no | No reproducible allele-specific occupancy difference for a relevant candidate. | Ref-biased GATA2 occupancy is detected. | Ref-biased GATA3 occupancy is detected. | Alt-biased FOXJ3 occupancy is detected. |
| Perturb or delete cCRE EH38E1518342 in SK-N-SH and measure LMO1 expression. | medium | no | No reproducible LMO1 expression change follows cCRE perturbation. | Perturbation changes LMO1 expression; this supports an element-to-gene link but does not alone establish GATA2 mediation. | Perturbation changes LMO1 expression; this supports an element-to-gene link but does not alone establish GATA3 mediation. | Perturbation changes LMO1 expression; this supports an element-to-gene link but does not alone establish FOXJ3 mediation. |

## Next experiment

Use the same ref/alt reporter in SK-N-SH with separate GATA2 and GATA3 depletion and control conditions, then test whether either depletion selectively removes a reproducible allelic reporter difference. This is the most direct single experiment to distinguish the top two chains; binding differences alone would not establish regulatory output.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- qbic_tf_detail({"tf": "GATA3"}) for H2.binding, ran as [E35](#e35). Expected: If a GATA3-specific model independently predicts stronger binding to ref C, H2.binding gains support and H2 becomes a stronger alternative to H1; if the result only confirms the GATA2-mapped prediction or gives no clear change, H2 remains weak.
- qbic_tf_detail({"tf": "FOXJ3"}) for H3.binding, ran as [E36](#e36). Expected: If a FOXJ3-specific model supports stronger binding to alt A, H3.binding gains support; if the alt-favoring result is only from the FOXG1-mapped model or FOXJ3-specific models show no clear change, H3 remains weak.
- gene_disease({"gene": "LMO1"}) for H1.phenotype, ran as [E37](#e37). Expected: If Open Targets reports neuroblastoma-specific LMO1 association evidence, the shared LMO1-to-disease link gains support for H1 and the competing LMO1 chains; if not, that link remains weak and the null retains weight.

- Result of qbic_tf_detail({"tf":"GATA3"}): E35 reports a GATA3-specific own-model result: ref C is predicted to bind more strongly than alt A, with a detected QBiC-SELEX change. GATA3 is also occupied at the site in SK-N-SH. (as expected: yes)
- Result of qbic_tf_detail({"tf":"FOXJ3"}): E36 reports a FOXJ3-specific own-model result predicting stronger binding to alt A than ref C, with a detected QBiC-SELEX change. FOXJ3 is also occupied at the site in SK-N-SH. (as expected: yes)
- Result of gene_disease({"gene":"LMO1"}): E37 gives LMO1 an Open Targets neuroblastoma association score of 0.48, with literature and genetic-association components. This supports an LMO1-to-neuroblastoma link but does not establish this variant's mechanism or risk effect. (as expected: yes)

Chains after revision: GATA3 0.32; GATA2 0.29; null 0.28; FOXJ3 0.11. Link grades changed: H1.phenotype: weak → missing, H2.binding: weak → supported, H2.phenotype: weak → missing, H3.binding: weak → supported, H3.phenotype: weak → missing.

### Round 2

- literature_search({"query": "chr11:8233861 LMO1 neuroblastoma enhancer variant"}) for H1.gene, ran as [E38](#e38). Expected: If the literature reports variant- or element-specific functional evidence linking this region to LMO1, H1.gene strengthens; if not, the link remains indirect.
- literature_search({"query": "LMO1 enhancer neuroblastoma SK-N-SH enhancer regulation"}) for H2.gene, ran as [E39](#e39). Expected: If studies connect an enhancer in this region to LMO1 regulation in neuroblastoma cells, H2.gene strengthens; otherwise the target-gene link remains plausible but unproven.

- Result of literature_search({"query": "chr11:8233861 LMO1 neuroblastoma enhancer variant"}): E38 returned no literature hits for the query. It provides no variant- or element-specific functional evidence linking this region to LMO1. (as expected: yes)
- Result of literature_search({"query": "LMO1 enhancer neuroblastoma SK-N-SH enhancer regulation"}): E39 returned 41 hits, but none supplied evidence connecting this variant-containing cCRE to LMO1 regulation in SK-N-SH. The quoted study reports that iron chelation decreases LMO1 expression in neuroblastoma cells, which is gene-level context rather than evidence for this enhancer or variant. (as expected: yes)

Chains after revision: null 0.29; GATA2 0.27; GATA3 0.25; FOXJ3 0.14; ZNF8 0.05. Link grades changed: H1.phenotype: missing → weak, H2.phenotype: missing → weak, H3.phenotype: missing → weak, H4.binding: absent → supported, H4.cell_type: absent → supported, H4.element: absent → supported, H4.gene: absent → weak, H4.phenotype: absent → weak.

### Round 3

- literature_search({"query": "chr11:8233861 LMO1 neuroblastoma enhancer SK-N-SH reporter CRISPR regulatory variant"}) for H1.gene, ran as [E40](#e40). Expected: If the search finds direct evidence that this variant or its cCRE regulates LMO1 in neuroblastoma cells, H1.gene becomes stronger and the non-null chains rise relative to the null; if it finds evidence against that connection, H1.gene weakens and the null rises.

- Result of literature_search for direct evidence that chr11:8233861 or its cCRE regulates LMO1 in neuroblastoma cells: E40 returned 0 hits for the specified query; this search found no direct supporting evidence, but the absence of hits is not evidence against the connection. (as expected: unclear)

Chains after revision: null 0.45; GATA2 0.23; GATA3 0.20; FOXJ3 0.12. Link grades changed: H4.binding: supported → absent, H4.cell_type: supported → absent, H4.element: supported → absent, H4.gene: weak → absent, H4.phenotype: weak → absent.

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

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr11:8233861:C>A: 30 peaks contain the variant, from 22 factors in 6 biosamples. In the matching biosample SK-N-SH: 19 peaks from 15 factors. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): BNC2, EP300, MXI1, MYC, PRDM6, RCOR1, TOX2, TRIM28. Bound, expressed TFs with a binding model: 12; listed one per row: GATA2, GATA3, FOXJ3, TEAD4, MAX, YY1, GLIS3, BACH2, ZNF8, TSHZ2; also bound: NFIC, CEBPB. Bound but below 1 TPM: OSR2, SP7. Assayed with no peak here: 30 TFs in the matching biosample, 529 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATA2: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH; also in SH-SY5Y (e.g. ENCSR706VOO). 133.07 TPM in DepMap:ACH-000149 (SK-N-SH), rank 17 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATA3: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH; also in SH-SY5Y (e.g. ENCSR000BTH). 51.82 TPM in DepMap:ACH-000149 (SK-N-SH), rank 80 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXJ3: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR667WDR). 26.62 TPM in DepMap:ACH-000149 (SK-N-SH), rank 196 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TEAD4: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR000BUQ). 16.62 TPM in DepMap:ACH-000149 (SK-N-SH), rank 346 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR000BVD). 60.9 TPM in DepMap:ACH-000149 (SK-N-SH), rank 61 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> YY1: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR000BLZ). 43.79 TPM in DepMap:ACH-000149 (SK-N-SH), rank 102 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GLIS3: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR507BWM). 7.84 TPM in DepMap:ACH-000149 (SK-N-SH), rank 629 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> BACH2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR036THH). 3.54 TPM in DepMap:ACH-000149 (SK-N-SH), rank 907 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF8: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR325QLX). 2.18 TPM in DepMap:ACH-000149 (SK-N-SH), rank 1024 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TSHZ2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample SK-N-SH (e.g. ENCSR282NLQ). 2.15 TPM in DepMap:ACH-000149 (SK-N-SH), rank 1028 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs2168101&size=100; retrieved 2026-10-25T17:26:22+00:00)

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

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:15+00:00)

> 158 credible sets contain 11_8233861_C_A: 157 GWAS, 1 molecular QTL.
> GWAS Height: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Hemoglobin A1c levels: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Tyrosine levels: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Total concentration of branched-chain amino acids (leucine +: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS chloride  (minimum, inv-norm transformed): PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> GWAS Diastolic blood pressure x short total sleep time interactio: PIP 1.00; L2G LMO1 0.70, RIC3 0.06
> pqtl for CFC1 (UKB_PPP_EUR_CFC1_P0CG37_OID21261_v1): PIP 1.00
> Best L2G gene scores across these sets: LMO1 0.92, RIC3 0.08

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr11_8233861_C_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T00:40:54+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr11_8233861_C_A_b38. NES is the effect of the alt allele (A) relative to ref (C).
> LMO1 in Muscle_Skeletal: NES -0.13, p 1.6e-09

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=LMO1%20AND%20%22neuroblastoma%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:19:16+00:00)

> Europe PMC: 396 hits for 'LMO1 AND "neuroblastoma"'; top 8 with PMIDs:
> PMID 41858882 (2026): LMO1 expression in neuroblastoma cells reprograms tumor-associated macrophages to promote metastasis.
> PMID 41630162 (2026): ARX mutation-associated interneuron defects provide insights into mechanisms underlying developmental epilepsies.
> PMID 42909156 (2026): The role of personalised medicine in treating high-risk neuroblastoma in paediatric patients.
> PMID 41960368 (2026): Cellular Functional Analyses of &lt;i&gt;ARX&lt;/i&gt; Variants Reveal New Insights Into Genotype-Phenotype Correlations in Neurodevelopmental Disorders Among Male and Female Patients.
> PMID 41202161 (2026): Defining the Functional Role and Potential as an Immunotherapeutic Target of ALCAM in Neuroblastoma.
> PMID 40078563 (2025): Improving neuroblastoma risk prediction through a polygenic risk score derived from genome-wide association study-identified loci.
> PMID 40076569 (2025): Prognostic Biomarkers in Breast Cancer via Multi-Omics Clustering Analysis.
> PMID 41982370 (2026): miRNA-Processing Gene Variants and Neuroblastoma Susceptibility: A Pilot Case-Control Study.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41858882 (https://europepmc.org/article/MED/41858882; retrieved 2026-10-26T20:19:16+00:00)

> To better understand this synergy, we performed single-cell RNA sequencing analysis on primary tumors from transgenic zebrafish overexpressing MYCN alone or with LMO1.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41858882 (https://europepmc.org/article/MED/41858882; retrieved 2026-10-26T20:19:16+00:00)

> Our data suggest that LMO1 overexpression in MYCN-amplified NB cells increases the pro-metastatic properties of macrophages in the tumor-cell microenvironment, which is important for driving NB metastasis.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 40078563 (https://europepmc.org/article/MED/40078563; retrieved 2026-10-26T20:19:16+00:00)

> Fourteen loci, including ten protective polymorphisms from CASC15, BARD1, LMO1, HSD17B12, and HACE1, and four risk variants from BARD1, RSRC1, CPZ and MMP20 were significantly associated with neuroblastoma risk.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr11:8233861:C>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000149), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 12 occupied (5 with a strong site), 5 of 115 with unknown occupancy. Left out: 30 TFs assayed in the matching biosample and 529 assayed only elsewhere, none with a peak here; 2 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA2 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (its own model), z -56.07, effect -0.816: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 133.07 TPM, rank 17 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR706VOO. Best model's site strength: ref 100.0th, alt 77.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (a CIS-BP-mapped model of GATA2), z -56.07, effect -0.816: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 51.82 TPM, rank 80 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BTH. Best model's site strength: ref 100.0th, alt 77.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF8 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF8_FL_TC40NACGGGA_AATA_jolma2025_0_2_7mer (its own model), z 16.02, effect 0.286: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.18 TPM, rank 1024 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR325QLX. Best model's site strength: ref 99.2th, alt 99.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXJ3 (Forkhead, 10 models; QBiC-SELEX coverage: own model): best model FOXG1_NA_TATCTG20NTCG_ESAF_yang2017_0_4_7mer (a CIS-BP-mapped model of FOXG1), z 14.24, effect 0.65: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.62 TPM, rank 196 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR667WDR. Best model's site strength: ref 54.8th, alt 99.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GLIS3 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model GLIS3_NA_TCGCAT20NGA_O_jolma2013_0_6_6mer (its own model), z 1.73, effect 0.715: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 7.84 TPM, rank 629 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR507BWM. Best model's site strength: ref 81.2th, alt 98.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z -4.96, effect -0.274: ref allele binds more (|z| above the gate), but between weak k-mers. 60.9 TPM, rank 61 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BVD. Best model's site strength: ref 47.4th, alt 46.1th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TEAD4 (TEA, 4 models; QBiC-SELEX coverage: own model): best model TEAD4_NA_TGATTT20NTTA_ESY_yang2017_0_4_7mer (its own model), z -4.85, effect -0.29: ref allele binds more (|z| above the gate), but between weak k-mers. 16.62 TPM, rank 346 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BUQ. Best model's site strength: ref 96.8th, alt 67.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> YY1 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model YY1_FL_GG40NGTGAGA_YWKA_jolma2025_0_3_7mer (its own model), z 3.73, effect 0.326: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 43.79 TPM, rank 102 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR000BLZ. Best model's site strength: ref 88.6th, alt 92.5th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> BACH2 (bZIP, 1 model; QBiC-SELEX coverage: own model): best model BACH2_eDBD_TAGCAT40NAGG_KR_yin2017_0_3_7mer (its own model), z -2.45, effect -0.123: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 3.54 TPM, rank 907 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR036THH. Best model's site strength: ref 96.2th, alt 77.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TSHZ2 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model TSHZ2_FL_AG40NGGAATC_YWL_jolma2025_0_4_7mer (its own model), z -0.28, effect -0.022: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 2.15 TPM, rank 1028 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in SK-N-SH, e.g. ENCSR282NLQ. Best model's site strength: ref 86.8th, alt 79.7th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CPEB1 (Unknown, 1 model; QBiC-SELEX coverage: own model): best model CPEB1_NA_TAACCC20NCG_ESAC_yang2017_0_3_7mer (its own model), z 78.94, effect 3.719: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.79 TPM, rank 829 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXC9 (Homeodomain, 18 models; QBiC-SELEX coverage: own model): best model HOXC11_NA_TCACTA20NTCA_ESAC_yang2017_0_4_7mer (a CIS-BP-mapped model of HOXC11), z 40.23, effect 1.457: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 5.16 TPM, rank 797 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 92.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXD9 (Homeodomain, 18 models; QBiC-SELEX coverage: own model): best model HOXC11_NA_TCACTA20NTCA_ESAC_yang2017_0_4_7mer (a CIS-BP-mapped model of HOXC11), z 40.23, effect 1.457: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.58 TPM, rank 648 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 92.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB18 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB18_eDBD_TACTCC40NGTA_KR_yin2017_0_3_7mer (its own model), z -31.2, effect -2.791: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 17.06 TPM, rank 337 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.4th, alt 78.4th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOXC5 (Homeodomain, 18 models; QBiC-SELEX coverage: mapped models only): best model HOXC9_FL_TATGTA40NTGT_KV_yin2017_1_2_7mer (a CIS-BP-mapped model of HOXC9), z 29.07, effect 0.472: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.65 TPM, rank 899 of 1626 TFs in DepMap:ACH-000149 (SK-N-SH). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 72.2th, alt 99.9th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GATA3","symbol":"GATA3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr11:8233861:C>A","gate_p":5.02e-05,"models":[{"model":"GATA3_NA_TGTCGT20NGA_ESAC_yang2017_0_4_7mer","mapping":"own","group":"G010 GATA, 6 models","quality":0.858,"effect":-4.206,"z":-54.11,"p":0.0,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":97.4,"k":7}},{"model":"GATA1_eDBD_TTTAGA40NGGC_KN_yin2017_0_4_7mer","mapping":"CIS-BP (GATA1)","group":"G010 GATA, 6 models","quality":0.626,"effect":-5.572,"z":-49.7,"p":0.0,"rank_abs_z":"10/997","passed_gate":true,"site_strength":{"ref_percentile":99.3,"alt_percentile":78.7,"k":7}},{"model":"GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer","mapping":"CIS-BP (GATA2)","group":"G010 GATA, 6 models","quality":0.874,"effect":-0.816,"z":-56.07,"p":0.0,"rank_abs_z":"4/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":77.3,"k":7}},{"model":"GATA4_NA_TAAAAT20NAAA_Y_jolma2013_0_3_7mer","mapping":"CIS-BP (GATA4)","group":"G010 GATA, 6 models","quality":0.789,"effect":-3.553,"z":-38.66,"p":0.0,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":98.5,"k":7}},{"model":"GATA5_NA_TAAATG20NTAA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (GATA5)","group":"G010 GATA, 6 models","quality":0.882,"effect":-3.915,"z":-52.75,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":99.5,"alt_percentile":99.5,"k":7}},{"model":"GATA6_eDBD_TCCATC40NTGA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (GATA6)","group":"G010 GATA, 6 models","quality":0.937,"effect":-3.654,"z":-53.73,"p":0.0,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":95.4,"k":7}}]}

<a id="e36"></a>**E36** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"FOXJ3","symbol":"FOXJ3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr11:8233861:C>A","gate_p":5.02e-05,"models":[{"model":"FOXJ3_NA_TAAACA20NCAA_AF_jolma2013_0_3_7mer","mapping":"own","group":"G183 Forkhead, 1 model","quality":0.654,"effect":0.346,"z":9.6,"p":8.3e-22,"rank_abs_z":"109/997","passed_gate":true,"site_strength":{"ref_percentile":97.2,"alt_percentile":99.9,"k":7}},{"model":"FOXC2_eDBD_TCAGAA40NAGG_KO_yin2017_0_4_7mer","mapping":"CIS-BP (FOXC2)","group":"G007 Forkhead, 10 models","quality":0.877,"effect":0.746,"z":7.12,"p":1.1e-12,"rank_abs_z":"161/997","passed_gate":true,"site_strength":{"ref_percentile":96.7,"alt_percentile":97.1,"k":7}},{"model":"FOXD2_eDBD_TCGCCG40NTGC_KO_yin2017_0_4_7mer","mapping":"CIS-BP (FOXD2)","group":"G007 Forkhead, 10 models","quality":0.805,"effect":-0.318,"z":-3.59,"p":0.00034,"rank_abs_z":"382/997","passed_gate":false,"site_strength":{"ref_percentile":99.9,"alt_percentile":99.6,"k":7}},{"model":"FOXD3_NA_TGGGGT20NGGT_Z_jolma2013_0_3_7mer","mapping":"CIS-BP (FOXD3)","group":"G007 Forkhead, 10 models","quality":0.562,"effect":0.615,"z":9.21,"p":3.1e-20,"rank_abs_z":"115/997","passed_gate":true,"site_strength":{"ref_percentile":99.3,"alt_percentile":98.9,"k":7}},{"model":"FOXG1_NA_TATCTG20NTCG_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (FOXG1)","group":"G007 Forkhead, 10 models","quality":0.61,"effect":0.65,"z":14.24,"p":5.2e-46,"rank_abs_z":"62/997","passed_gate":true,"site_strength":{"ref_percentile":54.8,"alt_percentile":99.0,"k":7}},{"model":"FOXI1_NA_TCGGAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (FOXI1)","group":"G007 Forkhead, 10 models","quality":0.615,"effect":0.613,"z":12.23,"p":2.3e-34,"rank_abs_z":"72/997","passed_gate":true,"site_strength":{"ref_percentile":81.7,"alt_percentile":99.3,"k":7}},{"model":"FOXJ2_eDBD_TAAAGG40NGAC_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (FOXJ2)","group":"G182 Forkhead, 1 model","quality":0.921,"effect":1.038,"z":10.31,"p":6.3e-25,"rank_abs_z":"98/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":97.3,"k":7}},{"model":"FOXK1_NA_TGGGTA20NCG_ESQ_yang2017_0_4_7mer","mapping":"CIS-BP (FOXK1)","group":"G184 Forkhead, 1 model","quality":0.667,"effect":0.762,"z":7.57,"p":3.7e-14,"rank_abs_z":"146/997","passed_gate":true,"site_strength":{"ref_percentile":88.5,"alt_percentile":98.5,"k":7}},{"model":"FOXP1_eDBD_TTATGA40NCAG_KT_yin2017_0_4_7mer","mapping":"CIS-BP (FOXP1)","group":"G069 Forkhead, 2 models","quality":0.81,"effect":0.239,"z":3.44,"p":0.00058,"rank_abs_z":"400/997","passed_gate":false,"site_strength":{"ref_percentile":89.0,"alt_percentile":88.7,"k":7}},{"model":"FOXP3_FL_TCCACA40NGCC_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (FOXP3)","group":"G069 Forkhead, 2 models","quality":0.473,"effect":0.302,"z":4.81,"p":1.5e-06,"rank_abs_z":"272/997","passed_gate":true,"site_strength":{"ref_percentile":77.9,"alt_percentile":93.4,"k":7}}]}

<a id="e37"></a>**E37** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:28:30+00:00)

> Open Targets: LMO1 and neuroblastoma (MONDO_0005072), overall score 0.48; by evidence type: literature 0.91, genetic_association 0.74

<a id="e38"></a>**E38** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr11%3A8233861%20LMO1%20neuroblastoma%20enhancer%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:09:42+00:00)

> Europe PMC: 0 hits for 'chr11:8233861 LMO1 neuroblastoma enhancer variant'; top 0 with PMIDs:

<a id="e39"></a>**E39** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=LMO1%20enhancer%20neuroblastoma%20SK-N-SH%20enhancer%20regulation&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:09:42+00:00)

> Europe PMC: 41 hits for 'LMO1 enhancer neuroblastoma SK-N-SH enhancer regulation'; top 8 with PMIDs:
> PMID 41202161 (2026): Defining the Functional Role and Potential as an Immunotherapeutic Target of ALCAM in Neuroblastoma.
> PMID 42279421 (2026): Alternative Splicing of the NF-Y Subunit, NF-YA, in Neuroblastoma Phenotype Heterogeneity.
> PMID 40525640 (2025): The Non-Coding Regulatory Variant rs[masked] at chr11p11.2 Increases Neuroblastoma Risk by Affecting HSD17B12 Expression and Lipid Metabolism.
> PMID 37274289 (2023): Metastasis in neuroblastoma: the <i>MYCN</i> question.
> PMID 37849756 (2023): Two bullets in the gun: combining immunotherapy with chemotherapy to defeat neuroblastoma by targeting adrenergic-mesenchymal plasticity.
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.
> PMID 36152315 (2023): Genetic regulatory and biological implications of the 10q24.32 schizophrenia risk locus.
> PMID 35805002 (2022): Iron Chelator VLX600 Inhibits Mitochondrial Respiration and Promotes Sensitization of Neuroblastoma Cells in Nutrition-Restricted Conditions.

<a id="e39a"></a>**E39a** literature_search, Europe PMC abstract, PMID 35805002 (https://europepmc.org/article/MED/35805002; retrieved 2026-10-26T22:09:42+00:00)

> Here, we show for the first time that in neuroblastoma, iron chelator VLX600 inhibits mitochondrial respiration, decreases expression levels of MYCN/LMO1, and induces an efficient cell death regardless of MYCN status in both 2D and 3D culture conditions.

<a id="e40"></a>**E40** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr11%3A8233861%20LMO1%20neuroblastoma%20enhancer%20SK-N-SH%20reporter%20CRISPR%20regulatory%20variant&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:11:15+00:00)

> Europe PMC: 0 hits for 'chr11:8233861 LMO1 neuroblastoma enhancer SK-N-SH reporter CRISPR regulatory variant'; top 0 with PMIDs:
