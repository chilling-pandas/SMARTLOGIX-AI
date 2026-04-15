SmartLogix AI is an end-to-end AI-powered logistics and supply chain intelligence system. It predicts product demand levels and delivery ETA using machine learning models, stores predictions for traceability, and provides interactive dashboards for analytics and decision support.
# SmartLogix AI

SmartLogix AI is an intelligent logistics optimization platform that leverages machine learning to predict demand and estimate route ETAs for efficient shipping and supply chain management.

🚀 Key Features

- REST API-based ML inference
- Database persistence for auditability
- Interactive analytics dashboard
- Filterable operations view (date, warehouse, product)
- Model evaluation artifacts included
- Clean separation of ML, API, and storage layers


## 🏗️ Project Structure

```mermaid
graph TD

A[SmartLogix AI]:::root

A --> B[AI Engine]:::ai
A --> C[Backend API]:::backend
A --> D[Frontend]:::frontend
A --> E[Data Layer]:::data
A --> F[Docker]:::infra
A --> G[Notebooks]:::notebook
A --> H[Vector Index]:::vector

%% AI ENGINE
B --> B1[Demand Forecasting]:::ai_sub
B1 --> B1a[features.py]
B1 --> B1b[model.py]
B1 --> B1c[train.py]

B --> B2[Route ETA]:::ai_sub
B2 --> B2a[features.py]
B2 --> B2b[model.py]
B2 --> B2c[train.py]

B --> B3[Utils]:::ai_sub
B3 --> B3a[encoders.py]

%% BACKEND
C --> C1[App Core]:::backend_sub
C1 --> C1a[main.py]
C1 --> C1b[create_tables.py]

C --> C2[API Layer]:::backend_sub
C2 --> C2a[demand.py]
C2 --> C2b[shipping.py]
C2 --> C2c[health.py]

C --> C3[Core Config]:::backend_sub
C3 --> C3a[config.py]
C3 --> C3b[database.py]

C --> C4[Models]:::backend_sub
C4 --> C4a[order.py]
C4 --> C4b[shipment.py]

C --> C5[Schemas]:::backend_sub
C5 --> C5a[demand.py]
C5 --> C5b[shipping.py]

%% FRONTEND
D --> D1[Streamlit App]:::frontend_sub
D1 --> D1a[app.py]

%% DATA
E --> E1[Raw Data]
E --> E2[Processed Data]
E --> E3[Samples]

%% DOCKER
F --> F1[Backend Dockerfile]
F --> F2[AI Dockerfile]

%% NOTEBOOK
G --> G1[exploration.ipynb]

%% VECTOR
H --> H1[FAISS Index]

%% STYLES
classDef root fill:#0f172a,stroke:#ffffff,color:#ffffff,stroke-width:2px;

classDef ai fill:#6366f1,color:#ffffff,stroke:#1e1b4b;
classDef ai_sub fill:#a5b4fc,color:#000000;

classDef backend fill:#10b981,color:#ffffff,stroke:#064e3b;
classDef backend_sub fill:#6ee7b7,color:#000000;

classDef frontend fill:#f59e0b,color:#ffffff,stroke:#78350f;
classDef frontend_sub fill:#fde68a,color:#000000;

classDef data fill:#3b82f6,color:#ffffff,stroke:#1e3a8a;

classDef infra fill:#ef4444,color:#ffffff,stroke:#7f1d1d;

classDef notebook fill:#8b5cf6,color:#ffffff,stroke:#4c1d95;

classDef vector fill:#14b8a6,color:#ffffff,stroke:#134e4a;


### Running the Application

**Start Backend (FastAPI)**
```bash
uvicorn backend.app.main:app --reload --log-level debug
```
The API will be available at `http://localhost:8000`

**Start Frontend (Streamlit)** (Optional)
```bash
streamlit run frontend/streamlit_app/app.py
```

**API Documentation**
- Swagger UI: `http://localhost:8000/docs`

🤖 Components

### AI Engine
- **Demand Forecasting**: Predicts future demand based on historical data
- **Route ETA**: Estimates delivery times for shipping routes
- **Encoders**: Utility functions for feature encoding

### Backend API
- `/health`: Health check endpoint
- `/demand`: Demand prediction endpoints
- `/shipping`: Shipping and shipment management
- `/history`: Historical data and analytics

### Frontend
Interactive Streamlit application for visualization and interaction with the AI models.

📦 Docker Support

Build and run using Docker:
```bash
docker build -f docker/backend.Dockerfile -t smartlogix-backend .
docker run -p 8000:8000 smartlogix-backend
```

📝 Notes

- Ensure database migrations are set up before running the backend
- Vector indices for FAISS are pre-built and stored in `vectore_index/`
- Training scripts for ML models are available in respective module directories under `ai_engine/`


🏗️ System Architecture

Streamlit (Frontend)
        ↓
FastAPI (Backend API Layer)
        ↓
AI Engine (ML Models)
   ├── Demand Forecasting (Logistic Regression)
   └── ETA Prediction (Linear Regression)
        ↓
PostgreSQL (Prediction & Shipment Storage)
        ↓
Evaluation Layer (Metrics + Confusion Matrix)

📊 Model Evaluation

### Demand Forecasting Model (Classification)

- Train/Test Split: 70/30
- Model: Logistic Regression
- Metric: Accuracy, Confusion Matrix

#### Accuracy
See `evaluation/demand_metrics.json`

#### Confusion Matrix
![Confusion Matrix](evaluation/confusion_matrix.png)

---

ETA Prediction Model (Regression)

- Train/Test Split: 70/30
- Model: Linear Regression
- Metrics:
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - R² Score

See `evaluation/eta_metrics.json`

📈 Why These Metrics?

### Classification (Demand Model)

- **Accuracy**: Measures overall correctness of demand classification.
- **Confusion Matrix**: Provides class-level insight into prediction errors (LOW vs MEDIUM vs HIGH).
- **Classification Report**: Precision, Recall, and F1-score give deeper performance understanding.

### Regression (ETA Model)

- **MAE**: Measures average absolute prediction error in minutes. Easy to interpret operationally.
- **MSE**: Penalizes larger errors more heavily.
- **R² Score**: Indicates how well the model explains variance in delivery time.

### Prerequisites
- Python 3.8+
- pip or conda


2. **Install Backend Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

3. **Install AI Engine Dependencies**
   ```bash
   cd ai_engine
   pip install -r requirements.txt
   cd ..
   ```

4. **Install Frontend Dependencies** (Optional)
   ```bash
   cd frontend/streamlit_app
   pip install -r requirements.txt
   cd ../..
   ```
### Prerequisites
- Python 3.8+
- pip or conda


2. **Install Backend Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

3. **Install AI Engine Dependencies**
   ```bash
   cd ai_engine
   pip install -r requirements.txt
   cd ..
   ```

4. **Install Frontend Dependencies** (Optional)
   ```bash
   cd frontend/streamlit_app
   pip install -r requirements.txt
   cd ../..
   ```### Prerequisites
- Python 3.8+
- pip or conda


2. **Install Backend Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

3. **Install AI Engine Dependencies**
   ```bash
   cd ai_engine
   pip install -r requirements.txt
   cd ..
   ```

4. **Install Frontend Dependencies** (Optional)
   ```bash
   cd frontend/streamlit_app
   pip install -r requirements.txt
   cd ../..
   ```

🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- PostgreSQL
- Scikit-learn
- SQLAlchemy
- Pandas
- Matplotlib