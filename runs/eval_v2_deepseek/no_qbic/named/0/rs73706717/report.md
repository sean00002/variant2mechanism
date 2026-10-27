# rs73706717 and Colorectal cancer (8q24)

Configuration `no_qbic`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.04 over 8 model calls; 165 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H4: Null: no TF-mediated effect of rs73706717 (p = 0.46)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at this base.; No allele-specific effect on POU5F1B or MYC expression in HCT116 or colon tissue.; Any disease association is explained by linkage to another 8q24 variant, a passenger/weak effect, or no effect of this base.

Falsified if: Allele-specific TF binding and enhancer activity are demonstrated at this base, and perturbation of the candidate TF changes the target gene in HCT116.; A direct colorectal cancer GWAS or eQTL signal maps to this variant independently of nearby 8q24 variants.

### 2. H1: TCF7L2 enhancer effect on POU5F1B (p = 0.31)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The chain hypothesis is that TCF7L2 binds this element more strongly on alt C. TCF7L2 is selected because it has HCT116 ChIP-seq peaks containing the variant and is highly expressed in HCT116 (rank 53 of 1626 TFs), whereas many other listed bound TFs are supported only in other biosamples. No QBiC-SELEX model or allele-specific ChIP/reporter data is supplied for TCF7L2, so the alt>C direction is unmeasured. | supported | [E04](#e04), [E05](#e05) |
| element | The variant lies in cCRE EH38E3858447 (pELS) with DNase, H3K27ac and CTCF signal, so it is in an enhancer-like element; these are ENCODE maxima, not HCT116-specific or allele-specific activity measurements. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is the nearest protein-coding gene and the variant is in a POU5F1B intron; L2G also favors POU5F1B, but the L2G sets are non-CRC with PIP 0.04, colon eQTLs are absent, and E21 shows POU5F1B is not a colorectal dependency. Target assignment is therefore plausible but unproven. | weak | [E01](#e01), [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20), [E21](#e21) |
| cell_type | HCT116 is the supplied colorectal carcinoma context and has TCF7L2 occupancy over the variant plus high TCF7L2 expression. | supported | [E04](#e04), [E05](#e05) |
| phenotype | If causal, allele-specific TCF7L2 binding at this enhancer would alter POU5F1B expression and contribute to 8q24 colorectal cancer; the chain's stated direction is increased POU5F1B, but the sign is unproven and TCF7L2 could repress. Direct support is absent: no GWAS Catalog association for rs73706717, no colon eQTL, and POU5F1B is not a colorectal-lineage dependency. E18 is gene-level literature, not variant-specific. | missing | [E15](#e15), [E17](#e17), [E18](#e18), [E20](#e20), [E21](#e21) |

Predictions: Allele-specific TCF7L2 ChIP or enhancer reporter assays show stronger TCF7L2 binding and stronger enhancer activity for alt C than ref T.; TCF7L2 knockdown or CRISPR disruption of EH38E3858447 changes POU5F1B expression in HCT116.; The variant shows an allele-specific effect on POU5F1B but not on MYC.

Falsified if: No allele-specific TCF7L2 binding or enhancer activity is detected at this base.; TCF7L2 perturbation or EH38E3858447 disruption does not change POU5F1B expression in HCT116.; Colon eQTL or 3C/CRISPR evidence links this variant to MYC rather than POU5F1B.

### 3. H3: SP1 enhancer effect on POU5F1B (p = 0.14)

TF SP1 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E3858447 pELS; gene POU5F1B; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The chain hypothesis is that SP1 binds this element more strongly on alt C. SP1 is selected because it has HCT116 ChIP-seq peaks containing the variant and is expressed in HCT116 (rank 118 of 1626 TFs). No QBiC-SELEX model or allele-specific ChIP/reporter data is supplied for SP1, so the alt>C direction is a motif-based hypothesis, not a measured allelic effect. | weak | [E04](#e04), [E06](#e06) |
| element | The variant lies in the active pELS EH38E3858447, a proximal enhancer-like element with DNase and H3K27ac signal; the annotation is not HCT116-specific or allele-specific. | supported | [E03](#e03) |
| gene | POU5F1B is the nearest protein-coding gene and the variant is in a POU5F1B intron; L2G favors POU5F1B but with non-CRC sets and PIP 0.04, colon eQTLs are absent, and E21 shows POU5F1B is not a colorectal dependency. The enhancer-gene link is therefore weak. | weak | [E01](#e01), [E02](#e02), [E16](#e16), [E17](#e17), [E20](#e20), [E21](#e21) |
| cell_type | HCT116 is the supplied colorectal carcinoma context and has SP1 occupancy over the variant plus SP1 expression. | supported | [E04](#e04), [E06](#e06) |
| phenotype | The chain posits that SP1-mediated enhancer activity increases POU5F1B expression and contributes to colorectal cancer biology, but there is no GWAS Catalog association for rs73706717, no colon eQTL, and no variant-specific SP1/POU5F1B assay; E18 is gene-level literature. | missing | [E15](#e15), [E17](#e17), [E18](#e18), [E20](#e20), [E21](#e21) |

Predictions: SP1 ChIP or reporter assays show allele-specific SP1 binding and enhancer activity favoring alt C.; SP1 knockdown reduces POU5F1B expression in HCT116.; TCF7L2 binding at this base is not allele-specific.

Falsified if: No allele-specific SP1 binding or enhancer activity is detected at this base.; SP1 knockdown does not change POU5F1B expression in HCT116.; Allele-specific binding at this base is attributable to TCF7L2 rather than SP1.

### 4. H2: TCF7L2 enhancer effect on MYC (p = 0.09)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element EH38E3858447 pELS; gene MYC; cell type HCT116 colorectal carcinoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The chain hypothesis is that TCF7L2 binds this element more strongly on alt C. TCF7L2 has HCT116 ChIP-seq peaks containing the variant and is highly expressed in HCT116, but no QBiC-SELEX model or allele-specific ChIP/reporter data is supplied, so the alt>C direction is unmeasured. Other listed TFs such as CTCF, CEBPB and MYBL2 are bound only in other biosamples, which is why TCF7L2 is preferred over them. | weak | [E04](#e04), [E05](#e05), [E07](#e07), [E08](#e08), [E09](#e09) |
| element | The variant is in the pELS EH38E3858447, an active enhancer-like element by DNase and H3K27ac annotation; the evidence is ENCODE-wide, not HCT116-specific or allelic. | supported | [E03](#e03) |
| gene | MYC is a canonical 8q24 colorectal cancer target 334 kb upstream, and E19 names a colorectal cancer-associated MYC-335 enhancer in this region, but that study characterized rs67491583, not rs73706717. No 3C/CRISPR/eQTL evidence shows this element contacts MYC, and POU5F1B is closer and in the variant-containing transcript. | weak | [E01](#e01), [E02](#e02), [E18](#e18), [E19](#e19) |
| cell_type | HCT116 has TCF7L2 occupancy over the variant and high TCF7L2 expression, but this does not establish a broader 8q24-active cell context or allele-specific activity. | supported | [E04](#e04), [E05](#e05) |
| phenotype | The chain posits that allele-specific TCF7L2 binding increases MYC expression and contributes to colorectal cancer, but there is no GWAS Catalog association for rs73706717, no colon eQTL, and no variant-specific MYC regulatory assay; E18 is generic MYC/ecDNA literature. | missing | [E15](#e15), [E17](#e17), [E18](#e18), [E20](#e20) |

Predictions: Allele-specific enhancer assays show alt C increases activity, and 3C/CRISPR assays link EH38E3858447 to MYC rather than POU5F1B.; TCF7L2 perturbation changes MYC expression in HCT116.; POU5F1B is not the primary target of this element.

Falsified if: 3C/CRISPR or eQTL evidence links EH38E3858447 to POU5F1B rather than MYC.; TCF7L2 perturbation does not change MYC expression in HCT116.; No allele-specific TCF7L2 binding or enhancer activity is detected at this base.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H3 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 ChIP-qPCR at rs73706717 in a heterozygous colorectal line (HCT116 if heterozygous), comparing T and C alleles. | low | yes | No reproducible allele-specific TCF7L2 binding at this base. | Alt C increases TCF7L2 binding and TCF7L2-dependent enhancer activity, with a downstream change in POU5F1B. | No allele-specific TCF7L2 binding at this base; any allelic effect is SP1-mediated. | Alt C increases TCF7L2 binding, but the regulatory target is MYC rather than POU5F1B. |
| Allele-specific SP1 ChIP-qPCR or small reporter assay at rs73706717 in HCT116. | low | no | No allele-specific SP1 binding at this base. | No allele-specific SP1 binding at this base. | Alt C increases SP1 binding and SP1-dependent enhancer activity. | No allele-specific SP1 binding at this base. |
| Colon transverse eQTL lookup for rs73706717 (already reported zero in E20). | low | yes | No allele-specific expression effect in colon tissue. | Alt C is associated with increased POU5F1B expression in colon tissue. | Alt C is associated with increased POU5F1B expression in colon tissue. | Alt C is associated with increased MYC expression in colon tissue. |
| 3C/CRISPRi linking EH38E3858447 to POU5F1B versus MYC in HCT116. | medium | no | The element may contact a gene, but no allele-specific TF-mediated activity is detected. | EH38E3858447 contacts and regulates POU5F1B in HCT116, with allele-specific activity. | EH38E3858447 contacts and regulates POU5F1B in HCT116, with SP1 allele-specific activity. | EH38E3858447 contacts and regulates MYC in HCT116, with allele-specific activity. |
| TCF7L2 knockdown/CRISPRi followed by POU5F1B and MYC expression in HCT116. | medium | no | Any TF loss effect is independent of this variant; no allele-specific effect is seen. | TCF7L2 loss reduces POU5F1B expression in HCT116. | SP1 loss, not TCF7L2 loss, reduces POU5F1B expression. | TCF7L2 loss reduces MYC expression but not POU5F1B. |

## Next experiment

Allele-specific TCF7L2 ChIP-qPCR at rs73706717 in a heterozygous colorectal line (HCT116 if heterozygous), comparing T and C alleles; this directly tests the top non-null chain H1 against the null H4. If HCT116 is homozygous, the cheapest equivalent is a small allele-specific reporter/MPRA containing the EH38E3858447 element with T versus C.

## Investigate calls

- literature_search({"query": "rs73706717"})
- eqtl_lookup({"tissue": "Colon - Transverse"})
- gene_dependency({"gene": "POU5F1B"})

## Flags

- literature_fallback: no hits for 'rs73706717 AND POU5F1B AND "colorectal cancer"'; dropped the rsID
- quote_rejected: PMID 42465001: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401265-127401265:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:21:56+00:00)

> Variant chr8:127401265:T>C (GRCh38), allele string T/C
> Known IDs: rs73706717
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: -2.8
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401265-128401265?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:21:59+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401265:T>C, by distance to TSS:
> POU5F1B: 79.1 kb from TSS (in gene body, strand +1)
> MYC: 334.2 kb from TSS (upstream, strand +1)
> LRATD2: 842.8 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:21:42+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:127401265:T>C: 149 peaks contain the variant, from 83 factors in 25 biosamples. In the matching biosample HCT116: 3 peaks from 3 factors. cCRE class at the variant: pELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, CHD4, EP300, HDAC1, HDAC2, HMGXB4, KDM1A, KDM6A, LCORL, LIN54, MED1, MED13 (+26 more). Bound, expressed TFs with a binding model: 40; listed one per row: TCF7L2, SP1, CTCF, CEBPB, MYBL2, NR2C2, TFAP4, ISL2, NR2F2, ERF; also bound: NR2F6, NFIC, ELF1, ZNF317, NFIL3, ZBTB7B, KLF16, PITX1, JUNB, SKI, CREM, RXRB, ATF2, ZNF609, ZNF280D, ZNF12, AHDC1, ZNF652, PHF21A, ETS1, NFIA, NR3C1, BCL6, PRDM10, HOXA3, HNF4A, MNX1, HNF1B, ZNF362, FOXA1. Bound but below 1 TPM: FOXA2, HNF1A, ONECUT1, SOX6, TBX2. Assayed with no peak here: 11 TFs in the matching biosample, 517 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000EUV). 63.61 TPM in DepMap:ACH-000971 (HCT 116), rank 53 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000BSF). 38.96 TPM in DepMap:ACH-000971 (HCT 116), rank 118 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 34 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, C4-2B, Panc1, RWPE2, adrenal gland, astrocyte (+13 more) (e.g. ENCSR173IEA). 50.0 TPM in DepMap:ACH-000971 (HCT 116), rank 78 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BQI). 13.15 TPM in DepMap:ACH-000971 (HCT 116), rank 408 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 67.51 TPM in DepMap:ACH-000971 (HCT 116), rank 46 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR559ZKI). 22.6 TPM in DepMap:ACH-000971 (HCT 116), rank 244 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TFAP4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR587BVQ). 19.72 TPM in DepMap:ACH-000971 (HCT 116), rank 283 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ISL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR492IHH). 2.77 TPM in DepMap:ACH-000971 (HCT 116), rank 862 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BVM). 61.74 TPM in DepMap:ACH-000971 (HCT 116), rank 58 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ERF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR159DQO). 46.58 TPM in DepMap:ACH-000971 (HCT 116), rank 90 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs73706717&size=100; retrieved 2026-10-26T02:21:56+00:00)

> 0 GWAS Catalog associations for rs73706717, strongest first:

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:21:56+00:00)

> 2 credible sets contain 8_127401265_T_C: 2 GWAS, 0 molecular QTL.
> GWAS prostate-specific antigen (PSA, maximum, inv-norm transforme: PIP 0.04; L2G POU5F1B 0.83
> GWAS Urinary incontinence (PheCode 599.4): PIP 0.04; L2G POU5F1B 0.78
> Best L2G gene scores across these sets: POU5F1B 0.83

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:21:59+00:00)

> Europe PMC: 150 hits for 'POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 42465001 (2026): Circ_0075829 affects POU5F1B expression through sponging miR-576-3p to promote growth, invasion, and angiogenesis of colon cancer cells.
> PMID 41993623 (2026): Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research.
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 41930642 (2026): Systematic Identification and Characterization of Causal Risk Genes Implicated in Colorectal Cancer by Integrating GWAS, eQTL, and mQTL Data.
> PMID 42686757 (2026): Phase separation of ecDNA condensates establishes in-trans contact domains that boost selective MYC regulatory interactions.
> PMID 40506516 (2025): Association between methylation quantitative trait loci and colorectal cancer risk, survival and cancer recurrence.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 41196428 (2025): Combined CHK1 and PD-L1 blockade as a novel therapeutic strategy against stemness and immunosuppression in ovarian cancer.

<a id="e19"></a>**E19** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs73706717&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:33:34+00:00)

> Europe PMC: 1 hits for 'rs73706717'; top 1 with PMIDs:
> PMID 22429595 (2012): Characterization of the colorectal cancer-associated enhancer MYC-335 at 8q24: the role of rs67491583.

<a id="e20"></a>**E20** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e21"></a>**E21** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for POU5F1B (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): -0.09. Bowel lineage, 31 lines: median -0.06, 0% dependent. All 351 lines: median -0.05, 3% dependent.
