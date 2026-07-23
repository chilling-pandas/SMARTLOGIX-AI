import joblib


class EtaModel:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def predict(self, X):
        eta = self.model.predict(X)[0]
        return round(float(eta), 2)