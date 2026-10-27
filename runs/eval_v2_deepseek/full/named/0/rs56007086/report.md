# rs56007086 and Breast cancer (16q12)

Configuration `full`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 246 s.

Variant `chr16:52565398:G>A` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z 12.52); NR2F2 (bound here, z 10.89); GATA3 (bound here, z 8.32); SPDEF (bound here, z -7.0); FOXA1 (bound here, z 6.27); CEBPB (bound here, z -1.64, no clear allelic change); ELF1 (bound elsewhere, z -47.67); ERF (bound elsewhere, z -47.67); ELF4 (bound elsewhere, z -47.67); GABPA (bound elsewhere, z -47.67). Occupancy unknown: ETV3 (z -47.67); SLC2A4RG (z -45.42); MTERF3 (z 24.43); PBX4 (z 18.55); SOX12 (z 17.9). Diagnostic, not shown to the model: 569 of 997 models pass Bonferroni.

## Ranked chains

### 1. null: No TF-mediated allelic effect of rs56007086; association may be linked or passenger (p = 0.43)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF ChIP or enhancer-reporter difference at this base.; Any breast cancer association at 16q12 is driven by a linked variant or haplotype context, not by rs56007086 itself.; The variant may be a passenger in a regulatory hotspot without a direct allele-specific TF effect.

Falsified if: A robust allele-specific TF occupancy or enhancer activity difference is demonstrated at this base.; CRISPR editing of rs56007086 alone changes TOX3 expression or a breast cancer-relevant phenotype.; Fine-mapping shows this base, rather than a linked variant, is the functional allele.

### 2. chain_SPDEF: Ref allele preserves a stronger SPDEF site in the TOX3 enhancer; alt allele weakens SPDEF binding (p = 0.40)

TF SPDEF (QBiC-SELEX coverage own_model), ref allele binds more; element ENSR16_9QTBS enhancer / nearby dELS at 16q12; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SPDEF binds the ref G allele more strongly than the alt A allele. SPDEF has an ENCODE ChIP-seq peak over the variant in MCF-7 and is well expressed in MCF7. Its own QBiC-SELEX model detects a ref-gain effect (z -7.0, effect -0.244), with the ref site at the 99.7th percentile versus 95.0th for alt. This is the only chain here with an own-model QBiC-SELEX result plus matching MCF-7 occupancy. | supported | [E07](#e07), [E19](#e19), [E23](#e23) |
| element | The variant lies in the VEP-annotated ENSR16_9QTBS enhancer. No cCRE overlaps the base itself; the nearest dELS is 38 bp away and has active enhancer marks (H3K27ac z 6.1, DNase z 4.2). The element shows extensive TF ChIP-seq occupancy, consistent with an active regulatory element, but the cCRE assignment is nearby rather than base-overlapping. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | TOX3 is the nearest protein-coding gene (17.6 kb upstream) and is a breast-cancer-associated locus by Open Targets (overall score 0.58; genetic_association 0.91, literature 0.89). However, there is no GTEx eQTL and no breast eQTL/ASE evidence for this SNP, so the SNP-to-TOX3 link remains inferential. | weak | [E02](#e02), [E37](#e37), [E17](#e17), [E36](#e36) |
| cell_type | MCF7 is a relevant breast cancer epithelial context: SPDEF is expressed in DepMap MCF7 at 72.51 TPM (rank 40/1626) and has an ENCODE ChIP-seq peak over the variant in MCF-7. | supported | [E07](#e07), [E23](#e23) |
| phenotype | TOX3 is linked to breast cancer in Open Targets and locus literature, but the supplied evidence does not establish that this base changes TOX3 expression or disease risk. If SPDEF activates the enhancer, loss of SPDEF binding on alt would lower TOX3; if SPDEF represses, alt would increase TOX3. The downstream sign is unresolved. | weak | [E37](#e37), [E18a](#e18a), [E18b](#e18b), [E17](#e17), [E36](#e36) |

Predictions: Allele-specific SPDEF ChIP will show higher ref G occupancy than alt A at rs56007086.; SPDEF knockdown or overexpression will alter the allelic enhancer activity of the ENSR16_9QTBS/dELS element in MCF7.; The allele-dependent enhancer effect should be SPDEF-dependent and not require TCF7L2.

Falsified if: SPDEF ChIP is not allele-specific at this base.; The SPDEF ref-gain QBiC-SELEX result does not reproduce in an allele-specific reporter or direct binding assay.; SPDEF perturbation does not alter TOX3 enhancer activity or TOX3 expression.

### 3. chain_TCF7L2: Alt allele creates a stronger TCF7L2 site in the TOX3 enhancer (p = 0.17)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element ENSR16_9QTBS enhancer / nearby dELS at 16q12; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the alt A allele more strongly in the QBiC-SELEX assay (z 12.52, effect 0.745; alt site rises from the 57.0th to 97.8th percentile), and TCF7L2 has an ENCODE ChIP-seq peak over the variant in MCF-7. The evidence is weakened because TCF7L2 has no own QBiC-SELEX model; the best model is CIS-BP-mapped from TCF7L1, and TCF7L2 is expressed at only 4.89 TPM in MCF7. | weak | [E10](#e10), [E19](#e19), [E20](#e20) |
| element | The variant lies in the VEP-annotated ENSR16_9QTBS enhancer. No cCRE overlaps the base; the nearest dELS is 38 bp away and has active enhancer marks and extensive TF ChIP-seq occupancy. The element assignment is therefore nearby-enhancer rather than base-overlapping. | supported | [E01](#e01), [E03](#e03), [E04](#e04) |
| gene | TOX3 is the nearest protein-coding gene and is a breast-cancer-associated locus in Open Targets. No GTEx eQTL and no breast eQTL/ASE support this SNP as a direct TOX3 regulatory variant, so the target-gene link is inferential. | weak | [E02](#e02), [E37](#e37), [E17](#e17), [E36](#e36) |
| cell_type | MCF7 is a relevant breast cancer context and has TCF7L2 ChIP-seq occupancy over the variant. However, TCF7L2 expression is low in MCF7 (4.89 TPM, rank 642/1626), weakening it as the primary allele-specific TF. | weak | [E10](#e10), [E20](#e20) |
| phenotype | TOX3 is linked to breast cancer, but the supplied evidence does not establish that this variant alters TOX3 expression or disease risk. If TCF7L2 activates the enhancer, the alt allele would increase TOX3; if TCF7L2 represses, the direction would reverse. The downstream sign is unresolved. | weak | [E37](#e37), [E18a](#e18a), [E18b](#e18b), [E17](#e17), [E36](#e36) |

Predictions: Allele-specific TCF7L2 ChIP will show higher alt A occupancy than ref G at rs56007086.; The allelic enhancer activity should be TCF7L2-dependent in MCF7.; The effect should be weaker or less reproducible than the SPDEF ref-gain model because TCF7L2 expression is low and the QBiC-SELEX model is mapped from TCF7L1.

Falsified if: TCF7L2 ChIP is not allele-specific at this base.; The TCF7L2 alt-gain QBiC-SELEX result does not reproduce with a TCF7L2-specific assay.; TCF7L2 perturbation does not alter TOX3 enhancer activity or TOX3 expression.

## Prediction matrix

| Test | Cost | Separates top two | null | chain_SPDEF | chain_TCF7L2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific SPDEF ChIP-qPCR/ddPCR at rs56007086 in a heterozygous MCF7/breast line, or SPDEF ChIP in isogenic ref/alt cells | low | yes | No reproducible allele-specific SPDEF occupancy. | Higher SPDEF occupancy on ref G than alt A. | No required SPDEF ref>alt allelic difference; TCF7L2 is primary. |
| Allele-specific TCF7L2 ChIP-qPCR/ddPCR at rs56007086 in MCF7/breast cells | low | no | No reproducible allele-specific TCF7L2 occupancy. | No TCF7L2 alt>ref allelic difference; SPDEF is the primary base-specific TF. | Higher TCF7L2 occupancy on alt A than ref G. |
| Ref-vs-alt enhancer reporter for the ENSR16_9QTBS/dELS element in MCF7, with and without SPDEF knockdown/overexpression | medium | yes | No reproducible ref-vs-alt enhancer activity difference. | A reproducible ref-vs-alt activity difference that is SPDEF-dependent; direction depends on whether SPDEF activates or represses. | A reproducible ref-vs-alt activity difference that is TCF7L2-dependent, not SPDEF-dependent. |
| CRISPR base edit of rs56007086 G>A in MCF7/breast cells, measuring TOX3 enhancer RNA/expression and SPDEF occupancy | high | yes | No TOX3/enhancer RNA change attributable to this base; linked variant or haplotype explains any signal. | The edit changes TOX3 enhancer RNA/expression in a SPDEF-dependent way; SPDEF occupancy is ref>alt. | The edit changes TOX3 enhancer RNA/expression in a TCF7L2-dependent way; TCF7L2 occupancy is alt>ref. |
| Breast eQTL or allele-specific expression for rs56007086–TOX3 (GTEx breast or breast tumor ASE) | low | no | No eQTL/ASE at this SNP. | May show a TOX3 eQTL/ASE; absence is compatible; direction depends on activator/repressor function. | May show a TOX3 eQTL/ASE; absence is compatible. |

## Next experiment

The cheapest experiment that separates the top two chains is allele-specific SPDEF ChIP-qPCR/ddPCR at rs56007086 in a heterozygous breast cancer line (MCF7 if heterozygous; otherwise a heterozygous patient-derived line). The SPDEF chain predicts ref G > alt A SPDEF occupancy, whereas the null predicts no reproducible allele-specific SPDEF occupancy. This is cheaper than enhancer-reporter or CRISPR editing and directly tests the best-supported TF allele effect.

## Investigate calls

- qbic_tf_detail({"tf": "NR2F2"})
- eqtl_lookup({"tissue": "breast"})
- gene_disease({"gene": "TOX3"})

## Flags

- literature_fallback: no hits for 'rs56007086 AND TOX3 AND "breast cancer"'; dropped the rsID

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/16:52565398-52565398:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:25:34+00:00)

> Variant chr16:52565398:G>A (GRCh38), allele string G/A
> Known IDs: rs56007086
> Most severe consequence: intron_variant
> Regulatory features: ENSR16_9QTBS enhancer
> GERP conservation score at the site: -4.73
> Transcript consequences: CASC16 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/16:51565398-53565398?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:25:46+00:00)

> 6 protein-coding genes within 1000 kb of chr16:52565398:G>A, by distance to TSS:
> TOX3: 17.6 kb from TSS (upstream, strand -1)
> CHD9NB: 487.5 kb from TSS (downstream, strand -1)
> CHD9: 489.6 kb from TSS (upstream, strand +1)
> RBL2: 868.6 kb from TSS (upstream, strand +1)
> AKTIP: 939.0 kb from TSS (downstream, strand -1)
> HNRNPA1L3: 1012.0 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:25:06+00:00)

> No cCRE overlaps the variant; nearest is EH38E3180851 (dELS) 38 bp away.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3180851 dELS: DNase z 4.2, H3K27ac z 6.1, H3K4me3 z 1.8, CTCF z 1.9; nearby genes CASC16, TOX3, AC026462.5
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr16:52565398:G>A: 215 peaks contain the variant, from 162 factors in 7 biosamples. In the matching biosample MCF-7: 16 peaks from 11 factors. No cCRE contains the variant. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, ARID5B, ASH2L, BCL3, CBX5, CHD4, CTBP1, EP300, GATAD1, GZF1, HBP1, HDAC1 (+51 more). Bound, expressed TFs with a binding model: 79; listed one per row: FOXA1, GATA3, SPDEF, NR2F2, CEBPB, TCF7L2, MYBL2, SP1, YY1, MAX; also bound: JUND, GATAD2A, BHLHE40, ZGPAT, RXRA, ZNF609, RXRB, ZNF770, FOXP4, AHDC1, GMEB1, ZNF772, ZNF788P, HMG20B, ELF1, ELF3, RELA, TBX2, ERF, HMG20A, CREB1, MBD1, ATF1, CREM, FOSL2, THAP11, SOX13, MEF2A, ZNF703, FOXJ3 (+39 more). Bound but below 1 TPM: DLX6, ETS1, FOXA2, FOXA3, GFI1, HLF, HNF1A, HNF1B, HNF4A, MAFF. Assayed with no peak here: 49 TFs in the matching biosample, 425 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> FOXA1: bound here. 5 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7; also in A549, HepG2, liver (e.g. ENCSR126YEB). 88.38 TPM in DepMap:ACH-000019 (MCF7), rank 28 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GATA3: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000EWV). 346.04 TPM in DepMap:ACH-000019 (MCF7), rank 5 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SPDEF: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR042GSX). 72.51 TPM in DepMap:ACH-000019 (MCF7), rank 40 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000BUY). 38.14 TPM in DepMap:ACH-000019 (MCF7), rank 103 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000BSR). 24.33 TPM in DepMap:ACH-000019 (MCF7), rank 169 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample MCF-7 (e.g. ENCSR000EWT). 4.89 TPM in DepMap:ACH-000019 (MCF7), rank 642 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 49.2 TPM in DepMap:ACH-000019 (MCF7), rank 66 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound elsewhere. 4 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, liver (e.g. ENCSR000BPE). 33.01 TPM in DepMap:ACH-000019 (MCF7), rank 122 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> YY1: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: liver (e.g. ENCSR382MOM). 61.08 TPM in DepMap:ACH-000019 (MCF7), rank 48 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: liver (e.g. ENCSR521IID). 76.95 TPM in DepMap:ACH-000019 (MCF7), rank 35 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs56007086&size=100; retrieved 2026-10-26T02:25:35+00:00)

> 0 GWAS Catalog associations for rs56007086, strongest first:

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:25:34+00:00)

> Open Targets has no record of 16_52565398_G_A.

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565398_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:27:56+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565398_G_A_b38. NES is the effect of the alt allele (A) relative to ref (G).

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

> Key examples include promoter mutations [e.g., rs2279744 (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs4784227 (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 41871294 (https://europepmc.org/article/MED/41871294; retrieved 2026-10-26T02:25:47+00:00)

> Differences in panel performance influenced association signals, including breast cancer candidate loci such as FGFR2, TOX3, and ESR1.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr16:52565398:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000019), bound here before bound elsewhere, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 79 occupied, 5 of 137 with unknown occupancy. Left out: 49 TFs assayed in the matching biosample and 425 assayed only elsewhere, none with a peak here; 20 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer (a CIS-BP-mapped model of TCF7L1), z 12.52, effect 0.745: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.89 TPM, rank 642 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWT. Best model's site strength: ref 57.0th, alt 97.8th percentile of its k-mer coefficients.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model PPARD_eDBD_TGTCTT40NTTC_KR_yin2017_0_2_7mer (a CIS-BP-mapped model of PPARD), z 10.89, effect 0.436: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 38.14 TPM, rank 103 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000BUY. Best model's site strength: ref 77.8th, alt 91.8th percentile of its k-mer coefficients.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): best model GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer (a CIS-BP-mapped model of GATA2), z 8.32, effect 0.197: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 346.04 TPM, rank 5 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000EWV. Best model's site strength: ref 37.1th, alt 35.5th percentile of its k-mer coefficients.

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SPDEF (Ets, 1 model; QBiC-SELEX coverage: own model): best model SPDEF_NA_TCATTG20NCG_ESAD_yang2017_0_3_7mer (its own model), z -7.0, effect -0.244: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 72.51 TPM, rank 40 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR042GSX. Best model's site strength: ref 99.7th, alt 95.0th percentile of its k-mer coefficients.

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FOXA1 (Forkhead, 4 models; QBiC-SELEX coverage: own model): best model FOXA2_eDBD_TTGCGA40NGTA_KT_yin2017_1_2_7mer (a CIS-BP-mapped model of FOXA2), z 6.27, effect 0.131: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 88.38 TPM, rank 28 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR126YEB. Best model's site strength: ref 90.2th, alt 81.8th percentile of its k-mer coefficients.

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPB (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (its own model), z -1.64, effect -0.203: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 24.33 TPM, rank 169 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in MCF-7, e.g. ENCSR000BSR. Best model's site strength: ref 76.8th, alt 75.0th percentile of its k-mer coefficients.

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ELF1 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z -47.67, effect -0.77: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 57.44 TPM, rank 52 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR321VGW. Best model's site strength: ref 95.8th, alt 86.8th percentile of its k-mer coefficients.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ERF (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z -47.67, effect -0.77: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 35.09 TPM, rank 109 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR159DQO. Best model's site strength: ref 95.8th, alt 86.8th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ELF4 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z -47.67, effect -0.77: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 12.15 TPM, rank 348 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR980HGI. Best model's site strength: ref 95.8th, alt 86.8th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GABPA (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z -47.67, effect -0.77: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.21 TPM, rank 472 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in liver, e.g. ENCSR038GMB. Best model's site strength: ref 95.8th, alt 86.8th percentile of its k-mer coefficients.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z -47.67, effect -0.77: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.33 TPM, rank 516 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.8th, alt 86.8th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SLC2A4RG (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model SLC2A4RG_FL_CT40NGCGCTA_YWPA_jolma2025_0_3_7mer (its own model), z -45.42, effect -4.513: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 148.81 TPM, rank 15 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.9th, alt 93.5th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MTERF3 (mTERF, 1 model; QBiC-SELEX coverage: own model): best model MTERF3_FL_GG40NTAGTTT_YWJA_jolma2025_0_3_7mer (its own model), z 24.43, effect 0.234: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 19.0 TPM, rank 217 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 71.0th, alt 83.4th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> PBX4 (Homeodomain, 1 model; QBiC-SELEX coverage: mapped models only): best model PBX1_eDBD_TAAGTC40NCGT_KR_yin2017_0_4_7mer (a CIS-BP-mapped model of PBX1), z 18.55, effect 0.733: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.15 TPM, rank 766 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 75.2th, alt 97.8th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SOX12 (HMG/Sox, 18 models; QBiC-SELEX coverage: own model): best model SOX18_eDBD_TCACGC40NACT_KP_yin2017_0_4_7mer (a CIS-BP-mapped model of SOX18), z 17.9, effect 0.672: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.17 TPM, rank 439 of 1626 TFs in DepMap:ACH-000019 (MCF7). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 74.4th, alt 82.6th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"NR2F2","symbol":"NR2F2","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565398:G>A","gate_p":5.02e-05,"models":[{"model":"COUP-TF2_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer","mapping":"own","group":"G002 Nuclear receptor, 29 models","quality":0.896,"effect":-0.091,"z":-2.51,"p":0.012,"rank_abs_z":"717/997","passed_gate":false,"site_strength":{"ref_percentile":79.5,"alt_percentile":94.5,"k":7}},{"model":"ESR1_eDBD_TGTGGG40NAAC_KV_yin2017_0_4_7mer","mapping":"CIS-BP (ESR1)","group":"G002 Nuclear receptor, 29 models","quality":0.64,"effect":0.309,"z":7.83,"p":4.9e-15,"rank_abs_z":"254/997","passed_gate":true,"site_strength":{"ref_percentile":86.1,"alt_percentile":95.0,"k":7}},{"model":"HNF4A_NA_TGACAG20NGA_AF_jolma2013_1_3_7mer","mapping":"CIS-BP (HNF4A)","group":"G078 Nuclear receptor, 2 models","quality":0.709,"effect":-0.045,"z":-1.27,"p":0.2,"rank_abs_z":"855/997","passed_gate":false,"site_strength":{"ref_percentile":71.1,"alt_percentile":93.4,"k":7}},{"model":"HNF4G_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (HNF4G)","group":"G078 Nuclear receptor, 2 models","quality":0.731,"effect":-0.053,"z":-1.52,"p":0.13,"rank_abs_z":"821/997","passed_gate":false,"site_strength":{"ref_percentile":82.8,"alt_percentile":93.3,"k":7}},{"model":"Rev-ErbA-Alpha_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (NR1D1)","group":"G002 Nuclear receptor, 29 models","quality":0.72,"effect":0.143,"z":3.76,"p":0.00017,"rank_abs_z":"585/997","passed_gate":false,"site_strength":{"ref_percentile":85.2,"alt_percentile":89.1,"k":7}},{"model":"NR1D2_eDBD_TGAATT40NTAA_KR_yin2017_0_3_7mer","mapping":"CIS-BP (NR1D2)","group":"G002 Nuclear receptor, 29 models","quality":0.957,"effect":0.272,"z":1.58,"p":0.11,"rank_abs_z":"814/997","passed_gate":false,"site_strength":{"ref_percentile":77.7,"alt_percentile":77.5,"k":7}},{"model":"NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer","mapping":"CIS-BP (NR1H3)","group":"G002 Nuclear receptor, 29 models","quality":0.832,"effect":0.11,"z":6.01,"p":1.8e-09,"rank_abs_z":"384/997","passed_gate":true,"site_strength":{"ref_percentile":83.7,"alt_percentile":87.6,"k":7}},{"model":"FXR_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer","mapping":"CIS-BP (NR1H4)","group":"G002 Nuclear receptor, 29 models","quality":0.83,"effect":-0.019,"z":-0.38,"p":0.71,"rank_abs_z":"953/997","passed_gate":false,"site_strength":{"ref_percentile":86.2,"alt_percentile":94.4,"k":7}},{"model":"NR2C1_eDBD_TATTCA40NAGT_KT_yin2017_0_3_7mer","mapping":"CIS-BP (NR2C1)","group":"G002 Nuclear receptor, 29 models","quality":0.939,"effect":0.523,"z":9.91,"p":3.6e-23,"rank_abs_z":"139/997","passed_gate":true,"site_strength":{"ref_percentile":67.2,"alt_percentile":86.3,"k":7}}],"n_models_trimmed":21}

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565398_G_A_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:27:56+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565398_G_A_b38 in tissues matching 'breast'. NES is the effect of the alt allele (A) relative to ref (G).

<a id="e37"></a>**E37** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:34:32+00:00)

> Open Targets: TOX3 and breast cancer (MONDO_0007254), overall score 0.58; by evidence type: genetic_association 0.91, literature 0.89
