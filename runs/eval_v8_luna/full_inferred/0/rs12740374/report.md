# rs12740374 and LDL cholesterol, myocardial infarction (1p13) (v8, full, masked, seed 0)

Context: GTEx:Muscle - Skeletal (eQTL tissue: the variant's strongest GTEx eQTL is for CELSR2 in Muscle - Skeletal (p 2.3e-76)).

**Verdict: mechanism.** CEBPB meets every check.

- TF mechanism: mechanism (CEBPB meets every check)
- Target gene: SORT1 (supporting: eQTL for SORT1 in Liver (another tissue))
- Disease link: supported (GWAS Catalog: low density lipoprotein cholesterol (LDLC, maximum, inv-norm transformed) (p 4.0e-164); 107 matching association(s) in all)

Cost $0.010 over 3 model calls; 130 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | H2 (F2) | CEBPB | SORT1 | supporting | supporting | indirect | supporting | direct | kept |
| - | H1 (F1) | NKX2-5 | SORT1 | indirect | indirect | contradicted | supporting | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |
| - | H3 (F3) | TFAP2E | SORT1 | indirect | indirect | contradicted | supporting | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |
| - | H4 (F4) | RFX5 | SORT1 | supporting | supporting | contradicted | supporting | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |
| - | H5 (F5) | NKX3-1 | SORT1 | supporting | supporting | contradicted | supporting | direct | eliminated: element: inactive (Low-DNase) in cardiac muscle cell, and no TF bound there |

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

In a disease-relevant hepatocyte model, perform allele-specific CEBPB occupancy testing at the variant and an isogenic G-to-T edit with SORT1 expression readout; include CEBPB perturbation to test whether any allele-dependent expression effect depends on CEBPB. If the skeletal-muscle cell-type claim is retained, test occupancy there separately rather than inferring it from the current unmatched assays.

## Flags

- tool_failed: E27 gene_disease: Open Targets lookup failed: no disease matches 'LDL cholesterol, myocardial infarction'
