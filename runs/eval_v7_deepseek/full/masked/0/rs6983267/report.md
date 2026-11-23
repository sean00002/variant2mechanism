# rs6983267 and Colorectal cancer (8q24)

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.11 over 26 model calls; 542 s.

Variant `chr8:127401060:G>T` (germline); expression context: DepMap:ACH-000971 (HCT 116).

**Verdict: undetermined.** The null leads, but nothing tested counts against TCF7L2, NR2F2, SP1.

Association with the disease (not part of the verdict): GWAS Catalog found; Open Targets fine-mapping found.

Pairwise ranking (Bradley-Terry strengths): H1_TCF7L2_derepression 0.46, H5_NR2F2_alt_binding_POU5F1B 0.26, H3_SP1_ref_binding 0.15, H0_null_no_TF_effect 0.13. 1 of 6 pairs came out differently in the two orders.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: TCF7L2 (bound here, z -4.66); SRF (bound here, z -7.74, weak site); SP1 (bound here, z -4.76, weak site); JUND (bound here, z -3.01, no clear allelic change, weak site); CEBPB (bound here, z 1.9, no clear allelic change, weak site); MAX (bound here, z -0.97, no clear allelic change, weak site); YY1 (bound here, z -0.43, no clear allelic change, weak site); HNF4A (bound elsewhere, z 53.69); GFI1 (bound elsewhere, z -31.27); NR2F2 (bound elsewhere, z 20.82). Occupancy unknown: ZNF493 (z -34.16); TBX19 (z 26.18); MBNL2 (z -22.42); NR1D1 (z 20.82); NR1D2 (z 20.82). Diagnostic, not shown to the model: 421 of 997 models pass Bonferroni.

## Ranked chains

### 1. H0_null_no_TF_effect: No TF-mediated effect of this variant; linked or non-TF mechanism (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at this exact base after controlling for linked variants.; The GWAS signal is explained by a linked causal variant, CTCF/insulator effects, or a non-TF mechanism.; Changing the G>T base alone does not alter enhancer activity in colorectal cells.

Falsified if: A linked causal variant is excluded and allele-specific TF occupancy at this exact base is demonstrated.; A specific TF is shown to bind allele-selectively and to regulate POU5F1B, CASC8, or another target in colorectal cells.; The G>T base alone changes enhancer activity in colorectal cells.

### 2. H1_TCF7L2_derepression: Alt T reduces TCF7L2 binding and derepresses POU5F1B (p = 0.30)

TF TCF7L2 (QBiC-SELEX coverage mapped), ref allele binds more; element active pELS enhancer EH38E3858447; gene POU5F1B; cell type HCT116 colorectal carcinoma and colon transverse expression context.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TCF7L2 is expressed in HCT116 (63.61 TPM; E05), has an ENCODE ChIP-seq peak over the variant in HCT116 (E05), and QBiC-SELEX HMG/Sox models detect allele-specific binding with ref G binding more strongly than alt T (best LEF1-mapped model effect -0.47, z -4.66; E20/E35). E43 shows LEF1 has the same own model and comparable effect, so the motif is HMG/Sox but TCF7L2-specific attribution remains ambiguous. | weak | [E05](#e05), [E20](#e20), [E35](#e35), [E43](#e43) |
| element | The variant lies in EH38E3858447, a proximal enhancer-like cCRE with DNase, H3K27ac and CTCF signal, and VEP annotates an enhancer at the site. The chromatin z-scores are maxima over ENCODE biosamples, so HCT116-specific activity is inferred rather than directly shown. | weak | [E01](#e01), [E03](#e03) |
| gene | This chain uses POU5F1B as the target because the colon-transverse eQTL shows alt T associated with higher POU5F1B (NES +0.20; E17/E38) and POU5F1B has the best L2G score at the locus (0.89; E16). The mechanism requires TCF7L2 to repress POU5F1B, so that loss of TCF7L2 binding on alt T derepresses POU5F1B. E41 found only co-mentions of TCF7L2 and colorectal cancer/Wnt signaling, not a direct TCF7L2-POU5F1B regulatory report or perturbation; the repressor step remains an assumption. | weak | [E16](#e16), [E17](#e17), [E38](#e38), [E41](#e41) |
| cell_type | TCF7L2 occupancy over the variant is shown in the matching HCT116 biosample (E05), and the POU5F1B eQTL is significant in colon transverse (E38). The occupancy and colon expression contexts align, but no HCT116 POU5F1B perturbation or allele-specific reporter is cited. | weak | [E05](#e05), [E38](#e38) |
| phenotype | The T allele is the strongest colorectal cancer risk allele at this locus (p 2.0e-122; E15), and POU5F1B has the best L2G score (E16) with substantial Open Targets colorectal-cancer association (overall 0.54, genetic_association 0.87; E42). However, POU5F1B is not a CRISPR dependency in HCT116 or bowel lineage (E37), and E15 reports G as the effect allele for several other colorectal/colon traits, so phenotype mediation remains unproven and direction is not uniform across trait definitions. | weak | [E15](#e15), [E16](#e16), [E37](#e37), [E42](#e42) |

Predictions: Allele-specific TCF7L2 ChIP or EMSA shows stronger TCF7L2 binding on ref G than alt T at this base.; TCF7L2 depletion in HCT116 increases POU5F1B, mimicking loss of TCF7L2 binding on alt T.; An enhancer reporter shows alt T increases POU5F1B-linked activity, and mutation of the TCF7L2 site mimics alt T.

Falsified if: Allele-specific TCF7L2 ChIP or EMSA shows no difference between ref G and alt T at this exact base.; TCF7L2 depletion in HCT116 does not increase POU5F1B or does not mimic the alt T allele.; An MPRA/reporter shows no alt-T-dependent enhancer change or shows that mutation of the TCF7L2 site does not alter the allelic effect.

### 3. H5_NR2F2_alt_binding_POU5F1B: Alt T increases NR2F2 binding and may activate POU5F1B (p = 0.10)

TF NR2F2 (QBiC-SELEX coverage own_model), alt allele binds more; element active pELS enhancer EH38E3858447; gene POU5F1B; cell type HCT116 colorectal carcinoma expression context, but no HCT116 NR2F2 occupancy.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | NR2F2 is expressed in HCT116 (61.74 TPM; E29) and its QBiC-SELEX nuclear-receptor model detects stronger alt T binding: effect 1.92, z 20.82, with a strong site (E29). However, E36 shows ENCODE has no NR2F2 ChIP-seq in HCT116 and ReMap has only a HepG2 peak, so HCT116 occupancy is not tested. This is a strong in vitro binding prediction without case-cell-type occupancy evidence. | weak | [E29](#e29), [E36](#e36) |
| element | The variant lies in the active pELS enhancer EH38E3858447. The active-mark z-scores are maxima over ENCODE biosamples, so HCT116-specific enhancer activity is inferred rather than directly measured. | weak | [E01](#e01), [E03](#e03) |
| gene | If NR2F2 activates POU5F1B, stronger alt T binding would increase POU5F1B, matching the colon-transverse POU5F1B eQTL (alt T NES +0.20; E17/E38), the POU5F1B L2G score (E16) and POU5F1B colorectal-cancer association (E42). The activator role and the NR2F2-POU5F1B regulatory link are not demonstrated. | weak | [E16](#e16), [E17](#e17), [E38](#e38), [E42](#e42) |
| cell_type | NR2F2 is expressed in HCT116, but there is no HCT116 NR2F2 ChIP-seq; E36 is explicitly not tested in HCT116. The POU5F1B eQTL is in colon transverse, so the cell-type link is incomplete and rests on expression plus a colon eQTL. | weak | [E29](#e29), [E36](#e36), [E38](#e38) |
| phenotype | The T allele is the colorectal cancer risk allele at this locus (E15), and POU5F1B has the best L2G score (E16) and substantial Open Targets colorectal-cancer association (E42). However, POU5F1B is not a CRISPR dependency in HCT116 or bowel lineage (E37), and NR2F2 causality at this locus is not established. | weak | [E15](#e15), [E16](#e16), [E37](#e37), [E42](#e42) |

Predictions: Allele-specific NR2F2 ChIP or EMSA shows stronger NR2F2 binding on alt T than ref G.; NR2F2 depletion in HCT116 reduces POU5F1B and opposes the alt T effect.; An enhancer reporter shows alt T increases activity through an NR2F2 site, not a TCF7L2 site.

Falsified if: Allele-specific NR2F2 binding in HCT116 shows no difference or shows ref > alt.; NR2F2 depletion does not reduce POU5F1B or does not mimic the alt T allele.; NR2F2 is not expressed or not able to regulate POU5F1B in colorectal cells.

### 4. H3_SP1_ref_binding: Ref G binds SP1 more; alt T may lower CASC8 if SP1 activates it (p = 0.05)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element active pELS enhancer EH38E3858447; gene CASC8; cell type HCT116 colorectal carcinoma, with weak-site caveat.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SP1 is expressed in HCT116 (38.96 TPM; E06) and has ENCODE ChIP-seq occupancy over the variant in HCT116 (E06). Its QBiC-SELEX SP4-mapped model detects a change with ref G binding more than alt T (effect -0.211, z -4.76; E22), but the site is weak at both alleles, so the evidence itself states the ChIP peak more likely reflects another site in the element. | weak | [E06](#e06), [E22](#e22) |
| element | The variant is in the active pELS enhancer EH38E3858447. The active-mark z-scores are maxima over ENCODE biosamples, so activity in HCT116 is inferred rather than directly measured. | weak | [E01](#e01), [E03](#e03) |
| gene | If SP1 activates CASC8, loss of SP1 binding on alt T would lower CASC8, matching the whole-blood CASC8 eQTL (alt T NES -0.32; E17). However, E38 reports no colon CASC8 eQTL, no SP1-CASC8 perturbation is cited, and CASC8 has only weak Open Targets colorectal-cancer evidence (overall 0.02; E40). | weak | [E17](#e17), [E38](#e38), [E40](#e40) |
| cell_type | SP1 occupancy over the variant is shown in HCT116 (E06), but the CASC8 eQTL is from whole blood (E17), not colon, and E38 finds no CASC8 colon-transverse eQTL. The cell-type support for the gene link is incomplete. | weak | [E06](#e06), [E17](#e17), [E38](#e38) |
| phenotype | The T allele is associated with colorectal cancer (E15), but CASC8 has only weak Open Targets colorectal-cancer evidence (overall score 0.02; E40). The phenotype link is therefore weak and not causal. | weak | [E15](#e15), [E40](#e40) |

Predictions: Allele-specific SP1 ChIP or EMSA shows stronger SP1 binding on ref G than alt T.; SP1 depletion lowers CASC8 if SP1 activates CASC8 at this element.; The alt T allele lowers enhancer activity only when the SP1 site is intact.

Falsified if: Allele-specific SP1 ChIP or EMSA shows no difference between ref G and alt T at this base.; SP1 depletion does not change CASC8 or enhancer activity.; SP1 is not an activator at this element, removing the direction match for alt T lowering CASC8.

## Prediction matrix

| Test | Cost | Separates top two | H0_null_no_TF_effect | H1_TCF7L2_derepression | H5_NR2F2_alt_binding_POU5F1B | H3_SP1_ref_binding |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TCF7L2 EMSA with ref-G and alt-T oligos spanning chr8:127401060 | low | yes | no allele-specific TF binding at this exact base | ref G > alt T TCF7L2 binding | no TCF7L2-specific allelic difference | no TCF7L2-specific allelic difference |
| Allele-specific NR2F2 EMSA or ChIP-qPCR at chr8:127401060 in HCT116 | low | no | no allele-specific TF binding at this exact base | no NR2F2-specific allelic difference | alt T > ref G NR2F2 binding | no NR2F2-specific allelic difference |
| TCF7L2 knockdown/knockout in HCT116 followed by POU5F1B expression | medium | yes | no TCF7L2-dependent POU5F1B change | TCF7L2 depletion increases POU5F1B | TCF7L2 depletion does not increase POU5F1B | TCF7L2 depletion does not increase POU5F1B |
| Enhancer reporter/MPRA with ref vs alt and TCF7L2-site mutation in colorectal cells | medium | yes | no allele-specific enhancer activity | alt T increases activity; mutating the TCF7L2 site mimics alt T | alt T increases activity through an NR2F2 site | alt T decreases activity if SP1 activates CASC8 |
| NR2F2 knockdown/knockout in HCT116 followed by POU5F1B expression | medium | no | no NR2F2-dependent POU5F1B change | NR2F2 depletion does not change POU5F1B | NR2F2 depletion reduces POU5F1B | NR2F2 depletion does not change POU5F1B |
| SP1 knockdown/knockout in HCT116 followed by CASC8 expression or enhancer activity | medium | no | no SP1-dependent CASC8 change | SP1 depletion does not change CASC8 | SP1 depletion does not change CASC8 | SP1 depletion lowers CASC8/enhancer activity |

## Next experiment

Allele-specific TCF7L2 EMSA with ref-G and alt-T oligos spanning chr8:127401060 is the cheapest single test that separates the top two chains. H1 predicts ref G > alt T TCF7L2 binding; the null predicts no allele-specific TF binding at this exact base. This tests binding only, not chromatin occupancy or POU5F1B regulation, so a positive result would support H1.binding but would not by itself prove the full derepression mechanism.

## Refinement rounds

Stopped: round limit (3).

### Round 1

- qbic_tf_detail({"tf": "TCF7L2"}) for H1.binding, ran as [E35](#e35). Expected: If QBiC-SELEX has a TCF7L2-specific model at this site with ref G binding more, H1.binding strengthens; if TCF7L2 is covered only by the LEF1 CIS-BP proxy and related HMG/Sox factors share the same allelic signal, H1.binding remains weak and H1's lead over H0 shrinks.
- chip_peaks({"tf": "NR2F2", "biosample": "HCT116"}) for H2.cell_type, ran as [E36](#e36) (not tested). Expected: If NR2F2 has an ENCODE ChIP-seq peak over the variant in HCT116, H2.cell_type become supported and H2 rises above H3; if there is no HCT116 peak, H2's own occupancy premise is falsified in the case cell type and weight shifts toward H1/H0.
- gene_dependency({"gene": "POU5F1B"}) for H1.phenotype (shared with H2/H3.phenotype), ran as [E37](#e37). Expected: If POU5F1B is a selective dependency in the colorectal lineage, the shared phenotype link for H1/H2/H3 gains support; if POU5F1B is not a selective dependency and is not common-essential, the phenotype step weakens across the non-null chains and H0 gains weight.

- Result of qbic_tf_detail({"tf":"TCF7L2"}) for H1.binding; result E35: E35 confirms TCF7L2 has QBiC-SELEX coverage only through CIS-BP-mapped HMG/Sox models: best LEF1-mapped model z -4.66, effect -0.47 (ref G binds more, strong site); TCF7-mapped model z -4.59, effect -0.229; TCF7L1-mapped model below gate. This is not a TCF7L2-specific model, so the allelic signal is shared-proxy evidence rather than direct TCF7L2 motif evidence. (as expected: yes)
- Result of chip_peaks({"tf":"NR2F2","biosample":"HCT116"}) for H2.cell_type; result E36: E36 finds no ENCODE NR2F2 ChIP-seq experiment in HCT116 and 0 ReMap HCT116 peaks; the only NR2F2 peak over the variant is in Hep-G2. The H2 occupancy premise in the case cell type is therefore unsupported and was dropped. (as expected: yes)
- Result of gene_dependency({"gene":"POU5F1B"}) for shared phenotype link; result E37: E37 finds POU5F1B is not a selective dependency in HCT116 (-0.09), bowel lineage median -0.06 with 0% dependent, and only 3% dependent across all lines. This weakens the POU5F1B phenotype step; it does not rule out a risk-gene role, but it does not support dependency-based causality. (as expected: yes)

Chains after revision: TCF7L2 0.45; null 0.39; SP1 0.08; SRF 0.08. Link grades changed: H1_TCF7L2_derepression.cell_type: supported → weak, H1_TCF7L2_derepression.element: weak → supported, H2_NR2F2_alt_binding.binding: weak → absent, H2_NR2F2_alt_binding.cell_type: weak → absent, H2_NR2F2_alt_binding.element: weak → absent, H2_NR2F2_alt_binding.gene: weak → absent, H2_NR2F2_alt_binding.phenotype: weak → absent, H3_SP1_ref_binding.cell_type: supported → weak, H3_SP1_ref_binding.element: weak → supported, H4_SRF_ref_binding.binding: absent → weak, H4_SRF_ref_binding.cell_type: absent → weak, H4_SRF_ref_binding.element: absent → supported, H4_SRF_ref_binding.gene: absent → weak, H4_SRF_ref_binding.phenotype: absent → weak.

### Round 2

- eqtl_lookup({"tissue": "Colon_Transverse"}) for H1_TCF7L2_derepression.gene, ran as [E38](#e38). Expected: E17 already reports only POU5F1B as a significant colon-transverse eQTL for this variant (NES +0.20, p 8.2e-06) and no CASC8 colon eQTL. I expect this tissue-specific lookup to confirm that pattern: POU5F1B significant, CASC8 not significant. If so, H1.gene and H1.cell_type remain weak because the CASC8 link is still whole-blood only, and the null/POU5F1B alternative gains relative to H1. If instead a CASC8 colon eQTL appears with alt T lower, H1.gene and H1.cell_type become supported and H1 rises.
- literature_search({"query": "TCF7L2 CASC8 colorectal cancer"}) for H1_TCF7L2_derepression.gene, ran as [E39](#e39). Expected: I expect few or no direct studies showing TCF7L2 perturbation changes CASC8 in colorectal cells; CASC8 is usually discussed as an 8q24 lncRNA rather than a demonstrated TCF7L2 target. If no direct TCF7L2-CASC8 regulatory evidence is found, H1.gene stays weak and H1 falls slightly relative to the null. If a direct TCF7L2-CASC8 regulatory study in colon cells is found, H1.gene becomes supported and H1 rises.
- gene_disease({"gene": "CASC8"}) for H1_TCF7L2_derepression.phenotype, ran as [E40](#e40). Expected: I expect Open Targets to show some 8q24 GWAS association for CASC8 but not strong mechanistic or perturbation evidence tying CASC8 to colorectal cancer. If CASC8 has a strong colorectal-cancer association across evidence types, H1.phenotype becomes better supported and H1 rises. If CASC8 has weak or absent colorectal-cancer association, H1.phenotype remains weak and the null gains relative weight.

- Result of eqtl_lookup({"tissue":"Colon_Transverse"}) for H1_TCF7L2_derepression.gene: E38 reports one significant GTEx v8 Colon_Transverse eQTL: POU5F1B NES +0.20, p 8.2e-06. No CASC8 colon-transverse eQTL is reported. This matches the expected pattern and supports POU5F1B, not CASC8, as the colon expression target. (as expected: yes)
- Result of literature_search({"query":"TCF7L2 CASC8 colorectal cancer"}) for H1_TCF7L2_derepression.gene: E39 returns 37 hits, mostly TCF7L2/CASC8/GREM1 association or review literature. No direct TCF7L2 perturbation-CASC8 regulatory study in colorectal cells is cited. E39a mentions TCF7L2 in Wnt/TCF signaling, but this does not establish CASC8 as its target. (as expected: yes)
- Result of gene_disease({"gene":"CASC8"}) for H1_TCF7L2_derepression.phenotype: E40 reports Open Targets CASC8-colorectal cancer overall score 0.02, with literature 0.17 and rna_expression 0.06. This is weak mechanistic/disease evidence for CASC8, as expected. (as expected: yes)

Chains after revision: TCF7L2 0.40; null 0.39; NR2F2 0.11; SP1 0.06; SRF 0.04. Link grades changed: H1_TCF7L2_derepression.binding: weak → supported, H5_NR2F2_alt_binding_POU5F1B.binding: absent → weak, H5_NR2F2_alt_binding_POU5F1B.cell_type: absent → weak, H5_NR2F2_alt_binding_POU5F1B.element: absent → supported, H5_NR2F2_alt_binding_POU5F1B.gene: absent → weak, H5_NR2F2_alt_binding_POU5F1B.phenotype: absent → weak.

### Round 3

- literature_search({"query": "TCF7L2 POU5F1B colorectal cancer"}) for H1.gene, ran as [E41](#e41). Expected: A direct report or perturbation showing TCF7L2 regulates POU5F1B in colorectal cells would support H1.gene; only co-mentions or no TCF7L2-POU5F1B link would leave H1.gene weak.
- gene_disease({"gene": "POU5F1B"}) for H1.phenotype, ran as [E42](#e42). Expected: If Open Targets gives substantial colorectal-cancer association evidence for POU5F1B, H1.phenotype and H5.phenotype strengthen; if evidence is weak or absent, H1.phenotype stays weak and the null gains weight.
- qbic_tf_detail({"tf": "LEF1"}) for H1.binding, ran as [E43](#e43). Expected: If LEF1 has its own or mapped QBiC-SELEX model with a comparable ref>alt effect, TCF7L2-specific attribution in H1.binding becomes more ambiguous; if LEF1 is not covered or shows a different effect, TCF7L2 remains the better-supported HMG/Sox candidate.

- Result of literature_search('TCF7L2 POU5F1B colorectal cancer') for H1.gene: E41 returned 37 hits; the top records and quotes co-mention TCF7L2 with colorectal cancer/Wnt signaling or CCAT2, but no direct TCF7L2-to-POU5F1B regulatory report or perturbation was found. This did not provide the direct link expected to strengthen H1.gene, so H1.gene remains an assumption built on consistent eQTL/L2G direction alone. (as expected: no)
- Result of gene_disease('POU5F1B') for H1.phenotype: E42 gives Open Targets POU5F1B-colorectal cancer overall score 0.54, with genetic_association 0.87, literature 0.18 and rna_expression 0.14. This substantially strengthens the POU5F1B disease-association part of the phenotype link, though it does not establish TCF7L2 mediation and does not overcome the negative CRISPR dependency data in E37. (as expected: yes)
- Result of qbic_tf_detail('LEF1') for H1.binding: E43 shows LEF1 has its own model, LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer, with the same effect -0.47 and z -4.66 as the LEF1-mapped model used for TCF7L2 in E20/E35, plus related TCF7 and TCF7L1 models. This confirms that the allele-specific QBiC-SELEX signal is an HMG/Sox motif effect but does not resolve TCF7L2-specific attribution. (as expected: yes)

Chains after revision: null 0.55; TCF7L2 0.30; NR2F2 0.10; SP1 0.05. Link grades changed: H1_TCF7L2_derepression.binding: supported → weak, H1_TCF7L2_derepression.element: supported → weak, H3_SP1_ref_binding.element: supported → weak, H4_SRF_ref_binding.binding: weak → absent, H4_SRF_ref_binding.cell_type: weak → absent, H4_SRF_ref_binding.element: supported → absent, H4_SRF_ref_binding.gene: weak → absent, H4_SRF_ref_binding.phenotype: weak → absent, H5_NR2F2_alt_binding_POU5F1B.element: supported → weak.

## Flags

- quote_rejected: PMID 42465001: not an exact substring of the abstract

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

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr8:127401060:G>T: 330 peaks contain the variant, from 116 factors in 64 biosamples. In the matching biosample HCT116: 10 peaks from 9 factors. cCRE class at the variant: pELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID5B, ASH2L, CHD4, EHMT2, EP300, HDAC1, HDAC2, HMGXB4, KAT8, KDM1A, KDM6A, LCOR (+34 more). Bound, expressed TFs with a binding model: 64; listed one per row: TCF7L2, SP1, YY1, MAX, SRF, JUND, CEBPB, CTCF, MYBL2, ERF; also bound: NR2F6, NR2F1, ELF1, NR2C2, KLF16, CREM, TFAP4, RXRB, ATF2, RXRA, ZNF609, AHDC1, ZNF652, NFIA, HNF4A, MNX1, HNF1B, ZNF362, FOXA1, HMG20B, NR2F2, KLF6, NFIC, ATF1, TEAD4, ETV5, ZNF317, NFIL3, THAP11, ZBTB7B (+24 more). Bound but below 1 TPM: FOXA2, HNF1A, MIXL1, ONECUT1, SOX6, TBX2. Assayed with no peak here: 6 TFs in the matching biosample, 497 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> TCF7L2: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2 (e.g. ENCSR000EUV). 63.61 TPM in DepMap:ACH-000971 (HCT 116), rank 53 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SP1: bound here. 4 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116; also in HepG2, liver (e.g. ENCSR000BSF). 38.96 TPM in DepMap:ACH-000971 (HCT 116), rank 118 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> YY1: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BNX). 84.45 TPM in DepMap:ACH-000971 (HCT 116), rank 34 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSH). 42.59 TPM in DepMap:ACH-000971 (HCT 116), rank 102 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> SRF: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSC). 25.61 TPM in DepMap:ACH-000971 (HCT 116), rank 217 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUND: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSA). 18.66 TPM in DepMap:ACH-000971 (HCT 116), rank 300 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CEBPB: bound here. 1 ENCODE ChIP-seq peak(s) contain the variant, in the matching biosample HCT116 (e.g. ENCSR000BSD). 13.15 TPM in DepMap:ACH-000971 (HCT 116), rank 408 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 150 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: 22Rv1, A549, A673, B cell, C4-2B, CD14-positive monocyte (+53 more) (e.g. ENCSR072EUE). 50.0 TPM in DepMap:ACH-000971 (HCT 116), rank 78 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MYBL2: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR581KCO). 67.51 TPM in DepMap:ACH-000971 (HCT 116), rank 46 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ERF: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR159DQO). 46.58 TPM in DepMap:ACH-000971 (HCT 116), rank 90 of 1626 TFs.

<a id="e15"></a>**E15** gwas_lookup, GWAS Catalog REST v2 (https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs6983267&size=100; retrieved 2026-10-25T16:33:55+00:00)

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

<a id="e16"></a>**E16** finemap_lookup, Open Targets Platform (credible sets, L2G) (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-25T16:33:46+00:00)

> 92 credible sets contain 8_127401060_G_T: 91 GWAS, 1 molecular QTL.
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Cancer of prostate (PheCode 185): PIP 1.00; L2G POU5F1B 0.82
> GWAS Elevated prostate specific antigen [PSA] (PheCode 796): PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> GWAS Prostate cancer: PIP 1.00; L2G POU5F1B 0.82
> sceqtl for PVT1 (OTAR2057_IBDverse_ge_Colon_Goblet_MUC2+_SPDEF+_ENS): PIP 0.95
> Best L2G gene scores across these sets: POU5F1B 0.89, MYC 0.05

<a id="e17"></a>**E17** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 2 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38. NES is the effect of the alt allele (T) relative to ref (G).
> CASC8 in Whole_Blood: NES -0.32, p 6.3e-10
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

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

> QBiC-SELEX screen of chr8:127401060:G>T, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap line ACH-000971), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 64 occupied (19 with a strong site), 5 of 133 with unknown occupancy. Left out: 6 TFs assayed in the matching biosample and 497 assayed only elsewhere, none with a peak here; 6 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): best model LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer (a CIS-BP-mapped model of LEF1), z -4.66, effect -0.47: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 63.61 TPM, rank 53 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000EUV. Best model's site strength: ref 98.8th, alt 98.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SRF (MADS box, 1 model; QBiC-SELEX coverage: own model): best model SRF_eDBD_TGCCAC40NGCC_KR_yin2017_0_3_7mer (its own model), z -7.74, effect -1.191: ref allele binds more (|z| above the gate), but between weak k-mers. 25.61 TPM, rank 217 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSC. Best model's site strength: ref 95.1th, alt 91.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): best model SP4_NA_TTATGT20NGTA_ESAE_yang2017_0_3_7mer (a CIS-BP-mapped model of SP4), z -4.76, effect -0.211: ref allele binds more (|z| above the gate), but between weak k-mers. 38.96 TPM, rank 118 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSF. Best model's site strength: ref 95.8th, alt 75.9th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e23"></a>**E23** qbic_screen (tested, negative), QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUND (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUN_FL_TCAGTG40NGAT_KAE_yin2017_0_3_7mer (a CIS-BP-mapped model of JUN), z -3.01, effect -0.059: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 18.66 TPM, rank 300 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSA. Best model's site strength: ref 89.3th, alt 96.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e24"></a>**E24** qbic_screen (tested, negative), QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CEBPB (bZIP, 3 models; QBiC-SELEX coverage: own model): best model CEBPB_eDBD_TATAAA40NACG_KAN_yin2017_0_4_7mer (its own model), z 1.9, effect 0.205: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 13.15 TPM, rank 408 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSD. Best model's site strength: ref 75.7th, alt 85.6th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e25"></a>**E25** qbic_screen (tested, negative), QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MAX (bHLH, 1 model; QBiC-SELEX coverage: own model): best model MAX_FL_TG40NGACCTT_YWN_jolma2025_0_3_7mer (its own model), z -0.97, effect -0.058: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 42.59 TPM, rank 102 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BSH. Best model's site strength: ref 91.8th, alt 95.3th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e26"></a>**E26** qbic_screen (tested, negative), QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> YY1 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model YY1_FL_GG40NGTGAGA_YWKA_jolma2025_0_3_7mer (its own model), z -0.43, effect -0.033: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 84.45 TPM, rank 34 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound here: ENCODE ChIP-seq peak over the variant in HCT116, e.g. ENCSR000BNX. Best model's site strength: ref 91.3th, alt 88.8th percentile of its k-mer coefficients: a weak site (neither allele reaches the 97.5th), so the ChIP peak more likely reflects another site in the element.

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> HNF4A (Nuclear receptor, 1 model; QBiC-SELEX coverage: own model): best model TLX_NA_Lib1_NA_bhimsaria2023_0(2)_2_7mer (a CIS-BP-mapped model of NR2E1), z 53.69, effect 1.968: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.95 TPM, rank 850 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, liver, e.g. ENCSR445QRF. Best model's site strength: ref 96.7th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GFI1 (C2H2 ZF, 2 models; QBiC-SELEX coverage: own model): best model GFI1B_eDBD_TTCTCA40NCCT_KR_yin2017_0_3_7mer (a CIS-BP-mapped model of GFI1B), z -31.27, effect -2.144: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 2.9 TPM, rank 857 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR849FVL. Best model's site strength: ref 99.9th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 61.74 TPM, rank 58 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR000BVM. Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZNF493 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZNF493_FL_TG40NTCTTGC_YWRA_jolma2025_0_2_7mer (its own model), z -34.16, effect -0.598: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.33 TPM, rank 977 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 100.0th, alt 88.9th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TBX19 (T-box, 2 models; QBiC-SELEX coverage: own model): best model TBX19_eDBD_TCTTGT40NCAG_KP_yin2017_0_4_7mer (its own model), z 26.18, effect 4.18: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.92 TPM, rank 936 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 79.0th, alt 99.9th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> MBNL2 (CCCH ZF, 1 model; QBiC-SELEX coverage: own model): best model MBNL2_FL_TCTAAG40NTTA_KZ_yin2017_0_4_7mer (its own model), z -22.42, effect -2.708: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.09 TPM, rank 209 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.1th, alt 51.1th percentile of its k-mer coefficients.

<a id="e33"></a>**E33** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1D1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 14.85 TPM, rank 361 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e34"></a>**E34** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR1D2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model NR2F6_FL_TGCCTC40NCAA_KV_yin2017_0_4_7mer (a CIS-BP-mapped model of NR2F6), z 20.82, effect 1.92: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 37.06 TPM, rank 132 of 1626 TFs in DepMap:ACH-000971 (HCT 116). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 98.6th, alt 100.0th percentile of its k-mer coefficients.

<a id="e35"></a>**E35** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"TCF7L2","symbol":"TCF7L2","via":"hgnc_symbol","notes":[],"coverage":"mapped","variant":"chr8:127401060:G>T","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"CIS-BP (LEF1)","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.47,"z":-4.66,"p":3.2e-06,"rank_abs_z":"351/997","passed_gate":true,"site_strength":{"ref_percentile":98.8,"alt_percentile":98.4,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.229,"z":-4.59,"p":4.4e-06,"rank_abs_z":"367/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.275,"z":-3.47,"p":0.00052,"rank_abs_z":"486/997","passed_gate":false,"site_strength":{"ref_percentile":83.5,"alt_percentile":92.1,"k":7}}]}

<a id="e36"></a>**E36** chip_peaks (not tested), ENCODE experiment search; ReMap 2022 (UCSC track ReMapTFs) (https://www.encodeproject.org/search/?type=Experiment&assay_title=TF+ChIP-seq&status=released&assembly=GRCh38&format=json&limit=all&field=target.label&field=biosample_ontology.term_name&field=accession; retrieved local)

> ENCODE has no NR2F2 ChIP-seq experiment in biosamples matching 'HCT116', so ENCODE says nothing about it there, for or against. ENCODE assayed NR2F2 in: HepG2, K562, MCF-7, liver. ReMap 2022 (published ChIP-seq, reprocessed): 1 NR2F2 peaks contain the variant, in 1 biosamples: Hep-G2 (ENCSR000BVM). 0 of them in biosamples matching 'HCT116'.

<a id="e37"></a>**E37** gene_dependency (tested, negative), DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for POU5F1B (0 = no effect, -1 = median common-essential; < -0.5 called dependent). HCT 116 (ACH-000971): -0.09. Bowel lineage, 31 lines: median -0.06, 0% dependent. All 351 lines: median -0.05, 3% dependent.

<a id="e38"></a>**E38** eqtl_lookup, GTEx Portal API v2 (gtex_v8) (https://gtexportal.org/api/v2/association/singleTissueEqtl?variantId=chr8_127401060_G_T_b38&datasetId=gtex_v8; retrieved 2026-10-25T16:35:30+00:00)

> 1 significant GTEx v8 single-tissue eQTLs for chr8_127401060_G_T_b38 in Colon_Transverse. NES is the effect of the alt allele (T) relative to ref (G).
> POU5F1B in Colon_Transverse: NES +0.20, p 8.2e-06

<a id="e39"></a>**E39** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TCF7L2%20CASC8%20colorectal%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-28T00:58:19+00:00)

> Europe PMC: 37 hits for 'TCF7L2 CASC8 colorectal cancer'; top 8 with PMIDs:
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 40356985 (2025): Research progress on m6A and drug resistance in gastrointestinal tumors.
> PMID 36800588 (2023): TCF7L2, CASC8, and GREM1 polymorphism and colorectal cancer in south-eastern Romanian population.
> PMID 35893034 (2022): Association of &lt;i&gt;TCF7L2&lt;/i&gt;, &lt;i&gt;CASC8&lt;/i&gt; and &lt;i&gt;GREM1&lt;/i&gt; Polymorphisms in Patients with Colorectal Cancer and Type II Diabetes Mellitus.
> PMID 39921239 (2025): System genetic analysis of intestinal cancer and periodontitis development as influenced by aging and diabesity using Collaborative Cross mice.
> PMID 37961996 (2024): New insights into the interaction between m6A modification and lncRNA in cancer drug resistance.
> PMID 40642605 (2025): Functions and mechanisms of long non-coding RNA in esophageal squamous cell carcinoma (Review).

<a id="e39a"></a>**E39a** literature_search, Europe PMC abstract, PMID 41144378 (https://europepmc.org/article/MED/41144378; retrieved 2026-10-28T00:58:19+00:00)

> Integration of GWAS and RNA-seq revealed that 24 CRC-associated genes, including PYGL, SMAD7, and TCF7L2, are involved in tumor metabolism and Wnt/TCF signaling.

<a id="e39b"></a>**E39b** literature_search, Europe PMC abstract, PMID 36800588 (https://europepmc.org/article/MED/36800588; retrieved 2026-10-28T00:58:19+00:00)

> The aim of our study was to investigate the association of the TCF7L2 rs[masked], CASC8 rs[masked], and Gremlin1 (GREM1) rs[masked] polymorphism in patients with CRC without other pathologies.

<a id="e39c"></a>**E39c** literature_search, Europe PMC abstract, PMID 36800588 (https://europepmc.org/article/MED/36800588; retrieved 2026-10-28T00:58:19+00:00)

> Our study did not confirm a significant association between TCF7L2 rs[masked], CASC8 rs[masked], and GREM1 rs[masked] with CRC, but emphasizes the possibility of existence of a high risk of CRC development in patients with TT genotype of rs[masked].

<a id="e39d"></a>**E39d** literature_search, Europe PMC abstract, PMID 35893034 (https://europepmc.org/article/MED/35893034; retrieved 2026-10-28T00:58:19+00:00)

> BackgroundThe aim of the study is to explore the association between the TCF7L2 rs[masked], CASC8 rs[masked] and GREM1 rs[masked] polymorphisms in patients diagnosed with type 2 diabetes mellitus (T2DM) and colorectal cancer.

<a id="e39e"></a>**E39e** literature_search, Europe PMC abstract, PMID 35893034 (https://europepmc.org/article/MED/35893034; retrieved 2026-10-28T00:58:19+00:00)

> ConclusionsTCF7L2 rs[masked], CASC8 rs[masked] and GREM1 rs[masked] could be risk factors for the association of T2DM with CRC.

<a id="e40"></a>**E40** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-28T00:58:29+00:00)

> Open Targets: CASC8 and colorectal cancer (MONDO_0005575), overall score 0.02; by evidence type: literature 0.17, rna_expression 0.06

<a id="e41"></a>**E41** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TCF7L2%20POU5F1B%20colorectal%20cancer&format=json&pageSize=8&resultType=core; retrieved 2026-10-28T01:00:10+00:00)

> Europe PMC: 37 hits for 'TCF7L2 POU5F1B colorectal cancer'; top 8 with PMIDs:
> PMID 41796348 (2026): Harnessing the LncRNA CCAT2 role in gastric cancer: from molecular insights to clinical implications.
> PMID 41144378 (2025): Integrative GWAS and RNA-Seq analysis for target identification and virtual drug screening in colorectal cancer.
> PMID 40498368 (2025): CCAT2 role in gastrointestinal cancer progression and metastasis: a novel target for therapeutic strategies.
> PMID 40458721 (2025): Integrating next-generation sequencing and artificial intelligence for the identification and validation of pathogenic variants in colorectal cancer.
> PMID 39921239 (2025): System genetic analysis of intestinal cancer and periodontitis development as influenced by aging and diabesity using Collaborative Cross mice.
> PMID 40770356 (2025): Distinctive chromosomal, mutational and transcriptional profiling in colon versus rectal cancers.
> PMID 38670944 (2024): Fine-mapping analysis including over 254,000 East Asian and European descendants identifies 136 putative colorectal cancer susceptibility genes.
> PMID 39284974 (2024): Systematic prioritization of functional variants and effector genes underlying colorectal cancer risk.

<a id="e41a"></a>**E41a** literature_search, Europe PMC abstract, PMID 41144378 (https://europepmc.org/article/MED/41144378; retrieved 2026-10-28T01:00:10+00:00)

> Integration of GWAS and RNA-seq revealed that 24 CRC-associated genes, including PYGL, SMAD7, and TCF7L2, are involved in tumor metabolism and Wnt/TCF signaling.

<a id="e42"></a>**E42** gene_disease, Open Targets Platform (https://api.platform.opentargets.org/api/v4/graphql; retrieved 2026-10-26T02:23:32+00:00)

> Open Targets: POU5F1B and colorectal cancer (MONDO_0005575), overall score 0.54; by evidence type: genetic_association 0.87, literature 0.18, rna_expression 0.14

<a id="e43"></a>**E43** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"LEF1","symbol":"LEF1","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr8:127401060:G>T","gate_p":5.02e-05,"models":[{"model":"LEF1_FL_TAGTCG40NAGA_KZ_yin2017_0_3_7mer","mapping":"own","group":"G041 HMG/Sox, 3 models","quality":0.63,"effect":-0.47,"z":-4.66,"p":3.2e-06,"rank_abs_z":"351/997","passed_gate":true,"site_strength":{"ref_percentile":98.8,"alt_percentile":98.4,"k":7}},{"model":"TCF7_eDBD_TCGGAC40NCCA_KS_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7)","group":"G041 HMG/Sox, 3 models","quality":0.732,"effect":-0.229,"z":-4.59,"p":4.4e-06,"rank_abs_z":"367/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.2,"k":7}},{"model":"TCF7L1_eDBD_TTGGCA40NTCG_KW_yin2017_0_3_7mer","mapping":"CIS-BP (TCF7L1)","group":"G041 HMG/Sox, 3 models","quality":0.602,"effect":-0.275,"z":-3.47,"p":0.00052,"rank_abs_z":"486/997","passed_gate":false,"site_strength":{"ref_percentile":83.5,"alt_percentile":92.1,"k":7}}]}
