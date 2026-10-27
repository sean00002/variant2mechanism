"""The run viewer (demo/run_viewer.html): the demo runs, round by round, in one self-contained page.

    uv run python scripts/make_viewer.py

Reads the reports copied into demo/runs/ (nothing is fetched). A masked run shows its evidence as the model saw it,
rsIDs replaced. The page has no <html> or <body> tags: the artifact host adds them.
"""

import json
from pathlib import Path

from variant2mechanism.config import REPO
from variant2mechanism.context.literature import mask_rsids

TEMPLATE = Path(__file__).with_name("viewer_template.html")
OUT = REPO / "demo" / "run_viewer.html"

# (report, tab label, kind, headline, one-sentence summary)
RUNS = [
    ("demo/runs/rs339331_luna_named/report.json", "Finds the right TF", "Prostate cancer, 6q22 · GPT-6 Luna",
     "The agent tests a TF its draft did not propose, and it holds up",
     "The screen drops HOXB13, because ENCODE assayed it only in other cell types, and lists HOXC13, whose strongest "
     "QBiC-SELEX model is HOXB13's. The draft proposes HOXC13 behind the null and AR. The critic questions that "
     "attribution; the planner checks HOXB13 itself and predicts that T binds more. QBiC-SELEX confirms it (own model, "
     "first of 997), and HOXB13 leads from round 1."),
    ("demo/runs/rs73706717_deepseek_masked/report.json", "Withdraws a false claim", "Near-miss control, 8q24 · DeepSeek",
     "Same enhancer and ChIP-seq peak as a famous SNP, no mechanism of its own",
     "rs73706717 sits in the rs6983267 enhancer, inside the same TCF7L2 peak in HCT116, and the draft ranks TCF7L2 "
     "first. Before each call the agent predicts the result: no colon eQTL, no NFIC peak in HCT116, only a mapped "
     "TCF7L2 model with a weak site. All three come back as predicted, and the null moves to first. The model never "
     "saw the rsID."),
]
FINDINGS = [
    "Critique as a filter: across 187 one-round runs, revision withdrew 7 false claims at the control variants and "
    "introduced none. At true cases it fixed 11 top answers and broke 15, mostly by falling back to the null.",
    "The domain tool helps when the model cannot recall the answer: with rsIDs hidden, adding QBiC-SELEX lowered "
    "Luna's p(null) more at the 9 true cases than at the 6 controls in 50 of 54 pairs (p = 0.002). With rsIDs shown "
    "it never did, for any model.",
    "On its own, QBiC-SELEX ranks the published TF first of 1,109 TFs at both TERT promoter mutations and at rs339331.",
    "More rounds did not beat one. Each round looked again for a ChIP-seq peak in the matching cell type, mostly found "
    "none because ENCODE never ran that experiment, and moved probability to the null. Treating a missing experiment "
    "as no evidence, and stopping once the answer holds, stopped that erosion and cut the cost back to near one "
    "round's, but did not raise the scores. These two runs were made before that fix.",
]
FOOTNOTE = ("Seed 0. 15 cases: 9 with a published TF mechanism, 3 random and 3 near-miss controls. Models through "
            "OpenRouter. The full comparison is eval/screen_v3_and_luna.md.")


def slim(report: dict) -> dict:
    mask = mask_rsids if report["mode"] == "masked" else (lambda s: s)
    rounds = report.get("rounds", [])
    return {
        "id": report["case_id"], "variant": report["variant"], "key": report["variant_key"],
        "disease": report["disease"], "context": report["expression_context"], "mode": report["mode"],
        "models": report["models"], "cost": report["cost_usd"], "seconds": report["seconds"],
        "calls": report["model_calls"], "stop": report.get("stop_reason") or "",
        "versions": [{"label": "Draft", "chains": report["chains_v0"], "grades": report["grades_v0"]}]
        + [{"label": f"Round {r['round']}", "chains": r["chains"], "grades": r["grades"],
            "changed": r["grades_changed"]} for r in rounds],
        "rounds": rounds,
        "skipped": [c for c in report["investigate_calls"] if c["round"] > len(rounds)],
        "final": [{k: c[k] for k in ("id", "title", "tf", "is_null", "allele_binding_more", "probability", "links")}
                  for c in report["chains"]],
        "next_experiment": report["next_experiment"],
        "evidence": {e["id"]: {"tool": e["tool"], "source": e["source"], "url": mask(e["url"] or ""), "ok": e["ok"],
                               "summary": mask(e["summary"])[:1500]} for e in report["evidence"]},
    }


def main():
    runs = []
    for path, tab, kind, headline, summary in RUNS:
        r = slim(json.loads((REPO / path).read_text()))
        runs.append(r | {"tab": tab, "kind": kind, "headline": headline, "summary": summary})
    data = json.dumps({"runs": runs, "findings": FINDINGS, "footnote": FOOTNOTE}, separators=(",", ":"))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(TEMPLATE.read_text().replace("__DATA__", data.replace("</", "<\\/")))
    print(f"wrote {OUT.relative_to(REPO)} ({OUT.stat().st_size // 1024} KB, {len(runs)} runs)")


if __name__ == "__main__":
    main()
