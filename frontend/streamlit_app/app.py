import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "http://127.0.0.1:8000/api"

st.set_page_config(page_title="SmartLogix AI", layout="centered")

st.title("🚚 SmartLogix AI Dashboard")

tab1, tab2, tab3 = st.tabs([
    "📦 Demand Prediction",
    "⏱️ ETA Prediction",
    "📊 Prediction History"
])


# -------------------------
# Demand Prediction
# -------------------------
with tab1:
    st.subheader("Predict Product Demand")

    product_id = st.number_input("Product ID", min_value=1)
    warehouse_id = st.number_input("Warehouse ID", min_value=1)

    avg_7 = st.number_input("Avg 7-Day Sales")
    avg_30 = st.number_input("Avg 30-Day Sales")
    stock = st.number_input("Stock Level")
    variance = st.number_input("Demand Variance")

    if st.button("Predict Demand"):
        payload = {
            "product_id": product_id,
            "warehouse_id": warehouse_id,
            "avg_7_day_sales": avg_7,
            "avg_30_day_sales": avg_30,
            "stock_level": stock,
            "demand_variance": variance
        }

        res = requests.post(f"{BACKEND_URL}/predict-demand", json=payload)

        if res.status_code == 200:
            data = res.json()
            st.success(f"Demand: {data['predicted_demand']}")
            st.write(f"Confidence: {data['confidence']}")
            st.info(data["recommendation"])
        else:
            st.error("Prediction failed")

# -------------------------
# ETA Prediction
# -------------------------
with tab2:
    st.subheader("Predict Delivery ETA")

    source = st.number_input("Source ID", min_value=1)
    destination = st.number_input("Destination ID", min_value=1)
    distance = st.number_input("Distance (km)")

    traffic = st.selectbox("Traffic Level", ["LOW", "MEDIUM", "HIGH"])
    weather = st.selectbox("Weather", ["CLEAR", "RAIN"])
    vehicle = st.selectbox("Vehicle Type", ["BIKE", "VAN", "TRUCK"])

    if st.button("Predict ETA"):
        payload = {
            "source_id": source,
            "destination_id": destination,
            "distance_km": distance,
            "traffic_level": traffic,
            "weather": weather,
            "vehicle_type": vehicle
        }

        res = requests.post(f"{BACKEND_URL}/predict-eta", json=payload)

        if res.status_code == 200:
            data = res.json()
            st.success(f"Estimated Time: {data['estimated_time_minutes']} minutes")
        else:
            st.error("ETA prediction failed")

# Add History Tabs
with tab3:
    import pandas as pd
    import streamlit as st
    st.subheader("📦 Demand Prediction History")

    demand_res = requests.get(f"{BACKEND_URL}/history/demand")

    if demand_res.status_code == 200:
        demand_data = demand_res.json()
        df_demand = pd.DataFrame(demand_data)

        if not df_demand.empty:
            # Raw Table
            if st.checkbox("Show Raw Data"):
               st.dataframe(df_demand, use_container_width=True)

            # KPIs
            col1, col2 = st.columns(2)
            col1.metric("Total Predictions", len(df_demand))
            col2.metric("Avg Confidence", round(df_demand["confidence"].mean(), 2))

            # Distribution
            st.subheader("Demand Distribution")
            st.bar_chart(df_demand["predicted_demand"].value_counts())

            # Trend
            st.subheader("Demand Trend")
            df_demand["created_at"] = pd.to_datetime(df_demand["created_at"])
            df_trend = df_demand.groupby(df_demand["created_at"].dt.date).size()
            st.line_chart(df_trend)

        else:
            st.info("No demand history yet")
    else:
        st.error("Failed to load demand history")

    st.divider()
    st.subheader("🚚 Shipment / ETA History")
    
    ship_res = requests.get(f"{BACKEND_URL}/history/shipments")
    
    if ship_res.status_code == 200:
        ship_data = ship_res.json()
        df_ship = pd.DataFrame(ship_data)
    
        if not df_ship.empty:
            # if st.checkbox("Show Raw Data"):
            #    st.dataframe(df_ship, use_container_width=True)
    
            # ---------------- KPI Row ----------------
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Shipments", len(df_ship))
            col2.metric("Avg ETA (min)", round(df_ship["eta_minutes"].mean(), 2))
            col3.metric("Max ETA", round(df_ship["eta_minutes"].max(), 2))
            
            show_raw_demand = st.checkbox("Show Raw Data", key="demand_raw")


            if show_raw_demand:
                st.dataframe(df_ship, use_container_width=True)
            # ---------------- ETA Distribution ----------------
            st.subheader("ETA Distribution")
            st.bar_chart(df_ship["eta_minutes"])
    
            # ---------------- Traffic Impact ----------------
            st.subheader("Traffic vs Avg ETA")
            traffic_eta = df_ship.groupby("traffic_level")["eta_minutes"].mean()
            st.bar_chart(traffic_eta)
    
            # ---------------- Vehicle Impact ----------------
            st.subheader("Vehicle Type vs Avg ETA")
            vehicle_eta = df_ship.groupby("vehicle_type")["eta_minutes"].mean()
            st.bar_chart(vehicle_eta)
    
        else:
            st.info("No shipment history yet")
    
    else:
        st.error("Failed to load shipment history")



# st.write("Demand history response:", demand_res.text)
# st.write("Shipment history response:", ship_res.text)
# st.write("Status:", res.status_code)
# st.write("Response:", res.text)


