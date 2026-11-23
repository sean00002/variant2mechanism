# rs4784227 and Breast cancer (16q12) (v8, full, named, seed 0)

Context: DepMap:ACH-000019 (MCF7) (given: given with the case).

**Verdict: mechanism.** GATA3 meets every check.

- TF mechanism: mechanism (GATA3 meets every check)
- Target gene: TOX3 (indirect: Open Targets L2G 0.96)
- Disease link: supported (GWAS Catalog: Breast cancer (p 2.0e-240); 63 matching association(s) in all)

Cost $0.013 over 6 model calls; 157 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | GATA3 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 2 | H1 (F1) | MSX2 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 3 | H3 (F3) | FOXA1 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 4 | H4 (F4) | CUX1 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 5 | H5 (F5) | ESR1 | TOX3 | direct | direct | supporting | indirect | direct | kept |

## Family screen

- F1 Homeodomain, 81 models: named MSX2 (z 28.05); ChIP tier here 1, anywhere 1
- F2 GATA, 6 models: named GATA3 (z 18.65); ChIP tier here 1, anywhere 1
- F3 Forkhead, 4 models: named FOXA1 (z 15.4); ChIP tier here 1, anywhere 1
- F4 CUT; Homeodomain, 2 models: named CUX1 (z -12.07); ChIP tier here 1, anywhere 1
- F5 Nuclear receptor, 29 models: named ESR1 (z 9.51); ChIP tier here 1, anywhere 1
- F6 bZIP, 2 models: named CREB1 (z 7.55); ChIP tier here 1, anywhere 1
- F7 E2F, 4 models: named E2F1 (z -6.05); ChIP tier here 1, anywhere 1
- F8 TEA, 4 models: named TEAD4 (z -4.83); ChIP tier here 1, anywhere 1
- F9 Ets, 18 models: named SPDEF (z 10.52); ChIP tier here 2, anywhere 1
- F10 Nuclear receptor, 4 models: named NR3C1 (z -5.97); ChIP tier here 2, anywhere 1
- F11 HMG/Sox, 3 models: named TCF7L2 (z 8.45); ChIP tier here 2, anywhere 2
- F12 C2H2 ZF, 3 models: named ZXDC (z 4.78); ChIP tier here 2, anywhere 2

## Next experiment

In a breast-cancer model where EH38E3180851 is confirmed active, introduce the C and T alleles by endogenous base editing, measure allele-specific FOXA1 and ESR1 occupancy and TOX3 expression, and test whether FOXA1 perturbation changes the allele-dependent effect.

## Flags

- none
