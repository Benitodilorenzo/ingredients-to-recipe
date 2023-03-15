import streamlit as st
from PIL import Image

st.markdown('# About the app')

#Creating a background

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

st.markdown('###### This app is the final project we developed over the last few days at Le Wagon\'s data science bootcamp in March 2023.')

st.markdown("- Our app recognizes ingredients on uploaded images using a powerful algorithm called yolov7. We trained this Convolutional Neural Network on a dataset of 20,000 images featuring 24 categories of ingredients (fruits & vegetables).")
st.markdown("- We created a FastAPI to run the object detection on the uploaded image and return objects and their confidence levels.")
st.markdown("- We've also integrated Restegourmet's API, which provides a wide range of recipes in German.")

st.markdown("###### We\'d like to thank Restegourmet for their cooperation and Le Wagon\'s teachers for their guidance and endless patience. We\'re proud to present this app as the culmination of our efforts, and we hope that you find it useful and enjoyable.")
