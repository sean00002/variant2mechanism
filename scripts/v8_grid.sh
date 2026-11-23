#!/usr/bin/env zsh
# The v8 testing plan on GPT-6 Luna (agent-lab/v8-plan-draft.md, testing section), after the pilot and the freeze.
# Stages 3 to 5 plus the named reference, then the code-only baselines (no model calls). Runs already done are
# skipped, so the script can be re-run after an interruption.
#   zsh -i scripts/v8_grid.sh
set -u
export UV_PROJECT_ENVIRONMENT=$HOME/.venvs/v2m-v2
cd "${0:A:h}/.."
TF_CASES=(tert_c228t tert_c250t rs6983267 rs4784227 rs339331 rs2168101 rs12740374 rs1421085 rs642961)
run() { uv run --quiet v2m v8 eval --profile luna_v8 --concurrency 5 "$@" || echo "STAGE FAILED: $*"; }
run --arm single                                   # stage 3: memory floor
run --arm ablation --cases $TF_CASES               # stage 3: evidence ablation (TF cases only)
run --arm full_given                               # stage 4: the main arm, seed 0
run --arm full_inferred
run --arm noqbic_given
run --arm full_given --seeds 1 2                   # stage 5: seeds
run --arm named_given                              # the real-use reference
for arm in full_given full_inferred noqbic_given named_given; do
  run --arm $arm --code-only
done
run --arm ablation --cases $TF_CASES --code-only
echo "GRID DONE"
