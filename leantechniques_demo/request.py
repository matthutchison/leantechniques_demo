import requests
from typing import Iterable
from leantechniques_demo.data import Photo

SERVICE_URL = 'https://jsonplaceholder.typicode.com/photos'

def get_photos(**params) -> Iterable[Photo]:
    if 'id' in params and not params['id'].isdigit():
        raise ValueError('The Photo ID parameter should be an integer')
    if 'albumId' in params and not params['albumId'].isdigit():
        raise ValueError('The Album ID parameter should be an integer')
    r = requests.get(SERVICE_URL, params=params, timeout=5)
    ret = [Photo(**i) for i in r.json()]
    return ret