"""Command line: `v2m run`, `v2m eval`, `v2m qbic`."""

import argparse
import logging
import sys

from .qbic.backend import get_backend


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="v2m", description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="run the workflow on one case or variant")
    run.add_argument("--case", help="gold-set case_id")
    run.add_argument("--variant", help="rsID or chr:pos:ref>alt (GRCh38, plus strand)")
    run.add_argument("--disease")
    run.add_argument("--context", help="expression context, e.g. DepMap:ACH-000971")
    run.add_argument("--alt", help="alternate allele, for rsIDs with more than one")
    run.add_argument("--config", choices=["single", "no_qbic", "full"], default="full")
    run.add_argument("--masked", action="store_true")
    run.add_argument("--seed", type=int, default=0)
    run.add_argument("--refresh", action="store_true", help="bypass the HTTP cache")
    run.add_argument("--somatic", action="store_true", help="with --variant: a somatic mutation (default germline)")
    run.add_argument("--profile", help="a profile from config.yaml (models, run folders, budget), e.g. deepseek")

    ev = sub.add_parser("eval", help="evaluation runner")
    ev.add_argument("--pilot", action="store_true")
    ev.add_argument("--grid", choices=["named", "masked"])
    ev.add_argument("--metrics", action="store_true")
    ev.add_argument("--configs", nargs="+", choices=["single", "no_qbic", "full"],
                    default=["single", "no_qbic", "full"], help="with --grid: which configurations to run")
    ev.add_argument("--profile", help="a profile from config.yaml (models, run folders, budget), e.g. deepseek")
    ev.add_argument("--concurrency", type=int, help="with --grid: runs at once (default eval.concurrency); fewer "
                    "runs hold less of the budget in worst-case reservations")

    q = sub.add_parser("qbic", help="QBiC-SELEX cache and cluster")
    qsub = q.add_subparsers(dest="qbic_command", required=True)
    imp = qsub.add_parser("import", help="poll and import a finished cluster run")
    imp.add_argument("run_id")
    return p


def qbic_command(args) -> int:
    if args.qbic_command == "import":
        run = get_backend().import_run(args.run_id)
        print(f"imported {run['rows_imported']} rows from {run['run_id']} (job {run['slurm_job']}), "
              f"task seconds {run['task_seconds']}")
        return 0
    return 2


def case_from_args(args):
    from .agent.case import CaseSpec, load_gold_case
    if args.case:
        spec = load_gold_case(args.case)
        if args.context:
            spec.expression_context = args.context
        return spec
    if not args.variant or not args.disease:
        raise SystemExit("give --case, or --variant and --disease")
    from .config import load_config
    from .context.ensembl import resolve_rsid
    from .context.http import Http
    from .qbic.variants import parse
    if args.variant.lower().startswith("rs"):
        v, rsid = resolve_rsid(Http(load_config().path("tools", "http_cache")), args.variant, args.alt), args.variant
    else:
        v, rsid = parse(args.variant), None
    origin = "somatic" if args.somatic else "germline"
    return CaseSpec(args.variant.replace(":", "_").replace(">", "_"), args.variant, v, origin, args.disease,
                    args.context, rsid)


def run_command(args) -> int:
    from .agent.llm import LLMError
    from .agent.run import run_case
    from .agent.stages.screen import RunStopped
    from .config import ConfigError, load_config, with_profile
    from .qbic.variants import VariantError
    try:
        cfg = with_profile(load_config(), args.profile)
        spec = case_from_args(args)
        report = run_case(spec, args.config, masked=args.masked, seed=args.seed, refresh=args.refresh, cfg=cfg)
    except (RunStopped, LLMError, VariantError, KeyError, ConfigError) as e:
        print(f"run stopped: {e}", file=sys.stderr)
        return 1
    top = report["chains"][:2]
    print(f"{report['case_id']} {report['config']} {report['mode']}: ${report['cost_usd']:.2f}, "
          f"{report['seconds']:.0f} s, {report['model_calls']} model calls, "
          f"{len(report['rounds'])} rounds, {sum(c['run'] for c in report['investigate_calls'])} tool calls, "
          f"{len(report['flags'])} flags")
    for c in top:
        print(f"  {c['rank']}. {c['id']} p={c['probability']:.2f} {c['title']}")
    return 0


def eval_command(args) -> int:
    from .config import REPO, load_config, with_profile
    from .evaluation import metrics, runner
    from .evaluation.gold import excluded, load_gold, scored_cases
    cfg = with_profile(load_config(), args.profile)
    gold = scored_cases(load_gold(cfg), cfg)
    if args.metrics:
        from .qbic.registry import get_registry
        df = metrics.collect(REPO / cfg["eval"]["runs_dir"], get_registry(), gold, metrics.load_direction_labels())
        print(metrics.summarise(df).to_string(index=False) if len(df) else "no saved runs to score")
        for case_id, why in excluded(cfg).items():
            print(f"not scored: {case_id} ({why})")
        return 0
    if args.pilot:
        rows = runner.pilot(cfg)
    elif args.grid:
        cases = gold.case_id.tolist()
        rows = runner.run_grid(cases, args.configs, masked=args.grid == "masked", cfg=cfg,
                               concurrency=args.concurrency)
    else:
        print("give --pilot, --grid named|masked or --metrics", file=sys.stderr)
        return 2
    for r in rows:
        print(r)
    return 0


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
    args = build_parser().parse_args(argv)
    if args.command == "qbic":
        return qbic_command(args)
    if args.command == "run":
        return run_command(args)
    if args.command == "eval":
        return eval_command(args)
    print(f"v2m {args.command}: not built yet", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
