import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from xgboost import XGBRegressor


# Load Dataset
df = pd.read_csv("data/raw/Delivery_Logistics.csv")
import re

def extract_hours(value):
    match = re.search(r'(\d+)$', str(value))
    return int(match.group(1))

df["delivery_time_hours"] = df["delivery_time_hours"].apply(extract_hours)
df["expected_time_hours"] = df["expected_time_hours"].apply(extract_hours)

# Drop unused columns
X = df.drop(
    columns=[
        "delivery_id",
        "delivery_time_hours",
        "expected_time_hours",
        "delayed",
        "delivery_status",
        "delivery_cost",
    ]
)

y = df["delivery_time_hours"]

# Categorical & Numerical Features
categorical_features = X.select_dtypes(include=["object"]).columns.tolist()
numeric_features = X.select_dtypes(exclude=["object"]).columns.tolist()

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features,
        ),
        (
            "num",
            "passthrough",
            numeric_features,
        ),
    ]
)

# Model
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "model",
            XGBRegressor(
                n_estimators=200,
                learning_rate=0.05,
                max_depth=6,
                random_state=42,
                objective="reg:squarederror",
            ),
        ),
    ]
)

# Train
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

print("Model Performance")
print("--------------------")
print("MAE :", mean_absolute_error(y_test, pred))
print("RMSE:", mean_squared_error(y_test, pred) ** 0.5)
print("R²  :", r2_score(y_test, pred))

# Save Model
joblib.dump(model, "ai_engine/route_eta/eta_model.pkl")

print("Model saved successfully!")