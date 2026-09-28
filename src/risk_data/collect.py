"""Download the Corporate Financial Risk Assessment dataset from Kaggle.

Owner: Helen (feature/data-collection)
"""

from pathlib import Path

RAW_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"


def collect(dest_dir: Path = RAW_DATA_DIR) -> Path:
    """Download the raw dataset into dest_dir via kagglehub and return its path."""
    raise NotImplementedError("TODO(Helen): download via kagglehub, save into data/raw/")


if __name__ == "__main__":
    collect()
