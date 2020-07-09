# "Hacking" to see package of validaor (Not needed when pip installed)
from pathlib import Path
import sys, os

# add ../../ to path
validator_path = os.path.abspath(Path(os.path.abspath(__file__)).parent.parent.parent)
sys.path += [validator_path]

# real imports
from validator import Validator, validate, rules as R
from flask import Flask, url_for, request
import json

app = Flask(__name__)


@app.route("/register-1", methods=["GET", "POST"])
def register_1():
    rules = {
        "first_name": "required",
        "last_name": "required",
        "age": "required|integer|between:18,30",
        "mail": "mail",
    }
    result = validate(request.values, rules, True)
    return json.dumps(result)


if __name__ == "__main__":
    app.run()
