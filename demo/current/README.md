# The 15 test variants, filed again under the current code

Public copies of the same 15 variants as [`demo/tables`](../tables/), built on 25 November 2026 with what was
added after the scoring: five more sources, an article's own name for a mutation, and the record that joins a TF to
a gene ([`docs/report.md`](../../docs/report.md)).

- **No model was called for these.** Each run files the readings saved from the scored runs again, with the new
  sources asked afresh. The critic and the judge are not part of them.
- **They are not a test.** The 15 variants were used while these parts were built. The table shows what changed,
  and it is not a score.

| Run | Kind | Chains tied for first, before and now | Claims of the first chain with support, of 8 | What changed |
|---|---|---|---|---|
| [rs339331](rs339331/answer.md) | published mechanism | 1, 1 | 7, 7 | nothing |
| [rs2168101](rs2168101/answer.md) | published mechanism | 1, 1 | 7, 7 | nothing |
| [rs6983267](rs6983267/answer.md) | published mechanism | 2, **1** | 7, 7 | a join: the TCF/LEF group with CCAT2 |
| [rs642961](rs642961/answer.md) | published mechanism | 4, 4 | 6, 6 | nothing |
| [rs4784227](rs4784227/answer.md) | published mechanism | 6, 6 | 6, 6 | nothing |
| [rs12740374](rs12740374/answer.md) | published mechanism | 12, **1** | 7, 7 | a join: the C/EBP group with SORT1 |
| [rs1421085](rs1421085/answer.md) | published mechanism | 12, 12 | 7, 7 | nothing |
| [TERT C228T](tert_c228t/answer.md) | published mechanism, somatic | 8, **1** | 3, **5** | experiments filed under "-124C>T"; a deposited reporter assay; tumours by cancer type |
| [TERT C250T](tert_c250t/answer.md) | published mechanism, somatic | 11, 11 | 3, **5** | a deposited reporter assay; tumours by cancer type |
| [rs73706717](rs73706717/answer.md) | near-miss control | 6, 6 | 5, 5 | nothing |
| [rs34768248](rs34768248/answer.md) | near-miss control | 8, 8 | 6, 6 | nothing |
| [rs56007086](rs56007086/answer.md) | near-miss control | 1, 1 | 3, 3 | nothing |
| [rs13078086](rs13078086/answer.md) | random control | 1, 1 | 2, 2 | nothing |
| [rs11629191](rs11629191/answer.md) | random control | 1, 1 | 2, 2 | nothing |
| [rs7001688](rs7001688/answer.md) | random control | 316, 316 | 1, 1 | nothing |

- **Eight variants now end in one leading chain, where five did.**
- **No control changed.** The six controls hold what they held: nothing new counts for a variant with no
  published mechanism.

## What a public copy holds

The same four files as in [`demo/tables`](../tables/README.md): `answer.md`, `table.md`, `graph.json.gz` and
`manifest.json`, with every quoted passage bounded to 600 characters and the articles' text removed.

Rebuild the tables, with no key and no network:

```bash
uv run python scripts/v9_chain_table.py --runs demo/current --out /tmp/v2m_current
```
