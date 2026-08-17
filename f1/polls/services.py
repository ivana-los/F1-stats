
import requests

BASE_URL = "https://api.openf1.org/v1"

def get_drivers():
    response = requests.get(f"{BASE_URL}/drivers")
    return response.json()