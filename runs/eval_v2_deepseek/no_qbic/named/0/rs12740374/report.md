# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 8 model calls; 151 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. CEBPA_alt: Alt T strengthens CEBPA binding at a SORT1 enhancer (p = 0.62)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in an active distal enhancer-like cCRE (dELS) that is occupied by CEBPA in HepG2.; gene SORT1; cell type Liver/hepatocyte-line context; HepG2 ChIP is a proxy for Hep 3B2.1-7, where CEBPA is highly expressed..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA is the best-supported C/EBP-family candidate at this element: it is occupied at the variant-containing element in HepG2 (E04), is highly expressed in the exact DepMap context Hep 3B2.1-7 (E20), and C/EBP allele-specific SORT1 enhancer literature is indexed by the E19 search. Alt T is proposed to strengthen CEBPA binding based on C/EBP-site literature/motif logic. No QBiC-SELEX model for CEBPA is supplied, so this allele-specific direction is not directly measured by the provided evidence. | weak | [E04](#e04), [E19](#e19), [E20](#e20) |
| element | The variant sits in cCRE EH38E1374646, a dELS with DNase/H3K27ac/H3K4me3 signal, and CEBPA is among the bound factors at this active element. E03 z-scores are maxima over ENCODE biosamples, not HepG2-specific. | supported | [E03](#e03), [E04](#e04) |
| gene | Alt T is associated with higher SORT1 expression in liver (NES +1.27, p 3.1e-54), and SORT1 has the strongest L2G support at this locus (0.99). This supports SORT1 as a target gene with the stated direction, though not CEBPA mediation. | supported | [E16](#e16), [E17](#e17) |
| cell_type | CEBPA is expressed at 141.33 TPM in Hep 3B2.1-7 (rank 18/1626 TFs; 99.2th percentile), and the ENCODE ChIP evidence is from the liver-cancer-line proxy HepG2; liver SORT1 eQTLs support the liver context. | supported | [E04](#e04), [E17](#e17), [E20](#e20) |
| phenotype | Most strongest GWAS lipid rows report G as the high-cholesterol risk allele, while alt T increases SORT1 in liver; if increased SORT1 lowers LDL cholesterol, T would be protective. One LDL row reports effect allele T, so the GWAS direction is not fully uniform. E18 provides literature titles, not quoted functional experiments. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E18](#e18) |

Predictions: Allele-specific CEBPA ChIP-qPCR or EMSA will show stronger CEBPA binding on alt T than ref G.; A SORT1 enhancer reporter in liver cells will be more active with alt T than ref G.; CEBPA knockdown/knockout will attenuate the alt-T effect on SORT1 expression.

Falsified if: Allele-specific CEBPA binding at rs12740374 is not stronger on alt T than ref G in hepatocyte/liver-cell assays.; CEBPA loss-of-function does not attenuate the alt-T effect on SORT1 expression.; The variant effect on SORT1 is fully explained by a linked variant or by another TF.

### 2. null_no_tf: No TF-mediated effect; linked causal variant, CELSR2 UTR effect, or passenger explanation (p = 0.24)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding or enhancer activity will be found at chr1:109274968 after controlling for linked variants.; The causal variant will lie elsewhere in the same credible set, in another nearby cCRE, or the signal will reflect a CELSR2 UTR/transcript effect rather than a TF-mediated enhancer effect.

Falsified if: A validated allele-specific TF binding or enhancer-activity difference at this exact base is demonstrated.; The SORT1/LDL association is shown to be caused by rs12740374 itself rather than a linked variant.

### 3. CEBPA_alt_CELSR2: Alt T strengthens CEBPA binding and raises CELSR2 (p = 0.08)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element The variant lies in an active dELS and is also annotated as a CELSR2 3_prime_UTR_variant, so the same enhancer/UTR region could influence CELSR2.; gene CELSR2; cell type Liver/hepatocyte-line context; HepG2 ChIP is a proxy for Hep 3B2.1-7, where CEBPA is highly expressed..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA is occupied at the variant-containing element in HepG2, is highly expressed in Hep 3B2.1-7, and C/EBP allele-specific SORT1-enhancer literature is indexed by the E19 search. Alt T is proposed to strengthen CEBPA binding. No QBiC-SELEX model for CEBPA is supplied, so the direction is inferred rather than directly measured here. | weak | [E04](#e04), [E19](#e19), [E20](#e20) |
| element | The variant lies in an active dELS (E03) and is also annotated as a CELSR2 3_prime_UTR_variant (E01), so CELSR2 is a plausible target of the same regulatory region. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | Alt T is associated with higher CELSR2 expression in liver (NES +1.04, p 9.4e-34), and CELSR2 has high L2G support (0.96-0.98). This supports CELSR2 as a target gene with the stated direction, though not CEBPA mediation. | supported | [E16](#e16), [E17](#e17) |
| cell_type | CEBPA is highly expressed in Hep 3B2.1-7, HepG2 ChIP provides liver-cell occupancy, and CELSR2 eQTLs are observed in liver. | supported | [E04](#e04), [E17](#e17), [E20](#e20) |
| phenotype | Alt T increases CELSR2 in liver, and CELSR2 is genetically associated with lipid traits. The phenotype direction is inferential because E18 supplies titles, not quoted functional experiments, and the GWAS lipid direction in E15 is not fully uniform. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E18](#e18) |

Predictions: Allele-specific CEBPA ChIP or EMSA will show stronger binding on alt T than ref G.; A CELSR2 3'UTR/enhancer reporter will show an alt-T effect in liver cells.; CEBPA loss-of-function will attenuate the alt-T effect on CELSR2 expression.

Falsified if: Allele-specific CEBPA binding at rs12740374 is not stronger on alt T than ref G.; CEBPA loss-of-function does not attenuate the alt-T effect on CELSR2 expression.; CELSR2 expression is unaffected by the variant after controlling for linked variants.

### 4. FOXA1_repressor: Ref G-bound FOXA1 represses SORT1 (p = 0.06)

TF FOXA1 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant lies in an active dELS occupied by FOXA1.; gene SORT1; cell type Liver/hepatocyte-line context; FOXA1 is expressed in Hep 3B2.1-7 and bound in HepG2..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies the variant-containing element in HepG2 and is highly expressed in the exact DepMap context Hep 3B2.1-7 (53.15 TPM; rank 84/1626). Ref G is proposed to bind FOXA1 more strongly, but no QBiC-SELEX model for FOXA1 is supplied and no allele-specific FOXA1 ChIP/EMSA is provided. | weak | [E05](#e05) |
| element | The variant lies in an active dELS (E03), and FOXA1 ChIP-seq peaks contain the variant in HepG2 (E05). | supported | [E03](#e03), [E05](#e05) |
| gene | If ref G-bound FOXA1 represses SORT1, loss of FOXA1 binding on alt T would derepress SORT1, matching the alt-T-associated increase in liver SORT1 expression. No perturbation evidence shows FOXA1 represses SORT1. | missing | [E17](#e17) |
| cell_type | FOXA1 is expressed in Hep 3B2.1-7 and bound in HepG2; SORT1 eQTLs are seen in liver. | supported | [E05](#e05), [E17](#e17) |
| phenotype | Higher SORT1 from alt T is proposed to lower LDL cholesterol and MI risk, opposite to the high-cholesterol risk association of G. The phenotype direction remains inferential because E18 gives titles, not quoted functional experiments, and E15 has one LDL row with effect allele T. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E18](#e18) |

Predictions: Allele-specific FOXA1 ChIP or EMSA will show stronger binding on ref G than alt T.; FOXA1 depletion will increase SORT1 expression if FOXA1 is a repressor at this element.; FOXA1 loss-of-function will attenuate the variant effect on SORT1 if FOXA1 mediates it.

Falsified if: FOXA1 binding at the variant is not stronger on ref G than alt T.; FOXA1 knockdown reduces rather than increases SORT1 expression.; No FOXA1-dependent effect on SORT1 is observed.

## Prediction matrix

| Test | Cost | Separates top two | CEBPA_alt | null_no_tf | CEBPA_alt_CELSR2 | FOXA1_repressor |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CEBPA binding by EMSA or ChIP-qPCR at rs12740374 in HepG2/Hep 3B2.1-7 cells | low | yes | alt T > ref G for CEBPA binding | no allele-specific CEBPA binding | alt T > ref G for CEBPA binding | no required CEBPA allele effect; FOXA1 itself is predicted ref G > alt T |
| Allele-specific FOXA1 binding by EMSA or ChIP-qPCR at rs12740374 | low | no | no required FOXA1 allele-specific effect | no allele-specific FOXA1 binding | no required FOXA1 allele-specific effect | ref G > alt T for FOXA1 binding |
| SORT1 enhancer reporter or endogenous SORT1 expression with ref vs alt enhancer in liver cells | medium | yes | alt T increases SORT1 enhancer activity/expression | no variant effect on SORT1 after controlling linked variants | little or no primary SORT1 effect; CELSR2 is the primary target | alt T increases SORT1 via loss of FOXA1 repression |
| CEBPA knockdown/knockout followed by allele-specific SORT1 expression measurement | medium | yes | CEBPA loss attenuates alt-T-induced SORT1 expression | no CEBPA-dependent effect on SORT1 | CEBPA loss attenuates CELSR2 but not primarily SORT1 induction | CEBPA loss does not attenuate SORT1; FOXA1 loss increases SORT1 |
| CELSR2 3'UTR/enhancer reporter or endogenous CELSR2 expression with ref vs alt | medium | no | no primary CELSR2 effect, or weaker than SORT1 | no variant effect on CELSR2 after controlling linked variants | alt T increases CELSR2 expression or 3'UTR reporter activity | no specific CELSR2 prediction |

## Next experiment

Cheapest test separating the top two chains (CEBPA_alt vs null_no_tf): allele-specific CEBPA binding by EMSA with HepG2/Hep 3B2.1-7 nuclear extract and CEBPA antibody supershift, using ref-G and alt-T oligos around rs12740374. Stronger alt-T binding supports CEBPA_alt; no allele-specific CEBPA binding supports the null.

## Investigate calls

- literature_search({"query": "rs12740374 C/EBP SORT1 enhancer allele-specific binding LDL"})
- tf_expression({"tf": "CEBPA", "context": "DepMap:ACH-000625"})
- gene_disease({"gene": "SORT1"})

## Flags

- quote_rejected: PMID 42019808: not an exact substring of the abstract
- quote_rejected: PMID 39858645: not an exact substring of the abstract
- tool_failed: E21 gene_disease: Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/1:109274968-109274968:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T18:05:00+00:00)

> Variant chr1:109274968:G>T (GRCh38), allele string G/T
> Known IDs: rs12740374
> Most severe consequence: 3_prime_UTR_variant
> Regulatory features: ENSR1_CDSQQ enhancer
> GERP conservation score at the site: -0.782
> Transcript consequences: CELSR2 (3_prime_UTR_variant); PSRC1 (downstream_gene_variant); CELSR2 (downstream_gene_variant); CELSR2 (non_coding_transcript_exon_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/1:108274968-110274968?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T18:05:25+00:00)

> 41 protein-coding genes within 1000 kb of chr1:109274968:G>T, by distance to TSS:
> PSRC1: 9.1 kb from TSS (downstream, strand -1)
> CELSR2: 25.4 kb from TSS (in gene body, strand +1)
> MYBPHL: 32.2 kb from TSS (downstream, strand -1)
> SARS1: 61.1 kb from TSS (downstream, strand +1)
> SORT1: 123.0 kb from TSS (downstream, strand -1)
> PSMA5: 151.5 kb from TSS (downstream, strand -1)
> CFAP276: 161.1 kb from TSS (upstream, strand -1)
> ELAPOR1: 161.8 kb from TSS (downstream, strand +1)
> TMEM167B: 184.6 kb from TSS (downstream, strand +1)
> SYPL2: 191.6 kb from TSS (upstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:28:56+00:00)

> The variant lies in cCRE EH38E1374646 (dELS: distal enhancer-like), chr1:109274794-109275142.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E1374646 dELS (contains the variant): DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 4.2, CTCF z 1.9; nearby genes CELSR2, PSRC1, MYBPHL
> EH38E2829474 dELS: DNase z 3.2, H3K27ac z 4.8, H3K4me3 z 4.4, CTCF z 1.9; nearby genes CELSR2, PSRC1, MYBPHL
> EH38E2829475 dELS: DNase z 4.6, H3K27ac z 4.5, H3K4me3 z 3.7, CTCF z 1.6; nearby genes CELSR2, PSRC1, MYBPHL
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr1:109274968:G>T: 501 peaks contain the variant, from 261 factors in 25 biosamples. In the matching biosample HepG2 (HepG2 stands in for Hep 3B2.1-7 (both liver cancer lines)): 224 peaks from 188 factors. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): AFF1, ARID4A, ARID5B, ASH2L, BCL3, BRD4, CBFA2T3, CTBP1, DMAP1, DPF2, EED, EP300 (+97 more). Bound, expressed TFs with a binding model: 140; listed one per row: FOXA1, MAX, SP1, TCF7L2, FOXA2, USF1, JUND, RXRA, NR2F2, TCF12; also bound: ELF1, CREB1, EGR1, ATF3, NRF1, NCOA1, HNF4A, E2F4, YY1, NR2F6, ZNF281, MEIS2, FOXK2, FOXJ3, FOXA3, ZNF687, HNF1B, SOX6, FOXP1, ZHX2, MEF2D, CREM, ZBTB33, FOSL2, KLF9, CEBPA, KDM2A, MYBL2, ERF, ELF3 (+100 more). Bound but below 1 TPM: EGR2, ESR1, HOXD1, KLF1, KLF11, KLF4, MITF, MSX2, NKX3-1, NR5A1. Assayed with no peak here: 251 TFs in the matching biosample, 170 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXA1: bound here. 9 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, Ishikawa, MCF-7, T47D (+1 more) (e.g. ENCSR865RXA). 53.15 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 84 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound here. 8 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, HeLa-S3, K562, MCF-7 (e.g. ENCSR168DYA). 33.54 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 153 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 7 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, HCT116, liver (e.g. ENCSR000BJX). 23.48 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 234 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 6 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in HeLa-S3, MCF-7, Panc1 (e.g. ENCSR346BOD). 24.15 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 229 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXA2: bound here. 6 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, liver (e.g. ENCSR066EBK). 22.07 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 253 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> USF1: bound here. 5 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, K562 (e.g. ENCSR099FCQ). 85.08 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 42 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUND: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, K562, MCF-7 (e.g. ENCSR000BGK). 48.46 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 97 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> RXRA: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in liver (e.g. ENCSR416HDG). 31.42 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 167 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in MCF-7 (e.g. ENCSR000BVM). 22.86 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 243 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF12: bound here. 3 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HepG2; also in A549, MCF-7 (e.g. ENCSR000BJG). 40.85 TPM in DepMap:ACH-000625 (Hep 3B2.1-7), rank 123 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs12740374&size=100; retrieved 2026-10-25T17:29:12+00:00)

> 100 GWAS Catalog associations for rs12740374, strongest first:
> High cholesterol: p 9.9e-324, effect allele G, risk-allele frequency 0.7788, PMID 39024449
> Takes medication for high cholesterol?: p 6.0e-297, effect allele G, risk-allele frequency 0.7815, PMID 39024449
> Disorders of lipid metabolism (PheCode 272): p 7.0e-262, effect allele G, risk-allele frequency 0.778, PMID 39024449
> Circulating TNFSF13 levels: p 4.0e-260, effect allele ?, risk-allele frequency NR, PMID 42097137
> Hyperlipidemia (PheCode 272.1): p 6.0e-259, effect allele G, risk-allele frequency 0.778, PMID 39024449
> total cholesterol (minimum, inv-norm transformed): p 1.0e-208, effect allele G, risk-allele frequency 0.7774, PMID 39024449
> low density lipoprotein cholesterol (LDLC, maximum, inv-norm transformed): p 4.0e-164, effect allele G, risk-allele frequency 0.7453, PMID 39024449
> low density lipoprotein cholesterol (LDLC, mean, inv-norm transformed): p 4.0e-154, effect allele G, risk-allele frequency 0.7454, PMID 39024449
> Circulating LAG3 levels (id: OID05553_OID21315): p 1.0e-153, effect allele ?, risk-allele frequency NR, PMID 42097137
> Circulating LAG3 levels (id: OID01023_OID21315): p 1.0e-152, effect allele ?, risk-allele frequency NR, PMID 42097137
> LDL cholesterol levels: p 2.0e-137, effect allele T, risk-allele frequency NR, PMID 39414775
> total cholesterol (maximum, inv-norm transformed): p 2.0e-123, effect allele G, risk-allele frequency 0.7453, PMID 39024449

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:04+00:00)

> 2316 credible sets contain 1_109274968_G_T: 189 GWAS, 11 molecular QTL.
> GWAS Total cholines levels (UKB data field 23436): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Apolipoprotein B levels (UKB data field 23439): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Total cholesterol levels: PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Cholesterol to total lipids in large HDL percentage (UKB dat: PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Total lipids in small VLDL (UKB data field 23510): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> GWAS Triglycerides in medium VLDL (UKB data field 23508): PIP 1.00; L2G SORT1 0.99, CELSR2 0.96, PSRC1 0.20
> sqtl for SORT1 (gtex-v10_majiq_liver_ensg00000134243_s_109314672-1): PIP 0.72
> sqtl for CELSR2 (gtex-v10_majiq_muscle_ensg00000143126_s_109273436-): PIP 0.49
> eqtl for PSRC1 (gtex-v10_ge_pancreas_ensg00000134222): PIP 0.41
> eqtl for CELSR2 (gtex-v10_exon_esophagus_mucosa_ensg00000143126_8_1): PIP 0.37
> tuqtl for CELSR2 (gtex-v10_txrev_liver_ensg00000143126_grp_2_contain): PIP 0.32
> eqtl for PSRC1 (fairfax_2014_microarray_monocyte_naive_ilmn_231596): PIP 0.25
> Best L2G gene scores across these sets: SORT1 0.99, CELSR2 0.98, PSRC1 0.66

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_109274968_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:36+00:00)

> 39 significant GTEx v8 single-tissue eQTLs for chr1_109274968_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).
> CELSR2 in Muscle_Skeletal: NES +0.54, p 2.3e-76
> SORT1 in Liver: NES +1.27, p 3.1e-54
> PSRC1 in Liver: NES +1.24, p 1.1e-37
> CELSR2 in Liver: NES +1.04, p 9.4e-34
> PSRC1 in Esophagus_Mucosa: NES +0.40, p 1.8e-24
> CELSR2 in Esophagus_Mucosa: NES +0.31, p 1.1e-16
> PSRC1 in Whole_Blood: NES +0.30, p 4.0e-16
> PSRC1 in Pancreas: NES +0.53, p 2.2e-13
> CELSR2 in Pancreas: NES +0.32, p 2.8e-13
> PSRC1 in Muscle_Skeletal: NES +0.35, p 1.5e-12
> PSRC1 in Skin_Not_Sun_Exposed_Suprapubic: NES +0.29, p 2.0e-12
> PSRC1 in Testis: NES +0.35, p 9.0e-12
> CELSR2 in Skin_Sun_Exposed_Lower_leg: NES +0.12, p 5.1e-11
> SORT1 in Esophagus_Mucosa: NES +0.13, p 8.4e-11
> PSRC1 in Brain_Cortex: NES +0.34, p 2.5e-09

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20AND%20SORT1%20AND%20%28%22ldl%20cholesterol%22%20OR%20%22myocardial%20infarction%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:12+00:00)

> Europe PMC: 127 hits for 'rs12740374 AND SORT1 AND ("ldl cholesterol" OR "myocardial infarction")'; top 8 with PMIDs:
> PMID 42019808 (2026): Causal statistical association between remnant cholesterol and coronary heart disease: genetic insights into the PSRC1-CELSR2-SORT1 gene cluster.
> PMID 42820291 (2026): Clinical trials in a dish: cardiometabolic drug development with biological and digital twins.
> PMID 40922271 (2025): Effect of dietary habits on multiple cardiovascular diseases: A comprehensive Mendelian randomization study.
> PMID 41380003 (2025): Computationally efficient whole-genome quantile regression at biobank scale.
> PMID 39858645 (2025): Research Progress and Clinical Translation Potential of Coronary Atherosclerosis Diagnostic Markers from a Genomic Perspective.
> PMID 42211154 (2026): Treatment Target Discovery From Vasculo-Protective Phenotypes.
> PMID 41991941 (2026): Genetic and molecular factors underlying human longevity and epigenetic aging.
> PMID 38266112 (2024): Genome-Wide Genetic Associations Prioritize Evaluation of Causal Mechanisms of Atherosclerotic Disease Risk.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20C/EBP%20SORT1%20enhancer%20allele-specific%20binding%20LDL&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:29:08+00:00)

> Europe PMC: 31 hits for 'rs12740374 C/EBP SORT1 enhancer allele-specific binding LDL'; top 8 with PMIDs:
> PMID 41380003 (2025): Computationally efficient whole-genome quantile regression at biobank scale.
> PMID 40250421 (2025): Characterization of non-coding variants associated with transcription-factor binding through ATAC-seq-defined footprint QTLs in liver.
> PMID 41650936 (2026): Expanded chromatin accessibility mapping explains genetic variation associated with complex traits in liver.
> PMID 39858645 (2025): Research Progress and Clinical Translation Potential of Coronary Atherosclerosis Diagnostic Markers from a Genomic Perspective.
> PMID 38266112 (2024): Genome-Wide Genetic Associations Prioritize Evaluation of Causal Mechanisms of Atherosclerotic Disease Risk.
> PMID 37582372 (2023): Prioritization of therapeutic targets for dyslipidemia using integrative multi-omics and multi-trait analysis.
> PMID 35724703 (2022): Sorting through the extensive and confusing roles of sortilin in metabolic disease.
> PMID 34784266 (2022): Emerging roles of sortilin in affecting the metabolism of glucose and lipid profiles.

<a id="e20"></a>**E20** tf_expression, DepMap expression / GTEx v8 medians (local files; retrieved local)

> CEBPA in DepMap line ACH-000625: 141.33 TPM, rank 18 of 1626 TFs (1 = highest); this context is at the 99.2th percentile of CEBPA across all DepMap lines.

<a id="e21"></a>**E21** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'
