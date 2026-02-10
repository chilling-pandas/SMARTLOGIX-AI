import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

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

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "eta_model.pkl")

print("✅ Dummy ETA model trained & saved")
