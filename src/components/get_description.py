import pandas as pd

from src.api import get_description as get_description_api


def get_description(product_id):
    description = get_description_api(product_id)
    if description != {}:
        data = {
            'id': [product_id],
            'description': [description['description']],
            'positive': [description['positive']],
            'negative': [description['negative']],
            'recommended': [description['recommended']]
        }
        return pd.DataFrame(data=data)
