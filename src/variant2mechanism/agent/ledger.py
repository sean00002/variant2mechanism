"""The evidence ledger: one SQLite file per run (spec 2, section 5).

Stages change it only through the functions below, and every write leaves an `events` row. Evidence IDs are E01,
E02, ... in the order code adds them; gather adds its results in the fixed tool order, so the same case always
gives the same prompt. Literature quotes are their own rows, E06a, E06b, ... under their search.
"""

import json
import sqlite3
import string
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from pydantic import BaseModel

SCHEMA = """
CREATE TABLE IF NOT EXISTS evidence(id TEXT PRIMARY KEY, seq INTEGER, stage TEXT, tool TEXT, args TEXT, source TEXT,
  url TEXT, retrieved_utc TEXT, kind TEXT, summary TEXT, full_path TEXT, quote TEXT, pmid TEXT, parent TEXT, ok INTEGER);
CREATE TABLE IF NOT EXISTS chains(version INTEGER, hypothesis_id TEXT, rank INTEGER, data TEXT,
  PRIMARY KEY(version, hypothesis_id));
CREATE TABLE IF NOT EXISTS grades(version INTEGER, grader TEXT, hypothesis_id TEXT, step TEXT, status TEXT,
  reason TEXT, PRIMARY KEY(version, grader, hypothesis_id, step));
CREATE TABLE IF NOT EXISTS checks(idx INTEGER PRIMARY KEY, tool TEXT, args_json TEXT, resolves TEXT, why TEXT,
  kept INTEGER, note TEXT);
CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT, time TEXT, stage TEXT, action TEXT,
  detail TEXT);
"""


@dataclass
class Evidence:
    id: str
    stage: str
    tool: str
    args: dict
    source: str
    url: str
    retrieved_utc: str | None
    kind: str
    summary: str
    full_path: str | None = None
    quote: str | None = None
    pmid: str | None = None
    parent: str | None = None
    ok: bool = True
    extra: dict = field(default_factory=dict)

    def prompt_line(self) -> str:
        """How the model sees it: id, kind, source, summary. No times, run ids or paths."""
        if self.quote is not None:
            return f'{self.id} [literature quote] PMID {self.pmid}: "{self.quote}"'
        return f"{self.id} [{self.kind}] {self.source}:\n{self.summary}"


class Ledger:
    def __init__(self, run_dir: Path):
        self.dir = Path(run_dir)
        self.dir.mkdir(parents=True, exist_ok=True)
        (self.dir / "tool_outputs").mkdir(exist_ok=True)
        self.path = self.dir / "ledger.sqlite"
        self.con = sqlite3.connect(self.path, check_same_thread=False)
        self.con.executescript(SCHEMA)
        self._n = self.con.execute("SELECT COALESCE(MAX(seq), 0) FROM evidence WHERE parent IS NULL").fetchone()[0]

    def _event(self, stage: str, action: str, detail: Any) -> None:
        self.con.execute("INSERT INTO events(time, stage, action, detail) VALUES (?,?,?,?)",
                         [datetime.now(UTC).isoformat(timespec="seconds"), stage, action,
                          json.dumps(detail, default=str)[:4000]])

    # -- evidence --------------------------------------------------------------------------------------------

    def add_evidence(self, stage: str, result, full: Any = None) -> Evidence:
        """Add one tool result (a ToolResult) as the next E-number; its full output goes to tool_outputs/."""
        self._n += 1
        eid = f"E{self._n:02d}"
        path = self.dir / "tool_outputs" / f"{eid}_{result.tool}.json"
        path.write_text(json.dumps(full if full is not None else result.full, indent=1, default=str))
        ev = Evidence(eid, stage, result.tool, result.args, result.source, result.url, result.retrieved_utc,
                      result.kind, result.summary, str(path.relative_to(self.dir)), ok=result.ok)
        with self.con:
            self._insert(ev, self._n)
            self._event(stage, "add_evidence", {"id": eid, "tool": ev.tool, "ok": ev.ok})
        return ev

    def add_quote(self, stage: str, parent: Evidence, pmid: str, sentence: str, url: str) -> Evidence:
        n = self.con.execute("SELECT COUNT(*) FROM evidence WHERE parent=?", [parent.id]).fetchone()[0]
        eid = f"{parent.id}{string.ascii_lowercase[n]}"
        ev = Evidence(eid, stage, parent.tool, {"pmid": pmid}, f"Europe PMC abstract, PMID {pmid}", url,
                      parent.retrieved_utc, "literature", sentence, parent.full_path, quote=sentence, pmid=pmid,
                      parent=parent.id)
        with self.con:
            self._insert(ev, None)
            self._event(stage, "add_quote", {"id": eid, "pmid": pmid})
        return ev

    def _insert(self, ev: Evidence, seq: int | None) -> None:
        self.con.execute("INSERT INTO evidence VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", [
            ev.id, seq, ev.stage, ev.tool, json.dumps(ev.args, default=str), ev.source, ev.url, ev.retrieved_utc,
            ev.kind, ev.summary, ev.full_path, ev.quote, ev.pmid, ev.parent, int(ev.ok)])

    def evidence(self) -> list[Evidence]:
        rows = self.con.execute("SELECT id, stage, tool, args, source, url, retrieved_utc, kind, summary, full_path, "
                                "quote, pmid, parent, ok FROM evidence").fetchall()
        evs = [Evidence(r[0], r[1], r[2], json.loads(r[3]), r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12],
                        bool(r[13])) for r in rows]
        return sorted(evs, key=_evidence_order)

    def get(self, eid: str) -> Evidence | None:
        return next((e for e in self.evidence() if e.id == eid), None)

    # -- chains, grades, checks ------------------------------------------------------------------------------

    def add_chains(self, stage: str, version: int, hyps: list[BaseModel], ranks: dict[str, int] | None = None):
        with self.con:
            for h in hyps:
                self.con.execute("INSERT OR REPLACE INTO chains VALUES (?,?,?,?)",
                                 [version, h.id, (ranks or {}).get(h.id), h.model_dump_json()])
            self._event(stage, "add_chains", {"version": version, "ids": [h.id for h in hyps]})

    def add_grades(self, stage: str, version: int, grader: str, grades: list[BaseModel]):
        with self.con:
            for g in grades:
                self.con.execute("INSERT OR REPLACE INTO grades VALUES (?,?,?,?,?,?)",
                                 [version, grader, g.hypothesis_id, g.step, g.status, g.reason])
            self._event(stage, "add_grades", {"version": version, "grader": grader, "n": len(grades)})

    def add_checks(self, stage: str, checks: list[dict]):
        with self.con:
            for i, c in enumerate(checks):
                self.con.execute("INSERT OR REPLACE INTO checks VALUES (?,?,?,?,?,?,?)",
                                 [i, c["tool"], c["args_json"], c["resolves"], c["why"], int(c["kept"]),
                                  c.get("note")])
            self._event(stage, "add_checks", {"n": len(checks), "kept": sum(bool(c["kept"]) for c in checks)})

    def log(self, stage: str, action: str, detail: Any) -> None:
        with self.con:
            self._event(stage, action, detail)

    def events(self) -> list[tuple]:
        return self.con.execute("SELECT stage, action, detail FROM events ORDER BY seq").fetchall()

    def close(self):
        self.con.close()


def _evidence_order(e: Evidence):
    base = e.parent or e.id
    return (int(base[1:]), e.id)


def render_evidence(evidence: list[Evidence], mask=None) -> str:
    lines = [e.prompt_line() for e in evidence]
    text = "\n\n".join(lines)
    return mask(text) if mask else text
