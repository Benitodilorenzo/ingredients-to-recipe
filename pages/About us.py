import streamlit as st
from PIL import Image

st.markdown('# Meet our team')

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/pastel-yellow-soft-gradient-blur-background_53876-105434.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

col1, col2 = st.columns(2)

with col1:
    st.markdown('#### Benjamin di Lorenzo')
    st.image('pages/Benjamin.png', width = 200)
    st.markdown('#### Viktor Zöld')
    st.image('pages/Victor.png', width = 200)


with col2:
    st.markdown('#### Pratima Thapa')
    st.image('pages/Pratima.png', width = 200)
    st.markdown('#### Pavan Kumar Hosakere Mathada')
    st.image('pages/Pavan.png', width = 200)
