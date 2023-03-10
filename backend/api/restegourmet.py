import requests
import streamlit as st


def search_content(ingredient_slugs_must):
    key = st.secrets.restegourmet_token.token
    base_url = 'https://superserve.restegourmet.de/api/ext'
    endpoint = '/content/search'
    headers = {'Authorization': f'Token {key}'}
    params = {'ingredient_slugs_must': ingredient_slugs_must}
    response = requests.get(base_url + endpoint, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Request failed with error code {response.status_code}')


def extract_from_hits(myjson):
    """
    Process a JSON object and return a list of dictionaries representing
    recipe hits, where each dictionary contains keys "image_url", "url",
    and "name" with corresponding values.
    """
    hits_list = []
    for hit in myjson["recipes"]['hits']:
        hit_dict = {
            "image_url": hit['image_url'],
            "url": hit['url'],
            "name": hit['name']
        }
        hits_list.append(hit_dict)
    return hits_list
