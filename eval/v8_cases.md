# v8 per case (GPT-6 Luna)

Main arm (`full_given`: the given context, rsID masked, literature cut at the source paper's year). ✓ the gold TF named first, ✗ another TF. A control is right when the overall verdict is "no mechanism".

| Case | Kind | Gold TF | Agent, repeat 0 | Agent, repeat 1 | Agent, repeat 2 | Code only | Memory test | TF line, overall verdict (agent, repeat 0) |
|---|---|---|---|---|---|---|---|---|
| tert_c228t | TF, cancer | GABPA | E2F1 ✗ | E2F1 ✗ | E2F1 ✗ | E2F1 ✗ | GABPA ✓ | mechanism, mechanism |
| tert_c250t | TF, cancer | GABPA | E2F1 ✗ | E2F1 ✗ | E2F1 ✗ | E2F1 ✗ | GABPA ✓ | mechanism, mechanism |
| rs6983267 | TF, cancer | TCF7L2 | TCF7L2 ✓ | TCF7L2 ✓ | TCF7L2 ✓ | TCF7L2 ✓ | TCF7L2 ✓ | mechanism, mechanism |
| rs4784227 | TF, cancer | FOXA1 | GATA3 ✗ | GATA3 ✗ | GATA3 ✗ | MSX2 ✗ | FOXA1 ✓ | mechanism, mechanism |
| rs339331 | TF, cancer | HOXB13 | HOXB13 ✓ | HOXB13 ✓ | HOXB13 ✓ | HOXB13 ✓ | HOXB13 ✓ | mechanism, mechanism |
| rs2168101 | TF, cancer | GATA3 | GATA2 ✗ | GATA2 ✗ | GATA2 ✗ | GATA2 ✗ | GATA3 ✓ | mechanism, mechanism |
| rs12740374 | TF, other | CEBPA | HNF4A ✗ | SOX13 ✗ | HNF4A ✗ | HNF4A ✗ | CEBPA ✓ | mechanism, mechanism |
| rs1421085 | TF, other | ARID5B | ONECUT1 ✗ | ONECUT1 ✗ | FOXS1 ✗ | ONECUT1 ✗ | ARID5B ✓ | undetermined, undetermined |
| rs642961 | TF, other | TFAP2A | TFAP2C ✗ | TFAP2C ✗ | TFAP2C ✗ | TFAP2C ✗ | TFAP2A ✓ | undetermined, undetermined |
| rs13078086 | random control | none (control) | ZNF696 | no chain | ZNF696 | ZNF696 | TCF7L2 | no mechanism, no mechanism |
| rs11629191 | random control | none (control) | XBP1 | XBP1 | XBP1 | XBP1 | FOXA1 | no mechanism, no mechanism |
| rs7001688 | random control | none (control) | RELA | RELA | RELA | RELA | HNF4A | no mechanism, no mechanism |
| rs73706717 | near-miss control | none (control) | TCF7L2 | TCF7L2 | TCF7L2 | CTCF | TCF7L2 | mechanism, no mechanism |
| rs34768248 | near-miss control | none (control) | TCF3 | TCF3 | TCF3 | TCF3 | GABPA | mechanism, no mechanism |
| rs56007086 | near-miss control | none (control) | ESR1 | ESR1 | ESR1 | ESR1 | FOXA1 | mechanism, no mechanism |

- Agent: the gold TF first in 6/27 TF-case runs; right in all 3 repeats at 2/9 TF cases.
- Code-only baseline: 2/9 TF cases.
- Memory test, no tools and no evidence: 9/9 TF cases.
- Controls, agent, repeat 0: overall "no mechanism" 6/6; the TF line says "mechanism" at 3/6, and only the disease line turns those into "no mechanism".
