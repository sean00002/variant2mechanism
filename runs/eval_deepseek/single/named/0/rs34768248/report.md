# rs34768248 and Glioblastoma, melanoma, bladder

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 42 s.

Variant `chr5:1295601:G>A` (germline); expression context: DepMap:subtype=Glioblastoma (median of 54 lines).

## Ranked chains

### 1. H0_null: No TF-mediated allelic effect (p = 0.42)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific binding of GABPA, ELK1, E2F1, or other candidate TFs at rs34768248.; No allele-specific effect in a TERT promoter reporter assay.; No rs34768248 genotype effect on TERT mRNA/protein in glioblastoma lines.; Any disease association is explained by linkage disequilibrium with another causal variant or by a passenger event.

Falsified if: A robust allele-specific TF binding difference is demonstrated at rs34768248.; An allele-specific TERT reporter effect is demonstrated and depends on the candidate TF binding site.

### 2. H1_GABPA: Alt allele increases GABPA binding at the TERT promoter (p = 0.30)

TF GABPA (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter/regulatory element; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GABPA binds the alt A allele more strongly than the ref G allele; GABPA is chosen as the TERT-promoter ETS-family factor from literature knowledge, not from provided QBiC-SELEX evidence. | missing | none |
| element | rs34768248 lies in a TERT promoter/regulatory element where an ETS/GABPA site can affect promoter activity. | missing | none |
| gene | Increased GABPA occupancy at this element increases TERT transcription. | missing | none |
| cell_type | TERT is expressed and the TERT promoter is active in glioblastoma cells, including the DepMap glioblastoma context. | missing | none |
| phenotype | Higher TERT expression/telomerase activity promotes glioblastoma, and the same element may contribute in melanoma and bladder cancer. | missing | none |

Predictions: Allele-specific GABPA EMSA: alt > ref.; GABPA ChIP-qPCR at the rs34768248 element: alt allele occupied more.; TERT promoter reporter: alt > ref, reduced by GABPA-site mutation or GABPA knockdown.; TERT mRNA/protein higher with alt allele in suitable glioblastoma lines.

Falsified if: GABPA shows no allele-specific binding at rs34768248.; The alt allele does not increase TERT reporter activity or TERT expression in the relevant cellular context.

### 3. H2_ELK1: Alt allele increases ELK1 binding at the TERT promoter (p = 0.14)

TF ELK1 (stated coverage not_checked; registry own_model), alt allele binds more; element TERT promoter/regulatory element; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ELK1, another ETS-family factor, binds the alt A allele more strongly than ref G at a candidate ETS-like motif created or strengthened by the variant. | missing | none |
| element | The variant lies in a TERT promoter/regulatory element where ETS-family occupancy can modulate transcription. | missing | none |
| gene | Increased ELK1 occupancy at this element increases TERT transcription. | missing | none |
| cell_type | ELK1 is expressed and TERT promoter is active in glioblastoma cells. | missing | none |
| phenotype | Increased TERT expression/telomerase activity contributes to glioblastoma and possibly melanoma and bladder cancer. | missing | none |

Predictions: Allele-specific ELK1 EMSA: alt > ref.; ELK1 ChIP-qPCR at the rs34768248 element: alt allele occupied more.; TERT reporter: alt > ref, reduced by ELK1 knockdown but not by GABPA knockdown.; TERT mRNA/protein higher with alt allele.

Falsified if: ELK1 shows no allele-specific binding at rs34768248.; The allele-specific TERT reporter effect is lost only with GABPA perturbation and not with ELK1 perturbation.

### 4. H3_E2F1_repressor: Alt allele loses repressive E2F1 binding and derepresses TERT (p = 0.14)

TF E2F1 (stated coverage not_checked; registry own_model), ref allele binds more; element TERT promoter/regulatory element; gene TERT; cell type Glioblastoma.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | E2F1 binds the ref G allele more strongly than the alt A allele; the alt allele is predicted to weaken an E2F1-like repressive site. | missing | none |
| element | rs34768248 lies in a TERT promoter/regulatory element where loss of a repressive factor can increase promoter activity. | missing | none |
| gene | Reduced E2F1 occupancy at this element derepresses TERT transcription. | missing | none |
| cell_type | E2F1 is expressed in glioblastoma cells and TERT is expressed in the DepMap glioblastoma context. | missing | none |
| phenotype | Derepressed TERT increases telomerase activity and contributes to glioblastoma, melanoma, and bladder cancer. | missing | none |

Predictions: Allele-specific E2F1 EMSA: ref > alt.; E2F1 ChIP-qPCR at the rs34768248 element: ref allele occupied more.; TERT reporter: alt > ref, and the effect is reduced by an E2F1-site mutation or E2F1 overexpression.; TERT mRNA/protein higher with alt allele.

Falsified if: E2F1 shows no allele-specific binding at rs34768248.; The alt allele does not increase TERT reporter activity or TERT expression.; The allele-specific effect is instead explained by an activating ETS factor such as GABPA.

## Prediction matrix

| Test | Cost | Separates top two | H0_null | H1_GABPA | H2_ELK1 | H3_E2F1_repressor |
| --- | --- | --- | --- | --- | --- | --- |
| Allele-specific GABPA EMSA | low | yes | No differential GABPA binding | alt > ref GABPA binding | No differential GABPA binding | No differential GABPA binding |
| Allele-specific ELK1 EMSA | low | no | No differential ELK1 binding | No differential ELK1 binding | alt > ref ELK1 binding | No differential ELK1 binding |
| Allele-specific E2F1 EMSA | low | no | No differential E2F1 binding | No differential E2F1 binding | No differential E2F1 binding | ref > alt E2F1 binding |
| TERT promoter reporter, ref vs alt | medium | no | No allele-specific reporter difference | alt > ref reporter activity; GABPA-site mutation or knockdown reduces effect | alt > ref reporter activity; ELK1 knockdown reduces effect | alt > ref reporter activity; E2F1-site mutation or E2F1 overexpression reduces effect |

## Next experiment

Run the cheapest discriminating experiment: allele-specific EMSA with recombinant GABPA on ref-G and alt-A oligos spanning rs34768248. A clear alt > ref GABPA shift supports H1_GABPA over H0_null; no differential GABPA binding supports H0_null over H1_GABPA.

## Flags

- none

## Evidence
