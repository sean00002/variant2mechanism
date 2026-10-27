# rs73706717 and Colorectal cancer (8q24)

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.07 over 17 model calls; 292 s.

Variant `chr8:127401265:T>C` (germline); expression context: DepMap:ACH-000971 (HCT 116).

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -8.8, weak site); SP1 (bound here, z -7.07, weak site); NFIC (bound elsewhere, z 24.28); NFIA (bound elsewhere, z 24.28); HNF1B (bound elsewhere, z -23.93); CTCF (bound elsewhere, z 8.21); CEBPB (bound elsewhere, z -6.94); TFAP4 (bound elsewhere, z 0.51, no clear allelic change); NR2F2 (bound elsewhere, z -15.02, weak site); NR2F6 (bound elsewhere, z -15.02, weak site). Occupancy unknown: ZBTB22 (z -33.75); NR1H3 (z -15.02); TET3 (z 14.12); NR1D2 (z -13.82); NR4A2 (z -13.82). Diagnostic, not shown to the model: 307 of 997 models pass Bonferroni.

## Ranked chains

### 1. M4: Null: no TF-mediated effect of this variant (p = 0.66)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF occupancy at this base in HCT116.; No allele-specific enhancer activity or target-gene expression difference attributable to this variant.; Any disease association is due to a linked causal variant, chance, or a passenger event rather than a TF-mediated effect at chr8:127401265.

Falsified if: Reproducible allele-specific TF occupancy at this base is found in HCT116.; An allele-specific enhancer or target-gene expression difference is attributable to this variant.; The disease association is shown to be mediated by a TF binding this exact base.

### 2. M1: TCF7L2 binds the ref allele at an 8q24 enhancer and may regulate MYC (p = 0.17)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element pELS EH38E3858447; gene MYC; cell type HCT116 colorectal cancer cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 binds the ref T allele more strongly than the alt C allele, but exact-base allele specificity is not established. TCF7L2 is expressed in HCT116 (63.61 TPM, rank 53/1626) and has ENCODE ChIP-seq peaks over the variant in HCT116 (E05). QBiC-SELEX gives z=-8.8 and effect=-0.429 for a CIS-BP-mapped TCF7 model, with weak k-mer sites (ref 90.0th, alt 87.2th percentile); no own TCF7L2 model is available (E20, E37). The ChIP peak is not allele-specific. | weak | [E05](#e05), [E20](#e20), [E37](#e37) |
| element | The variant lies in pELS EH38E3858447, an active enhancer-like cCRE with DNase and H3K27ac signal. | supported | [E01](#e01), [E03](#e03) |
| gene | MYC is only a proximity/locus candidate: E02 places MYC 334.2 kb upstream at 8q24 and E18 gives locus biology, but there is no direct colon eQTL linking this SNP to MYC (E17, E35). L2G instead favors POU5F1B in non-colorectal credible sets with low PIP (E16). | weak | [E02](#e02), [E16](#e16), [E17](#e17), [E18](#e18), [E35](#e35) |
| cell_type | HCT116 is a colorectal cancer line in which TCF7L2 is expressed and has an ENCODE ChIP-seq peak over this variant, so the cell context is plausible, though the peak is not allele-specific. | supported | [E05](#e05) |
| phenotype | The colorectal cancer connection is indirect: no GWAS Catalog association for this variant, L2G credible sets are for PSA and urinary incontinence rather than colorectal cancer, and GTEx reports no significant colon eQTL. Literature supports 8q24/MYC/CCAT2/POU5F1B biology but not this specific variant-phenotype mechanism. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E18](#e18), [E35](#e35) |

Predictions: Allele-specific TCF7L2 ChIP in HCT116 should show higher ref T than alt C occupancy at this base.; If TCF7L2 regulates the enhancer, the alt C allele should produce a TCF7L2-dependent change in enhancer activity; the downstream direction depends on whether TCF7L2 activates or represses.; TCF7L2 knockdown or enhancer disruption should attenuate the allele-dependent effect.

Falsified if: Allele-specific TCF7L2 occupancy at this base in HCT116 is not higher on ref T than alt C.; TCF7L2 knockdown or enhancer disruption does not attenuate an allele-dependent enhancer or target-gene effect.; The alt C allele has no reproducible allele-specific effect in a TCF7L2-dependent assay.

### 3. M3: NFIC binds the alt allele strongly in vitro but lacks HCT116 occupancy evidence (p = 0.12)

TF NFIC (QBiC-SELEX coverage own_model), alt allele binds more; element pELS EH38E3858447; gene POU5F1B; cell type HCT116 colorectal cancer cell line, with NFIC occupancy evidence currently only in HepG2.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NFIC binds the alt C allele more strongly than the ref T allele in vitro, but HCT116 occupancy is missing. E41 shows NFIC has its own QBiC-SELEX model that passes the gate strongly (z=23.35, effect=+1.226, alt>ref; strong site), and the mapped NFIB model is also strong (z=24.28, effect=+1.783). NFIC is expressed in HCT116 (36.29 TPM), but ENCODE ChIP-seq occupancy over this variant is reported only in HepG2, not HCT116 (E22, E36). NFIA shares the mapped NFIB model with identical statistics, and E39 finds no NFIA HCT116 peak, so SMAD-family occupancy in HCT116 is unsupported and NFIC versus NFIA identity remains unresolved. | weak | [E22](#e22), [E23](#e23), [E36](#e36), [E39](#e39), [E41](#e41) |
| element | The variant lies in pELS EH38E3858447, an active enhancer-like cCRE with DNase and H3K27ac signal. | supported | [E01](#e01), [E03](#e03) |
| gene | POU5F1B is the best L2G gene at this locus (score 0.83) and is 79.1 kb from the variant. E40 adds a gene-level POU5F1B-colorectal cancer association, but the L2G credible sets are not colorectal cancer. E42 shows POU5F1B is not a selective dependency in HCT116 or bowel lineages, so this target-gene link remains weak and is not supported as a functional dependency. E43 finds no direct NFIC-POU5F1B colorectal cancer literature. | weak | [E02](#e02), [E16](#e16), [E40](#e40), [E42](#e42), [E43](#e43) |
| cell_type | HCT116 expresses NFIC, but the provided ENCODE ChIP data do not show NFIC occupancy over this variant in HCT116; occupancy is only in HepG2, and E36 notes that absence could also mean no NFIC experiment in HCT116. E39 likewise finds no NFIA peak over this variant in HCT116. | weak | [E22](#e22), [E36](#e36), [E39](#e39) |
| phenotype | POU5F1B has a gene-level colorectal cancer association in Open Targets (E40), but the credible sets containing this variant are for PSA and urinary incontinence rather than colorectal cancer, there is no colorectal cancer GWAS association for this variant, GTEx reports no significant colon eQTL, and POU5F1B is not a dependency in HCT116/bowel lineages (E42). No provided evidence ties this specific NFIC-binding allele to colorectal cancer. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E35](#e35), [E40](#e40), [E42](#e42) |

Predictions: If NFIC acts here, alt C should increase NFIC occupancy in HCT116 and alter POU5F1B expression in an NFIC-dependent manner.; NFIC knockdown should reduce the alt-C-dependent enhancer or POU5F1B effect.; The effect should be absent in cell types where NFIC does not occupy this element.; A TF-specific assay should distinguish NFIC from NFIA.

Falsified if: Alt C does not increase NFIC occupancy at this base in HCT116.; NFIC knockdown does not alter the alt-C-dependent enhancer or POU5F1B effect.; The effect is present where NFIC does not occupy this element.; A more specific assay fails to distinguish NFIC from NFIA and does not support NFIC over NFIA.

### 4. M2: SP1 binds the ref allele at the pELS and may regulate CCAT2 (p = 0.05)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element pELS EH38E3858447; gene CCAT2; cell type HCT116 colorectal cancer cell line.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 binds the ref T allele more strongly than the alt C allele, but allele-specific SP1 binding is not supported. SP1 is expressed in HCT116 (38.96 TPM) and has HCT116 ENCODE ChIP-seq peaks over the variant (E06). The SP1 own QBiC-SELEX model does not pass the gate (z=-0.11, effect=-0.007); only CIS-BP-mapped SP3 (z=-7.07, effect=-0.298) and SP9 (z=-6.42, effect=-0.485) pass, both at weak k-mer sites, and mapped SP3/SP9 changes cannot substitute for SP1 (E21, E38). | weak | [E06](#e06), [E21](#e21), [E38](#e38) |
| element | The variant lies in pELS EH38E3858447, an active enhancer-like cCRE with DNase and H3K27ac signal. | supported | [E01](#e01), [E03](#e03) |
| gene | CCAT2 is a positional candidate only: the variant lies in a CCAT2 non_coding_transcript_exon and the cCRE is annotated near CCAT2, but there is no direct evidence that this variant regulates CCAT2 or that SP1 mediates such regulation. | weak | [E01](#e01), [E03](#e03) |
| cell_type | HCT116 is a colorectal cancer line in which SP1 is expressed and ChIP-bound over this variant, although the peak is not allele-specific. | supported | [E06](#e06) |
| phenotype | The CCAT2 colorectal cancer connection is indirect in the provided literature; CCAT2 is discussed mainly in gastric/gastrointestinal cancer, and no provided genetic data link this variant to colorectal cancer through CCAT2. | weak | [E15](#e15), [E16](#e16), [E17](#e17), [E18](#e18), [E35](#e35) |

Predictions: Allele-specific SP1 ChIP in HCT116 should show higher ref T than alt C occupancy if M2 is correct.; If SP1 regulates CCAT2 through this enhancer, the alt C allele should alter SP1-dependent enhancer activity and CCAT2 expression.; SP1 knockdown should reduce the allele-dependent enhancer or CCAT2 effect.

Falsified if: Allele-specific SP1 occupancy at this base in HCT116 is not higher on ref T than alt C.; SP1 knockdown does not reduce an allele-dependent enhancer or CCAT2 effect.; The SP1 own QBiC-SELEX model remains non-significant and mapped SP3/SP9 effects cannot be shown to reflect SP1 binding at this base.

## Prediction matrix

| Test | Cost | Separates top two | M4 | M1 | M3 | M2 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 ChIP-qPCR at chr8:127401265 in HCT116 | medium | yes | No reproducible allele-specific TCF7L2 occupancy at this base. | Ref T > alt C TCF7L2 occupancy at this base in HCT116. | No allele-specific TCF7L2 occupancy; NFIC would instead show alt C > ref T if measured. | No allele-specific TCF7L2 occupancy; SP1 may be bound but is not tested by this assay. |
| Allele-specific NFIC ChIP-qPCR at chr8:127401265 in HCT116 | medium | no | No reproducible allele-specific NFIC occupancy. | No allele-specific NFIC occupancy. | Alt C > ref T NFIC occupancy at this base in HCT116. | No allele-specific NFIC occupancy. |
| TCF7L2 knockdown or CRISPRi in HCT116 with an allele-specific enhancer readout | medium | no | No allele-dependent effect to attenuate. | TCF7L2 knockdown reduces the allele-dependent enhancer effect. | No TCF7L2-dependent allele effect. | No TCF7L2-dependent allele effect. |
| NFIC knockdown in HCT116 with an allele-specific enhancer or POU5F1B readout | medium | no | No allele-dependent effect to attenuate. | No NFIC-dependent allele effect. | NFIC knockdown reduces the alt-C-dependent enhancer or POU5F1B effect. | No NFIC-dependent allele effect. |
| POU5F1B CRISPR knockout growth/expression readout in HCT116 | low | no | No variant-specific POU5F1B effect. | No specific requirement for POU5F1B dependency. | If POU5F1B mediates the phenotype, perturbation should show a POU5F1B-dependent effect; E42 already argues against a selective dependency. | No specific requirement for POU5F1B dependency. |

## Next experiment

Allele-specific TCF7L2 ChIP-qPCR at chr8:127401265 in HCT116 (or another heterozygous colorectal line), comparing ref T versus alt C occupancy; this is the cheapest direct test separating M4 from M1.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- eqtl_lookup({"tissue": "Colon"}) for M1.gene, ran as [E35](#e35). Expected: I expect a null result (no significant colon eQTL for MYC, CCAT2, or POU5F1B at this variant), consistent with the pan-tissue null in E17. If null, M1.gene stays weak and M1 does not rise above the null; a significant colon eQTL for MYC would upgrade M1.gene and strengthen M1, while a POU5F1B eQTL would favor M3 over M1.
- chip_peaks({"tf": "NFIC", "biosample": "HCT116"}) for M3.binding, ran as [E36](#e36). Expected: I expect no NFIC HCT116 peak over the variant, since E22 reports occupancy only in HepG2. If absent, M3.binding remains weak and M3 should fall; if present, M3 gains the missing HCT116 occupancy link and its alt-allele chain rises.
- qbic_tf_detail({"tf": "TCF7L2"}) for M1.binding, ran as [E37](#e37). Expected: I expect QBiC-SELEX coverage only through a CIS-BP-mapped TCF7/TCF7L2 model, not a TCF7L2 own model, matching E20. That would keep M1.binding weak and prevent overinterpreting the ref>alt QBiC result as TCF7L2-specific; an own model with a clear allele effect would strengthen M1.binding, while absence of coverage would weaken M1.

- Result of eqtl_lookup({"tissue":"Colon"}): E35 reports 0 significant GTEx v8 colon eQTLs for chr8_127401265_T_C_b38; NES is alt vs ref. This is a null result for colon eQTLs, consistent with the pan-tissue null in E17 and with no direct variant-to-MYC, CCAT2, or POU5F1B eQTL support in colon. It does not upgrade M1.gene and does not specifically favor M3 over M1 because there is no POU5F1B colon eQTL either. (as expected: yes)
- Result of chip_peaks({"tf":"NFIC","biosample":"HCT116"}): E36 reports no ENCODE NFIC ChIP-seq peak containing chr8:127401265:T>C in HCT116; one NFIC peak containing the variant is reported in HepG2. The absence has the caveat that it could also reflect no NFIC experiment in HCT116, so it weakens M3.binding rather than formally disproving NFIC occupancy there. (as expected: yes)
- Result of qbic_tf_detail({"tf":"TCF7L2"}): E37 reports 3 TCF7L2-group models, but only the CIS-BP-mapped TCF7 model passes the gate (z=-8.8, effect=-0.429, ref>alt; site strength ref 90.0th/alt 87.2th percentile, weak). The other models do not pass. This confirms coverage is through a mapped related-family model rather than a TCF7L2 own model and supports keeping M1.binding weak. (as expected: yes)

Chains after revision: null 0.56; TCF7L2 0.18; NFIC 0.14; SP1 0.12. Link grades changed: M3.cell_type: supported → weak.

### Round 2

- qbic_tf_detail({"tf": "SP1"}) for M2.binding, ran as [E38](#e38). Expected: If an SP1 own model (not only the mapped SP3 model) passes the QBiC-SELEX gate with ref>alt and a strong site, M2.binding becomes better supported and M2 rises. If only the mapped SP3 weak-site model is present, or the direction/gate fails, M2.binding stays weak and M2 falls.
- chip_peaks({"tf": "NFIA", "biosample": "HCT116"}) for M3.cell_type, ran as [E39](#e39). Expected: If an NFIA ChIP-seq peak contains the variant in HCT116, SMAD-family occupancy in the relevant cell line is supported and M3.cell_type rises, although NFIC versus NFIA identity would remain unresolved. If no NFIA peak is found, M3.cell_type stays weak and M3 falls.
- gene_disease({"gene": "POU5F1B"}) for M3.phenotype, ran as [E40](#e40). Expected: If POU5F1B has a colorectal cancer association in Open Targets, the M3 phenotype/gene relevance rises. If POU5F1B lacks CRC association, M3.phenotype stays weak and M3 falls relative to M1 and the null.

- Result of qbic_tf_detail({"tf":"SP1"}) for M2.binding: E38: SP1 has 5 models. The SP1 own model does not pass the QBiC-SELEX gate (z=-0.11, effect=-0.007). Only CIS-BP-mapped SP3 (z=-7.07, effect=-0.298, ref>alt) and SP9 (z=-6.42, effect=-0.485, ref>alt) pass; both have weak k-mer sites, not strong sites. This matches the branch where M2.binding remains weak because the own SP1 model fails and only mapped weak-site models pass. M2 falls slightly. (as expected: yes)
- Result of chip_peaks({"tf":"NFIA","biosample":"HCT116"}) for M3.cell_type: E39: no NFIA ENCODE ChIP-seq peak contains the variant in HCT116. The only NFIA peak over the variant is in HepG2. This matches the expected negative result: SMAD-family HCT116 occupancy is not supported, and NFIC versus NFIA identity remains unresolved. M3.cell_type stays weak and M3 falls relative to the null, though E40 partially offsets this at the gene/phenotype level. (as expected: yes)
- Result of gene_disease({"gene":"POU5F1B"}) for M3.phenotype: E40: Open Targets reports POU5F1B and colorectal cancer overall score 0.54, with genetic_association 0.87, literature 0.18, and rna_expression 0.14. This matches the expected positive gene-level CRC association and modestly raises M3.gene/M3.phenotype relevance. It does not show that this variant mediates POU5F1B regulation or that NFIC is the effector. (as expected: yes)

Chains after revision: null 0.57; NFIC 0.18; TCF7L2 0.15; SP1 0.10. Link grades changed: M2.binding: weak → missing.

### Round 3

- qbic_tf_detail({"tf": "NFIC"}) for M3.binding, ran as [E41](#e41). Expected: If NFIC has its own QBiC-SELEX model that passes the gate with alt C binding more, the NFIC-specific allelic effect is supported beyond the mapped NFIB model; if NFIC is covered only through the mapped NFIB model, or its own model does not pass, the NFIC binding claim stays weak and ambiguous with NFIA.
- gene_dependency({"gene": "POU5F1B"}) for M3.gene, ran as [E42](#e42). Expected: If POU5F1B knockout shows a selective dependency in colorectal cancer lineages, the POU5F1B target-gene link and M3 phenotype become more plausible; if POU5F1B is not measured, not dependent, or commonly essential, M3.gene/M3.phenotype remain weak or fall.
- literature_search({"query": "NFIC POU5F1B colorectal cancer"}) for M3.gene, ran as [E43](#e43). Expected: If the literature directly reports NFIC regulating POU5F1B in colorectal cancer, M3.gene and M3.phenotype rise; if hits are only generic POU5F1B cancer literature or unrelated, those links remain weak and the null retains more weight.

- Result of qbic_tf_detail(NFIC): E41 shows NFIC has its own QBiC-SELEX model that passes the gate with a strong alt>C effect: NFIC_FL model z=23.35, effect=+1.226, strong site; mapped NFIB model z=24.28, effect=+1.783. This supports an NFIC-specific in vitro allelic preference but does not provide HCT116 occupancy over the variant, and NFIA remains indistinguishable because it shares the mapped NFIB model with identical statistics (E23). (as expected: yes)
- Result of gene_dependency(POU5F1B): E42 shows POU5F1B is not a dependency in HCT116: CRISPR gene effect -0.09; bowel lineage median -0.06 with 0% dependent; all lines median -0.05 and only 3% dependent. This weakens the POU5F1B target-gene and phenotype links for M3, as expected if the gene is not a selective dependency in colorectal lineages. (as expected: yes)
- Result of literature_search('NFIC POU5F1B colorectal cancer'): E43 returns only 2 hits, neither directly reporting NFIC regulation of POU5F1B in colorectal cancer: one on calorie restriction and epigenetic ageing, one on PD-1/PD-L1 biomarkers. This leaves M3.gene and M3.phenotype weak. (as expected: yes)

Chains after revision: null 0.66; TCF7L2 0.17; NFIC 0.12; SP1 0.05. Link grades changed: M2.binding: missing → weak.

## Flags

- quote_rejected: PMID 42465001: not an exact substring of the abstract

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/8:127401265-127401265:1/C?content-type=application/json&Conservation=1; retrieved 2026-10-26T02:21:56+00:00)

> Variant chr8:127401265:T>C (GRCh38), allele string T/C
> Known IDs: rs73706717
> Most severe consequence: non_coding_transcript_exon_variant
> Regulatory features: ENSR8_CGMBX enhancer
> GERP conservation score at the site: -2.8
> Transcript consequences: CASC8 (intron_variant, non_coding_transcript_variant); CCAT2 (non_coding_transcript_exon_variant); PCAT1 (intron_variant, non_coding_transcript_variant); POU5F1B (intron_variant); PCAT1 (downstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/8:126401265-128401265?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-26T02:21:59+00:00)

> 3 protein-coding genes within 1000 kb of chr8:127401265:T>C, by distance to TSS:
> POU5F1B: 79.1 kb from TSS (in gene body, strand +1)
> MYC: 334.2 kb from TSS (upstream, strand +1)
> LRATD2: 842.8 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-26T02:21:42+00:00)

> The variant lies in cCRE EH38E3858447 (pELS: proximal enhancer-like), chr8:127401053-127401303.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3858447 pELS (contains the variant): DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 4.1; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858448 pELS: DNase z 5.2, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 2.2; nearby genes CCAT2, PCAT1, POU5F1B
> EH38E3858446 pELS: DNase z 4.9, H3K27ac z 4.8, H3K4me3 z 1.5, CTCF z 5.5; nearby genes CCAT2, PCAT1, POU5F1B
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:127401265:T>C: 149 peaks contain the variant, from 83 factors in 25 biosamples. In the matching biosample HCT116: 3 peaks from 3 factors. cCRE class at the variant: pELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, CHD4, EP300, HDAC1, HDAC2, HMGXB4, KDM1A, KDM6A, LCORL, LIN54, MED1, MED13 (+26 more). Bound, expressed TFs with a binding model: 40; listed one per row: TCF7L2, SP1, CTCF, CEBPB, MYBL2, NR2C2, TFAP4, ISL2, NR2F2, ERF; also bound: NR2F6, NFIC, ELF1, ZNF317, NFIL3, ZBTB7B, KLF16, PITX1, JUNB, SKI, CREM, RXRB, ATF2, ZNF609, ZNF280D, ZNF12, AHDC1, ZNF652, PHF21A, ETS1, NFIA, NR3C1, BCL6, PRDM10, HOXA3, HNF4A, MNX1, HNF1B, ZNF362, FOXA1. Bound but below 1 TPM: FOXA2, HNF1A, ONECUT1, SOX6, TBX2. Assayed with no peak here: 11 TFs in the matching biosample, 517 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000EUV). 63.61 TPM in DepMap:ACH-000971 (HCT 116), rank 53 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 2 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000BSF). 38.96 TPM in DepMap:ACH-000971 (HCT 116), rank 118 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 34 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, C4-2B, Panc1, RWPE2, adrenal gland, astrocyte (+13 more) (e.g. ENCSR173IEA). 50.0 TPM in DepMap:ACH-000971 (HCT 116), rank 78 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BQI). 13.15 TPM in DepMap:ACH-000971 (HCT 116), rank 408 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 67.51 TPM in DepMap:ACH-000971 (HCT 116), rank 46 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR559ZKI). 22.6 TPM in DepMap:ACH-000971 (HCT 116), rank 244 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TFAP4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR587BVQ). 19.72 TPM in DepMap:ACH-000971 (HCT 116), rank 283 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ISL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR492IHH). 2.77 TPM in DepMap:ACH-000971 (HCT 116), rank 862 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2F2: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR000BVM). 61.74 TPM in DepMap:ACH-000971 (HCT 116), rank 58 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ERF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR159DQO). 46.58 TPM in DepMap:ACH-000971 (HCT 116), rank 90 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs73706717&size=100; retrieved 2026-10-26T02:21:56+00:00)

> 0 GWAS Catalog associations for rs73706717, strongest first:

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:21:56+00:00)

> 2 credible sets contain 8_127401265_T_C: 2 GWAS, 0 molecular QTL.
> GWAS prostate-specific antigen (PSA, maximum, inv-norm transforme: PIP 0.04; L2G POU5F1B 0.83
> GWAS Urinary incontinence (PheCode 599.4): PIP 0.04; L2G POU5F1B 0.78
> Best L2G gene scores across these sets: POU5F1B 0.83

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e18"></a>**E18** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=POU5F1B%20AND%20%22colorectal%20cancer%22&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T02:21:59+00:00)

> Europe PMC: 150 hits for 'POU5F1B AND "colorectal cancer"'; top 8 with PMIDs:
> PMID 42465001 (2026): Circ_0075829 affects POU5F1B expression through sponging miR-576-3p to promote growth, invasion, and angiogenesis of colon cancer cells.
> PMID 41993623 (2026): Tailorable porous collagen hydrogels as a physiologically relevant platform for extrachromosomal DNA-associated colorectal cancer research.
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 41930642 (2026): Systematic Identification and Characterization of Causal Risk Genes Implicated in Colorectal Cancer by Integrating GWAS, eQTL, and mQTL Data.
> PMID 42686757 (2026): Phase separation of ecDNA condensates establishes in-trans contact domains that boost selective MYC regulatory interactions.
> PMID 40506516 (2025): Association between methylation quantitative trait loci and colorectal cancer risk, survival and cancer recurrence.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 41196428 (2025): Combined CHK1 and PD-L1 blockade as a novel therapeutic strategy against stemness and immunosuppression in ovarian cancer.

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr8:127401265:T>C, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 40 occupied (6 with a strong site), 5 of 103 with unknown occupancy. Left out: 11 TFs assayed in the matching biosample and 517 assayed only elsewhere, none with a peak here; 5 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer (a CIS-BP-mapped model of TCF7), z -8.8, effect -0.429: ref allele binds more (|z| above the gate), but between weak k-mers. 63.61 TPM, rank 53 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000EUV. Best model's site strength: ref 90.0th, alt 87.2th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): best model SP3_eDBD_TTCACC40NGCT_KR_yin2017_0_3_7mer (a CIS-BP-mapped model of SP3), z -7.07, effect -0.298: ref allele binds more (|z| above the gate), but between weak k-mers. 38.96 TPM, rank 118 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSF. Best model's site strength: ref 90.4th, alt 75.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NFIC (SMAD, 4 models; QBiC-SELEX coverage: own model): best model NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer (a CIS-BP-mapped model of NFIB), z 24.28, effect 1.783: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 36.29 TPM, rank 137 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BQX. Best model's site strength: ref 96.3th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NFIA (SMAD, 4 models; QBiC-SELEX coverage: own model): best model NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer (a CIS-BP-mapped model of NFIB), z 24.28, effect 1.783: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.07 TPM, rank 616 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR226QQM. Best model's site strength: ref 96.3th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF1B (Homeodomain, 3 models; QBiC-SELEX coverage: own model): best model HMBOX1_eDBD_TGGCTC40NCGC_KAN_yin2017_1_2_7mer (a CIS-BP-mapped model of HMBOX1), z -23.93, effect -0.32: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.08 TPM, rank 929 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR127XTZ. Best model's site strength: ref 100.0th, alt 67.8th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z 8.21, effect 0.902: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 50.0 TPM, rank 78 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, C4-2B, Panc1, RWPE2, adrenal gland (+14 more), e.g. ENCSR173IEA. Best model's site strength: ref 98.8th, alt 99.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPB (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (its own model), z -6.94, effect -0.844: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 13.15 TPM, rank 408 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BQI. Best model's site strength: ref 98.2th, alt 73.1th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP4 (bHLH, 1 model; QBiC-SELEX coverage: own model): best model TFAP4_NA_TCACGT20NGCA_ESAC_yang2017_0_3_7mer (its own model), z 0.51, effect 0.042: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 19.72 TPM, rank 283 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR587BVQ. Best model's site strength: ref 98.2th, alt 96.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (a CIS-BP-mapped model of NR1H3), z -15.02, effect -0.286: ref allele binds more (|z| above the gate), but between weak k-mers. 61.74 TPM, rank 58 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BVM. Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F6 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (a CIS-BP-mapped model of NR1H3), z -15.02, effect -0.286: ref allele binds more (|z| above the gate), but between weak k-mers. 37.02 TPM, rank 133 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR798IJO. Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB22 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB22_eDBD_TGCCTC40NCAA_KP_yin2017_0_4_7mer (its own model), z -33.75, effect -1.962: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.74 TPM, rank 794 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.8th, alt 92.4th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1H3 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR1H3_DBD_TGAGCG40NTTG_KY_nitta2015_2_3_7mer (its own model), z -15.02, effect -0.286: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 11.39 TPM, rank 459 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 95.9th, alt 60.2th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TET3 (CxxC, 2 models; QBiC-SELEX coverage: own model): best model CXXC4_FL_GG40NTAGTTT_YWKC_jolma2025_0_4_7mer (a CIS-BP-mapped model of CXXC4), z 14.12, effect 0.794: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 10.17 TPM, rank 497 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 87.7th, alt 96.6th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1D2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2C1_eDBD_TATTCA40NAGT_KT_yin2017_0_3_7mer (a CIS-BP-mapped model of NR2C1), z -13.82, effect -0.705: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 37.06 TPM, rank 132 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.3th, alt 92.0th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR4A2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2C1_eDBD_TATTCA40NAGT_KT_yin2017_0_3_7mer (a CIS-BP-mapped model of NR2C1), z -13.82, effect -0.705: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 7.19 TPM, rank 611 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.3th, alt 92.0th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401265_T_C_b38&datasetId=gtex_v8; retrieved 2026-10-26T02:23:32+00:00)

> 0 significant GTEx v8 single-tissue eQTLs for chr8_127401265_T_C_b38 in tissues matching 'Colon'. NES is the effect of the alt allele (C) relative to ref (T).

<a id="e36"></a>**E36** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T13:23:02+00:00)

> No ENCODE NFIC ChIP-seq peak contains chr8:127401265:T>C in biosamples matching 'HCT116'. Absence can also mean no NFIC experiment in that biosample. In other biosamples, 1 NFIC peaks do contain the variant: HepG2 (experiments ENCSR000BQX).

<a id="e37"></a>**E37** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401265:T>C","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.306,"z":-2.77,"p":0.0056,"rank_abs_z":"461/997","passed_gate":false,"site_strength":{"ref_percentile":81.3,"alt_percentile":95.3,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.429,"z":-8.8,"p":1.4e-18,"rank_abs_z":"66/997","passed_gate":true,"site_strength":{"ref_percentile":90.0,"alt_percentile":87.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.242,"z":-3.57,"p":0.00036,"rank_abs_z":"359/997","passed_gate":false,"site_strength":{"ref_percentile":84.6,"alt_percentile":58.3,"k":7}}]}

<a id="e38"></a>**E38** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"SP1","symbol":"SP1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr8:127401265:T>C","gate_p":5.02e-05,"models":[{"model":"SP1_eDBD_TCTCTA40NCAC_KV_yin2017_0_3_7mer","mapping":"own","group":"G015 C2H2 ZF, 5 models","quality":0.891,"effect":-0.007,"z":-0.11,"p":0.91,"rank_abs_z":"975/997","passed_gate":false,"site_strength":{"ref_percentile":97.2,"alt_percentile":97.4,"k":7}},{"model":"SP3_eDBD_TTCACC40NGCT_KR_yin2017_0_3_7mer","mapping":"CIS-BP (SP3)","group":"G015 C2H2 ZF, 5 models","quality":0.813,"effect":-0.298,"z":-7.07,"p":1.5e-12,"rank_abs_z":"117/997","passed_gate":true,"site_strength":{"ref_percentile":90.4,"alt_percentile":75.6,"k":7}},{"model":"SP4_NA_TTATGT20NGTA_ESAE_yang2017_0_3_7mer","mapping":"CIS-BP (SP4)","group":"G015 C2H2 ZF, 5 models","quality":0.825,"effect":-0.111,"z":-2.06,"p":0.04,"rank_abs_z":"566/997","passed_gate":false,"site_strength":{"ref_percentile":65.1,"alt_percentile":79.1,"k":7}},{"model":"SP8_NA_TGCTCG20NCTC_ESY_yang2017_0_4_7mer","mapping":"CIS-BP (SP8)","group":"G015 C2H2 ZF, 5 models","quality":0.672,"effect":-0.048,"z":-0.66,"p":0.51,"rank_abs_z":"848/997","passed_gate":false,"site_strength":{"ref_percentile":88.7,"alt_percentile":84.7,"k":7}},{"model":"SP9_eDBD_TACCGA40NATA_KP_yin2017_0_4_7mer","mapping":"CIS-BP (SP9)","group":"G015 C2H2 ZF, 5 models","quality":0.936,"effect":-0.485,"z":-6.42,"p":1.3e-10,"rank_abs_z":"143/997","passed_gate":true,"site_strength":{"ref_percentile":70.8,"alt_percentile":67.5,"k":7}}]}

<a id="e39"></a>**E39** chip_peaks, Factorbook (ENCODE TF ChIP-seq peaks) (https://factorbook.api.wenglab.org/graphql; retrieved 2026-10-26T22:09:49+00:00)

> No ENCODE NFIA ChIP-seq peak contains chr8:127401265:T>C in biosamples matching 'HCT116'. Absence can also mean no NFIA experiment in that biosample. In other biosamples, 1 NFIA peaks do contain the variant: HepG2 (experiments ENCSR226QQM).

<a id="e40"></a>**E40** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14

<a id="e41"></a>**E41** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"NFIC","symbol":"NFIC","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr8:127401265:T>C","gate_p":5.02e-05,"models":[{"model":"NFIC_FL_TATGGA40NAGA_KX_yin2017_1_3_7mer","mapping":"own","group":"G027 SMAD, 4 models","quality":0.832,"effect":1.226,"z":23.35,"p":1.5e-120,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":93.8,"alt_percentile":97.8,"k":7}},{"model":"NFIA_NA_TACGTC20NTGC_ESAA_yang2017_0_2_7mer","mapping":"CIS-BP (NFIA)","group":"G027 SMAD, 4 models","quality":0.778,"effect":0.414,"z":11.49,"p":1.4e-30,"rank_abs_z":"36/997","passed_gate":true,"site_strength":{"ref_percentile":93.2,"alt_percentile":99.5,"k":7}},{"model":"NFIB_NA_TCATCA20NCG_ESAD_yang2017_0_3_7mer","mapping":"CIS-BP (NFIB)","group":"G027 SMAD, 4 models","quality":0.873,"effect":1.783,"z":24.28,"p":3.6e-130,"rank_abs_z":"4/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":99.5,"k":7}},{"model":"NFIX_FL_TTGAGC40NGTC_KAE_yin2017_1_3_7mer","mapping":"CIS-BP (NFIX)","group":"G027 SMAD, 4 models","quality":0.881,"effect":1.633,"z":23.96,"p":6.6e-127,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":91.7,"alt_percentile":98.8,"k":7}}]}

<a id="e42"></a>**E42** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for POU5F1B (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): -0.09. Bowel lineage, 31 lines: median -0.06, 0% dependent. All 351 lines: median -0.05, 3% dependent.

<a id="e43"></a>**E43** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=NFIC%20POU5F1B%20colorectal%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-26T22:11:39+00:00)

> Europe PMC: 2 hits for 'NFIC POU5F1B colorectal cancer'; top 2 with PMIDs:
> PMID 41432313 (2026): Graded Calorie Restriction Causes Graded Slowing of Epigenetic Ageing in Mice.
> PMID 37345033 (2023): Development and Validation of Blood-Based Predictive Biomarkers for Response to PD-1/PD-L1 Checkpoint Inhibitors: Evidence of a Universal Systemic Core of 3D Immunogenetic Profiling across Multiple Oncological Indications.
