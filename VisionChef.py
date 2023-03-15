#dont forget to add secrets to streamlit cloud settings, just copy what's inside secrets.toml

import streamlit as st
from functions import *
import requests
from backend.api.restegourmet import *
import shutil
from PIL import Image

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


col1, col2 = st.columns([1, 5])

with col1:
    image = Image.open("logo.png")
    st.image(image, use_column_width=True)
with col2:
    st.markdown("# VisionChef")

## From fridge to feast
st.markdown("""
### Take a snap, cook like a pro!
##### 📷 1. Take a picture of your leftover ingredients
##### 📜 2. Get recipes for gourmet meals
""")

#not sure what this does
#st.set_option('deprecation.showfileUploaderEncoding', False)

# File upload
uploaded_file = st.file_uploader("Upload an image ", type=["jpg", "jpeg", "png"])

# Define function to save uploaded image to temporary file
def save_to_temp_file(uploaded_file):
    """
    Save the uploaded image to a temporary file.
    """
    with open("temp_file_from_user.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

# Define function to copy image to root folder
def save_image_to_root(image_path):
    """
    Save the image to the root folder.
    """
    # Create a new image path with the desired name
    new_image_path = "temp_file_from_user.jpg"

    # Copy the image to the new path
    shutil.copy2(image_path, new_image_path)

# Define the list of example images
example_images = [
    'sample_images/Apple-Puree-3-Ways-2.jpg',
    'sample_images/carbropotonionbean.jpg',
    'sample_images/tomeggon.jpg'
]

# Save uploaded file if available
#if uploaded_file is not None:
    #save_to_temp_file(uploaded_file)

# Create the expandable element
with st.expander("or select one from our examples"):
    # Show the example images
    st.subheader("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(example_images[0], width=200)
    with col2:
        st.image(example_images[1], width=200)
    with col3:
        st.image(example_images[2], width=200)

    # Create the radio buttons
    option = st.radio(
        "",
        ("My uploaded image", "Example 1", "Example 2", "Example 3"),
        index=0
    )

    # Determine which image to use and save it to the root folder if it's an example image
    if option == "My uploaded image" and uploaded_file is not None:
        image_url = "temp_file_from_user.jpg"
    #    save_to_temp_file(uploaded_file)
    elif option == "Example 1":
        image_url = example_images[0]
        save_image_to_root(image_url)
    elif option == "Example 2":
        image_url = example_images[1]
        save_image_to_root(image_url)
    elif option == "Example 3":
        image_url = example_images[2]
        save_image_to_root(image_url)

def show_URL(codes):
    #convert codes to EN list
    en_ingr = get_values_from_dict(codes,int_EN_dict)
    st.write("We found the following ingredients:")
    st.write(", ".join(en_ingr))

    #convert EN list to DE for URL
    de_ingr = EN2DE(en_ingr, EN_DE_dict)
    st.write("To see some tasty recipes from restegourmet.de:")
    url_to_visit = generate_restegourmet_url(de_ingr)
    st.write(url_to_visit)

def show_widgets(codes):
    # Convert codes to EN list
    en_ingr = get_values_from_dict(codes, int_EN_dict)
    en_str = ", ".join(en_ingr)
    st.write(f"We found the following ingredients: {en_str}")

    # Convert EN list to DE for API
    de_ingr = EN2DE(en_ingr, EN_DE_dict)

    # Get recipes via images and links
    st.write("Tasty recipes from restegourmet.de:")
    stuff = ",".join(de_ingr)
    everything = check_image_urls(must_can_funct(stuff)[:6])
    # If you want to use hardcoded list
    # everything = search_content("birne,nektarine")

    #ADJUST HOW MANY RECIPES WE SHOW
    recipes = everything[:6]

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

def call_api(uploaded_file):
    # convert API response which is a dict, to a list of classes (code names)
    #!!!!!!!!threshold is used here!!!!
    #uncomment st.write to see what is the API response
    #st.write(response.json())
    api_url = "https://new-phec24vmza-ey.a.run.app/predict"
    params = {"image_filename": uploaded_file.getbuffer()}
    response = requests.post(api_url, files=params)
    return filter_dict_by_value(response.json(),"0.2")

def relabel(codes):
    with st.expander("You can re-label your ingredients"):
        #st.image(uploaded_file, use_column_width=True)
        selected = st.multiselect("", unique_values(int_EN_dict), get_values_from_dict(codes,int_EN_dict))
        #st.write("You selected:", selected)
        codes = lookup_keys(selected, int_EN_dict)
        #st.write(codes)
        return codes


if uploaded_file is not None:
    with open("temp_file_from_user.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    codes = call_api(uploaded_file)
    codes = relabel(codes)
    #show_URL(codes)
    show_widgets(codes)


if uploaded_file is None and option != "My uploaded image":
    codes = call_api()
    codes = relabel(codes)
    #show_URL(codes)
    show_widgets(codes)
