import streamlit as st
import numpy as np
import pickle
import os

st.title("🔥 Calories Burned Predictor")

# Check if model file exists
model_path = "calorie_model.pkl"
if not os.path.exists(model_path):
    st.error("🚫 Model file not found. Please place 'calorie_model.pkl' in this folder.")
    st.stop()

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

# UI Inputs
age = st.slider("Age", 10, 80, 25)
gender = st.selectbox("Gender", ["male", "female"])
duration = st.slider("Workout Duration (minutes)", 1, 180, 30)
heart_rate = st.slider("Heart Rate", 60, 200, 120)
body_temp = st.slider("Body Temperature (°C)", 36.0, 40.0, 37.0)
height = st.slider("Height (cm)", 120, 220, 170)
weight = st.slider("Weight (kg)", 40, 150, 70)


# Encode gender
gender_num = 0 if gender == "male" else 1

# Make prediction
features = np.array([[age, gender_num, height, weight, duration, heart_rate, body_temp]])
calories = model.predict(features)[0]

st.success(f"🔥 Estimated Calories Burned: {calories:.2f} kcal")
