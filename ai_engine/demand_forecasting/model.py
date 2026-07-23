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
        pred = self.model.predict(X)[0]
        confidence = self.model.predict_proba(X)[0].max()

        # If the model already returns string labels
        if isinstance(pred, str):
            return pred, confidence

        # Otherwise convert numeric class to label
        return LABEL_MAP[pred], confidence
