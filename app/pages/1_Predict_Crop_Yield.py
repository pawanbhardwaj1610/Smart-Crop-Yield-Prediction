import streamlit as st

from app.utils import make_prediction

st.set_page_config(page_title="Predict Crop Yield", layout="wide")

st.title("🌾 Predict Crop Yield")
st.markdown("Enter the crop and environmental information to generate a prediction.")

states = [
    "Assam",
    "Punjab",
    "Karnataka",
    "Kerala",
    "Tamil Nadu",
    "Maharashtra",
    "Uttar Pradesh",
    "West Bengal",
    "Haryana",
    "Gujarat",
]
crops = [
    "Wheat",
    "Rice",
    "Maize",
    "Sugarcane",
    "Cotton",
    "Gram",
    "Potato",
    "Jute",
    "Groundnut",
    "Millets",
]

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        state = st.selectbox("State", states)
        crop = st.selectbox("Crop", crops)
        year = st.number_input("Year", min_value=2000, max_value=2050, value=2024)
        rainfall = st.number_input("Annual Rainfall", min_value=0.0, value=800.0)
        temperature = st.number_input("Average Temperature", min_value=0.0, value=25.0)
        humidity = st.number_input("Humidity", min_value=0.0, value=60.0)
    with col2:
        nitrogen = st.number_input("Nitrogen", min_value=0.0, value=120.0)
        phosphorus = st.number_input("Phosphorus", min_value=0.0, value=40.0)
        potassium = st.number_input("Potassium", min_value=0.0, value=20.0)
        ph = st.number_input("Soil pH", min_value=0.0, value=6.5)
        season = st.selectbox("Season", ["Kharif", "Rabi", "Summer", "Winter", "Whole Year"])

    submitted = st.form_submit_button("Predict Yield")

if submitted:
    payload = {
        "Crop": crop,
        "Year": int(year),
        "State": state,
        "Area": 100.0,
        "Production": 200.0,
        "Rainfall": float(rainfall),
        "Temperature": float(temperature),
        "Humidity": float(humidity),
        "N": float(nitrogen),
        "P": float(phosphorus),
        "K": float(potassium),
        "pH": float(ph),
        "Season": season,
        "Annual_Rainfall": float(rainfall),
        "Fertilizer": 1000.0,
        "Pesticide": 200.0,
        "avg_temp_c": float(temperature),
        "total_rainfall_mm": float(rainfall),
        "avg_humidity_percent": float(humidity),
    }

    try:
        result = make_prediction(payload)
        st.success(f"Predicted Yield: {result.get('Predicted Yield', 'N/A')} Tons/Hectare")
    except Exception as exc:
        st.error(str(exc))
