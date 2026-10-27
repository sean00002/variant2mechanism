# rs4784227 and Breast cancer (16q12)

Configuration `full`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 8 model calls; 212 s.

Variant `chr16:52565276:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GATA3 (bound here, z 18.65); FOXA1 (bound here, z 15.4); NR2F2 (bound here, z 9.51); TCF7L2 (bound here, z 8.45); SPDEF (bound here, z 5.89, weak site); MAFK (bound elsewhere, z 71.57); HOMEZ (bound elsewhere, z -49.09); MNX1 (bound elsewhere, z -27.02); PITX1 (bound elsewhere, z -21.39); TFAP4 (bound elsewhere, z 19.55). Occupancy unknown: MAFA (z 71.57); MAFB (z 71.57); LHX2 (z 28.05); LHX4 (z 28.05); LMX1B (z 28.05). Diagnostic, not shown to the model: 290 of 997 models pass Bonferroni.

## Ranked chains

### 1. H2: GATA3-dependent enhancer effect on TOX3 (p = 0.38)

TF GATA3 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps a distal enhancer-like cCRE, but its chromatin annotations do not establish MCF-7-specific or allele-specific enhancer activity.; gene TOX3 is prioritized by proximity and locus-to-gene scoring; literature reports a genotype association with TOX3 expression in breast tumors, but a direct enhancer connection and expression direction are unresolved.; cell type MCF-7 is a plausible context because GATA3 is highly expressed there and has ChIP-seq occupancy over the variant..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 is the leading TF candidate because it is highly expressed and occupied at the site in MCF-7, and its own QBiC-SELEX model as well as a GATA2-mapped model predict stronger binding to T; these in-vitro results do not prove allele-specific occupancy in cells. | supported | [E06](#e06), [E20](#e20), [E37](#e37) |
| element | The variant lies in a distal enhancer-like cCRE with regulatory chromatin annotations, although the reported maxima do not establish activity in MCF-7 or an allelic difference. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is a candidate target based on proximity and locus-to-gene prioritization, and a literature report describes a genotype association with TOX3 expression in breast tumors; direct regulation by this cCRE and the expression direction remain unshown. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E35c](#e35c), [E36](#e36) |
| cell_type | GATA3 occupancy over the variant and high GATA3 expression are reported in MCF-7, making it a plausible context to test this chain. | supported | [E04](#e04), [E06](#e06) |
| phenotype | T is associated with breast-cancer risk, but the evidence does not show that GATA3-mediated regulation explains this association or whether increased binding raises or lowers risk. | supported | [E15](#e15), [E16](#e16) |

Predictions: If GATA3 mediates the allelic effect, the variant-dependent regulatory output should be more sensitive to GATA3 perturbation than to FOXA1 perturbation.; A GATA3-dependent effect should be detectable in an assay comparing the C and T enhancer alleles, but its direction for TOX3 expression is not established by the current evidence.

Falsified if: A sensitive allele-resolved assay finds no T-favoring GATA3 occupancy in a relevant context.; GATA3 perturbation does not alter the C-versus-T regulatory difference in a relevant assay.

### 2. H1: FOXA1-dependent enhancer effect on TOX3 (p = 0.27)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps a distal enhancer-like cCRE, but the available chromatin maxima are not MCF-7-specific and do not establish allele-specific activity.; gene TOX3 is prioritized by proximity and locus-to-gene scoring; literature reports a genotype association with TOX3 expression in breast tumors, but the direction and direct enhancer connection are unresolved.; cell type MCF-7 is a plausible context because FOXA1 is expressed there and has ChIP-seq occupancy over the variant..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 is a plausible mediator because it is occupied at the site and expressed in MCF-7; the QBiC-SELEX model mapped from FOXA2 predicts stronger binding to T, and literature proposes altered FOXA1 affinity, but neither establishes a FOXA1-specific allelic effect in cells. | weak | [E05](#e05), [E21](#e21), [E35a](#e35a), [E35b](#e35b) |
| element | The variant lies in a distal enhancer-like cCRE with regulatory chromatin annotations, although the reported maxima do not establish activity in MCF-7 or an allelic difference. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is a candidate target based on proximity and locus-to-gene prioritization, and a literature report describes a genotype association with TOX3 expression in breast tumors; direct regulation by this cCRE and the expression direction remain unshown. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E35c](#e35c), [E36](#e36) |
| cell_type | FOXA1 occupancy over the variant and high FOXA1 expression are reported in MCF-7, making it a plausible context to test this chain. | supported | [E04](#e04), [E05](#e05) |
| phenotype | T is associated with breast-cancer risk, but the evidence does not show that FOXA1-mediated regulation explains this association or whether increased binding raises or lowers risk. | supported | [E15](#e15), [E16](#e16) |

Predictions: If FOXA1 mediates the allelic effect, the variant-dependent regulatory output should be more sensitive to FOXA1 perturbation than to GATA3 perturbation.; A FOXA1-dependent effect should be detectable in an assay comparing the C and T enhancer alleles, but its direction for TOX3 expression is not established by the current evidence.

Falsified if: A sensitive allele-resolved assay finds no T-favoring FOXA1 occupancy in a relevant context.; FOXA1 perturbation does not alter the C-versus-T regulatory difference in a relevant assay.

### 3. H5: Null: no TF-mediated effect of rs4784227 (p = 0.27)

Null chain: no TF-mediated effect of this variant.

Predictions: The breast-cancer association may arise from a linked causal variant, or rs4784227 may have no consequential TF-mediated effect despite the in-vitro binding predictions and ChIP overlap.; Editing the variant or perturbing the candidate element may produce no reproducible allele-dependent regulatory change.

Falsified if: Precise editing of C to T reproducibly changes TF occupancy and enhancer-dependent gene regulation in a relevant breast-cell context, and factor-specific perturbation supports mediation by a TF at this base.

### 4. H3: NR2F2-dependent enhancer effect on TOX3 (p = 0.05)

TF NR2F2 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps a distal enhancer-like cCRE, but the available chromatin evidence does not establish allele-specific enhancer activity.; gene TOX3 is prioritized by proximity and locus-to-gene scoring; direct regulation by this cCRE remains unshown.; cell type MCF-7 is a possible context because NR2F2 is expressed there and has a ChIP-seq peak over the variant..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NR2F2 is occupied at the variant and expressed in MCF-7; a QBiC-SELEX model mapped from PPARG predicts stronger binding to T, so the allelic prediction is indirect for NR2F2. | weak | [E08](#e08), [E22](#e22) |
| element | The variant lies in a distal enhancer-like cCRE with regulatory chromatin annotations, but these do not establish allele-specific activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is a plausible target based on proximity and locus-to-gene prioritization, but direct regulation by this cCRE is not demonstrated. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | NR2F2 occupancy over the variant and expression are reported in MCF-7, making this a possible context to test the chain. | supported | [E04](#e04), [E08](#e08) |
| phenotype | T is associated with breast-cancer risk, but these data do not connect NR2F2 binding to a risk-promoting regulatory effect. | supported | [E15](#e15), [E16](#e16) |

Predictions: A NR2F2-mediated model predicts that the C-versus-T regulatory difference will depend on NR2F2, rather than selectively on FOXA1 or GATA3.; If the mapped in-vitro prediction transfers to cells, NR2F2 occupancy should favor T; a regulatory effect on TOX3 remains a testable, unconfirmed consequence.

Falsified if: A sensitive allele-resolved assay finds no T-favoring NR2F2 occupancy in a relevant context.; NR2F2 perturbation does not alter the C-versus-T regulatory difference when the element is active.

### 5. H4: TCF7L2-dependent enhancer effect on TOX3 (p = 0.03)

TF TCF7L2 (QBiC-SELEX coverage mapped), alt allele binds more; element The variant overlaps a distal enhancer-like cCRE, but the available chromatin evidence does not establish allele-specific enhancer activity.; gene TOX3 is prioritized by proximity and locus-to-gene scoring; direct regulation by this cCRE remains unshown.; cell type MCF-7 is a possible context because a TCF7L2 ChIP-seq peak overlaps the variant there, although reported expression is comparatively low..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 has a reported MCF-7 ChIP-seq peak over the variant and a QBiC-SELEX model mapped from TCF7 predicts stronger binding to T; the prediction is indirect for TCF7L2, which is expressed at comparatively low levels. | weak | [E09](#e09), [E23](#e23) |
| element | The variant lies in a distal enhancer-like cCRE with regulatory chromatin annotations, but these do not establish allele-specific activity. | supported | [E01](#e01), [E03](#e03) |
| gene | TOX3 is a plausible target based on proximity and locus-to-gene prioritization, but direct regulation by this cCRE is not demonstrated. | supported | [E02](#e02), [E16](#e16), [E17](#e17), [E36](#e36) |
| cell_type | TCF7L2 occupancy over the variant is reported in MCF-7, but its comparatively low reported expression makes this context less compelling than for GATA3 or FOXA1. | supported | [E04](#e04), [E09](#e09) |
| phenotype | T is associated with breast-cancer risk, but the evidence does not show that TCF7L2 binding mediates that association. | supported | [E15](#e15), [E16](#e16) |

Predictions: A TCF7L2-mediated model predicts that the C-versus-T regulatory difference will depend on TCF7L2, rather than selectively on FOXA1 or GATA3.; If the mapped in-vitro prediction transfers to cells, TCF7L2 occupancy should favor T; a regulatory effect on TOX3 remains unconfirmed.

Falsified if: A sensitive allele-resolved assay finds no T-favoring TCF7L2 occupancy in a relevant context.; TCF7L2 perturbation does not alter the C-versus-T regulatory difference when the element is active.

## Prediction matrix

| Test | Cost | Separates top two | H2 | H1 | H5 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-resolved CUT&RUN or ChIP-qPCR for GATA3 and FOXA1 in an informative MCF-7 genotype or edited isogenic cells. | medium | no | GATA3 occupancy is predicted to favor T if this chain is correct; FOXA1 occupancy may also be present but is not the proposed mediator. | FOXA1 occupancy is predicted to favor T if this chain is correct; GATA3 occupancy may also be present but is not the proposed mediator. | No reproducible allele-dependent occupancy difference is expected to support a consequential TF-mediated effect. | This chain does not predict a decisive FOXA1-versus-GATA3 result; NR2F2 occupancy should be tested separately. | This chain does not predict a decisive FOXA1-versus-GATA3 result; TCF7L2 occupancy should be tested separately. |
| Matched C- and T-allele enhancer reporter in MCF-7 with separate FOXA1 and GATA3 depletion; measure the allele-by-depletion interaction. | medium | yes | The C-versus-T reporter difference should be preferentially reduced by GATA3 depletion. | The C-versus-T reporter difference should be preferentially reduced by FOXA1 depletion. | No reproducible C-versus-T reporter difference dependent on either factor is expected. | Neither FOXA1 nor GATA3 depletion is predicted to selectively remove the difference; NR2F2 dependence is predicted instead. | Neither FOXA1 nor GATA3 depletion is predicted to selectively remove the difference; TCF7L2 dependence is predicted instead. |
| Precisely edit C to T and T to C in isogenic MCF-7 cells, then measure allele-dependent expression of TOX3 and nearby candidate genes. | high | no | Editing is predicted to change regulatory output; a TOX3 change is a candidate outcome, with direction not specified. | Editing is predicted to change regulatory output; a TOX3 change is a candidate outcome, with direction not specified. | No reproducible expression change attributable to the edited base is expected. | Editing is predicted to change regulatory output if the NR2F2-mediated chain is correct; target and direction remain uncertain. | Editing is predicted to change regulatory output if the TCF7L2-mediated chain is correct; target and direction remain uncertain. |
| Perturb the cCRE and test its physical or functional connection to TOX3, for example by enhancer CRISPRi with gene-expression readout. | medium | no | A cCRE effect on regulatory output is predicted, potentially including TOX3, but this test alone does not establish GATA3 mediation. | A cCRE effect on regulatory output is predicted, potentially including TOX3, but this test alone does not establish FOXA1 mediation. | No relevant cCRE-dependent regulatory effect attributable to rs4784227 is expected. | A cCRE effect on regulatory output is predicted if this chain is correct, but the target is not established. | A cCRE effect on regulatory output is predicted if this chain is correct, but the target is not established. |

## Next experiment

Run the matched C-versus-T enhancer reporter in MCF-7 with separate FOXA1 and GATA3 depletion and test which depletion selectively removes the allele-dependent reporter difference. This is the least costly proposed test that directly distinguishes the two leading TF-mediated chains; it would not by itself establish regulation of endogenous TOX3.

## Investigate calls

- literature_search({"query": "rs4784227 functional enhancer allele-specific TOX3 breast cancer"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- qbic_tf_detail({"tf": "GATA3"})

## Flags

- none

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

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20AND%20TOX3%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:26:28+00:00)

> Europe PMC: 77 hits for 'rs4784227 AND TOX3 AND "breast cancer"'; top 8 with PMIDs:
> PMID 41230718 (2026): Cis-regulatory and long noncoding RNA alterations in breast cancer - current insights, biomarker utility, and the critical need for functional validation.
> PMID 40932605 (2025): Molecular signatures of breast cancer in the Iranian population: a review of cell growth and cell cycle regulators.
> PMID 42001218 (2026): Prioritizing context-specific genetic risk mechanisms in 11 solid cancers.
> PMID 36042591 (2022): Association between the rs4784227-CASC16 polymorphism and the risk of breast cancer: A meta-analysis.
> PMID 39777116 (2025): Identification of significant single-nucleotide polymorphisms associated with breast cancer recurrence and metastasis using GWAS.
> PMID 38741014 (2024): Genome-wide association analyses of breast cancer in women of African ancestry identify new susceptibility loci and improve risk prediction.
> PMID 39587695 (2024): The shared genetic landscape of polycystic ovary syndrome and breast cancer: convergence on ER + breast cancer but not ER- breast cancer.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.

<a id="e18a"></a>**E18a** literature_search, Europe PMC abstract, PMID 41230718 (https://europepmc.org/article/MED/41230718; retrieved 2026-10-25T17:26:28+00:00)

> Key examples include promoter mutations [e.g., rs2279744 (Mouse double minute 2 homolog gene; MDM2)], enhancer mutations [e.g., rs4784227 (thymocyte selection-associated high mobility group box family member 3 gene; TOX3)], and lncRNAs [e.g., HOX transcript antisense intergenic RNA (HOTAIR)] linked to progression, metastasis, and poor survival.

<a id="e18b"></a>**E18b** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> ObjectiveAlthough several studies have identified an association between the rs4784227-cancer susceptibility candidate gene 16 (CASC16) polymorphism and breast cancer, the results remain inconclusive.

<a id="e18c"></a>**E18c** literature_search, Europe PMC abstract, PMID 36042591 (https://europepmc.org/article/MED/36042591; retrieved 2026-10-25T17:26:28+00:00)

> Our pooled analysis showed a significant association between the rs4784227- (T) allele and breast cancer susceptibility in Asian and North American populations, and intervention with this mutation might be a new therapeutic strategy for breast cancer.

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

<a id="e35"></a>**E35** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs4784227%20functional%20enhancer%20allele-specific%20TOX3%20breast%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:33:08+00:00)

> Europe PMC: 25 hits for 'rs4784227 functional enhancer allele-specific TOX3 breast cancer'; top 8 with PMIDs:
> PMID 39777116 (2025): Identification of significant single-nucleotide polymorphisms associated with breast cancer recurrence and metastasis using GWAS.
> PMID 38902506 (2024): Hidden secrets of the cancer genome: unlocking the impact of non-coding mutations in gene regulatory elements.
> PMID 31338012 (2019): Association of <i>rs4784227-CASC16 (LOC643714 locus)</i> and <i>rs4782447-ACSF3</i> polymorphisms and their association with breast cancer risk among Iranian population.
> PMID 35011637 (2021): Three-Dimensional Genome Organization in Breast and Gynecological Cancers: How Chromatin Folding Influences Tumorigenic Transcriptional Programs.
> PMID 32765587 (2020): ABC-GWAS: Functional Annotation of Estrogen Receptor-Positive Breast Cancer Genetic Variants.
> PMID 33919522 (2021): Genetic Variants in Transcription Factor Binding Sites in Humans: Triggered by Natural Selection and Triggers of Diseases.
> PMID 27806084 (2016): Genetic and Epigenetic Regulation of TOX3 Expression in Breast Cancer.
> PMID 30323354 (2018): BRCA1/2-negative, high-risk breast cancers (BRCAX) for Asian women: genetic susceptibility loci and their potential impacts.

<a id="e35a"></a>**E35a** literature_search, Europe PMC abstract, PMID 31338012 (https://europepmc.org/article/MED/31338012; retrieved 2026-10-26T13:33:08+00:00)

> rs4784227-CASC16 and rs4782447-ACSF3, as single nucleotide polymorphisms (SNPs), located at the 16q may affect the FOXA1 DNA binding sequence change and therefore may enhance the FOXA1-binding affinity to the promoter of TOX3 gene.

<a id="e35b"></a>**E35b** literature_search, Europe PMC abstract, PMID 31338012 (https://europepmc.org/article/MED/31338012; retrieved 2026-10-26T13:33:08+00:00)

> This is in line with other studies suggesting these SNPs as risk-associated polymorphisms which may lead to a change in the affinity of FOXA1, as a distal enhancer, to TOX3 and thus change in TOX3 expression, which can eventually affect the risk of breast cancer.

<a id="e35c"></a>**E35c** literature_search, Europe PMC abstract, PMID 27806084 (https://europepmc.org/article/MED/27806084; retrieved 2026-10-26T13:33:08+00:00)

> Expression quantitative trait loci (eQTL) analyses revealed significant associations of rs3803662 and rs4784227 genotypes with TOX3 expression in breast tumors.

<a id="e35d"></a>**E35d** literature_search, Europe PMC abstract, PMID 27806084 (https://europepmc.org/article/MED/27806084; retrieved 2026-10-26T13:33:08+00:00)

> These data suggest a complex system of TOX3 regulation in breast tumors, driven by germline variants and somatic epigenetic modifications in a subtype specific manner.

<a id="e36"></a>**E36** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr16_52565276_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:27:51+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr16_52565276_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e37"></a>**E37** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GATA3","symbol":"GATA3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr16:52565276:C>T","gate_p":5.02e-05,"models":[{"model":"GATA3_NA_TGTCGT20NGA_ESAC_yang2017_0_4_7mer","mapping":"own","group":"G010 GATA, 6 models","quality":0.858,"effect":0.783,"z":10.91,"p":1.1e-27,"rank_abs_z":"65/997","passed_gate":true,"site_strength":{"ref_percentile":83.3,"alt_percentile":98.0,"k":7}},{"model":"GATA1_eDBD_TTTAGA40NGGC_KN_yin2017_0_4_7mer","mapping":"CIS-BP (GATA1)","group":"G010 GATA, 6 models","quality":0.626,"effect":1.507,"z":12.45,"p":1.3e-35,"rank_abs_z":"57/997","passed_gate":true,"site_strength":{"ref_percentile":95.2,"alt_percentile":98.2,"k":7}},{"model":"GATA2_eDBD_TATGCA40NGAG_KR_yin2017_1_3_7mer","mapping":"CIS-BP (GATA2)","group":"G010 GATA, 6 models","quality":0.874,"effect":0.283,"z":18.65,"p":1.3e-77,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":92.3,"alt_percentile":98.6,"k":7}},{"model":"GATA4_NA_TAAAAT20NAAA_Y_jolma2013_0_3_7mer","mapping":"CIS-BP (GATA4)","group":"G010 GATA, 6 models","quality":0.789,"effect":0.772,"z":8.04,"p":9.1e-16,"rank_abs_z":"116/997","passed_gate":true,"site_strength":{"ref_percentile":92.0,"alt_percentile":97.4,"k":7}},{"model":"GATA5_NA_TAAATG20NTAA_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (GATA5)","group":"G010 GATA, 6 models","quality":0.882,"effect":0.733,"z":7.92,"p":2.3e-15,"rank_abs_z":"117/997","passed_gate":true,"site_strength":{"ref_percentile":99.5,"alt_percentile":99.4,"k":7}},{"model":"GATA6_eDBD_TCCATC40NTGA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (GATA6)","group":"G010 GATA, 6 models","quality":0.937,"effect":0.764,"z":14.98,"p":1e-50,"rank_abs_z":"40/997","passed_gate":true,"site_strength":{"ref_percentile":97.4,"alt_percentile":98.7,"k":7}}]}
