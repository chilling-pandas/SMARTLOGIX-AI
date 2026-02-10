import numpy as np

def build_features(data: dict) -> np.ndarray:
    """
    Convert input dictionary into ML feature vector
    """
    return np.array([[
        data["avg_7_day_sales"],
        data["avg_30_day_sales"],
        data["stock_level"],
        data["demand_variance"]
    ]])

