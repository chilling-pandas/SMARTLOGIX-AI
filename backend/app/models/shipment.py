from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from backend.app.core.database import Base

class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)

    delivery_partner = Column(String)
    package_type = Column(String)
    vehicle_type = Column(String)
    delivery_mode = Column(String)
    region = Column(String)
    weather_condition = Column(String)

    distance_km = Column(Float)
    package_weight_kg = Column(Float)
    delivery_rating = Column(Float)

    actual_time = Column(Float)

    created_at = Column(DateTime, default=datetime.utcnow)