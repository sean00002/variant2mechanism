"""TF names, QBiC-SELEX coverage and CIS-BP groups (spec 1, part C).

Every gene is keyed by its current HGNC symbol. Table and Lambert symbols are mapped to it through the
Ensembl gene ID first, then by symbol; names with no HGNC match (such as AC138696.1) are kept as they are.
"""

import json
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import pandas as pd

from ..config import Config, load_config

PRIMARY = "primary"


@dataclass
class Registry:
    hgnc_by_ensembl: dict[str, str]
    hgnc_symbols: dict[str, str]                 # upper-case -> HGNC spelling
    prev_index: dict[str, set[str]]              # upper-case previous symbol -> current symbols
    alias_index: dict[str, set[str]]             # upper-case alias -> current symbols
    label_index: dict[str, set[str]]             # upper-case Table S1 label -> current symbols
    entrez_to_symbol: dict[str, str]
    ensembl_by_symbol: dict[str, str]
    lambert_tfs: set[str]                        # current symbols of the 1,639 Lambert TFs
    lambert_dbd: dict[str, str]
    model_tfs: dict[str, set[str]]               # primary model -> all mapped TFs (Table S5)
    own_model: dict[str, str]                    # TF -> its cognate primary model
    cognate_tf: dict[str, str]                   # primary model -> its cognate TF
    mapped_models: dict[str, list[str]]          # TF -> CIS-BP-mapped primary models (Table S6)
    tf_models_s6: dict[str, list[str]]           # TF -> every primary model in Table S6 (own and CIS-BP)
    quality: dict[str, dict]                     # primary model -> Table S3 metrics
    model_ids: list[str]                         # the 997 primary models, sorted
    _groups: dict | None = field(default=None, repr=False)

    # -- names ---------------------------------------------------------------------------------------------

    def canonical(self, symbol: str, ensembl: str | None = None) -> str:
        if ensembl and ensembl in self.hgnc_by_ensembl:
            return self.hgnc_by_ensembl[ensembl]
        return self.hgnc_symbols.get(symbol.upper(), symbol)

    def is_tf(self, symbol: str) -> bool:
        return symbol in self.lambert_tfs or symbol in self.own_model or symbol in self.tf_models_s6

    def resolve_tf(self, name: str) -> dict:
        """Resolve a TF name: HGNC symbol, then Table S1 label, then previous symbol, then alias."""
        key = name.strip().upper()
        notes: list[str] = []
        steps = [
            ("hgnc_symbol", {self.hgnc_symbols[key]} if key in self.hgnc_symbols else set()),
            ("qbic_label", self.label_index.get(key, set())),
            ("previous_symbol", self.prev_index.get(key, set())),
            ("alias", self.alias_index.get(key, set())),
        ]
        for via, found in steps:
            if not found:
                continue
            if via in ("previous_symbol", "alias"):
                tfs = {s for s in found if self.is_tf(s)}
                found = tfs or found      # prefer TFs; fall back to any gene with that name
            if len(found) > 1:
                cands = [{"symbol": s, "coverage": self.coverage(s)["status"]} for s in sorted(found)]
                return {"status": "ambiguous", "symbol": None, "candidates": cands, "via": via,
                        "notes": [f"{name} is a {via.replace('_', ' ')} of {len(found)} genes; name one by HGNC symbol."]}
            symbol = next(iter(found))
            if via == "hgnc_symbol":
                for other in sorted(self.prev_index.get(key, set()) - {symbol}):
                    if self.is_tf(other):
                        notes.append(f"{symbol} is also a former name of {other}.")
            elif symbol.upper() != key:
                notes.append(f"{name} resolved to {symbol} ({via.replace('_', ' ')}).")
            cands = [{"symbol": symbol, "coverage": self.coverage(symbol)["status"]}]
            return {"status": "ok", "symbol": symbol, "candidates": cands, "via": via, "notes": notes}
        return {"status": "unknown_name", "symbol": None, "candidates": [], "via": None,
                "notes": [f"No HGNC symbol, QBiC-SELEX label, previous symbol or alias matches {name}."]}

    # -- coverage ------------------------------------------------------------------------------------------

    def coverage(self, symbol: str) -> dict:
        own = self.own_model.get(symbol)
        mapped = self.mapped_models.get(symbol, [])
        status = "tf" if own else ("mapped" if mapped else "not_in_coverage")
        return {"status": status, "own_model": own, "mapped_models": list(mapped)}

    # -- groups --------------------------------------------------------------------------------------------

    def groups(self) -> dict:
        if self._groups is None:
            self._groups = load_groups(self)
        return self._groups

    def group_of_model(self, model_id: str) -> dict:
        g = self.groups()
        return g["groups"][g["model_to_group"][model_id]]

    def groups_of_tf(self, symbol: str) -> list[dict]:
        """Groups holding the TF's own or mapped models."""
        g = self.groups()
        ids = {g["model_to_group"][m] for m in self.tf_models_s6.get(symbol, []) if m in g["model_to_group"]}
        return [g["groups"][i] for i in sorted(ids)]


def _split(value) -> list[str]:
    return [x.strip() for x in str(value).split("|") if x.strip()] if isinstance(value, str) else []


def build_registry(cfg: Config) -> Registry:
    hgnc = pd.read_csv(cfg.path("data", "hgnc"), sep="\t", low_memory=False,
                       usecols=["symbol", "prev_symbol", "alias_symbol", "ensembl_gene_id", "entrez_id"])
    hgnc_by_ensembl = {e: s for s, e in zip(hgnc.symbol, hgnc.ensembl_gene_id, strict=True) if isinstance(e, str)}
    hgnc_symbols = {s.upper(): s for s in hgnc.symbol}
    prev_index: dict[str, set[str]] = defaultdict(set)
    alias_index: dict[str, set[str]] = defaultdict(set)
    for s, prev, alias in zip(hgnc.symbol, hgnc.prev_symbol, hgnc.alias_symbol, strict=True):
        for p in _split(prev):
            prev_index[p.upper()].add(s)
        for a in _split(alias):
            alias_index[a.upper()].add(s)
    entrez_to_symbol = {str(int(e)): s for s, e in zip(hgnc.symbol, hgnc.entrez_id, strict=True) if pd.notna(e)}
    ensembl_by_symbol = {s: e for e, s in hgnc_by_ensembl.items()}

    def canon(symbol: str, ensembl=None) -> str:
        if isinstance(ensembl, str) and ensembl in hgnc_by_ensembl:
            return hgnc_by_ensembl[ensembl]
        return hgnc_symbols.get(str(symbol).upper(), str(symbol))

    s1 = pd.read_csv(cfg.path("data", "table_s1"), usecols=["source_tf_label", "hgnc_symbol", "ensembl_gene_id"])
    label_index: dict[str, set[str]] = defaultdict(set)
    for lab, sym, ens in s1.drop_duplicates().itertuples(index=False):
        if isinstance(lab, str) and isinstance(sym, str):
            label_index[lab.upper()].add(canon(sym, ens))

    lam = pd.read_csv(cfg.path("data", "lambert"))
    lam = lam[lam["Is TF?"] == "Yes"]
    lambert_dbd = {canon(s, e): d for s, e, d in zip(lam["HGNC symbol"], lam["Ensembl ID"], lam["DBD"], strict=True)}
    lambert_tfs = set(lambert_dbd)

    s5 = pd.read_csv(cfg.path("data", "table_s5"))
    s5 = s5[s5.model_collection == PRIMARY]
    model_tfs: dict[str, set[str]] = defaultdict(set)
    own_model: dict[str, str] = {}
    cognate_tf: dict[str, str] = {}
    for m, sym, ens, kind in s5[["model_id", "mapped_tf_hgnc_symbol", "mapped_tf_ensembl_gene_id",
                                 "mapping_type"]].itertuples(index=False):
        tf = canon(sym, ens)
        model_tfs[m].add(tf)
        if kind == "cognate":
            own_model[tf] = m
            cognate_tf[m] = tf

    s6 = pd.read_csv(cfg.path("data", "table_s6"))
    s6 = s6[s6.model_collection == PRIMARY]
    mapped_models: dict[str, list[str]] = defaultdict(list)
    tf_models_s6: dict[str, list[str]] = defaultdict(list)
    for sym, ens, m, kind in s6[["tf_hgnc_symbol", "ensembl_gene_id", "mapped_model_id",
                                 "mapping_type"]].itertuples(index=False):
        tf = canon(sym, ens)
        if m not in tf_models_s6[tf]:
            tf_models_s6[tf].append(m)
        if kind == "CIS-BP" and m not in mapped_models[tf]:
            mapped_models[tf].append(m)

    s3 = pd.read_csv(cfg.path("data", "table_s3"))
    quality = {r.model_id: {"cross_exp_pearsonr": round(float(r.cross_exp_pearsonr), 3),
                            "within_exp_pearsonr": round(float(r.within_exp_pearsonr), 3)}
               for r in s3.itertuples(index=False)}

    return Registry(
        hgnc_by_ensembl=hgnc_by_ensembl, hgnc_symbols=hgnc_symbols, prev_index=dict(prev_index),
        alias_index=dict(alias_index), label_index=dict(label_index), entrez_to_symbol=entrez_to_symbol,
        ensembl_by_symbol=ensembl_by_symbol, lambert_tfs=lambert_tfs, lambert_dbd=lambert_dbd,
        model_tfs=dict(model_tfs), own_model=own_model, cognate_tf=cognate_tf, mapped_models=dict(mapped_models),
        tf_models_s6=dict(tf_models_s6), quality=quality, model_ids=sorted(model_tfs),
    )


@lru_cache(maxsize=1)
def get_registry() -> Registry:
    return build_registry(load_config())


# -- groups --------------------------------------------------------------------------------------------------


def compute_groups(reg: Registry, jaccard: float = 0.5) -> dict:
    """Connected components of primary models whose TF sets have Jaccard index >= `jaccard`."""
    models = reg.model_ids
    parent = {m: m for m in models}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    by_tf: dict[str, list[str]] = defaultdict(list)
    for m in models:
        for tf in reg.model_tfs[m]:
            by_tf[tf].append(m)
    seen: set[tuple[str, str]] = set()
    for ms in by_tf.values():                  # only models sharing a TF can have a non-zero Jaccard index
        for i, a in enumerate(ms):
            for b in ms[i + 1:]:
                if (a, b) in seen:
                    continue
                seen.add((a, b))
                sa, sb = reg.model_tfs[a], reg.model_tfs[b]
                if len(sa & sb) / len(sa | sb) >= jaccard:
                    parent[find(a)] = find(b)

    comps: dict[str, list[str]] = defaultdict(list)
    for m in models:
        comps[find(m)].append(m)
    ordered = sorted((sorted(c) for c in comps.values()), key=lambda c: (-len(c), c[0]))

    groups, model_to_group = [], {}
    for i, members in enumerate(ordered):
        gid = f"G{i + 1:03d}"
        dbds = Counter(reg.lambert_dbd.get(reg.cognate_tf.get(m, ""), "Unknown") for m in members)
        dbd = dbds.most_common(1)[0][0]
        tfs = sorted({tf for tf, ms in reg.tf_models_s6.items() if set(ms) & set(members)})
        groups.append({"id": gid, "label": f"{dbd}, {len(members)} model{'s' if len(members) > 1 else ''}",
                       "dbd": dbd, "dbd_labels": dict(dbds), "models": members, "tfs": tfs})
        for m in members:
            model_to_group[m] = i
    sizes = [len(g["models"]) for g in groups]
    return {"settings": {"jaccard": jaccard, "collection": PRIMARY, "n_models": len(models)},
            "summary": {"n_groups": len(groups), "n_singletons": sizes.count(1), "largest": sorted(sizes)[-2:][::-1]},
            "groups": groups, "model_to_group": model_to_group}


def load_groups(reg: Registry, path: Path | None = None, rebuild: bool = False) -> dict:
    cfg = load_config()
    path = path or cfg.path("cache", "groups")
    jaccard = float(cfg["screen"]["jaccard"])
    if path.exists() and not rebuild:
        data = json.loads(path.read_text())
        if data["settings"]["jaccard"] == jaccard and data["settings"]["n_models"] == len(reg.model_ids):
            return data
    data = compute_groups(reg, jaccard)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=1))
    return data
