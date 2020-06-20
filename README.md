# Validator

Validator is a Python library for dealing with request validating.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Validator.

```bash
pip install validator
```

## Usage

User should pass request dictionary and rules dictionary for validating data in the request.

Please see examples below:

```python
from validator import validate

reqs = {"name": "Jon Doe",
        "age": 33,
        "mail": "jon_doe@gmail.com"}

rule = {"name": "required",
        "age": "integer|min:18",
        "mail": "required|mail"}

result = validate(request, rules)
# result is True
```
`valiadte()` returns either True or False.

Another option is to use `Validator` class
```python
from validator import Validator

reqs = {...}
rule = {...}

val = Validator(request, rules)
result = val.validate()
# result is True
```


### Error Messages
Validator allows user to have a look at failed validations

```python
from validator import validate

reqs = {"name": "",
        "mail": "jon_doe"}

rule = {"name": "required",
        "mail": "mail"}

result, errors = validate(reqs, rule, return_errors=True)

"""
result = True
errors = {'name': {'Required': 'Field was empty'},
          mail': {'Mail': 'Expected a Mail, Got: jon_doe'}}
"""
```

Or you can use `Validator` classfor error messages as well.

```python
val = Validator(request, rules)
result = val.validate()
errors = val.get_error_messages()
```

## Rules

Validator Rules can be used in different ways. Please see some examples below:

#### Strings

```python
rule = {"name": "required",
        "age": "integer|min:18",
        "mail": "required|mail"}
```
#### Array of Strings
```python
rule = {"name": ["required"],
        "age": ["integer", "min:18"],
        "mail": ["required", "mail"]}
```

#### Array of Rules
```python
from validator import rules as R

rules = {"name": [R.Required()],
        "age": [R.Integer(), R.Min(18)],
        "mail": [R.Requried(), R.Mail()]}
```

#### Other Miscellaneous
```python
from validator import rules as R

rules = {"name": R.Required(),           # no need for Array Brackets if one rule
        "age": [R.Integer, R.Min(18)],
        "mail": [R.Requried, R.Mail]}   # no need for class initialization with brakcets () 
                                        # if no arguments are passed to rule
```

#### *All of rules are listed in [RULES.md](RULES.md) file*

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please see [CONTRIBUTING.md](CONTRIBUTING.md) before making PR :)

## License
[MIT](https://choosealicense.com/licenses/mit/)
