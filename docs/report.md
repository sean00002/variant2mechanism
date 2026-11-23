# variant2mechanism, version 9: project report

23 November 2026

## Summary

- **What it is for.** To work out how a non-coding variant could lead to a trait, a disease or a cancer. The answer
  is a chain of small claims from the variant to the trait, each backed by data in databases, model predictions and
  experiments read from the literature. A run starts from a variant alone, or from a variant and a trait.
- **What this version is.** A prototype built around one model, QBiC-SELEX, which predicts how a variant changes
  transcription factor (TF) binding. So every chain runs through TF binding and has four fixed steps. Other models,
  other routes and a loop that goes back for missing evidence are planned (see "What comes next").
- **What it does.** For one variant, the pipeline builds that route as eight small claims and shows, for each
  claim, what a database, a model prediction and the literature say.
- **Who does what.** Code fills the table and ranks the chains. Three language-model roles read papers, check
  records and read ties. None of them can add a fact that code cannot find in a source.
- **How it was tested.** The pipeline was frozen and scored once on 15 variants: 9 published mechanisms and 6
  controls.
- **What it found.** The published TF's group is among the leading chains in 7 of 8 cases, usually tied with
  others. Two cases have one leading chain, and both are right. The published TF itself is never named.
- **Where it fails.** It finds only what its sources index. The two somatic promoter mutations in the test set get
  no gene and no trait.

## The question

Given a non-coding variant, what is the route by which it could change a trait, and how good is the evidence for
each step of that route?

The answer is a table, not a paragraph. A chain is one route: a transcription factor (TF), the regulatory element
the variant lies in, a target gene and a trait. Each chain has four steps and each step two claims.

| Step | The alleles differ | The parts are in place |
|---|---|---|
| 1. TF binding | The two alleles differ in binding the TF | The TF is present where it would act |
| 2. Regulatory activity | The two alleles differ in the regulatory activity of the site | The variant lies in a regulatory element |
| 3. Target gene | The two alleles differ in the gene's RNA | The element regulates the gene |
| 4. Trait | The two alleles differ in the trait | The gene bears on the trait |

Each claim has three cells, one per kind of record: a database record, a model prediction, and an experiment read
from an article. A cell says "supports", "disagrees", "nothing found", "not checked" or "no source". The full
definition is in [`chain-table.md`](chain-table.md).

## Design rules

1. **A fixed table.** Every chain has the same eight claims and every claim the same three cells. A checker tests a
   table against the rules without knowing the right answer, so the same check works for a variant nobody has
   studied.
2. **Two kinds of claim.** The left column is about this variant's two alleles. Only a record that compares them can
   support it. A knock-down of the TF, a deletion of the element, a perturbation of the gene or a result at a
   neighbouring variant can support only the right column.
3. **A model's memory is never evidence.** Version 8 showed why. Asked with no tools and no evidence, the model
   named the published TF at all nine test cases. A correct name therefore shows recall. In version 9 a model may
   read an article and point to sentences, and code decides what the sentences are evidence for.
4. **Kinds of evidence, not amounts.** A claim is as strong as the strongest kind of record under it: an edit, an
   assay that compares the alleles, an association, a prediction, or nothing. Effect sizes, read counts, expression
   levels and the number of records do not enter the order. A TF that was never assayed is not a TF that is absent,
   so a missing record removes nothing.
5. **No model can add a fact.** Each model role has a narrow job with a limit that code enforces.

## The pipeline

![The pipeline](pipeline.svg)

| Stage | Who | What it is given | What it returns |
|---|---|---|---|
| Fill | code | The variant | Every claim a database record or a QBiC-SELEX prediction can count for, with its records |
| Find and choose articles | code | The variant's rsIDs | Up to 20 articles that name the variant; reviews are left out |
| Read | first model | One article and the variant, and nothing about what the run hopes to find | The experiments the article reports, each pointing to at most four sentences |
| File and link | code | The model's pointers | A record for each experiment whose sentences and fields check out, linked to the claims it bears on |
| Check | second model | A record that a cell depends on alone, its paragraph, and the claims it counts for | For each claim: shown, not shown or cannot tell |
| Order | code | The table | Chains ranked by their weakest link, with ties |
| Read a tie | second model | The experiments that no cell counts, for the tied TFs and genes | For each: tied to the site, not tied or cannot tell |

**The reader points and code quotes.** Each passage is shown with numbered sentences. The model names a run of
sentences and code copies it, so a quotation is the article's own text by construction. A reply that breaks a limit
is sent back once. What still breaks it is refused.

**The critic reads only what can change a cell.** Taking the one record out of a cell changes the cell. Taking out
one of several changes nothing. So only records that stand alone are sent. The critic sees the article's text and
the claim, and nothing of the reader's reading.

**The judge reads what no cell may count.** Some experiments test no single claim. A TF is removed and the
difference between the alleles goes away: that names a TF, yet it does not compare the alleles' binding. The judge
reads such experiments for the chains tied for first, and its answer is written under the tie. It changes no cell
and no rank.

**Chains.** A chain takes one TF candidate and one gene candidate, and there is a chain for every pair. TFs that
share a QBiC-SELEX model are one candidate. Chains are compared weakest link first, then the next weakest. Two
yes-or-no facts break ties: a strong QBiC-SELEX prediction with a ChIP-seq peak over the variant, and records that
show the TF in place. A chain never ranks above one that is at least as strong on every link.

**Models and cost.** The reader runs on GPT-6 Luna and the critic and judge on Claude Sonnet 5.5, a model from
another provider. The 15 test variants took 126 model calls: 98 by the reader, 20 by the critic and 8 by the judge.
At list prices that is about 43 cents, or 3 cents a variant.

## Testing the roles without an answer key

The 15 test variants have published answers, and the pipeline's rules were not to be tuned to them. So each role was
tested with controls that need no answer key.

**The reader.** Code's checks are the test. On the 15 variants the searches found 134 articles. The model read 87 of
them and returned 262 experiments. Code filed 166 as records and linked 60 of them to a claim of a table. The rest
are on file and count for nothing. An audit of one earlier run found 5 wrong among 44 counted records. The reader's
rules were tightened after it, and the 44 became the critic's test.

**The critic.**

| Check | What was read | What the critic did |
|---|---|---|
| Decoys, on variants outside the test set | 34 real claims and 25 claims whose TF or gene the paragraph never names | Rejected all 25 decoys and kept all 34 real claims. For 6 it pointed to further sentences that state the result |
| The audited records | 44 counted records, 5 of them wrong | Took out 4 of the 5 and none of the other 39. It kept the fifth and quoted the later sentences that do support it |
| The 15 test variants | 60 counted records, 20 of them alone behind a claim | Read the 20: 29 of 30 claims shown, one "cannot tell", none taken out. No cell changed |

With today's reader the critic changes nothing in the 15 tables. Its value there is a second reading on file beside
each record that carries a cell alone. On records from the earlier reader it removes the known errors.

**The judge.**

| Set | Ties for first | With experiments to read | Points to | Made-up candidate turned down |
|---|---|---|---|---|
| 8 variants outside the test set | 4 | 3 | PRRX1 at rs4684847, KITLG at rs12821256 | 6 of 6 readings |
| The 15 test variants, run once | 10 | 4 | the C/EBP group at rs12740374 | 8 of 8 readings |

Every question to the judge carries one made-up candidate, a TF or gene that no paragraph names, and is asked twice
with the candidates in opposite orders. An answer is kept only when both readings give it. A reading that accepts
the made-up candidate invalidates the whole tie.

Development found four faults, and each changed the protocol before it was frozen:

- **It trusted code's list.** The judge accepted a renamed candidate while noting that the article names another
  factor. It is now told to find the candidate in the paragraph itself.
- **It favoured the first candidate.** The candidate listed first was twice given an answer its records did not
  bear out. That is why each question is asked in both orders, and why the made-up candidate exists: it gives a tie
  with one candidate a second position to be read in.
- **Its answer contradicted its reason.** The reply now gives the reason before the answer.
- **One bad pointer lost a whole reading.** A pointer that code cannot copy now costs only the pointer.

## The frozen test

**The freeze.** `eval/fill_freeze_20261123.json` holds the hash of every file a run executes (151 files) and of the
15 tables. `scripts/v9_freeze.py check` lists anything that has changed since, and the scorer refuses to run if
something has.

**The rule, written before any table was scored.** A case's answer is the set of chains tied for first. Names are
matched by the answer key's own rules. "Named" counts a case when a first-ranked chain names the published answer.
"By share" is the matching candidates over the candidates in the tie, summed over cases: what picking one candidate
from each tie at random would get. Both are given again with the judge's answers applied. Direction and context are
not scored, and controls get no score. The rule is the docstring of `scripts/v9_table_score.py`.

| Component | Cases it applies to | Named | By share | By share, with the judge |
|---|---|---|---|---|
| TF, as the member | 9 | 0 | 0.00 | 0.00 |
| TF, as its group | 8 | 7 | 3.95 | 4.86 |
| TF, as its family | 8 | 7 | 4.28 | 4.86 |
| Target gene | 9 | 6 | 4.58 | 4.58 |
| TF group and gene in one chain | 9 | 4 | 2.25 | 3.17 |
| Trait | 9 | 7 | 7.00 | 7.00 |

Two of the nine cases, rs12740374 and TERT C228T, were used while an earlier version was built. Without them the
judge changes no number:

| Component | Cases it applies to | Named | By share |
|---|---|---|---|
| TF, as the member | 7 | 0 | 0.00 |
| TF, as its group | 6 | 5 | 3.36 |
| TF, as its family | 6 | 5 | 3.36 |
| Target gene | 7 | 5 | 3.58 |
| TF group and gene in one chain | 7 | 3 | 2.17 |
| Trait | 7 | 6 | 6.00 |

Case by case ("4 of 8": four of the eight tied candidates match):

| Case | Chains tied for first | TF, as its group | Target gene | Both in one chain | Trait |
|---|---|---|---|---|---|
| TERT C228T | 8 | 4 of 8 | 0 of 1 | 0 of 8 | no |
| TERT C250T | 11 | 4 of 11 | 0 of 1 | 0 of 11 | no |
| rs6983267 | 2 | 1 of 2 | 0 of 1 | 0 of 2 | yes |
| rs4784227 | 6 | 1 of 2 | 1 of 3 | 1 of 6 | yes |
| rs339331 | 1 | 1 of 1 | 1 of 1 | 1 of 1 | yes |
| rs2168101 | 1 | 1 of 1 | 1 of 1 | 1 of 1 | yes |
| rs12740374 | 12 | 1 of 12; with the judge 1 of 1 | 1 of 1 | 1 of 12; with the judge 1 of 1 | yes |
| rs1421085 | 12 | does not apply | 1 of 1 | 0 of 12 | yes |
| rs642961 | 4 | 0 of 1 | 1 of 4 | 0 of 4 | yes |

What the numbers say:

- **Two clean answers.** rs339331 and rs2168101 have one leading chain each, and it names the published TF group,
  gene and trait. Both have an article with experiments on the two alleles that is indexed under the rsID.
- **Right group, rarely alone.** The published TF's group is in the leading tie in 7 of 8 cases: 3.95 of 8 by share.
- **Never the single TF.** TFs that share a model are one candidate, and an experiment that names one member is
  filed under the group.
- **The judge's gain is one case.** It adds 0.92 to two rows, all at rs12740374. On the seven other cases it read
  three ties, pointed to nothing and changed nothing.
- **The trait number is generous.** A chain lists every trait a source ties to the variant, and one match counts.

### Controls

These counts need no answer key.

| Set | Cases | Claims of the first chain with support, mean of 8 | Cases whose first chain has a measured claim that the alleles differ |
|---|---|---|---|
| Published mechanisms | 9 | 5.9 | 7 |
| Near-miss controls | 3 | 4.7 | 1 |
| Random controls | 3 | 1.7 | 0 |

A measured claim rests on an assay or an edit, not only on an association or a prediction. It separates the sets
better than the count of supported claims does. The two published cases without one are the TERT cases. The one
control with one is rs56007086, which lies in the same element as rs4784227: a database records ChIP-seq reads of
ESR1 that favour one allele there. That is a measurement, not an error, and the chain stops at it.

## Why each miss happened

Each cause was read from the saved tables after the scoring.

- **TERT promoter, both cases.** The literature search uses the rsID alone. The papers on these mutations name them
  by position, so the search found four articles for one case, none with a usable experiment, and no article for the
  other. No database the fill reads holds a somatic mutation. No chain names a gene or a trait, and the first chain
  has 3 of 8 claims with support, as a control has.
- **MYC at rs6983267.** No record of any kind says the alleles differ in MYC. One article reports that CCAT2, a
  transcript that contains the variant, is expressed more from one allele, so the leading chains name CCAT2. The
  first chain that names MYC is at rank 1,045.
- **AP-2α at rs642961.** The reader filed the article's binding experiment under the name the article uses for the
  protein. Nothing maps that name to the gene symbol TFAP2A. So the experiment and the QBiC-SELEX prediction for
  that TF's group sit on two candidates, the group is at rank 6, and the rule counts a miss at every TF level.
- **ARID5B at rs1421085.** No QBiC-SELEX model covers it and no filed record names it.

## Against the earlier versions

**Version 8** had code gather evidence and screen TF families, a generator model write chains and a critic model
grade them. Its evaluation is the reason for version 9's rules.

| Arm of version 8 | Published TF named first | Controls with "no mechanism" |
|---|---|---|
| Agent, 3 repeats | 6 of 27 runs | 18 of 18 |
| Code only, no model | 2 of 9 | 6 of 6 |
| Model alone, no tools or evidence | 9 of 9 | not run |

The agent did no better than code, and the model alone did best, because the cases are well known.

**The first version 9 engine** let model roles propose hypotheses, ask for evidence and compare. It was frozen and
run once on the same 15 variants on 14 November. Its own evaluator scored the hypotheses each run stood behind: TF
group 2 of 8, target gene 6 of 9, trait 0 of 9. Three published cases ended with no supported explanation. A hand
count of its first-ranked chains, with ties counted and never scripted, gave the TF or its group in 7 of 9, the gene
in 8 of 9 and both in 6 of 9.

**The table-filling pipeline**, scored above, gives 7 of 9, 6 of 9 and 4 of 9 by "named". It names no more published
answers than the engine's chains did, and two genes fewer. The engine let a model propose TERT from memory, and this
pipeline names only what a source names. What it adds is the evidence under each claim, which the answer key does
not measure.

## What this does not show

- **It is not a blind test.** The published answers were known while the pipeline was designed. TERT C250T, which
  counts among the seven, has the same promoter, TF and gene as TERT C228T. The reader's last rules came from an
  audit of its records on these variants.
- **The answer key is unreviewed.** Every number is provisional until it is reviewed.
- **Nine cases.** One case is 11 points. No statistical claim is made.
- **The order of evidence is a choice.** Edit, assay, association and prediction are ranked by kind. The order was
  fixed by argument and is not calibrated against variants of known effect.
- **A chain is not a demonstrated path.** Each link is a separate claim. A chain pairs every TF with every gene, and
  no claim says that this TF regulates this gene.
- **From here the 15 are development data** for anything changed because of these results. A new test needs variants
  that nobody here has looked at.

## What comes next

- **More models.** Predictions of regulatory activity and expression from AlphaGenome and ChromBPNet-style models,
  beside QBiC-SELEX for TF binding. Two of the four steps have no model prediction today.
- **More routes.** Chains whose steps are not fixed in advance, so that a mechanism need not run through TF binding.
- **Going back for evidence.** When a chain has a gap, look for what would fill it, then build the chains again.
  Today code looks everything up once.
- **A test on other variants.** Variants outside the 15, chosen before any run.
- **Find papers under a mutation's other names**, not only its rsID.
- **Let a promoter variant name its gene**, as a claim with the annotation behind it.
- **Map protein names to gene symbols** when an experiment is filed.
- **A role that proposes.** A model may propose a TF or a gene from memory for code to look up. The proposal is a
  candidate and never evidence.
- **The statistical module as a source.** Fine-mapping and colocalisation computed from summary statistics
  ([`statgen.md`](statgen.md)) are not yet read by the table.
- **A claim that the TF regulates the gene**, so that a chain's steps are tied to one another.

## Reproducing it

The 15 scored runs are saved as public copies in [`demo/tables/`](../demo/tables/). The tables built from those
copies are identical to the originals, and the score is the same.

```bash
uv sync
# rebuild the 15 tables and their summary: no key, no network
uv run python scripts/v9_chain_table.py --runs demo/tables --out /tmp/v2m_tables
# recompute the score: needs the two reference tables named in the README
uv run python scripts/v9_table_score.py --runs demo/tables --out /tmp/v2m_score
```

| What | Where |
|---|---|
| The scores, case by case | [`eval/fill_score_20261123.md`](../eval/fill_score_20261123.md) |
| The tables' counts, the reader's, the critic's and the judge's | [`eval/fill_tables_20261122.md`](../eval/fill_tables_20261122.md) |
| The freeze | `eval/fill_freeze_20261123.json`, `scripts/v9_freeze.py` |
| The answer key and its matching rules | `eval/v9_gold_spec.json` |
| The checks of the critic and the judge | `scripts/v9_critic_check.py`, `scripts/v9_judge_check.py` |

Running a new variant needs the two model keys, the local data folder and a QBiC-SELEX run for the variant. The
response caches that let a saved run replay offline are not in the repository.
