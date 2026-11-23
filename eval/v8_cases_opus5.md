# v8 per case (Claude Opus 5)

Main arm (`full_given`: the given context, rsID masked, literature cut at the source paper's year). ✓ the gold TF named first, ✗ another TF. A control is right when the overall verdict is "no mechanism".

| Case | Kind | Gold TF | Agent, repeat 0 | GPT-6 Luna, repeat 0 | Code only | TF line, overall verdict (agent, repeat 0) |
|---|---|---|---|---|---|---|
| tert_c228t | TF, cancer | GABPA | E2F1 ✗ | E2F1 ✗ | E2F1 ✗ | mechanism, mechanism |
| tert_c250t | TF, cancer | GABPA | E2F1 ✗ | E2F1 ✗ | E2F1 ✗ | mechanism, mechanism |
| rs6983267 | TF, cancer | TCF7L2 | TCF7L2 ✓ | TCF7L2 ✓ | TCF7L2 ✓ | mechanism, mechanism |
| rs4784227 | TF, cancer | FOXA1 | GATA3 ✗ | GATA3 ✗ | MSX2 ✗ | mechanism, mechanism |
| rs339331 | TF, cancer | HOXB13 | HOXB13 ✓ | HOXB13 ✓ | HOXB13 ✓ | mechanism, mechanism |
| rs2168101 | TF, cancer | GATA3 | GATA2 ✗ | GATA2 ✗ | GATA2 ✗ | mechanism, mechanism |
| rs12740374 | TF, other | CEBPA | HNF4A ✗ | HNF4A ✗ | HNF4A ✗ | mechanism, mechanism |
| rs1421085 | TF, other | ARID5B | FOXS1 ✗ | ONECUT1 ✗ | ONECUT1 ✗ | undetermined, undetermined |
| rs642961 | TF, other | TFAP2A | TFAP2C ✗ | TFAP2C ✗ | TFAP2C ✗ | undetermined, undetermined |
| rs13078086 | random control | none (control) | TFAP2E | ZNF696 | ZNF696 | no mechanism, no mechanism |
| rs11629191 | random control | none (control) | XBP1 | XBP1 | XBP1 | no mechanism, no mechanism |
| rs7001688 | random control | none (control) | RELA | RELA | RELA | no mechanism, no mechanism |
| rs73706717 | near-miss control | none (control) | CTCF | TCF7L2 | CTCF | mechanism, no mechanism |
| rs34768248 | near-miss control | none (control) | TCF3 | TCF3 | TCF3 | mechanism, no mechanism |
| rs56007086 | near-miss control | none (control) | ESR1 | ESR1 | ESR1 | mechanism, no mechanism |

- Agent: the gold TF first in 2/9 TF-case runs.
- GPT-6 Luna, repeat 0 (the saved grid): the gold TF first in 2/9 TF cases.
- Code-only baseline: 2/9 TF cases (the saved grid's runs: code only makes no model call).
- Controls, agent, repeat 0: overall "no mechanism" 6/6; the TF line says "mechanism" at 3/6, and only the disease line turns those into "no mechanism".
