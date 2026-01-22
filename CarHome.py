# cd "D:\Python\python\car crash"

# py -m streamlit run CarHome.py

import streamlit as st
from PIL import Image
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Car Crash Analysis",
    page_icon="🚗",
    layout="wide"
)

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center;'>🚗 Car Crashes Data Analysis</h1>",
    unsafe_allow_html=True
)

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- DEBUG (REMOVE LATER IF YOU WANT) ----------------
st.write("Files in current directory:", os.listdir())

# ---------------- IMAGE SECTION ----------------
try:
    img = Image.open("suren.avif")   # image MUST be in same folder
    st.image(img, use_container_width=True)
except Exception as e:
    st.error("❌ Image load nahi ho pa rahi. File name ya path check karo.")
    st.exception(e)

# ---------------- DESCRIPTION ----------------
st.markdown("""
## 📊 Project Overview

This dashboard presents a comprehensive analysis of **car crash data across different states**, 
focusing on key risk factors such as:

- 🍺 Alcohol consumption  
- 🚦 Speeding  
- 🧠 Driver behavior  

### 🎯 Objective
The objective of this analysis is to:
- Identify **high-risk and low-risk regions**
- Understand **accident patterns**
- Evaluate impact on **insurance premiums and losses**

### 💡 Impact
By leveraging **data-driven insights**, this dashboard helps:
- Insurance companies  
- Data analysts  
- Policy makers  

to design **risk-based pricing strategies**, optimize policies, and promote **road safety initiatives**.
""")

st.markdown("<hr>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    "<p style='text-align:center; color:grey;'>Created by Surend | Streamlit Dashboard</p>",
    unsafe_allow_html=True
)





