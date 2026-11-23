# rs12740374 and LDL cholesterol, myocardial infarction (1p13) (v8, full, masked, seed 0)

Context: DepMap:ACH-000625 (Hep 3B2.1-7) (given: given with the case).

**Verdict: mechanism.** SOX13 meets every check.

- TF mechanism: mechanism (SOX13 meets every check)
- Target gene: SORT1 (direct: eQTL for SORT1 in Liver (NES +1.27))
- Disease link: supported (GWAS Catalog: low density lipoprotein cholesterol (LDLC, maximum, inv-norm transformed) (p 4.0e-164); 107 matching association(s) in all)

Cost $0.013 over 5 model calls; 141 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | SOX13 | SORT1 | direct | direct | direct | direct | direct | kept |
| 2 | H1 (F1) | HNF4A | SORT1 | direct | direct | direct | direct | direct | kept |
| 3 | H3 (F3) | FOXP1 | SORT1 | direct | direct | direct | direct | direct | kept |
| 4 | H4 (F4) | SP1 | SORT1 | direct | direct | direct | direct | direct | kept |
| 5 | H5 (F5) | TCF7L2 | SORT1 | direct | direct | direct | direct | direct | kept |

## Family screen

- F1 Nuclear receptor, 29 models: named HNF4A (z 11.41); ChIP tier here 1, anywhere 1
- F2 HMG/Sox, 18 models: named SOX13 (z -8.25); ChIP tier here 1, anywhere 1
- F3 Forkhead, 10 models: named FOXP4 (z 6.51); ChIP tier here 1, anywhere 1
- F4 C2H2 ZF, 5 models: named SP1 (z -5.32); ChIP tier here 1, anywhere 1
- F5 HMG/Sox, 3 models: named TCF7L2 (z 4.85); ChIP tier here 1, anywhere 1
- F6 Nuclear receptor, 2 models: named HNF4G (z -4.69); ChIP tier here 1, anywhere 1
- F7 Ets, 18 models: named GABPA (z 4.5); ChIP tier here 1, anywhere 1
- F8 Forkhead, 4 models: named FOXO1 (z 4.45); ChIP tier here 1, anywhere 1
- F9 CCCH ZF, 1 model: named ZGPAT (z -4.08); ChIP tier here 1, anywhere 1
- F10 bZIP, 3 models: named CEBPB (z 22.81); ChIP tier here 2, anywhere 1
- F11 Forkhead, 4 models: named FOXA1 (z 9.02); ChIP tier here 2, anywhere 1
- F12 Rel, 2 models: named NFKB2 (z -7.4); ChIP tier here 2, anywhere 1

## Next experiment

In an allele-aware HepG2 assay, compare G and T for HNF4A and FOXP1 occupancy at EH38E1374646 and measure SORT1 expression after editing the site; include TF perturbation to test whether either factor mediates the allele-dependent effect.

## Flags

- none
