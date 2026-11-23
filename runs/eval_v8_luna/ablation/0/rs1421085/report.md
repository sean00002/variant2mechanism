# rs1421085 and Obesity (FTO) (v8, full, masked, seed 0)

Context: GTEx:Adipose - Subcutaneous (proxy for preadipocytes) (given: given with the case).

**Verdict: undetermined.** ONECUT1: not shown: expressed, element open.

- TF mechanism: undetermined (ONECUT1: not shown: expressed, element open)
- Target gene: FTO (supporting: eQTL for FTO in Muscle_Skeletal (another tissue))
- Disease link: supported (GWAS Catalog: Body mass index (BMI, mean, inv-normal transformed) (p 9.9e-324); 28 matching association(s) in all)

Cost $0.009 over 3 model calls; 117 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | ONECUT1 | FTO | supporting | indirect | untested | supporting | direct | kept |
| 2 | H2 (F2) | FOXS1 | FTO | indirect | supporting | untested | supporting | direct | kept |
| 3 | H3 (F3) | PAX8 | FTO | indirect | supporting | untested | supporting | direct | kept |
| 4 | H4 (F4) | PRRX1 | FTO | indirect | supporting | untested | supporting | direct | kept |
| 5 | H5 (F5) | GATA2 | FTO | indirect | supporting | untested | supporting | direct | kept |

## Family screen

- F1 CUT; Homeodomain, 3 models: named ONECUT1 (z -47.91); ChIP tier here 3, anywhere 1
- F2 Forkhead, 4 models: named FOXS1 (z -23.72); ChIP tier here 3, anywhere 1
- F3 Paired box, 8 models: named PAX8 (z 22.55); ChIP tier here 3, anywhere 1
- F4 Homeodomain, 81 models: named PRRX1 (z -21.48); ChIP tier here 3, anywhere 1
- F5 GATA, 6 models: named GATA2 (z -18.66); ChIP tier here 3, anywhere 1
- F6 HMG/Sox, 3 models: named TCF7L1 (z 8.64); ChIP tier here 3, anywhere 1
- F7 Homeodomain, 18 models: named MEOX2 (z -7.79); ChIP tier here 3, anywhere 1
- F8 Nuclear receptor, 3 models: named ESRRA (z 62.01); ChIP tier here 3, anywhere 2
- F9 Nuclear receptor, 29 models: named NR4A1 (z 32.74); ChIP tier here 3, anywhere 2
- F10 Forkhead, 10 models: named FOXJ3 (z -32.62); ChIP tier here 3, anywhere 2
- F11 bZIP, 2 models: named ATF3 (z 21.73); ChIP tier here 3, anywhere 2
- F12 TEA, 4 models: named TEAD1 (z 21.23); ChIP tier here 3, anywhere 2

## Next experiment

In adipocyte precursor cells, test the allele-dependent regulatory effect of EH38E3181208 on FTO with an allele-aware perturbation assay, and assess whether candidate-TF perturbation changes that effect. Include direct occupancy validation for the prioritized TF rather than inferring member-specific binding from family models.

## Flags

- none
