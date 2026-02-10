from pydantic import BaseModel
from typing import List

class EtaRequest(BaseModel):
    source_id: int
    destination_id: int
    distance_km: float
    traffic_level: str      # LOW / MEDIUM / HIGH
    weather: str            # CLEAR / RAIN
    vehicle_type: str       # BIKE / VAN / TRUCK


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
