# rs339331 and Prostate cancer (6q22)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 51 s.

Variant `chr6:116888889:T>C` (germline); expression context: DepMap:ACH-000977 (LNCaP clone FGC).

## Ranked chains

### 1. C1: HOXB13 binds the ref T allele more and activates RFX6 (p = 0.43)

TF HOXB13 (stated coverage not_checked; registry own_model), ref allele binds more; element intronic RFX6 enhancer; gene RFX6; cell type prostate epithelial/LNCaP.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 binds the ref T allele more strongly than the alt C allele at rs339331; QBiC-SELEX coverage is not_checked. | missing | none |
| element | rs339331 lies in a prostate-active intronic enhancer in RFX6, and the ref T allele increases enhancer activity. | missing | none |
| gene | The ref T enhancer increases RFX6 expression. | missing | none |
| cell_type | The effect is observed in prostate epithelial/LNCaP cells. | missing | none |
| phenotype | Higher RFX6 increases prostate cancer risk at 6q22. | missing | none |

Predictions: HOXB13 binds the ref T allele more than the alt C allele; The ref T allele increases enhancer activity in prostate cells; RFX6 expression is higher with ref T; HOXB13 knockdown reduces RFX6; The risk-associated ref allele increases prostate cancer risk via higher RFX6

Falsified if: HOXB13 does not bind rs339331 allele-specifically; Ref T does not increase enhancer activity or RFX6 expression; HOXB13 knockdown does not affect RFX6

### 2. C2: Null: no TF-mediated allelic effect (p = 0.32)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs339331; No allelic enhancer activity difference; No allele-specific RFX6 expression difference; Any disease association is due to a linked causal variant or is a passenger effect

Falsified if: An allele-specific TF binding is demonstrated; An allele-specific enhancer or RFX6 expression effect is demonstrated

### 3. C3: AR binds the ref T allele more and activates RFX6 (p = 0.14)

TF AR (stated coverage not_checked; registry own_model), ref allele binds more; element intronic RFX6 enhancer; gene RFX6; cell type prostate epithelial/LNCaP.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | AR binds the ref T allele more strongly than the alt C allele at rs339331; QBiC-SELEX coverage is not_checked. | missing | none |
| element | rs339331 is in a prostate-active intronic RFX6 enhancer whose activity is increased by the ref T allele. | missing | none |
| gene | The AR-bound ref T enhancer increases RFX6 expression. | missing | none |
| cell_type | The effect occurs in prostate epithelial/LNCaP cells. | missing | none |
| phenotype | Higher RFX6 increases prostate cancer risk. | missing | none |

Predictions: AR binds the ref T allele more than the alt C allele; The ref T allele increases enhancer activity in prostate cells; RFX6 expression is higher with ref T; AR knockdown reduces RFX6; Higher RFX6 increases prostate cancer risk

Falsified if: AR does not bind rs339331 allele-specifically; AR knockdown does not affect RFX6; HOXB13, not AR, accounts for the allele-specific binding

### 4. C4: HOXB13 binds the ref T allele more but represses RFX6 (p = 0.11)

TF HOXB13 (stated coverage not_checked; registry own_model), ref allele binds more; element intronic RFX6 element; gene RFX6; cell type prostate epithelial/LNCaP.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HOXB13 binds the ref T allele more strongly than the alt C allele at rs339331; QBiC-SELEX coverage is not_checked. | missing | none |
| element | The ref T allele increases HOXB13 occupancy at an intronic RFX6 element. | missing | none |
| gene | HOXB13 binding represses RFX6 expression. | missing | none |
| cell_type | The repression occurs in prostate epithelial/LNCaP cells. | missing | none |
| phenotype | Lower RFX6 impairs prostate epithelial differentiation and increases prostate cancer risk. | missing | none |

Predictions: HOXB13 binds the ref T allele more than the alt C allele; The ref T allele increases HOXB13 occupancy at the enhancer; RFX6 expression is lower with ref T; HOXB13 knockdown increases RFX6; Lower RFX6 alters prostate epithelial differentiation and increases cancer risk

Falsified if: HOXB13 does not bind rs339331 allele-specifically; Ref T does not lower RFX6; HOXB13 knockdown does not increase RFX6

## Prediction matrix

| Test | Cost | Separates top two | C1 | C2 | C3 | C4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific binding by named TF | low | yes | HOXB13 binds ref T more than alt C | No allele-specific HOXB13 binding | AR binds ref T more than alt C | HOXB13 binds ref T more than alt C |
| Allele-specific reporter in prostate/LNCaP cells | medium | no | Ref T enhancer activity > alt C | No allelic enhancer difference | Ref T enhancer activity > alt C | Ref T enhancer activity > alt C |
| RFX6 expression after HOXB13 knockdown in LNCaP | medium | no | RFX6 decreases | No change | RFX6 decreases | RFX6 increases |

## Next experiment

Allele-specific EMSA with recombinant HOXB13 and double-stranded probes spanning rs339331 (ref T vs alt C); a stronger HOXB13 shift for ref T supports C1 over the null.

## Flags

- none

## Evidence
