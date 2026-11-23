# rs339331 and Prostate cancer (6q22) (v8, full, masked, seed 0)

Context: DepMap:subtype=Prostate Adenocarcinoma (median of 6 lines) (cancer subtype: 'Prostate cancer (6q22)' matches the DepMap Oncotree subtype 'Prostate Adenocarcinoma' (6 lines)).

**Verdict: mechanism.** HOXB13 meets every check.

- TF mechanism: mechanism (HOXB13 meets every check)
- Target gene: RFX6 (indirect: Open Targets L2G 0.87)
- Disease link: supported (GWAS Catalog: Prostate cancer (p 5.0e-20); 33 matching association(s) in all)

Cost $0.012 over 5 model calls; 151 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | HOXB13 | RFX6 | direct | direct | supporting | indirect | direct | kept |
| 2 | H3 (F2) | VDR | RFX6 | direct | direct | supporting | indirect | direct | kept |
| 3 | H2 (F3) | AR | RFX6 | direct | direct | supporting | indirect | direct | kept |
| 4 | H4 (F5) | GATA2 | RFX6 | direct | direct | supporting | indirect | direct | kept |
| 5 | H5 (F4) | NR1I3 | RFX6 | indirect | supporting | supporting | indirect | direct | kept |

## Family screen

- F1 Homeodomain, 4 models: named HOXB13 (z -103.49); ChIP tier here 1, anywhere 1
- F2 Nuclear receptor, 29 models: named VDR (z 10.34); ChIP tier here 1, anywhere 1
- F3 Nuclear receptor, 4 models: named AR (z 9.5); ChIP tier here 1, anywhere 1
- F4 Nuclear receptor, 3 models: named NR1I3 (z 8.59); ChIP tier here 1, anywhere 1
- F5 GATA, 6 models: named GATA2 (z 6.47); ChIP tier here 1, anywhere 1
- F6 Rel, 1 model: named RELA (z 5.05); ChIP tier here 1, anywhere 1
- F7 Nuclear receptor, 1 model: named HNF4G (z 4.94); ChIP tier here 1, anywhere 1
- F8 HMG/Sox, 18 models: named SOX4 (z 17.04); ChIP tier here 3, anywhere 1
- F9 HMG/Sox, 3 models: named LEF1 (z 15.7); ChIP tier here 3, anywhere 2
- F10 C2H2 ZF, 3 models: named ZXDC (z 13.42); ChIP tier here 3, anywhere 2
- F11 Homeodomain, 9 models: named TGIF1 (z 11.43); ChIP tier here 3, anywhere 2
- F12 Homeodomain, 18 models: named HOXC6 (z -84.28); ChIP tier here 3, anywhere 3

## Next experiment

First identify a prostate-relevant model in which EH38E2496909 is active. In that model, compare endogenous T and C alleles by allele-specific TF occupancy and expression of candidate targets, then perturb the implicated TF and CRISPRi the cCRE to test whether occupancy and any allele-dependent expression effect require that element.

## Flags

- none
