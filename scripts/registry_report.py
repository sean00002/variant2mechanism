"""Print name resolution, coverage, group and expression for each gold-set TF (spec 1, checkpoint 4)."""

import pandas as pd

from variant2mechanism.config import load_config
from variant2mechanism.evaluation.gold import is_control
from variant2mechanism.qbic.expression import get_expression
from variant2mechanism.qbic.registry import get_registry


def main():
    cfg = load_config()
    reg, expr = get_registry(), get_expression()
    gold = pd.read_csv(cfg.path("eval", "gold_set"), dtype=str, keep_default_na=False)
    for row in gold.itertuples(index=False):
        if is_control(row):
            print(f"{row.case_id:11} control: no causal TF (the correct answer is the null)")
            continue
        for name in [t.strip() for t in row.causal_tf.split(",")]:
            r = reg.resolve_tf(name)
            sym = r["symbol"]
            cov = reg.coverage(sym) if sym else {"status": r["status"]}
            groups = reg.groups_of_tf(sym) if sym else []
            gtxt = "; ".join(f"{g['id']} {g['label']}" for g in groups) or "-"
            e = expr.tf_expression([sym], row.expression_context)[sym] if sym else {}
            etxt = (f"TPM {e['tpm']}, rank {e.get('rank_among_tfs')}/{e.get('n_tfs')}"
                    + (f", {e['n_lines']} lines" if "n_lines" in e else "")) if e.get("tpm") is not None \
                else e.get("source", "-")
            print(f"{row.case_id:11} {name:7} -> {sym or r['status']:7} {cov['status']:16} {gtxt:38} {etxt}")


if __name__ == "__main__":
    main()
