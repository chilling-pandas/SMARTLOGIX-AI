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

    eta = eta_model.predict(X)

    shipment = Shipment(
        delivery_partner=request.delivery_partner,
        package_type=request.package_type,
        vehicle_type=request.vehicle_type,
        delivery_mode=request.delivery_mode,
        region=request.region,
        weather_condition=request.weather_condition,
        distance_km=request.distance_km,
        package_weight_kg=request.package_weight_kg,
        delivery_rating=request.delivery_rating,
        actual_time=eta
    )

    db.add(shipment)
    db.commit()
    db.refresh(shipment)


    eta_hours = eta
    return EtaResponse(
         estimated_time_minutes=round(eta_hours * 60, 2),
         confidence=0.75
    )