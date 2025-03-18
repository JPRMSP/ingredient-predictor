import streamlit as st

# Function to set background image
def set_bg_image():
    page_bg = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://raw.githubusercontent.com/JPRMSP/ingredient-predictor/main/images.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    [data-testid="stSidebar"], .block-container {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background-color: #ff6347;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 8px 15px;
        border: none;
    }
    .stMarkdown, .stText {
        color: #333;
        font-size: 18px;
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# Set the background image
set_bg_image()

# Display a logo (Replace with your own image URL)
st.image("https://raw.githubusercontent.com/your-github-username/your-repo/main/logo.png", width=150)

# App Title
st.title("🍽️ Precision Baking - AI Ingredient Measurement")

# App Description
st.write("Enter the ingredient details below to get accurate weight predictions.")

# Input fields
ingredient = st.text_input("Ingredient Name", placeholder="e.g., Sugar")
volume = st.number_input("Enter Volume (ml)", min_value=0.0, format="%.2f")
density = st.number_input("Enter Density (g/ml)", min_value=0.0, format="%.2f")

# Prediction Button
if st.button("Predict Weight"):
    if volume > 0 and density > 0:
        weight = volume * density
        st.success(f"Estimated Weight: {weight:.2f} grams")
    else:
        st.error("Please enter valid values for volume and density.")
