import requests
from typing import Iterable
from leantechniques_demo.data import Photo

SERVICE_URL = 'https://jsonplaceholder.typicode.com/photos'

def get_photos(**params) -> Iterable[Photo]:
    r = requests.get(SERVICE_URL, params=params, timeout=5)
    ret = [Photo(**i) for i in r.json()]
    return ret