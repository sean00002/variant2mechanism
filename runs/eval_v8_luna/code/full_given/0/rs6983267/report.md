# rs6983267 and Colorectal cancer (8q24) (v8, full, masked, seed None)

Context: DepMap:ACH-000971 (HCT 116) (given: given with the case).

**Verdict: mechanism.** TCF7L2 meets every check.

- TF mechanism: mechanism (TCF7L2 meets every check)
- Target gene: POU5F1B (direct: eQTL for POU5F1B in Colon_Transverse (NES +0.20))
- Disease link: supported (GWAS Catalog: Colorectal cancer (p 2.0e-122); 56 matching association(s) in all)

Cost $0.000 over 0 model calls; 5 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | TCF7L2 | POU5F1B | direct | direct | supporting | direct | direct | kept |
| 2 | H2 (F2) | SRF | POU5F1B | supporting | direct | supporting | direct | direct | kept |
| 3 | H3 (F3) | SP1 | POU5F1B | supporting | direct | supporting | direct | direct | kept |
| 4 | H4 (F4) | HNF4A | POU5F1B | supporting | supporting | supporting | direct | direct | kept |
| 5 | H5 (F5) | NR2F2 | POU5F1B | indirect | supporting | supporting | direct | direct | kept |

## Family screen

- F1 HMG/Sox, 3 models: named TCF7L2 (z -4.66); ChIP tier here 1, anywhere 1
- F2 MADS box, 1 model: named SRF (z -7.74); ChIP tier here 2, anywhere 2
- F3 C2H2 ZF, 5 models: named SP1 (z -4.76); ChIP tier here 2, anywhere 2
- F4 Nuclear receptor, 1 model: named HNF4A (z 53.69); ChIP tier here 3, anywhere 1
- F5 Nuclear receptor, 29 models: named NR2F2 (z 20.82); ChIP tier here 3, anywhere 1
- F6 Nuclear receptor, 3 models: named ESRRA (z 19.58); ChIP tier here 3, anywhere 1
- F7 Homeodomain, 2 models: named SHOX2 (z -10.21); ChIP tier here 3, anywhere 1
- F8 Homeodomain, 81 models: named HOXA9 (z -9.89); ChIP tier here 3, anywhere 1
- F9 Nuclear receptor, 3 models: named VDR (z 9.87); ChIP tier here 3, anywhere 1
- F10 C2H2 ZF, 6 models: named KLF6 (z -9.74); ChIP tier here 3, anywhere 1
- F11 Forkhead, 4 models: named FOXA3 (z -6.77); ChIP tier here 3, anywhere 1
- F12 Ets, 18 models: named EHF (z -5.95); ChIP tier here 3, anywhere 1

## Next experiment

none

## Flags

- none
