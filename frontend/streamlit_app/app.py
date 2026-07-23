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
            try:
                st.error(res.json()["detail"])
            except:
                st.error(res.text)

# -------------------------
# ETA Prediction
# -------------------------
with tab2:
    st.subheader("🚚 Predict Delivery ETA")

    delivery_partner = st.selectbox(
        "Delivery Partner",
        [
            "amazon logistics",
            "blue dart",
            "delhivery",
            "dhl",
            "ecom express",
            "ekart",
            "fedex",
            "shadowfax",
            "xpressbees"
        ]
    )

    package_type = st.selectbox(
        "Package Type",
        [
            "automobile parts",
            "clothing",
            "cosmetics",
            "documents",
            "electronics",
            "fragile items",
            "furniture",
            "groceries",
            "pharmacy"
        ]
    )

    vehicle_type = st.selectbox(
        "Vehicle Type",
        [
            "bike",
            "ev bike",
            "ev van",
            "scooter",
            "truck",
            "van"
        ]
    )

    delivery_mode = st.selectbox(
        "Delivery Mode",
        [
            "express",
            "same day",
            "standard",
            "two day"
        ]
    )

    region = st.selectbox(
        "Region",
        [
            "central",
            "east",
            "north",
            "south",
            "west"
        ]
    )

    weather_condition = st.selectbox(
        "Weather",
        [
            "clear",
            "cold",
            "foggy",
            "hot",
            "rainy",
            "stormy"
        ]
    )

    distance_km = st.number_input(
        "Distance (km)",
        min_value=3.6,
        max_value=297.1,
        value=10.0,
        step=0.1
    )

    package_weight = st.number_input(
        "Package Weight (kg)",
        min_value=0.1,
        max_value=50.0,
        value=5.0,
        step=0.1
    )

    delivery_rating = st.slider(
        "Delivery Rating",
        min_value=1.0,
        max_value=5.0,
        value=3.0,
        step=1.0
    )

    if st.button("Predict ETA"):

        payload = {
            "delivery_partner": delivery_partner,
            "package_type": package_type,
            "vehicle_type": vehicle_type,
            "delivery_mode": delivery_mode,
            "region": region,
            "weather_condition": weather_condition,
            "distance_km": distance_km,
            "package_weight_kg": package_weight,
            "delivery_rating": delivery_rating
        }

        res = requests.post(
            f"{BACKEND_URL}/predict-eta",
            json=payload
        )

        if res.status_code == 200:
            data = res.json()

            st.success(
                f"Estimated Time: {data['estimated_time_minutes']} minutes"
            )

            st.metric(
                "Confidence",
                data["confidence"]
            )

        else:
            try:
                st.error(res.json()["detail"])
            except:
                st.error(res.text)
# Add History Tabs
with tab3:
    
    st.subheader("📦 Demand Prediction History")

    # ================= FILTER INPUTS FIRST =================
    st.markdown("### 🔍 Filters")

    # Date filter (simple default range)
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    selected_warehouse = st.number_input("Warehouse ID (optional)", value=0)
    selected_product = st.number_input("Product ID (optional)", value=0)

    # ================= BUILD PARAMS =================
    params = {}

    if selected_warehouse != 0:
        params["warehouse_id"] = selected_warehouse

    if selected_product != 0:
        params["product_id"] = selected_product

    if start_date:
        params["start_date"] = start_date

    if end_date:
        params["end_date"] = end_date

    # ================= FETCH FILTERED DATA =================
    demand_res = requests.get(
        f"{BACKEND_URL}/history/demand",
        params=params
    )

    if demand_res.status_code == 200:
        df_demand = pd.DataFrame(demand_res.json())

        if not df_demand.empty:

            df_demand["created_at"] = pd.to_datetime(df_demand["created_at"])

            # ================= KPIs =================
            col1, col2 = st.columns(2)
            col1.metric("Total Predictions", len(df_demand))
            col2.metric(
                "Avg Confidence",
                round(df_demand["confidence"].mean(), 2)
            )

            # ================= TABLE =================
            #if st.toggle("Show Demand Table"):
            #    st.dataframe(df_demand, use_container_width=True)

            # ================= CHARTS =================
            st.subheader("Demand Distribution")
            dist_data = df_demand["predicted_demand"].value_counts()
            st.bar_chart(dist_data)

            st.subheader("Demand Trend")
            trend = (
                df_demand
                .groupby(df_demand["created_at"].dt.date)
                .size()
            )
            st.line_chart(trend)

        else:
            st.info("No demand history found for selected filters")

    else:
        st.error("Failed to load demand history")


    # ================= SHIPMENTS =================
    st.divider()
    st.subheader("🚚 Shipment / ETA History")
    
    ship_res = requests.get(f"{BACKEND_URL}/history/shipments")
    
    if ship_res.status_code == 200:
        df_ship = pd.DataFrame(ship_res.json())
    
        if not df_ship.empty:
    
            # Ensure numeric type
            df_ship["eta_minutes"] = pd.to_numeric(df_ship["eta_minutes"])
    
            # ================= KPI ROW =================
            st.subheader("Shipment KPIs")
    
            col1, col2, col3 = st.columns(3)
    
            col1.metric("Total Shipments", len(df_ship))
            col2.metric("Avg ETA (min)", round(df_ship["eta_minutes"].mean(), 2))
            col3.metric("Max ETA", round(df_ship["eta_minutes"].max(), 2))
    
            # ================= TOGGLE TABLE =================
            #if st.toggle("Show Shipment Table"):
            #    st.dataframe(df_ship, use_container_width=True)
    
            # ================= ETA DISTRIBUTION =================
            st.subheader("ETA Distribution (Filtered)")
            st.bar_chart(df_ship["eta_minutes"])
    
            # ================= TRAFFIC VS ETA =================
            st.subheader("Region vs Avg ETA")
    
            region_eta = (
                df_ship
                .groupby("region")["eta_minutes"]
                .mean()
            )
            
            st.bar_chart(region_eta)
            st.subheader("Weather vs Avg ETA")

            weather_eta = (
                df_ship
                .groupby("weather_condition")["eta_minutes"]
                .mean()
            )
            
            st.bar_chart(weather_eta)
            # ================= VEHICLE VS ETA =================
            st.subheader("Vehicle Type vs Avg ETA")
    
            vehicle_eta = (
                df_ship
                .groupby("vehicle_type")["eta_minutes"]
                .mean()
                .reset_index()
            )
    
            st.bar_chart(vehicle_eta.set_index("vehicle_type"))
    
            # ================= ETA TREND (STEP 3 FULL) =================
            if "created_at" in df_ship.columns:
                st.subheader("Shipment ETA Trend Over Time")
    
                df_ship["created_at"] = pd.to_datetime(df_ship["created_at"])
    
                eta_trend = (
                    df_ship
                    .groupby(df_ship["created_at"].dt.date)["eta_minutes"]
                    .mean()
                    .reset_index()
                )
    
                eta_trend.columns = ["Date", "Avg ETA"]
    
                st.line_chart(eta_trend.set_index("Date"))
            st.divider()
    
            st.subheader("🤖 Model Evaluation")
            
            col1, col2, col3 = st.columns(3)
            
            # col1.metric("Accuracy", "0.92")
            # col2.metric("Precision", "0.90")
            # col3.metric("Recall", "0.91")
            
    
        else:
            st.info("No shipment history yet")
    
    else:
        st.error("Failed to load shipment history")





# st.write("Demand history response:", demand_res.text)
# st.write("Shipment history response:", ship_res.text)
# st.write("Status:", res.status_code)
# st.write("Response:", res.text)


