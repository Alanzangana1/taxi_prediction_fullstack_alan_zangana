import streamlit as st
import httpx

url = "http://127.0.0.1:8000/predict"

def predict_price(payload):
    with httpx.Client(timeout=10) as client:
        response = client.post(url, json=payload)
        response.raise_for_status()
        return response

st.markdown("# Taxi Price Prediction")

with st.form("taxi_form"):
    trip_distance = st.number_input(
        "Trip Distance (km)", min_value=0.1, max_value=100.0, value=10.0, step=0.1
    )
    passenger_count = st.number_input(
        "Passenger Count", min_value=1, max_value=10, value=2, step=1
    )
    base_fare = st.number_input(
        "Base Fare", min_value=0.0, max_value=200.0, value=20.0, step=0.1
    )
    per_km_rate = st.number_input(
        "Per Km Rate", min_value=0.0, max_value=20.0, value=5.0, step=0.1
    )
    per_minute_rate = st.number_input(
        "Per Minute Rate", min_value=0.0, max_value=10.0, value=1.0, step=0.1
    )
    duration = st.number_input(
        "Trip Duration (minutes)", min_value=1, max_value=300, value=30, step=1
    )
    time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
    day_of_week = st.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    traffic_conditions = st.selectbox("Traffic Conditions", ["Low", "Medium", "High"])
    weather = st.selectbox("Weather", ["Clear", "Rain", "Snow"])

    submitted = st.form_submit_button("PREDICT")

if submitted:
    payload = {
        "Trip_Distance_km": trip_distance,
        "Passenger_Count": passenger_count,
        "Base_Fare": base_fare,
        "Per_Km_Rate": per_km_rate,
        "Per_Minute_Rate": per_minute_rate,
        "Trip_Duration_Minutes": duration,
        "Time_of_Day": time_of_day,
        "Day_of_Week": day_of_week,
        "Traffic_Conditions": traffic_conditions,
        "Weather": weather
    }
    try:
        response = predict_price(payload=payload).json()
        price = response.get("predicted_price")
        st.markdown(f"**Predikterat pris: {price:.2f} USD**")
    except Exception as e:
        st.markdown(f"Fel: {e}")