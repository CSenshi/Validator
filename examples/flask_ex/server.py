# "Hacking" to see package of validaor (Not needed when pip installed)
from pathlib import Path
import sys, os

# add ../../ to path
validator_path = os.path.abspath(Path(os.path.abspath(__file__)).parent.parent.parent)
print(validator_path)
sys.path += [validator_path]

# real imports
from validator import Validator, validate, rules as R
from flask import Flask, url_for, request


app = Flask(__name__)


@app.route("/register/", methods=["GET"])
def register():
    val_request, rules = {}, {}

    val_request["first_name"] = request.args.get("first_name")
    val_request["last_name"] = request.args.get("last_name")
    val_request["age"] = request.args.get("age")
    val_request["mail"] = request.args.get("mail")

    rules["first_name"] = rules["last_name"] = [R.Required]
    rules["age"] = [R.Integer, R.Min(18), R.Max(30)]
    rules["mail"] = [R.Mail]

    result = validate(val_request, rules, True)

    return str(result)


if __name__ == "__main__":
    app.run()
