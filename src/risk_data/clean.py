"""Clean the raw Corporate Financial Risk Assessment dataset.

Owner: Lilly (feature/data-cleaning)
"""

from pathlib import Path

import pandas as pd

RAW_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
PROCESSED_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the corporate financial risk DataFrame and return the cleaned copy."""
    df = df.copy()

    # 1. Check missing values first (in case a column needs a different strategy)
    print("Missing values per column:")
    print(df.isna().sum())

    # 2. Drop duplicate (Company_ID, Date) rows
    before = len(df)
    df = df.drop_duplicates(subset=["Company_ID", "Date"])
    print(f"Dropped {before - len(df)} duplicate rows")

    # 3. Convert types
    df["Date"] = pd.to_datetime(df["Date"])
    df["Industry_Sector"] = df["Industry_Sector"].astype("category")
    df["Financial_Risk_Label"] = df["Financial_Risk_Label"].astype("category")

    # 4. Fill missing numeric values with the median
    num_cols = df.select_dtypes(include="number").columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # 5. Sanity checks
    assert not df.duplicated(subset=["Company_ID", "Date"]).any(), "Duplicates remain"
    assert df[num_cols].isna().sum().sum() == 0, "NaNs remain in numeric columns"

    return df


def clean(raw_dir: Path = RAW_DATA_DIR, processed_dir: Path = PROCESSED_DATA_DIR) -> pd.DataFrame:
    """Load the raw CSV, clean it, save it to the processed folder, and return it."""
    # kagglehub saves the file in a dataset subfolder, so search recursively
    # (and skip Jupyter checkpoint copies of the CSV).
    csv_files = sorted(
        p for p in Path(raw_dir).rglob("*.csv") if ".ipynb_checkpoints" not in p.parts
    )
    if not csv_files:
        raise FileNotFoundError(f"No CSV file found in {raw_dir}")

    df = pd.read_csv(csv_files[0])
    df = clean_data(df)

    processed_dir = Path(processed_dir)
    processed_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed_dir / "cleaned_data.csv", index=False)

    return df


if __name__ == "__main__":
    cleaned = clean()
    print(f"Cleaned data shape: {cleaned.shape}")
