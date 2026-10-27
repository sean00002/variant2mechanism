# rs13078086 and Colorectal cancer

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.02 over 7 model calls; 336 s.

Variant `chr3:191441666:T>G` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: none. Occupancy unknown: EBF4 (z -60.28); TFAP2A (z -18.37); TFAP2C (z -18.37); TFAP2E (z -18.37); ETV3 (z 13.11). Diagnostic, not shown to the model: 209 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0: Null: no TF-mediated effect of chr3:191441666:T>G (p = 0.72)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this base in HCT116 or any ENCODE biosample.; No cCRE, GWAS, Open Targets, or GTEx eQTL signal connects this variant to colorectal cancer or nearby gene expression.; Any disease association would reflect a linked causal variant, chance, or a passenger event rather than a TF binding change at this base.

Falsified if: ChIP, MPRA, or another allele-specific occupancy assay shows a TF footprint at this base in colorectal cancer cells.; Such occupancy is linked to allele-specific expression of PYDC2 or another nearby gene and to a colorectal cancer phenotype.

### 2. H2: TFAP2E/AP-2 is predicted to bind the ref allele more strongly at a cryptic intronic site (p = 0.12)

TF TFAP2E (QBiC-SELEX coverage own_model), ref allele binds more; element PYDC2-AS1 intron, 42 bp from dELS EH38E2269392; gene PYDC2; cell type HCT116 colorectal cancer cells (DepMap ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2E/AP-2 is predicted to bind the ref T allele more strongly than the alt G allele (QBiC-SELEX effect -0.765, z -18.37). The AP-2 signal is family-ambiguous: TFAP2A, TFAP2C, and TFAP2E share the same TFAP2E-mapped model and identical effect statistics, so TFAP2E is named only because it has the highest HCT116 expression and an own model among the AP-2 candidates; no ENCODE ChIP-seq peak contains the variant, and TFAP2A ChIP-seq in HCT116 shows no peak, although absence can reflect no experiment. | weak | [E13](#e13), [E11](#e11), [E12](#e12), [E09](#e09), [E04](#e04), [E15](#e15) |
| element | The variant is intronic in PYDC2-AS1 and does not overlap a cCRE; the nearest element is a dELS 42 bp away, and its reported z-scores are maxima over ENCODE biosamples, so a functional AP-2 site here would be cryptic and non-registry. | supported | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb, but no GTEx v8 eQTL links this variant to PYDC2 expression, including in Colon Transverse, leaving the target gene uncertain. | missing | [E02](#e02), [E07](#e07), [E17](#e17) |
| cell_type | HCT116 is the expression context, and TFAP2E is expressed there at 8.5 TPM, higher than the other AP-2 candidates, but there is no HCT116 ChIP evidence showing AP-2 occupancy at this site and the family signal is not uniquely attributable to TFAP2E. | weak | [E13](#e13), [E04](#e04), [E15](#e15) |
| phenotype | Any colorectal cancer effect would require altered AP-2 occupancy to change PYDC2 or nearby gene expression; current genetic and literature evidence do not establish this chain, and the expression direction is unknown because AP-2 factors can activate or repress. | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E08](#e08) |

Predictions: AP-2 family ChIP or an allele-specific reporter assay in HCT116 would show stronger binding or activity for the ref T allele than for the alt G allele.; TFAP2E knockdown would reduce the allele-specific AP-2 effect if TFAP2E is the relevant family member.; PYDC2 or nearby gene expression would change with the allele if this element is functional.

Falsified if: No AP-2 family occupancy is detected at this base in HCT116.; TFAP2E is not the relevant AP-2 factor, or the allele effect is absent or reversed.; The variant does not affect PYDC2 or nearby gene expression.

### 3. H1: EBF4 is predicted to bind the ref allele more strongly at a cryptic intronic site (p = 0.08)

TF EBF4 (QBiC-SELEX coverage own_model), ref allele binds more; element PYDC2-AS1 intron, 42 bp from dELS EH38E2269392; gene PYDC2; cell type HCT116 colorectal cancer cells (DepMap ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | EBF4 is predicted to bind the ref T allele more strongly than the alt G allele (QBiC-SELEX effect -1.954, z -60.28). EBF4 was chosen because it has the largest QBiC-SELEX allele effect among the candidates, but occupancy is unknown: no ENCODE ChIP-seq peak contains this variant and EBF4 was never assayed by ENCODE; EBF4 is also expressed at only 1.22 TPM in HCT116. | weak | [E10](#e10), [E09](#e09), [E04](#e04) |
| element | The variant is intronic in PYDC2-AS1 and does not overlap a registered cCRE; the nearest element is a dELS 42 bp away, and its reported chromatin z-scores are maxima over ENCODE biosamples rather than HCT116-specific evidence. | supported | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb, but no GTEx v8 eQTL links this variant to PYDC2 expression, including in Colon Transverse, so the target-gene assignment is speculative. | missing | [E02](#e02), [E07](#e07), [E17](#e17) |
| cell_type | HCT116 is the supplied expression context, and EBF4 is expressed there at a low level (1.22 TPM, rank 988/1626); this is compatible with but does not demonstrate a functional EBF4 role in this cell type, and no HCT116 occupancy evidence exists. | weak | [E10](#e10), [E04](#e04) |
| phenotype | A colorectal cancer effect would require allele-specific EBF4 occupancy to change PYDC2 or nearby gene expression; current GWAS, Open Targets, eQTL, and literature evidence do not establish this chain, and the direction of any expression effect is unknown because EBF4 could activate or repress. | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E08](#e08) |

Predictions: EBF4 ChIP or an allele-specific reporter assay in HCT116 would show stronger binding or activity for the ref T allele than for the alt G allele at this base.; EBF4 knockdown would reduce the allele-specific effect if EBF4 is the responsible factor.; If PYDC2 is the target, PYDC2 expression would correlate with the EBF4-bound allele.

Falsified if: EBF4 does not occupy this site in HCT116 or colorectal cancer cells.; The allele-specific binding effect is absent or reversed in an occupancy assay.; No change in PYDC2 or nearby gene expression is linked to the variant.

### 4. H3: ETV3 is predicted to bind the alt allele more strongly at a cryptic intronic site (p = 0.08)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element PYDC2-AS1 intron, 42 bp from dELS EH38E2269392; gene PYDC2; cell type HCT116 colorectal cancer cells (DepMap ACH-000971).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3 is predicted to bind the alt G allele more strongly than the ref T allele, but only weakly: the best reported ETV3 model in E14 is a CIS-BP-mapped ETV5 model (effect +0.251, z 13.11), while E16 shows ETV3's own model does not pass the QBiC-SELEX gate (effect +0.115, z 3.5) and its alt site strength is 95.9th percentile, below the strong-site threshold; other Ets-family models at this base, including ELF1 and ELF2, predict ref>alt. No ENCODE ChIP-seq peak contains the variant and ETV3 was never assayed by ENCODE, so occupancy is unknown. | weak | [E14](#e14), [E16](#e16), [E09](#e09), [E04](#e04) |
| element | The variant is intronic in PYDC2-AS1 and does not overlap a cCRE; the nearest element is a dELS 42 bp away, so an ETV3 site here would be cryptic and not supported by current cCRE annotation. | supported | [E01](#e01), [E03](#e03) |
| gene | PYDC2 is the nearest protein-coding gene at 19.5 kb, but no GTEx v8 eQTL links this variant to PYDC2 expression, including in Colon Transverse, so the target gene is not established. | missing | [E02](#e02), [E07](#e07), [E17](#e17) |
| cell_type | HCT116 is the expression context, and ETV3 is expressed there at 16.34 TPM, but there is no HCT116 ChIP evidence showing ETV3 occupancy at this site, and the binding prediction comes from a mapped ETV5 model at a weak site. | weak | [E14](#e14), [E04](#e04) |
| phenotype | A colorectal cancer effect would require allele-specific ETV3 occupancy to alter PYDC2 or nearby gene expression; current GWAS, Open Targets, eQTL, and literature evidence do not establish this, and the direction of any expression change is unknown because ETV3 could activate or repress. | missing | [E05](#e05), [E06](#e06), [E07](#e07), [E08](#e08) |

Predictions: ETV3 ChIP or an allele-specific reporter assay in HCT116 would show stronger binding or activity for the alt G allele than for the ref T allele.; ETV3 knockdown would reduce the allele-specific effect if ETV3 is the responsible Ets factor.; PYDC2 or nearby gene expression would change with the allele in colorectal cancer cells.

Falsified if: ETV3 does not occupy this site in HCT116 or colorectal cancer cells.; The allele-specific binding effect is absent or reversed in an occupancy assay.; The mapped ETV5 model does not reflect ETV3 binding here, or no downstream expression effect is found.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H2 | H1 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific AP-2 family ChIP-qPCR in HCT116 at chr3:191441666 | medium | yes | No AP-2 occupancy above background or no ref>alt allele difference at this base. | AP-2 occupancy with the ref T allele stronger than the alt G allele. | No AP-2 occupancy; EBF4 is not tested by this assay. | No AP-2 occupancy or no allele difference. |
| Allele-specific EBF4 ChIP-qPCR in HCT116 at chr3:191441666 | medium | no | No EBF4 occupancy or no allele difference at this base. | No EBF4 occupancy. | EBF4 occupancy stronger on the ref T allele than on the alt G allele. | No EBF4 occupancy. |
| Allele-specific ETV3 ChIP-qPCR in HCT116 at chr3:191441666 | medium | no | No ETV3 occupancy or no allele difference at this base. | No ETV3 occupancy. | No ETV3 occupancy. | ETV3 occupancy stronger on the alt G allele than on the ref T allele. |
| Allele-specific MPRA of a 200-bp element containing the variant in HCT116 | medium | yes | No allele-specific reporter activity. | Ref T > alt G reporter activity. | Ref T > alt G reporter activity. | Alt G > ref T reporter activity. |
| Colon Transverse GTEx eQTL lookup for variant and PYDC2 (existing data) | existing data | no | No significant eQTL, consistent with no variant-to-PYDC2 regulatory link. | No significant eQTL, so the gene link remains missing. | No significant eQTL, so the gene link remains missing. | No significant eQTL, so the gene link remains missing. |

## Next experiment

Allele-specific AP-2 family ChIP-qPCR in HCT116 at chr3:191441666 (TFAP2A/TFAP2E), with input and no-antibody controls: ref>alt AP-2 occupancy supports H2, while no AP-2 occupancy supports H0 and separates the top two chains.

## Investigate calls

- chip_peaks({"tf": "TFAP2A", "biosample": "HCT116"})
- qbic_tf_detail({"tf": "ETV3"})
- eqtl_lookup({"tissue": "Colon - Transverse"})

## Flags

- none

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

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr3:191441666:T>G, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 0 of 0 occupied (0 with a strong site), 5 of 85 with unknown occupancy. Left out: 16 TFs assayed in the matching biosample and 557 assayed only elsewhere, none with a peak here. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element. No ENCODE TF ChIP-seq peak contains this variant in any biosample; QBiC-SELEX changes below have no occupancy support.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EBF4 (EBF1, 2 models; QBiC-SELEX coverage: own model): best model EBF4_FL_TCGATT40NTTG_KK_nitta2015_1_3_7mer (its own model), z -60.28, effect -1.954: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.22 TPM, rank 988 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 99.7th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2A (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -18.37, effect -0.765: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.18 TPM, rank 657 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2C (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -18.37, effect -0.765: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.59 TPM, rank 883 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2E (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (its own model), z -18.37, effect -0.765: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.5 TPM, rank 553 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.7th, alt 99.6th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 13.11, effect 0.251: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 16.34 TPM, rank 334 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 94.6th, alt 95.3th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:34:00+00:00)

> No ENCODE TFAP2A ChIP-seq peak contains chr3:191441666:T>G in biosamples matching 'HCT116'. Absence can also mean no TFAP2A experiment in that biosample. 0 peaks lie within 100 bp without containing it.

<a id="e16"></a>**E16** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"ETV3","symbol":"ETV3","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr3:191441666:T>G","gate_p":5.02e-05,"models":[{"model":"ETV3_NA_TCAGGA20NCG_ESW_yang2017_1_4_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.775,"effect":0.115,"z":3.5,"p":0.00047,"rank_abs_z":"283/997","passed_gate":false,"site_strength":{"ref_percentile":72.7,"alt_percentile":95.9,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":-0.231,"z":-7.84,"p":4.3e-15,"rank_abs_z":"28/997","passed_gate":true,"site_strength":{"ref_percentile":72.6,"alt_percentile":86.8,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":-0.705,"z":-4.96,"p":7e-07,"rank_abs_z":"139/997","passed_gate":true,"site_strength":{"ref_percentile":66.1,"alt_percentile":83.2,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":-0.291,"z":-3.78,"p":0.00016,"rank_abs_z":"250/997","passed_gate":false,"site_strength":{"ref_percentile":91.9,"alt_percentile":80.7,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":0.124,"z":0.97,"p":0.33,"rank_abs_z":"725/997","passed_gate":false,"site_strength":{"ref_percentile":68.6,"alt_percentile":70.8,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":0.149,"z":1.6,"p":0.11,"rank_abs_z":"594/997","passed_gate":false,"site_strength":{"ref_percentile":74.8,"alt_percentile":96.5,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":0.138,"z":2.01,"p":0.044,"rank_abs_z":"527/997","passed_gate":false,"site_strength":{"ref_percentile":75.0,"alt_percentile":74.1,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.125,"z":3.97,"p":7.3e-05,"rank_abs_z":"222/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":94.1,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":0.217,"z":1.72,"p":0.085,"rank_abs_z":"571/997","passed_gate":false,"site_strength":{"ref_percentile":80.6,"alt_percentile":93.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":-0.236,"z":-3.54,"p":0.00039,"rank_abs_z":"275/997","passed_gate":false,"site_strength":{"ref_percentile":95.1,"alt_percentile":95.7,"k":7}}],"n_models_trimmed":8}

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr3_191441666_T_G_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:00+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr3_191441666_T_G_b38 in tissues matching 'Colon - Transverse'. NES is the effect of the alt allele (G) relative to ref (T).
