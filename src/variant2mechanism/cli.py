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
    run.add_argument("--profile", help="a profile from config.yaml (models, run folders, budget); default: "
                    "default_profile (release), or none for the bare settings")

    ev = sub.add_parser("eval", help="evaluation runner")
    ev.add_argument("--pilot", action="store_true")
    ev.add_argument("--grid", choices=["named", "masked"])
    ev.add_argument("--metrics", action="store_true")
    ev.add_argument("--configs", nargs="+", choices=["single", "no_qbic", "full"],
                    default=["single", "no_qbic", "full"], help="with --grid: which configurations to run")
    ev.add_argument("--profile", help="a profile from config.yaml (models, run folders, budget); default: "
                    "default_profile (release), or none for the bare settings")
    ev.add_argument("--cases", nargs="+", help="with --grid: only these gold-set cases (default all)")
    ev.add_argument("--seeds", nargs="+", type=int, default=[0], help="with --grid: one run per seed (default 0)")
    ev.add_argument("--concurrency", type=int, help="with --grid: runs at once (default eval.concurrency); fewer "
                    "runs hold less of the budget in worst-case reservations")

    v8 = sub.add_parser("v8", help="v8: family screen, code tiers and verdict (agent-lab/v8-plan-draft.md)")
    v8.add_argument("action", choices=["run", "eval", "summary"])
    v8.add_argument("--case", help="run: a gold-set case_id")
    v8.add_argument("--arm", default="full_given", help="an evaluation arm (v8/evaluation.py ARMS)")
    v8.add_argument("--cases", nargs="+", help="eval: only these cases (default all)")
    v8.add_argument("--repeats", "--seeds", dest="repeats", nargs="+", type=int, default=[0],
                    help="repeat numbers (default 0); a repeat only changes the model cache key, it is not a sampling "
                         "seed (--seeds is the old name)")
    v8.add_argument("--code-only", action="store_true", help="no model calls: the code-only baseline")
    v8.add_argument("--profile", help="a profile from config.yaml, e.g. luna_v8 (default: default_profile, release)")
    v8.add_argument("--concurrency", type=int, default=4)
    v8.add_argument("--dev", action="store_true", help="kept for old scripts: a single run always charges the dev "
                    "budget and writes to v8.dev_dir, so it never displaces a saved evaluation run")
    v8.add_argument("--subdir", help="write under <v8.runs_dir>/<subdir> (smoke, pilot): kept out of the results")

    rp = sub.add_parser("replay", help="re-run a saved v8 run offline from the caches, with no API key, and compare "
                        "the reports; exit 0 identical, 1 different, 2 it would need a paid call")
    rp.add_argument("target", nargs="?", help="a gold-set case_id, or a saved run folder")
    rp.add_argument("--arm", default="full_given", help="with a case_id: the evaluation arm (default full_given)")
    rp.add_argument("--repeat", type=int, default=0, help="with a case_id: the repeat (default 0)")
    rp.add_argument("--code-only", action="store_true", help="with a case_id: the arm's code-only baseline")
    rp.add_argument("--runs-dir", help="the saved runs (default: v8.runs_dir in config.yaml, the Luna grid)")
    rp.add_argument("--out", help="output folder (default runs/replay/...); never inside the saved run")
    rp.add_argument("--render-only", action="store_true",
                    help="re-render the saved report.json as report.md and report.html, re-running nothing")
    rp.add_argument("--guard", action="store_true",
                    help="replay the guard set: the main arm's 15 code-only baselines and three agent runs")
    add_v9_parser(sub)
    q = sub.add_parser("qbic", help="QBiC-SELEX cache and cluster")
    qsub = q.add_subparsers(dest="qbic_command", required=True)
    imp = qsub.add_parser("import", help="poll and import a finished cluster run")
    imp.add_argument("run_id")
    return p


def add_v9_parser(sub) -> None:
    """`v2m v9 ...`: the claim-graph engine (v9/commands.py; the evaluator's audit and eval are wired below)."""
    v9 = sub.add_parser("v9", help="v9: the claim-graph engine (evidence bundles, runs, reports, replay, fixtures, "
                        "public exports; audit and eval for the evaluator)")
    v9sub = v9.add_subparsers(dest="v9_command", required=True)
    profile = ("a profile from config.yaml (models, run folders, budget); default: default_profile (release), or none "
               "for the bare settings")
    for name, text, modes in (
            ("evidence", "code's fact collection for one variant: every tool that applies with no TF or gene named; "
                         "no model call", "live: saved responses first, then the network; cache-only: saved "
                                          "responses only, never the network"),
            ("fill", "the chain table of one variant filled by code: every claim a database row or a model "
                     "prediction can count for, with its records; no model call unless --read is given",
             "live: saved responses first, then the network (and, with --read, the provider: the profile's dev "
             "budget); cache-only: saved responses only, never the network or a provider (with --read, a reply that "
             "is not cached stops the reading: exit 2)"),
            ("run", "investigate one variant: hypotheses, questions, evidence, revisions and a comparison",
             "live: saved responses and cached replies first, then the network and the provider (the profile's dev "
             "budget); cache-only: saved responses and cached model replies only, never the network or a provider "
             "(a reply that is not cached stops the run: exit 2)")):
        c = v9sub.add_parser(name, help=text)
        c.add_argument("--variant", required=True, help="chr2:60490908:T>G, 2:60490908 T>G or an rsID (GRCh38, plus "
                                                        "strand)")
        c.add_argument("--origin", choices=["germline", "somatic", "unknown"], default="unknown",
                       help="as supplied; never inferred (default unknown)")
        c.add_argument("--disease", action="append", default=[], help="a supplied disease or trait (repeat the flag "
                                                                      "for several)")
        c.add_argument("--context", action="append", default=[], help="a supplied cell line, cell type or tissue "
                                                                      "(repeat the flag for several)")
        c.add_argument("--request-id", help="the run's id (letters, digits, '.', '_', '-'); default REQ- and a hash "
                                            "of the request")
        c.add_argument("--out", help="a new run folder (default <v9.runs_dir>/<request id>); an existing folder is "
                                     "refused")
        c.add_argument("--mode", choices=["live", "cache-only"], default="live", help=modes)
        c.add_argument("--profile", help=profile)
        if name == "fill":
            c.add_argument("--read", action="store_true",
                           help="also fill the literature column: code finds the articles that name the variant and "
                                "a model reads each one once (one call per article), returning the experiments it "
                                "reports; code checks, files and links them")
            c.add_argument("--max-articles", type=int, default=None,
                           help="with --read: the most articles sent to the model in one run (default 30: every "
                                "article the three searches can list)")
            c.add_argument("--critic", action="store_true",
                           help="with --read: a second model, from another provider (v9.critic in config.yaml), "
                                "reads each experiment that is the only record behind a cell against the claims it "
                                "counts for; it can take a record out of the count, or point to further sentences "
                                "of the paragraph that state the result")
            c.add_argument("--judge", action="store_true",
                           help="with --read: when chains tie for first, the second model reads the experiments no "
                                "cell counts for the tied TFs and genes and says which of them an experiment ties to "
                                "the variant's site; the answer is written under the tie and changes no cell")
            c.add_argument("--skip-unread", action="store_true",
                           help="with --read in cache-only mode: an article whose reading is not saved is listed "
                                "as not read and the run goes on (without this a cache-only run stops at it); for "
                                "filing saved readings again under changed code, at no cost")
            c.add_argument("--loop", choices=["model", "code"], default=None,
                           help="with --read: after the first reading, go back for articles where the leading "
                                "chains tie or are weakest, for a few rounds. model: a planner model picks from "
                                "the menu code lists; code: the menu is taken in its own order (the baseline)")
            c.add_argument("--loop-rounds", type=int, default=None, help="with --loop: the most rounds (default 3)")
            c.add_argument("--loop-articles", type=int, default=None,
                           help="with --loop: the most new articles one round sends to the reader (default 10)")
            c.add_argument("--loop-dry", action="store_true",
                           help="with --loop: plan the first round and run its searches, read nothing new and send "
                                "no model any request (replies come from the response cache); for seeing what a "
                                "round would read before paying for it")
    rep = v9sub.add_parser("report", help="render report.html and report.md from a saved v9 run folder")
    rep.add_argument("--run", required=True, help="a v9 run folder")
    rep.add_argument("--out", help="a new folder for a render-only report (default: the run folder, where existing "
                                   "reports are never overwritten)")
    rpl = v9sub.add_parser("replay", help="re-run a saved v9 run offline from its bundle and the response cache, and "
                           "compare graph.json; exit 0 identical, 1 different or failed (or the saved run changed "
                           "after it was written), 2 a cache miss or a run that cannot be replayed")
    rpl.add_argument("run_dir", metavar="DIR", help="a saved v9 run folder")
    rpl.add_argument("--out", help="a new folder for the replay (default runs/replay/v9/<run>-<time>); never inside "
                                   "the saved run")
    fx = v9sub.add_parser("fixture", help="run the engine on a synthetic fixture with its scripted roles (no network, "
                          "no model, not biological evidence)")
    fx.add_argument("fixture", help="synthetic, another fixture name in v9/fixtures, or a fixture file")
    fx.add_argument("--out", required=True, help="a new run folder")
    fx.add_argument("--profile", help=profile)
    ex = v9sub.add_parser("export", help="a public copy of a run: verified passages only, no article text and no "
                          "evaluation")
    ex.add_argument("--run", required=True, help="a v9 run folder")
    ex.add_argument("--out", required=True, help="a new folder outside the run")
    au = v9sub.add_parser("audit", help="evaluator only: score a finished run against the gold specification "
                          "(writes evaluation.json in the run folder, never read by the engine)")
    au.add_argument("--run", required=True, help="a finished v9 run folder")
    au.add_argument("--case", required=True, help="the run's case id in the gold specification")
    au.add_argument("--profile", help=profile)
    ev9 = v9sub.add_parser("eval", help="evaluator only: a frozen suite under an explicit currency cap (refused "
                           "without --budget-usd; the suite runner is not built yet)")
    ev9.add_argument("--suite", required=True, help="the frozen suite manifest of clean requests")
    ev9.add_argument("--budget-usd", type=float, help="the explicit currency cap for the whole suite (required)")


def v9_command(args) -> int:
    if args.v9_command in ("audit", "eval"):
        return v9_evaluator_command(args)
    if args.v9_command == "replay":                  # as `v2m replay`: the outcome lines, not the run's progress
        logging.getLogger().setLevel(logging.WARNING)
    from .v9 import commands
    return commands.main(args)


def v9_evaluator_command(args) -> int:
    """`v2m v9 audit` and `v2m v9 eval`, the evaluator's entry points. They are wired here because no v9 module but
    the evaluator itself may import it: gold material stays out of every engine path. A refusal exits 2."""
    from .config import ConfigError, profile_config
    from .v9 import evaluation as ev
    try:
        if args.v9_command == "audit":
            cfg = profile_config(args.profile)
            print(ev.write_evaluation(args.run, ev.spec_entry(ev.load_gold_spec(config=cfg), args.case), config=cfg))
            return 0
        ev.run_suite(args.suite, args.budget_usd)
    except NotImplementedError as e:
        print(f"v9 {args.v9_command}: the suite runner is not built yet ({e})", file=sys.stderr)
    except (ev.SuiteRefusal, KeyError, ValueError, FileExistsError, FileNotFoundError, ConfigError) as e:
        print(f"v9 {args.v9_command}: {e.args[0] if isinstance(e, KeyError) and e.args else e}", file=sys.stderr)
    return 2


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
    from .config import ConfigError, profile_config
    from .qbic.variants import VariantError
    try:
        cfg = profile_config(args.profile)
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
    from .config import REPO, profile_config
    from .evaluation import metrics, runner
    from .evaluation.gold import excluded, load_gold, scored_cases
    cfg = profile_config(args.profile)
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
        unknown = set(args.cases or []) - set(cases)
        if unknown:
            print(f"not in the scored gold set: {', '.join(sorted(unknown))}", file=sys.stderr)
            return 2
        cases = [c for c in cases if not args.cases or c in args.cases]
        rows = []
        for seed in args.seeds:                    # the model cache keys on the seed, so each seed makes new calls
            rows += runner.run_grid(cases, args.configs, masked=args.grid == "masked", seed=seed, cfg=cfg,
                                    concurrency=args.concurrency)
            if any(r["status"] == "budget" for r in rows):
                break
    else:
        print("give --pilot, --grid named|masked or --metrics", file=sys.stderr)
        return 2
    for r in rows:
        print(r)
    return 0


def v8_command(args) -> int:
    import json

    from .config import REPO, profile_config
    from .v8 import evaluation as ev
    cfg = profile_config(args.profile)
    if args.subdir:
        cfg = type(cfg)({**cfg, "v8": {**cfg["v8"], "runs_dir": f"{cfg['v8']['runs_dir']}/{args.subdir}",
                                       "dev_dir": f"{cfg['v8']['dev_dir']}/{args.subdir}"}})
    if args.action == "summary":
        df = ev.collect(cfg)
        print(ev.summary(df, ev.attempts(cfg)).to_string(index=False) if len(df) else "no v8 runs yet")
        return 0
    if args.action == "run":
        from .agent.case import load_gold_case
        from .v8.run import run_case8
        a = ev.ARMS[args.arm]
        d = (REPO / cfg["v8"]["dev_dir"] / ("code/" if args.code_only else "") / args.arm / str(args.repeats[0])
             / args.case)
        r = run_case8(load_gold_case(args.case, cfg), arm=a["arm"], masked=a["masked"], seed=args.repeats[0], cfg=cfg,
                      run_dir=d, phase="dev", infer=a["infer"], code_only=args.code_only)
        print(json.dumps({k: r[k] for k in ("case_id", "arm", "cost_usd", "seconds", "model_calls")}))
        print(json.dumps(r.get("verdict"), indent=1)[:1500])
        return 0
    status = ev.run_arm(args.arm, args.cases, args.repeats, cfg, code_only=args.code_only,
                        concurrency=args.concurrency)
    for s in sorted(status, key=lambda s: (s["repeat"], s["case_id"])):
        print(json.dumps(s))
    return 0 if all(s["status"] in ("ok", "skipped (done)") for s in status) else 1


def replay_command(args) -> int:
    from pathlib import Path

    from .v9 import replay as rp
    runs_dir = Path(args.runs_dir) if args.runs_dir else None
    if args.guard:
        results = rp.guard(runs_dir, Path(args.out) if args.out else None)
        for r in results:
            print(r.line())
            for d in r.differences[:5]:
                print(f"    {d}")
        n = {s: sum(r.status == s for r in results) for s in rp.EXIT}
        print(f"{len(results)} replays: " + ", ".join(f"{k} {v}" for k, v in n.items() if v))
        return max((r.code for r in results), default=0)
    if not args.target:
        print("give a case_id or a saved run folder, or --guard", file=sys.stderr)
        return 2
    if (Path(args.target) / "manifest.json").is_file():      # a v9 run folder goes to the v9 replay
        from .v9 import commands
        if commands.is_v9_run(Path(args.target)):
            return commands.replay_folder(Path(args.target), Path(args.out) if args.out else None,
                                          render_only=args.render_only)
    try:
        t = Path(args.target)
        saved = t if (t / "report.json").exists() else rp.find_run(args.target, args.arm, args.repeat,
                                                                   args.code_only, runs_dir)
        out = Path(args.out) if args.out else rp.default_out(saved)
        if args.render_only:
            for p in rp.render(saved, out):
                print(p)
            return 0
        r = rp.replay(saved, out)
    except (FileNotFoundError, ValueError) as e:
        print(f"replay: {e}", file=sys.stderr)
        return 1
    print(r.line())
    for d in r.differences[:20]:
        print(f"  {d}")
    if r.added:
        print(f"  fields the saved report does not have: {', '.join(r.added[:10])}")
    if r.status in ("identical", "different"):
        print(f"output: {out}")
    return r.code


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S")
    args = build_parser().parse_args(argv)
    if args.command == "qbic":
        return qbic_command(args)
    if args.command == "replay":
        logging.getLogger().setLevel(logging.WARNING)
        return replay_command(args)
    if args.command == "run":
        return run_command(args)
    if args.command == "eval":
        return eval_command(args)
    if args.command == "v8":
        return v8_command(args)
    if args.command == "v9":
        return v9_command(args)
    print(f"v2m {args.command}: not built yet", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
