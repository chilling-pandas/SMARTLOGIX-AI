from fastapi import FastAPI
from backend.app.api import demand, shipping

app = FastAPI(title="SmartLogix AI")

app.include_router(demand.router, prefix="/api")
app.include_router(shipping.router, prefix="/api")


@app.get("/health")
def health_check():
    return {"status": "ok"}

#Register History Router
from backend.app.api import history

app.include_router(history.router, prefix="/api")
