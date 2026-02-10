from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from backend.app.core.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    warehouse_id = Column(Integer, index=True)
    predicted_demand = Column(String)
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

