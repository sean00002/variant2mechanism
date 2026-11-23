# Source-local extraction repair and variant identity

A rejected experiment now receives one bounded repair per source/location before another discovery round.
The retry includes the specific failure and original read/location. Whole-sentence selectors let code copy
source text rather than relying on another generated quotation. The existing assay, scope, variant and direction
checks still run. A missing source leaves an explicit processing gap; reserved audit/final capacity is preserved.
Valid experiments and previous refusal events remain in the graph. Repair adds no HTTP or literature-read call.

Identity metadata distinguishes verified same, verified different and unresolved. During a CIViC gene survey,
at most six catalogue SNV names are checked against exact NCBI primary-assembly placements for the input
substitution. The catalogue's declared build, chromosome, position and ordered alleles must match. This creates
identity metadata, never experimental evidence. The verified names become discovery terms in role packets.
Names outside the bounded survey remain unverified and can be queried explicitly.

A DNA shorthand actually named in a promoter/sequence experiment can be retained in a paper namespace even
without a case mapping. Such evidence cannot support or contradict a case-variant claim. An exact catalogue
name and gene, plus compatible ordered alleles and verified coordinates, can map it to the case. Paper notation,
catalogue provenance, placement provenance and any strand conversion are retained. No coordinate is inferred
from a numeric suffix, and complementary shorthand names are not invented. This is bounded SNV support, not
universal HGVS, protein or transcript resolution. An unresolved identity is not evidence of difference.

Minor/major labels are not assumed to be alternate/reference bases. When the effect base is unknown, keep the
relative observation but leave the allele and genomic direction unresolved. Repeated abstract text now takes
part in content-based no-progress detection; new passages or genuinely different claim scopes remain allowed.

Regression coverage includes exact source copying, negation preservation, one retry without rereading, audit
reserve protection, paper-scoped retention, wrong alleles/positions/builds, gene scoping, no invented complementary
aliases, catalogue identity without biological evidence, and new text versus repeated abstract text. No expected
case gene, TF, primary-paper lookup table or gold label was added to production code.

## Frozen development reruns — 10 November 2026

The complete suite passed: 1,120 tests, one real-cluster test skipped. Lint passed. Both runs used the same
frozen production source, v9 tests and configuration, with coordinates, alleles and origin only. Existing
graphs and gold labels were hash-checked and preserved. No cluster job was submitted.

| Case / saved run | New supported molecular claims | Remaining limit | Cost |
|---|---|---|---|
| rs12740374 / `dev13_rs12740374_source_repair_20261110` | C5: in-vitro minor/major binding difference; C10: Hep3B reporter effect | T-versus-G direction remains unresolved in these extracts; no complete disease chain | $0.082200 |
| TERT / `dev14_tert_c228t_alias_repair_20261110` | C7: A-versus-G reporter activity increase in the reported cell-line assays | No supported member-specific binding or endogenous/disease mechanism | $0.042341 |

The rs12740374 run exercised two repair calls: the binding repair succeeded; the reporter repair proposed an
unlisted span and was refused. A later ordinary extraction retained the reporter result. The TERT run exercised
one successful repair and verified the C228T alias against catalogue coordinates and NCBI placements. Its final
experiment mapping used an explicit paper coordinate plus NCBI, not the catalogue-only experiment mapper.

The two reruns cost $0.124541; cumulative development spend is $0.690928 of $5, with no reservations remaining.
Both ended at the unchanged guarded call allowance (17 sends each), not the currency ceiling. This is a
development comparison, not an ablation or blind validation. Duplicate drafts, comparison-level polarity,
paper-local allele definitions and repair of refused graph links remain limitations.

Open [the portable HTML report](../demo/v9/repair-alias-check-20261110/index.html) for before/after counts,
claim diagrams, source links, refusal reasons and the complete manual audit. The generator is
`scripts/v9_repair_alias_report.py`; it reads saved runs without model or network calls.
