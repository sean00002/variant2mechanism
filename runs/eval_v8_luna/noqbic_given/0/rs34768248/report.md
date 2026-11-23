# rs34768248 and Glioblastoma, melanoma, bladder (v8, no_qbic, masked, seed 0)

Context: DepMap:subtype=Glioblastoma (median of 54 lines) (given: given with the case).

**Verdict: no mechanism.** every chain was eliminated.

- TF mechanism: no mechanism (every chain was eliminated)
- Target gene: None (None: no chain)
- Disease link: no association (common variant (MAF 0.0271): neither the GWAS Catalog nor Open Targets lists an association with Glioblastoma, melanoma, bladder)

Cost $0.010 over 4 model calls; 140 s.

## Chains

| Rank | Chain | TF | Gene | Binding | Cell type | Element | Gene link | Disease | Status |
|---|---|---|---|---|---|---|---|---|---|
| - | H1 (F1) | NFE2L2 | TERT | supporting | supporting | contradicted | direct | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H2 (F5) | RUNX1 | TERT | supporting | supporting | contradicted | direct | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H3 (F3) | RELA | TERT | supporting | supporting | contradicted | direct | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H4 (F4) | EGR1 | TERT | supporting | supporting | contradicted | direct | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |
| - | H5 (F2) | ETS1 | TERT | untested | supporting | contradicted | direct | contradicted | eliminated: element: the variant is not in a cCRE and no TF is bound there in the context |

## Family screen

- F1 bZIP, 3 models: named NFE2L1; ChIP tier here 3, anywhere 1
- F2 Ets, 18 models: named ETS1; ChIP tier here 3, anywhere 1
- F3 Rel, 1 model: named RELA; ChIP tier here 3, anywhere 1
- F4 C2H2 ZF, 4 models: named EGR1; ChIP tier here 3, anywhere 1
- F5 Runt, 2 models: named RUNX1; ChIP tier here 3, anywhere 1
- F6 bZIP, 2 models: named JDP2; ChIP tier here 3, anywhere 1
- F7 C2H2 ZF, 1 model: named ZNF207; ChIP tier here 3, anywhere 2
- F8 bZIP, 3 models: named JUN; ChIP tier here 3, anywhere 2
- F9 MBD, 1 model: named MBD3; ChIP tier here 3, anywhere 2
- F10 bHLH, 2 models: named SREBF1; ChIP tier here 3, anywhere 2
- F11 bHLH, 1 model: named MAX; ChIP tier here 3, anywhere 2
- F12 E2F, 4 models: named E2F4; ChIP tier here 3, anywhere 2

## Next experiment

In a relevant glioblastoma model, test the G and A alleles with an allele-resolved binding assay for the nominated TFs, alongside an isogenic allele-editing or reporter assay measuring TERT expression. This would test binding direction and the proposed element-to-gene effect in the same context.

## Flags

- none
