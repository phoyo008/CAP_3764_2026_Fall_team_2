# Executive Summary Report

Team Number: 2
Date: November 15, 2026
Subject: Corporate Financial Risk Assessment

## Project Goal

Our goal was to identify financial characteristics associated with companies being labeled at risk and compare classification models. The findings help us understand this dataset, but do not establish that we can predict future financial distress.

## Major Findings

We started with 5,000 records and removed 1,425 exact duplicates, leaving 3,575 companies. No missing values were found. Of these companies, 575 (16.08%) were labeled at risk, so we focused on precision, recall, and average precision (AP) rather than accuracy alone.

Table 1. Test Results for Selected Model Comparisons

| Model | ROC-AUC | Test AP | Recall |
|---|---:|---:|---:|
| Logistic all | 0.968 | 0.890 | 0.922 |
| Boosting all | 1.000 | 1.000 | 0.991 |
| Boosting reduced | 0.607 | 0.378 | 0.226 |

The all-features models scored very highly, but we should be cautious: they may be learning the way the labels were created. Our feature importance analysis showed that the original gradient boosting model relied most on debt-to-equity ratio.

Removing debt-to-equity ratio, cash flow, and total liabilities and retraining reduced test AP to 0.378, versus a 0.161 constant-score baseline. Net income became the most important remaining input. At the default threshold, the reduced model identified only 22.6% of at-risk test companies. Its above-baseline ranking score therefore does not mean it catches most at-risk companies.

## Recommendations

1. Complete the label-sensitivity analysis to check whether the high scores mainly reflect how the labels were assigned.
2. Keep the current models exploratory. Before practical use, confirm label definitions and test on independent or later-period data.
3. Choose any future decision threshold around the cost of missed risk versus false alarms, using training data rather than repeated test-set adjustments.
4. Finish the tuning interpretation review and the team's fresh-clone reproducibility check before submission.

## Analytical Overview

We used a stratified 80/20 split with a fixed seed: 2,860 training records and 715 test records, including 115 at-risk test companies. We compared a baseline, logistic regression, random forest, and gradient boosting. Scaling and sector encoding were fitted inside training pipelines and five-fold cross-validation. Permutation importance measured the score decrease after shuffling an input. A separate tuning notebook reproduced only a tiny logistic-regression change in test AP (0.3415 to 0.3416), with no change for gradient boosting; its interpretation remains under review.

## Risks and Limitations

Feature importance measures model reliance, not causes of distress. Related inputs such as net income and cash flow may substitute for one another; removing three columns does not prove label-related information is gone. Companies appear once across 40 quarter-end dates from 2015 to 2024, without company histories or a future target for forecasting. Test-set reuse limits independent validation claims. Label provenance, sensitivity results, and external validation remain unresolved.
