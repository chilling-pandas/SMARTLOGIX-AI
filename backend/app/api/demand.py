from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.core.database import get_db
from backend.app.models.prediction import Prediction
from backend.app.schemas.demand import DemandRequest, DemandResponse
from ai_engine.demand_forecasting.features import build_features
from ai_engine.demand_forecasting.model import DemandModel

router = APIRouter()
model = DemandModel("ai_engine/demand_forecasting/demand_model.pkl")

@router.post("/predict-demand", response_model=DemandResponse)
def predict_demand(request: DemandRequest, db: Session = Depends(get_db)):
    try:
        features = build_features(request.dict())
        demand, confidence = model.predict(features)

        record = Prediction(
            product_id=request.product_id,
            warehouse_id=request.warehouse_id,
            predicted_demand=demand,
            confidence=float(confidence)  # force cast
        )

        db.add(record)
        db.commit()

        return DemandResponse(
            product_id=request.product_id,
            warehouse_id=request.warehouse_id,
            predicted_demand=demand,
            confidence=round(float(confidence), 2),
            recommendation={
                "LOW": "Reduce stock",
                "MEDIUM": "Maintain stock",
                "HIGH": "Increase stock"
            }[demand]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
