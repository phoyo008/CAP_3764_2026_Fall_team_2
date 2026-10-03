"""Download the Corporate Financial Risk Assessment dataset from Kaggle.

Owner: Pablo (feature/data-collection)
"""

import shutil
from pathlib import Path

import kagglehub

RAW_DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"
DATASET_HANDLE = "zoya77/corporate-financial-risk-assessment-dataset"


def collect(dest_dir: Path = RAW_DATA_DIR) -> Path:
    """Download the raw dataset into dest_dir via kagglehub and return its path.

    The files land in ``dest_dir/<dataset-name>/``, which is where
    ``risk_data.clean.clean`` looks for the CSV (it searches recursively).
    """
    cache_path = Path(kagglehub.dataset_download(DATASET_HANDLE))

    target = Path(dest_dir) / DATASET_HANDLE.split("/")[-1]
    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(cache_path, target, dirs_exist_ok=True)

    csv_files = list(target.rglob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"Download finished but no CSV found in {target}")

    print(f"Dataset saved to {target}")
    return target


if __name__ == "__main__":
    collect()
