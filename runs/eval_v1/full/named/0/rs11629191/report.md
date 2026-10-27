# rs11629191 and Breast cancer

Configuration `full`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.56 over 7 model calls; 196 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## QBiC-SELEX screen

445 of 997 models pass the gate. Top groups: bZIP, 1 model (best XBP1, z -91.69); bZIP, 4 models (best CREB3, z -76.89); SAND, 2 models (best SP140L, z -57.31); bZIP, 3 models (best ATF2, z -49.19); CxxC, 2 models (best CXXC4, z -44.11).

## Ranked chains

### 1. H1: Null: no TF-mediated effect of rs11629191 (passenger / linked variant / no allelic activity) (p = 0.72)

Null chain: no TF-mediated effect of this variant.

Predictions: No allelic difference in MPRA or luciferase reporters at this site in MCF7 or other breast lines; No allele-specific ATAC or ChIP signal at chr14:55887040 in breast cells; No significant breast eQTL for PELI2, KTN1 or any neighbouring gene (consistent with E19); Variant stays outside breast cancer credible sets in larger GWAS (consistent with E04, E05); CRISPRi tiling of the site changes no neighbouring gene's expression

Falsified if: A breast cancer credible set includes rs11629191 with demonstrated allele-specific regulatory activity; Reproducible allele-specific ChIP-seq or ATAC-seq is observed at chr14:55887040 in breast cells; An MPRA shows a significant, replicated allelic effect at this site

### 2. H2: Alt allele weakens a strong XBP1 bZIP site in a cryptic element near PELI2 in ER-positive breast cells (p = 0.10)

TF XBP1 (stated coverage own_model; registry own_model), ref allele binds more; element unannotated non-coding site 1.9 kb from the dELS cCRE EH38E1716463; no cCRE overlap; gene PELI2 (assigned by distance only); cell type ER-positive luminal breast carcinoma (MCF7).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | QBiC-SELEX predicts the ref C allele binds an XBP1-type bZIP site more strongly (own XBP1 model, z -91.69, effect -3.167); XBP1 is the sole TF in group G382 and is very highly expressed in MCF7 (636 TPM), so the group's specificity is assigned to XBP1. This is an in vitro prediction only, and the site-strength change is small (100.0th to 98.7th percentile) | weak | [E07](#e07), [E08](#e08) |
| element | No cCRE overlaps the variant and the nearest dELS is 1.9 kb away, so any element here is unannotated and at best weakly or cell-type-restrictedly active; the site is also not conserved (GERP -3.12). E01 is internally inconsistent (reports intron_variant but lists no transcript consequences) | missing | [E01](#e01), [E03](#e03) |
| gene | No functional link to any gene is available; PELI2 is nominated solely as the nearest protein-coding TSS (231 kb), and there is no breast eQTL for this variant | missing | [E02](#e02), [E19](#e19) |
| cell_type | XBP1 is abundant in MCF7, so the TF is present in this context; no evidence shows the site is open or bound in MCF7, and no XBP1 ChIP peak is found there | weak | [E08](#e08), [E18](#e18) |
| phenotype | No evidence links PELI2 to breast cancer risk: Open Targets gives an overall score of 0.00 and the literature places PELI2 only in prognostic gene lists for other cancers; this link is unsupported | missing | [E06](#e06), [E06a](#e06a), [E20](#e20), [E04](#e04) |

Predictions: Allele-specific XBP1 ChIP-seq in MCF7 with stronger occupancy on C; C allele gives higher reporter activity than T in MCF7, and the difference is lost in XBP1-low cells or after XBP1 knockdown; ER/UPR stimulation (tunicamycin, which activates XBP1s) amplifies the allelic reporter difference

Falsified if: No XBP1 ChIP signal at this locus in an MCF7 XBP1 ChIP experiment that is performed; Reporter activity is equal for both alleles; XBP1 knockdown leaves the allelic difference unchanged

### 3. H3: Alt allele weakens a CRE bound by CREB1/ATF1, reducing basal activity of a cryptic element in the PELI2-KTN1 interval (p = 0.06)

TF CREB1 (stated coverage own_model; registry own_model), ref allele binds more; element unannotated CRE-like site in the PELI2/KTN1 intergenic region (no cCRE within 500 bp); gene PELI2 or KTN1 (distance only; unresolved); cell type MCF7 breast carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Group G062 predicts weaker alt binding (own CREB1 model, z -37.47, effect -2.019; CREM z -29.21). Within the group CREB1 (30.3 TPM) and ATF1 (25.9 TPM) are similarly expressed, so TF identity is ambiguous; CREB1 is named because it carries the own model and the top z, which is a weak basis. Site strength falls only from the 99.2nd to the 91.5th percentile | weak | [E07](#e07), [E16](#e16) |
| element | No annotated cCRE lies within 500 bp, so the CRE-like element is asserted from sequence alone and is at best weakly active | missing | [E03](#e03), [E01](#e01) |
| gene | Target assigned by proximity only (PELI2 231 kb, KTN1 328 kb); no breast eQTL exists for this variant and the single QTL credible set concerns ENSG00000259868 in brain with PIP 0.03 | missing | [E02](#e02), [E05](#e05), [E19](#e19) |
| cell_type | CREB1, ATF1 and CREM are all expressed in MCF7, giving expression context only; no evidence of locus activity in MCF7 | weak | [E16](#e16) |
| phenotype | No evidence connects altered PELI2 or KTN1 dosage to breast cancer risk (Open Targets score 0.00) | missing | [E20](#e20), [E06a](#e06a), [E04](#e04) |

Predictions: ENCODE MCF7 CREB1 or ATF1 ChIP-seq shows a peak at this position with reference-allele bias; cAMP/forskolin stimulation amplifies the allelic reporter difference, unlike all other chains; CREB1 knockdown collapses the allelic difference while XBP1 knockdown does not

Falsified if: No CREB1 or ATF1 occupancy at the locus in MCF7 ChIP-seq; No allelic reporter difference under cAMP stimulation

### 4. H4: Alt allele weakens a TGIF/MEIS homeodomain repressor site, de-repressing a nearby element (p = 0.06)

TF TGIF1 (stated coverage mapped; registry own_model), ref allele binds more; element unannotated intergenic homeodomain-bound site at 14q22; gene KTN1 or PELI2 (distance only); cell type MCF7 breast carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Group G008 predicts weaker alt binding of a TGIF/MEIS specificity (best model TGIF2, z -38.69, effect -2.43; 7 passing models all the same sign). TGIF1 is the most expressed member in MCF7 (39.9 TPM) but is covered only through a CIS-BP-mapped model, so the TF within the group is chosen on expression and remains ambiguous (TGIF2 20.5 TPM, MEIS3 15.6 TPM also expressed) | weak | [E07](#e07), [E13](#e13) |
| element | No cCRE overlaps the variant and the site is not conserved, so a repressive/cryptic element is speculation | missing | [E03](#e03), [E01](#e01) |
| gene | No functional data tie the site to a gene; KTN1 (328 kb) and PELI2 (231 kb) are nominated by distance only, and no breast eQTL exists | missing | [E02](#e02), [E19](#e19) |
| cell_type | TGIF1, TGIF2 and MEIS3 are expressed in MCF7, providing a possible repressive context only | weak | [E13](#e13) |
| phenotype | Because TGIF proteins typically repress, weaker binding would raise target expression; no evidence links this to breast cancer risk | missing | [E04](#e04), [E20](#e20) |

Predictions: Alt allele shows higher, not lower, reporter activity (opposite direction to H2, H3, H6); TGIF1 knockdown raises reporter activity specifically on the C allele; Deletion of the site increases, not decreases, KTN1/PELI2 expression

Falsified if: Alt allele shows lower or equal reporter activity; No TGIF1/TGIF2 ChIP-seq occupancy at the site

### 5. H6: Alt allele destroys a GC-box EGR site (largest site-strength loss among expressed groups) in a cryptic element at 14q22 (p = 0.06)

TF EGR1 (stated coverage mapped; registry own_model), ref allele binds more; element unannotated GC-rich site at chr14:55887040 (no cCRE overlap); gene PELI2 (distance only); cell type MCF7 breast carcinoma cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Group G019 predicts weaker alt binding of an EGR C2H2 specificity (best model EGR2, z -30.48, effect -1.10) with a large site-strength drop (100.0th to 76.4th percentile), larger than for XBP1 or CREB1. Within the group EGR3 (12.8 TPM) and EGR1 (10.8 TPM) are expressed while EGR2 (0.23 TPM) is not, so EGR1 is named on expression and its well-documented activity in breast cells; EGR1 is covered through a CIS-BP-mapped model, not its own passing model, so the attribution is uncertain | weak | [E07](#e07), [E17](#e17) |
| element | No cCRE overlaps the variant; a GC-box-containing element here is inferred from sequence alone and is unconserved (GERP -3.12) | missing | [E03](#e03), [E01](#e01) |
| gene | No eQTL or contact data; PELI2 nominated by distance only | missing | [E02](#e02), [E19](#e19) |
| cell_type | EGR1 and EGR3 are expressed in MCF7, giving context only | weak | [E17](#e17) |
| phenotype | No GWAS association and no Open Targets support for PELI2 in breast cancer, so the phenotype link is unsupported | missing | [E04](#e04), [E20](#e20) |

Predictions: EGR1 ChIP-seq in MCF7 shows reference-biased occupancy; XBP1 and CREB1 ChIP do not; Serum or PMA stimulation (which induces EGR1) amplifies the allelic reporter difference; EGR1 knockdown, but not XBP1 knockdown, abolishes the allelic difference

Falsified if: No EGR1 occupancy at the site in MCF7; Allelic reporter difference persists after EGR1 knockdown

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H4 | H6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XBP1 ChIP-seq peak lookup at chr14:55887040 in MCF-7 (Factorbook/ENCODE) | existing data | yes | No peak (already observed, E18) | Peak with reference-allele bias expected; current absence (E18) argues against H2, though no MCF7 XBP1 experiment may exist | No XBP1 peak required | No XBP1 peak required | No XBP1 peak required |
| GTEx/eQTL Catalogue lookup of rs11629191 in Breast - Mammary Tissue for PELI2, KTN1 and all genes within 1 Mb | existing data | yes | No significant eQTL (already observed, E19) | PELI2 eQTL with lower expression on T | PELI2 or KTN1 eQTL with lower expression on T | KTN1/PELI2 eQTL with higher expression on T | PELI2 eQTL with lower expression on T |
| Allele-specific luciferase/MPRA of the 200 bp around the variant in MCF7 | medium | yes | No allelic difference | C > T activity, enhanced by UPR induction | C > T activity, enhanced by forskolin | T > C activity | C > T activity, enhanced by serum/PMA |
| ATAC-seq / H3K27ac allele-specific signal at chr14:55887040 in MCF7 and normal breast epithelium | existing data | yes | No accessibility or acetylation; site closed | Open chromatin with C-biased accessibility | Open chromatin with C-biased accessibility | Site may be closed on C (repressed) and more open on T | Open chromatin with C-biased accessibility |
| TF knockdown panel in MCF7 (XBP1, CREB1, TGIF1, EGR1) with reporter or endogenous PELI2 readout | high | no | No knockdown changes an allelic effect because none exists | Only XBP1 knockdown removes the allelic difference | Only CREB1/ATF1 knockdown removes it | TGIF1 knockdown raises C-allele activity | Only EGR1 knockdown removes it |
| Breast cancer GWAS fine-mapping (BCAC) credible-set membership of rs11629191 and its LD partners | existing data | yes | Variant absent from credible sets, or weight on a linked variant (consistent with E04, E05) | rs11629191 in a breast cancer credible set | rs11629191 in a breast cancer credible set | rs11629191 in a breast cancer credible set | rs11629191 in a breast cancer credible set |

## Next experiment

Query existing MCF7 epigenomic and QTL data first: allele-specific ATAC/H3K27ac and XBP1 ChIP signal at chr14:55887040 in MCF-7 (zero cost, uses released ENCODE data). If the site is closed and unbound, as E03, E18 and E19 already suggest, H1 stands and H2 falls; if an open, C-biased footprint is present, proceed to the allele-specific luciferase assay in MCF7 with and without XBP1 knockdown.

## Investigate calls

- chip_peaks({"tf": "XBP1", "biosample": "MCF-7"})
- eqtl_lookup({"tissue": "Breast - Mammary Tissue"})
- gene_disease({"gene": "PELI2"})

## Flags

- literature_fallback: no hits for 'rs11629191 AND PELI2 AND "breast cancer"'; dropped the rsID
- coverage_misstated: H4: stated mapped, registry says own_model for TGIF1
- coverage_misstated: H6: stated mapped, registry says own_model for EGR1

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/14:55887040-55887040:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T17:32:49+00:00)

> Variant chr14:55887040:C>T (GRCh38), allele string C/T
> Known IDs: rs11629191
> Most severe consequence: intron_variant
> Regulatory features: none
> GERP conservation score at the site: -3.12
> Transcript consequences: none (intergenic)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/14:54887040-56887040?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T17:32:40+00:00)

> 14 protein-coding genes within 1000 kb of chr14:55887040:C>T, by distance to TSS:
> PELI2: 230.8 kb from TSS (upstream, strand +1)
> KTN1: 328.0 kb from TSS (downstream, strand +1)
> TBPL2: 430.3 kb from TSS (upstream, strand -1)
> ATG14: 475.2 kb from TSS (upstream, strand -1)
> TMEM260: 601.3 kb from TSS (upstream, strand +1)
> CHMP4BP1: 615.7 kb from TSS (downstream, strand +1)
> FBXO34: 615.7 kb from TSS (downstream, strand +1)
> DLGAP5: 695.4 kb from TSS (upstream, strand -1)
> LGALS3: 765.7 kb from TSS (downstream, strand +1)
> MAPK1IP1L: 835.4 kb from TSS (downstream, strand +1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T17:32:13+00:00)

> No cCRE overlaps the variant; nearest is EH38E1716463 (dELS) 1868 bp away.
> SCREEN: 0 cCREs within 500 bp (max z-score across ENCODE biosamples):
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs11629191&size=100; retrieved 2026-10-25T17:32:50+00:00)

> 0 GWAS Catalog associations for rs11629191, strongest first:

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:32:49+00:00)

> 1 credible sets contain 14_55887040_C_T: 0 GWAS, 1 molecular QTL.
> eqtl for ENSG00000259868 (gtex-v10_ge_brain_nucleus_accumbens_ensg0000025986): PIP 0.03

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PELI2%20AND%20%22breast%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T17:32:50+00:00)

> Europe PMC: 178 hits for 'PELI2 AND "breast cancer"'; top 7 with PMIDs:
> PMID 41023515 (2025): Pellino ubiquitin ligases: double-edged swords in hematologic malignancies-from oncogenic stabilizers to therapeutic vulnerabilities.
> PMID 41331176 (2025): Construction and validation of risk models of prognostic genes associated with parthanatos in papillary thyroid carcinoma based on bioinformatics.
> PMID 40362379 (2025): &lt;i&gt;O&lt;/i&gt;-Desmethyltramadol Enhanced Anti-Cancer Efficacy over Tramadol Through Non-μ-Opioid Receptor and Differential Cellular Contexts of Human Breast Cancer Cells.
> PMID 42757486 (2026): Pemetrexed increases BRCA1 protein stability and sensitizes TNBC cells to radiotherapy.
> PMID 42734444 (2027): Anesthesia inhalation agent sevoflurane induces perioperative cognitive impairment: Apelin/early growth response 1 axis induces ferritinophagy and exacerbates ferroptosis.
> PMID 41079921 (2025): PRMT1/PRMT5-Mediated Differential Arginine Methylation of CRIP1 Promotes the Recurrence of Small Cell Lung Cancer after Chemotherapy.
> PMID 42380137 (2026): HOXC9 accelerates esophageal squamous cell carcinoma progression via OTUD1-FABP5-mediated lipid metabolic reprogramming.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 41331176 (https://europepmc.org/article/MED/41331176; retrieved 2026-10-25T17:32:50+00:00)

> ResultsSeven prognostic genes (TSHZ3, SERGEF, AKAP12, SGPP2, ASGR1, AK1, PELI2) were identified.

<a id="e07"></a>**E07** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr14:55887040:C>T: 997 models scored, 445 pass the gate (Bonferroni 0.05/997, p < 5.02e-05, |z| > 4.05), in 324 CIS-BP groups. Expression context: DepMap line ACH-000019. Groups shown: 10; dropped because no TF in the group reaches 1 TPM: 95 (GCM, 2 models z 44.55, C2H2 ZF, 1 model z 33.3, bZIP, 1 model z -32.97, bZIP, 1 model z -29.97, bHLH, 1 model z -16.81). predicted_effect > 0 means the alternate allele binds more strongly. In vitro binding only: expression and chromatin decide whether a change matters.

<a id="e08"></a>**E08** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G382 (bZIP, 1 model): best model XBP1_eDBD_TCCTTG40NGGT_KAN_yin2017_0_4_7mer (own model of XBP1), z -91.69, effect -3.167 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: XBP1 z -91.69. TFs this group covers (own and CIS-BP-mapped models): XBP1 636.57 TPM; best model's site strength: ref 100.0th, alt 98.7th percentile of its k-mer coefficients.

<a id="e09"></a>**E09** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G017 (bZIP, 4 models): best model CREB3_NA_TAGAAC20NCG_ESAD_yang2017_0_3_7mer (own model of CREB3), z -76.89, effect -1.64 (alt binds less); 4 passing models (4 with the best model's sign). Passing members: CREB3 z -76.89, CREB3L1 z -60.99, CREB3L2 z -49.16, CREB3L4 z -37.55. TFs this group covers (own and CIS-BP-mapped models): CREB3L4 48.8 TPM, CREB3 45.81 TPM, CREB3L2 7.06 TPM, CREB3L1 0.09 TPM; best model's site strength: ref 99.9th, alt 98.2th percentile of its k-mer coefficients.

<a id="e10"></a>**E10** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G099 (SAND, 2 models): best model SP140L_FL_TG40NGACCTT_YWPA_jolma2025_0_2_7mer (own model of SP140L), z -57.31, effect -1.491 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: SP140L z -57.31, SP140 z -16.92. TFs this group covers (own and CIS-BP-mapped models): SP140L 7.63 TPM, SP140 0.86 TPM; best model's site strength: ref 99.9th, alt 72.0th percentile of its k-mer coefficients.

<a id="e11"></a>**E11** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G033 (bZIP, 3 models): best model ATF2_eDBD_TGAACC40NCCA_KP_yin2017_0_3_7mer (own model of ATF2), z -49.19, effect -1.348 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: ATF2 z -49.19, CREB5 z -6.61. TFs this group covers (own and CIS-BP-mapped models): ATF7 20.81 TPM, ATF2 16.22 TPM, CREB5 0.02 TPM, ATF7-NPFF; best model's site strength: ref 99.7th, alt 95.7th percentile of its k-mer coefficients.

<a id="e12"></a>**E12** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G064 (CxxC, 2 models): best model CXXC4_FL_GG40NTAGTTT_YWKC_jolma2025_0_4_7mer (own model of CXXC4), z -44.11, effect -2.102 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: CXXC4 z -44.11, TET3 z -20.67. TFs this group covers (own and CIS-BP-mapped models): CXXC5 77.02 TPM, TET3 9.96 TPM, CXXC4 0.33 TPM; best model's site strength: ref 98.8th, alt 70.2th percentile of its k-mer coefficients.

<a id="e13"></a>**E13** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G008 (Homeodomain, 9 models): best model TGIF2_eDBD_TTGCAA40NGTG_KO_yin2017_0_4_7mer (own model of TGIF2), z -38.69, effect -2.43 (alt binds less); 7 passing models (7 with the best model's sign). Passing members: TGIF2 z -38.69, MEIS3 z -23.79, PKNOX2 z -19.46, TGIF2LY z -17.27, TGIF2LX z -15.65 (+2 more). TFs this group covers (own and CIS-BP-mapped models): TGIF1 39.86 TPM, TGIF2 20.51 TPM, MEIS3 15.61 TPM, PKNOX1 7.53 TPM, MEIS2 6.32 TPM, MEIS1 1.52 TPM, PKNOX2 0.05 TPM, TGIF2LX 0.0 TPM, TGIF2LY 0.0 TPM; best model's site strength: ref 99.8th, alt 94.1th percentile of its k-mer coefficients.

<a id="e14"></a>**E14** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G012 (bZIP, 6 models): best model NRL_eDBD_TGGAGA40NCCA_KR_yin2017_0_4_7mer (own model of NRL), z -38.05, effect -1.53 (alt binds less); 6 passing models (6 with the best model's sign). Passing members: NRL z -38.05, MAF z -34.57, MAFG z -27.77, MAFB z -27.66, MAFK z -24.11 (+1 more). TFs this group covers (own and CIS-BP-mapped models): MAFK 16.96 TPM, MAFG 8.48 TPM, MAFB 3.09 TPM, MAFA 1.07 TPM, NRL 0.98 TPM, MAF 0.23 TPM; best model's site strength: ref 100.0th, alt 99.5th percentile of its k-mer coefficients.

<a id="e15"></a>**E15** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G381 (bHLH, 1 model): best model USF3_DBD_CG40NACGGTT_YWCB_jolma2025_0_1_7mer (own model of USF3), z -37.78, effect -0.258 (alt binds less); 1 passing models (1 with the best model's sign). Passing members: USF3 z -37.78. TFs this group covers (own and CIS-BP-mapped models): USF3 3.82 TPM; best model's site strength: ref 100.0th, alt 59.5th percentile of its k-mer coefficients.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G062 (bZIP, 2 models): best model CREB1_eDBD_TTTGAC40NGGT_KR_yin2017_0_3_7mer (own model of CREB1), z -37.47, effect -2.019 (alt binds less); 2 passing models (2 with the best model's sign). Passing members: CREB1 z -37.47, CREM z -29.21. TFs this group covers (own and CIS-BP-mapped models): CREB1 30.28 TPM, ATF1 25.91 TPM, CREM 24.59 TPM; best model's site strength: ref 99.2th, alt 91.5th percentile of its k-mer coefficients.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> Group G019 (C2H2 ZF, 4 models): best model EGR2_NA_TCGGCC20NGA_ESW_yang2017_0_3_7mer (own model of EGR2), z -30.48, effect -1.1 (alt binds less); 3 passing models (3 with the best model's sign). Passing members: EGR2 z -30.48, EGR3 z -23.43, EGR1 z -6.33. TFs this group covers (own and CIS-BP-mapped models): EGR3 12.82 TPM, EGR1 10.78 TPM, EGR2 0.23 TPM, EGR4 0.0 TPM; best model's site strength: ref 100.0th, alt 76.4th percentile of its k-mer coefficients.

<a id="e18"></a>**E18** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T17:34:02+00:00)

> No ENCODE XBP1 ChIP-seq peak contains chr14:55887040:C>T in biosamples matching 'MCF-7' (0 peaks within 100 bp). Absence can also mean no XBP1 experiment in that biosample.

<a id="e19"></a>**E19** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr14_55887040_C_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T17:34:02+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr14_55887040_C_T_b38 in tissues matching 'Breast - Mammary Tissue'. NES is the effect of the alt allele (T) relative to ref (C).

<a id="e20"></a>**E20** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T17:34:03+00:00)

> Open Targets: PELI2 and breast cancer (MONDO_0007254), overall score 0.00; by evidence type: literature 0.01
