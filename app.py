import streamlit as st
import joblib
import numpy as np

# 🎨 Function to Apply Background Image & Styling
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
    /* Button Styling */
    .stButton>button {
        background-color: #ff6347;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px;
    }
    /* Change text color */
    .stMarkdown, .stText {
        color: #333;
        font-size: 18px;
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# Call the function to set UI styles
set_bg_image()

# 🌟 Load the Ingredient Prediction Model
model = joblib.load("ingredient_model.pkl")

# 🌟 Add a Logo & Title
st.image("https://upload.wikimedia.org/wikipedia/commons/6/6a/Baking_icon.svg", width=100)
st.title("🍽️ Precision Baking - AI Ingredient Measurement")

# 📌 User Inputs
st.subheader("🔢 Enter Ingredient Details")
volume = st.number_input("Enter Volume (ml):", min_value=0.0, step=1.0)
density = st.number_input("Enter Density (g/ml):", min_value=0.0, step=0.1)

# 🎯 Predict Weight
if st.button("⚡ Predict Weight"):
    if volume > 0 and density > 0:
        weight = model.predict(np.array([[volume, density]]))
        st.success(f"✅ Predicted Weight: **{weight[0]:.2f} grams**")
    else:
        st.warning("⚠️ Please enter valid values for volume and density!")

# 📌 Footer
st.markdown("---")
st.markdown("🔗 Developed by **Your Name** | Powered by **AI & Streamlit**")
