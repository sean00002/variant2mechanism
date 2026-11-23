"""An optional check of coloc.py and susie.py against the R packages they follow (coloc, susieR), through Rscript.

Nothing in this package needs R. Where R and the two packages are installed, the same numbers can be run through
both and compared; where they are not, `available` says so and the comparison is skipped (the tests skip it too).
The R side is two small scripts in this file, each reading a CSV this module writes and printing numbers only.
"""

import shutil
import subprocess
import tempfile
from pathlib import Path

import numpy as np

COLOC_R = """
args <- commandArgs(trailingOnly = TRUE)
d <- read.csv(args[1])
suppressPackageStartupMessages(library(coloc))
one <- list(beta = d$beta1, varbeta = d$se1^2, snp = as.character(d$snp), type = "quant", sdY = as.numeric(args[2]))
two <- list(beta = d$beta2, varbeta = d$se2^2, snp = as.character(d$snp), type = "quant", sdY = as.numeric(args[3]))
sink(tempfile())
res <- coloc.abf(one, two, p1 = as.numeric(args[4]), p2 = as.numeric(args[5]), p12 = as.numeric(args[6]))
sink()
cat(paste(format(unname(res$summary[2:6]), digits = 15), collapse = ","))
"""
SUSIE_R = """
args <- commandArgs(trailingOnly = TRUE)
z <- read.csv(args[1])$z
R <- as.matrix(read.csv(args[2], header = FALSE))
suppressPackageStartupMessages(library(susieR))
fit <- susie_rss(z = z, R = R, n = as.numeric(args[3]))
cat(paste(format(fit$pip, digits = 15), collapse = ","))
"""


def available(packages: tuple[str, ...] = ("coloc", "susieR")) -> bool:
    """Whether Rscript is on the path and has every package named."""
    if shutil.which("Rscript") is None:
        return False
    wanted = ", ".join(f'"{p}"' for p in packages)
    code = f"cat(all(sapply(c({wanted}), requireNamespace, quietly = TRUE)))"
    try:
        done = subprocess.run(["Rscript", "-e", code], capture_output=True, text=True, timeout=120, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return False
    return done.returncode == 0 and done.stdout.strip().endswith("TRUE")


def _run(script: str, *args: str) -> np.ndarray:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "check.R"
        path.write_text(script)
        done = subprocess.run(["Rscript", str(path), *args], capture_output=True, text=True, timeout=600,
                              check=False)
    if done.returncode != 0:
        raise RuntimeError(f"Rscript failed: {done.stderr.strip()[-500:]}")
    return np.array([float(x) for x in done.stdout.strip().split(",")])


def coloc_abf_r(beta1: np.ndarray, se1: np.ndarray, beta2: np.ndarray, se2: np.ndarray, sdy1: float = 1.0,
                sdy2: float = 1.0, p1: float = 1e-4, p2: float = 1e-4, p12: float = 1e-5) -> np.ndarray:
    """PP.H0 to PP.H4 from R's coloc.abf for two quantitative traits with the standard deviations given."""
    with tempfile.TemporaryDirectory() as tmp:
        table = Path(tmp) / "traits.csv"
        rows = ["snp,beta1,se1,beta2,se2"] + [f"s{i},{a!r},{b!r},{c!r},{d!r}" for i, (a, b, c, d) in enumerate(
            zip(map(float, beta1), map(float, se1), map(float, beta2), map(float, se2), strict=True))]
        table.write_text("\n".join(rows) + "\n")
        return _run(COLOC_R, str(table), repr(float(sdy1)), repr(float(sdy2)), repr(p1), repr(p2), repr(p12))


def susie_pip_r(z: np.ndarray, r: np.ndarray, n: float) -> np.ndarray:
    """The posterior inclusion probabilities from R's susie_rss with its defaults."""
    with tempfile.TemporaryDirectory() as tmp:
        zs, ld = Path(tmp) / "z.csv", Path(tmp) / "ld.csv"
        zs.write_text("z\n" + "\n".join(repr(float(x)) for x in z) + "\n")
        np.savetxt(ld, np.asarray(r, float), delimiter=",", fmt="%.17g")
        return _run(SUSIE_R, str(zs), str(ld), repr(float(n)))
