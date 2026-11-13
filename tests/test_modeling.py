"""Tests for risk_data.modeling (written before the implementation)."""

import numpy as np
import pandas as pd
import pytest

from risk_data import modeling


@pytest.fixture
def frame() -> pd.DataFrame:
    rng = np.random.default_rng(0)
    n = 200
    label = (rng.random(n) < 0.2).astype(int)
    return pd.DataFrame(
        {
            "Company_ID": [f"C{i}" for i in range(n)],
            "Date": "2020-01-01",
            "Industry_Sector": rng.choice(["Tech", "Energy", "Retail"], n),
            "Debt_Equity_Ratio": rng.normal(1, 0.3, n) + label * 2,
            "Revenue": rng.normal(100, 10, n),
            "Financial_Risk_Label": label,
        }
    )


def test_split_features_drops_identifiers_and_target(frame):
    X, y = modeling.split_features(frame)

    assert "Company_ID" not in X.columns
    assert "Date" not in X.columns
    assert "Financial_Risk_Label" not in X.columns
    assert y.name == "Financial_Risk_Label"
    assert len(X) == len(y) == len(frame)


def test_train_test_split_is_stratified_and_reproducible(frame):
    X, y = modeling.split_features(frame)

    a = modeling.make_train_test_split(X, y)
    b = modeling.make_train_test_split(X, y)

    X_train, X_test, y_train, y_test = a
    assert abs(y_train.mean() - y_test.mean()) < 0.03
    assert len(X_test) == pytest.approx(0.2 * len(X), abs=1)
    assert X_train.index.equals(b[0].index)
    assert set(X_train.index).isdisjoint(X_test.index)


def test_build_models_returns_named_pipelines_that_fit(frame):
    X, y = modeling.split_features(frame)

    models = modeling.build_models(X)

    assert {"dummy", "logistic_regression", "random_forest", "gradient_boosting"} <= set(models)
    for model in models.values():
        model.fit(X, y)
        assert model.predict(X).shape == (len(X),)


def test_preprocessing_is_fit_on_training_data_only(frame):
    X, y = modeling.split_features(frame)
    X_train, X_test, y_train, _ = modeling.make_train_test_split(X, y)
    model = modeling.build_models(X)["logistic_regression"]

    model.fit(X_train, y_train)

    scaler = model.named_steps["preprocess"].named_transformers_["num"]
    assert scaler.mean_[0] == pytest.approx(X_train["Debt_Equity_Ratio"].mean())
    assert scaler.mean_[0] != pytest.approx(X["Debt_Equity_Ratio"].mean())


def test_unseen_category_does_not_crash(frame):
    X, y = modeling.split_features(frame)
    model = modeling.build_models(X)["logistic_regression"].fit(X, y)
    new = X.head(3).copy()
    new["Industry_Sector"] = "Unknown"

    assert model.predict(new).shape == (3,)


def test_evaluate_returns_expected_metrics(frame):
    X, y = modeling.split_features(frame)
    X_train, X_test, y_train, y_test = modeling.make_train_test_split(X, y)
    model = modeling.build_models(X)["logistic_regression"].fit(X_train, y_train)

    metrics = modeling.evaluate(model, X_test, y_test)

    assert set(metrics) == {"precision", "recall", "f1", "roc_auc", "pr_auc"}
    assert all(0 <= v <= 1 for v in metrics.values())
    assert metrics["roc_auc"] > 0.8


def test_cross_validate_models_returns_one_row_per_model(frame):
    X, y = modeling.split_features(frame)

    table = modeling.cross_validate_models(modeling.build_models(X), X, y, n_splits=3)

    assert list(table.index) == list(modeling.build_models(X))
    assert {"roc_auc_mean", "pr_auc_mean", "f1_mean"} <= set(table.columns)


def test_load_model_data_missing_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        modeling.load_model_data(tmp_path / "nope.csv")
