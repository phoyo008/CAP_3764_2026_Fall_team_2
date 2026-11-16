# Executive Summary Report

Team Number: 2
Date: November 15, 2026
Subject: Corporate Financial Risk Assessment

## Project Goal

Our goal was to compare financial risk classification models and identify the inputs they rely on. Risk screening could help lenders prioritize further review, but these results do not show that the models can predict future financial distress.

## Major Findings

We removed 1,425 exact duplicates from 5,000 records, leaving 3,575 companies with no missing values. Of these companies, 575 (16.08%) were labeled at risk. Because this group was relatively small, we focused on precision, recall, and average precision (AP) rather than accuracy alone.

Table 1. Test Results Using the Reduced Feature Set

| Model | ROC-AUC | Test AP | Recall |
|---|---:|---:|---:|
| Logistic | 0.633 | 0.342 | 0.522 |
| Random forest | 0.607 | 0.369 | 0.200 |
| Grad. boosting | 0.607 | 0.378 | 0.226 |

With all features, random forest and gradient boosting achieved test AP of 1.000. However, a simple debt-to-equity and cash flow rule reproduced every test label, suggesting the models learned the labeling process. These scores do not establish real-world predictive performance.

After removing debt-to-equity ratio, cash flow, and total liabilities, gradient boosting had the highest reduced-set AP (0.378), versus a 0.161 baseline. Net income became its most important input. Its 22.6% recall means it missed nearly four out of five at-risk test companies, making it unsuitable for stand-alone screening at the default threshold.

## Recommendations for Action

1. Collect independently verified financial outcomes and test the reduced models on those records. Do not use the current scores alone to approve or deny credit.
2. Confirm how the risk labels were defined and whether the inputs would be available before the outcome being predicted.
3. Select a classification threshold based on the costs of missed risk and false alarms. Use training data for this decision to avoid repeatedly adjusting the model based on test results.
4. Use these findings to guide further research. The models need stronger validation before they can support lending or investment decisions.

## Analytical Overview

We used a stratified 80/20 split with a fixed random seed: 2,860 training records and 715 test records, including 115 at-risk test companies. We compared a baseline model, logistic regression, random forest, and gradient boosting. During five-fold cross-validation, preprocessing was fitted using only the training data in each fold. Feature importance measured the decrease in AP after shuffling an input. Tuning used training data only. Test AP for logistic regression was essentially unchanged (0.3415 to 0.3416); gradient boosting was unchanged. This search found no meaningful improvement.

## Risks/Limitations

Feature importance shows model reliance, not causes of financial distress. Other inputs may still contain information related to the removed features. Each company has one observation, with dates spanning 40 quarter ends from 2015 to 2024. The dataset lacks company histories and a future outcome for time series forecasting. Reusing the test set limits independent validation. The origin of the labels remains unconfirmed, and performance on independent real-world data has not been established.
