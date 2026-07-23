import pandas as pd


def build_features(data: dict) -> pd.DataFrame:
    return pd.DataFrame([{
        "delivery_partner": data["delivery_partner"],
        "package_type": data["package_type"],
        "vehicle_type": data["vehicle_type"],
        "delivery_mode": data["delivery_mode"],
        "region": data["region"],
        "weather_condition": data["weather_condition"],
        "distance_km": data["distance_km"],
        "package_weight_kg": data["package_weight_kg"],
        "delivery_rating": data["delivery_rating"],
    }])