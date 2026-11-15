# Executive summary: Corporate Financial Risk Assessment

**Draft for team review — sensitivity analysis and final reproducibility checks are pending.**

## Objective

Assess which company financial characteristics are associated with `Financial_Risk_Label` and evaluate whether classifiers can identify companies labeled at risk. The label has no documented future prediction horizon; this project does not establish the ability to forecast future distress or default.

## Data and preparation

The Kaggle dataset contains 5,000 records and 20 columns. Shared cleaning removed 1,425 exact duplicates, leaving 3,575 companies with no missing values. Each company appears once. Although records span 40 quarter-end dates from 2015 to 2024, they do not form repeated company histories suitable for company-level time series forecasting. There are 575 at-risk companies (16.08%), making accuracy alone an inadequate measure of usefulness.

## Methods

The team used a reproducible, stratified 80/20 split: 2,860 training records and 715 test records, including 115 at-risk test companies. Models included a constant-score baseline, logistic regression, random forest, and gradient boosting. Scaling and sector encoding were fitted inside training pipelines, including during five-fold cross-validation. Evaluation included precision, recall, F1, ROC-AUC, and average precision (AP), the precision–recall measure called PR-AUC in the notebooks. Permutation importance measured how test AP changed when an input was shuffled.

## Findings

With all features, logistic regression achieved test AP 0.890, precision 0.671, and recall 0.922. Random forest achieved test AP 1.000; gradient boosting also achieved AP 1.000. These high scores require caution: they may reflect reconstruction of the dataset's labeling rule rather than real-world financial-risk prediction.

The all-features gradient boosting model relied most on debt-to-equity ratio: shuffling it reduced AP by 0.772 on average. Following the team's prespecified comparison, removing debt-to-equity ratio, cash flow, and total liabilities reduced the refitted model's test AP to 0.378, compared with a constant-score baseline of 0.161. Net income became the strongest remaining input, but it may act as a proxy for cash flow. Feature importance measures model reliance, not causation.

The reduced model's precision was 0.394 and recall 0.226 at the default threshold. Thus, its above-baseline ranking score does not translate into reliably identifying most at-risk companies at that threshold.

The independently rerun tuning notebook found only a tiny logistic-regression change: test AP 0.3415 to 0.3416. Gradient boosting remained at AP 0.3784. This search found no meaningful improvement; it does not rule out benefits from other settings or models. The tuning interpretation is still under review.

## Implications and limitations

The current models are exploratory tools for understanding this dataset, not validated lending or investment decision systems. Removing three suspected inputs does not prove that label-related information has been eliminated. Reuse of the same test sample across analyses also limits claims of independent validation.

Before final submission, incorporate the team's label-sensitivity analysis, resolve the tuning interpretation review, and complete the fresh-clone reproducibility check. Before practical use, establish label provenance, information availability at prediction time, and performance on independent or later-period data. Report the near-perfect scores with these limitations rather than as evidence of forecasting ability.

## Evidence

Executed results: [numerical EDA](../notebooks/01_eda_numerical.ipynb), [core modeling](../notebooks/04_modeling.ipynb), and [feature importance](../notebooks/05_feature_importance.ipynb). Tuning results were reproduced from [PR #25](https://github.com/phoyo008/CAP_3764_2026_Fall_team_2/pull/25) at commit `90f431e`; its interpretation review and the sensitivity analysis remain pending.
