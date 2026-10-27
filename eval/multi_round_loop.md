# The multi-round loop (v4)

What changed, how it was tested, what the demo runs did, and what GPT-6 Luna's masked `full` grid shows when it gets
up to three rounds instead of one (v4), then with the not-assayed fix (v5, section 7), and with ReMap (v6, section 8). Seed 0; counts, not
percentages. Tables from `scripts/loop_value.py`.

## 1. What changed

**Before (v1 to v3): one round.** The critic suggested up to 3 checks; the generator made up to 3 tool calls in a
native tool-calling loop; it revised once; the critic regraded once, and those grades were final.

**Now (v4): up to three rounds of plan, act, revise and regrade** (`agent/stages/investigate.py`).

- **Plan:** the generator returns its calls as data (`Plan`): for each, the tool, its arguments, the link it should
  resolve, and the result it expects with what that result would change. It sees every earlier call and the evidence
  ID it produced.
- **Act:** code checks each call against the tool's schema, refuses a repeat of any earlier call (same tool, same
  arguments), allows 3 per round, and runs the rest, writing each result to the ledger first.
- **Revise:** the revision (`RevisedRound`) adds, for each call, what it found and whether that matched the
  expectation (yes, no or unclear).
- **Regrade:** the critic returns grades, problems and checks, like the first critique, so its checks can steer the
  next round.
- **Stop:** when the planner has no new call to run (it may say why), when a round moves no link grade and no
  probability by 0.05 or more, or after 3 rounds. (v5 replaced the 0.05 rule; section 7.)
- **Report:** `report.json` gains `rounds` and `stop_reason`; `report.md` gains a "Refinement rounds" section.
- **Settings:** `investigate.max_rounds`, `max_tool_calls` (per round) and, in v4 only, `stable_delta` in
  `config.yaml`. v4 runs went to `runs/*_v4_*`; every earlier folder is kept.

Tests (offline, fake model): calls carried between rounds and repeats refused, the stop when a round changes nothing,
and the round limit. 148 passed.

## 2. The demo runs

| Run | Draft | After round 1 | Final | What happened |
|---|---|---|---|---|
| rs339331, Luna, named | null 0.50, AR 0.38, HOXC13 0.08 | HOXB13 0.70, null 0.17 | HOXB13 0.78, null 0.17 | The critic questions HOXC13 (its QBiC-SELEX change comes from a HOXB13 model). The planner checks HOXB13 itself, predicting that T binds more: own model, first of 997. H2.binding goes from weak to supported. Rounds 2 and 3 look for HOXB13 ChIP-seq in LNCaP and VCaP; ENCODE has none. |
| rs73706717, DeepSeek, masked | TCF7L2 0.43, null 0.35 | null 0.56, TCF7L2 0.18 | null 0.66, TCF7L2 0.17 | A near-miss control in the rs6983267 enhancer. The planner predicts a null colon eQTL, no NFIC peak in HCT116, and only a mapped, weak-site TCF7L2 model; all three come back as predicted. |
| rs339331, DeepSeek, named | AR 0.40, HOXB13 0.28, null 0.24 | HOXB13 0.38, AR 0.29 | null 0.43, HOXB13 0.42 | The same HOXB13 result in round 1, but later rounds find no HOXB13 ChIP-seq peak in any cell type, and the null edges ahead. |

The first two are in the [run viewer](https://htmlpreview.github.io/?https://github.com/sean00002/variant2mechanism/blob/main/demo/run_viewer.html) and in `demo/runs/`.

## 3. Luna, masked `full`: one round against up to three

The same 15 cases, model, mode and screen (v3); only the loop differs.

| masked `full`, 15 cases (9 TF cases) | one round | up to three rounds |
|---|---|---|
| TF cases: gold TF ranked first | 1 | 1 |
| TF cases: gold TF in the top three | 6 | 6 |
| TF cases: null ranked first | 7 | 8 |
| TF cases: mean p(gold TF) | 0.17 | 0.13 |
| Random controls: mean p(null) | 0.92 | 0.96 |
| Near-miss controls: mean p(null) | 0.74 | 0.72 |
| Cost, total | $0.18 | $0.37 |
| Model calls per run (mean) | 7.1 | 13.1 |
| Seconds per run (mean) | 133 | 264 |

Each round against the one before (top answer right: the gold TF at a TF case, the null at a control):

| Kind · round | right both | fixed | broken | wrong both |
|---|---|---|---|---|
| TF case · round 1 | 0 | 2 | 1 | 6 |
| TF case · round 2 | 0 | 0 | 2 | 7 |
| TF case · round 3 | 0 | 1 | 0 | 8 |
| control · round 1 | 5 | 1 | 0 | 0 |
| control · round 2 | 6 | 0 | 0 | 0 |
| control · round 3 | 5 | 0 | 0 | 0 |

The top answer of each case, draft and rounds 1 to 3 (the gold TF's probability in brackets; * marks a right
answer):

| Case | Draft | Round 1 | Round 2 | Round 3 |
|---|---|---|---|---|
| tert_c228t | null 0.70 [0.19] | null 0.83 [0.06] | null 0.86 [0.06] | null 0.90 [0.04] |
| tert_c250t | null 0.34 [0.32] | null 0.56 [0.19] | null 0.75 [0.08] | null 0.84 [0.04] |
| rs6983267 | *TCF7L2 0.60 | null 0.48 [0.40] | null 0.62 [0.28] | null 0.65 [0.23] |
| rs4784227 | GATA3 0.32 [0.30] | null 0.55 [0.16] | null 0.32 [0.25] | *FOXA1 0.40 |
| rs339331 | null 0.55 [0] | null 0.76 [0] | null 0.85 [0] | null 0.62 [0] |
| rs2168101 | null 0.38 [0.16] | *GATA3 0.32 | null 0.29 [0.25] | null 0.45 [0.20] |
| rs12740374 | null 0.32 [0.30] | *CEBPA 0.29 | CEBPG 0.27 [0.24] | null 0.38 [0.25] |
| rs1421085 | null 0.52 [0] | null 0.71 [0] | null 0.68 [0] | null 0.72 [0] |
| rs642961 | null 0.75 [0] | null 0.82 [0] | null 0.94 [0] | null 0.94 [0] |
| rs13078086 | *null 0.82 | *null 0.94 | *null 0.98 | *null 0.97 |
| rs11629191 | *null 0.90 | *null 0.94 | *null 0.96 | stopped |
| rs7001688 | *null 0.65 | *null 0.87 | *null 0.94 | *null 0.95 |
| rs73706717 | *null 0.60 | *null 0.55 | *null 0.70 | *null 0.78 |
| rs34768248 | *null 0.62 | *null 0.82 | *null 0.83 | *null 0.82 |
| rs56007086 | TCF7L2 0.30 | *null 0.45 | *null 0.58 | *null 0.57 |

Across the 15 runs: 14 used all three rounds and one stopped after two (nothing new to run). All 110 planned calls ran;
the planner never tried a repeat. The revisions judged 100 results as expected and 10 as unclear, none as not
expected.

## 4. What this shows

1. **Three rounds did not beat one on this set, at twice the cost.** The gold TF is in the top three in 6 cases
   either way.
2. **Iterating a sceptical critic compounds its scepticism.** Each round looks again for a ChIP-seq peak in the
   matching cell type, mostly finds none because ENCODE never assayed that TF there, and moves probability to the
   null. That helps at the controls (p(null) rises at every one, and the near-miss rs56007086 is withdrawn in
   round 1) and hurts true cases: GABPA at the TERT promoter falls from 0.32 to 0.04, and TCF7L2 at rs6983267 from
   0.60 to 0.23. Round 1 put CEBPA and GATA3 on top; round 2 lost both.
3. **The loop never turned a correct null at a control into a claim,** here or in the 187 one-round runs.
4. **The agent's own verdicts are a weak check.** It writes each expectation as a two-sided conditional ("if X, H1
   rises; if not, H1 falls"), so almost any result counts as expected.
5. **The stopping rule is too loose.** A round almost always moves some probability by 0.05, so 14 of 15 runs ran to
   the limit.

## 5. What to change next

- **Treat "not assayed here" as missing, not negative.** Done in v5 (section 7).
- **Stop on the answer, not on any probability.** Done in v5 (section 7).
- **Make expectations falsifiable (not done):** ask for one predicted result per call, scored by code where it can be
  (a z above the gate, a peak present), not a conditional the model grades itself.

## 6. Cost

- Luna masked `full` grid with the new loop (v4): $0.37.
- Demo runs (v4): Luna rs339331 $0.03; DeepSeek rs339331 $0.07 and rs73706717 $0.07 (DeepSeek dev budget now $0.27
  of $0.50).
- Luna masked `full` grid with the not-assayed fix (v5): $0.22. Luna's budget now stands at $1.41 of $2 (eval $1.35
  of $1.80, dev $0.06 of $0.20).

## 7. The not-assayed fix (v5)

**What changed:**

- **The ChIP-seq tool answers one of three,** from ENCODE's released-experiment list (the cached search the
  occupancy step already makes): a peak contains the variant; ENCODE assayed the TF in that biosample and found no
  peak (evidence against occupancy there); or ENCODE has no such experiment (no information).
- **The critic's rubric and the revise prompt** say that a missing experiment never lowers a grade or a chain.
- **In the loop,** a "no experiment" answer does not use up one of the round's calls, and a round whose calls bring no
  new information ends refinement.
- **The stopping rule** is now: stop when a round leaves the top chain and the grades of its links as they were. It
  replaces "no probability moved by 0.05".

The demo runs in section 2 and in the viewer were made before this fix.

**The three loops on the same 15 masked cases (Luna, screen v3):**

| masked `full`, 15 cases (9 TF cases) | one round (v3) | up to three (v4) | up to three, with the fix (v5) |
|---|---|---|---|
| TF cases: gold TF ranked first | 1 | 1 | 0 |
| TF cases: gold TF in the top three | 6 | 6 | 7 |
| TF cases: null ranked first | 7 | 8 | 8 |
| TF cases: mean p(gold TF) | 0.17 | 0.13 | 0.18 |
| Random controls: mean p(null) | 0.92 | 0.96 | 0.89 |
| Near-miss controls: mean p(null) | 0.74 | 0.72 | 0.61 |
| Cost, total | $0.18 | $0.37 | $0.22 |
| Model calls per run (mean) | 7.1 | 13.1 | 7.7 |
| Seconds per run (mean) | 133 | 264 | 149 |

With the fix, 11 of 15 runs stopped after round 1 (10 because the answer held, 1 because its calls brought nothing
new), 1 after round 2, and 3 ran all three rounds. Six ChIP-seq calls were answered "no experiment"; none lowered a
chain.

**The final top answer of each case (gold TF's probability in brackets; for a control, p(null)):**

| Case | One round (v3) | Up to three (v4) | With the fix (v5) | Rounds (v5) |
|---|---|---|---|---|
| tert_c228t | null 0.78 [0.07] | null 0.90 [0.04] | null 0.78 [0.10] | 1 |
| tert_c250t | null 0.61 [0.17] | null 0.84 [0.04] | null 0.46 [0.34] | 1 |
| rs6983267 | TCF7L2 0.46 | null 0.65 [0.23] | null 0.64 [0.12] | 3 |
| rs4784227 | GATA3 0.30 [0.28] | FOXA1 0.40 | null 0.40 [0.24] | 2 |
| rs339331 | null 0.72 [0] | null 0.62 [0] | null 0.72 [0.18] | 1 |
| rs2168101 | null 0.31 [0.27] | null 0.45 [0.20] | GATA2 0.36 [0.36] | 3 |
| rs12740374 | null 0.35 [0.27] | null 0.38 [0.25] | null 0.36 [0.27] | 1 |
| rs1421085 | null 0.68 [0] | null 0.72 [0] | null 0.52 [0] | 1 |
| rs642961 | null 0.82 [0] | null 0.94 [0] | null 0.84 [0] | 1 |
| rs13078086 | null 0.94 | null 0.97 | null 0.96 | 1 |
| rs11629191 | null 0.95 | null 0.96 | null 0.92 | 1 |
| rs7001688 | null 0.88 | null 0.95 | null 0.80 | 1 |
| rs73706717 | null 0.78 | null 0.78 | null 0.66 | 1 |
| rs34768248 | null 0.79 | null 0.82 | null 0.77 | 1 |
| rs56007086 | null 0.65 | null 0.57 | SPDEF 0.43 [null 0.40] | 3 |

**What the fix did:**

1. **It stopped the erosion it was aimed at.** GABPA at TERT C250T stays at 0.34 (0.04 with three rounds and no fix,
   0.17 with one round).
2. **It made the loop cheap.** Most runs stop after one round, so it costs $0.22 against $0.37, close to the one-round
   $0.18.
3. **It did not raise the scores.** On one seed and 15 cases, the three loops are within a case of each other on every
   count.

**What it did not fix:**

- **The same mistake through another tool.** At rs6983267, with the rsID hidden, two literature searches by position
  in round 2 return no hits, and the revision moves TCF7L2 from 0.42 to 0.13. A search that finds nothing is no more
  evidence against a mechanism than a missing ChIP-seq experiment. The next step is the same rule for the literature
  tool: zero hits is missing, not negative.
- **A real candidate at a near-miss control.** At rs56007086, SPDEF has a ChIP-seq peak in MCF-7 and a strong-site
  change in its own QBiC-SELEX model, so the rubric grades its binding as supported, and Luna ranks it first (0.43
  against the null's 0.40). Without the extra rounds' scepticism, nothing pushes it down. The gold set lists the
  near-miss controls as having no known effect, which is not proof that SPDEF does nothing there.

## 8. ReMap in the ChIP-seq tool (v6)

**What changed:** `chip_peaks` also reports ReMap 2022 (published ChIP-seq from GEO and ENCODE, reprocessed),
through the UCSC Genome Browser API (hg38 track `ReMapTFs`): one cached request per variant, filtered by TF and
biosample, with dataset accessions and the distance to the nearest peak summit. A ReMap peak in a matching biosample
counts as occupancy even where ENCODE has no experiment; no ReMap peak stays no information, since ReMap lists peaks,
not experiments. The screen stays ENCODE-only.

**On recorded data** it fills the gap that mattered: HOXB13 over rs339331 in LNCaP becomes a peak (33 HOXB13
datasets over the variant, among them 4 in LNCaP and about 28 prostate tissue and tumour samples; nearest summit 11 bp).
GABPA at the TERT promoter stays "no experiment": no published GABPA ChIP-seq in glioblastoma is in ReMap.

**Luna, masked `full`:** the same as v5 within noise (random controls 0.89, near-miss controls 0.58, gold TF in the
top three 7 of 9). Most model calls replayed from the cache ($0.02), because the evidence did not change: the agent
asked ChIP-seq about 6 TF and cell-type pairs (JUN and ATF3 in adipose; CREB1, NKRF and JUN in glioblastoma; NFIC in
HCT116), and ReMap had a peak in the matching cell type for none of them.

**rs339331, named (Luna):** HOXB13 leads from round 1 (0.52) and ends at 0.68 (0.78 in the v4 demo run). Its
binding link reaches "supported" in round 2, through a literature report of greater HOXB13 binding on the T allele
and HOXB13's own QBiC-SELEX model. The agent asked ChIP-seq only about AR (ReMap: 125 AR peaks over the variant in
LNCaP, VCaP, 22Rv1 and prostate tissue), never about HOXB13.

**What this shows:** a better source helps only when the agent asks it the right question. ReMap's HOXB13 data would
matter most in the screen, which drops HOXB13 at rs339331 because ENCODE assayed it only in A549. Adding ReMap to the
screen's occupancy classes, for TFs QBiC-SELEX covers, would list HOXB13 first there. Not done: it changes the screen
for every case, and needs care at enhancers that hundreds of factors bind in ReMap (713 at rs6983267).

**Cost:** the v6 grid $0.02, the rs339331 run $0.03. Luna's budget now stands at $1.46 of $2.

