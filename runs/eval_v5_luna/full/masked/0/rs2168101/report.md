# rs2168101 and Neuroblastoma (LMO1)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.03 over 13 model calls; 256 s.

Variant `chr11:8233861:C>A` (germline); expression context: DepMap:ACH-000149 (SK-N-SH).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GATA2 (bound here, z -56.07); GATA3 (bound here, z -56.07); ZNF8 (bound here, z 16.02); FOXJ3 (bound here, z 14.24); GLIS3 (bound here, z 1.73, no clear allelic change); MAX (bound here, z -4.96, weak site); TEAD4 (bound here, z -4.85, weak site); YY1 (bound here, z 3.73, no clear allelic change, weak site); BACH2 (bound here, z -2.45, no clear allelic change, weak site); TSHZ2 (bound here, z -0.28, no clear allelic change, weak site). Occupancy unknown: CPEB1 (z 78.94); HOXC9 (z 40.23); HOXD9 (z 40.23); ZBTB18 (z -31.2); HOXC5 (z 29.07). Diagnostic, not shown to the model: 334 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: Reduced GATA2 binding at an LMO1 regulatory element (p = 0.36)

TF GATA2 (QBiC-SELEX coverage own_model), ref allele binds more; element cCRE EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA2 is occupied at the variant and highly expressed in SK-N-SH; its QBiC-SELEX model predicts stronger binding to ref C than alt A. GATA3 also has occupancy and an independently supported ref-favoring prediction, so the evidence does not uniquely identify GATA2; this chain gives weight to its high expression and occupancy. | supported | [E05](#e05), [E20](#e20), [E06](#e06), [E37](#e37) |
| element | The variant lies in enhancer-like cCRE EH38E1518342, although its reported activity scores are maxima across biosamples rather than SK-N-SH-specific measurements. | supported | [E03](#e03) |
| gene | LMO1 is a plausible target because the variant is intronic and the literature places the corresponding polymorphism in an LMO1 super-enhancer that modulates LMO1 expression in cis; regulation by this particular cCRE in SK-N-SH is not established. | supported | [E01](#e01), [E03](#e03), [E16](#e16), [E39a](#e39a), [E39b](#e39b) |
| cell_type | GATA2 occupancy at the variant and high GATA2 expression are documented in SK-N-SH. | supported | [E05](#e05), [E20](#e20) |
| phenotype | The LMO1 regulatory polymorphism is linked in the literature to neuroblastoma susceptibility, but GATA2-specific mediation is unproven; LMO1 is not a CRISPR dependency in SK-N-SH. | weak | [E39a](#e39a), [E39b](#e39b), [E41](#e41) |

Predictions: Allele-specific GATA2 occupancy at the variant should be greater for C than A in SK-N-SH.; If GATA2 mediates a regulatory effect, GATA2-specific perturbation should reduce the allele-dependent enhancer-output or LMO1-expression difference; the direction of that difference is not established.

Falsified if: A sensitive allele-specific assay finds no C-over-A GATA2 occupancy difference in SK-N-SH.; GATA2-specific perturbation leaves any allele-dependent regulatory difference intact, while GATA3-specific perturbation removes it.

### 2. H2: Reduced GATA3 binding at an LMO1 regulatory element (p = 0.36)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element cCRE EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is occupied at the variant and expressed in SK-N-SH; its own QBiC-SELEX model predicts stronger binding to ref C than alt A. GATA2 has the same predicted direction and is also occupied, so the evidence does not resolve which GATA factor mediates an effect. | supported | [E06](#e06), [E37](#e37), [E05](#e05), [E20](#e20) |
| element | The variant lies in enhancer-like cCRE EH38E1518342, although its reported activity scores are maxima across biosamples rather than SK-N-SH-specific measurements. | supported | [E03](#e03) |
| gene | LMO1 is a plausible target because the variant is intronic and the literature places the corresponding polymorphism in an LMO1 super-enhancer that modulates LMO1 expression in cis; regulation by this particular cCRE in SK-N-SH is not established. | supported | [E01](#e01), [E03](#e03), [E16](#e16), [E39a](#e39a), [E39b](#e39b) |
| cell_type | GATA3 occupancy at the variant and GATA3 expression are documented in SK-N-SH. | supported | [E06](#e06), [E37](#e37) |
| phenotype | The LMO1 regulatory polymorphism is linked in the literature to neuroblastoma susceptibility, but GATA3-specific mediation is unproven; LMO1 is not a CRISPR dependency in SK-N-SH. | weak | [E39a](#e39a), [E39b](#e39b), [E41](#e41) |

Predictions: Allele-specific GATA3 occupancy at the variant should be greater for C than A in SK-N-SH.; If GATA3 mediates a regulatory effect, GATA3-specific perturbation should reduce the allele-dependent enhancer-output or LMO1-expression difference; the direction of that difference is not established.

Falsified if: A sensitive allele-specific assay finds no C-over-A GATA3 occupancy difference in SK-N-SH.; GATA3-specific perturbation leaves any allele-dependent regulatory difference intact, while GATA2-specific perturbation removes it.

### 3. H0: No TF-mediated effect of this variant on neuroblastoma (p = 0.20)

Null chain: no TF-mediated effect of this variant.

Predictions: The in-vitro binding predictions and occupancy evidence will not translate into a reproducible TF-mediated effect of this base on enhancer output or LMO1 regulation in relevant neuroblastoma cells.; The evidence will not establish a variant-specific TF mechanism for neuroblastoma susceptibility.

Falsified if: Allele-specific binding and TF-specific perturbation show that binding at this base causes a reproducible enhancer-output difference that alters LMO1 regulation in neuroblastoma cells.

### 4. H3: Alt-favoring FOXJ3 binding at an LMO1 enhancer-like element (p = 0.08)

TF FOXJ3 (QBiC-SELEX coverage own_model), alt allele binds more; element cCRE EH38E1518342; gene LMO1; cell type SK-N-SH neuroblastoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXJ3 is occupied at the variant and expressed in SK-N-SH; its own QBiC-SELEX model predicts stronger binding to alt A than ref C. This supports an allele-sensitive binding prediction, not a demonstrated regulatory effect. | supported | [E07](#e07), [E38](#e38) |
| element | The variant lies in enhancer-like cCRE EH38E1518342, although its reported activity scores are maxima across biosamples rather than SK-N-SH-specific measurements. | supported | [E03](#e03) |
| gene | LMO1 is a plausible target because the variant is intronic and the literature places the corresponding polymorphism in an LMO1 super-enhancer that modulates LMO1 expression in cis; regulation by this particular cCRE in SK-N-SH is not established. | supported | [E01](#e01), [E03](#e03), [E16](#e16), [E39a](#e39a), [E39b](#e39b) |
| cell_type | FOXJ3 occupancy at the variant and FOXJ3 expression are documented in SK-N-SH. | supported | [E07](#e07), [E38](#e38) |
| phenotype | The LMO1 regulatory polymorphism is linked in the literature to neuroblastoma susceptibility, but no evidence connects FOXJ3-mediated binding at this base to that phenotype; LMO1 is not a CRISPR dependency in SK-N-SH. | weak | [E39a](#e39a), [E39b](#e39b), [E41](#e41) |

Predictions: Allele-specific FOXJ3 occupancy at the variant should be greater for A than C in SK-N-SH.; If FOXJ3 mediates a regulatory effect, FOXJ3-specific perturbation should reduce the allele-dependent enhancer-output or LMO1-expression difference; the direction of that difference is not established.

Falsified if: A sensitive allele-specific assay finds no A-over-C FOXJ3 occupancy difference in SK-N-SH.; FOXJ3-specific perturbation leaves any allele-dependent regulatory difference intact, while a GATA-specific perturbation removes it.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H0 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GATA2 and GATA3 occupancy at the endogenous variant in SK-N-SH | medium | no | C-over-A GATA2 occupancy difference; this alone would support binding but not prove a regulatory consequence. | C-over-A GATA3 occupancy difference; this alone would support binding but not prove a regulatory consequence. | No reproducible allele-specific occupancy difference attributable to a causal TF mechanism. | No defining GATA-specific result; FOXJ3 occupancy is predicted to favor A. |
| Compare GATA2- and GATA3-specific depletion with allele-specific enhancer-reporter output, testing both variant alleles | medium | yes | GATA2 depletion, more than GATA3 depletion, reduces the allele-dependent reporter difference. | GATA3 depletion, more than GATA2 depletion, reduces the allele-dependent reporter difference. | No reproducible allele-dependent reporter difference, or no TF-specific depletion effect on such a difference. | The difference, if present, is not selectively dependent on GATA2 or GATA3; FOXJ3 perturbation would be the relevant follow-up. |
| Endogenous allele editing followed by TF perturbation and measurement of LMO1 expression in SK-N-SH | high | yes | An allele-dependent LMO1 expression difference is reduced by GATA2 perturbation. | An allele-dependent LMO1 expression difference is reduced by GATA3 perturbation. | No reproducible variant-dependent LMO1 expression difference or TF-specific effect. | An allele-dependent LMO1 expression difference is reduced by FOXJ3 perturbation. |

## Next experiment

Use a dual-allele enhancer reporter in SK-N-SH with separate GATA2 and GATA3 depletion, and compare the allele-dependent reporter difference between perturbations. This is the cheapest direct test of the leading alternatives; it would not by itself establish endogenous LMO1 regulation.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- literature_search({"query": "chr11:8233861 LMO1 neuroblastoma variant enhancer"}) for H1.gene, ran as [E35](#e35). Expected: If the literature reports this variant or its containing element directly regulating LMO1 in neuroblastoma, H1.gene strengthens and H1 rises; if results are only general LMO1 or locus associations, the link remains weak.
- gene_disease({"gene": "LMO1"}) for H1.phenotype, ran as [E36](#e36). Expected: If Open Targets reports strong neuroblastoma-specific disease evidence for LMO1, H1.phenotype gains gene-level support, though this would not establish a causal effect of this variant; weak or absent disease evidence leaves the link weak.

- Result of literature_search({"query":"chr11:8233861 LMO1 neuroblastoma variant enhancer"}): E35 returned zero hits, so no direct report connecting this variant or its containing element to LMO1 regulation in neuroblastoma was found. (as expected: yes)
- Result of gene_disease({"gene":"LMO1"}): E36 reports an overall LMO1–neuroblastoma score of 0.48, with literature and genetic-association evidence; this is gene-level context, not evidence that this variant causes disease. (as expected: unclear)

Chains after revision: GATA2 0.44; null 0.36; FOXJ3 0.12; GATA3 0.08. Link grades changed: H1.phenotype: weak → supported, H2.phenotype: weak → supported, H3.phenotype: weak → supported.

### Round 2

- qbic_tf_detail({"tf": "GATA3"}) for H2.binding, ran as [E37](#e37). Expected: If a GATA3-specific QBiC-SELEX model also predicts stronger binding to ref C, H2.binding gains support and H2 rises relative to chains relying on indirect model evidence; if no such model or prediction supports the direction, H2 remains weak.
- qbic_tf_detail({"tf": "FOXJ3"}) for H3.binding, ran as [E38](#e38). Expected: If a FOXJ3-specific QBiC-SELEX model supports stronger binding to alt A, H3.binding gains support and H3 rises; if the prediction is only from the mapped FOXG1 model or does not support that direction, H3 remains weak.
- literature_search({"query": "LMO1 enhancer variant SK-N-SH neuroblastoma allele-specific regulation"}) for H1.gene, ran as [E39](#e39). Expected: If the literature reports functional evidence connecting this variant or cCRE EH38E1518342 to LMO1 regulation in neuroblastoma cells, H1.gene gains support and H1 rises; if no such evidence is found, the gene link remains indirect.

- Result of qbic_tf_detail({"tf":"GATA3"}): E37 reports a GATA3-specific QBiC-SELEX model with a strong, significant prediction favoring ref C over alt A. This strengthens H2 relative to its prior mapped-model evidence. (as expected: yes)
- Result of qbic_tf_detail({"tf":"FOXJ3"}): E38 reports a FOXJ3-specific QBiC-SELEX model with a significant prediction favoring alt A over ref C. This strengthens H3 beyond the prior FOXG1-mapped prediction. (as expected: yes)
- Result of literature_search({"query":"LMO1 enhancer variant SK-N-SH neuroblastoma allele-specific regulation"}): E39a-b report that the neuroblastoma-associated polymorphism lies in an LMO1 super-enhancer and that differential GATA binding and direct cis modulation of LMO1 expression influence susceptibility. The result supports the variant-to-LMO1 link at the literature level, but does not identify the responsible GATA factor or establish the specific cCRE-to-LMO1 link in SK-N-SH. (as expected: yes)

Chains after revision: GATA3 0.46; GATA2 0.34; null 0.12; FOXJ3 0.08. Link grades changed: H1.gene: weak → supported, H2.binding: weak → supported, H2.gene: weak → supported, H3.binding: weak → supported, H3.gene: weak → supported.

### Round 3

- literature_search({"query": "PMID 26560027 LMO1 super-enhancer GATA2 GATA3 allele-specific binding reporter assay neuroblastoma"}) for H1.binding, ran as [E40](#e40). Expected: If the paper reports allele-specific binding or functional assays identifying GATA2 versus GATA3, that could distinguish the two leading chains and change their relative ranking; if it reports only generic GATA binding, their ranking remains unresolved.
- gene_dependency({"gene": "LMO1"}) for H1.phenotype, ran as [E41](#e41). Expected: If LMO1 shows neuroblastoma-lineage dependency, that strengthens the disease relevance of the proposed LMO1 target, though it would not establish a variant-specific mechanism; lack of dependency would weaken that downstream link.

- Result of literature_search({"query": "PMID 26560027 LMO1 super-enhancer GATA2 GATA3 allele-specific binding reporter assay neuroblastoma"}): E40 returned no hits for the targeted search; it provides no result distinguishing GATA2 from GATA3 or confirming an allele-specific functional assay. (as expected: unclear)
- Result of gene_dependency({"gene": "LMO1"}): E41 reports no LMO1 CRISPR dependency in SK-N-SH (gene effect -0.04), and 0% dependency in the peripheral nervous system lineage. (as expected: yes)

Chains after revision: GATA2 0.36; GATA3 0.36; null 0.20; FOXJ3 0.08. Link grades changed: H1.phenotype: supported → weak, H2.phenotype: supported → weak, H3.phenotype: supported → weak.

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

<a id="e35"></a>**E35** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr11%3A8233861%20LMO1%20neuroblastoma%20variant%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T23:21:56+00:00)

> Europe PMC: 0 hits for 'chr11:8233861 LMO1 neuroblastoma variant enhancer'; top 0 with PMIDs:

<a id="e36"></a>**E36** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:28:30+00:00)

> Open Targets: LMO1 and neuroblastoma (MONDO_0005072), overall score 0.48; by evidence type: literature 0.91, genetic_association 0.74

<a id="e37"></a>**E37** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GATA3","symbol":"GATA3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr11:8233861:C>A","gate_p":5.02e-05,"models":[{"model":"GATA3_NA_TGTCGT20NGA_ESAC_yang2017_0_4_7mer","mapping":"own","group":"G010 GATA, 6 models","quality":0.858,"effect":-4.206,"z":-54.11,"p":0.0,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":97.4,"k":7}},{"model":"GATA1_eDBD_TTTAGA40NGGC_KN_yin2017_0_4_7mer","mapping":"CIS-BP (GATA1)","group":"G010 GATA, 6 models","quality":0.626,"effect":-5.572,"z":-49.7,"p":0.0,"rank_abs_z":"10/997","passed_gate":true,"site_strength":{"ref_percentile":99.3,"alt_percentile":78.7,"k":7}},{"model":"GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer","mapping":"CIS-BP (GATA2)","group":"G010 GATA, 6 models","quality":0.874,"effect":-0.816,"z":-56.07,"p":0.0,"rank_abs_z":"4/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":77.3,"k":7}},{"model":"GATA4_NA_TAAAAT20NAAA_Y_jolma2013_0_3_7mer","mapping":"CIS-BP (GATA4)","group":"G010 GATA, 6 models","quality":0.789,"effect":-3.553,"z":-38.66,"p":0.0,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":99.9,"alt_percentile":98.5,"k":7}},{"model":"GATA5_NA_TAAATG20NTAA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (GATA5)","group":"G010 GATA, 6 models","quality":0.882,"effect":-3.915,"z":-52.75,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":99.5,"alt_percentile":99.5,"k":7}},{"model":"GATA6_eDBD_TCCATC40NTGA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (GATA6)","group":"G010 GATA, 6 models","quality":0.937,"effect":-3.654,"z":-53.73,"p":0.0,"rank_abs_z":"6/997","passed_gate":true,"site_strength":{"ref_percentile":100.0,"alt_percentile":95.4,"k":7}}]}

<a id="e38"></a>**E38** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"FOXJ3","symbol":"FOXJ3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr11:8233861:C>A","gate_p":5.02e-05,"models":[{"model":"FOXJ3_NA_TAAACA20NCAA_AF_jolma2013_0_3_7mer","mapping":"own","group":"G183 Forkhead, 1 model","quality":0.654,"effect":0.346,"z":9.6,"p":8.3e-22,"rank_abs_z":"109/997","passed_gate":true,"site_strength":{"ref_percentile":97.2,"alt_percentile":99.9,"k":7}},{"model":"FOXC2_eDBD_TCAGAA40NAGG_KO_yin2017_0_4_7mer","mapping":"CIS-BP (FOXC2)","group":"G007 Forkhead, 10 models","quality":0.877,"effect":0.746,"z":7.12,"p":1.1e-12,"rank_abs_z":"161/997","passed_gate":true,"site_strength":{"ref_percentile":96.7,"alt_percentile":97.1,"k":7}},{"model":"FOXD2_eDBD_TCGCCG40NTGC_KO_yin2017_0_4_7mer","mapping":"CIS-BP (FOXD2)","group":"G007 Forkhead, 10 models","quality":0.805,"effect":-0.318,"z":-3.59,"p":0.00034,"rank_abs_z":"382/997","passed_gate":false,"site_strength":{"ref_percentile":99.9,"alt_percentile":99.6,"k":7}},{"model":"FOXD3_NA_TGGGGT20NGGT_Z_jolma2013_0_3_7mer","mapping":"CIS-BP (FOXD3)","group":"G007 Forkhead, 10 models","quality":0.562,"effect":0.615,"z":9.21,"p":3.1e-20,"rank_abs_z":"115/997","passed_gate":true,"site_strength":{"ref_percentile":99.3,"alt_percentile":98.9,"k":7}},{"model":"FOXG1_NA_TATCTG20NTCG_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (FOXG1)","group":"G007 Forkhead, 10 models","quality":0.61,"effect":0.65,"z":14.24,"p":5.2e-46,"rank_abs_z":"62/997","passed_gate":true,"site_strength":{"ref_percentile":54.8,"alt_percentile":99.0,"k":7}},{"model":"FOXI1_NA_TCGGAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (FOXI1)","group":"G007 Forkhead, 10 models","quality":0.615,"effect":0.613,"z":12.23,"p":2.3e-34,"rank_abs_z":"72/997","passed_gate":true,"site_strength":{"ref_percentile":81.7,"alt_percentile":99.3,"k":7}},{"model":"FOXJ2_eDBD_TAAAGG40NGAC_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (FOXJ2)","group":"G182 Forkhead, 1 model","quality":0.921,"effect":1.038,"z":10.31,"p":6.3e-25,"rank_abs_z":"98/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":97.3,"k":7}},{"model":"FOXK1_NA_TGGGTA20NCG_ESQ_yang2017_0_4_7mer","mapping":"CIS-BP (FOXK1)","group":"G184 Forkhead, 1 model","quality":0.667,"effect":0.762,"z":7.57,"p":3.7e-14,"rank_abs_z":"146/997","passed_gate":true,"site_strength":{"ref_percentile":88.5,"alt_percentile":98.5,"k":7}},{"model":"FOXP1_eDBD_TTATGA40NCAG_KT_yin2017_0_4_7mer","mapping":"CIS-BP (FOXP1)","group":"G069 Forkhead, 2 models","quality":0.81,"effect":0.239,"z":3.44,"p":0.00058,"rank_abs_z":"400/997","passed_gate":false,"site_strength":{"ref_percentile":89.0,"alt_percentile":88.7,"k":7}},{"model":"FOXP3_FL_TCCACA40NGCC_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (FOXP3)","group":"G069 Forkhead, 2 models","quality":0.473,"effect":0.302,"z":4.81,"p":1.5e-06,"rank_abs_z":"272/997","passed_gate":true,"site_strength":{"ref_percentile":77.9,"alt_percentile":93.4,"k":7}}]}

<a id="e39"></a>**E39** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=LMO1%20enhancer%20variant%20SK-N-SH%20neuroblastoma%20allele-specific%20regulation&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T23:23:02+00:00)

> Europe PMC: 19 hits for 'LMO1 enhancer variant SK-N-SH neuroblastoma allele-specific regulation'; top 8 with PMIDs:
> PMID 40525640 (2025): The Non-Coding Regulatory Variant rs[masked] at chr11p11.2 Increases Neuroblastoma Risk by Affecting HSD17B12 Expression and Lipid Metabolism.
> PMID 36152315 (2023): Genetic regulatory and biological implications of the 10q24.32 schizophrenia risk locus.
> PMID 38542080 (2024): Super-Enhancers and Their Parts: From Prediction Efforts to Pathognomonic Status.
> PMID 37180836 (2023): Variant rs[masked] enhances ALKBH5 expression through disrupting miR-186 binding and promotes neuroblastoma progression.
> PMID 36425957 (2023): <i>CFDP1</i> is a neuroblastoma susceptibility gene that regulates transcription factors of the noradrenergic cell identity.
> PMID 33870932 (2021): LIM domain only 1: an oncogenic transcription cofactor contributing to the tumorigenesis of multiple cancer types.
> PMID 31819055 (2019): ASCL1 is a MYCN- and LMO1-dependent member of the adrenergic neuroblastoma core regulatory circuitry.
> PMID 26560027 (2015): Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism.

<a id="e39a"></a>**E39a** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T23:23:02+00:00)

> We show that SNP rs[masked] G>T is the most highly associated variant (combined P = 7.47 × 10(-29), odds ratio 0.65, 95% confidence interval 0.60-0.70), and resides in a super-enhancer defined by extensive acetylation of histone H3 lysine 27 within the first intron of LMO1.

<a id="e39b"></a>**E39b** literature_search, Europe PMC abstract, PMID 26560027 (https://europepmc.org/article/MED/26560027; retrieved 2026-10-26T23:23:02+00:00)

> These findings indicate that a recently evolved polymorphism within a super-enhancer element in the first intron of LMO1 influences neuroblastoma susceptibility through differential GATA transcription factor binding and direct modulation of LMO1 expression in cis, and this leads to an oncogenic dependency in tumour cells.

<a id="e39c"></a>**E39c** literature_search, Europe PMC abstract, PMID 31819055 (https://europepmc.org/article/MED/31819055; retrieved 2026-10-26T23:23:02+00:00)

> A heritable polymorphism within regulatory sequences of the LMO1 gene is associated with its elevated expression and increased susceptibility to develop neuroblastoma, but the oncogenic pathways downstream of the LMO1 transcriptional co-regulatory protein are unknown.

<a id="e40"></a>**E40** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMID%2026560027%20LMO1%20super-enhancer%20GATA2%20GATA3%20allele-specific%20binding%20reporter%20assay%20neuroblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T23:24:28+00:00)

> Europe PMC: 0 hits for 'PMID 26560027 LMO1 super-enhancer GATA2 GATA3 allele-specific binding reporter assay neuroblastoma'; top 0 with PMIDs:

<a id="e41"></a>**E41** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for LMO1 (0 = no effect, -1 = median common-essential; < -0.5 called dependent). SK-N-SH (ACH-000149): -0.04. Peripheral Nervous System lineage, 45 lines: median 0.01, 0% dependent. All 1183 lines: median 0.04, 0% dependent.
