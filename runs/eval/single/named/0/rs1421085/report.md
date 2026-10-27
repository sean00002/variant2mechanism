# rs1421085 and Obesity (FTO)

Configuration `single`, named mode, seed 0. Models: generator claude-opus-5, critic claude-sonnet-5-5, summariser claude-haiku-5-5. Cost $0.13 over 1 model calls; 54 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. H1: Alt C disrupts ARID5B repressor binding at an FTO intron-1 adipocyte enhancer, derepressing IRX3/IRX5 (p = 0.45)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element FTO intron 1 (~chr16:53.767 Mb) conserved enhancer active in preadipocytes/adipocytes; gene IRX3 and IRX5 (long-range targets, not FTO itself); cell type Adipocyte progenitors / preadipocytes (subcutaneous adipose).

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref T allele creates an AT-rich motif bound by the ARID-family repressor ARID5B; the alt C allele weakens this binding. ARID5B chosen within the AT-rich ARID binding group because it is the ARID member expressed in adipose progenitors and reported at this locus; coverage in QBiC-SELEX not checked here. | missing | none |
| element | The variant sits in a conserved enhancer within FTO intron 1 that loops to the IRX3/IRX5 promoters; loss of ARID5B occupancy converts the element from repressed to active. | missing | none |
| gene | Enhancer derepression raises IRX3 and IRX5 expression in cis during early adipocyte differentiation. | missing | none |
| cell_type | The effect is restricted to adipocyte precursors at the beige/white fate decision window, not to mature adipocytes or brain. | missing | none |
| phenotype | Higher IRX3/IRX5 shifts cells from beige thermogenic to white lipid-storing programme (lower UCP1, lower mitochondrial respiration), increasing fat mass and BMI. | missing | none |

Predictions: ARID5B ChIP or EMSA shows allele-specific occupancy favouring T; CRISPR repair C->T in risk-allele adipocytes restores UCP1 and respiration; ARID5B knockdown on the T allele phenocopies the C allele; IRX3/IRX5, not FTO, show allelic expression imbalance

Falsified if: No allele-specific ARID5B binding by EMSA/ChIP; Editing the single base changes no gene expression; IRX3/IRX5 unchanged while FTO itself is the only cis-regulated gene

### 2. H5: Null: rs1421085 is a passenger in a strong LD block and another variant carries the causal regulatory effect (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: Single-base editing of rs1421085 alone changes no target gene expression; MPRA shows no allelic activity for this variant but does for a neighbouring LD partner (e.g. rs1558902, rs9939609, rs8050136); No allele-specific TF occupancy at this position

Falsified if: Isogenic single-base edit of C->T reverses IRX3/IRX5 expression and the cellular phenotype; Reproducible allele-specific TF binding at this exact base

### 3. H2: Alt C creates/strengthens a CUX1 (CUT-homeodomain) site that activates the same enhancer (p = 0.15)

TF CUX1 (stated coverage not_checked; registry own_model), alt allele binds more; element Same FTO intron-1 enhancer; gene IRX3/IRX5; cell type Preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The C allele generates a CUT/homeodomain-like site; CUX1 chosen within that specificity group as the broadly expressed family member in adipose tissue. QBiC coverage not checked. | missing | none |
| element | Gain of an activator at the intron-1 element increases enhancer output rather than relieving repression. | missing | none |
| gene | IRX3/IRX5 transcription rises through activator recruitment. | missing | none |
| cell_type | Acts in preadipocytes where CUX1 (p110/p200 isoforms) is present. | missing | none |
| phenotype | Same downstream white-adipocyte shift and increased adiposity. | missing | none |

Predictions: CUX1 ChIP shows C-allele-preferential occupancy; CUX1 knockdown lowers IRX3/IRX5 specifically on the C allele; Reporter with C allele is more active only when CUX1 is co-expressed

Falsified if: No CUX1 binding at the element; Knockdown of CUX1 has no allele-specific effect; Allelic effect is loss-of-binding rather than gain

### 4. H3: Allelic effect on a CTCF/cohesin-dependent contact that changes FTO-IRX3 looping (p = 0.08)

TF CTCF (stated coverage not_checked; registry own_model), ref allele binds more; element Intron-1 element acting as a loop anchor within the FTO TAD; gene IRX3 (and FTO); cell type Adipose/preadipocytes.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Ref T supports stronger CTCF occupancy at a nearby anchor; alt C weakens it. CTCF is the sole TF with this specificity, so no within-group choice is needed. Coverage not checked. | missing | none |
| element | Weakened anchor changes enhancer-promoter contact frequency across the ~1 Mb FTO-IRX3 domain. | missing | none |
| gene | IRX3 promoter gains contact with distal enhancers, raising its expression. | missing | none |
| cell_type | Loop architecture differences manifest in adipose lineage where the enhancers are active. | missing | none |
| phenotype | Elevated IRX3 reduces thermogenesis and increases adiposity. | missing | none |

Predictions: Allele-specific CTCF ChIP-seq signal at the variant; 4C/Hi-C shows genotype-dependent contact changes; Cohesin depletion abolishes the allelic expression difference

Falsified if: No CTCF motif or occupancy at the variant; Contact maps identical between genotypes; Allelic effect persists after cohesin depletion

### 5. H4: Variant acts on FTO itself via an adipose promoter-proximal regulatory element (p = 0.07)

TF IRF4 (stated coverage not_checked; registry own_model), alt allele binds more; element FTO intron-1 element acting on the FTO promoter; gene FTO; cell type Subcutaneous adipose.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alt C improves an IRF-family site; IRF4 chosen within the IRF specificity group because it is the IRF member with an established adipocyte lipolysis/thermogenesis role. Coverage not checked. | missing | none |
| element | The element behaves as an FTO-proximal enhancer rather than a long-range IRX3 enhancer. | missing | none |
| gene | FTO mRNA levels change in cis in adipose tissue. | missing | none |
| cell_type | Effect seen in mature adipocytes where IRF4 is abundant. | missing | none |
| phenotype | Altered FTO m6A demethylase activity changes adipogenesis and energy intake, raising BMI. | missing | none |

Predictions: FTO shows allele-specific expression in adipose, IRX3/IRX5 do not; FTO eQTL colocalises with the obesity signal in adipose; IRF4 ChIP shows allelic binding

Falsified if: No FTO eQTL at this variant in adipose; IRX3/IRX5 but not FTO show allelic imbalance; No IRF motif disrupted

## Prediction matrix

| Test | Cost | Separates top two | H1 | H5 | H2 | H3 | H4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| EMSA/allele-specific ChIP for ARID5B with T vs C oligos from adipocyte progenitor nuclear extract | low | yes | Stronger ARID5B complex on T | No allelic difference with any extract | No ARID5B difference; any gained complex is on C | No ARID5B difference | No ARID5B difference |
| Isogenic CRISPR single-base conversion (C->T) in human adipocyte progenitors, then RT-qPCR of IRX3, IRX5, FTO, UCP1 | high | yes | IRX3/IRX5 down, UCP1 up; FTO unchanged | No expression change | IRX3/IRX5 down, dependent on CUX1 levels | IRX3 down with altered looping; FTO may also shift | FTO changes, IRX3/IRX5 unchanged |
| MPRA/luciferase of 150 bp T vs C element in preadipocytes | low | no | C allele more active (loss of repression) | No allelic difference | C allele more active, CUX1-dependent | Little or no difference (architectural effect) | C allele more active on an FTO-promoter reporter |
| Allele-specific CTCF ChIP-seq in heterozygous adipose cells | existing data | no | No CTCF allelic signal | No CTCF allelic signal | No CTCF allelic signal | Allelic CTCF imbalance favouring T | No CTCF allelic signal |

## Next experiment

Run a low-cost allele-specific EMSA with supershift (anti-ARID5B, anti-CUX1) using T and C oligos and preadipocyte nuclear extract: a T-preferential ARID5B complex supports H1, no allelic complex at all supports the null H5, and a C-preferential CUX1 complex supports H2.

## Flags

- none

## Evidence
