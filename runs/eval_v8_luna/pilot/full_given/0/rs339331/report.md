# rs339331 and Prostate cancer (6q22) (v8, full, masked, seed 0)

Context: DepMap:ACH-000977 (LNCaP clone FGC) (given: given with the case).

**Verdict: mechanism.** HOXB13 meets every check.

- TF mechanism: mechanism (HOXB13 meets every check)
- Target gene: RFX6 is prioritized as a likely target by the prostate cancer L2G results; the element-to-RFX6 link is not directly demonstrated. (untested: nothing links the element to RFX6 is prioritized as a likely target by the prostate cancer L2G results; the element-to-RFX6 link is not directly demonstrated.)
- Disease link: supported (GWAS Catalog: Prostate cancer (p 5.0e-20); 33 matching association(s) in all)

Cost $0.012 over 5 model calls; 148 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | F1 (F1) | HOXB13 | RFX6 is prioritized as a likely target by the prostate cancer L2G results; the element-to-RFX6 link is not directly demonstrated. | direct | direct | supporting | untested | supporting | kept |
| 2 | F2 (F2) | VDR | RFX6 is prioritized as a likely target by the prostate cancer L2G results; the element-to-RFX6 link is not directly demonstrated. | direct | direct | supporting | untested | supporting | kept |
| 3 | F3 (F3) | AR | RFX6 is prioritized as a likely target by the prostate cancer L2G results; the element-to-RFX6 link is not directly demonstrated. | direct | direct | supporting | untested | supporting | kept |
| 4 | F4 (F4) | VDR | RFX6 is prioritized as a likely target by the prostate cancer L2G results; the element-to-RFX6 link is not directly demonstrated. | direct | direct | supporting | untested | supporting | kept |
| 5 | F5 (F5) | GATA2 | RFX6 is prioritized as a likely target by the prostate cancer L2G results; the element-to-RFX6 link is not directly demonstrated. | direct | direct | supporting | untested | supporting | kept |

## Family screen

- F1 Homeodomain, 4 models: named HOXB13 (z -103.49); ChIP tier here 1, anywhere 1
- F2 Nuclear receptor, 29 models: named VDR (z 10.34); ChIP tier here 1, anywhere 1
- F3 Nuclear receptor, 4 models: named AR (z 9.5); ChIP tier here 1, anywhere 1
- F4 Nuclear receptor, 3 models: named NR1I3 (z 8.59); ChIP tier here 1, anywhere 1
- F5 GATA, 6 models: named GATA2 (z 6.47); ChIP tier here 1, anywhere 1
- F6 Rel, 1 model: named RELA (z 5.05); ChIP tier here 1, anywhere 1
- F7 HMG/Sox, 18 models: named SOX12 (z 17.04); ChIP tier here 3, anywhere 1
- F8 HMG/Sox, 3 models: named TCF7L2 (z 15.7); ChIP tier here 3, anywhere 2
- F9 C2H2 ZF, 3 models: named ZXDC (z 13.42); ChIP tier here 3, anywhere 2
- F10 Homeodomain, 9 models: named TGIF1 (z 11.43); ChIP tier here 3, anywhere 2
- F11 Homeodomain, 18 models: named HOXC6 (z -84.28); ChIP tier here 3, anywhere 3
- F12 IRF, 2 models: named IRF6 (z 56.39); ChIP tier here 3, anywhere 3

## Next experiment

Use allele-specific assays in LNCaP clone FGC to test occupancy at the endogenous site, prioritizing AR and HOXB13, and combine this with targeted perturbation of the cCRE and measurement of RFX6, FAM162B, and other plausible target-gene expression. This would test allele direction, element function, and the unresolved target link.

## Flags

- none
