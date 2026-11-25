"""Fill the chain table for every case of the gold specification: the "code only" arm, or with --read the "code
and reader" arm.

    python scripts/v9_fill_suite.py --out runs/fill_code_only_<date>
    python scripts/v9_fill_suite.py --out runs/fill_reader_<date> --read --budget-usd 1.00
    python scripts/v9_chain_table.py --runs runs/fill_code_only_<date> --out runs/chain_table_fill_<date>

It reads only each case's clean request (variant, origin, and for the supplied_disease form the disease) from
eval/v9_gold_spec.json: no label, component or note reaches the fill, which is started as a separate process
(`v2m v9 fill`) per case. Without --read no model is called and nothing is spent: a live run makes the free lookups
a variant needs (Ensembl, GTEx, the GWAS Catalog, ENCODE, ReMap, Open Targets); --mode cache-only makes none.

With --read each case also searches Europe PMC and has a model read the articles found, one call per article, at
most --max-articles per case (reader.py). That spends money, so --budget-usd is required: the suite stops before a
case once the cases so far have cost that much, and the profile's own budget still applies to every call. The cost
of a case is read from its metrics.json.

With --requests FILE the cases come from that file instead of the gold specification: a JSON list of requests, each
with a case_id, a variant and an origin (disease and context are optional lists). That is how the reader is
developed on variants outside the gold cases (eval/reader_dev_requests.json), so no choice about it is made by
looking at a labelled case.

With --critic as well (it needs --read), a second model from another provider reads each experiment that is the
only record behind a cell against the claims it counts for, one call per such experiment (critic.py). The same
budget covers both.

With --judge as well (it needs --read), when chains tie for first that second model also reads the experiments no
cell counts for the tied TFs and genes, at most two calls a case (judge.py). The same budget covers it.

With --loop model|code as well (it needs --read), each case goes back for articles after its first reading, where
its leading chains tie or are weakest, for a few rounds (loop.py): "model" has a planner model pick from the menu
code lists, "code" takes the menu in its own order, which is the baseline arm. --loop-dry plans the first round and
runs its searches, reads nothing new and sends no model any request, so it needs no budget.

A case that already has a folder is skipped, so an interrupted suite resumes; nothing is re-run or overwritten.
suite.json records the commit, whether the working tree was clean, and each case's exit code, seconds and cost.
With --dry-run it prints what it would do and starts nothing.
"""

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "eval" / "v9_gold_spec.json"


def requests(form: str, path: Path | None = None) -> list[dict]:
    """The clean requests, in the specification's order: nothing but what a user would type. With `path`, the
    requests of that file instead (a JSON list; disease and context default to none)."""
    if path is not None:
        return [{"case_id": r["case_id"], "variant": r["variant"], "origin": r["origin"],
                 "disease": list(r.get("disease") or []), "context": list(r.get("context") or [])}
                for r in json.loads(path.read_text())]
    spec = json.loads(SPEC.read_text())
    return [{"case_id": c["case_id"], **{k: c["requests"][form][k] for k in ("variant", "origin", "disease", "context")}}
            for c in spec["cases"]]


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()


def command(request: dict, folder: Path, mode: str, articles: int | None = None,
            critic: bool = False, judge: bool = False, loop: dict | None = None,
            profile: str | None = None, skip_unread: bool = False) -> list[str]:
    cmd = ["v2m", "v9", "fill", "--variant", request["variant"], "--origin", request["origin"], "--mode", mode,
           "--out", str(folder)]
    if profile:
        cmd += ["--profile", profile]
    if skip_unread:
        cmd += ["--skip-unread"]
    for flag in ("disease", "context"):
        for value in request[flag]:
            cmd += [f"--{flag}", value]
    if articles is not None:
        cmd += ["--read", "--max-articles", str(articles)]
    if critic:
        cmd += ["--critic"]
    if judge:
        cmd += ["--judge"]
    if loop:
        cmd += ["--loop", loop["planner"]]
        for flag in ("rounds", "articles"):
            if loop.get(flag) is not None:
                cmd += [f"--loop-{flag}", str(loop[flag])]
        if loop.get("dry"):
            cmd += ["--loop-dry"]
    return cmd


def cost_of(folder: Path) -> tuple[float, int]:
    """(dollars, model calls) a finished case's metrics.json records; zero for a case that called no model."""
    try:
        metrics = json.loads((folder / "metrics.json").read_text())
    except (OSError, ValueError):
        return 0.0, 0
    engine = metrics.get("engine") or {}
    model = metrics.get("model") or {}
    return (float(engine.get("cost_usd") or model.get("cost_usd") or 0.0),
            int(engine.get("model_calls") or model.get("calls") or 0))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", required=True, help="the suite's folder, under the repository")
    parser.add_argument("--form", choices=["main", "supplied_disease"], default="main",
                        help="main gives the fill the variant alone; supplied_disease adds the disease")
    parser.add_argument("--mode", choices=["live", "cache-only"], default="live",
                        help="live: saved responses first, then the network; cache-only: saved responses only")
    parser.add_argument("--read", action="store_true",
                        help="also read the articles that name the variant: one model call per article (paid)")
    parser.add_argument("--requests", default=None,
                        help="a JSON list of requests to run instead of the gold specification's cases")
    parser.add_argument("--max-articles", type=int, default=30,
                        help="with --read: articles per case (default 30: every article the searches list)")
    parser.add_argument("--critic", action="store_true",
                        help="with --read: a second model checks each experiment the reader filed (paid)")
    parser.add_argument("--judge", action="store_true",
                        help="with --read: the second model reads a tie for first (paid, at most two calls a case)")
    parser.add_argument("--loop", choices=["model", "code"], default=None,
                        help="with --read: go back for articles after the first reading (model: a planner model "
                             "picks from the menu, paid; code: the menu in its own order)")
    parser.add_argument("--loop-rounds", type=int, default=None, help="with --loop: rounds per case (default 3)")
    parser.add_argument("--loop-articles", type=int, default=None,
                        help="with --loop: new articles read per round (default 10)")
    parser.add_argument("--loop-dry", action="store_true",
                        help="with --loop: plan the first round and run its searches; read nothing, pay nothing")
    parser.add_argument("--skip-unread", action="store_true",
                        help="with --read in cache-only mode: go on past an article whose reading is not saved")
    parser.add_argument("--profile", default=None,
                        help="the config profile every case runs with (default: the config's default profile)")
    parser.add_argument("--budget-usd", type=float, default=None,
                        help="with --read (required): stop before a case once the suite has cost this much")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    out = (ROOT / args.out).resolve()
    source = (ROOT / args.requests).resolve() if args.requests else None
    todo = requests(args.form, source)
    if args.critic and not args.read:
        print("refused: --critic checks what the reader files, so it needs --read", file=sys.stderr)
        return 2
    if args.judge and not args.read:
        print("refused: --judge reads the experiments the reader files, so it needs --read", file=sys.stderr)
        return 2
    if (args.loop or args.loop_dry or args.loop_rounds or args.loop_articles) and not (args.read and args.loop):
        print("refused: the loop goes back for articles after the first reading, so it needs --read and --loop",
              file=sys.stderr)
        return 2
    arm = ("fill_with_reader_and_critic" if args.critic else "fill_with_reader") if args.read else "code_only_fill"
    arm += "_and_judge" if args.judge else ""
    loop = ({"planner": args.loop, "rounds": args.loop_rounds, "articles": args.loop_articles,
             "dry": args.loop_dry} if args.loop else None)
    if loop:
        arm += "_loop_dry" if args.loop_dry else f"_loop_{args.loop}"
    articles = args.max_articles if args.read else None
    if args.dry_run:
        for r in todo:
            print(" ".join(command(r, out / r["case_id"], args.mode, articles, args.critic, args.judge, loop,
                                   args.profile, args.skip_unread)))
        # with the loop: its rounds' readings, and one planner call a round (none in a dry run of it)
        more = ((args.loop_rounds or 3) * ((args.loop_articles or 10) + (args.loop == "model"))
                if loop and not args.loop_dry else 0)
        print(f"{len(todo)} cases, form {args.form}, mode {args.mode}; " + (
            f"up to {articles + more} model calls per case, {len(todo) * (articles + more)} in all" if args.read else
            "no model is called"))
        return 0
    if args.read and args.mode == "live" and args.budget_usd is None and not args.loop_dry:
        print("refused: --read in live mode spends money; give --budget-usd", file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    record_path = out / "suite.json"
    record = json.loads(record_path.read_text()) if record_path.exists() else {
        "arm": arm, "commit": git("rev-parse", "HEAD"),
        "clean_tree": not git("status", "--porcelain", "--untracked-files=no"), "form": args.form,
        "mode": args.mode, "max_articles": articles, "budget_usd": args.budget_usd, "profile": args.profile,
        "requests": str(source.relative_to(ROOT)) if source else "eval/v9_gold_spec.json",
        "started": datetime.now().isoformat(timespec="seconds"), "cases": {}}
    if (record["form"], record["mode"], record.get("arm", "code_only_fill")) != (args.form, args.mode, arm):
        print(f"refused: {record_path} was started as {record.get('arm', 'code_only_fill')} with form "
              f"{record['form']} in {record['mode']} mode", file=sys.stderr)
        return 2
    for r in todo:
        folder = out / r["case_id"]
        if folder.exists():
            continue
        spent = sum(c.get("cost_usd", 0.0) for c in record["cases"].values())
        if args.budget_usd is not None and spent >= args.budget_usd:
            print(f"stopped before {r['case_id']}: ${spent:.4f} spent of the ${args.budget_usd:.2f} given", flush=True)
            break
        started = time.monotonic()
        done = subprocess.run(command(r, folder, args.mode, articles, args.critic, args.judge, loop, args.profile,
                                      args.skip_unread), cwd=ROOT, capture_output=True, text=True)
        (out / f"{r['case_id']}.log").write_text(done.stdout + done.stderr)
        cost, calls = cost_of(folder)
        record["cases"][r["case_id"]] = {"exit": done.returncode, "seconds": round(time.monotonic() - started, 1),
                                        "finished": (folder / "table.json").exists(), "cost_usd": cost,
                                        "model_calls": calls}
        record_path.write_text(json.dumps(record, indent=1))
        answer = next((line.strip() for line in done.stdout.splitlines() if line.strip().startswith("answer:")), "")
        print(f"{r['case_id']}: exit {done.returncode}, {record['cases'][r['case_id']]['seconds']:.0f} s, "
              f"{calls} model call(s), ${cost:.4f}. {answer}", flush=True)
    finished = sum(c["finished"] for c in record["cases"].values())
    calls = sum(c.get("model_calls", 0) for c in record["cases"].values())
    cost = sum(c.get("cost_usd", 0.0) for c in record["cases"].values())
    print(f"suite: {finished} of {len(todo)} cases have a table; {calls} model call(s), ${cost:.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
