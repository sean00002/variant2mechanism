"""Statistical genetics on summary statistics: fine-mapping and colocalisation of a GWAS signal with a molecular QTL.

No language model is called anywhere in this package. It answers two questions about a window of the genome, from
association statistics alone:

- which variants could be the causal one for a trait (fine-mapping), and
- whether a trait and a gene's expression share a causal variant there (colocalisation).

    abf.py        Wakefield's approximate Bayes factor per variant; the posterior and the credible set that follow
                  when the window holds exactly one causal variant
    coloc.py      colocalisation of two traits under that assumption (Giambartolomei et al. 2014): the posterior
                  probabilities of the five hypotheses H0 to H4, and each variant's share of H4
    susie.py      the sum of single effects model fitted to z-scores and an LD matrix (Wang et al. 2020; Zou et al.
                  2022), for windows with more than one causal variant; needs LD from the GWAS sample itself
    simulate.py   a locus with known causal variants, in LD, for the tests and for showing what each method assumes
    sumstats.py   one window of a harmonised GWAS file (GWAS Catalog) or of an eQTL dataset (eQTL Catalogue), read
                  by tabix over HTTPS and cached; alleles matched between the two
    locus.py      the analysis of one window: a GWAS against every gene of an eQTL dataset
    plot.py       the regional figure of that analysis

What each method assumes, and what breaks it:

- abf.py and coloc.py need no LD. They assume at most one causal variant per trait in the window. With two signals
  for one trait the posterior follows the stronger one, and colocalisation of the weaker is missed.
- susie.py allows several causal variants, and for that it needs the correlation between the variants in the very
  sample the z-scores come from. A reference panel only approximates it, and with a large GWAS a small mismatch
  creates signals that are not there. Here it is run only where the LD is right: on simulated data, where the LD
  is computed from the same genotypes. For published data the credible sets the source computed in-sample are read
  instead of being recomputed.
- Colocalisation says that two traits share a causal variant. It does not say which gene mediates the trait: when
  several genes' expression colocalises with one signal, nothing in this package chooses among them.
"""
