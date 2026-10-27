# rs642961 and Cleft lip (IRF6)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 28 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. chain_1: TFAP2A binds the ref A allele more strongly (p = 0.48)

TF TFAP2A (stated coverage not_checked; registry own_model), ref allele binds more; element IRF6 craniofacial enhancer containing rs642961; gene IRF6; cell type oral/craniofacial epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A binds the ref A allele more strongly than the alt G allele at rs642961; the G allele weakens an AP-2-type binding site. | missing | none |
| element | rs642961 lies in an IRF6 craniofacial enhancer; the A>G change reduces enhancer activity. | missing | none |
| gene | Reduced enhancer activity lowers IRF6 transcription. | missing | none |
| cell_type | The relevant cells are oral/craniofacial epithelial cells where TFAP2A and IRF6 are expressed. | missing | none |
| phenotype | Lower IRF6 levels in the developing lip epithelium increase cleft lip risk. | missing | none |

Predictions: recombinant TFAP2A binds ref-A oligo more than alt-G oligo; rs642961 A>G reduces enhancer activity in oral/craniofacial epithelial cells; risk G allele associates with lower IRF6 expression in relevant epithelial cells; lower IRF6 increases cleft lip risk

Falsified if: EMSA or ChIP shows no ref>alt TFAP2A binding at rs642961; ref-A and alt-G reporters have equal activity in oral epithelial cells; IRF6 expression is not allele-dependently altered in relevant cells

### 2. null: null: no TF-mediated allelic effect at rs642961 (p = 0.30)

Null chain: no TF-mediated effect of this variant.

Predictions: no allele-specific TF binding at rs642961; no allele-specific enhancer activity in the relevant cells; no allele-specific IRF6 expression change; association with cleft lip is explained by LD with a linked causal variant or by chance/passenger effect

Falsified if: a reproducible allele-specific TFAP2A binding difference is found for rs642961; a ref-vs-alt reporter shows allele-specific activity in oral/craniofacial epithelial cells

### 3. chain_2: TFAP2C, not TFAP2A, mediates the allelic binding effect (p = 0.12)

TF TFAP2C (stated coverage not_checked; registry own_model), ref allele binds more; element IRF6 craniofacial enhancer containing rs642961; gene IRF6; cell type oral/craniofacial epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2C binds the ref A allele more strongly than the alt G allele at rs642961, with AP-2-family redundancy at this site. | missing | none |
| element | rs642961 lies in an IRF6 craniofacial enhancer whose activity depends on this AP-2-family site. | missing | none |
| gene | Allele-specific TFAP2C binding alters IRF6 enhancer output and IRF6 transcription. | missing | none |
| cell_type | The effect occurs in oral/craniofacial epithelial cells expressing TFAP2C and IRF6. | missing | none |
| phenotype | Altered IRF6 dosage in the developing lip increases cleft lip risk. | missing | none |

Predictions: recombinant TFAP2C binds ref-A oligo more than alt-G oligo; TFAP2C ChIP at the IRF6 enhancer is allele-specific; TFAP2A knockdown does not abolish the allele-specific enhancer effect; TFAP2C knockdown reduces IRF6 enhancer activity in oral epithelial cells

Falsified if: TFAP2C shows no allele-specific binding at rs642961; TFAP2A, not TFAP2C, is the major allele-specific factor in the relevant cells

### 4. chain_3: TFAP2A binds the alt G allele more strongly (p = 0.10)

TF TFAP2A (stated coverage not_checked; registry own_model), alt allele binds more; element IRF6 craniofacial enhancer containing rs642961; gene IRF6; cell type oral/craniofacial epithelial cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A binds the alt G allele more strongly than the ref A allele at rs642961. | missing | none |
| element | rs642961 lies in an IRF6 craniofacial enhancer and the G allele strengthens its activity. | missing | none |
| gene | Increased enhancer activity raises IRF6 transcription. | missing | none |
| cell_type | The effect occurs in oral/craniofacial epithelial cells. | missing | none |
| phenotype | Altered IRF6 dosage in the developing lip changes cleft lip risk. | missing | none |

Predictions: recombinant TFAP2A binds alt-G oligo more than ref-A oligo; risk G allele increases enhancer activity in the assay used; the direction of IRF6 expression change is opposite to the ref>alt model; if IRF6 is protective, the alt-G higher-binding model could still fit cleft lip risk

Falsified if: EMSA shows ref A binds TFAP2A more strongly than alt G; reporter assays show the G allele reduces rather than increases enhancer activity

## Prediction matrix

| Test | Cost | Separates top two | chain_1 | null | chain_2 | chain_3 |
| --- | --- | --- | --- | --- | --- | --- |
| TFAP2A EMSA | low | yes | ref A > alt G | no allelic difference |  |  |

## Next experiment

allele-specific EMSA with recombinant TFAP2A and ref-A vs alt-G oligos around rs642961; include TFAP2C as a secondary probe. This is the cheapest direct test of the top chain's binding claim and can separate it from the null no-allelic-effect chain. A ref>alt TFAP2A binding difference supports the TFAP2A chain and weakens the null; absence of allele-specific binding falsifies the primary binding link. EMSA alone cannot prove the IRF6 enhancer, cell-type, or phenotype links.

## Flags

- none

## Evidence
