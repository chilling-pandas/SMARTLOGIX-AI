from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.database import get_db
from backend.app.schemas.shipping import EtaRequest, EtaResponse
from backend.app.models.shipment import Shipment

from ai_engine.route_eta.features import build_features
from ai_engine.route_eta.model import EtaModel

router = APIRouter()

# Load model once
eta_model = EtaModel("ai_engine/route_eta/eta_model.pkl")


@router.post("/predict-eta", response_model=EtaResponse)
def predict_eta(
    request: EtaRequest,
    db: Session = Depends(get_db)
):
    X = build_features(request.dict())
    eta = eta_model.predict(X)   # ✅ correct variable

    shipment = Shipment(
        source_id=request.source_id,
        destination_id=request.destination_id,
        distance_km=request.distance_km,
        traffic_level=request.traffic_level,
        weather=request.weather,
        vehicle_type=request.vehicle_type,
        actual_time=eta
    )

    db.add(shipment)
    db.commit()
    db.refresh(shipment)

    return EtaResponse(
        estimated_time_minutes=eta,
        confidence=0.75
    )
