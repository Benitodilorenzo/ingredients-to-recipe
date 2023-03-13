#dont forget to add secrets to streamlit cloud settings, just copy what's inside secrets.toml


import streamlit as st
from functions import *
import requests
from backend.api.restegourmet import *
import webbrowser

#background image
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


#title
st.markdown("""# VisionChef
### Take a snap, cook like a pro!
##### 📷 1. Take a picture of your leftover ingredients
##### 📜 2. Get recipes for gourmet meals
""")

st.set_option('deprecation.showfileUploaderEncoding', False)

#file upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])


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
    #!!!!!!!!threshold is used here!!!!
    #uncomment st.write to see what is the API response
    #st.write(response.json())
    codes = filter_dict_by_value(response.json(),"0.2")

    #convert codes to EN list
    en_ingr = get_values_from_dict(codes,int_EN_dict)
    st.write("We found the following ingredients:")
    st.write(", ".join(en_ingr))

    #convert EN list to DE
    de_ingr = EN2DE(en_ingr, EN_DE_dict)

    #get recipes via URL
    st.write("To see some tasty recipes from restegourmet.de, click on the link")
    url_to_visit = generate_restegourmet_url(de_ingr)
    st.write(url_to_visit)

    #get recipes via images and links
    st.write("Here are some tasty from restegourmet.de:")
    #st.write(de_ingr)
    stuff = ",".join(de_ingr)
    everything = search_content(stuff)
    #st.write(stuff)

    ##if you want to use hardcoded list
    #everything = search_content("birne,nektarine")

    #ADJUST HOW MANY RECIPES WE SHOW
    recipes = extract_from_hits(everything)[:4]

    #widgets
    num_columns = 3
    for i in range(0, len(recipes), num_columns):
        row = recipes[i:i+num_columns]
        columns = st.columns(num_columns)
        for j, recipe in enumerate(row):
            with columns[j]:
                st.image(recipe["image_url"], use_column_width=True)
                #st.write(recipe["name"])
                #st.write(recipe["url"])
                st.markdown(f'<a href="{recipe["url"]}" target="_blank">{recipe["name"]}</a>', unsafe_allow_html=True)
