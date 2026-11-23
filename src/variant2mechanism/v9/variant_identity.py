"""SNV identity across primary assemblies, anchored to the exact case allele; never biological evidence."""

import re

COMPLEMENT = str.maketrans("ACGT", "TGCA")
NCBI = "https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/"
BASES = ("A", "C", "G", "T")
# How a passage names an allele: "G-allele", "T allele", "allele G", "G>T", "G/T", "G to T", "G and T alleles".
ALLELE_NAMED = re.compile(
    r"(?<![A-Za-z0-9])([ACGT])[- ]alleles?(?![A-Za-z0-9])"
    r"|(?<![A-Za-z0-9])alleles?\s+([ACGT])(?![A-Za-z0-9])"
    r"|(?<![A-Za-z0-9])([ACGT])\s*(?:>|/|→|to)\s*([ACGT])(?![A-Za-z0-9])"
    r"|(?<![A-Za-z0-9])([ACGT])\s+(?:and|or|versus|vs\.?)\s+([ACGT])\s+alleles?(?![A-Za-z0-9])")


def complement(allele):
    return allele[::-1].translate(COMPLEMENT)


def placement_rows(payload, variant, rsid):
    """Only primary chromosome placements with an exact GRCh38 anchor and the same SNV substitution.

    Multiallelic rsIDs do not identify a substitution by themselves. Relative alignment orientation determines
    the allele conversion; alternate loci, patches, mismatches and ambiguous primary placements are excluded.
    """
    if str(payload.get("refsnp_id")) != rsid.removeprefix("rs"):
        return []
    placements = []
    for p in payload.get("primary_snapshot_data", {}).get("placements_with_allele", []):
        a = p.get("placement_annot", {})
        seq = str(p.get("seq_id", ""))
        m = re.fullmatch(r"NC_0*(\d+)\.\d+", seq)
        if not m or not 1 <= int(m[1]) <= 24 or a.get("is_mismatch"):
            continue
        chrom = {23: "X", 24: "Y"}.get(int(m[1]), str(int(m[1])))
        for build in a.get("seq_id_traits_by_assembly", []):
            if not build.get("is_top_level") or build.get("is_alt") or build.get("is_patch"):
                continue
            assembly = str(build.get("assembly_name", "")).split(".")[0]
            if assembly not in ("GRCh37", "GRCh38"):
                continue
            for entry in p.get("alleles", []):
                spdi = entry.get("allele", {}).get("spdi", {})
                ref, alt = spdi.get("deleted_sequence", ""), spdi.get("inserted_sequence", "")
                if (spdi.get("seq_id") != seq or len(ref) != 1 or len(alt) != 1 or ref == alt or
                        ref not in "ACGT" or alt not in "ACGT"):
                    continue
                placements.append(dict(assembly=assembly, chrom=chrom, pos=int(spdi["position"]) + 1,
                                       ref=ref, alt=alt, seq_id=seq,
                                       opposite=bool(a.get("is_aln_opposite_orientation"))))
    anchors = [r for r in placements if (r["assembly"], r["chrom"], r["pos"], r["ref"], r["alt"]) ==
               (variant.assembly, variant.chrom, variant.pos, variant.ref, variant.alt)]
    if len(anchors) != 1:
        return []
    anchor = anchors[0]
    rows = []
    for row in placements:
        flip = row["opposite"] != anchor["opposite"]
        if (row["ref"], row["alt"]) != ((complement(variant.ref), complement(variant.alt)) if flip else
                                        (variant.ref, variant.alt)):
            continue
        rows.append({"record": "variant_mapping", **row, "case_key": variant.key, "rsid": rsid,
                     "case_strand_flip": flip, "source": NCBI + rsid[2:]})
    return [r for r in rows if sum(x["assembly"] == r["assembly"] for x in rows) == 1]


def mappings(graph):
    return [(t.tool_call_id, o) for t in graph.tool_calls.values()
            if t.tool_name == "variant_annotation" and t.execution_status == "success"
            for o in t.observations if o.get("record") == "variant_mapping" and
            o.get("case_key") == graph.case.variant.key]


def catalogue_identity(hit, detail, graph):
    """A named catalogue record is the same only when its declared-build substitution matches a case placement."""
    coords = detail.get("coordinates") or {}
    build = {"GRCH37": "GRCh37", "GRCH38": "GRCh38"}.get(str(coords.get("referenceBuild", "")).upper())
    rows = [(tid, r) for tid, r in mappings(graph) if r["assembly"] == build]
    state, matched = "unresolved", []
    pos, end = coords.get("start"), coords.get("stop")
    ref, alt = coords.get("referenceBases"), coords.get("variantBases")
    if rows and isinstance(pos, int) and pos == end and ref in ("A", "C", "G", "T") and alt in ("A", "C", "G", "T"):
        matched = [(tid, r) for tid, r in rows if (r["chrom"], r["pos"], r["ref"], r["alt"]) ==
                   (str(coords.get("chromosome", "")).removeprefix("chr"), pos, ref, alt)]
        state = "verified_same" if len(matched) == 1 else "verified_different" if not matched else "unresolved"
    return {"record": "variant_alias_identity", "status": state, "gene": hit["gene"],
            "aliases": list(dict.fromkeys([hit["name"], *hit.get("aliases", [])])),
            "case_key": graph.case.variant.key, "coordinates": coords,
            "source": f"https://civicdb.org/variants/{hit['id']}",
            "placement": matched[0][1] if len(matched) == 1 else None,
            "placement_call": matched[0][0] if len(matched) == 1 else None}


def identity_lines(graph):
    """Identity observations stay separate from biological Evidence and are visible to every investigator."""
    import json
    rows = [{"tool_call": t.tool_call_id, **o} for t in graph.tool_calls.values()
            if t.execution_status == "success" for o in t.observations
            if o.get("record") in ("variant_mapping", "variant_alias_identity")]
    return ["Identity is three-state: verified_same, verified_different, unresolved. A missing mapping does NOT "
            "mean a different variant. Catalogue names are discovery aliases, not experiments. Retain unmapped "
            "experiments in paper scope; never guess shorthand coordinates or minor/major allele bases.",
            *[json.dumps(r).replace("<", "\\u003c").replace(">", "\\u003e") for r in rows[:24]]]


def _catalogue_map(evidence, graph, article):
    names = evidence.data.get("paper_variant_names", [])
    if len(names) != 1:
        return evidence
    alias = names[0]
    context = " ".join([article.title if article else "", *evidence.about_genes, *evidence.about_elements,
                        evidence.experiment.passage if evidence.experiment else ""])
    if not re.search(r"promoter|non[- ]?coding|nucleotide|oligonucleotide|base.pair", context, re.I):
        return evidence  # do not interpret a protein substitution label as nucleotide alleles
    found = [(t.tool_call_id, o) for t in graph.tool_calls.values() if t.execution_status == "success"
             for o in t.observations if o.get("record") == "variant_alias_identity" and
             o.get("case_key") == graph.case.variant.key and alias.casefold() in
             {a.casefold() for a in o["aliases"]} and
             re.search(r"(?<![A-Za-z0-9])" + re.escape(o["gene"]) + r"(?![A-Za-z0-9])", context, re.I)]
    if not found or any(o["status"] != "verified_same" for _, o in found):
        return evidence
    tid, row = found[0]
    pair = re.fullmatch(r"([ACGT])\d+([ACGT])", alias, re.I)
    if not pair:
        return evidence  # an HGVS/transcript alias needs its own strand verifier
    pair = pair[1].upper(), pair[2].upper()
    place = row["placement"]
    target = place["ref"], place["alt"]
    if pair not in (target, tuple(complement(a) for a in target)):
        return evidence
    flip = (pair != target) != place["case_strand_flip"]
    allele = evidence.allele
    if flip and allele in ("A", "C", "G", "T"):
        allele = complement(allele)
    proof = {"paper_variant": alias, "paper_assembly": evidence.data.get("paper_assembly"),
             "placement_assembly": place["assembly"], "case_key": graph.case.variant.key,
             "source": row["source"], "tool_call": tid, "placement_source": place["source"],
             "paper_to_case_strand_flip": flip, "paper_allele": evidence.allele, "case_allele": allele}
    return evidence.model_copy(update={"about_variants": [graph.case.variant.key], "allele": allele,
        "data": {**evidence.data, "variant_identity": proof, "variant_identity_status": "verified_same"},
        "limitations": [*evidence.limitations, "Paper alias matched by exact catalogue name and gene, then "
                        "verified substitution/build; the original experiment notation is retained."]})


def named_alleles(text):
    """The single-base alleles a passage names as alleles (ALLELE_NAMED), never a base in a sequence or a word."""
    return {base for hit in ALLELE_NAMED.finditer(text or "") for base in hit.groups() if base}


def _other_strand(evidence, graph):
    """An allele the paper names on the other strand, placed on the case variant's strand.

    A paper often writes a variant's alleles on the strand of its gene: rs2168101 is C>A on the reference strand and
    G>T in the LMO1 literature. The graph reads an observation's direction for the allele it names, so such a record
    was refused ("allele T is neither ref C nor alt A") although the experiment compared the right alleles. The
    complement is taken only when nothing else can be meant:
    - the record is an experiment read from an article, names the case variant and no other one, and no other rule
      has already mapped it;
    - its allele is one base that is neither the reference nor the alternate allele;
    - the case variant's two alleles are not each other's complements (an A/T or C/G variant reads the same on both
      strands, so the base cannot say which strand was meant);
    - the verified passage itself names both complements as alleles and neither of the case's own (G and T for a
      C>A variant). A passage that names one allele only is left as it is: its partner could be a third allele.
    The experiment record keeps the paper's notation; the proof is kept in data.variant_identity."""
    v = graph.case.variant
    allele = (evidence.allele or "").upper()
    if evidence.experiment is None or evidence.data.get("variant_identity") or v.variant_type != "SNV":
        return evidence
    case, other = {v.ref, v.alt}, {complement(v.ref), complement(v.alt)}
    if allele not in BASES or allele in case or case & other:
        return evidence
    mentions = [graph.variant_mention(x) for x in evidence.about_variants]
    if "case" not in mentions or "other" in mentions:
        return evidence
    named = named_alleles(evidence.experiment.passage)
    if not other <= named or named & case:
        return evidence
    placed = complement(allele)
    proof = {"basis": "other_strand_allele_pair", "paper_alleles": sorted(other), "case_alleles": [v.ref, v.alt],
             "case_key": v.key, "paper_to_case_strand_flip": True, "paper_allele": allele, "case_allele": placed}
    note = (f"The passage names the alleles {' and '.join(sorted(other))}, the other strand's names of "
            f"{v.ref} and {v.alt}: {allele} is read as {placed}. The experiment record keeps the paper's notation.")
    return evidence.model_copy(update={"allele": placed, "data": {**evidence.data, "variant_identity": proof},
                                       "limitations": [*evidence.limitations, note]})


def normalise_evidence(evidence, graph, *, article=None):
    """Map a paper-verified coordinate and ordered allele pair, keeping the paper record and audit trail intact.

    No free rsID equivalence, naked position matching, or inferred build. If the article omits the build, accept
    only a single matching primary-assembly placement. Opposite-strand SNVs require an unambiguous ordered pair. A
    record that names the case variant by rsID and its alleles on the other strand is placed by _other_strand.
    """
    return _other_strand(_coordinate_map(_catalogue_map(evidence, graph, article), graph), graph)


def _coordinate_map(evidence, graph):
    """The coordinate rule of normalise_evidence: a paper-verified position with an ordered allele pair."""
    placements = mappings(graph)
    if not placements or len(evidence.about_variants) != 1:
        return evidence
    name = evidence.about_variants[0]
    m = re.fullmatch(r"chr(\d+|X|Y):(\d+) ([ACGT])>([ACGT])", name)
    if not m:
        return evidence
    build = evidence.data.get("paper_assembly")
    candidates = []
    for tid, row in placements:
        if (m[1], int(m[2])) != (row["chrom"], row["pos"]) or (build and build != row["assembly"]):
            continue
        pair = m[3], m[4]
        for flip, expected in [(False, (row["ref"], row["alt"])),
                               (True, (complement(row["ref"]), complement(row["alt"])) )]:
            if pair == expected:
                candidates.append((tid, row, flip))
    # Same coordinate on two assemblies is ambiguous without a stated assembly, even if both map to the case.
    if len(candidates) != 1:
        return evidence
    tid, row, flip = candidates[0]
    allele = evidence.allele
    flip = flip != row["case_strand_flip"]
    if allele in ("A", "C", "G", "T") and flip:
        allele = complement(allele)
    proof = {"paper_variant": name, "paper_assembly": build, "placement_assembly": row["assembly"],
             "case_key": row["case_key"], "source": row["source"], "tool_call": tid,
             "paper_to_case_strand_flip": flip, "paper_allele": evidence.allele, "case_allele": allele}
    return evidence.model_copy(update={"about_variants": [graph.case.variant.key], "allele": allele,
                                       "data": {**evidence.data, "variant_identity": proof},
                                       "limitations": [*evidence.limitations,
                                                        "Variant identity mapped using verified NCBI placements; "
                                                        "the experiment record retains the paper's notation."]})
