import streamlit as st
import pandas as pd
import joblib

# Load your trained model
model = joblib.load("decision_tree_calories.joblib")

# App title
st.title("🔥 Calories Burned Predictor 🔥")
st.write("Enter your details to estimate calories burned during exercise.")

# Input fields
weight = st.number_input("Weight (kg):", min_value=1)
age = st.number_input("Age:", min_value=1)
gender = st.selectbox("Gender:", ["Male", "Female"])
exercise_type = st.selectbox("Exercise Type:", ["Running", "Cycling", "Walking", "Other"])
duration = st.number_input("Exercise Duration (minutes):", min_value=1)
heart_rate = st.number_input("Heart Rate (bpm):", min_value=1)

# Prepare input with one-hot encoding
input_df = pd.DataFrame({
    "Age": [age],
    "Duration": [duration],
    "Heart Rate": [heart_rate],
    "Weight": [weight],
    "Gender_Male": [1 if gender == "Male" else 0],
    "Gender_Female": [1 if gender == "Female" else 0],
    "Exercise_Running": [1 if exercise_type == "Running" else 0],
    "Exercise_Cycling": [1 if exercise_type == "Cycling" else 0],
    "Exercise_Walking": [1 if exercise_type == "Walking" else 0],
    "Exercise_Other": [1 if exercise_type == "Other" else 0]
})

# Ensure all columns match model training order
expected_cols = model.feature_names_in_
for col in expected_cols:
    if col not in input_df.columns:
        input_df[col] = 0  # fill missing columns with 0

input_df = input_df[expected_cols]  # reorder columns

# Prediction
if st.button("Predict Calories Burned"):
    calories = model.predict(input_df)
    st.success(f"Estimated Calories Burned: {calories[0]:.2f} kcal")

