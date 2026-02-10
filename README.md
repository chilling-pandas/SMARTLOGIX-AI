# SmartLogix AI

SmartLogix AI is an intelligent logistics optimization platform that leverages machine learning to predict demand and estimate route ETAs for efficient shipping and supply chain management.

## 📋 Project Structure

```
smartlogix-ai/
├── ai_engine/                    # Machine Learning models and training
│   ├── demand_forecasting/       # Demand prediction models
│   ├── route_eta/                # Route ETA estimation
│   └── utils/                    # Utility functions and encoders
├── backend/                      # FastAPI backend application
│   ├── app/
│   │   ├── api/                  # API endpoints for demand, shipping, health, history
│   │   ├── core/                 # Core configs, database, ML loader
│   │   ├── models/               # SQLAlchemy ORM models
│   │   └── schemas/              # Pydantic schemas
│   └── requirements.txt
├── frontend/                     # Streamlit UI application
│   └── streamlit_app/
├── notebooks/                    # Jupyter notebooks for exploration
├── data/                         # Data storage (raw, processed, samples)
├── docker/                       # Docker configurations
└── vectore_index/                # FAISS vector indexing
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. **Clone the repository**
   ```bash
   cd smartlogix-ai
   ```

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
- ReDoc: `http://localhost:8000/redoc`

## 🤖 Components

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

## 📦 Docker Support

Build and run using Docker:
```bash
docker build -f docker/backend.Dockerfile -t smartlogix-backend .
docker run -p 8000:8000 smartlogix-backend
```

## 📝 Notes

- Ensure database migrations are set up before running the backend
- Vector indices for FAISS are pre-built and stored in `vectore_index/`
- Training scripts for ML models are available in respective module directories under `ai_engine/`

## 📄 License

This project is proprietary and confidential.
