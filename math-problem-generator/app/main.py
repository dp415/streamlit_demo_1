import streamlit as st
from utils import read_data, head, body, set_bg, add_bg_from_local, add_bg_from_url

st.set_page_config(
    page_title='Math Problem Generator',
    page_icon='assets/icon.png'
)

#set_bg('assets/background.png')
#add_bg_from_local('assets/background.png')
add_bg_from_url('https://raw.githubusercontent.com/dp415/streamlit_demo_1/main/math-problem-generator/assets/background.png')

head()

if st.button('Bring it on!'):
    df = read_data('https://raw.githubusercontent.com/dp415/streamlit_demo_1/testing2.0-0-SmallerFile/math-problem-generator/data/olympiad-problems2.csv')
    choice = df.sample(1)
    body(choice)