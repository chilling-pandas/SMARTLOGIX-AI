from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.models.prediction import Prediction
from backend.app.models.shipment import Shipment

router = APIRouter()

# ---------------------------
# Demand Prediction History
# ---------------------------
@router.get("/history/demand")
def demand_history(db: Session = Depends(get_db)):
    records = db.query(Prediction).order_by(Prediction.created_at.desc()).limit(50).all()
    return [
        {
            "product_id": r.product_id,
            "warehouse_id": r.warehouse_id,
            "predicted_demand": r.predicted_demand,
            "confidence": r.confidence,
            "created_at": r.created_at
        }
        for r in records
    ]


# ---------------------------
# ETA / Shipment History
# ---------------------------
@router.get("/history/shipments")
def shipment_history(db: Session = Depends(get_db)):
    records = db.query(Shipment).order_by(Shipment.id.desc()).limit(50).all()

    return [
        {
            "delivery_partner": r.delivery_partner,
            "package_type": r.package_type,
            "vehicle_type": r.vehicle_type,
            "delivery_mode": r.delivery_mode,
            "region": r.region,
            "weather_condition": r.weather_condition,
            "distance_km": r.distance_km,
            "package_weight_kg": r.package_weight_kg,
            "delivery_rating": r.delivery_rating,
            "eta_minutes": r.actual_time,
            "created_at": r.created_at
        }
        for r in records
    ]
