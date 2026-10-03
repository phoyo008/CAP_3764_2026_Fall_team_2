# CAP 3764 — Corporate Financial Risk Assessment (Team 2)

Final project for CAP 3764, Fall 2026. This first submission covers repo setup,
data collection, cleaning, and initial EDA — modeling/forecasting comes later
(Module 8).

**Dataset:** [Corporate Financial Risk Assessment Dataset](https://www.kaggle.com/datasets/zoya77/corporate-financial-risk-assessment-dataset)
(Kaggle) — 5,000 company records (3,575 after cleaning), 20 columns covering financial figures
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

## Dataset at a Glance

| Item | Detail |
|------|--------|
| Source | Kaggle — `zoya77/corporate-financial-risk-assessment-dataset` |
| Raw size | 5,000 rows x 20 columns |
| Time span | 2015-03-31 to 2024-12-31 (`Date`) |
| Numerical variables | Total_Assets, Total_Liabilities, Current_Assets, Current_Liabilities, Net_Income, Revenue, Operating_Income, Cash_Flow, Debt_Equity_Ratio, Return_on_Assets, Working_Capital_Ratio, Stock_Price_Close, Volatility_Index, GDP_Growth_Rate, Interest_Rate, Inflation_Rate |
| Categorical variables | Industry_Sector (6 sectors), Financial_Risk_Label (0/1, 1 = at risk) |
| Identifiers | Company_ID, Date |
| Class balance | ~16.1% at risk, ~83.9% not at risk |

**Project goal:** understand which financial and macroeconomic characteristics are associated
with a company being labeled financially at risk, as groundwork for the modeling stage.

## Setup

```bash
git clone https://github.com/phoyo008/CAP_3764_2026_Fall_team_2.git
cd CAP_3764_2026_Fall_team_2

conda env create -f environment.yml
conda activate cap3764-risk

python -m ipykernel install --user --name cap3764-risk --display-name "Python (cap3764-risk)"
```

## Reproduce the Analysis

Run from the project root inside the `cap3764-risk` environment:

```bash
python src/risk_data/collect.py   # 1. download raw data from Kaggle -> data/raw/
python src/risk_data/clean.py     # 2. clean -> data/processed/cleaned_data.csv
jupyter lab                       # 3. open the notebooks with the "Python (cap3764-risk)" kernel
```

Data files are gitignored, so steps 1-2 must be run once on each machine.

## Project Structure

```
data/
├── raw/                          # untouched downloads (gitignored)
└── processed/                    # cleaned datasets (gitignored)
notebooks/
├── eda_numerical.ipynb           # numerical EDA (Helen)
└── 02_eda_categorical.ipynb      # categorical EDA (Jorlfran)
reports/figures/                  # exported numerical charts
src/risk_data/
├── collect.py                    # Kaggle download via kagglehub (Pablo)
└── clean.py                      # dedup, dtype conversion, median fill (Lilly)
environment.yml                   # conda environment (cap3764-risk)
```

## Data Collection & Cleaning

- `collect.py` automates the download with `kagglehub` and copies the CSV into `data/raw/`.
- `clean.py` reports missing values (none found), drops duplicate `Company_ID`/`Date`
  rows (**1,425 removed, 5,000 -> 3,575**), converts `Date` to datetime and
  `Industry_Sector`/`Financial_Risk_Label` to categorical, fills any numeric gaps with the
  median, and asserts no duplicates or NaNs remain.
- After cleaning, each `Company_ID` appears once, so the data behaves as a cross-section
  rather than a company time series.

## Exploratory Data Analysis

**Numerical** (`notebooks/eda_numerical.ipynb`): summary statistics (mean, median, std, skew,
kurtosis) for every numeric column, histograms/KDE and box plots, correlation heatmap,
financial ratios by risk label, IQR outlier audit, and a raw-vs-cleaned row audit.
Figures are saved to `reports/figures/numerical_*.png`.

**Categorical** (`notebooks/02_eda_categorical.ipynb`): counts and proportions for
`Industry_Sector` and `Financial_Risk_Label`, mean ratios and at-risk rate by sector,
static bar charts, one interactive Plotly chart, and a chi-square test.

Preliminary insights:
- Finance has the highest at-risk rate (19.2%) vs. 16.1% overall; Retail (14.0%) and
  Technology (14.5%) are lowest.
- The sector differences are **not statistically significant** (chi-square p = 0.18).
- Ratio differences between sectors are small and inconsistent.

## Team & GitHub Workflow

| Person   | Branch                    | Task                                                         | PR |
|----------|---------------------------|--------------------------------------------------------------|----|
| Pablo    | setup/scaffolding         | Repo structure, conda env, .gitignore, module stubs, README  | #1, #2 |
| Pablo    | feature/data-collection   | `collect.py` — automated download via kagglehub              | #5 |
| Lilly    | feature/data-cleaning     | `clean.py` — dedup, missing values, dtype conversion         | #3 |
| Helen    | feature/eda-numerical     | Summary stats, distributions, correlations, outliers         | #7 |
| Jorlfran | feature/eda-categorical   | Categorical breakdowns, summary tables, visualizations       | #6 |

Every task was developed on its own branch and merged into `main` through a pull request.

## Next Steps

- Decide how to treat the 1,425 removed duplicates and the extreme values flagged by the IQR audit.
- Feature engineering and a baseline classifier for `Financial_Risk_Label`, handling the 84/16 class imbalance.
- Check whether macro indicators (GDP, interest, inflation) add signal beyond company ratios.

## Submission Checklist

- [x] Team repo, per-task branches, pull requests
- [x] Conda environment and `environment.yml`
- [x] Data collection module and initial cleaning
- [x] Numerical and categorical EDA with tables and visualizations
- [ ] Slide deck
- [ ] 10-minute YouTube video: link — _TBD_
- [ ] Peer-review forms (each member)
