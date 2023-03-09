import streamlit as st
from functions import *
import requests

#title
st.markdown("""# Image to recipes
## Turn leftover ingredients into gourmet meals:
### 📷 1. Take a picture of your ingredients
### 📜 2. Get recipes
""")

st.set_option('deprecation.showfileUploaderEncoding', False)

#file upload
uploaded_file = st.file_uploader("Upload an image of your ingredients", type=["jpg", "jpeg", "png"])


####you might need to adjust the api_url variable!!!!!!!
# If an image is uploaded
if uploaded_file is not None:
    # Save the image to a temporary location
    with open("temp_file_from_user.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Call the API with the image filename parameter
    api_url = "http://127.0.0.1:8000/predict?"
    params = {"image_filename": "temp_file_from_user.jpg"}
    response = requests.get(api_url, params=params)

    # convert API response which is a dict, to a list of classes (code names)
    #threshold is used here!!!!
    #uncomment st.write to see what is the API response
    #st.write(response.json())
    codes = filter_dict_by_value(response.json(),"0.2")

    #convert codes to EN list
    en_ingr = get_values_from_dict(codes,int_EN_dict)
    st.write("We found the following ingredients:")
    st.write(", ".join(en_ingr))

    #convert EN list to DE list
    de_ingr = EN2DE(en_ingr, EN_DE_dict)
    st.write("To see some tasty recipes from restegourmet.de, click on the link below")
    url_to_visit = generate_restegourmet_url(de_ingr)
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
