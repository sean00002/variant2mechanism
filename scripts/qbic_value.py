"""Does QBiC-SELEX help? (eval/screen_v3_and_luna.md, section 7). Seed 0; counts, not percentages.

    uv run python scripts/qbic_value.py

Tool level, with no model in the loop: the gold TF's place among every TF QBiC-SELEX covers (each TF's best |z| over
its own and mapped models) and among the TFs with an ENCODE peak over the variant (the screen v3 order, |z| alone,
expression alone); the famous TF at each near-miss control against its causal neighbour; models passing the gate.
Agent level: `full` against `no_qbic`, paired by case, for every run set, named and masked.
"""

import json
import math
from functools import partial
from itertools import combinations, product

from variant2mechanism.config import REPO, load_config
from variant2mechanism.context.base import Case
from variant2mechanism.context.http import Http
from variant2mechanism.context.occupancy import NOT_SEQUENCE_SPECIFIC, fetch
from variant2mechanism.evaluation import metrics
from variant2mechanism.evaluation.gold import load_gold, scoring_tf
from variant2mechanism.qbic.registry import get_registry
from variant2mechanism.qbic.screen import ScreenV2Settings, screen_v2
from variant2mechanism.qbic.tools import QbicTools
from variant2mechanism.qbic.variants import Variant

# (name, mode, no_qbic folder, full folder). DeepSeek's named no_qbic runs are its v2 runs: the screen enters only full.
RUN_SETS = [
    ("Claude v1", "named", "runs/eval", "runs/eval"),
    ("DeepSeek v1", "named", "runs/eval_deepseek", "runs/eval_deepseek"),
    ("DeepSeek v2", "named", "runs/eval_v2_deepseek", "runs/eval_v2_deepseek"),
    ("DeepSeek v3", "named", "runs/eval_v2_deepseek", "runs/eval_v3_deepseek"),
    ("Luna v3", "named", "runs/eval_v3_luna", "runs/eval_v3_luna"),
    ("DeepSeek v3", "masked", "runs/eval_v3_deepseek", "runs/eval_v3_deepseek"),
    ("Luna v3", "masked", "runs/eval_v3_luna", "runs/eval_v3_luna"),
]
NEAR_MISS = {"rs73706717": ("rs6983267", "TCF7L2"), "rs34768248": ("tert_c228t", "GABPA"),
             "rs56007086": ("rs4784227", "FOXA1")}   # near-miss control: (its causal neighbour, the famous TF)
CLASS = {"bound_here": "bound here", "bound_elsewhere": "bound elsewhere", "unbound_assayed_here": "unbound, assayed here",
         "unbound_assayed_elsewhere": "unbound, assayed elsewhere", "not_assayed": "not assayed"}


def is_control(r) -> bool:
    return r["label_class"].startswith("control")


def is_tf_case(r) -> bool:
    return not is_control(r)


def is_random(r) -> bool:
    return r["label_class"] == "control_random"


def is_near_miss(r) -> bool:
    return r["label_class"] == "control_near_miss"


def fisher(ps: list[float]) -> float:
    """Fisher's combined probability for independent p-values (chi-square with 2k df, closed form)."""
    h = -sum(math.log(p) for p in ps)
    return math.exp(-h) * sum(h ** i / math.factorial(i) for i in range(len(ps)))


def auc(ctl: list[float], tf: list[float]) -> float:
    """P(a control's p(null) exceeds a TF case's), ties half: how well p(null) separates controls from TF cases."""
    return sum((c > t) + 0.5 * (c == t) for c, t in product(ctl, tf)) / (len(ctl) * len(tf))


def same_family(reg, a: str, b: str) -> bool:
    if a == b:
        return True
    if a.startswith("unresolved:"):
        return False
    return bool({g["id"] for g in reg.groups_of_tf(a)} & {g["id"] for g in reg.groups_of_tf(b)})


# -- tool level --------------------------------------------------------------------------------------------------


def best_z(scores, reg) -> dict[str, tuple[float, str]]:
    """Per sequence-specific TF: (best |z| over its own and mapped models, that model)."""
    ok = scores[(scores.status == "ok") & scores.z.notna()]
    z = dict(zip(ok.model, ok.z.abs(), strict=True))
    out = {}
    for tf in (set(reg.own_model) | set(reg.mapped_models)) - NOT_SEQUENCE_SPECIFIC:
        ms = ([reg.own_model[tf]] if tf in reg.own_model else []) + reg.mapped_models.get(tf, [])
        vals = [(z[m], m) for m in ms if m in z]
        if vals:
            out[tf] = max(vals)
    return out


def screens(rows: dict, reg, cfg) -> tuple[QbicTools, dict]:
    """Screen v3 per case with every occupied TF (not only the 10 shown), from the caches; no network."""
    t, sc = QbicTools(), cfg["screen"]
    settings = ScreenV2Settings(alpha=float(sc["alpha"]), min_tpm=float(sc["min_tpm"]),
                                strong_site_pct=float(sc["strong_site_pct"]), max_occupied=10_000)
    http = Http(cfg.path("tools", "http_cache"), offline=True)
    out = {}
    for cid, r in rows.items():
        v = Variant.make(r["chrom"], int(r["pos_grch38"]), r["ref"], r["alt"])
        scores = t.cache.scores(v.key(), stats=True)
        o, err = fetch(Case(v, r["disease_or_trait"], expression_context=r["expression_context"], http=http), reg)
        if err:
            raise SystemExit(f"{cid}: occupancy is not in the HTTP cache ({err})")
        s = screen_v2(scores, reg, len(t.cache.models), t.expression, r["expression_context"], o,
                      site=partial(t.site, key=v.key()), settings=settings, exclude=NOT_SEQUENCE_SPECIFIC)
        out[cid] = {"key": v.key(), "occ": o, "screen": s, "best": best_z(scores, reg)}
    return t, out


def rank_of(best: dict, tf: str) -> int:
    return 1 + sum(1 for v in best.values() if v[0] > best[tf][0])


def tool_level(rows: dict, reg) -> list[str]:
    cfg = load_config()
    strong = float(cfg["screen"]["strong_site_pct"])
    t, sc = screens(rows, reg, cfg)
    out = ["### Tool level: QBiC-SELEX with no model", "",
           "| Case | Gold TF | QBiC-SELEX alone: rank among all TFs | ENCODE class | TFs in that class "
           "| Screen v3 rank | Rank by \\|z\\| alone | Rank by expression alone |",
           "|---|---|---|---|---|---|---|---|"]
    ps = {"screen v3": [], "|z| alone": [], "expression alone": []}
    for cid, r in rows.items():
        if is_control(r):
            continue
        g, s = scoring_tf(r), sc[cid]
        if g not in s["best"]:
            out.append(f"| {cid} | {g} | no QBiC-SELEX model | | | | | |")
            continue
        alone = f"{rank_of(s['best'], g)} of {len(s['best'])} (\\|z\\| {s['best'][g][0]:.1f})"
        hit = next((x for x in s["screen"]["occupied"] if x["tf"] == g), None)
        if hit is None:
            out.append(f"| {cid} | {g} | {alone} | {CLASS[s['occ'].tf_class(g)]}: not listed | | | | |")
            continue
        cls = [x for x in s["screen"]["occupied"] if x["occupancy"] == hit["occupancy"]]
        ranks = {"screen v3": 1 + cls.index(hit),
                 "|z| alone": 1 + sum(1 for x in cls if abs(x["z"]) > abs(hit["z"])),
                 "expression alone": 1 + sum(1 for x in cls if (x["tpm"] or 0) > (hit["tpm"] or 0))}
        for k, v in ranks.items():
            ps[k].append(v / len(cls))
        out.append(f"| {cid} | {g} | {alone} | {CLASS[hit['occupancy']]} | {len(cls)} "
                   f"| {ranks['screen v3']} | {ranks['|z| alone']} | {ranks['expression alone']} |")
    combined = "; ".join(f"{k} {fisher(v):.3f}" for k, v in ps.items())
    out += ["", f"Chance of ranks this good in all {len(ps['screen v3'])} listed cases under a random order "
            f"(Fisher's method): {combined}.", ""]

    out += ["| Near-miss control | TF | Variant | ENCODE class | Best \\|z\\| (model) | Rank among all TFs "
            "| Better allele's site | Strong site |", "|---|---|---|---|---|---|---|---|"]
    for near, (causal, tf) in NEAR_MISS.items():
        for cid in (causal, near):
            s = sc[cid]
            zv, model = s["best"][tf]
            st = t.site(model, s["key"])
            better = max(st["ref_percentile"], st["alt_percentile"])
            out.append(f"| {near} | {tf} | {cid} | {CLASS[s['occ'].tf_class(tf)]} | {zv:.1f} ({model}) "
                       f"| {rank_of(s['best'], tf)} of {len(s['best'])} | {better:.1f}th "
                       f"| {'yes' if better >= strong else 'no'} |")
    n_models = sc[next(iter(rows))]["screen"]["n_models_scored"]
    gate = "; ".join(f"{cid} {sc[cid]['screen']['n_pass']}" for cid in rows)
    return out + ["", f"Models passing the Bonferroni gate, of {n_models}: {gate}.", ""]


# -- agent level -------------------------------------------------------------------------------------------------


def facts(folder: str, config: str, mode: str, cid: str, r: dict, reg) -> dict | None:
    p = REPO / folder / config / mode / "0" / cid / "report.json"
    if not p.exists():
        return None
    chains = sorted(json.loads(p.read_text())["chains"], key=lambda c: c["rank"])
    marg = metrics.tf_marginals(chains, reg)
    top_tf = max(marg, key=marg.get) if marg else None
    f = {"chains": chains, "p_null": sum(c["probability"] for c in chains if c["is_null"]),
         "null_first": bool(chains) and chains[0]["is_null"]}
    if is_tf_case(r):
        g = metrics.resolves_to(reg, scoring_tf(r)) or scoring_tf(r)
        naming = [not c["is_null"] and metrics.resolves_to(reg, c["tf"]) == g for c in chains]
        f |= {"gold": g, "p_gold": marg.get(g, 0.0), "gold_top": top_tf == g,
              "family_top": bool(top_tf) and same_family(reg, top_tf, g),
              "first": any(naming[:1]), "top3": any(naming[:3])}
    elif cid in NEAR_MISS:
        f["p_famous"] = marg.get(NEAR_MISS[cid][1], 0.0)
    return f


def paired(rows: dict, reg, no_qbic: str, full: str, mode: str) -> dict:
    """case_id -> (no_qbic facts, full facts), for the cases both configurations ran."""
    out = {}
    for cid, r in rows.items():
        a, b = facts(no_qbic, "no_qbic", mode, cid, r, reg), facts(full, "full", mode, cid, r, reg)
        if a is not None and b is not None:
            out[cid] = (a, b)
    return out


def total(key):
    return lambda xs: str(sum(1 for x in xs if x[key]))


def mean(key):
    return lambda xs: f"{sum(x[key] for x in xs) / len(xs):.2f}"


METRICS = [
    ("Gold TF ranked first", is_tf_case, total("first")),
    ("Gold TF in the top three", is_tf_case, total("top3")),
    ("Gold TF is the top TF, null ignored", is_tf_case, total("gold_top")),
    ("Top TF in the gold TF's motif family, null ignored", is_tf_case, total("family_top")),
    ("TF cases: null ranked first", is_tf_case, total("null_first")),
    ("TF cases: mean p(gold TF)", is_tf_case, mean("p_gold")),
    ("Random controls: mean p(null)", is_random, mean("p_null")),
    ("Near-miss controls: mean p(null)", is_near_miss, mean("p_null")),
    ("Near-miss controls: mean p(the famous neighbour's TF)", is_near_miss, mean("p_famous")),
]


def separation(p: dict, rows: dict, i: int) -> str:
    ctl = [x[i]["p_null"] for cid, x in p.items() if is_control(rows[cid])]
    tf = [x[i]["p_null"] for cid, x in p.items() if is_tf_case(rows[cid])]
    return f"{auc(ctl, tf):.2f}" if ctl and tf else "none"


def lowered_more_at_tf_cases(p: dict, rows: dict) -> str:
    """Did adding QBiC-SELEX lower p(null) more at the TF cases than at the controls? The share of (TF case, control)
    pairs where it did (ties half), and a one-sided permutation p over every way of labelling the cases."""
    d = {cid: b["p_null"] - a["p_null"] for cid, (a, b) in p.items()}
    tf = [v for cid, v in d.items() if is_tf_case(rows[cid])]
    ctl = [v for cid, v in d.items() if is_control(rows[cid])]
    if not tf or not ctl:
        return "none"

    def pairs(t, c):
        return sum((x < y) + 0.5 * (x == y) for x, y in product(t, c))

    vals, obs = list(d.values()), pairs(tf, ctl)
    splits = [pairs([vals[i] for i in idx], [vals[i] for i in range(len(vals)) if i not in idx])
              for idx in combinations(range(len(vals)), len(tf))]
    p_value = sum(1 for s in splits if s >= obs - 1e-9) / len(splits)
    return f"{obs / (len(tf) * len(ctl)):.2f} (p {p_value:.3f})"


def agent_table(rows: dict, reg, mode: str) -> list[str]:
    sets = [(n, paired(rows, reg, a, b, mode)) for n, m, a, b in RUN_SETS if m == mode]
    sets = [(n, p) for n, p in sets if p]
    if not sets:
        return [f"No {mode} runs yet.", ""]
    out = [f"| `no_qbic` → `full`, {mode} | " + " | ".join(n for n, _ in sets) + " |", "|---|" + "---|" * len(sets),
           "| TF cases compared | " + " | ".join(str(sum(1 for c in p if is_tf_case(rows[c]))) for _, p in sets) + " |"]
    for name, keep, fn in METRICS:
        cells = []
        for _, p in sets:
            sub = [x for cid, x in p.items() if keep(rows[cid])]
            cells.append(f"{fn([a for a, _ in sub])} → {fn([b for _, b in sub])}" if sub else "none")
        out.append(f"| {name} | " + " | ".join(cells) + " |")
    out.append("| Separation: AUC of p(null), controls against TF cases | "
               + " | ".join(f"{separation(p, rows, 0)} → {separation(p, rows, 1)}" for _, p in sets) + " |")
    moved = []
    for _, p in sets:
        d = [b["p_null"] - a["p_null"] for cid, (a, b) in p.items() if is_control(rows[cid])]
        moved.append(f"{sum(1 for x in d if x < -0.005)} / {sum(1 for x in d if x > 0.005)} of {len(d)}")
    out.append("| Controls where p(null) fell / rose with QBiC-SELEX | " + " | ".join(moved) + " |")
    out.append("| p(null) lowered more at TF cases than at controls: share of pairs (permutation p) | "
               + " | ".join(lowered_more_at_tf_cases(p, rows) for _, p in sets) + " |")
    return out + [""]


def top3(f: dict | None, reg) -> str:
    """The top three chains: TF, the allele said to bind more, probability; the gold TF in bold."""
    if f is None:
        return "not run"
    cs, gold = f["chains"], f.get("gold")
    parts = []
    for c in cs[:3]:
        if c["is_null"]:
            parts.append(f"null {c['probability']:.2f}")
            continue
        name = f"**{c['tf']}**" if gold and metrics.resolves_to(reg, c["tf"]) == gold else c["tf"]
        parts.append(f"{name} {c.get('allele_binding_more') or '?'} {c['probability']:.2f}")
    text = "; ".join(parts)
    return text if any(c["is_null"] for c in cs[:3]) else f"{text} (null {f['p_null']:.2f})"


def per_case(rows: dict, reg, mode: str) -> list[str]:
    cols = [(f"{n} {c}", f, c) for n, m, a, b in RUN_SETS if m == mode for f, c in ((a, "no_qbic"), (b, "full"))]
    out = ["| Case | " + " | ".join(h for h, _, _ in cols) + " |", "|---|" + "---|" * len(cols)]
    for cid, r in rows.items():
        out.append(f"| {cid} | " + " | ".join(top3(facts(f, c, mode, cid, r, reg), reg) for _, f, c in cols) + " |")
    return out + [""]


def main():
    reg = get_registry()
    rows = {r["case_id"]: r for r in load_gold().to_dict("records")}
    lines = tool_level(rows, reg)
    for mode in ("named", "masked"):
        lines += [f"### Agent level, {mode}", ""] + agent_table(rows, reg, mode)
    lines += ["### Masked runs: the top three chains", ""] + per_case(rows, reg, "masked")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
