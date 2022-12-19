"""
Utility functions for:
    1. reading data
    2. setting background
    3. writing head and body
"""

import base64
import pandas as pd
import streamlit as st

@st.cache(suppress_st_warning=True)

def read_data(path):
    return pd.read_csv(path)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data)

def set_background(address_type,address):
    if(address_type=="url"):
        st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("{address}");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
        )
    elif(address_type=="local"): #handle as local file
        bin_str = get_base64(address)
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"png"};base64,{bin_str.decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    else: #error: address_type not an acceptible type
        return False

def head():
    st.markdown("""
        <h1 style='text-align: center; margin-bottom: -35px;'>
        Math Problem Generator
        </h1>
    """, unsafe_allow_html=True
    )
    
    st.caption("""
        <p style='text-align: center'>
        by <a href='https://medium.com/geoclid'>Geoclid</a>
        </p>
    """, unsafe_allow_html=True
    )
    
    st.write(
        "Feeling overwhelmed by your daily grind?",
        "Looking for something fun to do?",
        "Click the button for a random math problem \U0001F642."
    )

def body(sample):
    name = sample.iloc[0, 0]
    link = sample.iloc[0, 1]
    prob = sample.iloc[0, 2]
    st.info(f'### {name}')
    st.write(prob)
    st.caption(f'[source]({link})')
    st.markdown('---')