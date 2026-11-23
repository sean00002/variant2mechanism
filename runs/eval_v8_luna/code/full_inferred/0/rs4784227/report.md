# rs4784227 and Breast cancer (16q12) (v8, full, masked, seed None)

Context: DepMap:subtype=Breast Invasive Ductal Carcinoma (median of 32 lines) (cancer subtype: 'Breast cancer (16q12)' matches the DepMap Oncotree subtype 'Breast Invasive Ductal Carcinoma' (32 lines)).

**Verdict: mechanism.** GATA3 meets every check.

- TF mechanism: mechanism (GATA3 meets every check)
- Target gene: TOX3 (indirect: Open Targets L2G 0.96)
- Disease link: supported (GWAS Catalog: Breast cancer (p 2.0e-240); 63 matching association(s) in all)

Cost $0.000 over 0 model calls; 2 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | GATA3 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 2 | H2 (F2) | FOXA1 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 3 | H3 (F3) | ESR1 | TOX3 | direct | direct | supporting | indirect | direct | kept |
| 4 | H4 (F4) | NR3C1 | TOX3 | supporting | direct | supporting | indirect | direct | kept |
| 5 | H5 (F5) | PITX1 | TOX3 | indirect | supporting | supporting | indirect | direct | kept |

## Family screen

- F1 GATA, 6 models: named GATA3 (z 18.65); ChIP tier here 1, anywhere 1
- F2 Forkhead, 4 models: named FOXA1 (z 15.4); ChIP tier here 1, anywhere 1
- F3 Nuclear receptor, 29 models: named ESR1 (z 9.51); ChIP tier here 1, anywhere 1
- F4 Nuclear receptor, 4 models: named NR3C1 (z -5.97); ChIP tier here 2, anywhere 1
- F5 Homeodomain, 81 models: named PITX1 (z 28.05); ChIP tier here 3, anywhere 1
- F6 bHLH, 1 model: named TFAP4 (z 19.55); ChIP tier here 3, anywhere 1
- F7 Forkhead, 10 models: named FOXK2 (z 17.15); ChIP tier here 3, anywhere 1
- F8 CUT; Homeodomain, 2 models: named CUX1 (z -12.07); ChIP tier here 3, anywhere 1
- F9 Ets, 18 models: named ELF3 (z 10.52); ChIP tier here 3, anywhere 1
- F10 Homeodomain, 18 models: named HOXC10 (z -10.35); ChIP tier here 3, anywhere 1
- F11 HMG/Sox, 18 models: named SOX4 (z -10.04); ChIP tier here 3, anywhere 1
- F12 C2H2 ZF, 1 model: named ZNF384 (z -9.91); ChIP tier here 3, anywhere 1

## Next experiment

none

## Flags

- none
