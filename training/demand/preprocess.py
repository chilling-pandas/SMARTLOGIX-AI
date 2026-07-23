from pathlib import Path

import pandas as pd


def load_dataset():
    """
    Load the raw retail inventory dataset.
    """
    project_root = Path(__file__).resolve().parents[2]

    csv_path = (
        project_root
        / "data"
        / "raw"
        / "retail_store_inventory.csv"
    )

    return pd.read_csv(csv_path)


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform basic cleaning and preprocessing.
    """

    # -----------------------------
    # Convert Date column
    # -----------------------------
    df["Date"] = pd.to_datetime(df["Date"])

    # -----------------------------
    # Create date features
    # -----------------------------
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["DayOfWeek"] = df["Date"].dt.dayofweek

    # -----------------------------
    # Remove original date
    # -----------------------------
    # df.drop(columns=["Date"], inplace=True)

    # -----------------------------
    # Demand cannot be negative
    # -----------------------------
    df["Demand Forecast"] = df["Demand Forecast"].clip(lower=0)

    # -----------------------------
    # Remove duplicate rows
    # -----------------------------
    df.drop_duplicates(inplace=True)

    return df