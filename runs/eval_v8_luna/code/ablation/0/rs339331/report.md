# rs339331 and Prostate cancer (6q22) (v8, full, masked, seed None)

Context: DepMap:ACH-000977 (LNCaP clone FGC) (given: given with the case).

**Verdict: mechanism.** VDR meets every check.

- TF mechanism: mechanism (VDR meets every check)
- Target gene: FAM162B (supporting: eQTL for FAM162B in Adipose_Subcutaneous (another tissue))
- Disease link: supported (GWAS Catalog: Prostate cancer (p 5.0e-20); 33 matching association(s) in all)

Cost $0.000 over 0 model calls; 1 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | VDR | FAM162B | direct | direct | supporting | supporting | supporting | kept |
| 2 | H2 (F2) | AR | FAM162B | direct | direct | supporting | supporting | supporting | kept |
| 3 | H4 (F4) | GATA2 | FAM162B | direct | direct | supporting | supporting | supporting | kept |
| 4 | H5 (F5) | RELA | FAM162B | direct | direct | supporting | supporting | supporting | kept |
| 5 | H3 (F3) | NR1I3 | FAM162B | indirect | supporting | supporting | supporting | supporting | kept |

## Family screen

- F1 Nuclear receptor, 29 models: named VDR (z 10.34); ChIP tier here 1, anywhere 1
- F2 Nuclear receptor, 4 models: named AR (z 9.5); ChIP tier here 1, anywhere 1
- F3 Nuclear receptor, 3 models: named NR1I3 (z 8.59); ChIP tier here 1, anywhere 1
- F4 GATA, 6 models: named GATA2 (z 6.47); ChIP tier here 1, anywhere 1
- F5 Rel, 1 model: named RELA (z 5.05); ChIP tier here 1, anywhere 1
- F6 HMG/Sox, 18 models: named SOX12 (z 17.04); ChIP tier here 3, anywhere 1
- F7 HMG/Sox, 3 models: named TCF7L2 (z 15.7); ChIP tier here 3, anywhere 2
- F8 C2H2 ZF, 3 models: named ZXDC (z 13.42); ChIP tier here 3, anywhere 2
- F9 Homeodomain, 9 models: named TGIF1 (z 11.43); ChIP tier here 3, anywhere 2
- F10 Homeodomain, 4 models: named HOXC13 (z -103.49); ChIP tier here 3, anywhere 3
- F11 Homeodomain, 18 models: named HOXC6 (z -84.28); ChIP tier here 3, anywhere 3
- F12 IRF, 2 models: named IRF6 (z 56.39); ChIP tier here 3, anywhere 3

## Next experiment

none

## Flags

- none
