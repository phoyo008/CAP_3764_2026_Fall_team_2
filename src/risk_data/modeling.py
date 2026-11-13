"""Model building and evaluation for Financial_Risk_Label.

Owner: Pablo (feature/modeling)

All preprocessing lives inside sklearn Pipelines, so scaling and encoding are fit on
training data only (no leakage), including inside each cross-validation fold.
"""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    f1_score,
    make_scorer,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

PROCESSED_DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "processed" / "cleaned_data.csv"
TARGET = "Financial_Risk_Label"
IDENTIFIER_COLUMNS = ["Company_ID", "Date"]
CATEGORICAL_COLUMNS = ["Industry_Sector"]
RANDOM_STATE = 42
TEST_SIZE = 0.2
CV_SPLITS = 5
CV_SCORING = {
    "roc_auc": "roc_auc",
    "pr_auc": "average_precision",
    "f1": make_scorer(f1_score, zero_division=0),
    "precision": make_scorer(precision_score, zero_division=0),
    "recall": make_scorer(recall_score, zero_division=0),
}


def load_model_data(path: Path = PROCESSED_DATA_PATH) -> pd.DataFrame:
    """Load the cleaned dataset produced by ``risk_data.clean``."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Run collect.py and clean.py first (see README)."
        )
    return pd.read_csv(path)


def split_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Return (X, y), dropping identifiers (one row per company, no signal) and the target."""
    X = df.drop(columns=[TARGET, *IDENTIFIER_COLUMNS], errors="ignore")
    return X, df[TARGET]


def make_train_test_split(
    X: pd.DataFrame, y: pd.Series, test_size: float = TEST_SIZE, random_state: int = RANDOM_STATE
):
    """Stratified train/test split so both parts keep the ~16% at-risk rate."""
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    """Scale numeric columns and one-hot encode categorical ones."""
    categorical = [c for c in CATEGORICAL_COLUMNS if c in X.columns]
    numeric = [c for c in X.columns if c not in categorical]
    return ColumnTransformer(
        [
            ("num", StandardScaler(), numeric),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ]
    )


def build_models(X: pd.DataFrame, random_state: int = RANDOM_STATE) -> dict[str, Pipeline]:
    """Baseline plus three classifiers, each handling class imbalance via class weights."""
    estimators = {
        "dummy": DummyClassifier(strategy="prior"),
        "logistic_regression": LogisticRegression(
            class_weight="balanced", max_iter=1000, random_state=random_state
        ),
        "random_forest": RandomForestClassifier(
            n_estimators=300,
            min_samples_leaf=5,
            class_weight="balanced",
            n_jobs=-1,
            random_state=random_state,
        ),
        "gradient_boosting": HistGradientBoostingClassifier(
            class_weight="balanced", random_state=random_state
        ),
    }
    return {
        name: Pipeline([("preprocess", build_preprocessor(X)), ("model", est)])
        for name, est in estimators.items()
    }


def cross_validate_models(
    models: dict[str, Pipeline],
    X: pd.DataFrame,
    y: pd.Series,
    n_splits: int = CV_SPLITS,
    random_state: int = RANDOM_STATE,
) -> pd.DataFrame:
    """Stratified k-fold CV; returns mean and std of each metric per model."""
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
    rows = {}
    for name, model in models.items():
        scores = cross_validate(model, X, y, cv=cv, scoring=CV_SCORING)
        row = {}
        for metric in CV_SCORING:
            values = scores[f"test_{metric}"]
            row[f"{metric}_mean"] = values.mean()
            row[f"{metric}_std"] = values.std()
        rows[name] = row
    return pd.DataFrame.from_dict(rows, orient="index")


def evaluate(model: Pipeline, X_test: pd.DataFrame, y_test: pd.Series) -> dict[str, float]:
    """Metrics on held-out data. Accuracy is omitted on purpose: 84% is achievable by guessing."""
    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]
    return {
        "precision": precision_score(y_test, pred, zero_division=0),
        "recall": recall_score(y_test, pred, zero_division=0),
        "f1": f1_score(y_test, pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, proba),
        "pr_auc": average_precision_score(y_test, proba),
    }
