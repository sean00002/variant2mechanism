# rs642961 and Cleft lip (IRF6)

Configuration `full`, masked mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.02 over 12 model calls; 272 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: ZNF687 (bound elsewhere, z -0.21, no clear allelic change, weak site). Occupancy unknown: ETV2 (z 77.65); ETV3 (z 77.65); ETV3L (z 77.65); FEV (z 77.65); FLI1 (z 77.65). Diagnostic, not shown to the model: 222 of 997 models pass Bonferroni.

## Ranked chains

### 1. H1: Null: no TF-mediated effect of this variant (p = 0.94)

Null chain: no TF-mediated effect of this variant.

Predictions: Precise A/G comparisons in relevant craniofacial cells will not show a reproducible variant-dependent TF effect that changes a downstream gene; the association could reflect linkage or another mechanism.

Falsified if: Precise allele editing in relevant cells demonstrates a reproducible variant-dependent TF effect at this element and a downstream molecular change.

### 2. H2: Exploratory ETV3-dependent enhancer effect on IRF6 (p = 0.04)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2863563; gene IRF6; cell type Craniofacial developmental cells; not established by the supplied evidence.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3 is an exploratory ETS-factor candidate, not specifically supported over other ETS factors: the shared ETV5-mapped QBiC-SELEX model predicts stronger in-vitro binding to G, but does not establish ETV3-specific binding or occupancy. No ETV3 peak was reported in cranial neural crest cells; assay availability is unclear. | weak | [E10](#e10), [E13](#e13), [E17](#e17) |
| element | The variant lies in enhancer-like cCRE EH38E2863563, but the activity maxima reported across biosamples do not establish activity in craniofacial cells. | supported | [E01](#e01), [E03](#e03) |
| gene | IRF6 is a candidate target because it is nearby and has stronger cleft-lip gene-disease support than TRAF3IP3, but the evidence does not show that this cCRE regulates IRF6. | weak | [E02](#e02), [E07](#e07), [E23](#e23) |
| cell_type | Craniofacial developmental cells are a plausible context from the general enhancer literature, but element activity and ETV3 occupancy in those cells are not established. | weak | [E03](#e03), [E09a](#e09a), [E17](#e17) |
| phenotype | The variant is associated with orofacial clefts broadly; the evidence does not establish a cleft-lip-specific causal effect or an ETV3–IRF6 mechanism. | supported | [E06](#e06), [E07](#e07), [E23](#e23) |

Predictions: If this chain is correct, relevant-cell assays should detect ETV3 at the element, greater binding to G, and an allele-dependent change in IRF6 regulation. The direction of the IRF6 expression change and its effect on cleft risk are not established.

Falsified if: ETV3 is absent from or does not occupy the element in relevant cells, or allele editing with ETV3 perturbation shows no reproducible allele-dependent IRF6 effect.

### 3. H5: Exploratory ZNF687-dependent enhancer effect on IRF6 (p = 0.02)

TF ZNF687 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2863563; gene IRF6; cell type Craniofacial developmental cells; not established by the supplied evidence.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF687 is the only reported bound TF with a binding model, but its variant-overlapping peak is from GM12878 rather than a matching craniofacial context. Its own QBiC-SELEX model shows only a small, non-significant preference for A at a weak site, arguing against a clear allelic binding effect through this base. | weak | [E04](#e04), [E05](#e05), [E11](#e11) |
| element | The variant lies in enhancer-like cCRE EH38E2863563, although the reported activity maxima are not specific to craniofacial cells. | supported | [E01](#e01), [E03](#e03) |
| gene | IRF6 is a candidate target based on proximity and gene-disease evidence; no supplied evidence connects this cCRE to IRF6. | weak | [E02](#e02), [E07](#e07), [E23](#e23) |
| cell_type | Craniofacial developmental cells are a plausible context, but neither ZNF687 occupancy nor activity of this cCRE in those cells is established. | weak | [E03](#e03), [E05](#e05), [E09a](#e09a) |
| phenotype | The variant has association evidence for orofacial clefts broadly, but the evidence does not show that a ZNF687–IRF6 effect mediates cleft risk. | supported | [E06](#e06), [E07](#e07), [E23](#e23) |

Predictions: If this chain is correct, relevant-cell assays should detect ZNF687 occupancy and a reproducible A-versus-G difference in ZNF687-dependent IRF6 regulation, despite the small effect predicted by its current QBiC-SELEX model.

Falsified if: ZNF687 does not occupy the element in relevant cells, or allele editing with ZNF687 perturbation shows no reproducible allele-dependent IRF6 effect.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H5 |
| --- | --- | --- | --- | --- | --- |
| Compare ref and alt oligonucleotide binding by ETV3 in vitro, with an ETV3-specific assay | low | yes | No reproducible ETV3-specific binding difference. | Greater ETV3 binding to the alt G oligonucleotide. | No ETV3-specific difference predicted; this chain instead requires ZNF687-dependent activity. |
| In relevant craniofacial cells, edit A to G and test factor occupancy and IRF6 expression, with separate ETV3 and ZNF687 perturbations | high | yes | No reproducible allele-dependent TF occupancy and IRF6 change. | ETV3 occupancy and an allele-dependent IRF6 change, stronger with G. | ZNF687 occupancy and an allele-dependent IRF6 change dependent on ZNF687. |
| Test chromatin contact from EH38E2863563 to IRF6 in relevant craniofacial cells | medium | yes | No specific contact supporting this proposed enhancer-to-IRF6 link. | A contact consistent with EH38E2863563 regulating IRF6. | A contact consistent with EH38E2863563 regulating IRF6. |

## Next experiment

The cheapest direct discriminator for the top two hypotheses is an ETV3-specific ref-versus-alt oligonucleotide-binding assay. Greater binding to G would support the binding prediction in H2 over H1, though it would not establish occupancy or regulation in craniofacial cells.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- chip_peaks({"tf": "ETV3", "biosample": "cranial neural crest cells"}) for H2.binding, ran as [E17](#e17). Expected: If a variant-overlapping ETV3 peak is found in cranial neural crest cells, H2.binding gains relevant-cell occupancy support alongside the G-favored prediction, and H2 rises relative to the other ETS-factor chains. If no such peak is found, H2 remains weak; absence of a peak would be informative only if this biosample was assayed.
- literature_search({"query": "\"chr1:209815925\" OR \"209815925\" IRF6 UTP25 TRAF3IP3 orofacial cleft PMID 42873673"}) for H2.gene, ran as [E18](#e18). Expected: If the search finds variant-specific enhancer perturbation or contact evidence linking this element to IRF6, H2.gene gains direct support and H2 rises relative to chains proposing UTP25 or TRAF3IP3. If it finds only general enhancer or gene-association claims, the gene link remains weak.
- gene_disease({"gene": "UTP25"}) for H3.gene, ran as [E19](#e19). Expected: If independent disease-association evidence links UTP25 to orofacial clefts, H3.gene gains support for UTP25 as a disease-relevant candidate, though the variant-to-gene link remains unproven. If such evidence is absent or weak, H3.gene remains weak and H3 does not gain ground over the competing target-gene chains.

- Result of chip_peaks({"tf":"ETV3","biosample":"cranial neural crest cells"}): E17 reports no variant-overlapping ETV3 peak in cranial neural crest cells, but notes that the absence may reflect no experiment in that biosample. (as expected: unclear)
- Result of literature_search({"query":"\"chr1:209815925\" OR \"209815925\" IRF6 UTP25 TRAF3IP3 orofacial cleft PMID 42873673"}): E18 found no hits linking the exact variant or position to IRF6, UTP25, or TRAF3IP3 and orofacial cleft. (as expected: yes)
- Result of gene_disease({"gene":"UTP25"}): E19 reports an overall UTP25–cleft-lip score of 0.35, with genetic-association evidence 0.57 and literature evidence 0.04; this is modest gene-disease support, not evidence that this variant regulates UTP25. (as expected: unclear)

Chains after revision: null 0.82; ETV3 0.06; FLI1 0.06; ETV2 0.06. Link grades changed: H2.cell_type: weak → missing, H5.binding: missing → absent, H5.cell_type: weak → absent, H5.element: supported → absent, H5.gene: weak → absent, H5.phenotype: supported → absent.

### Round 2

- chip_peaks({"tf": "FLI1", "biosample": "cranial neural crest cells"}) for H3.binding, ran as [E20](#e20). Expected: If FLI1 has a peak containing the variant in cranial neural crest cells, H3.binding gains relevant-cell occupancy support and H3 rises relative to candidates without such support; if no peak is found, H3 remains weak or falls, noting that absence may reflect no experiment.
- chip_peaks({"tf": "ETV2", "biosample": "cranial neural crest cells"}) for H4.binding, ran as [E21](#e21). Expected: If ETV2 has a peak containing the variant in cranial neural crest cells, H4.binding gains relevant-cell occupancy support and H4 rises relative to candidates without such support; if no peak is found, H4 remains weak or falls, noting that absence may reflect no experiment.

- Result of chip_peaks({"tf":"FLI1","biosample":"cranial neural crest cells"}): E20 reports no FLI1 ChIP-seq peak containing the variant, and none within 100 bp, in matching cranial neural crest cells; the absence may reflect no experiment in that biosample. (as expected: yes)
- Result of chip_peaks({"tf":"ETV2","biosample":"cranial neural crest cells"}): E21 reports no ETV2 ChIP-seq peak containing the variant, and none within 100 bp, in matching cranial neural crest cells; the absence may reflect no experiment in that biosample. (as expected: yes)

Chains after revision: null 0.94; ETV3 0.02; FLI1 0.02; ETV2 0.02. Link grades changed: H2.cell_type: missing → weak.

### Round 3

- literature_search({"query": "42873673 EH38E2863563 chr1:209815925 IRF6 UTP25 TRAF3IP3 functional enhancer"}) for H2.gene; H3.gene; H4.gene, ran as [E22](#e22). Expected: If the abstract reports evidence specifically connecting this variant or cCRE to a target gene, that gene link gains support and target prioritization may change; if it gives only general enhancer context, the links remain weak.
- gene_disease({"gene": "IRF6"}) for H2.gene, ran as [E23](#e23). Expected: A strong cleft-lip disease association would increase IRF6's plausibility relative to the other candidate targets, but would not by itself establish that this cCRE regulates IRF6.
- gene_disease({"gene": "TRAF3IP3"}) for H4.gene, ran as [E24](#e24). Expected: A strong cleft-lip disease association would increase TRAF3IP3's plausibility relative to IRF6 and UTP25, but would not by itself establish regulation by this variant or cCRE.

- Result of literature_search({"query": "42873673 EH38E2863563 chr1:209815925 IRF6 UTP25 TRAF3IP3 functional enhancer"}): E22 returned zero literature hits for the variant/cCRE and candidate-gene search; it provides no variant- or cCRE-specific target-gene evidence. (as expected: unclear)
- Result of gene_disease({"gene": "IRF6"}): E23 reports an overall IRF6–cleft-lip score of 0.54, including genetic association, genetic literature, and animal-model evidence. This strengthens IRF6 as a disease-relevant candidate but does not link this cCRE to IRF6. (as expected: yes)
- Result of gene_disease({"gene": "TRAF3IP3"}): E24 reports a low overall TRAF3IP3–cleft-lip score of 0.04, providing little support for TRAF3IP3 relative to IRF6; it does not establish regulation by this variant or cCRE. (as expected: yes)

Chains after revision: null 0.94; ETV3 0.04; ZNF687 0.02. Link grades changed: H3.binding: weak → absent, H3.cell_type: weak → absent, H3.element: supported → absent, H3.gene: weak → absent, H3.phenotype: supported → absent, H4.binding: weak → absent, H4.cell_type: weak → absent, H4.element: supported → absent, H4.gene: weak → absent, H4.phenotype: supported → absent, H5.binding: absent → weak, H5.cell_type: absent → weak, H5.element: absent → supported, H5.gene: absent → weak, H5.phenotype: absent → supported.

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

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr1:209815925:A>G, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (none: expression filter skipped), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 1 of 1 occupied (0 with a strong site), 5 of 249 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 572 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element. No occupied TF has a strong site at the variant.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF687 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF687_FL_TA40NGTTAGC_YWL_jolma2025_0_3_7mer (its own model), z -0.21, effect -0.013: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). expression not filtered. Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR859FDL. Best model's site strength: ref 92.7th, alt 88.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV2 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3L (Ets, 18 models; QBiC-SELEX coverage: mapped models only): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FEV (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FLI1 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 77.65, effect 1.32: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). expression not filtered. Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 65.0th, alt 99.2th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:36:37+00:00)

> No ENCODE ETV3 ChIP-seq peak contains chr1:209815925:A>G in biosamples matching 'cranial neural crest cells'. Absence can also mean no ETV3 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22chr1%3A209815925%22%20OR%20%22209815925%22%20IRF6%20UTP25%20TRAF3IP3%20orofacial%20cleft%20PMID%2042873673&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T20:31:22+00:00)

> Europe PMC: 0 hits for '"chr1:209815925" OR "209815925" IRF6 UTP25 TRAF3IP3 orofacial cleft PMID 42873673'; top 0 with PMIDs:

<a id="e19"></a>**E19** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T20:22:47+00:00)

> Open Targets: UTP25 and cleft lip (EFO_0003959), overall score 0.35; by evidence type: genetic_association 0.57, literature 0.04

<a id="e20"></a>**E20** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T20:42:12+00:00)

> No ENCODE FLI1 ChIP-seq peak contains chr1:209815925:A>G in biosamples matching 'cranial neural crest cells'. Absence can also mean no FLI1 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e21"></a>**E21** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:36:37+00:00)

> No ENCODE ETV2 ChIP-seq peak contains chr1:209815925:A>G in biosamples matching 'cranial neural crest cells'. Absence can also mean no ETV2 experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e22"></a>**E22** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=42873673%20EH38E2863563%20chr1%3A209815925%20IRF6%20UTP25%20TRAF3IP3%20functional%20enhancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:15:40+00:00)

> Europe PMC: 0 hits for '42873673 EH38E2863563 chr1:209815925 IRF6 UTP25 TRAF3IP3 functional enhancer'; top 0 with PMIDs:

<a id="e23"></a>**E23** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:31:08+00:00)

> Open Targets: IRF6 and cleft lip (EFO_0003959), overall score 0.54; by evidence type: genetic_association 0.72, genetic_literature 0.61, animal_model 0.54, literature 0.35

<a id="e24"></a>**E24** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T22:15:40+00:00)

> Open Targets: TRAF3IP3 and cleft lip (EFO_0003959), overall score 0.04; by evidence type: genetic_association 0.07, literature 0.01
