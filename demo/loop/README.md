# The loop's first round on five variants

Public copies of five dry runs of the loop, made on 25 November 2026 (`v2m v9 fill --read --loop code --loop-dry`).
In each, code read the finished table, listed its gaps, planned one round and ran the searches. The section
"Going back for evidence" of each `answer.md` lists every search and what it found.

- **Nothing was read.** A dry run sends no article to a model, so no record was filed and no table changed. It
  shows what a round would read, not what the reading would find.
- **Code planned.** These runs take the menu in code's own order. The planner model has not been run yet.

| Run | Gaps the loop found | What round 1 searched | Articles listed | New to the run |
|---|---|---|---|---|
| [TERT C250T](tert_c250t/answer.md) | 11 chains tie on the TF; no article was on file | each tied TF group with the mutation's names; the names "C250T" and "-146C>T" | 57 | 41 |
| [rs4684847](rs4684847/answer.md) | 4 chains tie on the TF and the gene; nothing joins a TF to a gene | 4 pairs of TF and gene; each tied TF and gene with the variant; what 4 reviews cite | 15 | 3 |
| [rs4784227](rs4784227/answer.md) | 6 chains tie on the TF and the gene; nothing joins a TF to a gene | 4 pairs of TF and gene; each tied TF group and gene with the variant; what 4 reviews cite | 58 | 20 |
| [rs9349379](rs9349379/answer.md) | 3 chains tie on the gene; no TF is named | each tied gene with the variant; what 4 reviews cite | 49 | 20 |
| [rs7001688](rs7001688/answer.md), a random control | 316 chains tie on the TF, on a prediction alone | nothing | 0 | 0 |

- **TERT C250T** is a somatic mutation that papers name by position, so the first search by rsID found nothing.
  The other names come from a catalogue and are verified by position.
- **rs4684847** shows a search that finds nothing: no title or abstract names PRRX1 or ILF3 with PPARG or TIMP4
  and a word for a perturbation. The pairs stay unjoined, and the report says so.
- **rs4784227** shows the joiner's queue: the searches for three of the four pairs list 6 articles that the
  first reading never saw, one of them for two pairs. Their titles are mostly expression screens and association
  studies, so few are likely to hold an experiment that changed the TF.
- **rs9349379** shows where new articles come from for a common variant: 18 of the 20 are cited by a review in a
  paragraph that names the variant.
- **rs7001688** shows the loop leaving a variant alone. Every tied candidate gets the same search or none does,
  and 316 are too many to search one by one. No article names the variant, so there is no review to follow and no
  other name to search under. The round ends with nothing on the menu.

## What a public copy holds

The same four files as in [`demo/tables`](../tables/README.md): `answer.md`, `table.md`, `graph.json.gz` and
`manifest.json`, with every quoted passage bounded to 600 characters and the articles' text removed.
