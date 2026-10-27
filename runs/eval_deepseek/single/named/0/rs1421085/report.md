# rs1421085 and Obesity (FTO)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 2 model calls; 50 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. H1: ARID5B binds the ref-T allele of the FTO intronic enhancer; loss of binding on alt-C derepresses IRX3/IRX5 in subcutaneous preadipocytes and shifts adipogenesis toward white fat (p = 0.50)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element FTO intronic enhancer; gene IRX3/IRX5; cell type subcutaneous preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the ref-T allele more strongly than the alt-C allele at rs1421085. | missing | none |
| element | rs1421085 lies in an FTO intronic enhancer whose ARID5B-binding motif is disrupted by alt-C. | missing | none |
| gene | Loss of ARID5B occupancy on alt-C relieves repression and increases IRX3/IRX5 expression. | missing | none |
| cell_type | The enhancer is active and the effect occurs in subcutaneous adipose preadipocytes. | missing | none |
| phenotype | Higher IRX3/IRX5 biases adipocyte precursors toward white adipogenesis, contributing to obesity. | missing | none |

Predictions: ARID5B binds the ref-T probe more strongly than the alt-C probe; alt-C increases enhancer reporter activity in preadipocytes; alt-C increases IRX3/IRX5 expression in subcutaneous preadipocytes; alt-C favors white adipogenesis and reduces browning capacity

Falsified if: ARID5B binding is not allele-specific at rs1421085 in preadipocyte extracts.; The alt-C enhancer reporter is not more active than ref-T in preadipocytes.; alt-C does not increase IRX3/IRX5 in preadipocytes.

### 2. H0: No TF-mediated effect of rs1421085: the obesity association reflects a linked causal variant in LD or a passenger variant, with no allele-specific TF binding at this position (p = 0.28)

Null chain: no TF-mediated effect of this variant.

Predictions: ARID5B binding is not allele-specific at rs1421085; The ref-T and alt-C enhancer reporters have equal activity in preadipocytes; IRX3/IRX5 and FTO are not allele-specifically expressed in preadipocytes; The obesity signal is attributable to a different variant in linkage disequilibrium

Falsified if: Allele-specific ARID5B binding and allele-specific enhancer activity are demonstrated in preadipocytes.; The alt-C allele reproducibly changes IRX3/IRX5 or FTO expression in the relevant cell type.

### 3. H2: ARID5B loss at the same FTO intronic enhancer directly changes FTO expression rather than IRX3/IRX5 (p = 0.12)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element FTO intronic enhancer; gene FTO; cell type subcutaneous preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the ref-T allele more strongly than the alt-C allele at rs1421085. | missing | none |
| element | rs1421085 lies in an FTO intronic enhancer whose ARID5B motif is disrupted by alt-C. | missing | none |
| gene | The enhancer directly regulates FTO expression in cis. | missing | none |
| cell_type | The effect occurs in subcutaneous adipose preadipocytes. | missing | none |
| phenotype | Altered FTO dosage affects body-weight regulation and contributes to obesity. | missing | none |

Predictions: ARID5B binds the ref-T probe more strongly than the alt-C probe; alt-C changes FTO expression in preadipocytes; IRX3/IRX5 expression is not allele-specifically changed in the same cells

Falsified if: FTO expression is not allele-specific in preadipocytes.; IRX3/IRX5, not FTO, is the allele-specific target of the enhancer.

### 4. H3: ARID5B loss at the FTO intronic enhancer acts on IRX3 in hypothalamic neurons to alter energy balance rather than in adipocytes (p = 0.10)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element FTO intronic enhancer; gene IRX3; cell type hypothalamic neuron.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the ref-T allele more strongly than the alt-C allele at rs1421085. | missing | none |
| element | rs1421085 lies in an FTO intronic enhancer whose ARID5B motif is disrupted by alt-C. | missing | none |
| gene | The enhancer regulates IRX3 expression. | missing | none |
| cell_type | The relevant effect occurs in hypothalamic neurons. | missing | none |
| phenotype | Altered hypothalamic IRX3 changes appetite and energy balance, contributing to obesity. | missing | none |

Predictions: ARID5B binding is stronger on ref-T than alt-C in hypothalamic cell extracts; alt-C increases IRX3 in hypothalamic neurons; IRX3/IRX5 is not allele-specifically changed in subcutaneous preadipocytes

Falsified if: ARID5B or IRX3 is not expressed in the relevant hypothalamic cells.; The allele-specific effect is present only in adipocytes and absent in hypothalamic models.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H0 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B binding at rs1421085 (EMSA or oligo pulldown with preadipocyte nuclear extract, ARID5B immunodepletion) | low | yes | ref-T binds ARID5B more strongly than alt-C | No allele-specific ARID5B binding |  |  |
| Allele-specific enhancer reporter activity in subcutaneous preadipocytes | low | yes | alt-C > ref-T activity | no allelic difference |  |  |
| Allele-specific IRX3/IRX5 expression in subcutaneous preadipocytes (e.g. ASE or CRISPR-edited isogenic lines) | medium | yes | alt-C increases IRX3/IRX5 | no allelic change |  |  |
| Allele-specific FTO expression in preadipocytes | medium | no | no FTO allelic change |  | alt-C changes FTO dosage with no IRX3/IRX5 change |  |
| Allele-specific IRX3 in hypothalamic neurons (or hypothalamic-relevant model) | high | no | no hypothalamic allelic effect |  |  | allele-specific IRX3 change only in hypothalamic cells |

## Next experiment

Single cheapest decisive assay: an allele-specific enhancer reporter (ref-T vs alt-C fragment cloned upstream of a minimal promoter–luciferase, or an MPRA oligo containing rs1421085) transfected into subcutaneous preadipocytes or a preadipocyte line. It separates H1 (alt-C increases enhancer activity) from H0 (no allelic difference) and from H3 (effect requires hypothalamic, not adipose, context); a positive result then needs IRX3/IRX5 expression measurement to separate H1 from H2.

## Flags

- none

## Evidence
