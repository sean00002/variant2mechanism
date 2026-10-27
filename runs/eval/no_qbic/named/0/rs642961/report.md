# rs642961 and Cleft lip (IRF6)

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.58 over 8 model calls; 179 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. H1: Risk allele A disrupts an AP-2alpha (TFAP2A) site in the IRF6 upstream enhancer (MCS9.7-type), lowering IRF6 expression in oral periderm (p = 0.44)

TF TFAP2A (stated coverage not_checked; registry own_model), alt allele binds more; element Distal enhancer EH38E2863563 / ENSR1_B3JM9C, ~10 kb upstream of IRF6 (MCS9.7-type element); gene IRF6; cell type Oral/embryonic periderm and surface ectoderm of the fusing lip and palate.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Biochemical work cited in the literature states that rs642961 abrogates one of four AP-2alpha binding sites, i.e. one allele loses AP-2 binding; since the A allele is the cleft risk allele, the alt allele G is the stronger binder. Within the AP-2 specificity group (TFAP2A/B/C share a near-identical motif) TFAP2A is named because it is the paralog explicitly named in that biochemical report; no QBiC-SELEX row or tf lookup was supplied, so coverage is not_checked. Counter-evidence: no ENCODE TFAP2A ChIP-seq peak contains the variant, though this may reflect absence of the relevant biosample. | supported | [E09a](#e09a), [E09b](#e09b), [E07](#e07), [E04](#e04) |
| element | The variant lies in an active distal enhancer-like cCRE (DNase z 5.3, H3K27ac z 5.0; Ensembl regulatory enhancer), so an allelic change in TF occupancy could change enhancer output; these are maxima over biosamples, not craniofacial-specific. | supported | [E01](#e01), [E03](#e03) |
| gene | The enhancer is nearest IRF6 (TSS 9.7 kb) and IRF6 is the top L2G gene in the orofacial-cleft credible set (0.16) and reaches 0.67 in another set; however UTP25/DIEXF has the highest best L2G (0.75) and is the gene with the most GTEx eQTLs here, so the assignment is not settled by these data. | weak | [E02](#e02), [E03](#e03), [E05](#e05), [E08](#e08) |
| cell_type | The relevant tissue is embryonic oral periderm/ectoderm; the only direct support is that functional SNPs near IRF6 were assayed in iPSC-derived embryonic oral epithelium and that two functional SNPs near IRF6 account for most CL/P risk at this locus. Periderm-specific activity of this cCRE is not shown by the data given. | weak | [E06a](#e06a), [E09](#e09) |
| phenotype | Lower AP-2-driven IRF6 enhancer activity on the A allele would impair lip fusion, matching the orofacial-cleft association with effect allele A (p 2e-6); the GTEx IRF6 eQTL (alt G lower IRF6, cerebellum only) runs opposite to this expectation but is in an irrelevant tissue. | weak | [E04](#e04), [E05](#e05), [E06a](#e06a), [E08](#e08) |

Predictions: In oral-epithelial/keratinocyte reporter or base-edited isogenic cells, the G element drives higher activity and higher IRF6 than the A element.; EMSA or ChIP in AP-2-expressing oral epithelium shows more TFAP2A on G than on A.; TFAP2A knockdown abolishes the allelic difference; TFAP2C or ETS2 knockdown does not.; CRISPRi of EH38E2863563 lowers IRF6 without lowering UTP25/TRAF3IP3 in periderm-like cells.

Falsified if: Allele-specific binding assays in a cell type expressing TFAP2A show no AP-2 occupancy or equal occupancy on both alleles.; Isogenic allele swap at rs642961 gives no IRF6 or enhancer-activity difference in oral epithelium.; Enhancer perturbation changes only UTP25/TRAF3IP3 and not IRF6.

### 2. H5: Null: rs642961 is not itself the TF-mediated cleft driver; a linked variant (e.g. the IRF6 promoter SNP rs12403599) carries the risk (p = 0.26)

Null chain: no TF-mediated effect of this variant.

Predictions: Conditioning on rs12403599 (or the other functional SNP near IRF6) removes the rs642961 cleft association.; Isogenic allele swap at rs642961 alone gives no change in enhancer activity or IRF6 expression, while the linked variant does.; Fine-mapping PIP for rs642961 in the orofacial-cleft credible set stays low (~0.05), and no TF shows allele-specific binding at this site.

Falsified if: rs642961 remains associated after conditioning on all nearby candidate variants.; Isogenic allele swaps at rs642961 alone change IRF6 enhancer activity or expression, or a TF shows reproducible allele-specific binding there.

### 3. H4: Same AP-2 binding change, but the regulated gene is UTP25/DIEXF (or TRAF3IP3), not IRF6 (p = 0.12)

TF TFAP2A (stated coverage not_checked; registry own_model), alt allele binds more; element Distal enhancer EH38E2863563 within the IRF6/UTP25/C1orf74 cluster; gene UTP25; cell type Fibroblasts, artery and blood/immune cells (the tissues with the eQTL and blood-pressure signal).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The same AP-2 site is weakened by the ref allele A; TFAP2A chosen as in H1 from the AP-2-alpha biochemical report. Coverage not_checked. | weak | [E09b](#e09b) |
| element | The cCRE is annotated to IRF6, UTP25 and C1orf74 alike, so target assignment from epigenomics alone is ambiguous. | weak | [E03](#e03) |
| gene | UTP25/DIEXF has the highest best L2G (0.75) and the strongest and most numerous GTEx eQTLs at this variant (fibroblasts NES -0.23 p 1.9e-14, artery, blood, lung, adipose), with TRAF3IP3 eQTLs in blood; IRF6 has an eQTL only in cerebellum. | weak | [E05](#e05), [E08](#e08), [E02](#e02) |
| cell_type | The eQTL tissues are fibroblasts, artery, blood and immune cells rather than craniofacial epithelium, consistent with the much stronger blood-pressure association. | weak | [E08](#e08), [E05](#e05), [E04](#e04) |
| phenotype | Altered UTP25/TRAF3IP3 expression could mediate the blood-pressure association (p 6e-12); it is not shown to explain the cleft phenotype, and the allele directions across traits are mixed (hypertension and clefts effect allele A, SBP effect allele G). | weak | [E04](#e04), [E05](#e05), [E08](#e08) |

Predictions: CRISPRi of the element changes UTP25/DIEXF or TRAF3IP3 but not IRF6.; Allele-specific expression at the locus tracks UTP25/TRAF3IP3 in fibroblasts or blood.; Enhancer perturbation in oral epithelium has no effect on IRF6.

Falsified if: Enhancer perturbation changes IRF6 only.; Isogenic allele swap in oral epithelium changes IRF6 without changing UTP25/TRAF3IP3.

### 4. H6: ETS2 binding at an IRF6-proximal regulatory element is altered by this variant, changing IRF6 output in oral epithelium (p = 0.10)

TF ETS2 (stated coverage not_checked; registry own_model), alt allele binds more; element Distal enhancer EH38E2863563 upstream of IRF6; gene IRF6; cell type iPSC-derived embryonic oral epithelium / periderm.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | A genome-engineering study of two functional SNPs near IRF6 in embryonic oral epithelium found allele-specific effects on the binding affinity of FOXE1 or ETS2; ETS2 is the candidate at the IRF6 locus. The quote does not say which SNP or which allele binds more, so the direction (alt G stronger) is assumed by analogy with the AP-2 report and is not directly supported. No QBiC-SELEX evidence supplied, so coverage is not_checked. | weak | [E09c](#e09c), [E06a](#e06a) |
| element | The variant lies in an active distal enhancer-like cCRE assigned to IRF6/UTP25/C1orf74. | supported | [E01](#e01), [E03](#e03) |
| gene | The engineered-allele study measured effector gene expression near IRF6, and IRF6 is the proximal gene with substantial L2G support. | weak | [E06a](#e06a), [E05](#e05), [E02](#e02) |
| cell_type | The allele-specific effects were observed in iPSC-derived embryonic oral epithelium, the tissue relevant to lip fusion. | weak | [E06a](#e06a), [E09](#e09) |
| phenotype | An allele-specific change in IRF6 expression in oral epithelium raises cleft risk on the A allele. | weak | [E04](#e04), [E06a](#e06a) |

Predictions: ETS2 ChIP or in vitro binding shows allelic imbalance at chr1:209815925; ETS2 depletion flattens the allelic difference while AP-2 depletion does not.; An ETS core (GGAA/T) is created or destroyed by the A>G change in the local sequence.

Falsified if: The ETS2 result in that study maps to a different SNP near IRF6, not rs642961.; No ETS core is present at the site, or ETS2 shows no allelic binding.

### 5. H2: The AP-2 paralog TFAP2C, not TFAP2A, is the bound factor, with the same allelic direction (p = 0.08)

TF TFAP2C (stated coverage not_checked; registry own_model), alt allele binds more; element Distal enhancer EH38E2863563 upstream of IRF6; gene IRF6; cell type Surface ectoderm / periderm keratinocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The reported loss of an 'AP-2alpha' site defines an AP-2 motif, which TFAP2A/B/C all read; if TFAP2C is the dominant AP-2 member in the relevant ectodermal cells it is the factor whose binding the ref allele A weakens and alt G favours. The absence of a TFAP2A ENCODE peak at the site is mildly consistent with a different paralog. No QBiC-SELEX evidence supplied, so coverage is not_checked. | weak | [E09b](#e09b), [E07](#e07) |
| element | The same active dELS cCRE carries the variant. | supported | [E01](#e01), [E03](#e03) |
| gene | Target assignment is still to IRF6 by proximity and L2G, with UTP25/TRAF3IP3 not excluded. | weak | [E02](#e02), [E05](#e05) |
| cell_type | The assayed cell context for functional SNPs near IRF6 is iPSC-derived embryonic oral epithelium; no evidence provided shows which AP-2 paralog is expressed there, so paralog assignment is unsupported. | missing | [E09](#e09) |
| phenotype | Lower IRF6 in ectoderm on the A allele leads to failed lip fusion and the cleft association with allele A. | weak | [E04](#e04), [E06a](#e06a) |

Predictions: TFAP2C ChIP-seq in keratinocytes or oral epithelium shows a peak at the variant with allelic imbalance toward G, while TFAP2A does not.; TFAP2C knockdown, not TFAP2A knockdown, removes the allelic enhancer difference.

Falsified if: TFAP2A rather than TFAP2C occupies the site in relevant cells.; No AP-2 family occupancy is detectable at the site.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H4 | H6 | H2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Conditional / joint fine-mapping of the orofacial-cleft GWAS at the IRF6 locus on rs12403599 and the other reported functional SNP (existing summary statistics) | existing data | yes | rs642961 retains an independent cleft signal | rs642961 cleft signal collapses after conditioning | rs642961 signal may persist for blood pressure but weak/absent for clefts | rs642961 retains an independent cleft signal | rs642961 retains an independent cleft signal |
| Base-edited isogenic A vs G iPSC-derived oral epithelium; measure IRF6, UTP25 and TRAF3IP3 expression | high | yes | G higher IRF6; UTP25/TRAF3IP3 unchanged | no allelic difference in any gene | UTP25/TRAF3IP3 change, IRF6 unchanged | G higher IRF6, effect lost on ETS2 depletion | G higher IRF6; UTP25/TRAF3IP3 unchanged |
| Allele-specific ChIP/EMSA for TFAP2A, TFAP2C and ETS2 at chr1:209815925 in oral epithelium or keratinocytes | medium | yes | TFAP2A occupancy biased to G | no allele-specific occupancy by any factor | TFAP2A occupancy biased to G (same binding, different target) | ETS2 occupancy allele-biased; AP-2 not | TFAP2C, not TFAP2A, occupancy biased to G |
| CRISPRi of EH38E2863563 in oral epithelial cells and in fibroblasts, RNA-seq readout | high | no | IRF6 down in oral epithelium | element may still regulate a gene, but with no allelic dependence | UTP25/TRAF3IP3 down, IRF6 unchanged | IRF6 down in oral epithelium | IRF6 down in oral epithelium |
| TF knockdown panel (TFAP2A, TFAP2C, ETS2) with allelic reporter assay | medium | no | TFAP2A knockdown removes allelic difference | no allelic difference to remove | TFAP2A knockdown removes allelic difference but on a UTP25-directed readout | ETS2 knockdown removes it | TFAP2C knockdown removes it |

## Next experiment

Run conditional/joint association analysis of the orofacial-cleft GWAS at the IRF6 locus, conditioning rs642961 on rs12403599 and the other reported functional SNP near IRF6, using existing summary statistics; persistence of an independent rs642961 cleft signal favours H1, collapse favours the null H5.

## Investigate calls

- chip_peaks({"tf": "TFAP2A", "biosample": null})
- eqtl_lookup({"tissue": null})
- literature_search({"query": "rs642961 IRF6 enhancer AP-2 allele-specific cleft lip"})

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

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs642961&size=100; retrieved 2026-10-25T17:29:42+00:00)

> 8 GWAS Catalog associations for rs642961, strongest first:
> Systolic blood pressure: p 6.0e-12, effect allele G, risk-allele frequency NR, PMID 38689001
> Hypertension: p 2.0e-08, effect allele A, risk-allele frequency 0.1951, PMID 33230300
> Pulse pressure: p 1.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Diastolic blood pressure: p 3.0e-07, effect allele G, risk-allele frequency NR, PMID 38689001
> Orofacial clefts: p 2.0e-06, effect allele A, risk-allele frequency NR, PMID 19270707

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:29:41+00:00)

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

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20AND%20UTP25%20AND%20%22cleft%20lip%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:29:43+00:00)

> Europe PMC: 2 hits for 'rs642961 AND UTP25 AND "cleft lip"'; top 2 with PMIDs:
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 37161310 (2023): A Variant in the <i>IRF6</i> Promoter Associated with the Risk for Orofacial Clefting.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-25T17:29:43+00:00)

> Conditional analyses of GWAS data suggest the two functional SNPs near IRF6 account for the majority of risk for CL/P at this locus.

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 37161310 (https://europepmc.org/article/MED/37161310; retrieved 2026-10-25T17:29:43+00:00)

> The single-nucleotide polymorphism (SNP) rs2235371 (IRF6 V274I) is associated with nonsyndromic cleft lip with or without cleft palate (NSCL/P) in Han Chinese and other populations but appears to be without a functional effect.

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 37161310 (https://europepmc.org/article/MED/37161310; retrieved 2026-10-25T17:29:43+00:00)

> This study revealed that the SNP rs12403599, within the IRF6 promoter, is associated with all phenotypes of NSCL/P, especially nonsyndromic cleft lip (NSCLO) and a subphenotype of it, microform cleft lip (MCL).

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:31:05+00:00)

> No ENCODE TFAP2A ChIP-seq peak contains chr1:209815925:A>G. Absence can also mean no TFAP2A experiment in that biosample. 0 peaks lie within 100 bp without containing it.

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

<a id="e09"></a>**E09** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs642961%20IRF6%20enhancer%20AP-2%20allele-specific%20cleft%20lip&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T00:23:46+00:00)

> Europe PMC: 21 hits for 'rs642961 IRF6 enhancer AP-2 allele-specific cleft lip'; top 8 with PMIDs:
> PMID 40670354 (2025): Identification of functional non-coding variants associated with orofacial cleft.
> PMID 39500877 (2024): High incidence and geographic distribution of cleft palate in Finland are associated with the IRF6 gene.
> PMID 39397453 (2024): [Single nucleotide polymorphism heritability of non-syndromic cleft lip with or without cleft palate in Chinese population].
> PMID 34310873 (2021): Family based and case-control designs reveal an association of TFAP2A in nonsyndromic cleft lip only among Vietnamese population.
> PMID 35110662 (2022): Allele-specific transcription factor binding in a cellular model of orofacial clefting.
> PMID 35226783 (2022): Revisiting the embryogenesis of lip and palate development.
> PMID 26332872 (2016): Toward an orofacial gene regulatory network.
> PMID 32031521 (2020): Analysis of zebrafish periderm enhancers facilitates identification of a regulatory variant near human <i>KRT8/18</i>.

<a id="e09a"></a>**E09a** literature_search, Europe PMC abstract, PMID 26332872 (https://europepmc.org/article/MED/26332872; retrieved 2026-10-26T00:23:46+00:00)

> In addition, a common variant (rs642961) in the IRF6 locus is found in 30% of the world's population and contributes risk for isolated orofacial clefting.

<a id="e09b"></a>**E09b** literature_search, Europe PMC abstract, PMID 26332872 (https://europepmc.org/article/MED/26332872; retrieved 2026-10-26T00:23:46+00:00)

> Biochemical studies revealed that rs642961 abrogates one of four AP-2alpha binding sites.

<a id="e09c"></a>**E09c** literature_search, Europe PMC abstract, PMID 40670354 (https://europepmc.org/article/MED/40670354; retrieved 2026-10-26T00:23:46+00:00)

> For two SNPs near IRF6 and one near FOXE1, we engineer the genome of induced pluripotent stem cells, differentiate the cells into embryonic oral epithelium, and discover allele-specific effects on the levels of effector gene expression, and, in two cases, the binding affinity of transcription factors FOXE1 or ETS2.
