"""SCREEN V4 from local downloads (v8): a cCRE's class in each of the 170 core-collection biosamples, and its cCRE-gene
links (3D chromatin, eQTLs, CRISPR). SCREEN's own API is closed to the public while authentication is added, so these
are the files from downloads.wenglab.org (data/screen, outside Dropbox). A lookup scans the gzipped files once per
cCRE and is cached as JSON under cache/screen.
"""

import gzip
import json
import subprocess
from pathlib import Path

from ..config import Config, load_config
from .chipgrade import name_match

FILES = {"classes": "Core-Collection-Class-Matrix.txt.gz", "3d": "V4-hg38.Gene-Links.3D-Chromatin.txt.gz",
         "eqtl": "V4-hg38.Gene-Links.eQTLs.txt.gz", "crispr": "V4-hg38.Gene-Links.CRISPR.txt.gz"}
ACTIVE = ("PLS", "pELS", "dELS")
OPEN = ("CA-H3K4me3", "CA-CTCF", "CA-TF", "CA-only", "TF-only")
ENCODE_SEARCH = "https://www.encodeproject.org/search/?type=Experiment&format=json&limit=all&field=accession" \
                "&field=biosample_ontology.term_name&"
SOURCE = "SCREEN V4 (ENCODE cCRE registry), downloads.wenglab.org"
# GTEx tissue -> words that name the same tissue among SCREEN and ChIP-seq biosamples
TISSUE_WORDS = {"adipose": ["adipose", "adipocyte"], "colon": ["colon", "colonic"], "liver": ["liver", "hepatocyte"],
                "breast": ["breast", "mammary"], "prostate": ["prostate"], "skin": ["skin", "keratinocyte", "foreskin"],
                "lung": ["lung"], "blood": ["blood", "t-cell", "b cell", "monocyte", "lymphocyte"],
                "brain": ["brain", "astrocyte", "neural", "neuron"], "heart": ["heart", "cardiac"],
                "muscle": ["muscle", "myotube", "skeletal"], "stomach": ["stomach", "gastric"],
                "pancreas": ["pancrea"], "kidney": ["kidney", "renal"], "nerve": ["nerve", "schwann"],
                "esophagus": ["esophag", "oesophag"], "artery": ["artery", "aorta", "endothelial"],
                "thyroid": ["thyroid"], "ovary": ["ovary"], "testis": ["testis"], "spleen": ["spleen"]}


def _dirs(cfg: Config) -> tuple[Path, Path]:
    cache = cfg.path("v8", "screen_cache")
    cache.mkdir(parents=True, exist_ok=True)
    return cfg.path("data", "screen_dir"), cache


def _zgrep(path: Path, word: str) -> list[str]:
    out = subprocess.run(["zgrep", "-F", "-w", word, str(path)], capture_output=True, text=True, check=False)
    return [line for line in out.stdout.splitlines() if line.split("\t", 1)[0] == word]


def core_biosamples(http, cfg: Config | None = None) -> list[str]:
    """Biosample names of the class matrix's columns, which are ENCODE experiment accessions."""
    cfg = cfg or load_config()
    data, _ = _dirs(cfg)
    saved = data / "core_biosamples.json"
    if saved.exists():
        return json.loads(saved.read_text())
    with gzip.open(data / FILES["classes"], "rt") as f:
        accessions = f.readline().rstrip("\n").split("\t")[1:]
    r = http.get(ENCODE_SEARCH + "&".join(f"accession={a}" for a in accessions), timeout=180)
    if not r.ok:
        raise RuntimeError(f"ENCODE search for the core biosamples failed: {r.error}")
    names = {x["accession"]: (x.get("biosample_ontology") or {}).get("term_name", x["accession"])
             for x in r.data.get("@graph", [])}
    out = [names.get(a, a) for a in accessions]
    saved.write_text(json.dumps(out))
    return out


def lookup(ccre: str, http, cfg: Config | None = None) -> dict:
    """The cCRE's class in each core biosample and its gene links, from the cache or the files."""
    cfg = cfg or load_config()
    data, cache = _dirs(cfg)
    path = cache / f"{ccre}.json"
    if path.exists():
        return json.loads(path.read_text())
    names = core_biosamples(http, cfg)
    rows = {k: _zgrep(data / name, ccre) for k, name in FILES.items()}
    classes = list(zip(names, rows["classes"][0].split("\t")[1:], strict=False)) if rows["classes"] else []
    out = {"ccre": ccre, "classes": classes, "links": _links(rows)}
    path.write_text(json.dumps(out))
    return out


def warm(ccres: list[str], http, cfg: Config | None = None) -> list[str]:
    """Fill the cache for many cCREs with one pass over each file (grep -F -f), instead of one scan per cCRE."""
    cfg = cfg or load_config()
    data, cache = _dirs(cfg)
    todo = sorted({c for c in ccres if c and not (cache / f"{c}.json").exists()})
    if not todo:
        return []
    names = core_biosamples(http, cfg)
    ids = cache / "_ids.txt"
    ids.write_text("\n".join(todo) + "\n")
    found: dict[str, dict[str, list[str]]] = {c: {k: [] for k in FILES} for c in todo}
    for kind, name in FILES.items():
        cmd = f"gzip -dc {data / name} | grep -F -w -f {ids}"
        out = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=False).stdout
        for line in out.splitlines():
            key = line.split("\t", 1)[0]
            if key in found:
                found[key][kind].append(line)
    ids.unlink()
    for c, rows in found.items():
        classes = list(zip(names, rows["classes"][0].split("\t")[1:], strict=False)) if rows["classes"] else []
        (cache / f"{c}.json").write_text(json.dumps({"ccre": c, "classes": classes, "links": _links(rows)}))
    return todo


def _links(rows: dict[str, list[str]]) -> dict:
    links = {"3d": [], "eqtl": [], "crispr": []}
    for line in rows["3d"]:
        p = line.split("\t")
        links["3d"].append({"gene": p[2].strip(), "gene_type": p[3], "method": p[4], "experiment": p[5],
                            "biosample": p[6].split("_genetically")[0].replace("_", " "),
                            "modified": "_genetically" in p[6], "score": p[7]})
    for line in rows["eqtl"]:
        p = line.split("\t")
        links["eqtl"].append({"gene": p[2].strip(), "gene_type": p[3], "variant": p[4], "source": p[5],
                              "tissue": p[6], "slope": float(p[7]), "p": float(p[8])})
    for line in rows["crispr"]:
        p = line.split("\t")
        links["crispr"].append({"gene": p[2].strip(), "gene_type": p[3], "region": p[4], "method": p[5],
                                "experiment": p[6], "biosample": p[7], "effect": float(p[8]), "p": float(p[9])})
    return links


def matches(name: str, here_names: list[str], tissue: str | None = None) -> bool:
    """A biosample matches the context by name (HCT116, HCT-116) or, for a GTEx tissue, by the tissue's words."""
    if any(name_match(n, name) for n in here_names):
        return True
    if tissue:
        low = name.lower()
        return any(w in low for key, words in TISSUE_WORDS.items() if key in tissue.lower() for w in words)
    return False


def activity(classes: list[tuple[str, str]], here_names: list[str], tissue: str | None = None) -> dict:
    """Active (PLS, pELS, dELS), open (CA-*), inactive (Low-DNase in every matched biosample) or unknown (no matched
    core biosample), with the matched rows and the biosamples where the element is active."""
    if not classes:
        return {"status": "no_ccre_data", "here": [], "active_elsewhere": [], "n": 0}
    here = [(n, c) for n, c in classes if matches(n, here_names, tissue)]
    active = [(n, c) for n, c in classes if c in ACTIVE]
    if not here:
        status = "unknown"
    elif any(c in ACTIVE for _, c in here):
        status = "active"
    elif any(c in OPEN for _, c in here):
        status = "open"
    else:
        status = "inactive"
    return {"status": status, "here": here, "active_elsewhere": active, "n": len(classes)}
