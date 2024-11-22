import streamlit as st
import pickle as pk
import numpy as np
import joblib
# Load the model
# model = pk.load(open('bike_prediction.pkl', 'rb'))
# model=joblib.load('linear-model.lb')
# model = pk.load(open('bike_prediction.pkl', 'rb'))
model=joblib.load('scaled_xg.lb')
scaler=joblib.load('scaler.lb')


# Title of the app
st.title('Bike Price Prediction')

# Dictionary for brand mapping
d = {
    'TVS': 0,
    'Royal Enfield': 1,
    'Triumph': 2,
    'Yamaha': 3,
    'Honda': 4,
    'Hero': 5,
    'Bajaj': 6,
    'Suzuki': 7,
    'Benelli': 8,
    'KTM': 9,
    'Mahindra': 10,
    'Kawasaki': 11,
    'Ducati': 12,
    'Hyosung': 13,
    'Harley-Davidson': 14,
    'Jawa': 15,
    'BMW': 16,
    'Indian': 17,
    'Rajdoot': 18,
    'LML': 19,
    'Yezdi': 20,
    'MV': 21,
    'Ideal': 22,
}

# Extract brands for selectbox
brands = list(d.keys())

# Sidebar for input parameters
st.sidebar.title("Input Parameters")
brand_name = st.sidebar.selectbox("Select Brand Name", brands,index=0)

kms_driven = st.sidebar.slider("Kms Driven", 1, 80000, 20000)
age = st.sidebar.slider("Age (years)", 1, 16, 5)
power = st.sidebar.slider("Power (cc)", 100, 800, 150)
owner = st.sidebar.slider("Owner", 1, 3, 1)

# Display the inputs
st.write("### Model Inputs")
st.write(f"Owner: {owner}")
st.write(f"Brand: {brand_name}")
st.write(f"Kms Driven: {kms_driven}")
st.write(f"Age: {age}")
st.write(f"Power: {power}")

# Predict the price
brand_index = d[brand_name]  # Get the brand index from the dictionary
prediction = model.predict(scaler.transform([[owner, brand_index, kms_driven, age, power]]))

# Display the prediction
st.subheader(f"Predicted Price of Bike is: Rs. {np.round(prediction.ravel()[0], 4)}")
