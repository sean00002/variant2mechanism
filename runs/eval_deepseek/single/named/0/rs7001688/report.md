# rs7001688 and LDL cholesterol

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 39 s.

Variant `chr8:57573391:G>T` (germline); expression context: DepMap:ACH-000625 (Hep 3B2.1-7).

## Ranked chains

### 1. C0: Null: no TF-mediated allelic effect of rs7001688 (p = 0.40)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF binding at rs7001688 in Hep3B nuclear extract.; No allele-specific regulatory-element activity for ref G versus alt T.; No allelic effect on CYP7A1 or other local transcript; any LDL association is due to a linked causal variant or chance.

Falsified if: A reproducible allele-specific TF footprint, EMSA shift, or ChIP-qPCR difference is seen for ref versus alt in Hep3B cells.

### 2. C1: HNF4A binds ref G more and activates CYP7A1 (p = 0.28)

TF HNF4A (stated coverage not_checked; registry own_model), ref allele binds more; element hepatocyte enhancer; gene CYP7A1; cell type hepatocyte/Hep3B.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HNF4A binds the ref G allele more strongly than the alt T allele at rs7001688, consistent with disruption of a candidate HNF4A motif; direct evidence not supplied. | missing | none |
| element | rs7001688 lies in a candidate hepatocyte-active regulatory element whose activity depends on the HNF4A site. | missing | none |
| gene | The element regulates CYP7A1 transcription in hepatocytes. | missing | none |
| cell_type | Hep3B is an appropriate model because HNF4A and CYP7A1 are expressed in hepatocyte-lineage cells. | missing | none |
| phenotype | Ref G increases HNF4A-dependent CYP7A1 expression, increasing bile-acid synthesis and lowering LDL cholesterol. | missing | none |

Predictions: Ref G shows stronger HNF4A EMSA/ChIP signal than alt T in Hep3B.; Ref G increases CYP7A1 reporter activity and CYP7A1 expression.; Ref G is associated with lower LDL cholesterol through this element.

Falsified if: No ref>alt HNF4A binding is detected, HNF4A supershift fails, or CYP7A1 expression is not allele-dependent in hepatocytes.

### 3. C2: HNF1A binds alt T more and represses CYP7A1 (p = 0.14)

TF HNF1A (stated coverage not_checked; registry own_model), alt allele binds more; element hepatocyte repressive element; gene CYP7A1; cell type hepatocyte/Hep3B.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | HNF1A binds the alt T allele more strongly than ref G at rs7001688, creating a candidate HNF1A site; direct evidence not supplied. | missing | none |
| element | The alt T allele increases occupancy of a repressive hepatocyte regulatory element. | missing | none |
| gene | The repressive element lowers CYP7A1 transcription. | missing | none |
| cell_type | Hep3B is relevant because HNF1A is expressed in hepatocyte-lineage cells. | missing | none |
| phenotype | Alt T increases HNF1A-mediated repression of CYP7A1, reducing bile-acid synthesis and raising LDL cholesterol. | missing | none |

Predictions: Alt T shows stronger HNF1A EMSA/ChIP signal than ref G.; Alt T lowers CYP7A1 reporter activity and CYP7A1 expression.; Alt T is associated with higher LDL cholesterol through this element.

Falsified if: No alt>ref HNF1A binding is detected, HNF1A supershift fails, or CYP7A1 is not repressed by the alt allele.

### 4. C3: CEBPB binds ref G more and activates CYP7A1 (p = 0.10)

TF CEBPB (stated coverage not_checked; registry own_model), ref allele binds more; element hepatocyte enhancer; gene CYP7A1; cell type hepatocyte/Hep3B.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB binds the ref G allele more strongly than alt T at rs7001688, consistent with a candidate CEBPB motif; direct evidence not supplied. | missing | none |
| element | The ref G allele increases activity of a hepatocyte regulatory element. | missing | none |
| gene | The element increases CYP7A1 transcription. | missing | none |
| cell_type | Hep3B is appropriate because CEBPB is expressed in hepatocyte-lineage cells. | missing | none |
| phenotype | Ref G increases CEBPB-dependent CYP7A1 expression, increasing bile-acid synthesis and lowering LDL cholesterol. | missing | none |

Predictions: Ref G shows stronger CEBPB EMSA/ChIP signal than alt T.; Ref G increases CYP7A1 reporter activity.; Ref G is associated with lower LDL cholesterol through this element.

Falsified if: No ref>alt CEBPB binding is detected or CYP7A1 expression is not CEBPB-dependent in hepatocytes.

### 5. C4: SREBF2 binds alt T more and represses CYP7A1 (p = 0.08)

TF SREBF2 (stated coverage not_checked; registry own_model), alt allele binds more; element sterol-responsive repressive element; gene CYP7A1; cell type hepatocyte/Hep3B.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | SREBF2 binds the alt T allele more strongly than ref G at rs7001688, creating a candidate SREBF2 site; direct evidence not supplied. | missing | none |
| element | The alt T allele increases occupancy of a sterol-responsive repressive element. | missing | none |
| gene | The element lowers CYP7A1 transcription. | missing | none |
| cell_type | Hep3B is relevant because SREBF2 is expressed in hepatocyte-lineage cells. | missing | none |
| phenotype | Alt T increases SREBF2-mediated repression of CYP7A1, reducing bile-acid synthesis and raising LDL cholesterol. | missing | none |

Predictions: Alt T shows stronger SREBF2 EMSA/ChIP signal than ref G.; Alt T lowers CYP7A1 reporter activity.; Alt T is associated with higher LDL cholesterol through this element.

Falsified if: No alt>ref SREBF2 binding is detected or CYP7A1 is not repressed by the alt allele in hepatocytes.

## Prediction matrix

| Test | Cost | Separates top two | C0 | C1 | C2 | C3 | C4 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Allele-specific TF binding in Hep3B | low | yes | No reproducible ref/alt binding difference | Ref G binds HNF4A more strongly |  |  |  |

## Next experiment

Run allele-specific EMSA with Hep3B nuclear extract using ref-G and alt-T probes, then HNF4A antibody supershift; this directly tests the top two chains C0 vs C1. If HNF4A binds ref G more strongly, C1 is favored; if binding is allele-independent or HNF4A supershift fails, C0 is favored.

## Flags

- none

## Evidence
