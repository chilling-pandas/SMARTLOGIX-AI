from pathlib import Path
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from dataset import load_training_data


# -----------------------------
# Load Dataset
# -----------------------------
X, y = load_training_data()

# -----------------------------
# Train/Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1,
)

# -----------------------------
# Train
# -----------------------------
model.fit(X_train, y_train)

# -----------------------------
# Predict
# -----------------------------
predictions = model.predict(X_test)

# -----------------------------
# Accuracy
# -----------------------------
accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy : {accuracy:.4f}")

print("\nClassification Report\n")
print(classification_report(y_test, predictions))

# -----------------------------
# Save Model
# -----------------------------
project_root = Path(__file__).resolve().parents[2]

model_path = (
    project_root
    / "ai_engine"
    / "demand_forecasting"
    / "demand_model.pkl"
)
print("\nTraining completed...")
print(f"Number of trees: {len(model.estimators_)}")
print(f"Max depth of first tree: {model.estimators_[0].tree_.max_depth}")

joblib.dump(model, model_path, compress=3)
print(f"\nModel saved to:\n{model_path}")