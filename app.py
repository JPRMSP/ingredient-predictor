import streamlit as st
import joblib
import os

# Load the trained model
model_path = "ingredient_model.pkl"
if not os.path.exists(model_path):
    st.error("Model file not found! Please upload `ingredient_model.pkl` to the same directory.")
else:
    model = joblib.load(model_path)

# Web App Title
st.title("AI-Powered Ingredient Weight Predictor")

# Take User Inputs
volume = st.number_input("Enter Volume (ml):", min_value=1, step=1)
density = st.number_input("Enter Density (g/ml):", min_value=0.1, step=0.01)

# Button to Predict
if st.button("Predict Weight"):
    prediction = model.predict([[volume, density]])[0]
    st.success(f"Predicted Weight: {prediction:.2f} grams")
