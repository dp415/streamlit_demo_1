import streamlit as st
from utils import read_data, head, body, set_bg, add_bg_from_local, add_bg_from_url
from data_location import data_location

address_type = "local" #local or url

data_location = data_location[address_type] #declare the data source depending upon the version: development = offline, publish = online

st.set_page_config(
    page_title = 'Math Problem Generator',
    page_icon = data_location['page_icon']
)

set_bg(data_location['background'])
#set_background(address_type,data_location['background'])
#add_bg_from_local('../assets/background.png')
#add_bg_from_url(data_location['background'])

head()

if st.button('Bring it on!'):
    df = read_data(data_location['math_problems'])
    #df = read_data('../data/olympiad-problems.csv')
    choice = df.sample(1)
    body(choice)