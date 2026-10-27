# rs642961 and Cleft lip (IRF6)

Configuration `single`, named mode, seed 0. Models: generator openai/gpt-6-luna, critic openai/gpt-6-luna, summariser openai/gpt-6-luna. Cost $0.00 over 1 model calls; 39 s.

Variant `chr1:209815925:A>G` (germline); expression context: none.

## Ranked chains

### 1. H1: G strengthens an activating TFAP2A–IRF6 enhancer connection (p = 0.68)

TF TFAP2A (QBiC-SELEX coverage own_model), alt allele binds more; element rs642961-containing IRF6 craniofacial enhancer; gene IRF6; cell type developing craniofacial epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A is the favored AP-2-family factor for this site based on reported rs642961-specific allele-sensitive binding; the alt G allele is expected to bind more strongly than ref A. No QBiC-SELEX result or case-specific occupancy result is provided here. | missing | none |
| element | The variant lies in a cis-regulatory element that can act as an IRF6 enhancer. | missing | none |
| gene | Greater TFAP2A binding increases enhancer output and IRF6 expression. | missing | none |
| cell_type | This enhancer effect occurs in developing craniofacial epithelium. | missing | none |
| phenotype | Increased IRF6 expression from the G allele lowers cleft-lip risk relative to the A allele. | missing | none |

Predictions: In a relevant craniofacial epithelial context, the G allele shows greater TFAP2A binding than the A allele.; An otherwise matched enhancer assay shows greater activity from the G allele, accompanied by increased IRF6 expression.

Falsified if: Allele-matched assays in a relevant context show no greater TFAP2A binding or enhancer activity for G than A.; The G allele consistently lowers IRF6 expression in the relevant cell context.

### 2. H3: No TF-mediated effect of rs642961 (p = 0.24)

Null chain: no TF-mediated effect of this variant.

Predictions: In an appropriate cellular context, changing A to G at rs642961 produces no reproducible TF-mediated change in enhancer activity or IRF6 expression.; Any association with cleft lip could reflect linkage to another causal variant or another non-TF mechanism.

Falsified if: Precise allele editing or matched allele assays reproducibly show a TF-dependent change at rs642961 that alters IRF6 expression.

### 3. H2: G strengthens TFAP2A binding but reduces IRF6 enhancer output (p = 0.08)

TF TFAP2A (QBiC-SELEX coverage own_model), alt allele binds more; element rs642961-containing IRF6 craniofacial enhancer; gene IRF6; cell type developing craniofacial epithelium.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | TFAP2A is the favored AP-2-family factor for this site based on reported rs642961-specific allele-sensitive binding; the alt G allele is expected to bind more strongly than ref A. No QBiC-SELEX result or case-specific occupancy result is provided here. | missing | none |
| element | The variant lies in a cis-regulatory element that can act as an IRF6 enhancer. | missing | none |
| gene | In this alternative model, greater TFAP2A binding reduces enhancer output and IRF6 expression. | missing | none |
| cell_type | This repressive effect occurs in developing craniofacial epithelium. | missing | none |
| phenotype | Reduced IRF6 expression from the G allele increases cleft-lip risk relative to the A allele. | missing | none |

Predictions: The G allele shows greater TFAP2A binding than the A allele.; An otherwise matched enhancer assay shows lower activity from the G allele, accompanied by reduced IRF6 expression.

Falsified if: The G allele increases enhancer activity and IRF6 expression in a relevant cell context.; Allele-matched assays show no greater TFAP2A binding for G than A.

## Prediction matrix

| Test | Cost | Separates top two | H1 | H3 | H2 |
| --- | --- | --- | --- | --- | --- |
| Paired A-versus-G IRF6 enhancer reporter assay in a relevant craniofacial epithelial cell model, with IRF6 expression measured if feasible | low | yes | G produces greater enhancer activity than A, consistent with increased IRF6 expression. | No reproducible allele-dependent difference in enhancer activity or IRF6 expression. | G produces lower enhancer activity than A, consistent with reduced IRF6 expression. |

## Next experiment

Run a paired A-versus-G IRF6 enhancer reporter assay in a relevant craniofacial epithelial cell model; the direction of the activity difference distinguishes the two leading functional models.

## Flags

- none

## Evidence
