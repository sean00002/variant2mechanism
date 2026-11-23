# rs6983267 and Colorectal cancer (8q24) (v8, full, named, seed 0)

Context: DepMap:ACH-000971 (HCT 116) (given: given with the case).

**Verdict: mechanism.** TCF7L2 meets every check.

- TF mechanism: mechanism (TCF7L2 meets every check)
- Target gene: MYC (supporting: 3D contact with MYC in HCT116 (RNAPII-ChIAPET))
- Disease link: supported (GWAS Catalog: Colorectal cancer (p 2.0e-122); 56 matching association(s) in all)

Cost $0.011 over 5 model calls; 160 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | TCF7L2 | MYC | direct | direct | supporting | supporting | supporting | kept |
| 2 | H2 (F2) | SRF | MYC | supporting | direct | supporting | supporting | supporting | kept |
| 3 | H3 (F3) | SP1 | MYC | supporting | direct | supporting | supporting | supporting | kept |
| 4 | H4 (F4) | HNF4A | MYC | supporting | supporting | supporting | supporting | supporting | kept |
| 5 | H5 (F5) | NR2F2 | MYC | indirect | supporting | supporting | supporting | supporting | kept |

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

Use isogenic HCT116 cells edited to carry G or T at rs6983267 to measure allele-dependent SRF occupancy at the element and MYC expression, with SRF perturbation to test whether any allele effect depends on SRF.

## Literature flags

- H1: PMID 34830370 (variant and TF, complete chain)

## Flags

- none
