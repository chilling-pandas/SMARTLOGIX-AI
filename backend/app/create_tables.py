from backend.app.core.database import engine
from backend.app.models.order import Order
from backend.app.models.shipment import Shipment
from backend.app.models.prediction import Prediction

Order.metadata.create_all(bind=engine)
Shipment.metadata.create_all(bind=engine)
Prediction.metadata.create_all(bind=engine)

print("✅ Tables created")
