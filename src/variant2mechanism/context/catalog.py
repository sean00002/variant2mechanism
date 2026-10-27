"""The gather order and the investigate tools with their strict schemas (spec 2, section 6).

The model passes only the arguments in each schema; code binds the variant and the case.
"""

from collections.abc import Callable

from .base import Case, ToolResult, call_tool
from .ccre import ccre_lookup
from .chip import chip_peaks
from .depmap import gene_dependency, tf_expression
from .ensembl import nearest_genes, variant_annotation
from .genetics import eqtl_lookup, finemap_lookup, gene_disease, gwas_lookup
from .literature import literature_search

# Fixed gather order; evidence IDs are numbered in this order whatever finishes first.
GATHER_ORDER = ["variant_annotation", "nearest_genes", "ccre_lookup", "gwas_lookup", "finemap_lookup",
                "literature_search", "qbic_screen"]
GERMLINE_ONLY = {"gwas_lookup", "finemap_lookup"}


def _schema(props: dict) -> dict:
    """Strict tool schema: every property is required; optional ones accept null."""
    return {"type": "object", "properties": props, "required": list(props), "additionalProperties": False}


def _opt(desc: str) -> dict:
    return {"type": ["string", "null"], "description": desc}


INVESTIGATE_TOOLS: dict[str, dict] = {
    "qbic_tf_detail": {
        "description": ("Look up what QBiC-SELEX predicts for one named TF at this variant, including old or "
                        "ambiguous names. Says whether the TF has its own model, is covered through CIS-BP-mapped "
                        "models, or is not in coverage."),
        "input_schema": _schema({"tf": {"type": "string", "description": "TF name, ideally an HGNC symbol"}}),
        "configs": {"full"},
    },
    "chip_peaks": {
        "description": "ENCODE ChIP-seq peaks of one TF that contain this variant (Factorbook), optionally in one "
                       "biosample (cell line or tissue name).",
        "input_schema": _schema({"tf": {"type": "string", "description": "HGNC symbol of the ChIP target"},
                                 "biosample": _opt("biosample name such as HCT116, or null for all")}),
        "configs": {"no_qbic", "full"},
    },
    "eqtl_lookup": {
        "description": "GTEx v8 single-tissue eQTLs for this variant, optionally limited to one tissue.",
        "input_schema": _schema({"tissue": _opt("GTEx tissue such as 'Colon - Transverse', or null for all")}),
        "configs": {"no_qbic", "full"},
    },
    "tf_expression": {
        "description": "Expression (TPM and rank among TFs) of one TF in this case's expression context, or in "
                       "another DepMap or GTEx context.",
        "input_schema": _schema({"tf": {"type": "string", "description": "TF name"},
                                 "context": _opt("DepMap:<ModelID>, DepMap:subtype=<subtype>, GTEx:<tissue>, "
                                                 "or null for the case's context")}),
        "configs": {"no_qbic", "full"},
    },
    "literature_search": {
        "description": "Search Europe PMC; returns PMIDs and titles, and verbatim quotes from the abstracts.",
        "input_schema": _schema({"query": {"type": "string", "description": "Europe PMC query"}}),
        "configs": {"no_qbic", "full"},
    },
    "gene_disease": {
        "description": "Open Targets association between one gene and this case's disease, by evidence type.",
        "input_schema": _schema({"gene": {"type": "string", "description": "HGNC symbol"}}),
        "configs": {"no_qbic", "full"},
    },
    "gene_dependency": {
        "description": "DepMap CRISPR knockout effect of one gene in this case's cancer lineage, and whether the "
                       "gene is common-essential (cancer cases).",
        "input_schema": _schema({"gene": {"type": "string", "description": "HGNC symbol"}}),
        "configs": {"no_qbic", "full"},
    },
}

LOCAL_TOOLS: dict[str, Callable[..., ToolResult]] = {
    "variant_annotation": variant_annotation, "nearest_genes": nearest_genes, "ccre_lookup": ccre_lookup,
    "gwas_lookup": gwas_lookup, "finemap_lookup": finemap_lookup, "literature_search": literature_search,
    "chip_peaks": chip_peaks, "eqtl_lookup": eqtl_lookup, "tf_expression": tf_expression,
    "gene_disease": gene_disease, "gene_dependency": gene_dependency,
}


def tool_specs(config: str, cancer: bool) -> dict[str, dict]:
    """The investigate tools available here, by name; gene_dependency only for cancer cases."""
    return {name: spec for name, spec in INVESTIGATE_TOOLS.items()
            if config in spec["configs"] and not (name == "gene_dependency" and not cancer)}


def tool_definitions(config: str, cancer: bool) -> list[dict]:
    """Function tool definitions (strict, OpenAI chat-completions form) for the investigate step."""
    return [{"type": "function", "function": {"name": name, "description": spec["description"],
                                              "parameters": spec["input_schema"], "strict": True}}
            for name, spec in tool_specs(config, cancer).items()]


def run_context_tool(name: str, case: Case, args: dict) -> ToolResult:
    """Run one non-QBiC tool with model-supplied arguments (validated against its schema by the caller)."""
    fn = LOCAL_TOOLS[name]
    clean = {k: v for k, v in args.items() if v is not None}
    return call_tool(fn, case, **clean)
