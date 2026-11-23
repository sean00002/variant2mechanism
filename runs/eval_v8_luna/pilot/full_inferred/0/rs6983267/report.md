# rs6983267 and Colorectal cancer (8q24) (v8, full, masked, seed 0)

Context: DepMap:subtype=Colon Adenocarcinoma (median of 66 lines) (cancer subtype: 'Colorectal cancer (8q24)' matches the DepMap Oncotree subtype 'Colon Adenocarcinoma' (66 lines)).

**Verdict: mechanism.** HNF4A meets every check.

- TF mechanism: mechanism (HNF4A meets every check)
- Target gene: POU5F1B (direct: eQTL for POU5F1B in Colon_Transverse (NES +0.20))
- Disease link: supported (GWAS Catalog: Colorectal cancer (p 2.0e-122); 56 matching association(s) in all)

Cost $0.012 over 5 model calls; 145 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | HNF4A | POU5F1B | direct | direct | direct | direct | direct | kept |
| 2 | H2 (F2) | PPARG | POU5F1B | direct | direct | direct | direct | direct | kept |
| 3 | H3 (F3) | VDR | POU5F1B | direct | direct | direct | direct | direct | kept |
| 4 | H4 (F4) | KLF5 | POU5F1B | direct | direct | direct | direct | direct | kept |
| 5 | H5 (F5) | FOXA2 | POU5F1B | direct | direct | direct | direct | direct | kept |

## Family screen

- F1 Nuclear receptor, 1 model: named HNF4A (z 53.69); ChIP tier here 1, anywhere 1
- F2 Nuclear receptor, 29 models: named PPARG (z 20.82); ChIP tier here 1, anywhere 1
- F3 Nuclear receptor, 3 models: named VDR (z 9.87); ChIP tier here 1, anywhere 1
- F4 C2H2 ZF, 6 models: named KLF5 (z -9.74); ChIP tier here 1, anywhere 1
- F5 Forkhead, 4 models: named FOXA2 (z -6.77); ChIP tier here 1, anywhere 1
- F6 HMG/Sox, 3 models: named TCF7L2 (z -4.66); ChIP tier here 1, anywhere 1
- F7 HMG/Sox, 18 models: named SOX9 (z -9.03); ChIP tier here 2, anywhere 2
- F8 MADS box, 1 model: named SRF (z -7.74); ChIP tier here 2, anywhere 2
- F9 bHLH, 1 model: named NCOA1 (z -4.87); ChIP tier here 2, anywhere 2
- F10 C2H2 ZF, 5 models: named SP1 (z -4.76); ChIP tier here 2, anywhere 2
- F11 Prospero, 1 model: named PROX1 (z -4.17); ChIP tier here 2, anywhere 2
- F12 Nuclear receptor, 3 models: named ESRRA (z 19.58); ChIP tier here 3, anywhere 1

## Next experiment

In Caco-2 cells, perform an isogenic G-to-T edit followed by allele-specific HNF4A occupancy measurement and POU5F1B expression analysis; this tests the newly strengthened H1 occupancy link as well as its proposed downstream gene effect.

## Flags

- none
