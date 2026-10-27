# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 57 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. C1: GATA2 site created by alt A at the TERT promoter (p = 0.35)

TF GATA2 (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter; gene TERT; cell type glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alt A is predicted to create a GATA2 consensus site at rs34768248, so GATA2 binds the alt allele more strongly than ref G. I choose GATA2 rather than GATA1/GATA3 because GATA2 is a plausible TERT-promoter regulator in glioblastoma and the G>A change fits a GATA-motif creation model; no QBiC-SELEX or ChIP evidence is supplied, so this is a motif-based claim only. | missing | none |
| element | rs34768248 lies in the TERT promoter region upstream of the TERT transcription start site, where a gained GATA2 site could act as a promoter/enhancer element. | missing | none |
| gene | The element regulates TERT, the telomerase catalytic subunit gene. | missing | none |
| cell_type | The effect is expected in glioblastoma cells, and possibly melanoma and bladder cancer cells, where TERT promoter activity and GATA2 expression are relevant; DepMap glioblastoma is the supplied expression context. | missing | none |
| phenotype | Increased GATA2 binding at the alt allele is predicted to increase TERT expression, supporting telomere maintenance and cancer risk in glioblastoma, melanoma and bladder cancer. | missing | none |

Predictions: Alt-specific GATA2 binding by EMSA or ChIP-qPCR over rs34768248.; Alt allele gives higher TERT reporter activity in glioblastoma cells.; GATA2 knockdown reduces the alt-allele-specific TERT effect.

Falsified if: GATA2 binds ref more than alt, or does not bind either allele.; No allele-specific TERT expression or reporter effect is observed.

### 2. C4: Null: no TF-mediated allelic effect at rs34768248 (p = 0.35)

Null chain: no TF-mediated effect of this variant.

Predictions: No reproducible allele-specific TF binding at rs34768248.; Any TERT or disease association is explained by a linked causal variant, a passenger event, or no allelic effect.; Reporter assays show no allele-specific difference after controlling for nearby variants.

Falsified if: A reproducible allele-specific TF occupancy and allele-specific TERT effect are demonstrated at rs34768248.

### 3. C2: GABPA/ETS site created by alt A at the TERT promoter (p = 0.20)

TF GABPA (QBiC-SELEX coverage own_model), alt allele binds more; element TERT promoter; gene TERT; cell type glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Alt A is predicted to create or strengthen an ETS-family motif, so GABPA binds the alt allele more strongly than ref G. I choose GABPA over ETS1/ELK1 because TERT promoter ETS sites are commonly GABPA-bound and TERT promoter mutations often create ETS sites; no QBiC-SELEX or ChIP evidence is supplied, so this remains motif- and literature-based. | missing | none |
| element | rs34768248 lies in the TERT promoter, where a gained ETS/GABPA site could modulate promoter activity. | missing | none |
| gene | The element regulates TERT. | missing | none |
| cell_type | The effect is expected in glioblastoma and other TERT-promoter-active cancers such as melanoma and bladder cancer. | missing | none |
| phenotype | Increased GABPA binding at the alt allele is predicted to increase TERT expression and support cancer risk. | missing | none |

Predictions: Alt-specific GABPA binding by EMSA or ChIP-qPCR over rs34768248.; Alt allele gives higher TERT reporter activity.; GABPA knockdown reduces the alt-allele-specific TERT effect.

Falsified if: GABPA does not occupy the variant region or binds ref more than alt.; TERT expression is not allele-specific in the relevant cell type.

### 4. C3: SP1 site disrupted by alt A, lowering TERT (p = 0.10)

TF SP1 (QBiC-SELEX coverage own_model), ref allele binds more; element TERT promoter; gene TERT; cell type glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | Ref G is predicted to preserve a GC-box/SP1 site, so SP1 binds ref more strongly than alt A; alt A would disrupt SP1 binding. This is a lower-probability motif-based alternative because TERT promoters are GC-rich and SP1 is a known TERT activator, but no QBiC-SELEX or ChIP evidence is supplied. | missing | none |
| element | rs34768248 lies in the TERT promoter, where loss of an SP1 site could reduce promoter activity. | missing | none |
| gene | The element regulates TERT. | missing | none |
| cell_type | The effect would be expected in glioblastoma and other TERT-expressing cancer cells. | missing | none |
| phenotype | Alt A is predicted to lower SP1-driven TERT expression; if alt is the risk allele, this chain requires TERT lowering to be oncogenic in the relevant context, which is not the usual TERT-promoter model and is therefore assigned low probability. | missing | none |

Predictions: Ref-specific SP1 binding by EMSA or ChIP-qPCR.; Alt allele gives lower TERT reporter activity.; SP1 knockdown reduces the ref-allele-specific TERT effect.

Falsified if: SP1 binds alt more than ref or does not bind the region.; Alt allele increases rather than decreases TERT expression.

## Prediction matrix

| Test | Cost | Separates top two | C1 | C4 | C2 | C3 |
| --- | --- | --- | --- | --- | --- | --- |
| no | low | yes | alt-specific GATA2 band/supershift | no allele-specific band for any tested TF | alt-specific GABPA band/supershift | ref-specific SP1 band |

## Next experiment

Allele-specific EMSA with short probes spanning rs34768248 (G vs A) and recombinant GATA2 and GABPA, optionally with antibody supershift; this is the cheapest single experiment that separates C1 from C2. C1 predicts an alt-specific GATA2 shift; C2 predicts an alt-specific GABPA shift; C4 predicts no allele-specific shift.

## Flags

- none

## Evidence
