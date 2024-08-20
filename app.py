import streamlit as st
import pickle
import numpy as np
import pandas as pd
import altair as alt

# Load the Random Forest model
model_path = "Random_Forest_Regressor.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

st.image(r"Diamond Banner.jpg")

# Define the Streamlit app
st.title('Diamond Price Prediction')
st.header('Fill the Details to Predict Diamond price')

# Define input fields for all features used in the model
st.image(r"D:\PYTHON1\Advance ML Project Using Chatgpt\Carat weight 1.png")
carat = st.number_input('Carat', min_value=0.0, max_value=5.0, step=0.01)

st.image(r"D:\PYTHON1\Advance ML Project Using Chatgpt\Cut 1.png") 
cut = st.selectbox('Cut', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])

st.image(r"D:\PYTHON1\Advance ML Project Using Chatgpt\Colour 1.png")
color = st.selectbox('Color', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])

st.image(r"D:\PYTHON1\Advance ML Project Using Chatgpt\Clarity 1.png")
clarity = st.selectbox('Clarity', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])

depth = st.number_input("Depth: Percentage of diamond's height", min_value=50.0, max_value=70.0, step=0.1)

table = st.number_input('Table (Width of the Top of Diamond relative to widest point)', min_value=50.0, max_value=70.0, step=0.1)
x = st.number_input('X (length in mm)', min_value=0.0, max_value=10.0, step=0.1)
y = st.number_input('Y (width in mm)', min_value=0.0, max_value=10.0, step=0.1)
z = st.number_input('Z: Vertical diamond height (depth in mm)', min_value=0.0, max_value=10.0, step=0.1)

# Make prediction
if st.button('Predict'):
    input_data = pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]],
                              columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z'])
    prediction = model.predict(input_data)[0]
    st.write(f'The predicted price of the diamond is ₹{prediction:.2f}')

