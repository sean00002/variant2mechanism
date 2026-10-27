# rs1421085 and Obesity (FTO)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 2 model calls; 49 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. H0: null_model (p = 0.55)

Null chain: no TF-mediated effect of this variant.

Predictions: ARID5B ChIP or EMSA signal at rs1421085 is genotype-independent in adipocytes.; IRX3/IRX5 expression is not allele-dependently regulated by rs1421085 in adipocytes.

Falsified if: Adipocyte ARID5B binding at rs1421085 differs between T and C alleles.; Adipocyte IRX3/IRX5 expression is allele-dependent at rs1421085.

### 2. H1: ARID5B_loss_derepresses_IRX3_IRX5 (p = 0.25)

TF ARID5B (QBiC-SELEX coverage not_in_coverage), ref allele binds more; element FTO intron 1 enhancer; gene IRX3; cell type adipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the T allele more strongly than the C allele at rs1421085; ARID5B is chosen from known adipocyte enhancer/motif literature over related TFs, and no evidence IDs are supplied here. | missing | none |
| element | rs1421085 lies in an adipocyte enhancer in FTO intron 1. | missing | none |
| gene | Loss of ARID5B binding on the C allele increases IRX3 and IRX5 expression. | missing | none |
| cell_type | This occurs in subcutaneous adipocytes or pre-adipocytes. | missing | none |
| phenotype | Increased IRX3/IRX5 expression reduces thermogenesis and increases obesity risk. | missing | none |

Predictions: ARID5B binds the T allele more strongly than the C allele at rs1421085.; The obesity-risk C allele associates with higher IRX3 and IRX5 expression in adipocytes.

Falsified if: ARID5B ChIP or EMSA shows no T-over-C binding difference at rs1421085.

### 3. H2: ARID5B_loss_increases_FTO_expression (p = 0.12)

TF ARID5B (QBiC-SELEX coverage not_in_coverage), ref allele binds more; element FTO intron 1 enhancer; gene FTO; cell type adipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the T allele more strongly than the C allele at rs1421085; ARID5B is chosen from known adipocyte enhancer/motif literature, with no evidence IDs supplied here. | missing | none |
| element | rs1421085 lies in an adipocyte enhancer in FTO intron 1. | missing | none |
| gene | Loss of ARID5B binding on the C allele increases FTO expression. | missing | none |
| cell_type | This occurs in subcutaneous adipocytes or pre-adipocytes. | missing | none |
| phenotype | Increased FTO expression increases obesity risk. | missing | none |

Predictions: ARID5B binds the T allele more strongly than the C allele at rs1421085.; FTO expression is higher on the C allele than on the T allele in adipocytes.

Falsified if: FTO expression is not allele-dependent at rs1421085 in adipocytes.

### 4. H3: CTCF_insulator_disruption (p = 0.08)

TF CTCF (QBiC-SELEX coverage own_model), alt allele binds more; element FTO intron 1 enhancer; gene IRX3; cell type adipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CTCF binds the C allele more strongly than the T allele at rs1421085; no CTCF QBiC-SELEX model is cited here. | missing | none |
| element | rs1421085 lies in an adipocyte insulator or enhancer element in FTO intron 1. | missing | none |
| gene | Altered CTCF binding changes IRX3/IRX5 chromatin insulation and expression. | missing | none |
| cell_type | This occurs in subcutaneous adipocytes or pre-adipocytes. | missing | none |
| phenotype | Altered IRX3/IRX5 expression changes thermogenesis and obesity risk. | missing | none |

Predictions: CTCF binding at rs1421085 differs between the T and C alleles.; Altered CTCF occupancy changes IRX3/IRX5 insulation or expression in adipocytes.

Falsified if: CTCF ChIP shows no genotype-dependent binding at rs1421085.

## Prediction matrix

| Test | Cost | Separates top two | H0 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B binding at rs1421085 | low | yes | Equal binding or no ARID5B occupancy | T allele shows stronger ARID5B binding than C |  |  |
| Adipocyte eQTL for IRX3/IRX5 by rs1421085 genotype | medium | no | No allelic effect on IRX3/IRX5 | C allele associates with higher IRX3/IRX5 |  |  |

## Next experiment

Allele-specific EMSA with adipocyte nuclear extract using T and C probes spanning rs1421085; this is the cheapest single assay that separates H1 (ARID5B binds T more than C) from H0 (no genotype-dependent ARID5B binding).

## Flags

- none

## Evidence
