# Limitations of v8

What the v8 numbers do and do not show, measured on the saved GPT-6 Luna grid (`runs/eval_v8_luna`, 198 runs; see
`eval/v8_results.md` and `eval/v8_cases.md`). Each item says what it means for a reader of the results.

## What the evaluation can show

- **The development set is famous.** With no tools and no evidence, from the position and the disease alone, the
  model names the gold TF first at all 9 TF cases (`single` arm, 9/9). The 15 cases come from well-known papers, so
  they show whether the workflow runs and is honest, not whether it finds mechanisms the model does not already know.
  Cases published after the model's training data are needed for that. Claude Opus 5.5 also names 9/9 from memory,
  and writes the masked rsID itself at all 7 TF cases that have one (`eval/v8_opus55.md`): masking the rsID does not
  hide a famous variant.
- **The agent ties code.** In the main arm the agent names the gold TF first in 6 of 27 TF-case runs (2 of 9 cases,
  TCF7L2 and HOXB13, in all three repeats). The code-only baseline, with no model call, also gets 2 of 9.
- **The model barely decides.** It never names a member other than code's (0 of 225 main-arm chains), and its top TF
  differs from code's in 19 of 90 runs across four arms. Its link grades are reported but never used to rank.
- **A stronger model changes nothing.** Claude Opus 5, through the Anthropic API, gives Luna's overall verdict at 15/15
  main-arm cases and names the gold TF first at the same 2/9, at 75 times the cost (`eval/v8_opus5.md`). It did
  override code's member in 3 of 75 chains; at rs12740374 that brought in CEBPA, the gold TF, which code then ranked
  last because its ChIP-seq peak has no summit within 50 bp of the variant.
- **Fifteen cases are few.** No paired comparison reaches significance (the smallest sign-test p is 0.5). A
  difference of one case is noise.
- **Repeats are not seeds.** A repeat only changes the model's cache key; no sampling seed is sent. Three repeats show
  how stable the answers are at the provider's default sampling, nothing more.

## Where v8 goes wrong

- **Member choice.** Of the 7 TF cases missed in repeat 0, 4 have the gold family among the chains but the wrong
  member (for example GATA2 for GATA3 at rs2168101, TFAP2C for TFAP2A at rs642961). The member rule prefers the member
  with ChIP-seq at the variant, and ChIP-seq exists for some paralogs and not others.
- **Occupancy first.** Families are ordered by ChIP-seq grade before effect size. This finds TCF7L2 at rs6983267 but
  loses the ETS family at the TERT promoter (|z| 166, no ETS1 summit in the context) to E2F1.
- **Controls pass on the disease line only.** At all three near-miss controls the TF line says "mechanism" in every
  repeat (9 of 18 control runs). The overall verdict is "no mechanism" only because the disease line finds no
  association. A variant with a real association but no TF mechanism would not be caught.
- **Coverage.** QBiC-SELEX has no model for ARID5B (rs1421085), so that case cannot be answered from binding.
  QBiC-SELEX predicts in vitro binding of single TFs; cofactors, chromatin and cooperative binding are not modelled.
- **Expression filters.** A TF called unexpressed in bulk data of the context gets a contradicted cell-type link. A TF
  expressed in a rare cell type of a tissue can be diluted out.
- **Site strength.** The element tier lets a chain that creates a strong site count as indirect support
  (`v8/tiers.py`, `creates_site`), although site strength was meant to be shown, never used.

## Evidence and tools

- **The literature cut-off leaves nothing.** Masked runs keep only papers published before the case's source paper.
  PubTator3 then returns no papers for any of the 9 TF cases; named runs get 1 to 16. The masked arms therefore run
  without literature.
- **Association evidence reaches the model.** The disease is in every prompt, and the GWAS and Open Targets rows are
  in the evidence the model reads. The model could pick a mechanism because the variant is associated with the
  disease, not because of the mechanism evidence. VEP's raw output also carries ClinVar's significance; the summary
  the model sees leaves it out.
- **SCREEN's API is closed** to the public. Element activity comes from SCREEN's downloads; the cCRE at the variant
  comes from the local ENCODE registry, which still answers when the API fails.
- **New variants need QBiC-SELEX statistics.** The 15 gold-set variants are cached in `cache/qbic.sqlite`. Another
  variant needs a QBiC-SELEX run with the covariances (133 GB) and hg38, locally or on a Slurm cluster.
- **Replays need the local caches.** `v2m replay` re-executes a saved run from `cache/http`, `cache/llm`,
  `cache/screen` and `data/`, which are not in the repository. From a fresh checkout, `--render-only` re-renders the
  saved reports.

## Fixed in M1 (3 November 2026)

- A failed literature search no longer falls back to Europe PMC without the cut-off.
- A failed cCRE lookup is no longer read as "not in a cCRE"; one failed association source gives "unknown", not "no
  association".
- A cited evidence ID that is not in the ledger is refused, with one retry.
- The reason for a family swap is kept, and rejected eliminations say why they were rejected.
- The results tables give every denominator, report TF cases and controls apart, and show the TF line's over-claims.
- A single `v2m v8 run` writes to the dev folder and never displaces a saved evaluation run.

One saved run no longer replays exactly because of these fixes: `full_given/2/rs1421085` (its critique prompt now
carries the swap reason). `full_given/1/rs13078086` replays with the corrected rejection label.
