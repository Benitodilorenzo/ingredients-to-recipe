import requests
import streamlit as st


def search_content(ingredient_slugs,behaviour):
    #as behaviour use "must" or "can"
    key = st.secrets.restegourmet_token.token
    base_url = 'https://superserve.restegourmet.de/api/ext'
    endpoint = '/content/search'
    headers = {'Authorization': f'Token {key}'}
    params = {f"ingredient_slugs_{behaviour}": ingredient_slugs}
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

def must_can_funct(ingredient_slugs):
    hits = search_content(ingredient_slugs, "must")["recipes"]["hits"]
    if hits:
        return extract_from_hits(search_content(ingredient_slugs, "must"))
    else:
        return extract_from_hits(search_content(ingredient_slugs, "can"))

def check_image_urls(json_data):
    for item in json_data:
        try:
            response = requests.get(item['image_url'])
            if response.status_code == 404:
                item['image_url'] = 'https://images.eatsmarter.de/sites/default/files/404seite.png'
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            continue
    return json_data
