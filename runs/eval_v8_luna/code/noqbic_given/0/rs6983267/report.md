# rs6983267 and Colorectal cancer (8q24) (v8, no_qbic, masked, seed None)

Context: DepMap:ACH-000971 (HCT 116) (given: given with the case).

**Verdict: mechanism.** TCF7L2 meets every check.

- TF mechanism: mechanism (TCF7L2 meets every check)
- Target gene: POU5F1B (direct: eQTL for POU5F1B in Colon_Transverse (NES +0.20))
- Disease link: supported (GWAS Catalog: Colorectal cancer (p 2.0e-122); 56 matching association(s) in all)

Cost $0.000 over 0 model calls; 4 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | TCF7L2 | POU5F1B | direct | direct | supporting | direct | direct | kept |
| 2 | H2 (F2) | JUND | POU5F1B | supporting | direct | supporting | direct | direct | kept |
| 3 | H3 (F3) | YY1 | POU5F1B | supporting | direct | supporting | direct | direct | kept |
| 4 | H4 (F4) | SP1 | POU5F1B | supporting | direct | supporting | direct | direct | kept |
| 5 | H5 (F5) | CTCF | POU5F1B | supporting | direct | supporting | direct | direct | kept |

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

none

## Flags

- none
