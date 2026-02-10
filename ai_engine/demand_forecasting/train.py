import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression

# -----------------------------
# Synthetic training data
# Features:
# [avg_7_day_sales, avg_30_day_sales, stock_level, demand_variance]
# -----------------------------

X = np.array([
    [10, 12, 200, 2],    # LOW
    [15, 18, 180, 3],    # LOW
    [30, 28, 120, 5],    # MEDIUM
    [35, 32, 100, 6],    # MEDIUM
    [60, 55, 50, 10],    # HIGH
    [70, 65, 40, 12]     # HIGH
])

# Labels: 0=LOW, 1=MEDIUM, 2=HIGH
y = np.array([0, 0, 1, 1, 2, 2])

# Train model
model = LogisticRegression(max_iter=500)
model.fit(X, y)

# Save model
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "demand_model.pkl")

joblib.dump(model, MODEL_PATH)
print("✅ Dummy demand model trained & saved at", MODEL_PATH)
