# rs6983267 and Colorectal cancer (8q24) (v8, no_qbic, masked, seed 0)

Context: DepMap:ACH-000971 (HCT 116) (given: given with the case).

**Verdict: mechanism.** TCF7L2 meets every check.

- TF mechanism: mechanism (TCF7L2 meets every check)
- Target gene: MYC (supporting: 3D contact with MYC in HCT116 (RNAPII-ChIAPET))
- Disease link: supported (GWAS Catalog: Colorectal cancer (p 2.0e-122); 56 matching association(s) in all)

Cost $0.008 over 3 model calls; 114 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | TCF7L2 | MYC | direct | direct | supporting | supporting | supporting | kept |
| 2 | H2 (F2) | JUND | MYC | supporting | direct | supporting | supporting | supporting | kept |
| 3 | H3 (F3) | YY1 | MYC | supporting | direct | supporting | supporting | supporting | kept |
| 4 | H4 (F4) | SP1 | MYC | supporting | direct | supporting | supporting | supporting | kept |
| 5 | H5 (F5) | CTCF | MYC | supporting | direct | supporting | supporting | supporting | kept |

## Family screen

- F1 HMG/Sox, 3 models: named TCF7L2; ChIP tier here 1, anywhere 1
- F2 bZIP, 3 models: named JUND; ChIP tier here 2, anywhere 1
- F3 C2H2 ZF, 1 model: named YY1; ChIP tier here 2, anywhere 2
- F4 C2H2 ZF, 5 models: named SP1; ChIP tier here 2, anywhere 2
- F5 C2H2 ZF, 1 model: named CTCF; ChIP tier here 2, anywhere 2
- F6 bHLH, 1 model: named MAX; ChIP tier here 2, anywhere 2
- F7 MADS box, 1 model: named SRF; ChIP tier here 2, anywhere 2
- F8 bZIP, 3 models: named CEBPB; ChIP tier here 2, anywhere 2
- F9 bHLH, 3 models: named TCF3; ChIP tier here 3, anywhere 1
- F10 Homeodomain, 81 models: named HOXA9; ChIP tier here 3, anywhere 1
- F11 Ets, 18 models: named EHF; ChIP tier here 3, anywhere 1
- F12 Forkhead, 1 model: named FOXK2; ChIP tier here 3, anywhere 1

## Next experiment

Create isogenic HCT116 G and T alleles (or precisely edit the endogenous site), then measure allele-specific TF occupancy and expression of MYC and other linked genes. Combine this with separate acute perturbations of TCF7L2, JUND, and YY1 to test which factor, if any, makes the variant-dependent regulatory effect.

## Flags

- none
