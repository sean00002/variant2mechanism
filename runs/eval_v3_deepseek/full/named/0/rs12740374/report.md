# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 8 model calls; 357 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: CEBPG (bound here, z 26.76); CEBPA (bound here, z 22.81); MLX (bound here, z -15.37); GFI1 (bound here, z 14.71); KLF6 (bound here, z -13.34); KLF12 (bound here, z -13.34); HNF4A (bound here, z 11.41); NR2F6 (bound here, z 11.41); RXRB (bound here, z 11.41); RXRA (bound here, z 11.41). Occupancy unknown: ZNF43 (z 35.83); RFX2 (z 23.16); TFAP2A (z -21.21); TFAP2E (z -21.21); ZNF345 (z 20.62). Diagnostic, not shown to the model: 239 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1_CEBPA_SORT1: Alt T strengthens a CEBPA site in the dELS and is associated with higher liver SORT1 and LDL trait (p = 0.40)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646 dELS; gene SORT1; cell type hepatocyte / liver cancer line HepG2-Hep3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA binds the alt T allele more strongly than ref G at this base. CEBPA has an ENCODE HepG2 ChIP-seq peak over the variant and is highly expressed in DepMap Hep 3B2.1-7; its QBiC-SELEX entry shows alt>ref (z 22.81, effect +2.331, strong alt site). Caveat: the best CEBPA QBiC model is CIS-BP-mapped from CEBPB, and allele-specific occupancy at rs12740374 is not demonstrated. | weak | [E21](#e21), [E04](#e04) |
| element | The variant lies in the active distal enhancer cCRE EH38E1374646 (dELS), with DNase, H3K27ac and H3K4me3 support, so an allele-specific TF change at this base could alter enhancer activity. | supported | [E03](#e03), [E01](#e01) |
| gene | The alt T allele is associated with higher SORT1 expression in liver (NES +1.27), and SORT1 has the top L2G score with a liver SQTL signal, supporting SORT1 as a plausible distal target. | supported | [E17](#e17), [E16](#e16), [E02](#e02) |
| cell_type | The relevant context is liver/hepatocyte: the SORT1 eQTL is in liver, CEBPA is expressed in Hep 3B2.1-7, and ChIP occupancy is in HepG2, a liver cancer line used as a stand-in for Hep 3B2.1-7. | supported | [E17](#e17), [E21](#e21), [E04](#e04) |
| phenotype | rs12740374 is strongly associated with LDL/high cholesterol, but the direction needs harmonization: the strongest high-cholesterol/LDLC records list G as the effect/risk allele at risk-allele frequency ~0.78, while one LDL record lists T. Alt T is associated with higher liver SORT1, but the provided evidence does not directly show that changing SORT1 expression causally changes LDL or MI risk. | weak | [E15](#e15), [E17](#e17), [E16](#e16) |

Predictions: Allele-specific CEBPA ChIP or reporter activity is higher on alt T than ref G in hepatocytes.; CEBPA knockdown/CRISPRi reduces the alt-T-associated enhancer activity and SORT1 expression.; CEBPB does not show stronger allele-specific occupancy than CEBPA at this base.

Falsified if: CEBPA does not bind allele-specifically at this base in hepatocytes.; CEBPA loss does not change the alt-T enhancer effect or SORT1 expression.; CEBPB, not CEBPA, explains the allele-specific C/EBP-family occupancy.

### 2. H6_CEBPB_SORT1: Alt T strengthens a CEBPB site in the dELS and is associated with higher liver SORT1 and LDL trait (p = 0.18)

TF CEBPB (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646 dELS; gene SORT1; cell type hepatocyte / liver cancer line HepG2-Hep3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB binds the alt T allele more strongly than ref G in vitro: its own QBiC-SELEX model gives z 22.81, effect +2.331 and a strong alt site. CEBPB occupancy at this exact base in HepG2 is not explicitly reported in the provided evidence, although E04 shows broad HepG2 TF occupancy over the variant; this occupancy link is therefore plausible but less directly supported than for CEBPA. | weak | [E36](#e36), [E04](#e04) |
| element | The variant lies in the active dELS EH38E1374646, so a CEBPB binding change at this base could alter enhancer output. | supported | [E03](#e03), [E01](#e01) |
| gene | The alt T allele is associated with higher SORT1 expression in liver (NES +1.27), and SORT1 has the top L2G score with a liver SQTL signal, making SORT1 a plausible target of this element. | supported | [E17](#e17), [E16](#e16) |
| cell_type | The candidate context is liver/hepatocyte: the SORT1 eQTL is in liver, E04 reports broad HepG2 occupancy, and CEBPB is a liver-expressed C/EBP-family factor, though no primary hepatocyte CEBPB ChIP is provided. | weak | [E17](#e17), [E04](#e04), [E36](#e36) |
| phenotype | rs12740374 is strongly associated with LDL/high cholesterol, but the effect-allele direction is not fully harmonized in E15, and no provided experiment shows that CEBPB-dependent SORT1 change causally alters LDL or MI risk. | weak | [E15](#e15), [E17](#e17) |

Predictions: Allele-specific CEBPB ChIP is stronger on alt T than ref G in hepatocytes.; CEBPB knockdown/CRISPRi reduces the alt-T enhancer effect and SORT1 expression.; CEBPA does not show stronger allele-specific occupancy than CEBPB at this base.

Falsified if: CEBPB does not occupy this base allele-specifically in hepatocytes.; CEBPB loss does not affect the alt-T enhancer or SORT1 expression.; CEBPA, not CEBPB, explains the C/EBP-family allele-specific signal.

### 3. H2_CEBPG_SORT1: Alt T strengthens a CEBPG site in the same enhancer and is associated with higher liver SORT1 (p = 0.15)

TF CEBPG (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646 dELS; gene SORT1; cell type hepatocyte / liver cancer line HepG2-Hep3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPG binds the alt T allele more strongly than ref G. CEBPG has its own QBiC-SELEX model with a strong alt-specific effect (z 26.76, effect +2.321), is expressed in Hep 3B2.1-7, and has an ENCODE HepG2 ChIP-seq peak over the variant. C/EBP paralogs share binding specificity, so CEBPG is a candidate but not uniquely resolved. | supported | [E20](#e20), [E04](#e04) |
| element | The variant is in the active dELS EH38E1374646, consistent with CEBPG acting through this enhancer. | supported | [E03](#e03), [E01](#e01) |
| gene | The alt T allele is associated with higher SORT1 mRNA in liver, and SORT1 is the top L2G gene, so CEBPG binding could increase SORT1 expression. | supported | [E17](#e17), [E16](#e16) |
| cell_type | CEBPG is expressed in Hep 3B2.1-7, ChIP occupancy is in HepG2, and the SORT1 eQTL is in liver, supporting a liver context with cancer-line caveats. | supported | [E20](#e20), [E04](#e04), [E17](#e17) |
| phenotype | Alt T is associated with higher liver SORT1 and with LDL/high-cholesterol GWAS signals, but the effect-allele direction needs harmonization and SORT1-to-LDL causality is not shown here. | weak | [E15](#e15), [E17](#e17) |

Predictions: CEBPG ChIP or reporter assays show alt-T-specific binding at this base.; CEBPG knockdown reduces the alt-T enhancer effect on SORT1.; CEBPA and CEBPB do not show stronger allele-specific occupancy than CEBPG.

Falsified if: CEBPG does not occupy this base allele-specifically in hepatocytes.; CEBPG loss does not affect the SORT1 eQTL or enhancer activity.; Another C/EBP paralog fully explains the allele-specific signal.

### 4. H5_null: No TF-mediated effect of rs12740374; association is driven by a linked causal variant or no allelic effect (p = 0.15)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at this exact base in hepatocytes.; The GWAS/eQTL signal is explained by another variant in LD.; Editing rs12740374 alone does not change enhancer activity or SORT1/CELSR2 expression.

Falsified if: Allele-specific C/EBP-family binding at this base is demonstrated.; CRISPR swapping rs12740374 changes enhancer activity or target gene expression in hepatocytes.; The eQTL/GWAS signal remains after controlling for linked variants.

### 5. H3_CEBPA_CELSR2: Alt T strengthens a CEBPA site and is associated with higher CELSR2, with CELSR2 contributing to the LDL trait (p = 0.12)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646 dELS / CELSR2 3_prime_UTR overlap; gene CELSR2; cell type hepatocyte / liver cancer line HepG2-Hep3B2.1-7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA binds the alt T allele more strongly, supported by its HepG2 ChIP occupancy over the variant and its QBiC-SELEX alt-specific increase, with the same caveat that the best CEBPA model is CIS-BP-mapped from CEBPB and allele-specific occupancy is not demonstrated. | weak | [E21](#e21), [E04](#e04) |
| element | The variant is in the dELS EH38E1374646 and also overlaps the CELSR2 3_prime_UTR, so this element or the transcript overlap could regulate CELSR2 in addition to distal genes. | supported | [E03](#e03), [E01](#e01) |
| gene | The alt T allele is associated with higher CELSR2 expression in liver (NES +1.04), and CELSR2 has high L2G support (0.98), making CELSR2 a plausible target. | supported | [E17](#e17), [E16](#e16) |
| cell_type | The relevant context is liver/hepatocyte: the CELSR2 liver eQTL is present, CEBPA is expressed in Hep 3B2.1-7, and ChIP is in HepG2. | supported | [E17](#e17), [E21](#e21), [E04](#e04) |
| phenotype | rs12740374 is strongly associated with LDL/high cholesterol, and alt T is associated with higher CELSR2, but the CELSR2-to-LDL causal direction is not shown, and target-gene ambiguity remains because SORT1 has equally strong L2G support. | weak | [E15](#e15), [E17](#e17), [E16](#e16) |

Predictions: Allele-specific CEBPA binding tracks CELSR2 expression more closely than SORT1 expression in some liver contexts.; CEBPA site disruption reduces the CELSR2 eQTL effect.; CELSR2, not SORT1, mediates part of the phenotype in the relevant hepatocyte state.

Falsified if: CELSR2 expression is not affected by the CEBPA site.; SORT1 fully explains the LDL effect and CELSR2 has no independent contribution.; The CELSR2 signal is explained by the 3_prime_UTR transcript overlap rather than enhancer regulation.

## Prediction matrix

| Test | Cost | Separates top two | H1_CEBPA_SORT1 | H6_CEBPB_SORT1 | H2_CEBPG_SORT1 | H5_null | H3_CEBPA_CELSR2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ChIP-qPCR for CEBPA at rs12740374 in a heterozygous hepatocyte line | medium | yes | CEBPA ChIP is stronger on alt T than ref G. | No or weak CEBPA allelic bias. | No or weak CEBPA allelic bias. | No CEBPA allelic bias. | CEBPA ChIP is stronger on alt T than ref G. |
| Allele-specific ChIP-qPCR for CEBPB at rs12740374 in a heterozygous hepatocyte line | medium | yes | No or weak CEBPB allelic bias. | CEBPB ChIP is stronger on alt T than ref G. | No or weak CEBPB allelic bias. | No CEBPB allelic bias. | No or weak CEBPB allelic bias. |
| CEBPA knockdown/CRISPRi in HepG2 or Hep3B2.1-7 followed by SORT1 expression and enhancer activity | medium | yes | CEBPA loss reduces the alt-T enhancer effect and SORT1 expression. | CEBPA loss has little or no effect. | CEBPA loss has little or no effect. | No allele-specific enhancer effect to lose. | CEBPA loss reduces CELSR2 more than SORT1. |
| CEBPB knockdown/CRISPRi in HepG2 or Hep3B2.1-7 followed by SORT1 expression and enhancer activity | medium | yes | CEBPB loss has little or no effect. | CEBPB loss reduces the alt-T enhancer effect and SORT1 expression. | CEBPB loss has little or no effect. | No allele-specific enhancer effect to lose. | CEBPB loss has little or no effect on CELSR2. |
| CEBPG knockdown/CRISPRi followed by SORT1 expression | medium | no | Little or no effect. | Little or no effect. | Reduces the alt-T enhancer effect on SORT1. | No allele-specific effect. | Little or no effect. |
| Allele-swap reporter at rs12740374 in HepG2/Hep3B2.1-7 | medium | no | Alt T increases reporter activity. | Alt T increases reporter activity. | Alt T increases reporter activity. | No allele-specific reporter difference. | Alt T increases reporter activity, possibly with CELSR2 context. |
| CRISPR deletion/fine-mapping of SORT1 versus CELSR2 regulatory regions followed by eQTL or expression readout | high | no | SORT1 expression is affected; CELSR2 less so. | SORT1 expression is affected; CELSR2 less so. | SORT1 expression is affected; CELSR2 less so. | Neither gene is affected by rs12740374 editing alone. | CELSR2 expression is affected; SORT1 less so. |
| Conditional GWAS/eQTL analysis controlling for linked variants in the 1p13 locus | low | no | rs12740374 retains an independent signal. | rs12740374 retains an independent signal. | rs12740374 retains an independent signal. | Signal is explained by a linked variant. | rs12740374 retains an independent signal. |
| Harmonize E15 effect alleles and betas against LD and eQTL direction | low | no | Alt T is the non-risk allele with higher SORT1. | Alt T is the non-risk allele with higher SORT1. | Alt T is the non-risk allele with higher SORT1. | No consistent allelic direction after harmonization. | Alt T is the non-risk allele with higher CELSR2. |

## Next experiment

The cheapest separating experiment is allele-specific ChIP-qPCR for CEBPA and CEBPB at rs12740374 in a heterozygous hepatocyte line: H1_CEBPA_SORT1 predicts CEBPA alt>ref with no CEBPB bias, whereas H6_CEBPB_SORT1 predicts CEBPB alt>ref with no CEBPA bias. If the available liver lines are not heterozygous at this site, the same separation can be obtained with an allele-swap reporter plus CEBPA versus CEBPB knockdown, but allele-specific ChIP is cheaper and more direct.

## Investigate calls

- literature_search({"query": "rs12740374 AND (CEBPA OR CEBPB OR CEBPG) AND (allele-specific OR reporter OR CRISPR OR MPRA OR SORT1)"})
- qbic_tf_detail({"tf": "CEBPB"})
- gene_disease({"gene": "SORT1"})

## Flags

- quote_rejected: PMID 42019808: not an exact substring of the abstract
- tool_failed: E37 gene_disease: Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'

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

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:109274968:G>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000625), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 140 occupied (63 with a strong site), 5 of 78 with unknown occupancy. Left out: 251 TFs assayed in the matching biosample and 170 assayed only elsewhere, none with a peak here; 12 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPG (bZIP, 1 model; QBiC-SELEX coverage: own model): best model CEBPG_eDBD_TACTTT40NTCT_KN_yin2017_0_4_7mer (its own model), z 26.76, effect 2.321: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 46.37 TPM, rank 103 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR639IIZ. Best model's site strength: ref 64.5th, alt 99.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPA (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (a CIS-BP-mapped model of CEBPB), z 22.81, effect 2.331: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 141.33 TPM, rank 18 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR142IGM. Best model's site strength: ref 87.0th, alt 99.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MLX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MLX_eDBD_TAGGCT40NACC_KAN_yin2017_0_4_6mer (its own model), z -15.37, effect -0.496: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 57.97 TPM, rank 73 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR125DAD. Best model's site strength: ref 99.4th, alt 82.1th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GFI1 (C2H2 ZF, 2 models; QBiC-SELEX coverage: own model): best model GFI1_eDBD_TCTGCT40NTGT_KR_yin2017_1_2_7mer (its own model), z 14.71, effect 0.372: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.47 TPM, rank 921 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR849FVL. Best model's site strength: ref 87.9th, alt 97.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> KLF6 (C2H2 ZF, 6 models; QBiC-SELEX coverage: own model): best model KLF6_eDBD_TGCTCC40NCCG_KW_yin2017_0_3_7mer (its own model), z -13.34, effect -0.351: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 46.95 TPM, rank 99 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR757EKM. Best model's site strength: ref 98.6th, alt 82.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> KLF12 (C2H2 ZF, 6 models; QBiC-SELEX coverage: own model): best model KLF6_eDBD_TGCTCC40NCCG_KW_yin2017_0_3_7mer (a CIS-BP-mapped model of KLF6), z -13.34, effect -0.351: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.14 TPM, rank 1054 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR552YWL. Best model's site strength: ref 98.6th, alt 82.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF4A (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2F2), z 11.41, effect 0.416: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 90.19 TPM, rank 38 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR469FBY. Best model's site strength: ref 95.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F6 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2F2), z 11.41, effect 0.416: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 47.82 TPM, rank 98 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR798IJO. Best model's site strength: ref 95.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> RXRB (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2F2), z 11.41, effect 0.416: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 32.41 TPM, rank 159 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR560SEP. Best model's site strength: ref 95.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> RXRA (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2F2), z 11.41, effect 0.416: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 31.42 TPM, rank 167 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR416HDG. Best model's site strength: ref 95.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF43 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF43_FL_GC40NTATAGG_YWRA_jolma2025_0_3_7mer (its own model), z 35.83, effect 3.431: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.74 TPM, rank 525 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 93.6th, alt 99.9th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> RFX2 (RFX, 4 models; QBiC-SELEX coverage: own model): best model RFX4_eDBD_TACTCG40NCAA_KAN_yin2017_0_3_7mer (a CIS-BP-mapped model of RFX4), z 23.16, effect 1.235: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.97 TPM, rank 708 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.8th, alt 99.0th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2A (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -21.21, effect -0.98: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.65 TPM, rank 570 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.8th, alt 98.8th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2E (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (its own model), z -21.21, effect -0.98: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.06 TPM, rank 961 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.8th, alt 98.8th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF345 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF345_eDBD_TGTAAG40NACT_KT_yin2017_0_3_7mer (its own model), z 20.62, effect 0.964: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.64 TPM, rank 1005 of 1626 TFs in DepMap:ACH-000625 (Hep 3B2.1-7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.7th, alt 99.9th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs12740374%20AND%20%28CEBPA%20OR%20CEBPB%20OR%20CEBPG%29%20AND%20%28allele-specific%20OR%20reporter%20OR%20CRISPR%20OR%20MPRA%20OR%20SORT1%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:16:24+00:00)

> Europe PMC: 31 hits for 'rs12740374 AND (CEBPA OR CEBPB OR CEBPG) AND (allele-specific OR reporter OR CRISPR OR MPRA OR SORT1)'; top 8 with PMIDs:
> PMID 39868043 (2025): Abundant repressor binding sites in human enhancers are associated with the fine-tuning of gene regulation.
> PMID 39858645 (2025): Research Progress and Clinical Translation Potential of Coronary Atherosclerosis Diagnostic Markers from a Genomic Perspective.
> PMID 40537438 (2025): Application of human iPSC-derived white, beige, and brown adipocytes for metabolic disease modeling and transplantation therapy.
> PMID 31433696 (2019): Functional Genomics and CRISPR Applied to Cardiovascular Research and Medicine. [no abstract]
> PMID 28186491 (2017): Combinatorial bZIP dimers display complex DNA-binding specificity landscapes.
> PMID 34024118 (2021): Single-Cell Epigenomics and Functional Fine-Mapping of Atherosclerosis GWAS Loci.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 34570217 (2022): VannoPortal: multiscale functional annotation of human genetic variants for interrogating molecular mechanism of traits and diseases.

<a id="e35a"></a>**E35a** literature_search, Europe PMC abstract, PMID 39858645 (https://europepmc.org/article/MED/39858645; retrieved 2026-10-26T13:16:24+00:00)

> GWASs and sequencing studies have identified key genetic variations associated with CAD, including JCAD/KIAA1462, GUCY1A3, PCSK9, and SORT1, which regulate inflammation, lipid metabolism, and vascular function.

<a id="e36"></a>**E36** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"CEBPB","symbol":"CEBPB","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr1:109274968:G>T","gate_p":5.02e-05,"models":[{"model":"CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer","mapping":"own","group":"G035 bZIP, 3 models","quality":0.748,"effect":2.331,"z":22.81,"p":3.9e-115,"rank_abs_z":"8/997","passed_gate":true,"site_strength":{"ref_percentile":87.0,"alt_percentile":99.8,"k":7}},{"model":"CEBPA_NA_lib5_20N_rm2017_0_3_7mer","mapping":"CIS-BP (CEBPA)","group":"G035 bZIP, 3 models","quality":0.948,"effect":2.803,"z":22.63,"p":2.2e-113,"rank_abs_z":"9/997","passed_gate":true,"site_strength":{"ref_percentile":66.0,"alt_percentile":98.8,"k":7}},{"model":"CEBPE_eDBD_TTAGGC40NATA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (CEBPE)","group":"G035 bZIP, 3 models","quality":0.817,"effect":1.731,"z":11.28,"p":1.7e-29,"rank_abs_z":"28/997","passed_gate":true,"site_strength":{"ref_percentile":77.0,"alt_percentile":99.3,"k":7}}]}

<a id="e37"></a>**E37** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'
