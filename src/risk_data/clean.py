"""Clean the raw Corporate Financial Risk Assessment dataset.

Owner: Lilly (feature/data-cleaning)
"""

from pathlib import Path

import pandas as pd

RAW_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
PROCESSED_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "processed"


def clean(raw_dir: Path = RAW_DATA_DIR, processed_dir: Path = PROCESSED_DATA_DIR) -> pd.DataFrame:
    """Deduplicate rows, handle missing values, and fix dtypes; return the cleaned DataFrame."""
    raise NotImplementedError("TODO(Lilly): dedup, handle missing values, convert dtypes")


if __name__ == "__main__":
    clean()
