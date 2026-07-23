from pydantic import BaseModel
from typing import List


class EtaRequest(BaseModel):
    delivery_partner: str
    package_type: str
    vehicle_type: str
    delivery_mode: str
    region: str
    weather_condition: str

    distance_km: float
    package_weight_kg: float
    delivery_rating: float


class EtaResponse(BaseModel):
    estimated_time_minutes: float
    confidence: float


class RouteOption(BaseModel):
    route_id: str
    distance_km: float
    traffic_level: str


class BestRouteRequest(BaseModel):
    routes: List[RouteOption]
    weather: str
    vehicle_type: str


class BestRouteResponse(BaseModel):
    best_route_id: str
    estimated_time_minutes: float
    reason: str