# 🚚 SmartLogix AI

SmartLogix AI is an AI-powered logistics and supply chain intelligence system that predicts product demand and delivery ETA using machine learning, with backend APIs and analytics dashboards for decision support.

---

## 🚚 Problem Statement

Logistics systems often face inaccurate demand estimation and delivery delays.  
SmartLogix AI addresses this using machine learning predictions combined with operational analytics dashboards.

---

## 🚀 Key Features

- Demand Prediction (LOW / MEDIUM / HIGH)
- ETA Prediction for shipments
- FastAPI-based REST API
- PostgreSQL persistence for auditability
- Streamlit analytics dashboard
- Filterable views (date, warehouse, product)
- Model evaluation with metrics & confusion matrix

---

## 🧠 Tech Stack

- Python
- FastAPI
- Streamlit
- PostgreSQL
- Scikit-learn
- SQLAlchemy
- Pandas
- Matplotlib

---

## 📁 Project Structure (Visual)

```mermaid
graph TD

A[SmartLogix AI]:::root

A --> B[AI Engine]:::ai
A --> C[Backend]:::backend
A --> D[Frontend]:::frontend
A --> E[Data]:::data
A --> F[Docker]:::infra
A --> G[Notebooks]:::notebook

%% AI ENGINE
B --> B1[Demand Forecasting]
B --> B2[Route ETA]
B --> B3[Utils]

%% BACKEND
C --> C1[API Layer]
C --> C2[Core Config]
C --> C3[Models]
C --> C4[Schemas]

%% FRONTEND
D --> D1[Streamlit App]

%% DATA
E --> E1[Raw]
E --> E2[Processed]
E --> E3[Samples]

%% DOCKER
F --> F1[Backend Dockerfile]
F --> F2[AI Dockerfile]

%% NOTEBOOK
G --> G1[Exploration]

%% STYLES
classDef root fill:#0f172a,color:#ffffff,stroke:#ffffff;
classDef ai fill:#6366f1,color:#ffffff;
classDef backend fill:#10b981,color:#ffffff;
classDef frontend fill:#f59e0b,color:#ffffff;
classDef data fill:#3b82f6,color:#ffffff;
classDef infra fill:#ef4444,color:#ffffff;
classDef notebook fill:#8b5cf6,color:#ffffff;

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[Frontend - Streamlit] --> B[Backend - FastAPI]
    B --> C[AI Engine]
    C --> D[Demand Model - Logistic Regression]
    C --> E[ETA Model - Linear Regression]
    B --> F[(PostgreSQL Database)]
    C --> G[Evaluation Metrics]


