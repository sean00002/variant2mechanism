# Saved runs of the 15 test variants

Public copies of the runs that were scored on 23 November 2026 ([`docs/report.md`](../../docs/report.md)). Each
run started from the variant alone: no disease and no cell context were given.

| File | What it is |
|---|---|
| `answer.md` | The top of the run's report: the ranked chains, the first chain's table, the numbers each source returned, what would fill the gaps, and the outcome |
| `table.md` | The first chain's eight claims and their cells |
| `graph.json.gz` | The run's claim graph: every claim, record and link. The tables, the reports and the scores are built from it |
| `manifest.json` | What ran (models, formats, sources) and what the public copy cut |

## The runs

| Run | Kind | Chains tied for first | Claims of the first chain with support, of 8 |
|---|---|---|---|
| [rs339331](rs339331/answer.md) | published mechanism | 1 | 7 |
| [rs2168101](rs2168101/answer.md) | published mechanism | 1 | 7 |
| [rs6983267](rs6983267/answer.md) | published mechanism | 2 | 7 |
| [rs642961](rs642961/answer.md) | published mechanism | 4 | 6 |
| [rs4784227](rs4784227/answer.md) | published mechanism | 6 | 6 |
| [rs12740374](rs12740374/answer.md) | published mechanism | 12 | 7 |
| [rs1421085](rs1421085/answer.md) | published mechanism | 12 | 7 |
| [TERT C228T](tert_c228t/answer.md) | published mechanism, somatic | 8 | 3 |
| [TERT C250T](tert_c250t/answer.md) | published mechanism, somatic | 11 | 3 |
| [rs73706717](rs73706717/answer.md) | near-miss control | 6 | 5 |
| [rs34768248](rs34768248/answer.md) | near-miss control | 8 | 6 |
| [rs56007086](rs56007086/answer.md) | near-miss control | 1 | 3 |
| [rs13078086](rs13078086/answer.md) | random control | 1 | 2 |
| [rs11629191](rs11629191/answer.md) | random control | 1 | 2 |
| [rs7001688](rs7001688/answer.md) | random control | 316 | 1 |

## What a public copy leaves out

`scripts/v9_demo_export.py` made these folders from the saved runs. A public copy bounds every quoted passage to 600
characters, removes the articles' text and cuts local paths. `answer.md` also leaves out the report's two
subsections that quote the articles. The quotations are in the graph, and a rendered report shows them.

## Using them

Rebuild the tables, with no key and no network:

```bash
uv run python scripts/v9_chain_table.py --runs demo/tables --out /tmp/v2m_tables
```

Render one run's whole report:

```bash
mkdir -p /tmp/v2m_run && gunzip -c demo/tables/rs339331/graph.json.gz > /tmp/v2m_run/graph.json
uv run v2m v9 report --run /tmp/v2m_run
```

Recompute the score (needs two public reference tables; see the main [README](../../README.md)):

```bash
uv run python scripts/v9_table_score.py --runs demo/tables --out /tmp/v2m_score
```

The tables built from these copies are identical to those of the original runs, and the score is the same.
