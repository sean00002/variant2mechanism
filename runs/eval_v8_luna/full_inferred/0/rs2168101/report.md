# rs2168101 and Neuroblastoma (LMO1) (v8, full, masked, seed 0)

Context: DepMap:subtype=Neuroblastoma (median of 36 lines) (cancer subtype: 'Neuroblastoma (LMO1)' matches the DepMap Oncotree subtype 'Neuroblastoma' (36 lines)).

**Verdict: mechanism.** GATA3 meets every check.

- TF mechanism: mechanism (GATA3 meets every check)
- Target gene: LMO1 (supporting: 3D contact with LMO1 in SK-N-SH (RNAPII-ChIAPET))
- Disease link: supported (GWAS Catalog: Sporadic neuroblastoma (p 3.0e-16); 2 matching association(s) in all)

Cost $0.011 over 5 model calls; 116 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H1 (F1) | GATA3 | LMO1 | direct | direct | supporting | supporting | direct | kept |
| 2 | H2 (F2) | ISL1 | LMO1 | direct | direct | supporting | supporting | direct | kept |
| 3 | H3 (F3) | TBX2 | LMO1 | direct | direct | supporting | supporting | direct | kept |
| 4 | H4 (F4) | RARA | LMO1 | direct | direct | supporting | supporting | direct | kept |
| 5 | H5 (F5) | EBF3 | LMO1 | direct | direct | supporting | supporting | direct | kept |

## Family screen

- F1 GATA, 6 models: named GATA3 (z -56.07); ChIP tier here 1, anywhere 1
- F2 Homeodomain, 81 models: named ISL1 (z 17.7); ChIP tier here 1, anywhere 1
- F3 T-box, 4 models: named TBX2 (z 11.68); ChIP tier here 1, anywhere 1
- F4 Nuclear receptor, 29 models: named RARA (z 10.15); ChIP tier here 1, anywhere 1
- F5 EBF1, 2 models: named EBF3 (z 4.95); ChIP tier here 1, anywhere 1
- F6 TEA, 4 models: named TEAD4 (z -4.85); ChIP tier here 1, anywhere 1
- F7 Forkhead, 10 models: named FOXJ3 (z 26.8); ChIP tier here 2, anywhere 2
- F8 C2H2 ZF, 1 model: named ZNF8 (z 16.02); ChIP tier here 2, anywhere 2
- F9 C2H2 ZF, 1 model: named ZFP3 (z 10.67); ChIP tier here 2, anywhere 2
- F10 Forkhead, 1 model: named FOXK2 (z 10.31); ChIP tier here 2, anywhere 2
- F11 Forkhead, 1 model: named FOXP1 (z 9.6); ChIP tier here 2, anywhere 2
- F12 Forkhead, 1 model: named FOXK1 (z 7.57); ChIP tier here 2, anywhere 2

## Next experiment

In heterozygous neuroblastoma models with confirmed expression, perform allele-specific GATA3 occupancy profiling at the site, followed by GATA3 perturbation and measurement of LMO1 expression. This would test H1's ref-favored prediction and whether occupancy connects to the proposed target gene.

## Flags

- none
