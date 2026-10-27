# rs642961 and Cleft lip (IRF6)

Configuration `no_qbic`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 7 model calls; 177 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of this variant (p = 0.90)

Null chain: no TF-mediated effect of this variant.

Predictions: There is no reproducible, disease-relevant allele-specific TF-mediated effect at this base; the cleft association may reflect linkage or another explanation.; The variant may overlap an active element in some biosamples without that element mediating a cleft-relevant effect.

Falsified if: In a relevant craniofacial cell model, the alleles show reproducible differential TF binding and editing this base causes a corresponding, TF-dependent regulatory effect on a target gene.

### 2. H3: Candidate ZNF687 enhancer model for UTP25: G binds more and raises UTP25 (p = 0.04)

TF ZNF687 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps the distal enhancer-like cCRE EH38E2863563; activity in a cleft-relevant cell is unestablished.; gene UTP25; cell type NHEK-like craniofacial epithelial cells are a candidate context, not established for this variant..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF687 is a tentative candidate because it is the only reported TF with a binding model and a peak overlapping the variant, but that peak is from GM12878; no matching NHEK peak is reported. No allelic binding result is supplied. This chain hypothesizes greater binding to G, rather than treating that direction as evidence-based. | missing | [E04](#e04), [E05](#e05), [E10](#e10) |
| element | The variant overlaps a dELS cCRE with enhancer-like chromatin signals among ENCODE biosamples, but the reported maxima do not establish activity in NHEK or craniofacial cells. | supported | [E01](#e01), [E03](#e03) |
| gene | UTP25 is a candidate target based on proximity, a high best L2G score, and a modest gene-level cleft-lip score; none demonstrates regulation by this cCRE. This model predicts that greater G binding raises UTP25 expression, an unverified activating-effect assumption. | weak | [E02](#e02), [E07](#e07), [E11](#e11), [E12](#e12) |
| cell_type | NHEK-active enhancers and FOX-family recruitment are described for a set of variants, but this does not establish activity of this cCRE or ZNF687 action at this variant in NHEK cells. | weak | [E09a](#e09a), [E10](#e10) |
| phenotype | A is reported as the risk allele for orofacial clefts; this model predicts that its lower UTP25 expression contributes to risk, but neither the association nor the gene-level score establishes this mechanism or a cleft-lip-specific causal effect. | weak | [E06](#e06), [E07](#e07), [E12](#e12) |

Predictions: In a relevant cell model, G should bind ZNF687 more strongly than A and should increase UTP25 expression relative to A.; Editing the variant or perturbing the element should affect UTP25 more than IRF6 or TRAF3IP3; the predicted UTP25 effect should depend on ZNF687.

Falsified if: A relevant-cell assay finds no ZNF687 occupancy or finds stronger binding to A.; Editing or perturbing the element has no effect on UTP25, or IRF6 responds reproducibly while UTP25 does not.; Greater G binding fails to increase UTP25 expression in the proposed context.

### 3. H1: Candidate ZNF687 enhancer model for IRF6: G binds more and raises IRF6 (p = 0.04)

TF ZNF687 (QBiC-SELEX coverage own_model), alt allele binds more; element The variant overlaps the distal enhancer-like cCRE EH38E2863563; activity in a cleft-relevant cell is unestablished.; gene IRF6; cell type NHEK-like craniofacial epithelial cells are a candidate context, not established for this variant..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF687 is a tentative candidate because it is the only reported TF with a binding model and a peak overlapping the variant, but that peak is from GM12878; no matching NHEK peak is reported. No allelic binding result is supplied. This chain hypothesizes greater binding to G, rather than treating that direction as evidence-based. | missing | [E04](#e04), [E05](#e05), [E10](#e10) |
| element | The variant overlaps a dELS cCRE with enhancer-like chromatin signals among ENCODE biosamples, but the reported maxima do not establish activity in NHEK or craniofacial cells. | supported | [E01](#e01), [E03](#e03) |
| gene | IRF6 is a candidate target based on proximity, cleft credible-set prioritization, and a brain-tissue eQTL; none demonstrates regulation by this cCRE. The model specifically predicts that greater G binding raises IRF6 expression, an unverified activating-effect assumption. | weak | [E02](#e02), [E07](#e07), [E08](#e08), [E11](#e11) |
| cell_type | NHEK-active enhancers and FOX-family recruitment are described for a set of variants, but this does not establish activity of this cCRE or ZNF687 action at this variant in NHEK cells. | weak | [E09a](#e09a), [E10](#e10) |
| phenotype | A is reported as the risk allele for orofacial clefts; this model predicts that its lower IRF6 expression contributes to risk, but the association does not establish this mechanism or a cleft-lip-specific causal effect. | weak | [E06](#e06), [E07](#e07) |

Predictions: In a relevant cell model, G should bind ZNF687 more strongly than A and should increase IRF6 expression relative to A.; Editing the variant or perturbing the element should affect IRF6 more than UTP25 or TRAF3IP3; the predicted IRF6 effect should depend on ZNF687.

Falsified if: A relevant-cell assay finds no ZNF687 occupancy or finds stronger binding to A.; Editing or perturbing the element has no effect on IRF6, or a different target responds reproducibly while IRF6 does not.; Greater G binding fails to increase IRF6 expression in the proposed context.

### 4. H2: Candidate ZNF687 enhancer model for IRF6: A binds more and represses IRF6 (p = 0.03)

TF ZNF687 (QBiC-SELEX coverage own_model), ref allele binds more; element The variant overlaps the distal enhancer-like cCRE EH38E2863563; activity in a cleft-relevant cell is unestablished.; gene IRF6; cell type NHEK-like craniofacial epithelial cells are a candidate context, not established for this variant..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF687 is a tentative candidate because it is the only reported TF with a binding model and a peak overlapping the variant, but that peak is from GM12878; no matching NHEK peak is reported. No allelic binding result is supplied. This chain hypothesizes greater binding to A, rather than treating that direction as evidence-based. | missing | [E04](#e04), [E05](#e05), [E10](#e10) |
| element | The variant overlaps a dELS cCRE with enhancer-like chromatin signals among ENCODE biosamples, but the reported maxima do not establish activity in NHEK or craniofacial cells. | supported | [E01](#e01), [E03](#e03) |
| gene | IRF6 is a candidate target based on proximity, cleft credible-set prioritization, and a brain-tissue eQTL; none demonstrates regulation by this cCRE. The model specifically predicts that greater A binding represses IRF6 expression, an unverified repressive-effect assumption. | weak | [E02](#e02), [E07](#e07), [E08](#e08), [E11](#e11) |
| cell_type | NHEK-active enhancers and FOX-family recruitment are described for a set of variants, but this does not establish activity of this cCRE or ZNF687 action at this variant in NHEK cells. | weak | [E09a](#e09a), [E10](#e10) |
| phenotype | A is reported as the risk allele for orofacial clefts; this model predicts that its lower IRF6 expression contributes to risk, but the association does not establish this mechanism or a cleft-lip-specific causal effect. | weak | [E06](#e06), [E07](#e07) |

Predictions: In a relevant cell model, A should bind ZNF687 more strongly than G and should reduce IRF6 expression relative to G.; Editing the variant or perturbing the element should affect IRF6 more than UTP25 or TRAF3IP3; the predicted IRF6 effect should depend on ZNF687.

Falsified if: A relevant-cell assay finds no ZNF687 occupancy or finds stronger binding to G.; Editing or perturbing the element has no effect on IRF6, or a different target responds reproducibly while IRF6 does not.; Greater A binding fails to reduce IRF6 expression in the proposed context.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H3 | H1 | H2 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific EMSA with ZNF687 and A- versus G-containing oligonucleotides | low | yes | No reproducible allele-specific ZNF687 binding is predicted. | G shows stronger ZNF687 binding than A. | G shows stronger ZNF687 binding than A. | A shows stronger ZNF687 binding than G. |
| Measure ZNF687 occupancy at the variant in an NHEK-like craniofacial epithelial model, with allele-specific analysis if heterozygous | medium | yes | No relevant-cell occupancy supporting an allele-specific ZNF687 mechanism. | ZNF687 occupies the site; allele-specific signal favors G. | ZNF687 occupies the site; allele-specific signal favors G. | ZNF687 occupies the site; allele-specific signal favors A. |
| Edit A to G and G to A in a relevant epithelial model, then measure IRF6 and UTP25 expression with and without ZNF687 perturbation | high | yes | No reproducible allele-dependent, ZNF687-dependent change in IRF6 or UTP25. | G raises UTP25 relative to A, and this difference is reduced by ZNF687 perturbation. | G raises IRF6 relative to A, and this difference is reduced by ZNF687 perturbation. | A lowers IRF6 relative to G, and this difference is reduced by ZNF687 perturbation. |

## Next experiment

Run the low-cost allele-specific ZNF687 EMSA with A- and G-containing oligonucleotides. H0 predicts no reproducible differential binding, whereas the second-ranked chain, H3, predicts stronger binding to G. A differential result would test only the binding step, not establish enhancer activity, target-gene regulation, or disease causality.

## Investigate calls

- chip_peaks({"tf": "ZNF687", "biosample": "NHEK"})
- literature_search({"query": "chr1:209815925 IRF6 UTP25 orofacial cleft variant enhancer"})
- gene_disease({"gene": "UTP25"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/1:209815925-209815925:1/G?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:29:41+00:00)

> Variant chr1:209815925:A>G (GRCh38), allele string A/G
> Known IDs: rs642961
> Most severe consequence: regulatory_region_variant
> Regulatory features: ENSR1_B3JM9C enhancer
> GERP conservation score at the site: 0.516
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/1:208815925-210815925?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:29:25+00:00)

> 13 protein-coding genes within 1000 kb of chr1:209815925:A>G, by distance to TSS:
> IRF6: 9.7 kb from TSS (upstream, strand -1)
> ENSG00000289700: 9.7 kb from TSS (upstream, strand -1)
> UTP25: 12.0 kb from TSS (upstream, strand +1)
> C1orf74: 31.3 kb from TSS (upstream, strand -1)
> TRAF3IP3: 60.4 kb from TSS (downstream, strand +1)
> SYT14: 85.0 kb from TSS (upstream, strand +1)
> HSD11B1: 129.8 kb from TSS (downstream, strand +1)
> G0S2: 140.5 kb from TSS (downstream, strand +1)
> LAMB3: 162.8 kb from TSS (upstream, strand -1)
> CAMK1G: 232.2 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:29:16+00:00)

> The variant lies in cCRE EH38E2863563 (dELS: distal enhancer-like), chr1:209815915-209816264.
> SCREEN: 2 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2863563 dELS (contains the variant): DNase z 5.3, H3K27ac z 5.0, H3K4me3 z 2.4, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> EH38E2863562 dELS: DNase z 3.2, H3K27ac z 4.9, H3K4me3 z 1.9, CTCF z 1.5; nearby genes IRF6, UTP25, C1orf74
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr1:209815925:A>G: 15 peaks contain the variant, from 6 factors in 6 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): DPF2, MYC, POLR2A, POLR2AphosphoS5, STAT3. Bound, expressed TFs with a binding model: 1; listed one per row: ZNF687. Assayed with no peak here: 0 TFs in the matching biosample, 572 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR859FDL). expression not filtered (no expression data for this context).

<a id="e06"></a>**E06** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs642961&size=100; retrieved 2026-10-25T17:29:42+00:00)

> 8 GWAS Catalog associations for rs642961, strongest first:
> Systolic blood pressure: p 6.0e-12, effect allele G, risk-allele frequency NR, PMID 38689001
> Hypertension: p 2.0e-08, effect allele A, risk-allele frequency 0.1951, PMID 33230300
> Pulse pressure: p 1.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Diastolic blood pressure: p 3.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Orofacial clefts: p 2.0e-06, effect allele A, risk-allele frequency NR, PMID 19270707

<a id="e07"></a>**E07** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:41+00:00)

> 18 credible sets contain 1_209815925_A_G: 14 GWAS, 4 molecular QTL.
> GWAS Systolic blood pressure: PIP 0.10; L2G TRAF3IP3 0.11, IRF6 0.11, UTP25 0.10
> GWAS Systolic blood pressure: PIP 0.09; L2G IRF6 0.67, UTP25 0.14, TRAF3IP3 0.08
> GWAS Systolic blood pressure, combined automated + manual reading: PIP 0.05; L2G IRF6 0.13, UTP25 0.10, C1orf74 0.10
> GWAS Orofacial clefts: PIP 0.05; L2G IRF6 0.16, TRAF3IP3 0.12, C1orf74 0.10
> GWAS Systolic blood pressure: PIP 0.05; L2G IRF6 0.13, C1orf74 0.09, UTP25 0.08
> GWAS Systolic blood pressure (MTAG): PIP 0.05; L2G IRF6 0.17, C1orf74 0.09, UTP25 0.08
> eqtl for TRAF3IP3 (blueprint_tx_monocyte_enst00000460314): PIP 0.04
> eqtl for TRAF3IP3 (twinsuk_tx_blood_enst00000367023): PIP 0.02
> eqtl for TRAF3IP3 (twinsuk_exon_blood_ensg00000009790_15_1_209782056_): PIP 0.02
> eqtl for TRAF3IP3 (schmiedel_2018_exon_treg_naive_ensg00000009790_15_): PIP 0.02
> Best L2G gene scores across these sets: UTP25 0.75, IRF6 0.67, TRAF3IP3 0.53, C1orf74 0.10

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr1_209815925_A_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T22:31:38+00:00)

> 15 significant GTEx v8 single-tissue eQTLs for chr1_209815925_A_G_b38. NES is the effect of the alt allele (G) relative to ref (A).
> SYT14 in Nerve_Tibial: NES -0.50, p 6.7e-20
> DIEXF in Cells_Cultured_fibroblasts: NES -0.23, p 1.9e-14
> DIEXF in Artery_Tibial: NES -0.23, p 1.2e-10
> TRAF3IP3 in Whole_Blood: NES +0.24, p 5.9e-10
> IRF6 in Brain_Cerebellum: NES -0.62, p 2.2e-07
> DIEXF in Whole_Blood: NES -0.15, p 2.9e-07
> SYT14 in Brain_Hippocampus: NES +0.53, p 3.3e-07
> DIEXF in Adipose_Subcutaneous: NES -0.20, p 7.5e-07
> SYT14 in Brain_Spinal_cord_cervical_c-1: NES +0.72, p 2.7e-06
> DIEXF in Lung: NES -0.11, p 3.2e-06
> IRF6 in Brain_Cerebellar_Hemisphere: NES -0.61, p 3.3e-06
> DIEXF in Brain_Frontal_Cortex_BA9: NES +0.35, p 4.6e-06
> DIEXF in Brain_Cortex: NES +0.33, p 7.0e-06
> DIEXF in Adipose_Visceral_Omentum: NES -0.16, p 2.5e-05
> C1orf74 in Whole_Blood: NES +0.15, p 8.6e-05

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:21:47+00:00)

> Europe PMC: 7 hits for 'UTP25 AND "cleft lip"'; top 6 with PMIDs:
> PMID 42873673 (2026): Genetic Heterogeneity in Cleft Lip and/or Palate With Alveolar Cleft: A Targeted Analysis of NHEK-Active Enhancer Variants.
> PMID 41075272 (2025): Genetic heterogeneity and homogeneity among orofacial cleft subtypes: genome-wide association studies in the cleft collective.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 33987535 (2021): Wavelet Screening identifies regions highly enriched for differentially methylated loci for orofacial clefts.
> PMID 30760477 (2019): Wnt signaling in orofacial clefts: crosstalk, pathogenesis and models.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 42873673 (https://europepmc.org/article/MED/42873673; retrieved 2026-10-26T20:21:47+00:00)

> All three variants overlap NHEK-active enhancers and regulate craniofacial development genes (IRF6, UTP25, TRAF3IP3, BNIP3, JAKMIP3, PPP2R2D) through chromatin looping, pluripotency factor binding, and FOX family transcription factor recruitment.

<a id="e10"></a>**E10** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:17:42+00:00)

> No ENCODE ZNF687 ChIP-seq peak contains chr1:209815925:A>G in biosamples matching 'NHEK'. Absence can also mean no ZNF687 experiment in that biosample. In other biosamples, 1 ZNF687 peaks do contain the variant: GM12878 (experiments ENCSR859FDL).

<a id="e11"></a>**E11** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=chr1%3A209815925%20IRF6%20UTP25%20orofacial%20cleft%20variant%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:22:47+00:00)

> Europe PMC: 0 hits for 'chr1:209815925 IRF6 UTP25 orofacial cleft variant enhancer'; top 0 with PMIDs:

<a id="e12"></a>**E12** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T20:22:47+00:00)

> Open Targets: UTP25 and cleft lip (EFO_0003959), overall score 0.35; by evidence type: genetic_association 0.57, literature 0.04
