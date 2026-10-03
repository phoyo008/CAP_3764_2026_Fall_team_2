# CAP 3764 — Corporate Financial Risk Assessment (Team 2)

Final project for CAP 3764, Fall 2026. This first submission covers repo setup,
data collection, cleaning, and initial EDA — modeling/forecasting comes later
(Module 8).

**Dataset:** [Corporate Financial Risk Assessment Dataset](https://www.kaggle.com/datasets/zoya77/corporate-financial-risk-assessment-dataset)
(Kaggle) — 5,000 company-quarter records, 20 columns covering financial figures
(Total_Assets, Revenue, Debt_Equity_Ratio, ...), macro indicators (GDP_Growth_Rate,
Inflation_Rate), Industry_Sector, and a binary Financial_Risk_Label.

## Setup

```bash
git clone https://github.com/phoyo008/CAP_3764_2026_Fall_team_2.git
cd CAP_3764_2026_Fall_team_2

conda env create -f environment.yml
conda activate cap3764-risk

python -m ipykernel install --user --name cap3764-risk --display-name "Python (cap3764-risk)"

jupyter lab
```

In JupyterLab, select the **Python (cap3764-risk)** kernel for any notebook in this project.

## Project Structure

```
data/
├── raw/              # untouched downloads (gitignored)
└── processed/        # cleaned datasets (gitignored)
notebooks/            # exploratory / EDA notebooks
reports/figures/      # exported charts and figures
src/risk_data/
├── collect.py         # Kaggle download via kagglehub
└── clean.py            # dedup, missing values, dtype conversion
```

## Team & Task Breakdown

| Person   | Branch                    | Task                                                      |
|----------|---------------------------|-------------------------------------------------------------|
| Pablo  (done)  | setup/scaffolding         | Repo structure, conda env, .gitignore, module stubs, README |
| Pablo  (done)  | feature/data-collection   | `collect.py` — automated download via kagglehub (done)      |
| Helen    | feature/eda-numerical     | Numeric summary stats, correlation heatmap, distribution plots |
| Lilly (done)   | feature/data-cleaning     | `clean.py` — dedup, missing values, dtype conversion         |
| Jorlfran | feature/eda-categorical   | Categorical breakdowns, summary tables, visualizations       |

**Merge order:** `setup/scaffolding` merges first (creates the structure everyone
else builds on), then the other branches proceed in parallel.
