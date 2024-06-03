import os

API_BASE_URL = os.getenv('API_BASE_URL', "https://restful-booker.herokuapp.com")
TOKEN_URL  = os.getenv("TOKEN_URL", "https://restful-booker.herokuapp.com/auth")