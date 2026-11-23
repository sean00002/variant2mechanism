# rs12740374 and LDL cholesterol, myocardial infarction (1p13) (v8, full, masked, seed None)

Context: GTEx:Muscle - Skeletal (eQTL tissue: the variant's strongest GTEx eQTL is for CELSR2 in Muscle - Skeletal (p 2.3e-76)).

**Verdict: mechanism.** CEBPB meets every check.

- TF mechanism: mechanism (CEBPB meets every check)
- Target gene: CELSR2 (direct: eQTL for CELSR2 in Muscle_Skeletal (NES +0.54))
- Disease link: supported (GWAS Catalog: low density lipoprotein cholesterol (LDLC, maximum, inv-norm transformed) (p 4.0e-164); 107 matching association(s) in all)

Cost $0.000 over 0 model calls; 1 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | CEBPB | CELSR2 | supporting | supporting | indirect | direct | direct | kept |
| - | H1 (F1) | NKX2-5 | CELSR2 | indirect | indirect | contradicted | direct | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |
| - | H3 (F3) | TFAP2E | CELSR2 | indirect | indirect | contradicted | direct | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |
| - | H4 (F4) | RFX5 | CELSR2 | supporting | supporting | contradicted | direct | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |
| - | H5 (F5) | NKX3-1 | CELSR2 | supporting | supporting | contradicted | direct | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |

## Family screen

- F1 Homeodomain, 3 models: named NKX2-5 (z -27.46); ChIP tier here 3, anywhere 1
- F2 bZIP, 3 models: named CEBPB (z 22.81); ChIP tier here 3, anywhere 1
- F3 AP-2, 4 models: named TFAP2E (z -21.21); ChIP tier here 3, anywhere 1
- F4 RFX, 2 models: named RFX5 (z 18.73); ChIP tier here 3, anywhere 1
- F5 Homeodomain, 2 models: named NKX3-1 (z -17.61); ChIP tier here 3, anywhere 1
- F6 C2H2 ZF, 2 models: named GFI1 (z 14.71); ChIP tier here 3, anywhere 1
- F7 Nuclear receptor, 29 models: named ESRRA (z 11.41); ChIP tier here 3, anywhere 1
- F8 bZIP, 1 model: named MAFF (z 10.86); ChIP tier here 3, anywhere 1
- F9 Homeodomain, 81 models: named HOXC9 (z -10.43); ChIP tier here 3, anywhere 1
- F10 Forkhead, 4 models: named FOXS1 (z 9.02); ChIP tier here 3, anywhere 1
- F11 Homeodomain, 18 models: named HOXC10 (z -8.73); ChIP tier here 3, anywhere 1
- F12 HMG/Sox, 18 models: named SOX18 (z -8.25); ChIP tier here 3, anywhere 1

## Next experiment

none

## Flags

- none
