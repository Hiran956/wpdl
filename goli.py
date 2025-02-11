import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("goli_soda_risk_model.joblib")

# Streamlit UI
st.title("🧪 Goli Soda Manufacturing Risk Predictor")
st.write("Predict the defect percentage in Goli Soda production.")

# User Inputs
sugar = st.slider("Sugar (g/L)", 140, 180, 160)
co2 = st.slider("CO₂ Pressure (psi)", 35, 45, 40)
temp = st.slider("Bottle Temp (°C)", 15, 22, 18)
ph = st.slider("pH Level", 3.0, 3.5, 3.2)
time = st.slider("Production Time (mins)", 25, 35, 30)

# Predict Button
if st.button("Predict Defect Percentage"):
    input_data = np.array([[sugar, co2, temp, ph, time]])
    prediction = model.predict(input_data)[0]
    st.success(f"📉 Predicted Defective Percentage: **{prediction:.2f}%**")
