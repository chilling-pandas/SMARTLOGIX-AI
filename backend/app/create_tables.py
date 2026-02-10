from app.core.database import engine
from app.models.order import Order
from app.models.shipment import Shipment
from app.models.prediction import Prediction

Order.metadata.create_all(bind=engine)
Shipment.metadata.create_all(bind=engine)
Prediction.metadata.create_all(bind=engine)

print("✅ Tables created")
