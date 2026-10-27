# rs642961 and Cleft lip (IRF6)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 41 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. C1: TFAP2A loss-of-binding at the ref A allele reduces IRF6 enhancer activity (p = 0.55)

TF TFAP2A (QBiC-SELEX coverage own_model), ref allele binds more; element distal IRF6 enhancer; gene IRF6; cell type oral/craniofacial epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A binds the ref A allele more strongly than the alt G allele; TFAP2A is chosen because the element is an IRF6 oral-epithelial enhancer with an AP-2-like site and AP-2α is the craniofacial epithelial paralog implicated at this locus. No QBiC-SELEX data are supplied, so this is a literature/motif-based binding claim, not a direct QBiC measurement. | missing | none |
| element | rs642961 lies in a distal IRF6 enhancer; the ref A allele preserves a functional AP-2-responsive enhancer, while alt G weakens it. | missing | none |
| gene | Weakened enhancer activity lowers IRF6 transcription. | missing | none |
| cell_type | The relevant cells are developing oral/craniofacial epithelial cells, including lip fusion epithelium. | missing | none |
| phenotype | Lower IRF6 dosage impairs epithelial adhesion/fusion and increases cleft lip risk. | missing | none |

Predictions: ref A binds TFAP2A more strongly than alt G; A allele has higher enhancer activity in oral epithelial cells; alt G associates with lower IRF6 expression; alt G increases cleft lip risk

Falsified if: alt G binds TFAP2A more strongly than ref A; no allele-specific TFAP2A binding is detectable; A and G alleles show no differential enhancer activity in oral epithelial cells

### 2. C4: No TF-mediated effect of rs642961; association is due to a linked causal variant or passenger effect (p = 0.20)

Null chain: no TF-mediated effect of this variant.

Predictions: ref A and alt G show no allele-specific TF binding at this base; no allele-specific enhancer activity attributable to rs642961; any IRF6 association is explained by a linked variant or another mechanism

Falsified if: a specific TF shows reproducible allele-specific binding at rs642961; allele-specific enhancer activity maps to this base; the variant changes IRF6 expression in the relevant cell type

### 3. C2: TFAP2C binds the alt G allele more strongly and creates a stronger IRF6 enhancer (p = 0.15)

TF TFAP2C (QBiC-SELEX coverage own_model), alt allele binds more; element distal IRF6 enhancer; gene IRF6; cell type oral/craniofacial epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2C, a close AP-2 paralog with shared binding specificity, binds the alt G allele more strongly than ref A. No QBiC-SELEX data are supplied; this competing claim rests on shared AP-2 motif recognition and epithelial expression, not on direct allele-specific data. | missing | none |
| element | The alt G allele creates or strengthens a TFAP2C-responsive IRF6 enhancer. | missing | none |
| gene | The stronger enhancer increases IRF6 transcription. | missing | none |
| cell_type | The effect occurs in oral/craniofacial epithelial cells. | missing | none |
| phenotype | Misexpressed or increased IRF6 perturbs epithelial fusion and increases cleft lip risk. | missing | none |

Predictions: alt G binds TFAP2C more strongly than ref A; G allele has higher enhancer activity in oral epithelial cells; alt G associates with higher IRF6 expression; altered IRF6 dosage increases cleft lip risk

Falsified if: ref A binds TFAP2C more strongly than alt G; no TFAP2C occupancy is detectable over the element; G allele does not increase enhancer activity or IRF6 expression

### 4. C3: TP63 binds the ref A allele more strongly at a p63-dependent IRF6 enhancer (p = 0.10)

TF TP63 (QBiC-SELEX coverage own_model), ref allele binds more; element distal IRF6 enhancer; gene IRF6; cell type oral/craniofacial epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TP63 binds the ref A allele more strongly than alt G. This is a competing explanation because TP63 is a key craniofacial epithelial TF in the IRF6 pathway; no QBiC-SELEX data are supplied, so this binding claim is not directly measured. | missing | none |
| element | The variant lies in a TP63-responsive IRF6 enhancer; ref A preserves and alt G weakens it. | missing | none |
| gene | Weakened TP63-dependent enhancer activity lowers IRF6 transcription. | missing | none |
| cell_type | The relevant cells are oral/craniofacial keratinocytes or epithelial cells. | missing | none |
| phenotype | Lower IRF6 in these cells impairs lip fusion and increases cleft lip risk. | missing | none |

Predictions: ref A binds TP63 more strongly than alt G; A allele has higher enhancer activity in keratinocytes/oral epithelium; alt G associates with lower IRF6 expression; alt G increases cleft lip risk

Falsified if: alt G binds TP63 more strongly than ref A; TP63 is not occupied at the element; the allelic effect on IRF6 is independent of TP63

## Prediction matrix

| Test | Cost | Separates top two | C1 | C4 | C2 | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| allele-specific EMSA with TFAP2A antibody supershift | low | yes | ref A probe shifts more than alt G; supershift confirms TFAP2A | no allele-specific TFAP2A shift |  |  |
| allele-specific reporter in oral epithelial cells | medium | yes | A allele higher enhancer activity | no allele-specific enhancer activity |  |  |
| allele-specific ChIP-qPCR for TFAP2A over the element | medium | yes | A allele preferentially occupied by TFAP2A | no allelic occupancy difference |  |  |

## Next experiment

none

## Flags

- none

## Evidence
