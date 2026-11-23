# rs4784227 and Breast cancer (16q12) (v8, no_qbic, masked, seed 0)

Context: DepMap:ACH-000019 (MCF7) (given: given with the case).

**Verdict: mechanism.** FOXA1 meets every check.

- TF mechanism: mechanism (FOXA1 meets every check)
- Target gene: TOX3 (indirect: Open Targets L2G 0.96)
- Disease link: supported (GWAS Catalog: Breast cancer (p 2.0e-240); 63 matching association(s) in all)

Cost $0.011 over 5 model calls; 149 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | FOXA1 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 2 | H1 (F1) | GATA3 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 3 | H3 (F3) | CUX1 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 4 | H4 (F4) | E2F1 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 5 | H5 (F5) | ESR1 | TOX3 | direct | direct | supporting | indirect | direct | kept |

## Family screen

- F1 GATA, 6 models: named GATA3; ChIP tier here 1, anywhere 1
- F2 Forkhead, 4 models: named FOXA1; ChIP tier here 1, anywhere 1
- F3 CUT; Homeodomain, 2 models: named CUX1; ChIP tier here 1, anywhere 1
- F4 E2F, 4 models: named E2F1; ChIP tier here 1, anywhere 1
- F5 Nuclear receptor, 29 models: named ESR1; ChIP tier here 1, anywhere 1
- F6 Nuclear receptor, 3 models: named ESRRA; ChIP tier here 1, anywhere 1
- F7 Rel, 1 model: named RELA; ChIP tier here 1, anywhere 1
- F8 bZIP, 2 models: named CREB1; ChIP tier here 1, anywhere 1
- F9 C2H2 ZF, 1 model: named ZNF444; ChIP tier here 1, anywhere 1
- F10 Homeodomain, 81 models: named MSX2; ChIP tier here 1, anywhere 1
- F11 TEA, 4 models: named TEAD4; ChIP tier here 1, anywhere 1
- F12 ARID/BRIGHT; RFX, 1 model: named ARID2; ChIP tier here 1, anywhere 1

## Next experiment

Test the endogenous C>T effect in an appropriate ER-positive breast-cancer model: generate isogenic reference and alternate alleles, measure TOX3 expression, and assess allele-specific TF occupancy. First verify that the element is active in the chosen model; MCF-7 is classified as inactive at this cCRE.

## Flags

- none
