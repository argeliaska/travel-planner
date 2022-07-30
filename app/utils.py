import requests
import logging
from http import HTTPStatus
from requests.exceptions import HTTPError

def get_response(url: str=None, params: dict={}):
    try:
        response = requests.get(url, params=params)

        response.raise_for_status() 
    except HTTPError as http_err:
        print(f'HTTP error ocurred: {http_err}')
        logging.error(f'HTTP error ocurred: {http_err}')
        
    except Exception as exc:
        print(f'Error ocurred: {exc}')
        logging.error(f'Error ocurred: {exc}')
    else:
        if response.status_code == HTTPStatus.OK.value:
            return response.json()