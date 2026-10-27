# rs6983267 and Colorectal cancer (8q24)

Configuration `no_qbic`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.54 over 7 model calls; 169 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## Ranked chains

### 1. H3: TCF7L2 bound preferentially to the G allele restrains POU5F1B; the T allele relieves this and raises POU5F1B in colon (p = 0.32)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element cCRE EH38E3858447 (pELS) within the POU5F1B intron, 78.9 kb from the POU5F1B TSS; gene POU5F1B; cell type Colon epithelium / colorectal carcinoma cells (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies this base in HCT 116 (ENCSR000EUV); the proposed direction is stronger binding to ref G, with TCF7L2 acting here as a repressor of POU5F1B, since more binding need not mean more activity. No QBiC-SELEX model was supplied, so coverage is not checked and the direction is untested. | weak | [E07](#e07) |
| element | The variant lies in an active pELS cCRE whose SCREEN-linked genes are CCAT2, PCAT1 and POU5F1B, and the variant is intronic to POU5F1B. | supported | [E01](#e01), [E03](#e03) |
| gene | The alt T allele is associated with higher POU5F1B in transverse colon (GTEx NES +0.20, p 8.2e-06), the direction expected if G-bound TCF7L2 represses, and Open Targets L2G ranks POU5F1B first (0.89) versus MYC (0.05). | supported | [E08](#e08), [E05](#e05), [E02](#e02) |
| cell_type | The eQTL is in colon tissue and the TCF7L2 peak is in a colorectal line; POU5F1B is a TWAS-implicated colorectal susceptibility gene. | weak | [E08](#e08), [E07](#e07), [E06b](#e06b) |
| phenotype | POU5F1B promotes CRC cell proliferation and metastasis, so higher POU5F1B on the T allele is a coherent route to the T-associated CRC risk reported in the strongest association. | weak | [E06c](#e06c), [E04](#e04) |

Predictions: CRISPRi of EH38E3858447 in HCT 116 raises or leaves POU5F1B unchanged while MYC is unaffected.; TCF7L2 knockdown increases POU5F1B in colon lines.; Allele-specific POU5F1B expression in heterozygous colon tissue favours T.; MPRA at this base shows higher enhancer output for T in colon cells.

Falsified if: POU5F1B is unaffected by element perturbation or TCF7L2 depletion.; Allele-specific expression of POU5F1B favours G.; No TCF7L2 footprint overlaps the variant base in colon cells.

### 2. H1: G allele strengthens a TCF7L2 site in the 8q24 enhancer, raising long-range MYC expression in colon epithelium (p = 0.26)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element ENCODE cCRE EH38E3858447 / Ensembl enhancer ENSR8_CGMBX at chr8:127401060; gene MYC; cell type Colorectal carcinoma epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 occupies this base in HCT 116 (one ENCODE TCF7L2 peak containing the variant, ENCSR000EUV; three further peaks in HepG2), so the TF is physically present at the site; the direction (ref G bound more strongly, consistent with a better TCF/LEF T-site match) is a hypothesis only, as no QBiC-SELEX model was supplied (coverage not checked) and no allele-specific ChIP data were provided. | weak | [E07](#e07) |
| element | The variant lies in an active proximal enhancer-like cCRE (EH38E3858447) with high DNase/H3K27ac z-scores (maxima across biosamples) and an annotated Ensembl enhancer. | supported | [E01](#e01), [E03](#e03) |
| gene | MYC is 334 kb upstream and is proposed as the long-range target; the cited evidence does not support this (L2G for MYC is only 0.05 versus 0.89 for POU5F1B, and no colon eQTL for MYC is reported), so this link rests on the absence of a nearer coding gene other than POU5F1B. | missing | [E02](#e02), [E05](#e05), [E08](#e08) |
| cell_type | TCF7L2 ChIP signal at this base is documented specifically in HCT 116, the supplied expression context; no cited evidence quantifies Wnt activity in that line. | weak | [E07](#e07) |
| phenotype | MYC is required for growth of HCT 116 and of bowel lines generally (CRISPR effect -1.27; 98% of bowel lines dependent), although MYC is a common essential, so this is permissive rather than lineage-specific support for the CRC association at rs6983267. | weak | [E09](#e09), [E04](#e04), [E06a](#e06a) |

Predictions: Allele-specific TCF7L2 ChIP in heterozygous colon cells shows G-allele enrichment.; CRISPRi/deletion of EH38E3858447 lowers MYC mRNA in HCT 116 more than POU5F1B or PVT1.; 4C/Hi-C from the element shows a contact with the MYC promoter at 335 kb.; Colon eQTL for MYC emerges in larger or tumour-specific datasets.

Falsified if: Enhancer perturbation leaves MYC unchanged while POU5F1B or PVT1 change.; No allele-specific TCF7L2 occupancy at chr8:127401060.; TCF7L2 binds the T allele more strongly.

### 3. H4: Null: no TF-mediated allelic effect of rs6983267 itself (p = 0.20)

Null chain: no TF-mediated effect of this variant.

Predictions: Reporter, MPRA or base-editing assays show no allelic difference at chr8:127401060 in colon cells.; TCF7L2 ChIP in heterozygous colon cells shows balanced allelic occupancy despite a peak at the site.; Fine-mapping in additional ancestries moves the credible set to a neighbouring variant in the EH38E3858446/448 cluster.; Colon eQTL signals at POU5F1B and PVT1 are driven by a linked variant, not this base.

Falsified if: A reproducible allele-specific reporter/MPRA effect at this exact base.; Allele-specific TF binding or allele-specific POU5F1B/CCAT2/PVT1 expression in heterozygous colon cells.

### 4. H2: Allelic TCF7L2 binding alters the overlapping lncRNA CCAT2/CASC8 transcript at the variant (p = 0.12)

TF TCF7L2 (stated coverage not_checked; registry mapped), ref allele binds more; element CCAT2 exon overlapping cCRE EH38E3858447; gene CCAT2; cell type Colorectal carcinoma epithelium (HCT 116).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds this base in HCT 116 by ENCODE ChIP-seq; the ref-G-binds-more direction is assumed, not shown, and no QBiC-SELEX model was supplied (coverage not checked). | weak | [E07](#e07) |
| element | The variant is an exonic position of CCAT2 (and intronic in CASC8) inside an active pELS cCRE, so TF occupancy here could affect both transcription and transcript sequence. | weak | [E01](#e01), [E03](#e03) |
| gene | CCAT2 is the transcript directly overlapping the variant; the only reported cis-eQTL in the same transcript family is CASC8 in whole blood (NES -0.32 for alt T), and no colon eQTL for CCAT2 is reported, so effector status is unproven. | weak | [E01](#e01), [E08](#e08) |
| cell_type | The cCRE is active and TCF7L2-bound in HCT 116, but no cited data show CCAT2 expression level in that line. | weak | [E03](#e03), [E07](#e07) |
| phenotype | CCAT2 is repeatedly reviewed as a gastrointestinal-cancer lncRNA at 8q24, matching the CRC association, but only review-level titles are cited, so this link is weak. | weak | [E04](#e04), [E06](#e06), [E06a](#e06a) |

Predictions: CCAT2 RNA shows allelic imbalance favouring G in heterozygous colorectal tumours.; CCAT2 knockdown reduces proliferation in HCT 116 without changing POU5F1B.; Enhancer CRISPRi changes CCAT2/CASC8 levels more than POU5F1B or MYC.

Falsified if: CCAT2 expression is allele-independent in heterozygous colon samples.; Enhancer perturbation changes POU5F1B or MYC but not CCAT2.

### 5. H5: The element acts as a CTCF-dependent anchor whose allelic occupancy tunes PVT1 in colonic secretory cells (p = 0.10)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element CTCF-marked pELS cluster EH38E3858446/447/448; gene PVT1; cell type Colonic goblet (MUC2+/SPDEF+) epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The cCRE cluster carries CTCF signal (z 4.1 at the variant-containing element, 5.5 nearby), but these are maxima across biosamples over 250 bp elements; no allelic or base-level CTCF evidence is cited and no QBiC-SELEX model was supplied, so coverage is not checked and this binding claim is the weakest of the set. | weak | [E03](#e03) |
| element | The variant lies in an open, CTCF-marked pELS that could act as a loop anchor as well as an enhancer. | weak | [E01](#e01), [E03](#e03) |
| gene | The only molecular QTL among the 92 credible sets containing this variant is a single-cell eQTL for PVT1 in colon goblet cells (PIP 0.95), pointing to a target not proposed by the other chains. | weak | [E05](#e05) |
| cell_type | That QTL is specific to MUC2+/SPDEF+ colonic goblet cells, a cell type not represented by HCT 116, so the effect may be invisible in the supplied expression context. | weak | [E05](#e05) |
| phenotype | PVT1 is the lncRNA neighbouring MYC at 8q24 and altered PVT1 output could plausibly affect colonic epithelial proliferation; no cited evidence links PVT1 to the CRC association here. | missing | [E04](#e04) |

Predictions: Allele-specific CTCF ChIP signal at chr8:127401060 in colon cells.; PVT1 shows genotype-dependent expression in colon secretory cells but not in HCT 116.; Element deletion changes local loop structure measured by Hi-C without changing MYC in HCT 116.

Falsified if: No CTCF footprint at the variant base.; PVT1 expression is genotype-independent in colon single-cell data.; Element perturbation changes POU5F1B or MYC with no PVT1 change.

## Prediction matrix

| Test | Cost | Separates top two | H3 | H1 | H4 | H2 | H5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dCas9-KRAB CRISPRi of EH38E3858447 in HCT 116, RT-qPCR of MYC, POU5F1B, CCAT2/CASC8, PVT1 | medium | yes | POU5F1B changes (de-repression or loss, depending on element polarity); MYC unchanged | MYC falls; POU5F1B largely unchanged | Element may still be functional, but effect is genotype-independent; no prediction tied to the variant base | CCAT2/CASC8 falls most; MYC and POU5F1B little changed | No change in HCT 116 (goblet-cell-restricted effect) |
| Allele-specific TCF7L2 ChIP-seq (or ChIP-qPCR with allele counting) in heterozygous colon cells | medium | no | G-allele enriched reads | G-allele enriched reads | Balanced allelic occupancy | G-allele enriched reads | Balanced TCF7L2; allelic CTCF instead |
| Existing GTEx/Open Targets colon eQTL and sc-eQTL readout | existing data | yes | POU5F1B up with T in transverse colon (observed) | No MYC colon eQTL expected (unsupportive) | Signals attributable to linked variants | CASC8 eQTL in blood only; no colon CCAT2 signal | PVT1 sc-eQTL in goblet cells (observed) |
| MPRA / prime-edited isogenic G vs T HCT 116 clones, RNA-seq | high | yes | T clones show higher POU5F1B | T clones show lower MYC | No allelic difference in any gene | T clones show lower CCAT2 | No difference in HCT 116 |
| TCF7L2 siRNA knockdown in HCT 116, RT-qPCR of MYC and POU5F1B | low | yes | POU5F1B rises (repression relieved) | MYC falls | Changes, if any, unrelated to this variant | CCAT2 falls | Little change; CTCF-dependent instead |
| 4C/Hi-C from EH38E3858447 in HCT 116 | high | yes | Contact with POU5F1B promoter | Strong contact with MYC promoter | Contacts present but genotype-independent | Local contacts within CCAT2/CASC8 | CTCF-anchored loop toward PVT1 |

## Next experiment

TCF7L2 siRNA knockdown in HCT 116 followed by RT-qPCR of MYC and POU5F1B (low cost): H1 predicts MYC falls with little POU5F1B change, H3 predicts POU5F1B rises as TCF7L2 repression is relieved, so it directly separates the top two chains before committing to CRISPRi or prime editing.

## Investigate calls

- chip_peaks({"tf": "TCF7L2", "biosample": "HCT116"})
- eqtl_lookup({"tissue": null})
- gene_dependency({"gene": "MYC"})

## Flags

- none

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401060-127401060:1/T?content-type=application/json&Conservation=1; retrieved 2026-10-25T16:33:46+00:00)

> Variant chr8:127401060:G>T (GRCh38), allele string G/T
> Known IDs: rs6983267
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: 1.54
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401060-128401060?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T16:33:42+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401060:G>T, by distance to TSS:
> POU5F1B: 78.9 kb from TSS (in gene body, strand +1)
> MYC: 334.4 kb from TSS (upstream, strand +1)
> LRATD2: 842.6 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T16:32:58+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs6983267&size=100; retrieved 2026-10-25T16:33:55+00:00)

> 69 GWAS Catalog associations for rs6983267, strongest first:
> Colorectal cancer: p 2.0e-122, effect allele T, risk-allele frequency NR, PMID 36539618
> Prostate-specific antigen levels: p 9.0e-121, effect allele T, risk-allele frequency NR, PMID 39930085
> Prostate cancer: p 1.0e-113, effect allele G, risk-allele frequency NR, PMID 33398198
> Elevated prostate specific antigen [PSA] (PheCode 796): p 2.0e-96, effect allele G, risk-allele frequency 0.5087, PMID 39024449
> prostate-specific antigen (PSA, maximum, inv-norm transformed): p 7.0e-74, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Cancer (pleiotropy): p 8.0e-74, effect allele G, risk-allele frequency NR, PMID 32887889
> prostate-specific antigen (PSA, mean, inv-norm transformed): p 1.0e-72, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Colorectal cancer or advanced adenoma: p 3.0e-64, effect allele G, risk-allele frequency 0.5228, PMID 30510241
> prostate-specific antigen (PSA, minimum, inv-norm transformed): p 6.0e-52, effect allele G, risk-allele frequency 0.5102, PMID 39024449
> Benign neoplasm of colon (PheCode 208): p 2.0e-48, effect allele G, risk-allele frequency 0.5088, PMID 39024449
> Colon polyps: p 6.0e-30, effect allele G, risk-allele frequency 0.566, PMID 39024449
> Colon cancer (PheCode 153.2): p 8.0e-26, effect allele G, risk-allele frequency 0.5899, PMID 39024449

<a id="e05"></a>**E05** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T16:33:46+00:00)

> 92 credible sets contain 8_127401060_G_T: 91 GWAS, 1 molecular QTL.
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Cancer of prostate (PheCode 185): PIP 1.00; L2G POU5F1B 0.82
> GWAS Elevated prostate specific antigen [PSA] (PheCode 796): PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> sceqtl for PVT1 (OTAR2057_IBDverse_ge_Colon_Goblet_MUC2+_SPDEF+_ENS): PIP 0.95
> Best L2G gene scores across these sets: POU5F1B 0.89, MYC 0.05

<a id="e06"></a>**E06** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=rs6983267%20AND%20POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T16:33:56+00:00)

> Europe PMC: 52 hits for 'rs6983267 AND POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 35812248 (2022): Genome-Wide Association and Transcriptome-Wide Association Studies Identify Novel Susceptibility Genes Contributing to Colorectal Cancer.
> PMID 35987910 (2022): Transposon-activated POU5F1B promotes colorectal cancer growth and metastasis.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.
> PMID 39921239 (2025): System genetic analysis of intestinal cancer and periodontitis development as influenced by aging and diabesity using Collaborative Cross mice.
> PMID 36103972 (2022): Long non-coding RNA colon cancer-associated transcript 2: role and function in human cancers.
> PMID 34594420 (2021): Repurposing non-invasive prenatal testing data: Population study of single nucleotide variants associated with colorectal cancer and Lynch syndrome.

<a id="e06a"></a>**E06a** literature_search, Europe PMC abstract, PMID 35812248 (https://europepmc.org/article/MED/35812248; retrieved 2026-10-25T16:33:56+00:00)

> In the post-GWAS analyses, we first identified new genome-wide significant associations: three genomic risk loci were identified at 8q24.21 (rs6983267, P = 6.98 × 10-12), 15q13.3 (rs58658771, P = 1.40 × 10-10), and 18q21.1 (rs6507874, P = 1.91 × 10-14).

<a id="e06b"></a>**E06b** literature_search, Europe PMC abstract, PMID 35812248 (https://europepmc.org/article/MED/35812248; retrieved 2026-10-25T16:33:56+00:00)

> In addition, the TWAS also identified four loci statistically significantly associated with CRC risk, largely explained by expression regulation, including six candidate genes (DUSP10, POU5F1B, C11orf53, COLCA1, COLCA2, and GREM1-AS1).

<a id="e06c"></a>**E06c** literature_search, Europe PMC abstract, PMID 35987910 (https://europepmc.org/article/MED/35987910; retrieved 2026-10-25T16:33:56+00:00)

> Correlating this observation, we demonstrate that POU5F1B fosters the proliferation and metastatic potential of CRC cells.

<a id="e07"></a>**E07** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-25T16:35:30+00:00)

> 1 ENCODE TCF7L2 ChIP-seq peaks contain chr8:127401060:G>T in biosamples matching 'HCT116': biosamples HCT116; experiments ENCSR000EUV. In other biosamples, 3 TCF7L2 peaks do contain the variant: HepG2 (experiments ENCSR000EVQ, ENCSR346BOD).

<a id="e08"></a>**E08** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 2 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).
> CASC8 in Whole_Blood: NES -0.32, p 6.3e-10
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

<a id="e09"></a>**E09** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for MYC (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): -1.27. Bowel lineage, 63 lines: median -1.89, 98% dependent. All 1183 lines: median -1.83, 95% dependent. common-essential in DepMap: a strong knockout effect here is not evidence for a lineage-specific role.
