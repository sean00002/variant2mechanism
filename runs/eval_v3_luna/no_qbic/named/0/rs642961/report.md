# rs642961 and Cleft lip (IRF6)

Configuration `no_qbic`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.01 over 9 model calls; 210 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. H2: TFAP2A binding disruption at the enhancer reduces IRF6 regulation (p = 0.78)

TF TFAP2A (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2863563 (MCS9.7 enhancer-like cCRE); gene IRF6; cell type Epidermal development is implicated in the literature; a specific cleft-relevant developmental cell type is not established by the supplied evidence..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The literature reports that rs642961 abrogates AP2A binding, predicting stronger binding to ref A than alt G; no QBiC-SELEX result is supplied, and ENCODE reports no TFAP2A ChIP peak at the variant. | weak | [E10a](#e10a), [E11](#e11) |
| element | rs642961 lies in the enhancer-like cCRE EH38E2863563, also described in the literature as MCS9.7. | supported | [E03](#e03), [E10a](#e10a) |
| gene | The literature reports that AP2A regulates MCS9.7 enhancer activity and IRF6 protein expression, supporting IRF6 as the proposed target. | weak | [E10b](#e10b) |
| cell_type | The reported TFAP2A–MCS9.7–IRF6 regulatory relationship is in the context of epidermal development, but its operation in a specific cleft-relevant cell type is not shown here. | supported | [E10b](#e10b) |
| phenotype | rs642961 is associated with orofacial clefts, but the supplied evidence does not prove that this TFAP2A–IRF6 mechanism causes the association. | supported | [E06](#e06), [E07](#e07), [E12](#e12) |

Predictions: In a relevant developmental cell model, the G allele should show less TFAP2A occupancy than A and should reduce IRF6 regulation through this element.; Perturbing or editing the element should affect IRF6 more consistently than UTP25 or TRAF3IP3.

Falsified if: A and G show no reproducible difference in TFAP2A binding in an appropriate assay, or editing the variant/element has no effect on IRF6 regulation in a relevant developmental model.

### 2. H1: No TF-mediated effect at rs642961 (p = 0.16)

Null chain: no TF-mediated effect of this variant.

Predictions: There is no reproducible TF-mediated allelic effect of rs642961 in a relevant developmental context; the cleft association could instead reflect linkage or another mechanism.; An allele-specific binding difference in an in vitro assay, if observed, would not by itself establish a regulatory effect in cells.

Falsified if: Editing A to G in a relevant developmental cell model reproducibly reduces TFAP2A occupancy and IRF6 expression, and restoring the binding or enhancer activity rescues the expression effect.

### 3. H3: TFAP2A binding disruption at the enhancer regulates TRAF3IP3 instead (p = 0.03)

TF TFAP2A (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2863563 (MCS9.7 enhancer-like cCRE); gene TRAF3IP3; cell type A cleft-relevant developmental context is proposed but not established; the supplied TRAF3IP3 eQTL evidence is from blood-related tissues..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The literature reports that rs642961 abrogates AP2A binding, predicting stronger binding to ref A than alt G; no QBiC-SELEX result is supplied, and ENCODE reports no TFAP2A ChIP peak at the variant. | weak | [E10a](#e10a), [E11](#e11) |
| element | rs642961 lies in the enhancer-like cCRE EH38E2863563. | supported | [E03](#e03) |
| gene | TRAF3IP3 is a possible locus target based on locus-to-gene scores and blood-related eQTLs, but regulation by this cCRE is not demonstrated. | weak | [E02](#e02), [E07](#e07), [E08](#e08) |
| cell_type | The available TRAF3IP3 eQTL observations are in blood-related contexts and do not establish regulation in cleft-relevant developmental cells. | supported | [E07](#e07), [E08](#e08) |
| phenotype | The variant/locus is associated with orofacial clefts, but no supplied evidence connects a TRAF3IP3 regulatory effect to that phenotype. | supported | [E06](#e06), [E07](#e07) |

Predictions: If this alternative is correct, perturbing the element in a relevant developmental model should affect TRAF3IP3 more than IRF6 or UTP25.; The G allele is predicted to reduce TFAP2A binding, but the blood-related TRAF3IP3 eQTL effect does not establish the direction of a developmental-cell effect.

Falsified if: Element perturbation or variant editing affects IRF6 but not TRAF3IP3 in relevant cells, or there is no relevant-cell TFAP2A binding difference.

### 4. H4: TFAP2A binding disruption at the enhancer regulates UTP25 instead (p = 0.03)

TF TFAP2A (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2863563 (MCS9.7 enhancer-like cCRE); gene UTP25; cell type A cleft-relevant developmental context is proposed but not established by the supplied evidence..

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The literature reports that rs642961 abrogates AP2A binding, predicting stronger binding to ref A than alt G; no QBiC-SELEX result is supplied, and ENCODE reports no TFAP2A ChIP peak at the variant. | weak | [E10a](#e10a), [E11](#e11) |
| element | rs642961 lies in the enhancer-like cCRE EH38E2863563. | supported | [E03](#e03) |
| gene | UTP25 is nearby and has a high best locus-to-gene score, but the supplied evidence does not show that this cCRE regulates UTP25. | weak | [E02](#e02), [E07](#e07) |
| cell_type | The supplied evidence does not identify a cell type in which this element regulates UTP25. | supported | [E03](#e03), [E04](#e04) |
| phenotype | The variant/locus is associated with orofacial clefts, but no supplied evidence connects UTP25 regulation to that phenotype. | supported | [E06](#e06), [E07](#e07) |

Predictions: If this alternative is correct, perturbing the element in a relevant developmental model should affect UTP25 more than IRF6 or TRAF3IP3.; The G allele is predicted to reduce TFAP2A binding, but a UTP25 expression consequence has not been demonstrated.

Falsified if: Element perturbation or variant editing affects IRF6 but not UTP25 in relevant cells, or there is no relevant-cell TFAP2A binding difference.

## Prediction matrix

| Test | Cost | Separates top two | H2 | H1 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TFAP2A EMSA using A and G rs642961 probes, with TFAP2A-specific competition or supershift | low | yes | A should show stronger TFAP2A-specific binding than G. | No reproducible TFAP2A-specific difference between A and G is expected. | A should show stronger TFAP2A-specific binding than G. | A should show stronger TFAP2A-specific binding than G. |
| Allele-specific TFAP2A CUT&RUN or ChIP in a cleft-relevant developmental epithelial model | medium | yes | TFAP2A occupancy should be greater on A than G. | No reproducible allele-specific TFAP2A occupancy is expected. | TFAP2A occupancy should be greater on A than G. | TFAP2A occupancy should be greater on A than G. |
| Isogenic A-to-G editing followed by element perturbation and measurement of IRF6, TRAF3IP3, and UTP25 expression in a relevant developmental model | high | yes | The G edit should reduce IRF6 regulation; IRF6 should respond more clearly than the alternative genes. | No reproducible TF-mediated, allele-dependent target-gene effect is expected. | The G edit or element perturbation should affect TRAF3IP3 more clearly than IRF6 or UTP25. | The G edit or element perturbation should affect UTP25 more clearly than IRF6 or TRAF3IP3. |

## Next experiment

Run the low-cost allele-specific TFAP2A EMSA with A and G rs642961 probes and TFAP2A-specific competition or supershift. The predicted A-greater-than-G binding would support the proposed binding step over the null, but would not by itself establish occupancy or a regulatory effect in developmental cells.

## Investigate calls

- literature_search({"query": "rs642961 allele-specific binding enhancer reporter IRF6 cleft lip"})
- chip_peaks({"tf": "TFAP2A", "biosample": null})
- gene_disease({"gene": "IRF6"})

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

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20AND%20UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:43+00:00)

> Europe PMC: 2 hits for 'rs642961 AND UTP25 AND "cleft lip"'; top 2 with PMIDs:
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-25T17:29:43+00:00)

> Conditional analyses of GWAS data suggest the two functional SNPs near IRF6 account for the majority of risk for CL/P at this locus.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 37161310 (https://europepmc.org/article/MED/37161310; retrieved 2026-10-25T17:29:43+00:00)

> This study revealed that the SNP rs12403599, within the IRF6 promoter, is associated with all phenotypes of NSCL/P, especially nonsyndromic cleft lip (NSCLO) and a subphenotype of it, microform cleft lip (MCL).

<a id="e10"></a>**E10** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20allele-specific%20binding%20enhancer%20reporter%20IRF6%20cleft%20lip&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T13:27:32+00:00)

> Europe PMC: 17 hits for 'rs642961 allele-specific binding enhancer reporter IRF6 cleft lip'; top 8 with PMIDs:
> PMID 42799765 (2026): The orofacial cleft risk gene IRF6 is a target gene of SOX9 in cranial neural crest cells.
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 40918684 (2025): Functional Validation of Noncoding Variants Associated With Nonsyndromic Orofacial Cleft.
> PMID 39500877 (2024): High incidence and geographic distribution of cleft palate in Finland are associated with the IRF6 gene.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.
> PMID 36008388 (2022): Chromatin conformation of human oral epithelium can identify orofacial cleft missing functional variants.
> PMID 35226783 (2022): Revisiting the embryogenesis of lip and palate development.
> PMID 29913133 (2018): IRF6 and AP2A Interaction Regulates Epidermal Development.

<a id="e10a"></a>**E10a** literature_search, Europe PMC abstract, PMID 29913133 (https://europepmc.org/article/MED/29913133; retrieved 2026-10-26T13:27:32+00:00)

> This variant (rs642961) abrogates AP2A protein binding at MCS9.7.

<a id="e10b"></a>**E10b** literature_search, Europe PMC abstract, PMID 29913133 (https://europepmc.org/article/MED/29913133; retrieved 2026-10-26T13:27:32+00:00)

> Here, we found that AP2A protein regulates MCS9.7 enhancer activity in vivo and IRF6 protein expression in epidermal development.

<a id="e11"></a>**E11** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:31:05+00:00)

> No ENCODE TFAP2A ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no TFAP2A experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e12"></a>**E12** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:31:08+00:00)

> Open Targets: IRF6 and cleft lip (EFO_0003959), overall score 0.54; by evidence type: genetic_association 0.72, genetic_literature 0.61, animal_model 0.54, literature 0.35
