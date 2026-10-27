# rs11629191 and Breast cancer

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 119 s.

Variant `chr14:55887040:C>T` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H4: Null: no TF-mediated effect at this base (p = 0.52)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs11629191.; No allele-specific reporter activity in MCF7.; Any disease association is due to linkage disequilibrium with a nearby causal variant or chance.

Falsified if: A robust allele-specific TF binding and functional effect is demonstrated at this base.

### 2. H1: FOXA1-bound enhancer allele increases PRPF39 (p = 0.25)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element intronic enhancer at rs11629191; gene PRPF39; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alt T creates a stronger forkhead/FOXA1-like motif than ref C. FOXA1 is expressed in MCF7 and is a breast-lineage TF; no QBiC-SELEX model is supplied for FOXA1 here, so this is motif-based and not direct binding evidence. | missing | none |
| element | The variant lies in a plausible open-chromatin/intronic enhancer element in MCF7 where FOXA1 occupancy could change enhancer activity. | missing | none |
| gene | The element is assigned to PRPF39 as the nearest MCF7-expressed gene in this interval; this assignment is an assumption, not supplied evidence. | missing | none |
| cell_type | MCF7 breast cancer cells express FOXA1 and are the stated expression context. | missing | none |
| phenotype | Increased FOXA1-bound enhancer activity raises PRPF39 expression and contributes to breast cancer risk or behavior. | missing | none |

Predictions: Alt allele shows higher FOXA1 occupancy in MCF7.; Alt reporter activity is higher in MCF7.; FOXA1 knockdown reduces PRPF39 expression in MCF7.

Falsified if: Allele-specific FOXA1 ChIP shows no alt enrichment.; Reporter assays show no allele difference.

### 3. H2: CTCF insulator disruption at rs11629191 (p = 0.14)

TF CTCF (QBiC-SELEX coverage own_model), ref allele binds more; element CTCF insulator site; gene PRPF39; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Ref C preserves a C-rich CTCF core motif better than alt T; CTCF is broadly expressed and no QBiC-SELEX model is supplied, so this is motif-based. | missing | none |
| element | The variant could sit in a CTCF insulator element; loss of CTCF binding may alter chromatin domain boundaries. | missing | none |
| gene | Altered insulation changes PRPF39 regulatory contact frequency; target assignment is hypothetical. | missing | none |
| cell_type | MCF7 cells express CTCF and have CTCF-bound chromatin. | missing | none |
| phenotype | CTCF loss at this site de-insulates PRPF39 and contributes to breast cancer. | missing | none |

Predictions: Ref allele shows higher CTCF occupancy.; Alt allele weakens CTCF binding and changes local chromatin contacts.

Falsified if: CTCF ChIP shows no allele-specific occupancy.; Chromatin contact assays show no insulation change.

### 4. H3: TFAP2C motif loss de-represses OTX2 (p = 0.09)

TF TFAP2C (QBiC-SELEX coverage own_model), ref allele binds more; element TFAP2C-bound enhancer; gene OTX2; cell type MCF7.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Ref C fits a TFAP2C/AP-2-like motif better than alt T. TFAP2C is expressed in breast cancer cells; no QBiC-SELEX model is supplied, so this is motif-based. | missing | none |
| element | The element is proposed to be a TFAP2C-bound enhancer; weakened binding could change enhancer output. | missing | none |
| gene | The element is assumed to contact OTX2, a developmental TF gene, rather than the nearest gene. | missing | none |
| cell_type | MCF7 cells express TFAP2C and are a breast cancer context. | missing | none |
| phenotype | Loss of TFAP2C repression increases OTX2 expression and promotes breast cancer phenotypes. | missing | none |

Predictions: Ref allele shows higher TFAP2C occupancy.; Alt allele increases OTX2 expression in MCF7.

Falsified if: TFAP2C ChIP shows no allele effect.; OTX2 expression is unchanged by allele or TFAP2C knockdown.

## Prediction matrix

| Test | Cost | Separates top two | H4 | H1 | H2 | H3 |
| --- | --- | --- | --- | --- | --- | --- |
| EMSA with recombinant FOXA1 and ref/alt probes | low | yes | Ref and alt probes show equal FOXA1 binding | Alt probe shows stronger FOXA1 shift |  |  |
| Allele-specific FOXA1 ChIP-qPCR in heterozygous MCF7 cells | medium | yes | No allelic imbalance at rs11629191 | Alt allele is enriched for FOXA1 |  |  |
| CTCF ChIP-qPCR across rs11629191 in MCF7 | medium | no |  | No CTCF allele effect | Ref allele is enriched for CTCF |  |
| Ref/alt luciferase reporter in MCF7 | medium | yes | No allele difference in reporter activity | Alt allele increases reporter activity |  |  |

## Next experiment

EMSA with recombinant FOXA1 and ref/alt probes is the cheapest first test for allele-specific FOXA1 binding; if positive, confirm occupancy with allele-specific FOXA1 ChIP-qPCR in MCF7.

## Flags

- none

## Evidence
