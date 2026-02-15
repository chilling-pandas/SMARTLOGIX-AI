import numpy as np
import joblib
import json
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

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

# -----------------------------
# Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression(max_iter=500)
model.fit(X, y)

# -----------------------------
# Evaluate
# -----------------------------
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", report)

# Create evaluation directory
os.makedirs("evaluation", exist_ok=True)

# Save metrics to JSON
metrics = {
    "accuracy": float(accuracy),
    "classification_report": report
}

with open("evaluation/demand_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

# Save confusion matrix image
plt.figure()
plt.imshow(cm, interpolation="nearest")
plt.title("Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("evaluation/confusion_matrix.png")
plt.close()


# Save model
import os
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "demand_model.pkl")

joblib.dump(model, MODEL_PATH)
print("✅ Dummy demand model trained & saved at", MODEL_PATH)
