# Second Submission — Team Workflow

Goal: one cohesive, reproducible project (collect → clean → EDA → model → report) that
addresses the feedback from submission 1. Every task is its own branch, its own PR with a
real description, and a review from a *different* teammate.

## Task assignments

Every member owns distinct pieces of the pipeline, opens their own PRs, and reviews others.
Pablo already did the setup and the core modeling code, so Pablo takes **no new work** beyond
the modeling PR and reviews. See `docs/MODELING_NOTES.md` for findings and briefs.

| # | Owner | Branch | Deliverable |
|---|-------|--------|-------------|
| 1 | Pablo | `feature/modeling` | `src/risk_data/modeling.py`, `tests/`, `notebooks/04_modeling.ipynb`, `scikit-learn`/`pytest` pinned in the env. **Already built; this PR goes first** so everyone can import it |
| 2 | Lilly | `feature/cleaning-notebook` | `notebooks/00_data_cleaning.ipynb`: run `risk_data.clean`, before/after row counts, documented missing-value strategy (numeric = median; categorical = none found, state the rule) |
| 3 | Lilly | `feature/model-tuning` | `notebooks/07_tuning.ipynb` (brief in MODELING_NOTES) |
| 4 | Jorlfran | `feature/categorical-eda-update` | Update `02_eda_categorical.ipynb`: load via `risk_data`, comments, section headers, remove unused cells |
| 5 | Jorlfran | `feature/leakage-sensitivity` | `notebooks/06_leakage_and_sensitivity.ipynb` (brief in MODELING_NOTES) |
| 6 | Helen | `docs/numerical-eda-cleanup` | Tidy `01_eda_numerical.ipynb`; add a short "what this means for modeling" cell |
| 7 | Helen | `feature/feature-importance` | `notebooks/05_feature_importance.ipynb` (brief in MODELING_NOTES) |
| 8 | Helen | `docs/executive-summary` | `reports/executive_summary.md` (max 600 words, template sections) from executed results |
| 9 | Jorlfran | `docs/final-repo-check` | Fresh-clone run (env, collect, clean, every notebook top to bottom) and README/checklist fixes |

Per person: Pablo 1 PR, Lilly 2, Jorlfran 3, Helen 3. Pablo's other contribution is review (below).

## Review rotation (so PR activity is balanced)

Every PR needs one reviewer who is not the author, and the reviewer leaves at least one real comment.

| PR | Author | Reviewer |
|----|--------|----------|
| 1 | Pablo | Lilly |
| 2, 3 | Lilly | Pablo (2), Helen (3) |
| 4, 5, 9 | Jorlfran | Lilly (4), Pablo (5), Helen (9) |
| 6, 7, 8 | Helen | Jorlfran (6), Lilly (7), Pablo (8) |

Reviews: Pablo 3, Lilly 3, Helen 2, Jorlfran 1. Each PR description: what changed, why, how to
test it, and results from executed output.

## Rubric alignment

| Rubric (20 pts each) | Where it is earned | Owners |
|----------------------|--------------------|--------|
| Data science lifecycle | 00 cleaning, 01/02 EDA, 04 to 07 modeling, summary: all phases connected | everyone |
| Reproducibility and technical rigor | pinned env, installable package, tests, data instructions, fresh-clone check (#9) | Pablo, Jorlfran |
| Modeling and evaluation | 04 core models, 05 importance, 06 leakage, 07 tuning, with honest limitations | Pablo, Helen, Jorlfran, Lilly |
| Communication and reporting | executive summary (#8) and labelled figures | Helen |
| GitHub collaboration | 9 PRs across 4 people, review rotation, descriptive commits | everyone |

Collaboration tips: commit small and often on your own branch; use descriptive commit messages
and PR descriptions; each person should also open a GitHub issue for their own task if they
want issue credit (optional, not created for you). Submit the peer-review form individually.

## Timeline

1. **Day 1**: Pablo pushes the modeling PR (#1); Lilly reviews and it merges. Everyone pulls `main`, recreates the env, and runs the load-working skill.
2. **Days 2 to 4**: Lilly (#2, #3), Jorlfran (#4, #5), Helen (#6, #7) in parallel. #3, #5 and #7 need the merged modeling module.
3. **Days 5 to 6**: Helen writes the executive summary (#8) from executed results; reviewers check numbers against notebooks.
4. **Day 7**: Jorlfran runs the fresh-clone check (#9) and fixes what fails.
5. **Before submitting**: each member files the peer-review form; README checklist updated.
