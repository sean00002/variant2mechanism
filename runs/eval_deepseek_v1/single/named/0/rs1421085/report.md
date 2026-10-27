# rs1421085 and Obesity (FTO)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 69 s.

Variant `chr16:53767042:T>C` (germline); expression context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes).

## Ranked chains

### 1. H1: ARID5B binding at the rs1421085 enhancer regulates IRX3 (p = 0.55)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element rs1421085 enhancer; gene IRX3; cell type preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the rs1421085 T allele more strongly than the C allele. | missing | none |
| element | The rs1421085 region is an enhancer active in preadipocytes. | missing | none |
| gene | The enhancer regulates IRX3. | missing | none |
| cell_type | Preadipocytes mediate the effect. | missing | none |
| phenotype | IRX3 level influences obesity. | missing | none |

Predictions: rs1421085 T>C alters ARID5B binding in preadipocytes; IRX3 expression changes in cis; IRX3 knockdown rescues the phenotype

Falsified if: ARID5B binding is not allele-specific in preadipocytes; IRX3 is not the regulated gene

### 2. H2: ARID5B binding at the rs1421085 enhancer regulates IRX5 (p = 0.30)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element rs1421085 enhancer; gene IRX5; cell type preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the rs1421085 T allele more strongly than the C allele. | missing | none |
| element | The rs1421085 region is an enhancer active in preadipocytes. | missing | none |
| gene | The enhancer regulates IRX5. | missing | none |
| cell_type | Preadipocytes mediate the effect. | missing | none |
| phenotype | IRX5 level influences obesity. | missing | none |

Predictions: rs1421085 T>C alters ARID5B binding in preadipocytes; IRX5 expression changes in cis; IRX5 knockdown rescues the phenotype

Falsified if: ARID5B binding is not allele-specific in preadipocytes; IRX5 is not the regulated gene

### 3. H3: ARID5B binding at the rs1421085 enhancer regulates FTO (p = 0.13)

TF ARID5B (stated coverage not_checked; registry not_in_coverage), ref allele binds more; element rs1421085 enhancer; gene FTO; cell type preadipocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ARID5B binds the rs1421085 T allele more strongly than the C allele. | missing | none |
| element | The rs1421085 region is an enhancer active in preadipocytes. | missing | none |
| gene | The enhancer regulates FTO. | missing | none |
| cell_type | Preadipocytes mediate the effect. | missing | none |
| phenotype | FTO level influences obesity. | missing | none |

Predictions: rs1421085 T>C alters ARID5B binding in preadipocytes; FTO expression changes in cis; FTO knockdown rescues the phenotype

Falsified if: ARID5B binding is not allele-specific in preadipocytes; FTO is not the regulated gene

### 4. H0: No TF-mediated effect of rs1421085 (p = 0.02)

Null chain: no TF-mediated effect of this variant.

Predictions: rs1421085 T>C does not alter ARID5B binding in preadipocytes; No cis-expression change of IRX3, IRX5, or FTO; Association is due to linkage disequilibrium with a causal variant

Falsified if: ARID5B binding is allele-specific in preadipocytes; A cis-expression change is detected

## Prediction matrix

| Test | Cost | Separates top two | H1 | H2 | H3 | H0 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific ARID5B binding, preadipocytes | low | yes | ARID5B binding is stronger on ref T than alt C | ARID5B binding is stronger on ref T than alt C |  | No allele-specific ARID5B binding |

## Next experiment

In preadipocytes heterozygous for rs1421085, siRNA knockdown IRX3 versus IRX5 and measure thermogenic markers (UCP1, PPARGC1A) and lipid accumulation.

## Flags

- none

## Evidence
