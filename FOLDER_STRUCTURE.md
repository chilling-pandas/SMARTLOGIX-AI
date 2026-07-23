# SmartLogix AI - Folder Structure

```text
smartlogix-ai/
|
|-- README.md
|-- FOLDER_STRUCTURE.md
|-- LICENSE
|-- requirements.txt
|-- .gitignore
|
|-- ai_engine/                         # Machine-learning inference and training code
|   |-- __init__.py
|   |-- requirements.txt
|   |
|   |-- demand_forecasting/
|   |   |-- __init__.py
|   |   |-- features.py                # Demand feature preparation
|   |   |-- model.py                   # Demand model inference
|   |   |-- train.py                   # Demand model training
|   |   |-- demand_model.pkl           # Trained demand model
|   |   `-- demand_metrics.pkl         # Demand model metrics
|   |
|   |-- route_eta/
|   |   |-- features.py                # ETA feature preparation
|   |   |-- model.py                   # ETA model inference
|   |   |-- train.py                   # ETA model training
|   |   `-- eta_model.pkl              # Trained ETA model
|   |
|   `-- utils/
|       `-- encoders.py                # Shared categorical encoders
|
|-- backend/                           # FastAPI application and persistence
|   |-- __init__.py
|   `-- app/
|       |-- __init__.py
|       |-- main.py                    # FastAPI application entry point
|       |-- create_tables.py           # Database table initialization
|       |
|       |-- api/
|       |   |-- __init__.py
|       |   |-- health.py               # Health endpoint
|       |   |-- demand.py               # Demand prediction endpoints
|       |   |-- shipping.py             # ETA prediction endpoints
|       |   `-- history.py              # Prediction history endpoints
|       |
|       |-- core/
|       |   |-- __init__.py
|       |   |-- config.py               # Application configuration
|       |   |-- database.py             # Database connection and session
|       |   `-- ml_loader.py            # Trained model loading
|       |
|       |-- models/
|       |   |-- __init__.py
|       |   |-- order.py                # Order database model
|       |   |-- shipment.py             # Shipment database model
|       |   `-- prediction.py           # Prediction database model
|       |
|       `-- schemas/
|           |-- __init__.py
|           |-- demand.py               # Demand request/response schemas
|           `-- shipping.py             # Shipping request/response schemas
|
|-- frontend/                           # User-facing applications
|   `-- streamlit_app/
|       |-- app.py                      # Streamlit dashboard entry point
|       `-- requirements.txt
|
|-- training/                           # Offline dataset preparation and training workflows
|   `-- demand/
|       |-- dataset.py                  # Training data loading
|       |-- preprocess.py               # Data cleaning and preprocessing
|       |-- feature_engineering.py      # Training feature generation
|       `-- train.py                    # Demand model training workflow
|
|-- data/                               # Datasets used by training and evaluation
|   |-- raw/
|   |   |-- retail_store_inventory.csv
|   |   `-- Delivery_Logistics.csv
|   |-- processed/                      # Generated cleaned datasets
|   `-- samples/                        # Small datasets for local testing
|
|-- evaluation/                         # Model evaluation artifacts
|   |-- demand_metrics.json
|   |-- eta_metrics.json
|   `-- confusion_matrix.png
|
|-- notebooks/
|   `-- exploration.ipynb               # Exploratory analysis
|
|-- assets/                             # README and dashboard images
|
`-- docker/                             # Container build definitions
    |-- backend.Dockerfile
    `-- ai.Dockerfile
```

## Directory Responsibilities

| Directory | Responsibility |
| --- | --- |
| `ai_engine/` | Loads trained models and exposes reusable prediction logic. |
| `backend/` | Provides the FastAPI REST API, validation, and database access. |
| `frontend/` | Contains the Streamlit analytics dashboard. |
| `training/` | Prepares datasets and trains machine-learning models. |
| `data/` | Stores raw input data and generated local datasets. |
| `evaluation/` | Stores metrics and visual evaluation outputs. |
| `notebooks/` | Supports exploratory data analysis and experimentation. |
| `docker/` | Contains container definitions for the backend and AI services. |