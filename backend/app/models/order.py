from sqlalchemy import Column, Integer, Date
from app.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    warehouse_id = Column(Integer, index=True)
    quantity = Column(Integer)
    order_date = Column(Date)
