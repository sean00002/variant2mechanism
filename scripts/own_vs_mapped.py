"""Own versus CIS-BP-mapped QBiC-SELEX models (eval/results.md). Offline: Table S6 and the QBiC-SELEX cache.

1. Primary collection: how often a mapped model has a higher cross-experiment r than the TF's own model.
2. SNP-SELEX (Table S6, secondary collection): the TF's own model against its mapped models on that TF's
   allelic-binding benchmark.
3. Gold set: own and mapped models at each gold variant, from the cache.

    uv run python scripts/own_vs_mapped.py
"""

import pandas as pd
from scipy.stats import spearmanr, wilcoxon

from variant2mechanism.config import load_config
from variant2mechanism.evaluation.gold import is_control, load_gold, scoring_tf
from variant2mechanism.evaluation.metrics import load_direction_labels
from variant2mechanism.qbic.tools import QbicTools

BATCHES = {"first": "snpselex_first_batch_pearsonr", "novel": "snpselex_novel_batch_pearsonr"}


def quality(s6: pd.DataFrame) -> None:
    prim = s6[s6.model_collection == "primary"]
    rows = []
    for _tf, g in prim.groupby("tf_hgnc_symbol"):
        own, mapped = g[g.mapping_type == "cognate"], g[g.mapping_type == "CIS-BP"]
        if len(own) and len(mapped):
            rows.append((own.cross_exp_pearsonr.max(), mapped.cross_exp_pearsonr.max()))
    t = pd.DataFrame(rows, columns=["own", "best_mapped"])
    print(f"Primary collection: {len(t)} TFs have their own model and CIS-BP-mapped models. A mapped model has the "
          f"higher cross-experiment r in {(t.best_mapped > t.own).sum()} ({(t.best_mapped > t.own).mean():.0%}); "
          f"higher by more than 0.05 in {(t.best_mapped > t.own + 0.05).sum()}.\n")


def snpselex(s6: pd.DataFrame) -> None:
    sec = s6[s6.model_collection.str.startswith("secondary")]
    in_primary = set(sec.mapped_model_id) & set(s6[s6.model_collection == "primary"].mapped_model_id)
    print(f"SNP-SELEX, secondary collection ({sec.mapped_model_id.nunique()} models, {len(in_primary)} of them in "
          "the primary collection). Per TF with its own model and at least one mapped model scored:\n")
    print("| | " + " | ".join(f"{b} batch" for b in BATCHES) + " |")
    print("|---|" + "---|" * len(BATCHES))
    stats = {}
    for b, col in BATCHES.items():
        d = sec[sec[col].notna()]
        out = []
        for _tf, g in d.groupby("tf_hgnc_symbol"):
            own, mapped = g[g.mapping_type == "cognate"], g[g.mapping_type == "CIS-BP"]
            if len(own) and len(mapped):
                by_q = mapped.sort_values("within_exp_pearsonr", ascending=False).iloc[0]
                out.append({"own": own[col].max(), "median": mapped[col].median(), "by_quality": by_q[col],
                            "best": mapped[col].max(), "n": len(mapped)})
        t = pd.DataFrame(out)
        rho = spearmanr(d.within_exp_pearsonr, d[col], nan_policy="omit").statistic
        stats[b] = {"TFs": f"{len(t)}", "Mapped models per TF, median": f"{t.n.median():.0f}",
                    "Own model, median r": f"{t.own.median():.2f}",
                    "Mapped models, median r": f"{t['median'].median():.2f}",
                    "Median mapped model beats own": f"{(t['median'] > t.own).mean():.0%}",
                    "Highest-quality mapped model beats own": f"{(t.by_quality > t.own).mean():.0%} "
                                                              f"(Wilcoxon p {wilcoxon(t.own, t.by_quality).pvalue:.2f})",
                    "Best mapped model, chosen after the fact, beats own": f"{(t.best > t.own).mean():.0%}",
                    "Spearman, model quality vs SNP-SELEX r (all rows)": f"{rho:.2f}"}
    for key in stats["first"]:
        print(f"| {key} | " + " | ".join(stats[b][key] for b in BATCHES) + " |")
    print()


def gold_variants() -> None:
    labels = load_direction_labels()
    tools = QbicTools()
    print("| Case | TF | Label | Own model | Mapped models | Passing models agreeing with the label | "
          "Highest-quality model |")
    print("|---|---|---|---|---|---|---|")
    for r in load_gold().to_dict("records"):
        if is_control(r):
            continue
        tf = scoring_tf(r)
        d = tools.qbic_tf_detail(r["chrom"], int(r["pos_grch38"]), r["ref"], r["alt"], tf)
        want = labels.loc[r["case_id"], "allele_binding_more"]
        models = d.get("models", [])
        if not models:
            print(f"| {r['case_id']} | {tf} | {want} | none: {d.get('coverage')} | | | |")
            continue

        def allele(m):
            return "alt" if m["effect"] > 0 else "ref"

        def gate(m):
            return "" if m["passed_gate"] else ", fails the gate"

        own = [m for m in models if m["mapping"] == "own"]
        mapped = [m for m in models if m["mapping"] != "own"]
        passing = [m for m in models if m["passed_gate"]]
        top = max(models, key=lambda m: m["quality"])
        own_txt = (f"z {own[0]['z']:+.1f}, quality {own[0]['quality']:.2f}{gate(own[0])}" if own else "none")
        shown = f"{len(mapped)}" + (f" (+{d['n_models_trimmed']} not shown)" if d.get("n_models_trimmed") else "")
        print(f"| {r['case_id']} | {tf} | {want} | {own_txt} | {shown}, {sum(m['passed_gate'] for m in mapped)} pass | "
              f"{sum(allele(m) == want for m in passing)} of {len(passing)} | {top['model'].split('_')[0]} "
              f"({top['quality']:.2f}): z {top['z']:+.1f}{gate(top)} |")


def main():
    s6 = pd.read_csv(load_config().path("data", "table_s6"))
    quality(s6)
    snpselex(s6)
    gold_variants()


if __name__ == "__main__":
    main()
