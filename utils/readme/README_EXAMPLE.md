# Validator

Validator is a Python library for dealing with request validating.

## Installation (Not Released Yet)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Validator.

```bash
pip install validator
```

## Usage

```python
from validator import Validator


request = {
    "firstName": "Jon",
    "lastName": "Doe",
    "age": 33,
    "mail": "jon_doe@gmail.com",
}

rules = {
    "firstName": "required",
    "lastName": "required",
    "age": "required|min:18",
    "mail": "required|mail",
}

Validator(request, rules).validate()   # returns True

```

## Rules
<!-- CD4A678E95173E4BE5E27E2C8169F -->

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
