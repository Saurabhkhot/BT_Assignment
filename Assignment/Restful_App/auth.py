import requests
from config import TOKEN_URL
from logger import logger

def get_access_token():
    try:
        response = requests.post(TOKEN_URL, data = {
            "username": "admin",
            "password": "password123"
        }, verify=False)
        logger.info(f'Access Token created')
        return response.json()["token"]
    except Exception as e:
        raise e