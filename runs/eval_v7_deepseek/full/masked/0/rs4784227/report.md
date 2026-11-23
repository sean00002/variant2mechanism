# rs4784227 and Breast cancer (16q12)

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 19 model calls; 332 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

**Verdict: undetermined.** The null leads, but nothing tested counts against GATA3, FOXA1.

Association with the disease (not part of the verdict): GWAS Catalog found; Open Targets fine-mapping found.

Pairwise ranking (Bradley-Terry strengths): H1 0.45, H2 0.45, H4 0.09. 0 of 3 pairs came out differently in the two orders.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GATA3 (bound here, z 18.65); FOXA1 (bound here, z 15.4); NR2F2 (bound here, z 9.51); TCF7L2 (bound here, z 8.45); SPDEF (bound here, z 5.89, weak site); MAFK (bound elsewhere, z 71.57); HOMEZ (bound elsewhere, z -49.09); MNX1 (bound elsewhere, z -27.02); PITX1 (bound elsewhere, z -21.39); TFAP4 (bound elsewhere, z 19.55). Occupancy unknown: MAFA (z 71.57); MAFB (z 71.57); LHX2 (z 28.05); LHX4 (z 28.05); LMX1B (z 28.05). Diagnostic, not shown to the model: 290 of 997 models pass Bonferroni.

## Ranked chains

### 1. H4: No TF-mediated allelic effect at this base; linked or non-TF mechanism explains the GWAS signal (p = 0.44)

Null chain: no TF-mediated effect of this variant.

Predictions: Allele-specific TF ChIP and enhancer reporter assays should show no reproducible difference between ref C and alt T at this base.; The breast cancer association may be driven by a linked causal variant in the TOX3 locus or by a regulatory mechanism not mediated by a TF binding change at chr16:52565276.; GTEx v8's lack of a significant single-tissue eQTL, including in breast mammary tissue, is compatible with no simple allelic expression effect in bulk tissues.

Falsified if: A reproducible allele-specific TF occupancy difference and allele-specific enhancer activity are demonstrated at this exact base in a relevant breast cell context.; CRISPR editing of this base alone changes TOX3 expression or a breast cancer-relevant phenotype.

### 2. H1: GATA3 mediates an alt-T enhancer effect at TOX3 (p = 0.32)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR16_9QTBS / EH38E3180851 distal enhancer-like element; gene TOX3; cell type MCF-7 (DepMap ACH-000019).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is bound over the variant in MCF-7 ChIP-seq and is very highly expressed in MCF-7. QBiC-SELEX with GATA3's own model and a CIS-BP-mapped GATA2 model supports stronger alt-T binding. The ChIP evidence is peak-level occupancy, not allele-specific occupancy, so the allelic direction is inferred from in vitro binding rather than directly shown. | supported | [E04](#e04), [E06](#e06), [E20](#e20), [E35](#e35) |
| element | The variant lies in an active distal enhancer-like cCRE with DNase, H3K27ac and TF occupancy. This supports an enhancer element, but the cCRE values are maxima across biosamples and no allele-specific enhancer-activity or reporter assay at this base is cited. | weak | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | TOX3 is the nearest protein-coding gene and Open Targets credible-set L2G strongly assigns the breast cancer signal to TOX3. This is genetic target assignment plus distance, not direct enhancer-gene perturbation. GTEx v8 reports no significant single-tissue eQTL, including no significant breast mammary tissue eQTL. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E40](#e40) |
| cell_type | MCF-7 is the matching breast cancer biosample and shows GATA3 ChIP-seq occupancy over the variant with very high GATA3 expression. | supported | [E04](#e04), [E06](#e06) |
| phenotype | The T allele is strongly associated with breast cancer risk and L2G implicates TOX3, but the direction of TOX3 expression and whether GATA3 mediates the effect are not measured. GTEx v8 eQTL results are negative, and the literature is broad rather than variant-specific. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E40](#e40), [E18a](#e18a) |

Predictions: Allele-specific GATA3 ChIP in a heterozygous breast cancer cell line should show higher GATA3 occupancy on alt T than ref C.; An allele-specific enhancer reporter or MPRA should show higher activity for alt T than ref C if this is an activating GATA3-dependent enhancer.; GATA3 depletion or CRISPRi of this enhancer should reduce TOX3 expression in the relevant breast cell context.

Falsified if: No allele-specific GATA3 occupancy difference is observed at this exact base in a relevant heterozygous breast cell context.; The alt T allele does not increase enhancer activity in an allele-specific reporter, or the effect is not GATA3-dependent.; GATA3 loss does not affect this enhancer or TOX3 expression in the relevant breast cell context.

### 3. H2: FOXA1 mediates an alt-T enhancer effect at TOX3 (p = 0.24)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element ENSR16_9QTBS / EH38E3180851 distal enhancer-like element; gene TOX3; cell type MCF-7 (DepMap ACH-000019).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is bound over the variant in MCF-7 ChIP-seq and is well expressed in MCF-7. QBiC-SELEX with FOXA1's own model and a CIS-BP-mapped FOXA2 model supports stronger alt-T binding. The ChIP evidence is peak-level occupancy, not allele-specific occupancy, so the allelic direction is inferred from in vitro binding rather than directly shown. | supported | [E04](#e04), [E05](#e05), [E21](#e21), [E36](#e36) |
| element | The variant is in an active distal enhancer with open chromatin and H3K27ac, and FOXA1 is bound there in MCF-7. No allele-specific FOXA1 occupancy or allele-specific enhancer-activity assay at this base is cited. | weak | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | TOX3 is the nearest protein-coding gene and genetic credible-set mapping strongly implicates TOX3. This is L2G/distance evidence, not direct enhancer-gene perturbation. GTEx v8 reports no significant single-tissue eQTL, including no significant breast mammary tissue eQTL. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E40](#e40) |
| cell_type | MCF-7 is the matching breast cancer biosample and shows FOXA1 ChIP occupancy over the variant with high FOXA1 expression. | supported | [E04](#e04), [E05](#e05) |
| phenotype | The T allele is the breast cancer risk allele and TOX3 is the L2G target, but the direction of TOX3 expression and whether FOXA1 mediates the effect are not measured. GTEx v8 eQTL results are negative, and the literature is broad rather than variant-specific. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E40](#e40), [E18a](#e18a) |

Predictions: Allele-specific FOXA1 ChIP in a heterozygous breast cancer cell line should show higher FOXA1 occupancy on alt T than ref C.; An allele-specific enhancer reporter or MPRA should show higher activity for alt T than ref C if this is an activating FOXA1-dependent enhancer.; FOXA1 depletion should reduce accessibility or activity of this enhancer and reduce TOX3 expression if FOXA1 is the functional mediator.

Falsified if: No allele-specific FOXA1 occupancy difference is observed at this exact base in a relevant heterozygous breast cell context.; The alt T allele does not change FOXA1 occupancy or enhancer activity in breast cells.; FOXA1 depletion does not alter this enhancer or TOX3 expression.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific GATA3 ChIP-qPCR in a heterozygous breast cancer line (e.g. MCF-7 if heterozygous) | medium | yes | No reproducible allele-specific GATA3 occupancy difference. | Alt T shows higher GATA3 occupancy than ref C. | No GATA3 allele-specific difference; any FOXA1 effect would be tested separately. |
| Allele-specific FOXA1 ChIP-qPCR in a heterozygous breast cancer line | medium | no | No reproducible allele-specific FOXA1 occupancy difference. | No FOXA1 allele-specific difference; GATA3 effect would be tested separately. | Alt T shows higher FOXA1 occupancy than ref C. |
| Allele-specific enhancer reporter or MPRA for ref C versus alt T in MCF-7 breast cancer cells | medium | yes | No reproducible allele-specific enhancer activity difference. | Alt T increases enhancer activity in a GATA3-dependent manner. | Alt T increases enhancer activity in a FOXA1-dependent manner. |
| GATA3 versus FOXA1 depletion/CRISPRi followed by TOX3 expression and enhancer activity | high | yes | Neither depletion specifically changes this enhancer or TOX3 expression. | GATA3 loss reduces enhancer activity/TOX3 expression more than FOXA1 loss. | FOXA1 loss reduces enhancer activity/TOX3 expression more than GATA3 loss. |
| Existing GTEx v8 breast mammary eQTL lookup for this variant | existing data | no | No significant single-tissue eQTL is compatible with the null. | A significant TOX3 eQTL with a measurable direction would support the GATA3-enhancer model, but no significant eQTL was found. | A significant TOX3 eQTL with a measurable direction would support the FOXA1-enhancer model, but no significant eQTL was found. |

## Next experiment

The cheapest experiment that separates the top two chains is allele-specific GATA3 ChIP-qPCR in a heterozygous breast cancer line (MCF-7 if heterozygous): it directly tests whether alt T increases GATA3 occupancy at this base, distinguishing H1 from the null; FOXA1 allele-specific ChIP should be run in parallel to distinguish H2.

## Refinement rounds

Stopped: round 2 left the top chain and the grades of its links unchanged.

### Round 1

- qbic_tf_detail({"tf": "GATA3"}) for H1.binding, ran as [E35](#e35). Expected: If GATA3 has an own or better direct QBiC-SELEX model showing alt-T binding stronger at a strong site, H1.binding strengthens; if only the CIS-BP-mapped GATA2 model supports the effect, or GATA3's own model is absent/contradictory, H1.binding remains weak or falls.
- qbic_tf_detail({"tf": "FOXA1"}) for H2.binding, ran as [E36](#e36). Expected: If FOXA1 has an own or better direct QBiC-SELEX model showing alt-T binding stronger at a strong site, H2.binding strengthens and H2 may separate from H1; if only the mapped FOXA2 model supports it, or the direct model is absent/contradictory, H2.binding remains weak.
- literature_search({"query": "TOX3 enhancer GATA3 FOXA1 allele-specific breast cancer rs4784227"}) for H1.phenotype and H2.binding/phenotype, ran as [E37](#e37). Expected: If the search returns functional studies showing allele-specific GATA3 or FOXA1 occupancy, enhancer activity, or TOX3 expression direction at this TOX3 variant, the top chain can be distinguished and the phenotype link strengthened; if no variant-specific functional data are returned, the chains remain weak and the null keeps substantial weight.

- Result of qbic_tf_detail({"tf":"GATA3"}) for H1.binding: E35 shows GATA3's own QBiC-SELEX model passes the gate with alt-T binding stronger (effect 0.783, z 10.91, alt 98.0th percentile), and a CIS-BP-mapped GATA2 model also shows alt-T stronger (effect 0.283, z 18.65). ENCODE ChIP is occupancy, not allele-specific. (as expected: yes)
- Result of qbic_tf_detail({"tf":"FOXA1"}) for H2.binding: E36 shows FOXA1's own QBiC-SELEX model passes the gate with alt-T binding stronger (effect 0.314, z 9.34, alt 99.8th percentile), and a CIS-BP-mapped FOXA2 model also shows alt-T stronger (effect 0.296, z 15.4). ENCODE ChIP is occupancy, not allele-specific. (as expected: yes)
- Result of literature_search({"query":"TOX3 enhancer GATA3 FOXA1 allele-specific breast cancer rs4784227"}) for H1.phenotype and H2.binding/phenotype: E37 returns 7 broad Europe PMC hits, none providing variant-specific allele-specific GATA3/FOXA1 occupancy, enhancer activity, or TOX3 expression-direction data at this base. (as expected: yes)

Chains after revision: null 0.41; GATA3 0.30; FOXA1 0.24; NR2F2 0.05. Link grades changed: H1.binding: weak → supported, H1.element: supported → weak, H1.gene: supported → weak, H2.binding: weak → supported, H2.element: supported → weak, H2.gene: supported → weak, H3.gene: supported → weak.

### Round 2

- qbic_tf_detail({"tf": "NR2F2"}) for H3.binding, ran as [E38](#e38). Expected: If NR2F2 has its own QBiC-SELEX model with a direct alt-T binding effect, H3.binding upgrades from weak and H3 becomes more plausible; if the only allelic signal is the CIS-BP-mapped PPARG model or NR2F2 has no direct model, H3.binding stays weak and H3 remains low.
- literature_search({"query": "allele-specific TOX3 enhancer breast cancer GATA3 FOXA1 reporter MPRA"}) for H1.phenotype, ran as [E39](#e39). Expected: If a variant-specific reporter, MPRA, allele-specific ChIP, or CRISPR study at this TOX3 enhancer is found, H1.element and H1.phenotype can be upgraded and H1 may pull ahead of H2; if only general TOX3/GATA3/FOXA1 breast-cancer literature is returned, those links remain weak and the top two stay close.
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"}) for H1.gene, ran as [E40](#e40). Expected: If a breast-tissue eQTL for this variant is reported with a measurable TOX3 direction, H1.gene upgrades and the phenotype direction becomes clearer; if no significant breast eQTL is found, H1.gene remains weak and the null retains weight.

- Result of qbic_tf_detail NR2F2 for H3.binding: E38: NR2F2 has an own-model COUP-TF2 QBiC-SELEX result with effect 0.035 and z 0.85, below the gate; the only passing mapped model is ESR1 at a weak site, and a mapped FXR model is negative. The direct NR2F2 model does not support an allelic binding change at this base. (as expected: yes)
- Result of literature_search allele-specific TOX3 enhancer breast cancer GATA3 FOXA1 reporter MPRA: E39 returned only general reviews on non-coding regulatory variants and breast cancer risk loci; no variant-specific reporter, MPRA, allele-specific ChIP, or CRISPR study at this exact TOX3 enhancer base was found. (as expected: yes)
- Result of eqtl_lookup Breast - Mammary Tissue: E40 reports no significant single-tissue eQTL in Breast_Mammary_Tissue for chr16_52565276_C_T. (as expected: yes)

Chains after revision: null 0.44; GATA3 0.32; FOXA1 0.24. Link grades changed: H1.gene: weak → supported, H2.gene: weak → supported, H3.binding: weak → absent, H3.cell_type: supported → absent, H3.element: weak → absent, H3.gene: weak → absent, H3.phenotype: weak → absent.

## Flags

- quote_rejected: PMID 38902506: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:52565276-52565276:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:26:24+00:00)

> Variant chr16:52565276:C>T (GRCh38), allele string C/T
> Known IDs: rs4784227
> Most severe consequence: intron_variant
> Regulatory features: ENSR16_9QTBS enhancer
> GERP conservation score at the site: -2
> Transcript consequences: CASC16 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:51565276-53565276?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:25:47+00:00)

> 6 protein-coding genes within 1000 kb of chr16:52565276:C>T, by distance to TSS:
> TOX3: 17.5 kb from TSS (upstream, strand -1)
> CHD9NB: 487.6 kb from TSS (downstream, strand -1)
> CHD9: 489.7 kb from TSS (upstream, strand +1)
> RBL2: 868.7 kb from TSS (upstream, strand +1)
> AKTIP: 939.1 kb from TSS (downstream, strand -1)
> HNRNPA1L3: 1011.8 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:25:50+00:00)

> The variant lies in cCRE EH38E3180851 (dELS: distal enhancer-like), chr16:52565011-52565360.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3180851 dELS (contains the variant): DNase z 4.2, H3K27ac z 6.1, H3K4me3 z 1.8, CTCF z 1.9; nearby genes CASC16, TOX3, AC026462.5
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr16:52565276:C>T: 276 peaks contain the variant, from 193 factors in 7 biosamples. In the matching biosample MCF-7: 14 peaks from 9 factors. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, ARID5B, ASH2L, BCL3, CBX5, CHD4, CTBP1, DPF2, EP300, GATAD1, GZF1, HBP1 (+64 more). Bound, expressed TFs with a binding model: 95; listed one per row: FOXA1, GATA3, SPDEF, NR2F2, TCF7L2, SP1, MYBL2, MAX, JUND, RXRA; also bound: YY1, GATAD2A, ZGPAT, CREM, FOSL2, ZNF609, ZNF703, TEAD1, RXRB, FOXP4, EGR1, MEF2D, ZNF800, AHDC1, GMEB1, ZNF772, ZNF788P, HMG20B, ELF1, TRAFD1, E2F4, ELF3, RELA, MLX, TBX2, ERF, HMG20A, BHLHE40, CREB1, ZBTB7B (+55 more). Bound but below 1 TPM: DLX6, ETS1, FOXA2, FOXA3, GATA4, GFI1, HLF, HNF1A, HNF1B, HNF4A. Assayed with no peak here: 45 TFs in the matching biosample, 411 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXA1: bound here. 8 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in A549, HepG2, liver (e.g. ENCSR126YEB). 88.38 TPM in DepMap:ACH-000019 (MCF7), rank 28 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATA3: bound here. 7 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in A549, T47D (e.g. ENCSR000EWV). 346.04 TPM in DepMap:ACH-000019 (MCF7), rank 5 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SPDEF: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR042GSX). 72.51 TPM in DepMap:ACH-000019 (MCF7), rank 40 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in HepG2 (e.g. ENCSR000BUY). 38.14 TPM in DepMap:ACH-000019 (MCF7), rank 103 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000EWT). 4.89 TPM in DepMap:ACH-000019 (MCF7), rank 642 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound elsewhere. 6 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, HepG2, liver (e.g. ENCSR386YIH). 33.01 TPM in DepMap:ACH-000019 (MCF7), rank 122 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 5 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BRO). 49.2 TPM in DepMap:ACH-000019 (MCF7), rank 66 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, liver (e.g. ENCSR521IID). 76.95 TPM in DepMap:ACH-000019 (MCF7), rank 35 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUND: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, liver (e.g. ENCSR000BGK). 44.21 TPM in DepMap:ACH-000019 (MCF7), rank 83 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> RXRA: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, liver (e.g. ENCSR352QSB). 30.65 TPM in DepMap:ACH-000019 (MCF7), rank 132 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs4784227&size=100; retrieved 2026-10-25T17:26:28+00:00)

> 34 GWAS Catalog associations for rs4784227, strongest first:
> Breast cancer: p 2.0e-240, effect allele T, risk-allele frequency NR, PMID 32139696
> Postmenopausal breast cancer: p 5.0e-50, effect allele T, risk-allele frequency NR, PMID 38538606
> Breast cancer (estrogen-receptor negative): p 2.0e-26, effect allele T, risk-allele frequency 0.24, PMID 29058716
> Biological Mother:  Cancer, Breast: p 2.0e-25, effect allele C, risk-allele frequency 0.7783, PMID 39024449
> Breast cancer (estrogen-receptor positive): p 1.0e-13, effect allele T, risk-allele frequency 0.06, PMID 38741014
> Parkinson's disease: p 1.0e-10, effect allele T, risk-allele frequency 0.265, PMID 28892059
> Systolic blood pressure: p 1.0e-09, effect allele T, risk-allele frequency 0.2398, PMID 33230300
> BRCA1/2-negative high-risk breast cancer: p 2.0e-09, effect allele T, risk-allele frequency 0.26, PMID 30323354
> Pulse pressure: p 2.0e-08, effect allele T, risk-allele frequency 0.2354, PMID 33230300
> Cancer: p 3.0e-08, effect allele ?, risk-allele frequency NR, PMID 34290314

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:26:25+00:00)

> 83 credible sets contain 16_52565276_C_T: 74 GWAS, 9 molecular QTL.
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, excluding all cancers (control: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer: PIP 1.00; L2G TOX3 0.93
> GWAS Breast cancer (luminal A): PIP 1.00; L2G TOX3 0.92
> GWAS Malignant neoplasm of breast, ER-positive, excluding all can: PIP 1.00; L2G TOX3 0.92
> GWAS Breast cancer [female] (PheCode 174.1): PIP 1.00; L2G TOX3 0.92
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_spinal_cord_ensg00000285800_1_): PIP 0.07
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_hippocampus_ensg00000285800): PIP 0.06
> tuqtl for TOX3 (gtex-v10_txrev_brain_hippocampus_ensg00000103460_g): PIP 0.05
> eqtl for ENSG00000285800 (gtex-v10_ge_brain_spinal_cord_ensg00000285800): PIP 0.04
> tuqtl for TOX3 (gtex-v10_txrev_brain_substantia_nigra_ensg00000103): PIP 0.04
> eqtl for ENSG00000285800 (gtex-v10_exon_brain_hippocampus_ensg00000285800_1_): PIP 0.03
> Best L2G gene scores across these sets: TOX3 0.96

<a id="e17"></a>**E17** eqtl_lookup (tested, negative), GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> GTEx v8 tested chr16_52565276_C_T_b38: no significant single-tissue eQTL in any tissue.

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TOX3%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:25:47+00:00)

> Europe PMC: 586 hits for 'TOX3 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 41849381 (2026): A transcription regulator atlas identifies TOX3 as an Atoh1 coactivator in cerebellar development and tumorigenesis.
> PMID 41595182 (2026): Identification and Characterisation of Canine Osteosarcoma Biomarkers and Therapeutic Targets.
> PMID 41596432 (2026): Bone Metastasis in Estrogen Receptor-Positive Breast Cancer: Molecular Insights and Therapeutic Advances.
> PMID 40932605 (2025): Molecular signatures of breast cancer in the Iranian population: a review of cell growth and cell cycle regulators.
> PMID 42700350 (2026): Interactions between circular RNAs (circRNAs) and the Hippo pathway in cancer.
> PMID 41871294 (2026): A reanalysis of a genome-wide association study on breast cancer in Asian populations using the SG10K_Health reference panel for imputation: a multi-Centre case-control analysis.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-26T02:25:47+00:00)

> Key examples include promoter mutations [e.g., rs[masked] (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs[masked] (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41871294 (https://europepmc.org/article/MED/41871294; retrieved 2026-10-26T02:25:47+00:00)

> Differences in panel performance influenced association signals, including breast cancer candidate loci such as FGFR2, TOX3, and ESR1.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:52565276:C>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000019), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 95 occupied (27 with a strong site), 5 of 75 with unknown occupancy. Left out: 45 TFs assayed in the matching biosample and 411 assayed only elsewhere, none with a peak here; 22 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (a CIS-BP-mapped model of GATA2), z 18.65, effect 0.283: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 346.04 TPM, rank 5 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWV. Best model's site strength: ref 92.3th, alt 98.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXA1 (Forkhead, 4 models; QBiC-SELEX coverage: own model): best model FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer (a CIS-BP-mapped model of FOXA2), z 15.4, effect 0.296: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 88.38 TPM, rank 28 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR126YEB. Best model's site strength: ref 91.3th, alt 98.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model PPARG_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of PPARG), z 9.51, effect 0.22: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 38.14 TPM, rank 103 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000BUY. Best model's site strength: ref 95.4th, alt 97.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer (a CIS-BP-mapped model of TCF7), z 8.45, effect 0.455: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.89 TPM, rank 642 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWT. Best model's site strength: ref 81.2th, alt 97.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SPDEF (Ets, 18 models; QBiC-SELEX coverage: own model): best model ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer (a CIS-BP-mapped model of ELF1), z 5.89, effect 0.213: alt allele binds more (|z| above the gate), but between weak k-mers. 72.51 TPM, rank 40 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR042GSX. Best model's site strength: ref 79.2th, alt 76.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAFK (bZIP, 6 models; QBiC-SELEX coverage: own model): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (a CIS-BP-mapped model of MAFG), z 71.57, effect 2.788: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 16.96 TPM, rank 253 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000EEB. Best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HOMEZ (Homeodomain, 1 model; QBiC-SELEX coverage: own model): best model HOMEZ_NA_TCGATC20NTAT_ESY_yang2017_0_3_7mer (its own model), z -49.09, effect -2.698: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR117CHD. Best model's site strength: ref 99.4th, alt 89.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MNX1 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model BARHL2_NA_TATTGT20NGTG_ESAC_yang2017_0_2_7mer (a CIS-BP-mapped model of BARHL2), z -27.02, effect -0.936: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.78 TPM, rank 791 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR108MKR. Best model's site strength: ref 99.9th, alt 95.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PITX1 (Homeodomain, 11 models; QBiC-SELEX coverage: own model): best model TPRX1_DBD_TG40NGACCTT_YWCB_jolma2025_0_2_7mer (a CIS-BP-mapped model of TPRX1), z -21.39, effect -0.283: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.1 TPM, rank 702 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR374MAS. Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP4 (bHLH, 1 model; QBiC-SELEX coverage: own model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (its own model), z 19.55, effect 1.433: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.85 TPM, rank 542 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR103SZL. Best model's site strength: ref 83.4th, alt 100.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAFA (bZIP, 6 models; QBiC-SELEX coverage: own model): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (a CIS-BP-mapped model of MAFG), z 71.57, effect 2.788: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.07 TPM, rank 953 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAFB (bZIP, 6 models; QBiC-SELEX coverage: own model): best model MAFG_eDBD_TTGTTC40NAAG_KN_yin2017_0_3_7mer (a CIS-BP-mapped model of MAFG), z 71.57, effect 2.788: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.09 TPM, rank 773 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> LHX2 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model LHX8_FL_TTGCGA40NGTA_KW_yin2017_0_4_7mer (a CIS-BP-mapped model of LHX8), z 28.05, effect 2.175: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.59 TPM, rank 898 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.6th, alt 99.3th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> LHX4 (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model LHX8_FL_TTGCGA40NGTA_KW_yin2017_0_4_7mer (a CIS-BP-mapped model of LHX8), z 28.05, effect 2.175: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.58 TPM, rank 900 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.6th, alt 99.3th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> LMX1B (Homeodomain, 81 models; QBiC-SELEX coverage: own model): best model LHX8_FL_TTGCGA40NGTA_KW_yin2017_0_4_7mer (a CIS-BP-mapped model of LHX8), z 28.05, effect 2.175: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 11.66 TPM, rank 366 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.6th, alt 99.3th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GATA3","symbol":"GATA3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565276:C>T","gate_p":5.02e-05,"models":[{"model":"GATA3_NA_TGTCGT20NGA_ESAC_yang2017_0_4_7mer","mapping":"own","group":"G010 GATA, 6 models","quality":0.858,"effect":0.783,"z":10.91,"p":1.1e-27,"rank_abs_z":"65/997","passed_gate":true,"site_strength":{"ref_percentile":83.3,"alt_percentile":98.0,"k":7}},{"model":"GATA1_eDBD_TTTAGA40NGGC_KN_yin2017_0_4_7mer","mapping":"CIS-BP (GATA1)","group":"G010 GATA, 6 models","quality":0.626,"effect":1.507,"z":12.45,"p":1.3e-35,"rank_abs_z":"57/997","passed_gate":true,"site_strength":{"ref_percentile":95.2,"alt_percentile":98.2,"k":7}},{"model":"GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer","mapping":"CIS-BP (GATA2)","group":"G010 GATA, 6 models","quality":0.874,"effect":0.283,"z":18.65,"p":1.3e-77,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":92.3,"alt_percentile":98.6,"k":7}},{"model":"GATA4_NA_TAAAAT20NAAA_Y_jolma2013_0_3_7mer","mapping":"CIS-BP (GATA4)","group":"G010 GATA, 6 models","quality":0.789,"effect":0.772,"z":8.04,"p":9.1e-16,"rank_abs_z":"116/997","passed_gate":true,"site_strength":{"ref_percentile":92.0,"alt_percentile":97.4,"k":7}},{"model":"GATA5_NA_TAAATG20NTAA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (GATA5)","group":"G010 GATA, 6 models","quality":0.882,"effect":0.733,"z":7.92,"p":2.3e-15,"rank_abs_z":"117/997","passed_gate":true,"site_strength":{"ref_percentile":99.5,"alt_percentile":99.4,"k":7}},{"model":"GATA6_eDBD_TCCATC40NTGA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (GATA6)","group":"G010 GATA, 6 models","quality":0.937,"effect":0.764,"z":14.98,"p":1e-50,"rank_abs_z":"40/997","passed_gate":true,"site_strength":{"ref_percentile":97.4,"alt_percentile":98.7,"k":7}}]}

<a id="e36"></a>**E36** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"FOXA1","symbol":"FOXA1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565276:C>T","gate_p":5.02e-05,"models":[{"model":"FOXA1_FL_TCCCAT40NTGT_KX_yin2017_0_4_7mer","mapping":"own","group":"G022 Forkhead, 4 models","quality":0.775,"effect":0.314,"z":9.34,"p":9.6e-21,"rank_abs_z":"82/997","passed_gate":true,"site_strength":{"ref_percentile":99.0,"alt_percentile":99.8,"k":7}},{"model":"FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer","mapping":"CIS-BP (FOXA2)","group":"G022 Forkhead, 4 models","quality":0.83,"effect":0.296,"z":15.4,"p":1.6e-53,"rank_abs_z":"37/997","passed_gate":true,"site_strength":{"ref_percentile":91.3,"alt_percentile":98.8,"k":7}},{"model":"FOXA3_FL_TGTGGT40NGGC_KX_yin2017_0_3_7mer","mapping":"CIS-BP (FOXA3)","group":"G022 Forkhead, 4 models","quality":0.928,"effect":0.144,"z":1.85,"p":0.065,"rank_abs_z":"569/997","passed_gate":false,"site_strength":{"ref_percentile":79.5,"alt_percentile":98.7,"k":7}},{"model":"FOXB1_NA_TGAGCA30NCGA_ESAI_yang2017_0_4_7mer","mapping":"CIS-BP (FOXB1)","group":"G022 Forkhead, 4 models","quality":0.674,"effect":0.045,"z":0.7,"p":0.49,"rank_abs_z":"814/997","passed_gate":false,"site_strength":{"ref_percentile":72.5,"alt_percentile":94.6,"k":7}}]}

<a id="e37"></a>**E37** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TOX3%20enhancer%20GATA3%20FOXA1%20allele-specific%20breast%20cancer%20rs4784227&format=json&pageSize=8&resultType=core; retrieved 2026-10-28T01:06:14+00:00)

> Europe PMC: 7 hits for 'TOX3 enhancer GATA3 FOXA1 allele-specific breast cancer rs[masked]'; top 7 with PMIDs:
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 32765587 (2020): ABC-GWAS: Functional Annotation of Estrogen Receptor-Positive Breast Cancer Genetic Variants.
> PMID 30116257 (2018): Elucidating the Underlying Functional Mechanisms of Breast Cancer Susceptibility Through Post-GWAS Analyses.
> PMID 26001967 (2015): Global transcription network incorporating distal regulator binding reveals selective cooperation of cancer drivers and risk genes.
> PMID 29215763 (2018): Breast cancer: The translation of big genomic data to cancer precision medicine.
> PMID 27807102 (2016): Emergence of the Noncoding Cancer Genome: A Target of Genetic and Epigenetic Alterations.
> PMID 31911677 (2020): Fine-mapping of 150 breast cancer risk regions identifies 191 likely target genes.

<a id="e38"></a>**E38** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"NR2F2","symbol":"NR2F2","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565276:C>T","gate_p":5.02e-05,"models":[{"model":"COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer","mapping":"own","group":"G002 Nuclear receptor, 29 models","quality":0.896,"effect":0.035,"z":0.85,"p":0.4,"rank_abs_z":"783/997","passed_gate":false,"site_strength":{"ref_percentile":83.2,"alt_percentile":81.4,"k":7}},{"model":"ESR1_eDBD_TGTGGG40NAAC_KV_yin2017_0_4_7mer","mapping":"CIS-BP (ESR1)","group":"G002 Nuclear receptor, 29 models","quality":0.64,"effect":0.17,"z":4.32,"p":1.6e-05,"rank_abs_z":"270/997","passed_gate":true,"site_strength":{"ref_percentile":39.5,"alt_percentile":92.1,"k":7}},{"model":"HNF4A_NA_TGACAG20NGA_AF_jolma2013_1_3_7mer","mapping":"CIS-BP (HNF4A)","group":"G078 Nuclear receptor, 2 models","quality":0.709,"effect":0.112,"z":3.1,"p":0.002,"rank_abs_z":"378/997","passed_gate":false,"site_strength":{"ref_percentile":69.3,"alt_percentile":64.9,"k":7}},{"model":"HNF4G_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (HNF4G)","group":"G078 Nuclear receptor, 2 models","quality":0.731,"effect":-0.012,"z":-0.35,"p":0.73,"rank_abs_z":"908/997","passed_gate":false,"site_strength":{"ref_percentile":92.7,"alt_percentile":91.8,"k":7}},{"model":"Rev-ErbA-Alpha_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (NR1D1)","group":"G002 Nuclear receptor, 29 models","quality":0.72,"effect":0.064,"z":1.79,"p":0.073,"rank_abs_z":"580/997","passed_gate":false,"site_strength":{"ref_percentile":93.2,"alt_percentile":93.8,"k":7}},{"model":"NR1D2_eDBD_TGAATT40NTAA_KR_yin2017_0_3_7mer","mapping":"CIS-BP (NR1D2)","group":"G002 Nuclear receptor, 29 models","quality":0.957,"effect":-0.198,"z":-1.43,"p":0.15,"rank_abs_z":"639/997","passed_gate":false,"site_strength":{"ref_percentile":96.4,"alt_percentile":79.1,"k":7}},{"model":"NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer","mapping":"CIS-BP (NR1H3)","group":"G002 Nuclear receptor, 29 models","quality":0.832,"effect":0.049,"z":2.08,"p":0.038,"rank_abs_z":"529/997","passed_gate":false,"site_strength":{"ref_percentile":74.1,"alt_percentile":94.1,"k":7}},{"model":"FXR_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (NR1H4)","group":"G002 Nuclear receptor, 29 models","quality":0.83,"effect":-0.26,"z":-5.13,"p":2.9e-07,"rank_abs_z":"213/997","passed_gate":true,"site_strength":{"ref_percentile":86.7,"alt_percentile":83.5,"k":7}},{"model":"NR2C1_eDBD_TATTCA40NAGT_KT_yin2017_0_3_7mer","mapping":"CIS-BP (NR2C1)","group":"G002 Nuclear receptor, 29 models","quality":0.939,"effect":0.22,"z":3.33,"p":0.00085,"rank_abs_z":"355/997","passed_gate":false,"site_strength":{"ref_percentile":85.7,"alt_percentile":76.5,"k":7}}],"n_models_trimmed":21}

<a id="e39"></a>**E39** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=allele-specific%20TOX3%20enhancer%20breast%20cancer%20GATA3%20FOXA1%20reporter%20MPRA&format=json&pageSize=8&resultType=core; retrieved 2026-10-28T01:07:44+00:00)

> Europe PMC: 3 hits for 'allele-specific TOX3 enhancer breast cancer GATA3 FOXA1 reporter MPRA'; top 3 with PMIDs:
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 34741135 (2022): Functional annotation of breast cancer risk loci: current progress and future directions.
> PMID 27807102 (2016): Emergence of the Noncoding Cancer Genome: A Target of Genetic and Epigenetic Alterations.

<a id="e39a"></a>**E39a** literature_search, Europe PMC abstract, PMID 38902506 (https://europepmc.org/article/MED/38902506; retrieved 2026-10-28T01:07:44+00:00)

> Notably, new evidence shows how mutations within these regions substantially influence gene expression programs, especially in the context of cancer.

<a id="e39b"></a>**E39b** literature_search, Europe PMC abstract, PMID 38902506 (https://europepmc.org/article/MED/38902506; retrieved 2026-10-28T01:07:44+00:00)

> This review provides an overview of somatic and germline non-coding single nucleotide alterations affecting transcription factor binding sites in GREs, specifically involved in cancer biology.

<a id="e39c"></a>**E39c** literature_search, Europe PMC abstract, PMID 34741135 (https://europepmc.org/article/MED/34741135; retrieved 2026-10-28T01:07:44+00:00)

> The vast majority of credible causal variants map to noncoding DNA, implicating regulation of gene expression as the mechanism by which functional variants influence risk.

<a id="e39d"></a>**E39d** literature_search, Europe PMC abstract, PMID 27807102 (https://europepmc.org/article/MED/27807102; retrieved 2026-10-28T01:07:44+00:00)

> Recent studies have shown that cis-regulatory elements are commonly the targets of genetic and epigenetic alterations associated with aberrant gene expression in cancer.

<a id="e39e"></a>**E39e** literature_search, Europe PMC abstract, PMID 27807102 (https://europepmc.org/article/MED/27807102; retrieved 2026-10-28T01:07:44+00:00)

> This has already unmasked the positions of thousands of functional cis-regulatory elements integral to transcriptional regulation, such as enhancers, promoters, and anchors of chromatin interactions that populate the noncoding genome.

<a id="e40"></a>**E40** eqtl_lookup (tested, negative), GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> GTEx v8 tested chr16_52565276_C_T_b38: no significant single-tissue eQTL in Breast_Mammary_Tissue.
