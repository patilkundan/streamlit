import numpy as np
import pandas as pd
import pickle
import streamlit as st
import joblib  # Import joblib to load the model

# Define the path to your model
# model_path = r"C:\Users\Kundan Patil\DS0522\Evaluation Phase- Batch DS0522\12\model.pkl"

# Load your model here
model = joblib.load("model.pkl")

# Streamlit app title
st.title("Shopping Card Eligibility Prediction")

# Add LinkedIn and GitHub logos in one line at the top of the sidebar with center alignment
st.sidebar.markdown(
    """
    <div style="display: flex; align-items: left; justify-content: left;">
        <a href='https://www.linkedin.com/in/kundanpatilds/' target='_blank' style="margin-right: 5px;">
            <img src='https://raw.githubusercontent.com/patilkundan/images/a324e86ac65c421634bc45eb8c057cdc7b453d3a/linkedin-svgrepo-com.svg' alt='LinkedIn' width='24'>
        </a>
        <a href='https://github.com/patilkundan?tab=repositories' target='_blank'>
            <img src='https://raw.githubusercontent.com/patilkundan/images/421fe319d64da3b7bd4fd627b248299735085d47/github-142-svgrepo-com.svg' alt='GitHub' width='19'>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar with Additional information
st.sidebar.title("About Project")
st.sidebar.markdown("**Objective:** Developed a ML Model for Retail Store Product Demand Forecasting and Shopping Card Eligibility.")
st.sidebar.markdown("**Impact:** The predictive classification model revolutionized the company's shopping card acquisition strategy, significantly diminishing the need for labor-intensive customer outreach efforts. This shift led to substantial increases in both customer acquisition and retention rates, making a significant contribution to the company's overall growth and profitability")
# Link to the full article
st.sidebar.markdown("[Visit the full article](https://www.linkedin.com/pulse/revolutionizing-shopping-card-acquisition-ml-case-study-kundan-patil)")



# Input fields
purchase_rate = st.slider("Purchase Rate", 1.0, 100.0, 50.0)
Spending_Score = st.slider("Spending Score", 302, 850, 576)
visit_frequency = st.slider("Frequency of Visits", 1, 100, 10)

# Make a prediction
def predict_eligibility(purchase_rate, Spending_Score, visit_frequency):
    # Prepare input features as a list or a numpy array
    input_data = [[purchase_rate, Spending_Score, visit_frequency]]
    
    # Make the prediction
    prediction = model.predict(input_data)[0]

    return prediction

# Display the prediction result
if st.button("Predict"):
    result = predict_eligibility(purchase_rate, Spending_Score, visit_frequency)
    if result == 1:
        st.success("Great! Person is eligible for a shopping card: 😀🛒💰")
    else:
        st.error("Oh! Person is not eligible for a shopping card: 😥😢🛒❌ Don't worry! You can still keep shopping")

# Center-align the author information at the bottom of the app
st.markdown("<p style='text-align:center;'>@Author: Kundan Patil | <a href='https://www.linkedin.com/in/kundanpatilds/'>LinkedIn</a></p>", unsafe_allow_html=True)

