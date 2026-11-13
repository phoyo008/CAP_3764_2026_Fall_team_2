# Modeling notes (hand-off for notebooks 05, 06, 07 and the report)

Context from `04_modeling.ipynb` and `src/risk_data/modeling.py`. Use these as a starting
point, then write your own notebook, run it, and interpret **your own** output.

## What exists
- `risk_data.modeling`: `load_model_data`, `split_features`, `make_train_test_split`,
  `build_models`, `cross_validate_models`, `evaluate` (all tested in `tests/test_modeling.py`).
- Split: stratified 80/20, `random_state=42`. Models: dummy, logistic regression, random forest,
  gradient boosting, each a Pipeline (scale + one-hot inside, so no leakage), class weights for the 84/16 imbalance.
- Metrics: precision, recall, F1, ROC-AUC, PR-AUC. Accuracy is not used (84% by always predicting "safe").
- Always use the same split: `X, y = split_features(load_model_data())` then `make_train_test_split(X, y)`.

## Key finding (drives notebooks 05 to 07 and the report)
All-features results are suspiciously perfect (random forest and gradient boosting: ROC-AUC about 1.0).
A quick check shows why: the label looks rule-generated.

- No "not at risk" company has `Debt_Equity_Ratio` above 2.50; every company above 2.50 is at risk.
- A depth-2 decision tree on `Debt_Equity_Ratio` and `Cash_Flow` reproduces most labels.
- `Total_Liabilities` is tied to debt-to-equity by accounting.

So tree models mostly rediscover the labelling rule rather than predict real risk.
Without `Debt_Equity_Ratio`, `Cash_Flow` and `Total_Liabilities`, cross-validated PR-AUC falls to
about 0.32 (logistic regression) and about 0.41 (random forest, gradient boosting) vs a 0.16
no-skill level: some real signal, but weak. These numbers came from one exploratory run;
**re-derive them in your own notebook and report what you get.**

## Notebook briefs

| Notebook | Owner | Do |
|----------|-------|----|
| `05_feature_importance.ipynb` | Helen | Permutation importance (scoring `average_precision`) on the test set for the gradient boosting model, on all features and on the reduced set; bar chart saved to `reports/figures/`; 3 to 5 sentences on what drives risk and what a business reader should take from it |
| `06_leakage_and_sensitivity.ipynb` | Jorlfran | Show the evidence that the label is rule-like (depth-2 tree, `Debt_Equity_Ratio` ranges by class); drop the suspect features, re-run `cross_validate_models` and test `evaluate`; chart comparing all-features vs reduced; state clearly which result should be reported and why. Check whether dropping `Total_Liabilities` is needed or whether only the first two features are enough |
| `07_tuning.ipynb` | Lilly | Reduced feature set only. `GridSearchCV` (scoring `average_precision`, same `StratifiedKFold`) on logistic regression (`C`) and gradient boosting (learning rate, depth, iterations); report best params, CV vs test PR-AUC, and whether tuning helped |

Report writer (Helen): quote only numbers that appear in executed notebook output.
