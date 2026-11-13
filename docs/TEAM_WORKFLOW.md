# Second Submission — Team Workflow

Goal: one cohesive, reproducible project (collect → clean → EDA → model → report) that
addresses the feedback from submission 1. Every task is its own branch, its own PR with a
real description, and a review from a *different* teammate.

## Task assignments

Pablo takes the single hardest task (modeling); everything else is spread out so commit and
PR history is balanced. Helen and Lilly get the easiest tasks.

| # | Owner | Difficulty | Branch | Deliverable |
|---|-------|-----------|--------|-------------|
| 1 | Pablo | Hard | `feature/modeling` | Add `scikit-learn` to the pinned env; `notebooks/04_modeling.ipynb` (stratified split, baseline logistic regression, tree-based model, 84/16 imbalance handling, cross-validation, metrics, feature importance); reusable code in `src/risk_data/modeling.py` |
| 2 | Jorlfran | Easy | `feature/categorical-eda-update` | Update `02_eda_categorical.ipynb`: load data via `risk_data`, add comments and section headers, remove unused cells |
| 3 | Lilly | Easiest | `feature/cleaning-notebook` | `notebooks/00_data_cleaning.ipynb`: run `risk_data.clean`, show before/after row counts, document missing-value handling (numeric = median; categorical = none found, state the rule) |
| 4 | Lilly | Easiest | `docs/final-repo-check` | Day-7 fresh-clone run (env, collect, clean, notebooks) and README/checklist fixes |
| 5 | Helen | Easiest | `docs/numerical-eda-cleanup` | Tidy `01_eda_numerical.ipynb`: comments, section order, remove unneeded content; add a short "what this means for modeling" cell |
| 6 | Helen | Easiest | `docs/executive-summary` | `reports/executive_summary.md` (max 600 words, template sections), written from Pablo's modeling results; Pablo and Jorlfran review for accuracy |

## Review rotation (so PR activity is balanced)

| PR | Author | Reviewer |
|----|--------|----------|
| 1 | Pablo | Jorlfran (code) and Lilly (docs) |
| 2 | Jorlfran | Helen |
| 3, 4 | Lilly | Jorlfran, Pablo |
| 5 | Helen | Lilly |
| 6 | Helen | Pablo and Jorlfran |

Each PR description: what changed, why, how to test it, and a screenshot or table if relevant.
Each reviewer leaves at least one real comment (not just "LGTM").

## Timeline

1. **Day 1** — merge env/organization PR (`chore/env-and-repo-organization`). Everyone pulls `main`, recreates the env, and confirms `import risk_data` works.
2. **Days 2–4** — tasks 1 to 3 and 5 in parallel.
3. **Days 5–6** — task 1 finishes; task 6 is written from its results.
4. **Day 7** — fresh clone on a clean machine: create env, run collect → clean → notebooks top to bottom. Fix anything that fails.
5. **Before submitting** — each member fills in the peer-review form; README checklist updated.

## Rubric check

| Rubric item | Covered by |
|-------------|-----------|
| Data science lifecycle | tasks 1, 2, 3, 5 (clean → EDA → model) |
| Reproducibility | pinned env, `pyproject.toml`, task 4 (day-7 clean run) |
| Modeling and evaluation | task 1 |
| Communication and reporting | task 6 |
| GitHub collaboration | branches + review rotation above |
