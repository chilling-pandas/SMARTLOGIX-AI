import numpy as np

TRAFFIC_MAP = {"LOW": 1, "MEDIUM": 2, "HIGH": 3}
WEATHER_MAP = {"CLEAR": 0, "RAIN": 1}
VEHICLE_MAP = {"BIKE": 1, "VAN": 2, "TRUCK": 3}

def build_features(data: dict) -> np.ndarray:
    return np.array([[
        data["distance_km"],
        TRAFFIC_MAP[data["traffic_level"]],
        WEATHER_MAP[data["weather"]],
        VEHICLE_MAP[data["vehicle_type"]],
    ]])
