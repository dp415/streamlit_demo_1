import streamlit as st
from utils import read_data, set_background, head, body
from data_location import data_location

address_type = "url"

data_location = data_location[address_type]

st.set_page_config(
    page_title = 'Math Problem Generator',
    page_icon = data_location['page_icon']
)

set_background(address_type,data_location['background'])

head()

if st.button('Bring it on!'):
    df = read_data(data_location['math_problems'])
    choice = df.sample(1)
    body(choice)