import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

df_path = r'C:\Users\luffy\Laptop-Price-Predictor\df.pkl'

try:
    with open(df_path, 'rb') as f:
        df = pickle.load(f)

    if not isinstance(df, pd.DataFrame):
        raise ValueError("Loaded 'df.pkl' is not a valid DataFrame.")

except FileNotFoundError as e:
    st.error(f"File not found: {str(e)}")
    st.stop()

except Exception as e:
    st.error(f"Error loading the dataset: {str(e)}")
    st.stop()

st.title("Laptop Price Predictor")

company = st.selectbox('Brand', df['Company'].unique()) if 'Company' in df.columns else st.stop()
type = st.selectbox('Type', df['TypeName'].unique()) if 'TypeName' in df.columns else st.stop()
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
weight = st.number_input('Weight of the Laptop')
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
touchscreen = 1 if touchscreen == 'Yes' else 0
ips = st.selectbox('IPS', ['No', 'Yes'])
ips = 1 if ips == 'Yes' else 0
screen_size = st.slider('Screen Size (in inches)', 10.0, 18.0, 13.3)

resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160',
    '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
])

cpu = st.selectbox('CPU', df['Cpu brand'].unique()) if 'Cpu brand' in df.columns else st.stop()
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
gpu = st.selectbox('GPU', df['Gpu brand'].unique()) if 'Gpu brand' in df.columns else st.stop()
os = st.selectbox('OS', df['os'].unique()) if 'os' in df.columns else st.stop()

# Predict
if st.button('Predict Price'):
    
    X_res, Y_res = map(int, resolution.split('x'))
    ppi = np.sqrt(X_res**2 + Y_res**2) / screen_size

    
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])
    query = query.reshape(1, -1)

    
    dummy_price = 59999 + (ram * 1000) + (ssd * 5) - (weight * 100)
    st.title(f"The predicted price of this configuration is: ₹{int(dummy_price)}")
