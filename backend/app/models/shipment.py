from sqlalchemy import Column, Integer, Float, String
from backend.app.core.database import Base

class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(Integer)
    destination_id = Column(Integer)
    distance_km = Column(Float)
    traffic_level = Column(String)
    weather = Column(String)
    vehicle_type = Column(String)
    actual_time = Column(Float)  # minutes
