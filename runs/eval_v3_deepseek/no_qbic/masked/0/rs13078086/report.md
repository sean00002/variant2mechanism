# rs13078086 and Colorectal cancer

Configuration `no_qbic`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.01 over 7 model calls; 307 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H0: No TF-mediated effect; intronic passenger or linked variant (p = 0.95)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding or chromatin-state change at chr3:191441666 in HCT116.; No cis-eQTL for PYDC2, CCDC50, or other nearby genes in colorectal cancer contexts.; Any disease association would be due to linkage disequilibrium with another variant or chance.

Falsified if: Allele-specific ChIP-seq, CUT&RUN, or MPRA shows a TF binding difference at this base.; A significant cis-eQTL for a nearby gene is found in colorectal cancer cells.

### 2. H1: CTCF gain at nearby dELS alters PYDC2 expression (p = 0.03)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2269392 dELS, 42 bp away; gene PYDC2; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: CTCF binds the alt G allele more strongly than the ref T. No QBiC-SELEX model or data for CTCF is supplied, and E04/E09 report no CTCF ChIP-seq peak over this variant in HCT116; the binding-direction claim is therefore unsupported and speculative. | missing | [E04](#e04), [E09](#e09) |
| element | The variant lies 42 bp from dELS EH38E2269392 and does not overlap a cCRE (E03), but there is no evidence that this dELS is active in HCT116 or that the variant changes its activity. | weak | [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene, 19.5 kb upstream (E02), and the variant is intronic in PYDC2-AS1 (E01); however, GTEx reports no significant eQTL for this variant, including in colon transverse (E07,E10), so the gene link is only distance/annotation-based. | weak | [E01](#e01), [E02](#e02), [E07](#e07), [E10](#e10) |
| cell_type | HCT116 is the supplied expression context, but E04 reports no HCT116 TF ChIP-seq peak at this base, and there is no positive evidence that a CTCF-PYDC2 axis is active in HCT116. | missing | [E04](#e04) |
| phenotype | A CTCF-gain-to-PYDC2-to-colorectal-cancer effect is speculative; GWAS, Open Targets, and eQTL evidence are null (E05-E07,E10), and the literature hits do not directly link this variant or PYDC2 to colorectal cancer (E08). | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E08](#e08), [E10](#e10) |

Predictions: Allele-specific CTCF ChIP or CUT&RUN at this base or the 42-bp dELS, with alt stronger than ref.; CTCF knockdown or dCas9 disruption changes PYDC2 expression or enhancer-promoter contact in HCT116.; No comparable allele-specific effect for RELA.

Falsified if: No allele-specific CTCF occupancy is detected at this locus in HCT116.; CTCF knockdown does not change PYDC2 expression or chromatin contact.; Another TF is shown to mediate the allele-specific effect.

### 3. H2: RELA/NF-kB gain at nearby dELS increases PYDC2 expression (p = 0.02)

TF RELA (QBiC-SELEX coverage own_model), alt allele binds more; element EH38E2269392 dELS, 42 bp away; gene PYDC2; cell type HCT116 colorectal cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Hypothesis: RELA binds the alt G allele more strongly than the ref T. No QBiC-SELEX model or data for RELA is supplied, and E04 reports no RELA ChIP-seq peak over this variant in HCT116; the binding-direction claim is unsupported and speculative. | missing | [E04](#e04) |
| element | The variant is 42 bp from dELS EH38E2269392 and not within a cCRE (E03), but there is no evidence that RELA binds this dELS in HCT116 or that the variant changes enhancer activity. | weak | [E03](#e03) |
| gene | PYDC2 is 19.5 kb upstream (E02) and the variant is intronic in PYDC2-AS1 (E01), but GTEx reports no significant eQTL for this variant, including in colon transverse (E07,E10); the RELA-to-PYDC2 gene link is unsupported. | weak | [E01](#e01), [E02](#e02), [E07](#e07), [E10](#e10) |
| cell_type | HCT116 is only the supplied expression context; E04 reports no HCT116 TF ChIP-seq peak at this base, and there is no positive evidence for a RELA-PYDC2 regulatory axis in HCT116. | missing | [E04](#e04) |
| phenotype | An inflammasome/PYDC2 effect on colorectal cancer is plausible in general but not demonstrated here; GWAS, Open Targets, and eQTL evidence are null (E05-E07,E10), and the literature does not directly connect this variant, RELA, or PYDC2 to colorectal cancer (E08). | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E08](#e08), [E10](#e10) |

Predictions: Allele-specific RELA ChIP or CUT&RUN at this base or the nearby dELS, with alt stronger than ref.; NF-kB inhibition or RELA knockdown reduces PYDC2 expression in HCT116.; CTCF does not show the same allele-specific occupancy.

Falsified if: No allele-specific RELA occupancy is detected at this locus.; RELA knockdown or NF-kB inhibition does not affect PYDC2 expression.; The disease-linked effect is independent of PYDC2.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 |
| --- | --- | --- | --- | --- | --- |
| Allele-specific CTCF CUT&RUN or ChIP-qPCR at chr3:191441666 in HCT116 (ref vs alt) | medium | yes | No allele-specific CTCF occupancy at this base. | CTCF occupancy is stronger on alt G than ref T at this base or the flanking dELS. | No allele-specific CTCF occupancy; any effect would be RELA-dependent. |
| Allele-specific RELA ChIP or CUT&RUN at chr3:191441666 in HCT116 (ref vs alt) | medium | no | No allele-specific RELA occupancy at this base. | No allele-specific RELA occupancy; CTCF is the proposed mediator instead. | RELA occupancy is stronger on alt G than ref T at this base or the flanking dELS. |
| Existing GTEx colon transverse eQTL lookup for PYDC2/CCDC50 | existing data | yes | No significant cis-eQTL for nearby genes. | Significant PYDC2 cis-eQTL with an alt-allele effect. | Significant PYDC2 cis-eQTL with an alt-allele effect. |
| CRISPRi/knockout of PYDC2 in HCT116 with colorectal cancer growth or expression readout | high | yes | No PYDC2 dependency or variant-linked expression effect. | PYDC2 expression changes with CTCF perturbation and affects growth. | PYDC2 expression changes with RELA perturbation and affects growth. |

## Next experiment

Perform targeted allele-specific CTCF CUT&RUN (or ChIP-qPCR) at chr3:191441666 in HCT116, comparing alt and ref reads; this is the cheapest test that separates H0 from H1, the top two chains.

## Investigate calls

- chip_peaks({"tf": "CTCF", "biosample": "HCT116"})
- eqtl_lookup({"tissue": "Colon - Transverse"})
- gene_dependency({"gene": "PYDC2"})

## Flags

- tool_failed: E11 gene_dependency: DepMap CRISPR lookup failed: PYDC2 not in the matrix

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/3:191441666-191441666:1/G?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:32:09+00:00)

> Variant chr3:191441666:T>G (GRCh38), allele string T/G
> Known IDs: rs13078086
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: -1.82
> Transcript consequences: PYDC2-AS1 (intron_variant, non_coding_transcript_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/3:190441666-192441666?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:06+00:00)

> 8 protein-coding genes within 1000 kb of chr3:191441666:T>G, by distance to TSS:
> PYDC2: 19.5 kb from TSS (upstream, strand +1)
> UTS2B: 111.1 kb from TSS (upstream, strand -1)
> CCDC50: 112.6 kb from TSS (downstream, strand +1)
> OSTN: 242.4 kb from TSS (downstream, strand +1)
> GMNC: 549.2 kb from TSS (upstream, strand -1)
> IL1RAP: 954.2 kb from TSS (downstream, strand +1)
> TMEM207: 991.8 kb from TSS (upstream, strand -1)
> FGF12: 1326.1 kb from TSS (downstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:05+00:00)

> No cCRE overlaps the variant; nearest is EH38E2269392 (dELS) 42 bp away.
> SCREEN: 1 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E2269392 dELS: DNase z 3.5, H3K27ac z 1.8, H3K4me3 z 1.5, CTCF z 1.5; nearby genes AC073365.1, PYDC2, CCDC50
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> No ENCODE TF ChIP-seq peak contains chr3:191441666:T>G in any biosample. In the matching biosample HCT116: 0 peaks from 0 factors. No cCRE contains the variant. Of the TFs with a binding model, 16 were assayed in the matching biosample and 557 only elsewhere, all without a peak here; 536 were never assayed.

<a id="e05"></a>**E05** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs13078086&size=100; retrieved 2026-10-25T17:32:10+00:00)

> 0 GWAS Catalog associations for rs13078086, strongest first:

<a id="e06"></a>**E06** finemap_lookup, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:09+00:00)

> Open Targets has no record of 3_191441666_T_G.

<a id="e07"></a>**E07** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38. NES is the effect of the alt allele (G) relative to ref (T).

<a id="e08"></a>**E08** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PYDC2%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:10+00:00)

> Europe PMC: 16 hits for 'PYDC2 AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 40026444 (2025): Correlation Analysis of Pyroptosis-Related Genes CASP1, NLRP3, AIM2, and NLRP1 With Lung Adenocarcinoma.
> PMID 41154652 (2025): Oncogenic Role of SAMD4B in Breast Cancer Progression by Activating Wnt/β-Catenin Pathway.
> PMID 36319832 (2022): A novel refined pyroptosis and inflammasome-related genes signature for predicting prognosis and immune microenvironment in pancreatic ductal adenocarcinoma.
> PMID 36341349 (2022): The strategies of NLRP3 inflammasome to combat <i>Toxoplasma gondii</i>.
> PMID 36732864 (2023): RNA binding protein SAMD4: current knowledge and future perspectives.
> PMID 39561929 (2024): Optimizing iNKT-driven immune responses against cancer by modulating CD1d in tumor and antigen presenting cells.
> PMID 35159382 (2022): Metabolomics of Acute vs. Chronic Spinach Intake in an Apc-Mutant Genetic Background: Linoleate and Butanoate Metabolites Targeting HDAC Activity and IFN-γ Signaling.
> PMID 35338151 (2022): PUMILIO proteins promote colorectal cancer growth via suppressing p21.

<a id="e09"></a>**E09** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T00:26:42+00:00)

> No ENCODE CTCF ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT116'. Absence can also mean no CTCF experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e10"></a>**E10** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (G) relative to ref (T).

<a id="e11"></a>**E11** gene_dependency (failed), DepMap CRISPR (; retrieved local)

> DepMap CRISPR lookup failed: PYDC2 not in the matrix
