import streamlit as st
import requests

st.title("Supermarket Sales Forecast")

# Input sliders or number inputs
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):
    data = {
        "feature1": feature1,
        "feature2": feature2,
        "feature3": feature3
    }
    response = requests.post("https://YOUR_DEPLOYED_API_URL/predict", json=data)
    st.write("Prediction:", response.json()["prediction"])
