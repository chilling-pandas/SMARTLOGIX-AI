import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create the features expected by the Demand API.
    """

    # Sort by product and date
    df = df.sort_values(["Product ID", "Date"]).copy()

    # Rolling averages
    df["avg_7_day_sales"] = (
    df.groupby("Product ID")["Units Sold"]
      .transform(lambda x: x.shift(1).rolling(7, min_periods=7).mean())
    )
    
    df["avg_30_day_sales"] = (
        df.groupby("Product ID")["Units Sold"]
          .transform(lambda x: x.shift(1).rolling(30, min_periods=30).mean())
    )
# -----------------------------
# Current stock level
# -----------------------------
    df["stock_level"] = df["Inventory Level"]
    
    df["demand_variance"] = (
        df.groupby("Product ID")["Units Sold"]
          .transform(lambda x: x.shift(1).rolling(30, min_periods=1).var())
          .fillna(0)
    )
    
    # Create classification target
    def demand_label(x):
        if x <= 53:
            return "LOW"
        elif x <= 208:
            return "MEDIUM"
        return "HIGH"

    df["target"] = df["Demand Forecast"].apply(demand_label)

    df.dropna(
    subset=[
        "avg_7_day_sales",
        "avg_30_day_sales"
    ],
    inplace=True
)

    # Keep only the columns used by the API + target
    final_df = df[
        [
            "avg_7_day_sales",
            "avg_30_day_sales",
            "stock_level",
            "demand_variance",
            "target",
        ]
    ].copy()

    return final_df