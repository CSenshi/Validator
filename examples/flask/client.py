import requests as req
from pprint import pprint
import utils as U
import json

FLASK_SERVER_URL = "http://127.0.0.1:5000"


# Main Client Functions
def register_1_pass():
    U._log_prompt("1. GET Request With Valid Data")
    # Data to validate
    data = {
        "age": "23",
        "first_name": "John",
        "last_name": "Doe",
        "mail": "john.doe@gmail.com",
    }

    # Create URL on specific route
    URL = FLASK_SERVER_URL + "/register?"
    params = "&".join(f"{key}={data[key]}" for key in data)
    # Append URL and parameters
    URL += params

    # Do GET request
    U._log_paragraph("Sent GET Request to:")
    print(URL)
    resp = req.get(URL)
    U._log_pass("\nReceived Response:")
    pprint(json.loads(resp.text))


def register_2_pass():
    U._log_prompt("2. POST Request With Valid Data")
    # Data to validate
    data = {
        "age": "23",
        "first_name": "John",
        "last_name": "Doe",
        "mail": "john.doe@gmail.com",
    }

    # Create URL on specific route
    URL = FLASK_SERVER_URL + "/register"

    # Do POST request
    U._log_paragraph("Sent GET Request to:")
    print(URL)
    U._log_paragraph("Sent Data: ")
    pprint(data)
    resp = req.post(URL, data=data)
    U._log_pass("\nReceived Response:")
    pprint(json.loads(resp.text))


def register_3_fail():
    U._log_prompt("3. GET Request With Invalid Data")
    # Data to validate
    data = {
        "age": "23",
        "first_name": "",
        "last_name": "Doe",
        "mail": "",
    }

    # Create URL on specific route
    URL = FLASK_SERVER_URL + "/register?"
    params = "&".join(f"{key}={data[key]}" for key in data)
    # Append URL and parameters
    URL += params

    # Do GET request
    U._log_paragraph("Sent GET Request to:")
    print(URL)
    resp = req.get(URL)
    U._log_fail("\nReceived Response:")
    pprint(json.loads(resp.text))


def register_4_fail():
    U._log_prompt("4. POST Request With Invalid Data")
    # Data to validate
    data = {
        "age": "13",
        "first_name": "John",
        "last_name": "Doe",
        "mail": "john.doe",
    }

    # Create URL on specific route
    URL = FLASK_SERVER_URL + "/register"

    # Do POST request
    U._log_paragraph("Sent POST Request to:")
    print(URL)
    U._log_paragraph("Sent Data: ")
    pprint(data)
    resp = req.post(URL, data=data)
    U._log_fail("\nReceived Response:")
    pprint(json.loads(resp.text))


register_1_pass()
register_2_pass()
register_3_fail()
register_4_fail()
