from os import environ
from requests import get


def get_description(product_id):
    url = f'{environ.get("API_URL")}/{product_id}'
    response = get(url)
    if response.status_code != 200:
        return {}
    return response.json()
