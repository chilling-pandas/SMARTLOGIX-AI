from ai_engine.demand_forecasting.model import DemandModel
from ai_engine.route_eta.model import EtaModel

DEMAND_MODEL_PATH = "ai_engine/demand_forecasting/demand_model.pkl"
ETA_MODEL_PATH = "ai_engine/route_eta/eta_model.pkl"

demand_model = DemandModel(DEMAND_MODEL_PATH)
eta_model = EtaModel(ETA_MODEL_PATH)
