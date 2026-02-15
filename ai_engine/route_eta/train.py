import numpy as np
import joblib
import json
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Features:
# [distance, traffic, weather, vehicle]
X = np.array([
    [5, 1, 0, 1],
    [10, 2, 0, 2],
    [15, 3, 1, 3],
    [20, 2, 1, 2],
    [8, 1, 0, 1],
    [18, 3, 1, 3],
])

# ETA in minutes
y = np.array([15, 30, 60, 50, 22, 70])

# -----------------------------
# Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Evaluate
# -----------------------------
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("R2 Score:", r2)

os.makedirs("evaluation", exist_ok=True)

eta_metrics = {
    "MAE": float(mae),
    "MSE": float(mse),
    "R2": float(r2)
}

with open("evaluation/eta_metrics.json", "w") as f:
    json.dump(eta_metrics, f, indent=4)


joblib.dump(model, "eta_model.pkl")

print("✅ Dummy ETA model trained & saved")
