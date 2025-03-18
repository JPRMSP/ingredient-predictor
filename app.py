import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("ingredient_model.pkl")

# Function to set background image
def set_bg_image():
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://source.unsplash.com/1600x900/?food,kitchen");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    [data-testid="stSidebar"], .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 10px;
    }

    /* Style buttons */
    .stButton>button {
        background-color: #ff6347;
        color: white;
        font-size: 16px;
        border-radius: 5px;
    }

    /* Style text */
    .stMarkdown, .stText {
        color: #333;
        font-size: 18px;
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# Apply background styling
set_bg_image()

# Add logo
st.image("https://upload.wikimedia.org/wikipedia/commons/6/6a/Baking_icon.svg", width=120)

# App title
st.title("🍽️ Precision Baking - AI Ingredient Measurement")

# Description
st.write("Enter the ingredient details below to get an accurate weight prediction.")

# User input form
with st.form("ingredient_form"):
    ingredient = st.selectbox("Select Ingredient", ["Flour", "Sugar", "Milk", "Butter", "Eggs"])
    volume = st.number_input("Enter Volume (ml)", min_value=1.0, step=1.0)
    density = st.number_input("Enter Density (g/ml)", min_value=0.1, step=0.1)

    # Submit button
    submit_button = st.form_submit_button("Calculate Weight")

# Predict weight
if submit_button:
    weight = model.predict(np.array([[volume, density]]))[0]  # Make prediction
    st.success(f"Predicted Weight: **{weight:.2f} grams**")  # Display result
