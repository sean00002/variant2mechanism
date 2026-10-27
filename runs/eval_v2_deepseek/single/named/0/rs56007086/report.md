# rs56007086 and Breast cancer (16q12)

Configuration `single`, named mode, seed 0. Models: generator deepseek/deepseek-v4.1-flash-1017, critic deepseek/deepseek-v4.1-flash-1017, summariser deepseek/deepseek-v4.1-flash-1017. Cost $0.00 over 1 model calls; 24 s.

Variant `chr16:52565398:G>A` (germline); expression context: DepMap:ACH-000019 (MCF7).

## Ranked chains

### 1. H_FOXA1: FOXA1 gain-of-binding at the alt allele activates TOX3 (p = 0.40)

TF FOXA1 (QBiC-SELEX coverage own_model), alt allele binds more; element TOX3-associated 16q12 enhancer; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | FOXA1 binds the alt A allele more strongly than the ref G allele at rs56007086; this is a literature/context-based hypothesis, and no QBiC-SELEX model or ChIP occupancy evidence is supplied in this case. | missing | none |
| element | rs56007086 lies in a 16q12 element near TOX3 that is plausibly an enhancer in breast-cancer cells. | missing | none |
| gene | The enhancer regulates TOX3. | missing | none |
| cell_type | FOXA1 is expressed and active in MCF7 breast cancer cells. | missing | none |
| phenotype | Increased TOX3 enhancer activity and TOX3 expression promote breast-cancer risk. | missing | none |

Predictions: Alt A increases FOXA1 occupancy.; Alt A increases enhancer activity and TOX3 expression in MCF7.; The risk/effect allele tracks with higher TOX3 expression.

Falsified if: Allele-specific FOXA1 ChIP or EMSA shows no differential FOXA1 binding between G and A.; Editing G>A in MCF7 does not alter TOX3 expression or enhancer activity.

### 2. H_NULL: No TF-mediated allelic effect; linked causal variant or null (p = 0.25)

Null chain: no TF-mediated effect of this variant.

Predictions: No allele-specific TF occupancy at rs56007086.; The association is explained by LD with a nearby causal variant or by chance/passenger effects.; Editing rs56007086 alone does not change TOX3 expression.

Falsified if: Fine-mapping and functional assays show rs56007086 itself has allele-specific TF binding and regulatory activity.; No linked causal variant can explain the association.

### 3. H_GATA3: GATA3 loss-of-binding at the alt allele derepresses TOX3 (p = 0.15)

TF GATA3 (QBiC-SELEX coverage own_model), ref allele binds more; element TOX3-associated 16q12 enhancer; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | GATA3 binds the ref G allele more strongly than the alt A allele at rs56007086; no QBiC-SELEX model or occupancy evidence is supplied, so this is a competing motif hypothesis. | missing | none |
| element | The variant sits in a TOX3-associated 16q12 regulatory element. | missing | none |
| gene | GATA3 occupancy at this element represses TOX3. | missing | none |
| cell_type | GATA3 is a key breast epithelial TF expressed in MCF7 cells. | missing | none |
| phenotype | Loss of GATA3 repression increases TOX3 and breast-cancer risk. | missing | none |

Predictions: Ref G increases GATA3 occupancy relative to alt A.; Alt A reduces GATA3-dependent repression and increases TOX3 expression.; GATA3 knockdown should mimic the alt allele.

Falsified if: Allele-specific GATA3 ChIP or EMSA shows no preferential GATA3 binding to G over A.; GATA3 knockdown does not change TOX3 expression or enhancer activity.

### 4. H_CEBPB: CEBPB gain-of-binding at the alt allele activates TOX3 (p = 0.10)

TF CEBPB (QBiC-SELEX coverage own_model), alt allele binds more; element TOX3-associated 16q12 enhancer; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | CEBPB binds the alt A allele more strongly than the ref G allele; no QBiC-SELEX model or occupancy evidence is supplied, so this is a lower-confidence motif hypothesis. | missing | none |
| element | The variant is in a candidate 16q12 enhancer near TOX3. | missing | none |
| gene | CEBPB binding activates TOX3. | missing | none |
| cell_type | CEBPB is expressed in MCF7 breast cancer cells. | missing | none |
| phenotype | Higher TOX3 contributes to breast-cancer risk. | missing | none |

Predictions: Alt A increases CEBPB occupancy.; Alt A increases TOX3 expression.; CEBPB knockdown reduces the alt-allele enhancer effect.

Falsified if: CEBPB ChIP or EMSA shows no allele-specific binding at rs56007086.; CEBPB perturbation does not affect TOX3 or the enhancer.

### 5. H_ZNF263: ZNF263 loss-of-binding at the alt allele derepresses TOX3 (p = 0.10)

TF ZNF263 (QBiC-SELEX coverage own_model), ref allele binds more; element TOX3-associated 16q12 enhancer; gene TOX3; cell type MCF7 breast cancer cells.

| Step | Claim | Status | Evidence |
| --- | --- | --- | --- |
| binding | ZNF263 binds the ref G allele more strongly than the alt A allele; no QBiC-SELEX model or occupancy evidence is supplied, so this is a low-confidence motif hypothesis. | missing | none |
| element | The variant lies in a 16q12 element near TOX3. | missing | none |
| gene | ZNF263 represses TOX3. | missing | none |
| cell_type | ZNF263 is expressed in MCF7 cells. | missing | none |
| phenotype | Loss of ZNF263 repression increases TOX3 and breast-cancer risk. | missing | none |

Predictions: Ref G increases ZNF263 occupancy.; Alt A reduces ZNF263 binding and increases TOX3.; ZNF263 knockdown increases TOX3.

Falsified if: ZNF263 ChIP or EMSA shows no allele-specific binding.; ZNF263 perturbation does not alter TOX3 expression.

## Prediction matrix

| Test | Cost | Separates top two | H_FOXA1 | H_NULL | H_GATA3 | H_CEBPB | H_ZNF263 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Recombinant EMSA with FOXA1 and GATA3 on ref-G and alt-A probes, including competition and supershift controls. | low | yes | Alt A probe shifts with FOXA1; ref G does not. |  | Ref G probe shifts with GATA3; alt A does not. |  |  |

## Next experiment

Perform recombinant EMSA with FOXA1 and GATA3 on ref-G and alt-A probes; this is the cheapest single experiment that can distinguish the top two chains because they differ in both TF identity (FOXA1 vs GATA3) and preferred allele (alt vs ref).

## Flags

- none

## Evidence
