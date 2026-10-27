# Screen v1 against screen v2 (spec 3, checkpoint 3)

DeepSeek V4.1 Flash (`deepseek/deepseek-v4.1-flash-1017`) for all three roles, named mode, seed 0, all 15 gold-set
cases (9 TF cases, 3 random controls, 3 near-miss controls). Counts, not percentages.

- **v1** (`runs/eval_deepseek`): the 25-26 October grid on the chat-completions client, plus the 9 near-miss runs
  made on 26 October with the same v1 code (commit `bb18f04`), so that both versions cover the same 15 cases.
- **v2** (`runs/eval_v2_deepseek`): spec 3 (commit `eaa1c0f`): occupancy in gather, screen v2 in `full`, no
  `qbic_coverage` field, the occupancy principle in the generator prompt, the new binding rubric for the critic, and
  `eqtl_lookup` in gather. `single` changed only through the prompt.

Reproduce with `uv run python scripts/compare_screens.py`.

## Summary

| | v1 single | v2 single | v1 no_qbic | v2 no_qbic | v1 full | v2 full |
|---|---|---|---|---|---|---|
| Gold TF ranked first | 8 of 9 | 6 of 9 | 5 of 9 | 5 of 9 | 3 of 9 | 4 of 9 |
| Gold TF in top 3 | 8 of 9 | 9 of 9 | 7 of 9 | 7 of 9 | 7 of 9 | 9 of 9 |
| Direction right (when the gold TF is ranked) | 7 of 8 | 7 of 9 | 7 of 7 | 7 of 7 | 6 of 7 | 9 of 9 |
| Random controls: null ranked first | 3 of 3 | 3 of 3 | 3 of 3 | 3 of 3 | 3 of 3 | 2 of 2 |
| Random controls: over-claiming (mean) | 0.58 | 0.55 | 0.13 | 0.07 | 0.31 | 0.15 |
| Near-miss controls: null ranked first | 3 of 3 | 0 of 3 | 3 of 3 | 3 of 3 | 3 of 3 | 3 of 3 |
| Near-miss controls: over-claiming (mean) | 0.51 | 0.70 | 0.36 | 0.37 | 0.47 | 0.58 |
| Answer in the evidence (retrieval audit) | 0 of 9 | 0 of 9 | 4 of 9 | 6 of 9 | 3 of 9 | 7 of 9 |
| Agent asked a tool about the gold TF | 0 of 9 | 0 of 9 | 7 of 9 | 7 of 9 | 7 of 9 | 8 of 9 |
| Gold TF led before any agent-chosen tool | 8 of 9 | 8 of 9 | 6 of 9 | 6 of 9 | 5 of 9 | 4 of 9 |
| Investigate calls per run (mean) | 0.00 | 0.00 | 3.00 | 3.00 | 2.93 | 3.00 |
| Runs scored | 15 | 15 | 15 | 15 | 15 | 14 |
| Cost, total | $0.06 | $0.06 | $0.39 | $0.44 | $0.35 | $0.44 |

One v2 run failed: `full` on the random control rs13078086 (the critic's regrade left links ungraded twice), so v2
`full` has 2 random controls, not 3.

## Gold TF rank per case (chains in rank order; "absent" means no chain names the gold TF)

| Case | v1 no_qbic | v2 no_qbic | v1 full | v2 full |
|---|---|---|---|---|
| tert_c228t | rank 1 | rank 1 | rank 1 | rank 1 |
| tert_c250t | rank 2 | rank 2 | rank 1 | rank 1 |
| rs6983267 | rank 1 | rank 1 | rank 3 | rank 2 |
| rs4784227 | rank 1 | rank 1 | absent | rank 2 |
| rs339331 | absent | absent | rank 3 | rank 3 |
| rs2168101 | rank 2 | rank 1 | rank 3 | rank 3 |
| rs12740374 | rank 1 | rank 1 | rank 1 | rank 3 |
| rs1421085 | rank 1 | rank 2 | rank 2 | rank 1 |
| rs642961 | absent | absent | absent | rank 1 |
| rs13078086 | null first, over-claim 0.12 | null first, over-claim 0.06 | null first, over-claim 0.45 | not run |
| rs11629191 | null first, over-claim 0.20 | null first, over-claim 0.05 | null first, over-claim 0.25 | null first, over-claim 0.13 |
| rs7001688 | null first, over-claim 0.08 | null first, over-claim 0.11 | null first, over-claim 0.22 | null first, over-claim 0.18 |
| rs73706717 | null first, over-claim 0.34 | null first, over-claim 0.54 | null first, over-claim 0.53 | null first, over-claim 0.55 |
| rs34768248 | null first, over-claim 0.35 | null first, over-claim 0.14 | null first, over-claim 0.38 | null first, over-claim 0.62 |
| rs56007086 | null first, over-claim 0.40 | null first, over-claim 0.42 | null first, over-claim 0.50 | null first, over-claim 0.57 |

## What changed

1. **`full` improved on the TF cases.** The gold TF is in the top 3 in 9 of 9 cases (v1: 7 of 9) and ranked first
   in 4 of 9 (v1: 3 of 9); the direction is right in all 9 (v1: 6 of 7). Two cases came back: TFAP2A at rs642961
   (absent in v1, first in v2) and FOXA1 at rs4784227 (absent, then second, behind GATA3). One got worse: CEBPA at
   rs12740374 (first, then third).
2. **Random controls: over-claiming in `full` halved,** 0.31 to 0.15. At rs11629191 the XBP1 group that led the v1
   screen is gone: XBP1 was assayed in MCF-7 with no peak at the SNP, so screen v2 leaves it out.
3. **Near-miss controls: the null still comes first in 3 of 3, but over-claiming rose in `full`,** 0.47 to 0.58.
   The near-miss SNPs share the famous element's ChIP peaks, and the occupied TFs still pass the |z| gate there, so
   the agent proposes mechanisms. The gate does not separate the causal SNP from its near-miss; site strength does:

   | TF | Causal SNP: z, effect, site percentile (ref / alt) | Near-miss SNP: z, effect, site percentile (ref / alt) |
   | --- | --- | --- |
   | TCF7L2 (rs6983267 / rs73706717) | -4.66, -0.47, 98.8 / 98.4 | -8.80, -0.43, 90.0 / 87.2 |
   | FOXA1 (rs4784227 / rs56007086) | +15.4, +0.30, 91.3 / 98.8 | +6.27, +0.13, 90.2 / 81.8 |
   | GABPA (TERT C228T / rs34768248) | +124.3, +2.51, 92.6 / 100.0 | +8.55, +0.23, 61.8 / 79.3 |

   At the causal SNPs one allele touches a k-mer at the 98.8th to 100th percentile of the model's coefficients; at
   the near-miss SNPs neither allele reaches the 91st. Three pairs only, and site strength is not yet a rule in the
   screen: that is a decision still to make.
4. **Retrieval audit:** in v2 `full` the answer appears in the evidence in 7 of 9 cases (v1: 3 of 9), and the gold
   TF led the chains before any agent-chosen tool in 4 of 9 (v1: 5 of 9).
5. **`single` (no tools) moved with the prompt alone,** first 8 of 9 to 6 of 9, and on the near-miss controls the
   null first 3 of 3 to 0 of 3. Two v1 runs of the same grid agreed on only 74% of the gold-TF-first verdicts, so
   differences of one or two cases are within run-to-run noise.
6. **Flags:** v2 has 5 `unknown_evidence_id` and 2 `failed_citation` (citations to IDs that do not exist; the
   evidence lists are longer), and 18 quotes rejected for not matching their abstract (v1: 12). `coverage_misstated`
   is gone with the field.

## Screen v2 as the model saw it (checkpoints 1 and 2)

### tert_c228t

- **Occupancy element line (E04):** ENCODE TF ChIP-seq at chr5:1295113:G>A: 121 peaks contain the variant, from 54 factors in 21 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. cCRE class at the variant: PLS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, BCL3, DMAP1, EZH2, EZH2phosphoT487, GABPB1, HDAC1, HDAC2, HDAC6, HNRNPK, IKZF1, KDM4A (+21 more). Bound, expressed TFs with a binding model: 20; listed one per row: MAX, JUN, EGR1, BHLHE40, E2F4, E2F6, GABPA, ZNF687, CTCF, N…
- **Screen rows:** GABPA (Ets, 18 models; QBiC-SELEX coverage: own model): z 166.19 / ZIC2 (C2H2 ZF, 4 models; QBiC-SELEX coverage: mapped models only): z -20.85 / CTCF (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): z -14.7 / ZBTB7A (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): z -14.11

### rs4784227

- **Occupancy element line (E04):** ENCODE TF ChIP-seq at chr16:52565276:C>T: 276 peaks contain the variant, from 193 factors in 7 biosamples. In the matching biosample MCF-7: 14 peaks from 9 factors. cCRE class at the variant: dELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, ARID5B, ASH2L, BCL3, CBX5, CHD4, CTBP1, DPF2, EP300, GATAD1, GZF1, HBP1 (+64 more). Bound, expressed TFs with a binding model: 95; listed one per row: FOXA1, GATA3, SPDEF, NR2F2, TCF7L2, SP1, MYBL2, MAX, JUND, RXRA; also bound: YY1, GATAD2A, ZGPAT,…
- **Screen rows:** GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): z 18.65 / FOXA1 (Forkhead, 4 models; QBiC-SELEX coverage: own model): z 15.4 / NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): z 9.51 / TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): z 8.45

### rs11629191

- **Occupancy element line (E04):** No ENCODE TF ChIP-seq peak contains chr14:55887040:C>T in any biosample. In the matching biosample MCF-7: 0 peaks from 0 factors. No cCRE contains the variant. Of the TFs with a binding model, 65 were assayed in the matching biosample and 508 only elsewhere, all without a peak here; 536 were never assayed.
- **Screen rows:** CREB3L2 (bZIP, 4 models; QBiC-SELEX coverage: own model): z -60.99 / CREB3L4 (bZIP, 4 models; QBiC-SELEX coverage: own model): z -49.16 / TET3 (CxxC, 2 models; QBiC-SELEX coverage: own model): z -44.11 / MEIS3 (Homeodomain, 9 models; QBiC-SELEX coverage: own model): z -38.69

### rs73706717

- **Occupancy element line (E04):** ENCODE TF ChIP-seq at chr8:127401265:T>C: 149 peaks contain the variant, from 83 factors in 25 biosamples. In the matching biosample HCT116: 3 peaks from 3 factors. cCRE class at the variant: pELS. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, CHD4, EP300, HDAC1, HDAC2, HMGXB4, KDM1A, KDM6A, LCORL, LIN54, MED1, MED13 (+26 more). Bound, expressed TFs with a binding model: 40; listed one per row: TCF7L2, SP1, CTCF, CEBPB, MYBL2, NR2C2, TFAP4, ISL2, NR2F2, ERF; also bound: NR2F6, NFIC, ELF1,…
- **Screen rows:** TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): z -8.8 / SP1 (C2H2 ZF, 5 models; QBiC-SELEX coverage: own model): z -7.07 / NFIC (SMAD, 4 models; QBiC-SELEX coverage: own model): z 24.28 / NFIA (SMAD, 4 models; QBiC-SELEX coverage: own model): z 24.28

### rs34768248

- **Occupancy element line (E04):** ENCODE TF ChIP-seq at chr5:1295601:G>A: 35 peaks contain the variant, from 27 factors in 9 biosamples. No ENCODE biosample matches the expression context, so no peak counts as bound here. No cCRE contains the variant. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ASH2L, BCL3, DNMT1, DPF2, EZH2, EZH2phosphoT487, GABPB1, IKZF1, KDM4A, MAZ, MTA1, RBBP5 (+5 more). Bound, expressed TFs with a binding model: 10; listed one per row: JUN, CTCF, ZNF687, MAX, CREB1, NR2C2, RXRA, ZBTB33, ZNF800, NKRF. Assa…
- **Screen rows:** NKRF (Unknown, 1 model; QBiC-SELEX coverage: own model): z -12.31 / NR2C2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): z 7.56 / ZNF800 (C2H2 ZF, 1 model; QBiC-SELEX coverage: own model): z 6.43 / CREB1 (bZIP, 2 models; QBiC-SELEX coverage: own model): z 6.24

### rs56007086

- **Occupancy element line (E04):** ENCODE TF ChIP-seq at chr16:52565398:G>A: 215 peaks contain the variant, from 162 factors in 7 biosamples. In the matching biosample MCF-7: 16 peaks from 11 factors. No cCRE contains the variant. Bound factors outside the TF model collection (co-factors, Pol II, and TFs with no binding model; signs of an active element, not TF candidates): ARID4A, ARID5B, ASH2L, BCL3, CBX5, CHD4, CTBP1, EP300, GATAD1, GZF1, HBP1, HDAC1 (+51 more). Bound, expressed TFs with a binding model: 79; listed one per row: FOXA1, GATA3, SPDEF, NR2F2, CEBPB, TCF7L2, MYBL2, SP1, YY1, MAX; also bound: JUND, GATAD2A, BHLHE4…
- **Screen rows:** TCF7L2 (HMG/Sox, 3 models; QBiC-SELEX coverage: mapped models only): z 12.52 / NR2F2 (Nuclear receptor, 29 models; QBiC-SELEX coverage: own model): z 10.89 / GATA3 (GATA, 6 models; QBiC-SELEX coverage: own model): z 8.32 / SPDEF (Ets, 1 model; QBiC-SELEX coverage: own model): z -7.0
