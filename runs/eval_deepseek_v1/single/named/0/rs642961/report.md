# rs642961 and Cleft lip (IRF6)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 40 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. C1: TFAP2A binds the ref A allele more strongly; the risk G allele weakens the IRF6 enhancer and lowers IRF6 (p = 0.55)

TF TFAP2A (stated coverage not_checked; registry own_model), ref allele binds more; element IRF6 MCS9.7 enhancer; gene IRF6; cell type developing oral epithelium/periderm at the lip.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A binds the ref A allele more strongly than the alt G allele at rs642961; the G allele is predicted to disrupt an AP-2-binding site. TFAP2A was chosen as the AP-2-family member most consistent with the known IRF6 enhancer biology; QBiC-SELEX coverage is not_checked because no screen or qbic_tf_detail evidence was supplied. | missing | none |
| element | rs642961 lies in the IRF6 MCS9.7 enhancer; the A allele preserves an enhancer sequence that can be bound by TFAP2A, while the G allele weakens it. | missing | none |
| gene | The TFAP2A-bound IRF6 enhancer element promotes IRF6 transcription. | missing | none |
| cell_type | The relevant cell type is developing oral epithelium/periderm at the lip, with possible contributions from cranial neural crest-derived lip mesenchyme. | missing | none |
| phenotype | Reduced IRF6 dosage in the developing lip impairs epithelial fusion and increases cleft lip risk. | missing | none |

Predictions: TFAP2A binds the A allele more than the G allele at rs642961.; The A allele preserves higher enhancer activity than the G allele in an IRF6 enhancer reporter.; IRF6 expression is lower when the G allele is present in the relevant craniofacial epithelial context.; The phenotype is consistent with reduced IRF6 dosage increasing cleft lip risk.

Falsified if: TFAP2A shows no reproducible allele-specific binding to rs642961 probes.; The G allele does not reduce IRF6 enhancer activity or IRF6 expression in the relevant cell context.

### 2. C2: No TF-mediated allelic effect at rs642961; association is due to a linked causal variant or passenger signal (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: rs642961 itself does not alter TF binding or enhancer activity.; Any association with cleft lip is explained by linkage disequilibrium with another variant.; Allele-specific TFAP2A binding is not reproducible.

Falsified if: rs642961 shows reproducible allele-specific TF binding and enhancer activity in the relevant cell context.

### 3. C3: Opposite-direction TFAP2A chain: the alt G allele binds TFAP2A more strongly and represses IRF6 (p = 0.10)

TF TFAP2A (stated coverage not_checked; registry own_model), alt allele binds more; element IRF6 MCS9.7 enhancer; gene IRF6; cell type developing oral epithelium/periderm at the lip.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A binds the alt G allele more strongly than the ref A allele at rs642961. QBiC-SELEX coverage is not_checked because no screen or qbic_tf_detail evidence was supplied. | missing | none |
| element | The G allele creates or strengthens a TFAP2A-responsive sequence in the IRF6 MCS9.7 enhancer. | missing | none |
| gene | Increased TFAP2A occupancy at this element represses IRF6 transcription. | missing | none |
| cell_type | The relevant cell type is developing oral epithelium/periderm at the lip. | missing | none |
| phenotype | Reduced IRF6 expression increases cleft lip risk. | missing | none |

Predictions: TFAP2A binds the G allele more than the A allele at rs642961.; The G allele increases TFAP2A occupancy and reduces IRF6 enhancer activity if TFAP2A acts as a repressor in this context.; IRF6 expression is lower with the G allele, but through increased rather than decreased TFAP2A binding.

Falsified if: TFAP2A binds the A allele more strongly than the G allele.; The G allele increases rather than decreases IRF6 enhancer activity.

### 4. C4: TP63 rather than TFAP2A mediates the allelic effect at rs642961 (p = 0.10)

TF TP63 (stated coverage not_checked; registry own_model), ref allele binds more; element IRF6 MCS9.7 enhancer; gene IRF6; cell type developing oral epithelium/periderm at the lip.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TP63 binds the ref A allele more strongly than the alt G allele at rs642961. TP63 QBiC-SELEX coverage is not_checked because no screen or qbic_tf_detail evidence was supplied. | missing | none |
| element | rs642961 lies within an IRF6 enhancer that can be regulated by TP63-responsive sequences. | missing | none |
| gene | TP63-bound enhancer activity contributes to IRF6 transcription. | missing | none |
| cell_type | The relevant cell type is developing oral epithelium/periderm at the lip. | missing | none |
| phenotype | Reduced TP63-dependent IRF6 expression increases cleft lip risk. | missing | none |

Predictions: TP63 binds the ref A allele more than the alt G allele at rs642961.; The G allele reduces TP63-dependent IRF6 enhancer activity.; TFAP2A allelic binding is not the primary driver.

Falsified if: TP63 shows no allele-specific binding to rs642961.; TFAP2A, not TP63, accounts for the allele-specific enhancer effect.

## Prediction matrix

| Test | Cost | Separates top two | C1 | C2 | C3 | C4 |
| --- | --- | --- | --- | --- | --- | --- |
| TFAP2A binding to ref vs alt probe | low | yes | Much stronger binding to ref A than alt G | No reproducible allele-specific binding |  |  |

## Next experiment

Allele-specific EMSA with recombinant TFAP2A and short dsDNA probes centered on rs642961 (ref A vs alt G), with cold competitor and, if available, TFAP2A antibody supershift. A reproducible ref>alt binding difference supports the TFAP2A-loss chain; no allele-specific binding supports the null.

## Flags

- none

## Evidence
