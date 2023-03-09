import streamlit as st
from streamlit_option_menu import option_menu
from functions import *


#title
st.markdown("""# Ingredients to recipes
## Turn leftovers into gourmet meals in 2 steps!
### 📷 1. Take a picture of your ingredients
### 📜 2. Get recipes
""")

st.set_option('deprecation.showfileUploaderEncoding', False)

#file upload
uploaded_file = st.file_uploader("Upload an image of your ingredients")

#dummy ingredients, normally provided by API
ingredients_EN = ["tomato yellow","cactus fruit","grape white","grape white 3","redcurrant"]

#translate list to DE
ingredients_DE = EN2DE(ingredients_EN,translations)

#generate URL
url_to_visit = generate_restegourmet_url(ingredients_DE)

#if an image is uploaded, show recipe
if uploaded_file is not None:
    st.write("We found the following ingredients:")
    st.write(", ".join(ingredients_EN))
    st.write("To see some tasty recipes from restegourmet.de, click on the link below")
    st.write(url_to_visit)

#background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2017/10/22/20/42/table-2879213_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
