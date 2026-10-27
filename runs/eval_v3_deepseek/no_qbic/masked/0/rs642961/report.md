# rs642961 and Cleft lip (IRF6)

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 7 model calls; 581 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. H3: No TF-mediated allelic effect; the association is explained by linkage, pleiotropy or a bystander regulatory variant (p = 0.58)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific ZNF687 occupancy or enhancer activity should be detected at this exact base in the disease-relevant cell type.; The cleft-lip association should be attributable to a linked causal variant, pleiotropy, or nearby regulatory variation rather than this A>G change.; The ZNF687 ChIP peak in GM12878 should not be allele-specific or relevant to craniofacial epithelium.

Falsified if: Allele-specific ZNF687 binding and enhancer activity are demonstrated at this base in craniofacial cells.; The A allele reproducibly alters IRF6 or UTP25 expression in a disease-relevant cell type.; Fine-mapping excludes linked variants and supports this position as the causal regulatory change.

### 2. H1: ZNF687 binding at the IRF6 dELS is a candidate activator of IRF6 in craniofacial epithelium (p = 0.30)

TF ZNF687 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2863563 dELS / IRF6 enhancer; gene IRF6; cell type craniofacial epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF687 is the only ENCODE-bound, expressed TF with a binding model reported at this variant (E04), but its only containing peak is in GM12878, not a craniofacial sample (E05), and no ZNF687 QBiC-SELEX model is supplied. The ref-A > alt-G direction is therefore not directly measured; I set ref more because the IRF6 eQTL shows alt G lowering IRF6 (E08), which is consistent with a ref-bound activator, but this is an assumption. | missing | [E04](#e04), [E05](#e05), [E08](#e08) |
| element | The variant lies in EH38E2863563, a distal enhancer-like cCRE with DNase and H3K27ac signal at the IRF6 locus; the signal values are biosample maxima and not craniofacial-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | IRF6 is 9.7 kb away, although ENSG00000289700 is also listed at 9.7 kb, so IRF6 is not uniquely nearest. E08 reports IRF6 eQTLs in brain cerebellum/hemisphere with alt G NES -0.62 and -0.61, i.e. A is associated with higher IRF6, but not in craniofacial epithelium. | weak | [E02](#e02), [E08](#e08) |
| cell_type | The cleft-lip GWAS and cleft literature point to craniofacial epithelial biology, but no expression context was provided and the E12 lookup for keratinocyte failed, so this cell type is inferred rather than measured. | weak | [E06](#e06), [E09](#e09), [E12](#e12) |
| phenotype | The orofacial cleft GWAS reports an association at this variant with effect allele A (p 2.0e-06); if A increases ZNF687-driven IRF6 expression in craniofacial epithelium, altered IRF6 dosage could contribute, but the mechanism is not demonstrated. | weak | [E06](#e06), [E09](#e09) |

Predictions: ZNF687 should bind the ref A allele more strongly than the alt G allele at this base in an allele-specific binding assay.; EH38E2863563 should show allele-dependent enhancer activity in craniofacial epithelial cells, with the A allele increasing activity if ZNF687 activates IRF6.; The A allele should associate with higher IRF6 expression in a craniofacial-relevant context, matching the direction of the brain IRF6 eQTL.

Falsified if: ZNF687 does not bind this site allele-specifically, or binds the alt G allele more strongly than ref A.; The A allele reduces rather than increases IRF6 enhancer activity or IRF6 expression in craniofacial epithelial cells.; EH38E2863563 does not contact or regulate the IRF6 promoter in craniofacial cells.

### 3. H2: ZNF687 binding at the same dELS regulates UTP25 and contributes to cleft lip (p = 0.12)

TF ZNF687 (QBiC-SELEX coverage own_model), ref allele binds more; element EH38E2863563 dELS near UTP25; gene UTP25; cell type craniofacial epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF687 is the only ENCODE-bound, expressed TF with a binding model at this variant (E04), but its containing peak is only in GM12878 (E05) and no ZNF687 QBiC-SELEX model is supplied. The ref-A > alt-G direction is not measured and is inferred by analogy to H1 rather than from UTP25 allele-specific data. | missing | [E04](#e04), [E05](#e05) |
| element | The variant lies in EH38E2863563, a dELS whose SCREEN nearby genes include UTP25 as well as IRF6; this is proximity-based and does not establish UTP25 as the target. | supported | [E01](#e01), [E03](#e03) |
| gene | UTP25 is 12.0 kb from the variant and has the best L2G score across credible sets (0.75), but the relevant credible-set PIPs are low (0.05-0.10) and the source set for 0.75 is unspecified. Open Targets gives UTP25 a cleft-lip score of 0.35, genetic association 0.57, while E08 contains no UTP25 eQTL. | weak | [E02](#e02), [E07](#e07), [E09](#e09), [E11](#e11) |
| cell_type | UTP25 cleft-lip literature hits and the Open Targets association support a disease link, but they do not establish UTP25 expression or function in craniofacial epithelium; no expression or chromatin-contact data are provided, and the E12 keratinocyte lookup failed. | weak | [E09](#e09), [E11](#e11), [E12](#e12) |
| phenotype | If the A allele increases ZNF687-driven UTP25 expression in craniofacial epithelium, altered UTP25 dosage could contribute to the orofacial cleft association, but UTP25 mediation is not shown and the cleft GWAS signal is modest. | weak | [E06](#e06), [E09](#e09), [E11](#e11) |

Predictions: Chromatin contact or reporter assays should link EH38E2863563 to the UTP25 promoter in craniofacial cells.; The A allele should increase UTP25 expression in a craniofacial-relevant context.; UTP25, rather than IRF6, should show the stronger allele-specific regulatory effect in the disease-relevant cell type.

Falsified if: EH38E2863563 does not contact the UTP25 promoter in craniofacial cells.; The variant has no allele-specific effect on UTP25 expression.; UTP25 is not expressed or required in the relevant craniofacial epithelium.

## Prediction matrix

| Test | Cost | Separates top two | H3 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific ZNF687 binding assay (EMSA with recombinant ZNF687 or ChIP-qPCR in a heterozygous ZNF687-expressing line) at chr1:209815925 ref-A vs alt-G | low | yes | No reproducible allele-specific ZNF687 binding at this base; supports the null. | ZNF687 binds ref A more strongly than alt G; supports the ZNF687-IRF6 chain. | ZNF687 binds ref A more strongly than alt G; supports the shared binding link but does not distinguish H1 from H2. |
| ZNF687 ChIP-qPCR or ChIP-seq in craniofacial epithelial/keratinocyte cells at EH38E2863563 | medium | yes | No ZNF687 occupancy at this element in craniofacial epithelial cells; supports the null. | ZNF687 occupies the element in craniofacial epithelial cells; supports use of this enhancer. | ZNF687 occupies the element in craniofacial epithelial cells; supports the shared element but not UTP25 targeting. |
| Allele-specific reporter assay for EH38E2863563 in craniofacial epithelial cells, with IRF6 and UTP25 expression readouts | medium | yes | No allele-specific enhancer activity and no allele-specific IRF6 or UTP25 expression. | The A allele increases enhancer activity and IRF6 expression; G is lower. | The A allele increases UTP25 expression, with little or no IRF6 effect. |
| Capture Hi-C, ABC, or CRISPRi linking EH38E2863563 to the IRF6 versus UTP25 promoter in craniofacial cells | high | yes | No specific contact to either promoter, or contact is not allele-dependent. | The element contacts the IRF6 promoter. | The element contacts the UTP25 promoter. |

## Next experiment

Run the cheapest discriminating assay: allele-specific ZNF687 binding at chr1:209815925 (EMSA with recombinant ZNF687, or ChIP-qPCR in a heterozygous ZNF687-expressing line) comparing ref-A and alt-G oligos. Ref-A binding more strongly supports H1; no reproducible allele-specific binding supports H3.

## Investigate calls

- chip_peaks({"tf": "TFAP2A", "biosample": null})
- gene_disease({"gene": "UTP25"})
- tf_expression({"tf": "TFAP2A", "context": "keratinocyte"})

## Flags

- quote_rejected: PMID 42873673: not an exact substring of the abstract
- tool_failed: E12 tf_expression: local DepMap/GTEx lookup failed: Unknown expression context 'keratinocyte'. Use DepMap:<ModelID>, DepMap:subtype=<Oncotree subtype>, GTEx:<tissue> or none.

Citation support: 0.80 of links cite only evidence that passed every check.

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

<a id="e10"></a>**E10** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:31:05+00:00)

> No ENCODE TFAP2A ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no TFAP2A experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e11"></a>**E11** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T20:22:47+00:00)

> Open Targets: UTP25 and cleft lip (EFO_0003959), overall score 0.35; by evidence type: genetic_association 0.57, literature 0.04

<a id="e12"></a>**E12** tf_expression (failed), local DepMap/GTEx (; retrieved local)

> local DepMap/GTEx lookup failed: Unknown expression context 'keratinocyte'. Use DepMap:<ModelID>, DepMap:subtype=<Oncotree subtype>, GTEx:<tissue> or none.
