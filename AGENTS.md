# AGENTS.md: CAP 3764 Team 2 (Corporate Financial Risk)

Instructions for any AI coding agent (Claude Code, Codex, etc.) working in this repo.
Humans: read it too, it is the team contract.

## Project

Predict/understand `Financial_Risk_Label` (binary, ~16% positive) from company financials and
macro indicators. Pipeline: collect -> clean -> EDA -> model -> executive summary.
Dataset: Kaggle `zoya77/corporate-financial-risk-assessment-dataset` (5,000 rows, 3,575 after cleaning).

## Source of truth for tasks

`docs/TEAM_WORKFLOW.md` lists who owns which task, its branch name, deliverable, and who reviews it.
**Work only on the task assigned to the person you are helping.** If asked to do something that
belongs to someone else, say so and stop; suggest they ping the owner.

## Environment

- Conda env file: `environment-cap3764-final-project.yml` (env name `cap3764-risk`, kernel "Python (cap3764-risk)").
- All versions are pinned. If you need a new package: add it to the yml with a pinned version, mention it in the PR, never `pip install` ad hoc and move on.
- `src/risk_data/` is an installed package (`pip install -e .`). Notebooks must `from risk_data...` for loading and cleaning, not re-implement it.

## Repo layout

```
src/risk_data/   reusable code (collect, clean, modeling ...)
notebooks/       00_data_cleaning, 01_eda_numerical, 02_eda_categorical, 04_modeling (numbered, in lifecycle order)
reports/         figures/ and executive_summary.md
data/raw, data/processed   gitignored, recreate with collect.py and clean.py. NEVER commit data.
docs/            TEAM_WORKFLOW.md
```

## Rules

1. **Git**: never commit to `main`; one branch per task using the branch name in the workflow doc; conventional commits (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`); small, frequent commits so history shows real progress. Never force-push, never rewrite others' work, never push without the user saying so.
2. **Stay in scope**: touch only files that belong to your task. Do not reformat or "improve" other people's notebooks/modules. Unrelated problems go in the PR description, not in the diff.
3. **Notebooks**: markdown header per section, short comments explaining *why*, no leftover debug cells, no `Untitled*.ipynb`, must pass *Restart & Run All* from a clean kernel. Clear nothing the author needs, but do not commit huge outputs.
4. **Reproducibility**: fixed `random_state`, relative paths via `Path`, no absolute paths, no secrets or Kaggle credentials in the repo.
5. **Modeling** (if your task): stratified split, no leakage (fit preprocessing on train only), report precision/recall/F1/ROC-AUC/PR-AUC rather than accuracy alone, state limitations honestly.
6. **Reporting**: numbers in prose must come from executed notebook output, never invented. Executive summary max 600 words.
7. **Be honest**: if something fails or was not run, say so. Do not claim it passed.
8. Do not add files in the repo root. Do not commit `.pptx`, caches, or checkpoints.

## Slash commands (skills)

- `/load-working`: sync with `main`, find my assigned task, set up the branch, and do the task.
- `/cap3764-handoff`: verify, commit, push, and leave the PR description ready for the reviewer.
