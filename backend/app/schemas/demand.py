from pydantic import BaseModel

class DemandRequest(BaseModel):
    product_id: int
    warehouse_id: int
    avg_7_day_sales: float
    avg_30_day_sales: float
    stock_level: int
    demand_variance: float


class DemandResponse(BaseModel):
    product_id: int
    warehouse_id: int
    predicted_demand: str   # LOW / MEDIUM / HIGH
    confidence: float
    recommendation: str
