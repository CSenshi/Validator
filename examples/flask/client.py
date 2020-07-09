import requests as req
from pprint import pprint
import json

FLASK_SERVER_URL = "http://127.0.0.1:5000"


def register_1_pass():
    # Data to validate
    data = {
        "age": "23",
        "first_name": "Jon",
        "last_name": "Doe",
        "mail": "jon.doe@gmail.com",
    }

    # Create URL on specific route
    URL = FLASK_SERVER_URL + "/register-1?"
    params = "&".join(f"{key}={data[key]}" for key in data)
    # Append URL and parameters
    URL += params

    # Do GET request
    print("Sent GET Request to :")
    print(URL)
    resp = req.get(URL)
    print("\nReceived Response:")
    pprint(json.loads(resp.text))


def register_2_pass():
    # Data to validate
    data = {
        "age": "23",
        "first_name": "Jon",
        "last_name": "Doe",
        "mail": "jon.doe@gmail.com",
    }

    # Create URL on specific route
    URL = FLASK_SERVER_URL + "/register-1"

    # Do POST request
    print("Sent GET Request to :")
    print(URL)
    resp = req.post(URL, data=data)
    print("\nReceived Response:")
    pprint(json.loads(resp.text))


register_1_pass()
register_2_pass()
