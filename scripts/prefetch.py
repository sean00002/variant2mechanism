"""One array job with statistics for every gold-set variant not yet cached (spec 1, section 9).

Without --submit it only prints what it would run. Afterwards it prints, per case, n_pass, the top 3 groups and
whether the gold TF's group is in the top 10. It does not judge the biology.
"""

import argparse
import logging
import sys

import pandas as pd

from variant2mechanism.config import load_config
from variant2mechanism.evaluation.gold import is_control
from variant2mechanism.qbic.backend import get_backend
from variant2mechanism.qbic.tools import QbicTools
from variant2mechanism.qbic.variants import Variant


def summary(cfg) -> None:
    tools = QbicTools(cfg)
    reg = tools.registry
    gold = pd.read_csv(cfg.path("eval", "gold_set"), dtype=str, keep_default_na=False)
    for row in gold.itertuples(index=False):
        out = tools.qbic_screen(row.chrom, row.pos_grch38, row.ref, row.alt, row.expression_context, compact=False)
        if "error" in out:
            print(f"{row.case_id:11} ERROR {out['error']}")
            continue
        top3 = "; ".join(f"{g['label']} z={g['z']}" for g in out["groups"][:3])
        if is_control(row):
            rank = "control (null)"
        else:
            gold_groups = set()
            for name in str(row.causal_tf).split(","):
                sym = reg.resolve_tf(name.strip())["symbol"]
                gold_groups |= {g["id"] for g in reg.groups_of_tf(sym)} if sym else set()
            ids = [g["group"] for g in out["groups"]]
            hit = [ids.index(g) + 1 for g in gold_groups if g in ids]
            rank = min(hit) if hit else ("n/a" if not gold_groups else ">10")
        print(f"{row.case_id:11} n_pass={out['n_pass']:4d} dropped={out['dropped_by_expression']['count']:3d} "
              f"gold group rank={rank}  | {top3}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--submit", action="store_true", help="submit the job to the cluster")
    ap.add_argument("--summary-only", action="store_true")
    ap.add_argument("--backend", choices=["slurm", "local"], help="override qbic.backend in config.yaml")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
    cfg = load_config()
    if not args.summary_only:
        gold = pd.read_csv(cfg.path("eval", "gold_set"))
        variants = sorted({Variant.make(r.chrom, r.pos_grch38, r.ref, r.alt) for r in gold.itertuples(index=False)})
        c = get_backend(cfg, args.backend)
        todo = [v for v in variants if v.key() not in c.cache.cached([v.key()], stats=True)]
        print(f"{len(variants)} gold-set variants, {len(todo)} not cached with statistics: "
              f"{', '.join(v.key() for v in todo)}")
        if c.name == "slurm":
            print(f"job: partition {cfg['slurm']['partition']}, {cfg['slurm']['model_chunks']} tasks, "
                  f"device {cfg['slurm']['device']}, statistics on")
        else:
            print(f"local: {cfg['local']['workers']} parallel qbic-selex processes, statistics on")
        if todo and not args.submit:
            print("dry run: pass --submit to run it")
            return 0
        if todo:
            run_id = c.run(todo, stats=True)
            run = c.load_run(run_id)
            print(f"run {run_id}, job {run['slurm_job']}, wall {run['wall_seconds']} s, "
                  f"task seconds {run['task_seconds']}")
    summary(cfg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
