# rs1421085 and Obesity (FTO) (v8, full, masked, seed None)

Context: GTEx:Muscle - Skeletal (eQTL tissue: the variant's strongest GTEx eQTL is for FTO in Muscle - Skeletal (p 7.5e-08)).

**Verdict: no mechanism.** no chain meets the minimum; the top chain (FOXS1) fails: expressed.

- TF mechanism: no mechanism (no chain meets the minimum; the top chain (FOXS1) fails: expressed)
- Target gene: FTO (direct: eQTL for FTO in Muscle_Skeletal (NES +0.14))
- Disease link: supported (GWAS Catalog: Body mass index (BMI, mean, inv-normal transformed) (p 9.9e-324); 28 matching association(s) in all)

Cost $0.000 over 0 model calls; 1 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | FOXS1 | FTO | indirect | indirect | indirect | direct | direct | kept |
| - | H1 (F1) | ONECUT2 | FTO | supporting | indirect | contradicted | direct | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |
| - | H3 (F3) | PAX7 | FTO | supporting | supporting | contradicted | direct | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |
| - | H4 (F4) | HOXC9 | FTO | indirect | supporting | contradicted | direct | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |
| - | H5 (F5) | GATA2 | FTO | indirect | supporting | contradicted | direct | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |

## Family screen

- F1 CUT; Homeodomain, 3 models: named ONECUT2 (z -47.91); ChIP tier here 3, anywhere 1
- F2 Forkhead, 4 models: named FOXS1 (z -23.72); ChIP tier here 3, anywhere 1
- F3 Paired box, 8 models: named PAX7 (z 22.55); ChIP tier here 3, anywhere 1
- F4 Homeodomain, 81 models: named HOXC9 (z -21.48); ChIP tier here 3, anywhere 1
- F5 GATA, 6 models: named GATA2 (z -18.66); ChIP tier here 3, anywhere 1
- F6 HMG/Sox, 3 models: named TCF7L1 (z 8.64); ChIP tier here 3, anywhere 1
- F7 Homeodomain, 18 models: named HOXC10 (z -7.79); ChIP tier here 3, anywhere 1
- F8 Nuclear receptor, 3 models: named ESRRA (z 62.01); ChIP tier here 3, anywhere 2
- F9 Nuclear receptor, 29 models: named NR4A1 (z 32.74); ChIP tier here 3, anywhere 2
- F10 Forkhead, 10 models: named FOXJ3 (z -32.62); ChIP tier here 3, anywhere 2
- F11 bZIP, 2 models: named ATF3 (z 21.73); ChIP tier here 3, anywhere 2
- F12 TEA, 4 models: named TEAD4 (z 21.23); ChIP tier here 3, anywhere 2

## Next experiment

none

## Flags

- none
