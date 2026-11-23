"""The family screen (v8, code): candidates are TF families, conclusions are single TFs.

A family is a registry group: QBiC-SELEX models that share mapped TFs (CIS-BP). A mapped model counts as each member's
own. With QBiC-SELEX (`full`), a family is a candidate when one of its models passes the Bonferroni gate and at least
one member is not known to be unexpressed; without it (`no_qbic`), when a member that is not known to be unexpressed
has ChIP-seq at the variant (grade 1 or 2) anywhere. Nothing is dropped for missing ChIP-seq.

Order: the best member's ChIP grade in the matched biosamples, then anywhere, then the family's best |z| (or, without
QBiC-SELEX, its highest expression). Site strength is shown, never used to order. Within a family, code names one
member: own ChIP grade in the matched biosamples, then expression, then own ChIP grade anywhere; the members that cannot
be ruled out are listed as paralogs.
"""

EXPRESSED, LOW, UNEXPRESSED, UNKNOWN = "expressed", "low in bulk tissue", "not expressed", "unknown"
STATE_ORDER = {EXPRESSED: 0, LOW: 1, UNKNOWN: 2, UNEXPRESSED: 3}


def expression_states(tfs: list[str], expression, ctx, min_tpm: float = 1.0) -> dict[str, dict]:
    """TPM and state per TF. A cell line or a DepMap subtype median below `min_tpm` is "not expressed"; GTEx bulk
    tissue below it is only "low" (a rare cell type can be diluted out); no context or no data is "unknown"."""
    if ctx is None or ctx.kind == "none":
        return {t: {"tpm": None, "state": UNKNOWN} for t in tfs}
    rows = expression.tf_expression(tfs, ctx)
    out = {}
    for t in tfs:
        tpm = (rows.get(t) or {}).get("tpm")
        if tpm is None:
            state = UNKNOWN
        elif tpm >= min_tpm:
            state = EXPRESSED
        else:
            state = LOW if ctx.kind == "gtex" else UNEXPRESSED
        out[t] = {"tpm": tpm, "state": state}
    return out


def member_key(m: dict) -> tuple:
    return (m["grade_here"], STATE_ORDER[m["state"]], -(m["tpm"] or 0.0), m["grade_any"], m["tf"])


def family_screen(groups: dict, reg, scores, z_thr: float, expression, ctx, chip, site=None, use_qbic: bool = True,
                  drop: set[str] | None = None, table_n: int = 12, min_tpm: float = 1.0) -> dict:
    """Every candidate family, ordered, with its members; `drop` removes TFs (the evaluation's ablation only)."""
    drop = {d.upper() for d in (drop or set())}
    ok = scores[scores.status == "ok"] if scores is not None else None
    by_model = {r.model: r for r in ok.itertuples(index=False) if r.z == r.z} if ok is not None else {}
    all_tfs = sorted({t for g in groups["groups"] for t in g["tfs"]} - drop)
    states = expression_states(all_tfs, expression, ctx, min_tpm)
    fams, n_pass_fams = [], 0
    for g in groups["groups"]:
        members = []
        for t in g["tfs"]:
            if t.upper() in drop or states[t]["state"] == UNEXPRESSED:
                continue
            members.append({"tf": t, **states[t], **chip.member(t)})
        n_unexpressed = sum(1 for t in g["tfs"] if t in states and states[t]["state"] == UNEXPRESSED)
        row = {"gid": g["id"], "label": g["label"], "dbd": g.get("dbd"), "n_tfs": len(g["tfs"]),
               "n_unexpressed": n_unexpressed}
        if use_qbic:
            scored = [by_model[m] for m in g["models"] if m in by_model]
            passing = [r for r in scored if abs(r.z) > z_thr]
            if not passing:
                continue
            n_pass_fams += 1
            best = max(passing, key=lambda r: abs(r.z))
            signs = {r.effect > 0 for r in passing}
            row |= {"best_model": best.model, "model_tf": reg.cognate_tf.get(best.model), "z": round(float(best.z), 2),
                    "effect": round(float(best.effect), 3), "binds_more": "alt" if best.effect > 0 else "ref",
                    "n_models": len(g["models"]), "n_models_pass": len(passing), "mixed_direction": len(signs) > 1}
        if not members:
            continue
        if not use_qbic and min(m["grade_any"] for m in members) > 2:
            continue
        members.sort(key=member_key)
        row |= {"members": members, "tier_here": min(m["grade_here"] for m in members),
                "tier_any": min(m["grade_any"] for m in members), "named": members[0]["tf"],
                "paralogs": [m["tf"] for m in members[1:] if m["grade_any"] <= 2 or m["state"] == EXPRESSED][:4],
                "max_tpm": max((m["tpm"] or 0.0) for m in members),
                "assayed": any(m["assayed_any"] for m in members)}
        fams.append(row)
    if use_qbic:
        fams.sort(key=lambda f: (f["tier_here"], f["tier_any"], -abs(f["z"]), f["label"]))
    else:
        fams.sort(key=lambda f: (f["tier_here"], f["tier_any"], -f["max_tpm"], f["label"]))
    named, unique = set(), []
    for f in fams:          # a TF in two groups is named once, by the higher family; a family left with none is dropped
        free = [m for m in f["members"] if m["tf"] not in named]
        if not free:
            continue
        f["named"] = free[0]["tf"]
        f["paralogs"] = [m["tf"] for m in free[1:] if m["grade_any"] <= 2 or m["state"] == EXPRESSED][:4]
        named.add(f["named"])
        unique.append(f)
    fams = unique
    shown = fams[:table_n]
    for i, f in enumerate(shown, 1):
        f["fid"] = f"F{i}"
        if site is not None and use_qbic:
            f["site"] = site(f["best_model"])
    counts = {"families_passing": n_pass_fams if use_qbic else None, "candidates": len(fams),
              "with_chip_here": sum(1 for f in fams if f["tier_here"] <= 2),
              "with_chip_anywhere": sum(1 for f in fams if f["tier_any"] <= 2),
              "with_summit_here": sum(1 for f in fams if f["tier_here"] == 1), "shown": len(shown)}
    return {"families": shown, "counts": counts, "z_thr": round(z_thr, 2) if use_qbic else None,
            "use_qbic": use_qbic}


def grade_text(m: dict, here_label: str) -> str:
    if m["grade_here"] == 1:
        return f"summit {m['summit_here']} bp in {here_label}"
    if m["grade_here"] == 2:
        return f"peak in {here_label}" + (f", summit {m['summit_here']} bp away" if m["summit_here"] is not None else "")
    if m["grade_any"] == 1:
        return f"summit {m['summit_any']} bp elsewhere ({', '.join(m['cells_any'][:3])})"
    if m["grade_any"] == 2:
        return f"peak elsewhere ({', '.join(m['cells_any'][:3])})"
    return "assayed here, no peak" if m["assayed_here"] else ("assayed elsewhere, no peak" if m["assayed_any"]
                                                              else "no ChIP-seq at the variant")


def member_text(m: dict, here_label: str) -> str:
    tpm = f"{m['tpm']:.1f} TPM" if m["tpm"] is not None else "TPM unknown"
    return f"{m['tf']} ({tpm}; {grade_text(m, here_label)})"


def family_line(f: dict, here_label: str, context: str) -> str:
    """One evidence row per family: what the model sees."""
    head = f"{f['fid']} {f['label'].split(',')[0]} family"
    if "z" in f:
        site = f.get("site") or {}
        site_txt = (f"; site strength ref {site['ref']}, alt {site['alt']} percentile (all overlapping {site['k']}-mers "
                    f"over 21 bp, against random 21-mers)") if "ref" in site else ""
        head += (f" (best model: {f['model_tf']} HT-SELEX, {f['n_models_pass']} of {f['n_models']} family models pass the "
                 f"gate): z {f['z']}, effect {f['effect']:+}, the {f['binds_more']} allele binds more"
                 + (" (models disagree on direction)" if f.get("mixed_direction") else "") + site_txt)
    named = next(m for m in f["members"] if m["tf"] == f["named"])
    others = [m for m in f["members"] if m["tf"] != f["named"]][:6]
    text = (f"{head}. Expression context: {context}. Code names {member_text(named, here_label)}"
            + (f"; paralogs not ruled out: {', '.join(f['paralogs'])}" if f["paralogs"] else "")
            + (f". Other members: {'; '.join(member_text(m, here_label) for m in others)}" if others else "")
            + (f". {f['n_unexpressed']} more members are not expressed here" if f["n_unexpressed"] else "") + ".")
    return text
