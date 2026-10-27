# rs12740374 and LDL cholesterol, myocardial infarction (1p13)

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 9 model calls; 222 s.

Variant `chr1:109274968:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. H5: No TF-mediated effect of this variant (p = 0.50)

Null chain: no TF-mediated effect of this variant.

Predictions: The lipid associations and expression associations may arise from linkage to another causal change or a mechanism that does not involve altered TF binding at this base.; Precise editing of this base will not reproducibly alter SORT1 or CELSR2 expression through a TF-mediated mechanism.

Falsified if: Precise editing of this base reproducibly changes SORT1 or CELSR2 expression, and the allele-dependent effect is shown to depend on a specific TF's occupancy at the variant.

### 2. H1: FOXA1-mediated regulation of SORT1 (p = 0.20)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646; gene SORT1; cell type Liver; the relevant cell type is not resolved.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies the variant in HepG2 and is expressed in the stated liver cancer cell context. FOXA1 is a reasonable lead among the listed liver-context factors because it has more reported HepG2 peaks here than FOXA2 and is more highly expressed in the stated context; this does not establish that it is causal. Alt (T) is the working prediction for stronger binding, not a direction supported by allele-specific evidence: no QBiC-SELEX result is supplied. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies in enhancer-like cCRE EH38E1374646, but the reported activity maxima do not establish activity in liver cells. | supported | [E03](#e03) |
| gene | SORT1 is a plausible target: it has a high locus-to-gene score and the T allele is associated with higher SORT1 expression in bulk liver. These data do not demonstrate that this cCRE or FOXA1 causes the expression association. | supported | [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | A liver-context mechanism is plausible from FOXA1 occupancy in HepG2 and the bulk-liver SORT1 eQTL, but hepatocyte-specific enhancer activity or FOXA1 mediation is not established. | weak | [E05](#e05), [E17](#e17), [E21](#e21) |
| phenotype | The variant is associated with cholesterol and LDL traits. Several reported associations list G as the effect allele, whereas T is associated with higher liver SORT1 expression; the evidence does not establish that this expression change mediates the lipid associations. Literature describes protective effects of hepatic expression of the gene cluster, not a FOXA1-mediated effect of this variant. | weak | [E15](#e15), [E18b](#e18b) |

Predictions: Precise G-to-T editing in an appropriate liver-cell model will change SORT1 expression in the direction suggested by the liver eQTL, and FOXA1 perturbation will attenuate that allele-dependent difference.; FOXA1 occupancy will be higher on T than G if the working binding-direction prediction is correct; the supplied evidence does not establish this direction.

Falsified if: Precise editing produces no reproducible SORT1 expression difference in a relevant liver-cell model.; The allele-dependent SORT1 difference persists unchanged after effective FOXA1 perturbation.

### 3. H4: FOXA1-mediated regulation of CELSR2 (p = 0.16)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646; gene CELSR2; cell type Liver; the relevant cell type is not resolved.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 occupies the variant in HepG2 and is expressed in the stated context. It is a candidate, not a demonstrated mediator. Alt (T) is the working prediction for stronger binding, not a direction supported by allele-specific evidence: no QBiC-SELEX result is supplied. | weak | [E04](#e04), [E05](#e05) |
| element | The variant lies in enhancer-like cCRE EH38E1374646, but liver-specific activity is not established. | supported | [E03](#e03) |
| gene | CELSR2 is a plausible alternative target because it has a high locus-to-gene score and the T allele is associated with higher CELSR2 expression in bulk liver. The evidence does not resolve CELSR2 versus SORT1 as the causal target. | supported | [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | FOXA1 occupancy in HepG2 and the bulk-liver CELSR2 eQTL are consistent with a liver-context mechanism, but do not establish cell-specific enhancer activity or FOXA1 mediation. | weak | [E05](#e05), [E17](#e17), [E21](#e21) |
| phenotype | The variant is associated with cholesterol and LDL traits, but the supplied evidence does not establish that altered CELSR2 expression mediates those associations. | weak | [E15](#e15), [E16](#e16) |

Predictions: Precise G-to-T editing in an appropriate liver-cell model will change CELSR2 expression in the direction suggested by the liver eQTL, and FOXA1 perturbation will attenuate that allele-dependent difference.; The allele-dependent expression effect will be clearer for CELSR2 than for SORT1 in a targeted test of both genes.

Falsified if: Precise editing produces no reproducible CELSR2 expression difference in a relevant liver-cell model.; The allele-dependent CELSR2 difference persists unchanged after effective FOXA1 perturbation.

### 4. H2: FOXA2-mediated regulation of SORT1 (p = 0.08)

TF FOXA2 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646; gene SORT1; cell type Liver; the relevant cell type is not resolved.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA2 occupies the variant in HepG2 and is expressed in the stated context. FOXA2 has related binding specificity to FOXA1, and the available occupancy evidence does not distinguish their causal roles. Alt (T) is the working prediction for stronger binding, not a direction supported by allele-specific evidence: no FOXA2 QBiC-SELEX result is supplied. | weak | [E04](#e04), [E09](#e09) |
| element | The variant lies in enhancer-like cCRE EH38E1374646; liver-specific activity is not established by the supplied biosample-maximal scores. | supported | [E03](#e03) |
| gene | SORT1 is a plausible target based on its high locus-to-gene score and the positive T-allele liver eQTL, but neither result assigns the effect to FOXA2 or to this element. | supported | [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | FOXA2 occupancy in HepG2 and a bulk-liver SORT1 eQTL are consistent with a liver-context mechanism, but do not establish hepatocyte-specific enhancer activity or FOXA2 mediation. | weak | [E09](#e09), [E17](#e17), [E21](#e21) |
| phenotype | The variant is associated with cholesterol and LDL traits, but the evidence does not connect a FOXA2-dependent expression change to those traits. | weak | [E15](#e15) |

Predictions: If FOXA2 mediates the liver eQTL, precise editing will alter SORT1 expression and FOXA2 perturbation will attenuate the allele-dependent difference.; In matched perturbation experiments, FOXA2 loss will attenuate the allele-dependent SORT1 effect more than FOXA1 or USF1 loss.

Falsified if: Effective FOXA2 perturbation leaves the allele-dependent SORT1 expression difference unchanged.; The variant has no reproducible effect on SORT1 expression after precise editing in a relevant liver-cell model.

### 5. H3: USF1-mediated regulation of SORT1 (p = 0.06)

TF USF1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E1374646; gene SORT1; cell type Liver; the relevant cell type is not resolved.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | USF1 occupies the variant in HepG2 and is highly expressed in the stated context. Its occupancy makes it a candidate, but does not show that it mediates the variant effect. Alt (T) is the working prediction for stronger binding, not a direction supported by allele-specific evidence: no USF1 QBiC-SELEX result is supplied. | weak | [E04](#e04), [E10](#e10) |
| element | The variant lies in enhancer-like cCRE EH38E1374646, although the activity maxima are not liver-specific. | supported | [E03](#e03) |
| gene | SORT1 is a plausible target because of its high locus-to-gene score and the positive T-allele liver eQTL; these data do not establish USF1-dependent regulation. | supported | [E16](#e16), [E17](#e17), [E21](#e21) |
| cell_type | USF1 occupancy in HepG2 and the bulk-liver SORT1 eQTL are consistent with a liver-context hypothesis, but do not resolve the relevant liver cell type or establish USF1 mediation. | weak | [E10](#e10), [E17](#e17), [E21](#e21) |
| phenotype | The variant is associated with cholesterol and LDL traits, but no supplied evidence establishes a USF1-mediated path from this variant to those traits. | weak | [E15](#e15) |

Predictions: If USF1 mediates the liver eQTL, precise editing will alter SORT1 expression and USF1 perturbation will attenuate the allele-dependent difference.; USF1 perturbation, rather than FOXA1 or FOXA2 perturbation, will preferentially attenuate the allele-dependent SORT1 effect.

Falsified if: Effective USF1 perturbation leaves the allele-dependent SORT1 expression difference unchanged.; The variant has no reproducible effect on SORT1 expression after precise editing in a relevant liver-cell model.

## Prediction matrix

| Test | Cost | Separates top two | H5 | H1 | H4 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Paired G/T allele reporter assay in a liver-context cell line, with and without FOXA1 depletion; measure reporter output. | low | yes | No reproducible allele-dependent, FOXA1-dependent reporter effect. | Allele-dependent reporter output is reduced or lost with FOXA1 depletion. | A FOXA1-dependent allele effect may be observed, but this assay alone does not identify CELSR2 as the endogenous target. | Any allele-dependent reporter effect is preferentially reduced by FOXA2 depletion, not FOXA1 depletion. | Any allele-dependent reporter effect is preferentially reduced by USF1 depletion, not FOXA1 depletion. |
| Precise G/T base editing in a liver-context cell model; measure SORT1 and CELSR2 expression, with matched TF perturbations. | high | yes | Editing does not reproducibly produce a TF-dependent expression difference in either candidate gene. | T editing increases SORT1 expression, and FOXA1 perturbation attenuates the difference. | T editing increases CELSR2 expression, and FOXA1 perturbation attenuates the difference. | T editing increases SORT1 expression, and FOXA2 perturbation attenuates the difference. | T editing increases SORT1 expression, and USF1 perturbation attenuates the difference. |

## Next experiment

The cheapest informative first test is a paired G/T allele reporter assay in a liver-context cell line with and without FOXA1 depletion. H1 predicts a FOXA1-dependent allele effect; the null predicts no reproducible FOXA1-dependent effect. A positive reporter result would still require endogenous editing to establish the target gene and causal mechanism.

## Investigate calls

- literature_search({"query": "SORT1 CELSR2 PSRC1 locus liver enhancer variant allele-specific reporter CRISPR perturbation FOXA1 FOXA2 USF1"})
- gene_disease({"gene": "SORT1"})
- eqtl_lookup({"tissue": "Liver"})

## Flags

- tool_failed: E20 gene_disease: Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'

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

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 42358645 (https://europepmc.org/article/MED/42358645; retrieved 2026-10-26T20:19:55+00:00)

> Sortilin (encoded by SORT1), a multi-ligand intracellular trafficking receptor, has recently emerged as a critical molecular mediator linking metabolic risk factors-such as dyslipidemia, diabetes, hypertension, and chronic kidney disease-to pro-calcific cellular responses.

<a id="e18d"></a>**E18d** literature_search, Europe PMC abstract, PMID 39858645 (https://europepmc.org/article/MED/39858645; retrieved 2026-10-26T20:19:55+00:00)

> GWASs and sequencing studies have identified key genetic variations associated with CAD, including JCAD/KIAA1462, GUCY1A3, PCSK9, and SORT1, which regulate inflammation, lipid metabolism, and vascular function.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SORT1%20CELSR2%20PSRC1%20locus%20liver%20enhancer%20variant%20allele-specific%20reporter%20CRISPR%20perturbation%20FOXA1%20FOXA2%20USF1&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:21:11+00:00)

> Europe PMC: 0 hits for 'SORT1 CELSR2 PSRC1 locus liver enhancer variant allele-specific reporter CRISPR perturbation FOXA1 FOXA2 USF1'; top 0 with PMIDs:

<a id="e20"></a>**E20** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'

<a id="e21"></a>**E21** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_109274968_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:30:36+00:00)

> 5 significant GTEx v8 single-tissue eQTLs for chr1_109274968_G_T_b38 in tissues matching 'Liver'. NES is the effect of the alt allele (T) relative to ref (G).
> SORT1 in Liver: NES +1.27, p 3.1e-54
> PSRC1 in Liver: NES +1.24, p 1.1e-37
> CELSR2 in Liver: NES +1.04, p 9.4e-34
> ATXN7L2 in Liver: NES +0.40, p 5.9e-07
> SYPL2 in Liver: NES +0.50, p 1.2e-06
