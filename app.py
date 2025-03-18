import streamlit as st
import joblib

# Load the trained model
model = joblib.load("ingredient_model.pkl")

# Web App Title
st.title("AI-Powered Ingredient Weight Predictor")

# Take User Inputs
volume = st.number_input("Enter Volume (ml):", min_value=1, step=1)
density = st.number_input("Enter Density (g/ml):", min_value=0.1, step=0.01)

# Button to Predict
if st.button("Predict Weight"):
    prediction = model.predict([[volume, density]])[0]
    st.success(f"Predicted Weight: {prediction:.2f} grams")
