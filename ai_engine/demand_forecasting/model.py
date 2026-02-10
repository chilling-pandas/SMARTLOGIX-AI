import joblib
from sklearn.linear_model import LogisticRegression

LABEL_MAP = {
    0: "LOW",
    1: "MEDIUM",
    2: "HIGH"
}

class DemandModel:
    def __init__(self, model_path: str):
        self.model: LogisticRegression = joblib.load(model_path)

    def predict(self, X):
        pred_class = self.model.predict(X)[0]
        confidence = self.model.predict_proba(X)[0].max()
        return LABEL_MAP[pred_class], confidence
