import streamlit as st
from PIL import Image
import os

# Page configuration
st.set_page_config(
    page_title="Car Crash Analysis",
    page_icon="🚗",
    layout="wide"
)

# Title
st.markdown(
    "<h1 style='text-align:center;'>🚗 Car Crashes Data Analysis</h1>",
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# Image (Cloud-safe path)
base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir, "suren.avif")

img = Image.open(image_path)
st.image(img, use_container_width=True)

# Description
st.markdown("""
## 📊 Project Overview

This dashboard presents a comprehensive analysis of **car crash data across different states**,
focusing on key risk factors such as:

- Alcohol consumption  
- Speeding  
- Driver behavior  

### 🎯 Objective
- Identify high-risk and low-risk regions  
- Understand accident patterns  
- Evaluate impact on insurance premiums and losses  

### 💡 Impact
This dashboard supports insurance companies, analysts, and policymakers in building
risk-based strategies and promoting road safety initiatives.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# Footer
st.markdown(
    "<p style='text-align:center; color:grey;'>Created by Surend | Streamlit Dashboard</p>",
    unsafe_allow_html=True
)










