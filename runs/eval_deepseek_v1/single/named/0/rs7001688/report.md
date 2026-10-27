# rs7001688 and LDL cholesterol

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 33 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. C0_null: No TF-mediated allelic effect; association is explained by a linked causal variant or no causal effect (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs7001688 in hepatocyte-relevant assays.; No allele-specific enhancer/reporter activity difference for rs7001688 itself.; Any CYP7A1 or LDL cholesterol association is driven by a linked variant, not by rs7001688.; rs7001688 behaves as a passenger or marker variant.

Falsified if: A reproducible allele-specific TF binding and enhancer effect is demonstrated for rs7001688.; The allelic reporter effect is abolished by knocking down the named TF.

### 2. C1_HNF4A: HNF4A binding gain at a liver enhancer increases CYP7A1 and lowers LDL cholesterol (p = 0.30)

TF HNF4A (stated coverage not_checked; registry own_model), alt allele binds more; element CYP7A1 liver enhancer; gene CYP7A1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele is predicted to strengthen a hepatocyte HNF4A binding site at rs7001688, so HNF4A binds the alt allele more strongly than the ref G allele. | missing | none |
| element | The allele-specific HNF4A site lies in a liver enhancer that can regulate CYP7A1. | missing | none |
| gene | Increased HNF4A binding at this element increases CYP7A1 transcription. | missing | none |
| cell_type | This mechanism occurs in hepatocytes, with HepG2/DepMap ACH-000625 as a relevant expression context. | missing | none |
| phenotype | Higher CYP7A1 activity increases bile-acid synthesis from cholesterol and lowers LDL cholesterol. | missing | none |

Predictions: Alt T increases allele-specific HNF4A occupancy in HepG2 hepatocytes.; Alt T increases reporter activity in an allele-specific CYP7A1 enhancer reporter.; Alt T is associated with higher CYP7A1 expression in liver/hepatocyte context.; Alt T is associated with lower LDL cholesterol.

Falsified if: No allele-specific HNF4A binding is detectable at rs7001688.; The alt allele does not increase enhancer/reporter activity, or the effect is not HNF4A-dependent.; CYP7A1 expression is not higher with the alt allele in hepatocyte-relevant assays.

### 3. C2_NR5A2: NR5A2/LRH-1 binding loss at a liver enhancer reduces CYP7A1 and raises LDL cholesterol (p = 0.20)

TF NR5A2 (stated coverage not_checked; registry own_model), ref allele binds more; element CYP7A1 liver enhancer; gene CYP7A1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The ref G allele is predicted to preserve a stronger NR5A2/LRH-1 binding site than the alt T allele at rs7001688. | missing | none |
| element | The NR5A2 site lies in a liver enhancer that can regulate CYP7A1. | missing | none |
| gene | Stronger NR5A2 binding at this element increases CYP7A1 transcription. | missing | none |
| cell_type | This occurs in hepatocytes, consistent with the HepG2 expression context. | missing | none |
| phenotype | Higher CYP7A1 activity lowers LDL cholesterol. | missing | none |

Predictions: Ref G increases allele-specific NR5A2 occupancy in HepG2 hepatocytes.; Ref G increases reporter activity in an allele-specific CYP7A1 enhancer reporter.; Ref G is associated with higher CYP7A1 expression.; Ref G is associated with lower LDL cholesterol.

Falsified if: No allele-specific NR5A2 binding is detectable at rs7001688.; Ref G does not increase enhancer/reporter activity in hepatocyte models.; NR5A2 knockdown does not reduce the allele-specific reporter effect.

### 4. C3_NR1H4: FXR/NR1H4 binding gain represses CYP7A1 and raises LDL cholesterol (p = 0.15)

TF NR1H4 (stated coverage not_checked; registry own_model), alt allele binds more; element CYP7A1 liver enhancer; gene CYP7A1; cell type hepatocyte.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | The alt T allele is predicted to create or strengthen an NR1H4/FXR binding site at rs7001688, so FXR binds alt more strongly than ref. | missing | none |
| element | The allele-specific FXR site lies in a liver regulatory element capable of repressing CYP7A1. | missing | none |
| gene | Increased FXR binding represses CYP7A1 transcription, directly or through SHP-mediated repression. | missing | none |
| cell_type | This occurs in hepatocytes, consistent with HepG2 as a liver-derived context. | missing | none |
| phenotype | Lower CYP7A1 activity reduces bile-acid synthesis and raises LDL cholesterol. | missing | none |

Predictions: Alt T increases allele-specific FXR occupancy in HepG2 hepatocytes.; Alt T decreases CYP7A1 enhancer/reporter activity, consistent with FXR-mediated repression.; Alt T is associated with lower CYP7A1 expression.; Alt T is associated with higher LDL cholesterol.

Falsified if: No allele-specific FXR binding is detectable at rs7001688.; Alt T does not reduce CYP7A1 reporter activity in hepatocyte models.; FXR knockdown or ligand treatment does not alter the allele-specific effect.

## Prediction matrix

| Test | Cost | Separates top two | C0_null | C1_HNF4A | C2_NR5A2 | C3_NR1H4 |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TF binding in HepG2 | low | yes | no allele-specific TF binding | alt > ref for HNF4A binding | ref > alt for NR5A2 binding | alt > ref for FXR binding |
| Allele-specific CYP7A1 enhancer reporter in HepG2 | low | yes | no reproducible allele difference | alt reporter > ref reporter; effect reduced by HNF4A knockdown | ref reporter > alt reporter; effect reduced by NR5A2 knockdown | alt reporter < ref reporter; effect altered by FXR knockdown/ligand |
| CYP7A1 expression by allele in hepatocyte-relevant context | medium | no | no rs7001688-specific allelic effect; linked variant only | alt allele higher CYP7A1 | ref allele higher CYP7A1 | alt allele lower CYP7A1 |
| LDL cholesterol direction in genotype association | high | no | association attributable to linked variant | alt allele lower LDL | ref allele lower LDL | alt allele higher LDL |

## Next experiment

The single cheapest experiment to separate the top two chains C1_HNF4A and C0_null is an allele-specific CYP7A1 enhancer luciferase reporter assay in HepG2 cells comparing ref G versus alt T, with and without HNF4A knockdown. C1_HNF4A predicts alt > ref reporter activity and loss of the allelic difference upon HNF4A knockdown; C0_null predicts no reproducible rs7001688 allele-specific reporter effect.

## Flags

- none

## Evidence
