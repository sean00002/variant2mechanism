# TERT promoter C228T and Glioblastoma, melanoma, bladder

Configuration `full`, masked mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.06 over 28 model calls; 484 s.

Variant `chr5:1295113:G>A` (somatic); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

**Verdict: undetermined.** The null leads, but nothing tested counts against GABPA, TFAP2C, ETV3.

Pairwise ranking (Bradley-Terry strengths): GABPA_ETS_alt 0.62, ETV3_ETS_alt_unknown_occupancy 0.17, TFAP2C_ref_repressor_loss 0.17, null_no_TF_mediated_effect 0.05. 0 of 6 pairs came out differently in the two orders.

## QBiC-SELEX screen (occupancy first)

Occupied candidates: GABPA (bound elsewhere, z 166.19); ZIC2 (bound elsewhere, z -20.85); CTCF (bound elsewhere, z -14.7); ZBTB7A (bound elsewhere, z -14.11); NR2C1 (bound elsewhere, z -10.53); E2F4 (bound elsewhere, z 5.78); E2F6 (bound elsewhere, z 5.78); E2F5 (bound elsewhere, z 5.78); EGR1 (bound elsewhere, z -3.42, no clear allelic change); JUN (bound elsewhere, z 3.26, no clear allelic change). Occupancy unknown: ETV2 (z 166.19); ETV3 (z 166.19); FLI1 (z 166.19); TFAP2A (z -36.84); TFAP2C (z -36.84). Diagnostic, not shown to the model: 310 of 997 models pass Bonferroni.

## Ranked chains

### 1. null_no_TF_mediated_effect: No TF-mediated allelic effect at this base; linked variant, passenger hotspot, or no functional consequence (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF occupancy or chromatin change is found at this exact base in a disease-relevant cell type.; Any disease association is explained by a linked causal variant, a passenger mutation at a mutational hotspot, or TERT promoter effects not mediated by the predicted TF-site change.; QBiC-SELEX differences do not translate into occupancy or function in the relevant disease cell type.

Falsified if: Allele-specific TF occupancy and TERT expression or promoter activity are both shown in a relevant disease cell type.; A specific TF is shown to bind the alt or ref allele and causally change TERT expression.; The variant is shown to be the causal base rather than a linked passenger.

### 2. GABPA_ETS_alt: Alt allele strengthens a GABPA/Ets site in the TERT promoter; GABP is a known TERTp activator but glioblastoma occupancy at this base is unproven (p = 0.40)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type glioblastoma (DepMap subtype median).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA has its own QBiC-SELEX model that passes the gate and shows the alt allele binds more strongly (effect +4.01, z 68.47; alt site 99.8th percentile), and a shared Ets model also shows alt-more binding (effect +2.121, z 166.19). GABPA is expressed in glioblastoma and GABPA ChIP-seq peaks over this variant exist in other biosamples, but no glioblastoma ChIP is available, so occupancy at this element in the disease context is unproven. Literature supports GABP as a TERT-promoter activator at TERTp mutations generally, not this exact base. | weak | [E33](#e33), [E17](#e17), [E11](#e11), [E32](#e32), [E35c](#e35c), [E35e](#e35e), [E39e](#e39e) |
| element | The variant lies in the promoter-like cCRE EH38E3622530 with DNase, H3K27ac and H3K4me3 signal, and is annotated as a TERT upstream promoter-region variant. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest protein-coding gene, with its TSS 0.0 kb away, and VEP annotates the variant as a TERT upstream_gene_variant. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is the expression context and GABPA is expressed there, but no glioblastoma GABPA ChIP-seq is available; GABPA knockout is common-essential rather than lineage-selective, so the cell-type link is weak and not specific. | weak | [E15](#e15), [E11](#e11), [E32](#e32), [E36](#e36) |
| phenotype | The phenotype link is inferential: GABP has been reported to activate mutant TERTp generally, and TERTp mutations are common in glioblastoma, but no cited study tests this exact variant or shows GABPA-dependent TERT activation through this base. TERT is not a selective dependency in glioblastoma lines, and GABPA is common-essential, so the lineage-specific phenotype link remains weak. | weak | [E15](#e15), [E35c](#e35c), [E39d](#e39d), [E39e](#e39e), [E36](#e36), [E37](#e37) |

Predictions: Allele-specific GABPA ChIP or CUT&RUN in a glioblastoma cell line heterozygous at chr5:1295113 shows GABPA occupancy at this element, with the alt allele bound more strongly.; Acute GABPA or GABPB1 knockdown reduces TERT expression or an alt/ref TERT promoter reporter preferentially from the alt allele.; The variant's effect on TERT is GABPA/Ets-dependent, not mediated by TFAP2C or a non-Ets mechanism.

Falsified if: No GABPA occupancy is detectable at this element in glioblastoma cells.; The alt allele does not increase TERT expression or promoter activity in a GABPA-dependent manner.; The shared Ets QBiC-SELEX signal is shown to be irrelevant to GABPA because another Ets factor fully accounts for occupancy and function.

### 3. TFAP2C_ref_repressor_loss: Ref allele binds TFAP2C more strongly; alt allele may lose a repressive AP-2 site, but no TERT-repressor evidence (p = 0.03)

TF TFAP2C (QBiC-SELEX coverage own_model), ref allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type glioblastoma (DepMap subtype median).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2C has a QBiC-SELEX model showing the ref allele binds more strongly (effect -1.289, z -36.84), but it is a TFAP2E-mapped model. TFAP2C was never assayed by ENCODE here, so occupancy at this element is unknown and the evidence is in vitro only. | weak | [E31](#e31) |
| element | The variant is in a promoter-like cCRE with active promoter marks, consistent with a regulatory element that could bind AP-2 factors. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene and the variant is annotated as a TERT upstream variant. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is the expression context and TFAP2C is expressed, but TFAP2C occupancy at this element in glioblastoma is not established here. | weak | [E15](#e15), [E31](#e31) |
| phenotype | No cited evidence shows TFAP2C represses TERT or acts at this variant; the TFAP2C TERT promoter repressor literature search returned no direct TFAP2C-TERT repressor evidence. TERT is not a selective dependency in glioblastoma lines. | missing | [E40](#e40), [E37](#e37) |

Predictions: Ref allele increases TFAP2C occupancy at this element in a TFAP2C-expressing cancer cell context.; Alt allele reduces TFAP2C binding and, if TFAP2C is repressive, increases TERT expression.; TFAP2C knockdown phenocopies the alt allele only if TFAP2C represses TERT.

Falsified if: TFAP2C does not occupy the TERT promoter in relevant cells.; Alt allele does not change TERT expression in a TFAP2C-dependent direction.; TFAP2C acts as an activator rather than a repressor, reversing the predicted phenotype direction.

### 4. ETV3_ETS_alt_unknown_occupancy: Low-expression Ets factor ETV3 is a weak alternative at the same Ets motif (p = 0.02)

TF ETV3 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter cCRE EH38E3622530; gene TERT; cell type glioblastoma (DepMap subtype median).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ETV3 has only a shared ETV5-mapped Ets QBiC-SELEX model showing stronger alt-allele binding (effect +2.121, z 166.19). ETV3 is expressed at low level in glioblastoma, and ENCODE never assayed ETV3, so occupancy at this site is unknown; this in vitro binding evidence does not uniquely identify ETV3. | weak | [E28](#e28) |
| element | The variant lies in the promoter-like cCRE EH38E3622530 with active promoter marks and TERT upstream annotation. | supported | [E01](#e01), [E03](#e03) |
| gene | TERT is the nearest gene and the variant is annotated as a TERT upstream variant. | supported | [E01](#e01), [E02](#e02) |
| cell_type | Glioblastoma is the expression context and ETV3 is expressed at low level there, but direct ETV3 occupancy in glioblastoma is not shown. | weak | [E15](#e15), [E28](#e28) |
| phenotype | No cited evidence links ETV3 to TERT regulation or this variant; the ETV3 TERT promoter literature search returned no direct ETV3-TERT evidence. TERT is not a selective dependency in glioblastoma lines. | missing | [E39](#e39), [E37](#e37) |

Predictions: Alt allele increases ETV3 occupancy at the TERT promoter in a cell type where ETV3 is sufficiently expressed.; ETV3 knockdown reduces TERT expression from the alt allele.; The effect is ETV3-dependent rather than GABPA-dependent.

Falsified if: ETV3 does not occupy the TERT promoter in any TERT-expressing cancer cell model.; The alt-allele Ets effect is fully accounted for by GABPA or another Ets factor with no ETV3 contribution.; ETV3 expression is too low to support functional occupancy in glioblastoma.

## Prediction matrix

| Test | Cost | Separates top two | null_no_TF_mediated_effect | GABPA_ETS_alt | TFAP2C_ref_repressor_loss | ETV3_ETS_alt_unknown_occupancy |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA CUT&RUN/ChIP in a glioblastoma line heterozygous at chr5:1295113 | high | yes | No allele-specific GABPA occupancy. | Alt > ref GABPA occupancy at this element. | No GABPA allelic occupancy; ref > alt TFAP2C in parallel assay. | No GABPA allelic occupancy; ETV3 not measured by this assay. |
| Acute GABPA or GABPB1 knockdown in a TERTp-mutant glioblastoma line; measure TERT expression and allele-specific transcript | medium | yes | No change in TERT expression or allele-specific transcript. | TERT decreases, with preferential loss of alt-allele transcript. | No GABPA-dependent decrease; TFAP2C knockdown may increase TERT if the repressor model is true. | No GABPA-dependent decrease; ETV3 knockdown, not GABPA knockdown, affects TERT if this chain is true. |
| Allele-specific TFAP2C ChIP/CUT&RUN in TFAP2C-expressing cells | high | no | No TFAP2C allele bias. | No TFAP2C allele bias. | Ref > alt TFAP2C occupancy. | No TFAP2C allele bias. |
| Allele-specific ETV3 ChIP/CUT&RUN or ETV3 knockdown in ETV3-expressing cells | high | no | No ETV3 allele bias and no ETV3-dependent TERT change. | No ETV3 allele bias and no ETV3-dependent TERT change. | No ETV3 allele bias and no ETV3-dependent TERT change. | Alt > ref ETV3 occupancy and ETV3 knockdown reduces TERT. |
| TERT promoter reporter (ref vs alt) in glioblastoma cells, with GABPA-site mutation or GABPA knockdown | medium | yes | Ref and alt reporters are equal. | Alt increases reporter activity; GABPA-site mutation or GABPA knockdown abolishes the alt-specific increase. | Alt increases reporter activity through loss of repression; GABPA-site mutation has no effect. | Alt increases reporter activity, but ETV3 knockdown, not GABPA-site mutation, reduces the effect. |

## Next experiment

Acute GABPA/GABPB1 knockdown in a heterozygous TERTp-mutant glioblastoma line, measuring total and allele-specific TERT transcript. It is cheaper than allele-specific ChIP/CUT&RUN and separates the top two chains: GABPA_ETS_alt predicts a GABPA-dependent drop in TERT, preferentially from the alt allele, whereas the null predicts no change.

## Refinement rounds

Stopped: round 3 left the top chain and the grades of its links unchanged.

### Round 1

- chip_peaks({"tf": "GABPA", "biosample": "glioblastoma"}) for GABPA_ETS_alt.binding, ran as [E32](#e32) (not tested). Expected: If a GABPA ChIP-seq peak containing the variant is found in glioblastoma or a glioblastoma-derived biosample, GABPA_ETS_alt.binding moves from weak to supported and this chain rises toward the null. If the result is negative or not tested, GABPA occupancy in the relevant context remains unshown and the null gains relative weight.
- qbic_tf_detail({"tf": "GABPA"}) for GABPA_ETS_alt.binding, ran as [E33](#e33). Expected: If GABPA has its own QBiC-SELEX model that passes the gate with the same alt-allele preference, the shared Ets signal becomes more attributable to GABPA and GABPA_ETS_alt.binding strengthens. If GABPA is covered only through the CIS-BP-mapped ETV5/Ets model, the binding evidence remains weak and this chain stays less distinguishable from other Ets factors, favoring the null.
- literature_search({"query": "GABPA TERT promoter glioblastoma"}) for GABPA_ETS_alt.phenotype, ran as [E34](#e34). Expected: If abstracts report GABPA binding or activating the TERT promoter or Ets motifs in glioblastoma, the phenotype link gains support and GABPA_ETS_alt rises. If no such evidence is returned, the phenotype link remains missing and the null gains relative weight.

- Result of chip_peaks({"tf": "GABPA", "biosample": "glioblastoma"}): E32: no ENCODE GABPA ChIP-seq in glioblastoma; ReMap has GABPA peaks only in Hep-G2 and SK-N-SH, 0 in glioblastoma. The result is 'not tested' for the matching context, so it is no evidence for or against GABPA occupancy in glioblastoma. (as expected: yes)
- Result of qbic_tf_detail({"tf": "GABPA"}): E33: GABPA has its own QBiC-SELEX model that passes the gate and shows stronger alt-allele binding (effect +4.01, z 68.47), plus several CIS-BP-mapped Ets models with the same alt-more direction. This strengthens GABPA-specific in vitro binding but does not establish occupancy. (as expected: yes)
- Result of literature_search({"query": "GABPA TERT promoter glioblastoma"}): E34: 147 hits, but the top titles are broad TERT/TERT-promoter cancer literature and do not report GABPA binding or activating the TERT promoter in glioblastoma. The phenotype link remains missing/inferential. (as expected: yes)

Chains after revision: GABPA 0.46; null 0.39; ETV3 0.09; TFAP2C 0.06. Link grades changed: ETV3_ETS_alt_unknown_occupancy.phenotype: missing → weak, GABPA_ETS_alt.phenotype: missing → weak, TFAP2C_ref_repressor_loss.phenotype: missing → weak.

### Round 2

- literature_search({"query": "GABPA GABP TERT promoter mutation binding"}) for GABPA_ETS_alt.binding, ran as [E35](#e35). Expected: If the search returns direct evidence that GABPA/GABP binds the TERT promoter at an Ets motif and activates TERT in glioblastoma or TERT-promoter-mutant cancer cells, the binding and phenotype claims for GABPA strengthen. If it returns only generic TERT-cancer or GABPA-biology papers, the binding link stays weak. The result would change GABPA_ETS_alt.binding from weak toward supported only with specific GABPA-TERT promoter occupancy/function evidence.
- gene_dependency({"gene": "GABPA"}) for GABPA_ETS_alt.cell_type, ran as [E36](#e36). Expected: If DepMap CRISPR shows GABPA knockout selectively reduces fitness in glioblastoma lineage lines and GABPA is not common-essential, the cell-type/phenotype relevance of GABPA in glioblastoma strengthens. If GABPA is common-essential or shows no lineage-selective effect, this weakens the GABPA chain and leaves more weight on the null.
- gene_dependency({"gene": "TERT"}) for GABPA_ETS_alt.phenotype, ran as [E37](#e37). Expected: If TERT is a selective dependency in the glioblastoma lineage, the phenotype link from a TERT-activating promoter allele to disease is strengthened for all non-null chains. If TERT is not a selective dependency or is common-essential, this call does not separate GABPA from the null and the phenotype link remains weak.

- Result of literature_search('GABPA GABP TERT promoter mutation binding'): E35: GABP tetramer is reported to be responsible for promoter activation in TERTp-mutant cancers; TERTp mutations create de novo ETS binding motifs; a GABPA-bound promoter example is given. (as expected: yes)
- Result of gene_dependency('GABPA'): E36: GABPA CRISPR median gene effect -0.87 in CNS/brain and all lines, with 94% and 97% dependent; common-essential, not lineage-selective. (as expected: no)
- Result of gene_dependency('TERT'): E37: TERT CRISPR median gene effect approximately 0.00 in CNS/brain and all lines, with only 2% and 1% dependent; not a selective dependency. (as expected: no)

Chains after revision: null 0.50; GABPA 0.40; ETV3 0.05; TFAP2C 0.05. Link grades changed: ETV3_ETS_alt_unknown_occupancy.phenotype: weak → missing, TFAP2C_ref_repressor_loss.phenotype: weak → missing.

### Round 3

- gene_disease({"gene": "GABPA"}) for GABPA_ETS_alt.phenotype, ran as [E38](#e38) (failed). Expected: If Open Targets returns strong GABPA–glioblastoma/melanoma/bladder association evidence, the GABPA phenotype link could strengthen from weak toward supported and GABPA could separate from the null; if GABPA has no disease association, the phenotype link stays weak and the null gains relative weight.
- literature_search({"query": "ETV3 TERT promoter"}) for ETV3_ETS_alt_unknown_occupancy.phenotype, ran as [E39](#e39). Expected: If direct ETV3–TERT promoter regulatory evidence exists, the ETV3 phenotype link could move from missing to weak/supported and the chain could rise slightly; if no such evidence is returned, the phenotype link remains missing and the ETV3 chain falls.
- literature_search({"query": "TFAP2C TERT promoter repressor"}) for TFAP2C_ref_repressor_loss.phenotype, ran as [E40](#e40). Expected: If TFAP2C is reported to bind or repress the TERT promoter, the TFAP2C phenotype link could move from missing to weak and the repressive-direction claim gains some support; if no direct evidence is found, the phenotype link remains missing and the TFAP2C chain falls.

- Result of gene_disease({"gene": "GABPA"}) for GABPA_ETS_alt.phenotype: E38: Open Targets lookup failed with no disease match for 'Glioblastoma, melanoma, bladder'. This is a technical non-result, not evidence that GABPA is unassociated. (as expected: unclear)
- Result of literature_search({"query": "ETV3 TERT promoter"}) for ETV3_ETS_alt_unknown_occupancy.phenotype: E39: 18 hits, but the top hits concern TERTp mutations, GABP, or unrelated topics; no direct ETV3-TERT promoter regulatory evidence was returned. ETV3 phenotype link remains missing. (as expected: yes)
- Result of literature_search({"query": "TFAP2C TERT promoter repressor"}) for TFAP2C_ref_repressor_loss.phenotype: E40: 30 hits, but no direct evidence that TFAP2C binds or represses the TERT promoter; E40a concerns a breast-cancer AP-2 site, not TERT. TFAP2C phenotype link remains missing. (as expected: yes)

Chains after revision: null 0.55; GABPA 0.40; TFAP2C 0.03; ETV3 0.02. Link grades changed: none.

## Flags

- quote_rejected: PMID 41744838: not an exact substring of the abstract
- quote_rejected: PMID 40513567: not an exact substring of the abstract
- tool_failed: E38 gene_disease: Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'

Citation support: 1.00 of links cite only evidence that passed every check.

## Evidence

<a id="e01"></a>**E01** variant_annotation, Ensembl VEP (GRCh38) (https://rest.ensembl.org/vep/human/region/5:1295113-1295113:1/A?content-type=application/json&Conservation=1; retrieved 2026-10-25T11:57:36+00:00)

> Variant chr5:1295113:G>A (GRCh38), allele string G/A
> Known IDs: rs1242535815
> Most severe consequence: upstream_gene_variant
> Regulatory features: ENSR5_832QG promoter
> GERP conservation score at the site: -7.45
> Transcript consequences: TERT (upstream_gene_variant)

<a id="e02"></a>**E02** nearest_genes, Ensembl overlap (protein_coding) (https://rest.ensembl.org/overlap/region/human/5:295113-2295113?feature=gene;biotype=protein_coding;content-type=application/json; retrieved 2026-10-25T11:57:33+00:00)

> 23 protein-coding genes within 1000 kb of chr5:1295113:G>A, by distance to TSS:
> TERT: 0.0 kb from TSS (upstream, strand -1)
> CLPTM1L: 50.0 kb from TSS (downstream, strand -1)
> SLC6A18: 69.7 kb from TSS (downstream, strand +1)
> SLC6A19: 93.5 kb from TSS (downstream, strand +1)
> SLC12A7: 138.9 kb from TSS (upstream, strand -1)
> SLC6A3: 150.4 kb from TSS (downstream, strand -1)
> LPCAT1: 229.2 kb from TSS (downstream, strand -1)
> NKD2: 287.1 kb from TSS (downstream, strand +1)
> TRIP13: 402.3 kb from TSS (downstream, strand +1)
> BRD9: 402.3 kb from TSS (upstream, strand -1)

<a id="e03"></a>**E03** ccre_lookup, ENCODE v4 cCRE registry (ENCFF420VPZ) and SCREEN (https://screen-beta-api.wenglab.org/dataws/cre_table; retrieved 2026-10-25T11:57:31+00:00)

> The variant lies in cCRE EH38E3622530 (PLS: promoter-like), chr5:1294945-1295294.
> SCREEN: 3 cCREs within 500 bp (max z-score across ENCODE biosamples):
> EH38E3622530 PLS (contains the variant): DNase z 4.8, H3K27ac z 4.2, H3K4me3 z 4.5, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622531 pELS: DNase z 3.9, H3K27ac z 4.3, H3K4me3 z 4.4, CTCF z 2.8; nearby genes TERT, MIR4457, CLPTM1L
> EH38E3622529 pELS: DNase z 3.7, H3K27ac z 4.1, H3K4me3 z 4.6, CTCF z 2.0; nearby genes TERT, MIR4457, CLPTM1L
> Biosample-specific z-scores are not in this call; the values above are maxima over biosamples.

<a id="e04"></a>**E04** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ENCODE TF ChIP-seq at chr5:1295113:G>A: 121 peaks contain the variant, from 54 factors in 21 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: PLS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, BCL3, DMAP1, EZH2, EZH2phosphoT487, GABPB1, HDAC1, HDAC2, HDAC6, HNRNPK, IKZF1, KDM4A (+21 more). Bound, expressed TFs with a binding model: 20; listed one per row: MAX, JUN, EGR1, BHLHE40, E2F4, E2F6, GABPA, ZNF687, CTCF, NR2C1; also bound: ZNF143, SP2, TGIF2, MNT, ZBTB7A, E2F5, ZBTB26, KLF12, ZNF48, ZIC2. Bound but below 1 TPM: ZFHX2. Assayed with no peak here: 0 TFs in the matching biosample, 552 only elsewhere; never assayed: 536.

<a id="e05"></a>**E05** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> MAX: bound elsewhere. 13 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, HCT116, HepG2, Ishikawa, K562, MCF-7 (+2 more) (e.g. ENCSR000BLP). 58.6 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 48 of 1626 TFs.

<a id="e06"></a>**E06** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> JUN: bound elsewhere. 11 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549 (e.g. ENCSR022WVP). 91.65 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 16 of 1626 TFs.

<a id="e07"></a>**E07** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> EGR1: bound elsewhere. 3 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, Ishikawa, K562 (e.g. ENCSR000BNE). 28.32 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 151 of 1626 TFs.

<a id="e08"></a>**E08** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> BHLHE40: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR000DZJ). 68.33 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 33 of 1626 TFs.

<a id="e09"></a>**E09** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> E2F4: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878, HepG2 (e.g. ENCSR000DYY). 58.31 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 49 of 1626 TFs.

<a id="e10"></a>**E10** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> E2F6: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: A549, K562 (e.g. ENCSR000BLI). 17.63 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 267 of 1626 TFs.

<a id="e11"></a>**E11** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> GABPA: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2, SK-N-SH (e.g. ENCSR000BJK). 15.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 303 of 1626 TFs.

<a id="e12"></a>**E12** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> ZNF687: bound elsewhere. 2 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: HepG2 (e.g. ENCSR647PSR). 10.74 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 436 of 1626 TFs.

<a id="e13"></a>**E13** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> CTCF: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: DOHH2 (e.g. ENCSR084RDK). 26.45 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 163 of 1626 TFs.

<a id="e14"></a>**E14** occupancy, ENCODE TF ChIP-seq (Factorbook peaks; ENCODE experiment search) (https://factorbook.api.wenglab.org/graphql; retrieved local)

> NR2C1: bound elsewhere. 1 ENCODE ChIP-seq peak(s) contain the variant, only in other biosamples: GM12878 (e.g. ENCSR784VIQ). 18.52 TPM in DepMap:subtype=Glioblastoma (median of 54 lines), rank 251 of 1626 TFs.

<a id="e15"></a>**E15** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TERT%20AND%20%28%22glioblastoma%22%20OR%20%22melanoma%22%20OR%20%22bladder%22%29&format=json&pageSize=8&resultType=core; retrieved 2026-10-25T11:57:36+00:00)

> Europe PMC: 23888 hits for 'TERT AND ("glioblastoma" OR "melanoma" OR "bladder")'; top 7 with PMIDs:
> PMID 41744838 (2026): Telomerase Activity in Melanoma: Impact on Cancer Cell Proliferation Kinetics, Tumor Progression, and Clinical Therapeutic Strategies-A Scoping Review.
> PMID 42577103 (2026): Familial melanoma: genetic, clinical, and dermoscopic insights and follow-up.
> PMID 42722679 (2026): Developing neoantigen cancer vaccines: where are we now?
> PMID 42741698 (2026): Melanoma of unknown primary with solitary lesions to the prostate and lung uncovered after simple prostatectomy.
> PMID 42804732 (2026): SNP rs[masked] potentially elevates the risk of glioblastoma development and leads to worse prognosis when in cis with mutant TERT promoter in a Japanese cohort.
> PMID 42807929 (2026): USP10 stabilizes FOXM1 through KAT5-mediated acetylation to suppress cell senescence and promote melanoma malignant progression.
> PMID 42859331 (2026): CDKN2A deletion associated with poor prognosis in patients with TERT promoter wild-type, IDH wild-type glioblastoma.

<a id="e16"></a>**E16** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> QBiC-SELEX screen of chr5:1295113:G>A, one line per TF, each with the TF's own or CIS-BP-mapped model of largest |z|. Candidates are TFs whose ENCODE ChIP-seq peaks contain the variant and that are expressed (DepMap subtype median Glioblastoma), bound here before bound elsewhere, then a strong site before a weak one, then by |z|; then expressed TFs ENCODE never assayed whose best model passes the gate (occupancy unknown). Shown: 10 of 20 occupied (15 with a strong site), 5 of 111 with unknown occupancy. Left out: 0 TFs assayed in the matching biosample and 552 assayed only elsewhere, none with a peak here; 1 bound but below 1 TPM. The gate (|z| > 4.05, Bonferroni over 997 models) marks a change QBiC-SELEX detects; it says nothing about occupancy. Effect > 0 means the alternate allele binds more strongly. In vitro binding only. Site strength is the better allele's best k-mer over the variant, as a percentile of the best model's k-mers; a strong site reaches the 97.5th. At a weak site the ChIP peak more likely reflects another site in the element.

<a id="e17"></a>**E17** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> GABPA (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 15.52 TPM, rank 303 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, SK-N-SH, e.g. ENCSR000BJK. Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e18"></a>**E18** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZIC2 (C2H2 ZF, 4 models; QBiC-SELEX coverage: mapped models only): best model ZIC4_eDBD_TGCGTA40NTCA_KT_yin2017_1_3_7mer (a CIS-BP-mapped model of ZIC4), z -20.85, effect -0.916: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 3.7 TPM, rank 852 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HEK293, e.g. ENCSR728MWW. Best model's site strength: ref 99.8th, alt 97.4th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e19"></a>**E19** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model CTCF_FL_TG40NCTGTGG_YWL_jolma2025_0_3_7mer (its own model), z -14.7, effect -1.719: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 26.45 TPM, rank 163 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in DOHH2, e.g. ENCSR084RDK. Best model's site strength: ref 99.8th, alt 97.0th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e20"></a>**E20** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ZBTB7A (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): best model ZBTB7A_eDBD_TTTGCT40NCGT_KR_yin2017_0_4_7mer (its own model), z -14.11, effect -0.826: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.49 TPM, rank 531 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in K562, e.g. ENCSR000BME. Best model's site strength: ref 99.9th, alt 99.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e21"></a>**E21** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> NR2C1 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): best model FXR_NA_Lib1_NA_bhimsaria2023_0(3)_3_7mer (a CIS-BP-mapped model of NR1H4), z -10.53, effect -0.434: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 18.52 TPM, rank 251 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, e.g. ENCSR784VIQ. Best model's site strength: ref 97.7th, alt 97.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e22"></a>**E22** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F4 (E2F, 4 models; QBiC-SELEX coverage: own model): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 58.31 TPM, rank 49 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in GM12878, HepG2, e.g. ENCSR000DYY. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e23"></a>**E23** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F6 (E2F, 4 models; QBiC-SELEX coverage: mapped models only): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 17.63 TPM, rank 267 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, K562, e.g. ENCSR000BLI. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e24"></a>**E24** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> E2F5 (E2F, 4 models; QBiC-SELEX coverage: mapped models only): best model E2F1_NA_CAATT14N_ESU_yang2017_0_4_7mer (a CIS-BP-mapped model of E2F1), z 5.78, effect 0.464: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.91 TPM, rank 605 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, e.g. ENCSR486JYI. Best model's site strength: ref 98.9th, alt 99.5th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e25"></a>**E25** qbic_screen (tested, negative), QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> EGR1 (C2H2 ZF, 4 models; QBiC-SELEX coverage: own model): best model EGR4_NA_TGCGCC20NCGC_Y_jolma2013_1_4_7mer (a CIS-BP-mapped model of EGR4), z -3.42, effect -0.541: ref allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 28.32 TPM, rank 151 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in HepG2, Ishikawa, K562, e.g. ENCSR000BNE. Best model's site strength: ref 99.5th, alt 99.6th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e26"></a>**E26** qbic_screen (tested, negative), QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> JUN (bZIP, 3 models; QBiC-SELEX coverage: own model): best model JUND_eDBD_TCTCTA40NCAC_KS_yin2017_0_4_7mer (a CIS-BP-mapped model of JUND), z 3.26, effect 0.185: alt allele binds slightly more; occupied, no clear allelic change (|z| below the gate). 91.65 TPM, rank 16 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: bound elsewhere: ENCODE ChIP-seq peak over the variant in A549, e.g. ENCSR022WVP. Best model's site strength: ref 98.5th, alt 94.9th percentile of its k-mer coefficients: a strong site (the better allele reaches the 97.5th).

<a id="e27"></a>**E27** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV2 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 1.4 TPM, rank 1063 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e28"></a>**E28** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> ETV3 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 8.69 TPM, rank 521 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e29"></a>**E29** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> FLI1 (Ets, 18 models; QBiC-SELEX coverage: own model): best model ETV5_NA_TGCACT20NGA_ESAF_yang2017_1_3_6mer (a CIS-BP-mapped model of ETV5), z 166.19, effect 2.121: alt allele binds more; QBiC-SELEX detects a change (|z| above the gate). 4.71 TPM, rank 767 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 97.1th, alt 99.3th percentile of its k-mer coefficients.

<a id="e30"></a>**E30** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2A (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -36.84, effect -1.289: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 9.65 TPM, rank 479 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.5th, alt 96.5th percentile of its k-mer coefficients.

<a id="e31"></a>**E31** qbic_screen, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> TFAP2C (AP-2, 4 models; QBiC-SELEX coverage: own model): best model TFAP2E_FL_TCAAAC40NAAC_KW_yin2017_1_3_7mer (a CIS-BP-mapped model of TFAP2E), z -36.84, effect -1.289: ref allele binds more; QBiC-SELEX detects a change (|z| above the gate). 6.49 TPM, rank 631 of 1626 TFs in DepMap:subtype=Glioblastoma (median of 54 lines). Occupancy: unknown (ENCODE never assayed this TF). Best model's site strength: ref 99.5th, alt 96.5th percentile of its k-mer coefficients.

<a id="e32"></a>**E32** chip_peaks (not tested), ENCODE experiment search; ReMap 2022 (UCSC track ReMapTFs) (https://www.encodeproject.org/search/?type=Experiment&assay_title=TF+ChIP-seq&status=released&assembly=GRCh38&format=json&limit=all&field=target.label&field=biosample_ontology.term_name&field=accession; retrieved local)

> ENCODE has no GABPA ChIP-seq experiment in biosamples matching 'glioblastoma', so ENCODE says nothing about it there, for or against. ENCODE assayed GABPA in: A549, GM12878, H1, HL-60, HeLa-S3, HepG2, K562, MCF-7, SK-N-SH, liver. ReMap 2022 (published ChIP-seq, reprocessed): 4 GABPA peaks contain the variant, in 2 biosamples: Hep-G2 (ENCSR000BJK, ENCSR269TNX, GSE72082); SK-N-SH (ENCSR000BTG). 0 of them in biosamples matching 'glioblastoma'.

<a id="e33"></a>**E33** qbic_tf_detail, QBiC-SELEX 1.0.0 primary collection (997 models) (cache/qbic.sqlite; retrieved local)

> {"tf":"GABPA","symbol":"GABPA","via":"hgnc_symbol","notes":[],"coverage":"own_model","variant":"chr5:1295113:G>A","gate_p":5.02e-05,"models":[{"model":"GABPA_FL_TC40NGCGATT_YWL_jolma2025_0_2_7mer","mapping":"own","group":"G003 Ets, 18 models","quality":0.658,"effect":4.01,"z":68.47,"p":0.0,"rank_abs_z":"5/997","passed_gate":true,"site_strength":{"ref_percentile":96.3,"alt_percentile":99.8,"k":7}},{"model":"ELF1_FL_TATGAC40NTCA_KW_yin2017_0_2_7mer","mapping":"CIS-BP (ELF1)","group":"G003 Ets, 18 models","quality":0.615,"effect":2.514,"z":124.32,"p":0.0,"rank_abs_z":"2/997","passed_gate":true,"site_strength":{"ref_percentile":92.6,"alt_percentile":100.0,"k":7}},{"model":"ELF2_eDBD_TGAAAT40NCAA_KR_yin2017_0_4_7mer","mapping":"CIS-BP (ELF2)","group":"G003 Ets, 18 models","quality":0.896,"effect":4.515,"z":35.9,"p":2.7e-282,"rank_abs_z":"15/997","passed_gate":true,"site_strength":{"ref_percentile":97.8,"alt_percentile":100.0,"k":7}},{"model":"ELF4_eDBD_TGCGGT40NTCA_KAN_yin2017_0_4_7mer","mapping":"CIS-BP (ELF4)","group":"G003 Ets, 18 models","quality":0.732,"effect":3.97,"z":85.47,"p":0.0,"rank_abs_z":"3/997","passed_gate":true,"site_strength":{"ref_percentile":97.0,"alt_percentile":100.0,"k":7}},{"model":"ELK1_NA_TCGGAA20NAGT_ESAG_yang2017_1_3_7mer","mapping":"CIS-BP (ELK1)","group":"G003 Ets, 18 models","quality":0.779,"effect":1.363,"z":12.45,"p":1.4e-35,"rank_abs_z":"63/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.4,"k":7}},{"model":"ELK3_FL_TTCGAA40NGAC_KX_yin2017_0_4_7mer","mapping":"CIS-BP (ELK3)","group":"G003 Ets, 18 models","quality":0.841,"effect":2.56,"z":31.23,"p":4.6e-214,"rank_abs_z":"16/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":100.0,"k":7}},{"model":"ELK4_FL_TCCGCC40NTCA_KAE_yin2017_0_3_7mer","mapping":"CIS-BP (ELK4)","group":"G003 Ets, 18 models","quality":0.921,"effect":3.273,"z":56.2,"p":0.0,"rank_abs_z":"7/997","passed_gate":true,"site_strength":{"ref_percentile":92.2,"alt_percentile":99.6,"k":7}},{"model":"ERF_NA_TCAGAG20NCG_ESW_yang2017_1_4_7mer","mapping":"CIS-BP (ERF)","group":"G003 Ets, 18 models","quality":0.729,"effect":0.63,"z":23.53,"p":2.2e-122,"rank_abs_z":"23/997","passed_gate":true,"site_strength":{"ref_percentile":96.9,"alt_percentile":99.7,"k":7}},{"model":"ERG_NA_TCTACA20NCAG_ESAG_yang2017_1_4_7mer","mapping":"CIS-BP (ERG)","group":"G003 Ets, 18 models","quality":0.881,"effect":2.323,"z":22.12,"p":2e-108,"rank_abs_z":"26/997","passed_gate":true,"site_strength":{"ref_percentile":98.2,"alt_percentile":99.8,"k":7}},{"model":"ETS1_NA_TGTAAA20NGA_ESAF_yang2017_0_4_7mer","mapping":"CIS-BP (ETS1)","group":"G003 Ets, 18 models","quality":0.873,"effect":1.97,"z":40.46,"p":0.0,"rank_abs_z":"12/997","passed_gate":true,"site_strength":{"ref_percentile":98.7,"alt_percentile":100.0,"k":7}}],"n_models_trimmed":8}

<a id="e34"></a>**E34** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABPA%20TERT%20promoter%20glioblastoma&format=json&pageSize=8&resultType=core; retrieved 2026-10-28T01:05:59+00:00)

> Europe PMC: 147 hits for 'GABPA TERT promoter glioblastoma'; top 8 with PMIDs:
> PMID 40513567 (2025): The immortality mechanism of TERT promoter mutant cancers is self-reinforcing and reversible.
> PMID 41975789 (2026): Frequency of TERT Promoter Mutations in Ameloblastoma: A Retrospective Study.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 41776093 (2026): Unrevealing the dual role of paired box and sex determining region Y related high mobility group box in glioblastoma.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 41155227 (2025): From Transcription Factors Dysregulation to Malignancy: In Silico Reconstruction of Cancer's Foundational Drivers-The Eternity Triangle.
> PMID 39228402 (2024): Role of post-translational modifications of Sp1 in cancer: state of the art.
> PMID 37918959 (2023): E4F1 and ZNF148 are transcriptional activators of the -57A &gt; C and wild-type &lt;i&gt;TERT&lt;/i&gt; promoter.

<a id="e35"></a>**E35** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=GABPA%20GABP%20TERT%20promoter%20mutation%20binding&format=json&pageSize=8&resultType=core; retrieved 2026-10-28T01:08:26+00:00)

> Europe PMC: 83 hits for 'GABPA GABP TERT promoter mutation binding'; top 8 with PMIDs:
> PMID 41817108 (2026): DDX21 Links &lt;i&gt;BRAF&lt;sup&gt;V600E&lt;/sup&gt;&lt;/i&gt; and TERT to Promote Thyroid Cancer Progression.
> PMID 40513567 (2025): The immortality mechanism of TERT promoter mutant cancers is self-reinforcing and reversible.
> PMID 39557834 (2024): Mechanistic basis of atypical TERT promoter mutations.
> PMID 42650008 (2026): ERK Signaling in Thyroid Cancer: Lineage Suppression, Epigenetic Reprogramming, and Theranostic Reversal.
> PMID 40469184 (2025): Application and recent advances in conventional biomarkers for the prognosis of papillary thyroid carcinoma.
> PMID 40822359 (2025): AURKB and PI3K/AKT/mTOR pathways converge to regulate &lt;i&gt;TERT&lt;/i&gt; expression.
> PMID 38033865 (2023): Reactivation of telomerase reverse transcriptase expression in cancer: the role of TERT promoter mutations.
> PMID 40860184 (2025): Blocking interplay between TERT and c-Myc: a new therapeutic strategy for &lt;i&gt;BRAF&lt;sup&gt;V600E&lt;/sup&gt;/pTERT&lt;/i&gt; double mutated tumors.

<a id="e35a"></a>**E35a** literature_search, Europe PMC abstract, PMID 41817108 (https://europepmc.org/article/MED/41817108; retrieved 2026-10-28T01:08:26+00:00)

> GABPA bound to the promoter of DDX21, and knockdown of GABPA or GABPB1 suppressed DDX21 promoter activity and transcription.

<a id="e35b"></a>**E35b** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-28T01:08:26+00:00)

> TERT promoter (TERTp) mutations create a de novo E26 transformation-specific (ETS) transcription factor binding motif.

<a id="e35c"></a>**E35c** literature_search, Europe PMC abstract, PMID 40513567 (https://europepmc.org/article/MED/40513567; retrieved 2026-10-28T01:08:26+00:00)

> Here, we analyzed 53 cell lines representing 16 cancer types and 6 recurrent TERTp mutations and found that the GA-binding protein (GABP) tetramer is responsible for promoter activation in all cases.

<a id="e35d"></a>**E35d** literature_search, Europe PMC abstract, PMID 39557834 (https://europepmc.org/article/MED/39557834; retrieved 2026-10-28T01:08:26+00:00)

> Canonical TERTp mutations create de novo binding sites for ETS family transcription factors that induce favourable conditions for DNA damage formation by UV light, thus creating a hotspot effect but only after a first mutational hit.

<a id="e35e"></a>**E35e** literature_search, Europe PMC abstract, PMID 38033865 (https://europepmc.org/article/MED/38033865; retrieved 2026-10-28T01:08:26+00:00)

> These mutations promote TERT gene expression by multiple mechanisms, including the generation of novel binding sites for nuclear transcription factors, displacement of negative regulators from DNA G-quadruplexes, recruitment of epigenetic activators and disruption of long-range interactions between TERT locus and telomeres.

<a id="e36"></a>**E36** gene_dependency, DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for GABPA (0 = no effect, -1 = median common-essential; < -0.5 called dependent). CNS/Brain lineage, 50 lines: median -0.87, 94% dependent. All 1183 lines: median -0.87, 97% dependent. common-essential in DepMap: a strong knockout effect here is not evidence for a lineage-specific role.

<a id="e37"></a>**E37** gene_dependency (tested, negative), DepMap CRISPRGeneEffect (Biomni copy) and CRISPRInferredCommonEssentials (Public 26Q3) (local files; retrieved local)

> DepMap CRISPR gene effect for TERT (0 = no effect, -1 = median common-essential; < -0.5 called dependent). CNS/Brain lineage, 50 lines: median -0.00, 2% dependent. All 1183 lines: median -0.02, 1% dependent.

<a id="e38"></a>**E38** gene_disease (failed), Open Targets (; retrieved local)

> Open Targets lookup failed: no disease matches 'Glioblastoma, melanoma, bladder'

<a id="e39"></a>**E39** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=ETV3%20TERT%20promoter&format=json&pageSize=8&resultType=core; retrieved 2026-10-28T01:10:19+00:00)

> Europe PMC: 18 hits for 'ETV3 TERT promoter'; top 8 with PMIDs:
> PMID 40998781 (2025): Disease-linked regulatory DNA variants and homeostatic transcription factors in epidermis.
> PMID 40565279 (2025): Molecular Determinants of the Human Retinal Pigment Epithelium Cell Fate and Potential Pharmacogenomic Targets for Precision Medicine.
> PMID 37520692 (2023): Identifying functional regulatory mutation blocks by integrating genome sequencing and transcriptome data.
> PMID 37967508 (2023): Super-enhancer driven SOX2 promotes tumor formation by chromatin re-organization in nasopharyngeal carcinoma.
> PMID 35568649 (2022): Emerging mechanisms of telomerase reactivation in cancer.
> PMID 33851100 (2021): Pan-cancer noncoding genomic analysis identifies functional <i>CDC20</i> promoter mutation hotspots.
> PMID 35927480 (2022): PROBER identifies proteins associated with programmable sequence-specific DNA in living cells.
> PMID 25977370 (2015): Cancer. The transcription factor GABP selectively binds and activates the mutant TERT promoter in cancer.

<a id="e39a"></a>**E39a** literature_search, Europe PMC abstract, PMID 35568649 (https://europepmc.org/article/MED/35568649; retrieved 2026-10-28T01:10:19+00:00)

> Mutations in the promoter of human telomerase reverse transcriptase (hTERT) result in hyperactivation of hTERT.

<a id="e39b"></a>**E39b** literature_search, Europe PMC abstract, PMID 35568649 (https://europepmc.org/article/MED/35568649; retrieved 2026-10-28T01:10:19+00:00)

> Initially, the mutations were understood to reactivate hTERT by generating novel E26 transformation-specific (ETS) binding sites.

<a id="e39c"></a>**E39c** literature_search, Europe PMC abstract, PMID 35927480 (https://europepmc.org/article/MED/35927480; retrieved 2026-10-28T01:10:19+00:00)

> PROBER identified alterations in regulator associations due to cancer hotspot mutations in the hTERT promoter, indicating that these mutations increase promoter association with specific gene activators.

<a id="e39d"></a>**E39d** literature_search, Europe PMC abstract, PMID 25977370 (https://europepmc.org/article/MED/25977370; retrieved 2026-10-28T01:10:19+00:00)

> Multiple cancer types, including up to 83% of glioblastomas (GBMs), harbor highly recurrent TERT promoter mutations of unknown function but specific to two nucleotide positions.

<a id="e39e"></a>**E39e** literature_search, Europe PMC abstract, PMID 25977370 (https://europepmc.org/article/MED/25977370; retrieved 2026-10-28T01:10:19+00:00)

> Tandem flanking native E26 transformation-specific motifs critically cooperate with these mutations to activate TERT, probably by facilitating GABP heterotetramer binding.

<a id="e40"></a>**E40** literature_search, Europe PMC REST (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=TFAP2C%20TERT%20promoter%20repressor&format=json&pageSize=8&resultType=core; retrieved 2026-10-28T01:10:26+00:00)

> Europe PMC: 30 hits for 'TFAP2C TERT promoter repressor'; top 8 with PMIDs:
> PMID 41129222 (2025): Genetic regulation of the estrogen receptor and inherited predisposition to breast cancer.
> PMID 41437062 (2025): Histone lysine demethylases in breast cancer: molecular mechanisms, biological functions, and therapeutic intervention.
> PMID 40862123 (2025): Advances in &lt;i&gt;in vitro&lt;/i&gt; oocyte generation from pluripotent stem cells and ovarian stem cells.
> PMID 37291585 (2023): Crucial role of the transcription factors family activator protein 2 in cancer: current clue and views.
> PMID 41514294 (2026): Modeling mammalian meiosis with pluripotent stem cells: progress and challenges.
> PMID 39562537 (2024): Chromatin landscape dynamics during reprogramming towards human naïve and primed pluripotency reveals the divergent function of PRDM1 isoforms.
> PMID 40448182 (2025): Biological roles of enhancer RNA m6A modification and its implications in cancer.
> PMID 36184610 (2022): Germline stem cells in human.

<a id="e40a"></a>**E40a** literature_search, Europe PMC abstract, PMID 41129222 (https://europepmc.org/article/MED/41129222; retrieved 2026-10-28T01:10:26+00:00)

> At the site with the most striking effect, the breast-cancer-linked allele was associated with increased binding by transcription factor AP2-gamma TFAP2C in both MCF7 and T47D cells.

<a id="e40b"></a>**E40b** literature_search, Europe PMC abstract, PMID 37291585 (https://europepmc.org/article/MED/37291585; retrieved 2026-10-28T01:10:26+00:00)

> The TFAP2 family consists of five DNA-binding proteins, including TFAP2A, TFAP2B, TFAP2C, TFAP2D and TFAP2E.

<a id="e40c"></a>**E40c** literature_search, Europe PMC abstract, PMID 37291585 (https://europepmc.org/article/MED/37291585; retrieved 2026-10-28T01:10:26+00:00)

> As a transcription factor, TFAP2 regulates the downstream targets directly by binding to their regulatory region.
