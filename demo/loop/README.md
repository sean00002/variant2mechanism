# The loop on real variants

Public copies of six loop runs made on 25 November 2026. In each, code read the finished table, listed its gaps and
the searches that could close them, and a round was planned and searched. The section "Going back for evidence" of
each `answer.md` lists every search and what it found.

## Two runs that read what they found

The same variant, rs9349379, run twice from the same first reading and the same code.

| Run | Who planned | Rounds | New articles | Read | Experiments filed | Count for a claim | Chains first |
|---|---|---|---|---|---|---|---|
| [rs9349379](rs9349379/answer.md) | the planner model | 2 | 35 | 4 | 8 | 2 | **1: MEF2 → PHACTR1** |
| [rs9349379, code's order](rs9349379_code_order/answer.md) | code, taking its menu in order | 1 | 20 | 2 | 3 | 0 | 3, no TF named |

- **The difference is two names.** Both runs made the same six searches in round 1: the tied genes with the
  variant, and what four reviews cite. The planner also named MEF2A and EDN1 from memory, and code searched for
  each with the variant.
- **One name found an article.** The search for MEF2A listed four articles the run had not seen. Two were read,
  and one (PMID 25838425) gave the two records that count: a gel-shift assay in which MEF2 binds the A allele and
  not the G allele, and a 34-bp deletion that removes the variant and lowers PHACTR1 expression by 35%.
- **The name left no other trace.** The reader was never told why the article was found, and both records quote
  the article's own sentences.
- **Round 2 changed nothing.** It searched for MEF2 with PHACTR1 and for MEF2 with the variant, and opened four
  more reviews. Nothing new was read, so the loop stopped.
- **A second gene stays in the table.** The chain MEF2 → EDN1 holds edited alleles at the gene step and ranks
  fifth, because no record ties EDN1 to a trait at this locus.

The same two runs were made on seven more variants outside the test set. None of those tables changed
([`docs/report.md`](../../docs/report.md) has every number).

## Four first rounds with nothing read

Dry runs (`v2m v9 fill --read --loop code --loop-dry`): code planned, the searches ran, and no article was sent to
a model. They show what a round would read, not what the reading would find.

| Run | Gaps the loop found | What round 1 searched | Articles listed | New to the run |
|---|---|---|---|---|
| [TERT C250T](tert_c250t/answer.md) | 11 chains tie on the TF; no article was on file | each tied TF group with the mutation's names; the names "C250T" and "-146C>T" | 57 | 41 |
| [rs4684847](rs4684847/answer.md) | 4 chains tie on the TF and the gene; nothing joins a TF to a gene | 4 pairs of TF and gene; each tied TF and gene with the variant; what 4 reviews cite | 15 | 3 |
| [rs4784227](rs4784227/answer.md) | 6 chains tie on the TF and the gene; nothing joins a TF to a gene | 4 pairs of TF and gene; each tied TF group and gene with the variant; what 4 reviews cite | 58 | 20 |
| [rs7001688](rs7001688/answer.md), a random control | 316 chains tie on the TF, on a prediction alone | nothing | 0 | 0 |

- **TERT C250T** is a somatic mutation that papers name by position, so the first search by rsID found nothing.
  The other names come from a catalogue and are verified by position.
- **rs4684847** shows a search that finds nothing: no title or abstract names PRRX1 or ILF3 with PPARG or TIMP4
  and a word for a perturbation. The pairs stay unjoined, and the report says so.
- **rs4784227** shows the joiner's queue: the searches for three of the four pairs list 6 articles that the
  first reading never saw, one of them for two pairs. Their titles are mostly expression screens and association
  studies, so few are likely to hold an experiment that changed the TF.
- **rs7001688** shows the loop leaving a variant alone. Every tied candidate gets the same search or none does,
  and 316 are too many to search one by one. No article names the variant, so there is no review to follow and no
  other name to search under. The round ends with nothing on the menu.

## What a public copy holds

The same four files as in [`demo/tables`](../tables/README.md): `answer.md`, `table.md`, `graph.json.gz` and
`manifest.json`, with every quoted passage bounded to 600 characters and the articles' text removed.
