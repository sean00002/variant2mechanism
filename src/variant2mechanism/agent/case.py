"""The case a run works on, its header (spec 2, section 8.1), masking, and the shared run state."""

import re
from dataclasses import dataclass, field
from pathlib import Path

from ..config import Config, load_config
from ..context.base import Case
from ..context.literature import mask_rsids
from ..qbic.variants import Variant
from .ledger import Ledger, render_evidence

PROMPTS = Path(__file__).parent / "prompts"
BRACKETS = re.compile(r"\s*\([^()]*\)")
CANCER_WORDS = ("cancer", "carcinoma", "glioblastoma", "melanoma", "neuroblastoma", "leukaemia", "leukemia",
                "lymphoma", "tumour", "tumor", "sarcoma", "bladder")


def prompt(name: str) -> str:
    return (PROMPTS / f"{name}.txt").read_text().strip()


@dataclass
class CaseSpec:
    case_id: str
    label: str                 # as given: rsID or a name such as "TERT promoter C228T"
    variant: Variant
    origin: str
    disease: str
    expression_context: str | None
    rsid: str | None

    @property
    def is_cancer(self) -> bool:
        return self.origin == "somatic" or any(w in self.disease.lower() for w in CANCER_WORDS)

    def header(self, masked: bool) -> str:
        v = self.variant
        lines = ["Case"]
        if not masked:
            lines.append(f"Variant: {self.label}")
        lines += [f"GRCh38 position: {v.chrom}:{v.pos} (1-based, plus strand)",
                  f"Alleles: ref {v.ref}, alt {v.alt}",
                  f"Origin: {self.origin}",
                  f"Disease or trait: {BRACKETS.sub('', self.disease).strip() if masked else self.disease}",
                  f"Expression context: {self.expression_context or 'none'}"]
        return "\n".join(lines)


def load_gold_case(case_id: str, cfg: Config | None = None) -> CaseSpec:
    """A case from the gold set, built from PROMPT_COLUMNS only: labels, source and notes never reach a prompt."""
    from ..evaluation.gold import PROMPT_COLUMNS, load_gold
    cfg = cfg or load_config()
    gold = load_gold(cfg)
    rows = gold[gold.case_id == case_id]
    if rows.empty:
        raise KeyError(f"{case_id} is not in {cfg['eval']['gold_set']}")
    r = {k: str(rows.iloc[0][k]) for k in PROMPT_COLUMNS}
    ctx = r["expression_context"].strip()
    ctx = None if not ctx or ctx.lower().startswith("none") else ctx
    rsid = r["variant"] if r["variant"].startswith("rs") else None
    return CaseSpec(case_id, r["variant"], Variant.make(r["chrom"], r["pos_grch38"], r["ref"], r["alt"]), r["origin"],
                    r["disease_or_trait"], ctx, rsid)


@dataclass
class RunState:
    spec: CaseSpec
    config: str                      # single, no_qbic, full
    masked: bool
    run_dir: Path
    ledger: Ledger
    llm: object
    tool_case: Case                  # what context tools bind
    qbic: object | None = None       # QbicTools, full only
    v0: list = field(default_factory=list)
    grades0: list = field(default_factory=list)
    problems: list = field(default_factory=list)     # the latest critic's: the critique, then each regrade
    checks: list = field(default_factory=list)       # likewise
    checks0: list = field(default_factory=list)      # the critique's checks
    revised: object | None = None
    grades1: list = field(default_factory=list)      # the latest regrade
    flags: list = field(default_factory=list)
    investigate_calls: list = field(default_factory=list)   # every planned call of every round, run or not
    rounds: list = field(default_factory=list)       # one record per refinement round
    stop_reason: str = ""
    screen: dict | None = None
    occupancy: object | None = None  # context/occupancy.Occupancy, from gather (no_qbic and full)

    def mask(self, text: str) -> str:
        return mask_rsids(text) if self.masked else text

    def current_chains(self) -> list:
        return self.revised.hypotheses if self.revised is not None else self.v0

    def current_grades(self) -> list:
        return self.grades1 if self.revised is not None else self.grades0

    def user_message(self, instruction: str, with_evidence: bool = True) -> list[dict]:
        """Header and evidence first, the stage's instruction after: providers cache a repeated prefix themselves."""
        first = self.spec.header(self.masked)
        if with_evidence:
            first += "\n\nEvidence (cite these IDs):\n\n" + render_evidence(self.ledger.evidence(), self.mask)
        return [{"role": "user", "content": f"{first}\n\n{instruction}"}]

    def flag(self, kind: str, detail: str) -> None:
        self.flags.append({"flag": kind, "detail": detail})
        self.ledger.log("flags", kind, detail)
