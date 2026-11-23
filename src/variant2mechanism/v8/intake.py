"""Intake (v8, code): the facts that set a run's route, each with its reason. Nothing here comes from a model.

- Association with the disease: a GWAS Catalog association (p <= 5e-8) or an Open Targets credible set for a matching
  trait supports it. A common variant with neither gives "no association found"; a rare variant, or a somatic one (v2m
  has no recurrence data), is "not testable".
- Promoter: the variant lies from 1 kb upstream to 500 bp downstream of a transcript start, of any gene type.
- Context: the expression context, given or inferred (the cancer's Oncotree subtype in DepMap; else the GTEx tissue of
  the variant's strongest eQTL; else a core biosample where its element is active), and the biosample names that
  match it in ChIP-seq and SCREEN.
"""

import re
from functools import lru_cache

import pandas as pd

from ..config import load_config
from ..context.occupancy import biosample_match
from .screendb import ACTIVE, TISSUE_WORDS

GENOME_WIDE = 5e-8
RARE = 0.01
GENERIC = {"cancer", "carcinoma", "adenocarcinoma", "neoplasm", "neoplasms", "tumour", "tumor", "malignant",
           "disease", "and", "or", "of", "the", "with", "levels", "level", "risk"}
CANCER_WORDS = {"cancer", "carcinoma", "adenocarcinoma", "neoplasm", "tumour", "tumor", "malignant", "glioblastoma",
                "neuroblastoma", "melanoma", "lymphoma", "leukaemia", "leukemia", "sarcoma", "glioma"}
CANCER_SYNONYMS = {"colorectal": {"colon", "rectal", "colorectal"}, "liver": {"hepatocellular", "liver"},
                   "brain": {"glioma", "glioblastoma"}, "bowel": {"colon", "rectal"}}
NON_CANCER = ("non-cancerous", "fibroblast", "immortalized", "hyperplasia", "normal")
SYNONYMS = {"ldl cholesterol": ["ldl", "low density lipoprotein"],
            "obesity": ["obesity", "body mass index", "bmi", "adiposity", "waist", "body weight"],
            "myocardial infarction": ["myocardial infarction", "coronary artery disease", "coronary heart disease"],
            "cleft lip": ["cleft"]}
ENSEMBL_OVERLAP = ("https://rest.ensembl.org/overlap/region/human/{chrom}:{start}-{end}?feature=gene;"
                   "feature=transcript;content-type=application/json")


def words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def disease_phrases(disease: str) -> list[str]:
    text = re.sub(r"\([^()]*\)", " ", disease)
    parts = re.split(r"[,;/]| or ", text)
    return [p.strip().lower() for p in parts if p.strip()]


def trait_matches(trait: str, disease: str) -> bool:
    """Every content word of one disease phrase is in the trait (a generic cancer word matches any cancer word), or
    one of the phrase's synonyms is."""
    t = trait.lower()
    tw = words(t)
    for phrase in disease_phrases(disease):
        if any(s in t for s in SYNONYMS.get(phrase, [])):
            return True
        pw = words(phrase)
        content = pw - GENERIC
        if not content:
            continue
        cancerish = bool(pw & CANCER_WORDS)
        if content <= tw and (not cancerish or tw & CANCER_WORDS or content & CANCER_WORDS):
            return True
    return False


def minor_allele_frequency(va_full, alt: str) -> float | None:
    """From VEP's colocated variants: the alt allele's gnomAD genome frequency (else 1000 Genomes), folded."""
    try:
        for c in va_full[0].get("colocated_variants", []):
            freqs = (c.get("frequencies") or {}).get(alt)
            if freqs:
                f = freqs.get("gnomadg", freqs.get("af"))
                if f is not None:
                    return round(min(f, 1 - f), 4)
    except (TypeError, IndexError, KeyError):
        return None
    return None


def disease_line(origin: str, disease: str, gwas, finemap, va, alt: str) -> dict:
    """supported, no_association, not_testable or unknown (the tools failed), with the matching evidence."""
    if origin == "somatic":
        return {"state": "not_testable", "reason": "somatic variant: v2m has no tumour recurrence data", "matches": []}
    matches = []
    if gwas is not None and gwas.ok:
        for a in gwas.full or []:
            trait = "; ".join(a.get("reported_trait") or [])
            p = a.get("p_value")
            if trait and p is not None and p <= GENOME_WIDE and trait_matches(trait, disease):
                eff = ", ".join(x.get("effect_allele", "?") for x in a.get("snp_allele") or [])
                matches.append({"source": "GWAS Catalog", "trait": trait, "p": p, "effect_allele": eff,
                                "beta": a.get("beta"), "pmid": a.get("pubmed_id")})
    if finemap is not None and finemap.ok and isinstance(finemap.full, dict):
        for x in finemap.full.get("gwas", []):
            trait = x["study"]["traitFromSource"]
            if trait_matches(trait, disease):
                loc = x["locus"]["rows"]
                matches.append({"source": "Open Targets credible set", "trait": trait,
                                "pip": loc[0]["posteriorProbability"] if loc else None, "study": x["study"]["id"]})
    if matches:
        best = matches[0]
        what = (f"p {best['p']:.1e}" if "p" in best else f"PIP {best['pip']:.2f}" if best.get("pip") is not None
                else "in a credible set")
        return {"state": "supported", "reason": f"{best['source']}: {best['trait']} ({what}); {len(matches)} matching "
                                                f"association(s) in all", "matches": matches[:12]}
    gwas_ok, finemap_ok = gwas is not None and gwas.ok, finemap is not None and finemap.ok
    if not (gwas_ok or finemap_ok):
        return {"state": "unknown", "reason": "the GWAS and fine-mapping lookups failed", "matches": []}
    maf = minor_allele_frequency(va.full if va is not None and va.ok else None, alt)
    if maf is not None and maf < RARE:
        return {"state": "not_testable", "reason": f"rare variant (MAF {maf}): GWAS cannot test it", "matches": [],
                "maf": maf}
    # an absence counts only when both sources answered and GWAS could have seen the variant (it is common)
    if not (gwas_ok and finemap_ok):
        down = "Open Targets" if gwas_ok else "GWAS Catalog"
        return {"state": "unknown", "matches": [], "maf": maf,
                "reason": f"the {down} lookup failed, so the other's lack of an association with {disease} cannot "
                          "be read as an absence"}
    if maf is None:
        return {"state": "unknown", "matches": [], "maf": None,
                "reason": f"neither the GWAS Catalog nor Open Targets lists an association with {disease}, but the "
                          "variant's frequency is unknown, so whether GWAS could test it is unknown"}
    return {"state": "no_association", "matches": [], "maf": maf,
            "reason": f"common variant (MAF {maf}): neither the GWAS Catalog nor Open Targets lists an association "
                      f"with {disease}"}


def promoter_check(case) -> dict:
    """Transcript starts (any gene type) within 1 kb; promoter = 1 kb upstream to 500 bp downstream of one."""
    v = case.variant
    url = ENSEMBL_OVERLAP.format(chrom=v.chrom.removeprefix("chr"), start=max(1, v.pos - 1000), end=v.pos + 1000)
    r = case.http.get(url, timeout=60)
    if not r.ok or not isinstance(r.data, list):
        return {"ok": False, "promoter_of": [], "nearest_tss": None, "url": url}
    genes = {g["id"]: g for g in r.data if g.get("feature_type") == "gene"}
    hits = []
    for t in (x for x in r.data if x.get("feature_type") == "transcript"):
        tss = t["start"] if t["strand"] == 1 else t["end"]
        d = (v.pos - tss) * t["strand"]                 # negative: upstream of the start
        g = genes.get(t.get("Parent"), {})
        name = g.get("external_name") or (t.get("external_name") or "").rsplit("-", 1)[0] or t.get("Parent") or "?"
        hits.append({"gene": name, "biotype": g.get("biotype") or t.get("biotype"), "distance": d})
    hits.sort(key=lambda h: abs(h["distance"]))
    promoter = []
    for h in hits:
        if -1000 <= h["distance"] <= 500 and h["gene"] not in [p["gene"] for p in promoter]:
            promoter.append(h)
    return {"ok": True, "promoter_of": promoter, "nearest_tss": hits[0] if hits else None, "url": url}


# -- context --------------------------------------------------------------------------------------------------------


@lru_cache(maxsize=1)
def depmap_models() -> pd.DataFrame:
    cfg = load_config()
    cols = ["ModelID", "CellLineName", "StrippedCellLineName", "OncotreeLineage", "OncotreePrimaryDisease",
            "OncotreeSubtype"]
    return pd.read_csv(cfg.path("data", "depmap_models"), usecols=cols, low_memory=False
                       ).drop_duplicates("ModelID").set_index("ModelID")


def norm(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", str(name).lower())


def cancer_subtype(disease: str, expression) -> tuple[str, int] | None:
    """The cancer subtype in DepMap (with expression data) that names a disease phrase's content words (colorectal
    also matches colon and rectal); non-cancerous subtypes never match; ties go to the subtype with more lines."""
    counts = expression.subtype.value_counts()
    models = depmap_models()
    primary = models.groupby("OncotreeSubtype")["OncotreePrimaryDisease"].first()
    best = None
    for phrase in disease_phrases(disease):
        content = set()
        for w in words(phrase) - GENERIC:
            content |= CANCER_SYNONYMS.get(w, {w})
        if not content:
            continue
        for sub, n in counts.items():
            label = f"{sub} {primary.get(sub, '')}".lower()
            if any(x in label for x in NON_CANCER):
                continue
            overlap = len(content & words(str(sub)))
            if overlap and (best is None or (overlap, n) > (best[2], best[1])):
                best = (sub, int(n), overlap)
        if best:                                      # the first disease phrase that matches wins
            return best[0], best[1]
    return None


def gtex_column(tissue_id: str, expression) -> str | None:
    want = norm(tissue_id)
    return next((c for c in expression.gtex.columns if norm(c) == want), None)


def infer_context(disease: str, cancer: bool, eqtl, classes: list, expression) -> dict:
    """The first route that gives a context: cancer subtype, strongest eQTL tissue, active core biosample."""
    tried = []
    if cancer:
        hit = cancer_subtype(disease, expression)
        if hit:
            return {"context": f"DepMap:subtype={hit[0]} (median of {hit[1]} lines)", "route": "cancer subtype",
                    "reason": f"'{disease}' matches the DepMap Oncotree subtype '{hit[0]}' ({hit[1]} lines)",
                    "tried": tried}
        tried.append("cancer subtype: no DepMap subtype matches the disease")
    rows = sorted(eqtl.full or [], key=lambda x: x["pValue"]) if eqtl is not None and eqtl.ok else []
    for x in rows:
        col = gtex_column(x["tissueSiteDetailId"], expression)
        if col:
            return {"context": f"GTEx:{col}", "route": "eQTL tissue",
                    "reason": f"the variant's strongest GTEx eQTL is for {x['geneSymbol']} in {col} "
                              f"(p {x['pValue']:.1e})", "tried": tried}
    tried.append("eQTL tissue: no GTEx eQTL" if not rows else "eQTL tissue: no tissue with expression data")
    models = depmap_models()
    lines = {norm(n): mid for mid, n in models.CellLineName.items()}
    for name, cls in classes or []:
        if cls not in ACTIVE:
            continue
        if norm(name) in lines:
            mid = lines[norm(name)]
            return {"context": f"DepMap:{mid} ({models.at[mid, 'CellLineName']})", "route": "active element",
                    "reason": f"the element is active ({cls}) in the core biosample {name}", "tried": tried}
        for key, ws in TISSUE_WORDS.items():
            if any(w in name.lower() for w in ws):
                col = next((c for c in expression.gtex.columns if key in c.lower()), None)
                if col:
                    return {"context": f"GTEx:{col}", "route": "active element",
                            "reason": f"the element is active ({cls}) in {name}", "tried": tried}
    tried.append("active element: no active core biosample maps to an expression context")
    return {"context": None, "route": "none", "reason": "; ".join(tried), "tried": tried}


def here_names(context: str | None) -> tuple[list[str], str | None]:
    """Biosample names matching the context (ChIP-seq, SCREEN), and the GTEx tissue for word matching."""
    if not context or context.lower().startswith("none"):
        return [], None
    m = biosample_match(context)
    names = list(m.biosamples)
    models = depmap_models()
    if context.startswith("DepMap:subtype="):
        sub = re.sub(r"\s*\([^()]*\)\s*$", "", context[len("DepMap:subtype="):]).strip()
        if not names:
            names = models.loc[models.OncotreeSubtype == sub, "CellLineName"].dropna().tolist()
        return names, None
    if context.startswith("DepMap:"):
        mid = re.match(r"DepMap:(ACH-\d+)", context)
        if not names and mid and mid.group(1) in models.index:
            names = [models.at[mid.group(1), "CellLineName"]]
        return names, None
    if context.startswith("GTEx:"):
        tissue = context[len("GTEx:"):].strip()
        key = next((k for k in TISSUE_WORDS if k in tissue.lower()), None)
        return names + (TISSUE_WORDS[key] if key else []), tissue
    return names, None
