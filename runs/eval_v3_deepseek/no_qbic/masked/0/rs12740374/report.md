# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.03 over 9 model calls; 437 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H1: CEBPA site creation at the dELS increases SORT1 and is protective (p = 0.52)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646 dELS; gene SORT1; cell type liver/hepatocyte-lineage (HepG2/Hep3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA binds this element. I choose CEBPA because E19 shows an exact CEBPA ChIP-seq peak containing this base in HepG2, and E04 lists CEBPA among bound, expressed TFs with a binding model in HepG2. The alt T allele is nominated to bind CEBPA more strongly than ref G because this is a C/EBP-site-creating 1p13 SORT1 mechanism, but no CEBPA QBiC-SELEX model or allele-specific assay is supplied here, so the direction is the weakest link. | weak | [E19](#e19), [E04](#e04) |
| element | The variant lies in active distal enhancer-like cCRE EH38E1374646, with DNase, H3K27ac and H3K4me3 signal; E03 scores are maxima over ENCODE biosamples, not HepG2-specific. | supported | [E03](#e03), [E04](#e04) |
| gene | The alt T allele is associated with higher SORT1 expression in liver (NES +1.27, p 3.1e-54), and SORT1 has the strongest L2G score at this locus (0.99). This supports variant-to-SORT1 expression association, not element-to-SORT1 causality. | supported | [E17](#e17), [E16](#e16) |
| cell_type | The relevant context is liver/hepatocyte-lineage: CEBPA has an exact ChIP-seq peak over this base in HepG2, and the SORT1 eQTL is observed in liver. HepG2 is a hepatoma stand-in for Hep 3B2.1-7, so this is indirect. | weak | [E19](#e19), [E17](#e17), [E04](#e04) |
| phenotype | The G allele is the risk allele for high cholesterol/LDL in the strongest E15 associations, and the T allele is associated with higher SORT1 expression in E17. If higher hepatic SORT1 is protective, this is directionally consistent. However, one LDL trait reports T as effect allele and E18b says PSRC1-CELSR2-SORT1 protection may act via remnant cholesterol/CHD independent of LDL-C, so LDL-specific protection is not established. | weak | [E15](#e15), [E17](#e17), [E18b](#e18b) |

Predictions: Allele-specific CEBPA ChIP or EMSA will show stronger CEBPA binding to alt T than ref G at this base.; CRISPR editing of this base from G to T in a liver-cell context will increase SORT1 expression.; CEBPA knockdown will reduce the alt-T enhancer effect on SORT1.

Falsified if: No allele-specific CEBPA binding is detected at this base.; Editing this base alone does not change SORT1 enhancer activity or SORT1 expression in liver cells.; CEBPA knockdown does not affect the alt-T effect.

### 2. H0: No TF-mediated effect of this base; linked causal variant or direct CELSR2 3'UTR effect explains the signal (p = 0.31)

Null chain: no TF-mediated effect of this variant.

Predictions: This base will show no allele-specific CEBPA or FOXA1 binding in relevant liver cells.; The GWAS and eQTL signals will be explained by a nearby linked causal variant or by a direct CELSR2 3'UTR/transcript effect rather than by this base.; Editing this base alone will not change SORT1, CELSR2 or PSRC1 expression.

Falsified if: Allele-specific CEBPA binding at this base is demonstrated.; CRISPR editing of this base alone changes enhancer activity and SORT1, CELSR2 or PSRC1 expression in liver cells.; The eQTL and GWAS signals are shown to require this exact base rather than a linked variant.

### 3. H2: CEBPA site creation at the dELS increases CELSR2 (p = 0.10)

TF CEBPA (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646 dELS; gene CELSR2; cell type liver/hepatocyte-lineage (HepG2/Hep3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPA binds this element. CEBPA is chosen because E19 shows an exact CEBPA ChIP-seq peak over this base in HepG2 and E04 lists CEBPA among bound, expressed TFs there. The alt T allele is nominated to bind CEBPA more strongly than ref G, but no CEBPA QBiC-SELEX model or allele-specific assay is supplied, so the direction is unsupported. | weak | [E19](#e19), [E04](#e04) |
| element | The variant lies in active dELS EH38E1374646 with DNase, H3K27ac and H3K4me3 signal; the E03 z-scores are biosample maxima, so HepG2-specific activity is not directly shown. | supported | [E03](#e03), [E04](#e04) |
| gene | The alt T allele is associated with higher CELSR2 expression in liver (NES +1.04, p 9.4e-34), and CELSR2 has high L2G scores (0.96-0.98). E01 also annotates the variant as a CELSR2 3_prime_UTR_variant, so a direct transcript/3'UTR effect remains an alternative. | supported | [E17](#e17), [E16](#e16) |
| cell_type | Liver/hepatocyte-lineage is relevant: CEBPA has an exact ChIP-seq peak in HepG2 and CELSR2 has a liver eQTL. The HepG2-to-Hep3B2.1-7 substitution is indirect. | weak | [E19](#e19), [E17](#e17), [E04](#e04) |
| phenotype | G is the risk allele for high cholesterol/LDL in the strongest E15 traits, and T increases CELSR2 in E17; this is directionally consistent if higher CELSR2 is protective. But one LDL trait reports T as effect allele and E18b describes CHD protection via remnant cholesterol independent of LDL-C, so the LDL-specific claim is not established. | weak | [E15](#e15), [E17](#e17), [E18b](#e18b) |

Predictions: Allele-specific CEBPA binding at this base will correlate more strongly with CELSR2 than with SORT1 expression.; The CELSR2 liver eQTL will require this dELS and CEBPA.; A CELSR2 3'UTR reporter will not explain the full allelic effect if the enhancer mechanism is correct.

Falsified if: No allele-specific CEBPA binding is detected at this base.; CELSR2 expression is not affected by this dELS in liver cells.; The CELSR2 signal is fully explained by a direct 3'UTR effect rather than enhancer activity.

### 4. H3: FOXA1 site creation at the dELS increases SORT1 (p = 0.07)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646 dELS; gene SORT1; cell type liver/hepatocyte-lineage (HepG2/Hep3B2.1-7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 binds this element. I choose FOXA1 because E05 reports 9 FOXA1 ChIP-seq peaks containing this base in HepG2 and high expression in Hep3B2.1-7 (53.15 TPM, rank 84 of 1626 TFs), and E04 lists FOXA1 among bound, expressed TFs with a binding model in HepG2. The alt T allele is nominated to bind FOXA1 more strongly than ref G, but no FOXA1 QBiC-SELEX model or allele-specific assay is supplied, so this direction is weak. | weak | [E05](#e05), [E04](#e04) |
| element | The variant lies in active dELS EH38E1374646 with DNase, H3K27ac and H3K4me3 signal; E03 scores are maxima over biosamples, not HepG2-specific. | supported | [E03](#e03), [E04](#e04) |
| gene | The alt T allele is associated with higher SORT1 expression in liver (NES +1.27, p 3.1e-54), and SORT1 has the strongest L2G score (0.99). This supports variant-to-SORT1 association, not FOXA1 mediation. | supported | [E17](#e17), [E16](#e16) |
| cell_type | The relevant context is liver/hepatocyte-lineage: FOXA1 has exact ChIP-seq peaks over this base in HepG2 and high expression in Hep3B2.1-7, and SORT1 has a liver eQTL. HepG2 is a stand-in for Hep3B2.1-7. | supported | [E05](#e05), [E17](#e17) |
| phenotype | G is the risk allele for high cholesterol/LDL in the strongest E15 traits, and T increases SORT1 in E17; this is directionally consistent if higher SORT1 is protective. But one LDL trait reports T as effect allele and E18b says protection may be via remnant cholesterol/CHD independent of LDL-C, so LDL-specific protection is not established. | weak | [E15](#e15), [E17](#e17), [E18b](#e18b) |

Predictions: Allele-specific FOXA1 ChIP will show stronger FOXA1 binding to alt T than ref G at this base.; FOXA1 knockdown, not CEBPA knockdown, will blunt the alt-T enhancer effect on SORT1.; CRISPR editing this base will change FOXA1 occupancy and SORT1 expression in liver cells.

Falsified if: No allele-specific FOXA1 binding is detected at this base.; FOXA1 knockdown does not affect enhancer activity or SORT1 expression.; CEBPA, not FOXA1, explains the allele-specific effect.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific CEBPA ChIP-qPCR or EMSA at the exact base in HepG2/Hep3B2.1-7 | low | yes | Expected outcome: alt T shows stronger CEBPA binding than ref G. | Expected outcome: no allele-specific CEBPA binding at this base. | Expected outcome: alt T shows stronger CEBPA binding than ref G, but the downstream target is CELSR2 rather than SORT1. | Expected outcome: no CEBPA allele-specific binding; FOXA1, not CEBPA, shows allele-specific occupancy if any. |
| CRISPR base edit ref G vs alt T in HepG2/Hep3B2.1-7, measure SORT1 and CELSR2 expression | medium | yes | Expected outcome: alt T increases SORT1 expression. | Expected outcome: no change in SORT1 or CELSR2 expression from editing this base alone. | Expected outcome: alt T increases CELSR2 expression more than SORT1. | Expected outcome: alt T increases SORT1 expression only if FOXA1 is intact. |
| Allele-specific FOXA1 ChIP-qPCR at the exact base in HepG2 | low | no | Expected outcome: no FOXA1 allele-specific binding. | Expected outcome: no FOXA1 allele-specific binding. | Expected outcome: no FOXA1 allele-specific binding. | Expected outcome: alt T binds FOXA1 more strongly than ref G. |
| CEBPA knockdown in HepG2/Hep3B2.1-7 followed by allele-specific enhancer-reporter assay | medium | yes | Expected outcome: CEBPA knockdown blunts the alt-T increase in SORT1 enhancer activity. | Expected outcome: no allele-specific enhancer activity and no CEBPA dependence. | Expected outcome: CEBPA knockdown blunts the alt-T increase in CELSR2 enhancer activity. | Expected outcome: CEBPA knockdown has little effect; FOXA1 knockdown blunts enhancer activity. |

## Next experiment

Allele-specific CEBPA ChIP-qPCR or EMSA at chr1:109274968 in HepG2/Hep3B2.1-7, comparing ref G vs alt T; low cost; separates H1 from H0 because H1 predicts stronger CEBPA binding to alt T and H0 predicts no allele-specific CEBPA binding.

## Investigate calls

- chip_peaks({"tf": "CEBPA", "biosample": "HepG2"})
- literature_search({"query": "C/EBP SORT1 1p13 noncoding variant enhancer allele-specific LDL rs12740374"})
- gene_disease({"gene": "SORT1"})

## Flags

- quote_rejected: PMID 29097363: not an exact substring of the abstract
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

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SORT1%20AND%20%28%22ldl%20cholesterol%22%20OR%20%22myocardial%20infarction%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:19:55+00:00)

> Europe PMC: 868 hits for 'SORT1 AND ("ldl cholesterol" OR "myocardial infarction")'; top 8 with PMIDs:
> PMID 41892715 (2026): Genome-Wide Association Studies of Myocardial Infarction: A Systematic Literature Review.
> PMID 42615437 (2026): South Asian Cardiovascular Risk: Role of Coronary Artery Calcium Scoring and Computed Tomography Angiography.
> PMID 42820291 (2026): Clinical trials in a dish: cardiometabolic drug development with biological and digital twins.
> PMID 42019808 (2026): Causal statistical association between remnant cholesterol and coronary heart disease: genetic insights into the PSRC1-CELSR2-SORT1 gene cluster.
> PMID 41999980 (2026): From lipoprotein metabolism to blood clotting: Highlights of the 2025 Fredrickson lipid research conference.
> PMID 42358645 (2026): The role of sortilin in cardiovascular calcification: mechanisms and therapeutic potential.
> PMID 39858645 (2025): Research Progress and Clinical Translation Potential of Coronary Atherosclerosis Diagnostic Markers from a Genomic Perspective.
> PMID 42511725 (2026): Special Issue "Advances in Molecular Forensic Pathology and Toxicology: An Update".

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 42019808 (https://europepmc.org/article/MED/42019808; retrieved 2026-10-26T20:19:55+00:00)

> Colocalization identified shared signals at the PSRC1-CELSR2-SORT1 locus, with lead variants rs[masked] and rs[masked].

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 42019808 (https://europepmc.org/article/MED/42019808; retrieved 2026-10-26T20:19:55+00:00)

> Hepatic expression of PSRC1-CELSR2-SORT1 protects against CHD via RC reduction, independent of LDL-C, supporting RC as promising target for CHD prevention.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 39858645 (https://europepmc.org/article/MED/39858645; retrieved 2026-10-26T20:19:55+00:00)

> GWASs and sequencing studies have identified key genetic variations associated with CAD, including JCAD/KIAA1462, GUCY1A3, PCSK9, and SORT1, which regulate inflammation, lipid metabolism, and vascular function.

<a id="e19"></a>**E19** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:30:36+00:00)

> 1 ENCODE CEBPA ChIP-seq peaks contain chr1:109274968:G>T in biosamples matching 'HepG2': biosamples HepG2; experiments ENCSR142IGM.

<a id="e20"></a>**E20** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=C/EBP%20SORT1%201p13%20noncoding%20variant%20enhancer%20allele-specific%20LDL%20rs12740374&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:24:42+00:00)

> Europe PMC: 10 hits for 'C/EBP SORT1 1p13 noncoding variant enhancer allele-specific LDL rs[masked]'; top 8 with PMIDs:
> PMID 38266112 (2024): Genome-Wide Genetic Associations Prioritize Evaluation of Causal Mechanisms of Atherosclerotic Disease Risk.
> PMID 29097363 (2018): Interrogation of the Atherosclerosis-Associated <i>SORT1</i> (Sortilin 1) Locus With Primary Human Hepatocytes, Induced Pluripotent Stem Cell-Hepatocytes, and Locus-Humanized Mice.
> PMID 31380393 (2019): Relevance of Multi-Omics Studies in Cardiovascular Diseases.
> PMID 31395865 (2019): Saturation mutagenesis of twenty disease-associated regulatory elements at single base-pair resolution.
> PMID 29915816 (2018): From Genotype to Phenotype: A Primer on the Functional Follow-up of Genome-Wide Association Studies in Cardiovascular Disease.
> PMID 21287300 (2011): Genome-wide association studies complemented with mechanistic biological studies identify sortilin 1 as a novel regulator of cholesterol trafficking. [no abstract]
> PMID 20686566 (2010): From noncoding variant to phenotype via SORT1 at the 1p13 cholesterol locus.
> PMID 25870159 (2015): Genome-wide association studies of late-onset cardiovascular disease.

<a id="e21"></a>**E21** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'
